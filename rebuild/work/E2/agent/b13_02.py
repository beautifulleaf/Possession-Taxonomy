import json, os
def X(n,d,mk,y,s,v=(),dt='',a=''): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=a1,mk=b,y=c,d=e) for a1,b,c,e in v],"dt":dt}
PS='https://www.popsci.com/gear/best-boxing-gloves/'; LK='https://lowkickmma.com/best-boxing-headgear'; BR='https://bleacherreport.com/articles/1286577-breaking-down-different-brands-of-boxing-gloves-worn-by-the-pros'
kinds=[
{"n":"Boxing glove","a":"","d":"Padded glove worn for boxing sparring, bagwork or competition.",
 "t":["lace-up","hook-and-loop","bag glove","sparring glove","competition glove","Muay Thai glove","MMA glove (open-finger)","horsehair or foam padding","8–20 oz"],
 "s":"https://ebay.com/t/Boxing-Gloves/30102/bn_1943751",
 "x":[X("Cleto Reyes glove","Handmade Mexican 'puncher's glove' with less knuckle padding, first used in a title bout in 1945.","Cleto Reyes","1945","https://www.mmawarehouse.com/products/cleto-reyes-safetec-boxing-gloves",
        [("Traditional Lace","Cleto Reyes","",""),("Professional","Cleto Reyes","","fight model"),("Safetec","Cleto Reyes","","lace-up, moulded Safetec padding"),("High Precision","Cleto Reyes","",""),("Hook and Loop Training","Cleto Reyes","",""),("Hero","Cleto Reyes","","double-loop closure")],"latex foam, horsehair or Safetec padding · lace or hook-and-loop · colours"),
      X("Winning MS-600","Japanese 'Professional Type' glove known for maximum hand protection ('pillows').","Winning","","https://www.ebay.de/itm/186429899280",[("MS-600 lace-up","Winning","","16 oz, cowhide")],"lace-up or hook-and-loop · 8–16 oz"),
      X("Twins Special glove","Thai-made leather glove with a short cuff and good weight balance; a classic, widely respected design.","Twins Special","",PS,[],"10–16 oz"),
      X("Hayabusa T3","Glove with a semi-rigid wrist splint, dual straps and five foam layers, noted for wrist support.","Hayabusa","",PS,[],"10–18 oz")],
 "m":[["Prostyle 2","Everlast"],["Elite ProStyle Training","Everlast"],["Core 2","Everlast"],["Protex","Everlast"],["Spark Training","Everlast"],["Titan Hybrid","Everlast"],["IMF Tech","Ringside"],["Apex Flash","Ringside"],["BGV1","Fairtex"],["Essential Gel Boxing Gloves","Sanabul"],["Classic","Venum"],["Contender","Venum"],["Elite Boxing","Venum"],["Hybrid 80","adidas"]]},
{"n":"Punch bag","a":"punching bag · heavy bag","d":"Heavy hanging or free-standing bag struck in boxing and fitness training.",
 "t":["heavy (hanging)","free-standing","speed ball","double-end","Muay Thai (long) bag"],
 "s":"https://www.dickssportinggoods.com/f/heavy-bags-boxing-collection",
 "x":[X("Everlast Powercore free-standing bag","Free-standing heavy bag on a water- or sand-filled base, height-adjustable, with a NevaTear synthetic-leather cover.","Everlast","","https://ie.fitshop.com/everlast-free-standing-heavy-bag-powercore-ev-p00001266",[],"height 137–165 cm")],
 "m":[["Heritage Heavy Bag","Ringside"],["Muay Thai Heavy Bag","Ringside"],["Powerhide Soft Filled Bag","Ringside"]]},
{"n":"Boxing headguard","a":"headgear · head guard","d":"Padded helmet that protects the head in boxing sparring and amateur competition.",
 "t":["open face","cheek protector (Mexican style)","full face with nose bar (face saver)","competition-approved"],
 "s":LK,
 "m":[["Classic Training Headgear","Cleto Reyes"],["Protective Headgear 2","Cleto Reyes"],["Deluxe Face Saver Boxing Headgear","Ringside"],["Competition-Like Headgear with Cheeks","Ringside"],["Leather Sparring Headgear","Title Boxing"],["USA Boxing Amateur Competition Headgear","Title Boxing"],["Adjustable T3 Headgear","Hayabusa"],["HGL T1W","RDX"],["Elite Headgear","Venum"],["Core Series Headgear","Sanabul"]]},
{"n":"Hand wraps","a":"handwraps","d":"Long cotton or semi-elastic strips wound round the hands and wrists under boxing gloves.",
 "t":["cotton","semi-elastic","120 in","170 in","gel or quick wraps"],
 "s":"https://en.wikipedia.org/wiki/Boxing_glove"},
{"n":"Focus mitts","a":"punch mitts · pads","d":"Padded hand-held targets worn by a coach to feed punches and combinations.",
 "t":["focus mitt","curved mitt","Thai pads","kick shield","body shield"],
 "s":"https://en.wikipedia.org/wiki/Focus_mitt"},
]
K='knowledge'
brands=[
 {"n":"Everlast","c":"United States","f":"1910","seg":"Mainstream","kf":"boxing equipment","d":"Bronx-founded boxing brand, owned by Frasers Group since 2007, making gloves, bags and protection.","lines":["Pro Style","Powercore"],"eras":["Jacob Golomb, from 1910"],"sig":["Everlast Powercore free-standing bag"],"sc":["boxing"],"rel":[],"s":"https://en.wikipedia.org/wiki/Everlast_(brand)"},
 {"n":"Cleto Reyes","c":"Mexico","f":"1945","seg":"Heritage manufactory","kf":"handmade boxing gloves","d":"Mexican maker of handmade boxing gloves, founded by Cleto Reyes.","lines":["Traditional","Safetec","Hero"],"eras":["Cleto Reyes, from 1945","Alberto Reyes, from about 1970"],"sig":["Cleto Reyes glove"],"sc":["professional boxing"],"rel":[],"s":"https://wbcboxing.com/en/cleto-reyes-hand-in-glove-excellence/"},
 {"n":"Winning","c":"Japan","f":"","seg":"Professional & flagship","kf":"boxing gloves","d":"Japanese glove maker known for highly protective gloves used by professionals.","lines":["MS"],"eras":[],"sig":["Winning MS-600"],"sc":["professional boxing"],"rel":[],"s":BR},
 {"n":"Twins Special","c":"Thailand","f":"","seg":"Premium","kf":"Muay Thai and boxing gloves","d":"Thai maker of premium leather gloves and pads.","lines":[],"eras":[],"sig":["Twins Special glove"],"sc":["Muay Thai","boxing"],"rel":[],"s":PS},
 {"n":"Hayabusa","c":"Canada","f":"","seg":"Premium","kf":"combat sports gear","d":"Combat-sports brand known for the T3 glove's wrist-splint design.","lines":["T3"],"eras":[],"sig":["Hayabusa T3"],"sc":["boxing","MMA"],"rel":[],"s":K},
 {"n":"Grant","c":"","f":"","seg":"Professional & flagship","kf":"boxing gloves","d":"Glove maker praised for wrist support, worn by many professional champions.","lines":[],"eras":[],"sig":[],"sc":["professional boxing"],"rel":[],"s":BR},
 {"n":"Rival","c":"","f":"","seg":"Premium","kf":"boxing gloves","d":"Glove brand popular in Canada, blending padding and punching power.","lines":[],"eras":[],"sig":[],"sc":["boxing"],"rel":[],"s":BR},
 {"n":"Ringside","c":"United States","f":"","seg":"Mainstream","kf":"boxing equipment","d":"American boxing-equipment brand selling gloves, headgear and bags.","lines":[],"eras":[],"sig":[],"sc":["boxing"],"rel":[],"s":K},
]
notes=("Kept Boxing glove and Punch bag; added Boxing headguard, Hand wraps and Focus mitts (Thai pads as t). Glove archetypes: Cleto Reyes, Winning MS-600, Twins Special, Hayabusa T3; Everlast/Venum/Ringside models stay in m. "
 "Grant and Rival in the register without models (no retrieved page named a model). Hand wraps and focus mitts carry types only; no model page was retrieved.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/13_02.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
