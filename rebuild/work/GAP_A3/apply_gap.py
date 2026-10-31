import json,re,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/A3.json'))
def kinds():
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']: yield dp,s,k
def find(n):
    for dp,s,k in kinds():
        if k['n']==n: return k
def shelf(n):
    for dp,s,k in kinds():
        if s['n']==n: return s
W='https://en.wikipedia.org/wiki/'
# --- house entries
def own_all(kn,own,tier=None,own_y=None):
    for e in find(kn)['x']:
        e['own']=own
        if tier: e['tier']=tier
        if own_y: e['own_y']=own_y
own_all('Harry Winston jewellery lines','The Swatch Group','Global group','2013')
own_all('Chopard jewellery lines','Scheufele family','Independent','1963')
own_all('Mikimoto jewellery lines','Privately held (owner not named)')
own_all('Georg Jensen jewellery lines','Fiskars Group',None,'2023')
own_all('Monica Vinader lines','Bridgepoint Development Capital (majority)')
own_all('Thomas Sabo jewellery lines','Privately held (owner not named)')
own_all('Chow Sang Sang collections','Chow Sang Sang Holdings International Limited')
own_all('Tanishq collections','Titan Company')
own_all('Kalyan Jewellers collections','Kalyan Jewellers (listed on BSE and NSE)')
own_all('Malabar Gold & Diamonds collections','M. P. Ahammed')
own_all('Graff jewellery lines','Family-owned (owner not named)')
def kd(kn,add): 
    k=find(kn); k['d']=(k.get('d','')+' '+add).strip()
kd('Harry Winston jewellery lines','Bought by the Swatch Group on 26 March 2013 for $1 billion.')
kd('Chopard jewellery lines','Founded 1860 at Sonvilier; owned by the Scheufele family since 1963.')
kd('Georg Jensen jewellery lines','Founded 1904 in Copenhagen; bought by Fiskars Group in December 2023 for EUR 155 million, from Investcorp.')
kd('Monica Vinader lines','Founded 2007; Bridgepoint Development Capital holds a majority stake (Wikipedia, year not given).')
kd('Tanishq collections','Owned by Titan Company of the Tata Group; sub-brands Mia (2011), Rivaah (2017), Mirayah (2017), Aveer (2017) are named on Wikipedia.')
kd('Kalyan Jewellers collections','Founded 1993 by T. S. Kalyanaraman; Warburg Pincus took a minority stake in 2014; listed after a 2021 IPO.')
kd('Malabar Gold & Diamonds collections','Founded 1993 by M. P. Ahammed; Wikipedia names no collections.')
kd('Chow Sang Sang collections','Listed in Hong Kong (code 116) since 1973; founded 1934 in Guangzhou.')
kd('Graff jewellery lines','Described by Sotheby\'s as family-owned and operated; founded 1960.')
kd('Mikimoto jewellery lines','Founded 1899; Wikipedia gives the company as privately held.')
kd('Thomas Sabo jewellery lines','Founded 1984 in Lauf an der Pegnitz; Wikipedia gives the company as private.')
# Qeelin
k=find('Qeelin jewellery lines'); k['d']='Chinese-heritage fine jewellery house founded in 2004; Kering acquired a majority stake in January 2013.'
q=[('Wulu','2004',"The house's first collection."),('Maggie\'s bangles','2010',''),('XiXi','2012',''),('Bo Bo','','Panda symbol; a limited-edition pendant was made in 2016.'),('Ling Long','',''),('Qin Qin','',''),('Wang Wang','','')]
for e in k['x']: e['own_y']='2013'
for n,y,dd in q:
    e={'n':n,'mk':'Qeelin','s':W+'Qeelin','v':[],'g':'Named in Wikipedia','own':'Kering','tier':'Global group','cty':'China','own_y':'2013'}
    if y: e['y']=y
    if dd: e['d']=dd
    k['x'].append(e)
