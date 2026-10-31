AL=WP+'List_of_armour_types';SH=WP+'Shield'
add('Plate armour harness',rows("""Almain rivet|German-style articulated plate harness of the 16th century.|Plate armour
Kasten-brust armour|Plate harness with a box-shaped breastplate.|Plate armour
White armour|Plate armour left bright rather than painted or covered.|Plate armour
Transitional armour|Mixed mail and plate armour of the 13th and 14th centuries.|Transitional""",AL))
setg('Plate armour harness','Plate armour',{'Milanese armour':'Plate armour','Gothic plate armour':'Plate armour'})
setg('Plate armour harness','Plate armour',{'Maximilian armour':'Plate armour','Greenwich armour':'Plate armour','Munition armour':'Plate armour'})
add('Japanese armour',rows("""Haramaki|Japanese armour wrapped round the body and tied at the back.|Japanese
Tatami|Folding Japanese armour of small plates.|Japanese
Kikko|Japanese armour of hexagonal plates.|Japanese
Kusari|Japanese mail armour.|Japanese
Karuta|Japanese armour of small plates.|Japanese
Keiko|Japanese lamellar armour.|Japanese
Tankō|Japanese plate cuirass.|Japanese""",AL))
setg('Japanese armour','Japanese')
add('Gambeson',rows("""Buff coat|Thick leather coat worn in the 17th century.|Early modern
Linothorax|Ancient Greek armour of layered linen.|Ancient""",AL))
setg('Gambeson','Medieval')
add('Mail shirt',rows("""Lorica hamata|Roman mail shirt.|Ancient
Hauberk|Long mail shirt of the Middle Ages.|Medieval
Chain mail|Armour of interlinked rings.|Medieval
Mail and plate armour|Mail reinforced with plates, 13th–15th century.|Medieval""",AL))
add('Scale armour',rows("Lorica squamata|Roman scale armour.|Ancient",AL))
add('Lamellar armour',rows("""Klivanion|Byzantine lamellar cuirass.|Byzantine
Laminar armour|Armour of overlapping horizontal bands.|Medieval""",AL))
add('Brigandine',rows("""Coat of plates|Cloth or leather coat lined with riveted plates.|Medieval
Splint armour|Armour of narrow metal strips.|Medieval
Mirror armour|Persian and Central Asian armour with polished plates.|Eastern
Lame (armor)|Armour of overlapping bands.|Medieval""",AL))
setg('Brigandine','Medieval',{'Jack of plate':'Medieval','Dingjia':'Eastern'})
add('Cuirass',rows("""Lorica segmentata|Roman armour of overlapping steel bands.|Ancient
Breastplate|Single plate over the chest.|Medieval and later""",AL) if False else rows("Breastplate|Single plate over the chest.|Medieval and later",AL))
setg('Cuirass','Medieval and later',{'Muscle cuirass':'Ancient','Lorica segmentata':'Ancient'})
for kn in ('Plate armour harness','Japanese armour','Gambeson','Mail shirt','Scale armour','Lamellar armour','Brigandine','Cuirass'):
    KIND[kn]['xg']='by period and region'
    KIND[kn]['nl']="One entry is a named armour type of its kind, by period and region; surviving or replica sets are versions."
    KIND[kn]['sel']="Armour types in Wikipedia's List of armour types, placed in their nearest torso kind; the page's fictional types and modern systems (with Modern body armour) are left out."
    for x in KIND[kn].get('x',[]):
        if not x.get('g'): x['g']='Medieval'
