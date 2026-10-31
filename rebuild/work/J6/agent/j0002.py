import json
W='https://en.wikipedia.org/wiki/'
def A(n,a,d,mk,y,s,v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
S=W+'Single-serve_coffee_container'
cap=[
 A("Nespresso Original","OriginalLine","Aluminium capsule of 5-7 g for 40 ml espresso or 110 ml lungo; patents began expiring in 2012, allowing compatibles.","Nespresso","1986",W+'Nespresso',[V("Third-party compatibles","","2012","Became possible once Nestlé's patents expired"),V("Starbucks Nespresso-compatible capsules","Starbucks","2016","Announced for consumer machines in Europe")],"material: aluminium · size 5-7 g · drinks: espresso, lungo"),
 A("Nespresso Vertuo","VertuoLine","Barcode-read capsule spun up to 7,000 rpm for cups from 40 ml to 414 ml; not interchangeable with Original.","Nespresso","2014",W+'Nespresso',[V("France launch","","2016","Original line renamed Original there")],"reading: barcode · sizes: espresso to Alto XL"),
 A("Keurig K-Cup","K-Cup","Plastic pod for Keurig brewers; main patent expired in 2012 and many clones exist, including compostable ones.","Keurig","1992 (company); 1998 launch",W+'Keurig',[V("Home brewers","Keurig","2004","Added after office launch"),V("Compostable K-Cup clones (PurPod100, OneCUP)","Club Coffee, San Francisco Bay Coffee","2015","Unauthorised compostable pods")],"material: polypropylene since 2020 · owner Keurig Dr Pepper"),
 A("Nescafé Dolce Gusto","Dolce Gusto","Capsule system that mostly uses roast-and-ground coffee, with machines made by Krups or De'Longhi.","Nestlé","2006",W+'Dolce_Gusto',[],"machines: Krups, De'Longhi"),
 A("Tassimo T-Disc","T-Disc","Barcode-read disc for espresso, coffee, tea and hot chocolate; machines by Bosch from 2008.","Tassimo","2004",W+'Tassimo',[],"barcode reading · owner JDE Peet's (Kraft Heinz in North America)"),
 A("Lavazza A Modo Mio","A Modo Mio","Lavazza capsule and machine range launched in 2007, with machines by Saeco, Electrolux and others.","Lavazza","2007",W+'Lavazza_A_Modo_Mio',[V("Espresso Point","Lavazza","1983","Earlier Lavazza capsule system"),V("Espresso Point MAXI","Lavazza","1992","Larger Lavazza capsule")],"maker: Lavazza"),
 A("illy iperEspresso","iperEspresso","Capsule system developed and patented by illy; works with FrancisFrancis, Gaggia and Cuisinart machines.","illy","2007 (per the comparison table)",S,[],"maker: illy"),
 A("E.S.E. pod","Easy Serving Espresso · ESE","Open-standard 44 mm paper pod with about 7 g of coffee for non-grinding espresso machines.","Italian E.S.E. consortium","1998 (consortium founded)",W+'Easy_Serving_Espresso_Pod',[],"size: 44 mm, 7 g · material: paper"),
 A("Senseo pad","Senseo","Paper pad system from Philips and Douwe Egberts, interchangeable across many makers.","Senseo","2001",W+'Senseo',[],"size: 70 mm paper pad"),
 A("Caffitaly / K-Fee","Caffitaly · K-Fee","Capsule system by Caffita System, physically compatible with Krüger's K-Fee.","Caffita System","2004",S,[V("K-Fee","Krüger Group","2010","Compatible capsule")],"multi-brand capsules"),
]
inst=[
 A("Nescafé spray-dried instant","Nescafé Classic","Original soluble coffee launched in Switzerland on 1 April 1938; the first 1938 powder was half coffee solids, half maltodextrin.","Nescafé","1938",W+'Nescaf%C3%A9',[],"drying: spray · pack: jar, sachet"),
 A("Freeze-dried instant","freeze-dried coffee","Frozen extract dried by sublimation into flaky granules; costlier than spray-drying. First launched as Maxwell House in 1963.","Maxwell House","1963",W+'Instant_coffee',[V("Nescafé Gold Blend","Nestlé","","UK freeze-dried coffee sold under the Nescafé name; ad campaign 1987-1993")],"drying: freeze · form: granule"),
 A("Camp Coffee","coffee and chicory essence","Liquid coffee and chicory essence first made in Scotland in 1876.","Camp Coffee","1876",W+'Instant_coffee',[],"form: liquid essence"),
]
kinds=[
 {"n":"Coffee capsules & pods","a":"E.S.E. pod · paper pad · coffee capsule","d":"Single-serve capsule, E.S.E. pod or paper pad of coffee made to fit one machine system.","t":["aluminium capsule","plastic capsule","compostable capsule","paper pod"],"s":"https://www.nespresso.com/dk/en/order/capsules","x":cap},
 {"n":"Instant coffee","a":"soluble coffee","d":"Dried soluble coffee extract, including a dry mix when coffee is its largest ingredient by weight.","t":["spray-dried","freeze-dried","agglomerated granules"],"s":"https://www.ocado.com/products/nescafe-gold-blend-freeze-dried-instant-coffee-12003011","m":[["Nescafé Gold Blend","Nestlé"]],"x":inst},
 {"n":"Cold brew & coffee concentrate","a":"liquid coffee extract","d":"Liquid coffee extract sold to dilute, with coffee as its main ingredient; a sweetened or milk ready-to-drink is not included.","t":["cold brew concentrate","hot-brewed concentrate"],"s":"https://shop.westrockcoffee.com/collections/coffees/products/cold-brew-black-coffee-concentrate-32oz-6ct","m":[["Cold Brew Black Coffee Concentrate - Bottle","Westrock Coffee"]]},
]
B=lambda n,c,f,seg,kf,d,s,**k: dict({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s},**k)
brands=[
 B("Nespresso","Switzerland","1986","Premium","capsule system","Nestlé capsule brand with Original and Vertuo lines.",W+'Nespresso'),
 B("Keurig","United States","1992","Mainstream","K-Cup","Pod brewer brand, now part of Keurig Dr Pepper.",W+'Keurig'),
 B("Nescafé","Switzerland","1938","Mainstream","instant coffee","Nestlé instant coffee brand launched in 1938.",W+'Nescaf%C3%A9'),
 B("Nescafé Dolce Gusto","Switzerland","2006","Mainstream","capsule system","Nestlé capsule system made with Krups or De'Longhi machines.",W+'Dolce_Gusto'),
 B("Tassimo","","2004","Mainstream","T-Disc","Barcode disc system now owned by JDE Peet's.",W+'Tassimo'),
 B("Senseo","Netherlands","2001","Mainstream","paper pad","Philips and Douwe Egberts pad system.",W+'Senseo'),
]
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":"Test winners (Which?/CR) not retrieved; Starbucks VIA, Sudden, Swift Cup, Voila, Kopiko, OldTown, Nescafe 3in1, Taster's Choice left out (not on retrieved pages). Cold brew keeps only old consumer bottle entry; Westrock 6-case trade wording dropped from definition; no cold brew page retrieved for new tier picks. Ready-to-drink milk coffees excluded per brief."}
json.dump(out,open('00_02.src.json','w'),ensure_ascii=False)
