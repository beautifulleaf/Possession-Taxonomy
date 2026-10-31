import json,os
W='https://en.wikipedia.org/wiki/'
def A(n,d,s,dt="",a=""):return {"n":n,"a":a,"d":d,"mk":"","y":"","s":s,"dt":dt}
k=[
{"n":"White sugar","a":"granulated sugar","d":"Refined white cane or beet sugar crystals; fine caster and ordinary granulated sugar both belong here.","s":"https://www.billingtons.co.uk/our-products","t":["Granulated","Caster"]},
{"n":"Brown sugar","a":"","d":"Unrefined and soft brown cane sugars that differ by crystal size, moisture and molasses content.","t":["Demerara sugar","Muscovado sugar","Soft brown sugar","Turbinado"],"s":W+"Brown_sugar",
 "m":[["Billington's Demerara Sugar","Billington's"],["Billington's Dark Muscovado Sugar","Billington's"]]},
{"n":"Icing sugar","a":"powdered sugar","d":"White sugar milled to a fine powder, with 2-5% anti-caking agent.","s":"https://www.billingtons.co.uk/our-products"},
{"n":"Jaggery","a":"gur · panela · piloncillo","d":"Unrefined cane juice boiled down and set in blocks or cones.","s":"https://www.heb.com/product-detail/goya-piloncillo-panela-brown-sugar-cane/128989","t":["Cane","Date palm","Palm sap"],
 "x":[A("Gur (jaggery)","South Asian non-centrifugal cane sugar, golden to dark brown, from North India, Pakistan and Bangladesh.",W+"Jaggery","also gud, gul"),
 A("Panela","Latin American unrefined whole cane sugar in moulded blocks; Colombia is the largest producer.",W+"Panela","Also papelón (Venezuela), chancaca (Bolivia, Chile, Peru)"),
 A("Piloncillo","Mexican panela, cone-shaped, in blanco (light) and oscuro (dark) versions.",W+"Panela"),
 A("Rapadura","Portuguese-language name of panela in Brazil, Argentina and other countries.",W+"Panela"),
 A("Kokuto","Japanese 'black sugar'; the Japanese term for jaggery.",W+"Jaggery")],
 "m":[["Piloncillo (panela)",""]]},
{"n":"Palm and coconut sugar","a":"","d":"Sugar boiled from palm sap, sold as blocks, cakes, crystals or paste.","s":W+"Palm_sugar","t":["Coconut blossom sugar","Date palm","Palmyra","Sugar palm (aren)"],
 "x":[A("Gula melaka","Malaysian palm sugar from coconut flower buds, set in bamboo-tube cylinders.",W+"Palm_sugar","named for Malacca; used in sago pudding, chendol"),
 A("Coconut sugar","Sap of the coconut palm flower stem heated to syrup, crystals or blocks.",W+"Coconut_sugar","mild brown-sugar taste")]},
{"n":"Sugar substitutes","a":"sweeteners","d":"Low- or no-calorie sweeteners such as stevia, erythritol, sucralose and aspartame.","s":W+"Sugar_substitute","t":["Stevia","Erythritol","Sucralose","Aspartame","Saccharin"],
 "m":[["Truvia","Cargill"],["Splenda",""],["Sweet'N Low",""],["Equal",""]]}]
br=[{"n":"Billington's","c":"United Kingdom","seg":"Premium","kf":"unrefined cane sugar","d":"UK unrefined and brown sugar brand kept from old data.","s":"knowledge"}]
out={"kinds":k,"brands":br,"traditions":[],"notes":"Wasanbon, Canderel not found on retrieved pages so omitted. Sugar substitute makers beyond Truvia (Cargill) were not stated on the page, so left blank. Brown sugar kind now sourced to Wikipedia."}
json.dump(out,open('work/J5/shelves/03_02.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/J5/shelves/03_02.tmp','work/J5/shelves/03_02.json')
