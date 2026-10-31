import json,os
WP="https://www.whichfordpottery.com/pots-and-more/garden-essentials-range/longtom"
kinds=[
{"n":"Plant pot","a":"flowerpot · planter","d":"Container with drainage in which a plant grows.",
 "t":["terracotta","glazed","plastic","fibreclay","saucer (dish set under a pot to catch drained water)"],
 "s":"https://www.bunnings.co.nz/products/garden/plant-pots-planters-baskets?page=18",
 "x":[
  {"n":"Long tom","a":"longtom","d":"Taller, thinner terracotta pot made for deep-rooting plants such as auriculas.","mk":"","y":"Victorian era",
   "s":"https://en.wikipedia.org/wiki/Flowerpot",
   "v":[{"n":"Victorian long tom","mk":"Sankey of Bulwell","y":"Victorian","d":"hand-thrown, often stamped with the pottery name"},
        {"n":"Victorian long tom","mk":"Ward of Darlaston","y":"Victorian","d":"hand-thrown, often stamped with the pottery name"},
        {"n":"Longtom (codes 1242–1245)","mk":"Whichford Pottery","y":"","d":"handmade, 14–27 cm high, 10-year frostproof guarantee"},
        {"n":"Jim's Tom (codes 410–412)","mk":"Whichford Pottery","y":"","d":"longtom with carved lion roulette at top and bottom, 31–53 cm high"}],
   "dt":"traditional auricula size about 3 in across × 4 in deep · hand-thrown or handmade · maker's stamp"},
  {"n":"Impruneta citrus pot","a":"conca · lemon pot","d":"Large hand-built terracotta pot of iron-rich Impruneta clay, made for container-grown citrus.","mk":"","y":"late 16th century",
   "s":"https://www.uffizi.it/en/news/new_terracotta_citrus_plants_boboli_gardens",
   "v":[{"n":"Medici conca","mk":"","y":"late 16th century","d":"citrus pot of the Boboli Gardens collection begun under Cosimo I de' Medici"},
        {"n":"Truncated conical vase","mk":"","y":"Lorena and Savoy periods","d":"later Boboli citrus pot shape"},
        {"n":"Boboli replacement pots","mk":"","y":"2020","d":"made by an Impruneta pottery by colombino hand-moulding, measured from early-1700s pots"}],
   "dt":"frost-resistant, relatively light clay · hand coiling (colombino) · size by citrus tree"},
  {"n":"Cretan pithos","a":"pitharia","d":"Large person-high storage jar of Minoan origin, still associated with the potters of Thrapsano in Crete.","mk":"","y":"Bronze Age form; still made",
   "s":"https://en.wikipedia.org/wiki/Thrapsano",
   "v":[{"n":"Minoan pithos","mk":"","y":"Bronze Age","d":"storage jar for wine, oil and grain, as at Knossos"},
        {"n":"Thrapsano pitharia","mk":"","y":"","d":"made by teams of village potters, historically on the summer Ventema campaign"}],
   "dt":"height up to person-high · unglazed earthenware"}],
 "r":[["Villa","Northcote Pottery"]]},
{"n":"Raised bed","a":"","d":"Framed bed standing above ground level, filled with soil to grow plants in.",
 "t":["timber","metal","fabric","elevated (legged) planter"],
 "s":"https://www.gardenista.com/products/cedar-raised-bed-kit/",
 "m":[["VegTrug Classic","VegTrug"],["Herb Garden","VegTrug"],["VegTub 6-in-1 Modular Bed","VegTrug"],["Round Raised Bed","Smart Pot"]]},
{"n":"Self-watering planter","a":"sub-irrigated planter","d":"Planter with a built-in reservoir that feeds water to the roots.",
 "s":"https://plantaddicts.com/brands/lechuza-planters/",
 "m":[["Classico Color LS","Lechuza"],["Deltini","Lechuza"],["Vego Garden self-watering tomato planter","Vego Garden"]],
 "r":[["Classico","Lechuza"],["Cubico","Lechuza"],["Balconera","Lechuza"],["Delta","Lechuza"]]},
{"n":"Window box","a":"","d":"Long narrow planter made to sit on or hang from a window sill or railing.",
 "s":"https://www.bunnings.co.nz/products/garden/plant-pots-planters-baskets?page=18"},
{"n":"Hanging basket","a":"","d":"Basket or container hung from a bracket or chain to grow plants in.",
 "t":["wire","rustic","plastic","liner (coir, moss or fibre)"],
 "s":"https://www.mitre10.com.au/garden/plant-containers/hanging-baskets",
 "m":[["Rustic Hanging Basket","Gardman"]]},
{"n":"Cachepot","a":"overpot","d":"Decorative outer container without drainage that holds a potted plant.",
 "s":"https://www.ilnature.co.uk/garden-planters"},
{"n":"Fabric grow pot","a":"fabric grow bag","d":"Pot made of breathable fabric that air-prunes roots.",
 "s":"https://www.gertens.com/3-gal-blk-smart-pot",
 "m":[["Smart Pot Fabric Planter","Smart Pot"],["Geo-Thermal Fabric Grow Bag","Smart Pot"]]},
{"n":"Vertical garden planter","a":"living wall planter","d":"Wall-hung or stacked pocket or module system in which plants grow in a vertical surface.",
 "s":"https://www.bunnings.co.nz/products/garden/plant-pots-planters-baskets?page=18"}]
