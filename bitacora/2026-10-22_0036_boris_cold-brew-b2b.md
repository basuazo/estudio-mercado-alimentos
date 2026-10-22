---
fecha: 2026-10-22 00:36
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: Profundización de una candidata (cold brew), etapa 1 de escritorio
estado: completado
---

# Cold brew B2B: factibilidad de producción, costos, mercado y equipo rojo

## Objetivo
Boris y el grupo ven con buenos ojos el cold brew B2B: concentrado a granel y en botella de 1 L para oficinas y cafeterías de Santiago. Las preguntas eran: ¿se puede producir en cocina o hay que maquilar?, ¿cuánto cuesta? y ¿qué tan viable es la idea de crear el hábito con marketing "push"?

## Qué se hizo
- Tres investigaciones en paralelo con fuentes primarias: regulación e inocuidad, producción (cocinas, maquila, insumos, equipos, rendimiento) y mercado B2B. Además, un equipo rojo independiente.
- Modelo de costos por unidad en script: `entregables/2026-10-22_cold-brew-b2b/modelo_costos.py` → `datos/limpios/2026-10-22_cold-brew_modelo-costos.csv`.
- Informe con la tesis ajustada y la prueba con umbrales: `entregables/2026-10-22_cold-brew-b2b/informe.md`.

## Hallazgos
Fuentes con URL en el informe, capturadas el 2026-10-22.
- **Se puede producir en cocina** con resolución sanitaria (DS 977/96, arts. 6–9 y 12, por establecimiento y giro). Concentrado solo de café y agua, sin sellos. Cadena de frío ≤ 5 °C. Vida útil de **7 días** en bag-in-box o barril y ≤ 10 en botella, hasta tener un estudio de desafío (regla de 10 días de la FSA; Listeria sobrevive en cold brew refrigerado).
- **No hay maquila de café en Chile.** Alta HPP no acepta vidrio y no esteriliza. CoCook cuesta ~575.000 CLP por 48 h al mes, con resolución vigente; falta confirmar si acepta bebidas y el reposo nocturno.
- **Margen bruto:** 44 % en granel con café comercial (costo de 5.067 CLP/L, precio supuesto de 9.000) y 11 % con café de especialidad.
- **Equilibrio** con CoCook más operador: 13 cuentas de cafetería en verano y 45 en invierno. Inversión de ~7,5 MM CLP; el kit nitro cuesta ~690.000 CLP por cuenta.
- **Hueco:** nadie vende bag-in-box ni nitro en Chile, y los servicios de café para oficinas no ofrecen bebidas frías. Briu (13.990 por 1 L) y Tuesta (19.000) solo venden botella.
- **Equipo rojo:**
  - Un bag-in-box de 10 L pierde entre el 45 y el 77 % en una cafetería chica.
  - En invierno la cuenta apenas paga el despacho.
  - Solo el 4 % declara tomar café frío habitualmente (ANDA/CORPA 2025).
  - Hay cierres por la red de frío y por depender de un solo canal (Peet's Coldcraft 2019, Joyride 2020).

## Archivos creados o modificados
- `entregables/2026-10-22_cold-brew-b2b/modelo-costos-cold-brew.xlsx` — modelo editable con fórmulas para los socios (mismos resultados que el script).
- Documento para compartir y comentar (Claude Docs): https://claude.ai/artifact/LTxEyi72819WYCdETXh2yj
- `entregables/2026-10-22_cold-brew-b2b/informe.md` y `modelo_costos.py` — nuevos.
- `datos/limpios/2026-10-22_cold-brew_modelo-costos.csv` — nuevo.
- `estado/boris.md` — actualizado.

## Decisiones propuestas (para acordar en grupo)
- Ajustar la tesis:
  - envase de 3 L y botella de 1 L;
  - primero clientes sin barista (restaurantes, hoteles, coworkings, gimnasios);
  - operadores con frío propio como canal;
  - marca blanca o "toll brewing" como opción;
  - nitro solo con ≥ 40 vasos por semana comprobados.
- Producir al inicio en una cocina con resolución vigente (tipo CoCook), no en un módulo con contrato de 12 meses ni con maquila.
- Correr la prueba de 3–4 semanas **antes de diciembre**, con los umbrales del informe (≥ 6 de 15 cuentas en preventa pagada, ≥ 4 que repiten pedido, ≥ 4 L por semana por cuenta, rendimiento ≥ 3,8 L/kg y ≥ 1 carta de intención de un operador).

## Pendientes y siguiente paso
- [ ] Consulta escrita a la SEREMI RM sobre producir bajo la resolución de una cocina compartida — por asignar.
- [ ] Llamar a CoCook, Uni Kitchens y Cofactory (bebidas, reposo nocturno, precio) — por asignar.
- [ ] Cotizar el estudio de vida útil (SGS, CECTA-USACH, Eurofins) — por asignar.
- [ ] Piloto de rendimiento con 2 kg en una Toddy: L/kg, Brix y pH, sin venta — Boris.
- [ ] 5 entrevistas con restaurantes o coworkings y 2 con servicios de café para oficinas — Mario o Chalo.
- [ ] Precios mayoristas de Briu, Tuesta, Puelo y Kawas — por asignar.

## Contexto para la próxima sesión
- Los supuestos del modelo están al inicio de `modelo_costos.py` (marcados C o S). Para cambiar un escenario, se edita el diccionario `P` y se vuelve a correr.
- Los supuestos más frágiles son la porción de 80 ml, el consumo de 24 L al mes por cafetería en verano, el despacho a 4.000 CLP por visita y la merma del 10 %. El equipo rojo mostró que la merma con bag-in-box de 10 L es mucho mayor: por eso la tesis ajustada usa envases de 3 L.
- El cold brew todavía no está en el dashboard. Si se suma, entra como filas del dataset de oportunidades (regla de no crear pantallas nuevas).
