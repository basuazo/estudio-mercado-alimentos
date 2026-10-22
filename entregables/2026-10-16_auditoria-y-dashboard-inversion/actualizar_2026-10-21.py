"""Genera los datasets nuevos del dashboard (21-oct): tendencias asiáticas, Australia y nuevas líneas de oferta.
Correr desde la raíz del repositorio: python entregables/2026-10-16_auditoria-y-dashboard-inversion/actualizar_2026-10-21.py
Escribe JSON en entregables/2026-10-16_auditoria-y-dashboard-inversion/datos/ (se suben como archivos del dashboard).
"""
import csv, json, re, statistics
from collections import defaultdict
from pathlib import Path

R = Path(__file__).resolve().parents[2]
D = R / "datos"
OUT = Path(__file__).resolve().parent / "datos"


def rd(p):
    return list(csv.DictReader(open(p, encoding="utf-8")))


def num(x):
    try:
        return float(x) if x not in ("", None) else None
    except ValueError:
        return None


def w(name, rows):
    json.dump(rows, open(OUT / f"{name}.json", "w", encoding="utf-8"), ensure_ascii=False)
    print(name, len(rows))


CAT = {"fideos y sopas": "Fideos y sopas", "bebidas asiaticas": "Bebidas asiáticas", "japones": "Japonés", "coreano": "Coreano",
       "chino y chifa": "Chino y chifa", "sudeste asiatico e india": "Sudeste asiático e India", "ingredientes y salsas": "Ingredientes y salsas",
       "salud de origen asiatico": "Salud de origen asiático", "snacks y dulces": "Snacks y dulces", "canal": "Canal"}
# 1. Matriz de términos asiáticos
m = rd(D / "limpios/2026-10-21_matriz-asiaticos_trends-x-ads.csv")
w("asia_terminos", [{
    "termino": r["termino"], "categoria": CAT.get(r["categoria"], r["categoria"]), "cuadrante": r["cuadrante"],
    "busquedas_mes": num(r["busquedas_mes"]), "competencia": r["competencia"] or None, "cpc_alto_clp": num(r["cpc_alto_clp"]),
    "nivel_trends": r["volumen"], "var_anual_pct": num(r["var_ano2_vs_ano1_pct"]), "var_oct_jun_pct": num(r["var_oct_jun_pct"]),
    "semana_maximo": r["semana_maximo"] or None, "indice_vs_granola": num(r["indice_volumen_vs_granola"]),
    "cambio_anual_ads": r["cambio_anual"] or None} for r in m])

# 2. Series mensuales (términos con datos suficientes o medios)
okt = {r["termino"] for r in m if r["volumen"] in ("suficiente", "media")}
cat = {r["termino"]: CAT.get(r["categoria"], r["categoria"]) for r in m}
s = rd(D / "crudos/2026-10-21_google-trends_cl_2anios_individual_asiaticos.csv")
acc = defaultdict(list)
for r in s:
    mes = r["semana"][:7]
    for k in okt:
        acc[(k, mes)].append(num(r[k]) or 0)
w("asia_series", [{"termino": k, "categoria": cat[k], "mes": mes, "indice": round(sum(v) / len(v), 1)}
                  for (k, mes), v in sorted(acc.items()) if mes >= "2024-10" and mes <= "2026-09"])

# 3. Ideas del Planificador: por intención y por marca
I = [r for r in rd(D / "limpios/2026-10-21_google-ads_asiaticos_ideas_clasificadas.csv") if r["extranjero_probable"] == "False"]
NOM = {"local_o_marca_por_confirmar": "Local o marca (por confirmar)", "otro": "Otra", "restaurante": "Restaurante o delivery",
       "marca": "Marca de producto", "receta": "Receta", "salud": "Salud", "compra": "Compra o precio"}
g = defaultdict(lambda: [0, 0, 0])
for r in I:
    k = ("intencion", NOM.get(r["intencion"], r["intencion"]))
    g[k][0] += 1; g[k][1] += num(r["busquedas_mes"]) or 0; g[k][2] += r["cambio_anual"] in ("900%", "∞")
    if r["marca"]:
        k = ("marca", r["marca"].title())
        g[k][0] += 1; g[k][1] += num(r["busquedas_mes"]) or 0; g[k][2] += r["cambio_anual"] in ("900%", "∞")
w("asia_ideas", [{"id": f"{a}:{b}", "grupo": a, "nombre": b, "ideas": v[0], "busquedas_mes": v[1], "ideas_que_saltan": v[2]}
                 for (a, b), v in sorted(g.items(), key=lambda x: -x[1][1])])

