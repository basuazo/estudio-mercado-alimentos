"""
Diccionario de términos de Google Ads por oportunidad (rediseño del 2026-10-17, tras la auditoría del 16-oct).

En vez de agrupar términos con expresiones regulares escondidas en el script, cada término queda en una tabla
revisable por personas: datos/referencia/google-ads_terminos.csv

Columnas: oportunidad, termino, tipo, concepto, busquedas_mes_chile, cpc_alto_clp, competencia, fuente,
          es_clave_radar, validado, nota
  tipo:
    especifico      describe el formato o producto que estudiamos ("electrolitos en sobre")   -> cuenta en el índice
    paraguas        la categoría amplia ("electrolitos", "matcha latte")                       -> solo techo
    otro_producto   otro producto que comparte palabras ("suero oral", "proteína en polvo")    -> no cuenta
    informativo     busca información o recetas ("para qué sirve", "receta")                  -> no cuenta
    marca           busca una marca ("david rio chai")                                         -> no cuenta
  concepto: variantes de un mismo término se agrupan y se toma el máximo, no la suma.

Uso:
    python scripts/google_ads_terminos.py proponer [AAAA-MM-DD]   # arma o completa el diccionario (no pisa lo validado)
    python scripts/google_ads_terminos.py importar <carpeta>      # aplica lo validado en la mesa (JSON por documento)
    python scripts/google_ads_terminos.py json [AAAA-MM-DD]       # exporta lo que se muestra en la mesa de validación
Después: python scripts/actualizar_radar_google_ads.py
"""
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
LIMPIOS = RAIZ / "datos" / "limpios"
DICC = RAIZ / "datos" / "referencia" / "google-ads_terminos.csv"
CAMPOS = ["oportunidad", "termino", "tipo", "concepto", "busquedas_mes_chile", "cpc_alto_clp", "competencia", "fuente",
          "es_clave_radar", "validado", "nota"]


def n(s):
    return unicodedata.normalize("NFD", (s or "").lower()).encode("ascii", "ignore").decode().strip()


INFORMATIVO = (r"\b(que es|que son|para que sirve|sirve|beneficio|como (se )?(hace|hacer|prepara|preparar|tomar|usar)|"
               r"receta|propiedades|contraindicacion|cuando tomar|calorias|significado|wikipedia|efectos|dano|hace mal|"
               r"diferencia|vs|cuanto|cuantas|dosis|historia|origen|casera|casero|todo sobre|aumentar masa|bajar de peso)\b")
OTRO_PAIS = r"\b(guadalajara|mexico|cdmx|monterrey|espana|madrid|argentina|peru|colombia|bogota|oxxo|walmart|costco)\b"
MARCAS = (r"\b(david rio|marley|starbucks|oregon|arkadia|andes tea|twinings|suerox|gatorade|powerade|electrolit|"
          r"pedialyte|liquid iv|lmnt|amazing care|extra life|nescafe|dolce gusto|loncoleche|soprole|colun|nestle|"
          r"milo|notco|not co|akapro|nude|briu|lavazza|wandering bear|califia|oatly|alpro|tazo|lipton|matcha dna|"
          r"mercadona|lider|jumbo|tottus|unimarc|costco|walmart|ito en|celsius|monster|red bull|prime)\b")

