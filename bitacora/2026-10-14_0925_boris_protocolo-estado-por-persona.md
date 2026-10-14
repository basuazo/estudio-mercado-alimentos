---
fecha: 2026-10-14 09:25
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 0
paso_del_plan: Protocolo de trabajo (git y estructura de contexto)
estado: completado (propuesta para acordar)
---

# Estado por persona y regla "commit antes de pull"

## Objetivo
Evitar los stash y conflictos de GitHub Desktop que tuvo Mario el 13-oct, y separar el contexto fijo del estado de cada persona.

## Qué se hizo
- `ESTADO.md` se dividió en `estado/boris.md`, `estado/mario.md`, `estado/chalo.md` (cada uno lo edita solo su dueño) y `estado/equipo.md` (solo en la integración). Se copió el contenido vigente de cada sección, incluida la de Chalo del 13-oct.
- `ESTADO.md` queda con un aviso de "en desuso" y sin borrar. Así el commit pendiente de Mario, que cambia su sección, se combina sin conflicto. Se borra en la próxima integración, después de pasar el cambio de Mario a `estado/mario.md`.
- `CONTEXTO.md` queda como documento fijo: visión, fase, criterios y una sección nueva "Cómo trabajamos", con qué documento es qué y la regla de git.
- `CLAUDE.md`: al iniciar, el agente commitea lo pendiente antes del pull y lee `CONTEXTO.md` y los tres archivos de `estado/`. Al cerrar, actualiza solo `estado/<persona>.md` y sigue el orden Commit → Pull → Push. Nunca descarta un stash sin revisarlo.
- Comandos `/inicio`, `/cierre` y `/integrar`, prompts, `README.md` y guías actualizados. Las guías agregan una fila de problemas frecuentes para el aviso de stash.
- `scripts/sync` y `scripts/cierre` usan `git pull --rebase --autostash`.
- `.gitignore` ignora los archivos de R (`.Rhistory`, `.RData`, `.Rproj.user/`).

## Hallazgos
- El stash aparece cuando alguien hace Pull con cambios sin commit en un archivo que otro también cambió. Con `ESTADO.md` compartido pasaba en casi cada sesión. La bitácora nunca tuvo el problema porque cada sesión crea un archivo nuevo.

## Archivos creados o modificados
- `estado/` (4 archivos nuevos), `ESTADO.md` (aviso), `CONTEXTO.md`, `CLAUDE.md`, `README.md`, `guias/`, `prompts/`, `.claude/commands/`, `config-claude/commands/`, `scripts/`, `.gitignore`.

## Decisiones propuestas (para acordar en grupo)
- Adoptar un archivo de estado por persona (`estado/`) y `CONTEXTO.md` como documento fijo que se actualiza solo en la integración.
- Adoptar la regla "Commit antes de Pull, siempre" (cierre: Commit → Pull → Push).
- Borrar `ESTADO.md` en la primera integración.

## Pendientes y siguiente paso
- [ ] Mario: subir su commit pendiente (bitácora, limpieza y su sección de `ESTADO.md`). En su próxima sesión, su agente pasa esa sección a `estado/mario.md`.
- [ ] Quien integre: borrar `ESTADO.md` después de verificar que todo está en `estado/`.
- [ ] Todos: hacer Pull y que el agente lea el nuevo `CLAUDE.md` antes de su próxima sesión.

## Contexto para la próxima sesión
Desde ahora el estado de cada persona está en `estado/<persona>.md`. Si alguien edita `ESTADO.md` por costumbre, su agente debe mover ese cambio a `estado/`.
