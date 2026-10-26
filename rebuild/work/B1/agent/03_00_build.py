import json, os
W='https://en.wikipedia.org/wiki/'
SF='https://www.sleepfoundation.org/best-bed-frames'
kinds=[
{"n":"Bed frame","a":"bedstead · panel bed","d":"A bed of headboard, side rails and usually a footboard that holds the mattress on slats, a box spring or a separate base.",
 "t":["panel bed","sleigh bed","storage bed","upholstered bed","headboard only","metal frame","wooden frame"],
 "s":"https://www.ikea.com/us/en/cat/bedframes-bm003/",
 "x":[{"n":"Sleigh bed","a":"","d":"Bed whose headboard and footboard curve or scroll outward like a sleigh, from French and American Empire furniture.","mk":"","y":"early 19th century","s":W+"Sleigh_bed",
   "v":[{"n":"Lannuier bedstead","mk":"Charles-Honoré Lannuier","y":"c. 1805–1808","d":"New York Empire bedstead in the Metropolitan Museum of Art"},
        {"n":"Modern sleigh bed","mk":"","y":"","d":"wood, iron, steel or aluminium with gentler curves"}],
   "dt":"heavy carved wood (period) · metal or upholstered (modern) · curve depth"}],
 "m":[["MALM","IKEA"],["BRIMNES","IKEA"],["TONSTAD","IKEA"],["HEMNES","IKEA"],["Claremont Bed Frame","DreamCloud"],["Santorini","Saatva"],["Wooden Bed Frame","Silk & Snow"]],
 "r":[["MALM","IKEA"],["BRIMNES","IKEA"],["SONGESAND","IKEA"],["TONSTAD","IKEA"]]},
{"n":"Platform bed","a":"","d":"A bed frame with a solid or slatted platform that takes a mattress without a separate base.","t":["low platform","high-rise platform","with storage"],
 "s":"https://www.ikea.com/us/en/cat/beds-bm003",
 "m":[["The Bed","Thuma"],["Platform Base","Nolah"],["High Rise Platform Bed","Brooklyn Bedding"]],
 "r":[["SONGESAND","IKEA"],["TONSTAD","IKEA"]]},
{"n":"Divan base","a":"divan bed","d":"An upholstered box base on which a mattress sits, often with drawers or a lift-up storage top.","t":["drawer divan","ottoman (lift-up) divan","sprung edge","platform top"],
 "s":"https://www.ikea.com/gb/en/cat/divan-beds-28433/","m":[["BALESTRAND","IKEA"]]},
{"n":"Slatted bed base","a":"slat base · bed slats","d":"A frame of flat or sprung slats that supports a mattress inside a bed frame.","t":["flat slats","sprung slats","adjustable (motorised) base"],
 "s":"https://www.ikea.com/ie/en/p/luroey-slatted-bed-base-90160211/","m":[["LUROY","IKEA"],["Adjustable Base Plus","Saatva"]]},
{"n":"Four-poster bed","a":"tester bed · canopy bed","d":"A bed with a tall post at each corner, often carrying a tester or canopy hung with curtains.",
 "t":["full tester","half-tester","canopy (fabric)","open posts (no tester)","carved wood","metal"],
 "s":"https://www.1stdibs.com/buy/4-poster-canopy-beds",
 "x":[{"n":"Medieval–Tudor curtained tester bed","a":"Elizabethan four-poster","d":"Ornate oak four-poster whose tester and backboard carried costly hangings and heraldry as a show of status.","mk":"","y":"15th–16th century","s":W+"Four-poster_bed",
   "v":[{"n":"Marriage bed of Henry VII","mk":"","y":"c. 1486","d":"thought to date from his marriage"},{"n":"Crathes Castle bed","mk":"","y":"16th century","d":"made for the castle's original owners"}],
   "dt":"carved oak · tester panel · curtain rails · heraldic decoration"},
  {"n":"Lit à colonnes","a":"","d":"French column-post bed with a full canopy.","mk":"","y":"19th century","s":W+"Four-poster_bed",
   "v":[{"n":"Château de Compiègne bed","mk":"","y":"19th century","d":"displayed at the château"}],"dt":"columns · full canopy · hangings"},
  {"n":"Lit à la polonaise","a":"","d":"Bed with equal upholstered head and footboards and bent poles holding a small crown canopy.","mk":"","y":"","s":W+"Canopy_bed","dt":"crown canopy · upholstered ends · drapery"},
  {"n":"Lit à la duchesse","a":"","d":"Bed with upholstered headboard and no posts, under a flat canopy projecting from the wall.","mk":"","y":"","s":W+"Canopy_bed",
   "v":[{"n":"Lit à l'ange","mk":"","y":"","d":"also lit à demi-ciel: canopy shorter than the bed (half-tester)"}],"dt":"wall-hung canopy · full or half length"},
  {"n":"Chinese canopy bed","a":"alcove bed","d":"Enclosed canopy bed, the main piece of household furniture and often part of a bride's dowry.","mk":"","y":"before 1911 (Qing examples)","s":W+"Canopy_bed","dt":"hardwood frame · carved panels · enclosure"}]},
{"n":"Daybed","a":"","d":"A bed with a back and sides that serves as a sofa by day and a bed by night.","t":["trundle daybed","outdoor daybed (roofed)","hanging daybed","metal","wood"],
 "s":"https://www.ikea.com/us/en/cat/bedframes-bm003/"},
{"n":"Charpai","a":"charpoy · khat · khatla · manja · manji · rope cot","d":"South Asian bed of a wooden frame on four legs, laced with a woven rope or tape sleeping surface.",
 "t":["natural-fibre rope (munj, cotton, date leaf)","plastic tape","metal frame","diagonal weave","diamond weave","carved or animal-form legs","daybed size"],
 "s":W+"Charpai"},
{"n":"Wall bed","a":"Murphy bed · pull-down bed · fold-down bed","d":"A bed hinged at one end that folds up to stand against the wall or inside a cabinet.",
 "t":["vertical","sideways (horizontal)","with desk or table","with sofa","with shelving","bunk wall bed","piston lift","spring lift"],
 "s":W+"Murphy_bed",
 "x":[{"n":"Murphy bed","a":"disappearing bed","d":"Pivoting, counterbalanced bed that swings up into a closet or wall; the name became generic in 1989.","mk":"Murphy Bed and Door Company","y":"c. 1900","s":W+"Murphy_bed",
   "v":[{"n":"Disappearing Bed patent","mk":"Murphy Bed and Door Company","y":"1912","d":"US patent of 18 June 1912"},{"n":"Design for a Bed patent","mk":"Murphy Bed and Door Company","y":"1916","d":"US patent of 27 June 1916"},{"n":"Modern piston or torsion-spring wall bed","mk":"","y":"","d":"lift assisted by pistons or springs"}],
   "dt":"pivot · counterbalance · cabinet or closet housing · bed size"},
  {"n":"Bureau bedstead","a":"","d":"Bed that folds into a piece of case furniture resembling a bureau.","mk":"Gillows of Lancaster and London","y":"18th century","s":W+"Murphy_bed",
   "v":[{"n":"Gillows bureau bedstead","mk":"Gillows of Lancaster and London","y":"1788","d":""}],"dt":"case furniture · folding frame"}]},
{"n":"Bunk bed","a":"bunks","d":"Two or more beds stacked one above the other on one frame.","tg":["baby"],
 "t":["twin over twin","twin over full","full over full","futon bunk","L-shaped","triple bunk","with trundle"],
 "s":"https://www.ikea.com/ae/en/cat/childrens-beds-18723","m":[["MYDAL","IKEA"],["SVARTA","IKEA"],["TUFFING","IKEA"],["VITVAL","IKEA"]]},
{"n":"Loft bed","a":"high sleeper · mezzanine bed","d":"A single bed raised high on a frame with a ladder, leaving open space beneath for a desk, storage or play.","tg":["baby"],
 "t":["mid sleeper","high sleeper","with desk","with trundle","triple loft"],
 "s":"https://www.ikea.com/ae/en/cat/childrens-beds-18723"},
{"n":"Camp bed","a":"cot (US) · field bed","d":"A light, narrow folding bed of cloth stretched on a frame, used for camping or guests.","t":["X-frame","folding sections","with mosquito net","aluminium","wood and canvas"],
 "s":"https://www.remodelista.com/shop/category/folding-beds-camp-beds/",
 "x":[{"n":"Sectional folding camp bed","a":"","d":"Bed in hinged sections that folds flat for carrying.","mk":"","y":"c. 1330 BC onward","s":W+"Camp_bed",
   "v":[{"n":"Tutankhamun's folding bed","mk":"","y":"c. 1332–1323 BC","d":"three sections folding into a Z, found 1922"},{"n":"George Washington's camp bed","mk":"","y":"18th century","d":"wood-and-canvas, X-shaped base with iron mounts; New-York Historical Society"}],
   "dt":"sections · X-base · canvas · iron mounts"},
  {"n":"Campaign bed","a":"Napoleonic camp bed","d":"Officer's portable bed with wheeled legs and posts able to carry a canopy.","mk":"","y":"early 19th century","s":W+"Camp_bed",
   "v":[{"n":"Napoleon's camp bed","mk":"","y":"to 1821","d":"gilt copper frame, six wheeled legs"}],"dt":"metal frame · wheels · canopy posts"},
  {"n":"Military folding cot","a":"army cot","d":"Mass-made canvas-on-folding-frame bed issued to soldiers and used in shelters.","mk":"","y":"20th century","s":W+"Camp_bed",
   "v":[{"n":"American Army folding bed","mk":"","y":"World War II","d":""},{"n":"WW2 Folding Camp Bed","mk":"Topos Workshop","y":"","d":"reproduction/retail version"}],"dt":"canvas · wood or aluminium legs"}]},
]
brands=[
{"n":"IKEA","c":"Sweden","f":"1943","seg":"Mass-market flat-pack furniture","d":"Swedish-founded flat-pack furniture and homeware retailer.","s":"knowledge"},
{"n":"Saatva","c":"United States","seg":"Online mattress and bed brand","d":"US direct-to-consumer maker of mattresses, bed frames and adjustable bases.","s":"knowledge"},
{"n":"DreamCloud","c":"United States","seg":"Online mattress and bed brand","d":"US direct-to-consumer mattress brand that also sells bed frames.","s":"knowledge"},
{"n":"Murphy Bed and Door Company","c":"United States","seg":"Wall beds","d":"Company led by William Lawrence Murphy (1876–1957), originator of the pivoting wall bed.","sig":["Murphy bed"],"s":W+"Murphy_bed"},
{"n":"Gillows of Lancaster and London","c":"United Kingdom","seg":"Georgian cabinet makers","d":"Lancaster and London cabinet makers; made a bureau bedstead in 1788.","sig":["Bureau bedstead"],"s":W+"Murphy_bed"},
]
trads=[
{"n":"Charpai rope-bed weaving","g":"Woodwork & furniture","r":"Indian subcontinent (Pakistan, north and central India, Bihar), Afghanistan, Myanmar","p":"attested from 2nd century BC; described by Ibn Battuta in the 1300s",
 "d":"Hand-built bed frame of four legs and four rails, laced with a rope surface that can be retensioned.","tech":"diagonal (bias) weave; short end laced to the foot rail (badaan) to adjust tension",
 "mat":"wooden legs and rails; munj, cotton or date-leaf rope; modern plastic tape and metal",
 "forms":["Charpai","Rajasthani diamond-weave daybed","small Pakistani charpai"],"ctr":[],"auth":"wooden paaga legs and iss/upala rails jointed without a fixed platform; hand-laced natural-fibre webbing with a tensioning end","s":W+"Charpai"},
]
notes=("Four-poster: all nine 1stdibs dealer SKUs dropped (brief: cut 1stdibs SKUs); canopy, full tester and half-tester as types; period forms as archetypes "
 "(medieval–Tudor tester bed, lit à colonnes, lit à la polonaise, lit à la duchesse/lit à l'ange, Chinese canopy bed). Bed frame: IKEA trimmed from 12 models to 4 "
 "(MALM, BRIMNES, TONSTAD, HEMNES dropped? no: HEMNES not in old data) ")
