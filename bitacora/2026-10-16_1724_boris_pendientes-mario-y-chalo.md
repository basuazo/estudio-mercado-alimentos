---
fecha: 2026-10-16 17:24
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: A3 Oferta y precios (términos de uso, distribuidores) · A4 Macro (Comtrade, SII) · A1 (Google Ads)
estado: en curso (SII y Google Ads necesitan una acción manual)
---

# Adelanto de pendientes de Mario y Chalo

## Objetivo
Boris pidió dejar de tratar las tareas como exclusivas y avanzar también lo pendiente de Mario y Chalo en el estudio de mercado. Mario y Chalo revisan y validan lo hecho.

## Qué se hizo
- **Términos de uso por sitio (Mario):** primera pasada de términos y robots.txt de Mercado Libre, Jumbo, Santa Isabel, Líder, Unimarc y Tottus, con veredicto y forma de captura por sitio → `datos/referencia/terminos-de-uso-por-sitio.md`.
- **Google Ads (Mario):** lista de términos ampliada de 100 a 114 con las señales de Mercado Libre, e instructivo paso a paso → `guias/04-google-ads-keyword-planner.md`. No se pudo correr: requiere cuenta de Google Ads.
- **Farmacia Mont (Mario):** búsqueda web y en un espejo de datos de Mercado Público. Resultado abajo.
- **Distribuidores (Chalo):** 31 distribuidores y mayoristas con contacto corporativo público y fuente (24 Santiago, 7 Ñuble) → `datos/referencia/2026-10-16_distribuidores-santiago-nuble.csv`.
- **UN Comtrade (Chalo):** importaciones de Chile 2021–2025 en 12 partidas y principales orígenes 2025, vía la API pública de previsualización (sin clave; una llamada por año) → `datos/crudos/2026-10-16_un-comtrade_importaciones-chile_hs6.csv` y `..._origen-2025.csv`. Dos cifras verificadas directamente contra la API (210111-2025 y 350220-2024).
- **SII (Chalo):** la página de estadísticas se puede leer, pero la descarga de `EMPRESAS.zip` está bloqueada desde el entorno del agente (403 del proxy). Queda para descarga manual.

## Hallazgos
- **Términos de uso** (2026-10-16): Mercado Libre **prohíbe expresamente** robots y scraping (términos para desarrolladores, secc. 7.6) y pide autorización para publicar métricas derivadas como precios promedio (secc. 5.4). El robots.txt de **Líder** excluye búsqueda, supermercado y catálogo para todos los bots. **Jumbo, Santa Isabel y Tottus** quedan en zona gris (sin cláusula sobre bots; robots.txt permite fichas de producto). **Unimarc** no se pudo abrir. Regla propuesta: captura manual en todos por ahora; si se automatiza, solo Jumbo, Santa Isabel y Tottus respetando robots.txt.
- **Importaciones** (UN Comtrade, CIF USD, 2025 y variación 2021→2025):
  - 210111 extractos y concentrados de café: 92,5 M (+92 %; +56 % solo en 2025), desde Brasil, Colombia y Corea. Señal de consumo de café soluble y concentrado (incluye cold brew concentrado, pero la partida es amplia).
  - 350220 proteína de suero: 7,0 M (+602 %), 68 % desde EE.UU. Acompaña la señal de proteína.
  - 210120 extractos de té y preparaciones (chai, matcha latte): 36,7 M (+199 %), 46 % desde China.
  - 210410 preparaciones para sopas: 19,8 M (+92 %), 65 % EE.UU.
  - 210690 preparaciones n.c.p. (donde entran electrolitos en polvo y suplementos): 254,5 M, plano (+0 %); partida demasiado amplia para leer electrolitos.
  - 220299 y 220210 cambian de forma brusca en 2022 (probable reclasificación HS2022): leerlas juntas.
- **Farmacia Mont:** no aparece por nombre en la web ni en mercadopublico.decidechile.cl. Existe una "Farmacia Montt" en Francisco Ramírez 33, Chillán (buscafarma.cl), probablemente la misma, sin cadena aparente. mercadopublico.cl está bloqueado para el agente. Para saber si vende al Estado hace falta su RUT. Fuente: https://buscafarma.cl/farmacias-de-turno/nuble/chillan
- **Distribuidores más útiles para un producto nuevo:** Snaqui y Emporio Vive Vegano (aceptan marcas pequeñas saludables), Suplementos al Mayor (electrolitos y proteicos), Bidfood y Cafeteros Chile (cafeterías, cold brew), y en Ñuble Dispack y La Escoba (vendedores en terreno). Alvi y Central Mayorista sirven como referencia de precio a almacenes. SMU cerró la marca Mayorista 10 (dic-2025).

## Archivos creados o modificados
- `datos/referencia/terminos-de-uso-por-sitio.md` — veredicto y forma de captura por sitio.
- `datos/referencia/2026-10-16_distribuidores-santiago-nuble.csv` — 31 distribuidores con fuente.
- `datos/referencia/terminos-busqueda.csv` — 14 términos nuevos (101–114).
- `datos/crudos/2026-10-16_un-comtrade_importaciones-chile_hs6.csv` y `..._origen-2025.csv` — importaciones.
- `guias/04-google-ads-keyword-planner.md` — instructivo.
- `estado/mario.md` y `estado/chalo.md` — tareas marcadas como adelantadas, con autorización de Boris.

## Decisiones propuestas (para acordar en grupo)
- Adoptar la regla de captura por sitio de `terminos-de-uso-por-sitio.md` (manual por ahora; nunca automatizar Mercado Libre ni Líder).
- No publicar precios promedio de Mercado Libre hasta resolver la secc. 5.4.
- Usar las importaciones como señal de apoyo, no como fuente independiente, cuando la partida es amplia (210690, 220299).

## Pendientes y siguiente paso
- [ ] **Boris (manual):** descargar `EMPRESAS.zip` y `PUB_EMPRESAS_PJ_2020_A_2024.zip` del SII en `datos/crudos/sii/` (los .zip no se suben). Después el agente los procesa (rubros de alimentos, Ñuble y RM).
- [ ] **Boris o Mario (manual):** cuenta de Google Ads y planificador según `guias/04-google-ads-keyword-planner.md`.
- [ ] Mario: validar términos de uso; abrir a mano mercadolibre.cl y Unimarc.
- [ ] Mario o Boris: conseguir el RUT de Farmacia Montt y buscarla en Mercado Público.
- [ ] Chalo: revisar la lista de distribuidores y completar Ñuble (saludables y cafeterías); abrir a mano las bases mensuales de Aduanas (aduana.cl, bloqueado para el agente).

## Contexto para la próxima sesión
mercadopublico.cl, aduana.cl y la descarga de archivos de sii.cl están bloqueados para el agente; comtradeapi.un.org funciona vía lectura web (no por curl). Para repetir Comtrade: `https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=152&period=AAAA&cmdCode=HS6&flowCode=M&partnerCode=0`, un año por llamada.
