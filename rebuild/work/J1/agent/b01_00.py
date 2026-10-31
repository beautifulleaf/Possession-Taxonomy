import json,os
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
CR="https://www.consumoresponde.es/actualidad/noticias/precinto-etiquetado-mejores-referencias-calidad-origen-jamon-paleta-ibericos"
kinds=[
{"n":"Ibérico pork","a":"Iberian pork · cerdo ibérico · pata negra (fresh)","d":"Fresh, uncured meat of the Iberian pig, sold as named butcher's cuts and labelled by diet and breed purity.",
 "t":["secreto","presa","pluma","lagarto","abanico","carrillera (cheek)","cabecero (collar)","solomillo (tenderloin)","costillas (ribs)"],
 "s":"https://eatcampogrande.com/blogs/kitchen/types-of-iberico-pork-cuts",
 "x":[X("Ibérico label classes (Real Decreto 4/2014)","Spain's quality standard naming Ibérico products by feeding and breed purity, with coloured seals; also applies to fresh cuts.","","2014",CR,
   [{"n":"100% ibérico de bellota (black seal)","mk":"","y":"2014","d":"100% Iberian parents in the herdbook, acorn-fattened; only class allowed 'pata negra'"},
    {"n":"Ibérico de bellota (red seal)","mk":"","y":"2014","d":"at least 50% Iberian, acorn-fattened"},
    {"n":"Ibérico de cebo de campo (green seal)","mk":"","y":"2014","d":"feed-fattened, extensive or outdoor farms"},
    {"n":"Ibérico de cebo (white seal)","mk":"","y":"2014","d":"feed-fattened, intensive farms"}],
   "seal colour · breed % · cut"),
  X("Iberian pig","Traditional dark pig breed of Spain and Portugal, fattened on holm, gall and cork oak acorns in the dehesa.","","Neolithic origins",W+"Iberian_pig",[],"breed purity · region",a="Alentejo pig · porco alentejano")],
 "dt":"label class · breed purity · cut"},
{"n":"Heritage-breed pork","a":"rare-breed pork · traditional-breed pork","d":"Fresh pork from a named traditional or rare pig breed, often sold under a breed society or protected label.",
 "t":["Duroc","Tamworth","Large Black"],
 "s":W+"Gloucestershire_Old_Spots",
 "x":[
  X("Berkshire pork (Kurobuta)","Meat of the black English Berkshire breed, marketed in Japan and the US as Kurobuta at a premium.","","",W+"Berkshire_pig",
    [{"n":"Kagoshima Berkshire","mk":"","y":"1930s","d":"Japanese line from two British Berkshires, considered a separate breed"},
     {"n":"Snake River Farms Kurobuta pork","mk":"Snake River Farms","y":"","d":"US Kurobuta line: chops, ribs, roasts, bacon, ham"}],"cut",a="Kurobuta · black pork"),
  X("Mangalitsa pork","Fatty, juicy meat of Hungary's curly-coated lard pig.","","1833",W+"Mangalica",
    [{"n":"Blonde Mangalica","mk":"","y":"1833","d":""},{"n":"Swallow-bellied Mangalica","mk":"","y":"","d":""},{"n":"Red Mangalica","mk":"","y":"","d":""}],"variety · cut",a="Mangalica · Mangalitza"),
  X("Traditionally farmed Gloucestershire Old Spots pork","Pork of the spotted Gloucestershire Old Spots breed, protected as a Traditional Speciality Guaranteed.","","2010",W+"Gloucestershire_Old_Spots",[],"cut",a="Old Spots"),
  X("Suino Cinto Toscano DOP","Meat of Tuscan-raised Cinta Senese pigs under protected designation of origin.","","2006",W+"Cinta_Senese",[],"cut",a="Cinta Senese"),
  X("Porc noir de Bigorre AOP","Red, marbled meat of the black Bigorre pig, raised outdoors in the Hautes-Pyrénées and slaughtered at about 15 months.","","2017","https://www.connexionfrance.com/magazine/from-extinction-to-frances-top-jambon/407039",[],"cut · fresh or cured",a="Noir de Bigorre"),
 ],
 "dt":"breed · label · cut"},
{"n":"Suckling pig","a":"cochinillo · lechón · sucking pig","d":"A whole milk-fed young pig, sold whole for roasting.",
 "t":["whole","half"],
 "s":"https://www.dartagnan.com/buy/meat-game",
 "x":[X("Cochinillo de Segovia","Segovia white-breed piglet fed only on its mother's milk, at most three weeks old and 5.2–7.3 kg, tagged on the leg.","","", "https://theobjective.com/espana/madrid/2023-12-30/cochinillo-asado-horno-lena-marca-garantia/",[],"weight · whole or half",a="Marca de Garantía Cochinillo de Segovia")]},
]
notes=("Ibérico: cured hams live under Dry-cured hams. Left out: Kagoshima Kurobuta as a separate label (only Kagoshima Berkshire breed attested), Jinhua (wiki page 404, no other source retrieved), Duroc/Tamworth/Large Black kept as types only (no retrieved page). "
"Snake River Farms brand entry is given in shelf 00_00. Wikidata helper unavailable.")
out={"kinds":kinds,"brands":[],"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/01_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
