import json,re,sys,copy,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import data_boats as B, data_air as A
ROOT='/home/user/Possession-Taxonomy/'
G=json.load(open(ROOT+'rebuild/out/G1.json'))
W="https://www.wikidata.org/wiki/"
WIKI="https://en.wikipedia.org/wiki/"
def dept(n): return copy.deepcopy(next(x for x in G['depts'] if x['n']==n))
def kind(dp,n):
    for s in dp['s']:
        for k in s['k']:
            if k['n']==n: return k
    raise KeyError(n)
def shelf(dp,n): return next(s for s in dp['s'] if s['n']==n)
def yr(v):
    m=re.search(r'\d{4}',str(v or '')); return int(m.group()) if m else None
def era(y):
    y=yr(y)
    if y is None: return 'Year not stated'
    return 'Before 1950' if y<1950 else '1950–1969' if y<1970 else '1970–1989' if y<1990 else '1990 onward'
ERA_ORDER=['Before 1950','1950–1969','1970–1989','1990 onward','Year not stated']
def names(k): return {e['n'].lower() for e in k.get('x',[])}
def addx(k,e):
    k.setdefault('x',[])
    if e['n'].lower() in names(k): return False
    k['x'].append(e); return True
def addv(e,n,y='',d='',mk=''):
    e.setdefault('v',[])
    if n.lower() in {v['n'].lower() for v in e['v']}: return
    e['v'].append({'n':n,'mk':mk,'y':y,'d':d})
def mkkind(n,a,d,s,tt):
    return {'n':n,'a':a,'d':d,'s':s,'x':[],'tt':tt}
report={}

############ BOATS
bo=dept('Boats')
SAIL=shelf(bo,'Sailing boats')
WDC=W+'Q106179098'
# new kinds
def insert_after(sh,after,k):
    i=[x['n'] for x in sh['k']].index(after); sh['k'].insert(i+1,k)
insert_after(SAIL,'Sailing dinghy',mkkind('Racing skiff and foiler','high-performance skiff','Light dinghy with wings or trapezes, or foils, built for speed.',WDC,[['Crew',['Single-handed','Two-person']],['Hull',['Skiff','Foiling']]]))
insert_after(SAIL,'Beach catamaran',mkkind('Racing multihull','offshore multihull · foiling catamaran','Large racing catamaran or trimaran built for a class or circuit rather than for cruising.',WDC,[['Hulls',['Catamaran','Trimaran']],['Foils',['Foiling','Non-foiling']]]))
insert_after(SAIL,'Racer-cruiser',mkkind('Rating-rule class','metre class · International Rule','Keelboat built to a rating rule such as the International Rule, from the 2.4 Metre to the 12 Metre and J-class.',WDC,[['Rule',['International Rule','Other rating rule']],['Build',['Wood','GRP']]]))
insert_after(SAIL,'Rating-rule class',mkkind('Offshore racing class','IMOCA · Class40 · Mini','Single-design or box-rule yachts raced short-handed offshore.',WDC,[['Class',['Box rule','One design']],['Crew',['Single-handed','Double-handed']]]))
for kk in SAIL['k']:
    if kk['n']=='Ice boat': kk['d']=kk['d'] or 'Boat on runners driven by sail over ice.'
kcode={'D':'Sailing dinghy','S':'Racing skiff and foiler','C':'Beach catamaran','K':'Open keelboat','R':'Racer-cruiser','Y':'Cruising monohull','M':'Rating-rule class','O':'Offshore racing class','I':'Ice boat'}
RACECAT={'Extreme 40','GC32','F50','MOD 70','Diam 24','Flying Phantom'}
CRUISECAT={'Corsair 24 Mark II','Corsair Cruze 970','Farrier F-22','Farrier F-27','F-31 Sport Cruiser'}
EXCL_NAMES={'First Class 8','Hallberg-Rassy 24','Fantasia 27'}
rows=[]
seen=set()
import glob
AUTO={}
def parse_auto(f):
    out=[]
    for l in open(f):
        p=l.rstrip('\n').split('|')
        if len(p)<5: continue
        q,n,y,d,c=p[:5]; code=p[5] if len(p)>5 and p[5] else 'Y'
        out.append(dict(q=q,n=n,y=y,d=d,c=c,code=code,b=''))
    return out
