import json, os
U = dict(cbj="https://climbingbusinessjournal.com/training-board-hold-systems/",
 bm="https://www.mont.com.au/blogs/the-mont-blog/beastmaker-1000-2000-training-boards-two-very-different-beasts-by-kale",
 pad="https://www.outdoorgearlab.com/topics/climbing/best-bouldering-crash-pad", campus="https://en.wikipedia.org/wiki/Campus_board",
 lapis="https://rockrun.com/products/lapis-wooden-brush", led="https://www.climbing.com/gear/led-board-reviews?scope=anon")
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": U[s], "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
kinds = [
 {"n": "Bouldering crash pad", "a": "crash pad · bouldering mat",
  "d": "Folding foam pad placed under a boulder problem to cushion falls.",
  "t": ["taco fold", "hinge fold", "hybrid fold", "sit-start pad", "highball (large)", "layered open- and closed-cell foam"],
  "s": "https://www.inglesport.com/product-category/climb/climbing-types/bouldering/",
  "x": [X("Organic Big Pad", "Simple large pad with a triple-layer open- and closed-cell foam sandwich; best overall in GearLab's test.", "Organic", "", "pad",
          [("5\" Thick Big Pad", "Organic", "", "46 x 57 in, 5 in thick")], dt="thickness 4 or 5 in · colour panels"),
        X("Black Diamond Mondo", "Very large 5-inch highball pad with a closed-cell top layer.", "Black Diamond", "", "pad", dt="65 x 44 in"),
        X("Metolius Magnum", "Large three-layer pad, 70 x 47 inches.", "Metolius", "", "pad"),
        X("Mad Rock Duo", "Feature-rich 5-inch pad with three-layer foam.", "Mad Rock", "", "pad")],
  "m": [["Full Pad", "Organic"], ["Simple", "Organic"], ["Circuit", "Black Diamond"], ["Circuit Z", "Black Diamond"], ["Erratic", "Black Diamond"],
        ["Mad Pad", "Mad Rock"], ["Recon", "Metolius"], ["Session II", "Metolius"], ["Newton 4.0", "Kinetik"], ["Alto", "Petzl"], ["Mantle IV", "Edelrid"]]},
 {"n": "Hangboard", "a": "fingerboard",
  "d": "Wall-mounted board with grips of set depth used to train finger strength.",
  "t": ["wood", "resin", "portable / lift block", "edge depth set"],
  "s": "https://rockrun.com/products/beastmaker-2000",
  "x": [X("Beastmaker 1000", "All-round wooden board with jugs, pockets, slots of varied depth and a benchmark edge.", "Beastmaker", "", "bm"),
        X("Beastmaker 2000", "Advanced wooden board with no jugs and harder finger combinations such as monos.", "Beastmaker", "", "bm")]},
 {"n": "Climbing board", "a": "home climbing wall · system board · training board · LED board",
  "d": "Steep wall panel with a standard hold layout, often lit and app-linked, used to train climbing at home or in a gym.",
  "t": ["fixed angle", "adjustable angle", "LED-lit holds", "mirrored layout", "freestanding frame", "campus rungs"],
  "s": U["cbj"],
  "x": [X("Campus board", "Overhanging board of wooden rungs climbed without feet, invented by Wolfgang Güllich at the Campus Centre in Nuremberg.", "", "1988", "campus", dt="rung depth · spacing"),
        X("MoonBoard", "Standardised 25° or 40° wall by Ben Moon whose fixed hold grid lets climbers share problems worldwide; first commercial LED board.", "Moon Climbing", "2005", "campus",
          [("2016 layout", "Moon Climbing", "2016", "first commercial LED layout"), ("2017 layout", "Moon Climbing", "2017", ""), ("2019 layout", "Moon Climbing", "2019", ""),
           ("MoonBoard Mini", "Moon Climbing", "2020", ""), ("2024 MoonBoard", "Moon Climbing", "2024", "fixed kicker with 10 footholds")], dt="25° or 40° · hold sets"),
        X("Tension Board", "Adjustable-angle LED board with mirrored layout.", "Tension Climbing", "2017", "cbj",
          [("Tension Board 1", "Tension Climbing", "2017", "second commercial LED board"), ("Tension Board 2", "Tension Climbing", "2022", "Mirror or Spray layout, 0–65°")], dt="size 12x8 or 12x12 ft"),
        X("Kilter Board", "App-controlled adjustable-angle board with perimeter-lit holds, by Ian Powell and Jackie Hueftle.", "Kilter", "2018", "cbj",
          [("Lemur x Kilter", "Kilter", "", "freestanding frame made with Lemur Design")]),
        X("Grasshopper Board", "Adjustable board frame by Boone Speed with a mirrored layout.", "Grasshopper", "2020", "cbj", [("12x12 side panels", "Grasshopper", "2022", "")]),
        X("Woods Board", "Densely set light-up board designed by Andy Raether with Daniel Woods, adjustable 20–70°.", "Menagerie Climbing", "2022", "led"),
        X("Decoy Board", "Symmetrical LED board without a kickboard, with ten hold sets.", "Decoy", "2022", "cbj")]},
 {"n": "Climbing brush", "a": "boar's hair brush · bouldering brush",
  "d": "Brush used to clean holds on boulders and routes.",
  "t": ["boar's hair", "horsehair", "nylon", "pole-mounted"],
  "s": "https://www.inglesport.com/product-category/climb/climbing-types/bouldering/",
  "x": [X("Lapis brush", "Popular small hold brush; the original has a plastic handle.", "Lapis", "", "lapis",
          [("Lapis Wooden Brush", "Lapis", "", "wider horsehair head, wooden handle, for slopers and volumes")])]},
]
def B(n, c, f, seg, kf, d, s="knowledge", sig=()):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "s": s}
    if sig: b["sig"] = list(sig)
    return b
