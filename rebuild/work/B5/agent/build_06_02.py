import json, glob, os
W='https://en.wikipedia.org/wiki/'
HM='https://www.hivemodern.com/pages/product16016/cylinda-line-sugar-bowl-arne-jacobsen-stelton'
VA='https://collections.vam.ac.uk/context/organisation/A20566/stelton-ltd'
def X(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a1,"mk":b,"y":c,"d":e} for a1,b,c,e in v],"dt":dt}
kinds=[
 {"n":"Serving tray","a":"tray · tea tray · salver","d":"Flat tray with a raised edge for carrying and serving food and drink.",
  "t":["butler's tray (folding stand)","tea tray","galleried tray","lacquer tray (Japanese obon)","bed or lap tray","silver or silver-plated salver","anodised aluminium","melamine or printed tray"],
  "s":"https://www.replacements.com/piece-guide",
  "x":[X("Butler's tray","","Tray with a raised surround and long-side handles on a folding-legged stand, serving drinks and doubling as a side table.","","",W+"Tray",[],"wood or metal · tray plus folding stand"),
       X("Kaymet tray","Kaymet ribbed tray","London-made anodised aluminium tray, pressed from one sheet or assembled with ridged edges and handles.","Kaymet","1947","https://spitalfieldslife.com/?p=207402",
         [("Ribbed tray","Kaymet","","Ribbing cut polishing and metal use; 1950s look."),("Assembled tray with ridged edges and handles","Kaymet","","")],"anodised aluminium · grained or polished finish · colours · sizes"),
       X("Girotondo","Girotondo round tray","Mirror-polished steel tray with a border of cut-out little-men figures by King-Kong (Stefano Giovannoni and Guido Venturini).","Alessi","1989","https://uk.alessi.com/products/girotondo-round-tray",
         [("Round tray AKKGT, 40 cm (15.75 in)","Alessi","1989","18/10 stainless steel, mirror polished.")],"18/10 stainless steel · round sizes · later coloured versions"),
       X("Vertigo","Vertigo tray","Silver-plated tray by Andrée Putman with asymmetric raised rings that serve as handles.","Christofle","","https://www.maisonlipari.ca/products/christofle-vertigo-rectangular-tray-with-handles",
         [("Rectangular tray with handles","Christofle","","Sizes 6×8, 16×12 and 21×16.5 in.")],"silver plate · round and rectangular · sizes")]},
 {"n":"Serving bowl","a":"salad bowl · fruit bowl","d":"Large bowl holding several portions, set on the table for sharing.",
  "t":["salad bowl","fruit bowl","pedestal bowl","nesting set","wood, ceramic, glass or steel"],"s":W+"Bowl",
  "x":[X("Bernadotte serving bowl","Bernadotte bowl","Ribbed polished bowl from Sigvard Bernadotte's Georg Jensen line, used for fruit or snacks.","Georg Jensen","1930","https://www.connox.com/categories/kitchenware/serving-bowls/georg-jensen-bernadotte-serving-bowl.html",
         [("Stainless steel serving bowl, small / medium / large","Georg Jensen","","Current high-gloss steel production.")],"stainless steel (current) · sterling silver (vintage) · sizes"),
       X("Cylinda-Line salad bowl","","Cylindrical stainless steel salad bowl from Arne Jacobsen's Cylinda-Line for Stelton.","Stelton","1967",HM,[],"stainless steel")]},
 {"n":"Cake stand","a":"étagère · cake plate on pedestal","d":"Raised plate, or stack of plates, for presenting cakes and pastries at the table.",
  "t":["pedestal stand","tiered stand (étagère)","covered stand with dome","glass, ceramic, metal or wood"],"s":W+"Cake_stand"},
 {"n":"Cheese board","a":"cheese platter · cheese tools","d":"Board for serving cheese, with the knives and tools used to cut it.",
  "t":["cheese knife set","cheese dome","wood, slate or marble board","cheese plane","girolle"],"s":W+"Girolle",
  "x":[X("Ostehøvel","cheese slicer · cheese plane","Norwegian slotted-blade cheese plane invented by Thor Bjørklund, made in Lillehammer.","","1925",W+"Cheese_slicer",
         [("Original plane","","1925","Invented 1925; mass production from 1927.")],"blade steel · handle material"),
       X("Girolle","Tête de Moine curler","Rotating scraper that shaves Tête de Moine cheese into rosettes, invented by Nicolas Crevoisier and made by Métafil-laGirolle.","","1982",W+"Girolle",[],"base wood · cover")]},
 {"n":"Butter dish","a":"beurrier · butter keeper","d":"Covered dish for keeping and serving butter at the table.",
  "t":["covered butter dish","French butter dish (water seal)","butter dish with ice chamber (historic)","ceramic, glass or silver"],"s":W+"Butter_dish",
  "x":[X("French butter dish","butter bell · butter crock","Bell-shaped lid holding butter over water in the base, sealing it from air.","","",W+"Butter_dish",[],"ceramic · colours"),
       X("Le Creuset stoneware butter dish","","Enamelled stoneware covered dish sized for a 225–250 g block, with a grip knob lid.","Le Creuset","","https://www.johnlewis.com/le-creuset-stoneware-butter-dish-thyme/p114464166",[],"stoneware · house colours")]},
 {"n":"Sugar bowl and creamer","a":"sugar basin · milk jug · cream jug · creamer","d":"Lidded bowl for sugar and small jug for milk or cream, served with tea or coffee.",
  "t":["sugar bowl","creamer / cream jug","milk jug","sugar tongs","silver, porcelain or glass"],"s":W+"Sugar_bowl",
  "x":[X("Cow creamer","","Creamer shaped as a cow, filled through the back and poured from the mouth; Dutch in origin.","","c. 1740",W+"Cow_creamer",
         [("Staffordshire saltglaze stoneware","","c. 1740","English ceramic version."),("Silver cow creamer by John Schuppe","","from 1753","London silversmith who made little else.")],"saltglaze, earthenware or silver"),
       X("Bombè","Bombé","Carlo Alessi's rounded steel tea and coffee service with bakelite details; sugar bowl and milk jug sold with it.","Alessi","1945","https://saltsmillshop.co.uk/products/sugar-bowl-bombe",
         [("Sugar bowl, about 14¾ oz","Alessi","1945","18/10 steel and bakelite."),("Milk jug","Alessi","1945","")],"18/10 stainless steel · bakelite"),
       X("Cylinda-Line","","Arne Jacobsen's stainless steel service for Stelton based on standard steel tubes; won the Danish ID Prize.","Stelton","1967",HM,
         [("Sugar bowl","Stelton","1967","")],"stainless steel · cylindrical pieces")]},
 {"n":"Cruet set","a":"cruet stand · condiment set · ménagère · salt and pepper","d":"Stand holding salt, pepper, oil and vinegar containers, or the matched shakers alone.",
  "t":["salt and pepper shakers","salt cellar (open salt)","salt pig","oil and vinegar cruets","silver, glass, ceramic or steel"],"s":W+"Cruet-stand",
  "x":[X("Salt cellar","salt · open salt · salt dip","Open dish for salt at the table, from the medieval master salt to small trencher salts.","","Roman era onwards",W+"Salt_cellar",
         [("Master or standing salt","","Middle Ages","Large status vessel at the head table."),("Trencher salt","","by early 18th c.","Small dish by each setting."),("Cellini Salt Cellar","","1540–43","Gold and enamel, for Francis I.")],"silver, pressed glass, ceramic"),
       X("Silver cruet stand","","Metal stand carrying condiment bottles and casters, an English silver form.","","1720s",W+"Cruet-stand",[("Silver cruet stand","","1720–23","")],"silver or plate · bottle count"),
       X("5070","Sottsass cruet set","Ettore Sottsass's steel stand holding glass oil, vinegar, salt and pepper bottles on their sides.","Alessi","1978","https://www.boijmans.nl/en/collection/artworks/108287/cruet",[],"stainless steel · crystal"),
       X("Cylinda-Line salt and pepper set","","Cylindrical steel salt and pepper set from Arne Jacobsen's Cylinda-Line.","Stelton","1967",VA,[],"stainless steel")]},
 {"n":"Bread basket","a":"breadbasket","d":"Basket or dish for serving bread and rolls at the table.",
  "t":["woven wicker or bamboo","wire","linen-lined","bread bag"],"s":"https://shop.mohd.it/en/nordic-kitchen-bread-basket-small-sand.html",
  "m":[["Nordic Kitchen bread basket","Eva Trio"]]},
 {"n":"Trivet","a":"pot stand · hot pad · pot coaster","d":"Heat-resistant stand set under a hot dish or pan to protect the table.",
  "t":["three-legged","cast iron or metal","wood","ceramic tile","cork","silicone"],"s":W+"Trivet"},
 {"n":"Hard placemat","a":"place mat","d":"Rigid mat set under a place setting; textile placemats are in Soft Furnishings.",
  "t":["cork","bamboo","resin","cork-backed printed board","slate"],"s":"https://www.charlies.co.uk/creative-tops-cork-terrazzo-design-placemats-set-of-4/",
  "m":[["Cork-backed placemats","Pimpernel"],["Cork terrazzo placemats","Creative Tops"]]},
 {"n":"Coaster","a":"drinks mat","d":"Small hard mat set under a glass or cup.",
  "t":["cork","ceramic","cork-backed printed board","slate","steel"],"s":"https://shop.rnli.org/products/rs2672311-cork-shipping-forecast-coasters-set-of-4",
  "x":[X("Cylinda-Line coaster set","","Stainless steel coasters from Arne Jacobsen's Cylinda-Line.","Stelton","1967",HM,[],"stainless steel")],
  "m":[["Cork-backed coasters","Pimpernel"]]},
 {"n":"Napkin ring","a":"serviette ring","d":"Ring that holds a rolled napkin, originally marking each person's napkin.",
  "t":["silver or silver plate","figural","wood","bone","porcelain or glass","numbered set"],"s":W+"Napkin_ring"},
 {"n":"Lazy Susan","a":"dumb waiter · revolving server · turntable","d":"Rotating round tray on a table so diners can share dishes.",
  "t":["wood","glass","plastic"],"s":W+"Lazy_Susan"},
]
want={'Alessi','Georg Jensen','Christofle','Le Creuset'}; brands=[]; seen=set()
for f in sorted(glob.glob('work/B5/shelves/*.json')):
  if f.endswith('06_02.json'): continue
  for b in json.load(open(f)).get('brands',[]):
    if b['n'] in want and b['n'] not in seen: seen.add(b['n']); brands.append(b)
