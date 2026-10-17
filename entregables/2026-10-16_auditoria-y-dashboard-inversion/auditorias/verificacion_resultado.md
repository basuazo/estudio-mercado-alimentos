# Verificación independiente del tablero "Radar de inversión en alimentos"

Revisor: Claude (revisor escéptico, solo lectura) · 16-oct-2026
Insumos: `/home/claude/analisis/dash/*.json`, `dash/index.html`, `build_dash.py`, auditorías por fuente y el repositorio `company-builder` (datos crudos y limpios, recalculados con pandas en el equipo del usuario, sin modificar nada).

## Veredicto global

**Las cifras son confiables; algunas reglas y frases no.** Recalculé 52 cifras desde los archivos crudos o limpios del repositorio. Ninguna discrepa de forma material: las únicas diferencias son de redondeo o de una etiqueta. Los KPI de `index.html` salen correctos con la lógica declarada y todos los `data-field` de las tablas existen en su JSON. Los problemas están en otra parte:

1. La regla de "señal de demanda" les da "Media" a productos cuyo formato casi no se busca (matcha RTD, agua con gas saborizada, té helado).
2. Dos textos del Resumen exageran: la alerta de "demanda fuerte" y el KPI de cobertura del 24 %.
3. Hay detalles de normalización: severidades compuestas, la deriva incluye un término "ruido" y una etiqueta dice "$/kg".

Recomiendo corregir los puntos de severidad media antes de la reunión del 28-oct. Ninguno invalida el tablero.

## 1. Tabla de verificaciones

Método Trends: promedio de las 52 semanas más recientes contra las 52 previas, y las últimas 13 semanas contra las mismas 13 del año anterior. En ambos casos se excluye la semana parcial del 11-oct-2026. Archivo: `datos/crudos/2026-10-13_google-trends_cl_2anios_individual_100.csv`. Con la semana parcial incluida, las cifras no cuadran; sin ella, cuadran exacto.

