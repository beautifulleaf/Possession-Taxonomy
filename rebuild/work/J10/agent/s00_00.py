import json
W='https://en.wikipedia.org/wiki/'
def x(n,mk,y,s,d,v=None,dt='',a=''):
    r={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a1,"mk":mk,"y":b1,"d":c1} for a1,b1,c1 in v]
    if dt: r["dt"]=dt
    return r
xs=[
x("Cohiba Línea Clásica","Cohiba","1966",W+"Cohiba_(cigar)","Original Cohiba range, made at El Laguito.",
 [("Robusto","","4⅞ in × 50"),("Lanceros","","7½ in × 38"),("Espléndido","","7 in × 47"),("Corona Especial","","6 in × 38"),("Exquisito","","4⅞ in × 33"),("Panetela","","4½ in × 26")],"vitolas · band · box"),
x("Cohiba Siglo","Cohiba","",W+"Cohiba_(cigar)","Cohiba range of six numbered vitolas (Siglo I to VI).",
 [("Siglo I","","4 in × 40"),("Siglo II","","5⅛ in × 42"),("Siglo III","","6⅛ in × 42"),("Siglo IV","","5⅝ in × 46"),("Siglo V","","6¾ in × 43"),("Siglo VI","","5⅞ in × 52")]),
x("Cohiba Maduro 5","Cohiba","",W+"Cohiba_(cigar)","Cohiba line using aged maduro-style wrapper.",
 [("Genios","","5½ in × 52"),("Mágicos","","4½ in × 52"),("Secretos","","4⅜ in × 40")]),
x("Cohiba Behike","Cohiba","",W+"Cohiba_(cigar)","Top-tier Cohiba line in three sizes.",
 [("BHK 52","","4½ in"),("BHK 54","","5½ in"),("BHK 56","","6½ in")]),
x("Montecristo Línea Clásica","Montecristo","1935",W+"Montecristo_(cigar)","Original Montecristo range founded 1935, led by No. 2 (pirámide) and No. 4.",
 [("No. 2","","pirámide, widely described as most popular"),("No. 4","","best-selling Cuban cigar per article"),("Edmundo","2004","large robusto"),("Especial No. 1","",""),("Joyita","","")]),
x("Montecristo Open","Montecristo","2009",W+"Montecristo_(cigar)","Lighter-bodied Montecristo line launched February 2009; vitola names draw on golf and yachting."),
x("Partagás Serie D","Partagás","1975",W+"Partag%C3%A1s_(cigar_brand)","Partagás range around the Serie D No. 4 robusto, introduced 1975.",
 [("Serie D No. 4","1975","4⅞ in × 50, robusto"),("Serie D No. 3","2001","Edición Limitada"),("Serie D No. 2","2003","Edición Limitada"),("Serie D No. 1","2004","Edición Limitada"),("Serie D No. 5","2008","Edición Limitada"),("Serie D Especial","2010","Edición Limitada")]),
x("Partagás Serie P","Partagás","2005",W+"Partag%C3%A1s_(cigar_brand)","Partagás pyramid line; Serie P No. 2 introduced as a regular size in 2005.",
 [("Serie P No. 2","2005","6⅛ in × 52, pirámide")]),
x("Partagás Classic Vitolas","Partagás","1845",W+"Partag%C3%A1s_(cigar_brand)","Traditional Partagás sizes outside the Series lines.",
 [("Presidente","","6¼ in × 47"),("Lusitania","","7⅝ in × 49"),("Partagás de Luxe","","5½ in × 40"),("Culebras","","5¾ in × 39")]),
x("H. Upmann Magnum","H. Upmann","",W+"H._Upmann","Cuban H. Upmann range of thick Magnum sizes plus Edición Limitada releases.",
 [("Magnum 46","","5.6 in × 46"),("Magnum 50","2008","6.3 in × 50"),("Magnum 50 EL","2005","Edición Limitada"),("Magnum 48 EL","2009","4.3 in × 48"),("Magnum 56 EL","2015","5.9 in × 56")]),
x("H. Upmann Classic Vitolas","H. Upmann","1844",W+"H._Upmann","Traditional H. Upmann sizes.",
 [("Sir Winston","","7 in × 47"),("Corona Major","","5.2 in × 42")]),
x("Romeo y Julieta Churchill","Romeo y Julieta","1875",W+"Romeo_y_Julieta_(cigar)","Romeo y Julieta flagship 7 in × 47 vitola named for Winston Churchill, with shorter and wider variants.",
 [("Churchill","","7 in × 47"),("Short Churchill","","4⅞ in × 50"),("Wide Churchill","","5⅛ in × 55")]),
x("Hoyo de Monterrey Epicure","Hoyo de Monterrey","1865",W+"Hoyo_de_Monterrey","Hoyo de Monterrey's prized Epicure sizes and Double Coronas.",
 [("Epicure No. 2","","4.9 in × 50"),("Epicure No. 1","","5.6 in × 46"),("Double Coronas","","7.6 in × 49"),("Le Hoyo des Dieux","","6.1 in × 42")]),
x("Bolívar","Bolívar","c.1901",W+"Bol%C3%ADvar_(cigar_brand)","Cuban Bolívar range, known for full-bodied belicosos and coronas.",
 [("Belicoso Fino","","5½ in × 52"),("Royal Corona","","4⅞ in × 50"),("Corona Gigante","","7 in × 47"),("Petit Corona","","5⅛ in × 42"),("Libertadores","","6.5 in × 54, special release")]),
x("Punch","Punch","1840",W+"Punch_(cigar)","Cuban Punch range of Churchill, Double Corona and Royal Selection sizes.",
 [("Double Corona","","7⅝ in × 49"),("Churchill","","7 in × 47"),("Punch Punch","","5⅝ in × 46"),("Royal Selection No. 12","","5⅛ in × 42")]),
x("Trinidad","Trinidad","1969",W+"Trinidad_(cigar)","Former diplomatic brand made at El Laguito, on public sale from February 1998 (Fundador).",
 [("Fundador","1998","7½ in × 40"),("Coloniales","2003","5¼ in × 44"),("Reyes","2003","4⅜ in × 40"),("Robusto Extra","2003","6⅛ in × 50"),("Robusto T","","4⅞ in × 50")]),
x("Cuaba","Cuaba","1996",W+"Cuaba","All-perfecto Cuban line launched 19 November 1996.",
 [("Salomónes","","7¼ in × 57, double perfecto"),("Diademas","","9⅛ in × 55"),("Distinguidos","","6⅜ in × 52"),("Exclusivos","","5¾ in × 46"),("Generosos","","5¼ in × 42"),("Tradicionales","","4¾ in × 42"),("Divinos","","4 in × 43")]),
]
H="https://www.holts.com/clubhouse/cigar-101/cigar-shapes-sizes-guide"
kind={"n":"Habano (Cuban premium cigar)","a":"Havana cigar · Cuban cigar","d":"Hand-rolled premium cigar made in Cuba and sold by Habanos S.A., organised by house line, then vitola and limited release.",
 "t":["Robusto","Toro","Corona","Churchill","Corona gorda","Petit corona","Panatela","Double corona","Gordo","Lancero","Lonsdale","Torpedo","Belicoso","Perfecto","Diadema","Culebra"],
 "s":H,"x":xs,
 "m":[["Por Larranaga Petit Corona","Por Larranaga"],["Rafael Gonzalez Petit Corona","Rafael Gonzalez"],["Sancho Panza Belicoso","Sancho Panza"]]}
