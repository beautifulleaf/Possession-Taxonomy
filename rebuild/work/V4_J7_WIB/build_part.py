import json,os
SP="https://en.wikipedia.org/wiki/Spanish_wine_regions"
PTL="https://winesofportugal.com/en/discover/wine-regions/"
PT09="https://en.wikipedia.org/wiki/List_of_Portuguese_wine_regions"
IGU="https://www.vinetowinecircle.com/en/regions"
RIOJA="https://en.wikipedia.org/wiki/Rioja_(wine)"
SHERRY="https://en.wikipedia.org/wiki/Sherry"
CAVA="https://en.wikipedia.org/wiki/Cava_(Spanish_wine)"
PORT="https://en.wikipedia.org/wiki/Port_wine"
MAD="https://en.wikipedia.org/wiki/Madeira_wine"
PRI="https://en.wikipedia.org/wiki/Priorat_(DOQ)"
QC="https://en.wikipedia.org/wiki/Quinta_classification"
PTW="https://en.wikipedia.org/wiki/Portuguese_wine"
DOCP="https://www.winewithseth.com/winewiki/doc-dop-portugal/"

def E(n,d,s,**kw):
    e={"n":n,"d":d,"s":s}; e.update(kw); e.setdefault("v",[]); return e
def V(n,d,y=""):
    return {"n":n,"y":y,"d":d}
def do(n,reg,**kw): return E(n,f"Spanish denominación de origen in {reg}.",SP,**kw)
def vp(n,reg,**kw): return E(n,f"Vino de Pago, a single-estate designation, in {reg}.",SP,**kw)
def vc(n,reg,**kw): return E(n,f"Vino de Calidad con indicación geográfica in {reg}.",SP,**kw)
def vt(n,reg,**kw): return E(n,f"Vino de la Tierra, a Spanish protected geographical indication for wine, in {reg}.",SP,**kw)
def dop(n,reg,**kw): return E(n,f"Portuguese denominação de origem protegida in the {reg} wine region.",PTL,**kw)

STY=["Red","White","Rosé","Sparkling","Sweet","Fortified"]
def tt(extra=None,sty=None):
    t=[["Colour and style",sty or ["Red","White","Rosé"]]]
    if extra: t+=extra
    return t
def kind(n,d,nl,sel,entries,t,xg=None):
    k={"n":n,"d":d,"nl":nl,"sel":sel,"x":entries,"tt":t}
    if xg: k["xg"]=xg
    return k
NLDO="One entry is a Spanish wine appellation (a denominación de origen or its higher tier); styles and ageing grades are versions."
NLVP="One entry is a single-estate Vino de Pago or a Vino de Calidad appellation."
NLVT="One entry is a Vino de la Tierra, the Spanish protected geographical indication for wine (IGP)."
SELSP="Every entry of this tier that Wikipedia's Spanish wine regions page lists for this community (page counts as of 2019: 2 DOCa, 68 DO, 7 VC, 19 VP, 42 VT); later additions to the register are not included."
def spk(name,d,entries,t,nl=NLDO,xg=None,extra=""):
    return kind(name,d,nl,SELSP+extra,entries,t,xg)

shelves=[]
# ---------- SPAIN
rioja=E("Rioja","Spain's first DOCa, covering La Rioja, Álava and Navarre in three subzones; red, white and rosé graded by ageing.",RIOJA,
  y="1991",g="DOCa",role="origin",
  dt="subzone (Rioja Alta, Rioja Alavesa, Rioja Oriental) · ageing grade · single vineyard (Viñedo Singular, added 2017)",
  v=[V("Crianza","red: 2 years in total with at least 1 year in oak; white and rosé: 2 years with at least 6 months in oak"),
     V("Reserva","red: 36 months with at least 12 months in oak; white and rosé: 24 months with at least 6 months in oak"),
     V("Gran Reserva","red: at least 24 months in oak and 36 months in bottle; white and rosé: 48 months with at least 6 months in oak")])
