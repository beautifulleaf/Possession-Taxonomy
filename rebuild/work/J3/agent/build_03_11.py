import json, os
W='https://en.wikipedia.org/wiki/'; WD='https://www.wikidata.org/wiki/'
def V(n,mk='',y='',d=''): return {"n":n,"mk":mk,"y":y,"d":d}
def X(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v,"dt":dt}
feta={"n":"Feta","a":"Greek feta · Feta PDO · φέτα","d":"Greek white brined cheese of sheep's milk with up to 30% goat's milk, crumbly, salty and rindless; protected origin since 2002.",
 "t":["firm (tangier)","soft (spreadable)","barrel-matured","metal-vessel / tin-matured","trímma (crumble)","block in brine","vacuum pack"],
 "s":"https://www.cheese.com/raw-milk-feta/",
 "x":[X("Feta PDO","φέτα · Greek feta","Brined sheep's-and-goat's-milk cheese from mainland Greece and Lesbos, matured at least two months; the name is reserved to it in the EU.","","PDO 2002",W+"Feta",
   [V("Dodoni Feta PDO","Dodoni","","Epirus milk; first exported feta brand per the maker"),
    V("Kolios Authentic Feta PDO","Kolios","","also Vintage FETA and Bio Organic Feta PDO lines"),
    V("Feta Mevgal","Mevgal","","Macedonian dairy, Koufalia"),
    V("Epiros Original Feta PDO","Epiros","","sheep and goat milk; in brine or vacuum pack"),
    V("YAMAS! Greek Feta PDO","Futura Foods","","importer label")],
   "matured in wooden barrels or metal vessels · firm or soft · block, crumble or cubes · tub, tin or vacuum pack")]}
brined={"n":"Brined white cheese","a":"white cheese · beyaz peynir · sirene · telemea · Domiati · Lighvan · salad cheese","d":"White cheese ripened and kept in brine, soft to semi-hard and salty, sold under a regional name or as white cheese rather than as feta.",
 "t":["sheep's milk","goat's milk","cow's milk","buffalo milk","mixed milk","fresh","matured","with herbs (otlu)","UF (ultrafiltered)"],
 "s":"https://toptan.migros.com.tr/peynir-cs-5-76",
 "x":[
  X("Beyaz peynir","Turkish white cheese · salamura beyaz peynir","Turkish brined cheese of sheep's, cow's or goat's milk, cut into blocks and kept in brine for about six months.","","",W+"Beyaz_peynir",
   [V("Ezine peyniri GI","","","Ezine, Çanakkale"),V("Edirne beyaz peyniri GI"),V("Van otlu peyniri GI","","","herb cheese"),V("Şanlıurfa peyniri GI"),
    V("Tahsildaroğlu Ezine Peyniri","Tahsildaroğlu Süt Ürünleri"),V("Yelken Ezine Koyun Beyaz Peynir","Yelken"),V("Sütaş Beyaz Peynir","Sütaş"),V("İçim Beyaz Peynir","İçim")],
   "milk sheep, cow, goat or mixed · fresh to mature · full-fat or light · tin or block"),
  X("Sirene","Bulgarsko byalo salamureno sirene · bjalo sirene · Bulgarian white cheese","Bulgarian crumbly brined white cheese of goat's, sheep's, cow's or buffalo milk, aged at least three months.","","PDO 2023",W+"Sirene",
   [V("Bulgarsko byalo salamureno sirene PDO","","2023","EU-registered name")],"milk sheep, cow, goat or buffalo · minimum 3 months · block in brine"),
  X("Telemea","","Romanian soft brined cheese, traditionally sheep's milk, now also cow's; firmer and saltier with age, sometimes with cumin.","","",W+"Telemea",
   [V("Telemea de Ibănești PDO","","2017","first Romanian PDO"),V("Telemea de Sibiu PGI","","2019")],"milk sheep, cow, goat or buffalo · young or aged · plain or with cumin"),
  X("Domiati","Egyptian white cheese","Egypt's most common cheese: soft brined white cheese of buffalo or cow's milk, salted before renneting.","","",W+"Domiati",
   [V("Obour Land Gold White Cheese","Obour Land")],"fresh or aged in brine · buffalo, cow or mixed milk"),
  X("Lighvan","Lighvan cheese · Liqvan","Iranian sour brined curd cheese of raw ewe's milk from Liqvan village, matured 3–4 months in brine.","","",W+"Lighvan_cheese",[],"raw ewe's milk · 3–4 months in 10–12% brine"),
  X("Imeruli","Imeretian cheese · chkinti kveli","Georgian handmade fresh cow's-milk cheese from Imereti, salted on a clay tray to ripen.","","",W+"Chkinti",
   [V("Imeruli Kveli GI")],"fresh or salted · cow's milk"),
  X("Sjenica cheese","Sjenički sir","Serbian white brined cheese of sheep's milk from the Pešter plateau.","","",W+"Serbian_cheeses",
   [V("Zlatarski sir","","","cow's-milk white brined cheese, Pešter area"),V("Homoljski sir GI","","","Homolje; cow, goat or sheep milk")],"sheep or cow milk · block in brine"),
  X("Batzos","Μπάτζος","Greek hard brined cheese of sheep's and/or goat's milk from Macedonia and Thessaly, matured at least three months in brine.","","PDO 1996",W+"Batzos",[],"sheep, goat or mixed milk · raw or pasteurised"),
  X("Kalathaki Limnou","Καλαθάκι Λήμνου · basket cheese of Lemnos","Soft white brined cheese of Lemnos, drained in small baskets that give its round patterned shape.","","PDO","https://thecheeseatlas.com/cheese-profiles/kalathaki-limnou/",[],"sheep's milk with up to 30% goat's · at least 2 months in brine"),
  X("Sfela","Σφέλα","Greek brined white cheese with protected designation of origin.","","PDO",WD+"Q5489566",[],"sheep or goat milk"),
  X("Feta-style white cheese","white cheese · salad cheese · UF feta","Feta-type brined cheese made outside the Greek PDO, often from cow's or buffalo milk and sold under other names.","","",W+"Feta",
   [V("Apetina","Arla Foods","","renamed from feta after the EU ruling"),V("Fine Fettle Yorkshire","","","formerly Yorkshire Feta"),
    V("Mrs Bell's Salad Cheese","Shepherds Purse Cheeses"),V("St Canice","Abbey Cheese Company"),V("Domty Feta Plus","Arabian Food Industries (Domty)"),
    V("Almarai Full Cream Feta Cheese","Almarai"),V("Torku Fresh Turkish Type UF Feta Cheese","Torku"),V("First Choice South African Feta","Woodlands Dairy")],
   "cow, buffalo or mixed milk · UF or traditional · block or tub")],
 "m":[["Brânză de Măgură PDO",""],["Hutsul sheep bryndza GI",""],["Hutsul cow's milk bryndza GI",""],["Kobi GI",""],["Kartuli Kveli GI",""]]}
