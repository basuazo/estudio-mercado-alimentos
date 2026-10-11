# Plan de Estudio de Mercado — Industria de Alimentos

**Versión exportada:** 2026-10-10 · Autor: Boris · Doc vivo: https://claude.ai/code/artifact/51651435-1c29-4d8a-a447-b606095af0d5

## Objetivo y alcance

El estudio debe terminar en una lista corta de 3 a 5 productos alimentarios simples, con evidencia de demanda en Chile y un vacío de oferta, para validar uno en el mercado. Así lo acordamos en la reunión del 10 de octubre: priorizar viabilidad comercial sobre desarrollo técnico y entrar con productos simples (ej. barras, bebidas con proteína o fibra, granel fraccionado).

**Preguntas que el estudio debe responder**

1. ¿Qué categorías y atributos crecen en interés en Chile (búsquedas, publicidad, ventas visibles)?
2. ¿Quién compite hoy en esas categorías, a qué precio y por qué canal?
3. ¿Qué productos venden bien en mercados comparables y no existen (o casi no existen) en Chile?
4. ¿Cuáles de esos productos podemos producir, maquilar, importar o reetiquetar con nuestro capital y sin resolución técnica compleja?

**Dentro del alcance:** alimentos y bebidas envasados de consumo masivo, canales retail, minimarket, e-commerce y mayorista.

**Fuera del alcance por ahora:** desarrollo de recetas en laboratorio, agroindustria de gran escala en Ñuble (queda como horizonte de largo plazo) y estimaciones de ventas reales de supermercados, que no son públicas.

**Principio de trabajo:** no buscamos datos perfectos, sino señales repetidas en varias fuentes. Una oportunidad entra a la lista corta solo si aparece en al menos 3 fuentes independientes.

## Enfoque A: mercado local

El objetivo es mapear demanda, oferta y precios en Chile con fuentes públicas, repitiendo la captura cada semana para ver movimiento y no solo una foto. Antes de cualquier scraping, Mario valida términos de uso de cada sitio; donde no esté permitido, se captura manualmente o con muestras pequeñas.

### A1. Demanda: qué busca y mira la gente

