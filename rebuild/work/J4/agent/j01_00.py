import sys; sys.path.insert(0,'work/J4/agent')
from lib_j4b import *
L="https://en.wikipedia.org/wiki/List_of_potato_cultivars"
x=[
A("Russet Burbank",L,"Long-russeted American baking and chipping potato, the world's reference processing cultivar.",y="1902",a="Idaho potato",dt="russet skin · floury · baking, fries"),
A("King Edward",L,"Cream-and-pink British floury main-crop, a classic roaster and mash potato.",y="1902",v=[("King Edward","","1902","UK origin")],dt="floury · roasting, mash"),
A("Maris Piper",L,"UK's most widely sold all-round main-crop, used for chips and roasting.",y="1966",dt="all-rounder"),
A("Bintje",L,"Dutch-bred yellow-fleshed main-crop, the classic Belgian and Dutch frying potato.",y="1904",dt="yellow flesh · chips"),
A("Désirée",L,"Red-skinned yellow-fleshed Dutch all-rounder.",y="1962",a="Desiree",dt="red skin · yellow flesh"),
A("Yukon Gold",L,"Canadian yellow-fleshed all-rounder that set the yellow-flesh market.",y="1965",dt="yellow flesh · all-rounder"),
A("Charlotte",L,"French waxy salad potato, blight-resistant.",y="1981",dt="waxy · salad"),
A("Ratte",L,"French fingerling salad potato with nutty flavour.",a="La Ratte",v=[("Pomme de terre de l'île de Ré AOP","","","regional appellation")],dt="waxy · fingerling"),
A("Jersey Royal",L,"Jersey new potato, the island's early crop, lifted in spring.",y="1880",a="International Kidney",v=[("Jersey Royal Potatoes PDO","","","protected designation of origin")],dt="waxy new potato"),
A("Nicola",L,"German waxy salad potato, German 'Potato of the Year' 2016.",dt="waxy · salad"),
A("Agria",L,"German yellow-fleshed floury potato for frying and baking.",y="1985",dt="floury · frying"),
A("Kennebec",L,"American white-skinned main-crop used for chips and baking.",y="1941"),
A("May Queen",L,"Japanese round potato widely grown for steaming and simmering.",a="メークイン",dt="waxy · simmering"),
A("Kitaakari",L,"Japanese yellow-fleshed potato bred in Hokkaido.",y="1987"),
A("Atlantic",L,"American chipping potato bred for crisp production.",y="1978"),
A("Cara",L,"Irish blight-resistant white main-crop.",y="1973"),
A("Rooster",L,"Irish red-skinned floury main-crop.",y="1990"),
A("Marfona",L,"Dutch all-round yellow main-crop.",y="1975"),
A("Sieglinde",L,"German waxy early potato, German 'Potato of the Year' 2010.",y="1938",dt="waxy"),
A("Red Pontiac",L,"American red-skinned potato.",a="Pontiac"),
A("Red La Soda",L,"American red-skinned potato.",y="1948"),
A("Bamberg potato",L,"Old German finger-shaped waxy potato, the Bamberger Hörnla.",y="1819",a="Bamberger Hörnla",v=[("Bamberger Hörnla PGI","","","protected geographical indication")],dt="fingerling · waxy"),
A("Puikula",L,"Finnish small waxy potato.",v=[("Lapin Puikula PDO","","","Lapland, protected designation of origin")]),
A("Vitelotte",L,"French purple-fleshed heritage fingerling.",dt="purple flesh"),
A("Pink Fir Apple",L,"Knobbly pink fingerling salad potato.",dt="waxy · salad"),
A("Kipfler",L,"Crescent-shaped waxy fingerling.",dt="fingerling"),
A("Huayro",L,"Peruvian Andean native potato.",dt="Andean native"),
A("Andean native potatoes","https://www.potatopro.com/companies/potato-park-parque-de-la-papa","Landraces (papa nativa) of the Andes, grown in thousands of colours and shapes.",v=[("Ajanhuiri",),("Imilla",),("Huayro",),("Quebrada de Humahuaca Andean Potatoes","","","GI region")],dt="over 1,400 varieties kept in Peru's Potato Park"),
]
m=["Pomme de terre de Merville PGI","Pomme de terre de Noirmoutier PGI","Béa du Roussillon AOP","Ayrshire New Potatoes PGI","Pembrokeshire Earlies PGI","New Season Comber Potatoes PGI","Lüneburger Heidekartoffeln PGI","De Meerlander PGI","Batata de Trás-os-Montes PGI","Lički krumpir PGI","Patata della Sila PGI","Patata di Bologna PGI","Patata del Fucino PGI"]
k=K("Potato","Fresh potato, organised by cultivar and, for cooking, waxy, floury or all-rounder.",x=x,t=["waxy","floury","all-rounder","new/early","maincrop","salad/fingerling"],s="https://plu.pro/commodity/potato",m=m)
t=[{"n":"Andean native potatoes","g":"Food & drink","r":"Andes, Peru","p":"ancient","d":"Community-conserved native potato landraces, kept in Peru's Potato Park near Cusco with the International Potato Center.","tech":"community seed conservation","mat":"native potato tubers","forms":["Huayro","Imilla"],"ctr":["Potato Park (Parque de la Papa), Sacred Valley"],"auth":"grown by the six Quechua communities of the Potato Park","s":"https://www.potatopro.com/companies/potato-park-parque-de-la-papa"}]
save("01_00",[k],[],t,"Cut 295 old names to sourced cultivars; GI regional potatoes kept as flat models or versions. Not sourced and dropped: most minor cultivars (e.g. russet breeding-line series). Danshaku not on source page, omitted.")
