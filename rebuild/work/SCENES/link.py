"""Apply scene harvests, then link every scene brand to a brand register entry.
Usage: python3 work/SCENES/link.py [--write]"""
import json,re,sys,os,collections,copy
W='--write' in sys.argv
A='out/A1.json'; BR='out/A1_brands.json'; H='../verify/work/SCENE_AUDIT/'
a=json.load(open(A)); br=json.load(open(BR))
if W:
    json.dump(a,open('work/SCENES/A1.before_link.json','w'),ensure_ascii=False); json.dump(br,open('work/SCENES/A1_brands.before_link.json','w'),ensure_ascii=False)
G={g['n']:g for g in a['scenes']}
def all_scenes():
    for g in a['scenes']:
        st=[(s,g['n'],None) for s in g['s']]
        while st:
            s,gn,p=st.pop(0); yield s,gn,p
            st=[(c,gn,s) for c in s.get('c',[])]+st
def find(n):
    for s,gn,p in all_scenes():
        if s['n']==n or s['n'].split(' [')[0]==n: return s
# 1. harvests
PLACE={"Bogan":("Regional youth tribes",None),"Racaille":("Regional youth tribes",None),"Maranza":("Regional youth tribes",None),"Talahon":("Regional youth tribes",None),
 "Boho-chic":("Bohemian & counterculture",None),"Lagenlook":("Bohemian & counterculture",None),"Coquette":("Online aesthetics",None),"Baddie":("Online aesthetics",None),
 "French Girl":("Online aesthetics",None),"Dancehall":("Hip-hop, street, skate & surf",None),"UK garage":("Festival & club",None),"Yanki":("Japanese street fashion","YANKI")}
added=0; thin_added=0
for fn in ('harvest_missing.json','harvest_thin.json'):
    if not os.path.exists(H+fn): print('no',fn); continue
    h=json.load(open(H+fn))
    for m in h.get('missing',[]):
        if not m.get('b'): continue
        key=[k for k in PLACE if m['n'].startswith(k)]; assert key,m['n']
        gname,flag=PLACE[key[0]]
        sc={"n":m['n'],"d":m.get('d',''),"src":m['src'],"b":[[x[0],int(x[1]),x[2] if len(x)>2 else []] for x in m['b']]}
        if m.get('bsrc'): sc['bsrc']=m['bsrc']
        g=G[gname]
        if flag=='YANKI':
            kids=[s for s in g['s'] if s['n'].split(' [')[0] in ('Bosozoku','Sukeban')]
            for k in kids: g['s'].remove(k)
            sc['c']=kids
        g['s'].append(sc); added+=1
    for t in h.get('thin',[]):
        s=find(t['scene']); assert s,t['scene']
        have={y[0].lower() for y in s['b']}
        for x in t.get('add',[]):
            if x[0].lower() not in have: s['b'].append([x[0],int(x[1]),x[2] if len(x)>2 else []]); have.add(x[0].lower()); thin_added+=1
        if t.get('bsrc'): s.setdefault('bsrc',{}).update(t['bsrc'])
print('scenes added',added,'brands added to thin scenes',thin_added)
# 2. linking
def norm(s):
    s=s.lower().replace('&','and')
    s=re.sub(r'\((label|clothing line|brand)\)','',s)
    s=re.sub(r"[^a-z0-9]",'',s)
    return s
gidx=json.load(open('reader/_brand_index.json'))['b']
canon={}
for r in gidx: canon.setdefault(norm(r[0]),r[0])
reg={x['n']:x for x in br['b']}
for x in br['b']: canon.setdefault(norm(x['n']),x['n'])
SEG={"Hip-hop, street, skate & surf":"Streetwear","Korean & Chinese contemporary":"Contemporary & premium","Heritage, workwear & military":"Heritage & workwear",
 "Outdoor, technical & sport":"Outdoor & technical","Tailoring & classic":"Contemporary & premium","Avant-garde & archive":"Designer","Minimal & modern":"Contemporary & premium",
 "Designer houses & couture":"Luxury house"}
SCSEG={"Japanese denim":"Japanese & denim","Athleisure and sportswear":"Athletic & sportswear","Classic tailoring (sartorial)":"Bespoke & artisan","Savile Row tailoring":"Bespoke & artisan","Neapolitan tailoring":"Bespoke & artisan"}
def seg(gn,sn):
    if sn.split(' [')[0] in SCSEG: return SCSEG[sn.split(' [')[0]]
    if gn.startswith('Traditional dress'): return "Traditional & national dress"
    return SEG.get(gn,"Subculture & alternative")
mem=collections.defaultdict(list); renamed=0; stubs={}
for s,gn,p in all_scenes():
    sn=s['n'].split(' [')[0]
    for y in s['b']:
        c=canon.get(norm(y[0]))
        if c and c!=y[0]: y[0]=c; renamed+=1
        if not c:
            c=y[0]; canon[norm(c)]=c
            src=(s.get('bsrc') or {}).get(c) or s.get('src','')
            stubs[c]={"n":c,"seg":seg(gn,s['n']),"kf":"","sc":[],"rel":[],"s":src,"cats":["A1"],"note":"Named by the scene source; no brand page fetched yet."}
        if sn not in mem[c]: mem[c].append(sn)
# existing register: scene tags become exact scene names; old free tags kept as tg
scn={s['n'].split(' [')[0] for s,_,_ in all_scenes()}
low={x.lower():x for x in scn}
ALIAS={'hip hop':'Hip-hop fashion','hip-hop':'Hip-hop fashion','casuals':'Casuals (football casual)','football casuals':'Casuals (football casual)','skinhead':'Skinhead','rockabilly':'Rockabilly','streetwear':'Streetwear','gorpcore':'Gorpcore (outdoor)','techwear':'Techwear','preppy':'Preppy','ivy':'Ivy style (Ivy League look)','indie sleaze':'Indie sleaze','minimalism':'Minimalism','ura-harajuku':'Ura-Harajuku (Ura-Hara)','sweet lolita':'Sweet Lolita','amekaji':'Amekaji (American casual, Japan)','military surplus':'Military surplus and field-jacket wear','nautical':'Nautical and marinière style (Breton stripe, sailor dress)','fetish':'Latex and fetish fashion','british country':'British countryside style','café racer':'Rockers (ton-up boys, cafe racers)','motorcycle':'Biker'}
retag=0
for x in br['b']:
    old=x.get('sc',[]); new=[]; tg=[]
    for t in old:
        m=low.get(t.lower()) or ALIAS.get(t.lower())
        (new if m else tg).append(m or t)
    for t in mem.get(x['n'],[]):
        if t not in new: new.append(t)
    if new!=old: retag+=1
    x['sc']=new
    if tg: x['tg']=sorted(set(x.get('tg',[])+tg))
# brands registered in another category only: add A1 to nothing (they open there); record membership count
other=[c for c in mem if c not in reg and c not in stubs]
for c,st in stubs.items(): st['sc']=mem[c]
br['b']+=list(stubs.values())
print('renamed to register spelling',renamed,'register entries retagged',retag,'new A1 register entries',len(stubs),'scene brands registered in other categories',len(other))
if W:
    json.dump(a,open(A,'w'),ensure_ascii=False,indent=1); json.dump(br,open(BR,'w'),ensure_ascii=False,indent=1); print('written')
