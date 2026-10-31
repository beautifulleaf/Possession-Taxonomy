import json, os
W='https://en.wikipedia.org/wiki/'
TQ=W+'Tequila'; MZ=W+'Mezcal'
def v(n,mk,y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
def X(n,d,mk,y,s,vs=(),dt='',a=''): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":list(vs),"dt":dt}
TDT='blanco · reposado · añejo · extra añejo · 100% agave'
tequila={"n":"Tequila","a":"","d":"Spirit distilled from blue agave (Agave tequilana) in Jalisco and set municipalities of four other Mexican states.",
 "t":["Blanco / plata (unaged or under two months)","Joven / oro (blend or coloured blanco)","Reposado (2–12 months in oak)","Añejo (1–3 years in small oak)","Extra añejo (3+ years in oak)","Cristalino (aged, filtered clear; not a NOM class)","Rosa (rested in red-wine barrels; not a NOM class)","100% agave","Mixto (at least 51% blue agave)"],
 "s":"https://en.wikipedia.org/wiki/List_of_tequilas",
 "x":[
  X("Jose Cuervo Reserva de la Familia","Cuervo's family-reserve 100% agave line, launched for La Rojeña's 200th anniversary.","Jose Cuervo","1995",W+"Jose_Cuervo",
    [v("Reserva de la Familia Extra Añejo","Jose Cuervo"),v("Reserva de la Familia Platino","Jose Cuervo"),v("Reserva de la Familia Reposado","Jose Cuervo"),v("Reserva de la Familia Cristalino","Jose Cuervo")],"platino · reposado · extra añejo · cristalino"),
  X("Jose Cuervo Especial","Cuervo's mainstream mixto tequila, made at La Rojeña, the oldest active distillery in Latin America.","Jose Cuervo","",W+"Jose_Cuervo",
    [v("Especial Gold","Jose Cuervo"),v("Especial Silver","Jose Cuervo"),v("Tradicional (Blanco, Reposado, Añejo, Cristalino)","Jose Cuervo","","100% agave line")],"silver · gold"),
  X("Sauza","Tequila from Cenobio Sauza's La Perseverancia distillery; he was first to export tequila to the United States.","Sauza","1873",W+"Sauza_Tequila",
    [v("Sauza Tres Generaciones","Sauza","","triple-distilled plata, reposado, añejo"),v("Sauza Conmemorativo","Sauza","","100% agave, 18 months in bourbon casks"),v("Sauza Blue Silver / Blue Reposado","Sauza","","100% agave"),v("Sauza Blanco / Extra Gold","Sauza")],"blanco · gold · reposado · añejo"),
  X("Herradura","Amatitán hacienda tequila, all 100% blue agave; introduced its first reposado in 1974.","Herradura","1870",W+"Tequila_Herradura",
    [v("Herradura Reposado","Herradura","1974","eleven months in oak"),v("Herradura Selección Suprema","Herradura","","extra añejo aged 49 months"),v("Herradura Blanco","Herradura"),v("Herradura Añejo","Herradura"),v("Herradura Antiguo","Herradura")],TDT),
  X("El Tesoro","La Alteña distillery's tequila, named for Don Felipe Camarena and made by the Camarena family.","El Tesoro","1990",W+"El_Tesoro_tequila",
    [v("El Tesoro Paradiso","El Tesoro","","extra añejo"),v("El Tesoro Reposado Tequila","El Tesoro"),v("El Tesoro Blanco","El Tesoro"),v("El Tesoro Añejo","El Tesoro"),v("El Tesoro Extra Añejo","El Tesoro"),v("El Tesoro 85 Anniversario","El Tesoro")],TDT),
  X("Fortaleza","Small-batch additive-free tequila from the Sauza family's old distillery in Tequila: brick oven, tahona, copper pot stills.","Fortaleza","2002","https://distilling.com/distillermagazine/guillermo-sauza-of-fortaleza/",
    [v("Fortaleza Blanco","Fortaleza"),v("Fortaleza Reposado","Fortaleza"),v("Fortaleza Añejo","Fortaleza"),v("Fortaleza Still Strength Blanco","Fortaleza"),v("Fortaleza Winter Blend Reposado","Fortaleza","","annual release")],"blanco · reposado · añejo · still strength",a="Los Abuelos (Mexico)"),
  X("Don Julio","Tequila from Don Julio González's Atotonilco distillery, begun in 1942; now Diageo-owned.","Don Julio","1942",W+"Don_Julio",
    [v("Don Julio 1942","Don Julio","","añejo named for the founding year"),v("Don Julio Real","Don Julio","","extra añejo"),v("Don Julio 70 Añejo Claro","Don Julio","","clear añejo"),v("Don Julio Blanco / Reposado / Añejo","Don Julio")],TDT),
  X("Patrón","Premium 100% agave tequila in individually numbered glass bottles; Bacardi-owned since 2018.","Patrón","1989",W+"Patr%C3%B3n",
    [v("Patrón Silver","Patrón"),v("Patrón Reposado","Patrón"),v("Patrón Añejo","Patrón"),v("Gran Patrón Platinum","Patrón"),v("Gran Patrón Burdeos","Patrón"),v("Gran Patrón Piedra","Patrón"),v("Roca Patrón (Silver, Reposado, Añejo)","Patrón")],"silver · reposado · añejo · numbered bottle"),
  X("1800","Beckmann-family sipping tequila in a trapezoidal bottle; named for the year tequila was first aged in oak.","1800 Tequila","1967",W+"1800_Tequila",
    [v("1800 Silver","1800 Tequila"),v("1800 Reposado","1800 Tequila"),v("1800 Añejo","1800 Tequila"),v("1800 Cristalino","1800 Tequila"),v("1800 Milenio","1800 Tequila")],"silver · reposado · añejo · cristalino"),
  X("Hornitos","Sauza's 100% agave line, made at La Perseverancia.","Hornitos","",W+"Sauza_Tequila",
    [v("Hornitos Plata","Hornitos"),v("Hornitos Reposado","Hornitos"),v("Hornitos Añejo","Hornitos"),v("Hornitos Black Barrel","Hornitos")],"plata · reposado · añejo"),
  X("Casamigos","Celebrity-founded tequila (Clooney, Gerber, Meldman), bought by Diageo in 2017.","Casamigos","2013",W+"Casamigos",[],"blanco · reposado · añejo"),
 ],
 "r":[["Espolòn tequila range","Espolòn"]]}
# fix Patrón URL to logged form
tequila["x"][7]["s"]=W+"Patrón"
mezcal={"n":"Mezcal","a":"Mescal","d":"Agave spirit, usually from pit-roasted agave, protected by a Mexican designation of origin centred on Oaxaca.",
 "t":["Mezcal (industrial equipment allowed)","Mezcal artesanal (artisanal stills)","Mezcal ancestral (pit oven, hand milling, clay or wood stills)","Blanco / joven","Madurado en vidrio (rested in glass)","Reposado (2–12 months in wood)","Añejo (over a year in wood)","Abocado (flavoured or infused)","Destilado con (redistilled with other ingredients)","Ensamble (blend of agaves)"],
 "s":"https://www.masterofmalt.com/mezcal/",
 "x":[
  X("Espadín mezcal","Mezcal from cultivated Agave angustifolia, the most-used agave and predominant in Oaxaca.","","",MZ,[],"category · ABV · producer · village"),
  X("Tobalá mezcal","Mezcal from wild Agave potatorum, the most famous wild agave.","","",MZ,[],"category · producer · village"),
  X("Wild-agave mezcal","Mezcal from other named agaves: arroqueño, cirial, barril, mexicano, cincoañero, madrecuixe, tepeztate, jabalí, bicuixe.","","",MZ,[],"agave species · producer · village",a="Silvestre"),
  X("Mezcal de pechuga","Mezcal redistilled with fruit and spices and a chicken breast hung in the still.","","",MZ,[],"producer · fruit and spice recipe"),
  X("Del Maguey Single Village","Single-village mezcals named after the Oaxacan village of each palenquero; Chichicapa was the first release.","Del Maguey","1995","https://www.diffordsguide.com/producer/1267/del-maguey-single-village-mezcals/San-Baltazar-Chichicapam",
    [v("Chichicapa","Del Maguey","","San Baltazar Chichicapam; first release")],"village · agave · producer"),
  X("Mezcal Vago","Oaxacan mezcals credited to named mezcaleros, launched with Aquilino García López; first exported in 2013.","Mezcal Vago","2013","https://mezcalreviews.com/mezcal/vago-elote",
    [v("Vago Elote","Mezcal Vago","","espadín redistilled with toasted corn; Aquilino García López; 50%"),v("Vago Espadín","Mezcal Vago"),v("Vago Tepeztate","Mezcal Vago","","Joel Barriga"),v("Vago Madre Cuixe","Mezcal Vago"),v("Vago Pechuga","Mezcal Vago"),v("Vago Ensamble En Barro Joven Ancestral Mezcal","Mezcal Vago")],"mezcalero · agave · ABV"),
  X("Ilegal","Mezcal created for John Rexer's Café No Sé in Antigua, Guatemala, made in Santiago Matatlán, Oaxaca; Bacardi-owned since 2023.","Ilegal Mezcal","2006",W+"Ilegal_Mezcal",
    [v("Ilegal Joven","Ilegal Mezcal"),v("Ilegal Reposado","Ilegal Mezcal","","about six months in American oak"),v("Ilegal Añejo","Ilegal Mezcal","","13 months in oak"),v("Ilegal 7-year Añejo","Ilegal Mezcal","2022","limited, French oak")],"joven · reposado · añejo"),
 ],
 "m":[["Enmascarado 45","Enmascarado"],["Enmascarado 54","Enmascarado"],["Sepulto Ensamble Artesanal Mezcal","La Huaracha Vinata"],["Pensador Ensamble Joven Artesanal Mezcal","Meanwhile Drinks"],["Mezcal Reina Ancestral Ensamble Joven Mezcal","Mezcal Reina"]]}
sotol={"n":"Sotol","a":"Desert spoon spirit","d":"Spirit distilled from Dasylirion (desert spoon), made like an agave spirit; DO covers Chihuahua, Coahuila and Durango.",
 "t":["Mexican sotol (DO, 2002)","Texas sotol","Palmilla (Sonora)","Cucharillo (Oaxaca)"],
 "s":"https://www.masterofmalt.com/other-spirits/","m":[["Clande Sotol","Clande"]]}
raicilla={"n":"Raicilla","a":"","d":"Agave spirit from south-western Jalisco and Bahía de Banderas, Nayarit, protected by a designation of origin.",
 "t":["Agave angustifolia (chico aguiar)","Agave maximiliana","Agave inaequidens","Agave rhodacantha"],"s":W+"Raicilla"}
bacanora={"n":"Bacanora","a":"","d":"Agave spirit from Sonora, legal to distil only since 1992; designation of origin from 2000.","s":W+"Bacanora"}
B=[
 {"n":"Jose Cuervo","c":"Mexico","f":"1795","seg":"Tequila house","d":"Beckmann-family tequila house at La Rojeña, Tequila, Jalisco; first commercial tequila licence.","lines":["Especial","Tradicional","Reserva de la Familia"],"sig":["Jose Cuervo Reserva de la Familia","Jose Cuervo Especial"],"rel":["1800 Tequila"],"s":W+"Jose_Cuervo"},
 {"n":"1800 Tequila","c":"Mexico","f":"1967","seg":"Premium tequila","d":"Beckmann-family sipping tequila brand in a trapezoidal bottle.","sig":["1800"],"rel":["Jose Cuervo"],"s":W+"1800_Tequila"},
 {"n":"Sauza","c":"Mexico","f":"1873","seg":"Tequila house","d":"Cenobio Sauza's La Perseverancia distillery in Tequila; owned by Suntory Global Spirits.","lines":["Sauza","Conmemorativo","Hornitos","Tres Generaciones"],"sig":["Sauza"],"rel":["Hornitos","Fortaleza"],"s":W+"Sauza_Tequila"},
 {"n":"Hornitos","c":"Mexico","seg":"Tequila","d":"100% agave tequila line from Sauza's La Perseverancia distillery.","sig":["Hornitos"],"rel":["Sauza"],"s":W+"Sauza_Tequila"},
 {"n":"Herradura","c":"Mexico","f":"1870","seg":"Tequila house","d":"Hacienda San José del Refugio in Amatitán, Jalisco; Brown-Forman-owned since 2007; also makes El Jimador.","sig":["Herradura"],"s":W+"Tequila_Herradura"},
 {"n":"El Tesoro","c":"Mexico","f":"1990","seg":"Premium tequila","d":"Camarena family tequila from La Alteña (founded 1937), marketed by Suntory Global Spirits.","sig":["El Tesoro"],"s":W+"El_Tesoro_tequila"},
 {"n":"Fortaleza","c":"Mexico","f":"2002","seg":"Craft tequila","d":"Guillermo Sauza's tahona-made tequila from the family's old distillery in Tequila; launched as Los Abuelos.","sig":["Fortaleza"],"rel":["Sauza"],"s":"https://distilling.com/distillermagazine/guillermo-sauza-of-fortaleza/"},
 {"n":"Don Julio","c":"Mexico","f":"1942","seg":"Premium tequila","d":"Don Julio González's tequila from Atotonilco, Jalisco; fully owned by Diageo since 2014.","sig":["Don Julio"],"s":W+"Don_Julio"},
 {"n":"Patrón","c":"Mexico","f":"1989","seg":"Premium tequila","d":"Jalisco tequila founded by John Paul DeJoria and Martin Crowley; bought by Bacardi in 2018.","lines":["Patrón","Gran Patrón","Roca Patrón","XO Cafe"],"sig":["Patrón"],"s":W+"Patrón"},
 {"n":"Casamigos","c":"United States","f":"2013","seg":"Celebrity tequila","d":"Tequila founded by George Clooney, Rande Gerber and Mike Meldman; bought by Diageo in 2017.","sig":["Casamigos"],"s":W+"Casamigos"},
 {"n":"Espolòn","c":"Mexico","seg":"Tequila","d":"Tequila brand owned by Campari.","s":"knowledge"},
 {"n":"Del Maguey","c":"Mexico","f":"1995","seg":"Single-village mezcal","d":"Ron Cooper's single-village mezcal brand working with Oaxacan palenqueros.","sig":["Del Maguey Single Village"],"s":"https://www.diffordsguide.com/producer/1267/del-maguey-single-village-mezcals/San-Baltazar-Chichicapam"},
 {"n":"Mezcal Vago","c":"Mexico","f":"2013","seg":"Craft mezcal","d":"Oaxacan mezcal brand founded by Judah Kuper, Aquilino García and Dylan Sloan; listed as Heaven Hill-owned.","sig":["Mezcal Vago"],"s":"https://mezcalreviews.com/mezcal/vago-elote"},
 {"n":"Ilegal Mezcal","c":"Mexico","f":"2006","seg":"Mezcal","d":"John Rexer's mezcal, made at Mal de Amor, Santiago Matatlán, Oaxaca; Bacardi-owned since 2023.","sig":["Ilegal"],"s":W+"Ilegal_Mezcal"},
]
T=[
 {"n":"Tequila (Agave Landscape of Jalisco)","g":"Food & drink","r":"Valles region, Jalisco, Mexico (Tequila, Amatitán, El Arenal, Magdalena)","p":"16th century to present","d":"Blue-agave cultivation and tequila distilling, recognised as a UNESCO World Heritage cultural landscape in 2006.","tech":"Cooking, fermenting and distilling blue agave hearts","mat":"Blue agave (Agave tequilana Weber)","forms":["Tequila"],"ctr":["Tequila","Amatitán","El Arenal","Magdalena"],"auth":"NOM distillery number and Tequila Regulatory Council certification; '100% agave' on the label","s":W+"Agave_Landscape_and_Ancient_Industrial_Facilities_of_Tequila"},
 {"n":"Mezcal (ancestral and artisanal)","g":"Food & drink","r":"Oaxaca and other DO states, Mexico","p":"Traditional; designation of origin since 1994","d":"Village palenque mezcal making from cultivated and wild agaves.","tech":"Pit-roasting agave, milling by mallet or stone tahona, fermenting, distilling in copper, clay or wood stills","mat":"Agave (espadín, tobalá and other wild species)","forms":["Mezcal","Mezcal de pechuga"],"ctr":["Oaxaca","Santiago Matatlán","San Baltazar Chichicapam"],"auth":"Certified category on label (mezcal, artesanal, ancestral), agave species and producer named","s":MZ},
]
notes=("Kept all planned kinds (Tequila, Mezcal, Sotol, Raicilla, Bacanora). Grades and categories as t types. Old tequila ranges turned into archetypes (Cuervo, Sauza, Herradura, El Tesoro, Don Julio, Patrón, 1800, Hornitos, Casamigos) plus Fortaleza; Espolòn kept as a range (no page retrieved). "
 "Old mezcal models: Vago and Ilegal moved into archetype versions; duplicate 'Meanwhile Drinks Pensador' merged with 'Pensador'. Casamigos has no versions (Wikipedia names none). Del Maguey village list beyond Chichicapa not confirmed, so left out. "
 "No named brands added for raicilla or bacanora (pages name none in body). Raicilla types are the four agaves named on its Wikipedia page.")
out={"kinds":[tequila,mezcal,sotol,raicilla,bacanora],"brands":B,"traditions":T,"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/06_02.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
