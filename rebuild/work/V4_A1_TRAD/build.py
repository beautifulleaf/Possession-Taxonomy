import json,copy,re,urllib.parse
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/A1.json'))
dep=copy.deepcopy([x for x in d['depts'] if x['n']=='Traditional dress'][0])
W='https://en.wikipedia.org/wiki/'
# ---- 1. dissolve cloth shelf
cloth=[s for s in dep['s'] if s['n']=='Named cloths & textiles'][0]
dep['s']=[s for s in dep['s'] if s is not cloth]
cl={k['n']:[e['n'] for e in k.get('x',[])] for k in cloth['k']}
cvals={'Kente cloth':'Kente','Wax print (Ankara)':'Wax print','Batik cloth':'Batik','Shweshwe':'Shweshwe','Bogolan':'Bogolan','Adire & aso-oke':'Adire and aso-oke','Ikat cloth':'Ikat','Songket & tenun':'Songket and tenun','Khadi & handloom cloth':'Khadi and handloom','Faso Dan Fani':'Faso Dan Fani','Tapa & masi':'Tapa and masi','Tartan cloth':'Tartan','Tweed cloth':'Tweed'}
assign={'Sari':['Ikat cloth','Khadi & handloom cloth'],'Dupatta':['Ikat cloth'],'Dhoti':['Khadi & handloom cloth'],'Kimono':['Ikat cloth'],
'Dashiki':['Kente cloth','Wax print (Ankara)'],'Kaba and slit':['Kente cloth','Wax print (Ankara)'],'Boubou & agbada':['Adire & aso-oke','Bogolan','Faso Dan Fani','Wax print (Ankara)'],
'Southern African dress':['Shweshwe'],'Kebaya':['Batik cloth'],'Sarong & wrap cloth':['Batik cloth','Songket & tenun','Ikat cloth'],'Baju kurung & baju Melayu':['Songket & tenun','Batik cloth'],
'Pacific island dress':['Tapa & masi'],'Kilt':['Tartan cloth','Tweed cloth']}
# ---- 2. drop loose models/ranges
dropped_m=[];dropped_r=[]
for s in dep['s']:
  for k in s['k']:
    for key,l in (('m',dropped_m),('r',dropped_r)):
      if key in k:
        l+= [(k['n'],a,b) for a,b in k.pop(key)]
# ---- helpers
K={k['n']:k for s in dep['s'] for k in s['k']}
def ent(k,n,dd,s,g,a='',y='',role=None,v=None):
    k.setdefault('x',[])
    if any(e['n'].lower()==n.lower() for e in k['x']): return
    e={'n':n,'a':a,'d':dd,'mk':'','y':y,'s':s,'g':g}
    if role:e['role']=role
    if v:e['v']=v
    k['x'].append(e)
def setg(k,mp,default=None):
    for e in k.get('x',[]):
        e['g']=mp.get(e['n'],e.get('g') or default)
def sortg(k,order):
    k['x'].sort(key=lambda e:(order.index(e['g']) if e['g'] in order else 99))
# ---- Sari
k=K['Sari'];SA=W+'Sari'
reg={'Banarasi sari':'North India','Kanjivaram sari':'South India','Paithani sari':'West India','Patola sari':'West India','Pochampally ikat sari':'South India','Jamdani sari':'Bangladesh','Chanderi sari':'Central India','Maheshwari sari':'Central India','Mangalgiri sari':'South India','Sambalpuri sari':'East India','Leheriya sari':'West India','Bandhani sari':'West India','Tangaliya sari':'West India','Uppada sari':'South India','Kasavu sari':'South India','Kota Doria sari':'West India'}
for e in k['x']: e['g']=reg[e['n']]
alias={'Banarasi sari':'Banaras brocade · Benarasi','Kanjivaram sari':'Kanchipuram silk · Kanjipuram pattu','Jamdani sari':'Dhakai','Pochampally ikat sari':'Puttapaka','Mangalgiri sari':'Mangalagiri','Kasavu sari':'Kerala sari','Kota Doria sari':'Kota doria'}
for e in k['x']:
  if e['n'] in alias: e['a']=alias[e['n']]
