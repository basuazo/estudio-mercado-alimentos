#!/usr/bin/env python3
"""Agrega al radar de oportunidades las columnas de Google Ads (nivel de busqueda mensual en Chile).
Uso: python scripts/actualizar_radar_google_ads.py [AAAA-MM-DD]  (lee los CSV limpios de procesar_google_ads_keyword_planner.py)"""
import csv, sys
F = sys.argv[1] if len(sys.argv) > 1 else '2026-10-16'
LI = 'datos/limpios/'
RADAR = LI + f'{F}_radar-oportunidades_boris.csv'
MAP = {
 'Sobres y tabletas de electrolitos': ['electrolitos', 'electrolitos en sobre', 'sobres de electrolitos', 'suero oral', 'bebida isotonica', 'bebida hidratante en polvo'],
 'Cafe o batido proteico listo para beber 20-30 g': ['batido de proteina', 'leche proteica', 'cafe proteico', 'bebida proteica', 'proteina lista para beber', 'bebida proteica cafe'],
 'Avena barista para cafeterias (foodservice)': ['leche de avena', 'leche de avena barista'],
 'Matcha listo para beber': ['matcha', 'matcha latte'],
 'Cold brew local sin azucar': ['cold brew', 'cafe cold brew', 'cold brew concentrado'],
 'Granola con legumbre a bajo precio (marca propia)': ['granola', 'legumbres'],
 'Leche sin lactosa y sin lactosa como atributo': ['leche sin lactosa', 'sin lactosa'],
 'Jugos prensados en frio y shots': ['jugo natural', 'jugo prensado en frio', 'shot de jengibre'],
 'Agua con gas saborizada sin azucar en formato familiar': ['agua con gas', 'agua saborizada', 'agua con gas saborizada'],
 'Snack horneado de lentejas o garbanzo': ['hummus', 'legumbres', 'chips de garbanzo'],
 'Yogur griego proteico formato familiar 500 g a 1 kg sin azucar': ['yogurt griego', 'yogurt proteico'],
 'Tes helados sin azucar': ['te helado'],
 'Pan de masa madre': ['pan de masa madre'],
 'Kimchi y fermentados de verdura': ['kimchi', 'alimentos fermentados'],
 'Tofu y proteina vegetal': ['tofu', 'proteina vegetal'],
 'Creatina en gomitas y formatos nuevos': ['creatina'],
 'Productos sin sellos': ['sin sellos'],
 'Chai latte en polvo o concentrado': ['chai latte'],
 'Comida liofilizada de montana (outdoor y trekking)': ['comida liofilizada'],
 'Fruta liofilizada como snack': ['fruta liofilizada'],
 'Ginger beer sin alcohol': ['ginger beer'],
 'Agua de coco': ['agua de coco'],
 'Compra al por mayor en linea (canal)': ['bebidas por mayor', 'tienda a granel'],
}
# termino mas cercano al producto (los terminos paraguas, como 'electrolitos' o 'matcha', inflan el nivel)
CLAVE = {
 'Sobres y tabletas de electrolitos': 'electrolitos en sobre', 'Cafe o batido proteico listo para beber 20-30 g': 'batido de proteina',
 'Avena barista para cafeterias (foodservice)': 'leche de avena barista', 'Matcha listo para beber': 'matcha latte',
 'Cold brew local sin azucar': 'cold brew', 'Granola con legumbre a bajo precio (marca propia)': 'granola',
 'Leche sin lactosa y sin lactosa como atributo': 'leche sin lactosa', 'Jugos prensados en frio y shots': 'jugo prensado en frio',
 'Agua con gas saborizada sin azucar en formato familiar': 'agua con gas saborizada', 'Snack horneado de lentejas o garbanzo': 'chips de garbanzo',
 'Yogur griego proteico formato familiar 500 g a 1 kg sin azucar': 'yogurt proteico', 'Tes helados sin azucar': 'te helado',
 'Pan de masa madre': 'pan de masa madre', 'Kimchi y fermentados de verdura': 'kimchi', 'Tofu y proteina vegetal': 'tofu',
 'Creatina en gomitas y formatos nuevos': 'creatina', 'Productos sin sellos': 'sin sellos', 'Chai latte en polvo o concentrado': 'chai latte',
 'Comida liofilizada de montana (outdoor y trekking)': 'comida liofilizada', 'Fruta liofilizada como snack': 'fruta liofilizada',
 'Ginger beer sin alcohol': 'ginger beer', 'Agua de coco': 'agua de coco', 'Compra al por mayor en linea (canal)': 'bebidas por mayor',
}
vol = {}
for r in csv.DictReader(open(LI + f'{F}_google-ads_volumenes_114.csv', encoding='utf-8-sig')):
    vol[r['termino']] = r
for r in csv.DictReader(open(LI + f'{F}_google-ads_ideas_por_candidata.csv', encoding='utf-8-sig')):
    vol.setdefault(r['idea'], r)
def fmt(n): return f'{int(n):,}'.replace(',', '.')
rows = list(csv.DictReader(open(RADAR, encoding='utf-8-sig')))
cols = [c for c in rows[0].keys() if c not in ('termino_clave_google_ads', 'nivel_termino_clave_mes', 'senal_google_ads')]
for r in rows:
    ts = [(t, vol[t]) for t in MAP[r['oportunidad']] if t in vol]
    nums = [(int(v['busquedas_mes_chile'] or 0), t) for t, v in ts]
    mx = max((n for n, _ in nums), default=0)
    partes = '; '.join(f'{t} {fmt(n)}' for n, t in sorted(nums, key=lambda x: -x[0]))
    cpc = [int(v['cpc_alto_clp']) for _, v in ts if v.get('cpc_alto_clp')]
    comp = {v['competencia'] for _, v in ts if v.get('competencia')}
    extra = []
    if cpc: extra.append(f'CPC alto hasta {fmt(max(cpc))} CLP')
    if comp: extra.append('competencia ' + '/'.join(sorted(c.lower() for c in comp)))
    k = CLAVE[r['oportunidad']]
    r['termino_clave_google_ads'] = k
    r['nivel_termino_clave_mes'] = int(vol[k]['busquedas_mes_chile'] or 0) if k in vol else ''
    r['senal_google_ads'] = (partes + (' | ' + ', '.join(extra) if extra else '')) if partes else 'sin datos'
cols += ['termino_clave_google_ads', 'nivel_termino_clave_mes', 'senal_google_ads']
with open(RADAR, 'w', encoding='utf-8-sig', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(rows)
for r in rows: print(f"{r['nivel_termino_clave_mes']:>6} {r['termino_clave_google_ads'][:24]:24s} {r['oportunidad'][:48]:48s} {r['senal_google_ads']}")
