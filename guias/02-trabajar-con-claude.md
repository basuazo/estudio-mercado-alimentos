# Instructivo: trabajar con el proyecto desde Claude

**Versión:** 2026-10-10 · Autor: Boris · Doc vivo: https://claude.ai/code/artifact/9b5b54fd-1978-4cdc-a958-412599301102

## La idea en un minuto

Todos trabajamos con un agente de IA sobre la misma carpeta. Al empezar, el agente lee lo que hicieron los demás; al terminar, deja escrita una entrada de bitácora con lo que hiciste. Así nadie depende de la memoria de una conversación y cualquiera puede retomar.

```
pull  →  inicio  →  trabajo  →  cierre (bitácora + estado/<persona>.md)  →  commit → pull → push
```

El paso clave es el **cierre**: sin entrada de bitácora, tu trabajo existe pero nadie (ni su agente) sabe que está ahí.

## Elegir herramienta

Cualquiera de las dos sirve y pueden mezclarse dentro del equipo: el protocolo vive en la carpeta (`CLAUDE.md`), no en la herramienta. Si nunca has usado una terminal, parte con Claude desktop.

|  | Claude desktop (Cowork) | Claude Code |
| --- | --- | --- |
| Cómo se ve | App de escritorio con chat | Terminal (o la app de escritorio en modo código) |
| Qué necesitas | App de Claude para escritorio y un plan que incluya Cowork | Plan Pro, Max, Team o Enterprise ([el plan gratis no incluye Claude Code](https://code.claude.com/docs/en/setup)) y Git instalado |
| Iniciar sesión de trabajo | Pegar el prompt de `prompts/inicio-sesion.md` | Escribir `/inicio` |
| Cerrar sesión de trabajo | Pegar el prompt de `prompts/cierre-sesion.md` | Escribir `/cierre` |
| Pull y Push | Tú, con GitHub Desktop | El agente, automáticamente |
| Mejor para | Leer, redactar, analizar, investigar | Lo anterior + scripts, scraping y manejo de datos |

Antes de seguir, debes tener el repositorio clonado (ver el instructivo para clonar).

## Opción A: Claude desktop

**Una sola vez**

1. Instala la app de escritorio de Claude desde [claude.com/download](https://claude.com/download) e inicia sesión.
2. Abre una tarea nueva de Cowork y usa **Add folder** para conectar tu carpeta `estudio-mercado-alimentos`. Acepta el permiso de acceso que aparece en el computador.

**Cada sesión**

1. **Traer cambios:** en GitHub Desktop, **Fetch origin** y luego **Pull origin** si aparece.
2. **Iniciar:** en Claude, con la carpeta conectada, pega y completa:

```
Inicio de sesión. Lee CLAUDE.md de esta carpeta y sigue el protocolo de inicio.
Soy mario. Hoy quiero trabajar en: A3, términos de uso de supermercados.
```

El agente leerá el contexto y te resumirá qué hicieron los demás y tus pendientes.

3. **Trabajar:** pide lo que necesites (ver ejemplos más abajo). Lo que el agente produzca queda guardado en las carpetas del repositorio.
4. **Cerrar:** cuando termines la sesión o un paso del plan, pega:

```
Cierre de sesión. Sigue la sección 3 de CLAUDE.md: escribe mi entrada de bitácora
con la plantilla, actualiza mi archivo estado/<persona>.md y dame el mensaje de commit.
```

5. **Subir:** en GitHub Desktop, revisa los archivos en **Changes**, pega el mensaje de commit en **Summary**, clic en **Commit to main**, luego **Pull origin** si aparece, y luego **Push origin**.

## Opción B: Claude Code

**Una sola vez**

1. Instala Git (paso 3 del instructivo para clonar).
2. Instala Claude Code ([guía oficial](https://code.claude.com/docs/en/setup)):
   - **Windows (PowerShell):** `irm https://claude.ai/install.ps1 | iex`
   - **Mac (Terminal):** `curl -fsSL https://claude.ai/install.sh | bash`
3. Cierra y vuelve a abrir la terminal, y verifica con `claude --version`.

**Cada sesión**

1. Abre la carpeta del repositorio en la terminal. En GitHub Desktop: **Repository → Open in Command Prompt** (Windows) u **Open in Terminal** (Mac).
2. Escribe `claude`. La primera vez te pedirá iniciar sesión en el navegador.
3. Escribe `/inicio` seguido del tema, por ejemplo: `/inicio A1 tendencias de Google`. El agente hace el pull, lee el contexto y te resume.
4. Trabaja normalmente. Cuando el agente quiera ejecutar comandos o editar archivos, te pedirá permiso: lee y aprueba.
5. Escribe `/cierre`. El agente te muestra la entrada de bitácora, y al aprobarla hace commit, pull y push.

Si `/inicio` no aparece, revisa que exista la carpeta `.claude/commands/` en el repositorio. Mientras tanto, puedes pegar los mismos prompts de la opción A.

## Qué pedirle al agente

Pide resultados concretos y dónde guardarlos; el agente ya conoce el plan y las carpetas. Nombra siempre el paso del plan para que la bitácora quede ordenada.

| Paso del plan | Ejemplo de pedido |
| --- | --- |
| A1 Demanda | “Arma la lista de 40 términos para Google Trends según el plan y una plantilla CSV en `datos/crudos/` para registrar los resultados.” |
| A2 Competencia | “Te paso lo que vi en la Biblioteca de anuncios de Meta. Ordénalo en una tabla de marcas con número de anuncios y antigüedad.” |
| A3 Oferta y precios | “Resume los términos de uso de Jumbo y Líder sobre extracción de datos y propón cómo capturar precios sin infringirlos.” |
| A4 Macro | “Explícame qué tablas del SII y de Aduanas sirven para medir el rubro de snacks y cómo descargarlas.” |
| B Benchmarking | “Aplica el método B3 a estas 15 barras de Mercadona: clasifícalas según si existen en Chile y guarda la tabla en `datos/limpios/`.” |
| C Etnografía | “Usa `prompts/etnografico.md`, módulo entrevista a dueño de minimarket, y prepárame la guía para el sábado.” |
| Análisis | “Con lo que hay en `datos/limpios/`, llena la matriz de puntaje para los candidatos actuales.” |
| Contexto | “¿Qué decidimos sobre la innovación como filtro?” o “¿Qué hizo Chalo esta semana?” |

## Antes de cada reunión: integración

El día de la reunión, una persona (por turnos) integra el trabajo de los tres. Toma 10 minutos y es lo que permite llegar con una agenda clara.

1. Pull, para tener las bitácoras de todos.
2. En Claude Code: `/integrar`. En Claude desktop: pega el texto de `prompts/integracion.md`.
3. El agente escribe una entrada `..._integracion.md` en `bitacora/` con avances por persona, cruces, duplicaciones, riesgos y propuestas de próximos pasos.
4. También actualiza `estado/equipo.md` y prepara la lista de decisiones por confirmar.
5. Commit y push antes de la reunión.
6. En la reunión revisan esa lista. Lo que se acuerde se agrega a `decisiones.md` en la siguiente sesión de quien integró.

## Buenas prácticas

**Haz**

- Cierra sesión cada vez que termines un paso, aunque sigas trabajando: entradas cortas y frecuentes valen más que una larga.
- Revisa la entrada de bitácora antes de subirla: es lo que leerán los demás y sus agentes.
- Pide fuentes: todo dato externo debe quedar con URL o archivo y fecha.
- Si el agente propone una decisión, déjala como propuesta; se confirma en reunión.

**No hagas**

- No edites el archivo `estado/` de otra persona ni sus entradas de bitácora.
- No hagas Pull con cambios sin commit: primero commit, después Pull.
- No subas claves, contraseñas, datos personales de entrevistados ni archivos pesados (audios, videos): van al Drive y se enlazan.
- No borres archivos de otros. Si algo está mal, anótalo en tu bitácora.
- No trabajes varios días sin hacer push: aumenta el riesgo de conflictos.

**¿Y el Proyecto de Claude?**

El Proyecto “Proyecto de Company Builder Social” en claude.ai sirve para conversar ideas y redactar documentos con el contexto general cargado, pero no lee el repositorio ni escribe en él. Regla simple: lo que se decide o produce en el Proyecto se lleva al repositorio en la siguiente sesión con el agente, y el repositorio manda si hay diferencias. Compartir el Proyecto entre los tres depende del plan de Claude que tengan.
