---
fecha: 2026-10-16 17:31
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: A4 Datos macro (SII) — tarea de Chalo adelantada con autorización de Boris
estado: completado (primera pasada)
---

# Bases del SII: empresas de alimentos y bebidas en Chile, Ñuble y RM

## Objetivo
Procesar las bases del SII que Chalo dejó listadas (`datos/referencia/fuentes-macro-sii-aduanas.md`): cuántas empresas hay por actividad de alimentos, cómo crecen, cuánto pesa Ñuble y quiénes podrían maquilar.

## Qué se hizo
- Boris descargó a mano `EMPRESAS.zip` (estadísticas 2005–2024, act. nov-2025) y `PUB_EMPRESAS_PJ_2020_A_2024.zip` (nómina de personas jurídicas, act. ene-2026) en su carpeta Descargas; no se suben al repositorio.
- Script `scripts/procesar_sii_empresas.py`: filtra 18 actividades (10 de elaboración, 4 mayoristas y 4 minoristas) y genera 5 tablas en `datos/limpios/`.
- **Códigos de actividad confirmados** contra `PUB_ACT.txt` (pendiente de Chalo): el SII usa 6 dígitos; 1104 se divide en 110401 (bebidas no alcohólicas) y 110402 (aguas embotelladas); 1079 en 107901 (té, café, mate e infusiones) y 107909 (otros n.c.p.); 1075 es 107500 (comidas preparadas envasadas y rotuladas).

## Hallazgos
Fuente: SII, Estadísticas de empresas por actividad (año comercial 2024, cifras preliminares) → `datos/limpios/2026-10-16_sii_alimentos_resumen.csv`.
- **Elaboración que más crece en número de empresas (2019→2024):** comidas preparadas envasadas 437 → 1.594 (+265 %); aguas embotelladas 696 → 1.501 (+116 %); té, café e infusiones 779 → 1.315 (+69 %); otros alimentos n.c.p. 2.593 → 4.289 (+65 %); bebidas no alcohólicas 269 → 361 (+34 %). Lácteos (+4 %) y frutas y hortalizas (+5 %) están planos.
- **Concentración:** en bebidas no alcohólicas la venta promedio es de 341 mil UF por empresa (pocas y grandes); en té y café, 5 mil UF (muchas y pequeñas). Es más fácil entrar en té/café/infusiones que en bebidas embotelladas.
- **Ñuble pesa poco en elaboración:** 0,8 % a 1,7 % de las empresas de té y café, comidas preparadas, bebidas y otros n.c.p.; algo más en frutas y hortalizas (6,1 %) y molinería (7,2 %). La RM concentra el 39–43 %.
- **Ñuble aparece con el 10 % de los supermercados (471100)**, muy sobre su peso en otras actividades: dato raro, por revisar (puede ser una diferencia de clasificación).
- **Personas jurídicas vigentes de Ñuble que elaboran alimentos o bebidas (2024, sin EIRL):** 206 → `datos/limpios/2026-10-16_sii_nuble_elaboracion_pj.csv`. La mayoría son micro o sin ventas; destacan Orafti Chile (Pemuco, grande, inulina) y algunas pequeñas en helados, masas y aguas (Las Vertientes, Chillán).
- **Posibles maquiladores en el país** (personas jurídicas vigentes, tramo pequeña o mayor, en bebidas no alcohólicas, té y café, comidas preparadas y otros n.c.p.): 753, 62 % en la RM → `datos/limpios/2026-10-16_sii_posibles-maquiladores_pj.csv`. Es una lista para filtrar, no para contactar en bloque.

## Archivos creados o modificados
- `scripts/procesar_sii_empresas.py` — procesamiento reproducible.
- `datos/limpios/2026-10-16_sii_alimentos_nacional.csv`, `..._region.csv`, `..._resumen.csv`, `..._sii_nuble_elaboracion_pj.csv`, `..._sii_posibles-maquiladores_pj.csv`.
- `datos/referencia/fuentes-macro-sii-aduanas.md` — pendientes actualizados.
- `estado/chalo.md` y `estado/boris.md`.

## Decisiones propuestas (para acordar en grupo)
- Usar el crecimiento del número de empresas como señal de "categoría que atrae entrantes" (té/café/infusiones, comidas preparadas), no como demanda.
- Las listas de empresas excluyen EIRL y no guardan RUT, por la regla de no subir datos personales de terceros.

## Pendientes y siguiente paso
- [ ] Chalo: revisar el dato de supermercados en Ñuble (471100) y si conviene sumar las nóminas 2015–2019 para ver nacimientos y cierres.
- [ ] Boris o Chalo: de la lista de maquiladores, marcar 10 a 15 que hagan bebidas en polvo, café o té y que sirvan para las candidatas (electrolitos, café proteico, cold brew).
- [ ] Integración: cruzar con importaciones (UN Comtrade) y radar.

## Contexto para la próxima sesión
Para repetir: dejar los .zip en `datos/crudos/sii/` (ignorados por git) y correr `python scripts/procesar_sii_empresas.py`, o pasar las rutas como argumentos. El SII mezcla codificaciones (UTF-8 y Latin-1) y formatos numéricos según el archivo; el script lo resuelve. "*" = dato reservado.
