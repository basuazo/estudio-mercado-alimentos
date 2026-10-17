# Auditoría de datos: Mercado Libre (API de tendencias y catálogo + captura de publicaciones)

Auditor: Claude (solo lectura sobre el repositorio `company-builder`). Fecha de la auditoría: 2026-10-16.
Alcance: archivos de `datos/crudos` y `datos/limpios` del 2026-10-16, los 3 scripts, las bitácoras 1615, 1653 y 1752, la guía 03, la pauta de captura, los términos de uso y las columnas `oportunidad` y `senal_mercadolibre` del radar. No se accedió a mercadolibre.cl ni se amplió ninguna extracción.

## Veredicto corto

| Fuente | Confiabilidad | Utilidad |
|---|---|---|
| API tendencias (569 palabras, 14 categorías) | B | Buena para ver qué marcas y términos buscan (sin volumen) |
| API catálogo (360 fichas, 12 búsquedas) | C | Media: es una muestra de 30 fichas por búsqueda y no coincide con lo que se vende en los avisos |
| Captura de publicaciones (434 filas, 7 términos) | C | Media-alta para rangos de precio por unidad, una vez corregidos los packs. No sirve para saturación ni ventas |
| **Conjunto Mercado Libre** | **C** | **B- para hipótesis de hueco de oferta; no apto para cifras citables sin corregir** |

Lo más grave, en orden:
1. **Packs mal normalizados** inflan precios hasta 6 veces: cold brew importado "19.000–140.000 CLP/L" en el radar es en realidad ~18.800–29.200 CLP/L; fruta liofilizada "80.000–950.000 CLP/kg" es ~38.000–291.000 CLP/kg.
2. **Un archivo crudo está contaminado**: `bebida-hidratante-en-polvo.csv` trae pegadas las 35 filas del cold brew (98 filas, solo 63 son suyas).
3. **Las columnas que responden la pauta están vacías** (marca, vendedor oficial, vendidos, reputación, formato). El resumen muestra ceros engañosos (0 marcas, 0 tiendas oficiales, 0 publicaciones con +100 vendidos).
4. **Catálogo y captura son universos casi disjuntos**: las marcas "pocas" del catálogo no son las que aparecen en las publicaciones (café proteico: 4 en catálogo + 3 en captura, sin solapamiento = al menos 7; liofilizada y cold brew igual). El argumento "poca oferta" es más débil de lo que dice el radar.
5. **Riesgo de términos de uso (secc. 7.6)** por la captura con script en consola, y la pauta dice "sin scripts" (inconsistencia documental).

## 1. Inventario

| Archivo | Filas | Columnas | Fecha | Método | Qué cubre |
|---|---|---|---|---|---|
| `crudos/..._mercadolibre-api_tendencias.csv` | 569 | 7 | 2026-10-16 | API oficial, token de aplicación (script `mercadolibre_api.ps1`) | Top 50 semanal de palabras por categoría (14 categorías; Aguas 30, Energizantes 32, Jugos 39, Isotónicas 17, **Leche solo 1**) |
| `crudos/..._mercadolibre-api_catalogo.csv` | 360 | 19 | 2026-10-16 | API oficial `/products/search`, 3 páginas de 10 | 12 búsquedas x 30 fichas de catálogo, con marca, formato y GTIN |
| `limpios/..._catalogo_limpio.csv` | 360 | 23 | 2026-10-16 | `limpiar_catalogo_mercadolibre.py` | Clasifica 170 objetivo / 109 adyacente / 81 ruido |
| `limpios/..._catalogo_resumen.csv` | 12 | 13 | 2026-10-16 | idem | Una fila por búsqueda |
| `crudos/..._mercadolibre_cl_<término>.csv` (7) | 35 a 98 c/u; 434 en total | 15 | 2026-10-16 | Captura de Boris con script en la consola del navegador (confirmado en bitácora 1752) | Primeras 35–68 posiciones por término, orden "Más relevantes". Trae título, precio, envío, URL. No trae marca, formato, vendidos, reputación ni tienda oficial |
| `limpios/..._cl_captura.csv` | 434 | 23 | 2026-10-16 | `resumir_captura_mercadolibre.py` | Agrega precio unitario, formato inferido y marca de relevancia |
| `limpios/..._cl_resumen.csv` | 7 | 16 | 2026-10-16 | idem | Una fila por término |

