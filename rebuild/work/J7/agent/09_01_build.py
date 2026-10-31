import json,os
W="https://en.wikipedia.org/wiki/"
M=W+"Mead"; P=W+"Polish_mead"; T=W+"Tej"; PQ=W+"Pulque"; PW=W+"Palm_wine"; FW=W+"Fruit_wine"; TU=W+"Tub%C3%A2"
def A(n,d,s,a="",mk="",y="",v=None,dt=""):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
mead={"n":"Mead","a":"honey wine · hydromel","d":"Wine fermented from honey and water, sometimes with fruit, spices, grapes or malt.",
 "t":["Traditional mead","Fruit mead","Spice mead","Sparkling mead","Dry · semi-sweet · sweet · dessert"],"s":M,
 "x":[
  A("Traditional mead","Mead made only from honey, water and yeast.",M,a="show mead",dt="dry to sweet · still or sparkling · single-varietal honey"),
  A("Sack mead","Strong mead of about 14% ABV or more, made with extra honey and often sweet.",M,dt="sweet · high strength"),
  A("Melomel","Mead that contains fruit.",M,a="fruit mead",v=[V("Cyser","","","honey and apple, honey supplying most sugar"),V("Pyment","","","honey with grapes or grape juice"),V("Black mead","","","honey and blackcurrants"),V("Morat","","","honey and mulberries"),V("Rubamel","","","raspberry melomel"),V("Bilbemel","","","blueberry mead")],dt="fruit · fruit share · sweetness"),
  A("Metheglin","Mead flavoured with herbs or spices.",M,a="spice mead",dt="spices · herbs"),
  A("Braggot","Mead brewed with malt, with hops optional.",M,a="bragot · bragget",dt="malt share · hopped or not"),
  A("Bochet","Mead made with honey caramelised before the water is added.",M,v=[V("Bochetomel","","","bochet with fruit")],dt="degree of caramelisation"),
  A("Acerglyn","Mead made from honey and maple syrup.",M),
  A("Session mead","Lower-alcohol mead, often carbonated.",M,a="hydromel · short mead · quick mead",dt="strength · carbonation"),
  A("Polish mead grades","Polish TSG meads named for the honey-to-water ratio: półtorak, dwójniak, trójniak, czwórniak.",P,a="miód pitny",y="2008",
    v=[V("Półtorak","","","2:1 honey:water, 15–18%, dessert, aged 3 years"),V("Dwójniak","","","1:1, 15–18%, sweet, aged 2 years"),V("Trójniak","","","1:2, 12–15%, semi-sweet, aged 1 year"),V("Czwórniak","","","1:3, 9–12%, dry, aged 9 months")],dt="grade · sweetness · ageing"),
  A("Tej","Ethiopian and Eritrean honey wine flavoured with gesho, cloudy, sweet and lightly effervescent.",T,a="mes · t'ej",v=[V("Berz","","","sweeter, weaker honey-water, aged less")],dt="7–11% ABV · served in a berele"),
  A("Chouchen","Breton mead, traditionally of buckwheat honey with fermentation started by apple juice or cider.",W+"Chouchen",v=[V("Chufere","","","weaker honey-and-cider drink")]),
  A("Medovukha","Eastern Slavic honey drink fermented quickly, sometimes with herbs or berries.",W+"Medovukha",a="medovuha · myod"),
  A("Sima","Low-alcohol Finnish mead flavoured with lemon, drunk at vappu.",M),
  A("Muratina","Kenyan mead made with honey, water and Kigelia fruit.",M,a="karuvu · murigi"),
 ],
 "m":[["Lyme Bay Traditional Mead","Lyme Bay Winery"]]}
fruit={"n":"Fruit wine","a":"country wine","d":"Wine fermented from a fruit other than grape, apple or pear, such as plum or berry.",
 "t":["Elderberry","Plum","Strawberry","Cherry","Blackcurrant","Blackberry","Pomegranate","Pineapple","Flower wine (elderflower, dandelion)"],"s":"https://lymebaywinery.co.uk/fruit-wine/strawberry-wine",
 "x":[
  A("Elderberry wine","English country wine of fermented elderberries; elderflower wine is called elder blow wine.",FW),
  A("Plum jerkum","Plum wine of the north Cotswolds, once made in Worcester.",FW),
  A("Cherry wine","Wine fermented from cherries, including Danish and Croatian Marasca styles.",FW,v=[V("Cherry Kijafa","","","Danish fortified cherry wine, about 16%"),V("Maraska","","","Croatian Marasca cherry wine"),V("Fredriksdal Cherry Wine","","","Danish")],dt="sweet or fortified · spiced"),
  A("Pomegranate wine","Wine fermented from pomegranates, with roots in Armenia.",FW,v=[V("Rimon","Rimon Winery","","Israeli commercial pomegranate wine")]),
  A("Dandelion wine","Country wine fermented with dandelion flowers.",FW),
  A("Strawberry wine","Wine fermented from strawberries.","https://lymebaywinery.co.uk/fruit-wine/strawberry-wine",v=[V("Lyme Bay Strawberry Wine","Lyme Bay Winery","","medium, 11%"),V("Vinoscout Strawberry Wine","Glina Whisky Destillerie")]),
  A("Pineapple wine","Wine fermented from pineapple, made in Hawaii, Nigeria, the Dominican Republic and Okinawa.",FW,v=[V("Maui's Winery pineapple wine","Maui's Winery"),V("Jacobs Wines pineapple wine","Jacobs Wines","","Nigeria")]),
 ]}
