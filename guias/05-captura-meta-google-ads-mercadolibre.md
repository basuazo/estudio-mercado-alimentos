# Captura de Meta, Google Ads y Mercado Libre: paso a paso para el equipo

**Para:** cualquier persona del equipo · **Creada:** 2026-10-18 (Boris con Claude) · **Paso del plan:** A1 Demanda, A2 Competencia, A3 Oferta y precios
**Tiempo:** preparación 15 min (una vez) · Meta 30–40 min · Google Ads 20–30 min · Mercado Libre 45–60 min (3 términos)
Reemplaza y amplía `guias/03-captura-manual-mercadolibre.md` y `guias/04-google-ads-keyword-planner.md` (siguen valiendo como detalle).

---

## 0. Antes de empezar: qué es "scraping" en este proyecto

Ni Mercado Libre ni Meta permiten robots que recorran sus páginas: Mercado Libre lo prohíbe expresamente (términos para desarrolladores, secc. 7.6) y Meta tiene términos de recopilación automatizada de datos que exigen permiso previo. Por eso nuestra regla (`datos/referencia/terminos-de-uso-por-sitio.md`) es:

| Fuente | Qué se automatiza | Qué se hace a mano | Script |
|---|---|---|---|
| **Meta** (Biblioteca de anuncios) | Crear el archivo del día y los enlaces de búsqueda; resumir y comparar con la semana anterior | Abrir cada búsqueda y anotar total de anuncios y anunciantes | `preparar_captura.py meta` → `resumir_meta_ads.py` |
| **Google Ads** (Planificador de palabras clave) | Limpiar la descarga y cruzarla con el diccionario de términos | Pegar los términos y descargar el CSV (la descarga es oficial) | `procesar_google_ads.py` |
| **Mercado Libre** | API oficial: tendencias y catálogo (marcas, sabores, formatos) | Precios, vendidos y vendedores de los primeros 20 resultados | `mercadolibre_api.ps1`, `preparar_captura.py mercadolibre` → `resumir_captura_mercadolibre.py` |

**Reglas de captura (para los tres):** ritmo humano, sin extensiones ni scripts en la consola del navegador, sin saltarse captchas ni inicios de sesión. Guardar solo precio, formato, marca, anunciante y fecha: nada de imágenes, descripciones ni nombres de personas en reseñas. Los resultados son de **uso interno**: no publicar precios promedio de Mercado Libre.

> Nota: la captura de Mercado Libre del 16-oct se hizo con un script en la consola del navegador. Eso es extracción automatizada y choca con la secc. 7.6; desde ahora se captura a mano.

---

## 1. Preparación (una vez por persona)

### 1.1 Traer lo último del repositorio
GitHub Desktop → **Fetch origin** → **Pull origin**. (Si tienes algo en *Changes*, primero **Commit to main**.)

### 1.2 Instalar Python (si no lo tienes)
1. Descargar desde https://www.python.org/downloads/ (versión 3.10 o más nueva).
2. En el instalador, **marcar "Add python.exe to PATH"** antes de *Install Now*.
3. Comprobar: abrir una terminal y escribir `python --version`. Debe responder `Python 3.x.x`.
   - En Windows, si dice que no existe, prueba `py --version` y usa `py` en vez de `python` en toda la guía.

No hay que instalar librerías: los scripts usan solo lo que trae Python.

### 1.3 Abrir una terminal en la carpeta del repositorio
- **Opción fácil:** GitHub Desktop → menú **Repository** → **Open in Command Prompt** (o *Open in Terminal*).
- **Otra opción:** abrir la carpeta `company-builder` en el Explorador, hacer clic en la barra de dirección, escribir `cmd` y Enter.

Todos los comandos de esta guía se escriben ahí, **desde la raíz del repositorio** (la carpeta donde está `README.md`).

### 1.4 Editar los CSV: mejor Google Sheets
Excel en configuración chilena guarda los CSV con `;` y a veces rompe tildes. Recomendado:
**Google Sheets → Archivo → Importar → Subir** el CSV → completar → **Archivo → Descargar → Valores separados por comas (.csv)** → reemplazar el archivo en `datos/crudos/` con **el mismo nombre**.
Si usas Excel: *Guardar como* → **CSV UTF-8 (delimitado por comas)**.

---

## 2. Meta: Biblioteca de anuncios

