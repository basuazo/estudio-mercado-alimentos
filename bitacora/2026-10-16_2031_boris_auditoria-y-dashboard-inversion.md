---
fecha: 2026-10-16 20:31
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1 (cierre) → preparación Fase 2
paso_del_plan: Revisión general · auditoría de fuentes A1–A4 y B · insumo para la matriz del 28-oct
estado: completado
---

# Auditoría de todo el estudio de mercado y dashboard de inversión

## Objetivo
Revisar toda la información reunida, auditar su confiabilidad y utilidad, integrarla y construir un dashboard con metodología, advertencias, limitaciones y caminos de mejora para decidir en grupo.

## Qué se hizo
- Inventario completo del repo (contexto, decisiones, plan, 15 bitácoras, datos crudos y limpios, scripts, entregables).
- Cinco auditorías independientes en paralelo (subagentes de Claude), en solo lectura, recalculando desde los crudos: Trends+Meta, Google Ads, Mercado Libre, SII+Comtrade+distribuidores, B3+radar+método. Una sexta investigó fuentes y estrategias de mejora en la web.
- Integración por oportunidad (`build_dash.py`) y dashboard de 8 pantallas: https://claude.ai/artifact/MDjMSTxEXamWJjUeb5mzbH
- Verificación independiente del resultado: 52 cifras recalculadas contra el repo, todas cuadran; se corrigieron 4 reglas o textos de severidad media (señal de demanda con términos proxy, término clave amplio, cobertura que contaba juicio como dato, alerta exagerada) y varios detalles.

## Hallazgos
- Con familias de fuentes independientes, solo 3 de 23 oportunidades cumplen la regla de 3 (café/batido proteico, granola con legumbre, chai); el radar contaba 4. Electrolitos baja a 2 (el B3 no la valida) y matcha listo para beber a 1. → `entregables/2026-10-16_auditoria-y-dashboard-inversion/auditorias/auditoria_metodo.md`
- Regulatorio: el sello ALTO EN aplica solo a nutrientes añadidos (DS 13/2015, art. 120 bis); electrolitos con sodio añadido pueden llevar ALTO EN SODIO. Ruta suplemento vs alimento sin resolver. Mercado Libre mezcla sales de rehidratación (medicamentos) con electrolitos.
- Trends: el "último trimestre" del resumen compara estaciones distintas (proteína +22 % → −0,4 % interanual real); 39 de 100 términos son ruido; deriva común +8,45 %. Electrolitos crece casi al ritmo de la deriva. Crecen sobre la deriva: yogur griego, leche de avena, agua con gas, pan de masa madre, granola, kimchi, matcha, tofu. Agua con gas y agua mineral tienen peak en enero; granola, avena y legumbres en invierno.
- Google Ads: el término clave del radar infla la demanda 1 a 2 niveles en 8 de 23 oportunidades (matcha RTD, chai, proteica RTD, kimchi, tofu, té helado, granola, creatina). Las columnas mensuales vienen vacías (cuenta sin gasto): no hay estacionalidad en Ads.
- Mercado Libre: packs mal normalizados (cold brew importado 18.800–29.200 CLP/L, no 19.000–140.000); archivo de hidratante en polvo contaminado con 35 filas de cold brew; hueco de precio en electrolitos entre 1.300 y 2.000 CLP/porción. Euromonitor (titular gratuito, nov-2025) dice que el café RTD cuesta ganar aceptación en Chile.
- SII/Comtrade: +265 % de comidas preparadas es artefacto de código nuevo; con base 2022 casi todo se aplana salvo té/café (que incluye cafeterías). Extractos de café +92 % es precio (volumen +4 %). Los 753 maquiladores tienen 36–53 % de falsos positivos estimados.
- Fuentes nuevas: Aduanas publica DIN/DUS 2026 en datos.gob.cl (evita el bloqueo de aduana.cl). Sercotec Capital Semilla exige no haber iniciado actividades: no formalizar antes de decidir si se postula.

## Archivos creados o modificados
- `entregables/2026-10-16_auditoria-y-dashboard-inversion/` — LEEME, 5 auditorías, verificación, fuentes y estrategias, datasets JSON, script y copia de la página.
- `bitacora/2026-10-16_2031_boris_auditoria-y-dashboard-inversion.md` — esta entrada.
- `estado/boris.md` — actualizado.

## Decisiones propuestas (para acordar en grupo)
- Contar evidencia por **familias** independientes (búsqueda Google, marketplace, publicidad, benchmark, macro, terreno) y exigir al menos una de terreno para pasar a validación.
- Adoptar la matriz propuesta: filtros previos (ruta regulatoria escrita, capital ≤ CLP 6 M, margen ≥ 40 %, sin cadena de frío, ≤ 8 h/semana por socio) y 8 criterios ponderados; Mario y Chalo puntúan a ciegas con umbrales fijados antes de ver resultados.
- No llevar electrolitos ni café proteico como "lista corta" al 28-oct hasta tener consulta regulatoria y cotizaciones; tratarlos como candidatas a investigar.
- Discutir explícitamente la tensión entre el modelo (sin frío, poco capital) y dónde está el crecimiento de búsqueda (lácteos y refrigerados).

## Pendientes y siguiente paso
- [ ] Compartir el dashboard con Mario y Chalo desde el menú Compartir del artefacto — Boris.
- [ ] Consulta regulatoria escrita (electrolitos y proteína: alimento vs suplemento, sellos con fórmula real) — Mario, 30-oct.
- [ ] Cotizaciones de maquila (3 por candidata) — Chalo, 4-nov.
- [ ] Etnografía mínima (cafeterías, farmacias/tiendas deportivas, minimarkets) — los tres, 4-nov.
- [ ] Exportar ventas de Mayorístico por categoría — Boris, 28-oct.
- [ ] Corregir `resumir_captura_mercadolibre.py` (packs), limpiar el crudo contaminado y `actualizar_radar_google_ads.py` (CPC por término clave) — Boris.
- [ ] Segunda tanda en Google Ads con términos de formato (matcha listo para beber, té helado sin azúcar, chai en polvo, creatina gomitas, granola con legumbres) — Mario.
- [ ] Bajar DIN 2026 de datos.gob.cl y ciclo de vida de empresas del SII — Chalo.

## Contexto para la próxima sesión
El dashboard (artefacto de Claude) se alimenta de los JSON en `entregables/2026-10-16_auditoria-y-dashboard-inversion/datos/`; para actualizarlo, pedir a Claude que lo refresque con las nuevas capturas. Las lecturas preliminares por oportunidad son juicio del auditor y no deben anclar el puntaje a ciegas. Lista completa de errores (68, 19 altos) y limitaciones (38) en la pantalla Auditoría de datos y en `auditorias/`.