for b in brands:
  if b['n']=='Alessi': b['sig']=b['sig']+['Girotondo','Bombè','5070']
  if b['n']=='Georg Jensen': b['sig']=b['sig']+['Bernadotte serving bowl']
  if b['n']=='Christofle': b['sig']=b['sig']+['Vertigo']
brands+=[
 {"n":"Stelton","c":"Denmark","f":"","seg":"design houseware","d":"Danish steel houseware maker known for Arne Jacobsen's 1967 Cylinda-Line service.","lines":["Cylinda-Line"],"eras":["Arne Jacobsen Cylinda-Line, 1967","Erik Magnussen vacuum jug, c. 1976"],"sig":["Cylinda-Line"],"sc":["Scandinavian design"],"rel":["Georg Jensen"],"s":VA},
 {"n":"Kaymet","c":"United Kingdom","f":"1947","seg":"anodised aluminium trays","d":"London maker of anodised aluminium trays and trolleys founded by Sydney Schreiber (Kahn); revived in Bermondsey from 2013.","lines":["Trays","Trolleys"],"eras":["Sydney Kahn, 1947–","Mark Brearley, 2013–"],"sig":["Kaymet tray"],"sc":["mid-century British design"],"rel":[],"s":"https://spitalfieldslife.com/?p=207402"}]