# 4. Comtrade asiático
c = rd(D / "crudos/2026-10-21_un-comtrade_importaciones-chile_asiaticos.csv")
w("asia_comtrade", [{"id": f"{r['partida_hs6']}-{r['anio']}", "partida": r["partida_hs6"], "descripcion": r["descripcion"],
                     "anio": int(r["anio"]), "cif_usd": num(r["valor_cif_usd"]), "kg": num(r["peso_neto_kg"]),
                     "pct_asia": num(r["pct_desde_asia"]), "origenes": r["principales_origenes_asia_pct"]} for r in c])

# 5. Australia vs Chile: resumen y series trimestrales
NOMBRE = {"bubble tea": "Bubble tea", "poke": "Poke", "matcha": "Matcha", "kombucha": "Kombucha", "oat milk": "Leche de avena",
          "sourdough": "Masa madre", "acai": "Açaí", "kimchi": "Kimchi", "ramen": "Ramen", "korean fried chicken": "Pollo frito coreano",
          "tteokbokki": "Tteokbokki", "mochi": "Mochi", "cold brew": "Cold brew", "kefir": "Kéfir", "collagen": "Colágeno",
          "ketogenic diet": "Dieta keto", "hard seltzer": "Hard seltzer", "kale": "Kale", "quinoa": "Quinoa", "chia seed": "Chía",
          "coconut water": "Agua de coco", "birria": "Birria", "smash burger": "Smash burger", "cottage cheese": "Cottage cheese",
          "dubai chocolate": "Chocolate Dubái", "buldak": "Buldak"}
LECT = {"chia seed": "Chile primero o propio", "collagen": "Chile primero o propio", "ketogenic diet": "Chile primero o propio",
        "matcha": "Simultáneo (ruido en el despegue)", "oat milk": "Simultáneo (ruido en el despegue)", "poke": "No llegó (débil en Chile)",
        "acai": "No llegó (débil en Chile)", "kale": "No llegó (débil en Chile)", "hard seltzer": "No llegó (débil en Chile)"}
a = rd(D / "limpios/2026-10-21_au-vs-cl_resumen_por-tema.csv")
def anio(q):
    return int(q[:4]) + (int(q[-1]) - 1) / 4 if q else None
rows = []
for r in a:
    pat = LECT.get(r["concepto"]) or {"Australia primero": "Australia primero", "casi simultaneo": "Simultáneo",
                                       "Chile primero": "Chile primero o propio", "no despego en Chile": "No llegó (débil en Chile)"}[r["patron"]]
    rows.append({"concepto": NOMBRE[r["concepto"]], "despegue_au": r["despegue_AU"], "despegue_cl": r["despegue_CL"],
                 "despegue_au_anio": anio(r["despegue_AU"]), "despegue_cl_anio": anio(r["despegue_CL"]),
                 "rezago_trimestres": num(r["rezago_trimestres"]), "patron_calculado": r["patron"], "patron": pat,
                 "peak_au": r["peak_AU"], "peak_cl": r["peak_CL"], "actual_vs_peak_au_pct": num(r["nivel_actual_vs_peak_AU_pct"]),
                 "actual_vs_peak_cl_pct": num(r["nivel_actual_vs_peak_CL_pct"]), "corr_sin_rezago": num(r["corr_crecimiento_sin_rezago"]),
                 "mejor_rezago_trim": num(r["mejor_rezago_corr_trim"]), "corr_mejor_rezago": num(r["corr_mejor_rezago"])})
w("au_temas", rows)
t = rd(D / "crudos/2026-10-21_google-trends_au-vs-cl_trimestral_26-temas.csv")
qs = [k for k in t[0] if re.match(r"\d{4}Q\d", k)]
w("au_series", [{"concepto": NOMBRE[r["concepto"]], "pais": "Australia" if r["pais"] == "AU" else "Chile", "trimestre": q,
                 "t": int(q[:4]) + (int(q[-1]) - 1) / 4, "indice": num(r[q])} for r in t for q in qs])
x = rd(D / "limpios/2026-10-21_au-vs-cl_correlacion_por-rezago.csv")
byL = defaultdict(list)
for r in x:
    if r["correlacion"] not in ("", "nan"):
        byL[int(r["rezago_trimestres"])].append(float(r["correlacion"]))
w("au_correlacion", [{"rezago_trimestres": L, "correlacion_mediana": round(statistics.median(v), 2), "n_temas": len(v)} for L, v in sorted(byL.items())])

# 6. Radar Australia (15 temas asiáticos, 5 años)
NOM2 = {"hojicha": "Hojicha", "yuzu": "Yuzu", "tanghulu": "Tanghulu", "bingsu": "Bingsu", "onigiri": "Onigiri", "katsu sando": "Katsu sando",
        "mochi donut": "Mochi donut", "korean corn dog": "Corn dog coreano", "taiyaki": "Taiyaki", "gochujang": "Gochujang", "hot pot": "Hot pot",
        "dumpling": "Dumplings", "japanese cheesecake": "Cheesecake japonés", "yakult": "Yakult"}
