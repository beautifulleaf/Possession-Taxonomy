import json,os,copy,re
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'A5.json')); br=json.load(open(P+'A5_brands.json'))
kinds={}
for dep in d['depts']:
    for sh in dep['s']:
        for k in sh['k']: kinds[k['n']]=(dep,sh,k)
# sibling attrs per maker
sib={}
for n,(dep,sh,k) in kinds.items():
    for e in k.get('x',[]):
        if e.get('mk') and e['mk'] not in sib and 'own' in e: sib[e['mk']]=e
def add(kind,n,y,mk,d_,s,role=None,v=None,gmk=None):
    k=kinds[kind][2]; x=k.setdefault('x',[])
    if any(e['n'].lower()==n.lower() for e in x): return
    e={'n':n,'d':d_,'mk':mk,'y':y,'s':s,'v':v or []}
    sb=sib.get(mk)
    if sb:
        for f in('cty','own','tier','own_y'):
            if f in sb: e[f]=sb[f]
        e['g']=sb.get('g','')
    else: e['g']=gmk or mk
    if role: e['role']=role
    x.append(e)
W='https://en.wikipedia.org/wiki/'
add('Dive watch','Amfibia','1967','Vostok','Mechanical diver from the Vostok factory in Chistopol, sold in manual and automatic versions.',W+'Amfibia')
add('Dive watch','Khaki Navy BeLOWZERO','2020','Hamilton','Limited edition of 888 pieces inspired by props in the film Tenet.',W+'Hamilton_Watch_Company')
add('Dive watch','Parawater','1959','Citizen','Described as Japan\'s first fully water-resistant wristwatch.',W+'Citizen_Watch')
add('Dive watch','Professional Diver 1300m','1982','Citizen','Professional diving watch.',W+'Citizen_Watch')
add('Dive watch','Aqualand','','Citizen','Diving watch that incorporated an electronic depth sensor.',W+'Citizen_Watch')
add('Flyback chronograph','Longines flyback chronograph','1934','Longines','Longines released the first chronograph with a flyback function.',W+'Longines')
add('Everyday watch','PR 516','1972','Tissot','Tissot sports watch; the Automatic PR 516 GL dates from 1972 and appears on screen in the film Shaft.',W+'Tissot')
add('Jewellery watch','Pearl watch','1987','Tissot','Tissot was among the first to make watches from mother of pearl.',W+'Tissot')
add('Avant-garde watch','Wood watch','1988','Tissot','Tissot watch made of wood, one of the materials the maker lists as a first.',W+'Tissot')
add('Dress watch','Goldfeather','1960','Seiko','Slim dress watch housing Caliber 60, then the thinnest centre-seconds movement in the world.',W+'Seiko')
add('Everyday watch','Marvel','1956','Seiko','Improved model with a larger movement diameter, raising accuracy and productivity.',W+'Seiko')
add('Everyday watch','Gyro Marvel','1959','Seiko','Introduced the Magic Lever self-winding mechanism, which popularised automatic watches.',W+'Seiko')
add('Everyday watch','Seiko Automatic','1956','Seiko','Japan\'s first automatic wristwatch.',W+'Seiko')
add('Electric & early quartz watch','Twin Quartz','1978','Seiko','Used a second crystal to compensate for temperature effects on quartz accuracy.',W+'Seiko')
add('Solar-powered watch','Astron GPS Solar','2012','Seiko','The world\'s first GPS solar watch.',W+'Seiko')
add('Tourbillon watch','Credor Fugaku','2016','Seiko','The first Seiko watch with a tourbillon, priced at 50 million yen.',W+'Seiko')
add('Tourbillon watch','Grand Seiko Kodo','2022','Grand Seiko','Combined a tourbillon and a constant-force mechanism on a single axis.',W+'Seiko')
add('Digital watch','TimeTron','','Seiko','Retro-futuristic digital line with a dot-matrix display, from the late 1990s.',W+'Seiko')
add('Solar-powered watch','Crystron Solar Cell','1976','Citizen','Described by Citizen as the world\'s first analogue quartz watch powered by a solar cell.',W+'Citizen_Watch')
add('Solar-powered watch','Eco-Drive One','2016','Citizen','Light-powered watch with a movement 1 mm thick.',W+'Citizen_Watch')
add('Radio-controlled watch','Eco-Drive Satellite Wave','2011','Citizen','Received time information from navigation satellites.',W+'Citizen_Watch')
add('Dress watch','The Citizen','1995','Citizen','Premium line introduced for the company\'s 65th anniversary.',W+'Citizen_Watch')
add('Everyday watch','Tsuyosa','2021','Citizen','Automatic mechanical line derived from the NH299 series, launched first in Asian markets.',W+'Citizen_Watch')
add('Everyday watch','Attesa','','Citizen','Titanium-focused Citizen line that includes a radio-controlled Eco-Drive chronograph.',W+'Citizen_Watch')
add('Electric & early quartz watch','X8','1966','Citizen','Described as Japan\'s first domestically produced electronic wristwatch.',W+'Citizen_Watch')
add('Electric & early quartz watch','Vantage','','Hamilton','Leftover Hamilton-Ricoh electronic movements re-cased under the Vantage name and sold in the United States.',W+'Hamilton_Watch_Company')
add('Jewellery watch','Kallista','1979','Vacheron Constantin','One of the most expensive wristwatches in the world, set with 118 emerald-cut diamonds.',W+'Vacheron_Constantin')
add('Grande-complication watch','Tour de l\'Île','2005','Vacheron Constantin','Made for the 250th anniversary with 834 parts and 16 complications; seven were made.',W+'Vacheron_Constantin')
add('Grande-complication watch','Les Cabinotiers Solaria Ultra Grand Complication','2025','Vacheron Constantin','Wristwatch with 41 complications, the most complicated wristwatch in Wikipedia\'s list.',W+'Complication_(horology)')
add('Grande-complication watch','Hybris Mechanica Grande Sonnerie','','Jaeger-LeCoultre','Wristwatch with 27 complications on a Jaeger-LeCoultre Calibre 182 movement.',W+'Complication_(horology)')
# Ermeto: new kind
dep,sh,ck=kinds['Coin watch']
pk={'n':'Purse watch','a':'Ermeto','d':'Rectangular watch kept in a case that winds it as it is opened and closed.','s':W+'Movado_Ermeto_watch',
 'nl':'One entry is a purse or case-wound watch model sold under its own name.',
 'x':[{'n':'Ermeto','d':'Rectangular pocket or purse watch made by Movado from 1926 to 1985; opening and closing the two sliding case halves winds it.','mk':'Movado','y':'1926','s':W+'Movado_Ermeto_watch','v':[],'g':'Movado'}],
 'sel':"Follows Wikipedia's Movado Ermeto watch page, the only purse watch in Category:Watch models. Complete: 1 of 1 in that page."}
