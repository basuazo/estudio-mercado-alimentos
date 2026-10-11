> Copia del documento `claude/estructura-legal-company-builder.md` del Proyecto de Claude "Proyecto de Company Builder Social", tomada el 2026-10-10. Solo lectura: la versión viva está en el Proyecto.

# Estructura legal del Company Builder — decisiones y fundamentos

**Fecha del análisis:** 3 de septiembre de 2026 · **v2** (corregida por el perfil real de los socios)
**Documento vivo (artifact):** https://claude.ai/code/artifact/22feaa1a-129e-44a7-8713-465f92283a74

## Supuestos del caso (confirmados por Boris)

- 3 socios, **todos titulados**, con **≈10 años de experiencia laboral cada uno**. Capital inicial muy bajo.
- Dedicación **mixta**: los tres con **empleo formal vigente** en paralelo.
- **Bootstrapping** por ahora; no hay ronda de VC a la vista en 12–18 meses.
- Rubros abiertos, foco en **sostenibilidad de forma sistemática** en sus distintas dimensiones. Se asume que tarde o temprano habrá un rubro con riesgo operacional real y/o regulado.

### Qué cambió respecto de la v1 (perfil de estudiantes)

1. **La SRL de profesionales pasó de nota al pie a decisión real** — exención de IVA 19% disponible ahora, con la opción de primera categoría (ver §1 y §6).
2. **Apareció un riesgo nuevo que no existía: sus contratos de trabajo vigentes** (art. 160 N°2 CT y presunción de PI del empleador). Nueva §4.
3. **El régimen transparente 14 D N°8 quedó descartado sin matices** — la utilidad atribuida se apila sobre sus sueldos.
4. **Tienen patrimonio personal real** → avales, régimen patrimonial y separación de cuentas dejan de ser teóricos (§5).

## Decisión central

Una sola **SpA** constituida gratis en el Registro de Empresas y Sociedades, en régimen **Pro Pyme General (art. 14 D N°3 LIR)**, que opera todos los proyectos como divisiones internas con nombres de fantasía. Pacto de accionistas firmado el mismo mes. Filiales solo al cruzar gatillos de riesgo/escala. Nada en Delaware hoy.

| Decisión | Contenido |
|---|---|
| Vehículo | SpA (Ley 20.190). Admite accionista único → filiales 100% de la matriz sin socio de paja. Cesión privada de acciones. Series, acciones reservadas, autocartera. |
| Arquitectura | Un RUT ahora; filializar por gatillos. Cada filial vacía cuesta $500.000–$1.400.000/año. |
| Régimen | 14 D N°3: 12,5% IDPC hasta año comercial 2027, base de caja, PPM a la mitad. Transparente descartado. |
| IVA | SRL de profesionales exenta = opción real, pero solo si buena parte de los clientes no recupera el 19%. Decidir con 2 meses de cotizaciones reales. |
| Riesgo nuevo | Contratos de trabajo vigentes. Leerlos antes de constituir. |
| Extranjero | No. Diseñar para que el *flip* sea barato después. |
| Activos | Marcas, dominios, código y contratos a nombre de la matriz; filiales bajo licencia con royalty. |
| Prioridad de gasto | Pacto de accionistas > marca del holding > contabilidad ordenada. |

## §1 Tipos societarios

- **SpA — elegida.** Cesión de acciones sin escritura pública; máxima flexibilidad estatutaria; admite un accionista; autocartera (permite recomprar al socio que se va sin que otro socio ponga plata).
- **SRL.** Ceder derechos sociales exige unanimidad + escritura pública + inscripción → fatal para vesting. Como matriz, descartada.

### La SRL de profesionales: decisión real, no nota al pie

Requisitos (todos se cumplen con el perfil actual): SRL o colectiva civil (la SpA **no** califica), todos los socios personas naturales tituladas, profesiones idénticas/afines/complementarias, todos ejerciendo efectivamente su profesión para la sociedad, giro **exclusivamente** de servicios profesionales, inscripción en el Registro de Sociedades de Profesionales del SII.

