import json
W='https://en.wikipedia.org/wiki/'
H=W+"Hookah"
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":b,"y":c,"d":e} for a,b,c,e in v]
    return r
kinds=[
{"n":"Hookah","a":"waterpipe · nargile · shisha · ghalyan","d":"Water pipe with a bowl, body, water base and one or more hoses, for shisha.","t":["Single-hose","Multi-hose","Travel hookah"],"s":"https://hookah.com/",
 "x":[x("Egyptian shisha","","",H,"Water pipe called shisha in Egypt, Sudan and much of the Arab world; Levant form is arjīlah."),
      x("Turkish nargile","","",H,"Nargile as used in Turkey and the Balkans."),
      x("Persian ghalyan","","",H,"Ghalyan of Persian-speaking countries; earliest known literary reference is from the poet Ahlī Shirazi, died 1535."),
      x("Indian huqqa","","",H,"Huqqa of the Indian subcontinent; the hookah is credited by one account to Abul-Fath Gilani at the Mughal court.",[("Malabar (Koyilandy) hookah","","","Historic Indian export style")]),
      x("Kaloud Krysalis","Kaloud","",H,"Los Angeles-based Kaloud's heat-management system, tested by commissioned German laboratory work.",[("Krysalis Calix","Kaloud","",""),("Krysalis Eltheria","Kaloud","","")])],
 "r":[["Krysalis","Kaloud"]]},
{"n":"Shisha tobacco","a":"muʽassel · hookah tobacco","d":"Moist, usually flavoured tobacco for smoking in a hookah, mixed with molasses, glycerol and flavouring.","t":["Molasses-based","Flavoured","Unflavoured"],"s":"https://hookah.com/",
 "x":[x("Muʽassel","","early 20th century",W+"Mu%CA%BDassel","Sweetened tobacco mix of molasses, vegetable glycerol and flavourings, developed in Egypt in the early 20th century."),
      x("Al Fakher","Al Fakher","1999",H,"Lebanon-based flavoured shisha maker founded 1999, common on American café menus."),
      x("Nakhla","Nakhla Tobacco","",H,"Egypt-based shisha tobacco maker.")]},
{"n":"Tumbak","a":"ajami","d":"Unflavoured, coarse tobacco burned directly with charcoal in rural South Asian and Persian-Turkish water pipes.","t":["Washed tumbak","Dry tumbak"],"s":H},
{"n":"Tobacco-free shisha","a":"herbal shisha","d":"Shisha of non-tobacco material, sold with the hookah products it imitates.","t":["Molasses herbal mix","Steam stones"],"s":W+"Shiazo",
 "x":[x("Shiazo steam stones","Shiazo","",W+"Shiazo","Porous mineral stones that absorb vegetable glycerol and flavouring and release vapour when heated; German brand.")]},
]
brands=[
{"n":"Kaloud","c":"United States","f":"","seg":"Specialist","kf":"hookah systems","d":"Los Angeles hookah systems company behind the Krysalis.","s":H},
{"n":"Al Fakher","c":"Lebanon","f":"1999","seg":"Mainstream","kf":"shisha","d":"Lebanon-based flavoured shisha tobacco maker owned by AIR Global.","s":H},
{"n":"Nakhla","c":"Egypt","f":"","seg":"Heritage manufactory","kf":"Egyptian shisha","d":"Egyptian shisha tobacco maker, also known as Al-Nakhla.","s":H},
{"n":"Shiazo","c":"Germany","f":"","seg":"Specialist","kf":"steam stones","d":"German maker of steam stones, the first of their kind.","s":W+"Shiazo"},
]
trad=[
{"n":"Egyptian and Levantine shisha","g":"Food & drink","r":"Egypt, Levant","p":"early 20th century to present","d":"Water-pipe smoking of sweetened muʽassel tobacco, called shisha in Egypt and arjīlah in the Levant.","tech":"Molasses-fermented tobacco smoked over charcoal","mat":"Tobacco, molasses, glycerol, flavour","forms":["Hookah","Shisha tobacco"],"ctr":["Egypt","Lebanon"],"auth":"Sealed packs from named makers such as Al Fakher and Nakhla.","s":W+"Mu%CA%BDassel"},
{"n":"Turkish nargile","g":"Food & drink","r":"Turkey, Balkans","p":"16th century to present","d":"Turkish water pipe tradition, nargile.","tech":"Water pipe smoking","mat":"Glass, metal, tobacco","forms":["Hookah"],"ctr":[],"auth":"","s":H},
{"n":"Persian ghalyan","g":"Food & drink","r":"Persia (Iran)","p":"16th century to present","d":"Persian water pipe, with literary reference by Ahlī Shirazi before 1535 and a court post of hookah tender.","tech":"Water pipe smoking","mat":"Glass and precious metals for the rich","forms":["Hookah","Tumbak"],"ctr":[],"auth":"","s":H},
{"n":"Indian huqqa","g":"Metal & blades","r":"Indian subcontinent","p":"16th century to present","d":"Indian water pipe; Koyilandy (Malabar) hookahs were an export style.","tech":"Water pipe smoking","mat":"Metal, coconut","forms":["Hookah","Malabar hookah"],"ctr":["Koyilandy"],"auth":"","s":H},
]
json.dump({"kinds":kinds,"brands":brands,"traditions":trad,"notes":"Khalil Mamoon, Alpha Hookah, Maklaud, Steamulation, Dschinni, Aladin, Starbuzz, Afzal, Fumari, Tangiers, Adalya, Darkside, MustHave and Bidriware not on retrieved pages; omitted. Shiazo is the only tobacco-free brand sourced. Hookah.com is the old source for two kinds."},open('s05_00.json','w'),ensure_ascii=False)
