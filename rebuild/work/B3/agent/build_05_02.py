import json, os
W = 'https://en.wikipedia.org/wiki/'
FC = 'https://www.farmcollector.com/equipment/coleman-lanterns-zm0z12octzbea/'
TM = 'https://terry-marsh.com/coleman-us-lanterns-1946-1960'
LN = 'https://lanternnet.com/r-e-dietz-compendium-index-of-non-electric-american-made-products/'
MH = 'https://scholarworks.moreheadstate.edu/mh_and_rm_artifacts/78'
UCO = 'https://www.purpleturtle.co.uk/about-uco-candle-lanterns/'
UI = 'https://blog.lib.uiowa.edu/speccoll/2024/09/12/the-special-collections-and-archives-fall-2024-reading-room-exhibition-japanese-pocket-lanterns-brings-a-delicate-art-to-life/'
IB = 'https://visit.ibarakiguide.jp/en/?p=46546'
GW = 'https://www.telegraphherald.com/news/features/article_4ac05670-27fc-11ef-a101-cf2394eafeac.html'
TK = 'https://kraftstories.com/blogs/turkish-mosaic-lamp/the-rich-history-of-turkish-lamps-craftsmanship-and-culture'
MB = 'https://www.1stdibs.com/buy/moroccan-brass-lanterns'

def X(n, d, mk, y, s, v=(), a='', dt=''):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s,
            "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}

