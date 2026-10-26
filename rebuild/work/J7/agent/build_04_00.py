import json, os
W='https://en.wikipedia.org/wiki/'
BJ1='https://www.bjcp.org/style/2021/beer/'; BJ2='https://www.bjcp.org/style/2021/beer/?pg=2'; OLD='https://www.bjcp.org/style/2021/beer'
def X(n,d,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=a1,mk=b,y=c,d=e) for a1,b,c,e in v],"dt":dt}
K=[]
K.append({"n":"International pale lager","a":"Pale lager · Premium lager · American lager · Dry beer",
 "d":"Pale, clean, well-attenuated lager of standard strength, often brewed with rice or corn adjuncts.",
 "t":["All-malt","Adjunct (rice or corn)","American lager","Dry (highly attenuated)","Premium export"],
 "s":OLD,
 "x":[X("Heineken","Dutch pale lager of 5% ABV, brewed with a bottom-fermenting yeast developed for the brewery in 1873.","Heineken","1873",W+"Heineken_Pilsener",
        [("Heineken Premium Light","Heineken","","lighter version"),("Heineken 0.0","Heineken","2017","alcohol-free version")],"bottle, can or draught · strength (regular, light, 0.0)",a="Heineken Pilsener · Heineken Lager Beer"),
      X("Budweiser","American pale lager from St. Louis, the reference for the American lager style.","Anheuser-Busch","1876",W+"Budweiser",
        [("Bud Ice","Anheuser-Busch","",""),("Budweiser 66","Anheuser-Busch","2010","UK, 4% ABV"),("Bud Zero","Anheuser-Busch","2020","alcohol-free")],"pack · strength · market version"),
      X("Asahi Super Dry","Highly attenuated Japanese lager with a crisp, dry finish that started the dry-beer category.","Asahi Breweries","1987",W+"Asahi_Super_Dry",
        [("Dry Crystal","Asahi Breweries","2023","3.5% ABV, Japan"),("Dry Zero","Asahi Breweries","","alcohol-free")],"bottle, can or draught · strength"),
      X("Corona Extra","Mexican pale lager in a clear bottle, first brewed by Grupo Modelo.","Grupo Modelo","1925",W+"Negra_Modelo",[],"bottle or can · size"),
      X("Modelo Especial","Pilsner-style Mexican lager from Grupo Modelo.","Grupo Modelo","1925",W+"Negra_Modelo",[],"bottle or can · size")],
 "m":[["Birkebeinerpils","Victor 23 Brewing"],["Birra Moretti","Birra Moretti"]]})
K.append({"n":"American light lager","a":"Light beer · Lite beer","d":"Very pale, highly carbonated, light-bodied lager of low strength and reduced calories.",
 "t":["Regular light","Flavoured light (lime etc.)"],"s":OLD,
 "x":[X("Gablinger's Diet Beer","First reduced-carbohydrate diet beer, made with an enzyme that broke down more starch.","Rheingold Breweries","1967",W+"Pale_lager",[],"bottle or can"),
      X("Miller Lite","Pilsner-style light lager of 4.2% ABV that made light beer a mass category.","Miller Brewing Company","1975",W+"Miller_Lite",
        [("Meister Brau Lite","Meister Brau","1967","predecessor bought by Miller in 1972")],"bottle, can or draught"),
      X("Bud Light","Anheuser-Busch light lager; overtook Miller Lite in sales by 1994.","Anheuser-Busch","1982",W+"Miller_Lite",
        [("Bud Light Lime","Anheuser-Busch","","lime-flavoured")],"bottle, can or draught · flavour"),
      X("Coors Light","Pilsner-style light lager of 4.2% ABV.","Coors Brewing Company","1978",W+"Coors_Light",[],"bottle, can or draught")],
 "m":[["Transmission Light","Transmission Brewing"]]})