# helmets
H=rows("""Attic helmet|Greek helmet of the Attic type.|Ancient
Boeotian helmet|Greek helmet.|Ancient
Chalcidian helmet|Greek helmet.|Ancient
Corinthian helmet|Greek helmet covering the face.|Ancient
Illyrian helmet|Greek and Balkan helmet.|Ancient
Pilos helmet|Greek conical helmet.|Ancient
Konos helmet|Greek conical helmet.|Ancient
Phrygian helmet|Helmet with a forward-curving peak.|Ancient
Montefortino helmet|Roman and Celtic helmet.|Ancient
Coolus helmet|Roman helmet.|Ancient
Imperial helmet|Roman helmet of the Imperial type.|Ancient
Galea|Roman helmet.|Ancient
Negau helmet|Helmet of the Alpine Iron Age.|Ancient
Novo Mesto helmet|Iron Age helmet of present-day Slovenia.|Ancient
Boar's tusk helmet|Mycenaean helmet covered in boar tusks.|Ancient
Cudon|Ancient helmet type.|Ancient
Kegelhelm|Ancient conical helmet.|Ancient
Late Roman ridge helmet|Late Roman helmet with a ridge.|Ancient
Cervelliere|Close-fitting medieval steel cap.|Medieval
Enclosed helmet|Medieval helmet enclosing the head.|Medieval
Frog-mouth helmet|Tournament helmet with a narrow eye slit.|Medieval
Hounskull|Bascinet with a pointed visor.|Medieval
Kulah khud|Persian and Mughal helmet.|Medieval
Lamellenhelm|Helmet made of lamellae.|Medieval
Secrete|Hidden steel cap worn under a hat.|Medieval
Turban helmet|Ottoman helmet with a turban-shaped bowl.|Medieval
Dragoon helmet|Cavalry helmet.|Late modern
Pickelhaube|Prussian spiked helmet.|Late modern
Pith helmet|Colonial sun helmet.|Late modern
Tarleton helmet|British light-dragoon helmet.|Late modern
Jingasa|Japanese hat helmet.|Medieval
Katapu|Helmet of Southeast Asia.|Medieval
Paseki|Helmet of Asia.|Medieval
Takula tofao|Samoan helmet.|Medieval
Adrian helmet|French helmet of the First World War.|Twentieth century
Brodie helmet|British helmet of the First World War.|Twentieth century
Stahlhelm|German steel helmet.|Twentieth century
M1 helmet|US steel helmet of the Second World War.|Twentieth century
Mk III helmet|British turtle helmet.|Twentieth century""",AL)
add('Historical helmet',H)
setg('Historical helmet','Medieval',{'Spangenhelm':'Early medieval','Nasal helmet':'Early medieval','Great helm':'Medieval','Bascinet':'Medieval','Kettle hat':'Medieval','Sallet':'Medieval','Barbute':'Medieval','Armet':'Medieval','Close helmet':'Early modern','Burgonet':'Early modern','Morion':'Early modern','Lobster-tailed pot':'Early modern'})
KIND['Historical helmet']['xg']='by period'
KIND['Historical helmet']['nl']="One entry is a named type of helmet; surviving or replica helmets are versions."
KIND['Historical helmet']['sel']="Helmet types of Wikipedia's List of armour types: ancient, medieval and early modern, late modern and 1914–1945 combat helmets in current collecting; later military helmets are under Ballistic helmet and the athletic, work and fictional groups are left out."
add('Ballistic helmet',rows("""PASGT helmet|US Army ballistic helmet of the 1980s.|Late twentieth century
MICH helmet|US modular integrated communications helmet.|Twenty-first century
Advanced Combat Helmet|US ballistic helmet.|Twenty-first century
FAST helmet|Lightweight ballistic helmet.|Twenty-first century
Lightweight Helmet|US Marine Corps ballistic helmet.|Twenty-first century""",AL))
KIND['Ballistic helmet']['xg']='by era'
KIND['Ballistic helmet']['nl']="One entry is a named military ballistic helmet system; maker variants are versions."
KIND['Ballistic helmet']['sel']="Combat helmets of Wikipedia's List of armour types from 1980 onward, cut to the best-known US systems."
for x in KIND['Ballistic helmet']['x']:
    if x['n']=='FAST helmet': x['v']=[{'n':n,'y':'','d':'Ops-Core variant'} for n in ('Ops-Core FAST SF','Ops-Core FAST XP','Ops-Core FAST RF1')]
