import json, os
W='https://en.wikipedia.org/wiki/'
def V(n,mk,y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
def X(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v,"dt":dt}
kinds=[
{"n":"City bike","a":"utility bicycle · roadster · omafiets · opafiets · stadsfiets · town bike",
 "d":"Upright everyday bicycle for town riding, usually with mudguards and a chain guard.",
 "t":["Dutch roadster","step-through","single-speed","hub-gear","light roadster"],
 "s":"https://batavus.com/en-nl",
 "x":[
  X("Dutch roadster","omafiets (ladies') · opafiets (gents') · stadsfiets","Heavy steel upright roadster with hub gears or coaster brake; the ladies' step-through classic has changed little since 1911.","","1911",W+"Roadster_(bicycle)",
    [V("Gazelle roadster","Gazelle","","Dutch maker imported to the UK")],
    "frame: diamond or step-through · gears: coaster brake, hub gear · chain case, mudguards, rack"),
  X("Pashley traditional roadsters","Princess · Roadster","Pashley's English traditional roadsters: the loop-frame Princess with wicker basket and Brooks saddle, and the gents' Roadster based on a 1920s design.","Pashley","1920s design",W+"Pashley_Cycles",
    [V("Princess","Pashley","","ladies' loop frame, wicker basket"),V("Roadster","Pashley","","gents', 1920s design"),V("Guv'nor","Pashley","2007","inspired by a 1930s catalogue"),V("Patriot","Pashley","1984","sports light roadster")],
    "frame: loop or diamond · steel · hub gears · basket, saddle"),
  X("Pashley Pronto / Mailstar","Mailstar","Step-through load-carrying bicycle built by Pashley for Royal Mail deliveries.","Pashley","2001",W+"Pashley_Cycles",
    [V("Mailstar","Pashley","2001","Royal Mail delivery bike")],"front carrier · step-through frame")
 ]},
{"n":"Hybrid bike","a":"cross bike · fitness bike · flat-bar road bike",
 "d":"Flat-bar bicycle mixing road and mountain-bike features for general riding.",
 "t":["fitness (flat-bar road)","comfort hybrid","trekking","suspension fork"],
 "s":"https://www.cyclesuk.com/shop/bikes/sub/hybrid",
 "m":[["Treadwell","Cannondale"],["Larkspur","Marin"],["Sirrus X","Specialized"],["RHeO","Whyte Bikes"]]},
{"n":"Folding bike","a":"folder · folding bicycle",
 "d":"Bicycle whose frame folds to a compact size for carrying or storage.",
 "t":["vertical fold","half fold","triangle hinge","separable","electric folding"],
 "s":"https://us.brompton.com/c-line",
 "x":[
  X("Brompton","","Andrew Ritchie's 16-inch folder with hinged main tube, pivoting rear triangle and hinged stem; folds into a self-supporting package.","Brompton","1976",W+"Brompton_Bicycle",
    [V("Original design","Brompton","1979","patent filed; mass production from 1988"),V("C Line","Brompton","","steel, 4 or 12 speed"),V("P Line","Brompton","","4 or 12 speed"),V("T Line","Brompton","2022","all-titanium frame"),V("A Line","Brompton","","3 speed, older parts"),V("G Line","Brompton","2024","20-inch wheels, 8-speed Alfine; electric version")],
    "line · gearing 3/4/12 speed · steel or titanium · handlebar type · electric or not"),
  X("Dahon","","Half-fold steel and aluminium folders from the company founded by David T. Hon in California.","Dahon","1982",W+"Dahon",
    [V("Boardwalk","Dahon","","entry steel commuter, best seller"),V("EEZZ","Dahon","2012","Eurobike Award"),V("Curl","Dahon","2017","Kickstarter, 35th anniversary"),V("K-Feather","Dahon","2025","12 kg electric folder")],
    "fold type · wheel 16/20 in · gearing · electric or not"),
  X("Tern","","Half-fold folders from the Taipei company founded by Florence Shen and Joshua Hon.","Tern","2011",W+"Tern_(company)",
    [V("Verge","Tern","","performance folder"),V("Link","Tern","","everyday folder"),V("eLink","Tern","2014","first Tern e-bike"),V("BYB","Tern","","")],
    "line · wheel size · gearing · electric or not"),
  X("Birdy","","Full-suspension folding bike with a hingeless one-piece aluminium frame and 18-inch wheels.","Riese & Müller","1995",W+"Birdy_(bicycle)",
    [V("Mark 1","Riese & Müller","1995","original"),V("Mark 2","Riese & Müller","2006","monocoque frame"),V("Birdy Race","Riese & Müller","2013","drop bars"),V("Mark 3","Riese & Müller","2015","smaller fold; built by Pacific Cycles")],
    "generation · gearing · handlebar"),
  X("Bike Friday","","Custom-sized small-wheel travel folders from Eugene, Oregon, designed to pack into a suitcase.","Bike Friday","1993",W+"Bike_Friday",
    [V("Pocket Rocket","Bike Friday","late 1990s","performance road"),V("Ticket","Bike Friday","2007",""),V("All-Packa","Bike Friday","2021","bikepacking"),V("All-Day","Bike Friday","2025","touring")],
    "model · rider size · suitcase pack"),
  X("Strida","","Triangular-frame folder that folds to resemble a unicycle.","","",W+"Folding_bicycle",[],"belt drive · triangle frame"),
  X("Bickerton","","Lightweight folder that was the iconic folding bike of the 1970s.","","1970s",W+"Folding_bicycle",[],""),
  X("Gazelle Kwikstep","","Gazelle's folding bicycle of 1964.","Gazelle","1964",W+"Gazelle_(bicycle_company)",[],"")
 ]},
{"n":"Cargo bike","a":"freight bicycle · bakfiets · box bike · long john · longtail",
 "d":"Bicycle built to carry loads or passengers on a platform, box or extended rear.",
 "t":["longtail","midtail","box bike (bakfiets)","front-loader / long john","cargo trike","electric-assist"],
 "s":"https://www.splendidcycles.com/products-1",
 "x":[
  X("Long John","","Two-wheel front-loader with the cargo bed ahead of the rider and linkage steering, invented in Denmark.","","1923",W+"Freight_bicycle",
    [V("Smith & Co. original","Smith & Co.","1923","shown at Wembley 1924"),V("Monark","Monark","","last maker of the original style")],
    "load bed · wheelbase · linkage steering"),
  X("Christiania bike","Christiania trike","Copenhagen front-box cargo tricycle created by Lars Engstrøm, carrying children ahead of the rider.","Christiania Bikes","1984","https://www.christianiabikes.com/en/about-us/vores-historie/",
    [V("Classic","Christiania Bikes","",""),V("Model T","Christiania Bikes","",""),V("Model S","Christiania Bikes","",""),V("R1","Christiania Bikes","","hub motor"),V("M1","Christiania Bikes","","mid-drive motor")],
    "box size · motor: none, hub or mid-drive"),
  X("Bullitt","","Light aluminium long-john front-loader from Copenhagen, unchanged in core design since 2008.","Larry vs Harry","2008","https://www.bicyclejunction.co.nz/products/the-original-bullitt",
    [V("Bullitt","Larry vs Harry","2008","original; from 22 kg")],"gearing · box, rack or child seat · electric or not"),
  X("Urban Arrow","","Dutch electric front-loader cargo bike from Amsterdam, aimed at families and delivery firms.","Urban Arrow","c. 2009","https://bicycleretailer.com/international/2019/11/19/pon-bike-acquires-urban-arrow",
    [],"box volume · family or cargo"),
  X("Riese & Müller Load and Packster","","Riese & Müller electric front-loaders: the full-suspension Load and the Packster family cargo bike.","Riese & Müller","2017",W+"Riese_und_M%C3%BCller",
    [V("Packster 40","Riese & Müller","2017","Eurobike Award"),V("Packster 70","Riese & Müller","",""),V("Load 60","Riese & Müller","",""),V("Load 75","Riese & Müller","",""),V("Transporter","Riese & Müller","","60 and 85")],
    "box length · motor · suspension"),
  X("Longtail","midtail","Bicycle with an extended rear frame and long wheelbase carrying passengers or bags behind the rider.","","1998",W+"Freight_bicycle",
    [V("Free Radical","Xtracycle","1998","bolt-on kit"),V("Ute","Kona","2008",""),V("Big Dummy","Surly","2008","chromoly, 26 in"),V("GSD","Tern","",""),V("HSD","Tern","",""),V("Haul-a-Day","Bike Friday","2014","adjustable")],
    "length · wheel size · electric or not"),
 ],
 "m":[["NBD","Tern"],["Quick Haul","Tern"]]},
{"n":"Mini-velo","a":"small-wheel bicycle",
 "d":"Non-folding bicycle with small wheels and a full-size frame fit.",
 "t":["suspension","separable"],
 "s":"https://www.ternbicycles.com/my/bikes/471/crest",
 "x":[
  X("Moulton","Moulton bicycle","Alex Moulton's small-wheel bicycle with high-pressure tyres and suspension, first an F-frame and later space frames.","Moulton","1962",W+"Moulton_bicycle",
    [V("Series 1 (M0–M6)","Moulton","1962–1967","F-frame; Stowaway separable"),V("Mark III","Raleigh","1970",""),V("AM","Moulton","early 1980s","space frame"),V("APB","Pashley","1992–2005","under licence"),V("New Series","Moulton","1998","Pylon, Double Pylon"),V("TSR","Pashley","2005",""),V("Bridgestone Moulton","Bridgestone","2000","")],
    "frame: F-frame or space frame · suspension · separable or fixed")
 ],
 "m":[["Crest","Tern"]]},
{"n":"Electric bike","a":"e-bike · pedelec · electric bicycle · EPAC",
 "d":"Bicycle with an electric motor that assists pedalling, usually limited to 25 km/h in Europe.",
 "t":["pedelec","speed pedelec","throttle e-bike","e-MTB","e-road","folding e-bike","US class 1/2/3"],
 "s":W+"Electric_bicycle",
 "x":[
  X("VanMoof S and X","Electrified S · Electrified X","Amsterdam integrated city e-bikes with straight-tube S and compact X frames.","VanMoof","2016",W+"VanMoof",
    [V("Electrified S","VanMoof","2016",""),V("Electrified X","VanMoof","2017",""),V("S2/X2","VanMoof","2018",""),V("S3/X3","VanMoof","2020",""),V("S5/A5","VanMoof","2022",""),V("S4/X4","VanMoof","2023",""),V("S6","VanMoof","2025","")],
    "frame S or X/A · generation · colour"),
  X("Cowboy","","Brussels connected city e-bike with rear hub motor and removable battery.","Cowboy","",
    "https://discerningcyclist.com/cowboy-cruiser-vs-classic/",
    [V("Cowboy 4 / Classic","Cowboy","","renamed Classic 2023"),V("Cowboy 4 ST / Cruiser ST","Cowboy","","step-through"),V("Cruiser","Cowboy","2023","upright, belt drive")],
    "frame: high or step-through · 250 W hub · 360 Wh battery")
 ],
 "m":[["Charger3","Riese & Müller"],["Nevo4","Riese & Müller"],["Multicharger Mixte","Riese & Müller"],["Delite","Riese & Müller"],["Homage","Riese & Müller"]]},
]
def B(n,c,f,seg,d,lines,sig,s,rel=None):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"eras":[],"sig":sig,"sc":[],"rel":rel or [],"s":s}
brands=[
 B("Brompton","United Kingdom","1976","folding bikes","London folding-bike maker founded by Andrew Ritchie; Britain's largest-volume bicycle maker.",["A Line","C Line","P Line","T Line","G Line"],["Brompton"],W+"Brompton_Bicycle"),
 B("Dahon","United States","1982","folding bikes","Folding-bike maker founded in California by David T. Hon, producing in Shenzhen.",["Boardwalk","Curl","K-Feather"],["Dahon"],W+"Dahon",["Tern"]),
 B("Tern","Taiwan","2011","folding, cargo and e-bikes","Taipei maker of folding, cargo and electric bikes founded by Florence Shen and Joshua Hon.",["Verge","Link","GSD","HSD","NBD","Quick Haul","BYB","Vektron"],["Tern","Longtail"],W+"Tern_(company)",["Dahon"]),
 B("Moulton","United Kingdom","1962","small-wheel bicycles","Bradford-on-Avon maker of Alex Moulton's suspended small-wheel bicycles.",["AM","New Series","TSR"],["Moulton"],W+"Moulton_bicycle",["Pashley"]),
 B("Pashley","United Kingdom","1926","traditional and utility bicycles","Stratford-upon-Avon maker of traditional roadsters, tricycles and delivery bikes.",["Princess","Roadster","Guv'nor","Mailstar"],["Pashley traditional roadsters","Pashley Pronto / Mailstar"],W+"Pashley_Cycles",["Moulton"]),
 B("Bike Friday","United States","1992","travel folding bikes","Eugene, Oregon maker of custom small-wheel travel and folding bikes.",["Pocket Rocket","Ticket","Haul-a-Day","All-Packa"],["Bike Friday"],W+"Bike_Friday"),
 B("Gazelle","Netherlands","1892","city and e-bikes","Dieren maker, the largest Dutch bicycle manufacturer; Royal since 1992, owned by Pon since 2011.",["Kwikstep","Champion Mondial"],["Dutch roadster","Gazelle Kwikstep"],W+"Gazelle_(bicycle_company)",["Batavus","Urban Arrow"]),
 B("Batavus","Netherlands","1904","city bikes and mopeds","Heerenveen bicycle maker founded by Andries Gaastra.",[],[],W+"Batavus",["Gazelle"]),
 B("VanMoof","Netherlands","2009","city e-bikes","Amsterdam e-bike maker founded by Taco and Ties Carlier; bankrupt 2023 and bought by Lavoie.",["S","X","A"],["VanMoof S and X"],W+"VanMoof",["Cowboy"]),
 B("Cowboy","Belgium","2017","city e-bikes","Brussels maker of connected city e-bikes.",["Classic","Cruiser"],["Cowboy"],"knowledge",["VanMoof"]),
 B("Riese & Müller","Germany","1993","premium e-bikes and cargo bikes","Mühltal maker of premium e-bikes and cargo bikes, founded by Markus Riese and Heiko Müller.",["Birdy","Load","Packster","Charger","Nevo","Multicharger","Delite"],["Birdy","Riese & Müller Load and Packster"],W+"Riese_und_M%C3%BCller"),
 B("Christiania Bikes","Denmark","1978","cargo tricycles","Danish maker of the Christiania front-box cargo trike, from the Christiania smithy in Copenhagen; now on Bornholm.",["Classic","Model T","Model S"],["Christiania bike"],"https://www.christianiabikes.com/en/about-us/vores-historie/",["Larry vs Harry"]),
 B("Larry vs Harry","Denmark","","cargo bikes","Copenhagen maker of the Bullitt cargo bike.",["Bullitt"],["Bullitt"],"knowledge",["Christiania Bikes"]),
 B("Urban Arrow","Netherlands","","electric cargo bikes","Amsterdam electric cargo-bike maker founded by Jorrit Kreek and Gerald van Weel; owned by Pon.Bike since 2019.",[],["Urban Arrow"],"https://bicycleretailer.com/international/2019/11/19/pon-bike-acquires-urban-arrow",["Gazelle"]),
]
notes=("All six planned kinds kept (Electric bike new, sourced to Wikipedia). Moulton placed in Mini-velo (non-folding/separable small-wheel design) rather than Folding bike. "
 "Brompton lines kept as versions of one Brompton archetype. Batavus has a brand entry but no archetype: its sourced page names no bicycle model. "
 "Urban Arrow archetype has no versions: no retrieved page named its models (urbanarrow.com/about returned an error page). Cowboy 1-3 left out (no retrieved source); Cowboy founding facts from knowledge. "
 "Hybrid makers (Cannondale, Marin, Specialized, Whyte) kept as flat models without brand entries (likely registered by other bicycle shelves). No traditions: no artisan tradition applies to this shelf. "
 "E-cargo stays in Cargo bike, e-MTB/e-road as types of Electric bike.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/G1/shelves/03_02.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
