import json,re,urllib.parse,os,collections,copy
W='/home/user/Possession-Taxonomy/rebuild/work/V4_G1_MOTO/'
OUT='/home/user/Possession-Taxonomy/rebuild/out/'
WP='https://en.wikipedia.org/wiki/'
def alnum(s): return re.sub(r'[^a-z0-9]','',s.lower())
# ---------- marque table
MQ={}
for l in open(W+'marques.txt'):
    p=l.rstrip('\n').split('|')
    if len(p)==4 and p[1]!='x': MQ[p[0]]=(p[1],p[2],p[3])
DEFUNCT={'AJS':'United Kingdom','Matchless':'United Kingdom','Ariel':'United Kingdom','BSA':'United Kingdom','Douglas':'United Kingdom','Greeves':'United Kingdom','James':'United Kingdom','Velocette':'United Kingdom','Vincent':'United Kingdom','Laverda':'Italy','DKW':'Germany','NSU':'Germany','Zündapp':'Germany','Kreidler':'Germany','Horex':'Germany','Hercules':'Germany','Excelsior':'United Kingdom','FN':'Belgium','Ascot-Pullin':'United Kingdom','Hesketh':'United Kingdom','Scott':'United Kingdom','Sunbeam':'United Kingdom','Panther':'United Kingdom','Brough':'United Kingdom','Malaguti':'Italy','Motobécane':'France','Sokół':'Poland','SHL':'Poland','Csepel':'Hungary','Riga':'Latvia','Pope':'United States','Pierce-Arrow':'United States','Thomas':'United States','Curtiss':'United States','Alligator':'United States','Daimler':'Germany','Aero':'Japan','Paton':'Italy','Condor':'Switzerland','Welbike':'United Kingdom','Mondial':'Italy','Elf':'France','Podolsk':'USSR','Tula':'USSR','Subaru':'Japan','Ilmor':'United Kingdom'}
CTY_OTHER={'Aston Martin':'United Kingdom','Mondial':'Turkey','Petronas':'Malaysia','Sachs':'Germany','Subaru':'Japan','Boss Hoss Cycles':'United States','Husqvarna':'Sweden','Modenas':'Malaysia','Yadea':'China','Johammer':'Austria','Horex':'Germany','Mahindra':'India','Sokół':'Poland','Podolsk':'USSR','Allen Millyard':'United Kingdom','Krauser':'Germany','Suter':'Switzerland','Gelbke':'United States'}
def mq(m):
    if m in MQ: return MQ[m]
    if m in DEFUNCT: return ('None (marque defunct)','Independent',DEFUNCT[m])
    return ('owner not stated','Independent',CTY_OTHER.get(m,''))
