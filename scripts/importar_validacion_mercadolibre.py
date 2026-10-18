"""
Pasa al repositorio lo validado en la mesa de validación (artefacto "Mesa de validación ML").

El agente descarga la base del artefacto como JSON (un archivo por documento) en una carpeta, por ejemplo:
    <carpeta>/validacion/<termino>~<id_pub>.json
    <carpeta>/marcas/<marca>.json
y corre:
    python scripts/importar_validacion_mercadolibre.py <carpeta>

Escribe (reemplaza):
    datos/referencia/mercadolibre_validacion.csv          una fila por publicación validada
    datos/referencia/mercadolibre_marcas_corregidas.csv   marca detectada -> nombre correcto
Luego: python scripts/resumir_captura_mercadolibre.py resumir
"""
import csv
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REF = RAIZ / "datos" / "referencia"
CAMPOS = ["id_pub", "termino", "clase", "tipo", "marca", "envases", "contenido", "unidad", "porciones", "medir_por", "precio_clp",
          "nota", "validado_por", "fecha_validacion"]


def leer(carpeta):
    for p in sorted(Path(carpeta).glob("*.json")):
        d = json.load(open(p, encoding="utf-8"))
        yield d.get("data", d)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    base = Path(sys.argv[1])
    filas = [v for v in leer(base / "validacion") if v.get("id_pub") and v.get("termino")]
    filas.sort(key=lambda v: (v["termino"], v["id_pub"]))
    with open(REF / "mercadolibre_validacion.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=CAMPOS, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)
    marcas = [m for m in leer(base / "marcas") if m.get("detectada") and m.get("canonica")
              and m["detectada"] != m["canonica"]]
    with open(REF / "mercadolibre_marcas_corregidas.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["detectada", "canonica"], lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(sorted(marcas, key=lambda m: m["detectada"]))
    print(f"{len(filas)} publicaciones validadas y {len(marcas)} marcas corregidas guardadas en datos/referencia/")


if __name__ == "__main__":
    main()
