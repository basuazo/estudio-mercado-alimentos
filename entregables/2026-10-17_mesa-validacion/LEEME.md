# Mesa de validación (Mercado Libre y Google Ads)

Artefacto privado de Boris: https://claude.ai/artifact/W6Nvd15kmsRkdYuoSmVT5k ("Mesa de validación ML"). Creado el 2026-10-17.

## Para qué sirve
Corregir de raíz los errores de la auditoría del 16-oct: en vez de adivinar formato, pack, marca y relevancia
con reglas escondidas en los scripts, una persona confirma o corrige lo que propone el script, y eso queda guardado.

- **Publicaciones**: una ficha por publicación de la captura de Mercado Libre, con clase (objetivo, adyacente, descartar),
  tipo, marca, envases, contenido, unidad y porciones prellenados. El precio por unidad se recalcula al editar.
- **Marcas**: corregir una marca detectada se aplica a todas sus publicaciones.
- **Google Ads**: tipo de cada término (específico, paraguas, otro producto, informativo, marca) y su concepto. Muestra el índice específico al tiro.

Lo validado vive en la base del artefacto (colecciones `validacion`, `marcas`, `ads`). La página solo la ve Boris hasta que la comparta.

## Flujo
1. `python scripts/resumir_captura_mercadolibre.py proponer` y `python scripts/google_ads_terminos.py proponer` + `json`
   generan `datos/limpios/*_propuesta.json` y `*_google-ads_terminos_para_validar.json`, que se suben a la página.
2. Se valida en la página.
3. El agente baja la base del artefacto (ArtifactData, una carpeta con un JSON por documento) y corre
   `python scripts/importar_validacion_mercadolibre.py <carpeta>` y `python scripts/google_ads_terminos.py importar <carpeta>/ads`.
4. `python scripts/resumir_captura_mercadolibre.py resumir` y `python scripts/actualizar_radar_google_ads.py`.

Con una captura nueva solo aparecen como pendientes las publicaciones que no estaban validadas (la clave es el id de la publicación).

`mesa.html` es la copia de la página publicada (sin los JSON, que están en `datos/limpios/`).