| # | Cifra | Valor dashboard | Recalculado | OK/NO |
|---|---|---|---|---|
| 1 | Trends "yogurt griego" 12 m / trim. interanual | +69,4 % / +61,4 % | +69,4 / +61,4 | OK |
| 2 | Trends "electrolitos" | +12,8 / +6,5 | +12,8 / +6,5 | OK |
| 3 | Trends "matcha" | +28,7 / +11,1 | +28,7 / +11,1 | OK |
| 4 | Trends "whey protein" | +19,2 / +5,2 | +19,2 / +5,2 | OK |
| 5 | Trends "tofu" | +24,2 / +49,7 | +24,2 / +49,7 | OK |
| 6 | Trends "agua con gas" | +46,7 / +36,6 | +46,7 / +36,6 | OK |
| 7 | Trends "pan de masa madre" | +41,4 / +19,1 | +41,4 / +19,1 | OK |
| 8 | Trends "kimchi" | +32,3 / +68,2 | +32,3 / +68,2 | OK |
| 9 | Trends "leche de avena" | +42,5 / +42,1 | +42,5 / +42,1 | OK |
| 10 | Trends "proteina" | +1,7 / −0,4 | +1,7 / −0,4 | OK |
| 11 | Trends "creatina" | +14,7 / −0,8 | +14,7 / −0,8 | OK |
| 12 | Trends "cold brew" | +184,1 / +512,6 | +184,1 / +512,6 | OK |
| 13 | Trends "leche sin lactosa" | +22,5 / +15,7 | +22,5 / +15,7 | OK |
| 14 | Trends "agua de coco" | +17,4 / +24,7 | +17,4 / +24,7 | OK |
| 15 | Trends "granola" | +39,3 / +51,6 | +39,3 / +51,6 | OK |
| 16 | % semanas en cero "leche de avena" | 1,0 | 0,9 (sobre 106 semanas; 1,0 sobre 105) | OK (denominador) |
| 17 | Serie mensual electrolitos oct-24 / sep-26 | 59 / 82 | 59,2 / 81,5 | OK |
| 18 | Estacionalidad electrolitos, enero | 72,4 | 71,0 crudo; 72,4 sin tendencia lineal | OK, pero la etiqueta no dice "sin tendencia" (ver E8) |
| 19 | Ads "electrolitos" (búsquedas/mes) | 50.000 | 50.000 | OK |
| 20 | Ads "electrolitos en sobre" | 5.000 | 5.000 | OK |
| 21 | Ads "cafe proteico" | 500 | 500 | OK |
| 22 | Ads "matcha" / "matcha latte" | 50.000 / 5.000 | 50.000 / 5.000 | OK |
| 23 | Ads "granola" | 50.000 | 50.000 | OK |
| 24 | Ads "kimchi" | 50.000 | 50.000 | OK |
| 25 | Ads "te chai latte" / "chai lata" | 5.000 / 5.000 | 5.000 / 5.000 | OK |
| 26 | Ads "bebida hidratante en polvo" | 50 | 50 | OK |
| 27 | Ads "cold brew" / "cold brew concentrado" | 5.000 / 50 | 5.000 / 50 | OK |
| 28 | Ads "yogurt proteico" / "leche de avena barista" | 500 / 500 | 500 / 500 | OK |
| 29 | Índice Ads café proteico (650/mes) / chai (100/mes) | 28 / 8 | 27,8 / 7,5 | OK |
| 30 | ML mediana script, 7 términos (1.739; 952; 49.966; 39.780; 74.322; 35.560; 128.492) | idénticos | `mercadolibre_cl_resumen.csv` | OK (7/7) |
| 31 | ML cold brew RTD, mediana auditoría | 22.013 CLP/L (p25 19.502, p75 23.392, n=10) | 22.013 / 19.502 / 23.392, n=10 (rehecho a mano desde los títulos) | OK |
| 32 | ML cold brew, share top-3 / n.º de marcas | 45,2 % / 14 | 14/31 = 45,2 %; unas 13–14 marcas en los títulos | OK |
| 33 | ML electrolitos: Extra Life / Chispa (publicaciones) | 16 / 7 | 16 / 7 | OK |
| 34 | ML electrolitos: Amazing Care | 15 | 19 en bruto; 15 después de los filtros del auditor | No replicable sin la lista de exclusión (plausible) |
| 35 | ML chai: Dolce Gusto / Arkadia / Andes | 9 / 9 / 5 | 9 / 9 / 5 | OK |
| 36 | SII 107901 (té, café): 19–24 / 22–24 | +68,8 / +25,6 | +68,8 / +25,6 | OK |
| 37 | SII 107500 (platos preparados) | +264,8 / +8,8 | +264,8 / +8,8 | OK |
| 38 | SII 110402 (aguas) | +115,7 / −0,3 | +115,7 / −0,3 | OK |
| 39 | SII 105000 (lácteos) | +3,8 / −2,3; 314.678 UF/empresa | idem | OK |
| 40 | SII 472101 | +18,6 / −2,3 | idem | OK |
| 41 | SII 110401 | +34,2 / +1,4 | idem | OK |
| 42 | SII 107100 (panadería) | +30,2 / +0,2 | idem | OK |
| 43 | SII % Ñuble 2024 (107901 / 471100 / 107100) | 0,8 / 10,1 / 2,7 | 0,8 / 10,1 / 2,7 | OK |
| 44 | Comtrade 210111: USD 2025 / var. 21–25 / USD/kg | 92,45 M / +92 % / 22,25 | 92.452.619 / +92 / 22,25 | OK |
| 45 | Comtrade 220210 | 98,1 M / +813 % / 0,74 | idem | OK (reclasificación, ver riesgos) |
| 46 | Comtrade 210690 | 254,5 M / 0 % / 7,05 | idem | OK |
| 47 | Comtrade 350220: USD 2025 / +602 % / CAGR 22–25 | 7,05 M / +602 / +91,9 | idem | OK |
| 48 | Comtrade 200899: USD/kg 2025 / var. kg | 2,82 / +44 | 2,815 / +43,9 | OK |
| 49 | Comtrade 210410: USD/kg 2025 | 4,71 | 4,71 | OK |
| 50 | Radar n_fuentes (10 primeras oportunidades) | 3,3,3,3,2,2,2,2,2,2 | `radar-oportunidades_boris.csv` idem | OK |
| 51 | Deriva común (pct_ceros ≤ 5) | +8,7 %, n=51 | mediana 8,7, n=51 | OK (ver E5) |
| 52 | KPI resumen | 23 oport.; 3 estrictas; 4 radar; 3 fuertes; 18/68 errores altos; 24 % | 23; 3; 4; 3; 18/68; 24,0 % | OK en cálculo (ver E4 y E13 sobre lectura) |

