import json,re,unicodedata,urllib.parse,collections,copy
R='/home/user/Possession-Taxonomy/rebuild/'
exec(open(R+'work/V4_G1_CARS/data1.py').read())
g1=json.load(open(R+'out/G1.json'))
cars=copy.deepcopy([x for x in g1['depts'] if x['n']=='Cars'][0])
brands_old={b['n']:b for b in json.load(open(R+'out/G1_brands.json'))['b']}
KIND={'C':'City car','H':'Hatchback','S':'Saloon','E':'Estate','M':'MPV','U':'SUV','L':'Luxury saloon','Q':'Limousine','G':'Grand tourer','P':'Sports car','X':'Coupé','V':'Convertible','R':'Roadster','T':'Hot hatch','W':'Muscle car','Z':'Supercar','Y':'Hypercar','O':'Off-roader','A':'Kei car','B':'Microcar','D':'Three-wheeled car','c':'Coachbuilt car','k':'Kit car','h':'Hot rod and custom car'}
def norm(s):
    s=unicodedata.normalize('NFKD',s).lower()
    s=''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]','',s)
def wurl(t): return 'https://en.wikipedia.org/wiki/'+urllib.parse.quote(t.replace(' ','_'),safe="()',:.!*~-_/&@+$;=")
def yr(y):
    m=re.search(r'\d{4}',y or ''); return int(m.group()) if m else 9999
# existing index
kinds={}
for sh in cars['s']:
    for k in sh['k']: kinds[k['n']]=k
byname={}
for kn,k in kinds.items():
    for x in k.get('x',[]):
        byname[norm(x['n'])]=(kn,x)
        for a in re.split(r'\s*[·,;]\s*',x.get('a','') or ''):
            if a: byname.setdefault(norm(a),(kn,x))
        x['_mk']=x.get('mk','')
def fold(t):
    m=re.match(r'^(.*?) \(([^)]*)\)$',t)
    if m:
        ins=m.group(2)
        if 'generation' in ins or re.fullmatch(r'[A-Z]{1,4}\d{0,4}[A-Za-z]?(/[A-Z]\d+)?',ins) or re.fullmatch(r'\d{4}([–-]\d{4})?',ins): return m.group(1),ins
    m=re.match(r'^(.*) (Mk ?\d+)$',t)
    if m: return m.group(1),m.group(2)
    return None
pick=[]; dropped_m=[]
items=[]  # (title,marque,code,year)
seen=set()
for key,(own,cty,oy,tier,spec) in D.items():
    mq=key.split('#')[0]
    for blk in spec.split('|'):
        code,_,names=blk.partition(':')
        for nm in names.split(';'):
            nm=nm.strip()
            if not nm: continue
            y=''
            if '~' in nm: nm,y=nm.rsplit('~',1)
            if nm.startswith('='): t=nm[1:]
            elif nm.startswith(mq+' ') or nm==mq: t=nm
            else: t=mq+' '+nm
            if norm(t) in seen: continue
            seen.add(norm(t))
            items.append((t,mq,code,y,key))
# groups for folding
base_items={}; folds=collections.OrderedDict()
for t,mq,code,y,key in items:
    f=fold(t)
    if f: folds.setdefault((f[0],mq),[]).append((t,f[1],y,code,key))
    else: base_items[norm(t)]=(t,mq,code,y,key)
newentries=collections.OrderedDict()  # norm -> (kind,entry)
def own_of(key): 
    o=D[key]; return o
pickups=[]
def add(t,mq,code,y,key,fl=None):
    if code in 'IJ': pickups.append(f'{t} ({mq})'); return None
    if code not in KIND: return None
    own,cty,oy,tier,_=D[key]
    e={'n':t,'a':'','d':'','mk':mq,'y':y,'s':wurl(t),'v':[],'g':mq,'own':own,'tier':tier,'cty':cty}
    if oy: e['own_y']=oy
    return e
tgt={}
for nk,(t,mq,code,y,key) in base_items.items():
    if nk in byname:
        kn,x=byname[nk]; tgt[nk]=(kn,x,False); continue
    e=add(t,mq,code,y,key)
    if e: newentries[nk]=(KIND[code],e); tgt[nk]=(KIND[code],e,True)
