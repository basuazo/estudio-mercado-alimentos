# Trae los cambios del equipo antes de empezar a trabajar.
# Uso (PowerShell, desde la carpeta del repositorio):  .\scripts\sync.ps1
git pull --rebase
if ($LASTEXITCODE -ne 0) { Write-Host "Hubo un problema al sincronizar. Pidele ayuda a tu agente o a Boris." -ForegroundColor Yellow; exit 1 }
Write-Host "Listo: tienes la ultima version. Ahora abre tu agente y escribe 'inicio'." -ForegroundColor Green