kinds = [
 {"n": "Gas & pressure lantern", "a": "mantle lantern · pressure lamp · propane lantern · liquid-fuel lantern · dual-fuel lantern · Tilley lamp",
  "d": "Carried lantern in which pressurised fuel or gas heats a mantle until it glows.",
  "t": ["Kerosene (paraffin) pressure", "White gas (Coleman fuel)", "Dual fuel", "Propane", "Gas cartridge", "Single mantle", "Double mantle"],
  "s": "https://en.wikipedia.org/wiki/Coleman_Lantern",
  "x": [
   X("Coleman pressure lantern", "Pump-up mantle lantern from Coleman, burning kerosene, gasoline, Coleman fuel or propane; the American camping and farm standard.",
     "Coleman", "1914", W + "Coleman_Lantern", a="Coleman Lantern",
     v=[("Arc-style lantern", "Coleman", "1905", "first Coleman lantern, ornate home model; 5,000 made"),
        ("Model 427", "Coleman", "1926–1930", ""),
        ("Model 237", "Coleman", "1928", "all-purpose kerosene lantern common in dairy barns"),
        ("Model 242C", "Coleman", "1942–1950", "green painted, later nickel-plated fount"),
        ("Model 220 (military)", "Coleman", "1943", "wartime issue"),
        ("Model 220C / 220D / 220E", "Coleman", "1944–1951", "double mantle; 220D nickel-plated then green fount; 220E steel fount from 1951"),
        ("Model 228C / 228D / 228E", "Coleman", "1945–1951", "green painted or nickel-plated brass founts; 228E steel"),
        ("Model 200", "Coleman", "1950–1951", "single mantle; nickel-plated then green brass fount"),
        ("Model 200A", "Coleman", "1951–1983", "single mantle; red most years, maroon 1961, factory white 1953, green late run"),
        ("Model 202", "Coleman", "1954", "made about ten years"),
        ("Model 220F", "Coleman", "", "")],
     dt="single or double mantle · fount metal (brass, nickel, steel) · fount colour (green, red, maroon, white) · date stamp on fount"),
   X("Petromax pressure lantern", "German kerosene pressure lantern devised by Max Graetz; much copied (Tower, Lea Hin, Prabhat).",
     "Petromax", "1910", W + "Petromax",
     v=[("829/500CP", "Petromax", "", "paraffin pressure lantern"),
        ("HK500", "Petromax", "", "500 candlepower class"), ("HK350", "Petromax", "", ""), ("HK250", "Petromax", "", "")],
     dt="candlepower 250–500 · brass or nickel finish · kerosene or multi-fuel"),
   X("Tilley X246 storm lantern", "British paraffin pressure storm lantern, the best-known Tilley.",
     "Tilley", "1964", W + "Tilley_lamp", a="Tilley lamp",
     v=[("X246B", "Tilley", "1964", "storm lantern, made in Northern Ireland")]),
   X("Vapalux pressure lantern", "Halifax-made paraffin pressure lantern, standard British Army issue from the Second World War.",
     "Willis & Bates", "1938", W + "Vapalux", a="Bialaddin",
     v=[("E41", "Willis & Bates", "c. 1938–1941", "earliest model"),
        ("300", "Willis & Bates", "1938–1946", "army issue"),
        ("300X", "Willis & Bates", "1938–1946", "later sold as Bialaddin 300X"),
        ("21C", "Willis & Bates", "late 1940s", "armed forces issue"),
        ("M1", "Willis & Bates", "1945–1968", "also Bialaddin 305"),
        ("M320", "Willis & Bates", "1968", "called M1 in army service; still made"),
        ("M1B", "Willis & Bates", "1990", "retro-style civilian lamp")])],
  "m": [["F1 Lite", "Coleman"], ["Easylight Lantern", "Primus"], ["Easylight Duo", "Primus"], ["Micron Lantern", "Primus"],
        ["Ultralight Micron Compact LP", "Primus"], ["Mini Lite Lantern", "Go System"], ["Gas Lantern", "Vango"], ["Mini Gas Lantern", "Gelert"]]},

 {"n": "Hurricane lantern", "a": "kerosene lantern · barn lantern · storm lantern · tubular lantern",
  "d": "Carried flat-wick oil lantern with a glass globe, shielded so wind cannot blow out the flame.",
  "t": ["Dead-flame", "Hot-blast (tubular)", "Cold-blast (tubular)"],
  "s": "https://en.wikipedia.org/wiki/R._E._Dietz_Company",
  "x": [
   X("Dietz Junior", "Cold-blast lantern patterned on the C.T. Ham Gem; called possibly the most popular lantern of all time.",
     "R. E. Dietz Company", "1899", LN, a="Dietz No. 20 Junior",
     v=[("Junior #857", "R. E. Dietz Company", "1899", "early versions with outside globe lift"),
        ("No. 20 Junior", "R. E. Dietz Company", "", "current production")],
     dt="globe lift (outside, inside) · finish (tin, painted colours) · fount size"),
   X("Dietz Blizzard", "Large cold-blast lantern introduced alongside the Junior.",
     "R. E. Dietz Company", "1899", LN,
     v=[("Blizzard #2", "R. E. Dietz Company", "1899", "oldest versions with outside globe lift and slotted brass cone")]),
   X("Dietz D-Lite", "Premium cold-blast hand lantern, the #2 Wizard renamed in 1919.",
     "R. E. Dietz Company", "1913", LN, a="Dietz No. 2 D-Lite",
     v=[("Top-lift D-Lite", "R. E. Dietz Company", "1913–1919", "Dietz's answer to the C.T. Ham Nu-Style"),
        ("D-Lite Streamline", "R. E. Dietz Company", "1936", ""),
        ("Air Pilot #8", "R. E. Dietz Company", "1957", "built on D-Lite tooling")]),
   X("Dietz Little Wizard", "Small cold-blast lantern, often sold to contractors for marking road barricades.",
     "R. E. Dietz Company", "1913", LN,
     v=[("Little Wizard Streamline", "R. E. Dietz Company", "1936", "")]),
   X("Dietz Monarch", "The most popular hot-blast lantern, made in at least seven variations.",
     "R. E. Dietz Company", "", LN,
     v=[("Monarch Streamline", "R. E. Dietz Company", "1936", "")]),
   X("Dietz Little Giant", "Long-burning cold-blast lantern rated for 70 hours.",
     "R. E. Dietz Company", "1926", LN,
     v=[("Little Giant #851", "R. E. Dietz Company", "1926–c. 1957", "70-hour"),
        ("#100", "R. E. Dietz Company", "", "3/8-inch wick, 100 hours")]),
   X("Feuerhand Baby", "Short-globe German steel hurricane lantern, a wartime best seller still in production.",
     "Feuerhand", "c. 1950", MH,
     v=[("Baby #275", "Feuerhand", "c. 1950", "West German steel utility lantern"),
        ("276 Baby Special", "Feuerhand", "", "current production under Petromax group")],
     dt="finish (galvanised, coloured powder coat) · globe")],
  "m": [["Dietz 78", "R. E. Dietz Company"], ["Dietz 90", "R. E. Dietz Company"]]},

 {"n": "Oil & kerosene lamp", "a": "paraffin lamp · oil lamp · wick lamp · mantle lamp",
  "d": "Standing or hanging lamp that burns lamp oil or kerosene through a wick, usually under a glass chimney.",
  "t": ["Flat wick", "Central draught (round wick)", "Side draught", "Duplex (two wicks)", "Mantle", "Electrified antique"],
  "s": W + "Kerosene_lamp",
  "x": [
   X("Argand lamp", "Oil lamp with a hollow sleeve wick and glass chimney feeding air inside and outside the flame.",
     "", "1780", W + "Argand_lamp",
     v=[("Carcel lamp", "", "1800", "clockwork pump lets the reservoir sit below the burner"),
        ("Moderator lamp", "", "1836", "Franchot's spring-driven design"),
        ("Astral lamp", "", "", "reservoir arranged to cast no shadow")]),
   X("Kosmos burner lamp", "Side-draught round-wick lamp; the burner allows glass or ceramic reservoirs.",
     "Wild & Wessel", "1865", W + "Kerosene_lamp", dt="burner size · glass, ceramic or metal reservoir"),
   X("Duplex lamp", "Lamp with two flat wicks under one chimney, each with its own adjuster; popular in Britain.",
     "", "", W + "Kerosene_lamp"),
   X("Aladdin mantle lamp", "Non-pressurised kerosene lamp whose round wick heats a mantle; Aladdin is the last maker of the type.",
     "Aladdin Industries", "1912", W + "Aladdin_Industries", dt="glass or metal fount · shade · chimney"),
   X("Tilley table lamp", "Paraffin pressure lamp made as a domestic table lamp.",
     "Tilley", "1922", W + "Tilley_lamp", v=[("TL10", "Tilley", "1922–1946", "")]),
   X("Victorian parlour lamp", "Ornate late-19th-century oil parlour lamp with coloured, often hand-painted glass shades; many later electrified.",
     "", "late 19th century", GW, a="Gone with the Wind lamp", dt="satin or painted glass · floral decoration · oil or converted"),
   X("Turkish mosaic lamp", "Lamp whose blown-glass globe is covered in hand-cut coloured glass pieces, set in a brass or bronze frame.",
     "", "Ottoman era tradition", TK, dt="form (table, hanging, floor, chandelier) · glass colours · bronze or brass base"),
   X("Moroccan pierced brass lantern", "Brass lantern cut or punched with openwork so light falls in patterns, often with coloured glass panes.",
     "", "", MB, a="fanoos", dt="octagonal, hexagonal or domed · glass panes · Fez, Marrakesh or Meknes style")]},

 {"n": "Candle lantern", "a": "",
  "d": "Enclosed lantern with a handle that holds a candle, made to be carried or hung.",
  "s": "https://knifecountryusa.com/store/product/323317.323322/uco-00411-original-candle-lantern-gray.html",
  "x": [
   X("UCO Original Candle Lantern", "Telescoping aluminium and glass camping lantern with a spring-fed candle.",
     "UCO", "", UCO,
     v=[("Original Candle Lantern", "UCO", "", ""), ("Candlelier", "UCO", "", "three candles"),
        ("Mini Candle Lantern", "UCO", "", ""), ("Candle Survival Lantern", "UCO", "", "")],
     dt="aluminium, brass or painted body · citronella or plain candles"),
   X("Gandō", "Edo-period Japanese lantern whose gimballed candle and rear mirror throw light forward only.",
     "", "early 17th century", W + "Gand%C5%8D", a="shagandō",
     dt="copper, tinplate or galvanised steel shroud")]},

 {"n": "Paper lantern", "a": "chōchin",
  "d": "Collapsible or rigid paper-covered lantern made to be carried as a light. One made to hang as decoration is not a lamp.",
  "t": ["Collapsible spiral frame", "Candle", "Battery LED insert"],
  "s": "https://metropolisjapan.com/hara-koushu-chochin-lanterns/",
  "x": [
   X("Odawara chōchin", "Small folding pocket lantern sold to travellers at the Tokaido post town of Odawara.",
     "", "late 18th–early 20th century", UI, a="pocket lantern",
     dt="copper or brass ends · lacquered koyori ends · tin and wire 'poor man's' version · oiled or persimmon-treated paper"),
   X("Gifu chōchin", "Gifu lantern of Mino washi on a thin frame, often painted; a designated traditional craft.",
     "", "mid-18th century shape", W + "Gifu_lanterns", a="Gifu lantern",
     dt="plain or painted washi · exposed wooden parts"),
   X("Suifu chōchin", "Mito folding lantern covered in tough Nishinouchi paper, a craft begun by low-ranking samurai.",
     "", "", IB, a="Mito lantern")]},

 {"n": "Electric lantern", "a": "LED lantern · camping lantern · solar lantern",
  "d": "Carried lantern lit by a battery, rechargeable cell or solar panel.",
  "t": ["Disposable battery", "Rechargeable", "Solar", "Hand-crank", "Inflatable solar", "Power-bank output"],
  "s": "https://zips.com/shop-by-brand/streamlight",
  "m": [["AlpenGlow 500", "BioLite"], ["Lighthouse 600", "Goal Zero"], ["Lighthouse Micro Charge", "Goal Zero"],
        ["Luci Outdoor 2.0", "MPOWERD"], ["Apollo", "Black Diamond"], ["Moji", "Black Diamond"],
        ["CL30R", "Fenix"], ["Siege", "Streamlight"], ["PackLite Max", "luminAID"], ["Home and Camp Lantern", "Snow Peak"],
        ["Classic Recharge", "Coleman"]]},
]

