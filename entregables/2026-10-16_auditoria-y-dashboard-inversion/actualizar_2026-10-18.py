"""Actualización del dashboard con el trabajo del 17-oct (corrección ML y Google Ads, benchmark internacional).
Corre DESPUÉS de build_dash.py. Lee los CSV nuevos del repo (copiados a U) y modifica los JSON de dash/.
"""
import csv, json
B = '/home/claude/analisis'; O = B + '/dash'
U = '/mnt/user-data/uploads/company-builder/datos/limpios/'
L = lambda n: json.load(open(f'{O}/{n}.json'))
S = lambda n, d: json.dump(d, open(f'{O}/{n}.json', 'w'), ensure_ascii=False)
rd = lambda f: list(csv.DictReader(open(U + f, encoding='utf-8-sig')))
num = lambda v: None if v in (None, '') else float(v)

ops = L('oportunidades')
by = {r['nombre_radar']: r for r in ops}

# 1) Google Ads: índice específico corregido en el repo (17-oct)
for a in rd('2026-10-17_google-ads_indice_oportunidades.csv'):
    r = by[a['oportunidad']]
    medido = a['estado_medicion'] == 'medido'
    r['ads_indice'] = num(a['indice_busqueda_especifico']) if medido else None
    r['ads_volumen_especifico'] = num(a['volumen_especifico_aprox']) if medido else None
    r['ads_estado'] = 'Medido' if medido else 'No medido'
    r['ads_termino_amplio'] = 'Sí' if a['termino_clave_demasiado_amplio'] == 'si' else 'No'
    r['ads_cpc_max_clp'] = num(a['cpc_alto_max_especifico_clp'])

# 2) Mercado Libre: resumen por oportunidad y tipo (propuesta automática del 17-oct, sin validar)
TIPO_PRINCIPAL = {  # el tipo que corresponde al producto de la oportunidad
    'Sobres y tabletas de electrolitos': ('sobre', 'CLP/porción'),
    'Cafe o batido proteico listo para beber 20-30 g': ('rtd', 'CLP/L'),
    'Cold brew local sin azucar': ('rtd', 'CLP/L'),
    'Chai latte en polvo o concentrado': ('polvo', 'CLP/kg'),
    'Comida liofilizada de montana (outdoor y trekking)': ('plato', 'CLP/porción'),
}
mlr = rd('2026-10-16_mercadolibre_cl_resumen_oportunidad.csv')
ml_rows = []
for m in mlr:
    ml_rows.append({'clave': f"{m['oportunidad']}|{m['tipo']}|{m['unidad_precio']}", 'oportunidad': by[m['oportunidad']]['oportunidad'], 'id': by[m['oportunidad']]['id'],
                    'tipo': m['tipo'], 'unidad_precio': m['unidad_precio'], 'publicaciones_objetivo': num(m['publicaciones_objetivo']),
                    'n_con_precio': num(m['n_con_precio_unitario']), 'validadas': num(m['validadas']), 'marcas': num(m['marcas_distintas']),
                    'share_top3_pct': num(m['share_top3_pct']), 'p25': num(m['precio_unitario_p25']), 'mediana': num(m['precio_unitario_mediana']),
                    'p75': num(m['precio_unitario_p75']), 'envio_gratis_pct': num(m['envio_gratis_pct'])})
    tp = TIPO_PRINCIPAL.get(m['oportunidad'])
    if tp and (m['tipo'], m['unidad_precio']) == tp:
        r = by[m['oportunidad']]
        r['ml_precio_mediana'] = num(m['precio_unitario_mediana'])
        r['ml_unidad_precio'] = f"{m['unidad_precio']} ({m['tipo']})"
        r['ml_publicaciones'] = num(m['publicaciones_objetivo'])
S('ml_resumen', ml_rows)

# 3) Benchmark internacional (17-oct): nueva columna y familia "Benchmark-internacional"
FAV = lambda d: d.startswith('favorable')
for b in rd('2026-10-17_benchmark-internacional_senal-por-oportunidad.csv'):
    r = by[b['oportunidad_radar']]
    r['intl_etapa'] = b['etapa_global'] or None
    r['intl_direccion'] = b['direccion_senal_internacional'] or None
    r['intl_barrera'] = b['barrera_para_entrante_chico'] or None
    r['intl_confianza'] = b['confianza'] or None
    r['intl_chile'] = b['presencia_chile_vista'] or None
    r['intl_lectura'] = b['lectura'] or None
    fams = [f.strip() for f in r['familias'].split(';') if f.strip()]
    tiene_b = any(f.startswith('Benchmark-internacional') for f in fams)
    if FAV(b['direccion_senal_internacional']) and b['confianza'] in ('alta', 'media') and not tiene_b and r['tipo'] != 'otro':
        fams.append('Benchmark-internacional (17-oct)')
        r['n_familias_estricto'] += 1
    r['familias'] = '; '.join(fams)

