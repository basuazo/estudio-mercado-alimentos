# Auditoría del estudio de mercado y dashboard "Radar de inversión en alimentos"

**Fecha:** 2026-10-16 · **Persona:** Boris (con Claude, Cowork) · **Paso del plan:** cierre Fase 1, preparación de la reunión del 28-oct

Dashboard publicado en Claude: https://claude.ai/artifact/MDjMSTxEXamWJjUeb5mzbH (privado hasta que Boris lo comparta desde el menú Compartir).

## Qué es

Una auditoría completa de todo lo capturado entre el 10 y el 16 de octubre (Trends, Meta, Google Ads, Mercado Libre, SII, UN Comtrade, benchmark B3, radar y plan), integrada en un dashboard de 8 pantallas para decidir en grupo:

1. **Resumen**: indicadores clave, avisos críticos, mapa de demanda, fuentes del radar vs familias independientes, lectura preliminar por oportunidad.
2. **Oportunidades**: matriz integrada de las 23 oportunidades con notas por fuente; factores no cubiertos por los datos (regulatorio, capital, operación, competencia, canal).
3. **Demanda y ciclos**: crecimiento sobre la deriva común, series mensuales, estacionalidad, inflación del término clave del radar, términos de Google Ads.
4. **Oferta y precios**: precios recalculados de Mercado Libre (packs normalizados), marcas por término, concentración.
5. **Industria**: SII con base 2019 y 2022; importaciones en valor, volumen y USD/kg.
6. **Auditoría de datos**: notas por fuente, 68 errores con evidencia y corrección, 38 limitaciones con camino de solución.
7. **Metodología**: cómo se hizo, definiciones, advertencias, matriz de puntaje propuesta, cobertura de la matriz, marco regulatorio.
8. **Cómo mejorar**: 13 brechas con responsable y fecha, 14 estrategias, 34 fuentes nuevas verificadas.

## Cómo se hizo

- Cinco auditores independientes (subagentes de Claude), uno por familia de fuentes, recalcularon las cifras desde los archivos crudos del repositorio en **modo solo lectura** y revisaron los scripts. Un sexto investigó fuentes y estrategias de mejora en la web.
- `build_dash.py` integra sus resultados por oportunidad (nombre exacto del radar) y genera los JSON de `datos/`. Las rutas del script son las del espacio de trabajo de Claude; para re-ejecutarlo hay que ajustar `B`.
- Un revisor independiente verificó 52 cifras del dashboard contra los archivos del repo (todas cuadran salvo redondeo) y propuso correcciones de reglas y textos, ya aplicadas → `auditorias/verificacion_resultado.md`.
- `dashboard_pagina.html` es la copia de la página del dashboard (solo se ve dentro del artefacto; usa el motor de dashboards de Claude).

## Hallazgos principales

- **La regla de 3 fuentes se aplicaba mal.** Trends y Google Ads miden lo mismo; tendencias, catálogo y captura de Mercado Libre son una sola fuente. Contando familias independientes, solo 3 de 23 llegan a 3 (café/batido proteico, granola con legumbre y chai); electrolitos baja a 2 y matcha listo para beber a 1.
- **Error regulatorio en la tesis de líquidos sin sellos:** el sello ALTO EN aplica solo a nutrientes añadidos; un electrolito con sodio añadido, evaluado disuelto, puede llevar ALTO EN SODIO. Falta resolver suplemento vs alimento.
- **Cifras citadas que no se sostienen:** el "último trimestre" de Trends comparaba jul–oct 2026 con oct–dic 2024 (proteína +22 % → −0,4 % real); 39 términos de Trends son ruido; precios de cold brew y fruta liofilizada inflados por packs mal leídos; +265 % de comidas preparadas es un artefacto de clasificación; +92 % de extractos de café es precio, no volumen.
- **Deriva común:** la mediana de crecimiento de búsqueda es +8,45 % (50 términos con señal); un crecimiento menor no es señal (electrolitos +12,8 % está casi en la deriva).
- **El mayor crecimiento de búsqueda** (yogur griego, leche de avena, pan de masa madre, tofu, leche sin lactosa) está en productos con frío, producción láctea o grandes competidores.
- **La matriz de decisión tiene evidencia en ~14 %** (ponderado, solo datos) para las 5 candidatas: faltan margen, evidencia de compra, capital y ruta regulatoria.

## Archivos

| Archivo | Contenido |
|---|---|
| `auditorias/auditoria_trends_meta.md` | Google Trends y Meta (nota B; Meta C) |
| `auditorias/auditoria_google_ads.md` | Keyword Planner (nota C) |
| `auditorias/auditoria_mercadolibre.md` | API y captura (nota C); riesgo de términos de uso |
| `auditorias/auditoria_macro.md` | SII, Comtrade, maquiladores, distribuidores (nota B) |
| `auditorias/auditoria_metodo.md` | Regla de fuentes, sesgos, regulatorio, matriz propuesta, brechas |
| `auditorias/verificacion_resultado.md` | Verificación independiente del dashboard |
| `fuentes-y-estrategias-de-mejora.md` | 34 fuentes y 14 estrategias para mejorar el análisis |
| `datos/*.json` | Datasets que alimentan el dashboard |
| `build_dash.py` | Script de integración |
| `dashboard_pagina.html` | Copia de la página del dashboard |

Nota: los precios de Mercado Libre son solo de uso interno mientras Mario valida los términos de uso (secc. 5.4 y 7.6).