k['sel']="The two collections linked on Qeelin's own home page (Yu Yi, Miracle Garden), then the seven collections named in Wikipedia's Qeelin article (read to its end). The site has no collections index. Complete: 9 of 9 named on those pages."
k['xg']='by source: home page, Wikipedia'
# Fred
k=find('Fred jewellery lines')
k['d']='Paris jeweller founded in 1936 by Fred Samuel; owned by the LVMH Group since 1995.'
fw=W+'Fred_Joaillier'
yrs={'Force 10':'1966 (launched 1978)','Ombre Féline':'2019','Chance Infinie':'2016 (as 8°0)'}
for e in k['x']:
    e.update({'own':'LVMH','tier':'Global group','own_y':'1995','g':'Main collections'})
    if e['n'] in yrs: e['y']=yrs[e['n']]
    e['s']=[e['s'],fw] if False else e['s']
for e in k['x']:
    if e['n']=='Force 10': e['v']=[{'n':'Force 10 interchangeable bracelet','mk':'Fred','y':'2007','d':''},{'n':'Force 10 #GoBeyond','mk':'Fred','y':'2020','d':''}]
    if e['n']=='Chance Infinie': e['v']=[{'n':'8°0','mk':'Fred','y':'2016','d':'original name; became Chance Infinie in 2020'}]
new=[('Success','2000','Main collections',''),('Pain de Sucre','2011','Main collections','Interchangeable ring added in 2013.'),('Riviera','2012–2015','Main collections','Includes Baie des Anges, Belles Rives and Une Ile d\'Or.'),('Pretty Woman','2021','Main collections','Reissue.'),
('Les Fredy\'s','1989','Historical and high jewellery','Mini-Fredy\'s followed in 1995; a collaboration with Jean-Paul Goude in 2009.'),('Mouvementé','1996','Historical and high jewellery',''),('Diamond Tag','2005','Historical and high jewellery',''),('Kate Moss for Fred','2011','Historical and high jewellery',''),('Monsieur Fred Inner Light','2022','Historical and high jewellery',''),('Monsieur Fred Ideal Light','2024','Historical and high jewellery','')]
for n,y,g,dd in new:
    e={'n':n,'mk':'Fred','y':y,'s':fw,'v':[],'g':g,'own':'LVMH','tier':'Global group','cty':'France','own_y':'1995'}
    if dd: e['d']=dd
    k['x'].append(e)
k['x'].sort(key=lambda e:(0 if e['g']=='Main collections' else 1))
k['sel']="Every collection linked on Fred's own English home page (3), then the collections and lines listed in Wikipedia's Fred Joaillier article (10 more; watch lines and the Force 10 eyewear are left out). Complete: 13 of 13 collections on the page and in the article."
k['xg']='by line type: main collections, historical and high jewellery'
# De Beers
k=find('De Beers jewellery lines')
for e in k['x']: pass
k['x'].append({'n':'Lightbox','mk':'De Beers','y':'2018','s':W+'De_Beers_Group','d':'Lab-grown diamond jewellery brand made with Element Six; announced May 2018, on sale September 2018, discontinued May 2025.','v':[],'g':'Named in Wikipedia','own':'Anglo American','tier':'Global group','cty':'United Kingdom'})
k['d']='Jewellery arm of the diamond company; De Beers Diamond Jewellers was set up in 2001 as a 50:50 venture with LVMH; De Beers Group bought LVMH\'s half in March 2017; renamed De Beers London in 2025.'
k['sel']="The collections linked on De Beers' own US home page (Lotus by De Beers, Undulation, Talisman, and a high jewellery thematic page), plus Lightbox from Wikipedia's De Beers Group article (read to its end; it names no other jewellery collection). Covers 4 lines named on those pages; De Beers publishes no full collections index in the retrieved pages."
# Swarovski, David Yurman, Mejuri, Malabar
k=find('Swarovski jewellery lines')
k['sel']=k['sel'].replace('the US collections page was not retrievable','the US collections page was not retrievable and the Belgian page returned 403 on a second try; a third-party guide (odsjewellers.com) confirms Millenia, Matrix and Dextera')
k=find('David Yurman lines'); k['sel']=k['sel']+' Wikipedia\'s David Yurman article names only the Wedding Collection (2006); no further lines found.'
k=find('Malabar Gold & Diamonds collections'); k['sel']=k['sel']+' Wikipedia\'s Malabar Gold & Diamonds article names no collections.'
k=find('Mejuri lines'); k['sel']=k['sel']+' Wikipedia has no fetchable Mejuri page.'
# Chooda versions
for e in find('Bangle')['x']:
    if e['n']=='Chooda':
        e['s']=W+'Chura_(bangles)'
        e['d']='Set of bangles traditionally worn by Indian brides, usually red and white, once made of ivory with inlay and now often plastic.'
        e['v']=[{'n':n,'mk':'','y':'','d':dd} for n,dd in [('Gujarati chudlo',''),('Hirva chuda','Marathi, peacock-green'),('Nepali chura','red gilded bangles'),('Shakha pola','Bengali and Odia, conch shell and red coral'),('Muthi kharu','Assamese, gold and silver layered'),('Sindhi chura','')]]
