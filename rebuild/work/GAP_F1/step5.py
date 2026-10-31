import json,re
d=json.load(open('F1.s4a.json'))
K={k['n']:k for dp in d['depts'] for sh in dp['s'] for k in sh['k']}
D={dp['n']:dp for dp in d['depts']}
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
SRC_PULP='https://storytellingdb.com/list-of-pulp-magazines/'
# ---- pulp
k=K['Pulp magazine']
for e in k['x']: e['g']='Genre families'
names={norm(e['n']) for e in k['x']}
n=0
for line in open('pulp_rows.txt',encoding='utf8'):
    t,pub,dt=line.rstrip('\n').split('|')
    y=dt[:4] if re.match(r'\d{4}',dt) else ''
    g=(y[:3]+'0s') if y else 'Start year not given'
    if norm(t) in names: continue
    names.add(norm(t))
    when=f"first issued {dt}" if dt else "start date not given"
    k['x'].append({"n":t,"a":"","d":f"Pulp magazine from {pub}, {when}.","mk":pub,"y":y,"g":g,"s":SRC_PULP}); n+=1
# remove version rows duplicating titles
ents={norm(e['n']) for e in k['x']}
for e in k['x']:
    if 'v' in e: e['v']=[v for v in e['v'] if norm(v['n']) not in ents]
k['xg']='by decade of first issue'
k['nl']="One entry is a pulp magazine title, as listed by StorytellingDB; the genre families are types, not titles."
k['sel']="Every title of StorytellingDB's List of Pulp Magazines, a third-party list, read in all windows to row 882 (Zoom). Complete: "+str(n)+" titles added, 882 of 882 rows (same-name titles from different years and publishers kept apart by year). No Wikipedia list exists. The list is mostly American; British and other pulps are thin."
print('pulp added',n,len(k['x']))
# ---- atlases
SRC_AT='https://en.wikipedia.org/wiki/List_of_atlases'
at=[("Douce Atlas","","","15th century"),("Theatrum Orbis Terrarum","Ortelius","1570","16th century"),("Mercator's Atlas","Gerardus Mercator","1578","16th century"),
("Atlas Novus","Blaeu","1635","17th century"),("Dell'Arcano del Mare","","1645","17th century"),("Cartes générales de toutes les parties du monde","","1658","17th century"),("Klencke Atlas","","1660","17th century"),("Atlas Maior","Blaeu","1662","17th century"),("Atlante Veneto","Vincenzo Coronelli","1691","17th century"),
("Britannia Depicta","","1720","18th century"),("Atlas Nouveau","","1742","18th century"),("Cary's New and Correct English Atlas","John Cary","1787","18th century"),
("Andrees Allgemeiner Handatlas","","1881","19th century"),("Atlas do Visconde de Santarem","","1841","19th century"),("Bosatlas","","1877","19th century"),("Cedid Atlas","","1803","19th century"),("Rand McNally Atlas","Rand McNally","1881","19th century"),("Stielers Handatlas","","1817","19th century"),
("Atlante Internazionale del Touring Club Italiano","Touring Club Italiano","1927","20th century"),("Atlas Mira","","1937","20th century"),("Geographers' A–Z Street Atlas","Geographers' A–Z Map Company","1938","20th century"),("Gran Atlas Aguilar","","1969","20th century"),("Historical Atlas of China (1980)","","1980","20th century"),("The Historical Atlas of China","","1982","20th century"),("Pergamon World Atlas","","1962","20th century"),("Dorling Kindersley Atlas of the World","Dorling Kindersley","1994","20th century")]
cntry={"Douce Atlas":"nautical atlas","Theatrum Orbis Terrarum":"Flanders","Mercator's Atlas":"","Atlas Novus":"Netherlands","Dell'Arcano del Mare":"England and Italy","Cartes générales de toutes les parties du monde":"France","Atlas Maior":"Netherlands","Atlante Veneto":"Venice","Britannia Depicta":"London","Atlas Nouveau":"Amsterdam","Cary's New and Correct English Atlas":"London","Andrees Allgemeiner Handatlas":"Germany","Atlas do Visconde de Santarem":"Paris","Bosatlas":"Netherlands","Cedid Atlas":"Istanbul","Rand McNally Atlas":"United States","Stielers Handatlas":"Germany","Atlante Internazionale del Touring Club Italiano":"Italy","Atlas Mira":"Russia","Geographers' A–Z Street Atlas":"United Kingdom","Historical Atlas of China (1980)":"Taiwan","The Historical Atlas of China":"China"}
ka=K['Antique atlas']; kn=K['Atlas']
for kind in (ka,kn):
    for e in kind['x']: e.setdefault('g', 'Earlier entries')
adds=0
for nm,mk,y,cent in at:
    kind=kn if cent=='20th century' else ka
    allnames={norm(e['n']) for e in ka['x']+kn['x']}
    if norm(nm) in allnames or (nm=="Theatrum Orbis Terrarum") or (nm=="Atlas Maior") : continue
    where=cntry.get(nm,'')
    dsc=f"Atlas listed by Wikipedia's List of atlases under the {cent}"+(f", from {where}" if where else "")+(f", first published {y}" if y else "")+"."
    kind['x'].append({"n":nm,"a":"","d":dsc,"mk":mk,"y":y,"g":cent,"s":SRC_AT}); adds+=1
