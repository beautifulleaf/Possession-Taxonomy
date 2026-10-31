import json, os, sys
def K(n, a, d, s, t=None, m=None):
    k = {"n": n, "a": a, "d": d, "s": s}
    if t: k["t"] = t
    if m: k["m"] = m
    return k
def W(code, job, kinds, notes):
    p = f"work/{code}/shelves/{job}.json"; os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + ".tmp"
    json.dump({"kinds": kinds, "brands": [], "traditions": [], "notes": notes}, open(tmp, "w"), ensure_ascii=False, indent=1)
    os.replace(tmp, p)
LM = "https://london-medals.co.uk/medal-mounting-and-framing/"
W("F3", "06_03", [
 K("Medal mounting bar and ribbon", "Ordenspange · Bandspange · medal bar · ribbon bar · medal ribbon",
   "Bar on which medals or their ribbons are mounted for wear, or a length of ribbon made for one medal.", LM,
   t=["court mounting", "swing mounting", "ribbon bar", "medal ribbon"]),
 K("Medal case", "", "Case made to hold one medal or decoration.",
   "https://www.usmint.gov/deluxe-black-presentation-case-for-3-inch-medal-N52.html"),
], "Merged medal bar and medal ribbon into one kind (court mounting, swing mounting, ribbon bar, medal ribbon as types). Dropped the US Mint presentation-case SKU as single-retailer noise.")
TM = "https://www.trophiesmedals.co.uk/shop"; CA = "https://www.crownawards.com/"
W("F3", "07_00", [
 K("Trophy cup", "perpetual cup", "Cup-shaped trophy on a base, perpetual cups included.", TM),
 K("Upright award", "", "Column, figure, star, block or obelisk award on a base.", CA),
 K("Award plaque or shield", "award plaque · award shield", "Flat or shield-shaped award panel with an inscription or plates for engraved names.", TM, t=["plaque", "shield"]),
 K("Bowl, tankard or salver", "", "Bowl, tankard, tray or salver given as an award.", TM),
 K("Rosette or ribbon", "", "Rosette or ribbon given as an award.", "https://hodgesbadge.com/collections/equestrian-awards/products/deluxe-wheaton-3-rosette-award-ribbon-6-1-2-top"),
 K("Championship belt", "", "Belt awarded to a champion.", CA, t=["replica championship belt"]),
 K("Championship ring", "", "Ring awarded to the members of a championship team or to a champion.", CA),
], "Dropped the trophy-shop ranges (Trophies Medals & More: Advocate, Colonial, Prestige, Revolution, Supreme, Ultimate Awards) and the Hodges Badge Company ranges and Deluxe Wheaton rosette SKU as SKU noise. Merged award shield and award plaque into one kind. Replica belts are a type of championship belt.")
