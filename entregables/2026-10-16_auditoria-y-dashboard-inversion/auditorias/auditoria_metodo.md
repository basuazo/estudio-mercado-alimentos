# Auditoría metodológica: B3, radar de oportunidades y método del estudio

**Auditor:** Claude (rol de auditor metodológico senior) · **Fecha:** 2026-10-16 · **Alcance:** benchmarking B3, radar de oportunidades (23 filas), plan y método general, consistencia entre fuentes.
**Repositorio revisado (solo lectura):** `company-builder` en el equipo de Boris. Datos estructurados en `datos.json` (misma carpeta).

> Escalas usadas en este documento: confiabilidad y utilidad de 1 (muy baja) a 5 (muy alta). En la evaluación cualitativa, 1 = favorable y 5 = desfavorable en barrera, capital, complejidad y competencia; en encaje de canal, 1 = mal encaje y 5 = muy buen encaje.

---

## 1. Resumen ejecutivo

1. **El estudio está bien documentado y es trazable** (bitácoras, scripts reproducibles, fuente y fecha en casi todo). Para explorar sirve. **Para decidir una inversión todavía no**: mide casi solo interés de búsqueda y oferta visible. No tiene voz del consumidor ni del canal, ventas reales, costos, márgenes ni tamaño de mercado.
2. **La regla de "3 fuentes independientes" no se cumple como está escrita.** Con un criterio estricto de familias, **sobres de electrolitos baja de 3 a 2**: el propio entregable B3 dice que "esta categoría no se valida por Mercadona y Tesco"; la "señal B3" del radar es Falabella Chile. **El café o batido proteico listo para beber queda en 3, pero con la señal de Google débil.** Hoy no hay ninguna candidata que cumpla la regla con holgura.
3. **La regla también se aplicó de forma inconsistente.** Seis oportunidades con 2 fuentes siguen en "radar" y no pasan a "candidata". Cold brew es "candidata" con 2. Seis oportunidades recibieron su primera señal de Google (vía Ads) y no se les sumó la familia. Granola tiene señal en 4 familias y figura con 2. **La regla cuenta señales, no atractivo.** La categoría con más familias (granola) es también la más saturada.
4. **Hay errores regulatorios que cambian la lectura central de "líquidos sin azúcar = ventaja regulatoria".** (a) El art. 120 bis del Reglamento Sanitario de los Alimentos (RSA) exime del "ALTO EN" a los alimentos **sin azúcares, miel, jarabes, sodio ni grasas saturadas añadidos**. Por eso un jugo 100 % fruta sin azúcar añadida **no** llevaría sello de azúcares, y la granola Wild "libre de sellos" con 346 kcal no es una anomalía. (b) Un electrolito **lleva sodio añadido**. Si se registra como alimento, se evalúa ya reconstituido y puede pasar de 100 mg/100 ml (ALTO EN SODIO). (c) Los suplementos alimentarios están exentos de sellos. Los "alimentos para deportistas" lo están solo si cumplen los descriptores a)–d) del art. 540 (energía o carbohidratos), y un electrolito sin azúcar no los cumple. (d) En Mercado Libre, la categoría "electrolitos sobres" está contaminada con **sales de rehidratación oral, que en Chile son medicamentos** (Suma, Hydrasor, Apotex).
5. **Sesgos estructurales:** un solo analista (Boris) generó 14 de 15 bitácoras y 26 de 29 commits en unos 5 días, incluidas tareas de Mario y Chalo. La preferencia por los líquidos con proteína venía desde la reunión del 10-oct. Además, el 82 % de las filas del B3 ronda 2 vienen de subagentes sin verificar.
6. **Recomendación:** no aprobar la lista corta el 28-oct con la evidencia actual. Aprobar la **matriz y los umbrales antes de ver los puntajes** (sección 7), asignar a Mario y Chalo la evidencia de terreno y costos, y llegar al 11-nov con **costo por maquila, ruta regulatoria escrita y 20+ conversaciones de terreno** para 2 o 3 candidatas.

**Confiabilidad del conjunto: 2,5/5. Utilidad para la decisión del 11-nov: 3/5** (sirve para descartar y priorizar qué investigar, no para elegir).

---

## 2. Auditoría del método

### 2a. La regla de las "3 fuentes independientes"

**Problema conceptual.** Las fuentes del estudio no son independientes en dos sentidos:

- **Misma plataforma, mismo fenómeno.** Google Trends y Google Ads Keyword Planner miden lo mismo: consultas en Google. Las tendencias, el catálogo (API) y la captura de Mercado Libre miden lo mismo desde el mismo marketplace. El grupo ya lo reconoció para ambos casos (bitácoras 1653 y 1850), pero **no lo aplicó parejo** (ver 3.2).
- **Mismo analista, mismo marco.** El B3 no es una fuente de datos. Es juicio del analista sobre una muestra de conveniencia (prensa, Open Food Facts, fichas sueltas), elegida a partir de las mismas señales de Trends. Si la categoría se escogió porque subía en Trends, que luego "aparezca en B3" no es independiente de Trends.
- **Señales de distinto signo se suman como si fueran iguales.** "Poca oferta en Mercado Libre" se cuenta como fuente a favor, pero puede significar hueco o falta de demanda (lo dice el propio radar para el snack de legumbre y el cold brew). Una regla de conteo debería exigir que cada familia muestre **dirección favorable** y separar demanda de oferta.

**Recuento con familias estrictas** (Búsqueda-Google, Marketplace-ML, Publicidad-Meta, Benchmark-internacional-B3, Macro-SII/Comtrade, Terreno-etnografía). Una familia cuenta solo si su señal es directa sobre la oportunidad y en dirección favorable. La captura en retail chileno (Falabella, Jumbo, Líder) dentro del B3 **no** cuenta como benchmark internacional: es oferta local.

| Oportunidad | n_fuentes radar | Familias con señal (estricto) | n estricto | Comentario |
|---|---|---|---|---|
| Sobres y tabletas de electrolitos | 3 | Google, ML | **2** | El B3 no la valida (dicho en el propio entregable); la señal "B3" es Falabella Chile. ML mezcla sales de rehidratación (medicamentos). Trends +13 % ≈ mediana de los términos (+9 %) |
| Café o batido proteico listo para beber 20–30 g | 3 | Google (débil), ML, B3 | **3** | "batido de proteína" en Trends: 90 % de semanas en cero y −17 %; la señal usada es el término paraguas "proteína" y "whey" (polvo). Meta (Surlat) y Comtrade (suero +602 %) son adyacentes |
| Avena barista para cafeterías (foodservice) | 3 | Google, ML | **2** (0 para el canal) | El B3 internacional no muestra producto barista (Hacendado avena y avena con café, sin verificar); "retail saturado" es Chile. Ninguna familia mide foodservice |
| Matcha listo para beber | 3 | B3 (sin verificar) | **1** (formato) | Google, ML y Comtrade (210120 +199 %) apoyan la categoría matcha (4 familias), no el formato listo. Keyword Planner no da ninguna idea de búsqueda de matcha listo |
| Cold brew local sin azúcar | 2 | Google, B3 (débil) | **2** | ML no muestra demanda (no está en el Top 50). Comtrade 210111 +92 % es una partida amplia; sirve como apoyo, no como familia |
| Granola con legumbre a bajo precio | 2 | Google, ML, B3, Meta | **4** | Subconteo. Muestra que la regla no mide atractivo: es la categoría más saturada |
| Leche sin lactosa | 2 | Google, ML | 2 | ML es demanda por marca grande |
| Jugos prensados en frío y shots | 2 | Google, B3 (sin verificar) | 2 | El banco de ideas no es evidencia; ML sin señal |
| Agua con gas saborizada sin azúcar | 2 | Google, B3 (sin verificar) | 2 | El término específico tiene nivel 50 en Ads |
| Snack horneado de lentejas o garbanzo | 2 | B3 | **1** | Google sin dirección favorable (legumbres 0 %, hummus +4 %, chips de garbanzo 50); ML 0 de 30 |
| Yogur griego proteico familiar | 2 | Google, B3 (sin verificar) | 2 | La señal de ML es "yogurt Soprole por mayor", no griego |
| Tés helados sin azúcar | 1 | Google (volumen bajo), B3 | **2** | Subconteo: Mercadona té rojo zero está en el CSV del B3 |
| Chai latte | 1 | Google (Ads), ML, Macro (débil) | **3** | Subconteo. Trends nunca se midió; Ads es la primera señal de Google. Comtrade 210120 +199 % |
| Comida liofilizada | 1 | Google (Ads), ML | **2** | Subconteo |
| Fruta liofilizada | 1 | Google (Ads), ML | **2** | Subconteo |
| Ginger beer | 1 | Google (Ads), ML | **2** | Subconteo |
| Agua de coco | 1 | Google (Trends +18 % y Ads), ML | **2** | El radar dice "sin revisar" en Trends, pero el término está en el resumen de 100 |
| Compra por mayor en línea (canal) | 1 | Google (Ads), ML | 2 | Es un canal, no un producto |
| Pan de masa madre, kimchi, tofu, creatina en gomitas, productos sin sellos | 1 | Google | 1 | "Sin sellos": Meta (Underfive) lo usa como mensaje, pero es adyacente |

