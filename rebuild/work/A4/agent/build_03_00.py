import json, os
W = "https://en.wikipedia.org/wiki/"
OLD = "https://www.cleverjourney.com/backpack-types/"
FJ = W + "Fjällräven"; JS = W + "JanSport"; OS = W + "Osprey_Packs"; RD = W + "Randoseru"
TU = W + "Tumi_Inc."; DE = W + "Deuter_Sport"; GR = W + "GORUCK"; PD = W + "Peak_Design"
AER3 = "https://www.carryology.com/reviews/bags/backpacks/aer-travel-pack-3-review/"
AER4 = "https://www.gearpatrol.com/?p=973774"; AERA = "https://www.aersf.com/about-us"
HOF19 = "https://www.carryology.com/projects/carry-awards/hall-of-fame-2019"
HOFX = "https://www.carryology.com/projects/carry-awards/hall-of-fame-carry-awards-x/"
POR = "https://heddels-newsletter.beehiiv.com/p/march-29-yoshida-porter"
HER = "https://www.footshop.eu/blog/herschels-signature-icon-little-america/"
MR = "https://www.mysteryranch.com/blog/post/humble-beginnings-the-gleasons-and-mystery-ranch"
HMG = "https://www.halfwayanywhere.com/reviews/hyperlite-mountain-gear-southwest-3400-review/"
HMGB = "https://dyneema.com/sectors/sports-and-consumer-products/enabling-ultra-light-hiking-gear-with-hyperlite"
SYN = "https://packhacker.com/travel-gear/tom-bihn/synik-30/"
AERO = "https://www.wardrobeoxygen.com/tom-bihn-aeronaut/"
FAR = "https://www.outdoorgearlab.com/reviews/travel/travel-backpack/osprey-farpoint-40"
GRG = "https://www.gearx.com/blog/brand-spotlight-gregory-packs"
PDE = "https://www.macworld.com/article/2199657/peak-design-everyday-backpack-review.html"
GR1T = "https://www.gearpatrol.com/outdoors/goruck-gr1-usa-throwback/"
GYM = "https://wordwebonline.com/en/GYMBAG"
INC = "https://madegooddesigns.com/incase-brand-guidelines/"


def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s,
            "v": [dict(zip(("n", "mk", "y", "d"), q)) for q in v], "dt": dt}


