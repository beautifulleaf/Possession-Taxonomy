import json, os
W='https://en.wikipedia.org/wiki/'
def v(n,mk,y,d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def x(n,a,d,mk,y,s,vs,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":vs,"dt":dt}
ATV=W+'All-terrain_vehicle'
quad={"n":"Quad bike","a":"ATV · quad · four-wheeler · three-wheeler (ATC)","d":"Straddle-seat all-terrain vehicle with handlebars and low-pressure tyres, off-road or road-registered.",
 "t":["sport (two-wheel drive, manual)","utility (four-wheel drive, racks, towing)","youth","two-up","road-registered","three-wheeled ATC (vintage)","electric"],
 "s":"https://www.polaris.com/en-us/off-road/atv-4-wheeler/",
 "x":[
  x("Honda ATC","All Terrain Cycle · three-wheeler · US90 · ATC90","Three-wheeled balloon-tyred straddle vehicle that created the ATV market; Honda left three-wheelers in 1987.","Honda","1970–1987",W+'List_of_Honda_three-wheeled_all-terrain_vehicles',
    [v("US90","Honda","1970","first model, designed by Osamu Takeuchi; enlarged ST70 engine"),v("ATC250R","Honda","1981","first Sport ATC built for competition; liquid-cooled 1985–1986"),
     v("ATC200E Big Red","Honda","1982","utility model"),v("ATC200X","Honda","1983","sport"),v("350X","Honda","1985","sport")],
    "engine size · sport or utility · racks · colour"),
  x("Suzuki QuadRacer LT250R","LT250R · QuadRacer","Lightweight fully suspended two-stroke sport quad that moved ATV racing from three wheels to four.","Suzuki","1985–1992",W+'Suzuki_LT250R',
    [v("QuadRunner LT125","Suzuki","1982","Suzuki's first four-wheeler"),v("LT250R QuadRacer","Suzuki","1985–1992","249 cc liquid-cooled two-stroke"),v("LT500R QuadRacer","Suzuki","1987–1990","larger follow-up")],
    "model year · engine · colour"),
  x("Honda FourTrax (TRX)","TRX · FourTrax · 250R · Rancher · Rincon","Honda's four-wheeled ATV family, from the TRX250R racer to the four-wheel-drive utility quads.","Honda","1986–",ATV,
    [v("FourTrax TRX250R","Honda","1986–1989","liquid-cooled two-stroke sport quad, long a racers' choice"),v("FourTrax TRX350 4x4","Honda","1986","began the four-wheel-drive ATV era"),
     v("Rancher (TRX420)","Honda","","utility; two generations"),v("Rincon","Honda","2003","recreational, automatic with torque converter; second model 2006")],
    "sport or utility · two- or four-wheel drive · manual or automatic"),
  x("Yamaha Banshee 350","Banshee · YFZ350","Sport quad with a twin-cylinder two-stroke engine from the RZ350 road bike.","Yamaha Motor","1987–2012",W+'Yamaha_Banshee_350',
    [v("YFZ350 (US)","Yamaha Motor","1987–2006","sold in Canada until 2008, Australia 1998–2012")],"model year · colour · aftermarket pipes and porting"),
  x("Yamaha Blaster","Blaster · YFS200","Compact entry-level two-stroke sport quad with a large aftermarket.","Yamaha Motor","1988–2006",W+'Yamaha_Blaster',[],"model year · colour · modifications"),
  x("Yamaha Raptor","Raptor 660 · Raptor 700R","Yamaha's four-stroke sport quad family.","Yamaha Motor","",W+'Yamaha_Raptor_700R',
    [v("Raptor 660","Yamaha Motor","","first generation"),v("Raptor 700R","Yamaha Motor","","second generation; 686 cc fuel-injected single, five-speed with reverse")],"engine · special editions · colour"),
  x("Yamaha Grizzly","Grizzly EPS","Yamaha's large utility ATV.","Yamaha Motor","",W+'Yamaha_Grizzly',[v("Grizzly EPS","Yamaha Motor","","electric power steering")],"engine · EPS · colour"),
  x("Polaris Scrambler and Trail Boss","Scrambler · Trail Boss","Polaris's first ATVs, regarded as the first American-made production ATVs.","Polaris","1985",W+'Polaris_Inc.',
    [v("Scrambler (three-wheeler)","Polaris","1985–1986","about 1,600 built"),v("Trail Boss","Polaris","1985","")],"three or four wheels · model year"),
  x("Can-Am Outlander and Renegade","Outlander · Renegade · Traxter","BRP's utility (Outlander) and sport-utility (Renegade) quads, successors to the Traxter.","Can-Am","1998–",W+'Can-Am_Off-Road',
    [v("Traxter","Can-Am","1998","utility ATV; XL 2000, two-seat MAX 2002"),v("Outlander 800","Can-Am","2006",""),v("Renegade 800","Can-Am","2007",""),v("DS 450","Can-Am","","sport quad, X mx and X xc")],"engine · one or two seats (MAX) · trim")],
 "m":[["Sportsman 450","Polaris"],["Sportsman 570","Polaris"],["Sportsman XP 1000","Polaris"],["Outlaw 70","Polaris"],["YFZ50","Yamaha Motor"]]}
sxs={"n":"Side-by-side","a":"UTV · SxS · ROV · utility task vehicle","d":"Off-road vehicle with side-by-side seats in a roll cage, a steering wheel and foot controls.",
 "t":["sport","utility","recreational/crossover","two-seat","four- or six-seat (crew)","petrol","diesel","electric"],
 "s":W+'Side-by-side_(vehicle)',
 "x":[
  x("Kawasaki MULE","Multi-Use Light Equipment · Mule","Lightweight utility side-by-side series built since 1988, in petrol and diesel versions.","Kawasaki","1988–",W+'Kawasaki_MULE',
    [v("MULE 1000","Kawasaki","1988","original, 454 cc twin"),v("MULE 2500 series","Kawasaki","1992","diesel from 1999"),v("MULE 3000 series","Kawasaki","2000","diesel 2003; four-seat 2005"),
     v("MULE 4000 series","Kawasaki","2009","petrol and diesel"),v("MULE PRO-FXT","Kawasaki","2014","")],"seats · petrol or diesel · bed · cab"),
  x("Yamaha Rhino","Rhino","Two-seat two- or four-wheel-drive side-by-side built in Georgia, USA.","Yamaha Motor","2004–2012",W+'Yamaha_Rhino',[],"engine · drive · colour"),
  x("Polaris RZR","Ranger RZR · Razor","Sport side-by-side launched as a sub-model of the Ranger and now Polaris's performance line.","Polaris","2007–",W+'Polaris_RZR',
    [v("RZR 800","Polaris","2008","launched as Ranger RZR"),v("RZR S 800","Polaris","2009",""),v("RZR XP 900","Polaris","2011","875 cc"),v("RZR 570","Polaris","2012",""),
     v("RZR XP 1000","Polaris","2014","999 cc"),v("RZR XP Turbo","Polaris","2016",""),v("RZR Pro XP","Polaris","2020",""),v("RZR Pro R","Polaris","2022","1,997 cc")],
    "width · two or four seats · trim · colour"),
  x("Can-Am Maverick","Maverick · Maverick X3 · Maverick MAX","BRP's sport side-by-side, launched with the Maverick 1000R.","Can-Am","2013–",W+'Can-Am_Off-Road',
    [v("Maverick 1000R","Can-Am","2013","first model"),v("Maverick X3","Can-Am","",""),v("Maverick Sport","Can-Am","",""),v("Maverick Trail","Can-Am","","")],"two or four seats (MAX) · trim · width"),
  x("Can-Am Commander and Defender","Commander · Defender","BRP's crossover (Commander) and utility (Defender) side-by-sides.","Can-Am","2010–",W+'Can-Am_Off-Road',
    [v("Commander 1000","Can-Am","2010","first Can-Am side-by-side"),v("Defender 6x6","Can-Am","","tows up to 3,000 lb")],"seats · cab · bed")],
 "m":[["Ranger 1000","Polaris"],["Ranger XD 1500 NorthStar","Polaris"],["General XP 1000","Polaris"],["Mule SX","Kawasaki"]]}
buggy={"n":"Dune buggy","a":"beach buggy · sand rail · sand car · Baja Bug","d":"Light open off-road car with large wide tyres for sand, beaches and desert, often rear-engined.",
 "t":["fibreglass-bodied (Beetle-based)","tube-frame sand rail","Baja Bug","kit","turnkey","street-legal","electric"],
 "s":W+'Dune_buggy',
 "x":[
  x("Meyers Manx","Manx · Old Red","Roofless fibreglass two-seater body on a shortened Volkswagen Beetle chassis that defined the dune buggy.","Meyers Manx","1964–",W+'Meyers_Manx',
    [v("Old Red","Meyers Manx","1964","first car, built in Bruce Meyers's garage"),v("Manx Mk I","Meyers Manx","1965–1971","about 6,000 kits"),v("Manx SR","Meyers Manx","","sporty roadster"),
     v("Manxter 2+2 and DualSport","Meyers Manx","2002",""),v("Kick-Out Manx","Meyers Manx","2009","shortened wheelbase"),v("Manx 2.0 EV","Meyers Manx","","electric, revival company"),v("Classic Buggy","Meyers Manx","","")],
    "kit or turnkey · engine · body colour · copies (EMPI Imp and others)"),
  x("Baja Bug","Baja · Baja Beetle","Volkswagen Beetle cut and modified for desert and dune driving; raced in classes such as SCORE Class 11.","","1960s–",W+'Baja_Bug',[],"stock-based or race class · fibreglass panels · suspension"),
  x("Sandrail","sand rail · rail · sand car","Lightweight tube-frame off-road car built specifically for sand.","","",W+'Sandrail',[],"seats · engine · long-travel suspension"),
  x("Funco sand cars","Funco","High-performance long-travel sand cars from Funco Motorsports.","Funco Motorsports","",W+'Funco_Motorsports',
    [v("F9","Funco Motorsports",""),v("FD9","Funco Motorsports",""),v("GTX","Funco Motorsports","")],"seats · engine · suspension")]}
sled={"n":"Snowmobile","a":"sled · snowmachine · skidoo · motor sled","d":"Vehicle with a rear track and front skis made to travel over snow.",
 "t":["trail","mountain (deep snow)","snocross/race","crossover","touring (two-up)","utility/working","youth","two-stroke","four-stroke","electric"],
 "s":"https://ski-doo.brp.com/us/en/",
 "x":[
  x("Ski-Doo","Ski-Dog · skidoo","Open-cockpit personal snowmobile introduced by Joseph-Armand Bombardier; its name became the Canadian generic word.","Ski-Doo","1959–",W+'Ski-Doo',
    [v("first Ski-Doo","Ski-Doo","1959","named Ski-Dog until a brochure typo"),v("MXZ","Ski-Doo","","trail; Gen-4 2017"),v("Summit","Ski-Doo","","mountain; Gen-4 2017"),v("Renegade","Ski-Doo","","crossover; Gen-4 2017"),
     v("Expedition","Ski-Doo","","touring"),v("Skandic","Ski-Doo","","utility"),v("Tundra","Ski-Doo","","utility"),v("Freeride","Ski-Doo","","")],"track length · engine · platform · colour"),
  x("Polaris Sno Traveler","Sno-Traveler","Polaris's first commercial snowmobile.","Polaris","1957",W+'Snowmobile',[],"condition · restoration"),
  x("Polaris Indy","Indy","Polaris's trail-sled line, built from the early 1980s, paused in 2004 and revived in 2012.","Polaris","1980s–",W+'Polaris_Inc.',
    [v("Indy 600 and 600 SP","Polaris","2013","revival")],"engine · track · colour"),
  x("Polaris RMK","Rocky Mountain King","Polaris's two-stroke mountain and deep-snow snowmobile series.","Polaris","1996–",W+'Polaris_RMK',[],"track length · engine · chassis"),
  x("Arctic Cat snowmobiles","Arctic Cat · Boss Cat","Snowmobiles from the Minnesota firm founded by Edgar Hetteen; now part of Textron.","Arctic Cat","1960–",W+'Arctic_Cat',[v("Boss Cat","Arctic Cat","1970",""),v("M800","Arctic Cat","","mountain")],"model line · engine · colour"),
  x("Lynx","Lynx snowmobile","Finnish snowmobile brand, now BRP, with PPS rear suspension for rough conditions.","Lynx","1968–",W+'Lynx_(snowmobile)',[v("first Lynx","Lynx","1968","Velsa Oy, Kurikka")],"suspension · engine · track")],
 "m":[["Switchback","Polaris"]]}
golf={"n":"Golf cart","a":"golf buggy · golf car · personal transportation vehicle · LSV","d":"Small low-speed vehicle made to carry golfers and bags, also used privately round estates and communities.",
 "t":["two-seat","four- or six-seat","lifted","electric","petrol","street-legal (LSV)","utility bed"],
 "s":"https://www.clubcar.com/en/personal/golf-carts/onward-4-passenger",
 "x":[
  x("Club Car DS","DS","Club Car's signature golf car, named after designer Dom Saporito.","Club Car","c.1980–2004",W+'Club_Car',[],"electric or petrol · year · colour"),
  x("Club Car Precedent","Precedent · Tempo","Club Car's golf car from 2004, replaced by the Tempo in 2018.","Club Car","2004–",W+'Club_Car',[v("Precedent i2","Club Car","2008","new drive system"),v("Precedent i3","Club Car","2008","first connected golf cart"),v("Tempo","Club Car","2018","replacement")],"electric or petrol · seats"),
  x("Club Car Onward","Onward · Onward LSV","Club Car's personal transportation line for private owners.","Club Car","2017–",W+'Club_Car',[v("Onward LSV","Club Car","2025","street-legal low-speed vehicle")],"seats · lifted · electric or petrol"),
  x("Marketeer golf cart","Marketeer","Early electric golf cart by Merle Williams of Long Beach, California.","","1951",W+'Golf_cart',[],"vintage condition")],
 "m":[]}
kart={"n":"Go-kart","a":"kart · go-cart · racing kart","d":"Small open single-seat four-wheeled vehicle with a low chassis and no suspension.",
 "t":["sprint chassis","cadet/mini chassis","shifter","rental/leisure","off-road kart","electric","pedal (children's)"],
 "s":"https://nextkarting.co.uk/collections/karts-chassis",
 "x":[
  x("Ingels go-kart","first go-kart","Original go-kart built from scrap metal and a West Bend two-stroke by Art Ingels in 1956.","","1956",W+'Art_Ingels',[],""),
  x("Tony Kart","OTK · Tony Kart","Italian racing chassis brand of OTK Kart Group, with many world titles.","Tony Kart","1958–",W+'OTK_Kart_Group',
    [v("Racer 401 T","Tony Kart",""),v("LN Lando","Tony Kart",""),v("Kosmic 950 Mini Rookie","Tony Kart","","Kosmic brand, 1996–"),v("e-Viper","Tony Kart","","electric")],"class (cadet, senior, shifter) · tube diameter · engine"),
  x("CRG","Kalì Kart","Italian kart chassis maker founded as Kalì Kart, renamed CRG in 1986.","CRG","1986–",W+'CRG_(kart_manufacturer)',[],"class · chassis · engine"),
  x("Birel","Birel · Easykart","Kart maker from Lissone near Milan, building karts since the late 1950s.","Birel","1950s–",W+'Birel',[v("Easykart","Birel","","one-make classes 60 cc Cadet to 125 cc")],"class · chassis · engine")]}
amph={"n":"Amphibious vehicle","a":"amphibian · amphicar · amphibious ATV · AATV","d":"Vehicle that drives on land and floats or travels on water.",
 "t":["amphibious car","amphibious ATV (6x6, 8x8)","amphibious quad","tracks","outboard"],
 "s":W+'Amphibious_vehicle',
 "x":[
  x("Volkswagen Schwimmwagen","Type 166","Light four-wheel-drive amphibious car of the Second World War; the most-produced amphibious car.","Volkswagen","1941–",W+'Volkswagen_Schwimmwagen',[v("Type 128","Volkswagen","","prototype"),v("Type 166","Volkswagen","1941","production")],"originality · restoration"),
  x("Amphicar 770","Amphicar","West German amphibious car designed by Hans Trippel; 3,878 built.","Amphicar","1961–1968",W+'Amphicar',[],"colour · restoration"),
  x("Argo","Argocat · Argo 6x6 · Argo 8x8","Skid-steer six- or eight-wheeled amphibious ATV from Ontario.","Argo","",W+'Argo_(ATV_manufacturer)',[v("Argo Avenger","Argo","","8x8"),v("Argo Conquest","Argo","","8x8"),v("Argo 8x8 750 HDi","Argo","","")],"6x6 or 8x8 · tracks · outboard"),
  x("Amphicat","Artés Gato Montés","Six-wheel-drive skid-steer amphibious ATV of the late 1960s.","","late 1960s–early 1970s",W+'Amphicat',[],""),
  x("Gibbs Aquada","Aquada","High-speed amphibious car with a 2.5 litre Rover V6.","Gibbs Sports Amphibians","2003–2004",W+'Gibbs_Aquada',[],""),
  x("Gibbs Quadski","Quadski","Amphibious quad that turns into a personal watercraft, 45 mph on land and water.","Gibbs Sports Amphibians","2012–",W+'Gibbs_Quadski',[],"")]}
def b(n,c,f,seg,d,sig,s,lines=None,rel=None): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines or [],"eras":[],"sig":sig,"sc":[],"rel":rel or [],"s":s}
brands=[
 b("Honda","Japan","1948","mass-market","Japanese maker of motorcycles, cars and power equipment; created the ATC three-wheeler.",["Honda ATC","Honda FourTrax (TRX)"],"knowledge",["ATC","FourTrax/TRX"]),
 b("Suzuki","Japan","1909","mass-market","Japanese maker of cars, motorcycles and ATVs.",["Suzuki QuadRacer LT250R"],"knowledge",["QuadRunner","QuadRacer"]),
 b("Yamaha Motor","Japan","1955","mass-market and performance","Japanese motorcycle, ATV and marine maker.",["Yamaha Banshee 350","Yamaha Blaster","Yamaha Raptor","Yamaha Grizzly","Yamaha Rhino"],W+'Yamaha_Motor_Company'),
 b("Kawasaki","Japan","","mass-market","Japanese maker of motorcycles, ATVs and utility vehicles.",["Kawasaki MULE"],W+'Kawasaki_Motors',["MULE"]),
 b("Polaris","United States","1954","powersports","Minnesota maker of snowmobiles, ATVs and side-by-sides, founded in Roseau.",["Polaris RZR","Polaris Indy","Polaris RMK","Polaris Sno Traveler"],W+'Polaris_Inc.',["Sportsman","Ranger","RZR","General","Indy","RMK"],["Arctic Cat"]),
 b("Can-Am","Canada","","powersports","BRP brand for ATVs, side-by-sides and three-wheelers.",["Can-Am Maverick","Can-Am Outlander and Renegade"],W+'Can-Am_Off-Road',["Outlander","Renegade","Maverick","Commander","Defender"],["Ski-Doo","Lynx"]),
 b("Ski-Doo","Canada","1959","snowmobiles","BRP snowmobile brand begun by Joseph-Armand Bombardier.",["Ski-Doo"],W+'Ski-Doo',["MXZ","Summit","Renegade","Expedition","Skandic","Tundra","Freeride"],["Lynx","Can-Am"]),
 b("Lynx","Finland","1968","snowmobiles","Finnish snowmobile brand, owned by BRP since 1988.",["Lynx"],W+'Lynx_(snowmobile)',[],["Ski-Doo"]),
 b("Arctic Cat","United States","1960","snowmobiles and ATVs","Minnesota snowmobile and ATV maker founded by Edgar Hetteen; Textron since 2017.",["Arctic Cat snowmobiles"],W+'Arctic_Cat',[],["Polaris"]),
 b("Meyers Manx","United States","1964","dune buggies","California maker of the original fibreglass Beetle-based dune buggy, revived in 2020.",["Meyers Manx"],W+'Meyers_Manx'),
 b("Funco Motorsports","United States","","sand cars","American maker of high-performance sand cars.",["Funco sand cars"],W+'Funco_Motorsports'),
 b("Club Car","United States","1958","golf cars","Golf car and utility vehicle maker of Evans, Georgia.",["Club Car DS","Club Car Precedent","Club Car Onward"],W+'Club_Car',["Onward","Tempo","Villager","Carryall"],["E-Z-GO"]),
 b("E-Z-GO","United States","1954","golf cars","Augusta-area golf car maker owned by Textron.",[],"knowledge",[],["Club Car"]),
 b("Tony Kart","Italy","1958","racing karts","Kart chassis brand of OTK Kart Group, Prevalle.",["Tony Kart"],W+'OTK_Kart_Group',["Kosmic","Exprit"],["CRG","Birel"]),
 b("CRG","Italy","","racing karts","Italian kart chassis maker, formerly Kalì Kart.",["CRG"],W+'CRG_(kart_manufacturer)',[],["Tony Kart"]),
 b("Birel","Italy","","karts","Lissone kart maker, formerly a bicycle maker.",["Birel"],W+'Birel',["Easykart"]),
 b("Volkswagen","Germany","1937","mass-market","German volume carmaker; its Beetle underpins dune buggies.",["Volkswagen Schwimmwagen"],"knowledge"),
 b("Amphicar","West Germany","","amphibious cars","Maker of the Amphicar 770, built at Lübeck and Berlin.",["Amphicar 770"],W+'Amphicar'),
 b("Gibbs Sports Amphibians","","","amphibious vehicles","Maker of high-speed amphibians.",["Gibbs Aquada","Gibbs Quadski"],W+'Gibbs_Aquada'),
 b("Argo","Canada","1962","amphibious ATVs","Ontario maker of six- and eight-wheeled amphibious ATVs, founded as Ontario Drive and Gear.",["Argo"],W+'Argo_(ATV_manufacturer)'),
]
notes=("Kept all six old kinds and added Amphibious vehicle. Trimmed Polaris skew: old Polaris Sportsman 500/450 duplicates cut to three Sportsman models; Ranger 500/600 cut; "
 "Funco SKU list (G52/GEN6, GT ANA, GTU, GTF) reduced to a Funco archetype with F9/FD9/GTX as versions (GTF/GTX old pair kept as GTX). "
 "Left out without a retrieved page: Polaris Sportsman, Ranger and General as archetypes (kept as m), E-Z-GO models (no page with models retrieved; brand from knowledge), "
 "Arctic Cat and Polaris Indy model detail beyond what pages state, Ski-Doo platforms (REV etc.), CRG/Birel chassis models, Argo first-6x6 year (only in search snippets). "
 "Polaris snowmobile history page returned 403; not retried.")
out={"kinds":[quad,sxs,buggy,sled,golf,kart,amph],"brands":brands,"traditions":[],"notes":notes}
p='work/G1/shelves/07_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('ok')