shelves.append({"n":"Rioja, Navarre & Basque Country","t":"Appellations of the upper Ebro and the Basque coast: Rioja, Navarre, the three Txacolí denominations, three Vinos de Pago and the regional wines of Navarre and La Rioja; Cava → Catalonia.","ax":"kinds by appellation tier: denominations of origin, single-estate and quality wines, regional wines","k":[
 spk("Rioja, Navarre & Basque Country: denominations of origin","Denominations of Rioja, Navarre and the Basque coast, led by the Rioja DOCa.",
  [rioja,do("Navarra","the Foral Community of Navarre",g="DO"),do("Txacolí de Álava","the Basque Country",g="DO"),do("Txacolí de Bizcaia","the Basque Country",g="DO"),do("Txacolí de Getaria","the Basque Country",g="DO")],
  tt([["Permitted grapes (Rioja)",["Tempranillo","Garnacha tinta","Mazuelo (Cariñena)","Graciano","Maturana tinta","Viura","Malvasía","Garnacha blanca","Maturana blanca","Tempranillo blanco","Turruntés"]],["Ageing grade (Rioja)",["Crianza","Reserva","Gran Reserva"]]]),xg="by appellation tier, DOCa first"),
 spk("Navarre: single-estate wines","Single-estate Vinos de Pago of Navarre.",[vp("Pago de Arínzano","Navarre"),vp("Otazu","Navarre"),vp("Prado de Irache","Navarre")],tt(),NLVP),
 spk("Navarre & La Rioja: regional wines","Vinos de la Tierra of Navarre and La Rioja.",[vt("3 Riberas","Navarre"),vt("Ribera del Queiles","Navarre and Aragon (multi-regional)"),vt("Valles de Sadacia","La Rioja")],tt(),NLVT)]})

priorat=E("Priorat","Catalan DOQ, the second Spanish denomination at the top tier; DO since 1954, with red from Garnatxa negre and Cariñena on hillside villages.",PRI,y="1954",g="DOCa",
  dt="village (Gratallops, Porrera, Poboleda, Scala Dei…) · ageing grade",
  v=[V("Crianza","6 months in oak, then 18 months in bottle"),V("Reserva","12 months in oak, then 24 months in bottle"),V("Gran Reserva","24 months in oak, then 36 months in bottle")])
cava=E("Cava","Sparkling DO made by the traditional method, with about 95% from Penedès and permitted areas in several communities; white or rosé.",CAVA,
  dt="sweetness level · white or rosé · producing area",
  v=[V("Brut nature","driest level"),V("Brut",""),V("Brut reserve",""),V("Seco",""),V("Semiseco",""),V("Dulce","sweetest level"),V("Rosé cava","by saignée from Garnacha, Pinot Noir, Trepat or Monastrell; blending is not allowed")])
shelves.append({"n":"Catalonia","t":"The Catalan appellations, from Penedès and Cava to Priorat; Catalonia has no Vino de la Tierra listed.","ax":"kinds by appellation tier","k":[
 spk("Catalonia: denominations of origin","Eleven Catalan denominations, with the Priorat DOQ and the multi-region Cava.",
  [priorat,do("Alella","Catalonia",g="DO"),cava.copy() if False else cava,do("Catalunya","Catalonia",g="DO"),do("Conca de Barberà","Catalonia",g="DO"),do("Costers del Segre","Catalonia",g="DO"),do("Empordà","Catalonia",g="DO"),do("Montsant","Catalonia",g="DO"),do("Penedès","Catalonia",g="DO"),do("Pla de Bages","Catalonia",g="DO"),do("Tarragona","Catalonia",g="DO"),do("Terra Alta","Catalonia",g="DO")],
  tt([["Permitted grapes (Cava and Priorat)",["Macabeo","Parellada","Xarel·lo","Garnatxa negre","Cariñena (Samsó)"]]],sty=["Red","White","Rosé","Sparkling"]),xg="by appellation tier, DOCa first",
  extra=" Cava is shown here although it spans six communities; the page lists it under each.")]})

