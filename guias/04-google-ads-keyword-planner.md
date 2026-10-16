# Planificador de palabras clave de Google Ads: volúmenes de búsqueda

**Para:** quien tenga cuenta de Google Ads (tarea original de Mario) · **Creada:** 2026-10-16 · **Tiempo:** 20–30 min
El planificador es gratis, pero exige una cuenta de Google Ads. No hace falta pagar ni dejar una campaña activa.

## 1. Crear o abrir la cuenta (una vez)
1. Entrar a https://ads.google.com con la cuenta de Google del proyecto.
2. Si pide crear una campaña, elegir **"Cambiar a modo experto"** y luego **"Crear una cuenta sin campaña"**. País Chile, zona horaria Santiago, moneda CLP.
3. No ingresar medio de pago si no lo exige. Sin campaña activa no se cobra nada.

## 2. Pedir los volúmenes
1. Herramientas → Planificación → **Planificador de palabras clave** → **"Obtener el volumen de búsqueda y las previsiones"**.
2. Pegar los términos de `datos/referencia/terminos-busqueda.csv` (columna `termino`; hasta 10.000 por consulta, se pueden pegar los 114 de una vez).
3. Segmentación: **Chile**, idioma **español**, red **Google**. Período: **últimos 24 meses**.
4. Descargar → **CSV**. Guardarlo como `datos/crudos/AAAA-MM-DD_google-ads_keyword-planner.csv`.
5. Repetir con **"Descubrir nuevas palabras clave"** para 5 semillas: `electrolitos`, `bebida proteica`, `cold brew`, `matcha`, `chai latte`. Guardar como `..._keyword-planner_ideas.csv`.

## 3. Qué se lee
- **Promedio de búsquedas mensuales** (sin gasto activo, Google muestra rangos como 1K–10K: igual sirve para ordenar).
- **Cambio en 3 meses y cambio interanual**: confirma o contradice Google Trends.
- **Competencia y puja estimada (CPC)**: proxy de cuánto pagan otros por ese cliente.

Después, pedir al agente que lo cruce con Google Trends y el radar (`datos/limpios/2026-10-16_radar-oportunidades_boris.csv`).
