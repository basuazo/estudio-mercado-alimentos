> **Archivo en desuso desde el 2026-10-13.** El estado ahora vive en un archivo por persona: `estado/boris.md`, `estado/mario.md`, `estado/chalo.md` y `estado/equipo.md`. No edites este archivo; se borrará en la próxima integración, después de pasar cualquier cambio pendiente a `estado/`.

# Estado del proyecto

Tablero vivo. Cada persona (o su agente) edita **solo su sección**. La sección "Resumen del equipo" se actualiza en cada integración.

## Resumen del equipo

**Última integración:** — (aún no hay)
**Fase:** Estudio de mercado de alimentos · Fase 0 (preparación, 10–14 oct)
**Próximo hito:** reunión del miércoles 2026-10-14 — aprobar el plan del estudio de mercado.

---

## Boris

**Actualizado:** 2026-10-13

- **En curso:** —
- **Terminado:**
  - Plan del estudio de mercado (borrador para el miércoles).
  - Repositorio en GitHub y guías de uso.
  - Google Trends ampliado a 100 términos (incluye aguas y bebidas funcionales) y dashboard v2 interactivo.
  - Primera pasada de Google Trends (42 términos, 2 años) y Meta (10 marcas) → `entregables/2026-10-12_trends-y-meta_primera-pasada.md` y dashboard https://claude.ai/artifact/5S6M6umJvaDBJDjrENxKKt
- **Siguiente:**
  - [ ] Confirmar que Mario y Chalo tienen acceso al repositorio y compartirles el dashboard.
  - [ ] Probar el método B3 con Mercadona y Tesco en la categoría barras.
  - [ ] Sesión de 30 min de introducción a GitHub con Mario.
  - [ ] Confirmar qué vende GoNat; repetir Meta semanal.
- **Bloqueos:** ninguno. Mario puede usar `datos/referencia/terminos-busqueda.csv` para Google Ads.

## Mario

**Actualizado:** 2026-10-13

- **En curso:** —
- **Terminado:**
  - Acceso al repositorio y puesta al día con todo el contexto (13-oct).
  - Limpieza de archivos de prueba y `.gitignore` para archivos de R.
  - Copia propia del dashboard: https://claude.ai/artifact/Tq1RMTXaSTPhhvjHgsoxzA (el original de Boris aún no está compartido).
- **Siguiente:**
  - [ ] Revisar términos de uso de Mercado Libre, Jumbo, Líder y Unimarc respecto a scraping; proponer alternativa por sitio.
  - [ ] Planificador de palabras clave de Google Ads con los 100 términos de `datos/referencia/terminos-busqueda.csv`.
  - [ ] Revisar a Farmacia Mont en Mercado Público.
- **Bloqueos:** ninguno.

## Chalo

**Actualizado:** 2026-10-13

- **En curso:** A4 Datos macro — bases del SII y Aduanas para alimentos.
- **Terminado:**
  - Acceso al repositorio y revisión completa del trabajo de Boris.
  - Listado de bases del SII y Aduanas, con URLs, códigos de actividad y APIs → `datos/referencia/fuentes-macro-sii-aduanas.md`.
  - Copia del dashboard Radar de alimentos como artefacto propio: https://claude.ai/artifact/1nxr4wuDLFic8pMdEj2yvs
- **Siguiente:**
  - [ ] Descargar `EMPRESAS.zip` y la nómina de personas jurídicas 2020–2024 del SII y procesarlas (subrubros de alimentos, Ñuble).
  - [ ] Revisar las bases mensuales de Aduanas y probar UN Comtrade con las partidas candidatas.
  - [ ] Listar distribuidores de Santiago y Chillán con contacto.
  - [ ] Reunión del martes con el contacto de intermediación en compras públicas.
- **Bloqueos:** ninguno. sii.cl está bloqueado para el agente: las descargas se hacen a mano.
