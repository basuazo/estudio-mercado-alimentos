# Contexto del proyecto

**Actualizado:** 2026-10-13 · **Fase actual:** Estudio de mercado de la industria de alimentos — Fase 0 (preparación, 10–14 oct)

Este es el documento **fijo** del proyecto: qué somos, hacia dónde vamos, qué criterios usamos y cómo trabajamos. Cambia poco y solo en la integración. Lo que cambia día a día (en qué está cada uno) vive en `estado/`.

## Qué somos

Tres compañeros de universidad (Boris, Mario y Chalo), titulados, con unos 10 años de experiencia laboral cada uno y empleo formal vigente. Construimos un *company builder*: un vehículo de inversión que nos permita entrar en varios rubros y, a mediano plazo, trabajar de forma independiente. Foco transversal en sostenibilidad. Financiamiento: bootstrapping y, cuando aplique, fondos concursables (Corfo, Sercotec) y compras públicas.

## Horizonte

- **Largo plazo:** aportar a la agroindustria de Ñuble.
- **Corto plazo (acordado el 2026-10-10):** validar un producto alimentario simple en el mercado para generar ingresos y tracción, antes de desarrollos técnicos complejos.

## Dónde estamos

1. **Estructura legal** definida en papel: una SpA en régimen Pro Pyme General, proyectos como divisiones internas, filiales solo por gatillos de riesgo. Pendiente: leer contratos de trabajo, pacto de accionistas, constitución. → `antecedentes/estructura-legal-company-builder.md`
2. **Banco de 58 ideas** agrupadas en cinco tesis, con priorización Fibonacci. → `antecedentes/banco-de-ideas.md`
3. **Exploraciones paralelas:** economía circular (15 ideas, falta elegir 1–2) y metodología de nicho socioecológico para consultoría. → `antecedentes/`
4. **En curso: estudio de mercado de alimentos.** Tres enfoques: (A) mercado local con fuentes digitales públicas, (B) benchmarking de productos en países comparables que no existen en Chile, (C) etnografía en terreno y en línea. Meta: lista corta de 3 a 5 productos al 11 de noviembre. → `plan/plan-estudio-mercado-alimentos.md`
   - Primeras pasadas hechas: demanda en Google Trends (100 términos) y competencia en Meta (A1, A2) → `entregables/2026-10-12_trends-y-meta_primera-pasada.md` y dashboard https://claude.ai/artifact/5S6M6umJvaDBJDjrENxKKt; fuentes macro SII y Aduanas (A4) → `datos/referencia/fuentes-macro-sii-aduanas.md`.
5. **Línea paralela de compras públicas:** venta de drones vía Mercado Público (licitación con cierre 14-oct) e intermediación con pymes.

## Criterios que el grupo ya usa

- Productos simples con presencia comercial antes que innovación técnica.
- Una oportunidad entra a la lista corta solo si aparece en 3 o más fuentes independientes.
- La innovación **no** es filtro de entrada (pendiente de acuerdo final).
- Velocidad de ingreso, capital de entrada, barrera regulatoria y compatibilidad con nuestros empleos actuales pesan en toda decisión.

## Activos y accesos útiles

- **Mayorístico.cl:** minimarket online de abarrotes que opera Boris con su mamá (Jumpseller). Da datos reales de rotación y un canal de prueba.
- **Redes de proveedores** en Santiago y Chillán vía negocios familiares (Mario).
- **Herramienta de alertas de Mercado Público** configurada por Boris.
- **Drive del proyecto** (organizado por Chalo): transcripciones, audios, historial de WhatsApp.

## Cómo trabajamos

Los tres trabajamos con agentes de IA sobre esta misma carpeta, sincronizada con git (GitHub). El protocolo detallado para los agentes está en `CLAUDE.md`; aquí va lo esencial.

### Qué documento es qué

| Documento | Para qué sirve | Cambia | Quién lo edita |
| --- | --- | --- | --- |
| `CONTEXTO.md` (este) | Visión, fase, criterios y reglas de trabajo | Poco: en la integración | Quien integra |
| `estado/boris.md` · `estado/mario.md` · `estado/chalo.md` | En qué está cada uno, qué terminó, qué sigue, bloqueos | En cada cierre de sesión | **Solo su dueño** |
| `estado/equipo.md` | Resumen del equipo y próximo hito | En la integración | Quien integra |
| `decisiones.md` | Lo acordado por el grupo | Tras cada acuerdo | Solo con acuerdo |
| `bitacora/` | Una entrada por sesión (un archivo nuevo cada vez) | En cada cierre | Cada uno las suyas |

**Al iniciar, el agente lee:** `CONTEXTO.md`, los tres archivos de `estado/` (y `estado/equipo.md`), `decisiones.md` y las entradas recientes de `bitacora/`. Así sabe la visión general y lo último de cada persona.

### Regla de git: nunca dos personas editan el mismo archivo

Los conflictos y los "stash" de GitHub Desktop aparecen cuando alguien tiene cambios **sin commit** en un archivo que otro también cambió. Para que no pase:

1. **Cada uno escribe solo en sus archivos:** su `estado/<persona>.md`, sus entradas de bitácora y sus datos o entregables. Los archivos compartidos (`CONTEXTO.md`, `estado/equipo.md`, `decisiones.md`, `CLAUDE.md`) se tocan solo en la integración o por acuerdo.
2. **Commit antes de Pull, siempre.** Al cerrar: **Commit → Pull → Push**. Al iniciar: si hay cambios sin commit, primero se commitean y después se hace Pull.
3. **Si aparece el diálogo de stash** en GitHub Desktop: elegir **Stash Changes and Continue** y después **Restore** en *Stashed Changes*. Nunca **Discard** sin revisar qué contiene. Ante cualquier duda, pedirle al agente que lo revise antes de tocar nada.
4. Archivos de prueba o generados por programas (`.Rhistory`, `.RData`, archivos de prueba) no se suben: van en `.gitignore` o se borran.

## Fuentes de este contexto

Documentos del Proyecto de Claude "Proyecto de Company Builder Social", notas de la reunión del 2026-10-10 (Chalo, Mario, Boris) y bitácoras del 10 al 13 de octubre.
