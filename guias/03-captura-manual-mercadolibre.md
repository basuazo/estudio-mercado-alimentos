# Captura manual en Mercado Libre: hoja de trabajo

**Para:** Boris (o quien capture) · **Creada:** 2026-10-16 · **Tiempo estimado:** 45–60 min para las 3 candidatas
Complementa la pauta `datos/referencia/pauta-captura-mercadolibre.md` (qué y por qué). Esta guía es el cómo, paso a paso.
La captura la hace una persona navegando normalmente: sin scripts, extensiones ni agentes que recorran el sitio (pauta y términos de uso, pendientes de Mario).

## Antes de empezar
1. Copia `datos/crudos/plantilla_mercadolibre_cl.csv` una vez por término, con la fecha del día:
   `datos/crudos/AAAA-MM-DD_mercadolibre_cl_electrolitos-sobres.csv`, `..._bebida-proteica-cafe.csv`, `..._cold-brew.csv`.
2. Ábrelos en Excel o Google Sheets. Al guardar en Excel: **CSV UTF-8 (delimitado por comas)**.

## Orden de captura (prioridad 1)

| # | Término | Enlace (ordenar por "Más relevantes") | Qué mirar con atención |
|---|---|---|---|
| 1 | electrolitos sobres | https://listado.mercadolibre.cl/electrolitos-sobres | Lytos, ENA, Quenut, Superieur; farmacia (Suma, Hydrasor, Sesen) |
| 2 | bebida proteica café | https://listado.mercadolibre.cl/bebida-proteica-cafe | Solo 4 fichas de catálogo eran sabor café listas para beber (Emana, Optimum Nutrition, Mu, SlimFast) |
| 3 | cold brew | https://listado.mercadolibre.cl/cold-brew | Saltar licores y cafeteras; anotar solo café listo o concentrado (Matiz, Kali, Punta del Cielo, Barizzimo) |

Si queda tiempo (prioridad 2): `bebida hidratante en polvo`, `proteína lista para beber`, `chai latte`, `comida liofilizada`.

## Qué anotar (una fila por publicación, primeros 20)
- **precio_clp:** el precio que se ve, sin cuotas. Si hay descuento, el precio final; el original va en `observaciones`.
- **formato:** cómo viene, escrito para que el script lo entienda: `30 sobres`, `12 x 250 ml`, `1 l`, `400 g`, `20 porciones`.
- **precio_por_porcion_o_litro:** déjalo vacío; lo calcula el script.
- **vendidos_visibles:** tal cual aparece (`+100 vendidos`, `+5mil vendidos`). Si no aparece, vacío.
- **tienda_oficial / envio_gratis:** `si` o `no`.
- **reputacion_vendedor:** color o nivel (`verde`, `MercadoLíder`, `amarillo`…).
- **observaciones:** si es importado, si dice "sin sellos", "sin azúcar", "farmacia", descuento, reseñas llamativas.
- Aparte, copia 10 comentarios de las 2–3 publicaciones líderes en `observaciones` o en un `.md` en `etnografia/` (netnografía).

## Después de capturar
1. Desde la raíz del repositorio: `python scripts/resumir_captura_mercadolibre.py`
   → `datos/limpios/AAAA-MM-DD_mercadolibre_cl_captura.csv` y `..._resumen.csv` (precio mediano por litro, kilo o porción, marcas, vendedores, más vendidos).
2. Pídele al agente que actualice el radar y escriba la bitácora con lo encontrado.
3. Commit → Pull → Push.

## Preguntas que la captura debe responder (de la pauta)
1. ¿Cuántas marcas y cuántas publicaciones con +100 vendidos hay? (saturación)
2. ¿Qué precio por porción o litro cobran los más vendidos?
3. ¿Hay vendedores chilenos nuevos o solo importadores y revendedores?
4. ¿Qué dicen las reseñas de las publicaciones líderes?
