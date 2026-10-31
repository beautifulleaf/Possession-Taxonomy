import json
R='/home/user/Possession-Taxonomy/rebuild/out/'
W='https://en.wikipedia.org/wiki/'
# brands
bp=R+'J1_brands.json'; B=json.load(open(bp))
have={b['n'].lower() for b in B['b']}
def br(n,c,f,seg,kf,d,sig,s,rel=[]):
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":[],"eras":[],"sig":sig,"sc":[],"rel":rel,"s":s}
new=[
br("Tyson Foods","United States","1935","Mainstream","chicken, beef, pork","US processor of chicken, beef and pork; owns Jimmy Dean, Hillshire Farm and Ball Park.",[],W+"Tyson_Foods",["Jimmy Dean"]),
br("Perdue Farms","United States","1920","Mainstream","chicken, turkey","Maryland poultry and pork producer; owns Niman Ranch since 2015.",[],"https://en.wikipedia.org/wiki/Perdue_Farms",["Niman Ranch"]),
br("Applegate","United States","1987","Premium","natural & organic meats","Natural and organic prepared meats from animals raised without antibiotics or hormones; owned by Hormel since 2015.",[],"https://www.hormelfoods.com/about/our-family/applegate-farms-llc",["Hormel Foods"]),
br("Niman Ranch","United States","1969","Premium","humane-raised beef, pork, lamb","American beef, pork and lamb brand started by rancher Bill Niman; Certified Humane since 2016.",[],W+"Niman_Ranch",["Perdue Farms"]),
br("Campofrío","Spain","1952","Mainstream","deli meats, ham","Spanish processed-meat group started in Burgos by José Luis Ballvé; also owns Aoste, Cesare Fiorucci and Nobre.",[],W+"Campofr%C3%ADo_Food_Group"),
br("ElPozo","Spain","1954","Mainstream","deli meats, ham","Family-owned Spanish meat-products company in Alhama de Murcia, with low-fat and low-sodium lines.",[],W+"ElPozo"),
br("Fleury Michon","France","1905","Mainstream","ham, deli, ready meats","French charcuterie and prepared-food company, among the most bought agri-food brands in France.",[],W+"Fleury_Michon",["Herta"]),
br("Herta","Germany","","Mainstream","ham, frankfurters, knacki","Brand from a butcher shop in Herten, Germany; best known for frankfurters and, in France, ham.",[],W+"Herta_Foods",["Fleury Michon"]),
br("Rovagnati","Italy","1941","Premium","cooked ham, Gran Biscotto","Lombard salumificio from Biassono, known for premium prosciutto cotto and Salame Felino.",["Gran Biscotto"],"https://www.eataly.com/us_en/magazine/producer-stories/meet-rovagnati"),
br("Citterio","Italy","1878","Mainstream","salami, Italian cured meats","Rho salumificio founded by Giuseppe Citterio; created Salame di Milano and introduced vacuum-packed sliced meats in 1958.",["Salame di Milano"],"https://www.citterio.com/en/company/story"),
br("La Quercia","United States","","Artisan & independent","American prosciutto","Norwalk, Iowa curer of prosciutto, founded by Herb and Kathy Eckhouse; flagship Prosciutto Americano.",["Prosciutto Americano"],"https://heavytable.com/prosciutto-making-at-la-quercia-in-norwalk-ia/"),
]
for n in new:
    assert n['n'].lower() not in have; B['b'].append(n)
