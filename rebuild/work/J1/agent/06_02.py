import json, os
W = "https://en.wikipedia.org/wiki/"
L = W + "List_of_sausages"
def X(n, d, s, a="", y="", v=None, dt=None, mk=""):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s}
    if v: x["v"] = [{"n": a_, "mk": "", "y": b_, "d": c_} for a_, b_, c_ in v]
    if dt: x["dt"] = dt
    return x
DT = "whole stick or pre-sliced · diameter · grind coarseness · ageing time"
kinds = [
 {"n": "Italian salame", "a": "salami · salumi · dry-cured salami", "d": "Fermented, air-dried Italian-style sausage of chopped pork and fat, eaten without cooking.",
  "s": "https://www.ditalia.com/collections/salumi", "t": ["whole", "pre-sliced", "salametti"],
  "x": [
   X("Salame Milano", "Fine-grained salami named after Milan.", W + "Salami", "Milano salami", dt=DT),
   X("Salame di Varzi", "Hand-tied salami of the Oltrepò Pavese in natural casing; PDO since 1996.", "https://www.visitromagnese.it/content/1b67703afc73ca67ee80094a3517b813/salame-di-varzi-dop", "Varzi", "PDO 1996", dt=DT),
   X("Salame Felino", "Salami from Felino and nearby comuni in the province of Parma; PGI.", W + "Salame_Felino", "Felino", "PGI", dt=DT),
   X("Finocchiona", "Tuscan salami of pork with fennel seed, red wine and pepper, typical of Florence.", W + "Finocchiona", "", "PGI", dt=DT),
   X("Soppressata", "Southern Italian dry salami; the Calabrian one is PDO, while the Veneto sopressa is pressed between planks.", W + "Soppressata", "sopressa", "",
     [("Soppressata di Calabria", "PDO", "Acri and Decollatura"), ("Sopressa veneta", "", "pressed between wooden planks")], DT),
   X("Salamini italiani alla cacciatora", "Small ruby-red 'hunter's' salami of lean pork, fat, pepper and garlic from Lombardy; DOP, pigs from 11 regions.", "https://www.visittuscany.com/it/sapori/salamini-italiani-alla-cacciatora/", "cacciatore · cacciatorini", "DOP"),
   X("Salame Napoli", "Coarsely minced pork salami, the ancestor of American pepperoni.", W + "Salami", "Napoli-type"),
   X("Genoa salami", "US style of dry-cured, unsmoked coarse pork salami in natural casing, the name denoting a style not a place.", W + "Genoa_salami", "Genoa salame", dt=DT),
   X("Ciauscolo", "Soft Marche salami listed among Italian varieties.", W + "Salami"),
   X("Salame cotto", "Piedmontese salami cooked or smoked for flavour.", W + "Salami"),
   X("Strolghino", "Thin Emilian salami listed among Italian varieties.", W + "Salami")
  ]},
 {"n": "Saucisson sec", "a": "saucisson · saucisse sèche", "d": "French thick dry-cured sausage of pork, or pork with other meats, sliced to eat raw.",
  "s": W + "Saucisson", "t": ["plain", "with herbs", "with nuts", "with cheese"],
  "x": [
   X("Rosette de Lyon", "Large Lyon saucisson named after its rosette casing, truncated-cone shaped, at least 550 g of noble cuts; IGP, Label Rouge since 2001.", W + "Rosette_de_Lyon", "rosette", "IGP 2004",
     [("Rosette de Lyon IGP", "2004", "INAO approved the specification")]),
   X("Jésus de Lyon", "Large Lyonnais dry sausage covered by the same IGP and Label Rouge as the rosette.", "https://www.reussir.fr/lesmarches/la-rosette-et-le-jesus-de-lyon-sous-igp", "jésus", "IGP"),
   X("Saucisson de l'Ardèche", "Fermented, dried sausage of fresh pork and hard fat in natural pork casings from south-east France; PGI 2011.", "https://www.meatsandsausages.com/sausage-recipes/fermented/saucisson-ardeche", "", "PGI 2011"),
   X("Saucisson neuchâtelois", "Swiss raw smoked pork sausage, cooked while still soft; IGP.", W + "Saucisson", "", "IGP")
  ]},
 {"n": "Fuet & salchichón", "a": "fuet · salchichón · llonganissa", "d": "Spanish and Catalan dry-cured pork sausage seasoned with black pepper rather than paprika.",
  "s": W + "Fuet", "t": ["whole", "pre-sliced", "ibérico"],
  "x": [
   X("Fuet", "Thin air-dried Catalan pork sausage in pork casing with edible white mould, famous from Vic and Olot.", W + "Fuet", "Vic fuet"),
   X("Salchichón de Vic", "Catalan sausage of lean pork and fat with salt, pepper and sugar; IGP Salchichón de Vic / Llonganissa de Vic.", "https://spanishclub.ie/charcuterie/pont-llonganissa-de-vic-igp-from-catalonia-pre-sliced-90-gr.html", "Llonganissa de Vic", "IGP",
     [("Pont Llonganissa de Vic IGP", "", "pre-sliced 90 g")]),
   X("Salchichón", "Spanish dry or smoked summer sausage, usually pork, sometimes ox, veal or horse.", W + "Salchichón")
  ]},
 {"n": "Chorizo", "a": "paprika dry-cured sausage · chouriço", "d": "Dry-cured sausage of coarsely chopped pork seasoned with garlic and pimentón, sweet or hot.",
  "s": "https://www.olympiaprovisions.com/collections/artisansalami", "t": ["dulce (sweet)", "picante (hot)", "sarta (horseshoe)", "vela (straight)", "sliced"],
  "x": [
   X("Chorizo de Cantimpalos", "Segovian chorizo, one of the two Spanish chorizos on the EU register.", W + "Chorizo", "", "PGI"),
   X("Chorizo Riojano", "La Rioja chorizo with EU PGI protection.", W + "Chorizo", "", "PGI"),
   X("Chorizo de Pamplona", "Thicker chorizo with finer-ground meat.", W + "Chorizo"),
   X("Portuguese chouriço", "Smoked, dried pork sausage with paprika, garlic and sometimes wine, in natural casing.", W + "Chorizo", "chouriço"),
   X("Goan chouriço", "Pork marinated in vinegar and red chillies, sometimes sun-dried.", W + "Chorizo")
  ]},
 {"n": "Hungarian salami", "a": "winter salami · téliszalámi", "d": "Hungarian pork salami cured in cold air, slowly smoked and ripened under a noble mould.",
  "s": W + "Winter_salami",
  "x": [
   X("Szegedi téliszalámi", "Winter salami of Szeged with white pepper and allspice; PDO 2007.", W + "Winter_salami", "Szeged winter salami", "PDO 2007"),
   X("Budapesti téliszalámi", "Budapest winter salami; PGI 2009.", W + "Winter_salami", "", "PGI 2009"),
   X("Pick salami", "Szeged winter salami of the Pick brand, with paprika or chilli.", W + "Salami", mk="Pick"),
   X("Herz salami", "Budapest winter salami of the Herz brand, advertised from the 1900s.", W + "Salami", mk="Herz")
  ]},
 {"n": "'Nduja & sobrasada", "a": "spreadable dry-cured sausage · Teewurst", "d": "Soft, spreadable cured pork sausage sold in a casing (a jar of spread is in Pantry Staples).",
  "s": "https://www.ditalia.com/collections/salumi",
  "x": [
   X("'Nduja di Spilinga", "Spicy spreadable Calabrian pork sausage of trimmings, fatback and sun-dried chilli, smoked and aged 3–6 months.", W + "'Nduja", "'nduja"),
   X("Sobrasada de Mallorca", "Uncooked cured Balearic pork sausage with paprika; IGP, including a black-pig version.", W + "Sobrasada", "sobrassada", "IGP",
     [("Sobrasada de Mallorca de cerdo negro", "", "Mallorcan black pig")]),
   X("Rügenwalder Teewurst", "Raw spreadable pork and bacon sausage smoked over beech, from Rügenwalde; protected 1927.", W + "Teewurst", "Teewurst", "1927")
  ]},
 {"n": "Pepperoni", "a": "pepperoni stick · sliced pepperoni", "d": "American spicy salami of pork, or pork and beef, with paprika and chilli, sold as a stick or sliced.",
  "s": "https://www.delallo.com/shop/delallo-short-stick-pepperoni", "t": ["stick", "sliced", "cupping", "turkey"],
  "x": [
   X("Cup-and-char pepperoni", "Natural-casing pepperoni that curls into cups and chars in a hot oven, popular around Cleveland and Buffalo.", W + "Pepperoni", "cupping pepperoni"),
   X("Flat-lying pizza pepperoni", "Commercial pepperoni with the casing removed, which lies flat on pizza.", W + "Pepperoni")
  ]},
 {"n": "Sucuk", "a": "sujuk · sudžuk · sudzhuk", "d": "Dry, spicy fermented sausage of ground beef or lamb with cumin, garlic and red pepper.",
  "s": W + "Sucuk",
  "x": [
   X("Turkish sucuk", "Beef sucuk sliced and fried with eggs.", W + "Sucuk"),
   X("Balkan sudžuk", "Bosnian, Croatian and Bulgarian forms of sujuk.", W + "Sucuk", "sudzhuk"),
   X("Armenian sujukh", "Armenian sujuk, subject of a 2025 geographical-indication application.", W + "Sucuk", "", "2025")
  ]},
 {"n": "Chinese sausage", "a": "lap cheong · lạp xưởng · xiangchang", "d": "Dried, hard, sweetened pork sausage, typically smoked and seasoned with rice wine and soy.",
  "s": W + "Chinese_sausage",
  "x": [
   X("Cantonese lap cheong", "Sweet dried pork sausage with rose wine and soy, used in claypot rice and turnip cake.", W + "Chinese_sausage", "lap cheong"),
   X("Sichuan sausage", "Chinese sausage flavoured with chilli, Sichuan pepper and Pixian bean paste.", W + "Chinese_sausage"),
   X("Duck liver sausage", "Chinese sausage made with duck liver.", W + "Chinese_sausage", "yeun cheung"),
   X("Taiwanese sausage", "Sweeter, rarely air-dried emulsified sausage made by local butchers.", W + "Chinese_sausage", "xiangchang")
  ]},
 {"n": "Kabanos & snack sticks", "a": "kabanos · cabanossi · Landjäger · meat sticks", "d": "Thin dried or semi-dried smoked sausages eaten as a snack.",
  "s": W + "Kabanos",
  "x": [
   X("Kabanos", "Slim, smoky air-dried Polish pork sausage with caraway; Kabanosy staropolskie TSG 2011.", W + "Kabanos", "cabanossi · kabana", "TSG 2011"),
   X("Landjäger", "Smoked semi-dried sausage pressed into a rectangular shape, from southern Germany, Austria, Switzerland and Alsace.", W + "Landjäger")
  ]}
]
brands = [
 {"n": "Pick", "c": "Hungary", "f": "1869", "seg": "Heritage manufactory", "kf": "winter salami", "d": "Szeged salami maker, the best-known Hungarian winter salami brand.", "s": "knowledge"},
 {"n": "Herz", "c": "Hungary", "seg": "Heritage manufactory", "kf": "winter salami", "d": "Budapest salami maker advertised from around 1900.", "s": "knowledge"},
 {"n": "Pont", "c": "Spain", "seg": "Specialist", "kf": "Llonganissa de Vic", "d": "Catalan maker of Llonganissa de Vic IGP.", "s": "https://spanishclub.ie/charcuterie/pont-llonganissa-de-vic-igp-from-catalonia-pre-sliced-90-gr.html"},
 {"n": "Rügenwalder Mühle", "c": "Germany", "seg": "Mainstream", "kf": "Teewurst", "d": "German maker originally from Rügenwalde, entitled to the Rügenwalder Teewurst name.", "s": "knowledge"}
]
notes = ("Old 11-model Salami kind split: Cacciatore, Finocchiona, Genoa salame, Salame Felino, Salame di Varzi, Soppressata became Italian salame archetypes; Saucisson sec, Salchichón became archetypes of their own kinds; "
         "Cervelat handed to Cooked & smoked sausages (06_01), Droëwors to Biltong & droëwors (cured shelf), Landjäger to Kabanos & snack sticks. Old Sobrasada model became an archetype. "
         "Teewurst (liver-free raw spreadable) placed here from the cooked shelf. Not confirmed on retrieved pages so left out: ibérico chorizo, Salame Brianza, US meat sticks/Slim Jim, Cantonese vs Hunan styles.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/06_02.json"
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1); os.replace(p + ".tmp", p)
