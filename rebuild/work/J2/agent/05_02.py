import json,os
def A(n,d,s,mk="",y="",dt="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=v
    return x
K=[
{"n":"Dried abalone","a":"鲍鱼干 · Yoshihama · Oma · Amidori","d":"Abalone dried whole for rehydrating and cooking, sold by count per catty.","t":["Japanese","South African","by head count","golden","red"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/chinese-dried-abalone"},
{"n":"Dried sea cucumber","a":"刺参 · haishen · cishen · trepang","d":"Sea cucumber dried for rehydrating and cooking.","t":["spiny (cishen)","salted","unsalted","by size"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/seafood-sea-cucumber",
 "x":[A("Hiyama Haishen GI","Unsalted spiny dried sea cucumber from Hiyama, Hokkaido; Japanese GI no. 92, which keeps its shape when rehydrated and needs no desalting.","https://www.maff.go.jp/e/policies/intel/gi_act/register/s92.html",dt="Setana, Yakumo, Otobe, Esashi, Kaminokuni, Okushiri",a="檜山海参")]},
{"n":"Dried scallop","a":"conpoy · 干贝 · 江瑶柱 · kaibashira","d":"Scallop adductor muscle dried for eating or cooking.","t":["Japanese (Hokkaido)","Chinese (Atrina)","by size"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/dried-scallops",
 "x":[A("Hokkaido dried scallop adductor","Okhotsk coast scallop adductor muscle boiled in salted water and dried to under 16% moisture, graded by inspectors; shiraboshi dates from the Meiji period.","https://www.maff.go.jp/e/policies/market/dento_syoku/menu/dried_scallops.html",dt="scallops caught June to October · kuroboshi whole-flesh form",a="Hokkaido conpoy"),
 A("Atrina conpoy","Milder, smaller conpoy from the mainland Chinese Atrina pectinata, against stronger Japanese Mizuhopecten yessoensis.","https://en.wikipedia.org/wiki/Conpoy",dt="江珧柱")]},
{"n":"Dried oyster","a":"hao si · ho see · 蠔豉","d":"Sun-dried or semi-dried oysters, a Cantonese New Year ingredient.","t":["raw-dried","cooked then dried","by size","by origin"],"s":"https://thewoksoflife.com/dried-oyster-black-moss/",
 "x":[A("Ho see fat choy","Dried oysters stir-fried with black moss, eaten almost only at Chinese New Year in Hong Kong and South China.","https://thewoksoflife.com/dried-oyster-black-moss/",dt="graded by size, origin and whether dried raw or cooked",a="蠔豉髮菜")]},
{"n":"Dried shrimp","a":"虾米 · ebi","d":"Shrimp dried whole or shelled for eating or cooking.","t":["whole","shelled","small","large"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/ebi"},
{"n":"Dried squid & cuttlefish","a":"鱿鱼干 · surume · shredded squid","d":"Squid or cuttlefish (Sepia) dried whole, in pieces or in shreds.","t":["squid","cuttlefish","whole","shredded snack","seasoned"],"s":"https://www.weee.com/en/grocery-near-me/lang-en/explore/dried-squid"}
]
out={"kinds":K,"brands":[],"traditions":[],"notes":"Dried squid and Dried cuttlefish merged into Dried squid & cuttlefish as planned. Archetypes only where a page was retrieved: Hiyama Haishen GI (MAFF), Hokkaido dried scallop (MAFF), Atrina conpoy (Wikipedia) and ho see (Woks of Life). Not added for lack of a retrieved page: Japanese dried abalone Yoshihama/Oma/Amidori (only search snippets and a 403 HKU page), Kanto/Hokkaido dried sea cucumber lines beyond Hiyama, size count tables. Dried shrimp has no archetypes."}
p='work/J2/shelves/05_02.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(p+'.tmp',p)
