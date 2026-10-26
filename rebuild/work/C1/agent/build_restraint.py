import json, os
D = '/home/user/Possession-Taxonomy/rebuild/work/C1/shelves'
def K(n, a, d, s, m=None, r=None, t=None):
    k = {"n": n, "a": a, "d": d}
    if t: k["t"] = t
    if s: k["s"] = s
    if m: k["m"] = m
    if r: k["r"] = r
    return k
TS = "https://www.toolstation.com/power-tools/"
J = {}
J["00_01"] = ([
 K("Drill driver","drill/driver · cordless drill","Hand-held rotary tool with a chuck and clutch for drilling holes and driving screws.",TS+"drill-drivers/c768",
   [["GSR 12V-32","Bosch"],["DCD791","DeWalt"],["DCD803","DeWalt"],["DCD701","DeWalt"],["M12 FUEL FDD2","Milwaukee"],["M12BLDDRC","Milwaukee"],["M18 Right Angle Drill Driver C18RAD","Milwaukee"],["Blueprint 12V Multi-Drill","Dremel"]],
   t=["12 V compact","18 V","right-angle"]),
 K("Combi (hammer) drill","hammer drill · combi drill","Drill driver with an added hammer action and an ordinary chuck, for drilling masonry as well as wood and metal.","https://toolstation.com/power-tools/impact-drill/c1159",
   [["DWD024","DeWalt"]], t=["corded","cordless"]),
 K("Impact driver","","Hand-held power driver with a rotary impact mechanism and a quarter-inch hex bit holder, for driving long screws.",TS+"impact-drivers-wrenches/c551",
   [["DCF850","DeWalt"],["DCF887","DeWalt"],["DCF809","DeWalt"],["M18 FID3","Milwaukee"],["M12FID2","Milwaukee"],["DTD173","Makita"],["TD111D","Makita"],["GDR 12V-110","Bosch"],["RID18","Ryobi"]],
   t=["standard impact","hydraulic (oil-pulse)"]),
 K("Rotary hammer","SDS drill","Hand-held tool with an electro-pneumatic hammer mechanism and an SDS-type bit holder, for heavy drilling and chiselling in masonry.",TS+"sds-drills/c514",
   [["D25133K","DeWalt"],["DCH273","DeWalt"],["DCH481","DeWalt"],["HR2670","Makita"],["M18FH","Milwaukee"],["M18BLHX","Milwaukee"],["GBH 18V-22 X","Bosch"],["R18SDS","Ryobi"]],
   t=["SDS-plus","SDS-max","corded","cordless"]),
 K("Impact wrench","","Power wrench with an impact mechanism and a square drive, for sockets on heavy nuts and bolts.",TS+"impact-drivers-wrenches/c551",
   [["DCF900","DeWalt"],["DCF922","DeWalt"],["DCF921","DeWalt"],["DCF923","DeWalt"],["M18 ONEFHIWF12","Milwaukee"],["M18FMTIW2F12","Milwaukee"],["M12FCIWF38","Milwaukee"]],
   t=["3/8-inch drive","1/2-inch drive","mid-torque","high-torque","right-angle"]),
 K("Electric screwdriver","","Small powered driver for light screwdriving, without an impact mechanism.","https://toolstation.com/power-tools/impact-driver/c1210",
   [["DCF601","DeWalt"]]),
 K("Demolition hammer","breaker · jack hammer","Powered tool that drives a chisel or point by hammer blows alone, without rotation, to break concrete, masonry and tile.","https://gigatools.ph/products/makita-hm1214c-sds-max-demolition-hammer-1500w",
   [["HM1214C","Makita"]], t=["electric","petrol","pneumatic"]),
 K("Magnetic drill","mag drill","Portable drill press on an electromagnetic base that clamps to steel, usually with annular cutters.",TS+"bench-tools/c335"),
], "Restraint only. Dropped all battery-platform ranges (18V XR, M12/M18 FUEL, 18V LXT, 12V CXT, 18V ONE+, FlexVolt), now held in Battery platforms. Drill driver: right-angle as a type. Impact driver: trimmed DCF870 and M12 SURGE into the type 'hydraulic (oil-pulse)'. Rotary hammer: trimmed D25033K, DCH263, DCH333, M18BH (12 to 8). Impact wrench: dropped DCF897 and M12 FRAIWF12 (right-angle kept as a type). Magnetic drill kept kind-level with no models (trade tool); Milwaukee M18 FMDP dropped. Model names stripped of repeated maker words.")
J["00_02"] = ([
 K("Circular saw","","Hand-held power saw with a rotating toothed disc, for straight cuts in timber and sheet.",TS+"saws/c722",
   [["DCS391","DeWalt"],["DWE560","DeWalt"],["M18BLCS66","Milwaukee"],["HD18CS","Milwaukee"],["R185CCS","Evolution"],["R18CS","Ryobi"]], t=["corded","cordless"]),
 K("Jigsaw","","Hand-held power saw with a short, vertically reciprocating blade, for curves and cut-outs.",TS+"saws/c722",[["M18BJS","Milwaukee"]], t=["corded","cordless"]),
 K("Mitre saw","chop saw · compound mitre saw","Power saw with its blade on a pivoting arm over a table, for crosscuts and angled cuts.",TS+"saws/c722",
   [["KAPEX KS 120 REB","Festool"],["DWS780","DeWalt"],["DWS727","DeWalt"],["DCS777","DeWalt"],["LS1219L","Makita"],["GCM 12 GDL","Bosch"],["GCM 8 SDE","Bosch"],["R255SMS+","Evolution"]],
   t=["compound","sliding compound","cordless"]),
 K("Track saw","plunge saw","Circular saw whose blade plunges from a sprung housing and that runs on a guide rail, for straight sheet cuts.",TS+"saws/c722"),
 K("Reciprocating saw","recip saw · sabre saw","Hand-held power saw with a long blade driven back and forth in line with the body, for demolition and rough cuts.",TS+"saws/c722"),
 K("Cut-off saw","disc cutter · concrete saw","Hand-held engine or electric saw with a large abrasive or diamond disc behind a guard, for concrete, stone and steel.",TS+"saws/c722", t=["petrol","electric","cordless"]),
 K("Wall chaser","chasing saw","Hand-held machine with twin diamond discs that cuts parallel channels in masonry for cables and pipes.",TS+"angle-grinders/c378"),
], "Restraint only. Dropped platform ranges (18V ONE+, 18V XR, M18 FUEL, FlexVolt 54V) and the KAPEX range (its model stays). Mitre saw trimmed 11 to 8 (dropped GCM 12 SDE, KAPEX KS 60 E, LS0815FL); sliding and compound are types. Cut-off saw and wall chaser joined from the old breakers shelf, kind-level.")
J["00_03"] = ([
 K("Angle grinder","","Hand-held power tool with a disc on a right-angle head, for grinding and cutting.",TS+"angle-grinders/c378",
   [["DCG407","DeWalt"],["DWE4206","DeWalt"],["DWE492","DeWalt"],["M18BLSAG115XPD","Milwaukee"]], t=["115 mm","125 mm","230 mm","corded","cordless"]),
 K("Random orbital sander","random-orbit sander · ROS","Hand-held sander with a round pad that both orbits and rotates, for a swirl-free finish.",TS+"sanders/c863",
   [["DWE6423","DeWalt"],["DCW211","DeWalt"],["M18BOS125","Milwaukee"]]),
 K("Sheet sander","orbital finishing sander","Hand-held sander with a rectangular pad moving in small orbits, taking a cut-down abrasive sheet.",TS+"sanders/c863"),
 K("Detail sander","delta sander · mouse sander","Hand-held sander with a small triangular pad that vibrates, for corners and narrow areas.",TS+"sanders/c863"),
 K("Belt sander","","Sander with a continuous abrasive belt running over two rollers, for fast stock removal.",TS+"sanders/c863",
   [["DCW220","DeWalt"],["Powerfile Belt Sander","Black & Decker"]], t=["standard","narrow-belt file sander"]),
 K("Die grinder","","Straight-bodied high-speed hand tool for burrs and mounted points.",TS+"angle-grinders/c378",
   [["M12 FDGA2","Milwaukee"],["M18 FDGROVPDB","Milwaukee"]], t=["straight","right-angle"]),
 K("Polisher","","Power tool with a soft pad or mop that rotates to polish a surface.",TS+"sanders/c863",[["M12BPS","Milwaukee"]], t=["rotary","dual-action"]),
 K("Drywall sander","","Sander with a large round head on a long pole and dust extraction, for plasterboard walls and ceilings.",TS+"sanders/c863"),
], "Restraint only. Dropped platform ranges (18V XR, M12/M18 FUEL). All models kept (each kind already had 4 or fewer). Distinct sander kinds kept; drywall sander kind-level.")
HF = "https://www.harborfreight.com/air-tools-compressors/air-nailers-staplers.html"
PW = ["pneumatic","gas","battery"]
J["00_05"] = ([
 K("Framing nailer","nailer · nail gun","Nailer for structural work such as walls, decks and sheathing, driving large collated nails.",HF,
   [["IM350+ framing gas nailer","Paslode"],["360Xi framing gas nailer","Paslode"],["DCN930 framing nailer","DeWalt"],["PPNXi positive placement nailer","Paslode"]],
   t=PW+["positive-placement (connector)"]),
 K("Finish nailer","","Nailer for trim and moulding, driving 15- or 16-gauge finish nails.",HF, t=PW),
 K("Brad nailer","","Nailer driving thin 18-gauge brads for light trim and small woodwork.",HF, t=PW),
 K("Pin nailer","","Nailer driving headless 23-gauge pins that leave almost invisible holes.",HF, t=["pneumatic","battery"]),
 K("Staple gun","stapler","Tool that fires staples into a surface.","https://www.toolstation.com/power-tools/nailers/c48", t=["manual","electric","pneumatic","battery"]),
 K("Palm nailer","","Compact hand-held nailer that fits in the palm, for tight spaces.",HF,[["M12 palm nailer","Milwaukee"]], t=["pneumatic","battery"]),
 K("Flooring nailer","","Nailer or nailer-stapler made to fix tongue-and-groove flooring.",HF, t=["manual","pneumatic"]),
 K("Roofing and siding nailer","coil nailer","Coil nailer for fixing roofing shingles and siding.",HF, t=["roofing","siding"]),
 K("Heat gun","hot-air gun","Hand-held electric hot-air tool for stripping paint, shrinking and softening.","https://towntools.co.uk/collections/glue-heat-guns",
   [["HL1820S heat gun","STEINEL"],["MobileHeat 5","STEINEL"],["HG5030K heat gun","Makita"]], t=["mains","cordless"]),
 K("Glue gun","hot glue gun","Hand-held electric tool that melts and dispenses adhesive sticks.","https://towntools.co.uk/collections/glue-heat-guns",
   [["EG212 glue gun","Rapid"],["EG340 glue gun","Rapid"],["MiniPlus glue gun","Arrow"]], t=["mains","cordless"]),
 K("Rivet gun","riveter","Tool that sets blind rivets.","https://www.tooled-up.com/stanley-mr100-hand-riveter/prod/198004/",
   [["MR100 hand riveter","Stanley"]], t=["hand riveter","powered riveter"]),
], "Restraint only. 'Other nail guns' dissolved into Framing nailer (Paslode PPNXi kept; positive-placement as a type); power source (pneumatic, gas, battery) is a type, not a kind. Dropped Milwaukee M12/M18 platform ranges. Dropped the placeholder model 'pin nailer' (no maker). Rivet gun: hand and powered riveters as types. Model names stripped of repeated maker words.")
HB = "https://harborfreight.com/power-tools/drill-driver-bits.html"
J["00_06"] = ([
 K("Drill bit","twist drill · masonry bit · spade bit · auger bit · Forstner bit","Cutting bit held in a drill chuck to bore holes.","https://www.axminstertools.com/bosch-impact-control-hss-drill-screwdriver-set-107560",
   t=["twist (HSS)","masonry","wood: spade","wood: auger","wood: brad point","wood: Forstner","step"]),
 K("Screwdriver bit","driver bit","Interchangeable screwdriving tip for a drill, driver or bit holder.","https://www.axminstertools.com/bosch-impact-control-hss-drill-screwdriver-set-107560",
   r=[["Impact Control","Bosch"],["CENTROTEC","Festool"]]),
 K("Hole saw","","Ring-shaped toothed cutter with a pilot bit, for cutting large round holes.",HB),
 K("Saw blade","","Toothed blade or disc made to fit a power saw.","https://www.harborfreight.com/power-tools/power-saw-blades.html",
   [["Expert for Wood circular saw blade","Bosch"]], t=["circular/mitre/table","jigsaw (T- or U-shank)","reciprocating","bandsaw"]),
 K("Grinder disc","grinding disc · cutting disc","Abrasive disc fitted to an angle grinder for cutting or grinding.","https://www.klium.nl/en/makita-e-00393-grinding-disc-x-lock-for-metal-125x6x2223mm-109485",
   t=["cutting disc","grinding disc"]),
 K("Sanding sheet or disc","sandpaper","Abrasive sheet or disc shaped to fit a sander.","https://www.bosch-professional.com/gb/en/products/expert-c470-sandpaper-set-for-random-orbital-sanders-125-mm-multihole-g-60-120-240-6-pc-2608901101",
   [["EXPERT C470 sanding discs","Bosch"]], t=["sheet","disc"]),
], "Restraint only. One entry per accessory family. Twist, masonry, wood and step drill bits merged into Drill bit with patterns as types. Circular, jigsaw, reciprocating, band saw blades and the 'Other saw blades' catch-all merged into Saw blade with types. Bosch Impact Control and Festool CENTROTEC ranges kept once, on Screwdriver bit (no longer repeated on Drill bit); Bosch EXPERT range dropped as repeated (its models stay).")
TH = "https://www.toolstation.com/hand-tools/hammers/c27"
TU = "https://www.tooled-up.com/bars/cat/2000233/?page=1"
HW = "https://www.highlandwoodworking.com/collections/hammers"
J["02_02"] = ([
 K("Claw hammer","","Hammer with a striking face and a curved or straight claw for pulling nails.",TH,
   [["Sure Strike claw hammer","Estwing"],["Ultra claw hammer","Estwing"],["FatMax Curve claw hammer","Stanley"],["Steel Rip claw hammer","Milwaukee"],["High Velocity claw hammer","Minotaur"]],
   t=["steel shaft","fibreglass shaft","wooden shaft"]),
 K("Mallet","","Soft-faced or wooden-headed hammer for striking chisels and tapping parts together.",TH,
   [["Thorex 712 nylon face hammer","Thor Hammer Co"]], t=["wooden","rubber","nylon-faced","dead blow"]),
 K("Club hammer","lump hammer","Short-handled heavy double-faced hammer for driving chisels and light demolition.",TH),
 K("Ball-pein hammer","engineer's hammer","Engineer's hammer with a flat face and a rounded pein, for metalwork and riveting.",TH),
 K("Cross-pein hammer","Warrington hammer","Hammer with a flat face and a wedge-shaped pein across the handle, for starting pins and tacks.",TH),
 K("Sledgehammer","","Long-handled heavy hammer swung with both hands, for demolition and driving stakes.",TH),
 K("Brick hammer","","Hammer with a square striking face and a chisel blade, for cutting and setting bricks.",TH),
 K("Slater's hammer","","Roofer's hammer with a pointed pick, a side nail claw and a blade for cutting and holing slates.",TH),
 K("Punch","nail set · centre punch","Hardened steel rod struck with a hammer to mark centres, drive pins or set nails.",HW, t=["centre punch","pin punch","nail set"]),
 K("Wrecking bar","crowbar","Flat or round steel bar with a curved claw end, for prying and demolition.","https://www.estwing.com/?p=15197",
   [["FatMax wrecking bar","Stanley"],["Shockshield wrecking pry bar","Milwaukee"],["Gorilla Bar","Roughneck"]], t=["gooseneck","flat"]),
 K("Pry bar","flat bar","Thin flat steel bar with bevelled ends and nail slots, for prising trim and boards.",TU),
 K("Nail puller","cat's paw","Short bar with a claw tip driven under a nail head to lever it out.",HW),
 K("Lifting bar","pinch bar","Long heavy straight bar with a chisel or point end, used as a lever to lift slabs and heavy items.",TU),
], "Restraint only. Claw hammer models kept (5 market makers: Estwing, Stanley, Milwaukee, Minotaur); FatMax range dropped as repeated. Mallet: makerless 'dead blow mallet' turned into a type. Wrecking bar: makerless 'gooseneck wrecking bar' turned into a type. Pein patterns kept as kinds; pry, nail-puller and lifting bars kind-level.")
J["04_03"] = ([
 K("Dust extractor","dust collector · shop vac","Extraction unit that collects dust from workshop machines and power tools.","https://www.tooled-up.com/dust-extractors/cat/10004286/?page=1",
   [["Festool CTL MIDI I","Festool"],["Festool CTLC MINI","Festool"],["Makita VC2012L","Makita"],["Makita VC3012M","Makita"],["Makita DVC350","Makita"],["DeWalt DWV905M","DeWalt"],["DeWalt DCV586M","DeWalt"],["Bosch GAS 35 H AFC","Bosch"],["Einhell TE-VC 2230 SACL","Einhell"]],
   t=["shop vac (wet and dry)","mobile dust extractor","cyclone collector","cordless"]),
 K("Bench grinder","","Electric motor with grinding wheels on a stand, for sharpening and shaping.","https://www.toolstation.com/power-tools/bench-tools/c335", t=["dry wheel","wet wheel"]),
 K("Belt and disc sander","","Bench machine combining a sanding belt and a sanding disc on one motor.","https://www.toolstation.com/power-tools/workshop-tools/c721"),
 K("Spindle sander","bobbin sander · oscillating spindle sander","Bench machine with an abrasive sleeve on a spindle that rotates and moves up and down through a table, for curves.","https://www.toolstation.com/power-tools/workshop-tools/c721"),
], "Restraint only. Dust extractor trimmed 18 to 9 models across market-covering makers (Festool, Makita, DeWalt, Bosch, Einhell); dropped Bosch GAS 18V-10 L, DeWalt DCV584L, Draper DE2200, Festool CT 15, CTLC SYS Twin, CTM MIDI I, Flex VCE 26 L MC, Makita VC3011L, Sealey SM68, and the Festool Cleantec range. Shop vac and cyclone collector as types.")
TL = "https://www.toolstation.com/hand-tools/levels-measuring-detection/c671"
J["05_01"] = ([
 K("Tape measure","measuring tape","Coiled flexible rule that retracts into a case.",TL,
   [["FatMax Xtreme tape measure","Stanley"],["Tylon tape measure","Stanley"],["Powerwinder fibreglass tape","Stanley"]], t=["steel blade","long fibreglass tape"]),
 K("Spirit level","","Straight body with liquid vials showing level or plumb.",TL,
   [["96-2 spirit level","Stabila"],["80AS-2 spirit level","Stabila"],["FatMax Pro box beam level","Stanley"]], t=["box beam","I-beam","torpedo"]),
 K("Laser measure","laser distance measurer","Hand-held device that measures distance with a laser beam.",TL,[["DWHT77100 laser distance measurer","DeWalt"]]),
 K("Line laser","cross-line laser level","Self-levelling laser projecting horizontal and vertical lines for setting out.",TL, t=["red beam","green beam"]),
 K("Rotary laser","rotating laser level","Laser with a spinning head that sweeps a 360-degree level plane, read by a detector on site.",TL),
 K("Optical level","dumpy level · builder's level","Telescope on a tripod that sights a level line onto a staff, for site levels.",TL),
], "Restraint only. Dropped the Stanley FatMax range (repeated; its models stay). Brief names Bosch and Leica DISTO for laser measures, but the old data has no models from them and this restraint pass adds no unsourced models, so only the DeWalt model remains. Rotary laser and optical level kind-level (trade).")
FL = "https://www.fluke.com/en-us/products/electrical-test/digital-multimeters"
J["05_02"] = ([
 K("Multimeter","digital multimeter · DMM","Instrument that measures voltage, current, resistance and other electrical quantities.",FL,
   [["117 multimeter","Fluke"],["87V industrial multimeter","Fluke"]]),
 K("Clamp meter","","Electrical meter whose jaws close round a conductor to measure current without breaking the circuit.",FL),
 K("Stud, pipe and cable detector","stud finder · wall scanner","Hand-held device that senses studs, metal pipes or live cables behind a surface.",TL),
 K("Moisture meter","","Instrument that measures moisture in timber or building materials.",TL, t=["pin","pinless"]),
 K("Infrared thermometer","","Hand-held non-contact thermometer that reads surface temperature from infrared radiation.",TL),
 K("Inspection camera","endoscope · borescope","Camera on a flexible probe with a screen, for looking inside walls, pipes and machines.",TL),
 K("Oscilloscope","scope · ScopeMeter","Instrument that displays electrical signals as waveforms.",FL, t=["handheld","bench"]),
 K("Sound level meter","","Instrument that measures sound pressure level in decibels.",TL),
], "Restraint only. Fluke 117 and 87V kept as tier picks; all other kinds kind-level (no models in old data).")
TW = "https://www.toolstation.com/power-tools/welding/c157"
J["06_00"] = ([
 K("MIG welder","","Welding machine that feeds a continuous wire electrode through a gun, with shielding gas or flux-cored wire.",TW, t=["gas-shielded","gasless (flux-cored)"]),
 K("Multi-process welder","","One welding machine set up to run more than one of the MIG, TIG and stick processes.",TW,
   [["Weldmate Autoplus MIG/ARC/TIG","SIP"],["Tigren MIG/MMA/TIG inverter welder","SIP"],["X-Series MST 350XT","Bossweld"]]),
 K("TIG welder","","Welding machine using a tungsten electrode and a separate filler rod under shielding gas.",TW, t=["DC","AC/DC"]),
 K("Stick welder","arc welder · MMA welder","Welding machine that burns coated rod electrodes held in a clamp.",TW,[["Turbo Arc welder","Draper"]], t=["inverter","transformer"]),
 K("Plasma cutter","","Machine that cuts metal with an electric arc through a constricted gas jet.",TW),
], "Restraint only. Removed the SIP Weldmate range repeated on every kind (its Autoplus model stays under Multi-process welder). The brief names Lincoln, Miller, ESAB and R-Tech, but the old data holds no welder models from them and this restraint pass adds no unsourced models.")
CW = "https://canadaweldingsupply.ca/collections/welding-wire-and-electrodes?page=4"
J["06_01"] = ([
 K("Soldering iron","soldering station","Electrically heated hand tool that melts solder, sold as a plain iron or with a temperature-controlled base station.","",
   [["FX-888D soldering station","Hakko"],["FX-888DX digital soldering station","Hakko"],["M12 soldering iron","Milwaukee"]], t=["soldering iron","soldering station","cordless"]),
 K("Gas torch","soldering torch · blowtorch","Hand-held butane or propane torch for soldering, brazing and heating.","https://www.toolstation.com/hand-tools/soldering-iron/c1241", t=["butane","propane"]),
 K("Fume extractor","","Unit that draws away soldering or welding fumes.","https://store.arduino.cc/products/benchtop-solder-fume-extractor-23w", t=["benchtop soldering","welding"]),
 K("Welding wire and rod","welding wire · welding rod · electrode · filler rod","Consumable filler wire, rod or electrode used in welding and brazing.",CW,
   [["EasyArc ER70S-6 MIG wire","Lincoln Electric"],["UltraCore E316T1-1 flux-cored wire","Lincoln Electric"],["Techalloy 276 TIG rod","Lincoln Electric"],["Jupiter cast iron arc rod","Rockmount Research and Alloys"]],
   r=[["Sureweld","ESAB"]], t=["MIG wire","flux-cored wire","stick electrode","TIG filler rod","tungsten electrode","brazing rod"]),
 K("Solder","solder wire","Fusible alloy, usually wire with a flux core, melted to join metal parts and electronics.","https://www.tequipment.net/Kester/series_kester-solder-wire-series/",
   [["Kester 44","Kester"],["Kester 245","Kester"],["Kester 24-7068","Kester"]], t=["leaded","lead-free"]),
 K("Flux","soldering flux · brazing flux","Paste, liquid or powder that cleans joint surfaces for soldering or brazing.",CW, t=["paste","liquid","powder"]),
], "Restraint only. Welding wire, welding rod, tungsten electrode and brazing rod merged into 'Welding wire and rod' with types. Dropped the Milwaukee M12 platform range and the Hakko FX-888 and Lincoln EasyArc ranges (their models stay); ESAB Sureweld kept as the only ESAB entry. Soldering iron had no old source URL, so none is given.")
TSL = "https://www.toolstation.com/ladders-storage/"
J["07_00"] = ([
 K("Stepladder","step ladder · platform stepladder","Free-standing hinged A-frame ladder, with or without a top platform.",TSL+"step-ladders/c323",
   [["MasterTrade Stepladder","Werner"],["AdjustaStep PRO Aluminium Stepladder","Werner"],["INSUL8-S Fibreglass Professional Swingback Step","TB Davies"],["MAXI Professional Platform Step Ladder","TB Davies"],["HORIZON Platform Step Ladder","TB Davies"],["Select Step Ladder","Little Giant"],["MagnaStep Platform Step Ladder","Lyte Ladders"]],
   t=["swingback","platform","aluminium","fibreglass"]),
 K("Combination ladder","multi-purpose ladder","Ladder that can be set up in more than one form, such as step or extension, from one set of rails.",TSL+"ladders/c686",
   [["Velocity Series 2.0 Multi-purpose Ladder","Little Giant"],["LeanSafe X3 Combination Ladder","Werner"],["ExtensionPLUS X4 Combination Ladder","Werner"],["Stilo Aluminium Combination Ladder","TB Davies"],["Skymaster X Combination Ladder","Zarges"]]),
 K("Extension ladder","","Ladder with sliding sections, leaned against a support.","https://toolstation.com/ladders-storage/extension-ladders/c94",
   [["TradePRO Square-Rung Extension Ladder","Werner"],["Pro Square Rung Extension Ladder","Werner"],["TASKMASTER Extension Ladder","TB Davies"],["Everest Extension Ladder","Zarges"]], t=["two-section","three-section"]),
 K("Telescopic ladder","","Ladder whose rungs and rails telescope into each other for compact storage.","https://toolstation.com/ladders-storage/telescopic-ladders/c1050",
   [["Xtend+Climb ProSeries S2.0 Telescopic Ladder","TB Davies"],["Soft Close Telescopic Extension Ladder","Werner"],["MT-LADDER","Werner"]]),
 K("Single ladder","leaning ladder","One-section ladder leaned against a support.","https://toolstation.com/ladders-storage/extension-ladders/c94"),
 K("Roof ladder","","Ladder with wheels and a ridge hook, laid on a pitched roof.",TSL+"ladders/c686"),
 K("Tripod ladder","garden ladder · orchard ladder","Ladder with a single rear leg forming a tripod, for uneven ground and hedges.",TSL+"ladders/c686"),
], "Restraint only. Platform stepladder merged into Stepladder as a type (Werner Mastertrade Platform Stepladder dropped as a near-duplicate of MasterTrade Stepladder). Dropped the TASKMASTER and TradePRO ranges, which only repeated their models.")
TJ = "https://toolstation.com/automotive/jacks-stands-winches/c453"
J["07_01"] = ([
 K("Sack truck","hand truck","Upright two-wheel carrier with a toe plate, tilted back to move loads.","https://www.ajproducts.co.uk/warehouse-workshop/trolleys-castors/sack-trucks/folding-sack-trucks", t=["fixed","folding","stair-climbing"]),
 K("Moving dolly","dolly · furniture dolly","Low platform carrier on wheels or casters.","https://toolstation.com/ladders-storage/trolleys-dollies/c1425"),
 K("Hand cart","platform trolley","Hand-pushed multi-wheel cart or trolley for goods.","https://www.verdex.com.au/trolleys-hand-trucks/platform-trolleys/folding-platform-trolleys/",
   [["V-Cart Folding Aluminium Trolley","Verdex Equipment"]], t=["fixed","folding"]),
 K("Bottle jack","","Hydraulic jack in a vertical bottle form, for lifting heavy loads.",TJ),
 K("Winch","","Drum and rope or cable device for pulling or lifting.",TJ, t=["hand","electric"]),
 K("Chain hoist","chain block","Hand or electric hoist that lifts loads with a chain.",TJ, t=["manual","electric"]),
], "Restraint only. All planned kinds kept kind-level; Verdex V-Cart kept as the only model. Vehicle jacks and stands were moved to Vehicles by the plan and are not on this shelf.")
J["08_00"] = ([
 K("Portable generator","generator · inverter generator · open-frame generator","Engine-driven generator for portable mains power, either inverter type for stable output or open-frame.","https://www.harborfreight.com/generators-engines/generators/inverter-generators.html",
   t=["inverter","open-frame (conventional)","petrol","dual-fuel"]),
 K("Air compressor","","Machine that makes compressed air for tools, tyre inflation and spraying.","https://www.tooled-up.com/brand/draper/draper/air-compressors/10001315/",
   [["D20AC4L cordless air compressor","Draper"]], t=["oil-free","oil-lubricated","cordless"]),
 K("Submersible pump","drainage pump · sump pump","Pump that sits under water to remove or drain it.","https://tanks-direct.co.uk/collections/submersible-pumps",
   [["Ama Drainer 301","KSB"]], t=["clean water","dirty water"]),
 K("Surface pump","pressure pump","Surface-mounted general-purpose pump that draws water and delivers it under pressure.","https://tanks-direct.co.uk/collections/submersible-pumps"),
 K("Transfer pump","barrel pump","Pump that moves liquid from one container to another.","https://us.sparex.com/workshop-merchandising/workshop-consumables/fluid-fuel-delivery-storage/fuel-transfer-pumps.html",
   [["Supa Mover Barrel Pump","Sparex"]], t=["hand","electric"]),
 K("Cement mixer","concrete mixer","Drum machine that mixes cement, mortar or concrete.","https://www.toolstation.com/construction-insulation/site-equipment/c1059", t=["electric","petrol"]),
 K("Plate compactor","wacker plate","Vibrating plate machine that compacts soil and aggregate.","https://www.wackerneuson.co.uk/about-us/news/detail/new-products-by-wacker-neuson-1",
   [["BPS1550","Wacker Neuson"],["APS1550e","Wacker Neuson"],["DPS2050","Wacker Neuson"]], t=["forward","reversible"]),
], "Restraint only. Inverter and open-frame generators merged into Portable generator with types; the Harbor Freight PREDATOR range dropped (repeated, retailer house range). Draper D20 platform range dropped (model stays). Plate compactor trimmed from 5 Wacker Neuson models to 3 and its range dropped. Trade plant is not on this shelf.")
TB = "https://www.tooled-up.com/tool-boxes-storage/cat/23"
J["09_00"] = ([
 K("Portable tool box","toolbox · tool trolley · modular tool storage system","Portable box or case for carrying tools, with wheels or stackable modular fittings as options.","",
   r=[["TSTAK","DeWalt"],["PACKOUT","Milwaukee"],["Systainer","Festool"],["L-BOXX","Bosch"],["MakPac","Makita"],["FatMax Pro Stack","Stanley"]],
   t=["portable toolbox","wheeled toolbox","stackable tool case"]),
 K("Tool chest","top box","Drawered or lidded box for tools, set on a bench or roller cabinet.",TB),
 K("Roller cabinet","roll cab","Drawered tool cabinet on casters.",TB,[["Superline Pro Roller Cabinet","Sealey"]]),
 K("Site box","jobsite box · site chest","Large lockable steel box for storing tools on site or in a van.",TB),
 K("Tool bag","","Soft or hard-bodied bag made to carry tools.",TB, t=["open tote","zipped bag","backpack"]),
 K("Tool roll","","Flexible roll-up wrap with pockets for tools.","https://www.tooled-up.com/brand/bahco/bahco/tool-rolls/2001444/"),
 K("Tool pouch","tool belt pouch","Belt-worn pouch or holder that keeps tools and fixings at hand.",TB),
], "Restraint only. Modular storage systems kept as ranges on Portable tool box. Sealey Superline Pro range dropped as it only repeated its model. Portable tool box had no old source URL, so none is given.")
for job, (kinds, notes) in J.items():
    p = os.path.join(D, job + '.json'); tmp = p + '.tmp'
    if os.path.exists(p): print('exists, skip', job); continue
    json.dump({"kinds": kinds, "brands": [], "traditions": [], "notes": notes}, open(tmp, 'w'), ensure_ascii=False, indent=1)
    os.replace(tmp, p); print('wrote', job)
