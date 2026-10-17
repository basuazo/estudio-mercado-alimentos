"""Integra las auditorías por fuente en datasets JSON para el dashboard.
Entrada: /home/claude/analisis/<fuente>/datos.json (generados por los subagentes auditores).
Salida: /home/claude/analisis/dash/*.json
"""
import json, os
B = '/home/claude/analisis'
O = B + '/dash'
os.makedirs(O, exist_ok=True)
L = lambda f: json.load(open(f'{B}/{f}/datos.json'))
t, m, a, x, me = L('trends_meta'), L('mercadolibre'), L('google_ads'), L('macro'), L('metodo')
mj = json.load(open(f'{B}/mejoras/fuentes_estrategias.json'))

import statistics
_v = [r['var_12m_pct'] for r in t['tablas']['terminos'] if r.get('pct_ceros') is not None and r['pct_ceros'] <= 5 and r.get('var_12m_pct') is not None and r.get('clasificacion') != 'ruido']
DERIVA = statistics.median(_v)  # mediana 12 m de términos con <=5 % de semanas en cero y sin clasificar como ruido
for _r in t['tablas']['terminos']:
    _r['exceso_vs_mediana_pp'] = None if _r.get('var_12m_pct') is None else round(_r['var_12m_pct'] - DERIVA, 1)

T = {r['oportunidad']: r for r in t['metricas_por_oportunidad']}
M = {r['oportunidad']: r for r in m['metricas_por_oportunidad']}
A = {r['oportunidad']: r for r in a['metricas_por_oportunidad']}
X = {r['oportunidad']: r for r in x['metricas_por_oportunidad']}
F = {r['oportunidad']: r for r in me['fuentes_independientes']}
Q = {r['oportunidad']: r for r in me['evaluacion_cualitativa']}

