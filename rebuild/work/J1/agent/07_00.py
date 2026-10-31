import json, os
W = "https://en.wikipedia.org/wiki/"
DG = "https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques-et-les-faq/le-foie-gras-acheter-un-produit-de-qualite"
def X(n, d, s, a="", y="", v=None, dt=None, mk=""):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s}
    if v: x["v"] = [{"n": a_, "mk": m_, "y": b_, "d": c_} for a_, m_, b_, c_ in v]
    if dt: x["dt"] = dt
    return x
kinds = [
 {"n": "Pâtés and terrines", "a": "pâté · terrine · meat loaf pâté", "d": "Cooked ground-meat loaves sold sliced, whole or tinned; finer pâté or coarser terrine.",
  "s": "https://fr.vikidia.org/wiki/P%C3%A2t%C3%A9", "t": ["Pâté", "Terrine", "fine", "coarse", "tinned", "sliced"],
  "x": [
   X("Pâté de campagne", "Coarse country pâté of chopped pork with liver and fat, baked to a brown crust.", "https://inao.gouv.fr/node/1549/printable/pdf", "country pâté", "",
     [("Pâté de campagne breton IGP", "", "", "Brittany, coarse grind with pieces of liver and fat, sliced, in jars or terrine")], "pork or wild boar · coarse · sliced, jar or terrine"),
   X("Pâté en croûte", "Pâté baked inside puff or shortcrust pastry and served in slices as a starter.", "https://fr.vikidia.org/wiki/P%C3%A2t%C3%A9"),
   X("Ardennes pâté", "Belgian-style coarse pork and liver pâté with smoked bacon and herbs, baked in a loaf and eaten cold.", "https://www.noordernieuws.be/en/recipes/ardennes-pate/", "pâté ardennais"),
   X("Brussels pâté", "Soft, smooth Belgian liver pâté of liver, meat, eggs, cream and spices.", "https://psinfoodservice.com/en/product/142268-brussels-pate", "", "",
     [("Brussels Pâté", "De Spiegeleire", "", "Diest, Belgium"), ("Brussels Pâté Log", "", "", "1 kg log")]),
   X("Jambon persillé", "Burgundy Easter terrine of cooked ham set in parsleyed jelly; Label Rouge, IGP under review.", "https://www.reussir.fr/lesmarches/charcuterie-un-label-rouge-pour-le-jambon-persille", "jambon persillé de Bourgogne", "Label Rouge"),
   X("Pâté Hénaff", "Pure-pork pâté in small blue tins from Pouldreuzic, Brittany, first sold in 1915.", "https://www.bible-marques.fr/henaff.html", "sailors' pâté", "1915", mk="Hénaff")
  ]},
 {"n": "Rillettes", "a": "rillons", "d": "Meat slow-cooked in its own fat for hours, shredded and packed under fat, spread on bread.",
  "s": W + "Rillettes", "t": ["pork", "duck", "goose", "rabbit", "chicken"],
  "x": [
   X("Rillettes de Tours", "Pork rillettes cooked uncovered, brown and shredded; the only rillettes with IGP (2013); first written mention 1480.", "https://www.pariszigzag.fr/insolite/rillettes-de-tours/", "", "IGP 2013"),
   X("Rillettes du Mans", "Sarthe pork rillettes cooked covered, finer and more spreadable, with larger pieces and less colour.", W + "Rillettes", "rillettes sarthoises"),
   X("Duck and goose rillettes", "Rillettes made by the same method from duck or goose.", W + "Rillettes", "rillettes de canard · rillettes d'oie")
  ]},
 {"n": "Prepared foie gras", "a": "foie gras entier · bloc de foie gras · mi-cuit", "d": "Fattened duck or goose liver seasoned and cooked, sold in jars, tins or vacuum packs under French legal names.",
  "s": DG, "t": ["duck (canard)", "goose (oie)", "mi-cuit", "cuit (tin or jar)", "cru (raw)"],
  "x": [
   X("Foie gras entier", "A whole liver or one or more lobes plus seasoning (Décret 93-999, 1993).", DG, "whole foie gras", "1993",
     [("Mi-cuit", "", "", "poached 30–40 minutes; fresh or preserved"), ("Cru", "", "", "whole raw liver to cook or cure at home")]),
   X("Foie gras", "Pieces of lobes pressed together with seasoning.", DG),
   X("Bloc de foie gras", "Reconstituted foie gras with seasoning, added water capped at 10%.", DG, "bloc", "",
     [("Bloc avec morceaux", "", "", "pieces of liver at least 30% of the weight")]),
   X("Parfait de foie gras", "Preparation of at least 75% foie gras.", DG, "parfait"),
   X("Médaillon or pâté de foie gras", "Preparation of at least 50% foie gras or bloc.", DG),
   X("Mousse de foie gras", "At least 50% foie gras mixed with a stuffing.", DG, "mousse"),
   X("Galantine de foie gras", "At least 50% foie gras or bloc mixed with a stuffing.", DG)
  ]},
 {"n": "Confit", "a": "confit de canard · confit d'oie · duck confit", "d": "Meat (duck, goose, pork) salted and cooked slowly in its own fat, kept under the fat in a tin, jar or pot.",
  "s": "https://stopandshop.com/groceries/product/dartagnan-duck-leg-confit-5-oz-pkg/218199", "t": ["legs", "gizzards", "whole bird"],
  "m": [["D'Artagnan Duck Leg Confit", "D'Artagnan"]],
  "x": [
   X("Confit de canard", "Salt-cured duck seasoned with garlic and herbs and slowly cooked in its own fat, associated with Gascony.", W + "Duck_confit", "duck confit", "",
     [("Duck Leg Confit", "D'Artagnan", "", "US retail pack")]),
   X("Confit d'oie", "Goose legs cooked and stored in goose fat, linked to Béarn and the Basque country.", W + "Confit", "goose confit"),
   X("Pork confit", "Pork prepared as confit, often shredded into rillettes.", W + "Confit", "confit de porc")
  ]},
 {"n": "Head cheese", "a": "brawn · souse · fromage de tête · Sülze", "d": "Pieces of head meat set in their own jelly, sold as a loaf or slice.",
  "s": "https://farmfetch.co.uk/products/fromage-de-tete",
  "x": [
   X("Brawn", "British head cheese, also called pork cheese in Yorkshire and Norfolk.", W + "Head_cheese", "pork cheese"),
   X("Potted heid", "Scottish head cheese of beef, pork or sheep head.", W + "Head_cheese"),
   X("Fromage de tête", "French and Belgian head cheese.", W + "Head_cheese", "tête pressée · pâté de tête"),
   X("Sülze", "German and Austrian head cheese in aspic, with many regional styles.", W + "Head_cheese", "Presskopf · Presssack · Schwartenmagen",
     v=[("Presskopf", "", "", ""), ("Presssack", "", "", ""), ("Schwartenmagen", "", "", "")]),
   X("Salceson", "Polish head cheese.", W + "Head_cheese"),
   X("Tlačenka", "Pressed head cheese in pork stomach, Czech, Slovak and Slovenian.", W + "Head_cheese"),
   X("Disznósajt", "Hungarian pork head cheese, often smoked.", W + "Head_cheese"),
   X("Coppa di testa", "Head cheese of central and northern Italy.", W + "Head_cheese", "testa in cassetta"),
   X("Souse", "Pickled head cheese of North America and the West Indies.", W + "Head_cheese", "hog's head cheese"),
   X("Queso de puerco", "Mexican head cheese with oregano and vinegar.", W + "Head_cheese", "queso de cabeza")
  ]}
]
brands = [
 {"n": "Hénaff", "c": "France", "f": "1907", "seg": "Heritage manufactory", "kf": "tinned pork pâté", "d": "Pouldreuzic cannery founded by Jean Hénaff, making its pure-pork pâté since 1915.", "s": "https://www.bible-marques.fr/henaff.html"},
 {"n": "D'Artagnan", "c": "United States", "f": "1985", "seg": "Specialist", "kf": "foie gras, duck", "d": "New Jersey supplier of foie gras, duck, game and charcuterie.", "s": "knowledge"},
 {"n": "Rougié", "c": "France", "seg": "Premium", "kf": "foie gras", "d": "French foie gras maker.", "s": "knowledge"},
 {"n": "Labeyrie", "c": "France", "seg": "Mainstream", "kf": "foie gras, smoked salmon", "d": "French foie gras and festive foods brand.", "s": "knowledge"},
 {"n": "De Spiegeleire", "c": "Belgium", "seg": "Specialist", "kf": "Belgian pâté", "d": "Diest maker of Brussels pâté.", "s": "https://psinfoodservice.com/en/product/142268-brussels-pate"}
]
notes = ("Old models Ardennes pâté, Brussels pâté, Pâté de campagne, Jambon persillé, Fromage de tête, Sülze became archetypes; D'Artagnan Duck Leg Confit kept as model and as version. "
         "Foie gras torchon not confirmed on a retrieved page, left out; Sud-Ouest IGP not attested. No traditions added.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/07_00.json"
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1); os.replace(p + ".tmp", p)