sherry=E("Jerez-Xérès-Sherry","Fortified DO of the Sherry Triangle (Jerez de la Frontera, Sanlúcar de Barrameda, El Puerto de Santa María), mostly from Palomino; the first Spanish denominación.",SHERRY,y="1933",role="origin",
  dt="style · sweetness · age statement (VOS, VORS) · solera",
  v=[V("Fino","driest and palest style, aged under flor"),V("Amontillado","aged first under flor, then oxidatively"),V("Palo Cortado","starts as amontillado and ages like an oloroso"),V("Oloroso","oxidative ageing; 17–22 % alcohol"),V("Cream","sweetened oloroso-style blend, first made in the 1860s"),V("Pale Cream","45–115 g/L sugar"),V("Pedro Ximénez","sun-dried grapes, 212 g/L sugar or more"),V("Moscatel","sun-dried grapes, 160 g/L sugar or more"),V("VOS","Vinum Optimum Signatum: average age of at least 20 years"),V("VORS","Vinum Optimum Rare Signatum: average age of at least 30 years")])
manz=E("Manzanilla-Sanlúcar de Barrameda","Separate DO for the light fino-style Manzanilla matured at Sanlúcar de Barrameda.",SHERRY,
  v=[V("Manzanilla","particularly light fino made around Sanlúcar"),V("Manzanilla Pasada","extended ageing or partial oxidation, richer and nuttier")])
shelves.append({"n":"Andalusia","t":"Sherry, Montilla-Moriles and the other southern appellations, with the regional wines of the south.","ax":"kinds by appellation tier","k":[
 spk("Andalusia: denominations of origin","Seven Andalusian denominations, led by the sherry country.",
  [sherry,manz,do("Condado de Huelva","Andalusia"),do("Granada","Andalusia"),do("Málaga","Andalusia"),do("Montilla-Moriles","Andalusia"),do("Sierras de Málaga","Andalusia")],
  tt([["Permitted grapes (Jerez)",["Palomino","Pedro Ximénez","Moscatel"]]],sty=["Red","White","Rosé","Sweet","Fortified"])),
 spk("Andalusia: quality wine","Vino de Calidad of Andalusia.",[vc("Lebrija","Andalusia")],tt(),NLVP),
 spk("Andalusia: regional wines","Sixteen Vinos de la Tierra of Andalusia.",[vt(n,"Andalusia") for n in ["Altiplano de Sierra Nevada","Bailén","Cádiz","Córdoba","Cumbres del Guadalfeo","Desierto de Almería","Laderas del Genil","Laujar-Alpujarra","Los Palacios","Norte de Almería","Ribera del Andarax","Sierra Norte de Sevilla","Sierra Sur de Jaén","Sierras de Las Estancias y Los Filabres","Torreperogil","Villaviciosa de Córdoba"]],tt(),NLVT)]})

shelves.append({"n":"Galicia","t":"The Atlantic north-west: five denominations and four regional wines.","ax":"kinds by appellation tier","k":[
 spk("Galicia: denominations of origin","Five Galician denominations.",[do(n,"Galicia") for n in ["Monterrei","Rías Baixas","Ribeira Sacra","Ribeiro","Valdeorras"]],tt()),
 spk("Galicia: regional wines","Four Vinos de la Tierra of Galicia.",[vt(n,"Galicia") for n in ["Barbanza e Iria","Betanzos","Ribeiras do Morrazo","Valle del Miño-Ourense"]],tt(),NLVT)]})

