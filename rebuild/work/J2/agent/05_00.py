import json,os
def A(n,d,s,mk="",y="",dt="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=v
    return x
FF="https://en.wikipedia.org/wiki/Fermented_fish"
SH="https://en.wikipedia.org/wiki/Soused_herring"
MO="https://www.foodswinesfromspain.com/en/food/products/preserves/mojama-de-isla-cristina-pgi---mojama-de-barbate-pgi"
K=[
{"n":"Salt cod","a":"bacalhau · bacalao · baccalà · klippfisk · morue salée","d":"Cod preserved by salting and drying, sold to be soaked and cooked.","t":["Atlantic cod","Pacific cod","Greenland cod","whole","loins","tails","grade by weight"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/salted-cod-fish",
 "x":[A("Bacalhau de Cura Tradicional Portuguesa TSG","Portuguese traditional-cure salt cod protected as a TSG; graded by weight from Especial over 4 kg to Miúdo under 500 g.","https://en.wikipedia.org/wiki/Bacalhau",dt="TSG protects the method, not the origin of the fish",v=[{"n":"Especial","mk":"","y":"","d":"over 4 kg"},{"n":"Graúdo","mk":"","y":"","d":"4 to 2 kg"},{"n":"Crescido","mk":"","y":"","d":"2 to 1 kg"},{"n":"Corrente","mk":"","y":"","d":"1 to 0.5 kg"},{"n":"Miúdo","mk":"","y":"","d":"under 500 g"}])],
 "m":[["Møre og Romsdal Salted Cod",""]]},
{"n":"Stockfish","a":"tørrfisk · stoccafisso · Stockfisch · air-dried cod","d":"Unsalted cod air-dried on racks for about three months, the base of lutefisk.","t":["Lofoten skrei","Ragno","Westre","Lub","for lutefisk"],"s":"https://visitlofoten.com/en/topic/lofoten-food/skrei-and-stockfish/",
 "x":[A("Tørrfisk fra Lofoten PGI","Skrei landed in Lofoten or Vesterålen and air-dried in Lofoten; Norwegian protection 2007, EU PGI 2014, the first Norwegian EU-certified product.","https://visitlofoten.com/en/topic/lofoten-food/skrei-and-stockfish/",y="2014",dt="over 20 quality grades · about 75% water lost",a="Stockfish from Lofoten",v=[{"n":"Lub","mk":"","y":"","d":"grade name from Hanseatic trade"},{"n":"Ragno","mk":"","y":"","d":"grade name"},{"n":"Westre Ancona","mk":"","y":"","d":"grade name"},{"n":"Italia Grande","mk":"","y":"","d":"grade name"}])]},
{"n":"Salted herring & matjes","a":"matjes · maatjes · Hollandse Nieuwe · salt herring","d":"Herring cured in brine or salt and sold chilled, to be eaten as the fish itself.","t":["matjes","salted","fillet","barrel","frozen first (Anisakis rule)"],"s":"https://www.knuspr.de/91236-matjes-fillet",
 "x":[A("Glückstädter Matjes PGI","Matjes herring from Glückstadt, Schleswig-Holstein, with PGI status.",SH,dt="brined about five days in oak casks"),
 A("Hollandse Nieuwe","Dutch new herring, a mild matjes from immature fish; Hollandse Nieuwe, Holländischer Matjes and Hollandse maatjesharing are EU TSGs.",SH,dt="caught late May to early July at over 15% oil",a="Hollandse maatjesharing")]},
{"n":"Mojama","a":"salt-dried tuna loin","d":"Tuna loin salted and air-dried, sold whole or sliced; protected regional makes such as Mojama de Barbate are included.","t":["Extra","Primera","whole piece","sliced","in olive oil"],"s":"https://www.gourmets.net/salon-gourmets/2024/catalogo-expositores/ahumados-conservas-y-salazones-la-chanca",
 "x":[A("Mojama de Isla Cristina PGI","Salt-cured wild tuna loin from the Gulf of Cádiz coast, from yellowfin or bluefin over 200 kg.",MO,dt="Extra from the lean loin near the spine · Primera from the fattier outer loin",v=[{"n":"Categoría Extra","mk":"","y":"","d":"leanest cut"},{"n":"Categoría Primera","mk":"","y":"","d":"fattier cut"}]),
 A("Mojama de Barbate PGI","Mojama made in Barbate and La Janda, Cádiz, to the same tuna and grade rules.",MO,dt="Cádiz, Andalusia")]},
{"n":"Fermented fish","a":"surströmming · rakfisk · hákarl · funazushi · kusaya","d":"Whole fish preserved by controlled fermentation and eaten as the fish itself, not as a paste or sauce.","t":["canned","barrelled","dried","with rice"],"s":FF,
 "x":[A("Surströmming","Lightly salted Baltic herring from northern Sweden that goes on fermenting in the sealed tin; sales open on the third Thursday of August.","https://en.wikipedia.org/wiki/Surstr%C3%B6mming",dt="canned from early July · tin bulges",v=[]),
 A("Rakfisk","Norwegian fermented trout.",FF,dt="Norway"),
 A("Hákarl","Icelandic fermented and dried shark.",FF,dt="Iceland"),
 A("Funazushi","Japanese freshwater fish packed in salt and rice and fermented for years.",FF,dt="Lake Biwa area",a="narezushi"),
 A("Kusaya","Pungent salted and dried fish of the Izu Islands with a strong smell but mild flavour.",FF,dt="Izu Islands, Japan")]},
{"n":"Salted fermented seafood","a":"jeotgal · shiokara · bagoong · pla ra · saeujeot","d":"Whole or cut seafood preserved by salting and fermenting and eaten as the seafood itself; a paste or sauce is in Pantry Staples.","t":["fish","shrimp","squid","roe","paste form"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/fermented-salted-shrimp",
 "x":[A("Jeotgal","Korean salted, fermented seafood, solid side dishes or the liquid aekjeot used in kimchi.",FF,dt="Korea",a="saeujeot · myeongnanjeot"),
 A("Bagoong","Philippine salted fish or shrimp paste fermented 30 to 90 days.",FF,dt="Philippines"),
 A("Pla ra","Thai salt-fermented freshwater fish.",FF,dt="Thailand"),
 A("Shiokara","Japanese salted and fermented seafood, kept in the shape of the fish or as paste.",FF,dt="Japan")]}
]
T=[
{"n":"Bacalhau","g":"Food & drink","r":"Portugal, with fish from Norway and Iceland","p":"500 years or more","d":"Dry-salted cod, a Portuguese staple adopted from Basque salting off Newfoundland.","tech":"cod gutted, salted and air-dried","mat":"Gadus morhua and relatives, salt","forms":["Bacalhau de Cura Tradicional Portuguesa","Salt cod loins"],"ctr":["Portugal","Norway","Iceland"],"auth":"TSG label Bacalhau de Cura Tradicional Portuguesa","s":"https://en.wikipedia.org/wiki/Bacalhau"},
{"n":"Lofoten stockfish","g":"Food & drink","r":"Lofoten and Vesterålen, Norway","p":"Viking age onward","d":"Skrei hung to dry outdoors for about three months, Norway's oldest food export still traded.","tech":"open-air racks, cold wind, then sorting into 20-plus grades","mat":"skrei (spawning Arctic cod)","forms":["Stockfish","Lutefisk base"],"ctr":["Lofoten","Bergen (Bryggen)"],"auth":"Tørrfisk fra Lofoten PGI","s":"https://visitlofoten.com/en/topic/lofoten-food/skrei-and-stockfish/"},
{"n":"Surströmming","g":"Food & drink","r":"High Coast, northern Sweden","p":"since at least the 16th century","d":"Baltic herring brined then canned to ferment further, sold from the third Thursday of August.","tech":"caught May and June, brined, headed and gutted, barrelled at 15 to 18 C, canned early July","mat":"Baltic herring, salt","forms":["Surströmming tin"],"ctr":["Ulvön and the High Coast"],"auth":"sale date and tin fermentation","s":"https://en.wikipedia.org/wiki/Surstr%C3%B6mming"}]
out={"kinds":K,"brands":[],"traditions":T,"notes":"Added Stockfish and Fermented fish kinds. Bacalhau TSG and Glueckstaedter Matjes became archetypes (removed from flat models); the old 'Matjes (maatjes) herring' model merged into the Hollandse Nieuwe archetype. Not added for lack of a retrieved page: klippfisk Moere og Romsdal (kept as a model); Roeda Ulven, Oskars (surstroemming page does not name them), Valdres rakfisk PGI, hakarl and kusaya details beyond the fermented fish page, jeotgal subtypes, Tradition entry for klippfisk."}
p='work/J2/shelves/05_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
