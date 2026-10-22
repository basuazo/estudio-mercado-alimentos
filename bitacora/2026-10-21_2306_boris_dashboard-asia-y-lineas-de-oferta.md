---
fecha: 2026-10-21 23:06
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: A3 Oferta y precios · dashboard de inversión
estado: completado (Mercado Libre queda para captura manual)
---

# Dashboard con tendencias asiáticas y Australia, y nuevas líneas de oferta

## Objetivo
Llevar al dashboard las tendencias asiáticas y la prueba de Australia, y revisar qué líneas de producto nuevas conviene estudiar en oferta (supermercados y luego Mercado Libre).

## Qué se hizo
- **14 líneas de producto** definidas desde las tendencias asiáticas. Cada una tiene su demanda (Ads y Trends), su señal de Australia y el estado de la oferta → `datos/limpios/2026-10-21_lineas-oferta-asiaticas.csv`.
- **Barrido de existencia en supermercados online:** 24 búsquedas en Santa Isabel y 18 en Tottus, desde el navegador de Claude. Se hizo a ritmo humano, solo primera página, respetando robots.txt y sin la API. Se guardó solo marca, precio, formato y fecha → `datos/crudos/2026-10-21_supermercados_lineas-asiaticas_busquedas.csv`. En Tottus se guardaron solo los productos del rubro, porque su búsqueda trae 48 resultados mezclados. Jumbo y Líder no se revisaron, por su robots.txt.
- **Mercado Libre preparado para captura manual:** 9 términos nuevos en `scripts/resumir_captura_mercadolibre.py`. Cada uno tiene reglas de objetivo, adyacente y descarte, tipos propios (caldo, congelado, perlas, salsa, fermentado, fideo instantáneo) y unidad de precio. Los tipos nuevos se aplican solo a esos términos; los 13 casos de prueba anteriores siguen correctos. La pauta está en `entregables/2026-10-21_lineas-de-oferta-asiaticas.md`.
- **Dashboard** (https://claude.ai/artifact/MDjMSTxEXamWJjUeb5mzbH): tres pantallas nuevas, con 10 datasets nuevos y 6 cálculos.
  - **Asia en Chile:** mapa volumen × crecimiento, categorías, curvas mensuales, tabla de 100 términos, ideas del Planificador y Comtrade.
  - **Australia como radar:** despegue de cada tendencia en los dos países, curvas comparadas, correlación según rezago y radar de 14 temas asiáticos.
  - **Nuevas líneas de oferta:** mapa demanda × oferta, pauta de Mercado Libre y productos vistos.
  - Además, un aviso "Qué cambió el 21-oct" en el Resumen.
  - Script `entregables/2026-10-16_auditoria-y-dashboard-inversion/actualizar_2026-10-21.py`; copia de la página en `dashboard_pagina.html`.
- **Corrección del informe de tendencias** (anotada al final del informe): el adelanto de Australia es de unos 2,5 años en las 12 tendencias que aparecieron primero allá y llegaron con fuerza. No son "14 con 5 trimestres": esa mediana mezclaba tendencias simultáneas y de Chile primero.

## Hallazgos
Fuente: Santa Isabel y Tottus (búsquedas del 21-oct-2026), y datos del informe de tendencias del 21-oct.
- **6 líneas con demanda (5.000 búsquedas al mes o más) y cero productos en los dos supermercados:** ramen coreano, boba y té con leche, onigiri y kimbap, gochujang, mochi y pasta miso.
- **Ramen premium:** D'Fab entró a Tottus como "nuevo" con ramen artesanal congelado (375 g, 6.490–6.790 CLP, unos 19.000 CLP/kg). Valida el formato y es el competidor directo de un caldo de ramen.
- **Gyozas congeladas:** solo Frutos del Maipo y Cuisine & Co (Santa Isabel), a 10.900–30.250 CLP/kg; en Tottus solo arrollados (Asia Wok).
- **Kimchi:** La Fermentista en Tottus (400 g, 7.350). **Matcha:** Krüger y Supremo. **Edamame:** solo Minuto Verde.
- **Ramen instantáneo masivo** (Maruchan, Nissin, Traverso, Cuisine & Co) y **salsas de soya** (más de 15 marcas) están saturados.

## Archivos creados o modificados
- `datos/crudos/2026-10-21_supermercados_lineas-asiaticas_busquedas.csv` y `datos/limpios/2026-10-21_lineas-oferta-asiaticas.csv` — nuevos.
- `entregables/2026-10-21_lineas-de-oferta-asiaticas.md` — informe y pauta de Mercado Libre.
- `scripts/resumir_captura_mercadolibre.py` — 9 términos asiáticos.
- `entregables/2026-10-16_auditoria-y-dashboard-inversion/` — `actualizar_2026-10-21.py`, `datos/{asia_*,au_*,lineas_*}.json`, `dashboard_pagina.html`, `LEEME.md`.
- `entregables/2026-10-21_tendencias-asiaticas_trends-ads-australia.md`, `bitacora/2026-10-21_2236_...` y `estado/boris.md` — corrección del adelanto de Australia (la bitácora anterior se corrigió por ser un error evidente de la misma sesión).

## Decisiones propuestas (para acordar en grupo)
- Llevar a la matriz 4 líneas asiáticas (ramen premium o caldo listo, gyozas congeladas, boba o té con leche, gochujang). Cada una tiene que pasar la regla de 3 familias.
- Contar "oferta en supermercado online" como familia propia, distinta de Mercado Libre.
- No priorizar ramen instantáneo masivo, salsas de soya ni edamame.

## Pendientes y siguiente paso
- [ ] Captura manual en Mercado Libre de los 4 términos de prioridad 1 (guía 05, 4.B) — Mario o Chalo.
- [ ] Terreno: Patronato (ramen coreano, gochujang, mochi, tapioca), rotación de D'Fab en Tottus, congelados de Jumbo y Líder — por asignar.
- [ ] Compartir el dashboard con Mario y Chalo — Boris.

## Contexto para la próxima sesión
- Chrome no estaba conectado; se usó el navegador de Claude.
- **Santa Isabel:** `santaisabel.cl/busqueda?ft=<termino>` muestra los productos tras unos 4 segundos. La búsqueda es aproximada ("mochi" trae Bon o Bon), así que hay que filtrar por rubro.
- **Tottus:** `tottus.cl/tottus-cl/buscar?Ntt=<termino>` trae 48 resultados mezclados; si hay una sola coincidencia abre directo la ficha.
- En los dos se guardó la captura en sessionStorage, con un lector de texto de la página.
- Para el dashboard: los datos van como archivos del artefacto (assets) y la página se escribe en `files/index.html` con ArtifactData.
