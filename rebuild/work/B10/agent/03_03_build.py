import json, os
SK='https://en.wikipedia.org/wiki/Protein_skimmer'
CR='https://en.wikipedia.org/wiki/Calcium_reactor'
RA='https://en.wikipedia.org/wiki/Reef_aquarium'
RS='https://reefsupplies.ca/collections/protein-skimmers?page=1'
CURVE='https://gensou.sg/?p=33357'
VT='https://reefbuilders.com/2013/05/21/trip-memory-lane-ecotech-marine-vortech-pump-controllers'
WM='https://gensou.sg/?p=41260'
PFK='https://www.practicalfishkeeping.co.uk/fishkeeping-news/new-maxspect-gyre-generator/'
SALT='https://gensou.sg/?p=41259'
RD='https://www.coralmagazine.com/2021/04/30/red-sea-introduces-reefdose-dosing-pumps/'
DOS='https://reefbuilders.com/2017/09/13/five-new-products-shaping-the-future-of-reef-tanks-part-3-smart-dosing-pumps'
ATO='https://www.bulkreefsupply.com/content/post/best-ato-system-of-2019'
CAR='https://gensou.sg/?p=22444'
kinds=[
 {"n":"Protein skimmer","a":"foam fractionator · skimmer","d":"Device that strips dissolved organic waste from marine tank water by foam fractionation into a collection cup.",
  "t":["in-sump","hang-on-back","internal","cone body","needle-wheel pump","air stone","venturi","downdraft","Beckett","DC pump with controller"],
  "s":SK,
  "x":[
   {"n":"Needle-wheel skimmer","a":"aspirating pinwheel skimmer","d":"Pump-driven skimmer whose impeller pins chop air into fine bubbles; the most popular type in home reef tanks.","mk":"","y":"","s":SK,"v":[],"dt":"in-sump, hang-on or internal · pump · body shape"},
   {"n":"Cone skimmer","a":"conical skimmer","d":"Skimmer with a cone-shaped body, widely sold from around 2006–2007.","mk":"","y":"c. 2006–2007","s":SK,
    "v":[{"n":"Revolution","mk":"Korallen-Zucht","y":"c. 2007","d":"Early cone skimmer line"}],"dt":"cone diameter · pump · acrylic"},
   {"n":"Beckett skimmer","a":"","d":"Skimmer that produces bubbles through a patented foam nozzle.","mk":"Beckett Corporation","y":"","s":SK,"v":[],"dt":"nozzle count · pump"},
   {"n":"Bubble Magus Curve","a":"Curve","d":"Compact in-sump cone skimmer with a needle-wheel pump, a common nano and mid-size reef choice.","mk":"Bubble Magus","y":"","s":CURVE,
    "v":[{"n":"Curve 5","mk":"Bubble Magus","y":"","d":"Rock SP1000 needle-wheel pump, 9 W"},{"n":"Curve 7","mk":"Bubble Magus","y":"","d":"Rock SP2000 pump, 18 W"},{"n":"Curve 5 Elite","mk":"Bubble Magus","y":"","d":"With Sicce SK-200 pump"}],"dt":"size · pump"},
   {"n":"Nyos Quantum","a":"","d":"Premium internal skimmer range.","mk":"Nyos","y":"","s":RS,
    "v":[{"n":"Quantum 120","mk":"Nyos","y":"","d":""},{"n":"Quantum 160","mk":"Nyos","y":"","d":""},{"n":"Quantum 220","mk":"Nyos","y":"","d":""}],"dt":"size"},
   {"n":"Reef Octopus Classic","a":"","d":"Wide skimmer range in space-saver, internal and hang-on formats.","mk":"Reef Octopus","y":"","s":RS,
    "v":[{"n":"Classic 110SS","mk":"Reef Octopus","y":"","d":"Space saver"},{"n":"Classic 150SS","mk":"Reef Octopus","y":"","d":"Space saver"},{"n":"Classic 110INT","mk":"Reef Octopus","y":"","d":"Internal"},{"n":"Classic 1000 HOB","mk":"Reef Octopus","y":"","d":"Hang-on-back"},{"n":"Classic BH2000 HOB","mk":"Reef Octopus","y":"","d":"Hang-on-back"}],"dt":"size · format"},
   {"n":"Tunze Comline and DOC skimmers","a":"","d":"Compact internal skimmers for nano and small reefs.","mk":"Tunze","y":"","s":RS,
    "v":[{"n":"Comline 9001","mk":"Tunze","y":"","d":"Nano skimmer"},{"n":"Comline 9001 DC","mk":"Tunze","y":"","d":"DC version"},{"n":"DOC Skimmer 9004 DC","mk":"Tunze","y":"","d":"With controller"}],"dt":"size · AC or DC"}],
  "m":[["Reefer Skimmer RSK-300","Red Sea"],["Reefer Skimmer RSK-600","Red Sea"],["K1 Nano Protein Skimmer","IceCap"],["HOB 1.5 Hang-On-Back Protein Skimmer","AquaMaxx"]]},
 {"n":"Wavemaker","a":"powerhead · flow pump · stream pump","d":"Submersible or magnet-coupled pump that creates variable water movement in a reef tank.",
  "t":["propeller pump","external magnetic drive (dry-side motor)","cross-flow (gyre)","closed loop","wave timer controller","Wi-Fi control"],
  "s":WM,
  "x":[
   {"n":"EcoTech Marine VorTech","a":"VorTech · MP pump","d":"Propeller pump whose motor sits outside the glass and drives the wet side magnetically; a reference reef flow pump.","mk":"EcoTech Marine","y":"2005","s":VT,
    "v":[{"n":"VorTech MP40","mk":"EcoTech Marine","y":"2005","d":"First 50 handmade units sold in a beta programme"},{"n":"VorTech MP10QD","mk":"EcoTech Marine","y":"","d":"QuietDrive model for 90–380 L tanks, Wi-Fi control"}],
    "dt":"size · controller generation (EcoSmart) · QuietDrive"},
   {"n":"Maxspect Gyre","a":"Gyre generator","d":"Cross-flow pump with a horizontal paddle cylinder instead of a propeller, sold as the first gyre generator.","mk":"Maxspect","y":"c. 2014","s":PFK,
    "v":[{"n":"Gyre XF150","mk":"Maxspect","y":"","d":"50 W, with controller"},{"n":"Gyre XF130","mk":"Maxspect","y":"","d":"Smaller model"},{"n":"Gyre XF170","mk":"Maxspect","y":"","d":"Larger model, announced for early 2015"},{"n":"Gyre XF330","mk":"Maxspect","y":"","d":"7000 lph, 200–400 L tanks"}],
    "dt":"size · controller modes (surge, alternating)"},
   {"n":"Tunze Stream","a":"","d":"Propeller-style wave pump, described as the reference standard of its type.","mk":"Tunze","y":"","s":WM,
    "v":[{"n":"6055 Stream","mk":"Tunze","y":"","d":"Controllable, 4500–8000 lph"}],"dt":"size · controllable or fixed"}]},
 {"n":"Reef salt mix","a":"marine salt · sea salt mix","d":"Synthetic sea-salt blend mixed with purified water to make reef tank water.",
  "t":["natural seawater levels","elevated alkalinity and calcium","bucket or bag size"],
  "s":SALT,
  "m":[["Coral Pro","Red Sea"],["Pro Reef","Tropic Marin"],["Reef Salt","Aquaforest"]]},
 {"n":"Dosing pump","a":"doser · peristaltic doser","d":"Programmable peristaltic pump that adds measured doses of reef supplements on a schedule.",
  "t":["single-head","multi-head","master and slave units","app or controller programmed","stepper motor"],
  "s":RD,
  "m":[["ReefDose 2","Red Sea"],["ReefDose 4","Red Sea"],["Profilux doser","GHL"],["Doser 2","GHL"],["Libra","Vertex Aquaristik"],["Kore 7th","PacificSun"],["Reefdoser Evo 4","Aqua Medic"],["IV Dosers","Eshopps"],["Vida Dosing Computer","ARKA"]]},
 {"n":"Calcium reactor","a":"","d":"CO2-fed chamber of aragonite media that dissolves calcium and alkalinity into a reef tank's water.",
  "t":["single chamber","secondary (buffer) chamber","pH-controlled CO2"],
  "s":CR,
  "m":[["CR-140","Reef Octopus"],["PF 501","Deltec"],["612","GEO"]]},
 {"n":"Auto top-off system","a":"ATO","d":"Sensor and pump or valve that replaces evaporated water automatically to keep salinity steady.",
  "t":["optical sensor","float switch","conductivity sensor","dual sensor","solenoid valve"],
  "s":ATO,
  "m":[["Osmolator 3155","Tunze"],["Osmolator Nano 3152","Tunze"],["HydroFill Titanium","Innovative Marine"],["Duetto","XP Aqua"],["SMART AWC Auto Water Changer and ATO","AutoAqua"]]}]
