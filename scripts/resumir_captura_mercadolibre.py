"""
Procesa la captura de Mercado Libre en tres capas (rediseño del 2026-10-17, tras la auditoría del 16-oct):

  1. CRUDO      datos/crudos/AAAA-MM-DD_mercadolibre_cl_<termino>.csv   (lo que trae la función de consola; no se toca)
  2. VALIDACIÓN datos/referencia/mercadolibre_validacion.csv           (lo que decide una persona, por publicación)
  3. CÁLCULO    este script: combina 1 + 2 y, donde no hay validación, usa una PROPUESTA automática con su confianza.

Uso (desde la raíz del repositorio):
    python scripts/resumir_captura_mercadolibre.py proponer [AAAA-MM-DD]   # propuesta para la mesa de validación
    python scripts/resumir_captura_mercadolibre.py resumir  [AAAA-MM-DD]   # captura limpia + resumen por término y tipo
    python scripts/resumir_captura_mercadolibre.py probar                  # casos de prueba de la auditoría

Salidas:
    datos/limpios/AAAA-MM-DD_mercadolibre_cl_propuesta.csv  y  .json  (una fila por publicación única, para validar)
    datos/limpios/AAAA-MM-DD_mercadolibre_cl_captura.csv               (filas finales, con origen de cada dato)
    datos/limpios/AAAA-MM-DD_mercadolibre_cl_resumen.csv              (por término y tipo de producto)

Reglas clave:
  - Filas pegadas desde otro término (mismo título y precio en otro archivo, con etiqueta distinta) se separan
    como "contaminada" y se reportan; duplicados dentro de un término se cuentan una vez.
  - Precio por unidad = precio / (envases x contenido) o / porciones; la unidad depende del término y del tipo.
  - Lo que no se capturó (vendidos, vendedor, tienda oficial) queda vacío, nunca en cero.
  - Marcas: datos/referencia/marcas_mercadolibre.csv (marca, patrón). Se amplía al validar.
"""
import csv
import hashlib
import json
import re
import statistics
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CRUDOS = RAIZ / "datos" / "crudos"
LIMPIOS = RAIZ / "datos" / "limpios"
REF = RAIZ / "datos" / "referencia"
VALIDACION = REF / "mercadolibre_validacion.csv"
CAMPOS_VALIDACION = ["id_pub", "termino", "clase", "tipo", "marca", "envases", "contenido", "unidad",
                     "porciones", "medir_por", "precio_clp", "nota", "validado_por", "fecha_validacion"]

