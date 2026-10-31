import json,os
W='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"First-aid kit","a":"Verbandkasten · first-aid box · grab bag","d":"Boxed or bagged set of dressings and basics sold as one product; compare by the standard and size class it meets.",
 "t":["Home & leisure","Car / motor vehicle (DIN 13164 in Germany; BS 8599-2 in UK)","Workplace (BS 8599-1 small, medium, large; DIN 13157/13169; ANSI/ISEA Z308.1)","Travel","Outdoor & wilderness (group size × trip length)","Trauma / IFAK (tourniquet, chest seal, haemostatic dressing)"],
 "s":W+"First_aid_kit",
 "m":[["St John Ambulance Home First Aid Kit","St John Ambulance"],["St John Ambulance Small Workplace First Aid Kit BS 8599-1:2019","St John Ambulance"],["St John Ambulance Small Motor Vehicle First Aid Kit BS 8599-2:2014","St John Ambulance"],["Aura3 BS 8599-1 medium workplace kit","Reliance Medical"],["Verbandskasten Klassik DIN 13164","Holthaus Medical"],["Holthaus Office 63158","Holthaus Medical"],["Söhngen Kiel","Söhngen"],["Söhngen Office","Söhngen"],["Leina-Werke KFZ Euro","Leina-Werke"],["Leina-Werke Standard","Leina-Werke"],["Kalff compact","Kalff"]]},
{"n":"Plaster","a":"adhesive bandage · sticking plaster · Band-Aid · Elastoplast","d":"Small dressing pad on an adhesive strip for minor cuts; blister plasters use a hydrocolloid gel cushion.",
 "t":["Fabric (flexible)","Waterproof / washproof film","Sensitive skin","Children's printed","Blister plaster (hydrocolloid)","Hydrogel / transparent","Strip roll to cut"],
 "s":W+"Adhesive_bandage",
 "m":[["Band-Aid adhesive bandages","Band-Aid"],["Elastoplast plasters","Elastoplast"],["Hansaplast Universal Strips","Hansaplast"],["Hansaplast Sensitive Sterile","Hansaplast"],["Compeed blister plasters (hydrocolloid)","Compeed"],["Nexcare Happy Kids Mix","Nexcare"],["DermaPlast Textile plaster","DermaPlast"]]},
{"n":"Bandage","a":"roller bandage · gauze bandage · triangular bandage · sling · tubular bandage","d":"Strip, tube or triangle of fabric used to hold a dressing, support a limb or make a sling.",
 "t":["Roller (gauze, conforming)","Triangular (sling, cravat)","Tubular (elastic or gauze tube)","Cohesive (self-adhering)","Compression / elastic (short-stretch, long-stretch)"],
 "s":W+"Bandage"},
{"n":"Wound-closure strip","a":"Steri-Strip · butterfly closure · butterfly stitch","d":"Thin porous adhesive strips that pull the edges of a small cut together while it heals.",
 "t":["Strip","Butterfly shape"],"s":W+"Steri-Strip",
 "m":[["Steri-Strip","Nexcare"]]},
{"n":"Liquid bandage","a":"spray plaster · liquid plaster","d":"Liquid or spray that dries to a thin protective polymer film over a minor wound.",
 "t":["Brush-on liquid","Spray"],"s":W+"Liquid_bandage",
 "m":[["Nexcare liquid bandage","Nexcare"]]},
{"n":"Home defibrillator","a":"home AED · automated external defibrillator · public-access defibrillator","d":"Automated external defibrillator kept at home or in a community cabinet that analyses heart rhythm and guides the rescuer with voice prompts.",
 "t":["Semi-automatic (rescuer presses shock)","Fully automatic","With CPR feedback","Spare parts: electrode pads, battery, carry case, wall cabinet"],
 "s":W+"Automated_external_defibrillator",
 "m":[["HeartStart Home (M5068A)","Philips"],["HeartStart OnSite (M5066A)","Philips"],["AED Plus","ZOLL"]]},
]
brands=[
{"n":"St John Ambulance","c":"United Kingdom","f":"1877","seg":"First-aid charity; first-aid training and kits","d":"First-aid charity founded in England as the St John Ambulance Association, selling home, vehicle and BS 8599 workplace kits.","lines":["Home First Aid Kit","Universal First Aid Kit Grab Bag","Workplace kits BS 8599-1","Motor vehicle kits BS 8599-2"],"rel":["Reliance Medical"],"s":W+"St_John_Ambulance"},
{"n":"Band-Aid","c":"United States","f":"1920","seg":"Plasters; Kenvue (spun off from Johnson & Johnson, 2023)","d":"Adhesive-bandage brand invented by Johnson & Johnson employee Earle Dickson; a genericised name for plasters in the US, Canada, Australia and India.","rel":["Elastoplast","Nexcare","Compeed"],"s":W+"Band-Aid"},
{"n":"Elastoplast","c":"","f":"","seg":"Plasters and dressings; Beiersdorf","d":"Plaster and dressing brand made under licence by Smith & Nephew from 1928 and owned by Beiersdorf since 2000; sold as Hansaplast in parts of Europe.","lines":["Hansaplast (Beiersdorf, from 1922)","Curitas (Latin America)","Airstrip","SilverHealing"],"rel":["Hansaplast","Band-Aid"],"s":W+"Elastoplast"},
{"n":"Compeed","c":"Denmark","f":"1986","seg":"Hydrocolloid blister plasters; HRA Pharma","d":"Hydrocolloid gel plaster brand for blisters, corns and cold sores, developed at Coloplast and owned by HRA Pharma since 2017.","sig":["Blister plaster"],"rel":["Band-Aid","Elastoplast"],"s":W+"Compeed"},
{"n":"Nexcare","c":"United States","f":"1994","seg":"3M personal health care brand","d":"3M brand for plasters, tapes, gauze, cold-sore treatments, liquid bandages and Steri-Strip wound-closure strips.","lines":["Steri-Strip","Liquid bandage","Happy Kids plasters"],"rel":["Band-Aid"],"s":W+"Nexcare"},
{"n":"Philips","c":"Netherlands","f":"1891","seg":"Health technology group","d":"Amsterdam-based health-technology company whose HeartStart Home and OnSite are over-the-counter AEDs in the US.","lines":["HeartStart Home","HeartStart OnSite"],"rel":["ZOLL"],"s":"https://www.philips.com/a-w/about/news/archive/standard/news/press/2019/20190619-philips-receives-fda-premarket-approval-for-its-heartstart-onsite-and-heartstart-home-defibrillators.html"},
]
notes=("Merged Plaster + Blister plaster (blister now a type; Compeed listed). Merged Roller, Triangular and Tubular bandage into Bandage (types; cohesive and compression added from the Bandage article). "
"First-aid kit cut from 14 SKUs to 11: St John Ambulance (UK shop listing), Reliance Medical Aura3 (BHF shop) and Holthaus Klassik DIN 13164 added from retrieved pages; dropped Flexeo, Gramm-Medical, Petex, WERKSTEIN, two Holthaus SKUs and Leina-Werke Star II as SKU noise. "
"Adventure Medical Kits left out: product pages (REI, Cabela's) blocked, so no model could be confirmed. Home defibrillator added (Philips HeartStart Home M5068A / OnSite M5066A from Philips 2019 FDA release; ZOLL AED Plus from Canadian Red Cross shop). "
"No ZOLL brand entry: Wikipedia page not found and Wikidata Q118075142 has no country or founding date. Elastoplast country left blank (not stated on the page). No traditions (not relevant). Plaster types kept from the brief; no test-winner (Which?/CR) data retrieved for plasters or kits.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/H2/shelves/02_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
