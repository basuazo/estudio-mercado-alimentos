---
fecha: 2026-10-16 18:25
persona: boris
agente: Claude desktop
fase: Estudio de mercado · Fase 1
paso_del_plan: A1 Demanda (Google Ads, tarea adelantada de Mario)
estado: completado
---

# Google Ads Keyword Planner: volúmenes de los 114 términos e ideas por semilla

## Objetivo
Correr el Planificador de palabras clave con los 114 términos de `terminos-busqueda.csv` y las 5 semillas de la guía, y dejar los datos limpios y agrupados por candidata para la matriz del 28-oct. Boris lo hizo en lugar de Mario (autorizado el 16-oct).

## Qué se hizo
- Boris exportó 4 archivos del Planificador (UTF-16, tabulados). Qué es cada uno:
  - `2026-10-16_google-ads_keywords-planner-2.csv` — volúmenes de los 114 términos (Chile, últimos 12 meses oct-2025 a sep-2026).
  - `..._keyword-planner_ideas.csv` — ideas desde la semilla `electrolitos` (310 filas).
  - `..._keyword-planner_ideas2.csv` — ideas desde las semillas `bebida proteica`, `cold brew`, `matcha`, `chai latte` (1.248 filas).
  - `..._keywords-planner.csv` — es una previsión de campaña (Campaign1, Maximizar clics, nov-2026: 4.705 clics, 116.688 impresiones, 136.800 CLP, CPC 29 CLP). No lista términos; no sirve para el estudio.
- Script nuevo `scripts/procesar_google_ads_keyword_planner.py`: lee los CSV, agrupa por candidata (regex sobre el término) y cruza con Google Trends.
- Los 114 términos vinieron todos con dato; no faltó ninguno.

## Hallazgos
- **Los volúmenes son órdenes de magnitud, no cifras.** Sin gasto activo, Google devuelve solo 0 / 50 / 500 / 5.000 / 50.000 / 500.000. Sirven para comparar entre niveles (cada nivel es ~10 veces el anterior), no dentro de un mismo nivel. Distribución de los 114: 18 en 50, 21 en 500, 48 en 5.000, 26 en 50.000, 1 en 500.000 (creatina).
- **Los cambios de 3 meses e interanual no son confiables.** Solo aparecen 0 %, ±90 % y 900 %, que son saltos de nivel. Las columnas mensuales vienen vacías. Para dirección de la demanda, usar Google Trends.
- **Electrolitos:** "electrolitos" 50.000; "electrolitos en sobre" 5.000 (interanual +900 %, coherente con +450 % en consultas de Trends); "bebida isotónica" 5.000 pero cayendo en Trends (-53 %); "sobres de electrolitos" 500; "suero oral" 500; "bebida hidratante en polvo" 50. De 271 ideas nuevas, solo 19 pasan de 500 y casi todas son informativas ("qué son", "en la sangre", "caseros"): hay mucho interés por el tema y poca búsqueda de compra por sobre.
- **Café o batido proteico listo para beber:** se busca como "batido de proteína" (5.000) y "leche proteica" (5.000), no como "bebida proteica" (50), "proteína lista para beber" (50) ni "bebida proteica café" (50). "Café proteico" 500 (CPC alto más bajo del grupo: 175 CLP). Las 17 ideas nuevas son todas de 50. Implicancia: el nombre de la categoría para el consumidor es "batido" o "leche", no "bebida proteica".
- **Cold brew:** "cold brew" 5.000 con competencia media y el CPC más bajo de todo el set (17–537 CLP); "café cold brew" 500; "cold brew concentrado" 50. Las demás ideas (72) son de 50 y apuntan a Starbucks, prensa francesa y preparación casera. Trends: +183 % año 2 vs año 1.
- **Matcha:** "matcha" 50.000 (Trends +29 %, +49 % último trimestre), "matcha latte" 5.000, 9 ideas de 5.000 o más. Sin ninguna idea de matcha listo para beber, y la demanda es de té/polvo (coincide con Mercado Libre). Matcha como bebida lista sigue sin respaldo en búsquedas.
- **Avena barista:** "leche de avena" 5.000, "leche de avena barista" 500; competencia alta, CPC alto hasta 943 CLP. Pocas ideas nuevas (2).
- **Radar de 1 fuente:** chai latte 5.000 (438 ideas, 7 de 5.000 o más), ginger beer 5.000, agua de coco 5.000, "bebidas por mayor" 5.000 (marcado +900 % en 3 meses, puede ser solo salto de nivel), comida liofilizada 500, fruta liofilizada 500.
- **Competencia por palabra:** casi todo es "Alta". Solo cold brew tiene "Media" entre los términos de candidatas.

## Archivos creados o modificados
- `scripts/procesar_google_ads_keyword_planner.py` — procesa y agrupa (uso: `python scripts/procesar_google_ads_keyword_planner.py 2026-10-16`).
- `datos/limpios/2026-10-16_google-ads_volumenes_114.csv` — los 114 términos con candidata, volumen, competencia, CPC y señales de Trends.
- `datos/limpios/2026-10-16_google-ads_ideas_por_candidata.csv` — 1.558 ideas únicas, agrupadas por candidata (88 de los 114 términos y la mayoría de las ideas quedan sin candidata, por diseño).
- `datos/limpios/2026-10-16_google-ads_resumen_candidatas.csv` — una fila por candidata.
- `datos/referencia/2026-10-16_terminos-busqueda_para-pegar.txt` — los 114 términos, uno por línea.

## Decisiones propuestas (para acordar en grupo)
- Usar Keyword Planner solo para ordenar por nivel de magnitud y para el nombre con que la gente busca la categoría; la dirección de la demanda sale de Google Trends.
- En la matriz del 28-oct, puntuar la demanda por nivel (50 / 500 / 5.000 / 50.000) y no por cifra.
- Probar "batido proteico" o "leche proteica" como nombre de la candidata proteica en las siguientes consultas.

## Pendientes y siguiente paso
- [ ] Cruzar estos volúmenes con el radar y actualizar la columna de señal de búsquedas (siguiente sesión con Claude).
- [ ] Mario: la tarea de Google Ads queda hecha; sigue pendiente validar los términos de uso de Mercado Libre (21-oct).
- [ ] Opcional: repetir con semillas "batido de proteína", "leche proteica" y "sobres hidratantes" para ver las ideas reales de compra.

## Contexto para la próxima sesión
La carpeta `datos/crudos/` tiene 4 exportaciones de Google Ads con nombres poco claros (ver arriba). Los volúmenes vienen redondeados por nivel porque la cuenta no tiene campañas ni gasto. El archivo de previsión de campaña (`keywords-planner.csv`) no es útil y puede ignorarse.
