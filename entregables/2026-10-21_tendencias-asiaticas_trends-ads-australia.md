# Tendencias de comida asiática en Chile y Australia como predictor

**Fecha:** 2026-10-21 · **Persona:** Boris · **Paso del plan:** A1 Demanda (ampliación asiática) y B (benchmark internacional)
**Fuentes:** Google Trends Chile y Australia (captura 21-oct desde el Chrome de Boris), Planificador de Google Ads (exportaciones de Boris del 21-oct, 22:05), UN Comtrade (API pública, consulta 21-oct) y prensa citada al final.

## Por qué este informe
El estudio del 12–13 de octubre (100 términos) tenía un sesgo occidental: proteína, keto, kombucha, granola. En Chile entró con fuerza comida asiática (ramen, bubble tea, comida coreana) y no la estábamos midiendo. Aquí medimos 100 términos asiáticos con el mismo método y probamos si Australia sirve para anticipar lo que llega a Chile.

## Resumen en 8 puntos
1. **Lo japonés es el mercado grande y maduro.** Sushi tiene unas 500.000 búsquedas al mes y crece +10 %, casi lo mismo que la deriva común de +8 %. Las 13 palabras japonesas suman unas 735.000 al mes, la mitad de todo lo asiático medido (1,46 millones al mes). Es grande, pero ya no crece rápido.
2. **Lo que crece son los fideos y los caldos.** Ramen tiene 50.000 búsquedas al mes y sube +27 % (+35 % año contra año). Buldak sube +112 % (en el Planificador salta +900 %). Desde bases más chicas suben udon (+152 %), pho (+174 %), soba y yakisoba.
3. **Formatos de mano y colación.** Dumplings (+193 %, unas 50.000 al mes), onigiri (+51 %, unas 50.000), kimbap (+160 %) y mochi (+25 %, unas 50.000). Calzan con la "colación", la ocasión que ya marcamos como transversal.
4. **Lo coreano pasó de novedad a platos concretos.** "Comida coreana" baja −11 %, pero kimbap, bibimbap, gochujang, buldak y tteokbokki suben. Es señal de que la categoría está madurando, no de que se esté acabando.
5. **Bubble tea: la palabra cae y el producto no.** "Bubble tea" baja −26 % y "boba" sube +23 % (con más volumen: índice 52 contra 19). "Té con leche" sube +92 % desde una base chica. La importación de tapioca se multiplicó por 3,5 en kilos entre 2021 y 2025.
6. **Salsas e ingredientes para cocinar en casa crecen poco pero de forma estable.** Salsa de soya sube +22 % y miso +29 %. El resto está estable (teriyaki, ostras, aceite de sésamo, arroz para sushi).
7. **Lo que no mueve la aguja:** soju (−22 %), ginseng (−3 %), té verde (−4 %), y lo "funcional asiático" (konjac, shirataki, tempeh, goji), que tiene búsquedas pero sin tendencia clara.
8. **Australia sirve como radar, no como pronóstico.** De 26 tendencias globales de comida, 12 aparecieron antes en Australia y llegaron con fuerza a Chile (adelanto mediano de unos 2,5 años; otras 2, kale y açaí, llegaron débiles), 5 fueron simultáneas y algunas nunca llegaron (hard seltzer, corn dog coreano, mochi donut, tanghulu). El rezago se acortó: antes de 2020 era de 2–3 años y ahora es de 0–5 trimestres. Australia anticipa bien **qué** puede llegar y si una moda se va a desinflar, pero mal **cuándo**.

