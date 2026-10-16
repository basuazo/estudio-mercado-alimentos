---
fecha: 2026-10-16 16:53
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: B3 Método (Mercado Libre: limpieza de catálogo, radar y preparación de captura manual)
estado: completado (la captura manual queda para Boris)
---

# Catálogo de Mercado Libre limpio, radar actualizado y captura manual preparada

## Objetivo
Cerrar los pendientes de la sesión de la API: limpiar el catálogo por dominio, llevar las señales de Mercado Libre al radar y dejar lista la captura manual de precios y vendidos.

## Qué se hizo
- Script `scripts/limpiar_catalogo_mercadolibre.py`: clasifica cada ficha del catálogo como **objetivo**, **adyacente** o **ruido** según la búsqueda que la trajo (reglas por búsqueda, editables), infiere el formato (polvo, sobres, líquido, cápsulas) y el país de registro del GTIN. Reproducible cada semana después de `mercadolibre_api.ps1`.
- Radar actualizado con una columna nueva `senal_mercadolibre` y `fecha_actualizacion`; 10 oportunidades con señal nueva y 6 oportunidades agregadas.
- Script `scripts/resumir_captura_mercadolibre.py`: toma los CSV de la captura manual y calcula precio por litro, kilo o porción, marcas, vendedores, tiendas oficiales y los más vendidos por término. Probado con datos de ejemplo fuera del repositorio.
- Guía `guias/03-captura-manual-mercadolibre.md`: hoja de trabajo con enlaces, orden y cómo escribir cada campo.
- README: filas de `scripts/` y `guias/` actualizadas.

## Hallazgos
Fuente: `datos/limpios/2026-10-16_mercadolibre-api_catalogo_resumen.csv` y `datos/crudos/2026-10-16_mercadolibre-api_tendencias.csv` (captura del 2026-10-16). El catálogo mide oferta en fichas, no ventas.
- **Electrolitos:** "electrolitos sobres" con 29 de 30 fichas útiles y 16 marcas, sobre todo de farmacia (Suma, Hydrasor, Sesen, Apotex) y con GTIN de México. Sumado a la señal de tendencias (9 de 17 palabras en Isotónicas), es la **tercera fuente independiente** → cumple el criterio de lista corta.
- **Café o batido proteico listo para beber:** solo 4 de 30 fichas son sabor café y listas para beber (Emana, Optimum Nutrition, Mu, SlimFast), todas importadas. En tendencias, la proteína lista para beber ya la buscan por marcas grandes (Loncoleche, Milo). Tercera fuente → lista corta, con el riesgo de competir con lácteas grandes.
- **Cold brew:** no está en el Top 50; solo 4 de 30 fichas son café cold brew listo (el resto licores, cafeteras, tés). Poca oferta, sin señal de demanda en la plataforma.
- **Matcha:** "matcha" es #2 en Infusiones, pero solo 1 de 30 fichas es líquida (concentrado Tazo): la demanda es de polvo. Sube a 3 fuentes pero sigue candidata hasta tener señal del formato listo para beber.
- **Avena barista:** oatly #3 y not milk #20 en Bebidas; 10 de 30 fichas útiles, 8 marcas casi todas importadas. Señal de consumo final, no del canal cafeterías → sigue candidata.
- **Snack de lentejas:** 0 de 30 fichas son snacks (todas lentejas a granel). **Jugo prensado en frío:** 3 de 30 son jugos; el resto extractoras.
- **Nuevas en el radar (1 fuente):** chai latte (4 palabras en Infusiones, 23 marcas importadas en polvo), comida liofilizada de montaña (2 categorías, solo 4 marcas), fruta liofilizada como snack (conecta con fruta de Ñuble), ginger beer, agua de coco y la compra "por mayor" en línea como canal (27 palabras "por mayor", útil para Mayorístico).
- Ruido de la API: 81 de 360 fichas (22 %) no son alimentos (toallas "color matcha", licores "cold brew", extractoras). Por eso conviene leer siempre el resumen limpio y no el crudo.

## Archivos creados o modificados
- `scripts/limpiar_catalogo_mercadolibre.py` — limpieza y clasificación del catálogo.
- `scripts/resumir_captura_mercadolibre.py` — resumen de la captura manual.
- `datos/limpios/2026-10-16_mercadolibre-api_catalogo_limpio.csv` — 360 fichas clasificadas.
- `datos/limpios/2026-10-16_mercadolibre-api_catalogo_resumen.csv` — una fila por búsqueda.
- `datos/limpios/2026-10-16_radar-oportunidades_boris.csv` — columnas `senal_mercadolibre` y `fecha_actualizacion`; 23 oportunidades (2 lista corta propuesta, 3 candidatas, 18 radar).
- `guias/03-captura-manual-mercadolibre.md` — hoja de trabajo de la captura.
- `README.md` — filas de `scripts/` y `guias/`.
- `.Rhistory` — sacado del control de versiones (`git rm --cached`; ya estaba en `.gitignore`, el archivo local sigue).
- `estado/boris.md` — actualizado.

## Decisiones propuestas (para acordar en grupo)
- Contar Mercado Libre (tendencias + catálogo) como **una** fuente independiente, distinta de Google Trends y del B3.
- Pasar a **lista corta**: sobres de electrolitos y café o batido proteico listo para beber (3 fuentes cada uno).
- Correr `limpiar_catalogo_mercadolibre.py` cada vez que se corra el script de la API.

## Pendientes y siguiente paso
- [ ] Boris: captura manual de las 3 candidatas con `guias/03-captura-manual-mercadolibre.md` y luego `python scripts/resumir_captura_mercadolibre.py`.
- [ ] Boris: revisar el estado de 6 oportunidades con 2 fuentes que siguen en radar (jugos, agua con gas, snack de legumbre, yogur griego, granola, leche sin lactosa): por la regla serían candidatas.
- [ ] Chalo: decidir si `PruebaGonza.txt` (archivo de prueba vacío en la raíz) se borra.
- [ ] Integración: `ESTADO.md` está en desuso desde el 13-oct; proponer borrarlo.
- [ ] Mario: términos de uso de Mercado Libre y Google Ads Keyword Planner, sumando chai latte, comida liofilizada y matcha latte a `datos/referencia/terminos-busqueda.csv`.
- [ ] Boris: correr `mercadolibre_api.ps1` y la limpieza la semana del 23-oct.

## Contexto para la próxima sesión
Los scripts en Python necesitan Python 3.9+ sin librerías externas (`python scripts/<script>.py` desde la raíz). Las reglas de clasificación del catálogo están dentro de `clasificar()`; si se agrega una búsqueda nueva al script de la API, hay que agregar su regla o quedará como `sin_regla`. Los estados del radar ("lista corta (propuesta)", "candidata", "radar") son de Boris, no decisiones del grupo.
