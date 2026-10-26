import json, os
NW = "https://www.niwaki.com/secateurs/"
FH = "https://america.felco.com/pages/company-history"
FW = "https://world.felco.com/"
PS = "https://en.wikipedia.org/wiki/Pruning_shears"
LOWE = "https://wtsh.de/en/looking-back-on-100-years-with-pride"

secateurs = {
 "n": "Secateurs", "a": "pruning shears · pruners · hand pruners",
 "d": "One-handed scissor-action pruning shears for stems and small branches, manual or powered.",
 "t": ["bypass", "anvil", "ratchet", "parrot-beak", "powered", "left-handed"],
 "s": "https://www.hornbach.de/c/garten/gartenwerkzeug-gartengeraete/S1943/",
 "x": [
  {"n": "Felco 2", "a": "FELCO 2", "d": "Swiss bypass secateur with forged aluminium handles and an adjustable cutting head; the reference professional pruner.",
   "mk": "Felco", "y": "1948", "s": FH,
   "v": [{"n": "Felco 6", "mk": "Felco", "y": "", "d": "size M version"},
         {"n": "Felco 8", "mk": "Felco", "y": "", "d": "size L version"},
         {"n": "Felco 9", "mk": "Felco", "y": "", "d": "left-handed model"},
         {"n": "Felco 6 Elite / Felco 8 Elite", "mk": "Felco", "y": "", "d": "Elite professional versions"},
         {"n": "Felco 2 80th Anniversary Special Edition", "mk": "Felco", "y": "", "d": "special edition"},
         {"n": "Felco 2e", "mk": "Felco", "y": "2026", "d": "battery-powered successor, cuts to 27 mm"}],
   "dt": "size S · M · L · right- or left-handed · rotating handle · colour editions"},
  {"n": "Original LÖWE anvil secateur", "a": "LÖWE 1 · Rolcut", "d": "The first anvil pruner: a drawing blade cuts against a fixed anvil, with every part replaceable.",
   "mk": "Original LÖWE", "y": "1923", "s": LOWE,
   "v": [{"n": "Original LÖWE 1", "mk": "Original LÖWE", "y": "1923", "d": "first model, still made"},
         {"n": "Rolcut", "mk": "Rolcut", "y": "1928", "d": "British licence brand set up by Col. B. J. Walker; made in England from 1945"},
         {"n": "Anvil Comfort Plus", "mk": "Wolf-Garten", "y": "", "d": "anvil interpretation"},
         {"n": "RS5000 Professional Anvil", "mk": "Wolf-Garten", "y": "", "d": "anvil interpretation"},
         {"n": "PG25 Anvil", "mk": "STIHL", "y": "", "d": "anvil interpretation"}],
   "dt": "anvil · straight or angled head · cut capacity"},
  {"n": "Okatsune 103", "a": "Okatsune No. 103", "d": "Japanese bypass secateur in carbon steel with a direct, ungeared action, riveted at the shoulder.",
   "mk": "Okatsune", "y": "", "s": "https://www.niwaki.com/okatsune-secateurs/",
   "v": [{"n": "No. 101", "mk": "Okatsune", "y": "", "d": "small size"},
         {"n": "No. 103", "mk": "Okatsune", "y": "", "d": "standard size"},
         {"n": "No. 104B", "mk": "Okatsune", "y": "", "d": "large size, longer handles"}],
   "dt": "Hitachi carbon steel · vinyl grips · three sizes"},
  {"n": "Tobisho SR-1", "a": "Tobisho x Niwaki SR-1", "d": "Hand-forged Japanese bypass secateur in high-carbon steel, light and finely balanced.",
   "mk": "Tobisho", "y": "", "s": "https://www.niwaki.com/tobisho-sr-1-secateurs/",
   "v": [{"n": "SR-1 small right-handed", "mk": "Tobisho", "y": "", "d": ""},
         {"n": "SR-1 left-handed", "mk": "Tobisho", "y": "", "d": ""},
         {"n": "Tobisho x Niwaki SR-1", "mk": "Tobisho", "y": "", "d": "collaboration version"}],
   "dt": "S-58C carbon steel · vinyl grips · max cut about 15 mm"},
  {"n": "Tobisho Hiryu", "a": "Hiryu", "d": "Hand-forged secateur with a thin hollow-ground blade and double spring, made for repetitive orchard pruning.",
   "mk": "Tobisho", "y": "", "s": "https://www.niwaki.com/tobisho-hiryu-secateurs/",
   "v": [], "dt": "YCS-3 steel · double spring · 19 cm"},
  {"n": "Niwaki GR Pro", "a": "GR secateurs", "d": "Japanese bypass secateur in S58C carbon steel, hand-finished in Yamagata; Niwaki's best-selling pruner.",
   "mk": "Niwaki", "y": "", "s": "https://www.niwaki.com/gr-pro-secateurs/",
   "v": [{"n": "GR Pro Small / Large / Left-handed", "mk": "Niwaki", "y": "", "d": "sizes and handedness"},
         {"n": "GR Pro S-Type", "mk": "Niwaki", "y": "", "d": ""},
         {"n": "GR Pro Lightweight", "mk": "Niwaki", "y": "", "d": ""},
         {"n": "Higurashi GR", "mk": "Niwaki", "y": "", "d": ""}],
   "dt": "S58C carbon steel · vinyl grips · small, standard, large"},
  {"n": "ARS VS-8", "a": "ARS VS-8Z", "d": "Japanese bypass pruning shear with a replaceable high-carbon steel blade and rubber-coated handles.",
   "mk": "ARS Corporation", "y": "", "s": "https://www.skyman.cz/en/p/ars-profi-vs-8z-bypass-pruning-shears",
   "v": [{"n": "VS-8Z", "mk": "ARS Corporation", "y": "", "d": "200 mm, 22 mm cut"}],
   "dt": "200 mm · carbon steel · cut 22 mm"},
  {"n": "Darlac Compound Action Pruner", "a": "DP332", "d": "Bypass pruner with a lever (compound) action that adds cutting force for tough stems.",
   "mk": "Darlac", "y": "", "s": "https://www.charlies.co.uk/darlac-dp332-compound-action-pruner",
   "v": [{"n": "DP332", "mk": "Darlac", "y": "", "d": "170 mm, cut 20 mm"}],
   "dt": "coated high-carbon steel blade · TPR grips"},
  {"n": "Ratchet pruner", "a": "ratchet anvil pruner", "d": "Pruner whose ratchet closes the blade in stages, multiplying force for stems over about 2 cm.",
   "mk": "", "y": "", "s": PS,
   "v": [{"n": "Super Classic Ratchet", "mk": "Darlac", "y": "", "d": ""},
         {"n": "Ratchet Pruner", "mk": "Burgon & Ball", "y": "", "d": ""},
         {"n": "Ratchet Anvil Pruner", "mk": "Ames", "y": "", "d": ""},
         {"n": "Ratchet Pruning", "mk": "Bulldog", "y": "", "d": ""},
         {"n": "Ratchet", "mk": "Jardin de France", "y": "", "d": ""}],
   "dt": "anvil or bypass head · cut capacity"}
 ],
 "m": [["AssistCut", "Gardena"], ["ExpertCut", "Gardena"], ["SmartCut Comfort", "Gardena"], ["Alu Garden Secateurs B/L", "Gardena"],
       ["Eversharp Bypass", "Kent & Stowe"], ["Eversharp All Purpose Lite", "Kent & Stowe"],
       ["Left Handed Bypass", "Burgon & Ball"], ["Expert DP1030A", "Darlac"],
       ["Razorsharp PRO Heavy Duty", "Spear & Jackson"], ["Felco Model 32", "Felco"],
       ["Mainichi Secateurs", "Niwaki"], ["Sentei Secateurs", "Niwaki"], ["Pro Secateurs", "Niwaki"],
       ["Daikiba Secateurs", "Niwaki"], ["Kurumi Secateurs", "Niwaki"], ["Yamakawa Secateurs", "Niwaki"], ["Joppari Secateurs", "Niwaki"],
       ["A-Type", "Tobisho"], ["B-Type", "Tobisho"],
       ["EasyPrune", "Bosch"]]
}
# Makita DUP181Z kept as powered model -> 21 would exceed; put powered in m by replacing Joppari
secateurs["m"][16] = ["DUP181Z", "Makita"]

