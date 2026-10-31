import json,re,os,copy,collections,urllib.parse
W='/home/user/Possession-Taxonomy/rebuild/work/V4_G1_MOTO/'
OUT='/home/user/Possession-Taxonomy/rebuild/out/'
exec(open(W+'build_head.py').read())   # cands from wikidata + lists, helpers
# ---- new marque/owner table (Wikidata + fetched pages)
MQ={}
for l in open(W+'marques2.txt'):
    p=l.rstrip('\n').split('|')
    MQ[p[0]]=(p[1],p[2],p[3],p[4])
DEF2={'AJS','Matchless','Ariel','BSA','Douglas','Greeves','James','Velocette','Vincent','DKW','NSU','Zündapp','Kreidler','Hercules','Excelsior','FN','Hesketh','Scott','Sunbeam','Panther','Motobécane','Csepel','Pope','Pierce-Arrow','Curtiss','MZ','Simson'}
CT={'Ariel':'United Kingdom','BSA':'United Kingdom','Douglas':'United Kingdom','Greeves':'United Kingdom','James':'United Kingdom','Velocette':'United Kingdom','Vincent':'United Kingdom','DKW':'Germany','NSU':'Germany','Zündapp':'Germany','Kreidler':'Germany','Hercules':'Germany','Excelsior':'United Kingdom','FN':'Belgium','Hesketh':'United Kingdom','Scott':'United Kingdom','Sunbeam':'United Kingdom','Panther':'United Kingdom','Motobécane':'France','Csepel':'Hungary','Pope':'United States','Pierce-Arrow':'United States','Curtiss':'United States','MZ':'Germany','Simson':'Germany','Mondial':'Turkey','Petronas':'Malaysia','Sachs':'Germany','Subaru':'Japan','Boss Hoss Cycles':'United States','Modenas':'Malaysia','Yadea':'China','Horex':'Germany','Aston Martin':'United Kingdom','Riga':'Latvia','Tula':'USSR','Sokół':'Poland','SHL':'Poland','Podolsk':'USSR','Puch':'Austria','Tomos':'Slovenia','Solex':'France','Montesa Honda':'Spain','Beta':'Italy','Bultaco':'Spain','Gelbke':'United States','Allen Millyard':'United Kingdom','Rikuo':'Japan','Aero':'Japan','Thomas':'United States','Ilmor':'United Kingdom'}
def mq(m):
    if m in MQ:
        o,t,c,y=MQ[m]; return (o,t,c,y)
    if m in DEF2: return ('None (marque defunct)','Independent',CT.get(m,''),'')
    return ('owner not stated','Independent',CT.get(m,''),'')
# ---- type files
TYPEFILES=[('Trike','cat_Trike.txt'),('Underbone motorcycle','cat_Underbone_motorcycle.txt'),('Moped','cat_Moped.txt'),('Scooter','cat_Scooter.txt'),('Dual-sport motorcycle','cat_Dual-sport_motorcycle.txt'),('Cruiser motorcycle','cat_Cruiser_motorcycle.txt'),('Touring motorcycle','cat_Touring_motorcycle.txt'),('Sport motorcycle','cat_Sport_motorcycle.txt'),('Trail bike','cat_Trail_bike.txt'),('Standard motorcycle','cat_Standard_motorcycle.txt')]
CATURL={'Trike':'Category:Tricycle_motorcycles','Underbone motorcycle':'Category:Underbone_motorcycles','Moped':'Category:Mopeds','Scooter':'Category:Motor_scooters','Dual-sport motorcycle':'Category:Dual-sport_motorcycles','Cruiser motorcycle':'Category:Cruiser_motorcycles','Touring motorcycle':'Category:Touring_motorcycles and Category:Sport_touring_motorcycles','Sport motorcycle':'Category:Sport_bikes','Trail bike':'Category:Off-road_motorcycles','Standard motorcycle':'Category:Standard_motorcycles'}
SKIPT={'Dual-sport motorcycle','Cruiser (motorcycle)','Touring motorcycle','Sport bike','Sport touring motorcycle','Scooter (motorcycle)','Moped','Underbone','Sport moped','Universal Japanese Motorcycle','Café racer','Streetfighter (motorcycle)','Enduro motorcycle','Rokon (motorcycle manufacturer)','Carver (automotive company)','KTM LC4 engine','Types of motorcycles','Kawasaki triple'}
def nk2(name,marque):
    n=re.sub(r'\s*\((motorcycle|scooter|moped|motor scooter|motorcycle manufacturer|bike)\)','',name)
    n=re.split(r' and | & ',n)[0] if re.search(r'^\S+ \S*\d',n) else n
    return norm_key(n,marque)
