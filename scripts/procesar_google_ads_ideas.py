"""Procesa una exportacion del Planificador de Google Ads (terminos + ideas) y clasifica las ideas.

Uso: python scripts/procesar_google_ads_ideas.py <terminos_12m.tsv> <ideas_24m.tsv> <terminos.csv> <prefijo>
Los .tsv son la exportacion original de Google Ads convertida a UTF-8 (separador tabulador, 2 lineas de titulo).
Salidas en datos/limpios/: <prefijo>_terminos.csv, <prefijo>_ideas_clasificadas.csv, <prefijo>_ideas_resumen.csv
Clasificacion por reglas de texto (revisar a mano lo importante): intencion = compra, marca, salud, receta,
restaurante, local_o_marca_por_confirmar, otro. extranjero_probable = nombres de locales de otros paises.
"""
import re, sys, unicodedata
import pandas as pd

f12, f24, fterm, pref = sys.argv[1:5]
a = pd.read_csv(f12, sep="\t", skiprows=2).dropna(subset=["Keyword"])
d = pd.read_csv(f24, sep="\t", skiprows=2)
t = pd.read_csv(fterm)

a = a.rename(columns={"Keyword": "termino", "Avg. monthly searches": "busquedas_mes", "Three month change": "cambio_3m",
                      "YoY change": "cambio_anual", "Competition": "competencia", "Competition (indexed value)": "competencia_idx",
                      "Top of page bid (low range)": "cpc_bajo_clp", "Top of page bid (high range)": "cpc_alto_clp"})
a = a[["termino", "busquedas_mes", "cambio_3m", "cambio_anual", "competencia", "competencia_idx", "cpc_bajo_clp", "cpc_alto_clp"]]
semillas = set(t.termino)
d = d.rename(columns={"Keyword": "idea", "Avg. monthly searches": "busquedas_mes", "Cambio interanual": "cambio_anual",
                      "Cambio en tres meses": "cambio_3m", "Competition": "competencia", "Top of page bid (high range)": "cpc_alto_clp"})
m = t[["termino", "categoria"]].merge(a, on="termino", how="left")
m.to_csv(f"datos/limpios/{pref}_terminos.csv", index=False)

I = d[~d.idea.isin(semillas)][["idea", "busquedas_mes", "cambio_3m", "cambio_anual", "competencia", "cpc_alto_clp"]].copy()

def n(s): return unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()
MARCAS = ["maruchan", "nongshim", "samyang", "buldak", "nissin", "jin ramen", "knorr", "shin ramyun", "indomie", "blue dragon", "fu sheng", "lucky me", "ottogi", "paldo"]
GENERICAS = set("de con y el la los las para sin a en coreano coreana coreanos japones japonesa chino china picante instantaneo instantaneos instantanea pollo carne cerdo cerca mi receta recetas precio sopa caldo fideos fideo arroz noodles pasta salsa tipos mejor mejores comprar hacer como que es casero vegano vegetariano shoyu miso tonkotsu kimchi queso huevo maruchan buldak samyang nissin nongshim pack caja paquete significado oriental naruto".split())
FAM = [("buldak", "ramen"), ("ramen", "ramen"), ("topokki", "tteokbokki"), ("pho", "pho"), ("udon", "udon"), ("yakisoba", "yakisoba"),
       ("soba", "soba"), ("pad thai", "pad thai"), ("miso", "miso"), ("arroz", "fideos de arroz"), ("noodle", "fideos"),
       ("fideo", "fideos"), ("tallarin", "fideos"), ("pasta", "fideos")]
viet = re.compile(r"[ơưđẠ-ỹ]|\b(thanh|anh|huong|gia dinh|hoan|nguyen|kieu|hanoi|saigon|xin chao|ta pho|kha|linh|duc|lan)\b")
fuera = re.compile(r"espana|madrid|barcelona|gran via|tibidabo|dominicano|mexico|cdmx|bogota|lima|buenos aires|peru|colombia")

def fam(s):
    s = n(s)
    return next((v for k, v in FAM if k in s), "otro")

def intent(s):
    s = n(s)
    if re.search(r"cerca|domicilio|delivery|menu|restaurant|restoran|\bbar\b|\blocal\b|carta|reserva|house", s): return "restaurante"
    if re.search(r"comprar|precio|donde|venta|\bpack\b|caja|mayor|lider|\bjumbo\b|tottus|unimarc|mercado libre|oferta|descuento|santa isabel", s): return "compra"
    if any(x in s for x in MARCAS): return "marca"
    if re.search(r"engorda|dieta|caloria|sin gluten|saludable|nutricional|keto|proteina|shirataki|light", s): return "salud"
    if re.search(r"receta|como (se )?hace|preparacion|ingrediente|thermomix|casero|con (pollo|carne|camaron|verdura|huevo|soja|salsa|brocoli|champinon)", s): return "receta"
    w = s.split()
    if len(w) == 2 and ("ramen" in w or "sushi" in w or "pho" in w) and not (set(w) - {"ramen", "sushi", "pho"}) <= GENERICAS:
        return "local_o_marca_por_confirmar"
    if len(w) == 1 and w[0].endswith("ramen") and w[0] != "ramen": return "local_o_marca_por_confirmar"
    return "otro"

I["familia"] = I.idea.map(fam)
I["intencion"] = I.idea.map(intent)
I["marca"] = I.idea.map(lambda s: next((x for x in MARCAS if x in n(s)), ""))
I["extranjero_probable"] = I.idea.map(lambda s: bool(viet.search(s.lower())) or bool(fuera.search(n(s))))
I.to_csv(f"datos/limpios/{pref}_ideas_clasificadas.csv", index=False)

J = I[~I.extranjero_probable]
res = J.groupby(["familia", "intencion"]).agg(ideas=("idea", "size"), busquedas_mes_suma=("busquedas_mes", "sum"),
                                              ideas_salto_anual=("cambio_anual", lambda x: int(x.isin(["900%", "∞"]).sum()))).reset_index()
res.to_csv(f"datos/limpios/{pref}_ideas_resumen.csv", index=False)
print(len(I), "ideas;", int(I.extranjero_probable.sum()), "extranjeras probables")
print(J.groupby("intencion").agg(ideas=("idea", "size"), busq=("busquedas_mes", "sum")).sort_values("busq", ascending=False))
print(J[J.marca != ""].groupby("marca").agg(ideas=("idea", "size"), busq=("busquedas_mes", "sum")).sort_values("busq", ascending=False))
