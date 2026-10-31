import json, os
U = dict(nomic="https://www.climbing.com/gear/editors-choice-2019-petzl-nomic-review/?scope=anon", aac="https://americanalpineclub.org/news/2018/3/27/the-ice-axe",
 dmm="https://eu.dmmwales.com/blogs/journal/fred-hall-how-ice-axes-have-evolved-through-adventure-and-innovation", fp="https://en.wikipedia.org/wiki/Front_pointing",
 mp="https://www.mountainproject.com/v/110046312", g12="https://www.advnture.com/reviews/grivel-g12", axe="https://www.outdoorgearlab.com/topics/snow-sports/best-ice-axe",
 vf="https://edelrid.com/ch-en/knowledge/knowledge-base/in-depth-knowledge-about-via-ferrata-sets", lynx="https://rockrun.com/blogs/the-flash-rock-run-blog/petzl-lynx-crampon-review",
 ob="https://outsidebozeman.com/gear/product-reviews/equipment/review-petzl-nomic", fuel="https://blog.weighmyrack.com/black-diamond-fuel-ice-tool/")
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": U[s], "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
kinds = [
 {"n": "Ice axe", "a": "mountaineering axe · walking axe",
  "d": "Axe with a pick and adze made for climbing and travel on snow and ice.",
  "t": ["straight shaft", "bent shaft", "CEN-B (basic)", "CEN-T (technical)", "adze or hammer head", "ultralight aluminium", "leash"],
  "s": "https://www.mec.ca/products/climbing/climbing-gear/mountaineering-and-ice-climbing-gear",
  "x": [X("MacInnes Massey ice axe", "The first ice axe made entirely of metal, by Hamish MacInnes with Benjamin and Steven Massey.", "", "early 1960s", "aac"),
        X("Petzl Summit", "Bent-shaft general mountaineering axe.", "Petzl", "", "axe",
          [("Summit", "Petzl", "", "360 g, CEN-B"), ("Summit Evo", "Petzl", "", "400 g, CEN-B; best overall in GearLab test")], dt="length · weight"),
        X("Grivel Air Tech", "Bent-shaft general mountaineering axe with hammer option.", "Grivel", "", "axe", [("Air Tech Evolution", "Grivel", "", "430 g, CEN-B")], dt="length · adze or hammer"),
        X("Black Diamond Raven", "Straight-shaft classic walking and glacier axe.", "Black Diamond", "", "axe",
          [("Raven", "Black Diamond", "", "437 g"), ("Raven Pro", "Black Diamond", "", "362 g"), ("Raven Ultra", "Black Diamond", "", "348 g, ultralight")], dt="length"),
        X("Petzl Glacier", "Straight-shaft basic glacier axe.", "Petzl", "", "axe",
          [("Glacier", "Petzl", "", "350 g"), ("Glacier Literide", "Petzl", "", "320 g ultralight")], dt="length"),
        X("CAMP Corsa", "Ultralight aluminium axe for ski mountaineering and approaches.", "CAMP", "", "axe",
          [("Corsa", "CAMP", "", "209 g, the lightest tested"), ("Corsa Nanotech", "CAMP", "", "249 g, steel-tipped bent shaft")], dt="length")],
  "m": [["Sum'Tec", "Petzl"], ["Gully", "Petzl"], ["Ride", "Petzl"], ["Swift", "Black Diamond"], ["Venom", "Black Diamond"],
        ["Neve", "CAMP"], ["G1", "Grivel"], ["Altum", "Trango"]]},
 {"n": "Ice tool", "a": "technical ice axe · ice hammer",
  "d": "Technical axe with a curved shaft and steep pick made for ice and mixed climbing.",
  "t": ["leashed", "leashless", "hammer", "adze", "modular picks", "dry-tooling pick", "ice pick"],
  "s": "https://www.mec.ca/products/climbing/climbing-gear/mountaineering-and-ice-climbing-gear",
  "x": [X("Terrordactyl", "Short tool with a steeply dropped straight pick, designed by Hamish MacInnes and made by Trevor Peck; suited to Scottish ice.", "", "early 1970s", "dmm"),
        X("Chouinard Zero", "Curved-pick Chouinard tool with a laminated bamboo shaft.", "Chouinard Equipment", "", "dmm"),
        X("Lowe Alpine Hummingbird", "Tool with interchangeable parts, more popular in America than Europe.", "Lowe Alpine", "", "dmm"),
        X("DMM Predator", "First ice axe with a fully curved shaft, designed by Phil Waters.", "DMM", "", "dmm",
          [("Venom", "DMM", "", "kinked shaft, banana pick"), ("Rebel", "DMM", "", "forged one-piece head and shaft"), ("Cortex", "DMM", "", "CNC-machined leashless tool")]),
        X("Black Diamond Cobra", "Carbon-fibre-shafted ice tool.", "Black Diamond", "", "fuel",
          [("Fuel", "Black Diamond", "2014", "single hydroformed aluminium piece combining Cobra performance with Fusion modularity"), ("Fusion", "Black Diamond", "", "modular mixed tool")]),
        X("Petzl Nomic", "Leashless technical ice tool that set the standard for steep ice.", "Petzl", "", "nomic",
          [("Nomic (2019)", "Petzl", "2019", "about 21 oz; Mini Marteau hammer, steel spike, Pur'Ice pick")], dt="pick · hammer · pick weights"),
        X("Petzl Quark", "All-round technical tool sharing picks with the Nomic, Ergonomic and Sum'Tec.", "Petzl", "", "ob", dt="hammer or adze"),
        X("Petzl Ergonomic", "Petzl tool for hard mixed climbing and dry tooling.", "Petzl", "", "nomic")],
  "m": [["Vulture", "Clog"]]},
 {"n": "Crampon", "a": "",
  "d": "Spiked frame fitted to a boot for grip on ice and hard snow.",
  "t": ["strap (C1)", "hybrid (C2)", "step-in (C3)", "10-point", "12-point", "14-point", "mono-point", "dual-point", "horizontal front points", "vertical front points", "anti-balling plates", "walking / hiking spikes"],
  "s": "https://www.mec.ca/products/climbing/climbing-gear/mountaineering-and-ice-climbing-gear",
  "x": [X("Grivel front-point crampon", "Grivel's addition of two front points to the 10-point crampon, which created front pointing.", "Grivel", "early 1930s", "fp"),
        X("Grivel G12", "Classic 12-point chromoly mountaineering crampon, called 'the king of the crampons'.", "Grivel", "", "g12",
          [("G12 Cramp-o-matic", "Grivel", "", "C3 step-in"), ("G12 New-matic", "Grivel", "", "C2 semi-automatic"), ("G12 New classic", "Grivel", "", "C1 flexible bails")], dt="binding · size"),
        X("Petzl Lynx", "Modular chromoly ice and mixed crampon with interchangeable mono and dual front points.", "Petzl", "", "lynx", dt="mono or dual points · B2/B3 binding")],
  "m": [["Contact", "Black Diamond"], ["Neve Pro", "Black Diamond"], ["Sabretooth Pro", "Black Diamond"], ["Stinger", "Black Diamond"], ["Harfang Tech", "Blue Ice"],
        ["KTS Hiking Crampons", "Kahtoola"], ["Dart Leverlock", "Petzl"], ["Leopard Flexlock", "Petzl"]]},
 {"n": "Ice screw", "a": "",
  "d": "Threaded tube screwed into ice as climbing protection.",
  "t": ["steel", "aluminium", "integrated crank", "length 10–22 cm"],
  "s": "https://www.mec.ca/products/climbing/climbing-gear/mountaineering-and-ice-climbing-gear",
  "x": [X("Black Diamond Express", "Steel ice screw with a folding crank, long the standard rack screw.", "Black Diamond", "", "mp", dt="length"),
        X("Petzl Laser Speed", "Ice screw with a small hanger and crank knob that places quickly.", "Petzl", "", "mp",
          [("Laser Speed Light", "Petzl", "", "aluminium body with steel tip")], dt="length")]},
 {"n": "Via ferrata lanyard", "a": "via ferrata set · klettersteig set",
  "d": "Energy-absorbing Y lanyard with two carabiners made for clipping along a via ferrata cable, tested to EN 958.",
  "t": ["progressive-tear energy absorber", "elastic arms", "swivel", "EN 958:2017", "EN 958:2024"],
  "s": "https://www.inglesport.com/product-category/climb/slings-cords/etriers-lanyards/",
  "m": [["Scorpio Eashook", "Petzl"], ["Scorpio Vertigo", "Petzl"]]},
]
def B(n, c, f, seg, kf, d, s="knowledge", sig=()):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "s": s}
    if sig: b["sig"] = list(sig)
    return b
