import json,os
W='https://en.wikipedia.org/wiki/'
I='https://www.indoasiangroceries.com.au/category/rice'
def A(n,d,s,dt="",y="",v=None,a="",mk=""):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v:x["v"]=v
    return x
k=[
{"n":"Basmati rice","a":"","d":"The long, aromatic, aged grain of the basmati group, GI-registered in India since 2016.","s":I,"t":["Brown","Parboiled (steam)","White"],
 "x":[A("Dehraduni basmati","Traditional basmati group from Dehradun, valued for a popcorn aroma.",W+"Basmati","Dehradun, Tapovan and Tehri groups"),
 A("Pusa Basmati 1121","Very long-grain Indian basmati, up to 9 mm, fluffy and aromatic.",W+"Pusa_Basmati_1121","IARI, released 2003 as Pusa 1121; renamed 2008","2003"),
 A("Super Kernel basmati","Pakistani basmati variety.",W+"Basmati")],
 "m":[["Daawat Traditional Basmati","Daawat"],["India Gate Basmati Rice Classic","India Gate"]]},
{"n":"Jasmine rice","a":"","d":"The long, soft, fragrant grain of the jasmine group.","s":I,"t":["White","Brown"],
 "x":[A("Thai Hom Mali (Khao Dawk Mali 105)","Thailand's jasmine rice, a slender white grain with a pandan-like fragrance.",W+"Jasmine_rice","grown mainly in the Northeast; Surin, Buriram and Sisaket regarded as best","")],
 "m":[["Thai Hom Mali",""]]},
{"n":"Long-grain rice","a":"","d":"Slender non-aromatic rice grains that stay separate when cooked.","s":I,"t":["White","Brown","Parboiled"],"m":[["Ben's Original Long Grain","Ben's Original"]]},
{"n":"Medium- and short-grain rice","a":"sushi rice","d":"Rounder rice that cooks tender and clings, including Japanese varieties and the Indian table rices.","s":I,
 "x":[A("Koshihikari","Japan's most widely grown premium variety, bred in 1956 from Nourin No.1 and No.22.",W+"Koshihikari","Fukui, 1956","1956"),
 A("Akitakomachi","Non-glutinous Japanese table rice.",W+"List_of_rice_cultivars"),
 A("Hitomebore","Non-glutinous Japanese table rice.",W+"List_of_rice_cultivars"),
 A("Tsuyahime","Non-glutinous Japanese table rice.",W+"List_of_rice_cultivars"),
 A("Calrose","California medium-grain japonica, soft and clinging, released 1948.",W+"Calrose_rice","Biggs, California; Caloro x Calady","1948"),
 A("Sona Masoori","Indian table rice from Andhra Pradesh, also called Bangaru Theegalu.",W+"List_of_rice_cultivars"),
 A("Samba","Indian (Tamil Nadu) and Sri Lankan rice.",W+"List_of_rice_cultivars"),
 A("Gobindobhog","Aromatic rice of West Bengal.",W+"List_of_rice_cultivars")],
 "m":[["Baby basmati (Kala Jeera)",""]]},
{"n":"Risotto rice","a":"","d":"Rice sold for risotto because it gives up starch as it cooks.","s":"https://www.foodstories.shop/shop/everyday-staples/rice/",
 "x":[A("Carnaroli","Longer, firmer Italian risotto rice, crossed in 1945 from Vialone and Lencino; 'king of rices'.",W+"Carnaroli","Pavia, Novara, Vercelli","1945"),
 A("Arborio","Medium-grain rice from the Po Valley; firm, creamy and chewy.",W+"Arborio_rice","Arborio, Piedmont"),
 A("Riso Nano Vialone Veronese IGP","Medium-grain Veronese rice with a pearly core, PGI since 1996.",W+"Vialone_Nano","Bassa Veronese, 24 municipalities","1996")],
 "m":[["Acquerello","Acquerello"]]},
{"n":"Paella rice","a":"","d":"Rice sold for paella because it absorbs a lot of stock and stays whole.","s":I,
 "x":[A("Bomba","Short pearly Spanish rice that absorbs two to three times its volume of liquid without bursting.",W+"Bomba_rice","Valencia, Murcia"),
 A("Calasparra DOP","Murcian rice with a Denominación de Origen since 1986; slow maturing, absorbs liquid well.",W+"Calasparra_rice","Murcia, terrace irrigation","1986")]},
{"n":"Sticky rice","a":"glutinous rice","d":"Rice that turns sticky and translucent when cooked, of any bran colour.","s":I,"t":["White","Black (purple)"],
 "x":[A("Khao niao (Thai/Lao sticky rice)","Glutinous rice of Thailand and Laos, steamed and served in a basket.",W+"Glutinous_rice"),
 A("Mochigome","Japanese glutinous rice used for sekihan and mochi.",W+"Glutinous_rice")],
 "m":[["Black Thai rice (purple sticky)",""]]},
{"n":"Red and black rice","a":"forbidden rice","d":"Non-glutinous rice with a red or black bran layer left on.","s":"https://www.yami.com/us/en/collections/black-rice",
 "x":[A("Black rice (forbidden rice)","Anthocyanin-rich bran turns it deep purple when cooked; 'forbidden rice' is a marketing name.",W+"Black_rice","includes Thai jasmine black rice, Chak-hao (Manipur), kavuni arisi (Tamil Nadu)"),
 A("Camargue red rice","Newer red rice from the wetlands of the Camargue, France.",W+"Red_rice"),
 A("Bhutanese red rice","Medium-grain red rice from Bhutan.",W+"Red_rice")],
 "m":[["Thai red rice",""]]},
{"n":"Flattened rice","a":"poha","d":"Rice grains steamed or parboiled and rolled flat.","s":I,"t":["Thick","Thin"],
 "x":[A("Poha","Flattened rice of India, also aval, avalakki, chiura.",W+"Flattened_rice")]}]
br=[{"n":n,"c":c,"seg":"Mainstream","kf":"rice","d":d,"s":"knowledge"} for n,c,d in [("Tilda","United Kingdom","Basmati and aromatic rice brand."),("Daawat","India","Indian basmati brand."),("India Gate","India","Indian basmati brand."),("Ben's Original","United States","Rice brand formerly Uncle Ben's.")]]
out={"kinds":k,"brands":br,"traditions":[],"notes":"Toku-A grade, Uonuma, Yumepirika, Traditional/Taraori basmati, Gobindobhog details and Acquerello versions not confirmed on retrieved pages so left out or kept thin. Brown/parboiled as t."}
json.dump(out,open('work/J5/shelves/01_00.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/J5/shelves/01_00.tmp','work/J5/shelves/01_00.json')
