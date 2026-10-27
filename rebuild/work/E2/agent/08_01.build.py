import json, os
U = dict(slcd="https://en.wikipedia.org/wiki/Spring-loaded_camming_device", nut="https://en.wikipedia.org/wiki/Nut_(climbing)",
 hex="https://en.wikipedia.org/wiki/Hex_(climbing)", pit="https://en.wikipedia.org/wiki/Piton", croll="https://en.wikipedia.org/wiki/Petzl_Croll",
 asc="https://en.wikipedia.org/wiki/Ascender_(climbing)", dragon="https://www.outdoorgearlab.com/reviews/climbing/climbing-cams/dmm-dragon-cam",
 best="https://www.outdoorgearlab.com/topics/climbing/best-ascender", mr="https://honeybros.com/maillon-rapide-delta/")
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": U[s], "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
kinds = [
 {"n": "Camming device", "a": "cam · SLCD · friend",
  "d": "Spring-loaded active protection whose lobes expand to grip a crack.",
  "t": ["single axle", "double axle", "offset", "micro cam", "three-lobe", "extendable sling"],
  "s": "https://www.inglesport.com/product-category/climb/protection/cams/",
  "x": [X("Wild Country Friend", "Ray Jardine's spring-loaded cam with a constant camming angle, the origin of the modern SLCD; 'friend' became generic.", "Wild Country", "1978", "slcd",
          [("Friend", "Wild Country", "1978", "Jardine design, US patent 4,184,657")], dt="size · colour code"),
        X("Black Diamond Camalot", "Double-axle cam that widened each unit's range; the most familiar size and colour scheme.", "Black Diamond", "", "slcd",
          [("Camalot C4", "Black Diamond", "", ""), ("Camalot Ultralight", "Black Diamond", "", "lighter version"), ("Camalot Z4", "Black Diamond", "", "small double-axle cams")], dt="size 0.3–6 · colour code"),
        X("DMM Dragon", "Double-axle cam with an extendable Dyneema sling and textured lobes.", "DMM", "", "dragon", dt="size · colour code"),
        X("Totem Cam", "Cam whose lobes expand independently.", "Totem", "", "slcd", dt="size"),
        X("Omega Pacific Link Cam", "Linked-lobe cam that spans an unusually wide crack range.", "Omega Pacific", "", "slcd"),
        X("CCH Alien", "Flexible-stem small cam.", "CCH", "", "slcd")],
  "m": [["Ultralight Master Cam", "Metolius"]]},
 {"n": "Climbing nut", "a": "chock · wire · rock",
  "d": "Passive wedge of metal on a wire placed in a crack as climbing protection.",
  "t": ["stopper (wedge)", "hex", "offset", "curved", "brass micro nut (RP)"],
  "s": "https://www.inglesport.com/product-category/climb/protection/nuts-rocks/",
  "x": [X("Hexentric", "Six-sided irregular chock by Yvon Chouinard and Tom Frost, placed passively or to cam in parallel cracks.", "Chouinard Equipment", "1973", "hex",
          [("Polycentric Hexentric", "Chouinard Equipment", "1973", "Tomas Carlstrom design"), ("Hexentric", "Black Diamond", "1989", "design sold to Black Diamond, still made")], dt="size · on wire or sling"),
        X("Black Diamond Stopper", "Tapered wedge nut on a wire; the brand name often used for nuts in general.", "Black Diamond", "", "nut", dt="size · colour code")],
  "m": [["Halfnuts", "DMM"], ["IMP Brass Nut", "DMM"], ["Wallnut", "DMM"], ["Rocks", "Wild Country"]]},
 {"n": "Piton", "a": "peg · pin",
  "d": "Steel spike hammered into a rock crack as a fixed or temporary anchor.",
  "t": ["knifeblade (bugaboo)", "angle", "bong", "beak"],
  "s": "https://www.inglesport.com/product-category/climb/protection/ice-screws-pitons/",
  "x": [X("Lost Arrow", "Hot-forged tapered piton for medium cracks, named after Salathé's ascent of Lost Arrow Spire.", "", "", "pit",
          [("Salathé pin", "", "", "hardened-steel forerunner made for the Lost Arrow climb"), ("Lost Arrow", "Chouinard Equipment", "", "Salathé–Chouinard design")], dt="length"),
        X("RURP", "Realized Ultimate Reality Piton: tiny piton for thin seams in aid climbing.", "Chouinard Equipment", "1959", "pit",
          [("RURP", "Chouinard Equipment", "1959", "Tom Frost and Yvon Chouinard")])],
  "m": [["V Conique", "Petzl"]]},
 {"n": "Rope ascender", "a": "jumar · jammer",
  "d": "Mechanical clamp that slides up a rope and locks under load, held in the hand, on the chest or on the foot.",
  "t": ["handled", "handleless", "chest", "foot", "emergency (minimal)"],
  "s": "https://www.inglesport.com/product-category/cave/srt-equipment/ascenders/",
  "x": [X("Jumar", "The first commercial handled ascender, by Adolph Jüsi and Walter Marti; gave its name to 'jumaring'.", "Jümar Pangit", "1958", "asc", dt="left or right hand"),
        X("Petzl Croll", "Chest ascender for caving and rope access, built by Fernand Petzl for Bruno Dressler.", "Petzl", "1968", "croll"),
        X("Petzl Ascension", "Handled ascender with an ergonomic grip.", "Petzl", "", "best", dt="left or right hand"),
        X("Petzl Basic", "Compact handleless ascender, often paired with the Croll.", "Petzl", "", "best"),
        X("Petzl Tibloc", "Ultralight emergency rope clamp used with a carabiner.", "Petzl", "", "best"),
        X("Black Diamond Index", "Handled ascender whose trigger works with thumb or index finger.", "Black Diamond", "", "best")],
  "m": [["Hand Cruiser", "Edelrid"], ["Quick Roll", "Climbing Technology"], ["Simple+", "Climbing Technology"], ["A&D", "Grivel"], ["Futura Body", "Kong"],
        ["Solo 2", "CAMP"], ["Turbohand", "Camp"], ["Hands Up", "Beal"], ["Pantin", "Petzl"], ["Ropeman 1", "Wild Country"], ["Ropeman 2", "Wild Country"]]},
 {"n": "Climbing pulley", "a": "progress-capture pulley · hauling device",
  "d": "Sheave in a side plate that redirects or hauls rope, with or without a progress-capture cam.",
  "t": ["simple pulley", "progress capture", "tandem (zip-line)", "pulley-carabiner"],
  "s": "https://www.inglesport.com/product-category/cave/rigging-equipment/pulleys/",
  "x": [X("Petzl Traxion", "Progress-capture pulley family used for hauling, ascending and top-rope soloing.", "Petzl", "", "best",
          [("Micro Traxion", "Petzl", "", "79 g, 8–11 mm, the most versatile"), ("Mini Traxion", "Petzl", "", ""), ("Pro Traxion", "Petzl", "", "")], dt="rope range · sheave bearing")],
  "m": [["Rollclip", "Petzl"], ["Spin L2", "Petzl"], ["Tandem", "Petzl"], ["Tandem Speed", "Petzl"], ["Orbiter D", "Skylotec"],
        ["Roll n' Lock", "Climbing Technology"], ["Spoc", "Edelrid"]]},
 {"n": "Climbing daisy chain", "a": "adjustable lanyard", "d": "Chain of loops or adjustable lanyard that links the harness to an anchor in aid climbing.",
  "t": ["pocketed daisy chain", "adjustable lanyard", "single or dual"], "s": "https://www.needlesports.com/Catalogue/Climbing/Big-Wall-Aid-Climbing/Daisy-Chains",
  "m": [["Connect Adjust", "Petzl"], ["Dual Connect Adjust", "Petzl"]]},
 {"n": "Climbing etrier", "a": "aider", "d": "Short webbing ladder with steps clipped to gear to stand on in aid climbing.",
  "t": ["ladder", "alternating steps"], "s": "https://www.inglesport.com/product-category/climb/slings-cords/etriers-lanyards/",
  "m": [["Lyon Etrier", "Lyon"]]},
 {"n": "Clip stick", "a": "stick clip", "d": "Telescopic pole with a clip head that pre-clips a quickdraw or the rope to a bolt from below.",
  "s": "https://v12outdoor.com/products/pongoose-climber-550-3-in-1-clipstick-stick-clip-with-extender-and-2-x-coupling-bands",
  "m": [["Pongoose Climber 550+ Clipstick", "Pongoose"]]},
 {"n": "Bolt hanger", "a": "hanger", "d": "Metal plate fixed on an expansion or glue-in bolt to give a rope anchor point.",
  "t": ["plate hanger", "ring", "twisted hanger", "stainless steel"], "s": "https://www.inglesport.com/product-category/cave/rigging-equipment/hangers/",
  "m": [["Collinox", "Petzl"], ["Vrillee Twist Hanger", "Petzl"], ["Anellox", "Raumer"], ["Superstar", "Raumer"]]},
 {"n": "Maillon rapide", "a": "quick link · screw link", "d": "Steel screw-link connector for permanent rigging of anchors.",
  "t": ["oval", "delta", "semi-circular", "steel", "stainless", "EN 362 / EN 12275 certified"],
  "s": "https://www.inglesport.com/product-category/cave/carabiners-connectors/maillon-rapides/",
  "m": [["Maillon Rapide Delta", "Péguet"], ["P11", "Petzl"]]},
]
def B(n, c, f, seg, kf, d, s="knowledge", sig=()):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "s": s}
    if sig: b["sig"] = list(sig)
    return b
