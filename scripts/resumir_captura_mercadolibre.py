"""
Resume la captura manual de Mercado Libre (pauta: datos/referencia/pauta-captura-mercadolibre.md).

Uso (desde la raíz del repositorio):
    python scripts/resumir_captura_mercadolibre.py            # usa la fecha de captura más reciente
    python scripts/resumir_captura_mercadolibre.py 2026-10-18 # una fecha específica

Entrada:  datos/crudos/AAAA-MM-DD_mercadolibre_cl_<termino>.csv (columnas de plantilla_mercadolibre_cl.csv)
Salida:   datos/limpios/AAAA-MM-DD_mercadolibre_cl_captura.csv  (todas las filas, con precio por unidad calculado)
          datos/limpios/AAAA-MM-DD_mercadolibre_cl_resumen.csv  (una fila por término)

Cómo escribir la columna "formato" para que el cálculo funcione (ejemplos):
    "30 sobres"   "12 x 250 ml"   "1 l"   "500 ml"   "400 g"   "6 x 330 ml"   "20 porciones"
Si "precio_por_porcion_o_litro" viene vacío, se calcula: CLP por litro (líquidos), por kilo (sólidos)
o por unidad/porción (sobres, cápsulas, porciones). Si ya viene escrito, se respeta.
"""
import csv
import glob
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def numero(texto):
    t = re.sub(r"[^\d,\.]", "", str(texto or ""))
    if not t:
        return None
    t = t.replace(".", "").replace(",", ".") if re.search(r"\.\d{3}(\D|$)", t) or "," in t else t
    try:
        return float(t)
    except ValueError:
        return None


def precio_unitario(precio, formato):
    """Devuelve (valor, unidad) o (None, '')."""
    if not precio or not formato:
        return None, ""
    f = formato.lower().replace(",", ".")
    mult = 1.0
    m = re.match(r"\s*(\d+)\s*x\s*(.*)", f)
    if m:
        mult, f = float(m.group(1)), m.group(2)
    m = re.search(r"(\d+(?:\.\d+)?)\s*(ml|cc|l|lt|litros?|g|gr|grs|kg|kilos?|sobres?|sticks?|c[aá]psulas?|porci[oó]n(?:es)?|unidades?|u|tabletas?)\b", f)
    if not m:
        return None, ""
    cant, uni = float(m.group(1)) * mult, m.group(2)
    if uni in ("ml", "cc"):
        return round(precio / (cant / 1000)), "CLP/litro"
    if uni in ("l", "lt", "litro", "litros"):
        return round(precio / cant), "CLP/litro"
    if uni in ("g", "gr", "grs"):
        return round(precio / (cant / 1000)), "CLP/kilo"
    if uni in ("kg", "kilo", "kilos"):
        return round(precio / cant), "CLP/kilo"
    return round(precio / cant), "CLP/unidad o porcion"


def vendidos_min(texto):
    """'+100 vendidos' -> 100; '+1000' -> 1000; '+5mil' -> 5000."""
    t = str(texto or "").lower()
    m = re.search(r"(\d+(?:[\.,]\d+)?)\s*(mil)?", t)
    if not m:
        return None
    v = float(m.group(1).replace(".", "").replace(",", "."))
    return int(v * 1000) if m.group(2) else int(v)


def main():
    archivos = sorted(glob.glob(str(RAIZ / "datos" / "crudos" / "*_mercadolibre_cl_*.csv")))
    archivos = [a for a in archivos if "plantilla" not in a]
    if not archivos:
        sys.exit("No hay capturas en datos/crudos/ (AAAA-MM-DD_mercadolibre_cl_<termino>.csv).")
    fecha = sys.argv[1] if len(sys.argv) > 1 else max(Path(a).name[:10] for a in archivos)
    archivos = [a for a in archivos if Path(a).name.startswith(fecha)]

    filas = []
    for a in archivos:
        for f in csv.DictReader(open(a, encoding="utf-8-sig")):
            if not any((v or "").strip() for v in f.values()):
                continue
            precio = numero(f.get("precio_clp"))
            pu, unidad = precio_unitario(precio, f.get("formato"))
            if (f.get("precio_por_porcion_o_litro") or "").strip():
                pu, unidad = numero(f["precio_por_porcion_o_litro"]), "informado a mano"
            f["precio_clp_num"] = precio or ""
            f["precio_unitario_calc"] = pu or ""
            f["unidad_precio"] = unidad
            f["vendidos_min"] = vendidos_min(f.get("vendidos_visibles")) or ""
            f["archivo"] = Path(a).name
            filas.append(f)
    if not filas:
        sys.exit(f"Las capturas del {fecha} están vacías.")

    cols = list(filas[0].keys())
    out = RAIZ / "datos" / "limpios" / f"{fecha}_mercadolibre_cl_captura.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)

    resumen = []
    for termino in dict.fromkeys(f["termino"] for f in filas):
        g = [f for f in filas if f["termino"] == termino]
        precios = [f["precio_clp_num"] for f in g if f["precio_clp_num"]]
        unidades = Counter(f["unidad_precio"] for f in g if f["precio_unitario_calc"])
        u = unidades.most_common(1)[0][0] if unidades else ""
        pus = [f["precio_unitario_calc"] for f in g if f["precio_unitario_calc"] and f["unidad_precio"] == u]
        vend = [f for f in g if f["vendidos_min"] != ""]
        top = sorted(vend, key=lambda f: -f["vendidos_min"])[:5]
        marcas = Counter((f.get("marca") or "").strip() for f in g if (f.get("marca") or "").strip())
        resumen.append({
            "fecha_captura": fecha,
            "termino": termino,
            "publicaciones": len(g),
            "marcas_distintas": len(marcas),
            "vendedores_distintos": len({(f.get("vendedor") or "").strip() for f in g if (f.get("vendedor") or "").strip()}),
            "tiendas_oficiales": sum((f.get("tienda_oficial") or "").strip().lower() in ("si", "sí", "1", "true") for f in g),
            "publicaciones_100_o_mas_vendidos": sum(f["vendidos_min"] != "" and f["vendidos_min"] >= 100 for f in g),
            "precio_mediana_clp": round(statistics.median(precios)) if precios else "",
            "precio_unitario_mediana": round(statistics.median(pus)) if pus else "",
            "precio_unitario_min": min(pus) if pus else "",
            "precio_unitario_max": max(pus) if pus else "",
            "unidad_precio": u,
            "envio_gratis_pct": round(100 * sum((f.get("envio_gratis") or "").strip().lower() in ("si", "sí", "1", "true") for f in g) / len(g)),
            "marcas_principales": " | ".join(f"{m} ({n})" for m, n in marcas.most_common(5)),
            "mas_vendidos": " | ".join(f"{(f.get('marca') or f.get('titulo') or '')[:30]} (+{f['vendidos_min']})" for f in top),
        })
    out_r = RAIZ / "datos" / "limpios" / f"{fecha}_mercadolibre_cl_resumen.csv"
    with out_r.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(resumen[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(resumen)
    print(f"Guardado: {out.relative_to(RAIZ)} ({len(filas)} publicaciones)")
    print(f"Guardado: {out_r.relative_to(RAIZ)} ({len(resumen)} términos)")
    sin = sum(1 for f in filas if f["precio_clp_num"] and not f["precio_unitario_calc"])
    if sin:
        print(f"Atención: {sin} filas con precio pero sin formato reconocible; revisa la columna 'formato'.")


if __name__ == "__main__":
    main()
