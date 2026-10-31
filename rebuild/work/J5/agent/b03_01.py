import json,os
W='https://en.wikipedia.org/wiki/'
SM='https://www.shipton-mill.com/collections/all-flour'
KE='https://www.kesargrocery.com/speciality-flour/?page=2&sort=title'
PG='https://punjabigroceries.com/collections/atta-flour'
G='https://theglutenfreeaustrian.com/the-best-gluten-free-flour-blends-for-baking-and-how-i-use-them/'
k=[
{"n":"Rye flour","a":"","d":"Flour milled from rye, mostly mixed with wheat because rye lacks enough gluten.","s":SM,"t":["Light","Dark","Wholemeal"]},
{"n":"Rice flour","a":"","d":"Flour milled from rice, brown or white, or glutinous.","s":KE,"t":["White","Brown","Glutinous (mochiko)"]},
{"n":"Chickpea flour","a":"besan · gram flour","d":"Flour milled from chickpeas, used in Indian cooking and Ligurian farinata.","s":KE},
{"n":"Maize flour","a":"makki atta","d":"Flour milled from whole maize; cornflour starch is not this kind.","s":PG},
{"n":"Masa harina","a":"","d":"Dried flour of nixtamalised maize dough, used for tortillas and tamales.","s":W+"History_of_the_tortilla","m":[["Maseca","Gruma"],["Minsa","Minsa"]]},
{"n":"Buckwheat flour","a":"","d":"Flour milled from buckwheat, used in soba, blini and Breton crêpes.","s":KE},
{"n":"Millet flour","a":"bajra","d":"Flour milled from pearl or other millets.","s":PG},
{"n":"Urad and moong flour","a":"","d":"Flour milled from black gram or mung beans.","s":KE,"t":["Urad","Moong"]},
{"n":"Cornflour and starches","a":"cornstarch","d":"Pure starches for thickening: cornflour (cornstarch), arrowroot, potato and tapioca starch.","s":W+"Corn_starch","t":["Cornflour (cornstarch)","Arrowroot","Potato starch","Tapioca starch","Wheaten cornflour (Australia)"]},
{"n":"Gluten-free flour blends","a":"","d":"Ready-mixed gluten-free flours, either all-purpose 1-to-1 blends or yeast-dough blends.","s":G,"t":["1-to-1 baking blends","Yeast-dough blends"],
 "m":[["Gluten Free 1-to-1 Baking Flour","Bob's Red Mill"],["Measure for Measure","King Arthur"],["Fioreglut","Caputo"],["Cup4Cup","Cup4Cup"]]}]
br=[{"n":"Gruma","c":"Mexico","f":"1949","seg":"Mainstream","kf":"Maseca masa harina","d":"Maker of Maseca, the first commercial masa harina in Mexico.","s":W+"History_of_the_tortilla"}]
out={"kinds":k,"brands":br,"traditions":[],"notes":"Doves Farm not found on a retrieved page so omitted. Urad and moong merged. Millet flour and urad/moong definitions kept from old data (Wikipedia Flour page does not cover them). Mochiko as t of rice flour from Mochi page."}
json.dump(out,open('work/J5/shelves/03_01.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/J5/shelves/03_01.tmp','work/J5/shelves/03_01.json')
