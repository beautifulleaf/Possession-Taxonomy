import json,re,sys,copy,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import data_air as A
ROOT='/home/user/Possession-Taxonomy/'
G=json.load(open(ROOT+'rebuild/out/G1.json'))
W=A.W; WIKI="https://en.wikipedia.org/wiki/"
ad=copy.deepcopy(next(x for x in G['depts'] if x['n']=='Aircraft'))
def kind(n):
    for s in ad['s']:
        for k in s['k']:
            if k['n']==n: return k
    raise KeyError(n)
def yr(v):
    m=re.search(r'\d{4}',str(v or '')); return int(m.group()) if m else None
def names(k): return {e['n'].lower() for e in k.get('x',[])}
def addx(k,e):
    k.setdefault('x',[])
    if e['n'].lower() in names(k): return False
    k['x'].append(e); return True
def addv(e,n,y='',d='',mk=''):
    e.setdefault('v',[])
    if n.lower() in {v['n'].lower() for v in e['v']}: return
    e['v'].append({'n':n,'mk':mk,'y':y,'d':d})
KM={'SEP':'Single-engine piston airplane','MEP':'Multi-engine piston airplane','TP':'Turboprop airplane','JET':'Jet','WAR':'Warbird','HB':'Homebuilt aircraft','MG':'Motor-glider','HELI':'Helicopter','LSA':'Light-sport and ultralight airplane'}
PAGES={'Cirrus':WIKI+'Cirrus_Aircraft','Mooney':WIKI+'Mooney_International_Corporation','Robinson':WIKI+'Robinson_Helicopter_Company'}
MKN={'Grob':'Grob Aircraft','Diamond':'Diamond Aircraft','Pilatus':'Pilatus','Luscombe':'Luscombe Aircraft','Maule':'Maule Air','Rutan':'Rutan Aircraft Factory','Robinson':'Robinson Helicopter'}
added={}
for l in A.RAW.strip().splitlines():
    p=l.split('|')
    kc,n,y,mk,src=p[:5]
    if 'additional record' in n: continue
    n=n.replace('Cessna L-19/O-2 Skymaster','Cessna O-2 Skymaster')
    k=kind(KM[kc])
    s=PAGES[src[5:]] if src.startswith('PAGE:') else A.W+src
    e={'n':n,'a':'','mk':MKN.get(mk,mk),'y':y,'s':s,'v':[]}
    if y: e['d']='First flight %s.'%y
    if addx(k,e): added[kc]=added.get(kc,0)+1
# existing entries: versions
def ent(kn,name): return next(e for e in kind(kn)['x'] if e['n']==name)
cit=ent('Jet','Cessna Citation')
for n,y,q in A.CIT_VERS: addv(cit,n,y,'first flight %s (Wikidata)'%y if y else 'Wikidata item '+q,mk='Cessna')
ka=ent('Turboprop airplane','Beechcraft King Air')
for n,y,q in A.KINGAIR_V: addv(ka,n,y,'Wikidata item '+q,mk='Beechcraft')
bz=ent('Single-engine piston airplane','Beechcraft Bonanza')
for n,y,q in A.BON_V: addv(bz,n,y,'Wikidata item '+q,mk='Beechcraft')
br=ent('Multi-engine piston airplane','Beechcraft Baron')
for n,y,q in A.BARON_V: addv(br,n,y,'Wikidata item '+q,mk='Beechcraft')
j3=ent('Single-engine piston airplane','Piper J-3 Cub'); j3['v']=[v for v in j3['v'] if v['n']!='PA-18 Super Cub']
mo=ent('Single-engine piston airplane','Mooney M20'); mo['s']=PAGES['Mooney']
for n,y,d in A.MOONEY_M20: addv(mo,n,y,d,mk='Mooney')
import data_air2 as A2
def kentry(kn,name,y,mk,src,d,vs):
    k=kind(kn)
    e={'n':name,'a':'','mk':mk,'y':y,'s':src,'v':[]}
    if d: e['d']=d
    for n,yy,dd in vs: addv(e,n,yy,dd,mk=mk)
    return addx(k,e)
