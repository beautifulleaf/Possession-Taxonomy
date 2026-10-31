import json, os
W = 'https://en.wikipedia.org/wiki/'
X = []
def a(n, al, d, mk, y, s, v=(), dt=''):
    X.append({"n": n, "a": al, "d": d, "mk": mk, "y": y, "s": s,
              "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt})

LP = "Louis Poulsen"
a("PH lamp", "PH three-shade lamp · PH pendant", "Poul Henningsen's layered-shade system that hides the bulb and spreads glare-free light; the first PH lamp won gold in Paris 1925.",
  LP, "1925–26", W + "PH_lamp",
  [("PH 5", LP, "", "the best-known three-shade pendant"), ("PH 5 Mini", LP, "", "smaller PH 5"),
   ("PH 3/3", LP, "", "three-shade pendant, 30 cm top shade"),
   ("PH 4/3", "", "1928", "glass shades; metal version 1966"),
   ("PH Septima", "", "1927–31", "seven partly sandblasted glass shades"),
   ("PH Four-Shade Lamp", LP, "1930", "four shades; relaunched 1979 as PH 6½–6"),
   ("PH Louvre", LP, "1954", "13 shades; for the Adventist church, Skodsborg"),
   ("PH Snowball", LP, "1954", "8 shades"),
   ("PH Artichoke", LP, "1958", "layered leaf shades; for the Langelinie Pavilion"),
   ("PH Plate Lamp", LP, "1958", "for the Langelinie Pavilion"),
   ("PH Contrast", LP, "1959", "ten lacquered shades in four colours; original run ended 1991"),
   ("PH Globen", LP, "", "")],
  "shade system (3:2:1 proportions, e.g. PH 5/5 = 50/31/16.5 cm) · metal, glass, copper · colourways")
a("VL45 Radiohus", "VL45 Radiohus pendant", "Opal glass globe pendant by architect Vilhelm Lauritzen, named after his Radiohuset broadcasting house in Copenhagen (1936–41).",
  LP, "1936–41", "https://cultdesign.com.au/products/vl45-radiohus-pendant-o370mm",
  [("Ø370 mm", LP, "", "largest size")], "diameter · glass shade with bottom opening")
a("Bubble lamp", "Nelson Bubble lamp", "George Nelson's pendants of plastic membrane stretched over a wire frame.",
  "Howard Miller Clock Company", "1947", W + "George_Nelson_(designer)",
  [("Howard Miller original", "Howard Miller Clock Company", "1947", "first production"),
   ("Modernica", "Modernica", "", "later licensed maker"),
   ("Herman Miller", "Herman Miller", "", "current maker")],
  "shape · diameter")
a("Flowerpot", "Flower Pot lamp", "Verner Panton's late-1960s pop-era pendant lamp.",
  "Verner Panton", "c. 1967–69", W + "Verner_Panton", [], "size · lacquer colours")
a("Caravaggio", "Caravaggio pendant", "Cecilie Manz's bell-shaped lacquered pendant with an upward opening that lights its own cord.",
  "Fritz Hansen", "2005", "https://www.nedgis.com/en/products/pendant-light-caravaggio-p3-black-o40cm-h51-6cm-lightyears",
  [("Caravaggio (Lightyears)", "Lightyears", "2005", "original label, now Fritz Hansen"),
   ("Caravaggio Matt", "Fritz Hansen", "", "matt lacquer instead of high gloss"),
   ("Caravaggio Opal", "Fritz Hansen", "", "opal glass shade")],
  "five diameters 11–55 cm · white, black, chrome black · cord colours")
a("Akari pendant", "Akari light sculpture", "Isamu Noguchi's washi-paper and bamboo shades, hand-made in Gifu; over 200 shapes.",
  "Ozeki & Co.", "1951", W + "Akari_(lamp)", [], "shape · size · washi paper, bamboo, metal")
a("Random Light", "Random pendant", "Bertjan Pot's sphere of epoxy-soaked fibreglass yarn coiled at random round an inflatable mould.",
  "Moooi", "2001", "https://hivemodern.com/pages/product3270/moooi-bertjan-pot-random-suspension-light",
  [("Random Light", "Moooi", "2001", "original")], "S/M/L (about 50, 80, 105 cm) · white, black")
a("Beat light", "Beat pendant", "Tom Dixon's spun brass pendants hand-beaten in Moradabad, shaped after Indian cooking and water vessels.",
  "Tom Dixon", "2006", "https://www.rume.co.uk/tom-dixon-beat-light-stout.html",
  [("Beat Fat", "Tom Dixon", "", ""), ("Beat Stout", "Tom Dixon", "", ""), ("Beat Tall", "Tom Dixon", "", ""), ("Beat Wide", "Tom Dixon", "", "")],
  "shape · black, white, brass or grey exterior with hammered interior")
a("Mirror Ball", "Mirror Ball pendant", "Tom Dixon's polycarbonate globe vacuum-metallised inside to a mirror finish.",
  "Tom Dixon", "2004", "https://hivemodern.com/pages/product7625/mirror-ball-pendant-light-tom-dixon",
  [("Mirror Ball 25", "Tom Dixon", "", "25 cm"), ("Mirror Ball 40", "Tom Dixon", "", "40 cm"), ("Mirror Ball 50", "Tom Dixon", "", "50 cm")],
  "diameter · vacuum-metallised mirror finish")
a("Big Bang", "", "Enrico Franzolini and Vicente García Jiménez's pendant of intersecting methacrylate planes like a frozen explosion.",
  "Foscarini", "2005", "https://hivemodern.com/pages/product2163/foscarini-big-bang-suspension-lamp",
  [("Big Bang", "Foscarini", "2005", "original size"), ("Big Bang L / XL LED", "Foscarini", "2016", "large LED versions shown at Salone 2016")],
  "size · white, red · bulb or LED")
a("Caboche", "Caboche Plus", "Patricia Urquiola and Eliana Gerotto's pendant of clear acrylic spheres round a blown-glass diffuser, like a beaded bracelet.",
  "Foscarini", "2005", "https://www.hivemodern.com/pages/product2158/caboche-plus-suspension-lamp-patricia-urquiola-foscarini",
  [("Caboche", "Foscarini", "2005", "original"), ("Caboche Plus", "Foscarini", "", "current family")],
  "small, medium, large")
a("Porca Miseria!", "", "Ingo Maurer's suspension lamp built from smashed porcelain shards.", "Ingo Maurer", "1994", W + "Ingo_Maurer", [], "one-off, hand-assembled")
a("Zettel'z", "Zettel'z hanging lamp", "Ingo Maurer's hanging lamp of paper notes (Zettel = note).", "Ingo Maurer", "1997", W + "Ingo_Maurer", [], "")
a("Splüghen Braü", "Splügen Bräu", "Achille and Pier Giacomo Castiglioni's pendant light for Flos.", "Flos", "1964", W + "Achille_Castiglioni", [], "")
a("Parentesi", "", "Castiglioni and Pio Manzù's light that slides on a tensioned cable from ceiling to floor; Compasso d'Oro 1979.", "Flos", "1970", W + "Achille_Castiglioni", [], "")
a("Frisbi", "", "Achille Castiglioni's suspension lamp for Flos.", "Flos", "1978", W + "Achille_Castiglioni", [], "")
a("Saliscendi", "Rise-and-fall pendant", "Castiglioni brothers' dual-light pendant whose source slides on pulleys to trade table light for room light.",
  "Stilnovo", "1957", "https://urbanlighting.com.au/collections/stilnovo/products/saliscendi-1957-achille-e-pier-giacomo-castiglioni",
  [("Milan Chamber of Commerce prototypes", "Stilnovo", "1958", "two unique copies"), ("LED reissue", "Stilnovo", "", "dimmable LED, grey-white, ruby red or green")],
  "Ø630 mm shade · drop 1000–2900 mm")
a("Billiard pendant", "Pool-table light · snooker light", "Long bar with several metal shades hung about 80 cm over a billiard or pool table.",
  "", "c. 1900", "https://edisonlightglobes.com.au/shop/fittings/billiard-table-lights/vintage-extra-long-billiard-table-light/", [],
  "length for 9 ft or 12 ft table · 3–4 shades · green dome, steel or enamel coolie shades")
a("Paper lantern shade", "China ball · chōchin", "East Asian collapsible lantern of thin paper on a bamboo or wire hoop frame, used as a cheap ceiling shade.",
  "", "Tang dynasty onwards", W + "Paper_lantern", [], "diameter · round or shaped · white or coloured paper")

kind = {"n": "Pendant light", "a": "pendant · suspension light · hanging light",
        "d": "Fitting hung from the ceiling on a cord, chain or rod, with the light source and shade below the ceiling.",
        "t": ["cord pendant", "chain pendant", "rod pendant", "multi-light cluster", "rise-and-fall", "plug-in (swag) pendant", "integrated LED"],
        "s": "https://www.lights.co.uk/c/indoor-lighting/pendant-lighting", "x": X,
        "m": [["LC Shutters", "Louis Poulsen"], ["Twiggy", "Foscarini"], ["Allegretto Ritmico", "Foscarini"], ["Gregg", "Foscarini"],
              ["Spokes", "Foscarini"], ["Aplomb", "Foscarini"], ["Silvia", "UMAGE"], ["Cross LED Pendant", "Resident"],
              ["IKEA PS 2014", "IKEA"], ["MELODI", "IKEA"], ["Newtown", "Eglo"], ["Elamira", "Lindby"], ["Daelor", "Lucande"],
              ["Conni", "Paul Neuhaus"], ["Albiona", "Arcchio"]],
        "r": [["HEKTAR", "IKEA"], ["NYMÅNE", "IKEA"], ["RANARP", "IKEA"], ["Anuva", "Lindby"], ["Branford", "Lindby"], ["Tamani", "Lucande"]]}

K = "knowledge"
brands = [
 {"n": "Louis Poulsen", "c": "Denmark", "f": "1874", "seg": "Design lighting", "d": "Copenhagen lighting maker best known for Poul Henningsen's PH lamps.",
  "lines": ["PH lamps"], "eras": ["Poul Henningsen, from 1925"], "sig": ["PH lamp", "VL45 Radiohus"], "sc": [], "rel": [], "s": W + "Louis_Poulsen"},
 {"n": "Flos", "c": "Italy", "f": "1962", "seg": "Design lighting", "d": "Italian design-lighting maker, long-time producer of the Castiglioni brothers' lamps.",
  "lines": [], "eras": [], "sig": ["Splüghen Braü", "Parentesi", "Frisbi"], "sc": [], "rel": [], "s": K},
 {"n": "Foscarini", "c": "Italy", "f": "1981", "seg": "Design lighting", "d": "Italian design-lighting maker founded on Murano.",
  "lines": [], "eras": [], "sig": ["Big Bang", "Caboche"], "sc": [], "rel": [], "s": K},
 {"n": "Ingo Maurer", "c": "Germany", "f": "1963", "seg": "Design lighting", "d": "Munich studio of lighting designer Ingo Maurer, founded as Design M.",
  "lines": [], "eras": ["Ingo Maurer, from 1963"], "sig": ["Porca Miseria!", "Zettel'z"], "sc": [], "rel": [], "s": W + "Ingo_Maurer"},
 {"n": "Moooi", "c": "Netherlands", "f": "2001", "seg": "Design furniture & lighting", "d": "Dutch design label founded by Marcel Wanders and Casper Vissers.",
  "lines": [], "eras": [], "sig": ["Random Light"], "sc": [], "rel": [], "s": W + "Moooi"},
 {"n": "Tom Dixon", "c": "United Kingdom", "f": "2002", "seg": "Design lighting & furniture", "d": "London design brand of designer Tom Dixon.",
  "lines": [], "eras": [], "sig": ["Beat light", "Mirror Ball"], "sc": [], "rel": [], "s": K},
 {"n": "Fritz Hansen", "c": "Denmark", "f": "1872", "seg": "Design furniture & lighting", "d": "Danish furniture maker that took over the Lightyears lighting label.",
  "lines": [], "eras": [], "sig": ["Caravaggio"], "sc": [], "rel": [], "s": K},
 {"n": "Stilnovo", "c": "Italy", "f": "1946", "seg": "Design lighting", "d": "Milan lighting maker of the post-war era, revived in the 21st century.",
  "lines": [], "eras": [], "sig": ["Saliscendi"], "sc": [], "rel": [], "s": K},
 {"n": "Ozeki & Co.", "c": "Japan", "f": "", "seg": "Paper lanterns", "d": "Gifu lantern maker that has hand-made Noguchi's Akari since 1951.",
  "lines": ["Akari"], "eras": [], "sig": ["Akari pendant"], "sc": [], "rel": [], "s": W + "Akari_(lamp)"},
 {"n": "Howard Miller Clock Company", "c": "United States", "f": "", "seg": "Clocks & lighting", "d": "Original maker of George Nelson's Bubble lamps.",
  "lines": [], "eras": [], "sig": ["Bubble lamp"], "sc": [], "rel": ["Herman Miller"], "s": W + "George_Nelson_(designer)"},
 {"n": "Herman Miller", "c": "United States", "f": "", "seg": "Design furniture", "d": "American furniture maker and current producer of the Nelson Bubble lamps.",
  "lines": [], "eras": [], "sig": ["Bubble lamp"], "sc": [], "rel": [], "s": K},
]
notes = ("Kept the single planned kind Pendant light (old k2). 19 archetypes ordered by significance: PH family (old PH models became versions, years from the "
 "Henningsen works table), VL45, Nelson Bubble, Flowerpot, Caravaggio, Akari, Random, Beat, Mirror Ball, Big Bang, Caboche, Porca Miseria!, Zettel'z, "
 "Castiglioni/Flos (Splüghen Braü, Parentesi, Frisbi), Saliscendi, billiard pendant, paper lantern shade. Dropped: about 30 IKEA SKUs (kept PS 2014, MELODI "
 "and three ranges), the 5 Studio Luminosa SKUs, KARE Scala Balls, Foscarini Chouchin/Pli/Rituals/Spokes 2/Troag (kept 5 Foscarini models), duplicate IKEA ranges, "
 "and ranges now covered by archetypes (PH lamps, Flos Castiglioni designs, Mirror Ball). Flowerpot has no current-maker version (&Tradition not on a retrieved page); "
 "Bubble lamp Vitra/HAY not confirmed, left out. VL45 original year left as the Radiohuset build span. Traditions: none added here (Gifu lantern tradition belongs "
 "with Lanterns & flame lamps / Paper lantern). Brands without f were not confirmed.")
out = {"kinds": [kind], "brands": brands, "traditions": [], "notes": notes}
p = 'work/B3/shelves/01_00.json'
open(p + '.tmp', 'w').write(json.dumps(out, ensure_ascii=False, indent=1))
os.replace(p + '.tmp', p)
print('ok')
