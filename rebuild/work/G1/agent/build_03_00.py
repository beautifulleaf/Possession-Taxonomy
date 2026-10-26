import json, os
W='https://en.wikipedia.org/wiki/'
SP=W+'Specialized_Bicycle_Components'; TR=W+'Trek_Bicycle_Corporation'; CO=W+'Colnago'; PI=W+'Pinarello'
CE=W+'Cerv%C3%A9lo'; BI=W+'Bianchi_(company)'; CI=W+'Cinelli'; SU=W+'Surly_Bikes'
def V(n,mk,y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Road bike","a":"racing bicycle · road racer · racer","d":"Drop-bar bicycle made for speed on paved roads.",
 "t":["race","endurance / sportive","aero","lightweight climbing","classic lugged steel","flat-bar road"],
 "s":W+"Road_bicycle",
 "x":[
  {"n":"Bianchi celeste racer","a":"Bianchi Celeste","d":"Bianchi's racing bicycles in celeste, the brand's turquoise, from Coppi's steel racers to modern carbon.","mk":"Bianchi","y":"1885","s":BI,
   "v":[V("Fausto Coppi steel racer","Bianchi","1950–1952","bike used by Coppi"),V("Campione del Mondo","Bianchi","1953","after Coppi's world championship"),
        V("Specialissima","Bianchi","","2017 range"),V("Infinito","Bianchi","","2017 range"),V("Oltre XR1–XR4","Bianchi","","2017 range")],
   "dt":"frame material · celeste shade (bluer or greener by era) · groupset"},
  {"n":"Colnago C-series","a":"C40 · C64 · C68","d":"Colnago's Italian-made carbon tube-and-lug flagship road frames, begun with the monocoque C35.","mk":"Colnago","y":"1989","s":CO,
   "v":[V("C35","Colnago","1989","full carbon monocoque"),V("C40","Colnago","1994","carbon; first with Precisa steel fork"),V("C50","Colnago","2004","1.125 in fork"),
        V("C59","Colnago","2011","profiled tubes"),V("C60","Colnago","2014","star-shaped tubes through the lugs"),V("C64","Colnago","2018",""),V("C68","Colnago","2022","made in Italy")],
   "dt":"size · paint scheme · rim or disc brake"},
  {"n":"Colnago Master","a":"","d":"Colnago's top steel road frame with Precisa steel fork.","mk":"Colnago","y":"1983","s":CO,"v":[],"dt":"size · paint scheme"},
  {"n":"Cinelli Supercorsa","a":"Speciale Corsa · Super Corsa","d":"Cinelli's steel road racer, called the oldest bicycle model still in production.","mk":"Cinelli","y":"1947","s":CI,
   "v":[V("Speciale Corsa","Cinelli","1947","original name; renamed after a decal error")],"dt":"size · colour"},
  {"n":"Pinarello Dogma","a":"","d":"Pinarello's flagship carbon race bike, successor to the Prince.","mk":"Pinarello","y":"2010","s":PI,
   "v":[V("Prince","Pinarello","","predecessor range"),V("Dogma","Pinarello","2010",""),V("Dogma 2","Pinarello","2011",""),V("Dogma 65.1 Think2","Pinarello","2013",""),
        V("Dogma F8","Pinarello","2014",""),V("Dogma K8-S","Pinarello","2015","endurance"),V("Dogma F10","Pinarello","2017",""),V("Dogma K10","Pinarello","2017","endurance"),V("Dogma F12","Pinarello","2019","")],
   "dt":"size · rim or disc · paint"},
  {"n":"Specialized Allez","a":"","d":"Specialized's road bike line, today its aluminium race bike.","mk":"Specialized","y":"1981","s":SP,
   "v":[V("Allez","Specialized","1981","first road bike"),V("Allez Epic","Specialized","","carbon version"),V("Allez Sprint","Specialized","","aluminium race")],"dt":"frame material · groupset"},
  {"n":"Specialized Tarmac","a":"","d":"Specialized's race bike, aluminium at launch and carbon since the SL1.","mk":"Specialized","y":"2003","s":"https://en.brujulabike.com/history-of-the-specialized-tarmac-eight-generations-of-records-evolution-and-an-unbeatable-legacy/",
   "v":[V("Tarmac","Specialized","2003","aluminium"),V("Tarmac SL1","Specialized","2006","first carbon"),V("Tarmac SL5","Specialized","2015","disc brakes added"),V("Tarmac SL7","Specialized","2021","replaced the Venge aero bike")],
   "dt":"generation · S-Works or standard · groupset"},
  {"n":"Trek Madone","a":"","d":"Trek's top race bike, named after the Col de la Madone; since 2024 also its lightweight bike.","mk":"Trek","y":"2003","s":TR,
   "v":[V("Madone","Trek","2003","original"),V("Madone 8","Trek","2024","merged with the Émonda")],"dt":"generation · SLR or SL · groupset"},
  {"n":"Trek Émonda","a":"Emonda","d":"Trek's lightweight climbing race bike, merged into the Madone in 2024.","mk":"Trek","y":"2014","s":"https://www.bikeradar.com/features/opinion/oscar-huckle-bring-back-the-trek-emonda",
   "v":[V("Émonda (gen 1)","Trek","2014","690 g claimed frame"),V("Émonda (gen 2)","Trek","2017","rim and disc"),V("Émonda (gen 3)","Trek","2020","disc only, more aero")],"dt":"SLR or SL · groupset"},
  {"n":"Cervélo R-Series","a":"","d":"Cervélo's climbing road bikes.","mk":"Cervélo","y":"","s":CE,
   "v":[V("RS","Cervélo"),V("R2","Cervélo"),V("R3","Cervélo"),V("R5","Cervélo"),V("RCA","Cervélo")],"dt":"rim or disc (d suffix) · groupset"},
  {"n":"Cervélo S-Series","a":"","d":"Cervélo's aero road bikes.","mk":"Cervélo","y":"","s":CE,
   "v":[V("S1","Cervélo","","discontinued"),V("S2","Cervélo"),V("S3","Cervélo"),V("S5","Cervélo")],"dt":"rim or disc · groupset"}],
 "m":[["Domane","Trek"],["Aethos","Specialized"],["5500 (OCLV carbon)","Trek"],["Soloist","Cervélo"],["C-Series","Cervélo"],["Roadeo","Rivendell Bicycle Works"],["Vincitore","Mercian Cycles"]]},
{"n":"Gravel bike","a":"adventure bike · all-road bike","d":"Drop-bar bicycle with wide tyre clearance, made for mixed paved and unpaved roads.",
 "t":["race","adventure / bikepacking","suspension","700c","650b"],"s":W+"Gravel_bicycle",
 "x":[{"n":"Pinarello Grevil","a":"","d":"Pinarello's carbon gravel bike.","mk":"Pinarello","y":"2018","s":PI,"v":[V("Grevil","Pinarello","2018",""),V("Grevil F","Pinarello","2022","")],"dt":"size · groupset · tyre width"}],
 "m":[["Diverge","Specialized"],["Crux","Specialized"],["Checkmate","Trek"],["CheckOUT","Trek"],["Topstone","Cannondale"],["SuperX","Cannondale"],["True Grit","Lauf"],["URS","BMC"],["Terra","Orbea"],["765","Look"],["Áspero","Cervélo"]]},
{"n":"Touring bike","a":"tourer · trekking bike · expedition bike","d":"Sturdy bicycle made to carry luggage on long rides.",
 "t":["road touring","sport touring","randonneur","expedition","mixed-terrain","travel (couplers)"],"s":W+"Touring_bicycle",
 "x":[
  {"n":"Surly Long Haul Trucker","a":"LHT","d":"Steel loaded-touring bike with long chainstays and many mounts.","mk":"Surly","y":"","s":"https://surlybikes.com/bikes/legacy/long_haul_trucker",
   "v":[V("Long Haul Trucker 26in","Surly","","frame sizes 42–58 cm"),V("Long Haul Trucker 700c","Surly","","frame sizes 56–62 cm"),V("Disc Trucker","Surly","","disc-brake version")],
   "dt":"4130 chromoly · 26in or 700c · rim or disc brakes"},
  {"n":"Koga WorldTraveller","a":"Worldtraveller","d":"Dutch expedition touring bike without suspension, combining MTB and trekking parts.","mk":"Koga","y":"1999","s":"https://www.bike-magazin.de/en/bicycles/trekking-bikes/koga-worldtraveller-29-once-around-the-world/",
   "v":[V("WorldTraveller","Koga","1999","26in wheels, XT groupset, racks"),V("WorldTraveller 29","Koga","","29in wheels; Signature or series build")],"dt":"wheel size · Signature custom build · groupset"},
  {"n":"Rivendell Atlantis","a":"","d":"Rivendell's touring frame made for 26in or 700C wheels.","mk":"Rivendell Bicycle Works","y":"","s":W+"Touring_bicycle","v":[],"dt":"wheel size · frame size"}],
 "m":[["Cascadia","Co-Motion"],["Travelers Check","Surly"],["EXP","Thorn Cycles"],["Raven","Thorn Cycles"],["Roughstuff","Roberts"],["Fargo","Salsa"]]},
{"n":"Cyclocross bike","a":"cyclo-cross bike · CX bike · cross bike","d":"Drop-bar bicycle made for cyclocross racing on mixed off-road courses.",
 "t":["disc brake","cantilever brake","single-speed","1x"],"s":W+"Cyclo-cross_bicycle",
 "x":[{"n":"Surly Cross-Check","a":"Crosscheck","d":"Steel cyclocross-style all-rounder, discontinued in 2023 after 24 years.","mk":"Surly","y":"1999","s":SU,"v":[],"dt":"frame size · groupset · single or multi chainring"}],
 "m":[["TCX","Giant"],["Klatch","Co-Motion"],["Crossista F","Pinarello"],["R5-CX","Cervélo"]]},
{"n":"Track bike","a":"track bicycle · pista · keirin bike","d":"Fixed-gear bicycle without brakes made for velodrome racing.",
 "t":["sprint","endurance / pursuit","keirin (NJS)","fixed-gear street / criterium"],"s":W+"Track_bicycle",
 "x":[
  {"n":"Cinelli Laser","a":"","d":"TIG-welded track pursuit and time-trial bike that won 28 Olympic and world gold medals.","mk":"Cinelli","y":"1980","s":CI,"v":[],"dt":"size · paint"},
  {"n":"Cinelli Vigorelli","a":"","d":"Cinelli track frame named after Milan's Vigorelli velodrome, rooted in fixed-gear criterium racing.","mk":"Cinelli","y":"","s":"https://www.360cycles.ie/cinelli-vigorelli-steel-frameset.html",
   "v":[V("Vigorelli (Columbus Airplane alloy)","Cinelli","","aero seat tube, 377 mm chainstays, carbon fork")],"dt":"size · colour"},
  {"n":"Cervélo T-Series","a":"","d":"Cervélo's track bikes.","mk":"Cervélo","y":"","s":CE,"v":[V("T1","Cervélo","","discontinued"),V("T3","Cervélo"),V("T4","Cervélo"),V("T5GB","Cervélo")],"dt":"size"}],
 "m":[["Supercorsa Pista","Cinelli"],["Tutto Plus","Cinelli"],["MASH","Cinelli"],["MAAT 60.1","Pinarello"],["T20","Look"]]},
{"n":"Time-trial bike","a":"TT bike · triathlon bike","d":"Aerodynamic road bicycle with aero bars made for racing against the clock.",
 "t":["UCI-legal time trial","triathlon"],"s":W+"Time_trial_bicycle",
 "x":[
  {"n":"Cervélo P-Series","a":"P3 · P5","d":"Cervélo's time-trial and triathlon bikes.","mk":"Cervélo","y":"","s":CE,
   "v":[V("P1","Cervélo","","discontinued"),V("P2","Cervélo"),V("P3","Cervélo"),V("P3X","Cervélo"),V("P4","Cervélo","","discontinued"),V("P5-three","Cervélo","","UCI-compliant"),V("P5-six","Cervélo","","triathlon"),V("P5X","Cervélo")],
   "dt":"UCI or triathlon · groupset"},
  {"n":"Pinarello Bolide","a":"","d":"Pinarello's time-trial bike, used by Bradley Wiggins for the 2015 hour record in HR form.","mk":"Pinarello","y":"2013","s":PI,
   "v":[V("Espada","Pinarello","1994","predecessor, built for an hour record attempt"),V("Bolide","Pinarello","2013",""),V("Bolide HR","Pinarello","2015","hour record"),V("Bolide TT","Pinarello","2016","")],"dt":"size · groupset"}],
 "m":[["TTX","Trek"],["S-Works Transition","Specialized"],["Ordu","Orbea"]]}]
