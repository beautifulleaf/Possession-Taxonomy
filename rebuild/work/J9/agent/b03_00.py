import json, os
W='https://en.wikipedia.org/wiki/'
K=[]
def k(n,a,d,s,t=None,m=None,x=None,tg=None):
    o={"n":n,"a":a,"d":d}
    if t: o["t"]=t
    if tg: o["tg"]=tg
    o["s"]=s
    if x: o["x"]=x
    if m: o["m"]=m
    K.append(o)
k("Orange juice","OJ · orange juice","Juice squeezed or reamed from oranges, sold chilled or shelf-stable, fresh, not-from-concentrate or reconstituted.",W+"Orange_juice",
  t=["not from concentrate (NFC)","from concentrate","freshly squeezed, unpasteurised","with pulp / juicy bits","smooth, no pulp","blood orange","fortified (calcium, vitamin D)","low-acid","organic","frozen concentrate"],
  m=[["Tropicana Pure Premium","Tropicana"],["Trop50","Tropicana"],["Simply Orange","Simply Beverages"],["Minute Maid orange juice","Minute Maid"],["Florida's Natural","Florida's Natural Growers"],["Naked Orange Juice","Naked Juice"],["Innocent juices","Innocent Drinks"],["Del Monte orange juice","Del Monte"],["Princes orange juice","Princes"],["Daily Juice","National Foods"],["Pago orange","Pago"]])
k("Apple juice","apple juice · apple cider (US, unfiltered)","Juice pressed from apples, sold clear and filtered or cloudy and unfiltered, sometimes from a single apple variety.",W+"Apple_juice",
  t=["clear / clarified","cloudy / unfiltered","US fresh apple cider","single-variety (e.g. McIntosh, Russet)","from concentrate","organic"],
  m=[["Simply Apple","Simply Beverages"],["Innocent apple juice","Innocent Drinks"],["Pago apple","Pago"],["Granini apple","Granini"],["Happy Day","Rauch"]])
k("Grape juice","grape juice · Concord grape juice","Unfermented juice of crushed grapes, purple from Concord grapes or white from Niagara and other varieties.",W+"Grape_juice",
  t=["purple / red (Concord)","white (Niagara)","sparkling grape juice","from concentrate"],
  x=[{"n":"Welch's Concord grape juice","a":"Welch's grape juice","d":"Pasteurised unfermented Concord grape juice, the original bottled grape juice of the United States.","mk":"Welch's","y":"1869","s":W+"Welch%27s",
      "v":[{"n":"Pasteurised grape juice","mk":"Welch's","y":"1869","d":"Thomas Bramwell Welch's method to stop fermentation"},{"n":"Welch's Grape Juice Company","mk":"Welch's","y":"1893","d":"Company founded by Charles E. Welch in Westfield, New York"},{"n":"Sparkling juices","mk":"Welch's","y":"","d":"Carbonated grape juice line"}],
      "dt":"purple or white · 100% juice or juice drink · bottle or frozen concentrate"}])
k("Cranberry & berry juice","cranberry juice · cranberry juice cocktail · berry juice","Tart cranberry juice, usually blended with other juice and sugar as a juice cocktail, plus other berry juices.",W+"Cranberry_juice",
  t=["juice cocktail (about 25–27% cranberry)","100% juice blend","light / sweetener","white cranberry","cranberry blends (apple, grape)","blackcurrant & other berries"],
  x=[{"n":"Ocean Spray Cranberry Juice Cocktail","a":"Cran-Apple · Cran-Grape","d":"Sweetened cranberry juice cocktail from the American growers' cooperative, the reference cranberry drink.","mk":"Ocean Spray","y":"1933","s":"https://en.wikipedia.org/wiki/Ocean_Spray_(cooperative)",
      "v":[{"n":"Cranberry Juice Cocktail","mk":"Ocean Spray","y":"1933","d":"Original juice cocktail"},{"n":"Cranapple","mk":"Ocean Spray","y":"1963","d":"Cranberry–apple blend, later Cran-Apple and Cran-Grape"},{"n":"White cranberry juice","mk":"Ocean Spray","y":"2002","d":"Made from white cranberries"}],
      "dt":"regular, light or diet · single cranberry or blend · bottle size"}],
  m=[["Fruit d'Or cranberry juice","Fruit d'Or"]])