**Hallazgo clave:** una sociedad de profesionales puede **optar por declarar en primera categoría y mantener la exención de IVA**. Circular SII N°50 de 2022: quedan comprendidos los ingresos de las sociedades de profesionales del art. 42 N°2 «aun cuando hayan optado por declarar sus rentas de acuerdo con las normas de la primera categoría». Eso abre la combinación **IVA exento + Pro Pyme 12,5% + diferimiento**, en lugar de atribución anual al IGC de tres personas con sueldo.

**La pregunta que decide: ¿los clientes recuperan el IVA?**
- Cliente contribuyente de IVA → recupera el crédito, la exención no le ahorra nada, y ustedes pierden el derecho a recuperar el IVA de sus propias compras. **Pérdida neta.**
- Cliente que NO recupera (sector público, municipios, ONG, fundaciones, cooperación internacional, entidades exentas, personas naturales) → el 19% es margen real o precio 19% más bajo. En licitaciones públicas de sostenibilidad, decisivo.

**Regla:** si >50% de los ingresos de consultoría vendrá de clientes que no recuperan IVA, se paga sola. Si la mezcla es principalmente corporativa, quedarse con la SpA facturando con IVA.

**No decidir ahora.** Cotizar 2 meses y mirar el dato. Postergar no quema la opción: una SRL constituida después no arrastra historia de facturación afecta a IVA (confirmar con contador).

**Costos de tener ese segundo vehículo:** no puede ser filial del holding (socios personas naturales) → cuarto RUT al lado de la matriz; el fee que le cobre la matriz va con IVA y la SRL exenta no lo recupera (costo muerto — mantenerlo acotado); giro exclusivo sin excepciones (nada de productos, licencias ni reventa); rigidez de equity (sin vesting ni pool ahí — eso vive en la SpA); si deja de cumplir un requisito hay que informar al SII el último día del mes o quedan excluidos del registro, y perder la calidad = perder la exención de inmediato (Res. Ex. N°82 de 2024).
- **S.A. cerrada.** Directorio obligatorio (mín. 3), junta ordinaria anual, memoria. Sobrecarga innecesaria hoy.
- **EIRL.** Descartada: un solo titular persona natural.
- **C-Corp Delaware — etapa posterior.** Costo estatal mínimo ~US$275/año (franchise tax US$175 + annual report US$50 + registered agent) pero el costo real es cumplimiento: Form 1120 anual, Form 5472 por accionista extranjero ≥25% y por operaciones con relacionados, con multa de **US$25.000** por año y entidad; contabilidad US$1.000–3.000/año. Además, si la matriz fuera extranjera y los 3 son residentes chilenos, aplican las reglas de rentas pasivas de entidades controladas del exterior (**art. 41 G LIR**): tributan en Chile por rentas devengadas aunque no se distribuyan. El *flip* (holdco extranjera arriba de la chilena) cuesta US$15.000–40.000 y se hace cuando el inversionista lo exija; aportar acciones chilenas a la holdco puede generar renta gravada y tasación (art. 64 Código Tributario). Excepción: aceleradora que exija la C-Corp como condición.

## §2 Arquitectura: fase 0 → fase 1

**Fase 0 (hoy): un solo RUT.** Proyectos como divisiones internas con nombres de fantasía informados al SII. Razones:
- Cada RUT extra = contabilidad $40.000–120.000/mes + F29 en cero + inicio de actividades + patente municipal + DJ anuales.
- **En Chile no hay consolidación fiscal.** Dentro de un mismo RUT la pérdida del proyecto que falló rebaja la utilidad del que funcionó; con filiales, cada pérdida queda atrapada en su RUT. En fase de experimentación es un subsidio cruzado legítimo entre apuestas.
- Riesgo asumido: no hay muro de responsabilidad. Mitigación: no comprar activos arrendables, seguro de RC cuando un proyecto atienda público, y no experimentar en rubros riesgosos desde el RUT común.

