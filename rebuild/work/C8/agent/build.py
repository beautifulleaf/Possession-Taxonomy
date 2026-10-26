import json, os, sys
D = 'work/C8/shelves'
TH = "https://www.toolstation.com/screws-fixings/fixings-fasteners/c730"
TU = "https://www.tooled-up.com/adhesives/cat/100345"
HO = "https://www.huntoffice.ie/packing-supplies.html"
M10 = "https://www.mitre10.co.nz/shop/outdoor-bbq/bbqs-accessories/bbq-accessories/gas-bottles-charcoal/c/RF5464"
def K(n,a,d,s,t=None,m=None,r=None):
    k={"n":n,"a":a,"d":d}
    if t: k["t"]=t
    k["s"]=s
    if m: k["m"]=m
    if r: k["r"]=r
    return k
jobs = {
"09_02": ([
 K("Bolt","","Threaded fastener with a head, used with a nut; its strength is shown as a property class.","https://www.toolstation.com/screws-fixings/c12",t=["Coach bolt","Roof bolt","Hexagon bolt"]),
 K("Nut","","Internally threaded fastener that mates with a bolt or stud.","https://www.toolstation.com/screws-fixings/nuts-washers/c77",t=["Hexagon nut","Nylon lock nut","Connector nut"]),
 K("Washer","","Flat or spring ring set under a nut or head to spread load or lock it.","https://www.toolstation.com/screws-fixings/nuts-washers/c77",t=["Flat washer","Penny washer","Repair washer","Spring washer"]),
 K("Rivet","pop rivet · blind rivet","Fastener set by deforming its tail, including blind (pop) rivets.","https://www.toolstation.com/screws-fixings/rivets/c103"),
], "All four kinds kept; old blank-maker models (coach/roof bolt, hexagon/nylon lock/connector nut, penny/repair washer) became types. No models remain."),
"09_03": ([
 K("Wall plug","rawlplug · anchor plug","Plastic or fibre sleeve that expands in a drilled hole to hold a screw.",TH,m=[["Fischer Duopower","Fischer"],["Fischer UX-R","Fischer"],["Rawlplug UNO","Rawlplug"],["Rawlplug 4ALL","Rawlplug"]]),
 K("Cavity fixing","hollow-wall fixing · plasterboard fixing","Fixing that opens or grips behind a hollow wall or board.",TH,t=["Spring toggle","Self-drill plasterboard fixing","Metal cavity anchor"],m=[["GripIt Plasterboard Fixing","GripIt"],["Rawlplug Interset","Rawlplug"],["Rawlplug DRA02","Rawlplug"],["Driva-Loc","Deltaleigh"]]),
 K("Frame fixing","","Long plug and screw that fix a frame through to masonry in one pass.",TH,m=[["Fischer SRS","Fischer"],["Rawlplug KKS-R","Rawlplug"]]),
 K("Steel anchor","anchor bolt · throughbolt","Metal expansion anchor or anchor bolt for heavy fixings in concrete or masonry.",TH,t=["Shield anchor","Throughbolt"],m=[["Fischer FXA Throughbolt","Fischer"],["Rawlplug RBL2 Rawlbolt","Rawlplug"]]),
 K("Chemical anchor","resin anchor","Resin cartridge or capsule that bonds a stud or bar into a drilled hole; resin sold alone is included.","https://www.toolstation.com/screws-fixings/chemical-fixings/c102",m=[["Fischer FIP 300 SF","Fischer"],["Rawlplug R-KEM-II","Rawlplug"],["Rawlplug R-KER II","Rawlplug"],["Everbuild Anchorset Green 300","Everbuild"]]),
], "All five kinds kept. Blank-maker models (spring toggle, shield anchor) became types; branded models from the old data kept (Fischer, Rawlplug, GripIt, Deltaleigh, Everbuild)."),
"09_04": ([
 K("Timber connector","joist hanger · framing connector","Pressed-steel plate, hanger or bracket that joins timber members.","https://www.sydenhams.co.uk/shop-by-brand/simpson_strong_tie",t=["Joist hanger","Truss clip","Nail plate"],m=[["Simpson Strong-Tie JHA270","Simpson Strong-Tie"],["Simpson Strong-Tie JHM","Simpson Strong-Tie"]]),
 K("Post support","post spike · post shoe","Metal shoe, spike or base that holds a post in the ground or on a surface.","https://www.toolstation.com/brands/powapost",t=["Drive-in spike","Bolt-down base","Concrete-in shoe"],m=[["Powapost EasyGrip Post Spike","Powapost"],["Simpson Outdoor Accents Adjustable Post Base","Simpson Strong-Tie"]],r=[["Powapost","Powapost"]]),
 K("Dowel","dowel pin","Wooden, plastic or metal pin set into holes to join or align two parts.","https://www.toolstation.com/power-tool-accessories/dowels-biscuits/c87",t=["Fluted dowel pin","Spiral dowel pin","Dowel rod"]),
 K("Jointing biscuit","biscuit","Compressed wooden wafer glued into matching slots to join two boards.","https://www.toolstation.com/power-tool-accessories/dowels-biscuits/c87"),
], "All four kinds kept. Blank-maker models (joist hanger, fluted and spiral dowel pins) became types. The Powapost range now sits only under Post support (it was repeated under Timber connector)."),
"10_00": ([
 K("Grab adhesive","instant grab adhesive · no-nails adhesive","High-tack construction adhesive from a cartridge that holds on contact.","https://toolstation.com/adhesives-sealants/grab-adhesive/c403",m=[["CT1 Adhesive & Sealant","CT1"],["Evo-Stik Gripfill","Evo-Stik"],["Evo-Stik Sticks Like Sh*t","Evo-Stik"],["Pinkgrip","Everbuild"],["Sika Stixall","Sika"],["Sika Instant Nails","Sika"],["Soudal Fix All High Tack","Soudal"],["C-Tec Power Grab n Bond","C-Tec"]]),
 K("Wood glue","PVA","Adhesive made to bond wood, usually PVA.","https://www.tooled-up.com/adhesives/cat/100345",t=["Interior PVA","Weatherproof wood adhesive","Resin wood adhesive"],m=[["Evo-Stik Weatherproof Wood Adhesive","Evo-Stik"],["Evo-Stik Resin Wood Adhesive","Evo-Stik"],["Gorilla PVA Wood Glue","Gorilla Glue"],["Everbuild All Purpose Weatherproof Wood Adhesive","Everbuild"]]),
 K("All-purpose glue","general adhesive","General-purpose glue for household and building repairs.",TU,t=["PVA bond","Polyurethane glue"],m=[["Evo-Stik Super Concentrate PVA","Evo-Stik"],["Everbuild Universal PVA Bond","Everbuild"],["SikaBond PVA+","Sika"],["Gorilla General Purpose Waterproof Glue","Gorilla Glue"]]),
 K("Contact and spray adhesive","contact adhesive · impact adhesive · spray adhesive","Adhesive spread or sprayed on both surfaces that bonds on contact once touch-dry.",TU,t=["Contact (impact) adhesive in tin or tube","Aerosol spray adhesive"]),
 K("Flooring adhesive","","Adhesive for laying vinyl, wood or other floor coverings.",TU,t=["Vinyl flooring adhesive","Wood flooring adhesive"]),
 K("Wallpaper adhesive","wallpaper paste","Paste for hanging wallpaper.",TU,t=["Powder paste","Ready-mixed paste"],m=[["Solvite All Purpose Wallpaper Adhesive Paste","Solvite"]]),
], "Six kinds from seven: Contact adhesive and Spray adhesive merged into Contact and spray adhesive. Grab adhesive trimmed from 11 to 8 models (dropped Evo-Stik The Dog's, Sika Multi Stick, Soudal Fix All Turbo as duplicate lines of brands already listed)."),
"10_01": ([
 K("Sealant","caulk · silicone","Flexible compound that seals joints and gaps against water and air.","https://www.toolstation.com/adhesives-sealants/sealants/c658?page=1",t=["Sanitary silicone","Frame silicone","Decorators' caulk","Polyurethane","Hybrid"],m=[["Dowsil DC785+ Sanitary Silicone Sealant","Dowsil"],["SikaSeal Sanitary Silicone","Sika"],["Sika Silicone 825","Sika"],["Bostik Pro S41 Window & Door Frame Silicone","Bostik"],["Bostik Pro PU91 Polyurethane Construction Sealant","Bostik"],["Mapesil AC Zero","Mapei"],["Evo-Stik Trade Building Silicone","Evo-Stik"],["Soudal Trade All Weather Sealant","Soudal"]]),
 K("Tile adhesive","","Adhesive for fixing wall and floor tiles.",TU,t=["Ready-mixed","Powder"],m=[["Mapei Keraquick Easy S1","Mapei"],["Mapei Adesilex P9 Express","Mapei"],["Mapei Ultimate Showerproof Wall Tile Adhesive","Mapei"],["Mapei Trade Super Grab Tile Adhesive","Mapei"],["Evo-Stik Tile A Wall","Evo-Stik"],["Everbuild Mould Resistant Fix and Grout","Everbuild"]]),
 K("Tile grout","grout","Compound that fills the joints between tiles.","https://www.toolstation.com/brands/mapei",m=[["Mapei Ultracolor Plus","Mapei"]]),
 K("Expanding foam","PU foam · gap filler","Polyurethane foam from a can or gun that expands to fill and seal gaps.","https://toolstation.com/adhesives-sealants/grab-adhesive/c403",t=["Hand-held can","Gun-grade"]),
 K("Duct tape","cloth tape · gaffer tape","Strong cloth-backed adhesive tape for repairs and sealing.","https://www.huntoffice.ie/packing-supplies.html"),
], "All five kinds kept; sealant formulations listed as types. Models unchanged from the old data (all within the 12 limit)."),
"10_02": ([
 K("Packing box","moving box · removal box","Cardboard box sold flat for packing or moving; storage boxes are in Furniture & Storage.",HO,t=["Single wall","Double wall","Wardrobe box"]),
 K("Parcel tape","packing tape","Wide adhesive tape for sealing parcels and boxes.",HO,t=["Polypropylene","Vinyl","Paper"]),
 K("Tape dispenser","tape gun","Hand dispenser with a cutting edge that lays parcel tape on boxes.",HO),
 K("Bubble wrap","bubble film","Plastic sheet of air bubbles for cushioning goods.",HO,m=[["Sealed Air AirCap","Sealed Air"]]),
 K("Packing fill","void fill · foam packing","Loose fill, paper, air pillows or foam packed round goods in a box.","https://www.ipack.com/solutions/packaging-supplies-materials",t=["Loose fill","Paper","Air pillows","Foam sheet and corners"]),
], "Five kinds from six: Void fill and Foam packing merged into Packing fill (types: loose fill, paper, air pillows, foam sheet and corners). Stretch film and strapping were not in this shelf's old data; per the brief they are trade/warehouse supplies and stay out."),
"12_00": ([
 K("LPG cylinder","propane bottle · butane bottle · gas bottle","Refillable propane or butane bottle, owned or leased; gas type and valve type vary.",M10,t=["Propane","Butane","Patio gas"]),
 K("Gas canister","camping gas","Small disposable gas canister for stoves, torches and lighters.","https://www.bbqworld.co.uk/m/browse/charcoal.asp",t=["Pierceable","Screw-thread valve","Click-on valve"],m=[["Campingaz CV 300 Plus","Campingaz"],["Coleman C500","Coleman"]]),
 K("LPG regulator","gas regulator","Valve fitted to a gas cylinder that lowers its pressure for an appliance, sold with or without hose.",M10,t=["Propane","Butane"]),
 K("Fuel can","jerry can · petrol can","Container made to carry and store fuel.","https://www.tooled-up.com/jerry-cans/cat/2000104/",t=["Metal jerry can","Plastic fuel can"]),
 K("Lubricant","oil · grease · penetrating oil","General oil, grease or penetrating lubricant sold in a can or tube.","https://www.screwfix.com/c/automotive/automotive-lubricants/cat810058",t=["Multi-use oil","Penetrating oil","Silicone lubricant","Grease"],m=[["WD-40 Multi-Use Lubricant","WD-40"],["WD-40 Penetrant","WD-40"],["WD-40 Silicone Lubricant","WD-40"],["PlusGas Formula A Dismantling Lubricant","PlusGas"],["OB41 Multi-Use Penetrating Oil Spray","OB41"]]),
], "All five kinds kept with their old models; attribute variants added as types."),
"12_02": ([
 K("Firelighter","fire starter","Block, cube or bag of fuel made to start a fire.","https://www.tesco.com/groceries/en-GB/products/314107982",t=["Paraffin cube","Odourless","Natural wood wool"],m=[["Zip Odourless Firelighters","Zip"]]),
 K("Match","matches","Safety or strike-anywhere match.","https://www.ocado.com/products/swan-vestas-matches/543662011",t=["Safety match","Strike-anywhere match","Long fireplace match"],m=[["Swan Vestas","Republic Technologies (UK) Limited"]]),
 K("Utility lighter","long lighter · candle lighter","Long-nozzle lighter for barbecues, stoves, fires and candles; pocket lighters are in Smoking & Vaping.","https://Tractorsupply.Com/tsc/product/scripto-aim-n-flame-ii-xtra-long-utility-lighter",t=["Long-nozzle butane","Rechargeable arc","Candle lighter"],m=[["Scripto Aim n Flame II Xtra Long Utility Lighter","Scripto"]]),
 K("Lighter fluid","","Liquid fuel for refilling lighters or lighting barbecues.",M10,t=["Butane refill","Naphtha lighter fluid","Barbecue lighter fluid"]),
], "Four kinds from five: Candle lighter merged into Utility lighter as a type. Lighter flints were not in this shelf's old data; per the brief they belong with pocket lighters in Smoking & Vaping."),
}
for j in (sys.argv[1:] or jobs):
    k,n = jobs[j]
    p=f"{D}/{j}.json"; tmp=p+".tmp"
    with open(tmp,'w') as f: json.dump({"kinds":k,"brands":[],"traditions":[],"notes":n},f,ensure_ascii=False,indent=1)
    os.replace(tmp,p)