# 4) Lecturas preliminares actualizadas con la evidencia nueva
UPD = {
 'Sobres y tabletas de electrolitos': ('Investigar', 'Ahora 3 familias: el benchmark internacional es favorable con confianza alta (los polvos de hidratación crecen afuera; el sobre es lo más fácil de maquilar). Demanda de búsqueda alta pero al ritmo del mercado; hueco de precio en 1.300–2.000 CLP/porción. Resolver primero el sodio añadido (posible ALTO EN SODIO) y la ruta alimento vs suplemento.'),
 'Cafe o batido proteico listo para beber 20-30 g': ('Rebajar', 'Afuera la demanda crece, pero el cuello de botella es fabricar (maquila aséptica o UHT, mínimos altos). En Chile el formato casi no se busca (índice 29) y Euromonitor dice que el café listo para beber cuesta ganar aceptación.'),
 'Avena barista para cafeterias (foodservice)': ('Terreno primero', '"Leche de avena" crece en búsquedas, pero afuera la categoría está madura (leche vegetal −2 % en EE. UU.; Oatly perdió su mayor cliente de cafeterías). Ninguna fuente mide el canal cafeterías y vender ahí choca con los empleos.'),
 'Matcha listo para beber': ('Rebajar', 'Afuera crece, pero la materia prima subió fuerte (tencha +265 %) y aprieta el margen. En Chile el formato listo para beber no tiene búsquedas medibles ni oferta.'),
 'Cold brew local sin azucar': ('Investigar', 'Benchmark favorable con confianza alta (cold brew +16 % en EE. UU. mientras el café listo cae). Importados a ~21.700 CLP/L frente a Briu ~10.000: hay hueco de precio. Sin señal en tendencias de Mercado Libre; riesgos: precio del café y vida útil.'),
 'Yogur griego proteico formato familiar 500 g a 1 kg sin azucar': ('Investigar', 'Mayor crecimiento de búsqueda en Chile (+69 %) y benchmark favorable con confianza alta; el formato familiar casi no está en góndola. Pero es lácteo refrigerado: exige socio lácteo y frío.'),
 'Agua de coco': ('Investigar', 'Benchmark favorable con confianza alta: Vita Coco es el modelo de importación con marca más parecido a lo que el grupo puede hacer. Búsqueda nivel 5.000 y crecimiento cercano a la deriva. Ahora llega a 3 familias. Riesgo: tipo de cambio y abastecimiento.'),
 'Tes helados sin azucar': ('Descartar', 'Afuera es un producto de precio con embotelladoras grandes (benchmark desfavorable) y en Chile la señal de búsqueda es ruido.'),
 'Creatina en gomitas y formatos nuevos': ('Fuera de alcance', 'Suplemento, ya en Falabella y farmacias, con prensa crítica por dosificación. La señal de búsqueda es de creatina en general.'),
 'Agua con gas saborizada sin azucar en formato familiar': ('Radar', 'Búsqueda de "agua con gas" crece fuerte con peak en enero, pero el formato saborizado casi no se busca y afuera la categoría está madura; para un actor chico pesa el costo de mover agua.'),
 'Jugos prensados en frio y shots': ('Postergar', 'El jugo prensado está en declive afuera; lo que crece son los shots funcionales. Ambos piden frío.'),
}
ORDEN = {'Investigar': 1, 'Terreno primero': 2, 'Rebajar': 3, 'Radar': 4, 'Sin señal': 5, 'Postergar': 6, 'Atributo': 7, 'Canal': 8, 'Fuera de modelo': 9, 'Fuera de alcance': 10, 'Descartar': 11}
for k, (v, t) in UPD.items():
    by[k]['veredicto_preliminar'] = v; by[k]['orden_veredicto'] = ORDEN[v]; by[k]['lectura'] = t
by['Matcha listo para beber']['ads_volumen_especifico'] = None
S('oportunidades', ops)

# 5) Estado de los errores tras la corrección del 17-oct
ESTADO = {
 'GOO-01': 'Corregido 17-oct', 'GOO-02': 'Corregido 17-oct', 'GOO-03': 'Corregido 17-oct', 'GOO-04': 'Corregido 17-oct',
 'MER-01': 'Corregido 17-oct', 'MER-02': 'Corregido 17-oct', 'MER-04': 'Corregido 17-oct', 'MER-05': 'Corregido 17-oct', 'MER-15': 'Corregido 17-oct',
 'MER-03': 'En corrección (falta actualizar el radar)', 'MER-06': 'En corrección (falta validar)', 'MER-08': 'En corrección (falta validar marcas)', 'MER-09': 'En corrección (falta validar)',
}
err = L('errores')
for e in err: e['estado'] = ESTADO.get(e['id'], 'Abierto')
S('errores', err)
hal = L('hallazgos')
for i, (h, ev, c) in enumerate([
 ('El modelo que más se repite afuera con poco capital es marca propia con maquila o importación (Vita Coco, LMNT, Score).', 'Benchmark internacional, 6 barridos con control cruzado de 9 fuentes (17-oct).', 'media'),
 ('Señal internacional favorable con confianza alta: electrolitos en sobre, cold brew, yogur griego familiar y agua de coco.', 'datos/limpios/2026-10-17_benchmark-internacional_senal-por-oportunidad.csv', 'alta'),
 ('Desfavorable para un entrante chico: granola, leche sin lactosa, té helado sin azúcar y creatina en gomitas.', 'Misma tabla: categorías maduras, de precio o dominadas por grandes.', 'media'),
 ('Cold brew crece afuera mientras el café listo para beber en general cae.', 'Circana 2025: cold brew EE. UU. +16 % (USD 244 M); café y té listos para beber −2 %.', 'alta'),
 ('En Chile la marca propia pesa poco en supermercados, lo que deja espacio a marcas nuevas pero también indica poca maquila para supermercado.', 'NIQ, primer semestre 2026: marca propia 13,4 % del supermercado.', 'media'),
], 1):
    hal.append({'id': f'BEN-H{i:02d}', 'fuente': 'Benchmark internacional (17-oct)', 'hallazgo': h, 'evidencia': ev, 'confianza': c, 'confianza_detalle': c})
S('hallazgos', hal)
print({k: sum(1 for e in err if e['estado'] == k) for k in set(e['estado'] for e in err)})
print(sum(1 for e in err if e['severidad'] == 'alta' and e['estado'] == 'Abierto'))
print([(r['oportunidad'], r['n_familias_estricto']) for r in ops if r['n_familias_estricto'] >= 3])
