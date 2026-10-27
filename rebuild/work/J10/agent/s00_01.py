import json
W='https://en.wikipedia.org/wiki/'
L=W+"List_of_cigar_brands"
def x(n,mk,y,s,d,v=None,dt=''):
    r={"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s}
    if v: r["v"]=[{"n":a,"mk":mk,"y":b,"d":c} for a,b,c in v]
    if dt: r["dt"]=dt
    return r
dom=[
x("Fuente Fuente OpusX","Arturo Fuente","1995",W+"Fuente_Fuente_OpusX","Arturo Fuente's top line: a Dominican puro with Rosado wrapper grown at Chateau de la Fuente; released November 1995. Cigar Aficionado 2005 Cigar of the Year (Opus X corona); Reserva d'Chateau Cigar of the Year 2023.",
 [("Double Corona","","7⅝ in × 49"),("Fuente Fuente","","5⅝ in × 46"),("Reserve d'Chateau","","7 in × 48"),("Robusto","","5¼ in × 50"),("Belicoso XXX","","4⅝ in × 49"),("Perfecxion X","","6¼ in × 48"),("Perfecxion A","","9¼ in × 47"),("Shark","","5⅝ in × 54"),("Angel's Share","","variant with middle-priming wrapper"),("Oro Oscuro","","variant with extra-aged maduro wrapper")],"13 vitolas at launch · Rosado wrapper"),
x("Arturo Fuente Hemingway","Arturo Fuente","mid-1980s",W+"Arturo_Fuente","Medium-bodied Arturo Fuente line using unusual figurado shapes; the brand's first major success."),
x("Arturo Fuente Don Carlos","Arturo Fuente","",W+"Arturo_Fuente","Arturo Fuente line named in the brand's product list; Don Carlos Eye of the Shark rated 97 and top of Cigar Aficionado's list in 2017."),
x("Davidoff Aniversario","Davidoff","1986",W+"Davidoff","Began as a 1986 limited release for Zino Davidoff's 80th birthday; an ongoing series from 1991."),
x("Davidoff Grand Cru","Davidoff","",W+"Davidoff","Name given to the former Château series after production moved to the Dominican Republic."),
x("La Flor Dominicana","La Flor Dominicana","1996",W+"La_Flor_Dominicana","Cigars of Litto Gomez and Ines Lorenzo, first called Los Libertadores; made in Tamboril, Dominican Republic."),
x("E.P. Carrillo","E.P. Carrillo","",L,"Dominican-made brand of Ernesto Perez-Carrillo, listed in Wikipedia's cigar brand list."),
]
nic=[
x("Padrón Series","Padrón","",W+"Piloto_Cigars_Inc.","Padrón's core all-Nicaraguan range of 15 vitolas in natural and maduro wrappers.",
 [("Delicias Corona Extra","","4⅞ in × 46"),("Londres Corona","","5½ in × 42"),("Palmas Double Corona","","6½ in × 54"),("Churchill","","6⅞ in × 46"),("Giant (Magnum)","","9 in × 50")]),
x("Padrón 1964 Anniversary Series","Padrón","1994",W+"Piloto_Cigars_Inc.","Range introduced in 1994 for Padrón's 30th anniversary; natural and maduro, each cigar numbered.",
 [("Diplomatico","","7 in × 50"),("Exclusivo","","5½ in × 50"),("Imperial","","6 in × 54"),("Monarca","","6½ in × 46"),("Piramide","","6⅞ in × 52")]),
x("Padrón Serie 1926","Padrón","2002",W+"Piloto_Cigars_Inc.","Blend created in 2002 for José Padrón's 75th birthday. 40th Anniversary was among Cigar Aficionado's 25 Best Cigars of 2004.",
 [("No. 9","","Robusto 5¼ in × 56"),("No. 6","","Robusto 4¾ in × 50"),("No. 1","","Toro 6¾ in × 54"),("No. 2","","Belicoso 5½ in × 52"),("40th Anniversary","2004","Torpedo 6½ in × 54")]),
x("Padrón Family Reserve","Padrón","2009",W+"Piloto_Cigars_Inc.","Six blends from 2009, each tied to a special date.",
 [("44 Years","","Torpedo 6 in × 52"),("46 Years","","Robusto Grande 5½ in × 56"),("85 Years","","Robusto 5¼ in × 50")]),
x("My Father (Garcia family)","My Father Cigars","",W+"Don_Pepin_Garcia_(cigar_brand)","Cigars of the Garcia family: José 'Pepín' García and son Jaime García, made at Tabacalera Cubana in Estelí.",
 [("My Father Le Bijou 1922","","")]),
x("Oliva Serie V","Oliva","",W+"../" if False else "https://www.cigaraficionado.com/top25cigar/oliva-serie-v-churchill-extra-2022","Oliva's Nicaraguan full-bodied line; Churchill Extra (7 in × 52) was #5 in Cigar Aficionado's Top 25 of 2022 with 95 points.",
 [("Churchill Extra","","7 in × 52")]),
x("Joya de Nicaragua Antaño","Joya de Nicaragua","",W+"Joya_de_Nicaragua","Nicaraguan heritage range of Joya de Nicaragua, whose other ranges include Cinco Decadas and Número Uno."),
x("Liga Privada","Drew Estate","2007","https://www.cigaraficionado.com/company/drew-estate","Drew Estate's private-blend line, introduced 2007; includes Liga Privada No. 9 and T52."),
x("Undercrown","Drew Estate","","https://www.cigaraficionado.com/company/drew-estate","Drew Estate line listed beside Liga Privada and ACID."),
x("Tatuaje Havana VI","Tatuaje","2003",W+"Tatuaje","Nicaraguan long-filler puro by Pete Johnson with Pepin Garcia, blended to resemble medium-bodied Havana cigars; Tatuaje released from 2003."),
x("AJ Fernández","AJ Fernandez","",L,"Nicaraguan-made brand owned by AJ Fernandez Incorporated, as listed in Wikipedia's cigar brand list."),
x("Perdomo Lot 23","Perdomo","1992",W+"Perdomo_(cigar_brand)","Perdomo line made at the 'El Monstro' factory in Estelí; the brand began in 1992 in Miami."),
]
hon=[
x("Camacho Corojo","Camacho","1962",W+"Camacho_Cigars","Camacho's Honduran-made lines (Corojo, Triple Maduro, Connecticut, Ecuador), made at the Rancho Jamastran factory in Danlí."),
x("Rocky Patel Decade","Rocky Patel","2008",W+"Rocky_Patel_Premium_Cigars","Line made to mark the brand's tenth year; Decade earned a 95 in Cigar Aficionado in 2008. Production started with El Paraíso, Honduras tobacco, later Nicaragua."),
x("Alec Bradley Prensado","Alec Bradley","2011",W+"Alec_Bradley","Prensado Churchill was Cigar Aficionado's #1 Cigar of the Year 2011; the brand also has Tempus, Black Market and Project 40.",
 [("Prensado Churchill","2011","#1 Cigar of the Year"),("Prensado Torpedo","2023","#8")]),
]
mex=[
x("Te-Amo","Te-Amo","mid-1960s","https://www.cigaraficionado.com/article/south-of-the-border-smokes-7736","Mexican brand launched after the Cuban embargo, made at the Matacapan factory in the San Andrés Valley."),
x("Santa Clara 1830","Santa Clara","","https://www.cigaraficionado.com/article/south-of-the-border-smokes-7736","Tabacos Santa Clara (Ortiz family) blend of Veracruz Havana-seed and San Andrés leaf."),
x("Dannemann","Dannemann","1873",W+"Dannemann_Cigars","Brazilian-born cigar house founded by Geraldo Dannemann in São Félix; now Germany-based."),
]
def k(n,a,d,xs,s,t=None):
    r={"n":n,"a":a,"d":d,"x":xs,"s":s}
    if t: r["t"]=t
    return r
kinds=[
k("Dominican premium cigar","Dominican puro · Dominican cigar","Handmade premium cigar made in the Dominican Republic, the largest non-Cuban producer, with Santiago and La Romana among its centres.",dom,W+"Arturo_Fuente",["Puro","Cameroon wrapper","Maduro wrapper"]),
k("Nicaraguan premium cigar","Nicaraguan puro","Handmade premium cigar made in Nicaragua, mainly in Estelí.",nic,W+"Piloto_Cigars_Inc.",["Puro","Habano wrapper","Maduro wrapper"]),
k("Honduran premium cigar","Honduran cigar","Handmade premium cigar made in Honduras, centred on Danlí and El Paraíso.",hon,W+"Camacho_Cigars",["Corojo","Maduro wrapper"]),
k("Mexican & Brazilian cigar","San Andrés cigar","Cigar from Mexico's San Andrés Valley or from Brazil's Bahia tradition.",mex,"https://www.cigaraficionado.com/article/south-of-the-border-smokes-7736",["Mexican puro","Brazilian leaf"]),
]
def b(n,c,f,seg,kf,d,s,lines=None,rel=None):
    r={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if lines: r["lines"]=lines; r["sig"]=lines[:2]
    if rel: r["rel"]=rel
    return r
A="Artisan & independent"
brands=[
b("Arturo Fuente","Dominican Republic","1912",A,"OpusX","Family cigar maker founded in West Tampa in 1912 by Arturo Fuente Sr., now producing in the Dominican Republic.",W+"Arturo_Fuente",["Fuente Fuente OpusX","Hemingway","Don Carlos"],["Ashton"]),
b("Davidoff","Switzerland","1906","Premium","Swiss luxury","Swiss house; cigars made in the Dominican Republic and Honduras, Cuban production ended in 1991.",W+"Davidoff",["Aniversario","Grand Cru","Zino"],["Camacho"]),
b("La Flor Dominicana","Dominican Republic","1996",A,"Tamboril","Founded in Santiago in 1996 by Litto Gomez and Ines Lorenzo; first called Los Libertadores.",W+"La_Flor_Dominicana"),
b("E.P. Carrillo","Dominican Republic","",A,"Dominican","Dominican-made brand of Ernesto Perez-Carrillo.",L),
b("Padrón","Nicaragua","1964",A,"Nicaraguan puro","Founded in Miami in 1964 by José Orlando Padrón; production moved to Estelí in 1970.",W+"Piloto_Cigars_Inc.",["1964 Anniversary Series","Serie 1926","Family Reserve"]),
b("My Father Cigars","Nicaragua","",A,"Garcia family","Garcia-family brand of José 'Pepín' García and son Jaime, made in Estelí.",W+"Don_Pepin_Garcia_(cigar_brand)"),
b("Oliva","Nicaragua","",A,"Serie V","Nicaraguan maker (Tabacalera Oliva); bought by Belgian J. Cortès Cigars in 2016.","https://www.cigaraficionado.com/top25cigar/oliva-serie-v-churchill-extra-2022",["Serie V"]),
b("Joya de Nicaragua","Nicaragua","1968",A,"Nicaraguan heritage","Estelí-based maker, owned since 1994 by Alejandro Martínez Cuenca.",W+"Joya_de_Nicaragua",["Antaño","Cinco Decadas","Número Uno"]),
b("Drew Estate","Nicaragua","1995",A,"infused cigars","Nicaragua's largest handmade-cigar producer, founded by Jonathan Drew and Marvin Samel.","https://www.cigaraficionado.com/company/drew-estate",["Liga Privada","Undercrown","ACID"]),
b("AJ Fernandez","Nicaragua","",A,"Nicaraguan","Nicaraguan maker owned by AJ Fernandez Incorporated.",L),
b("Perdomo","Nicaragua","1992",A,"Estelí","Started in Nick Perdomo Jr.'s Miami garage in 1992; factory in Estelí.",W+"Perdomo_(cigar_brand)",["Lot 23","20th Anniversary"]),
b("Tatuaje","United States","2003",A,"Pete Johnson","Brand of Pete Johnson, first released 2003, made with Pepin Garcia in Miami and Estelí.",W+"Tatuaje",["Havana VI","Reserva","Monster Series"]),
b("Camacho","Honduras","1962","Premium","Corojo","Founded 1962 by Simon Camacho; bought by Oettinger Davidoff Group in 2008.",W+"Camacho_Cigars",["Corojo","Triple Maduro","Connecticut"],["Davidoff"]),
b("Rocky Patel","United States","1995","Premium","Decade","Founded 1995 as Indian Tabac Cigar Co. by Rakesh Patel; renamed 2006.",W+"Rocky_Patel_Premium_Cigars",["Decade"]),
b("Alec Bradley","United States","1996",A,"Prensado","Founded 1996 by Alan Rubin; made in Honduran and Nicaraguan factories.",W+"Alec_Bradley",["Prensado","Tempus","Black Market","Project 40"]),
b("Te-Amo","Mexico","","Premium","San Andrés leaf","Mexican brand made at the Matacapan factory in the San Andrés Valley.","https://www.cigaraficionado.com/article/south-of-the-border-smokes-7736"),
b("Santa Clara","Mexico","",A,"San Andrés","Tabacos Santa Clara of the Ortiz family.","https://www.cigaraficionado.com/article/south-of-the-border-smokes-7736",["Santa Clara 1830"]),
b("Dannemann","Brazil","1873","Heritage manufactory","Brazilian origin","Founded by Geraldo Dannemann in São Félix, Brazil; now Swiss-owned and Germany-based.",W+"Dannemann_Cigars"),
]
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":"All four kinds are new. Ashton, CAO, Oliva history, AJ Fernández lines and Davidoff Millennium/Winston Churchill not found on retrieved pages; Ashton and CAO omitted, Davidoff Millennium/Winston Churchill omitted. Cigar Aficionado placements only where retrieved. Alec Bradley and Rocky Patel placed under Honduran because they began with Honduran factories. Foundation years for Davidoff from the page tags."},open('s00_01.json','w'),ensure_ascii=False)