brands = [
 {"n": "Coleman", "c": "United States", "f": "", "seg": "Camping equipment", "d": "American camping brand whose pressure lantern became the standard camp and farm light.",
  "lines": ["Coleman Lantern"], "eras": [], "sig": ["Coleman pressure lantern"], "sc": ["Camping"], "rel": [], "s": W + "Coleman_Lantern"},
 {"n": "Petromax", "c": "Germany", "f": "1910", "seg": "Pressure lanterns and outdoor cooking", "d": "Brand of Max Graetz's kerosene pressure lantern, revived as Petromax GmbH in 2010.",
  "lines": ["HK500", "HK350", "HK250"], "eras": ["Ehrich & Graetz, Berlin", "Petromax GmbH, 2010–"], "sig": ["Petromax pressure lantern"], "sc": ["Camping"], "rel": ["Feuerhand"], "s": W + "Petromax"},
 {"n": "Tilley", "c": "United Kingdom", "f": "", "seg": "Paraffin pressure lamps", "d": "British maker of paraffin pressure lamps, lanterns and heaters.",
  "lines": ["X246", "TL10"], "eras": ["London (Hendon, Colindale)", "Belfast, early 1960s–2000"], "sig": ["Tilley X246 storm lantern", "Tilley table lamp"], "sc": [], "rel": ["Willis & Bates"], "s": W + "Tilley_lamp"},
 {"n": "Willis & Bates", "c": "United Kingdom", "f": "", "seg": "Paraffin pressure lanterns", "d": "Halifax maker of Vapalux pressure lanterns; brand sold to a Korean maker in 2010.",
  "lines": ["Vapalux", "Bialaddin (with Aladdin Industries, 1946–1968)"], "eras": ["Pellon Works, Halifax, 1900–1997", "Bairstow Brothers, 1997–2010"], "sig": ["Vapalux pressure lantern"], "sc": [], "rel": ["Tilley", "Aladdin Industries"], "s": W + "Vapalux"},
 {"n": "R. E. Dietz Company", "c": "United States", "f": "1840", "seg": "Hurricane lanterns", "d": "Brooklyn lamp firm, the leading American hurricane-lantern maker, now based in Hong Kong.",
  "lines": [], "eras": [], "sig": ["Dietz Junior", "Dietz Blizzard", "Dietz D-Lite", "Dietz Monarch"], "sc": [], "rel": [], "s": W + "R._E._Dietz_Company"},
 {"n": "Feuerhand", "c": "Germany", "f": "", "seg": "Hurricane lanterns", "d": "German hurricane-lantern maker whose trademark the Petromax group acquired in 2014.",
  "lines": [], "eras": [], "sig": ["Feuerhand Baby"], "sc": [], "rel": ["Petromax"], "s": MH},
 {"n": "Aladdin Industries", "c": "United States", "f": "1908", "seg": "Mantle lamps", "d": "Chicago firm, founded as the Mantle Lamp Company, maker of Aladdin mantle lamps from 1912.",
  "lines": [], "eras": [], "sig": ["Aladdin mantle lamp"], "sc": [], "rel": ["Willis & Bates"], "s": W + "Aladdin_Industries"},
 {"n": "UCO", "c": "United States", "f": "1971", "seg": "Camping lanterns", "d": "Redmond, Washington, maker of candle lanterns and candles.",
  "lines": [], "eras": [], "sig": ["UCO Original Candle Lantern"], "sc": ["Camping"], "rel": [], "s": UCO},
 {"n": "BioLite", "c": "United States", "f": "2006", "seg": "Off-grid energy and camping", "d": "Brooklyn maker of camp stoves, lanterns, headlamps and solar power.",
  "lines": ["AlpenGlow", "BaseLantern", "SunLight"], "eras": [], "sig": [], "sc": ["Camping"], "rel": [], "s": W + "BioLite"},
]

