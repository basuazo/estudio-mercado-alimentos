#!/usr/bin/env python3
"""
Prepara los archivos del día para una captura manual y muestra los enlaces que hay que abrir.
No navega ningún sitio: solo crea CSV vacíos con el nombre correcto y arma los enlaces de búsqueda.

Uso (desde la raíz del repositorio):
    python scripts/preparar_captura.py mercadolibre                       # términos de prioridad 1
    python scripts/preparar_captura.py mercadolibre "cold brew" "matcha"  # términos a elección
    python scripts/preparar_captura.py meta --persona mario               # palabras clave por defecto
    python scripts/preparar_captura.py meta "electrolitos" "cold brew" --amplia

Opciones:
    --fecha AAAA-MM-DD   fecha de la captura (por defecto, hoy)
    --persona NOMBRE     boris, mario o chalo (solo Meta; queda en la columna persona)
    --amplia             Meta: búsqueda por palabras sueltas en vez de frase exacta

Salidas:
    datos/crudos/AAAA-MM-DD_mercadolibre_cl_<termino>.csv     (uno por término, solo encabezado)
    datos/crudos/AAAA-MM-DD_meta-ads-library_cl_captura.csv   (una fila por palabra clave, para completar)
Nunca sobrescribe un archivo que ya existe.
"""
import csv
import datetime
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote

RAIZ = Path(__file__).resolve().parent.parent
CRUDOS = RAIZ / "datos" / "crudos"

ML_POR_DEFECTO = ["electrolitos sobres", "bebida hidratante en polvo", "bebida proteica cafe",
                  "proteina lista para beber", "cold brew"]
META_POR_DEFECTO = ["electrolitos", "bebida hidratante", "bebida proteica", "proteina", "cold brew",
                    "matcha", "leche de avena", "yogurt griego", "barra de proteina", "sin azucar"]

ML_COLUMNAS = ["fecha", "termino", "posicion", "titulo", "marca", "vendedor", "tienda_oficial", "precio_clp",
               "formato", "precio_por_porcion_o_litro", "vendidos_visibles", "reputacion_vendedor",
               "envio_gratis", "url", "observaciones"]
META_COLUMNAS = ["fecha", "persona", "palabra_clave", "tipo_busqueda", "resultados_activos_aprox", "anunciante",
                 "anuncios_del_anunciante", "anuncio_mas_antiguo", "producto_pautado", "mensaje_principal",
                 "es_alimento_o_bebida", "url_busqueda", "nota"]


def slug(texto):
    t = unicodedata.normalize("NFD", texto.lower()).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def leer_opciones(args):
    op = {"fecha": datetime.date.today().isoformat(), "persona": "", "amplia": False, "terminos": []}
    i = 0
    while i < len(args):
        a = args[i]
        if a in ("--fecha", "--persona"):
            if i + 1 >= len(args):
                sys.exit(f"Falta el valor después de {a}")
            op[a[2:]] = args[i + 1].strip().lower()
            i += 2
            continue
        if a == "--amplia":
            op["amplia"] = True
        else:
            op["terminos"].append(a.strip())
        i += 1
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", op["fecha"]):
        sys.exit("La fecha debe ir como AAAA-MM-DD, por ejemplo 2026-10-25")
    return op


def enlace_ml(termino):
    return f"https://listado.mercadolibre.cl/{slug(termino)}"


def enlace_meta(termino, amplia):
    tipo = "keyword_unordered" if amplia else "keyword_exact_phrase"
    q = quote(termino) if amplia else quote(f'"{termino}"')
    return ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=CL"
            f"&media_type=all&q={q}&search_type={tipo}")


def preparar_ml(op):
    terminos = op["terminos"] or ML_POR_DEFECTO
    CRUDOS.mkdir(parents=True, exist_ok=True)
    print(f"\nMercado Libre, captura del {op['fecha']}\n")
    for t in terminos:
        ruta = CRUDOS / f"{op['fecha']}_mercadolibre_cl_{slug(t)}.csv"
        if ruta.exists():
            estado = "ya existía, no se tocó"
        else:
            with open(ruta, "w", encoding="utf-8-sig", newline="") as fh:
                csv.writer(fh).writerow(ML_COLUMNAS)
            estado = "creado"
        print(f"  {t}\n    archivo: datos/crudos/{ruta.name} ({estado})\n    abrir:   {enlace_ml(t)}\n")
    print("Anota los primeros 20 resultados de cada búsqueda (orden: Más relevantes).")
    print("Al terminar: python scripts/resumir_captura_mercadolibre.py resumir " + op["fecha"])


def preparar_meta(op):
    terminos = op["terminos"] or META_POR_DEFECTO
    tipo = "amplia" if op["amplia"] else "frase exacta"
    ruta = CRUDOS / f"{op['fecha']}_meta-ads-library_cl_captura.csv"
    CRUDOS.mkdir(parents=True, exist_ok=True)
    print(f"\nBiblioteca de anuncios de Meta (Chile, activos), captura del {op['fecha']}\n")
    if ruta.exists():
        print(f"  datos/crudos/{ruta.name} ya existe: no se tocó. Agrega filas a mano si quieres más palabras.\n")
    else:
        with open(ruta, "w", encoding="utf-8-sig", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(META_COLUMNAS)
            for t in terminos:
                fila = dict.fromkeys(META_COLUMNAS, "")
                fila.update(fecha=op["fecha"], persona=op["persona"], palabra_clave=t, tipo_busqueda=tipo,
                            url_busqueda=enlace_meta(t, op["amplia"]))
                w.writerow([fila[c] for c in META_COLUMNAS])
        print(f"  creado: datos/crudos/{ruta.name} ({len(terminos)} palabras clave)\n")
    for t in terminos:
        print(f"  {t}\n    {enlace_meta(t, op['amplia'])}")
    print("\nPor cada palabra: anota el total (~N resultados) y una fila por anunciante relevante (hasta 10).")
    print("Al terminar: python scripts/resumir_meta_ads.py " + op["fecha"])


def main():
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass
    if len(sys.argv) < 2 or sys.argv[1] not in ("mercadolibre", "meta"):
        print(__doc__)
        sys.exit(1)
    op = leer_opciones(sys.argv[2:])
    preparar_ml(op) if sys.argv[1] == "mercadolibre" else preparar_meta(op)


if __name__ == "__main__":
    main()
