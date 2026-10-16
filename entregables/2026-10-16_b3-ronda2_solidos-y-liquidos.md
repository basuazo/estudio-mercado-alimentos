# B3 ronda 2: categorías con señal en Trends, sólidos y líquidos

**Autor:** Boris (con Claude) · **Captura:** 2026-10-16 · **Estado:** primera pasada, para discutir en la próxima reunión. Sigue a `entregables/2026-10-16_b3_barras-mercadona-tesco.md`.
**Datos:** `datos/limpios/2026-10-16_b3_ronda2_productos.csv` (65 filas, con una columna `verificacion`).

## Cómo se hizo y cuánto confiar

- Se eligieron 10 categorías con señal en A1 (Trends 12 y 13-oct), 7 de ellas líquidas: yogur griego y proteico, bebidas lácteas proteicas, avena barista, café frío y matcha, jugos prensados en frío y shots, agua con gas saborizada, electrolitos y agua de coco, granola y clusters, tortitas y snacks de legumbres, más tés helados sin azúcar como señal débil.
- La búsqueda la hicieron cuatro agentes en paralelo (España/Mercadona, Reino Unido/Tesco y Chile). **Yo revisé contra la fuente las afirmaciones que sostienen las conclusiones**: el batido de café de Mercadona, el snack de lentejas, la oferta de electrolitos en Falabella, los snacks de legumbres en Jumbo, la gama proteica líquida de Soprole, la granola Wild Protein y los umbrales de sellos para líquidos. El resto del CSV queda marcado "reportado por subagente; no verificado".
- **Mercadona.es, Tesco y Mercado Libre no se pueden leer con la herramienta.** Afuera se usó prensa, Open Food Facts y fichas sueltas. En Chile, cada búsqueda mostró solo la primera página de resultados, así que los conteos de marcas y SKU son un piso. Falabella, Líder y Jumbo no muestran los sellos por producto en el texto.
- Ninguna categoría cumple todavía el criterio de 3 fuentes independientes: tienen Trends y B3, falta Google Ads (Mario), góndola y entrevistas.

## Cuadro resumen

Clasificación B3 para Chile. "Por qué" resume la evidencia; el detalle está más abajo.