sh['k'].append(pk); kinds['Purse watch']=(dep,sh,pk)
# Sunrise alarm clock origin
k=kinds['Sunrise alarm clock'][2]
k['x']=[{'n':'Mechanical sunrise','d':'Patented in 1890: the first recorded dawn-simulation device, the idea behind the sunrise alarm clock.','y':'1890','s':W+'Dawn_simulation','role':'origin','v':[]}]
k['nl']='One entry is the origin of the kind; later sunrise alarm clocks are commodity.'
k['sel']="Follows Wikipedia's Dawn simulation article, which dates the first patent to 1890; brand and model lists are left out under the icon rule. Complete: 1 of 1 in that article."
# Seth Thomas railroad
rr=kinds['Railroad-grade pocket watch'][2]
ST='https://mobile.railswest.com/time/seththomas.html'
rows=[('Henry Molineux grade','1880s','Highest grade of the Model 2 and Model 3 lines, adjusted to railroad requirements.'),
('Model 5 Maiden Lane','1895','18-size Model 5 full-plate open-face, the highest grade made, with 17 to 25 jewels.'),
('No. 260','1895','18-size Model 5, 21 jewels, adjusted to six (later five) positions; Seth Thomas\'s most popular railroad watch.'),
('No. 248','1895','18-size Model 5, 21 jewels, adjusted to three positions; discontinued about 1906 and accepted on some railroads into the 1920s.'),
('No. 382','1895','18-size Model 5, 17 jewels, adjusted to five positions.'),
('No. 282','1895','18-size Model 5, 17 jewels, adjusted to three positions; discontinued about 1906.'),
('No. 182','1890s','18-size Model 5, 17 jewels, patent regulator for temperature and isochronism; met some railroad requirements in the 1890s.'),
('Nos. 508, 180, 506 and 179','1896','17-jewel adjusted Model 2 and Model 3 movements with micrometer regulator, listed in the 1896 catalogue.')]
for n,y,dd in rows:
    rr['x'].append({'n':'Seth Thomas '+n,'d':dd,'mk':'Seth Thomas','y':y,'s':ST,'v':[],'g':'Seth Thomas'})
