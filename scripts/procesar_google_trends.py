"""Calcula indicadores de Google Trends (misma regla que el estudio del 13-oct).

Uso: python scripts/procesar_google_trends.py <series_individuales.csv> <volumen_relativo.csv> <terminos.csv> <prefijo_salida>
- series: columnas semana + un término por columna (escala 0-100 propia de cada término).
- volumen relativo: termino, prom52_termino, prom52_granola (grupos de 5 con granola como ancla).
- terminos: id, termino, categoria, ...
Agrega var_oct_jun_pct (oct-jun de cada anio, sin el invierno) y semana_maximo.
Salidas: <prefijo>_resumen.csv y <prefijo>_series-largo.csv en datos/limpios/.
"""
import csv, sys

serie_f, rel_f, term_f, pref = sys.argv[1:5]
rows = list(csv.DictReader(open(serie_f, encoding="utf-8")))
rel = {r["termino"]: r for r in csv.DictReader(open(rel_f, encoding="utf-8"))}
terms = list(csv.DictReader(open(term_f, encoding="utf-8")))

def num(x):
    return float(x) if x not in ("", None) else 0.0

def pct(a, b):
    return round((a / b - 1) * 100) if b > 0 else ""

out, largo = [], []
for t in terms:
    k = t["termino"]
    v = [num(r[k]) for r in rows]
    n = len(v)
    ceros = round(100 * sum(1 for x in v if x == 0) / n)
    y1, y2 = sum(v[:52]) / 52, sum(v[-52:]) / 52
    p13, u13 = sum(v[:13]) / 13, sum(v[-13:]) / 13
    if ceros == 100:
        nivel = "sin datos"
    elif ceros <= 5:
        nivel = "suficiente"
    elif ceros < 50:
        nivel = "media"
    else:
        nivel = "baja (datos esporadicos)"
    # ventana comparable sin julio-septiembre (semanas 1-38 de cada anio): evita peaks de invierno
    a, b = sum(v[0:38]), sum(v[52:90])
    smax = rows[v.index(max(v))]["semana"] if max(v) > 0 else ""
    idx = ""
    if k in rel and num(rel[k]["prom52_granola"]) > 0:
        idx = round(100 * num(rel[k]["prom52_termino"]) / num(rel[k]["prom52_granola"]))
    out.append({"termino": k, "categoria": t["categoria"], "volumen": nivel,
                "pct_semanas_cero": ceros, "prom_ano1": round(y1, 1), "prom_ano2": round(y2, 1),
                "var_ano2_vs_ano1_pct": pct(y2, y1) if nivel != "sin datos" else "",
                "var_ult13sem_vs_prim13sem_pct": pct(u13, p13) if nivel != "sin datos" else "",
                "var_oct_jun_pct": pct(b, a) if nivel != "sin datos" else "",
                "semana_maximo": smax,
                "indice_volumen_vs_granola": idx})
    if nivel in ("suficiente", "media"):
        for r in rows:
            largo.append({"semana": r["semana"], "termino": k, "indice": r[k] or 0})

with open(f"datos/limpios/{pref}_resumen.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
with open(f"datos/limpios/{pref}_series-largo.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["semana", "termino", "indice"]); w.writeheader(); w.writerows(largo)
print(len(out), "terminos;", sum(1 for o in out if o["volumen"] == "suficiente"), "suficientes")
