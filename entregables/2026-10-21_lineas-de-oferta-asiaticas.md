# Nuevas líneas de producto para estudiar oferta (comida asiática)

**Fecha:** 2026-10-21 · **Persona:** Boris · **Paso del plan:** A3 Oferta y precios
**Viene de:** `entregables/2026-10-21_tendencias-asiaticas_trends-ads-australia.md` (demanda).
**Datos:**
- `datos/crudos/2026-10-21_supermercados_lineas-asiaticas_busquedas.csv` (búsquedas en Santa Isabel y Tottus, 21-oct).
- `datos/limpios/2026-10-21_lineas-oferta-asiaticas.csv` (14 líneas).

## Qué se hizo
- Se definieron **14 líneas de producto** a partir de las tendencias asiáticas. Cada una tiene sus términos de demanda (Google Ads y Trends) y la señal de Australia.
- Para ver si **ya existe oferta en el retail masivo**, se buscaron 24 términos en **Santa Isabel** y 18 en **Tottus**. La regla de `datos/referencia/terminos-de-uso-por-sitio.md` permite automatizar estos dos sitios respetando robots.txt. La búsqueda se hizo desde el navegador de Claude, a ritmo humano y sin la API. Se guardó solo precio, formato, marca y fecha.
- **Mercado Libre no se tocó.** Por la regla del equipo, esa captura es manual. Abajo queda la pauta para hacerla con los términos nuevos, y el script de resumen ya los reconoce.

**Limitaciones:**
- Solo se miró la primera página de resultados de cada cadena.
- Las dos cadenas buscan de forma aproximada (por ejemplo, "mochi" trae Bon o Bon). Se contaron solo los productos del rubro.
- Jumbo y Líder no se revisaron: Jumbo bloquea búsquedas con parámetros y Líder prohíbe los robots.
- Santa Isabel es un formato chico y puede tener menos surtido que Jumbo.

## Resultado: dónde hay oferta y dónde no

| Línea | Demanda (Ads/mes · oct–jun) | Oferta en supermercado (21-oct) | Lectura |
|---|---|---|---|
| Ramen coreano picante | 5.000 · buldak +112 % | **Nada** en Santa Isabel ni Tottus | Brecha de distribución: la oferta está en tiendas asiáticas y online |
| Ramen premium o caldo listo | 50.000 · ramen +27 % | **D'Fab** (Tottus, "nuevo"): ramen artesanal congelado 375 g a 6.490–6.790 (unos 19.000 CLP/kg) | El formato ya entró al retail. Es competidor directo y prueba de concepto |
| Gyozas y dumplings congelados | 50.000 · +193 % | Frutos del Maipo (cerdo y camarón, 200 g, 4.530–6.050) y Cuisine & Co (verduras, 320 g, 3.990); arrollados de Alimentos Shen y Asia Wok | Solo 2 marcas de gyoza. Hay espacio para variedad (coreana o vegetariana) |
| Boba y té con leche | 5.000 · boba +23 % | **Nada** (ni perlas de tapioca ni kits) | La oferta está en cafeterías. La palabra "bubble tea" ya baja |
| Salsas coreanas (gochujang) | 5.000 · Australia 2,5 veces | **Nada** | Las salsas asiáticas que hay son japonesas o tailandesas |
| Mochi | 50.000 · +25 % | **Nada** | Probable venta en pastelerías y online |
| Pasta miso | 5.000 · +29 % | **Nada** | — |
| Onigiri y kimbap | 50.000 · onigiri +51 % | Nada (es comida preparada) | Su canal es conveniencia y cafeterías, no la góndola |
| Kimchi | Trends +32 % (13-oct) | La Fermentista (Tottus, 400 g, 7.350) | Una marca local artesanal |
| Té japonés (matcha y hojicha) | matcha +29 % (13-oct) | Krüger matcha latte (10 sobres, 3.990) y Supremo matcha (40 g, 2.290); hojicha nada | Casi vacío |
| Fideos asiáticos secos | udon +152 % (base chica) | Fideos de arroz: Exotic Food, Real Thai, Roland, Tucapel y El Dorado; udon nada | Pocas marcas importadas |
| Ramen instantáneo masivo | 50.000 | Maruchan, Nissin, Cuisine & Co, Traverso, Aji-No-Men, Bonanza: 590–720 el sobre de 85 g (6.700–8.500 CLP/kg) | Saturado. Sirve como piso de precio |
| Salsas asiáticas (soya y teriyaki) | 5.000 · soya +22 % | Más de 15 marcas (Kikkoman, Gourmet, Traverso, Japón a tu Mesa, Lee Kum Kee, Crying Thaiger…) | Competido |
| Edamame congelado | 50.000 · estable | Minuto Verde (400 g, 3.890–4.020) | Monomarca y sin crecimiento |