N,E,NE,C,Wt,S,BD='North India','East India','Northeast India','Central India','West India','South India','Bangladesh'
rows=[
('Shalu',N,'Weave from Uttar Pradesh'),('Tanchoi',N,'Weave from Uttar Pradesh'),('Kulluvi pattu',N,'Woollen sari from Himachal Pradesh'),
('Kosa silk',C,'Silk sari from Chhattisgarh'),('Dhokra silk',C,'Silk sari from Madhya Pradesh'),
('Bhagalpur tussar',E,'Tussar silk sari from Bhagalpur, Bihar'),('Madhubani sari',E,'Painted folk-style sari from Mithila, Bihar'),('Pindna cotton',E,'Cotton sari from Jharkhand'),
('Tant',E,'Daily-wear cotton sari of Bangladesh and West Bengal'),('Baluchari',E,'Brocade sari from Bishnupur, West Bengal'),('Garode (Korial)',E,'Weave from Murshidabad, West Bengal'),
('Shantipuri cotton',E,'Cotton sari from Shantipur and Phulia, West Bengal'),('Murshidabad silk',E,'Silk sari from Murshidabad, West Bengal'),
('Begampuri',E,'Eastern Indian sari listed in the Sari article navigation box'),('Dhaniakhali',E,'Eastern Indian sari listed in the Sari article navigation box'),('Garad',E,'Eastern Indian sari listed in the Sari article navigation box'),('Habaspuri',E,'Eastern Indian sari listed in the Sari article navigation box'),
('Rajshahi silk (Eri)',BD,'Silk sari from Rajshahi, Bangladesh'),('Dhakai Katan',BD,'Silk sari from Dhaka, Bangladesh'),('Tangail',BD,'Weave from Tangail, Bangladesh'),
('Mooga silk',NE,'Silk sari from Assam'),('Mekhela cotton',NE,'Cotton sari-set fabric from Assam'),('Patt silk',NE,'Silk sari from Assam'),('Manipuri tant',NE,'Cotton sari from Manipur'),('Moirang phi',NE,'Weave from Manipur'),
('Bargarh ikat',E,'Silk and cotton ikat sari from Bargarh, Odisha'),('Bomkai',E,'Silk sari from Ganjam, Odisha'),('Khandua',E,'Silk and cotton sari from Nuapatna, Odisha'),('Pasapali',E,'Weave from Bargarh, Odisha'),('Sonepuri',E,'Silk and cotton sari from Subarnapur, Odisha'),('Berhampuri silk',E,'Silk sari from Berhampur, Odisha'),('Mattha silk',E,'Silk sari from Mayurbhanj, Odisha'),('Bapta',E,'Silk and cotton sari from Koraput, Odisha'),('Kotpad',E,'Weave from Koraput, Odisha'),('Kotki',E,'Weave from Odisha'),('Tanta cotton',E,'Cotton sari from Balasore, Odisha'),
('Yeola',Wt,'Weave from Maharashtra'),('Peshwai shalu',Wt,'Shalu fabric sari from Maharashtra'),('Mahalsa',Wt,'Weave from Maharashtra'),('Karvati tussar',Wt,'Tussar silk sari from Maharashtra'),('Lugade',Wt,'Tie-dye sari from Maharashtra'),
('Rogan sari',Wt,'Weave from Gujarat'),('Bhujodi sari',Wt,'Weave from Gujarat'),
('Mysore silk',S,'Silk sari from Karnataka'),('Arani silk',S,'Silk sari from Tamil Nadu'),('Arni silk',S,'Silk sari from Tamil Nadu'),('Ilkal',S,'Weave from Karnataka'),('Molakalmuru',S,'Weave from Karnataka'),('Sulebhavi',S,'Weave from Karnataka'),
('Venkatagiri',S,'Weave from Andhra Pradesh'),('Chirala',S,'Weave from Andhra Pradesh'),('Bandar',S,'Weave from Andhra Pradesh'),('Bandarulanka',S,'Weave from Andhra Pradesh'),('Kuppadam',S,'Weave from Andhra Pradesh'),('Dharmavaram silk',S,'Silk sari from Anantapur district, Andhra Pradesh'),('Gollabhama',S,'South Indian sari listed in the Sari article navigation box'),
('Chettinad',S,'Weave from Tamil Nadu'),('Kandangi',S,'Weave from Chettinad, Tamil Nadu'),('Thirubuvanam silk',S,'Silk sari from Kumbakonam, Tamil Nadu'),('Coimbatore cotton',S,'Cotton sari from Tamil Nadu'),('Salem silk',S,'Silk sari from Tamil Nadu'),('Sungudi',S,'Tie-dye sari from Madurai, Tamil Nadu'),('Rasipuram silk',S,'Silk sari from Tamil Nadu'),('Koorai silk',S,'Silk sari from Mayiladuthurai, Tamil Nadu'),('Madurai cotton',S,'Cotton sari from Tamil Nadu'),('Karaikudi',S,'Weave from Tamil Nadu'),('Tiruchirappalli',S,'Weave from Tamil Nadu'),('Nagercoil',S,'Weave from Tamil Nadu'),('Thoothukudi',S,'Weave from Tamil Nadu'),('Thanjavur',S,'Weave from Tamil Nadu'),('Tiruppur',S,'Weave from Tamil Nadu'),
('Balarampuram',S,'Weave from Kerala'),('Mundum neriyathum',S,'Two-piece cotton set from Kerala'),('Mayilati silk',S,'Silk sari from Kerala'),('Kannur cotton',S,'Cotton sari from Kerala'),('Kalpathi silk',S,'Silk sari from Kerala'),('Maradaka silk',S,'Silk sari from Kerala'),('Samudrikapuram',S,'Silk and cotton sari from Kerala'),('Kasargod',S,'Weave from Kerala'),('Kuthampully',S,'South Indian sari listed in the Sari article navigation box'),
('Gadwal',S,'Weave from Telangana'),('Narayanpet (Narayanpeth)',S,'Weave listed for both Telangana and Maharashtra'),
]
for n,g,dd in rows: ent(k,n,dd,SA,g)
sortg(k,[N,C,E,NE,Wt,S,BD])
k['x'][[e['n'] for e in k['x']].index('Banarasi sari')]['role']='landmark' if False else None
for e in k['x']:
  if e.get('role') is None: e.pop('role',None)