typeof={}; cattitles=[]; catcount=collections.Counter()
for kind,fn in TYPEFILES:
    for t in open(W+fn).read().replace('\n',' ').split(';'):
        t=t.strip()
        if not t or t in SKIPT: continue
        m=marque_of(t,'')
        cattitles.append((t,m,kind)); catcount[kind]+=1
        typeof.setdefault(nk2(t,m),kind)
# list-section types
SEC_TYPE={'Step-throughs, scooters, underbones':'Scooter','Maxi-scooters':'Scooter','Three-wheelers':'Scooter','Trail two-stroke':'Trail bike','Trail four-stroke':'Trail bike','Enduro':'Enduro bike','Trials':'Trials bike','Motocross':'Motocross bike',
 'Sport':'Sport motorcycle','Sport-touring':'Touring motorcycle','Cruiser':'Cruiser motorcycle','Scooters':'Scooter','Off road':'Trail bike','Dual purpose':'Dual-sport motorcycle',
 'Touring':'Touring motorcycle','Trikes':'Trike','Adventure touring':'Adventure motorcycle'}
SUZ={'Mini bike':{'JR50','MT50 Trailhopper','PV50','RB50 GAG'},'Scooter':{'CS','CP50','Sepia ZZ','SJ50','RC50','Choinori','FA50','FM50','FZ50','FY50 Youdy','M30 Mokick','M31',"Let's",'Mini Free MF1','Suzumoped','FX110','Sixteens','Gemma'},'Sport motorcycle':{'FXR150','Satria R','SFV650 Gladius','SV650','SV1000','SV-7 GX','TL1000R','TL1000S','XN85'}}
SUZ_KEYS={}
for k,v in SUZ.items():
    for n in v: SUZ_KEYS[nk2('Suzuki '+n,'Suzuki')]=k
# honda sections
HSEC={}
sec=None
for l in open(W+'wp_honda_sec.txt'):
    l=l.strip()
    if l.startswith('@'): sec=l[1:].split('|')[0]; continue
    for n in l.split(';'):
        if n: HSEC[nk2('Honda '+n.strip(),'Honda')]=sec
# add honda section + table candidates
for k,v in HSEC.items(): pass
sec=None
for l in open(W+'wp_honda_sec.txt'):
    l=l.strip()
    if l.startswith('@'): sec=l[1:].split('|')[0]; continue
    for n in l.split(';'):
        n=n.strip()
        if n: add('Honda '+n if not n.startswith('Honda') else n,'','Honda',WP+'List_of_Honda_motorcycles',3,'')
HONDA_TABLE=[]
for it in open(W+'honda_eng.txt').read().replace('\n','').split(';'):
    if '|' not in it: continue
    n,cc=it.rsplit('|',1)
    HONDA_TABLE.append((n.strip(),cc.strip()))
# ---- curated
old=json.load(open(OUT+'G1.json'))
dept=[d for d in old['depts'] if d['n']=='Motorcycles & scooters'][0]
gear=[d for d in old['depts'] if d['n']=='Motorcycle riding gear'][0]
MKMAP={'Yamaha Motor':'Yamaha','BMW':'BMW Motorrad','Husqvarna':'Husqvarna Motorcycles','Triumph Motorcycles':'Triumph','Bajaj Auto':'Bajaj'}
def getm(x):
    nm=x['n']
    for p,m in PREF:
        if nm.startswith(p): return m
    return MKMAP.get(x.get('mk',''),x.get('mk','')) or 'Other marques'
def decorate(e,m):
    o,t,c,y=mq(m)
    e['g']=m; e['mk']=m; e['own']=o; e['tier']=t
    if c: e['cty']=c
    if y: e['own_y']=y
    return e