rr['sel']=re.sub(r'The Seth Thomas page was not read; ','',rr['sel'])
rr['sel']=re.sub(r'Covers \d+ of about \d+ lines on the Rails West pages read\.?','',rr['sel']).rstrip()
rr['sel']+=" The Seth Thomas page was read in the gap pass. Complete: %d of %d lines on the Rails West maker pages read."%(len(rr['x']),len(rr['x']))
# owners
OWN={'Chopard':('Scheufele family','Independent','1963','https://en.wikipedia.org/wiki/Chopard'),
'Girard-Perregaux':('Sowind Group','Independent','','https://en.wikipedia.org/wiki/Girard-Perregaux'),
'Doxa':('Jenny family (Walca S.A.)','Independent','1997','https://en.wikipedia.org/wiki/Doxa_SA'),
'Glycine':('Invicta Watch Group','Independent','2016','https://en.wikipedia.org/wiki/Glycine_Watch'),
'Universal Genève':('Breitling SA','Independent','2023','https://en.wikipedia.org/wiki/Universal_Gen%C3%A8ve'),
'Waltham':('Waltham International SA','Independent','2011','https://en.wikipedia.org/wiki/Waltham_Watch_Company'),
'Greubel Forsey':('Greubel Forsey (private; Richemont holds a minority stake from 2006)','Independent','','https://en.wikipedia.org/wiki/Greubel_Forsey'),
'Christopher Ward':('Christopher Ward London Holdings Ltd','Independent','2014','https://en.wikipedia.org/wiki/Christopher_Ward_(watchmaker)'),
'Vostok':('Vostok Watch Factory LTD','Independent','','https://en.wikipedia.org/wiki/Vostok_(watches)'),
'Baltic':('Baltic (independent French brand founded by Étienne Malec)','Craft & indie','','https://timeandtidewatches.com/everything-you-need-to-know-about-french-independent-baltic/'),
'Philippe Dufour':('Philippe Dufour (independent)','Independent','','https://www.ahci.ch/members/philippe-dufour'),
'Sinclair Radionics':('Defunct (National Enterprise Board held 73 % from 1977; broken up 1979)',None,'','https://en.wikipedia.org/wiki/Sinclair_Radionics')}
def setown(o,mk):
    own,tier,oy,s=OWN[mk]; o['own']=own
    if tier: o['tier']=tier
    if oy: o['own_y']=oy
    if o.get('own_s') is None: pass
cnt=0
for n,(dep,sh,k) in kinds.items():
    for e in k.get('x',[]):
        if e.get('mk') in OWN and 'not stated' in e.get('own','not stated'):
            setown(e,e['mk']); cnt+=1
for b in br['b']:
    if b['n'] in OWN and not b.get('own') or (b['n'] in OWN and 'not stated' in b.get('own','')):
        own,tier,oy,s=OWN[b['n']]; b['own']=own
        if tier: b['tier']=tier
        if oy: b['own_y']=oy
print('owners set',cnt)
# coverage lines on wristwatch kinds
WR="No complete list exists; follows Wikipedia's Category:Watch models (38 pages, read in full, with its Casio, Omega, Rolex and Timex subcategories), the Wikipedia pages of the makers named above, Wikidata class Q178794 (246 items, mostly museum objects) and Watchbase for nine makers; Watchbase for other makers is blocked and deferred."
for sh in d['depts'][0]['s']:
    for k in sh['k']:
        if k['n'] in('Watch movement','Design clock'): continue
        if k.get('x'): 
            k['sel']=re.sub(r'\s*(No complete list exists;|Complete:|Covers \d+).*$','',k['sel'],flags=re.S).rstrip()+' '+WR
k=kinds['Watch movement'][2]; k['sel']=re.sub(r'Covers 25 calibres.*$','',k['sel'],flags=re.S).rstrip()+" No complete list exists; follows the calibres named on fetched maker and movement pages and Wikipedia's ETA, List of ETA Movements, Valjoux 7750 and Miyota pages."
k=kinds['Design clock'][2]; k['sel']=re.sub(r'Covers 22 of 22 Braun models.*$','',k['sel'],flags=re.S).rstrip()+" Core77's list of Braun clocks is read in full (22 of 22); no complete list of design clocks exists; follows Core77, Vitra and MoMA records."
json.dump(d,open(P+'A5.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'A5.json.tmp',P+'A5.json')
json.dump(br,open(P+'A5_brands.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'A5_brands.json.tmp',P+'A5_brands.json')