# new kinds
def newkind(shn,k): shelf(shn)['k'].append(k)
newkind('In the hair',{'n':'Ferronnière','a':'','d':'Headband that encircles the forehead with a small jewel hanging at the centre; worn in late 15th-century Italy and revived and named in the 19th century.','s':W+'Ferronni%C3%A8re'})
newkind('South Asian jewellery',{'n':'Aranjanam','a':'Araijan kodi · aranjana charadu · molathadu','d':'Slender gold, silver or thread waist ornament given to babies in South India on the 28th day after birth and worn by many adults.','s':W+'Aranjanam'})
newkind('South Asian jewellery',{'n':'Navaratna jewellery','a':'Navratna','d':'Jewellery set with nine gems tied to nine planets: ruby (Sun), diamond (Venus), pearl (Moon), coral (Mars), hessonite (Rahu), blue sapphire (Saturn), cat\'s eye (Ketu), yellow sapphire (Jupiter), emerald (Mercury).','s':'https://exoticindia.com/product/jewelry/navaratna-ring-jyw27'})
newkind('South Asian jewellery',{'n':'Payyannur Pavithra ring','a':'Pavithra mothiram','d':'Gold ring worn for ritual purposes, once made of grass, sanctified at the Subramanya Temple in Payyannur, Kerala, before it is sold.','s':W+'Payyannur_Pavithra_ring'})
newkind('European, American & Oceanic jewellery',{'n':'Hawaiian heirloom jewellery','a':'Hawaiian heirloom bracelet','d':'Engraved bracelets and pendants carrying Hawaiian names or initials in Old English lettering; the first bracelet was made in 1862 by Christian Eckart for the young Lydia Park, later Queen Liliʻuokalani.','s':'https://www.hawaiimagazine.com/?p=139431'})
# regional g
G={'Borla':'Rajasthan','Passa':'Region not stated','Borla matha patti':'Rajasthan','Mundavalya':'Maharashtra','Temple jhumka':'South India (temple style)','Hanging jhumka':'Region not stated','Jhumar':'Region not stated','Hoop jhumka':'Region not stated','Ear-cuff jhumka':'Region not stated',
'Maharashtrian nath':'Maharashtra','Tehri nath':'Garhwal','Kumaoni nath':'Kumaon','Bengali nath':'Bengal','Tanmaniya':'Maharashtra','Lakshmi tali':'Telugu region','Minnu':'Kerala','Kumbha tali':'Tamil Nadu','Kali poath':'Deccan',
'Rani haar':'Mughal India','Satlada':'Deccan','Laxmi haar':'Maharashtra','Oddiyanam':'South India','Arapatta':'South India','Kardhani':'Rajasthan','Maharashtrian kamarband':'Maharashtra',
'Talhakim':'Tuareg','Lalibela cross':'Ethiopia','Axum cross':'Ethiopia','Tizerzai':'Amazigh','Tabzimt':'Kabylie','Crowned Claddagh':'Galway, Ireland','Fenian Claddagh':'Ireland',
'Navajo squash blossom':'Navajo','Naja':'Navajo','Zuni stone-set squash blossom':'Zuni','Pueblo cross necklace':'Pueblo','Hei matau':'Maori, New Zealand'}
n0=0
for dp,s,k in kinds():
    xs=k.get('x') or []
    for e in xs:
        if e.get('g'): continue
        if k.get('xg')=='by house or maker': e['g']=e.get('mk') or 'No maker named'
        elif k.get('xg')=='by people or region': e['g']=G.get(e['n'],'Region not stated')
        elif k.get('xg')=='by historic or modern period': pass
        n0+=1
    # coverage wording
    sel=k.get('sel') or ''
    if xs and 'No whole-space reference exists for this kind' in sel:
        k['sel']="No complete list exists; follows the pages cited on each entry (%d lines named there)."%len(xs)
    elif xs and 'no whole-space list exists for regional jewellery' in sel:
        k['sel']="No complete list exists for regional jewellery; follows the pages cited on each entry (%d types named there)."%len(xs)