for f in ('sail1.tsv','sail2.tsv','sail3.tsv'):
    for l in open(f):
        p=l.rstrip('\n').split('|')
        ci=next(i for i in range(2,len(p)) if re.fullmatch(r'[DSCKRYMOI]',p[i]))
        mid=(p[2:ci]+['','',''])[:3]
        q,n=p[0],p[1]; y,d,c=mid; code=p[ci]; bld=p[ci+1] if len(p)>ci+1 else ''
        if q in seen: continue
        seen.add(q)
        if n.startswith('Beneteau') or bld=='Beneteau' or n in EXCL_NAMES: continue
        rows.append(dict(q=q,n=n,y=y,d=d,c=c,code=code,b=bld))
auto=[]
for f in sorted(glob.glob('sail[4-9].tsv')+glob.glob('sail[1-9][0-9].tsv')):
    auto+=parse_auto(f)
from collections import Counter
tok=lambda n: re.match(r"^([A-Za-z&' ]+?)[ -]?\d",n).group(1).strip() if re.match(r"^([A-Za-z&' ]+?)[ -]?\d",n) else None
cnt=Counter(tok(r['n']) for r in auto if r['code'] in 'YR' and tok(r['n']))
DISPB={'C&C':'C&C Yachts','Cal':'Cal Yachts','CS':'CS Yachts','Bayfield':'Bayfield Yachts','Aloha':'Aloha Yachts','Bristol':'Bristol Yachts','Hunter':'Hunter Marine','Catalina':'Catalina Yachts','Columbia':'Columbia Yachts','Mirage':'Mirage Yachts','Pearson':'Pearson Yachts','Swan':'Nautor Swan','Albin':'Albin Marine'}
for r in auto:
    if r['q'] in seen: continue
    seen.add(r['q'])
    if re.match(r'^(Beneteau|B.n.teau|Sun Odyssey|Sun Fast|Jeanneau)',r['n']): continue
    t=tok(r['n'])
    if r['code'] in 'YR' and t and (cnt[t]>=2 or t in DISPB) and not r['n'].startswith('Swan'):
        r['b']=t
    if r['n'].startswith('Swan'): r['b']='Nautor Swan'
    rows.append(r)
nread=int(open("nread.txt").read())
# duplicate-name fix
for r in rows:
    if r['n']=='Flipper': r['n']='Flipper (%s)'%('Denmark' if r['c']=='Denmark' else 'United States')
# existing entries map for dedupe (all sailing kinds)
exist={}
for kk in SAIL['k']:
    for e in kk.get('x',[]): exist[e['n'].lower()]=(kk,e)
ALIAS={'laser (ilca)':'laser / ilca','laser standard':'laser / ilca','laser radial (ilca 6)':'laser / ilca','laser 4.7 (ilca 4)':'laser / ilca','hobie cat':'hobie 16','platu 25':None,'international 14':None,'j-class yacht':None}
def wd_entry(r,kindname=None):
    bits=[]
    if r['y']: bits.append('Class from %s'%r['y'])
    if r['d']: bits.append('designed by %s'%r['d'])
    if r['c']: bits.append(r['c'])
    d=(', '.join(bits)+'.') if bits else ''
    e={'n':r['n'],'a':'','mk':r['d'],'y':r['y'],'s':W+r['q'],'v':[]}
    if d: e['d']=d
    return e
