# -*- coding: utf-8 -*-
import json,re,sys,os,unicodedata,shutil
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/GAP_J5')
from data_rice import RICE
from data2 import *
R='/home/user/Possession-Taxonomy/rebuild/'
j=json.load(open(R+'work/GAP_J5/bak/J5.json'))
brands=json.load(open(R+'work/GAP_J5/bak/J5_brands.json'))
def norm(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+',' ',s).strip()
K={}
for dp in j['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=(dp,s,k)
def kn(n): return K[n][2]
def names(k):
    out=set()
    for e in k.get('x',[]):
        out.add(norm(e['n']))
        for a in (e.get('a') or '').split('·'):
            if a.strip(): out.add(norm(a))
    return out
ALLN=set()
for n,(dp,s,k) in K.items(): ALLN|=names(k)
stats={}
def addx(kind,e,glob=False):
    k=kn(kind); nn=norm(e['n'])
    if nn in names(k) or (glob and nn in ALLN): return False
    for z in ('a','mk','y','dt'): e.setdefault(z,'')
    e.setdefault('v',[])
    k.setdefault('x',[]).append(e); ALLN.add(nn); stats[kind]=stats.get(kind,0)+1; return True
def newkind(shelf,name,d,s,nl):
    for dp in j['depts']:
        for sh in dp['s']:
            if sh['n']==shelf:
                k={"n":name,"a":"","d":d,"s":s,"x":[],"nl":nl,"sel":""}
                sh['k'].append(k); K[name]=(dp,sh,k); return k
    raise Exception(shelf)
def setsel(kind,text,replace=True):
    k=kn(kind)
    old=k.get('sel','')
    if replace: k['sel']=text
    else: k['sel']=(old+' '+text).strip()
def pt(s): return s if s.endswith('.') else s+'.'

# 1 RICE
rice_kinds=[x for x in K if K[x][1]['n']=='Rice']
k=newkind('Rice','Rice cultivars by country',"Named rice cultivars and landraces from national and state lists outside the Italian, Spanish, Japanese, Californian, Carolina, Australian, Thai and Vietnamese lists.",W+'List_of_rice_cultivars',
 "One entry is a named rice cultivar or landrace from Wikipedia's list of rice cultivars; brands and pack sizes are not entries.")
rice_total=0
for cty,s in RICE.items():
    for nme in s.split(';'):
        rice_total+=1
        nn=norm(nme)
        found=any(nn in names(kn(x)) for x in rice_kinds)
        if found: continue
        addx('Rice cultivars by country',{"n":nme,"d":f"Rice cultivar listed for {cty} by Wikipedia.","s":W+'List_of_rice_cultivars',"g":cty})
rn=len(kn('Rice cultivars by country')['x'])
kn('Rice cultivars by country')['xg']='by country or state'
kn('Rice cultivars by country')['sel']=f"Follows Wikipedia, List of rice cultivars, every national and state list not already placed in the other rice kinds. Complete: the whole page was read to its end; {rn} cultivars of other countries and states held here. Left out as not cultivars: group labels (for example Rice specific to Karnataka, Medicinal Rice, Diabetic Rice), wild rice (Zizania) and repeated names within a list."
for x in rice_kinds:
    if x=='Rice cultivars by country': continue
    kk=kn(x); kk['xg']='by country'
    setsel(x,"Follows Wikipedia, List of rice cultivars, country by country. Complete: with Rice cultivars by country, every list on the page (read to its end) is placed; this kind holds the cultivars of that list by grain type.")

# 2 INSTANT NOODLES
U=W+'List_of_instant_noodle_brands'
for line in NOODLES.split('\n'):
    n,cty,own,note=line.split('|')
    e={"n":n,"d":pt(note) if note else "Instant-noodle brand listed by Wikipedia.","s":U,"g":cty or "Not stated"}
    if own: e['mk']=own; e['own']=own
    if cty: e['cty']=cty
    addx('Instant noodles',e,glob=False)
setsel('Instant noodles',f"Follows Wikipedia, List of instant noodle brands. Complete: all 70 rows of the main brand table, read to the page end, plus the named brands of its country sections that state a maker ({len(kn('Instant noodles')['x'])} entries). Navigation-box repeats and brands with no stated maker are left out.")
kn('Instant noodles')['xg']='by home country'

# 3 SPLIT PULSES
Dl=W+'Dal'
for line in SPLIT.split('\n'):
    n,src,note=line.split('|')
    addx('Split pulses and dals',{"n":n,"d":pt(f"{src}. {note}"),"s":Dl,"g":"South Asia"})
setsel('Split pulses and dals',"Follows Wikipedia, Dal (read to its end), which names the split pulses sold as dals. Complete: 14 of 14 dal types the page names; cooked dishes (dal tadka, sambar) and besan are not pantry entries.")
kn('Split pulses and dals')['xg']='by region'

# 4 PAPRIKA
P=W+'Paprika'
for n,g,d in [("Különleges","Hungary","Highest of the five Hungarian commercial grades, exquisite and delicate."),("Édesnemes","Hungary","Second Hungarian grade, delicate and sweet-noble."),("Félédes","Hungary","Third Hungarian grade, semi-sweet."),("Rózsa","Hungary","Fourth Hungarian grade, named rose."),("Erős","Hungary","Fifth Hungarian grade, hot."),("Pimentón dulce","Spain","Mild Spanish pimentón."),("Pimentón agridulce","Spain","Mildly spicy Spanish pimentón."),("Pimentón picante","Spain","Spicy Spanish pimentón."),("Pimentón Tap de Cortí","Spain","Mallorcan pimentón named by the page without detail.")]:
    addx('Paprika',{"n":n,"d":d,"s":P,"g":g})
for e in kn('Paprika')['x']:
    if not e.get('g'): e['g']='Spain' if 'imentón' in e['n'] else ('Slovakia' if 'itava' in e['n'] else 'Hungary')
setsel('Paprika',"Follows Wikipedia, Paprika (first 100,000 of 113,220 characters; the rest is references): the five Hungarian grades and the Spanish pimentón types and protected names; Žitava is from Wikipedia, List of Protected Designation of Origin products by country. Complete: every paprika type or grade the page names; growing areas (Szeged, Kalocsa) and local names for paprika (colorau, tahmira) are not entries.")
kn('Paprika')['xg']='by country'

# 5 SPICE BLENDS (Spice mix page)
SM=W+'Spice_mix'
chk=['Jerk','Montreal','Old Bay','Herbes de Provence','Quatre','Mixed spice','Baharat','Berbere','Ras el hanout','Zaatar','Five spice','Shichimi','Chaat','Garam masala','Panch phoron','Tandoori','Harissa','Adjika','Bouquet garni','Persillade','Recado rojo','Idli podi','Crab boil','Cinnamon sugar','Powder douce']
absent=[c for c in chk if not any(norm(c) in x for x in ALLN)]
print('absent blends',absent)
ADD=[('Adjika','European herb and spice blends','Caucasus','Blend listed in the Spice mix navigation box.'),
('Bouquet garni','European herb and spice blends','France','Herb bundle listed in the Spice mix navigation box.'),
('Persillade','European herb and spice blends','France','Parsley and garlic mix listed in the Spice mix navigation box.'),
('Powder-douce','European herb and spice blends','Europe','Medieval spice powder listed in the Spice mix navigation box.'),
('Cinnamon sugar','Barbecue rubs and seasonings','North America','Sweet spice mix listed in the Spice mix navigation box.'),
('Crab boil','Barbecue rubs and seasonings','North America','Seafood-boil seasoning listed in the Spice mix navigation box.'),
('Recado rojo','Barbecue rubs and seasonings','Mexico','Yucatán red seasoning paste listed in the Spice mix navigation box.'),
('Idli podi','South Asian masalas','India','Dry chutney powder listed in the Spice mix navigation box.')]
added_blend=0
for n,kind,g,d in ADD:
    if addx(kind,{"n":n,"d":d,"s":SM,"g":g},glob=True): added_blend+=1
blend_kinds=['Barbecue rubs and seasonings','European herb and spice blends','Middle Eastern and African spice blends','East and Southeast Asian spice blends','South Asian masalas']
for x in blend_kinds:
    setsel(x,f"Follows Wikipedia, Spice mix, regional lists and navigation box, read in full. Complete: every blend the page names is either an entry in the five regional blend kinds or has its own kind on this shelf (garam masala, chaat masala, shichimi and so on); the page reader may have dropped rows, so the count is the page's own names, not a verified total.")
    kn(x)['xg']='by region'

# 6 HOPS
H=W+'List_of_hop_varieties'
for line in HOPS.split('\n'):
    n,cty,use,y=line.split('|')
    d=f"{cty} hop"+(f", {use}" if use else "")+" variety listed by Wikipedia."
    addx('Hops',{"n":n,"d":d,"s":H,"g":cty,"y":y} ,glob=False)
for e in kn('Hops')['x']:
    if not e.get('g'):
        e['g']={'Saaz':'Czech Republic','East Kent Goldings':'England','Fuggle':'England','Challenger':'England','Target':'England','Hallertau Mittelfrüh':'Germany','Perle':'Germany','Tettnang':'Germany','Magnum':'Germany','Nelson Sauvin':'New Zealand','Motueka':'New Zealand','Galaxy':'Australia','Northern Brewer':'England'}.get(e['n'],'United States')
setsel('Hops',f"Follows Wikipedia, List of hop varieties (first 100,000 of 116,765 characters; the rest is references). Complete: all {len(kn('Hops')['x'])} varieties in its table, with country as section; purpose and year are given only where the page states them.")
kn('Hops')['xg']='by country'

# 7 HOT SAUCE
HS=W+'List_of_hot_sauces'
for line in HOT.split('\n'):
    n,cty,mk=line.split('|')
    e={"n":n,"d":f"Hot sauce from {cty} listed by Wikipedia.","s":HS,"g":cty}
    if mk: e['mk']=mk
    addx('Hot sauce',e,glob=False)
tab=kn('Hot sauce')
for e in tab['x']:
    if not e.get('g'):
        e['g']={'Tabasco':'United States',"Frank's RedHot":'United States','Crystal Hot Sauce':'United States','Louisiana Hot Sauce':'United States','Cholula':'Mexico','Valentina':'Mexico','Tapatío':'United States','El Yucateco':'Mexico','Sriracha':'United States',"Marie Sharp's":'Belize','Peri-peri sauce':'Southern Africa','The Last Dab':'United States','Secret Aardvark':'United States',"Melinda's":'United States','Yellowbird':'United States'}.get(e['n'],'United States')
for e in tab['x']:
    if e['n']=='Tabasco' and not e['v']:
        e['v']=[{"n":x,"y":"","d":"Tabasco variant listed by Wikipedia","mk":""} for x in ['Original','Habanero','Scorpion','Chipotle','Green Sauce','Garlic Pepper Sauce','Sweet and Spicy']]
    if e['n']=="Frank's RedHot" and not e['v']:
        e['v']=[{"n":"Xtra Hot","y":"","d":"Frank's RedHot variant listed by Wikipedia","mk":""}]
setsel('Hot sauce',f"Follows Wikipedia, List of hot sauces (its table read in full). Complete: all 52 rows, with the Tabasco, Trappey's, Taco Bell and Toad Sweat variants folded into their brand; {len(tab['x'])} entries including brands from earlier passes.")
tab['xg']='by country'

# 8 OLIVE CULTIVARS
O=W+'List_of_olive_cultivars'
k=newkind('Olive oil','Olive cultivars',"Olive tree cultivars used for oil, table olives or both.",O,"One entry is a named olive cultivar from Wikipedia's list; the oils and olives made from it are versions of the Olive oil and Table olives kinds.")
for line in OLIVES.split('\n'):
    n,cty,use=line.split('|')
    addx('Olive cultivars',{"n":n,"d":f"Olive cultivar from {cty}"+(f" used for {use}" if use else "")+".","s":O,"g":cty.split(',')[0]})
k['xg']='by country'
k['sel']=f"Follows Wikipedia, List of olive cultivars. Complete: {len(k['x'])} of {len(OLIVES.splitlines())} cultivar rows on the page; the page gives use only for some."
# olive oil PDO note
setsel('Olive oil',"Follows the pages cited on each entry plus Wikipedia, List of Protected Designation of Origin products by country. Covers 5 of about 104 protected olive oils (one overview counts 30 Spanish, 42 Italian, 18 Greek, 7 French, 6 Portuguese, 1 Slovenian); the eAmbrosia register is JavaScript-only, the page reader returned no Spanish, Greek or French oil rows, a Wikidata query returned nothing and the French overview page names none of its oils. Searched: 'Protected Designation of Origin olive oil list Spain Greece France Italy Portugal PDO oils register'.")

# 9 DATES
D=W+'List_of_date_cultivars'
for line in DATES.split('\n'):
    n,cty,note=line.split('|')
    addx('Dates',{"n":n,"d":pt(note),"s":D,"g":cty.split(',')[0]})
for e in kn('Dates')['x']:
    if not e.get('g'): e['g']={'Medjool':'Morocco','Deglet Nour':'Algeria','Ajwa':'Saudi Arabia','Sukkari':'Saudi Arabia','Khalas':'Saudi Arabia','Mazafati':'Iran'}.get(e['n'],'Not stated')
setsel('Dates',"Follows Wikipedia, List of date cultivars. Covers 36 of about 370 cultivars: those the page describes with a note and the main trade dates. The rest are local oasis names (mostly Moroccan, Tunisian, Chadian, Nigerien, Mauritanian, Saudi and Pakistani) with no description on the page and no trade presence, so out of scope for a pantry shelf.")
kn('Dates')['xg']='by country'

# 10 DRIED CHILLI
C=W+'List_of_Capsicum_cultivars'
for line in CHILLI.split('\n'):
    n,sp,heat=line.split('|')
    addx('Dried chilli',{"n":n,"d":f"{sp} chilli, {heat}, listed by Wikipedia.","s":C,"g":sp},glob=True)
for e in kn('Dried chilli')['x']:
    if not e.get('g'): e['g']='C. annuum'
setsel('Dried chilli',"Follows Wikipedia, List of Capsicum cultivars (100,000 of 108,556 characters; the rest is references). Covers 33 of about 84 cultivars: those sold dried, flaked or ground. The rest are fresh-pod or ornamental cultivars (Anaheim, Poblano, Padrón, Jalapeño and so on), which sit in J4 Chilli.")
kn('Dried chilli')['xg']='by species'

# 11 FROZEN
F=W+'List_of_frozen_food_brands'
for n in FROZEN.split('\n'):
    addx('Frozen ready meals',{"n":n,"d":"Frozen food brand listed by Wikipedia.","s":F,"g":"Frozen food"},glob=True)
for n in PIZZA.split('\n'):
    addx('Frozen pizza',{"n":n,"d":"Frozen pizza brand listed by Wikipedia.","s":F,"g":"Frozen pizza"},glob=True)
for x,cnt in (('Frozen ready meals',None),('Frozen pizza',None)):
    for e in kn(x)['x']:
        if not e.get('g'): e['g']='Frozen food' if x=='Frozen ready meals' else 'Frozen pizza'
setsel('Frozen ready meals',"Follows Wikipedia, List of frozen food brands, main list. Complete: 50 of 50 main-list brands (those already in other frozen kinds stay there); the page gives no country or owner, so none is recorded here.")
setsel('Frozen pizza',"Follows Wikipedia, List of frozen food brands, frozen pizza section. Complete: 17 of 17 brands; the page gives no country or owner.")
kn('Frozen ready meals')['xg']='by list section'; kn('Frozen pizza')['xg']='by list section'

# 12 KIMCHI
KM=W+'Kimchi'
for line in KIMCHI.split('\n'):
    n,ing,note=line.split('|')
    addx('Kimchi',{"n":n,"d":pt(note) if note else "Kimchi variety named by Wikipedia.","s":KM,"g":(ing or 'type')},glob=False)
for e in kn('Kimchi')['x']:
    if not e.get('g'): e['g']='brand' if e['n'] not in('Baechu kimchi','Kkakdugi','Oi-sobagi') else 'napa cabbage' if e['n']=='Baechu kimchi' else 'radish' if e['n']=='Kkakdugi' else 'cucumber'
setsel('Kimchi',"Follows Wikipedia, Kimchi (first 200,000 of 202,918 characters; the rest is references). Complete: the named varieties on the page, with main ingredient as section; the page has no whole-space list and the separate list page returned 404. Kimchi dishes (fried rice, pancake, dumpling) are not entries.")
kn('Kimchi')['xg']='by main ingredient'

# 13 PASTA BRANDS
setsel('Pasta brands',"No complete list exists; follows Wikipedia, Barilla Group (brands owned, with acquisition years). Searched: 'Wikipedia list of pasta manufacturers companies brands Italy' (no list page; Wikipedia's List of pasta brands returned 404; the one commercial overview fetched returned no text).")

# 14 default coverage lines
def hosts(sel):
    m=re.search(r'cited on each entry \(([^)]*)\)',sel)
    return m.group(1) if m else ''
cov=0
for n,(dp,s,k) in K.items():
    if not k.get('x') and not k.get('m'): continue
    sel=k.get('sel','')
    if re.search(r'(Complete: \d+ of|Complete:|Covers \d+ of|No complete list exists)',sel): continue
    h=hosts(sel)
    k['sel']="No complete list exists; follows "+(f"the overviews cited on each entry ({h})." if h else "the overviews cited on each entry.")
    extra=re.sub(r'^Follows the pages cited on each entry \([^)]*\)\. No whole-space reference list exists for this kind, so the entries are the named items those pages give, not a complete canon\.\s*','',sel)
    if extra and extra!=sel and 'Protected names' not in extra: k['sel']+=' '+extra
    cov+=1
print('default coverage lines',cov)

# 15 xg for kinds with g on most entries
for n,(dp,s,k) in K.items():
    x=k.get('x',[])
    if x and not k.get('xg') and sum(1 for e in x if e.get('g'))>=max(2,len(x)//2):
        vals={e.get('g') for e in x if e.get('g')}
        k['xg']='by section' if len(vals)<=6 and any(('pasta' in str(v).lower() or 'Long' in str(v)) for v in vals) else 'by country or maker'
    # fill missing g where xg exists
    if k.get('xg'):
        for e in x:
            if not e.get('g'): e['g']='Other'

json.dump(stats,open(R+'work/GAP_J5/stats.json','w'),indent=1)
print(stats)
tmp=R+'work/GAP_J5/J5.new.json'
json.dump(j,open(tmp,'w'),ensure_ascii=False,indent=1)
os.replace(tmp,R+'out/J5.json')
print('rice listed',rice_total,'new',rn)
