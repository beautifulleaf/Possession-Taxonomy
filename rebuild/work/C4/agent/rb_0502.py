import sys; sys.path.insert(0,'work/C4/agent')
from rb_lib import *
WU='https://www.firemountaingems.com/learn/categories/essential-resources/how-tos/G72J-article.html'
MC='https://en.wikipedia.org/wiki/Metal_clay'
VE='https://en.wikipedia.org/wiki/Vitreous_enamel'
MI='https://woolery.com/blog/guest-post-claudia-chase-of-mirrix-looms'
KC='https://knewconcepts.shop/collections/jewelers-saws-tools'
OF='https://www.ottofrei.com/collections/jewelry-pliers-cutters'
SF='https://www.seattlefindings.com/jewelry_soldering_torches.html'
FM='https://www.firemountaingems.com/beads/'
ST='https://stuller.com/benchjeweler/resources/bencharticles/view/essential-metalsmithing-tools-and-supplies'
kinds=[
{'n':'Jewellery pliers','a':'','d':'Small pliers made for bending wire and closing findings.','t':['chain-nose','flat-nose','round-nose','crimping','mandrel (forming)','cutters'],
 'm':[['Supreme Pliers and Cutter Kit','Lindstrom'],['Naked Pliers 5-1/8 in','Otto Frei'],['Revere Pliers','Revere Academy'],['Chain-nose pliers',''],['Crimping pliers',''],['Flat-nose pliers',''],['Round-nose pliers','']],'s':OF,
 'x':[X('Wubbers mandrel pliers','Jewellery-specific forming pliers designed by psychologist and teacher Patti Bullard; the range includes looping, round and bail-making, and triangular, oval, square and half-round mandrel pliers.','Wubbers',WU,v=[('Classic Wubbers Kit of 6','Wubbers'),('Half Round Mandrel Wubbers Pliers Kit','Wubbers'),('Oval Mandrel Wubbers Pliers Kit','Wubbers'),('Round Mandrel Wubbers Pliers Kit','Wubbers'),('Square Mandrel Wubbers Pliers Kit','Wubbers'),('Triangle Mandrel Wubbers Pliers Kit','Wubbers')],dt='mandrel shape · set type (regular, Baby, ProLine)')]},
{'n':"Jeweller's saw",'a':'saw frame · piercing saw','d':'Fine-bladed frame saw made for cutting metal in jewellery work.','t':['adjustable frame 3, 5 or 8 in throat','fixed frame','blade grade'],
 'm':[['3-Piece Miniature Saw Frame Set','Anderson'],["Jeweler's Saw Frame (Big Belly, Mini)",'GreenLion Studios']],'s':KC,
 'x':[X('Knew Concepts Mk.IV saw frame','Lever-tension heavy-duty fret and jeweller saw frame sold in 3, 5 and 8 inch sizes, with or without swivelling blade clamps.','Knew Concepts',KC,v=[('Mk.IV Heavy Duty Fret and Jeweler\'s Saw','Knew Concepts'),('Titanium Birdcage Fret Saw','Knew Concepts','titanium, lever tension'),('MK4 High-Tension Jeweler\'s Saw Frame','Knew Concepts'),('MK5 Jeweler\'s Saw Frame','Knew Concepts')],dt='throat depth · tension lever · clamp type')]},
{'n':'Jewellery soldering torch','a':'soldering kit','d':'Torch or kit made for soldering, brazing or annealing jewellery.','t':['oxy-propane','oxy-acetylene','butane micro torch','hand-held'],
 'm':[['Small Torch Kit','Gentec'],['Microflame Refillable Butane Torch','Microflame'],['ORCA Torch','Orca Torch'],['Micro Torch','SFC Tools'],['Mighty Torch','SFC Tools'],['Little Smith Torch 5 Tip Kit','Smiths'],['Little Torch Kit','Smiths']],'s':SF},
{'n':"Jeweller's bench and bench pin",'a':'bench peg','d':'Workbench with a V-slotted pin that supports work for sawing and filing.','t':['clamp-on pin','bench with sweeps drawer','ring clamp'],'m':[],'s':ST},
{'n':"Ring mandrel and jeweller's hammer",'a':'','d':'Tapered steel rod for sizing and shaping rings, and hammers for forming metal.','t':['steel ring mandrel','bracelet mandrel','ball-peen hammer','nylon-faced hammer','riveting hammer'],'m':[],'s':ST},
{'n':'Metal clay','a':'precious metal clay · PMC','d':'Clay of fine metal powder and binder that is shaped, dried and fired to solid metal.','t':['fine silver','gold','sterling','bronze','copper'],'m':[],'s':MC,
 'x':[X('Precious Metal Clay (PMC)','First metal clay, developed in early-1990s Japan by Masaki Morikawa at Mitsubishi Materials; discontinued in 2023 according to Wikipedia.','Mitsubishi Materials',MC,'early 1990s',v=[('PMC+','Mitsubishi Materials'),('PMC3','Mitsubishi Materials'),('PMC Pro','Mitsubishi Materials'),('PMC Sterling','Mitsubishi Materials')],dt='metal · firing temperature · form (clay, paste, sheet)'),
      X('Art Clay Silver','Silver clay by AIDA Chemical Industries, listed as the oldest metal clay brand still available.','AIDA Chemical Industries',MC,v=[('Original','AIDA Chemical Industries'),('Slow Dry','AIDA Chemical Industries'),('650','AIDA Chemical Industries'),('Slow Tarnish','AIDA Chemical Industries')],dt='metal · firing range · drying time'),
      X('BRONZclay and COPPRclay','Base-metal clays by Metal Adventures; bronze introduced 2008.','Metal Adventures',MC,'2008',dt='metal · kiln atmosphere'),
      X('EZ960 Sterling','Enriched sterling silver clay invented by Bill Struve of Metal Adventures.','Metal Adventures',MC,dt='sterling alloy')]},
{'n':'Enamelling supplies','a':'enameling · vitreous enamel','d':'Glass-based enamel powders and tools for fusing colour onto metal.','t':['powder enamel','lump enamel','transparent','opaque','kiln'],'m':[],'s':VE,
 'x':[X('Vitreous enamelling techniques','Named enamelling methods: cloisonne, champleve, basse-taille, plique-a-jour and painted Limoges, fired at roughly 750 to 850 degrees C.','',VE,dt='technique · base metal · enamel opacity')]},
{'n':'Bead loom','a':'','d':'Frame made for weaving seed beads on warp threads.','t':['simple frame','tension-adjustable','tapestry-and-bead loom'],'m':[],'s':FM,
 'x':[X('Mirrix loom','Metal tapestry and bead-weaving loom from Mirrix Looms, started by Claudia Chase with orders by June 1996.','Mirrix Looms',MI,'1996',dt='weaving width · frame size')]},
{'n':'Bead design board','a':'','d':'Flocked tray with channels made for laying out bead designs.','t':[],'m':[],'s':FM},
]
brands=[
B('Wubbers','United States','','Specialist','jewellery pliers','Jewellery pliers designed by Patti Bullard.',s=WU,sig=['Wubbers mandrel pliers']),
B('Knew Concepts','United States','','Specialist','saw frames','Maker of lever-tension jeweller saw frames.',s=KC,sig=['Knew Concepts Mk.IV saw frame']),
B('Mirrix Looms','United States','1996','Specialist','bead and tapestry looms','Loom maker founded by Claudia Chase.',s=MI,sig=['Mirrix loom']),
B('Mitsubishi Materials','Japan','','Professional & flagship','metal clay','Japanese materials group whose Masaki Morikawa developed PMC.',s=MC,sig=['Precious Metal Clay (PMC)']),
B('AIDA Chemical Industries','Japan','','Specialist','metal clay','Maker of Art Clay Silver.',s=MC,sig=['Art Clay Silver']),
B('Metal Adventures','United States','','Specialist','base-metal clay','Maker of BRONZclay, COPPRclay and EZ960 Sterling.',s=MC,sig=['BRONZclay and COPPRclay','EZ960 Sterling']),
]
save('05_02',kinds,brands,[],'Kept all planned kinds. Lindstrom, Smith Little Torch, Durston, GRS, Thompson not confirmed from fetched pages beyond old data, so no archetypes. Bench pin and ring mandrel kinds sourced to the Stuller bench-jeweler article; no models added.')