**Conclusión.** Ninguna familia de las que existen mide **compra** (sell-out, conversión, recompra) ni la **opinión del cliente o del canal**. La familia Terreno-etnografía está vacía para las 23 oportunidades. Con el criterio estricto, **solo el café o batido proteico llega a 3, y con Google débil**.

### 2b. Sesgos

| Sesgo o vacío | Evidencia | Efecto probable |
|---|---|---|
| **Un solo analista** | 14 de 15 bitácoras y 26 de 29 commits son de Boris; las tareas de Mario (términos de uso, Google Ads) y de Chalo (SII, Comtrade, distribuidores) las hizo Boris con su agente el 16-oct; `estado/mario.md` aún dice "necesita acceso al repositorio" | Sin revisión cruzada: los errores de la sección 3 pasaron sin que nadie los viera |
| **Velocidad** | La mayor parte de la evidencia se generó el 16-oct, entre las 09:50 y las 18:50 | Poco tiempo para verificar; 53 de 65 filas del B3 ronda 2 no están verificadas |
| **Confirmación** | Boris propuso "alimentos líquidos que aporten proteína y fibra" el 10-oct (notas, 01:00:25); el 16-oct los líquidos pasan a ser "eje" (bitácora 1055) sin acuerdo; las candidatas son las 5 líquidas | Las categorías se eligen por Trends y luego se "confirman" con B3 y ML sobre las mismas categorías |
| **Selección previa de líquidos** | 7 de las 10 categorías del B3 ronda 2 son líquidas; la tesis regulatoria que lo justifica ("los sólidos llevan sello") está mal planteada (sección 3.3) | Se pueden estar descartando sólidos sin azúcar añadida que no llevarían sello |
| **Sin enfoque C (etnografía)** | La carpeta `etnografia/` está vacía | Sin voz del consumidor ni del canal; no se sabe por qué se compra ni a qué precio |
| **Sin ventas reales** | El catálogo de ML mide fichas, no ventas; la captura no trae vendidos (`publicaciones_100_o_mas_vendidos` = 0 en todos los términos); Mayorístico no se ha usado | No hay ningún dato de sell-out |
| **Sin costos ni márgenes** | Ningún maquilador verificado; la matriz no se puntuó en margen ni en producción (bien hecho, para no inventar) | El criterio de mayor peso (margen, 20 %) está vacío |
| **Sin tamaño de mercado** | Solo niveles de Keyword Planner (50/500/5.000/50.000) y el dato de barras de US$ 85 M | No se puede saber si el hueco paga un negocio |
| **Tasa base ignorada en Trends** | Mediana de la variación año 2 vs año 1 en los 51 términos con volumen suficiente: **+9 %** (p25 −2,5 %, p75 +17,5 %; 65 % suben) | "Electrolitos +13 %" es un crecimiento típico, no destacado |
| **Términos paraguas** | Café proteico se apoya en "proteína" y "whey"; matcha listo para beber, en "matcha" | Se infla la señal del formato específico |

### 2c. B3: fuentes, fechas y tipo de cambio

- **Barras (13 filas):** todas tienen URL. Una sin fecha (Fulfil, Trolley). Dos de 2024 (Barebells, mango Hacendado). No hay columna de verificación. El dato de Belladieta ("algo más de 100 kcal/100 g") se marcó bien como inconsistente.
- **Ronda 2 (65 filas):** todas tienen URL. **53 (82 %) dicen "reportado por subagente; no verificado"** y solo 12 están verificadas. 9 están "sin fecha" y 2 tienen fuente de 2021–2023. Hay `precio_local` no numéricos ("770 / 690", "1.50-2.00 PVP", "<5", "3490-4490", "no indicado") y no hay columna `fecha_captura`. Además, las capturas chilenas usan URL de `super.lider.cl/search`, que el robots.txt de Líder excluye para bots, en contra de la regla propia del repositorio.
- **Tipo de cambio: no se usó ninguno.** Se dice explícitamente en barras ("sin tipo de cambio no comparo"), pero el radar compara "Hacendado 6,6 EUR/kg frente a ~19.000 CLP/kg" y la ronda 2 cita "€4,24/L" junto a precios en CLP. **Corrección:** fijar el dólar y el euro observados del Banco Central en la fecha de captura, guardarlos en una columna `tc_clp` y comparar por paridad de poder de compra (o al menos en CLP nominal) y por gramo de proteína.

---

## 3. Revisión del radar (23 oportunidades)