for kn,name,y,mk,src,d,vs in A2.NEW: kentry(kn,name,y,mk,src,d,vs)
for kn,en,vs in A2.VERS_ADD:
    e=ent(kn,en)
    for n,yy,dd in vs: addv(e,n,yy,dd,mk=e.get('mk',''))
for n,y,d in A2.SLINGSBY: addx(kind('Glider'),{'n':n,'a':'','mk':'Slingsby Aviation','y':y,'s':WIKI+'Slingsby_Aviation','v':[],**({'d':d[0].upper()+d[1:]+'.'} if d else {})})
for n,y,d in A2.SLINGSBY_AC: addx(kind('Single-engine piston airplane'),{'n':n,'a':'','mk':'Slingsby Aviation','y':y,'s':WIKI+'Slingsby_Aviation','v':[],**({'d':d[0].upper()+d[1:]+'.'} if d else {})})
# gliders
GL=kind('Glider'); MG=kind('Motor-glider')
SC=WIKI+'Alexander_Schleicher_GmbH_%26_Co'; SH=WIKI+'Schempp-Hirth'
for l in A.SCHL.strip().splitlines():
    n,c=l.split('|'); addx(GL,{'n':n,'a':'','mk':'Alexander Schleicher','y':'','s':SC,'v':[],'d':c[0].upper()+c[1:]+'.'})
for l in A.SCHL_MG.strip().splitlines():
    n,c=l.split('|'); addx(MG,{'n':n,'a':'','mk':'Alexander Schleicher','y':'','s':SC,'v':[],'d':c[0].upper()+c[1:]+'.'})
for l in A.SCHH.strip().splitlines():
    n,y,c=l.split('|'); e={'n':n,'a':'','mk':'Schempp-Hirth','y':y,'s':SH,'v':[]}
    if c: e['d']=c[0].upper()+c[1:]+'.'
    addx(GL,e)
for en,vs in A.SH_VERS.items():
    e=ent('Glider',en)
    for n,y,q in vs: addv(e,n,y,'',mk='Schempp-Hirth')
# existing motor-glider m ASK 21 Mi etc. dropped; keep entries
# existing dropped m
dropped=[]
for s in ad['s']:
    for k in s['k']:
        for m in k.pop('m',[]) or []: dropped.append((k['n'],m))
