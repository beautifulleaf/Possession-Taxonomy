import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
L=W+"Lettuce"
let=[A("Iceberg",L,"Crisphead lettuce, the most popular type in the United States, developed in 1894 by Burpee.",a="crisphead",y="1894",dt="heat-sensitive"),
A("Romaine",L,"Long upright-headed lettuce used in Caesar salad.",a="cos",v=[("Forellenschluss","","","Austrian romaine")]),
A("Little Gem",L,"Compact dwarf romaine popular in the UK.",dt="dwarf romaine"),
A("Butterhead",L,"Loose-headed, sweet and tender lettuce.",a="Boston · Bibb"),
A("Batavia",L,"Between crisphead and leaf types, larger and more bolt-resistant.",a="Summercrisp · French crisp",v=[("Prajzerica","","","Croatian variety")]),
A("Loose-leaf",L,"Loosely bunched leaves, the most widely planted lettuce type; includes red leaf.",a="cutting · bunching",dt="Lollo and oak leaf types"),
A("Celtuce",L,"Stem lettuce grown for its stalk, mainly in Chinese cooking.",a="stem lettuce")]
chic=[A("Radicchio",W+"Common_chicory","Red or variegated bitter chicory; Treviso, Verona and Chioggia types are protected under PGI.",v=[("Radicchio Rosso di Treviso PGI",),("Radicchio Variegato di Castelfranco PGI",),("Radicchio di Chioggia PGI",),("Radicchio di Verona PGI",)]),
A("Witloof",W+"Common_chicory","Belgian endive: small cream-coloured head forced in the dark, technique found in Brussels in the 1850s.",a="Belgian endive · chicon",v=[("Brussels grondwitloof PGI",)]),
A("Puntarelle",W+"Common_chicory","Catalogna chicory group used throughout Italy.",a="Catalogna")]
kinds=[K("Lettuce","Fresh lettuce, whole heads, hearts or cut leaves; head type is the organising axis.",x=let,t=["crisphead/iceberg","romaine/cos","butterhead","Batavia","loose-leaf","living lettuce"],s="https://plu.pro/commodity/lettuce",m=["Insalata di Lusia PGI","Salate von der Insel Reichenau PGI","Lollo Rosso (Red Coral)","Lollo Biondo (Green Coral)","Oak Leaf","Mignonette"]),
K("Chicory","Fresh Cichorium leaves and forced chicons: radicchio, witloof, sugarloaf, curly endive.",x=chic,t=["radicchio","witloof","endive/frisée","escarole","puntarelle"],s="https://www.regione.calabria.it/wp-content/uploads/2023/06/DOP__IGP_e_STG_Registrati_agg_23.03.23.pdf"),
K("Rocket","Fresh rocket (arugula) leaves, sold as a salad or leaf vegetable rather than a herb.",t=["salad rocket","wild rocket (Diplotaxis)"],s="https://plu.pro/commodity/arugularocket",m=["Rucola della Piana del Sele PGI"],a="arugula"),
K("Watercress","Fresh watercress (Nasturtium officinale).",s="https://en.wikipedia.org/wiki/List_of_United_Kingdom_food_and_drink_products_with_protected_status",m=["Watercress TSG"]),
K("Lamb's lettuce","Fresh Valerianella leaves.",s="https://fr.wikipedia.org/wiki/Liste_des_indications_g%C3%A9ographiques_prot%C3%A9g%C3%A9es_fran%C3%A7aises",a="mâche · corn salad · doucette",m=["Feldsalat von der Insel Reichenau PGI","Mâche nantaise PGI"]),
K("Mizuna","Fresh mizuna leaves (Brassica rapa var. nipposinica), sold as a salad or cooking green.",x=[A("Benigoromo",W+"Mizuna","Mizuna variety with pink to purple anthocyanin colouring.",v=[("Pinky Pop",)])],s="https://www.melissas.com/products/mizuna",a="Japanese mustard greens"),
K("Mixed salad leaves","An undressed mix of salad leaves in which no one leaf makes up half or more of the weight; mesclun began in Provence.",s="https://plu.pro/commodity/lettuce",a="mesclun · spring mix"),
K("Sprouts & microgreens","Sprouts and cut microgreens sold to eat; microgreens are cut without roots, sprouts eaten whole.",t=["bean sprouts","alfalfa","cress","microgreens"],s="https://plu.pro/commodity/bean-sprouts",m=["大鰐温泉もやし GI"]),
]
brands=[{"n":"Bonduelle","c":"France","f":"1853","seg":"Mainstream","kf":"bagged salads, vegetables","d":"French vegetable group selling fresh bagged salads and frozen vegetables.","s":"knowledge"},
{"n":"Florette","c":"France","f":"","seg":"Mainstream","kf":"bagged salads","d":"European brand of ready-washed salad leaves.","s":"knowledge"},
{"n":"Fresh Express","c":"United States","f":"","seg":"Mainstream","kf":"bagged salads","d":"US brand of bagged salad blends.","s":"knowledge"},
{"n":"Taylor Farms","c":"United States","f":"","seg":"Mainstream","kf":"salad kits","d":"US fresh-cut salad and salad kit producer.","s":"knowledge"}]
save("02_00",kinds,brands,[],"Four lettuce kinds merged. Lollo Rosso, Oak Leaf not on retrieved page (kept as flat old models). Rocket (Diplotaxis) and chicory cultivars like Castelfranco beyond PGI names not separately sourced. Brand facts from knowledge; founding years left out except Bonduelle.")
