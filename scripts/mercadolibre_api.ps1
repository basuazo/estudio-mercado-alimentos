# Consulta la API oficial de Mercado Libre Chile (token de aplicacion) y guarda
# dos CSV con fecha en datos/crudos/:
#   AAAA-MM-DD_mercadolibre-api_tendencias.csv  (Top 50 semanal de palabras por categoria)
#   AAAA-MM-DD_mercadolibre-api_catalogo.csv    (fichas de catalogo por busqueda: marca, sabor, formato...)
#
# La API NO entrega precios, vendidos ni vendedores con este tipo de token
# (pruebas del 2026-10-16). Eso sigue por captura manual: datos/referencia/pauta-captura-mercadolibre.md
#
# Requisitos: archivo .env en la raiz del repositorio (no se sube a GitHub) con:
#   ML_CLIENT_ID=...
#   ML_CLIENT_SECRET=...
# (ver .env.ejemplo)
#
# Uso (PowerShell, desde la carpeta del repositorio):
#   powershell -ExecutionPolicy Bypass -File scripts\mercadolibre_api.ps1
#   powershell -ExecutionPolicy Bypass -File scripts\mercadolibre_api.ps1 -SoloTendencias
#   powershell -ExecutionPolicy Bypass -File scripts\mercadolibre_api.ps1 -SoloCatalogo -MaxPaginas 2
#
# Uso responsable: pausa entre llamadas, tope de paginas, reintento con espera ante 429.
# Correrlo como maximo una vez por semana (las tendencias son semanales).

param(
  [switch]$SoloTendencias,
  [switch]$SoloCatalogo,
  [int]$MaxPaginas = 3,          # paginas de 10 fichas por busqueda
  [double]$Pausa = 1.5           # segundos entre llamadas
)

$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# ---------------------------------------------------------------------------
# 1. Configuracion: edita estas listas
# ---------------------------------------------------------------------------

# Categorias para tendencias ("MLC" = todo el sitio). IDs verificados el 2026-10-16.
$Categorias = @(
  "MLC",        # Todo Mercado Libre Chile
  "MLC1403",    # Alimentos y Bebidas
  "MLC1423",    # Almacen
  "MLC437073",  # Bebidas
  "MLC416869",  # Isotonicas
  "MLC181021",  # Aguas
  "MLC179791",  # Energizantes
  "MLC194298",  # Jugos
  "MLC455818",  # Leche
  "MLC178670",  # Infusiones
  "MLC194313",  # Cereales y Barras
  "MLC194331",  # Snacks
  "MLC1276",    # Deportes y Fitness
  "MLC409431"   # Salud y Equipamiento Medico
)

# Busquedas en catalogo (prioridad 1 y 2 de la pauta, mas el radar)
$Busquedas = @(
  "electrolitos",
  "electrolitos sobres",
  "bebida hidratante en polvo",
  "bebida proteica cafe",
  "proteina lista para beber",
  "cold brew",
  "leche de avena barista",
  "matcha",
  "chai latte",
  "comida liofilizada",
  "jugo prensado en frio",
  "snack de lentejas"
)

# Atributos de la ficha que van en columnas propias (el resto queda en "otros_atributos")
$AtributosColumna = [ordered]@{
  marca       = "BRAND"
  linea       = "LINE"
  modelo      = "MODEL"
  sabor       = "FLAVOR"
  peso_neto   = "NET_WEIGHT"
  volumen     = "NET_VOLUME"
  unidades    = "UNITS_PER_PACK"
  formato     = "SALE_FORMAT"
  gtin        = "GTIN"
}

# ---------------------------------------------------------------------------
# 2. Rutas y claves
# ---------------------------------------------------------------------------

$Raiz   = Split-Path -Parent $PSScriptRoot
$Salida = Join-Path $Raiz "datos\crudos"
$Fecha  = Get-Date -Format "yyyy-MM-dd"
$Api    = "https://api.mercadolibre.com"

function Leer-Env($ruta) {
  if (-not (Test-Path $ruta)) { return }
  foreach ($linea in Get-Content $ruta) {
    $l = $linea.Trim()
    if ($l -eq "" -or $l.StartsWith("#") -or -not $l.Contains("=")) { continue }
    $i = $l.IndexOf("=")
    $k = $l.Substring(0, $i).Trim()
    $v = $l.Substring($i + 1).Trim().Trim('"').Trim("'")
    Set-Item -Path "Env:$k" -Value $v
  }
}

Leer-Env (Join-Path $Raiz ".env")
if (-not $env:ML_CLIENT_ID -or -not $env:ML_CLIENT_SECRET) {
  Write-Host "Faltan ML_CLIENT_ID y ML_CLIENT_SECRET. Copia .env.ejemplo como .env en la raiz del repositorio y completa tus claves." -ForegroundColor Yellow
  exit 1
}

# ---------------------------------------------------------------------------
# 3. Llamadas a la API
# ---------------------------------------------------------------------------

function Pedir-Token {
  $r = Invoke-RestMethod -Method Post -Uri "$Api/oauth/token" -Body @{
    grant_type    = "client_credentials"
    client_id     = $env:ML_CLIENT_ID
    client_secret = $env:ML_CLIENT_SECRET
  }
  return $r.access_token
}

$script:Token = Pedir-Token
$script:Errores = New-Object System.Collections.ArrayList