RAW={'BMW':'BMW Motorrad','Honda Racing Corporation':'Honda','Kawasaki Heavy Industries':'Kawasaki','Kawasaki Motors':'Kawasaki','Suzuki Motor Corporation':'Suzuki','Suzuki Motorcycle India Limited':'Suzuki','Yamaha Motor Company':'Yamaha','Yamaha Factory Racing':'Yamaha','MBK':'Yamaha','Triumph Motorcycles Ltd':'Triumph','Triumph Motorcycles':'Triumph','Birmingham Small Arms Company':'BSA','KR Motors':'Hyosung','Kwang Yang Motor':'Kymco','Royal Enfield India':'Royal Enfield','Indian Motorcycle':'Indian','Innocenti':'Lambretta','IMZ-Ural':'Dnepr','Dux Factory':'Dnepr','Krasny Oktyabr':'Dnepr','Kyiv Motorcycle Plant':'Dnepr','Aermacchi':'Harley-Davidson','Ariel Motorcycles':'Ariel','Ariel Motor Company':'Ariel','Ascot Motor & Manufacturing Company, Limited':'Ascot-Pullin','Associated Motor Cycles':'AMC','Aston Martin Lagonda':'Aston Martin','Auto Union':'DKW','Bajaj Auto':'Bajaj','Britten Motorcycle Company':'Britten','Buell Motorcycle Company':'Buell','CF MOTO':'CFMoto','Can-Am motorcycles':'Can-Am','Energica Motor Company':'Energica','Excelsior Motor Company':'Excelsior','Gottlieb Daimler':'Daimler','Wilhelm Maybach':'Daimler','Hesketh Motorcycles':'Hesketh','Husqvarna Motorcycles':'Husqvarna Motorcycles','Husqvarna':'Husqvarna Motorcycles','Lohia Machinery Limited':'LML','LML':'LML','Mahindra & Mahindra':'Mahindra','Malaguti':'Malaguti','Marine Turbine Technologies':'MTT','MTT':'MTT','Motobécane':'Motobécane','MotoTrans':'Ducati','NSU Motorenwerke':'NSU','Norton Motorcycle Company':'Norton','PGO Scooters':'PGO','Peugeot Motocycles':'Peugeot','Phelon & Moore':'Panther','Państwowe Zakłady Inżynierii':'Sokół','Podolsk Mechanical Plant':'Podolsk','Rikuo Motorcycle':'Rikuo','Royal Enfield India':'Royal Enfield','Sarkanā zvaigzne':'Riga','Subaru Corporation':'Subaru','Sunbeam (motorcycle)':'Sunbeam','The Scott Motorcycle Company':'Scott','Thomas Motor Company':'Thomas','Triumph Motorcycles Ltd':'Triumph','TVS Motor Company':'TVS','Tulamashzavod':'Tula','Vespa':'Vespa','Vincent Motorcycles':'Vincent','Yamaha Motor Company':'Yamaha','Zero Motorcycles':'Zero','Zündapp':'Zündapp','Pope Manufacturing Company':'Pope','Pierce-Arrow':'Pierce-Arrow','Teiyū Ichiryūsai':'Honda','Manfred Weiss Works':'Csepel','James Cycle Co':'James','Innocenti':'Lambretta','KSR Group':'Lambretta','Kreidler':'Kreidler','LiveWire':'LiveWire','Elf Aquitaine':'Elf','Glenn Curtiss':'Curtiss','Curtiss':'Curtiss','Sunbeam':'Sunbeam','Sarkanā zvaigzne':'Riga','Wild Bill Gelbke':'Gelbke','Allen Millyard':'Allen Millyard'}
PREF=[('Hero Honda','Hero MotoCorp'),('Hero','Hero MotoCorp'),('Harley-Davidson','Harley-Davidson'),('Harley Davidson','Harley-Davidson'),('LiveWire','LiveWire'),('Royal Enfield','Royal Enfield'),('Moto Guzzi','Moto Guzzi'),('Moto Morini','Moto Morini'),('MV Agusta','MV Agusta'),('Brough Superior','Brough Superior'),('BRP Can-Am','Can-Am'),('Can-Am','Can-Am'),('Piaggio Vespa','Vespa'),('Piaggio','Piaggio'),('Vespa','Vespa'),('Lambretta','Lambretta'),('Gilera','Gilera'),('Aprilia','Aprilia'),('Ducati','Ducati'),('Honda','Honda'),('Yamaha','Yamaha'),('Suzuki','Suzuki'),('Kawasaki','Kawasaki'),('BMW','BMW Motorrad'),('KTM','KTM'),('Husqvarna','Husqvarna Motorcycles'),('Triumph','Triumph'),('Norton','Norton'),('BSA','BSA'),('AJS','AJS'),('Matchless','Matchless'),('Ariel','Ariel'),('Velocette','Velocette'),('Vincent','Vincent'),('Laverda','Laverda'),('Benelli','Benelli'),('Bimota','Bimota'),('Greeves','Greeves'),('Douglas','Douglas'),('Indian','Indian'),('Buell','Buell'),('Cagiva','Cagiva'),('Kymco','Kymco'),('Hyosung','Hyosung'),('CFMoto','CFMoto'),('Keeway','Keeway'),('MZ','MZ'),('DKW','DKW'),('NSU','NSU'),('Zündapp','Zündapp'),('TVS','TVS'),('Bajaj','Bajaj'),('Mahindra','Mahindra'),('Malaguti','Malaguti'),('Derbi','Derbi'),('Energica','Energica'),('Zero ','Zero'),('Sachs','Sachs'),('Kreidler','Kreidler'),('Peugeot','Peugeot'),('Jawa','Jawa'),('Dnepr','Dnepr'),('Velocette','Velocette'),('Panther','Panther'),('Scott','Scott'),('Sunbeam','Sunbeam'),('Curtiss','Curtiss'),('Excelsior','Excelsior'),('Hesketh','Hesketh'),('Horex','Horex'),('Hercules','Hercules'),('FN ','FN'),('James','James'),('Condor','Condor'),('Petronas','Petronas'),('Paton','Paton'),('Mondial','Mondial'),('Aston Martin','Aston Martin'),('Modenas','Modenas'),('Moriwaki','Moriwaki'),('Britten','Britten'),('Pope','Pope'),('Thomas','Thomas'),('Boss Hoss','Boss Hoss Cycles'),('SYM','SYM'),('PGO','PGO'),('Genuine','PGO'),('Csepel','Csepel'),('Riga','Riga'),('Yadea','Yadea'),('Johammer','Johammer'),('Suter','Suter'),('Krauser','Krauser'),('Millyard','Allen Millyard'),('Ilmor','Ilmor'),('Ascot','Ascot-Pullin'),('Welbike','Welbike'),('ELF','Elf'),('Tula','Tula'),('Muravey','Tula'),('Sokół','Sokół'),('SHL','SHL'),('PMZ','Podolsk'),('Fuji','Subaru'),('Daimler','Daimler'),('Type 97','Rikuo'),('Kettenkrad','NSU'),('Auto Four','Gelbke'),('Roadog','Gelbke'),('Pierce','Pierce-Arrow'),('Auto-Bi','Thomas'),('LML','LML'),('Rajdoot','Yamaha'),('Tenere','Yamaha'),('Mobylette','Motobécane'),('Slippery Sam','Triumph'),('Castrol Rocket','Triumph'),('BRP','Can-Am'),('Silver Streak','Matchless'),('Krauser','Krauser'),('MTT','MTT'),('Softail','Harley-Davidson'),('Scarabeo','Aprilia'),('Hunter','Hunter Motorcycles'),('Kawasaki','Kawasaki')]
def marque_of(name,raw):
    for p,m in PREF:
        if name.startswith(p) : return m
    if raw: return RAW.get(raw,raw)
    return 'Other marques'
