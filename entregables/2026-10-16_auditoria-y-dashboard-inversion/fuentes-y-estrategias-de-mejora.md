# Mejoras al estudio de mercado: fuentes y estrategias (16-oct-2026)

Objetivo: llegar a la decisión del 11-nov con evidencia más sólida. Detalle completo y campos estructurados en `fuentes_estrategias.json` (34 fuentes, 14 estrategias). Todo lo marcado "parcial" o "no" abajo no se pudo abrir hoy.

## Hallazgos que cambian el plan

1. **Aduanas sí es accesible por otra puerta.** datos.gob.cl publica los registros de importaciones (DIN) y exportaciones (DUS) 2026, con Importaciones actualizado el 30-sep. Evita el bloqueo de aduana.cl. Falta probar la descarga de los archivos y confirmar el nivel de detalle arancelario.
2. **Google Trends tiene API en alfa** (5 años, valores consistentes, subregiones). Hay que postular; el acceso es limitado. Mientras tanto, términos de control en el sitio web.
3. **Kantar Worldpanel ahora es "Worldpanel by Numerator".** Buscar con ambos nombres. Lo gratuito son solo titulares en prensa. NIQ aparece igual (nota del 3-oct sobre marcas propias: café +33,2% en valor).
4. **Euromonitor "RTD Coffee in Chile" (nov-2025): titular gratis dice que el café RTD cuesta ganar aceptación en Chile.** Informe completo cuesta USD 1.195. Es una señal contraria para la candidata café/batido RTD; contrastar con evidencia local.
5. **Corfo: no hay convocatorias abiertas.** El calendario del 2-oct muestra todas cerradas (Crea y Valida 2026 cerró el 4-ago). Sercotec Capital Semilla Emprende exige **no haber iniciado actividades de primera categoría en el SII**: no formalizar antes de decidir si se postula.
6. **Espacio Food & Service 2026 ya pasó** (29-sep a 1-oct). Sirve su listado de expositores como directorio.
7. **Ruta regulatoria:** no hay categoría propia de suplementos; se tratan como alimento salvo ingredientes o claims farmacológicos (fuentes secundarias). No encontré una calculadora oficial de sellos ni un listado ISP. Las cifras de trámite SEREMI ($12.100 a $899.700 + 0,5% del capital, 30 días hábiles) vienen de un sitio comercial y la ficha oficial de ChileAtiende no abrió: confirmar antes de usar.

## Fuentes por prioridad (resumen)

**Prioridad 1 (hacer ya)**
- Aduanas DIN/DUS en datos.gob.cl: https://datos.gob.cl/organization/servicio_nacional_de_aduanas (verificado; descarga sin probar)
- Google Trends API alfa: https://developers.google.com/search/apis/trends?hl=es-419 (verificado)
- NIQ vía prensa: https://g5noticias.cl/2026/10/03/marcas-propias-mantienen-una-participacion-relevante-en-supermercados-durante-el-primer-semestre-de-2026/ (verificado)
- DF, alto en proteínas: https://www.df.cl/empresas/consumo/alto-en-proteinas-la-oferta-crece-casi-600-en-chile-desde-2020-y-las (verificado; solo datos de PedidosYa)
- MINSAL, reglamento de etiquetado (DS 977 act., DS 13/2015): https://www.minsal.cl/reglamento-de-la-ley-de-etiquetado-de-alimentos-descarga/ (verificado)
- ChileAtiende, autorización sanitaria: https://www.chileatiende.gob.cl/fichas/ver/172 (URL de buscador; no abrió)
- Suplementos en Chile: https://www.artixio.com/post/food-supplement-regulations-compliance-chile (verificado, fuente secundaria)
- CPM Foods / LiquidHub, maquila de bebidas en Quilicura: https://cpmfoods.cl/ (verificado; mínimos no publicados)
- Calendario Corfo 2026: https://www.corfo.gob.cl/sites/cpp/convocatorias_programas_innovacion/ (verificado)