# ---------------------------------------------------------------------------------------------------------------
# Configuración por término: qué tipos son objetivo, cuáles adyacentes, y en qué unidad se mide el precio.
# unidad por tipo: "litro" (CLP/L), "kilo" (CLP/kg), "porcion" (CLP por porción, sobre o plato).
# ---------------------------------------------------------------------------------------------------------------
TERMINOS = {
    "electrolitos sobres": {
        "pertenece": r"electrolit|hidrat|isoton|suero|rehidrat|sales\b|gatorade|powerade|suerox|lmnt|hydrat|electrolyte",
        "objetivo": ["sobre"], "adyacente": ["polvo", "tabletas", "rtd", "capsulas", "gomitas"],
        "unidad": {"sobre": "porcion", "polvo": "porcion", "tabletas": "porcion", "rtd": "litro",
                   "capsulas": "porcion", "gomitas": "porcion"},
    },
    "bebida hidratante en polvo": {
        "pertenece": r"electrolit|hidrat|isoton|suero|rehidrat|gatorade|powerade|suerox|lmnt|hydrat|electrolyte",
        "objetivo": ["sobre", "polvo"], "adyacente": ["tabletas", "rtd", "capsulas", "gomitas"],
        "unidad": {"sobre": "porcion", "polvo": "porcion", "tabletas": "porcion", "rtd": "litro",
                   "capsulas": "porcion", "gomitas": "porcion"},
    },
    "bebida proteica cafe": {
        "pertenece": r"prote|whey",
        "objetivo": ["rtd"], "adyacente": ["polvo", "sobre", "barra"],
        "unidad": {"rtd": "litro", "polvo": "kilo", "sobre": "porcion", "barra": "porcion"},
        "atributo": ("sabor_cafe", r"caf[eé]|capuc|cappuc|latte|moca|mocha|espresso|coffee"),
    },
    "proteina lista para beber": {
        "pertenece": r"prote|whey|shake|malteada",
        "objetivo": ["rtd"], "adyacente": ["polvo", "sobre", "barra"],
        "unidad": {"rtd": "litro", "polvo": "kilo", "sobre": "porcion", "barra": "porcion"},
    },
    "cold brew": {
        "pertenece": r"cold\s*brew",
        "objetivo": ["rtd", "concentrado"], "adyacente": ["cafe_molido", "capsulas"],
        "unidad": {"rtd": "litro", "concentrado": "litro", "cafe_molido": "kilo", "capsulas": "porcion"},
    },
    "bebida chai latte": {
        "pertenece": r"chai",
        "objetivo": ["polvo", "concentrado"], "adyacente": ["te_hojas", "capsulas", "jarabe", "rtd"],
        "unidad": {"polvo": "kilo", "concentrado": "litro", "te_hojas": "kilo", "capsulas": "porcion",
                   "jarabe": "litro", "rtd": "litro"},
    },
    "agua de coco": {
        "pertenece": r"\bcoco\b",
        # otros productos de coco: no son bebida
        "excluir": r"aceite|rallad|leche de coco|crema de coco|harina|azucar de coco|dulce de coco|laminad|deshidratad|"
                   r"\bcubos?\b|chips|jabon|shampoo|vela",
        "objetivo": ["rtd"], "adyacente": ["con_gas", "polvo", "concentrado"],
        "unidad": {"rtd": "litro", "con_gas": "litro", "polvo": "kilo", "concentrado": "litro"},
        # agua de coco pura; mezclas (aloe, colágeno, limonada, saborizada) quedan como adyacentes
        "atributo": ("agua_de_coco_pura", r"^(?!.*(aloe|colageno|limonada|saborizada|vitaminizada|love water|hint)).*(agua\s+(de\s+)?coco|coco\s+water)"),
    },
    "comida liofilizada": {
        "pertenece": r"liofiliz",
        "objetivo": ["plato"], "adyacente": ["fruta", "snack"],
        "unidad": {"plato": "porcion", "fruta": "kilo", "snack": "kilo"},
    },
    # --- Líneas asiáticas (agregadas 2026-10-21; ver entregables/2026-10-21_lineas-de-oferta-asiaticas.md) ---
    "ramen coreano": {
        "pertenece": r"ramen|ramyun|ramyeon|buldak|samyang|nongshim|ottogi|paldo|jin\s*ramen|shin\s*ramyun|fideo|noodle",
        "objetivo": ["fideo_inst"], "adyacente": ["salsa", "snack", "kit", "dulce"],
        "unidad": {"fideo_inst": "kilo", "salsa": "kilo", "snack": "kilo", "kit": "porcion", "dulce": "kilo"},
        # ramen no coreano (Maruchan, Nissin, marcas propias) queda como adyacente
        "atributo": ("coreano", r"buldak|samyang|nongshim|ottogi|paldo|jin\s*ramen|shin\s*ramyun|ramyun|ramyeon|corea|korean|neoguri|chapaguetti|jjapaguetti"),
    },
    "caldo ramen": {
        "pertenece": r"ramen|caldo|tonkotsu|shoyu|miso|broth",
        "excluir": r"cubo|cubito|consom",
        "objetivo": ["caldo", "congelado", "kit"], "adyacente": ["fideo_inst", "fideo_seco", "salsa"],
        "unidad": {"caldo": "litro", "congelado": "kilo", "kit": "porcion", "fideo_inst": "kilo",
                   "fideo_seco": "kilo", "salsa": "kilo"},
    },
    "perlas de tapioca": {
        "pertenece": r"tapioca|boba|bubble|perlas?",
        "excluir": r"harina|almid[oó]n|f[eé]cula|chipa|pan de",
        "objetivo": ["perlas", "kit"], "adyacente": ["polvo", "jarabe", "rtd", "te_hojas"],
        "unidad": {"perlas": "kilo", "kit": "porcion", "polvo": "kilo", "jarabe": "litro", "rtd": "litro", "te_hojas": "kilo"},
    },
    "gochujang": {
        "pertenece": r"gochujang|gochu|kochujang|pasta\s+de\s+aj[ií]\s+coreana|corean",
        "objetivo": ["salsa"], "adyacente": ["polvo", "fideo_inst", "kit"],
        "unidad": {"salsa": "kilo", "polvo": "kilo", "fideo_inst": "kilo", "kit": "porcion"},
    },
    "mochi": {
        "pertenece": r"mochi|daifuku",
        "objetivo": ["congelado", "dulce"], "adyacente": ["polvo", "kit"],
        "unidad": {"congelado": "porcion", "dulce": "porcion", "polvo": "kilo", "kit": "porcion"},
    },
    "kimchi": {
        "pertenece": r"kimchi",
        "objetivo": ["fermentado"], "adyacente": ["salsa", "polvo", "fideo_inst", "snack", "kit"],
        "unidad": {"fermentado": "kilo", "salsa": "kilo", "polvo": "kilo", "fideo_inst": "kilo", "snack": "kilo", "kit": "porcion"},
    },
    "pasta miso": {
        "pertenece": r"\bmiso\b",
        "objetivo": ["salsa"], "adyacente": ["polvo", "fideo_inst", "caldo", "congelado"],
        "unidad": {"salsa": "kilo", "polvo": "kilo", "fideo_inst": "kilo", "caldo": "litro", "congelado": "porcion"},
    },
    "gyozas congeladas": {
        "pertenece": r"gyoz|gyos|dumpling|wan\s*tan|wantan|mandu|jiaozi|\bbao\b|siu\s*mai|shumai|arrollado",
        "objetivo": ["congelado"], "adyacente": ["masa", "salsa", "kit"],
        "unidad": {"congelado": "kilo", "masa": "kilo", "salsa": "kilo", "kit": "porcion"},
    },
    "te hojicha": {
        "pertenece": r"hojicha|houjicha|hoji\s*cha",
        "objetivo": ["polvo", "te_hojas"], "adyacente": ["rtd", "capsulas", "concentrado"],
        "unidad": {"polvo": "kilo", "te_hojas": "kilo", "rtd": "litro", "capsulas": "porcion", "concentrado": "litro"},
    },
}
# Oportunidad del radar a la que alimenta cada término (dos términos pueden alimentar la misma)
OPORTUNIDAD = {
    "electrolitos sobres": "Sobres y tabletas de electrolitos",
    "bebida hidratante en polvo": "Sobres y tabletas de electrolitos",
    "bebida proteica cafe": "Cafe o batido proteico listo para beber 20-30 g",
    "proteina lista para beber": "Cafe o batido proteico listo para beber 20-30 g",
    "cold brew": "Cold brew local sin azucar",
    "bebida chai latte": "Chai latte en polvo o concentrado",
    "comida liofilizada": "Comida liofilizada de montana (outdoor y trekking)",
    "agua de coco": "Agua de coco",
    "ramen coreano": "Ramen coreano importado o con marca propia",
    "caldo ramen": "Caldo de ramen listo (liquido o congelado)",
    "perlas de tapioca": "Te con leche o boba listo para beber / kit",
    "gochujang": "Salsas coreanas (gochujang) con marca local",
    "mochi": "Mochi congelado",
    "kimchi": "Kimchi y fermentados asiaticos",
    "pasta miso": "Caldo de ramen listo (liquido o congelado)",
    "gyozas congeladas": "Dumplings o gyozas congeladas",
    "te hojicha": "Te japones (hojicha, matcha) para cafeterias",
}
DEFAULT_TERMINO = {"pertenece": r".", "objetivo": [], "adyacente": [], "unidad": {}}