**Los 6 gatillos para filializar** (cualquiera basta):
1. Riesgo operacional real (alimentos, transporte, obra, salud, custodia de dinero de terceros, importación) → filial **antes** de la primera operación.
2. Actividad regulada / requiere permiso → filial con giro único.
3. Contratación de personal propio.
4. Capital o socio externo solo en ese proyecto.
5. Deuda o contratos de largo plazo.
6. Escala: P&L propio positivo y sostenido.

Regla: filializar cuando el costo esperado de no hacerlo supere los ~$1,5M anuales de mantener el RUT.

**Fase 1 (target):** Matriz SpA (holding + servicios compartidos) dueña del 100% de cada filial SpA. La matriz cobra **fee de servicios compartidos** + **royalty por licencia de marca y PI**.

> **Trampa crítica:** para ser Pyme del art. 14 D se requiere capital efectivo inicial ≤85.000 UF, ingresos promedio 3 años ≤75.000 UF y **rentas pasivas ≤35% de los ingresos brutos del giro** — donde "pasivas" incluye expresamente la tenencia de acciones y derechos sociales. Una matriz que solo recibe dividendos tiene 100% de ingresos pasivos, pierde la calidad de Pyme y cae al art. 14 A (semiintegrado, 27% con crédito parcial). El fee de servicios reales lo evita: le da ingresos operacionales, sube utilidades vía gasto deducible en la filial, y es lo que hace un company builder de todos modos. Requiere contrato escrito, precio de mercado y facturación efectiva (operaciones entre relacionados, tasables por el SII).

**Holdings personales por socio:** todavía no, pero por otra razón. Con 10 años de trabajo cada uno sí hay patrimonio que proteger — pero **un holding personal no protege de nada de lo que está en juego aquí**. Lo que protege es la personalidad jurídica de la SpA, filializar antes de tomar riesgo, y no firmar avales. El holding personal sirve para diferir impuestos sobre dividendos y ordenar un evento de liquidez; hoy no hay ni dividendos ni liquidez. Anotar para esa fase.

## §3 Pacto de accionistas — 12 cláusulas obligatorias

> **Requisito formal:** los pactos entre accionistas relativos a cesión de acciones deben depositarse en la compañía a disposición de los demás accionistas y su referencia **anotarse en el registro de accionistas**; si no, se tienen por no escritos frente a la sociedad. Un pacto guardado en un Drive no impide que la sociedad registre el traspaso a un tercero.

