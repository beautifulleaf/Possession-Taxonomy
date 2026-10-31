DL=WP+'List_of_daggers'
# Daggers
add('Dagger',rows("""Bronze Age dagger|Early dagger cast in bronze.|Ancient
Parazonium|Short ancient dagger or sword carried by Greek and Roman officers.|Ancient
Sica|Curved single-edged ancient blade of the Thracians and Romans.|Ancient
Knightly dagger|Dagger carried by a knight in the High Middle Ages.|High Middle Ages
Anelace|Long English dagger of the 14th century worn as an accoutrement.|Late Middle Ages|14th c.
Poignard|Slender thrusting dagger of the Late Middle Ages and later.|Late Middle Ages
Hunting dagger|German hunting dagger of the 18th century.|Early modern|18th c.
Bebut|Dagger of the Caucasus and Russia.|Early modern
Main gauche|Left-hand parrying dagger of rapier fencing.|Early modern""",DL))
for x in KIND['Dagger']['x']:
    if x['n']=='Main gauche': x['d']='Left-hand parrying dagger of rapier fencing; a form of parrying dagger.'
setg('Dagger',None,{'Pugio':'Ancient','Rondel dagger':'Late Middle Ages','Baselard':'Late Middle Ages','Bollock dagger':'Late Middle Ages','Misericorde':'Late Middle Ages','Cinquedea':'Renaissance','Ear dagger':'Late Middle Ages','Stiletto':'Renaissance','Parrying dagger':'Early modern','Scottish dirk':'Early modern','Khanjar':'Asian tradition','Khanjali':'Asian tradition','Pesh-kabz':'Asian tradition','Fairbairn–Sykes fighting knife':'20th century'})
KIND['Dagger']['nl']="One entry is a named dagger form of Europe, the ancient Mediterranean or the 20th-century military; marks and famous patterns are versions."
KIND['Dagger']['sel']="European and ancient daggers named in Wikipedia's List of daggers, Asian and African forms being in their own kinds; the Fairbairn–Sykes knife is the one military pattern kept here."
KIND['Dagger']['xg']='by period'
dropm('Dagger','Main gauche became an entry; the retail Benchmade SOCP Dagger removed as a retail model')
newkind('Daggers & fighting knives','Asian dagger','kard · kirpan · kujang','Dagger of Asia and the Middle East of Asia.',DL)
add('Asian dagger',rows("""Badik|Dagger of the Malay world.|Southeast Asia
Balarao|Traditional Asian dagger.|South Asia
Bichuwa|Indian dagger with a curved, scorpion-sting blade.|South Asia
Haladie|Indian double-bladed dagger.|South Asia
Jamdhar Katari|Afghan form of the katar.|West and Central Asia
Jambiya|Curved dagger of Yemen and Arabia.|West and Central Asia
Kaiken|Small Japanese dagger.|East Asia
Kard|Persian straight single-edged knife.|West and Central Asia
Kila|Traditional Asian dagger.|South Asia
Kirpan|Sikh ceremonial dagger.|South Asia
Kujang|Traditional blade of the Sundanese of Java.|Southeast Asia
Maduvu|Indian horn-tipped parrying weapon.|South Asia
Malappuram Kathi|Dagger of Malappuram, Kerala.|South Asia
Piha kaetta|Sri Lankan knife.|South Asia
Punyal|Philippine dagger.|Southeast Asia
Qama|Caucasian dagger.|West and Central Asia
Shuckra|Traditional Asian dagger.|South Asia
Yoroi doshi|Japanese armour-piercing dagger.|East Asia""",DL),"One entry is a named dagger of Asia not given its own kind; makes are versions.","Every dagger under 'Asian tradition' in Wikipedia's List of daggers except those with their own kind here (kris, karambit, kukri, katar, sai, tantō, balisong, hachiwara, kalis, khanjar, khanjali, pesh-kabz).",'by region')
newkind('Daggers & fighting knives','African dagger','billao · seme · koummya','Dagger or short blade of Africa of Africa.',DL)
add('African dagger',rows("""Jile|Dagger of the Somali people.|East Africa
Billao|Somali dagger.|East Africa
Seme|Kenyan dagger.|East Africa
Mambele|Central African throwing knife.|Central Africa
Koummya|Moroccan dagger.|North Africa""",DL),"One entry is a named dagger or knife of Africa; local makes are versions.","All five African daggers of Wikipedia's List of daggers.",'by region')
newkind('Daggers & fighting knives','American and military fighting knife','V-42 · Gerber Mark II · Facón','Fighting knife of the Americas or of the 20th-century forces, of the Americas.',DL)
add('American and military fighting knife',rows("""Facón|Gaucho knife of Argentina, Brazil and Uruguay.|South America|19th c.
Corvo|Chilean curved knife.|South America|19th c.
BC-41|Fighting knife of the Second World War.|Military issue|1941
Cuchillo de Paracaidista|Argentine paratrooper knife.|Military issue
Gerber Mark II|Fighting knife made by Gerber.|Military issue|1967
United States Marine Raider stiletto|Fighting stiletto of the US Marine Raiders.|Military issue|WWII
V-42 stiletto|Fighting stiletto of the First Special Service Force.|Military issue|WWII
Applegate–Fairbairn fighting knife|Fighting knife designed by Applegate and Fairbairn.|Military issue|WWII
Yank Levy fighting knife|Fighting knife associated with Yank Levy.|Military issue
SOG Knife|Special-forces fighting knife of the Vietnam War era.|Military issue""",DL),"One entry is a named fighting knife of the Americas or of a military issue.","All American-tradition knives of Wikipedia's List of daggers except those with their own kind (Bowie, trench knife, push dagger, bayonets).",'by origin')
for kn in ('Seax','Bowie knife','Trench knife','Kris','Karambit','Push dagger','Hunting knife','Kukri'):
    dropm(kn,'Retail or unsourced models; removed as out of scope')
