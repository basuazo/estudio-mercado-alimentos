# Instructivo: clonar el repositorio estudio-mercado-alimentos

**Versión:** 2026-10-10 · Autor: Boris · Doc vivo: https://claude.ai/code/artifact/2325242f-906d-4192-b288-0504fbecd233

## Antes de empezar

En unos 20 minutos tendrás en tu computador una copia de la carpeta del proyecto, conectada a GitHub para recibir el trabajo de los demás y compartir el tuyo. Lo haces una sola vez; después solo usas dos botones: **Pull** y **Push**.

**Necesitas:**

- Un computador con Windows o Mac donde puedas instalar programas.
- Un correo para crear tu cuenta de GitHub (puede ser el personal).
- Que Boris ya haya publicado el repositorio y te haya invitado. Si no te llegó el correo de invitación, pídeselo antes de seguir.

**Glosario mínimo**

| Palabra | Qué significa aquí |
| --- | --- |
| Repositorio | La carpeta del proyecto con su historial de cambios. Se llama `estudio-mercado-alimentos`. |
| Clonar | Descargar el repositorio a tu computador, quedando conectado a GitHub. |
| Pull | Traer a tu carpeta los cambios que subieron los demás. |
| Commit | Guardar un paquete de cambios con un mensaje que dice qué hiciste. |
| Push | Subir tus commits a GitHub para que los demás los vean. |

No uses el computador ni las cuentas de tu empleador para este proyecto: todo en equipo y cuentas personales (ver `antecedentes/estructura-legal-company-builder.md`, sección 4).

## Paso a paso

### 1. Crear tu cuenta de GitHub