**Qué responde:** cuánta pauta activa hay por tema y quién la está pagando (competencia y saturación). Cuenta como **una** fuente para la regla de 3.
**Frecuencia:** semanal, idealmente el mismo día.

### 2.1 Preparar el archivo del día
```
python scripts/preparar_captura.py meta --persona tu-nombre
```
`tu-nombre` va en minúsculas, como en la bitácora (`boris`, `mario` o `chalo`). Crea `datos/crudos/AAAA-MM-DD_meta-ads-library_cl_captura.csv` con una fila por palabra clave (por defecto: electrolitos, bebida hidratante, bebida proteica, proteina, cold brew, matcha, leche de avena, yogurt griego, barra de proteina, sin azucar) y muestra en pantalla un enlace por palabra.

Para elegir otras palabras: `python scripts/preparar_captura.py meta --persona tu-nombre "agua de coco" "kombucha"`.
Por defecto busca la **frase exacta**; agrega `--amplia` para palabras sueltas.

### 2.2 Abrir cada enlace
El enlace ya viene con **País: Chile**, **Todos los anuncios** y **Activos**. No hace falta iniciar sesión en Facebook. Si la página pide confirmar algo, revisa que esos tres filtros sigan puestos.

### 2.3 Qué anotar (en la fila de cada palabra)
| Columna | Qué poner | Ejemplo |
|---|---|---|
| `resultados_activos_aprox` | El número de arriba, "~N resultados" | `~2.800` |
| `anunciante` | Nombre de la página que paga el anuncio | `Feroz Snack` |
| `anuncios_del_anunciante` | Cuántos anuncios suyos aparecen (o "N anuncios usan este contenido") | `27` |
| `anuncio_mas_antiguo` | El "Circulando desde el…" más antiguo de ese anunciante | `12 dic 2025` |
| `producto_pautado` | Qué vende en el anuncio | `charqui proteico` |
| `mensaje_principal` | La promesa central, en pocas palabras | `24 g de proteína, no frito` |
| `es_alimento_o_bebida` | `si` / `no` (apps, suplementos de EE.UU., recetas = `no`) | `si` |
| `nota` | Lo que llame la atención | `mucho ruido de apps` |

**Más de un anunciante:** copia la fila completa (con su `palabra_clave` y `url_busqueda`) y cambia solo las columnas del anunciante. Anota **hasta 10 anunciantes relevantes** por palabra, priorizando marcas de alimentos y bebidas. El total (`resultados_activos_aprox`) basta en una fila por palabra.

**Detalle de una marca (opcional):** clic en el nombre del anunciante → muestra todos sus anuncios activos → anota el total en `anuncios_del_anunciante`.

Los conteos de Meta son aproximados: tómalos como un piso, no como el total.

### 2.4 Resumir
```
python scripts/resumir_meta_ads.py
```
Salidas en `datos/limpios/`:
- `AAAA-MM-DD_meta-ads_resumen-palabras.csv`: total por palabra, anunciantes anotados, los 5 principales y **variación contra la captura anterior**.
- `AAAA-MM-DD_meta-ads_anunciantes.csv`: por anunciante, en cuántas palabras aparece, anuncios, el más antiguo y si es **nuevo** respecto a capturas anteriores.

El script avisa si faltó algún total o si una fecha no se entendió (por ejemplo "ayer": escribe la fecha).

---

## 3. Google Ads: Planificador de palabras clave

**Qué responde:** cuánta gente busca cada término en Google en Chile, si sube o baja, y cuánto pagan otros por ese clic (CPC).
**Frecuencia:** una vez por tanda de términos.

### 3.1 Cuenta (una vez)
1. Entrar a https://ads.google.com con la cuenta de Google del proyecto.
2. Si pide crear una campaña: **"Cambiar a modo experto"** → **"Crear una cuenta sin campaña"**. País Chile, zona horaria Santiago, moneda CLP.
3. No ingresar medio de pago si no lo exige. Sin campaña activa no se cobra nada.

