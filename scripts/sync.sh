#!/usr/bin/env bash
# Trae los cambios del equipo antes de empezar a trabajar.  Uso: ./scripts/sync.sh
set -e
git pull --rebase && echo "Listo: tienes la última versión. Abre tu agente y escribe 'inicio'."
