import json,os
W='https://en.wikipedia.org/wiki/'
S='https://stopandshop.com/groceries/browse-aisles/1088-dried-beans-lentils'
PV=W+'Phaseolus_vulgaris'
L=W+'List_of_Italian_food_and_drink_products_with_protected_status'
def A(n,d,s,dt="",y="",a=""):return {"n":n,"a":a,"d":d,"mk":"","y":y,"s":s,"dt":dt}
k=[
{"n":"Black beans","a":"turtle beans","d":"Small black Phaseolus beans.","s":S},
{"n":"Red kidney beans","a":"rajma","d":"The dark red, kidney-shaped Phaseolus bean.","s":S,"m":[["Rajma Jammu",""]]},
{"n":"Cannellini beans","a":"","d":"Large white kidney-shaped Phaseolus beans.","s":S,
 "x":[A("Fagiolo di Sorana IGP","Small, flat, pearly white Tuscan bean from the Pescia valley, PGI since 2002.",W+"Sorana_bean","Pistoia, Tuscany; sun-dried; thin skin","2002"),
 A("Fagiolo Cannellino di Atina DOP","Cannellini bean from Atina, Lazio, protected as a PDO.",L,"Frosinone, Lazio"),
 A("Fagiolo di Lamon IGP","Bean of the Belluno valley, Veneto, protected as a PGI.",L,"Belluno, Veneto")]},
{"n":"Pinto beans","a":"","d":"Mottled beige Phaseolus beans.","s":S},
{"n":"Navy (haricot) beans","a":"haricot beans","d":"Small white Phaseolus beans.","s":S,
 "x":[A("Haricot Tarbais","Large white bean with a very thin skin and soft melting flesh, PGI since 2000 and Label Rouge since 1997.",W+"Tarbais_bean","Hautes-Pyrénées, south-west France","2000")]},
{"n":"Small red beans","a":"","d":"Small red Phaseolus beans.","s":"https://www.laxmidals.com/"},
{"n":"Lima and butter beans","a":"","d":"Flat, pale lima (butter) beans.","s":"https://shop.camelliabrand.com/products/baby-lima-bean","m":[["Camellia Baby Lima Beans","Camellia Brand"]]},
{"n":"Runner beans (dried)","a":"","d":"Large dried beans of Phaseolus coccineus, such as the white Judión de La Granja.","s":W+"Phaseolus_coccineus",
 "x":[A("Judión de La Granja","Large white runner bean grown in San Ildefonso, Spain, basis of a Segovian bean dish with pork and chorizo.",W+"Phaseolus_coccineus","San Ildefonso (La Granja), Segovia")]},
{"n":"Black-eyed peas","a":"lobia","d":"Dried cowpeas (Vigna unguiculata) with a dark eye.","s":"https://www.distacart.com/collections/pulses-dals"},
{"n":"Dried broad beans","a":"fava · ful","d":"Dried broad beans (Vicia faba), whole or split.","s":"https://www.foodswinesfromspain.com/en/food/products/legumes---rice/calasparra-pdo","t":["Whole","Split"]},
{"n":"Dried soybeans","a":"","d":"Whole dried soybeans sold to cook.","s":"https://www.laxmidals.com/"},
{"n":"Adzuki beans","a":"azuki · red bean","d":"Small red East Asian beans (Vigna angularis), mostly sweetened into red bean paste.","s":W+"Adzuki_bean","t":["Red","Black adzuki"]}]
br=[{"n":"Rancho Gordo","c":"United States","f":"2001","seg":"Artisan & independent","kf":"heirloom beans","d":"Napa company founded by Steve Sando selling heirloom dried beans from the Americas.","s":W+"Rancho_Gordo"}]
out={"kinds":k,"brands":br,"traditions":[],"notes":"Added Runner beans (dried) to hold Judión de La Granja (a Phaseolus coccineus bean). Fabada Asturiana faba, Gigantes Kastorias and Rajma Chakrata could not be confirmed on retrieved pages so omitted; Rajma Jammu stays as old model. Rancho Gordo is in the brand register, with no per-variety range because no page listing it was retrieved."}
json.dump(out,open('work/J5/shelves/02_02.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/J5/shelves/02_02.tmp','work/J5/shelves/02_02.json')