kinds = [
 {"n": "Daypack", "a": "rucksack · everyday backpack", "d": "General backpack sized for one day's personal items.",
  "t": ["top-loading", "panel-loading", "flap-top", "canvas", "nylon"], "s": OLD,
  "x": [
   X("Kånken", "Fjällräven's boxy rectangular daypack, made after a 1977 study of back problems among Swedish schoolchildren.", "Fjällräven", "1978", FJ,
     [("Mini-Kånken", "Fjällräven", "2002", "7-litre preschool size"), ("Kånken Laptop", "Fjällräven", "2006", "back laptop pocket"),
      ("Re-Kånken", "Fjällräven", "2016", "polyester from recycled bottles"), ("Tree-Kånken", "Fjällräven", "2021", "Pine Weave fabric")],
     dt="sizes · original or recycled fabric · colours"),
   X("JanSport Daypack", "JanSport's panel-loading campus daypack, first sold at the University of Washington bookstore.", "JanSport", "1975", JS,
     [("University Bookstore Rucksack", "JanSport", "1975", "original name"), ("SuperBreak", "JanSport", "", "successor to the daypack")],
     a="University Bookstore Rucksack", dt="colours · prints"),
   X("Little America", "Herschel's retro canvas-look backpack with two leather front straps on magnetic clips and a fleece laptop sleeve.", "Herschel Supply Co.", "", HER,
     [("Little America", "Herschel Supply Co.", "", "25 litres")], dt="sizes · colours · collaborations"),
   X("Tanker", "Porter's nylon bag series modelled on the MA-1 flight jacket, in sage green or black with a bright orange lining.", "Porter", "1983", POR,
     [], dt="three-layer nylon twill fabric · sage green, black · day pack, rucksack and other shapes"),
   X("3 Day Assault Pack", "Mystery Ranch's military assault pack with 3-Zip access, built to carry three days of gear.", "Mystery Ranch", "around 2000", HOFX,
     [], a="3DAP", dt="Cordura nylon · Futura harness · colours"),
  ]},
 {"n": "Carry-on travel backpack", "a": "one-bag travel pack · travel backpack", "d": "Backpack sized to airline cabin limits that opens like a suitcase.",
  "t": ["clamshell opening", "stowable harness", "hip belt"], "s": OLD,
  "x": [
   X("GR1", "GORUCK's founding clamshell rucksack inspired by military medical packs, hand-made in the USA in 1000D Cordura.", "GORUCK", "2008", HOF19,
     [("GR1 21L", "GORUCK", "", ""), ("GR1 26L", "GORUCK", "", ""), ("GR1 USA Throwback", "GORUCK", "2025", "limited archival reissue")],
     dt="21 or 26 L · 1000D Cordura, 1680D ballistic nylon · MOLLE webbing · colours"),
   X("Travel Pack", "Aer's clamshell carry-on backpack built to airline size limits, now in its fourth generation.", "Aer", "about 2016", AER4,
     [("Travel Pack 3", "Aer", "", "35 L; ballistic nylon, Cordura or X-Pac"), ("Travel Pack 4", "Aer", "", "28 or 35 L")],
     dt="28 or 35 L · 1680D ballistic nylon, 700D Cordura, VX42 X-Pac · colours"),
   X("Peak Design Travel Backpack", "Peak Design's expandable carry-on travel backpack, launched with packing tools on Kickstarter.", "Peak Design", "2018", PD,
     [], dt="capacity settings · colours"),
   X("Farpoint", "Osprey's front-opening travel pack with an internal frame and hip belt.", "Osprey", "", FAR,
     [("Farpoint 40", "Osprey", "", "40 L, recycled 450D polyester")], dt="capacities · colours"),
   X("Aeronaut 45", "Tom Bihn's carry-on duffel that converts to a backpack, made in Seattle.", "Tom Bihn", "", AERO,
     [], dt="fabric · colours · optional straps"),
   X("Synik", "Tom Bihn's travel and everyday backpack, the next iteration of the Synapse, handmade in the USA.", "Tom Bihn", "", SYN,
     [("Synapse", "Tom Bihn", "", "predecessor"), ("Synik 22", "Tom Bihn", "", "22 L"), ("Synik 30", "Tom Bihn", "", "30 L")],
     dt="525D ballistic nylon · 200D Halcyon lining · colours"),
  ]},
 {"n": "Laptop backpack", "a": "commuter backpack · tech backpack", "d": "Backpack built around a padded laptop compartment.",
  "t": ["laptop size", "USB pass-through", "trolley sleeve"], "s": OLD,
  "x": [
   X("Everyday Backpack", "Peak Design's camera and everyday backpack with a MagLatch flap and side access, launched on Kickstarter in 2016.", "Peak Design", "2016", PDE,
     [("Everyday Backpack 20L", "Peak Design", "", ""), ("Everyday Backpack 30L", "Peak Design", "", "")],
     dt="20 or 30 L · recycled 400D nylon · colours"),
   X("ICON", "Incase's flagship laptop backpack.", "Incase", "", INC, [], dt="sizes · colours"),
  ],
  "r": [["Alpha", "Tumi"], ["Alpha Bravo", "Tumi"]]},
 {"n": "Hiking backpack", "a": "backpacking pack · trekking pack", "d": "Backpack with a load-bearing harness and hip belt for walking on trails.",
  "t": ["internal frame", "external frame", "frameless", "roll-top", "capacity in litres"], "s": OLD,
  "x": [
   X("Cassin", "Gregory's expedition top-loader with contoured profile, ergonomic hip belt and adjustable suspension.", "Gregory", "1977", GRG, [], dt="sizes"),
   X("Baltoro", "Gregory's large-capacity backpacking pack, with the Deva as the women's version.", "Gregory", "", GRG,
     [("Deva", "Gregory", "", "women's version")], dt="capacities · torso sizes"),
   X("Aether", "Osprey's internal-frame backpacking pack.", "Osprey", "", OS,
     [("Aether 60", "Osprey", "2001", "on the cover of Time with Erik Weihenmayer")], dt="capacities · torso sizes"),
   X("Southwest", "Hyperlite Mountain Gear's roll-top ultralight pack in Dyneema composite with removable aluminium stays, made in Maine.", "Hyperlite Mountain Gear", "", HMG,
     [("Southwest 3400", "Hyperlite Mountain Gear", "", "55 L, Dyneema Hardline pockets"), ("Windrider", "Hyperlite Mountain Gear", "", "mesh outer pockets"),
      ("Junction", "Hyperlite Mountain Gear", "", "mesh front pocket only")], dt="capacities · white or black"),
  ]},
 {"n": "School backpack", "a": "school satchel · rigid school backpack", "d": "Backpack with a rigid box-shaped body and frame, padded back and reflective panels, made for a child to carry books.",
  "tg": ["baby"], "t": ["reflective panels", "chest and hip straps", "school set with pencil case"],
  "s": "https://www.carryology.com/bags/ignition-reports-randoseru-japanese-schoolbag/",
  "x": [
   X("Randoseru", "Japanese rigid leather or synthetic-leather school backpack given at school entry and used to grade 6.", "", "1880s", RD,
     [], a="ransel", dt="leather, cordovan or Clarino · colours"),
  ],
  "m": [["Genius", "Scout"], ["Alpha", "Scout"], ["Cloud", "Step by Step"], ["Space", "Step by Step"],
        ["ErgoFlex Easy", "DerDieDas"], ["School Set Boxy Unique", "Lässig"], ["EasyFit Glow", "Scooli"]]},
 {"n": "Drawstring bag", "a": "gym sack · gymsack · drawstring backpack", "d": "Light cloth sack closed with a drawstring that doubles as shoulder cords, for sports kit.",
  "t": ["cotton", "polyester", "mesh"], "s": GYM},
]

