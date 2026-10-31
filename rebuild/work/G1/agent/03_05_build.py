import json, os
W='https://en.wikipedia.org/wiki/'
CP='https://cycling-passion.com/dura-ace-history'
CAM=W+'Campagnolo'; SR=W+'SRAM_Corporation'; RS=W+'RockShox'; FX=W+'Fox_Factory'; ZP=W+'Zipp'
def V(n,mk,y,d): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Frameset","a":"frame and fork · frame","d":"A bicycle frame sold with its matching fork, sometimes with headset and seatpost, as the base of a custom build.",
 "t":["steel","aluminium","titanium","carbon fibre","bamboo","road","gravel","mountain","track"],"s":W+"Bicycle_frame",
 "x":[
  {"n":"Look KG86","a":"KG 86","d":"Look's carbon-and-Kevlar road frame, the company's first carbon frame, ridden to the 1986 Tour de France win.","mk":"Look","y":"1986","s":W+"Look_(company)",
   "v":[V("KG86","Look","1986","Carbon and Kevlar tubes; Greg LeMond's 1986 Tour win"),V("KG196","Look","1990","Look's first monocoque carbon frame")],"dt":"carbon/Kevlar · lugged then monocoque · size"},
  {"n":"Reynolds 531 frame","a":"531 tubing","d":"Frame built from Reynolds 531 manganese-molybdenum steel tubing, one of the most successful classic frame steels.","mk":"Reynolds","y":"","s":W+"Bicycle_frame",
   "v":[],"dt":"lugged or fillet-brazed steel · builder · size · paint"}]},
{"n":"Groupset","a":"gruppo · groupo · drivetrain group","d":"A maker's matched set of shifters, brakes, derailleurs, crankset, chain and cassette.",
 "t":["mechanical","electronic wired","electronic wireless","1x","2x","road","gravel","mountain","rim brake","hydraulic disc"],"s":W+"Groupset",
 "x":[
  {"n":"Shimano Dura-Ace","a":"Dura Ace","d":"Shimano's top road groupset since 1973, named after duralumin; introduced index shifting, STI levers and Di2.","mk":"Shimano","y":"1973","s":CP,
   "v":[V("Dura-Ace (first)","Shimano","1973","First aluminium pro-level road group"),V("Dura-Ace 10","Shimano","1976","Track group with 10 mm chain pitch"),
        V("7100","Shimano","1977","Second generation"),V("EX 7200","Shimano","1978","6-speed, new freehubs"),V("AX 7300","Shimano","1980","Aerodynamic design"),
        V("7400 SIS","Shimano","1984","Shimano Indexed Shifting"),V("7400 STI","Shimano","1990","Shift levers built into brake levers"),
        V("7700","Shimano","1996","9-speed"),V("7800","Shimano","2004","10-speed, Hollowtech II cranks"),V("7900","Shimano","2008","Hidden shift cables"),
        V("Di2 7970","Shimano","2009","Electronic shifting"),V("9000","Shimano","2012","11-speed, four-arm crankset"),
        V("R9100/R9150","Shimano","2016","Power meter option, hydraulic disc brakes"),V("R9200","Shimano","2021","12-speed, wireless shifters, electronic only")],
   "dt":"speeds 5–12 · mechanical/Di2 · rim/disc brake · crank length and gearing"},
  {"n":"Campagnolo Record","a":"Nuovo Record · C-Record","d":"Campagnolo's long-running road line, from the 1963 Record rear derailleur to complete 12-speed groupsets.","mk":"Campagnolo","y":"1963","s":CAM,
   "v":[V("Record rear derailleur","Campagnolo","1963","Original Record derailleur"),V("Nuovo Record rear derailleur","Campagnolo","1966","Parallelogram successor"),
        V("C-Record","Campagnolo","1986","Redesigned road and track groupsets"),V("Record 12-speed","Campagnolo","2018","12-speed")],
   "dt":"speeds · mechanical/EPS · rim/disc · polished or carbon finish"},
  {"n":"Campagnolo Super Record","a":"SR","d":"Campagnolo's top road groupset, launched for road and track in 1973 and revived as the flagship line.","mk":"Campagnolo","y":"1973","s":CAM,
   "v":[V("Super Record","Campagnolo","1973","Road and track groups"),V("Super Record RS","Campagnolo","2014",""),V("Super Record EPS 12-speed","Campagnolo","2019","Electronic"),
        V("Super Record Wireless","Campagnolo","2023","Wireless electronic"),V("Super Record 13-speed","Campagnolo","2025","13-speed")],
   "dt":"speeds · mechanical/EPS/wireless · carbon and titanium parts"},
  {"n":"SRAM Red","a":"Red eTap · Red AXS","d":"SRAM's top road groupset, which brought wireless electronic shifting to road bikes.","mk":"SRAM","y":"2007","s":SR,
   "v":[V("Red 10-speed","SRAM","2007","Mechanical"),V("Red eTap","SRAM","2015","Wireless electronic"),V("Red eTap AXS","SRAM","2019","12-speed wireless")],
   "dt":"mechanical/eTap/AXS · 1x or 2x · rim/disc"},
  {"n":"SRAM Eagle","a":"XX1 Eagle · X01 Eagle · GX Eagle","d":"SRAM's single-chainring 12-speed mountain-bike drivetrain family.","mk":"SRAM","y":"2016","s":SR,
   "v":[V("XX1 (1x11)","SRAM","2012","Wide-range 1x11 predecessor"),V("Eagle 1x12","SRAM","2016","12-speed launch"),V("GX Eagle","SRAM","2017","Lower-priced version"),
        V("XX1 / X01 Eagle AXS","SRAM","2019","Wireless electronic")],"dt":"tier XX/X0/GX/NX · mechanical/AXS · cassette range"},
  {"n":"Campagnolo Ekar","a":"","d":"Campagnolo's 13-speed single-chainring groupset for gravel riding.","mk":"Campagnolo","y":"2020","s":CAM,"v":[],"dt":"13-speed · 1x · cassette range"}],
 "m":[["Force","SRAM"],["Apex","SRAM"],["Chorus","Campagnolo"],["Potenza","Campagnolo"],["Veloce","Campagnolo"],["Claris","Shimano"]]},
{"n":"Wheelset","a":"wheels · wheel pair","d":"A matched front and rear bicycle wheel, usually bought ready-built as an upgrade.",
 "t":["rim brake","disc brake","clincher","tubular","tubeless-ready","deep-section aero","disc wheel","carbon","aluminium","handbuilt"],"s":W+"Bicycle_wheel",
 "x":[
  {"n":"Mavic Ksyrium","a":"","d":"Mavic's factory-built road wheelset with bladed Zicral spokes threaded into undrilled rims; a benchmark all-round wheel.","mk":"Mavic","y":"1999","s":"https://road.cc/content/feature/224256-design-classic-mavic-ksyrium-wheels",
   "v":[V("Ksyrium","Mavic","1999","Fore rims, Maxtal hubs, bladed Zicral spokes")],"dt":"aluminium or carbon rim · rim/disc brake · range level"},
  {"n":"Zipp disc wheel","a":"Sub9 · Super-9","d":"Zipp's carbon-fibre solid rear disc wheel for time trials and triathlon.","mk":"Zipp","y":"1988","s":ZP,
   "v":[V("First carbon disc","Zipp","1988",""),V("Sub9","Zipp","2008",""),V("Super-9","Zipp","2010",""),V("Super-9 disc clincher","Zipp","2013","Clincher rear wheel")],"dt":"tubular/clincher · rim/disc brake"},
  {"n":"Zipp 808","a":"808 NSW","d":"Zipp's extra-deep 82 mm carbon aero wheel.","mk":"Zipp","y":"2005","s":ZP,
   "v":[V("808","Zipp","2005","82 mm deep"),V("808 track","Zipp","2007",""),V("808 Firecrest clincher","Zipp","2011","Firecrest rim shape"),V("808 NSW","Zipp","2015","Launched at Kona")],"dt":"tubular/clincher · rim/disc"},
  {"n":"Zipp 404","a":"404 Firecrest · 404 Firestrike","d":"Zipp's mid-depth carbon aero road wheel, its most popular model.","mk":"Zipp","y":"","s":ZP,
   "v":[V("404 Firecrest carbon clincher","Zipp","2011",""),V("404 Firestrike","Zipp","2014","Limited edition")],"dt":"tubular/clincher · rim/disc"},
  {"n":"Zipp 303","a":"303 Firecrest","d":"Zipp's shallower all-round carbon wheel.","mk":"Zipp","y":"2010","s":ZP,
   "v":[V("303 redesign","Zipp","2010",""),V("303 Firecrest clincher","Zipp","2011",""),V("303 Firecrest tubular","Zipp","2012",""),V("303 disc brake","Zipp","2013","")],"dt":"tubular/clincher · rim/disc"}],
 "m":[["RRC1250","DT Swiss"]]},
{"n":"Suspension fork","a":"sus fork · front suspension","d":"A front fork with a spring and damper in telescoping legs, mainly for mountain bikes.",
 "t":["single-crown","dual-crown","air spring","coil spring","linkage","single-sided","26 in","27.5 in","29 in"],"s":W+"Bicycle_fork",
 "x":[
  {"n":"RockShox RS-1","a":"","d":"RockShox's first production suspension fork.","mk":"RockShox","y":"1990","s":RS,"v":[V("RS-1","RockShox","1990","First 100 made August 1990; discontinued 1991")],"dt":"travel · steerer"},
  {"n":"RockShox SID","a":"","d":"RockShox's lightweight cross-country fork.","mk":"RockShox","y":"1998","s":RS,"v":[V("SID","RockShox","1998",""),V("SID (current generation)","RockShox","2021","")],"dt":"travel · wheel size · damper"},
  {"n":"RockShox Pike","a":"","d":"RockShox's trail fork with 140–160 mm travel.","mk":"RockShox","y":"2004","s":RS,"v":[],"dt":"140/150/160 mm · wheel size · damper"},
  {"n":"Fox 36","a":"Fox Float 36","d":"Fox's 150–160 mm single-crown fork for trail and enduro riding.","mk":"Fox Factory","y":"","s":FX,"v":[],"dt":"150–160 mm · wheel size · damper"},
  {"n":"RockShox Boxxer","a":"BoXXer","d":"RockShox's dual-crown downhill fork.","mk":"RockShox","y":"1998","s":RS,"v":[],"dt":"180/200 mm · air/coil"},
  {"n":"Fox 40","a":"","d":"Fox's 203 mm dual-crown downhill fork.","mk":"Fox Factory","y":"","s":FX,"v":[],"dt":"203 mm · wheel size"},
  {"n":"Cannondale Lefty","a":"","d":"Cannondale's single-legged fork on needle bearings, needing a special Lefty hub.","mk":"Cannondale","y":"","s":W+"Bicycle_fork","v":[],"dt":"conventional/inverted · travel"}],
 "m":[["Judy","RockShox"],["Reba","RockShox"],["Lyrik","RockShox"],["Zeb","RockShox"],["32","Fox Factory"],["34","Fox Factory"],["38","Fox Factory"]]},
{"n":"Bicycle saddle","a":"bike seat · saddle","d":"The seat of a bicycle, fitted to the seatpost; one of the rider's contact points.",
 "t":["leather","padded","racing","comfort","sprung","noseless","cutaway","women-specific","banana seat"],"s":W+"Bicycle_saddle",
 "x":[
  {"n":"Brooks B17","a":"","d":"Brooks' tensioned vegetable-tanned leather saddle on steel rails that moulds to the rider, its best-seller for over a century.","mk":"Brooks England","y":"","s":"https://www.brooksengland.com/en_eu/b17.html",
   "v":[],"dt":"275 × 175 mm · 520 g · leather colours black, honey, brown, racing green"},
  {"n":"Selle Italia Turbo","a":"","d":"Classic padded road saddle from Selle Italia.","mk":"Selle Italia","y":"","s":W+"Bicycle_saddle","v":[],"dt":"colour · shell"}],
 "m":[["Team Pro","Brooks England"],["Swift","Brooks England"],["Swallow","Brooks England"]]},
{"n":"Bicycle pedals","a":"pedals · clipless pedals · flats","d":"The foot platforms turning the cranks, either flat or clipless with a shoe cleat.",
 "t":["flat/platform","toe clip and strap","clipless road (3-bolt)","clipless mountain (2-bolt)","double-sided entry","fixed or floating cleat"],"s":W+"Bicycle_pedal",
 "x":[
  {"n":"Cinelli M71","a":"","d":"Early clipless pedal using a plastic cleat and a release lever.","mk":"Cinelli","y":"1971","s":W+"Bicycle_pedal","v":[],"dt":""},
  {"n":"Look clipless pedal","a":"PP65 · Delta · Kéo","d":"Look's ski-binding-style road pedal, the first widely used clipless system.","mk":"Look","y":"1984","s":W+"Look_(company)",
   "v":[V("PP65","Look","1984","Hinault's 1985 Tour win"),V("Kéo","Look","2004","Lighter system; Kéo Easy has fixed 4.5° float")],"dt":"cleat float 0°/4.5°/9° · axle"},
  {"n":"Shimano SPD","a":"Shimano Pedaling Dynamics","d":"Shimano's two-bolt mountain clipless system with a cleat recessed in the sole for walking.","mk":"Shimano","y":"1990","s":W+"Shimano_Pedaling_Dynamics",
   "v":[V("PD-M737","Shimano","1990","First SPD pedal, with M100 shoe")],"dt":"cleat SH51 single-release / SH56 multi-release"},
  {"n":"Shimano SPD-SL","a":"","d":"Shimano's three-bolt road clipless system with a large cleat.","mk":"Shimano","y":"","s":W+"Shimano_Pedaling_Dynamics","v":[],"dt":"cleat float red 0°, blue 2°, yellow 6°"},
  {"n":"Speedplay","a":"lollipop pedal · Speedplay X · Zero","d":"Double-sided road clipless pedal with adjustable float up to 15°.","mk":"Speedplay","y":"1989","s":W+"Speedplay_(bicycle_pedal)",
   "v":[V("X","Speedplay","1989","Patented by Richard Byrne"),V("Wahoo redesign","Speedplay","2021","Sealed bearings")],"dt":"float · axle material"},
  {"n":"Crankbrothers Eggbeater","a":"","d":"Minimal four-sided mountain clipless pedal with six-degree float.","mk":"Crankbrothers","y":"","s":W+"Bicycle_pedal","v":[],"dt":""}],
 "m":[["Time pedals","Time"]]},
{"n":"Bicycle tyre","a":"bike tire · tyre","d":"The rubber tyre on a bicycle rim, as clincher, tubular or tubeless.",
 "t":["clincher","tubular","tubeless","studded","puncture-resistant","airless","width"],"s":W+"Bicycle_tire",
 "x":[
  {"n":"Continental Grand Prix 5000","a":"GP5000 · GP 5000 TL","d":"Continental's road racing tyre with Black Chili compound and Vectran puncture layer, successor to the GP4000.","mk":"Continental","y":"","s":"https://bikeradar.com/reviews/components/tyres/road-bike-tyres/continental-grand-prix-5000-clincher-tyre-review",
   "v":[V("GP4000","Continental","","Predecessor"),V("GP5000 clincher","Continental",""," "),V("GP5000 TL","Continental","","Tubeless")],"dt":"25/28 mm · clincher/tubeless"},
  {"n":"Schwalbe Marathon","a":"Marathon Plus","d":"Schwalbe's long-wearing touring and commuting tyre series.","mk":"Schwalbe","y":"","s":"https://schwalbetires.com/technology-faq/history",
   "v":[{"n":"Marathon Plus","mk":"Schwalbe","y":"","d":"5 mm SmartGuard puncture layer"}],"dt":"26 in–700c · width · reflective sidewall"}],
 "m":[["Stelvio Evolution","Schwalbe"],["Serenity","Hutchinson"],["C Elite","Tufo"],["Big Fat Larry","Surly"]]},
{"n":"Headset","a":"steering bearings","d":"The bearing set that lets the fork turn inside the frame's head tube.",
 "t":["threaded","threadless","integrated","semi-integrated","tapered","1 in","1 1/8 in"],"s":W+"Headset_(bicycle_part)",
 "x":[
  {"n":"Chris King NoThreadSet","a":"","d":"Chris King's modular threadless headset with sealed stainless bearings, an early threadless design.","mk":"Chris King","y":"1976","s":"https://condorcycles.com/en-us/products/chris-king-nothreadset-headset",
   "v":[],"dt":"1 in / 1 1/8 in · aluminium cups · colours"},
  {"n":"Aheadset","a":"threadless headset","d":"Threadless headset held by the stem clamp, patented and trademarked by Dia-Compe, now Cane Creek.","mk":"Cane Creek","y":"","s":W+"Headset_(bicycle_part)","v":[],"dt":""}],
 "m":[["InSet","Chris King"],["ZeroStack","Cane Creek"]]},
]
# fix stray blank
for k in kinds:
    for x in k.get('x',[]):
        for v in x['v']:
            v['d']=v['d'].strip()
            for f in ('y','d'):
                if not v[f]: del v[f]
        if not x.get('y'): x.pop('y',None)
        if not x.get('dt'): x.pop('dt',None)
        if not x.get('a'): x.pop('a',None)