kinds=collections.OrderedDict()   # kind name -> list
NOTSTATED='Motorcycle, type not stated'
KS=['Standard motorcycle','Sport motorcycle','Cruiser motorcycle','Touring motorcycle','Adventure motorcycle','Café racer','Scrambler','Chopper and bobber','Trike','Motorcycle with sidecar','Motocross bike','Enduro bike','Trials bike','Supermoto','Dual-sport motorcycle','Trail bike','Pit bike','Scooter','Moped','Underbone motorcycle','Mini bike',NOTSTATED]
for k in KS: kinds[k]=[]
seen=set(); other_kinds={}
cnt=collections.Counter()
for s in dept['s']:
    for k in s['k']:
        for x in k.get('x',[]):
            if k['n'] in kinds:
                m=getm(x); e=decorate(copy.deepcopy(x),m)
                seen.add(nk2(x['n'],m)); kinds[k['n']].append(e); cnt['cur']+=1
            else:
                other_kinds.setdefault(k['n'],[]).append(x)
def resolve(name,m,sec,srcrank):
    key=nk2(name,m)
    if sec in SEC_TYPE and m in('Yamaha','Kawasaki','Harley-Davidson'): return SEC_TYPE[sec]
    if m=='Suzuki' and key in SUZ_KEYS: return SUZ_KEYS[key]
    if m=='Honda' and key in HSEC: return HSEC[key]
    if key in typeof: return typeof[key]
    if m=='Vespa': return 'Scooter'
    return NOTSTATED
WD_TYPE={'Yamaha_SZR660':'Sport motorcycle','Yamaha_XZ_550':'Sport motorcycle','Yamaha_FZ750':'Sport motorcycle','Ducati_Panigale_V4':'Sport motorcycle','Yamaha_RD500LC':'Sport motorcycle','Yamaha_FZR1000':'Sport motorcycle','Yamaha_FZR400':'Sport motorcycle','Yamaha_FZS600_Fazer':'Sport motorcycle','Ducati_Panigale_V2':'Sport motorcycle','James_Autocycle':'Moped'}
def addentry(name,m,y,s,sec,rank,d=None):
    key=nk2(name,m)
    if key in seen: return
    seen.add(key)
    kind=None
    t=s.split('/wiki/')[-1] if '/wiki/' in s else ''
    kind=WD_TYPE.get(t) or resolve(name,m,sec,rank)
    e={'n':name,'mk':m,'s':s}
    if y: e['y']=y
    if d: e['d']=d
    decorate(e,m)
    kinds[kind].append(e); cnt[kind]+=1
cands.sort(key=lambda c:c['r'])
for c in cands:
    if c['n'] in SKIPT: continue
    addentry(c['n'],c['m'],c['y'],c['s'],c['sec'],c['r'])
for t,m,kind in cattitles:
    nm=re.sub(r'\s*\((motorcycle|scooter|moped|motor scooter)\)$','',t)
    addentry(nm,m,'',WP+quote_title(t.replace(' ','_')),'',2.5)
for n,cc in HONDA_TABLE:
    nm=n if n.startswith('Honda') else 'Honda '+n
    m=re.search(r'\(([A-Z]{1,4}\d[^,)]*)',n)
    key2=nk2('Honda '+m.group(1),'Honda') if m else None
    base=re.split(r' also known| \(|, |/',n)[0].strip()
    key3=nk2('Honda '+base,'Honda')
    if (key2 and key2 in seen) or (not key2 and key3 in seen): continue
    addentry(nm,'Honda','',WP+'List_of_Honda_motorcycles','',3,d=cc+' cc, engine-size table')
    seen.add(key3)
    if key2: seen.add(key2)
# gold wing versions
GW=['GL1000','GL1100','GL1200','GL1500','GL1800']
for k in kinds:
    for e in kinds[k]:
        if e['n']=='Honda Gold Wing': e['v']=[{'n':'Gold Wing '+g,'mk':'Honda','y':'','d':'engine size in the model code, from the engine-size table'} for g in GW]
def ykey(e):
    mm=re.search(r'\d{4}',e.get('y',''))
    return int(mm.group()) if mm else 9999
for k in kinds:
    kinds[k].sort(key=lambda e:(e['g'].lower(),ykey(e),e['n'].lower()))
marques=collections.Counter(); 
for k in kinds:
    for e in kinds[k]: marques[e['g']]+=1
