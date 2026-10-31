import json,os
W='https://en.wikipedia.org/wiki/'
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def B(n,c,f,seg,kf,d,s,sig=None):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if sig: b["sig"]=sig
    return b
def T(n,g,r,p,d,tech,mat,forms,ctr,auth,s): return {"n":n,"g":g,"r":r,"p":p,"d":d,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":s}
SG=W+"Studio_glass"; AG=W+"Art_glass"; SGL=W+"Stained_glass"; CH=W+"Dale_Chihuly"
kinds=[
 {"n":"Studio glass","a":"glass art · contemporary art glass","d":"Glass made as sculptural or decorative art by the artist in a small workshop, since the 1962 Toledo workshops.",
  "t":["blown","flameworked","cast","kiln-formed","cold-worked","installation element","signed and dated"],
  "s":SG,
  "x":[
   {"n":"Littleton Toledo glass","a":"American Studio Glass origin","d":"Work of the movement begun by Harvey Littleton and chemist Dominick Labino at the Toledo Museum of Art in 1962.","mk":"Harvey Littleton","y":"1962","s":W+"Harvey_Littleton",
    "v":[V("First Toledo workshop","Harvey Littleton","1962","23 March–1 April"),V("Second Toledo workshop","Harvey Littleton","1962","18–30 June"),V("First university hot-glass programme, Wisconsin–Madison","Harvey Littleton")],
    "dt":"hot-shop vs studio · signed · date"},
   {"n":"Chihuly Macchia","a":"Chihuly series","d":"Dale Chihuly's blown-glass series, each with its own form and palette; Macchia shows nearly every studio colour.","mk":"Dale Chihuly","y":"1975 onward","s":CH,
    "v":[V("Navajo Blanket","Dale Chihuly","1975"),V("Basket","Dale Chihuly","1977"),V("Seaform","Dale Chihuly","1980"),V("Macchia","Dale Chihuly","1981"),V("Persian","Dale Chihuly","1986"),V("Venetian","Dale Chihuly","1988"),V("Chandeliers","Dale Chihuly","1992")],
    "dt":"series · colour · scale · studio team vs maestro-signed"},
   {"n":"Tagliapietra glass","a":"Lino Tagliapietra","d":"Murano-trained maestro Lino Tagliapietra's blown glass, made as studio art from the 1980s.","mk":"Lino Tagliapietra","y":"1980s onward","s":W+"Lino_Tagliapietra",
    "v":[V("Endeavor (35 suspended boats)","Lino Tagliapietra","","acquired by the Columbus Museum of Art in 2012")],
    "dt":"form · colour · signed and dated · apprenticed under Archimede Seguso from 1946"},
   {"n":"Zynsky filet-de-verre vessel","a":"Toots Zynsky","d":"Vessels of fine fused glass threads pulled from canes and shaped over moulds, a technique developed by Toots Zynsky.","mk":"Toots Zynsky","y":"1980s onward","s":W+"Toots_Zynsky",
    "v":[V("Rakow Commission","Toots Zynsky","1988"),V("Corning residency","Toots Zynsky","2016")],
    "dt":"thread colour · mould shape · signed"}]},
 {"n":"Art glass","a":"decorative glass · iridescent glass","d":"Decorative glass made as sculpture or ornament rather than for use, mostly since the mid-19th century.",
  "t":["iridescent","cameo","pâte de verre","cased","Art Nouveau","Art Deco","Murano studio piece"],
  "s":AG,
  "x":[
   {"n":"Tiffany Favrile glass","a":"Favrile","d":"Iridescent art glass made at Louis Comfort Tiffany's Tiffany Furnaces in Corona, Queens; colour is part of the glass.","mk":"Tiffany Studios","y":"1894–1930s","s":W+"Favrile_glass",
    "v":[V("Patent","Tiffany Studios","1894"),V("First Favrile objects","Tiffany Studios","1896"),V("Flower-form bud vase","Tiffany Studios")],
    "dt":"form · iridescence · engraved Tiffany/LCT mark · number"},
   {"n":"Steuben Aurene","a":"Gold Aurene · Carder glass","d":"Frederick Carder's iridescent art glass for Steuben, comparable to Tiffany's.","mk":"Steuben","y":"1903 onward","s":W+"Steuben_Glass_Company",
    "v":[V("Gold Aurene","Steuben"),V("Steuben founded by Carder and Hawkes","Steuben","1903"),V("Corning acquires Steuben","Steuben","1918")],
    "dt":"colour · form · etched Steuben/Aurene signature"},
   {"n":"Gallé cameo vase","a":"Émile Gallé cameo glass","d":"Layered coloured glass carved or etched through to plant and flower designs, by Émile Gallé of Nancy.","mk":"Gallé","y":"1880s–1904","s":W+"%C3%89mile_Gall%C3%A9",
    "v":[V("Cross of Lorraine mark","Gallé","after 1871"),V("École de Nancy formally organised","Gallé","1901"),V("Fiori Oscuri vase","Gallé")],
    "dt":"layers · technique (acid or wheel) · signature · series"},
   {"n":"Daum cameo glass","a":"Daum Nancy","d":"Floral cameo vases and lamps from the Daum glassworks, a founding member of the École de Nancy.","mk":"Daum","y":"c. 1890–1914","s":W+"Cameo_glass",
    "v":[V("Glass lamps and vases with floral designs","Daum")],
    "dt":"layers · enamel · signed Daum Nancy with Cross of Lorraine"},
   {"n":"Loetz iridescent glass","a":"Loetz Witwe","d":"Iridescent coloured Art Nouveau glass from Klostermühle in Bohemia, rivalling Tiffany's.","mk":"Loetz","y":"1860s–1940","s":W+"Joh._Loetz_Witwe",
    "v":[V("Works bought by Susanne Loetz","Loetz","1850"),V("Max Ritter von Spaun takes over","Loetz","1879")],
    "dt":"iridescence · decor name · engraved signature or unsigned · Passau Glass Museum holds largest collection"},
   {"n":"Venini Fazzoletto vase","a":"handkerchief vase","d":"The handkerchief-shaped Venini vase designed by Paolo Venini with Fulvio Bianconi.","mk":"Venini","y":"c. 1948","s":W+"Paolo_Venini",
    "v":[V("Fazzoletto series","Venini","c. 1948","with Fulvio Bianconi; cross-link to home decor B4")],
    "dt":"colour · size · acid stamp · Murano origin"}]},
 {"n":"Stained-glass panel","a":"leaded glass panel · autonomous panel","d":"A leaded or copper-foil glass picture made to be hung or framed, not set in a building's window.",
  "t":["lead came","copper foil","painted and fired","opalescent glass","framed window panel","light box"],
  "s":SGL,
  "x":[
   {"n":"Harry Clarke window and panel","a":"Harry Clarke Studios","d":"Windows and panels by the Dublin artist Harry Clarke, known for deep blues and leading built into the design.","mk":"Harry Clarke Studios","y":"1913–1931","s":W+"Harry_Clarke",
    "v":[V("Saint Gobnait window","Harry Clarke Studios","1916"),V("Eve of St Agnes window","Harry Clarke Studios","","now in the Hugh Lane Gallery"),V("Geneva Window","Harry Clarke Studios","1930","Wolfsonian, Miami")],
    "dt":"subject · size · studio number · museum comparison"},
   {"n":"Tiffany leaded glass","a":"opalescent glass window","d":"Windows and glass pictures in Tiffany's opalescent streaky glass; Favrile glass went into windows and mosaics.","mk":"Tiffany Studios","y":"1878–1932","s":SGL,
    "v":[V("Stained glass windows in Favrile glass","Tiffany Studios","","Favrile page")],
    "dt":"opalescent glass · copper foil vs lead came · designer · studio stamp"}]}
]
brands=[
 B("Tiffany Studios","United States","","Premium","Favrile glass","New York studios of Louis Comfort Tiffany, maker of Favrile art glass and windows.",W+"Favrile_glass"),
 B("Steuben","United States","1903","Premium","Aurene, crystal","Corning, New York glassworks founded by Frederick Carder and Thomas G. Hawkes in 1903.",W+"Steuben_Glass_Company"),
 B("Gallé","France","","Heritage manufactory","cameo glass","Nancy glassworks of Émile Gallé (1846–1904), founder of the École de Nancy.",W+"%C3%89mile_Gall%C3%A9"),
 B("Daum","France","","Heritage manufactory","cameo glass, crystal","Nancy crystal manufactory, a founding member of the École de Nancy.",W+"%C3%89cole_de_Nancy"),
 B("Loetz","Czech Republic","","Heritage manufactory","iridescent glass","Bohemian art glassworks at Klostermühle, bought by Susanne Loetz in 1850; ended after the Second World War.",W+"Joh._Loetz_Witwe"),
 B("Venini","Italy","1921","Premium","Murano design glass","Murano firm founded in 1921 by Paolo Venini and Giacomo Cappellin.",W+"Paolo_Venini",["Venini Fazzoletto vase"]),
 B("Harry Clarke Studios","Ireland","","Artisan & independent","stained glass","Dublin studio, Joshua Clarke & Sons, run by Harry and Walter Clarke from 1921.",W+"Harry_Clarke")]
trad=[
 T("Murano glass","Glass","Murano, Venice, Italy","from 1291","Venetian glass centre after a 1291 law moved furnaces to the island; cristallo, lattimo, millefiori, murrine.","hot-working, enamelling, engraving, cane-based murrine","glass",["Venini Fazzoletto vase","Murano glass figure"],["Murano","Venini"],"Artistic Glass Murano trademark (1994) certifies Murano origin",W+"Venetian_glass"),
 T("École de Nancy","Glass","Nancy, France","1894–1914","Art Nouveau group organised in 1901 under Émile Gallé; members included Daum, Majorelle and Vallin.","cameo glass, glass marquetry","glass",["Gallé cameo vase","Daum cameo glass"],["Gallé","Daum"],"Signatures with Cross of Lorraine",W+"%C3%89cole_de_Nancy"),
 T("American Studio Glass movement","Glass","United States","1962 onward","Movement begun with Harvey Littleton's 1962 Toledo workshops, making glass in artists' studios.","glassblowing, flameworking, casting, kiln-forming, cold working","glass",["Chihuly Macchia","Littleton Toledo glass"],["Toledo Museum of Art","Pilchuck Glass School (1971)"],"Signed and dated studio work",SG)]
notes="Old data empty. Left out for lack of retrieved support: Lalique pâte de verre, Daum pâte de verre, Tiffany Chapel and named Tiffany windows, Murano studio pieces beyond Venini. Tiffany lamps stay in B3. Daum cameo archetype rests on the cameo glass and École de Nancy pages. Dates for Favrile conflict across pages (1892 vs 1894); Favrile page gives 1894 patent."
json.dump({"kinds":kinds,"brands":brands,"traditions":trad,"notes":notes},open('work/F2/shelves/06_01.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/F2/shelves/06_01.tmp','work/F2/shelves/06_01.json')