## 1. Método (igual al estudio del 13-oct, con dos mejoras)
- **100 términos** en 10 grupos: fideos y sopas, bebidas asiáticas, japonés, coreano, chino y chifa, sudeste asiático e India, ingredientes y salsas, salud de origen asiático, snacks y dulces, y canal → `datos/referencia/2026-10-21_terminos-busqueda_asiaticos.csv`.
- **Google Trends Chile:** se usó la misma ventana (2024-10-06 a 2026-10-04, semanal) y cada término se consultó solo. El año 2 se compara con el año 1 y se calcula el volumen relativo con granola como ancla (grupos de 4 + granola).
- **Mejora 1: ventana octubre–junio.** Entre julio y agosto de 2026, 10 términos tuvieron su máximo en la misma semana (2 de agosto): ramen, udon, soba, pho, dumplings, onigiri, miso, kimbap, mochi y edamame. Las consultas relacionadas de esa semana están en inglés ("udon noodle soup near me", "edamame near me"). Puede ser un cambio de Google o Maps, turismo de invierno o un evento, y queda **por confirmar**. Para no confundir ese pico con una tendencia, el indicador principal es **octubre–junio de un año contra octubre–junio del anterior**, que deja fuera el invierno en ambos años. La variación anual completa sigue en el CSV.
- **Mejora 2: cruce con Google Ads.** Del Planificador sale el volumen absoluto (en tramos de 50 / 500 / 5.000 / 50.000 / 500.000), el CPC y la competencia. Con eso armamos una matriz de 5 cuadrantes: *crece con volumen*, *crece desde base chica*, *estable*, *cae* y *nicho o sin datos*.
- **Deriva común:** la auditoría del 16-oct encontró que las búsquedas crecen en general un +8,45 % (mediana). En este set, la mediana de los 28 términos con datos suficientes es +8 % (año) y +7,5 % (oct–jun). Un término crece de verdad solo si supera claramente ese piso: sushi (+10 %) está en la deriva; ramen (+27 %) y salsa de soya (+22 %) están sobre ella.
- **Limitaciones:**
  - El Planificador redondea por tramos, así que su "0 %" de cambio no significa que el término esté plano.
  - Ads suma variantes ("gyozas", "gyosas") y Trends mide el término exacto. Por eso gyoza tiene unas 50.000 búsquedas en Ads y datos esporádicos en Trends.
  - El índice de sushi frente a granola (1.793) es impreciso porque granola queda casi en cero en ese grupo.
  - 11 de los 100 términos no tienen datos en Trends y 42 tienen datos esporádicos.

## 2. Matriz Trends × Ads (Chile)
Fuente: `datos/limpios/2026-10-21_matriz-asiaticos_trends-x-ads.csv`. La variación es octubre–junio contra el año anterior.

**Crece con volumen (13)**

| Término | Búsquedas/mes (Ads) | Var. oct–jun | Competencia Ads | CPC alto (CLP) |
|---|---|---|---|---|
| dumplings | 50.000 | +193 % | Media | 323 |
| pho | 5.000 | +174 % | Baja | — |
| kimbap | 5.000 | +160 % | Baja | 790 |
| udon | 5.000 | +152 % | Baja | 1.183 |
| buldak | 5.000 | +112 % | Alta | 468 |
| onigiri | 50.000 | +51 % | Baja | 708 |
| miso | 5.000 | +29 % | Media | 542 |
| ramen | 50.000 | +27 % | Media | 852 |
| mochi | 50.000 | +25 % | Baja | 903 |
| boba | 5.000 | +23 % | Media | 846 |
| sushi delivery | 5.000 | +23 % | Baja | 959 |
| ghee | 5.000 | +23 % | Alta | 787 |
| salsa de soya | 5.000 | +22 % | Alta | 859 |

**Crece desde base chica:** té con leche (+92 %) y ramune (+75 %).
**Cae:** bubble tea (−26 %), soju (−22 %) y comida coreana (−11 %).
**Estable (29):** sushi (+10 %), comida china, chapsui, arroz chaufa, wantan, curry, tempura, teriyaki, panko, edamame, leche de coco, té verde y ginseng, entre otros.
**Nicho con señal que vigilar** (datos esporádicos en Trends, pero con volumen en Ads): gyoza (50.000 en Ads), bibimbap, gochujang, yakisoba, yakult, dim sum, bulgogi y konjac.

**Por categoría:**
- Lo japonés concentra el volumen.
- Fideos y sopas tiene la mayor cantidad de términos que crecen.
- Lo coreano tiene la mediana de crecimiento más alta, pero desde bases chicas.
- Snacks y dulces, y salud de origen asiático, no muestran tendencia.

