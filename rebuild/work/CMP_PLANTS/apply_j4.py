import json,re,os,collections
W='/home/user/Possession-Taxonomy/rebuild/work/CMP_PLANTS/'
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(W+'bak/J4.json'))   # always start from the backup (idempotent)
removed=json.load(open(R+'work/V4_J4/removed_m.json'))
kinds={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: kinds[k['n']]=k
def norm(n,kind=''):
    n=n.lower(); n=re.sub(r'\(.*?\)|\[.*?\]','',n)
    n=re.sub(r"[’'\"‘`]",'',n)
    for w in (kind.lower(),'apple','pear','potato','banana','melon','cherry','strawberry','orange','mango','tomato','blueberry','cultivar'):
        n=re.sub(r'\b%s$'%re.escape(w),'',n.strip())
    return re.sub(r'\s+',' ',n).strip()
def keys(x,kind):
    ks={norm(x['n'],kind)}
    a=x.get('a') or ''
    if isinstance(a,list): a=';'.join(a)
    for t in re.split(r'[;,]',a):
        if t.strip(): ks.add(norm(t,kind))
    return ks
WD='https://www.wikidata.org/wiki/'
ITL='https://en.wikipedia.org/wiki/List_of_Italian_food_and_drink_products_with_protected_status'
FP='https://www.freshplaza.com/europe/article/9742629/eu-fresh-produce-pdos-and-pgis/'
full={'PDO':'protected designation of origin','PGI':'protected geographical indication'}
added=collections.defaultdict(list); addedkeys=collections.defaultdict(set); counts=collections.Counter()
def have(kind):
    h=set()
    for x in kinds[kind].get('x',[]): h|=keys(x,kind)
    return h
def add(kind,e,tag):
    k=kinds[kind]; h=have(kind)|addedkeys[kind]
    ks=keys(e,kind)
    if ks&h:
        counts[(kind,'dup')]+=1; addedkeys[kind]|=ks; return
    k.setdefault('x',[]).append(e); addedkeys[kind]|=ks; added[kind].append(e['n']); counts[(kind,tag)]+=1
def wdent(kind,q,n,y,c):
    ph=kind.lower()+' cultivar'
    if kind in('Chilli',): ph='chilli cultivar'
    if kind=='Table grape': ph='table grape cultivar'
    if kind=='Melon': ph='melon cultivar'
    dd=ph[0].upper()+ph[1:]
    if c: dd+=' from '+c
    if y: dd+=(', dated ' if c else ', dated ')+y
    dd+='; Wikidata lists it with an English Wikipedia article.'
    return {"n":n,"a":"","d":dd,"mk":"","y":y,"s":WD+q,"v":[]}
for line in open(W+'wd_Apple.tsv'):
    q,n,y,c=line.rstrip('\n').split('|'); add('Apple',wdent('Apple',q,n,y,c),'wd')
for line in open(W+'wd_other.tsv'):
    kind,q,n,y,c=line.rstrip('\n').split('|'); add(kind,wdent(kind,q,n,y,c),'wd')
for kind,q,n in [('Pear','Q1095094',"Clapp's Favourite"),('Pear','Q1437125','Forelle'),('Nectarine','Q1388967','Nectavigne'),('Plum','Q115914001','Angeleno'),('Plum','Q116301508','Gaviota')]:
    add(kind,wdent(kind,q,n,'',''),'wd')
for line in open(W+'wd_it.tsv'):
    kind,n,st=line.rstrip('\n').split('|')
    dd="Italian %s name registered as a %s in the EU; the Wikipedia list gives its status as %s."%(kind.lower(),full[st],st)
    add(kind,{"n":n,"a":"","d":dd,"mk":"","y":"","s":ITL,"v":[]},'it')
for line in open(W+'wd_fp.tsv'):
    kind,n,st,c=line.rstrip('\n').split('|')
    dd="%s %s name registered as a %s (%s), as the FreshPlaza article states."%(c,kind.lower(),full[st],st)
    add(kind,{"n":n,"a":"","d":dd,"mk":"","y":"","s":FP,"v":[]},'fp')
# coverage lines
cls={'Apple':("apple cultivar",245,238,'The 245 rows less 7 that are not named cultivars; Wikidata holds 2,809 apple cultivar items in all and Wikipedia\'s list over 7,500 cultivars, so cultivars without an article are missing'),
 'Mango':("mango cultivar",89,89,None),'Potato':("potato variety",51,49,None),'Banana':("banana cultivar",28,25,None),'Pear':("pear cultivar",19,19,None),
 'Orange':("Orange cultivar",17,11,None),'Cherry':("sweet cherry cultivar",17,17,None),'Sour cherry':("sour cherry cultivar",11,10,None),'Tomato':("tomato cultivar",11,11,None),
 'Strawberry':("strawberry cultivar",7,7,None),'Plum':("plum cultivar",4,4,None),'Peach':("peach cultivar",3,2,None),'Avocado':("avocado cultivar",5,5,None),
 'Blackberry':("blackberry cultivar",4,4,None),'Blueberry':("fruit cultivar",11,2,None),'Melon':("fruit cultivar",11,9,None),'Garlic':("garlic cultivar",2,2,None),
 'Bulb onion':("Allium cultivar",3,3,None),'Chilli':("Capsicum cultivar",2,2,None),'Mandarin':("Orange and citrus cultivar",None,None,None),'Plantain':("banana cultivar",None,None,None)}
nit=collections.Counter()
for line in open(W+'wd_it.tsv'): nit[line.split('|')[0]]+=1
for kind,(c,m,k,why) in cls.items():
    kx=kinds[kind]; 
    if m is None:
        s="Wikidata's 'Orange cultivar' and 'citrus cultivar' items with an English Wikipedia article that are mandarins were added (queried 2026-10-31); other mandarins are not claimed complete." if kind=='Mandarin' else "Wikidata's 'banana cultivar' items with an English Wikipedia article that are plantains were added (queried 2026-10-31); others are not claimed complete."
    elif kind=='Apple':
        s="Covers %d of 2,809 apple cultivar items on Wikidata: the %d with an English Wikipedia article (queried 2026-10-31) less 7 that are not named cultivars, plus 5 cider apples; Wikipedia's list has over 7,500 cultivars, so cultivars without an article are missing."%(k+5,m)
    elif k==m:
        s="Complete: %d of %d in Wikidata's '%s' items with an English Wikipedia article (queried 2026-10-31); cultivars without an article are not listed."%(k,m,c)
    else:
        s="Covers %d of %d in Wikidata's '%s' items with an English Wikipedia article (queried 2026-10-31); the rest are %s or belong to another kind."%(k,m,c,'generic types, unnamed items')
    kx['sel']=(kx.get('sel','').rstrip()+' '+s).strip()
for kind in set(nit)|{'Potato','Asparagus','Apricot','Chicory','Persimmon','Horseradish','Table grape','Pear','Garlic','Melon'}:
    if kind in kinds and (nit[kind] or any(l.startswith(kind+'|') for l in open(W+'wd_fp.tsv'))):
        kx=kinds[kind]
        s="Protected-origin names follow the fruit, vegetables and cereals section of Wikipedia's List of Italian food and drink products with protected status (complete for Italy) and, for other countries, only the names a fetched FreshPlaza article states."
        kx['sel']=(kx.get('sel','').rstrip()+' '+s).strip()
# unconfirmed report
conf=[];unc=[]
for kind,v in removed.items():
    for a,b in v['m']:
        cands={norm(a,kind)}|{norm(z,kind) for z in re.findall(r'\((.*?)\)',a)}
        cands2=set(cands); cands2.add(norm(re.sub(r'\s+(PDO|PGI|AOP|AOC|GI|IG|DO|IP|TSG)$','',a),kind))
        if kind in kinds and cands2&(have(kind)):
            conf.append((kind,a))
        else: unc.append((kind,a))
json.dump({'confirmed':conf,'unconfirmed':unc},open(W+'unconfirmed.json','w'),ensure_ascii=False,indent=0)
out=R+'out/J4.json'; json.dump(d,open(W+'J4.tmp','w'),ensure_ascii=False,indent=1)
os.replace(W+'J4.tmp',out)
print('added',{k:len(v) for k,v in added.items()}, 'total',sum(len(v) for v in added.values()))
print('dups',sum(v for (k,t),v in counts.items() if t=='dup'))
print('removed confirmed',len(conf),'unconfirmed',len(unc))