1. **Vesting inverso con cliff.** 4 años, cliff 12 meses, mensual después. Acciones emitidas al 100% desde el día 1 + opción de compra irrevocable a favor de la sociedad a valor nominal sobre lo no consolidado + prenda sobre esas acciones. Aceleración *double trigger*. Con dedicación mixta: horas semanales por socio, y **suspensión del vesting** si baja del umbral >2 meses sin acuerdo escrito.
2. **Dedicación, exclusividad y anexo de excepciones.** Horas mínimas por socio; anexo firmado donde cada uno declara **su empleador actual, su cargo** y sus proyectos y compromisos preexistentes (lo que no está en el anexo, no está autorizado); no captación de clientes ni equipo; no competencia 12–24 meses post-salida. *Nota:* una no competencia entre **accionistas**, con contraprestación y alcance acotado, tiene mucho mejor pie en Chile que una no competencia post-contractual laboral (libertad de trabajo). Redactar como pacto comercial. Se completa con las salvaguardas de §4.
3. **Good leaver / bad leaver.** Good: conserva lo consolidado, recompra a valor de mercado o fórmula. Bad (abandono, competencia, dolo): pierde lo no consolidado, recompra de lo consolidado con descuento fuerte. **Definir la fórmula de valorización hoy.**
4. **Drag along.** Umbral = dos socios que sumen más de dos tercios. Si se fija en 75%, cualquiera bloquea toda venta futura.
5. **Tag along.** Proporcional y en las mismas condiciones.
6. **Derecho preferente / primera oferta + prohibición de gravar o prendar acciones.**
7. **Deadlock escalonado:** (i) 15 días de negociación; (ii) mediación con tercero **nombrado en el pacto** y reemplazante; (iii) compra forzada tipo sobre cerrado; (iv) arbitraje ante centro determinado, árbitro arbitrador o mixto. Nunca "tribunales ordinarios". Complemento: **lista corta de materias de supermayoría** (emitir acciones, endeudarse sobre X, vender activos, abrir/cerrar filiales, sueldos de socios, dividendos, cambio de giro, partes relacionadas); todo lo demás mayoría simple.
8. **Cesión de PI anticipada y total** + anexo de PI preexistente. La ley de PI presume titularidad del empleador solo para **trabajadores dependientes**; un socio sin contrato de trabajo no está cubierto → sin cláusula, el código del socio es suyo y el logo del freelancer es del freelancer. Regla operativa: nadie escribe código ni entrega diseño sin cesión firmada (socios, practicantes, freelancers).
9. **Oportunidades corporativas** — la cláusula más importante para un company builder: toda idea en el ámbito de la sostenibilidad se ofrece primero al holding; si el holding la rechaza por escrito en plazo, el socio queda libre.
10. **Reglas de dinero antes de que haya dinero:** política de dividendos (cero reparto hasta umbral de caja), financiamiento de aportes futuros, y **qué pasa si un socio no puede seguir aportando** (dilución con fórmula predefinida). **Sueldos:** mientras los tres tengan su renta principal afuera, nadie cobra sueldo del holding (con base de caja y 12,5%, cada peso que no sale se reinvierte barato; un sueldo obliga a cotizaciones desde el primer mes). Definir en cambio *el momento* en que se empieza a pagar y **quién cobra primero si el primero en dejar su trabajo es uno solo**.
11. **Pool de talento:** acciones de pago reservadas para emisión futura en estatutos. Estructura limpia: **1.000.000 de acciones autorizadas — 300.000 por socio + 100.000 reservadas (10%)**.
12. **Adhesión obligatoria** de todo nuevo accionista al pacto como condición del traspaso + confidencialidad.

## §4 Trabajo en paralelo — el riesgo que trajeron consigo (NUEVA en v2)

Tres personas con década de trayectoria y empleo formal vigente están empezando *desde adentro* de tres empresas que tienen contratos firmados con ellos. Es el riesgo más subestimado y el único que puede materializarse antes de facturar el primer peso.

**Art. 160 N°2 Código del Trabajo:** el empleador puede terminar el contrato **sin derecho a indemnización alguna** por «negociaciones que efectúe el trabajador dentro del giro del negocio y que hubieren sido prohibidas por escrito en el respectivo contrato». Requiere las dos cosas: prohibición escrita + actividad dentro del giro. Los tribunales la aplican con laxitud y parte de la jurisprudencia acepta perjuicio **potencial**, sin daño consumado. Con años de antigüedad, lo que está en juego por socio son varios sueldos.

**PI del empleador:** la ley presume que el titular del software creado por **trabajadores dependientes** es el empleador. Ellos SÍ son trabajadores dependientes — de otra empresa. Si un socio desarrolla algo dentro de sus funciones o del giro de su empleador, ese empleador tiene argumento sobre el activo. Titularidad discutida = inversionista que se baja o venta que se cae años después.

**Las cinco salvaguardas:**
1. **Leer los tres contratos esta semana, antes de constituir.** Buscar: prohibición de negociar en el giro, exclusividad, cesión de PI (y su amplitud), no competencia post-contractual.
2. **Separación física y digital absoluta desde el día 1.** Nada del holding con equipo, cuenta, correo, red, licencia ni tiempo del empleador. Historial de commits, metadatos y logs son prueba en ambas direcciones.
3. **Autorización escrita donde el solape sea real.** Incómodo una vez y barato; el juicio es caro y largo.
4. **No ocultarlo.** El registro de sociedades es público y buscable por RUT. Ocultar convierte un problema contractual manejable en un problema de lealtad y buena fe.
5. **Cláusula de indemnidad entre socios en el pacto.** Si el empleador de uno reclama titularidad sobre lo que ese socio aportó, ese socio mantiene indemnes a los otros dos y a la sociedad.