# Accesorios y cosas que no son alimento: siempre "descartar".
NO_ALIMENTO = (r"shaker|\bvaso\b|termo\b|cafetera|\blibro\b|mochila|peluche|labial|esmalte|\bvela\b|\btaza\b|"
               r"\bjarra\b|filtro|tetera|aeropress|hario|mascota|perro|gato|artemia|\bpeces?\b|licor|j[aä]germeister|"
               r"botella\s+(?:t[eé]rmica|deportiva|de\s+agua)|hidrataci[oó]n\s+(?:mochila|bolsa)|bladder|cantimplora|"
               r"maquillaje|ColourPop|crema\b|shampoo|\bguide\b|\bgu[ií]a\b")

# Tipo de producto: primera regla que calza (el orden importa).
TIPOS = [
    ("capsulas", r"c[aá]psula|dolce\s*gusto|nespresso|k-?cup"),
    ("jarabe", r"jarabe|syrup|\bmonin\b|sirope"),
    ("gomitas", r"gomita|chews?\b|\bgel(es)?\b|gummies"),
    ("tabletas", r"tableta|\btabs?\b|efervescente|comprimido"),
    ("barra", r"\bbarra|barrita|\bbar\b"),
    ("concentrado", r"concentrad"),
    ("fruta", r"fruta|frutilla|fresa|mango|pi[ñn]a\b|frambuesa|manzana|banan|pl[aá]tano|ar[aá]ndano|kiwi|durazno|melocot|bayas|berries|"
              r"guisante|espinaca|patata|verdura|vegetal|yogur|helado|calafate|maqui"),
    ("plato", r"comida|fideo|pasta|risotto|arroz|carne|pollo|cazuela|desayuno|almuerzo|cena|guiso|chili|"
              r"lasa[ñn]a|porotos|lentejas|curry|stroganoff|outdoor|trekking|monta[ñn]a|camping|emergencia"),
    ("te_hojas", r"bolsitas|\bhojas\b|hebras|t[eé]\s+negro|blend|granel|loose"),
    ("sobre", r"sobres?\b|\bsobr\b|bolsas?\s+de\s+electrolit|sachets?|stick\s*packs?|stickpacks?|sticks?\b|\bpz\b|piezas"),
    ("cafe_molido", r"caf[eé]\s+(?:molido|en\s+grano)|grano\s+entero|molienda"),
    ("polvo", r"polvo|whey|scoop|servicios|\bisolate|aislada|\bmezcla\b|instant[aá]neo|soluble|premezcla"),
    ("con_gas", r"sparkl|con\s+gas|gasificad"),
    ("rtd", r"lista?\s+para\s+(?:beber|tomar)|\bliquid[oa]?\b|\blisto\b|\brtd\b|\blatas?\b|\bbotellas?\b|ready\s+to\s+drink|shake\b"),
]

UNIDADES_VOL = {"ml": 1, "cc": 1, "l": 1000, "lt": 1000, "lts": 1000, "litro": 1000, "litros": 1000}
UNIDADES_PESO = {"g": 1, "gr": 1, "grs": 1, "gramos": 1, "kg": 1000, "kilo": 1000, "kilos": 1000, "k": 1000,
                 "lb": 453.6, "lbs": 453.6, "lib": 453.6, "libra": 453.6, "libras": 453.6}
RE_TAM = re.compile(r"(\d+(?:\.\d+)?)\s*(fl\.?\s*oz|oz|onzas?|ml|cc|lts?|litros?|l|kg|kilos?|k|grs?|gramos|g|lbs?|lib|libras?)(?![a-z])")
PALABRA_ENVASE = r"(?:un|und|unid|unids|unidades|u|uds|latas?|botellas?|bolsas?|paquetes?|envases?|frascos?|potes?|cajas?|packs?|botellines?)"
PALABRA_PORCION = r"(?:sobres?|sobr|sachets?|stick\s*packs?|stickpacks?|sticks?|serv|porciones|porci[oó]n|servicios|servings?|tabletas?|tabs|c[aá]psulas?|bolsitas?|barritas?|barras|raciones|platos|pz|piezas|dosis)"


def norm(t):
    t = unicodedata.normalize("NFD", (t or "").lower()).encode("ascii", "ignore").decode()
    t = re.sub(r"(\d),(\d)", r"\1.\2", t)
    t = re.sub(r"(\d)\.(\d{3})(?!\d)", r"\1\2", t)  # 1.000 ml -> 1000 ml
    return t


def termino_de_archivo(nombre):
    return " ".join(Path(nombre).stem.split("_mercadolibre_cl_", 1)[-1].replace("-", " ").split())


def id_publicacion(url, termino, titulo, precio):
    m = re.search(r"MLC-?(\d{5,})", url or "", re.I)
    if m:
        return f"MLC{m.group(1)}"
    if url:
        return "URL-" + hashlib.md5(url.split("#")[0].split("?")[0].encode()).hexdigest()[:10]
    return "SIN-" + hashlib.md5(f"{termino}|{titulo}|{precio}".encode()).hexdigest()[:10]


def numero(texto):
    t = re.sub(r"[^\d]", "", str(texto or "").split(",")[0])
    return float(t) if t else None