K.append({"n":"German Pils","a":"Pilsener · Pils · German pilsner","d":"Pale, crisp, hop-bitter German lager, straw to golden, drier and more bitter than Czech pilsner.",
 "t":["North German (drier, more bitter)","South German (softer)"],"s":OLD,
 "x":[X("Bitburger Pilsner","Rhineland pilsner of 4.8% ABV, flagship of the Bitburger brewery founded in 1817.","Bitburger Brewery","",W+"Bitburger_Brewery",
        [("Bitburger Alkoholfrei","Bitburger Brewery","","alcohol-free; sold as Drive in English-speaking countries")],"bottle, can or draught · strength"),
      X("Jever Pilsener","Frisian pilsner known for its strong bitterness, sold under this name since 1934.","Friesisches Brauhaus zu Jever","1934",W+"Jever_(beer)",
        [("Jever Fun","Friesisches Brauhaus zu Jever","","alcohol-free"),("Jever Light","Friesisches Brauhaus zu Jever","","")],"bottle, can or draught · strength")],
 "m":[["König Pilsener","König"],["Rothaus Pils","Rothaus"],["Trumer Pils","Trumer"],["Paulaner Pils","Paulaner"],["ABK Pils Anno 1907","ABK"],["Schönramer Pils","Schönramer"],
      ["Warsteiner","Warsteiner"],["Krombacher","Krombacher"],["Veltins","Veltins"],["Radeberger","Radeberger"],["Beck's","Beck's"],["Flensburger","Flensburger"]]})
K.append({"n":"Czech pale lager","a":"Czech pilsner · Bohemian pilsner · Světlý ležák · Czech premium pale lager","d":"Golden Czech lager with a soft malt and Saaz hop character, from draught-strength výčepní to premium ležák.",
 "t":["Výčepní (draught strength, about 10°)","Ležák (premium, 11–12°)","Unfiltered","Unpasteurised tank beer"],"s":OLD,
 "x":[X("Pilsner Urquell","The first golden lager, brewed in Plzeň with Saaz hops and soft water; the only beer allowed to be called pilsner in Czechia.","Plzeňský Prazdroj","1842",W+"Pilsner_Urquell",
        [("Unfiltered draught","Plzeňský Prazdroj","","small volumes"),("Tank (unpasteurised)","Plzeňský Prazdroj","","")],"draught, tank, can (330, 355, 500 ml) or green/brown bottle"),
      X("Budějovický Budvar Original","90-day-matured pale lager of 5% ABV from the state-owned brewery in České Budějovice.","Budějovický Budvar","1895",W+"Budweiser_Budvar_Brewery",
        [("Czechvar","Budějovický Budvar","","export name in the US, Canada, Mexico and Brazil"),("Budvar 33 světlý ležák","Budějovický Budvar","",""),("Classic","Budějovický Budvar","","pale draught"),("Free","Budějovický Budvar","","low-alcohol")],"strength · bottle, can or draught",a="Budweiser Budvar · Czechvar")],
 "m":[["Bernard Sváteční ležák","Bernard"],["Primátor Premium","Primátor"],["Radegast Ryze hořká 12","Radegast"],["Únětická 12°","Únětický pivovar"],["Pivovar Jihlava Ježek 11°","Pivovar Jihlava"],
      ["Gambrinus","Gambrinus"],["Kozel","Kozel"],["Staropramen","Staropramen"],["Krušovice","Krušovice"],["Tisnovanka 11%","Pivovar Tisnov"],["Lockport Lager","New York Beer Project"]]})
