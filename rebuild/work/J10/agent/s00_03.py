import json
W='https://en.wikipedia.org/wiki/'
H=W+"Humidor"
def x(n,mk,y,s,d):
    return {"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
kinds=[
{"n":"Humidor","a":"standing humidor","d":"Lined box or cabinet that holds cigars at about 70% humidity; sizes run from travel cases (2-20 cigars) to cabinets (1,000-5,000).","t":["Travel humidor","Desktop humidor","Cabinet humidor","Electric humidor","Walk-in humidor"],"s":H,
 "x":[x("Davidoff desktop humidor","Davidoff","",H,"Zino Davidoff is credited with inventing the desktop humidor, the most common home type holding about 25-500 cigars."),
      x("Boveda humidor","Boveda","",  "https://www.cigaraficionado.com/article/a-proprietary-desktop-humidor-made-just-for-boveda-packets","Desktop humidor of macassar ebony with Spanish cedar lining, built for Boveda packs and holding 50 cigars.")],
 "m":[["Cigar Caddy 3400","Cigar Caddy"],["Aficionado Deluxe","Adorini"],["Roma","Adorini"]]},
{"n":"Cigar cutter","a":"","d":"Tool for cutting the cap of a cigar, as a straight cut, punch or V-cut.","t":["Guillotine","Double guillotine","Punch","V-cut","Scissors"],"s":"https://www.northwoodshumidors.com/cigar-blog/10-best-cigar-accessories-top-picks-reviews",
 "x":[x("Xikar Xi","Xikar","","https://www.cigaraficionado.com/articles/xikar-cutters-1838","Teardrop-shaped double guillotine, opening by button; sold in several styles including Xi2 and Xi3."),
      x("Henckels dual-ended cutter","J.A. Henckels","",W+"Cigar_cutter","Rosewood-sided cutter making both straight and V-cuts.")]},
{"n":"Cigar case","a":"","d":"Case for carrying cigars on the person, usually leather or metal.","t":["Leather case","Metal tube case"],"s":"https://www.northwoodshumidors.com/collections/cigar-cases",
 "m":[["Night II","Visol"],["Envoy","Xikar"]],"r":[["Quasar","Colibri"]]},
{"n":"Humidifier & humidity pack","a":"humidification device","d":"Device that keeps humidor humidity near 70%: propylene glycol solution, silica gel beads, electronic or two-way pack.","t":["Propylene glycol humidifier","Silica gel humidifier","Electronic humidifier","Two-way humidity pack"],"s":H,
 "x":[x("Boveda two-way pack","Boveda","","https://www.cigaraficionado.com/article/a-proprietary-desktop-humidor-made-just-for-boveda-packets","Packet giving six months of maintenance-free humidification at 69% RH (size 320), with seasoning packets.")]},
{"n":"Hygrometer","a":"humidity gauge","d":"Gauge showing humidity inside a humidor; analog and digital types, digital described as more accurate.","t":["Analog hygrometer","Digital hygrometer"],"s":H},
]
brands=[
{"n":"Xikar","c":"United States","f":"","seg":"Specialist","kf":"cutters","d":"Maker of cigar cutters including the Xi line, and of cases.","lines":["Xi"],"s":"https://www.cigaraficionado.com/articles/xikar-cutters-1838"},
{"n":"Boveda","c":"United States","f":"","seg":"Specialist","kf":"humidity packs","d":"Maker of two-way humidity-control packs and a Boveda humidor.","lines":["Two-way pack"],"s":"https://www.cigaraficionado.com/article/a-proprietary-desktop-humidor-made-just-for-boveda-packets"},
{"n":"Davidoff","c":"Switzerland","f":"1906","seg":"Premium","kf":"Swiss luxury","d":"Swiss house credited with the desktop humidor.","s":H},
{"n":"J.A. Henckels","c":"Germany","f":"","seg":"Heritage manufactory","kf":"cutlery","d":"Solingen cutlery maker credited with a dual-ended cigar cutter.","s":W+"Cigar_cutter"},
]
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":"Elie Bleu, Les Fines Lames Le Petit, S.T. Dupont cutters and Davidoff cutters not found on a retrieved page (search snippets only), so omitted. Adorini list trimmed to two models. Old cutter models became types. Boveda 84% seasoning pack not confirmed by retrieved page."},open('s00_03.json','w'),ensure_ascii=False)
