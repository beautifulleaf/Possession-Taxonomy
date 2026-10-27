import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
W="https://en.wikipedia.org/wiki/"
L=W+"List_of_tomato_cultivars"
x=[
A("San Marzano",W+"San_Marzano_tomato","Heirloom plum tomato from San Marzano sul Sarno near Naples, the canning reference.",mk="",y="1926",v=[("Pomodoro San Marzano dell'Agro Sarnese-Nocerino PDO","","","protected designation of origin")],dt="plum · indeterminate · red"),
A("Roma",L,"Hybrid plum tomato, determinate, used for sauces and canning.",dt="plum"),
A("Pomodoro di Pachino",L,"Sicilian tomato from Pachino, listed as Pomodoro di Pachino.",v=[("Pomodoro di Pachino",)],dt="PGI"),
A("Raf",L,"Spanish red tomato listed as Raf.",dt="red"),
A("Moneymaker",L,"Heirloom UK greenhouse tomato popular with home growers because seed is cheap; blight prone.",dt="red · indeterminate"),
A("Alicante",L,"UK heirloom, once the classic breakfast tomato for productivity and taste.",dt="red · 2-6 oz"),
A("Gardener's Delight",L,"Heirloom bite-sized red tomato valued for high yields.",dt="small · red"),
A("Brandywine",L,"Pink potato-leaf beefsteak heirloom dating to 1885, noted for flavour and size.",y="1885",v=[("Yellow Brandywine",),("True Black Brandywine",)],dt="pink · beefsteak · up to 24 oz"),
A("Cherokee Purple",L,"Brown-purple beefsteak heirloom developed by Craig LeHoullier from seed from Tennessee.",dt="beefsteak · 8-12 oz"),
A("Mortgage Lifter",L,"Large pink beefsteak heirloom; two famous versions came from 1920s-30s West Virginia.",dt="beefsteak · 16-32 oz"),
A("Green Zebra",L,"Green and yellow striped tomato developed by Tom Wagner in Everett, WA c. 1983.",y="1983",dt="green/yellow · 3 oz"),
A("Black Krim",L,"Purple-brown beefsteak heirloom from the Crimea area, rich sweet flavour.",dt="beefsteak"),
A("Campari",L,"Hybrid cocktail tomato known for juiciness, high sugar and low acidity.",dt="small · hybrid"),
A("Kumato",L,"Brown-red hybrid tomato sold under a trade name for the variety Olmeca.",a="Olmeca",dt="hybrid · brown/red"),
A("Early Girl",L,"Red hybrid, named to complement Better Boy.",dt="hybrid"),
A("Better Boy",L,"Red hybrid with medium-large fruit.",dt="hybrid"),
A("Celebrity",L,"Flattened globe hybrid, AAS winner 1998, known for flavour.",dt="hybrid · 10 oz"),
]
m=["Tomaten von der Insel Reichenau PGI","Tomate La Cañada PGI","Τοματάκι Σαντορίνης (Tomataki Santorinis) PDO","Pomodorino del Piennolo del Vesuvio","Pomodorino di Manduria","Tomberry","Sungold","Cuore di Bue","Marmande","Momotaro","Super Sweet 100","Cherubs (NatureSweet)","Y.E.L.O. Cocktail Tomato (Mastronardi Produce)"]
kinds=[K("Tomato","Fresh tomato, shape and colour as types, grouped by named cultivar.",x=x,t=["cherry","grape","plum/roma","beefsteak","round/salad","on the vine","heirloom"],s="https://plu.pro/commodity/tomatoes",m=m),
K("Tomatillo","Fresh husked Physalis philadelphica fruit.",s=W+"Tomatillo",a="husk tomato")]
brands=[{"n":"NatureSweet","c":"United States","f":"","seg":"Mainstream","kf":"greenhouse tomatoes","d":"Brand of branded greenhouse cherry and snacking tomatoes.","lines":["Cherubs","Eclipses","Glorys","Jubilees","SunBursts"],"s":"knowledge"},
{"n":"Mastronardi Produce","c":"Canada","f":"","seg":"Mainstream","kf":"greenhouse tomatoes","d":"Greenhouse grower marketing Sunset and Campari-branded tomatoes.","lines":["Sunset","Campari"],"s":"knowledge"}]
save("01_05",kinds,brands,[],"Merged six tomato kinds; ~150 old cultivar names cut to attested archetypes (list of tomato cultivars page). Sungold, Marmande, Cuore di Bue, Momotaro, Ailsa Craig not found on retrieved pages; kept as flat models (old data) or dropped. Brand facts founding years left out.")
