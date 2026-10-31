import json,os,re,urllib.parse,copy
P='/home/user/Possession-Taxonomy/rebuild/out/C3.json'
G='/home/user/Possession-Taxonomy/rebuild/work/GAP_C3/g/'
d=json.load(open(P))
def qurl(gen,cult=False):
    if not cult:
        q='SELECT DISTINCT ?l WHERE { ?g wdt:P225 "%s"; wdt:P105 wd:Q34740. ?sp wdt:P171+ ?g; wdt:P105 wd:Q7432; rdfs:label ?l. FILTER(LANG(?l)="en") ?a schema:about ?sp; schema:isPartOf <https://en.wikipedia.org/>. } ORDER BY ?l'%gen
    else:
        q='SELECT DISTINCT ?l WHERE { ?g wdt:P225 "%s". ?sp wdt:P171+ ?g. {?sp wdt:P105 wd:Q4886} UNION {?sp wdt:P31 wd:Q4886} ?sp rdfs:label ?l. FILTER(LANG(?l)="en") ?a schema:about ?sp; schema:isPartOf <https://en.wikipedia.org/>. } ORDER BY ?l'%gen
    return 'https://query.wikidata.org/sparql?format=json&query='+urllib.parse.quote(q,safe='')
def norm(s):
    s=s.lower()
    for c in "'‘’ʽ\"": s=s.replace(c,'')
    s=re.sub(r'^(rosa|malus domestica|dahlia|clematis|camellia japonica|hemerocallis|magnolia|rhododendron) ','',s)
    s=re.sub(r' (potato|pear|orange|cherry|fig|tree)$','',s)
    return s.strip()
kinds={}
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']: kinds[k['n']]=(sh,k)
sp_map={'Philodendron':'Philodendron','Anthurium':'Anthurium','Hoya':'Wax plant','Mammillaria':'Mammillaria','Echeveria':'Echeveria','Haworthia':'Haworthia','Monstera':'Monstera','Alocasia':'Alocasia','Goeppertia':'Prayer plant','Begonia':'Begonia','Pelargonium':'Pelargonium','Fuchsia':'Fuchsia','Hosta':'Hosta','Paeonia':'Peony','Hydrangea':'Hydrangea','Clematis':'Clematis','Lavandula':'Lavender','Camellia':'Camellia','Rhododendron':'Rhododendron & azalea','Magnolia':'Magnolia','Tulipa':'Tulip bulb','Narcissus':'Daffodil bulb','Iris':'Iris','Dahlia':'Dahlia tuber'}
def mk(n,s,desc):
    return {"n":n,"a":"","d":desc,"mk":"","y":"","s":s,"v":[]}
changed={}
def add(kn,ents):
    k=kinds[kn][1]; ex={norm(e['n']) for e in k['x']}
    n0=len(k['x'])
    for e in ents:
        if norm(e['n']) not in ex:
            k['x'].append(e); ex.add(norm(e['n']))
    changed[kn]=changed.get(kn,0)+len(k['x'])-n0
spcount={}
for gen,kn in sp_map.items():
    toks=open(G+gen+'.txt').read().split()
    # glue "×" tokens
    ents=[]; i=0; names=[]
    while i<len(toks):
        t=toks[i]
        if t=='×' and i+1<len(toks): t='×'+toks[i+1]; i+=1
        names.append(t); i+=1
    url=qurl(gen)
    for t in names:
        if t.startswith('×'): n='%s × %s'%(gen,t[1:]); desc='Named hybrid of the genus %s listed with an English Wikipedia article.'%gen
        elif t.startswith("'"): n='%s %s'%(gen,t); desc='Cultivar of %s listed with an English Wikipedia article.'%gen
        else: n='%s %s'%(gen,t); desc='Species of the genus %s listed with an English Wikipedia article.'%gen
        ents.append(mk(n,url,desc))
    add(kn,ents); spcount[kn]=(gen,len(names))
