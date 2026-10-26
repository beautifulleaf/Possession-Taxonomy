import json, os
W='https://en.wikipedia.org/wiki/'
CB=W+'Cowboy_boot'; RB=W+'Riding_boot'
HRS='https://horseracingsense.com/types-of-cowboy-boots-western-style/'
TEC='https://tecovas.com/blog/what-are-roper-boots'
kinds=[
{"n":"Cowboy boot","a":"western boot","d":"Pull-on boot with a stitched shaft, rounded to pointed toe and angled heel in the western pattern.",
 "t":["round toe","square toe","pointed or snip toe","cowboy (angled) heel","walking heel","cowhide","exotic skins (ostrich, caiman, snake, stingray, bison)","hand-tooled"],
 "s":"https://www.fashionbeans.com/article/best-cowboy-boot-brands",
 "x":[
  {"n":"Classic western boot","a":"western · classic cowboy boot","d":"Tall pull-on boot with a shaft to at least mid-calf, angled cowboy heel over one inch and no lacing.",
   "mk":"","y":"1860s–1880s","s":CB,
   "v":[{"n":"McInerney American-style boot","mk":"T. C. McInerney","y":"1871","d":"American-style cowboy boot advertised in the Abilene Weekly Chronicle, Kansas"}],
   "dt":"shaft 12 in or more · stacked leather heel about 1.5–1.75 in · round or square toe (narrow pointed toe from about the early 1940s) · cowhide or exotic skins · decorative stitching or tooling"},
  {"n":"Roper","a":"roper boot","d":"Short-shafted cowboy boot ending above the ankle, with a low squared heel, made for calf roping and walking.",
   "mk":"","y":"1950s","s":CB,
   "v":[{"n":"Duke Roper","mk":"Frye","y":"","d":"roper in the old list"},
        {"n":"Jake","mk":"Tecovas","y":"","d":"roper boot (Tecovas blog)"},
        {"n":"Knox","mk":"Tecovas","y":"","d":"wedge roper with 1 in wedge sole (Tecovas blog)"}],
   "dt":"shaft about 8–10 in · heel under 1 in, squared · round or square toe · leather or rubber sole · pull-on or lace-up"},
  {"n":"Stockman","a":"stockman boot","d":"Ranch boot between the classic western and the roper: taller western shaft, shorter wide block heel, roomier toe box.",
   "mk":"","y":"","s":HRS,"dt":"mid-calf shaft · short block heel · roomy toe"},
  {"n":"Buckaroo","a":"buckaroo boot","d":"Very tall cowboy boot of 14 in or more with an angled riding heel, from Western range-riding tradition.",
   "mk":"","y":"","s":HRS,"dt":"shaft 14 in or more · tall angled riding heel · often scalloped top"},
  {"n":"Packer","a":"packer boot","d":"Lace-up frontier riding boot with a high heel, related to the pull-on cowboy boot; laces adjust the fit.",
   "mk":"","y":"19th century","s":"https://artsandculture.google.com/asset/american-packer-boots-by-justin-boots/VAFGKJJJyf7_Qw",
   "v":[{"n":"American packer boot","mk":"Justin Boots","y":"20th century","d":"plain unembellished pair in the Bata Shoe Museum, Toronto"}],
   "dt":"lace-up vamp · riding heel · plain or stitched shaft"},
  {"n":"Western dress boot","a":"","d":"Cowboy boot with a sleeker, streamlined shaft and a walking heel, made for town wear.",
   "mk":"","y":"","s":"https://twistedx.com/blogs/beyond-the-buckle/cowboy-boot-styles-men","dt":"slim shaft · walking heel · dress leathers and exotics"}],
 "m":[["Baker","Lucchese"],["Crayton","Lucchese"],["Dusky Bonham","Tony Lama"],["Marshall","Tecovas"],["Cartwright","Tecovas"],["Dillon","Tecovas"],["Tucson Bison","Rios of Mercedes"]]},
{"n":"Knee-high boot","a":"tall boot · riding-style boot","d":"Boot whose shaft reaches to, or just below, the knee; includes the everyday riding-style boot in the equestrian pattern.",
 "t":["riding-style boot (equestrian pattern, low heel)","flat","block heel","stiletto heel","platform","pull-on","zip","lace-up","wide calf","leather","suede","rubber/neoprene (work)"],
 "s":"https://www.dsw.com/category/womens/shoes/boots/knee-high",
 "m":[["Penny","Sam Edelman"]]},
{"n":"Over-the-knee boot","a":"thigh boot · thigh-high boot · OTK boot","d":"Boot with the shaft rising above the knee, from just over it to mid-thigh or higher.",
 "t":["over-the-knee","thigh-high","crotch-high","pull-on","zip","tie-back","leather","suede","stretch","vinyl or latex"],
 "s":"https://www.dsw.com/category/womens/shoes/boots/over-the-knee?No=2",
 "x":[
  {"n":"5050","a":"5050 boot","d":"Tall boot with a leather or suede front and micro-stretch back half, giving the name 50/50.",
   "mk":"Stuart Weitzman","y":"1993","s":"https://www.ladige.it/salute-e-benessere/25-anni-di-stivali-con-un-mito-kate-moss-per-stuart-weitzman-scf8prn7",
   "v":[{"n":"5050 (original)","mk":"Stuart Weitzman","y":"1993","d":"micro-stretch back, leather or suede front"},
        {"n":"5050 Reserve","mk":"Stuart Weitzman","y":"","d":"40 mm wide heel"}],
   "dt":"several shaft heights · leather or suede front · micro-stretch back · flat to block heel"},
  {"n":"Lowland","a":"","d":"Over-the-knee stretch-suede or leather boot with flat block heel and adjustable tie at the back of the thigh.",
   "mk":"Stuart Weitzman","y":"","s":"https://scarpa.co.nz/products/stulowlblacksuede",
   "dt":"shaft 58 cm · 30 mm block heel · almond toe · stretch suede or leather · tie-back"}]},
{"n":"Equestrian riding boot","a":"tall riding boot · English riding boot","d":"Tall boot made for riding: smooth sole, distinct low heel, close fit to the leg.",
 "t":["black","brown","calf leather","synthetic","back zip","custom-made"],
 "s":"https://www.ariat.com/mens-tall-boots",
 "x":[
  {"n":"Field boot","a":"","d":"Tall riding boot reaching just below the knee with lacing at the vamp so the ankle flexes at short jumping stirrups.",
   "mk":"","y":"","s":RB,
   "v":[{"n":"Miami Pro Field Boot","mk":"Parlanti","y":"","d":"front laces, rear elastic, full-grain calfskin, handcrafted in Italy"}],
   "dt":"front lacing at ankle · black or brown · zip or pull-on"},
  {"n":"Dress boot","a":"","d":"Stiffer tall riding boot without ankle lacing, used for dressage, formal hunting and showing.",
   "mk":"","y":"","s":RB,
   "v":[{"n":"Denver Pro Dress Boot","mk":"Parlanti","y":"","d":"lace-free, full-grain calfskin, handcrafted in Italy"}],
   "dt":"no laces · stiff shaft · traditionally black"},
  {"n":"Hunt boot","a":"top boot","d":"Dress-style tall boot with a contrasting cuff at the top, usually black with tan, worn for fox hunting.",
   "mk":"","y":"","s":RB,"dt":"black with tan cuff · no laces"}],
 "m":[["Heritage Contour","Ariat"],["Devon","Ariat"],["Palisade","Ariat"],["Ravello","Ariat"],["Sirani","Tredstep"],["Veganza","Mountain Horse"],["Flex Plus","Ovation"],["Rover","Horze"]]}]