for (base,mq),lst in folds.items():
    nk=norm(base)
    if nk not in tgt and nk in byname:
        kn,x=byname[nk]; tgt[nk]=(kn,x,False)
    if nk not in tgt:
        t0,vn0,y0,code0,key0=lst[0]
        e=add(base,mq,code0,'',key0)
        if not e: continue
        e['s']=wurl(t0); e['note_base']=True
        newentries[nk]=(KIND[code0],e); tgt[nk]=(KIND[code0],e,True)
    kn,e,isnew=tgt[nk]
    have={norm(v['n']) for v in e.get('v',[])}
    for t,vn,y,code,key in lst:
        short=t[len(mq)+1:] if t.startswith(mq+' ') else t
        if norm(short) in have or norm(vn) in have: continue
        e.setdefault('v',[]).append({'n':short,'mk':mq,'y':y,'d':''}); have.add(norm(short))
# loose m -> entries or removal
for kn,k in kinds.items():
    for mm in k.get('m',[]) or []:
        nm=norm(mm[1]+' '+mm[0]) 
        if nm in byname or nm in newentries: continue
        dropped_m.append(f'{mm[1]} {mm[0]} ({kn})')
    k.pop('m',None)
# insert
for nk,(kn,e) in newentries.items():
    e.pop('note_base',None)
    if not e['a']: e.pop('a')
    if not e['d']: e.pop('d')
    kinds[kn].setdefault('x',[]).append(e)
# decorate existing
ownmap={}
for key,(own,cty,oy,tier,_) in D.items(): ownmap.setdefault(key.split('#')[0],(own,cty,oy,tier))
EXTRA={'Lancia':('Stellantis','Italy','','Global group'),'Maybach':('Mercedes-Benz Group','Germany','','Global group'),'Mercedes-Maybach':('Mercedes-Benz Group','Germany','','Global group'),'Smart':('Smart Automobile','Germany','','Global group'),'Ram':('Stellantis','United States','','Global group'),'McLaren':('McLaren Group','United Kingdom','','Independent'),'Pagani':('Pagani Automobili','Italy','','Craft & indie'),'Koenigsegg':('Koenigsegg Automotive','Sweden','','Craft & indie'),'Morgan':('Morgan Motor Company','United Kingdom','','Craft & indie'),'Caterham':('Caterham Cars','United Kingdom','','Craft & indie'),'Lada':('AvtoVAZ','Russia','','National champion'),'Isuzu':('Isuzu Motors','Japan','','Independent'),'Saab':('Defunct (Saab Automobile)','Sweden','','Independent'),'Pontiac':('Defunct (General Motors)','United States','','Independent'),'Plymouth':('Defunct (Chrysler)','United States','','Independent'),'Iso':('Defunct (Iso Rivolta)','Italy','','Independent'),'Autozam':('Defunct (Mazda)','Japan','','Independent'),'BMC':('Defunct (British Motor Corporation)','United Kingdom','','Independent'),'Messerschmitt':('Defunct (Messerschmitt)','Germany','','Independent'),'Reliant':('Defunct (Reliant Motor Company)','United Kingdom','','Independent'),'Westfield':('Westfield Sportscars','United Kingdom','','Craft & indie'),'Ultima Sports':('Ultima Sports','United Kingdom','','Craft & indie'),'Radical Sportscars':('Radical Sportscars','United Kingdom','','Craft & indie'),'Factory Five Racing':('Factory Five Racing','United States','','Craft & indie'),'Vanderhall':('Vanderhall Motor Works','United States','','Craft & indie'),'Willys':('Defunct (Willys-Overland)','United States','','Independent'),'Zagato':('Zagato','Italy','','Craft & indie'),'Pininfarina':('Pininfarina','Italy','','Craft & indie'),'Vignale':('Defunct (Ford)','Italy','','Independent'),'Ghia':('Defunct (Ford)','Italy','','Independent'),'Bond':('Defunct (Bond Cars)','United Kingdom','','Independent'),'Campagna':('Campagna Motors','Canada','','Craft & indie'),'Peel Engineering Company':('Peel Engineering Company','United Kingdom','','Craft & indie'),'Léon Bollée':('Defunct (Léon Bollée)','France','','Independent'),'Sterling':('Defunct (Sterling Cars)','United Kingdom','','Independent'),'Carrozzeria Touring Superleggera':('Carrozzeria Touring Superleggera','Italy','','Craft & indie'),'Mulliner Park Ward':('BMW Group','United Kingdom','','Global group')}
for _k,_v in EXTRA.items(): ownmap.setdefault(_k,_v)
unmapped=set()
for kn,k in kinds.items():
    for x in k.get('x',[]):
        x.pop('_mk',None)
        mk=x.get('mk','')
        x.setdefault('g',mk or 'Unattributed')
        if mk in ownmap and 'own' not in x:
            o=ownmap[mk]; x['own'],x['cty'],x['tier']=o[0],o[1],o[3]
            if o[2]: x['own_y']=o[2]
        elif 'own' not in x and mk: unmapped.add(mk)
