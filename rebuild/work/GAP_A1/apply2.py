import json,os
R='/home/user/Possession-Taxonomy/rebuild/out/'
B=json.load(open(R+'A1_brands.json')); bm={x['n']:x for x in B['b']}
tiers={}
for x in B['b']:
    if x.get('own') and x.get('tier'): tiers.setdefault(x['own'],x['tier'])
GG={'Authentic Brands Group','WHP Global','Marquee Brands','Gildan','Pentland Group','Prada Group','Wolverine World Wide','Frasers Group','G-III Apparel Group','Iconix Brand Group','Fanatics'}
W='https://en.wikipedia.org/wiki/'
# name: (own, own_y, wiki title or None)
D={
'Ben Sherman':('Marquee Brands',None,'Ben_Sherman'),
'Fred Perry':('Hit Union Co',1995,'Fred_Perry_(clothing_label)'),
'N.Peal':('Adam Holdsworth',None,'N.Peal'),
'Barbour':('J. Barbour & Sons Limited',None,'Barbour_(company)'),
'Charvet':('Chanel',None,'Charvet'),
'Gant':('Maus Frères',None,'Gant_(company)'),
'Tori Richard':('Tori Richard (family-owned)',None,'Tori_Richard'),
'Carhartt':('Descendants of Hamilton Carhartt',None,'Carhartt'),
'Diesel':('OTB Group',None,'Diesel_(company)'),
'3sixteen':('Andrew Chen and Johan Lam',None,'3sixteen'),
"Hudson's Bay Company":('NRDC Equity Partners',2008,'Hudson%27s_Bay_Company'),
'Momotaro Jeans':('Daidoh Ltd',2025,'Momotaro_Jeans'),
'Nudie Jeans':('Svenska Jeans Holding AB',None,'Nudie_Jeans'),
'R.M. Williams':('Tattarang',None,'R._M._Williams_(company)'),
'Reigning Champ':('Aritzia',2021,'Reigning_Champ'),
'Bonobos':('Express, Inc.',2023,'Bonobos_(apparel)'),
'Craghoppers':('Regatta Group',None,'Craghoppers'),
'Duck Head':('Oxford Industries',None,'Duck_Head'),
"Jimmy'z":('Authentic Brands Group',None,'Jimmy%27z'),
'Red Kap':('Workwear Outfitters',2021,'Red_Kap'),
'Rip Curl':('KMD Brands',None,'Rip_Curl'),
'American Apparel':('Gildan',None,'American_Apparel'),
'Roots Canada':('Searchlight Capital Partners',2015,'Roots_Canada'),
'Schiaparelli':('Tod\'s Group',None,'Schiaparelli_(fashion_house)'),
'Sweaty Betty':('Wolverine World Wide',2021,'Sweaty_Betty'),
'Biba':('House of Fraser',None,'Biba'),
'Gunne Sax':('Jessica McClintock, Inc.',None,'Gunne_Sax'),
'Laura Ashley':('Marquee Brands',2025,'Laura_Ashley_(company)'),
'Pronovias':('Bain Capital and MV Credit',2023,'Pronovias'),
'Vera Wang':('WHP Global',2024,'Vera_Wang'),
'Versace':('Prada Group',2025,'Versace'),
'Crombie':('Crombie 1805 Ltd',None,'Crombie_(clothing)'),
'Driza-Bone':('S. Kidman & Co',None,'Driza-Bone'),
'Hunter':('Pall Mall Legacy',None,'Hunter_Boot_Ltd'),
'London Fog':('Iconix Brand Group',None,'London_Fog_(company)'),
'Magee of Donegal':('Temple family',None,'Magee_of_Donegal'),
'Morphsuits':('AFG Media',None,'Morphsuits'),
'Montgomery Ward':('Colony Brands',None,'Montgomery_Ward'),
'Aigle':('Maus Frères',2005,'Aigle_(company)'),
'Avirex':('Centric Brands',None,'Avirex'),
'Belstaff':('Castore',2025,'Belstaff'),
'Corneliani':('Investcorp',2016,'Corneliani'),
'Mammut':('Jacobs Capital',2021,'Mammut_Sports_Group'),
'Anderson & Sheppard':('Anda Rowland',2004,'Anderson_%26_Sheppard'),
"Drake's":('Mark Cho and Michael Hill',None,"Drake%27s_(haberdashers)"),
'Henry Poole & Co':('Cundey family',None,'Henry_Poole_%26_Co'),
'KingGee':('Workwear Group',None,'KingGee'),
'Rubinacci':('Rubinacci family',None,'Rubinacci'),
'Zegna':('Zegna family',None,'Zegna'),
'Akubra':('Tattarang',2023,'Akubra'),
'Borsalino':('Haeres Equita',None,'Borsalino'),
'Charnos':('Pour Moi Ltd',2019,'Charnos'),
'Ebbets Field Flannels':('Lids',None,'Ebbets_Field_Flannels'),
'Kangol':('Frasers Group',None,'Kangol'),

'Vilebrequin':('G-III Apparel Group',None,'Vilebrequin'),
'Von Dutch':('WSG Brands',2024,'Von_Dutch'),
'Wigwam Mills':('Margaret Newhard and Chris Chesebro',None,'Wigwam_Mills'),
'Cia. Hering':('Soma',None,'Cia._Hering'),
'Dents':('Dewhurst Dent plc',None,'Dents'),
'Gymshark':('Ben Francis (General Atlantic holds 21 %)',None,'Gymshark'),
'Merz b. Schwanen':('Peter Plotnicki',None,'Merz_b._Schwanen'),
'Canterbury of New Zealand':('Pentland Group',2012,'Canterbury_of_New_Zealand'),
'Mitchell & Ness':('Fanatics',2022,'Mitchell_%26_Ness'),
'Umbro':('Iconix Brand Group',2012,'Umbro'),
'Le Coq Sportif':('Airesis S.A.',None,'Le_Coq_Sportif'),
'Hermès':('Hermès family',None,'Herm%C3%A8s'),
'Hongdu':('Aviation Industry Corporation of China',None,'Hongdu'),
'Tootal':('Coats Viyella',None,'Tootal'),
'Norrøna':('Jørgensen family',None,'Norr%C3%B8na'),
'Pampero':('Grupo Cardon',None,'Pampero'),
'Cimalp':('Manufacture Drômoise de Confection',None,'Cimalp'),
'Krizia':('Shenzhen Marisfrolg',None,'Krizia'),
'Tilley':('Gibraltar & Company',2018,'Tilley_Endurables'),
'Gieves & Hawkes':('Frasers Group',2022,''),
'Gul Ahmed':('Gul Ahmed Group',None,''),
'E. Marinella':('Marinella family',None,''),
'Loden-Frey':('Loden-Frey family',None,''),
'Rowing Blazers':('Burch Creative Capital',2024,''),
'Shukr':('Niswa Fashion',None,''),
}
extra=[]
for n,(own,y,t) in D.items():
    x=bm.get(n)
    if not x: extra.append(n); continue
    if x.get('own'): continue
    x['own']=own
    x['tier']=tiers.get(own) or ('Global group' if own in GG else 'Independent')
    if y: x['own_y']=y
    if not x.get('s') or 'wikipedia' not in x['s']: pass
x=bm['Eres']; x['tier']='Independent'
json.dump(B,open(R+'A1_brands.json.tmp','w'),ensure_ascii=False); os.replace(R+'A1_brands.json.tmp',R+'A1_brands.json')
print('missing names',extra); print(sum(1 for x in B['b'] if x.get('own')))
