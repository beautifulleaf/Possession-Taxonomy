import json
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
Y=W+'Yerba_mate'; hl="https://happyluckys.com/collections/"
mate=[
 A("Argentine mate","mate argentino","Argentina is the second-largest producer (about 32-37%) and the leading brands are Taragüí, Playadito and CBSé.","","1930s Argentina overtakes Brazil",Y,[V("Taragüí","Establecimiento Las Marías","","Argentine brand of tea and yerba mate"),V("Playadito","Colonia Liebig cooperative","1932","First sold 1932; packaged as a brand in 1979"),V("CBSé","CBSé","1978","Founded in San Francisco, Córdoba; 'yerba mate compuesta' blends")],"drink: mate in gourd with bombilla"),
 A("Brazilian chimarrão","chimarrão · chá mate","Hot mate served in a gourd in southern Brazil, plus roasted chá mate and toasted mate batido.","","",Y,[V("Matte Leão","","","Brazilian brand named on the page"),V("Mate batido","","","Toasted, less bitter, shaken until creamy")],"Brazil about 53-58% of production"),
 A("Paraguayan tereré","tereré","Cold mate prepared with cold water or fruit juice, served in a horn cup; Paraguay is a traditional drinking country.","","",Y,[V("Mate cocido","","","Sweetened tea-bag or loose-leaf version sold in Paraguay, Argentina and Brazil")],"cold water or juice · horn cup"),
 A("Guayakí","Guayakí","US brand named among yerba mate companies.","Guayakí","",Y,[],"organic mate"),
]
rooi=[
 A("Cederberg rooibos","red rooibos · green rooibos","Aspalathus linearis grown in the Cederberg, South Africa; the name has EU PDO status since May 2021.","","2021 PDO; 1930 commercial trials",W+'Rooibos',[V("Pieter Nortier trials","","1930","Commercial cultivation trials in Clanwilliam"),V("Green rooibos","","","Unoxidised, malty and grassy"),V("Red rooibos","","","Oxidised, reddish-brown")],"grade: leaf-to-stem ratio · type: red, green"),
]
hb=[
 A("Honeybush","Cyclopia","Sweeter red-tea relative of rooibos from Cyclopia species, graded Super Fine, Regular Fine or Coarse.","","",W+'Cyclopia_(plant)',[V("Cyclopia intermedia (bergtee)"),V("Cyclopia genistoides (kustee)"),V("Cyclopia maculata"),V("Cyclopia sessiliflora"),V("Cyclopia subternata (vleitee)")],"species: C. intermedia, genistoides, maculata, sessiliflora, subternata"),
]
gu=[A("Ecuadorian guayusa","Ilex guayusa","Caffeinated holly leaves (1.7-3.5% caffeine) grown mainly in Napo and Pastaza, Ecuador, and drunk daily by the Kichwa.","","",W+'Ilex_guayusa',[],"native upper Amazon, 200-2,000 m")]
kv=[
 A("Vanuatu noble kava","noble kava","Noble cultivars (Borogu, Melomelo, Palarasul) are the only kava allowed for export from Vanuatu, aged at least five years and organically farmed.","","",W+'Kava',[V("Borogu"),V("Melomelo"),V("Palarasul")],"noble vs tudei · root age 5+ years"),
 A("Hawaiian 'awa","'awa","Hawaiian kava cultivars include Mahakea, Moʻi, Hiwa and Nene; Moʻi was reserved for royalty.","","",W+'Kava',[V("Mahakea"),V("Moʻi"),V("Hiwa"),V("Nene")],"cultivar"),
 A("Fiji waka","waka grade","Fijian kava grade made only from lateral roots.","","",W+'Kava',[],"root: lateral (waka)"),
]
kinds=[
 {"n":"Yerba mate","a":"mate · chimarrão · tereré","d":"Dried, usually aged leaves and stems of Ilex paraguariensis sold for infusion.","t":["con palo","despalada","barbacuá smoke-dried"],"s":hl+"yerba-mate","m":[["Taragui Sin Palo","Taragui"]],"x":mate},
 {"n":"Rooibos","a":"red bush tea","d":"Dried, usually oxidised leaves and stems of Aspalathus linearis sold for infusion.","t":["red","green","super grade","long cut"],"s":hl+"rooibos","x":rooi},
 {"n":"Honeybush","a":"","d":"Dried, usually oxidised leaves and stems of Cyclopia sold for infusion.","s":hl+"rooibos","x":hb},
 {"n":"Guayusa","a":"","d":"Dried leaves of Ilex guayusa sold for infusion.","s":hl+"yerba-mate","x":gu},
 {"n":"Kava","a":"kava root powder · awa","d":"Ground root of Piper methysticum sold to prepare as a drink.","t":["noble","tudei","root powder","micronised"],"s":"https://www.mountainroseherbs.com/products/kava-kava-root-powder/profile","x":kv},
]
B=lambda n,c,f,seg,kf,d,s,**k: dict({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s},**k)
brands=[
 B("Taragüí","Argentina","","Mainstream","yerba mate","Argentine brand of tea and yerba mate, owned by Establecimiento Las Marías.",W+'Tarag%C3%BCi'),
 B("Playadito","Argentina","1932","Mainstream","yerba mate","Brand of the Colonia Liebig cooperative, first sold in 1932.",W+'Playadito'),
 B("CBSé","Argentina","1978","Mainstream","compound yerba mate","Argentine yerba mate company founded by Florentino Orquera and María Amelia Elizagaray.",W+'CBS%C3%A9'),
 B("Guayakí","United States","","Specialist","organic mate","Yerba mate company named on the Wikipedia yerba mate page.",W+'Yerba_mate'),
 B("Freshpak","South Africa","","Mainstream","rooibos","South African rooibos brand.","knowledge"),
 B("Runa","Ecuador","","Specialist","guayusa","Guayusa brand.","knowledge"),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Left out unsourced: Rosamonte, Cruz de Malta, La Merced, Canarias, Baldo, Sara, Pajarito, Kurupi, Selecta, Barao brand stubs; Uruguayan despalada style and barbacua (not on retrieved page; kept as t types from old data); Carmien and Red Espresso; Tonga kava (no detail); Fiji lawena. Mate gourds and bombillas are equipment (not here). Guayusa and Honeybush are kind-level with one archetype."}
json.dump(out,open('02_02.src.json','w'),ensure_ascii=False)
