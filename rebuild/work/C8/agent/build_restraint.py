import json, os, sys
B = '/home/user/Possession-Taxonomy/rebuild/work/C8/shelves/'
def K(n, d, s, a='', t=None, m=None, r=None):
    k = {"n": n, "a": a, "d": d}
    if t: k["t"] = t
    k["s"] = s
    if m: k["m"] = m
    if r: k["r"] = r
    return k
S = {}
S['04_01'] = ([
 K("Electric fence energiser", "Unit that sends pulses of current along an electric fence for farm, paddock or garden use.",
   "https://shop.wejameson.co.uk/collections/energisers", a="fence charger · fencer",
   m=[["Patura P1", "Patura"], ["Patura P35", "Patura"]]),
 K("Electric fence wire and insulators", "Conductive tape, wire or rope strung as an electric fence, and the insulators that hold it on posts.",
   "https://shop.wejameson.co.uk/collections/electric-fencing", a="electric fence tape · polywire · electric fence insulator",
   t=["polytape", "polywire", "rope", "ring insulator", "corner insulator", "strain insulator"],
   m=[["Patura Tornado XL Polywire", "Patura"], ["Patura Insultube", "Patura"]]),
], "Merged tape and insulator kinds (k38, k39); maker-less insulator models became types. Energiser list cut from four Patura SKUs to the smallest and largest (P1, P35); no other market brands added because this is a restraint-only pass with no research (Gallagher-type market leaders left for a later sourcing pass).")
S['05_01'] = ([
 K("Wood oil", "Penetrating oil finish that soaks into wood, for furniture, worktops and decking.",
   "https://www.screwfix.com/c/painting-decorating/wood-oil/cat850452", a="decking oil · furniture oil",
   t=["Danish oil", "linseed oil", "teak oil", "tung oil", "hardwax oil"],
   m=[["Wood Finishing Oil", "Osmo"], ["Water-Based Wax Oil", "Liberon"]]),
 K("Varnish", "Clear or tinted film-forming finish for wood.", "https://www.screwfix.com/c/painting-decorating/varnish/cat850450"),
 K("Wood stain", "Coloured finish that soaks into wood and shows its grain.", "https://www.screwfix.com/c/painting-decorating/wood-stain/cat850456"),
 K("Wood wax", "Wax finish rubbed into wood.", "https://www.screwfix.com/c/painting-decorating/wood-wax/cat9900006"),
 K("Exterior wood treatment", "Paint, stain or preservative that protects outdoor timber such as fences and sheds against rot, insects and weather.",
   "https://www.screwfix.com/c/painting-decorating/exterior-paint-woodcare/cat850186", a="fence paint · shed paint · wood preservative",
   t=["fence and shed paint", "preservative"]),
 K("Sandpaper", "Abrasive sheet or roll for hand or general use, not cut to fit one sander.", "https://www.screwfix.com/c/tools/hand-sanding/cat6160014", a="glasspaper · abrasive paper"),
], "Fence paint (k156) merged into Exterior wood treatment (kept wood preservative's source). Maker-less oil models became types (wax oil -> hardwax oil). Nothing dropped.")
S['06_00'] = ([
 K("Plumbing pipe", "Plumbing, heating, gas or water supply pipe of copper, plastic or steel, sold by length or coil.",
   "https://www.toolstation.com/plumbing/c15", t=["copper", "PEX", "polybutylene", "MDPE", "steel"]),
 K("Pipe fitting", "Elbow, tee, coupler or reducer that joins plumbing pipes, chosen by joint method.",
   "https://www.screwfix.com/c/heating-plumbing/pipe-fittings/cat831504", a="push-fit fitting · compression fitting · solder-ring fitting · end-feed fitting · press-fit fitting",
   t=["push-fit", "compression", "solder-ring", "end-feed", "press-fit"],
   m=[["JG Speedfit Plastic Push-Fit", "JG Speedfit"], ["Hep2O Keyless", "Hep2O"], ["Tectite Sprint Copper Push-Fit", "Tectite Sprint"]],
   r=[["JG Speedfit", "JG Speedfit"], ["Hep2O", "Hep2O"], ["Tectite Sprint", "Tectite Sprint"], ["B Press", "Conex Banninger"]]),
 K("Valve", "Valve that shuts off or controls flow in a pipe, or absorbs pressure shocks in it.",
   "https://www.screwfix.com/c/heating-plumbing/brassware-valves-taps/cat831576", a="stop cock · isolating valve · radiator valve",
   t=["stopcock", "isolating", "ball", "gate", "check", "pressure-reducing", "thermostatic mixing", "water hammer arrester"],
   m=[["PB300 Compression Ball Valve", "Pegler"], ["HX22 Ball Valve", "Hep2O"]]),
 K("Flexible hose", "Braided flexible hose with fittings that connects a tap, cistern or appliance to the supply pipe.",
   "https://www.toolstation.com/plumbing/c15", a="tap connector"),
 K("Pipe clip", "Clip or bracket that holds a pipe to a wall or joist.", "https://www.screwfix.com/c/heating-plumbing/pipe-clips/cat831642",
   m=[["Double Hinge Clip", "Talon"]]),
], "Five fitting-joint kinds (k102-k106) merged into Pipe fitting with joint types; water hammer arrester (k111) folded into Valve as a type; maker-less valve models became types. Fitting ranges kept once on Pipe fitting and removed from Valve (brand ranges repeated across kinds).")
S['06_01'] = ([
 K("Waste and trap", "Pipe, fitting and water-sealed trap for the waste outlet of a basin, sink or bath.",
   "https://www.screwfix.com/c/heating-plumbing/wastes-traps/cat2410005", a="waste fitting · trap"),
 K("Guttering", "Gutter and downpipe sections and fittings that carry rainwater from a roof.",
   "https://www.screwfix.com/c/heating-plumbing/guttering/cat831536", a="rainwater goods",
   t=["half round", "square line", "ogee", "deep flow", "cast iron"]),
 K("Soil and drain pipe", "Large-bore pipe and fittings that carry waste from toilets and drains to the sewer, above or below ground.", "https://www.toolstation.com/plumbing/c15"),
 K("Drainage channel", "Surface channel with a grating that collects water from a drive, patio or floor.", "https://www.toolstation.com/plumbing/c15"),
], "Waste fitting (k112) and trap (k113) merged; guttering profiles became types. Nothing dropped.")
S['07_00'] = ([
 K("Cable", "Fixed-wiring cable for mains circuits, including steel-wire armoured cable for burial or exposed runs.",
   "https://www.screwfix.com/c/electrical-lighting/cable/cat8960001", a="twin and earth · armoured cable",
   t=["twin and earth (6242Y)", "three-core and earth", "armoured (SWA)", "coaxial"],
   m=[["6943X Armoured Cable", "Prysmian"]]),
 K("Flex", "Flexible mains cord for connecting appliances and fittings.", "https://www.toolstation.com/electrical-supplies-accessories/c4"),
 K("Conduit and trunking", "Tube or lidded surface channel through which cables are run and hidden.",
   "https://www.toolstation.com/electrical-supplies-accessories/c4", a="conduit · trunking", t=["rigid conduit", "flexible conduit", "trunking"]),
 K("Junction box", "Enclosure in which mains cables are joined.", "https://www.toolstation.com/electrical-supplies-accessories/c4"),
 K("Cable clip", "Clip that fixes a cable to a wall or surface.", "https://www.screwfix.com/c/electrical-lighting/cable-clips/cat830572"),
 K("Cable tie", "Plastic or metal strap with a ratchet that bundles or fixes cables.", "https://www.toolstation.com/electrical-supplies-accessories/c4", a="zip tie"),
], "Armoured cable (k124) merged into Cable; conduit (k127) and trunking (k128) merged. Maker-less twin-and-earth model became a type. Nothing dropped.")
S['07_01'] = ([
 K("Extension lead", "Flex with a mains plug and one or more sockets, on a reel or not.",
   "https://www.screwfix.com/c/electrical-lighting/extension-leads/cat830084", t=["surge-protected", "reel", "USB", "smart"]),
 K("Mains plug", "Rewireable or moulded plug for a mains flex, of any national plug type.", "https://www.screwfix.com/c/electrical-lighting/electric-plugs/cat8800007"),
 K("Plug adaptor", "Plug-in unit that gives one socket-outlet two or more outlets or a different socket type.",
   "https://www.screwfix.com/c/electrical-lighting/electric-plugs/cat8800007", a="travel adaptor"),
 K("Fuse", "Cartridge or rewireable fuse that breaks a circuit on overload.", "https://www.screwfix.com/c/electrical-lighting/consumer-unit-fuses/cat13610001"),
], "Restraint only; no models existed. Nothing merged or dropped.")
S['08_01'] = ([
 K("Latch", "Catch that holds a door or gate shut without a key.", "https://toolstation.com/ironmongery/gate-hardware/c312",
   t=["ring", "thumb", "gate", "auto-locking"]),
 K("Door bolt", "Sliding bolt that secures a door or gate from one side.", "https://toolstation.com/security/padlock-bolts-hasps/c382?page=2",
   t=["tower", "surface", "Brenton"]),
 K("Hasp", "Hinged slotted plate and staple that take a padlock.", "https://toolstation.com/security/padlock-bolts-hasps/c382?page=2", a="hasp and staple"),
 K("Bracket", "General bracket or shelf support fixed to a wall or structure, not one made for a single screen or speaker.",
   "https://www.screwfix.com/c/security-ironmongery/shelf-brackets/cat880018", a="shelf support"),
 K("Safety sign", "Sign that gives a safety, fire, hazard or legal instruction.", "https://www.toolstation.com/help-and-advice/buying-guides/safety-signs-buying-guide", a="regulatory sign"),
], "Maker-less latch and bolt patterns became types. Nothing merged or dropped.")
S['09_00'] = ([
 K("Wood screw", "Tapered, coarse-threaded screw for fixing into timber and boards.", "https://www.toolstation.com/screws-fixings/wood-screws/c852",
   m=[["SPAX S Self Countersinking Pozi", "SPAX"], ["Forgefast Pozi Elite Performance", "Forgefix"], ["TimCo Solo", "TimCo"]],
   r=[["Wirox", "SPAX"], ["Forgefast", "Forgefix"]]),
 K("Decking screw", "Corrosion-resistant screw made to fix decking boards to joists.", "https://www.toolstation.com/screws-fixings/decking-roofing-screws/c301",
   t=["timber decking", "composite decking"]),
 K("Drywall screw", "Fine- or coarse-threaded bugle-head screw for fixing plasterboard to studs.", "https://www.toolstation.com/screws-fixings/drywall/c390",
   t=["fine thread", "coarse thread"]),
 K("Masonry screw", "Hardened screw that cuts its own thread into a drilled hole in masonry or concrete.", "https://www.toolstation.com/screws-fixings/masonry-screws/c856",
   a="concrete screw", m=[["Fischer FFS Frame Fixing Screw", "Fischer"], ["Rawlplug R-LX Concrete Screw Anchor", "Rawlplug"]]),
 K("Coach screw", "Heavy hexagon-head wood screw driven with a spanner for structural timber fixings.", "https://www.toolstation.com/screws-fixings/c12", a="lag screw"),
 K("Self-tapping screw", "Sheet-metal screw that forms its own thread, with or without a drill point.", "", a="self-drilling screw",
   t=["self-tapping", "self-drilling"]),
 K("Machine screw", "Parallel-threaded screw for a tapped hole or a nut.", "https://www.toolstation.com/screws-fixings/machine-screws/c76"),
], "Trimmed to the brief's market brands (SPAX, Forgefix, TimCo, Fischer, Rawlplug): dropped retailer-own-brand models Spectre Advanced Double Countersunk (wood screw), Deck-Tite Composite Plus (decking) and Ulti-Mate II drywall screw; dropped the Forgefast/Wirox ranges repeated on Decking screw (kept once on Wood screw). Self-tapping screw had no old source and keeps a blank s. No kinds dropped.")
S['09_01'] = ([
 K("Nail", "Steel pin with a head, driven by hammer or nail gun, loose or collated, into timber or masonry.",
   "https://www.toolstation.com/screws-fixings/nails-staples/c729", a="concrete nail · masonry nail",
   t=["round wire", "oval", "lost head", "annular ring", "clout", "panel pin", "veneer pin", "brad", "cut clasp", "masonry"]),
 K("Staple", "U-shaped wire fastener driven by a stapler or tacker.", "https://www.toolstation.com/screws-fixings/staples/c109",
   m=[["Tacwise 53 Series", "Tacwise"], ["Tacwise Type 91 Narrow Crown", "Tacwise"], ["DeWalt Narrow Crown SX Type", "DeWalt"]]),
], "Nail patterns became types; concrete nail (k67) merged in as the masonry type. Dropped the Don Quichotte masonry nail model (retailer house brand, F&F/Toolstation). Nothing else dropped.")
jobs = sys.argv[1:] or list(S)
for j in jobs:
    kinds, notes = S[j]
    p = B + j + '.json'; tmp = p + '.tmp'
    json.dump({"kinds": kinds, "brands": [], "traditions": [], "notes": notes}, open(tmp, 'w'), ensure_ascii=False, indent=1)
    os.replace(tmp, p)
