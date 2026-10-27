import json,os
def A(n,d,s,mk="",y="",dt="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=v
    return x
DB="https://www.maff.go.jp/e/policies/market/dento_syoku/menu/dried_bonito.html"
AP="https://en.wikipedia.org/wiki/Alaska_pollock_as_food"
K=[
{"n":"Katsuobushi","a":"dried bonito · bonito flakes · 鰹節","d":"Skipjack tuna boiled, smoked and dried hard, sold as whole blocks or shaved flakes.","t":["block","kezuribushi (shaved flakes)","arabushi","karebushi","honkarebushi"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/bonito-flakes-katsuobushi",
 "x":[A("Honkarebushi","Highest grade of katsuobushi, moulded several times and matured four to six months.",DB,dt="surface shaved before each mould",a="本枯節"),
 A("Arabushi","Basic boiled and smoked skipjack before any mould is applied; shaved arabushi is hadakabushi.",DB,dt="boiled and smoked",a="荒節"),
 A("Karebushi","Katsuobushi with added mould, more common in Kanto.",DB,dt="mould-ripened",a="枯節"),
 A("Makurazaki katsuobushi GI","Katsuobushi of Makurazaki, Kagoshima, Japan's largest producer; GI no. 168 registered 18 March 2025.","https://www.maff.go.jp/j/shokusan/gi_act/register/0168/index.html",y="2025",dt="over 300 years of history · oak and chestnut smoke",a="枕崎鰹節")]},
{"n":"Niboshi","a":"iriko · myeolchi · ikan bilis · dried anchovies · dried sardines","d":"Small boiled and dried fish, mostly anchovies, for stock and snacks.","t":["anchovy","sardine","round herring","sand lance","for dashi","snack"],"s":"https://en.wikipedia.org/wiki/Niboshi",
 "x":[A("Iriko","Western Japanese name for niboshi, the base of miso soup dashi and eaten at New Year as tazukuri.","https://en.wikipedia.org/wiki/Niboshi",dt="mostly Japanese anchovy",a="niboshi")]},
{"n":"Dried pollock","a":"hwangtae · bugeo · kodari · myeongtae","d":"Alaska pollock dried in Korea: hwangtae by winter freeze-thaw, bugeo, and half-dried kodari.","t":["hwangtae","bugeo","kodari","whole","shredded"],"s":AP,
 "x":[A("Hwangtae","Korean pollock dried over winter by natural freeze-thaw cycles, used in hangover soup, grilled and simmered dishes.",AP,dt="yellow pollock",a="yellow pollock"),
 A("Bugeo","Dried pollock used for clear soup (bugeo-guk) and jerky.",AP,dt="Korea")]},
{"n":"Dried filefish","a":"jwipo","d":"Filefish (Monacanthidae) fillets dried, plain or lightly seasoned and pressed, sold to eat or to grill.","t":["plain","seasoned","shredded"],"s":"https://www.accessdata.fda.gov/cms_ia/importalert_49.html"},
{"n":"Dried rockfish","a":"geonureok","d":"Rockfish (Sebastes) salted and dried or half-dried, sold whole to grill or steam; raw rockfish is Rockfish.","t":["whole","half-dried"],"s":"https://www.nfqs.go.kr/hpmg/data/actionMarineGeographicForm.do?menuId=M0000230","m":[["Shinan dried rockfish",""]]},
{"n":"Fish maw","a":"swim bladder · fish sound","d":"Dried swim bladder of croaker, sturgeon or other fish, sold for rehydrating and cooking.","t":["croaker","cod","sturgeon","totoaba (restricted)","dried","fried"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/fish-maw"},
{"n":"Fish floss","a":"yu song · yú sōng","d":"Fish cooked, shredded and dry-fried with light seasoning into a fine dry floss; a blend led by seaweed, sesame or flour is a topping in Pantry Staples.","t":["Jiangsu dry-cooked","Fujian fried"],"s":"https://www.sfda.gov.sa/sites/default/files/2020-11/Taiwan-fish.pdf"},
{"n":"Dried shark fin","a":"","d":"Shark fin dried for rehydrating and cooking; trade is restricted for CITES-listed species and finning is banned in some regions.","t":["whole","needles (processed)"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/shark-fin"}
]
out={"kinds":K,"brands":[],"traditions":[],"notes":"All 8 planned kinds kept. Makurazaki katsuobushi GI and honkarebushi became archetypes (old duplicates removed). Shinan dried rockfish kept once as a flat model (GI name duplicate dropped). Niboshi and Dried pollock are new kinds. Shark fin has no models; the trade-ban note is from a search snippet about the 2013 CITES decision (the NPR page returned an error) and is kept general. Not added for lack of a retrieved page: Yaizu, Yongdae-ri hwangtae (seller pages only), myeolchi and ikan bilis as separate archetypes (kept as aliases), fish maw/floss archetypes."}
p='work/J2/shelves/05_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
