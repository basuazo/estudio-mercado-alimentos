# Cold brew B2B en Santiago: factibilidad de escritorio (etapa 1)

**Fecha:** 2026-10-22 · **Persona:** Boris (con Claude) · **Fase:** Estudio de mercado, Fase 1 → profundización de una candidata
**Alcance:** concentrado a granel y concentrado en botella de 1 L para cafeterías y oficinas de Santiago, producido en una dark kitchen o con maquila. Todas las fuentes se capturaron el 22-oct-2026 (lista al final). Las cifras marcadas **S** son supuestos que hay que medir o cotizar. El modelo está en `modelo_costos.py` y su salida en `datos/limpios/2026-10-22_cold-brew_modelo-costos.csv`.

## Meta de fondo y juez

- **Meta de fondo:** cuentas B2B que **repiten el pedido** porque sus clientes compran café frío.
- **Juez externo:** el registro de ventas (POS) de las cuentas piloto y sus pedidos repetidos.

## Veredicto en seis líneas

1. **Se puede producir en cocina.** Las condiciones: concentrado solo de café y agua, extracción en frío, cadena de frío ≤ 5 °C, resolución sanitaria y **vida útil de 7 días** hasta validarla en laboratorio. No hace falta maquila para empezar.
2. **No existe maquila de café en Chile** que publique tarifas. La HPP (Alta HPP) solo se justifica para vida útil larga: no acepta vidrio y no esteriliza.
3. **Los márgenes funcionan con café comercial:** 44 % en granel a 9.000 CLP/L. **No funcionan con café de especialidad comprado:** 11 %.
4. **Hay un hueco:** nadie vende bag-in-box ni nitro en Chile, y los servicios de café para oficinas no ofrecen bebidas frías. Briu y Tuesta venden botella de 1 L a 13.990 y 19.000 CLP.
5. **El riesgo número uno no es producir. Son la vida útil, el despacho y el invierno.** Un bag-in-box de 10 L se pierde a la mitad en una cafetería chica. En invierno se necesitan 45 a 70 cuentas solo para cubrir costos fijos.
6. **Hay que cambiar la tesis antes de probar.** Envases del tamaño de la vida útil, clientes **sin barista** y operadores con frío propio como canal. La prueba tiene que partir **antes de diciembre**, porque el verano es la ventana.

## 1. ¿Dark kitchen o maquila?

| Tema | Lo que encontramos | Implicancia |
|---|---|---|
| Autorización | DS 977/96, arts. 6–9 y 12: la resolución es **del establecimiento y por giro**; la SEREMI resuelve en 30 días hábiles después de inspeccionar (ChileAtiende, ficha 172). La etiqueta lleva el número de resolución (art. 107). | En una cocina compartida, o el operador tiene el giro "bebidas analcohólicas / concentrado de café" y producimos como su maquila formal, o tramitamos una resolución propia para un espacio delimitado. **Preguntar por escrito a la SEREMI RM.** |
| Sellos | Un concentrado solo de café y agua queda exento (art. 120 bis). | Sin sellos si no lleva azúcar. |
| Inocuidad | Baja acidez (pH ~5,3), aw > 0,97. Regla de los 10 días para envases con oxígeno reducido (FSA). En 8 de 18 cold brews comerciales, Listeria sobrevivió 60 días (Utah State, 2022). El retiro de Death Wish (FDA, 2017) fue por toxina botulínica en lata sin frío. | **7 días** en bag-in-box o barril y **≤ 10 días** en botella hasta tener nuestro estudio de desafío. Nunca a temperatura ambiente. |
| Cocinas | **CoCook** (Santiago Centro): 11.000–12.490 CLP/h; 48 h = 575.520 CLP al mes, con resolución, cámaras de frío y servicios. **Kutt** (Independencia): ~1,04 MM CLP al mes por 18 m², contrato de 12 meses. También Uni Kitchens, Núcleo y Cofactory. | **CoCook u otra por horas** baja el costo fijo y permite partir con resolución existente. Hay que confirmar si aceptan bebidas y si **dejan los tanques reposando de un día para otro** en la cámara (la extracción dura de 12 a 24 h). |
| Maquila | Alta HPP (Lo Espejo) hace HPP a maquila, con prueba gratis, pero no acepta vidrio. No encontramos ninguna maquila de café. | Maquila solo si la cocina falla o si se necesitan más de 14 días de vida útil. Según el modelo, la maquila sale más barata solo si cobra menos de **1.160 CLP/L a 1.000 L al mes** (comparado con CoCook más un operador). |

