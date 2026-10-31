import json,re
R='/home/user/Possession-Taxonomy/'
S=json.load(open(R+'rebuild/work/V4_A1_OUTER/stage1.json'))
REG={x['n'].lower() for x in json.load(open(R+'rebuild/out/A1_brands.json'))['b']}
W='https://en.wikipedia.org/wiki/'
ART={'Overcoat':('Overcoat; Trench coat',0),'Pea coat':('Pea coat',0),'Duffle coat':('Duffel coat',0),'Trench coat':('Trench coat',0),
'Raincoat':('Raincoat',0),'Parka':('Parka',0),'Puffer coat':('Down jacket',0),'Puffer jacket':('Down jacket',0),'Puffer vest':('Gilet',0),
'Cape':('Cape',0),'Flight jacket':('Flight jacket; Bomber jacket',0),'Field jacket':('Trench coat; Safari jacket',0),'Biker jacket':('Perfecto motorcycle jacket',0),
'Waxed cotton jacket':('Waxed jacket',0),'Mackinaw':('Mackinaw coat',1),'Norfolk jacket':('Norfolk jacket',0),'Trucker jacket':('Jean jacket',0),
'Harrington jacket':('Harrington jacket',0),'Varsity jacket':('Letterman (sports)',0),'Track jacket':('Tracksuit',0),'Tracksuit':('Tracksuit',0),
'Bolero':('Bolero jacket',0),'Shell jacket':('Parka',0),'Anorak':('Parka',0),'Fleece jacket & pullover':('Polar fleece',0),
'Business suit':('Suit',168380),'Blazer':('Blazer',0),'Waistcoat':('Waistcoat',110474),'Tuxedo':('Tuxedo',190725),'Morning dress':('Morning dress; Tuxedo',142835),
'Tailcoat':('Tailcoat',0),'Smoking jacket':('Smoking jacket',0),'Tie':('Necktie',157287),'Bow tie':('Bow tie',0),'Ascot & cravat':('Bow tie; Necktie',157287),
'Cummerbund & collar stay':('Cummerbund',0),'Pocket square':('Handkerchief',0),'Braces':('Suspenders',0),'Work trousers':('Overalls',0),
'Overalls':('Overalls',0),'Boiler suit':('Boilersuit',0),'Chore coat':('Chore jacket',0),'Work jacket':('Chore jacket',0),'Donkey jacket':('Donkey jacket',0),
"Chef's jacket":("Chef's uniform",0),'Scrub top':('Scrubs (clothing)',0),'Lab coat':('Lab coat',0)}
TRUNC={'Mackinaw':'6,937 of 106,937','Business suit':'68,380 of 168,380','Waistcoat':'10,474 of 110,474','Tuxedo':'90,725 of 190,725','Morning dress':'42,835 of 142,835','Tie':'57,287 of 157,287','Ascot & cravat':'57,287 of 157,287'}
cnt=0
for dp in S['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            x=k.get('x',[])
            b=sum(1 for e in x if e['g']!='Named forms without a brand'); f=len(x)-b
            art=ART.get(k['n'])
            if x:
                a=art[0] if art else 'the garment article named in s'
                line=f"Follows two references: the register's signature pieces and lines for this garment (each on the brand page named in s) and the brands and named types in Wikipedia: {a}."
                cov=f" Complete: {b} of {b} brand pieces in the register for this garment, {f} named forms from the fetched article."
                if k['n'] in TRUNC: cov=f" Covers {len(x)} entries; the article was read to its first 100,000 characters and the last {TRUNC[k['n']].split(' of ')[0]} characters were not read."
                k['sel']=line+cov+" Brands outside the 2,531-brand register are not listed."
            else:
                k['sel']=("No entries. "+(f"The fetched Wikipedia article ({art[0]}) names no brand or list of named types for this garment. " if art else "No Wikipedia article on this garment was fetched. ")+"No signature piece in the brand register matches it. Complete: 0 of 0.")
            cnt+=1
    dp['msum']=("No market-share figure for this department was found on a fetched page, so the department has no market table. Entries are grouped by the brand's home country; owners are given only where the brand register's page states them.")
# brands
new=[
 ('Eddie Bauer','United States','Outdoor brand named in the Down jacket article for the 1936 Skyliner.',W+'Down_jacket','Outdoor & technical'),
 ('Peter Storm','United Kingdom','Maker of the cagoule, credited to Noel Bibby in the early 1960s.',W+'Parka','Outdoor & technical'),
 ('Castell & Son','United Kingdom','Oxford firm opened in 1846, credited with the first modern-style necktie in 1870.',W+'Necktie','Heritage & workwear'),
 ('Gannex','United Kingdom','Raincoat style named in the Raincoat article.',W+'Raincoat','Heritage & workwear'),
 ('Driza-Bone','Australia','Oilskin coat style named in the Raincoat article.',W+'Raincoat','Heritage & workwear'),
 ("Hudson's Bay Company",'Canada','Supplier of point blankets and later of the point blanket coat.',W+'Mackinaw_coat','Heritage & workwear'),
 ('Blue Bell','United States','North Carolina overall maker begun in 1904, popular with railroad workers.',W+'Overalls','Heritage & workwear'),
 ('Grenfell','United Kingdom','Formerly Haythornthwaite and Sons; claims an identical golf jacket to Baracuta\'s.',W+'Harrington_jacket','Heritage & workwear'),
 ('Le Coq Sportif','France','French sportswear maker said to have first made sweatpants in 1920.',W+'Tracksuit','Athletic & sportswear'),
 ('One-In-Hand Tie Company','United States','Clinton, Iowa, maker of pre-tied and clip-on neckties.',W+'Necktie','Heritage & workwear'),
 ('Jesse Langsdorf','United States','New York tie maker who introduced bias-cut ties in 1922.',W+'Necktie','Heritage & workwear'),
 ('George Key','United Kingdom','Rugeley draper who developed the donkey jacket in 1888.',W+'Donkey_jacket','Heritage & workwear'),
]
brands=[{'n':n,'c':c,'f':'1846' if n=='Castell & Son' else ('1904' if n=='Blue Bell' else ''),'seg':seg,'d':d,'lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':s,'kf':''} for n,c,d,s,seg in new if n.lower() not in REG]
segs=set(json.load(open(R+'rebuild/out/A1_brands.json'))['b'][i]['seg'] for i in range(2531))
print('segs',sorted(segs))
OWN={'Aquascutum':('Shandong Ruyi','Independent',''),"Arc'teryx":('Amer Sports','Global group',''),'Mackintosh':('Yagi Tsusho','Independent',''),'Napapijri':('VF Corporation','Global group','2004'),'Rab':('Equip','Independent',''),'Stone Island':('Moncler','Global group','2020'),'The North Face':('VF Corporation','Global group','2000'),'DAKS':('Sankyo Seiko','Independent','1991'),"OshKosh B'gosh":("Carter's",'Global group',''),'Stubbies':('Workwear Group','Independent',''),'Fjällräven':('Fenix Outdoor','Independent',''),'Lacoste':('Maus Frères','Independent','')}
bu={n:{'own':o[0],'tier':o[1],'c':{x['n']:x.get('c','') for x in json.load(open(R+'rebuild/out/A1_brands.json'))['b']}[n]} for n,o in OWN.items()}
for n,o in OWN.items():
    if o[2]: bu[n]['own_y']=o[2]
import os
os.makedirs(R+'rebuild/out/A1_parts',exist_ok=True)
for dp in S['depts']:
    for sh in dp['s']:
        for k in sh['k']:
            for e in k.get('x',[]):
                if e.get('mk')=='DuPont': e['g']='United States';e['cty']='United States'
part={'replaces':['Coats & jackets','Suits & formalwear','Workwear & uniform clothing'],'depts':S['depts'],'brands':brands,'brand_updates':bu,'renames':{},'moves':[]}
json.dump(part,open(R+'rebuild/out/A1_parts/OUTER.json','w'),ensure_ascii=False,indent=0)
print(len(brands),'new brands',os.path.getsize(R+'rebuild/out/A1_parts/OUTER.json'))