palm={"n":"Palm wine","a":"palm toddy · sap wine · emu · nsafufuo · tuak","d":"Wine fermented from the sap of palms such as coconut, palmyra, date or oil palm.",
 "t":["Fresh (sweet)","Matured (sour)","Coconut","Palmyra","Oil palm","Raffia","Nipa"],"s":"https://kulturcart.de/nkulenus-palm-drink-315ml-6034000022025-momjays-afro-markt/",
 "x":[
  A("Toddy","South Asian palm wine of coconut or palmyra sap, sold in toddy shops.",PW,a="kallu · kള്ള്",dt="coconut or palmyra · fresh or matured"),
  A("West African palm wine","Oil-palm or raffia sap wine of Nigeria, Ghana and Cameroon, used at weddings and funerals.",PW,a="emu · nsafufuo · palmy",dt="oil palm or raffia · bottled or fresh"),
  A("Tubâ","Filipino palm wine of coconut, kaong or fishtail sap, also made in western Mexico and Guam.",TU,a="tuba · tuhak · tunggang",v=[V("Bahalina","","","aged with mangrove bark, deep brown-orange"),V("Tuba fresca","","","non-alcoholic Mexican version")],dt="palm species · mangrove bark"),
  A("Tuak","Palm wine of Indonesia and Malaysia, notably among the Batak, Iban and Dusun.",PW),
  A("Lagmi","Date-palm sap wine of Tunisia and Algeria.",PW),
 ],
 "m":[["Nkulenu's Palm Drink","Nkulenu's"]]}
palm["x"][0]["a"]="kallu"
pulque={"n":"Pulque","a":"octli · metoctli","d":"Milky, low-alcohol drink fermented from the aguamiel sap of maguey agave in central Mexico.",
 "t":["Natural (blanco)","Curado (with fruit or nuts)","Canned"],"s":PQ,
 "x":[
  A("Pulque natural","Plain pulque fermented from aguamiel with seed pulque, 2–7% ABV, served from barrels in pulquerías.",PQ,y="pre-Hispanic"),
  A("Pulque curado","Pulque blended with fruit, nuts or other ingredients.",PQ,dt="flavour"),
  A("Canned pulque","Pasteurised pulque packed in cans for export.",PQ,v=[V("San Bartolo Hacienda","San Bartolo Hacienda","","Tlaxcala; principal exporter"),V("Nectar del Razo","Nectar del Razo","","sold in the US by Boulder Imports")]),
 ]}
trad=[
 {"n":"Polish mead (miód pitny)","g":"Food & drink","r":"Poland","p":"Medieval–present; grade names 17th–18th c.; EU TSG 2008","d":"Mead made in four legally defined grades by honey-to-water ratio and ageing.","tech":"Honey must fermented and aged 9 months to 3 years","mat":"Honey, water, sometimes fruit juice or spices","forms":["Półtorak","Dwójniak","Trójniak","Czwórniak"],"ctr":[],"auth":"TSG label with grade name; ratio and minimum ageing per grade","s":P},
 {"n":"Ethiopian tej","g":"Food & drink","r":"Ethiopia and Eritrea","p":"Aksumite era–present","d":"Honey wine flavoured with gesho, made at home and sold in tej houses.","tech":"Honey water fermented with boiled gesho stems and leaves, stirred daily, filtered","mat":"Honey, water, gesho (Rhamnus prinoides)","forms":["Tej","Berz"],"ctr":["Tejbet (tej houses)"],"auth":"Cloudy yellow, sweet, slightly effervescent; served in a berele","s":T},
 {"n":"Mexican pulque","g":"Food & drink","r":"Central Mexico (Hidalgo, Tlaxcala)","p":"Mesoamerican–present; peak late 19th century","d":"Fermented maguey sap drink sold in pulquerías.","tech":"Aguamiel tapped twice daily and fermented 7–14 days with seed pulque (Zymomonas mobilis)","mat":"Maguey sap (Agave americana and related)","forms":["Pulque natural","Pulque curado"],"ctr":["Pulquerías of Mexico City","Haciendas of Hidalgo and Tlaxcala"],"auth":"Fresh, viscous, milky; canning changes the flavour","s":PQ},
 {"n":"Palm-wine tapping","g":"Food & drink","r":"West Africa, South and Southeast Asia, Pacific, western Mexico","p":"Traditional–present","d":"Tapping palm flower stalks for sap that ferments naturally within hours.","tech":"Flower stalk cut and sap collected in a fastened container; wild-yeast fermentation","mat":"Coconut, palmyra, oil, raffia, date, nipa or kaong palm sap","forms":["Toddy","Tubâ","West African palm wine","Tuak"],"ctr":["Toddy shops (Kerala, Sri Lanka)"],"auth":"Sold fresh; sours within a day","s":PW},
]
out={"kinds":[mead,fruit,palm,pulque],"brands":[],"traditions":trad,
 "notes":"All four planned kinds kept (k108 Mead, k109 Fruit wine, k110 Palm wine renamed from 'Palm or sap wine'; Pulque new). Archetypes are maker-free styles sourced to Wikipedia; old models kept (Lyme Bay, Nkulenu's in m; strawberry models as versions). Left out: lambanog/arrack (distilled, belong with spirits), umeshu (steeped liqueur, not fermented fruit), mulsum/oxymel/hypocras (historic, not mead proper), Polish mead producers (none on retrieved page), no brand entries since no archetype has a maker."}
p="work/J7/shelves/09_01.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
