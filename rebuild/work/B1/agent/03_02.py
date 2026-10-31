import json,os
B=["baby"]
kinds=[
{"n":"Baby cot","a":"crib · cot bed · convertible crib · mini crib","d":"A barred bed made for an infant or toddler.","tg":B,
 "t":["full-size/standard","convertible (cot bed, converts to toddler bed or daybed)","mini crib","folding/portable","wood","metal","round/oval"],
 "s":"https://en.wikipedia.org/wiki/Infant_bed",
 "x":[{"n":"Stokke Sleepi","a":"Sleepi","d":"Oval adjustable cot that grows from crib to junior bed, a design benchmark among premium cots.","mk":"Stokke","y":"1999","s":"https://en.wikipedia.org/wiki/Stokke_AS","dt":"oval frame · beech · designed by Susanne Grønlund and Claus Hviid Knudsen"}],
 "m":[["Hudson 3-in-1","Babyletto"],["Kalani 4-in-1","DaVinci"],["Jenny Lind 3-in-1","DaVinci"],["Union 4-in-1","DaVinci"],["Benton 4-in-1","Graco"],["Emery Deluxe 6-in-1","Delta Children"],["Steveston 4-in-1","Storkcraft"],["Folding Mini Crib","Delta Children"],["SUNDVIK","IKEA"],["SMAGORA","IKEA"],["MYLLRA","IKEA"],["GULLIVER","IKEA"]]},
{"n":"Bassinet","a":"cradle · Moses basket · bedside sleeper · co-sleeper","d":"A small basket-like or rocking bed for a newborn, on legs or a stand, used for the first months.","tg":B,
 "t":["bassinet (fixed legs or casters)","cradle (rocking or gliding)","Moses basket/carry cot","bedside sleeper/co-sleeper","smart bassinet (automated soothing)","swivel"],
 "s":"https://en.wikipedia.org/wiki/Bassinet",
 "m":[["Iora Bedside Bassinet","Maxi-Cosi"],["Beside Me Doze Deluxe","Baby Delight"],["LullaGlide Plus 3-in-1","Chicco"],["Close to You 3-in-1","Chicco"],["Clear-Vue Co-Sleeper","Arm's Reach"],["Bedside Sleeper","babybay"],["BassiNest Swivel Sleeper 3.0","HALO"],["SNOO Smart Sleeper",""],["Cradle","BabyBjörn"],["Breeze Bassinet","4moms"]]},
{"n":"Changing table","a":"changing unit · changing station · baby changer","d":"A raised platform or unit with a padded top for changing a baby's nappy, often with storage below.","tg":B,
 "t":["freestanding table","changing unit with drawers","changing top for a chest of drawers","wall-mounted fold-down","changing mat"],
 "s":"https://en.wikipedia.org/wiki/Changing_table",
 "m":[["Linea","Leander"]]},
{"n":"Playpen","a":"play yard · playard · travel cot · Pack 'n Play","d":"A freestanding enclosure that holds a small child in place to play or sleep.","tg":B,
 "t":["traditional wooden playpen","portable mesh play yard","travel cot","bassinet insert","changer attachment"],
 "s":"https://en.wikipedia.org/wiki/Playpen",
 "x":[{"n":"Pack 'n Play","a":"Graco playard","d":"Folding mesh-sided portable play yard credited as the first of its kind; its name is used generically for play yards.","mk":"Graco","y":"1987","s":"https://en.wikipedia.org/wiki/Graco_(baby_products)",
   "v":[{"n":"Pack 'n Play Portable Playard","mk":"Graco","y":"","d":"core play yard, compared in Consumer Reports' play-yard review"},{"n":"Pack 'n Play On the Go","mk":"Graco","y":"","d":"travel version"},{"n":"Pack 'n Play On the Go Bassinet","mk":"Graco","y":"","d":"with newborn bassinet insert"}],
   "dt":"metal and plastic frame · mesh sides · bassinet and changer inserts · fabric colours"}],
 "m":[["Travel Crib Light","BabyBjörn"],["Lotus Travel Crib","Guava Family"]]},
{"n":"High chair","a":"highchair · feeding chair","d":"A raised chair with a tray or harness that holds a small child at table height.","tg":B,
 "t":["standard with tray","folding","grow-with-child/convertible","hook-on table chair","wooden"],
 "s":"https://en.wikipedia.org/wiki/High_chair",
 "x":[{"n":"Tripp Trapp","a":"KinderZeat (former North American name)","d":"Adjustable wooden chair by Peter Opsvik whose seat and footrest move so it grows from baby to adult.","mk":"Stokke","y":"1972","s":"https://en.wikipedia.org/wiki/Tripp_Trapp",
   "v":[{"n":"Tripp Trapp Baby Set","mk":"Stokke","y":"","d":"backrest and leg ring for babies"},{"n":"Tripp Trapp Newborn Set","mk":"Stokke","y":"","d":"reclining newborn seat attachment"},{"n":"Oak limited editions","mk":"Stokke","y":"","d":"oak instead of beech"}],
   "dt":"beech, oak · colour finishes · tray, cushion"}],
 "m":[["Clikk","Stokke"],["Float Easy Foldable","Munchkin"],["Ciro","UPPAbaby"],["ANTILOP","IKEA"],["BLÅMES","IKEA"],["SANDKATT","IKEA"],["Mimzy Spin 3in1","Joie"],["Minla","Maxi-Cosi"],["Bryn","Nuna"],["Snack 'n' Stow","Graco"]]},
{"n":"Booster seat","a":"table booster · feeding booster","d":"A seat with straps fixed on an adult chair to raise a small child to table height.","tg":B,
 "t":["strapped booster with tray","foam/compact booster","folding travel booster"],
 "s":"https://babygearlab.com/topics/nursing-feeding/best-table-booster-seat",
 "m":[["SQUISH","Prince Lionheart"],["Tot Nest Booster Seat","OXO"],["Baby Base","Ingenuity"],["Zoo Booster Seat","Skip Hop"],["Tot Perch with Straps","OXO"],["Pocket Booster Seat","Chicco"]]},
{"n":"Bed guard rail","a":"bed rail · toddler bed rail · bed guard","d":"A rail made to be fitted to one bed to keep a child from rolling out.","tg":B,
 "t":["swing-down/fold-down","fixed","foam bumper","mesh","double-sided","extra-long"],
 "s":"https://www.babylist.com/hello-baby/best-toddler-bed-rails",
 "m":[["Flexguard Toddler bed rail","TotCraft"],["Miniflex","TotCraft"],["Bed Rail for Toddlers","Baby Joy"],["Toddler Bed Rail","Munchkin"],["Toddler Bed Rail Bumper","hiccapop"],["Savoy Fold Down Bed Rail","Dreambaby"],["Convertible Swing Down Crib Rail","Regalo"]]}
]
brands=[
{"n":"Stokke","c":"Norway","f":"1932","seg":"Premium children's furniture","d":"Norwegian children's furniture maker from Ålesund, owned by NXMH since 2014.","lines":["Tripp Trapp","Sleepi","Clikk"],"sig":["Tripp Trapp","Stokke Sleepi"],"s":"https://en.wikipedia.org/wiki/Stokke_AS"},
{"n":"Graco","c":"United States","f":"1942","seg":"Mass-market baby gear","d":"American baby products company, owned by Newell Brands.","lines":["Pack 'n Play"],"sig":["Pack 'n Play"],"s":"https://en.wikipedia.org/wiki/Graco_(baby_products)"},
{"n":"IKEA","c":"Sweden","f":"1943","seg":"Mass-market flat-pack furniture","d":"Swedish-founded flat-pack furniture and homeware retailer.","s":"knowledge"},
{"n":"Chicco","c":"Italy","seg":"Mass-market baby gear","d":"Italian baby products brand of the Artsana group.","s":"knowledge"}]
notes=("All kinds tagged baby. Archetypes: Tripp Trapp (Stokke 1972), Pack 'n Play (Graco 1987), Stokke Sleepi (1999). Models trimmed to market makers plus independent test picks "
"(Consumer Reports top picks for high chairs/bassinets/play yards, Which? tested list, BabyGearLab booster and bassinet awards, Healthline cribs, Babylist bed rails). "
"IKEA cots cut from 7 to 4 (ALSKVARD, GONATT, SNIGLAR dropped). Changing table added (only one sourced model: Leander Linea; The Bump page blocked). "
"SNOO kept as model with blank maker (maker not named on retrieved pages). Old Google-taxonomy/IKEA/eBay/Vevor kind sources replaced by retrieved Wikipedia/test pages. "
"No traditions (none relevant). Nothing dropped as out of scope.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/B1/shelves/03_02.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=0); os.replace(p+".tmp",p)
