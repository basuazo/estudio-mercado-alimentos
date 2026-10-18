---
fecha: 2026-10-17 13:54
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: B Benchmarking internacional (B1, B2 y fuentes de informes de A4)
estado: completado (primer barrido; cobertura despareja)
---

# Benchmark internacional: primer barrido de marcas e informes de consultoras

## Objetivo
Centralizar marcas de referencia, cifras de mercado e informes de consultoras para las 23 oportunidades del radar, y dejar una señal internacional por oportunidad para la matriz del 28-oct.

## Qué se hizo
- Seis subagentes en paralelo (hidratación y funcionales; café y té; proteína, lácteos y vegetal; sólidos y snacks; informes globales; Chile y LatAm) con un esquema común: cada fila tiene fuente, fecha, cita y estado de verificación.
- Control cruzado independiente: se volvieron a abrir 9 fuentes de cifras centrales y las 9 cuadraron (en una, el 20 % exacto de crecimiento no apareció al releer; el tamaño sí).
- Consolidación en 5 tablas y lectura por oportunidad (`senal-por-oportunidad`), con confiabilidad de la fuente marcada.

## Hallazgos
- Señal internacional favorable con confianza alta: electrolitos en sobre, cold brew, yogur griego familiar, agua de coco y "sin sellos" como criterio de diseño. Favorable con barrera alta: café o batido proteico (maquila aséptica) y matcha (tencha +265 %).
- Neutral o desfavorable para un entrante chico: granola, leche sin lactosa, té helado sin azúcar, agua con gas saborizada, creatina en gomitas y avena barista.
- El modelo que más se repite con poco capital es marca + maquila o importación (Vita Coco, Score, LMNT). Maquilar para marca propia es la segunda vía; en Chile la marca propia es solo 13,4 % del supermercado (NIQ, 1er semestre 2026).
- Score (energéticas maquiladas en Europa) aparece como caso chileno relevante; las energéticas no están en el radar.
- Detalle y fuentes: `entregables/2026-10-17_benchmark-internacional_primer-barrido.md`.

## Archivos creados o modificados
- `entregables/2026-10-17_benchmark-internacional_primer-barrido.md` — síntesis, límites y decisiones propuestas.
- `datos/limpios/2026-10-17_benchmark-internacional_senal-por-oportunidad.csv` — 23 oportunidades con etapa, señal, barrera y filas de respaldo.
- `datos/limpios/2026-10-17_benchmark-internacional_marcas.csv` (167), `_mercado.csv` (110), `_informes.csv` (78), `_notas-categoria.csv` (42).
- `estado/boris.md`.

## Decisiones propuestas (para acordar en grupo)
- Agregar a la matriz una columna de señal internacional, separada de la demanda en Chile.
- Bajar de prioridad granola, leche sin lactosa, té helado sin azúcar y creatina en gomitas.
- Evaluar agua de coco como candidata.
- Agregar el modelo de entrada (marca con maquila / importación con marca / maquila para marca propia) como dimensión de la matriz.
- Incluir el riesgo de materia prima (café, matcha) en el criterio de margen.

## Pendientes y siguiente paso
- [ ] Segunda pasada del benchmark (presencia en Chile de bebidas, liofilizados, Rabobank, BCG, Kantar Brand Footprint, Anuga) — Boris.
- [ ] Plazos y costos de resolución sanitaria, registro ISP y aranceles por TLC — Mario (cruza con la consulta regulatoria del 30-oct).
- [ ] Llevar la señal internacional a la matriz y al dashboard — Boris, antes del 28-oct.

## Contexto para la próxima sesión
- La auditoría del 16-oct pidió no contar como benchmark la captura en retail chileno: en estas tablas la presencia en Chile va en una columna aparte.
- Las cifras de firmas genéricas de *market research* están marcadas como confiabilidad baja; no usarlas para tamaño de mercado sin otra fuente.
- Se agotó el cupo de búsquedas web del turno; la cobertura de algunas categorías es delgada (ver la columna `confianza`).
