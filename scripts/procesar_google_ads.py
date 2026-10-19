#!/usr/bin/env python3
"""
Limpia una o varias exportaciones del Planificador de palabras clave de Google Ads (cualquier idioma de la
interfaz, UTF-16 con tabulaciones o CSV normal) y las deja en una sola tabla.

Uso (desde la raíz del repositorio):
    python scripts/procesar_google_ads.py                         # todas las exportaciones de la fecha más reciente
    python scripts/procesar_google_ads.py 2026-10-25              # las de esa fecha
    python scripts/procesar_google_ads.py datos/crudos/archivo.csv [otro.csv ...]

Entrada:  datos/crudos/AAAA-MM-DD_google-ads_*.csv   (tal como los descarga Google Ads; no se editan)
Salida:   datos/limpios/AAAA-MM-DD_google-ads_limpio.csv
          una fila por término: búsquedas/mes, cambio 3 meses e interanual, competencia, CPC, mes más alto,
          y si el término ya está en el diccionario del estudio (datos/referencia/google-ads_terminos.csv).

Ojo: sin campañas con gasto, Google entrega volúmenes por nivel (50 / 500 / 5.000 / 50.000). Sirven para
ordenar, no para sumar. Lo que no viene queda vacío, nunca en cero.
"""
import csv
import io
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CRUDOS = RAIZ / "datos" / "crudos"
LIMPIOS = RAIZ / "datos" / "limpios"
REFERENCIA = RAIZ / "datos" / "referencia"

# nombre interno -> encabezados posibles (normalizados: minúsculas, sin tildes)
COLUMNAS = {
    "termino": ["keyword", "palabra clave"],
    "busquedas": ["avg. monthly searches", "promedio de busquedas mensuales", "busquedas mensuales promedio"],
    "cambio_3m": ["three month change", "cambio en tres meses", "cambio en 3 meses"],
    "cambio_anual": ["yoy change", "cambio interanual"],
    "competencia": ["competition", "competencia"],
    "indice_competencia": ["competition (indexed value)", "competencia (valor indexado)"],
    "cpc_bajo": ["top of page bid (low range)", "puja por la parte superior de la pagina (intervalo bajo)",
                 "puja por la parte superior de la pagina (rango bajo)"],
    "cpc_alto": ["top of page bid (high range)", "puja por la parte superior de la pagina (intervalo alto)",
                 "puja por la parte superior de la pagina (rango alto)"],
    "moneda": ["currency", "moneda"],
}
COMPETENCIA = {"high": "Alta", "alta": "Alta", "medium": "Media", "media": "Media", "low": "Baja", "baja": "Baja"}


def norm(s):
    return unicodedata.normalize("NFD", (s or "").strip().lower()).encode("ascii", "ignore").decode()


def numero(x):
    t = (x or "").strip().replace("\xa0", "").replace(" ", "")
    if not t or t in ("-", "--"):
        return None
    if "," in t and "." in t:
        t = t.replace(".", "").replace(",", ".") if t.rfind(",") > t.rfind(".") else t.replace(",", "")
    elif re.fullmatch(r"\d{1,3}(\.\d{3})+", t):
        t = t.replace(".", "")
    else:
        t = t.replace(",", ".")
    try:
        return float(t)
    except ValueError:
        return None


def entero(x):
    n = numero(x)
    return "" if n is None else int(round(n))


def porcentaje(x):
    n = numero((x or "").replace("%", ""))
    return "" if n is None else int(round(n))