brands=[
{"n":"Whichford Pottery","c":"United Kingdom","f":"1976","seg":"Handmade terracotta","d":"Family pottery in England making handmade frostproof terracotta pots stamped with maker and year code.",
 "lines":["Garden Essentials Range","Best Loved Designs","Large Statement Planters"],"eras":[],"sig":["Long tom"],"sc":[],"rel":[],
 "s":"https://www.whichfordpottery.com/pots-and-more/best-loved-designs/jims-tom"},
{"n":"Lechuza","c":"Germany","f":"2000","seg":"Self-watering planters","d":"Plastic self-watering planter brand created by the makers of Playmobil, with a patented sub-irrigation system.",
 "lines":["Classico","Cubico","Balconera","Delta","Cube","Rondo","Quadro"],"eras":[],"sig":[],"sc":[],"rel":[],
 "s":"https://plantaddicts.com/brands/lechuza-planters/"},
{"n":"Smart Pot","c":"United States","f":"1984","seg":"Fabric pots","d":"Original fabric planter made in the USA by High Caliper Growing; sold at retail since 2006.",
 "lines":["Smart Pot Fabric Planter","Round Raised Bed","Lil' Shorty Raised Bed Planter"],"eras":["Ralph Reiger, inventor of the fabric pot"],"sig":[],"sc":[],"rel":[],
 "s":"https://smartpots.com/spot-fake-smart-pot/"},
{"n":"VegTrug","c":"United Kingdom","f":"","seg":"Raised beds","d":"Raised-bed and elevated planter brand owned by Takasho, sold in the UK and US.",
 "lines":["VegTrug Classic"],"eras":[],"sig":[],"sc":[],"rel":[],
 "s":"https://vegtrug.com/de/about-us"}]
trads=[
{"n":"Impruneta terracotta","g":"Ceramics & glass","r":"Impruneta, Tuscany, Italy","p":"14th century to present",
 "d":"Terracotta pots, basins and bricks made from the iron-rich clay of Impruneta south of Florence.",
 "tech":"Clay worked by hand (colombino coiling for large pots) and kiln-fired","mat":"Schistose, iron-rich local clay",
 "forms":["Impruneta citrus pot","large oil and wine jars","garden ornaments","bricks and roof tiles"],
 "ctr":["Impruneta","Ferrone","Tavarnuzze","Val di Greve","Boboli Gardens (Florence) citrus collection"],
 "auth":"Frost-resistant iron-rich clay; large pots hand-coiled rather than moulded",
 "s":"https://www.visittuscany.com/en/crafts/terracotta-of-impruneta/"},
{"n":"Thrapsano pottery","g":"Ceramics & glass","r":"Thrapsano, Crete, Greece","p":"Minoan roots to present",
 "d":"Village pottery tradition making large storage jars (pitharia) and other earthenware.",
 "tech":"Team throwing of large jars, historically on the migratory summer Ventema campaign","mat":"Local earthenware clay, wood-fired",
 "forms":["Cretan pithos"],"ctr":["Thrapsano"],"auth":"",
 "s":"https://en.wikipedia.org/wiki/Thrapsano"}]
notes=("Plant saucer merged into Plant pot as a type; hanging basket liner merged into Hanging basket as a type. "
 "Whichford longtoms are versions of one maker-free Long tom archetype (not a separate archetype). Northcote Pottery SKU lists (Ava, Oslo, Holland, Jardin) dropped as retail noise; its Villa range kept. "
 "Lechuza, Smart Pot and VegTrug kept as tier lines (models/ranges), not archetypes, as no dated reference pages were retrieved. "
 "Cretan pithos use as a garden jar not attested on a retrieved page, so the definition states only the jar and its makers. "
 "Not retrieved (403/404/503): theflorentine.net Impruneta article, plasticstoday Lechuza article, galaxus/digitec Lechuza brand pages; Impruneta guild date and authenticity stamping left out. No Northcote Pottery brand entry (no page retrieved).")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p="work/C2/shelves/05_00.json"; t=p+".tmp"
json.dump(out,open(t,"w"),ensure_ascii=False,indent=1); os.replace(t,p)
