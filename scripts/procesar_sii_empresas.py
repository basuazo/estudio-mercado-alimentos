"""
Procesa las bases del SII para el estudio de mercado de alimentos (paso A4 del plan).

Uso (desde la raíz del repositorio):
    python scripts/procesar_sii_empresas.py                                   # busca los .zip en datos/crudos/sii/
    python scripts/procesar_sii_empresas.py RUTA/EMPRESAS.zip RUTA/PUB_EMPRESAS_PJ_2020_A_2024.zip

Entradas (descarga manual desde sii.cl; los .zip no se suben al repositorio):
    EMPRESAS.zip                     https://www.sii.cl/sobre_el_sii/empresas/EMPRESAS.zip
    PUB_EMPRESAS_PJ_2020_A_2024.zip  https://www.sii.cl/estadisticas/nominas/PUB_EMPRESAS_PJ_2020_A_2024.zip
Salidas en datos/limpios/ (prefijo con la fecha de proceso):
    _sii_alimentos_nacional.csv     N° de empresas, ventas (UF) y trabajadores por actividad, 2015–2024
    _sii_alimentos_region.csv       Lo mismo para Ñuble y Región Metropolitana
    _sii_alimentos_resumen.csv      Una fila por actividad: 2019 vs 2024, ventas por empresa, peso de Ñuble
    _sii_nuble_elaboracion_pj.csv   Personas jurídicas vigentes de Ñuble que elaboran alimentos o bebidas (año 2024)
    _sii_posibles-maquiladores_pj.csv  Personas jurídicas vigentes del país, pequeñas o más grandes, en bebidas
                                       no alcohólicas, té y café, comidas preparadas y otros alimentos n.c.p.
Notas: las listas de empresas excluyen las EIRL (su razón social suele ser el nombre de una persona) y no
incluyen RUT, siguiendo la regla del repositorio de no guardar datos personales de terceros.
"*" en la fuente = dato reservado por el SII (queda vacío). Las nóminas solo traen personas jurídicas
(no personas naturales con giro), así que cuentan menos empresas que las estadísticas agregadas.
Requisitos: Python 3.9+, sin librerías externas.
"""
import csv
import glob
import io
import sys
import unicodedata
import zipfile
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "datos" / "limpios"
HOY = date.today().isoformat()
ANIO_DESDE = 2015

# Actividades (CIIU4.CL, 6 dígitos, confirmadas contra PUB_ACT del SII, act. nov-2025)
ACTIVIDADES = {
    "103000": "elaboracion", "105000": "elaboracion", "106109": "elaboracion", "107100": "elaboracion",
    "107300": "elaboracion", "107500": "elaboracion", "107901": "elaboracion", "107909": "elaboracion",
    "110401": "elaboracion", "110402": "elaboracion",
    "463014": "comercio_mayorista", "463019": "comercio_mayorista", "463020": "comercio_mayorista",
    "469000": "comercio_mayorista",
    "471100": "comercio_minorista", "472101": "comercio_minorista", "472109": "comercio_minorista",
    "472200": "comercio_minorista",
}
MAQUILA = {"110401", "107901", "107500", "107909"}
REGIONES = {"NUBLE": "Ñuble", "METROPOLITANA": "Región Metropolitana"}
TRAMOS = {  # tramos de ventas del SII (13 tramos, UF anuales)
    "1": "sin ventas", "2": "micro 1", "3": "micro 2", "4": "micro 3", "5": "pequeña 1", "6": "pequeña 2",
    "7": "pequeña 3", "8": "mediana 1", "9": "mediana 2", "10": "grande 1", "11": "grande 2",
    "12": "grande 3", "13": "grande 4",
}