k("Tropical & exotic juice","pineapple juice · mango juice · passion fruit · guava · pomegranate juice","Juices and juice drinks from tropical and exotic fruit such as pineapple, mango, passion fruit, guava, lychee and pomegranate.",W+"Pineapple_juice",
  t=["pineapple","mango","passion fruit","guava","lychee","pomegranate","multivitamin / multifruit"],
  m=[["Rubicon mango","Rubicon"],["Rubicon guava","Rubicon"],["POM Wonderful pomegranate juice","POM Wonderful"],["Jumex","Jumex"],["Pago mango","Pago"]])
k("Tomato & vegetable juice","tomato juice · vegetable juice · V8","Juice of tomatoes or mixed vegetables, often salted and spiced, drunk plain or used for Bloody Mary-style drinks.",W+"Tomato_juice",
  t=["plain tomato","seasoned / spiced","low-sodium","mixed vegetable","carrot & beetroot","clam-tomato (Clamato)"],
  x=[{"n":"V8","a":"V-8","d":"American eight-vegetable juice built on tomato, the best-known vegetable juice.","mk":"Campbell's","y":"1933","s":"https://en.wikipedia.org/wiki/V8_(beverage)",
      "v":[{"n":"V8 Original","mk":"Campbell's","y":"","d":"Tomato concentrate with a blend of vegetable juices"},{"n":"Spicy Hot","mk":"Campbell's","y":"","d":"Spiced version"},{"n":"Low-Sodium","mk":"Campbell's","y":"","d":"Reduced-salt version"},{"n":"V-Fusion","mk":"Campbell's","y":"","d":"Fruit-and-vegetable 100% juice blend"},{"n":"V8 Splash","mk":"Campbell's","y":"","d":"Sweetened juice cocktail"}],
      "dt":"original, spicy, low-sodium, organic · can or bottle"}],
  m=[["Clamato","Clamato"],["Pago tomato","Pago"]])
k("Fruit nectar","nectar · Fruchtnektar · néctar","Fruit purée or juice diluted with water and a little sugar, with 25–50% fruit depending on the fruit.","https://www.pfanner.com/en/fruit-facts/whats-the-difference-between-100-juice-a-nectar-and-a-fruit-juice-drink/",
  t=["peach","apricot","pear","mango","sour cherry","banana","blackcurrant"],
  m=[["Granini nectars","Granini"],["Pago nectars","Pago"],["Jumex nectars","Jumex"],["Kern's nectars","Jumex"],["Happy Day","Rauch"],["Pfanner nectars","Pfanner"]])
k("Juice drink","juice cocktail · fruit drink · juice pouch","Sweetened drink with some fruit juice, below nectar strength, often in cartons or pouches for children.",W+"Juice",
  t=["juice cocktail","fruit drink","pouch","carton with straw","no added sugar","spritzer (juice with sparkling water)"],tg=["baby"],
  x=[{"n":"Capri-Sun pouch","a":"Capri-Sonne","d":"Juice-concentrate drink in a 200 ml foil stand-up pouch with a straw, launched in West Germany.","mk":"Capri-Sun","y":"1969","s":W+"Capri-Sun",
      "v":[{"n":"Capri-Sonne","mk":"Capri-Sun","y":"1969","d":"Original orange drink, 22 June 1969"},{"n":"100% Juice / Organic","mk":"Capri-Sun","y":"","d":"No-added-sugar lines"},{"n":"Fruity Water / Roarin' Waters","mk":"Capri-Sun","y":"","d":"Flavoured water pouches (UK / US)"},{"n":"330 ml spouted pouch","mk":"Capri-Sun","y":"","d":"Resealable pouch for older drinkers"}],
      "dt":"flavour · 200 ml pouch or larger formats · regular or no added sugar"},
     {"n":"Hi-C","a":"","d":"American fruit-juice-flavoured drink from the Minute Maid division.","mk":"Minute Maid","y":"1947","s":W+"Hi-C","v":[],"dt":"flavour · juice box or bottle"},
     {"n":"SunnyD","a":"Sunny Delight","d":"Orange-flavoured drink with little juice, launched in Florida and later in the UK.","mk":"SunnyD","y":"1963","s":W+"Sunny_Delight",
      "v":[{"n":"Sunny Delight","mk":"Doric Foods","y":"1963","d":"Original, Mount Dora, Florida"},{"n":"UK launch","mk":"SunnyD","y":"1998","d":"Launched in the United Kingdom"}],"dt":"flavour · chilled or ambient"}],
  m=[["Ceres Liqui-Fruit","Ceres"],["Welch's juice drinks","Welch's"]])
