# Instrucciones para el agente — Company Builder

Trabajas dentro del repositorio compartido de Boris, Mario y Chalo (Gonzalo). Los tres trabajan con agentes de IA (Claude Code, Claude desktop/Cowork u otros) sobre esta misma carpeta, sincronizada con git. Tu trabajo debe dejar rastro para que el agente de la siguiente persona sepa qué se hizo, por qué y qué sigue.

Responde siempre en español de Chile, de forma concisa.

## 1. Al iniciar una sesión (siempre, antes de trabajar)

Cuando la persona diga "inicio", "/inicio", "empecemos" o abra una sesión nueva:

1. **Sincronizar, sin pisar nada.** Si puedes ejecutar comandos: corre `git status`; si hay cambios sin commit, muéstralos y commitéalos primero (con el nombre de la persona), y recién entonces `git pull --rebase`. Si no puedes ejecutar comandos, pídele a la persona que en GitHub Desktop haga **Commit** de lo pendiente (si hay algo en *Changes*) y después **Fetch/Pull** (o `scripts/sync`), y espera su confirmación. Si hay un stash pendiente, revisa su contenido antes de restaurarlo o descartarlo.
2. **Identificar a la persona.** Usa `git config user.name` y la tabla de `EQUIPO.md`. Si no calza, pregunta quién es.
3. **Leer contexto, en este orden:**
   - `CONTEXTO.md` — documento fijo: qué es el proyecto, fase, criterios y reglas de trabajo.
   - Los tres archivos de `estado/` (`boris.md`, `mario.md`, `chalo.md`) y `estado/equipo.md` — en qué está cada uno y qué sigue. Léelos todos, no solo el de la persona.
   - Mientras exista `ESTADO.md` (en desuso desde el 2026-10-13), revisa si alguien lo editó después de esa fecha y avisa para pasar ese cambio a `estado/`.
   - `decisiones.md` — lo acordado por el grupo (no lo contradigas sin decirlo).
   - Las **5 entradas más recientes** de `bitacora/` (orden por nombre de archivo, que empieza con la fecha) y **todas las entradas desde la última sesión de esta persona**.
   - El plan vigente en `plan/` si la tarea toca el estudio de mercado.
4. **Resumir en 5–8 líneas:** qué hicieron los otros desde la última sesión de esta persona, sus pendientes según `estado/<persona>.md`, y cualquier conflicto o duplicación que veas. Luego pregunta qué quiere hacer hoy (o propón el siguiente paso del plan).

## 2. Durante la sesión

- Guarda lo que produzcas en la carpeta que corresponde (ver `README.md` → Estructura). Nombres de archivo en minúsculas, sin espacios ni tildes, con fecha si es una captura: `datos/crudos/2026-10-15_google-trends_proteina.csv`.
- Cada dato o afirmación que venga de una fuente externa lleva su fuente (URL o archivo) y fecha de captura.
- No borres ni reescribas trabajo de otra persona. Si algo está mal, anótalo en la bitácora como observación y propón el cambio.
- No modifiques `decisiones.md` por tu cuenta: las decisiones se proponen en la bitácora y se pasan a `decisiones.md` cuando el grupo las acuerda (normalmente en `/integrar`).
- Escribe **solo en archivos de la persona con la que trabajas**: su `estado/<persona>.md`, sus entradas de bitácora, sus datos y entregables. No edites `estado/` de otros ni archivos compartidos (`CONTEXTO.md`, `estado/equipo.md`, `decisiones.md`, `CLAUDE.md`) salvo en la integración o por acuerdo. Así dos personas nunca cambian el mismo archivo y git no genera conflictos ni stash.
- Nada de datos personales de terceros, claves, tokens ni archivos pesados (audios, videos, fotos > 5 MB) en el repositorio: van a Drive y aquí se enlazan.

## 3. Al cerrar una sesión o terminar un paso del plan

Cuando la persona diga "cierre", "/cierre", "terminamos" o complete un paso:

1. **Escribir la entrada de bitácora** con la plantilla `plantillas/entrada-bitacora.md`, en `bitacora/AAAA-MM-DD_HHMM_persona_tema-corto.md` (hora local de Chile, persona en minúsculas: `boris`, `mario`, `chalo`). Una entrada por sesión. Debe poder leerse sola, sin la conversación.
2. **Actualizar `estado/<persona>.md`**: en qué está, qué terminó, qué sigue, y si está bloqueada por alguien.
3. **Listar decisiones propuestas** en la entrada (no en `decisiones.md`).
4. **Verificar** que los archivos nuevos estén en su carpeta y que no haya archivos pesados o sensibles.
5. **Commit → Pull → Push, en ese orden.** Si puedes ejecutar comandos: `git add -A`, `git commit -m "<persona>: <tema> (<paso del plan>)"`, `git pull --rebase`, `git push`. Si no puedes (o el push pide credenciales), entrega el mensaje de commit listo y pide a la persona que en GitHub Desktop haga **Commit to main**, luego **Pull origin** si aparece, y luego **Push origin** (o `scripts/cierre`).
6. Si `git pull --rebase` da conflicto: nunca descartes cambios ajenos. Explica el conflicto a la persona en palabras simples y resuélvelo conservando ambas versiones cuando sea texto de bitácora o estado.

## 4. Integración (semanal o antes de cada reunión)

Cuando alguien pida "/integrar" o "integración":

1. `git pull --rebase` y leer todas las entradas de `bitacora/` desde la última integración (`bitacora/*_integracion.md`).
2. Escribir `bitacora/AAAA-MM-DD_HHMM_<persona>_integracion.md` con: avances por persona, hallazgos que se cruzan, duplicaciones, decisiones propuestas pendientes de acordar, riesgos, y una propuesta de próximos pasos por persona.
3. Actualizar `estado/equipo.md` y, si corresponde, la fase y "Dónde estamos" en `CONTEXTO.md`.
4. Las decisiones propuestas se pasan a `decisiones.md` solo después de que el grupo las confirme; deja la lista lista para revisar en la reunión.

## 5. Reglas generales

- La bitácora es de solo agregar: no edites entradas pasadas salvo para corregir un error evidente, y anótalo al final de esa entrada.
- Prefiere archivos Markdown y CSV (legibles por personas y agentes) sobre formatos binarios.
- Si una tarea no calza con el plan vigente, dilo y pregunta antes de avanzar.
- Si no estás seguro de algo, márcalo como "por confirmar" en vez de inventarlo.
- Si GitHub Desktop o git muestran un stash o un conflicto: no descartes nada. Revisa qué contiene cada versión, explícalo en palabras simples y combina conservando el trabajo de ambos.
- No subas archivos de prueba ni generados por programas (`.Rhistory`, `.RData`, etc.).