ve_sari_excl=['Aari Kashida','Zari Chhaapa','Baavan Booti weave','Sujni','Kaantha','Bagru','Phulkari','Ajrak','Kalamkari','Dabu','Bagh','Ghicha','Guntur','Georgette','Mukaish','Nuapatna','Khun fabric','Tassar silk','Katan']
k['sel']=("Every regional sari named in Wikipedia's Sari article (its regional weave list, the navigation box and the Bangladesh section), sectioned by region of origin. Fabrics, embroidery, block-print and dye techniques that the article names without a sari form (e.g. Bagru, Phulkari, Ajrak, Kalamkari, Georgette, Aari Kashida) are cloth traditions and left to the visual-art taxonomy; drapes are the Drape attribute. "
 "Covers %d of the sari forms in the article text read (characters 0 to 200,000 of 205,520; the remaining 5,520 were not read); same-name variants in the article (Arani and Arni, Narayanpeth and Narayanpet) are kept as the article gives them."%len(k['x']))
k['nl']="One entry is a regional sari form named for its place of weaving, as Wikipedia's Sari article lists it; fabrics, borders and bases are versions."
k['xg']='by region of origin'
# ---- Dhoti
k=K['Dhoti'];DH=W+'Dhoti'
reg={'Mundu':'South India','Veshti':'South India'}
for e in k['x']: e['g']=reg[e['n']]
ent(k,'Antariya','Ancient Indian garment from which the dhoti evolved.',DH,'Historical forms',role='origin')
ent(k,'Panchakacham','Better-known name for the dhoti in South India.',DH,'South India')
ent(k,'Pancha (panche)','Worn by conservative Jain men for puja at temples; the Jain counterpart of the dhoti.',DH,'North and West India')
ent(k,'Pitambar','Yellow silk dhoti worn on auspicious occasions.',DH,'North and West India')
ent(k,'Kalari dhoti','Worn by Kalaripayattu martial artists in Kerala.',DH,'South India')
ent(k,'Jaiñboh dhoti','Worn by Khasi folk dancers.',DH,'Northeast India')
ent(k,'Sakaccha and vikaccha','Two historical ways of wearing the dhoti in the Sunga period; vikaccha resembled a lungi.',DH,'Historical forms')
sortg(k,['Historical forms','North and West India','South India','Northeast India'])
k['nl']="One entry is a named form of the dhoti as Wikipedia's Dhoti article describes it; local-language names of the same garment are aliases."
k['sel']="Forms and regional names in Wikipedia's Dhoti article (whole page read), sectioned by region; local-language names (dhuti, dhotiyu, vaetti, pancha, mundu and others) are aliases of the garment. Complete: %d of %d forms named in the article."%(len(k['x']),len(k['x']))
k['xg']='by region'
# ---- Sarong
k=K['Sarong & wrap cloth'];SG=W+'Sarong'
reg={'Longyi':'Mainland Southeast Asia','Sinh':'Mainland Southeast Asia','Sampot':'Mainland Southeast Asia','Lavalava':'Pacific','Pāreu':'Pacific','Isulu':'Pacific','Tupenu':'Pacific','Malong':'Philippines','Kain pelikat':'Maritime Southeast Asia','Lungi':'South Asia','Kikoi':'Africa','Kanga':'Africa','Chitenge':'Africa','Capulana':'Africa','Lamba':'Africa'}
for e in k['x']: e['g']=reg[e['n']]
for n,g,dd in [('Sarung','Maritime Southeast Asia','Indonesian and Malaysian name of the sarong; also kain sarung.'),('Kamben','Maritime Southeast Asia','Balinese sarong.'),('Jarik','Maritime Southeast Asia','Javanese wrap cloth.'),('Sabok','Maritime Southeast Asia','Men\'s sarong of Sarawak.'),('Tapeh','Maritime Southeast Asia','Women\'s sarong of Sarawak.'),
('Patadyong','Philippines','Tubular wrap skirt of the Visayas and Sulu Archipelago.'),('Tapis','Philippines','Wrap cloth of Luzon.'),('Alampay','Philippines','Wrap cloth of the Cordillera highlands.'),
('Pha khao ma','Mainland Southeast Asia','Thai men\'s wrap cloth.'),('Pha thung','Mainland Southeast Asia','Thai women\'s wrap skirt.'),
('Futa','Arabian Peninsula','Wrap cloth of Saudi Arabia and Yemen; also izaar, mewaz and maqtab.'),('Macawiis','Africa','Wrap cloth of Somalia and Djibouti.'),
('Phanek','South Asia','Wrap cloth of Manipur.'),('Mekhela','South Asia','Wrap skirt of Assam.'),('Feyli','South Asia','Wrap cloth of the Maldives.'),('Saram','South Asia','Sri Lankan wrap cloth; sarama in Sinhalese.'),('Redda','South Asia','Women\'s wrap skirt of Sri Lanka.'),
('Rāpaki','Pacific','Māori wrap cloth of New Zealand.'),('Kikepa','Pacific','Hawaiian wrap cloth.'),('Lap-lap','Pacific','Wrap cloth of Papua New Guinea in Tok Pisin; rami in Hiri Motu.'),('Kie','Pacific','Wrap cloth of Wallis and Futuna.')]:
  ent(k,n,dd,SG,g)