traditions = [
 {"n": "Japanese chōchin lantern making", "g": "Paper & lighting crafts", "r": "Japan (Gifu, Odawara, Mito)",
  "p": "Recorded from 1085; regional forms flourished in the Edo period",
  "d": "Collapsible paper lanterns of washi stretched over a spiral split-bamboo frame that folds into its base.",
  "tech": "Paper attached to the frame (hari), designs added (surikomi), powder on exposed wood (moriage); work often split between specialists",
  "mat": "Washi (Mino, Nishinouchi), split bamboo, wood, copper or brass fittings",
  "forms": ["Gifu chōchin", "Odawara chōchin", "Suifu chōchin"],
  "ctr": ["Gifu", "Odawara", "Mito: Suzuki Mohei Shoten (1865)", "Ozeki Lanterns, Gifu"],
  "auth": "Gifu lanterns: designated traditional craft (1995) with a regional brandmark (2006); hand-applied washi on bamboo, not printed fabric or plastic",
  "s": W + "Gifu_lanterns"},
 {"n": "Turkish mosaic lamp making", "g": "Ceramics & glass", "r": "Turkey", "p": "Most prominent in the Ottoman era; made today",
  "d": "Lamps whose blown-glass shades are covered in small hand-cut pieces of coloured glass.",
  "tech": "Glass pieces glued by hand onto a clear blown globe, gaps filled with paste, shade fitted to a metal frame",
  "mat": "Coloured glass, clear blown glass, beads, brass or bronze",
  "forms": ["Turkish mosaic lamp"], "ctr": [],
  "auth": "Slight variation between pieces, deep colour when lit, heavy bronze base, glass rings when tapped (plastic copies sound dull)",
  "s": TK},
 {"n": "Moroccan pierced brass lanterns", "g": "Metal & blades", "r": "Morocco", "p": "19th century to present",
  "d": "Brass lanterns cut or punched with geometric and floral openwork, often glazed with coloured glass.",
  "tech": "Sheet brass pierced, hammered, chased and worked in repoussé; glass panes set in",
  "mat": "Brass, coloured, seeded or etched glass",
  "forms": ["Moroccan pierced brass lantern"], "ctr": ["Marrakesh", "Fez", "Meknes"],
  "auth": "Many 'Moroccan-style' lanterns are made elsewhere (notably India); check origin and hand-cut rather than stamped work",
  "s": MB},
]

