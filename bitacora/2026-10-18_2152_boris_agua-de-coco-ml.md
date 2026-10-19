---
fecha: 2026-10-18 21:52
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: A3 Oferta y precios (Mercado Libre)
estado: completado
---

# Captura de agua de coco en Mercado Libre agregada al procesamiento y a la mesa

## Objetivo
Sumar la captura de agua de coco del 18-oct (`datos/crudos/2026-10-18_mercadolibre_cl_agua-de-coco.csv`) al procesamiento de tres capas y a la mesa de validación.

## Qué se hizo
- `scripts/resumir_captura_mercadolibre.py`:
  - Término nuevo **agua de coco** (oportunidad "Agua de coco" del radar): objetivo = agua de coco lista para tomar; adyacentes = con gas (sparkling) y mezclas (aloe, colágeno, limonada, saborizada); descartar = otros productos de coco (aceite, leche, crema, rallado, laminado, dulce).
  - **Contaminación por etiqueta**: el archivo traía 123 filas, 64 de ellas del chai del 16-oct (etiqueta `chai-latte`). Ahora se separan como "contaminada" cuando la etiqueta nombra otra búsqueda, aunque la otra captura sea de otra fecha. El crudo no se toca.
  - Packs "24-pack" y "6-pack" (con guion) se leen bien; 2 casos nuevos de prueba: 13/13 correctos.
  - `proponer` junta todas las fechas en una sola propuesta para la mesa; la fecha de cada fila es la del nombre del archivo (la columna `fecha` del crudo dice 2026-10-19, en UTC).
  - El término se toma del nombre del archivo sin espacios sobrantes.
- `datos/referencia/marcas_mercadolibre.csv`: 15 marcas nuevas (B Organics, Natures Charm, Dr. Fruit, Vita Coco, Coco do Vale, Sococo, Copra, Andina Grains, entre otras).
- `datos/crudos/2026-10-16_mercadolibre_cl_bebida-chai-latte .csv` (con un espacio antes de .csv, contenido idéntico al original) se devolvió a su nombre: git lo veía como borrado.
- Mesa de validación republicada con 458 publicaciones (8 términos) y el vendedor visible cuando la captura lo trae.

## Hallazgos (propuesta automática, sin validar; captura 18-oct)
- 59 publicaciones de agua de coco: 31 objetivo, 14 adyacentes, 14 descartadas (aceite, leche de coco, laminado, isotónicas Purihydra que aparecieron en la búsqueda).
- Agua de coco lista para tomar: mediana **5.064 CLP/L** (p25–p75 4.490–7.673), n=29, 8 marcas; top-3 = 69 % de las publicaciones (B Organics domina, también vendida por Andina Grains). Mínimo 2.499 CLP/L (Coco do Vale, caja 12 × 1 L). Solo 3 % con envío gratis.
- Por revisar en la mesa: "Agua De Coco 330ml Natural B Organics" a 9.900 (30.000 CLP/L, probable pack sin cantidad en el título) y "Pack 4u" y "Pack 3x" de B Organics sin volumen.
- La captura trae vendedor en 32 de 123 filas: primera vez que hay ese dato.
- La función de consola volvió a arrastrar la búsqueda anterior (chai) al archivo nuevo, igual que el 16-oct con cold brew. La guía 05 ya propone dejar la consola; si se sigue usando, hay que recargar la página entre búsquedas.

## Archivos creados o modificados
- `scripts/resumir_captura_mercadolibre.py`, `datos/referencia/marcas_mercadolibre.csv`.
- `datos/limpios/2026-10-18_mercadolibre_cl_{captura,resumen,resumen_oportunidad,propuesta}.csv`, `..._propuesta.json` (todas las fechas).
- `datos/limpios/2026-10-16_mercadolibre_cl_*.csv` regenerados (sin cambios de cifras salvo los ajustes de cálculo del 17-oct).
- `entregables/2026-10-17_mesa-validacion/mesa.html`.

## Decisiones propuestas (para acordar en grupo)
- Contar el agua de coco con gas y las mezclas como adyacentes, no como el producto.

## Pendientes y siguiente paso
- [ ] Validar agua de coco en la mesa — Boris.
- [ ] Llevar la señal de Mercado Libre del agua de coco al radar (hoy tiene 1 fuente) al propagar lo validado — Boris (con Claude).

## Contexto para la próxima sesión
Para una captura nueva: guardar `datos/crudos/AAAA-MM-DD_mercadolibre_cl_<termino>.csv`, agregar el término en `TERMINOS` y `OPORTUNIDAD` del script si es nuevo, correr `proponer` (todas las fechas) y `resumir <fecha>`, y subir `..._propuesta.json` a la mesa.