shelves.append({"n":"Castile and León","t":"The Duero basin and the north-west plateau: nine denominations, three quality-wine appellations and one regional wine.","ax":"kinds by appellation tier","k":[
 spk("Castile and León: denominations of origin","Nine denominations of the Duero basin and its neighbours.",[do(n,"Castile and León") for n in ["Arlanza","Arribes","Bierzo","Cigales","Ribera del Duero","Rueda","Tierra de León","Tierra del Vino de Zamora","Toro"]],tt()),
 spk("Castile and León: quality wine","Vinos de Calidad of Castile and León.",[vc(n,"Castile and León") for n in ["Sierra de Salamanca","Valles de Benavente","Valtiendas"]],tt(),NLVP),
 spk("Castile and León: regional wines","The Vino de la Tierra covering Castile and León.",[vt("Castilla y León","Castile and León")],tt(),NLVT)]})

shelves.append({"n":"Aragon","t":"Four Aragonese denominations, one Vino de Pago and six regional wines.","ax":"kinds by appellation tier","k":[
 spk("Aragon: denominations of origin","Four Aragonese denominations.",[do(n,"Aragon") for n in ["Calatayud","Campo de Borja","Cariñena","Somontano"]],tt()),
 spk("Aragon: single-estate wines","Vino de Pago of Aragon.",[vp("Pago Aylés","Aragon")],tt(),NLVP),
 spk("Aragon: regional wines","Six Vinos de la Tierra of Aragon.",[vt(n,"Aragon") for n in ["Bajo Aragón","Ribera del Gállego-Cinco Villas","Ribera del Jiloca","Valdejalón","Valle del Cinca"]]+[vt("Ribera del Queiles","Aragon and Navarre (multi-regional)")][:0],tt(),NLVT)]})

clm_do=[do(n,"Castilla-La Mancha") for n in ["Almansa","La Mancha","Manchuela","Méntrida","Mondéjar","Ribera del Júcar","Uclés","Valdepeñas"]]
clm_do.append(E("Campo de Calatrava","Castilla-La Mancha appellation named in a footnote of the page, which does not state its tier.",SP))
clm_vp=[vp(n,"Castilla-La Mancha") for n in ["Campo de La Guardia","Casa del Blanco","Dehesa del Carrizal","Dominio de Valdepusa","El Vicario","Finca Élez","Guijoso","La Jaraba","Los Cerrillos","Pago Calzadilla","Pago Florentino","Vallegarcía"]]
shelves.append({"n":"Castilla-La Mancha","t":"The central plateau: nine denominations, twelve Vinos de Pago and one regional wine; Jumilla → Valencia & Murcia.","ax":"kinds by appellation tier","k":[
 spk("Castilla-La Mancha: denominations of origin","Denominations of the central plateau.",clm_do,tt()),
 spk("Castilla-La Mancha: single-estate wines","Twelve Vinos de Pago, the largest group in any community.",clm_vp,tt(),NLVP),
 spk("Castilla-La Mancha: regional wines","The Vino de la Tierra covering Castilla-La Mancha.",[vt("Castilla","Castilla-La Mancha")],tt(),NLVT)]})

shelves.append({"n":"Valencia & Murcia","t":"The Mediterranean south-east: Valencian and Murcian denominations, Vinos de Pago and regional wines.","ax":"kinds by appellation tier","k":[
 spk("Valencia & Murcia: denominations of origin","Six denominations of the south-east, including Jumilla, which spans Murcia and Castilla-La Mancha.",[do("Alicante","the Valencian Community"),do("Utiel-Requena","the Valencian Community"),do("Valencia","the Valencian Community"),do("Bullas","Murcia"),do("Jumilla","Murcia and Castilla-La Mancha (multi-regional)"),do("Yecla","Murcia")],tt()),
 spk("Valencia: single-estate wines","Vinos de Pago of the Valencian Community.",[vp(n,"the Valencian Community") for n in ["El Terrerazo","Los Balagueses","Vera de Estenas"]],tt(),NLVP),
 spk("Valencia & Murcia: regional wines","Vinos de la Tierra of Valencia and Murcia.",[vt("Castelló","the Valencian Community"),vt("Abanilla","Murcia"),vt("Campo de Cartagena","Murcia"),vt("Murcia","Murcia")],tt(),NLVT)]})