buildergroups={}
added=0
for r in rows:
    key=r['n'].lower()
    if key in ALIAS and ALIAS[key]:
        kk,e=exist[ALIAS[key]]
        if r['n'].startswith('Laser') :
            addv(e,r['n'],r['y'],'listed on Wikidata as a Laser variant')
        continue
    if key in exist: continue
    if r['b']:
        b=r['b']
        buildergroups.setdefault(b,[]).append(r); continue
    code=r['code']
    if code=='C':
        kn='Cruising multihull' if r['n'] in CRUISECAT else 'Racing multihull' if r['n'] in RACECAT else 'Beach catamaran'
    elif r['n'] in RACECAT: kn='Racing multihull'
    else: kn=kcode[code]
    k=kind(bo,kn)
    if addx(k,wd_entry(r)): added+=1
BKIND={'Archambault':'Racer-cruiser','Corsair Marine':'Cruising multihull','Nautor Swan':None,'Prindle':'Beach catamaran','Lagoon':'Cruising multihull'}
for b,rs in buildergroups.items():
    if b=='Nautor Swan':
        kk,e=exist['swan']
        for r in rs: addv(e,r['n'],r['y'],'listed on Wikidata',mk='Nautor Swan')
        continue
    kn=BKIND.get(b,'Cruising monohull')
    k=kind(bo,kn)
    disp=DISPB.get(b) or {'C&C':'C&C Yachts','Aloha':'Aloha Yachts','Bayfield':'Bayfield Yachts','Bristol':'Bristol Yachts','Contessa':'Contessa yachts','Edel':'Edel yachts','Grampian':'Grampian Marine','Mirage Yachts':'Mirage Yachts'}.get(b,b)
    ys=[yr(r['y']) for r in rs if yr(r['y'])]
    e={'n':disp,'a':'','mk':disp,'y':('%d–%d'%(min(ys),max(ys))) if ys else '','s':W+rs[0]['q'],'v':[],'d':'Builder with %d models listed on Wikidata as sailboat classes.'%len(rs)}
    for r in sorted(rs,key=lambda r:(yr(r['y']) or 9999,r['n'])):
        addv(e,r['n'],r['y'],('designed by %s'%r['d']) if r['d'] else '',mk=disp)
    ex=next((x for x in k['x'] if x['n'].lower()==disp.lower()),None)
    if ex is not None:
        for v in e['v']: addv(ex,v['n'],v['y'],v['d'],mk=disp)
        continue
    if addx(k,e): added+=1
report['sail_added']=added
# Wikidata sail rows excluded: windsurfers (RS:X, iQFoil, Mistral, Windglider) never transcribed
############ Beneteau, Jeanneau, HR entries
def fam(name,rowsl,mk,src,d,y,gen=False):
    e={'n':name,'a':'','mk':mk,'y':y,'s':src,'v':[],'d':d}
    for n,yy,x in rowsl:
        addv(e,n,yy,x,mk=mk)
    return e
cm=kind(bo,'Cruising monohull'); rc=kind(bo,'Racer-cruiser')
# existing Oceanis entry: replace versions
oc=next(e for e in cm['x'] if e['n']=='Beneteau Oceanis'); oc['v']=[]; oc['mk']='Beneteau'
for n,yy,x in B.OCEANIS: addv(oc,n,yy,x,mk='Beneteau')
oc['s']=B.BEN
fi=next((e for e in rc['x'] if e['n']=='Beneteau First'),None)
if fi is None:
    fi={'n':'Beneteau First','a':'','d':'Beneteau racer-cruiser range with seven generations from 1977.','mk':'Beneteau','y':'1977–','s':B.BEN,'v':[]}; rc['x'].append(fi)