EXCL=re.compile(r'^(list of|star motorcycles|puma motorcycles|triton motorcycle|side-by-side|boda boda|bmw 247 engine|n100 plan|kawasaki police|concept|silver bird|crosscage|stratosphere|recursion|biplane|g-strider|nuda$|skywave type|address v50g|lc4 engine)',re.I)
def norm_key(name,marque):
    k=alnum(name)
    for pre in {alnum(marque),alnum(marque.replace(' Motorrad','')),'harleydavidson','bmw','herohonda','hero','piaggio','vespa','royalenfield','ktm','honda','yamaha','suzuki','kawasaki','triumph','ducati'}:
        if pre and k.startswith(pre) and len(k)>len(pre)+1: k=k[len(pre):]; break
    k=re.sub(r'(motorcycles|motorcycle|series|model)$','',k)
    return k
def quote_title(t): return urllib.parse.quote(t,safe="/_()-,.'!&:~%")
SC=re.compile(r"\b(vespa|lambretta|scoopy|spacy|dio|activa|aviator|grazia|pcx|nmax|xmax|tmax|tricity|burgman|skywave|jog|aerox|majesty|cygnus|mio|nouvo|ntorq|wego|scooty|chetak|jupiter|zuma|vino|fazzio|metropolis|tweet|ludix|speedfight|vivacity|kisbee|django|citystar|looxor|elystar|satelis|liberty|medley|beverly|mp3|x7|x8|x9|x10|ciao|buddy|vario|click|airblade|forza|silver wing|ruckus|zoomer|elite|metropolitan|cliq|genio|stylo|navi|helix|reflex|dylan|foresight|pantheon|cub|monkey|dax|mobylette|solex|quickly|schwalbe|moped|chaly|motocompo|grom|riga|muravey|pleasure|maestro|destini|xoom|duet|address|access 125|let's|sepia|choinori|people|downtown|agility|xciting|filano|nozza|lexi|fino|passol|neo's|epsilon|c ?400|c ?600|c ?650|c evolution|ce ?0[24]|ct ?\d+|z50\w*|ape|express|pop 110i|sh ?\d+|spree|motra|welbike|scooter|kymco|sym|pgo|autocycle|ap?\d|fantic)\b",re.I)
SC_SEC={'Step-throughs, scooters, underbones','Maxi-scooters','Electric','Scooters','Scooter','Three-wheelers'}
# ---------- gather sources
cands=[]  # dict: name,y,mk(raw marque canon),s,srcrank,sec
def add(name,y,maq,s,rank,sec='',own_y=None):
    name=name.strip()
    if not name or EXCL.search(name): return
    cands.append(dict(n=name,y=y,m=maq,s=s,r=rank,sec=sec))