shelves.append({"n":"Madrid & Extremadura","t":"Central and south-western Spain: Vinos de Madrid and Ribera del Guadiana.","ax":"kinds by appellation tier","k":[
 spk("Madrid & Extremadura: denominations of origin","The two denominations of the region.",[do("Vinos de Madrid","the Community of Madrid"),do("Ribera del Guadiana","Extremadura")],tt()),
 spk("Extremadura: regional wines","The Vino de la Tierra of Extremadura.",[vt("Extremadura","Extremadura")],tt(),NLVT)]})

shelves.append({"n":"Balearic & Canary Islands","t":"The Spanish island wines: two Balearic and ten Canarian denominations, with island regional wines.","ax":"kinds by archipelago and appellation tier","k":[
 spk("Balearic Islands: denominations of origin","Two Balearic denominations.",[do("Binissalem","the Balearic Islands"),do("Plà i Llevant","the Balearic Islands")],tt()),
 spk("Balearic Islands: regional wines","Six Vinos de la Tierra of the Balearic Islands.",[vt(n,"the Balearic Islands") for n in ["Formentera","Ibiza","Illes Balears","Isla de Menorca","Mallorca","Serra de Tramuntana-Costa Nord"]],tt(),NLVT),
 spk("Canary Islands: denominations of origin","Ten Canarian denominations.",[do(n,"the Canary Islands") for n in ["Abona","El Hierro","Gran Canaria","La Gomera","La Palma","Lanzarote","Tacoronte-Acentejo","Valle de Güímar","Valle de la Orotava","Ycoden-Daute-Isora"]],tt()),
 spk("Canary Islands: quality and regional wines","Vino de Calidad and Vino de la Tierra covering the Canary Islands.",[vc("Islas Canarias","the Canary Islands"),vt("Islas Canarias","the Canary Islands")],tt(),NLVP)]})

shelves.append({"n":"Asturias & Cantabria","t":"The Cantabrian coast: one quality-wine appellation and two regional wines.","ax":"kinds by appellation tier","k":[
 spk("Asturias & Cantabria: quality and regional wines","Cangas in Asturias and the two Cantabrian regional wines.",[vc("Cangas","Asturias"),vt("Costa de Cantabria","Cantabria"),vt("Liébana","Cantabria")],tt(),NLVP)]})

# ---------- PORTUGAL
def ig(n,reg,**kw): return E(n,f"Portuguese indicação geográfica (Vinho Regional) in the {reg} wine region.",IGU,**kw)
NLP="One entry is a Portuguese denominação de origem protegida (DOC/DOP); subregions are detail and special designations or styles are versions."
NLI="One entry is a Portuguese indicação geográfica (Vinho Regional), the wider tier below the DOP."
SELP="The 31 DOPs that Wines of Portugal lists under its 14 wine regions; subregions and special designations from Wikipedia's List of Portuguese wine regions (a 2009 count)."
SELI="The 14 Vinho Regional names, from the region list on Vine to Wine Circle and Wikipedia's List of Portuguese wine regions (2009)."
def ptk(n,d,entries,t,nl=NLP,sel=SELP,xg=None): return kind(n,d,nl,sel,entries,t,xg)
PSTY=["Red","White","Rosé","Sparkling","Fortified"]
vv=dop("Vinho Verde","Vinho Verde",y="1908",dt="subregion (Amarante, Ave, Baião, Basto, Cávado, Lima, Monção e Melgaço, Paiva, Sousa)",
  v=[V("Vinho Verde Alvarinho","special designation"),V("Vinho Verde Alvarinho Espumante","sparkling Alvarinho designation")])