# cultivars
cu={'Apple tree':('Malus domestica',["Beacon","Gascoyne's Scarlet","King of the Pippins","Malinda","Mutsu","Wealthy","Aport"]),
'Pear tree':('Pyrus',["Bosc","D'Anjou"]),
'Plum tree':('Prunus',["Black Amber","Climax"]),
'Cherry tree':('Prunus',["Emperor Francis","Evans","Griotte de Kleparow","Marasca","Ulster","North Star"]),
'Peach tree':('Prunus',["Sunhigh","Sugar May"]),
'Orange tree':('Citrus',["Jaffa"]),
'Mandarin tree':('Citrus',["'Encore'"]),
'Speciality citrus':('Citrus',["Kawachi bankan"]),
'Lemon & lime tree':('Citrus',["Limone di Siracusa PGI","Variegated pink lemon"]),
'Fig tree':('Ficus',["Mission"]),
'Olive tree':('Olea',["Verdale-de-l'Hérault"]),
'Strawberry plant':('Fragaria',["Camino Real","Marshall"]),
'Seed potato':('Solanum',"Adirondack Red;Anya;Atlantic;Bintje;Black Champion;Bloomer;British Queen;Butte;Désirée;Gala;Home Guard;Irish White;Kennebec;Kerr's Pink;Laura;Marcy;Marfona;Mizen;Pike;Ratte;Skerry Champion;Stobrawa;Superior;Ulster Emblem;Vitelotte".split(';')),
'Tomato seed':('Solanum',["Aunt Ruby's German Green","Azoychka"]),
'Dahlia tuber':('Dahlia',["'Akita'","'Alfred Grille'","'Apache'","'Arabian Night'","'Babylon Bronze'","'Babylon Pink'","'Bora Bora'","'Bridge View Aloha'","'Chat Noir'","'Moonfire'","'Mrs Eileen'"]),
'Clematis':('Clematis',["'Princess Diana'"]),
'Camellia':('Camellia',["'Prince Frederick William'","'The Czar'"]),
'Daylily':('Hemerocallis',["'Duke of Durham'"]),
'Magnolia':('Magnolia',["'Butterflies'","'Elizabeth'"]),
'Rhododendron & azalea':('Rhododendron',["'President Roosevelt'"])}
for kn,(gen,names) in cu.items():
    url=qurl(gen,True)
    add(kn,[mk(n,url,'Cultivar named on an English Wikipedia article listed in Wikidata for %s.'%gen) for n in names])
# roses: new kind
rose_names=open(G+'roses.txt').read().strip().split(';')
sh=kinds['Species rose'][0]
allrose=set()
for kn in ['Hybrid tea rose','Floribunda rose','English rose','Shrub rose','Climbing rose','Rambler rose','Old garden rose','Species rose']:
    for e in kinds[kn][1]['x']: allrose.add(norm(e['n']))
url=qurl('Rosa',True)
new=[mk("'%s'"%n,url,'Rose cultivar with an English Wikipedia article; the source gives no class.') for n in rose_names if norm(n) not in allrose]
rk={"n":"Rose cultivar (class not stated)","a":"named garden rose","d":"Named garden rose cultivar whose class is not stated by the source, held here until its class is read from a rose register.",
"s":url,"tt":[["Habit",["Bush","Shrub","Climber"]]],"see":[],"x":new,
"nl":"One entry is a named rose cultivar that has an English Wikipedia article; its class (hybrid tea, floribunda, English, shrub, climber, old garden) is not stated in the source.",
"sel":""}
sh['k'].append(rk); kinds[rk['n']]=(sh,rk); changed[rk['n']]=len(new)
print('new roses',len(new))
def cls(n):
    if '×' in n or 'hybrid' in n.lower(): return 'Hybrid'
    if "'" in n or '‘' in n or 'Group' in n or 'group' in n: return 'Cultivar or group'
    if re.match(r'^[A-Z][a-z]+ [a-z-]+$',n): return 'Species'
    return 'Form or common name'
order=['Species','Hybrid','Cultivar or group','Form or common name']
for kn,(sh,k) in kinds.items():
    if not k.get('x'): continue
    n=len(k['x'])
    if kn in sp_map.values() or kn in cu or kn==rk['n']:
        pass
    if kn in spcount:
        gen,m=spcount[kn]
        k['sel']="Covers %d entries: the %d %s species, hybrids and cultivars that have an English Wikipedia article in Wikidata (queried 2026-10-31), plus items from the earlier cited pages; species without an article are not listed and no complete accepted-species register was fetched."%(n,m,gen)
    elif kn==rk['n']:
        k['sel']="Covers %d rose cultivars with an English Wikipedia article in Wikidata (queried 2026-10-31); the source states no class, so they are not placed in the class kinds. Roses already in the class kinds are not repeated."%n
    elif kn in cu:
        k['sel']="Covers %d entries named on the cited RHS and Wikipedia pages, plus cultivars with an English Wikipedia article in Wikidata (queried 2026-10-31); no complete cultivar register was fetched, so other cultivars are not listed."%n
    elif kn in changed or True:
        k['sel']=re.sub(r'Covers \d+ entries',"Covers %d entries"%n,k['sel'])
    if n>12:
        cs=[cls(e['n']) for e in k['x']]
        if len(set(cs))>=2:
            for e,c in zip(k['x'],cs): e['g']=c
            k['x'].sort(key=lambda e:order.index(e['g']))
            k['xg']='by name type in the reference: species, hybrid, cultivar or group'
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
print({k:v for k,v in changed.items() if v})
print(sum(1 for k,(s,kk) in kinds.items() if kk.get('xg')),'kinds sectioned')
