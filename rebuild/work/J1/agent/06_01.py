import json, os
W = "https://en.wikipedia.org/wiki/"
L = W + "List_of_sausages"
def X(n, d, s, a="", y="", v=None, dt=None):
    x = {"n": n, "a": a, "d": d, "mk": "", "y": y, "s": s}
    if v: x["v"] = [{"n": a_, "mk": "", "y": b_, "d": c_} for a_, b_, c_ in v]
    if dt: x["dt"] = dt
    return x
kinds = [
 {"n": "Frankfurter & hot dog", "a": "frankfurter · wiener · hot dog sausage · frank", "d": "Thin, finely blended parboiled sausage, usually smoked, heated or eaten cold.",
  "s": "https://www.olympiaprovisions.com/collections/sausage", "t": ["natural casing", "skinless", "all-beef", "pork and beef", "chicken or turkey", "kosher", "tinned"],
  "x": [
   X("Frankfurter Würstchen", "Slim, lightly boiled sausage in sheep casing, cold-smoked; since 1929 the name is reserved to producers around Frankfurt.", W + "Frankfurter_Würstchen", "Frankfurter", "protected 1929"),
   X("Wiener Würstchen", "Thin parboiled pork-and-beef sausage in sheep casing with a low-temperature smoke; called Frankfurter Würstl in Austria.", W + "Vienna_sausage", "wiener · Vienna sausage", "",
     [("Canned Vienna sausage", "1950s", "short, skinless, tinned North American version")]),
   X("Knackwurst", "Short, plump northern German sausage of veal, pork and garlic whose casing cracks when bitten.", W + "Knackwurst", "knockwurst", "mid-16th c."),
   X("American hot dog sausage", "Cured, smoked emulsified sausage of pork and beef, or cheaper chicken and turkey, mostly skinless; natural-casing dogs snap.", W + "Hot_dog", "frank · weenie", "",
     [("Skinless", "", "casing removed after cooking"), ("Natural casing", "", "sheep casing, firmer snap"), ("Kosher", "", "usually skinless or collagen casing"), ("All-beef", "", "regional New York and Michigan styles")]),
   X("Frankfurter Rindswurst", "All-beef Frankfurt sausage listed beside the Frankfurter Würstchen.", L)
  ]},
 {"n": "Kielbasa & smoked sausage", "a": "kiełbasa · Polish sausage · smoked sausage · kubasa", "d": "Coarse or medium-ground smoked sausage, sold in links or rings to heat or slice.",
  "s": "https://www.olympiaprovisions.com/collections/gift-collection/products/sausage-fest", "t": ["ring", "links", "pork", "beef", "turkey"],
  "x": [
   X("Krakowska", "Thick, straight, hot-smoked sausage with pepper and garlic, named after Kraków.", W + "Kielbasa", "kiełbasa krakowska", "",
     [("Kiełbasa krakowska sucha staropolska", "", "TSG, dried")]),
   X("Wiejska", "Farmhouse U-shaped pork and veal sausage with marjoram and garlic; the model for US kielbasa.", W + "Kielbasa", "kiełbasa wiejska"),
   X("Myśliwska", "Smoked, dried pork 'hunter's' sausage, like a much thicker kabanos.", W + "Kielbasa", "kiełbasa myśliwska", "",
     [("Kiełbasa myśliwska staropolska", "", "TSG")]),
   X("Kiełbasa wędzona", "Smoked Polish sausage often used in soups.", W + "Kielbasa"),
   X("Weselna", "Medium-thick U-shaped smoked 'wedding' sausage.", W + "Kielbasa"),
   X("Kiełbasa jałowcowa staropolska", "Juniper-flavoured Old Polish sausage with TSG protection.", W + "Kielbasa", "", "TSG"),
   X("Kiełbasa lisiecka", "Sausage from Małopolska with PGI protection.", W + "Kielbasa", "", "PGI"),
   X("Kiełbasa biała", "Uncooked Polish white sausage used in soups such as barszcz biały.", W + "Kielbasa", "biała", "",
     [("Kiełbasa biała parzona wielkopolska", "", "PGI, scalded Greater Poland white sausage")]),
   X("American kielbasa", "Coarse U-shaped smoked sausage of any meat, close to wiejska; also called Polish sausage.", W + "Kielbasa", "Polish sausage · kubie"),
   X("Cajun andouille", "Coarse, double-smoked Louisiana pork sausage with garlic and pepper; LaPlace calls itself its capital.", W + "Andouille", "Louisiana andouille")
  ]},
 {"n": "Weisswurst", "a": "Weißwurst · white sausage · Münchner Weißwurst", "d": "Bavarian scalded sausage of minced veal and pork fatback with parsley and lemon, eaten peeled before noon.",
  "s": W + "Weisswurst",
  "x": [X("Münchner Weißwurst", "Veal and pork back fat with parsley, lemon, mace, onion, ginger and cardamom; served warm with sweet mustard and a pretzel.", W + "Weisswurst", "Weisswurst", "1853")]},
 {"n": "Cervelat", "a": "cervelas · Servelat · Klöpfer", "d": "Switzerland's national sausage of beef, pork, bacon and rind, lightly smoked and boiled, grilled or eaten cold.",
  "s": W + "Cervelat",
  "x": [X("Swiss cervelat", "Beef, pork, bacon and rind in zebu casing, slightly smoked and boiled; about 160 million made a year.", W + "Cervelat", "Cervelat · cervelas")]},
 {"n": "Mortadella & bologna", "a": "large emulsified scalded sausage · Lyoner · baloney", "d": "Large sausage of finely blended cooked meat, often with cubes of fat, sold for slicing.",
  "s": "https://www.knuspr.de/en-DE/7684-simonini-mortadella-bologna-igp", "t": ["whole", "sliced", "with pistachio", "plain"],
  "x": [
   X("Mortadella Bologna", "Finely ground cured pork with at least 15% cubes of neck fat, peppercorns, sometimes pistachio, cooked; PGI.", W + "Mortadella", "Mortadella Bologna IGP", "PGI",
     [("Mortadella di Prato", "PGI", "Tuscan, garlic, coloured with alchermes"), ("Mortadella di Campotosto", "", "Abruzzo, 'coglioni di mulo'"), ("Mortadella di Amatrice", "", "Lazio, cinnamon and cloves")]),
   X("Bologna sausage", "Finely ground cooked US sausage adapted from mortadella, usually pork; finely ground by USDA standard.", W + "Bologna_sausage", "bologna · baloney", "",
     [("Ring bologna", "", "narrow link bent into a half-circle"), ("Rag bologna", "", "wax-coated high-fat stick, West Tennessee"), ("Lebanon bologna", "", "Pennsylvania style")]),
   X("Lyoner", "German fine scalded sausage, also a name for cervelat in Saarland.", W + "Cervelat", "Fleischwurst"),
   X("Jagdwurst", "German cooked 'hunting sausage' of fine pork farce with coarse lean pork chunks; mustard seed in the north, pistachio in the south.", W + "Jagdwurst")
  ]},
 {"n": "Liver sausage", "a": "liverwurst · Leberwurst · leverworst", "d": "Cooked sausage made mainly of liver and meat, sliced or spread from the casing.",
  "s": "https://www.dietzandwatson.com/product/Black-Forest-Braunschweiger-Liverwurst-3", "t": ["spreadable", "sliceable", "smoked", "coarse", "fine"],
  "x": [
   X("Thüringer Leberwurst", "Thuringian liver sausage with EU protected geographical status.", W + "Leberwurst", "", "PGI"),
   X("Pfälzer Leberwurst", "Liver sausage of the Rhineland-Palatinate.", W + "Leberwurst"),
   X("Braunschweiger", "In North America a smoked pork liver sausage, often with bacon; in Germany a smoked spreadable Mettwurst.", W + "Braunschweiger_(sausage)"),
   X("Dutch leverworst", "Groninger and Haagse leverworst, sliced and served with mustard.", W + "Leberwurst", "", "",
     [("Groninger leverworst", "", ""), ("Haagse leverworst", "", "The Hague")]),
   X("Lebăr", "Romanian pork liver sausage eaten over the winter holidays.", W + "Leberwurst", "lebărvurst · cârnat de ficat"),
   X("Pasztetowa", "Polish calf's-liver sausage served on rye at Christmas and Easter.", W + "Leberwurst")
  ]},
 {"n": "Black pudding", "a": "blood sausage · Blutwurst · morcilla · boudin noir", "d": "Cooked sausage made mainly of blood with fat, grain or meat, sliced or heated to eat.",
  "s": "https://farmfetch.co.uk/collections/sausages",
  "x": [
   X("Stornoway black pudding", "Western Isles black pudding of blood, suet and oatmeal with PGI status.", W + "Black_pudding", "", "PGI 2013"),
   X("Bury black pudding", "Lancashire black pudding, boiled and served with malt vinegar; local butchers claim a history to 1810.", W + "Black_pudding", "", "1810"),
   X("Sneem black pudding", "County Kerry black pudding with PGI status.", W + "Black_pudding", "", "PGI"),
   X("Drisheen", "Cork blood pudding, usually of cow's blood, with a gelatinous texture.", W + "Black_pudding"),
   X("Morcilla de Burgos", "Spanish pork blood sausage with rice and onion.", W + "Blood_sausage"),
   X("Boudin noir", "French and Walloon blood sausage, often with cream and apple or onion.", W + "Blood_sausage"),
   X("Blutwurst", "German and Austrian blood sausage of pork rind and blood with regional fillers such as barley.", W + "Blood_sausage", "", "",
     [("Thüringer Rotwurst", "PGI", "Thuringian Blutwurst")]),
   X("Kaszanka", "Polish blood sausage with buckwheat kasha.", W + "Blood_sausage", "kiszka · krupniok"),
   X("Morcela", "Portuguese smoked sausage of blood and pork fat.", W + "Blood_sausage"),
   X("Mustamakkara", "Finnish blood sausage from Tampere, roasted.", W + "Blood_sausage"),
   X("Verivorst", "Estonian Christmas blood sausage with barley and marjoram.", W + "Blood_sausage"),
   X("Sundae", "Korean blood sausage with sweet-potato noodles and barley.", W + "Blood_sausage"),
   X("Sanguinaccio", "Italian regional blood sausage family.", W + "Blood_sausage")
  ]},
 {"n": "White pudding", "a": "oatmeal pudding · mealy pudding · hog's pudding", "d": "Cooked sausage of pork, fat and oatmeal or other grain, without blood, sliced or heated to eat.",
  "s": "https://www.ocado.com/products/clonakilty-irish-white-pudding/82011011",
  "x": [
   X("Irish white pudding", "Pork, pork liver and fat with oatmeal; part of the Irish breakfast.", W + "White_pudding", "putóg bhán"),
   X("Scottish mealie pudding", "Oatmeal, onion and beef suet pudding, often deep-fried in chip shops.", W + "White_pudding", "mealy pudding · marag gheal"),
   X("Hog's pudding", "More highly spiced white pudding of Cornwall and Devon.", W + "White_pudding", "groats pudding"),
   X("Boudin blanc", "French white sausage, listed in its Rethel form.", L, "", "", [("Boudin blanc de Rethel", "", "")])
  ]},
 {"n": "Andouillette & andouille", "a": "andouillette · andouille", "d": "French coarse sausage of pork intestines with pepper, wine and onion, grilled or fried.",
  "s": W + "Andouillette",
  "x": [
   X("Andouillette de Troyes", "Pork-only andouillette, the most common in supermarkets.", W + "Andouillette", "", ""),
   X("Andouillette lyonnaise", "Lyon-style andouillette.", W + "Andouillette"),
   X("Andouillette de Cambrai", "Cambrésis andouillette.", W + "Andouillette"),
   X("Andouillette de Chablis", "Burgundy andouillette.", W + "Andouillette"),
   X("Andouille de Vire", "Norman andouille of chitterlings and tripe, grey and strong; PGI since 2019.", W + "Andouille", "", "2019"),
   X("Andouille de Guémené", "Breton regional andouille.", W + "Andouille")
  ]}
]
for k in kinds:
    if k["n"] == "Andouillette & andouille":
        k["dt"] = None