# ---------------------------------------------------------------------------------------------------------------
# Lectura de cantidades desde el título
# ---------------------------------------------------------------------------------------------------------------
def leer_cantidades(titulo, preferir="litro"):
    """Devuelve dict: envases, contenido, unidad (ml|g|''), porciones, confianza, motivo."""
    t = norm(titulo)
    motivo = []

    # Tamaños, ignorando gramos de proteína o de porción ("con 25g de proteína", "16g proteína")
    tams = []
    for m in RE_TAM.finditer(t):
        val, uni = float(m.group(1)), m.group(2).replace(" ", "").replace(".", "")
        antes, despues = t[max(0, m.start() - 12):m.start()], t[m.end():m.end() + 14]
        es_peso = uni in UNIDADES_PESO or uni in ("oz", "onza", "onzas")
        if es_peso and val < 60 and (re.match(r"\s*(?:de\s+)?prote", despues) or re.search(r"\bcon\s*$|prote[ií]na\s*$", antes)):
            motivo.append(f"ignora {m.group(0)} (proteína)")
            continue
        if es_peso and re.match(r"\s*(?:/|por|x)\s*porci", despues):
            motivo.append(f"ignora {m.group(0)} (por porción)")
            continue
        if re.match(r"\s*(?:de\s+)?(?:az[uú]car|carbo|sodio|cafe[ií]na|col[aá]geno|fibra)", despues):
            continue
        if uni in ("floz",) or (uni in ("oz", "onza", "onzas") and preferir == "litro"):
            tams.append((val * 29.57, "ml", m))
        elif uni in ("oz", "onza", "onzas"):
            tams.append((val * 28.35, "g", m))
        elif uni in UNIDADES_VOL:
            tams.append((val * UNIDADES_VOL[uni], "ml", m))
        elif uni in UNIDADES_PESO:
            tams.append((val * UNIDADES_PESO[uni], "g", m))

    # Porciones explícitas
    porciones, span_porc = None, None
    m = re.search(r"(\d+)\s*" + PALABRA_PORCION + r"\b", t) or re.search(r"\bx\s*(\d+)\s*" + PALABRA_PORCION, t)
    if m:
        porciones, span_porc = int(m.group(1)), m.span(1)
    m2 = re.search(r"rinde\s*(\d+)", t)
    if m2 and not porciones:
        porciones, span_porc = int(m2.group(1)), m2.span(1)

    # Envases (pack)
    envases, span_env = None, None
    patrones = [
        r"(?:pack|paquete|caja|kit|set|display)\s*(?:de|x|con)?\s*(\d+)(?!\s*(?:ml|cc|l\b|lt|g\b|gr|kg|k\b|oz|lb|%))",
        r"(\d+)\s*-?\s*" + PALABRA_ENVASE + r"\b",  # "12 latas", "6pack", "24-pack"
        r"\b(\d+)\s*x\s*\d",
        r"(?:ml|cc|lt|l|g|gr|grs|kg|oz)\s*x\s*(\d+)\b",
        r"\bx\s*(\d+)\s*" + PALABRA_ENVASE + r"\b",
        r"\(\s*(\d+)\s*" + PALABRA_ENVASE,
        r"\bx\s*(\d+)\b(?!\s*[\d.])",
        r"\b(\d+)\s*x\b(?!\s*\d)",
    ]
    for p in patrones:
        m = re.search(p, t)
        if m and int(m.group(1)) > 0:
            if span_porc and m.start(1) == span_porc[0]:
                continue  # "caja de 12 sobres": el 12 son porciones, no envases
            envases, span_env = int(m.group(1)), m.span(1)
            break
    # Un número de tamaño no es un pack ("pack 5 kg")
    if envases and any(tm[2].start(1) == span_env[0] for tm in tams):
        envases = None

    # Elegir el tamaño según la unidad que se quiere medir
    contenido, unidad = None, ""
    if tams:
        dim = "ml" if preferir == "litro" else "g" if preferir == "kilo" else None
        cand = [x for x in tams if x[1] == dim] if dim else tams
        cand = cand or tams
        contenido, unidad = cand[0][0], cand[0][1]
        if len({round(x[0]) for x in cand}) > 1:
            motivo.append("varios tamaños en el título")

    conf = "alta"
    if motivo and "varios tamaños en el título" in motivo:
        conf = "media"
    if not contenido and not porciones and not (envases and preferir == "porcion"):
        conf = "baja"
        motivo.append("sin cantidad legible")
    return {"envases": envases, "contenido": round(contenido, 2) if contenido else None, "unidad": unidad,
            "porciones": porciones, "confianza_cantidad": conf, "motivo": "; ".join(motivo)}


def precio_unitario(precio, medida, envases, contenido, unidad, porciones):
    """medida: litro | kilo | porcion. Devuelve (valor, etiqueta) o (None, motivo)."""
    if not precio:
        return None, "sin precio"
    env = envases or 1
    if medida in ("litro", "kilo"):
        # Se usa la unidad que de verdad tiene el producto: un líquido en un término de polvos se mide por litro
        if contenido and unidad == "ml":
            return round(precio / (env * contenido / 1000)), "CLP/L"
        if contenido and unidad == "g":
            return round(precio / (env * contenido / 1000)), "CLP/kg"
        return None, "falta volumen (ml)" if medida == "litro" else "falta peso (g)"
    if medida == "porcion":
        if porciones:  # porciones POR ENVASE: total = porciones x envases
            return round(precio / (porciones * env)), "CLP/porción"
        # Sin porciones pero con peso o volumen: los envases son bolsas o frascos, no porciones -> CLP/kg o CLP/L
        if contenido and unidad == "g":
            return round(precio / (env * contenido / 1000)), "CLP/kg"
        if contenido and unidad == "ml":
            return round(precio / (env * contenido / 1000)), "CLP/L"
        if envases:
            return round(precio / envases), "CLP/porción"
        return None, "faltan porciones"
    return None, "sin unidad definida"


# ---------------------------------------------------------------------------------------------------------------
# Propuesta automática: clase, tipo y marca
# ---------------------------------------------------------------------------------------------------------------
def cargar_marcas():
    ruta = REF / "marcas_mercadolibre.csv"
    if not ruta.exists():
        return []
    return [(f["marca"], re.compile(f["patron"], re.I)) for f in csv.DictReader(open(ruta, encoding="utf-8-sig"))]


