import json, os
W="https://en.wikipedia.org/wiki/"
MSC="https://www.mscdirect.com/resources/buying-guides/pliers"
kinds=[
{"n":"Combination pliers","a":"lineman's pliers · linesman pliers · Kleins","d":"Pliers with flat gripping jaws and side cutters, for gripping, bending and cutting wire.",
 "t":["VDE insulated","high-leverage","with crimper"],"s":"https://toolstation.com/hand-tools/pliers/c30",
 "x":[{"n":"Lineman's pliers","a":"Klein pattern","d":"Stub-nosed side-cutting pliers first sold by Mathias Klein & Sons; the reference combination plier.","mk":"Klein Tools","y":"early 20th century","s":W+"Lineman%27s_pliers",
   "v":[],"dt":"length 7–9 in · insulated or plain handles · crimper or not"}],
 "m":[["CK Redline VDE combination pliers","CK"],["NWS Combimax multi-function pliers","NWS"],["Stanley Control Grip combination pliers","Stanley"]],
 "r":[["Control Grip","Stanley"]]},
{"n":"Tongue and groove pliers","a":"water pump pliers · groove-joint pliers · Channellocks · multigrips","d":"Pliers with a grooved joint giving several jaw widths, for large or irregular objects.",
 "t":["straight jaw","V-jaw","push-button adjustment","parallel jaw"],"s":MSC,
 "x":[
  {"n":"Higgins adjustable pliers","d":"Blacksmith's adjustable-joint pliers, the first patented tongue-and-groove design.","mk":"","y":"1899","s":W+"Tongue-and-groove_pliers",
   "v":[{"n":"Canadian patent CA64246A","mk":"","y":"1899","d":"Vernon Graham Higgins, Fortuna, California"}],"dt":""},
  {"n":"Channellock tongue-and-groove pliers","d":"Modern tongue-and-groove design that gave the tool its common name, with sky-blue grips.","mk":"Channellock","y":"1933",
   "s":W+"Channellock","v":[{"n":"Manning design","mk":"Channellock","y":"1933","d":"Howard Manning; US patent 1934"},{"n":"Sky-blue grips","mk":"Channellock","y":"1956","d":"trademarked handle colour"}],"dt":"length · straight or V jaw"},
  {"n":"Cobra","d":"Knipex water pump pliers with push-button one-handed jaw adjustment.","mk":"Knipex","y":"1984","s":W+"Knipex",
   "v":[{"n":"Cobra water pump pliers","mk":"Knipex","y":"1984","d":"replaced the Alligator pliers"}],"dt":"length 125–560 mm · handle grips"},
  {"n":"Pliers Wrench","d":"Knipex parallel-jaw adjustable pliers that grip nuts flat, made to replace a set of spanners.","mk":"Knipex","y":"1994","s":W+"Knipex","v":[],"dt":"length · jaw capacity"}]},
{"n":"Locking pliers","a":"Vise-Grips · Mole grips · mole wrench","d":"Pliers with a toggle-link mechanism that locks the jaws on the work, adjustable by a screw.",
 "t":["curved jaw","straight jaw","long nose","C-clamp","welding clamp"],"s":MSC,
 "x":[
  {"n":"Vise-Grip","d":"The original locking pliers, invented by blacksmith William S. Petersen.","mk":"Irwin","y":"1924","s":W+"Irwin_Industrial_Tools",
   "v":[{"n":"Petersen original","mk":"","y":"1924","d":"DeWitt, Nebraska"},{"n":"Petersen Manufacturing production","mk":"","y":"1934","d":"company formed to make Vise-Grips"}],"dt":"size · jaw style"},
  {"n":"Mole grips","a":"Mole wrench","d":"British locking pliers nearly identical to the Vise-Grip.","mk":"M.K. Mole and Son","y":"1955","s":W+"Locking_pliers","v":[],"dt":"size · jaw style"}],
 "m":[["Milwaukee Torque Lock curved jaw pliers","Milwaukee"]]},
{"n":"Long nose pliers","a":"needle nose pliers · snipe-nose pliers · chain nose pliers","d":"Pliers with slim tapering jaws for tight spaces, bending wire and gripping small parts.",
 "t":["straight","bent nose","round nose","with cutter"],"s":MSC},
{"n":"Cutting pliers","a":"side cutters · diagonal cutters · end cutting pliers · nippers · dikes","d":"Pliers whose jaws are edged for cutting wire, including side cutters and end cutters.",
 "t":["symmetrical diagonal","flush cutter","compound-action","high-leverage","end cutter"],"s":MSC,
 "x":[{"n":"TwinForce","d":"Knipex high-leverage side and diagonal cutter line.","mk":"Knipex","y":"","s":W+"Knipex","v":[],"dt":"length · insulated or not"}]},
{"n":"Slip joint pliers","a":"","d":"Pliers with a two-position joint that sets the jaw opening, for gripping and turning.",
 "t":["straight slip joint","multiple-position"],"s":MSC},
{"n":"Wire stripper","a":"","d":"Hand tool that removes insulation from electrical wire without nicking the conductor.",
 "t":["notched manual","screw-adjusted (European style)","automatic (self-adjusting)"],"s":W+"Wire_stripper",
 "x":[{"n":"Compound automatic wire stripper","d":"One squeeze grips the wire, cuts the insulation and pulls it off.","mk":"","y":"1915","s":W+"Wire_stripper",
   "v":[{"n":"Wood patent","mk":"","y":"1915","d":"Stuart G. Wood, Brooklyn"},{"n":"Wood refinement","mk":"","y":"1943","d":""},{"n":"Hindenburg refinement","mk":"","y":"1959","d":"Eugene D. Hindenburg"}],"dt":"wire gauge range"}]},
{"n":"Crimping tool","a":"crimper · crimping pliers","d":"Pliers that deform a connector or terminal on to a wire to join them.",
 "t":["ratchet crimper","insulated terminal","modular (RJ45)","ferrule","hydraulic"],"s":W+"Crimp_(electrical)"}]