| Categoría | Tipo | Demanda (Trends Chile) | Chile hoy (B3) | Sellos y regulación | Lectura |
| --- | --- | --- | --- | --- | --- |
| Sobres y tabletas de electrolitos | Líquido (polvo para disolver) | electrolitos +13 %; "sobres de electrolitos" +450 % en consultas (el Mundial 2026 infla "hidratación") | **Existe con poca oferta**: en Falabella 37 resultados, casi todo Amazing Care (17 de 28 SKU vistos), más Happyflow, Powerbar, Simply y Strive; $700 a $3.000 por porción | Probable suplemento alimentario (fuente de consultora, sin confirmar): rótulo, SEREMI y CDA si se importa | **Candidata 1** |
| Café o batido proteico listo para beber (20–30 g) | Líquido | proteína +3 % (últ. trimestre +22 %); whey +21 %; "bebida proteica" sin volumen | **No encontrado** con 20–30 g. Sí hay leche proteica saturada (13 productos de Soprole en Líder) y café proteico solo en polvo | Hacendado: 153 kcal en 330 ml ≈ 46 kcal/100 ml, bajo el umbral de 70; estimo que no llevaría sello (faltan sodio y saturadas) | **Candidata 2**, con duda de fabricación (lácteo UHT) |
| Cold brew y café frío sin leche | Líquido | cold brew +183 % desde base baja | **Existe importado caro**: La Colombe ≈ $21.000/L; el café frío local es con leche y azúcar, de $7.500 a $11.200/L (Nescafé, Marley, Starbucks) | Sin azúcar y sin leche, bajo en calorías: favorable | **Candidata 3** |
| Avena barista para cafeterías | Líquido | leche de avena +43 %; "barista" +300 % en consultas | **Saturado en retail**: 5 marcas barista en Jumbo (OraSì, NotCo, Naveia, Natrue, Vilay), $2.850–4.490/L. Foodservice no verificado | Sin sellos probables | Solo si el canal cafeterías tiene hueco de precio |
| Jugos prensados en frío y shots | Líquido | jugo natural +28 %; "jugo prensado en frío" y shots sin volumen | **Existe con poca oferta**: 2 marcas (Bless, Zuma), ~14 SKU, sin shots | Los jugos 100 % fruta superan 5 g de azúcares/100 ml: Tesco shot 7,5 g, naranja 10 g → **ALTO EN azúcares probable**. Cadena de frío y HPP sin verificar | Calza con la idea del banco de ideas (inversionista), pero el sello es el problema |
| Snack horneado de lentejas o garbanzo | Sólido | legumbres 0 %, hummus +4 %, "chips de garbanzo" sin datos | **Poca oferta**: en Jumbo solo 3 SKU (Nutripop, edamame Lowcarb); en Líder y Falabella no apareció | Hacendado: 413 kcal/100 g → **ALTO EN calorías** (supera 275) | Hueco real pero con sello y demanda débil |
| Agua con gas saborizada sin azúcar | Líquido | agua con gas +47 %; saborizada +189 % desde base baja | Sin gas, **saturado** (Jumbo: 105 resultados); con gas y sin azúcar, poca oferta (Sofruco en lata, Más) | Sin sello (0,1–0,2 g de azúcares) | Embotellar exige capital y compite con Cachantun y Benedictino: no es "simple" |
| Yogur griego y proteico | Semisólido | yogurt griego +70 %, el más fuerte | **Saturado** individual (52 resultados en Líder y 5+ marcas, según el agente; no verificado). Formato familiar ≥ 500 g sin azúcar: poca oferta, pero solo leí 7 de 32 resultados | Lácteo con resolución sanitaria y grandes jugadores | Baja prioridad |
| Leche proteica | Líquido | sin volumen propio | **Saturado** (41 resultados en Líder; Soprole, Loncoleche, Colun) | — | Descartar por ahora |
| Granola y clusters | Sólido | granola +40 %; "clusters" +300 % | **Saturado**: unas 11 marcas y 20+ SKU, ya con granolas proteicas (Wild, Tika) | Ver nota de sellos abajo | Baja prioridad |

## Lo que sale del cruce