vv["d"]="Portugal's largest DOP, in the Minho; fresh, slightly petillant whites from Alvarinho, Loureiro, Arinto, Avesso, Azal and Trajadura, first demarcated in 1908."
vv["s"]=DOCP
tm=dop("Trás-os-Montes","Trás-os-Montes",dt="subregion (Chaves, Planalto Mirandês, Valpaços)")
shelves.append({"n":"Minho & Trás-os-Montes","t":"The north-west and north-east of Portugal: Vinho Verde and Trás-os-Montes with their regional wines.","ax":"kinds by appellation tier","k":[
 ptk("Minho & Trás-os-Montes: DOP","Two DOPs of northern Portugal.",[vv,tm],tt(sty=PSTY)),
 ptk("Minho & Trás-os-Montes: regional wines","Vinho Regional names of the north.",[ig("Minho","Minho"),ig("Transmontano","Trás-os-Montes")],tt(),NLI,SELI)]})

douro=dop("Douro","Porto and Douro",y="1756",dt="subregion (Baixo Corgo, Cima Corgo, Douro Superior) · still wine, Moscatel do Douro",
  v=[V("Moscatel do Douro","special designation listed on the 2009 Wikipedia page")])
douro["d"]="Still wines of the Douro valley, with a DOC for table wine from 1979; the region was demarcated in 1756."
douro["s"]=DOCP
port=dop("Porto","Porto and Douro",y="1756",
  dt="Douro subregion · style · vintage · shipper · vineyard grade A to F (IVDP rating of Douro vineyards)",
  v=[V("Ruby","young, aged in tank, fined and filtered"),V("Reserve ruby","premium ruby approved by the IVDP tasting panel"),V("Tawny","wood-aged blend, usually three to seven years"),V("Tawny reserve","about seven years in wood"),
     V("Tawny with indication of age","blend with a stated average age of 10, 20, 30, 40 or 50 years"),V("Colheita","single-vintage tawny, at least seven years in wood"),V("White Port","dry to sweet; the lágrima style is the sweetest"),V("Rosé Port","ruby-category style first released in 2008","2008"),
     V("Late Bottled Vintage","four to six years in wood, then bottled"),V("Vintage Port","one declared harvest, about 2.5 years in cask, then decades in bottle; roughly 2 % of production"),V("Single quinta vintage","from one estate, often released in years without a declared vintage"),V("Crusted","unfiltered blend of several vintages, decanted before drinking"),V("Garrafeira","vintage-dated; 3 to 6 years in wood, then at least 8 years in glass demijohns")])
port["d"]="Fortified wine of the Douro, from a region demarcated in 1756; styles run from ruby to vintage and the IVDP rates Douro vineyards A to F."
port["s"]=PORT
shelves.append({"n":"Douro & Port","t":"The Douro valley: the Douro DOP for table wine, the Porto DOP for Port, and the Duriense regional wine.","ax":"kinds by appellation tier","k":[
 ptk("Douro & Port: DOP","The two DOPs of the Douro valley.",[douro,port],tt([["Permitted grapes (Port)",["Tinta Barroca","Tinto Cão","Tinta Roriz","Touriga Francesa","Touriga Nacional","Donzelinho Branco","Esgana-Cão","Folgasão","Gouveio","Malvasia Fina","Rabigato","Viosinho"]]],sty=["Red","White","Rosé","Fortified"])),
 ptk("Douro: regional wines","Vinho Regional of the Douro.",[ig("Duriense","Porto and Douro")],tt(),NLI,SELI)]})

dao=dop("Dão","Dão and Lafões",y="1908",dt="subregion (Alva, Besteiros, Castendo, Serra da Estrela, Silgueiros, Terras de Azurara, Terras de Senhorim)",v=[V("Dão Nobre","special designation listed on the 2009 Wikipedia page")])
dao["d"]="DOP of the Dão highlands, demarcated in 1908."; dao["s"]=PTW
bai=dop("Bairrada","Bairrada",y="1979"); bai["d"]="DOP classified in 1979, known for tannic, high-acid reds from Baga and for sparkling wine."; bai["s"]=PTW
shelves.append({"n":"Beiras & Bairrada","t":"Central Portugal inland and on the Atlantic: Távora-Varosa, Dão, Lafões, Bairrada and Beira Interior with the Beiras regional wines.","ax":"kinds by appellation tier","k":[
 ptk("Beiras & Bairrada: DOP","Five DOPs of central Portugal.",[dop("Távora-Varosa","Távora and Varosa"),dao,dop("Lafões","Dão and Lafões"),bai,dop("Beira Interior","Beira Interior",dt="subregion (Castelo Rodrigo, Cova da Beira, Pinhel)")],tt(sty=PSTY)),
 ptk("Beiras: regional wines","Four Vinho Regional names of the Beiras.",[ig("Terras de Cister","Beiras"),ig("Terras da Beira","Beiras"),ig("Beira Atlântico","Beiras"),ig("Terras do Dão","Beiras")],tt(),NLI,SELI)]})

