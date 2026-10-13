# Trends (2 años) y anuncios en Meta: primera pasada (A1 y A2)

**Autor:** Boris (con Claude) · **Captura:** 2026-10-12 · **Fuente:** [Google Trends](https://trends.google.com), Chile, todas las categorías, búsqueda web, 2024-10-06 a 2026-10-04 (semanal; se excluye la semana parcial del 11-oct).
**Dashboard:** https://claude.ai/artifact/5S6M6umJvaDBJDjrENxKKt (privado hasta compartirlo).
**Estado:** primera pasada, para discutir el 14-oct. No es concluyente por sí sola: cuenta como **una** fuente de las tres que exige el criterio de lista corta.

## Método

- 42 términos de `datos/referencia/terminos-busqueda.csv`, en cuatro grupos: atributos, barras y snacks, bebidas funcionales, granel fraccionado (más canal/ocasión).
- **Tendencia:** cada término consultado solo (escala 0–100 propia). Se compara el promedio del año 2 (oct-25 a oct-26) con el año 1 (oct-24 a oct-25), y las últimas 13 semanas (jul–oct 2026) con las primeras 13 de la serie (oct 2024–ene 2025). Ojo: son estaciones distintas, así que este segundo indicador es solo de apoyo.
- **Volumen relativo:** grupos de 5 términos con *granola* como ancla (granola = 100), promedio de las últimas 52 semanas. Sirve para ordenar tamaños, no da búsquedas absolutas (eso sale del Planificador de Google Ads que hará Mario).
- Archivos: `datos/crudos/2026-10-12_google-trends_cl_2anios_individual.csv` (series semanales), `datos/limpios/2026-10-12_google-trends_cl_2anios_resumen.csv` (indicadores), `datos/crudos/2026-10-12_google-trends_cl_2anios_consultas-en-aumento.csv`.

## Resultados

### Crecen con volumen relevante

| Término | Var. año 2 vs año 1 | Volumen (granola = 100) | Lectura |
| --- | --- | --- | --- |
| yogurt griego | **+70 %** | 65 | El crecimiento más fuerte y sostenido. En aumento: "1 litro" (+250 %), "sin azúcar" (+80 %), recetas caseras. |
| leche de avena | +43 % | 37 | Sube sostenido. "barista" +300 % → canal cafeterías. |
| granola | +40 % | 100 | Sube sostenido, con peak en ago-sep 2026. "clusters" +300 %. |
| kefir | +44 % | 237 | **Moda pasajera:** peak oct-nov 2025 y vuelta al nivel de 2024 (último trimestre vs 2024: +5 %). No tomarlo como tendencia. |
| whey protein | +21 % | 109 | Sube; impulso de marcas importadas (Ostrovit, Dymatize) y "clear whey" (+160 %). |
| galletas de arroz | +16 % | 33 | Crecimiento moderado. |
| sin azúcar | +12 % | 257 | Atributo grande y en alza; lo mueven lanzamientos de marcas (Franui, Daily, Red Bull, Nutella). |
| chía · avena · mantequilla de maní | +9 a +11 % | 211 · 590 · 70 | Crecen suave sobre base grande. Maní "en polvo" +190 %. |
| proteína | +3 % (últ. trimestre vs 2024: +22 %) | 869 | El atributo más buscado; lo empujan productos de marca: Dunkin proteína, Surlat proteína, Lean Active. |

### Estables

fibra (+1 %), quinoa (+1 %), legumbres (0 %), leche de almendras (0 %), sin gluten (−2 %), frutos secos (+4 %).

### Caen

keto (**−25 %**, últ. trimestre vs 2024: −42 %), probióticos (−28 %), vegano (−14 %), colágeno (−9 %), kombucha (−3 %, últ. trimestre vs 2024: −21 %; aún se busca "qué es", la categoría no despegó).

### Sin volumen suficiente en Trends

snack saludable, barra keto, chips de garbanzo, snack de fruta deshidratada, bebida proteica, batido de proteína, bebida isotónica, agua con gas saborizada, yogurt proteico, bebida energética natural, semillas de maravilla, tienda a granel, comida saludable delivery, colación saludable, alto en proteína. Barra de proteína (18) y barra de cereal (9) tienen volumen bajo y planos.
→ La gente **no busca por categoría genérica** ("snack saludable", "bebida proteica"): busca productos concretos o marcas. Estos términos hay que medirlos en Google Ads (volumen absoluto) y Mercado Libre (ventas), no en Trends.

## Qué sugiere para las categorías foco (por confirmar con otras fuentes)

1. **Lácteos y bebidas con proteína o sin azúcar** es la señal más fuerte: yogurt griego, whey, proteína y sin azúcar suben, y las grandes marcas (Soprole, Surlat, Dunkin) están lanzando versiones proteicas. Buena noticia para la demanda; mala para la competencia. Hay que buscar el nicho (formato, canal, precio) que las grandes no cubren.
2. **Granola y bebidas vegetales para cafeterías** (avena barista) crecen sostenido y son productos simples de fabricar o fraccionar. Calzan con "productos simples con presencia comercial".
3. **Barras:** en Trends la demanda de búsqueda es baja y plana. No las descarta (se compran por impulso, sin buscarlas), pero la evidencia tendrá que venir de góndola, Mercado Libre y Meta.
4. **Evitar apostar por keto, vegano, kombucha y probióticos** como eje: están cayendo.

## Advertencias

- Trends entrega índices relativos, no búsquedas absolutas.
- Los términos de bajo volumen muestran valores distintos de cero solo en las últimas 3 semanas. Es un efecto de cómo Google procesa los datos recientes, no una señal de alza.
- Algunas "consultas en aumento" son ruido: en inglés (recetas, apps) o de cosmética (colágeno Garnier, avena coloidal). Están marcadas en el CSV.
- La consulta del grupo ancla se hizo en el navegador de Boris, el 2026-10-12. Si se repite otro día, los valores pueden variar algunos puntos por el muestreo de Google.

## A2. Biblioteca de anuncios de Meta (captura 2026-10-12)

**Fuente:** [Biblioteca de anuncios de Meta](https://www.facebook.com/ads/library/), país Chile, anuncios activos, todas las plataformas. 8 búsquedas por palabra clave (frase exacta, salvo granola) y búsqueda por marca. Se revisaron las primeras ~50 piezas de cada búsqueda, ordenadas por impresiones.
**Archivos:** `datos/crudos/2026-10-12_meta-ads-library_cl_busquedas.csv` (por palabra clave) y `datos/limpios/2026-10-12_meta-ads_marcas-activas.csv` (10 marcas).

### Cuánta publicidad hay por categoría

| Palabra clave | Anuncios activos (aprox.) | Lectura |
| --- | --- | --- |
| proteína | ~2.800 | Saturado, pero lo dominan apps de calorías y suplementos, no alimentos. |
| sin azúcar | ~2.300 | Atributo muy usado (Mundo Verde Pro, PediaSure, Benedictino, Nestlé). |
| granola | ~230 | Mucho ruido; marcas locales: Tika, Underfive, Oakberry (bowls). |
| mantequilla de maní | ~160 | **Competida:** Kremosa, GoNat, Allnuts, Holy Brand, NotCo. |
| yogurt griego | ~62 | **Casi sin marcas pautando**, pese a ser el término que más crece en Trends. |
| snack saludable · barra de proteína | ~27 · ~26 | Pocos anunciantes, casi todos emprendimientos. NotCo acaba de entrar a barras. |
| leche de avena | ~8 | **Sin marcas pautando**, pese a crecer +43 % en Trends. |

### 10 marcas con anuncios activos

| Marca | Qué pauta | Anuncios activos visibles | Pauta desde | Lectura |
| --- | --- | --- | --- | --- |
| Kremosa | Mantequillas de frutos secos | 51 | ene-2025 | La más constante: 20 meses pautando. |
| Feroz Snack | Charqui y chicharrones proteicos | 27 | dic-2025 | Proteína en snack salado, no barra. |
| AMA Time | Snacks y compotas de fruta (Frutipop) | 24 | may-2026 | Snack de fruta para niños. |
| GoNat | Por confirmar (aparece en mantequilla de maní) | 17 | jun-2026 | Revisar el sitio. |
| Tika Foods | Granolas y barra proteica | 10 | jul-2026 | Apunta a la colación escolar y de oficina. |
| Underfive | Granola proteica de 5 ingredientes | 10 | jul-2026 | Mensaje: pocos ingredientes y sin sellos. |
| EasyProtein | Barras de proteína | 10+ | jul-2025 | Más de un año pautando. |
| The Not Company | NotSquare, barra proteica sin azúcar | 8+ | sep-2026 | Gran actor entrando a barras. |
| B-Japi | Snacks de nutricionista emprendedora | 9 | oct-2026 | Recién partiendo. |
| Surlat (referencia) | Leche y yogurt Protein Whey | 3 | abr-2026 | Gran empresa en lácteos proteicos. |

### Cruce con Trends

- **Mensajes que se repiten:** proteína, sin azúcar, pocos ingredientes o sin sellos, y "colación" (escolar, oficina, media tarde). La **colación** aparece en Tika, Underfive y NotCo: es la ocasión de consumo que más se pauta.
- **Yogurt griego y leche de avena:** suben fuerte en búsquedas y casi nadie pauta. Puede ser un espacio libre o puede ser que estos productos se vendan en supermercado sin publicidad digital. Hay que revisar góndola (A3) antes de sacar conclusiones.
- **Granola y barras:** varias marcas pautando de forma sostenida (Tika, Underfive, EasyProtein, NotCo). Hay competencia, pero la demanda parece validada, y el formato de colación se pauta cada vez más.
- **Mantequilla de maní:** demanda que crece suave (+9 %) y competencia alta (Kremosa con 20 meses de pauta). Menos atractiva para entrar.

### Advertencias (Meta)

- La biblioteca muestra anuncios que *se ven* en Chile, incluidos los de anunciantes extranjeros. Se filtraron a mano los que parecen marcas locales de alimentos.
- Los conteos por marca son las piezas visibles en la búsqueda (con tope práctico de unas 50 por consulta). Son un piso, no el total.
- "Pauta desde" es el anuncio activo más antiguo, no la fecha en que la marca empezó a pautar.
- GoNat queda por confirmar. La búsqueda por "NotCo" no cargó; sus datos salen de la búsqueda "barra de proteína".

## Ampliación a 100 términos (2026-10-13)

Se sumaron 58 términos: 24 de bebidas y aguas (agua funcional, alcalina, con electrolitos, de coco, con colágeno, con vitaminas, mineral, con gas, bebida probiótica, matcha, cold brew, jugos, shot de jengibre, suero oral, hidratación, entre otros), snacks (frutos secos, hummus, muesli), panadería y cereales, suplementos, endulzantes y atributos (sin lactosa, fermentados, kimchi, tofu, cúrcuma, espirulina). Se reordenaron las categorías: **bebidas y aguas** (30 términos), **lácteos** (yogurt griego, kefir, leches), **suplementos** (whey, creatina, proteína en polvo, colágeno hidrolizado).
**Archivos:** `datos/referencia/terminos-busqueda.csv` (100), `datos/crudos/2026-10-13_google-trends_cl_2anios_individual_100.csv`, `datos/limpios/2026-10-13_google-trends_cl_2anios_resumen_100.csv`, `datos/limpios/2026-10-13_google-trends_cl_2anios_series-largo_100.csv`, `datos/crudos/2026-10-13_google-trends_cl_2anios_consultas-en-aumento.csv`.

**Resultado:** 56 de 100 términos tienen datos suficientes en Trends; los 44 restantes (incluidas casi todas las "aguas funcionales") se buscan muy poco o nada.

### Líquidos: qué dice Trends

| Término | Var. año 2 vs año 1 | Volumen (granola = 100) | Lectura |
| --- | --- | --- | --- |
| cold brew | +183 % | 38 | Crece fuerte, pero desde una base baja con semanas sin datos. Confirmar con Ads. |
| agua con gas | **+47 %** | 55 | El líquido con datos firmes que más crece. |
| leche de avena | +43 % | 37 | Confirma lo de ayer. |
| matcha | +29 % | 195 | Grande y creciendo; impulso de lanzamientos (KitKat matcha). |
| jugo natural | +28 % | 28 | Crece. |
| agua de coco | +18 % | 26 | Crece moderado. |
| electrolitos | +13 % | 67 | Crece; en aumento "sobres de electrolitos" (+450 %) y la marca Extra Life. |
| hidratación | +17 % | 64 | Inflado por la "pausa de hidratación" del Mundial 2026: no es tendencia de producto. |
| agua mineral | +15 % | 57 | Crece. |
| limonada · leche de almendras · kombucha | 0 a −3 % | 198 · 18 · 61 | Planos. |

**Sin volumen en Trends:** agua funcional, agua alcalina (solo dudas de "qué es"), agua con electrolitos, agua saborizada, agua con colágeno, agua con vitaminas, bebida probiótica, bebida sin azúcar, bebida vegetal, leche proteica, té helado, jugo prensado en frío, shot de jengibre, suero oral. La categoría "agua funcional" **no existe en el vocabulario del consumidor chileno**: la gente busca electrolitos, agua con gas o agua de coco, no "agua funcional". Si el grupo quiere entrar en aguas, el producto tiene que nombrarse por su beneficio concreto (hidratación con electrolitos, en sobre o lista para beber).

### Otros hallazgos de la ampliación

- **Crecen:** pan de masa madre (+42 %), kimchi (+32 %), leche sin lactosa (+24 %), tofu (+23 %), creatina (+16 %, volumen 677, "creatina en gomitas" +600 %), proteína en polvo (+17 %), pan integral (+17 %), nueces (+14 %), miel (+12 %).
- **Caen:** espirulina (−24 %), pistachos (−19 %), cúrcuma (−15 %), colágeno hidrolizado (−9 %), pan sin gluten (−7 %).
- **Formatos que aparecen en las consultas en aumento:** sobres de electrolitos, gomitas de creatina, mantequilla de maní en polvo, clear whey. El **formato** (sobre, gomita, polvo, porción individual) se repite como innovación simple.

## Próximo paso

- Cruzar con el Planificador de Google Ads (Mario) usando la misma lista de términos.
- Revisar en góndola (A3) por qué yogurt griego y leche de avena casi no tienen pauta digital.
- Repetir Meta cada semana (plan A2) para ver qué marcas sostienen la pauta.
- Repetir la captura una vez al mes (plan A1).
