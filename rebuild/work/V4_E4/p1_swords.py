OAK=WP+'Oakeshott_typology'
# --- Oakeshott: rebuild from old entries, subtypes as versions
old={}
for kn in('Arming sword','Longsword'):
    for x in KIND[kn]['x']: old[x['n']]=x
def oak(base,d,y,sub,g):
    o=copy.deepcopy(old.get('Oakeshott Type '+base)) or e('Oakeshott Type '+base,d,y,s=OAK)
    o['d']=d; o['y']=y; o['s']=OAK; o['g']=g; o['a']=o.get('a','')
    o.pop('dt',None) if False else None
    vs=o.setdefault('v',[])
    for sn,sy,sd in sub:
        prev=old.get('Oakeshott Type '+sn)
        vs.insert(0,{'n':'Type '+sn,'y':sy,'d':sd})
        if prev:
            for q in prev.get('v',[]):
                if q['n'] not in [z['n'] for z in vs]: vs.append(q)
    return o
G1='Viking age to 13th century';G2='14th to 15th century';G3='Late 15th to 16th century'
arm=[
 oak('X','Broad, flat, long blade with a wide shallow fuller and rounded point; the Norman sword.','late Viking age to 13th c.',[('Xa','','narrower fullers')],G1),
 oak('XI','Longer, slimmer blade with an acute point, suited to slashing from horseback.','c. 1100–1175',[('XIa','','broader, shorter blade')],G1),
 oak('XII','Tapering blade with a shortened fuller, better for the thrust; the classic crusade-era sword.','later 13th c., possibly earlier',[('XIIa','mid-13th c.','longer, more massive greatsword form')],G1),
 oak('XIII','Knightly sword with a long, wide, parallel-edged blade and lens-shaped section.','second half of 13th c.',[('XIIIa','','longer blades and grips; the knightly greatswords'),('XIIIb','c. 1300','smaller single-handed form')],G1),
 oak('XIV','Short, broad, strongly tapering blade of flat section with a wheel pommel.','c. 1270 – early 14th c.',[],G2),
 oak('XV','Straight tapering blade of diamond section with a sharp point, linked with the rise of plate armour.','14th–15th c.',[('XVa','','longer, narrower blade with a two-handed grip')],G2),
 oak('XVI','Flat cutting blade tapering to a reinforced acute point, somewhat like a slimmer Type XIV.','14th–15th c.',[('XVIa','','longer blade, shorter fuller, extended grip')],G2),
]
lng=[
 oak('XVII','Long, evenly tapering blade of hexagonal section with a two-handed grip.','c. 1360–1420',[],G2),
 oak('XVIII','Broad-based tapering blade of diamond section with a raised midrib.','14th–15th c.',[('XVIIIa','','narrow blade with a longer grip'),('XVIIIb','c. 1450–1520','bastard sword with longer blade and grip'),('XVIIIc','','shorter grip and broad blade of about 90 cm'),('XVIIIe','','narrow, long blade with extended ricasso and very long grip')],G2),
 oak('XIX','Narrow, flat, hexagonal-section blade with a pronounced ricasso and finger loops below the guard.','15th c.',[],G2),
 oak('XX','Hand-and-a-half or two-handed sword with two or more fullers.','14th–15th c.',[('XXa','','narrower blade with a more acute, linear taper')],G2),
 oak('XXI','Broad, heavily tapering sword with several long fullers and downward-curved quillons, resembling the cinquedea.','late 15th c.',[],G3),
 oak('XXII','Broad, flat, spatulate blade with one or two short fullers, probably often ceremonial.','mid-15th – 16th c.',[],G3),
]
KIND['Arming sword']['x']=[]; KIND['Longsword']['x']=[]
sel_o="Every blade type X to XXII of Wikipedia's Oakeshott typology, with its subtypes as versions; types X to XVI sit here and XVII to XXII under Longsword. Sections follow the page's dates."
add('Arming sword',arm,"One entry is an Oakeshott blade type for the medieval one-handed sword; lettered subtypes and surviving swords are versions.",sel_o,'by period')
add('Longsword',lng,"One entry is an Oakeshott blade type for the hand-and-a-half or two-handed sword; lettered subtypes and surviving swords are versions.",sel_o.replace('types X to XVI sit here and XVII to XXII under Longsword','types XVII to XXII sit here and X to XVI under Arming sword'),'by period')
dropm('Arming sword','Retail replica products of makers; no sword canon names them, so removed as out of scope')
dropm('Longsword','Retail replica products; removed as out of scope')
dropm('Greatsword','Retail replica product; removed as out of scope')
dropm('Rapier','Retail replica products; removed as out of scope')
dropm('Smallsword','Retail replica product; removed as out of scope')
# --- other European
T=WP+'Types_of_swords'
add('Short sword',[
 e('Falcata','One-handed single-edged sword with a forward-curving blade; the sword of the Iberian peoples.','',g='Ancient',s=T),
 e('Kopis','One-handed single-edged forward-curving slashing sword of ancient Greece.','',g='Ancient',s=T),
 e('Makhaira','Greek single-edged shortsword or knife for cutting and thrusting.','',g='Ancient',s=T),
 e('Falx','Curved single-edged short sword of the Dacians and Thracians.','',g='Ancient',s=T),
 e('Harpe','Bronze Age curved sword known mainly from Greek myth.','',g='Ancient',s=T),
 e('Rhomphaia','Greek single-edged broadsword for slashing and thrusting.','',g='Ancient',s=T),
 e('Sica','Curved single-edged blade of Thracian origin, named in the ancient list.','',g='Ancient',s=T),
 e('Xyele','Short, slightly curved, single-edged Spartan sword.','',g='Ancient',s=T),
],"One entry is a named short sword form of the ancient Mediterranean and Europe; modern replicas and surviving finds are versions.","Every ancient European sword named in Wikipedia's Types of swords (prehistory and ancient period), the long swords (spatha) excepted; Gladius and Xiphos were already here.",'by period')
setg('Short sword','Ancient')
add('Spatha',[
 e('Ring-sword','Merovingian-period development of the spatha with a ring-shaped pommel attachment.','',g='Migration Period to early Middle Ages',s=T),
 e('Krefeld type','Migration Period sword type.','',g='Migration Period to early Middle Ages',s=T),
 e('Migration Period sword','Germanic long sword of the Migration Period.','',g='Migration Period to early Middle Ages',s=T),
],"One entry is a named type of the late-Roman and early-medieval long sword; finds and replicas are versions.","The spatha-derived swords named in Wikipedia's Types of swords; no whole-space list exists.")
add('Viking sword',[e('Carolingian sword','Early medieval spatha-derived sword, also used as another name for the Viking sword.','',g='Early Middle Ages',s=T)])
setg('Viking sword','Early Middle Ages')
KIND['Viking sword']['nl']="One entry is a named type or famous make of the Viking-age sword; surviving swords are versions."
KIND['Viking sword']['sel']="The Petersen types and Ulfberht swords already cited from their own articles, plus the Carolingian sword of Wikipedia's Types of swords; no whole-space list exists."
add('Greatsword',[
 e('Montante','Large Spanish and Italian two-handed sword of the early modern period.','',g='Early modern',s=T),
 e('Flamberge','Sword with a wavy, flame-shaped blade.','',g='Early modern',s=T),
 e('Executioner\'s sword','Two-edged sword with a rounded tip made for beheading.','',g='Early modern',s=T),
],"One entry is a named type of two-handed sword; later makes and training copies are versions.","Two-handed swords named in Wikipedia's Types of swords (Zweihänder, claymore, montante, flamberge, executioner's sword).")
setg('Greatsword','Early modern',{'Two-handed claymore':'Late Middle Ages and early modern'})
add('Katzbalger',[e('Swiss degen','Early modern Swiss short sword.','',g='Early modern',s=T)],"One entry is a named short sword of the Landsknecht and Swiss tradition.","The Katzbalger and Swiss degen from Wikipedia's Types of swords.")
setg('Katzbalger','Early modern')
add('Rapier',[
 e('Espada ropera','Spanish name for the early rapier, or sword of the dress.','',g='Early modern',s=T),
 e('Spada da lato','Italian side-sword of the early modern period; used in early modern fencing.','',g='Early modern',s=T),
 e('Schiavonesca','Venetian basket-hilted sword; a forerunner of the schiavona.','',g='Early modern',s=T),
 e('Pistol sword','Sword with a firearm built into the hilt or blade.','',g='Late modern',s=T),
],"One entry is a named rapier-age sword form; dated makes are versions.","Rapiers and side-swords named in Wikipedia's Types of swords; no whole-space list exists.")
setg('Rapier','Early modern')
add('Smallsword',[
 e('Colichemarde','Smallsword with a blade broad at the forte and narrow beyond.','',g='Late modern',s=T),
 e('Spadroon','Light cut-and-thrust sword of the 18th and early 19th centuries.','',g='Late modern',s=T),
 e('Hunting sword','Short sword carried for the hunt.','',g='Late modern',s=T),
],"One entry is a named light-sword form of the 17th to 19th centuries.","Light swords named in Wikipedia's Types of swords.")
setg('Smallsword','Late modern')
add('Sabre',[
 e('Karabela','Polish and Eastern European curved sabre with a distinctive hilt.','',g='Early modern',s=T),
 e('Dussack','Single-edged sabre of the German 16th century, later a training weapon.','',g='Early modern',s=T),
],"One entry is a named sabre form or a sabre pattern issued to a service.","Sabres named in Wikipedia's Types of swords, plus the military patterns already cited from their own articles; no whole-space list exists.")
setg('Sabre','Early modern',{'1796 Pattern Light Cavalry Sabre':'Late modern','Model 1913 cavalry saber':'Late modern','Shashka':'Late modern','Polish szabla':'Early modern'})
# 'm' entries without maker -> entries
for nm in ['British 1897 pattern infantry officer sword','Mongolian sabre (Yuan)','US Marine Corps NCO sword']:
    pass
