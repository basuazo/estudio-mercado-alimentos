---
fecha: 2026-10-21 22:36
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: A1 Demanda (ampliación asiática) · A4 Macro (Comtrade) · B Benchmark internacional (Australia)
estado: completado (primera pasada)
---

# Tendencias de comida asiática (100 términos) y Australia como predictor

## Objetivo
Corregir el sesgo occidental del estudio de tendencias del 12–13 de octubre midiendo 100 términos de comida asiática (Trends + Google Ads, mismo método) y probar si el mercado australiano anticipa al chileno.

## Qué se hizo
- Lista de 100 términos asiáticos en 10 categorías y archivo para pegar en el Planificador.
- Google Trends Chile para los 100 términos, con la misma ventana del estudio anterior (2024-10-06 a 2026-10-04): series individuales y volumen relativo con granola como ancla. La captura se hizo desde el Chrome de Boris; Trends limitó la frecuencia y tomó unos 40 minutos. Se verificó que lo transcrito coincide con lo capturado (suma de control por término).
- Indicador nuevo, **octubre–junio contra octubre–junio**: 10 términos tienen su máximo en la semana del 2-ago-2026, con consultas en inglés del tipo "near me" (por confirmar). Este indicador evita leer ese pico como tendencia. El script `procesar_google_trends.py` queda reutilizable.
- Google Ads (exportaciones de Boris del 21-oct): 100 términos a 12 meses y 1.844 ideas a 24 meses, clasificadas por intención y marca (`procesar_google_ads_ideas.py`). Matriz Trends × Ads con 5 cuadrantes.
- UN Comtrade: importaciones 2021–2025 de 10 partidas asiáticas (tapioca, fideos, algas, salsa de soya, sake, aceite de sésamo, té). El proxy bloquea la API desde el agente, así que se consultó desde el navegador.
- Australia contra Chile: 26 temas globales de comida (trimestral 2010–2026, temas de Trends independientes del idioma) y 15 temas asiáticos a 5 años. Se calcularon despegue, rezago y correlación del crecimiento (`analizar_australia_vs_chile.py`, resultado reproducible).

## Hallazgos
Fuentes: Google Trends CL/AU y Google Ads (captura 2026-10-21), UN Comtrade (consulta 2026-10-21) y prensa citada en el entregable.
- Lo japonés es la mitad de todas las búsquedas asiáticas (sushi 500.000 al mes, +10 %), pero ya está maduro. Lo que crece con volumen: dumplings +193 %, pho +174 %, kimbap +160 %, udon +152 %, buldak +112 %, onigiri +51 %, miso +29 %, ramen +27 % (50.000 al mes), mochi +25 %, boba +23 % y salsa de soya +22 % (oct–jun).
- Caen bubble tea (−26 %; boba sube +23 %), soju (−22 %) y el genérico "comida coreana" (−11 %). En cambio suben los platos coreanos concretos.
- En ramen instantáneo domina Maruchan (unas 10.000 búsquedas al mes en ideas, contra unas 2.650 de Samyang y Buldak). "Ramen cerca de mí" tiene unas 50.000 al mes (+900 %) y hay escena de ramenerías.
- La importación de tapioca se multiplicó por 3,5 en kilos (2021→2025, 54 % desde Taiwán). En fideos de la partida 190230 los kilos suben +62 % y el valor +23 %. Corea pesa solo 4 % como origen directo.
- Australia: 12 de 26 tendencias aparecen antes allá y llegan con fuerza (adelanto mediano de unos 2,5 años; kale y açaí llegan débiles), 5 son simultáneas y hard seltzer nunca llegó. El rezago bajó de 2–3 años (antes de 2020) a 0–5 trimestres. La correlación del crecimiento es débil (mediana 0,37–0,39). Sirve como radar de qué y de cuándo se desinfla una moda (kombucha, bubble tea), no para pronosticar cifras.
- Radar Australia: hojicha, yuzu y katsu sando crecen allá y en Chile no llegan. Gochujang, dumplings y hot pot ya están llegando. Corn dog coreano, mochi donut y tanghulu se desinflaron en Australia y en Chile no pegaron.

