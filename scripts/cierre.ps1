# Sube tu trabajo al repositorio compartido.
# Uso:  .\scripts\cierre.ps1 "boris: tendencias google (A1)"
param([Parameter(Mandatory=$true)][string]$mensaje)
git add -A
git commit -m $mensaje
git pull --rebase --autostash
if ($LASTEXITCODE -ne 0) { Write-Host "Conflicto al integrar con el trabajo de otro. No borres nada: pidele a tu agente que lo resuelva." -ForegroundColor Yellow; exit 1 }
git push
Write-Host "Listo: tu sesion quedo en GitHub." -ForegroundColor Green
