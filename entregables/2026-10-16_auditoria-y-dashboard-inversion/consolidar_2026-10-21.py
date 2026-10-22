"""Consolida los datos del dashboard en un solo universo (21-oct).

- oportunidades.json: las 23 del radar + las 14 líneas asiáticas, con el campo `foco`. Las líneas asiáticas traen
  oferta en supermercado y prioridad de Mercado Libre; sus familias se cuentan con la misma regla estricta
  (la oferta en supermercado online NO cuenta como familia hasta que el grupo lo acuerde).
- terminos_busqueda.json: los 200 términos de búsqueda (100 del 13-oct + 100 asiáticos del 21-oct) con la misma
  medida para todos: variación octubre–junio contra octubre–junio, calculada desde los crudos.
- series_mensuales.json: curva mensual de los términos con datos suficientes o medios de los dos estudios.

Correr desde la raíz: python entregables/2026-10-16_auditoria-y-dashboard-inversion/consolidar_2026-10-21.py
(después de actualizar_2026-10-21.py, que genera lineas_oferta.json).
"""
import csv, json, math, statistics
from collections import defaultdict
from pathlib import Path

R = Path(__file__).resolve().parents[2]
D = R / "datos"
OUT = Path(__file__).resolve().parent / "datos"
rd = lambda p: list(csv.DictReader(open(p, encoding="utf-8-sig")))
num = lambda x: (float(x) if x not in ("", None) else None)


def wj(name, rows):
    json.dump(rows, open(OUT / f"{name}.json", "w", encoding="utf-8"), ensure_ascii=False)
    print(name, len(rows))


# ---------------------------------------------------------------- términos de búsqueda (200)
def metricas(crudo):
    rows = rd(crudo)
    out = {}
    for k in rows[0]:
        if k == "semana":
            continue
        v = [num(r[k]) or 0 for r in rows]
        sem = [r["semana"] for r in rows]
        a = sum(x for x, s in zip(v, sem) if "2024-10-06" <= s < "2025-06-29")
        b = sum(x for x, s in zip(v, sem) if "2025-10-05" <= s < "2026-06-28")
        ceros = round(100 * sum(1 for x in v if x == 0) / len(v))
        nivel = "sin datos" if ceros == 100 else "suficiente" if ceros <= 5 else "media" if ceros < 50 else "baja (datos esporadicos)"
        out[k] = {"nivel": nivel, "pct_ceros": ceros, "var_oct_jun": round((b / a - 1) * 100) if a and nivel != "sin datos" else None,
                  "semana_max": sem[v.index(max(v))] if max(v) > 0 else None, "serie": list(zip(sem, v))}
    return out


CAT = {"fideos y sopas": "Fideos y sopas", "bebidas asiaticas": "Bebidas asiáticas", "japones": "Japonés", "coreano": "Coreano",
       "chino y chifa": "Chino y chifa", "sudeste asiatico e india": "Sudeste asiático e India", "ingredientes y salsas": "Ingredientes y salsas asiáticos",
       "salud de origen asiatico": "Salud de origen asiático", "snacks y dulces": "Snacks y dulces asiáticos", "canal": "Canal",
       "atributo": "Atributos", "barras y snacks": "Barras y snacks", "bebidas y aguas": "Bebidas y aguas", "lacteos": "Lácteos",
       "suplementos": "Suplementos", "granel fraccionado": "Granel", "panaderia y cereales": "Panadería y cereales",
       "endulzantes": "Endulzantes", "comidas preparadas": "Comidas preparadas"}
m_old = metricas(D / "crudos/2026-10-13_google-trends_cl_2anios_individual_100.csv")
m_new = metricas(D / "crudos/2026-10-21_google-trends_cl_2anios_individual_asiaticos.csv")
aud = {r["termino"]: r for r in json.load(open(OUT / "trends_terminos.json", encoding="utf-8"))}
ref_old = {r["termino"]: r for r in rd(D / "referencia/terminos-busqueda.csv")}
ads_old = {r["termino"]: r for r in rd(D / "limpios/2026-10-16_google-ads_volumenes_114.csv")}
res_old = {r["termino"]: r for r in rd(D / "limpios/2026-10-13_google-trends_cl_2anios_resumen_100.csv")}
mat_new = {r["termino"]: r for r in rd(D / "limpios/2026-10-21_matriz-asiaticos_trends-x-ads.csv")}

