import json
W='https://en.wikipedia.org/wiki/'
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":b,"y":c,"d":e} for a,b,c,e in v]
    return r
kinds=[
{"n":"Ashtray","a":"","d":"Receptacle for ash and stubs, usually a shallow dish; cigar ashtrays are larger with bigger notches.","t":["Cigar ashtray","Pocket ashtray","Covered ashtray","Standing ashtray","Advertising ashtray"],"s":"https://www.northwoodshumidors.com/cigar-blog/10-best-cigar-accessories-top-picks-reviews",
 "x":[x("Cylinda-Line ashtray","Stelton","1967","https://hivemodern.com/pages/product16018/cylinda-line-revolving-ashtray-arne-jacobsen-stelton","Stainless-steel revolving ashtray designed by Arne Jacobsen for Stelton in 1967.",[("Cigar ashtray","Stelton","","Cylinda-Line cigar version")])],
 "m":[["Flor de Alba","Elie Bleu"]]},
{"n":"Cigarette case","a":"","d":"Small flat case for carrying cigarettes on the person, in precious metal, leather, wood or plastic.","t":["Metal","Leather","Silver","Enamel","Flat fifty tin"],"s":W+"Cigarette_case",
 "x":[x("Fabergé cigarette case","Fabergé","",W+"Cigarette_case","Peter Carl Fabergé made gold and gem cases for the Tsar's family."),
      x("Cartier cigarette case","Cartier","",W+"Cigarette_case","Cartier cases given by Linda Lee Thomas to Cole Porter on his Broadway openings."),
      x("Legrain snakeskin case","Pierre Legrain","c.1925",W+"Cigarette_case","Snakeskin cigarette case designed around 1925 by Pierre Legrain.")]},
{"n":"Cigarette holder","a":"","d":"Slender tube in which a cigarette is held for smoking, keeping ash off clothes and nicotine off fingers.","t":["Opera (16-20 in)","Theatre (10-14 in)","Dinner (4-6 in)","Cocktail","Men's (up to 4 in)","Filter holder"],"s":W+"Cigarette_holder"},
]
brands=[{"n":"Stelton","c":"Denmark","f":"","seg":"Premium","kf":"Scandinavian design","d":"Danish design house that makes the Cylinda-Line range by Arne Jacobsen.","s":"https://hivemodern.com/pages/product16018/cylinda-line-revolving-ashtray-arne-jacobsen-stelton"}]
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":"Guy Janot and Jean Claude cigarette-case models dropped as unsourced SKU noise; Elie Bleu Flor de Alba kept as old model. Art Deco enamel, Denicotea and Elie Bleu archetype not found on retrieved pages. Period and advertising ashtrays are types/attributes, not kinds."},open('s06_01.json','w'),ensure_ascii=False)
