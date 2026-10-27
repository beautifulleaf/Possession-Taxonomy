import json, os
U = dict(bob="https://en.wikipedia.org/wiki/Bobbin_(caving_equipment)", stop="https://en.wikipedia.org/wiki/Petzl_Stop",
 srt="https://en.wikipedia.org/wiki/Single-rope_technique", cav="https://en.wikipedia.org/wiki/Caving_equipment",
 ny="https://nymcc.org.uk/nymcc-equipment-reviews-oversuits/")
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": U[s], "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
kinds = [
 {"n": "SRT kit", "a": "single rope technique kit · vertical kit",
  "d": "Set of harness-mounted rope-climbing gear (ascenders, descender, cowstails, foot loop) sold or assembled as one single rope technique kit.",
  "t": ["frog (sit-stand)", "Texas kick", "ropewalker", "Mitchell"],
  "s": "https://www.inglesport.com/product-category/cave/srt-equipment/srt-kits/",
  "x": [X("Frog rig", "Sit-stand system with a chest ascender and a hand ascender on a foot loop.", "", "", "srt", dt="harness · ascenders · descender"),
        X("Ropewalker rig", "Rope-walking system with ascenders on each foot, as in the ropewalker and Mitchell systems.", "", "", "srt")]},
 {"n": "Caving descender", "a": "bobbin · rack",
  "d": "Bobbin or rack descender made for single rope technique in caves, often with assisted braking.",
  "t": ["bobbin", "self-braking bobbin", "rack"],
  "s": "https://www.inglesport.com/product-category/cave/srt-equipment/ascenders/",
  "x": [X("Petzl Simple", "Two-bobbin descender from Bruno Dressler's 1960s design, the ancestor of most modern bobbins.", "Petzl", "", "bob"),
        X("Petzl Stop", "Self-braking bobbin descender whose cam crimps the rope when the handle is released.", "Petzl", "", "stop",
          [("Stop (original)", "Petzl", "", "aluminium bobbins, 9–12 mm rope"), ("Stop (2019)", "Petzl", "2019", "stainless bobbins, folding handle, 8.5–11 mm, recreational only")]),
        X("Rappel rack", "Bar-frame descender developed by Huntsville, Alabama cavers for long descents.", "", "late 1960s", "srt", dt="number of bars")],
  "m": [["Rig", "Petzl"]]},
 {"n": "Caving chest harness", "a": "chest strap",
  "d": "Chest strap or harness that holds the chest ascender upright for single rope technique.",
  "t": ["webbing strap", "padded harness", "quick-adjust buckle"], "s": "https://proteushop.com/en/37897-caving?page=3"},
 {"n": "Caving cowstail", "a": "cow's tail · safety cord",
  "d": "Short lanyard with a carabiner used to clip into rebelays and traverse lines on single rope technique.",
  "t": ["dynamic rope", "adjustable", "long and short arms"], "s": "https://www.inglesport.com/product-category/cave/srt-equipment/cowstails-footloops/",
  "m": [["Progress Adjust-I", "Petzl"]]},
 {"n": "Caving foot loop", "a": "",
  "d": "Adjustable loop of webbing or cord that holds a foot ascender and the foot for climbing a rope.",
  "t": ["webbing", "cord", "double foot"], "s": "https://www.inglesport.com/product-category/cave/srt-equipment/cowstails-footloops/",
  "m": [["Footup", "Aventure Verticale"], ["Footape", "Petzl"], ["Footcord", "Petzl"]]},
 {"n": "Caving oversuit", "a": "caving suit",
  "d": "Abrasion-resistant one-piece suit (Cordura or PVC) worn over the undersuit in caves.",
  "t": ["Cordura", "PVC", "zipped", "hook-and-loop sealed"],
  "s": "https://www.inglesport.com/product-category/cave/caving-clothing/oversuits/",
  "x": [X("Warmbac Cordura oversuit", "Tough Cordura suit that loses waterproofing over time and shrinks with use.", "Warmbac", "", "ny",
          [("Standard", "Warmbac", "", "zipped, more flexible"), ("Digger", "Warmbac", "", "hook-and-loop sealed, very durable")], dt="size · colour"),
        X("Meander PVC suit", "Fully waterproof heat-sealed PVC suit for wet caves.", "Meander", "", "ny"),
        X("AV Titan", "Well-cut flexible oversuit that stays waterproof for a time.", "Aventure Verticale", "", "ny")],
  "m": [["Bitex Oversuit", "Alp Design"], ["Cordura Plus Caving Oversuit", "Landjoff"], ["PVC Caving Oversuit", "Warmbac"]]},
 {"n": "Caving undersuit", "a": "furry",
  "d": "Thermal one-piece fleece or pile suit worn under a caving oversuit.",
  "t": ["fleece", "fibre pile", "neoprene wetsuit (wet caves)"], "s": "https://ubss.org.uk/caving/gear-guide/"},
 {"n": "Caving tackle bag", "a": "tacklesack · kit bag",
  "d": "Round or oval bag with shoulder straps and drawstring or roll-top closure for hauling rope and gear through caves.",
  "t": ["PVC", "drawstring", "roll-top", "belt-hung small bag"],
  "s": "https://www.inglesport.com/product-category/cave/bags-containers/tacklebags/",
  "m": [["AV Confort", "Aventure Verticale"], ["Colectivo", "MTDE"], ["Sherpa", "MTDE"], ["Classique", "Petzl"], ["Transport 45L", "Petzl"],
        ["Daren Tackle Bag", "Warmbac"], ["SRT Bag", "Warmbac"]]},
 {"n": "Caving ladder", "a": "electron ladder",
  "d": "Light flexible ladder of wire rope and alloy rungs rigged down pitches in caves.",
  "t": ["length", "rung spacing", "spreader"],
  "s": "https://proteushop.com/en/37897-caving?page=3",
  "x": [X("Elektron ladder", "Light wire ladder with aluminium rungs developed by Robert de Joly; it opened deep caves such as the Gouffre Berger.", "", "", "cav", dt="length · wire gauge")]},
]
def B(n, c, f, seg, kf, d, s="knowledge", sig=()):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "s": s}
    if sig: b["sig"] = list(sig)
    return b
brands = [
 B("Petzl", "France", "1975", "Professional & flagship", "caving and climbing hardware", "French maker of caving, climbing and work-at-height equipment.", sig=["Stop", "Simple", "Croll"]),
 B("Warmbac", "", "", "Specialist", "caving oversuits", "Caving clothing and bag maker known for tough Cordura oversuits.", U["ny"], ["Cordura oversuit", "Digger"]),
 B("Meander", "", "", "Specialist", "PVC caving suits", "Maker of heat-sealed PVC caving suits.", U["ny"], ["Meander PVC suit"]),
 B("Aventure Verticale", "", "", "Specialist", "caving gear", "Caving equipment brand (AV).", U["ny"], ["Titan"]),
]
notes = ("All 9 planned kinds kept. Meanderthal oversuit and Lyon tackle bags from the brief not attested on any fetched page, so left out. "
         "Lights left to B3 per brief. Countries for Warmbac, Meander and Aventure Verticale left blank (not on retrieved page).")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/08_04.json"
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1); os.replace(p + ".tmp", p)
print("ok")
