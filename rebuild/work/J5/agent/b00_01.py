import json,os
W='https://en.wikipedia.org/wiki/'
def K(n,d,s,t=None,m=None,a=""):
    k={"n":n,"a":a,"d":d,"s":s}
    if t:k["t"]=t
    if m:k["m"]=m
    return k
k=[
K("Rapeseed oil","Oil pressed from rapeseed; canola is the low-erucic-acid bred variety.","https://www.delli.market/collections/hillfarm-oils",["Cold-pressed","Refined"],[["hillfarm Extra Virgin Cold-Pressed Rapeseed Oil","hillfarm Oils"]],"canola oil"),
K("Sunflower oil","Oil pressed from sunflower seed.","https://www.ocado.com/products/filippo-berio-sunflower-oil/650704011",["High-oleic","Mid-oleic","High-linoleic","Cold-pressed"],[["Filippo Berio Sunflower Oil","Filippo Berio"]]),
K("Groundnut oil","Oil pressed from peanuts, refined for frying or roasted for flavour.",W+"Peanut_oil",["Refined","Unrefined","Cold-pressed","Roasted"],a="peanut oil"),
K("Coconut oil","Fat pressed from coconut flesh, solid below about 24 C.",W+"Coconut_oil",["Virgin","Refined (RBD)","Fractionated"]),
K("Avocado oil","Oil pressed from avocado flesh, with a very high smoke point.",W+"Avocado_oil",["Unrefined (cold-pressed, extra virgin)","Refined"]),
K("Sesame oil","Oil pressed from sesame seed, toasted for flavour or plain for frying.","https://www.ocado.com/products/kadoya-sesame-oil-489916011",["Toasted (dark)","Plain (light)","Refined"],[["Kadoya Pure Sesame Oil","Kadoya"]],"gingelly oil"),
K("Mustard oil","Pungent oil pressed from mustard seed, used in eastern and northern Indian cooking.","https://www.zepto.com/buy-kachi-ghani-mustard-oil",["Pressed (kachi ghani)","Refined"],[["Dhara Kachi Ghani Mustard Oil","Dhara"],["Fortune Kachi Ghani Mustard Oil","Fortune"]]),
{"n":"Nut and seed oils","a":"","d":"Specialty oils pressed from nuts and seeds, such as walnut, hazelnut, pumpkin seed, argan and flaxseed.","t":["Walnut","Hazelnut","Argan","Flaxseed","Pumpkin seed"],"s":W+"Pumpkin_seed_oil",
 "x":[{"n":"Steirisches Kürbiskernöl","a":"Styrian pumpkin seed oil","d":"Dark green oil pressed from roasted hull-less seeds of the Styrian oil pumpkin.","mk":"","y":"","s":W+"Pumpkin_seed_oil","dt":"roasted hull-less pumpkin seeds · Austria and Slovenia"}]},
K("Lard, dripping and poultry fat","Rendered animal fat for frying and baking: pork lard, beef dripping, and poultry fats.","https://www.trolley.co.uk/explore/lards",["Leaf lard","Fatback lard","Dripping","Duck fat","Goose fat","Schmaltz (chicken or goose)"],[["Armour Lard","Armour"],["Silverleaf Pure Lard","Swift & Company"]]),
K("Vegetable shortening","Solid white vegetable fat used for baking and frying.",W+"Shortening",["Palm and rapeseed blend","Coconut-based"],[["Crisco","Procter & Gamble"],["Trex","Trex"],["Cookeen","Cookeen"],["Copha","Copha"]]),
K("Margarine","Spreadable fat made from plant oils and water, with no butter.","https://www.tesco.com/groceries/en-GB/products/254263443",["Baking block","Tub spread"],[["Stork Original Baking Block","Stork"],["Flora Original","Flora"]],"plant-only fat spreads"),
]
br=[{"n":"Stork","c":"United Kingdom","f":"1920","seg":"Mainstream","kf":"baking margarine","d":"Margarine brand from Van den Berghs & Jurgens, now owned by Flora Food Group.","s":W+"Stork_(margarine)"},
{"n":"Flora","c":"United Kingdom","seg":"Mainstream","kf":"plant spread","d":"Plant-based spread developed by Unilever, now owned by Flora Food Group.","s":W+"Flora_(spread)"},
{"n":"Crisco","c":"United States","f":"1911","seg":"Mainstream","kf":"shortening","d":"Procter & Gamble vegetable shortening, sold from 1911.","s":W+"Shortening"},
{"n":"Kadoya","c":"Japan","seg":"Specialist","kf":"sesame oil","d":"Japanese sesame oil brand.","s":"knowledge"}]
out={"kinds":k,"brands":br,"traditions":[],"notes":"Trimmed to old models plus models named on retrieved Wikipedia pages (Shortening, Lard, Stork, Flora). Argan, walnut etc. as t of Nut and seed oils; Styrian pumpkin seed oil as archetype (page does not state PGI, so PGI claim omitted). Kadoya/Dhara/Fortune kept from old data."}
json.dump(out,open('work/J5/shelves/00_01.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/J5/shelves/00_01.tmp','work/J5/shelves/00_01.json')
