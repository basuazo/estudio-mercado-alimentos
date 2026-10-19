---
fecha: 2026-10-18 20:42
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: A1 Demanda (Google Ads), A2 Competencia (Meta), A3 Oferta y precios (Mercado Libre)
estado: completado
---

# Guía paso a paso y scripts para que Mario y Chalo capturen Meta, Google Ads y Mercado Libre

## Objetivo
Dejar listo, para la reunión del 18-oct, un instructivo que Mario y Chalo puedan seguir solos para capturar las tres fuentes, con scripts que no dependan de fechas ni nombres de archivo fijos.

## Qué se hizo
- Guía única `guias/05-captura-meta-google-ads-mercadolibre.md`, con indicaciones generales que cualquiera de los tres puede ejecutar (sin tareas por persona, a pedido de Boris): preparación (Python, terminal, Google Sheets), Meta, Google Ads, Mercado Libre (API y manual), cierre y problemas frecuentes.
- Tres scripts nuevos, solo con la biblioteca estándar de Python (no hay que instalar nada):
  - `scripts/preparar_captura.py`: crea los CSV del día con el nombre correcto (Mercado Libre: uno por término; Meta: una fila por palabra clave) y muestra los enlaces de búsqueda. No navega ningún sitio y nunca sobrescribe.
  - `scripts/resumir_meta_ads.py`: resume la captura de Meta por palabra clave y por anunciante, compara con la captura anterior (variación y anunciantes nuevos) y avisa totales o fechas faltantes.
  - `scripts/procesar_google_ads.py`: limpia cualquier descarga del planificador (inglés o español, UTF-16 o CSV), une varias, quita duplicados y marca los términos que no están en el diccionario. Detecta y descarta la descarga de *Previsiones* (clics estimados), que no trae volúmenes.
- `.env.ejemplo` (lo pedía `scripts/mercadolibre_api.ps1` y no existía).
- Pruebas en una copia fuera del repositorio: `procesar_google_ads.py` con las descargas del 16-oct (1.657 términos únicos; `2026-10-16_google-ads_keywords-planner.csv` resultó ser una descarga de Previsiones), `resumir_meta_ads.py` con dos capturas de prueba (números "~2.800" y "3,1 mil", fechas "12 dic 2025" y "12-12-2025"), y `resumir_captura_mercadolibre.py resumir 2026-10-16` sigue funcionando. Ningún archivo de prueba quedó en el repositorio.

## Hallazgos
- La captura de Mercado Libre del 16-oct se hizo con un script en la consola del navegador (bitácora 2026-10-16_1752). La guía nueva lo deja como captura manual, coherente con `datos/referencia/terminos-de-uso-por-sitio.md` (secc. 7.6 de los términos para desarrolladores).
- Excel en configuración chilena guarda CSV con `;`: `resumir_captura_mercadolibre.py` lee solo comas. La guía recomienda Google Sheets; `resumir_meta_ads.py` acepta ambos.

## Archivos creados o modificados
- `guias/05-captura-meta-google-ads-mercadolibre.md` — instructivo para el equipo.
- `scripts/preparar_captura.py`, `scripts/resumir_meta_ads.py`, `scripts/procesar_google_ads.py` — scripts nuevos.
- `.env.ejemplo` — plantilla de claves de la API de Mercado Libre (sin claves).

## Decisiones propuestas (para acordar en grupo)
- Meta pasa a formato largo (una fila por palabra clave y anunciante) en `AAAA-MM-DD_meta-ads-library_cl_captura.csv`, para comparar semana a semana.
- Desde ahora, Mercado Libre solo por API oficial o captura manual (sin script de consola).
- Cada persona que corra la API de Mercado Libre crea su propia aplicación; las claves no se comparten.

## Pendientes y siguiente paso
- [ ] Probar la guía con Mario y Chalo en la reunión y anotar lo que no se entienda — Boris.
- [ ] Primera captura de Meta en el formato nuevo (la del 12-oct quedó en formato antiguo) — Boris.
- [ ] Corregir `datos/referencia/pauta-captura-mercadolibre.md` y el comentario de `resumir_captura_mercadolibre.py` ("función de consola") cuando Mario cierre la revisión de términos — Mario.
- [ ] Agregar la guía 05 a la tabla de `README.md` en la próxima integración.

## Contexto para la próxima sesión
Todos los comandos se corren desde la raíz del repositorio. Flujo: `preparar_captura.py meta|mercadolibre` → captura a mano → `resumir_meta_ads.py` / `resumir_captura_mercadolibre.py resumir <fecha>`; Google Ads: descarga en *Métricas históricas* → `datos/crudos/AAAA-MM-DD_google-ads_keyword-planner.csv` → `procesar_google_ads.py`. En paralelo hubo otra sesión de Boris sobre el dashboard de inversión (`bitacora/2026-10-18_2040_boris_actualizacion-dashboard-inversion.md`); sus archivos no se incluyeron en este commit.
