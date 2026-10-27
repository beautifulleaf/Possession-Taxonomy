import json,os
def A(n,d,s,mk="",y="",dt="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=v
    return x
FR="https://www.foodrepublic.com/2016/06/21/what-are-the-different-types-of-fish-eggs-in-japanese-cuisine/"
BO="https://en.wikipedia.org/wiki/Bottarga"
K=[
{"n":"Salmon roe","a":"ikura · red caviar · keta roe","d":"Roe of salmon, whole eggs sold loose or marinated.","t":["salted","soy-cured","loose","wild","farmed"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/salmon-roe",
 "x":[A("Ikura","Large orange salmon eggs cured in salt or soy sauce, popping texture, often called Japanese caviar.",FR,dt="soy-cured (shoyu-zuke) · sold loose",a="Japanese caviar")],
 "m":[["Regiis Ova Salmon Roe","Regiis Ova Caviar"]]},
{"n":"Trout roe","a":"steelhead roe","d":"Roe of trout, sold fresh, cured or smoked.","t":["steelhead","cured","smoked"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/fish-roe","m":[["Steelhead Trout Roe","Caviar Russe"]]},
{"n":"Vendace roe","a":"löjrom","d":"Roe of the vendace Coregonus albula, small orange eggs sold lightly salted, chilled or frozen.","t":["chilled","frozen","lightly salted"],"s":"https://swedishwild.se/en-uk/products/kalix-lojrom",
 "x":[A("Kalix löjrom PDO","Orange roe of vendace from the Bothnian Bay archipelago, EU PDO since 2010, harvested from late September.","https://en.wikipedia.org/wiki/Kalix_L%C3%B6jrom",y="2010",dt="Norrbotten, Sweden · Caviar of Kalix",a="Caviar of Kalix")],
 "m":[["Vänerlöjrom",""]]},
{"n":"Pollock roe","a":"tarako · myeongran · mentaiko","d":"Roe of Alaska pollock Gadus chalcogrammus, sold as salted or seasoned whole sacs.","t":["plain salted (tarako)","chilli-marinated (mentaiko)","whole sacs"],"s":"https://www.weee.com/en/product/DEOKHWA-Seasoned-Pollock-Roe-Spicy-115g-/2816522",
 "x":[A("Hakata karashi mentaiko","Pollock roe marinated in chilli, first sold in Nakasu, Hakata in 1949 by Fukuya, and now a Fukuoka speciality.","https://www.crossroadfukuoka.jp/en/articles/mentaiko",mk="Fukuya",y="1949",dt="descends from Korean myeongnanjeot",a="karashi mentaiko",v=[{"n":"Aji no Mentaiko","mk":"Fukuya","y":"","d":"old data"}])]},
{"n":"Cod roe","a":"smoked cod roe · Kalles Kaviar · tarama base","d":"Roe of cod Gadus morhua and relatives sold whole, fresh, salted or smoked.","t":["whole","fresh","salted","hot-smoked","creamed spread"],"s":"https://www.thefishsociety.co.uk/products/hot-smoked-icelandic-cod-roe",
 "x":[A("Kalles Kaviar","Swedish tube spread of smoked, sugared and salted cod and pollock roe, introduced 1954 and made by Abba Seafood.","https://en.wikipedia.org/wiki/Kalles_Kaviar",mk="Abba",y="1954",dt="aluminium tube · Original, Mild, Light, Vegan, KRAV versions",a="Kalles")]},
{"n":"Bottarga","a":"botargo · butàriga · avgotaraxo · karasumi · grey mullet roe","d":"Salted, pressed and dried roe pouch of grey mullet or tuna, sold whole or grated.","t":["grey mullet","tuna","whole","grated","waxed"],"s":"https://www.thefishsociety.co.uk/products/sardinian-bottarga-cured-grey-mullet-roe",
 "x":[A("Bottarga di Orbetello","Grey mullet roe from the Orbetello lagoon, Tuscany, made by a 58-fisherman cooperative; a Slow Food presidium.","https://storienogastronomiche.it/?p=12834",dt="salted and dried"),
 A("Avgotaraxo Messolonghi PDO","Greek bottarga of flathead mullet caught in the Messolonghi lagoons, with PDO status.",BO,dt="Greece",a="avgotaraho"),
 A("Sicilian tuna bottarga","Bottarga made from bluefin tuna roe, the Sicilian version.",BO,dt="tuna roe",a="bottarga di tonno")],
 "m":[["Mullet bottarga and traditional fishing from the Cabras pond",""]]},
{"n":"Herring roe","a":"kazunoko","d":"Roe of herring sold separately from the fish, as whole skeins or flakes, salted or seasoned.","t":["salted","soy-dashi seasoned","skein","flakes"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/fish-egg-kazunoko",
 "x":[A("Kazunoko","Golden-yellow clumps of herring eggs, crunchy, cured in soy sauce and dashi and eaten at New Year in osechi.",FR,dt="fertility symbol")]},
{"n":"Flying-fish roe","a":"tobiko","d":"Roe of flying fish, small crunchy eggs.","t":["natural orange","dyed (wasabi, yuzu, squid ink)"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/tobiko",
 "x":[A("Tobiko","Reddish-orange eggs of 0.5 to 0.8 mm, salty-sweet and slightly smoky, often dyed.",FR,dt="sushi topping")]},
{"n":"Capelin roe","a":"masago","d":"Roe of the capelin Mallotus villosus, very small eggs sold plain or seasoned.","t":["plain","dyed","seasoned"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/masago",
 "x":[A("Masago","Smaller, softer and sandier than tobiko, often dyed and used as a cheaper substitute.",FR,dt="mixed with spicy mayonnaise")]},
{"n":"Lumpfish roe","a":"lumpsucker roe","d":"Roe of the lumpfish Cyclopterus lumpus, sold as small dyed or natural eggs.","t":["black dyed","red dyed","natural"],"s":"https://littlefarms.com/shop-by-brand/k/kaviari/lumpfish-roe-black-100g-400620","m":[["Lumpfish Roe Black","Kaviari"]]},
{"n":"Bowfin roe","a":"choupique","d":"Roe of the bowfin Amia calva, sold as black small-grain roe and often labelled caviar.","t":["black","Louisiana"],"s":"https://olmafood.com/product-category/black-caviar/bowfin-caviar/"}
]
def Bk(n,c,f,seg,kf,d,sig,s): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":[],"s":s}
B=[Bk("Fukuya","Japan","1948","Heritage manufactory","karashi mentaiko","Hakata company credited with first selling chilli-marinated pollock roe in Japan, in 1949.",["Hakata karashi mentaiko"],"https://www.crossroadfukuoka.jp/en/articles/mentaiko"),
Bk("Abba","Sweden","","Mainstream","Kalles Kaviar","Swedish seafood company making the Kalles roe spread.",["Kalles Kaviar"],"https://en.wikipedia.org/wiki/Kalles_Kaviar")]
out={"kinds":K,"brands":B,"traditions":[],"notes":"All 11 planned kinds kept; Grey mullet roe was renamed Bottarga with types mullet/tuna and whole/grated. Kalix lojrom and Fukuya mentaiko became archetypes; Vanerlojrom and the Cabras entry stay as flat models (no page retrieved). Not added for lack of a retrieved page: Yamaya, karasumi (Nagasaki), Trapani tuna bottarga (the retrieved page only names Sicily), Cabras presidium, Komochi kombu. No tradition entries."}
p='work/J2/shelves/04_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