# g for kinds whose xg is 'single section' already have g
for dp,s,k in kinds():
    for e in k.get('x') or []:
        if not e.get('g'): print('no g',k['n'],e['n'],k.get('xg'))
json.dump(d,open(R+'work/GAP_A3/A3.tmp','w'),ensure_ascii=False,separators=(',',':'))
os.replace(R+'work/GAP_A3/A3.tmp',R+'out/A3.json')
# brands
bp=R+'out/A3_brands.json'; b=json.load(open(bp))
U={'Fred':{'own':'LVMH','tier':'Global group','d':'Paris house founded in 1936 by Fred Samuel; owned by LVMH since 1995.','s':fw},
'Harry Winston':{'own':'The Swatch Group','tier':'Global group','f':'','s':W+'Harry_Winston'},
'Graff':{'own':'Family-owned (owner not named)','c':'United Kingdom','f':'1960','s':W+'Graff_Diamonds'},
'Chopard':{'own':'Scheufele family'},
'Mikimoto':{'own':'Privately held (owner not named)'},
'Georg Jensen':{'own':'Fiskars Group'},
'Monica Vinader':{'own':'Bridgepoint Development Capital (majority)','f':'2007','s':W+'Monica_Vinader'},
'Thomas Sabo':{'own':'Privately held (owner not named)'},
'Chow Sang Sang':{'own':'Chow Sang Sang Holdings International Limited','f':'1934','s':W+'Chow_Sang_Sang'},
'Tanishq':{'own':'Titan Company','s':W+'Tanishq'},
'Kalyan Jewellers':{'own':'Kalyan Jewellers (listed on BSE and NSE)','s':W+'Kalyan_Jewellers'},
'Malabar Gold & Diamonds':{'own':'M. P. Ahammed','s':W+'Malabar_Gold_%26_Diamonds'},
'Qeelin':{'own':'Kering','s':W+'Qeelin'}}
for x in b['b']:
    if x['n'] in U: x.update(U[x['n']])
have={x['n'] for x in b['b']}
if 'The Swatch Group' not in have: b['b'].append({'n':'The Swatch Group','c':'Switzerland','seg':'Luxury house','d':'Swiss group that bought Harry Winston on 26 March 2013 for $1 billion.','s':W+'Harry_Winston','kf':'watch and jewellery group','own':'The Swatch Group','tier':'Global group'})
if 'Fiskars Group' not in have: b['b'].append({'n':'Fiskars Group','seg':'Luxury house','d':'Group that bought Georg Jensen in December 2023 for EUR 155 million.','s':W+'Georg_Jensen_A/S','kf':'owner of Georg Jensen','own':'Fiskars Group'})
json.dump(b,open(R+'work/GAP_A3/b.tmp','w'),ensure_ascii=False,separators=(',',':')); os.replace(R+'work/GAP_A3/b.tmp',bp)
print('done')
