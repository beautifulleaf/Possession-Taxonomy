import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/E4/agent')
from h import v,x,B,W
BI='https://bow-international.com/?p=6130'; BP='https://en.wikipedia.org/wiki/Bodkin_point'; GL='https://glasgowarchers1948.co.uk/2024/07/05/love-hoyts-you-in-the-wallet/'
WB='https://www.abbeyarchery.com.au/p/ARTC991/What+is+a+whisker+biscuit.html'; PS='https://www.petersenshunting.com/editorial/fixed-versus-slider-archery-sight/478467'
ES='https://eastonarchery.com/?p=101174'; RA='https://en.wikipedia.org/wiki/Release_aid'
kinds=[
{"n":"Arrow","a":"","d":"Shafted projectile shot from a bow, with a point, fletching and nock.",
 "t":["wood (e.g. cedar)","bamboo or reed","aluminium","carbon","aluminium-carbon","feather fletching","plastic vanes"],"s":"https://lancasterarchery.com/products/easton-6-5mm-hunter-classic-fletched-arrows",
 "x":[x("Easton XX75","Easton Archery","1958","Cold-drawn 7075-alloy aluminium shaft, the best-selling arrow shaft of all time, made in 22 sizes.",BI,
   [v("24SRT-X","Easton Archery","1939 or 1949 (sources differ)","Easton's first aluminium arrow")],"size (diameter and wall) · length · fletching"),
  x("Easton A/C/E","Easton Archery","1987","Barrelled aluminium-carbon target arrow; won the 1988 Olympic gold with Jay Barrs.",BI,dt="spine · length · point weight"),
  x("Easton X10","Easton Archery","1995","Aluminium-carbon arrow for long-distance target shooting; used for every Olympic archery gold since.",BI,[v("X10 ProTour","Easton Archery","","version for compound archers")],"spine · length · point weight")],
 "m":[["Easton 6.5mm Hunter Classic","Easton Archery"],["Superdrive Micro","Easton Archery"]]},
{"n":"Crossbow bolt","a":"quarrel · crossbow arrow","d":"Short shafted projectile, usually 15–22 in long, shot from a crossbow.","t":["carbon","aluminium","lighted nock"],
 "s":"https://copsplus.com/arrows/barnett-bar20031-headhunter-lighted-bolts-20-inches-black-3-pack/",
 "m":[["Headhunter Lighted Bolts","Barnett"],["ACU-X","TenPoint"]]},
{"n":"Arrowhead","a":"broadhead · field point · bodkin","d":"Point fitted to an arrow or bolt shaft.",
 "t":["field point","target point","broadhead, fixed-blade","broadhead, mechanical","broadhead, hybrid","judo point","blunt","bodkin","stone or bronze (historical)"],"s":"https://lancasterarchery.com/pages/bows",
 "x":[x("Bodkin point","","1st–2nd millennium AD","Needle-like squared iron arrowhead, up to 11.5 cm long, made to defeat armour; now copied for historical archery.",BP,
   [v("Needle bodkin","","","long and thin, against mail"),v("Plate cutter","","","shorter and sturdier, against plate")],"length · section · iron or steel")]},
{"n":"Bowstring","a":"","d":"String made to fit a bow or crossbow.","t":["Flemish twist","endless loop","crossbow string","cable (compound)"],"s":"https://lancasterarchery.com/pages/bows"},
{"n":"Bow riser","a":"handle","d":"Centre section of a take-down bow, sold without limbs, that holds the grip, sight and rest.","t":["ILF (dovetail) recurve","Formula recurve","barebow","hunting take-down"],
 "s":"https://lancasterarchery.com/pages/bows",
 "x":[x("ILF riser","Hoyt","mid-1980s","Take-down riser with Hoyt's dovetail limb fitting and limb bolts, adopted by most makers as the International Limb Fitting.",GL,
   [v("Grand Prix","Hoyt","","Hoyt's own name for the fitting"),v("Formula","Hoyt","2009","longer, non-interchangeable fitting")],"length 23–27 in · alloy or carbon · hand",a="Grand Prix fitting · dovetail riser")],
 "m":[["Hoyt RCRV Podium Series Grand Prix ILF riser","Hoyt"]]},
{"n":"Arrow rest","a":"","d":"Device on the bow riser that supports the arrow before release.","t":["containment (brush)","drop-away","blade rest","stick-on or shelf rest"],
 "s":"https://www.beararchery.com/products/trophy-ridge-whisker-biscuit-pro-arrow-rest",
 "x":[x("Whisker Biscuit","Trophy Ridge","c. 1999","Containment rest whose ring of synthetic bristles holds the arrow all round while fletching passes through.",WB,
   [v("Original Whisker Biscuit","Carolina Archery Products","c. 1999"),v("Quick Shot","Carolina Archery Products","2003","V entry slot"),v("Whisker Biscuit Pro","Trophy Ridge")],"bristle ring size S/M/L · hand · adjustment")]},
{"n":"Bow sight","a":"pin sight","d":"Sight fitted to the bow riser, with pins or a single aiming point set for distance.","t":["fixed-pin","slider (movable pin)","single-pin","target sight (recurve)"],"s":PS,
 "m":[["Fast Eddie PM","Spot-Hogg"],["Fast Eddie Five-Pin","Spot-Hogg"],["Hogg Father Single-Pin","Spot-Hogg"]]},
{"n":"Release aid","a":"mechanical release · release","d":"Hand-held trigger device that holds and releases the bowstring instead of the fingers.","t":["wrist trigger","T-handle","thumb button","back tension (hinge)","resistance (tension)","caliper jaw","rope or D-loop"],"s":RA,
 "m":[["Target 4","Carter"]]},
{"n":"Stabiliser","a":"stabilizer · long rod · V-bar","d":"Weighted rod or set of rods fitted to the riser to balance the bow and damp vibration.","t":["front rod","side rods","V-bar","hunting stabiliser"],"s":ES,
 "m":[["Halcyon","Easton Archery"],["Contour","Easton Archery"]]},
]
brands=[
 B("Easton Archery","United States","1922","Professional & flagship","arrows","Arrow maker founded by Doug Easton; made the first aluminium arrows and the X10 used for Olympic golds.",BI,sig=["Easton XX75","Easton A/C/E","Easton X10"],rel=["Hoyt"]),
 B("Trophy Ridge","United States","","Mainstream","arrow rests · sights","Archery-accessory brand of Escalade Sports that took over the Whisker Biscuit in 2007.",WB,sig=["Whisker Biscuit"]),
 B("Spot-Hogg","United States","","Specialist","bow sights","US bow-sight maker.",PS),
]
W('06_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"All six old kinds kept; Bow sight, Release aid and Stabiliser added. Old arrow-rest entries 'Blade rest' and 'Drop-away rest' became types; Whisker Biscuit Pro became a version of the Whisker Biscuit archetype. No bowstring models (none in old data). Easton 24SRT-X year given as 1939 or 1949 because bow-international.com and nrafamily.org disagree. No traditional/thumb-ring entries (no source fetched)."})