def wd(fn,fmt):
    mk=''
    for l in open(W+fn):
        l=l.rstrip('\n')
        if l.startswith('## '): mk=l[3:]; continue
        p=l.split('|')
        if fmt==4:
            name,y,raw,t=p[0],p[1],p[2],p[3]; mk=raw
        else:
            name,y,t=p[0],p[1],p[2]
        if t=='=' : t=name.replace(' ','_')
        t=t.replace('%C3%A9','é') if False else t
        m=marque_of(name,'' if mk in('none','') else mk)
        if m=='Other marques' and mk: m=RAW.get(mk,mk)
        if m=='AMC': m='AJS' if name.startswith('AJS') else ('Matchless' if name.startswith('Matchless') else 'AMC')
        add(name,y,m,WP+quote_title(t) if not t.startswith('http') else t,2)
for f,fm in (('wd0.txt',4),('wd1.txt',4)): wd(f,4)
for f in ('wd2.txt','wd3.txt','wd4.txt','wd5.txt','wd6.txt'): wd(f,3)
nwd=len(cands)
LISTS={'honda':('Honda','List_of_Honda_motorcycles'),'yamaha':('Yamaha','List_of_Yamaha_motorcycles'),'suzuki':('Suzuki','List_of_Suzuki_motorcycles'),'kawasaki':('Kawasaki','List_of_Kawasaki_motorcycles'),'hd':('Harley-Davidson','List_of_Harley-Davidson_motorcycles'),'re':('Royal Enfield','List_of_Royal_Enfield_motorcycles'),'triumph':('Triumph','List_of_Triumph_motorcycles'),'guzzi':('Moto Guzzi','List_of_Moto_Guzzi_motorcycles'),'norton':('Norton','List_of_Norton_motorcycles'),'bsa':('BSA','List_of_BSA_motorcycles'),'vincent':('Vincent','List_of_Vincent_motorcycles'),'velocette':('Velocette','List_of_Velocette_motorcycles'),'laverda':('Laverda','List_of_Laverda_Motorcycles'),'benelli':('Benelli','List_of_Benelli_motorcycles'),'bimota':('Bimota','List_of_Bimota_motorcycles'),'ajs':('AJS','List_of_AMC_motorcycles'),'ariel':('Ariel','List_of_Ariel_motorcycles'),'greeves':('Greeves','List_of_Greeves_motorcycles'),'james':('James','List_of_James_motorcycles'),'peugeot':('Peugeot','List_of_Peugeot_motorcycles'),'douglas':('Douglas','List_of_Douglas_motorcycles')}
YR=re.compile(r'\s*\((\d{4}[^)]*)\)\s*$')
def wplist(key,fn):
    mq_,page=LISTS[key]
    src=WP+page
    sec=''
    for l in open(W+fn):
        l=l.strip()
        if l.startswith('@'): sec=l[1:].split('|')[0]; continue
        if key=='honda':
            names=[l.split('|')[0]]
        else: names=l.split(';')
        for n in names:
            n=n.strip(); y=''
            m=YR.search(n)
            if m: y=m.group(1); n=YR.sub('',n).strip()
            if not n: continue
            if key=='hd' or True:
                pass
            sm=mq_
            if key=='ajs':
                sm='AJS' if sec=='AJS' else 'Matchless'
            full=n
            if not alnum(n).startswith(alnum(sm)) and not (sm=='BMW Motorrad' and n.startswith('BMW')):
                pre={'Harley-Davidson':'Harley-Davidson','Moto Guzzi':'Moto Guzzi'}.get(sm,sm)
                full=pre+' '+n
            y=y.replace('–)','–').strip()
            add(full,y,sm,src,3,sec)