# helicopters: R66 handled in RAW
# drones -> move to D4
move={'to':'D4','dept':'Digital cameras','kind':{'n':'Camera drone','a':'drone','d':'Camera-carrying drone.','s':WIKI+'DJI_Mavic','x':[{'n':'DJI Mavic','a':'Mavic','mk':'DJI','y':'2016','s':WIKI+'DJI_Mavic','d':'Folding camera-drone line from DJI, first released 2016 as the Mavic Pro, now at its fourth generation.','v':[{'n':n,'mk':'DJI','y':y,'d':d} for n,y,d in A.MAVIC],'g':'DJI','role':'landmark'}],'nl':'One entry is a drone line; generations and variants are versions.','sel':'Follows the Wikipedia DJI Mavic page; covers the Mavic line only, other makers belong to the D4 camera-drone list.'}}
# finalize x kinds
EXP={'Single-engine piston airplane':'One entry is a single-engine piston model line; model-year letters and marks are versions.','Multi-engine piston airplane':'One entry is a twin piston model line; marks are versions.','Turboprop airplane':'One entry is a turboprop model line; marks are versions.','Jet':'One entry is a light or business jet model line; marks are versions.','Light-sport and ultralight airplane':'One entry is a light-sport or ultralight model line.','Homebuilt aircraft':'One entry is a homebuilt design offered to builders.','Aerobatic airplane':'One entry is an aerobatic model line.','Floatplane':'One entry is a floatplane or amphibian model line.','Warbird':'One entry is a military-heritage aircraft type in private hands.','Glider':'One entry is a glider model; variants and wingspans are versions.','Motor-glider':'One entry is a motor-glider model; engine and launch variants are versions.','Hot-air balloon':'One entry is a balloon maker\'s series.','Gas balloon':'One entry is a gas balloon type.','Airship':'One entry is an airship type.','Helicopter':'One entry is a helicopter model line; marks are versions.','Gyroplane':'One entry is a gyroplane model line.','Powered parachute':'One entry is a powered-parachute model.','Paramotor':'One entry is a paramotor line.','Weight-shift trike':'One entry is a trike model line.'}
SEL=('Follows Wikidata\'s aircraft family and aircraft model items (Q15056993, Q15056995) for the manufacturers named (Beechcraft, Cessna, Piper, Diamond, Pilatus, Schempp-Hirth, Tecnam, Robinson, Aeronca, Lancair, Luscombe, Maule, Pipistrel, Grob, Rutan; first flights from P606), the Wikipedia pages of Cirrus, Mooney, Robinson, Alexander Schleicher and Schempp-Hirth, and the earlier hand-built lines. '
 'Covers the models of those makers that have three or more Wikipedia articles (military-only and airline types left out); makers not queried (for example Bell, Aviat, Extra, Van\'s, Slingsby, Cameron, AutoGyro) keep their earlier entries only.')
def sortk(k):
    for e in k.get('x',[]):
        e['g']=e.get('mk') or 'Maker not stated'
        e.setdefault('v',[])
    k['x'].sort(key=lambda e:(e['g'].lower(),yr(e.get('y')) or 9999,e['n'].lower()))
for s in ad['s']:
    for k in s['k']:
        if k.get('x'):
            k['nl']=EXP.get(k['n'],'One entry is a model line.')
            k['sel']=SEL
            k['xg']='Entries are grouped by maker, then by first-flight year.'
            sortk(k)
ad['note']='Private and sport aircraft by type, with model lines as entries grouped by maker; airliners and military fleets out except privately owned warbirds. Drones belong to D4.'
ad['ms']=[
 {'mkt':'Light aircraft production','who':'Cessna','share':'more than 44,000 Cessna 172s built','yr':2026,'s':'https://en.wikipedia.org/wiki/Cessna_172','note':'carried over from the earlier entry; the 172 is the most-produced aircraft'},
 {'mkt':'Light aircraft production','who':'Cirrus Aircraft','share':'8,246+ SR22/22T and 1,932+ SR20 built','yr':2026,'s':PAGES['Cirrus'],'note':'Cirrus Wikipedia page; owned by China Aviation Industry General Aircraft (AVIC) since 2011'},
 {'mkt':'Light aircraft production','who':'Mooney','share':'11,000+ M20 built','yr':2026,'s':PAGES['Mooney'],'note':'owned by US Financial, LLC since 1 September 2020; Meijing Group ran it 2013 to 2020'},
 {'mkt':'Light aircraft production','who':'Piper Aircraft','share':'about 144,000 aircraft, 160 certified models, 1927 to 2009','yr':2009,'s':WIKI+'List_of_Piper_aircraft','note':'company-wide total on the Wikipedia Piper aircraft list'},
 {'mkt':'Helicopters','who':'Robinson Helicopter Company','share':'private company; models R22, R44, R66','yr':2026,'s':PAGES['Robinson'],'note':'founded 1973 by Frank Robinson; no owner named on the page'}]
ad['msum']='The light-aircraft market is shared by a few American makers (Cessna, Piper, Cirrus, Mooney, Beechcraft) with Chinese state ownership of Cirrus the main change; production totals are the only figures found on fetched pages.'
json.dump({'dept':ad,'dropped':dropped,'move':move,'added':added},open('air_out.json','w'))
print('air ok',added,len(dropped))