LEC2 = {"hojicha": "Por llegar", "yuzu": "Por llegar", "katsu sando": "Por llegar", "japanese cheesecake": "Por llegar (nicho)",
        "gochujang": "Llegando", "dumpling": "Llegando", "hot pot": "Llegando", "bingsu": "Llegando (base casi cero)", "taiyaki": "Llegando (base casi cero)",
        "onigiri": "Ya está en Chile", "korean corn dog": "Moda pasada, no llegó", "mochi donut": "Moda pasada, no llegó",
        "tanghulu": "Moda pasada, no llegó", "yakult": "Sin señal"}
z = [r for r in rd(D / "crudos/2026-10-21_google-trends_au-vs-cl_5anios_15-temas-asiaticos.csv") if r["concepto"] != "ube"]
by = defaultdict(dict)
for r in z:
    by[r["concepto"]][r["pais"]] = r
rows = []
for k, v in by.items():
    au, cl = v["AU"], v["CL"]
    a1, a5 = num(au["prom_anio1"]), num(au["prom_anio5"])
    rows.append({"tema": NOM2[k], "lectura": LEC2[k], "au_anio1": a1, "au_anio5": a5,
                 "au_var_5anios_pct": round((a5 / a1 - 1) * 100) if a1 else None,
                 "au_var_12m_pct": num(au["var_ult12m_vs_previos12m_pct"]), "cl_anio5": num(cl["prom_anio5"]),
                 "cl_var_12m_pct": num(cl["var_ult12m_vs_previos12m_pct"]), "cl_pct_semanas_cero": num(cl["pct_semanas_cero"])})
w("au_radar", rows)

# 7. Nuevas líneas de oferta y productos vistos en supermercados
L = rd(D / "limpios/2026-10-21_lineas-oferta-asiaticas.csv")
w("lineas_oferta", [{"id": r["id"], "linea": r["linea"], "terminos_demanda": r["terminos_demanda"], "busquedas_mes": num(r["busquedas_mes_ads"]),
                     "var_oct_jun_pct": num(r["var_oct_jun_pct"]), "senal_australia": r["senal_australia"],
                     "skus_santa_isabel": int(r["skus_santa_isabel"]), "skus_tottus": int(r["skus_tottus"]),
                     "skus_total": int(r["skus_santa_isabel"]) + int(r["skus_tottus"]), "marcas": r["marcas_supermercado"],
                     "precio_ref": r["precio_ref_clp_kg"], "estado_oferta": r["estado_oferta"], "lectura": r["lectura"],
                     "prioridad_ml": None if r["prioridad_ml"] in ("", "—") else int(r["prioridad_ml"]),
                     "terminos_ml": None if r["terminos_ml"] in ("", "—") else r["terminos_ml"], "siguiente_paso": r["siguiente_paso"]} for r in L])
# productos del rubro (filtro por línea)
REL = [("L01", "ramen|fideos instantaneos", r"ramen|instant|fideos inst|sopa instant"),
       ("L03", "ramen|miso", r"d'fab|artesanal"),
       ("L04", "gyozas|dumplings", r"gyoz|gyos|arrollado"),
       ("L08", "salsa de soya", r"soya|soja|teriyaki|unagi|asi[aá]tica|sriracha|ostra|pad thai|chili|wasabi|tamarindo"),
       ("L11", "matcha", r"matcha"), ("L12", "fideos de arroz", r"arroz"), ("L13", "kimchi", r"kimchi"),
       ("L14", "edamame", r"^edamame"), ("L03", "alga nori|yuzu", r"nori|nory")]
P = rd(D / "crudos/2026-10-21_supermercados_lineas-asiaticas_busquedas.csv")
prods, seen = [], set()
for r in P:
    for lid, terms, rx in REL:
        if re.fullmatch(terms, r["termino"]) and r["producto"] and re.search(rx, r["producto"], re.I):
            if lid == "L01" and re.search(r"d'fab|artesanal", r["producto"], re.I):
                continue
            if lid == "L03" and re.search(r"nori|nory", r["producto"], re.I):
                lid2 = "Otros"
            else:
                lid2 = lid
            key = (r["cadena"], r["producto"])
            if key in seen:
                continue
            seen.add(key)
            m_ = re.search(r"\$\s?([\d.]+)\s*(?:x|por)\s*(kg|lt|l)\b", r["precio_unitario_publicado"], re.I)
            prods.append({"id": f"{r['cadena']}|{r['producto']}", "linea_id": lid2, "cadena": r["cadena"].title(), "marca": r["marca"].title(),
                          "producto": r["producto"], "precio_clp": num(r["precio_clp"]),
                          "precio_kg_o_l": num(m_.group(1).replace(".", "")) if m_ else None,
                          "unidad": ("CLP/L" if m_.group(2).lower() in ("lt", "l") else "CLP/kg") if m_ else None, "nota": r["nota"] or None})
w("lineas_productos", prods)