## 3. Lo que dicen las 1.844 ideas del Planificador
Las ideas salieron de las semillas de fideos y ramen. Clasificación por reglas de texto en `datos/limpios/2026-10-21_google-ads_asiaticos_ideas_clasificadas.csv`. Se excluyeron 257 ideas que parecen de otros países (locales de pho en Vietnam o España).
- **Ramen también se busca como restaurante.** "Ramen cerca de mí" tiene unas 50.000 búsquedas al mes (+900 % anual) y hay 287 ideas con nombre de local o marca (unas 80.000 búsquedas al mes; por confirmar a mano). Hay una escena de ramenerías en Santiago (Ramen One, Joki, Ichiraku, Vramen y otras).
- **En ramen instantáneo manda Maruchan.** Tiene 51 ideas y unas 10.000 búsquedas al mes. Samyang y Buldak suman unas 2.650, Nissin 550, y Nongshim y Ottogi son marginales. El picante coreano crece rápido, pero el volumen sigue siendo de Maruchan.
- **Se busca para comprar y por salud.** Aparecen "fideos de arroz lider" (+900 %), "mercado libre ramen coreano", "caja de ramen maruchan" y "comprar ramen picante". También "engordan los fideos de arroz" (500 al mes), "fideos de arroz dieta", "udon sin gluten" y "shirataki fideos" (5.000).

## 4. Importaciones (UN Comtrade, Chile, CIF USD)
Fuente: `datos/crudos/2026-10-21_un-comtrade_importaciones-chile_asiaticos.csv`.

| Partida | 2021 | 2025 | Var. valor | Var. kilos | Origen asiático principal (2025) |
|---|---|---|---|---|---|
| 190300 Tapioca (perlas) | 87 mil | 217 mil | +148 % | +246 % | Taiwán 54 %, China 17 % |
| 190230 Pastas n.c.p. (incluye fideos instantáneos) | 13,1 M | 16,1 M | +23 % | +62 % | China 57 %, Corea 4 % |
| 121221 Algas comestibles (nori) | 9,6 M | 8,0 M | −17 % | −41 % | China 76 %, Corea 12 % |
| 210310 Salsa de soya | 9,1 M | 7,5 M | −18 % | −4 % | China 25 % |
| 220600 Fermentadas n.c.p. (incluye sake) | 2,2 M | 1,3 M | −40 % | −51 % | Japón 12 % (era 1 %) |
| 151550 Aceite de sésamo | 0,65 M | 0,69 M | +6 % | −8 % | China 50 % |

Lectura:
- La tapioca confirma que el bubble tea sigue vivo, aunque desde una base chica (124 t en 2025).
- En fideos crecen los kilos más que el valor, lo que apunta a fideos más baratos.
- Corea pesa poco como origen directo. Es probable que el ramen coreano entre por distribuidores o terceros países (por confirmar con datos de Aduanas por marca).

## 5. ¿Qué tan bueno es Australia para predecir a Chile?
Datos: `datos/crudos/2026-10-21_google-trends_au-vs-cl_trimestral_26-temas.csv` (temas de Trends, que no dependen del idioma, trimestral 2010–2026) y `datos/limpios/2026-10-21_au-vs-cl_resumen_por-tema.csv`. Script: `scripts/analizar_australia_vs_chile.py`.

**Cómo se midió:**
- Para cada tema se definió un "despegue": el primer trimestre en que la media móvil anual supera el 25 % de su máximo y se mantiene.
- Se comparó el despegue de Australia con el de Chile.
- Se correlacionó el crecimiento anual de ambos países con rezagos de 0 a 12 trimestres.

**Resultados (26 temas):**

| Patrón | Temas | Rezago típico |
|---|---|---|
| Australia primero | bubble tea, kombucha, ramen, kimchi, pollo frito coreano, tteokbokki, cold brew, agua de coco, kefir, mochi, birria, buldak (también kale y açaí, que en Chile casi no despegaron) | 1–3 años antes de 2020 (kefir y pollo frito coreano, más de 6); 1–5 trimestres después |
| Casi simultáneo (virales por redes) | masa madre (pandemia), quinoa, cottage cheese, smash burger, chocolate Dubái | 0–1 trimestre |
| Chile primero o propio | chía, colágeno, keto (Chile tuvo base temprana), matcha y leche de avena (ambos suben a la vez; la diferencia de despegue es ruido) | — |
| No llegó | hard seltzer (boom en Australia 2020–22; en Chile nunca pasó de ruido) | — |