snips = {
 "n": "Garden snips", "a": "flower snips · hasami · harvest snips",
 "d": "Scissor-form shears with finger loops and short straight blades for flowers, herbs and soft green growth.",
 "s": "https://www.gardena.com/int/products/tree-shrub-care/secateurs",
 "x": [
  {"n": "Okatsune snips", "a": "Niwaki garden snips", "d": "Japanese carbon-steel snips with 45 mm blades for flowers, fruit and vegetables, not woody growth.",
   "mk": "Okatsune", "y": "", "s": "https://www.architecturalplants.com/product/okatsunesnips/", "v": [],
   "dt": "Hitachi carbon steel · 45 mm blades · 115 g"},
  {"n": "Tobisho Barracuda Snips", "a": "Barracuda", "d": "Slender snip blade combined with the heft of a bypass secateur, for precise light pruning.",
   "mk": "Tobisho", "y": "", "s": "https://www.niwaki.com/tobisho-barracuda-snips", "v": [],
   "dt": "S-58C steel · 2 in blade · max cut about 8 mm"}
 ],
 "m": [["VeggieCut Scissors", "Gardena"], ["FreshCut Scissors", "Gardena"], ["HerbCut", "Gardena"], ["GripCut Scissors", "Gardena"], ["MultiCut Scissors", "Gardena"]]
}

