import json,os
W='https://en.wikipedia.org/wiki/'
P='https://shop.piedimonte.com.au/category/flour'
SM='https://www.shipton-mill.com/collections/all-flour'
BB='https://brickovenbaker.com/pages/information-about-caputo-flours'
def A(n,d,s,dt="",mk="",y=""):return {"n":n,"a":"","d":d,"mk":mk,"y":y,"s":s,"dt":dt}
k=[
{"n":"Plain flour","a":"all-purpose wheat flour","d":"Refined soft-wheat flour for general baking, about 9.5-11.5% protein.","s":P,"t":["Self-raising","Cake flour (6-7% protein)","Soft cake and pastry"],
 "x":[A("French Type 45","French white flour listed by Shipton Mill among pastry and cake flours.",SM,"T45 ash grading",mk="Shipton Mill"),A("French Type 55","French white flour listed by Shipton Mill among pastry and cake flours.",SM,"T55",mk="Shipton Mill")]},
{"n":"Bread flour","a":"pizza flour · bread and pizza wheat flour","d":"Stronger wheat flour for yeast doughs, about 11.5-13.5% protein.","s":P,"t":["Strong white","Type 00","Type 0"],
 "x":[A("Caputo Pizzeria Tipo 00","Caputo's Neapolitan-style pizza flour, Tipo 00, 1 kg bags.",BB,"Tipo 00",mk="Caputo"),
 A("Wildfarmed White Bread Flour T65","UK regenerative-grain white flour, T65, about 11% protein.","https://www.rattonpantry.co.uk/products/wildfarmed-strong-white-bread-flour-t65","T65 · 100% UK grain",mk="Wildfarmed"),
 A("Italian Type 00","Fine Italian grade often preferred for pizza and pasta, sold by Shipton Mill.",SM,"Type 00",mk="Shipton Mill")],
 "m":[["Caputo Cuoco (red bag) Tipo 00","Caputo"],["Caputo Manitoba Oro Tipo 0","Caputo"],["Caputo Nuvola Super Type 0","Caputo"],["Molino Dallagiovanna La Napoletana Type 00","Molino Dallagiovanna"],["Wildfarmed White Bread Flour T65","Wildfarmed"]]},
{"n":"Wholemeal flour","a":"wholemeal wheat flour","d":"Wheat flour milled from the whole grain.","s":SM,"t":["Stoneground","Roller-milled","T150"],"m":[["Wildfarmed Wholemeal Flour T150","Wildfarmed"]]},
{"n":"Spelt flour","a":"","d":"Flour milled from spelt.","s":SM,"t":["White","Wholemeal"]},
{"n":"Atta flour","a":"whole-wheat atta","d":"Finely ground whole-wheat flour for South Asian flatbreads.","s":"https://punjabigroceries.com/collections/atta-flour","m":[["Aashirvaad Whole Wheat Atta","Aashirvaad"]]},
{"n":"Semolina","a":"sooji · rava","d":"Coarse granular milled wheat endosperm.","s":"https://www.kesargrocery.com/speciality-flour/?page=2&sort=title","t":["Rimacinata (re-milled)","Coarse"],"m":[["Caputo Semola Rimacinata","Caputo"],["Molino Dallagiovanna Semola Rimacinata","Molino Dallagiovanna"]]}]
br=[{"n":"Caputo","c":"Italy","seg":"Heritage manufactory","kf":"00 pizza flour","d":"Antimo Caputo mill in Naples (Mulino Caputo).","s":BB},
{"n":"Wildfarmed","c":"United Kingdom","seg":"Artisan & independent","kf":"regenerative flour","d":"Flour milled from UK regenerative farmers' grain.","s":"https://www.rattonpantry.co.uk/products/wildfarmed-strong-white-bread-flour-t65"},
{"n":"Shipton Mill","c":"United Kingdom","seg":"Artisan & independent","kf":"organic flours","d":"UK mill selling a wide flour range, from Type 00 to heritage grains.","s":SM},
{"n":"King Arthur Baking","c":"United States","f":"1790","seg":"Premium","kf":"US flour","d":"Oldest US flour company, founded in Boston by Henry Wood; flour brand from 1896.","s":W+"King_Arthur_Baking"},
{"n":"Molino Dallagiovanna","c":"Italy","seg":"Heritage manufactory","kf":"Neapolitan flour","d":"Italian mill kept from old data.","s":"knowledge"}]
out={"kinds":k,"brands":br,"traditions":[],"notes":"Petra, Cuoco/Nuvola protein figures and Nuvola (non-Super) left out: not confirmed on retrieved pages. Caputo official site returned 403, so Caputo flours are attested from a retailer page plus old data. Italian Tipo and French T numbers are in dt/names. Atta and semolina keep old models."}
json.dump(out,open('work/J5/shelves/03_00.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/J5/shelves/03_00.tmp','work/J5/shelves/03_00.json')
