import json, os
def w(code, job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/{code}/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a1,"mk":b,"y":c,"d":e} for a1,b,c,e in v],"dt":dt}
K="knowledge"
MW="https://mtnweekly.com/reviews/best-avalanche-beacons/"
kinds=[
 {"n":"Cross-country ski","a":"Nordic ski · XC ski","d":"Long, narrow ski made for Nordic touring or racing with a free-heel binding.",
  "t":["classic (waxable)","classic (skin or fishscale grip)","skate","combi","backcountry / touring (metal edge)","race","recreational"],
  "s":"https://rei.com/c/cross-country-touring-skis",
  "x":[
   X("Speedmax","Fischer's top race ski line, with Air Core HM Carbon core and waxable gliding sidewall.","Fischer","",
     "https://www.skiessentials.com/2021-nordic-ski-test/skis/2021-fischer-speedmax-skate",
     [("Speedmax Skate","Fischer","2021","race skate"),("Speedmax 3D","Fischer","2021","Editor's Choice, skate"),("Twin Skin Speedmax","Fischer","2021","Editor's Choice, classic skin")],
     "skate or classic · flex · lengths 176–191 cm")],
  "m":[["Adventure 62 Crown","Fischer"],["Twin Skin Power EF Medium","Fischer"],["Voyager EF","Fischer"],["Fjelltech M50 Skin","Madshus"],["BC 65 Positrack","Rossignol"],
       ["Evo XC 60 R-Skin","Rossignol"],["Escape 51 Grip","Salomon"],["Outpath 60 Grip","Salomon"],["RC8 eSKIN","Salomon"],["RS10","Salomon"]],
  "r":[["Adventure","Fischer"],["Escape","Salomon"],["Evo","Rossignol"]]},
 {"n":"Cross-country ski boot","a":"Nordic boot","d":"Light boot with a Nordic binding interface made for cross-country skiing.",
  "t":["classic","skate","combi","backcountry","NNN / Prolink / Turnamic sole","SNS sole"],"s":"https://www.salomon.com/en-us/shop/sports/alpine-skiing.html",
  "m":[["X10","Rossignol"],["X-IUM W.C. Skate","Rossignol"],["RS8","Salomon"],["Vitane","Salomon"],["Pro Combi Prolink","Salomon"],["ProC3","Atomic"],["Carbonlite Skate","Fischer"]]},
 {"n":"Touring ski","a":"backcountry ski · ski-touring ski","d":"Light ski made for climbing with skins and then skiing down, used with a touring binding and boot.",
  "t":["ski mountaineering (light)","all-round touring","freeride touring","powder"],"s":"https://www.rei.com/c/backcountry-skis",
  "m":[["Zero G 105","Blizzard"],["Zero G 96","Blizzard"],["Backland 95","Atomic"],["Backland 109","Atomic"],["Crux 93 Pro","Head"],["Wayback 106","K2"],
       ["Escaper 97 Nano","Rossignol"],["HyperDrifter","Voile"],["Navis Freebird","Black Crows"],["Camox Freebird","Black Crows"],["Impulse 98 Ti","Black Diamond"],
       ["MTN 96 Carbon","Salomon"],["Capo","La Sportiva"],["Transalp 105 CTI","Fischer"]],
  "r":[["MTN","Salomon"]]},
 {"n":"Climbing skin","a":"skins","d":"Strip of mohair or nylon plush fixed to a ski or splitboard base for climbing.",
  "t":["mohair","nylon","mohair/nylon mix","glue or adhesive-free","cut-to-fit or pre-cut"],"s":"https://www.salomon.com/en-us/shop/sports/alpine-skiing.html",
  "m":[["Climb Pro S-Glide","Pomoca"],["Climb Pro Mohair","Pomoca"],["Free Pro Climb","Pomoca"],["Alpinist+ Universal","G3"],["GlideLite Mix STS","Black Diamond"],["Ascension","Black Diamond"]]},
 {"n":"Avalanche transceiver","a":"avalanche beacon · transceiver","d":"Body-worn radio on 457 kHz that transmits and searches to locate people buried in avalanches.",
  "t":["single, double or triple antenna","digital or analogue","Bluetooth app","voice guidance"],"s":MW,
  "x":[
   X("Barryvox","Swiss transceiver line from the army-commissioned VS-68, whose 457 kHz became the common frequency.","Mammut","1968",
     "https://www.mammut.com/us/en/stories-guides/story-barryvox",
     [("VS-68","","1974","consumer launch"),("Barryvox S","Mammut","",""),("Barryvox S2","Mammut","","")],"antennas · functions"),
   X("Tracker","BCA's simple, fast three-antenna beacon line.","BCA","",MW,[("Tracker 3+","BCA","",""),("Tracker 4","BCA","","")],"")],
  "m":[["Diract Voice","Ortovox"],["Recon X","Black Diamond"],["Guide BT","Black Diamond"],["Pro BT","Pieps"],["Powder BT","Pieps"]]},
 {"n":"Avalanche probe","a":"","d":"Collapsible rod assembled by cord to pinpoint a buried person in avalanche debris.",
  "t":["aluminium","carbon","length 240–330 cm","quick-lock tension"],"s":"https://www.evo.com/blogs/reviews/best-avalanche-shovels",
  "m":[["Quickdraw Pro 280","Black Diamond"],["Stealth 240","BCA"],["Stealth 330","BCA"],["Alu 240","Ortovox"]]},
 {"n":"Avalanche shovel","a":"snow shovel (avalanche)","d":"Collapsible metal shovel carried for avalanche rescue digging.",
  "t":["aluminium blade","telescoping shaft","D-grip or T-grip","hoe mode"],"s":"https://www.evo.com/blogs/reviews/best-avalanche-shovels",
  "m":[["Dozer 1T","BCA"],["Dozer 2H","BCA"],["Transfer LT","Black Diamond"],["Deploy","Black Diamond"],["PRO Alu III","Ortovox"],["Alugator Light","Mammut"]]},
 {"n":"Avalanche airbag pack","a":"airbag backpack · avalanche airbag","d":"Backpack with an airbag that inflates on demand to keep the wearer near the surface of an avalanche.",
  "t":["compressed-gas canister","battery fan","supercapacitor fan","removable system","vest"],"s":"https://www.switchbacktravel.com/best-avalanche-airbag-packs",
  "m":[["JetForce Pro 25L","Black Diamond"],["Pro 35 Removable Airbag 3.0","Mammut"],["Soelden Pro 32","Osprey"],["Float 22 2.0","BCA"],["Avabag Litric Tour 36 S","Ortovox"],
       ["Patrol E1 30","Scott"],["Float MtnPro Vest 2.0","BCA"]]},
]
brands=[
 {"n":"Fischer","c":"Austria","seg":"Professional & flagship","kf":"Nordic skis","d":"Austrian ski maker strong in cross-country racing.","sig":["Speedmax"],"s":K},
 {"n":"Mammut","c":"Switzerland","seg":"Premium","kf":"mountain gear, avalanche safety","d":"Swiss mountain-sports brand; maker of Barryvox transceivers.","sig":["Barryvox"],"s":"https://www.mammut.com/us/en/stories-guides/story-barryvox"},
 {"n":"BCA","c":"United States","seg":"Specialist","kf":"avalanche safety","d":"Backcountry Access, American avalanche-safety maker.","sig":["Tracker"],"s":MW},
]
notes=("All 4 old kinds kept; 4 new avalanche kinds sourced to retrieved test pages. Cross-country ski: 17 models cut to 10 + Speedmax archetype "
 "(dropped Fibre Crown EF, Evo XT 55 Positrack, Escape Snow 47 eSKIN, Outside 100 Grip, RC7 eSKIN, RS 8, RS7 as range duplicates). "
 "Touring ski: dropped Impulse 104 Ti, Tempo, MTN 86/91 Carbon, S/Lab QST Echo (ranges cover); added OutdoorGearLab award winners. "
 "Not done: Madshus/Atomic Redster XC lines, Alpina boots, Dynafit/Movement skis, Coll-Tex skins, ABS packs - not on a retrieved page. ")
w('E2','11_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":notes})