K='knowledge'
brands=[
 {"n":"Specialized","c":"United States","f":"1974","seg":"Mainstream performance bicycles","d":"Californian bicycle maker founded by Mike Sinyard, based in Morgan Hill.","lines":["S-Works"],"eras":[],"sig":["Specialized Allez","Specialized Tarmac"],"sc":[],"rel":["Trek"],"s":SP},
 {"n":"Trek","c":"United States","f":"1976","seg":"Mainstream performance bicycles","d":"Wisconsin bicycle maker based in Waterloo, known for OCLV carbon frames.","lines":[],"eras":[],"sig":["Trek Madone","Trek Émonda"],"sc":[],"rel":["Specialized"],"s":TR},
 {"n":"Colnago","c":"Italy","f":"1954","seg":"Italian racing marque","d":"Racing bicycle maker founded by Ernesto Colnago in Cambiago near Milan.","lines":["C-series","V-series"],"eras":[],"sig":["Colnago C-series","Colnago Master"],"sc":[],"rel":["Pinarello"],"s":CO},
 {"n":"Pinarello","c":"Italy","f":"1953","seg":"Italian racing marque","d":"Racing bicycle maker founded by Giovanni Pinarello in Treviso.","lines":["Dogma"],"eras":[],"sig":["Pinarello Dogma","Pinarello Bolide"],"sc":[],"rel":["Colnago"],"s":PI},
 {"n":"Cervélo","c":"Canada","f":"1995","seg":"Performance and aero bicycles","d":"Bicycle maker founded in Toronto by Gerard Vroomen and Phil White, now based in California.","lines":["R-Series","S-Series","P-Series","T-Series"],"eras":[],"sig":["Cervélo P-Series","Cervélo S-Series"],"sc":[],"rel":[],"s":CE},
 {"n":"Bianchi","c":"Italy","f":"1885","seg":"Italian racing marque","d":"Bicycle maker founded by Edoardo Bianchi in Milan, known for celeste paint.","lines":[],"eras":[],"sig":["Bianchi celeste racer"],"sc":[],"rel":[],"s":BI},
 {"n":"Cinelli","c":"Italy","f":"1948","seg":"Italian racing and fixed-gear marque","d":"Milan bicycle and component maker founded by racer Cino Cinelli.","lines":[],"eras":[],"sig":["Cinelli Supercorsa","Cinelli Laser","Cinelli Vigorelli"],"sc":["fixed-gear"],"rel":[],"s":CI},
 {"n":"Surly","c":"United States","f":"1998","seg":"Steel utility and touring bicycles","d":"Steel-frame bicycle brand of Quality Bicycle Products, Bloomington, Minnesota.","lines":[],"eras":[],"sig":["Surly Long Haul Trucker","Surly Cross-Check"],"sc":["touring","bikepacking"],"rel":[],"s":SU},
 {"n":"Koga","c":"Netherlands","f":"","seg":"Trekking and touring bicycles","d":"Dutch maker of trekking and expedition touring bicycles.","lines":["Signature"],"eras":[],"sig":["Koga WorldTraveller"],"sc":["touring"],"rel":[],"s":K},
 {"n":"Eddy Merckx Cycles","c":"Belgium","f":"1980","seg":"Racing bicycles","d":"Belgian road-bike brand founded by former professional cyclist Eddy Merckx.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":W+"Eddy_Merckx_Cycles"},
 {"n":"Rivendell Bicycle Works","c":"United States","f":"1994","seg":"Steel frame builder","d":"Steel-bicycle maker founded by Grant Petersen in Walnut Creek, California.","lines":[],"eras":[],"sig":["Rivendell Atlantis"],"sc":["touring"],"rel":[],"s":W+"Rivendell_Bicycle_Works"},
 {"n":"Mercian Cycles","c":"United Kingdom","f":"1946","seg":"Steel frame builder","d":"Lugged steel frame builder in Derby founded by Tom Crowther and Lou Barker.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Bob Jackson"],"s":W+"Mercian_Cycles"},
 {"n":"Bob Jackson","c":"United Kingdom","f":"","seg":"Steel frame builder","d":"English builder of hand-made steel bicycle frames.","lines":[],"eras":[],"sig":[],"sc":[],"rel":["Mercian Cycles"],"s":K}]
notes=("All six planned kinds kept. Specialized/Trek/Co-Motion skew trimmed: Co-Motion Deschutes and Tumalo dropped (Cascadia kept); Trek CheckOUT and Checkmate kept as flat models; "
 "Crux 5/Diverge 4 SKU names reduced to Crux/Diverge. Cannondale SuperX moved from Cyclocross to Gravel (maker page now calls it a gravel race bike). "
 "Left out: Eddy Merckx archetypes (no retrieved page names models; brand entry only), Bob Jackson models (no page found, Wikipedia 404; brand stub from knowledge), "
 "Tarmac SL2–SL4/SL6/SL8 and Specialized Diverge/Crux, Trek gravel archetypes (pages blocked or not naming them; kept as flat models), "
 "Vigorelli steel version (only in search snippets). No craft tradition added: no retrieved source on frame-building traditions. Randonneur is a touring type.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/G1/shelves/03_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('ok')
