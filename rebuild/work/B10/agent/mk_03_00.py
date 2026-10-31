import json, os
PS="https://www.petsathome.com/category/fish"
def X(n,d,mk,y,s,v=(),dt="",a=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
CG="https://www.aquasabi.de/ADA-Cube-Garden-60-P-60-30-36-cm_1"
JW="https://www.juwel-aquarium.de/en"; JH="https://juwel-aquarium.de/en/company/history"
aq={"n":"Aquarium","a":"tank · fish tank","d":"A glass or acrylic tank in which fish, plants or corals are kept.",
 "t":["rimless","framed","all-in-one","nano","reef-ready (drilled, with overflow)","bowfront","cube","corner","kreisel","glass","low-iron glass","acrylic"],
 "s":PS,"x":[
 X("ADA Cube Garden","Rimless-look tank of clear white glass with no glued-in struts, the reference tank of the Nature Aquarium style.","ADA","",CG,
   [("Cube Garden 30-C","ADA","","30 × 30 × 30 cm, 25 l"),("Cube Garden 45-P","ADA","","45 × 27 × 30 cm, 34 l"),("Cube Garden 60-P","ADA","","60 × 30 × 36 cm, 60 l, 6 mm glass"),("Cube Garden 90-P","ADA","","90 × 45 × 45 cm, 166 l"),("Cube Garden 120-P","ADA","","120 × 50 × 50 cm, 273 l"),("Cube Garden Mini M","ADA","","36 × 22 × 26 cm, 19 l")],
   "15 cm to 180 cm · glass 4–15 mm · -C cube, -P standard, -F flat, -H tall"),
 X("UNS classic rimless","Low-iron rimless tank with 45° mitred edges and clear silicone, sold bare for aquascaping.","Ultum Nature Systems","","https://www.bulkreefsupply.com/brands/ultum-nature-systems/classic-rimless-aquariums.html",
   [("UNS 30C","Ultum Nature Systems","","7 gal cube"),("UNS 45U","Ultum Nature Systems","","9 gal"),("UNS 60U","Ultum Nature Systems","","20 gal"),("UNS 90L","Ultum Nature Systems","","21 gal low")],
   "3N to 90L · 91% low-iron glass · non-tempered"),
 X("Juwel Rio","Framed complete aquarium with integrated lid lighting and filter, sold with a matching SBX cabinet.","JUWEL Aquarium","",JW,
   [("Rio 125 LED","JUWEL Aquarium","","125 l"),("Rio 180 LED","JUWEL Aquarium","","180 l"),("Rio 240 LED","JUWEL Aquarium","","240 l"),("Rio 350 LED","JUWEL Aquarium","","350 l"),("Rio 450 LED","JUWEL Aquarium","","450 l")],
   "125–450 l · white, black, grey, light and dark wood finishes"),
 X("Juwel Vision","Complete aquarium with a curved front pane, the first such tank made in Germany.","JUWEL Aquarium","1999",JH,
   [("Vision 180 LED","JUWEL Aquarium","","180 l"),("Vision 260 LED","JUWEL Aquarium","","260 l"),("Vision 450 LED","JUWEL Aquarium","","450 l")],"bowfront · 180–450 l"),
 X("Juwel Lido","Tall complete aquarium on a smaller footprint.","JUWEL Aquarium","",JW,
   [("Lido 120 LED","JUWEL Aquarium","","120 l"),("Lido 200 LED","JUWEL Aquarium","","200 l")],"120–200 l"),
 X("Fluval Flex","All-in-one kit with a curved front, honeycomb trim hiding the waterline and rear filter chambers.","Fluval","","https://www.bulkreefsupply.com/fluval-flex-15-gallon-aquarium-kit-fluval.html",
   [("Fluval Flex 15 gal","Fluval","","16 × 15 × 15 in, 132 GPH pump, RGB LED"),("Fluval Flex 2.0","Fluval","","")],"all-in-one · black or white"),
 X("Red Sea Reefer","Rimless reef-ready aquarium on a cabinet with overflow and sump plumbing.","Red Sea","2014","https://reefbuilders.com/tag/reefer",
   [("Reefer G2+","Red Sea","2023","ReefATO+ auto top-off as standard; peninsula models added"),("Reefer 200 G3+","Red Sea","","Eurobraced, ultra-clear glass"),("Reefer 425 G3+","Red Sea","",""),("Reefer 750 G3+","Red Sea","","")],
   "nano to XL · peninsula · deluxe with lights"),
 X("Waterbox Clear","Rimless ultra-clear glass tank for freshwater and custom reef builds, sold with or without stand.","Waterbox","2019","https://reefbuilders.com/2019/02/15/waterboxs-new-rimless-aquariums-for-freshwater-custom-reefs",
   [("Clear Mini","Waterbox","2019","6 gal"),("Clear Pro","Waterbox","2019","six-foot, 167 gal")],"6–167 gal · predrilled reef-ready line alongside"),
 ],
 "m":[["Dennerle Scaper's Tank","Dennerle"],["Dennerle Nano Cube","Dennerle"],["Fluval Spec","Fluval"],["Fluval Edge 2.0","Fluval"],["Eheim incpiria","EHEIM"],["Eheim proxima","EHEIM"],["Eheim vivaLineLED","EHEIM"],["Juwel Primo","JUWEL Aquarium"],["Juwel Trigon","JUWEL Aquarium"],["Juwel Vio","JUWEL Aquarium"],["Coralife LED Bio-Cube Aquarium Kit","Coralife"],["Innovative Marine Nuvo Abyss Panorama Glass","Innovative Marine"],["Red Sea Peninsula System","Red Sea"],["Aquatop Recife Eco All in One","Aquatop"],["Aquamaxx Long Low-Iron Rimless Aquarium","Aquamaxx"],["Oase biOrb","Oase"],["Aqueon Rectangle LED Aquarium Kit","Aqueon"],["Cobalt Aquatics C-Vue Aquarium Kit","Cobalt Aquatics"],["GEX Glass Aqua PERCO B-Dark Wood All-in-One Set","GEX"]]}
AD="https://www.adana.co.jp/en/solar_rgb/history.html"
li={"n":"Aquarium light","a":"aquarium LED · reef light · planted-tank light","d":"A lamp or light unit made for an aquarium.",
 "t":["hood or cover light","LED bar","pendant","puck or spot","metal halide","freshwater","planted","reef"],"s":PS,"x":[
 X("ADA Solar I","Metal halide pendant for open-top tanks, letting plants grow out of the water.","ADA","2002",AD,
   [("Solar II","ADA","","derivative"),("Grand Solar I","ADA","","derivative"),("Grand Solar II","ADA","","derivative"),("Grand Solar 250","ADA","","derivative")],"metal halide 150 W (NAMH-150W) · pendant on stand"),
 X("ADA Solar RGB","Fanless red-green-blue LED pendant that replaced the Solar I metal halide.","ADA","2016",AD,[],"up to 130 W · fits Solar I/II stands"),
 X("Chihiros WRGB II","App-programmable RGB LED bar for planted tanks, with red, green and blue set separately.","Chihiros","","https://www.aquasabi.de/Chihiros-LED-System-Series-WRGB-II",
   [("WRGB II 30","Chihiros","","33 W"),("WRGB II 60","Chihiros","","67 W"),("WRGB II 90","Chihiros","","100 W"),("WRGB II 120","Chihiros","","130 W"),("WRGB II Pro","Chihiros","",""),("WRGB II Slim","Chihiros","","")],"30–140 cm tanks · My Chihiros app"),
 X("Twinstar S series","Full-spectrum LED bar for high-light planted tanks, on rim legs or hung as a pendant.","Twinstar","","https://buceplant.com/products/twinstar-led-sa-series-aquarium-light-fixture",
   [("Twinstar 600S IV","Twinstar","","59 W, 3620 lm"),("Twinstar 1200S IV","Twinstar","","110 W, 6750 lm"),("Twinstar SA","Twinstar","","adjustable legs"),("Twinstar SP","Twinstar","","pendant")],"200–1200 mm · built-in dimmer"),
 X("Kessil A360","Compact dense-matrix LED spot giving a metal-halide-like shimmer.","Kessil","","https://bulkreefsupply.com/a360x-controllable-led-aquarium-light-tuna-blue-kessil.html",
   [("A360WE","Kessil","",""),("A360X Tuna Blue","Kessil","","90 W"),("A360XE","Kessil","","successor to A360X")],"Tuna Blue, Tuna Sun spectra · gooseneck or arm mount"),
 X("AI Hydra","App-controlled reef LED puck with a moonlight channel.","AquaIllumination","","https://www.bulkreefsupply.com/content/post/a-buyers-guide-to-aquaillumination-reef-tank-lighting-and-powerheads",
   [("Hydra 32 HD","AquaIllumination","","32 LEDs, 90 W"),("Hydra 64 HD","AquaIllumination","","64 LEDs, 135 W, four pucks"),("Prime 16HD","AquaIllumination","","smaller sibling, 55 W")],"reef or freshwater spectrum · black or white"),
 X("EcoTech Radion","Multi-channel reef LED fixture, set up by app, sold in generations.","EcoTech Marine","","https://bulkreefsupply.com/radion-xr30-g6-pro-led-light-fixture-ecotech-marine.html",
   [("Radion XR30 G6 Pro","EcoTech Marine","","100 LEDs, 10 channels"),("Radion XR30 G6 Blue","EcoTech Marine","","blue-weighted"),("Radion XR15 G6 Pro","EcoTech Marine","","smaller")],"Pro or Blue · Mobius app"),
 ],
 "m":[["Fluval Plant 3.0","Fluval"],["Fluval Aquasky 2.0","Fluval"],["Fluval Reef 4.0","Fluval"],["Juwel HeliaLux Spectrum","JUWEL Aquarium"],["Eheim powerLED+","EHEIM"],["JBL LED Solar Natur","JBL"],["Oase HighLine Classic LED","Oase"],["Tetra LightWave LED","Tetra"],["Aquael Moonlight LED","Aquael"],["Blade Smart LED Strip","AquaIllumination"]]}
he={"n":"Aquarium heater","a":"heater-thermostat","d":"A heater with a thermostat that keeps aquarium water warmer than the room.",
 "t":["submersible glass","titanium","preset","adjustable","electronic with display","in-line"],"s":PS,"x":[
 X("Jäger regulator heater","Adjustable submersible heater-thermostat devised by engineer Eugen Jäger; EHEIM bought the firm in 2002.","EHEIM","","https://eheim.com/ca_CA/company/news/?p=1",
   [("Eheim thermocontrol","EHEIM","","formerly sold as Eheim Jäger"),("Eheim thermocontrol+ e","EHEIM","","electronic")],"25–300 W · glass tube with dial"),
 X("Fluval E","Electronic heater with dual sensors and a temperature display that changes colour outside the set point.","Fluval","","https://www.pondkeeper.co.uk/fluval-e-300w-advanced-electronic-heater/",
   [("Fluval E100","Fluval","","100 W"),("Fluval E200","Fluval","","200 W"),("Fluval E300","Fluval","","300 W, up to 375 l")],"integrated fish guard · °C or °F"),
 ],
 "m":[["Fluval M Series Heater","Fluval"],["Juwel AquaHeat Control","JUWEL Aquarium"],["Aquael UltraHeater Day and Night","Aquael"],["JBL ProTemp III","JBL"],["Dennerle Heater Constant","Dennerle"],["Sicce SCUBA Preset Heater","Sicce"],["Tetra HT Adjustable Heater","Tetra"],["Oase HeatUp","Oase"],["Newa Therm","Newa"]]}
ca={"n":"Aquarium cabinet and stand","a":"aquarium stand · tank cabinet","d":"A cabinet or frame built to carry the full weight of a filled aquarium, often hiding equipment.",
 "t":["matching cabinet","wooden or plywood cabinet","metal stand","glass cabinet"],"s":"https://www.aquasabi.de/ADA-Aquarium-Combination-Cube-Cabinet-Clear-Cube-Garden","x":[
 X("ADA Cube Cabinet Clear","Four-compartment cabinet of white glass sized to a Cube Garden tank.","ADA","","https://www.aquasabi.de/ADA-Aquarium-Combination-Cube-Cabinet-Clear-Cube-Garden",
   [("Cube Cabinet Clear 30-C","ADA","","70 kg load"),("Cube Cabinet Clear 60-P","ADA","","100 kg load")],"700 mm high"),
 X("Juwel SBX cabinet","Cabinet sized and finished to match each Juwel complete aquarium, GS-certified.","JUWEL Aquarium","","https://mcmerwe.co.za/shop/juwel-rio-cabinet/",
   [("SBX Rio","JUWEL Aquarium","","sizes 125–450"),("SBX Lido","JUWEL Aquarium","",""),("SBX Vision","JUWEL Aquarium","","")],"white, black, grey, light and dark wood"),
 ]}
CH="https://www.bulkreefsupply.com/aquarium-heaters-chillers/aquarium-chillers.html"
ch={"n":"Aquarium chiller","a":"aquarium cooler","d":"A refrigeration unit that cools aquarium water when the room is warmer than the tank should be.",
 "t":["compressor chiller","chiller with heater","drop-in","thermoelectric","cooling fan"],"s":CH,"x":[
 X("TECO TK","Italian compressor chiller with titanium heat exchanger, many variants also heating.","TECO","","https://gensou.sg/teco-tk-chiller-review/",
   [("TECO TK500","TECO","","1/6 HP"),("TECO TK1000","TECO","","1/4 HP"),("TECO TK2000","TECO","","1/3 HP"),("TECO TK6000","TECO","","largest")],"0.1° setpoint · H versions with heater"),
 X("JBJ Arctica","Compressor chiller line sized by horsepower, from nano to 1/3 HP.","JBJ","",CH,
   [("Arctica 1/10 HP (DBA-075)","JBJ","",""),("Arctica 1/5 HP (DBA-150)","JBJ","",""),("Arctica 1/3 HP (DBM-250)","JBJ","",""),("Arctica Nano E-Chiller","JBJ","","")],""),
 ],
 "m":[["TECO DI-500 Drop-In Chiller","TECO"],["IceProbe Thermoelectric Aquarium Chiller","Nova Tec"]]}
K="knowledge"
def B(n,c,f,seg,d,s,sig=(),lines=(),rel=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 B("ADA","Japan","1982","Aquascaping equipment","Aqua Design Amano, founded by Takashi Amano, makers of Nature Aquarium tanks, lights and supplies.","https://en.wikipedia.org/wiki/Takashi_Amano",["ADA Cube Garden","ADA Solar I","ADA Solar RGB"],["Cube Garden","Solar","Cube Cabinet"]),
 B("JUWEL Aquarium","Germany","1970","Complete aquariums","Rotenburg maker of framed complete aquariums with integrated lighting, filter and heater and matching cabinets.",JH,["Juwel Rio","Juwel Vision","Juwel Lido"],["Rio","Lido","Vision","Trigon","Primo","Vio"]),
 B("EHEIM","Germany","1949","Aquarium filters and heaters","German aquarium technology maker founded by Gunther Eheim; owns the Jäger heater line since 2002.","https://eheim.com/ca_CA/company/news/?p=1",["Jäger regulator heater"]),
 B("Chihiros","China","2014","Aquarium LED lighting","Aquatic lighting brand for planted tanks.","https://www.aquasabi.de/Chihiros-LED-System-Series-WRGB-II",["Chihiros WRGB II"]),
 B("TECO","Italy","","Aquarium chillers","Italian maker of compressor aquarium chillers.","https://gensou.sg/teco-tk-chiller-review/",["TECO TK"]),
 B("Ultum Nature Systems","USA","","Aquascaping tanks and equipment","Brand of low-iron rimless aquascaping tanks.",K,["UNS classic rimless"],[],["ADA"]),
 B("Fluval","Canada","","Aquarium equipment","Aquarium brand of Rolf C. Hagen covering tanks, filters, lights and heaters.",K,["Fluval Flex","Fluval E"]),
 B("Red Sea","Israel","","Reef aquariums and supplements","Marine aquarium company making reef-ready systems, lights and salt.",K,["Red Sea Reefer"]),
 B("Waterbox","USA","","Rimless and reef aquariums","Maker of rimless glass aquariums and stands.",K,["Waterbox Clear"]),
 B("Twinstar","South Korea","","Planted-tank LED lighting","Korean maker of LED lights for planted aquariums.",K,["Twinstar S series"]),
 B("Kessil","USA","","Aquarium LED lighting","Californian maker of dense-matrix LED spot lights.",K,["Kessil A360"]),
 B("AquaIllumination","USA","","Reef LED lighting","Maker of app-controlled reef LED lights.",K,["AI Hydra"]),
 B("EcoTech Marine","USA","","Reef equipment","Pennsylvania maker of reef lighting and pumps.",K,["EcoTech Radion"]),
 B("JBJ","USA","","Aquarium equipment","Aquarium equipment maker known for chillers and nano tanks.",K,["JBJ Arctica"]),
]
out={"kinds":[aq,li,he,ca,ch],"brands":brands,"traditions":[],
 "notes":"All three old kinds kept; Aquarium cabinet and stand and Aquarium chiller added. Flat model lists trimmed to market-covering brands (≤20); archetype models moved into versions. Left out: Fluval official pages (403, so Fluval E sourced from a retailer); ADA Solar RGB II (only in search snippets); Cube Garden launch year (not on retrieved pages); Waterbox Reef/Marine X/AIO lines and Red Sea Reefer G2 model sizes (snippets only); Hailea chillers (snippets only); Waterbox/Red Sea stands (no retrieved page). Trade/commercial chillers (JBJ DA series) dropped under scope rule. Brand founding years only where a retrieved page gave them."}
p="/home/user/Possession-Taxonomy/rebuild/work/B10/shelves/03_00.json"; os.makedirs(os.path.dirname(p),exist_ok=True)
json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