json.dump(B,open(bp+'.tmp','w'),ensure_ascii=False,indent=1)
# traditions
tp=R+'J1_traditions.json'
def tr(n,r,d,tech,mat,forms,ctr,auth,s): return {"n":n,"g":"Food & drink","r":r,"p":"","d":d,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":s}
T=[
tr("Italian salumi","Italy","Italian meat products, mostly cured pork, served as antipasto; the name comes from Latin sal, salt.","Salting and curing; some, such as mortadella, are cooked.","Pork; beef for bresaola.",["Prosciutto crudo","Pancetta","Guanciale","Capocollo (coppa)","Bresaola","Lardo","Mortadella","Salami","Cotechino"],["Parma","San Daniele","South Tyrol","Modena","Felino","Calabria","Marche and Umbria","Abruzzo"],"Some are PDO (prosciutto di Parma, San Daniele); others such as Salame Felino hold the Italian traditional agri-food product (PAT) status.",W+"Salumi"),
tr("Parma and San Daniele prosciutto","Emilia-Romagna and Friuli-Venezia Giulia, Italy","Raw dry-cured hind leg made under EU protected designation of origin in two named zones.","Salted in stages, rested, then hung in humidity-controlled rooms; aged at least 14 months.","Pig hind leg and sea salt only; no nitrites or nitrates for Parma.",["Prosciutto di Parma","Prosciutto di San Daniele"],["Parma","San Daniele del Friuli"],"Consorzio del Prosciutto di Parma brands each ham with the ducal crown after a horse-bone needle check; the word prosciutto alone is not protected.",W+"Prosciutto_di_Parma"),
tr("Iberian dehesa curing","Spain and Portugal (Huelva, Córdoba, Cáceres, Badajoz, Salamanca, Alentejo)","Dry-curing of hind legs from black Iberian pigs reared on dehesa oak pasture.","Final fattening on acorns and grass; cured for months to years.","Black Iberian pig.",["Jamón ibérico","Paleta ibérica","Lomo ibérico"],["Guijuelo","Jabugo","Dehesa de Extremadura","Los Pedroches"],"Four PDOs; since 2014 coloured labels: black (100% ibérico de bellota, the only pata negra), red, green and white.",W+"Jam%C3%B3n_ib%C3%A9rico"),
tr("Spanish embutidos","Spain, Portugal and former colonies","Stuffed and cured sausages; the Royal Spanish Academy defines embutido as intestine stuffed with minced meat, mainly pork.","Stuffing into casings, then curing.","Pork, sometimes blood and other fillings.",["Chorizo","Salchichón","Fuet","Sobrasada","Botifarra","Morcilla","Androlla"],["Balearic Islands (sobrasada)","Catalonia (botifarra, fuet)","Galicia (androlla)"],"",W+"Embutido"),
tr("French charcuterie","France","Branch of French cuisine devoted to prepared meat products, mainly pork: ham, sausage, terrines, confit.","Salt-curing and brining, forcemeats, fermentation.","Mostly pork.",["Saucisson sec","Pâtés and terrines","Rillettes","Galantines","Cooked ham"],[],"",W+"Charcuterie"),
tr("German Wurst","Germany","Sausage-making with more than 1,500 types, mostly in natural casings, with strict composition rules since the 13th century.","Raw, cooked and smoked sausage making.","Pork, veal, blood.",["Bratwurst","Weißwurst","Wiener","Blutwurst","Leberwurst","Thüringer Mettwurst","Nürnberger Rostbratwurst"],["Bavaria","Thuringia","Nuremberg"],"",W+"German_cuisine"),
tr("Polish kiełbasa","Poland","Regional sausages smoked or fresh, of pork, beef, veal or turkey, with dozens of varieties.","Smoking, air-drying, scalding.","Pork, beef, veal, turkey.",["Kabanosy","Krakowska","Myśliwska","Wiejska","Kiełbasa biała","Kaszanka"],["Małopolska (lisiecka)","Wielkopolska (biała parzona)"],"EU PGI for kiełbasa lisiecka, kiełbasa biała parzona wielkopolska and kiełbasa piaszczańska; TSG for kabanosy staropolskie, krakowska sucha staropolska and others.",W+"Kie%C5%82basa"),
tr("Cantonese preserved meats","Guangdong and Hong Kong, China","Wind-dried and cured pork and duck eaten with rice, especially in autumn and winter.","Marinating in soy, Shaoxing wine and spices, then hanging to dry.","Pork belly, pork and fat, duck.",["Lap cheong (Chinese sausage)","Lap yuk (cured pork belly)","Preserved duck"],[],"",W+"Cantonese_cuisine"),
tr("Japanese jidori poultry","Japan","Local chickens whose parents, or one parent, are native to Japan, raised by a prescribed method.","Slow rearing at low stocking density.","Native-cross chickens.",["Hinai-jidori","Satsuma-jidori","Nagoya Cochin"],["Akita (Hinai)","Kagoshima","Aichi"],"",W+"Jidori"),
]
json.dump({"t":T},open(tp+'.tmp','w'),ensure_ascii=False,indent=1)
# items
P=R+'J1.json'; d=json.load(open(P))
def shelf(dn,sn):
    for dp in d['depts']:
        if dp['n']==dn:
            for s in dp['s']:
                if s['n']==sn: return s
    raise KeyError(sn)
def kind(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k
wc=kind('Whole chicken')
wc['x'].append({"n":"Hinai-jidori","a":"Hinai jidori","d":"Premium Akita chicken from a native Hinai male crossed with a Road hen; reared about 150 days, under five birds per square metre.","mk":"","y":"","s":"https://nihonmono.jp/en/?p=20963","v":[],"dt":"rearing days · stocking density"})
shelf('Poultry','Chicken')['k'].append({"n":"Poultry offal","a":"giblets · chicken livers · gizzards","d":"Edible organs of chickens and other fowl, sold raw: heart, gizzard, liver and neck.","t":["livers","gizzards","hearts","necks","mixed giblets"],"s":W+"Giblets"})
shelf('Ham, bacon & cured meats','Cured whole muscles & lardo')['k'].append({"n":"Lap yuk","a":"Chinese cured pork belly · là ròu · 臘肉","d":"Cantonese cured pork belly, marinated in soy and Shaoxing wine then hung to dry; steamed before eating.","t":["skin-on strips","smoked"],"s":"https://thewoksoflife.com/chinese-cured-pork-belly/"})
shelf('Sausages & salami','Cooked & smoked sausages')['k'].append({"n":"Saucisson à l'ail","a":"garlic sausage · saucisson de Paris · Paris-ail","d":"French pork sausage seasoned with fresh garlic, egg white, salt and pepper; sometimes smoked.","t":["smoked"],"s":"https://fr.wikipedia.org/wiki/Saucisson_%C3%A0_l%27ail"})
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1)