# Nombre corto y lectura preliminar del auditor (juicio de Claude a partir de las auditorías; no es dato)
CORTO = {
 'Sobres y tabletas de electrolitos': ('Electrolitos en sobre', 'Investigar', 'Demanda de búsqueda alta y estable, pero crece al ritmo del mercado; 26 marcas. Hueco de precio en 1.300–2.000 CLP/porción. Resolver antes el sodio añadido (posible ALTO EN SODIO) y el límite con sales de rehidratación.'),
 'Cafe o batido proteico listo para beber 20-30 g': ('Café/batido proteico RTD', 'Rebajar', 'El formato listo para beber casi no se busca (términos con 90–99 % de semanas en cero); la gente busca polvo y marcas. Maquila UHT exige mucho capital.'),
 'Avena barista para cafeterias (foodservice)': ('Avena barista', 'Terreno primero', '"Leche de avena" crece fuerte (+42 %) en consumo final, pero 0 familias miden el canal cafeterías. Vender a cafeterías choca con los empleos actuales.'),
 'Matcha listo para beber': ('Matcha RTD', 'Rebajar', 'Matcha como categoría crece, pero el formato listo para beber no registra búsquedas (Ads 50) ni oferta. Queda en radar.'),
 'Cold brew local sin azucar': ('Cold brew', 'Investigar', 'Trends muestra un alza grande pero de baja confianza (serie ruidosa); Ads nivel 5.000. Importados a ~22.000 CLP/L frente a Briu ~10.000: hay hueco de precio. Sin señal en tendencias de ML. Revisar vida útil.'),
 'Granola con legumbre a bajo precio (marca propia)': ('Granola con legumbre', 'Descartar', 'Categoría saturada; el término específico no se midió. Suma 4 familias de señales, lo que muestra que la regla cuenta señales, no atractivo.'),
 'Leche sin lactosa y sin lactosa como atributo': ('Leche sin lactosa', 'Descartar', 'Demanda real pero dominada por lácteas grandes; sin espacio para un entrante con poco capital.'),
 'Jugos prensados en frio y shots': ('Jugos prensados en frío', 'Postergar', 'Crecimiento moderado; requiere cadena de frío y vida útil corta: falla el filtro operativo propuesto.'),
 'Agua con gas saborizada sin azucar en formato familiar': ('Agua con gas saborizada', 'Investigar', '"Agua con gas" crece +47 % con peak en enero, pero el término específico tiene nivel 50. Medir el formato; la ventana de verano 2026–27 ya está encima.'),
 'Snack horneado de lentejas o garbanzo': ('Snack de legumbres', 'Descartar', 'Señales planas o sin volumen (chips de garbanzo nivel 50; 0 de 30 en ML).'),
 'Yogur griego proteico formato familiar 500 g a 1 kg sin azucar': ('Yogur griego familiar', 'Investigar', 'Crecimiento más fuerte y confiable de Trends (+69 %). Pero es lácteo refrigerado: capital y frío. Explorar maquila láctea o reventa.'),
 'Tes helados sin azucar': ('Té helado sin azúcar', 'Sin señal', 'Trends es ruido y Ads mide el término amplio. Medir "té helado sin azúcar" antes de seguir.'),
 'Pan de masa madre': ('Pan de masa madre', 'Fuera de modelo', 'Demanda real y sin estacionalidad, pero es negocio de panadería (perecible, local).'),
 'Kimchi y fermentados de verdura': ('Kimchi y fermentados', 'Radar', 'Nicho creciente (+32 %); refrigerado. El término "kimchi" infla la demanda del producto.'),
 'Tofu y proteina vegetal': ('Tofu', 'Radar', 'Crece (+24 %); producción y frío complejos.'),
 'Creatina en gomitas y formatos nuevos': ('Creatina en gomitas', 'Fuera de alcance', 'Es suplemento; la señal es de creatina en general y está plana.'),
 'Productos sin sellos': ('Productos sin sellos', 'Atributo', 'Es un atributo transversal, no un producto. Ojo: el sello solo aplica a nutrientes añadidos.'),
 'Chai latte en polvo o concentrado': ('Chai latte', 'Radar', 'Oferta fragmentada (13 marcas) y búsqueda específica baja (~100/mes).'),
 'Comida liofilizada de montana (outdoor y trekking)': ('Comida liofilizada', 'Radar', 'Nicho (~500 búsquedas/mes); pocas marcas visibles.'),
 'Fruta liofilizada como snack': ('Fruta liofilizada', 'Radar', 'Precio muy alto por kg (el rango del radar estaba inflado por packs); demanda de nicho.'),
 'Ginger beer sin alcohol': ('Ginger beer', 'Radar', 'Ads nivel 5.000 pero sin serie en Trends: medir dirección.'),
 'Agua de coco': ('Agua de coco', 'Radar', 'Crece (+17 %) y nivel 5.000; candidata a importar o reetiquetar.'),
 'Compra al por mayor en linea (canal)': ('Compra por mayor en línea', 'Canal', 'Es un canal, no un producto: conecta con Mayorístico.cl.'),
}
ORDEN = {'Investigar': 1, 'Terreno primero': 2, 'Rebajar': 3, 'Radar': 4, 'Sin señal': 5, 'Postergar': 6, 'Atributo': 7, 'Canal': 8, 'Fuera de modelo': 9, 'Fuera de alcance': 10, 'Descartar': 11}

def num(v):
    return None if v is None or v != v else v

def senal_demanda(tr, ad):
    """Regla explícita: combina dirección (Trends sobre la deriva) y nivel (índice Ads de términos específicos)."""
    v = tr.get('var_12m_pct'); clas = tr.get('clasificacion'); idx = ad.get('indice_demanda_busqueda')
    cal = tr.get('calidad_senal') or ''
    valida = v is not None and clas not in ('ruido', 'sin datos') and 'debil' not in cal and 'nula' not in cal and v - DERIVA >= 10
    sobre = valida and 'proxy' not in cal          # el término mide el producto
    sobre_cat = valida and 'proxy' in cal          # solo crece la categoría (término proxy)
    techo = ad.get('termino_demasiado_amplio') and idx is not None and idx == ad.get('indice_techo_termino_clave')
    nivel = idx is not None and idx >= 50 and not techo
    if sobre and nivel: return 'Fuerte'
    if sobre or nivel: return 'Media'
    if sobre_cat: return 'Media (categoría)'
    if idx is not None or (v is not None and clas not in ('ruido', 'sin datos')): return 'Débil'
    return 'Sin dato'