**Lectura general:** en el retail masivo casi no hay oferta asiática más allá del ramen instantáneo y las salsas. Hay 6 líneas con demanda medible que crece y **cero productos** en los dos supermercados: ramen coreano, boba, gochujang, mochi, pasta miso y onigiri. En gyozas, ramen premium y kimchi hay 1 o 2 marcas, y algunas son recién lanzadas (D'Fab). Eso tiene dos lecturas:
- **Oportunidad:** hay espacio en la góndola y nadie lo está ocupando.
- **Advertencia:** hay que ver si la demanda se compra en otro lado (Mercado Libre, tiendas de Patronato, delivery) o si el retail no lo tiene porque no rota.

Esa es la pregunta para Mercado Libre y para el terreno.

## Pauta para Mercado Libre (captura manual, guía 05, sección 4.B)
El script de resumen (`scripts/resumir_captura_mercadolibre.py`) ya reconoce estos términos. Para cada uno tiene reglas de objetivo, adyacente y descarte, y la unidad de precio (CLP/kg, CLP/L o CLP por porción). Los 13 casos de prueba anteriores siguen correctos.

| Prioridad | Término (escribirlo así) | Objetivo | Adyacente | Descartar |
|---|---|---|---|---|
| 1 | `ramen coreano` | ramen de marca coreana (Samyang/Buldak, Nongshim, Ottogi, Paldo) | ramen no coreano, salsas, snacks | lo que no es ramen |
| 1 | `caldo ramen` | caldo listo, ramen congelado y kits | fideos instantáneos o secos, salsas | cubos y consomé |
| 1 | `perlas de tapioca` | perlas y kits de bubble tea | té en polvo o en hojas, jarabes, listo para beber | harina o almidón de tapioca |
| 1 | `gochujang` | pasta o salsa | polvo, ramen con gochujang | — |
| 2 | `gyozas congeladas` | gyozas y dumplings congelados | masas o tapas, salsas | — |
| 2 | `mochi` | mochi congelado o dulce | harina para mochi | — |
| 2 | `kimchi` | kimchi | salsa o polvo de kimchi, ramen de kimchi | — |
| 2 | `pasta miso` | pasta miso | sopa instantánea, ramen de miso | — |
| 2 | `te hojicha` | polvo u hojas | listo para beber, cápsulas | — |

Cómo hacerlo:
1. `python scripts/preparar_captura.py mercadolibre "ramen coreano" "caldo ramen" "perlas de tapioca" "gochujang"` (prioridad 1, unos 80 minutos).
2. Anotar los primeros 20 resultados de cada término (guía 05, 4.B).
3. Correr `python scripts/resumir_captura_mercadolibre.py proponer` y `resumir AAAA-MM-DD`.
4. Subir la propuesta a la mesa de validación.

**Qué mirar además del precio:**
- Si el vendedor es importador, tienda asiática o marca chilena.
- Si hay tienda oficial.
- Los vendidos visibles en los 3 primeros resultados.
- Si aparecen marcas chilenas pequeñas: son las que muestran si el modelo "marca + maquila" ya existe en la línea.

## Terreno sugerido (lo que no ve ni el supermercado online ni Mercado Libre)
- **Patronato y tiendas asiáticas** (Barrio Coreano de Recoleta): surtido y precio de ramen coreano, gochujang, mochi, tteokbokki y perlas de tapioca. Preguntar quién importa y quién distribuye.
- **D'Fab en Tottus:** preguntar en tienda cómo rota y desde cuándo está.
- **Conveniencia y cafeterías** (Oxxo, estaciones, cafeterías universitarias): onigiri, kimbap y té con leche.
- **Congelados de Jumbo y Líder (a mano):** gyozas, dumplings y mochi.

## Decisiones propuestas (para acordar en grupo)
- Llevar a la matriz de puntaje 4 líneas con demanda y góndola vacía o incipiente: ramen premium o caldo listo, gyozas congeladas, boba o té con leche, y gochujang. Todas tienen que pasar la regla de 3 familias: hoy tienen búsqueda + supermercado + (Australia o Comtrade).
- No priorizar ramen instantáneo masivo, salsas de soya ni edamame (competidos o monomarca sin crecimiento).
- Tratar el supermercado online como una familia de fuente propia ("oferta en retail"), distinta de Mercado Libre.