terms = []
for t, mm in m_old.items():
    a = ads_old.get(t, {})
    terms.append({"termino": t, "foco": "Salud y funcional", "categoria": CAT.get(ref_old.get(t, {}).get("categoria"), ref_old.get(t, {}).get("categoria")),
                  "busquedas_mes": num(a.get("busquedas_mes_chile")), "competencia": a.get("competencia") or None, "cpc_alto_clp": num(a.get("cpc_alto_clp")),
                  "nivel_trends": mm["nivel"], "pct_semanas_cero": mm["pct_ceros"], "var_12m_pct": num(aud.get(t, {}).get("var_12m_pct")),
                  "var_oct_jun_pct": mm["var_oct_jun"], "semana_maximo": mm["semana_max"], "indice_vs_granola": num(res_old.get(t, {}).get("indice_volumen_vs_granola")),
                  "nota_auditoria": aud.get(t, {}).get("clasificacion"), "estudio": "13-oct"})
for t, mm in m_new.items():
    a = mat_new[t]
    terms.append({"termino": t, "foco": "Asiático", "categoria": CAT[a["categoria"]], "busquedas_mes": num(a["busquedas_mes"]),
                  "competencia": a["competencia"] or None, "cpc_alto_clp": num(a["cpc_alto_clp"]), "nivel_trends": mm["nivel"], "pct_semanas_cero": mm["pct_ceros"],
                  "var_12m_pct": num(a["var_ano2_vs_ano1_pct"]), "var_oct_jun_pct": mm["var_oct_jun"], "semana_maximo": mm["semana_max"],
                  "indice_vs_granola": num(a["indice_volumen_vs_granola"]), "nota_auditoria": None, "estudio": "21-oct"})
suf = [r["var_oct_jun_pct"] for r in terms if r["nivel_trends"] == "suficiente" and r["var_oct_jun_pct"] is not None]
deriva = statistics.median(suf)
print("deriva oct-jun (todos los suficientes):", deriva, len(suf))
for r in terms:
    v, b = r["var_oct_jun_pct"], r["busquedas_mes"]
    if r["nivel_trends"] in ("sin datos", "baja (datos esporadicos)") or v is None:
        c = "nicho o sin datos en Trends"
    elif v - deriva >= 10 and (b or 0) >= 5000:
        c = "crece con volumen"
    elif v - deriva >= 10:
        c = "crece desde base chica"
    elif v <= -10:
        c = "cae"
    else:
        c = "estable"
    r["cuadrante"] = c
    r["exceso_pp"] = None if v is None or c.startswith("nicho") else v - deriva
wj("terminos_busqueda", terms)

# ---------------------------------------------------------------- series mensuales de los dos estudios
ser = []
for foco, mm_all in (("Salud y funcional", m_old), ("Asiático", m_new)):
    for t, mm in mm_all.items():
        if mm["nivel"] not in ("suficiente", "media"):
            continue
        acc = defaultdict(list)
        for s, v in mm["serie"]:
            acc[s[:7]].append(v)
        for mes, v in sorted(acc.items()):
            if "2024-10" <= mes <= "2026-09":
                ser.append({"termino": t, "foco": foco, "mes": mes, "indice": round(sum(v) / len(v), 1)})
wj("series_mensuales", ser)

# ---------------------------------------------------------------- universo de oportunidades
opo = json.load(open(OUT / "oportunidades.json", encoding="utf-8"))
opo = [o for o in opo if not str(o["id"]).startswith("L")]  # re-ejecutable
for o in opo:
    o["foco"] = "Salud y funcional"
lin = json.load(open(OUT / "lineas_oferta.json", encoding="utf-8"))
VER = {"L01": "Descartar", "L02": "Radar", "L03": "Investigar", "L04": "Investigar", "L05": "Investigar", "L06": "Terreno primero",
       "L07": "Investigar", "L08": "Descartar", "L09": "Radar", "L10": "Radar", "L11": "Radar", "L12": "Radar", "L13": "Radar", "L14": "Descartar"}
