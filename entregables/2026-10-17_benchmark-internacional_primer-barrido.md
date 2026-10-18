# Benchmark internacional: primer barrido de marcas e informes (Enfoque B)

**Autor:** Boris (con Claude) · **Captura:** 2026-10-17 · **Estado:** primer barrido, para discutir el 28-oct. No reemplaza la etnografía ni los costos de maquila.
**Datos (base central del benchmark), en `datos/limpios/`:**

| Archivo | Filas | Qué tiene |
|---|---|---|
| `2026-10-17_benchmark-internacional_senal-por-oportunidad.csv` | 23 | Una fila por oportunidad del radar: etapa global, dirección de la señal, barrera, presencia en Chile, precio de referencia y filas de respaldo |
| `2026-10-17_benchmark-internacional_marcas.csv` | 167 | Casos de marca: hitos, cifras, precio, lección para Chile, fuente, cita y verificación |
| `2026-10-17_benchmark-internacional_mercado.csv` | 110 | Tamaño, crecimiento, participación y precio por categoría y país |
| `2026-10-17_benchmark-internacional_informes.csv` | 78 | Informes de consultoras, gremios, empresas y academia, con tipo de acceso |
| `2026-10-17_benchmark-internacional_notas-categoria.csv` | 42 | Lectura por categoría y por tema transversal |

Cada fila tiene `id` (por ejemplo `A-mar-05`), URL, fecha de la fuente y cita textual. La columna `confiabilidad_fuente` marca como **baja** las firmas genéricas de *market research* (Mordor, Grand View, Precedence y similares) y los newsletters.

## Cómo leer esto (límites)

- **Lo que mide:** cómo le va a la categoría **afuera** (etapa, quién gana, a qué precio, qué formato). No mide demanda en Chile. Cuenta para la familia "Benchmark internacional" de la auditoría solo cuando la dirección es favorable.
- **Verificación:** seis subagentes declararon haber leído la página de casi todas las filas (276 de 277). Como control independiente se volvieron a abrir 9 fuentes de cifras centrales (marca propia en Chile, Vita Coco, polvos de hidratación, sueros en México, Kombuchacha, cold brew, Oatly, tortitas de Mercadona) y **las 9 cuadraron**. Una diferencia: la fuente de los polvos de hidratación confirma USD 1.500 M y "dos dígitos durante cuatro años", pero el 20 % exacto no apareció en el texto releído. Las filas de esos controles están marcadas en `control_cruzado`. Cerca de un tercio de las citas de lácteos son paráfrasis cercanas, no textuales.
- **Cobertura despareja:** el cupo de búsquedas web se agotó a mitad del trabajo. Quedaron débiles: presencia en Chile de bebidas (agua con gas, jugos, tofu, chai, té), fruta y comida liofilizada, y Rabobank, BCG, PwC, EY, Kantar Brand Footprint y Anuga.
- **Sesgo:** casi todas las cifras son de EE. UU. y Europa. LatAm aparece en electrolitos (México), yogur (México), proteína y energéticas (Brasil y Perú), y sellos (México).

## Conclusión corta

1. **Cinco oportunidades del radar tienen señal internacional favorable y respaldo de alta confianza:** electrolitos en sobre, cold brew, yogur griego en formato familiar, agua de coco y "sin sellos" como criterio de diseño. Café o batido proteico y matcha también son favorables en demanda, pero con barrera alta (maquila aséptica) o costo de materia prima en alza (matcha).
2. **Seis quedan con señal neutral o desfavorable para un entrante chico:** granola, leche sin lactosa, té helado sin azúcar, agua con gas saborizada, creatina en gomitas y avena barista. No es que no crezcan afuera: o ya están cubiertas en Chile, o son productos de precio dominados por embotelladoras y marca propia.
3. **El modelo de negocio que más se repite entre los casos que funcionan con poco capital es "marca + maquila o importación"** (Vita Coco sin plantas, Score maquilada en Europa, LMNT con ~USD 6 M levantados, Colo Coffee enlatado por terceros). El segundo modelo es **maquilar para la marca propia de un supermercado** (tortitas de Mercadona hechas por Cerealto; Sow Good terminó ahí).
4. **La marca propia en Chile es baja:** 13,4 % del supermercado (NIQ, 1er semestre 2026) contra 40 % en Europa y 23,5 % de las unidades en EE. UU. El 56 % de los consumidores compraría más con más variedad. Es una vía de entrada que el estudio no ha mirado.
5. **Tres alertas para la matriz:** (a) el café arábica subió más de 80 % en 2024 y el matcha (tencha) hasta 265 % en 2025, lo que aprieta el margen de cold brew y matcha; (b) las modas se copian rápido (Sow Good cayó 88 % en un año cuando entraron los grandes); (c) lo vegetal procesado está en retirada (Beyond -15,6 %; NotCo vendió Brasil, Argentina y Uruguay).

