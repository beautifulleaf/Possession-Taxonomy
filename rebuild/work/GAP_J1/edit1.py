import json,re,os
P='rebuild/out/J1.json'
d=json.load(open(P))
K={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']: K[k['n']]=(dp,s,k)
WP='https://en.wikipedia.org/wiki/'
def ent(n,dsc,s,g=None,y='',a='',mk=''):
    e={'n':n,'a':a,'d':dsc,'mk':mk,'y':y,'s':s,'v':[]}
    if g: e['g']=g
    return e
def have(k): return {e['n'].lower() for e in k['x']}
def add(kn,rows,src,gcol=True):
    k=K[kn][2]; h=have(k); c=0
    for r in rows:
        if r[0].lower() in h: continue
        n,g,dsc=r[0],r[1],r[2]; y=r[3] if len(r)>3 else ''
        k['x'].append(ent(n,dsc,src,g,y)); h.add(n.lower()); c+=1
    return c
def setg(kn,mapping,default=None):
    for e in K[kn][2]['x']:
        if not e.get('g'): e['g']=mapping.get(e['n'],default)
        if not e.get('g'): print('NOG',kn,e['n'])
def sortg(kn):
    k=K[kn][2]; k['x'].sort(key=lambda e:(e.get('g',''),))
log={}
# ---- Hams
HL=WP+'List_of_hams'
log['Regional']=add('Regional dry-cured hams',[
 ('Jambon de Luxeuil','France','French ham named in the List of hams; the list gives no further detail.'),
 ('Jambon de Savoie','France','French ham named in the List of hams; the list gives no further detail.'),
 ('Jambon du Périgord','France','French ham named in the List of hams; the list gives no further detail.'),
 ('Jambon des Pyrénées','France','French ham named in the List of hams; the list gives no further detail.'),
 ('Smithfield ham','United States','Country ham from Smithfield, Virginia, finish-cured by the dry-cure method.'),
],HL)
k=K['Regional dry-cured hams'][2]
k['sel']=re.sub(r'Covers the French.*$','',k['sel']).strip()+" Complete: 26 of 26 dry-cured, eaten-raw ham rows outside Italy and Spain in that page (14 French, 5 Chinese and Balkan, Welsh, Bulgarian, Montenegrin, Galician and US rows), plus Kraški pršut and Barrancos from their own pages. Left out of this kind: Italian hams (own kinds), Presunto and Spanish jamón (own kinds), smoked hams (Smoked raw ham), and cooked, glazed, city, torchon and chipped hams, York, Wiltshire, Bradenham and Prague (Cooked ham) and Limerick (a method)."
k=K['Smoked raw ham'][2]
k['sel']=k['sel'].replace('Covers the German, South Tyrolean and Luxembourg hams in that list.','Complete: 6 of 6 smoked raw hams in that page (Ammerländer, Black Forest, Westphalian, Speck Alto Adige, Tyrolean Speck, Éisleker); Country ham is smoked but sits in Regional dry-cured hams.')
log['Serrano']=add('Jamón serrano',[('Pernil Cerretà','Spain','Cured ham of white-pig breeds from 24 comarcas of inland Catalonia, cured at least seven months boneless or nine on the bone; EU PGI registered in 2026.',"PGI 2026")],'https://www.3tres3.com/en/latest_swine_news/eu-registers-the-new-pgi-%E2%80%9Cpernil-cerreta_22724/')
log['Chistorra']=add('Fresh chorizo & longaniza',[('Chistorra de Navarra','Spain','Thin pork sausage with paprika and garlic, briefly cured, made in Navarra; EU PGI registered 31 October 2024.',"PGI 2024")],'https://www.cde.ual.es/en/the-commission-grants-a-new-protected-geographical-indication-pgi-to-chistorra-de-navarra-chistorra-from-navarra/')
# ---- Meat box
mk=K['Meat box'][2]
U='https://mob.co.uk/life/online-butcher-shops'
ukb=[('HG Walter','Independent family-run butcher selling high-welfare British meat from small free-range farms.'),
('Donald Russell','Supplier to restaurants, known for dry-aged tomahawk steak and pork chops.'),
('The Ginger Pig','Sells high-welfare, slow-reared meat; known for handmade sausages.'),
('Turner & George','Butcher founded by chef Richard H. Turner and master butcher James George, using traditional butchery.'),
('Riverford','Organic produce company that also sells British meat from its organic butchery in Devon.'),
('Farmison & Co','Butcher specialising in heritage breeds such as Belted Galloway beef.'),
('field&flower','Supports small free-range farmers and processes meat at its Somerset butchery.'),
('Crombies of Edinburgh','Delivers meat in chilled protective boxes.')]
h=have(mk)
for n,dsc in ukb:
    if n.lower() not in h: mk['x'].append(ent(n,dsc+' Listed in a 2021 guide.',U,'Premium online butchers (UK)',mk=n))
mk['x'].append(ent('The Kosher Express','Online kosher butcher selling meat and poultry for delivery across the United States; described in a 2011 article.','https://tcjewfolk.com/?p=17332','Kosher delivery (US)',y='',mk='The Kosher Express'))
mk['sel']=mk['sel'].split(' No ranked list')[0]+" Also Complete: 8 of 8 UK online butchers in the mob.co.uk guide (20 October 2021) and 1 of 1 in the 2011 Jewish Folk article on The Kosher Express. No current ranked list of kosher meat delivery or of premium UK butchers could be fetched: the Delicious magazine page (403) and Good Web Guide (403) were blocked, and searches for kosher meat delivery returned only vendor pages. The list is therefore not claimed complete for kosher delivery."
# ---- Black pudding
B=WP+'Blood_sausage'
bp=[('Thüringer Rotwurst','Germany','Thuringian blood sausage with EU PGI protection.','PGI'),
('Flönz','Germany','Rhineland fried blood sausage, traditionally horse-meat based.'),
('Beutelwurst','Germany','Blutwurst pressed in a linen or paper bag.'),
('Kartoffelwurst','Germany','Palatinate blood sausage using potato cubes to cut the fat, from after the Second World War.'),
('Blunze','Austria','Austrian Blutwurst, sometimes with roll pieces inside.'),
('Boudin du Béarn','France','Large boudin with pork pieces from Béarn, usually eaten cold.'),
('Bloedworst','Netherlands and Belgium','Large blood sausage with suet, sliced and usually pan-fried.'),
('Beuling','Belgium and Netherlands','Banana-sized individual blood sausage, also called zwarte pens.'),
('Tongenworst','Netherlands','Blood sausage with pig\'s tongue.'),
('Träipen','Luxembourg','Blood sausage with green cabbage, pan-fried and served with apple sauce.'),
('Krvavica','Balkans','Winter blood sausage of Slovenia, Bosnia, Croatia and Serbia, often served with sauerkraut and potatoes.'),
('Jelito','Czech Republic','Pork, pig\'s blood and peeled barley.'),
('Véres hurka','Hungary','Pig\'s blood with barley or cubed bread.'),
('Sângerete','Romania','Pork shoulder, pork blood and pre-boiled rice.'),
('Karvavitsa','Bulgaria','Pig\'s blood, fat and mountain herbs, eaten warm in winter.'),
('Blodpølse','Denmark','Pig\'s blood and suet with rye flour, sugar, raisins and spices.'),
('Blóðmör','Iceland','Lamb\'s blood, suet, rye flour and oats in a stomach pouch.'),
('Blodpudding','Sweden','Pig\'s blood, milk, flour, lard and allspice, baked in a water bath.'),
('Vėdarai','Lithuania','Local blood sausage.'),
('Asinsdesa','Latvia','Blood sausage with barley groats, served with lingonberry jam.'),
('Krupniok','Poland','Silesian name for blood sausage.'),
('Żymlok','Poland','Upper Silesian blood sausage using breadcrumbs instead of groats.'),
('Krovyanka','Russia','Buckwheat-filled blood sausage.'),
('Morcilla patatera','Spain','Extremaduran morcilla made creamy with mashed potatoes.'),
('Morcilla de León','Spain','Blood sausage without rice, grilled and spread on toast.'),
('Chouriço de sangue','Portugal','Smoked sausage of pig blood and pork meat from the north, the Beiras and the Alentejo.'),
('Negrinha','Portugal','Thinner, dark Portuguese blood sausage, also called negrito.'),
('Mazzita','Malta','Maltese blood sausage; production resumed in 2024.'),
('Buristo','Italy','Tuscan pig\'s blood and fat cooked in a stomach, spread on bread.'),
('Biroldo','Italy','Tuscan black pudding.'),
('Marsapan','Italy','Black pudding of southern Lombardy.'),
('Dồi tiết','Vietnam','Pork blood, pork fat and basil, boiled or fried.'),
('Sai krok lueat','Thailand','Blood sausage sliced and served with a spicy dipping sauce.'),
('Gyurma','Tibet','Yak or sheep blood sausage, optionally with rice or roasted barley flour.'),
('Doh snam','India','Pork intestine blood sausage from Meghalaya with local spices.'),
('Mutura','Kenya','Meat, blood and spices in a stomach or intestine casing.'),
('Moronga','Mexico','Central Mexican name for morcilla.'),
('Prieta','Chile','Thick-skinned blood sausage eaten cut lengthwise.'),
('Boudin rouge','United States','Louisiana Creole and Cajun pork blood sausage, now usually made without blood.'),
]
log['Black']=add('Black pudding',bp,B)
setg('Black pudding',{'Stornoway black pudding':'United Kingdom','Bury black pudding':'United Kingdom','Sneem black pudding':'Ireland','Drisheen':'Ireland','Morcilla de Burgos':'Spain','Boudin noir':'France','Blutwurst':'Germany','Kaszanka':'Poland','Morcela':'Portugal','Mustamakkara':'Finland','Verivorst':'Estonia','Sundae':'South Korea','Sanguinaccio':'Italy'})
k=K['Black pudding'][2]; k['xg']='country'; sortg('Black pudding')
k['sel']=f"Follows the named blood sausages of {B}. Covers {len(k['x'])} of about 110 named rows in that page (read to the end; the last 62,000 characters are references and a navigation box); the rest are generic local-language names for the same sausage, sweet puddings and dishes that are not sausages (blood tofu, pancakes, soups), or varieties already listed under another name."
# ---- Kielbasa
KB=WP+'Kielbasa'
kb=[('Kiełbasa biała parzona wielkopolska','Poland','Scalded white sausage from Wielkopolska; EU PGI.','PGI'),
('Kiełbasa piaszczańska','Poland','Regional sausage with EU PGI.','PGI'),
('Kiełbasa krakowska sucha staropolska','Poland','Traditional dry krakowska; EU TSG.','TSG'),
('Kiełbasa myśliwska staropolska','Poland',"Traditional hunter's sausage; EU TSG.",'TSG'),
('Kiełbasa odesska','Poland','Polish sausage made with beef.'),
('Gyulai kolbász','Hungary','Common Hungarian smoked sausage from Gyula.'),
('Csabai kolbász','Hungary','Common Hungarian smoked sausage from Békéscsaba.'),
('Csemege kolbász','Hungary','Common Hungarian smoked sausage.'),
('Házi kolbász','Hungary','Hungarian smoked homemade sausage.'),
('Cserkész kolbász','Hungary','Common Hungarian smoked sausage.'),
('Lecsókolbász','Hungary','Spicy sausage made to serve with the pepper-and-tomato stew lecsó.'),
('Budzhena kovbasa','Ukraine','Ukrainian smoked kovbasa.')]
log['Kiel']=add('Kielbasa & smoked sausage',kb,KB)
cc={n:'Poland' for n in ['Krakowska','Wiejska','Myśliwska','Kiełbasa wędzona','Weselna','Kiełbasa jałowcowa staropolska','Kiełbasa lisiecka','Kiełbasa biała']}
cc.update({'American kielbasa':'United States','Cajun andouille':'United States','Kranjska klobasa':'Slovenia','Debrecener':'Hungary','Rookworst':'Netherlands'})
setg('Kielbasa & smoked sausage',cc)
k=K['Kielbasa & smoked sausage'][2]; k['xg']='country'; sortg('Kielbasa & smoked sausage')
k['sel']=f"Follows the named kiełbasa of {KB} and the smoked sausages of https://en.wikipedia.org/wiki/List_of_sausages. Complete: all named Polish PGI and TSG sausages, the named smoked Hungarian sausages and the named Ukrainian smoked kovbasa in the kielbasa page ({len(k['x'])} entries). Left out: dry kabanos (kind Kabanos & snack sticks), blood and liver sausages (their own kinds), sandwiches (Maxwell Street Polish, Polish Boy), and generic national spellings and aliases of the word."
# ---- Bratwurst
k=K['Bratwurst'][2]
cm={'Fränkische Bratwurst':'Germany','Nürnberger Rostbratwurst':'Germany','Thüringer Rostbratwurst':'Germany','Coburger Bratwurst':'Germany','Kulmbacher Bratwurst':'Germany','Würzburger Bratwurst':'Germany','Nordhessische Bratwurst':'Germany','Rote Wurst':'Germany','St. Galler Bratwurst':'Switzerland','Banater Bratwurst':'Romania'}
k['sel']="Follows the regional bratwursts of "+WP+"Bratwurst. Complete: 10 of 10 regional varieties in that page; beer brat is a preparation, not a variety."
# ---- Head cheese
H=WP+'Head_cheese'
hc=[('Presswurst','Austria','Austrian head cheese, served with a light dressing in the west.'),
('Pacha','Bulgaria','Pig\'s head, legs and tongue in a garlic-seasoned broth.'),
('Hladetina','Croatia','Standard Croatian version.'),
('Tlačenica','Croatia','Strongly seasoned Croatian version.'),
('Švargl','Croatia','Chopped parts stuffed into a pig\'s stomach.'),
('Zalatina','Cyprus','Pork-based, often seasoned with lemon juice.'),
('Huspenina','Czech Republic','Boiled pig\'s head or legs set in its broth.'),
('Sylte','Denmark, Norway and Sweden','Traditionally pig\'s head, now often forequarters or shanks.'),
('Rullepølse','Denmark, Norway and Sweden','Rolled version with little aspic.'),
('Sült','Estonia','Looser, less seasoned head cheese, often Christmas food.'),
('Syltty','Finland','Finnish head cheese.'),
('Presssack','Germany','Large Bavarian sausage in deep red, pinkish and grey varieties.'),
('Kaisersülze','Germany','Made only from high-quality pure meat.'),
('Zungenwurst','Germany','Red variety made with beef tongue.'),
('Pichti','Greece','Greek head cheese, usually with vinegar.'),
('Sviðasulta','Iceland','Made from singed sheep\'s head, sometimes cured in lactic acid.'),
('Testa in cassetta','Italy','Genoese "head in a box".'),
('Galerts','Latvia','Meat in gelatine, often with vegetables.'),
('Šaltiena','Lithuania','Lithuanian jellied meat served cold.'),
('Zult','Netherlands and Belgium','Made with blood and pig\'s foot gelatine in Brabant.'),
('Hoofdkaas','Netherlands','Limburg head cheese in red sweet or grey sour varieties.'),
('Cabeça de xara','Portugal','Alentejo head cheese.'),
('Tobă','Romania','Romanian head cheese, also called "drum".'),
('Piftie','Romania','Various meats boiled with garlic and bay leaves, set in jelly.'),
('Kholodets','Russia','Russian jellied meat, popular at festive occasions.'),
('Cabeza de jabalí','Spain','Boar\'s head brawn.'),
('Pressylta','Sweden','Pressed pork and veal brawn.'),
('Sülzli','Switzerland','Typically made with chopped ham or pork.'),
('Matsyk','Ukraine','Especially meaty pressed pork loaf filled with cured pork, from Volhynia and Polisia.'),
('Potted hough','United Kingdom','Scottish potted shank of beef.'),
('Xiao rou','China','Southern Chinese pig trotters boned, pickled, rolled and pressed.'),
('Pyeonyuk','South Korea','Pressed meat, usually pig\'s head.'),
('Giò thủ','Vietnam','Head cheese wrapped in banana leaves, made around Tết.'),
('Kallepache','Iran','Cooked sheep\'s head marinated in its oil and cinnamon.'),
('Queijo de porco','Brazil','Gaúcho "pig cheese".'),
('Head cheese (Upper Midwest)','United States','Upper Midwest head cheese and unsmoked sulze with vinegar and pickles.'),
('Fromage de cochon','United States','Louisiana French head cheese seasoned with green onions.')]
log['Head']=add('Head cheese',hc,H)
cc={'Brawn':'United Kingdom','Potted heid':'United Kingdom','Fromage de tête':'France','Sülze':'Germany','Salceson':'Poland','Tlačenka':'Czech Republic','Disznósajt':'Hungary','Coppa di testa':'Italy','Souse':'Caribbean','Queso de puerco':'Mexico'}
setg('Head cheese',cc)
k=K['Head cheese'][2]; k['xg']='country'; sortg('Head cheese')
k['sel']=f"Follows the named head cheeses of {H}. Covers {len(k['x'])} of about 105 rows in that page (read whole); the rest are alternative local-language names and spellings of an entry already listed, or regional names in the Americas and the Netherlands for the same product."
# ---- new kinds
def newkind(shelf_name,kind):
    for dp in d['depts']:
        for s in dp['s']:
            if s['n']==shelf_name: s['k'].append(kind); return
    raise Exception(shelf_name)
newkind('Lamb cuts',{'n':'Lamb neck, breast & saddle','a':'scrag end · middle neck · breast · saddle · loin roast','d':'Lamb cuts not sold as leg, rack, chops, shoulder or shank: neck, breast, saddle and loin, sold raw.','s':WP+'Cut_of_lamb','tt':[['Cut',['Scrag end','Middle neck','Breast','Saddle','Loin roast','Flank']],['Preparation',['Bone-in','Boneless','Rolled']]]})
newkind('Horse, bison & other mammals',{'n':'Water buffalo','a':'carabeef · buffalo meat · padwa','d':'Meat of the water buffalo, lower in fat than beef and sold under local names such as padwa, pado and carabeef.','s':WP+'Buffalo_meat','tt':[['Age',['Young buffalo (padwa)','Adult']],['Cut',['Steak','Roast','Mince']]]})
newkind('Horse, bison & other mammals',{'n':'Yak','a':'yak meat','d':'Lean meat of the domestic yak, raised in Tibet and Mongolia and bred for lean meat in North America.','s':WP+'Domestic_yak','tt':[['Cut',['Steak','Roast','Mince']]]})
newkind('Birds, reptiles & other creatures',{'n':'Emu','a':'emu meat','d':'Lean red meat of the farmed emu, under 1.5 % fat, farmed in Australia and North America.','s':WP+'Emu','tt':[['Cut',['Fillet','Steak','Mince']]]})
# ---- ms
def addms(dn,fact,summ=None):
    for dp in d['depts']:
        if dp['n']==dn:
            dp.setdefault('ms',[]).append(fact)
            if summ: dp['msum']=(dp.get('msum','')+' '+summ).strip()
addms('Poultry',{'mkt':'World chicken exports','who':'Brazil','share':'36 %','yr':2024,'s':'https://datamarnews.com/noticias/brazil-projected-to-account-for-36-of-worlds-chicken-exports-in-2024/','note':'USDA projection for 2024 reported by Datamar News on 6 November 2023'},'Brazil is projected at 36 % of world chicken exports in 2024 (USDA projection, reported November 2023).')
addms('Other meats',{'mkt':'World buffalo meat production','who':'India','share':'about 43 %','yr':'','s':WP+'Buffalo_meat','note':'the page gives no year for the share'})
addms('Beef & veal',{'mkt':'World meat production (all species)','who':'China, United States, Brazil','share':'97.5, 47.5 and 31.6 million tonnes','yr':2023,'s':WP+'Meat_industry','note':'the three largest producers, together nearly half of world output; volume, not share'},'The Meat industry page puts China, the United States and Brazil as the largest meat producers in 2023.')
# ---- generic coverage lines
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if not k.get('x'): continue
      sel=k.get('sel','')
      if re.search(r'(Complete: \d+ of \d+|Covers \d+ of|No complete list exists)',sel): continue
      m=re.match(r'No whole-space reference was fetched for this kind; entries follow (.*?)\. Not claimed complete\.$',sel)
      if m: k['sel']='No complete list exists; follows '+m.group(1)+'.'
      else:
        m=re.match(r'Follows (.*?)\. Not claimed complete\.$',sel)
        if m: k['sel']='No complete list exists; follows '+m.group(1)+'.'
        elif 'Follows' in sel and not re.search(r'Covers|Complete',sel): print('MANUAL',k['n'],sel)
print(log)
tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,P)