ORD = {"Investigar": 1, "Terreno primero": 2, "Rebajar": 3, "Radar": 4, "Postergar": 5, "Descartar": 6}
# Misma regla que el benchmark del 18-oct: una señal externa cuenta como familia solo si es favorable.
# Australia: cuenta si la tendencia llegó, está llegando o está por llegar (boba no: ya se desinfla allá).
# Comtrade: cuenta solo si la partida es específica y crece (tapioca); soya y té verde bajan 2021→2025.
AU = {"L01", "L02", "L04", "L07", "L09", "L11", "L13"}
MACRO = {"L05": "190300 Tapioca"}
PARTIDA = {"L05": "190300 Tapioca", "L08": "210310 Salsa de soya", "L11": "090210 Té verde"}
TERM = {"L01": "ramen", "L02": "buldak", "L03": "ramen", "L04": "dumplings", "L05": "boba", "L06": "onigiri", "L07": "gochujang", "L08": "salsa de soya",
        "L09": "mochi", "L10": "miso", "L11": "matcha", "L12": "udon", "L13": "kimchi", "L14": "edamame"}
tt = {r["termino"]: r for r in terms}
for l in lin:
    k = TERM[l["id"]]; t = tt[k]
    fam = ["Busqueda-Google"] + (["Señal Australia (Trends, 21-oct)"] if l["id"] in AU else []) + (["Macro-Comtrade"] if l["id"] in MACRO else [])
    ex = t["exceso_pp"]
    b = l["busquedas_mes"] or t["busquedas_mes"]
    sen = "Sin dato" if ex is None else "Fuerte" if ex >= 10 and (b or 0) >= 5000 else "Media" if ex >= 10 else "Débil"
    b = l["busquedas_mes"] or t["busquedas_mes"]
    opo.append({
        "id": l["id"], "oportunidad": l["linea"], "nombre_radar": None, "foco": "Asiático", "tipo": None, "estado_radar": "nueva (21-oct)",
        "n_fuentes_radar": None, "n_familias_estricto": len(fam), "familias": "; ".join(fam),
        "trends_var_12m_pct": t["var_12m_pct"], "trends_exceso_pp": ex, "trends_clasificacion": t["cuadrante"],
        "ads_termino_clave": k, "ads_nivel_radar": None, "ads_volumen_especifico": b,
        "ads_indice": round((math.log10(b) - math.log10(50)) * 25) if b else None, "ads_termino_amplio": None, "ads_estado": "Medido" if b else None,
        "ml_publicaciones": None, "ml_marcas": None, "ml_share_top3_pct": None, "ml_precio_mediana": None, "ml_unidad_precio": None,
        "sii_actividad": None, "sii_var_empresas_2022_2024_pct": None, "import_partida": PARTIDA.get(l["id"]), "import_usd_2025": None,
        "intl_etapa": None, "intl_direccion": None, "intl_barrera": None, "intl_confianza": None, "intl_chile": None,
        "intl_lectura": ("Australia: " + l["senal_australia"]) if l["senal_australia"] not in ("", "—", None) else None,
        "senal_demanda": sen, "veredicto_preliminar": VER[l["id"]], "orden_veredicto": ORD[VER[l["id"]]],
        "lectura": l["lectura"] + " (Lectura preliminar del 21-oct, juicio y no dato.)",
        "nota_fuentes": "Australia y Comtrade cuentan como familia solo si la señal es favorable (misma regla que el benchmark). La oferta en supermercado online no se cuenta hasta que el grupo lo acuerde. La señal de Australia también viene de Google Trends, pero de otro mercado.",
        "nota_trends": f"Término clave '{k}': variación octubre–junio {t['var_oct_jun_pct']} % (sobre la deriva común de los 200 términos).",
        "retail_skus": l["skus_total"], "retail_estado": l["estado_oferta"], "retail_marcas": l["marcas"], "retail_precio_ref": l["precio_ref"],
        "prioridad_ml": l["prioridad_ml"], "terminos_ml": l["terminos_ml"], "siguiente_paso": l["siguiente_paso"],
    })
wj("oportunidades", opo)
