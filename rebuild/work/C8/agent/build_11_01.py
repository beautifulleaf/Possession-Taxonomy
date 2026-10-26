import json, os
W="https://en.wikipedia.org/wiki/"
L18="https://lygte-info.dk/review/batteries2012/"
def A(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v,"dt":dt}
x=[
 A("Panasonic NCR18650B","NCR18650B · 3400 mAh green Panasonic","High-capacity 18650 cell rated 3400 mAh, the long-time capacity benchmark for torches and laptop packs.","Panasonic","",L18+"Panasonic%20NCR18650B%203400mAh%20(Green)%20UK.html",[],"18650 · flat top or third-party protected button top · green wrap"),
 A("Samsung 25R","INR18650-25R","Unprotected 18650 power cell rated 2500 mAh and 20 A continuous discharge, a staple of power tools and vaping.","Samsung SDI","","https://www.18650batterystore.com/products/samsung-25r-18650",[],"18650 · 18.4 × 65 mm · flat top · 20 A"),
 A("Samsung 35E","INR18650-35E","Unprotected 18650 energy cell, 3350 mAh minimum with 8 A continuous discharge, used in e-bike and torch packs.","Samsung SDI","","https://www.18650batterystore.com/products/samsung-35e-18650-3500mah-8a-battery",[],"18650 · flat top · 8 A"),
 A("Samsung 50E","INR21700-50E","Unprotected 21700 energy cell, 4900 mAh minimum with 9.8 A continuous discharge.","Samsung SDI","","https://www.18650batterystore.com/21700-p/samsung-50e.htm",[],"21700 · 21.25 × 70.8 mm · flat top · 9.8 A"),
 A("LG HG2","INR18650HG2 · 'brown' cell","High-drain 18650 cell rated 3000 mAh and 20 A continuous, known by its brown wrap.","LG Energy Solution","2014",L18+"LG%2018650%20HG2%203000mAh%20(Brown)%20UK.html",[],"18650 · flat top · brown wrap · 20 A"),
 A("Murata VTC6","US18650VTC6 · Sony VTC6","18650 power cell from the former Sony line, 3000 mAh minimum and 15 A continuous discharge.","Murata","","https://www.18650batterystore.com/Sony-18650-p/sony-vtc6.htm",
   [{"n":"US18650VTC6M","mk":"Murata","y":"","d":"variant listed by European retailers"}],"18650 · flat top · unprotected · 15 A (30 A with 80 °C cut-off)"),
 A("Molicel P28A","INR-18650-P28A","High-power 18650 cell rated 2800 mAh and 35 A continuous discharge.","Molicel","","https://www.racedayquads.com/collections/all/products/molicel-p28a-2800mah-18650-li-ion-battery-2-pack",[],"18650 · flat top · 35 A"),
 A("Molicel P42A","INR-21700-P42A","High-power 21700 cell, 4200 mAh typical and 45 A continuous discharge.","Molicel","","https://www.18650batterystore.com/21700-p/molicel-p42a.htm",[],"21700 · flat top · 45 A"),
 A("Molicel P45B","INR21700-P45B","High-power 21700 cell, 4500 mAh rated with 45 A continuous discharge.","Molicel","","https://www.akkuteile.de/en/lithium-ionen-battery/size-21700/molicel/molicel-inr21700-p45b-4500mah-li-ion-battery-3-6v-3-7v_100852_3119",[],"21700 · 21.4 × 70 mm · 45 A continuous, about 90 A pulse"),
]
kind={"n":"Lithium-ion cell","a":"18650 battery · 21700 battery · 18650 cell · 21700 cell · loose Li-ion cell",
 "d":"Loose rechargeable cylindrical lithium-ion cell, named by size in millimetres (diameter, length), for torches, packs and devices.",
 "t":["18650","21700","14500","26650"],"s":W+"18650_battery","x":x,
 "m":[["Samsung INR21700-58E","Samsung SDI"],["EVE INR18650-30P","EVE Energy"],["EVE INR18650-33VA","EVE Energy"],["EVE INR21700-50PL","EVE Energy"],["BAK N21700CG","BAK"],["BAK N21700CH-58E","BAK"],["DMEGC INR18650-25P","DMEGC"],["Tenpower INR18650-35HE","Tenpower"]]}
def B(n,c,f,seg,d,lines,eras,sig,rel,s): return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines,"eras":eras,"sig":sig,"sc":[],"rel":rel,"s":s}
brands=[
 B("Panasonic","Japan","1918","Electronics group; cell maker via Panasonic Energy","Japanese electronics group whose Panasonic Energy subsidiary makes cylindrical lithium-ion cells, including for Tesla.",["Panasonic Energy"],["Sanyo merged in, 2009","Tesla Gigafactory partner from 2014"],["Panasonic NCR18650B"],["Samsung SDI","LG Energy Solution"],W+"Panasonic"),
 B("Samsung SDI","South Korea","1970","Battery and materials maker","Samsung Group battery maker producing cylindrical lithium-ion cells for devices, vehicles and storage.",[],["Founded as Samsung-NEC, 1970","Cylindrical lithium-ion cells by 1998"],["Samsung 25R","Samsung 35E","Samsung 50E"],["LG Energy Solution","Panasonic"],W+"Samsung_SDI"),
 B("LG Energy Solution","South Korea","2020","Battery maker","Korean battery maker spun off from LG Chem in 2020; its cells were long sold under the LG Chem name.",[],["LG Chem battery business, 1992–2020","LG Energy Solution, 2020–"],["LG HG2"],["Samsung SDI","Panasonic"],W+"LG_Energy_Solution"),
 B("Murata","Japan","1944","Electronic components; cell maker","Japanese components maker that bought Sony's battery business and continues its VTC cells.",[],["Sony battery business acquired after 2016 agreement"],["Murata VTC6"],["Samsung SDI","Molicel"],W+"Murata_Manufacturing"),
 B("Molicel","Taiwan","1998","High-power cell maker","Brand of E-One Moli Energy, a Taiwanese maker of high-power lithium-ion cells with Canadian Moli Energy roots.",[],["Moli Energy, Canada, 1977–1998","E-One Moli Energy, 1998–"],["Molicel P28A","Molicel P42A","Molicel P45B"],["Samsung SDI","Murata"],W+"E-One_Moli_Energy"),
 B("EVE Energy","China","2001","Battery maker","Chinese battery maker from Huizhou producing cylindrical, prismatic and pouch lithium-ion cells.",[],[],[],["Molicel"],W+"EVE_Energy"),
]
out={"kinds":[kind],"brands":brands,"traditions":[],"notes":"Merged old 18650 battery (k145) and 21700 battery (k146) into one kind with format types. Nine archetype cells from original makers (Panasonic, Samsung SDI, LG, Murata, Molicel), each sourced to a retrieved product/test page. Unarchetyped OEM models (EVE, BAK, DMEGC, Tenpower, Samsung 58E) kept in m. Left out: Samsung 30Q/40T/50S, Murata VTC5A, LG M50LT, Panasonic NCR18650GA and 14500/26650 named cells (no retrieved page or only search snippets); BAK/DMEGC/Tenpower brand entries (no page retrieved); rewrapped/relabelled cells (e.g. Epoch-wrapped Molicel) excluded as rewrap noise. nkon.nl blocked fetches (403)."}
p="work/C8/shelves/11_01.json"; t=p+".tmp"
json.dump(out,open(t,"w"),indent=1,ensure_ascii=False); os.replace(t,p)
