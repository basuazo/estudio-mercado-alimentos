#!/usr/bin/env python3
"""
Resume la captura manual de la Biblioteca de anuncios de Meta (Chile, anuncios activos).

Uso (desde la raíz del repositorio):
    python scripts/resumir_meta_ads.py              # usa la captura más reciente
    python scripts/resumir_meta_ads.py 2026-10-25   # una fecha en particular

Entrada:
    datos/crudos/AAAA-MM-DD_meta-ads-library_cl_captura.csv   (se crea con: python scripts/preparar_captura.py meta)
    Una fila por (palabra clave, anunciante). El total "resultados_activos_aprox" basta en una fila por palabra.

Salidas:
    datos/limpios/AAAA-MM-DD_meta-ads_resumen-palabras.csv   (por palabra clave; compara con la captura anterior)
    datos/limpios/AAAA-MM-DD_meta-ads_anunciantes.csv        (por anunciante; marca si es nuevo)

Reglas:
    - Lo que no se anotó queda vacío, nunca en cero.
    - Números aceptados: 2800, 2.800, ~2.800, "2,8 mil", "+1000". Fechas: 2025-01-29, 29-01-2025, "29 ene 2025".
    - Los conteos son un piso (Meta muestra aproximados) y cuentan como UNA fuente para la regla de 3.
"""
import csv
import re
import sys
import unicodedata
from collections import OrderedDict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CRUDOS = RAIZ / "datos" / "crudos"
LIMPIOS = RAIZ / "datos" / "limpios"
PATRON = "_meta-ads-library_cl_captura.csv"
MESES = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6, "jul": 7, "ago": 8,
         "sep": 9, "set": 9, "oct": 10, "nov": 11, "dic": 12}


def norm(s):
    return unicodedata.normalize("NFD", (s or "").strip().lower()).encode("ascii", "ignore").decode()


def numero(x):
    t = norm(x).replace("~", "").replace("+", "").replace("aprox", "").replace("resultados", "").strip()
    if not t:
        return None
    mil = 1
    if re.search(r"\b(mil|k)\b", t):
        mil, t = 1000, re.sub(r"\b(mil|k)\b", "", t).strip()
    t = t.replace(" ", "")
    if mil == 1000:
        t = t.replace(",", ".")
    elif re.fullmatch(r"\d{1,3}([.,]\d{3})+", t):
        t = re.sub(r"[.,]", "", t)
    try:
        return int(round(float(t) * mil))
    except ValueError:
        return None


def fecha(x):
    t = norm(x)
    if not t:
        return ""
    m = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})", t)
    if m:
        return f"{m[1]}-{int(m[2]):02d}-{int(m[3]):02d}"
    m = re.search(r"(\d{1,2})[-/](\d{1,2})[-/](\d{4})", t)
    if m:
        return f"{m[3]}-{int(m[2]):02d}-{int(m[1]):02d}"
    m = re.search(r"(\d{1,2})\s*(?:de\s+)?([a-z]{3})[a-z]*\.?\s*(?:de\s+)?(\d{4})", t)
    if m and m[2] in MESES:
        return f"{m[3]}-{MESES[m[2]]:02d}-{int(m[1]):02d}"
    return "por confirmar: " + x.strip()


def si_no(x):
    t = norm(x)
    return "si" if t in ("si", "s", "x", "1", "yes") else ("no" if t in ("no", "n", "0") else "")


def leer(ruta):
    filas = []
    with open(ruta, encoding="utf-8-sig") as fh:
        texto = fh.read()
    sep = ";" if texto.splitlines()[0].count(";") > texto.splitlines()[0].count(",") else ","
    for f in csv.DictReader(texto.splitlines(), delimiter=sep):
        f = {norm(k): (v or "").strip() for k, v in f.items() if k}
        if f.get("palabra_clave"):
            filas.append(f)
    return filas


def capturas():
    return sorted(p for p in CRUDOS.glob(f"*{PATRON}") if re.match(r"\d{4}-\d{2}-\d{2}_", p.name))


def resumir(filas):
    palabras, anunciantes = OrderedDict(), OrderedDict()
    for f in filas:
        clave = norm(f["palabra_clave"])
        p = palabras.setdefault(clave, {"palabra_clave": f["palabra_clave"], "tipo_busqueda": f.get("tipo_busqueda", ""),
                                        "resultados": None, "anunciantes": [], "alimento": 0})
        n = numero(f.get("resultados_activos_aprox"))
        if n is not None:
            p["resultados"] = max(p["resultados"] or 0, n)
        nombre = f.get("anunciante", "")
        if not nombre:
            continue
        anuncios = numero(f.get("anuncios_del_anunciante"))
        p["anunciantes"].append((nombre, anuncios))
        if si_no(f.get("es_alimento_o_bebida")) == "si":
            p["alimento"] += 1
        a = anunciantes.setdefault(norm(nombre), {"anunciante": nombre, "palabras": [], "anuncios": None,
                                                   "antiguo": "", "producto": "", "mensaje": "", "alimento": ""})
        if f["palabra_clave"] not in a["palabras"]:
            a["palabras"].append(f["palabra_clave"])
        if anuncios is not None:
            a["anuncios"] = max(a["anuncios"] or 0, anuncios)
        fa = fecha(f.get("anuncio_mas_antiguo"))
        if fa and (not a["antiguo"] or (fa < a["antiguo"] and not fa.startswith("por"))):
            a["antiguo"] = fa
        for campo, col in (("producto", "producto_pautado"), ("mensaje", "mensaje_principal")):
            a[campo] = a[campo] or f.get(col, "")
        a["alimento"] = a["alimento"] or si_no(f.get("es_alimento_o_bebida"))
    return palabras, anunciantes


