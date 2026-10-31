import json, os
W = 'https://en.wikipedia.org/wiki/'
OLD = 'https://besttravelumbrella.com/types-of-umbrellas/'
def V(n, mk='', y='', d=''): return {"n": n, "mk": mk, "y": y, "d": d}

stick = {"n": "Stick umbrella", "a": "walking-length umbrella · long umbrella · gentleman's umbrella",
 "d": "Umbrella with a fixed full-length shaft that does not collapse, usually ending in a crook or straight handle.",
 "t": ["crook handle", "straight handle", "bubble (dome canopy)", "inverted (reverse-closing)", "whole-stick (solid stick)", "manual", "auto-open", "storm (wind-rated)"],
 "s": OLD,
 "x": [
  {"n": "Paragon frame umbrella", "a": "steel-ribbed umbrella",
   "d": "Umbrella built on Samuel Fox's Paragon frame of U-section steel ribs, the pattern that replaced whalebone frames.",
   "mk": "Samuel Fox", "y": "1851", "s": W + "Samuel_Fox_(industrialist)",
   "v": [V("Paragon frame", "Samuel Fox", "1851", "Fox Umbrella Frames Ltd; Wikipedia's Umbrella article dates the steel-ribbed umbrella to 1852"),
         V("Paragon trademark adopted by William Henry Fox", "Fox Umbrellas", "c. 1913", "per Fox Umbrellas company history")],
   "dt": "U-section steel ribs · frame sizes standardised 18–26 in (1934)"},
  {"n": "Solid-stick umbrella", "a": "whole-stick umbrella · one-piece umbrella",
   "d": "Stick umbrella whose shaft and handle are shaped from a single piece of wood.",
   "mk": "", "y": "", "s": "https://www.gentlemansgazette.com/francesco-maglia/",
   "v": [V("Solid stick", "Francesco Maglia", "", "a house trademark; handle steam-shaped, brass crown milled in-house")],
   "dt": "wood species · handle shape · canopy fabric · ferrule"},
  {"n": "Brigg whangee umbrella", "a": "John Steed umbrella",
   "d": "Brigg gentleman's umbrella with a whangee bamboo handle, made famous by John Steed in The Avengers.",
   "mk": "Swaine Adeney Brigg", "y": "1962", "s": "https://swaine.london/pages/origins-of-brigg",
   "v": [V("The Avengers sword umbrella", "Swaine Adeney Brigg", "1962", "custom whangee umbrella with a sword hidden in the shaft"),
         V("John Steed umbrella", "Fox Umbrellas", "", "Fox Umbrellas also lists the Steed umbrella among its screen commissions")],
   "dt": "whangee handle · black canopy · Fox frame"},
  {"n": "Brigg Centenary", "a": "",
   "d": "Ultra-slim Brigg gentleman's umbrella introduced to mark the company's centenary.",
   "mk": "Swaine Adeney Brigg", "y": "", "s": "https://swaine.london/pages/origins-of-brigg",
   "v": [], "dt": "slim furled profile · handle wood"},
  {"n": "Birdcage", "a": "bubble umbrella · dome umbrella",
   "d": "Fulton's deep transparent PVC dome umbrella, carried by Queen Elizabeth II in colours matching her outfits.",
   "mk": "Fulton", "y": "1967", "s": "https://www.fultonumbrellas.com/about-us",
   "v": [V("Birdcage", "Fulton", "1967", "PVC dome")],
   "dt": "clear PVC canopy · trim colour · prints"},
  {"n": "Senz storm umbrella", "a": "senz° original",
   "d": "Asymmetric aerodynamic umbrella that aligns itself with the wind instead of turning inside out.",
   "mk": "Senz", "y": "2006", "s": "https://www.senz.com/about-us/",
   "v": [V("senz° original storm umbrella", "Senz", "2006", "rated to about 100 km/h"),
         V("Senz under licence", "Totes", "", "sold by Totes in the US (Wikipedia, Umbrella)")],
   "dt": "long and foldable versions · canopy colours"},
  {"n": "KAZbrella", "a": "inside-out umbrella · reverse umbrella",
   "d": "Inverted umbrella whose canopy closes downward so the dry inner face ends up outside.",
   "mk": "Jenan Kazim", "y": "2010", "s": "https://www.core77.com/posts/36546/Making-a-Drip-Free-Car-Friendly-Umbrella",
   "v": [V("Pulley-and-string patent", "Jenan Kazim", "2010", "concept begun 2000")],
   "dt": "double canopy · colours"},
  {"n": "Blunt Classic", "a": "",
   "d": "Stick umbrella with Blunt's radial tensioning system and rounded canopy tips instead of sharp points.",
   "mk": "Blunt", "y": "2017", "s": "https://good-design.org/projects/blunt-classic-umbrella",
   "v": [V("Classic", "Blunt", "2017", "year of Good Design listing; designer Greig Brebner")],
   "dt": "replaceable canopy · telescopic fibreglass ribs · polycarbonate struts"}],
 "m": [["Silver Lion Umbrella", "Pasotti"], ["Red Dahlia Umbrella", "Pasotti"], ["Savile", "Davek"]]}