for k,f in (('honda','wp_honda.txt'),('yamaha','wp_yamaha.txt'),('suzuki','wp_suzuki.txt'),('kawasaki','wp_kawasaki.txt'),('hd','wp_hd.txt'),('re','wp_re.txt'),('triumph','wp_triumph.txt'),('guzzi','wp_guzzi.txt'),('norton','wp_norton.txt'),('bsa','wp_bsa.txt'),('vincent','wp_vincent.txt'),('velocette','wp_velocette.txt'),('laverda','wp_laverda.txt'),('benelli','wp_benelli.txt'),('bimota','wp_bimota.txt'),('ajs','wp_ajs.txt'),('ariel','wp_ariel.txt'),('greeves','wp_greeves.txt'),('james','wp_james.txt'),('peugeot','wp_peugeot.txt'),('douglas','wp_douglas.txt')): wplist(k,f)
# india/ktm lists
INDIA={'Bajaj':('Bajaj','Bajaj_Auto'),'KTM':('KTM','Category:KTM_motorcycles'),'Hero':('Hero MotoCorp','Hero_MotoCorp'),'TVS':('TVS','TVS_Motor_Company')}
sec=''
for l in open(W+'wp_india.txt'):
    l=l.strip()
    if l.startswith('@'): sec=l[1:].split('|')[0]; continue
    mq_,page=INDIA[sec]
    for n in l.split(';'):
        n=n.strip()
        if not n: continue
        pre={'Bajaj':'Bajaj','KTM':'KTM','Hero MotoCorp':'Hero','TVS':'TVS'}[mq_]
        full=n if n.lower().startswith(pre.lower()) else pre+' '+n
        add(full,'',mq_,WP+page,3,'')
# ---------- existing curated entries
old=json.load(open(OUT+'G1.json'))
dept=[d for d in old['depts'] if d['n']=='Motorcycles & scooters'][0]
gear=[d for d in old['depts'] if d['n']=='Motorcycle riding gear'][0]
MKMAP={'Yamaha Motor':'Yamaha','BMW':'BMW Motorrad','Husqvarna':'Husqvarna Motorcycles','Triumph Motorcycles':'Triumph','Bajaj Auto':'Bajaj'}
cur=[]  # (oldkind, entry)
KEEPKINDS=('Trike','Motorcycle with sidecar')
mapkind={}
for s in dept['s']:
    for k in s['k']:
        if k['n'] in ('Scooter','Moped','Underbone motorcycle','Mini bike'): nk='Scooter, moped and cub'
        elif s['n'] in ('Road motorcycles','Retro & custom styles','Off-road motorcycles'): nk='Motorcycle'
        else: nk=k['n']
        mapkind[k['n']]=nk
curexist=[]
for s in dept['s']:
    for k in s['k']:
        nk=mapkind[k['n']]
        for x in k.get('x',[]):
            curexist.append((k['n'],nk,x))
# ---------- dedupe: priority existing, then wikidata(2), then lists(3)
cmap={}
def getm(x):
    mk=x.get('mk','') or ''
    mk=MKMAP.get(mk,mk)
    nm=x['n']
    for p,m in PREF:
        if nm.startswith(p): return m
    return mk or 'Other marques'
entries={'Motorcycle':[], 'Scooter, moped and cub':[]}
other=collections.defaultdict(list)
seen=set()
oldmeta={}
for ok,nk,x in curexist:
    m=getm(x)
    if nk in entries:
        key=norm_key(x['n'],m)
        seen.add((m,key)); seen.add(('',key))
        e=copy.deepcopy(x); e['g']=m; e['mk']=m
        o,t,c=mq(m); e['own']=o; e['tier']=t; 
        if c: e['cty']=c
        if m=='Norton': e['own_y']='2020'
        e['dt']=(e.get('dt','')+(' · ' if e.get('dt') else '')+'type: '+ok)
        entries[nk].append(e)
    else:
        e=copy.deepcopy(x); 
        other[nk].append(e)
ncur=sum(len(v) for v in entries.values())
cands.sort(key=lambda c:c['r'])
added=collections.Counter()
for c in cands:
    m=c['m']; key=norm_key(c['n'],m)
    if (m,key) in seen: continue
    seen.add((m,key))
    kind='Scooter, moped and cub' if (c['sec'] in SC_SEC or (SC.search(c['n']) and not re.search(r'(Tiger Cub|Gold Wing)',c['n']))) else 'Motorcycle'
    o,t,cty=mq(m)
    e={'n':c['n'],'mk':m,'s':c['s'],'g':m,'own':o,'tier':t}
    if cty: e['cty']=cty
    if c['y']: e['y']=c['y']
    if m=='Norton': e['own_y']='2020'
    entries[kind].append(e); added[kind]+=1
def ykey(e):
    mm=re.search(r'\d{4}',e.get('y',''))
    return (int(mm.group()) if mm else 9999)
for k in entries:
    entries[k].sort(key=lambda e:(e['g'].lower(),ykey(e),e['n'].lower()))
marques=collections.Counter()
for k in entries:
    for e in entries[k]: marques[e['g']]+=1
