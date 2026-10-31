import json,os
W='https://en.wikipedia.org/wiki/'
LA='https://www.laxmidals.com/'
def A(n,d,s,dt="",y=""):return {"n":n,"a":"","d":d,"mk":"","y":y,"s":s,"dt":dt}
k=[
{"n":"Lentils","a":"masoor","d":"Lentils of any colour, whole or split.","s":LA,"t":["Brown","Green","Black (beluga)","Red (split, hulled)","Whole","Split"],
 "x":[A("Lentille verte du Puy AOP","Small blue-green mottled lentil from France, sold elsewhere as French green.",W+"Lentil","Le Puy, France"),
 A("Beluga lentil","The Indianhead cultivar: tiny black lentil that holds its shape, named for resemblance to caviar.",W+"Lentil","black seed coat, yellow cotyledon"),
 A("Lenticchia di Castelluccio di Norcia IGP","Lentil of Umbria and Marche protected as a PGI.",W+"List_of_Italian_food_and_drink_products_with_protected_status","Umbria and Marche (Perugia, Macerata)")],
 "m":[["Lentille verte du Puy AOP",""]]},
{"n":"Chickpeas","a":"","d":"Kabuli or desi chickpeas, dried or tinned.","s":"https://stopandshop.com/groceries/browse-aisles/1088-dried-beans-lentils","t":["Kabuli (large, tan, smooth)","Desi (small, dark, rough)","Chana dal (split desi)"],
 "x":[A("Garbanzo de Escacena","Chickpea from Escacena del Campo, Huelva, listed with protected status in 2013.",W+"List_of_Andalusian_food_and_drink_products_with_protected_status","Escacena del Campo, Andalusia","2013")],
 "m":[["Garbanzo de Escacena PGI",""]]},
{"n":"Split peas","a":"dried peas","d":"Dried field peas, whole or split, green or yellow.","s":"https://stopandshop.com/groceries/browse-aisles/1088-dried-beans-lentils","t":["Green","Yellow","Whole","Split"]},
{"n":"Mung beans","a":"moong","d":"Small green mung beans, whole or split.","s":"https://www.pureindianfoods.com/products/organic-mung-beans","t":["Whole green","Split with skin (chilka)","Husked yellow (dhuli)"]},
{"n":"Black gram","a":"urad","d":"Black gram beans, whole or split.","s":LA,"t":["Whole (sabut)","Split with skin (chilka)","Husked split (dhuli)"]},
{"n":"Pigeon peas","a":"toor · arhar","d":"Pigeon peas, whole or split as dal.","s":LA,"t":["Whole dried","Toor dal (hulled, split)"]},
{"n":"Horse gram","a":"kulthi","d":"Dried horse gram seeds (Macrotyloma uniflorum).","s":"https://www.distacart.com/collections/pulses-dals"}]
out={"kinds":k,"brands":[],"traditions":[],"notes":"Lenticchia di Castelluccio is PGI per the Italian list. Lentilles vertes du Berry and Lenteja de La Armuña, Garbanzo de Fuentesauco not found on retrieved pages so omitted. Le Puy AOP status stays from old data (the Lentil page says PDO-protected). Dal forms (whole, chilka, dhuli) from the Dal page."}
json.dump(out,open('work/J5/shelves/02_03.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/J5/shelves/02_03.tmp','work/J5/shelves/02_03.json')
