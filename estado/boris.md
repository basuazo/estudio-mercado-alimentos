# Estado de Boris

Archivo vivo de Boris. **Solo lo edita Boris (o su agente)**, al cerrar cada sesión. Los demás lo leen al iniciar.

**Actualizado:** 2026-10-16

- **En curso:** —
- **Terminado:**
  - Bases del SII procesadas (16-oct): crecimiento de empresas por actividad, peso de Ñuble y lista de posibles maquiladores → `bitacora/2026-10-16_1731_boris_sii-empresas-alimentos.md`.
  - Adelanto de pendientes de Mario y Chalo (16-oct): términos de uso por sitio, 31 distribuidores, importaciones UN Comtrade 2021–2025, lista de términos para Google Ads ampliada y búsqueda de Farmacia Mont → `bitacora/2026-10-16_1724_boris_pendientes-mario-y-chalo.md`.
  - Catálogo de Mercado Libre limpio y clasificado, radar con señales de Mercado Libre (electrolitos y café proteico pasan a lista corta propuesta; 6 oportunidades nuevas) y captura manual preparada (guía + script de resumen) → `bitacora/2026-10-16_1653_boris_catalogo-limpio-y-radar.md`.
  - API de Mercado Libre (16-oct): solo entrega tendencias y catálogo; precios y vendidos van por captura manual. Script semanal `scripts/mercadolibre_api.ps1` y primeros CSV en `datos/crudos/` → `bitacora/2026-10-16_1615_boris_api-mercadolibre-script.md`.
  - B3 ronda 2 en 10 categorías, sólidos y líquidos (16-oct): candidatas electrolitos, café o batido proteico listo para beber y cold brew → `entregables/2026-10-16_b3-ronda2_solidos-y-liquidos.md`.
  - Prueba del método B3 con Mercadona y Tesco en barras (primera pasada, 16-oct): la barra proteica ya está competida en Chile → `entregables/2026-10-16_b3_barras-mercadona-tesco.md`.
  - Protocolo de estado por persona (`estado/`) y regla "commit antes de pull" (propuesta para el miércoles).
  - Plan del estudio de mercado (borrador para el miércoles).
  - Repositorio en GitHub y guías de uso.
  - Google Trends ampliado a 100 términos (incluye aguas y bebidas funcionales) y dashboard v2 interactivo.
  - Primera pasada de Google Trends (42 términos, 2 años) y Meta (10 marcas) → `entregables/2026-10-12_trends-y-meta_primera-pasada.md` y dashboard https://claude.ai/artifact/5S6M6umJvaDBJDjrENxKKt
- **Enfoque:** líquidos como eje del estudio (propuesta de Boris, por acordar con el grupo) y radar de otras oportunidades → `datos/limpios/2026-10-16_radar-oportunidades_boris.csv`.
- **Siguiente:**
  - [ ] Google Ads: crear cuenta y correr el planificador (`guias/04-google-ads-keyword-planner.md`), o coordinarlo con Mario.
  - [ ] Confirmar que Mario y Chalo tienen acceso al repositorio y compartirles el dashboard.
  - [ ] Cerrar pendientes de la ronda 2: tablas de Soprole, café proteico listo para beber en otros retailers, caso "libre de sellos" de Wild Protein, electrolitos en farmacias y llamada a cafeterías.
  - [ ] Capturar a mano novedades de Mercadona y Tesco (la herramienta no las lee).
  - [ ] Captura manual en Mercado Libre de las 3 candidatas (45–60 min) con `guias/03-captura-manual-mercadolibre.md`, luego `python scripts/resumir_captura_mercadolibre.py`.
  - [ ] Revisar el estado de las oportunidades con 2 fuentes que siguen en radar.
  - [ ] Correr `scripts/mercadolibre_api.ps1` y `scripts/limpiar_catalogo_mercadolibre.py` la semana del 23-oct.
  - [ ] Sesión de 30 min de introducción a GitHub con Mario.
  - [ ] Confirmar qué vende GoNat; repetir Meta semanal.
- **Bloqueos:** ninguno. Mario puede usar `datos/referencia/terminos-busqueda.csv` para Google Ads.