Ejemplos que muestran el valor y el límite:
- **Kombucha:** despega en Australia en 2015 y toca techo en 2018; Chile despega en 2018 y toca techo en 2021. Es el mismo ciclo, unos 3 años después. Australia hoy está en el 40 % de su máximo; Chile, en el 85 %. Si se repite el patrón, en Chile viene una baja.
- **Bubble tea:** techo en Australia en 2021, en Chile a fines de 2024. Chile ya está bajando (77 % del máximo), igual que Australia antes.
- **Pollo frito coreano:** unos 6 años de rezago, y en Chile recién está en su máximo (2026).
- **Birria y buldak:** solo 3 y 5 trimestres de rezago. La difusión por TikTok acortó la distancia.
- **La correlación del crecimiento es débil.** La mediana es 0,37–0,39 con 2–3 trimestres de rezago y baja a 0,09 a 12 trimestres. Australia no sirve para proyectar cifras de Chile.

**Radar actual** (Australia, 5 años, 15 temas asiáticos; `datos/crudos/2026-10-21_google-trends_au-vs-cl_5anios_15-temas-asiaticos.csv`):
- **En Australia crecen y en Chile todavía no llegan:**
  - hojicha (Australia ×3,6 en 5 años; Chile ~0);
  - yuzu (Australia +65 %; Chile empieza);
  - katsu sando (Australia +125 % el último año; Chile 0).
  - Son candidatos a llegar en 1–3 años, empezando como producto de cafetería.
- **Ya están llegando:** gochujang (Australia ×2,5; Chile +133 % el último año), dumplings (Chile +305 %), hot pot, bingsu y taiyaki (estos tres desde casi cero).
- **Modas que en Australia ya se desinflaron y en Chile no pegaron:** corn dog coreano (Australia −55 %), mochi donut (−24 %) y tanghulu (−18 %). Conviene no apostar por ellas.

**Conclusión:**
- Australia es un buen **radar temprano**: si algo de comida explota allá, hay una probabilidad razonable de que aparezca en Chile.
- También muestra **cómo termina el ciclo** (kombucha, bubble tea), y eso ayuda a decidir cuándo entrar y cuándo no.
- No sirve para estimar tamaño ni fecha exacta.
- Tiene sentido por tres razones: es del mismo hemisferio (mismas estaciones), tiene una población de origen asiático grande que adopta antes, y su consumo se parece al de Chile en ingreso y urbanización.
- Chile tiene motores propios que Australia no capta: la cocina peruana (chifa y nikkei), la comunidad coreana de Patronato, el K-pop y la ley de etiquetado.
- **Propuesta:** usar Australia como una señal más del benchmark internacional (junto a EE.UU. y Reino Unido), nunca como la única.

## 6. Qué significa para el Company Builder (para discutir)
Estas oportunidades siguen las mismas reglas del radar (3 familias de fuentes y foco en líquidos como eje propuesto):

| Oportunidad | Señales a favor | Familias | Preguntas abiertas |
|---|---|---|---|
| **Caldo de ramen listo o concentrado** (líquido, de almacén o refrigerado), versión sin sellos | Ramen 50.000/mes +27 %, ramenerías en crecimiento, sopa miso y miso +29 %, Australia confirma | Trends, Ads, prensa | Sodio: el sello "alto en sodio" es casi seguro en un caldo; ¿se puede bajar? Revisar maquila |
| **Bebida de té con leche o boba lista para beber**, o kit para casa | Boba +23 %, té con leche +92 %, tapioca ×3,5 en kilos, matcha +29 % (estudio anterior) | Trends, Ads, Comtrade | La palabra "bubble tea" cae: ¿moda madurando? Cadena de frío |
| **Dumplings o gyozas congeladas** con marca chilena | Dumplings 50.000/mes +193 %, gyoza 50.000, Australia confirma (dumpling +53 %) | Trends, Ads, Australia | Competencia en supermercado (por levantar en A3) |
| **Onigiri o kimbap para la colación** (formato de mano) | Onigiri 50.000 +51 %, kimbap +160 % | Trends, Ads | Vida útil, canal (cafeterías, minimarkets) |
| **Salsas coreanas** (gochujang) con marca local | Gochujang en Australia ×2,5 y en Chile +133 %, buldak +112 % | Trends, Australia | Volumen aún chico |
| **Té japonés (hojicha, matcha) para cafeterías** | Hojicha en alza en Australia, matcha ya creció en Chile | Australia, estudio anterior | Hoy no hay demanda medible en Chile |

