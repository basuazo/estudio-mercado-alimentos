"""
Limpia el catálogo bajado por scripts/mercadolibre_api.ps1 y lo clasifica por búsqueda.

Uso (desde la raíz del repositorio):
    python scripts/limpiar_catalogo_mercadolibre.py                      # usa el catálogo más reciente
    python scripts/limpiar_catalogo_mercadolibre.py datos/crudos/2026-10-16_mercadolibre-api_catalogo.csv

Entrada:  datos/crudos/AAAA-MM-DD_mercadolibre-api_catalogo.csv
Salida:   datos/limpios/AAAA-MM-DD_mercadolibre-api_catalogo_limpio.csv   (una fila por ficha, con clasificación)
          datos/limpios/AAAA-MM-DD_mercadolibre-api_catalogo_resumen.csv  (una fila por búsqueda)

Clasificación de cada ficha respecto de la búsqueda que la trajo:
  objetivo   = es el producto que se buscaba (ej. electrolitos en sobre, café proteico listo para beber)
  adyacente  = mismo rubro pero otro formato o uso (ej. matcha en polvo, cafetera cold brew, fruta liofilizada)
  ruido      = no es alimento ni bebida del rubro (ej. extractoras, licores, toallas color matcha)
Las reglas están en REGLAS: si aparece una búsqueda nueva en el script de la API, agrégala aquí.
Requisitos: Python 3.9+, sin librerías externas.
"""
import csv
import glob
import re
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Dominios que nunca son alimento o bebida del estudio
RUIDO_SIEMPRE = {
    "BOOKS", "BACKPACKS", "BATH_TOWELS", "FACIAL_TOWELS", "DESKTOP_COMPUTER_CASES", "BONGS",
    "COCKTAIL_SHAKERS", "LIP_LINERS", "NAIL_POLISH", "EYESHADOWS", "STUFFED_TOYS", "BAR_SOAPS",
    "BODY_SKIN_CARE_PRODUCTS", "LIQUID_HAND_AND_BODY_SOAPS", "ESSENTIAL_OILS", "HYDROMETERS_AND_DENSIMETERS",
    "FISH_FOODS", "CANTEENS", "LIQUORS", "GINS",
}
EQUIPOS = {"JUICERS", "ELECTRIC_SQUEEZERS", "ELECTRIC_COFFEE_MAKERS", "MANUAL_COFFEE_MAKERS", "TEA_INFUSERS"}


def tiene(texto, patron):
    return re.search(patron, texto, re.I) is not None


