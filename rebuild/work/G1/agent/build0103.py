import json, os
W='https://en.wikipedia.org/wiki/'
SEG=W+'Ninebot'; EUC=W+'Electric_unicycle'; SBS=W+'Self-balancing_scooter'; ESK=W+'Electric_skateboard'
EVO='https://www.rideevolve.com/'
def v(n,mk='',y='',d=''): return {k:val for k,val in dict(n=n,mk=mk,y=y,d=d).items() if val or k=='n'}
kinds=[
{"n":"Electric kick scooter","a":"e-scooter · electric scooter","d":"Stand-up scooter with an electric motor, made to carry a rider from place to place.",
 "t":["folding commuter","dual-motor performance","children's"],"s":"https://store.segway.com/ninebot-kickscooter-max-g30lp",
 "x":[
  {"n":"Autoped","a":"","d":"Early motorised stand-up scooter, built 1915–1921 and under licence by Krupp 1919–1922.","mk":"","y":"1915","s":W+'Motorized_scooter',
   "v":[v("Autoped",y="1915",d="original US production to 1921"),v("Krupp Autoped",mk="Krupp",y="1919",d="licence build to 1922")],"dt":"petrol engine on the front wheel"},
  {"n":"MyWay folding e-scooter","a":"Inokim","d":"Folding electric kick scooter designed by Nimrod Ricardo Sapir, made in Israel and later China.","mk":"Inokim","y":"2009–2010","s":W+'Motorized_scooter',
   "v":[v("MyWay",mk="Inokim",y="2009–2010",d="first brand name, made in Israel"),v("Inokim",mk="Inokim",y="2013",d="brand renamed; production moved to Ningbo")],"dt":"folding frame"},
  {"n":"Xiaomi M365","a":"Mi Electric Scooter","d":"Folding commuter scooter with front hub motor and 8.5-inch tyres; the template for early rental fleets such as Bird.","mk":"Xiaomi","y":"2016","s":W+'Xiaomi_M365',
   "v":[v("M365",mk="Xiaomi",y="2016",d="250 W motor, 30 km range, 12.5 kg"),v("M365 Pro",mk="Xiaomi",d="300 W motor, 45 km range, colour display, larger deck")],
   "dt":"8.5-inch pneumatic tyres · regenerative and disc brake · range 30–45 km"},
  {"n":"Ninebot KickScooter ES","a":"","d":"Segway-Ninebot's first-generation folding commuter scooter series.","mk":"Segway-Ninebot","y":"","s":SEG,
   "v":[v("ES1",mk="Segway-Ninebot"),v("ES2",mk="Segway-Ninebot"),v("ES4",mk="Segway-Ninebot")],"dt":"battery size · colour"},
  {"n":"Ninebot KickScooter Max","a":"Max G30","d":"Long-range folding commuter scooter series from Segway-Ninebot.","mk":"Segway-Ninebot","y":"","s":SEG,
   "v":[v("Max G30",mk="Segway-Ninebot"),v("Max G30P",mk="Segway-Ninebot"),v("Max G30LP",mk="Segway-Ninebot"),v("Max G2",mk="Segway-Ninebot"),v("Max G3",mk="Segway-Ninebot")],
   "dt":"battery size · regional speed limits"},
  {"n":"Ninebot KickScooter F","a":"","d":"Mid-range folding commuter scooter series from Segway-Ninebot.","mk":"Segway-Ninebot","y":"","s":SEG,
   "v":[v("F2 Pro",mk="Segway-Ninebot"),v("F2 II D",mk="Segway-Ninebot"),v("F3",mk="Segway-Ninebot")],"dt":"battery size · regional versions"},
  {"n":"Segway SuperScooter GT","a":"","d":"High-performance scooter series from Segway-Ninebot.","mk":"Segway-Ninebot","y":"","s":SEG,
   "v":[v("GT1",mk="Segway-Ninebot"),v("GT2",mk="Segway-Ninebot"),v("GT3",mk="Segway-Ninebot"),v("GT3 Pro",mk="Segway-Ninebot")],"dt":"motor power · suspension"}],
 "m":[["E2 Plus II","Segway-Ninebot"],["E3 Pro","Segway-Ninebot"],["ZT3 Pro","Segway-Ninebot"],["C2 Pro B","Segway-Ninebot"],["ZING A6","Segway-Ninebot"],["RS","InMotion"]]},
{"n":"Electric unicycle","a":"EUC · e-unicycle","d":"One-wheeled self-balancing electric vehicle ridden standing.",
 "t":["suspension","non-suspension","seated"],"s":"https://www.wilsonebikes.com/products/inmotion-v14-pro-electric-unicycle",
 "x":[
  {"n":"Solowheel","a":"","d":"Shane Chen's seatless self-balancing unicycle, the first widely sold electric unicycle.","mk":"Inventist","y":"2011","s":EUC,
   "v":[v("Solowheel",mk="Inventist",y="2011",d="launched February 2011; patent filed 2010")],"dt":""},
  {"n":"Ninebot One","a":"","d":"Segway-Ninebot's electric unicycle range for beginners and commuters.","mk":"Segway-Ninebot","y":"2017","s":SEG,
   "v":[v("One S1",mk="Segway-Ninebot",y="2017"),v("One S2",mk="Segway-Ninebot"),v("One E+",mk="Segway-Ninebot")],"dt":"battery size"},
  {"n":"Begode M-series","a":"Gotway Msuper","d":"Begode (formerly Gotway) performance wheel line that grew from the Msuper into the MSX, MSP and RS.","mk":"Begode","y":"","s":EUC,
   "v":[v("Msuper X",mk="Begode"),v("MSX",mk="Begode",y="2018",d="2000 W, 84 V, 18-inch"),v("MSP",mk="Begode"),v("RS",mk="Begode")],"dt":"voltage 84–100 V · battery Wh · 18-inch wheel"},
  {"n":"InMotion V11","a":"","d":"First electric unicycle with built-in air-spring pedal suspension.","mk":"InMotion","y":"2020","s":"https://www.designboom.com/technology/inmotion-v11-first-electric-unicycle-with-built-in-air-suspension-09-07-2020/",
   "v":[v("V11",mk="InMotion",y="2020",d="2200 W, 1500 Wh, 3-inch tyre"),v("V11Y",mk="InMotion")],"dt":"suspension travel · battery Wh"},
  {"n":"King Song 16X","a":"KS-16X","d":"16-inch high-capacity commuter wheel from King Song.","mk":"King Song","y":"","s":"https://kingsong.com/products/kingsong-16x",
   "v":[v("16X",mk="King Song",d="2200 W, 1554 Wh, 16-inch")],"dt":"16-inch tyre · battery Wh"},
  {"n":"Veteran Sherman","a":"","d":"Leaperkim's large-battery 18-inch road wheel series sold under the Veteran name.","mk":"Leaperkim","y":"","s":"https://freshlycharged.com/products/161/leaperkim-veteran-sherman-max",
   "v":[v("Sherman-S",mk="Leaperkim"),v("Sherman Max",mk="Leaperkim",y="2022",d="2800 W, 3600 Wh, 18-inch")],"dt":"battery Wh · suspension"}],
 "m":[["EX","Begode"],["Monster Pro","Begode"],["Mten3","Begode"],["V14 Pro","InMotion"],["V12 Pro","InMotion"],["S22 Pro","King Song"],["Patton S","Leaperkim"],["Aero","Nosfet"]]},
{"n":"Hoverboard","a":"self-balancing board · self-balancing scooter · Swegway","d":"Two-wheeled self-balancing electric board ridden standing.",
 "s":"https://www.hover-1.com/products/hover-1-titan-hoverboard",
 "x":[
  {"n":"Hovertrax","a":"","d":"Shane Chen's original self-balancing two-wheel board, launched on Kickstarter.","mk":"Inventist","y":"2013","s":SBS,
   "v":[v("Hovertrax",mk="Inventist",y="2013",d="Kickstarter May 2013; patent filed February 2013")],"dt":""},
  {"n":"Segway miniPRO","a":"","d":"Segway's smaller self-balancing scooter, among the first UL-certified boards.","mk":"Segway-Ninebot","y":"2016","s":W+'Segway_PT',
   "v":[v("miniPRO",mk="Segway-Ninebot",y="2016",d="UL certification May 2016")],"dt":""}],
 "m":[["Titan","Hover-1"]]},
{"n":"Self-balancing personal transporter","a":"Segway · gyropode","d":"Two-wheeled self-balancing vehicle ridden standing and steered by a handlebar.",
 "s":W+'Segway_PT',
 "x":[
  {"n":"Segway PT","a":"Segway HT","d":"Dean Kamen's self-balancing transporter, unveiled 2001 and built until 2020.","mk":"Segway-Ninebot","y":"2001","s":W+'Segway_PT',
   "v":[v("i167",mk="Segway-Ninebot",y="2002",d="first shipped model"),v("e167",mk="Segway-Ninebot",d="i167 with electric kickstand"),v("p133",mk="Segway-Ninebot",d="smaller, less powerful"),
        v("i180",mk="Segway-Ninebot",d="first with lithium-ion batteries"),v("XT",mk="Segway-Ninebot",d="first recreational model"),
        v("i2",mk="Segway-Ninebot",y="2006",d="on-road, LeanSteer"),v("x2",mk="Segway-Ninebot",y="2006",d="off-road, LeanSteer"),
        v("i2 SE / x2 SE",mk="Segway-Ninebot",y="2014",d="third generation")],"dt":"on-road or off-road tyres · battery type"}]},
{"n":"Powered skateboard","a":"electric skateboard · e-board · electric longboard","d":"Skateboard with an electric motor, made to carry a rider from place to place.",
 "t":["mini board","street (flexy) board","all-terrain (2-in-1) board","off-road mountainboard","racing board","folding board","one-wheel board","hub drive","direct drive","belt drive","gear drive"],
 "s":"https://www.evolveskateboards.com/",
 "x":[
  {"n":"Finkle wireless board","a":"","d":"Louie Finkle's wireless-remote electric board, often cited as the first modern electric skateboard.","mk":"","y":"1997","s":ESK,"v":[],"dt":""},
  {"n":"Boosted Board","a":"","d":"Flexible-deck dual-motor electric longboard that set the template for street e-boards.","mk":"Boosted","y":"2014","s":W+'Boosted_(company)',
   "v":[v("Single / Dual / Dual+",mk="Boosted",y="2014",d="first generation"),v("Dual / Dual+ (SR, XR)",mk="Boosted",y="2016",d="second generation"),
        v("Stealth",mk="Boosted",y="2018",d="third generation"),v("Plus",mk="Boosted",y="2018"),v("Mini X",mk="Boosted",y="2018"),v("Mini S",mk="Boosted",y="2018")],
   "dt":"deck length · battery SR/XR"},
  {"n":"Onewheel","a":"","d":"Self-balancing single-wheel board with a central hub-motor wheel, ridden sideways like a snowboard.","mk":"Future Motion","y":"2014","s":W+'Onewheel',
   "v":[v("Onewheel",mk="Future Motion",y="2014",d="original"),v("Onewheel+",mk="Future Motion",y="2017"),v("Onewheel+ XR",mk="Future Motion",y="2018"),
        v("Pint",mk="Future Motion",y="2019"),v("Pint X",mk="Future Motion",y="2021"),v("GT",mk="Future Motion",y="2021"),
        v("GT S-Series",mk="Future Motion",y="2023"),v("Pint S",mk="Future Motion",y="2024"),v("XR Classic",mk="Future Motion",y="2024"),v("Rally XL",mk="Future Motion",y="2025")],
   "dt":"board size · battery range · tyre"},
  {"n":"Evolve GTR","a":"","d":"Evolve's dual-motor belt-drive board sold in street and all-terrain set-ups.","mk":"Evolve Skateboards","y":"","s":EVO,
   "v":[v("GTR Bamboo Street",mk="Evolve Skateboards"),v("GTR Bamboo All Terrain",mk="Evolve Skateboards")],"dt":"street or all-terrain wheels · deck material"},
  {"n":"Evolve Diablo","a":"","d":"Evolve's top-range board in carbon or bamboo, street or all-terrain.","mk":"Evolve Skateboards","y":"","s":EVO,
   "v":[v("Diablo Carbon",mk="Evolve Skateboards"),v("Diablo Bamboo",mk="Evolve Skateboards"),v("Renegade Diablo",mk="Evolve Skateboards")],"dt":"carbon or bamboo deck · street or all-terrain wheels"}],
 "m":[["Fusion","Evolve Skateboards"],["Stoke X","Evolve Skateboards"],["Lonestar Supersport","LaCroix Boards"],["The Barrel","LaCroix Boards"]]}]
