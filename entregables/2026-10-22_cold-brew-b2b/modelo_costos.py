"""Modelo de costos por unidad del cold brew B2B (Santiago). Boris con Claude, 2026-10-22.
Cada supuesto lleva C (dato citado, ver informe) o S (supuesto, hay que medirlo o cotizarlo).
Uso: python modelo_costos.py  -> escribe datos/limpios/2026-10-22_cold-brew_modelo-costos.csv
"""
import csv, os, math

P = dict(
    rend_l_kg=4.17,          # C Toddy: 2,27 kg -> 9,46 L concentrado (1:5)
    cafe_com_kg=16990,       # C cafealmayor.cl, 36+ kg
    cafe_esp_kg=28000,       # C tuesta.cl / Luz mayorista (27.990-29.736)
    filtro_l=156,            # C filtro Toddy US$1,50 por 9,46 L
    agua_energia_l=30,       # S
    bib_l=300,               # S bolsa 10 L (~140/L, C) + caja y flete (~160/L, S)
    botella_l=818,           # C vidrio 1 L Cristal Pack
    merma=0.10,              # S vencimiento con vida util de 7 dias
    porcion_ml=80,           # S dilucion 1:2 (~240 ml de bebida + hielo); Tuesta usa 50 ml
    despacho_visita=4000,    # S ruta propia ~10 visitas/dia a ~40.000 CLP/dia
    visitas_mes=4.3,         # S vida util 7 dias -> 1 visita semanal por cuenta
    precio_bib_l=9000,       # S neto: porcion de 80 ml = 720 CLP (~19 % de un vaso de 3.700 neto)
    precio_bot_l=11000,      # S neto: bajo Briu (13.990 con IVA = 11.756 neto)
    operador_mes=400000,     # S media jornada con leyes sociales
    cocina={'CoCook 48 h': 575520, 'Kutt 18 m2 + servicios': 1138000},  # C (+100k servicios S)
    capex={'2 tanques 190 L (+30 % flete e impuestos)': 2*1178000*1.3,
           'refrigerador 1.300 L': 2130490,
           'pH-metro, refractometro, utensilios': 500000,       # S
           'estudio de vida util y desafio (laboratorio)': 1500000,  # S por cotizar
           'resolucion sanitaria y tramites': 300000},          # C rango 12.100-899.700
    kit_nitro=(249.95+165.89+124.95)*981.86*1.3,  # C KegOutlet + 30 % S
    vol_cuenta={'cafeteria o restaurante': (24, 10), 'oficina o coworking': (16, 8)},  # S L/mes verano, invierno
)

def costo_var_l(cafe_kg, envase_l):
    base = cafe_kg / P['rend_l_kg'] + P['filtro_l'] + P['agua_energia_l'] + envase_l
    return base / (1 - P['merma'])

filas = []
def fila(escenario, indicador, valor, unidad, nota=''):
    filas.append(dict(escenario=escenario, indicador=indicador, valor=round(valor), unidad=unidad, nota=nota))

for cafe, ck in [('comercial', P['cafe_com_kg']), ('especialidad', P['cafe_esp_kg'])]:
    for env, el, pr in [('bag-in-box', P['bib_l'], P['precio_bib_l']), ('botella 1 L', P['botella_l'], P['precio_bot_l'])]:
        cv = costo_var_l(ck, el)
        esc = f'cafe {cafe} / {env}'
        fila(esc, 'costo variable por litro', cv, 'CLP/L', 'incluye merma')
        fila(esc, 'costo variable por porcion', cv * P['porcion_ml'] / 1000, 'CLP/porcion')
        fila(esc, 'precio de venta', pr, 'CLP/L neto', 'supuesto')
        fila(esc, 'margen bruto', 100 * (pr - cv) / pr, '%')

# punto de equilibrio: cafe comercial, bag-in-box, cuentas tipo cafeteria
cv = costo_var_l(P['cafe_com_kg'], P['bib_l'])
for cocina, fijo_cocina in P['cocina'].items():
    for oper, fijo_op in [('socios sin sueldo', 0), ('con operador', P['operador_mes'])]:
        fijo = fijo_cocina + fijo_op
        for tipo, (lv, li) in P['vol_cuenta'].items():
            for est, l in [('verano', lv), ('invierno', li)]:
                contrib_cuenta = l * (P['precio_bib_l'] - cv) - P['visitas_mes'] * P['despacho_visita']
                n = math.ceil(fijo / contrib_cuenta) if contrib_cuenta > 0 else float('nan')
                esc = f'{cocina} / {oper} / {tipo} / {est}'
                fila(esc, 'contribucion por cuenta al mes', contrib_cuenta, 'CLP/mes')
                fila(esc, 'cuentas para cubrir costos fijos', n, 'cuentas')
                fila(esc, 'litros al mes en equilibrio', n * l, 'L/mes')

capex = sum(P['capex'].values())
fila('inversion inicial', 'equipos, laboratorio y tramites', capex, 'CLP')
fila('inversion inicial', 'kit nitro en comodato por cuenta', P['kit_nitro'], 'CLP/cuenta')
lv = P['vol_cuenta']['cafeteria o restaurante'][0]
contrib = lv * (P['precio_bib_l'] - cv) - P['visitas_mes'] * P['despacho_visita']
fila('inversion inicial', 'meses para recuperar un kit nitro (cafeteria, verano)', P['kit_nitro'] / contrib, 'meses')

# maquila: tarifa maxima por litro para igualar la dark kitchen
for cocina, fijo_cocina in P['cocina'].items():
    for vol in (500, 1000, 3000):
        tarifa_max = (fijo_cocina + P['operador_mes']) / vol + P['agua_energia_l'] + P['filtro_l']
        fila(f'maquila vs {cocina} con operador', f'tarifa maxima de maquila a {vol} L/mes', tarifa_max, 'CLP/L',
             'sobre esta tarifa conviene la dark kitchen')

# lado del cliente: costo de hacerlo ella misma (DIY) vs comprarnos
diy = (P['cafe_com_kg'] / P['rend_l_kg'] + P['filtro_l']) / (1 - P['merma']) + 2 * 5000 / 10  # S 2 h de barista por 10 L
fila('cliente', 'costo por litro si la cafeteria lo hace ella misma', diy, 'CLP/L', 'cafe comercial, 2 h de barista por 10 L (S)')
fila('cliente', 'costo por porcion si nos compra', P['precio_bib_l'] * P['porcion_ml'] / 1000, 'CLP/porcion')
fila('cliente', 'margen por vaso de 3.700 neto si nos compra', 100 * (1 - P['precio_bib_l'] * P['porcion_ml'] / 1000 / 3700), '%')

out = os.path.join(os.path.dirname(__file__), '..', '..', 'datos', 'limpios', '2026-10-22_cold-brew_modelo-costos.csv')
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(filas[0]))
    w.writeheader(); w.writerows(filas)
for r in filas: print(f"{r['escenario']:<70} | {r['indicador']:<55} | {r['valor']:>10} {r['unidad']}")