B=lambda **k:{kk:v for kk,v in k.items() if v}
brands=[
 B(n="Shimano",c="Japan",f="1921",seg="Components",d="Japanese maker of bicycle components, from Dura-Ace groupsets to SPD pedals.",lines=["Dura-Ace","SPD","SPD-SL","Claris"],sig=["Shimano Dura-Ace","Shimano SPD"],s="knowledge"),
 B(n="Campagnolo",c="Italy",f="1933",seg="Components",d="Vicenza maker of road groupsets founded by Tullio Campagnolo.",lines=["Super Record","Record","Chorus","Potenza","Centaur","Ekar"],sig=["Campagnolo Super Record","Campagnolo Record"],s=CAM),
 B(n="SRAM",c="United States",f="1987",seg="Components",d="Chicago component group owning RockShox and Zipp; makes Red road and Eagle mountain groupsets.",lines=["Red","Force","Rival","Apex","Eagle","AXS"],sig=["SRAM Red","SRAM Eagle"],rel=["RockShox","Zipp"],s=SR),
 B(n="Mavic",c="France",f="1889",seg="Wheels and rims",d="French wheel and rim maker, behind the first aluminium rim (1934) and the Ksyrium.",sig=["Mavic Ksyrium"],s=W+"Mavic_(bicycle_parts_company)"),
 B(n="Zipp",c="United States",f="1988",seg="Wheels",d="Indianapolis maker of carbon aero wheels, part of SRAM since 2007.",lines=["303","404","808","NSW"],sig=["Zipp 404","Zipp 808","Zipp disc wheel"],rel=["SRAM"],s=ZP),
 B(n="DT Swiss",c="Switzerland",f="1994",seg="Wheels, hubs and spokes",d="Biel maker of spokes, Star Ratchet hubs and wheelsets.",s="https://www.merlincycles.com/blog/brand-focus-dt-swiss/"),
 B(n="RockShox",c="United States",f="1989",seg="Suspension",d="Suspension maker founded by Paul Turner, owned by SRAM since 2002.",lines=["SID","Pike","Lyrik","Boxxer","Zeb"],sig=["RockShox RS-1","RockShox SID","RockShox Pike"],rel=["SRAM"],s=RS),
 B(n="Fox Factory",c="United States",f="1977",seg="Suspension",d="American suspension maker whose 32–40 forks span cross-country to downhill.",lines=["32","34","36","38","40"],sig=["Fox 36","Fox 40"],s=FX),
 B(n="Cannondale",c="United States",seg="Bicycles",d="American bicycle maker known for the single-legged Lefty fork.",sig=["Cannondale Lefty"],s="knowledge"),
 B(n="Brooks England",c="United Kingdom",f="1866",seg="Saddles",d="Birmingham-founded maker of leather saddles, made in Smethwick.",sig=["Brooks B17"],s=W+"Brooks_England"),
 B(n="Selle Italia",c="Italy",seg="Saddles",d="Italian saddle maker.",sig=["Selle Italia Turbo"],s="knowledge"),
 B(n="Look",c="France",f="1951",seg="Pedals and frames",d="Nevers firm that brought ski-binding pedals to cycling in 1984.",lines=["Kéo"],sig=["Look clipless pedal","Look KG86"],s=W+"Look_(company)"),
 B(n="Cinelli",c="Italy",seg="Components and frames",d="Italian maker of the M71 clipless pedal.",sig=["Cinelli M71"],s="knowledge"),
 B(n="Speedplay",c="United States",f="1991",seg="Pedals",d="San Diego pedal maker, owned by Wahoo Fitness since 2019.",sig=["Speedplay"],s=W+"Speedplay_(bicycle_pedal)"),
 B(n="Crankbrothers",c="United States",seg="Pedals",d="American maker of Eggbeater mountain pedals.",sig=["Crankbrothers Eggbeater"],s="knowledge"),
 B(n="Continental",c="Germany",seg="Tyres",d="German tyre maker whose Grand Prix line is a road-racing standard.",sig=["Continental Grand Prix 5000"],s="knowledge"),
 B(n="Schwalbe",c="Germany",f="1973",seg="Tyres",d="Bicycle-tyre brand of Ralf Bohle GmbH, named after the 'Swallow' tyres it first imported.",lines=["Marathon"],sig=["Schwalbe Marathon"],s="https://schwalbetires.com/technology-faq/history"),
 B(n="Chris King",c="United States",seg="Headsets and hubs",d="American maker of NoThreadSet headsets and hubs.",lines=["NoThreadSet","InSet"],sig=["Chris King NoThreadSet"],s="https://condorcycles.com/en-us/products/chris-king-nothreadset-headset"),
 B(n="Cane Creek",c="United States",seg="Headsets and suspension",d="Holder of the threadless-headset patent and the Aheadset trademark.",lines=["ZeroStack"],sig=["Aheadset"],s=W+"Headset_(bicycle_part)"),
 B(n="Reynolds",c="United Kingdom",seg="Frame tubing",d="British maker of steel bicycle tubing, famed for 531.",sig=["Reynolds 531 frame"],s=W+"Bicycle_frame"),
]
notes=("No old kinds on this shelf; all 8 kinds are new. Left out (no retrieved confirmation): Brooks B17 launch year and variant years, DT Swiss 240 hub and wheel lines, "
 "Mavic Cosmic/Helium years and later Ksyrium versions, Fox 36 launch year, GP5000 launch year, Marathon launch year, Columbus tubing models, Shimano XTR/Ultegra/105 tiers. "
 "Shimano's own history page blocked (403); Dura-Ace history taken from cycling-passion.com.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/G1/shelves/03_05.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(sum(len(k.get('x',[])) for k in kinds),'archetypes',len(brands),'brands')