rows = []
for i, (o, r) in enumerate(T.items(), 1):
    tr, ad, ml, mc, fi, q = r, A[o], M.get(o, {}), X[o], F[o], Q.get(o, {})
    corto, veredicto, lectura = CORTO[o]
    v = num(tr.get('var_12m_pct'))
    rows.append({
        'id': f'O{i:02d}', 'oportunidad': corto, 'nombre_radar': o,
        'tipo': None, 'estado_radar': None,
        'n_fuentes_radar': fi['n_fuentes_radar'], 'n_familias_estricto': fi['n_familias_estricto'],
        'familias': '; '.join(fi['familias_con_senal']),
        'trends_var_12m_pct': v,
        'trends_exceso_pp': None if v is None or tr.get('clasificacion') in ('ruido', 'sin datos') else round(v - DERIVA, 1),
        'trends_clasificacion': tr.get('clasificacion'), 'trends_calidad': tr.get('calidad_senal'),
        'trends_mes_peak': num(tr.get('mes_peak')), 'trends_amplitud': num(tr.get('amplitud_estacional')),
        'ads_termino_clave': ad.get('termino_clave'), 'ads_nivel_radar': ad.get('nivel_termino_clave'),
        'ads_volumen_especifico': num(ad.get('volumen_especifico_aprox')), 'ads_indice': num(ad.get('indice_demanda_busqueda')),
        'ads_termino_amplio': 'Sí' if ad.get('termino_demasiado_amplio') else 'No', 'ads_cpc_max_clp': num(ad.get('cpc_max_clp')),
        'ml_publicaciones': num(ml.get('n_publicaciones')), 'ml_marcas': num(ml.get('n_marcas')), 'ml_share_top3_pct': num(ml.get('share_top3')),
        'ml_precio_mediana': num(ml.get('precio_mediana')), 'ml_unidad_precio': ml.get('unidad_precio'),
        'sii_actividad': mc.get('actividad_sii'), 'sii_var_empresas_2022_2024_pct': num(mc.get('var_empresas_2022_2024_pct')),
        'import_partida': mc.get('partida_hs'), 'import_usd_2025': num(mc.get('import_usd_2025')),
        'q_barrera_regulatoria': q.get('barrera_regulatoria'), 'q_capital_entrada': q.get('capital_entrada'),
        'q_complejidad_operativa': q.get('complejidad_operativa'), 'q_intensidad_competitiva': q.get('intensidad_competitiva'),
        'q_encaje_canal': q.get('encaje_canal'),
        'senal_demanda': senal_demanda(tr, ad),
        'veredicto_preliminar': veredicto, 'orden_veredicto': ORDEN[veredicto], 'lectura': lectura,
        'nota_fuentes': fi.get('comentario') or '',
        'nota_trends': tr.get('comentario', ''), 'nota_ads': ad.get('comentario', ''), 'nota_ml': ml.get('comentario', ''), 'nota_macro': mc.get('comentario', ''),
    })
# tipo y estado desde el radar original (vía la auditoría de método no viene; se agregan desde el CSV copiado)
import csv
radar = {r['oportunidad']: r for r in csv.DictReader(open(f'{B}/radar.csv', encoding='utf-8-sig'))}
for r in rows:
    rr = radar[r['nombre_radar']]
    r['tipo'] = rr['tipo']; r['estado_radar'] = rr['estado']
json.dump(rows, open(f'{O}/oportunidades.json', 'w'), ensure_ascii=False)

