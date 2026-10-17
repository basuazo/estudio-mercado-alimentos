# Auditoría de Google Trends y Meta Ads Library

Alcance: archivos de Trends (12 y 13 de octubre de 2026) y Meta (12 de octubre), cruzados con el radar de oportunidades del 16 de octubre. Solo lectura sobre el repositorio. Datos de apoyo en `datos.json` (misma carpeta).

**Nota de confiabilidad: B** (Trends B, Meta C). **Utilidad: media.**

## 1. Inventario

| Archivo | Filas | Rango | Método |
| --- | --- | --- | --- |
| crudos/…google-trends_cl_2anios_individual.csv (12-oct) | 106 semanas × 42 términos | 2024-10-06 a 2026-10-11 | Un término por consulta (índice 0–100 relativo a sí mismo), Chile, todas las categorías, búsqueda web. Capturado a mano desde el Chrome de Boris. 3 columnas vacías. |
| crudos/…individual_100.csv (13-oct) | 106 × 100 | ídem | Mismo método. Las primeras 42 columnas son idénticas a las del archivo del 12-oct (misma captura reutilizada); 58 términos nuevos capturados el 13-oct con esperas por límite de frecuencia. 5 columnas vacías. |
| crudos/…consultas-en-aumento.csv | 69 | sin periodo declarado | Consultas "en aumento" de 28 términos base, sin volumen ni ventana de comparación. |
| limpios/…resumen.csv / resumen_100.csv | 42 / 100 | 2024-10-06 a 2026-10-04 | Indicadores por término. 51 términos "suficiente", 5 "media", 39 "baja", 5 "sin datos". |
| limpios/…series-largo.csv / series-largo_100.csv | 1.470 / 5.880 | 2024-10-06 a 2026-10-04 | 14 y 56 términos × 105 semanas; idénticos al crudo (0 diferencias). |
| crudos/…meta-ads-library_cl_busquedas.csv | 8 | captura única 2026-10-12 | Conteo aproximado de anuncios activos por palabra clave, ~50 piezas revisadas. |
| limpios/…meta-ads_marcas-activas.csv | 10 | anuncios activos del 2025-01-29 al 2026-10-08 | 10 marcas elegidas a mano. |

Granularidad: semanal (domingo a sábado), 105 semanas completas más una parcial (2026-10-11) que quedó en los crudos. Todos los términos se pidieron de a uno: cada serie está normalizada a su propio máximo (0–100). Las series no son comparables en volumen entre sí. El "índice de volumen vs granola" salió de comparaciones en grupos de 5 que no se guardaron.

## 2. Qué cuadra y qué no

**Cuadra.** Recalculé promedio año 2 vs año 1 desde las series para los 51 términos con datos suficientes. Diferencia mediana 0,4 pp y máxima 3,1 pp (por la ventana exacta de semanas). Ejemplos del resumen: electrolitos +13 % (recalculado +12,8), whey +21 % (+19,2), proteína +3 % (+1,7), kefir +44 % (+41), yogurt griego +70 % (+69). No hay fechas duplicadas ni huecos. El orden del índice de volumen coincide con los niveles de Google Ads del radar (creatina ×6,8 en Trends vs ×10 en Ads).

**No cuadra o engaña** (evidencia completa en `datos.json`, `errores_detectados`):