1. **Estado vs n_fuentes inconsistente.** Según la regla de la bitácora 1055 (1 = radar, 2 = candidata, 3+ = lista corta), 6 oportunidades con 2 deberían ser candidatas y siguen en radar. Matcha y avena (3) quedan como candidatas por juicio, con razones válidas que la regla no recoge. Cold brew es candidata con 2. **Hay que elegir: o la regla es mecánica, o es un umbral mínimo más juicio documentado.** Se recomienda lo segundo, con el juicio escrito en una columna `motivo_estado`.
2. **Google Ads aplicado de forma desigual.** La decisión "no contar Ads como fuente nueva porque es Google" es correcta para quien ya tenía señal de Trends. A chai, comida y fruta liofilizada, ginger beer, agua de coco y compra por mayor, Ads les da la **primera** señal de la familia Google, y eso debería sumar.
3. **"Avena barista: 3 fuentes de consumo final".** El propio radar reconoce que ninguna mide el canal foodservice. El conteo no corresponde a la oportunidad tal como está definida: con criterio estricto tiene 0 familias para la tesis de canal.
4. **Señales textuales sin cuantificar.** "Poca oferta", "retail saturado", "sin revisar", "lectura parcial", "consultas +450 %" (relativo, sin base), "muchas marcas". Falta una columna numérica por familia (por ejemplo, nivel de Ads, variación de Trends ajustada por la mediana, SKU en Chile, n.º de marcas, precio por unidad de valor en CLP) para que la matriz se alimente sin reinterpretar texto.
5. **Fecha.** `fecha_alta` y `fecha_actualizacion` son 2026-10-16 en las 23 filas, aunque el archivo se reescribió al menos cuatro veces ese día. No queda rastro dentro del archivo de cuándo cambió un estado (sí en git). Conviene un registro largo (`oportunidad, fecha, campo, valor_antes, valor_despues, motivo`).
6. **Fuentes que no son evidencia.** `antecedentes/banco-de-ideas.md` aparece como fuente en jugos, ginger beer y agua de coco. Es una lista interna de ideas, no un dato de mercado.
7. **Agua de coco** dice "sin revisar" en Trends, pero el término está en el resumen de 100 (+18 %).
8. **Volúmenes de Ads como cifra.** `nivel_termino_clave_mes` = 5000 se lee como número. Es un nivel (≈ entre 1.000 y 10.000) y el término clave se eligió a mano (`CLAVE` en el script).

### 3.3 Errores regulatorios dentro del radar y del B3

- **Exención A del art. 120 bis:** solo llevan "ALTO EN" los alimentos a los que se les añadió sodio, azúcares o grasas saturadas (y, en el caso de las calorías, azúcares, miel, jarabes o grasas saturadas). Consecuencias:
  - "Jugos prensados: ALTO EN azúcares probable" → **falso si son 100 % fruta sin azúcar añadida**. El problema real de los jugos es la inocuidad (HPP), la cadena de frío y la vida útil.
  - "Hacendado barrita 343 kcal → ALTO EN calorías aunque no tiene azúcar añadida" → depende de si lleva grasas o azúcares añadidos, no del total.
  - El "misterio" de la granola Wild de 346 kcal "libre de sellos" se explica por esta exención.
  - **La tesis "los sólidos llevan sello; los líquidos no" es demasiado gruesa.** La pregunta correcta es qué se añade.
- **Electrolitos "sin sellos probables":** el sodio es un ingrediente añadido. Como alimento, se evalúa listo para consumir. Con 300–500 mg de sodio por sobre en 500 ml queda entre 60 y 100 mg/100 ml, en el límite. Como suplemento estaría exento, pero con rotulado y advertencias propias. Como "alimento para deportistas", la exención exige cumplir a)–d) del art. 540 (energía o carbohidratos), que un producto sin azúcar no cumple. **Este es el punto que decide la categoría y no está resuelto.**
- **Frontera con medicamentos:** las sales de rehidratación oral (Pedialyte, Rehsal, "sales para rehidratación 60/75/90") están registradas como medicamentos en Chile. En el catálogo de ML de "electrolitos sobres" dominan Suma, Hydrasor, Sesen y Apotex, que son marcas de farmacia. **La señal de oferta y demanda de ML mezcla dos mercados con regulación distinta.**
- **Prórroga para microempresas:** el DS 63/2022 extendió a 120 meses el plazo para que las microempresas rotulen "ALTO EN" (antes eran 72). Contado desde la entrada en vigencia del DS 13/2015 (27-jun-2016), **vencería alrededor del 27-jun-2026**. Hay que confirmar si hubo otra prórroga. Si no la hubo, una SpA nueva tiene que rotular sellos desde el día uno.

