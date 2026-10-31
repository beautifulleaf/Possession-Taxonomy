import json, os
I = lambda *xs: [[x, "IKEA"] for x in xs]
jobs = {
"05_00": {"kinds": [
  {"n": "Storage box", "a": "storage bin · storage tub · toy box", "d": "A lidded or open box or bin made to hold several objects in a home.",
   "t": ["Plastic", "Fabric", "Cardboard", "Wood", "Lidded · open", "Stackable · underbed"],
   "s": "https://www.ikea.com/us/en/cat/storage-boxes-baskets-10550",
   "r": I("SAMLA", "TROFAST", "DRÖNA", "KUGGIS", "SMARRA")},
  {"n": "Storage basket", "a": "basket", "d": "A woven or wire basket made to hold several objects.",
   "t": ["Rattan, wicker or seagrass", "Wire", "Fabric or felt", "Plastic", "With handles · lidded"],
   "s": "https://www.ikea.com/us/en/cat/baskets-16201",
   "r": I("BRANÄS", "KNIPSA", "FLÅDIS", "LABBSAL", "JÄGMÄSTARE")},
  {"n": "Hanging organiser", "a": "hanging storage · hanging wardrobe organiser", "d": "A fabric unit of shelves, pockets or compartments that hangs from a rail, hook or door to store clothes and small items.",
   "t": ["Shoe bag", "Over-door organiser", "Wardrobe shelves"],
   "s": "https://www.ikea.com/us/en/cat/shoe-racks-stands-10454"}],
 "brands": [], "traditions": [],
 "notes": "Restraint only. Storage box: 7 IKEA ranges cut to 5 (dropped GÄRDESGÅRD, UPPDATERA); storage basket: 10 IKEA ranges cut to 5 (dropped BULLIG, GNABBAS, LUSTIGKURRE, TRUMMIS, ÅSUNDEN). Old data had no other makers, so no non-IKEA market leaders could be added without research; the choice among IKEA ranges is editorial, not test-based. Old model lists were range names, so they are kept as ranges (r). Shoe bag (k81) merged into Hanging organiser as a type with over-door organiser and wardrobe shelves; its old source (walmart hanging-shoe page) dropped in favour of k82's source. Material/size attributes moved into t. No web research, brands or traditions."},
"05_01": {"kinds": [
  {"n": "Coat rack", "a": "coat stand · hat stand · hall tree", "d": "A free-standing stand or wall rail of hooks for coats and hats.",
   "t": ["Free-standing stand", "Wall-mounted rail", "Hall tree with bench"],
   "s": "https://www.ikea.com/us/en/cat/clothes-racks-stands-10455",
   "r": I("HEMNES", "MACKAPÄR", "GRÅFJÄLLET", "PANGET", "BONDSKÄRET")},
  {"n": "Wall hook", "a": "coat hook · door hook · hook rail", "d": "A hook or row of hooks fixed to a wall or door for hanging things.",
   "t": ["Single hook", "Hook rail", "Over-door hook", "Adhesive hook"],
   "s": "https://www.ikea.com/us/en/cat/clothes-racks-stands-10455",
   "r": I("TJUSIG", "ÅRSJÖN", "LANDKRABBA", "GALTBOX")},
  {"n": "Shoe rack", "a": "shoe stand", "d": "An open rack of tiers that holds pairs of shoes.",
   "t": ["Floor-standing", "Wall-mounted", "Bench with shoe rack"],
   "s": "https://www.ikea.com/us/en/cat/shoe-racks-stands-10454",
   "r": I("TJUSIG", "VASSKÄR", "GREJIG", "MURVEL", "ÄLGANÄS")},
  {"n": "Clothes rail", "a": "clothes rack · garment rack", "d": "A freestanding frame with a hanging bar, often on castors, for clothes on hangers.",
   "t": ["On castors", "Fixed frame", "Double rail", "With shelf"],
   "s": "https://www.ikea.com/us/en/cat/clothes-racks-stands-10455"},
  {"n": "Clothes hanger", "a": "coat hanger · hanger", "d": "A shaped frame from which a garment hangs on a rail.",
   "t": ["Wood", "Plastic", "Velvet or flocked", "Wire", "Trouser · skirt · children's"],
   "s": "https://www.ikea.com/us/en/cat/hangers-20618/",
   "r": I("BUMERANG", "HÄNGA", "TRYSSE", "GÅRDSMÄSTARE")},
  {"n": "Umbrella stand", "a": "umbrella holder", "d": "A stand or holder that keeps several umbrellas upright, usually by a door.",
   "s": "https://www.google.com/basepages/producttype/taxonomy.en-US.txt"},
  {"n": "Wine rack", "a": "bottle rack", "d": "A free-standing or wall rack that holds wine bottles lying down.",
   "t": ["Free-standing", "Wall-mounted", "Countertop"],
   "s": "https://www.google.com/basepages/producttype/taxonomy.en-US.txt"},
  {"n": "Magazine rack", "a": "magazine holder · newspaper rack", "d": "A rack or holder for magazines and newspapers.",
   "s": "https://www.google.com/basepages/producttype/taxonomy.en-US.txt"}],
 "brands": [], "traditions": [],
 "notes": "Restraint only. All eight planned kinds kept with old sources. IKEA model lists (old m duplicated in r) kept once as ranges (r); coat rack cut from 7 to 5 (dropped KALLSÖ, NIPÅSEN), other lists were already 4-5 and kept. Old data had no non-IKEA makers, so none added (no research). Clothes rail, umbrella stand, wine rack, magazine rack stay kind-level with no models. Attribute variants as t. No brands or traditions."},
"07_00": {"kinds": [
  {"n": "Furniture spare parts", "a": "furniture replacement parts", "d": "Replacement parts made to repair or extend a piece of furniture.",
   "t": ["Bed slats", "Table legs", "Replacement shelves", "Hinges and fittings"],
   "s": "https://www.google.com/basepages/producttype/taxonomy.en-US.txt"}],
 "brands": [], "traditions": [],
 "notes": "Restraint only. Bed slats (k105), table leg (k107) and replacement shelf (k108) merged into one Furniture spare parts kind with these as types, plus hinges and fittings as planned. Kept the Google product taxonomy source shared by k107/k108; k105's IKEA mattresses URL dropped as off-topic. No models existed; none added."},
}
for job, data in jobs.items():
    p = f"work/B1/shelves/{job}.json"; tmp = p + ".tmp"
    with open(tmp, "w") as f: json.dump(data, f, ensure_ascii=False, indent=1)
    os.replace(tmp, p)