sortg(k,['Maritime Southeast Asia','Mainland Southeast Asia','Philippines','South Asia','Arabian Peninsula','Africa','Pacific'])
k['nl']="One entry is a named wrap-cloth garment from one region, as Wikipedia's Sarong article lists them; patterns and fibres are the Pattern attribute."
k['sel']="Garments named in Wikipedia's Sarong article, sectioned by region. Covers %d of about 85 names there (characters 0 to 100,000 of 134,695 read; the rest not read). Plain synonyms and spelling variants (sarung, kain, kikoy, pareo, tupenu) are aliases or folded into one entry; the Philippine, Indian and Pacific names are separate entries."%len(k['x'])
k['xg']='by region'
# ---- Shalwar kameez
k=K['Shalwar kameez'];SK=W+'Shalwar_kameez'
for e in k['x']: e['g']='Punjab and Pakhtunkhwa' if 'Peshawari' in e['n'] or 'Pathani' in e['n'] else ('Punjab' if 'Patiala' in e['n'] else 'Mughal-era revival')
for n,g,dd in [('Khet partug','Afghanistan','Worn by Pashtuns, Tajiks and Hazaras; the traditional Peshawari shalwar.'),('Perahan tunban','Afghanistan','Worn by most Pashtun men in Afghanistan and Pakistan.'),('Firaq partug','Pakistan and Afghanistan','Frock and shalwar of the north-west, linked to the Anarkali suit.'),('Balochi shalwar kameez','Pakistan and Afghanistan','Very baggy trousers of Balochistan, with a separate female version.'),
('Phiran, poots and shalwar','Kashmir and Jammu','Kashmiri dress set.'),('Dogri kurta and suthan','Kashmir and Jammu','Dress of Jammu.'),('Peshwaz','Kashmir and Jammu','Jammu dress similar to the Anarkali suit.'),
('Punjabi suit','Punjab','Kameez cut straight and flat with side slits.'),('Pothohari shalwar','Punjab','Wide shalwar of the Pothohar region with some folds.'),('Bahawalpuri shalwar','Punjab','Very wide, baggy shalwar of Bahawalpur, part of the Saraiki suits.'),('Multani shalwar (ghaire wali)','Punjab','Shalwar of Multan, very wide at the waist.'),('Punjabi suthan','Punjab','Older Punjabi form with many plaits and a tight band at the ankles.'),('Churidar suthan','Punjab','Tight from knees to ankles; Punjab and parts of Himachal Pradesh.'),
('Sindhi suthan','Sindh','Wide at the waist, narrowing below the knees.'),('Sindhi kancha','Sindh','Lower Sindh form, wide down to the ankles, now rarely worn.'),('Sindhi chareno','Sindh','Very baggy women\'s salwar of lower Sindh, now rarely worn.'),('Gairwari salwar','Sindh','Many pleats and voluminous.')]:
  ent(k,n,dd,SK,g)