hall={"n":"Halloumi","a":"hellim · χαλλούμι","d":"Cypriot semi-hard brined cheese whose curd is scalded in whey, folded with mint; squeaky and non-melting when grilled.",
 "t":["fresh","mature (brined 40+ days)","goat & sheep milk","cow's-milk blend","light","with mint","with chilli"],
 "s":"https://www.cheese.com/halloumi/",
 "x":[X("Cyprus halloumi PDO","Χαλλούμι/Halloumi/Hellim PDO","Halloumi from Cyprus, of goat's and/or sheep's milk with cow's milk now common, curd heated in whey, salted, minted and folded.","","PDO 2021",W+"Halloumi",
   [V("Fresh halloumi","","","elastic, milder, less salty"),V("Mature halloumi","","","brined at least 40 days; drier, harder, saltier"),V("Dodoni Halloumi","Dodoni")],
   "fresh or mature · milk mix (goat, sheep, cow) · with mint · in whey brine or vacuum pack")],
 "m":[["Pınar Halloumi Cheese","Pınar Süt Ürünleri"],["Almarai Halloumi Cheese","Almarai"],["Al Rawabi Full Fat Halloumi Cheese","Al Rawabi"],["Lyttos Halloumi","Aldi"],["K-Favourites Halloumi","Kaufland"],["Bahçıvan Hellim Peyniri","Bahçıvan Food Industry Trade"]]}