# ---------- build dept
OPEN={'t':None}
def kind_rest(name): 
    for s in dept['s']:
        for k in s['k']:
            if k['n']==name: return k
tt_motor=[['Type',['Standard / naked','Sport','Cruiser','Touring','Adventure','Café racer','Scrambler','Chopper and bobber','Motocross','Enduro','Trials','Supermoto','Dual-sport','Trail','Pit bike']],['Engine',['Two-stroke','Four-stroke','Electric']],['Registration',['Road-registered','Competition only']]]
tt_sc=[['Style',['Classic scooter','Maxi-scooter','Three-wheel tilting scooter','Pedal moped','Step-through cub','Mini bike']],['Power',['Petrol','Electric']]]
see_m=[['G1','Trike','three wheels'],['G1','Motorcycle with sidecar','outfits'],['G1','Scooter, moped and cub','small step-through machines']]
see_sc=[['H2','Mobility scooter','for reduced mobility, not a motorcycle'],['G1','Motorcycle','geared motorcycles']]
ncountry=len({(e['g']) for k in entries for e in entries[k]})
WDREAD=nwd
sel_m=("Wikidata items of class motorcycle model (Q23866334) and motorcycle model series (Q71310524) or motorcycle (Q34493) with an English Wikipedia article, read in full through the query service (1,194 + 225 rows), joined with the model rows of Wikipedia's per-manufacturer lists "
 "(List of Honda, Yamaha, Suzuki, Kawasaki, Harley-Davidson, Royal Enfield, Triumph, Moto Guzzi, Norton, BSA, AMC, Ariel, Douglas, Greeves, James, Peugeot, Velocette, Vincent, Laverda, Benelli and Bimota motorcycles) and the Bajaj, KTM, Hero MotoCorp and TVS company/category pages. "
 "Sections are marques; scooters, mopeds and cubs are in the next kind. Concepts, prototypes, quads and side-by-sides are left out. "
 "Marques and countries follow Wikipedia's List of motorcycle manufacturers (read to its end). Covers %d model lines under %d marques of about 430 marque names on that page; the Honda list (engine-size table of about 350 rows) was joined only in part, the BMW, Ducati, Aprilia, Husqvarna and Indian model lists have no Wikipedia list and rest on Wikidata and the category pages, and Vespa and Lambretta generation lists were read but kept as versions of the existing entries." %(len(entries['Motorcycle']),len({e['g'] for e in entries['Motorcycle']})))
sel_s=("Same references as Motorcycle; rows are placed here when the source section is a scooter or step-through section (Yamaha, Kawasaki) or the name matches a scooter, moped or cub keyword, so placement of new rows is a rule, not a reading of each page. Covers %d model lines under %d marques."%(len(entries['Scooter, moped and cub']),len({e['g'] for e in entries['Scooter, moped and cub']})))
newshelves=[
 {'n':'Motorcycles','t':'Geared motorcycles of every type, listed by marque; a scooter, moped or cub → Scooters, mopeds & cubs; a retro-look custom built at home → Motorcycle.',
  'ax':'kinds by machine: the motorcycle model itself, with type recorded as an attribute',
  'k':[{'n':'Motorcycle','a':'motorbike · bike','d':'Two-wheeled motor vehicle with a seat and handlebars, built for road, track or dirt, named by its marque and model line.','s':'https://en.wikipedia.org/wiki/List_of_motorcycle_manufacturers','nl':'One entry is a motorcycle model line or design sold or raced under a marque name; generations, capacity variants and special editions are versions.','sel':sel_m,'xg':'by marque (alphabetical), then year','tt':tt_motor,'see':see_m,'x':entries['Motorcycle']}]},
 {'n':'Scooters, mopeds & cubs','t':'Small-engined step-through machines for short trips, listed by marque; a pedal-assisted bicycle → Electric bike.',
  'ax':'kinds by frame and engine layout, merged into one list by marque',
  'k':[{'n':'Scooter, moped and cub','a':'scooter · moped · underbone · cub · mini bike','d':'Small step-through or low-frame machine with a small engine, from Vespa scooters to Honda cubs.','s':'https://en.wikipedia.org/wiki/List_of_motor_scooter_manufacturers_and_brands','nl':'One entry is a scooter, moped, cub or mini-bike model line sold under a marque name; generations and capacity variants are versions.','sel':sel_s,'xg':'by marque (alphabetical), then year','tt':tt_sc,'see':see_sc,'x':entries['Scooter, moped and cub']}]}]
