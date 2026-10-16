---
fecha: 2026-10-16 17:52
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: A3 Oferta y precios (captura Mercado Libre) · revisión general y plan actualizado
estado: completado
---

# Captura de Mercado Libre, revisión general y plan actualizado al 11-nov

## Objetivo
Procesar la captura de publicaciones de Mercado Libre, revisar todo lo hecho en el estudio y actualizar el plan hasta la lista corta.

## Qué se hizo
- Boris capturó 434 publicaciones en 7 términos (electrolitos sobres, bebida hidratante en polvo, bebida proteica café, proteína lista para beber, cold brew, chai latte, comida liofilizada). **Forma de captura:** navegó cada página de resultados y extrajo lo visible con un script en la consola del navegador. Trae título, precio, envío y URL; no trae marca, formato, vendidos ni reputación.
- `scripts/resumir_captura_mercadolibre.py` mejorado: saca el formato del título, marca cada publicación como relevante o no según el término (descarta cafeteras, licores, cápsulas, etc.) y toma el término del nombre del archivo.
- Radar actualizado con lo que mostró la captura.
- **Plan actualizado**: nueva sección "Actualización al 2026-10-16" en `plan/plan-estudio-mercado-alimentos.md` con avance por enfoque, estado de las candidatas, tareas por persona hasta el 28-oct y pasos de la Fase 2.
- `CONTEXTO.md`: fase y "Dónde estamos" al día.

## Hallazgos
Fuente: `datos/limpios/2026-10-16_mercadolibre_cl_resumen.csv` y `..._captura.csv` (captura del 2026-10-16; precios publicados, no ventas).
- **Electrolitos:** dos niveles de precio por porción. Masivo de 450 a 1.000 CLP (Amazing Care, Extra Life, Fuel Nutrition, Go!, Purihydra, Irio, Suerox) y premium importado de 2.000 a 6.700 CLP (LMNT, Zalt y otros). Hay marcas locales con ángulo "natural" (Chispa Hidratante, 1.333 CLP; Fisiobiss con maqui). El 66 % de las publicaciones de "electrolitos sobres" ofrece envío gratis.
- **Café proteico listo para beber:** casi toda la oferta "proteína sabor café" es en polvo (Coffit Protein, Winkler, ISO Whey). Listos para beber con café solo hay 3: NotCo NotShake café caramelo 250 ml (1.590 CLP), Akapro capuccino 12×330 ml (unos 6.100 CLP/L) y Nude Shake vainilla y café 250 ml (2.790 CLP). El hueco existe pero es más chico de lo que parecía.
- **Cold brew:** hay un competidor local, **Briu** (concentrado 1 L a 13.990 CLP; listo para tomar 1 L a 11.490 CLP; 12×250 ml a unos 9.500 CLP/L). El resto es importado y caro (19.000 a 140.000 CLP/L).
- **Chai latte:** mediana de 35.600 CLP/kg, con rango muy amplio (polvos importados y fraccionados).
- **Comida liofilizada:** la búsqueda trae sobre todo fruta liofilizada (80.000 a 950.000 CLP/kg); comidas de montaña, pocas.
- **Revisión general:** la brecha más grande del estudio es la **etnografía (enfoque C), que no ha partido**. Tampoco hay captura de supermercados, Google Ads ni costos de maquila, que la matriz de puntaje necesita.

## Archivos creados o modificados
- `datos/crudos/2026-10-16_mercadolibre_cl_*.csv` (7 archivos) — captura de Boris.
- `datos/limpios/2026-10-16_mercadolibre_cl_captura.csv` y `..._resumen.csv`.
- `scripts/resumir_captura_mercadolibre.py` — formato desde el título y relevancia.
- `datos/limpios/2026-10-16_radar-oportunidades_boris.csv` — señales de la captura.
- `plan/plan-estudio-mercado-alimentos.md` — sección "Actualización al 2026-10-16".
- `CONTEXTO.md` — fase 1 y "Dónde estamos".
- `estado/boris.md`.

## Decisiones propuestas (para acordar en grupo)
- Aprobar el plan hasta el 11-nov y sus responsables (reunión del miércoles 21 o 28-oct).
- Validar la forma de captura en Mercado Libre: el script de consola no recorre el sitio, pero es extracción automatizada y los términos para desarrolladores (secc. 7.6) prohíben "scraping or other technology". Mientras Mario lo revisa: volumen bajo, solo uso interno y sin publicar precios promedio.
- Priorizar la etnografía mínima antes del 28-oct.

## Pendientes y siguiente paso
- [ ] Mario: validar la forma de captura en Mercado Libre y términos de uso (21-oct); Google Ads (23-oct).
- [ ] Mario y Chalo: captura en Jumbo y Líder de las 5 candidatas (27-oct).
- [ ] Los tres: etnografía mínima (cafeterías, farmacias, minimarkets) (28-oct).
- [ ] Boris: netnografía de 50 reseñas y prueba de NotShake, Akapro, Nude y Briu (27-oct); segunda corrida de la API (23-oct).
- [ ] Chalo: maquiladores y Aduanas (28-oct).

## Contexto para la próxima sesión
El plan vigente está en la sección "Actualización al 2026-10-16" del plan. Para procesar una captura nueva: archivos `datos/crudos/AAAA-MM-DD_mercadolibre_cl_<termino>.csv` y `python scripts/resumir_captura_mercadolibre.py AAAA-MM-DD`. Si se agrega un término nuevo, sumar su regla en `RELEVANCIA` dentro del script.