# Oportunidad: (pertenece, especifico, otro_producto, termino clave actual del radar)
OPORTUNIDADES = {
    "Sobres y tabletas de electrolitos": (
        r"electrolit|isoton|hidratante|suero oral|sales de hidrat|rehidrat",
        r"(sobre|sachet|stick|polvo|tableta|efervescente|pastilla).*(electrolit|hidrat|isoton)|(electrolit|hidrat|isoton).*(sobre|sachet|stick|polvo|tableta|efervescente|pastilla)",
        r"suero oral|suero de rehidrat|orales|agua con electrolit|agua electrolit|bebida isotonica (botella|lata)",
        "electrolitos en sobre"),
    "Cafe o batido proteico listo para beber 20-30 g": (
        r"protei|whey|batido|shake",
        r"cafe protei|protei.*(lista|listo) para (beber|tomar)|bebida protei|shake protei|protein shake|batido protei.*(listo|botella|lata|caja)|protei.*(botella|lata|rtd)",
        r"polvo|whey|scoop|creatina|barra|yogur|leche protei|vegetal|isolate|aislada|hidrolizada|pancake|panqueque|galleta",
        "batido de proteina"),
    "Avena barista para cafeterias (foodservice)": (
        r"\bavena\b", r"barista", r"hojuela|harina|copos|salvado|galleta|grano|integral", "leche de avena barista"),
    "Matcha listo para beber": (
        r"matcha",
        r"(lista|listo) para (beber|tomar)|\blata\b|botella|\brtd\b|embotellad|bebida de matcha|matcha helado (botella|lata)",
        r"polvo|ceremonial|organico|kit|batidor|chasen|taza|cuenco|galleta|pastel|torta|helado$|crema|mascarilla|capsula",
        "matcha latte"),
    "Cold brew local sin azucar": (
        r"cold ?brew|cafe frio|cafe helado",
        r"embotellad|\blata\b|botella|listo|lista|concentrad|sin azucar|rtd|^cold ?brew$|^cafe cold ?brew$",
        r"cafetera|maquina|jarra|filtro|hario|toddy|grano|molido|prensa|french press|bodum",
        "cold brew"),
    "Granola con legumbre a bajo precio (marca propia)": (
        r"granola", r"legumbre|garbanzo|lenteja|protei|sin azucar|barata|precio|kilo|1 ?kg", r"barra|receta", "granola"),
    "Leche sin lactosa y sin lactosa como atributo": (
        r"lactosa", r"leche sin lactosa|leche deslactosada", r"intoleran|enzima|pastilla", "leche sin lactosa"),
    "Jugos prensados en frio y shots": (
        r"\bjugo|\bshot", r"prensad|cold press|shot de|shots? (de )?(jengibre|curcuma)|jugo verde", r"extractor|maquina|juguera|licuadora", "jugo prensado en frio"),
    "Agua con gas saborizada sin azucar en formato familiar": (
        r"agua (con gas|saborizada|mineral|gasificada)", r"con gas saborizada|saborizada con gas|gasificada saborizada|agua con gas (sabor|limon|frutilla|pomelo)",
        r"maquina|sodastream|purificador|filtro", "agua con gas saborizada"),
    "Snack horneado de lentejas o garbanzo": (
        r"garbanzo|lenteja|legumbre|hummus", r"chips|snack|crocante|tostad|horneado|crujiente|picoteo", r"hummus|harina|cocid|conserva", "chips de garbanzo"),
    "Yogur griego proteico formato familiar 500 g a 1 kg sin azucar": (
        r"yogur", r"protei|griego (natural|sin azucar|1 ?kg|kilo|familiar)|alto en protei", r"maquina|yogurtera|bebible|receta", "yogurt proteico"),
    "Tes helados sin azucar": (
        r"\bte helado|iced tea|\bte frio|ice tea", r"sin azucar|zero|light|sin endulzante", r"receta", "te helado"),
    "Pan de masa madre": (
        r"masa madre", r"pan de masa madre|pan masa madre", r"curso|receta|como hacer|iniciar", "pan de masa madre"),
    "Kimchi y fermentados de verdura": (
        r"kimchi|ferment|chucrut|sauerkraut|encurtid", r"comprar|precio|donde|envasad|frasco|alimentos fermentados|chucrut|sauerkraut",
        r"receta|como hacer|kombucha|kefir|yogur|vino|cerveza", "kimchi"),
    "Tofu y proteina vegetal": (
        r"\btofu|proteina vegetal", r"proteina vegetal|tofu (firme|ahumado|precio|comprar|organico)", r"polvo|whey|receta", "tofu"),
    "Creatina en gomitas y formatos nuevos": (
        r"creatin", r"gomita|gummies|gomas|masticable", r"monohidrat|polvo|capsula", "creatina"),
    "Productos sin sellos": (
        r"sellos|sin sello", r"sin sellos|libre de sellos|sin sello", r"ley|normativa", "sin sellos"),
    "Chai latte en polvo o concentrado": (
        r"\bchai\b", r"instantane|polvo|sobres?|concentrad|premezcla|mezcla", r"capsula|dolce gusto|receta|jarabe|syrup|monin|te en hojas|bolsitas", "chai latte"),
    "Comida liofilizada de montana (outdoor y trekking)": (
        r"liofiliz|comida (de )?(montana|trekking|camping|emergencia)|deshidratad", r"comida liofilizada|comida (de )?(montana|trekking|camping)|liofilizad.*(comida|plato|outdoor)",
        r"fruta|frutilla|maquina|liofilizador|leche|helado|mascota", "comida liofilizada"),
    "Fruta liofilizada como snack": (
        r"liofiliz", r"fruta liofilizada|(frutilla|fresa|mango|platano|manzana|frambuesa|arandano) liofilizad", r"maquina|liofilizador|comida", "fruta liofilizada"),
    "Ginger beer sin alcohol": (
        r"ginger (beer|ale)|cerveza de jengibre", r"ginger beer|cerveza de jengibre", r"ginger ale|receta", "ginger beer"),
    "Agua de coco": (
        r"agua de coco|coco water", r"agua de coco", r"coco rallado|aceite|leche de coco", "agua de coco"),
    "Compra al por mayor en linea (canal)": (
        r"por mayor|mayorista|granel", r"bebidas por mayor|abarrotes por mayor|tienda a granel|almacen mayorista|mayorista (online|en linea)",
        r"ropa|juguete|perfume|cosmetico|celular", "bebidas por mayor"),
}
STOP = {"de", "en", "la", "el", "los", "las", "para", "con", "y", "te", "tea", "the", "chile", "a", "latte", "leche"}