1. **"Último trimestre" mal definido (alta).** La columna `var_ult13sem_vs_prim13sem_pct` compara jul–oct 2026 con oct–dic 2024. Con el mismo trimestre del año anterior: proteína −0,4 % (el resumen dice +22 %), kimchi +68 % (+110 %), pan de masa madre +19 % (+109 %), electrolitos +6,5 % (+20 %), whey +5 % (+26 %), creatina −0,8 % (+39 %). El radar usa tres de estas cifras.
2. **Variaciones de términos sin señal (alta).** 39 términos tienen 79–99 % de semanas en cero (umbral de privacidad de Google). El resumen igual calcula variación: meal prep +1435 %, agua saborizada +189 %, sin sellos +176 %, colación saludable +183 %. El radar cita "sin sellos +176 %", "saborizada +189 %", "té helado +40 %" (41 % ceros) y "alimentos fermentados −79 %" (97 % ceros).
3. **Deriva común (media).** Mediana de variación de los 51 términos confiables: +8,7 %; 65 % sube; factor común +5,5 % interanual. Un +9 a +12 % (sin azúcar, chía, avena, mantequilla de maní) no es señal.
4. **Semana parcial (media).** Los crudos traen 2026-10-11: 31 series caen más de 20 % y 20 términos quedan en cero.
5. **"Consultas en aumento" (media).** Los porcentajes no tienen volumen base ni periodo declarado. "+450 % sobres de electrolitos" y "+350 % electrolitos en sobre" son la misma familia; "extra life" aparece dos veces; +3600 %, +4800 % y +5000 % son lanzamientos de marca o consultas en inglés. Sirve como pista cualitativa de formatos, no como magnitud.
6. **Términos ambiguos (media).** Granola puede estar inflada por la app Granola AI (aparece como consulta en aumento); matcha por lanzamientos de marca.
7. **Cold brew y meal prep (media).** Correlación semanal 0,86 entre dos términos sin relación: artefacto de muestreo. El +183 % de cold brew tiene confianza baja.
8. **Índice de volumen no auditable (media).** Ver sección 1.
9. **Meta (media).** Ver sección 4.
10. **Menores (baja).** 12 términos cambiaron de categoría entre los dos resúmenes. La advertencia "valores distintos de cero solo en las últimas 3 semanas" vale para 8 términos, no para todos los de baja señal.

## 3. Limitaciones y cómo resolverlas

| Limitación | Impacto | Cómo resolver | Quién |
| --- | --- | --- | --- |
| Índice relativo por término, sin volumen absoluto | No dimensiona mercado | Volumen del Planificador de Google Ads para la lista corta y los formatos | Mario |
| Solo 2 años (2 ciclos) | Estacionalidad confiable solo donde repite con claridad | Bajar 5 años mensuales con un término de control | Boris |
| Términos genéricos y de formato bajo el umbral de Google | Formatos RTD, sobres, gomitas, prensado en frío no medibles | Google Ads, ventas de Mercado Libre, avisos de prueba | Mario / Chalo |
| Selección de términos y ambigüedad | Sesgo heredado por el radar | Sinónimos, temas de Trends, categoría Alimentos y bebidas | Boris |
| Muestreo de Trends (volumen bajo) | Series inestables | Repetir en 3 días distintos y promediar | Boris |
| Canales foodservice y mayorista fuera de Trends | Sin evidencia de demanda para avena barista y compra por mayor | Llamadas a cafeterías y distribuidores | Chalo |
| Meta es una foto sin gasto ni alcance | Solo inventario de anunciantes | Repetir mensual con totales y sinónimos | Boris |
| Trends mide búsquedas, no ventas | Subestima productos de impulso | Cruzar con Mercado Libre y góndola | Mario |

## 4. Meta Ads Library

- **Muestra:** una sola fecha (2026-10-12), ~50 piezas por búsqueda, 8 palabras clave por frase exacta (granola, amplia) y 10 marcas elegidas a mano. Hay sesgo hacia emprendimientos visibles.
- **Qué mide:** anuncios activos visibles, no inversión, alcance ni ventas. Los conteos por marca son un piso. "Anuncio activo más antiguo" no es la fecha de inicio de la marca.
- **Ruido:** "proteína" (2.800) y "sin azúcar" (2.300) son sobre todo apps y suplementos; Mundo Verde Pro suma 107 piezas.
- **Inconsistencias:** EasyProtein figura con 10 anuncios en el CSV de marcas y ~360 resultados en la búsqueda; The Not Company "8+" queda como 8; GoNat sin producto confirmado; la búsqueda de NotCo no cargó.
- **Inferencia riesgosa:** "leche de avena ≈ 8 anuncios" y "yogurt griego ≈ 62, casi sin marcas" se leyeron como espacio libre. La frase exacta no captura "bebida de avena" ni nombres de marca. No se puede concluir ausencia de competencia.
- **Uso razonable:** lista de anunciantes y mensajes (colación, sin sellos, pocos ingredientes) y fecha de actividad. Nota C.

