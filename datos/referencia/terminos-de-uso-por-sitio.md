# Términos de uso y robots.txt por sitio: qué se puede capturar

**Paso del plan:** A3 Oferta y precios · validación de scraping (tarea de Mario) · **Revisado:** 2026-10-16 por Claude (sesión de Boris) · **Estado:** primera pasada; Mario la valida y completa lo que no se pudo abrir.
**No es asesoría legal.** Es una lectura de los textos públicos para decidir cómo capturar con bajo riesgo.

## Resumen por sitio

| Sitio | Qué dicen los términos | robots.txt | Veredicto | Cómo capturamos |
|---|---|---|---|---|
| **Mercado Libre** | Términos para desarrolladores, secc. 7.6: prohíbe *"robots, harvesters, spiders, scraping"* para acceder al contenido. Secc. 5.4: pide autorización previa para métricas derivadas como *"average prices"*. Fuente: versión en inglés de developers.mercadolibre.com.ar (se asume igual para Chile; los términos de .cl no abrieron). | No se pudo abrir. | **Prohibido expresamente** | Solo la API oficial (tendencias y catálogo) + captura manual a ritmo humano. **Ojo con la 5.4:** publicar precios promedio calculados por nosotros podría requerir permiso; para uso interno el riesgo es bajo, pero no publicarlos. |
| **Jumbo** (Cencosud) | Términos del 03-08-2026: sin cláusula sobre bots ni scraping en el texto leído (venía truncado; el PDF no abrió). | Bloquea parámetros `?map=`, `?ps=` y búsquedas vacías; no bloquea fichas de producto; permite expresamente a varios bots de IA. | **Zona gris (tolerado)** | Pocas fichas de producto por semana, a ritmo humano, sin usar búsquedas con parámetros. |
| **Santa Isabel** (Cencosud) | No se encontraron términos propios. | `Allow: /`, pero `Disallow: /api/`, `/_next/`, `/admin/`, `/private/`; `Crawl-delay: 1`. | **Zona gris** | Fichas públicas con ≥1 s entre solicitudes o captura manual; nunca `/api/`. |
| **Líder** (Walmart Chile) | Términos vigentes desde 18-08-2025: sin cláusula sobre bots. | Bloquea para todos los bots `/search*`, `/supermercado*`, `/catalogo/product*`, `/catalogo/category*`: justo lo que nos sirve. | **No automatizar** | Captura manual o muestra pequeña. |
| **Unimarc** (SMU) | No se pudo abrir. | No se pudo abrir. | **Sin información** | Captura manual hasta que Mario lo revise en el navegador. |
| **Tottus** (Falabella) | Sin términos propios; los de falabella.com (secc. 22) prohíben reproducir o copiar productos, imágenes o sonidos sin consentimiento; no mencionan bots ni precios. | Solo bloquea carro, cuenta, checkout y pedidos; publica sitemaps de productos. | **Zona gris** | Precios desde fichas del sitemap, baja frecuencia, sin guardar imágenes ni descripciones. |

## Reglas de captura para el equipo (propuesta)
1. **Mercado Libre:** API oficial o captura manual. Nada de scripts ni agentes navegando el sitio.
2. **Supermercados:** por ahora, captura manual (20–30 productos por categoría a la semana es viable a mano). Si se automatiza, solo Jumbo, Santa Isabel y Tottus, respetando robots.txt, con User-Agent honesto, pausas de ≥1 s y sin saltarse captchas ni inicios de sesión.
3. Guardar solo **precio, formato, marca y fecha**. No copiar imágenes, descripciones ni reseñas con nombre de persona.
4. Los resultados son de **uso interno**; no publicar precios promedio de Mercado Libre.

## Marco legal (resumen, con interpretación marcada)
- **Ley 21.459 (delitos informáticos), art. 2:** sanciona el acceso *"sin autorización o excediendo la autorización"* y *"superando barreras técnicas"*. *Interpretación:* leer páginas públicas sin saltarse barreras difícilmente calza; saltarse captchas o bloqueos sí podría.
- **Ley 17.336, art. 3 N°17:** protege las compilaciones por su selección o disposición, *"no abarca los datos"*. *Interpretación:* un precio aislado no está protegido; copiar la base completa o las imágenes es más riesgoso.
- **Leyes 19.628 y 21.719:** precio, formato y marca no son datos personales; aplicarían si se capturan reseñas con nombres o datos de vendedores personas naturales. (Sin revisión de fuentes en esta pasada.)
- Incumplir términos de uso es un tema contractual o civil, no penal.

## Pendiente para Mario
- [ ] Abrir a mano los términos generales de mercadolibre.cl y su robots.txt, y los términos y robots.txt de Unimarc.
- [ ] Confirmar si los términos de developers.mercadolibre.cl (Chile) son iguales a la versión leída.
- [ ] Decidir si se consulta a Mercado Libre por la secc. 5.4 (precios promedio).

## Fuentes (consultadas el 2026-10-16)
- https://developers.mercadolibre.com.ar/en_us/mercado-libre-developer-terms-and-conditions
- https://www.jumbo.cl/informaciones-legales/terminos-y-condiciones · https://www.jumbo.cl/robots.txt
- https://www.santaisabel.cl/robots.txt
- https://www.lider.cl/ayuda/articulo/terminos-y-condiciones/94565deaa82842389a0665f0706f6b8f · https://www.lider.cl/robots.txt
- https://www.tottus.cl/robots.txt · https://www.falabella.com/falabella-cl/page/terminos-condiciones-uso-falabellacom
- Ley 21.459: https://www.diariooficial.interior.gob.cl/publicaciones/2022/06/20/43283/01/2145558.pdf
- Ley 17.336: https://www.wipo.int/wipolex/en/legislation/details/18880