REMOVED.append(('Sabre',['British 1897 pattern infantry officer sword','Mongolian sabre (Yuan)','US Marine Corps NCO sword'],'No fetched page; removed as unsourced'))
KIND['Sabre'].pop('m',None)
KIND['Cutlass'].pop('m',None); REMOVED.append(('Cutlass',['Tactical Cutlass','Naval Cutlass','Anix','Shell Guard','Battlecry!','Heritage Pirate Cutlass','Naval cutlass 1860','RN 1804'],'Retail or unsourced models; removed'))
add('Cutlass',[e('Basket-hilted sword','Sword with a guard that wraps the hand, a form shared by cutlass, broadsword and schiavona.','',g='Late modern',s=T)] if False else [],"One entry is a named naval sword pattern.","The US Navy M1917 cutlass is cited from its own article; no whole-space list exists.")
# Japanese
J=WP+'Japanese_sword'
NIH='https://nihonto.com/about-swords/major-koto-schools/'
k=newkind('Japanese swords (nihontō)','Sword tradition (den)','Gokaden · five great schools','One of the five great regional traditions of Japanese swordmaking, each with its own schools of smiths.',NIH,pos=0)
add('Sword tradition (den)',[
 e('Yamato','Tradition of Nara province; masame grain and straight temper lines, with narrow graceful early blades.','late Heian to Kamakura',g='Gokaden (Kotō schools)',s=NIH,v=[('Senjuin','','major Yamato school'),('Taima','','mokume mixed with itame and chikei'),('Shikkake','','nakago iri-yamagata'),('Tegai','','major Yamato school'),('Hōshō','','only school with pure masame')]),
 e('Yamashiro','Tradition of Kyoto; fine ko-mokume grain and ko-chōji midare, narrow blades with small points in the early period.','late Heian to Muromachi',g='Gokaden (Kotō schools)',s=NIH,v=[('Awataguchi','','Yamashiro school'),('Rai','','wide suguha chōji-midare')]),
 e('Bizen','Tradition of Okayama; itame and mokume grain with utsuri and chōji midare; centre of Osafune.','late Heian to Shinshintō',g='Gokaden (Kotō schools)',s=NIH,v=[('Ko-Bizen','late Heian to early Kamakura','earliest Bizen work'),('Ichimonji','','juka-chōji hamon'),('Osafune','','main Bizen centre')]),
 e('Sōshū','Tradition of Kamakura founded in the late 13th century; nie-rich hamon and hitatsura.','late Kamakura to Muromachi',g='Gokaden (Kotō schools)',s=NIH,v=[('Shintōgo Kunimitsu lineage','late 13th c.','founder, with roots in Awataguchi')]),
 e('Mino','Tradition of Gifu from late Kamakura; sanbon-sugi hamon, with the later sue-seki school.','late Kamakura to Muromachi',g='Gokaden (Kotō schools)',s=NIH,v=[('Early Mino','late Kamakura','matches late Kamakura shape'),('Middle Mino','mid-Nanbokuchō to early Muromachi','wide o-midare or gunome'),('Sue-seki','Muromachi','later Mino school')]),
],"One entry is one of the five great swordmaking traditions of the Kotō period; its schools are versions.","The five traditions of the Gokaden as set out on nihonto.com's page on the major Kotō schools; the later Shintō and Shinshintō periods are not dated by that page.",'by tradition group')
for kn in ('Tachi','Katana','Wakizashi','Tantō','Ōdachi'):
    KIND[kn]['nl']="One entry is a named smith, school or famous blade of the form; dated copies and attributed blades are versions."
    KIND[kn]['sel']="Smiths and blades named in Wikipedia's articles on the form and in its list of National Treasures (swords); the Gokaden traditions are under Sword tradition. No whole-space list of Japanese blades exists."
    dropm(kn,'Retail replica products or unsourced pieces; removed as out of scope')