k("Cold-pressed juice & shot","cold-pressed juice · HPP juice · juice shot · wellness shot · ginger shot","Juice pressed in a hydraulic press and kept raw or high-pressure processed, including small ginger and wellness shots.",W+"Cold-pressed_juice",
  t=["raw unprocessed (about 3 days)","high-pressure processed (HPP, about 30 days)","green juice","ginger shot","turmeric shot","juice cleanse set"],
  m=[["BluePrint","BluePrint"],["Rubicon Raw Energy","Rubicon"]])
k("Smoothie","smoothie · fruit smoothie · green smoothie","Thick drink of puréed fruit, sometimes with vegetables, yoghurt or protein, sold bottled and chilled.",W+"Smoothie",
  t=["fruit","green / vegetable","protein","yoghurt-based","kids' pouch"],
  m=[["Innocent smoothies","Innocent Drinks"],["Naked Green Machine","Naked Juice"],["Naked protein smoothies","Naked Juice"],["Pago smoothies","Pago"],["Granini smoothies","Granini"],["Jumex smoothies","Jumex"]])
k("Still lemonade & limeade","still lemonade · cloudy lemonade · limeade · nimbu pani · shikanjvi · citron pressé","Non-carbonated drink of lemon or lime juice, water and sweetener, sold chilled or shelf-stable.",W+"Lemonade",
  t=["still cloudy lemonade","pink lemonade","limeade","mint lemonade (limonana)","spiced lemonade (nimbu pani, shikanjvi)","zero sugar"],
  m=[["Simply Lemonade","Simply Beverages"],["Simply Limeade","Simply Beverages"],["Minute Maid Lemonade","Minute Maid"],["Country Time","Country Time"],["Fentimans Victorian Lemonade","Fentimans"]])
k("Plant waters","coconut water · birch water · birch sap · maple water · aloe vera drink · cactus water","Packaged saps and plant liquids drunk as light refreshment, chiefly coconut water and birch sap.",W+"Coconut_water",
  t=["coconut water","pressed coconut water","birch water / birch sap","maple water","aloe vera drink with pulp","cactus water","sparkling"],
  m=[["Vita Coco Original","Vita Coco"],["Vita Coco Pressed","Vita Coco"],["Rubicon coconut water","Rubicon"],["Innocent coconut water","Innocent Drinks"],["Naked coconut water","Naked Juice"]])