1. Entra a [github.com/signup](https://github.com/signup) y crea una cuenta gratuita.
2. Activa la verificación en dos pasos cuando GitHub te la pida.
3. Mándale tu **nombre de usuario** de GitHub a Boris por WhatsApp.

### 2. Instalar GitHub Desktop

1. Descarga desde [desktop.github.com](https://desktop.github.com) e instala con las opciones por defecto.
2. Abre GitHub Desktop y elige **Sign in to GitHub.com**. Se abre el navegador: autoriza y vuelve a la app.

### 3. Instalar Git (solo si usarás Claude Code o los scripts)

GitHub Desktop trae su propio Git, pero Claude Code y los scripts de `scripts/` necesitan Git instalado en el sistema. Si solo usarás Claude desktop y GitHub Desktop, sáltate este paso.

- **Windows:** descarga desde [git-scm.com/download/win](https://git-scm.com/download/win) e instala con las opciones por defecto.
- **Mac:** abre la app Terminal, escribe `git --version` y acepta instalar las herramientas de desarrollo si te lo ofrece.

Después abre una terminal (PowerShell en Windows, Terminal en Mac) y deja tu nombre y correo, con el mismo nombre que aparece en `EQUIPO.md`:

```
git config --global user.name "Mario Espinoza"
git config --global user.email "tu-correo@ejemplo.com"
```

### 4. Aceptar la invitación

1. Abre el correo “[GitHub] … invited you to collaborate on estudio-mercado-alimentos”.
2. Haz clic en **View invitation** y luego en **Accept invitation**.
3. La invitación vence en 7 días; si venció, pídele a Boris que la reenvíe.

### 5. Clonar el repositorio

1. En GitHub Desktop: **File → Clone repository**.
2. Pestaña **GitHub.com** → elige `estudio-mercado-alimentos` en la lista.
3. En **Local path** elige una carpeta normal, por ejemplo `Documentos\Proyectos`. GitHub Desktop creará dentro la carpeta `estudio-mercado-alimentos`.
4. Haz clic en **Clone** y espera a que termine.

**Importante:** no clones dentro de una carpeta sincronizada con OneDrive, Google Drive o Dropbox. Dos sistemas sincronizando la misma carpeta generan archivos duplicados y conflictos.

### 6. Revisar tu nombre en GitHub Desktop

- **Windows:** **File → Options → Git**.
- **Mac:** **GitHub Desktop → Settings → Git**.

El nombre debe calzar con tu fila en `EQUIPO.md` (Mario Espinoza, Gonzalo Marquez). Así los agentes saben quién eres al iniciar una sesión.

### 7. Verificar que quedó bien

- [ ] En GitHub Desktop, arriba a la izquierda dice **Current repository: estudio-mercado-alimentos**.
- [ ] La pestaña **Changes** dice “No local changes”.
- [ ] La pestaña **History** muestra el primer commit de Boris.
- [ ] Con **Repository → Show in Explorer** (o **Show in Finder**) ves `README.md`, `CLAUDE.md`, `bitacora/` y las demás carpetas.

Si todo está marcado, sigue con el instructivo para trabajar con el proyecto desde Claude.

## El ciclo de cada día

Regla de oro: **Commit antes de Pull, siempre.** Pull antes de empezar, Push al terminar, y nunca hagas Pull con cambios sin commit. Si usas Claude Code, el agente lo hace por ti con `/inicio` y `/cierre`; con Claude desktop lo haces tú en GitHub Desktop.

**Al empezar**

1. Abre GitHub Desktop. Si la pestaña **Changes** muestra archivos, haz primero **Commit to main** con ellos.
2. Clic en **Fetch origin** (arriba a la derecha).
3. Si el botón cambia a **Pull origin**, haz clic: ya tienes el trabajo de los demás.

**Al terminar** (después de que tu agente escribió la entrada de bitácora)

1. En la pestaña **Changes** revisa la lista de archivos. Debería incluir tu entrada en `bitacora/` y tu archivo `estado/<persona>.md`.
2. Abajo a la izquierda, en **Summary**, pega el mensaje de commit que te dio el agente, por ejemplo `mario: terminos de uso supermercados (A3)`.
3. Clic en **Commit to main**.
4. Si aparece **Pull origin**, haz clic (tus cambios ya están en un commit, así que se combinan solos).
5. Clic en **Push origin**. Listo: tu sesión quedó en GitHub.

## Problemas frecuentes

| Síntoma | Qué pasa | Qué hacer |
| --- | --- | --- |
| `estudio-mercado-alimentos` no aparece en la lista al clonar | No aceptaste la invitación o entraste con otra cuenta | Acepta la invitación (paso 4) y revisa la cuenta en **Options → Accounts** |
| “Repository not found” | La invitación no llegó o venció | Pídele a Boris que te invite de nuevo |
| Aparece el aviso *Unable to pull when changes are present* con **Stash Changes and Continue** | Hiciste Pull con cambios sin commit en un archivo que otro también cambió | Elige **Stash Changes and Continue** y después, en **Stashed Changes**, **Restore**. Nunca **Discard** sin revisar. Para que no vuelva a pasar: commit antes de Pull |
| Aparece **Resolve conflicts** al hacer Pull | Otra persona cambió las mismas líneas que tú | No borres nada. Abre tu agente y pídele: “resuelve el conflicto de git conservando ambos cambios” |
| GitHub Desktop muestra archivos cambiados que no tocaste | Diferencias de fin de línea entre Windows y Mac | No los subas; avísale a Boris |
| PowerShell no deja correr los scripts | Política de seguridad de Windows | Usa `powershell -ExecutionPolicy Bypass -File scripts\sync.ps1` |
| `git` no se reconoce en la terminal | Git no está instalado en el sistema | Haz el paso 3 y vuelve a abrir la terminal |
| Subiste algo por error (clave, archivo pesado) | El historial de git lo guarda | Avisa de inmediato a Boris; no basta con borrarlo en un commit nuevo |

Cualquier otra duda: anota lo que ves (o una captura) y mándalo al grupo antes de intentar arreglarlo a la fuerza.
