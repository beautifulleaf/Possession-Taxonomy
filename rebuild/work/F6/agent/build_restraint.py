import json, os
def K(n, a, d, s, t=None):
    k = {"n": n, "a": a, "d": d, "s": s}
    if t: k["t"] = t
    return k
p = "work/F6/shelves/08_00.json"; os.makedirs(os.path.dirname(p), exist_ok=True)
kinds = [
 K("Specimen display dome", "", "Glass or acrylic dome with a base, made to cover and display one specimen.", "https://store.smm.org/products/glass-dome-with-wood-base"),
 K("Specimen stand", "", "Stand or mount made to hold and display one specimen.", "https://zoicpaleotech.com/products/adjustable-acrylic-display-stand-large-76x102mm",
   t=["acrylic riser", "museum putty"]),
 K("Specimen frame case", "floating frame · Riker mount", "Glazed floating frame or case made to hold and display one specimen. One holding several, such as a Riker tray, is in Furniture & Storage.", "https://www.fossilera.com/fossils-for-sale"),
 K("Single-specimen box", "perky box · gem jar · thumbnail box", "Box made to hold one specimen. A box holding several is in Furniture & Storage.", "https://www.wardsci.com/us/en/product/8876861/hinged-perky-specimen-box"),
]
json.dump({"kinds": kinds, "brands": [], "traditions": [], "notes": "Restraint only: Riker mount added as frame-case alias; Perky box moved from models to an alias of Single-specimen box with gem jar and thumbnail box; acrylic risers and museum putty as stand types. No makers were present, none added; nothing dropped."}, open(p + ".tmp", "w"), ensure_ascii=False, indent=1)
os.replace(p + ".tmp", p)
