import json, os
W='https://en.wikipedia.org/wiki/'
DH='https://www.diffordsguide.com/bws/1252/vermouth/history'
DC='https://www.diffordsguide.com/beer-wine-spirits/322/carpano-antica-formula'
def A(n,d,mk,y,s,v=(),a="",dt=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if v: x["v"]=[dict(n=a1,mk=b,y=c,d=e) for a1,b,c,e in v]
    if dt: x["dt"]=dt
    return x
verm={"n":"Vermouth","a":"vermut · vermouth di Torino · vermouth de Chambéry",
 "d":"Wine flavoured with wormwood and other botanicals and fortified, sold to drink.",
 "t":["rosso (sweet red)","dry / extra dry","bianco / blanc","rosé","ambré / amber"],
 "s":"https://www.wine.com/list/wine/dessert-sherry-and-port/7155-128",
 "x":[
  A("Turin sweet vermouth","Sweet red vermouth from Turin, first sold by Antonio Benedetto Carpano in 1786; now protected as Vermouth di Torino.","","1786 · Vermouth di Torino defined 2017",DH,
    [("Vermouth di Torino","","2017","Piedmont-made from Italian wine, mainly Piedmontese wormwood, 16–22% ABV (Ministerial Decree 1826)"),
     ("Cocchi Vermouth di Torino","Giulio Cocchi","","sweet red; Best Sweet Vermouth, Bartender's Best Awards 2014")],
    a="vermouth rosso · Italian vermouth",dt="rosso · Superiore · ABV 16–22%"),
  A("Carpano Antica Formula","Vanilla-scented rosso vermouth recreated by Fratelli Branca from a late-1780s Carpano recipe found in the firm's papers.","Carpano","late 1780s recipe · recreated 2001",DC,
    [("Carpano Antica Formula","Fratelli Branca","2001","16.5% ABV; bottle copied from an old Carpano design")],dt="rosso · 16.5% ABV"),
  A("Punt e Mes","Deep red Turin vermouth balancing sweetness with bitterness; the name means 'point and a half' in Piedmontese.","Carpano","",W+"Punt_e_Mes",
    [("Carpano Punt e Mes","Carpano","","made in Turin by the Carpano family until 2001, now by Fratelli Branca")]),
  A("Martini","Turin-area vermouth range from Pessione and the top-selling international vermouth brand.","Martini & Rossi","1863",W+"Martini_(vermouth)",
    [("Martini Rosso","Martini & Rossi","1863","sweet red"),("Martini Extra Dry","Martini & Rossi","1900","launched New Year's Day"),
     ("Martini Bianco","Martini & Rossi","1910","sweet white"),("Martini Rosato","Martini & Rossi","1980","rosé"),
     ("Martini Fiero","Martini & Rossi","1998","orange-led; new version 2017"),
     ("Martini Riserva Speciale Ambrato","Martini & Rossi","2015",""),("Martini Riserva Speciale Rubino","Martini & Rossi","2015","")],
    dt="rosso · bianco · extra dry · rosato"),
  A("Cinzano","Turin vermouth house founded in 1757 by the brothers Giovanni Giacomo and Carlo Stefano Cinzano.","Cinzano","1757",W+"Cinzano",
    [("Cinzano Rosso","Cinzano","",""),("Cinzano Bianco","Cinzano","",""),("Cinzano Extra Dry","Cinzano","",""),("Cinzano Rosé","Cinzano","","")]),
  A("Noilly Prat Original Dry","The classic dry, straw-coloured French vermouth from Marseillan, from Joseph Noilly's 1813 formula.","Noilly Prat","1813",W+"Noilly_Prat",
    [("Noilly Prat Original Dry","Noilly Prat","1813","main product"),("Noilly Prat Extra Dry","Noilly Prat","1979","North America 1979–2009, returned 2012"),
     ("Noilly Prat Rouge","Noilly Prat","1960s","red"),("Noilly Prat Ambré","Noilly Prat","1980s","amber")],a="French vermouth · dry vermouth"),
  A("Vermouth de Chambéry","Light Alpine vermouth from Chambéry, where Joseph Chavasse began in 1821 and the blanc style was created.","Dolin","1821",DH,
    [("Dolin Blanc Vermouth de Chambéry","Dolin","1881","the first blanc; may have inspired Martini Bianco"),
     ("Dolin Rouge Vermouth de Chambéry","Dolin","",""),],dt="dry · blanc · rouge"),
 ],
 "m":[["Gonzalez Byass La Copa Vermouth Extra Seco","Gonzalez Byass"],["Miguel Torres Casals Vermouth Dry NV","Miguel Torres"],
      ["Alessio Vermouth Bianco","Alessio"],["Bordiga Extra Dry Vermouth","Bordiga"],["Lo-Fi Aperitifs Sweet Vermouth","Lo-Fi Aperitifs"]]}
quin={"n":"Quinquina & americano","a":"quinquina · americano · aperitif wine · chinato",
 "d":"Wine aromatised with cinchona bark (quinine) and other botanicals, drunk as an aperitif or digestif.",
 "t":["blanc","rouge","rosé"],
 "s":"https://bottlebarn.com/products/byrrh-grand-quinquina-750ml",
 "x":[
  A("Dubonnet","French quinine aperitif wine created for a government competition to help Foreign Legionnaires take quinine.","Dubonnet","1846",W+"Dubonnet",
    [("Dubonnet Rouge","Dubonnet","",""),("Dubonnet Blanc","Dubonnet","",""),("Dubonnet Gold","Dubonnet","","vanilla and orange")]),
  A("Byrrh","Red-wine and mistelle quinquina from Thuir near Perpignan, made by the Violet brothers.","Byrrh","1866",W+"Byrrh",
    [("Byrrh Grand Quinquina","Byrrh","","")]),
  A("Lillet","Bordeaux-wine aperitif from Podensac, formerly Kina Lillet, the quinquina of the Vesper cocktail.","Lillet","1872",W+"Lillet",
    [("Kina Lillet","Lillet","1887","made until 1986"),("Lillet Dry","Lillet","1920","for the British market"),
     ("Lillet Rouge","Lillet","1962",""),("Lillet Blanc","Lillet","1986","replaced Kina Lillet after the 1985 reformulation"),("Lillet Rosé","Lillet","2011","")]),
  A("Cocchi Americano","Quinine-flavoured Americano aperitif wine from Asti, a common stand-in for Kina Lillet.","Giulio Cocchi","1891",W+"Cocchi_Americano",
    [("Cocchi Americano","Giulio Cocchi","1891","white"),("Cocchi Americano Rosa","Giulio Cocchi","","pink; more bitter and aromatic")],a="Aperitivo Americano"),
  A("Barolo Chinato","Digestif made by steeping cinchona bark and house spices in old Barolo.","","",W+"Barolo_Chinato",
    [("Cocchi Barolo Chinato","Giulio Cocchi","","")],dt="cinnamon · coriander · iris · mint · vanilla"),
 ],
 "m":[["Bonal Gentiane Quina","Bonal"],["St. Raphael Rouge","St. Raphael"]]}
sang={"n":"Sangria & mulled wine","a":"Gluhwein · aromatised wine-based drink",
 "d":"Wine flavoured with fruit, spices or herbs and not fortified, sold as sangria, mulled wine and the like.",
 "s":"https://groceries.morrisons.com/products/gluhwein-mulled-wine/114562503",
 "x":[
  A("Sangria","Spanish and Portuguese punch of red wine and chopped fruit; under EU rules only these countries may use the name.","","EU name rule 2014",W+"Sangria",
    [("Sangria blanca","","","white-wine version"),("Sangria de cava","","","made with cava"),("Clarea","","2014","white-wine drink; name reserved to Spain")],dt="red · white · cava"),
  A("Glühwein","Hot spiced red wine of the German-speaking countries and Alsace, sold ready to heat.","","",W+"Mulled_wine",
    [("Gluhwein","Continental Wine and Food Ltd","","ready-to-heat bottle")],a="mulled wine · vin chaud · vin brulé · svařák · grzaniec"),
  A("Glögg","Spiced Swedish-origin mulled wine or spirit drunk at Christmas, sold ready-made in the Nordic countries.","","",W+"Gl%C3%B6gg",
    a="gløgg · glögi",dt="red · white · blackcurrant · alcohol-free"),
 ]}
rets={"n":"Retsina","a":"resinated wine",
 "d":"Greek white or rosé wine flavoured with Aleppo pine resin added during fermentation.",
 "t":["white","rosé"],
 "s":"https://www.lcbo.com/en/kechribari-retsina-27137",
 "x":[A("Retsina","Greek resinated wine, mainly from Savatiano, protected in the EU for Greece and parts of Cyprus.","","ancient · EU traditional appellation",W+"Retsina",
    [("Kourtaki Retsina","Kourtaki","",""),("Malamatina Retsina","Malamatina","","")],dt="Savatiano · Assyrtiko · Rhoditis · Athiri (Rhodes) · Attica, Boeotia, Euboea")],
 "m":[["Kechribari Retsina","Kechribari"]]}
def B(n,c,f,seg,d,s,lines=(),sig=(),rel=()):
    b={"n":n,"c":c,"f":f,"seg":seg,"d":d,"s":s}
    if lines: b["lines"]=list(lines)
    if sig: b["sig"]=list(sig)
    if rel: b["rel"]=list(rel)
    return b
brands=[
 B("Carpano","Italy","","Vermouth","Turin vermouth house of the Carpano family; owned by Fratelli Branca since 2001.",W+"Punt_e_Mes",sig=["Carpano Antica Formula","Punt e Mes"]),
 B("Martini & Rossi","Italy","1847","Vermouth & sparkling wine","Pessione vermouth maker, named Martini & Rossi in 1879; part of Bacardi since 1992.",W+"Martini_(vermouth)",lines=["Rosso","Bianco","Extra Dry","Rosato","Riserva Speciale"],sig=["Martini"],rel=["Noilly Prat"]),
 B("Cinzano","Italy","1757","Vermouth & sparkling wine","Turin vermouth house; Campari owned it 1999–2025, now Gruppo Caffo 1915.",W+"Cinzano",sig=["Cinzano"]),
 B("Noilly Prat","France","1855","Vermouth","Marseillan dry vermouth house from Joseph Noilly's 1813 formula; owned by Martini & Rossi (Bacardi).",W+"Noilly_Prat",sig=["Noilly Prat Original Dry"],rel=["Martini & Rossi"]),
 B("Dolin","France","1821","Vermouth","Chambéry vermouth house begun by Joseph Chavasse; named after Louis-Ferdinand Dolin, who bought it in 1852.",DH,sig=["Vermouth de Chambéry"]),
 B("Giulio Cocchi","Italy","1891","Aperitif wine & sparkling","Asti winery founded by pastry chef Giulio Cocchi, known for Americano, Vermouth di Torino and Barolo Chinato.",W+"Giulio_Cocchi_Spumanti",sig=["Cocchi Americano","Barolo Chinato"]),
 B("Lillet","France","1872","Aperitif wine","Podensac aperitif house of Paul and Raymond Lillet; owned by Pernod Ricard since 2008.",W+"Lillet",sig=["Lillet"],rel=["Byrrh","Dubonnet"]),
 B("Dubonnet","France","1846","Aperitif wine","Quinine aperitif by Joseph Dubonnet; Pernod Ricard in France, Heaven Hill in the US.",W+"Dubonnet",sig=["Dubonnet"]),
 B("Byrrh","France","1866","Aperitif wine","Thuir quinquina of the Violet brothers; Pernod Ricard since 1977.",W+"Byrrh",sig=["Byrrh"]),
]
out={"kinds":[verm,quin,sang,rets],"brands":brands,"traditions":[],
 "notes":"All four old kinds kept (k67 Vermouth, k70 Quinquina→Quinquina & americano, k68, k69); old models turned into archetype versions where they fit, rest kept in m (Spanish vermut, Alessio, Bordiga, Lo-Fi, Bonal, St. Raphael, Kechribari). Left out: Vermouth de Chambéry 1932 AOC date and Dolin Dry (only in search snippets/retailers); Carpano founding year (no page); Contratto Americano, Mattei Cap Corse, Feuerzangenbowle, regional mulled-wine names beyond aliases, Gaia Ritinitis Nobilis (no retrieved page); Kourtaki/Malamatina not in brand register (no facts beyond captions). No traditions: none of these is an artisan craft tradition."}
p='/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/03_02.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