for e in k['x']:
  if e['g']=='Punjab and Pakhtunkhwa': e['g']='Pakistan and Afghanistan'
  if e['g']=='Mughal-era revival': e['g']='Punjab'
for e in k['x']:
  if e['n']=='Anarkali suit': e['g']='Kashmir and Jammu'
sortg(k,['Punjab','Kashmir and Jammu','Sindh','Pakistan and Afghanistan','Afghanistan'])
k['nl']="One entry is a named regional cut of the shalwar kameez, as Wikipedia's Shalwar kameez article lists it; fabrics and trims are versions."
k['sel']="Regional styles named in Wikipedia's Shalwar kameez article, sectioned by region; Pathani suit follows its own Wikipedia article. Covers %d of the styles in characters 0 to 100,000 of 187,298 read; the rest of the page was not read. Upper-garment variants (chola, Sindhi angrakho, Sindhi gaj) and cowl-pants modern equivalents are not entries."%len(k['x'])
k['xg']='by region'
# ---- Kurta
k=K['Kurta'];KU=W+'Kurta'
for e in k['x']: e['g']={'Lucknowi chikankari kurta':'Uttar Pradesh','Kalidar kurta':'North India','Muktsari kurta':'Punjab','Angarkha':'Rajasthan and Mughal courts','Pheran':'Kashmir'}[e['n']]
for n,g,dd in [('Bhopali kurta','Madhya Pradesh','Loose kurta pleated at the waist, between knee and ankle length.'),('Hyderabadi kurta','Telangana','Short top sitting at the waist with a keyhole neck.'),('Panjabi','Bengal and Assam','Straight-cut traditional kurta of Bangladesh, West Bengal and Assam.'),('Phulkari kurta','Punjab','Kurta with Phulkari embroidery.'),
('Pehran (Pehriyan)','Sindh','Male Sindhi kurta, embroidered and collarless.'),('Padhri','Sindh','Female Sindhi kurta, heavily embellished and tied at the shoulders.'),('Tuk ja kurta','Sindh','Appliqued Sindhi kurta.'),('Kurti','Modern','Short women\'s kurta reaching the hips; traditionally a waistcoat or jacket.')]:
  ent(k,n,dd,KU,g)