## 5. Análisis por término (100 términos)

Metodología: promedio de 52 semanas contra las 52 previas; trimestre contra el mismo trimestre del año anterior; estacionalidad sobre medias mensuales sin tendencia lineal (pico, amplitud pico/valle, repetición del mes de pico y correlación entre año 1 y año 2); volatilidad como dispersión semanal alrededor de una media móvil; % de semanas en cero. Una serie es "ruido" si tiene ≥30 % de ceros o media <10, o si es un pico puntual. "Estacional" exige amplitud ≥1,5, correlación ≥0,5 y mes de pico repetido (±1 mes).

Resultado: 4 crecientes estacionales, 19 crecientes estables, 23 planos, 8 decrecientes y 46 ruido (39 de baja señal, 5 sin datos, barra de cereal con 40 % de ceros y kefir como pico puntual). Tabla completa en `datos.json` > `tablas.terminos`.

### Crecen por encima de la deriva (exceso sobre la mediana +8,7 %)

| Término | Var. 12 m | Trimestre interanual | Exceso | Pico | Clasificación |
| --- | --- | --- | --- | --- | --- |
| yogurt griego | +69 % | +61 % | +61 pp | ago | creciente estable |
| agua con gas | +47 % | +37 % | +38 pp | ene | creciente estacional |
| leche de avena | +42 % | +42 % | +34 pp | ago | creciente estable |
| pan de masa madre | +41 % | +19 % | +33 pp | jul | creciente estable |
| granola | +39 % | +52 % | +31 pp | ago | creciente estacional |
| kimchi | +32 % | +68 % | +24 pp | ago | creciente estable |
| matcha | +29 % | +11 % | +20 pp | feb | creciente estable |
| tofu | +24 % | +50 % | +15 pp | ago | creciente estable |
| leche sin lactosa | +22 % | +16 % | +14 pp | ago | creciente estable |
| jugo natural | +25 % | +11 % | +16 pp | ene | creciente estable |
| whey protein | +19 % | +5 % | +10 pp | mar | creciente estable |
| cold brew | +184 % | +513 % | n/c | feb | creciente estable (confianza baja, base 11 → 32) |

### Planos, en deriva o estancados

proteína (+1,7 %), fibra, sin gluten, frutos secos, quinoa, legumbres (−0,3 %), almendras, stevia, limonada, hummus (+4 %), avena (+9 %), mantequilla de maní (+8 %), sin azúcar (+12 %, exceso +3 pp), chía (+11 %), electrolitos (+13 %, exceso +4 pp), creatina (+15 % anual pero −0,8 % interanual).

### Caen

probióticos −28 %, keto −25 %, espirulina −24 %, pistachos −20 %, cúrcuma −15 %, harina de almendras −14 %, vegano −14 %, colágeno hidrolizado −11 % (colágeno −9 %, interanual −26 %).

### Pico puntual

Kefir: +41 % anual por un pico nov-25 a ene-26 (88–91); interanual −45 %; oct-26 = 25, bajo oct-24 = 34.

### Estacionalidad

