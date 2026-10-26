import json, os
W='https://en.wikipedia.org/wiki/'
WH='https://www.weber.com/JP/en/our-history.html'
VWA='https://www.virtualweberbullet.com/determine-age-weber-grills-smokers/'
VWB='https://www.virtualweberbullet.com/weber-bullet-history/'
WKC='https://weberkettleclub.com/history/the-weber-master-touch-history/'
WHG='https://www.which.co.uk/reviews/barbecues/article/best-gas-barbecues-axVlH3d15McL'
WHC='https://www.which.co.uk/reviews/barbecues/article/best-charcoal-barbecues-aYz0z1j512eA'
CRS='https://www.consumerreports.org/home-garden/grills/sturdiest-grills-in-consumer-reports-tests-a4505677951/'
CRB='https://www.consumerreports.org/home-garden/grills/best-gas-grills-of-the-year-a6005011720/'
OKJ='https://www.oklahomajoes.com/products/highland-offset-reverse-flow-smoker-grill-24203003'
BS='https://blackstoneproducts.com/pages/weber-blackstone'
KJ='https://woodman.pt/en/the-story-of-kamado-joe/'
BK='https://broilking.ca/pages/manufacturing'
def X(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in v],"dt":dt}
kinds=[
{"n":"Kettle grill","a":"barbecue grill · charcoal grill · kettle barbecue","d":"Lidded round bowl grill on legs that cooks over charcoal, used for direct grilling and lid-down indirect cooking.",
 "t":["charcoal kettle","gas-assist kettle","square charcoal grill","brazier"],"s":"https://amer.weber.com/en-us/collections/charcoal-grills",
 "x":[X("Weber Original Kettle","The originating domed charcoal kettle grill, invented by George Stephen Sr.","Weber","1952",WH,
   [("One-Touch cleaning system","Weber","1983","Ash-cleaning system"),
    ("Performer","Weber","1990","Kettle on a cart with fully enclosed ash catcher; integrated cart from 1992"),
    ("Master-Touch","Weber","1992","Premium 22.5 in kettle; second generation reached the US in 2015 with Gourmet Grate system"),
    ("Summit Charcoal","Weber","2016","")],
   "bowl 18.5, 22.5 (57 cm) and 26.75 in · lid thermometer, ash catcher, cart",a="George's Barbecue Kettle")],
 "m":[["Master-Touch","Weber"],["Original Kettle","Weber"],["Performer","Weber"],["PRO22K-LEG-2","Napoleon"],["Kettleman","Char-Broil"]]},
{"n":"Gas grill","a":"gas barbecue · propane grill","d":"Grill heated by propane or natural-gas burners under a lid, usually on a wheeled cart with side shelves.",
 "t":["propane (LPG)","natural gas","infrared sear burner","side burner","freestanding cart"],"s":W+"Barbecue_grill",
 "x":[X("Weber Genesis","Weber's mainstream cart-mounted gas grill line that replaced the Gas Barbecue Kettle.","Weber","1985",WH,
   [("Genesis 1/2/3/4/5","Weber","1985","First series"),("Genesis 1000–5000","Weber","1993",""),("Genesis (redesign)","Weber","2007",""),
    ("Genesis II","Weber","2017","Genesis II LX S-240 and S-340 topped Consumer Reports' sturdiness tests"),("Genesis (2022)","Weber","2022","")],
   "burner count · sear zone, side burner"),
  X("Weber Spirit","Weber's entry-level cart gas grill, smaller and cheaper than the Genesis.","Weber","1995",WH,
   [("Spirit 500/700","Weber","early 1990s",""),("Spirit E-210 / E-310","Weber","2007",""),("Spirit II","Weber","2018",""),
    ("Spirit E-325","Weber","","Tested by Which?"),("Spirit E-425C","Weber","","Tested by Consumer Reports")],"burner count"),
  X("Weber Summit","Weber's top gas grill line above the Genesis.","Weber","1999",WH,[],""),
  X("Napoleon Prestige","Napoleon's premium gas grill line.","Napoleon","",CRS,
   [("Prestige Pro 665RSIB","Napoleon","","Top-scoring large grill in Consumer Reports' sturdiness test")],""),
  X("Weber Gas Barbecue Kettle","Weber's first gas grill, sold until the Genesis replaced it.","Weber","1971",VWA,[],"")],
 "r":[["Baron","Broil King"],["Regal","Broil King"],["Imperial","Broil King"],["Crown","Broil King"]],
 "m":[["Freestyle 365","Napoleon"],["Evolve","Char-Broil"],["FlavorMax","Char-Broil"],["AP55-GL4101S","Feasto"],["Force 2-burner","Everdure"],["FlexFlame","Ninja"]]},
{"n":"Kamado grill","a":"kamado · ceramic cooker · egg","d":"Thick-walled egg-shaped charcoal cooker, usually ceramic, with draft vents for grilling, smoking and baking.",
 "t":["ceramic","table-top / mini"],"s":W+"Kamado",
 "x":[X("Mushikamado","Traditional movable Japanese clay pot with domed lid; the model for the American kamado-style cooker.","","traditional",W+"Kamado",[],"clay body · removable domed lid"),
  X("Big Green Egg","Ceramic kamado with sliding bottom draft door and swivelling top vent; set the modern kamado pattern.","Big Green Egg","1974",W+"Big_Green_Egg",
   [("Mini","Big Green Egg","",""),("MiniMax","Big Green Egg","",""),("Small","Big Green Egg","",""),("Medium","Big Green Egg","",""),
    ("Large","Big Green Egg","","Core size"),("XLarge","Big Green Egg","",""),("2XL","Big Green Egg","","")],
   "grid 10–29 in · 39–375 lb · ConvEGGtor, pizza stone, EGG Nest stand"),
  X("Kamado Joe Classic Joe","Ceramic kamado with an 18 in grate and multi-level Divide & Conquer cooking system.","Kamado Joe","",KJ,
   [("Classic Joe Series I","Kamado Joe","",""),("Classic Joe Series II","Kamado Joe","",""),("Classic Joe Series III","Kamado Joe","","Adds SloRoller hyperbolic smoke chamber")],
   "Joe Jr 13.5 in · Classic 18 in · Big Joe 24 in · Kontrol Tower vent, Air Lift Hinge, AMP firebox")],
 "m":[["MiniMax","Big Green Egg"],["Joe Jr","Kamado Joe"]]},
{"n":"Pellet grill","a":"pellet smoker · wood-pellet grill","d":"Electric grill-smoker that augers wood pellets from a hopper into a fire pot, with a fan and controller holding temperature.",
 "t":["Wi-Fi controller","griddle combo"],"s":W+"Pellet_grill",
 "x":[X("Traeger pellet grill","The original auger-fed wood-pellet grill, adapted from pellet heating stoves; patented 1987 and sole maker until 2007.","Traeger","1985",W+"Pellet_grill",
   [("LMH controller grills","Traeger","","Early three-position low/medium/high controller"),("WiFIRE grills","Traeger","","App-connected controller")],
   "barrel cooking chamber · hopper · controller generation"),
  X("Pit Boss pellet grill","Value-priced pellet grill range from Dansons.","Pit Boss","","https://www.pitboss-grills.com/pages/this-is-pit-boss",
   [("Pro Series","Pit Boss","",""),("Competition Series","Pit Boss","",""),("Onyx Edition","Pit Boss","",""),("DX Series","Pit Boss","","")],"size by cooking area · combo and vertical variants"),
  X("Louisiana Grills Founders Legacy","Pellet grill line launched with Joe Traeger after Traeger's patent expired.","Louisiana Grills","2019",W+"Pellet_grill",[],""),
  X("Weber SmokeFire","Weber's wood-pellet grill.","Weber","2020",WH,[],"")],
 "m":[["Pellet Joe","Kamado Joe"],["900 Pellet","Blackstone"]]},
{"n":"Offset smoker","a":"stick burner · horizontal smoker · reverse-flow smoker","d":"Horizontal cooking chamber with a firebox at one end, so heat and wood smoke pass over the food and out a chimney.",
 "t":["classic offset","reverse flow"],"s":"https://en.wikipedia.org/wiki/Smoker_(cooking)",
 "x":[X("Oklahoma Joe's Highland","Mass-market steel offset smoker-grill burning charcoal and wood splits.","Oklahoma Joe's","",OKJ,
   [("Highland Classic","Oklahoma Joe's","","Traditional offset"),("Highland Reverse Flow","Oklahoma Joe's","","Model 24203003; removable baffles switch between reverse flow and traditional offset")],
   "about 616 sq in primary grate · firebox grate · heavy-gauge steel"),
  X("Oklahoma Joe's Longhorn","Larger Oklahoma Joe's offset smoker-grill.","Oklahoma Joe's","",OKJ,
   [("Longhorn Classic","Oklahoma Joe's","",""),("Longhorn Reverse Flow","Oklahoma Joe's","","")],""),
  X("Yoder Loaded Wichita","Handmade American offset smoker from Hutchinson, Kansas.","Yoder Smokers","","https://www.yodersmokers.com/2023/05/mastering-the-offset-smoker/",[],"")],
 "m":[["Kingman","Yoder Smokers"]]},
{"n":"Bullet smoker","a":"vertical water smoker · drum smoker","d":"Upright cylindrical charcoal smoker, often with a water pan between fire and grates to steady temperature.",
 "t":["water smoker","upright drum smoker"],"s":"https://en.wikipedia.org/wiki/Smoker_(cooking)",
 "x":[X("Weber Smokey Mountain Cooker","Bullet water smoker whose prototype Erich Schlosser built from Weber kettle parts.","Weber","1981",VWB,
   [("Model 2880 (18.5 in)","Weber","1981","Original; later renamed 2890 and 2820"),("Model 1880 (14.5 in)","Weber","1981","Discontinued 1983"),
    ("Model 721001 (18.5 in)","Weber","2009","Improved version"),("Model 731001 (22.5 in)","Weber","2009","Largest size"),("Model 711001 (14.5 in)","Weber","2014","Small size returns")],
   "14.5, 18.5, 22.5 in · access door · lid handle and leg materials by year",a="WSM"),
  X("Upright drum smoker","Home-built or commercial smoker made from a steel drum with charcoal at the bottom and racks near the top.","","","https://en.wikipedia.org/wiki/Smoker_(cooking)",[],"55-gallon drum most common",a="UDS · ugly drum smoker")]},
{"n":"Portable grill","a":"camping grill · tabletop grill · travel barbecue","d":"Small charcoal, gas or electric grill light enough to carry for camping, picnics or balconies.",
 "t":["charcoal","gas cartridge or propane","electric","tabletop"],"s":W+"Barbecue_grill",
 "x":[X("LazyMan Model AP","Early gas grill from Chicago Combustion Corporation, described as the first portable gas grill.","LazyMan","1954",W+"Barbecue_grill",[],""),
  X("Hibachi / shichirin","Small Japanese charcoal brazier; in English 'hibachi' usually means a small cast-iron or aluminium grill.","","Edo period",W+"Barbecue_grill",[],"cast iron, aluminium or clay"),
  X("Weber Smokey Joe","Miniature version of the Weber kettle.","Weber","1962",WH,[("Smokey Joe Premium 37cm","Weber","","Tested by Which?")],"37 cm bowl"),
  X("Weber Q","Compact Weber gas grill for balconies and travel.","Weber","2003",WH,
   [("Q 140","Weber","2009",""),("Q 240","Weber","2012",""),("Q 1400 / Q 2400","Weber","2014","Q 140 and Q 240 renamed")],""),
  X("Weber Go-Anywhere","Rectangular portable Weber grill; the gas version began as the Hot Shot Table Top Gas Grill.","Weber","early 1980s",VWA,[],"charcoal or gas"),
  X("Cobb","Bowl-shaped portable grill from South Africa, first fuelled with dried corn cobs; grills, roasts and smokes.","Cobb","","https://www.griliai.lt/en/blogs/news/cobb-grill-how-did-a-clumsy-bowl-shaped-container-become-a-global-hit",[],"")],
 "m":[["Traveler","Weber"],["Safari Chef 30","Cadac"],["TravelQ PRO285","Napoleon"]]},
{"n":"Flat-top griddle","a":"outdoor griddle · plancha","d":"Gas-fired flat steel cooking plate on a cart or tabletop stand for outdoor breakfast, smash burgers and stir-fry.",
 "t":["cart","tabletop","with hood","griddle–pellet combo"],"s":BS,
 "x":[X("Blackstone griddle","Outdoor griddle from the brand that pioneered backyard griddles.","Blackstone","2008",BS,
   [("28\" XL Omnivore Griddle with Hood","Blackstone","",""),("Adventure Ready 28\" Griddle","Blackstone","","Flexfold legs"),("Culinary 22\" XL Griddle Pellet Grill Combo","Blackstone","","Griddle plus pellet grill")],
   "17, 22, 28, 36 in plates · Iron Forged, Culinary, Bronco, Select, Tailgate collections")]},
]
brands=[
{"n":"Weber","c":"United States","f":"1893","seg":"Mainstream grills","d":"Palatine, Illinois maker that invented the charcoal kettle grill and leads in gas, charcoal and portable grills.",
 "lines":["Original Kettle","Smokey Joe","Smokey Mountain Cooker","Genesis","Spirit","Summit","Q","SmokeFire","Traveler"],"eras":["George Stephen Sr. kettle, 1951–52"],
 "sig":["Weber Original Kettle","Weber Smokey Mountain Cooker","Weber Genesis"],"sc":["backyard barbecue"],"rel":["Blackstone","Ducane"],"s":W+"Weber-Stephen_Products"},
{"n":"Big Green Egg","c":"United States","f":"1974","seg":"Premium kamado","d":"Atlanta firm founded by Ed Fisher making green ceramic kamado cookers in seven sizes.",
 "lines":["Mini","MiniMax","Small","Medium","Large","XLarge","2XL"],"eras":[],"sig":["Big Green Egg"],"sc":["Eggtoberfest"],"rel":["Kamado Joe"],"s":W+"Big_Green_Egg"},
{"n":"Kamado Joe","c":"United States","f":"2009","seg":"Premium kamado","d":"Atlanta kamado maker founded by Bobby Brennan and Kerry Coker.",
 "lines":["Classic Joe","Big Joe","Joe Jr","Pellet Joe"],"eras":[],"sig":["Kamado Joe Classic Joe"],"sc":[],"rel":["Big Green Egg"],"s":KJ},
{"n":"Traeger","c":"United States","f":"1985","seg":"Pellet grills","d":"Originator of the wood-pellet grill, founded by Joe Traeger in Oregon; now based in Salt Lake City.",
 "lines":["WiFIRE grills"],"eras":["Traeger family, 1985–2006"],"sig":["Traeger pellet grill"],"sc":[],"rel":["Pit Boss","Louisiana Grills"],"s":"https://www.traeger.com/about-us"},
{"n":"Pit Boss","c":"","f":"","seg":"Value pellet grills","d":"Dansons brand of pellet grills, combo grills, vertical smokers and griddles.",
 "lines":["Pro Series","Competition Series","Onyx Edition","DX Series"],"eras":[],"sig":["Pit Boss pellet grill"],"sc":[],"rel":["Louisiana Grills","Traeger"],"s":"https://www.pitboss-grills.com/pages/this-is-pit-boss"},
{"n":"Louisiana Grills","c":"","f":"1999","seg":"Pellet grills","d":"Dansons pellet-grill brand; Dansons was founded in 1999 by Dan Thiessen and his sons.",
 "lines":["Founders Series"],"eras":[],"sig":["Louisiana Grills Founders Legacy"],"sc":[],"rel":["Pit Boss"],"s":"https://louisiana-grills.com/blogs/blogs/founders-story"},
{"n":"Oklahoma Joe's","c":"United States","f":"1987","seg":"Offset smokers","d":"Smoker brand started by Joe Davidson, who sold his first twelve smokers in 1987; owned by W.C. Bradley Co. since 1998.",
 "lines":["Highland","Longhorn"],"eras":["Joe Davidson, 1987–1998"],"sig":["Oklahoma Joe's Highland"],"sc":["competition barbecue"],"rel":["Char-Broil"],"s":"https://www.oklahomajoes.com/pages/our-story"},
{"n":"Yoder Smokers","c":"United States","f":"","seg":"Enthusiast smokers","d":"Hutchinson, Kansas maker of handcrafted offset and pellet smokers.",
 "lines":["Loaded Wichita","Kingman"],"eras":[],"sig":["Yoder Loaded Wichita"],"sc":[],"rel":[],"s":"https://www.yodersmokers.com/2023/05/mastering-the-offset-smoker/"},
{"n":"Napoleon","c":"Canada","f":"1976","seg":"Premium gas grills","d":"Barrie, Ontario maker (Wolf Steel Ltd.) of fireplaces and grills; grills since 1995.",
 "lines":["Prestige","Freestyle","TravelQ"],"eras":["Wolfgang and Ingrid Schroeter, 1976–2018"],"sig":["Napoleon Prestige"],"sc":[],"rel":["Broil King","Weber"],"s":W+"Napoleon_(company)"},
{"n":"Broil King","c":"Canada","f":"1906","seg":"Gas grills","d":"Barbecue brand of Onward Manufacturing, a Waterloo, Ontario family firm that turned to Broil King grills in 1985.",
 "lines":["Baron","Regal","Imperial","Crown","Porta-Chef","Keg"],"eras":[],"sig":[],"sc":[],"rel":["Napoleon"],"s":BK},
{"n":"Char-Broil","c":"United States","f":"1948","seg":"Mass-market grills","d":"Columbus, Georgia grill maker owned by W.C. Bradley Co.",
 "lines":["Kettleman","Evolve","FlavorMax"],"eras":[],"sig":[],"sc":[],"rel":["Oklahoma Joe's"],"s":W+"Char-Broil"},
{"n":"Blackstone","c":"United States","f":"2008","seg":"Outdoor griddles","d":"Griddle pioneer founded by Roger Dahle; combined with Weber in 2025 as separate brands.",
 "lines":["Iron Forged","Culinary","Bronco","Select","Tailgate"],"eras":[],"sig":["Blackstone griddle"],"sc":[],"rel":["Weber"],"s":BS},
{"n":"Cobb","c":"South Africa","f":"","seg":"Portable grills","d":"Portable bowl grill first designed in South Africa to cook with corn cobs.",
 "lines":[],"eras":[],"sig":["Cobb"],"sc":["camping"],"rel":[],"s":"https://www.griliai.lt/en/blogs/news/cobb-grill-how-did-a-clumsy-bowl-shaped-container-become-a-global-hit"},
]
notes=("Old 'Barbecue grill' (k135) renamed Kettle grill per plan; its Weber models became versions of the Original Kettle archetype (also kept in m). "
 "Left out: Which? Best Buy names (paywalled), Wirecutter/Serious Eats picks (fetch blocked), Napoleon Rogue and Broil King model details (only search snippets), "
 "Kamado Joe and Pit Boss launch years and Yoder founding year (not on retrieved pages), Traeger model names (Pro, Ironwood, Timberline: not confirmed), Bandera/Weber Ranch details. "
 "Gas grill tier list relies on Consumer Reports sturdiness winners and CR/Which? tested models. No craft traditions apply to this shelf.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/C2/shelves/10_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(sum(len(k.get('x',[])) for k in kinds),'archetypes',len(brands),'brands')
