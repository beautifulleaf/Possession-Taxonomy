import json,os,re,urllib.parse
P='/home/user/Possession-Taxonomy/rebuild/out/C3.json'
G='/home/user/Possession-Taxonomy/rebuild/work/GAP_C3/g3/'
d=json.load(open(P))
def q(s): return 'https://query.wikidata.org/sparql?format=json&query='+urllib.parse.quote(s,safe='')
def qsp(gen): return q('SELECT DISTINCT ?l WHERE { ?g wdt:P225 "%s"; wdt:P105 wd:Q34740. ?sp wdt:P171+ ?g; wdt:P105 wd:Q7432; rdfs:label ?l. FILTER(LANG(?l)="en") ?a schema:about ?sp; schema:isPartOf <https://en.wikipedia.org/>. } ORDER BY ?l'%gen)
def qcl(lab): return q('SELECT DISTINCT ?l WHERE { ?c rdfs:label "%s"@en. ?sp wdt:P31/wdt:P279* ?c; rdfs:label ?l. FILTER(LANG(?l)="en") ?a schema:about ?sp; schema:isPartOf <https://en.wikipedia.org/>. } ORDER BY ?l'%lab)
def norm(s):
    s=s.lower()
    for c in "'‘’ʽ\"": s=s.replace(c,'')
    s=re.sub(r'^(rosa|malus domestica|dahlia|clematis|camellia japonica|hemerocallis|magnolia|rhododendron) ','',s)
    s=re.sub(r' (potato|pear|orange|cherry|fig|tree|olive|strawberry|apple|plum|tomato|citron|tangerine)$','',s)
    return s.strip()
kinds={}
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']: kinds[k['n']]=k
def mk(n,s,desc): return {"n":n,"a":"","d":desc,"mk":"","y":"","s":s,"v":[]}
sp_map={'Citrus':'Speciality citrus','Lilium':'Lily bulb','Hippeastrum':'Amaryllis bulb','Sempervivum':'Houseleek','Aloe':'Aloe','Agave':'Agave','Crassula':'Crassula','Dracaena':'Snake plant & dracaena','Ficus':'Houseplant fig','Peperomia':'Peperomia','Tillandsia':'Air plant','Nepenthes':'Tropical pitcher plant','Drosera':'Sundew','Juniperus':'Juniper bonsai','Salvia':'Salvia','Rosa':'Species rose','Syringa':'Lilac','Buxus':'Hedging & topiary plant','Phalaenopsis':'Moth orchid','Cattleya':'Cattleya','Dendrobium':'Dendrobium','Paphiopedilum':'Slipper orchid','Cymbidium':'Cymbidium','Oncidium':'Oncidium alliance','Vanda':'Vanda'}
added={}; spn={}
def add(kn,ents):
    k=kinds[kn]; ex={norm(e['n']) for e in k['x']}; n0=len(k['x'])
    for e in ents:
        if norm(e['n']) not in ex: k['x'].append(e); ex.add(norm(e['n']))
    added[kn]=added.get(kn,0)+len(k['x'])-n0
for gen,kn in sp_map.items():
    toks=open(G+gen+'.sp').read().split(); url=qsp(gen); ents=[]
    for t in toks:
        if t.startswith('×'): n='%s × %s'%(gen,t[1:]); desc='Named hybrid of the genus %s listed with an English Wikipedia article.'%gen
        else: n='%s %s'%(gen,t); desc='Species of the genus %s listed with an English Wikipedia article.'%gen
        ents.append(mk(n,url,desc))
    add(kn,ents); spn[kn]=(gen,len(toks))
def rd(f): return [x.strip() for x in open(G+f).read().strip().split(';') if x.strip()]
cu={}
cit=rd('citrus.txt')
orange=[x for x in cit if re.search(r'orange|Valencia|navel|Orange',x) and 'Blood' not in x]+['Blood orange']
citron=[x for x in cit if 'citron' in x]
mand=[x for x in cit if x not in orange and x not in citron]
cu['Apple tree']=('apple cultivar',rd('apple.txt'))
cu['Pear tree']=('pear cultivar',rd('pear.txt'))
cu['Plum tree']=('plum cultivar',rd('plum.txt'))
cu['Peach tree']=('peach cultivar',rd('peach.txt'))
cu['Orange tree']=('citrus cultivar',orange)
cu['Mandarin tree']=('citrus cultivar',mand)
cu['Speciality citrus ']=('citrus cultivar',citron)
cu['Olive tree']=('olive cultivar',rd('olive.txt'))
cu['Cherry tree']=('sour cherry cultivar',rd('sourcherry.txt')+rd('sweetcherry.txt'))
cu['Strawberry plant']=('strawberry cultivar',rd('strawberry.txt'))
cu['Tomato seed']=('tomato cultivar',rd('tomato.txt'))
for kn,(lab,names) in cu.items():
    kn=kn.strip(); url=qcl(lab)
    add(kn,[mk(n,url,'Cultivar with an English Wikipedia article, listed under "%s" in Wikidata.'%lab) for n in names])
def cls(n):
    if '×' in n or 'hybrid' in n.lower(): return 'Hybrid'
    if "'" in n or '‘' in n or 'Group' in n or 'group' in n: return 'Cultivar or group'
    if re.match(r'^[A-Z][a-z]+ [a-z-]+$',n): return 'Species'
    return 'Form or common name'
order=['Species','Hybrid','Cultivar or group','Form or common name']
cultonly={k.strip() for k in cu}|{'Seed potato','Tomato seed'}
for kn,k in kinds.items():
    if not k.get('x'): continue
    n=len(k['x'])
    if kn in spn:
        gen,m=spn[kn]
        k['sel']="Covers %d entries: the %d %s species and hybrids that have an English Wikipedia article in Wikidata (queried 2026-10-31), plus items from the earlier cited pages; species without an article are not listed and no complete accepted-species register was fetched."%(n,m,gen)
    elif kn in cultonly and added.get(kn):
        k['sel']="Covers %d entries: RHS and Wikipedia pages read earlier, plus every cultivar listed in Wikidata under the matching cultivar class that has an English Wikipedia article (queried 2026-10-31); cultivars without an article are not listed."%n
    else:
        k['sel']=re.sub(r'Covers \d+ entries',"Covers %d entries"%n,k['sel'])
    if n>12 and kn not in cultonly:
        cs=[cls(e['n']) for e in k['x']]
        if len(set(cs))>=2:
            for e,c in zip(k['x'],cs): e['g']=c
            k['x'].sort(key=lambda e:order.index(e['g']))
            k['xg']='by name type in the reference: species, hybrid, cultivar or group'
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
print({k:v for k,v in added.items() if v})
print(sum(1 for k in kinds.values() if k.get('xg')),'sectioned')