**Prioridad 2**
- SII ciclo de vida (descarga la hace un socio): https://www.sii.cl/sobre_el_sii/estadisticas_inicio_de_actividades.html
- BCCh Demografía de empresas: https://www.bcentral.cl/contenido/-/detalle/lanzamiento-dae
- INE EPF IX (alimentos y bebidas no alcohólicas 21,2% del gasto; $307.947/mes por hogar; datos 2021-22)
- INE IPC (para deflactar; PDF no abierto)
- Worldpanel by Numerator vía prensa: https://www.pauta.cl/economia/2025/12/22/hogares-en-chile-ajustan-su-consumo-alimentos-concentran-el-50-del-gasto.html
- Euromonitor ficha RTD coffee: https://www.euromonitor.com/rtd-coffee-in-chile/report
- USDA FAS Retail Foods Annual (ventas retail alimentos ~US$28.500 M en 2023; supermercados 53,6%): https://www.fas.usda.gov/data/chile-retail-foods-annual
- MINSAL manual de etiquetado 2017 (PDF no abierto)
- Pmatch.cl (artículo 2023; no sé si sigue activo)
- TikTok Creative Center (solo se abrió la página de ayuda)
- Sercotec Capital Semilla Emprende 2026: $3,5 M, aporte 3%

**Prioridad 3 (contexto o bajo calce):** BCCh Monitor de Comercio Exterior, WITS, IAC INE, índice de ventas de supermercados CNC, SERNAC y ODEPA (foco en frescos), ENCA 2010-11, CeTA (líneas piloto marinas/charcutería, sin bebidas), UBB Chillán (contacto académico), Start-Up Chile (base tecnológica), Pollfish (sin precio verificado), Meta Ad Library (solo comenta un tercero), memorias de SMU/Cencosud/Walmart (no se encontraron). Descartados: Maquila Chile (solo cápsulas) y Embotelladora Capri (es de Colombia).

**No verificado:** Trade Map (ITC), Cadem Plaza Pública, SurveyMonkey Audience, Fondo FIC regional Ñuble, calendario Corfo 2027, fechas de la próxima ronda de Capital Semilla, directorio de socios Chilealimentos.

## Estrategias (ordenadas por impacto en la decisión)

| # | Estrategia | Brecha | Costo aprox. | Plazo | Resp. |
|---|---|---|---|---|---|
| 1 | Pre-registro de umbrales y puntaje ciego | sesgo del equipo | $0 | umbrales hasta 26-oct; puntaje 5 a 8-nov | grupo |
| 2 | Triangulación por 6 familias de fuentes (3 familias, no 3 fuentes) | regla de 3 fuentes | $0 | 30-oct | Boris |
| 3 | Trends con términos de control, regional y API alfa | estacionalidad | $0 | 20 a 28-oct | Chalo |
| 4 | Tamaño de mercado Fermi top-down y bottom-up con rangos | tamaño y sell-out | $0 | hasta 6-nov | Boris |
| 5 | Aduanas datos abiertos: oferta importada y competidores | tamaño, costos | $0 | hasta 3-nov | Chalo |
| 6 | Prueba de humo (landing + Meta/Google, mismo gasto por candidata) | demanda primaria | ~$300.000 | lanzar 22-oct; cerrar 4-nov | Mario |
| 7 | Etnografía mínima (12-15 entrevistas + 6-8 tiendas) | voz del consumidor y canal | ~$80.000 | hasta 5-nov | grupo |
| 8 | Cotización estándar a 5 maquiladores y cascada de margen | costos y márgenes | $0 | hasta 6-nov | Mario |
| 9 | Ruta regulatoria: consulta SEREMI y tabla de sellos | regulación | ~$250.000 (si hay asesoría) | hasta 6-nov; respuesta SEREMI incierta | Chalo |
| 10 | Serie de precios retail semanal (23-oct, 30-oct, 6-nov) | serie de precios | ~$40.000 | 3 puntos nuevos | Boris |
| 11 | Cohortes SII y BCCh de altas y cierres | demanda B2B, saturación | $0 | hasta 3-nov | Mario |
| 12 | Van Westendorp con muestra propia | precio y voz | $0 (panel pagado por cotizar) | hasta 6-nov | Boris |
| 13 | Prensa de sell-out y ventas propias de Mayorístico.cl como proxy | sell-out | $0 | alertas hoy; datos 30-oct | Boris |
| 14 | Fondos: orden de formalización y calendario 2027 | fondos | $0 | 6-nov | Boris |

## Límites y supuestos a tener presentes

- Los montos en CLP son estimaciones mías; los de paneles pagados y asesoría legal no están cotizados.
- Los umbrales (CTR, costo por lead, tamaño de muestra) son prácticas habituales, no valores verificados en una fuente; deben fijarse y registrarse antes de mirar resultados.
- Con ~26 días hasta el 11-nov, la serie de precios solo logrará 3-4 puntos: sirve para dispersión y promociones, no para tendencia.
- Si no se consigue la respuesta de la SEREMI antes del 11-nov, declarar la clasificación de los sobres de electrolitos como riesgo abierto, no como resuelta.
