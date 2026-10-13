---
fecha: 2026-10-12 23:59
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 0
paso_del_plan: A1 Demanda (Google Trends) y A2 Competencia (Meta)
estado: completado (primera pasada)
---

# Primera pasada de Google Trends (2 años) y Biblioteca de anuncios de Meta

## Objetivo
Cumplir la tarea de Boris antes del 14-oct: Google Trends con unos 40 términos y 10 marcas con anuncios activos en Meta.

## Qué se hizo
- Se armó la lista de 42 términos de búsqueda en cuatro grupos: atributos, barras y snacks, bebidas funcionales, granel fraccionado (más canal/ocasión). Mario la usará para el Planificador de Google Ads.
- Google Trends Chile, 2 años (2024-10-06 a 2026-10-04): serie semanal por término, variación año 2 vs año 1, volumen relativo con granola como ancla y consultas en aumento de 18 términos. Los datos se sacaron desde el Chrome de Boris, porque Trends está bloqueado en el entorno de Claude.
- Biblioteca de anuncios de Meta (Chile, activos): 8 palabras clave y fichas de 10 marcas.
- Dashboard con todo lo anterior: https://claude.ai/artifact/5S6M6umJvaDBJDjrENxKKt (privado hasta que Boris lo comparta).
- Nota de protocolo: el commit del 12-oct "guías de uso y renombre a estudio-mercado-alimentos" (`guias/01-clonar-repositorio.md`, `guias/02-trabajar-con-claude.md`) quedó sin entrada de bitácora. Se registra aquí.

## Hallazgos
Fuente: Google Trends y Biblioteca de anuncios de Meta, captura 2026-10-12. Detalle en `entregables/2026-10-12_trends-y-meta_primera-pasada.md`.
- Crecen con volumen relevante: yogurt griego (+70 %), leche de avena (+43 %, "barista" +300 %), granola (+40 %), whey protein (+21 %), sin azúcar (+12 %).
- Kefir (+44 %) fue un peak puntual en oct–nov 2025; no es tendencia.
- Caen: keto (−25 %), probióticos (−28 %), vegano (−14 %), kombucha (plana o en baja).
- Términos genéricos ("snack saludable", "bebida proteica", "barra keto") casi no se buscan. Barra de proteína tiene volumen bajo y plano: medirla en Ads, Mercado Libre y góndola.
- Meta: yogurt griego (~62 anuncios) y leche de avena (~8) casi no tienen pauta, pese a crecer fuerte en búsquedas. Proteína (~2.800) y sin azúcar (~2.300) están saturados, aunque sobre todo por apps y suplementos.
- La colación (escolar, oficina, media tarde) es la ocasión más pautada: Tika, Underfive, NotCo.
- Marcas: Kremosa (51 anuncios, pauta desde ene-2025), Feroz Snack (27), AMA Time (24), GoNat (17, producto por confirmar), Tika Foods, Underfive, EasyProtein, The Not Company (NotSquare, sep-2026), B-Japi, Surlat (referencia).

## Archivos creados o modificados
- `datos/referencia/terminos-busqueda.csv` — lista de 42 términos (compartida con Mario).
- `datos/crudos/2026-10-12_google-trends_cl_2anios_individual.csv` — series semanales.
- `datos/crudos/2026-10-12_google-trends_cl_2anios_consultas-en-aumento.csv` — consultas en aumento.
- `datos/limpios/2026-10-12_google-trends_cl_2anios_resumen.csv` — indicadores por término.
- `datos/limpios/2026-10-12_google-trends_cl_2anios_series-largo.csv` — 14 términos en formato largo (para el dashboard).
- `datos/crudos/2026-10-12_meta-ads-library_cl_busquedas.csv` — anuncios por palabra clave.
- `datos/limpios/2026-10-12_meta-ads_marcas-activas.csv` — 10 marcas.
- `entregables/2026-10-12_trends-y-meta_primera-pasada.md` — informe de la primera pasada.

## Decisiones propuestas (para acordar en grupo)
- Usar estos resultados para elegir las categorías foco el 14-oct. Propuesta: (1) lácteos y bebidas con proteína o sin azúcar, (2) granola y colaciones, (3) bebidas vegetales para cafeterías. Barras quedan en observación hasta tener datos de Ads y góndola.
- Descartar keto, vegano, kombucha y probióticos como eje de entrada.
- Usar "colación" como ocasión de consumo transversal en la etnografía.

## Pendientes y siguiente paso
- [ ] Planificador de Google Ads con `datos/referencia/terminos-busqueda.csv` — Mario.
- [ ] Revisar en góndola y supermercados online por qué yogurt griego y leche de avena casi no tienen pauta digital (A3) — por asignar.
- [ ] Confirmar qué vende GoNat — Boris.
- [ ] Repetir Meta cada semana y Trends cada mes — Boris.
- [ ] Método B3 con Mercadona y Tesco (barras) — Boris.
- [ ] Compartir el dashboard con Mario y Chalo desde el menú Compartir — Boris.

## Contexto para la próxima sesión
Trends se consulta desde el Chrome del usuario: en el navegador, la API interna de Trends (`/trends/api/explore` y `widgetdata`) responde; con más de unas 40 consultas seguidas aparece un límite de frecuencia, así que hay que esperar y reintentar. En Meta, el texto de la página sirve para extraer anunciante, fecha y número de anuncios. Los conteos por marca son un piso, no el total. Cuenta como una sola fuente de las tres que pide la lista corta.
