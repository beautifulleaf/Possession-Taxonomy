import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
E=W+"Eggplant"; V=W+"Avocado"
egg=[A("Black Beauty",E,"Black-skinned, oval to elongated globe aubergine, the standard Western type.",v=[("Black Magic",),("Classic",),("Dusky",)],dt="black · oval"),
A("Listada de Gandía",E,"Bicoloured striped aubergine.",v=[("Udumalapet",)],dt="striped"),
A("Violetta di Firenze",E,"Bicoloured gradient heirloom aubergine.",a="Violetta Lunga",v=[("Rosa Bianca",),("Bianca Sfumata di Rosa",),("Prosperosa",)],dt="bicolour gradient"),
A("Thai long green",E,"Slim green-skinned aubergine.",v=[("Louisiana Long Green",)],a="Thai (Long) Green",dt="green · slim"),
A("Pingtung Long",E,"Slim purple-black aubergine, narrow cucumber-like shape typical of Chinese types.",dt="slim · purple-black"),
]
av=[A("Hass",V,"Pebbly-skinned market reference, descended from one tree raised by Rudolph Hass in La Habra Heights, California, patented 1935; about 80% of the world's avocados.",y="1935",mk="",v=[("Lamb Hass",),("Gwen","","1982","Hass × Thille, higher yielding and more dwarfing"),("Pinkerton","","1970s","Hass × Rincon seedling, peels easily")],dt="flower type A"),
A("Fuerte",V,"Budwood from Atlixco, Mexico, commercialised in the US in 1911; leading US variety for half the 20th century.",y="1911",dt="flower type B"),
A("Bacon",V,"Smooth-skinned green cultivar, flower type B.",dt="type B"),
A("Reed",V,"Chance seedling found by James S. Reed in California, 1948; Guatemalan type.",y="1948",dt="type A"),
A("Ettinger",V,"Green-skinned cultivar, flower type B.",dt="type B"),
A("Zutano",V,"Green-skinned cultivar, flower type B.",dt="type B"),
A("Choquette",V,"Large Miami seedling with good disease resistance, widely grown in south Florida.",dt="West Indian × type, type A")]
kinds=[K("Aubergine","Fresh aubergine (eggplant).",x=egg,s="https://plu.pro/commodity/eggplant-aubergine",m=["Melanzana Rossa di Rotonda PGI","Τσακώνικη Μελιτζάνα Λεωνιδίου PDO","吉川ナス GI","Jalgaon Bharit Brinjal GI","Vellore Spiny Brinjal GI","Udupi Mattu Gulla Brinjal GI","Ramnagar Bhanta (Brinjal) GI","Agsechi Vayingim (Agassaim Brinjal) GI","Japanese eggplant"]),
K("Avocado","Fresh avocado, shelved with vegetables because it is not sweet as sold.",x=av,t=["Hass-type","green-skinned","West Indian","cocktail (stoneless)"],s="https://plu.pro/commodity/avocados"),
K("Okra","Fresh or frozen okra, the immature green seed capsule eaten whole.",s="https://plufinder.com/plu/4655",m=["ひばり野オクラ GI"],t=["green pod","red pod"]),
K("Fresh olive","Fresh uncured olive; cured table olives are in Pantry Staples.",s="https://www.freshpoint.com/?p=449",t=["green","semi-ripe","black"]),
]
save("01_07",kinds,[],[],"Aubergine and avocado archetypes from Wikipedia (Eggplant, Avocado). Clemson Spineless not on retrieved page; Japanese Senryo/Kamo not found; Fresh olive cultivars not attested (kept kind-level). Cut avocado models to attested cultivars.")