K.append({"n":"Munich Helles","a":"Helles · Hell · Münchner Hell","d":"Pale, malt-forward Bavarian lager, mildly sweet and low in bitterness.",
 "t":["Standard Hell","Stronger Export-style (e.g. Edelstoff)"],"s":OLD,
 "x":[X("Spaten Münchner Hell","The first Munich Helles, introduced by Spaten in 1894.","Spaten-Franziskaner-Bräu","1894",W+"Spaten-Franziskaner-Bräu",[],"bottle, can or draught"),
      X("Augustiner Lagerbier Hell","Pale lager of 5.2% ABV from Munich's oldest brewery, a benchmark of the style.","Augustiner-Bräu","",W+"Augustiner-Bräu",
        [("Edelstoff","Augustiner-Bräu","","stronger 5.6%, served from wooden barrels"),("Alkoholfrei Hell","Augustiner-Bräu","","alcohol-free")],"bottle or wooden-barrel draught")],
 "m":[["Paulaner Münchner Hell","Paulaner"],["Hofbräu München Original","Hofbräu München"],["Löwenbräu Original","Löwenbräu"],["Hacker-Pschorr Münchner Gold","Hacker-Pschorr"],
      ["Weihenstephaner Original Helles","Weihenstephaner"],["Schönramer Hell","Schönramer"],["Ayinger Lager Hell","Ayinger"],["Tegernseer Hell","Tegernseer"],["Andechser Hell","Andechser"],
      ["Wagner Helles","Brauerei Wagner"],["Wander Back Lager","Wander Back Beerworks"]]})
K.append({"n":"Dortmunder Export","a":"German Helles Exportbier · Dortmunder · Export","d":"Pale, soft and rounded lager of slightly higher strength, between Helles and Pils, from Dortmund.",
 "s":W+"Dortmunder_Export",
 "x":[X("Dortmunder Union Export","Original Dortmund export lager, brewed since 1873 under the influence of Plzeň pilsner.","Dortmunder Union","1873",W+"Dortmunder_Export",[],"bottle or draught")],
 "m":[["DAB Dortmunder Export","Dortmunder Actien Brauerei"],["Dortmunder Kronen","Kronen"],["Schönramer Gold","Schönramer"],["Landshuter Edel Hell","Landshuter"],["Müllerbräu Export Gold","Müllerbräu"],["Chuckanut Export Dortmunder Lager","Chuckanut"]]})
K.append({"n":"Kellerbier","a":"Zwickelbier · Zwickel · Zwickl · Naturtrüb","d":"Unfiltered, cloudy German lager, low in carbonation, often served from the barrel; from Franconia.",
 "t":["Kellerbier (fuller)","Zwickelbier (lighter)","Kellerweizen (top-fermented)"],"s":W+"Kellerbier",
 "x":[X("Zoigl","Upper Palatinate lager brewed in communal brewhouses and served in brewers' homes under a six-pointed star sign.","","1508 (first documented)",W+"Zoigl",[],"village (Windischeschenbach, Neuhaus, Tirschenreuth) · serving calendar")]})
K.append({"n":"Festbier","a":"Oktoberfestbier · Wiesnbier · Wiesn","d":"Pale, full-bodied, slightly stronger lager served at Oktoberfest today, paler than traditional Märzen.",
 "t":["Munich Oktoberfestbier (EU-protected)","Other Festbier"],"s":BJ2,
 "x":[X("Munich Oktoberfestbier","Festival beer of the Munich breweries; the name is EU-protected for Munich beer.","","",W+"Märzen",
        [("Augustiner Oktoberfest","Augustiner-Bräu","","served from wooden barrels"),("Paulaner Oktoberfest Bier","Paulaner","",""),("Hacker-Pschorr Superior Festbier","Hacker-Pschorr","",""),
         ("Löwenbräu Oktoberfestbier","Löwenbräu","",""),("Hofbräu Oktoberfestbier","Hofbräu München","",""),("Spaten Oktoberfestbier","Spaten-Franziskaner-Bräu","","")],"brewery · bottle, can or Maß draught")],
 "m":[["Weihenstephaner Festbier","Weihenstephaner"]]})
