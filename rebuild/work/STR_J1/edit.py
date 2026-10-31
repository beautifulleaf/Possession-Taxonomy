import json, copy, os, sys
SRC='/home/user/Possession-Taxonomy/rebuild/work/STR_J1/bak/J1.json'
OUT='/home/user/Possession-Taxonomy/rebuild/out/J1.json'
d=json.load(open(SRC))
WP='https://en.wikipedia.org/wiki/'
K={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
before=dict(depts=len(d['depts']),shelves=sum(len(x['s']) for x in d['depts']),kinds=len(K),arch=sum(len(k.get('x',[])) for k in K.values()))

def demote(kn, names):
    k=K[kn]; keep=[]; m=k.setdefault('m',[])
    have={tuple(x) for x in m}
    for x in k.get('x',[]):
        if x['n'] in names:
            for v in x.get('v',[]) or []:
                e=(v['n'],v.get('mk',''))
                if e not in have: m.append(list(e)); have.add(e)
        else: keep.append(x)
    k['x']=keep
    if not m: del k['m']
    if not keep: del k['x']

# ---- demotions (generic species, breeds, duplicates of the kind name) ----
demote('Ibérico pork',{'Iberian pig'})
demote('Whole chicken',{'Ixworth chicken'})
demote('Turkey',{'Bronze turkey','Broad Breasted White','Norfolk Black','Bourbon Red','Narragansett'})
demote('Whole duck',{'American Pekin','Barbary duck','Mulard duck'})
demote('Goose',{'Embden goose','Toulouse goose'})
demote('Foie gras',{'Duck foie gras','Goose foie gras'})
demote('Venison by species',{'Red deer venison','Roe deer venison','Fallow deer venison','Sika venison','Muntjac venison','Axis venison','Reindeer meat','Elk (moose) meat'})
for kn,nm in [('Pheasant',{'Common pheasant'}),('Grouse',{'Red grouse','Black grouse','Ptarmigan'}),('Partridge',{'Red-legged partridge','Grey partridge'}),('Wild duck',{'Mallard','Teal'}),('Pigeon & squab',{'Wood pigeon','Squab'}),('Quail',{'Japanese quail','Common quail'}),('Guinea fowl',{'Helmeted guineafowl'}),('Rabbit',{'Farmed rabbit','Wild rabbit'}),('Hare',{'Brown hare','Mountain hare'}),('Wild boar',{'European wild boar'}),('Squirrel',{'Grey squirrel'}),('Bison',{'Plains bison'}),('Crocodile & alligator',{'Alligator tail meat','Crocodile tail meat'}),('Edible insects',{'EU-authorised insect foods'})]:
    demote(kn,nm)
demote('Merguez',{'Merguez'}); demote('Boerewors',{'Boerewors'}); demote('Toulouse sausage',{'Saucisse de Toulouse'})
demote('Weisswurst',{'Münchner Weißwurst'}); demote('Cervelat',{'Swiss cervelat'}); demote('Biltong & droëwors',{'Biltong','Droëwors'})
demote('Pancetta',{'Pancetta arrotolata','Pancetta tesa'})
demote('Bacon',{'American streaky bacon'})
demote('Italian sausage',{'North American Italian sausage'})
demote('Pepperoni',{'Cup-and-char pepperoni','Flat-lying pizza pepperoni'})
demote('Prepared foie gras',{'Foie gras entier','Foie gras','Bloc de foie gras','Parfait de foie gras','Médaillon or pâté de foie gras','Mousse de foie gras','Galantine de foie gras'})
demote('Confit',{'Confit de canard',"Confit d'oie",'Pork confit'})
demote('Rillettes',{'Duck and goose rillettes'})
demote('Pickled or fermented meat',{'Pickled meat snacks'})
demote('Plant-based meat',{'Plant-based sausage','Plant-based mince','Plant-based chicken'})
demote('Seitan',{'Seitan (macrobiotic)'})
demote('Corned beef & salt beef',{'Salt beef'})
demote('Frankfurter & hot dog',{'American hot dog sausage'})
demoted=True

# ---- tt (hand-written, kind by kind) ----
TT={
'Japanese wagyu':[['Breed',['Japanese Black (kuroge washu)','Japanese Brown (akaushi)','Japanese Polled (mukaku washu)','Japanese Shorthorn (nihon tankaku washu)']]],
'Wagyu outside Japan':[['Blood purity',['Fullblood','Purebred','Crossbred (F1 to F4)']]],
'Breed-branded beef':[['Breed',['Aberdeen Angus','Hereford','Highland','Longhorn','Charolais','Limousin']]],
'Protected-origin beef':[['Designation',['PDO (AOP)','PGI (IGP)']]],
'Ribeye steak':[['Bone',['Boneless','Bone-in','Cowboy cut','Tomahawk']],['Muscle',['Whole ribeye','Ribeye cap (spinalis)']],['Ageing',['Dry-aged']]],
'Sirloin steak (striploin)':[['Regional cut',['New York strip','Kansas City strip']],['Ageing',['Dry-aged']]],
'Fillet steak (tenderloin)':[['Portion',['Whole fillet','Centre cut','Steaks']]],
'T-bone & porterhouse':[['Size of fillet portion',['T-bone','Porterhouse (larger fillet)']],['Regional cut',['Florentine (bistecca alla fiorentina)']],['Ageing',['Dry-aged']]],
'Skirt & flank steak':[['Cut',['Outside skirt','Inside skirt','Flank']]],
'Rib roast':[['Bone',['Bone-in','Boneless','Côte de boeuf (single rib)']],['Ageing',['Dry-aged']]],
'Silverside & eye of round':[['Muscle',['Silverside','Eye of round']]],
'Chuck & blade':[['Cut',['Chuck eye roast','English chuck roast','Blade','Braising steak']]],
'Beef brisket':[['Part',['Whole packer','Point','Flat']]],
'Beef short rib':[['Cut',['English cut','Flanken or galbi cut','Plate short rib',"Jacob's ladder"]]],
'Beef shin':[['Bone',['On the bone','Off the bone']]],
'Beef mince & burgers':[['Fat content',['5%','10%','15%','20%']],['Form',['Steak mince','Burgers','Meatballs']]],
'Veal':[['Cut',['Chop','Escalope','Flank','Osso buco','Loin']],['Rearing',['White veal','Rose veal']]],
'Beef by the quarter or side':[['Portion',['Primal','Quarter','Half','Whole carcass']]],
'Beef & veal offal':[['Organ',['Liver','Tongue','Heart','Kidney','Sweetbreads','Tripe']],['Animal',['Ox','Calf']]],
'Ibérico pork':[['Cut',['Secreto','Presa','Pluma','Lagarto','Abanico','Carrillera (cheek)','Cabecero (collar)','Solomillo (tenderloin)','Costillas (ribs)']],['Feeding',['Bellota (acorn-fed)','Cebo de campo (pastured)','Cebo (grain-fed)']],['Breed',['Iberian pig']]],
'Heritage-breed pork':[['Breed',['Duroc','Tamworth','Large Black']]],
'Suckling pig':[['Portion',['Whole','Half']]],
'Pork loin':[['Cut',['Loin chop','Loin joint','Rack (French-trimmed)','Boneless loin steak']]],
'Pork tenderloin':[['Form',['Whole','Medallions']]],
'Pork shoulder':[['Part',['Whole shoulder','Blade','Picnic']]],
'Pork collar':[['Form',['Joint','Steaks']]],
'Pork leg':[['Form',['Whole leg','Joint','Steaks']]],
'Pork belly':[['Skin',['Skin-on','Skinless']]],
'Pork ribs':[['Cut',['Spare ribs','Baby back ribs','St. Louis cut','Country-style ribs','Rib tips']]],
'Pork mince & burgers':[['Form',['Mince','Burgers','Meatballs']]],
'Pork stomach & offal':[['Organ',['Stomach (maw)','Liver','Kidney','Caul fat','Blood']]],
'Pork by the half or side':[['Portion',['Primal','Half','Whole carcass']]],
'Lamb leg':[['Portion',['Whole','Half (shank end)','Half (fillet end)']],['Preparation',['Butterflied','Boneless']]],
'Lamb rack':[['Trim',['French-trimmed','Crown roast']]],
'Lamb chops':[['Cut',['Loin chop','Cutlet','Barnsley chop','Chump chop']]],
'Lamb shoulder':[['Bone',['Bone-in','Boneless']]],
'Protected-origin & breed lamb':[['Designation',['PDO','PGI','Label Rouge']]],
'Suckling lamb':[['Portion',['Whole','Half','Leg']]],
'Mutton & hogget':[['Age',['Hogget','Mutton']],['Portion',['Whole lamb','Half lamb']]],
'Goat & kid':[['Age',['Kid (cabrito)','Adult goat']],['Cut',['Whole or half','Leg','Chops','Shank','Shoulder','Diced']]],
'Goat mince & burgers':[['Form',['Mince','Burgers']]],
'Whole chicken':[['Farming',['Standard','Free-range','Organic','Corn-fed']],['Age and size',['Poussin','Poularde','Capon']],['Breed',['Ixworth']]],
'Chicken breast':[['Cut',['Supreme (wing bone on)','Fillet','Mini fillets','On the bone']]],
'Chicken leg & thigh':[['Cut',['Leg quarter','Thigh','Drumstick']]],
'Chicken wings':[['Cut',['Whole wing','Flats','Drumettes']]],
'Poultry mince & burgers':[['Bird',['Chicken','Turkey','Duck']],['Form',['Mince','Burgers']]],
'Poultry offal':[['Part',['Livers','Gizzards','Hearts','Necks','Mixed giblets']]],
'Turkey':[['Cut',['Whole bird','Crown','Breast joint','Thigh roast','Legs']],['Breed',['Bronze','Broad Breasted White','Norfolk Black','Bourbon Red','Narragansett']]],
'Whole duck':[['Preparation',['Oven-ready','With giblets']],['Breed',['American Pekin','Barbary','Mulard']]],
'Duck breast':[['Breed',['Pekin (Long Island)','Barbary']]],
'Duck leg':[['Breed',['Pekin','Moulard or Barbary']]],
'Goose':[['Cut',['Whole oven-ready (Christmas goose)','Breast','Leg']],['Breed',['Embden','Toulouse']]],
'Foie gras':[['Bird',['Duck','Goose']],['Form',['Whole raw lobe']],['Grade',['Grade A','Grade B','Grade C']]],
'Venison by species':[['Species',['Red deer','Roe deer','Fallow deer','Sika deer','Muntjac','Axis deer','Reindeer','Elk (moose)']],['Source',['Wild','Farmed','Park']]],
'Venison haunch':[['Cut',['Whole haunch on the bone','Boned and rolled joint','Haunch steaks','Denver leg (boned-out leg muscles)']]],
'Venison saddle & loin':[['Cut',['Saddle on the bone','Loin','Medallions']]],
'Venison rack':[['Trim',['French-trimmed rack','Chops']]],
'Venison mince & burgers':[['Form',['Mince','Burgers','Meatballs','Mince with added fat']]],
'Pheasant':[['Preparation',['Whole oven-ready','In feather','Breasts']],['Sold as',['Single bird','Brace (cock and hen)']],['Species',['Common pheasant']]],
'Grouse':[['Preparation',['Whole oven-ready','In feather','Breasts']],['Species',['Red grouse','Black grouse','Ptarmigan']]],
'Partridge':[['Preparation',['Whole oven-ready','In feather','Breasts']],['Species',['Red-legged partridge','Grey partridge']]],
'Wild duck':[['Species',['Mallard','Teal','Wigeon']],['Preparation',['Whole oven-ready','Breasts']]],
'Pigeon & squab':[['Bird',['Wood pigeon','Squab (pigeonneau)']],['Preparation',['Whole','Breasts']]],
'Quail':[['Species',['Japanese quail','Common quail']],['Preparation',['Whole','Spatchcocked','Boned']]],
'Guinea fowl':[['Preparation',['Whole','Supremes','Legs']],['Species',['Helmeted guineafowl']]],
'Rabbit':[['Source',['Farmed','Wild']],['Cut',['Whole','Jointed','Saddle','Legs']]],
'Hare':[['Species',['Brown hare','Mountain hare']],['Preparation',['Whole in fur','Oven-ready','Saddle','Legs']]],
'Wild boar':[['Source',['Wild-shot','Farmed']],['Cut',['Leg','Shoulder','Loin','Rack']],['Species',['European wild boar']]],
'Squirrel':[['Species',['Grey squirrel']]],
'Jamón ibérico':[['Feeding',['Bellota (acorn-fed)','Cebo de campo (pastured)','Cebo (grain-fed)']],['Form',['Whole on the bone','Boneless','Hand-sliced']]],
'Prosciutto crudo':[['Form',['Whole on the bone','Boneless','Pre-sliced']]],
'Jamón serrano':[['Form',['Whole on the bone','Boneless','Sliced']]],
'Pancetta':[['Style',['Arrotolata (rolled)','Tesa (flat)','Affumicata (smoked)']],['Form',['Cubed','Sliced']]],
'Cured pork loin (lomo)':[['Pig',['Ibérico de bellota','Serrano']],['Form',['Whole','Sliced']]],
'Lap yuk':[['Form',['Skin-on strips']],['Smoking',['Smoked']]],
'Bacon':[['Cut',['Back','Streaky','Middle','Collar']],['Smoking',['Smoked','Unsmoked (green)']],['Cure',['Dry-cured','Wet-cured']],['Form',['Rashers','Lardons','Piece']]],
'Gammon':[['Form',['Joint','Steak']],['Bone',['Bone-in','Boneless']],['Smoking',['Smoked','Unsmoked']],['Cure',['Dry-cured','Wet-cured']]],
'Cooked ham':[['Form',['On the bone','Boneless','Formed','Sliced']],['Finish',['Glazed']],['Smoking',['Smoked','Unsmoked']]],
'Corned beef & salt beef':[['Cut',['Brisket','Silverside','Round']],['State',['Raw to cook','Cooked','Sliced']]],
'Pastrami & smoked meat':[['Meat',['Beef navel','Beef brisket','Turkey']],['Form',['Whole','Sliced']]],
'Cooked cured tongue':[['Animal',['Ox','Pork']],['Form',['Pressed','Sliced']]],
'Jerky':[['Meat',['Beef','Turkey','Pork','Game']],['Style',['Smoked','Marinated']],['Form',['Sticks','Slabs']]],
'Biltong & droëwors':[['Meat',['Beef','Game','Ostrich']],['Form',['Sliced','Sticks']],['Flavour',['Chilli']]],
'Bakkwa':[['Meat',['Pork','Beef']],['Flavour',['Chilli']],['Form',['Sliced','Minced']]],
'British sausage':[['Meat',['Pork','Beef']],['Flavour',['Herb']],['Casing',['Skinless']]],
'Bratwurst':[['State',['Fresh','Pre-cooked']]],
'Italian sausage':[['Form',['Links','Coil','Loose sausagemeat']],['Seasoning',['Mild','Sweet (basil)','Hot (red pepper flakes)']]],
'Breakfast sausage':[['Form',['Links','Patties','Loose']],['Seasoning',['Maple','Sage','Hot']]],
'Merguez':[['Meat',['Lamb','Beef','Lamb and beef']]],
'Fresh chorizo & longaniza':[['Form',['Links','Loose']]],
'Frankfurter & hot dog':[['Casing',['Natural casing','Skinless']],['Meat',['All-beef','Pork and beef','Chicken or turkey']],['Pack',['Tinned']],['Certification',['Kosher']]],
'Kielbasa & smoked sausage':[['Shape',['Ring','Links']],['Meat',['Pork','Beef','Turkey']]],
'Mortadella & bologna':[['Form',['Whole','Sliced']],['Flavour',['With pistachio','Plain']]],
'Liver sausage':[['Texture',['Spreadable','Sliceable','Coarse','Fine']],['Smoking',['Smoked']]],
"Saucisson à l'ail":[['Smoking',['Smoked']]],
'Italian salame':[['Form',['Whole','Pre-sliced','Salametti']]],
'Saucisson sec':[['Flavouring',['Plain','With herbs','With nuts','With cheese']]],
'Fuet & salchichón':[['Form',['Whole','Pre-sliced']],['Pig',['Ibérico']]],
'Chorizo':[['Heat',['Dulce (sweet)','Picante (hot)']],['Shape',['Sarta (horseshoe)','Vela (straight)']],['Form',['Sliced']]],
'Pepperoni':[['Form',['Stick','Sliced']],['Style',['Cup-and-char','Flat-lying pizza pepperoni']],['Meat',['Turkey']]],
'Pâtés and terrines':[['Texture',['Fine','Coarse']],['Form',['Pâté','Terrine']],['Pack',['Tinned','Sliced']]],
'Rillettes':[['Meat',['Pork','Duck','Goose','Rabbit','Chicken']]],
'Prepared foie gras':[['Bird',['Duck (canard)','Goose (oie)']],['Cooking',['Mi-cuit','Cuit (tin or jar)','Cru (raw)']],['Preparation',['Foie gras entier','Bloc de foie gras','Parfait','Médaillon or pâté','Mousse','Galantine']]],
'Confit':[['Part',['Legs','Gizzards','Whole bird']],['Meat',['Duck','Goose','Pork']]],
'Cooked sliced roast meat':[['Meat',['Roast beef','Roast turkey','Roast pork']]],
'Horse meat':[['Cut',['Ribeye steak','Sirloin steak','Tenderloin','Flank steak','Mince']]],
'Bison':[['Cut',['Steak','Roast','Mince']],['Finish',['Grass-finished','Grain-finished']],['Species',['Plains bison']]],
'Kangaroo':[['Species',['Red kangaroo','Eastern grey','Western grey','Common wallaroo']],['Form',['Fillet','Steak','Mince','Sausages']]],
'Ostrich':[['Cut',['Fillet','Steak','Mince']]],
'Crocodile & alligator':[['Animal',['Alligator','Crocodile']],['Cut',['Tail meat','Body meat','Jaw meat','Ribs']]],
'Camel':[['Cut',['Hump','Brisket','Ribs','Loin','Mince']]],
"Frogs' legs":[['State',['Fresh','Frozen']]],
'Edible insects':[['Species',['House cricket (Acheta domesticus)','Yellow mealworm (Tenebrio molitor)','Migratory locust (Locusta migratoria)','Lesser mealworm (Alphitobius diaperinus)']],['Form',['Frozen','Dried','Powder']]],
'Meat box':[['Format',['One-off box','Subscription']],['Contents',['BBQ box','Family box']]],
'Charcuterie & deli selection':[['Contents',['Cured selection','Sausage selection','Cooked deli platter']]],
'Plant-based meat':[['Product',['Burger','Mince','Sausage','Chicken-style pieces','Nuggets','Bacon-style','Deli slices','Roast','Meatballs','Steak','Fish and seafood style']],['Protein',['Pea','Soy','Wheat']],['Storage',['Chilled','Frozen']]],
'Mycoprotein':[['Product',['Mince','Pieces','Sausages','Nuggets','Fillets','Burgers']],['Binder',['Egg white (vegetarian)','Potato protein (vegan)']]],
'Seitan':[['Form',['Block','Sliced','Marinated','In broth','Dried','Vital wheat gluten mix']]],
}
for kn,tt in TT.items():
    if kn in K:
        K[kn]['tt']=tt; K[kn].pop('t',None)
# ---- new kinds ----
def NK(n,a,dd,s,tt=None,x=None,see=None):
    k={'n':n,'a':a,'d':dd,'s':s}
    if tt: k['tt']=tt
    if x: k['x']=x
    K[n]=k; return k
CB=WP+'Cut_of_beef'
# reshape minor grilling steaks
mg=K.pop('Minor grilling steaks')
rump=mg; rump['n']='Rump steak'; rump['a']='rump (UK, AU) · top sirloin (US) · rumsteck · aiguillette baronne · bottom sirloin · butler\'s steak'
rump['d']='A flavourful, lean steak cut from the hindquarter above the leg, sold thick for pan-frying or grilling.'; rump.pop('t',None); rump['s']=CB; K['Rump steak']=rump
NK('Tri-tip','Santa Maria steak · triangle roast · bottom sirloin','A triangular muscle from the bottom sirloin, grilled whole or sliced across the grain.',CB)
NK('Skirt & flank steak','bavette · London broil (flank) · arrachera · entraña · onglet','Long, grainy muscles from the plate and flank, marinated and cooked fast, then sliced across the grain.',CB,TT['Skirt & flank steak'])
NK('Flat iron & hanger steak','top blade · butcher\'s steak · onglet (hanger)','Two tender, well-marbled steaks, flat iron from the shoulder blade and hanger from near the diaphragm.',CB)
NK('Cotechino','cotechino modena · zampone (trotter-cased)','Fresh Italian pork sausage with rind and spices, sold raw or pre-cooked and simmered, traditionally with lentils.',WP+'List_of_sausages',[['Casing',['Gut casing','Pig trotter (zampone)']],['State',['Raw','Pre-cooked']]])
NK('Thai & Southeast Asian sausage','sai ua · Chiang Mai sausage','Fresh herb-heavy pork sausages from Thailand and its neighbours, grilled whole.',WP+'List_of_sausages',None,[{'n':'Sai ua','a':'Chiang Mai sausage','d':'Northern Thai grilled pork sausage with red curry paste, lemongrass and kaffir lime.','mk':'','y':'','s':WP+'List_of_sausages','v':[]}])
NK('Saveloy','saveloy · chip-shop sausage','Bright red, fully cooked pork sausage, boiled or deep-fried, a British chip-shop staple.',WP+'List_of_sausages')
NK('Linguiça & Portuguese smoked sausage','linguiça · chouriço de carne','Garlicky, paprika-seasoned smoked pork sausage of Portugal and its former colonies.',WP+'List_of_sausages',None,[{'n':'Linguiça','a':'','d':'Portuguese smoked pork sausage, grilled or used in stews.','mk':'','y':'','s':WP+'List_of_sausages','v':[]}])
NK('Chả lụa','Vietnamese pork roll · giò lụa','Finely pounded steamed pork roll wrapped in banana leaf, sliced cold.',WP+'List_of_sausages')
NK('Balkan & Baltic dry sausage','kulen · lukanka · skilandis','Heavily seasoned, air-dried and sometimes smoked sausages of south-east and eastern Europe.',WP+'List_of_sausages',None,[
 {'n':'Kulen','a':'kulin','d':'Spicy paprika dry sausage from Croatia and Serbia, long-cured.','mk':'','y':'','s':WP+'List_of_sausages','v':[]},
 {'n':'Lukanka','a':'','d':'Flat, pressed Bulgarian dry salami seasoned with cumin and pepper.','mk':'','y':'','s':WP+'List_of_sausages','v':[]},
 {'n':'Skilandis','a':'','d':'Lithuanian smoked sausage stuffed into a pig stomach.','mk':'','y':'','s':WP+'List_of_sausages','v':[]}])
NK('Tinned sausages','Vienna sausages · tinned frankfurters','Short, fully cooked smoked sausages packed in a can with brine, jelly or sauce.',WP+'Vienna_sausage')
NK('Potted meat & devilled ham','potted meat · meat spread · deviled ham','Cooked, finely ground meat packed in small cans or jars and spread on bread.',WP+'Canned_meat')
# new hams as archetypes on regional dry-cured hams
rh=K['Regional dry-cured hams']
names={x['n'] for x in rh['x']}
for n,dd in [('Xuanwei ham','Chinese dry-cured ham from Yunnan, salted and aged for months.'),('Njeguški pršut','Dry-cured ham from the Njeguši area of Montenegro, smoked over beech.'),('Lacón gallego','Cured pork foreleg from Galicia, boiled before eating.'),('Anfu ham','Chinese dry-cured ham from Jiangxi.'),('Elenski but','Bulgarian dry-cured pork leg from the Elena area.')]:
    if n not in names: rh['x'].append({'n':n,'a':'','d':dd,'mk':'','y':'','s':WP+'List_of_hams','v':[]})
# ---- see links ----
SEE={
'Foie gras':[['J1','Prepared foie gras','the same liver sold cooked']],
'Prepared foie gras':[['J1','Foie gras','the raw liver to cook at home']],
'Rillettes':[['J2','Fish pâté & rillettes','the same spread made with fish']],
'Pâtés and terrines':[['J2','Fish pâté & rillettes','the same spread made with fish']],
'Pork belly':[['J1','Pancetta','cured belly'],['J1','Bacon','cured and smoked belly'],['J8','Pork scratchings & chicharrón','fried pork rind snack']],
'Pancetta':[['J1','Pork belly','the fresh cut']],
'Pork jowl & cheek':[['J1','Guanciale','cured jowl']],
'Guanciale':[['J1','Pork jowl & cheek','the fresh cut']],
'Pork collar':[['J1','Coppa','cured collar']],
'Coppa':[['J1','Pork collar','the fresh cut']],
'Pork leg':[['J1','Gammon','brined leg'],['J1','Prosciutto crudo','dry-cured leg']],
'Gammon':[['J1','Cooked ham','cooked and sliced leg'],['J1','Pork leg','the fresh cut']],
'Cooked ham':[['J1','Gammon','the joint cooked at home']],
'Beef brisket':[['J1','Corned beef & salt beef','brined brisket'],['J1','Pastrami & smoked meat','smoked brisket']],
'Corned beef & salt beef':[['J1','Tinned corned beef','the tinned form'],['J1','Beef brisket','the fresh cut']],
'Tinned corned beef':[['J1','Corned beef & salt beef','the fresh-cured form']],
'Pastrami & smoked meat':[['J1','Beef brisket','the fresh cut']],
'Jerky':[['J1','Biltong & droëwors','South African air-dried meat'],['J8','Protein snack','packaged meat snacks']],
'Biltong & droëwors':[['J1','Jerky','dried in strips, often smoked']],
'Duck leg':[['J1','Confit','the leg cooked in its fat']],
'Confit':[['J1','Duck leg','the fresh leg']],
'Air-dried beef (bresaola)':[['J1','Jerky','dried beef in strips']],
'Cured pork loin (lomo)':[['J1','Pork loin','the fresh cut']],
'Chinese sausage':[['J1','Chả lụa','Vietnamese cooked pork roll']],
'Suckling pig':[['J1','Suckling lamb','the lamb equivalent']],
'Suckling lamb':[['J1','Suckling pig','the pig equivalent']],
'Frankfurter & hot dog':[['J1','Tinned sausages','the tinned form']],
'Tinned sausages':[['J1','Frankfurter & hot dog','the fresh-packed form']],
'Seitan':[['J3','Tofu','another plant protein block']],
'Plant-based meat':[['J3','Tofu','plant protein not made to imitate meat']],
'Venison by species':[['J1','Wild boar','other large game']],
'Goat & kid':[['J1','Lamb leg','the closest everyday red meat']],
'Oxtail':[['J1','Beef shin','another bone-in braising cut']],
'Veal':[['J1','Beef & veal offal','calf organ meats']],
}
for kn,sv in SEE.items(): K[kn]['see']=sv

# ---- layout ----
def kinds(*names):
    out=[]
    for n in names:
        if n not in K: raise SystemExit('missing kind '+n)
        out.append(K[n])
    return out
def shelf(n,t,ax,*names):
    s={'n':n,'t':t,'k':kinds(*names)}
    if ax: s['ax']=ax
    return s
def dept(n,t,ax,shelves):
    od=[x for x in d['depts'] if x['n']==n][0]
    nd={'n':n,'mode':od['mode'],'t':t,'ax':ax}
    for f in ('note','b'):
        if f in od: nd[f]=od[f]
    nd['s']=shelves; return nd

D=[]
D.append(dept('Beef & veal',
 'Meat from cattle, sold under a named origin or breed, or as cuts for grilling, roasting, slow-cooking or mincing, plus veal and offal; cooked or cured beef → Ham, bacon & cured meats or Deli, cooked & tinned meats.',
 'Is it chosen by named origin or breed, or by the cut and the cooking it suits (grill, roast, slow-cook, grind), or is it veal or offal?',
 [shelf('Graded & branded beef','Beef sold under a protected place name, a breed society scheme or a grading system, such as Kobe beef, Certified Angus Beef or Scotch Beef PGI; an ordinary cut without a brand → the cut shelves.','kinds by who certifies the beef: Japanese wagyu, wagyu raised elsewhere, breed schemes, protected places','Japanese wagyu','Wagyu outside Japan','Breed-branded beef','Protected-origin beef'),
  shelf('Steaks','Cuts sliced for quick frying or grilling, such as ribeye, sirloin, fillet and rump; a thick roasting piece → Roasting joints.','kinds by where on the animal, from the rib through the loin and rump to the shoulder and belly muscles','Ribeye steak','T-bone & porterhouse','Sirloin steak (striploin)','Fillet steak (tenderloin)','Rump steak','Rump cap (picanha)','Tri-tip','Flat iron & hanger steak','Skirt & flank steak'),
  shelf('Roasting joints','Large lean or well-covered pieces cooked in the oven, such as rib roast, topside and silverside; tougher cuts cooked in liquid → Braising & slow-cook cuts.',None,'Rib roast','Topside & top round','Silverside & eye of round'),
  shelf('Braising & slow-cook cuts','Tougher, collagen-rich cuts cooked long and slow, such as chuck, brisket, short rib, shin and oxtail; brined brisket → Corned beef & salt beef.','kinds from shoulder to belly to leg: chuck, brisket, short rib, shin, oxtail','Chuck & blade','Beef brisket','Beef short rib','Beef shin','Oxtail'),
  shelf('Veal','Meat from young calves, sold as chops, escalopes and osso buco; adult beef → the cut shelves.',None,'Veal'),
  shelf('Mince, offal & bulk','Beef sold ground, as organ meat or by the quarter or side for the freezer.',None,'Beef mince & burgers','Beef & veal offal','Beef by the quarter or side')]))
D.append(dept('Pork',
 'Meat from pigs, sold as breed-named pork or as cuts for roasting, grilling, slow-cooking or mincing; cured, smoked or cooked pork → Ham, bacon & cured meats, Sausages & salami or Deli, cooked & tinned meats.',
 'Is it chosen by named breed, or by the cut and the cooking it suits (roast, chop, slow-cook, grind)?',
 [shelf('Breed & Ibérico pork','Pork sold under a breed or label name, such as Ibérico, Berkshire (Kurobuta) or Mangalitsa, and young pigs sold whole.',None,'Ibérico pork','Heritage-breed pork','Suckling pig'),
  shelf('Chops & roasting joints','Lean and meaty cuts from the back and legs, such as loin, tenderloin, shoulder, collar and leg.','kinds from loin to shoulder to leg: loin, tenderloin, shoulder, collar, leg','Pork loin','Pork tenderloin','Pork shoulder','Pork collar','Pork leg'),
  shelf('Belly, ribs & extremities','Fatty and bony cuts for slow roasting, barbecue and stock, such as belly, ribs, hock, jowl and trotter.','kinds from belly to ribs to head and feet','Pork belly','Pork ribs','Pork hock','Pork jowl & cheek','Pork trotter'),
  shelf('Mince, offal & bulk','Pork sold ground, as organ meat or by the half or side for the freezer.',None,'Pork mince & burgers','Pork stomach & offal','Pork by the half or side')]))
D.append(dept('Lamb & goat',
 'Meat from sheep and goats, sold as lamb cuts, protected-origin or breed lamb, older mutton, or goat; cured or cooked lamb → Deli, cooked & tinned meats.',
 'Is it lamb sold by the cut, lamb or mutton sold by origin and age, or goat?',
 [shelf('Lamb cuts','Cuts of young sheep, such as leg, rack, chops, shoulder and shank.','kinds from leg to rack to chops to shoulder to shank','Lamb leg','Lamb rack','Lamb chops','Lamb shoulder','Lamb shank'),
  shelf('Protected & breed lamb','Sheep meat sold by grazing, origin or age, such as salt-marsh lamb, Herdwick, milk-fed lamb and mutton.','kinds by what sets the meat apart: salt-marsh grazing, protected place, milk feeding, older age','Salt-marsh lamb','Protected-origin & breed lamb','Suckling lamb','Mutton & hogget'),
  shelf('Goat','Meat from goats and kids, sold whole, jointed or minced.',None,'Goat & kid','Goat mince & burgers')]))
D.append(dept('Poultry',
 'Chicken, turkey, duck and goose sold fresh or frozen as whole birds, joints, mince or liver; cooked or cured birds → Deli, cooked & tinned meats; wild birds → Game.',
 'Which farmed bird is it, and is it sold whole or in joints, or as mince, offal or liver?',
 [shelf('Chicken','Whole chickens and their joints, such as breast, leg and wings; minced poultry → Mince, offal & liver.','kinds from the whole bird to its joints: whole, breast, leg, wings','Whole chicken','Chicken breast','Chicken leg & thigh','Chicken wings'),
  shelf('Turkey, duck & goose','Larger farmed birds sold whole or in joints, such as turkey, Aylesbury duck, duck breast and goose.','kinds by bird, then by joint: turkey, duck whole then breast then leg, goose','Turkey','Whole duck','Duck breast','Duck leg','Goose'),
  shelf('Mince, offal & liver','Poultry sold ground, as giblets or as fattened liver (foie gras).',None,'Poultry mince & burgers','Poultry offal','Foie gras')]))
D.append(dept('Game',
 'Wild or farmed-wild animals and birds hunted for the table, such as venison, pheasant, rabbit and wild boar; domestic poultry → Poultry, other farmed meat → Other meats.',
 'Is it a hoofed animal, a bird, or a rabbit, hare or other small game?',
 [shelf('Venison & wild boar','Deer meat and wild pig, sold as whole carcass, haunch, saddle, fillet, rack or mince.','kinds from whole animal to cuts: species, haunch, saddle, fillet, rack, mince, then wild boar','Venison by species','Venison haunch','Venison saddle & loin','Venison fillet','Venison rack','Venison mince & burgers','Wild boar'),
  shelf('Game birds','Wild birds shot for eating, such as pheasant, grouse, partridge, wild duck, pigeon, quail and guinea fowl.','kinds from the classic shoot birds to duck, pigeon and the farmed small birds: pheasant, grouse, partridge, duck, pigeon, quail, guinea fowl','Pheasant','Grouse','Partridge','Wild duck','Pigeon & squab','Quail','Guinea fowl'),
  shelf('Rabbit, hare & small game','Small wild mammals hunted or farmed for meat, such as rabbit, hare and squirrel.',None,'Rabbit','Hare','Squirrel')]))
D.append(dept('Ham, bacon & cured meats',
 'Pork, beef and game preserved by salting, brining, smoking or drying, such as jamón, bacon, bresaola and jerky; sausages → Sausages & salami; cooked spreads and tinned meat → Deli, cooked & tinned meats.',
 'How was the meat preserved: dry-cured as a whole leg, cured as a whole muscle or belly, brined and cooked, or dried and fermented in strips?',
 [shelf('Dry-cured hams','Whole pork legs salted and air-dried for months, such as jamón ibérico, Parma ham and Jinhua ham; a cooked ham → Bacon, cooked ham & brined meats.','kinds by tradition: Iberian, Italian, other regions, smoked','Jamón ibérico','Jamón serrano','Cured shoulder (paleta)','Prosciutto crudo','Regional dry-cured hams','Smoked raw ham'),
  shelf('Cured whole muscles & lardo','Single cuts other than the leg, cured and dried, such as pancetta, guanciale, coppa, bresaola and lardo.','kinds by cut, from belly and jowl to neck, loin, beef and back fat','Pancetta','Guanciale','Coppa','Cured pork loin (lomo)','Air-dried beef (bresaola)','Lardo','Lap yuk'),
  shelf('Bacon, cooked ham & brined meats','Meat cured in brine or salt and eaten cooked, such as bacon, gammon, ham, corned beef and pastrami.','kinds from pork to beef to tongue: bacon, gammon, cooked ham, corned beef, pastrami, tongue','Bacon','Gammon','Cooked ham','Corned beef & salt beef','Pastrami & smoked meat','Cooked cured tongue'),
  shelf('Dried & fermented meats','Meat dried in strips or pieces, or soured, such as jerky, biltong, bakkwa and nem chua.','kinds by tradition: American, South African, Chinese, South-East Asian','Jerky','Biltong & droëwors','Bakkwa','Pickled or fermented meat')]))
D.append(dept('Sausages & salami',
 'Ground meat stuffed into a casing and sold as sausage, pudding or salami; whole-muscle cured meats → Ham, bacon & cured meats; a loose pâté → Deli, cooked & tinned meats.',
 'How is the sausage ready to eat: sold raw to be cooked, already cooked or smoked, or dry-cured to eat cold?',
 [shelf('Fresh sausages','Raw sausages sold to be fried, grilled or simmered, such as British bangers, bratwurst, Italian sausage and merguez.','kinds by tradition: British, German, Italian, American, French, North African, South African, Latin American, Asian','British sausage','Bratwurst','Italian sausage','Cotechino','Breakfast sausage','Toulouse sausage','Merguez','Boerewors','Fresh chorizo & longaniza','Thai & Southeast Asian sausage'),
  shelf('Cooked & smoked sausages','Sausages cooked, scalded or smoked at the factory, such as frankfurters, kielbasa, mortadella and black pudding; dry salami → Salami & dry sausages.','kinds from smoked links to emulsified, liver and blood sausages: frankfurter, kielbasa, saveloy, white and cervelat, mortadella, liver, blood, white pudding, andouille','Frankfurter & hot dog','Kielbasa & smoked sausage','Linguiça & Portuguese smoked sausage','Saveloy','Weisswurst','Cervelat',"Saucisson à l'ail",'Mortadella & bologna','Chả lụa','Liver sausage','Black pudding','White pudding','Andouillette & andouille'),
  shelf('Salami & dry sausages','Sausages fermented and air-dried until firm enough to eat cold, such as Italian salame, saucisson sec, chorizo and pepperoni.','kinds by tradition: Italian, French, Spanish, central European, Balkan, Turkish, American, Chinese','Italian salame','Saucisson sec','Fuet & salchichón','Chorizo','Spreadable raw sausage','Hungarian salami','Balkan & Baltic dry sausage','Sucuk','Pepperoni','Chinese sausage','Kabanos & snack sticks')]))
D.append(dept('Deli, cooked & tinned meats',
 'Meat already cooked or potted for eating cold or heating, such as pâté, rillettes, confit, roast slices, luncheon meat and tinned corned beef; raw cuts → the animal departments.',
 'Is it a French-style cooked spread or confit, or an everyday cooked or tinned meat?',
 [shelf('Pâtés, terrines & confit','Cooked meat spreads and preserved birds in the French charcuterie tradition: pâté, rillettes, foie gras, confit and brawn.','kinds from smooth spreads to potted and preserved pieces: pâté, foie gras, rillettes, brawn, confit','Pâtés and terrines','Prepared foie gras','Rillettes','Head cheese','Confit'),
  shelf('Cooked & tinned meats','Ready-cooked meats sold from the deli counter or in cans, such as rotisserie chicken, sliced roast beef, luncheon meat and tinned corned beef.','kinds from freshly cooked to tinned: rotisserie chicken, sliced roast, meatballs, luncheon meat, corned beef, sausages, potted meat','Rotisserie chicken','Cooked sliced roast meat','Cooked meatballs & patties','Luncheon meat','Tinned corned beef','Tinned sausages','Potted meat & devilled ham')]))
D.append(dept('Other meats',
 'Less common meats and mixed meat boxes: horse, bison, kangaroo, ostrich, crocodile, frogs and insects; goat → Lamb & goat, rabbit and wild birds → Game.',
 'Is it a large mammal, a bird, reptile, amphibian or insect, or a mixed selection of meats?',
 [shelf('Horse, bison & other mammals','Red meat from mammals other than cattle, pigs, sheep, goats and deer, such as horse, bison, kangaroo and camel.','kinds from the most eaten to the least: horse, bison, kangaroo, camel','Horse meat','Bison','Kangaroo','Camel'),
  shelf('Birds, reptiles & other creatures','Meat from ostrich, crocodile, frogs, turtle and edible insects.','kinds from bird to reptile to amphibian to insect: ostrich, crocodile, frogs, turtle, insects','Ostrich','Crocodile & alligator',"Frogs' legs",'Turtle meat','Edible insects'),
  shelf('Boxes & selections','Mixed packs of different meats sold together as a box or platter.',None,'Meat box','Charcuterie & deli selection')]))
D.append(dept('Meat alternatives',
 'Foods made from plants, fungus or wheat gluten to stand in for meat, such as plant-based burgers, Quorn and seitan; tofu and tempeh → Dairy-free alternatives and Tofu, tempeh & yuba.',
 'What is the protein made from: plants (soy, pea), a fungus, or wheat gluten?',
 [shelf('Meat alternatives','Meat-style products that contain no meat.',None,'Plant-based meat','Mycoprotein','Seitan')]))

used={k['n'] for dp in D for s in dp['s'] for k in s['k']}
left=set(K)-used
if left: print('UNPLACED',left)
d['depts']=D
d['ax']='Which animal does the meat come from, and is it sold fresh as a cut or preserved, cooked or made into a product?'
d['key']=[
 '1. Is it made from plants, fungus or wheat gluten to stand in for meat? → Meat alternatives',
 '2. Is it ground meat in a casing, sold as a sausage, pudding or salami? → Sausages & salami',
 '3. Is it a pâté, rillette, confit, tinned meat or other ready-cooked meat? → Deli, cooked & tinned meats',
 '4. Is it a ham, bacon, cured muscle or dried meat? → Ham, bacon & cured meats',
 '5. Is it fresh or frozen beef or veal? → Beef & veal',
 '6. Is it fresh or frozen pork? → Pork',
 '7. Is it fresh or frozen lamb, mutton or goat? → Lamb & goat',
 '8. Is it a farmed chicken, turkey, duck or goose, or its liver? → Poultry',
 '9. Is it a hunted deer, wild bird, hare, rabbit or boar? → Game',
 '10. Is it horse, bison, kangaroo, crocodile, insects or a mixed meat box? → Other meats',
 '<i>Precedence: preserving or cooking beats the animal, so a cured pork leg is a ham (step 4) before it is pork (step 6); a sausage is a sausage (step 2) whatever the meat; foie gras is poultry (step 8) when raw and deli (step 3) when prepared.</i>']
d['lead']='Meat and poultry a household buys, by animal (beef, pork, lamb and goat, poultry, game, other meats) and then by preserved form (cured hams and whole muscles, sausages by tradition, deli and tinned meats), with cuts under their regional names and graded, breed and protected-origin products as archetypes.'
after=dict(depts=len(D),shelves=sum(len(x['s']) for x in D),kinds=len(K),arch=sum(len(k.get('x',[])) for k in K.values()))
print(before,after)
tmp=OUT+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,OUT)
json.dump({'Minor grilling steaks':'Rump steak'},open('/home/user/Possession-Taxonomy/rebuild/out/J1_renames.json','w'),ensure_ascii=False,indent=1)