B=[
 {"n":"Tropicana","c":"United States","f":"1947","seg":"Chilled juice","d":"Orange-juice maker founded by Anthony T. Rossi in Florida; owned by PAI Partners (61%) and PepsiCo since 2021.","lines":["Pure Premium","Trop50"],"rel":["Naked Juice","Dole"],"s":W+"Tropicana_Products"},
 {"n":"Innocent Drinks","c":"United Kingdom","f":"1998","seg":"Smoothies & juice","d":"London smoothie and juice maker, majority-owned by Coca-Cola since 2010.","lines":["Smoothies","Juices","Coconut water"],"s":W+"Innocent_Drinks"},
 {"n":"Minute Maid","c":"United States","f":"1946","seg":"Juice","d":"Coca-Cola juice brand that first marketed frozen orange concentrate; Cappy and Del Valle regionally.","lines":["Minute Maid Lemonade","Hi-C"],"sig":["Hi-C"],"rel":["Simply Beverages"],"s":W+"Minute_Maid"},
 {"n":"Simply Beverages","c":"United States","f":"2001","seg":"Chilled not-from-concentrate juice","d":"Coca-Cola's chilled juice and lemonade brand within Minute Maid.","lines":["Simply Orange","Simply Lemonade","Simply Limeade","Simply Apple"],"rel":["Minute Maid"],"s":W+"Simply_Orange_Juice_Company"},
 {"n":"Ocean Spray","c":"United States","f":"1930","seg":"Cranberry cooperative","d":"Massachusetts-based cooperative of cranberry growers in the US, Canada and Chile.","lines":["Cranberry Juice Cocktail","Cran-Apple","Craisins"],"sig":["Ocean Spray Cranberry Juice Cocktail"],"s":"https://en.wikipedia.org/wiki/Ocean_Spray_(cooperative)"},
 {"n":"Welch's","c":"United States","f":"1869","seg":"Grape juice","d":"Grape-juice company owned since 1956 by the National Grape Cooperative.","sig":["Welch's Concord grape juice"],"s":W+"Welch%27s"},
 {"n":"Campbell's","c":"United States","seg":"Packaged food","d":"American food company that owns V8 vegetable juice, acquired in 1948.","lines":["V8"],"sig":["V8"],"s":"https://en.wikipedia.org/wiki/V8_(beverage)"},
 {"n":"Capri-Sun","c":"Germany","f":"1969","seg":"Juice drink pouches","d":"Pouched juice drink created by Rudolf Wild & Co. of Heidelberg; licensed to Kraft in North America.","sig":["Capri-Sun pouch"],"s":W+"Capri-Sun"},
 {"n":"SunnyD","c":"United States","f":"1963","seg":"Orange drink","d":"Low-juice orange-flavoured drink first made by Doric Foods in Florida.","sig":["SunnyD"],"s":W+"Sunny_Delight"},
 {"n":"Granini","c":"Germany","seg":"Juice & nectar","d":"Fruit-juice brand of the family-owned Eckes-Granini Group, Nieder-Olm.","rel":["Pago"],"s":W+"Granini"},
 {"n":"Pago","c":"Austria","f":"1888","seg":"Juice & nectar","d":"Klagenfurt juice and nectar brand in green glass bottles, now part of Eckes-Granini.","rel":["Granini"],"s":W+"Pago_International"},
 {"n":"Rauch","c":"Austria","f":"1919","seg":"Juice, nectar & iced tea","d":"Vorarlberg drinks maker behind Happy Day and Bravo juices.","lines":["Happy Day","Bravo"],"s":"https://en.wikipedia.org/wiki/Rauch_(company)"},
 {"n":"Naked Juice","c":"United States","f":"1983","seg":"Smoothies & juice","d":"Californian smoothie and juice brand, owned by PAI Partners and PepsiCo.","lines":["Green Machine"],"rel":["Tropicana"],"s":W+"Naked_Juice"},
 {"n":"Jumex","c":"Mexico","f":"1961","seg":"Juice & nectar","d":"Mexican juice and nectar maker known for its little blue can; owns Kern's.","lines":["Kern's","Frugo"],"s":W+"Jumex"},
 {"n":"Rubicon","c":"United Kingdom","f":"1982","seg":"Exotic juice drinks","d":"London-founded maker of mango, guava and other exotic fruit drinks, part of A.G. Barr.","s":W+"Rubicon_Drinks"},
 {"n":"Ceres","c":"South Africa","f":"1986","seg":"Juice","d":"Western Cape juice maker owned by Pioneer Foods, also behind Liqui-Fruit.","lines":["Liqui-Fruit"],"s":W+"Ceres_Fruit_Juices"},
 {"n":"Del Monte","c":"United States","f":"1886","seg":"Packaged fruit & juice","d":"Food brand whose packaged-food and brand rights are now split among Del Monte companies.","s":W+"Del_Monte_Foods"},
 {"n":"Vita Coco","c":"United States","f":"2004","seg":"Coconut water","d":"New York coconut-water company founded by Michael Kirban and Ira Liran.","lines":["Original","Pressed"],"s":W+"Vita_Coco"},
]
notes=("All 12 planned kinds kept (no old data). Tier lists built from fetched Wikipedia/maker pages and one independent taste test (Tasting Table orange-juice test: Naked winner, Tropicana runner-up). "
"Archetypes only for named icons: Welch's Concord, Ocean Spray Cranberry Juice Cocktail, V8, Capri-Sun, Hi-C, SunnyD. Left out: Suja/Pressed/Evolution Fresh (no page retrieved; Suja wiki 404), OKF aloe (only retail snippets), Dole juice (no confirming page), "
"named birch/maple water brands (none on fetched pages), Which?/Consumer Reports winners (not found). No regional style archetypes (blood orange, nimbu pani) as bottled-product icons could be confirmed, so they are types.")
out={"kinds":K,"brands":B,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J9/shelves/03_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