total=sum(len(v) for v in kinds.values())
# ---- assemble dept
READ='Wikidata classes Q23866334 (1,194 rows, all windows read), Q71310524 and Q34493 (about 225 rows), 21 Wikipedia per-manufacturer lists, the Honda engine-size table (all %d rows), and Wikipedia titles of the type categories named in each kind'%len(HONDA_TABLE)
catn={'Trike':(12,12,'Category:Tricycle_motorcycles'),'Underbone motorcycle':(21,21,'Category:Underbone_motorcycles'),'Moped':(46,46,'Category:Mopeds'),'Scooter':(162,162,'Category:Motor_scooters'),'Dual-sport motorcycle':(130,130,'Category:Dual-sport_motorcycles'),'Cruiser motorcycle':(92,92,'Category:Cruiser_motorcycles'),'Touring motorcycle':(86,86,'Category:Touring_motorcycles and Category:Sport_touring_motorcycles'),'Sport motorcycle':(221,221,'Category:Sport_bikes'),'Trail bike':(64,64,'Category:Off-road_motorcycles'),'Standard motorcycle':(336,336,'Category:Standard_motorcycles')}
subnote={'Scooter':'; its subcategories (electric, Indian, maxi, Piaggio Vespa scooters) were not read','Moped':'; its 5 subcategories were not read','Dual-sport motorcycle':'; the Rally raid bikes subcategory was not read'}
def cov(kind):
    a,b,c=catn[kind]
    got=catcount[kind]
    sub=subnote.get(kind,'')
    return 'Covers %d model pages of the %d pages in %s; the rest are general, manufacturer, engine or non-motorcycle pages%s.'%(got,b,c,sub)
SECTXT={'Standard motorcycle':'Type is stated by Wikipedia category membership (Standard motorcycles). ','Sport motorcycle':'Type from Wikipedia categories (Sport bikes) and the Yamaha and Kawasaki list sections. ','Cruiser motorcycle':'Type from Wikipedia category (Cruiser motorcycles). ','Touring motorcycle':'Type from Wikipedia categories (Touring and Sport touring motorcycles) and list sections. ','Dual-sport motorcycle':'Type from Wikipedia category (Dual-sport motorcycles) and the Honda dual-purpose section. ','Trail bike':'Type from the Wikipedia Off-road motorcycles category, which does not state a finer type, and Yamaha, Honda and Kawasaki off-road list sections. ','Scooter':'Type from Wikipedia category (Motor scooters) and list sections; the Vespa marque is a scooter marque on its article. ','Moped':'Type from Wikipedia category (Mopeds). ','Underbone motorcycle':'Type from Wikipedia category (Underbone motorcycles). ','Trike':'Type from Wikipedia category (Tricycle motorcycles) and the Harley-Davidson trikes section. '}
def kind_obj(name):
    o=None
    for s in dept['s']:
        for k in s['k']:
            if k['n']==name: o=copy.deepcopy(k)
    if o is None:
        o={'n':name,'a':'','d':'Motorcycle or scooter whose type no fetched source states, listed by marque.','s':'https://en.wikipedia.org/wiki/List_of_motorcycle_manufacturers','tt':[['Source of model',['Wikidata motorcycle model','Wikipedia per-manufacturer list']]]}
    o.pop('m',None); o.pop('r',None)
    if not o.get('a'): o.pop('a',None)
    xs=kinds.get(name,None)
    if xs is None: xs=copy.deepcopy(other_kinds.get(name,[]))
    for e in xs:
        if 'g' not in e:
            mkr=e.get('mk',''); mm=getm(e); decorate(e,mm)
    if xs or name==NOTSTATED:
        o['x']=xs
        o['nl']='One entry is a motorcycle or scooter model line or design sold or raced under a marque name; generations, capacity variants and special editions are versions.'
        base=READ+'. Sections are marques (home country and owner on each entry). '
        if name==NOTSTATED:
            o['sel']=base+'This kind holds every model whose type no fetched source states. Concepts, prototypes, quads and side-by-sides are left out; marques and countries follow Wikipedia\'s List of motorcycle manufacturers (read to its end, about 430 marque names). Owners follow Wikidata parent-organisation statements (one query for all maker items) or the marque page; where neither states an owner the entry says so. Covers %d model lines under %d marques; the Honda table is complete, the Honda, Yamaha, Suzuki and Kawasaki lists were read to their ends, and BMW, Ducati, Aprilia, Husqvarna, Indian and Lambretta have no Wikipedia list and rest on Wikidata and category pages.'%(len(xs),len({e['g'] for e in xs}))
        elif name in catn:
            o['sel']='Type from Wikipedia category and list sections; marque, owner and country as in the other kinds. '+SECTXT.get(name,'')+cov(name)+' Curated entries from the structure pass are kept.'
        else:
            o['sel']='Entries kept from the structure pass or placed by a list section that names this type (for example Yamaha trials, enduro and motocross sections); no whole-space reference exists for this type, so the list is partial.'
        o['xg']='by marque (alphabetical), then year'
    return o