def cargar_marcas_corregidas():
    ruta = REF / "mercadolibre_marcas_corregidas.csv"
    if not ruta.exists():
        return {}
    return {f["detectada"]: f["canonica"] for f in csv.DictReader(open(ruta, encoding="utf-8-sig"))}


CORREGIDAS = cargar_marcas_corregidas()


def proponer_marca(titulo, marcas):
    hallazgos = [(m.search(titulo or "").start(), nombre) for nombre, m in marcas if m.search(titulo or "")]
    marca = sorted(hallazgos)[0][1] if hallazgos else ""
    return CORREGIDAS.get(marca, marca)


SOLO_LIOFILIZADA = {"fruta", "plato"}
TIPO_POR_PESO = {"cold brew": "cafe_molido", "comida liofilizada": "plato"}


# Tipos propios de las líneas asiáticas: se revisan primero y solo para esos términos (no cambian los anteriores).
TIPOS_ASIA = [
    ("kit", r"\bkit\b|\bset\b|combo"),
    ("caldo", r"caldo|broth|base\s+(?:de\s+|para\s+)?ramen|fondo\s+de"),
    ("congelado", r"congelad|frozen|refrigerad|helado"),
    ("perlas", r"perlas?\b|\bboba\b|tapioca\s+(?:pearl|negra|perla)"),
    ("masa", r"\bmasas?\b|\btapas?\b|wrappers?|obleas?"),
    ("salsa", r"salsa|\bpasta\s+de\b|\bpaste\b|aderezo|sauce|gochujang|condimento|\bmiso\b(?!.*ramen)"),
    ("fideo_inst", r"ramen|ramyun|ramyeon|buldak|instant[aá]ne|noodle|fideo|yakisoba|udon|soba"),
    ("fermentado", r"kimchi|fermentad"),
    ("dulce", r"mochi|daifuku|dulce|postre"),
    ("snack", r"snack|chips|galleta"),
]
TERMINOS_ASIA = {"ramen coreano", "caldo ramen", "perlas de tapioca", "gochujang", "mochi", "kimchi", "pasta miso",
                 "gyozas congeladas", "te hojicha"}


def proponer_tipo(titulo, termino=""):
    t = norm(titulo)
    if termino in TERMINOS_ASIA:
        for tipo, p in TIPOS_ASIA:
            if re.search(p, t, re.I):
                if tipo == "fideo_inst" and termino == "caldo ramen" and not re.search(r"instant|sopa|sabor|pote|vaso|cup", t, re.I):
                    return "fideo_seco"
                return tipo
        if termino == "gyozas congeladas":
            return "congelado"
        if termino == "mochi":
            return "dulce"
    for tipo, p in TIPOS:
        if tipo in SOLO_LIOFILIZADA and termino != "comida liofilizada":
            continue
        if re.search(p, t, re.I):
            if tipo == "rtd":  # "shake 2 lbs" o "bebida 900 g" sin ml: es polvo
                c = leer_cantidades(titulo, preferir="kilo")
                if c["unidad"] == "g" and (c["contenido"] or 0) >= 100:
                    return "polvo"
            return tipo
    # Sin palabra clave: se deduce por la unidad del título
    cant = leer_cantidades(titulo, preferir="litro")
    if cant["unidad"] == "ml":  # si el título trae un volumen, es un líquido aunque también traiga gramos
        return "rtd"
    if cant["unidad"] == "g":
        return TIPO_POR_PESO.get(termino, "polvo")
    if termino == "comida liofilizada":
        return "plato"
    if termino == "cold brew" and cant["envases"]:
        return "rtd"
    if termino in ("electrolitos sobres", "bebida hidratante en polvo") and (cant["envases"] or cant["porciones"]):
        return "sobre"
    return ""


def proponer_clase(termino, titulo, tipo):
    cfg = TERMINOS.get(termino, DEFAULT_TERMINO)
    t = norm(titulo)
    if re.search(NO_ALIMENTO, t, re.I):
        return "descartar", "alta", "no es alimento (accesorio u otro)"
    if not re.search(cfg["pertenece"], t, re.I):
        return "descartar", "media", "no calza con el término"
    if cfg.get("excluir") and re.search(cfg["excluir"], t, re.I):
        return "descartar", "alta", "otro producto de la misma materia prima"
    if "atributo" in cfg:
        nombre, patron = cfg["atributo"]
        if not re.search(patron, t, re.I):
            return ("adyacente" if tipo else "descartar"), "media", f"sin {nombre}"
    if tipo in cfg["objetivo"]:
        return "objetivo", "alta", ""
    if tipo in cfg["adyacente"]:
        return "adyacente", "alta", ""
    if not tipo:
        return "objetivo" if cfg["objetivo"] else "adyacente", "baja", "tipo no reconocido"
    return "adyacente", "media", f"tipo {tipo} no previsto para el término"


# ---------------------------------------------------------------------------------------------------------------
# Lectura de crudos, contaminación y duplicados
# ---------------------------------------------------------------------------------------------------------------
def leer_crudos(fecha):
    archivos = sorted(p for p in CRUDOS.glob(f"{fecha}_mercadolibre_cl_*.csv"))
    filas = []
    for a in archivos:
        for f in csv.DictReader(open(a, encoding="utf-8-sig")):
            if not any((v or "").strip() for v in f.values()):
                continue
            f["termino_original"] = f.get("termino", "")
            f["termino"] = termino_de_archivo(a.name)
            f["archivo"] = a.name
            f["fecha_captura"] = fecha  # la del nombre del archivo (la columna "fecha" puede venir en UTC)
            f["precio_clp_num"] = numero(f.get("precio_clp"))
            filas.append(f)
    return filas


GENERICAS = {"alimentos bebidas"}  # etiqueta residual de la función de consola, no indica otra búsqueda