---

## 4. Factores de decisión que los datos de demanda no cubren

| Factor | Qué falta saber | Por qué decide |
|---|---|---|
| Regulatorio | Ruta alimento, suplemento o alimento para deportistas (electrolitos, proteína); sellos simulados con fórmula real; autorización sanitaria del lugar donde se elabora (SEREMI) o uso de la del maquilador; rotulado (art. 107), descriptores ("alto en proteínas"); en vegetales, si se puede usar "leche" | Tiempo a mercado y costo; puede bloquear el 12-nov |
| Capital y maquila | Pedido mínimo (MOQ) del maquilador, costo unitario, envase, desarrollo de fórmula, análisis de laboratorio | El criterio de mayor peso (margen) está vacío |
| Vida útil y frío | Los listos para beber lácteos o vegetales piden UHT, ESL o frío; el cold brew es una bebida de baja acidez con riesgo microbiológico si no se valida el proceso; los jugos HPP duran unas semanas y siempre en frío | Determina canal, mermas y logística; Mayorístico y ML funcionan mejor con productos que no requieren frío |
| Canal | Margen que exige cada canal (minimarket, distribuidor, ML con comisión y envío, cafeterías) | El precio de góndola no es el precio de venta del productor |
| Compatibilidad con empleos | Horas por semana por socio; quién atiende pedidos, despachos y ventas en terreno | Foodservice y retail con frío exigen ventas presenciales en horario laboral |

### Evaluación cualitativa preliminar (juicio del auditor, no dato)

> **Juicio preliminar** basado en la evidencia del repositorio y en conocimiento general del sector. Cada puntaje debe reemplazarse con cotizaciones, consulta regulatoria y terreno. Escala: 1 = favorable y 5 = desfavorable (barrera, capital, complejidad, competencia); en encaje de canal, 5 = muy buen encaje con Mayorístico, ML y canales propios.

| Oportunidad | Barrera reg. | Capital | Complejidad op. | Competencia | Encaje canal | Lectura |
|---|---|---|---|---|---|---|
| Sobres y tabletas de electrolitos | 4 | 2 | 2 | 4 | 4 | Fácil de operar y despachar; el riesgo es regulatorio (ruta suplemento, sodio, frontera con medicamento) y la guerra de precios en el nivel masivo |
| Café o batido proteico listo para beber | 3 | 5 | 4 | 4 | 2 | Requiere maquila UHT o aséptica con MOQ alto; compite con Soprole, Loncoleche, NotCo y Nude; pesado de despachar |
| Avena barista (foodservice) | 2 | 4 | 3 | 4 | 2 | Importar o maquilar UHT; vender a cafeterías exige visitas en horario laboral; posible restricción del nombre "leche" |
| Matcha listo para beber | 3 | 4 | 3 | 2 | 3 | Sin demanda del formato; la variante en polvo o sobres (importar y reetiquetar) baja capital a 2 pero sube competencia a 4 |
| Cold brew local sin azúcar | 3 | 3 | 4 | 2 | 3 | Proceso simple, pero vida útil e inocuidad (baja acidez) por validar; Briu ya está; el concentrado mejora logística |
| Granola con legumbre (marca propia) | 2 | 2 | 2 | 5 | 4 | Operación simple y buen encaje con granel y Mayorístico; categoría saturada; con miel o aceite añadidos llevaría sello |
| Leche sin lactosa | 3 | 5 | 4 | 5 | 2 | Terreno de Colun y Soprole; solo tiene sentido como reventa en Mayorístico |
| Jugos prensados en frío y shots | 3 | 4 | 5 | 3 | 2 | Sin sello si son 100 % fruta; HPP y frío obligatorios; vida útil corta; hay inversionista identificado (a favor) |
| Agua con gas saborizada | 2 | 5 | 4 | 5 | 2 | Embotellado intensivo en capital frente a CCU y Benedictino |
| Snack horneado de legumbre | 2 | 3 | 3 | 2 | 4 | No requiere frío y es liviano; demanda débil; con aceite o sal añadidos, sellos probables |
| Yogur griego familiar | 3 | 5 | 5 | 5 | 2 | Lácteo fresco, frío y vida útil corta, frente a grandes jugadores |

---

## 5. Tendencias y ciclos (lectura de los datos del repositorio)