shelves=[]
for s in dept['s']:
    ks=[kind_obj(k['n']) for k in s['k']]
    shelves.append({**{k:v for k,v in s.items() if k!='k'},'k':ks})
shelves.append({'n':'Type not stated','t':'Motorcycles and scooters whose type no fetched source states, listed by marque; a model with a stated type is in its type kind.','ax':'one kind: the model, listed by marque','k':[kind_obj(NOTSTATED)]})
newdept=copy.deepcopy(dept); newdept['s']=shelves
newdept['note']='Organised type → marque → model line → generation; type comes from Wikipedia categories and list sections only, otherwise the model is under Type not stated.'
for s in newdept['s']:
    for k in s['k']:
        if k.get('x'):
            for e in k['x']:
                if 'g' not in e: pass
# owners for non-canon kinds already decorated; electric kinds: drop m
# ---- market summary
AC='https://autocarpro.in/news/hero-motocorp-leads-fy25-2-wheeler-retail-sales-market-share-dips-125783'
ms=[]
for who,sh,vol in (('Hero MotoCorp','28.84 %','54.45 lakh units'),('Honda Motorcycle & Scooter India','25.37 %','47.89 lakh units'),('TVS Motor','17.49 %','33.02 lakh units'),('Bajaj Auto','11.41 %','21.54 lakh units'),('Royal Enfield','4.47 %','8.43 lakh units'),('Yamaha Motor India','3.44 %','6.50 lakh units')):
    ms.append({'mkt':'India two-wheelers, retail','who':who,'share':sh,'yr':2025,'s':AC,'note':'financial year 2024-25 retail, %s'%vol})
HOGS='https://www.sec.gov/Archives/edgar/data/793952/000079395225000063/hog-20241231.htm'
ms+=[{'mkt':'United States new motorcycle registrations, 601cc and over','who':'Harley-Davidson','share':'37.3 %','yr':2024,'s':HOGS,'note':'Form 10-K, industry data from the Motorcycle Industry Council; 94,383 new registrations; 37.9 % in 2023 and 41.2 % in 2022'},
 {'mkt':'Europe new motorcycle registrations, 601cc and over','who':'Harley-Davidson','share':'5.0 %','yr':2024,'s':HOGS,'note':'Form 10-K, industry data from Management Services Helwig Schmitt; 25,860 new registrations; 4.8 % in 2023'},
 {'mkt':'World motorcycles (Honda Group unit sales)','who':'Honda','share':'','yr':2024,'s':'https://global.honda/en/investors/news/news202405107/main/0/link/FY202403_4Q_financial_presentation_script_e_1.pdf','note':'fiscal year to March 2024: 18,819 thousand units (motorcycles, ATVs and side-by-sides), forecast 19,800 thousand; North America 498 thousand, Europe 440 thousand, Japan 241 thousand; no world market total on the page'},
 {'mkt':'Indonesia motorcycles','who':'Honda','share':'73.8 %','yr':2016,'s':'https://databoks.katadata.co.id/en/transportation-logistics/statistics/126b46d44bcef26/honda-remains-dominant-in-domestic-motorcycle-sales','note':'4.38 million of 5.93 million units, AISI; newest brand split found'},
 {'mkt':'Indonesia motorcycles','who':'Yamaha','share':'23.5 %','yr':2016,'s':'https://databoks.katadata.co.id/en/transportation-logistics/statistics/126b46d44bcef26/honda-remains-dominant-in-domestic-motorcycle-sales','note':'1.39 million units'},
 {'mkt':'Indonesia motorcycles','who':'All brands','share':'','yr':2024,'s':'https://auto.katadata.co.id/motor/new-motorcycle-sales-in-2024-reached-63-million-units-surpassing-2023-17613','note':'6,333,310 domestic units, 572,506 exported (AISI); no brand split on the page'},
 {'mkt':'India motorcycles','who':'Bajaj Auto','share':'31 %','yr':2013,'s':'https://en.wikipedia.org/wiki/Bajaj_Auto','note':'financial year 2012-13'},
 {'mkt':'India two-wheelers','who':'Hero MotoCorp','share':'30 %','yr':2024,'s':'https://en.wikipedia.org/wiki/Hero_MotoCorp','note':'as of March 2024, as the article states'}]
