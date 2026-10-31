import json
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
T=W+'Theobroma_cacao'; CB=W+'Cocoa_bean'
beans=[
 A("Criollo","","Traditionally the most prized and rarest cacao group; one of Motamayor's ten genetic clusters (2008).","","2008 genetic grouping",T,[],"group: Criollo · rare"),
 A("Forastero (Amelonado)","Amelonado","Basis of most commercial chocolate; Amelonado is its main variety and is also one of the ten genetic groups.","","",T,[],"group: Amelonado · West Africa"),
 A("Trinitario","","Any hybrid of Criollo and Forastero; Wikipedia treats Forastero and Trinitario as geohistorical rather than botanical categories.","","",CB,[],"hybrid"),
 A("Nacional (Arriba)","Nacional","Cacao linked to the Iquitos area of Peru and Ecuador, one of the ten genetic groups.","","",T,[],"group: Nacional · Ecuador"),
 A("Chuao (Venezuela)","Cacao de Chuao","Cacao from Chuao, Venezuela, granted an appellation of origin in November 2000.","","2000",T,[],"appellation 2000"),
 A("Motamayor ten genetic groups","Amelonado · Contamana · Criollo · Curaray · Guiana · Iquitos · Marañon · Nacional · Nanay · Purús","Ten groups proposed in 2008 from morphology, geography and genomics.","Motamayor et al.","2008",T,[V("Marañon"),V("Contamana"),V("Curaray"),V("Iquitos"),V("Nanay"),V("Purús"),V("Guiana")],"classification"),
]
kinds=[
 {"n":"Cacao beans","a":"cocoa beans","d":"Whole cacao beans, raw, fermented and dried, or roasted.","t":["raw","fermented and dried","roasted"],"s":"https://thechocolatelife.com/fs-cocoa-beans-from-trinidad.md","x":beans},
 {"n":"Cocoa paste & ceremonial cacao","a":"cocoa mass · cocoa liquor · ceremonial cacao","d":"Ground cocoa nibs set in a block or drops (cocoa liquor, ceremonial cacao); couverture and baking chocolate are in Pantry Staples.","t":["block","drops"],"s":"https://www.soulliftcacao.com/products/rukux-ulew-cacao-paste-block-ceremonial-cacao-guatemalan-family-farmed-ethical-direct-trade","m":[["Ruk'u'x Ulew (Heart of the Earth) ceremonial cacao","Soul Lift Cacao"]]},
 {"n":"Cocoa nibs","a":"cacao nibs","d":"Cocoa beans cracked and shelled into pieces, raw or roasted.","t":["raw","roasted"],"s":"https://www.cacaoculture.ph/blogs/news/cacao-culture-on-the-vegan-grocer-1"},
 {"n":"Cocoa butter","a":"theobroma oil","d":"The fat pressed from cocoa paste, about 54-58% of the nib.","t":["natural","deodorised"],"s":"https://www.floraandfauna.com.au/collections/power-super-foods.oembed"},
 {"n":"Cocoa shells","a":"cocoa husks · cacao husk tea","d":"The shell of the cocoa bean, sold for infusion.","s":"https://soulliftcacao.com/collections/other-goods/products/cacao-husk-tea-1-2lb-bag","m":[["Cacao Husk Tea","Soul Lift Cacao"]]},
]
B=lambda n,c,f,seg,kf,d,s,**k: dict({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s},**k)
brands=[B("Soul Lift Cacao","","","Specialist","ceremonial cacao","Seller of Guatemalan family-farmed ceremonial cacao paste and cacao husk tea.","knowledge")]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Left out unsourced: Porcelana, Ocumare, Piura white bean, Madagascar Sambirano, CCN-51 (not on retrieved pages), Heirloom Cacao Preservation designations, Keith's Cacao, Ora, Mesoamerican cacao tradition entry (no dedicated page retrieved). Ceremonial paste, nibs, butter and shells kept at kind level from old data. Cacao Husk Tea model name taken from the old source URL slug."}
json.dump(out,open('03_01.src.json','w'),ensure_ascii=False)