Las 3 oportunidades con 3+ familias estrictas son Café proteico, Granola (4) y Chai. Las 3 con señal fuerte son Leche sin lactosa, Pan de masa madre y Tofu.

**Coincidencia de campos:** los 18 `<table>` tienen todos sus `data-field` en el JSON correspondiente, y ninguna columna queda completamente vacía. También coinciden los campos que usan los gráficos (`indice`, `indice_promedio`, `n_publicaciones`, `usd_cif`, `kg`, `usd_kg`, `var_2019_2024_pct`, etc.).

**Escalas y formato revisados sin errores:**
- Conversión del nivel Ads a índice: `(log10(n) − log10(50)) × 25` da 50→0, 5.000→50 y 500.000→100. Coincide con la auditoría de Ads.
- Escala symlog del mapa y del SII.
- Formato con coma decimal (`d3.formatLocale`).
- `pct0` aplicado a `share_top3`, que viene en porcentaje y no en fracción.
- Orden por `orden_veredicto`.

## 2. Errores encontrados

| Id | Severidad | Problema | Corrección exacta |
|---|---|---|---|
| E1 | **Media** | `senal_demanda` cuenta como "sobre la deriva" las series *proxy*. Por eso Matcha RTD y Agua con gas saborizada quedan en "Media" aunque su índice específico es 0 (≈50 búsquedas/mes) y la propia lectura dice "el formato no registra búsquedas". Café proteico pasa el umbral de 10 pp por 0,5 pp gracias al proxy "whey protein". | `build_dash.py`, función `senal_demanda`: después de `sobre = ...`, agregar `prox = 'proxy' in cal`. Reemplazar `if sobre or nivel: return 'Media'` por `if nivel or (sobre and not prox): return 'Media'` y `if sobre and prox: return 'Media (categoría)'`. En `index.html`, agregar `'Media (categoría)': 1.5` al `sortv` de `tb-veredictos` y explicar la etiqueta en la definición "Señal de demanda". |
| E2 | **Media** | Té helado queda en "Media" por un índice Ads de 50 que sale del término amplio "te helado" (`volumen_especifico` = nivel del término clave, marcado como demasiado amplio). Contradice la definición de índice específico y su lectura "Sin señal". "Productos sin sellos" queda en "Sin dato" aunque tiene dato en Ads (≈50/mes); la definición dice "Débil: hay dato". | `build_dash.py`: `nivel = idx is not None and idx >= 50 and not (ad.get('termino_demasiado_amplio') and ad.get('volumen_especifico_aprox') == ad.get('nivel_termino_clave'))`. En la línea de "Débil", cambiar `(idx is not None and idx > 0)` por `idx is not None`. |
| E3 | **Media** | La alerta "La demanda fuerte está donde el modelo no calza" incluye a Yogur griego y Avena barista, que el mismo tablero clasifica como "Media", y dice que "crecen de verdad" cuando lo que crece es la búsqueda. Contradice el KPI de señal fuerte (3). | `index.html` línea 108: título "El mayor crecimiento de búsqueda está donde el modelo no calza". Texto: "Yogur griego, leche de avena, pan de masa madre, tofu y leche sin lactosa crecen en búsquedas entre 14 y 61 pp sobre la deriva, pero piden frío, producción láctea o compiten con grandes. Solo masa madre, tofu y leche sin lactosa tienen además volumen específico (señal fuerte)." |
| E4 | **Media** | El KPI "Matriz de decisión con evidencia: 24 %" valora "Juicio" (opinión del auditor, sin dato) en 0,25. Contando solo datos (Con datos = 1, Parcial = 0,5), la cobertura es **14 %**. | `build_dash.py` línea 119: `'Juicio': 0`. Otra opción es mantener el valor y cambiar la etiqueta en `index.html` línea 100 a "Matriz cubierta (datos + juicio)" con la nota "Solo con datos: 14 %". |
| E5 | Baja | La deriva incluye "kefir", clasificado como ruido (pico puntual, 0 % de ceros). El KPI dice "51 términos con señal", pero 54 series no son ruido y 4 de ellas tienen más de 5 % de ceros. Sin kefir, la mediana es 8,45 (n=50) y ninguna oportunidad cambia de clase. Además `DERIVA = 8.7` está fijo en `build_dash.py` y repite el cálculo de `index.html`: se pueden desincronizar. En el gráfico de exceso, kefir aparece como barra destacada de +32,5 pp. | `index.html` líneas 544 y 765: agregar `&& r.clasificacion !== 'ruido'` al filtro. `build_dash.py` línea 13: calcular `DERIVA` desde `t['tablas']['terminos']` con el mismo filtro, en vez de dejarlo fijo. |
| E6 | Baja | Hay severidades "media-alta" (B3-04) y "baja-media" (B3-07). No tienen estilo de pill, el filtro "Media" o "Alta" no las muestra, quedan al final del orden y el KPI de errores altos no cuenta la "media-alta". Además, el id queda "B3 -04", con un espacio. | `build_dash.py` líneas 138–140: guardar `severidad_original = e['severidad']` y normalizar con `{'media-alta': 'alta', 'baja-media': 'media'}`. Para el id, usar `nombre.split()[0][:3].upper()`. |
| E7 | Baja | Hay valores de confianza en hallazgos como "baja (30 fichas)", "alta (como limitacion)" y "media (partidas amplias)". Rompen el orden (`ord[...]` queda indefinido) y generan clases CSS inválidas. | `build_dash.py` línea 145: `'confianza': e.get('confianza','').split(' ')[0]` y `'confianza_detalle': e.get('confianza','')`. |
| E8 | Baja | El heatmap de estacionalidad usa índices sin tendencia lineal (`trends_meta/build.py` línea 163), pero se rotulan "Índice promedio" y "mes típico". | `index.html` línea 183: agregar "(serie sin tendencia lineal)". Línea 843: "Índice sin tendencia: ". |
| E9 | Baja | La etiqueta de las barras de importaciones dice "$/kg"; en Chile, "$" se lee como CLP. | `index.html` línea 997: `' USD/kg'`. |
| E10 | Baja | En `ml_precios`, la fila "comida liofilizada" muestra una "mediana auditoría" de 128.492 CLP/kg que corresponde solo a fruta liofilizada (la nota lo aclara, la columna no). La lectura de Fruta liofilizada dice "tras corregir packs", pero la mediana no cambió (script = auditoría = 128.492); lo que se corrigió fue el rango. | `build_dash.py`: renombrar el término a "comida liofilizada (precio: solo fruta)". En CORTO, cambiar la lectura de Fruta liofilizada a "Precios altos por kg (mediana 128.492; rango corregido hasta 290.680, no 950.000); demanda de nicho." |
| E11 | Baja | La columna "Empresas SII 22–24" parece específica de cada oportunidad, pero usa códigos CIIU amplios y compartidos: 107901 (+25,6 %) para cold brew, matcha y chai; 105000 para leche y yogur. | `index.html` línea 143: agregar a la nota "Empresas SII = actividad económica amplia, compartida entre oportunidades; no mide el nicho." |
| E12 | Baja | `deriva_txt` antepone "+" siempre: con una deriva negativa mostraría "+-3". | `index.html` línea 546: `(med > 0 ? '+' : '') + ...`. |
| E13 | Baja (lectura) | El titular "3 cumplen la regla… (el radar decía 4)" sugiere que las 3 salen de las 4 del radar. En realidad son Café proteico, Granola (lectura "Descartar") y Chai ("Radar"); solo Café estaba entre las 4. Además, "estricto" cuenta familias débiles o sin verificar (Google débil en Café, Macro débil en Chai). Sin ellas, solo Granola llega a 3. | `index.html` línea 80: agregar "(café proteico, granola y chai; solo café estaba en la lista corta, y granola tiene lectura descartar)". En la definición "Familia de fuentes", agregar "Se cuentan también señales marcadas débiles o sin verificar." |