brands = [
 B("Wild Country", "UK", "", "Specialist", "cams, nuts", "British climbing hardware brand that sold Ray Jardine's Friend, popularised by Mark Vallance.", U["slcd"], ["Friend", "Rocks"]),
 B("Black Diamond", "USA", "1989", "Mainstream", "climbing gear", "American climbing and ski equipment maker in Salt Lake City.", sig=["Camalot", "Stopper", "Hexentric", "Index"]),
 B("DMM", "UK", "", "Specialist", "hot-forged hardware", "Welsh climbing hardware maker in Llanberis.", sig=["Dragon", "Wallnut"]),
 B("Chouinard Equipment", "USA", "", "Heritage manufactory", "pitons, chocks", "Yvon Chouinard's climbing hardware firm; its designs passed to Black Diamond in 1989.", U["hex"], ["Hexentric", "RURP", "Lost Arrow"]),
 B("Petzl", "France", "1975", "Professional & flagship", "climbing and caving hardware", "French maker of climbing, caving and work-at-height equipment from Crolles.", sig=["Croll", "Ascension", "Basic", "Tibloc", "Traxion"]),
 B("Jümar Pangit", "Switzerland", "1958", "Heritage manufactory", "ascenders", "Swiss firm set up by Adolph Jüsi and Walter Marti to make the Jumar.", U["asc"], ["Jumar"]),
 B("Totem", "Spain", "", "Specialist", "cams", "Maker of the independently-expanding Totem Cam.", U["slcd"], ["Totem Cam"]),
 B("Omega Pacific", "USA", "", "Specialist", "cams, carabiners", "Maker of the Link Cam.", U["slcd"], ["Link Cam"]),
 B("CCH", "USA", "", "Specialist", "small cams", "Maker of the Alien cam.", U["slcd"], ["Alien"]),
 B("Péguet", "France", "", "Heritage manufactory", "quick links", "Family firm in the French Alps making Maillon Rapide quick links for three generations.", U["mr"], ["Maillon Rapide"]),
]
notes = ("All 10 planned kinds kept. Archetypes from fetched Wikipedia and OutdoorGearLab pages. Dropped from old models: Black Diamond Camalot range (now an archetype), "
         "Raumer Alien/Minox/Wing hangers (trim), Camalot C4/Ultralight moved to Camalot versions; Petzl Mini/Pro Traxion moved into the Traxion archetype. "
         "DMM Wallnut and Petzl Pro Traxion kept without details (no retrieved page). Totem country 'Spain' and CCH/Omega Pacific country 'USA' are from knowledge.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/08_01.json"
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1); os.replace(p + ".tmp", p)
print("ok")