def singular(w):
    return w[:-1] if w.endswith("s") and len(w) > 4 else w


def concepto(t):
    """Variantes del mismo término comparten concepto: sin artículos, en singular y sin importar el orden."""
    return " ".join(sorted({singular(w) for w in re.findall(r"[a-z0-9]+", n(t)) if w not in STOP})) or n(t)


def clasificar(op, termino):
    pertenece, especifico, otro, clave = OPORTUNIDADES[op]
    t = n(termino)
    if re.search(INFORMATIVO, t):
        return "informativo"
    if re.search(MARCAS, t):
        return "marca"
    if re.search(OTRO_PAIS, t):
        return "otro_producto"
    if otro and re.search(otro, t):
        return "otro_producto"
    if re.search(especifico, t):
        return "especifico"
    return "paraguas"


def num(x):
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return ""


def leer_volumenes(fecha):
    vols = {}
    for r in csv.DictReader(open(LIMPIOS / f"{fecha}_google-ads_volumenes_114.csv", encoding="utf-8-sig")):
        vols[r["termino"].strip()] = (r, "lista 114")
    for r in csv.DictReader(open(LIMPIOS / f"{fecha}_google-ads_ideas_por_candidata.csv", encoding="utf-8-sig")):
        vols.setdefault(r["idea"].strip(), (r, "ideas"))
    return vols


def leer_dicc():
    if not DICC.exists():
        return {}
    return {(f["oportunidad"], f["termino"]): f for f in csv.DictReader(open(DICC, encoding="utf-8-sig"))}


def escribir_dicc(filas):
    filas = sorted(filas.values(), key=lambda f: (f["oportunidad"], ["especifico", "paraguas", "otro_producto", "marca", "informativo"].index(f["tipo"]) if f["tipo"] in ("especifico", "paraguas", "otro_producto", "marca", "informativo") else 9, -(num(f["busquedas_mes_chile"]) or 0), f["termino"]))
    with open(DICC, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=CAMPOS, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)


def cmd_proponer(fecha):
    vols = leer_volumenes(fecha)
    dicc = leer_dicc()
    nuevos = 0
    for termino, (r, fuente) in vols.items():
        for op, (pertenece, *_ , clave) in OPORTUNIDADES.items():
            if not re.search(pertenece, n(termino)):
                continue
            k = (op, termino)
            base = {"oportunidad": op, "termino": termino, "busquedas_mes_chile": num(r.get("busquedas_mes_chile")),
                    "cpc_alto_clp": num(r.get("cpc_alto_clp")), "competencia": r.get("competencia", ""), "fuente": fuente,
                    "es_clave_radar": "si" if n(termino) == n(clave) else ""}
            if k in dicc and dicc[k].get("validado") == "si":
                dicc[k].update(base)  # se actualizan los números, no lo validado
                continue
            if k not in dicc:
                nuevos += 1
            dicc[k] = {**base, "tipo": clasificar(op, termino), "concepto": concepto(termino), "validado": "", "nota": ""}
    escribir_dicc(dicc)
    print(f"Diccionario: {len(dicc)} filas ({nuevos} nuevas) -> {DICC.relative_to(RAIZ)}")


def cmd_importar(carpeta):
    dicc = leer_dicc()
    n_ok = 0
    for p in sorted(Path(carpeta).glob("*.json")):
        d = json.load(open(p, encoding="utf-8"))
        d = d.get("data", d)
        k = (d.get("oportunidad"), d.get("termino"))
        if k in dicc:
            dicc[k].update({"tipo": d.get("tipo", dicc[k]["tipo"]), "concepto": d.get("concepto") or dicc[k]["concepto"],
                            "nota": d.get("nota", ""), "validado": "si"})
            n_ok += 1
    escribir_dicc(dicc)
    print(f"{n_ok} términos validados aplicados al diccionario")


def cmd_json(fecha):
    """Lo que se muestra en la mesa: todo término con 500+ búsquedas, todo específico y todo término clave."""
    dicc = leer_dicc()
    filas = [f for f in dicc.values() if (num(f["busquedas_mes_chile"]) or 0) >= 500 or f["tipo"] == "especifico" or f["es_clave_radar"]]
    out = LIMPIOS / f"{fecha}_google-ads_terminos_para_validar.json"
    json.dump({"fecha": fecha, "oportunidades": list(OPORTUNIDADES), "filas": filas}, open(out, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"{len(filas)} términos para validar -> {out.relative_to(RAIZ)}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    arg = sys.argv[2] if len(sys.argv) > 2 else "2026-10-16"
    {"proponer": cmd_proponer, "importar": cmd_importar, "json": cmd_json}.get(cmd, lambda _: sys.exit(__doc__))(arg)
