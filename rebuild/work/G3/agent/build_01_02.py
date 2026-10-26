import json, os
W="https://en.wikipedia.org/wiki/"
SAUNA=W+"Sauna"; FIN=W+"Finnish_sauna"; BANYA=W+"Banya_(sauna)"; HAMMAM=W+"Turkish_bath"
IR=W+"Infrared_sauna"; STEAM=W+"Steam_shower"; HOTTUB=W+"Hot_tub"; JAC=W+"Jacuzzi"; HARVIA=W+"Harvia"
S1="https://www.spabusiness.com/wellness-products-and-services/Different-design-approach-leads-to-space-saving-S1-sauna/316864"
TYLO="https://www.mynewsdesk.com/tylo/pressreleases/from-homemade-heaters-to-leading-sauna-manufacturer-2929652"
LEG="https://www.harvia.com/en-US/sauna-heaters/sauna-wood-burning-heater/legend-wood-burning-heaters"
LEG240="https://harvia.com/en/products/WK240LD/harvia-legend-240"
CIL="https://www.harvia.com/en-US/products/HPCE66400/cilindro-pc66e-66-kw-steel"
HIVE="https://finnmarksauna.com/products/huum-hive-electric-sauna-heater"
HUUM="https://huum.eu/"; SAUNUM="https://www.saunum.com/"
KLSTEAM="https://www.klafs.com/residential/products/steam-baths-steam-shower?lgchange=1"
STEAMIST="https://www.poolspanews.com/?p=19672"
SPAHIST="https://www.poolspanews.com/?p=25409"
HS="https://hotspring.com/shop"; CAL="https://www.calderaspas.com/?p=24993"
MS="https://www.masterspas.com/about/hot-tub-history"
BW="https://www.fitshop.ch/it/bestway"
KIR="https://harviagroup.com/harvia-strengthens-its-position-in-the-sauna-and-spa-market-by-acquiring-still-water-hot-tub-manufacturer-kirami-3561"
PLUNGE="https://athletechnews.com/best-cold-plunge-tubs/"
BARREL="https://themanual.com/fitness/barrel-sauna"
VORO="https://ich.unesco.org/en/RL/smoke-sauna-tradition-in-voromaa-00951?RL=00951"
GOEMON="https://www.folko.com.au/blog/japanese-minka-xcvi-bathing-areas-4"
OFURO=W+"Ofuro"

def X(n,d,mk,y,s,v=(),a="",dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}

