import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'
AGM="RHS Award of Garden Merit"
def X(n,a,d,s,y='',v=(),dt='pot size · plug or basket',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
A=lambda n,d="",y="",mk="":(n,mk,y,d)
PT,PG,FU,LO=W+"Petunia",W+"Pelargonium",W+"Fuchsia",W+"Lathyrus_odoratus"
IW,IH,NA,NS=W+"Impatiens_walleriana",W+"Impatiens_hawkeri",W+"Nicotiana_alata",W+"Nicotiana_sylvestris"
SU="https://horticulture.co.uk/surfinia/"; ST="https://gardencrossings.com/collections/petunia-supertunia-annuals"
HF="https://humanflowerproject.com/blame-the-spencers/"; WC="https://loghouseplants.com/plants/shop/lathyrus-odoratus-winston-churchill-spencer-sweet-pea/"
PW="Proven Winners"
kinds=[
 {"n":"Petunia","a":"Petunia × atkinsiana · trailing petunia","d":"Living bedding plant of the genus Petunia, mostly hybrids grown from seed or cuttings for beds, pots and baskets.",
  "t":["grandiflora","multiflora","trailing","double","seed-raised","vegetative (cuttings)"],"s":ST,"x":[
  X("Surfinia","Surfinia trailing petunia","First trailing petunia brand, from Japanese breeding begun in 1987 and grown from cuttings; "+AGM+" series.",SU,y="1987",mk="Suntory Flowers",
    v=[A("Classic range","Velvet Blue, Sky Blue, Deep Red, Burgundy, Hot Pink, Purple Vein, White and others"),A("Early-flowering range","Trailing Light Yellow, Trailing Red, Trailing Blue Ocean")],dt="colour · plug or basket"),
  X("Supertunia","","Proven Winners vegetative petunia series for baskets and containers.",ST,mk=PW,
    v=[A("Supertunia Vista Bubblegum II","bestseller",mk=PW),A("Supertunia Vista Silverberry",mk=PW),A("Supertunia Vista Fuchsia",mk=PW),A("Supertunia Vista Snowdrift",mk=PW),A("Supertunia Black Cherry",mk=PW),A("Supertunia Bordeaux II",mk=PW),A("Supertunia Honey",mk=PW),A("Supertunia Mini Vista","compact sub-series",mk=PW)],dt="colour · Vista (vigorous mounding) or standard"),
  X("NightSky","","Petunia with purple flowers speckled white like a starry sky; "+AGM+".",PT),
  X("Other AGM petunia series","","Petunia and calibrachoa-type series holding the "+AGM+".",PT,v=[A("Conchita"),A("Storm"),A("Tumbelina","double-flowered")]),
  X("'Firefly'","bioluminescent petunia","Genetically engineered glowing petunia approved for sale by the USDA in 2023.",PT,y="2023"),
  ],"m":[["Supertunia Bermuda Beach",PW],["Supertunia Blue Tiara",PW],["Supertunia Daybreak Charm",PW],["Supertunia Giant Pink",PW],["Supertunia Vista Jazzberry",PW],["Supertunia Vista Paradise",PW]]},
 {"n":"Pelargonium","a":"bedding geranium · geranium","d":"Living pelargonium, the tender 'geranium' of pots and bedding, in zonal, ivy-leaved, regal, angel, unique and scented-leaved groups.",
  "t":["zonal","ivy-leaved","regal","angel","unique","scented-leaved","stellar","dwarf","miniature"],"s":PG,"x":[
  X("Zonal pelargonium","Pelargonium × hortorum","Bushy pelargoniums with a dark zone on the leaf, named P. × hortorum by Liberty Hyde Bailey in 1916.",PG,y="1916",
    v=[A("'Frank Headley'","cream-variegated, salmon-pink; "+AGM),A("'Mrs Quilter'","bronze leaves; "+AGM),A("'Dolly Varden'","variegated, scarlet; "+AGM),A("'Chelsea Gem'","double, variegated"),A("Stellar","bred by Ted Both in Australia, late 1950s–1960s")],dt="single or double · leaf zoning · pot size"),
  X("Ivy-leaved pelargonium","P. peltatum hybrids","Trailing pelargoniums for hanging baskets.",PG,v=[A("'L'Élégante'","white and purple; "+AGM)]),
  X("Regal pelargonium","Martha Washington · P. × domesticum","Large-flowered compact show pelargoniums.",PG,v=[A("'Lara Susan'","miniature regal")]),
  X("Angel pelargonium","","Smaller regal-like plants with P. crispum parentage.",PG,v=[A("'Spanish Angel'","lilac and magenta; "+AGM)]),
  X("Scented-leaved pelargonium","","Pelargoniums grown for fragrant leaves.",PG,
    v=[A("'Attar of Roses'","rose-scented; "+AGM),A("'Mabel Grey'","lemon-scented; "+AGM),A("'Lady Plymouth'","variegated P. graveolens; "+AGM),A("'Royal Oak'","balsam-scented; "+AGM),A("P. tomentosum","peppermint-scented; "+AGM)]),
  X("Unique pelargonium","","Shrubby, scented pelargoniums with small blotched flowers.",PG,v=[A("'Hindoo'","regal × unique cross")]),
  ]},
 {"n":"Fuchsia","a":"lady's eardrops","d":"Living fuchsia shrub grown for pendant flowers, either hardy types left outdoors or tender bush, standard and trailing types.",
  "t":["hardy","tender upright","trailing","standard","triphylla"],"s":FU,"x":[
  X("Fuchsia magellanica","hardy fuchsia","South American species reaching Tierra del Fuego that proved very hardy outdoors in Britain.",FU,v=[A("'Riccartonii'","crimson and purple; "+AGM)]),
  X("'Mrs Popple'","","Vigorous hardy fuchsia with red sepals and purple petals; "+AGM+".",FU),
  X("'Tom Thumb'","","Compact fuchsia with pink sepals and mauve petals; "+AGM+".",FU),
  X("'Hawkshead'","","White self-coloured fuchsia; "+AGM+".",FU),
  X("Triphylla fuchsias","Fuchsia triphylla","Long-tubed fuchsias from the species first described by Charles Plumier on Hispaniola.",FU,y="1703",v=[A("'Thalia'","orange; "+AGM)]),
  ]},
 {"n":"Busy Lizzie","a":"Impatiens · balsam · New Guinea impatiens","d":"Living impatiens bedding plant for shade, mainly Impatiens walleriana and New Guinea impatiens.",
  "t":["single","double","shade bedding","sun-tolerant"],"s":IW,"x":[
  X("Impatiens walleriana","busy Lizzie · sultana","East African shade bedding plant.",IW,v=[A("Super Elfin","series developed by Claude Hope in Costa Rica"),A("Accent"),A("Tempo"),A("'Fiesta Ole'","double-flowered")]),
  X("New Guinea impatiens","Impatiens hawkeri","Species from Papua New Guinea and the Solomon Islands, first collected in 1884, bred into many leaf and flower colours.",IH,y="1884",v=[A("Divine",AGM),A("Magnum",AGM)]),
  X("SunPatiens","","Impatiens series holding the "+AGM+".",IW,v=[A("SunHarmony",AGM)]),
  ]},
 {"n":"Sweet pea","a":"Lathyrus odoratus","d":"Living annual climbing sweet pea (Lathyrus odoratus), grown up canes for scented cut flowers; over 50 cultivars hold the RHS AGM.",
  "t":["Spencer","Grandiflora","old-fashioned","dwarf"],"s":LO,"x":[
  X("'Cupani'","Cupani's sweet pea","Small bicoloured wild Sicilian sweet pea grown by the friar Francesco Cupani in Palermo.",HF,y="1695"),
  X("Grandiflora","","Larger-flowered sweet peas bred by Henry Eckford from 1879 with Dr William Sankey.",HF,y="1879",v=[A("'Bronze Prince'","First Class Certificate 1882","1882")]),
  X("Spencer","'Countess Spencer'","Large frilly sweet peas from the plant raised by Silas Cole, gardener at Althorp, in 1900; now the most widely grown.",HF,y="1900",
    v=[A("'Countess Spencer'","original Spencer plant","1900"),A("'Winston Churchill'","deep red Spencer")],dt="colour · seed or plug"),
  ]},
 {"n":"Flowering tobacco","a":"Nicotiana · tobacco plant","d":"Living tobacco or flowering tobacco plant of the genus Nicotiana.",
  "t":["tall","dwarf","night-scented"],"s":"https://www.dobies.co.uk/flowers/flower-plants/all/nicotiana-alata_mh8433","x":[
  X("Nicotiana alata","jasmine tobacco · sweet tobacco","Flowering tobacco whose flowers open in the evening with a night scent; parent of many hybrids.",NA),
  X("Nicotiana sylvestris","woodland tobacco","Tall flowering tobacco up to 1.5 m with intense night scent; cultivars hold the "+AGM+".",NS),
  ]},
]
brands=[
 {"n":"Suntory Flowers","c":"Japan","seg":"Specialist","kf":"bedding plant breeding","d":"Horticultural arm of the Suntory group, breeder of Surfinia trailing petunias.","sig":["Surfinia"],"s":"knowledge"},
 {"n":"Proven Winners","c":"United States","seg":"Mainstream","kf":"branded ornamental plants","d":"American brand of ornamental plants sold through garden centres.","sig":["Supertunia"],"s":"knowledge"},
]
w('C3','05_03',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Two old kinds kept with old s; four new kinds sourced to Wikipedia. Old 13-SKU Supertunia list trimmed to a series archetype with 7 versions; the other 6 old names kept in m. Surfinia year from horticulture.co.uk (1987 breeding); Suntory credited from brand knowledge. No retrieved page named Nicotiana series (Domino, Nicki) or Ball/Thompson & Morgan lines, so left out; no tradition needed."})