# Cobertura de la matriz propuesta para las 5 candidatas: qué criterio tiene evidencia hoy
cands = ['Electrolitos en sobre', 'Café/batido proteico RTD', 'Avena barista', 'Matcha RTD', 'Cold brew']
crit = [('Demanda (nivel y dirección)', 15), ('Evidencia de compra y del cliente', 15), ('Hueco de oferta y competencia', 10),
        ('Margen bruto unitario', 20), ('Capital de entrada y MOQ', 10), ('Barrera regulatoria y tiempo a mercado', 10),
        ('Complejidad operativa', 10), ('Encaje con canales propios y empleos', 10)]
est = {
 'Demanda (nivel y dirección)': {'Electrolitos en sobre': 'Con datos', 'Café/batido proteico RTD': 'Parcial', 'Avena barista': 'Parcial', 'Matcha RTD': 'Parcial', 'Cold brew': 'Parcial'},
 'Hueco de oferta y competencia': {c: 'Parcial' for c in cands},
 'Barrera regulatoria y tiempo a mercado': {c: 'Juicio' for c in cands},
 'Complejidad operativa': {c: 'Juicio' for c in cands},
 'Encaje con canales propios y empleos': {c: 'Juicio' for c in cands},
 'Capital de entrada y MOQ': {c: 'Juicio' for c in cands},
}
cob = []
for c, w in crit:
    for cand in cands:
        e = est.get(c, {}).get(cand, 'Sin datos')
        cob.append({'criterio': c, 'peso_pct': w, 'candidata': cand, 'estado': e,
                    'valor': {'Con datos': 1, 'Parcial': 0.5, 'Juicio': 0, 'Sin datos': 0}[e]})
json.dump(cob, open(f'{O}/cobertura_matriz.json', 'w'), ensure_ascii=False)

# Auditoría por fuente
def nota_txt(d):
    n = d['confiabilidad']['nota']; return f'{n}/5' if isinstance(n, (int, float)) else str(n)
fa = []
for clave, d, nombre in [('trends_meta', t, 'Google Trends + Meta'), ('google_ads', a, 'Google Ads Keyword Planner'), ('mercadolibre', m, 'Mercado Libre'),
                         ('macro', x, 'SII + UN Comtrade + distribuidores'), ('metodo', me, 'Benchmark B3, radar y método')]:
    u = d['utilidad']
    fa.append({'fuente': nombre, 'confiabilidad': nota_txt(d), 'utilidad': str(u.get('nota')) + ('/5' if isinstance(u.get('nota'), (int, float)) else ''),
               'para_que_sirve': u['para_que_sirve'] if isinstance(u['para_que_sirve'], str) else ' · '.join(u['para_que_sirve']),
               'razones': ' · '.join(d['confiabilidad']['razones']),
               'errores_alta': sum(e.get('severidad') == 'alta' for e in d['errores_detectados']),
               'errores_total': len(d['errores_detectados']), 'limitaciones': len(d['limitaciones'])})
json.dump(fa, open(f'{O}/fuentes_auditoria.json', 'w'), ensure_ascii=False)

err, lim, hal = [], [], []
for nombre, d in [('Trends + Meta', t), ('Google Ads', a), ('Mercado Libre', m), ('SII + Comtrade', x), ('B3 + radar + método', me)]:
    for k, e in enumerate(d['errores_detectados'], 1):
        err.append({'id': f'{nombre[:3].upper()}-{k:02d}', 'fuente': nombre, 'severidad': e.get('severidad', ''), 'archivo': e.get('archivo', ''),
                    'descripcion': e.get('descripcion', ''), 'evidencia': e.get('evidencia', ''), 'correccion': e.get('correccion', '')})
    for k, e in enumerate(d['limitaciones'], 1):
        lim.append({'id': f'{nombre[:3].upper()}-L{k:02d}', 'fuente': nombre, 'limitacion': e.get('descripcion', ''), 'impacto': e.get('impacto', ''),
                    'como_resolver': e.get('como_resolver', ''), 'responsable': e.get('responsable_sugerido', '')})
    for k, e in enumerate(d['tendencias_y_ciclos'], 1):
        hal.append({'id': f'{nombre[:3].upper()}-H{k:02d}', 'fuente': nombre, 'hallazgo': e.get('hallazgo', ''), 'evidencia': e.get('evidencia', ''), 'confianza': e.get('confianza', '')})
