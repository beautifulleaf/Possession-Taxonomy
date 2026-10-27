import json,os
W='https://en.wikipedia.org/wiki/'
def x(n,d,s,y='',v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":"","y":y,"s":W+s,"v":v or [],"dt":dt}
def v(n,d,y=''): return {"n":n,"mk":"","y":y,"d":d}
kinds=[
{"n":"Tektite","d":"Gravel-sized natural glass thrown out by a meteorite impact, collected by strewn field.","t":["splash form","button","Muong Nong layered type"],"s":"https://www.fossilera.com/meteorites-for-sale",
 "x":[
 x("Moldavite","Green tektite from the Central European field (Nördlinger Ries impact); the most collected and most faked tektite.","Moldavite","about 15 million years",[v("Southern Bohemia, Czech Republic","main source"),v("Moravia","browner, heavier pieces")],"weight · colour · surface etching · lechatelierite inclusions · cut gem or raw","Czech tektite"),
 x("Indochinite","Dark, almost black tektite of the Australasian field from Indochina.","Indochinite","about 700,000 years",[v("Layered Muong-Nong type","29.0 kg example on record")],"weight · shape · size"),
 x("Australite","Australian tektite of the Australasian field, known for flanged buttons.","Australite","610,000–750,000 years",[v("Flanged button","the best-known and rare form"),v("Port Campbell, Victoria","well-preserved finds")],"form: sphere · oval · boat · dumbbell · teardrop · flanged button · disc"),
 x("Philippinite","Black Philippine tektite of the Australasian field, also called rizalite.","Philippinite","about 710,000 years",[v("Rizal province","rediscovered 1926 at Novaliches","1926")],"splash form: sphere · teardrop · dumbbell","rizalite"),
 x("Bediasite","Black Texan tektite from the North American field (Chesapeake Bay impact).","Bediasite","about 34 million years",[v("Bedias area, eastern Texas","largest specimen about 200 g")],"weight · shape"),
 x("Georgiaite","Rare olive-green tektite found only in central and eastern Georgia.","Georgiaite","over 35 million years",[v("Dodge and Bleckley counties","discovered 1938","1938")],"weight · translucence")]},
{"n":"Impact glass","a":"desert glass","d":"Natural glass melted at a meteorite impact site, not scattered as tektites.","s":W+"Impactite",
 "x":[
 x("Libyan Desert Glass","Pale yellow silica glass from the Great Sand Sea of Libya and Egypt, used in a Tutankhamun scarab.","Libyan_desert_glass","about 29 million years",[v("Great Sand Sea","26 kg specimen shown in Paris 2018","2018")],"weight · transparency · polished cabochon or raw","Great Sand Sea glass"),
 x("Darwin glass","Green, white or black impact glass from western Tasmania around Darwin Crater.","Darwin_glass","about 816,000 years",[v("Strewn field south of Queenstown","410 km²; pieces up to 10 cm")],"type 1 · type 2 · weight"),
 x("Wabar glass","Black impact glass pellets from the Wabar craters in the Saudi Rub' al Khali.","Wabar_craters","under 250 years (thermoluminescence)",[v("Black glass","about 90% sand and 10% meteoric iron and nickel")],"weight · black glass or white Insta-Rock")],
 "m":[["Libyan Desert Glass",""]]},
{"n":"Impactite and shatter cone","a":"impact breccia","d":"Rock shocked, melted or brecciated by an impact, including suevite and cone-patterned shatter cones.","t":["suevite","impact melt rock","shocked quartz"],"s":W+"Impactite",
 "x":[
 x("Suevite","Impact breccia holding glass and rock fragments; named from the Nördlinger Ries.","Suevite","named 1919",[v("Nördlinger Ries, Germany","type locality"),v("Rochechouart","greenish suevite")],"clast size · glass content"),
 x("Shatter cone","Conical striated rock fracture formed under impact shock; collected as slabs and hand specimens.","Shatter_cone","",[v("Steinheim Basin, Germany","type locality"),v("Slate Islands, Ontario","largest registered cones, over 9 m")],"limestone horsetail striae · size")]}]
json.dump({"kinds":kinds,"brands":[],"traditions":[],"notes":"Old Tektite and impactite kind split into three. Moldavite fakes, Muong Nong, Atacama glass, Sudbury and Kentland localities not confirmed on retrieved pages so omitted. No dealer entries (IMCA entered in shelf 03_00)."},open('work/F6/shelves/03_01.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/F6/shelves/03_01.tmp','work/F6/shelves/03_01.json')