fi['v']=[]; fi['s']=B.BEN
for n,yy,x in B.FIRST: addv(fi,n,yy,x,mk='Beneteau')
addx(rc,fam('Beneteau First Class and one-designs',[r for r in B.BEN_ONE if not r[0].startswith('Platu')],'Beneteau',B.BEN,'Beneteau one-design and First Class racing keelboats, 1982–2003.','1982–2003'))
addx(kind(bo,'Offshore racing class'),fam('Beneteau Figaro',B.FIGARO,'Beneteau',B.BEN,'Single-design offshore racer for the Figaro circuit, in three generations.','1994–'))
addx(cm,fam('Beneteau Sense',B.SENSE,'Beneteau',B.BEN,'Beneteau cruising yacht series with an open cockpit, first built 2010.','2010–'))
addx(cm,fam('Beneteau Idylle',B.IDYLLE,'Beneteau',B.BEN,'Beneteau cruising yachts of the 1980s.','1982–1985'))
addx(cm,fam('Beneteau early models',B.BEN_EARLY,'Beneteau',B.BEN,'Beneteau dinghies and small cruisers of the 1960s to 1980s, from the Guppy of 1964.','1964–1986'))
# Jeanneau
sun=[r for r in B.JEA_ALL if r[0].startswith('Sun Odyssey')]
fast=[r for r in B.JEA_ALL if r[0].startswith('Sun Fast')]
jy=[r for r in B.JEA_ALL if r[0].startswith('Jeanneau Yachts')]
lag=[r for r in B.JEA_ALL if r[0].startswith('Lagoon')]
rest=[r for r in B.JEA_ALL if r not in sun+fast+jy+lag]
for kn,nm,lst,d in ((cm,'Jeanneau Sun Odyssey',sun,'Jeanneau mass-market cruising range, from the Sun Odyssey 43 of 1986.'),(rc,'Jeanneau Sun Fast',fast,'Jeanneau performance cruiser and racer range, from the Sun Fast 1/2 Ton of 1984.'),(cm,'Jeanneau Yachts',jy,'Jeanneau flagship cruising yachts from 2008, numbered by length.'),(cm,'Jeanneau earlier designs',rest,'Jeanneau designs from the Sea-bird of 1960 to the Sun series, Gin Fizz, Melody and Symphonie.')):
    addx(kn,fam(nm,[(a,b,'') for a,b,*_ in lst],'Jeanneau',B.JEA,d,'%s–'%lst[0][1]))
mh=kind(bo,'Cruising multihull')
lg=next((e for e in mh['x'] if e['n']=='Lagoon'),None)
if lg is None:
    lg=fam('Lagoon',[(a,b,'') for a,b,*_ in lag],'Lagoon',B.JEA,'Catamaran range first built by Jeanneau in 1987 with the Lagoon 55.','1987–'); mh['x'].append(lg)
else:
    for a,b,*_ in lag: addv(lg,a,b,'',mk='Lagoon')
# Hallberg-Rassy
hr=next((e for e in cm['x'] if e['n']=='Hallberg-Rassy'),None)
if hr is None:
    hr={'n':'Hallberg-Rassy','a':'HR','d':'Swedish cruising yachts built at Ellös, designed by Germán Frers since 1989.','mk':'Hallberg-Rassy','y':'1964–','s':B.HR,'v':[]}; cm['x'].append(hr)