**Lecturas preliminares (diccionario CORTO) contra las auditorías.** Ninguna contradice la evidencia en lo central. Confirmé contra los datos estos puntos:
- Electrolitos: hueco de 1.300–2.000 CLP/porción y 26 marcas (auditoría ML §6.3).
- Café: términos de formato con 90–99 % de semanas en cero.
- Avena: +42 %.
- Cold brew: 22.000 contra ~10.000 CLP/L de Briu.
- Agua con gas: +47 %, peak en enero.
- Snack: 0 de 30 en ML.
- Kimchi +32 %, Tofu +24 %, Agua de coco +17 %.
- Chai: 13 marcas, ~100/mes.

Hay que ajustar dos cosas: la de Fruta liofilizada (E10) y la de Avena barista. Para Avena, la auditoría de método dice "0 familias para el canal foodservice", pero la tabla muestra 2. Conviene que la lectura lo diga explícitamente, porque el KPI de familias la favorece.

**Avisos del Resumen.**
- Aviso 1 (lista corta) y aviso 2 (sodio): respaldados textualmente por la auditoría de método §1–3 y §3.3. El 2 está bien matizado: "puede llevar".
- Aviso 3: exagera (E3).
- Aviso 4: correcto, aunque "Corregido en este tablero" es amplio. Cold brew (+184 %, 11 % de ceros) sigue en el mapa en +175 pp y solo la lectura advierte la baja confianza. Sugiero un marcador distinto (contorno sin relleno) para las series con `calidad` "débil" en `drawMapa`.