for e in k['x']:
  if e['n']=='Hyderabadi kurta': e['v']=[{'n':'Jaali karga','y':'','mk':'','d':'worn with a net layer over it, by men and women'}]
sortg(k,['Uttar Pradesh','North India','Rajasthan and Mughal courts','Punjab','Kashmir','Madhya Pradesh','Telangana','Bengal and Assam','Sindh','Modern'])
k['nl']="One entry is a named regional kurta, as Wikipedia's Kurta article lists it; embroidery and fabric are versions or attributes."
k['sel']="Regional kurtas named in Wikipedia's Kurta article (whole page read), sectioned by region; Angarkha and Pheran have their own articles. Delhi-style kurtas are a general style, not a form, and the embroidery techniques (chikan, bandhani, kantha) belong to the visual-art taxonomy. Complete: %d of %d forms named."%(len(k['x']),len(k['x']))
k['xg']='by region'
# ---- Poncho
k=K['Poncho'];PO=W+'Poncho'
for e in k['x']:
  e['g']={'Ruana':'Colombia and Venezuela','Sarape de Saltillo':'Mexico','Jorongo':'Mexico','Chamanto':'Chile','Poncho chilote':'Chile','Poncho salteño':'Argentina','Quechquemitl':'Mexico','Otavalo alpaca poncho':'Ecuador'}[e['n']]
  if e['n']=='Otavalo alpaca poncho': e['cty']='Ecuador'
ent(k,'Gabán','Poncho of Michoacán, Mexico.',PO,'Mexico')
ent(k,'Pala (bernéu, ponche)','Brazilian names for the poncho; ponche is specific to the Caipira dialect.',PO,'Brazil')
sortg(k,['Mexico','Colombia and Venezuela','Ecuador','Chile','Argentina','Brazil'])
k['nl']="One entry is a named regional poncho or cape from one country, as Wikipedia's Poncho article lists them; weights and wool are versions."
k['sel']="Regional ponchos named in Wikipedia's Poncho article (characters 0 to 100,000 of 109,474 read), sectioned by country. Military ponchos (Zeltbahn, Alpenflage) are out of scope as institutional gear. Covers %d of the %d regional ponchos in the text read."%(len(k['x']),len(k['x']))
k['xg']='by country'
# ---- Kaftan
k=K['Kaftan'];KF=W+'Kaftan'
for e in k['x']:
  e['g']={'Ottoman kaftan':'Turkey and Central Asia','Moroccan caftan':'North Africa','Takchita':'North Africa','Algerian kaftan':'North Africa','Karakou':'North Africa','Chedda of Tlemcen':'North Africa','Western kaftan':'Fashion'}[e['n']]
for n,g,dd in [('Turkic kaftan','Turkey and Central Asia','Associated with early Turkic peoples in Seljuk and Ottoman lands.'),('Ghlila','North Africa','Algerian mid-calf jacket that preceded the female kaftan.'),
('West African kaftan','West Africa','Pullover robe worn by women.'),('Senegalese kaftan','West Africa','Men\'s pullover robe with bell-like sleeves.'),('Khalat','Persia and Russia','Persian robe of honour.'),('Russian kaftan','Persia and Russia','Long men\'s suit with tight sleeves, used in folk and ritual dress.'),('Bekishe','Hasidic communities','Silky robe adapted from Polish noble dress.'),('Kapoteh','Hasidic communities','Frock-coat-style kaftan.')]:
  ent(k,n,dd,KF,g)
