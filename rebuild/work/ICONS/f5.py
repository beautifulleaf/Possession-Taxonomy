import json, os, re, collections
R='/home/user/Possession-Taxonomy/rebuild/out/'
def save(p,d):
    t=p+'.tmp'; json.dump(d,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
d=json.load(open(R+'F5.json'))
def kinds():
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']: yield k
K={k['n']:k for k in kinds()}
SRC='https://en.wikipedia.org/wiki/List_of_public_transport_smart_cards'
rows=[l.rstrip('\n').split('\t') for l in open('transit_data.tsv') if l.strip()]
groups=collections.OrderedDict()
for r in rows:
    reg,cty,n,op,city,y=(r+['']*6)[:6]
    groups.setdefault(n,[]).append((reg,cty,op,city,y))
def yr(y):
    m=re.search(r'\d{4}',y or ''); return int(m.group()) if m else 9999
ents=[]
for n,lst in groups.items():
    reg,cty,op,city,y=sorted(lst,key=lambda t:yr(t[4]))[0]
    cities=sorted({t[1] for t in lst})
    e={"n":n,"a":"","d":f"Fare card used in {city}, {cty}." if len(lst)==1 else f"Fare card used in several places: {', '.join(sorted({t[3] for t in lst}))}.","mk":op,"y":y,"s":SRC,"v":[],"dt":"","g":reg}
    if len(lst)>1:
        e["v"]=[{"n":f"{n} ({t[3]})","mk":t[2],"y":t[4],"d":t[1]} for t in lst]
    e['_c']=cty
    ents.append(e)
order=["Africa","North America","Latin America and Caribbean","Europe","West and Central Asia","South Asia","East Asia","Southeast Asia","Oceania"]
ents.sort(key=lambda e:(order.index(e['g']),e['_c'],yr(e['y']),e['n'].lower()))
for e in ents: e.pop('_c')
tk=K['Transit card']
tk['x']=ents; tk['xg']="Region"
tk['nl']="One entry is a named public-transport fare card, or card brand, in Wikipedia's list; a card name used in several places is one entry with a version for each."
tk['sel']=("Follows Wikipedia's List of public transport smart cards, read in three windows (Africa, Americas, Asia and Oceania, Europe; the last window holds only references). "
 "Coverage: every row that names a card is an entry, sectioned by region and ordered by country, year and name; rows that name no card, and Wikipedia's few payment-scheme rows, are left out. "
 "The page also lists some e-money cards (Edy, nanaco, Flazz) and bank-branded cards; they are kept because the page lists them. No entry is marked as an origin because the page does not name a first fare card.")
# charge card
ck=K['Charge card']
ck['x']=[{"n":"Diners Club card","a":"","d":"First general-purpose charge card, according to Wikipedia's Credit card article.","mk":"Diners Club","y":"1950","s":"https://en.wikipedia.org/wiki/Credit_card","v":[],"dt":"","g":"Origin","role":"origin"}]
ck['xg']="Entry type"
ck['nl']="One entry is the first product of its kind or a design-collection landmark."
ck['sel']=("Follows only the fetched Wikipedia Credit card article. Coverage: at most one origin entry (the first of its kind, where a fetched page says so) and design-collection or major-award landmarks confirmed on a fetched page; no other cards are listed.")
save(R+'F5.json',d)
# brands
p=R+'F5_brands.json'; b=json.load(open(p)); have={x['n'] for x in b['b']}
opc={}
for r in rows:
    reg,cty,n,op,city,y=(r+['']*6)[:6]
    if op and op not in have and not re.match(r'(Whole|Several|Nationwide)',op): opc.setdefault(op,[cty,[]])[1].append(n)
for op,(cty,ns) in sorted(opc.items()):
    b['b'].append({"n":op,"c":cty,"f":"","seg":"Institution & issuer","kf":"transit card","d":f"Transit-card issuer, {cty}.","lines":sorted(set(ns))[:6],"eras":[],"sig":[],"sc":[],"rel":[],"s":SRC,"stub":True})
if 'Diners Club' not in have:
    b['b'].append({"n":"Diners Club","c":"","f":"1950","seg":"Institution & issuer","kf":"charge card","d":"Payment card company, named by Wikipedia as the first independent payment card company, founded 8 February 1950.","lines":["Diners Club card"],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://en.wikipedia.org/wiki/Diners_Club_International"})
save(p,b)
print(len(ents),len(opc))