# fix: no HEMNES (not in old data)
kinds[0]["m"]=[m for m in kinds[0]["m"] if m[0]!="HEMNES"]
notes=("Four-poster: all nine 1stdibs dealer SKUs dropped (brief: cut 1stdibs SKUs); canopy, full tester and half-tester are types; period forms are archetypes "
 "(medieval–Tudor tester bed, lit à colonnes, lit à la polonaise, lit à la duchesse with lit à l'ange version, Chinese canopy bed). "
 "Bed frame: IKEA cut from 12 models to 3 (MALM, BRIMNES, TONSTAD; ranges kept incl. SONGESAND) plus Sleep Foundation test picks (DreamCloud Claremont best overall, Saatva Santorini, Silk & Snow); "
 "sleigh bed is an archetype and a type. Platform bed gets Sleep Foundation picks (Thuma, Nolah, Brooklyn Bedding); Saatva Adjustable Base Plus under slatted base. "
 "New kinds Charpai (with tradition entry) and Wall bed (Murphy bed and Gillows bureau bedstead archetypes). Bunk and loft beds tagged baby (mostly children's rooms; CPSC top bunk age 6+). "
 "Camp bed: archetypes from Wikipedia; old Topos Workshop model kept as a version. No daybed archetypes (Barcelona daybed etc. not confirmed on a retrieved page). "
 "Brand entries for Thuma, Nolah, Brooklyn Bedding, Silk & Snow left out (facts not known reliably). No UK test (Which?) data retrieved.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/B1/shelves/03_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