K.append({"n":"Märzen","a":"Märzenbier · Oktoberfest (US)","d":"Amber, malty German lager brewed in spring and lagered into autumn, the traditional Oktoberfest type.",
 "s":OLD,
 "x":[X("Spaten Ur-Märzen","Spaten introduced Märzenbier in 1841; Ur-Märzen is the beer it served at Oktoberfest in 1872.","Spaten-Franziskaner-Bräu","1841",W+"Spaten-Franziskaner-Bräu",
        [("Spaten Oktoberfestbier","Spaten-Franziskaner-Bräu","","märzen brewed in spring for Oktoberfest")],"bottle, can or draught")],
 "m":[["Hacker-Pschorr Oktoberfest Märzen","Hacker-Pschorr"],["Paulaner Oktoberfest","Paulaner"],["Ayinger Märzen","Ayinger"],["Weltenburg Kloster Anno 1050","Weltenburg"],["Hofmark Märzen","Hofmark"],
      ["Saalfelder Ur-Saalfelder","Saalfelder"],["Egger Märzen","Egger"],["Marcowe","Żywiec"],["Baltijos","Švyturys"]]})
K.append({"n":"Vienna lager","a":"Wiener Lager · Vienna-style lager","d":"Amber, moderately strong lager with a toasty malt character, created in Vienna and carried on in Mexico.",
 "t":["Austrian","Mexican","American craft"],"s":OLD,
 "x":[X("Dreher Vienna lager","Original amber lager developed by Anton Dreher in the late 1830s and shown at the 1867 Paris Exposition.","Dreher","late 1830s",W+"Vienna_lager",
        [("Ottakringer Wiener Original","Ottakringer","","modern Austrian revival"),("Theresianer Vienna","Theresianer","","")],"brewery · bottle or draught"),
      X("Victoria","Mexican Vienna lager first brewed in Toluca, the oldest Grupo Modelo brand.","Grupo Modelo","1865",W+"Negra_Modelo",[],"bottle or can")],
 "m":[["Devils Backbone Vienna Lager","Devils Backbone"],["Chuckanut Vienna Lager","Chuckanut"],["Heavy Seas Cutlass","Heavy Seas"],["Schell's Firebrick","Schell's"],["Figueroa Mountain Red Lager","Figueroa Mountain"]]})
def B(n,c,f,seg,d,sig,s,lines=(),eras=(),rel=()):
    return dict(n=n,c=c,f=f,seg=seg,d=d,lines=list(lines),eras=list(eras),sig=list(sig),sc=[],rel=list(rel),s=s)