def clasificar(busqueda, dominio, nombre):
    """Devuelve (clasificacion, motivo)."""
    d = dominio.replace("MLC-", "")
    n = nombre
    if d in RUIDO_SIEMPRE:
        return "ruido", f"dominio fuera del rubro ({d})"

    if busqueda in ("electrolitos", "electrolitos sobres", "bebida hidratante en polvo"):
        if d in ("SUPPLEMENTS", "SPORTS_DRINKS", "SOFT_DRINKS"):
            if tiene(n, r"electrolit|hidrat|isot[oó]n|suero|sales|rehidrat|hydra|polvo|sobre"):
                return "objetivo", "hidratación o electrolitos"
            return "adyacente", "suplemento o bebida deportiva sin mención de hidratación"
        return "ruido", f"dominio {d}"

    if busqueda == "bebida proteica cafe":
        if tiene(n, r"\bcaf[eé]\b|capuc|cappuc|latte|\bmoca\b|mocha|espresso"):
            if tiene(n, r"polvo|mezcla|\b\d{3,4}\s?g\b"):
                return "adyacente", "proteína sabor café en polvo"
            return "objetivo", "bebida proteica sabor café"
        if d in ("SUPPLEMENTS", "MILK", "SWEET_PREMIXES"):
            return "adyacente", "bebida proteica de otro sabor o en polvo"
        return "ruido", f"dominio {d}"

    if busqueda == "proteina lista para beber":
        if tiene(n, r"prote|whey|malteada|shake"):
            return "objetivo", "proteína lista para beber"
        return "ruido", "coincidencia solo por 'lista para beber'"

    if busqueda == "cold brew":
        if d in EQUIPOS:
            return "adyacente", "cafetera o equipo para cold brew"
        if d in ("INSTANT_COFFEE", "FLAVORED_WATERS", "ENERGY_DRINKS") and tiene(n, r"cold brew"):
            return "objetivo", "café cold brew listo o concentrado"
        if d == "GROUND_AND_WHOLE_BEANS_COFFEE":
            return "adyacente", "café molido para preparar cold brew"
        if d in ("ICED_TEA", "TEA"):
            return "adyacente", "té en frío (no café)"
        return "ruido", f"dominio {d}"

    if busqueda == "leche de avena barista":
        if d in ("MILK", "OATMEAL") and tiene(n, r"avena|oat"):
            if tiene(n, r"barista|espumar"):
                return "objetivo", "bebida de avena barista"
            return "adyacente", "bebida de avena no barista"
        return "ruido", f"dominio {d}"

    if busqueda == "matcha":
        if d in EQUIPOS:
            return "adyacente", "accesorio para preparar matcha"
        if d in ("TEA", "SUPPLEMENTS") and tiene(n, r"matcha"):
            if tiene(n, r"concentrad|listo para|\blata\b|botella"):
                return "objetivo", "matcha líquido o listo para beber"
            return "adyacente", "matcha en polvo o bolsitas (no listo para beber)"
        return "ruido", f"dominio {d}"

    if busqueda == "chai latte":
        if d in ("TEA", "INSTANT_COFFEE", "READY_TO_DRINK_COCKTAILS") and tiene(n, r"chai"):
            return "objetivo", "chai latte (polvo, concentrado o listo)"
        return "ruido", f"dominio {d}"

    if busqueda == "comida liofilizada":
        if tiene(n, r"monta[ñn]a|mountain|outdoor|trekking|camps foods|mi men[uú]|risott?o|guiso|pasta|arroz|sopa|bocadillo|strogonoff|curry"):
            return "objetivo", "comida liofilizada de montaña o lista para hidratar"
        if tiene(n, r"fruta|fresa|frambuesa|zarzamora|pi[ñn]a|mora|granola"):
            return "adyacente", "fruta liofilizada o snack con fruta liofilizada"
        return "adyacente", "otro ingrediente liofilizado (leche, harina, jalea, salsa)"

    if busqueda == "jugo prensado en frio":
        if d == "JUICES":
            return "objetivo", "jugo envasado"
        if d in EQUIPOS:
            return "ruido", "extractora de jugos"
        return "ruido", f"dominio {d}"

    if busqueda == "snack de lentejas":
        if tiene(n, r"snack|chips|crocante|tostad|horneado|puff"):
            return "objetivo", "snack de legumbre"
        if tiene(n, r"outdoor|guisad|cocid|lata|tocino"):
            return "adyacente", "lenteja preparada o en conserva"
        return "adyacente", "lenteja a granel (no snack)"

    # Búsqueda sin regla: se clasifica solo por dominio
    return ("ruido", f"dominio {d}") if d in EQUIPOS else ("sin_regla", "agregar regla para esta búsqueda")


def formato(nombre, peso, volumen, unidades):
    t = " ".join([nombre, peso or "", volumen or "", unidades or ""])
    if tiene(t, r"c[aá]psula|k-cup|pastilla|tableta"):
        return "capsulas_o_tabletas"
    if tiene(t, r"sobre|stick|sachet|bolsita|saquito|bags"):
        return "sobres"
    if tiene(t, r"polvo|instant[aá]ne|mezcla|\b\d+(\.\d+)?\s?(g|gr|grs|kg|kilo|lb|oz)\b"):
        if tiene(t, r"\bml\b|\bcc\b|\blitro|\b\d\s?l\b|lata|botella|concentrad|liquid|l[ií]quid"):
            return "liquido"
        return "polvo_o_solido"
    if tiene(t, r"\bml\b|\bcc\b|litro|\b\d\s?l\b|lata|botella|concentrad|l[ií]quid|lista para"):
        return "liquido"
    return "sin_dato"


