import json, os
B="Bauerfeind"; F="FUTURO (3M)"; D="DonJoy"; P="Push"
kinds=[
{"n":"Knee support","a":"knee brace · knee sleeve · knee stabiliser","d":"Elastic sleeve, strapped stabiliser or hinged brace worn to support a sore, unstable or injured knee.",
 "t":["Compression sleeve","Open-patella or patella-ring support","Strapped or side-stabilised support","Hinged brace","Patella (knee) strap","Osteoarthritis unloader brace","Post-operative range-of-motion brace"],
 "s":"https://en.wikipedia.org/wiki/Knee_brace",
 "m":[["GenuTrain",B],["GenuTrain S (hinged)",B],["GenuTrain A3 (arthritis)",B],["GenuTrain OA (unloader)",B],["Genumedi","medi"],
      ["Performance Knee Stabilizer",F],["Hinged Knee Brace",F],["Defiance III",D],["Performance Bionic FullStop",D],["Knee Brace with Patella Support (Push Med)",P]]},
{"n":"Ankle support","a":"ankle brace · ankle sleeve · ankle stabiliser","d":"Sleeve, strapped or stirrup brace worn to steady the ankle after a sprain or to prevent one.",
 "t":["Compression sleeve","Figure-8 strap brace","Lace-up brace","Stirrup (rigid-shell) brace","Walker boot (immobilising)"],
 "s":"https://en.wikipedia.org/wiki/Ankle_brace",
 "m":[["MalleoTrain",B],["MalleoTrain Plus",B],["MalleoLoc",B],["Ankle Brace 8 (Push Sports)",P],["Aequi Flex (Push Med)",P],
      ["Stabilizing Pro Ankle Brace",D],["Velocity ES",D],["Performance Ankle Stabilizer",F],["Stirrup Ankle Brace",F]]},
{"n":"Back support","a":"back brace · lumbar support · posture corrector","d":"Belt, brace or harness that supports the lower back or holds the shoulders back.",
 "t":["Elastic lumbar belt","Rigid-stay lumbar brace","Posture corrector","Abdominal binder"],
 "s":"https://www.3m.com/3M/en_US/p/d/v100558159/",
 "m":[["Easy Adjustable Back Support",F],["Comfort Stabilizing Back Support",F],["Posture Corrector",F],["Push Med Back Brace",P],["Push Care Back Brace",P]]},
{"n":"Wrist & hand support","a":"wrist brace · wrist splint · thumb stabiliser","d":"Brace, splint or sleeve that supports the wrist, hand or thumb.",
 "t":["Compression sleeve or glove","Splinted wrist brace","Night wrist splint","Thumb stabiliser"],
 "s":"https://bauerfeind.us/wrist-brace-manutrain-titan-blue-2-left",
 "m":[["ManuTrain","Bauerfeind"],["Deluxe Wrist Stabilizer",F],["Adjustable Night Wrist Sleep Support",F],["Deluxe Thumb Stabilizer",F],["Push Med Wrist & Hand Brace",P],["Push Med Splint Wrist Brace",P]]},
{"n":"Elbow support","a":"elbow brace · tennis-elbow strap · epicondylitis clasp","d":"Brace, strap or sleeve that supports the elbow.",
 "t":["Compression sleeve","Tennis/golfer's-elbow strap","Hinged range-of-motion elbow brace"],
 "s":"https://www.bauerfeind.com.au/products/epitrain",
 "m":[["EpiTrain","Bauerfeind"],["Tennis Elbow Strap",F],["Sport Elbow Support",F],["Push Med Epi Elbow Brace",P],["X-Act ROM Elbow",D]]},
{"n":"Neck support","a":"cervical collar · neck brace","d":"Soft or rigid collar that supports the neck.",
 "t":["Soft foam collar","Rigid or adjustable collar"],
 "s":"https://www.ottobock.com/en-gb/product/50C91",
 "m":[["Smartspine Universal Collar","Ottobock"],["Cervical Collar",F],["Push Med Neck Brace",P]]},
{"n":"Orthotic insole","a":"orthotics · arch-support insole · foot orthosis","d":"Shoe insert that supports the arch or redistributes pressure to treat or prevent foot pain.",
 "t":["Prefabricated (off-the-shelf)","Custom-made from a foot cast or scan","Full or ¾ length","Low, medium or high arch","Heat-mouldable","With metatarsal pad","Sport-specific (running, court)"],
 "s":"https://en.wikipedia.org/wiki/Orthotics",
 "m":[["All-Purpose Support (low, medium, high arch)","Superfeet"],["Run Support","Superfeet"],["Pinnacle","Powerstep"],["Pinnacle Maxx","Powerstep"],
      ["Advanced Pain Relief Plantar Fasciitis Orthotic Insoles","Dr. Scholl's"],["RunPro","Currex"],["Premium Memory Foam Orthotics","Aetrex"]]},
{"n":"Compression stocking","a":"compression socks · support stockings · graduated compression hosiery","d":"Stocking with graduated pressure, strongest at the ankle, for leg veins, swelling or travel.",
 "t":["Support (OTC, about 8–20 mmHg)","Firm medical (20–30, 30–40 mmHg)","Anti-embolism (TED)","Knee-high","Thigh-high","Tights/pantyhose","Maternity","Circular knit or flat knit","Made-to-measure"],
 "s":"https://en.wikipedia.org/wiki/Compression_stockings",
 "m":[["Jobst Ultrasheer","BSN Jobst"],["Jobst forMen","BSN Jobst"],["Jobst ActiveWear","BSN Jobst"],["mediven Comfort","medi"],["mediven Plus","medi"],["mediven Sheer & Soft","medi"],
      ["Style (bamboo socks)","Sigvaris"],["Juzo Expert Feel","Juzo"]]},
]
brands=[
{"n":"Bauerfeind","c":"Germany","f":"1929","seg":"Medical supports, orthoses, compression stockings and insoles","d":"Zeulenroda-based maker of knitted supports, orthoses, compression stockings and orthopaedic insoles.",
 "lines":["Train supports (GenuTrain, MalleoTrain, EpiTrain, ManuTrain)","Sports supports"],"sig":["GenuTrain","MalleoTrain"],"rel":["medi","Ottobock"],"s":"https://en.wikipedia.org/wiki/Bauerfeind"},
{"n":"Ottobock","c":"Germany","f":"1919","seg":"Prosthetics and orthotics","d":"Duderstadt-based prosthetics leader that also makes orthoses, wheelchairs and exoskeletons.",
 "lines":["Smartspine"],"sig":["Smartspine Universal Collar"],"rel":["Bauerfeind"],"s":"https://en.wikipedia.org/wiki/Ottobock"},
{"n":"DonJoy","c":"United States","f":"1978","seg":"Orthopaedic bracing (Enovis, formerly DJO)","d":"Bracing brand begun in a Carlsbad garage, now part of Enovis, known for ligament knee braces.",
 "lines":["Defiance","Performance","Velocity"],"sig":["Defiance III"],"rel":["Bauerfeind","Push"],"s":"https://en.wikipedia.org/wiki/DJO_Global"},
{"n":"Dr. Scholl's","c":"United States","f":"1906","seg":"Mass-market foot care and insoles","d":"Foot-care brand founded by podiatrist William Mathias Scholl, sold as Scholl outside North America.",
 "lines":["Advanced Series","Custom Fit Orthotic Inserts"],"sig":["Advanced Pain Relief Plantar Fasciitis Orthotic Insoles"],"rel":["Superfeet","Powerstep"],"s":"https://en.wikipedia.org/wiki/Dr._Scholl%27s"},
]
notes=("Tier shelf. Added Knee support and Ankle support (Wikipedia sources) with Bauerfeind, medi, FUTURO, DonJoy and Push models. "
 "Insoles cut from 10 SKUs to 7 across Superfeet, Powerstep, Dr. Scholl's, Currex and Aetrex (dropped Pinnacle Plus Met, Run Cushion, Run Pacer Elite, Run Pain Relief). "
 "Compression stocking adds medi, Sigvaris and Juzo lines. Arm slings, abdominal and plantar-fasciitis night supports not added (outside planned kinds). "
 "No brand entries for FUTURO, Push, medi, Jobst, Sigvaris, Juzo, Superfeet, Powerstep, Currex or Aetrex: no retrieved page gave country/founding facts. No traditions apply.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/H2/shelves/02_01.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