col=dop("Colares","Lisboa"); col["d"]="Lisboa DOP of sandy coastal soils with ungrafted vines; Ramisco reds and Malvasia de Colares whites."; col["s"]=DOCP
shelves.append({"n":"Lisboa & Tejo","t":"The Lisbon coast and the Tejo valley: nine Lisboa DOPs, the Tejo DOP and the Lisboa and Tejo regional wines.","ax":"kinds by appellation tier","k":[
 ptk("Lisboa & Tejo: DOP","Ten DOPs around Lisbon and along the Tejo.",[dop("Encostas d'Aire","Lisboa",dt="subregion (Alcobaça, Ourém)"),dop("Óbidos","Lisboa"),dop("Alenquer","Lisboa"),dop("Arruda","Lisboa"),dop("Torres Vedras","Lisboa"),dop("Lourinhã","Lisboa"),dop("Bucelas","Lisboa"),dop("Carcavelos","Lisboa"),col,dop("Tejo","Tejo",dt="subregion (Almeirim, Cartaxo, Chamusca, Coruche, Santarém, Tomar)")],tt(sty=PSTY)),
 ptk("Lisboa & Tejo: regional wines","Vinho Regional names of the Lisbon and Tejo regions.",[ig("Lisboa","Lisboa"),ig("Tejo","Tejo")],tt(),NLI,SELI)]})

setu=dop("Setúbal","Península de Setúbal",v=[V("Moscatel de Setúbal","special designation"),V("Setúbal Roxo","special designation")])
shelves.append({"n":"Setúbal & Alentejo","t":"The Setúbal peninsula and the Alentejo: Palmela, Setúbal and Alentejo with their regional wines.","ax":"kinds by appellation tier","k":[
 ptk("Setúbal & Alentejo: DOP","Three DOPs south of the Tagus.",[dop("Palmela","Península de Setúbal"),setu,dop("Alentejo","Alentejo",y="1998",dt="subregion (Borba, Évora, Granja-Amareleja, Moura, Portalegre, Redondo, Reguengos, Vidigueira)")],tt(sty=PSTY)),
 ptk("Setúbal & Alentejo: regional wines","Vinho Regional names of the south.",[ig("Península de Setúbal","Península de Setúbal"),ig("Alentejano","Alentejo")],tt(),NLI,SELI)]})

shelves.append({"n":"Algarve","t":"The southern coast: four DOPs and the Algarve regional wine.","ax":"kinds by appellation tier","k":[
 ptk("Algarve: DOP","Four Algarve DOPs, demarcated together in 1980.",[dop(n,"Algarve",y="1980") for n in ["Lagos","Portimão","Lagoa","Tavira"]],tt(sty=PSTY)),
 ptk("Algarve: regional wines","Vinho Regional of the Algarve.",[ig("Algarve","Algarve")],tt(),NLI,SELI)]})

mad=dop("Madeira","Madeira",
  dt="style by grape · age category · single vintage",
  v=[V("Sercial","driest noble grape style, pale with almond flavours and high acidity"),V("Verdelho","medium-dry, smoky"),V("Bual","dark, medium-rich, raisin flavours"),V("Malmsey","sweetest, from Malvasia; dark and rich"),V("Terrantez","revived rare grape; sweetness between Verdelho and Bual"),V("Rainwater","dry to medium-dry aperitif style, mostly Tinta Negra"),
     V("Finest","at least 3 years"),V("Reserve","at least 5 years"),V("Special Reserve","10 years"),V("Extra Reserve","over 15 years"),V("Colheita","single vintage, at least 5 years in cask"),V("Frasqueira","vintage; at least 19 years in cask and one year in bottle")])
