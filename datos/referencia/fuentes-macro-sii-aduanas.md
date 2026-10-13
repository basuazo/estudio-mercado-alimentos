# Fuentes macro: SII y Aduanas (A4)

**Autor:** Chalo (con Claude) · **Revisado:** 2026-10-13 · **Paso del plan:** A4 Datos macro y de industria

## 1. Bases del SII

Ninguna tiene API: son archivos descargables (Excel .xlsb o ZIP con texto). Las cifras son preliminares y el SII las actualiza una vez al año.

### Prioridad alta para alimentos

| Base | Qué trae | Años | Archivo |
| --- | --- | --- | --- |
| Estadísticas de empresas: actividad económica | N° de empresas, ventas (UF), trabajadores dependientes y remuneraciones por actividad (6 dígitos) | 2005–2024 (act. oct-2025) | https://www.sii.cl/sobre_el_sii/empresas/PUB_ACT.xlsb |
| Ídem por tramo de ventas (5 tramos) y actividad | Lo mismo, por tamaño de empresa (micro a grande) | 2005–2024 | https://www.sii.cl/sobre_el_sii/empresas/PUB_TRAM5_ACT.xlsb |
| Ídem por región y actividad | Lo mismo, por región (Ñuble, RM) | 2005–2024 | https://www.sii.cl/sobre_el_sii/empresas/PUB_REG_ACT.xlsb |
| Ídem por comuna y actividad | Lo mismo, por comuna (Chillán, Santiago) | 2005–2024 | https://www.sii.cl/sobre_el_sii/empresas/PUB_COMU_ACT.xlsb |
| Todas las anteriores en formato abierto | Texto separado por tabulador (mejor para R/Python) | 2005–2024 | https://www.sii.cl/sobre_el_sii/empresas/EMPRESAS.zip |
| Nómina de empresas personas jurídicas | Una fila por empresa (sin RUT): rubro, subrubro y actividad principal, tramo de ventas, trabajadores, región, inicio y término de giro, tramo de capital | 2005–2024 (act. nov-2025) | https://www.sii.cl/estadisticas/nominas/PUB_EMPRESAS_PJ_2020_A_2024.zip (y bloques 2015–19, 2010–14, 2005–09) |
| Nómina de actividades económicas | Actividades inscritas y vigentes de cada persona jurídica | act. ago-2026 | https://www.sii.cl/estadisticas/nominas/PUB_NOM_ACTECOS.zip |
| Inicio de actividades y términos de giro | N° de empresas que nacen y cierran por rubro, región y año (dinamismo) | 2005–2024 | https://www.sii.cl/sobre_el_sii/estadisticas/ciclo_de_vida/Ciclo_Vida.zip |

### Complementarias

- Rubro y subrubro, solas o cruzadas con región, comuna, tramo y tramo de trabajadores: misma página, archivos `PUB_RUBR*`, `PUB_SUBR*`. https://www.sii.cl/sobre_el_sii/estadisticas_de_empresas.html
- Nómina de direcciones (casa matriz y sucursales) y de razón social de personas jurídicas: https://www.sii.cl/sobre_el_sii/nominapersonasjuridicas.html
- Estadísticas de principales formularios (F22, F29) por rubro y tamaño: https://www.sii.cl/sobre_el_sii/estadisticas_de_principales_formularios.html
- Nómina de grandes contribuyentes: https://www.sii.cl/contribuyentes/empresas_por_tamano/nomina_gc.zip
- Serie antigua por rubro, subrubro y actividad (2005–2015, superada por la de arriba): https://www.sii.cl/sobre_el_sii/empresas_rubro.html

### Actividades a filtrar (CIIU4.CL; el SII usa códigos de 6 dígitos que parten con estos 4)

**Por confirmar** contra el clasificador que viene en el ZIP.

- Elaboración de alimentos (división 10): 1050 lácteos, 1061 molinería (avena, cereales), 1071 panadería, 1073 cacao, chocolate y confites (barras), 1075 comidas preparadas, 1079 otros productos alimenticios n.c.p. (granola, snacks, suplementos), 1030 frutas y hortalizas (jugos, deshidratados).
- Bebidas (división 11): 1104 bebidas no alcohólicas y aguas minerales.
- Comercio: 4630 mayorista de alimentos y bebidas; 4711 minorista no especializado (supermercados, minimarkets); 4721 y 4722 minorista especializado en alimentos y bebidas.

## 2. ¿Hay API?

- **SII: no, para estadísticas.** Sus servicios web son para facturación electrónica y requieren certificado digital. Algunas empresas venden APIs de consulta por RUT, pero eso no sirve para mapear la industria. Además, raspar datos de sii.cl caería en la revisión legal que hace Mario.
- **Alternativa:** descargar `EMPRESAS.zip` y las nóminas una vez al año y cargarlas en R o Python. Basta un script que filtre las actividades de arriba.
- **APIs oficiales útiles para el contexto:**
  - [API BDE del Banco Central](https://si3.bcentral.cl/estadisticas/Principal1/Web_Services/index_API_sec1_es.htm): gratuita, pide registro. Tiene series de cuentas nacionales, precios y comercio exterior; falta confirmar qué tan desagregadas están para alimentos.
  - datos.gob.cl: tiene la API de catálogo CKAN. Falta confirmar si hay bases del SII ahí.

## 3. Aduanas

- Aduanas publica bases mensuales de importaciones (DIN) y exportaciones en su sitio, a nivel de partida arancelaria (por confirmar: no se pudo abrir la página desde la sesión). https://www.aduana.cl/transparencia/2016/datosestadmens.html
- No tiene API oficial. Existen scrapers de terceros, de pago, con los mismos datos (ej. Apify): revisarlos en la validación legal.
- **Alternativa con API:** UN Comtrade (gratis con clave), que tiene importaciones de Chile por código del Sistema Armonizado a 6 dígitos y país de origen. Códigos candidatos: 1904 (granola y cereales), 1905 (galletas y barras), 2009 (jugos), 2106 (preparaciones alimenticias y suplementos), 2202 (aguas y bebidas no alcohólicas), 0403 y 0402 (yogurt y leches).

## Pendientes

- [ ] Descargar `EMPRESAS.zip` y la nómina 2020–2024. Desde el entorno de Claude no se puede (sii.cl está bloqueado), así que hay que hacerlo desde el navegador y dejar los archivos en `datos/crudos/`.
- [ ] Confirmar los códigos de actividad con el clasificador del SII.
- [ ] Revisar la página de bases mensuales de Aduanas y probar UN Comtrade con las partidas de arriba.
