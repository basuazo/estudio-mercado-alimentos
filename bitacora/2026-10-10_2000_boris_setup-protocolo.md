---
fecha: 2026-10-10 20:00
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 0
paso_del_plan: Preparación — plan y protocolo de trabajo
estado: completado
---

# Plan del estudio de mercado y protocolo de trabajo con git

## Objetivo
Diseñar el plan del estudio de mercado de alimentos acordado en la reunión del 10-oct y montar un repositorio común para que los tres trabajemos con agentes y dejemos trazabilidad.

## Qué se hizo
- Se redactó el plan del estudio de mercado con tres enfoques: (A) mercado local con fuentes públicas, (B) benchmarking internacional, (C) etnografía con prompts por objetivo. Incluye matriz de puntaje, cronograma de 4 fases y responsables propuestos.
- Se creó este repositorio con el protocolo de sesiones: `CLAUDE.md` (instrucciones para agentes), bitácora, tablero `ESTADO.md`, `decisiones.md`, plantillas, prompts y comandos `/inicio`, `/cierre`, `/integrar`.
- Se copiaron a `antecedentes/` los documentos del Proyecto de Claude y el resumen de la reunión del 10-oct.

## Hallazgos
- Las conversaciones con Claude no se sincronizan solas entre personas; la bitácora con formato fijo es el mecanismo de traspaso de contexto.
- Mario necesita una introducción corta a GitHub; GitHub Desktop evita usar la terminal.

## Archivos creados o modificados
- `plan/plan-estudio-mercado-alimentos.md` — plan exportado (doc vivo: https://claude.ai/code/artifact/51651435-1c29-4d8a-a447-b606095af0d5).
- `CLAUDE.md`, `AGENTS.md`, `README.md`, `CONTEXTO.md`, `ESTADO.md`, `decisiones.md`, `EQUIPO.md` — protocolo y contexto.
- `prompts/`, `plantillas/`, `config-claude/commands/`, `scripts/` — herramientas del protocolo. `scripts/configurar.ps1` crea el repositorio git y la carpeta `.claude/` en el primer uso.
- `antecedentes/` — estructura legal, banco de ideas, economía circular, nicho socioecológico, notas de la reunión.

## Decisiones propuestas (para acordar en grupo)
- Adoptar este protocolo: pull → inicio → trabajo → cierre → push, con una entrada de bitácora por sesión.
- Usar GitHub (repositorio privado) como fuente de verdad, el Proyecto de Claude como memoria y Drive para archivos pesados.
- Correr `/integrar` antes de cada reunión.
- Asignación de frentes del plan (ver `ESTADO.md`), en especial las tareas propuestas para Chalo.

## Pendientes y siguiente paso
- [ ] Publicar el repositorio en GitHub e invitar a Mario y Chalo — Boris.
- [ ] Sesión de 30 min de introducción a GitHub con Mario — Boris.
- [ ] Presentar plan y protocolo en la reunión del miércoles 14-oct — todos.

## Contexto para la próxima sesión
El plan está en borrador y se aprueba el 14-oct. Hasta entonces, las tareas de `ESTADO.md` son propuestas. El paso siguiente de Boris es la primera pasada de Google Trends y Meta (A1/A2) y probar el método B3 con Mercadona y Tesco.
