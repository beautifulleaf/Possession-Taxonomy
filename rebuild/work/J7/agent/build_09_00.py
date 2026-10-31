import json, os
W = 'https://en.wikipedia.org/wiki/'
ASP, WES, THA, BUL = W+'Aspall_Cyder', W+'Westons_Cider', W+'Thatchers_Cider', W+'Bulmers'
STR, SJ, MAG = W+'Strongbow_(cider)', W+'Scrumpy_Jack', W+'Magners'
HEN = 'https://happerley.co.uk/browse_intermediaries/profile/HI4849362'
KB, CID, PER, BABY = W+'Kingston_Black', W+'Cider', W+'Perry', W+'Babycham'
HUET = 'https://cidersays.com/2017/11/27/pierre-huet-aoc-pays-dauge-cidre/'
BORD = 'https://www.callmewine.com/en/eric-bordelet-B1731.htm'
AST = 'https://www.tourspain.es/en/b2b/asturian-cider-cultural-heritage/'
TRA = 'https://www.turismoasturias.es/en/descubre/gastronomia/llagares/llagar-sidra-trabanco'
SAG = W+'Sagardotegi'
KOP, REK = W+'Kopparbergs_Bryggeri', W+'Rekorderlig'
ICE, POM = W+'Ice_cider', W+'Pommeau'

def v(n, mk, y='', d=''): return {"n": n, "mk": mk, "y": y, "d": d}
def x(n, a, d, mk, y, s, vs, dt): return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": vs, "dt": dt}

english = {"n": "English cider", "a": "West Country cider · Herefordshire cider · cyder · Irish cider",
  "d": "Cider in the English (and Irish) style, from bittersweet and bittersharp apples.",
  "t": ["Dry", "Medium", "Sweet", "Draught", "Vintage", "Single-variety", "Organic", "Still", "Sparkling"],
  "s": "https://bws.com.au/product/432348/thatchers-original-english-apple-cider-330ml",
  "x": [
    x("Aspall Suffolk Cyder", "Aspall", "Suffolk cyder from the Chevallier family's Aspall Hall estate, begun with apple trees brought from Jersey; owned by Molson Coors since 2018.",
      "Aspall", "1728", ASP,
      [v("Aspall Draught Suffolk Cyder", "Aspall", "", "5.5% ABV; old data: Suffolk Draught Cyder"),
       v("Aspall Premier Cru Suffolk Cyder", "Aspall", "", "6.8% ABV"),
       v("Aspall Vintage Imperial Cyder", "Aspall", "", "8.2% ABV"),
       v("Aspall Perronelle's Blush Suffolk Cyder", "Aspall", "", "5.4% ABV"),
       v("Aspall Organic Suffolk Cyder", "Aspall", "", "6.8% ABV"),
       v("Aspall 1728", "Aspall", "", "limited-edition sparkling cider, 11% ABV")],
      "dry to medium · draught, vintage, organic · ABV 4.5–11%"),
    x("Westons Herefordshire cider", "Henry Westons · Stowford Press", "Herefordshire cider from the Much Marcle mill founded by Henry Weston.",
      "Westons", "1880", WES,
      [v("Henry Westons Vintage", "Westons", "", "medium dry, 8.2% ABV"),
       v("Henry Westons Organic Cider", "Westons", "", "old data"),
       v("Stowford Press", "Westons", "", ""),
       v("Old Rosie", "Westons", "", ""),
       v("Wyld Wood Organic", "Westons", "", "")],
      "vintage, organic, cloudy · still or sparkling · ABV"),
    x("Thatchers Somerset cider", "Thatchers", "Somerset cider from Myrtle Farm, Sandford, founded by William Thatcher.",
      "Thatchers", "1904", THA,
      [v("Thatchers Gold", "Thatchers", "", "old data"),
       v("Thatchers Original English Apple Cider", "Thatchers", "", "old data"),
       v("Thatchers Vintage Cider", "Thatchers", "2020", "vintage-dated bottling"),
       v("Thatchers Katy Sparkling Cider", "Thatchers", "", "single-variety (Katy apple); old data"),
       v("Thatchers Haze Cloudy Cider", "Thatchers", "", "cloudy; old data")],
      "single variety · cloudy or clear · vintage year · ABV"),
    x("Strongbow", "", "Mass-market dry cider made mostly at H. P. Bulmer's Hereford plant; owned by Heineken.",
      "H. P. Bulmer", "1960", STR,
      [v("Strongbow Original", "H. P. Bulmer", "", "4.5% ABV in the UK"),
       v("Strongbow Gold", "H. P. Bulmer", "", "dry; 5% in Europe"),
       v("Strongbow Dark Fruit", "H. P. Bulmer", "", "fruit-flavoured")],
      "draught, can, bottle · flavours · ABV 4.5–6%"),
    x("Scrumpy Jack", "", "Strong Herefordshire cider first made by Symonds at Stoke Lacy, now made by H. P. Bulmer (Heineken).",
      "H. P. Bulmer", "1727", SJ, [v("Scrumpy Jack", "H. P. Bulmer", "", "6% ABV, formerly 7.5%")], "draught or packaged · ABV"),
    x("Magners Irish cider", "Bulmers Irish Cider", "Irish cider from Clonmel, County Tipperary, sold as Bulmers in Ireland and as Magners elsewhere; made by C&C Group.",
      "Magners", "1935", MAG,
      [v("Magners Original", "Magners", "", ""), v("Magners Light", "Magners", "", ""), v("Magners Berry", "Magners", "", "")],
      "served over ice · original, light, flavoured"),
    x("Henney's Herefordshire cider", "", "Herefordshire cider begun by Mike Henney as a hobby, milled and pressed at Bishops Frome.",
      "Henney's", "1996", HEN,
      [v("Henney's Dry Cider", "Henney's", "", "old data"), v("Henney's Autumn Gold", "Henney's", "", "old data"),
       v("No.1 English Vintage Cider", "Henney's", "", "old data")],
      "dry to medium · vintage"),
    x("Kingston Black single-variety cider", "Black Taunton", "Cider made from the Kingston Black cider apple of Kingston St Mary, Somerset, one of few apples that make a distinctive single-variety cider.",
      "", "early 19th century", KB,
      [v("Sheppy's Kingston Black Sparkling Cider", "Sheppy's", "", "old data")], "still or sparkling · vintage year"),
  ],
  "m": [["Hawkstone Cider", "Hawkstone"], ["Hawkstone Hedgerow Cider", "Hawkstone"]]}