### 3.2 Volúmenes de una lista de términos
1. **Herramientas** (ícono de llave) → **Planificación** → **Planificador de palabras clave**.
2. Elegir **"Obtener el volumen de búsqueda y las previsiones"**.
3. Abrir `datos/referencia/2026-10-17_google-ads_segunda-tanda_para-pegar.txt` (31 términos, uno por línea), copiar todo y pegarlo. Clic en **Comenzar**.
4. Arriba, revisar: Ubicación **Chile**, idioma **Español**, red **Google**, período **últimos 12 meses** (o 24).
5. Ir a la pestaña **"Métricas históricas"** (*Historical metrics*). ⚠️ No descargar desde *Previsiones*: esa descarga trae clics estimados y el script la descarta.
6. **Descargar** (flecha hacia abajo) → **CSV**.
7. Mover el archivo a `datos/crudos/` y renombrarlo, **sin abrirlo ni editarlo**:
   `AAAA-MM-DD_google-ads_keyword-planner.csv` (ej.: `2026-10-18_google-ads_keyword-planner.csv`).

### 3.3 Ideas nuevas (opcional, mismo día)
**"Descubrir nuevas palabras clave"** → escribir hasta 10 semillas (ej.: `electrolitos`, `bebida proteica`, `cold brew`) → **Métricas históricas** → Descargar CSV → `AAAA-MM-DD_google-ads_keyword-planner_ideas.csv`.

### 3.4 Procesar
```
python scripts/procesar_google_ads.py
```
Toma todas las descargas de la fecha más reciente (o `python scripts/procesar_google_ads.py 2026-10-18`). Acepta la interfaz en inglés o español.
Salida: `datos/limpios/AAAA-MM-DD_google-ads_limpio.csv`, una fila por término con `busquedas_mes_chile`, `cambio_3m_pct`, `cambio_interanual_pct`, `competencia`, `cpc_bajo`, `cpc_alto`, mes más alto y si el término ya está en el diccionario del estudio.
En pantalla: el top 15 y los términos con 500+ búsquedas que **no** están en el diccionario (pásaselos al agente para clasificarlos).

**Cómo leerlo:** sin gasto, Google muestra volúmenes por nivel (50 / 500 / 5.000 / 50.000). Sirven para **ordenar**, no para sumar. CPC alto y competencia "Alta" = otros ya pagan caro por ese cliente.

---

## 4. Mercado Libre

### 4.A API oficial: tendencias y catálogo
La API entrega las palabras más buscadas por categoría (semanal) y las fichas de catálogo (marca, sabor, formato). **No** entrega precios ni vendidos.

1. **Claves (una vez):** en https://developers.mercadolibre.cl → *Mis aplicaciones* → crear aplicación → copiar *Client ID* y *Client Secret*.
2. Copiar `.env.ejemplo` como `.env` en la raíz del repositorio y completar `ML_CLIENT_ID=` y `ML_CLIENT_SECRET=`. `.env` no se sube a GitHub. **Nunca pegues las claves en el chat, la bitácora ni WhatsApp**: cada persona que corra la API crea su propia aplicación.
3. Correr (PowerShell o cmd, desde la raíz):
   ```
   powershell -ExecutionPolicy Bypass -File scripts\mercadolibre_api.ps1
   ```
   Tarda unos minutos (hace pausas a propósito). Crea `datos/crudos/AAAA-MM-DD_mercadolibre-api_tendencias.csv` y `..._catalogo.csv`.
4. Limpiar el catálogo:
   ```
   python scripts/limpiar_catalogo_mercadolibre.py
   ```
   → `datos/limpios/AAAA-MM-DD_mercadolibre-api_catalogo_limpio.csv`.
5. Máximo **una vez por semana** (próxima: semana del 23-oct).

### 4.B Captura manual: precios y vendidos
**Qué responde:** cuántas marcas hay, cuánto cobran por litro, kilo o porción, quién vende más y si hay vendedores chilenos nuevos.

1. **Preparar los archivos:**
   ```
   python scripts/preparar_captura.py mercadolibre
   ```
   Crea un CSV vacío por término en `datos/crudos/` (`AAAA-MM-DD_mercadolibre_cl_<termino>.csv`) y muestra el enlace de cada búsqueda. Por defecto: electrolitos sobres, bebida hidratante en polvo, bebida proteica cafe, proteina lista para beber, cold brew. Para otros: `python scripts/preparar_captura.py mercadolibre "matcha" "chai latte"`.
   **No cambies el nombre del archivo:** el script de resumen saca el término del nombre.
2. **Abrir el enlace**, dejar el orden en **"Más relevantes"** y anotar los **primeros 20 resultados**, una fila por publicación:

| Columna | Qué poner | Ejemplo |
|---|---|---|
| `fecha` | Fecha de hoy | `2026-10-18` |
| `termino` | El término buscado | `cold brew` |
| `posicion` | 1 a 20 | `3` |
| `titulo` | Título tal cual | `Concentrado De Café Cold Brew Briu 1 Litro` |
| `marca` | Si se ve | `Briu` |
| `vendedor` | Nombre de la tienda o vendedor | `Briu Tienda Oficial` |
| `tienda_oficial` | `si` / `no` | `si` |
| `precio_clp` | Precio final que se ve, sin puntos ni $ (sin cuotas) | `13990` |
| `formato` | Escrito así: `30 sobres`, `12 x 250 ml`, `1 l`, `400 g`, `20 porciones` | `1 l` |
| `precio_por_porcion_o_litro` | **Vacío** (lo calcula el script) | |
| `vendidos_visibles` | Tal cual: `+100 vendidos`, `+5mil vendidos`; vacío si no aparece | `+500 vendidos` |
| `reputacion_vendedor` | `verde`, `MercadoLíder`, `amarillo`… | `MercadoLíder` |
| `envio_gratis` | `si` / `no` | `si` |
| `url` | Enlace de la publicación | |
| `observaciones` | Descuento (precio original), importado, "sin sellos", "sin azúcar", farmacia | `antes 15990` |

   Si un dato no aparece, **déjalo vacío** (nunca 0). Saltar resultados que no son del rubro (cafeteras, licores) y seguir hasta juntar 20 que sí.
3. **Netnografía (opcional):** en las 2–3 publicaciones líderes, resumir en `observaciones` qué critican y qué valoran los comentarios. Sin nombres de personas.
4. **Resumir:**
   ```
   python scripts/resumir_captura_mercadolibre.py resumir 2026-10-18
   ```
   → `datos/limpios/AAAA-MM-DD_mercadolibre_cl_captura.csv` y `..._resumen.csv` (precio mediano por litro, kilo o porción, marcas, vendedores, más vendidos). El script avisa qué porcentaje quedó sin precio por unidad: casi siempre es un `formato` mal escrito.
5. **Validación (opcional):** `python scripts/resumir_captura_mercadolibre.py proponer` genera la propuesta para la mesa de validación (ver `entregables/2026-10-17_mesa-validacion/LEEME.md`).

---

## 5. Al terminar (todos)
1. Revisar que tus archivos estén en `datos/crudos/` y `datos/limpios/` con fecha en el nombre.
2. Decirle a tu agente **"cierre"**: escribe tu bitácora y actualiza tu `estado/<persona>.md`.
3. GitHub Desktop: **Commit to main** → **Pull origin** (si aparece) → **Push origin**.

## 6. Problemas frecuentes
| Síntoma | Solución |
|---|---|
| `'python' no se reconoce como un comando` | Reinstalar Python marcando *Add to PATH*, o usar `py` en vez de `python` |
| `No such file or directory: scripts/...` | La terminal no está en la raíz del repositorio. Vuelve al paso 1.3 |
| El resumen de Mercado Libre sale vacío | El archivo quedó con `;` o con otro nombre. Descárgalo desde Google Sheets como CSV y deja el nombre que creó `preparar_captura.py` |
| Google Ads: "es la descarga de PREVISIONES" | Descargar desde la pestaña *Métricas históricas* |
| Google Ads muestra rangos ("1K–10K") | Normal sin campaña activa. Se usan igual para ordenar |
| Meta pide iniciar sesión o muestra otro país | Revisar filtros: Chile, Todos los anuncios, Activos. No hace falta cuenta |
| La API de Mercado Libre dice "Faltan ML_CLIENT_ID" | Falta el archivo `.env` (paso 4.A.2) |
| Mercado Libre muestra captcha | Parar, esperar y seguir más tarde. No intentar saltarlo |

## Fuentes
- Términos de uso y reglas del equipo: `datos/referencia/terminos-de-uso-por-sitio.md` (revisado 2026-10-16).
- Términos para desarrolladores de Mercado Libre, secc. 5.4 y 7.6: https://developers.mercadolibre.com.ar/en_us/mercado-libre-developer-terms-and-conditions (consultado 2026-10-16).
- Términos de recopilación automatizada de datos de Meta: https://www.facebook.com/apps/site_scraping_tos_terms.php (por confirmar que sigue vigente).
- Biblioteca de anuncios de Meta: https://www.facebook.com/ads/library/
- Planificador de palabras clave de Google Ads: https://ads.google.com