brands=[
{"n":"Knipex","c":"Germany","f":"1882","seg":"premium pliers","d":"Family-owned Wuppertal plier maker founded by Carl Gustav Putsch.","lines":["Cobra","Pliers Wrench","TwinForce"],"eras":["Ralf Putsch, since 1996"],"sig":["Cobra","Pliers Wrench"],"sc":[],"rel":[],"s":W+"Knipex"},
{"n":"Channellock","c":"United States","f":"1886","seg":"pliers","d":"Meadville, Pennsylvania plier maker founded by George B. DeArment; originator of modern tongue-and-groove pliers.","lines":[],"eras":[],"sig":["Channellock tongue-and-groove pliers"],"sc":[],"rel":[],"s":W+"Channellock"},
{"n":"Klein Tools","c":"United States","f":"1857","seg":"electricians' hand tools","d":"Chicago-founded maker of electricians' tools whose name became generic for lineman's pliers.","lines":["Journeyman"],"eras":[],"sig":["Lineman's pliers"],"sc":[],"rel":[],"s":W+"Klein_Tools"},
{"n":"Irwin","c":"United States","f":"1885","seg":"hand tools and accessories","d":"American tool brand, owner of Vise-Grip; part of Stanley Black & Decker since 2017.","lines":["Vise-Grip"],"eras":[],"sig":["Vise-Grip"],"sc":[],"rel":[],"s":W+"Irwin_Industrial_Tools"},
{"n":"M.K. Mole and Son","c":"United Kingdom","f":"","seg":"locking pliers","d":"British maker of Mole grips from 1955.","lines":["Mole grips"],"eras":[],"sig":["Mole grips"],"sc":[],"rel":[],"s":W+"Locking_pliers"}]
notes=("All 6 old kinds kept; 'Combination and other pliers' renamed Combination pliers (lineman's pliers merged as its archetype). New: Wire stripper, Crimping tool. "
 "Dropped generic placeholder models ('combination pliers', 'water pump pliers', etc.) and moved the Vise-Grip range to Locking pliers. "
 "Left out: Vise-Grip 10WR model number and Klein side-cutter model (no retrieved source); no crimper/stripper models (no retrieved model pages).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/C1/shelves/02_01.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
