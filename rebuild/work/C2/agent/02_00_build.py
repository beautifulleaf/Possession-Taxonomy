import json, os
W = {
 'spade': 'https://en.wikipedia.org/wiki/Spade',
 'fork': 'https://en.wikipedia.org/wiki/Garden_fork',
 'shovel': 'https://en.wikipedia.org/wiki/Shovel',
 'mattock': 'https://en.wikipedia.org/wiki/Mattock',
 'broadfork': 'https://en.wikipedia.org/wiki/Broadfork',
 'loy': 'https://en.wikipedia.org/wiki/Loy_(spade)',
}
NB = 'https://www.spear-and-jackson.com/files/catalogues/Neverbend_Sep09_low.pdf'
OLD_S = 'https://www.hornbach.de/c/garten/gartenwerkzeug-gartengeraete/S1943/'
SJ = 'Spear & Jackson'

def x(n, d, s, mk='', y='', a='', v=None, dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": v or [], "dt": dt}

def v(n, mk, y='', d=''):
    return {"n": n, "mk": mk, "y": y, "d": d}

kinds = [
 {"n": "Garden spade", "a": "spade", "d": "Long-handled tool with a flat, sharp-edged blade pushed in by foot to dig and cut soil.",
  "t": ["treaded", "untreaded", "carbon steel", "stainless steel", "T-grip", "D-grip", "YD-grip", "long-handled"],
  "s": OLD_S,
  "x": [
   x("Digging spade", "The standard full-size spade: long handle, wide treaded blade for digging and turning soil.", W['spade'], a="garden spade",
     v=[v("Neverbend Digging Spade - Treaded (1180NB)", SJ, "2009", "Neverbend Carbon re-introduction; solid forged carbon steel, 280 × 180 mm blade"),
        v("Neverbend Stainless Digging Spade (1160SP)", SJ, "2009", "Neverbend Stainless; 280 × 180 mm blade"),
        v("Neverbend Professional Treaded Digging Spade (1071AL)", SJ, "2009", "Professional range; 290 × 190 mm blade"),
        v("Spade with Steps", "Sneeboer", "", "hand-forged, curved blade, ash handle 85–100 cm"),
        v("Dutch Digging Spade", "DeWit", "", "hand-forged Swedish boron steel, 6½ × 11 in blade, ash T-handle")],
     dt="blade c. 280–290 × 180–190 mm · forged carbon or stainless steel · treads · shaft length and grip"),
   x("Border spade", "Smaller blade than a digging spade with a proportionately longer handle, for work among plants.", W['spade'], a="ladies' spade",
     v=[v("Border Spade", "Sneeboer"),
        v("Neverbend Border Spade - Treaded (1184NB)", SJ, "2009", "230 × 138 mm blade"),
        v("Neverbend Stainless Border Spade (1161BS)", SJ, "2009", "230 × 138 mm blade"),
        v("Long Handle Spade", "Joseph Bentley", "", "narrow polished stainless head, small treads, extra-long handle")],
     dt="blade c. 230 × 140 mm · stainless or carbon steel · handle length"),
   x("Transplanting spade", "Long, narrow, round-ended blade for lifting and moving plants among dense planting.", "https://www.rhsplants.co.uk/product/_/rhs-burgon-and-ball-stainless-transplanting-spade/classid.2000029182/",
     v=[v("RHS Stainless Transplanting Spade", "Burgon & Ball", "", "RHS-endorsed; 14 × 28 cm stainless blade, ash shaft, Y handle")],
     dt="blade c. 14 × 28 cm · stainless steel · treads"),
   x("Irish spade", "Spade like a garden spade but with a much thinner, longer head and a long handle.", W['spade'],
     v=[v("Neverbend Professional Irish Spade (1072AY)", SJ, "2009", "330 mm blade, 36 in shaft")],
     dt="blade length · shaft length"),
   x("Loy", "Narrow Irish spade with a single footrest on a long ash handle, used to build potato lazy beds.", W['loy'], y="19th century–1960s", a="lazy-bed spade",
     dt="blade c. 35 × 7.5 cm · handle c. 1.5–1.8 m · single footrest"),
   x("Sharpshooter", "Long, narrow spade, sometimes with flanged treads, for tight spots, trenches and post holes.", W['spade'], a="drain spade · trenching spade",
     dt="blade length and width · flanged or plain treads"),
   x("Fishtail spade", "Spade with a flared triangular blade, combining a Dutch hoe's versatility with a round-point shovel's power.", W['spade'],
     dt="blade shape · shaft length"),
   x("Turfing iron", "Short, round-headed spade for cutting and paring off turf.", W['spade'], dt="head diameter · handle"),
   x("Golden Spade", "Japanese all-steel spade with a tubular steel shaft and YD handle, used for digging and planting.", "https://www.scp.co.uk/products/japanese-golden-spade", mk="Niwaki",
     v=[v("Small", "Niwaki", "", "17 cm wide, 82 cm tall"), v("Standard", "Niwaki", "", "23 cm wide, 97 cm tall"), v("Long", "Niwaki", "", "24 cm wide, 110 cm tall")],
     dt="size small / standard / long · gold-painted steel"),
  ],
  "m": [["Xact Teleskop-Spaten", "Fiskars"], ["Hand spade", "DeWit"]]},

 {"n": "Garden fork", "a": "digging fork · spading fork", "d": "Long-handled tool with stout tines to dig, loosen and turn soil.",
  "t": ["digging", "border", "manure", "carbon steel", "stainless steel"],
  "s": OLD_S,
  "x": [
   x("Digging fork", "Standard garden fork with a square-shouldered head and usually four short, sturdy tines.", W['fork'], a="spading fork",
     v=[v("4t digging fork", "Sneeboer"),
        v("Neverbend Digging Fork (1680NB)", SJ, "2009", "solid forged carbon steel, 280 × 180 mm head"),
        v("Neverbend Stainless Digging Fork (1560SF)", SJ, "2009"),
        v("Neverbend Professional Digging Fork (1570AL)", SJ, "2009", "305 × 208 mm head"),
        v("Digging Fork - RHS Endorsed", "Burgon & Ball", "", "stainless steel tines")],
     dt="four tines · head size · carbon or stainless · D- or T-grip"),
   x("Border fork", "Smaller fork with shorter, thinner, closer tines on a full-size handle, for light work among plants.", W['fork'], a="ladies' fork",
     v=[v("Neverbend Border Fork (1684NB)", SJ, "2009", "230 × 138 mm head"),
        v("Neverbend Stainless Border Fork (1561BF)", SJ, "2009")],
     dt="head size · carbon or stainless"),
   x("Potato fork", "Fork with broader, flatter tines for lifting potatoes and other root crops.", W['fork'], a="root-crop fork",
     v=[v("Neverbend Professional Potato Fork (1650SN)", SJ, "2009", "280 × 180 mm head")],
     dt="tine width and number"),
   x("Spork", "Spade-fork hybrid with a ventilated, tined head and cutting edge that both digs and loosens soil.", "https://www.gardentoolcompany.com/products/dewit-spork", mk="DeWit",
     v=[v("Spork", "DeWit", "", "Swedish boron steel, 6¼ × 9½ in head, ash T-handle")],
     dt="head size · handle"),
  ]},

 {"n": "Shovel", "a": "", "d": "Long-handled tool with a broad, dished blade to lift and move loose soil or material.",
  "t": ["round-point", "square", "Holsteiner", "open socket", "D-grip", "long handle"],
  "s": OLD_S,
  "x": [
   x("Round-point shovel", "Shovel with a wider, tapered blade ending in a point, for digging and lifting.", W['spade'], dt="blade width · handle length"),
   x("Square-mouth shovel", "Shovel with a squarish blade edge for scooping loose material from hard surfaces.", W['shovel'], a="square shovel",
     v=[v("Neverbend Open Socket Shovel Square Mouth (2581NB)", SJ, "2009", "320 × 255 mm blade")],
     dt="blade size · open or closed socket"),
   x("Holsteiner shovel", "German shovel with a straight front edge, for digging and moving loose, sandy soil.", "https://www.globus-baumarkt.de/p/freund-victoria-holsteiner-schaufel-rot-eschestiel-0760351160/", a="Holsteiner Schaufel",
     v=[v("Holsteiner Schaufel", "Freund Victoria", "", "size 2, oil-hardened steel, 130 cm ash handle")],
     dt="blade size 1–3 · handle length"),
   x("Grain shovel", "Large, wide aluminium or plastic blade on a short handle for light loose material.", W['shovel'], a="barn shovel", dt="blade material · width"),
   x("Spoon shovel", "Long handle with a small, oval, cupped blade for deep, narrow holes.", W['shovel'], dt="blade size · handle length"),
  ],
  "m": [["Compact shovel ash T handle", "DeWit"]]},

 {"n": "Mattock", "a": "grub axe", "d": "Swung tool with a heavy head carrying an adze blade, used to break hard ground and cut roots.",
  "t": ["pick", "cutter", "hoeing", "pronged"],
  "s": OLD_S,
  "x": [
   x("Pick mattock", "Head with a pointed pick at one end and an adze blade at the other, for breaking hard ground.", W['mattock'], dt="head weight · shaft length c. 3–4 ft"),
   x("Cutter mattock", "Head with a vertical axe blade and a longer horizontal adze, best for cutting roots.", W['mattock'], a="grub axe",
     dt="head weight · shaft length"),
  ],
  "m": [["Planter Mattock", "Hoedag"], ["2 prong hoeing mattock", "DeWit"], ["3 prong digging mattock", "DeWit"], ["Fork & Mattock", "Sneeboer"]]},

 {"n": "Broadfork", "a": "U-fork · grelinette", "d": "Two-handled wide fork with long tines, rocked back to loosen soil deeply without turning it.",
  "t": ["steel", "wooden handles", "raised-bed width"],
  "s": "https://www.gardenersedge.com/c/planting-tools",
  "x": [
   x("Grelinette", "The original two-handled fork-spade with three to five bent tines that loosens soil without inverting it.", "https://fr.wikipedia.org/wiki/Grelinette",
     mk="André Grelin", y="1964", a="biobêche",
     v=[v("FR 1378114 'Dispositif pour jardinage'", "André Grelin", "1964", "patent")], dt="number of tines · width · handles"),
   x("People's Broadfork", "All-steel welded broadfork made in the USA from mostly recycled steel.", "https://meadowcreature.com/", mk="Meadow Creature",
     v=[v("People's Broadfork - 12\" tines", "Meadow Creature")], dt="tine length"),
   x("U-bar", "Broadfork-like digger with longer tines (up to 18 in) and elbows, for beds already double dug.", W['broadfork'], dt="tine length"),
  ]},
]

brands = [
 {"n": "Sneeboer", "c": "Netherlands", "f": "1913", "seg": "Hand-forged premium garden tools",
  "d": "Family forge founded by Arie Sneeboer, now in Bovenkarspel, making stainless garden tools since the early 1950s.",
  "lines": [], "eras": ["Arie Sneeboer, 1913–1956", "sons, 1956–1969", "fourth generation, present"],
  "sig": ["Digging spade", "Border spade", "Digging fork"], "sc": [], "rel": ["DeWit"], "s": "https://sneeboer.com/en/history"},
 {"n": "DeWit", "c": "Netherlands", "f": "1898", "seg": "Hand-forged premium garden tools",
  "d": "Blacksmith firm started by Willem de Wit in Kornhorn, run by the fourth generation, known for the Dutch hoe.",
  "lines": [], "eras": [], "sig": ["Spork", "Digging spade"], "sc": [], "rel": ["Sneeboer"],
  "s": "https://europeantoolsaustralia.com/blogs/news/dewit-a-company-history"},
 {"n": "Spear & Jackson", "c": "United Kingdom", "f": "1760", "seg": "Mainstream garden and hand tools",
  "d": "Sheffield tool maker, formed as Spear & Love and as Spear & Jackson from 1830; owned by SNH Global since 2014.",
  "lines": ["Neverbend Carbon", "Neverbend Stainless", "Neverbend Professional", "Eclipse"], "eras": [],
  "sig": ["Digging spade", "Border spade", "Irish spade"], "sc": [], "rel": [], "s": "https://en.wikipedia.org/wiki/Spear_%26_Jackson"},
 {"n": "Bulldog Tools", "c": "United Kingdom", "f": "1780", "seg": "Solid-forged spades and forks",
  "d": "Wigan maker founded by William and Henry Parkes at Clarington Forge; spades issued to British forces since WW1.",
  "lines": [], "eras": ["Rollins Group ownership, 2004–"], "sig": [], "sc": [], "rel": [], "s": "https://en.wikipedia.org/wiki/Bulldog_Tools"},
 {"n": "Joseph Bentley", "c": "United Kingdom", "f": "1895", "seg": "Stainless garden tools",
  "d": "Sheffield horticultural tool brand known for polished stainless spades with ash handles.",
  "lines": [], "eras": [], "sig": ["Border spade"], "sc": [], "rel": [], "s": "https://www.gardenista.com/products/joseph-bentley-long-handle-spade/"},
 {"n": "Burgon & Ball", "c": "United Kingdom", "f": "1730", "seg": "Garden tools (RHS-endorsed range)",
  "d": "Sheffield firm that began with agricultural shears and now sells RHS-endorsed garden tools.",
  "lines": ["RHS Endorsed Tools"], "eras": [], "sig": ["Transplanting spade", "Digging fork"], "sc": [], "rel": [], "s": "https://www.burgonandball.com/"},
 {"n": "Niwaki", "c": "United Kingdom", "f": "2006", "seg": "Japanese garden tools",
  "d": "Jake Hobson's business selling tools from Japan, plus pruning courses.",
  "lines": [], "eras": ["Jake Hobson, 2006–"], "sig": ["Golden Spade"], "sc": [], "rel": [], "s": "https://www.gardensillustrated.com/gardens/gardeners/jake-hobson-niwaki-interview"},
 {"n": "Freund Victoria", "c": "Germany", "f": "", "seg": "Mainstream garden tools",
  "d": "Garden tool maker in Schorndorf selling spades and Holsteiner shovels with ash handles.",
  "lines": [], "eras": [], "sig": ["Holsteiner shovel"], "sc": [], "rel": [], "s": "https://www.globus-baumarkt.de/p/freund-victoria-holsteiner-schaufel-rot-eschestiel-0760351160/"},
 {"n": "Krumpholz", "c": "Germany", "f": "", "seg": "Forged garden and forestry tools",
  "d": "Family forge at Guttenbergerhammer, Grafengehaig, making spades, hoes and axes from Swedish steel for over 220 years.",
  "lines": ["Spitzspaten"], "eras": [], "sig": [], "sc": [], "rel": [], "s": "https://www.lebensartmagazin.de/2023/09/15/krumpholz-zweitgroesste-investition-der-firmengeschichte-2/"},
 {"n": "Meadow Creature", "c": "United States", "f": "", "seg": "Broadforks",
  "d": "US maker of all-steel broadforks from recycled steel, sold with a lifetime warranty.",
  "lines": [], "eras": [], "sig": ["People's Broadfork"], "sc": [], "rel": [], "s": "https://meadowcreature.com/"},
]

notes = ("All five planned kinds kept. Mattock: dropped A.M. Leonard Cutter/Pick Mattock trade SKUs (scope rule); pick and cutter mattock "
 "kept as maker-free archetypes; Hoedag, DeWit and Sneeboer models kept in m. Old Freund maker recorded as Freund Victoria (retrieved page). "
 "Niwaki Golden Spade sourced from a retailer page (niwaki.com returned 403). Not added for lack of a retrievable page this session: "
 "Krumpholz specific spade models beyond the Spitzspaten line and its founding year; Clarington Forge/Bulldog named models; Meadow Creature tall broadfork "
 "(429); a Gardener's broadfork pattern; manure fork as archetype (kept as type). Snow and coal shovels left to other shelves/out. No traditions: no artisan "
 "tradition beyond the Irish loy, which is an archetype.")

out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/C2/shelves/02_00.json'
tmp = p + '.tmp'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, p)
print('written')