brands = [
 B("Petzl", "France", "1975", "Professional & flagship", "climbing and caving hardware", "French maker of climbing, caving and work-at-height equipment.", sig=["Nomic", "Quark", "Summit", "Lynx", "Laser Speed"]),
 B("Black Diamond", "USA", "1989", "Mainstream", "climbing gear", "American climbing and ski equipment maker in Salt Lake City.", sig=["Raven", "Cobra", "Fuel", "Express"]),
 B("Grivel", "Italy", "", "Heritage manufactory", "crampons, ice axes", "Italian maker of crampons and ice axes that added front points to the crampon.", U["fp"], ["G12", "Air Tech"]),
 B("CAMP", "Italy", "1889", "Specialist", "climbing hardware", "Italian mountain hardware maker from Premana.", sig=["Corsa"]),
 B("DMM", "UK", "", "Specialist", "hot-forged hardware", "Welsh climbing hardware maker in Llanberis.", U["dmm"], ["Predator", "Venom"]),
 B("Chouinard Equipment", "USA", "", "Heritage manufactory", "pitons, ice tools", "Yvon Chouinard's climbing hardware firm, forerunner of Black Diamond.", sig=["Zero"]),
 B("Lowe Alpine", "USA", "", "Specialist", "packs, ice tools", "Outdoor-equipment brand that made the Hummingbird ice tool.", U["dmm"], ["Hummingbird"]),
]
notes = ("All 5 planned kinds kept. Ice-screw history (Salewa/Chouinard tubular screws) and Grivel's founding date not found on a retrieved page (Grivel history page 404), so left out. "
         "Petzl Sarken and Petzl Scorpio not attested on a fetched page: Scorpio stays as old models, Sarken omitted. Black Diamond Cobra details only via the Fuel launch post (Colorado Mountain School review 403). "
         "Dropped old 'Corsa Alpine' (CAMP) as superseded by the Corsa archetype; Petzl Summit/Glacier/Gully kept as archetype versions or models.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/08_02.json"
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1); os.replace(p + ".tmp", p)
print("ok")