NSEV = {'media-alta': 'alta', 'alta-media': 'alta', 'baja-media': 'media', 'media-baja': 'media'}
for e in err: e['severidad'] = NSEV.get(e['severidad'].strip().lower(), e['severidad'].strip().lower()); e['id'] = e['id'].replace(' ', '')
for e in lim: e['id'] = e['id'].replace(' ', '')
for e in hal: e['confianza_detalle'] = e['confianza']; e['confianza'] = e['confianza'].strip().lower().split(' ')[0].split('-')[0].rstrip(',;'); e['id'] = e['id'].replace(' ', '')
sev = {'alta': 0, 'media': 1, 'baja': 2}
err.sort(key=lambda e: (sev.get(e['severidad'], 3), e['id']))
json.dump(err, open(f'{O}/errores.json', 'w'), ensure_ascii=False)
json.dump(lim, open(f'{O}/limitaciones.json', 'w'), ensure_ascii=False)
json.dump(hal, open(f'{O}/hallazgos.json', 'w'), ensure_ascii=False)

json.dump(t['tablas']['terminos'], open(f'{O}/trends_terminos.json', 'w'), ensure_ascii=False)
json.dump(t['tablas']['serie_mensual'], open(f'{O}/trends_mensual.json', 'w'), ensure_ascii=False)
json.dump(t['tablas']['estacionalidad_mensual'], open(f'{O}/trends_estacionalidad.json', 'w'), ensure_ascii=False)
json.dump(a['tablas']['terminos'], open(f'{O}/ads_terminos.json', 'w'), ensure_ascii=False)
json.dump(m['tablas']['precios_por_termino'], open(f'{O}/ml_precios.json', 'w'), ensure_ascii=False)
json.dump(m['tablas']['marcas_por_termino'], open(f'{O}/ml_marcas.json', 'w'), ensure_ascii=False)
json.dump(x['tablas']['sii_resumen'], open(f'{O}/sii_resumen.json', 'w'), ensure_ascii=False)
json.dump(x['tablas']['importaciones_anual'], open(f'{O}/importaciones_anual.json', 'w'), ensure_ascii=False)
json.dump(x['tablas']['importaciones_resumen'], open(f'{O}/importaciones_resumen.json', 'w'), ensure_ascii=False)
json.dump(me['matriz_propuesta'], open(f'{O}/matriz_propuesta.json', 'w'), ensure_ascii=False)
json.dump(me['brechas_prioritarias'], open(f'{O}/brechas.json', 'w'), ensure_ascii=False)
json.dump(me['regulatorio'], open(f'{O}/regulatorio.json', 'w'), ensure_ascii=False)
fu = [{k: (v if not isinstance(v, list) else '; '.join(map(str, v))) for k, v in f.items()} for f in mj['fuentes']]
for f in fu: f['accesible_para_agente'] = str(f.get('accesible_para_agente'))
json.dump(fu, open(f'{O}/mejoras_fuentes.json', 'w'), ensure_ascii=False)
es = [{k: (v if not isinstance(v, list) else ' → '.join(map(str, v))) for k, v in e.items()} for e in mj['estrategias']]
json.dump(es, open(f'{O}/mejoras_estrategias.json', 'w'), ensure_ascii=False)
for f in sorted(x for x in os.listdir(O) if x.endswith('.json')):
    d = json.load(open(f'{O}/{f}')); print(f, len(d), os.path.getsize(f'{O}/{f}'))
