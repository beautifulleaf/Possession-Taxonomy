import json, os
DI='https://en.wikipedia.org/wiki/DIANA_Mayer_%26_Grammelspacher'; WE='https://en.wikipedia.org/wiki/Weihrauch'
H35='https://en.wikipedia.org/wiki/Weihrauch_HW_35'; BSA='https://en.wikipedia.org/wiki/BSA_Meteor_Air_Rifle'
FWB='https://en.wikipedia.org/wiki/Feinwerkbau'; LGR='https://en.wikipedia.org/wiki/Walther_LGR'
C77='https://en.wikipedia.org/wiki/Crosman_1377'; D25='https://en.wikipedia.org/wiki/Daisy_Model_25'
DAI='https://en.wikipedia.org/wiki/Daisy_Outdoor_Products'; WEB='https://www.shootinguk.co.uk/shooting/the-history-of-webley-air-rifles/'
DAY='https://en.wikipedia.org/wiki/Daystate'; AA='https://www.gunmart.net/gun-reviews/airguns/air-rifles/air-arms-s510'
FX='https://www.bakerairguns.com/?p=167801'; AS='https://en.wikipedia.org/wiki/AEGs'
DM='Diana (Mayer & Grammelspacher)'
def v(n,mk,y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def x(n,mk,y,d,s,vs=(),dt="",a=""): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":list(vs),"dt":dt}
rifle_x=[
 x("Daisy Red Ryder","Daisy","","Lever-action spring-piston BB carbine with a smoothbore barrel, the classic American first gun.",DAI,dt="BB capacity · stock finish · youth or adult size"),
 x("Daisy Model 25","Daisy","1914","Pump-action BB gun modelled on a pump shotgun, designed by Charles F. Lefever.",D25,
   [v("No. 25 (original run)","Daisy","1914","made to 1978"),v("Model 25 revival","Daisy","","production restarted 2007 or 2009 (sources differ)")],"finish · markings · era",a="No. 25"),
 x("Diana Model 27","Diana (Mayer & Grammelspacher)","1910","Classic break-barrel spring-piston rifle, made in various forms for most of the 20th century.",DI,
   [v("Model 27",DM,"1910","made to 1987")],"calibre · trade name (Original, Beeman, Hy-Score, GECADO)"),
 x("Diana 34",DM,"","Break-barrel spring-piston sporting rifle in Diana's current range.",DI,dt="calibre · stock"),
 x("Webley Service Mk II","Webley & Scott","1932","Pre-war British air rifle with interchangeable barrels and a flip-up aperture rear sight.",WEB,
   [v("Mk1","Webley & Scott","1925","predecessor, about 1,500 made"),v("Mk2 Service, 1st–6th series","Webley & Scott","1932","made to 1947; about 16,300 in all")],
   "series · calibre .177, .22, .25 · sight position",a="Webley Mk2 Service"),
 x("Weihrauch HW 35","Weihrauch","1951","Break-barrel spring-piston rifle, Weihrauch's most successful model and first with the Rekord two-stage trigger.",H35,
   [v("HW 35 STD","Weihrauch","","beech stock"),v("HW 35L","Weihrauch","","walnut stock with cheek piece"),v("HW 35E (Export)","Weihrauch","","top of range, longer barrel"),
    v("HW 35LS","Weihrauch","1977","thumbhole stock"),v("HW 35 Safari","Weihrauch","1986"),v("HW 35 Vixen","Weihrauch","1979","UK tune by Norman May")],"calibre 4.5/5.5 mm · standard or carbine (K) · stock"),
 x("Weihrauch HW 80","Weihrauch","","Break-barrel spring-piston rifle, sold in North America as the Beeman R1.",WE,[v("Beeman R1","Weihrauch","","North American version")],"calibre · stock"),
 x("Weihrauch HW 77","Weihrauch","","Fixed-barrel underlever spring-piston rifle.",WE,[v("HW 77","Weihrauch"),v("HW 77 K","Weihrauch","","carbine")],"calibre · stock"),
 x("Weihrauch HW 97","Weihrauch","","Fixed-barrel underlever spring-piston rifle.",WE,[v("HW 97 K","Weihrauch")],"calibre · stock"),
 x("BSA Meteor","BSA Guns","1959","Break-barrel spring rifle, the first BSA air rifle made to take a telescopic sight.",BSA,
   [v("Meteor Mk.1","BSA Guns","1959"),v("Meteor Mk.2","BSA Guns","1962"),v("Meteor & Super Meteor Mk.3","BSA Guns","1967"),v("Meteor & Super Meteor Mk.4","BSA Guns","1974"),
    v("Meteor & Super Meteor Mk.5","BSA Guns","1979"),v("Meteor & Carbine Mk.6","BSA Guns","1993"),v("Mk7","BSA Guns","","made by Gamo")],"mark · calibre · standard or carbine"),
 x("Feinwerkbau 300","Feinwerkbau","","Recoilless side-lever spring-piston 10 m match rifle whose barrel and action slide on rails.",FWB,[v("300","Feinwerkbau"),v("300 S","Feinwerkbau")],"stock (standard, junior, universal) · sights"),
 x("Feinwerkbau 700","Feinwerkbau","","Pre-charged pneumatic 10 m match rifle.",FWB,[v("P700","Feinwerkbau")],"stock · cylinder · sights",a="P700"),
 x("Walther LG match air rifle","Walther","1972","Walther's line of 10 m match air rifles, begun with the single-stroke pneumatic LGR.",LGR,
   [v("LGR","Walther","1972","single-stroke pneumatic, to 1989"),v("LGR Match","Walther","","walnut stock"),v("LGR Match Universal","Walther","","adjustable cheekpiece"),v("LG90","Walther","","successor to the LGR"),v("LG300","Walther"),v("LG400","Walther")],"stock · power system",a="LGR"),
 x("Daystate Huntsman","Daystate","1980","Pre-charged pneumatic sporting rifle first built for Rentokil pest control.",DAY,dt="calibre · stock"),
 x("Air Arms S400","Air Arms","","Pre-charged pneumatic sporting rifle whose action also underlies the S510.",AA,[v("S410","Air Arms","","multi-shot"),v("S510","Air Arms","","side-lever, built on the S400 action")],"single or multi-shot · rifle or carbine · stock"),
 x("FX Impact","FX Airguns","","Regulated pre-charged pneumatic rifle platform.",FX,[v("Impact","FX Airguns","","original platform"),v("Impact M3","FX Airguns","2021")],"calibre · barrel length · finish"),
]
kinds=[
{"n":"Air rifle","a":"pellet rifle · BB gun","d":"Rifle-format air gun that fires pellets or BBs with compressed air or gas.",
 "t":["spring-piston (break-barrel, underlever, side-lever)","gas ram","pre-charged pneumatic (PCP)","multi-pump pneumatic","single-stroke pneumatic","CO2","BB gun","10 m match"],"s":"",
 "x":rifle_x,
 "m":[["Diana Outlaw Gen2 Synthetic",DM],["Diana Stormrider Sport",DM],["Gamo Urban","Gamo"],["Gamo Arrow SLT","Gamo"],["Umarex Gauntlet 2 SL","Umarex"],["Benjamin Armada Semi-Auto","Benjamin"],
      ["Air Venturi Avenge-XL","Air Venturi"],["Webley & Scott Nemesis X","Webley & Scott"],["Reximex Apex","Reximex"],["Norica NTX 35","Norica"],["SIG Sauer MPX PCC","Sig Sauer"],["Barra 270z","Barra Airguns"]]},
{"n":"Air pistol","a":"pellet pistol","d":"Handgun-format air gun that fires pellets or BBs with compressed air or gas.",
 "t":["CO2","pre-charged pneumatic (PCP)","multi-pump pneumatic","spring-piston","single-stroke pneumatic","10 m match"],"s":"",
 "x":[x("Crosman 1377","Crosman","1977","Single-shot bolt-action multi-pump pneumatic .177 pistol, made continuously since 1977.",C77,
   [v("Phase I","Crosman","1977","steel breech"),v("Phase II","Crosman","1981","plastic breech, pellets or BBs"),v("Phase III","Crosman","1999","pellets only"),v("1322","Crosman","","variant"),v("PC77 Pumpmaster 77","Crosman","","budget version")],"breech · stock 1399 · finish",a="American Classic")],
 "m":[["Crosman 2240","Crosman"],["Weihrauch HW44","Weihrauch"],["Benjamin Marauder Pistol","Benjamin"],["Hammerli AP20","Hammerli"],["Air Venturi Comp10 Match","Air Venturi"],["Umarex Steel Storm","Umarex"],
      ["Colt Defender","Umarex"],["Crosman SNR357","Crosman"],["Hatsan Jet II","Hatsan"],["Beeman 2027","Beeman"],["AirForce TalonP","AirForce Airguns"],["Reximex RP11","Reximex"],["Diana Bandit",DM],["Crosman Silhouette","Crosman"]],
 "r":[["Marauder","Benjamin"]]},
{"n":"Airsoft gun","a":"airsoft replica · AEG","d":"Replica gun that fires 6 mm plastic pellets for airsoft games and training; see also the airsoft scene in Sports.",
 "t":["spring","electric (AEG)","gas non-blowback","gas blowback (GBB)","high-pressure air (HPA)"],"s":AS,
 "x":[x("Tokyo Marui AEG","Tokyo Marui","","Battery-powered automatic electric gun built around the gearbox that Tokyo Marui originated.",AS,[v("Glock 18C electric pistol","Tokyo Marui","2005","automatic electric pistol")],"gearbox version · replica model · battery")]},
{"n":"Air-gun pellets","a":"","d":"Lead or alloy projectile made for air guns.","t":["diabolo","wadcutter (match)","pointed","hollow point","domed","slug"],
 "s":"https://www.pyramydair.com/ammo/pellets",
 "m":[["JSB Exact","JSB"],["RWS R-10 Match Heavy","RWS"],["H&N Hornet","H&N"],["FX Atomic","FX Airguns"],["JSB Hades","JSB"],["AEA Precision Center Punch Diabolo","AEA Precision"],["JTS Dead Center Precision","JTS Airguns"]]},
{"n":"Air-gun BBs","a":"BBs · steel BBs","d":"Round BBs for BB guns.","t":["steel","copper-plated steel","lead"],"s":"https://www.airgundepot.com/airgunbbs.html"},
{"n":"CO2 capsule","a":"CO2 cartridge · powerlet","d":"Sealed carbon dioxide cartridge that powers CO2 air guns and launchers.","t":["8 g","12 g","88 g"],
 "s":"https://www.blackovis.com/byrna-hd-xl-pepper-self-defense-weapon-kit-2020"},
]
K='knowledge'
def b(n,c,f,seg,kf,d,s=K):
    o={"n":n,"c":c,"seg":seg,"kf":kf,"d":d,"s":s}
    if f: o["f"]=f
    return o
brands=[
b("Daisy","United States","1882","Mainstream","BB guns","Arkansas maker of BB guns, founded in Plymouth, Michigan, as a windmill company.",DAI),
b(DM,"Germany","1890","Heritage manufactory","air rifles","Rastatt maker of spring-piston air rifles and pistols, sold under several trade names.",DI),
b("Weihrauch","Germany","1899","Heritage manufactory","spring air rifles","German maker of HW air rifles, sold in North America under the Beeman name.",WE),
b("BSA Guns","United Kingdom","","Mainstream","air rifles","Birmingham air rifle maker, now owned by Gamo."),
b("Webley & Scott","United Kingdom","","Heritage manufactory","air guns","Historic British gun maker known for air pistols and rifles."),
b("Crosman","United States","1923","Mainstream","CO2 and pump air guns","New York maker of pump and CO2 air guns."),
b("Feinwerkbau","Germany","1949","Professional & flagship","match air guns","Oberndorf maker of ISSF match air rifles and pistols.",FWB),
b("Walther","Germany","1886","Professional & flagship","match guns","German maker of pistols and match air rifles."),
b("Daystate","United Kingdom","1978","Premium","PCP air rifles","Staffordshire maker of pre-charged pneumatic rifles.",DAY),
b("Air Arms","United Kingdom","","Premium","PCP air rifles","Sussex maker of PCP and spring air rifles.",AA),
b("FX Airguns","Sweden","","Premium","PCP air rifles","Swedish maker of regulated PCP air rifles and pellets."),
b("Tokyo Marui","Japan","","Mainstream","airsoft","Japanese airsoft maker credited with the original AEG gearbox."),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Air rifle and air pistol keep power sources as types and gain archetypes (Red Ryder, Daisy 25, Diana 27/34, Webley Service, HW 35/80/77/97, BSA Meteor, FWB 300/700, Walther LG, Daystate Huntsman, Air Arms S400, FX Impact; Crosman 1377). Red Ryder year left blank: Daisy Wikipedia says 1940, other sources say 1938. Air rifle models trimmed 20->12 (dropped JTS AirStryke, Macavity MA1/MA8, RTI Mora II, Umarex Komplete/Notos, Diana Bandit Tactical, Air Venturi Alpha); air pistol 23->14. Crosman 2240 kept as a model (no retrieved page). New kind Airsoft gun (cross-link to Sports airsoft). Pellet maker 'FX' normalised to 'FX Airguns'."}
p='work/E4/shelves/05_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
