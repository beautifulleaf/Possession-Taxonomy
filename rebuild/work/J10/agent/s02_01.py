import json
W='https://en.wikipedia.org/wiki/'
LR=W+"List_of_rolling_papers"
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":mk,"y":b,"d":c} for a,b,c in v]
    return r
papers=[
x("Rizla","Rizla","1886",W+"Rizla","Original French rolling paper; standard papers are 69 x 35 mm and King Size arrived in 1977; owned by Imperial Brands since 1997.",[("Standard","","69 x 35 mm"),("King Size","1977","")]),
x("Zig-Zag","Zig-Zag","",W+"Zig-Zag_(company)","Paris brand of Maurice and Jacques Braunstein, named for its interleaved packaging invented in 1894.",[("French Orange","","Old data model")]),
x("OCB","OCB","",LR,"French brand sold by Bolloré to Republic Tobacco.",[("Premium","",""),("Organic Hemp","",""),("Virgin","",""),("X-Pert","","")]),
x("RAW","RAW","1995",W+"RAW_(rolling_papers)","Unbleached, vegan papers created in 1995 by Josh Kesselman; also sells tips, cones and machines.",[("Classic","","Standard and king size"),("Black","","Natural unbleached king size slim"),("Organic","","1 ¼ and king size slim hemp")]),
x("Smoking","Miquel y Costas","1924",W+"Smoking_(rolling_paper)","Spanish brand founded in 1924 in Capellades near Barcelona; predecessor El Pino dates to 1879.",[("King Size Slim","","")]),
x("Bambú","Miquel y Costas","",LR,"Spanish brand made by Miquel y Costas, with production now in Argentina."),
]
kinds=[
{"n":"Rolling paper","a":"rolling papers","d":"Thin paper for hand-rolling a cigarette or joint; empty blunt wraps included.","t":["Single wide","1¼","King size","King size slim","Hemp","Unbleached","Blunt wrap","Flavoured"],"s":"https://americanrollingclub.com/product-category/rolling-papers","x":papers,
 "m":[["Elements","Elements"],["Juicy Jays","Juicy Jays"]]},
{"n":"Filter tip","a":"roach · crutch","d":"Loose filter or card tip for a hand-rolled cigarette or joint.","t":["Card roach","Cotton or foam filter","Glass tip"],"s":"https://smoke-king.co.uk/products/raw-original-natural-rolling-paper-tips"},
{"n":"Rolling machine","a":"","d":"Hand device for rolling cigarettes or joints.","t":["Hand roller","Rollbox","Tube-filling machine"],"s":"https://www.smoke-king.co.uk/products/bull-brand-regular-metal-cigarette-hand-rolling-machine","m":[["Giro","Gizeh"],["Power-Roll","Top"],["Zen Rollbox","Zen"]]},
{"n":"Cigarette tube","a":"filter tube","d":"Empty filtered paper tube, 84 mm (king size) to 100 mm, filled with fine-cut tobacco by an injector.","t":["King size","100s","Cone"],"s":W+"Cigarette_tube"},
{"n":"Tube injector","a":"shooter","d":"Hand device that fills empty cigarette tubes with fine-cut tobacco.","t":["Hand injector","Crank injector","Electric machine"],"s":"https://www.eacarey.com/cigaccessories.html"},
{"n":"Rolling tray","a":"","d":"Tray made for rolling and holding material.","t":["Metal","Wood","Rubber"],"s":"https://blazysusan.com/product-category/trays/rolling-trays"},
]
def b(n,c,f,seg,kf,d,s): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
brands=[
b("Rizla","France","1886","Mainstream","rolling papers","French brand, now made in Belgium for Imperial Brands.",W+"Rizla"),
b("Zig-Zag","France","","Mainstream","interleaved papers","Paris rolling-paper house; North American rights with Turning Point Brands since 1997.",W+"Zig-Zag_(company)"),
b("OCB","France","","Mainstream","rolling papers","Former Bolloré brand now with Republic Tobacco.",LR),
b("RAW","United States","1995","Specialist","unbleached papers","Created by Josh Kesselman; based in Phoenix, Arizona.",W+"RAW_(rolling_papers)"),
b("Miquel y Costas","Spain","","Specialist","Smoking, Bambú","Spanish maker of Smoking, Bambú, Pure Hemp, Bugler and other papers.",W+"Smoking_(rolling_paper)"),
]
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":"RAW/OCB SKU list cut to versions under one archetype per brand. Gizeh, JOB, Elements papers not found on retrieved pages (Elements and Juicy Jays kept as flat models). Rolling-paper sizes (single wide, 1¼, king slim) are types per the brief, only Rizla sizes sourced."},open('s02_01.json','w'),ensure_ascii=False)