PREFIJOS = [  # (desde, hasta, país) para GTIN-13; pista de registro, no de origen
    (0, 139, "EEUU/Canadá"), (300, 379, "Francia"), (400, 440, "Alemania"), (450, 459, "Japón"),
    (490, 499, "Japón"), (500, 509, "Reino Unido"), (540, 549, "Bélgica"), (560, 560, "Portugal"),
    (690, 699, "China"), (750, 750, "México"), (760, 769, "Suiza"), (770, 771, "Colombia"),
    (773, 773, "Uruguay"), (775, 775, "Perú"), (778, 779, "Argentina"), (780, 780, "Chile"),
    (784, 784, "Paraguay"), (786, 786, "Ecuador"), (789, 790, "Brasil"), (800, 839, "Italia"),
    (840, 849, "España"), (870, 879, "Países Bajos"), (880, 880, "Corea del Sur"), (885, 885, "Tailandia"),
    (890, 890, "India"), (893, 893, "Vietnam"), (930, 939, "Australia"), (940, 949, "Nueva Zelanda"),
]


def pais_gtin(gtin):
    g = re.sub(r"\D", "", gtin or "")
    if len(g) == 12:
        return "EEUU/Canadá"
    if len(g) != 13:
        return ""
    p = int(g[:3])
    for a, b, pais in PREFIJOS:
        if a <= p <= b:
            return pais
    return f"otro ({g[:3]})"


def main():
    if len(sys.argv) > 1:
        entrada = Path(sys.argv[1])
    else:
        archivos = sorted(glob.glob(str(RAIZ / "datos" / "crudos" / "*_mercadolibre-api_catalogo.csv")))
        if not archivos:
            sys.exit("No hay catálogos en datos/crudos/. Corre primero scripts/mercadolibre_api.ps1")
        entrada = Path(archivos[-1])
    fecha = entrada.name[:10]
    filas = list(csv.DictReader(entrada.open(encoding="utf-8-sig")))

    limpias = []
    for f in filas:
        clase, motivo = clasificar(f["busqueda"], f["dominio"], f["nombre"])
        f = dict(f)
        f["clasificacion"] = clase
        f["motivo"] = motivo
        f["formato_inferido"] = formato(f["nombre"], f.get("peso_neto"), f.get("volumen"), f.get("unidades"))
        f["pais_registro_gtin"] = pais_gtin(f.get("gtin"))
        limpias.append(f)

    cols = list(filas[0].keys())
    cols = cols[:8] + ["clasificacion", "motivo", "formato_inferido", "pais_registro_gtin"] + cols[8:]
    salida = RAIZ / "datos" / "limpios" / f"{fecha}_mercadolibre-api_catalogo_limpio.csv"
    with salida.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(limpias)

    resumen = []
    for b in dict.fromkeys(f["busqueda"] for f in limpias):
        g = [f for f in limpias if f["busqueda"] == b]
        obj = [f for f in g if f["clasificacion"] == "objetivo"]
        marcas = Counter(f["marca"] for f in obj if f["marca"])
        paises = Counter(f["pais_registro_gtin"] for f in obj if f["pais_registro_gtin"])
        formatos = Counter(f["formato_inferido"] for f in obj)
        resumen.append({
            "fecha_captura": fecha,
            "busqueda": b,
            "total_informado_api": g[0].get("total_busqueda", ""),
            "fichas_leidas": len(g),
            "objetivo": len(obj),
            "adyacente": sum(f["clasificacion"] == "adyacente" for f in g),
            "ruido": sum(f["clasificacion"] == "ruido" for f in g),
            "pct_objetivo": round(100 * len(obj) / len(g)) if g else 0,
            "marcas_objetivo": len(marcas),
            "marcas_principales": " | ".join(f"{m} ({n})" for m, n in marcas.most_common(6)),
            "formatos_objetivo": " | ".join(f"{k} ({n})" for k, n in formatos.most_common()),
            "pais_registro_gtin_objetivo": " | ".join(f"{k} ({n})" for k, n in paises.most_common(5)),
            "fuente": str(entrada.relative_to(RAIZ)).replace("\\", "/"),
        })
    salida_r = RAIZ / "datos" / "limpios" / f"{fecha}_mercadolibre-api_catalogo_resumen.csv"
    with salida_r.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(resumen[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(resumen)

    sin = sum(f["clasificacion"] == "sin_regla" for f in limpias)
    print(f"Guardado: {salida.relative_to(RAIZ)} ({len(limpias)} fichas)")
    print(f"Guardado: {salida_r.relative_to(RAIZ)} ({len(resumen)} búsquedas)")
    if sin:
        print(f"Atención: {sin} fichas de búsquedas sin regla; agrégalas en REGLAS.")


if __name__ == "__main__":
    main()
