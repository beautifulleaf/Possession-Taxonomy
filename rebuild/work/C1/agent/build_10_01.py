import json, os
W='/home/user/Possession-Taxonomy/rebuild/work/C1/'
kinds=[
{"n":"Work gloves","a":"safety gloves · rigger gloves · protective gloves","d":"Gloves worn to protect the hands from cuts, abrasion, impact, heat or cold during work.",
 "t":["leather rigger","coated knit (nitrile, latex or PU palm)","cut-resistant (EN 388 level A–F)","impact-protected (EN 388 'P')","mechanic's","insulated winter","waterproof","chainsaw gloves (EN ISO 11393-4)","welding gauntlets"],
 "s":"https://satra.com/spotlight/article.php?id=488",
 "m":[["Ranchworx","Ironclad"],["Tuff Chix","Ironclad"],["1164 HydraHyde","Wells Lamont"],["Hybrid Plus","Youngstown Glove Co."],["ProFlex 850 Freezer","Ergodyne"],["T-Rex Flex TRX818","Magid"],["M-Pact","Mechanix Wear"]]},
{"n":"Hi-vis vest","a":"high-visibility vest · hi-vis clothing · safety vest","d":"Sleeveless fluorescent vest with reflective bands, worn for visibility.",
 "t":["ANSI/ISEA 107 Class 1, 2 or 3","EN ISO 20471 class","ANSI/ISEA 207 public-safety vest","breakaway (5-point)","surveyor's (pockets)","yellow, orange or green"],
 "s":"https://www.hivissupply.com/ansi-class-2-safety-vests.html"},
{"n":"Chainsaw trousers","a":"chainsaw pants · forestry trousers","d":"Trousers with cut-resistant layers that clog a running chain, worn for chainsaw work.",
 "t":["Class 1 (20 m/s)","Class 2 (24 m/s)","Class 3 (28 m/s)","Design A (front only)","Design A Plus (adds rear ankle to knee)","Design C (all-round)","EN ISO 11393-2 (formerly EN 381-5)","vented"],
 "s":"https://www.stihl.co.uk/en/ap/function-core-trousers-199347",
 "m":[["Breatheflex AT4010","Arbortec Forestwear"],["Breatheflex Pro AT4060","Arbortec Forestwear"],["Vented Chainsaw Pants AT4062","Arbortec Forestwear"],["Technical chainsaw trousers","Husqvarna"],["Technical Robust chainsaw trousers","Husqvarna"],["ADVANCE X-Light trousers","STIHL"],["ADVANCE FlexTEC trousers","STIHL"],["FUNCTION Universal trousers","STIHL"]]},
{"n":"Chainsaw chaps","a":"chainsaw leggings · chaps","d":"Cut-resistant leg aprons strapped over ordinary trousers for chainsaw work.",
 "t":["front apron","270-degree wrap","protection class"],
 "s":"https://shop.stihl.com.au/personal-protective-equipment/pants",
 "m":[["FUNCTION Core 270 Degree Chaps","STIHL"],["Professional Protection Chaps","STIHL"]]},
{"n":"Knee pads","a":"kneepads · knee protectors","d":"Strap-on pads that cushion and protect the knees during long kneeling.",
 "t":["hard cap","soft foam","gel","hinged","flat stabiliser cap","trouser-insert pads"],
 "s":"https://www.bobvila.com/reviews/best-knee-pads-2026/",
 "m":[["Hybrid Ultra Flex III KneePro","Sellstrom"],["Knee Pads For Work","WorkPro"],["AP16 All-Purpose","ProKnee"],["Stabilizer Knee Pads","Milwaukee"],["Heavy-Duty Hinged Knee Pads","Klein Tools"],["Flooring Knee Pads with Gel","DeWalt"],["GelGuard Pro","NoCry"],["GelFit Black Stabilizer","ToughBuilt"]]},
{"n":"Fall-arrest harness","a":"safety harness · full-body harness","d":"Full-body webbing harness that spreads the force of stopping a fall across shoulders, thighs and pelvis.",
 "t":["full-body (fall arrest)","chest harness","work-positioning","rescue","ANSI Z359.11 / CSA Z259.10","quick-connect or tongue-buckle legs"],
 "s":"https://en.wikipedia.org/wiki/Safety_harness",
 "m":[["DBI-SALA ExoFit NEX","3M"],["Scorpion Safety Harness","KwikSafety"],["Velocity","Guardian"],["Warthog Comfort MAXX","Malta Dynamics"]]}
]
brands=[
 {"n":"STIHL","c":"Germany","f":"1926","seg":"Professional & flagship","kf":"Chainsaws and forestry PPE","d":"Waiblingen chainsaw maker that also sells forestry protective clothing.","lines":["FUNCTION","ADVANCE"],"rel":["Husqvarna"],"s":"knowledge"},
 {"n":"Husqvarna","c":"Sweden","f":"1689","seg":"Professional & flagship","kf":"Chainsaws and forestry PPE","d":"Swedish maker of chainsaws, garden machinery and forestry protective clothing.","lines":["Technical"],"rel":["STIHL"],"s":"knowledge"}
]
notes=("Kept all 4 old kinds; added Work gloves, Knee pads and Fall-arrest harness (new, sourced; models from Bob Vila / BestReviews test lists). "
 "Chainsaw trousers trimmed from 13 to 8 models (dropped AT4015 Design A Plus, FS PROTECT, FUNCTION Core, Government and Utility trousers, AT4070); protection class and design moved to t. "
 "Chainsaw chaps kept as their own kind (plan lists it) but trimmed to 2 models (dropped Government and Utility chaps). Hi-vis vest generic models (breakaway, surveyor's) moved to t. "
 "Incoming A1 hi-vis clothing/workwear kinds arrive via moves and are not built here. No archetypes: this is a tier/restraint shelf.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
tmp=W+'shelves/10_01.json.tmp'; json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,W+'shelves/10_01.json')