## Archivos creados o modificados
- `entregables/2026-10-21_tendencias-asiaticas_trends-ads-australia.md` — informe completo.
- `datos/referencia/2026-10-21_terminos-busqueda_asiaticos.csv` y `..._para-pegar.txt` — términos.
- `datos/crudos/2026-10-21_google-trends_cl_2anios_individual_asiaticos.csv` y `..._volumen-relativo_asiaticos.csv` — Trends Chile.
- `datos/crudos/2026-10-21_google-ads_asiaticos_100-terminos_12m.tsv` y `..._ideas_24m.tsv` — exportaciones de Ads (convertidas a UTF-8, sin otros cambios).
- `datos/crudos/2026-10-21_un-comtrade_importaciones-chile_asiaticos.csv` — importaciones.
- `datos/crudos/2026-10-21_google-trends_au-vs-cl_trimestral_26-temas.csv` y `..._5anios_15-temas-asiaticos.csv` — Australia contra Chile (el segundo es un resumen anual; ube se descarta porque Trends eligió el tema "Uber").
- `datos/limpios/2026-10-21_google-trends_cl_2anios_asiaticos_resumen.csv` / `_series-largo.csv`, `datos/limpios/2026-10-21_google-ads_asiaticos_terminos.csv` / `_ideas_clasificadas.csv` / `_ideas_resumen.csv`, `datos/limpios/2026-10-21_matriz-asiaticos_trends-x-ads.csv`, `datos/limpios/2026-10-21_au-vs-cl_resumen_por-tema.csv` / `_correlacion_por-rezago.csv`.
- `scripts/procesar_google_trends.py`, `scripts/procesar_google_ads_ideas.py` y `scripts/analizar_australia_vs_chile.py` — nuevos.

## Decisiones propuestas (para acordar en grupo)
- Sumar la categoría asiática al radar con 5 candidatas: caldo de ramen listo (líquido; calza con el eje propuesto), té con leche o boba listo para beber, dumplings congelados, onigiri o kimbap para la colación, y salsas coreanas.
- Usar el indicador octubre–junio como medida principal de tendencia en las próximas capturas de Trends, para que los picos de invierno no se lean como tendencia.
- Incorporar Australia al benchmark internacional como señal de radar (no como predictor de cifras) y repetir la prueba con EE.UU. y Reino Unido.
- No apostar por modas que ya se desinflaron en Australia sin entrar en Chile (corn dog coreano, mochi donut, tanghulu).

## Pendientes y siguiente paso
- [ ] Góndola y Mercado Libre (A3): ramen o caldo, dumplings congelados y boba (marcas y precios) — por asignar.
- [ ] Confirmar qué explica el pico de la semana del 2-ago-2026 — Boris.
- [ ] Llevar las 5 candidatas asiáticas al radar y al dashboard — Boris.
- [ ] Repetir la prueba de rezago con EE.UU. y Reino Unido — Boris o Chalo.
- [ ] Volumen de ramen coreano por marca (Aduanas o importadores de Patronato) — Chalo.

## Contexto para la próxima sesión
- Trends se captura desde Chrome con la API interna (`/trends/api/explore` + `widgetdata/multiline`). Con unas 60 consultas seguidas aparecen errores 429; con espera progresiva (15–60 s) salen unos 100 términos en 40 minutos.
- El texto largo se extrae mejor escribiéndolo en la página y leyéndolo con get_page_text, porque el resultado de JavaScript se corta cerca de 2.000 caracteres.
- Al usar "temas" de Trends, revisa el tema elegido: poke dio "Poker" y se corrigió; ube dio "Uber" y se descartó. Las series por tema muestran ceros falsos entre 2016 y 2019 en algunos casos; el script los interpola.
- UN Comtrade responde desde el navegador (pestaña en comtradeapi.un.org + fetch), no desde la terminal.
