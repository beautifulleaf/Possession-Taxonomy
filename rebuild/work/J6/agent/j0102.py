import json
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
ip="Ippodo Tea"; old="https://global.ippodo-tea.co.jp/collections/all/"
sen=[
 A("Uji sencha","Uji tea","Sencha from Uji, Kyoto, where Soen Nagatani developed sencha in 1738 after about 15 years of testing.","","1738",W+'Uji_tea',[V("Hosen (sencha)",ip),V("Kaboku (sencha)",ip),V("Kumpu (sencha)",ip)],"region Kyoto · sun-grown, steamed, rolled"),
 A("Shizuoka and Kagoshima sencha","Shizuoka · Kagoshima","Japan's two largest producing prefectures, together about 70% of dried unrefined tea; Yabukita covers about 30% of Kagoshima fields.","","1319-1320 (Uji priest plants tea in Kagoshima)",W+'Kagoshima_green_tea',[V("Nansatsu Plateau","","","Largest Kagoshima growing area"),V("Shibushi and Kirishima","","","Next largest areas"),V("Yutakamidori and Saemidori","","","Prevalent Kagoshima cultivars")],"cultivar: Yabukita, Yutakamidori, Saemidori"),
 A("Shincha","new tea · first flush","First-picked tea of the year, prized for fresh aroma and sweetness, picked early April to late May.","","",W+'Sencha',[V("Kagoshima shaded first flush","","","Among the earliest shincha")],"season April-May"),
 A("Fukamushi sencha","deep-steamed sencha","Sencha steamed for about 1-2 minutes for a cloudier cup.","","",W+'Sencha',[V("Asamushi","","","Lightly steamed sencha")],"steaming 1-2 min"),
 A("Bancha","","Same tea as sencha harvested later in the season; the lowest grade of sencha.","","",W+'Sencha',[V("Tamaryokucha","","","Listed as a green tea type on the page")],"later harvest"),
]
gyo=[
 A("Yame gyokuro","Yamecha gyokuro","Gyokuro from Fukuoka, about 45% of Japan's gyokuro; won the national tea fair for 12 straight years from 2001.","","1406 (tea brought to Yame)",W+'Yamecha',[V("2007 national jury","","2007","Yame took the top 26 places")],"region Fukuoka"),
 A("Uji gyokuro","","Shade-grown tea from Uji, about 140 tons in 2008; shaded like matcha, steamed and rolled like sencha.","","19th century",W+'Uji_tea',[V("Ippoen (gyokuro)",ip),V("Kanro (gyokuro)",ip),V("Rimpo (gyokuro)",ip),V("Tenka-ichi (gyokuro)",ip)],"shading 20-30 days"),
 A("Yamamotoyama gyokuro","Yamamotoyama","Gyokuro credited to merchant Yamamoto Kahei, who in 1835 noticed netting changed the leaf.","Yamamotoyama","1835",W+'Gyokuro',[],"cultivar: Asahi, Okumidori, Yamakai, Saemidori"),
 A("Kabusecha","kabuse tea","Tea shaded for under twenty days, milder than sencha and less shaded than gyokuro.","","",W+'Gyokuro',[],"shading under 20 days"),
]
mat=[
 A("Uji matcha","ceremonial matcha","Powdered tencha from shade-grown Uji leaves, the historic centre of matcha, made without rolling.","","16th century shading",W+'Mattya',[V("Ummon-no-mukashi",ip),V("Sayaka-no-mukashi",ip),V("Ikuyo-no-mukashi",ip),V("Shoin-no-mukashi",ip),V("Kan-no-shiro",ip),V("Wakaki-shiro",ip)],"grade: usucha vs koicha · tencha"),
 A("Koicha vs usucha","thick tea · thin tea","Koicha uses about 4 g of higher-grade matcha in 30 ml of water; usucha is thinner and foamed.","","",W+'Mattya',[],"grade: koicha, usucha"),
 A("Historic Mukashi blends","Baba Mukashi · Hatsu Mukashi · Ato Mukashi","Named historic matcha brands listed on Wikipedia's matcha page.","","",W+'Mattya',[],"blends"),
]
hoj=[A("Hojicha","houjicha","Green tea roasted in a porcelain pot over charcoal, discovered in 1920 by a Kyoto merchant roasting unsaleable bancha.","","1920",W+'H%C5%8Djicha',[V("Gokujo Hojicha",ip),V("Iribancha / Kyobancha")],"base: bancha, sencha, kukicha · roast about 150 C")]
gen=[A("Genmaicha","brown rice tea · popcorn tea","Green tea blended with roasted popped brown rice, once a cheaper tea for poorer households.","","",W+'Genmaicha',[V("Matcha-iri genmaicha","","","Genmaicha with added powdered matcha")],"blend: green tea + roasted rice")]
kinds=[
 {"n":"Sencha & steamed green tea","a":"sencha · bancha · steamed green tea","d":"Unoxidised tea fixed by steaming, rolled and dried (sencha, bancha).","t":["shincha","fukamushi (deep-steamed)","asamushi","bancha","tamaryokucha"],"s":old,"x":sen},
 {"n":"Gyokuro & kabusecha","a":"shade-grown green tea","d":"Green tea from bushes shaded before harvest, then steamed (gyokuro, kabusecha).","t":["gyokuro","kabusecha"],"s":old,"x":gyo},
 {"n":"Matcha","a":"powdered green tea","d":"Shade-grown, steamed, unrolled tea leaf stone-ground to a fine powder.","t":["usucha grade","koicha grade","culinary grade"],"s":old,"x":mat},
 {"n":"Hojicha","a":"roasted green tea","d":"Green tea roasted after fixing (hojicha).","t":["bancha base","kukicha base","powdered"],"s":old,"x":hoj},
 {"n":"Genmaicha","a":"brown rice tea","d":"Green tea blended with roasted rice, formerly listed under flavoured tea.","t":["matcha-iri"],"s":W+'Genmaicha',"x":gen},
]
B=lambda n,c,f,seg,kf,d,s,**k: dict({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s},**k)
brands=[
 B("Yamamotoyama","Japan","1690","Heritage manufactory","gyokuro","Tea and seaweed maker claiming to be the world's oldest tea company; bought Stash Tea in 1993.",W+'Yamamotoyama_(company)'),
 B("Ippodo Tea","Japan","","Premium","Kyoto matcha and sencha","Kyoto tea house selling matcha, gyokuro and sencha.","knowledge"),
 B("Marukyu Koyamaen","Japan","","Premium","Uji matcha","Uji matcha producer.","knowledge"),
 B("Kanbayashi Shunsho","Japan","","Premium","Uji tea","Uji tea house.","knowledge"),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Ippodo-only SKU skew trimmed: Ippodo grades kept as versions beside other regions/houses. Left out unsourced: Marukyu Koyamaen Wako, Itohkyuemon, Sayama, Okumidori/Samidori cultivar archetypes (search snippet only), Yabukita page. Kanbayashi Shunsho appears as Mitsuboshien Kambayashi Honten on the Uji page; kept as knowledge-only brand stub."}
json.dump(out,open('01_02.src.json','w'),ensure_ascii=False)
