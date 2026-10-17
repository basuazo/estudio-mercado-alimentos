# Auditoría de datos macro e industria (SII + UN Comtrade + distribuidores)

Fecha: 2026-10-16. Alcance: archivos `sii_*`, `un-comtrade_*`, `distribuidores-santiago-nuble`, script `procesar_sii_empresas.py`, bitácoras 1731, 1724 y 13-oct (Chalo), y radar de oportunidades. Solo lectura. Las series completas están en `datos.json`.

**Veredicto:** confiabilidad B, utilidad B. Las cifras reproducen la fuente, pero los titulares de la bitácora (+265 %, +116 %, +69 %, +602 %, +199 %) son engañosos si se usan como señal de demanda. Buena parte se explica por cambio de código (CIIU4.CL 2018), pandemia 2020-21, precio del café y reclasificación arancelaria 2022.

## 1. Inventario y método

| Archivo | Contenido | Observación |
| --- | --- | --- |
| `sii_alimentos_nacional.csv` | 18 actividades × 2015–2024: N° empresas, ventas UF, trabajadores (180 filas) | 3 ventas vacías (107500, 2015-17: reservado) |
| `sii_alimentos_region.csv` | Ñuble y RM, mismas actividades (354 filas) | Ventas de 107901, 110401, 106109 Ñuble 2024 vacías (reservado) |
| `sii_alimentos_resumen.csv` | 2019 vs 2024, ventas/empresa, % Ñuble y RM | Recalculado: coincide al 100 % |
| `sii_nuble_elaboracion_pj.csv` | 206 PJ de Ñuble (sin EIRL), 2024 | 101 panaderías; 48 sin ventas |
| `sii_posibles-maquiladores_pj.csv` | 753 PJ, tramo ≥ pequeña 1, 4 actividades | Ver sección 4 |
| `un-comtrade_..._hs6.csv` | 12 partidas × 2021–2025: CIF, FOB, kg (60 filas) | 4 sin kg |
| `un-comtrade_..._origen-2025.csv` | Top-3 orígenes por partida (36 filas) | Cobertura 39 %–97 % |
| `distribuidores-santiago-nuble.csv` | 31 distribuidores (24 Santiago, 7 Ñuble) | Ver sección 4 |

Método SII: `PUB_ACT.txt` y `PUB_REG_ACT.txt` de `EMPRESAS.zip` (estadística de empresas por actividad, año comercial, cifras preliminares), filtradas a 18 códigos CIIU4.CL de 6 dígitos. La nómina PJ 2024 filtra por nombre de actividad, vigencia (sin término de giro), persona jurídica comercial sin EIRL. El script es correcto y reproducible. Sin RUT por regla del repo. Hay que declarar que la estadística incluye personas naturales y la nómina no (206 PJ en Ñuble frente a 631 empresas en la estadística).

Método Comtrade: API de previsualización pública, una llamada por año, flujo M (importación), reporter Chile (152). Verifiqué una cifra contra la API: 210120 en 2025 = 36.668.549 USD CIF, con `netWgt` nulo, coincide con el CSV. No pude abrir sii.cl ni aduana.cl (bloqueados), así que no verifiqué los tramos de ventas ni la nota metodológica del SII. Lo marco como pendiente.

## 2. Recálculo de las cifras citadas