fold = {"n": "Folding umbrella", "a": "compact umbrella · pocket umbrella · telescopic umbrella",
 "d": "Umbrella whose shaft and ribs collapse to a short length for carrying in a bag or pocket.",
 "t": ["manual", "auto-open", "auto open-close", "flat / mini", "telescopic", "trekking"],
 "s": OLD,
 "x": [
  {"n": "Knirps", "a": "pocket umbrella",
   "d": "Hans Haupt's shortenable pocket umbrella, the originator of the folding umbrella; its name is generic in German.",
   "mk": "Knirps", "y": "1928", "s": "https://knirps.com/company/",
   "v": [V("Shortenable umbrella patent DE 606015", "Knirps", "1930", "filed 1930, granted 1934; regarded as the birth of the Knirps (DPMA)"),
         V("First Knirps for women", "Knirps", "1932", "series production by Bremshey & Co, Solingen"),
         V("First Knirps for men", "Knirps", "1938", ""),
         V("Duomatic", "Knirps", "1965", "first Knirps automatic mechanism"),
         V("X1", "Knirps", "2003–04", "smallest Knirps"),
         V("Fiber T2", "Knirps", "2006", ""),
         V("T.series", "Knirps", "2016", "redesign")],
   "dt": "manual or Duomatic · size · canopy colour"},
  {"n": "Flirt", "a": "",
   "d": "Slawa Horowitz's Viennese compact folding umbrella, patented in 1929.",
   "mk": "Slawa Horowitz", "y": "1929", "s": W + "Umbrella",
   "v": [V("Prototype", "Slawa Horowitz", "1928", "patent 19 September 1929")], "dt": ""},
  {"n": "Totes folding umbrella", "a": "",
   "d": "Bradford Phillips's mass-market collapsible umbrella that made Totes the largest supplier of folding umbrellas.",
   "mk": "Totes", "y": "1970", "s": W + "Totes_Isotoner",
   "v": [V("Henryson patent", "Totes", "1968", "folding-umbrella patent bought with L.P. Henryson & Co.")],
   "dt": "auto-open · canopy colours"}],
 "m": [["Microlite", "Fulton"], ["Tiny", "Fulton"], ["Aerolite", "Fulton"], ["Solo", "Davek"], ["Mini", "Davek"], ["Elite", "Davek"]]}

golf = {"n": "Golf umbrella", "a": "",
 "d": "Large stick umbrella with a canopy about 150–180 cm across, sized to cover a player and bag.",
 "t": ["single canopy", "vented double canopy", "fibreglass frame"],
 "s": OLD,
 "m": [["Cyclone", "Fulton"], ["Golf Convertible", "Fulton"], ["Golf", "Davek"]]}