french = {"n": "French cider", "a": "cidre · cidre bouché", "d": "Cider in the French style, often keeved, sweet and low in alcohol.",
  "t": ["Brut", "Demi-sec", "Doux", "Cidre bouché", "Keeved", "Normandy", "Brittany"],
  "s": "https://hedonism.co.uk/product/bordelet-sidre-brut-2024",
  "x": [
    x("Cidre Pays d'Auge", "AOC Pays d'Auge cidre", "Normandy appellation cider: pure apple juice, unpasteurised, slow-fermented and naturally conditioned in the bottle.",
      "", "", HUET, [v("Pierre Huet Cidre Pays d'Auge", "Pierre Huet", "", "demi-sec, bottle conditioned, 3.5% ABV")],
      "brut, demi-sec, doux · producer · vintage"),
    x("Eric Bordelet cidre and poiré", "Sidre · Bordelet", "Grower cider and perry from the family estate revived by former sommelier Eric Bordelet.",
      "Eric Bordelet", "1992", BORD,
      [v("Bordelet Sidre Brut", "Eric Bordelet", "", "6.5% ABV"), v("Bordelet Poiré Authentique", "Eric Bordelet", "", "perry, 6% ABV")],
      "cuvée · vintage · brut or tendre"),
  ],
  "m": [["Galipette Brut Cider", "Galipette"]]}

spanish = {"n": "Spanish cider", "a": "sidra · sagardoa · sagardo", "d": "Cider in the Spanish and Basque style, tart and still or lightly sparkling.",
  "t": ["Sidra natural (still)", "Sparkling sidra", "Asturias", "Basque Country"],
  "s": "https://www.gourmets.net/salon-gourmets/2025/exhibitors-catalogue/sidra-trabanco/natural-cider-made-of-cider-apples",
  "x": [
    x("Asturian sidra natural", "sidra natural · escanciado", "Still natural cider of Asturias made from Asturian apples and poured from a height to aerate it.",
      "", "", AST,
      [v("Trabanco Tradicional Natural", "Sidra Trabanco", "", "natural cider"),
       v("Trabanco Selección", "Sidra Trabanco", "", "natural cider"),
       v("Trabanco Sobre la Madre", "Sidra Trabanco", "", "natural cider"),
       v("Poma Áurea D.O.P.", "Sidra Trabanco", "", "top of range")],
      "producer (llagar) · DOP or not · bottle"),
    x("Basque sagardoa", "sagardo · txotx cider", "Mostly still Basque cider, 4–6% ABV, matured in oak or chestnut barrels and poured from the barrel in sagardotegi.",
      "", "", SAG, [], "producer · bottle or barrel · season from 19 January"),
  ],
  "m": [["Pecado Natural", "Sidra Trabanco"]]}

