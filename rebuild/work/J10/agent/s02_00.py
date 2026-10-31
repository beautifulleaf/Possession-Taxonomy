import json
W='https://en.wikipedia.org/wiki/'
LB=W+"List_of_cigarette_brands"
def x(n,mk,y,s,d,v=None):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":mk,"y":b,"d":c} for a,b,c in v]
    return r
cig=[
x("Marlboro","Philip Morris","1924",W+"Marlboro","Philip Morris brand launched 1924 as a women's cigarette, repositioned for men in the 1950s with the Marlboro Man; top US seller from 1976.",[("Red","1924","Original full-flavour"),("Gold","","Former Lights, renamed after 2006 ruling"),("Menthol","","Includes Ice Blast capsule version")]),
x("Camel","R.J. Reynolds","1913",LB,"American brand introduced in 1913, owned by R.J. Reynolds in the US and Japan Tobacco International elsewhere."),
x("Lucky Strike","American Tobacco","1871",W+"Lucky_Strike","Began as R. A. Patterson's cut plug in 1871; a cigarette from the early 1900s, owned by American Tobacco from 1905 and now by BAT.",[("Original unfiltered","","Still sold in the US by R.J. Reynolds"),("Green menthol","1960s",""),("Silver","","Lighter variant")]),
x("Gauloises","SEITA","1910",W+"Gauloises","French dark-tobacco brand of 1910, first called Hongroises, short wide cigarettes of Syrian and Turkish leaf.",[("Gauloises Brunes","","Unfiltered dark tobacco, milder"),("Light American-style","1984","Filtered lighter line")]),
x("Gitanes","","1910",W+"Gitanes","French brown-tobacco brand of 1910, now Imperial Brands; filtered variant from 1956.",[("Gitanes Maïs","1918","Yellow corn paper"),("Gitanes Brunes","","Classic dark style"),("Gitanes Blondes","1986","")]),
x("Benson & Hedges","Benson & Hedges","1873",W+"Benson_&_Hedges","London brand founded 1873 by Richard Benson and William Hedges; Royal Warrant 1878, revoked 1999.",[("Gold","2001","UK brand renamed from Special Filter"),("Silver","2001","Lower tar")]),
x("Sobranie Black Russian","Sobranie","1879",W+"Sobranie","Black-and-gold premium cigarette of the Sobranie house, founded in London in 1879; now Gallaher/Japan Tobacco, made in Ukraine.",[("Cocktail","","Multi-coloured premium cigarette")]),
x("Peace","Japan Tobacco","1952",LB,"Japanese premium brand introduced in 1952."),
x("Seven Stars","Japan Tobacco","1969",W+"Seven_Stars_(cigarette)","Japan Tobacco brand launched 1 February 1969, the first cigarette with a charcoal filter.",[("Original","1969","14 mg tar"),("Black Charcoal Menthol","2009","Japan's first menthol charcoal filter")]),
x("Nat Sherman","Nat Sherman","1930",W+"Nat_Sherman","New York tobacconist brand of luxury cigarettes and cigars; Havana Ovals #149 is a cigarette made from cigar tobacco; bought by Altria in 2017."),
x("Natural American Spirit","Santa Fe Natural Tobacco","1982",LB,"American brand introduced in 1982, owned by R.J. Reynolds in the US and Japan Tobacco International elsewhere."),
]
ryo=[
x("Drum","Douwe Egberts","1952",W+"Drum_(tobacco)","Dutch fine-cut shag introduced 1952, owned by Imperial Brands since 1998; sold by colour.",[("Original","",""),("Bright Blue","",""),("Gold","",""),("Dark Kentucky","","")]),
x("Golden Virginia","Imperial Tobacco","1877",W+"Golden_Virginia","UK rolling tobacco of 1877 blending Virginia, burley and Oriental, owned by Imperial Tobacco."),
x("Amber Leaf","Gallaher","",W+"Amber_Leaf","Gallaher/Japan Tobacco rolling tobacco sold mainly in the UK and Ireland; Amber Leaf Blonde added 2012."),
x("Old Holborn","Richard Lloyd & Sons","1785",W+"Old_Holborn","Rolling tobacco from Richard Lloyd & Sons, named after Holborn, London; blue, yellow, white and orange varieties."),
]
kinds=[
{"n":"Manufactured cigarette","a":"filtered cigarette · plain cigarette","d":"Factory-made cigarette of cut tobacco in a paper tube, with or without a filter tip.","t":["Filtered","Plain (unfiltered)","Menthol","Slims","Charcoal filter"],"s":"https://kennet.mhlw.go.jp/information/information/tobacco/t-01-001.html","x":cig},
{"n":"Roll-your-own tobacco","a":"RYO · fine-cut tobacco","d":"Loose finely cut tobacco sold for hand-rolling or filling tubes.","t":["Fine-cut","Make-your-own (MYO)"],"s":"https://www.jti.co.jp/tobacco/index.html","x":ryo},
{"n":"Kretek (clove cigarette)","a":"kretek","d":"Indonesian cigarette of tobacco blended with about one third minced clove buds, named for the crackle of burning cloves.","t":["Filtered kretek","Hand-rolled kretek"],"s":W+"Kretek","r":[["A Mild","Sampoerna"],["Djarum Black","Djarum"]],
 "x":[x("Dji Sam Soe","Sampoerna","1913",LB,"Indonesian kretek brand introduced 1913, Philip Morris International and Sampoerna."),
      x("Gudang Garam","Gudang Garam","1958",LB,"Indonesian kretek brand introduced 1958."),
      x("Djarum","Djarum","",LB,"Indonesian kretek maker; Djarum 76 (1976) and Djarum Super (1981)."),
      x("Sampoerna A Mild","Sampoerna","1990",LB,"Sampoerna's A brand introduced 1990.")]},
{"n":"Bidi","a":"beedi · biri","d":"Small hand-rolled smoke of tobacco flake wrapped in a tendu leaf and tied with thread.","t":["Plain bidi","Flavoured bidi"],"s":W+"Beedi"},
]
def b(n,c,f,d,s,kf="tobacco group"): return {"n":n,"c":c,"f":f,"seg":"Mainstream","kf":kf,"d":d,"s":s}
brands=[
b("Philip Morris International","United States","2008","Marlboro maker outside the US, spun off from Altria in 2008.","knowledge"),
b("British American Tobacco","United Kingdom","1902","Owner of Lucky Strike and Dunhill cigarettes internationally.","knowledge"),
b("Japan Tobacco","Japan","1985","Japanese group behind Seven Stars, Peace, Camel (outside the US), Gallaher and Sobranie.","knowledge"),
b("Imperial Brands","United Kingdom","1901","Owner of Gauloises, Gitanes, Drum and Golden Virginia.","knowledge"),
b("Sampoerna","Indonesia","","Indonesian kretek maker of A Mild and Dji Sam Soe, part of Philip Morris International.",LB,"kretek"),
b("Djarum","Indonesia","","Indonesian kretek maker.",LB,"kretek"),
b("Gudang Garam","Indonesia","1958","Indonesian kretek maker.",LB,"kretek"),
]
trad=[{"n":"Indonesian kretek","g":"Food & drink","r":"Indonesia (Kudus, Central Java)","p":"1880 to present","d":"Clove-and-tobacco cigarettes first made in Kudus, credited to Hajj Djamhari, first sold as medicine.","tech":"Tobacco blended with minced dried clove buds, hand-rolled or machine-made","mat":"Tobacco, clove buds","forms":["Kretek (clove cigarette)"],"ctr":["Kudus","Sampoerna","Djarum","Gudang Garam"],"auth":"Crackling sound when burning; sold by named Indonesian makers.","s":W+"Kretek"}]
json.dump({"kinds":kinds,"brands":brands,"traditions":trad,"notes":"Filtered and plain cigarette merged into one kind with t. Dunhill, Nat Sherman Sobranie licence and Samson not given archetypes (no retrieved page for Dunhill cigarettes/Samson). Big-group brand entries from knowledge (owner decision). Sampoerna A, Djarum Black kept as old ranges."},open('s02_00.json','w'),ensure_ascii=False)
