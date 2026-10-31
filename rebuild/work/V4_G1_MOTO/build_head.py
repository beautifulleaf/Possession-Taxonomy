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
SC=re.compile(r"\b(vespa|lambretta|scoopy|spacy|dio|activa|aviator|grazia|pcx|nmax|xmax|tmax|tricity|burgman|skywave|jog|aerox|majesty|cygnus|mio|nouvo|ntorq|wego|scooty|chetak|jupiter|zuma|vino|fazzio|metropolis|tweet|ludix|speedfight|vivacity|kisbee|django|citystar|looxor|elystar|satelis|liberty|medley|beverly|mp3|x7|x8|x9|x10|ciao|buddy|vario|click|airblade|forza|silver wing|ruckus|zoomer|elite|metropolitan|cliq|genio|stylo|navi|helix|reflex|dylan|foresight|pantheon|cub|monkey|dax|mobylette|solex|quickly|schwalbe|moped|chaly|motocompo|grom|riga|muravey|pleasure|maestro|destini|xoom|duet|address|access 125|let's|sepia|choinori|people|downtown|agility|xciting|filano|nozza|lexi|fino|passol|neo's|epsilon|c ?400|c ?600|c ?650|c evolution|ce ?0[24]|ct ?\d+|z50\w*|ape|express|pop 110i|sh ?\d+|spree|motra|welbike|scooter|kymco|sym|pgo|autocycle|fantic)\b",re.I)
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