kinds[-1].pop("dt", None)
kinds[-1]["x"][0]["v"] = [{"n": "AAAAA diplôme", "mk": "", "y": "1970", "d": "award of the Association Amicale des Amateurs d'Andouillette Authentique"}]
brands = [
 {"n": "Hormel Foods", "c": "United States", "seg": "Mainstream", "kf": "SPAM, franks", "d": "US meat company shown smoking hot dogs in 1964.", "s": W + "Hot_dog"},
 {"n": "Oscar Mayer", "c": "United States", "seg": "Mainstream", "kf": "wieners, bologna", "d": "US hot dog and cold-cut brand, part of Kraft Heinz.", "s": "knowledge"},
 {"n": "Nathan's Famous", "c": "United States", "f": "1916", "seg": "Mainstream", "kf": "all-beef hot dogs", "d": "Coney Island hot dog stand turned packaged frank brand.", "s": "knowledge"},
 {"n": "Clonakilty", "c": "Ireland", "seg": "Specialist", "kf": "black and white pudding", "d": "Irish maker of black and white pudding from Clonakilty, County Cork.", "s": "knowledge"},
 {"n": "Dietz & Watson", "c": "United States", "seg": "Mainstream", "kf": "deli meats", "d": "Philadelphia deli-meat maker whose range includes braunschweiger liverwurst.", "s": "knowledge"}
]
notes = ("Old models Knackwurst, Bologna, Jagdwurst, Mortadella Bologna, Braunschweiger, Pfälzer Leberwurst became archetypes. Kabanos left to the dry-sausage shelf. "
         "Teewurst is liver-free raw spreadable sausage, so it was not placed under Liver sausage (handed to 'Nduja & spreadable sausages in 06_02). "
         "Clonakilty and Dietz & Watson recorded from knowledge; Simonini (Mortadella Bologna maker in old source) left out of the register. Münchner Weißwurst protection status not confirmed, left out.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/06_01.json"
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1); os.replace(p + ".tmp", p)
