# Auditoría de datos: Google Ads Keyword Planner

Auditor: Claude · Fecha de la auditoría: 2026-10-16 · Alcance: 4 exportes crudos, 3 limpios, 2 scripts, radar, guía y bitácoras 1825 y 1850. Repositorio leído en modo solo lectura; los números salen de recalcular desde los crudos.

**Veredicto:** confiabilidad **C**, utilidad **B**. El parseo técnico es correcto. El problema está en la señal: con cuenta sin gasto los volúmenes son bandas de 10x, no hay columnas mensuales, y el término clave del radar infla la demanda en 8 de 23 oportunidades.

## 1. Inventario y método

| Archivo | Filas | Qué es |
|---|---|---|
| `keywords-planner-2.csv` | 114 términos (+2 filas agregadas "Todo" y "Chile") | Volúmenes de `terminos-busqueda.csv`, Chile |
| `keyword-planner_ideas.csv` | 310 | Ideas desde la semilla "electrolitos" |
| `keyword-planner_ideas2.csv` | 1.248 | Ideas desde bebida proteica, cold brew, matcha, chai latte |
| `keywords-planner.csv` | 9 | Previsión de campaña "Campaign1", nov-2026. No es demanda |

- **Formato:** UTF-16 LE, tabulado, 2 filas de encabezado de Google (título y período). Los encabezados de `ideas*` vienen en español ("Cambio en tres meses") y los de `planner-2` en inglés ("Three month change"). El script solo lee columnas comunes, así que no falla.
- **Período:** 1-oct-2025 a 30-sep-2026 (12 meses). La guía pide 24; no coincide.
- **Ubicación e idioma:** el CSV solo muestra la segmentación "Chile". Idioma y red no constan (algunas ideas son de España, p. ej. "mercadona"). La bitácora los declara, pero no se pueden auditar.
- **Método de volumen:** cuenta sin gasto, así que Google entrega buckets 50 / 500 / 5.000 / 50.000 / 500.000. Cada uno representa una banda de 10x (10-100, 100-1K, 1K-10K, 10K-100K, 100K-1M). Prueba de que son buckets: las filas "Todo/Chile" suman 2.051.400, que es exactamente 18×50 + 21×500 + 48×5.000 + 26×50.000 + 1×500.000. No es un tamaño de mercado.
- **Distribución de los 114:** 18 / 21 / 48 / 26 / 1 (coincide con la bitácora). Ideas (1.558 únicas): 140 en 0, 1.274 en 50, 46 en 500, 17 en 5.000, 4 en 50.000.

## 2. Auditoría

### Lo que está bien
- Los 114 volúmenes limpios coinciden 114/114 con el crudo; los 114 términos del crudo coinciden con `terminos-busqueda.csv` (ninguno falta ni sobra).
- Las ideas no tienen duplicados exactos (310 + 1.248 = 1.558 únicas); solo 6 se repiten con los 114 y el script conserva el de los 114.
- Las filas agregadas vacías de Google se filtran correctamente (`Keyword` vacío).
- `nivel_termino_clave_mes` del radar coincide con el crudo en las 23 oportunidades.
- `keywords-planner.csv` está bien descartado: son números con coma decimal entrecomillados, sin términos, y los clics salen de presupuesto dividido por CPC.

### Hallazgos (detalle en `datos.json`, `errores_detectados`)
1. **Términos clave demasiado amplios (alta).** Sesgan 1 a 2 niveles en 8 oportunidades:

| Oportunidad | Término clave (nivel) | Específico real |
|---|---|---|
| Matcha listo para beber | matcha latte (5.000) | 0 de 640 ideas son RTD; techo 50 |
| Chai en polvo o concentrado | chai latte (5.000) | ~100 (instantáneo y sobres, 50 c/u) |
| Proteico listo para beber | batido de proteína (5.000) | ~650 (café proteico, bebida proteica, proteína lista para beber) |
| Kimchi y fermentados | kimchi (50.000) | 500 ("alimentos fermentados"); rango 500-50.000 |
| Tofu y proteína vegetal | tofu (50.000) | 5.000 ("proteína vegetal") |
| Tés helados sin azúcar | té helado (5.000) | techo, "sin azúcar" no medido |
| Granola con legumbre | granola (50.000) | no medido |
| Creatina en gomitas | creatina (500.000) | no medido |