KIND['Ballistic helmet'].pop('m',None); REMOVED.append(('Ballistic helmet',['Ops-Core FAST SF','Ops-Core FAST XP','Ops-Core FAST RF1'],'Became versions of FAST helmet'))
add('Plate carrier',rows("""Interceptor body armor|US Army modular vest system.|Twenty-first century
Improved Outer Tactical Vest|US Army successor to the outer tactical vest.|Twenty-first century
Modular Tactical Vest|US Marine Corps modular vest.|Twenty-first century
CIRAS|US Special Operations vest.|Twenty-first century
Osprey body armour|British Army vest.|Twenty-first century
Ranger Body Armor|US Army vest of the 1990s.|Late twentieth century
Dragon Skin|Armour of overlapping ceramic discs.|Twenty-first century
PASGT vest|US Army soft body armour of the 1980s.|Late twentieth century""",AL))
setg('Plate carrier','Twenty-first century')
KIND['Plate carrier']['xg']='by era'
KIND['Plate carrier']['nl']="One entry is a named body-armour system; issue patterns are versions."
KIND['Plate carrier']['sel']="Armour systems of Wikipedia's List of armour types (the page's section on armour systems), cut to US and British systems; others on the list are not read."
for kn in ('Soft ballistic vest','Hard armour plate','Stab-resistant vest'):
    dropm(kn,'Retail products; removed as out of scope')
# Shields
newkind('Shields','Shield of other cultures','taming · glagwa · figure-of-eight shield','Shield named by culture that is not one of the European forms in the kinds above.',SH)
add('Shield of other cultures',rows("""Figure-of-eight shield|Mycenaean Greek shield of wicker and leather.|Ancient
Tower shield|Rectangular Mycenaean shield of wicker and leather.|Ancient
Pelte|Small Greek light shield.|Ancient
Yetholm-type shield|Bronze Age metal shield, probably ceremonial.|Bronze Age
Battersea shield|Iron Age metal shield, probably ceremonial.|Iron Age
Bouche|Medieval shield with a notch for the lance.|Medieval
Glagwa|Cameroon shield.|Africa
Nguba|Shield of the Republic of the Congo.|Africa
Taming|Round rattan or wood shield of the Malay world.|Southeast Asia
Keliau|Large hexagonal wooden shield of the Dayak of Borneo.|Southeast Asia""",SH),"One entry is a named shield of a culture or period not covered by the kinds above.","Shield types of Wikipedia's Shield article not already a kind here; riot and ballistic shields are institutional equipment and are left out.",'by period or region')
add('Round shield',rows("""Parma|Small round Italian shield.|Italy
Rotella|Round Italian shield.|Italy
Viking round shield|Light wooden round shield with a metal boss.|Early medieval Europe""",SH))
setg('Round shield','Ancient',{'Aspis':'Ancient'})
KIND['Round shield']['nl']="One entry is a named round shield; replicas are versions."
KIND['Round shield']['sel']="Round shields named in Wikipedia's Shield article."
KIND['Round shield'].pop('m',None); REMOVED.append(('Round shield',['Windlass Steel Domed Shield'],'Retail product; removed'))
for kn in ('Plate armour harness','Japanese armour','Brigandine','Gauntlet'):
    KIND[kn].pop('m',None)
REMOVED.append(('Plate armour harness / Japanese armour / Brigandine / Gauntlet',['Savoyard armour','Hoshi-bachi','Suji-bachi','Zunari','Kawari kabuto','Happuri','Sōmen','Hanbō','15th-century form','16th-century form','Churburg gauntlets','Maximilian gauntlets'],'No fetched page names them; removed as unsourced'))
for kn in ('Gorget','Gauntlet'):
    KIND[kn]['nl']="One entry is a named type of the piece."
    KIND[kn]['sel']="Pieces cited from their own articles; no whole-space list exists."