## 3. Riesgos de interpretación que el tablero no advierte

1. **Anclaje de la lectura preliminar.** El tablero muestra pills de "Investigar" o "Descartar" antes de que el grupo puntúe, pero la propia metodología propone puntuar a ciegas. Conviene ocultar la columna "Lectura" por defecto, o separarla en otra pestaña, hasta después del puntaje del 28-oct.
2. **Clasificación sensible a la elección de términos.**
   - Yogur griego queda en "Media" porque su término específico es "yogurt proteico" (500/mes) y no "yogurt griego" (50.000/mes).
   - Tofu queda "Fuerte" gracias a "proteína vegetal".
   - El umbral de índice 50 cae justo en el borde de un rango ×10 de Google Ads.
   - Pequeñas decisiones del analista cambian la clase.
3. **Ruido de muestreo de Trends.** Hay una sola descarga y el umbral de +10 pp no se contrastó con la variación entre descargas (la limitación existe en la pestaña Auditoría, pero no junto al umbral). Café proteico pasa por 0,5 pp.
4. **La deriva no es "el mercado".** Es la mediana de una canasta de términos saludables elegida por el analista: "sobre la deriva" significa "más que otros términos de nicho", no "más que el consumo".
5. **Importaciones mal emparejadas e infladas por bases chicas.**
   - Emparejamientos dudosos: 210111 (sobre todo café instantáneo) para cold brew; 040299 (leche condensada, partida de control) para leche sin lactosa; 2202.99 (−77 %, probable reclasificación) para té helado, ginger beer y agua de coco.
   - Bases chicas: 350220 tiene +602 % y CAGR de +92 % sobre 1 M USD.
   - 220210 (+813 %) aparece en la tabla sin marca de reclasificación. La advertencia general existe, pero no está en la fila.
6. **Publicaciones ≠ ventas.** El share top-3 y el n.º de marcas miden visibilidad en una captura de un día ordenada por relevancia, que puede incluir avisos pagados (Briu en posiciones 1–4).
7. **Ninguna métrica mide tamaño de mercado, margen ni compra.** "Señal fuerte" no significa atractivo para invertir. El tablero lo dice en prosa, pero el KPI y el mapa invitan a leerlo como ranking.

## 4. Archivos revisados

- `/home/claude/analisis/dash/index.html` (líneas citadas arriba)
- `/home/claude/analisis/build_dash.py` (líneas 13, 53–62, 119, 138–145)
- `/home/claude/analisis/trends_meta/build.py` (línea 163, sin tendencia)
- Repositorio: `datos/crudos/2026-10-13_google-trends_cl_2anios_individual_100.csv`, `datos/crudos/2026-10-16_google-ads_*` (UTF-16), `datos/limpios/2026-10-16_mercadolibre_cl_captura.csv` y `_resumen.csv`, `datos/limpios/2026-10-16_sii_alimentos_nacional.csv` y `_region.csv`, `datos/crudos/2026-10-16_un-comtrade_importaciones-chile_hs6.csv`, `datos/limpios/2026-10-16_radar-oportunidades_boris.csv`.

No se modificó el repositorio ni el tablero. Los temporales quedaron en `$HOME/tmp_audit/` del equipo del usuario.