Cobertura por término de la captura: electrolitos sobres (58), bebida hidratante en polvo (98, de los cuales 35 son cold brew), bebida proteica café (60), proteína lista para beber (68), cold brew (35), chai latte (64), comida liofilizada (51). El radar no tiene captura para avena barista, matcha, jugo prensado, snack de lentejas ni las demás: esas filas solo tienen señal de catálogo y tendencias.

Todo es **una sola fecha** (foto del 16-oct, sin serie). Las tendencias son semanales y no traen volumen.

## 2. Auditoría de scripts

### `scripts/limpiar_catalogo_mercadolibre.py` (catálogo)
- **Clasificación por dominio**: lo que no cae en los dominios esperados queda como `ruido`. Efecto: *Liquid I.V.* (marca premium de electrolitos en sobre) quedó como ruido porque su dominio es `HYDRATION_BLADDERS`; "electrolitos sobres" sería 30 de 30 objetivo, no 29.
- **"Bebida hidratante en polvo": 30/30 objetivo**, pero 16 son líquidos listos (Powerade, Prime botella, Recupper, Flashlyte). Los polvos reales son 12 (B Life 5, Industrade 2, Hidro 2, Prime 1, Extra Life 1, Yuyo 1). El resumen dice "dominada por Powerade y Prime", que es verdad para líquidos, no para polvo.
- **"Proteína lista para beber": 21 objetivo**, pero 4 son "Proteína aislada: ¡lista!" de Pro Corps, que están en polvo (el script solo exige `prote|whey|shake`). Quedan 17 líquidos.
- **`formato`**: la regla de sólidos incluye `oz`, y los productos en onzas quedan como `polvo_o_solido` (p. ej. *Arizona Cold Brew Concentrate 28oz*, que además se clasifica como "té en frío, no café"). Además aparece 3 veces con distintos `product_id` (uno con la marca mal escrita "rizona").
- **País por GTIN**: el prefijo indica dónde se registró el código, no el origen. NotCo (marca chilena) sale con prefijo Brasil. Faltan prefijos (641, 852, 866 salen como "otro"). El radar dice "todas importadas" para café proteico, pero 3 de las 4 fichas objetivo no tienen GTIN: la afirmación descansa en 1 dato. "GTIN mayoritariamente de México" en electrolitos sobres es 13 de 29 fichas (45 %), o 13 de 17 de las que traen GTIN.
- `total_informado_api` = 10.000 en "electrolitos sobres" es un tope de la API, no un conteo real. No usar como tamaño de mercado.
- Un `product_id` aparece en dos búsquedas (electrolitos y electrolitos sobres): suma doble si se agrega entre búsquedas.
- Las reglas son razonables como primer filtro, pero se clasifica solo por título; con 30 fichas por búsqueda cualquier regla mueve el resultado un 10–15 %.

### `scripts/resumir_captura_mercadolibre.py` (captura)
- **`precio_unitario`**: solo multiplica cuando el formato viene como `N x tamaño`. Falla con "Paquete De 6", "12 Unid", "(20g X 5un)", "80 Gr (4 Bolsas)" y "Pack 5 Kg ... Bolsas de 1 Kg". Ejemplos verificados:
  - Wandering Bear 946 ml "Paquete De 6": script 129.856–140.353 CLP/L, real 21.643–23.392.
  - High Brew 12 latas de 296 ml: script 350.929, real 29.244.
  - Fruta liofilizada "20g X 5un": script 949.500 CLP/kg, real 189.900. "Tropical Mix 80 gr (4 bolsas)": 249.375 vs 62.344.
  - Pack 5 kg de chai: script 2.560 CLP/kg (el mínimo que cita el radar), real 12.798.
  - "Pack 6 Ostrovit 20 Tabs": 4.165 por "unidad", pero son 120 tabletas (~208 por tableta).