- **Estacionalidad de bebidas frías:** "agua con gas" llega a un índice medio de 73 en enero frente a 44 en junio. **La validación del 12 al 25-nov entra en el alza de verano:** cualquier prueba de bebidas en noviembre y diciembre va a sobrestimar la demanda anual. Hay que ajustar por estación o repetir en marzo y abril.
- **Electrolitos:** mínimo en julio (57) y máximo en septiembre (76), con enero a abril en torno a 71. **El "efecto Mundial 2026" (jun–jul) no se ve en la serie**: esos meses son los más bajos.
- **Alza común en jul–ago 2026:** la mediana semanal del índice en 56 términos sube de ~57 (12-jul) a ~73 (2-ago). Cuando muchos términos sin relación suben a la vez, hay que sospechar un factor común (estación o cambio en Google). Conviene verificarlo con términos de control (por ejemplo "pan" o "arroz") antes de leer crecimientos del último trimestre.
- **Tasa base:** la mediana de crecimiento interanual es de +9 %. Solo se destacan cold brew (+183 %, desde una base baja), agua saborizada (+189 %, base baja), yogur griego (+70 %), agua con gas (+47 %), leche de avena (+43 %) y granola (+40 %).
- **Importaciones (UN Comtrade, 2021→2025):** suero de leche en proteína +602 %, extractos de té +199 %, extractos de café +92 %. Apoyan las tesis de proteína y de té o café, pero son partidas amplias.
- **Entrada de empresas (SII 2019→2024):** té, café e infusiones +69 % y muchas empresas chicas; bebidas no alcohólicas pocas y grandes. Esto respalda los formatos de té o café en polvo y concentrado frente a las bebidas embotelladas.

---

## 6. Regulatorio: lo verificado (con fuente)

