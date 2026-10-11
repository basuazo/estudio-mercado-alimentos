#!/usr/bin/env bash
# Configuracion inicial del repositorio (solo una vez). Uso: ./scripts/configurar.sh
set -e
[ -d .git ] && { echo "Ya existe un repositorio git aqui."; exit 0; }
mkdir -p .claude && cp -r config-claude/commands .claude/
git init -b main
git add -A
git commit -m "boris: estructura inicial, protocolo de sesiones y plan del estudio de mercado (Fase 0)"
echo "Listo. Publica el repositorio en GitHub (privado) con GitHub Desktop o 'gh repo create'."