**Por tiempos, recomendamos CoCook o una cocina similar con resolución vigente.** Una resolución propia (30 días hábiles más la inspección) estaría lista recién a mediados de diciembre y nos haría perder el inicio del verano.

## 2. Economía por unidad

Base: receta 1:5 (Toddy), **4,17 L de concentrado por kg**, café comercial a 16.990 CLP/kg (36 kg o más), porción de **80 ml de concentrado (S)**, merma del 10 % (S).

| Escenario | Costo variable | Precio neto (S) | Margen bruto |
|---|---|---|---|
| Granel, café comercial | 5.067 CLP/L (405 por porción) | 9.000 | 44 % |
| Botella 1 L, café comercial | 5.643 CLP/L | 11.000 | 49 % |
| Granel, café de especialidad | 8.001 CLP/L | 9.000 | 11 % |
| Botella, café de especialidad | 8.576 CLP/L | 11.000 | 22 % |

- **El café es el 75–85 % del costo.** El rendimiento real por kg es el número que más mueve el resultado. Hay que medirlo en el piloto.
- **Del lado del cliente:** a 9.000 CLP/L, la porción le cuesta 720 CLP, un 19 % de un vaso de 3.700 neto. Si lo prepara ella misma le cuesta ~5.700 CLP/L (S). Nuestra diferencia tiene que pagarse con horas de barista, espacio, consistencia y nitro.
- **Punto de equilibrio** con CoCook y un operador de media jornada (despacho semanal de ~17.200 CLP al mes por cuenta, S):

| Cuenta tipo | Verano (24 L/mes) | Invierno (10 L/mes) |
|---|---|---|
| Cafetería o restaurante | 13 cuentas | 45 cuentas |
| Oficina o coworking (16 / 8 L) | 22 cuentas | 69 cuentas |

  Con el módulo Kutt sube a 20 y 70 cuentas de cafetería. Con los socios trabajando sin sueldo, CoCook baja a 8 y 27.
- **Inversión inicial:** ~7,5 MM CLP. Incluye dos tanques de 190 L, un refrigerador de 1.300 L, instrumentos, estudio de vida útil (S, por cotizar) y trámites. El **kit nitro en comodato** cuesta ~690.000 CLP por cuenta y se recupera en ~9 meses de verano. **No conviene ofrecerlo al inicio.**

## 3. Mercado y cliente

- **Competencia:** Briu (concentrado de 1 L a 13.990 CLP; página "Empresas" para HORECA, oficinas y gimnasios, sin granel), Tuesta (1 L a 19.000, para cafeterías), Puelo y Kawas (listo para beber) y Nescafé/CCU (lata, también a cafeterías y vending). **Nadie vende bag-in-box ni barril.**
- **Precio al público:** el cold brew cuesta 3.600–5.800 CLP por vaso (Starbucks 4.400; Elephant 5.800; Triciclo 3.600).
- **Oficinas:** los servicios de comodato (Nescafé con mínimo de 100 tazas al día, Cafeteros, Noli, Cafematic) no ofrecen bebidas frías. Una taza de cápsula cuesta 700–940 CLP: esa es la vara de precio por vaso.
- **Tamaño y hábito:** solo el **4 %** de los chilenos declara tomar café frío o cold brew habitualmente (CORPA para ANDA, abril de 2025). Es una advertencia, pero también el hueco: crear ese hábito es justamente la tesis. En el verano de 2010–11, Starbucks Chile reportó un alza de más de 200 % en bebidas heladas.
- **Referentes:** Wandering Bear partió con suscripciones para oficinas en Nueva York. Keurig lanzó en jul-2026 un dispensador frío para servicios de café de oficina. Joyride vendió su reparto a Aramark en 2020. Peet's cerró Coldcraft en 2019 por el costo de la red de frío.

