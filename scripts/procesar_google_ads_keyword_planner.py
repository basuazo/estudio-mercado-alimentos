#!/usr/bin/env python3
"""Limpia las exportaciones de Google Ads Keyword Planner (UTF-16, tabulado), las agrupa por
candidata del estudio de mercado y las cruza con Google Trends. Uso: python scripts/procesar_google_ads_keyword_planner.py [AAAA-MM-DD]"""
import csv, io, re, sys, unicodedata
FECHA = sys.argv[1] if len(sys.argv) > 1 else '2026-10-16'
CR, LI, RF = 'datos/crudos/', 'datos/limpios/', 'datos/referencia/'
def n(s): return unicodedata.normalize('NFD', s.lower()).encode('ascii', 'ignore').decode()
def cargar(f):
    t = open(CR + f, encoding='utf-16').read().splitlines()
    i = next(j for j, l in enumerate(t) if l.startswith('Keyword\t'))
    return [r for r in csv.DictReader(io.StringIO('\n'.join(t[i:])), delimiter='\t') if r['Keyword'].strip()]
def num(x):
    try: return int(float(x))
    except: return None
CAND = [
 ('electrolitos', r'electrolit|suero oral|rehidrat|bebida isoton|hidratante en polvo|sobres? de (sales|hidrat)'),
 ('proteica_rtd', r'(bebida|batido|shake|cafe|leche|listo|lista|yogurt).*protei|protei.*(bebida|batido|shake|cafe|listo|lista|rtd)'),
 ('cold_brew', r'cold ?brew|cafe frio'),
 ('matcha', r'matcha'),
 ('avena_barista', r'barista|leche de avena|bebida de avena'),
 ('chai', r'chai'), ('liofilizados', r'liofiliz'), ('ginger_beer', r'ginger'),
 ('agua_coco', r'agua de coco'), ('compra_por_mayor', r'por mayor|bebidas por mayor|mayorista'),
]
def candidata(k):
    for c, p in CAND:
        if re.search(p, n(k)): return c
    return ''
trends = {r['termino']: r for r in csv.DictReader(open(LI + '2026-10-13_google-trends_cl_2anios_resumen_100.csv', encoding='utf-8-sig'))}
terminos = {r['termino'].strip(): r for r in csv.DictReader(open(RF + 'terminos-busqueda.csv', encoding='utf-8-sig'))}
base = cargar(f'{FECHA}_google-ads_keywords-planner-2.csv')
out = []
for r in base:
    k = r['Keyword'].strip(); t = terminos.get(k, {}); tr = trends.get(k, {})
    out.append(dict(termino=k, categoria=t.get('categoria', ''), tipo=t.get('tipo', ''), candidata=candidata(k),
      busquedas_mes_chile=num(r['Avg. monthly searches']), competencia=r['Competition'], indice_competencia=r['Competition (indexed value)'],
      cpc_bajo_clp=num(r['Top of page bid (low range)']), cpc_alto_clp=num(r['Top of page bid (high range)']),
      trends_volumen=tr.get('volumen', ''), trends_var_ano2_vs_ano1_pct=tr.get('var_ano2_vs_ano1_pct', ''), trends_var_ult13sem_pct=tr.get('var_ult13sem_vs_prim13sem_pct', '')))
out.sort(key=lambda d: (-(d['busquedas_mes_chile'] or 0), d['termino']))
def w(f, rows):
    with open(LI + f, 'w', encoding='utf-8-sig', newline='') as fh:
        wr = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); wr.writeheader(); wr.writerows(rows)
w(f'{FECHA}_google-ads_volumenes_114.csv', out)
ideas = {}
for f, s in [(f'{FECHA}_google-ads_keyword-planner_ideas.csv', 'semilla electrolitos'), (f'{FECHA}_google-ads_keyword-planner_ideas2.csv', 'semillas bebida proteica/cold brew/matcha/chai latte')]:
    for r in cargar(f):
        k = r['Keyword'].strip()
        if k not in ideas:
            ideas[k] = dict(idea=k, candidata=candidata(k), busquedas_mes_chile=num(r['Avg. monthly searches']), competencia=r['Competition'],
              cpc_bajo_clp=num(r['Top of page bid (low range)']), cpc_alto_clp=num(r['Top of page bid (high range)']), semilla=s)
ideas = sorted(ideas.values(), key=lambda d: (d['candidata'] == '', -(d['busquedas_mes_chile'] or 0), d['idea']))
w(f'{FECHA}_google-ads_ideas_por_candidata.csv', ideas)
res = []
for c, _ in CAND:
    t = [d for d in out if d['candidata'] == c]; i = [d for d in ideas if d['candidata'] == c]
    cab = max(t, key=lambda d: d['busquedas_mes_chile'] or 0, default=None)
    cp = [d['cpc_alto_clp'] for d in t if d['cpc_alto_clp']]
    res.append(dict(candidata=c, terminos_de_los_114=len(t), termino_cabeza=cab['termino'] if cab else '', busquedas_cabeza=cab['busquedas_mes_chile'] if cab else '',
      terminos_114_con_5000_o_mas=sum(1 for d in t if (d['busquedas_mes_chile'] or 0) >= 5000),
      ideas_nuevas=len(i), ideas_con_500_o_mas=sum(1 for d in i if (d['busquedas_mes_chile'] or 0) >= 500),
      ideas_con_5000_o_mas=sum(1 for d in i if (d['busquedas_mes_chile'] or 0) >= 5000),
      cpc_alto_max_clp=max(cp) if cp else ''))
w(f'{FECHA}_google-ads_resumen_candidatas.csv', res)
for r in res: print(r)
print(len(out), len(ideas), sum(1 for d in out if not d['candidata']))