for kn in ('Sword bayonet','Spike bayonet','Knife bayonet','Throwing knife','Shuriken','Butterfly knife','Automatic knife'):
    dropm(kn,'Retail or unsourced models; removed as out of scope')
for kn,nl in [('Seax',"One entry is a Petersen-style seax type."),('Bowie knife',"One entry is a named Bowie, fighting-knife pattern or maker's model of the American tradition."),('Trench knife',"One entry is a named military trench-knife pattern."),('Kris',"One entry is a regional form of the wavy-bladed dagger."),('Karambit',"One entry is a regional form of the curved claw knife."),('Push dagger',"One entry is a named push dagger or punch knife."),('Hunting knife',"One entry is a famous hunting-knife model."),('Kukri',"One entry is a regional or service pattern of the kukri."),('Sword bayonet',"One entry is a military sword-bayonet pattern."),('Spike bayonet',"One entry is a military spike-bayonet pattern."),('Knife bayonet',"One entry is a military knife-bayonet pattern."),('Throwing knife',"One entry is a named throwing-knife form."),('Shuriken',"One entry is a form of throwing star."),('Butterfly knife',"One entry is a named balisong make or form."),('Automatic knife',"One entry is a named automatic-knife make or military pattern.")]:
    KIND[kn]['nl']=nl+" Versions are marks and variants."
    KIND[kn]['sel']="Patterns named in Wikipedia's List of daggers and in the form's own article; there is no whole-space list for this form."