def marcar_contaminacion_y_duplicados(filas):
    # Etiqueta mayoritaria por archivo
    mayoritaria = {}
    for arch in {f["archivo"] for f in filas}:
        mayoritaria[arch] = Counter(f["termino_original"] for f in filas if f["archivo"] == arch).most_common(1)[0][0]
    firma = defaultdict(set)
    for f in filas:
        firma[(f["titulo"], f["precio_clp"])].add(f["archivo"])
    def etiqueta(t):
        return " ".join(norm(t).replace("-", " ").split())

    for f in filas:
        f["estado_fila"] = "ok"
        otros = firma[(f["titulo"], f["precio_clp"])] - {f["archivo"]}
        et, term = etiqueta(f["termino_original"]), f["termino"]
        if f["termino_original"] != mayoritaria[f["archivo"]] and otros:
            f["estado_fila"] = "contaminada"
            f["nota_fila"] = f"copiada de {sorted(otros)[0]}"
        elif et and et not in GENERICAS and et not in term and term not in et:
            # la función de consola arrastró filas de otra búsqueda (la etiqueta nombra otro término)
            f["estado_fila"] = "contaminada"
            f["nota_fila"] = f"etiqueta de otra búsqueda: {f['termino_original']}"
    vistos = set()
    for f in filas:
        f["id_pub"] = id_publicacion(f.get("url"), f["termino"], f.get("titulo"), f.get("precio_clp"))
        if f["estado_fila"] != "ok":
            continue
        clave = (f["termino"], f["id_pub"])
        if clave in vistos:
            f["estado_fila"] = "duplicada"
        vistos.add(clave)
    return filas


def leer_validacion():
    if not VALIDACION.exists():
        return {}
    return {(v["termino"], v["id_pub"]): v for v in csv.DictReader(open(VALIDACION, encoding="utf-8-sig"))}


def construir(fecha):
    marcas = cargar_marcas()
    filas = marcar_contaminacion_y_duplicados(leer_crudos(fecha))
    validacion = leer_validacion()
    for f in filas:
        cfg = TERMINOS.get(f["termino"], DEFAULT_TERMINO)
        tipo = proponer_tipo(f.get("titulo"), f["termino"])
        clase, conf_clase, motivo_clase = proponer_clase(f["termino"], f.get("titulo"), tipo)
        medida = cfg["unidad"].get(tipo, "porcion" if tipo in ("sobre", "plato") else "litro" if tipo == "rtd" else "kilo")
        cant = leer_cantidades(f.get("titulo"), preferir=medida)
        if tipo == "sobre" and not cant["porciones"] and cant["envases"]:
            cant.update(porciones=cant["envases"], envases=None)  # "pack x12" de sobres: cada envase es una porción
        if tipo == "plato" and not (cant["porciones"] or cant["envases"]):
            cant.update(porciones=1, confianza_cantidad="media", motivo="se asume 1 plato por publicación")
        f.update({
            "prop_clase": clase, "prop_tipo": tipo, "prop_marca": proponer_marca(f.get("titulo"), marcas),
            "prop_envases": cant["envases"] or "", "prop_contenido": cant["contenido"] or "",
            "prop_unidad": cant["unidad"], "prop_porciones": cant["porciones"] or "",
            "confianza": min([conf_clase, cant["confianza_cantidad"] if clase == "objetivo" else "alta"],
                             key=["baja", "media", "alta"].index),
            "motivo": "; ".join(x for x in (motivo_clase, cant["motivo"]) if x),
        })
        v = validacion.get((f["termino"], f["id_pub"]))
        f["validado"] = "si" if v else "no"
        # Precio corregido a mano (el crudo no se toca): manda sobre el capturado y queda el original
        f["precio_original"], f["precio_corregido"] = f["precio_clp_num"] or "", ""
        if v and numero(v.get("precio_clp")):
            f["precio_clp_num"], f["precio_corregido"] = numero(v["precio_clp"]), "si"
        g = (lambda k, p: (v.get(k) if v and (v.get(k) or "").strip() != "" else f[p]))
        f["clase"], f["tipo"], f["marca_final"] = g("clase", "prop_clase"), g("tipo", "prop_tipo"), g("marca", "prop_marca")
        f["envases"], f["contenido"] = g("envases", "prop_envases"), g("contenido", "prop_contenido")
        f["unidad"], f["porciones"] = g("unidad", "prop_unidad"), g("porciones", "prop_porciones")
        medida = cfg["unidad"].get(f["tipo"], medida)
        # "Medir precio por" elegido a mano manda sobre la unidad del tipo
        f["medir_por"] = (v.get("medir_por") or "").strip() if v else ""
        if f["medir_por"] == "porcion":
            medida = "porcion"
        elif f["medir_por"] == "volumen_peso":
            medida = "litro"
        num = lambda x: float(x) if str(x).strip() not in ("", "None") else None
        args = (num(f["envases"]) and int(num(f["envases"])), num(f["contenido"]), f["unidad"],
                num(f["porciones"]) and float(num(f["porciones"])))
        pu, etiqueta = precio_unitario(f["precio_clp_num"], medida, *args)
        # Las dos lecturas, para comparar (columnas informativas)
        pp, ep = precio_unitario(f["precio_clp_num"], "porcion", args[0], None, "", args[3]) if args[3] else (None, "")
        pv, ev = precio_unitario(f["precio_clp_num"], "litro", *args)
        f["precio_por_porcion"] = pp if pp is not None else ""
        f["precio_por_litro_o_kilo"] = f"{pv} {ev}" if pv is not None else ""
        f["precio_unitario"] = pu if pu is not None else ""
        f["unidad_precio"] = etiqueta if pu is not None else ""
        f["sin_precio_unitario_motivo"] = "" if pu is not None else etiqueta
    return filas


