# Pauta de captura manual en Mercado Libre Chile

**Autor:** Boris (con Claude) · **Creada:** 2026-10-16 · **Para:** las 3 candidatas de B3 y el radar.
Mercado Libre bloquea la lectura automática, así que la captura la hace una persona navegando normalmente. No se usan scripts ni extensiones que recorran el sitio. Mario revisa los términos de uso (tarea pendiente) antes de ampliar el volumen.

## Qué se captura y con qué búsquedas

Prioridad 1 (candidatas): `electrolitos sobres`, `bebida hidratante en polvo`, `bebida proteica café`, `proteína lista para beber`, `cold brew`.
Prioridad 2 (radar): `leche de avena barista 1 litro`, `matcha listo para beber`, `jugo prensado en frio`, `snack de lentejas`.

Por cada búsqueda: ordenar por "Más relevantes", anotar los **primeros 20 resultados** y, aparte, los 5 primeros con filtro de tienda oficial si existe. Sin iniciar compras ni contactar vendedores.

## Campos (una fila por publicación)

`fecha, termino, posicion, titulo, marca, vendedor, tienda_oficial, precio_clp, formato (unidades o ml), precio_por_porcion_o_litro, vendidos_visibles, reputacion_vendedor, envio_gratis, url, observaciones`

- `vendidos_visibles`: lo que muestra la publicación ("+100 vendidos"). Es un rango, no ventas exactas.
- `precio_por_porcion_o_litro`: se calcula después a partir del precio y el formato.
- Guardar con fecha en `datos/crudos/AAAA-MM-DD_mercadolibre_cl_<termino>.csv`. La plantilla con encabezado está en `datos/crudos/plantilla_mercadolibre_cl.csv`.

## Qué buscamos leer

1. ¿Cuántas marcas distintas y cuántas publicaciones con ventas altas hay? (saturación)
2. ¿Qué precio por porción o litro cobran los vendedores más vendidos?
3. ¿Hay vendedores chilenos nuevos o solo importadores y revendedores?
4. ¿Qué dicen las reseñas de las publicaciones líderes? (se copian a mano 10 comentarios para netnografía)

## Cuenta de desarrollador (en paralelo, para la API)

1. Crear la aplicación en developers.mercadolibre.cl con la cuenta de Mercado Libre de quien la registre, y obtener el identificador y la clave.
2. Probar una búsqueda en el sitio de Chile (MLC) por palabra clave. El acceso a las búsquedas sin token se ha restringido en los últimos años: hay que probar si sirve con el token y si entrega precio y vendidos.
3. Si la API permite lo que necesitamos, se documenta aquí el endpoint y las condiciones de uso. Si no, seguimos con captura manual.

## Cuenta de vendedor

No se abre ahora. Se decide en la fase de validación (desde el 12-nov), cuando haya un producto que probar; ahí Mercado Libre es canal de prueba, no fuente de datos.