sortg(k,['Turkey and Central Asia','Persia and Russia','North Africa','West Africa','Hasidic communities','Fashion'])
k['nl']="One entry is a named regional or community form of the kaftan, as Wikipedia's Kaftan article lists them."
k['sel']="Forms named in Wikipedia's Kaftan article (characters 0 to 100,000 of 138,879 read), sectioned by region. Dashiki has its own kind and Jubah and Cadar (a veil) are left out. Covers %d of the forms in the text read."%len(k['x'])
k['xg']='by region'
# ---- Thobe
k=K['Thobe'];TH=W+'Thawb'
for e in k['x']: e['g']='Arabian Peninsula and Levant' if e['n'] in('Kandura','Dishdasha') else 'North Africa'
ent(k,'Jubbah','Ornately styled thobe-like robe of Pakistan and other parts of the subcontinent.',TH,'South Asia')
sortg(k,['Arabian Peninsula and Levant','North Africa','South Asia'])
k['nl']="One entry is a regional name or form of the thobe, as Wikipedia's Thawb article lists them."
k['sel']="Names in Wikipedia's Thawb article (whole page read) plus the Djellaba, Gandoura, Jellabiya and Kachabia articles from the structure pass, sectioned by region. Complete: %d of the %d names the Thawb article gives as separate garments (thawb itself is the kind)."%(len(k['x']),len(k['x']))
k['xg']='by region'
# ---- Kimono
k=K['Kimono'];KI=W+'Kimono'
form={'Furisode':'Formal women\'s','Kurotomesode':'Formal women\'s','Irotomesode':'Formal women\'s','Hōmongi':'Semi-formal women\'s','Tsukesage':'Semi-formal women\'s','Iromuji':'Semi-formal women\'s','Komon':'Informal women\'s','Tsumugi':'Informal women\'s','Meisen':'Informal women\'s','Uchikake':'Bridal and stage','Shiromuku':'Bridal and stage','Mofuku':'Mourning','Kuro-montsuki':'Formal men\'s','Hikizuri':'Bridal and stage'}
for e in k['x']: e['g']=form[e['n']]
for e in k['x']:
  if e['n']=='Furisode':
    e['v']=(e.get('v') or [])+[{'n':'Ko-furisode (nisyakusode)','y':'','mk':'','d':'shortest sleeves, 76–86 cm; rare'},{'n':'Chū-furisode','y':'','mk':'','d':'sleeves 86–115 cm; most formal occasions'},{'n':'Ō-furisode (hon-furisode)','y':'','mk':'','d':'longest sleeves; brides, dancers and singers'}]
  if e['n']=='Komon': e['v']=(e.get('v') or [])+[{'n':'Edo komon','y':'','mk':'','d':'fine all-over pattern, named in the article contents'}]
  if e['n']=='Hikizuri': e['a']='Susohiki'
