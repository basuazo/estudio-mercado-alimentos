# Estado de Boris

Archivo vivo de Boris. **Solo lo edita Boris (o su agente)**, al cerrar cada sesión. Los demás lo leen al iniciar.

**Actualizado:** 2026-10-16

- **En curso:** —
- **Terminado:**
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
  - [ ] Confirmar que Mario y Chalo tienen acceso al repositorio y compartirles el dashboard.
  - [ ] Cerrar pendientes de la ronda 2: tablas de Soprole, café proteico listo para beber en otros retailers, caso "libre de sellos" de Wild Protein, electrolitos en farmacias y llamada a cafeterías.
  - [ ] Capturar a mano novedades de Mercadona y Tesco (la herramienta no las lee).
  - [ ] Captura manual en Mercado Libre de las 3 candidatas (30 min) con `datos/referencia/pauta-captura-mercadolibre.md`, partiendo por Lytos, ENA, Quenut y Superieur.
  - [ ] Actualizar el radar (electrolitos en polvo, matcha, chai latte, comida liofilizada outdoor) y limpiar el catálogo de Mercado Libre por dominio.
  - [ ] Correr `scripts/mercadolibre_api.ps1` la semana del 23-oct.
  - [ ] Sesión de 30 min de introducción a GitHub con Mario.
  - [ ] Confirmar qué vende GoNat; repetir Meta semanal.
- **Bloqueos:** ninguno. Mario puede usar `datos/referencia/terminos-busqueda.csv` para Google Ads.
