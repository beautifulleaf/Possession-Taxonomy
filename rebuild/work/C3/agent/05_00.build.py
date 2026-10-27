import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'; GR=W+'Garden_roses'
AGM="RHS Award of Garden Merit"; HOF="WFRS Rose Hall of Fame (World's Favourite Rose)"
DA="David Austin Roses"; ME="Meilland"; KO="Kordes"; HA="Harkness Roses"; PO="Poulsen Roser"
def X(n,a,d,s,y='',v=(),dt='flower colour · bare-root or potted · bush or standard',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
kinds=[
 {"n":"Hybrid tea rose","a":"Rosa · large-flowered bush rose · HT · rose bush","d":"Living hybrid tea rose, a modern bush rose bearing large, high-centred flowers singly on long stems.",
  "t":["bush","standard (tree) rose","grandiflora"],"s":"","x":[
  X("'Peace'","'Madame A. Meilland' · 'Gioia' · 'Gloria Dei'","Light yellow to cream hybrid tea flushed crimson-pink at the edges, bred by Francis Meilland from 1935; first World's Favourite Rose (1976).",W+"Rosa_'Peace'",y="1935",mk=ME,
    v=[("'Peace'","Conard Pyle Co.","1945","US introduction under the name Peace"),("'Climbing Peace'","","","climbing sport")]),
  X("'Just Joey'","","Apricot-orange hybrid tea with copper shading, bred by Roger Pawsey and named for his wife; "+HOF+" 1994.",W+"Rosa_'Just_Joey'",y="1972"),
  X("'La France'","","Rose of 1867 regarded as the first of the modern hybrid tea class; marks the end of the old garden roses.",GR,y="1867"),
  X("'Papa Meilland'","","Dark red hybrid tea from Meilland.",W+"Meilland_International",y="1963",mk=ME),
  X("'Crimson Glory'","","Long-favoured crimson hybrid tea from Kordes.",W+"W._Kordes'_Söhne",y="1935",mk=KO),
  X("'Queen Elizabeth'","","Landmark grandiflora, a hybrid tea × floribunda back-cross bearing clusters of three to five flowers.",GR,y="1954"),
  X("Other landmark hybrid teas","","Hybrid teas named as class examples.",GR,v=[("'Mister Lincoln'","","",""),("'Double Delight'","","",""),("'Garden Party'","","",""),("'Black Baccara'","Meilland","",""),("'Line Renaud'","Meilland","2006","pink"),("'Louis de Funès'","Meilland","1987","yellow-red")]),
  ]},
 {"n":"Floribunda rose","a":"cluster-flowered bush rose · polyantha","d":"Living floribunda rose, a modern bush rose bearing flowers in large sprays, bred from polyanthas crossed with hybrid teas.",
  "t":["bush","standard","polyantha"],"s":GR,"x":[
  X("'Iceberg'","'Schneewittchen' · 'Fée des Neiges'","White floribunda bred by Reimer Kordes ('Robin Hood' × 'Virgo'); RNRS gold medal 1958 and World Favourite Rose 1983.",W+"Rosa_'Iceberg'",y="1958",mk=KO,
    v=[("'Climbing Iceberg'","Cants of Colchester","1968","climbing sport"),("weeping standard","","","")]),
  X("'Rödhätte'","","Early floribunda-type rose from Poulsen, a polyantha × hybrid tea.",GR,y="1907",mk=PO,v=[("'Else Poulsen'","Poulsen","1924","")]),
  X("'Anne Harkness'","","Floribunda from Harkness.",GR,mk=HA),
  X("'Bonica 82'","","Pink floribunda from Meilland.",W+"Meilland_International",y="1981",mk=ME),
  X("'Sunsprite'","","Floribunda from Kordes.",W+"W._Kordes'_Söhne",y="1973",mk=KO),
  X("Polyantha roses","","Small-flowered spray roses from R. chinensis × R. multiflora, first raised in France in the late 19th century.",GR,v=[("'Cécile Brünner'","","",""),("'Perle d'Or'","Joseph Rambaux","",""),("'Pink Fairy'","","",""),("'Red Fairy'","","","")]),
  ]},
 {"n":"English rose","a":"David Austin rose · Austin rose","d":"Living English rose, a repeat-flowering shrub rose bred by David Austin to join old-rose flower form and scent with modern repeat bloom.",
  "s":W+"David_Austin_Roses","x":[
  X("'Constance Spry'","","The first English rose.",W+"David_Austin_Roses",y="1961",mk=DA),
  X("'Graham Thomas'","AUSmas","Deep yellow English rose ('Charles Austin' × an 'Iceberg' seedling); "+AGM+" 1993 and World's Favourite Rose 2009.",W+"Rosa_'Graham_Thomas'",y="1983",mk=DA),
  X("'Gertrude Jekyll'","AUSbord","Bright pink English rose ('Wife of Bath' × 'Comte de Chambord'); "+AGM+".",W+"Rosa_'Gertrude_Jekyll'",y="1986",mk=DA),
  X("'Mary Rose'","","English rose of 1983.",W+"David_Austin_Roses",y="1983",mk=DA),
  X("'Abraham Darby'","","English rose of 1985.",W+"David_Austin_Roses",y="1985",mk=DA),
  X("Other David Austin introductions","","Further English roses named by Wikipedia.",W+"David_Austin_Roses",
    v=[("'Wife of Bath'","David Austin Roses","1969",""),("'Canterbury'","David Austin Roses","1969",""),("'Charles Austin'","David Austin Roses","1973",""),("'Golden Celebration'","David Austin Roses","1992",""),("'Darcey Bussell'","David Austin Roses","2006",""),("'Lady of Shalott'","David Austin Roses","2009","")]),
  ]},
 {"n":"Shrub rose","a":"modern shrub rose · ground-cover rose · patio rose · landscape rose · hybrid musk · hybrid rugosa","d":"Living modern shrub rose, an informal, robust rose for borders and hedges, including hybrid musks, rugosa hybrids, ground-cover and patio roses.",
  "t":["hybrid musk","hybrid rugosa","Canadian hardy","ground cover","patio"],"s":GR,"x":[
  X("Hybrid musk roses","","Disease-resistant repeat-flowering shrubs bred mainly by the Rev. Joseph Pemberton in the early 20th century.",GR,v=[("'Moonlight'","Pemberton","1913",""),("'Penelope'","Pemberton","1924",""),("'Buff Beauty'","","","")]),
  X("Hybrid rugosa roses","","Very hardy disease-resistant shrubs derived from Rosa rugosa.",W+"Rosa_rugosa",v=[("'Blanc Double de Coubert'","Cochet","1893","white double"),("'Hansa'","","","red-purple double"),("'Roseraie de L'Haÿ'","","","pink double"),("'Fru Dagmar Hastrup'","","","pink single"),("'Pink Grootendorst'","","","pink semi-double")]),
  X("Explorer series","Canadian hardy roses","Canadian roses hardy to about −35 °C, a programme led by Felicitas Svejda.",GR,y="1974",
    v=[("'Jens Munk'","","1974",""),("'Henry Hudson'","","1976",""),("'John Cabot'","","1978",""),("'William Baffin'","","1983",""),("'John Davis'","","1986","")]),
  X("Ground-cover roses","landscape roses","Low repeat-flowering roses usually under 60 cm.",GR,v=[("'Avon'","Poulsen","1992",""),("'Kent'","","1988","")]),
  X("Patio roses","","Compact roses 30–120 cm tall for small gardens and containers.",GR,v=[("'Open Arms'","Chris Warner","1995","")]),
  X("Kordes shrub roses","","Early Kordes shrub roses.",W+"W._Kordes'_Söhne",mk=KO,v=[("'Karl Förster'","Kordes","1930",""),("'Raubritter'","Kordes","1936",""),("'Harry Maasz'","Kordes","1939","")]),
  ]},
 {"n":"Climbing rose","a":"large-flowered climber · climbing sport","d":"Living climbing rose, a repeat-flowering rose with stiff canes usually 2–6 m long, trained on walls, pillars or arches.",
  "t":["large-flowered climber","climbing sport","noisette climber"],"s":GR,"x":[
  X("'New Dawn'","","Light pink climbing sport of 'Dr. W. Van Fleet', the first patented plant (1931); voted the most popular rose in the world in 1997.",W+"Rosa_'New_Dawn'",y="1930"),
  X("'Madame Alfred Carrière'","","Fragrant cream to pale pink tea-noisette climber bred by Joseph Schwartz, introduced in France in 1879.",'https://www.helpmefind.com/gardening/pl.php?n=3965',y="1875"),
  X("'Zéphirine Drouhin'","","Thornless Bourbon climber.",GR,y="1868",v=[("'Zéphirine Drouhin'","Bizot","1868","")]),
  X("'Pierre de Ronsard'","","Pink large-flowered climber from Meilland.",W+"Meilland_International",y="1985",mk=ME),
  X("Kordesii climbers","","Hardy climbers from Kordes' R. wichurana × R. rugosa line.",W+"W._Kordes'_Söhne",mk=KO,v=[("'Parkdirektor Riggers'","Kordes","",""),("'Leverkusen'","Kordes","",""),("'Hamburger Phönix'","Kordes","","")]),
  X("Climbing sports","","Climbing mutations of bush roses.",GR,v=[("'Climbing Peace'","","",""),("'Climbing Iceberg'","","1968",""),("'Blaze'","","","")]),
  ]},
 {"n":"Rambler rose","a":"rambling rose · hybrid wichurana","d":"Living rambler rose, a vigorous once-flowering rose 6–9 m long with flexible stems, for trees, pergolas and fences.",
  "s":GR,"x":[
  X("'Albertine'","","Salmon-pink hybrid wichurana rambler bred by René Barbier, introduced in 1923.",W+"Rosa_'Albertine'",y="1923"),
  X("'American Pillar'","","Landmark rambler.",GR),
  ]},
 {"n":"Old garden rose","a":"heritage rose · antique rose · historic rose","d":"Living old garden rose, belonging to a class that existed before 'La France' (1867): gallica, damask, alba, centifolia, moss, China, Portland, Bourbon, tea, noisette, hybrid perpetual.",
  "t":["gallica","damask","alba","centifolia","moss","China","Portland","Bourbon","tea","noisette","hybrid perpetual"],"s":GR,"x":[
  X("'Officinalis'","apothecary's rose · red rose of Lancaster · Rosa gallica var. officinalis","Semi-double deep pink gallica, county flower of Lancashire; "+AGM+".",W+"Rosa_gallica",
    v=[("'Versicolor'","","","Rosa Mundi; striped sport; "+AGM)]),
  X("Gallica roses","French rose","Once-flowering shrubs rarely over 1.25 m, including reds and crimsons.",W+"Rosa_gallica",v=[("'Charles de Mills'","","pre-1790",""),("'Duchesse de Montebello'","Laffay","1824",""),("'Cardinal de Richelieu'","Parmentier","pre-1847","")]),
  X("Damask roses","","Scented roses brought to Europe in the 13th century; the Autumn Damasks were the first remontant European roses.",GR,v=[("'Ispahan'","","",""),("'Madame Hardy'","","","")]),
  X("Alba roses","","Once-flowering scented white or pale pink roses with grey-green leaves.",GR,v=[("'Alba Semiplena'","","",""),("'Maiden's Blush'","","before 1400","")]),
  X("Centifolia and moss roses","Provence rose","Many-petalled once-flowering roses from 17th-century Netherlands, and their mossy-sepalled sports.",GR,v=[("'Common Moss'","","",""),("'Mousseline'","","","")]),
  X("China roses","","Repeat-flowering roses from Rosa chinensis that brought repeat bloom to Europe.",GR,v=[("'Old Blush'","","",""),("'Mutabilis'","","",""),("'Slater's Crimson China'","","1792","stud China"),("'Parsons' Pink China'","","1793","stud China")]),
  X("Portland roses","","Repeat-flowering class named after the Duchess of Portland, c. 1775.",GR,v=[("'Comte de Chambord'","","",""),("'Rose de Rescht'","","",""),("'James Veitch'","","","")]),
  X("Bourbon roses","","Roses from Île Bourbon (Réunion), introduced to France in 1820.",GR,y="1820",v=[("'Souvenir de la Malmaison'","Béluze","1843",""),("'Louise Odier'","","",""),("'Zéphirine Drouhin'","Bizot","1868","")]),
  X("Tea roses","","Roses with a scent like Chinese black tea, origin of the florist's rose form.",GR,v=[("'Lady Hillingdon'","","",""),("'Duchesse de Brabant'","","",""),("'Mrs Dudley Cross'","Paul","1907","")]),
  X("Noisette roses","","Class begun by South Carolina planter John Champneys.",GR,v=[("'Blush Noisette'","","1817",""),("'Desprez à fleurs jaunes'","Desprez","1830",""),("'Lamarque'","","","")]),
  X("Hybrid perpetual roses","","Class from 1838, the first to combine Asian repeat bloom with European lineages.",GR,y="1838",v=[("'La Reine'","Laffay","1844",""),("'Général Jacqueminot'","","",""),("'Ferdinand Pichard'","","",""),("'Reine des Violettes'","","","")]),
  ]},
 {"n":"Species rose","a":"wild rose · Rosa species","d":"Living wild rose species or close selection, usually single-flowered and grown for hips and natural form.",
  "s":W+"Rosa_rugosa","x":[
  X("Rosa rugosa","rugosa rose · beach rose · Japanese rose · Ramanas rose","Suckering East Asian coastal shrub with wrinkled leaves and large tomato-like hips.",W+"Rosa_rugosa",
    v=[("f. alba","","","white"),("'Rubra Plena'","","","semi-double dark pink")],dt="flower colour · hedge or specimen"),
  X("Rosa glauca","red-leaved rose · Rosa rubrifolia","European mountain shrub with blue-green to purplish waxy leaves and pink flowers; "+AGM+".",W+"Rosa_glauca",v=[("'Carmenetta'","","","hybrid with R. rugosa")]),
  X("Rosa moyesii","","Vigorous western Chinese shrub with red flowers and bottle-shaped hips.",W+"Rosa_moyesii",v=[("'Geranium'","","","compact; orange-scarlet; "+AGM)]),
  X("Rosa gallica","French rose · rose of Provins","Wild rose of southern and central Europe to Turkey and the Caucasus.",W+"Rosa_gallica"),
  ]},
]
brands=[
 {"n":DA,"c":"United Kingdom","f":"1969","seg":"Specialist","kf":"English roses","d":"Shropshire rose breeder founded by David C. H. Austin, creator of the English rose group with over 190 cultivars.","lines":["English roses"],"eras":["David C. H. Austin Sr., 1961–2018"],"sig":["'Graham Thomas'","'Gertrude Jekyll'","'Constance Spry'"],"rel":["Meilland","Kordes"],"s":W+"David_Austin_Roses"},
 {"n":ME,"c":"France","f":"c. 1850","seg":"Specialist","kf":"rose breeding","d":"Provençal rose house descended from Joseph Rambaux's Lyon nursery, breeder of 'Peace'; trades as Meilland International.","eras":["Francis Meilland, to 1958","Jacques Mouchotte, breeding from 1978"],"sig":["'Peace'","'Bonica 82'","'Pierre de Ronsard'"],"rel":["Kordes","David Austin Roses"],"s":W+"Meilland_International"},
 {"n":KO,"c":"Germany","f":"1887","seg":"Specialist","kf":"rose breeding","d":"Schleswig-Holstein rose breeder W. Kordes' Söhne, founded by Wilhelm Kordes I, known for hardy and disease-resistant roses.","lines":["Kordesii","Frühling series","hybrid musks"],"sig":["'Iceberg'","'Crimson Glory'"],"rel":["Tantau","Meilland"],"s":W+"W._Kordes'_Söhne"},
 {"n":HA,"c":"United Kingdom","seg":"Specialist","kf":"rose breeding","d":"English rose breeder and nursery.","sig":["'Anne Harkness'"],"s":"knowledge"},
 {"n":PO,"c":"Denmark","seg":"Specialist","kf":"rose breeding","d":"Danish rose breeder, raiser of early floribundas and ground-cover and patio roses.","sig":["'Rödhätte'","'Else Poulsen'","'Avon'"],"s":"knowledge"},
 {"n":"Tantau","c":"Germany","seg":"Specialist","kf":"rose breeding","d":"German rose breeder.","rel":["Kordes"],"s":"knowledge"},
 {"n":"Weeks Roses","c":"United States","seg":"Specialist","kf":"rose breeding","d":"American rose breeder and grower.","s":"knowledge"},
]
w('C3','05_00',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Old filter kind 'Rose bush' (k46) became 'Hybrid tea rose' with its old types split into seven new class kinds; it had no old source, so s left empty. Awards: RHS AGM and WFRS Hall of Fame noted per cultivar; ADR trial (Germany, since the 1950s; 'Iceberg' ADR 1960, revoked 2004) noted in notes only. Tantau and Weeks Roses given knowledge-only stubs with no founding year (not confirmed); no Tantau/Weeks/Harkness archetype beyond 'Anne Harkness' found on retrieved pages. HelpMeFind used for 'Madame Alfred Carrière' (no Wikipedia article). No traditions."})