**Consecuencia sobre el vesting:** la dedicación va a cambiar cuando alguien deje su trabajo, y no lo harán al mismo tiempo. Definir en el pacto qué pasa con el vesting y el sueldo del primero que salte.

## §5 Protección de activos

Principio: **los activos viven en la matriz, el riesgo vive en las filiales.** Licencia escrita, revocable, con royalty de mercado.

- **Marcas:** a nombre de la matriz, nunca de un socio. Registrar ahora solo la del holding, en las clases que usan (35 gestión/consultoría de negocios y 42 servicios tecnológicos y desarrollo de software cubren el núcleo de servicios). No registrar marcas de ideas no validadas; buscar disponibilidad gratis en la base de INAPI antes de gastar en logo. **Registrar el nombre de la sociedad NO da derechos de marca** — error clásico y caro.
- **Dominios:** titular = RUT de la sociedad; cuenta administrativa en correo institucional, **nunca** el Gmail personal de un socio; renovación automática y contratación a varios años. El .cl del proyecto se compra al validar la idea.
- **Código y datos:** organización de repositorios del holding; cesión de PI antes del primer commit; **depósito voluntario del software** en el registro de propiedad intelectual (barato, da fecha certera).
- **Contratos con clientes:** ceder el entregable específico y **retener expresamente** metodologías, plantillas, código base y herramientas reutilizables. Sin eso, cada proyecto de consultoría regala el activo escalable.
- **Ley 21.719 de protección de datos: vigencia plena el 1 de diciembre de 2026.** Agencia de Protección de Datos y multas de hasta miles de UTM. Si algún proyecto maneja datos personales: base legal, registro de actividades de tratamiento, respuesta a solicitudes en 30 días, notificación de brechas en 72 horas. Período inicial más benigno para empresas pequeñas. **Asignar responsable de datos entre los 3.**

### Patrimonio personal (ahora sí existe)

- **No firmar avales ni fianzas personales.** La advertencia más importante para alguien con casa y ahorros: un aval personal en un arriendo comercial, línea de crédito o leasing desarma toda la estructura en una firma. Negociar garantía acotada o boleta de garantía antes que aval solidario ilimitado; si igual hay que firmarlo, decisión de los tres.
- **Declarar el régimen patrimonial en el pacto.** Si alguno está casado en sociedad conyugal, las acciones adquiridas a título oneroso durante el matrimonio quedan comprometidas con el patrimonio común → complica transferencias, recompra por bad leaver y liquidación. Veinte minutos con el abogado hoy.
- **Separar cuentas desde el primer peso.** Mezclar fondos personales y sociales es el argumento más usado para pedir el levantamiento de la separación patrimonial.

## §6 Costos (UTM $71.721 · UF $40.877 al 3-sep-2026)

| Partida | Costo |
|---|---|
| Constitución SpA en el portal | $0 |
| Firma Electrónica Avanzada | $6.000–20.000 c/u al año |
| Alternativa: firma ante notario en el portal | ≈ $32.700 (0,26 UF + 0,18 UF por compareciente; 0,80 UF con 3 socios) |
| Escritura pública con estatutos a medida | $150.000–300.000 |
| Inicio de actividades y facturación electrónica SII | $0 |
| **Pacto de accionistas revisado por abogado** | **$150.000–400.000 — única partida donde no ahorrar** |
| Contabilidad mensual por RUT | $40.000–120.000/mes |
| Patente municipal primer año | $50.000–200.000 (según comuna y capital declarado) |
| Marca INAPI por clase | 3 UTM ≈ $215.000 (1 UTM al presentar + 2 UTM al conceder) + Diario Oficial |
| Dominio .cl | $10.000–15.000/año |
| Segundo vehículo: SRL de profesionales | $0 constitución + $40.000–120.000/mes de contabilidad (cuarto RUT) |