# ---------------------------------------------------------------------------------------------------------------
# Comandos
# ---------------------------------------------------------------------------------------------------------------
def todas_las_fechas():
    fechas = sorted({p.name[:10] for p in CRUDOS.glob("*_mercadolibre_cl_*.csv") if "plantilla" not in p.name})
    if not fechas:
        sys.exit("No hay capturas en datos/crudos/.")
    return fechas


def fecha_por_defecto():
    return todas_las_fechas()[-1]


def escribir_csv(ruta, filas, cols):
    with open(ruta, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)


def cmd_proponer(fecha):
    """Sin fecha (o 'todas'): junta todas las capturas en una sola propuesta, que es lo que carga la mesa."""
    fechas = todas_las_fechas() if fecha == "todas" else [fecha]
    filas = [f for fe in fechas for f in construir(fe)]
    fecha = fechas[-1]
    ok = [f for f in filas if f["estado_fila"] == "ok"]
    cols = ["id_pub", "fecha_captura", "termino", "posicion", "titulo", "precio_clp_num", "envio_gratis", "vendedor", "url", "prop_clase",
            "prop_tipo", "prop_marca", "prop_envases", "prop_contenido", "prop_unidad", "prop_porciones",
            "confianza", "motivo", "precio_unitario", "unidad_precio", "validado"]
    escribir_csv(LIMPIOS / f"{fecha}_mercadolibre_cl_propuesta.csv", ok, cols)
    tipos = {t: {"objetivo": c["objetivo"], "adyacente": c["adyacente"], "unidad": c["unidad"]} for t, c in TERMINOS.items()}
    json.dump({"fecha": ", ".join(fechas), "terminos": tipos, "marcas": [m for m, _ in cargar_marcas()],
               "filas": [{k: f.get(k, "") for k in cols} for f in ok]},
              open(LIMPIOS / f"{fecha}_mercadolibre_cl_propuesta.json", "w", encoding="utf-8"), ensure_ascii=False)
    c = Counter(f["estado_fila"] for f in filas)
    print(f"{len(filas)} filas crudas: {c['ok']} únicas, {c['duplicada']} duplicadas, {c['contaminada']} contaminadas")
    print("Confianza de la propuesta:", dict(Counter(f["confianza"] for f in ok)))
    print("Clase propuesta:", dict(Counter(f["prop_clase"] for f in ok)))


def pctl(v, q):
    v = sorted(v)
    if not v:
        return ""
    k = (len(v) - 1) * q
    i = int(k)
    return round(v[i] + (v[min(i + 1, len(v) - 1)] - v[i]) * (k - i))