keep=[]
for s in dept['s']:
    if s['n'] in ('Three-wheelers & sidecars','Electric rides'):
        s2=copy.deepcopy(s)
        for k in s2['k']:
            k.pop('m',None)
            nl_={'Trike':'One entry is a trike model sold under a maker name; trims are versions.','Motorcycle with sidecar':'One entry is a sidecar outfit model; chassis variants are versions.'}
            if k.get('x'):
                k['nl']=nl_.get(k['n'],'One entry is a model line of this kind sold under its maker name; versions are revisions.')
                k['sel']='Entries kept from the structure pass, each sourced to its Wikipedia or maker page; no whole-space reference exists for this kind, so the list is a set of originators and best-known lines, not a canon.'
                for e in k['x']:
                    mkr=e.get('mk',''); e['g']=mkr or 'Maker not stated'
                    o,t,c=mq(MKMAP.get(mkr,mkr)); e['own']=o; e['tier']=t
                    if c: e['cty']=c
        keep.append(s2)
newdept=copy.deepcopy(dept)
newdept['s']=newshelves+keep
newdept['t']=dept['t']; newdept['ax']=dept['ax']
newdept['note']='Organised marque → model line → generation; type is an attribute. Scooter, moped and cub lines are in their own kind.'
# ms
AC='https://autocarpro.in/news/hero-motocorp-leads-fy25-2-wheeler-retail-sales-market-share-dips-125783'
ms=[]
for who,sh,vol in (('Hero MotoCorp','28.84 %','54.45 lakh units'),('Honda Motorcycle & Scooter India','25.37 %','47.89 lakh units'),('TVS Motor','17.49 %','33.02 lakh units'),('Bajaj Auto','11.41 %','21.54 lakh units'),('Royal Enfield','4.47 %','8.43 lakh units'),('Yamaha Motor India','3.44 %','6.50 lakh units')):
    ms.append({'mkt':'India two-wheelers, retail','who':who,'share':sh,'yr':2025,'s':AC,'note':'financial year 2024-25 retail volume, %s'%vol})
ms+= [
 {'mkt':'Indonesia motorcycles','who':'Honda','share':'73.8 %','yr':2016,'s':'https://databoks.katadata.co.id/en/transportation-logistics/statistics/126b46d44bcef26/honda-remains-dominant-in-domestic-motorcycle-sales','note':'4.38 million of 5.93 million units, AISI data; the newest brand split found'},
 {'mkt':'Indonesia motorcycles','who':'Yamaha','share':'23.5 %','yr':2016,'s':'https://databoks.katadata.co.id/en/transportation-logistics/statistics/126b46d44bcef26/honda-remains-dominant-in-domestic-motorcycle-sales','note':'1.39 million units; Honda and Yamaha together 97.36 %'},
 {'mkt':'Indonesia motorcycles','who':'All brands','share':'','yr':2024,'s':'https://auto.katadata.co.id/motor/new-motorcycle-sales-in-2024-reached-63-million-units-surpassing-2023-17613','note':'6,333,310 domestic units and 572,506 exports, AISI; no brand split on the page'},
 {'mkt':'India motorcycles','who':'Bajaj Auto','share':'31 %','yr':2013,'s':'https://en.wikipedia.org/wiki/Bajaj_Auto','note':'motorcycle market, financial year 2012-13; third-largest motorcycle maker in the world'},
 {'mkt':'India two-wheelers','who':'Hero MotoCorp','share':'30 %','yr':2024,'s':'https://en.wikipedia.org/wiki/Hero_MotoCorp','note':'as of March 2024, as the article states'},
 {'mkt':'United States motorcycles','who':'Harley-Davidson','share':'','yr':2023,'s':'https://en.wikipedia.org/wiki/Harley-Davidson','note':'162,771 units produced; no US market share figure was found on a fetched page'},
 {'mkt':'World motorcycles','who':'Honda','share':'','yr':None,'s':'https://global.honda/en/sustainability/integratedreport/motorcycle-business-strategy/','note':"Honda describes itself as the world's No. 1 motorcycle maker by market share, with annual global sales of around 20 million units; the page gives no year or percentage"}]
for m in ms:
    if m['yr'] is None: del m['yr']
