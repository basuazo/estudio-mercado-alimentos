# estudio-mercado-alimentos — repositorio compartido del Company Builder

Carpeta común de Boris, Mario y Chalo. Aquí vive el contexto del proyecto, los datos, los entregables y una **bitácora de sesiones** para que cada uno (y su agente de IA) sepa qué hicieron los demás y pueda seguir desde ahí.

## Cómo funciona en una frase

Antes de trabajar traes los cambios (**pull**), trabajas con tu agente desde esta carpeta, y al terminar el agente escribe tu entrada de bitácora y subes los cambios (**push**).

```
pull  →  "inicio"  →  trabajo con el agente  →  "cierre"  →  push
```

## El flujo de cada sesión

| Paso | Qué haces | Con Claude Code | Con Claude desktop (Cowork) / otra app |
| --- | --- | --- | --- |
| 1. Sincronizar | Traer el trabajo de los demás | El agente hace `git pull` al escribir `/inicio` | GitHub Desktop → **Fetch origin** → **Pull**, o `scripts\sync.ps1` |
| 2. Iniciar | El agente lee el contexto y te resume qué pasó | `/inicio <tema>` | Pegar el texto de `prompts/inicio-sesion.md` |
| 3. Trabajar | Avanzar en un paso del plan | Normal | Normal (con esta carpeta conectada) |
| 4. Cerrar | El agente escribe tu entrada de bitácora y actualiza `ESTADO.md` | `/cierre` | Pegar `prompts/cierre-sesion.md` |
| 5. Subir | Compartir tus cambios | El agente hace commit y push | GitHub Desktop → escribir el mensaje → **Commit to main** → **Push origin**, o `scripts\cierre.ps1 "mensaje"` |

**Antes de cada reunión**, una persona corre `/integrar` (o `prompts/integracion.md`): el agente cruza las bitácoras de los tres y prepara avances, decisiones por confirmar y próximos pasos.

Cierra sesión cada vez que termines un paso del plan, aunque sigas trabajando: entradas cortas y frecuentes son más útiles que una larga.

## Estructura

| Carpeta / archivo | Qué contiene | Quién lo edita |
| --- | --- | --- |
| `CLAUDE.md` · `AGENTS.md` | Protocolo que siguen los agentes | Por acuerdo del grupo |
| `CONTEXTO.md` | Qué es el proyecto y en qué fase está | En cada integración |
| `ESTADO.md` | Tablero: qué hace cada uno y qué sigue | Cada uno **solo su sección** |
| `decisiones.md` | Decisiones acordadas por el grupo | Solo tras acuerdo |
| `EQUIPO.md` | Personas, nombres en bitácora y frentes | Cada uno su fila |
| `bitacora/` | Una entrada por sesión: `AAAA-MM-DD_HHMM_persona_tema.md` | Cada uno las suyas (solo agregar) |
| `plan/` | Plan vigente del estudio de mercado | Por acuerdo |
| `prompts/` | Prompts de inicio, cierre, integración y etnográfico | Cualquiera, avisando en bitácora |
| `plantillas/` | Plantilla de entrada de bitácora | Por acuerdo |
| `datos/crudos/` · `datos/limpios/` | Capturas tal como salen de la fuente / tablas de la base central | Quien captura |
| `etnografia/` | Pautas, notas de campo y codificaciones | Quien hace el trabajo de campo |
| `entregables/` | Informes y presentaciones terminadas | Quien los produce |
| `guias/` | Instructivos para clonar el repositorio y trabajar con Claude | Boris |
| `antecedentes/` | Documentos previos (estructura legal, banco de ideas, exploraciones) | Solo lectura |
| `scripts/` | `configurar` (una vez), `sync` y `cierre` para quien no usa GitHub Desktop | — |
| `config-claude/` · `.claude/` | Comandos `/inicio`, `/cierre`, `/integrar` para Claude Code | Por acuerdo |

Archivos pesados (audios, videos, fotos de terreno) van al **Drive del proyecto** y aquí se enlazan desde la bitácora o la carpeta que corresponda.

## Por qué así no chocamos

- Cada sesión crea **su propio archivo** de bitácora → nunca dos personas editan el mismo.
- En `ESTADO.md` cada uno edita solo su sección → git junta los cambios solo.
- `decisiones.md` cambia solo después de acordar en grupo.
- Siempre **pull antes de empezar** y **push al terminar**.

## Configuración inicial (una vez por persona)

Instructivos detallados, paso a paso y con problemas frecuentes: `guias/01-clonar-repositorio.md` y `guias/02-trabajar-con-claude.md`.

1. Crear una cuenta en [GitHub](https://github.com) y avisarle a Boris el usuario para que te invite al repositorio (privado).
2. Instalar [GitHub Desktop](https://desktop.github.com) e iniciar sesión.
3. Aceptar la invitación al repositorio y, en GitHub Desktop: **File → Clone repository** → elegir `estudio-mercado-alimentos` → elegir dónde guardarlo.
4. Revisar que tu nombre en git calce con `EQUIPO.md` (GitHub Desktop: **File → Options → Git**).
5. Abrir la carpeta con tu agente:
   - **Claude Code:** abrir una terminal en la carpeta y escribir `claude`; luego `/inicio`.
   - **Claude desktop (Cowork):** conectar la carpeta con **Add folder** y pegar el prompt de inicio.
6. Si usas los scripts de PowerShell y Windows los bloquea: `powershell -ExecutionPolicy Bypass -File scripts\sync.ps1`.

## Para Boris: crear y publicar el repositorio (una vez)

1. Abrir PowerShell en esta carpeta y correr:
   `powershell -ExecutionPolicy Bypass -File scripts\configurar.ps1`
   Esto crea el repositorio git, copia los comandos de `config-claude/` a `.claude/` (para `/inicio`, `/cierre` e `/integrar` en Claude Code) y hace el primer commit.
2. En GitHub Desktop: **File → Add local repository** → elegir esta carpeta.
3. **Publish repository** → nombre `estudio-mercado-alimentos` → dejar marcado **Keep this code private** → Publish.
4. En github.com, en el repositorio: **Settings → Collaborators → Add people** → invitar a Mario y Chalo.

Mario y Chalo no necesitan correr `configurar`: al clonar reciben todo, incluida la carpeta `.claude/`.

`config-claude/` es la copia editable de los comandos. Si cambias un comando, cámbialo en ambas carpetas o vuelve a copiarlo.
