---
fecha: 2026-10-13 00:23
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 0
paso_del_plan: A1 Demanda (ampliación) y dashboard
estado: completado
---

# Ampliación de Google Trends a 100 términos y dashboard v2

## Objetivo
Ampliar la búsqueda de Trends a 100 conceptos, incluyendo líquidos y aguas funcionales, y hacer el dashboard más interactivo.

## Qué se hizo
- Se sumaron 58 términos a `datos/referencia/terminos-busqueda.csv` (24 de bebidas y aguas) y se reordenaron las categorías: bebidas y aguas, lácteos, suplementos, panadería y cereales, endulzantes.
- Se capturaron las series de 2 años, el volumen relativo con granola como ancla y las consultas en aumento de 10 términos de líquidos y suplementos. Misma ventana que ayer (2024-10-06 a 2026-10-04).
- Dashboard v2 (https://claude.ai/artifact/5S6M6umJvaDBJDjrENxKKt):
  - pestañas Resumen, Demanda, Competencia, Todos los términos y Método;
  - filtro por categoría, buscador y orden por variación o volumen;
  - clic en un término para ver su curva semanal y sus consultas en aumento;
  - mapa de volumen contra crecimiento, mediana por categoría y tablas ordenables.
- El informe `entregables/2026-10-12_trends-y-meta_primera-pasada.md` tiene una sección nueva con la ampliación.

## Hallazgos
Fuente: Google Trends Chile, captura 2026-10-13.
- 56 de 100 términos tienen datos suficientes. Casi ninguna "agua funcional" se busca: ni agua funcional, alcalina, con electrolitos, con colágeno, con vitaminas ni bebida probiótica.
- Líquidos que crecen: agua con gas (+47 %), leche de avena (+43 %), matcha (+29 %), jugo natural (+28 %), agua de coco (+18 %), agua mineral (+15 %), electrolitos (+13 %; "sobres de electrolitos" +450 %). Cold brew sube +183 % desde una base baja. Hidratación (+17 %) está inflada por el Mundial 2026.
- Otros que crecen: pan de masa madre (+42 %), kimchi (+32 %), leche sin lactosa (+24 %), tofu (+23 %), creatina (+16 %, volumen alto; gomitas +600 %).
- Caen: espirulina, pistachos, cúrcuma, colágeno hidrolizado, pan sin gluten.
- El formato (sobre, gomita, polvo, porción individual) aparece una y otra vez como innovación simple.

## Archivos creados o modificados
- `datos/referencia/terminos-busqueda.csv` — 100 términos con categoría.
- `datos/crudos/2026-10-13_google-trends_cl_2anios_individual_100.csv` — series semanales de los 100 términos.
- `datos/limpios/2026-10-13_google-trends_cl_2anios_resumen_100.csv` — indicadores.
- `datos/limpios/2026-10-13_google-trends_cl_2anios_series-largo_100.csv` — formato largo (para el dashboard).
- `datos/crudos/2026-10-13_google-trends_cl_2anios_consultas-en-aumento.csv` — renombrado desde el del 12-oct, con 18 filas nuevas.
- `datos/crudos/2026-10-12_meta-ads-library_cl_busquedas.csv` — columna renombrada a `anunciantes_destacados`.
- `entregables/2026-10-12_trends-y-meta_primera-pasada.md` — sección de la ampliación.

## Decisiones propuestas (para acordar en grupo)
- Si el grupo explora aguas, nombrar el producto por su beneficio concreto (por ejemplo, electrolitos en sobre o agua de coco), no como "agua funcional".
- Sumar "formato" (sobre, gomita, polvo, porción individual) como eje de diferenciación en la matriz de puntaje.

## Pendientes y siguiente paso
- [ ] Planificador de Google Ads con los 100 términos — Mario.
- [ ] Revisar en góndola y online: agua con gas, electrolitos, agua de coco, cold brew (A3) — por asignar.
- [ ] Hacer push del commit (GitHub Desktop) y compartir el dashboard — Boris.

## Contexto para la próxima sesión
Trends limita la frecuencia de consultas: con espera progresiva (15–60 s) se completaron 58 términos en unos 30 minutos. Los términos de volumen bajo traen valores solo en las últimas 3 semanas: es un efecto del procesamiento de Google, no una señal de alza.