def cmd_resumir(fecha):
    filas = construir(fecha)
    cols = ["fecha", "termino", "posicion", "id_pub", "titulo", "precio_clp_num", "precio_original", "precio_corregido",
            "envio_gratis", "url",
            "estado_fila", "nota_fila", "clase", "tipo", "marca_final", "envases", "contenido", "unidad", "porciones",
            "precio_unitario", "unidad_precio", "sin_precio_unitario_motivo", "medir_por", "precio_por_porcion",
            "precio_por_litro_o_kilo", "validado", "confianza", "motivo",
            "vendidos_visibles", "vendedor", "tienda_oficial", "reputacion_vendedor", "archivo"]
    escribir_csv(LIMPIOS / f"{fecha}_mercadolibre_cl_captura.csv", filas, cols)

    resumen = []
    ok = [f for f in filas if f["estado_fila"] == "ok"]
    for termino in dict.fromkeys(f["termino"] for f in filas):
        todas = [f for f in filas if f["termino"] == termino]
        unicas = [f for f in ok if f["termino"] == termino]
        for clase in ("objetivo", "adyacente"):
            grupos = []
            for tipo in dict.fromkeys(f["tipo"] for f in unicas if f["clase"] == clase):
                del_tipo = [f for f in unicas if f["clase"] == clase and f["tipo"] == tipo]
                unidades = [u for u in dict.fromkeys(f["unidad_precio"] for f in del_tipo) if u] or [""]
                grupos += [(tipo, u, del_tipo) for u in unidades]
            for tipo, unidad_p, del_tipo in grupos:
                g = [f for f in del_tipo if f["unidad_precio"] == unidad_p] if unidad_p else del_tipo
                pus = [f["precio_unitario"] for f in g if f["precio_unitario"] != ""]
                marcas = Counter(f["marca_final"] for f in g if f["marca_final"])
                con_marca = sum(1 for f in g if f["marca_final"])
                tiene = lambda campo: any((f.get(campo) or "").strip() for f in g)
                resumen.append({
                    "fecha_captura": fecha, "termino": termino, "clase": clase, "tipo": tipo or "sin tipo",
                    "filas_crudas_termino": len(todas),
                    "contaminadas_termino": sum(f["estado_fila"] == "contaminada" for f in todas),
                    "duplicadas_termino": sum(f["estado_fila"] == "duplicada" for f in todas),
                    "publicaciones_tipo": len(del_tipo),
                    "publicaciones": len(g),
                    "validadas": sum(f["validado"] == "si" for f in g),
                    "con_marca": con_marca,
                    "marcas_distintas": len(marcas) if con_marca else "",
                    "share_top3_pct": round(100 * sum(n for _, n in marcas.most_common(3)) / con_marca) if con_marca else "",
                    "marcas_principales": " | ".join(f"{m} ({n})" for m, n in marcas.most_common(5)),
                    "unidad_precio": unidad_p or "sin precio por unidad",
                    "n_con_precio_unitario": len(pus),
                    "pct_tipo_sin_precio_unitario": round(100 * sum(1 for f in del_tipo if f["precio_unitario"] == "") / len(del_tipo)),
                    "precio_unitario_min": min(pus) if pus else "",
                    "precio_unitario_p25": pctl(pus, .25),
                    "precio_unitario_mediana": round(statistics.median(pus)) if pus else "",
                    "precio_unitario_p75": pctl(pus, .75),
                    "precio_unitario_max": max(pus) if pus else "",
                    "envio_gratis_pct": round(100 * sum((f.get("envio_gratis") or "").strip().lower() in ("si", "sí") for f in g) / len(g)),
                    # Campos no capturados: vacíos, no cero
                    "vendedores_distintos": len({f["vendedor"] for f in g if (f.get("vendedor") or "").strip()}) if tiene("vendedor") else "",
                    "tiendas_oficiales": sum((f.get("tienda_oficial") or "").strip().lower() in ("si", "sí") for f in g) if tiene("tienda_oficial") else "",
                    "con_vendidos_visibles": sum(1 for f in g if (f.get("vendidos_visibles") or "").strip()) if tiene("vendidos_visibles") else "",
                })
    escribir_csv(LIMPIOS / f"{fecha}_mercadolibre_cl_resumen.csv", resumen, list(resumen[0].keys()))

    # Por oportunidad del radar: une los términos que la alimentan y cuenta cada publicación una vez
    por_op = []
    for op in dict.fromkeys(OPORTUNIDAD.values()):
        vistos, g = set(), []
        for f in ok:
            if OPORTUNIDAD.get(f["termino"]) == op and f["clase"] == "objetivo" and f["id_pub"] not in vistos:
                vistos.add(f["id_pub"])
                g.append(f)
        for tipo, unidad_p in [x for x in dict.fromkeys((f["tipo"], f["unidad_precio"]) for f in g) if x[1]]:
            sub = [f for f in g if f["tipo"] == tipo and f["unidad_precio"] == unidad_p]
            pus = [f["precio_unitario"] for f in sub]
            marcas = Counter(f["marca_final"] for f in sub if f["marca_final"])
            con_marca = sum(marcas.values())
            por_op.append({
                "fecha_captura": fecha, "oportunidad": op,
                "terminos": " + ".join(t for t, o in OPORTUNIDAD.items() if o == op),
                "publicaciones_objetivo": len(g), "tipo": tipo, "unidad_precio": unidad_p, "n_con_precio_unitario": len(pus),
                "validadas": sum(f["validado"] == "si" for f in sub),
                "marcas_distintas": len(marcas) if con_marca else "",
                "share_top3_pct": round(100 * sum(n for _, n in marcas.most_common(3)) / con_marca) if con_marca else "",
                "precio_unitario_p25": pctl(pus, .25), "precio_unitario_mediana": round(statistics.median(pus)),
                "precio_unitario_p75": pctl(pus, .75), "precio_unitario_min": min(pus), "precio_unitario_max": max(pus),
                "envio_gratis_pct": round(100 * sum((f.get("envio_gratis") or "").strip().lower() in ("si", "sí") for f in sub) / len(sub)),
            })
    escribir_csv(LIMPIOS / f"{fecha}_mercadolibre_cl_resumen_oportunidad.csv", por_op, list(por_op[0].keys()))
    print(f"Guardado: captura ({len(filas)} filas) y resumen ({len(resumen)} grupos término × clase × tipo)")
    vistos = set()
    for r in resumen:
        if r["clase"] == "objetivo" and r["pct_tipo_sin_precio_unitario"] > 0 and (r["termino"], r["tipo"]) not in vistos:
            vistos.add((r["termino"], r["tipo"]))
            print(f"  {r['termino']} / {r['tipo']}: {r['pct_tipo_sin_precio_unitario']} % sin precio por unidad")


# Casos verificados a mano en la auditoría del 2026-10-16 (título, medida, precio, esperado)
CASOS = [
    ("Cold Brew Wandering Bear 946 ml Paquete De 6", "litro", 129856, 22887),
    ("High Brew Cold Brew 12 Latas De 296 Ml", "litro", 103875, 29244),
    ("Fruta Liofilizada Mix (20g X 5un)", "kilo", 18990, 189900),
    ("Fruta Liofilizada Tropical Mix 80 Gr (4 Bolsas)", "kilo", 19950, 62344),
    ("Pack 5 Kg Chai Latte Instantáneo Bolsas De 1 Kg", "kilo", 63990, 12798),
    ("Pack 6 Ostrovit Electrolitos 20 Tabs", "porcion", 24990, 208),
    ("Suero Proteico I Like 630 mL Con 12g Proteína", "litro", 2490, 3952),
    ("QNT Protein Shake 25g|330ml x12", "litro", 34990, 8836),
    ("24-pack Agua De Coco Natural B Organics 520ml Andina Grains", "litro", 62990, 5047),
    ("6-pack Agua De Coco Natural Sin Azucar 520 Ml Andina Grains", "litro", 16425, 5264),
    ("Electrolitos Amazing Care Caja De 30 Sobres", "porcion", 19990, 666),
    ("Arizona Cold Brew Concentrate 28oz", "litro", 9990, 12065),
    ("Chispa Electrolitos X30 Sobres", "porcion", 39990, 1333),
]


def cmd_probar():
    malos = 0
    for titulo, medida, precio, esperado in CASOS:
        c = leer_cantidades(titulo, preferir=medida)
        pu, et = precio_unitario(precio, medida, c["envases"], c["contenido"], c["unidad"], c["porciones"])
        ok = pu is not None and abs(pu - esperado) / esperado < 0.02
        malos += not ok
        print(f"{'OK ' if ok else 'MAL'} {titulo[:55]:55} -> {pu} {et} (esperado {esperado}) {c}")
    print(f"\n{len(CASOS) - malos}/{len(CASOS)} casos correctos")
    sys.exit(1 if malos else 0)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "resumir"
    if cmd == "probar":
        cmd_probar()
    fecha = sys.argv[2] if len(sys.argv) > 2 else ("todas" if cmd == "proponer" else fecha_por_defecto())
    {"proponer": cmd_proponer, "resumir": cmd_resumir}.get(cmd, lambda _: sys.exit(__doc__))(fecha)
