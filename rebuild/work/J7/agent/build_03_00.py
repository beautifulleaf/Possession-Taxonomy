import json, os
WP = "https://en.wikipedia.org/wiki/"
SAUT = WP + "Sauternes_(wine)"; TOK = WP + "Tokaji"; ICE = WP + "Ice_wine"; STRAW = WP + "Straw_wine"
YQ = WP + "Ch%C3%A2teau_d%27Yquem"; RIE = WP + "Ch%C3%A2teau_Rieussec"; CLI = WP + "Ch%C3%A2teau_Climens"
PRAD = WP + "Pr%C3%A4dikatswein"; TBA = WP + "Trockenbeerenauslese"; VT = WP + "Vendange_tardive"
VS = WP + "Vin_Santo"; AMA = WP + "Amarone"; REC = WP + "Recioto"; COM = WP + "Commandaria"
VDP = WP + "Vin_de_paille"; KC = WP + "Klein_Constantia"; INN = WP + "Inniskillin"; KR = WP + "Kracher"
RT = "https://wilsondaniels.com/winery/royal-tokaji/story/"

def X(n, d, s, mk="", y="", a="", v=(), dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s,
            "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}

kinds = [
 {"n": "Sauternes & Barsac", "a": "Sauternes · Barsac · Bordeaux sweet white",
  "d": "Sweet white Bordeaux from botrytised Sémillon, Sauvignon blanc and Muscadelle grown around the Ciron and Garonne.",
  "t": ["Sauternes", "Barsac", "Premier Cru Supérieur", "Premier Cru", "Deuxième Cru", "Unclassified", "Second wine", "Half bottle"],
  "s": "https://www.totalwine.com/wine/dessert-fortified-wine/bordeaux-blend/chateau-rieussec-sauternes/p/59615375",
  "x": [
   X("Château d'Yquem", "The only Premier Cru Supérieur of the 1855 classification; about 80% Sémillon, 20% Sauvignon blanc.", YQ,
     mk="Château d'Yquem", y="1855",
     v=[("Château d'Yquem (grand vin)", "Château d'Yquem", "", "not released under the château name in poor years, e.g. 1992 and 2012"),
        ("Ygrec", "Château d'Yquem", "1959", "dry white, mainly Sauvignon blanc; made every year since 2004")],
     dt="vintage · bottle size"),
   X("Sauternes classed growth", "Sauternes estate ranked Premier or Deuxième Cru in 1855 (11 and 15 estates today).", SAUT, y="1855",
     a="Sauternes grand cru classé",
     v=[("Château Rieussec", "Château Rieussec", "1855", "Fargues, Premier Cru; Domaines Barons de Rothschild (Lafite) since 1984; second wine Carmes de Rieussec"),
        ("Château La Tour Blanche", "", "1855", "Premier Cru")],
     dt="rank Premier / Deuxième Cru · commune (Sauternes, Bommes, Fargues, Preignac) · grand vin / second wine · vintage"),
   X("Barsac classed growth", "Classed growth from Barsac, which may sell as Barsac or Sauternes; usually lighter and drier in style.", SAUT, y="1855",
     a="Barsac grand cru classé",
     v=[("Château Climens", "Château Climens", "1855", "Premier Cru; all Sémillon; second wine Cypres de Climens"),
        ("Asphodèle du Climens", "Château Climens", "2018", "dry Sémillon")],
     dt="rank · label Barsac or Sauternes · vintage"),
  ],
  "m": [["Chateau Bastor-Lamontagne Sauternes", "Chateau Bastor-Lamontagne"],
        ["Château Haut-Bergeron Sauternes", "Château Haut-Bergeron"]]},

 {"n": "Tokaji", "a": "Tokaj · Tokay · Tokaji aszú",
  "d": "Sweet wines of the Tokaj region of Hungary and Slovakia, chiefly from botrytised Furmint and Hárslevelű.",
  "t": ["Furmint", "Hárslevelű", "Yellow Muscat (Sárgamuskotály)", "Zéta", "Kövérszőlő", "Kabar", "Single vineyard (dűlő)", "50 cl bottle"],
  "s": "https://www.astorwines.com/item/13172",
  "x": [
   X("Tokaji Aszú", "Botrytised aszú berries steeped as a paste in must or wine and cask-aged; graded 3–6 puttonyos.", TOK,
     y="by 1630 (legend); mentioned 1576", a="Tokay · Aszú",
     v=[("Royal Tokaji Aszú 5 Puttonyos", "Royal Tokaji", "", ""),
        ("Royal Tokaji Aszú 6 Puttonyos", "Royal Tokaji", "", ""),
        ("Royal Tokaji Betsek First Growth 6 Puttonyos", "Royal Tokaji", "", "single first-growth vineyard"),
        ("Oremus Aszú 6 Puttonyos", "Oremus", "", ""),
        ("Balassa Villő Aszú 6 Puttonyos", "Balassa", "", ""),
        ("Juliet Victor Aszú 6 Puttonyos", "Juliet Victor", "", ""),
        ("Antalóczy Dániel Aszú 5 Puttonyos", "Antalóczy", "", ""),
        ("Béres Aszú 5 Puttonyos", "Béres", "", "")],
     dt="3–6 puttonyos · vineyard class (first growth…) · vintage · 50 cl"),
   X("Tokaji Eszencia", "Free-run juice of aszú berries, 500–700 g/l sugar and about 5–6% alcohol.", TOK,
     a="Essencia · Aszú-Eszencia (historic, above 6 puttonyos)", dt="vintage · small bottle"),
   X("Szamorodni", "Wine from whole bunches with many botrytised grapes, about 14% alcohol, sweet or dry.", TOK,
     v=[("Balassa Bor Szamorodni", "Balassa Bor", "", "")], dt="édes (sweet) · száraz (dry, flor-aged)"),
   X("Fordítás & Máslás", "Must poured over used aszú paste (fordítás) or aszú lees (máslás).", TOK, dt="vintage"),
   X("Tokaji late harvest", "Reductively made late-harvest sweet wine (késői szüretelésű), outside the classic aszú categories.", TOK,
     a="Késői szüretelésű",
     v=[("Royal Tokaji Late Harvest", "Royal Tokaji", "", "")], dt="grape · vintage"),
  ]},

 {"n": "Late-harvest wine", "a": "Vendange tardive · Spätlese · Auslese · Beerenauslese · Trockenbeerenauslese · SGN",
  "d": "Sweet wine from grapes left on the vine past normal ripeness, often concentrated by noble rot.",
  "t": ["Riesling", "Gewürztraminer", "Pinot gris", "Muscat", "Welschriesling", "Botrytised", "Half bottle"],
  "s": "https://www.directwines.com.hk/products/royal-tokaji-late-harvest-50cl-2021",
  "x": [
   X("Trockenbeerenauslese & Beerenauslese", "German and Austrian Prädikat wines from hand-selected botrytised berries; TBA needs about 150 °Oe or 30 °KMW.", TBA,
     a="TBA · BA",
     v=[("Kracher Nummer 2 Trockenbeerenauslese Welschriesling Zwischen den Seen", "Kracher", "", ""),
        ("Angerhof Tschida Trockenbeerenauslese Ried Domkapitel Sämling 88 Neusiedlersee", "Angerhof Tschida", "", "")],
     dt="Prädikat BA / TBA · grape · region (Mosel, Rheingau, Neusiedlersee) · vintage"),
   X("Spätlese & Auslese", "Lower German Prädikat levels: late-picked (Spätlese, 76–90 °Oe) and selected bunches (Auslese, 83–100 °Oe).", PRAD,
     v=[("Puklavec Family Wines Jeruzalem Ormož Spätlese Edition 2 Welschriesling", "Puklavec Family Wines", "", "Slovenian late harvest")],
     dt="Prädikat level · grape · region · vintage"),
   X("Alsace Vendanges Tardives & Sélection de Grains Nobles", "Alsace late-harvest (VT) and noble-rot (SGN) wines from Gewurztraminer, Pinot gris, Riesling or Muscat; rules drafted by Jean Hugel.", VT,
     y="1984", a="VT · SGN", dt="VT / SGN · grape · vintage"),
   X("Vin de Constance", "Cape dessert wine from vine-dried Muscat, famed in the 18th–19th centuries and revived at Klein Constantia.", KC,
     mk="Klein Constantia", y="1986 (modern revival)", dt="vintage"),
  ],
  "m": [["Kracher Nouvelle Vague Nummer 1 Zweigelt", "Kracher"],
        ["Iločki Podrumi Izborna Berba Prosušenih Bobica Traminac", "Iločki Podrumi"],
        ["Vincent Denis Terres de Soleil Liquoreux", "Vincent Denis"]]},

 {"n": "Ice wine", "a": "Eiswein · Icewine",
  "d": "Sweet wine pressed from grapes frozen on the vine (Eiswein, Icewine).",
  "t": ["Vidal", "Riesling", "Cabernet Franc", "Sparkling", "Red", "Half bottle"],
  "s": "https://www.amathusdrinks.com/gruber-roschitz-riesling-eiswein-37-5cl",
  "x": [
   X("Canadian Icewine", "VQA icewine from Ontario or British Columbia, picked at −8 °C or below at 35° Brix or more.", ICE,
     y="1972 (first); 1984 (first commercial, Inniskillin)",
     v=[("Inniskillin Vidal Icewine 1989", "Inniskillin", "1989", "won the Grand Prix d'Honneur at Vinexpo 1991"),
        ("Peller Estates Icewine Vidal", "Peller Estates", "", ""),
        ("Pillitteri Estates Winery Commendatore Reserve Sparkling Icewine Vidal", "Pillitteri Estates Winery", "", "sparkling")],
     dt="grape (Vidal, Riesling, Cabernet Franc) · still / sparkling · province · vintage · 20–37.5 cl"),
   X("German & Austrian Eiswein", "Prädikat ice wine from naturally frozen grapes picked at −7 °C or colder; first documented 1830 at Dromersheim.", ICE,
     y="1830",
     v=[("Gruber Röschitz Riesling Eiswein", "Gruber Röschitz", "", "Austria")],
     dt="grape · region · vintage"),
   X("Cryoextraction dessert wine", "Wine in ice-wine style from mechanically frozen grapes, where natural freezing is not required.", ICE,
     a="Vin de glacière",
     v=[("Bonny Doon Vin de Glacière", "Bonny Doon Vineyard", "", "US")], dt="grape · producer"),
  ]},

 {"n": "Passito & dried-grape wine", "a": "dried-grape wine · straw wine · raisin wine · vin santo · appassimento",
  "d": "Wine made from grapes dried after picking (passito, vin santo, straw wine), usually sweet.",
  "t": ["White", "Red", "Rosé (Occhio di Pernice)", "Sweet", "Dry"],
  "s": "https://www.vino.com/en/vino/passito",
  "x": [
   X("Vin Santo", "Tuscan dessert wine from Trebbiano and Malvasia dried on mats or racks, aged years in small barrels.", VS,
     a="Vin Santo del Chianti · Vin Santo di Montepulciano · Occhio di Pernice",
     v=[("Vin Santo del Chianti", "", "", "DOC; sub-zones incl. Rufina, Montespertoli"),
        ("Vin Santo di Montepulciano Occhio di Pernice", "", "", "rosé from Sangiovese, aged at least 8 years"),
        ("Capezzana Riserva Carmignano Vin Santo", "Capezzana", "", ""),
        ("Fattoria La Vialla Vin Santo del Chianti Riserva", "Fattoria La Vialla", "", "")],
     dt="DOC · white / Occhio di Pernice · years in caratelli · 37.5–50 cl"),
   X("Amarone della Valpolicella", "Dry red from Corvina and Rondinella dried about 120 days (appassimento); DOCG since 2009.", AMA,
     y="DOC 1990; DOCG 2009", a="Amarone",
     v=[("Vigneti Villabella Fracastoro Amarone della Valpolicella Classico Riserva", "Vigneti Villabella", "", "Classico Riserva"),
        ("Cantina Valpantena Tesco Finest Amarone della Valpolicella", "Cantina Valpantena", "", "retailer own label")],
     dt="Classico / Valpantena · Riserva · vintage"),
   X("Recioto della Valpolicella", "Sweet red Valpolicella from dried Corvina, Rondinella and Molinara, fermentation stopped early.", REC,
     dt="vintage · half bottle"),
   X("Recioto di Soave", "Sweet passito white from dried Garganega around Verona.", REC, dt="vintage · half bottle"),
   X("Passito di Pantelleria", "Sweet passito from Zibibbo (ancient Muscat) on Pantelleria in the Strait of Sicily.", STRAW,
     a="Moscato Passito di Pantelleria", dt="producer · vintage"),
   X("Santorini Vinsanto", "Sweet sun-dried wine of Santorini from Assyrtiko with Aidani and Athiri.", STRAW,
     v=[("Estate Argyros Vinsanto Late Release", "Estate Argyros", "", "")], dt="years in cask · vintage"),
   X("Commandaria", "Cypriot dessert wine from sun-dried Xynisteri and Mavro, from 14 villages in the Troödos foothills.", COM,
     y="name from the 12th century", dt="producer (KEO, LOEL, SODAP…) · age"),
   X("Vin de paille", "French straw wine; in the Jura from Chardonnay, Savagnin and Poulsard dried on mats up to three months.", VDP,
     a="Straw wine · Vin paillé", dt="Jura / Hermitage · vintage"),
   X("Strohwein & Schilfwein", "Austrian Prädikat wine from grapes dried on straw or reeds for at least three months.", STRAW,
     v=[("Angerhof Tschida Schilfwein Muskat Ottonel", "Angerhof Tschida", "", "")], dt="grape · vintage"),
   X("Sciacchetrà", "Passito white from the Cinque Terre in Liguria.", STRAW, dt="vintage"),
   X("Picolit", "Friulian passito of high repute, made near Ramandolo.", STRAW, dt="producer · vintage"),
   X("Torcolato", "Passito white from Breganze in the Veneto.", STRAW, dt="vintage"),
   X("Passito di Caluso", "Piedmont passito from Erbaluce dried six months and oak-aged at least four years.", STRAW, dt="vintage"),
   X("Prošek", "Dalmatian dessert wine made by the passito method.", STRAW, dt="producer · vintage"),
  ]},
]

brands = [
 {"n": "Château d'Yquem", "c": "France", "f": "", "seg": "Sauternes Premier Cru Supérieur",
  "d": "Sauternes estate, sole Premier Cru Supérieur of 1855; owned by LVMH.",
  "lines": ["Château d'Yquem", "Ygrec"], "eras": [], "sig": ["Château d'Yquem"], "sc": [], "rel": [], "s": YQ},
 {"n": "Château Rieussec", "c": "France", "f": "", "seg": "Sauternes Premier Cru",
  "d": "Sauternes first growth in Fargues, owned by Domaines Barons de Rothschild (Lafite) since 1984.",
  "lines": ["Château Rieussec", "Carmes de Rieussec"], "eras": [], "sig": ["Sauternes classed growth"], "sc": [], "rel": [], "s": RIE},
 {"n": "Château Climens", "c": "France", "f": "", "seg": "Barsac Premier Cru",
  "d": "Barsac first growth planted entirely to Sémillon, run by Bérénice Lurton since 1992.",
  "lines": ["Château Climens", "Cypres de Climens", "Asphodèle du Climens"], "eras": ["Lurton family, from 1971"],
  "sig": ["Barsac classed growth"], "sc": [], "rel": [], "s": CLI},
 {"n": "Royal Tokaji", "c": "Hungary", "f": "1990", "seg": "Tokaji producer",
  "d": "Tokaj winery founded after communism by Hugh Johnson and investors, known for first-growth single-vineyard aszú.",
  "lines": ["Aszú", "Late Harvest"], "eras": [], "sig": ["Tokaji Aszú"], "sc": [], "rel": [], "s": RT},
 {"n": "Inniskillin", "c": "Canada", "f": "1975", "seg": "Icewine producer",
  "d": "Niagara-on-the-Lake winery of Donald Ziraldo and Karl Kaiser; first commercial Canadian icewine in 1984.",
  "lines": ["Vidal Icewine"], "eras": [], "sig": ["Canadian Icewine"], "sc": [], "rel": [], "s": INN},
 {"n": "Kracher", "c": "Austria", "f": "", "seg": "Sweet wine producer",
  "d": "Burgenland family winery (Weinlaubenhof Kracher) made famous for Trockenbeerenauslese by Alois Kracher Jr.",
  "lines": ["Nummer TBA series", "Nouvelle Vague", "Zwischen den Seen"], "eras": ["Alois Kracher Jr., 1986–2007"],
  "sig": ["Trockenbeerenauslese & Beerenauslese"], "sc": [], "rel": [], "s": KR},
 {"n": "Klein Constantia", "c": "South Africa", "f": "", "seg": "Cape wine estate",
  "d": "Constantia estate that revived Vin de Constance from Muscat in 1986.",
  "lines": ["Vin de Constance"], "eras": [], "sig": ["Vin de Constance"], "sc": [], "rel": [], "s": KC},
]

traditions = [
 {"n": "Tokaji aszú winemaking", "g": "Food & drink", "r": "Tokaj, Hungary and Slovakia", "p": "16th–17th century to present",
  "d": "Botrytised aszú berries macerated in must and cask-aged; vineyards classified from 1730 in one of the first appellations.",
  "tech": "Hand-picking aszú berries, paste maceration, cask ageing; puttonyos grading",
  "mat": "Furmint, Hárslevelű, Yellow Muscat", "forms": ["Tokaji Aszú", "Tokaji Eszencia", "Szamorodni", "Fordítás & Máslás"],
  "ctr": ["Mád", "Tokaj"], "auth": "Tokaji designation; puttonyos and vintage on label", "s": TOK},
 {"n": "Commandaria", "g": "Food & drink", "r": "Limassol District, Cyprus", "p": "Named in the 12th century; earlier roots",
  "d": "Sun-dried-grape dessert wine from 14 villages in the Troödos foothills, protected by Cypriot law of 1990 and EU PDO.",
  "tech": "Sun-drying grapes 7–10 days before pressing", "mat": "Xynisteri, Mavro", "forms": ["Commandaria"],
  "ctr": ["KEO", "LOEL", "SODAP"], "auth": "Commandaria PDO", "s": COM},
]

notes = ("All five planned kinds kept. Amarone moved into Passito & dried-grape wine as a dry passito archetype (with its two old models). "
         "Old Late-harvest model 'Royal Tokaji Late Harvest' sits under Tokaji. 'The Royal Tokaji Wine Company' normalised to 'Royal Tokaji'. "
         "Chateau Rieussec Sauternes became a version of the Sauternes classed growth archetype. Not added (no retrieved page in this session): "
         "full 1855 Sauternes list beyond Yquem/Rieussec/Climens/La Tour Blanche, German BA/TBA icon estates (e.g. Mosel names), Ausbruch (Rust), "
         "Royal Tokaji vineyard wines other than Betsek, Commandaria producer bottlings, Hungarian puttonyos thresholds. Pedro Ximénez left to the Sherry kind "
         "(fortified shelf). Wikidata was rate-limited (HTTP 429); Moscato di Pantelleria, Constantia wine and Royal Tokaji Wikipedia pages 404.")

out = {"kinds": kinds, "brands": brands, "traditions": traditions, "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/03_00.json"
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1); os.replace(p + ".tmp", p)
print("written")
