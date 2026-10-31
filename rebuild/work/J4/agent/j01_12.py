import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
asp=[A("Green asparagus",W+"Asparagus","The most widely eaten type.",dt="green"),
A("White asparagus",W+"Asparagus","Blanched by earthing up, peeled before cooking; centrepiece of the German Spargel season.",a="Spargel",dt="white",v=[("Schrobenhausener Spargel PGI",),("Beelitzer Spargel PGI",),("Abensberger Spargel PGI",),("Asparago Bianco di Bassano PGI",),("Asperge des Sables des Landes PGI",)]),
A("Violetto d'Albenga",W+"Asparagus","Purple asparagus developed near Albenga, Italy; high sugar, low fibre, turns green on cooking.",a="purple asparagus",dt="purple")]
art=[A("Green Globe",W+"Globe_artichoke","Large green globe artichoke grown in the USA and South Africa.",dt="large green"),
A("Camus de Bretagne",W+"Globe_artichoke","Large green Breton artichoke.",dt="large green"),
A("Romanesco artichoke",W+"Globe_artichoke","Large purple type.",a="Romanesco",v=[("Carciofo Romanesco del Lazio PGI",)],dt="large purple"),
A("Spinoso Sardo",W+"Globe_artichoke","Spined artichoke type, listed as Spinoso Sardo e Ingauno.",a="Spinoso Sardo e Ingauno",v=[("Carciofo Spinoso di Sardegna PGI",)],dt="spined"),
A("Violetta di Chioggia",W+"Globe_artichoke","Violet artichoke named in the article.")]
cel=[A("Pascal",W+"Celery","Cultivar dominating North American commercial celery, in tight straight parallel bunches.",dt="green")]
rh=[A("Timperley Early",W+"Rhubarb","Early rhubarb with RHS AGM, recommended for flavour.",dt="field/forced"),
A("Victoria",W+"Rhubarb","Rhubarb cultivar recommended by Lawrence D. Hills for flavour."),
A("Rhubarb Triangle forcing",W+"Rhubarb","Yorkshire candlelight forcing in sheds between Wakefield, Leeds and Morley gives sweeter, more tender stalks.",a="Yorkshire forced rhubarb",v=[("Yorkshire Forced Rhubarb PDO",)])]
card=[A("Argenté de Genève",W+"Cardoon","Spineless local cultivar of Geneva, introduced by Huguenot refugees around 1685.",a="Cardy",v=[("Cardon épineux genevois AOP",)])]
kinds=[K("Asparagus","Fresh or frozen asparagus spears.",x=asp,t=["green","white","purple","wild"],s="https://plu.pro/commodity/asparagus",m=["Marchfeldspargel PGI","Bornheimer Spargel PGI","Walbecker Spargel PGI","Vale of Evesham Asparagus PGI","Espárrago de Navarra PGI","Brabantse Wal Asperges PDO","Asparago verde di Altedo PGI"]),
K("Globe artichoke","Fresh artichoke heads; artichoke hearts in jars or tins are in Pantry Staples.",x=art,s="https://www.regione.calabria.it/wp-content/uploads/2023/06/DOP__IGP_e_STG_Registrati_agg_23.03.23.pdf",m=["Alcachofa de Tudela PGI","Artichaut du Roussillon PGI","Carciofo Brindisino PGI","Carciofo di Paestum PGI"]),
K("Celery","Fresh celery.",x=cel,t=["self-blanching","blanched"],s="https://plu.pro/commodity/celery",m=["Fenland Celery PGI","Sedano Bianco di Sperlonga PGI","山形セルリー GI"]),
K("Florence fennel","Fresh fennel bulb; fennel seed is in Pantry Staples.",s="https://www.regione.calabria.it/wp-content/uploads/2023/06/DOP__IGP_e_STG_Registrati_agg_23.03.23.pdf",m=["Finocchio di Isola Capo Rizzuto PGI"],a="finocchio"),
K("Rhubarb","Fresh or frozen rhubarb stalks (leaf stems), sold forced or field-grown, cooked with sugar.",x=rh,t=["forced","field-grown"],s="https://plufinder.com/plu/4745"),
K("Cardoon","Fresh Cynara cardunculus leaf stalks.",x=card,s="https://www.aop-igp.ch/en/about-pdo-pgi/register-of-the-swiss-designations-of-origin-and-geographical-indications/",m=["Cardo gobbo di Nizza Monferrato"]),
K("Bamboo shoot","Fresh bamboo shoots; tinned or boiled-packed shoots are in Pantry Staples.",s="https://www.cnipa.gov.cn/art/2026/8/4/art_1401_208262.html",a="takenoko",m=["八渡笋 地理标志产品"]),
K("Nopal","Fresh Opuntia pads, whole or cut, sold to cook as a vegetable; the fruit is prickly pear.",s="https://www.cosmos.com.mx/empresa/nopal-export-430z.html",a="nopales · cactus pads"),
K("Wild shoots & fiddleheads","Fresh wild edible shoots and fern fronds: warabi, urui, kogomi, fiddleheads, taranome.",x=[A("Ostrich fern fiddlehead",W+"Fiddlehead_fern","Furled fronds of Matteuccia struthiopteris, kogomi in Japan.",a="kogomi"),A("Bracken fiddlehead",W+"Fiddlehead_fern","Pteridium aquilinum fronds eaten as kogomi, gosari or juécài; must be fully cooked.",a="warabi · gosari")],t=["warabi","kogomi","taranome","ostrich fern"],s="https://www.maff.go.jp/j/shokusan/gi_act/register/index.html",m=["小笹うるい GI"]),
]
save("01_12",kinds,[],[],"Rhubarb PDO status and Fenland Celery PGI not confirmed on retrieved pages (kept as old-data models/versions). Warabi alias for bracken attached by knowledge (page only mentions warabimochi). Cut asparagus GI list to representative models.")