knife = {
 "n": "Pruning knife", "a": "garden knife · grafting knife · budding knife",
 "d": "Fixed or folding knife with a curved or straight blade made to cut stems, prune and graft plants.",
 "t": ["pruning (hawkbill)", "grafting", "budding", "fixed", "folding", "left-handed"],
 "s": "https://www.hornbach.de/c/garten/gartenwerkzeug-gartengeraete/S1943/",
 "x": [
  {"n": "Opinel No. 8 Pruning Knife", "a": "Opinel serpette", "d": "Folding hawkbill blade on a curved wooden handle for trimming shrubs and vines.",
   "mk": "Opinel", "y": "", "s": "https://en.wikipedia.org/wiki/Opinel_knife",
   "v": [{"n": "No. 10 Pruning Knife", "mk": "Opinel", "y": "", "d": "larger size"}],
   "dt": "hawkbill blade · wooden handle · No. 8 or No. 10"},
  {"n": "Opinel No. 8 Garden Knife", "a": "Couteau du Jardin", "d": "Folding drop-point Opinel with a slim tapered wooden handle, sold for garden use.",
   "mk": "Opinel", "y": "", "s": "https://en.wikipedia.org/wiki/Opinel_knife", "v": [],
   "dt": "8.5 cm drop-point blade · wooden handle"},
  {"n": "Victorinox Pruning Knife XS", "a": "3.9060", "d": "Swiss folding pruning knife with a curved 51 mm stainless blade for branches and saplings.",
   "mk": "Victorinox", "y": "", "s": "https://www.victorinox.com/Products/Swiss-Army-Knife%E2%84%A2-and-Tools/Gardening/Pruning-Knife/p/3.9060",
   "v": [{"n": "3.9060", "mk": "Victorinox", "y": "", "d": "red nylon handle"}],
   "dt": "curved blade 51 mm · 100 mm handle · non-locking"},
  {"n": "Tina 605 grafting knife", "a": "Tina 605", "d": "Hand-made German folding grafting knife with a 5.5 cm blade and walnut handle.",
   "mk": "Tina", "y": "", "s": "https://sneeboer.com/en-gb/hand-forged-garden-tools/tina-messen-handmade-in-germany-since-1854", "v": [],
   "dt": "5.5 cm or 10.5 cm blade · walnut handle"}
 ]
}