para = {"n": "Parasol", "a": "sunshade · sun umbrella",
 "d": "Hand-held umbrella that shades the carrier from the sun, with a lace, paper, silk or sun-blocking canopy.",
 "t": ["lace", "paper", "silk", "UV-blocking", "en-tout-cas (sun and rain)"],
 "s": "https://www.kohls.com/product/prd-8653640/lace-embroidery-sun-parasol-folding-wedding-umbrella.jsp",
 "x": [
  {"n": "Oil-paper umbrella", "a": "yóuzhǐsǎn · 油紙傘",
   "d": "Chinese umbrella of bamboo ribs and paper waterproofed with tung oil, often painted.",
   "mk": "", "y": "Song–Ming dynasties", "s": W + "Oil-paper_umbrella",
   "v": [V("Yuhang", "", "Qianlong era", "painted petal umbrellas"),
         V("Luzhou", "", "", "about 400 years; wind-resistant"),
         V("Meinong", "", "", "Hakka tradition, Taiwan; moso bamboo"),
         V("Bo Sang", "", "", "Chiang Mai, Thailand; village tradition")],
   "dt": "bamboo ribs · paper · tung oil · painted motifs · ceremonial colours"},
  {"n": "Wagasa", "a": "和傘 · Japanese umbrella",
   "d": "Japanese bamboo-and-washi oil-paper umbrella, developed from the Chinese form.",
   "mk": "", "y": "Muromachi period onward", "s": W + "Wagasa",
   "v": [V("Janome-gasa", "", "", "snake-eye bull's-eye pattern"),
         V("Kyō-wagasa", "", "", "fully handmade Kyoto style"),
         V("Gifu wagasa", "", "", "over a hundred procedures")],
   "dt": "bamboo ribs · washi · oil · painted designs"},
  {"n": "Pathein hti", "a": "Pathein umbrella",
   "d": "Hand-made Burmese umbrella of bamboo and oiled cotton or silk from Pathein.",
   "mk": "", "y": "late 19th century", "s": W + "Pathein_hti",
   "v": [V("Monk's umbrella", "", "", "saffron"), V("Beauty umbrella", "", "", "colourful, painted")],
   "dt": "Taragu bamboo ribs · oiled cotton or silk · Tasae dye · painted"}],
 "m": [["Parasoleil", "Fulton"], ["Parasol", "Davek"]]}

def B(n, c, f, seg, d, s, lines=(), eras=(), sig=(), rel=()):
    return {"n": n, "c": c, "f": f, "seg": seg, "d": d, "lines": list(lines), "eras": list(eras), "sig": list(sig), "sc": [], "rel": list(rel), "s": s}
brands = [
 B("Swaine Adeney Brigg", "United Kingdom", "1798", "Heritage umbrellas & leather", "London leather, whip and umbrella house; Thomas Brigg & Sons umbrellas merged in 1943; renamed Swaine London in 2022.", W + "Swaine_Adeney_Brigg",
   lines=["Brigg umbrellas", "Herbert Johnson hats"], eras=["Swaine Adeney family, to 1990", "Chargeurs, from the 2020s"], sig=["Brigg whangee umbrella", "Brigg Centenary"], rel=["Fox Umbrellas", "James Smith & Sons"]),
 B("Fox Umbrellas", "United Kingdom", "1868", "Heritage umbrellas", "London umbrella maker descended from Thomas Fox's City shop; factory in Shirley, Croydon.", "https://www.foxumbrellas.com/pages/fox-umbrellas-ltd",
   lines=["Classic Telescopics", "Animal Heads"], sig=["Paragon frame umbrella"], rel=["Swaine Adeney Brigg", "James Smith & Sons"]),
 B("James Smith & Sons", "United Kingdom", "1830", "Heritage umbrella shop", "London umbrella shop on New Oxford Street with Victorian fittings from about 1865.", W + "James_Smith_%26_Sons",
   rel=["Fox Umbrellas", "Swaine Adeney Brigg"]),
 B("Fulton", "United Kingdom", "1956", "Mainstream umbrellas", "London umbrella maker founded by Arnold Fulton in Whitechapel; royal warrant holder.", "https://www.fultonumbrellas.com/about-us",
   lines=["Birdcage", "Microlite", "Tiny", "Cyclone", "Parasoleil", "Aerolite"], sig=["Birdcage"], rel=["Totes", "Knirps"]),
 B("Pasotti", "Italy", "1956", "Luxury umbrellas", "Castellucchio maker of hand-made umbrellas with sculpted handles, also canes and shoehorns.", "https://www.ice.it/en/my-home/find-your-italian-partner/company-details/34199/PASOTTI",
   rel=["Francesco Maglia"]),
 B("Francesco Maglia", "Italy", "1854", "Luxury umbrellas", "Milan family umbrella maker known for solid-stick umbrellas made in about 70 steps.", "https://www.gentlemansgazette.com/francesco-maglia/",
   sig=["Solid-stick umbrella"], rel=["Pasotti"]),
 B("Knirps", "Germany", "1928", "Folding umbrellas", "Hans Haupt's pocket-umbrella brand, made by Bremshey of Solingen; passed to an Austrian company in 2005.", "https://knirps.com/company/",
   lines=["T.series", "X1", "Fiber"], sig=["Knirps"], rel=["Totes", "Fulton"]),
 B("Totes", "United States", "1924", "Mainstream umbrellas", "Cincinnati company (Totes Isotoner) that grew into the largest supplier of folding umbrellas.", W + "Totes_Isotoner",
   sig=["Totes folding umbrella"], rel=["Knirps", "Senz"]),
 B("Senz", "Netherlands", "2006", "Storm umbrellas", "Delft-born maker of asymmetric storm umbrellas rated to about 100 km/h.", "https://www.senz.com/about-us/",
   sig=["Senz storm umbrella"], rel=["Blunt", "Davek"]),
 B("Blunt", "New Zealand", "", "Storm umbrellas", "Umbrella brand built on Greig Brebner's radial tensioning system and blunt canopy tips.", "https://good-design.org/projects/blunt-classic-umbrella",
   sig=["Blunt Classic"], rel=["Senz", "Davek"]),
 B("Davek", "United States", "2005", "Premium umbrellas", "New York umbrella maker selling its range with an unconditional Forever Guarantee.", "https://davekny.com/pages/press-release",
   lines=["Solo", "Commuter", "Duet", "Mini", "Elite", "Golf", "Savile", "Parasol"], rel=["Blunt", "Senz"]),
]

