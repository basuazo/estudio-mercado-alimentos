# Configuracion inicial del repositorio (solo Boris, una vez).
# Uso (PowerShell, desde la carpeta company-builder):
#   powershell -ExecutionPolicy Bypass -File scripts\configurar.ps1
if (Test-Path .git) { Write-Host "Ya existe un repositorio git aqui. No hago nada." -ForegroundColor Yellow; exit 0 }
# 1. Comandos /inicio, /cierre e /integrar para Claude Code
New-Item -ItemType Directory -Force -Path .claude | Out-Null
Copy-Item -Recurse -Force config-claude\commands .claude\
# 2. Repositorio git con el primer commit
git init -b main
git config core.autocrlf false
git add -A
git commit -m "boris: estructura inicial, protocolo de sesiones y plan del estudio de mercado (Fase 0)"
if ($LASTEXITCODE -ne 0) { Write-Host "No se pudo hacer el commit. Revisa que git tenga tu nombre y correo (git config --global user.name / user.email)." -ForegroundColor Yellow; exit 1 }
Write-Host "Listo. Ahora abre GitHub Desktop: File > Add local repository > esta carpeta > Publish repository (privado)." -ForegroundColor Green