for kind in (ka,kn):
    for e in kind['x']:
        if e.get('g')=='Earlier entries': e['g']='Earlier entries (centuries not tagged)'
    kind['xg']='by century'
    kind['sel']=re.sub(r'\s*Complete: .*$','',kind.get('sel',''))
ka['sel']+=" Covers 15th to 19th-century atlases of Wikipedia's List of atlases: all 18 printed atlases listed for those centuries are included, Theatrum Orbis Terrarum and Atlas Maior being already entries. Piri Reis Map (a single map) is left out."
kn['sel']+=" Covers the 20th-century atlases of Wikipedia's List of atlases: all 10 are included; the 8 digital map services (Google Maps, Bing Maps and others) are not printed atlases and are left out."
print('atlas adds',adds)
# ---- globes
SRC_GL='https://omniterrum.com/reference/globe-makers'
def region(place):
    p=place
    for key,reg in [('Nuremberg','Germany'),('Berlin','Germany'),('Leipzig','Germany'),('Stuttgart','Germany'),('Gotha','Germany'),('Munich','Germany'),('Heidelberg','Germany'),('Tübingen','Germany'),('London','Britain'),('Edinburgh','Britain'),('England','Britain'),('Paris','France'),('Brussels','Belgium'),('Vienna','Austria'),('Prague','Czech lands'),('Stockholm','Sweden'),('Uppsala','Sweden'),('Venice','Italy'),('Budapest','Hungary'),('Hungary','Hungary'),('Moscow','Russia'),('Switzerland','Switzerland'),('Saint-Dié','France')]:
        if key in p: return reg
    return 'United States'
ant=K['Antique globe']; des=K['Desktop globe']
for e in ant['x']+des['x']: e.setdefault('g','Earlier entries (region not tagged)')
have={norm(e['n']) for e in ant['x']+des['x']}
ga=gd=0
for line in open('globes.txt',encoding='utf8'):
    nm,pl,dt=line.rstrip('\n').split('|')
    if norm(nm) in have: continue
    m=re.search(r'(\d{4})',dt); y0=int(m.group(1)) if m else None
    modern=('present' in dt) or (y0 and y0>=1880 and 'century' not in dt) or ('20th' in dt) or ('world wars' in dt) or ('1860s-1920s' in dt)
    kind=des if modern else ant
    dsc=f"Globe maker of {pl}"+(f", active {dt}" if dt else "")+"."
    kind['x'].append({"n":nm,"a":"","d":dsc,"mk":nm,"y":(str(y0) if y0 else ''),"g":region(pl),"s":SRC_GL})
    if modern: gd+=1
    else: ga+=1
for kind in (ant,des):
    kind['xg']='by country of the maker'
    kind['sel']=re.sub(r'\s*Complete: .*$','',kind.get('sel',''))
ant['sel']+=f" Covers {ga} makers before about 1880 from Omniterrum's list of globe makers (all but Archimedes of Syracuse, who left no surviving globe)."
des['sel']+=f" Covers {gd} makers active after about 1880 from Omniterrum's list of globe makers; with the antique globe kind this is 91 of 91 rows, less Archimedes and the Replogle row already an entry."
print('globes',ga,gd)
# Oxford World's Classics
K['Paperback book']['x'].append({"n":"Oxford World's Classics","a":"World's Classics","d":"Oxford University Press series of classics begun in 1901 under Grant Richards, taken over by Oxford and relaunched in paperback in March 1980.","mk":"Oxford University Press","y":"1901","s":"https://en.wikipedia.org/wiki/Oxford_World%27s_Classics"})
# market panel
ms=D['Records & audio']['ms']
ms+= [
 {"mkt":"Global recorded music, physical formats","who":"All physical formats","share":"16.4 %","yr":2024,"s":"https://musicbusinessworldwide.com/11-quick-and-important-takeaways-from-ifpis-global-music-report-2025","note":"Share of total global revenues, as Music Business Worldwide reports IFPI's Global Music Report 2025; physical trade revenues fell 3.1 % on the year."},
 {"mkt":"Global recorded music, vinyl","who":"Vinyl","share":"up 4.6 %","yr":2024,"s":"https://www.ifpi.org/ifpi-amidst-highly-competitive-market-global-recorded-music-revenues-grew-4-8-in-2024/","note":"IFPI release of 19 March 2025: 18th consecutive year of growth; total trade revenues US$29.6 billion; Asia 45.1 % of global physical revenues. IFPI gives no CD or vinyl value in this release."},
 {"mkt":"UK recorded music, vinyl LP","who":"Vinyl LP","share":"5.9 million units","yr":2023,"s":"https://www.bpi.co.uk/news/12886526","note":"BPI provisional figure of 28 December 2023, up 11.7 %; 16th consecutive year of growth."},
 {"mkt":"UK recorded music, CD","who":"CD","share":"nearly 11 million units","yr":2023,"s":"https://www.bpi.co.uk/news/12886526","note":"BPI provisional figure of 28 December 2023; the smallest annual decline in nearly a decade."},
 {"mkt":"UK recorded music, cassette","who":"Cassette","share":"195,000 units","yr":2022,"s":"https://www.bpi.co.uk/news/12886576","note":"BPI release of 19 April 2023: up 5.2 %, near a two-decade high; 185,000 units in 2021."}]
for k in K.values():
    if k['n']=='Records & audio': pass
json.dump(d,open('F1.s5.json','w'),ensure_ascii=False,indent=1)