hr['s']=B.HR
for n,yy,x in B.HR_ROWS: addv(hr,n,yy,('designed by %s'%x) if x else '',mk='Hallberg-Rassy')
# Powerboat builders
BW=WIKI+'Boston_Whaler'; SR=WIKI+'Sea_Ray'; SS=WIKI+'Sunseeker'; AZ=WIKI+'Azimut_Yachts'
cc=kind(bo,'Centre console boat'); cab=kind(bo,'Cabin cruiser'); ten=kind(bo,'Tender'); perf=kind(bo,'Performance powerboat'); my=kind(bo,'Motor yacht'); ski=kind(bo,'Ski and wakeboard boat')
mont=next(e for e in cc['x'] if e['n']=='Boston Whaler Montauk')
def bwe(n,d,k): addx(k,{'n':n,'a':'','d':d,'mk':'Boston Whaler','y':'','s':BW,'v':[]})
bwe('Boston Whaler Dauntless','Centre consoles from 17 to 27.8 ft with 90–600 hp.',cc)
bwe('Boston Whaler Vantage','Centre consoles and a cuddy cabin from 23 to 33.5 ft with 250–800 hp.',cc)
bwe('Boston Whaler Conquest','Cuddy cabins from 27.8 to 41.3 ft with 450–1,600 hp.',cab)
bwe('Boston Whaler Realm','Cuddy cabins of 35.5 ft and 38 ft with 750–1,600 hp.',cab)
bwe('Boston Whaler Super Sport','Skiffs of 13 ft and 16 ft.',ten)
bwe('Boston Whaler Sport','Skiffs under 11.3 ft with 5–25 hp.',ten)
bwe('Boston Whaler Tender','Skiff of 11.3 ft with 5–15 hp.',ten)
addx(ski,{'n':'Sea Ray Ski Ray','a':'','d':'Sea Ray water-skiing tow boats, launched with the moulded-in swim platform.','mk':'Sea Ray','y':'1991','s':SR,'v':[]})
addx(perf,{'n':'Sunseeker Superhawk','a':'Superhawk 34 · Superhawk 43','d':'Sunseeker speedboat; the Superhawk 34 of 1999 appears in a Bond film river chase.','mk':'Sunseeker','y':'1999','s':SS,'v':[{'n':'Superhawk 34','mk':'Sunseeker','y':'1999','d':'chase boat in The World Is Not Enough'},{'n':'Superhawk 43','mk':'Sunseeker','y':'','d':'appears in a later Bond film'}]})
addx(perf,{'n':'Sunseeker Sovereign 17','a':'','d':'One of Sunseeker\'s first open-cockpit speedboats.','mk':'Sunseeker','y':'','s':SS,'v':[]})
addx(my,{'n':'Sunseeker 131','a':'','d':'Large Sunseeker motor yacht shown in the BBC documentary Chasing Perfection.','mk':'Sunseeker','y':'','s':SS,'v':[]})
addx(cab,{'n':'Azimut AZ 32 Targa','a':'','d':'Described as the "Ford T" of boating, aimed at the lower end of the market.','mk':'Azimut','y':'1977','s':AZ,'v':[]})
addx(cab,{'n':'Azimut AZ 43 Bali','a':'','d':'Mass-produced fibreglass boat built with Amerglass.','mk':'Azimut','y':'1979','s':AZ,'v':[]})
addx(my,{'n':'Azimut 105 Failaka','a':'','d':'Launched to target the high end of the market.','mk':'Azimut','y':'1982','s':AZ,'v':[]})
# Riva Aquarama versions
RV=WIKI+'Riva_Aquarama'
aq=next(e for e in kind(bo,'Classic wooden runabout')['x'] if e['n']=='Riva Aquarama')
aq['s']=RV; aq['v']=[]
for n,yy,d in (('Aquarama','1962–1972','281 built'),('Super Aquarama','1963–1971','203 built'),('Aquarama Lungo','1972','7 built'),('Aquarama Special','1972–1996','277 built'),('Riva Lamborghini','1968','one-off with two Lamborghini V12 engines')):
    addv(aq,n,yy,d,mk='Riva')
aq['d']='Carlo Riva\'s luxury wooden runabout, built 1962 to 1996 with a hull based on the Tritone.'
# Old Town canoes
OT=WIKI+'Old_Town_Canoe'; cano=kind(bo,'Canoe')
for n,yy,d in (('Old Town Yankee Model','1935','Sigurd Olson bought several for his Border Lakes Outfitters'),('Old Town Common Sense Fifty Pound Model','1922','15 ft canoe; Gifford Pinchot received one'),('Old Town HW model (wood-canvas)','1934','Design no. 4'),('Old Town Guide Model','','16 ft; seven were used in making the film Deliverance'),('Old Town Discovery 158','','canoe pictured on the River Ure, England')):
    addx(cano,{'n':n,'a':'','d':d+'.','mk':'Old Town','y':yy,'s':OT,'v':[]})