| Tema | Detalle | Fuente |
|---|---|---|
| Quién lleva "ALTO EN" | Solo alimentos con sodio, azúcares o grasas saturadas **añadidos**. Exentos: sin esos añadidos (A), granel o fraccionado (B), regímenes especiales (C), **suplementos alimentarios (D.1)** y alimentos para deportistas que cumplan a)–d) del art. 540 (D.2). Los productos que se reconstituyen se evalúan listos para consumir | [DS 13/2015 que modifica el RSA (FAOLEX)](https://faolex.fao.org/docs/pdf/chi155737.pdf) |
| Umbrales finales | Sólidos por 100 g: 275 kcal, 10 g de azúcares, 400 mg de sodio, 4 g de grasas saturadas. Líquidos por 100 ml: 70 kcal, 5 g, 100 mg, 3 g | Citados en el repositorio ([Carey](https://www.carey.cl/entrada-en-vigencia-de-la-ultima-etapa-de-la-ley-de-etiquetado)); confirmar la tabla 1 en el texto oficial |
| Microempresas | DS 63/2022: plazo de 120 meses para que las microempresas rotulen "ALTO EN" (antes 72) | [Diario Oficial 14-jul-2022](https://www.diariooficial.interior.gob.cl/publicaciones/2022/07/14/43302/01/2155877.pdf) |
| Alimentos para deportistas | Art. 540: descriptores de energía, carbohidratos, proteína (alto ≥ 40 % de 50 g), electrolitos (sodio y potasio con mínimos; bebidas hipotónicas o isotónicas por osmolalidad), cafeína ≤ 500 mg/día | [iura.cl, art. 540 DS 977](https://iura.cl/dto-977-minsal/540) |
| Reforma de suplementos (propuesta) | Consulta pública de 2019: limitar "producto para deportistas" a isotónicas, proteína, aminoácidos y creatina; quitar la exención de sellos; venta solo en envase sellado. **No se confirmó si se aprobó** | [Carey, 2019](https://www.carey.cl/en/new-public-consultation-amendments-to-the-sanitary-foods-regulations-regarding-dietary-supplements-and-other-matters) |
| Autorización sanitaria | Quien produce, elabora, envasa, almacena, distribuye o expende alimentos necesita autorización de la SEREMI. Arancel de $12.100 a $899.700 más 0,5 % del capital; vigencia de 3 años; trámite en línea | [ChileAtiende, ficha 172](https://www.chileatiende.gob.cl/fichas/172-autorizacion-sanitaria-de-alimentos) |
| Sales de rehidratación oral | Registradas como medicamentos en Chile | [Vademécum Chile](https://www.vademecum.es/chile/medicamento/1305968/sales-para-rehidratacion-60-polvo-para-solucion-oral) |
| Actualización del RSA de 2026 | Según una fuente secundaria: "leche" solo para leche animal (art. 198); los sustitutos deben declarar su naturaleza (art. 107 a); la publicidad de "ALTO EN" restringida para menores de 14 | [TheFoodTech, mar-2026](https://thefoodtech.com/metodos-de-control-y-regulaciones/reglamento-sanitario-de-los-alimentos-en-chile-cambios-clave-tras-la-actualizacion-2026/); confirmar en el decreto |
| Ley 20.606 | Rotulado, restricción de publicidad a menores de 14 y prohibición de venta en colegios de productos "ALTO EN" | [BCN Ley 20.606](https://www.bcn.cl/leychile/navegar?i=1041570) |

*No es asesoría legal. Lo marcado "confirmar" requiere leer el texto vigente en BCN o consultar a la SEREMI o a un abogado.*

---

## 7. Matriz de puntaje propuesta (para la reunión del 28-oct)

### 7.1 Filtros de entrada (go/no-go previos al puntaje)

Una candidata **no se puntúa** si falla cualquiera de estos filtros:

1. **Ruta regulatoria escrita**: clasificación (alimento, suplemento o deportistas), sellos simulados con la fórmula del maquilador y quién tiene la autorización sanitaria. Si no está resuelta al 4-nov, la candidata no va a validación el 12-nov.
2. **Capital de entrada ≤ CLP 6 M** en total (MOQ + envase + rotulado + análisis + primera pauta), monto a confirmar por el grupo.
3. **Margen bruto ≥ 40 %** al precio del canal (no de góndola), con un costo cotizado por al menos un maquilador.
4. **Primer producto sin cadena de frío** (o con frío solo si el canal ya lo tiene resuelto).
5. **≤ 8 horas por semana por socio** en régimen, sin ventas presenciales en horario laboral.

### 7.2 Criterios y pesos

| Criterio | Peso | Cómo se mide | Fuente | Umbral para 3 o más (de 5) |
|---|---|---|---|---|
| Demanda (nivel y dirección) | 15 % | Nivel de Ads del término de **compra** (no paraguas) y variación de Trends **menos la mediana (+9 %)** | Google Ads, Trends | Nivel ≥ 5.000 y crecimiento sobre la mediana |
| Evidencia de compra y del cliente | 15 % | n.º de entrevistas con intención explícita; dueños de minimarket o cafeterías que lo comprarían; preventas | Etnografía, Mayorístico, netnografía | ≥ 5 de 10 entrevistados o ≥ 3 de 5 locales con interés concreto |
| Hueco de oferta y competencia | 10 % | Marcas y SKU en Chile; precio por unidad de valor (CLP por g de proteína, por porción o por litro) vs el líder | ML, captura en supermercados | ≤ 5 marcas locales o una brecha de precio ≥ 20 % |
| Margen bruto unitario | 20 % | (precio canal − costo puesto en el canal) / precio canal | Cotización de maquila, distribuidores | ≥ 40 % (5 si ≥ 55 %) |
| Capital de entrada y MOQ | 10 % | CLP para el primer lote vendible | Cotizaciones | ≤ CLP 3 M = 5; ≤ 6 M = 3 |
| Barrera regulatoria y tiempo a mercado | 10 % | Semanas hasta el primer lote rotulado legal | Consulta SEREMI o asesor | ≤ 6 semanas = 5; ≤ 12 = 3 |
| Complejidad operativa | 10 % | Vida útil, frío, peso y volumen por despacho, mermas | Ficha técnica del maquilador | Vida útil ≥ 6 meses sin frío = 5 |
| Encaje con canales propios y empleos | 10 % | ¿Se vende en Mayorístico y ML sin cambiar la operación? Horas por semana | Mayorístico, plan operativo | Sin cambios y ≤ 8 h por semana = 5 |

### 7.3 Protocolo para que los datos alimenten la decisión

1. **Pre-registro (28-oct):** se aprueban pesos, anclas 1–5 y umbrales en `decisiones.md` **antes** de puntuar. No se cambian después de ver los resultados.
2. **Ficha de evidencia por candidata:** una tabla con un dato por criterio, con fuente, fecha y verificación (sí/no). Sin dato, el criterio puntúa 1, no "N/A".
3. **Puntuación a ciegas y por separado:** Mario y Chalo puntúan cada uno por su cuenta. Boris prepara las fichas y no puntúa (o puntúa al final). Si dos puntajes difieren en 2 o más, se discute la evidencia, no el número.
4. **Sensibilidad:** se recalcula con ±10 puntos porcentuales en margen y demanda. Una candidata que cambia de lugar con eso es frágil.
5. **Regla de decisión (11-nov):** go a validación si el total ponderado es ≥ 3,5, pasa todos los filtros y tiene **al menos 3 familias estrictas, una de ellas Terreno**. Entre 3,0 y 3,5: se sigue investigando con un plazo. Bajo 3,0: se descarta y queda registrado el motivo.
6. **Validación (12–25 nov) con criterio de éxito definido de antemano**, por ejemplo: ≥ 30 preventas o ≥ 3 % de conversión en la publicación o landing; ≥ 3 de 8 minimarkets que aceptan consignación; recompra ≥ 25 % a 4 semanas (se mide en diciembre). Hay que ajustar por la estación (sección 5).

---

## 8. Qué falta para un estudio de nivel inversión (priorizado)

| # | Brecha | Acción | Responsable | Fecha |
|---|---|---|---|---|
| 1 | Ruta regulatoria de electrolitos y proteína | Consulta escrita a la SEREMI RM o a un asesor: clasificación, sellos con sodio, exención; confirmar si se aprobó la reforma de suplementos de 2019 y si se prorrogó el plazo de microempresas | Mario | 30-oct |
| 2 | Costos y MOQ | 3 cotizaciones por candidata (polvo en sachet, UHT o RTD, cold brew) usando la lista del SII y los distribuidores | Chalo | 4-nov |
| 3 | Voz del consumidor y del canal | 10 entrevistas a consumidores, 5 minimarkets (vía Mayorístico), 5 cafeterías y 3 farmacias o tiendas deportivas, con el prompt etnográfico | Mario y Chalo (Boris no conduce, para reducir el sesgo) | 4-nov |
| 4 | Sell-out | Exportar ventas de Mayorístico por categoría (bebidas, isotónicas, café) de los últimos 12 meses; vendidos visibles en ML (manual) | Boris | 28-oct |
| 5 | Tamaño de mercado | Estimación de arriba hacia abajo (Comtrade + producción, o informes) y de abajo hacia arriba (búsquedas de compra × conversión × ticket) para 2 o 3 candidatas, con rangos | Chalo | 6-nov |
| 6 | Verificación del B3 | Verificar las 53 filas "no verificadas" que sostienen las candidatas o marcarlas como excluidas; agregar `fecha_captura` y `tc_clp` (BCCh) | Boris | 27-oct |
| 7 | Corregir el radar | Recuento estricto por familias, columna `motivo_estado`, señales numéricas y registro de cambios | Boris (revisa Mario) | 27-oct |
| 8 | Separar electrolitos de las sales de rehidratación | Volver a clasificar el catálogo y la captura de ML excluyendo productos con registro ISP | Boris | 27-oct |
| 9 | Simulación de sellos con fórmulas reales | Tablas nutricionales de NotShake, Akapro, Nude, Briu, Happyflow y Amazing Care, más la fórmula de cada maquilador | Boris | 31-oct |
| 10 | Margen por canal | Márgenes que piden ML (comisión y envío), distribuidores y minimarkets | Mario | 4-nov |
| 11 | Control de estacionalidad en Trends | Términos de control y ajuste estacional; reglas para la validación de noviembre | Boris | 31-oct |
| 12 | Horas y roles reales | Plan operativo de 4 semanas por candidata (quién despacha, quién vende) | Los tres | 6-nov |
| 13 | Revisión cruzada | Mario y Chalo leen y firman las fichas antes del puntaje | Mario y Chalo | 7-nov |

---

## 9. Archivos revisados

`CONTEXTO.md`, `decisiones.md`, `plan/plan-estudio-mercado-alimentos.md`, `entregables/2026-10-12_trends-y-meta_primera-pasada.md` (vía datos), `entregables/2026-10-16_b3_barras-mercadona-tesco.md`, `entregables/2026-10-16_b3-ronda2_solidos-y-liquidos.md`, `datos/limpios/2026-10-16_b3_barras_productos.csv`, `datos/limpios/2026-10-16_b3_ronda2_productos.csv`, `datos/limpios/2026-10-16_radar-oportunidades_boris.csv`, `datos/limpios/2026-10-13_google-trends_cl_2anios_resumen_100.csv` y `_series-largo_100.csv`, `datos/limpios/2026-10-12_meta-ads_marcas-activas.csv`, `datos/limpios/2026-10-16_google-ads_resumen_candidatas.csv`, `datos/limpios/2026-10-16_mercadolibre_cl_resumen.csv`, `datos/limpios/2026-10-16_mercadolibre-api_catalogo_resumen.csv`, `datos/limpios/2026-10-16_sii_posibles-maquiladores_pj.csv`, las 15 bitácoras, `antecedentes/2026-10-10_notas-reunion.md`, `antecedentes/banco-de-ideas.md`, `datos/referencia/terminos-de-uso-por-sitio.md`, `estado/*.md` y el historial de git.