Bs=[B("Heineken","Netherlands","","Global brewer","Dutch brewer of Heineken lager, introduced in 1873.",["Heineken"],W+"Heineken_Pilsener",["Heineken","Heineken 0.0","Heineken Premium Light"]),
 B("Anheuser-Busch","United States","","Mass-market brewer (AB InBev)","St. Louis brewer of Budweiser and Bud Light, part of AB InBev.",["Budweiser","Bud Light"],W+"Budweiser",["Budweiser","Bud Light","Bud Zero"],rel=["Grupo Modelo","Spaten-Franziskaner-Bräu"]),
 B("Asahi Breweries","Japan","","Mass-market brewer","Japanese brewer of Super Dry; owns Pilsner Urquell since 2017.",["Asahi Super Dry"],W+"Asahi_Super_Dry",["Super Dry","Dry Crystal","Dry Zero"],rel=["Plzeňský Prazdroj"]),
 B("Grupo Modelo","Mexico","","Mass-market brewer (AB InBev)","Mexico City brewer of Corona, Modelo and Victoria; Constellation Brands holds the US rights.",["Corona Extra","Modelo Especial","Victoria"],W+"Negra_Modelo",["Corona Extra","Modelo Especial","Negra Modelo","Victoria"],rel=["Anheuser-Busch"]),
 B("Miller Brewing Company","United States","","Mass-market brewer (Molson Coors)","US brewer that launched Miller Lite nationally in 1975; now part of Molson Coors.",["Miller Lite"],W+"Miller_Lite",["Miller Lite"],rel=["Coors Brewing Company"]),
 B("Coors Brewing Company","United States","","Mass-market brewer (Molson Coors)","US brewer of Coors Light, introduced in 1978; now part of Molson Coors.",["Coors Light"],W+"Coors_Light",["Coors Light"],rel=["Miller Brewing Company"]),
 B("Rheingold Breweries","United States","","Historic brewer","Brooklyn brewer that introduced Gablinger's Diet Beer in 1967.",["Gablinger's Diet Beer"],W+"Pale_lager"),
 B("Bitburger Brewery","Germany","1817","Pilsner brewer","Bitburg brewery founded by Johann Wallenborn, known for Bitburger Pilsner.",["Bitburger Pilsner"],W+"Bitburger_Brewery",["Bitburger Pilsner","Bitburger Alkoholfrei (Drive)","Bit Sun"]),
 B("Friesisches Brauhaus zu Jever","Germany","1848","Pilsner brewer (Radeberger Group)","Frisian brewery founded by Diedrich König, maker of Jever Pilsener; part of the Oetker Group's Radeberger Group.",["Jever Pilsener"],W+"Jever_(beer)",["Jever Pilsener","Fun","Light","Maibock"]),
 B("Plzeňský Prazdroj","Czech Republic","1842","Pilsner brewery (Asahi)","Plzeň brewery of Pilsner Urquell, the first golden lager; owned by Asahi since 2017.",["Pilsner Urquell"],W+"Pilsner_Urquell",["Pilsner Urquell"],["SABMiller, 1999–2017","Asahi, from 2017"],rel=["Asahi Breweries"]),
 B("Budějovický Budvar","Czech Republic","1895","State-owned lager brewery","České Budějovice brewery of Budvar lager, sold as Czechvar in some markets.",["Budějovický Budvar Original"],W+"Budweiser_Budvar_Brewery",["Original","Classic","Dark","Free","Cryo"]),
 B("Spaten-Franziskaner-Bräu","Germany","1397","Munich brewery (AB InBev)","Munich brewery that introduced Märzen in 1841 and Münchner Hell in 1894.",["Spaten Münchner Hell","Spaten Ur-Märzen"],W+"Spaten-Franziskaner-Bräu",["Münchner Hell","Oktoberfestbier","Ur-Märzen","Franziskaner"],rel=["Anheuser-Busch"]),
 B("Augustiner-Bräu","Germany","1328","Munich brewery","Munich's oldest brewery, known for Lagerbier Hell and Edelstoff.",["Augustiner Lagerbier Hell"],W+"Augustiner-Bräu",["Lagerbier Hell","Edelstoff","Oktoberfestbier","Maximator"]),
 B("Dortmunder Union","Germany","","Historic Dortmund brewery","Dortmund brewery that originated Dortmunder Export in 1873.",["Dortmunder Union Export"],W+"Dortmunder_Export"),
 B("Dreher","Austria","","Historic Vienna brewery","Vienna brewery of Anton Dreher, who developed Vienna lager in the late 1830s.",["Dreher Vienna lager"],W+"Vienna_lager",eras=["Anton Dreher, late 1830s"])]
notes=("All 7 old kinds kept (Czech premium pale lager renamed Czech pale lager); 3 new kinds added (Dortmunder Export, Kellerbier, Festbier). "
 "Old homebrew/craft models kept in m. Commercial examples taken from BJCP 2021 pages and Wikipedia; makers in m are the brewery brand names. "
 "Left out: Negra Modelo as a Vienna archetype (Wikipedia calls it Dunkel-style; Victoria used instead); Samuel Adams Boston Lager (page calls it only 'amber lager'); "
 "Singha, Red Stripe, Foster's etc. (maker not on a retrieved page); Kellerbier commercial examples (none named on retrieved pages); Wikipedia 'Oktoberfest_beer' page 404. "
 "Augustiner Oktoberfest placed in Festbier per BJCP 2021 although Wikipedia calls it a Märzen. No craft tradition entries (industrial styles).")
out={"kinds":K,"brands":Bs,"traditions":[],"notes":notes}
p='work/J7/shelves/04_00.json'; open(p+'.tmp','w').write(json.dumps(out,ensure_ascii=False,indent=1)); os.replace(p+'.tmp',p)