### Régimen tributario

- **Elegido: Pro Pyme General, art. 14 D N°3.** IDPC **12,5%** para años comerciales 2025–2027 y **15% desde 2028** (Ley 21.755, condicionado al calendario de cotización previsional de la Ley 21.735; la tasa permanente del régimen es 25%). **PPM rebajado a la mitad** (0,125% al iniciar actividades) hasta enero de 2028. **Tributación sobre base de caja** (ingresos percibidos menos egresos pagados) — no se paga impuesto por facturas no cobradas. Contabilidad simplificada y depreciación instantánea.
- **Descartado sin matices: Pro Pyme Transparente, art. 14 D N°8.** Con tres sueldos profesionales, **la utilidad atribuida se apila sobre la renta de cada uno** y tributa a su tasa marginal de IGC, muy por encima del 12,5% corporativo — impuesto personal a pagar con plata que la empresa no entregó. Además: **pierden el diferimiento** (tributan aunque reinviertan) y **bloquea la arquitectura** (una filial cuyo dueño es una sociedad no puede estar en el transparente). No reabrir.
- **Si van por la SRL de profesionales: optar por primera categoría.** Por defecto tributa en segunda categoría con atribución a los socios — el peor escenario para este perfil. La opción de primera categoría permite 12,5% Pro Pyme con diferimiento manteniendo la exención de IVA (Circular 50/2022). **Confirmar con el contador:** si la opción es irrevocable y en qué plazo se ejerce, y que la sociedad califique efectivamente para Pro Pyme.

### Tres detalles de ejecución

- **Capital bajo y en muchas acciones.** El capital de la SpA debe pagarse en el plazo estatutario o se reduce de pleno derecho a lo aportado; además la patente municipal se calcula sobre el capital declarado. Capital simbólico en 1.000.000 de acciones.
- **Objeto social lo más amplio posible** — la línea más importante del estatuto: inversión y participación en toda clase de sociedades, desarrollo e incubación de negocios, productos y servicios de cualquier naturaleza, asesorías y servicios de gestión, adquisición y explotación de bienes muebles e inmuebles, y toda otra actividad lícita que los accionistas acuerden.
- **Cotizar siempre con IVA incluido.** Desde 2023 los servicios están afectos al 19% por regla general. Única salida estructural: la sociedad de profesionales de §1.
- Desde el día 1: **todas las facturas de gastos al RUT de la sociedad** (notaría, marcas, dominios, software, hosting, contabilidad, computador).

## §7 Plan de acción — 7 días

**Días 1–2 · antes de tocar ningún portal — leer los contratos de trabajo y firmar el acuerdo de una página**
- **Primero: los tres contratos de trabajo.** Una hora, los tres juntos, buscando las cuatro cláusulas de §4. Puede cambiar todo lo que viene después.
- Porcentajes: tercios iguales con vesting (el vesting corrige la desigualdad de esfuerzo; el porcentaje inicial no).
- Dedicación: horas semanales comprometidas por socio, con nombre y número + anexo de proyectos preexistentes.
- Roles y representante legal, con límite de monto para obligar a la sociedad solo.
- Nombre y objeto amplio. Verificar el nombre en 3 lugares: base de marcas de INAPI, dominio .cl, registro de sociedades.
- Los 3 con Clave Única activa; decidir FEA o firma ante notario (esto es lo que traba la semana).

**Días 3–4 · formalización**
- Constituir en registrodeempresasysociedades.cl: capital bajo en 1.000.000 de acciones (300.000 por socio + 100.000 reservadas), objeto amplio, administración acordada.
- Inicio de actividades en el SII marcando **Pro Pyme General 14 D N°3**; habilitar facturación electrónica gratuita.
- **Empezar la apertura de cuenta bancaria de inmediato** — es lo más lento para una sociedad sin historia.
- Comprar el dominio a nombre del RUT, crear correo institucional y organización de repositorios.

