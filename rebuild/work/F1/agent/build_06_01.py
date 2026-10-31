import json, os
W = 'https://en.wikipedia.org/wiki/'
K = 'knowledge'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
TOT = W + 'Theatrum_Orbis_Terrarum'; AM = W + 'Atlas_Maior'; HON = W + 'Jodocus_Hondius'; PTO = 'https://www.oldworldauctions.com/info/article/2024-01-The-Maps-and-Editions-of-Ptolemy'
SPD = 'https://www.cam.ac.uk/research/news/mapping-the-origins-of-a-masterpiece'; HOM = W + 'Johann_Homann'; CAS = W + 'Cassini_map'; CARY = W + 'John_Cary'
WAG = W + 'Lucas_Janszoon_Waghenaer'; VK = W + 'Johannes_van_Keulen'; ADM = W + 'Admiralty_chart'; HM = W + 'Harmonia_Macrocosmica'
DOP = 'https://crouchrarebooks.com/browse/an-encyclopedic-atlas-of-everything-astronomical/'; BRIT = W + 'Britannia_(atlas)'
HF = 'https://www.thehenryford.org/collections/explore/artifact/368818'; RYU = W + 'Ry%C5%ABsen-zu'; SEK = 'https://ica-abs.copernicus.org/articles/1/155/2019/'
GILL = 'https://www.themaphouse.com/exhibitions/57/works/255851-macdonald-gill-the-wonderground-map-of-london-1924-c./'; OSH = 'https://oshermaps.org/?p=486'
kinds = [
 {"n": "Antique map", "a": "old map · engraved map", "d": "Engraved or woodcut map sheet made before about 1850, often taken from a broken atlas; state and colouring are noted.",
  "t": ["woodcut", "copper engraving", "lithograph", "original hand colour", "later colour", "uncoloured", "first state", "later state", "Latin text verso", "vernacular text verso", "blank verso", "framed", "laid down on linen"],
  "s": OSH,
  "x": [
   X("Ptolemaic map", "Map from a printed edition of Ptolemy's Geographia, following his classical coordinates, sometimes with added 'modern' maps.", "", "1477", PTO,
     [("Copper-engraved", "", "1477", "Bologna and Rome editions"), ("Woodcut", "", "1482", "Ulm to Münster editions, last woodcuts 1552"), ("Gastaldi copper", "", "1548", "small Venice maps"),
      ("Ruscelli", "", "1561", "platemark reaches top edge")], dt="edition · classical or modern · colour"),
   X("Dutch golden-age atlas map", "Decorative copper-engraved map from the Antwerp and Amsterdam atlases of Ortelius, Mercator, Hondius, Blaeu and Janssonius.", "", "1570", OSH,
     [("Ortelius", "Abraham Ortelius", "1570", "uniform size"), ("Mercator–Hondius", "Hondius", "1606", ""), ("Blaeu", "Blaeu", "1635", ""), ("Janssonius", "Janssonius", "1633", "")],
     dt="atlas edition · text language on verso · colour"),
   X("Speed county map", "John Speed's county maps of Britain, each with an inset town plan, the model for folio county atlases.", "John Speed", "1611", SPD,
     [("First edition", "John Speed", "1611", "about 500 copies"), ("1627 edition", "John Speed", "1627", "")], dt="edition · colour · verso text"),
   X("Homann map", "Brightly hand-coloured Nuremberg map from the Homann firm and its successors.", "Homann Heirs", "1702", HOM,
     [("Johann Baptist Homann", "Homann Heirs", "1702", "founder's own imprint"), ("Homann Heirs", "Homann Heirs", "", "firm folded 1852")], dt="imprint · colour"),
   X("Cassini sheet", "Sheet of the first triangulated general map of France at 1:86,400.", "Cassini", "", CAS, [], dt="sheet · colour"),
   X("Cary county map", "Late-Georgian English county map from John Cary's atlases.", "John Cary", "1787", CARY,
     [("New and Correct English Atlas", "John Cary", "1787", ""), ("New Universal Atlas", "John Cary", "1808", "")], dt="atlas · edition · colour"),
   X("Japanese woodblock map", "Edo-period woodblock-printed map of Japan or its provinces.", "", "", RYU,
     [("Ryūsen-zu", "Ishikawa Ryūsen", "1686", "decorative style with wavy coastlines; colour-printed, hand-tinted or black and white"),
      ("Sekisui-zu", "Nagakubo Sekisui", "1780", "first with latitude and longitude; second edition 1791")], dt="style · edition · colouring"),
  ]},
 {"n": "Antique atlas", "a": "", "d": "Bound atlas made before about 1850, complete or partly complete.",
  "t": ["complete", "incomplete", "contemporary binding", "rebound", "original hand colour", "uncoloured", "folio", "pocket"],
  "s": TOT,
  "x": [
   X("Ptolemy's Geographia", "Printed editions of Ptolemy's Geography, the first printed atlases.", "", "1477", PTO,
     [("Bologna", "", "1477", "26 engraved maps"), ("Rome", "", "1478", "Buckinck; plates reused to 1508"), ("Ulm", "", "1482", "Holle; woodcut"),
      ("Strasbourg", "", "1513", "47 maps, 20 modern"), ("Basel", "", "1540", "Münster; woodcut"), ("Venice", "", "1548", "Gastaldi; 60 copper maps"), ("Mercator", "", "1578", "28 maps")],
     a="Geographia · Cosmographia", dt="edition · map count · colour"),
   X("Theatrum Orbis Terrarum", "Ortelius's atlas of uniform maps with text, the first modern atlas.", "Abraham Ortelius", "1570", TOT,
     [("First edition", "Abraham Ortelius", "1570", "Antwerp, 53 maps"), ("Additamentum", "Abraham Ortelius", "1573", "17 more maps"), ("1612 edition", "", "1612", "167 maps")],
     dt="edition · language · colour"),
   X("Mercator–Hondius Atlas", "Mercator's atlas revised and enlarged by Hondius, continued with Janssonius.", "Hondius", "1606", HON,
     [("First Hondius edition", "Hondius", "1606", "Latin; 107 Mercator maps plus 37 new"), ("Atlas Minor", "Hondius", "1607", "pocket version"), ("Janssonius co-imprint", "Janssonius", "1633", "")],
     dt="edition · language · colour"),
   X("Atlas Maior", "Joan Blaeu's multi-volume world atlas, the largest and costliest book of its century.", "Blaeu", "1662", AM,
     [("Atlas Novus", "Blaeu", "1635", "two-volume predecessor"), ("Latin", "Blaeu", "1662", "11 volumes"), ("French", "Blaeu", "", "12 volumes"), ("Dutch", "Blaeu", "", "9 volumes"),
      ("German", "Blaeu", "", "10 volumes"), ("Spanish", "Blaeu", "", "10 volumes")], dt="language · volumes · colour"),
   X("Theatre of the Empire of Great Britaine", "John Speed's atlas of county maps and 73 town plans.", "John Speed", "1611", SPD, [], dt="edition · colour"),
   X("Grosser Atlas ueber die ganze Welt", "Homann's great world atlas.", "Homann Heirs", "1716", HOM, [], dt="edition · colour"),
   X("New and Correct English Atlas", "John Cary's county atlas, a standard English reference.", "John Cary", "1787", CARY, [], dt="edition"),
  ]},
 {"n": "Sea chart", "a": "nautical chart · pilot atlas · sea atlas", "d": "Printed chart or atlas of charts for navigation at sea; antique or retired.",
  "t": ["engraved", "lithographed", "blue-back", "chart with corrections", "loose sheet", "sea atlas", "pilot guide with charts"],
  "s": ADM,
  "x": [
   X("Waghenaer pilot atlas", "The first printed sea atlas: charts bound with sailing directions for European coasts.", "Lucas Janszoon Waghenaer", "1584", WAG,
     [("Spieghel der zeevaerdt", "Lucas Janszoon Waghenaer", "1584", "second part the next year"), ("Thresoor der zeevaert", "Lucas Janszoon Waghenaer", "1592", "")], a="waggoner", dt="edition · language"),
   X("Van Keulen sea atlas", "Amsterdam charts and pilot guides from the Van Keulen house.", "Van Keulen", "1681", VK,
     [("Nieuwe Lichtende Zee-Fakkel", "Van Keulen", "1681", "five volumes, over 130 charts, 1681–84")], dt="volume · edition"),
   X("Admiralty chart", "British official nautical chart, sold to the public since 1821.", "Admiralty", "1800", ADM,
     [("Copper-engraved chart", "Admiralty", "1800", "first printing"), ("Metric chart", "Admiralty", "1967", "buff land, magenta lights")], dt="chart number · edition · corrections"),
  ]},
 {"n": "Celestial chart", "a": "star chart · celestial atlas", "d": "Antique printed chart or atlas of the heavens, constellations or cosmological systems.",
  "t": ["star chart", "planisphere", "cosmological plate", "hand coloured", "loose plate", "complete atlas"],
  "s": HM,
  "x": [
   X("Harmonia Macrocosmica", "Andreas Cellarius's atlas of 29 plates of the Ptolemaic, Copernican and Tychonic systems and star charts.", "Janssonius", "1660", HM, [], dt="plate · colour"),
   X("Atlas Novus Coelestis", "Doppelmayr's 30-plate astronomical atlas with ten star charts.", "Homann Heirs", "1742", DOP, [], a="Doppelmayr", dt="plate · colour"),
  ]},
 {"n": "Pictorial map", "a": "illustrated map · novelty map", "d": "Map drawn as illustration, with pictures, humour or advertising rather than survey detail.",
  "t": ["poster", "folding", "promotional", "humorous", "souvenir", "printed colour"],
  "s": GILL,
  "x": [
   X("Wonderground map", "MacDonald Gill's humorous pictorial map of London advertising Underground travel, which started a golden age of pictorial maps.", "MacDonald Gill", "1914", GILL,
     [("First issue", "MacDonald Gill", "1914", "printed by G. W. Bacon"), ("Reduced 1920s edition", "MacDonald Gill", "1924", "Westminster Press")], dt="edition · size"),
  ]},
 {"n": "Vintage road map", "a": "strip map · oil-company map · gas-station map", "d": "Old road map, in strip or folded form, including free maps from oil companies.",
  "t": ["strip map", "folded", "oil-company giveaway", "state map", "city map", "cover art"],
  "s": BRIT,
  "x": [
   X("Ogilby strip map", "Road shown as a continuous strip at one inch to the mile, with the 1,760-yard mile.", "John Ogilby", "1675", BRIT,
     [("Britannia", "John Ogilby", "1675", "100 strip maps; tinted and monochrome editions"), ("Britannia Depicta", "", "1720", "Bowen and Owen's follow-on")], dt="edition · colour"),
   X("Oil-company road map", "Free folding road map handed out at service stations, printed by map firms under an oil company's brand.", "H.M. Gousha Company", "", HF,
     [("Phillips 66 Illinois", "H.M. Gousha Company", "1934", "")], dt="oil brand · state · year · cover"),
   X("Cary's New Itinerary", "John Cary's survey-based map of the major roads of England and Wales.", "John Cary", "1798", CARY, [], dt="edition"),
  ]},
]
def B(n, c, f, seg, kf, d, s, sig=(), rel=()):
    o = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "s": s}
    if sig: o["sig"] = list(sig)
    if rel: o["rel"] = list(rel)
    return o