brands=[
 {"n":"EcoTech Marine","c":"United States","f":"c. 2003","seg":"Reef equipment","d":"Reef-equipment maker whose early product was a magnetically stirred kalkwasser stirrer, followed by the VorTech pump.","lines":["VorTech"],"eras":[],"sig":["EcoTech Marine VorTech"],"sc":["reef"],"rel":[],"s":VT},
 {"n":"Maxspect","c":"","f":"","seg":"Reef equipment","d":"Maker of the Gyre cross-flow pump.","lines":["Gyre"],"eras":[],"sig":["Maxspect Gyre"],"sc":["reef"],"rel":[],"s":PFK},
 {"n":"Tunze","c":"Germany","f":"","seg":"Aquarium pumps and reef equipment","d":"German maker of wave pumps, skimmers and Osmolator top-off systems.","lines":["Stream","Comline","Osmolator"],"eras":[],"sig":["Tunze Stream"],"sc":["reef"],"rel":[],"s":"knowledge"},
 {"n":"Red Sea","c":"Israel","f":"","seg":"Reef systems and supplies","d":"Israeli maker of reef aquariums, salt, skimmers and dosers.","lines":["Coral Pro","Reefer","ReefDose"],"eras":[],"sig":[],"sc":["reef"],"rel":[],"s":"knowledge"},
 {"n":"Bubble Magus","c":"","f":"","seg":"Reef equipment","d":"Maker of Curve cone skimmers and dosers.","lines":["Curve"],"eras":[],"sig":["Bubble Magus Curve"],"sc":["reef"],"rel":[],"s":CURVE},
 {"n":"Nyos","c":"","f":"","seg":"Reef equipment","d":"Maker of Quantum skimmers.","lines":["Quantum"],"eras":[],"sig":["Nyos Quantum"],"sc":["reef"],"rel":[],"s":RS},
 {"n":"Reef Octopus","c":"","f":"","seg":"Reef equipment","d":"Maker of skimmers and calcium reactors in many sizes.","lines":["Classic","CR"],"eras":[],"sig":["Reef Octopus Classic"],"sc":["reef"],"rel":[],"s":RS},
 {"n":"Beckett Corporation","c":"United States","f":"","seg":"Pumps and nozzles","d":"US company that developed the patented foam nozzle used in Beckett skimmers.","lines":[],"eras":[],"sig":["Beckett skimmer"],"sc":[],"rel":[],"s":SK},
 {"n":"Korallen-Zucht","c":"","f":"","seg":"Reef equipment","d":"Reef company that introduced the Revolution cone skimmer line around 2007.","lines":["Revolution"],"eras":[],"sig":["Cone skimmer"],"sc":["reef"],"rel":[],"s":SK}]
notes=("All six kinds are new (no old data). Corals, shrimp, snails and fish are animals and belong to the breeds/species register, so only equipment is here. "
 "Left out: Kamoer dosers (no model names on retrieved pages), Neptune ATK and Hydros ATO, Tank Vitals (not on fetched pages), Korallin reactors, refugium and kalkwasser reactors (mentioned only in context). "
 "Founding years and countries left blank where not on a retrieved page or reliably known.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/B10/shelves/03_03.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
