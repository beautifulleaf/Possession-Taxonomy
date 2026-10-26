import json, os
TW="https://www.turtlewax.com/pages/our-story"; COL="https://www.collinite.com/"; FM="https://www.fordmuscle.com/news/get-spotless-shine-with-meguiars-new-carnauba-plus-quik-wax/"
GT="https://www.corvetteblogger.com/2023/07/14/crystal-serum-ultra-from-gtechniq-provides-the-ultimate-ceramic-protection-for-up-to-nine-years/"
GY="https://gyeon.co/q2-collection"; MZ="https://www.nonpaints.com/en/menzerna-400-heavy-cut-compound"; RU="https://www.rupes.com/"
FX="https://www.flexpowertools.com/forced-rotation-polisher-392715"; PC="https://www.gtplanet.net/forum/threads/auto-detailing-porter-cable-7424-6-variable-speed-random-orbit-polisher.95183"
LC="https://www.thedetailingmafia.com/lake-country-manufacturing"; CC="https://www.covercraft.com/"; JS="https://autogeekonline.net/goto/post?id=1545619"
def v(n,mk,y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Car wax","a":"carnauba wax · paste wax · liquid wax · spray wax","d":"Wax applied over car paint for gloss and short-term protection, traditionally based on carnauba.",
 "t":["paste","liquid","spray","cleaner wax (all-in-one)","natural carnauba","hybrid carnauba-polymer","colour-matched"],
 "s":"https://en.wikipedia.org/wiki/Carnauba_wax",
 "x":[
  {"n":"Turtle Wax","a":"Plastone","d":"The original American bottled car polish, renamed Turtle Wax for its hard-shell finish.","mk":"Turtle Wax","y":"1944–","s":TW,
   "v":[v("Plastone","Turtle Wax","1944","first premium car polish, made in Chicago"),v("Turtle Wax","Turtle Wax","1946","renamed; first bottled car wax"),
        v("Spray Car Wax","Turtle Wax","1963","award-winning packaging"),v("Minute Wax","Turtle Wax","1982","first spray wax"),
        v("Color Magic","Turtle Wax","1993","six paint-matched waxes"),v("ICE","Turtle Wax","2006","first clear polish")],
   "dt":"paste, liquid, spray · colour-matched or clear"},
  {"n":"Collinite No. 845 Insulator Wax","a":"Collinite 845 · 845","d":"Liquid wax from Utica, New York, a long-running enthusiast and marine favourite for durability.","mk":"Collinite","y":"","s":COL,
   "v":[v("No. 845 Insulator Wax","Collinite","","original liquid wax"),v("No. S-845 Insulator Speed","Collinite","","spray version")],
   "dt":"liquid · bottle size"},
  {"n":"Collinite No. 476s Super Double-Coat Paste Wax","a":"Collinite 476s · 476","d":"Hard paste wax from Collinite's automotive range.","mk":"Collinite","y":"","s":COL,
   "v":[v("No. 476s Super Double-Coat Paste Wax","Collinite"),v("No. 915 Marque D'Elegance Paste Wax","Collinite","","higher-end paste")],
   "dt":"paste · tin size"},
  {"n":"Meguiar's Gold Class Carnauba Plus","a":"Gold Class","d":"Mass-market carnauba-and-polymer wax family from Meguiar's.","mk":"Meguiar's","y":"","s":FM,
   "v":[v("Gold Class Carnauba Plus Quik Wax","Meguiar's","2012","mist-on, wipe-off spray")],
   "dt":"paste, liquid, spray"}],
 "m":[["NXT Generation Tech Wax","Meguiar's"],["No. 325 All In One Cleaner Wax","Collinite"],["Q² Wax","Gyeon"],["No. 925 Marine Wax","Collinite"]]},
{"n":"Paint sealant","a":"polymer sealant · synthetic wax","d":"Fully synthetic polymer coating that bonds to paint and usually outlasts carnauba wax.",
 "t":["liquid","spray","polymer","SiO2-infused hybrid"],"s":JS,
 "x":[{"n":"Jescar Power Lock","a":"Power Lock Polymer Paint Sealant","d":"Polymer paint sealant, often layered under carnauba; owners report it is a rebadge of a Menzerna sealant.","mk":"Jescar","y":"","s":JS,
   "v":[v("Power Lock Polymer Paint Sealant","Jescar","","around six months' protection reported by owners")],"dt":"liquid · bottle size"}],
 "m":[["Deep Gloss Paint Sealant","Wolfgang"]]},
{"n":"Ceramic coating","a":"nano coating · glass coating · SiO2 coating","d":"Liquid silica- or polysilazane-based coating that cures into a hard, water-repellent layer lasting years.",
 "t":["professional-only (installer)","DIY kit","spray-on","matte-finish","topcoat"],"s":GY,
 "x":[
  {"n":"Gtechniq Crystal Serum","a":"CSU · CSL","d":"British two-layer ceramic coating line descended from Gtechniq's first coating, C1 Crystal Lacquer.","mk":"Gtechniq","y":"2004–","s":GT,
   "v":[v("C1 Crystal Lacquer","Gtechniq","2004","first Gtechniq product"),v("Crystal Serum Ultra","Gtechniq","2017","professional-only; 10H top layer over 7H base; nine-year guarantee"),
        v("Crystal Serum Light","Gtechniq","","DIY version, about 80% of Ultra's performance")],
   "dt":"layers (base, top, EXO topcoat) · guarantee years"},
  {"n":"Gyeon Q² Mohs","a":"Mohs · Mohs EVO","d":"Flagship Gyeon paint coating, now in a modified-polysilazane EVO form.","mk":"Gyeon","y":"","s":GY,
   "v":[v("Q² Mohs EVO","Gyeon","","modified polysilazane; 30, 50 or 100 ml")],"dt":"kit size 30–100 ml · single or double layer"},
  {"n":"Gyeon Q² CanCoat","a":"CanCoat","d":"Spray-applied ceramic coating marketed as the easiest coating to apply.","mk":"Gyeon","y":"","s":GY,
   "v":[v("Q² CanCoat EVO","Gyeon","","200 ml spray"),v("Q² CanCoat Pro EVO","Gyeon","","professional version")],"dt":"200 ml can"},
  {"n":"Turtle Wax Hybrid Solutions","a":"Hybrid Solutions Ceramic","d":"Mass-market ceramic range from Turtle Wax, later with graphene additives.","mk":"Turtle Wax","y":"2019–","s":TW,
   "v":[v("Hybrid Solutions ceramic range","Turtle Wax","2019","launched with five products"),v("Hybrid Solutions Ceramic-Graphene Paste Wax","Turtle Wax","2021","75th-anniversary product"),
        v("Hybrid Solutions Pure Bead","Turtle Wax","2026","water-beading technology")],"dt":"spray, paste, wash"}],
 "m":[["Q² Pure EVO","Gyeon"],["Q² One EVO","Gyeon"],["Q² Syncro EVO","Gyeon"],["Q² Matte EVO","Gyeon"]]},
{"n":"Polishing compound","a":"cutting compound · rubbing compound · finishing polish","d":"Abrasive paste or liquid that removes swirls and scratches from paint before waxing or coating.",
 "t":["heavy cut compound","medium cut polish","finishing polish","one-step polish","pre-wax cleaner"],"s":"https://www.menzerna.com/",
 "x":[{"n":"Menzerna 400 Heavy Cut Compound","a":"Menzerna 400 · HC400","d":"Low-dust German cutting compound for hard modern clearcoats, followed by a finishing polish.","mk":"Menzerna","y":"","s":MZ,
   "v":[v("400 Heavy Cut Compound","Menzerna","","250 ml and 1 litre")],"dt":"cut stage · bottle size"}],
 "m":[["2500 Medium Cut Polish","Menzerna"],["Super Finish Plus 3800","Menzerna"],["2200 Medium Cut Polishing Compound","Menzerna"],["No. 390 Pre Wax Polish","Collinite"],["No. 631 Fleetcut Compound","Collinite"]]},
{"n":"Dual-action polisher","a":"DA polisher · random-orbit polisher · machine polisher · buffer","d":"Hand-held electric machine that spins and oscillates a pad to polish car paint with little risk of burning it.",
 "t":["free-spinning DA","long-throw DA","forced-rotation","rotary","cordless","mini (small-pad)"],"s":RU,
 "x":[
  {"n":"Porter-Cable 7424","a":"PC 7424 · 7424XP","d":"6-inch variable-speed random-orbit polisher long popular with novice detailers.","mk":"Porter-Cable","y":"","s":PC,
   "v":[v("7424","Porter-Cable","","6-inch backing plate, about 6 lb")],"dt":"backing plate 6 in · speed dial"},
  {"n":"Rupes BigFoot","a":"LHR21 · LHR15","d":"Italian random-orbit polisher family in corded and battery (iBrid) forms.","mk":"Rupes","y":"","s":RU,
   "v":[v("LHR21 Mark V","Rupes"),v("LHR15 Mark V","Rupes"),v("HLR21 iBrid","Rupes","","cordless/corded hybrid"),v("HLR15 iBrid","Rupes"),v("iBrid Nano 2","Rupes","","small-pad")],
   "dt":"throw (21 or 15 mm per model name) · corded or battery"},
  {"n":"Flex XC 3401 VRG","a":"The Beast · XC3401","d":"German forced-rotation orbital polisher with 8 mm orbit and direct drive.","mk":"Flex","y":"","s":FX,
   "v":[v("XC 3401 VRG","Flex","","1010 W; 160–480 rpm; 3,200–9,600 opm")],"dt":"pad up to 6 in · speed range"}]},
{"n":"Polishing pad","a":"buffing pad · foam pad · wool pad","d":"Hook-and-loop foam, microfibre or wool pad fitted to a polisher, graded from heavy cut to finishing.",
 "t":["foam","microfibre","wool","foamed wool","cut grade (heavy, polishing, finishing)","size 3–7 in"],"s":LC,
 "x":[
  {"n":"Lake Country CCS foam pad","a":"CCS · HDO CCS","d":"Foam pad with partially closed cells that stop polish sinking into the pad.","mk":"Lake Country","y":"","s":LC,
   "v":[v("CCS foam pads","Lake Country"),v("HDO pads","Lake Country","","microfibre and foam, for long-throw DA polishers")],"dt":"colour-coded cut grade · diameter"},
  {"n":"Lake Country Purple Foamed Wool pad","a":"purple wool","d":"Foamed wool cutting pad that is a staple of detail and body shops.","mk":"Lake Country","y":"","s":LC,"v":[],"dt":"diameter"}]},
{"n":"Car cover","a":"vehicle cover · dust cover","d":"Fitted fabric cover that protects a parked car from dust, sun, rain or snow.",
 "t":["indoor","outdoor","custom-fit","semi-custom","universal","breathable","waterproof"],"s":CC,
 "x":[{"n":"Covercraft WeatherShield","a":"WeatherShield HP · WeatherShield HD","d":"Covercraft's outdoor custom-fit cover fabrics for rain and snow.","mk":"Covercraft","y":"","s":CC,
   "v":[v("WeatherShield HP","Covercraft","","'Rain' cover"),v("WeatherShield HD","Covercraft","","'Snow' cover")],"dt":"vehicle-specific fit · fabric"}]},
]
def b(n,c="",f="",seg="",d="",sig=(),s="knowledge",rel=()): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":[],"eras":[],"sig":list(sig),"sc":[],"rel":list(rel),"s":s}
brands=[
 b("Turtle Wax","United States","1941","Mass-market car care","Chicago-founded car-care maker started by Benjamin Hirsch; now based in Lombard, Illinois.",["Turtle Wax","Turtle Wax Hybrid Solutions"],"https://en.wikipedia.org/wiki/Turtle_Wax"),
 b("Meguiar's","United States","","Mass-market and enthusiast car care","Irvine, California car-care maker, acquired by 3M in 2008.",["Meguiar's Gold Class Carnauba Plus"],"https://en.wikipedia.org/wiki/Meguiar%27s"),
 b("Collinite","United States","1936","Enthusiast and marine waxes","Wax maker in Utica, New York, known for No. 845 Insulator Wax.",["Collinite No. 845 Insulator Wax","Collinite No. 476s Super Double-Coat Paste Wax"],COL),
 b("Swissvax","Switzerland","1930","Luxury carnauba waxes","Hand-mixed carnauba and beeswax products from Fällanden near Zürich; OEM partner to Rolls-Royce, Bugatti and Aston Martin.",[],"https://www.swissvax.com/",["Zymöl"]),
 b("Zymöl","United States","","Luxury carnauba waxes","Maker of natural carnauba and oil-based waxes.",[],"https://www.zymol.com/",["Swissvax"]),
 b("Gtechniq","United Kingdom","","Ceramic coatings","Coating maker founded by Drew Gill; first product C1 Crystal Lacquer (2004).",["Gtechniq Crystal Serum"],GT,["Gyeon"]),
 b("Gyeon","South Korea","","Ceramic coatings","Ceramic coating and car-care brand built around its Q² coating range.",["Gyeon Q² Mohs","Gyeon Q² CanCoat"],GY,["Gtechniq"]),
 b("Jescar","","","Enthusiast sealants","Maker of polymer paint sealants.",["Jescar Power Lock"],JS),
 b("Menzerna","Germany","1888","Polishing compounds","Polishing-compound maker in Ötigheim, Germany, with car polishes covering four polishing stages.",["Menzerna 400 Heavy Cut Compound"],"https://www.menzerna.com/"),
 b("Rupes","Italy","1947","Detailing polishers","Family-owned Milan power-tool maker known for BigFoot polishers.",["Rupes BigFoot"],RU,["Flex"]),
 b("Flex","Germany","","Power tools and polishers","German power-tool maker known for its polishers.",["Flex XC 3401 VRG"],"knowledge",["Rupes"]),
 b("Porter-Cable","United States","","Power tools","American power-tool brand whose 7424 random-orbit polisher was a detailing staple.",["Porter-Cable 7424"],"knowledge"),
 b("Lake Country","United States","","Polishing pads","Privately owned maker of polishing and buffing pads sold in about 50 countries.",["Lake Country CCS foam pad","Lake Country Purple Foamed Wool pad"],LC),
 b("Covercraft","United States","","Car covers","Car-cover maker based in Pauls Valley, Oklahoma.",["Covercraft WeatherShield"],CC),
]
notes=("New shelf; no old kinds. Left out: Zymöl and Swissvax archetypes (no retrieved page naming their waxes; brand entries only), Lake Country Force/Hydro-Tech pads, Porter-Cable 7424XP and Menzerna FG400 lineage (snippet-only), Covercraft fabric lines beyond WeatherShield, Meguiar's Ultimate/Mirror Glaze (meguiars.com blocked), "
 "Griot's Garage and Chemical Guys polishers (not retrieved). Paint protection film not added (not in plan). Founding years omitted where not on a retrieved page.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/G1/shelves/11_01.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