| Fuente | Acción concreta | Dato que sale | Frecuencia |
| --- | --- | --- | --- |
| [Google Trends](https://trends.google.com) | Comparar 40–60 términos (proteína, fibra, keto, sin azúcar, vegano, snack saludable, kombucha, granola, etc.) en Chile, 5 años y 12 meses; revisar “consultas en aumento” por región | Curvas de interés y términos emergentes | Mensual |
| Google Ads – Planificador de palabras clave | Volumen mensual y tendencia de los mismos términos y sus variantes de producto | Búsquedas/mes y CPC (proxy de competencia) | Una vez + actualización mensual |
| Autocompletado de Google, Mercado Libre y YouTube | Registrar sugerencias para “barra de…”, “bebida con…”, “snack sin…” | Lenguaje real del consumidor | Una vez |
| TikTok Creative Center (tendencias y hashtags) | Hashtags y productos de alimentos en tendencia en Chile | Productos virales y formatos | Quincenal |
| Instagram / TikTok orgánico | Seguir 20–30 cuentas de nutrición, fitness y marcas emergentes; anotar productos recomendados | Productos que “mueve” la conversación | Semanal |

### A2. Competencia: quién invierte y crece

| Fuente | Acción concreta | Dato que sale | Frecuencia |
| --- | --- | --- | --- |
| [Biblioteca de anuncios de Meta](https://www.facebook.com/ads/library) | Buscar por palabra clave y por marca; contar anuncios activos, antigüedad y formatos | Marcas que pagan publicidad y cuánto tiempo la sostienen | Semanal |
| [Centro de transparencia de Google Ads](https://adstransparency.google.com) | Revisar anunciantes de alimentos en Chile | Anunciantes activos y regiones | Quincenal |
| Sitios y RRSS de marcas | Ficha por marca: seguidores, crecimiento, precios, canales, puntos de venta | Mapa de competidores | Una vez + seguimiento |
| Kickstarter / Fondos Sercotec y Corfo adjudicados | Revisar proyectos de alimentos financiados recientemente | Qué ideas ya están en camino | Una vez |

### A3. Oferta y precios: qué se vende y a cuánto

| Fuente | Acción concreta | Dato que sale | Frecuencia |
| --- | --- | --- | --- |
| Mercado Libre Chile | Por categoría objetivo: listar publicaciones, precio, vendedor, unidades vendidas visibles y reputación (vía API oficial si el acceso lo permite) | Ranking de productos más vendidos y rango de precios | Semanal |
| Supermercados online (Jumbo, Líder, Unimarc, Tottus, Santa Isabel) | Captura de catálogo por categoría: SKU, marca, formato, precio, sellos, ofertas | Surtido actual, precio por kg/litro y huecos de categoría | Semanal (ofertas) / mensual (surtido) |
| Distribuidores y mayoristas (Alvi, Mayorista 10, Central Mayorista, distribuidores de Santiago y Chillán) | Listas de precios y catálogos; contacto directo donde no haya web | Precio mayorista y margen posible | Mensual |
| Apps de delivery (PedidosYa Market, Rappi, Uber Eats) | Surtido de categorías “saludables” en dark stores | Productos de alta rotación urbana | Mensual |
| Tiendas especializadas (naturistas, deportivas, veganas online) | Catálogo y precios de nicho | Productos premium y márgenes | Mensual |
| Mayorístico.cl (datos propios de Boris) | Exportar ventas por producto y categoría | Rotación real en minimarket | Una vez + mensual |
| Recorrido en terreno | 5–10 minimarkets y 2 supermercados en Santiago y Chillán: fotos de góndola y conversación con dueños | Qué se pide y no llega | Una vez |

### A4. Datos macro y de industria

| Fuente | Acción concreta | Dato que sale |
| --- | --- | --- |
| SII – estadísticas de empresas por rubro | Serie de número de empresas y ventas por actividad de elaboración y comercio de alimentos | Crecimiento y concentración por subrubro |
| Aduanas – datos de importaciones | Importaciones por código arancelario (barras, bebidas, suplementos, snacks) | Qué se trae de afuera, cuánto y de dónde |
| INE (IPC por producto) y ODEPA | Precios y consumo de alimentos | Contexto de precios |
| Mercado Público | Licitaciones y compras ágiles de alimentos (colaciones, JUNAEB, hospitales) | Demanda institucional |
| Informes de consultoras y gremios (Chilealimentos, Euromonitor, Kantar, NielsenIQ, McKinsey, EY) | Resúmenes públicos y notas de prensa | Tendencias de categoría |

## Enfoque B: benchmarking internacional

El objetivo es encontrar productos que ya funcionan en mercados parecidos a Chile y que aquí no existen, para replicarlos o importarlos en vez de inventar. Se revisan 6 mercados en dos grupos: los que suelen adelantarse a Chile en tendencias y los que tienen hábitos de consumo más cercanos.

### B1. Países a revisar

| País | Por qué | Fuentes principales |
| --- | --- | --- |
| España | Idioma, hábitos y marca blanca fuerte; Mercadona lanza productos saludables a precio masivo | Mercadona, Carrefour, El Corte Inglés, Amazon.es |
| Reino Unido | Mercado líder en snacks “high protein” y “free from” | Tesco, Sainsbury’s, Holland & Barrett, Amazon.co.uk |
| Estados Unidos | Origen de la mayoría de las tendencias que llegan a Chile con 2–5 años de rezago | Whole Foods, Trader Joe’s, Target, Amazon “Movers & Shakers” |
| Países Bajos / Alemania | Innovación en alternativas vegetales y formatos simples | Albert Heijn, Rewe, dm |
| Australia | Hemisferio sur (misma estacionalidad), consumo saludable alto | Woolworths, Coles |
| México / Argentina | Ingreso y canal tradicional parecidos a Chile; control de qué llega a Latinoamérica | Walmart MX, Coto, Mercado Libre MX/AR |

El criterio de similitud se puede afinar con datos: gasto en alimentos per cápita, penetración de retail moderno, tasa de obesidad y existencia de etiquetado frontal (México, Argentina y Colombia tienen sellos similares a los chilenos).

### B2. Fuentes transversales

- **Open Food Facts** (base abierta con millones de productos y país de venta): permite cruzar qué productos y categorías existen en Europa y no en Chile, con datos nutricionales para anticipar sellos.
- **Lanzamientos y premios:** ferias como SIAL, Anuga, Biofach y Expo West, y premios de innovación alimentaria; sus listas de ganadores son públicas.
- **Informes de tendencias:** resúmenes públicos de Mintel, Innova Market Insights y Euromonitor (“top trends del año”).
- **Marketplaces mayoristas y de marcas nuevas:** Faire, Amazon Launchpad, Product Hunt (categoría food).
- **Newsletters y medios del sector:** FoodNavigator, Food Dive, The Grocer.

### B3. Método para detectar productos ausentes en Chile

1. **Elegir categorías foco** (5–8) a partir de las señales del Enfoque A, para no revisar todo el supermercado.
2. **Capturar novedades** en cada supermercado extranjero: secciones “novedades”, “más vendidos” y marca propia, por categoría foco. Registrar nombre, formato, atributo principal, precio y foto.
3. **Buscar el equivalente en Chile** en Mercado Libre, supermercados online y tiendas especializadas. Clasificar: no existe / existe importado caro / existe con poca oferta / saturado.
4. **Revisar viabilidad regulatoria**: simular sellos “ALTO EN” con la tabla nutricional (Ley 20.606) y anotar si requiere resolución sanitaria especial.
5. **Identificar fabricantes**: buscar maquiladores en Chile o proveedores en Alibaba / Faire que produzcan algo similar, con costo estimado.
6. **Llevar a la matriz** los productos clasificados como “no existe” o “poca oferta”.

## Enfoque C: etnografía

Los datos digitales dicen qué crece; la etnografía explica por qué la gente compra, cuándo y qué le falta. Se usa en dos frentes: terreno (góndola, minimarket, entrevistas) y digital (comentarios y conversaciones en línea). Para que los tres trabajemos igual, usamos un prompt base para Claude más un módulo por objetivo.

### C1. Usos y entregables

| Objetivo | Dónde | Qué entrega Claude | Qué hacemos nosotros |
| --- | --- | --- | --- |
| Observación de góndola | Supermercados y minimarkets | Pauta de observación y plantilla de registro | Fotos, notas y conteo de SKU por categoría |
| Entrevista a dueños de minimarket | Santiago y Chillán | Guía de 15–20 min con preguntas abiertas | 5–8 entrevistas grabadas (con permiso) |
| Entrevista a consumidores | Perfiles objetivo (deportistas, oficinistas, familias) | Guía de entrevista y criterios de reclutamiento | 8–10 entrevistas |
| Netnografía | Reseñas de Mercado Libre, comentarios de Instagram/TikTok, Reddit r/chile, grupos de Facebook | Codificación de comentarios en temas, dolores y citas | Exportar o copiar los textos con su fuente |
| Síntesis | Todo lo anterior | Mapa de hallazgos, “trabajos por hacer” del consumidor y oportunidades | Revisar y decidir qué entra a la matriz |

Los hallazgos alimentan la matriz de puntaje (criterios de demanda y acceso a canal) y se guardan en la base central como una tabla más: `hallazgos_etnograficos`.

### C2. Prompt base

Se pega al inicio de cada conversación etnográfica, seguido del módulo del objetivo.

```markdown
Actúa como investigador etnográfico especializado en consumo de alimentos en Chile.

Contexto del proyecto: somos un equipo de tres personas buscando un producto alimentario simple
(ej. barras, bebidas con proteína o fibra, granel fraccionado) para entrar al mercado chileno.
No hacemos desarrollo de laboratorio: buscamos huecos de mercado que podamos cubrir
produciendo, maquilando, importando o reetiquetando.

Objetivo de esta sesión: {OBJETIVO}
Categorías foco: {CATEGORIAS}
Lugar o fuente: {LUGAR_O_FUENTE}
Perfil observado: {PERFIL}

Reglas:
- Distingue siempre lo observado (dato) de lo interpretado (hipótesis).
- Usa el lenguaje del consumidor; conserva citas textuales con su fuente.
- Busca momentos de consumo, sustitutos, frustraciones y gastos que la gente ya hace.
- Señala contradicciones entre lo que la gente dice y lo que hace.
- No inventes datos: si falta información, dilo y propón cómo obtenerla.
- Cierra con: 3 hallazgos principales, 3 preguntas abiertas y qué observar la próxima vez.
```

### C3. Módulos por objetivo

```markdown
[OBSERVACIÓN DE GÓNDOLA]
Diseña una pauta de observación de 20 minutos para {LUGAR}. Incluye: qué contar (SKU, marcas,
precios por kg/litro, sellos, espacio en góndola), qué fotografiar, qué conductas de compra
observar y una plantilla de registro en tabla. Luego, cuando te pase mis notas, analízalas.

[ENTREVISTA A DUEÑO DE MINIMARKET]
Diseña una guía de 15–20 minutos: productos que piden y no llegan, qué rota más, a quién le
compra, márgenes y condiciones que exige a un proveedor nuevo. Preguntas abiertas, sin inducir.

[ENTREVISTA A CONSUMIDOR]
Diseña criterios de reclutamiento y una guía de entrevista sobre su último snack o bebida
comprada: cuándo, dónde, por qué, qué reemplaza, cuánto pagó y qué le molesta.

[NETNOGRAFÍA]
Te pegaré comentarios con su fuente. Codifícalos en una tabla: tema, dolor o deseo, producto
mencionado, tono, cita textual, fuente. Agrupa en temas y cuenta frecuencias.

[SÍNTESIS]
Con todas las notas y tablas adjuntas, arma: mapa de temas, "trabajos por hacer" del consumidor,
oportunidades de producto y la evidencia que respalda cada una (fuente y número de menciones).
```

## Datos y herramientas

Toda captura termina en una misma base, con fecha y fuente en cada fila, para que cualquiera del equipo pueda repetir el análisis sin depender de otro.

> Diagrama: flujo de datos (5 grupos de fuentes → captura → base central → análisis → lista corta). Ver el doc vivo.

**Herramientas propuestas (gratuitas o de bajo costo)**

- **Base:** Google Sheets en una carpeta compartida para empezar; migrar a GitHub si los scripts crecen.
- **Captura:** Python (requests, BeautifulSoup, Playwright) para catálogos permitidos; pytrends para Google Trends; API oficial de Mercado Libre si el acceso lo permite.
- **Captura manual:** formulario de Google con campos fijos (producto, país, precio, foto, fuente) para el Enfoque B y el terreno.
- **Visualización:** Looker Studio conectado a la planilla para ver tendencias semana a semana.
- **Apoyo con IA:** Claude para clasificar productos, resumir informes y normalizar nombres entre fuentes.

### Trabajo colaborativo y contexto compartido

Recomendación: un repositorio privado en GitHub como fuente de verdad, un Proyecto de Claude como memoria de contexto y Drive solo para archivos pesados. Las conversaciones con Claude no se sincronizan solas entre personas; lo que se comparte es un resumen de cada sesión con formato fijo, guardado en el repositorio.

| Capa | Herramienta | Qué guarda | Por qué |
| --- | --- | --- | --- |
| Fuente de verdad | GitHub (repositorio privado) | Datos, scripts, prompts, resúmenes de sesión, decisiones | Historial de cambios, quién cambió qué, y Claude puede leer el repositorio completo como contexto |
| Memoria de Claude | Proyecto de Claude (“Proyecto de Company Builder Social”) | Archivo de contexto, plan vigente, decisiones y banco de ideas | Cada conversación nueva parte con el contexto cargado; compartirlo con Mario y Chalo depende del plan de Claude que tengan |
| Archivos pesados | Google Drive (la carpeta de Chalo) | Audios, fotos de terreno, transcripciones, PDFs | Git no maneja bien archivos grandes; se enlazan desde el repositorio |

**Estructura propuesta del repositorio**

```
company-builder/
├── CONTEXTO.md          # quiénes somos, objetivo, estado actual (lo lee Claude primero)
├── decisiones.md        # registro fechado de decisiones del grupo
├── plan/                # este plan y sus versiones
├── prompts/             # prompt etnográfico, de análisis, de cierre de sesión
├── bitacora/            # AAAA-MM-DD_HHMM_persona_tema.md (una entrada por sesión)
├── datos/
│   ├── crudos/          # capturas tal como salen de cada fuente
│   └── limpios/         # tablas de la base central
├── scripts/             # scraping y limpieza
└── etnografia/          # pautas, notas de campo y codificaciones (enlaces a Drive para audios)
```

**Protocolo de sesión con Claude**

1. Al abrir: trabajar dentro del Proyecto de Claude o adjuntar `CONTEXTO.md` y `decisiones.md`.
2. Al cerrar: pedir el resumen con el prompt de cierre (abajo) y guardarlo en `bitacora/`.
3. Si hubo decisiones, agregarlas a `decisiones.md` con fecha y responsable.
4. Cada viernes, uno de nosotros actualiza `CONTEXTO.md` y lo sube al Proyecto de Claude.

```markdown
[CIERRE DE SESIÓN]
Resume esta conversación para el repositorio del equipo, en este formato:
- Fecha, persona, tema
- Objetivo de la sesión
- Hallazgos (con fuentes)
- Decisiones tomadas o propuestas
- Archivos creados o modificados
- Pendientes y responsable sugerido
- Contexto que una próxima sesión necesita saber
Máximo una página. Sin repetir el contenido completo.
```

Para Mario, que recién parte con Git: GitHub Desktop o la edición desde el navegador basta para subir archivos sin usar la terminal; Boris arma el repositorio y hace una sesión de 30 minutos de introducción.

## Análisis y priorización

La decisión sale de cruzar tres preguntas por producto o categoría: ¿hay demanda creciente?, ¿hay poca oferta?, ¿podemos hacerlo? Una idea fuerte en las tres pasa a la lista corta.

### Cruces que vamos a hacer

1. **Demanda vs. oferta:** interés de búsqueda creciente (Trends, Planificador) contra número de SKU disponibles en supermercados y Mercado Libre. Alta demanda con pocos SKU = hueco.
2. **Publicidad vs. tracción:** marcas con anuncios activos por más de 3 meses y seguidores en alza indican categorías rentables; si nadie anuncia, la categoría puede ser nueva o poco rentable.
3. **Extranjero vs. Chile:** productos con ventas o premios afuera y clasificados “no existe” o “poca oferta” aquí.
4. **Precio vs. costo:** precio de venta en Chile (por kg o litro) contra costo mayorista o de maquila estimado. Margen bruto objetivo mínimo a definir (propuesta: 40%).
5. **Importaciones vs. producción local:** categorías con importaciones crecientes (Aduanas) son candidatas a sustitución local.

### Matriz de puntaje

Cada candidato se puntúa de 1 a 5 en cada criterio; el puntaje total ponderado ordena la lista.

| Criterio | Peso propuesto | Cómo se mide |
| --- | --- | --- |
| Demanda y tendencia | 25% | Crecimiento de búsquedas 12–24 meses, menciones en RRSS |
| Hueco de oferta | 20% | SKU en Chile, presencia de importados caros |
| Margen esperado | 20% | Precio de venta vs. costo estimado |
| Facilidad de producción o abastecimiento | 15% | Existencia de maquilador o proveedor, inversión inicial |
| Barrera regulatoria | 10% | Sellos, resolución sanitaria, etiquetado |
| Acceso a canal | 10% | Si entra en minimarket, Mercado Libre, Mayorístico o compras públicas |

La innovación no es filtro de entrada (quedó pendiente en la reunión); se puede sumar como criterio de desempate si el grupo lo acuerda.

## Cronograma y responsables

En seis semanas pasamos de este plan a una lista corta acordada; la validación de mercado parte el 12 de noviembre.

> Diagrama: ruta de trabajo — Fase 0 Preparación (10–14 oct) · Fase 1 Recolección (15–28 oct) · Fase 2 Análisis (29 oct–11 nov) · Fase 3 Validación (12–25 nov). Hitos: 14 oct plan aprobado; 11 nov lista corta.

| Frente | Responsable | Entregable |
| --- | --- | --- |
| A1 Demanda y A2 Competencia (Trends, Meta, TikTok) | Boris | Lista de términos y marcas con tendencia |
| Planificador de Google Ads y validación legal del scraping | Mario | Volúmenes de búsqueda y reglas por sitio |
| A3 Oferta y precios (supermercados, Mercado Libre, distribuidores) | Mario y Chalo | Catálogo y precios por categoría foco |
| A4 Macro (SII, Aduanas, informes) | Chalo | Series por subrubro e importaciones |
| B Benchmarking internacional | Boris | Fichas de productos ausentes en Chile |
| Base de datos y análisis | Boris (con todos) | Matriz de puntaje y lista corta |

La asignación es una propuesta para discutir el miércoles.

## Próximos pasos y decisiones pendientes

**Antes de la reunión del miércoles Oct 14, 2026**

- [ ] Boris: crear el repositorio privado en GitHub con la estructura propuesta, `CONTEXTO.md` y los prompts (etnográfico y de cierre de sesión).
- [ ] Boris: primera pasada de Google Trends con 40 términos y lista de 10 marcas con anuncios activos en Meta.
- [ ] Boris: elegir 2 supermercados extranjeros (Mercadona y Tesco) y probar el método B3 en una categoría (barras).
- [ ] Mario: revisar términos de uso de Mercado Libre, Jumbo, Líder y Unimarc respecto a scraping; proponer alternativa por sitio.
- [ ] Mario: Planificador de palabras clave de Google Ads con la misma lista de términos.
- [ ] Chalo: levantar fuentes macro (SII, Aduanas) y listar distribuidores de Santiago y Chillán con contacto.
- [ ] Todos: probar el prompt etnográfico con un módulo cada uno (una góndola, un dueño de minimarket, 50 reseñas de Mercado Libre) y guardar el resumen en `bitacora/`.

**Decisiones para el grupo**

- Categorías foco iniciales (propuesta: barras y snacks, bebidas funcionales con proteína o fibra, granel fraccionado).
- Pesos de la matriz de puntaje y margen mínimo aceptable.
- Si la innovación entra como criterio.
- Confirmar el esquema de trabajo compartido propuesto (GitHub + Proyecto de Claude + Drive) y quién actualiza el contexto cada semana.
- Presupuesto para herramientas pagadas (si alguna fuente gratuita se queda corta).