############ sort, group, nl/sel for boats
KIND_NL={}
def finalize_kind(k,nl,sel,mode='era'):
    k['nl']=nl
    for e in k.get('x',[]):
        if mode=='era': e['g']=era(e.get('y'))
        for v in e.get('v',[]): pass
    if mode=='era':
        k['x'].sort(key=lambda e:(ERA_ORDER.index(e['g']),yr(e.get('y')) or 9999,e['n'].lower()))
    k['sel']=sel
    k['xg']='Entries are grouped by the era the class or design began: before 1950, 1950–1969, 1970–1989, 1990 onward, then year not stated.'
SAILNL={'Sailing dinghy':'One entry is a sailing dinghy class or design with its own rules; hull builders and rig sizes are versions.',
'Racing skiff and foiler':'One entry is a high-performance skiff or foiling class; builders and rig sizes are versions.',
'Beach catamaran':'One entry is a beach or sports catamaran class; builders and sail plans are versions.',
'Racing multihull':'One entry is a racing catamaran or trimaran class; builders and series are versions.',
'Open keelboat':'One entry is an open keelboat class; builders and rig variants are versions.',
'Racer-cruiser':'One entry is a racer-cruiser or sportboat class, or one builder\'s range of them; individual models are versions.',
'Rating-rule class':'One entry is a rating-rule class (International Rule metre classes, J-class); builders and hull ages are versions.',
'Offshore racing class':'One entry is an offshore class; generations are versions.',
'Cruising monohull':'One entry is a cruising yacht model line or a builder\'s range; sizes and generations are versions.',
'Cruising multihull':'One entry is a cruising catamaran or trimaran range; sizes are versions.',
'Ice boat':'One entry is an ice-boat class.'}
cov={}
def covline(n): return 'Covers %d of about 1,943 in the Wikidata sailboat class set (Q106179098); the rest are classes with two or fewer Wikipedia articles, mostly one-off production yachts, not read in this pass. Windsurfer classes (RS:X, iQFoil, Mistral One Design, Windglider) are left to E2.'%nread
for k in SAIL['k']:
    if k['n'] in SAILNL and k.get('x'):
        finalize_kind(k,SAILNL[k['n']],'Follows Wikidata\'s sailboat class set (read in order of Wikipedia sitelinks, classes first, then the sitelink-2 tier A to R, reading rows 1 to 533), World Sailing and Olympic classes, plus Wikipedia builder pages for Beneteau, Jeanneau and Hallberg-Rassy. '+covline(k['n']))
# DN in ice boat
wi=[r for r in [] ]
# powerboat / other kinds
OTHER_NL={'Canoe':'One entry is a canoe model line or builder\'s historic model; sizes and colours are versions.','Kayak':'One entry is a kayak design or maker\'s folding or skin-on-frame line; sizes and builds are versions.','River raft':'One entry is a river raft or packraft design.','Rowing boat':'One entry is a traditional rowing boat type.','Rowing shell':'One entry is a racing-shell maker\'s line.','Pedal boat':'One entry is a pedal boat design.','Pontoon boat':'One entry is a pontoon boat range.','Bowrider':'One entry is a bowrider range.','Ski and wakeboard boat':'One entry is a tow-boat model line.','Jet boat':'One entry is a jet-boat range.','Performance powerboat':'One entry is a performance powerboat line.','Personal watercraft':'One entry is a maker\'s personal watercraft line; models are versions.','eFoil':'One entry is an electric hydrofoil board maker\'s line.','Classic wooden runabout':'One entry is a classic runabout model line; versions are marks and years.','Bass boat':'One entry is a bass boat maker\'s line.','Flats boat':'One entry is a flats boat line.','Centre console boat':'One entry is a model line of centre console boats; lengths are versions.','Sport-fishing boat':'One entry is a sport-fishing boat line.','Cabin cruiser':'One entry is a cabin cruiser model line.','Trawler':'One entry is a trawler yacht line.','Motor yacht':'One entry is a motor-yacht model line or builder\'s range.','Superyacht':'One entry is a superyacht builder\'s custom range.','Rigid inflatable boat':'One entry is a RIB model line.','Tender':'One entry is a yacht-tender model line.','Motorsailer':'One entry is a motorsailer line.','Classic wooden yacht':'One entry is a classic yacht design.','Gulet':'One entry is a gulet type.'}
BOATSEL='Follows the maker and overview pages fetched for each entry (Wikipedia builder and model pages, plus Old Town Canoe, Riva Aquarama, Boston Whaler, Sea Ray, Sunseeker and Azimut Yachts). No whole-space reference exists for powerboats and paddle craft; Wikipedia builder pages were read in full for the builders named, which are all that was read in this pass.'
for s in bo['s']:
    for k in s['k']:
        if k.get('nl') : continue
        if k.get('x'):
            finalize_kind(k,OTHER_NL.get(k['n'],'One entry is a model line or design.'),BOATSEL)
        for e in k.get('x',[]): e.setdefault('v',[])