trads=[{"n":"Wajima-nuri","g":"Lacquer","r":"Wajima, Ishikawa (Noto Peninsula), Japan","p":"Technique established early Edo period; oldest surviving piece 1524","d":"Japanese lacquerware on wooden cores with an unusually durable layered undercoat.","tech":"many layers of urushi mixed with powdered diatomaceous earth (ji-no-ko) over wood","mat":"urushi lacquer, ji-no-ko, zelkova wood","forms":["bowls","lacquer serveware"],"ctr":["Wajima City","Wajima Museum of Urushi Art"],"auth":"ji-no-ko undercoat on solid wood; Wajima-style pieces are also made by overseas workshops","s":W+"Wajima-nuri"}]
notes=("Old kinds kept: Serving tray (k82, Butler's tray model became an archetype), Hard placemat (k83), Coaster (k84). New kinds per plan, all sourced. "
 "Left out: Kay Bojesen, Riess enamel and Mason Cash (no serveware piece retrievable for this shelf; Mason Cash is in other shelves); Pimpernel only as a flat model (no brand page retrieved); "
 "Christofle Vertigo year and Alessi 5070 component list not confirmed on a fetched page so omitted; Japanese obon trays only as a type (Wajima-nuri tradition added). Textile placemats stay in B2.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p='work/B5/shelves/06_02.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(len(kinds), sum(len(k.get('x',[])) for k in kinds), len(brands))
