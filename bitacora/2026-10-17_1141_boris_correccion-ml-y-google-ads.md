---
fecha: 2026-10-17 11:41
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: A1 Demanda / A3 Oferta y precios (corrección tras la auditoría)
estado: en curso
---

# Corrección de raíz de Mercado Libre y Google Ads, y mesa de validación

## Objetivo
Corregir los errores que encontró la auditoría del 16-oct en los scripts de Mercado Libre y Google Ads, atacando la causa (reglas que adivinan desde texto libre) y dejando una forma humana de validar los datos.

## Qué se hizo
- **Diagnóstico común:** los dos errores vienen de lo mismo: el script adivina formato, pack, marca y oportunidad con expresiones regulares escondidas en el código. Se separó en tres capas: crudo (intacto), validación humana (tablas en `datos/referencia/`) y cálculo.
- **`scripts/resumir_captura_mercadolibre.py` reescrito** (comandos `proponer`, `resumir`, `probar`):
  - Separa las 35 filas de cold brew pegadas en el crudo de hidratante (se marcan "contaminada", el crudo no se toca) y deduplica por id de publicación.
  - Lee packs ("paquete de 6", "12 latas", "20g x 5un", "80 gr (4 bolsas)", "x30", "30x"), oz, fl oz y lb, e ignora gramos de proteína.
  - Propone clase (objetivo / adyacente / descartar), tipo (sobre, polvo, rtd, concentrado, plato, fruta…) y marca (`datos/referencia/marcas_mercadolibre.csv`, 95 marcas) con su confianza y motivo.
  - Si hay validación humana (`datos/referencia/mercadolibre_validacion.csv`), manda sobre la propuesta.
  - Resumen por término × clase × tipo y por oportunidad (une términos y cuenta cada publicación una vez); lo no capturado queda vacío, no en cero.
  - 11 casos verificados a mano en la auditoría como prueba (`probar`): 11/11 correctos.