brands = [
 B("Organic", "USA", "", "Artisan & independent", "crash pads", "American maker of crash pads and chalk bags.", sig=["Big Pad"]),
 B("Black Diamond", "USA", "1989", "Mainstream", "climbing gear", "American climbing and ski equipment maker in Salt Lake City.", sig=["Mondo"]),
 B("Metolius", "USA", "", "Specialist", "training boards, protection", "American climbing equipment maker.", sig=["Magnum"]),
 B("Mad Rock", "USA", "", "Value", "shoes, crash pads", "American climbing shoe and pad brand.", sig=["Duo"]),
 B("Beastmaker", "UK", "", "Artisan & independent", "wooden hangboards", "UK maker of wooden training boards, founded by climbers.", U["bm"], ["Beastmaker 1000", "Beastmaker 2000"]),
 B("Moon Climbing", "UK", "", "Specialist", "MoonBoard", "Ben Moon's climbing brand, maker of the MoonBoard.", sig=["MoonBoard"]),
 B("Tension Climbing", "USA", "", "Specialist", "training boards", "Maker of the Tension Board and wooden holds.", sig=["Tension Board"]),
 B("Kilter", "", "", "Specialist", "LED boards", "Maker of the Kilter Board, by Ian Powell and Jackie Hueftle.", U["cbj"], ["Kilter Board"]),
 B("Grasshopper", "", "", "Specialist", "board frames", "Boone Speed's adjustable board and frame maker.", U["cbj"], ["Grasshopper Board"]),
 B("Menagerie Climbing", "", "", "Specialist", "training boards", "Maker of the Woods Board.", U["led"], ["Woods Board"]),
 B("Decoy", "", "", "Specialist", "LED boards", "Dan Yagmin's board and hold maker.", U["cbj"], ["Decoy Board"]),
 B("Lapis", "", "", "Specialist", "climbing brushes", "Maker of the popular Lapis hold brush.", U["lapis"], ["Lapis brush"]),
]
notes = ("All 3 old kinds kept; new kind Climbing board added (source CBJ training-board survey). Metolius Simulator and Tension/Lattice hangboards not attested on a fetched page "
         "(snippets only), so left out. Some brand countries left blank where no retrieved page stated them. MoonBoard date: Wikipedia gives 2005 (Moon & Simpson), CBJ gives 2006; 2005 used.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = "/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/08_03.json"
json.dump(out, open(p + ".tmp", "w"), ensure_ascii=False, indent=1); os.replace(p + ".tmp", p)
print("ok")