## Próximos pasos sugeridos
- Levantar precios y oferta en góndola y en Mercado Libre (A3) para ramen o caldo, dumplings congelados y boba: cuántas marcas hay y a qué precio.
- Confirmar el pico de agosto de 2026: revisar las consultas relacionadas por semana y la prensa de esa fecha.
- Llevar las señales asiáticas al radar (`datos/limpios/2026-10-16_radar-oportunidades_boris.csv`) y al dashboard.
- Repetir Australia con EE.UU. y Reino Unido para ver si el rezago se repite (si los tres lo anticipan, la señal es más fuerte).
- Pedir a Aduanas o a un distribuidor (Snaqui, importadores coreanos de Patronato) el volumen de ramen coreano por marca.

## Archivos
- Términos: `datos/referencia/2026-10-21_terminos-busqueda_asiaticos.csv` y `..._para-pegar.txt`.
- Trends Chile: `datos/crudos/2026-10-21_google-trends_cl_2anios_individual_asiaticos.csv`, `datos/crudos/2026-10-21_google-trends_cl_volumen-relativo_asiaticos.csv` y `datos/limpios/2026-10-21_google-trends_cl_2anios_asiaticos_resumen.csv` / `_series-largo.csv`.
- Google Ads: `datos/crudos/2026-10-21_google-ads_asiaticos_100-terminos_12m.tsv`, `..._ideas_24m.tsv`, `datos/limpios/2026-10-21_google-ads_asiaticos_terminos.csv`, `..._ideas_clasificadas.csv` y `..._ideas_resumen.csv`.
- Cruce: `datos/limpios/2026-10-21_matriz-asiaticos_trends-x-ads.csv`.
- Comtrade: `datos/crudos/2026-10-21_un-comtrade_importaciones-chile_asiaticos.csv`.
- Australia: `datos/crudos/2026-10-21_google-trends_au-vs-cl_trimestral_26-temas.csv`, `datos/crudos/2026-10-21_google-trends_au-vs-cl_5anios_15-temas-asiaticos.csv`, `datos/limpios/2026-10-21_au-vs-cl_resumen_por-tema.csv` y `..._correlacion_por-rezago.csv`.
- Scripts: `scripts/procesar_google_trends.py`, `scripts/procesar_google_ads_ideas.py` y `scripts/analizar_australia_vs_chile.py`.

## Fuentes de prensa (consulta 2026-10-21)
- The Clinic, 5-ago-2023, "Comida coreana vive boom en Chile": más de 13 locales coreanos en el sector oriente en menos de 6 meses; calle Seúl en Recoleta (2022). https://www.theclinic.cl/2023/08/05/comida-coreana-vive-boom-en-chile-claves-del-fenomeno/
- Portal Innova, 25-ago-2025, "K-Food en Espacio Food Service busca su lugar en los supermercados chilenos": KOTRA Santiago trabaja con importadores y cadenas para llevar K-food a supermercados. https://portalinnova.cl/?p=172501
- Mediabanco, 24-ago-2026, "Del sushi al ramen…": cadenas de ramen en el nuevo patio de comidas de Parque Arauco Kennedy (mayo 2026). https://www.mediabanco.com/del-sushi-al-ramen-el-caldo-japones-que-esta-redefiniendo-la-comida-rapida-en-chile/


_Corrección 2026-10-21 (misma noche): el primer texto decía "14 aparecieron antes en Australia, rezago mediano de unos 5 trimestres". Esa mediana mezclaba tendencias simultáneas y de Chile primero. Contando solo las que aparecieron antes en Australia y llegaron con fuerza (12), el adelanto mediano es de 10 trimestres (unos 2,5 años): 2,9 años antes de 2020 y 4 trimestres desde 2020. Las cifras corregidas son las del dashboard._
