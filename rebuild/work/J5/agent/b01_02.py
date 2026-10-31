import json,os
W='https://en.wikipedia.org/wiki/'
def A(n,d,s,dt="",y="",mk="",a="",v=None):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"dt":dt}
    if v:x["v"]=v
    return x
T='https://tomatostoreus.com/collections/noodle'
IN=W+'List_of_instant_noodle_brands'
k=[
{"n":"Ramen noodles","a":"chukamen","d":"Alkaline wheat noodles made with kansui, fresh or dried.","s":T,"t":["Fresh","Dried","Thick","Thin","Straight","Wrinkled"]},
{"n":"Instant noodles","a":"","d":"Pre-cooked, dried noodle blocks or cups made ready with boiling water; first sold in 1958.","s":W+"Instant_noodles","t":["Block (packet)","Cup","Fried","Air-dried"],
 "x":[A("Chikin Ramen","The first modern instant noodle, launched by Momofuku Ando of Nissin on 25 August 1958 at 35 yen.",W+"Instant_noodles","","1958","Nissin Foods"),
 A("Cup Noodles","The first cup noodle, released by Nissin in 1971 after Ando saw Americans break blocks into cups.",W+"Instant_noodles","","1971","Nissin Foods"),
 A("Shin Ramyun","Nongshim's Korean instant noodle.",IN,mk="Nongshim"),
 A("Indomie Mi Goreng","Indofood's Indonesian instant fried noodle.",IN,mk="Indofood"),
 A("MAMA","Thai instant noodle by Thai President Foods.",IN,mk="Thai President Foods"),
 A("Maggi","Nestlé instant noodle popular in South Asia.",IN,mk="Nestlé"),
 A("Buldak Bokkeum Myun","Samyang's hot chicken instant noodle.",IN,mk="Samyang Foods")]},
{"n":"Udon","a":"","d":"Thick Japanese wheat noodles.","s":T,"m":[],
 "x":[A("Sanuki udon","Thick, rather stiff noodles from Kagawa Prefecture.",W+"Udon","Kagawa"),
 A("Inaniwa udon","Thin udon from Akita Prefecture.",W+"Udon","Akita"),
 A("Kishimen","Flat udon with wavy edges from Nagoya.",W+"Udon","Nagoya"),
 A("Ise udon","Soft noodle served with sweet soy sauce, from Ise, Mie.",W+"Udon"),
 A("Goto udon","Thin firm noodle coated in camellia oil, from the Goto Islands.",W+"Udon")]},
{"n":"Soba","a":"","d":"Japanese noodles made with buckwheat flour; the share of buckwheat varies by brand.","s":T,
 "x":[A("Juwari soba","100% buckwheat soba (also towari).",W+"Soba","100% buckwheat"),
 A("Ni-hachi soba","'Two-eight' soba: 80% buckwheat and 20% wheat.",W+"Soba","80:20"),
 A("Izumo soba","Soba named after Izumo in Shimane Prefecture.",W+"Soba"),
 A("Shinshu soba","Nagano soba; the name needs 40% or more buckwheat flour.",W+"Soba","40%+ buckwheat")],
 "m":[["Izumo soba",""]]},
{"n":"Somen","a":"","d":"Very thin Japanese wheat noodles, under 1.3 mm, stretched with oil and air-dried.","s":W+"S%C5%8Dmen",
 "x":[A("Miwa somen","Somen said to have evolved first in Miwa, Sakurai, Nara in the Heian period.",W+"S%C5%8Dmen","Nara")]},
{"n":"Chinese wheat and egg noodles","a":"","d":"Chinese wheat noodles, hand-pulled, knife-cut, or made with egg or lye water.","s":W+"Chinese_noodles","t":["Lamian (hand-pulled)","Knife-cut (daoxiao)","Egg noodles","Wonton noodles","Lo mein","Yi mein"],
 "x":[A("Lamian","Hand-pulled wheat noodles from which ramen was derived.",W+"Chinese_noodles"),
 A("Knife-cut noodles","Short flat noodles shaved off a block of dough with a knife.",W+"Chinese_noodles"),
 A("Wonton noodles","Fresh Cantonese egg noodles served with wontons and gai-lan.",W+"Wonton_noodles")]},
{"n":"Rice noodles","a":"","d":"Noodles made from rice, from thin vermicelli to wide fresh sheets.","s":W+"Rice_noodles","t":["Fresh","Dried"],
 "x":[A("Rice vermicelli","Thin rice noodles, also rice sticks.",W+"Rice_noodles"),
 A("Shahe fen (chow fun, ho fun)","Wide Chinese flat rice noodles.",W+"Rice_noodles"),
 A("Banh pho","Thick fresh rice noodle for pho soups.",W+"Rice_noodles"),
 A("Sen lek","Narrow flat Thai rice noodle used in pad thai and soups.",W+"Rice_noodles")]},
{"n":"Glass noodles","a":"harusame","d":"Transparent noodles made from mung bean, potato or a similar pure starch.","s":"https://erewhon.com/product/163121000/harusame-mung-bean-pasta","t":["Mung bean","Sweet potato","Potato"],
 "x":[A("Longkou vermicelli","Shandong glass noodles named for the port of Longkou.",W+"Glass_noodles","Zhangxing, Shandong"),
 A("Dangmyeon","Korean glass noodles, usually sweet potato starch, used in japchae.",W+"Glass_noodles"),
 A("Harusame","Japanese 'spring rain' glass noodles, usually potato starch.",W+"Glass_noodles")],
 "m":[["Eden Foods Harusame Mung Bean Pasta","Eden Foods"]]},
{"n":"Konjac noodles","a":"shirataki","d":"Noodles of konjac glucomannan, mostly water with few digestible carbohydrates.","s":W+"Shirataki_noodles"}]
B=lambda n,c,f,d,s=IN:{"n":n,"c":c,"seg":"Mainstream","kf":f,"d":d,"s":s}
br=[B("Nissin Foods","Japan","instant noodles","Maker of Chikin Ramen and Cup Noodles.",W+"Instant_noodles"),B("Nongshim","South Korea","Shin Ramyun","Korean instant noodle maker."),B("Indofood","Indonesia","Indomie","Maker of Indomie Mi Goreng."),B("Thai President Foods","Thailand","MAMA","Thai instant noodle maker."),B("Samyang Foods","South Korea","Buldak","Korean hot-chicken noodle maker.")]
out={"kinds":k,"brands":br,"traditions":[],"notes":"Mizusawa udon, Togakushi soba, Ibonoito somen, Guilin rice noodles and ramen-rater test winners not found on retrieved pages so omitted. Konjac noodles kept as a new kind from Wikipedia."}
json.dump(out,open('work/J5/shelves/01_02.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/J5/shelves/01_02.tmp','work/J5/shelves/01_02.json')