mad["d"]="Fortified wine of the Madeira islands, heated or aged in loft canteiro; the noble grapes are Sercial, Verdelho, Bual, Malvasia and Terrantez."
mad["s"]=MAD
shelves.append({"n":"Madeira & Azores","t":"The Atlantic islands: Madeira and Madeirense on Madeira, three Azorean DOPs and the island regional wines.","ax":"kinds by archipelago and appellation tier","k":[
 ptk("Madeira & Azores: DOP","Five island DOPs.",[mad,dop("Madeirense","Madeira"),dop("Graciosa","Açores"),dop("Biscoitos","Açores"),dop("Pico","Açores")],tt([["Permitted grapes (Madeira)",["Sercial","Verdelho","Bual","Malvasia","Terrantez","Tinta Negra"]]],sty=["Red","White","Fortified"])),
 ptk("Madeira & Azores: regional wines","Vinho Regional of the islands.",[ig("Terras Madeirenses","Madeira"),ig("Açores","Açores")],tt(),NLI,SELI)]})

# sort DOCa first inside kinds is already in list order
dept={"n":"Wine of Spain & Portugal","mode":"variety",
 "t":"Wines of Spain and Portugal named by appellation, with Sherry, Port, Madeira, Cava and Rioja; wine from another country → its own department; a producer outside these appellations is not an entry.",
 "ax":"Where is the wine grown and under which appellation: a country's region, then the tier its law gives the name?",
 "note":"Organised country → region → appellation tier; styles and ageing grades are versions of the appellation.",
 "b":[{"m":"Appellation and tier","v":"Spain: Vino de la Tierra → DO → DOCa; Vino de Pago and Vino de Calidad beside them; Portugal: Vinho Regional → DOP (DOC)","w":"The protected status named on the label."},
      {"m":"Style and ageing","v":"Rioja Crianza → Reserva → Gran Reserva; Sherry fino → oloroso, VOS → VORS; Port ruby → tawny → vintage; Madeira Reserve → Frasqueira","w":"Ageing grades and styles set by each appellation."}],
 "s":shelves}
renames={
 "Tempranillo":"Rioja, Navarre & Basque Country: denominations of origin","Graciano":"Rioja, Navarre & Basque Country: denominations of origin","Txakoli":"Rioja, Navarre & Basque Country: denominations of origin",
 "Monastrell":"Valencia & Murcia: denominations of origin",
 "Mencía":"Castile and León: denominations of origin","Verdejo":"Castile and León: denominations of origin","Albillo Mayor":"Castile and León: denominations of origin",
 "Albariño":"Galicia: denominations of origin","Godello":"Galicia: denominations of origin",
 "Cava":"Catalonia: denominations of origin","Sherry":"Andalusia: denominations of origin",
 "Touriga Nacional":"Douro & Port: DOP","Port":"Douro & Port: DOP",
 "Encruzado":"Beiras & Bairrada: DOP","Arinto":"Lisboa & Tejo: DOP","Loureiro":"Minho & Trás-os-Montes: DOP","Madeira":"Madeira & Azores: DOP"}
out={"depts":[dept],"brands":[],"renames":renames,"moves":[]}
tmp="/home/user/Possession-Taxonomy/rebuild/out/J7_parts/WIB.json.tmp"
json.dump(out,open(tmp,"w"),ensure_ascii=False,indent=1)
os.replace(tmp,"/home/user/Possession-Taxonomy/rebuild/out/J7_parts/WIB.json")
n=sum(len(k["x"]) for s in shelves for k in s["k"]);print("kinds",sum(len(s["k"]) for s in shelves),"entries",n)