## 4. Equipo rojo (análisis independiente)

1. **El formato no calza con la vida útil.** Una cafetería que usa 2–6 L por semana pierde entre el 45 y el 77 % de un bag-in-box de 10 L.
2. **La cuenta de invierno apenas paga el despacho** (~22.000 CLP al mes de contribución) y el reparto choca con los empleos de los socios.
3. **La demanda es chica** (4 %), y educar a todo el mercado cuesta caro.
4. **Hay sustitutos a ambos lados:** prepararlo en casa (~5.700 CLP/L) y Briu con marca establecida.
5. **La cadena de frío destruye valor** (Peet's Coldcraft). Un modelo de un solo canal, como oficinas, se cae con un shock (Joyride, Wandering Bear, Snowing In Space en 2020).

**El supuesto más frágil** es el de 24 L al mes por cafetería en verano. **Lo confirma** que 5 pilotos repitan su pedido 3 semanas seguidas, con al menos 5 L por semana. **Lo mata** que el POS muestre menos de 40 vasos por semana.

## 5. La tesis ajustada (más fuerte)

| Antes | Después | Por qué |
|---|---|---|
| Bag-in-box de 10 L | **Bag-in-box de 3 L y botella de 1 L**; granel grande solo para cuentas de ≥ 10 L por semana | Envase al tamaño de los 7 días de vida útil |
| Cafeterías de especialidad | **Primero, negocios con café pero sin barista:** restaurantes, hoteles, coworkings, gimnasios, heladerías y panaderías. Después, cafeterías que no quieren preparar cold brew | La cafetería de especialidad prepara el suyo y su café es parte de su identidad |
| Despacho propio a muchas cuentas chicas | **Canal con frío ajeno:** servicios de café para oficinas, casinos corporativos y distribuidores HORECA, más una ruta propia acotada a 1–2 comunas | Atomic sobrevivió gracias a la maquila; Joyride y Coldcraft cayeron por el reparto |
| Nuestra marca o nada | **También marca blanca**, y "toll brewing" (preparar con el grano del cliente) para tostadores y cafeterías | Elimina el problema del café de especialidad (11 %) y el costo de educar al mercado |
| Campaña "push" genérica | **Kit de verano con el cliente:** menú (cold brew tonic, con leche de avena), material en el punto de venta, 2 semanas de degustación y meta de vasos por día | El hábito se mide en vasos vendidos por cuenta, no en alcance |
| Nitro en comodato | Solo para cuentas con ≥ 40 vasos por semana comprobados | 690.000 CLP por cuenta no se recuperan en una temporada |

## 6. Escalera de ambición

1. **Probar:** 3–4 semanas con 15 cuentas en preventa pagada, antes de diciembre (ver la prueba).
2. **Crear el hábito con evidencia:** el kit de verano en las cuentas que pasen. Se mide el POS semana a semana para saber qué activación sube los vasos por día. Ese dato se vuelve el argumento de venta para la siguiente cuenta.
3. **Convertirse en el proveedor de café frío de los operadores:** un acuerdo con cuota mínima garantizada con 1–3 operadores con frío (servicios de café para oficinas, casinos o cadenas medianas), con nuestra receta y nuestro programa de activación. Así el negocio no depende de nuestra ruta ni de nuestras horas.

## 7. Prueba propuesta (juez y umbrales; hay que acordarlos antes de partir)

- **Producción:** bajo la resolución de una cocina como CoCook (confirmar bebidas y reposo nocturno), con café comercial o un blend, en botella de 1 L y bag-in-box de 3 L. **No se vende nada sin resolución.**
- **Cuentas:** 15 entre restaurantes, coworkings, hoteles y cafeterías sin cold brew. En paralelo, conversaciones con 5 operadores con frío.

| Indicador | Sigue | Se descarta |
|---|---|---|
| Cuentas que pagan por adelantado (9.000 CLP/L neto) | ≥ 6 de 15 | ≤ 5 |
| Cuentas que repiten pedido en la semana 3 | ≥ 4 | < 4 |
| Consumo por cuenta | ≥ 4 L por semana | < 2 L por semana o merma reportada > 25 % |
| Rendimiento medido | ≥ 3,8 L de concentrado por kg | < 3,3 L/kg (el margen cae bajo 35 %) |
| Operadores con frío | ≥ 1 carta de intención con volumen mínimo | 0 |

Límite: la prueba corre en primavera, así que el invierno queda por confirmar.

## 8. Qué falta (llamadas y cotizaciones)

- [ ] **SEREMI RM**, por escrito: ¿se puede producir bajo la resolución de una cocina compartida que agregue el giro de bebidas? — por asignar
- [ ] **CoCook, Uni Kitchens y Cofactory:** ¿aceptan bebidas? ¿Permiten reposo nocturno en la cámara? ¿Precio de un módulo privado? — por asignar
- [ ] **Laboratorio** (SGS, CECTA-USACH, Eurofins): cotizar un estudio de desafío y de vida útil — por asignar
- [ ] **Alta HPP:** tarifa y prueba gratis en bolsa flexible, solo si se necesita vida útil larga
- [ ] **Bag-in-box local** (San Jorge Packaging) y botella PET de 1 L: precio
- [ ] **Precios mayoristas** de Briu, Tuesta, Puelo y Kawas, haciendo de comprador B2B
- [ ] **Piloto de rendimiento:** 2 kg de café en una Toddy (~83.000 CLP) para medir L/kg, Brix/TDS y pH (sin venta)
- [ ] **5 entrevistas** con dueños de restaurantes o coworkings y 2 con servicios de café para oficinas

## Fuentes (capturadas el 2026-10-22)

**Regulación e inocuidad:** DS 977/96 https://isl.gob.cl/wp-content/uploads/2024/08/D.S-N-977actualizado-2013.pdf · art. 107 https://iura.cl/dto-977-minsal/107.html · art. 120 bis https://iura.cl/dto-977-minsal/120-bis · ChileAtiende https://www.chileatiende.gob.cl/fichas/172-autorizacion-sanitaria-de-alimentos · 21 CFR 113.3 https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-113/subpart-A/section-113.3 · 21 CFR 114 https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-114 · retiro de Death Wish https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts/death-wish-coffee-co-announces-recall-nitro-cold-brew-cans-retailers-online-sales · NCA https://www.ncausa.org/Industry-Resources/Cold-Brew/Cold-Brew-White-Paper · Eurofins https://eurofinsus.com/food-testing/resources/microbial-safety-of-cold-brewed-black-coffee-during-retail · Parra (UGA, 2024) https://openscholar.uga.edu/record/2327/files/ParraAngelaMS.pdf · Acharya (USU, 2022) https://digitalcommons.usu.edu/etd/8534 · Claassen et al. (2021) https://pmc.ncbi.nlm.nih.gov/articles/PMC8071471 · Polanco-Estibález et al. (2023) https://pmc.ncbi.nlm.nih.gov/articles/PMC10705998 · FSA https://www.food.gov.uk/sites/default/files/media/document/vacpac.pdf · Maricopa https://www.swm.maricopa.gov/DocumentCenter/View/44843/Cold-Brew-Coffee-Guidance-PDF-Archived · SGS https://www.sgs.com/en-cl/services/microbiological-challenge-testing · CECTA https://usach.cl/node/5193

**Producción:** CoCook https://cocook.cl/cuanto-cuesta-producir-alimentos-en-santiago/ · Kutt https://www.yapo.cl/bienes-raices-alquiler-comercios/dark-kitchen-arriendo-de-cocinas-170292/32571737 · Uni Kitchens https://unikitchens.cl/ · Núcleo https://nucleococinas.cl/ · Cofactory https://www.cofactory.cl/cocinas · Alta HPP https://altahpp.com/ · Café al Mayor https://cafealmayor.cl/tienda/ · Tuesta https://www.tuesta.cl/ · Luz Tostadores https://www.luztostadoresdecafe.cl/ · Outlet del Café https://www.outletdelcafe.cl/collections/cafe-verde-para-tostar · Cristal Pack https://cristalpack.cl/producto/botella-vidrio-de-1-litro/ · bag-in-box https://baginbox.store/es/product-category/bag-in-box-bags/ · https://baginbox.cl/ · Toddy https://argo.webstaurantstore.com/toddy-5-gallon-commercial-cold-brew-system-with-lift/975CMLTCM.html · KegOutlet https://www.kegoutlet.com/stainless-steel-cold-brew-coffee-system-50-gallon.html · refrigerador https://www.paris.cl/refrigerador-vertical-2-puertas-solidas-1300-litros-MKCBZHOWXL.html · Stumptown https://stumptowncoffee.com/brew-guides/filtron · UF https://www.sii.cl/valores_y_fechas/uf/uf2026.htm

**Mercado:** Briu https://www.briucoldbrew.com/pages/empresas · Tuesta https://pedir.tuesta.cl/pedir/JwAt5ZdKYjN9q8Ngy/cold-brew-1-l-concentrado · Puelo https://puelocafe.cl/products/cold-brew · Kawas https://www.kawas.cl/cold-brew-original-200ml · La Colombe https://www.lider.cl/ip/cafe-te-y-hierbas/cafe-cold-brew-la-colombe-negro-sin-azucar-325ml-x12/00060491300535 · Nescafé/CCU https://americaretail-malls.com/paises/chile/nestle-y-ccu-amplian-su-alianza-y-lanzan-cafe-frio-enlatado/ · T13 https://www.t13.cl/noticia/te-puede-servir/no-cafe-hielo-preparacion-demora-cerca-22-horas-busca-ganar-terreno-chile-22-9-2026 · Starbucks https://www.rappi.cl/restaurantes/900026886-starbucks · fmdos https://www.fmdos.cl/noticias/cafeterias-en-santiago-donde-comer-precios-y-especialidades · Nescafé máquinas https://www.nescafe.com/cl/cultura-cafe/cafe-estilo-de-vida/maquinas-negocio · Cafeteros https://www.cafeteroschile.cl/blogs/blog-cafetero/comodato-maquina-de-cafe-empresas · La Tercera https://www.latercera.com/pulso/noticia/cafeterias-suman-150-inauguraciones-en-el-ultimo-ano-pero-aun-no-llegan-al-peak-de-la-prepandemia/EEJNKCXAS5HXFLMFD2JJYK7XMI/ · ANDA/CORPA https://anda.cl/wp-content/uploads/2025/08/4221-7-Cafe-Presentacion_-ANDA.pdf · Emol 2011 https://www.emol.com/noticias/economia/2011/02/05/462583/las-estrategias-que-aplican-los-cafes-para-no-caer-en-ventas-durante-el-verano.html · Wandering Bear https://www.vendingmarketwatch.com/coffee-service/cold-brew-equipment-and-accessories/news/21075633/wandering-bear-coffee-introduces-shelf-stable-keg-just-in-time-for-cold-brew-season · Keurig https://www.vendingmarketwatch.com/coffee-service/news/55392646/keurig-dr-pepper-keurig-launches-cold-brew-system-for-workplaces-and-foodservice-venues · BevNET 2020 https://www.bevnet.com/news/2020/out-of-office-on-draft-coffee-suppliers-pivot-to-survive/ · Joyride https://www.bevnet.com/news/2020/aramark-acquires-joyride-distribution-services-brand-set-to-re-launch · Peet's Coldcraft https://www.bevnet.com/news/2019/peets-closes-coldcraft-unit-to-focus-on-shelf-stable-coffee-innovations
