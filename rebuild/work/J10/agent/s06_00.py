import json
W='https://en.wikipedia.org/wiki/'
LT=W+"Lighter"
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":b,"y":c,"d":e} for a,b,c,e in v]
    return r
pocket=[
x("Zippo windproof","Zippo","1933",W+"Zippo","Wick-and-naphtha windproof lighter first made in early 1933 by George Blaisdell, inspired by an Austrian IMCO lighter; patent 1936; lifetime guarantee.",[("Wartime black crackle","Zippo","","World War II steel finish"),("Date-coded models","Zippo","1955","Dots from 1955, later letter and numeral codes")]),
x("Ronson Banjo","Ronson","1926",W+"Ronson_(company)","One-hand automatic lighter lighting and extinguishing with a single push; sold in 1927 as the Ronson De-Light."),
x("Dunhill butane","Dunhill","mid-1950s",W+"Alfred_Dunhill_Ltd.","One of the first butane gas lighters; design stayed largely unchanged and appeared with James Bond."),
x("S.T. Dupont","S.T. Dupont","1941",W+"S._T._Dupont","Paris house whose first serially produced lighter, in 1941, was made of aluminium."),
x("Colibri","Colibri","1928",W+"Colibri_Group","American lighter house founded by Julius Lowenthal.",[("Monopol","Colibri","1935","Fully automatic lighter"),("Stormgard","Colibri","1940","Made 1940-45 for soldiers")]),
x("Bic","Bic","1973",W+"Bic_lighter","Disposable butane lighter made by Société Bic since 1973; over 30 billion sold by February 2024."),
x("Clipper","Flamagas","1972",W+"Clipper_(lighter)","Refillable butane lighter designed by Enric Sardà, made by Flamagas (founded 1959) in Barcelona."),
]
kinds=[
{"n":"Pocket lighter","a":"","d":"Lighter carried on the person, from windproof wick lighters to disposable butane ones.","t":["Flint-wheel","Piezo","Windproof butane","Disposable","Refillable"],"s":"https://colibri.com/collections/type-lighters","x":pocket,"m":[["Heritage Pocket","Colibri"]]},
{"n":"Cigar lighter","a":"","d":"Lighter made for lighting cigars, usually a jet or torch flame.","t":["Jet/torch","Multi-jet","Soft flame"],"s":"https://colibri.com/collections/type-lighters","m":[["Daytona","Colibri"],["Trezo","Xikar"],["Maxfield Jet Flame",""]]},
{"n":"Pipe lighter","a":"","d":"Lighter with a side flame for lighting a pipe bowl.","t":["Soft flame","Inline"],"s":"https://www.smokingpipes.com/accessories/lighters","m":[["Bowl Flame","Brebbia"],["Pacific Air","Colibri"],["Old Boy","IM Corona"]]},
{"n":"Table lighter","a":"","d":"Lighter made to stand on a table.","t":["Touch-tip","Desk"],"s":"https://www.smokingpipes.com/accessories/lighters",
 "x":[x("Ronson Touch-Tip","Ronson","early 1930s",W+"Ronson_(company)","Table lighter made from the early 1930s, often in Art Deco designs.")],
 "m":[["Quasar Desk Lighter","Colibri"],["Gentry","Flaminaire"]],"r":[["Quasar","Colibri"]]},
{"n":"Electric lighter","a":"arc lighter · plasma lighter","d":"Lighter that makes an electric arc (plasma) or heats an element, rechargeable by USB, with no fuel or flint.","t":["Arc/plasma","Heating element","USB-rechargeable"],"s":LT},
{"n":"Lighter fuel, flints & wicks","a":"","d":"Consumables for lighters: naphtha (Zippo) and butane fuel, ferrocerium flints and wicks.","t":["Naphtha fuel","Butane fuel","Flints","Wicks"],"s":"https://zippo.com/products/zippo-flint-wick-co-pack","m":[["Zippo Flint/Wick Co-Pack","Zippo"]]},
]
def b(n,c,f,seg,kf,d,s,lines=None):
    r={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if lines: r["lines"]=lines
    return r
brands=[
b("Zippo","United States","1932","Heritage manufactory","windproof","Founded by George Blaisdell in Bradford, Pennsylvania; owns Ronson in North America since 2010.",W+"Zippo"),
b("Ronson","United States","1898","Heritage manufactory","Banjo, Touch-Tip","Began as Art Metal Works in Newark; bankrupt 2010, Zippo bought the North American marks.",W+"Ronson_(company)",["Banjo","Touch-Tip"]),
b("Colibri","United States","1928","Premium","lighters","Founded by Julius Lowenthal; now New York based.",W+"Colibri_Group"),
b("S.T. Dupont","France","1872","Premium","luxury lighters","Paris house founded by Simon Tissot-Dupont; lighters from 1941.",W+"S._T._Dupont"),
b("Dunhill","United Kingdom","1893","Premium","London luxury","London house; butane lighter mid-1950s; lighters were about 75% of sales by 1975.",W+"Alfred_Dunhill_Ltd."),
b("Bic","France","","Value","disposables","Maker of the disposable Bic lighter, introduced 1973.",W+"Bic_lighter"),
b("Clipper","Spain","1959","Mainstream","refillable","Refillable butane lighter of Flamagas, founded 1959.",W+"Clipper_(lighter)"),
]
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":"Dunhill Rollagas/Unique/Aquarium, Ligne 2, Maxijet, Varaflame, Queen Anne, IMCO, Cricket not on retrieved pages; omitted. Colibri cigar-lighter list trimmed to one model; Aura, Ascari etc dropped. Colibri also kept in table/pipe lighters via old models."},open('s06_00.json','w'),ensure_ascii=False)
