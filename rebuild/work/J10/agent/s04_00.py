import json
W='https://en.wikipedia.org/wiki/'
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":b,"y":c,"d":e} for a,b,c,e in v]
    return r
SM="Swedish Match"
kinds=[
{"n":"Portion snus","a":"","d":"Snus in pouches, differing by whether the pouch is moist (original) or dry (white).","t":["Original portion snus","White portion snus","Mini portion"],"s":W+"Snus",
 "x":[x("Ettan","Swedish Match","1822",W+"Ettan_snus","Founded as Ljunglöf's No. 1 by Jacob Fredrik Ljunglöf; about a fifth of Swedish snus sales.",[("Ettan Original Portion","Swedish Match","","24 portions of 1.0 g"),("Ettan Vit","Swedish Match","","White portion, 24 of 0.9 g")]),
      x("Göteborgs Rapé","Swedish Match","1919",W+"G%C3%B6teborgs_Rap%C3%A9","Gothenburg recipe with juniper and herb tones, factory-made since 1919; white portion snus added in 1997.",[("White Mini Portions","Swedish Match","2005",""),("No. 2 Lingon","Swedish Match","2006","Lingonberry flavour")]),
      x("General","Swedish Match","",W+"Swedish_Match","Swedish Match's market-leading Scandinavian snus brand, sold in the US since 2009."),
      x("Siberia","","",W+"Snus","Snus whose 'Extremely Strong' variety has the highest listed nicotine content.")],
 "m":[["General Onyx","Swedish Match"]],"r":[["Ettan","Swedish Match"]]},
{"n":"Loose snus","a":"lössnus","d":"Moist, unportioned snus, often pressed into a 'pris' by hand.","t":["Fine ground","Coarse (grov)"],"s":W+"Snus",
 "x":[x("Ettan Lös","Swedish Match","1822",W+"Ettan_snus","Loose Ettan, 42 g can, 7.5 mg/g nicotine."),
      x("Grov","Swedish Match","",W+"Swedish_Match","Coarse-cut snus (Grovsnus) in Swedish Match's main brands.")],
 "m":[["Ettan Los","Swedish Match"]],"r":[["Ettan","Swedish Match"]]},
{"n":"Nicotine pouch","a":"nic pouch · white snus","d":"Tobacco-free pouch of plant fibre, nicotine (typically 1-10 mg) and flavour, placed between lip and gum.","t":["Slim","Mini","Strong"],"s":W+"Nicotine_pouch",
 "x":[x("Zyn","Swedish Match","2016",W+"Nicotine_pouch","Swedish Match pouch brand with over 70% of global share; first US sales 2016; FDA authorised 20 products in January 2025.")],
 "m":[["Velo","British American Tobacco"],["On!","Altria"]],"r":[["Nordic Spirit","Japan Tobacco"]]},
{"n":"Dissolvable nicotine product","a":"nicotine pearl · dissolvable tobacco · nicotine toothpick","d":"Product that dissolves in the mouth or delivers nicotine without burning: lozenge, orb, strip, pearl or nicotine toothpick.","t":["Dissolvable tobacco","Nicotine pearl","Nicotine toothpick"],"s":W+"List_of_tobacco_products","m":[["Camel Orbs","R.J. Reynolds"],["Ariva",""],["Stonewall",""]]},
]
brands=[{"n":"Swedish Match","c":"Sweden","f":"1868","seg":"Mainstream","kf":"snus","d":"Stockholm snus and match company; state tobacco monopoly of 1915 merged in, name adopted 1980, owned by Philip Morris International since 2022-23.","lines":["Ettan","Göteborgs Rapé","General","Grov","Catch","Zyn"],"sig":["Ettan","Zyn"],"s":W+"Swedish_Match"}]
trad=[{"n":"Swedish snus","g":"Food & drink","r":"Sweden","p":"1800s to present","d":"Moist steam-pasteurised tobacco placed under the upper lip, shifting from nasal snuff to snus by the early 1800s.","tech":"Steam pasteurisation rather than fermentation; loose or portion","mat":"Tobacco, salt, flavours","forms":["Portion snus","Loose snus"],"ctr":["Göteborgs Rapé","Ettan","General","Swedish Match"],"auth":"Sold in Sweden under the EU exemption; most other EU sales of tobacco snus are banned.","s":W+"Snus"}]
json.dump({"kinds":kinds,"brands":brands,"traditions":trad,"notes":"Catch and Röda Lacket not covered by retrieved pages, omitted. Velo and On! kept as flat models (not on retrieved pages). Camel Orbs kept: appears on List of tobacco products. Nicotine pearl is not on that page; kept as a type from the brief."},open('s04_00.json','w'),ensure_ascii=False)
