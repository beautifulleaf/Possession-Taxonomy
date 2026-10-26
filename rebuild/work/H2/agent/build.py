import json,os
W="https://en.wikipedia.org/wiki/"
kinds=[
{"n":"Meal-replacement shake","a":"meal shake · complete food · drinkable meal · meal-replacement powder · diet shake",
 "d":"Powder or ready-to-drink shake made to replace a whole meal with set calories and nutrients.",
 "t":["powder","ready-to-drink bottle","vegan","high-protein / lower-carb","weight-control (diet) shake","bar or hot meal format"],
 "s":"https://huel.com/collections/huel-powder",
 "m":[["Huel Powder","Huel"],["Huel Black Edition","Huel"],["Soylent","Soylent"],["yfood ready-to-drink meal","yfood Labs"],["SlimFast shake","SlimFast"]]},
{"n":"Oral nutritional supplement","a":"ONS · sip feed · nutritional drink · supplement drink · complete nutrition drink",
 "d":"Energy- and nutrient-dense drink or powder taken alongside food when appetite or diet falls short, often under medical advice.",
 "t":["standard (about 1–1.5 kcal/ml)","compact high-energy","high-protein","diabetes-specific","powder to mix with milk","juice style"],
 "s":"https://nutricia.com.au/adult/product/fortisip-compact/",
 "m":[["Ensure","Abbott"],["Ensure Gold","Abbott"],["Glucerna","Abbott"],["Fortisip Compact","Nutricia"],["BOOST Plus","Nestlé Health Science"],["BOOST High Protein","Nestlé Health Science"],["Complan","Complan"]]},
{"n":"Medical-condition formula","a":"hypoallergenic formula · amino-acid formula · elemental formula · metabolic formula · food for special medical purposes · medical food",
 "d":"Formula made for the dietary management of a medical condition, such as allergy or a metabolic disorder; a food, not a supplement.",
 "t":["extensively hydrolysed (hypoallergenic)","amino-acid based (elemental)","metabolic (e.g. PKU, phenylalanine-free)","infant","child / junior","nutritionally complete or incomplete"],
 "s":"https://hcp.meadjohnson.com/products/phenyl-free-2",
 "m":[["Nutramigen","Mead Johnson"],["Phenyl-Free 2","Mead Johnson"],["Neocate LCP","Nutricia"],["Neocate Syneo","Nutricia"],["Neocate Junior","Nutricia"],["EleCare","Abbott"]]}]
def B(n,c,f,seg,d,lines,sig,rel,s,sc=None): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"eras":[],"sig":sig,"sc":sc or [],"rel":rel,"s":s}
brands=[
B("Huel","United Kingdom","2014","Complete-food meal replacement","Hertfordshire maker of nutritionally complete powders, founded by Julian Hearn with nutritionist James Collier.",["Huel Powder","Black Edition","Daily Greens"],["Huel Powder"],["Soylent","yfood Labs"],W+"Huel"),
B("Soylent","United States","2013","Complete-food meal replacement","Los Angeles meal-replacement brand of Soylent Nutrition, sold as powder and ready-to-drink; now owned by Starco Brands.",["Soylent powder","Soylent ready-to-drink"],["Soylent"],["Huel"],W+"Soylent_(meal_replacement)"),
B("yfood Labs","Germany","2017","Ready-to-drink meal replacement","Munich maker of bottled drinkable meals, founded by Noel Bollmann and Benjamin Kremer; also powders and bars.",["Trinkmahlzeiten (drinks)","powders","bars"],["yfood ready-to-drink meal"],["Huel"],"https://just-food.com/?p=87572"),
B("SlimFast","United States","1977","Weight-control shakes","Diet shake and bar brand launched by Thompson Medical Company; later owned by Unilever, Glanbia and Heartland Food Products Group.",["shakes","meal bars","snacks"],["SlimFast shake"],[],W+"SlimFast"),
B("Abbott","United States","1888","Healthcare and nutrition","Illinois healthcare group whose nutrition arm makes Ensure, Glucerna, Similac and PediaSure.",["Ensure","Glucerna","PediaSure","Similac","EleCare"],["Ensure"],["Nutricia","Nestlé Health Science","Mead Johnson"],W+"Abbott_Laboratories"),
B("Nutricia","Netherlands","1896","Medical and infant nutrition","Dutch specialised-nutrition company, part of Danone since 2007, making medical nutrition and infant formula.",["Fortisip","Neocate","Aptamil","Cow & Gate"],["Fortisip Compact","Neocate"],["Abbott","Nestlé Health Science"],W+"Nutricia"),
B("Mead Johnson","United States","1905","Infant and medical nutrition","Evansville, Indiana nutrition company best known for Enfamil; part of Reckitt.",["Enfamil","Nutramigen","Phenyl-Free"],["Nutramigen"],["Abbott","Nutricia"],W+"Mead_Johnson"),
B("Complan","United Kingdom","1954","Milk-based nutrition drink","Powdered milk drink launched by Glaxo as 'the complete planned food'; Complan Foods, owned by Danone, and by Zydus Wellness in India.",["Complan"],["Complan"],["Nutricia"],W+"Complan"),
B("Nestlé Health Science","","","Medical and consumer nutrition","Nestlé nutrition unit whose BOOST line covers oral nutritional supplements.",["BOOST"],["BOOST Plus"],["Abbott","Nutricia"],"https://www.nestlemedicalhub.com/brands/boost"),
]
notes="All three planned kinds kept. Meal-replacement shake: Huel SKUs cut from 4 to 2 (Huel Essential and Superblend dropped as near-duplicates) and Huel range entry dropped; Soylent, yfood and SlimFast added. yfood is listed as a generic ready-to-drink meal because its site names flavours, not a model line. Oral nutritional supplement is a new kind (Ensure, Glucerna, Fortisip Compact, BOOST, Complan). Medical-condition formula stays kind-level with Mead Johnson, Nutricia (Neocate) and Abbott (EleCare). Fortisip variants named only in search snippets (Compact Protein, Compact Fibre) left out; Nestlé Health Science founding year and country not on a retrieved page, so left blank. Tier shelf: no archetypes or traditions."
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/H2/shelves/04_02.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