# Polearms
PA=WP+'Polearm'
add('Spear',rows("""Dory|Greek hoplite spear.|European
Kontos|Long Greek lance.|European
Xyston|Macedonian cavalry lance.|European
Trident|Three-pronged spear.|European
Hasta|Roman thrusting spear.|European
Javelin|Light throwing spear.|European
Lance|Mounted couched spear of the knight.|European
Bear spear|Spear with a crossbar for hunting bear.|European
Boar spear|Spear with a crossbar for hunting boar.|European
Ox tongue spear|Broad-bladed European spear.|European
Spontoon|Short pike carried by officers.|European
Atgeir|Norse polearm of the sagas.|European
Goedendag|Flemish infantry staff weapon.|European
Ahlspiess|German spike-bladed spear.|European
Jumonji yari|Japanese cross-bladed spear.|Japanese
Sasaho yari|Japanese spear with a leaf-shaped head.|Japanese
Hoko yari|Japanese spear with a broad head.|Japanese
Kama-yari|Japanese spear with side blades.|Asian
Ngao|Thai spear-glaive.|Asian
Barcha|South Asian spear.|South Asian
Karpa Barcha|South Asian spear.|South Asian
Nagni Barcha|South Asian spear.|South Asian
Ballam|South Asian spear.|South Asian
Bambu runcing|Sharpened bamboo spear of Indonesia.|Asian
Sibat|Philippine spear.|Asian
Trishula|Three-pronged spear of South Asia.|Asian
Assegai|Southern African spear.|African
Chuki|Spear of the Americas.|American
Kunka kuchuna|Spear of the Americas.|American
Sovnya|Slavic and Asian polearm.|European and Asian""",PA))
add('Pike',rows("Half pike|Short pike used in boarding and by infantry officers.|European",PA))
add('Glaive',rows("""Svärdstav|Swedish polearm.|European
Swordstaff|European polearm with a sword blade.|European
Rawcon|European polearm.|European
Runka|European polearm.|European
Ranseur|European polearm with a trident-like head.|European
Spetum|European polearm with side prongs.|European
Chauve-souris|French polearm with a bat-wing head.|European""",PA))
add('Halberd',rows("""Scottish halberd|Halberd of Scotland.|European
Viking halberd|Halberd of the Viking Age.|European
Scottish polearms|Polearms of Scotland.|European
Jeddart staff|Scottish axe-bladed staff.|European
Brogit staff|Scottish staff weapon.|European
Dagger-axe|Chinese ge, a dagger blade set at right angles on a pole.|Chinese""",PA))
add('Poleaxe',rows("""Doloire|French axe on a long handle.|European
Miner's axe|European axe on a pole.|European
Sparth axe|Broad-bladed axe of the Irish and Norse.|European
Sparr axe|Irish axe.|European""",PA))
add('Bill',rows("""Hedge-bill|English hedge-cutting tool used as a weapon.|English
Welsh hook|Hooked Welsh polearm.|European
War scythe|Scythe blade set upright on a pole.|European
Bohemian earspoon|Bohemian polearm with a spoon-shaped head.|European
Brandistock|Staff with a hidden blade.|European
Military fork|Fork-headed European polearm.|European
Man catcher|Pole with a spring-closing head for pulling a rider from the saddle.|European
Menaulion|Greek spear-like weapon.|European
Plançon à picot|Pointed European staff weapon.|European
Sasumata|Japanese forked man-catcher.|Japanese
Sodegarami|Japanese barbed man-catcher.|Japanese
Tsukubō|Japanese man-catching pole.|Japanese
Torimono sandōgu|Japanese set of three police tools.|Japanese""",PA))
add('Guandao',rows("""Yanyue dao|Chinese crescent-moon polearm.|Chinese
Chun qiu da dao|Chinese polearm named for Guan Yu's weapon.|Chinese
Nine-ring guandao|Guandao with nine rings.|Chinese
Elephant guandao|Guandao with an elephant-head design.|Chinese
Dragon head guandao|Guandao with a dragon-head blade.|Chinese
Podao|Chinese long-bladed polearm.|Chinese
Fangtian ji|Chinese halberd with crescent blades.|Chinese
Qinglong ji|Chinese halberd of the Green Dragon.|Chinese""",PA))
add('Naginata',rows("""Woldo|Korean polearm.|Korean
Bisento|Japanese heavy polearm.|Japanese""",PA))
setg('Naginata','Japanese',{'Woldo':'Korean'})
add('Pike',[],"One entry is a named pike or half pike.","Pikes named in Wikipedia's Polearm article.")
for kn in ('Spear','Glaive','Bill','Halberd','Poleaxe','Guandao','Naginata'):
    KIND[kn]['nl']="One entry is a named polearm of its family; makes and dated patterns are versions."
    KIND[kn]['sel']="Every polearm of Wikipedia's Polearm article placed under its nearest family; Chinese, Japanese and European forms are set apart by region."
    KIND[kn]['xg']='by region'
    for x in KIND[kn]['x']:
        if not x.get('g'): x['g']='European'
setg('Halberd','European',{'Ji':'Chinese'})
setg('Poleaxe','European'); setg('Bill','European',{'Roncone':'European'}); setg('Glaive','European')
setg('Spear','European',{'Iklwa':'African','Qiang':'Chinese','Yari':'Japanese','Dory':'European','Pilum':'European'})
setg('Guandao','Chinese')
KIND['Pike']['nl']="One entry is a named pike or half pike."; KIND['Pike']['sel']="Pikes named in Wikipedia's Polearm article."
for kn in ('Spear','Partisan','Naginata','Guandao','Poleaxe'): dropm(kn,'Retail replica products or unsourced pieces; removed as out of scope')
# Axes, maces, hammers
for kn in ('Battle axe','Tomahawk','Mace','War hammer','Flail','Staff'):
    dropm(kn,'Retail replica products or unsourced pieces; removed as out of scope')
    KIND[kn]['nl']="One entry is a named form of the weapon; dated patterns are versions."
    KIND[kn]['sel']="Forms named in Wikipedia's Polearm article and the form's own article; no whole-space list exists."
dropm('Nunchaku','Retail model; removed as out of scope')