- **Gramos de porción leídos como peso del producto**: "Revitta Whey Protein Bar 16 barritas 16g" da 1.624.375 CLP/kg; "Suero proteico I Like 630 mL con 12g" da 207.500 CLP/kg; "QNT 25g|330ml x12" da 116.633 CLP/kg en vez de ~8.800 CLP/L.
- **`inferir_formato`**: reconoce `pack|caja` pero no "paquete"; no reconoce `unid` (solo `und`/`unidades`); no maneja `oz`, `lb` ni `onzas` (30 de 47 publicaciones relevantes de liofilizada quedan sin precio unitario, y muchas de las importadas de electrolitos con títulos truncados también: 14 de 38).
- **`relevante` por regex**: es demasiado laxo y a la vez deja fuera cosas. Falsos positivos: "proteína lista para beber" marca 29 relevantes pero la mayoría son polvos (whey, vegana, crepes proteicos, un libro "High Protein Food List"); chai incluye 11 cápsulas Dolce Gusto y 4 jarabes Monin; electrolitos incluye tabletas efervescentes. Falsos negativos: Gatorade polvo (trending #5 y #11 en Isotónicas) marcado no relevante; Akapro y Nude en "bebida proteica café" marcados no relevantes (correcto por sabor, pero no se anotó en ninguna parte).
- **Unidad predominante**: el resumen elige la unidad más frecuente y calcula la mediana sobre ella. En "proteína lista para beber" la mediana (39.780 CLP/kg) es de polvos; en "bebida proteica café" (49.966 CLP/kg) también. Ninguna sirve para el producto que se quiere estudiar (líquido listo).
- **Ceros engañosos en el resumen**: `marcas_distintas`=0, `tiendas_oficiales`=0, `publicaciones_100_o_mas_vendidos`=0, `marcas_principales` y `mas_vendidos` vacíos, `vendedores_distintos` 0–7, porque la captura no trae esos campos. Debieron salir vacíos, no cero.
- `vendidos_min` no se calcula nunca (la captura no trae el dato). El parseo toma el primer número y lo trata como piso del rango (correcto para "+100"), pero "+1.5mil" con punto decimal daría 15.000 (se borra el punto antes de convertir). Es código sin uso por ahora; probarlo antes de la próxima captura.
- El término se toma del nombre de archivo (bien), pero `termino_original` queda como "alimentos-bebidas" en cold brew y liofilizada (86 filas): etiqueta residual del script de consola; los títulos son coherentes con el término, pero no hay forma de verificar la búsqueda exacta.

### `scripts/mercadolibre_api.ps1`
Razonable: token de aplicación, pausa de 1,5 s, reintento ante 429 y renovación de token. Sin errores de lógica relevantes. Observaciones: guarda con sufijo de hora si el archivo existe (genera duplicados si se corre dos veces el mismo día), no registra cuántas llamadas fallaron en el CSV (solo en consola), y la categoría Leche devolvió 1 palabra sin dejar aviso. Es el único componente claramente dentro de la vía autorizada (API oficial).

## 3. Recalculo de las cifras del radar (desde `..._cl_captura.csv`)

Se excluyeron las 35 filas contaminadas, se deduplicó por URL, se corrigieron packs y se separó producto objetivo.

| Cifra del radar | Recalculada | ¿Cuadra? |
|---|---|---|
| Electrolitos masivo 450–1.000 CLP/porción (Amazing Care, Extra Life, Fuel, Go!, Purihydra, Irio, Suerox) | 45 publicaciones de esas 7 marcas: min 442, p25 687, mediana 916, p75 1.248, max 1.699. El 69 % cae entre 450 y 1.000. Fuera del rango: Suerox x4 (1.498), Extra Life 4–10 sobres (1.248–1.699), Go! 442 | **Parcialmente.** El núcleo es 450–1.000 para cajas de 12–30 sobres; en packs chicos sube a 1.200–1.700 |
| Premium 2.000–6.700 (LMNT, Zalt y otros) | 10 publicaciones con cantidad legible: 2.105–6.711, p25–p75 2.419–3.531 (LMNT 2.105–2.626; Zalt 6.711). Otras 8 no se pueden calcular (títulos truncados sin cantidad) | **Sí**, con la salvedad de que 8 no se miden |
| Chispa 1.333 CLP | x30 = 1.333; x10 = 1.999 | Sí (solo el x30) |
| NotShake ~6.400 CLP/L | 1.590 / 0,25 L = 6.360 | Sí |
| Akapro ~6.100 CLP/L | caja x12 de 330 ml: 6.088; unidad suelta: 7.545 | Sí (es el precio de la caja) |
| Briu 9.500–14.000 CLP/L | 9.497 (12x250 listo), 11.490 (1 L listo), 13.330 y 13.990 (concentrados) | Sí, pero mezcla listo para tomar y concentrado (no comparables por litro) |
| Importados 19.000–140.000 CLP/L | Listos con volumen conocido: 18.788–29.244 (mediana 22.013). El 140.000 viene del error de pack | **No.** El techo real es ~29.000 |
| Fruta liofilizada 80.000–950.000 CLP/kg | 18 publicaciones: 37.990–290.680, p25 84.828, mediana 128.492, p75 177.658. El 950.000 es error de pack; el 37.990 es una publicación atípica ("1 kg") | **No.** El rango útil es ~60.000–290.000 |
| Chai: mediana 35.600, rango 2.600–150.000 CLP/kg | Chai instantáneo en polvo (n=18): mediana 29.125, p25 17.058, p75 44.936, rango 9.890–117.980. La mediana del script (35.560) cae en un té chai a granel de hojas; el 2.560 es error de pack | **No** (la mediana sobreestima ~20 %, el mínimo es falso) |
| "66 % con envío gratis" en electrolitos sobres | 25 de 38 relevantes = 66 %. Pero: 58 filas totales, 55 %; posiciones 1–20, 26 %; premium importado, 100 %; marcas locales, 5 %; y el término "bebida hidratante en polvo" da **2 %** | **Cuadra solo para ese término y está arrastrado por los importados** (todos los de posición 37+ tienen envío gratis). No describe a la oferta masiva local |
| "Café proteico RTD: solo 3 con café" | En la captura: NotShake café caramelo, Akapro capuccino, Nude vainilla y café. En el catálogo: Emana, Optimum Nutrition, Mu, SlimFast | **Las dos listas no se cruzan: al menos 7 marcas** |
| Liofilizada "pocas comidas de montaña (Outdoor Daff)" | 17 publicaciones de comida: Gufo 8 (10.490–11.990 CLP), Wise Food 5, Daff 1, 3 sin marca | **No.** Hay una marca con 8 sabores, no en el catálogo |
| Isotónicas "9 de 17 palabras de hidratación" | No reproducible. Por conteo propio, 15 de 17 son términos o marcas de hidratación; 2 son "por mayor" | Subestima; ver más abajo |
| Jugos prensados "no aparece en tendencias" | "jugos bless" #9, "jugo bless" #31 y "bless" #29 en Jugos; el catálogo clasifica Jugos Bless como objetivo | **No** del todo: hay una marca de jugo prensado en tendencias |

## 4. Calidad: duplicados, patrocinados, outliers, sesgos

- **Contaminación**: 35 filas de cold brew (posiciones 1–35, `termino_original` = `alimentos-bebidas`) dentro del archivo de hidratante. Inflan `publicaciones_capturadas` a 98 (real 63) y generan 35 URLs duplicadas. Los estadísticos "relevantes" no se ven afectados porque la regex las descarta.
- **Duplicados**: 10 publicaciones aparecen en dos términos (Nude Shake, Amazing Care, Dymatize, Gohard, Yuno, Crealyte). Hay variantes casi iguales: Wandering Bear 7 fichas, Extra Life 16, Stella Blue 3, Lavazza 3. Mismo título con precios distintos (Extra Life 10 un: 9.690 vs 16.490; Amazing Care x30: 19.990 vs 16.069 vs 24.990) por distintos vendedores o momentos.
- **Patrocinados**: no hay columna que los marque. Hay señales indirectas de tarjetas omitidas: posiciones faltantes (electrolitos 5 y 25; hidratante 30, 31, 39, 50, 53; chai 13, 26, 38, 51) y 80 filas sin URL (18 %). La muestra no es contigua y puede haber excluido avisos promocionados, o incluirlos sin etiqueta.
- **Orden por relevancia**: sesgo fuerte. En electrolitos sobres las posiciones 1–20 son marcas locales masivas (mediana 754 CLP/porción) y las 21+ son importados (mediana 2.626). En proteína lista para beber, la relevancia cae de 65 % (1–20) a 33 % (21+). La pauta pedía 20 posiciones; se capturaron 35–68 (434 filas vs ~140 previstas) sin documentar por qué.
- **Cold brew**: Briu aparece solo en posiciones 1–4 (todos con envío gratis, sin vendidos); no se puede distinguir si es posicionamiento orgánico o publicidad. Que sea "local" no está verificado (no hay vendedor ni tienda oficial capturados).
- **Outliers de precio**: Abintra 12 sobres 149.990 (12.499 por sobre, 10 veces el premium típico), Wandering Bear 130.000+ por pack de 6, Lavazza 80 paquetes 130.000+, Prosource 99.990 sin formato. Se separaron en el análisis.
- **Vendidos como rango**: la columna está vacía, así que no hay saturación medible. Cuando se capture, "+100", "+500" son pisos de un rango: subestiman a los grandes, y empatan a un vendedor con +100 con otro de +900. Usar como ordinal, nunca como ventas ni suma.
- **Foto de un solo día**: sin serie ni estacionalidad (cold brew +183 % y sobres +450 % en Google Trends son de base baja; ML no confirma demanda).
- **Envío gratis**: en Mercado Libre depende del umbral de compra, del comprador (dirección, sesión iniciada) y de Full; no se registró el estado de sesión. El porcentaje sube de 7 % a 71 % entre avisos de menos de $20.000 y de más de $60.000, o sea, es en buena parte una función del precio.
- **Importado vs local**: no se puede inferir con rigor (no hay marca ni vendedor ni origen). Indicativo por marca conocida: en electrolitos, 7 marcas masivas locales/regionales (Amazing Care, Extra Life, Fuel, Go!, Purihydra, Irio, Suerox) concentran 45 de 74 publicaciones; las 8+ marcas de EE. UU. de posición 37+ son todas importadas con envío gratis (traducciones literales en el título).

## 5. Análisis agregado por oportunidad

Marcas por título (diccionario manual, no por columna), publicaciones deduplicadas, solo producto objetivo. `share_top3` es por publicaciones; no hay "vendidos" para ponderar.

| Oportunidad (radar) | n publ. | n marcas | Share top-3 | Precio por unidad: mediana (p25–p75) | % envío gratis | Ranking en tendencias |
|---|---|---|---|---|---|---|
| Sobres y tabletas de electrolitos | 74 | 26 | 51 % (Extra Life 16, Amazing Care 15, Chispa 7) | 997 CLP/porción (806–1.528); masivo 916, premium 2.659 | 28 % (locales 5 %, importados 100 %) | Isotónicas: suerox #2, amazing care #3, hidratantes en polvo #4, gatorade en polvo #5, electrolit #6, irio #13, electrolitos #14 |
| Café o batido proteico listo para beber 20-30 g | 16 RTD (de 128 filas) | 10 | 56 % (Nude 5, Akapro 3, 1 c/u del resto) | 9.962 CLP/L (6.952–11.160); mín 3.952 (suero), máx 17.618 | 38 % | Alimentos y Bebidas: protein full pro loncoleche #11, milo protein #18 |
| Cold brew local sin azúcar | 35 | 14 (+4 sin identificar) | 45 % (Wandering Bear 7, Briu 4, Bizzy/Chamberlain/Lavazza/Stella 3 c/u) | RTD con volumen conocido: 22.013 CLP/L (19.502–23.392); Briu 9.497–11.490 | 89 % | No aparece en ninguna categoría |
| Chai latte en polvo o concentrado | 64 | 13 (+13 sin identificar) | 45 % (Dolce Gusto 9, Arkadia 9, Andes Tea 5) | 29.125 CLP/kg instantáneo (17.058–44.936; n=18) | 5 % | Infusiones: marley chai latte #14, chai latte #18, te chai starbucks #21, te chai marley #23 |
| Comida liofilizada de montaña | 17 comidas (de 51) | 3 (+3 sin marca) | 82 % (Gufo 8, Wise Food 5, Daff 1) | 10.490 CLP por plato (10.490–11.990; n=11 individuales); Wise Food 26.991–63.992 por 4–12 porciones | 6 % | Alimentos y Bebidas #48 (outdoor), Deportes #32 (trekking) |
| Fruta liofilizada como snack | 18 con precio | no medible | no medible | 128.492 CLP/kg (84.828–177.658) | 22 % (toda la búsqueda) | Almacén: fruta liofilizada #18 |

Oportunidades sin captura de publicaciones, solo catálogo y tendencias (marcas del catálogo, top-3 por fichas objetivo): avena barista 10 objetivo, 8 marcas, 50 %; matcha 1 objetivo (Tazo) y 20 adyacentes de polvo o bolsitas; jugo prensado 3 de 30 (Bless, Naturall, Pressade); snack de lentejas 0 de 30 (regla: todas "adyacentes").

## 6. Señales de hueco de oferta (hipótesis, con la confianza que permiten los datos)

1. **Cold brew listo para tomar, local, a menor precio por litro. Señal media-alta.** Los listos con volumen conocido cuestan 18.800–29.200 CLP/L; Briu, el único local visible, está a 9.500–11.500. El hueco de precio existe frente a importados (la mitad). Pero la mejor oferta no está lejos, y hay 4 publicaciones de Briu en el top 4 (probablemente posicionadas). No hay señal de demanda en ML (no aparece en tendencias).
2. **Café proteico RTD. Señal media.** En la captura solo 3 RTD con café y en el catálogo otras 4: al menos 7 marcas (Nude, NotCo, Akapro, Emana, Optimum Nutrition, Mu, SlimFast). Los de menor precio por litro (Akapro y NotShake ~6.100–6.400 CLP/L) ya están en rango bajo. El hueco es sabor café sin azúcar con 20–30 g de proteína; falta el dato de proteína por unidad (no capturado) para medir CLP por gramo de proteína.
3. **Electrolitos: hueco "natural / local en caja de 30" en 1.300–2.000 CLP/porción. Señal media.** Entre masivo (450–1.000) y premium importado (2.100–6.700) hay una franja con Chispa (1.333) y pocas más. La oferta masiva está concentrada (top-3 = 51 %, Extra Life y Amazing Care con 31 publicaciones) y respaldada por tendencias (4 marcas entre las 17 palabras de Isotónicas). Los premium dependen de envío internacional.
4. **Comida liofilizada de montaña: hay un competidor local con 8 sabores (Gufo).** La señal "pocas marcas" del catálogo (Lio Nutri, Camps Foods, Lyovibes, de Brasil y EE. UU.) no es la misma oferta que las publicaciones de la captura. Hueco menos claro. Mercado de plato único a ~10.500 CLP.
5. **Chai latte en polvo: oferta fragmentada (13+ marcas) con rango amplio de precio por kilo (10.000–118.000).** No hay concentración alta. El hueco podría ser una opción premium local de 20–30.000 CLP/kg, pero la señal es débil y no está medida para "listo para beber".
6. **Snack de lentejas y matcha listo para beber:** el catálogo no muestra ofertas del formato, pero la regla del clasificador pone todo como "adyacente" y la muestra es de 30 fichas; no se puede distinguir hueco de falta de demanda sin Google Ads o supermercados.

## 7. Limitaciones y riesgos

- **Términos de uso, secc. 7.6 (riesgo abierto, no resuelto):** la captura se hizo con un script en consola. Aunque no recorre el sitio, es extracción automatizada, y los términos para desarrolladores prohíben "scraping or other technology". La pauta (`pauta-captura-mercadolibre.md`) y la guía 03 dicen "sin scripts ni extensiones", así que hay una inconsistencia entre lo que se dijo y lo que se hizo; está registrada en la bitácora 1752. Secc. 5.4: calcular y publicar "average prices" requiere autorización. Mario debe resolverlo antes de repetir o ampliar. Esta auditoría no recomienda automatizar más; mientras tanto, el uso debe ser interno y sin publicar promedios.
- Una fecha, sin serie ni estacionalidad.
- Sin marca, vendedor, vendidos ni reputación: no hay saturación, no hay ventas, no hay origen.
- Orden por relevancia con posibles avisos promocionados no marcados y tarjetas omitidas.
- Los precios por unidad requieren formato correcto; hoy entre 16 % y 64 % de las publicaciones relevantes no tiene unidad calculada según el término (liofilizada 64 %, electrolitos sobres 37 %, café proteico 36 %, proteína RTD 24 %, hidratante 23 %, chai 22 %, cold brew 16 %).
- Tendencias sin volumen; la categoría Leche trajo 1 palabra.
- Catálogo: 30 fichas por búsqueda; no equivale a la oferta en avisos.
- El estado "lista corta (propuesta)" de dos oportunidades usa Mercado Libre como "tercera fuente independiente"; esa fuente es la API (tendencias y catálogo) y se cuenta como una sola.

## 8. Correcciones recomendadas (para quien mantiene los scripts)

1. Rechazar o separar filas cuando `termino_original` ≠ término del archivo y reportar el conteo (el archivo de hidratante).
2. En `precio_unitario`: aceptar "paquete de N", "pack N", `NNx`, `x N un`, "(A g x N un)" y "N bolsas", y reconocer oz, lb y onzas. Ignorar gramos de porción o de proteína.
3. Calcular la mediana solo sobre el formato objetivo (RTD, polvo en sobre) y escribir la mediana por tipo de producto, no por unidad predominante.
4. Dejar vacío, no cero, lo que no se capturó.
5. Agregar a `relevante` exclusiones de formato (polvo, cápsula, jarabe, libro) por término, y un valor `adyacente`.
6. En el catálogo: separar `liquido` listo de `polvo` en "hidratante en polvo", corregir `oz`, tratar `HYDRATION_BLADDERS`, no usar GTIN como origen.
7. Documentar una captura con las columnas de la pauta (marca, vendedor, oficial, vendidos como rango y patrocinado) si Mario aprueba la forma de captura.
8. Corregir en el radar: rangos de cold brew importado y fruta liofilizada, mediana de chai (instantáneo), la frase "todas importadas" del café proteico, la lista de marcas de liofilizada y la mención de Bless.
