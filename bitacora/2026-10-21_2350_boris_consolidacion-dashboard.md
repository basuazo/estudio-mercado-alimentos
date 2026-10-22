---
fecha: 2026-10-21 23:50
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: Dashboard de inversión (estructura)
estado: completado
---

# Consolidación del dashboard en seis pantallas fijas

## Objetivo
Boris pidió que el dashboard se consolide en vez de sumar pestañas con cada capa nueva. Eligió la estructura de 6 pantallas por pregunta.

## Qué se hizo
- **De 11 pantallas a 6:** Resumen, Oportunidades, Demanda, Oferta, Industria y Método y calidad. Los enlaces viejos (`#asia`, `#australia`, `#lineas`, `#auditoria`, `#mejoras`) llevan a la pantalla nueva que corresponde.
- **Selector de foco** arriba ("Todo el universo", "Salud y funcional", "Asiático"). Filtra gráficos y tablas de todas las pantallas; los indicadores cuentan todo el universo.
- **Un solo universo de oportunidades:** las 23 del radar más las 14 líneas asiáticas, en `oportunidades.json` con el campo `foco`. Las líneas asiáticas aparecen en el mapa, en el conteo de familias, en la lectura preliminar y en la matriz.
  - Para contar familias se usa la misma regla del benchmark: Australia y Comtrade cuentan solo si la señal es favorable.
  - La oferta en supermercado online no cuenta como familia hasta que el grupo lo acuerde.
  - Resultado: siguen siendo 5 de 37 con 3 familias o más (las mismas 5 del 18-oct).
- **Demanda con una sola medida para los 200 términos:** variación octubre–junio calculada desde los crudos de los dos estudios. La deriva común queda en +9 % (79 términos con datos suficientes); antes era +8,45 % a 12 meses.
  - Una sola tabla, un mapa volumen × crecimiento y una curva mensual para todos los términos.
  - Australia queda como sección "Señal anticipada" dentro de Demanda.
- **Oferta:** Mercado Libre más una sección de supermercado online (mapa demanda × oferta, pauta de Mercado Libre y productos vistos).
- **Industria:** se sumó la tarjeta de insumos asiáticos importados (Comtrade).
- **Método y calidad:** junta lo que eran Metodología, Auditoría de datos y Cómo mejorar, con el método de las capas del 21-oct.
- Datasets reemplazados y borrados del dashboard: `trends_terminos`, `trends_mensual`, `asia_terminos`, `asia_series` y `lineas_oferta`. Sus archivos siguen en el repo.
- Se probó la página fuera del dashboard (jsdom con los datos reales): las 6 pantallas y los 3 focos dibujan sin errores.

## Archivos creados o modificados
- `entregables/2026-10-16_auditoria-y-dashboard-inversion/consolidar_2026-10-21.py` — nuevo; genera `oportunidades.json` (37), `terminos_busqueda.json` (200) y `series_mensuales.json`.
- `entregables/2026-10-16_auditoria-y-dashboard-inversion/datos/` — esos tres JSON.
- `entregables/2026-10-16_auditoria-y-dashboard-inversion/dashboard_pagina.html` y `LEEME.md` — página nueva y regla de estructura.

## Decisiones propuestas (para acordar en grupo)
- **Regla de estructura del dashboard:** no se crean pantallas nuevas. Cada capa entra como filas con su `foco` en los datasets existentes (detalle en el LEEME del dashboard).
- Usar octubre–junio como medida de crecimiento de búsqueda para todos los términos. El "Sobre deriva" de las 23 oportunidades del radar sigue siendo el auditado a 12 meses hasta recalcularlo.

## Pendientes y siguiente paso
- [ ] Recalcular "Sobre deriva" de las 23 oportunidades del radar con octubre–junio, para que el mapa del Resumen use una sola medida — Boris (con Claude).
- [ ] Compartir el dashboard con Mario y Chalo — Boris.

## Contexto para la próxima sesión
- Orden para refrescar: `build_dash.py` → `actualizar_2026-10-18.py` → `actualizar_2026-10-21.py` → `consolidar_2026-10-21.py`.
- La página se escribe en `files/index.html` del artefacto con ArtifactData (versión 7 al cierre); los datos van como assets.
- Las funciones de cada pantalla viven en `window.RZ` (`drawDemanda`, `drawTerminos`, `drawAustralia`, `drawRetail`, `drawImpAsia`…). `window.RZ.focoOk(r)` aplica el foco.