def T(n, r, p, d, tech, mat, forms, ctr, auth, s):
    return {"n": n, "g": "Paper & bamboo crafts", "r": r, "p": p, "d": d, "tech": tech, "mat": mat, "forms": forms, "ctr": ctr, "auth": auth, "s": s}
trads = [
 T("Chinese oil-paper umbrella", "China, Taiwan, Thailand", "Tang dynasty onward; common by the Ming", "Bamboo-framed paper umbrellas waterproofed with tung oil and painted.",
   "bamboo frame tied with string; paper glued, trimmed, oiled and sun-dried; painted", "bamboo, paper, tung oil, persimmon juice",
   ["Parasol", "Oil-paper umbrella"], ["Yuhang", "Luzhou", "Meinong (Taiwan)", "Fuzhou", "Bo Sang (Thailand)"], "hand-tied bamboo frame, oiled paper canopy, hand painting", W + "Oil-paper_umbrella"),
 T("Wagasa", "Japan", "Muromachi period onward; peak in the Shōwa period", "Japanese bamboo-and-washi umbrellas developed from the Chinese oil-paper umbrella.",
   "over a hundred hand procedures in Gifu; oiled and painted paper", "bamboo, washi, sesame oil (Kyoto)",
   ["Parasol", "Wagasa", "Janome-gasa"], ["Gifu", "Kyoto", "Yodoe (Tottori)", "Nagano (Ajima-kasa)"], "hand-made bamboo ribs and washi canopy", W + "Wagasa"),
 T("Pathein umbrella", "Pathein, Ayeyarwady Region, Myanmar", "late 19th century onward; in Pathein from 1914", "Hand-made Burmese umbrellas descended from royal craftsmen of King Thibaw's court.",
   "entirely by hand: frame, canopy binding, Tasae dyeing, oiling, painting, polishing", "Taragu bamboo, Ma U Shwe War wood, oiled cotton or silk",
   ["Parasol", "Pathein hti"], ["Pathein", "U Shwe Sar"], "aged Taragu bamboo ribs, hand-painted oiled cotton", W + "Pathein_hti"),
]

notes = ("All 6 old kinds kept: Bubble and Inverted merged into Stick umbrella as types (Fulton Birdcage and KAZbrella added as their named archetypes). "
 "Left out: EuroSCHIRM (no fetched page; only retailer snippets), Swaine Adeney Brigg launch year of the Centenary (snippet only), Blunt founding and launch years (sources conflict; 2017 is the Good Design listing year), "
 "Francesco Maglia Milan move dates (Permanent Style blocked). Steed umbrella claimed by both Brigg and Fox; both recorded. Knirps parasols/garden umbrellas not added (garden furniture). "
 "Paragon frame year 1851 per Samuel Fox article (Umbrella article says 1852).")
out = {"kinds": [stick, fold, golf, para], "brands": brands, "traditions": trads, "notes": notes}
p = 'work/A4/shelves/06_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print('written')