brands=[
 {"n":"Segway-Ninebot","c":"China","f":"1999","seg":"Personal electric vehicles","d":"Segway Inc., founded by Dean Kamen in the US, acquired by Beijing-based Ninebot in 2015.",
  "lines":["Segway PT","miniPRO","Ninebot KickScooter ES","Max","F","GT SuperScooter","Ninebot One","Ninebot Gokart"],"sig":["Segway PT","Ninebot KickScooter Max"],"rel":["Xiaomi"],"s":SEG},
 {"n":"Xiaomi","c":"China","f":"2010","seg":"Consumer electronics","d":"Chinese electronics maker whose Mi Electric Scooter range popularised the folding e-scooter.","lines":["Mi Electric Scooter"],"sig":["Xiaomi M365"],"rel":["Segway-Ninebot"],"s":"knowledge"},
 {"n":"Inokim","c":"Israel","f":"2009","seg":"Electric scooters","d":"Folding e-scooter brand begun as MyWay by Nimrod Ricardo Sapir, renamed Inokim in 2013.","sig":["MyWay folding e-scooter"],"s":W+'Motorized_scooter'},
 {"n":"Inventist","seg":"Personal electric vehicles","d":"Shane Chen's company behind the Solowheel and the Hovertrax.","sig":["Solowheel","Hovertrax"],"s":SBS},
 {"n":"Begode","c":"China","seg":"Electric unicycles","d":"Chinese performance electric-unicycle maker, formerly called Gotway.","sig":["Begode M-series"],"rel":["King Song","InMotion","Leaperkim"],"s":EUC},
 {"n":"King Song","c":"China","seg":"Electric unicycles","d":"Chinese electric-unicycle maker.","sig":["King Song 16X"],"rel":["Begode","InMotion","Leaperkim"],"s":EUC},
 {"n":"InMotion","c":"China","seg":"Electric unicycles and scooters","d":"Chinese maker of electric unicycles and scooters; pioneer of suspension wheels.","sig":["InMotion V11"],"rel":["Begode","King Song"],"s":EUC},
 {"n":"Leaperkim","c":"China","seg":"Electric unicycles","d":"Chinese electric-unicycle maker selling under the Veteran name.","lines":["Veteran"],"sig":["Veteran Sherman"],"rel":["Begode","King Song"],"s":EUC},
 {"n":"Boosted","c":"United States","f":"2012","seg":"Electric skateboards","d":"Palo Alto maker of electric skateboards and the Rev scooter; defunct in 2020, assets partly to Lime.","lines":["Boosted Board","Rev"],"sig":["Boosted Board"],"s":W+'Boosted_(company)'},
 {"n":"Future Motion","c":"United States","seg":"Electric boards","d":"Santa Cruz company founded by Kyle Doerksen, maker of the Onewheel.","lines":["Onewheel","Pint","GT","XR"],"sig":["Onewheel"],"s":W+'Onewheel'},
 {"n":"Evolve Skateboards","seg":"Electric skateboards","d":"Electric skateboard maker with bamboo and carbon street and all-terrain boards.","lines":["GTR","Diablo","Fusion","Stoke"],"sig":["Evolve GTR","Evolve Diablo"],"s":EVO}]
notes=("Kept all 4 planned kinds. Added NEW kind 'Self-balancing personal transporter' for the Segway PT (brief named it as an archetype but it is neither a hoverboard nor a kick scooter). "
 "Trimmed SKU lists: Segway-Ninebot scooter models folded into ES/Max/F/GT archetypes; dropped flat E2 Pro D, E3 D, F2 II D duplicates where not versions. "
 "EUC: dropped Begode Monster V3, Nikola, Tesla T3; InMotion E20, P6, V10F, V12S, V6, V8S, V9; Nosfet Xeno (SKU noise, ≤8 flat). "
 "Wikipedia API was rate-limited (429) so pages were fetched with WebFetch. Not added: Gotway/Begode founding year, King Song/InMotion founding years, Evolve country (no retrieved source); "
 "Dualtron, Unagi, Apollo, Swagtron and ZBoard archetypes left out for lack of a fetched source within budget. Hover-1, LaCroix and Nosfet have no register entries (no archetypes).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/G1/shelves/01_03.json'; os.makedirs('work/G1/shelves',exist_ok=True)
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('ok')