- **Verano austral (pico enero):** agua con gas (amplitud 1,9) y agua mineral (2,1) repiten en ambos años; verano/invierno ×1,3–1,7 y ×1,4–1,6. Kombucha tiene un ×1,25 de verano, pero está plana. Té helado muestra el verano más fuerte (ene-25 = 69, ene-26 = 87, invierno ≈ 0) con 41 % de ceros, así que solo es direccional. Hidratación y electrolitos tienen estacionalidad débil (amplitud 1,25–1,3); el pico de hidratación de jun-26 es del Mundial.
- **Invierno (jun–ago):** granola, mantequilla de maní, avena, harina de avena, legumbres, nueces. Verano/invierno entre 0,6 y 0,8.
- **Sin ciclo repetible:** yogurt griego, leche de avena, tofu, kimchi, pan de masa madre, sin lactosa.

## 6. Mapeo a las 23 oportunidades del radar

| Oportunidad | Términos de Trends | Var. 12 m | Interanual trim. | Clasificación | Calidad de la señal |
| --- | --- | --- | --- | --- | --- |
| Sobres y tabletas de electrolitos | electrolitos, hidratación, suero oral, agua con electrolitos | +12,8 % | +6,5 % | creciente estable (cerca de la deriva) | proxy |
| Café o batido proteico listo para beber 20-30 g | proteína, whey, proteína en polvo, batido/bebida/leche proteica | +19,2 % (whey) | +5,2 % | creciente estable | proxy (formato sin volumen) |
| Avena barista para cafeterías (foodservice) | leche de avena, bebida vegetal, leche de almendras | +42,5 % | +42,1 % | creciente estable | proxy (no mide foodservice) |
| Matcha listo para beber | matcha | +28,7 % | +11,1 % | creciente estable | proxy (mezcla polvo y latte) |
| Cold brew local sin azúcar | cold brew | +184 % | +513 % | creciente estable (confianza baja) | directa débil |
| Granola con legumbre a bajo precio | granola, legumbres | +39,3 % | +51,6 % | creciente estacional (invierno) | directa |
| Leche sin lactosa y sin lactosa como atributo | leche sin lactosa, sin lactosa | +22,5 % | +15,7 % | creciente estable; el atributo está plano | directa |
| Jugos prensados en frío y shots | jugo natural, prensado en frío, shot de jengibre | +24,9 % | +11,2 % | creciente estable (solo jugo natural) | proxy |
| Agua con gas saborizada sin azúcar en formato familiar | agua con gas, agua saborizada, agua mineral | +46,7 % | +36,6 % | creciente estacional | proxy (saborizada es ruido) |
| Snack horneado de lentejas o garbanzo | legumbres, hummus, chips de garbanzo | +4,4 % (hummus) | +42,4 % | plano | proxy |
| Yogur griego proteico formato familiar 500 g a 1 kg sin azúcar | yogurt griego, yogurt proteico | +69,4 % | +61,4 % | creciente estable | proxy (el formato solo aparece en consultas) |
| Tés helados sin azúcar | té helado, bebida sin azúcar | no confiable | no confiable | ruido (verano evidente) | débil |
| Pan de masa madre | pan de masa madre | +41,4 % | +19,1 % | creciente estable | directa |
| Kimchi y fermentados de verdura | kimchi, alimentos fermentados | +32,3 % | +68,2 % | creciente estable (fermentados = ruido) | directa |
| Tofu y proteína vegetal | tofu, proteína vegetal | +24,2 % | +49,7 % | creciente estable; proteína vegetal plana | directa |
| Creatina en gomitas y formatos nuevos | creatina | +14,7 % | −0,8 % | plano (volumen muy alto) | directa (categoría) |
| Productos sin sellos | sin sellos | no confiable (70 % ceros) | — | ruido | débil |
| Chai latte en polvo o concentrado | sin término | — | — | sin datos | nula |
| Comida liofilizada de montaña (outdoor y trekking) | sin término | — | — | sin datos | nula |
| Fruta liofilizada como snack | fruta deshidratada (98 % ceros) | — | — | ruido | nula |
| Ginger beer sin alcohol | sin término | — | — | sin datos | nula |
| Agua de coco | agua de coco | +17,4 % | +24,7 % | creciente estable | directa |
| Compra al por mayor en línea (canal) | tienda a granel (99 % ceros) | — | — | ruido | nula |