| Cifra citada | Recalculada | Veredicto |
| --- | --- | --- |
| Comidas preparadas +265 % (2019→24) | 437→1.594 = +264,8 % | Reproduce, pero artefacto: 1, 4, 1 empresas en 2015-17; 78 en 2018. 2022→24: +8,8 % |
| Aguas embotelladas +116 % | 696→1.501 = +115,7 % | Reproduce; 2022→24: -0,3 % (plano) |
| Té/café/infusiones +69 % | 779→1.315 = +68,8 % | Reproduce; 2022→24: +25,6 %; incluye cafeterías |
| Bebidas no alcohólicas +34 % | 269→361 = +34,2 % | Reproduce; 2022→24: +1,4 % |
| 341 mil UF/empresa (bebidas) | 341.190 | Reproduce; promedio arrastrado por pocas grandes (rango 93k–451k según año) |
| 5 mil UF/empresa (té y café) | 5.116 | Reproduce; estable desde 2019 (6,1k) |
| Ñuble 1–2 % | 0,8–1,7 % en 5 actividades emergentes; 2,38 % en toda la elaboración | Cierto solo para actividades de nicho |
| 753 maquiladores | 753 | Es el conteo del filtro, no el universo de maquila |
| Café 210111: 92,5 M, +92 % | 92,45 M; +92 % | Reproduce; volumen +4 %, precio +84 % |
| Proteína 350220: 7,0 M, +602 % | 7,05 M; +602 % | Reproduce; base 1,0 M; kg 2025 sin dato |
| Té 210120: 36,7 M, +199 % | 36,67 M; +199 % | Reproduce; todo el salto ocurre en 2022; desde ahí -12 % |

## 3. Errores y riesgos detectados

