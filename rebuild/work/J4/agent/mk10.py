import sys;sys.path.insert(0,'work/J4/agent')
from lib import *
BA=[x("Gros Michel","","1835",W+"Gros_Michel","Thick-skinned AAA banana that was the main export banana until the 1950s, when Panama disease wiped it out.",[]),
 x("Cavendish","","c.1834",W+"Cavendish_banana","Triploid AAA subgroup that replaced Gros Michel and makes up most traded bananas; named after the Duke of Devonshire.",
   [v("Grand Nain","","","Grande Naine, the most important clone in trade and the Chiquita banana"),v("Dwarf Cavendish","","","Most widely grown clone"),
    v("Giant Cavendish (Williams)","","","Group including Williams"),v("Plátano de Canarias PGI","","","Cavendish grown in the Canary Islands, speckled skin, EU PGI"),
    v("Cavendish Zelig","","","Old-data entry")],a="Grand Nain · Williams"),
 x("Lady Finger","","",W+"Banana","Small sweet AAB banana, also sold as sugar banana.",[v("Lady Finger (Sugar banana)","","","Old-data name")]),
 x("Red banana","","",W+"Banana","Red-skinned dessert banana.",[v("Red banana","","","Old-data name"),v("Red Dacca","","","Old-data entry")]),
 x("Apple banana","","",W+"Banana","Latundan, the apple or silk banana of Southeast Asia, shown as an apple banana on Wikipedia.",[v("Apple banana (Manzano)","","","Old-data name"),v("Latundan (Silk)","","","Old-data name")],a="Manzano · Silk · Latundan")]
PL=[x("Nendran","","",W+"Banana","True plantain widely grown in Kerala, India.",[v("Nendran","","","Old-data name"),v("Chengalikodan Nendran Banana GI","","","Old-data GI")]),
 x("Saba","","",W+"Banana","Southeast Asian cooking banana.",[v("Saba","","","Old-data name")])]
PI=[x("Smooth Cayenne","","",W+"Pineapple","The most grown pineapple, spineless and ancient, ancestor of MD-2.",[v("Smooth Cayenne (Sarawak)","","","Old-data name"),v("Hilo","","","Compact Hawaiian variant")]),
 x("MD-2","Fresh Del Monte Produce","1996",W+"Pineapple","Del Monte's 73-114 bred from Smooth Cayenne lines and launched in 1996 as Gold Extra Sweet.",
   [v("MD-2 (73-114, Gold Extra Sweet)","Fresh Del Monte Produce","1996","Breeder code 73-114"),v("Del Monte Gold [Fresh Del Monte Produce]","Fresh Del Monte Produce","","Del Monte brand"),
    v("Pinkglow [Fresh Del Monte Produce]","Fresh Del Monte Produce","2020","Pink pineapple launched October 2020")],a="Gold Extra Sweet · Del Monte Gold"),
 x("Queen","","",W+"Pineapple","Natal Queen type with golden flesh and a mild flavour, grown in Australia, Malaysia and South Africa.",[v("Natal Queen","","","Old-data name")]),
 x("Red Spanish","","",W+"Pineapple","Squarish pale-fleshed pineapple suited to shipping.",[v("Red Spanish","","","Old-data name")])]
PA=[x("Maradol","","",W+"Papaya","Large red-fleshed papaya common in US markets, grown mainly in Mexico and Belize.",[]),
 x("Sunrise","","",W+"Papaya","Large red-fleshed papaya sold in US markets.",[]),
 x("Caribbean Red","","",W+"Papaya","Large red-fleshed papaya sold in US markets.",[])]
CO=[x("Nam Hom","","",W+"Dwarf_coconut","Thai aromatic green dwarf coconut from Nakhon Pathom, sold young for its water.",[],a="Aromatic Green Dwarf")]
brands=[B("Chiquita","Switzerland","Mainstream","bananas","Banana brand tracing to 1870, named Chiquita Brands International in 1990 and now owned by Safra Group and Cutrale.",W+"Chiquita",sig=["Grand Nain"]),
 B("Fyffes","Ireland","Mainstream","bananas and tropical fruit","Banana importer founded in London in 1888 by Edward Fyffe, owned by Sumitomo since 2017.",W+"Fyffes",f="1888"),
 B("Fresh Del Monte Produce","United States","Mainstream","pineapple and bananas","Fresh fruit company created in 1989 from the Del Monte fresh fruit division, behind MD-2 pineapple and Pinkglow.",W+"Fresh_Del_Monte_Produce",f="1989",sig=["MD-2"]),
 B("Dole","United States","Mainstream","bananas and pineapple","Major US fresh fruit company selling bananas and pineapples.","knowledge")]
kinds=[
K("Banana","Fresh eating banana, organised by Gros Michel, Cavendish and other dessert groups with their protected origins.","https://plu.pro/commodity/bananas",BA,["Burro","Blue Java (Ice Cream banana)","Goldfinger","Lakatan","Mysore","Ney Poovan","Pisang Ambon","Pisang Raja","Senorita (Monkoy)","Thousand Fingers","Baby banana (Nino)","BANANO DE COSTA RICA DO","Jalgaon Banana GI","Kamalapur Red Banana GI","Robusta","Red banana"],["Cavendish","dessert","red","apple"]),
K("Plantain","Starchy cooking banana, eaten green or ripe.","https://plu.pro/commodity/bananas",PL,["French plantain","Horn plantain","Dominico","Dominico-Harton","Pisang Awak","Bluggoe","Rhino Horn","Maqueno","Pelipita","Tanduk"]),
K("Pineapple","Fresh pineapple, whole or cut.","https://plu.pro/commodity/pineapple",PI,["Ananás dos Açores/São Miguel PDO","Perola","Kona Sugarloaf","Pernambuco (Eleuthera)","Fyffes Gold [Fyffes]","Honeyglow [Fresh Del Monte Produce]","Rubyglow [Fresh Del Monte Produce]","Ban Kha pineapple GI","Vazhakulam pineapple GI","Tripura Queen Pineapple GI","フアイムン・パイナップル GI"]),
K("Papaya","Fresh papaya (Carica papaya), ripe or green; green papaya sold to cook is the same fruit.","https://www.cosmos.com.mx/producto/papaya-4lvp/",PA,None,["ripe","green","red-fleshed","yellow-fleshed"]),
K("Coconut","Fresh whole coconut, young (drinking) or mature.",W+"Coconut",CO,None,["young","mature"]),
]
kinds[0]["m"]=[m for m in kinds[0]["m"] if m[0]!="Red banana"]
notes="Banana flat list cut from 52 to archetype versions plus 15 flat models. Solo/Hawaiian, Red Lady and Tainung papaya not on retrieved pages (not archetypes). Queen Victoria (Réunion) pineapple not found. French/Horn plantain not on retrieved pages, kept as flat models. Blue Java and Pisang Raja not on retrieved pages. Dole brand from knowledge. Plátano de Canarias PGI kept as a Cavendish version; the Spanish catalogue page was not fetched (search snippet only), though the fetched foodswinesfromspain page confirms Cavendish."
urls=[W+p for p in ["Cavendish_banana","Gros_Michel","Grand_Nain","Banana","Pineapple","Papaya","Dwarf_coconut","Coconut","Chiquita","Fyffes","Fresh_Del_Monte_Produce"]]+["https://www.foodswinesfromspain.com/en/food/products/fruits---vegetables/platano-de-canarias-pgi"]
write("00_10",kinds,brands,[],notes,urls)
