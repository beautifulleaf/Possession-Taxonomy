import json, os
W = 'https://en.wikipedia.org/wiki/'
K = 'knowledge'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
OS = 'https://ordnancesurvey.co.uk/blog/a-history-of-paper-maps'; IGN25 = 'https://www.ffrandonnee.fr/s-informer/actualites/cartographie-la-serie-ign-top-25-se-renouvelle'
MICH = 'https://blog.stanfords.co.uk/blog/2003/05/01/michelin-the-maps-they-are-a-changing/'; USGS = 'https://www.fs.usda.gov/r06/umpqua/maps-guides/75-minute-quadrangle-topographic-maps'
HAR = 'https://www.harveymaps.co.uk/acatalog/Superwalker-XT-The-Complete-Collection-YHSWSET.html'; NOR = W + 'Nordeca'
TIMES = W + 'Times_Atlas_of_the_World'; NG = 'https://www.nationalgeographic.com/science/article/131103-national-geographic-maps-atlas-changes-cartography'
PHIL = 'https://www.hachette.co.uk/titles/none/philips-navigator-britain-the-champion-of-road-atlases/9781849077316/'; AZ = W + 'Geographers%27_A%E2%80%93Z_Map_Company'
FMX = 'https://www.formaxprinting.com/blog/common-types-of-printed-maps'
kinds = [
 {"n": "Folded map", "a": "sheet map · pocket map · tear-off map pad", "d": "Printed map sheet folded to pocket size for carrying; the area covered and scale are noted.",
  "t": ["paper", "waterproof / laminated", "tear-off map pad", "flat sheet", "concertina fold", "1:25,000", "1:50,000", "1:100,000", "1:200,000", "topographic", "road", "street plan", "custom-centred"],
  "s": FMX,
  "x": [
   X("Ordnance Survey 1:25,000", "Britain's most detailed national leisure map, showing rights of way and open access, with orange covers.", "Ordnance Survey", "1972", OS,
     [("Outdoor Leisure", "Ordnance Survey", "1972", "national parks and popular areas"), ("Pathfinder", "Ordnance Survey", "", "rights of way in England and Wales"),
      ("Explorer", "Ordnance Survey", "1994", "three times a Pathfinder's area; 403 sheets by 2003, orange cover")], a="OS Explorer", dt="sheet number · paper or weatherproof · edition"),
   X("Ordnance Survey 1:50,000", "Britain's general-purpose national map in 204 sheets with pink covers.", "Ordnance Survey", "1974", OS,
     [("One-inch", "Ordnance Survey", "1801", "predecessor scale"), ("First Series", "Ordnance Survey", "1974", "204 sheets, 1974–76"), ("Landranger", "Ordnance Survey", "1980s", "pink cover")],
     a="OS Landranger", dt="sheet number · paper or weatherproof · edition"),
   X("IGN 1:25,000", "France's walking map at 1:25,000: TOP 25 for coasts, forests and mountains, Série Bleue for the rest.", "IGN", "", IGN25,
     [("TOP 25", "IGN", "", ""), ("Série Bleue", "IGN", "2014", "renewed 2014–18; each sheet 685 km²")], dt="sheet number · edition"),
   X("IGN TOP 100", "France's 1:100,000 tourist and road series, successor to the Série Verte.", "IGN", "", MICH,
     [("Série Verte", "IGN", "", "original name"), ("Série Rouge", "IGN", "", "regional series, later the IGN regional maps")], dt="sheet number"),
   X("Michelin 1:200,000", "Michelin's concertina-folded 'yellow maps' of France, the benchmark motoring map.", "Michelin", "1910s", MICH,
     [("France in 47 sheets", "Michelin", "1910s", "concertina format"), ("Corsica sheet", "Michelin", "1921", "completed the series"),
      ("British Isles series", "Michelin", "1920s", "31 sheets"), ("Regional maps", "Michelin", "1970s", "17 sheets for mainland France"),
      ("Local Maps", "Michelin", "2003", "replaced the concertina series")], a="yellow maps", dt="sheet number · edition"),
   X("USGS 7.5-minute quadrangle", "United States topographic map sheet at 1:24,000 covering about 50–70 square miles.", "USGS", "", USGS,
     [], a="quad · 24K quadrangle", dt="quadrangle name · colour or black and white"),
   X("Harvey Superwalker XT", "Waterproof 1:25,000 walkers' maps of British (1:30,000 Irish) hill areas.", "Harvey", "", HAR,
     [("Superwalker XT", "Harvey", "", "1:25,000 UK, 1:30,000 Ireland; 55 titles"), ("British Mountain Map", "Harvey", "", ""), ("Ultramap", "Harvey", "", ""), ("Trail Map", "Harvey", "", "")],
     dt="title · scale"),
   X("Nordeca Turkart", "Norwegian topographic hiking maps.", "Nordeca", "", NOR,
     [("Turkartserien", "Nordeca", "", "hiking maps"), ("Norge-serien", "Nordeca", "", "systematic topographic series")], dt="sheet number"),
  ],
  "m": [["Fjällkartan", "Norstedts"], ["TOP 250", "IGN"], ["Discoverer", "Ordnance Survey"], ["Veikart", "Nordeca"]]},
 {"n": "Atlas", "a": "road atlas · world atlas · street atlas", "d": "Bound book of maps, sold in boards, flexible cover or spiral-bound to lie flat.",
  "t": ["bound atlas", "spiral-bound", "lie-flat paperback", "large-print (easy read)", "road atlas", "street atlas", "world reference atlas", "school atlas"],
  "s": TIMES,
  "x": [
   X("The Times Atlas of the World", "Large-format British world reference atlas, issued in numbered editions since 1895.", "Times Books", "1895", TIMES,
     [("First edition", "", "1895", "117 map pages, 130,000 index names"), ("Times Survey Atlas", "", "1922", "Bartholomew, 47 × 33 cm"),
      ("Mid-Century Edition", "", "1955", "five elephant-folio volumes, 1955–59"), ("Comprehensive Edition", "", "1967", "one volume, maps both sides"),
      ("10th edition", "Times Books", "1999", "first fully computer-produced"), ("16th edition", "HarperCollins", "2023", "")], dt="edition · binding"),
   X("National Geographic Atlas of the World", "American world reference atlas, first published after seven years' work.", "National Geographic Society", "1963", NG,
     [("First edition", "National Geographic Society", "1963", "about 127,000 place names"), ("Second edition", "National Geographic Society", "1966", ""), ("10th edition", "National Geographic Society", "2014", "")],
     dt="edition · binding"),
   X("Philip's Navigator", "British road atlas at 1:100,000 (1.5 miles to the inch), sold as the best-selling detailed road atlas.", "Philip's", "", PHIL,
     [("Lie-flat paperback", "Philip's", "", ""), ("Spiral-bound", "Philip's", "", "")], dt="edition year · binding"),
   X("A–Z street atlas", "Indexed city street atlas, begun for London in the late 1930s.", "Geographers' A–Z Map Company", "1936", AZ,
     [("London", "Geographers' A–Z Map Company", "", "first A–Z street atlas"), ("Birmingham", "Geographers' A–Z Map Company", "1953", ""), ("Manchester", "Geographers' A–Z Map Company", "1963", "")],
     a="A to Z", dt="city · edition · binding"),
  ],
  "m": [["AA Traveller's Atlas", "AA"], ["AA Big Easy Read Atlas", "AA"], ["Philip's Britain & Ireland Road Atlas", "Philip's"], ["Great Britain A-Z Super Scale Road Atlas", "Geographers' A–Z Map Company"]]},
 {"n": "Wall map", "a": "", "d": "Map printed or mounted to hang flat on a wall, laminated or not.",
  "t": ["laminated", "paper", "framed", "pin board", "world", "country", "city", "Peters projection"],
  "s": "https://www.stanfords.co.uk/", "m": [["Bildkarten wall map", "Bollmann"], ["London Premier A-Z Wall Map", "Geographers' A–Z Map Company"]]},
 {"n": "Map booklet", "a": "", "d": "Map issued as a small stapled or bound booklet of map sections.", "t": ["stapled", "spiral-bound", "route booklet"], "s": FMX},
]
brands = [
 {"n": "Ordnance Survey", "c": "United Kingdom", "f": "1791", "seg": "Institution & issuer", "kf": "national mapping", "d": "Great Britain's national mapping agency, publisher of the Explorer and Landranger series.", "lines": ["Explorer", "Landranger", "Outdoor Leisure", "Pathfinder"], "sig": ["Ordnance Survey 1:25,000", "Ordnance Survey 1:50,000"], "s": K},
 {"n": "IGN", "c": "France", "f": "1940", "seg": "Institution & issuer", "kf": "national mapping", "d": "France's national mapping institute (Institut national de l'information géographique et forestière).", "lines": ["TOP 25", "Série Bleue", "TOP 100", "TOP 250"], "sig": ["IGN 1:25,000", "IGN TOP 100"], "s": K},
 {"n": "Michelin", "c": "France", "f": "1889", "seg": "Mainstream", "kf": "road maps, guides", "d": "French tyre maker publishing road maps and guides since 1900.", "lines": ["Local Maps", "Regional maps"], "sig": ["Michelin 1:200,000"], "s": MICH},
 {"n": "USGS", "c": "United States", "f": "1879", "seg": "Institution & issuer", "kf": "topographic maps", "d": "United States Geological Survey, publisher of the 7.5-minute quadrangle series.", "sig": ["USGS 7.5-minute quadrangle"], "s": K},
 {"n": "Harvey", "c": "United Kingdom", "f": "", "seg": "Specialist", "kf": "walkers' maps", "d": "Scottish publisher of waterproof walking and mountain maps.", "lines": ["Superwalker XT", "British Mountain Map", "Ultramap", "Trail Map"], "sig": ["Harvey Superwalker XT"], "s": HAR},
 {"n": "Nordeca", "c": "Norway", "f": "1990", "seg": "Specialist", "kf": "leisure maps", "d": "Lysaker map company, founded as Totalkart, leading Norway's printed leisure maps.", "lines": ["Turkartserien", "Norge-serien"], "sig": ["Nordeca Turkart"], "s": NOR},
 {"n": "Times Books", "c": "United Kingdom", "f": "", "seg": "Premium", "kf": "world atlases", "d": "Imprint publishing The Times Atlas of the World, now within HarperCollins.", "sig": ["The Times Atlas of the World"], "s": TIMES},
 {"n": "National Geographic Society", "c": "United States", "f": "1888", "seg": "Institution & issuer", "kf": "maps, atlases", "d": "American geographic society publishing world atlases and maps.", "sig": ["National Geographic Atlas of the World"], "s": K},
 {"n": "Philip's", "c": "United Kingdom", "f": "1834", "seg": "Mainstream", "kf": "road atlases", "d": "British map and atlas publisher, part of Hachette UK.", "sig": ["Philip's Navigator"], "s": K},
 {"n": "Geographers' A–Z Map Company", "c": "United Kingdom", "f": "1936", "seg": "Mainstream", "kf": "street atlases", "d": "London publisher of A–Z street atlases, founded by Alexander Gross; list sold to HarperCollins in 2019.", "sig": ["A–Z street atlas"], "s": AZ},
 {"n": "AA", "c": "United Kingdom", "f": "1905", "seg": "Mainstream", "kf": "road atlases", "d": "The Automobile Association, British motoring organisation publishing road atlases.", "s": K},
]
notes = ("Old Folded map and Tear-off map pad merged (pad as t). National survey series became archetypes (OS 1:25k/1:50k, IGN 1:25k and TOP 100, Michelin 1:200k, USGS quad, Harvey, Nordeca); "
         "Fjällkartan kept as model only (no fetchable page confirmed it; maker pages blocked). Atlases: Times Atlas, National Geographic, Philip's Navigator, A–Z as archetypes; AA atlases kept as models. "
         "Old Atlas kind had no source; now cites the Times Atlas page. Peters projection wall map moved to t (not a product). Bollmann kept as a model without a brand entry.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = 'work/F1/shelves/06_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
