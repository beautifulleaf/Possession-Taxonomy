import json,os
def A(n,d,s,mk="",y="",dt="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=v
    return x
PH="https://en.wikipedia.org/wiki/Pickled_herring"
K=[
{"n":"Tinned anchovies","a":"anchoas · anchois · alici · salted anchovies","d":"Salt-cured anchovy fillets or whole anchovies packed in oil or salt in a sealed tin or jar.",
 "t":["fillets in olive oil","whole","salt-packed in jars","in butter","spicy","semi-preserved (chilled)"],
 "s":"https://alltinned.com/fish-types/2",
 "x":[
 A("Anchoas de Santoña","Cantabrian anchovies cleaned, salted and cured at least six months, then filleted and packed in olive oil; semi-preserved and kept chilled.","https://www.foodswinesfromspain.com/en/food/products/preserves/anchovies-from-santona",dt="fillets 9 to 12 cm · anchovies, olive oil and salt only",a="Anchoa del Cantábrico"),
 A("Ortiz anchovies","Anchovies became the Ondarroa house's signature product in the early 20th century and opened Italian export markets.","https://www.conservasortiz.com/en/?p=5892",mk="Ortiz",y="1891")
 ],
 "m":[["Anchoas en Mantequilla Picante","Anchoas Hazas"],["Carmelo Santoña anchovies","Carmelo"],["Connétable Anchois entiers huile d'olive","Chancerelle"],["Anchovy Fillets in Olive Oil \"La Castreña\"","Conservera Castreña"],["Olasagasti Anchovies San Sebastián style Bocarte","Olasagasti"],["Olasagasti Cantabrian anchovies","Olasagasti"],["Olasagasti Large Cantabrian anchovies","Olasagasti"],["Zallo Cantabrian anchovies","Zallo"],["Zallo Large Cantabrian anchovies","Zallo"],["Acciughe sotto sale del Mar Ligure PGI",""],["Alici di menaica",""],["Anchois de Collioure PGI",""],["Magghia Masculina",""]]},
{"n":"Marinated herring","a":"rollmops · Bismarck herring · matjes · inlagd sill · soused herring","d":"Herring marinated in vinegar, oil or a sauce and sold in a jar or tub.",
 "t":["in vinegar","in wine sauce","in cream sauce","mustard","fillets","rolled"],
 "s":"https://www.thefishsociety.co.uk/collections/smoked-cured",
 "x":[
 A("Rollmops","Pickled herring fillets rolled around onion and gherkin; a 19th-century German specialty associated with Berlin.","https://en.wikipedia.org/wiki/Rollmops",dt="jars or tubs, skewered"),
 A("Bismarck herring","German common name for vinegar-pickled herring fillets, served flat; several theories link it to Otto von Bismarck.",PH,dt="flat fillets"),
 A("Matjes","Dutch soused herring, a mild salt herring from young immature fish ripened in brine.",PH,dt="maatjesharing",a="soused herring · maatjes")
 ]},
{"n":"Marinated anchovies","a":"boquerones · boquerones en vinagre","d":"Raw anchovy fillets marinated in vinegar, oil and garlic, sold chilled in a tray or jar.","t":["in vinegar","in oil and garlic","chilled","frozen first"],"s":"https://www.thefishsociety.co.uk/products/boquerones-marinated-anchovy-fillets",
 "x":[A("Boquerones en vinagre","Spanish tapa of fresh white anchovies marinated in vinegar, or vinegar and olive oil, with garlic and parsley.","https://en.wikipedia.org/wiki/Boquerones_en_vinagre",dt="served cold · traditional marinade 3 hours in brine, 6 in vinegar")]},
{"n":"Vinegar-marinated sea bream","a":"sasazuke · kodai sasazuke","d":"Small sea bream fillets salted, then marinated in vinegar and sold chilled in a tub or tray.","t":["barrelled","chilled"],"s":"https://www.maff.go.jp/j/shokusan/gi_act/register/0045/index.html",
 "x":[A("若狭小浜小鯛ささ漬","Small Sea of Japan sea bream fillets lightly salted and cured in vinegar, packed in barrels; Japanese GI registered 10 November 2017.","https://www.maff.go.jp/j/shokusan/gi_act/register/0045/index.html",y="2017",dt="bright pink skin · translucent firm flesh",a="Wakasa Obama kodai sasazuke GI")]}
]
T=[{"n":"Santoña anchovy salting","g":"Food & drink","r":"Cantabria, Spain","p":"19th century onward","d":"Salt-curing of spring-caught Cantabrian anchovies for at least six months before filleting and packing in olive oil.","tech":"clean, salt, cure six months or more, wash, fillet by hand, pack in olive oil","mat":"anchovies, salt, olive oil","forms":["Anchoas de Santoña","Anchoa del Cantábrico"],"ctr":["Santoña","Laredo","Ondarroa"],"auth":"fillets firm but flexible, 9 to 12 cm, only anchovies, olive oil and salt; kept chilled","s":"https://www.foodswinesfromspain.com/en/food/products/preserves/anchovies-from-santona"}]
out={"kinds":K,"brands":[],"traditions":T,"notes":"Rollmops and the Wakasa Obama names became archetypes (removed from flat models). Santona anchovy tradition added; the PGI status of Anchoa del Cantabrico is disputed in sources so not claimed. Not added for lack of a retrieved page: Don Bocarte, Nardin, Codesa, Conservas Emilia, Agostino Recca, Scalia, Cetara (colatura di alici PDO page retrieved but it is a fish sauce, off this shelf), Abba, Klaedesholmen (the pickled herring page does not mention them). Italian and French PGI anchovy names kept as flat models from old data."}
p='work/J2/shelves/03_02.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