brands = [
 B("Abraham Ortelius", "Spanish Netherlands", "", "Heritage manufactory", "first modern atlas", "Antwerp cartographer of the Theatrum Orbis Terrarum.", TOT, ["Theatrum Orbis Terrarum"]),
 B("Hondius", "Dutch Republic", "", "Heritage manufactory", "Mercator atlases", "Amsterdam map house of Jodocus Hondius and heirs, publisher of the Mercator–Hondius atlas.", HON, ["Mercator–Hondius Atlas"], ["Janssonius"]),
 B("Janssonius", "Dutch Republic", "", "Heritage manufactory", "atlases", "Jan Janssonius's Amsterdam house, co-publisher of the Mercator–Hondius atlas and of Cellarius.", HON, ["Harmonia Macrocosmica"], ["Hondius", "Blaeu"]),
 B("Blaeu", "Dutch Republic", "", "Heritage manufactory", "atlases", "Amsterdam map house of Willem and Joan Blaeu, publisher of the Atlas Novus and Atlas Maior.", AM, ["Atlas Maior"], ["Janssonius"]),
 B("John Speed", "England", "", "Heritage manufactory", "county maps", "English mapmaker whose Theatre of 1611 set the pattern for county atlases.", SPD, ["Speed county map"]),
 B("Homann Heirs", "Holy Roman Empire", "1702", "Heritage manufactory", "hand-coloured maps", "Nuremberg map house founded by Johann Baptist Homann, active until 1852.", HOM, ["Homann map", "Atlas Novus Coelestis"]),
 B("Cassini", "France", "", "Institution & issuer", "map of France", "Family of astronomers who compiled the 1:86,400 triangulated map of France.", CAS, ["Cassini sheet"]),
 B("John Cary", "England", "1783", "Heritage manufactory", "maps and globes", "London engraver and mapmaker of county atlases, road maps and globes.", CARY, ["Cary county map", "New and Correct English Atlas"]),
 B("Lucas Janszoon Waghenaer", "Dutch Republic", "", "Heritage manufactory", "sea atlases", "Dutch pilot whose Spieghel der zeevaerdt was the first printed sea atlas.", WAG, ["Waghenaer pilot atlas"]),
 B("Van Keulen", "Dutch Republic", "1678", "Heritage manufactory", "sea charts", "Amsterdam house of nautical charts and pilot guides, liquidated in 1885.", VK, ["Van Keulen sea atlas"]),
 B("Admiralty", "United Kingdom", "1795", "Institution & issuer", "nautical charts", "The UK Hydrographic Office's Admiralty chart series.", ADM, ["Admiralty chart"]),
 B("MacDonald Gill", "United Kingdom", "", "Artisan & independent", "pictorial maps", "English designer of the Wonderground map.", GILL, ["Wonderground map"]),
 B("John Ogilby", "England", "", "Heritage manufactory", "strip road maps", "Publisher of Britannia, the strip-map road atlas of 1675.", BRIT, ["Ogilby strip map"]),
 B("H.M. Gousha Company", "United States", "", "Specialist", "road maps", "American printer of oil-company road maps.", HF, ["Oil-company road map"]),
 B("Ishikawa Ryūsen", "Japan", "", "Artisan & independent", "woodblock maps", "Edo-period ukiyo-e artist and writer whose decorative maps are called Ryūsen-zu.", RYU),
 B("Nagakubo Sekisui", "Japan", "", "Artisan & independent", "woodblock maps", "Edo-period geographer whose 1780 map of Japan introduced latitude and longitude.", SEK),
]
traditions = [
 {"n": "Dutch and Flemish golden-age cartography", "g": "Paper & print", "r": "Antwerp and Amsterdam", "p": "16th–17th century",
  "d": "Commercial map and atlas publishing in the Low Countries that dominated European map production.", "tech": "copper engraving, hand colouring",
  "mat": "laid paper", "forms": ["Antique atlas", "Antique map", "Sea chart", "Celestial chart"], "ctr": ["Abraham Ortelius", "Gerard de Jode", "Gerard Mercator", "Hondius", "Blaeu", "Janssonius"],
  "auth": "text language and edition on the verso, paper and platemark, contemporary versus later colour", "s": OSH},
 {"n": "Japanese woodblock cartography", "g": "Paper & print", "r": "Japan", "p": "Edo period (late 17th–19th century)",
  "d": "Commercially printed woodblock maps of Japan and its provinces, from the decorative Ryūsen-zu to the more accurate Sekisui-zu.", "tech": "woodblock printing, colour printing, hand tinting",
  "mat": "washi paper", "forms": ["Antique map"], "ctr": ["Ishikawa Ryūsen", "Nagakubo Sekisui"],
  "auth": "edition and block revisions, place-name count, colouring", "s": RYU},
]
notes = ("New shelf, no old kinds. Six planned kinds built with cartographer-keyed archetypes. Loose sheets under Antique map, whole works under Antique atlas (Ptolemy, Ortelius, Mercator–Hondius, Blaeu, Speed, Homann, Cary). "
         "Cassini sheet count left out (sources disagree, 180–182). Celestial: Cellarius and Doppelmayr; Doppelmayr 1748 edition not confirmed so omitted. Mid-century road maps: oil-company maps via Gousha; Rand McNally and General Drafting not added (no fetched page). "
         "Two traditions added (Dutch/Flemish golden age, Japanese woodblock maps). Brand entries are historic map houses and cartographers keyed to archetype mk.")
out = {"kinds": kinds, "brands": brands, "traditions": traditions, "notes": notes}
p = 'work/F1/shelves/06_01.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