def leer_texto(ruta):
    crudo = ruta.read_bytes()
    if crudo[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return crudo.decode("utf-16")
    for enc in ("utf-8-sig", "cp1252"):
        try:
            return crudo.decode(enc)
        except UnicodeDecodeError:
            pass
    return crudo.decode("latin-1")


def leer_exportacion(ruta):
    lineas = leer_texto(ruta).splitlines()
    inicio = next((i for i, l in enumerate(lineas) if norm(re.split(r"[\t,;]", l)[0].strip('"')) in COLUMNAS["termino"]), None)
    if inicio is None:
        if any(x in norm(lineas[0]) for x in ("estimated clicks", "clics estimados", "campaign", "campana")):
            print(f"  ! {ruta.name}: es la descarga de PREVISIONES (clics estimados), no de volúmenes. Se omite.")
            print("    En el planificador, descarga desde la pestaña 'Métricas históricas' / 'Historical metrics'.")
            return []
        print(f"  ! {ruta.name}: no encontré la columna Keyword / Palabra clave. ¿Es una exportación del planificador?")
        return []
    cab = lineas[inicio]
    sep = "\t" if "\t" in cab else (";" if cab.count(";") > cab.count(",") else ",")
    lector = csv.reader(io.StringIO("\n".join(lineas[inicio:])), delimiter=sep)
    encabezados = [norm(h) for h in next(lector)]
    pos = {}
    for interno, opciones in COLUMNAS.items():
        for i, h in enumerate(encabezados):
            if h in opciones:
                pos[interno] = i
                break
    meses = [(i, h.split(":", 1)[1].strip()) for i, h in enumerate(encabezados)
             if h.startswith("searches:") or h.startswith("busquedas:")]
    filas = []
    for r in lector:
        def v(c):
            return r[pos[c]] if c in pos and pos[c] < len(r) else ""
        termino = v("termino").strip()
        if not termino:
            continue  # fila de totales
        serie = [(m, numero(r[i]) if i < len(r) else None) for i, m in meses]
        serie = [(m, n) for m, n in serie if n is not None]
        mes_max = max(serie, key=lambda x: x[1])[0] if serie else ""
        mn = min((n for _, n in serie), default=None)
        mx = max((n for _, n in serie), default=None)
        filas.append({
            "termino": termino,
            "busquedas_mes_chile": entero(v("busquedas")),
            "cambio_3m_pct": porcentaje(v("cambio_3m")),
            "cambio_interanual_pct": porcentaje(v("cambio_anual")),
            "competencia": COMPETENCIA.get(norm(v("competencia")), v("competencia")),
            "indice_competencia": entero(v("indice_competencia")),
            "cpc_bajo": entero(v("cpc_bajo")),
            "cpc_alto": entero(v("cpc_alto")),
            "moneda": v("moneda") or "CLP",
            "mes_mas_alto": mes_max,
            "max_sobre_min": round(mx / mn, 1) if mn else "",
            "archivo_origen": ruta.name,
        })
    return filas


def diccionario():
    dic = {}
    for nombre in ("google-ads_terminos.csv", "terminos-busqueda.csv"):
        ruta = REFERENCIA / nombre
        if not ruta.exists():
            continue
        for f in csv.DictReader(open(ruta, encoding="utf-8-sig")):
            t = norm(f.get("termino"))
            if t and t not in dic:
                dic[t] = f.get("oportunidad") or f.get("categoria") or ""
    return dic


def elegir_archivos(args):
    if args and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args[0]):
        rutas = [Path(a) if Path(a).is_absolute() else (Path.cwd() / a) for a in args]
        faltan = [str(r) for r in rutas if not r.exists()]
        if faltan:
            sys.exit("No existen: " + ", ".join(faltan))
        return rutas
    todos = sorted(p for p in CRUDOS.glob("*_google-ads_*.csv") if re.match(r"\d{4}-\d{2}-\d{2}_", p.name))
    if not todos:
        sys.exit("No hay exportaciones en datos/crudos/ (deben llamarse AAAA-MM-DD_google-ads_<algo>.csv)")
    dia = args[0] if args else todos[-1].name[:10]
    sel = [p for p in todos if p.name.startswith(dia)]
    if not sel:
        sys.exit(f"No hay exportaciones del {dia} en datos/crudos/")
    return sel


def main():
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass
    archivos = elegir_archivos(sys.argv[1:])
    dia = max((re.match(r"\d{4}-\d{2}-\d{2}", a.name) or [""])[0] for a in archivos) or "sin-fecha"
    dic = diccionario()
    unicos = {}
    for a in archivos:
        filas = leer_exportacion(a)
        print(f"  leído: {a.name} ({len(filas)} términos)")
        for f in filas:
            clave = norm(f["termino"])
            if clave in unicos:
                if a.name not in unicos[clave]["archivo_origen"]:
                    unicos[clave]["archivo_origen"] += "; " + a.name
                continue
            f["en_diccionario"] = "si" if clave in dic else "no"
            f["oportunidad_o_categoria"] = dic.get(clave, "")
            unicos[clave] = f
    if not unicos:
        sys.exit("No salió ningún término. Revisa que el archivo sea la descarga CSV del planificador.")
    salida = sorted(unicos.values(), key=lambda f: (-(f["busquedas_mes_chile"] or 0), f["termino"]))
    LIMPIOS.mkdir(parents=True, exist_ok=True)
    destino = LIMPIOS / f"{dia}_google-ads_limpio.csv"
    with open(destino, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(salida[0].keys()))
        w.writeheader()
        w.writerows(salida)
    print(f"\n  escrito: datos/limpios/{destino.name} ({len(salida)} términos únicos)\n")
    print("  Top 15 por búsquedas mensuales")
    for f in salida[:15]:
        print(f"    {f['termino'][:38]:38} {str(f['busquedas_mes_chile']):>8}  {f['competencia']:6} CPC alto {f['cpc_alto']}")
    nuevos = [f["termino"] for f in salida if f["en_diccionario"] == "no" and (f["busquedas_mes_chile"] or 0) >= 500]
    if nuevos:
        print(f"\n  {len(nuevos)} términos con 500+ búsquedas que no están en el diccionario (pásalos al agente para clasificar):")
        print("    " + ", ".join(nuevos[:30]) + (" ..." if len(nuevos) > 30 else ""))


if __name__ == "__main__":
    main()