## Señal por oportunidad del radar

| Oportunidad | Etapa afuera | Señal | Barrera para un entrante chico | Lo que pesa |
|---|---|---|---|---|
| Sobres de electrolitos | Crecimiento | **Favorable** | Media | Polvos de hidratación en EE. UU. USD 1.500 M (Circana); Liquid I.V. rumbo a USD 1.000 M; LMNT >USD 200 M con poco capital (cifra de newsletter); México 9.048 M MXN, Electrolit 45 %. Precio afuera USD 1,0-1,5 por porción, en línea con los ~970 CLP por porción de Mercado Libre |
| Cold brew sin azúcar | Crecimiento | **Favorable** | Media | Cold brew +16 % con el café listo para beber total en -2 % (Circana 2025); La Colombe ×3. En Chile, La Colombe importada a ~21.000 CLP/L y Nescafé en lata vía CCU |
| Yogur griego familiar | Crecimiento | **Favorable** | Alta (socio lácteo) | Chobani USD 3.800 M (+29 %); cottage +20 %; México lanza 700-900 g. En Jumbo solo se vio un formato familiar (Quillayes 800 g) |
| Agua de coco | Crecimiento | **Favorable** | Media | Vita Coco USD 610 M (+18 %), margen bruto 37 %, todo maquilado. En Chile, Samui importada a ~3.000-3.700 CLP/L |
| Café o batido proteico | Crecimiento | Favorable en demanda | **Alta** | BellRing USD 2.316 M (+16 %); fairlife limitado por capacidad; Mercadona fija el piso en EUR 1,40 por 330 ml con 30 g. Maquila aséptica escasa |
| Matcha listo para beber | Crecimiento | Favorable con riesgo | Media-alta | Exportaciones japonesas récord; tencha +265 %; el listo para beber llega después del polvo |
| Shots funcionales | Crecimiento | Favorable (solo shots) | Media | Shots en Reino Unido £100 M (+47 %); el jugo prensado de tienda está en declive |
| Pan de masa madre | Crecimiento | Favorable | Media-alta | +30 % en EE. UU. con el pan plano; fuera del foco de envasados |
| Tofu simple | Mixta | Favorable para tofu | Media | El tofu crece y los análogos caen |
| Chai, ginger beer, kimchi, snack de legumbres, agua con gas | Madura o nicho | Neutral | Media-alta | Ver CSV |
| Avena barista | Madura | Neutral a desfavorable | Media | Retail -2 %; foodservice +16 %; Oatly perdió su mayor cliente de cafetería |
| Granola, leche sin lactosa, té helado sin azúcar, creatina en gomitas | Madura o cubierta | **Desfavorable** | Alta | Atributo ya cubierto en Chile, producto de precio o problema de calidad |
| Fruta y comida liofilizada | — | Sin datos suficientes | Alta | Barrido incompleto |

## Lo que dicen las consultoras (transversal)