# GET con: lectura en UTF-8 (corrige los acentos de PowerShell 5.1),
# reintento ante 429 (15/30/60 s) y renovacion del token ante 401.
function ML-Get($ruta) {
  $url = "$Api$ruta"
  $esperas = @(15, 30, 60)
  $intento = 0
  while ($true) {
    try {
      Start-Sleep -Milliseconds ([int]($Pausa * 1000))
      $r = Invoke-WebRequest -Uri $url -Headers @{ Authorization = "Bearer $script:Token" } -UseBasicParsing
      $texto = [Text.Encoding]::UTF8.GetString($r.RawContentStream.ToArray())
      return ($texto | ConvertFrom-Json)
    } catch {
      $codigo = $null
      if ($_.Exception.Response) { $codigo = [int]$_.Exception.Response.StatusCode }
      if ($codigo -eq 429 -and $intento -lt $esperas.Count) {
        Write-Host "  429 (demasiadas llamadas): espero $($esperas[$intento]) s..." -ForegroundColor DarkYellow
        Start-Sleep -Seconds $esperas[$intento]; $intento++; continue
      }
      if ($codigo -eq 401 -and $intento -eq 0) {
        Write-Host "  401: renuevo el token..." -ForegroundColor DarkYellow
        $script:Token = Pedir-Token; $intento++; continue
      }
      [void]$script:Errores.Add([pscustomobject]@{ ruta = $ruta; codigo = $codigo })
      Write-Host "  Error $codigo en $ruta" -ForegroundColor Red
      return $null
    }
  }
}

function Guardar-Csv($filas, $nombre) {
  $ruta = Join-Path $Salida "$($Fecha)_$nombre.csv"
  if (Test-Path $ruta) { $ruta = Join-Path $Salida "$($Fecha)_$(Get-Date -Format HHmm)_$nombre.csv" }
  $lineas = $filas | ConvertTo-Csv -NoTypeInformation
  # UTF-8 sin BOM y saltos de linea LF, igual que el resto de los CSV del repositorio
  [IO.File]::WriteAllText($ruta, (($lineas -join "`n") + "`n"), (New-Object Text.UTF8Encoding($false)))
  Write-Host "Guardado: $ruta ($(@($filas).Count) filas)" -ForegroundColor Green
}

# ---------------------------------------------------------------------------
# 4. Tendencias por categoria
# ---------------------------------------------------------------------------

if (-not $SoloCatalogo) {
  Write-Host "`nTendencias ($($Categorias.Count) categorias)" -ForegroundColor Cyan
  $filas = New-Object System.Collections.ArrayList
  foreach ($cat in $Categorias) {
    if ($cat -eq "MLC") { $ruta = "/trends/MLC"; $nombreCat = "Todo Mercado Libre Chile" }
    else {
      $ruta = "/trends/MLC/$cat"
      $info = ML-Get "/categories/$cat"
      $nombreCat = if ($info) { $info.name } else { "" }
    }
    $lista = @(ML-Get $ruta)
    $pos = 0
    foreach ($t in $lista) {
      if (-not $t -or -not $t.keyword) { continue }
      $pos++
      [void]$filas.Add([pscustomobject]@{
        fecha_captura = $Fecha
        categoria_id  = $cat
        categoria     = $nombreCat
        posicion      = $pos
        palabra       = $t.keyword
        url           = $t.url
        fuente        = "$Api$ruta"
      })
    }
    Write-Host "  $cat $nombreCat : $pos palabras"
  }
  if ($filas.Count -gt 0) { Guardar-Csv $filas "mercadolibre-api_tendencias" }
}

# ---------------------------------------------------------------------------
# 5. Catalogo por busqueda
# ---------------------------------------------------------------------------

if (-not $SoloTendencias) {
  Write-Host "`nCatalogo ($($Busquedas.Count) busquedas, hasta $MaxPaginas paginas de 10)" -ForegroundColor Cyan
  $filas = New-Object System.Collections.ArrayList
  foreach ($q in $Busquedas) {
    $qUrl = [uri]::EscapeDataString($q)
    $n = 0; $total = ""
    for ($p = 0; $p -lt $MaxPaginas; $p++) {
      $offset = $p * 10
      $r = ML-Get "/products/search?status=active&site_id=MLC&q=$qUrl&offset=$offset&limit=10"
      if (-not $r -or -not $r.results) { break }
      if ($r.paging) { $total = $r.paging.total }
      foreach ($prod in @($r.results)) {
        $n++
        $fila = [ordered]@{
          fecha_captura = $Fecha
          busqueda      = $q
          posicion      = $n
          total_busqueda = $total
          product_id    = $prod.id
          nombre        = $prod.name
          dominio       = $prod.domain_id
          estado        = $prod.status
        }
        $attrs = @($prod.attributes)
        foreach ($col in $AtributosColumna.Keys) {
          $a = $attrs | Where-Object { $_.id -eq $AtributosColumna[$col] } | Select-Object -First 1
          $fila[$col] = if ($a) { $a.value_name } else { "" }
        }
        $usados = @($AtributosColumna.Values)
        $fila["otros_atributos"] = (($attrs | Where-Object { $usados -notcontains $_.id -and $_.value_name } |
          ForEach-Object { "$($_.id)=$($_.value_name)" }) -join " | ")
        $fila["fuente"] = "$Api/products/$($prod.id)"
        [void]$filas.Add([pscustomobject]$fila)
      }
      if (@($r.results).Count -lt 10) { break }
      if ($total -ne "" -and ($offset + 10) -ge [int]$total) { break }
    }
    Write-Host "  '$q': $n fichas (total informado: $total)"
  }
  if ($filas.Count -gt 0) { Guardar-Csv $filas "mercadolibre-api_catalogo" }
}

# ---------------------------------------------------------------------------
# 6. Resumen
# ---------------------------------------------------------------------------

if ($script:Errores.Count -gt 0) {
  Write-Host "`n$($script:Errores.Count) llamadas con error:" -ForegroundColor Yellow
  $script:Errores | Format-Table -AutoSize
} else {
  Write-Host "`nListo, sin errores." -ForegroundColor Green
}
