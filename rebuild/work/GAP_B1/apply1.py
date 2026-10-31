import json,os,re
P='rebuild/out/B1.json'; PB='rebuild/out/B1_brands.json'
d=json.load(open(P)); bd=json.load(open(PB))
URL='https://ikeamuseum.com/en/explore/product-stories/'
# (kind, name, type, year)
R=[
('Armchair','Mk','armchair',1950),('Armchair','Bohem','armchair',1955),('Armchair','Esbjerg','armchair',1956),('Armchair','Ägget','armchair',1956),
('Armchair','Cavelli','armchair',1958),('Armchair','Polo','armchair',1966),('Armchair','Katinka and Karusell','armchair, sofa and coffee table',1967),
('Armchair','Amiral','armchair',1969),('Armchair','Diana','armchair',1971),('Armchair','Kuling','armchair, sofa and coffee table',1971),
('Armchair','Skopa','armchair',1973),('Armchair','IKEA PS Lömsk','swivel armchair',2003),('Armchair','IKEA PS 2017 armchair','armchair',2017),('Armchair','Stockholm armchair','armchair',2017),
('Upholstered lounge chair','Kröken','lounge chair',1968),('Upholstered lounge chair','Trofé','lounge chair and footstool',1968),
('Upholstered lounge chair','Impala','easy chair',1971),('Upholstered lounge chair','Tajt','easy chair',1972),('Upholstered lounge chair','Järpen','easy chair',1982),('Upholstered lounge chair','IKEA a.i.r Rolig','easy chair',1999),
('Sofa','Praag','sofa',1956),('Sofa','Gråbo','sofa',1963),('Sofa','Moment sofa','sofa',1984),('Sofa','Karlanda','sofa',2000),('Sofa','Björksnäs','sofa with glass door cabinet',2015),('Sofa','Havsten','outdoor sofa',2017),('Sofa','Brusen','outdoor sofa',2019),
('Sofa bed','IKEA PS 1999 sofa bed','sofa bed',1999),
('Coffee table','Lövet','coffee table',1955),('Coffee table','Pavo','coffee table',1968),('Coffee table','Bogen','coffee table',1985),('Coffee table','Njurunda','coffee table',1993),
('Dining table','Peggy','table',1956),('Dining table','Moa','table',1959),('Dining table','Petita I','table',1959),('Dining table','Stabil','table',1972),('Dining table','Moment dining table','dining table',1986),('Dining table','IKEA PS Eden','dining table',2006),('Dining table','Norråker','bench table and stool',2015),
('Side table','Strajk','side table',1974),('Side table','Hatten','side table',1994),('Side table','Nordli','bedside table',2015),('Side table','Burvik','side table',2018),
('Dining chair','Grill','chair',1957),('Dining chair','Ögla','chair',1961),('Dining chair','Lena','chair',1968),('Dining chair','Snille','chair',1972),('Dining chair','Albert','chair',1984),('Dining chair','Emil','chair',1993),('Dining chair','Hallunda','chair',1993),('Dining chair','Mammut','children\'s chair',1993),('Dining chair','Olle','chair',2003),('Dining chair','IKEA PS Ellan','chair',2006),('Dining chair','Stockholm chair','chair',2013),('Dining chair','Omtänksam chair','chair',2018),
('Folding chair','Ted','folding chair',1978),
('Office chair','Jules','desk chair',1998),('Office chair','Örfjäll','swivel chair',2016),
('Rocking chair','IKEA PS Gullholmen','rocking chair',2002),
('High chair','Dino','highchair',1970),('High chair','Antilop','highchair',1991),
('Stool','Patrull','children\'s stool',1998),('Stool','Bursjö','stool with storage',1999),('Stool','Bekväm','step stool',2000),('Stool','Mästerby','step stool',2014),('Stool','Sinnerlig','stool',2015),
('Rolling cart','Tea','trolley',1958),
('Bed frame','Adam','bed',1971),('Bed frame','Kromvik','bed',1981),('Bed frame','Björkvalla','bedroom series',1992),('Bed frame','Gjöra','bed',2016),
('Desk','Lisabo','desk',2015),
('Bookcase','Hansa','bookcase',1956),('Bookcase','Regal','bookcase',1957),('Bookcase','Guide','bookshelf',1984),('Bookcase','Robin','multimedia shelf',1998),
('Chest of drawers','Tore','drawer unit',1959),('Chest of drawers','Vajer','chest of drawers',1995),('Chest of drawers','Hemnes','chest of drawers',2000),('Chest of drawers','Malm chest of drawers','chest of drawers',2002),
('Storage cabinet','MTP','cabinet',1962),('Storage cabinet','Stockholm glass door cabinet','glass door cabinet',1985),('Storage cabinet','IKEA PS 1999 cabinet','cabinet',1999),('Storage cabinet','Stockholm cabinet','cabinet',2006),
]
kinds={}
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']: kinds[k['n']]=k
have=set()
for k in kinds.values():
    for e in k.get('x',[]):
        have.add(e['n'].lower())
        for a in (e.get('a') or '').split('·'): have.add(a.strip().lower())