brands = [
 {"n": "Fjällräven", "c": "Sweden", "f": "1960", "seg": "outdoor", "d": "Örnsköldsvik outdoor brand founded by Åke Nordin.", "lines": ["Kånken"], "eras": [], "sig": ["Kånken"], "sc": [], "rel": [], "s": FJ},
 {"n": "JanSport", "c": "United States", "f": "1967", "seg": "daypacks", "d": "Seattle-founded backpack maker named after co-founder Jan Lewis, owned by VF Corporation.", "lines": ["SuperBreak"], "eras": [], "sig": ["JanSport Daypack"], "sc": [], "rel": [], "s": JS},
 {"n": "Herschel Supply Co.", "c": "Canada", "f": "2009", "seg": "lifestyle bags", "d": "Vancouver bag brand founded by brothers Jamie and Lyndon Cormack.", "lines": ["Little America", "Nova"], "eras": [], "sig": ["Little America"], "sc": [], "rel": [], "s": HER},
 {"n": "Porter", "c": "Japan", "f": "1962", "seg": "bags", "d": "Main brand of Tokyo bag maker Yoshida & Co., named after hotel porters.", "lines": ["Tanker", "Porter Girl", "Head Porter"], "eras": ["Kichizo Yoshida, founder (atelier 1935)"], "sig": ["Tanker"], "sc": [], "rel": ["Head Porter"], "s": POR},
 {"n": "Mystery Ranch", "c": "United States", "f": "2000", "seg": "technical packs", "d": "Montana pack maker run by Dana and Renee Gleason, successor to Kletterwerks and Dana Design.", "lines": ["Sphinx", "Mystic"], "eras": ["Dana Gleason"], "sig": ["3 Day Assault Pack"], "sc": ["military"], "rel": [], "s": MR},
 {"n": "GORUCK", "c": "United States", "f": "2008", "seg": "rucking packs", "d": "Florida rucksack and events company founded by former Green Beret Jason McCarthy.", "lines": [], "eras": [], "sig": ["GR1"], "sc": ["one-bag", "rucking"], "rel": [], "s": GR},
 {"n": "Aer", "c": "United States", "f": "2014", "seg": "travel and everyday bags", "d": "San Francisco bag brand that began with one bag for the gym and the office.", "lines": ["Travel Pack", "Duffel Pack"], "eras": [], "sig": ["Travel Pack"], "sc": ["one-bag"], "rel": [], "s": AERA},
 {"n": "Peak Design", "c": "United States", "f": "2010", "seg": "camera and travel bags", "d": "San Francisco design company founded by Peter Dering, funded through Kickstarter campaigns.", "lines": ["Everyday", "Travel"], "eras": [], "sig": ["Everyday Backpack", "Peak Design Travel Backpack"], "sc": ["one-bag", "photography"], "rel": [], "s": PD},
 {"n": "Tom Bihn", "c": "United States", "f": "", "seg": "travel and laptop bags", "d": "Seattle maker of travel and laptop bags, made in the USA.", "lines": ["Synik", "Aeronaut"], "eras": [], "sig": ["Synik", "Aeronaut 45"], "sc": ["one-bag"], "rel": [], "s": SYN},
 {"n": "Osprey", "c": "United States", "f": "1974", "seg": "outdoor packs", "d": "Pack maker founded by Mike Pfotenhauer in Santa Cruz, now based in Cortez, Colorado.", "lines": ["Aether", "Farpoint", "UNLTD"], "eras": [], "sig": ["Aether", "Farpoint"], "sc": [], "rel": [], "s": OS},
 {"n": "Gregory", "c": "United States", "f": "1977", "seg": "outdoor packs", "d": "San Diego pack maker founded by Wayne Gregory.", "lines": ["Baltoro", "Deva", "Z", "J"], "eras": ["Wayne Gregory"], "sig": ["Cassin", "Baltoro"], "sc": [], "rel": [], "s": GRG},
 {"n": "Deuter", "c": "Germany", "f": "1898", "seg": "outdoor packs", "d": "Augsburg-founded pack maker, now based in Gersthofen.", "lines": [], "eras": ["Hans Deuter, founder"], "sig": [], "sc": [], "rel": [], "s": DE},
 {"n": "Hyperlite Mountain Gear", "c": "United States", "f": "", "seg": "ultralight packs", "d": "Maine maker of ultralight packs and shelters in Dyneema fabrics, founded by Mike St. Pierre.", "lines": ["Southwest", "Windrider", "Junction"], "eras": [], "sig": ["Southwest"], "sc": ["ultralight hiking"], "rel": [], "s": HMGB},
 {"n": "Tumi", "c": "United States", "f": "1975", "seg": "premium luggage", "d": "New Jersey luggage and bag maker founded by Charlie Clifford, owned by Samsonite since 2016.", "lines": ["Alpha", "Alpha Bravo", "Arrivé", "Harrison", "Voyageur", "19 Degree"], "eras": [], "sig": [], "sc": [], "rel": ["Samsonite"], "s": TU},
 {"n": "Incase", "c": "United States", "f": "1997", "seg": "tech bags", "d": "California maker of cases, sleeves and backpacks for Apple hardware.", "lines": ["ICON", "A.R.C."], "eras": [], "sig": ["ICON"], "sc": [], "rel": [], "s": INC},
]