Cruce con la columna `senal_trends_chile` del radar: coinciden o son aceptables electrolitos +13 %, leche de avena +43 %, matcha +29 %, granola +40 %, agua con gas +47 %, yogurt griego +70 %, tofu +23 %, agua de coco, creatina +16 %. Hay que corregir:

- **Café o batido proteico:** "proteína +3 % (últ. trimestre +22 %)" → proteína está plana (−0,4 % interanual).
- **Pan de masa madre:** "últ. 13 sem +109 %" → +19 % interanual.
- **Kimchi y fermentados:** "últ. 13 sem +110 %" → +68 % interanual; "fermentados −79 %" es ruido.
- **Productos sin sellos:** "+176 %" no es una tendencia (70 % ceros).
- **Agua con gas saborizada:** "saborizada +189 %" es ruido; la evidencia vale para agua con gas sin saborizar.
- **Tés helados:** "+40 %" con 41 % de ceros.
- **Leche sin lactosa:** "sin lactosa +11 %" es deriva del mercado (+0,6 % interanual).
- **Snack de lentejas o garbanzo:** "legumbres 0 %; hummus +4 %" confirma demanda plana, no solo ausencia de datos.
- **Cuatro oportunidades sin término en Trends:** chai latte, comida liofilizada, ginger beer y fruta liofilizada (capturar 'chai latte', 'comida liofilizada', 'ginger beer', 'fruta liofilizada').

## 7. Tendencias y ciclos para decidir inversión

1. **Qué crece de verdad:** yogurt griego, leche de avena, agua con gas, pan de masa madre, granola, kimchi, tofu, matcha y leche sin lactosa superan la deriva del mercado en más de 14 pp. Confianza alta en yogurt griego, leche de avena y agua con gas.
2. **Qué es deriva o estancamiento:** sin azúcar, chía, avena, mantequilla de maní, electrolitos, proteína y creatina. Son categorías grandes y estables, no oportunidades de crecimiento.
3. **Qué cae o se acabó:** probióticos, keto, espirulina, pistachos, cúrcuma, vegano, colágeno; kefir fue moda.
4. **Qué es solo estacional:** agua mineral y té helado (verano, enero); mantequilla de maní, legumbres, avena, harina de avena y nueces (invierno). Granola y agua con gas combinan estación con crecimiento.
5. **Cuándo lanzar:** para productos de verano, estar en góndola o venta en octubre–noviembre. Hoy es 16 de octubre: para desarrollo propio la ventana realista es el verano 2027–28; solo importación o reetiquetado llegan al verano 2026–27. Para invierno (granola, avena), lanzar entre marzo y mayo. Yogurt griego, leche de avena, tofu, kimchi y pan de masa madre no dependen de la estación.
6. **Qué no se puede concluir con Trends:** formatos (listo para beber, sobres, gomitas, prensado en frío, saborizada), canales (foodservice, mayorista) y tamaño de mercado. Requieren Google Ads, Mercado Libre y trabajo de campo.

## 8. Próximos pasos propuestos

1. Corregir las filas del radar señaladas en la sección 6 y la columna `var_ult13sem_vs_prim13sem_pct` (o reemplazarla por el interanual).
2. Vaciar las variaciones de términos con ≥30 % de ceros en los resúmenes.
3. Capturar series para chai latte, comida liofilizada, ginger beer, fruta liofilizada, matcha latte, electrolitos en sobre y leche de avena barista; repetir granola, matcha y cold brew con categoría Alimentos y bebidas.
4. Bajar 5 años mensuales para los ~25 términos clave y validar la estacionalidad.
5. Traer volumen absoluto desde Google Ads para la lista corta.
