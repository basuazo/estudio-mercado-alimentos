---
fecha: 2026-10-16 18:50
persona: boris
agente: Claude desktop
fase: Estudio de mercado · Fase 1
paso_del_plan: A1 Demanda / radar de oportunidades
estado: completado
---

# Radar de oportunidades: señal de búsquedas de Google Ads

## Objetivo
Cruzar los volúmenes de Google Ads (ver `bitacora/2026-10-16_1825_boris_google-ads-keyword-planner.md`) con las 23 oportunidades del radar.

## Qué se hizo
- Script nuevo `scripts/actualizar_radar_google_ads.py`: a cada oportunidad le asigna sus términos de búsqueda, toma el nivel mensual, el CPC alto y la competencia, y agrega tres columnas al final del radar: `termino_clave_google_ads`, `nivel_termino_clave_mes` y `senal_google_ads`. Se puede volver a correr; reescribe esas columnas sin duplicarlas.
- Las columnas existentes (incluidas `n_fuentes`, `estado` y `fecha_actualizacion`) no se tocaron.
- `termino_clave_google_ads` es el término más cercano al producto, elegido a mano. Se separó del término paraguas porque este último infla el nivel (por ejemplo, "electrolitos" 50.000 frente a "electrolitos en sobre" 5.000).

## Hallazgos
- Nivel del término clave (búsquedas mensuales en Chile, por nivel):
  - 5.000: sobres de electrolitos ("electrolitos en sobre"), café o batido proteico ("batido de proteina"), matcha ("matcha latte"), cold brew, leche sin lactosa, té helado, pan de masa madre, chai latte, ginger beer, agua de coco, compra por mayor de bebidas.
  - 500: avena barista, jugos prensados en frío, yogur proteico, comida liofilizada, fruta liofilizada.
  - 50: agua con gas saborizada, snack de garbanzo, productos sin sellos.
  - 50.000 o más: granola, kimchi, tofu, creatina (500.000, pero la oportunidad es solo gomitas y formatos nuevos).
- De las 5 candidatas y listas cortas, ninguna cae bajo 500. Avena barista es la más baja (500) y además tiene competencia alta y CPC hasta 943 CLP.
- Cold brew es la única con competencia baja/media y CPC bajo en el grupo; coincide con Trends (+183 %, base baja).
- "Sin sellos" como búsqueda tiene solo 50 al mes: el atributo existe, pero la gente no lo busca por ese nombre.
- Seis oportunidades que estaban "sin revisar" en Trends (chai latte, comida y fruta liofilizada, ginger beer, agua de coco, compra por mayor) ahora tienen al menos una señal de demanda por búsquedas. Siguen en una fuente por criterio, ya que Google Ads y Trends son de la misma empresa y no se cuentan como fuentes independientes.

## Archivos creados o modificados
- `scripts/actualizar_radar_google_ads.py` — agrega la señal de Google Ads al radar.
- `datos/limpios/2026-10-16_radar-oportunidades_boris.csv` — con 3 columnas nuevas al final.

## Decisiones propuestas (para acordar en grupo)
- No contar Google Ads como una fuente independiente más para el criterio de 3 fuentes (misma plataforma que Trends). Se usa como medida de nivel de demanda.

## Pendientes y siguiente paso
- [ ] Revisar a mano los términos clave elegidos y cambiar los que el grupo vea distintos (están en el diccionario `CLAVE` del script).
- [ ] Llevar la columna `nivel_termino_clave_mes` a la matriz de puntaje del 28-oct.

## Contexto para la próxima sesión
Los volúmenes son niveles redondeados (50, 500, 5.000, 50.000). Una oportunidad con 5.000 y otra con 500 sí difieren en un orden de magnitud; dos con 5.000 no se pueden ordenar entre sí.