brands=[
 {"n":"Lucchese","c":"United States","f":"1883","seg":"Luxury western boots","d":"Bootmaker founded in San Antonio by the Lucchese brothers, now based in El Paso, Texas.","sc":["Western"],"rel":["Tony Lama","Justin Boots"],"s":W+"Lucchese_Boot_Company"},
 {"n":"Tony Lama","c":"United States","f":"1911","seg":"Western boots","d":"El Paso western boot brand, part of Justin Brands (Berkshire Hathaway) since 1990.","sc":["Western"],"rel":["Justin Boots","Lucchese"],"s":W+"Tony_Lama_Boots"},
 {"n":"Justin Boots","c":"United States","f":"1879","seg":"Western and work boots","d":"Fort Worth western boot maker founded by H. J. Justin; division of Justin Brands, a Berkshire Hathaway subsidiary.","sig":["Packer"],"sc":["Western"],"rel":["Tony Lama","Nocona"],"s":W+"Justin_Boots"},
 {"n":"Ariat","c":"United States","f":"1993","seg":"Equestrian, western and work footwear","d":"California brand founded by Beth Cross and Pam Parker for riding, western and work boots.","sc":["Equestrian","Western"],"rel":["Justin Boots"],"s":W+"Ariat"},
 {"n":"Tecovas","c":"United States","f":"2015","seg":"Direct-to-consumer western boots","d":"Austin, Texas cowboy boot retailer founded by Paul Hedrick, with boots made in León, Mexico.","sc":["Western"],"rel":["Lucchese"],"s":W+"Tecovas_(company)"},
 {"n":"Stuart Weitzman","c":"United States","seg":"Designer footwear","d":"Designer shoe brand made in Spain, owned by Coach since 2015.","sig":["5050","Lowland"],"s":W+"Stuart_Weitzman"},
 {"n":"Parlanti","c":"Italy","seg":"Equestrian riding boots","d":"Italian maker of handcrafted calfskin field and dress riding boots.","sig":["Field boot","Dress boot"],"sc":["Equestrian"],"s":"https://parlantiinternational.com/collections/the-pros/products/parlanti-miami-pro-field-boot"},
 {"n":"Dehner","c":"United States","f":"1875","seg":"Custom riding, polo and service boots","d":"Omaha, Nebraska maker of custom riding, polo, military and police boots.","sc":["Equestrian"],"s":"https://dehner.com/about/about-us/"}]
