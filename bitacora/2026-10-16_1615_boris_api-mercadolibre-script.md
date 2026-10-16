---
fecha: 2026-10-16 16:15
persona: boris
agente: Claude desktop (Cowork)
fase: Estudio de mercado · Fase 1
paso_del_plan: B3 Método (Mercado Libre: API y captura manual)
estado: completado
---

# API de Mercado Libre: qué entrega y script de tendencias y catálogo

## Objetivo
Definir qué información de Mercado Libre Chile se puede obtener por la API oficial, probar las vías pendientes y dejar automatizado lo que funciona.

## Qué se hizo
- Se revisó la documentación del DevCenter (Más vendidos, Competencia en catálogo, Autenticación) y se armó una estrategia en cadena: categoría → tendencias → fichas de catálogo → competencia por ficha → vendedor.
- Se probaron con token de aplicación (Client Credentials) las vías de precios:
  - `GET /products/{id}/items`: 404 "No winners found" en 10 fichas de electrolitos (Quenut, Superieur, ENA, Lytos) y 5 de Gatorade como control. Hay permiso, pero las fichas no tienen vendedores compitiendo en catálogo.
  - `GET /sites/MLC/search` (búsqueda de avisos): 403.
  - `GET /highlights/...` (más vendidos): 403, como en la sesión anterior.
- Segundo y último intento de token de usuario (Authorization Code): volvió "Lo sentimos, la aplicación no puede conectarse a tu cuenta", aun con URL armada por PowerShell, redirect URI exacta, permisos en solo lectura (el DevCenter no ofrece "Sin acceso"), perfil completado y ventana de incógnito. Se descarta por ahora.
- Se escribió y corrió `scripts/mercadolibre_api.ps1`: tendencias de 14 categorías y catálogo de 12 búsquedas (hasta 30 fichas cada una), con pausas, reintento ante 429 y CSV en UTF-8.

## Hallazgos
- Con token de aplicación la API sirve para **tendencias y catálogo**, no para precios, vendidos ni vendedores. Eso sigue por captura manual (`datos/referencia/pauta-captura-mercadolibre.md`). Fuente: pruebas del 2026-10-16.
- Electrolitos y Gatorade no se venden en modo catálogo en Chile: son avisos sueltos (mercado disperso).
- Catálogo (2026-10-16, `datos/crudos/2026-10-16_mercadolibre-api_catalogo.csv`):
  - "electrolitos": 20 marcas en 30 fichas (Quenut, ENA Sport, Lytos, Evolution, Superieur…). "electrolitos sobres" trae otras marcas, más de farmacia (Suma, Hydrasor, Sesen, Apotex).
  - "bebida hidratante en polvo": dominada por Powerade y Prime.
  - "bebida proteica cafe": el término con menos fichas (392 en total); calza con poca oferta.
  - "comida liofilizada": marcas chilenas de nicho (Lio Nutri, Camps Foods, Lyovibes).
  - Ruido: "cold brew" trae Jägermeister y "jugo prensado en frio" trae extractoras; hay que filtrar por `dominio` al limpiar.
- Tendencias (2026-10-16, `datos/crudos/2026-10-16_mercadolibre-api_tendencias.csv`): 569 palabras; Isotónicas con 17 (hidratación en polvo, Suerox, Electrolit), Leche con 1.
- Límites: las tendencias no tienen volumen; el total de fichas mide oferta en catálogo, no ventas.

## Archivos creados o modificados
- `scripts/mercadolibre_api.ps1` — script semanal de tendencias y catálogo (claves en `.env`, que no se sube).
- `datos/crudos/2026-10-16_mercadolibre-api_tendencias.csv` — Top 50 semanal por categoría.
- `datos/crudos/2026-10-16_mercadolibre-api_catalogo.csv` — fichas por búsqueda con marca, sabor, formato y GTIN.
- `estado/boris.md` — actualizado.
- Proyecto de Claude: `claude/estrategia-api-mercadolibre.md` y `claude/contexto-mercadolibre-api.md` (detalle técnico de endpoints, errores y checklist del token de usuario).

## Decisiones propuestas (para acordar en grupo)
- Usar la API solo para tendencias y catálogo, y correr el script una vez por semana para armar serie histórica.
- Precios, vendidos y reputación por captura manual según la pauta.
- No insistir con el token de usuario; reintentar solo en unos días o vía soporte del DevCenter.

## Pendientes y siguiente paso
- [ ] Boris: captura manual de precios y vendidos (Lytos, ENA, Quenut, Superieur; luego bebida proteica de café y cold brew).
- [ ] Boris: actualizar el radar con electrolitos en polvo (más fuerza), matcha, chai latte y comida liofilizada outdoor.
- [ ] Boris: limpiar el catálogo (filtrar por dominio de alimentos y bebidas) en `datos/limpios/`.
- [ ] Boris: correr el script de nuevo la semana del 23-oct.
- [ ] Mario: términos de uso de Mercado Libre y volúmenes en Google Ads Keyword Planner.

## Contexto para la próxima sesión
Para correr el script hace falta `.env` en la raíz con `ML_CLIENT_ID` y `ML_CLIENT_SECRET` (cada persona con su propia aplicación del DevCenter, o pedírselo a Boris). Uso: `powershell -ExecutionPolicy Bypass -File scripts\mercadolibre_api.ps1`. Las listas de categorías y búsquedas están al inicio del script. Si aparece 429, esperar unos minutos.