kind["d"]="Hand-rolled premium cigar made in Cuba for Habanos S.A.; vitolas are parejos (corona 5½-6 in × 42-44, robusto, toro, churchill, double corona, lancero) or figurados (torpedo, belicoso, perfecto, diadema, culebra)."
def b(n,f,kf,d,lines,s=W+"Habanos_S.A."):
    return {"n":n,"c":"Cuba","f":f,"seg":"Heritage manufactory","kf":kf,"d":d,"lines":lines,"sig":lines[:2],"rel":["Habanos S.A."],"s":s}
brands=[
{"n":"Habanos S.A.","c":"Cuba","f":"1994","seg":"Institution & issuer","kf":"Cuban cigars","d":"Havana-based marketer and distributor of Cuban premium cigars, jointly owned by Cubatabaco and Altadis.","s":W+"Habanos_S.A.","rel":["Cohiba","Montecristo"]},
b("Cohiba","1966","flagship","Cuban brand made at El Laguito, launched 1966 and on public sale from 1982.",["Línea Clásica","Siglo","Maduro 5","Behike"],W+"Cohiba_(cigar)"),
b("Montecristo","1935","No. 2, No. 4","Cuban brand created in 1935 by Alonso Menéndez.",["Línea Clásica","Open","Edmundo"],W+"Montecristo_(cigar)"),
b("Partagás","1845","Serie D No. 4","Cuban brand founded by Jaime Partagás y Ravell in Havana.",["Serie D","Serie P"],W+"Partag%C3%A1s_(cigar_brand)"),
b("H. Upmann","1844","Magnum","Cuban brand founded by banker Hermann Dietrich Upmann (cigar production from 1844).",["Magnum","Sir Winston"],W+"H._Upmann"),
b("Romeo y Julieta","1875","Churchill","Cuban brand established 1875 by Inocencio Alvarez and Manin García.",["Churchill","Short Churchill","Wide Churchill"],W+"Romeo_y_Julieta_(cigar)"),
b("Hoyo de Monterrey","1865","Epicure","Cuban brand registered 1865 by José Gener y Batet.",["Epicure","Le Hoyo"],W+"Hoyo_de_Monterrey"),
b("Bolívar","c.1901","full-bodied","Cuban brand founded about 1901-02 by José F. Rocha, registered in Havana in 1921.",["Belicoso Fino","Royal Corona"],W+"Bol%C3%ADvar_(cigar_brand)"),
b("Punch","1840","Double Corona","Cuban brand first registered in 1840 by a German named Stockmann.",["Double Corona","Churchill","Royal Selection"],W+"Punch_(cigar)"),
b("Trinidad","1969","ex-diplomatic","Cuban brand first produced in 1969 at El Laguito; public sale from 1998.",["Fundador","Reyes","Robusto Extra"],W+"Trinidad_(cigar)"),
b("Cuaba","1996","perfectos","Cuban all-perfecto line launched in 1996.",["Salomónes","Distinguidos"],W+"Cuaba"),
]
trad=[{"n":"Cuban cigar rolling","g":"Food & drink","r":"Cuba (Pinar del Río, Havana)","p":"19th century to present","d":"Hand rolling of premium cigars by torcedores from tobacco grown in the Vuelta Abajo.",
 "tech":"Hand rolling (totalmente a mano) by torcedores, mostly women today","mat":"Tobacco from Vuelta Abajo and Semi Vuelta, Pinar del Río",
 "forms":["Habano","Robusto","Churchill","Lancero"],"ctr":["Vuelta Abajo","El Laguito","Partagás factory"],"auth":"Boxes and labels carry 'Hecho en Cuba'; 'Totalmente a mano' marks fully handmade cigars.","s":W+"Cuban_cigar"}]
json.dump({"kinds":[kind],"brands":brands,"traditions":trad,"notes":"Vitola kinds dissolved into t; 9 old models became versions or stayed in m (Por Larranaga, Rafael Gonzalez, Sancho Panza lacked a retrieved page). Houses not in the register or archetypes (Ramón Allones, San Cristóbal, Quai d'Orsay, Vegas Robaina, Juan López, Diplomáticos, El Rey del Mundo, Vegueros, José L. Piedra, Sancho Panza etc.) left out for lack of retrieved pages. Edición Regional/Reserva/Gran Reserva releases not found in fetched pages; omitted."},open('s00_00.json','w'),ensure_ascii=False)
