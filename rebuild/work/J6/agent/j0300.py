import json
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
H=W+'Hot_chocolate'
dc=[
 A("Mexican table chocolate","chocolate para mesa · tablet chocolate","Semi-sweet tablets with cinnamon, sugar and vanilla, whipped to a froth (traditionally with a molinillo).","","",H,[V("Ibarra","Ibarra","1925","Chocolatera de Jalisco since 1954; cocoa paste, sugar, cinnamon, soy lecithin; 8-wedge tablet"),V("Abuelita","Abuelita","1939","Fábrica de Chocolates La Azteca; Nestlé since 1995"),V("Taza Chocolate Mexicano Discs","Taza Chocolate","2005","Stoneground organic discs, Somerville, Massachusetts"),V("Mayordomo","","","Mexican-style brand named on the page")],"form: tablet · whisk: molinillo"),
 A("Spanish chocolate a la taza","chocolate a la taza","Very thick Spanish drinking chocolate, sometimes thickened with cornstarch, eaten with churros.","","",H,[],"served with churros"),
 A("Italian cioccolata calda","cioccolata calda","Very thick, creamy Italian hot chocolate said to date from Turin around 1560.","","c.1560",H,[],"origin Turin"),
 A("British drinking chocolate","drinking chocolate","Sweetened cocoa-led powder for making a hot drink with milk or water.","Cadbury","",H,[V("Cadbury Drinking Chocolate","Cadbury"),V("Domori Cacao Cult Hot Chocolate","Domori"),V("Ghirardelli Double Chocolate Premium Hot Cocoa","Ghirardelli")],"cocoa the largest ingredient"),
]
cp=[
 A("Dutch-process cocoa","alkalised cocoa","Cocoa treated with alkali (usually potassium carbonate) to lower acidity and darken colour; developed by Coenraad Johannes van Houten.","Van Houten","early 19th century (press 1828)",W+'Dutch_process_cocoa',[V("Van Houten VH Finest Cacao","Van Houten"),V("Ghirardelli Premium Baking 100% Cocoa Dutch-Process","Ghirardelli"),V("Guittard Cocoa Rouge","Guittard")],"types: natural, Dutch, black"),
 A("Natural cocoa","non-alkalised","Acidic, lighter and more bitter cocoa powder.","","",W+'Dutch_process_cocoa',[],"acidic"),
 A("Black cocoa","","Cocoa given further alkali treatment for an earthy taste; defines Oreo-style cookies.","","",W+'Dutch_process_cocoa',[],"extra alkali"),
]
mm=[
 A("Ovaltine","Ovomaltine","Swiss malt-extract drink mix developed in 1904 by Albert Wander; ABF holds the trademark, Nestlé the US rights.","Ovaltine","1904",W+'Ovaltine',[V("Export to Britain as Ovaltine","","1909","")],"malt extract, sugar, whey; cocoa in some flavours"),
 A("Milo","","Chocolate-flavoured malted powder created in 1934 by Thomas Mayne for Nestlé in Australia.","Milo","1934",W+'Milo_(drink)',[],"malted barley, milk powder, sugar, cocoa"),
 A("Horlicks","","British malted milk powder founded in Chicago in 1873, with chocolate versions in the UK and India.","Horlicks","1873",W+'Horlicks',[V("UK chocolate Horlicks","Aimia Foods","","Chocolate version prepared with hot water")],"malt; chocolate flavour"),
]
kinds=[
 {"n":"Drinking chocolate","a":"hot chocolate · drinking chocolate powder","d":"Sweetened cocoa powder for making a drink, with cocoa as its largest ingredient by weight; a sugar-led mix is not included.","s":"https://thenibble.com/reviews/main/beverages/cocoas/hot-chocolate-product-reviews2.asp","m":[["Cadbury Drinking Chocolate","Cadbury"],["Domori Cacao Cult Hot Chocolate","Domori"],["Ghirardelli Chocolate Double Chocolate Premium Hot Cocoa","Ghirardelli"]],"x":dc},
 {"n":"Cocoa powder","a":"","d":"Unsweetened powder of pressed cocoa solids: natural, Dutch-process or black.","t":["natural","Dutch-process","black cocoa"],"s":"https://hbingredients.co.uk/products/ir-cp22241","m":[["Ghirardelli Premium Baking 100% Cocoa Dutch-Process","Ghirardelli"],["Guittard Cocoa Rouge Cocoa Powder","Guittard"],["VH Finest Cacao","Van Houten"]],"x":cp},
 {"n":"Malted chocolate drink powder","a":"malted drink mix","d":"Malt-based drink powders, often with cocoa, made up with milk or water; ready-to-drink cartons are in Soft Drinks.","s":W+'Ovaltine',"x":mm},
]
B=lambda n,c,f,seg,kf,d,s,**k: dict({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s},**k)
brands=[
 B("Van Houten","Netherlands","1815","Heritage manufactory","Dutch-process cocoa","Chocolate factory opened by Casparus van Houten in Amsterdam; Coenraad developed alkalised cocoa; Barry Callebaut owns the brand since 2002.",W+'Coenraad_Johannes_van_Houten'),
 B("Ibarra","Mexico","1925","Mainstream","table chocolate","Mexican chocolate para mesa, produced by Chocolatera de Jalisco since 1954.",W+'Ibarra_(chocolate)'),
 B("Abuelita","Mexico","1939","Mainstream","table chocolate","Mexican table chocolate brand now owned by Nestlé.",W+'Abuelita'),
 B("Taza Chocolate","United States","2005","Artisan & independent","stoneground Mexican-style","Somerville, Massachusetts stoneground organic chocolate maker founded by Alex Whitmore.",W+'Taza_Chocolate'),
 B("Ovaltine","Switzerland","1904","Mainstream","malt drink","Malt drink developed by Albert Wander in Bern.",W+'Ovaltine'),
 B("Milo","Australia","1934","Mainstream","malted chocolate drink","Nestlé malted drink created by Thomas Mayne.",W+'Milo_(drink)'),
 B("Horlicks","United Kingdom","1873","Mainstream","malted milk","Malted milk powder founded in Chicago by the Horlick brothers.",W+'Horlicks'),
 B("Cadbury","United Kingdom","","Mainstream","chocolate","British chocolate maker.","knowledge"),
 B("Ghirardelli","United States","","Mainstream","chocolate","San Francisco chocolate maker.","knowledge"),
 B("Guittard","United States","","Premium","baking chocolate","California chocolate maker.","knowledge"),
 B("Domori","Italy","","Premium","criollo chocolate","Italian craft chocolate maker.","knowledge"),
 B("Valrhona","France","","Premium","couverture","French couverture maker.","knowledge"),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Left out unsourced: Valor a la taza, Angelina, Hotel Chocolat, Willie's, Droste, Callebaut, Cacao Barry, Hershey's, Nesquik (page not retrieved) archetypes/versions; Droste and Valrhona only as knowledge/none. No test-winner pages retrieved. Malted drinks checked: mixes made up with milk/water stay here; RTD cartons are Soft Drinks."}
json.dump(out,open('03_00.src.json','w'),ensure_ascii=False)
