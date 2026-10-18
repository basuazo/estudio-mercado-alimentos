#!/usr/bin/env python3
"""Índice de demanda de búsqueda por oportunidad, desde el diccionario revisado de términos (rediseño 2026-10-17).

Lee  datos/referencia/google-ads_terminos.csv  (ver scripts/google_ads_terminos.py)
Escribe
  datos/limpios/<HOY>_google-ads_indice_oportunidades.csv   una fila por oportunidad
  columnas de Google Ads en datos/limpios/<RADAR>_radar-oportunidades_boris.csv

Método (auditoría Google Ads del 2026-10-16):
  - Solo cuentan los términos "especifico". Las variantes de un mismo concepto se colapsan al máximo, no se suman.
  - indice = (log10(volumen) - log10(50)) / (log10(500.000) - log10(50)) x 100   -> 0, 25, 50, 75, 100 por nivel.
    Con cuenta sin gasto los volúmenes son niveles de 10x: el error es aprox. x3 (rango ÷3 a x3).
  - techo = índice del término clave actual del radar (cota superior cuando ese término es demasiado amplio).
  - CPC y competencia solo de términos específicos con CPC informado.
  - Sin términos específicos medidos: "no medido" (no se inventa el dato).
Uso: python scripts/actualizar_radar_google_ads.py [RADAR=2026-10-16] [HOY=2026-10-17]
"""
import csv
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RADAR_F = sys.argv[1] if len(sys.argv) > 1 else "2026-10-16"
HOY = sys.argv[2] if len(sys.argv) > 2 else "2026-10-17"
LI = RAIZ / "datos" / "limpios"
DICC = RAIZ / "datos" / "referencia" / "google-ads_terminos.csv"
RADAR = LI / f"{RADAR_F}_radar-oportunidades_boris.csv"


def num(x):
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return None


def indice(v):
    if v is None:
        return None
    if v <= 50:
        return 0
    return round((math.log10(v) - math.log10(50)) / (math.log10(500000) - math.log10(50)) * 100)


def fmt(v):
    return "" if v is None else f"{v:,}".replace(",", ".")


filas = list(csv.DictReader(open(DICC, encoding="utf-8-sig")))
por_op = defaultdict(list)
for f in filas:
    por_op[f["oportunidad"]].append(f)

salida = []
for op, ts in por_op.items():
    esp = [t for t in ts if t["tipo"] == "especifico" and num(t["busquedas_mes_chile"]) is not None]
    conceptos = defaultdict(int)
    for t in esp:
        conceptos[t["concepto"]] = max(conceptos[t["concepto"]], num(t["busquedas_mes_chile"]))
    vol = sum(conceptos.values()) if esp else None
    clave = next((t for t in ts if t["es_clave_radar"] == "si"), None)
    techo = indice(num(clave["busquedas_mes_chile"])) if clave else None
    idx = indice(vol)
    cpcs = [num(t["cpc_alto_clp"]) for t in esp if num(t["cpc_alto_clp"])]
    comps = Counter(t["competencia"] for t in esp if t["competencia"] and (num(t["busquedas_mes_chile"]) or 0) >= 500) \
        or Counter(t["competencia"] for t in esp if t["competencia"])
    top = sorted(conceptos.items(), key=lambda x: -x[1])[:4]
    salida.append({
        "oportunidad": op,
        "termino_clave_radar": clave["termino"] if clave else "",
        "nivel_termino_clave": num(clave["busquedas_mes_chile"]) if clave else "",
        "indice_techo": techo if techo is not None else "",
        "terminos_especificos": len(esp),
        "conceptos_especificos": len(conceptos),
        "volumen_especifico_aprox": vol if vol is not None else "",
        "rango_volumen_especifico": f"{fmt(round(vol / 3))}-{fmt(vol * 3)}" if vol else "",
        "indice_busqueda_especifico": idx if idx is not None else "",
        "estado_medicion": "no medido" if vol is None else "medido",
        "termino_clave_demasiado_amplio": "si" if (techo is not None and (idx is None or techo - idx >= 25)) else "",
        "cpc_alto_max_especifico_clp": max(cpcs) if cpcs else "",
        "competencia_especifico": comps.most_common(1)[0][0] if comps else "",
        "conceptos_principales": "; ".join(f"{c} {fmt(v)}" for c, v in top),
        "terminos_validados": sum(1 for t in ts if t["validado"] == "si"),
        "terminos_en_diccionario": len(ts),
    })

out = LI / f"{HOY}_google-ads_indice_oportunidades.csv"
with open(out, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(salida[0].keys()), lineterminator="\n")
    w.writeheader()
    w.writerows(salida)

# Radar: se reemplazan las columnas de Google Ads
indice_por_op = {s["oportunidad"]: s for s in salida}
rows = list(csv.DictReader(open(RADAR, encoding="utf-8-sig")))
viejas = ("termino_clave_google_ads", "nivel_termino_clave_mes", "senal_google_ads", "indice_busqueda_especifico",
          "indice_techo_termino_clave", "volumen_especifico_aprox")
cols = [c for c in rows[0].keys() if c not in viejas]
for r in rows:
    s = indice_por_op.get(r["oportunidad"])
    if not s:
        r.update({k: "" for k in viejas})
        continue
    r["termino_clave_google_ads"] = s["termino_clave_radar"]
    r["nivel_termino_clave_mes"] = s["nivel_termino_clave"]
    r["indice_techo_termino_clave"] = s["indice_techo"]
    r["volumen_especifico_aprox"] = s["volumen_especifico_aprox"]
    r["indice_busqueda_especifico"] = s["indice_busqueda_especifico"]
    partes = [f"específico ~{fmt(num(s['volumen_especifico_aprox']))}/mes (índice {s['indice_busqueda_especifico']})"
              if s["estado_medicion"] == "medido" else "específico no medido"]
    if s["termino_clave_demasiado_amplio"]:
        partes.append(f"término clave amplio, techo {s['indice_techo']}")
    if s["cpc_alto_max_especifico_clp"]:
        partes.append(f"CPC alto hasta {fmt(s['cpc_alto_max_especifico_clp'])} CLP")
    if s["competencia_especifico"]:
        partes.append(f"competencia {s['competencia_especifico'].lower()}")
    r["senal_google_ads"] = " | ".join(partes)
cols += list(viejas)
with open(RADAR, "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols)
    w.writeheader()
    w.writerows(rows)
print(f"Guardado: {out.relative_to(RAIZ)} y columnas de Google Ads en {RADAR.relative_to(RAIZ)}")
for s in sorted(salida, key=lambda s: -(s["indice_busqueda_especifico"] if s["indice_busqueda_especifico"] != "" else -1)):
    print(f"{str(s['indice_busqueda_especifico']):>4} (techo {str(s['indice_techo']):>3}) {s['oportunidad'][:50]:50} {s['conceptos_principales'][:60]}")