KIND['Ken (tsurugi)'].pop('m',None);REMOVED.append(('Ken (tsurugi)',['Kongō-ji tsurugi','Yasaka Shrine tsurugi'],'Unsourced; removed'))
k=newkind('Japanese swords (nihontō)','Other Japanese sword form','Chokutō · kodachi · nagamaki','A Japanese sword form beyond tachi, katana, wakizashi and tantō, from the ancient straight blades to 20th-century types.',T)
add('Other Japanese sword form',[
 e('Chokutō','Straight single-edged ancient Japanese sword.','Yayoi–Nara',g='Ancient (Yayoi–Nara)',s=T),
 e('Tsurugi','Straight double-edged ancient Japanese sword, the ken.','Yayoi–Nara',g='Ancient (Yayoi–Nara)',s=T),
 e('Kodachi','Short companion sword of the Heian and Kamakura periods.','Heian–Kamakura',g='Heian to Edo',s=T),
 e('Nagamaki','Sword with a very long hilt, like a short polearm.','Heian–Kamakura',g='Heian to Edo',s=T),
 e('Kenukigata tachi','Tachi with a hilt and tang blade shaped like a pair of tweezers.','Heian',g='Heian to Edo',s=T),
 e('Jintachi','Tachi made for war rather than court.','',g='Heian to Edo',s=T),
 e('Kyū guntō','Army sword of the Meiji period in Western style.','Meiji',g='Meiji onward',s=T),
 e('Ninjatō','Straight-bladed sword attributed to ninja in later popular accounts.','',g='Meiji onward',s=T),
 e('Shikomizue','Blade hidden in a walking stick.','',g='Meiji onward',s=T),
],"One entry is a named Japanese sword form; makes and regional variants are versions.","The Japanese swords of Wikipedia's Types of swords not already a kind here; practice swords (bokken, shinai, shinken) belong to the sport departments and are left out.",'by period')
# Asia
add('Dao (Chinese sabre)',[
 e('Nandao','Southern Chinese sabre used in modern wushu.','',g='Modern',s=T),
 e('Wodao','Chinese name for the Japanese-style sword of the Ming era.','',g='Ming–Qing',s=T),
 e('Miaodao','Long two-handed Chinese sabre of the 20th century.','',g='Modern',s=T),
],"One entry is a named type of Chinese single-edged sabre.","Chinese sabres named in Wikipedia's Types of swords; Yanmaodao, Liuyedao and others were already here.",'by period')
setg('Dao (Chinese sabre)','Ming–Qing',{'Zhanmadao':'Medieval','Piandao':'Ming–Qing','Hengdao':'Ming–Qing','Changdao':'Ming–Qing','Duandao':'Ming–Qing','Niuweidao':'Ming–Qing'})
add('Jian',[
 e('Shuangshou jian','Two-handed Chinese straight sword.','',g='Ancient',s=T),
 e('Hook sword','Chinese sword with a hooked tip and crescent guard.','',g='Medieval',s=T),
],"One entry is a named type of Chinese straight sword.","Jian forms named in Wikipedia's Types of swords.")
setg('Jian','Ancient')
newk=newkind('Swords of Asia, Africa & the Middle East','Korean sword','hwandudaedo · saingeom','Sword or blade of Korea named in the ancient and Joseon periods.',T)
add('Korean sword',[
 e('Liaoning bronze dagger','Bronze Age dagger of Gojoseon.','',g='Bronze Age to Gojoseon',s=T),
 e('Hwandudaedo','Ring-pommel sword of the Three Kingdoms era.','',g='Iron Age to Three Kingdoms',s=T),
 e('Bonguk geom','Sword of the Goryeo and Joseon eras.','',g='Goryeo and Joseon',s=T),
 e('Saingeom','Joseon ritual sword.','',g='Goryeo and Joseon',s=T),
],"One entry is a named sword of Korea; later copies are versions.","Korean swords named in Wikipedia's Types of swords (all of them).",'by period')
k=newkind('Swords of Asia, Africa & the Middle East','South Asian sword','pata · urumi · firangi','Sword of the Indian subcontinent not already a kind of its own here.',T)
add('South Asian sword',[
 e('Aruval','Indian sickle-shaped blade of the ancient group.','',g='Ancient',s=T),
 e('Urumi','Flexible whip sword of South India.','',g='Ancient',s=T),
 e('Asi','South Asian name for a sword.','',g='Medieval and modern',s=T),
 e('Firangi','Indian sword with a European blade.','',g='Medieval and modern',s=T),
 e('Pata','Gauntlet sword of India.','',g='Medieval and modern',s=T),
 e('Kayamkulam vaal','Kerala sword.','',g='Medieval and modern',s=T),
 e('Kastane','Sri Lankan sword.','',g='Medieval and modern',s=T),
 e('Hengdang','Sword of the Indian subcontinent.','',g='Medieval and modern',s=T),
 e('Ram-dao','Sacrificial blade of Nepal and India.','',g='Medieval and modern',s=T),
 e('Moplah','Sword of the Moplah community of Kerala.','',g='Medieval and modern',s=T),
 e('Koftgiri','Indian sword decorated in koftgari inlay.','',g='Medieval and modern',s=T),
 e('Patag','Bhutanese sword.','',g='Medieval and modern',s=T),
],"One entry is a named sword of South Asia; regional makes are versions.","South Asian swords named in Wikipedia's Types of swords, except those with their own kind (khanda, talwar, kirpan).",'by period')
k=newkind('Swords of Asia, Africa & the Middle East','Arab, Persian and Central Asian sword','saif · scimitar · acinaces','Sword of Western and Central Asia not already a kind here.',T)
add('Arab, Persian and Central Asian sword',[
 e('Acinaces','Short Persian and Scythian sword of the ancient period.','',g='Ancient',s=T),
 e('Chereb','Western Asian sword of the ancient period.','',g='Ancient',s=T),
 e('Saif','Arab straight sword.','',g='Post-classical (Islamic world)',s=T),
 e('Scimitar','English word for curved swords of the Islamic world.','',g='Post-classical (Islamic world)',s=T),
 e('Turko-Mongol sabre','Curved sabre of the Turkic and Mongol peoples.','',g='Post-classical (Islamic world)',s=T),
 e('Arab sword','General type of Arab sword of the post-classical period.','',g='Post-classical (Islamic world)',s=T),
 e('Kindjal','Long double-edged Caucasian dagger-sword.','',g='Early modern',s=T),
],"One entry is a named sword of Western and Central Asia; regional makes are versions.","Western and Central Asian swords named in Wikipedia's Types of swords, except those with their own kind (shamshir, kilij, yataghan, pulwar).",'by period')
k=newkind('Swords of Asia, Africa & the Middle East','African sword','khopesh · kaskara · nimcha','Sword of Africa not already a kind here.',T)
add('African sword',[
 e('Khopesh','Sickle sword of ancient Egypt.','',g='Ancient Egypt',s=T),
 e('Kaskara','Straight Sudanese sword.','',g='Mainland Africa',s=T),
 e('Nimcha','Curved sword of Morocco, Algeria and Tunisia, 15th to 19th century.','15th–19th c.',g='Mainland Africa',s=T),
 e('Flyssa','Algerian sword of the Kabyle.','',g='Mainland Africa',s=T),
 e('Ida','Sword of Nigeria and Benin.','',g='Mainland Africa',s=T),
 e('Akrafena','Sword of Ghana and Togo.','',g='Mainland Africa',s=T),
 e('Ikakalaka','Central African sword.','',g='Mainland Africa',s=T),
 e('Ikul','Central African blade.','',g='Mainland Africa',s=T),
 e('Ngulu','Central African blade.','',g='Mainland Africa',s=T),
],"One entry is a named sword of Africa; local makes are versions.","African swords named in Wikipedia's Types of swords, except Shotel and Takoba (own kinds); the dagger-like Billao, Seme and Mambele are under African dagger.",'by region')
k=newkind('Swords of Asia, Africa & the Middle East','Maritime Southeast Asian sword','parang · barong · mandau','Sword or heavy knife of the Philippines and Indonesia.',T)
PH='Philippines';IN='Indonesia'
add('Maritime Southeast Asian sword',
 [e(n,'Blade of the Philippines named in the pre-colonial list.','',g=PH,s=T) for n in ['Balasiong','Bangkung','Banyal','Barong','Bicuco','Bolo','Dahong palay','Gayang','Gulok','Lahot','Laring','Panabas','Pirah','Pinuti','Sundang','Susuwat','Talibong','Utak','Balisword']]+
 [e(n,'Blade of Indonesia named in the early or late period list.','',g=IN,s=T) for n in ['Balato','Gari','Mandau','Niabor','Parang','Surik','Keris bahari','Klewang','Langgai tinggang','Parang nabur','Sikin Panjang']],
 "One entry is a named sword or heavy blade of the Philippines or Indonesia; local makes are versions.","Every Philippine and Indonesian blade of Wikipedia's Types of swords except the kris, kalis, karambit and kampilan, which have their own kinds; sections follow the page's country headings.",'by country')