**Días 5–7 · blindaje**
- Firmar el pacto ante notario, depositarlo en la sociedad y **anotar su referencia en el registro de accionistas**. Abrir el registro de accionistas.
- Firmar las 3 cesiones de PI con anexo de PI preexistente y de empleador actual, más la cláusula de indemnidad de §4.
- Montar la separación digital: equipo, cuentas, correo y repositorios del holding aparte de los del empleador de cada uno.
- Presentar la marca del holding en INAPI (1 UTM por clase ahora).
- Agendar revisión del abogado corporativo; si las horas no alcanzan, priorizar vesting, bad leaver y deadlock.

**Lo que NO hacer esta semana:** ninguna filial; nada en Delaware; **no crear todavía la SRL de profesionales**; ninguna marca ni dominio de proyectos que son ideas; no comprar activos arrendables ni contratar personal; no declarar capital alto "para verse serios"; **no renunciar a ningún trabajo** (la estructura está diseñada para que no haga falta).

**Los 2 meses siguientes — decisiones diferidas a propósito:**
1. **Mezcla de clientes → SRL de profesionales, sí o no.** Registrar cada cotización con una columna: ¿este cliente recupera IVA? Al segundo mes la decisión se toma sola.
2. **Umbral de sueldo y qué pasa con el primero que deje su trabajo.** Conversación agendada, con el pacto abierto.
3. **Régimen patrimonial y acuerdo de no firmar avales personales sin decisión conjunta.**
4. **Ley 21.719** antes del 1 de diciembre, si algún proyecto va a tocar datos personales.

## Pendientes / a validar

- Validar estatutos y pacto con abogado corporativo chileno antes de firmar.
- Validar con contador: interacción entre fee de servicios compartidos, límite del 35% de rentas pasivas y elección de régimen.
- Confirmar con el contador la entrada en régimen del **registro de beneficiarios finales** creado por la Ley 21.713 (administrado por el SII).
- Redactar el borrador del pacto de accionistas (no hecho aún).
- **Revisar §4 con un abogado laboral**, no solo corporativo: alcance real de las cláusulas de los tres contratos vigentes y redacción de la indemnidad entre socios.
- Confirmar con contador: irrevocabilidad y plazo de la opción de primera categoría para la sociedad de profesionales, y su elegibilidad Pro Pyme.

## Fuentes oficiales verificadas (3-sep-2026)

- [SII · Circular 53 de 2025 — tasas IDPC y PPM Pro Pyme](https://www.sii.cl/normativa_legislacion/circulares/2025/circu53.pdf)
- [SII · Requisitos del régimen Pro Pyme y límite de rentas pasivas](https://www.sii.cl/preguntas_frecuentes/declaracion_renta/001_140_7530.htm)
- [SII · IVA en la prestación de servicios y exención de sociedades de profesionales](https://www.sii.cl/destacados/iva_prestacion_servicios/)
- [SII · Exención de IVA a las sociedades de profesionales](https://www.sii.cl/preguntas_frecuentes/iva_servicios_profesionales/001_320_8311.htm) y criterio de la Circular 50/2022 sobre la opción de primera categoría
- [Art. 160 N°2 Código del Trabajo — despido por negociaciones incompatibles](https://derechopedia.cl/Despido_por_negociaciones_incompatibles)
- [Registro de Empresas y Sociedades · Aranceles notariales](https://www.registrodeempresasysociedades.cl/AyudaTarifasNotariasles.aspx)
- [INAPI · Tasas de solicitud y registro de marcas](https://www.inapi.cl/preguntas-frecuentes/marcas)
- [SII · Valor de la UF, septiembre 2026](https://www.sii.cl/valores_y_fechas/uf/uf2026.htm)
