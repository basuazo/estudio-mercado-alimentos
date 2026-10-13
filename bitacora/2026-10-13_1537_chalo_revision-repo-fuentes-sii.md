---
fecha: 2026-10-13 15:37
persona: chalo
agente: Claude (sesión en la nube con la carpeta vinculada)
fase: Estudio de mercado · Fase 0
paso_del_plan: A4 Datos macro (SII, Aduanas) y puesta al día con el repositorio
estado: en curso
---

# Revisión del repositorio, dashboard propio y fuentes macro del SII

## Objetivo
Ponerse al día con el repositorio y partir la tarea A4: levantar las bases del SII y de Aduanas, y ver si hay API.

## Qué se hizo
- Se revisó todo el repositorio: protocolo, plan, `ESTADO.md`, bitácoras de Boris, informe de Trends y Meta, y datos. Los números del informe cuadran con los CSV: "56 términos con datos" = 51 con datos suficientes + 5 con datos medios.
- Se publicó una copia del dashboard "Radar de alimentos Chile" como artefacto de Chalo en claude.ai (https://claude.ai/artifact/1nxr4wuDLFic8pMdEj2yvs). Se armó con `entregables/dashboard-radar-alimentos/radar-alimentos_pagina.html` y los 5 CSV que usa, porque el dashboard original de Boris no está compartido con Chalo. Es una copia: no se actualiza si Boris cambia los datos.
- Se armó el listado de bases del SII y Aduanas para alimentos → `datos/referencia/fuentes-macro-sii-aduanas.md`.

## Hallazgos
Fuentes: sii.cl y si3.bcentral.cl, consultados el 2026-10-13.
- El SII publica estadísticas de empresas 2005–2024 (actualizadas en oct-2025): número de empresas, ventas, trabajadores y remuneraciones por actividad económica, cruzadas con tamaño, región y comuna. También publica la nómina de personas jurídicas (una fila por empresa, sin RUT) y las estadísticas de inicio de actividades y término de giro. https://www.sii.cl/sobre_el_sii/estadisticas_de_empresas.html
- El SII **no tiene API** para estadísticas: son archivos descargables (.xlsb o ZIP con texto). Sus servicios web son solo para facturación electrónica.
- APIs oficiales alternativas:
  - API BDE del Banco Central: gratuita, con registro.
  - UN Comtrade: importaciones por partida arancelaria.
  - Aduanas publica bases mensuales, pero no tiene API (su página no se pudo abrir desde la sesión).
- sii.cl está bloqueado en el entorno de Claude y en la conexión con el computador de Chalo: las descargas hay que hacerlas a mano desde el navegador.

## Archivos creados o modificados
- `datos/referencia/fuentes-macro-sii-aduanas.md` — listado de bases del SII y Aduanas, URLs, códigos de actividad y partidas candidatas, APIs.
- `ESTADO.md` — sección de Chalo.

## Decisiones propuestas (para acordar en grupo)
- Usar las estadísticas de empresas del SII (por actividad y región) como fuente independiente del enfoque A4. Sirven para ver tamaño, concentración y dinamismo de cada subrubro de alimentos, incluido Ñuble.
- Agregar `.Rhistory` a `.gitignore`. Hoy está en el repositorio, vacío, desde el commit "Chalo: Prueba git" (que también subió `PruebaGonza.txt`): conviene borrar ambos.

## Pendientes y siguiente paso
- [ ] Descargar `EMPRESAS.zip` y `PUB_EMPRESAS_PJ_2020_A_2024.zip` del SII a `datos/crudos/` — Chalo.
- [ ] Script que filtre las actividades de alimentos (CIIU 10xx, 1104, 4630, 4711, 4721/4722) y saque series por subrubro y por Ñuble — Chalo con Claude.
- [ ] Confirmar los códigos de actividad con el clasificador del SII — Chalo.
- [ ] Revisar la página de bases mensuales de Aduanas y probar UN Comtrade con las partidas candidatas — Chalo.
- [ ] Listar distribuidores de Santiago y Chillán — Chalo.

## Contexto para la próxima sesión
El listado de fuentes ya tiene los enlaces de descarga directa y los códigos a filtrar. Lo siguiente es bajar los ZIP desde el navegador (sii.cl está bloqueado para el agente) y procesarlos en R o Python. Las cifras del SII son preliminares y cambian con cada actualización anual: registrar la fecha de descarga. El dashboard copia de Chalo está en https://claude.ai/artifact/1nxr4wuDLFic8pMdEj2yvs y es privado hasta que se comparta.