k=newkind('Swords of Asia, Africa & the Middle East','Mesoamerican sword-club','macuahuitl · macana','Wooden club-sword set with stone or obsidian blades.',T)
add('Mesoamerican sword-club',[e('Macuahuitl','Wooden club edged with obsidian blades.','',g='Pre-Columbian',s=T),e('Macana','Wooden club-sword of the Americas.','',g='Pre-Columbian',s=T)],"One entry is a named Pre-Columbian sword-club.","Both Mesoamerican weapons of Wikipedia's Types of swords.")
for kn in('Dha','Talwar','Shamshir','Kilij','Yataghan'):
    KIND[kn]['nl']="One entry is a named type or regional form of the sword; makes are versions."
    KIND[kn]['sel']="Forms of the sword named in Wikipedia's Types of swords and the form's own article; no whole-space list exists."
KIND['Kilij'].pop('m',None); REMOVED.append(('Kilij',['Janissary kilij','Sword attributed to Özbeg Khan'],'Unsourced; removed'))
# Tosogu
for kn in ('Tsuba','Fuchi-kashira','Menuki','Saya','Kozuka and kōgai'):
    KIND[kn]['nl']="One entry is a school of fitting makers or a named maker; examples are versions."
    KIND[kn]['sel']="Schools named by shibuiswords.com's tsuba artisan schools page and japaneseswordindex.com; no whole-space list exists."