- **Mesa de validación** (artefacto privado https://claude.ai/artifact/W6Nvd15kmsRkdYuoSmVT5k): fichas prellenadas, marcas y términos de Google Ads; guarda en la base del artefacto. Copia y flujo en `entregables/2026-10-17_mesa-validacion/`.
- **`scripts/importar_validacion_mercadolibre.py`**: pasa lo validado al repo.
- **Precio corregido** (pedido de Boris): la validación acepta `precio_clp` con nota de por qué. Manda sobre el precio capturado y la captura limpia guarda `precio_original` y `precio_corregido`; el crudo no se toca. Campo agregado en la mesa y en el importador.
- **Líquidos sin precio por unidad** (reportado por Boris): el cálculo exigía gramos cuando el tipo era polvo. Ahora usa la unidad real del producto (ml → CLP/L, g → CLP/kg) en el script y en la mesa; un título con volumen se clasifica como líquido aunque traiga gramos; se ignoran los gramos "por porción". Ej.: QNT 12 × 330 ml pasa de 116.633 CLP/kg a 8.836 CLP/L; leche con proteína 1 L, de 265.556 CLP/kg a 2.390 CLP/L.
- **Medir precio por** (reportado por Boris: ponía porciones y seguía en CLP/L): cada ficha tiene "Medir precio por" (automático según el tipo, porción, o litro/kilo), guardado como `medir_por` en la validación. "Porciones" pasa a ser **porciones por envase** (total = porciones × envases; se quitó la excepción cuando envases = porciones). La mesa muestra también la otra lectura, y la captura limpia trae `precio_por_porcion` y `precio_por_litro_o_kilo`. El resumen agrupa por la unidad elegida.
- **Google Ads:** `scripts/google_ads_terminos.py` arma el diccionario `datos/referencia/google-ads_terminos.csv` (1.517 filas oportunidad × término, con tipo y concepto); `scripts/actualizar_radar_google_ads.py` reescrito: índice específico (variantes colapsadas al máximo), techo del término clave, marca "demasiado amplio", CPC y competencia solo de términos específicos, "no medido" cuando corresponde → `datos/limpios/2026-10-17_google-ads_indice_oportunidades.csv` y columnas nuevas en el radar.
- **Segunda tanda para Mario:** 31 términos de formato y atributo → `datos/referencia/2026-10-17_google-ads_segunda-tanda.csv` (y `_para-pegar.txt`).

## Hallazgos
Propuesta automática, antes de validar (captura del 16-oct, `datos/limpios/2026-10-16_mercadolibre_cl_resumen_oportunidad.csv`); cuadra con el recálculo manual de la auditoría:

| Oportunidad · tipo | Mediana (p25–p75) | Auditoría |
|---|---|---|
| Electrolitos · sobre | 970 CLP/porción (687–1.763), n=48 | 997 (806–1.528) |
| Proteico listo para beber | 10.333 CLP/L (6.360–11.160), n=9 | 9.962 (6.952–11.160) |
| Cold brew · listo | 21.660 CLP/L (16.964–22.609), n=8 | 22.013 (19.502–23.392) |
| Comida liofilizada · plato | 10.490 CLP/plato (7.498–11.990), n=17 | 10.490 (10.490–11.990) |
| Chai · polvo | 32.772 CLP/kg (19.976–60.176), n=24 | 29.125 (17.058–44.936), n=18 |

- Falta precio por unidad en 29 % de los sobres de electrolitos y 56 % del cold brew listo (títulos truncados o "6 unidades" sin volumen): es lo que más aporta la validación.
- Índice de búsqueda específico (sin validar): electrolitos 50, cold brew 51, tofu 50 (techo 75), jugos 33, proteico 29 (techo 50), kimchi 25 (techo 75), chai 8 (techo 50); matcha listo para beber, granola con legumbre, creatina en gomitas y té helado sin azúcar quedan **no medidos**. Coincide con la auditoría.

## Archivos creados o modificados
- `scripts/resumir_captura_mercadolibre.py` — reescrito.
- `scripts/importar_validacion_mercadolibre.py`, `scripts/google_ads_terminos.py` — nuevos.
- `scripts/actualizar_radar_google_ads.py` — reescrito.
- `datos/referencia/marcas_mercadolibre.csv`, `datos/referencia/google-ads_terminos.csv`, `datos/referencia/2026-10-17_google-ads_segunda-tanda*.{csv,txt}` — nuevos.
- `datos/limpios/2026-10-16_mercadolibre_cl_{propuesta.csv,propuesta.json,captura.csv,resumen.csv,resumen_oportunidad.csv}` — regenerados o nuevos.
- `datos/limpios/2026-10-16_google-ads_terminos_para_validar.json`, `datos/limpios/2026-10-17_google-ads_indice_oportunidades.csv` — nuevos.
- `datos/limpios/2026-10-16_radar-oportunidades_boris.csv` — columnas de Google Ads reemplazadas (índice específico, techo, volumen específico).
- `entregables/2026-10-17_mesa-validacion/` — LEEME y copia de la página.

## Decisiones propuestas (para acordar en grupo)
- Usar el **índice específico** de Google Ads (no el nivel del término clave) en la matriz del 28-oct, con "no medido" donde corresponda.
- Las cifras de Mercado Libre que entren a la matriz salen de `..._resumen_oportunidad.csv` después de validar, por tipo de producto.
- Mantener las tres capas (crudo / validación humana / cálculo) para toda fuente nueva (supermercados, reseñas).

## Pendientes y siguiente paso
- [ ] Validar en la mesa: primero electrolitos y proteico; luego cold brew, chai y liofilizada; marcas; términos de Google Ads — Boris.
- [ ] Traer lo validado al repo, re-correr resúmenes e índice, y corregir la columna `senal_mercadolibre` del radar y los JSON del dashboard — Boris (con Claude).
- [ ] Pasar la segunda tanda de términos a Google Ads Keyword Planner — Mario.
- [ ] Corregir la pauta de captura (dice "sin scripts" y se usó un script de consola) cuando Mario cierre la revisión de términos de uso — Mario.

## Contexto para la próxima sesión
El crudo de Mercado Libre no se edita nunca. Para cambiar un dato se valida en la mesa (o se edita `datos/referencia/mercadolibre_validacion.csv`) y se re-corre `resumir`. La clave de cada publicación es `termino~id_pub` (id MLC de la URL, o un hash si no hay URL). La base del artefacto tiene las colecciones `validacion`, `marcas` y `ads`. No se amplió ni automatizó la captura de Mercado Libre.
