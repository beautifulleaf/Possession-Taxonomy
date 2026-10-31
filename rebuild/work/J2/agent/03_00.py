import json,os
def A(n,d,s,mk="",y="",dt="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=v
    return x
TF="https://www.thetinnedfishmarket.com/blogs/guides-to-tinned-fish/bonito-del-norte-tuna"
K=[
{"n":"Tinned tuna","a":"canned tuna · atún · thon · ventresca","d":"Tuna packed in a sealed tin, jar or pouch that keeps it shelf-stable.",
 "t":["skipjack","yellowfin","albacore","bluefin","chunk","solid","flaked","fillet","ventresca","in oil","in water","in brine","smoked","flavoured"],
 "s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/canned-tuna",
 "x":[
 A("Rio Mare","Italian mass-market tuna in oil or natural, the main food brand of the Bolton Group.","https://www.esmmagazine.com/a-brands/rio-mare-boosts-bolton-groups-fy-2024-sales-293921",mk="Rio Mare",dt="99.7% responsibly sourced tuna · aims for 100% MSC by 2030"),
 A("John West tuna","British canned tuna range from the house that moved into tuna in the 1950s; pole-and-line range launched 2011.","https://en.wikipedia.org/wiki/John_West_Foods",mk="John West",y="1857"),
 A("StarKist tuna","American canned tuna, sold under the StarKist name since 1942 and owned by Dongwon since 2008.","https://en.wikipedia.org/wiki/StarKist",mk="StarKist",y="1917",dt="mascot Charlie the Tuna"),
 A("Sea Chicken","Japanese tuna flakes launched 1958 by Hagoromo, one of Japan's leading canned tuna brands.","https://www.encyclopedia.com/books/politics-and-business-magazines/hagoromo-foods-corporation",mk="Hagoromo",y="1958",dt="flaked tuna"),
 A("Ventresca","Tuna belly, packed as a premium cut; examples are bluefin ventresca in Jersey butter and yellowfin ventresca.",TF,dt="bluefin, yellowfin or white tuna belly",a="tuna belly"),
 A("Herpac bluefin tuna","Bluefin loin, belly and tarantelo packed by Salazones Herpac.",TF,mk="Herpac",dt="loin · belly · morrillo · tarantelo")
 ],
 "m":[["Tonnino Yellowfin Tuna Solid Pack in Olive Oil","Tonnino"],["Tonnino Albacore Tuna Fillets in Olive Oil","Tonnino"],["Light Standard Tuna in Oil","Dongwon"],["Century Tuna","Century Pacific Food, Inc."],["Dardanel Tuna in Olive Oil","Dardanel"],["Lucky Star Tuna Chunks","Lucky Star"],["Gomes da Costa Chunk Tuna in Natural Water","Gomes da Costa"],["Isla Real Tuna","NIRSA (Negocios Industriales Real)"],["Tuna Flake","Nissui"],["Light Tuna Super Non-Oil","Inaba Foods"],["Olasagasti Yellowfin tuna in olive oil","Olasagasti"],["Real Conservera Española Ventresca tuna belly with curry","Real Conservera Española"]]},
{"n":"Bonito del Norte","a":"white tuna · albacore · bonito · Thunnus alalunga · atún blanco","d":"Premium tinned albacore (Thunnus alalunga) of the Cantabrian summer costera, canned as loins or belly in oil or escabeche.",
 "t":["loins","ventresca","in olive oil","in escabeche","natural","organic"],
 "s":TF,
 "x":[
 A("Ortiz Bonito del Norte","Line-caught Cantabrian albacore canned since 1891 by the Ondarroa house, originally in escabeche.","https://www.conservasortiz.com/en/?p=5892",mk="Ortiz",y="1891",dt="loins in olive oil · escabeche tradition · caught one by one",a="Ortiz white tuna"),
 A("Conservas Albo bonito","Albacore canned in Vigo, Galicia, by a house founded in 1869.","https://www.foodswinesfromspain.com/en/food/articles/2022/july/bonito-del-norte-canned-food",mk="Conservas Albo",y="1869"),
 A("Olasagasti white tuna","White tuna fillets in olive oil, in organic olive oil, in salsa Catalana and as ventresca.",TF,mk="Olasagasti",dt="fillets · ventresca · salsa Catalana",a="Olasagasti Bonito"),
 A("Carmelo tuna fillets","White tuna fillets in organic extra virgin olive oil, plus a spicy version.",TF,mk="Carmelo",dt="fillets in organic EVOO"),
 A("Angelachu bonito del norte","Bonito del Norte fillets in organic extra virgin olive oil.",TF,mk="Angelachu",dt="fillets in organic EVOO")
 ]},
{"n":"Tinned salmon & trout","a":"canned salmon · canned trout","d":"Salmon or trout packed in a sealed tin or jar, smoked or not.","t":["pink","sockeye","wild","smoked","in oil","in brine","trout"],"s":"https://alltinned.com/fish-types/5","m":[["Dardanel Salmon in Olive Oil","Dardanel"],["Geomar Salmón al Natural","Geomar"],["Tonnino Silver Salmon in Extra Virgin Olive Oil","Tonnino"]]},
{"n":"Tinned white fish","a":"tinned cod · tinned hake · tinned sea bass · tinned whitefish · tinned sturgeon","d":"Cod, hake, sea bass, whitefish and sturgeon packed in sealed tins or jars.","t":["cod","cod cheeks","cod neck","hake (merluza)","sea bass (lubina)","whitefish (sig)","sturgeon"],"s":"https://alltinned.com/fish-types","m":[["Los Peperetes Cod Galician style","Los Peperetes"],["Papa Anzóis Cod cheeks in extra virgin olive oil","Papa Anzóis"],["Papa Anzóis Cod neck in organic extra virgin olive oil","Papa Anzóis"]]},
{"n":"Tinned cod liver","a":"pechen treski","d":"Cod liver cooked and packed in its own oil in a sealed tin; cod flesh is Tinned white fish, cod liver oil is in Health, Medical & Mobility.","t":["natural","smoked"],"s":"https://www.thefishsociety.co.uk/cod-liver.html"},
{"n":"Tinned eel","a":"","d":"Eel or elver packed in a sealed tin or jar.","t":["smoked","in sauce","in olive oil"],"s":"https://alltinned.com/fish-types","m":[["Ecofood Eel in Unagi Sauce","EcoFood"],["Ecofood Smoked Eel in Olive Oil","EcoFood"]]}
]
def Bk(n,c,f,seg,kf,d,sig,s): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":[],"s":s}
B=[
Bk("Ortiz","Spain","1891","Premium","Bonito del Norte","Ondarroa conservera, fifth-generation family firm, canning north-coast white tuna and anchovies.",["Ortiz Bonito del Norte"],"https://www.conservasortiz.com/en/?p=5892"),
Bk("Rio Mare","Italy","","Mainstream","tuna","Italian tuna brand of the Bolton Group, which markets over 500,000 tonnes of tuna a year.",["Rio Mare"],"https://www.esmmagazine.com/a-brands/rio-mare-boosts-bolton-groups-fy-2024-sales-293921"),
Bk("John West","United Kingdom","1857","Mainstream","tuna and salmon","British tinned fish brand founded as Pelling Stanley and Company in Liverpool, owned by Thai Union.",["John West tuna"],"https://en.wikipedia.org/wiki/John_West_Foods"),
Bk("StarKist","United States","1917","Mainstream","tuna","Californian tuna canner founded as the French Sardine Company; owned by Dongwon Industries since 2008.",["StarKist tuna"],"https://en.wikipedia.org/wiki/StarKist"),
Bk("Hagoromo","Japan","1931","Mainstream","Sea Chicken","Shimizu canner founded as Goto Canning Company; Sea Chicken launched 1958.",["Sea Chicken"],"https://www.encyclopedia.com/books/politics-and-business-magazines/hagoromo-foods-corporation"),
Bk("Conservas Albo","Spain","1869","Premium","Galician tuna","Vigo canner of Cantabrian bonito.",["Conservas Albo bonito"],"https://www.foodswinesfromspain.com/en/food/articles/2022/july/bonito-del-norte-canned-food"),
Bk("Bumble Bee","United States","1899","Mainstream","tuna","American canned tuna brand that began in Astoria, Oregon.",[],"knowledge"),
Bk("Callipo","Italy","1913","Premium","Calabrian tuna","Tuna canner of Pizzo, Calabria.",[],"knowledge"),
Bk("Tonnino","Italy","","Mainstream","tuna fillets","Italian tinned tuna in olive oil and flavoured fillets.",[],"knowledge"),
Bk("Wild Planet","United States","","Specialist","pole-and-line tuna","American brand of pole-and-line caught tuna packed without added water or oil.",[],"knowledge"),
Bk("Petit Navire","France","","Mainstream","tuna","French tinned tuna brand.",[],"knowledge"),
Bk("Saupiquet","France","1877","Mainstream","tuna and sardines","French tinned fish brand.",[],"knowledge"),
Bk("Dongwon","South Korea","","Mainstream","tuna","Korean food group; Dongwon F&B sells tuna and Dongwon Industries owns StarKist.",[],"knowledge"),
Bk("Nuri","Portugal","","Premium","Portuguese conservas","Portuguese tinned fish house.",[],"knowledge"),
Bk("Ati Manel","Portugal","","Premium","Matosinhos conservas","Portuguese cannery making spiced skipjack and other tins.",[],"knowledge")]
T=[
{"n":"Cantabrian and Basque conservas","g":"Food & drink","r":"Cantabria and the Basque Country, Spain","p":"19th century onward","d":"Hand-processed canning of bonito del norte and anchovies on the Bay of Biscay coast, in oil or escabeche.","tech":"loins cooked in salt water, cleaned by hand, packed in olive oil or escabeche and sterilised in an autoclave","mat":"Thunnus alalunga, anchovies, olive oil","forms":["Bonito del Norte","Ventresca","Escabeche","Anchovies"],"ctr":["Ondarroa (Ortiz)","Santoña","Vigo (Albo)"],"auth":"check the can names Thunnus alalunga, not atún claro","s":"https://www.thetinnedfishmarket.com/blogs/guides-to-tinned-fish/bonito-del-norte-tuna"},
{"n":"Portuguese conservas","g":"Food & drink","r":"Portugal, notably Matosinhos","p":"mid-19th century onward","d":"Hand-prepared tinned sardines, tuna and mackerel in olive oil, with aged vintage tins valued like wine.","tech":"fish cut and gutted by hand, steamed outside the can, packed in tinplate and aged at least six months","mat":"sardines, tuna, carapau, cod, octopus, olive oil, tinplate","forms":["Sardines in olive oil","Vintage tins","Sardine roe"],"ctr":["Matosinhos","Pinhais (1920)","Ramirez (1853)"],"auth":"look for aged reserve tins and ANICP member producers","s":"https://www.360meridianos.com/especial/conservas-portuguesas"}]
out={"kinds":K,"brands":B,"traditions":T,"notes":"82 tuna SKUs cut to 6 archetypes by house plus 12 mainstream models; ranges (r) dropped as wholesale/SKU noise. Bonito del Norte added as new kind. White fish tins merged as types of Tinned white fish; trout merged into Tinned salmon & trout. Archetypes only where a page was retrieved: Bumble Bee, Callipo, Tonnino, Wild Planet, Petit Navire, Saupiquet, Dongwon, Nuri and Ati Manel are brand-register entries from knowledge only (no archetype). Brief's Ortiz ventresca not confirmed by retrieved Ortiz page, so ventresca is a generic archetype. Dongwon tuna kept as a flat model."}
p='work/J2/shelves/03_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
