import json, os, sys
D = '/home/user/Possession-Taxonomy/rebuild/work/C2/shelves'
os.makedirs(D, exist_ok=True)
def K(n, a, d, s, m=None, r=None, t=None):
    k = {"n": n, "a": a, "d": d}
    if t: k["t"] = t
    k["s"] = s
    if m: k["m"] = m
    if r: k["r"] = r
    return k
LES = "https://lesliespool.com/"
jobs = {
"06_01": ([
  K("Fertiliser", "plant feed", "Product that supplies plant nutrients to soil or plants.", "https://www.uk.plantura.garden/collections/granular-fertilisers", t=["Granular", "Liquid", "Slow-release"]),
  K("Herbicide", "weed killer", "Product made to kill or control unwanted plants.", "https://www.bunnings.com.au/our-range/garden/gardening/garden-pest-weed-control",
    m=[["Roundup Total", "Roundup"], ["Roundup Pump N Go", "Roundup"], ["Zero Super Concentrate", "Yates"], ["Zero Rapid", "Yates"], ["Slasher", "OCP"]],
    r=[["Zero", "Yates"]], t=["Concentrate", "Ready-to-use"]),
  K("Insecticide", "pest killer", "Product that kills or repels insects and other pests on plants.", "https://www.bunnings.com.au/our-range/garden/gardening/garden-pest-weed-control",
    m=[["Pyrethrum Insect Pest Killer", "Yates"], ["Eco-Neem", "OCP"], ["Eco-Caterpillar-Killer", "OCP"], ["EarthCare White Oil", "Seasol"]]),
  K("Fungicide", "", "Product that prevents or treats fungal disease on plants.", "https://www.bunnings.com.au/our-range/garden/gardening/garden-pest-weed-control",
    m=[["Liquid Copper Fungicide", "Yates"]]),
  K("Garden sprayer", "pump sprayer", "Hand-pumped or powered sprayer for applying liquid feeds and plant-protection products.", "https://www.hozelock.com/product/pulsar-plus/",
    m=[["Pulsar Plus", "Hozelock"], ["360D Non-Chemical Hand Sprayer", "Nylex"], ["18V ONE+ Garden Sprayer", "Ryobi"]], t=["Hand sprayer", "Pressure sprayer", "Battery sprayer"]),
  K("Soil test kit", "", "Kit for testing garden soil for pH or nutrients.", "https://blomidonnurseries.com/webstore/garden-tools-and-supplies/planting-aids-and-accessories/soil-testing/soil-test-kit-40-tests-ph-n-p-k",
    m=[["Soil Test Kit 40 Tests (pH-N-P-K)", "Luster Leaf"]], t=["pH", "NPK"]),
 ], "All 6 old kinds kept. Herbicide trimmed from 7 to 5 models (Roundup Tough and Zero Big Gun dropped as near-duplicate SKUs of the same lines). No web research (restraint-only shelf)."),
"07_01": ([
  K("Grow light", "", "Lamp made to give light for plant growth.", "https://www.spider-farmer.com/product-tag/100-200-watts/",
    r=[["SF Series", "Spider Farmer"]], t=["LED", "HPS", "CMH", "Fluorescent"]),
  K("Grow tent", "", "Lightproof reflective fabric tent on a frame for growing plants indoors under lights.", "https://www.spider-farmer.com/product-tag/100-200-watts/"),
  K("Propagator", "", "Covered tray for raising seeds and cuttings.", "https://www.worm.co.uk/pages/vitopod",
    m=[["Vitopod Propagator", "Vitopod"]], t=["Heated", "Unheated"]),
  K("Hydroponic system", "", "System that grows plants without soil, roots fed by a nutrient solution.", "https://tools.woot.com/offers/aerogarden-bounty-basic-indoor-garden",
    m=[["Bounty Basic", "AeroGarden"]]),
  K("Grow environment controller", "", "Controller that switches the lights, fans and humidity devices of a grow tent or room on set values.", "https://hydrobuilder.com/collections/shop-all-grow-tent-packages"),
 ], "All 5 old kinds kept. Grow light: four Spider Farmer SKUs (SF1000, SF1000D, SF2000, SF2000Pro) collapsed into the SF Series range per the 'ranges not SKU lists' brief; lamp technologies moved to types. No web research (restraint-only shelf)."),
"08_00": ([
  K("Leaf blower", "blower-vac", "Powered machine that blows leaves and debris into heaps; a blower-vac also sucks and shreds.", "https://www.diy.com/landingpage/outdoor-garden/garden-tools",
    m=[["BGA 60", "STIHL"], ["BGA 300", "STIHL"], ["BRA 600", "STIHL"], ["SHA 56", "STIHL"], ["230iB", "Husqvarna"], ["350iB Leaf Blaster", "Husqvarna"], ["570iBT", "Husqvarna"], ["PowerVac 3000", "Flymo"], ["24V Axial Blower", "Greenworks"]],
    t=["Handheld", "Backpack", "Blower-vac"]),
  K("Leaf rake", "", "Wide fan-shaped rake with springy tines for gathering leaves and debris.", "https://www.hornbach.de/c/garten/gartenwerkzeug-gartengeraete/S1943/",
    m=[["combisystem Rechenbesen", "Gardena"]], r=[["combisystem", "Gardena"]]),
  K("Wheelbarrow", "garden cart", "Wheeled container with handles for carrying soil, waste and materials in a garden.", "https://www.diy.com/landingpage/outdoor-garden/garden-tools",
    m=[["Expert", "Haemmerlin"], ["County", "Haemmerlin"], ["Colossus", "Haemmerlin"], ["Vibrante GO", "Haemmerlin"], ["King Tipper", "Carrimore"]]),
  K("Pressure washer", "", "Powered pump that sprays water at high pressure to clean paths, patios and vehicles.", "https://www.diy.com/landingpage/outdoor-garden/garden-tools",
    m=[["K 5 Classic", "Karcher"], ["RE 90", "STIHL"], ["RE 120 PLUS", "STIHL"], ["RCA 20", "STIHL"], ["Go P40", "AVA"], ["Evolution P60", "AVA"]]),
  K("Garden shredder", "", "Machine that shreds garden prunings and green waste into small pieces.", "https://www.benburgess.co.uk/shop/category/commercial-machinery/ride-on-lawn-mowers",
    m=[["GHE 105", "STIHL"], ["GHE 135 L", "STIHL"], ["GHE 150", "STIHL"], ["GHE 250 S", "STIHL"]], t=["Impact", "Quiet / roller"]),
  K("Wood chipper", "", "Engine or electric chipper that turns branches and brush into chips, not tractor-driven or towed.", "https://www.benburgess.co.uk/shop/category/commercial-machinery/ride-on-lawn-mowers",
    m=[["CSV-2515", "Patriot Products"], ["CSV-3090H", "Patriot Products"]]),
 ], "All 6 old kinds kept (stump grinder was never on this shelf; dropped by plan as hire/trade machinery). Leaf blower trimmed 10->9 (BGA 30 dropped as a near-duplicate of BGA 60); pressure washer 7->6 (RB 400 dropped as a petrol trade unit); wood chipper 4->2 (two Patriot models kept to show the electric/petrol span). Old models only; no web research."),
"08_01": ([
  K("Snow shovel", "snow pusher", "Wide-bladed hand shovel or pusher for clearing snow.", "https://www.hornbach.de/c/garten/gartenwerkzeug-gartengeraete/S1943/",
    m=[["Victoria", "Freund"], ["combisystem Schneeschieber", "Gardena"]], r=[["combisystem", "Gardena"]], t=["Shovel", "Pusher"]),
  K("Snow blower", "snow thrower", "Powered machine that gathers snow and throws it clear of a path or drive.", "https://www.husqvarna.com/us/snow-blowers",
    m=[["ST 124", "Husqvarna"], ["ST 224", "Husqvarna"], ["ST 424", "Husqvarna"]],
    r=[["Path-Pro", "Ariens"], ["Compact", "Ariens"], ["Deluxe", "Ariens"], ["Platinum", "Ariens"], ["Professional", "Ariens"]], t=["Single-stage", "Two-stage"]),
 ], "Both old kinds kept. Snow blower: Ariens ranges trimmed 7->5 (Classic and Track dropped as minor variants). No web research."),
"09_00": ([
  K("Above-ground pool", "", "Framed swimming pool that stands on the ground.", LES + "soft-sided-pools/",
    m=[["Power Steel", "Bestway"], ["Prism Frame", "Intex"]], t=["Steel frame", "Metal wall"]),
  K("Soft-sided pool", "", "Swimming pool with flexible walls, held up by an inflatable ring or by the water.", LES + "soft-sided-pools/",
    m=[["Fast Set", "Bestway"]], t=["Inflatable ring", "Paddling pool"]),
  K("Pool cover", "", "Cover laid over a pool to keep out debris, hold heat or make it safe.", LES + "pool-covers/",
    t=["Solar cover", "Winter cover", "Safety cover"]),
 ], "All 3 old kinds kept. Duplicate Bestway Power Steel range entry removed (already a model). No web research."),
"09_01": ([
  K("Pool pump", "", "Pump that circulates pool water through the filter.", LES + "pool-pumps/",
    m=[["IntelliFlo", "Pentair"], ["WhisperFlo", "Pentair"], ["SuperFlo", "Pentair"], ["Super Pump", "Hayward"], ["TriStar", "Hayward"], ["Max-Flo", "Hayward"], ["Power-Flo LX", "Hayward"], ["Protege", "Raypak"], ["Power Defender", "Waterway"]],
    t=["Single-speed", "Variable-speed", "Above-ground"]),
  K("Pool filter", "", "Unit that strains dirt from circulating pool water through sand, a pleated cartridge or diatomaceous-earth grids.", LES + "filter-cartridges/",
    m=[["Pro Series", "Hayward"], ["Sand Dollar", "Pentair"], ["Triton II", "Pentair"], ["Star-Clear", "Hayward"], ["Clean & Clear Plus", "Pentair"], ["SwimClear", "Hayward"], ["Pro-Grid", "Hayward"], ["Quad DE", "Pentair"], ["FNS Plus", "Pentair"], ["Crystal Water", "Waterway"]],
    r=[["Elite Replacement Cartridge", "Leslie's"]],
    t=["Sand filter", "Cartridge filter", "DE filter", "Spare parts: replacement cartridges, DE grids"]),
  K("Salt chlorinator", "salt cell", "Device that makes chlorine by electrolysis from salt dissolved in pool water.", LES + "salt-systems/",
    m=[["AquaRite", "Hayward"], ["SwimPure Plus", "Hayward"], ["AquaTrol", "Hayward"], ["Salt & Swim", "Hayward"], ["IntelliChlor", "Pentair"], ["AquaPure", "Jandy"]]),
  K("Pool heater", "pool heat pump", "Gas, electric, solar or heat-pump heater that warms pool water.", LES + "pool-heating/",
    m=[["MasterTemp", "Pentair"], ["Universal H-Series", "Hayward"], ["Digital", "Raypak"], ["HeatPro", "Hayward"], ["Crosswind", "Raypak"], ["Traditional Series", "Intermatic"]],
    t=["Gas", "Electric", "Solar", "Heat pump"]),
 ], "4 kinds from 7 old: pool filter cartridge and DE filter grid merged into Pool filter as spare parts; pool heat pump merged into Pool heater as a type. Pool filter had no old 's'; it takes the merged cartridge kind's old Leslie's source. Pump trimmed 11->9 (PowerFlo Matrix, Mustang dropped); filter 12->10 (Tagelus, Clean & Clear dropped as near-duplicates); duplicate model/range entries removed. No web research."),
"09_02": ([
  K("Robotic pool cleaner", "", "Self-powered cleaner with its own motor that scrubs and vacuums the pool.", LES + "automatic-pool-cleaners/",
    m=[["Proteus DX3", "Dolphin"], ["Proteus DX5i", "Dolphin"], ["Wave 60", "Dolphin"], ["FREEDOM", "Polaris"], ["VRX iQ+", "Polaris"], ["PCX 868 iQ", "Polaris"], ["Sol", "Aqua Products"]],
    r=[["Proteus", "Dolphin"], ["FREEDOM", "Polaris"]]),
  K("Suction-side pool cleaner", "", "Cleaner driven by the suction of the pool pump.", LES + "automatic-pool-cleaners/",
    m=[["PoolCleaner 2x", "Hayward"], ["PoolCleaner 4x", "Hayward"], ["Navigator Pro", "Hayward"], ["TracVac", "Hayward"], ["Kreepy Krauly Kruiser", "Pentair"], ["'Lil Rebel", "Pentair"], ["Sand Shark", "Kreepy Krauly"], ["MAXX", "Polaris"], ["MX6", "Zodiac"], ["G3", "Zodiac"]],
    r=[["PoolCleaner", "Hayward"]]),
  K("Pressure-side pool cleaner", "", "Cleaner driven by water pressure from the pool's return line or a booster pump.", LES + "automatic-pool-cleaners/",
    m=[["Polaris 280", "Polaris"], ["Polaris 380", "Polaris"], ["Polaris 3900 Sport", "Polaris"], ["Polaris QUATTRO T2", "Polaris"], ["Polaris P39", "Polaris"]],
    t=["Booster-pump driven", "Return-line driven", "Accessory: booster pump"]),
  K("Robotic pool skimmer", "solar pool skimmer", "Self-powered, often solar, floating robot that skims debris from the water surface.", LES + "automatic-pool-cleaners/"),
  K("Pool sanitiser", "pool chlorine", "Chemical that disinfects pool water, such as chlorine tablets or granules.", LES + "leslies-3-inch-jumbo-pool-chlorine-tablets-10-lbs-bucket/13072.html",
    t=["Chlorine tablets", "Chlorine granules"]),
  K("Pool test kit", "", "Kit for testing pool water for chlorine, pH and other values.", LES + "taylor-k-2006-complete-pool-water-test-kit/81329.html",
    m=[["K-2006 Complete Pool Water Test Kit", "Taylor Technologies"]]),
 ], "6 kinds from 7 old: pool cleaner booster pump merged into Pressure-side pool cleaner as an accessory type. Robotic cleaner trimmed 10->7, suction-side 14->10, pressure-side 6->5 (near-duplicate generations and toy-like units such as Wanda the Whale, Pool Vac XL dropped). Old models only; no web research."),
}
for job in (sys.argv[1:] or jobs):
    kinds, notes = jobs[job]
    p = os.path.join(D, job + '.json'); tmp = p + '.tmp'
    json.dump({"kinds": kinds, "brands": [], "traditions": [], "notes": notes}, open(tmp, 'w'), ensure_ascii=False, indent=1)
    os.replace(tmp, p)