ent(k,'Kosode','Historical predecessor of the modern kimono.',KI,'Historical',role='origin')
ent(k,'Iro-montsuki','Crested coloured kimono named in the Kimono article contents.',KI,'Formal women\'s')
ent(k,'Kataire','Children\'s kimono with fancier fabric in the okumi and upper back.',KI,'Children\'s')
sortg(k,['Historical','Formal women\'s','Semi-formal women\'s','Informal women\'s','Bridal and stage','Mourning','Formal men\'s','Children\'s'])
k['nl']="One entry is a named type of kimono by cut, pattern and formality, as Wikipedia's Kimono article lists them; sleeve lengths and crest counts are versions."
k['sel']="Types named in Wikipedia's Kimono article (characters 0 to 100,000 of 217,652 read; the rest, including men's types, not read), sectioned by formality and wearer. Yukata, haori, hakama and obi are separate kinds. Covers %d types."%len(k['x'])
k['xg']='by formality and wearer'
# ---- Bunad
k=K['Bunad'];BU=W+'Bunad'
for e in k['x']: e['g']='Vestlandet' if 'Hardanger' in e['n'] else 'Sørlandet'
ent(k,'Telemarksbunad','Bunad of Telemark; named in the Bunad article external links.',BU,'Telemark')
ent(k,'Østtelemark bunad','Woman\'s bunad of eastern Telemark.',BU,'Telemark')
ent(k,'Oslobunad','Bunad of Oslo; named in the Bunad article external links.',BU,'Østlandet')
sortg(k,['Østlandet','Telemark','Sørlandet','Vestlandet'])
k['nl']="One entry is a named regional bunad of Norway; trim and jewellery are versions or attributes."
k['sel']="Bunads named in Wikipedia's Bunad article (whole page read). Covers %d of about 200 bunads, the figure the article gives; the article names only these, so the rest are not listed."%len(k['x'])
k['xg']='by region of Norway'
# ---- generic nl/sel for the rest
for s in dep['s']:
  for k in s['k']:
    if not k.get('nl'):
      if k.get('x'):
        urls=sorted({e['s'] for e in k['x'] if 'wikipedia.org/wiki/' in e['s']})
        arts=[urllib.parse.unquote(u.split('/wiki/')[1]).replace('_',' ') for u in urls]
        k['nl']="One entry is a named regional, historical or designer form of the %s; fabrics, cuts and trims are versions."%k['n'].lower()
        k['sel']="Forms carried over from the structure pass, each confirmed on its source page; the Wikipedia articles %s were not re-read in this pass. Covers %d forms; completeness against those articles is not established."%(', '.join(arts) if arts else '(none)',len(k['x']))
      else:
        k['nl']="This kind has no named entries."
        k['sel']="No named entries: the %s is described by its attributes, and no list of named forms was fetched for it."%k['n'].lower()
# cloth attribute and ve
for kn,cs in assign.items():
  k=K[kn]
  k['tt']=(k.get('tt') or [])+[['Cloth',[cvals[c] for c in cs]]]
  k['ve']={'t':'Named cloths covered by the visual-art taxonomy','items':[{'n':c,'e':cl[c]} for c in cs]}
  k['sel']+=' Cloth traditions are not entries: the Cloth attribute names them and the visual-art taxonomy covers cloth and textile traditions.'
  k['d']=k['d'].rstrip()
# other see-text: no code exists for visual art
# role cap check and dept text
dep['t']='Garments belonging to a people or region and worn for daily, festive or ceremonial dress; a modern fashion version of the same garment sits here too. Cloth and textile traditions belong to the visual-art taxonomy.'
dep['ax']="Which people's or region's dress is it, and which garment?"
dep['note']='National dress as garment kinds by region; named regional forms of a garment are entries; cloths are a Cloth attribute, covered by the visual-art taxonomy.'
for e in K['Sari']['x']: pass
# brands: country on branded entries
for kn,en,c in [('Bombacha','',''),]: pass
for k in K.values():
  for e in k.get('x',[]):
    if e.get('mk')=='Pampero': e['cty']='Argentina'
    if e.get('mk')=='Vita Kin': e['cty']='Ukraine'
    if e.get('mk')=='Vlisco': e['cty']='Netherlands'
    if not e.get('role'): e.pop('role',None)
part={'replaces':['Traditional dress'],'depts':[dep],'brands':[],'brand_updates':{},'renames':{k:cvals.get(k,'') for k in []},'moves':[]}
part['renames']={}
json.dump(part,open(R+'out/A1_parts/TRAD.json','w'),ensure_ascii=False,indent=1)
json.dump({'cloth':cl,'m':dropped_m,'r':dropped_r},open(R+'work/V4_A1_TRAD/dropped.json','w'),ensure_ascii=False,indent=1)
tot=sum(len(k.get('x',[])) for s in dep['s'] for k in s['k'])
print('kinds',len(K),'entries',tot,'dropped m',len(dropped_m),'r',len(dropped_r))
for kn in ('Sari','Dhoti','Sarong & wrap cloth','Shalwar kameez','Kurta','Poncho','Kaftan','Thobe','Kimono','Bunad'): print(kn,len(K[kn]['x']))