# existing pickups
oldpick=[x['n'] for x in kinds['Pickup truck'].get('x',[])]
for k in ('Pickup truck',): pass
# remove Pickup truck kind
for sh in cars['s']:
    sh['k']=[k for k in sh['k'] if k['n']!='Pickup truck']
# per-kind fields, sorting
tot=0
for kn,k in kinds.items():
    if kn=='Pickup truck': continue
    xs=k.get('x',[])
    if not xs: continue
    xs.sort(key=lambda x:(norm(x['g']),yr(x.get('y')),x['n']))
    n=len(xs); tot+=n
    k['nl']='One entry is a production road car model sold to the public under its marque (Volkswagen Golf, Toyota Corolla, Ford Mustang); generations such as Mk1 to Mk8 or E30 are versions.'
    k['sel']=('Models of every marque read so far, from Wikipedia per-marque vehicle categories and Wikidata automobile models with an English Wikipedia article (fetched 2026-10-31), placed by body type or class; concept cars, race-only cars, vans, trucks and pickups are out. '
      f'Covers {n} entries here, part of about 7,585 automobile models with an English Wikipedia article in Wikidata; marques not yet read are listed in the report.')
    k['xg']='by marque'
kinds['Utility coupé']['sel']='Pickups and car-derived utilities are held in the Commercial part (kind Utility pickup); no entries are kept here.'
kinds['Utility coupé']['nl']='Kind kept as a pointer; car-derived pickups are named entries in Utility pickup.'
cars['note']='By body style, with generations as versions; entries carry their marque (xg by marque) and current owner group, so the same models can be read by marque or by group.'
cars['ms']=[
 {"mkt":"Europe (EU, EFTA, UK) new-car registrations","who":"Volkswagen Group","share":"26.3 %","yr":2024,"s":"https://www.best-selling-cars.com/europe/2024-full-year-europe-best-selling-car-manufacturers-and-brands","note":"3,407,242 registrations, ACEA data as reported by the page"},
 {"mkt":"Europe (EU, EFTA, UK) new-car registrations","who":"Stellantis","share":"15.2 %","yr":2024,"s":"https://www.best-selling-cars.com/europe/2024-full-year-europe-best-selling-car-manufacturers-and-brands","note":"1,969,594 registrations"},
 {"mkt":"Europe (EU, EFTA, UK) new-car registrations","who":"Renault Group","share":"9.9 %","yr":2024,"s":"https://www.best-selling-cars.com/europe/2024-full-year-europe-best-selling-car-manufacturers-and-brands","note":"1,282,453 registrations"},
 {"mkt":"Europe (EU, EFTA, UK) new-car registrations","who":"Hyundai Group","share":"8.2 %","yr":2024,"s":"https://www.best-selling-cars.com/europe/2024-full-year-europe-best-selling-car-manufacturers-and-brands","note":"1,063,517 registrations"},
 {"mkt":"Europe (EU, EFTA, UK) new-car registrations","who":"Toyota Group","share":"7.8 %","yr":2024,"s":"https://www.best-selling-cars.com/europe/2024-full-year-europe-best-selling-car-manufacturers-and-brands","note":"1,006,073 registrations"},
 {"mkt":"Europe (EU, EFTA, UK) new-car registrations","who":"BMW Group","share":"7.1 %","yr":2024,"s":"https://www.best-selling-cars.com/europe/2024-full-year-europe-best-selling-car-manufacturers-and-brands","note":"923,202 registrations"},
 {"mkt":"Europe (EU, EFTA, UK) new-car registrations","who":"Mercedes-Benz","share":"5.4 %","yr":2024,"s":"https://www.best-selling-cars.com/europe/2024-full-year-europe-best-selling-car-manufacturers-and-brands","note":"696,907 registrations"},
 {"mkt":"Europe (EU, EFTA, UK) new-car registrations","who":"Tesla","share":"2.5 %","yr":2024,"s":"https://www.best-selling-cars.com/europe/2024-full-year-europe-best-selling-car-manufacturers-and-brands","note":"327,034 registrations"},
 {"mkt":"Europe (EU, EFTA, UK) new-car registrations","who":"SAIC Motor","share":"1.9 %","yr":2024,"s":"https://www.best-selling-cars.com/europe/2024-full-year-europe-best-selling-car-manufacturers-and-brands","note":"244,595 registrations"},
 {"mkt":"Japan new-vehicle registrations","who":"Toyota","share":"30.66 %","yr":2024,"s":"https://www.best-selling-cars.com/japan/2024-full-year-japan-best-selling-carmakers-brands-and-market-analysis/","note":"1,355,581 of 4,421,494 registrations; share worked out from the page's figures"},
 {"mkt":"Japan new-vehicle registrations","who":"Suzuki","share":"16.32 %","yr":2024,"s":"https://www.best-selling-cars.com/japan/2024-full-year-japan-best-selling-carmakers-brands-and-market-analysis/","note":"721,785 registrations; share worked out from the page's figures"},
 {"mkt":"Japan new-vehicle registrations","who":"Honda","share":"15.12 %","yr":2024,"s":"https://www.best-selling-cars.com/japan/2024-full-year-japan-best-selling-carmakers-brands-and-market-analysis/","note":"668,414 registrations; share worked out from the page's figures"},
 {"mkt":"Japan new-vehicle registrations","who":"Nissan","share":"10.76 %","yr":2024,"s":"https://www.best-selling-cars.com/japan/2024-full-year-japan-best-selling-carmakers-brands-and-market-analysis/","note":"475,569 registrations; share worked out from the page's figures"},
 {"mkt":"Japan new-vehicle registrations","who":"Daihatsu","share":"8.29 %","yr":2024,"s":"https://www.best-selling-cars.com/japan/2024-full-year-japan-best-selling-carmakers-brands-and-market-analysis/","note":"366,635 registrations; share worked out from the page's figures"},
 {"mkt":"China domestic new-car market","who":"Chinese carmakers (all brands together)","share":"65 %","yr":2024,"s":"https://www.best-selling-cars.com/china/2024-full-year-china-car-production-and-exports-by-brand/","note":"market of about 31.44 million vehicles, as the page states"}]
