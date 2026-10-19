---
fecha: 2026-10-18 20:40
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: Revisión general · preparación de la presentación al grupo
estado: completado
---

# Actualización del dashboard de inversión con el trabajo del 17-oct

## Objetivo
Llevar al dashboard la corrección de Mercado Libre y Google Ads y el benchmark internacional del 17-oct, antes de presentarlo al grupo.

## Qué se hizo
- `entregables/2026-10-16_auditoria-y-dashboard-inversion/actualizar_2026-10-18.py` (corre después de `build_dash.py`) toma `datos/limpios/2026-10-17_google-ads_indice_oportunidades.csv`, `datos/limpios/2026-10-16_mercadolibre_cl_resumen_oportunidad.csv` y `datos/limpios/2026-10-17_benchmark-internacional_senal-por-oportunidad.csv`.
- Google Ads: índice de términos específicos del repo; matcha listo para beber, granola con legumbre, creatina en gomitas y té helado sin azúcar quedan "no medido".
- Mercado Libre: precio por oportunidad y tipo de producto del script corregido (propuesta automática, 0 fichas validadas). Nueva tabla en "Oferta y precios"; la anterior queda como "antes y después".
- Benchmark internacional: columna y tabla nuevas en "Oportunidades". Cuenta como familia solo si la señal es favorable con confianza alta o media y la oportunidad no tenía ya esa familia.
- Errores de la auditoría con estado: 9 corregidos el 17-oct, 4 en corrección (falta validar), 55 abiertos (13 graves).
- Avisos del Resumen actualizados y aviso nuevo "Qué cambió desde el 16-oct".

## Hallazgos
- Con familias independientes ahora pasan la regla de 3: electrolitos en sobre, café o batido proteico, granola con legumbre, chai y agua de coco (5 de 23; el radar decía 4). Ninguna tiene evidencia de terreno.
- Lecturas preliminares que cambian: agua de coco pasa a "investigar" (benchmark favorable, confianza alta; modelo Vita Coco); agua con gas saborizada baja a "radar"; té helado sin azúcar a "descartar".
- Para investigar quedan electrolitos, cold brew, yogur griego familiar y agua de coco; avena barista sigue como "terreno primero".

## Archivos creados o modificados
- `entregables/2026-10-16_auditoria-y-dashboard-inversion/actualizar_2026-10-18.py` — nuevo.
- `entregables/2026-10-16_auditoria-y-dashboard-inversion/datos/{oportunidades,errores,hallazgos,ml_resumen}.json` — actualizados o nuevos.
- `entregables/2026-10-16_auditoria-y-dashboard-inversion/dashboard_pagina.html`, `build_dash.py` — actualizados.

## Decisiones propuestas (para acordar en grupo)
- Las mismas del 16 y 17-oct; se suma: tratar agua de coco como candidata a investigar (importación con marca).

## Pendientes y siguiente paso
- [ ] Validar en la mesa las fichas de electrolitos y proteico y re-correr el resumen; luego refrescar el dashboard — Boris.
- [ ] Corregir la columna `senal_mercadolibre` del radar (error MER-03) — Boris.

## Contexto para la próxima sesión
Para refrescar el dashboard: `build_dash.py` y luego `actualizar_2026-10-18.py`, subir los JSON cambiados como assets del artefacto https://claude.ai/artifact/MDjMSTxEXamWJjUeb5mzbH y actualizar `datasets/<id>` (url y updated).
