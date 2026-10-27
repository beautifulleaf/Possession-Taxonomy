import sys; sys.path.insert(0,'work/C3/agent'); from w import w
W='https://en.wikipedia.org/wiki/'
AGM="RHS Award of Garden Merit"
def X(n,a,d,s,y='',v=(),dt='',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
A=lambda n,d="",y="",mk="":(n,mk,y,d)
OLDB="https://briteleaf.com/"; OLD="https://www.starkbros.com/products/fruit-trees"
CT='rootstock · pot size · bush or standard'
NT='rootstock or own-root · bare-root or pot · pollinator group'
ZG="Zaiger Genetics"
kinds=[
 {"n":"Orange tree","a":"sweet orange · Citrus × sinensis","d":"Sweet and blood orange trees.","t":["navel","common (Valencia type)","blood"],"s":OLDB,"x":[
  X("Washington navel","navel orange · Bahia","Seedless navel orange from a Bahia, Brazil mutation; Riverside, California trees from cuttings sent to Eliza Tibbets.",W+"Navel_orange",y="1873",dt=CT,
    v=[A("Cara Cara","pink-fleshed navel, Hacienda Cara Cara, Venezuela","1976"),A("Chocolate navel","brown peel, Valencia, Spain","2006")]),
  X("Valencia","","Late sweet orange raised by William Wolfskill in Southern California, grown mainly for juice.",W+"Valencia_orange",y="mid-19th century",dt=CT),
  X("Moro","","Deepest-coloured blood orange, a bud mutation of Sanguinello Moscato from around Lentini, Sicily.",W+"Blood_orange",y="early 19th century",dt=CT,
    v=[A("Tarocco","Italy's most popular table orange"),A("Sanguinello","Spain","1929")]),
  ]},
 {"n":"Lemon & lime tree","a":"lemon and lime tree","d":"Lemon and lime trees.","t":["lemon","lime","variegated"],"s":OLDB,"x":[
  X("Meyer lemon","Citrus × meyeri","Chinese citron hybrid brought to the USA by Frank N. Meyer; a compact, popular pot lemon.",W+"Meyer_lemon",y="1908",dt=CT,
    v=[A("Improved Meyer","virus-free selection released by the University of California","1975")]),
  X("Eureka","Four Seasons","Year-round fruiting lemon developed in 19th-century California from Neapolitan and Sicilian stock.",W+"Lemon",y="19th century",dt=CT,
    v=[A("Variegated Pink Eureka","pink flesh, striped skin")]),
  X("Lisbon","","Smooth, thin-skinned lemon brought to California by Portuguese immigrants.",W+"Lemon",dt=CT),
  X("Femminello St. Teresa","Sorrento","Italian lemon rich in zest oil, used for limoncello.",W+"Lemon",dt=CT),
  X("Ponderosa","","Very large, thick-skinned citron × pomelo hybrid sold as a lemon.",W+"Lemon",dt=CT),
  X("Tahiti lime","Persian lime · Bearss lime · Citrus × latifolia","Seedless triploid lime, the most widely grown commercial lime; Bearss selection from Porterville, California.",W+"Persian_lime",y="c. 1895",dt=CT),
  X("Kaffir lime","makrut lime · Thai lime · Citrus hystrix","Southeast Asian lime grown mostly for its aromatic leaves.",W+"Kaffir_lime",dt=CT),
  ]},
 {"n":"Mandarin tree","a":"tangerine · satsuma · clementine","d":"Mandarin, tangerine and tangelo trees.","t":["satsuma","clementine","tangerine","tangelo"],"s":OLDB,"x":[
  X("Satsuma","Citrus unshiu · unshu mikan","Cold-hardy seedless Japanese mandarin, surviving about −9 °C.",W+"Satsuma_mandarin",y="1600s",dt=CT,
    v=[A("Owari","brought from Japan to the USA","1878"),A("Miyagawa Wase","major Japanese cultivar"),A("Okitsu Wase","major Japanese cultivar")]),
  X("Clementine","","Mandarin × sweet orange hybrid from Brother Clément Rodier's orphanage garden at Misserghin, Algeria.",W+"Clementine",y="1902",dt=CT,
    v=[A("Algerian","original"),A("Fina","Spain"),A("Clemenules","seedless Fina mutation, Spain")]),
  ]},
 {"n":"Speciality citrus","a":"other citrus trees · unusual citrus","d":"Living citrus tree or bush of the less common kinds, compact ones kept as houseplants included.","t":["houseplant","variegated"],"s":OLD,"x":[
  X("Calamondin","calamansi · Citrus × microcarpa","Kumquat × mandarin hybrid, the usual potted citrus houseplant; "+AGM+".",W+"Calamondin",dt="pot size · variegated or plain",v=[A("Variegated calamondin","striped fruit")]),
  X("Kumquat","Fortunella","Small, cold-hardy citrus eaten whole.",W+"Kumquat",dt=CT,
    v=[A("Nagami","oval kumquat"),A("Meiwa","round, sweet"),A("Marumi","round kumquat; "+AGM),A("Centennial Variegated","striped sport of oval kumquat"),A("Limequat","key lime × kumquat hybrid")]),
  X("Buddha's hand","fingered citron · Citrus medica var. sarcodactylis","Citron whose fruit splits into fingers, grown for scent and rind.",W+"Buddha's_hand",dt=CT),
  X("Yuzu","Citrus × junos","Frost-hardy East Asian citrus, mandarin × ichang papeda, used for zest and juice.",W+"Yuzu",dt=CT),
  X("Finger lime","caviar lime · Citrus australasica","Australian rainforest lime whose juice vesicles are sold as lime caviar.",W+"Citrus_australasica",dt=CT),
  ],"m":[["Buddha's Hand",""],["Calamondin Orange",""]]},
 {"n":"Almond tree","a":"Prunus dulcis","d":"Living almond tree (Prunus dulcis) grown for nuts.","t":["self-fertile","needs pollinator","semi-dwarf"],"s":OLD,"x":[
  X("Nonpareil","","Leading thin-shelled almond, needs another cultivar for pollination.",W+"Almond",y="1800s",dt=NT),
  X("All-in-One","","Self-fertile semi-dwarf almond patented by Zaiger Genetics (PP04304).","https://ngr.ucdavis.edu/treedetails.cfm?v=6231",y="1977",mk=ZG,dt=NT),
  X("Tuono","","Self-fertile Italian almond with a thick shell.",W+"Almond",dt=NT),
  X("Marcona","","Spanish almond with a short, round, sweet kernel.",W+"Almond",dt=NT),
  ]},
 {"n":"Walnut tree","a":"Juglans · Persian walnut · English walnut","d":"Living walnut tree (Juglans) grown for nuts.","t":["grafted","seedling"],"s":OLD,"x":[
  X("Broadview","","Compact, early-bearing self-fertile walnut from Kelowna, British Columbia, by David and Jack Gellaty.","https://www.frankpmatthews.com/catalogue/walnut",y="1900s",dt=NT),
  X("Franquette","","Old walnut cultivar, among those most susceptible to walnut husk fly.",W+"Juglans_regia",dt=NT),
  X("Buccaneer","","Self-fertile walnut with round nuts for pickling.","https://www.frankpmatthews.com/catalogue/walnut",dt=NT,v=[A("Chandler","large thin-shelled nuts"),A("Fernette","pollinator for Fernor"),A("Seidersdorfer","thin-shelled")]),
  ]},
 {"n":"Pecan tree","a":"Carya illinoinensis","d":"Living pecan tree (Carya illinoinensis) grown for nuts.","s":OLD,"x":[
  X("Centennial","","First pecan successfully grafted, by Antoine at Oak Alley Plantation, Louisiana.",W+"Pecan",y="1846",dt=NT),
  X("Elliott","","Older pecan cultivar resistant to pecan scab.",W+"Pecan",dt=NT,v=[A("Stuart"),A("Desirable"),A("Schley")]),
  X("Kanza","","USDA grafted pecan for northern climates, cold tolerant.",W+"Pecan",dt=NT),
  ]},
 {"n":"Hazelnut","a":"cobnut · filbert · Corylus","d":"Living hazel bush (Corylus avellana or C. maxima) grown for cobnuts or filberts.","t":["cobnut (C. avellana)","filbert (C. maxima)","red-leaved"],"s":"https://www.rhs.org.uk/nuts/cobnuts-filberts","x":[
  X("Kentish Cob","Lambert's Filbert","Filbert of the Sevenoaks–Maidstone district of West Kent, once the leading English cobnut.","https://www.slowfood.org.uk/?p=1752",y="c. 1830",dt=NT),
  X("Cosford","","Thin-shelled sweet cobnut and reliable pollinator.","https://www.rhs.org.uk/nuts/cobnuts-filberts",dt=NT,v=[A("Butler","heavy cropper"),A("Pearson's Prolific","Nottingham Prolific; compact")]),
  X("Halle Giant","Hall's Giant · Merveille de Bollwiller","Hardy, vigorous filbert with large nuts.","https://www.rhs.org.uk/nuts/cobnuts-filberts",dt=NT,v=[A("Gunslebert","heavy cropper"),A("Ennis","large round nuts")]),
  X("Red Filbert","","Filbert with purple spring leaves and red nuts; "+AGM+".","https://www.rhs.org.uk/nuts/cobnuts-filberts",dt=NT),
  ]},
 {"n":"Sweet chestnut","a":"Castanea sativa · Spanish chestnut · marron","d":"Living sweet chestnut tree (Castanea sativa) grown for its nuts.","t":["grafted","seedling"],"s":W+"Castanea_sativa","x":[
  X("Marron de Lyon","","Grafted chestnut bearing a single large nut, cropping within about five years.",W+"Castanea_sativa",dt=NT,v=[A("Paragon","single large nut")]),
  X("Bouche de Bétizac","","French chestnut cultivar.",W+"Castanea_sativa",dt=NT,v=[A("Maraval"),A("Marigoule"),A("Marsol"),A("Précoce Migoule")]),
  ]},
]
brands=[
 {"n":ZG,"c":"United States","seg":"Specialist","kf":"fruit breeding","d":"Fruit-breeding company of Chris Floyd Zaiger, patentee of the All-in-One almond.","sig":["All-in-One almond"],"s":"https://ngr.ucdavis.edu/treedetails.cfm?v=6231"},
]
w('C3','06_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"All 7 old kinds kept with old s; 'Other citrus trees' dissolved into Speciality citrus (old models Buddha's Hand and Calamondin Orange kept in m and as archetypes). Hazelnut and Sweet chestnut added from RHS / Wikipedia pages. UC Riverside Citrus Variety Collection not fetched (Wikipedia covered the brief). Nonpareil date from Wikipedia ('1800s'); Kentish Cob raiser (Lambert) seen only in search snippets, so not recorded. All-in-One date: patent year 1977 from UC Davis NGR."})