# drop loose models
dropped=[]
for s in bo['s']:
    for k in s['k']:
        for m in k.pop('m',[]) or []: dropped.append((k['n'],m))
report['boat_dropped']=dropped
# Sea-Doo as entry with versions from former m (kind source retained)
pw=kind(bo,'Personal watercraft')
sd=[m for kn,m in dropped if kn=='Personal watercraft']
if sd:
    e={'n':'Sea-Doo','a':'','d':'Bombardier Recreational Products personal watercraft range.','mk':'Sea-Doo','y':'','s':pw['s'],'v':[]}
    for n,mkr in sd: addv(e,n,'','',mk=mkr)
    if addx(pw,e): finalize_kind(pw,OTHER_NL['Personal watercraft'],BOATSEL)
# boats note, ms
bo['note']='By use, with designs and class rules as entries; sailing classes follow Wikidata, builders follow their own pages and the brand register gives owners.'
bo['ms']=[
 {'mkt':'Recreational boat builders','who':'Brunswick Corporation','share':'owns Boston Whaler (bought 1996 for $27.4 million) and Sea Ray (bought 1986 for $350 million)','yr':2026,'s':BW,'note':'ownership stated on the Boston Whaler and Sea Ray Wikipedia pages'},
 {'mkt':'Recreational boat builders','who':'Groupe Beneteau','share':'owns Beneteau and Jeanneau (bought 1995); bought Seascape in 2018','yr':2026,'s':B.JEA,'note':'ownership stated on the Jeanneau and Beneteau Wikipedia pages'},
 {'mkt':'Motor yachts','who':'Lionheart Capital and Orienta Capital Partners','share':'owners of Sunseeker since 2024, bought from Dalian Wanda Group','yr':2024,'s':SS,'note':'ownership as stated on the Sunseeker Wikipedia page'},
 {'mkt':'Motor yachts','who':'Azimut Benetti S.p.A.','share':'Azimut bought Benetti in 1985','yr':1985,'s':AZ,'note':'group history as stated on the Azimut Yachts page'},
 {'mkt':'Cruising yachts','who':'The Rassy family','share':'owner of Hallberg-Rassy; Germán Frers has designed every boat since 1989','yr':2026,'s':B.HR,'note':'ownership and design as stated on the Hallberg-Rassy page'},
 {'mkt':'Canoes and kayaks','who':'Johnson Outdoors','share':'owner of Old Town since 2004 (S.C. Johnson from 1974)','yr':2004,'s':OT,'note':'Old Town began making kayaks in 1995'}]
bo['msum']='Boat ownership sits with a few groups: Brunswick for American runabouts and day boats, Groupe Beneteau for French sailing yachts, and family or private owners for the rest. No market-share figures were found on a fetched page.'
json.dump({'dept':bo,'nread':nread,'dropped':dropped},open('boats_out.json','w'))
print('boats ok',added,len(dropped))