notes = ("Gas & pressure lantern: Coleman Lantern range became an archetype with model versions from Farm Collector and Terry Marsh; "
 "Petromax, Tilley X246 and Vapalux (Willis & Bates models E41/300X/M1/M320 as versions) as archetypes; Primus, Go System, Vango, Gelert kept as flat models. "
 "Hurricane lantern: cold/hot-blast/dead-flame moved from models to types; Dietz Junior, Blizzard, D-Lite, Little Wizard, Monarch, Little Giant and Feuerhand Baby as archetypes; "
 "Dietz 78 and 90 left as flat models (no page found confirming them). "
 "New kind Oil & kerosene lamp: Argand (with Carcel, moderator, astral), Kosmos, Duplex, Aladdin, Tilley TL10, Victorian parlour, Turkish mosaic and Moroccan brass. "
 "No oil table lamps were moved from Table lamp (none in this shelf's data). Aladdin model numbers left out (unconfirmed). "
 "Candle lantern: UCO models as versions of the Original; gandō as an archetype. UCO introduction year left blank (sources conflict, 1971 vs 1981). "
 "Paper lantern: Odawara, Gifu, Suifu chōchin with a chōchin tradition entry. "
 "Electric lantern cut from 45 models to 11 (BioLite, Goal Zero, MPOWERD, Black Diamond, Fenix, Streamlight, luminAID, Snow Peak, Coleman); Vulcan range dropped as duty gear. "
 "Coleman founding year left blank (not on a retrieved page). gov-online.go.jp and web-japan.org returned 403; not retried.")

out = {"kinds": kinds, "brands": brands, "traditions": traditions, "notes": notes}
p = 'work/B3/shelves/05_02.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(p + '.tmp', p)
print('written', os.path.getsize(p))
