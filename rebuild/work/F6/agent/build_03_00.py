import json,os
W='https://en.wikipedia.org/wiki/'
def x(n,d,s,y='',v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":"","y":y,"s":W+s,"v":v or [],"dt":dt}
def v(n,d,y=''): return {"n":n,"mk":"","y":y,"d":d}
DT="slice · etched slice · endcut · individual · crust · TKW (total known weight) · weight"
old='https://www.fossilera.com/meteorites-for-sale'
kinds=[
{"n":"Iron meteorite","a":"siderite","d":"Meteorite made mainly of iron-nickel metal; polished and etched slices show Widmanstätten patterns.","t":["octahedrite","hexahedrite","ataxite"],"s":old,
 "x":[
 x("Gibeon","Namibian fine octahedrite (IVA) with a classic Widmanstätten pattern; the standard etched-slice iron.","Gibeon_(meteorite)","found 1838",[v("Strewn field, Hardap Region, Namibia","total known weight about 26,000 kg")],DT),
 x("Campo del Cielo","Argentine IAB octahedrite shower, the most plentiful iron on the market.","Campo_del_Cielo","first reported 1576",[v("Gancedo","30.8 tonne mass found 2016"),v("El Chaco","28.8 tonne mass found 1969")],DT),
 x("Sikhote-Alin","Russian IIAB iron from a witnessed 1947 fall, sold as shrapnel-shaped individuals and regmaglypted pieces.","Sikhote-Alin_meteorite","fell 12 Feb 1947",[v("Primorye fall","more than 23 tonnes recovered","1947")],"individual · shrapnel · regmaglypted · cut and etched · "+DT),
 x("Canyon Diablo","Coarse octahedrite (IAB-MG) from the Arizona impact that made Meteor Crater.","Canyon_Diablo_(meteorite)","found 1891",[v("Meteor Crater fragments","total known weight about 30 tonnes")],DT),
 x("Muonionalusta","Swedish fine octahedrite (IVA) with a distinctive Widmanstätten pattern, favoured for jewellery and watch dials.","Muonionalusta","found 1906",[v("Kitkiöjärvi, Pajala, Sweden","fell about one million years ago")],DT),
 x("Nantan","Chinese IAB-MG iron, heavily weathered, sold cheaply by the gram.","Nantan_meteorite","fall possibly 1516; fragments recovered 1958",[v("Nandan County, Guangxi","strewn field 28 × 8 km; largest piece about 2,000 kg")],DT),
 x("Dronino","Russian ataxite found near Ryazan in 2000; a common, inexpensive iron.","Dronino_meteorite","found 2000",[v("Ryazan Oblast, Russia","about 3,000 kg in over 600 fragments")],DT)],
 "m":[["Dronino",""],["Gibeon",""],["Nantan",""],["Canyon Diablo",""]]},
{"n":"Pallasite","a":"stony-iron with olivine","d":"Stony-iron meteorite of olivine crystals in iron-nickel metal; gem-quality olivine slices are prized.","s":old,
 "x":[
 x("Imilac","Atacama Desert main-group pallasite with large peridot crystals.","Imilac","found 1822",[v("Atacama Desert, Chile","total known weight 920 kg")],DT),
 x("Brenham","Kansas pallasite, one of the largest known; known for gem peridot slices.","Brenham_(meteorite)","found 1882 (infobox)",[v("Haviland, Kiowa County, Kansas","4.3 tons known"),v("650 kg oriented mass","recovered October 2005","2005")],DT),
 x("Fukang","Chinese pallasite with gem-quality olivine, the best-known 21st-century find.","Fukang_(meteorite)","found 2000",[v("Xinjiang, China","main mass 1,003 kg")],DT),
 x("Seymchan","Russian pallasite from Magadan, also sold as the iron-only variety.","Seymchan_(meteorite)","found 1967",[v("Hekandue riverbed, Magadan Oblast","main mass about 272 kg")],DT),
 x("Esquel","Argentine pallasite from Patagonia with large olivine crystals.","Esquel_(meteorite)","found 1951",[v("Chubut Province, Argentina","755 kg in the infobox")],DT)],
 "m":[["Admire",""],["Borzya",""],["Gyarub Zangbo",""],["Imilac",""],["Sericho",""]]},
{"n":"Mesosiderite","d":"Stony-iron meteorite of silicate breccia and iron-nickel metal in roughly equal parts.","s":old,
 "x":[
 x("Vaca Muerta","Chilean mesosiderite found in the Atacama Desert; prospectors first took the metal for silver.","Mesosiderite","19th century",[v("Atacama Desert, Chile","fragments total about 3.8 tons")],DT),
 x("Estherville","Iowa mesosiderite from an observed fall.","Mesosiderite","fell 10 May 1879",[v("Estherville, Iowa","about 320 kg recovered","1879")],DT),
 x("Łowicz","Polish mesosiderite from an observed fall.","Mesosiderite","fell 12 March 1935",[v("Łowicz, Poland","about 59 kg in over 50 fragments","1935")],DT)]},
{"n":"Ordinary chondrite","a":"H, L and LL chondrite","d":"The common stony meteorite of chondrules, in H, L and LL groups by iron content.","t":["H chondrite","L chondrite","LL chondrite"],"s":old,
 "x":[
 x("Chelyabinsk","Russian LL5 chondrite from the 2013 airburst; fusion-crusted stones and Lake Chebarkul pieces.","Chelyabinsk_meteorite","fell 15 Feb 2013",[v("Lake Chebarkul fragment","540 kg raised October 2013","2013"),v("Recovered total","about 1,000 kg")],"fusion crust · slice · individual · "+DT),
 x("Pultusk","Polish H5 shower of 1868, sold as small 'Pultusk Peas'.","Pultusk_(meteorite)","fell 30 Jan 1868",[v("Strewn field near Pułtusk","about 8,860 kg; largest piece 9.095 kg","1868")],DT),
 x("L'Aigle","French L6 fall of 1803 whose investigation helped establish meteoritics.","L'Aigle_(meteorite)","fell 26 April 1803",[v("L'Aigle, Normandy","37 kg total; over 3,000 fragments","1803")],DT)],
 "m":[["Bassikounou",""],["Bensour",""],["Gold Basin",""],["Holbrook",""],["Saint-Pierre-le-Viger",""],["Tsarev",""]]},
{"n":"Carbonaceous chondrite","a":"C chondrite","d":"Chondrite rich in carbon compounds and water-bearing minerals.","t":["CI","CM","CV","CO","CK","CR"],"s":old,
 "x":[
 x("Murchison","Australian CM2 fall with amino acids and presolar grains; the best-known carbonaceous chondrite for collectors.","Murchison_meteorite","fell 28 Sep 1969",[v("Murchison, Victoria","over 100 kg known","1969")],DT),
 x("Allende","Mexican CV3 fall, the largest carbonaceous chondrite known; holds calcium–aluminium-rich inclusions.","Allende_meteorite","fell 8 Feb 1969",[v("Pueblito de Allende, Chihuahua","over 2 tonnes recovered","1969")],DT)]},
{"n":"Enstatite chondrite","a":"E chondrite · EH · EL","d":"Rare chondrite rich in enstatite, in EH (high iron) and EL (low iron) groups.","t":["EH","EL"],"s":W+"Enstatite_chondrite",
 "x":[x("Abee","Alberta EH4 impact-melt breccia, the largest recorded enstatite chondrite fall.","Abee_(meteorite)","fell 9 June 1952",[v("Thorhild County, Alberta","107 kg main stone","1952")],DT)]},
{"n":"HED meteorite","a":"howardite · eucrite · diogenite","d":"Achondrite of the howardite, eucrite and diogenite group, from asteroid Vesta.","s":old,
 "x":[
 x("Millbillillie","Western Australian eucrite, an observed fall and a common eucrite for collectors.","Millbillillie_(meteorite)","fell Oct 1960",[v("Wiluna district, Western Australia","330 kg","1960")],"fusion crust · slice · "+DT)],
 "m":[]},
{"n":"Lunar meteorite","d":"Achondrite meteorite ejected from the Moon.","s":old,
 "x":[
 x("Northwest Africa 5000","Largest known lunar meteorite, a Saharan find.","Lunar_meteorite","found 2007",[],"slice · endcut · fragment · weight"),
 x("Allan Hills 81005","First recognised lunar meteorite, from Antarctica.","Lunar_meteorite","found January 1982",[],"institutional sample")],
 "m":[["Ajdabiya 001",""],["Ash Shaqqah 002",""],["Bechar 003",""],["Laayoune 002",""],["NWA 11182",""],["NWA 11303",""],["NWA 14188",""],["Oued el Hamim 001",""]]},
{"n":"Martian meteorite","a":"SNC · shergottite · nakhlite · chassignite","d":"Achondrite meteorite ejected from Mars.","t":["shergottite","nakhlite","chassignite","orthopyroxenite"],"s":old,
 "x":[
 x("Tissint","Moroccan olivine-phyric shergottite from an observed 2011 fall.","Tissint_meteorite","fell 18 July 2011",[v("Tata Province, Morocco","about 12–15 kg total","2011")],"fusion crust · slice · fragment · "+DT),
 x("Zagami","Nigerian shergottite from an observed 1962 fall.","Zagami_meteorite","fell 3 Oct 1962",[v("Katsina State, Nigeria","about 18 kg","1962")],DT),
 x("Northwest Africa 7034","Polymict Martian breccia nicknamed 'Black Beauty'.","Northwest_Africa_7034","found 2011",[v("Western Sahara find","about 320 g")],"slice · fragment · weight")],
 "m":[["NWA 12241",""],["NWA 17880",""]]},
{"n":"Asteroidal achondrite","a":"Other achondrite · aubrite · ureilite · angrite · brachinite","d":"Stony meteorite without chondrules that is not lunar, Martian or HED: aubrites, angrites, ureilites and primitive achondrites.","t":["aubrite","ureilite","angrite","brachinite"],"s":W+"Aubrite",
 "x":[
 x("Norton County","Kansas aubrite fall of 1948, a fragmental enstatite breccia.","Norton_County_(meteorite)","fell 18 Feb 1948",[v("Norton County, Kansas","about 1,100 kg","1948")],DT),
 x("Novo Urei","Russian ureilite that names the group.","Ureilite","fell 1886",[],DT),
 x("Angra dos Reis","Brazilian angrite, type specimen of the group.","Angrite","observed fall 1869",[v("Largest surviving piece","101 g, held in Rio de Janeiro")],DT),
 x("Brachina","South Australian meteorite that names the brachinites.","Brachinite","",[],DT)]},
]
brands=[
{"n":"Meteoritical Society","c":"International","f":"1933","seg":"Institution & issuer","kf":"classification","d":"Learned society whose Nomenclature Committee approves meteorite names and classifications in the Meteoritical Bulletin Database.","s":"knowledge"},
{"n":"International Meteorite Collectors Association","c":"International","f":"","seg":"Institution & issuer","kf":"dealer ethics","d":"Association of meteorite collectors and dealers with a code of ethics and a dealer-verification scheme.","s":"knowledge"}]
os.makedirs('work/F6/shelves',exist_ok=True)
json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":"Planned kind Other achondrite renamed Asteroidal achondrite (checker bars Other names). Old models kept as flat m where no page was retrieved (Admire, Sericho, Holbrook, etc.). Aguas Zarcas, Tatahouine, Campo/Meteoritical Bulletin database records not retrieved so left out. Vaca Muerta, Estherville and Lowicz are sourced from the Mesosiderite article. Dealer register limited to two knowledge-based entries."},open('work/F6/shelves/03_00.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/F6/shelves/03_00.tmp','work/F6/shelves/03_00.json')
