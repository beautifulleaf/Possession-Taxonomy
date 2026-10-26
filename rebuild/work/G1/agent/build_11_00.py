import json, os
AE_SH="https://www.autoexpress.co.uk/product-group-tests/86454/best-car-shampoo"
WHICH="https://www.which.co.uk/reviews/new-and-used-cars/article/best-car-wash-kit-car-shampoos-and-wheel-cleaners-tested-adyyg3Y1jieo"
kinds=[
 {"n":"Car-wash shampoo","a":"car shampoo · wash and wax","d":"Product made to wash a vehicle's paintwork.",
  "t":["pH-neutral shampoo","wash and wax","ceramic (SiO2) shampoo","waterless wash","rinseless wash","concentrate"],
  "s":"https://www.autoglym.com/bsc-bodywork-shampoo-conditioner.html",
  "m":[["Auto-Wash","Bilt Hamber"],["Bodywork Shampoo Conditioner","Autoglym"],["pH Neutral Shampoo","VP"],["Shampoo & Wax","Simoniz"],
       ["Born To Be Mild","Dodo Juice"],["Ultimate Wash & Wax","Meguiar's"],["Zip Wax Car Wash & Wax","Turtle Wax"],
       ["Ultra Wash & Wax","CarPlan"],["Ultra Shine Waterless Wash & Wax","Armor All"],["Car Shampoo 3-in-1","Kärcher"]]},
 {"n":"Snow foam","a":"pre-wash foam · foam cannon · foam lance","d":"Thick pre-wash foam sprayed from a pressure-washer lance to loosen dirt before contact washing.",
  "t":["snow foam liquid","alkaline (traffic-film) foam","pH-neutral foam","foam cannon / lance (pressure-washer)","pump-up foam sprayer"],
  "s":"https://www.autoexpress.co.uk/product-group-tests/95857/best-snow-foams",
  "m":[["Touch-Less","Bilt Hamber"],["Advanced HP Snow Foam","Halfords"],["Polar White","CarPlan"],["Vortex Blast","Triplewax"],
       ["Fast Foam","Angelwax"],["Actifoam Energy","Sonax"],["Polar Blast","Autoglym"],["Q2M Foam","Gyeon"],
       ["Premium Foam Cannon Kit","AVA"],["Pro V2.0 foam cannon","MJJC"],["Polar Blaster Snow Foamer","Autoglym"]]},
 {"n":"Wash mitt","a":"wash glove · wash pad","d":"Glove-like pad of microfibre, wool or chenille used to wash paintwork by hand.",
  "t":["microfibre","chenille (noodle)","lambswool / sheepskin","wheel mitt","wash pad"],
  "s":"https://www.autofinesse.com/en/shop/wash/wash-mitts",
  "m":[["Plush Microfibre Wash Mitt","Auto Finesse"],["Ultra Soft Wash Mitt","Auto Finesse"],["Plush Microfibre Wheel Mitt","Auto Finesse"],
       ["Advanced Microfibre Wash Mitt","Halfords"]]},
 {"n":"Drying towel","a":"drying cloth · microfibre drying towel","d":"Large absorbent microfibre towel for drying a vehicle after washing without marking the paint.",
  "t":["twisted loop","plush / long pile","waffle weave","short loop","edgeless","chamois / synthetic chamois"],
  "s":"https://www.autoexpress.co.uk/car-care/357935/best-car-drying-cloths",
  "m":[["Demon Micro Microfibre Drying Towel","CarPlan"],["Ultimate Microfibre Drying Towel","Turtle Wax"],["Large Luxury Loop Drying Towel","Squid Ink"],
       ["Advanced Drying Towel","Halfords"],["Twisted Loop Drying Towel","Angelwax"],["Ultra Soft Drying Towel","Autoglym"],
       ["Q2M Silk Dryer EVO","Gyeon"],["Short Loop Drying Towel","Gtechniq"]]},
 {"n":"Wheel and tyre cleaner","a":"alloy wheel cleaner · tyre cleaner","d":"Spray cleaner that dissolves brake dust and road grime from wheels and tyre sidewalls.",
  "t":["pH-balanced","acid","alkaline","iron-reactive (colour-change)","gel / foam","tyre cleaner"],
  "s":"https://www.autoexpress.co.uk/product-group-tests/63754/best-car-wheel-cleaners",
  "m":[["Auto-Wheel","Bilt Hamber"],["Axis Wheel Cleaner","Duel"],["Decon-It","VP"],["Alloy Cleaner","Liquid Tech"],["Ultracare Wheel Cleaner","Simoniz"],
       ["WheelX","CarPro"],["Q2M Iron Wheel Cleaner REDEFINED","Gyeon"],["Advanced All Wheel Cleaner","Autoglym"],["Ultimate Wheel Cleaner","Meguiar's"],
       ["Hyper Foam Cleaner","Turtle Wax"]]},
 {"n":"Clay bar","a":"detailing clay · clay mitt · clay towel","d":"Pliable clay used with lubricant to lift bonded contamination from paint and glass before polishing.",
  "t":["fine / mild","medium / regular","aggressive / heavy","clay mitt, towel or pad (synthetic clay)","clay kit with lubricant"],
  "s":"https://www.autoexpress.co.uk/product-group-tests/36221/best-clay-bars",
  "m":[["Mild Clay","CarPro"],["Clay Regular","Bilt Hamber"],["Cleanse Clay Bar","Angelwax"],["Fine Detailing Clay","Infinity Wax"],
       ["Clay Detailing Complete Kit","Autoglym"]]},
 {"n":"Iron and tar remover","a":"fallout remover · iron remover · tar and glue remover · bug and tar remover","d":"Chemical decontaminant that dissolves embedded iron particles, or solvent that removes tar, glue and bug residue.",
  "t":["iron / fallout remover (colour-change)","tar and glue remover (solvent)","bug and tar remover"],
  "s":"https://www.autoexpress.co.uk/product-group-tests/370240/best-tar-removers-2026",
  "m":[["Korrosol","Bilt Hamber"],["Fallout","26JPN"],["Purple Rain Iron Fallout Remover","Autobrite Direct"],["W6 Iron & General Fallout Remover","Gtechniq"],
       ["Nemesis","Angelwax"],["Intensive Tar Remover","Autoglym"],["W7 Tar & Glue Remover","Gtechniq"],["Advanced Tar & Glue Remover","Halfords"],
       ["Shift","Carbon Collective"]]},
 {"n":"Wash bucket and grit guard","a":"two-bucket wash · grit guard insert","d":"Wash bucket fitted with a grit-trapping insert, used in pairs (wash and rinse) to keep dirt off the mitt.",
  "t":["bucket only","grit guard insert","bucket with lid","bucket dolly / castor base"],
  "s":"https://esotericcarcare.com/grit-guard-insert",
  "m":[["Grit Guard Insert","Grit Guard"]]},
 {"n":"Glass cleaner","a":"car glass cleaner · rain repellent · glass treatment","d":"Streak-free cleaner for automotive glass, or a coating that makes rain bead and run off the windscreen.",
  "t":["glass cleaner","ceramic glass cleaner","glass wipes","rain repellent (glass treatment)","glass cleaner with rain repellent"],
  "s":"https://www.aol.com/tested-9-different-car-glass-140000759.html",
  "m":[["Perfect Clarity Glass Cleaner","Meguiar's"],["Cerami-X","Rain-X"],["Glass Cleaner + Rain Repellent","Rain-X"],["Rain-X original glass treatment","Rain-X"],
       ["Ceramic Glass Cleaner","Griot's Garage"],["Invisible Glass","Invisible Glass"],["Streak Free","Chemical Guys"],["Clarify","CarPro"],
       ["Glass Wipes","Armor All"]]},
]
K="knowledge"
brands=[
 {"n":"Autoglym","c":"United Kingdom","seg":"Mainstream car care","d":"British car-care maker known for its Bodywork Shampoo Conditioner and polishes.","lines":["Bodywork Shampoo Conditioner","Polar"],"sig":["Bodywork Shampoo Conditioner"],"s":K},
 {"n":"Meguiar's","c":"United States","seg":"Mainstream car care","d":"American car-care brand, owned by 3M, selling washes, waxes and polishes.","lines":["Ultimate","Gold Class"],"rel":["3M"],"s":K},
 {"n":"Turtle Wax","c":"United States","seg":"Mainstream car care","d":"American mass-market car-care brand best known for its car wax.","s":K},
 {"n":"Bilt Hamber","c":"United Kingdom","seg":"Enthusiast detailing","d":"British maker of detailing and anti-corrosion products; repeated winner of Auto Express washing tests.","lines":["Auto-Wash","Touch-Less","Auto-Wheel","Korrosol"],"s":"https://www.autoexpress.co.uk/product-group-tests/86454/best-car-shampoo"},
 {"n":"Chemical Guys","c":"United States","seg":"Enthusiast detailing","d":"American detailing-products brand with a wide retail range.","s":K},
 {"n":"Gyeon","c":"South Korea","seg":"Enthusiast detailing","d":"Korean detailing brand known for ceramic coatings and its Q2M maintenance range.","lines":["Q2M"],"s":K},
 {"n":"Auto Finesse","c":"United Kingdom","seg":"Enthusiast detailing","d":"British detailing brand selling washes, mitts and waxes.","s":"https://www.autofinesse.com/en/shop/wash/wash-mitts"},
 {"n":"Koch-Chemie","c":"Germany","seg":"Professional and enthusiast detailing","d":"German maker of professional vehicle-cleaning chemicals, also sold to enthusiasts.","s":K},
 {"n":"Rain-X","c":"United States","f":"1972","seg":"Glass care","d":"Water-repellent glass treatment brand invented by Howard G. Ohlhausen, now owned by ITW Global Brands.","lines":["Original glass treatment","washer fluid","wiper blades"],"rel":["Illinois Tool Works"],"s":"https://en.wikipedia.org/wiki/Rain-X"},
 {"n":"Gtechniq","c":"United Kingdom","seg":"Enthusiast detailing","d":"British maker of coatings and detailing chemicals.","s":K},
]
notes=("Tier shelf: models are market-covering brands plus independent test winners (Auto Express 2025–26 group tests for shampoo, snow foam, "
 "foam lances, wheel cleaners, clay, drying towels, tar removers; Which? 2026 car-wash kit test; Car Magazine fallout-remover guide; Car and Driver glass-cleaner test). "
 "No archetypes: these are consumables chosen on test results, not collected designs. Koch-Chemie appears only in the brand register because no retrieved test "
 "or page named a specific product. Two-bucket method recorded in the bucket kind definition. Car Magazine main site and Autocar returned 402 and were not used; "
 "Which? Best Buy names were behind login, so only the tested list was used. Brand facts marked knowledge omit founding years where unsure.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/G1/shelves/11_00.json"; t=p+".tmp"
json.dump(out,open(t,"w"),ensure_ascii=False,indent=1); os.replace(t,p)