fruit = {"n": "Fruit & flavoured cider", "a": "fruit cider · flavoured cider · Swedish cider", "d": "Apple cider sweetened and flavoured with other fruit or flavourings, or made extra strong.",
  "t": ["Common cider", "Strong cider", "Fruit cider"], "s": CID,
  "x": [
    x("Kopparberg fruit cider", "Kopparberg", "Swedish fruit cider from the family-owned Kopparberg brewery; in the UK since 2003.",
      "Kopparberg", "1882", KOP,
      [v("Kopparberg Mixed Fruit Cider", "Kopparberg", "", ""), v("Kopparberg Strawberry & Lime", "Kopparberg", "", ""),
       v("Kopparberg Alcohol-free Mixed Fruit", "Kopparberg", "", "alcohol-free")],
      "flavour · ABV · alcohol-free"),
    x("Rekorderlig", "", "Swedish fruit cider from Åbro Bryggeri, first made with Vimmerby spring water.",
      "Rekorderlig", "1996", REK, [v("Rekorderlig Wild Berries", "Rekorderlig", "", "")], "flavour"),
  ],
  "m": [["Ace High Imperial", "Ace Cider"], ["Secret Seven", "Cheeky Grog Co"]]}

ice = {"n": "Ice cider", "a": "cidre de glace", "d": "Strong sweet cider from apple juice concentrated by freezing, the cider counterpart of ice wine.",
  "t": ["Cryoconcentration", "Cryoextraction"], "s": ICE,
  "x": [x("Québec cidre de glace", "Quebec ice cider", "Quebec ice cider with a protected IGP (2014), 7–13% ABV, from producers' own apples with no added alcohol.",
      "", "1989", ICE,
      [v("La Face Cachée de la Pomme", "La Face Cachée de la Pomme", "", "Hemmingford; early development of the style"),
       v("La Cidrerie St-Nicholas", "La Cidrerie St-Nicholas", "1999", "first bottle sold as 'ice cider'")],
      "cryoconcentration or cryoextraction · 375 ml · producer")]}

pommeau = {"n": "Pommeau", "a": "pommeau de Normandie · pommeau de Bretagne", "d": "Apple juice blended with apple brandy and aged in oak at least 14 months, 16–18% ABV.",
  "s": POM,
  "x": [x("Pommeau de Normandie", "", "Pommeau made with Calvados in Normandy under its own appellation.", "", "", POM, [], "age · producer"),
        x("Pommeau de Bretagne", "", "Pommeau made with lambig (Breton apple brandy) under its own appellation.", "", "", POM, [], "age · producer"),
        x("Pommeau du Maine", "", "Pommeau of the Maine appellation.", "", "", POM, [], "age · producer")]}

perry = {"n": "Perry", "a": "poiré · pear cider", "d": "Fermented drink of pear juice, traditionally from small astringent perry pears.",
  "t": ["Traditional perry", "Pear cider (from concentrate)", "Single-variety", "Still", "Sparkling"],
  "s": "https://www.totalwine.com/beer/cider/perry-pear-cider/c/001293",
  "x": [
    x("Three Counties perry", "traditional perry", "Perry from Gloucestershire, Herefordshire and Worcestershire perry pears such as Hendre Huffcap, Thorn and Winnals Longdon.",
      "", "", PER, [v("Henry Westons Vintage Pear Cider", "Westons", "", "old data")], "pear variety · still or sparkling"),
    x("Domfrontais poiré", "Poiré Domfront AOC", "Normandy perry from the Domfront area with at least 40% Plant de Blanc pears; AOC 2002, PDO 2006.",
      "", "2002", PER, [], "producer · vintage"),
    x("Babycham", "champagne perry", "Light sparkling perry in miniature Champagne-style bottles, the first mass-produced branded perry, made in Shepton Mallet.",
      "Babycham", "1953", BABY, [v("Babycham", "Babycham", "", "6% ABV")], "bottle size"),
    x("Pear cider", "", "Mass-market perry branded as 'pear cider', a name popularised by Brothers Cider in 1995.",
      "", "1995", PER, [v("Kopparberg Pear Vintage", "Kopparberg", "", "old data"), v("Magners Pear", "Magners", "", "")], "flavour · ABV"),
  ],
  "m": [["Ace Perry Cider", "Ace Cider"], ["Bordelet Poire Granit", "Eric Bordelet"]]}