2. **Señal mezclada en el radar (media).** CPC y competencia salen del máximo y la unión de todos los términos mapeados:
   - *Snack de garbanzo:* CPC 1.056 viene de "legumbres" (compartido con granola). "Hummus" es otro producto (CPC 5-19). El único término propio, "chips de garbanzo", no tiene CPC. Su "competencia baja/media" no describe el snack.
   - *Electrolitos:* 1.113 viene de "suero oral" (producto médico). El CPC del sobre es 708.
   - *Cold brew:* "baja/media" incluye "cold brew concentrado", que es "Baja" porque nadie puja (volumen 50).
3. **Agrupación por regex (media).** `proteica_rtd` incluye "yogurt proteico", y `electrolitos` incluye "bebida isotónica", "agua con electrolitos" y "suero oral". `matcha` agrupa 640 ideas de té y polvo, ninguna RTD. `compra_por_mayor` omite "tienda a granel".
4. **Conteos inflados por variantes (media).** Chai tiene 7 ideas de 5.000 que son un solo concepto ("chai latte", "chai chai latte", "chai lata", "té chai latte", etc.). Matcha tiene 3 variantes a 50.000. Hay que tomar el máximo por concepto, no sumar.
5. **Cambios de 3 meses e interanual (media).** Son saltos de bucket (+900%, -90%, ∞ = de 0 a 50). Seis de nueve términos comparables contradicen Trends:
   - Creatina: Ads -90% interanual, Trends +16%.
   - Espirulina: Ads +900%, Trends -24%.
   - Leche sin lactosa: Ads -90% en 3 meses, Trends +64% (13 sem.).
   - Miel: Ads -90%, Trends +45%.
   - Nueces: Ads -90%, Trends +21%.
   - Té helado: Ads +900%, Trends -14%.
   
   Concuerdan galletas de arroz, proteína en polvo y yogur griego. El script no lee estas columnas, lo cual es correcto.
6. **Menores (baja).**
   - La guía dice 24 meses y el export tiene 12.
   - La bitácora dice que cold brew tiene "el CPC más bajo de todo el set". Hummus (5-19) y espirulina (16-267) son más bajos.
   - 9 de los 114 no tienen CPC y "bebida proteica café" no tiene competencia, aunque la bitácora dice que "todos vinieron con dato".
7. **Mezcla de intención.** En las ideas, 217 de 1.666 términos son informativos (13%); en electrolitos son 81 de 271 (18% del volumen de ideas). Chai tiene 156 de 438 ideas de marca (David Rio, Marley, Starbucks; 21% del volumen). Solo 63 términos tienen palabras de compra, todos de volumen 50.
8. **"Competition" de Google es de anunciantes**, no de mercado. En términos de 50 búsquedas, "Baja" o "Desconocida" solo refleja que no hay pujas.

## 3. Análisis por oportunidad

**Índice de demanda de búsqueda (0-100).** Se toma la suma de los volúmenes de los términos específicos del producto (sin paraguas, sin informativos, sin marcas, variantes de un mismo concepto colapsadas al máximo). Luego:

`índice = (log10(volumen) − log10(50)) / (log10(500.000) − log10(50)) × 100`

Esto da 0 para el bucket 50, 25 para 500, 50 para 5.000, 75 para 50.000 y 100 para 500.000. Un 0 es el piso del bucket (10-100), no demanda cero. La resolución es un nivel (25 puntos) y el error es de ±0,5 log10 (aprox. ×3). Por eso `datos.json` entrega también `rango_volumen_especifico` (÷3 a ×3) y `indice_techo_termino_clave`, que es el índice del término del radar. Cuando el término clave es demasiado amplio, el índice específico va marcado y el techo queda como cota superior. Si el término específico no se midió (granola, creatina), el índice es nulo.