**Alta severidad**
1. **Código nuevo en 2018 (107500).** La actividad casi no existía antes de CIIU4.CL. El +265 % mide la migración de códigos, formalización y delivery, no producto envasado. El nombre oficial dice "envasados, rotulados", pero la lista de maquiladores trae restobares, pizzerías y gastronomía bajo 107500. Úsese solo 2022→24 (+8,8 %).
2. **Todas las ventanas 2019→2024 mezclan quiebre de clasificación y pandemia.** Con base 2022 casi todo se aplana: panadería +0,2 %, aguas -0,3 %, bebidas +1,4 %, otros n.c.p. +6,6 %. Solo té/café sigue sobre +12 % anual.
3. **Ventas y trabajadores 2015-2018 no comparables con 2019+.** En 471100 las ventas pasan de 64,7 M UF (2017) a 198 M (2018) y 595 M (2019); los trabajadores de 28,7 mil a 132,8 mil. 107909 baja de 397 M a 106 M UF entre 2017 y 2018. No grafiquen ventas antes de 2019. La UF ya es una unidad indexada a la inflación, por lo que las ventas en UF no requieren deflactar. El problema es el cambio de clasificación y el sesgo por pocas empresas grandes, no la inflación.
4. **107901 incluye cafeterías, heladerías y salones de té.** Hay 46 nombres de este tipo en la lista de 753 (21 en 107901). Parte del +69 % es servicio, no producto envasado.
5. **Lista de 753 "posibles maquiladores".** Sin criterio de capacidad. El 60 % (450) es 107909 n.c.p.; hay 105 empresas de tramo grande (marcas o competidores: Watt's, Evercrisp, Embotelladora Andina, catering), 98 con 0 trabajadores, 56 holdings/catering/liquidación, 146 comercializadoras o distribuidoras, y alimento animal o acuícola (EWOS, Acuícola Alas). Con reglas simples (sin cafeterías, holdings, 0 trabajadores ni grandes) quedan 467; sin comercializadoras, 355. Falsos positivos estimados: 36–53 %. Solo 7 están en Ñuble y 42 en Biobío; 56 % están en la RM.
6. **Café 210111 es efecto precio.** Volumen 2021 3.992 t y 2025 4.155 t (+4 %); USD/kg 12,06 a 22,25. En 2025 el valor sube 56 % y el volumen 18 %.
7. **Quiebre 2021→2022 en tres partidas HS.** 210120: 12,3 a 41,8 M (kg x3,7). 220210: 10,7 a 150,4 M. 220299: 169,4 a 104,5 a 26,6 M. Parece reclasificación (concordancia HS2017→HS2022 o glosa arancelaria chilena); no lo pude confirmar. Combinadas, 220210+220299 pasan de 180 M a 137 M (-24 %). Para 210120 el CAGR 2022-25 es -4,3 %, y 2025 es -18 % frente a 2024.

**Media severidad**
- Ventas de 107500 en 2024 saltan x7,7 (1,77 M a 13,58 M UF) con empresas +4 %. Probable reclasificación o dato preliminar; usar 2023.
- Ñuble "1–2 %" requiere matiz (sección 2). Además el conteo es por domicilio tributario: una planta en Ñuble con casa matriz en RM cuenta en RM. No puedo cuantificarlo con estos archivos; se resuelve con nómina de direcciones o `PUB_COMU_ACT`.
- 350220 tiene base de 1,0 M USD. Concentrados de suero (WPC/WPI) normalmente van en 3504/0404.10, que no se consultaron.
- 210690 (254,5 M USD, plano, 0 % 2021-25) mezcla suplementos, electrolitos y bases de bebida; no permite leer electrolitos. 220299 también.

**Baja severidad**
- Ñuble 471100 = 10,1 %, estable desde 2015, con ventas/empresa de 7,2 mil UF frente a 107 mil nacional (0,7 % de las ventas): son comercios pequeños, no supermercados.
- 4 de 60 filas Comtrade sin peso neto (210111-2023, 210410-2023, 210120-2025, 350220-2025). La API devuelve `netWgt` nulo.
- Orígenes: solo top-3, de 38,7 % (220299) a 97,2 % (190420); 210690 apenas 42,5 %.
- 2025 parece completo: valores de escala similar a 2024 y sin patrón de año parcial, pero Comtrade revisa al alza. Contrastar con DIN mensual de Aduanas.
- Distribuidores: ver sección 4.

## 4. Calidad de listas

**Maquiladores.** Ver errores 5 y la tabla `maquiladores_resumen` del JSON. Recomendación: citar "~350 candidatos tras depuración básica, ~55 % en RM", y sacar 10–15 por palabras clave (polvo, instant, tostad, liofiliz, deshidrat) más llamada. En esa búsqueda de palabras 68 de los 355 calzan, pero el nombre es una señal débil. Ejemplos útiles por perfil: Kombuchacha (Araucanía), Deshidratadora La Paz (Biobío), Procesadora y Extrusora de Alimentos (RM).

**Distribuidores.** 31 filas, 0 duplicados, columnas de nombre, zona, comuna, tipo, categoría, canal, observaciones y fuente completas. Faltan correo en 17 (solo 1 de 7 de Ñuble lo tiene), teléfono en 7 y web en 2 (Mayorista 10 ×2). La fuente es única en 27 de 31 filas, 3 son blogs/agregadores (granloop, portalinnova) y 1 es una noticia. Mezcla clientes grandes (Alvi, Central Mayorista, CCU, Andina) con nichos útiles (Snaqui, Emporio Vive Vegano, Suplementos al Mayor, Bidfood, Cafeteros Chile, Dispack, La Escoba). Es una muestra de conveniencia: hay ~7.700 mayoristas 463019 en el SII.

## 5. Series y mapa a oportunidades

Las series anuales (N° empresas, ventas y ventas/empresa 2015-2024 por actividad, CAGR, peso Ñuble) y las importaciones por partida y año (CIF, kg, USD/kg, CAGR, top-3 orígenes 2025) están completas en `datos.json` (`sii_empresas_anual`, `sii_resumen`, `nuble`, `importaciones_anual`, `importaciones_resumen`, `origenes_2025`). Para gráficos usar 2019+ en ventas y base 2022 en importaciones de 210120, 220210 y 220299.

Resumen por oportunidad (completo en `metricas_por_oportunidad`; 23 filas con el nombre exacto del radar):

| Oportunidad | Actividad SII (var. empresas 2019→24 / 2022→24) | Partida HS (USD 2025; CAGR 2021-25) | Lectura |
| --- | --- | --- | --- |
| Electrolitos | 110401 (+34 % / +1 %) | 210690 (254,5 M; 0 %) | Macro neutra; partida inútil |
| Café/batido proteico RTD | 110401 | 350220 (7,0 M; +63 %) | Insumo; base pequeña |
| Matcha RTD y chai | 107901 (+69 % / +26 %) | 210120 (36,7 M; +32 %) | Inflado por 2022; desde ahí -4 % anual |
| Cold brew | 107901 | 210111 (92,5 M; +18 %) | Precio, no volumen |
| Agua con gas saborizada | 110402 (+116 % / 0 %) | 220210 (98,1 M) | Serie rota; 56 % Austria |
| Tés helados, ginger beer, agua de coco | 110401/110402 | 220299 (38,4 M) | No interpretable |
| Fruta liofilizada | 103000 (+5 % / -8 %) | 200899 (25,7 M; +9,6 %) | Crecimiento real en kg (+44 %) |
| Comida liofilizada | 107500 (+265 % / +9 %) | 210410 (19,8 M; +18 %) | Proxy débil |
| Granola | 107909 | 190420 (0,45 M; -23 %) | Local domina |
| Leche sin lactosa, yogur griego | 105000 (+4 % / -2 %) | 040299 control | Sin señal; oligopolio |
| Avena barista | 106109 (-3 %) | sin HS | Nicho |
| Panadería (masa madre) | 107100 (+30 % / 0 %) | sin HS | Atomizado |
| Mayorista online | 463019 (+42 % / +3 %) | sin HS | Canal grande, atomizado |

Sin partida o actividad útil: jugos prensados, snack de legumbre, kimchi, tofu, productos sin sellos, creatina (cae en 210690).

## 6. Tendencias y ciclos (con advertencias)

- **Estabilización desde 2022.** Elaboración total: 18.551 empresas (2019), 25.941 (2022), 26.553 (2024). +81 % de 2015 a 2022, +2,4 % de 2022 a 2024.
- **Ola de 2020-21.** Aguas pasan de 696 a 1.361 y comidas preparadas de 437 a 1.164 en dos años. Ambas se aplanan después. Es formalización y emprendimientos pandémicos, no necesariamente consumo.
- **Té/café sigue creciendo (+12 % anual 2022-24)** con ventas/empresa planas (~5 mil UF): muchas entradas pequeñas, algunas cafeterías. Es atractivo para microemprendedores y puede ser saturación.
- **Comercio tradicional en retroceso:** almacenes 472101 bajan de 98.087 (2022) a 95.823 (2024); mayoristas no especializados -14 % 2019-24.
- **Importaciones:** el café sube por precio (2025 en máximos); aguas/bebidas combinadas bajan -24 % 2021-25; las alzas reales en volumen están en frutas preparadas (+44 % kg) y sopas (+26 % kg).
- **Concentración:** bebidas no alcohólicas (361 empresas, 341 mil UF) y lácteos (825, 315 mil UF) son oligopolios. Té/café, aguas y comidas son atomizados. Entrar con marca propia en bebidas exige maquila y distribución.
- **Ñuble:** 2,4 % de la elaboración, alto en molinería (7 %) y frutas (6 %), con 101 panaderías entre 206 PJ. Consistente con la tesis agroindustrial de largo plazo, poco con maquila de polvos.
- **Advertencia:** un mayor N° de empresas sin crecimiento de ventas por empresa sugiere categoría fácil de entrar y con presión de precio, no mayor demanda. No usar crecimiento de empresas como evidencia de demanda; tratarlo como señal de competencia y de entrada de emprendedores.

## 7. Próximos pasos recomendados

1. Calcular altas y cierres con `Ciclo_Vida.zip` (natalidad y mortalidad por actividad) para separar dinamismo de saturación.
2. Bajar a 8 dígitos y ampliar partidas (0403, 0404.10, 3504, 2009, 1904/1905, 2008, 2101.20 fina, 220299) desde la DIN de Aduanas, y confirmar la reclasificación 2022.
3. Revisar la lista de maquiladores con las reglas de la sección 3 y priorizar 10–15 a mano.
4. Documentar tramos de ventas (UF) y universo estadística vs nómina en `fuentes-macro-sii-aduanas.md`.
5. Completar distribuidores de Ñuble/Biobío con segunda fuente y contactos.