brands = [
 {"n": "Felco", "c": "Switzerland", "f": "1945", "seg": "Professional secateurs", "d": "Swiss maker of bypass secateurs founded by Félix Flisch in Les Geneveys-sur-Coffrane.",
  "lines": ["Elite", "Premium SE", "Power Blade (electric)"], "eras": ["Félix Flisch, founder, 1945"], "sig": ["Felco 2"], "sc": [], "rel": ["Original LÖWE"], "s": FH},
 {"n": "Original LÖWE", "c": "Germany", "f": "1923", "seg": "Anvil secateurs", "d": "Brand of Gebrüder Schröder GmbH, Flintbek (formerly Kiel), whose Walther Schröder invented the anvil pruner in 1923.",
  "lines": [], "eras": ["Walther Schröder, 1923", "Randolph Schröder, third generation"], "sig": ["Original LÖWE anvil secateur"], "sc": [], "rel": ["Rolcut"], "s": LOWE},
 {"n": "Okatsune", "c": "Japan", "f": "", "seg": "Japanese secateurs", "d": "Japanese maker of carbon-steel secateurs and snips made in Onomichi, sold abroad by Niwaki.",
  "lines": [], "eras": [], "sig": ["Okatsune 103", "Okatsune snips"], "sc": [], "rel": ["Niwaki"], "s": "https://www.architecturalplants.com/product/okatsunesnips/"},
 {"n": "Tobisho", "c": "Japan", "f": "", "seg": "Hand-forged Japanese secateurs", "d": "Japanese smithy making hand-forged secateurs and snips.",
  "lines": [], "eras": [], "sig": ["Tobisho SR-1", "Tobisho Hiryu", "Tobisho Barracuda Snips"], "sc": [], "rel": ["Niwaki"], "s": "https://www.niwaki.com/tobisho-sr-1-secateurs/"},
 {"n": "Niwaki", "c": "", "f": "", "seg": "Japanese garden tools", "d": "Retailer and brand of Japanese garden tools, selling its own hand-forged secateurs and Okatsune and Tobisho tools.",
  "lines": ["GR Pro", "Mainichi", "Sentei"], "eras": [], "sig": ["Niwaki GR Pro"], "sc": [], "rel": ["Okatsune", "Tobisho"], "s": NW},
 {"n": "ARS Corporation", "c": "Japan", "f": "", "seg": "Pruning tools", "d": "Japanese pruning-tool maker based in Nishinomiya, Hyogo.",
  "lines": [], "eras": [], "sig": ["ARS VS-8"], "sc": [], "rel": [], "s": "https://www.skyman.cz/en/p/ars-profi-vs-8z-bypass-pruning-shears"},
 {"n": "Darlac", "c": "United Kingdom", "f": "", "seg": "Garden hand tools", "d": "Family-owned British maker of garden cutting tools, hand tools and watering equipment, based in Slough.",
  "lines": [], "eras": [], "sig": ["Darlac Compound Action Pruner"], "sc": [], "rel": [], "s": "https://www.charlies.co.uk/darlac-dp332-compound-action-pruner"},
 {"n": "Opinel", "c": "France", "f": "1890", "seg": "Folding knives", "d": "Savoie maker of numbered wooden-handled folding knives, founded by Joseph Opinel.",
  "lines": [], "eras": ["Joseph Opinel, founder, 1890"], "sig": ["Opinel No. 8 Pruning Knife", "Opinel No. 8 Garden Knife"], "sc": [], "rel": [], "s": "https://en.wikipedia.org/wiki/Opinel_knife"},
 {"n": "Victorinox", "c": "Switzerland", "f": "1884", "seg": "Knives and tools", "d": "Swiss Army Knife maker in Ibach, Schwyz, founded by Karl Elsener.",
  "lines": [], "eras": ["Karl Elsener, founder, 1884"], "sig": ["Victorinox Pruning Knife XS"], "sc": [], "rel": [], "s": "https://en.wikipedia.org/wiki/Victorinox"},
 {"n": "Tina", "c": "Germany", "f": "1854", "seg": "Grafting and pruning knives", "d": "TINA Messerfabrik in Württemberg, making hand-made grafting and pruning knives since 1854.",
  "lines": [], "eras": [], "sig": ["Tina 605 grafting knife"], "sc": [], "rel": [], "s": "https://sneeboer.com/en-gb/hand-forged-garden-tools/tina-messen-handmade-in-germany-since-1854"}
]

