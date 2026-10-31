import json,re
W='/home/user/Possession-Taxonomy/rebuild/work/CARS_ADD_EUROPE/'
norm=lambda s:re.sub(r'[^a-z0-9]','',s.lower())
base=json.load(open(W+'EUROPE_r1.json',encoding='utf-8'))
cars=json.load(open('/home/user/Possession-Taxonomy/rebuild/out/G1_parts/CARS.json',encoding='utf-8'))
stored={}  # existing entries by norm name
for s in cars['depts'][0]['s']:
    for k in s['k']:
        for e in k.get('x',[]): stored[norm(e['n'])]=e
NS='Car, body style not stated'
ents={}  # norm -> (kind, entry)
for kind,v in base['kinds'].items():
    for e in v: ents[norm(e['n'])]=[kind,e]
KW=[('hatchback','Hatchback'),('liftback','Hatchback'),('saloon','Saloon'),('sedan','Saloon'),('station wagon','Estate'),('estate','Estate'),('wagon','Estate'),('shooting brake','Estate'),('suv','SUV'),('crossover','SUV'),('mpv','MPV'),('minivan','MPV'),('coupé','Coupé'),('coupe','Coupé'),('convertible','Convertible'),('cabriolet','Convertible'),('roadster','Roadster'),('speedster','Roadster'),('sports car','Sports car'),('supercar','Supercar'),('grand tourer','Grand tourer'),('city car','City car'),('limousine','Limousine'),('microcar','Microcar'),('quadricycle','Microcar'),('three-wheel','Three-wheeled car'),('off-road','Off-roader')]
def kind_of(c):
    c=c.lower(); best=None
    for kw,k in KW:
        i=c.find(kw)
        if i>=0 and (best is None or i<best[0]): best=(i,k)
    return best[1] if best else None
FACT={}
for m,d in base['brand_updates'].items(): FACT[m]=d
extra={'Volkswagen':('Germany','Volkswagen Group',''),'Audi':('Germany','Volkswagen Group',''),'Porsche':('Germany','Volkswagen Group',''),'BMW':('Germany','',''),'Mercedes-Benz':('Germany','',''),'Renault':('France','',''),'Citroën':('France','Stellantis',''),'SEAT':('Spain','Volkswagen Group','1986'),'Rolls-Royce':('United Kingdom','BMW',''),'Aston Martin':('United Kingdom','Aston Martin Lagonda',''),'Alpina':('Germany','BMW',''),'Bentley':('United Kingdom','Volkswagen Group','1998'),'Land Rover':('United Kingdom','Tata Motors Limited','2008'),'Jaguar':('United Kingdom','Tata Motors Limited','2008'),'Borgward':('Germany','',''),'Rover':('United Kingdom','',''),'Cupra':('Spain','','')}
GLOBAL={'Stellantis','Volkswagen','Volkswagen Group','Geely','Tata Motors Limited','SAIC Motor','Mercedes-Benz Group; Geely','Renault','Audi AG','Mercedes-Benz Group','BMW'}
for m,(c,o,y) in extra.items():
    d={'c':c}
    if o: d['own']=o; d['tier']='Global group' if o in GLOBAL else 'Independent'
    if y: d['own_y']=y
    FACT.setdefault(m,d)
base['brand_updates']=FACT
yup={}; added=0; moved=0
for l in open(W+'lists_r2.txt',encoding='utf-8'):
    l=l.rstrip('\n')
    if l.startswith('#'):
        mk,url=l[1:].split('|',1); continue
    if not l.strip(): continue
    p=l.split('|'); g=p[0]; n=p[1].strip(); y=p[2].strip() if len(p)>2 else ''; c=p[3].strip() if len(p)>3 else ''
    if not re.fullmatch(r'\d{4}',y): y=''
    if not n.startswith(g) and g not in('Cupra',): n=g+' '+n
    k=norm(n)
    kd=kind_of(c)
    if k in stored:
        e=stored[k]
        if y and not e.get('y'): yup[e.get('g',g)+'|'+e['n']]=y
        continue
    if k in ents:
        kind,e=ents[k]
        if y and not e['y']: e['y']=y
        if kind==NS and kd: 
            ents[k][0]=kd; moved+=1
        continue
    e={'n':n,'mk':g,'y':y,'s':url,'v':[],'g':g}
    f=FACT.get(g)
    if f:
        e['cty']=f['c']
        if f.get('own'): e['own']=f['own']; e['tier']=f['tier']
        if f.get('own_y'): e['own_y']=f['own_y']
    ents[k]=[kd or NS,e]; added+=1
kinds={}
for k,(kind,e) in ents.items(): kinds.setdefault(kind,[]).append(e)
for k in kinds: kinds[k].sort(key=lambda e:(e['g'],e['y'] or '9999',e['n']))
base['kinds']=kinds
base['y_updates']=yup
base['brands']=sorted([{'n':m,'c':d['c']} for m,d in FACT.items()],key=lambda x:x['n'])
json.dump(base,open('/home/user/Possession-Taxonomy/rebuild/out/G1_parts/cars_add/EUROPE.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('added',added,'moved',moved,'yup',len(yup),{k:len(v) for k,v in kinds.items()},sum(len(v) for v in kinds.values()))
import collections
print(collections.Counter(e['g'] for v in kinds.values() for e in v).most_common(15))
