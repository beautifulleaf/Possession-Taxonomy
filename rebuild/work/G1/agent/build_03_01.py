import json, os
WP='https://en.wikipedia.org/wiki/'
def A(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),x)) for x in v],"dt":dt}
kinds=[
 {"n":"Cross-country mountain bike","a":"XC bike · cross-country bike","d":"Light mountain bike with short suspension travel, made for climbing and fast off-road riding.",
  "t":["hardtail","full suspension","29-inch wheels"],"s":WP+"Cross-country_cycling",
  "x":[A("Breezer Series 1","Joe Breeze's chrome-moly klunker-style bikes with twin lateral tubes, widely considered the first modern mountain bikes.","Breezer","1977",WP+"Joe_Breeze",
         [("Breezer #1","Breezer","1977","prototype, completed autumn 1977"),("Series 1 run","Breezer","1978","nine more built by June 1978, ten in all")],"chrome-moly steel frame · twin lateral tubes"),
       A("Specialized Epic","Specialized's carbon cross-country line, begun as the first production carbon-fibre mountain bike.","Specialized","1988",WP+"Specialized_Bicycle_Components",
         [("Stumpjumper Epic","Specialized","1988","first production carbon-fibre mountain bike"),("Epic with Brain shock","Specialized","2002","stand-alone full-suspension XC Epic"),("Epic redesign","Specialized","2008","")],"frame material · suspension (hardtail or Brain full suspension)"),
       A("Santa Cruz Blur","Santa Cruz's short-travel 29-inch cross-country race bike.","Santa Cruz","",WP+"Santa_Cruz_Bicycles",
         [("Blur XC","Santa Cruz","2018","107 mm travel, reintroduced 2018"),("Blur TR","Santa Cruz","","115 mm travel")],"29-inch wheels · travel setting")],
  "m":[["Exceed","Canyon"],["Chisel","Specialized"]]},
 {"n":"Trail mountain bike","a":"trail bike · all-mountain bike","d":"Mid-travel full-suspension mountain bike made for all-round trail riding, climbing and descending.",
  "t":["29-inch","mullet (mixed wheels)","27.5-inch","short-travel (downcountry)"],"s":WP+"Mountain_bike",
  "x":[A("Specialized Stumpjumper","The first mass-produced mountain bike, designed by Tim Neenan from an early Tom Ritchey design; now a full-suspension trail line.","Specialized","1981",WP+"Specialized_Bicycle_Components",
         [("Original Stumpjumper","Specialized","1981","first major production mountain bike; one is in the Smithsonian"),("Stumpjumper hardtail","Specialized","1991–2016",""),("First full-suspension Stumpjumper","Specialized","1993","line now full-suspension only")],"hardtail or full suspension · frame material · wheel size"),
       A("Trek Fuel EX","Trek's all-round full-suspension trail bike with ABP suspension, sitting between the Top Fuel and longer-travel bikes.","Trek","c. 2005",WP and "https://flowmountainbike.com/tests/trek-fuel-ex-8-gen-7-review-2026/",
         [("Gen 6","Trek","","reviewed by Flow in 2022"),("Gen 7 Fuel EX","Trek","2026 model year","145 mm rear, 150 mm fork, 29-inch; alloy or carbon"),("Fuel MX","Trek","2026 model year","160/150 mm, 29/27.5-inch mullet"),("Fuel LX","Trek","2026 model year","170/160 mm, 29-inch")],"generation · alloy or carbon · travel configuration"),
       A("Santa Cruz Bronson","Santa Cruz's 150 mm VPP trail bike on mixed 29/27.5-inch wheels.","Santa Cruz","",WP+"Santa_Cruz_Bicycles",[("Bronson MX","Santa Cruz","","150 mm VPP, 29-inch front, 27.5-inch rear")],"carbon or alloy · mixed wheels",a="Roubion (alloy)"),
       A("Santa Cruz Hightower","Santa Cruz's 150 mm VPP 29-inch trail bike.","Santa Cruz","",WP+"Santa_Cruz_Bicycles",[],"29-inch · 150 mm VPP"),
       A("Canyon Spectral","Canyon's direct-sale trail bike, launched on 27.5-inch wheels and later offered as 29er, mullet and short-travel versions.","Canyon","2014","https://flowmountainbike.com/tests/2024-canyon-spectral-cf-9-review/",
         [("Spectral (original)","Canyon","2014","27.5-inch"),("Spectral 29","Canyon","2020",""),("Spectral mullet","Canyon","2021",""),("Spectral 125","Canyon","2022","short-travel"),("Spectral 2024","Canyon","2024","new carbon frame, 140 mm rear / 150 mm fork, flip chip for 29 or mullet")],"wheel size · travel · carbon or alloy")],
  "m":[["Neuron","Canyon"],["Tallboy","Santa Cruz"]]},
 {"n":"Enduro mountain bike","a":"enduro bike · long-travel trail bike","d":"Long-travel mountain bike made for timed descents and the untimed climbs between them.",
  "t":["29-inch","mullet (mixed wheels)","coil or air shock"],"s":WP+"Enduro_(mountain_biking)",
  "x":[A("Santa Cruz Nomad","Santa Cruz's long-travel 170 mm VPP bike on mixed wheels.","Santa Cruz","",WP+"Santa_Cruz_Bicycles",[("Nomad MX","Santa Cruz","","170 mm VPP, 29-inch front, 27.5-inch rear")],"carbon or alloy · mixed wheels"),
       A("Santa Cruz Megatower","Santa Cruz's 165 mm VPP 29-inch enduro bike.","Santa Cruz","",WP+"Santa_Cruz_Bicycles",[],"29-inch · 165 mm VPP"),
       A("Yeti SB","Yeti's family of full-suspension bikes, first with dual-link Switch Technology, then Switch Infinity from 2014.","Yeti","",WP+"Yeti_Cycles",
         [("SB66 / SB75 / SB95","Yeti","","early Switch Technology models"),("SB5 / SB4.5 / SB5.5 / SB6","Yeti","2014 on","Switch Infinity"),("SB130 / SB150","Yeti","","Switch Infinity; discontinued"),("SB160","Yeti","","Switch Infinity; current")],"model number (travel) · wheel size"),
       A("Canyon Strive","Canyon's enduro race bike; the first Canyon Factory Racing bike.","Canyon","2020",WP+"Canyon_Bicycles",[("Strive CFR","Canyon","2020","first Canyon Factory Racing bike")],"carbon frame · travel")],
  "m":[["Torque","Canyon"]]},
 {"n":"Downhill mountain bike","a":"DH bike · gravity bike","d":"Very long-travel full-suspension mountain bike with a dual-crown fork, made for steep lift- or shuttle-served descents.",
  "t":["27.5-inch","29-inch","mullet (mixed wheels)"],"s":WP+"Downhill_mountain_biking",
  "x":[A("Santa Cruz V10","Santa Cruz's 208 mm VPP downhill race bike.","Santa Cruz","",WP+"Santa_Cruz_Bicycles",[("V10 MX","Santa Cruz","","mixed wheels"),("V10 29","Santa Cruz","","29-inch")],"wheel size · 208 mm VPP")],
  "m":[["Sender","Canyon"]]},
 {"n":"Dirt-jump mountain bike","a":"dirt jumper · DJ bike · jump bike","d":"Small, strong hardtail mountain bike with short-travel or rigid fork, made for jumps and pump tracks.",
  "t":["26-inch","24-inch","single speed","hardtail","short-travel full suspension"],"s":WP+"Dirt_jumping",
  "m":[["Stitched","Canyon"],["Alcatraz","Marin"]]},
 {"n":"Fat bike","a":"fatbike · fat-tyre bike · snow bike","d":"Bicycle with tyres of about 3.8 in (97 mm) or wider on wide rims, made for snow and sand.",
  "t":["rigid","suspension fork","full suspension","carbon","steel"],"s":WP+"Fat_bike",
  "x":[A("Wildfire Designs fat bike","Mark Gronewald's Alaskan fat-tyre bikes; he coined the trademark 'Fat Bike' in 2001.","Wildfire Designs","2000",WP+"Fat_bike",[],"frame · rim and tyre width"),
       A("Surly Pugsley","Surly's steel fat-bike frame that made fat bikes commercially available in shops worldwide.","Surly","2005",WP+"Surly_Bikes",
         [("Pugsley frame","Surly","2005","offset rear for a common hub"),("Large Marge rims and Endomorph 3.8-inch tyres","Surly","2006","fat rims and tyres for the platform")],"steel frame · rim and tyre width"),
       A("Fatback Corvus","Early carbon fat bike from Alaskan maker Fatback Bikes.","Fatback","2007",WP+"Fat_bike",[],"carbon frame")],
  "m":[["Mukluk","Salsa Cycles"],["Beargrease","Salsa Cycles"],["Heyday!","Salsa Cycles"]]},
 {"n":"BMX bike","a":"bicycle motocross bike","d":"Small-wheeled bicycle made for racing or stunt riding.",
  "t":["race","freestyle park","street","flatland","dirt","24-inch cruiser"],"s":WP+"BMX_bike",
  "x":[A("Haro Freestyler","The first frame and fork designed and sold specifically for freestyle BMX, built for Bob Haro by Torker.","Haro","1982","https://bmxmuseum.com/reference/2865",
         [("Mark 1","Haro","1982","built by Torker in Fullerton, July–October 1982"),("Mark 2","Haro","1982–1984","made after October 1982 to January 1984")],"73° head angle · twin top tubes · gussets",a="Torker-built Freestyler"),
       A("GT Pro Performer","GT's first freestyle bike, developed with Bob Morales and Eddie Fiola; its bent down tube became a GT trademark.","GT","1984",WP+"GT_Bicycles",[],"bent down tube · freestyle frame and fork")],
  "m":[["Legion L20","Mongoose"],["Legion L40","Mongoose"],["Title Pro","Mongoose"],["Title Expert","Mongoose"],["Rebel X24","Mongoose"]]},
]
# fix Fuel EX source
kinds[1]["x"][1]["s"]="https://flowmountainbike.com/tests/trek-fuel-ex-8-gen-7-review-2026/"
def B(n,c,f,seg,d,lines,sig,s,rel=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"eras":[],"sig":sig,"sc":[],"rel":list(rel),"s":s}
brands=[
 B("Specialized","United States","1974","Performance bicycles","Bicycle maker founded by Mike Sinyard, based in Morgan Hill, California.",["Stumpjumper","Epic","Chisel"],["Specialized Stumpjumper","Specialized Epic"],WP+"Specialized_Bicycle_Components",["Trek"]),
 B("Trek","United States","1976","Performance bicycles","Bicycle maker based in Waterloo, Wisconsin, founded by Dick Burke and Bevil Hogg; owns Electra.",["Fuel EX","Top Fuel"],["Trek Fuel EX"],WP+"Trek_Bicycle_Corporation",["Specialized"]),
 B("Santa Cruz","United States","","Premium mountain bikes","Santa Cruz, California mountain-bike maker known for VPP suspension; owned by Pon Holdings since 2015.",["Bronson","Nomad","Hightower","Megatower","V10","Blur","Tallboy"],["Santa Cruz V10","Santa Cruz Nomad","Santa Cruz Bronson"],WP+"Santa_Cruz_Bicycles",["GT","Yeti"]),
 B("Yeti","United States","1985","Premium mountain bikes","Mountain-bike maker founded by John Parker, based in Golden, Colorado; known for Switch Infinity suspension.",["SB series","ARC"],["Yeti SB"],WP+"Yeti_Cycles",["Santa Cruz"]),
 B("Canyon","Germany","","Direct-sale bicycles","Koblenz bicycle maker that grew from Radsport Arnold and sells direct to consumers.",["Spectral","Strive","Neuron","Sender","Exceed","Stitched","Torque"],["Canyon Spectral","Canyon Strive"],WP+"Canyon_Bicycles"),
 B("Breezer","United States","","Bicycles","Joe Breeze's brand, which began with the Breezer mountain bikes of 1977–78; sold to Advanced Sports International in 2008.",[],["Breezer Series 1"],WP+"Joe_Breeze"),
 B("Surly","United States","1998","Steel bicycles","Bloomington, Minnesota steel-frame brand, a division of Quality Bicycle Products.",["Pugsley"],["Surly Pugsley"],WP+"Surly_Bikes",["Salsa Cycles"]),
 B("Salsa Cycles","United States","","Adventure bicycles","Brand founded by Ross Shafer in the early 1980s, owned by Quality Bicycle Products since 1997.",["Mukluk","Beargrease"],[],WP+"Salsa_Cycles",["Surly"]),
 B("Fatback","United States","2007","Fat bikes","Alaskan fat-bike maker that launched with the carbon Corvus in 2007.",["Corvus"],["Fatback Corvus"],WP+"Fat_bike"),
 B("Wildfire Designs","United States","2000","Fat bikes","Mark Gronewald's workshop in Palmer, Alaska, which built early fat bikes from 2000.",[],["Wildfire Designs fat bike"],WP+"Fat_bike"),
 B("Haro","United States","1978","BMX and bicycles","BMX brand founded by freestyle pioneer Bob Haro.",["Freestyler"],["Haro Freestyler"],WP+"Haro_Bikes",["GT","Mongoose"]),
 B("GT","United States","1972","BMX and mountain bikes","Bicycle maker founded by Gary Turner and Richard Long in Santa Ana, California; owned by Pon Holdings since 2021.",["Pro Performer"],["GT Pro Performer"],WP+"GT_Bicycles",["Haro","Mongoose"]),
 B("Mongoose","United States","1974","BMX and bicycles","Brand begun by Skip Hess's BMX Products, Inc. in Simi Valley, California; now owned by Pon Holdings.",["Legion","Title"],[],WP+"Mongoose_(bicycles)",["GT","Haro"]),
 B("Marin","United States","1986","Mountain bikes","Marin County mountain-bike maker founded by Bob Buckley.",["Alcatraz"],[],WP+"Marin_Bikes"),
]
notes=("All seven old kinds kept (k45–k51); kind sources switched from retailer pages to fetched Wikipedia articles. "
 "Archetypes: Breezer Series 1, Specialized Epic, Santa Cruz Blur/Bronson/Hightower/Nomad/Megatower/V10, Specialized Stumpjumper, Trek Fuel EX, Canyon Spectral/Strive, Yeti SB, Wildfire Designs fat bike, Surly Pugsley, Fatback Corvus, Haro Freestyler, GT Pro Performer. "
 "Canyon-only lists cut: Lux Trail and Stoic dropped (trail list now multi-brand); Mongoose Legion L10, L18, MX dropped as SKU noise. "
 "Left out: Kona Process (pinkbike 403, vitalmtb/mbaction returned no content, no retrieved page confirms it) so no Kona entry; Mongoose classic BMX models (Supergoose etc.) not confirmed on any fetched page; "
 "Specialized Demo, Trek Session, Commencal Supreme not confirmed; model years for Santa Cruz and Yeti models not given on their pages, so left blank; Salsa Mukluk year unknown, kept in m. No craft traditions relevant.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/G1/shelves/03_01.json'; os.makedirs(os.path.dirname(p),exist_ok=True)
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print('ok')
