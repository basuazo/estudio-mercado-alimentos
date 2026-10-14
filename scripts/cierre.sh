#!/usr/bin/env bash
# Sube tu trabajo al repositorio compartido.  Uso: ./scripts/cierre.sh "mario: terminos de uso (A3)"
set -e
if [ -z "$1" ]; then echo "Falta el mensaje del commit"; exit 1; fi
git add -A
git commit -m "$1"
git pull --rebase --autostash || { echo "Conflicto al integrar. No borres nada: pídele a tu agente que lo resuelva."; exit 1; }
git push && echo "Listo: tu sesión quedó en GitHub."
