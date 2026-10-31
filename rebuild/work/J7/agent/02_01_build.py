import json, os
W='https://en.wikipedia.org/wiki/'
PRO=W+'Prosecco'; CAVA=W+'Cava_(Spanish_wine)'; BK='https://www.bkwine.com/news/stricter-rules-new-denominations-cava/'
CRE=W+'Crémant'; FRA=W+'Franciacorta_(wine)'; SEKT=W+'Sekt'; ASTI=W+'Asti_(wine)'; LAM=W+'Lambrusco'; PET=W+'Pétillant_naturel'
ENG=W+'English_sparkling_wine'; NYE=W+'Nyetimber'; CD=W+'Chapel_Down'; TAS=W+'Tasmanian_wine'; COD=W+'Codorníu_Winery'
FX=W+'Freixenet'; TRE=W+'Trento_DOC'; HEN=W+'Henkell_%26_Co.'; CDB=W+'Ca%27_del_Bosco'
def A(n,d,s,mk='',y='',a='',v=None,dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or []}
    if dt: x["dt"]=dt
    return x
def V(n,mk='',y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
{"n":"Prosecco","a":"Prosecco Superiore","d":"Italian sparkling wine, mainly from Glera, of the Prosecco DOC and DOCGs in Veneto and Friuli-Venezia Giulia.",
 "t":["Spumante","Frizzante","Tranquillo (still)","Col fondo (undisgorged)","Rosé"],"s":"https://www.vinoscout.de/en/collections/schaumwein",
 "x":[A("Conegliano Valdobbiadene Prosecco Superiore DOCG","Hillside zone between Conegliano and Valdobbiadene; always spumante.",PRO,y="2009",a="Valdobbiadene Prosecco Superiore",
     v=[V("Rive (single-hill subzones)",d="43 named Rive across 15 communes"),V("Bisol1542 Crede Brut Valdobbiadene Prosecco Superiore","Bisol1542"),
        V("Il Colle 1978 Rive di Rua di Feletto Extra Brut","Il Colle 1978"),V("Sui Nui Rive di Rolle Extra Brut","Sui Nui Spumanti"),
        V("Col Fondo",d="bottle-refermented, undisgorged, about 2.5 bar")],dt="sweetness Extra Brut · Brut · Extra Dry · Dry · Rive or village"),
   A("Superiore di Cartizze","107-hectare subzone within Conegliano Valdobbiadene, regarded as the top tier of Prosecco.",PRO,a="Cartizze",dt="about 140 growers · sweetness"),
   A("Asolo Prosecco DOCG","Hillside zone around Asolo; promoted in 2009 as Colli Asolani, renamed Asolo in 2014.",PRO,y="2009",a="Asolo Prosecco Superiore · Colli Asolani",dt="only zone currently allowed Extra Brut"),
   A("Prosecco DOC","Large-area designation across nine provinces of Veneto and Friuli-Venezia Giulia; Prosecco a geographical indication since 2010.",PRO,y="2010",
     v=[V("Prosecco Rosé DOC",y="2020",d="Glera with 10–15% Pinot nero"),V("Cornaro Prosecco Treviso Spumante DOC Brut","Cantina Montelliana"),V("Freixenet Prosecco DOC","Freixenet","2017")],
     dt="spumante · frizzante · Treviso or Trieste labelling · sweetness")],
 "m":[["Nani Rizzi Extra Brut","Nani Rizzi"]]},
{"n":"Cava","a":"","d":"Spanish traditional-method sparkling wine of the Cava designation, about 95% from Penedès in Catalonia.",
 "t":["Brut nature to dulce sweetness","Rosado (saignée)"],"s":"https://www.totalwine.com/wine/spain/cava/c/000623",
 "x":[A("Codorníu cava","The first Spanish cava, made by Josep Raventós at Codorníu in Sant Sadurní d'Anoia.",COD,mk="Codorníu",y="1872",v=[V("Benjamin sec","Codorníu")]),
   A("Cava de Guarda","Standard tier with at least 9 months on lees; about 85% of sales.",BK,dt="Macabeo, Xarel·lo, Parellada · green seal"),
   A("Cava Reserva","Guarda Superior tier with at least 18 months on lees and vintage on the label.",BK,v=[V("Segura Viudas Brut Reserva Cava","Segura Viudas"),V("Insito Brut Cava Reserva","Insito")]),
   A("Cava Gran Reserva","Guarda Superior tier with at least 30 months on lees.",BK),
   A("Cava de Paraje Calificado","Single-vineyard top tier with at least 36 months on lees, created for outstanding sites.",BK,y="2017",a="Paraje Calificado"),
   A("Carta Nevada","Freixenet's early cava brand.",FX,mk="Freixenet",y="1941"),
   A("Cordon Negro","Freixenet's black-bottle brut cava.",FX,mk="Freixenet",y="1974",v=[V("Freixenet Cordon Negro Brut","Freixenet")])],
 "m":[["Berberana Gran Tradicion Brut Cava","Berberana"],["Borrasca Brut Cava","Borrasca"],["Conde de Caralt Blanc de Blancs Brut Cava","Conde de Caralt"],
      ["Marques de Monistrol Brut Cava","Marques de Monistrol"],["Rondel Brut Cava","Rondel"],["Rondel Rose Semi Seco Cava","Rondel"]]},
{"n":"Crémant","a":"","d":"Traditional-method sparkling wine of a French Crémant designation outside Champagne.",
 "t":["Crémant de Die","Crémant du Jura","Crémant de Savoie","Blanc · Rosé"],"s":"https://www.vinoscout.de/en/collections/schaumwein",
 "x":[A("Crémant de Loire","Loire crémant, mostly around Saumur, from Chardonnay, Chenin blanc and Cabernet franc.",CRE,y="1975",
     v=[V("Bouvet Crémant de Loire Excellence Brut","Bouvet Ladubay"),V("Bouvet Crémant de Loire Rosé Excellence Brut","Bouvet Ladubay")]),
   A("Crémant de Bourgogne","Burgundy crémant with at least 30% Pinot noir, Chardonnay, Pinot blanc or Pinot gris; Aligoté often fills the rest.",CRE,y="1975"),
   A("Crémant d'Alsace","Alsace crémant.",CRE,y="1976",v=[V("Wolfberger Crémant d'Alsace Brut","Wolfberger"),V("Wolfberger Crémant Rosé d'Alsace Brut","Wolfberger")]),
   A("Crémant de Limoux","Limoux crémant, mainly Mauzac with some Chenin blanc and Chardonnay.",CRE,y="c. 1990",
     v=[V("Sieur d'Arques Blason Rouge Crémant de Limoux Brut","Sieur d'Arques"),V("Sieur d'Arques Grande Cuvée 1531 Crémant de Limoux Brut","Sieur d'Arques")]),
   A("Crémant de Bordeaux","Bordeaux crémant, among the first of the later crémant appellations.",CRE,y="c. 1990",v=[V("Malesan Crémant de Bordeaux Brut","Castel Chateaux & Grands Crus")])]},
{"n":"Franciacorta","a":"","d":"Traditional-method sparkling wine of the Franciacorta DOCG in Lombardy, mainly from Chardonnay and Pinot nero.","s":FRA,
 "x":[A("Franciacorta (non-vintage)","Standard Franciacorta with at least 25 months after harvest, 18 on lees.",FRA,y="1995",a="Franciacorta Brut",
     v=[V("First Franciacorta (3,000 bottles)","Guido Berlucchi","1961",d="made by Franco Ziliani"),V("Franciacorta DOC",y="1967"),V("Franciacorta DOCG",y="1995")],dt="sweetness · dosage"),
   A("Franciacorta Satèn","Blanc de blancs from Chardonnay and/or Pinot bianco at 5 rather than 6 atmospheres.",FRA,a="Satèn"),
   A("Franciacorta Rosé","Rosé with at least 35% Pinot nero.",FRA),
   A("Franciacorta Millesimato","Vintage Franciacorta with at least 37 months after harvest, 30 on lees.",FRA,a="Vintage Franciacorta")]},
{"n":"Traditional-method sparkling wine","a":"Bottle-fermented sparkling wine · méthode traditionnelle","d":"Bottle-fermented sparkling wine from regions outside Champagne, Spain, Lombardy and the French crémant areas, e.g. England, Tasmania, Trentino.",
 "s":"https://www.vinoscout.de/en/collections/sekt",
 "x":[A("English sparkling wine","Traditional-method wine from Chardonnay, Pinot Noir and Pinot Meunier, with a PDO and the Sussex PDO.",ENG,y="1984",a="English Quality Sparkling Wine",
     v=[V("Carr Taylor (first commercial traditional-method)","","1984"),V("Nyetimber Blanc de Blancs","Nyetimber","1992",d="first vintage, released 1996"),
        V("Chapel Down Brut","Chapel Down"),V("Chapel Down Rosé Brut","Chapel Down"),V("Chapel Down Kit's Coty Blanc de Blancs Brut","Chapel Down"),
        V("Langham Perpetual Chardonnay 2nd Edition Brut Nature","Langham"),V("Sussex PDO",d="first English regional classification")],dt="blanc de blancs · rosé · vintage · county"),
   A("Trento DOC","Trentino bottle-fermented wine from Chardonnay, Pinot noir, Pinot Meunier and Pinot blanc.",TRE,a="Trentodoc",
     v=[V("Ferrari","Ferrari",d="Giulio Ferrari brought Chardonnay c. 1900"),V("Cesarini Sforza","Cesarini Sforza","1974")],dt="NV 15 · vintage 24 · Riserva 36 months on lees"),
   A("Tasmanian sparkling wine","Cool-climate sparkling wine from Tasmanian Pinot Noir and Chardonnay, also base wine for mainland houses.",TAS,
     v=[V("House of Arras Grand Vintage Extra Brut","House of Arras"),V("Josef Chromy Finesse Brut","Josef Chromy")],dt="Tamar Valley · Pipers River")],
 "m":[["Kreinbacher Classic Brut","Kreinbacher"],["Printhie Swift Blanc de Blancs Brut","Printhie"],["AvinoDos Blanc de Blanc Extra Brut","AvinoDos"],["Winding Wood Rosé Brut","Winding Wood"]]},
{"n":"Sekt","a":"Qualitätsschaumwein · Hauersekt (Austria)","d":"German or Austrian quality sparkling wine, mostly tank-fermented, at least 10% alcohol and 3 bar.",
 "t":["Charmat (tank)","Traditional method","Trocken · Brut"],"s":SEKT,
 "x":[A("Winzersekt","Grower's Sekt b.A. made in small lots from the producer's own vineyards.",SEKT,a="Hauersekt (Austria)"),
   A("Sekt b.A.","Sekt from grapes of one of Germany's 13 quality wine regions.",SEKT),
   A("Deutscher Sekt","Sekt made exclusively from German grapes.",SEKT),
   A("Henkell Trocken","Henkell's dry Sekt brand, patented in 1894.",HEN,mk="Henkell & Co.",y="1894",v=[V("Söhnlein Brillant","Henkell & Co."),V("Kupferberg","Henkell & Co.")])]},
{"n":"Asti & Moscato d'Asti","a":"Asti Spumante","d":"Sweet, low-alcohol sparkling wines of Piedmont made from Moscato Bianco.","s":ASTI,
 "x":[A("Asti DOCG","Fully sparkling sweet Moscato Bianco made in one tank by the Charmat method, about 7–9% alcohol.",ASTI,y="1993",a="Asti Spumante",
     v=[V("First sparkling Asti","Gancia","c. 1870",d="Carlo Gancia, Canelli"),V("Asti DOC",y="1967")]),
   A("Moscato d'Asti","Lightly sparkling (frizzante) Moscato Bianco, lower in alcohol than Asti.",ASTI)]},
{"n":"Pétillant naturel","a":"Pét-nat · méthode ancestrale · rurale · pétillant originel","d":"Sparkling wine bottled before the first fermentation ends, so the bubbles come from a single fermentation.","s":PET,
 "x":[A("Blanquette de Limoux méthode ancestrale","Limoux ancestral-method sparkling wine, considered the world's first sparkling wine.",PET,y="1531",dt="Saint-Hilaire monastery"),
   A("Col Fondo","Italian bottle-refermented, undisgorged sparkling wine with sediment.",PET,v=[V("Conegliano Valdobbiadene / Asolo Superiore Col Fondo",d="about 2.5 bar")]),
   A("Montlouis pétillant originel","Montlouis-sur-Loire ancestral sparkling wine; named 'originel' because 'naturel' is banned on French labels.",PET),
   A("Bugey Cerdon","Ancestral-method sparkling wine of Bugey.",PET),
   A("Gaillac méthode gaillacoise","Ancestral-method sparkling wine of Gaillac.",PET),
   A("Clairette de Die","Drôme sparkling wine made by the related dioise method.",PET,a="méthode dioise")]},
{"n":"Lambrusco","a":"","d":"Lightly sparkling red or rosé wine of Emilia-Romagna and Mantua from Lambrusco grapes.","t":["Secco","Amabile","Dolce","Rosato"],
 "s":"https://vinissimus.com/en/wines/lambrusco",
 "x":[A("Lambrusco di Sorbara","Fragrant, deep ruby Lambrusco of at least 60% Sorbara, generally the highest quality.",LAM),
   A("Lambrusco Grasparossa di Castelvetro","Dry, full-bodied, most tannic Lambrusco from Grasparossa.",LAM,v=[V("Chiarli Castelvetro Lambrusco","Chiarli")]),
   A("Lambrusco Salamino di Santa Croce","Light frizzante Lambrusco of at least 90% Salamino, dry or semi-sweet.",LAM),
   A("Reggiano Lambrusco","Largest Lambrusco area; sweet light frizzante or fuller dry wines.",LAM),
   A("Lambrusco Mantovano","Lombardy Lambrusco, typically dry.",LAM)]},
]
K='knowledge'
brands=[
{"n":"Codorníu","c":"Spain","f":"1551","seg":"Cava house","d":"Sant Sadurní d'Anoia house where Josep Raventós made Spain's first cava in 1872.","sig":["Codorníu cava"],"rel":["Freixenet"],"s":COD},
{"n":"Freixenet","c":"Spain","f":"1914","seg":"Cava house","d":"Large Sant Sadurní d'Anoia cava producer, owned by Henkell since 2018–2026 as Henkell Freixenet.","lines":["Carta Nevada","Cordon Negro","Elyssia","Freixenet ICE","Freixenet Prosecco DOC"],"sig":["Cordon Negro","Carta Nevada"],"rel":["Henkell & Co.","Codorníu"],"s":FX},
{"n":"Henkell & Co.","c":"Germany","f":"1832","seg":"Sekt house","d":"Wiesbaden Sekt producer in the Oetker group, owner of Freixenet and Mionetto.","lines":["Henkell Trocken","Söhnlein Brillant","Kupferberg","Deinhard","Mionetto"],"sig":["Henkell Trocken"],"rel":["Freixenet"],"s":HEN},
{"n":"Nyetimber","c":"England","f":"1988","seg":"English sparkling wine","d":"West Sussex estate planted 1988 with Champagne varieties; first vintage Blanc de Blancs 1992.","sig":["English sparkling wine"],"s":NYE},
{"n":"Chapel Down","c":"England","seg":"English sparkling wine","d":"Tenterden, Kent winery making mainly traditional-method sparkling wine.","sig":["English sparkling wine"],"s":CD},
{"n":"Ca' del Bosco","c":"Italy","f":"1969","seg":"Franciacorta house","d":"Erbusco winery whose winemaker Maurizio Zanella drove the Franciacorta DOCG.","sig":["Franciacorta (non-vintage)"],"rel":["Guido Berlucchi"],"s":CDB},
{"n":"Guido Berlucchi","c":"Italy","seg":"Franciacorta house","d":"First to release a Franciacorta-named wine, in 1961.","sig":["Franciacorta (non-vintage)"],"rel":["Ca' del Bosco"],"s":FRA},
{"n":"Ferrari","c":"Italy","seg":"Trento DOC house","d":"Trentino sparkling house founded by Giulio Ferrari, now run by Bruno Lunelli.","sig":["Trento DOC"],"s":TRE},
{"n":"Gancia","c":"Italy","seg":"Spumante house","d":"Canelli house whose founder Carlo Gancia is credited with the first sparkling Asti.","sig":["Asti DOCG"],"s":ASTI},
{"n":"Bouvet Ladubay","c":"France","seg":"Loire sparkling house","d":"Saumur producer of Crémant de Loire.","lines":["Excellence"],"sig":["Crémant de Loire"],"s":K},
]
notes=("Renamed 'Other sparkling wine' to 'Traditional-method sparkling wine'. Dropped placeholder models ['Sekt',''] and ['Lambrusco',''] (became kinds/archetypes). "
 "Trimmed duplicate Cava SKUs (Borrasca Rose, Conde de Caralt Brut, Rondel GOLD). Cava zones, Austrian Sekt g.U. pyramid, Crémant de Die/Jura/Savoie years, "
 "Moscato d'Asti DOCG year, Lambrusco DOC years and Rotkäppchen/Ridgeview/Bouvet pages (404) left out: not on retrieved pages. Wikidata rate-limited (429). No traditions: appellation wine is not an artisan-craft tradition here.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J7/shelves/02_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print('ok')