| Oportunidad | Término clave (nivel) | Vol. específico | Índice | Techo | CPC máx (CLP) | Competencia | Amplio |
|---|---|---|---|---|---|---|---|
| Sobres y tabletas de electrolitos | electrolitos en sobre (5.000) | ~5.050 | 50 | 50 | 708 | Alta | no |
| Café o batido proteico RTD | batido de proteína (5.000) | ~650 | 28 | 50 | 1.166 | Alta | **sí** |
| Avena barista | leche de avena barista (500) | 500 | 25 | 25 | 943 | Alta | no |
| Matcha listo para beber | matcha latte (5.000) | ≤50 | 0 | 50 | 840 | Alta | **sí** |
| Cold brew sin azúcar | cold brew (5.000) | ~5.150 | 50 | 50 | 537 | Media | no |
| Granola con legumbre | granola (50.000) | no medido | n/d | 75 | 1.163 | Alta | **sí** |
| Leche sin lactosa | leche sin lactosa (5.000) | 5.000 | 50 | 50 | 692 | Alta | no |
| Jugos prensados y shots | jugo prensado en frío (500) | ~1.000 | 33 | 25 | 1.099 | Alta | no |
| Agua con gas saborizada | agua con gas saborizada (50) | 50 | 0 | 0 | 1.379 | Alta | no |
| Snack lenteja/garbanzo | chips de garbanzo (50) | 50 | 0 | 0 | sin CPC | Media | no |
| Yogur griego proteico | yogurt proteico (500) | 500 | 25 | 25 | 483 | Alta | no |
| Tés helados sin azúcar | té helado (5.000) | ≤5.000 | 50 (techo) | 50 | 731 | Alta | **sí** |
| Pan de masa madre | pan de masa madre (5.000) | 5.000 | 50 | 50 | 688 | Alta | no |
| Kimchi y fermentados | kimchi (50.000) | ~500 (hasta 50.000) | 25 | 75 | 1.193 | Baja | **sí** |
| Tofu y proteína vegetal | tofu (50.000) | ~5.000 | 50 | 75 | 750 | Media | **sí** |
| Creatina en gomitas | creatina (500.000) | no medido | n/d | 100 | 450 | Alta | **sí** |
| Productos sin sellos | sin sellos (50) | 50 | 0 | 0 | 699 | Alta | no |
| Chai latte en polvo | chai latte (5.000) | ~100 | 8 | 50 | 743 | Alta | **sí** |
| Comida liofilizada | comida liofilizada (500) | 500 | 25 | 25 | 210 | Alta | no |
| Fruta liofilizada | fruta liofilizada (500) | 500 | 25 | 25 | 2.924 (outlier) | Alta | no |
| Ginger beer | ginger beer (5.000) | 5.000 | 50 | 50 | 565 | Alta | no |
| Agua de coco | agua de coco (5.000) | 5.000 | 50 | 50 | 529 | Alta | no |
| Compra al por mayor | bebidas por mayor (5.000) | ~5.050 | 50 | 50 | 343 | Alta | no |

Notas de lectura:
- La competencia es "Alta" en casi todo (96 de 114 términos). No discrimina. Solo cold brew, tofu y chips de garbanzo (sin CPC) quedan en "Media", y kimchi en "Baja".
- Un CPC alto máximo sobre 1.000 CLP (granola, jugos, agua con gas, kimchi, proteica) indica valor comercial pero también pujas caras. El de fruta liofilizada (2.924) es un outlier de pocos anunciantes.
- Estacionalidad, mes peak y variación interanual quedan **nulos**: las 24 columnas mensuales están vacías en los 3 archivos de volúmenes (1.672 filas). `estacionalidad_mensual` está vacía por diseño.

## 4. Tendencias y ciclos

- **No hay tendencia utilizable desde Ads.** Sin gasto no hay mensuales, y los cambios son saltos de bucket que contradicen a Trends en 6 de 9 casos comparables.
- **Electrolitos en sobre sube** (500 a 5.000 en el interanual, +900%); "sobre electrolitos" también (50 a 500). Es la única señal direccional con respaldo parcial. La bitácora cita +450% en Trends, pero el término no está en el resumen de Trends de 100 términos, así que no se confirma aquí.
- **La demanda específica de formato es pequeña.** Matcha RTD ≤50, chai en polvo ~100, proteica RTD ~650, frente a 5.000-50.000 del paraguas. El interés existe en la categoría, pero no con ese formato ni con ese nombre.
- **Ciclos:** no medibles. Hipótesis a validar con las series de Trends: pico de verano austral (dic-feb) en electrolitos, cold brew, té helado, agua de coco y ginger beer, y pico de invierno en chai y avena barista. Confianza baja.

## Recomendaciones
1. Para la matriz del 28-oct, usar `volumen_especifico_aprox` o el índice específico, no `nivel_termino_clave_mes`. Marcar granola y creatina como "no medido".
2. Segunda tanda en el Planner con los términos de atributo ("granola con legumbres", "creatina gomitas", "matcha listo para beber", "té helado sin azúcar", "chai en polvo", más "comprar/precio/dónde" para kimchi y tofu).
3. Corregir `actualizar_radar_google_ads.py`: calcular CPC y competencia solo con términos específicos y excluir términos de 50 búsquedas sin CPC.
4. Para tendencia y estacionalidad, usar Trends. Si el grupo quiere mensuales de Ads, activar una campaña mínima con gasto.
5. Actualizar la guía (12 meses, límites de la cuenta sin gasto) y registrar ubicación, idioma y red del export.