- **Proteína es la tendencia #1** (Innova 2026). En Alemania los lácteos con proteína crecen 21,5 % contra 2,2 % del resto y cobran ~40 % más (NIQ, 2026). Pero ya es "lo mínimo esperado" y Mintel prevé que pierda fuerza hacia 2030.
- **Fibra y salud intestinal son la #2** (59 % la considera clave, Innova). La soda prebiótica ya maduró en EE. UU.
- **Hidratación funcional:** los lanzamientos con declaración de hidratación crecen 18 % anual compuesto (Innova). Apoya a electrolitos y agua de coco.
- **GLP-1 pesa en EE. UU., no todavía en Chile:** 23 % de los hogares de EE. UU. tiene un usuario (Circana), pero en Europa es menos de 1 % de los ingresos del supermercado (McKinsey).
- **Precio manda:** 47 % de los consumidores busca valor (Deloitte); en EE. UU. se proyecta crecimiento de 2-4 % solo por precio y mezcla (Circana). En Chile, el volumen de consumo masivo apenas subió 0,7 % (Worldpanel, MAT junio 2025) tras caer 2,9 % el año anterior.
- **Salidas:** las marcas insurgentes se vendieron a ~3 veces ventas (Simple Mills USD 795 M con USD 240 M de ventas) o más (Poppi, Alani Nu), pero con más de USD 200 M de ventas. Para un emprendimiento chileno, la salida realista es un grupo local o regional a múltiplos menores (ejemplo: Kunstmann compró 25 % de Kombuchacha).

## Chile y Latinoamérica: casos que sirven de referencia

- **Score (energéticas):** marca chilena maquilada en Austria y Polonia, ~100 millones de latas al año a ~1.290 CLP. Es la prueba local de que "marca + maquila afuera" escala. Chile es el mayor consumidor de energéticas de la región (~6 L por persona al año). **Las energéticas no están en el radar**; se anotan como observación.
- **Wild Foods:** USD 10 M de ventas en 2021, levantó USD 25 M en 2024 y entró a México. Fija el techo de precio en granola proteica (~19.300 CLP/kg).
- **Kombuchacha:** partió con 20 millones de pesos, tiene 64 % de la kombucha en Chile, produce más de 500.000 litros y Kunstmann tiene 25 %. Muestra un mercado chico dominado por un actor.
- **NotCo:** de ~USD 100 M (2022) a ~USD 65-70 M (2025), y salida de Brasil, Argentina, Uruguay y México. Es la advertencia del vegetal procesado.
- **Electrolit (México):** de suero de farmacia a USD 400-500 M en EE. UU. con planta propia. El respaldo farmacéutico es parte del producto, y en México enfrenta un posible IEPS.
- **Ley 20.606:** los productos con algún sello bajaron de 70,8 % a 52,5 %, y los sin sello subieron 5,5 % su precio relativo. Diseñar sin sellos tiene valor comercial medible.

## Decisiones propuestas (para el 28-oct)

1. Sumar a la matriz una columna "señal internacional" con la dirección de `senal-por-oportunidad.csv` (favorable / neutral / desfavorable), separada de la demanda en Chile.
2. Bajar de prioridad granola, leche sin lactosa, té helado sin azúcar y creatina en gomitas, salvo que la etnografía muestre algo distinto.
3. Evaluar **agua de coco** como candidata: tiene señal favorable, modelo de importación con marca y oferta chilena cara. Hoy está en radar con 2 familias.
4. Agregar a la matriz el modelo de entrada (marca propia con maquila / importación con marca / maquila para marca propia de supermercado), porque cambia capital y margen.
5. Anotar el riesgo de materia prima (café, matcha) en el criterio de margen.

## Pendientes del benchmark

- Segunda pasada con cupo de búsqueda fresco: presencia en Chile de agua con gas, jugos y shots, tofu, chai y té; fruta y comida liofilizada; Rabobank, BCG, Kantar Brand Footprint y Anuga.
- Costos de trámite: plazos y costo de resolución sanitaria, registro de suplementos en ISP y aranceles por TLC (hoy solo como conocimiento general no verificado).
- Precios de las candidatas favorables en Jumbo y Líder (parte de la captura manual del 27-oct).
- Leer completos los informes gratuitos más útiles: McKinsey *State of Grocery Europe 2026*, Bain *US Insurgent Brands 2026*, NIQ *Fiber*, Innova *Top Ten Trends 2026* y Worldpanel Chile.