traditions = [
 {"n": "Banshu Miki Uchihamono", "g": "Metal & blades", "r": "Miki, Hyogo, Japan", "p": "Edo period to present; designated traditional craft 1996",
  "d": "Forged-blade craft of Miki, which grew from carpenters' tools made to rebuild the town after Miki Castle fell to Hideyoshi.",
  "tech": "Iron and carbon steel forge-welded by hammering, mud-coated hardening, hand sharpening and finishing",
  "mat": "Iron, carbon steel, wooden handles", "forms": ["saws", "planes", "chisels", "trowels", "small knives"],
  "ctr": ["Miki Industrial Cooperative Association, Miki City"], "auth": "Traditional craft mark of the designated production area (Miki City)",
  "s": "https://kougeihin.jp/en/craft/0712"},
 {"n": "Echigo Sanjo Uchihamono", "g": "Metal & blades", "r": "Sanjo, Niigata, Japan", "p": "Middle Ages to present; designated traditional craft 2009",
  "d": "Sanjo forged blades, grown from medieval sickles and hoes into knives, chisels, axes and wood shears.",
  "tech": "Free forging, iron and carbon steel forge-welded, mud-coated hardening, all finishing by hand",
  "mat": "Iron, carbon steel, wooden handles", "forms": ["kitchen knives", "planes", "chisels", "hatchets", "sickles", "wood shears"],
  "ctr": ["Echigo Sanjo Blacksmith Group, Sanjo Blacksmithing Dojo"], "auth": "Traditional craft mark of the designated production area (Sanjo City)",
  "s": "https://kougeihin.jp/en/craft/0706/"}
]

notes = ("Secateurs: 41 flat models -> 9 archetypes (Felco 2, Original LÖWE anvil, Okatsune 103, Tobisho SR-1, Tobisho Hiryu, Niwaki GR Pro, ARS VS-8, "
 "Darlac compound, ratchet pruner) + 20 models. Dropped: duplicate Kent & Stowe row; Spear & Jackson 'Kew Gardens Collection' (a range, not a model); "
 "Higurashi GR folded into GR Pro; Felco 2e is the 2026 electric successor per Felco. Felco 600 is a folding saw, not a pruning knife, so it was "
 "left for the saws shelf. No Bahco, Wolf-Garten or Gardena ratchet archetype: no retrieved page names a specific model (Wolf-Garten anvils listed as "
 "LÖWE-pattern interpretations). Felco knives and Banshu Hamono ikebana scissors left out (no model page retrieved). Traditions: kougeihin.jp lists "
 "no pruning shears among Miki products and 'wood shears' for Sanjo, so they are given as general Japanese blade traditions.")

out = {"kinds": [secateurs, snips, knife], "brands": brands, "traditions": traditions, "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/C2/shelves/01_00.json"
tmp = p + ".tmp"
json.dump(out, open(tmp, "w"), ensure_ascii=False, indent=1)
os.replace(tmp, p)
print("written", len(secateurs["m"]))