traditions = [
 {"n": "Randoseru", "g": "Leather & bags", "r": "Japan", "p": "1880s–present", "d": "Rigid school backpack derived from the Dutch military ransel, standard for Japanese elementary pupils since Gakushūin adopted it.",
  "tech": "stitched firm leather over a stiff box body", "mat": "leather, cordovan, Clarino synthetic leather", "forms": ["Randoseru"],
  "ctr": ["Gakushūin (1885 adoption)", "department stores and traditional workshops"], "auth": "workshop or department-store make, genuine leather or cordovan versus Clarino; price bands from about ¥30,000 to over ¥100,000", "s": RD},
]

notes = ("Tumi ranges kept once here as r (Alpha, Alpha Bravo) with full line list in the Tumi brand entry; Arrivé, Harrison, Voyageur dropped from this kind (not backpack-specific). "
         "School backpack trimmed from 17 to 7 models (2 per main German brand plus Lässig, Scooli) and randoseru made an archetype plus a tradition. "
         "Left out (no retrieved page confirming the model): Peak Design Everyday/Travel version years beyond Kickstarter, Osprey Atmos/Exos, Deuter Aircontact/Futura, JanSport Right Pack, Herschel launch year, Tom Bihn founding year (sources give 1972 and 1982). "
         "Mystery Ranch 3DAP placed in Daypack; Porter Tanker placed in Daypack as a series.")
out = {"kinds": kinds, "brands": brands, "traditions": traditions, "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/A4/shelves/03_00.json"
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1)
os.replace(p + ".tmp", p)
print("written", sum(len(k.get("x", [])) for k in kinds), "archetypes")