1. **Los líquidos sin azúcar tienen una ventaja regulatoria sobre los sólidos.** Los umbrales de "ALTO EN" para líquidos son por 100 ml: 70 kcal, 5 g de azúcares, 100 mg de sodio y 3 g de grasas saturadas (Tetra Pak Chile, que además da la fecha de vigencia 27-jun-2019, y Carey, que rotula la tabla "por 100 g": hay que confirmar la unidad en el decreto). Para sólidos son 275 kcal, 10 g de azúcares, 400 mg de sodio y 4 g de saturadas por 100 g. **Casi cualquier snack, barra o granola con frutos secos o chocolate supera 275 kcal** y lleva "ALTO EN calorías" (Hacendado lentejas: 413; Tesco granola: 421; Hacendado muesli: 407). Un electrolito, un café frío sin azúcar o un agua saborizada no llegan a esos umbrales.
2. **Los jugos son la excepción.** Un jugo 100 % fruta suele pasar los 5 g de azúcares por 100 ml, así que un jugo prensado "natural" lleva sello de azúcares. Con el piloto de jugos que el grupo ya tiene identificado, conviene tener claro que el producto sale con sello salvo que se diluya o se formule distinto.
3. **Hay una inconsistencia que vale la pena resolver con la etiqueta real.** Jumbo rotula como "libre de sellos" la granola Wild Protein Golden Crunchy, cuya ficha dice 346 kcal por 100 g (sobre 275). O la ficha tiene un dato errado, o hay una regla que no estamos viendo. Si existe una forma legítima de evitar el sello en un sólido calórico, cambia la lectura de granolas, barras y snacks.
4. **Lo que sube afuera es proteína en lácteo y en líquido, no en barra.** Mercadona vende una bebida proteica de café de 330 ml con 30 g de proteína a €1,40 (≈ €4,24/L), sin azúcares añadidos y con edulcorante ([Menorca.info, 16-abr-2026](https://www.menorca.info/actualidad/dudas-respuestas/2026/04/16/2608871/mercadona-arrasa-nueva-bebida-proteina-sabor-cafe-practico-envase-por-poco-mas-euro.html)). En Chile la oferta proteica líquida es leche de 1 L o 200 ml (Soprole, Loncoleche, Colun); no encontré un café proteico listo para beber, solo en polvo.
5. **Los líquidos exigen ver el costo del lado de producción.** Ninguna de las cuatro búsquedas encontró un maquilador chileno ni los requisitos sanitarios de prensados en frío o de bebidas lácteas UHT. Es el vacío más grande para decidir.

## Detalle por categoría candidata

### 1. Sobres y tabletas de electrolitos

- **Afuera:** poca evidencia. 226ERS lanzó HydraZero (efervescente, 20 tabletas y masticable, 13) en España ([Alimarket, 7-abr-2025](https://www.alimarket.es/alimentacion/noticia/406485/226ers-suma-mas-opciones-en-su-linea-de-hidratacion)); en Tesco, Wowhydrate 4 × 500 ml a £4,50 (agotado). No encontré marca propia de Mercadona ni de Tesco. Es decir, **esta categoría no se valida por Mercadona y Tesco**: la señal viene de Trends.
- **Chile, Falabella (captura 16-oct):** 37 resultados; en los 28 que leí, Amazing Care (17 SKU: 5 sticks a $4.990, 12 a $8.990 y 30 a $20.990, o ≈ $700–750 por stick), Happyflow (9 o 18 sachets a $14.990–24.990, ≈ $1.390–1.670 por sachet), Powerbar (10 tabletas a $29.990, ≈ $3.000 por tableta), Simply (350 g, $34.990) y Strive. Para comparar, una isotónica lista de 1 L cuesta $1.250–1.950 en Líder (Gatorade, Powerade Zero, Suerox, Electrolit).
- **Hueco posible:** un sobre de electrolitos a menor precio por porción que Happyflow, o una versión sin azúcar con sodio y potasio claros. Falta mirar farmacias, Jumbo y Mercado Libre.
- **Regulación (no oficial):** una consultora (Artixio, ago-2026) indica que los sobres se rotulan como "Suplemento Alimentario" bajo el DS 977/96 (arts. 534–538), con advertencia para menores de 8 años, embarazadas y lactantes, y que al importar se pide CDA y autorización de la SEREMI. Confirmar con el Minsal o un asesor.

### 2. Café o batido proteico listo para beber

- **Afuera (verificado):** Hacendado, 330 ml, €1,40, 30 g de proteína, 153 kcal y 6,6 g de hidratos; "sin azúcares añadidos", con edulcorante sin nombrar.
- **Chile (verificado en Líder):** la gama proteica líquida de Soprole son 13 productos (1 L a $2.750–2.990, 200 ml a $590, cultivadas y Protein+ Power), pero **la página no muestra los gramos de proteína**; no puedo confirmar que ninguno llegue a 20–30 g por porción. El único café proteico visto en Jumbo es Revitta Coffit en polvo (300 g, $12.790–15.650). Hay que mirar la tabla nutricional de Soprole Protein+ Power y de las otras antes de afirmar un hueco.
- **Hueco posible:** formato individual listo para beber, 250–330 ml, con proteína alta y poca azúcar. Riesgo: es un producto lácteo procesado (UHT o ESL); no se sabe si hay maquilador accesible.

### 3. Cold brew y café frío sin leche

- **Afuera:** Kenco lanzó en mayo de 2026 un Espresso Concentrate (£5) y un Matcha Latte (£2,99) en Tesco, Asda y Sainsbury's ([Grocery Gazette, 11-may-2026](https://www.grocerygazette.co.uk/2026/05/11/kenco-unveils-matcha-latte-and-espresso-concentrate/)).
- **Chile (Jumbo y Líder):** solo 2 de 10 resultados de "cold brew" son cold brew de verdad. El café frío de supermercado es con leche: Nescafé $7.460/L, Marley $7.560–8.360/L, Starbucks $11.180/L. El cold brew negro sin azúcar es importado (La Colombe, 12 × 325 ml a $81.990, ≈ $21.000/L). Matcha listo para beber: no encontrado en Jumbo (solo polvo y sobres).
- **Hueco posible:** cold brew local, sin azúcar, en botella o concentrado. Falta Falabella, Líder en profundidad y Mercado Libre, y el costo de producir con vida útil suficiente.

### 4. Avena barista: el hueco, si existe, está en el canal

Retail saturado (5 marcas barista en Jumbo, 6 SKU). No se verificó oferta de 1 L en canal mayorista a cafeterías ni los precios por caja que paga una cafetería. Se puede cubrir con una llamada a 5 cafés y a un distribuidor: es más barato que seguir buscando en la web.

### 5. Snack horneado de lentejas

Hacendado lo lanzó en febrero de 2026: unos 100 g a €1,25, 4,2 g de fibra y 413 kcal por 100 g, horneado, "rico en proteínas" sin cifra ([The Objective, 21-feb-2026](https://theobjective.com/economia/consumo/2026-02-21/juan-roig-lo-vuelve-a-hacer-mercadona-lanza-un-nuevo-aperitivo-viral-de-lentejas-rico-en-proteinas-y-por-menos-de-dos-euros/)). En Chile, Jumbo muestra tres productos de legumbre (garbanzos Nutripop, 20 g a $1.050; edamame Lowcarb, 113 g a $5.990); Líder y Falabella no mostraron ninguno. **Con 413 kcal/100 g llevaría ALTO EN calorías**, lo que complica un posicionamiento saludable.

## Qué descartar o dejar en pausa

- **Barras proteicas, granola, yogur individual y leche proteica:** ya hay oferta amplia en Chile; el hueco sería precio o formato, no categoría.
- **Aguas saborizadas sin gas y bebidas isotónicas listas:** saturadas.
- **Tés helados sin azúcar:** señal solo en Mercadona 2026; en Chile no se investigó. Queda como "por investigar" si el grupo lo pide.

## Pendientes para cerrar esta ronda

1. Leer las tablas nutricionales de Soprole Protein+ Power y de las leches proteicas (gramos por porción) y buscar café proteico RTD en Mercado Libre, Paris y Unimarc.
2. Resolver por qué la granola Wild Protein de 346 kcal/100 g se rotula "libre de sellos" (revisar etiqueta física o consultar al Minsal).
3. Mirar electrolitos en farmacias, Jumbo y Mercado Libre y confirmar con una fuente oficial cómo se clasifican y qué exige el Minsal.
4. Llamar a 5 cafeterías y a un distribuidor para avena barista en 1 L.
5. Maquiladores: ninguno verificado en líquidos. Es el dato que falta para puntuar "facilidad de producción" y "margen" en la matriz; sin él no puntúo.
6. Google Ads (Mario): volumen absoluto de "electrolitos", "sobres de electrolitos", "cold brew", "leche de avena barista" y "bebida proteica".

## Matriz de puntaje

No la completé: de los seis criterios (demanda, hueco, margen, producción, regulación, canal) tengo evidencia razonable de tres. Margen y facilidad de producción no tienen datos de costo; puntuarlos ahora sería inventar. Con los pendientes de arriba se puede cerrar en una sesión.