newdept['ms']=ms
newdept['msum']="India's two-wheeler market was led by Hero MotoCorp (28.84 %) and Honda (25.37 %) in financial year 2024-25; Indonesia is a Honda and Yamaha market (97 % in 2016, 6.33 million units in 2024). No fetched page gave a world or US brand share."
# ---------- gear
newgear=copy.deepcopy(gear)
removed_models=0; removed_entries=0
brands_by_kind={}
for s in newgear['s']:
    for k in s['k']:
        nm=len(k.get('m',[])); removed_models+=nm
        xs=k.pop('x',[]) or []
        k.pop('m',None); k.pop('r',None)
        mks=[]
        for e in xs:
            if e.get('mk') and e['mk'] not in mks: mks.append(e['mk'])
        if k['n'].endswith('helmet') and mks:
            names=sorted(set(mks))
            k['tt']=(k.get('tt') or [])+[['Helmet line maker',names]]
        if k['n'] in('Full-face helmet','Modular helmet','Dual-sport helmet','Off-road helmet','Open-face helmet'):
            k['tt']=(k.get('tt') or [])+[['Safety standard',['ECE 22.06','DOT FMVSS 218','Snell M2020']]]
        removed_entries+=len(xs)
        if k['n']=='Full-face helmet':
            bs=[e for e in xs if e['n']=='Bell Star']
            if bs:
                e=bs[0]; e['role']='origin'; e['g']='Bell'; e['own']='Bell Sports'; e['tier']='Independent'; e['cty']='United States'
                k['x']=[e]
                k['nl']='One entry is the origin helmet of this kind; helmet lines and standards are attributes (tt), not entries.'
                k['sel']='Commodity kind under the icon rule: one origin entry, the first full-face motorcycle helmet, from the Bell Sports page. Helmet makers and standards are types.'
                removed_entries-=1
        for kk in list(k.keys()):
            if kk=='see' and not k['see']: k.pop('see')
newgear['note']='Commodity kinds: helmet makers and standards are types; only the origin helmet is an entry.'
part={'replaces':['Motorcycles & scooters','Motorcycle riding gear'],'depts':[newdept,newgear],'brands':[],'brand_updates':{},'renames':{k:v for k,v in mapkind.items() if v!=k},'moves':[]}
# ---------- brands
MFILE=json.load(open(OUT+'G1_brands.json'))['b']
exist={b['n'] for b in MFILE}
REG={'BMW Motorrad','Honda','Yamaha','Suzuki','Kawasaki','Harley-Davidson','Royal Enfield','Triumph','Piaggio','Vespa','Lambretta','Norton','Moto Guzzi','Gilera','Vincent','Brough Superior','Husqvarna Motorcycles','GASGAS','Ducati','KTM','Indian','Can-Am','Peugeot','Dnepr','Ural','NSU','Simson'}
LISTURL='https://en.wikipedia.org/wiki/List_of_motorcycle_manufacturers'
cnt_new=0
for m,n in marques.items():
    o,t,c=mq(m)
    if m in exist:
        part['brand_updates'][m]={'own':o,'tier':t,'c':c}
    else:
        b={'n':m,'c':c,'d':'','s':LISTURL}
        if m in('Hero MotoCorp','Bajaj','TVS'): b['s']={'Hero MotoCorp':'https://en.wikipedia.org/wiki/Hero_MotoCorp','Bajaj':'https://en.wikipedia.org/wiki/Bajaj_Auto','TVS':'https://en.wikipedia.org/wiki/TVS_Motor_Company'}[m]
        part['brands'].append(b); cnt_new+=1
# brand_updates for existing with name variants
for alt,tgt in (('BMW','BMW Motorrad'),('Yamaha Motor','Yamaha')):
    if alt in exist and tgt in marques:
        o,t,c=mq(tgt); part['brand_updates'][alt]={'own':o,'tier':t,'c':c}
for b in part['brands']:
    if b.get('d')=='': b.pop('d')
json.dump(part,open(OUT+'G1_parts/MOTO.json.tmp','w'),ensure_ascii=False)
os.replace(OUT+'G1_parts/MOTO.json.tmp',OUT+'G1_parts/MOTO.json')
print('wd cands',nwd,'total cands',len(cands),'cur',ncur,'added',dict(added),'marques',len(marques),'newbrands',cnt_new,'updates',len(part['brand_updates']))
print('gear removed models',removed_models,'entries',removed_entries)
print('size',os.path.getsize(OUT+'G1_parts/MOTO.json'))
print(marques.most_common(25))
E=None