kinds=[
 {"n":"Sauna cabin","a":"home sauna · sauna room · outdoor sauna · sauna house","d":"Hot-air bathing room or small building with benches and a stove, heated to about 80–100 °C for sweat bathing.",
  "t":["indoor cabin","outdoor sauna house","barrel sauna","glass-front cabin","infrared cabin","hybrid (stove and infrared)","wood-stove heated","electric heated","spruce","cedar","pine"],
  "s":SAUNA,"x":[
   X("Smoke sauna","Chimneyless sauna: a stove under a pile of stones fills the room with smoke, which is vented before bathing.","","traditional; revived from the 1980s",SAUNA,
     [("Finnish savusauna","","","the first type of Finnish sauna; nearly died out, revived by enthusiasts in the 1980s"),("Võro smoke sauna","","2014","Võromaa, Estonia; tradition on UNESCO's Representative List")],
     a="savusauna",dt="log building · stone-covered stove without flue · smoke vent · raised platform"),
   X("Finnish wood-stove sauna","Sauna heated by a metal wood-burning stove (kiuas) with stones on top and a chimney; water on the stones gives löyly.","","Industrial Revolution era",FIN,
     [("Electric sauna","","1938","electric stove introduced by Metos Ltd, Vaasa; usual in apartments and public saunas")],
     dt="stove type: wood or electric · 80–110 °C · birch whisk (vihta) · lake, shower or snow for cooling"),
   X("Russian banya","Wood-heated Russian steam bath, typically with steam room, washing room and entrance room, used with a birch or oak venik.","","described in the 12th-century Primary Chronicle",BANYA,
     [("Black banya","","","smoke vents through a hole in the ceiling"),("White banya","","","stove with exhaust pipe"),("Pokhodnaya (hiking) banya","","","stone oven inside a makeshift tent near water")],
     dt="three-room plan · stove with firebox, stone chamber and water tank · venik of birch, oak or eucalyptus"),
   X("Barrel sauna","Cylindrical outdoor sauna built from curved wooden staves, resembling a wine or whisky barrel.","","modern",BARREL,
     [],dt="wood: cedar, Nordic spruce or pine · uninsulated walls · about 45 minutes to heat"),
   X("Klafs S1","Retractable home sauna that folds to 60 cm deep and extends to nearly three times that at the press of a button.","Klafs","2015",S1,
     [("S1 (three sizes)","Klafs","2015","eMove extension in about 20 seconds; stops if obstructed; retracts only after the heater cools")],
     a="retractable sauna · folding sauna",dt="three sizes · trims and front panels"),
   X("Infrared sauna cabin","Cabin heated mainly by radiant infrared emitters rather than hot air and stones.","","1891 (light bath); revived 1970s Japan",IR,
     [("Incandescent electric light bath","John Harvey Kellogg","1891","radiant heat cabinet; patented 1896, shown at the 1893 Chicago World's Fair"),("Waon therapy","","1970s","modern revival in Japan")],
     dt="far-infrared emitters · lower air temperature than a Finnish sauna"),
   X("TylöHelo Jubilee Sauna","Limited-edition sauna marking Tylö's 70th and Helo's 100th anniversaries, lined with Taika wall panels.","Tylö","2019",TYLO,
     [],dt="Taika panels · sold 1 October to 31 March only"),
  ],
  "m":[["Ventura","Harvia"]]},
 {"n":"Sauna heater","a":"sauna stove · kiuas · sauna kiuas","d":"Stove that heats a sauna and holds stones onto which water is thrown to make steam (löyly).",
  "t":["wood-burning","electric","continuous-heat","heat-storage","combi (with steam/humidity)","fired from another room","wall-mounted","floor-standing","pillar","with water heater"],
  "s":SAUNA,"x":[
   X("Heat-storage stove","Stove with a large stone mass in a sealed compartment, heated slowly and holding heat for long sessions.","","traditional",SAUNA,
     [],dt="large stone mass · slow heat-up · sealed stone compartment with chimney"),
   X("Harvia Legend","Black steel-framed wood-burning heater with a large stone mass and a grate that sends part of the air to an upper chamber.","Harvia","",LEG,
     [("Legend 240","Harvia","","10–24 m³ rooms; 200 kg of stones; cast-iron glass door")],
     dt="room size · stone mass · door (cast iron or steel frame) · optional pipe-mounted water heater"),
   X("Harvia Cilindro","Tall narrow pillar-type electric heater giving small saunas a large stone surface.","Harvia","",CIL,
     [("Cilindro PC66E","Harvia","","6.6 kW; about 165 lb of stones; needs a separate control unit")],
     dt="power 6.6 kW and up · stainless or black steel · integrated or separate control"),
   X("HUUM Drop","Estonian electric heater with a round stainless-steel shell holding a large stone load.","HUUM","2015",HIVE,
     [("Drop","HUUM","2015","Red Dot Award for Product Design")],dt="stone capacity · power · UKU controller"),
   X("HUUM Hive","Floor-standing stainless-steel electric heater for large saunas, holding up to 250 kg of stones.","HUUM","",HIVE,
     [("Hive 12","HUUM","","12 kW, 12–18 m³"),("Hive 15","HUUM","","15 kW, 15–23 m³"),("Hive 18","HUUM","","18 kW, 18–28 m³"),("Air Tunnel","HUUM","2024","central stainless housing, standard from April 2024")],
     dt="750 × 560 × 560 mm · three-phase · UKU Local or Wi-Fi controller"),
   X("Saunum Air","Electric heater with a patented air-mixing system that evens out temperature between ceiling and floor.","Saunum","",SAUNUM,
     [("Air Perfect","Saunum","2024","Golden Wave award for most innovative technology"),("Air L","Saunum","",""),("Luxury","Saunum","","air-mixing heater with design casing"),("AirSolo","Saunum","","climate device used beside an ordinary wood or electric heater")],
     dt="air mixing · size · casing"),
   X("Tylö Sense Combi Elite","Combi heater giving both dry heat and humid steam bathing.","Tylö","",TYLO,[],dt="dry or humid modes · control panel"),
   X("Helo Himalaya","Combi sauna heater from Helo, the Finnish maker merged with Tylö in 2017.","Helo","",TYLO,[],dt=""),
  ]},
 {"n":"Portable sauna","a":"folding sauna · sauna tent · infrared tent · sauna blanket","d":"Sauna that is set up or folded inside a home, not a cabin standing as a building.",
  "t":["folding infrared cabin","infrared pop-up tent","sauna blanket","steam tent","wood-fired tent sauna"],
  "s":"https://www.wayfair.ca/outdoor/sb1/portable-saunas-c517774-a78717~456601.html","x":[
   X("Infrared tent sauna","Cheap sauna made as a tent with an infrared element inside.","","",IR,[],dt="tent size · emitter type · seat"),
  ]},
 {"n":"Steam room","a":"steam bath · steam cabin · steam shower · home hammam","d":"Sealed room or cabin filled with steam from a generator, at about 43–46 °C and near 100% humidity.",
  "t":["steam shower cabin","tiled bespoke steam room","prefabricated steam cabin","steam generator","aroma dosing","heated seats","starry-sky ceiling"],
  "s":STEAM,"x":[
   X("Klafs HOMBRE","Solid steam bath clad in porcelain stoneware with heated seats and push-button steam.","Klafs","",KLSTEAM,[],dt="porcelain stoneware · heated seats"),
   X("Klafs D12","Modular steam bath with glass walls, teak and natural stone accents and adaptable layout.","Klafs","",KLSTEAM,
     [("D12 Vario","Klafs","","onsen bath combining steam, bath and shower")],dt="modular size · glass · teak · natural stone"),
   X("Klafs QUADRANO","Design steam bath with raised seating and acrylic lounge areas.","Klafs","",KLSTEAM,[],dt="acrylic loungers · raised seats"),
   X("Klafs steam shower","Compact cabin for up to two people combining steam bath and shower.","Klafs","",KLSTEAM,[],dt="folding seat · starry-sky light"),
   X("Steamist Total Sense","Residential steam-bath system with spa options for chromatherapy, aromatherapy and music.","Steamist","",STEAMIST,
     [("InstaMist","Steamist","",""),("EvenSteam","Steamist","","")],dt="generator size · controls · spa options"),
  ]},
 {"n":"Hard-shell hot tub","a":"spa · acrylic hot tub · portable spa","d":"Hot tub with a moulded rigid shell and built-in heater and pumps.",
  "t":["cast acrylic shell","rotomoulded","plug-and-play","salt water system","lounger seat","wood or composite skirt"],
  "s":"https://leisuretimeinc.com/collections/caldera-hot-tubs",
  "m":[["Grandee","Hot Spring Spas"],["Jetsetter","Hot Spring Spas"],["Prism","Hot Spring Spas"],["Pulse","Hot Spring Spas"],["Rhythm","Hot Spring Spas"],["Caldera Ravello","Caldera Spas"],["Caldera Kauai","Caldera Spas"],["Celio","Caldera Spas"]],
  "r":[["Highlife","Hot Spring Spas"],["Limelight","Hot Spring Spas"],["Hot Spot","Hot Spring Spas"],["Freeflow","Hot Spring Spas"],["Utopia Series","Caldera Spas"],["Paradise Series","Caldera Spas"],["Vacanza Series","Caldera Spas"],["Fantasy Series","Caldera Spas"],["Sundance Spas","Jacuzzi"],["Hydropool","Jacuzzi"],["Twilight","Master Spas"]]},
 {"n":"Inflatable hot tub","a":"blow-up hot tub · inflatable spa","d":"Portable hot tub with an inflatable body and a plug-in heater and pump.",
  "t":["round","square","air jets","hydro jets","frost protection"],
  "s":"https://www.decathlon.co.uk/p/mp/bestway/bestway-brown-lay-z-spa-vegas-airjet-inflatable-hot-tub/_/R-p-3a4e0a43-c897-47ef-b319-1faa5701f4ed",
  "m":[["Lay-Z-Spa Vegas AirJet","Bestway"]],"r":[["Lay-Z-Spa","Bestway"]]},
 {"n":"Wood-fired hot tub","a":"wood-heated hot tub · still-water hot tub · hot tub with stove","d":"Tub of hot water heated by a wood-burning stove, inside or beside the tub.",
  "t":["external stove","internal (submersible) stove","wooden staves","plastic liner","aluminium liner","electric heater add-on"],
  "s":"https://homedepot.com/p/ALMOST-HEAVEN-SAUNAS-Kirami-4-Person-Wood-Fired-Hot-Tub-AHKIRAMI4P/324712696","x":[
   X("Goemon-buro","Japanese one-person bath: a tub over a cast-iron kettle heated by a stove built beneath it; the bather sits on a wooden board.","","named after the Azuchi-Momoyama outlaw Ishikawa Goemon",GOEMON,
     [("Chōshū-buro","","","southern Chōshū (Yamaguchi) variant, flue of ridge tiles or stone")],a="goemonburo · Goemon bath",dt="cast-iron kettle · bottom board (soko-ita) · fixed, often outdoors"),
   X("Redwood hot tub","Round tub of vertical redwood or cedar staves held by metal bands, first made from converted wine vats and heated by wood fire.","","1960s, Northern California",SPAHIST,
     [("Wine-vat conversions","","1960s","counterculture origin"),("Cooperage-built tubs","California Cooperage","",""),("Cooperage-built tubs","T.E. Brown","","")],dt="redwood, teak or cedar staves · metal bands"),
   X("Kirami still-water hot tub","Finnish wood-heated still-water hot tub, the main product of Kirami of Sastamala.","Kirami","2001",KIR,[],dt="stove · tub material · size"),
  ]},
 {"n":"Swim spa","a":"swimming spa · endless pool","d":"Long hard-shell spa with a swim current, heated and filtered like a hot tub, for swimming in place.",
  "t":["swim current jets","propeller current","dual-zone (swim and spa)","in-ground or above-ground"],
  "s":"https://www.jacuzzi.com/en-us/need-to-know-before-buying-a-swim-spa.html",
  "m":[["Michael Phelps Signature Swim Spa","Master Spas"],["H2X Challenger Pro","Master Spas"]],"r":[["H2X","Master Spas"],["H2X Challenger","Master Spas"]]},
 {"n":"Cold plunge tub","a":"ice bath · plunge tub · cold tub","d":"Tub of cold water, kept cold by a chiller or by ice, for brief cold immersion.",
  "t":["chiller-cooled","ice-filled","inflatable","acrylic and stainless steel","vertical","hot-and-cold combined"],
  "s":PLUNGE,
  "m":[["All-In Gen 2","Plunge"],["Cold Plunge Pro","Sun Home"],["Cold Plunge Vertical","Sun Home"],["Pod with Pro Chiller","Polar Dive"],["NordPod Plus","LifePro"],["Michael Phelps Chilly GOAT Cold Tub","Master Spas"],["Vigor","Hot Spring Spas"]]},
]
B=lambda n,c,f,seg,d,s,lines=(),eras=(),sig=(),rel=(): {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":list(lines),"eras":list(eras),"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Klafs","Germany","1928","Luxury saunas, steam baths and pools","Sauna, pool and spa maker based in Schwäbisch Hall.",S1,["S1","HOMBRE","D12","QUADRANO"],[],["Klafs S1","Klafs HOMBRE","Klafs D12"],["Harvia","Tylö"]),
 B("Harvia","Finland","1950","Sauna heaters and saunas","Sauna heater maker founded by Tapani Harvia in Jyväskylä, now based in Muurame; owns Sentiotec, Almost Heaven, EOS and Kirami.",HARVIA,["Legend","Cilindro","Spirit","Ventura"],[],["Harvia Legend","Harvia Cilindro"],["Kirami","Tylö","Klafs"]),
 B("Tylö","Sweden","c. 1949","Sauna heaters, steam generators and saunas","Halmstad maker started by electrician Sven-Olof Janson and named after the island of Tylön; joined Helo as TylöHelo in 2017.",TYLO,["Sense"],["TylöHelo, from 2017"],["Tylö Sense Combi Elite","TylöHelo Jubilee Sauna"],["Helo","Harvia"]),
 B("Helo","Finland","1919","Sauna heaters","Sauna maker founded in Viborg, Karelia; merged with Tylö in 2017.",TYLO,["Himalaya"],[],["Helo Himalaya"],["Tylö"]),
 B("HUUM","Estonia","","Design sauna heaters","Estonian maker of stainless-steel electric and wood sauna heaters built in Estonia.",HUUM,["Drop","Hive"],[],["HUUM Drop","HUUM Hive"],["Saunum","Harvia"]),
 B("Saunum","","","Sauna heaters","Heater maker known for patented air-mixing heaters.",SAUNUM,["Air","Luxury","AirSolo"],[],["Saunum Air"],["HUUM"]),
 B("Steamist","United States","","Residential steam baths","Steam-bath equipment maker in East Rutherford, New Jersey, focused on home steam systems.",STEAMIST,["Total Sense","InstaMist","EvenSteam"],[],["Steamist Total Sense"],[]),
 B("Jacuzzi","United States","1915","Hot tubs and whirlpool baths","Founded in Berkeley, California, by seven Jacuzzi siblings; Roy Jacuzzi's Roman Bath of 1968 was its first whirlpool bath.",JAC,["Sundance Spas","Hydropool","Gatsby Spas"],[],[],["Hot Spring Spas"]),
 B("Hot Spring Spas","United States","1977","Hard-shell hot tubs","Watkins Wellness brand whose 1977 Hot Spring Spa was among the first self-contained portable spas.",HS,["Highlife","Limelight","Hot Spot","Freeflow"],[],[],["Caldera Spas","Jacuzzi"]),
 B("Caldera Spas","United States","","Hard-shell hot tubs","Watkins-linked hot tub brand with Utopia, Paradise, Vacanza and Fantasy series.",CAL,["Utopia Series","Paradise Series","Vacanza Series","Fantasy Series"],[],[],["Hot Spring Spas"]),
 B("Master Spas","United States","","Hot tubs and swim spas","Midwest hot tub and swim spa maker; Michael Phelps signature swim spas since 2010.",MS,["H2X","Twilight","Michael Phelps Signature"],[],[],[]),
 B("Bestway","China","1994","Inflatable pools and hot tubs","Inflatables maker selling Lay-Z-Spa inflatable hot tubs since 2006.",BW,["Lay-Z-Spa"],[],[],[]),
 B("Kirami","Finland","2001","Wood-fired hot tubs","Family firm in Sastamala making wood-heated still-water hot tubs; part of Harvia since 2021.",KIR,[],[],["Kirami still-water hot tub"],["Harvia"]),
]
T=lambda n,r,p,d,tech,mat,forms,ctr,auth,s,g="Bathing traditions": {"n":n,"g":g,"r":r,"p":p,"d":d,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":s}
trads=[
 T("Finnish sauna","Finland","traditional; UNESCO list 2020","Hot-air bathing at 80–110 °C with löyly from water on the stones of a kiuas, alternated with cooling off.","wood or electric stove with stones; löyly; birch whisking","wood, stone, birch",["Sauna cabin","Sauna heater"],["Finnish Heritage Agency"],"wood stove with stone mass; sessions with vihta/vasta whisk",FIN),
 T("Võro smoke sauna","Võromaa, Estonia","traditional; UNESCO list 2014","Chimneyless smoke sauna tradition including bathing customs, whisk-making, sauna building and meat smoking.","stone-covered stove without chimney; smoke vented before bathing","wood, stone",["Sauna cabin"],["Võro community"],"no chimney; raised platform; smoke-blackened interior",VORO),
 T("Russian banya","Russia and East Slavic lands","from Kievan Rus'","Wood-heated steam bath with venik whisking, in black (smoke) or white (piped) form.","stove with firebox, stone chamber and water tank; venik","wood, stone, birch, oak",["Sauna cabin"],["Sanduny (Moscow)"],"three-room plan; venik; felt hat",BANYA),
 T("Turkish hammam","Islamic world, Ottoman lands","Umayyad period onwards; classical peak 16th century","Steam bath descended from Roman thermae, with warm and hot rooms and a heated marble navel stone.","furnace and hypocaust; steam","marble, plaster",["Steam room"],["Çemberlitaş, Süleymaniye (Istanbul)","Mimar Sinan"],"marble göbek taşı; domed hot room with skylights",HAMMAM),
 T("Japanese furo","Japan","traditional","Deep, square soaking bath entered after washing, traditionally wooden (hinoki) or a wood-fired cast-iron goemon-buro.","soak at 38–42 °C after rinsing; wood-fired kettle in goemon-buro","hinoki wood, cast iron",["Wood-fired hot tub"],["Kansai region"],"deep square tub; no overflow; hinoki wood",OFURO),
]
notes=("Kept all six old kinds; added Sauna heater, Steam room and Cold plunge tub. Hard-shell tub: cut 12-model Caldera SKU list to 8 models across Hot Spring and Caldera plus ranges. "
 "Left out: independent test winners (Which?/Consumer Reports pages not retrieved), Tylö VA steam generator and Harvia Legend 150/300 sizes (seen only in search snippets), "
 "Kirami tub models, Kastor heaters (brand named only), Endless Pools and Sundance models, Harvia Spirit (only a caption). Saunum country and HUUM founding year not on retrieved pages.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p="work/G3/shelves/01_02.json"; tmp=p+".tmp"
json.dump(out,open(tmp,"w"),ensure_ascii=False,indent=1); os.replace(tmp,p); print("written")
