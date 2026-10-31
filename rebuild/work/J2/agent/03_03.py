import json,os
def A(n,d,s,mk="",y="",dt="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=v
    return x
SV="https://tienda.com/blogs/press/saveur-magazine-briny-bites"
BM="https://www.barcelona-metropolitan.com/api/amp/eating-and-drinking/spains-cult-of-canned-fish/"
K=[
{"n":"Tinned mussels","a":"mejillones · moules · escabeche mussels","d":"Cooked mussels packed in a sealed tin or jar, in brine, oil or sauce.","t":["in escabeche","in brine","in olive oil","smoked","spicy"],"s":"https://alltinned.com/fish-types/11",
 "x":[A("Galician mussels in escabeche","Mussels marinated in escabeche in the Galician tradition, packed by the Rías houses.",SV,dt="escabeche",v=[{"n":"Ramón Peña Galician mussels in escabeche","mk":"Ramón Peña","y":"","d":"old data"},{"n":"Los Peperetes Galician mussels in escabeche","mk":"Los Peperetes","y":"","d":"old data"}])],
 "m":[["Choritos Angelmo en Aceite","Angelmo"],["Carmelo Spicy mussels with garlic and chilli","Carmelo"],["Hevva! Cornish mussels","Hevva"],["Lucky Star Smoked Mussels","Lucky Star"]]},
{"n":"Tinned cockles","a":"berberechos · coques","d":"Cockles packed in a sealed tin or jar.","t":["al natural (in brine)","in sauce","premium (small count)"],"s":"https://alltinned.com/fish-types",
 "x":[A("Espinaler berberechos","Premium cockles from the Barcelona house, traditionally eaten at the vermouth hour with Salsa Espinaler.","https://caputos.com/blog/espinaler/",mk="Espinaler",y="1896",dt="Salsa Espinaler vinegar-pepper sauce",a="Espinaler cockles")]},
{"n":"Tinned octopus","a":"pulpo · poulpe","d":"Cooked octopus packed in a sealed tin or jar.","t":["in olive oil","in paprika sauce","in salsa Gallega","with chilli and garlic"],"s":"https://alltinned.com/fish-types/9",
 "m":[["Los Peperetes Octopus with chilli and garlic","Los Peperetes"],["Papa Anzóis Octopus in extra virgin olive oil","Papa Anzóis"],["Ramón Peña Octopus in olive oil","Ramón Peña"],["Ramón Peña Octopus in paprika sauce","Ramón Peña"],["Ramón Peña Octopus in salsa Gallega","Ramón Peña"]]},
{"n":"Tinned squid","a":"calamares · chipirones · squid in ink","d":"Squid packed in a sealed tin or jar, often in its ink.","t":["in ink","in olive oil","baby squid (chipirones)"],"s":"https://alltinned.com/fish-types/10","m":[["Ramón Peña Squid in olive oil","Ramón Peña"],["Real Conservera Española Squid in ink sauce","Real Conservera Española"]]},
{"n":"Tinned razor clams","a":"navajas · couteaux","d":"Razor clams packed in a sealed tin or jar.","t":["in brine","with chilli and garlic","in olive oil"],"s":"https://alltinned.com/fish-types",
 "x":[A("Navajas de Finisterre","Galician razor clams hand-harvested by divers and canned in brine.",BM,dt="hand-harvested by divers"),],
 "m":[["Los Peperetes Razor clams in brine","Los Peperetes"],["Los Peperetes Razor clams with chilli and garlic","Los Peperetes"],["Ramón Peña Razor clams in brine","Ramón Peña"],["Real Conservera Española Razor clams in brine","Real Conservera Española"]]},
{"n":"Tinned clams","a":"almejas · machas","d":"Clams packed in a sealed tin or jar.","t":["in brine","al natural","in sauce"],"s":"https://alltinned.com/fish-types","m":[["Machas en Agua Angelmo","Angelmo"],["Ramón Peña Galician clams in brine","Ramón Peña"],["San José Almejas al Natural","San José"]]},
{"n":"Tinned scallops","a":"zamburiñas · vieiras · noix de St Jacques","d":"Scallops packed in a sealed tin or jar.","t":["in salsa","natural","zamburiñas (queen scallops)"],"s":"https://alltinned.com/fish-types",
 "x":[A("Zamburiñas in salsa","Galician queen scallops canned in a stewed sauce.",BM,dt="Galicia",a="zamburiñas")],
 "m":[["Carmelo Scallops in salsa","Carmelo"],["Connétable Noix de St Jacques au naturel","Chancerelle"],["Ramón Peña Stewed scallops in salsa","Ramón Peña"]]},
{"n":"Tinned oysters","a":"smoked oysters","d":"Oysters, often smoked, packed in oil or water in a sealed tin.","t":["smoked","in oil","in water","with chilli"],"s":"https://en.wikipedia.org/wiki/Bevans_Oyster_Company",
 "x":[A("Bevans canned oysters","Canned and jarred oysters from a Virginia family oyster farm founded in 1966.","https://en.wikipedia.org/wiki/Bevans_Oyster_Company",mk="Bevans Oyster Company",y="1966"),
  A("Chicken of the Sea oysters","Canned oysters in the range of the American brand that also sells crab, clams and sardines.","https://en.wikipedia.org/wiki/Chicken_of_the_Sea",mk="Chicken of the Sea",y="1914")]},
{"n":"Tinned crab meat","a":"crabmeat · carne de cangrejo","d":"Crab meat packed in a sealed tin or jar.","t":["snow crab","white","lump","claw"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/crab-meat-in-can","m":[["Los Peperetes Crab meat","Los Peperetes"],["Los Peperetes Snow crab","Los Peperetes"],["Japanese Snow Crab Canned Crab Meat","Maruha Nichiro Corporation"]]},
{"n":"Tinned abalone","a":"paua","d":"Abalone (Haliotis, including paua) cooked and packed in a sealed tin.","t":["paua","in brine","in sauce"],"s":"https://www.paua.org.nz/markets-export"},
{"n":"Tinned whelk or conch","a":"golbaengi · moon snail","d":"Sea snails (whelk, conch) cooked and packed in a sealed tin.","t":["in brine","seasoned"],"s":"https://shillamarket.com/products/canned-whelk-400g-e",
 "x":[A("Golbaengi","Korean canned whelk, precooked in brine and used for golbaengi-muchim, a spicy snail salad eaten as anju.","https://en.wikipedia.org/wiki/Golbaengi-muchim",dt="served with somyeon noodles",a="canned whelk")]}
]
def Bk(n,c,f,seg,kf,d,sig,s): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":[],"s":s}
B=[
Bk("Espinaler","Spain","1896","Premium","cockles and vermouth","Barcelona-area tavern turned maker of premium Galician-sourced preserved seafood and Salsa Espinaler.",["Espinaler berberechos"],"https://caputos.com/blog/espinaler/"),
Bk("Chicken of the Sea","United States","1914","Mainstream","canned tuna and shellfish","American seafood brand started by Gilbert Van Camp, owned by Thai Union.",["Chicken of the Sea oysters"],"https://en.wikipedia.org/wiki/Chicken_of_the_Sea"),
Bk("Bevans Oyster Company","United States","1966","Specialist","canned oysters","Virginia oyster farm with its own cannery.",["Bevans canned oysters"],"https://en.wikipedia.org/wiki/Bevans_Oyster_Company"),
Bk("Los Peperetes","Spain","","Premium","Galician shellfish tins","Galician brand making tinned seafood from the estuaries.",[],"https://tienda.com/blogs/press/saveur-magazine-briny-bites"),
Bk("Conservas de Cambados","Spain","","Premium","Ría de Arousa shellfish","Producer of mussels in escabeche and other Ría de Arousa shellfish.",[],"https://tienda.com/blogs/press/saveur-magazine-briny-bites")]
out={"kinds":K,"brands":B,"traditions":[],"notes":"All 11 planned kinds kept; models trimmed only where over 20 (none). Archetypes added where a page was retrieved. Not added for lack of a retrieved page: Gueyu Mar, Crown Prince / Lucky Star smoked oysters, Yumdong (the Korean whelk archetype cites the general golbaengi dish page, not Yumdong), Real Conservera Espanola, Angelmo. Tinned abalone, crab meat, squid and octopus have flat models or none."}
p='work/J2/shelves/03_03.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