trad=[{"n":"American western bootmaking","g":"Leather & footwear","r":"Texas, Oklahoma and Kansas, United States","p":"1860s–present",
 "d":"Cattle-country bootmakers who developed the pull-on cowboy boot; Texas named it State Footwear in 2007.",
 "tech":"pull-on boot with decoratively stitched shaft, stacked leather heel and optional hand-tooling","mat":"cowhide; exotic skins such as alligator, ostrich and snake",
 "forms":["Classic western boot","Roper","Packer"],"ctr":["Hyer Brothers, Olathe, Kansas","T. C. McInerney, Abilene, Kansas","Justin, Nocona and Fort Worth, Texas","Lucchese, San Antonio and El Paso","Tony Lama, El Paso"],
 "auth":"named maker in a cattle-country boot town; stacked leather heel; hand-stitched shaft","s":CB}]
notes=("Merged Riding-style boot into Knee-high boot (type; Sam Edelman Penny kept as only model). Dropped high-street SKUs: Franco Sarto Gisella, Marc Fisher Rilan, Naturalizer Nona, White Mountain Altitude, Aerosoles Lewes, Azalea Wang Langlau, Jessica Simpson Alexiana, London Rag Brandy. "
 "Stuart Weitzman 5050 and Lowland placed under Over-the-knee (brand site lists both as over-the-knee; 5050 shaft 53 cm), not Knee-high as the brief suggested. Highland left out (no retrievable page; stuartweitzman.com, fashionmagazine.com, truewestmagazine.com returned 403). "
 "Konig, Fabbri, Cavallo, Old Gringo, Rios of Mercedes register entries and models not added (no retrieved page). Old cowboy models without confirmed style stay in m. Paddock/jodhpur and polo boots left to other shelves/kinds.")
out={"kinds":kinds,"brands":brands,"traditions":trad,"notes":notes}
p='work/A2/shelves/04_02.json'; tmp=p+'.tmp'
json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,p); print('ok')