added={}
for kn,n,t,y in R:
    k=kinds[kn]
    if n.lower() in have: print('dup',n); continue
    have.add(n.lower())
    e={"n":n,"a":"","d":f"IKEA {t} of {y}, told in the IKEA Museum's product stories.","mk":"IKEA","y":str(y),"s":URL,"v":[],"own":"Inter IKEA Systems B.V.","tier":"Own label","cty":"Sweden","g":f"{y//10*10}s"}
    k.setdefault('x',[]).append(e); added[kn]=added.get(kn,0)+1
def gk(e):
    g=e.get('g') or 'Undated'
    return (1,g) if g=='Undated' else (0,g)
for kn in added:
    k=kinds[kn]; k['x']=sorted(k['x'],key=gk) if all(re.match(r'^(\d{4}s|Undated)$',e.get('g','')) for e in k['x']) else k['x']
# Klippan: fix undated
for e in kinds['Sofa']['x']:
    if e['n']=='Klippan': e['y']='1979'; e['g']='1970s'; e['s']=URL; e['d']='IKEA sofa of 1979, told in the IKEA Museum product stories; sold by the tens of millions.'
# Ownership
for e in kinds['Mattress']['x']:
    if e['n']=='Serta': e.update(own='Serta Simmons Bedding, LLC',tier='Independent',own_y='2012',s='https://en.wikipedia.org/wiki/Serta_Simmons_Bedding',d='US mattress brand; with Simmons it has shared a parent since Advent International\'s 2012 buyout, and the group went through Chapter 11 in 2023.',g='Independent')
    if e['n']=='Simmons': e.update(own='Serta Simmons Bedding, LLC',tier='Independent',own_y='2012',s='https://en.wikipedia.org/wiki/Serta_Simmons_Bedding',d='US mattress maker founded in Kenosha in 1870; Advent International took a majority in October 2012 and it shares a parent with Serta.',g='Independent')
    if e['n']=='Leesa': e.update(own='3Z Brands',tier='Independent',own_y='2023',s='https://sleepopolis.com/news/leesa-sleep-3z-brands-latest-acquisition/',d='US online mattress brand bought by 3Z Brands in March 2023; Leesa Reserve was a Consumer Reports side-sleeper pick.')
    if e['n']=='Nectar': e.update(own='Resident Home',tier='Independent',own_y='2024',d='Online memory-foam brand; its owner Resident Home was bought by Ashley in March 2024. Ultra Hybrid was a Consumer Reports side-sleeper pick.')
    if e['n']=='Nectar': e['s']='https://www.streetinsider.com/PRNewswire/Ashley+and+Resident+Announce+Acquisition/22885953.html'
for e in kinds['Mattress']['x']:
    if e['n']=='Nectar': e['own']='Ashley (via Resident Home)'
    if e['n'] in('Serta','Simmons','Leesa','Nectar'):
        pass
bs={x['n']:x for x in bd['b']}
bs['Simmons']['kf']='mattresses'
bs['Serta'].update(own='Serta Simmons Bedding, LLC',tier='Independent')
bs['Simmons'].update(own='Serta Simmons Bedding, LLC',tier='Independent')
bs['Leesa'].update(own='3Z Brands',tier='Independent')
bs['Nectar'].update(own='Ashley (via Resident Home)',tier='Independent')
for nm,c,note,s in [('Serta Simmons Bedding, LLC','United States','Doraville, Georgia parent of Serta and Simmons; Chapter 11 January to June 2023.','https://en.wikipedia.org/wiki/Serta_Simmons_Bedding'),
  ('3Z Brands','United States','Sleep-brand group (Brooklyn Bedding, Helix, Bear, Nolah, Birch, Leesa).','https://sleepopolis.com/news/leesa-sleep-3z-brands-latest-acquisition/'),
  ('Resident Home','United States','Online mattress group (Nectar, DreamCloud, Awara, Siena), bought by Ashley in March 2024.','https://www.streetinsider.com/PRNewswire/Ashley+and+Resident+Announce+Acquisition/22885953.html')]:
    if nm not in bs: bd['b'].append({'n':nm,'c':c,'seg':'Mainstream','d':note,'s':s,'kf':'mattresses'})
for p,o in ((P,d),(PB,bd)):
    json.dump(o,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
print(added,sum(added.values()))