def b(n, c, f, seg, d, lines, sig, rel, s): return {"n": n, "c": c, "f": f, "seg": seg, "d": d, "lines": lines, "eras": [], "sig": sig, "sc": [], "rel": rel, "s": s}
brands = [
  b("Aspall", "United Kingdom", "1728", "Craft & premium cider", "Suffolk cyder maker at Aspall Hall; owned by Molson Coors since 2018.", ["Suffolk Cyder", "Pip & Wild"], ["Aspall Suffolk Cyder"], [], ASP),
  b("Westons", "United Kingdom", "1880", "Traditional cider", "Herefordshire cider mill at Much Marcle founded by Henry Weston.", ["Henry Westons", "Stowford Press", "Old Rosie"], ["Westons Herefordshire cider"], [], WES),
  b("Thatchers", "United Kingdom", "1904", "Mainstream & premium cider", "Family cider maker at Myrtle Farm, Sandford, Somerset, founded by William Thatcher.", [], ["Thatchers Somerset cider"], [], THA),
  b("H. P. Bulmer", "United Kingdom", "", "Mass-market cider", "Hereford cider maker founded by Fred and Percy Bulmer; a Heineken subsidiary.", ["Bulmers", "Strongbow", "Scrumpy Jack"], ["Strongbow", "Scrumpy Jack"], ["Magners"], BUL),
  b("Magners", "Ireland", "1935", "Mass-market cider", "Clonmel cider made by C&C Group, sold as Bulmers in Ireland.", [], ["Magners Irish cider"], ["H. P. Bulmer"], MAG),
  b("Henney's", "United Kingdom", "1996", "Craft cider", "Herefordshire cider company at Bishops Frome run by founder Mike Henney.", [], ["Henney's Herefordshire cider"], [], HEN),
  b("Eric Bordelet", "France", "1992", "Grower cider & perry", "Normandy grower cider and perry estate revived by former sommelier Eric Bordelet.", [], ["Eric Bordelet cidre and poiré"], [], BORD),
  b("Pierre Huet", "France", "", "Grower cider & Calvados", "Family cidery in the Pays d'Auge making cidre, Calvados and pommeau.", [], ["Cidre Pays d'Auge"], [], HUET),
  b("Sidra Trabanco", "Spain", "1925", "Asturian cider", "Llagar founded by Emilio Trabanco at Lavandera, Gijón, making natural and sparkling ciders.", ["Camín", "Pecado", "Poma Áurea"], ["Asturian sidra natural"], [], TRA),
  b("Kopparberg", "Sweden", "1882", "Fruit cider", "Family-owned Swedish brewery in Kopparberg, Örebro County, known for fruit ciders.", [], ["Kopparberg fruit cider"], ["Rekorderlig"], KOP),
  b("Rekorderlig", "Sweden", "1996", "Fruit cider", "Fruit cider brand of Åbro Bryggeri.", [], ["Rekorderlig"], ["Kopparberg"], REK),
  b("Babycham", "United Kingdom", "1953", "Branded perry", "Sparkling perry created by Francis Showering at Shepton Mallet; owned by Brothers Drinks since 2021.", [], ["Babycham"], [], BABY),
]
traditions = [
  {"n": "Asturian cider culture", "g": "Food & drink", "r": "Asturias, Spain", "p": "Early Middle Ages to present",
   "d": "The making, pouring and shared drinking of natural cider in Asturias, inscribed by UNESCO as intangible cultural heritage in 2024.",
   "tech": "Natural fermentation of Asturian apples in cider mills; pouring from a height to aerate", "mat": "Asturian apples",
   "forms": ["Asturian sidra natural"], "ctr": ["Sidra Trabanco, Gijón"], "auth": "100% Asturian apples; DOP Sidra de Asturias label", "s": AST},
  {"n": "Basque cider houses", "g": "Food & drink", "r": "Gipuzkoa, Basque Country", "p": "Revived from the 1980s",
   "d": "Sagardotegi cider houses where still cider is drawn straight from the barrel at the call of txotx during the season from 19 January.",
   "tech": "Double fermentation and maturing in oak or chestnut barrels", "mat": "Apples",
   "forms": ["Basque sagardoa"], "ctr": ["Astigarraga", "Hernani"], "auth": "", "s": SAG},
]
notes = ("Old models kept as versions where they fit an archetype; Hawkstone, Galipette, Ace and Secret Seven stay in m. "
         "Old 'Sidra Natural Trabanco (Pecado del Paraiso)' replaced: the maker's page lists Pecado del Paraíso as a non-alcoholic refreshing drink, so the shelf uses Trabanco's named natural ciders and Pecado Natural. "
         "Aspall Blush renamed to Perronelle's Blush per Wikipedia. No version years beyond those on retrieved pages. "
         "Sheppy's, Galipette, Hawkstone, Ace have no register entries (no retrieved page). Magners placed under English cider (alias Irish cider) as the only British-Isles cider kind. "
         "Pommeau and ice cider are new kinds; Bordelet pommeau and Henney's Frome Valley left out (snippet-only). Asturias and Pays d'Auge Wikipedia pages not found (404).")
out = {"kinds": [english, french, spanish, fruit, ice, pommeau, perry], "brands": brands, "traditions": traditions, "notes": notes}
p = 'work/J7/shelves/09_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('ok')