def norm(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode()
    return " ".join(t.upper().split())


def lineas(z, nombre):
    """Lee un .txt del zip probando UTF-8 y, si falla, Latin-1 (el SII mezcla ambos)."""
    crudo = z.read(nombre)
    try:
        texto = crudo.decode("utf-8")
    except UnicodeDecodeError:
        texto = crudo.decode("latin-1")
    for l in io.StringIO(texto):
        c = l.rstrip("\r\n").split("\t")
        if any(x.strip() for x in c):
            yield c


def num(x, flotante):
    x = (x or "").strip()
    if not x or x == "*":
        return None
    try:
        return float(x) if flotante else float(x.replace(".", "").replace(",", "."))
    except ValueError:
        return None


def entero(v):
    return "" if v is None else int(round(v))


def nacional(z):
    filas, nombres = [], {}
    for c in lineas(z, "PUB_ACT.txt"):
        if not c[0].isdigit():
            continue
        anio, codigo = int(c[0]), c[1][:6]
        if codigo in ACTIVIDADES and anio >= ANIO_DESDE:
            nombres[codigo] = c[1][9:]
            filas.append({"anio": anio, "codigo": codigo, "actividad": c[1][9:], "grupo": ACTIVIDADES[codigo],
                          "n_empresas": entero(num(c[4], False)), "ventas_uf": entero(num(c[5], False)),
                          "trabajadores": entero(num(c[6], False)), "fuente": "SII EMPRESAS.zip / PUB_ACT.txt"})
    return filas, nombres


def regional(z):
    filas = []
    for c in lineas(z, "PUB_REG_ACT.txt"):
        if not c[0][:4].isdigit():
            continue
        anio, codigo = int(float(c[0])), c[2][:6]
        reg = next((v for k, v in REGIONES.items() if k in norm(c[1])), None)
        if reg and codigo in ACTIVIDADES and anio >= ANIO_DESDE:
            filas.append({"anio": anio, "region": reg, "codigo": codigo, "actividad": c[2][9:],
                          "grupo": ACTIVIDADES[codigo], "n_empresas": entero(num(c[5], True)),
                          "ventas_uf": entero(num(c[6], True)), "trabajadores": entero(num(c[7], True)),
                          "fuente": "SII EMPRESAS.zip / PUB_REG_ACT.txt"})
    return filas


def resumen(nac, reg, nombres):
    idx = {(f["codigo"], f["anio"]): f for f in nac}
    idr = {(f["codigo"], f["region"], f["anio"]): f for f in reg}
    out = []
    for cod, nombre in nombres.items():
        a, b = idx.get((cod, 2019), {}), idx.get((cod, 2024), {})
        e19, e24 = a.get("n_empresas"), b.get("n_empresas")
        v24 = b.get("ventas_uf")
        nu = idr.get((cod, "Ñuble", 2024), {}).get("n_empresas")
        rm = idr.get((cod, "Región Metropolitana", 2024), {}).get("n_empresas")
        out.append({
            "codigo": cod, "actividad": nombre, "grupo": ACTIVIDADES[cod],
            "empresas_2019": e19, "empresas_2024": e24,
            "var_empresas_2019_2024_pct": round(100 * (e24 / e19 - 1)) if e19 and e24 else "",
            "ventas_uf_2024": v24,
            "ventas_uf_por_empresa_2024": round(v24 / e24) if v24 and e24 else "",
            "empresas_nuble_2024": nu, "pct_nuble": round(100 * nu / e24, 1) if nu and e24 else "",
            "empresas_rm_2024": rm, "pct_rm": round(100 * rm / e24, 1) if rm and e24 else "",
        })
    return out


def nominas(zpj, nombres):
    objetivo = {norm(n): c for c, n in nombres.items()}
    archivo = sorted(n for n in zpj.namelist() if n.endswith(".txt"))[-1]  # año más reciente
    nuble, maquila = [], []
    for c in lineas(zpj, archivo):
        if not c[0].isdigit() or len(c) < 20:
            continue
        cod = objetivo.get(norm(c[16]))
        if not cod or ACTIVIDADES[cod] != "elaboracion" or c[7].strip():  # con término de giro
            continue
        if c[10] != "PERSONA JURIDICA COMERCIAL" or "INDIVIDUAL" in c[11]:
            continue  # fuera EIRL: su razón social suele ser el nombre de una persona natural
        fila = {"anio": c[0], "razon_social": c[3], "codigo": cod,
                "actividad": nombres[cod], "tramo_ventas": TRAMOS.get(c[4], c[4]), "trabajadores": c[5],
                "inicio_actividades": c[6], "subtipo": c[11], "region": c[17].title(), "comuna": c[19].title(),
                "fuente": f"SII PUB_EMPRESAS_PJ_2020_A_2024.zip / {archivo}"}
        if "NUBLE" in norm(c[17]):
            nuble.append(fila)
        if cod in MAQUILA and c[4].isdigit() and int(c[4]) >= 5:
            maquila.append(fila)
    clave = lambda f: (f["codigo"], -int(f["trabajadores"] or 0))
    return sorted(nuble, key=clave), sorted(maquila, key=clave)


def guardar(nombre, filas):
    ruta = SALIDA / f"{HOY}_{nombre}.csv"
    with ruta.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(filas)
    print(f"Guardado: {ruta.relative_to(RAIZ)} ({len(filas)} filas)")


def main():
    if len(sys.argv) == 3:
        z_emp, z_pj = sys.argv[1], sys.argv[2]
    else:
        base = RAIZ / "datos" / "crudos" / "sii"
        z_emp = base / "EMPRESAS.zip"
        pjs = sorted(glob.glob(str(base / "PUB_EMPRESAS_PJ_*.zip")))
        z_pj = pjs[-1] if pjs else None
        if not z_emp.exists() or not z_pj:
            sys.exit("Faltan EMPRESAS.zip y PUB_EMPRESAS_PJ_*.zip en datos/crudos/sii/ (o pásalos como argumentos).")
    with zipfile.ZipFile(z_emp) as z:
        nac, nombres = nacional(z)
        reg = regional(z)
    guardar("sii_alimentos_nacional", nac)
    guardar("sii_alimentos_region", reg)
    guardar("sii_alimentos_resumen", resumen(nac, reg, nombres))
    with zipfile.ZipFile(z_pj) as z:
        nuble, maquila = nominas(z, nombres)
    guardar("sii_nuble_elaboracion_pj", nuble)
    guardar("sii_posibles-maquiladores_pj", maquila)


if __name__ == "__main__":
    main()