newdept['ms']=ms
newdept['msum']="India's two-wheeler market was led by Hero MotoCorp (28.84 %) and Honda (25.37 %) in 2024-25. Harley-Davidson held 37.3 % of new US registrations of 601cc and over in 2024 (Motorcycle Industry Council data in its 10-K). Honda Group sold 18.8 million units in the year to March 2024. Indonesia was 73.8 % Honda and 23.5 % Yamaha in 2016."
# ---- gear (unchanged logic)
newgear=copy.deepcopy(gear)
rm=0; re_=0
for s in newgear['s']:
    for k in s['k']:
        rm+=len(k.get('m',[])); xs=k.pop('x',[]) or []; k.pop('m',None); k.pop('r',None)
        mks=sorted({e['mk'] for e in xs if e.get('mk')})
        if k['n'].endswith('helmet') and mks: k['tt']=(k.get('tt') or [])+[['Helmet line maker',mks]]
        if k['n'] in('Full-face helmet','Modular helmet','Dual-sport helmet','Off-road helmet','Open-face helmet'): k['tt']=(k.get('tt') or [])+[['Safety standard',['ECE 22.06','DOT FMVSS 218','Snell M2020']]]
        re_+=len(xs)
        if k['n']=='Full-face helmet':
            bs=[e for e in xs if e['n']=='Bell Star']
            if bs:
                e=bs[0]; e['role']='origin'; e['g']='Bell'; e['own']='owner not stated'; e['tier']='Independent'; e['cty']='United States'
                k['x']=[e]; re_-=1
                k['nl']='One entry is the origin helmet of this kind; helmet lines and standards are attributes (tt), not entries.'
                k['sel']='Commodity kind under the icon rule: one origin entry, the first full-face motorcycle helmet, from the Bell Sports page. Helmet makers and standards are types.'
        if k.get('see')==[]: k.pop('see',None)
newgear['note']='Commodity kinds: helmet makers and standards are types; only the origin helmet is an entry.'
part={'replaces':['Motorcycles & scooters','Motorcycle riding gear'],'depts':[newdept,newgear],'brands':[],'brand_updates':{},'renames':{},'moves':[]}
MFILE=json.load(open(OUT+'G1_brands.json'))['b']; exist={b['n'] for b in MFILE}
LISTURL='https://en.wikipedia.org/wiki/List_of_motorcycle_manufacturers'
WDQ='https://query.wikidata.org/sparql'
for m,n in marques.items():
    o,t,c,y=mq(m)
    upd={'own':o,'tier':t}
    if c: upd['c']=c
    if y: upd['own_y']=y
    if m in exist: part['brand_updates'][m]=upd
    else:
        b={'n':m,'own':o,'tier':t,'s':{'Hero MotoCorp':'https://en.wikipedia.org/wiki/Hero_MotoCorp','Bajaj':'https://en.wikipedia.org/wiki/Bajaj_Auto','TVS':'https://en.wikipedia.org/wiki/TVS_Motor_Company'}.get(m,LISTURL)}
        if c: b['c']=c
        if y: b['own_y']=y
        part['brands'].append(b)
for alt,tgt in (('BMW','BMW Motorrad'),('Yamaha Motor','Yamaha')):
    if alt in exist and tgt in marques:
        o,t,c,y=mq(tgt); part['brand_updates'][alt]={'own':o,'tier':t,'c':c}
json.dump(part,open(OUT+'G1_parts/MOTO.json.tmp','w'),ensure_ascii=False)
os.replace(OUT+'G1_parts/MOTO.json.tmp',OUT+'G1_parts/MOTO.json')
print('total entries',total,'marques',len(marques))
print({k:len(v) for k,v in kinds.items()})
print('gear removed models',rm,'entries',re_,'size',os.path.getsize(OUT+'G1_parts/MOTO.json'))
print({k:(catn[k][1],catcount[k]) for k in catn})