grill={"n":"Grilling cheese","a":"queijo coalho · leipäjuusto · juustoleipä · kalari · formaela · squeaky cheese","d":"Cheese with a high melting point sold to grill, fry or bake without melting and not kept in brine; halloumi has its own entry.",
 "t":["on skewers","baked disc","pan-fried slices","cow's milk","goat or sheep milk"],
 "s":"https://www.sutas.com/sutas-izgarella-cheese-6x60-g",
 "x":[
  X("Queijo coalho","queijo de coalho","Firm, squeaky cow's-milk cheese of north-eastern Brazil, grilled on a stick over charcoal.","","",W+"Queijo_coalho",[],"skewers or blocks · plain or with oregano"),
  X("Leipäjuusto","juustoleipä · bread cheese · Finnish squeaky cheese · kaffeost","Finnish disc of fresh curd baked, grilled or flambéed to brown marks; traditionally from cow's colostrum.","","",W+"Bread_cheese",[],"disc 2–3 cm thick · cow's milk or colostrum · goat milk in the US"),
  X("Kalari","Kaladi","Dense ripened cheese of the Udhampur district of Jammu, sautéed in its own fat.","","",W+"Kalari_cheese",[V("Udhampur Kaladi GI")],"cow, buffalo or goat milk"),
  X("Formaela","Formaella Arachova Parnassos","Hard sheep's or goat's-milk cheese made only in Arachova, eaten grilled or fried as saganaki.","","PDO 1996",W+"Formaela",[V("Formaella Arachova Parnassos PDO")],"sheep or goat milk · whole or sliced")]}
brands=[
 {"n":"Dodoni","c":"Greece","f":"1963","seg":"Dairy · feta","d":"Ioannina dairy using Epirus milk, calling itself the first exported feta brand.","lines":["Feta","Halloumi","Greek Yogurt","DODONI Plant'd"],"eras":[],"sig":["Feta PDO"],"sc":[],"rel":[],"s":"https://us.dodoni.com/who-we-are/"},
 {"n":"Kolios","c":"Greece","f":"1948","seg":"Dairy · feta","d":"Greek cheesemaker and a leading exporter of Feta PDO.","lines":["Authentic FETA","Vintage FETA","Traditional White cheeses","Local White cheeses","Mezé FETA","Manouri PDO"],"eras":[],"sig":["Feta PDO"],"sc":[],"rel":[],"s":"https://www.kolios.gr/en/our_products/feta-pdo-white-cheeses/authenic_range/bio-organic-feta-pdo/"},
 {"n":"Mevgal","c":"Greece","f":"1950","seg":"Dairy","d":"Macedonian milk industry based in Koufalia, Thessaloniki; yoghurt, desserts and cheese including feta.","lines":["Feta Mevgal"],"eras":[],"sig":["Feta PDO"],"sc":[],"rel":[],"s":W+"Mevgal"},
 {"n":"Epiros","c":"Greece","f":"","seg":"Dairy · feta","d":"Greek producer of Original Feta PDO from sheep's and goat's milk.","lines":["Original Feta PDO"],"eras":[],"sig":["Feta PDO"],"sc":[],"rel":[],"s":"https://www.epiros.eu/product/feta-p-d-o-2/"}]
notes=("Feta: PDO archetype with Dodoni, Kolios, Mevgal, Epiros, YAMAS! as versions; barrel/metal vessel and firm/soft as detail (no producer page confirmed barrel vs tin per brand). "
 "Non-PDO feta-type SKUs (Almarai, Domty, Torku, Woodlands, St Canice, Mrs Bell's) moved to Brined white cheese / Feta-style white cheese; dropped Domty Premium Gold, Milla, Käse Barrel Aged, İçim UF (SKU duplicates). "
 "Brined white cheese: Turkish SKU list trimmed to 4 Ezine/major-brand versions under Beyaz peynir; dropped Altınkılıç, Ayça, Duranlar, Ekici, Enka, Mora Çiftlik, Sancak, Teksüt, Ulussan, Yelken Gurme, Tahsildaroğlu İnek (SKU noise). "
 "Brânză de Popeasca dropped (not a brined white cheese; unconfirmed); Brânză de Măgură, Hutsul bryndzas, Kobi, Kartuli Kveli kept as flat models. Kalathaki and Sfela PDO year not confirmed so given as 'PDO'. "
 "Halloumi: Ekici and Käse halloumi SKUs dropped. Grilling cheese source pages found no EU TSG/GI years for leipäjuusto or kalari GI year. No traditions added.")
out={"kinds":[feta,brined,hall,grill],"brands":brands,"traditions":[],"notes":notes}
p='work/J3/shelves/03_11.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