cars['msum']='Europe and Japan figures are 2024 registrations from best-selling-cars.com; the page gives China only as a combined share for Chinese brands. Global, US and India group shares were not found on a fetched page.'
# brands
newb=[];bu={}
for mq,(own,cty,oy,tier) in ownmap.items():
    if mq in brands_old:
        bu[mq]={'own':own,'tier':tier,'c':cty}
    else:
        newb.append({'n':mq,'c':cty,'seg':'Mainstream','d':'','s':'https://en.wikipedia.org/wiki/Category:'+urllib.parse.quote(mq.replace(' ','_')+'_vehicles')})
for o in {v[0] for v in ownmap.values()}:
    if o not in brands_old and o not in {b['n'] for b in newb} and o not in ownmap:
        newb.append({'n':o,'c':'','seg':'Group','d':'','s':''})
part={'replaces':['Cars'],'depts':[cars],'brands':newb,'brand_updates':bu,'renames':{'Pickup truck':'Utility pickup'},'moves':[]}
json.dump(part,open(R+'out/G1_parts/CARS.json','w'),ensure_ascii=False)
json.dump({'pickups_new':pickups,'pickups_old':oldpick,'dropped_m':dropped_m,'unmapped_mk':sorted(unmapped),'total':tot},open(R+'work/V4_G1_CARS/summary.json','w'),ensure_ascii=False,indent=1)
print(tot,len(newb),len(bu),len(pickups),len(oldpick),len(dropped_m),sorted(unmapped))
