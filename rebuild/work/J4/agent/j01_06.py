import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
L=W+"List_of_Capsicum_cultivars"
sp=[
A("Bell pepper",W+"Bell_pepper","Blocky, non-pungent fruit of the Grossum Group of Capsicum annuum, green to red, yellow, orange.",a="blocky pepper · California Wonder",v=[("Permagreen","","","stays green when ripe")],dt="green, red, yellow, orange"),
A("Padrón",L,"Mostly mild frying pepper, about one in ten hot.",a="Pimiento de Padrón",dt="500-5,000 SHU"),
A("Shishito",L,"Mild Japanese frying pepper.",dt="50-200 SHU"),
A("Cubanelle",L,"Tapered frying pepper, green unripe, red mature.",dt="1-1,000 SHU"),
A("Friggitelli",L,"Sweet, mild Italian and Greek frying pepper, often pickled.",dt="100-500 SHU"),
A("Piquillo",L,"Spanish pepper listed among Capsicum cultivars.",a="Piquillo de Lodosa"),
A("Lamuyo",L,"Open-pollinated blocky type, named as example (Marconi Yellow).",a="Clovis"),
]
ch=[
A("Jalapeño",L,"Very popular green pepper, pickled or canned; smoke-dried ripe it is chipotle.",dt="Capsicum annuum · 2,500-8,000 SHU"),
A("Serrano",L,"Thin tapered chilli turning red when mature.",dt="Capsicum annuum · 10,000-23,000 SHU"),
A("Poblano",L,"Large heart-shaped dark green chilli; dried it is ancho, mature dried mulato.",dt="Capsicum annuum · 1,000-2,000 SHU"),
A("Anaheim",L,"Mild New Mexico chile brought to California in the 1900s, used for chile relleno.",dt="Capsicum annuum · 500-2,500 SHU"),
A("New Mexico chile",L,"Group of chiles including Big Jim, Chimayó and Sandia.",v=[("Chimayó","","","4,000-6,000 SHU"),("Big Jim",),("Sandia",)],dt="Capsicum annuum"),
A("Cayenne",L,"Long thin red chilli, often dried and ground.",dt="Capsicum annuum · 30,000-50,000 SHU"),
A("Bird's Eye",L,"Small pointed chilli with many local names in Southeast Asia.",dt="Capsicum annuum · 50,000-100,000 SHU"),
A("Piment d'Espelette",L,"Basque chilli grown at Espelette since about 1650; fresh fruit is Gorria.",a="Gorria",dt="Capsicum annuum · 1,500-2,500 SHU"),
A("Kashmiri chilli",L,"Kashmiri chilli listed in the Capsicum cultivar index.",dt="Capsicum annuum"),
A("Habanero",L,"Fruity floral chilli, close relative of many very hot peppers.",dt="Capsicum chinense · 100,000-350,000 SHU"),
A("Scotch Bonnet",L,"Chilli named for its resemblance to a tam o' shanter, close to habanero.",dt="Capsicum chinense · 150,000-325,000 SHU"),
A("Bhut Jolokia",L,"Mostly C. chinense with some C. frutescens genes, once Guinness's hottest.",a="Naga Jolokia · ghost pepper",v=[("Naga Mircha GI",)],dt="Capsicum chinense · up to 1,040,000 SHU"),
A("Carolina Reaper",L,"Developed by Ed Currie, once the Guinness hottest pepper.",mk="",dt="Capsicum chinense · 1.57-2.2 million SHU"),
A("Ají amarillo",L,"South American yellow chilli of Capsicum baccatum.",dt="Capsicum baccatum"),
A("Rocoto",L,"Black-seeded pubescens chilli, also called manzano or locoto.",a="manzano · locoto",dt="Capsicum pubescens · 30,000-100,000 SHU"),
]
kinds=[K("Sweet pepper","Fresh sweet, non-pungent pepper.",x=sp,t=["bell","pointed","frying","mini"],s="https://plu.pro/commodity/peppers-capsicums",m=["Peperone di Pontecorvo PGI","Peperoni di Senise PGI","Pimiento Riojano PGI","Pimiento de Fresno-Benavente PGI","Žitavská paprika PDO","万願寺甘とう GI","Szentesi paprika","Papaccella napoletana"]),
K("Chilli","Fresh or frozen pungent pepper, organised by species; heat is a detail.",x=ch,t=["annuum","chinense","baccatum","frutescens","pubescens"],s="https://plu.pro/commodity/peppers-capsicums",m=["Chile Habanero de Yucatán DO","Ají Chuquisaqueño DO","Guntur Sannam Chilli GI","Byadagi chilli GI","Mizo Chilli GI","Nandurbar Mirchi GI","Tabasco","Cheongyang","Malagueta","Peri-peri","清水森ナンバ GI"])]
save("01_06",kinds,[],[],"Pepper archetypes from Wikipedia list of Capsicum cultivars and Bell pepper; Pimiento de Herbón PDO, Piquillo de Lodosa PDO fresh and Kashmiri heat not confirmed. Cut ~90 chilli names to attested archetypes plus GI models.")
