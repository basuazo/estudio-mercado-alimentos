# Dashboard "Radar de alimentos Chile" (copia de respaldo)

Copia del código de la página del dashboard publicado en Claude (versión 2, 2026-10-13). Sirve como respaldo y para que el equipo vea cómo está armado.

**Importante:** `radar-alimentos_pagina.html` no se abre solo con doble clic. Usa el motor de dashboards de Claude (funciones `dash.*` y estilos propios), así que solo se ve dentro del artefacto en claude.ai. Para verlo, Boris tiene que compartir el enlace del artefacto desde claude.ai (por defecto es privado).

Lo que sí se puede revisar directo en el repositorio son los datos que alimentan cada pestaña:

| Fuente del dashboard | Archivo en el repo |
|---|---|
| Tendencia Google Trends (100 términos) | `datos/limpios/2026-10-13_google-trends_cl_2anios_resumen_100.csv` |
| Series semanales Trends | `datos/limpios/2026-10-13_google-trends_cl_2anios_series-largo_100.csv` |
| Consultas en aumento | `datos/crudos/2026-10-13_google-trends_cl_2anios_consultas-en-aumento.csv` |
| Anuncios Meta por palabra | `datos/crudos/2026-10-12_meta-ads-library_cl_busquedas.csv` |
| Marcas que pautan en Meta | `datos/limpios/2026-10-12_meta-ads_marcas-activas.csv` |

Resumen de hallazgos: `entregables/2026-10-12_trends-y-meta_primera-pasada.md`. Detalle de la sesión: `bitacora/2026-10-13_0023_boris_trends-100-terminos-dashboard.md`.

Fuentes: Google Trends Chile y Biblioteca de anuncios de Meta, capturadas el 2026-10-12 y 2026-10-13.