def escribir(nombre, filas, columnas):
    LIMPIOS.mkdir(parents=True, exist_ok=True)
    with open(LIMPIOS / nombre, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=columnas)
        w.writeheader()
        w.writerows(filas)
    print(f"  escrito: datos/limpios/{nombre} ({len(filas)} filas)")


def main():
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass
    todas = capturas()
    if not todas:
        sys.exit("No hay capturas. Primero: python scripts/preparar_captura.py meta")
    if len(sys.argv) > 1:
        sel = [p for p in todas if p.name.startswith(sys.argv[1])]
        if not sel:
            sys.exit(f"No existe datos/crudos/{sys.argv[1]}{PATRON}")
        actual = sel[0]
    else:
        actual = todas[-1]
    dia = actual.name[:10]
    previas = [p for p in todas if p.name[:10] < dia]
    filas = leer(actual)
    if not filas:
        sys.exit(f"{actual.name} no tiene filas con palabra_clave.")
    palabras, anunciantes = resumir(filas)
    ant_p, ant_a = ({}, {}) if not previas else resumir(leer(previas[-1]))
    vistos_antes = set()
    for p in previas:
        vistos_antes |= set(resumir(leer(p))[1])
    ref = previas[-1].name[:10] if previas else ""

    print(f"\nCaptura de Meta del {dia}" + (f" (se compara con {ref})" if ref else " (primera captura, sin comparación)"))
    salida_p = []
    for clave, p in palabras.items():
        top = sorted(p["anunciantes"], key=lambda x: -(x[1] or 0))[:5]
        antes = ant_p.get(clave, {}).get("resultados")
        var = ""
        if p["resultados"] is not None and antes:
            var = round((p["resultados"] - antes) / antes * 100)
        salida_p.append({
            "fecha": dia, "palabra_clave": p["palabra_clave"], "tipo_busqueda": p["tipo_busqueda"],
            "resultados_activos_aprox": "" if p["resultados"] is None else p["resultados"],
            "anunciantes_anotados": len(p["anunciantes"]), "anunciantes_alimento_o_bebida": p["alimento"],
            "principales_anunciantes": "; ".join(f"{n} ({a})" if a is not None else n for n, a in top),
            "resultados_captura_anterior": "" if antes is None else antes, "fecha_captura_anterior": ref,
            "variacion_pct": var})
    escribir(f"{dia}_meta-ads_resumen-palabras.csv", salida_p, list(salida_p[0].keys()))

    salida_a = []
    for clave, a in anunciantes.items():
        salida_a.append({
            "fecha": dia, "anunciante": a["anunciante"], "palabras_clave": "; ".join(a["palabras"]),
            "n_palabras": len(a["palabras"]), "anuncios_activos_max": "" if a["anuncios"] is None else a["anuncios"],
            "anuncio_mas_antiguo": a["antiguo"], "producto_pautado": a["producto"], "mensaje_principal": a["mensaje"],
            "es_alimento_o_bebida": a["alimento"],
            "nuevo_vs_capturas_anteriores": ("si" if clave not in vistos_antes else "no") if previas else ""})
    salida_a.sort(key=lambda d: (-(d["n_palabras"]), -(d["anuncios_activos_max"] or 0), d["anunciante"]))
    if salida_a:
        escribir(f"{dia}_meta-ads_anunciantes.csv", salida_a, list(salida_a[0].keys()))

    print("\nPalabra clave                  resultados  anunciantes  variación")
    for d in sorted(salida_p, key=lambda d: -(d["resultados_activos_aprox"] or 0)):
        v = f"{d['variacion_pct']:+d} %" if d["variacion_pct"] != "" else ""
        print(f"  {d['palabra_clave'][:28]:28} {str(d['resultados_activos_aprox']):>10}  {d['anunciantes_anotados']:>11}  {v}")
    faltan = [d["palabra_clave"] for d in salida_p if d["resultados_activos_aprox"] == ""]
    if faltan:
        print("\nOjo, sin total de resultados: " + ", ".join(faltan))
    raras = [a["anuncio_mas_antiguo"] for a in salida_a if str(a["anuncio_mas_antiguo"]).startswith("por confirmar")]
    if raras:
        print("Fechas que no se entendieron (revisar): " + ", ".join(raras))
    nuevos = [a["anunciante"] for a in salida_a if a["nuevo_vs_capturas_anteriores"] == "si"]
    if nuevos:
        print("Anunciantes nuevos: " + ", ".join(nuevos))


if __name__ == "__main__":
    main()
