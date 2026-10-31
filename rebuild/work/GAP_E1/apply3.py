import json,os,re
P='rebuild/out/E1.json'
d=json.load(open(P))
K={}
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']: K[k['n']]=k
def ent(n):
    for k in K.values():
        for e in k.get('x') or []:
            if e['n']==n: yield e
def upd(n,**kw):
    for e in ent(n):
        for a,b in kw.items():
            if a=='own':
                if e.get('own') in(None,'','owner not stated'): e['own']=b
                else: break
            elif a in('tier','own_y'): e[a]=b
            elif not e.get(a): e[a]=b
upd('Cabbage Patch Kids',own='Wicked Cool Toys',tier='Independent',y='1978')
upd('BABY born',own='MGA Entertainment',own_y='2024',tier='Independent',cty='Germany',y='1991')
upd('Webkinz',own='Ganz',tier='Independent',cty='Canada')
upd('Care Bears',own='Authentic Brands Group',tier='Independent')
upd('Blythe',cty='United States')
R='https://en.wikipedia.org/wiki/Rail_transport_modelling_scales'
have={e['n'].lower() for e in K['Model railway scale and gauge']['x']}
for n,dd in[('American OO gauge',"Scale name in the article's closing list of standard gauges and scales."),('4 mm scale',"Scale name in the article's closing list of standard gauges and scales."),('7 mm scale',"Scale name in the article's closing list of standard gauges and scales.")]:
    if n.lower() not in have: K['Model railway scale and gauge']['x'].append({'n':n,'a':'','d':dd,'mk':'','y':'','s':R,'v':[],'g':'Other scales'})
# sections
for kn in('Fashion doll','Teddy bear'):
    k=K[kn]; k['xg']="by maker's home country"
    for e in k['x']: e['g']=e.get('cty') or 'Country not stated'
k=K['Toy soldier & animal figure']; k['xg']='by initial letter (the list gives no other axis)'
for e in k['x']:
    c=e['n'].strip('The ')[:1].upper() if False else re.sub(r'^(The |A )','',e['n'])[:1].upper()
    e['g']='A to D' if c<='D' else 'E to L' if c<='L' else 'M to R' if c<='R' else 'S to Z'
# coverage
def add(kind,txt,replace=False):
    k=K[kind]; sel=(k.get('sel') or '').strip()
    k['sel']=(txt if replace else (sel+' '+txt).strip())
MP="Wikipedia's Mechanical puzzle article and Category:Mechanical puzzles (60 pages)"
add('Building brick set',"Covers 15 of 17 names in Wikipedia's Construction set article under studs; Playmobil is held in Playset and the generic 'Lego clones' is covered by Guangdong Loongon. Reference read to its end.")
add('Metal construction set',"Covers 9 of 10 names in the article's panels list; LEGO Technic is a version of LEGO. Reference read to its end.")
add('Girder-and-panel set',"Covers 5 of 6 names in the article's struts-and-panels list; Geomag is held in Magnetic tile set. Reference read to its end.")
add('Rod-and-connector set',"Complete: 7 of 7 names under struts joined at nodes or of variable length in Wikipedia's Construction set article.")
add('Magnetic tile set',"Complete: 1 of 1 magnetic name in Wikipedia's Construction set article (Geomag); Magna-Tiles is from the earlier pass.")
add('Wooden construction set',"Complete: 8 of 8 names under no connection or notches in Wikipedia's Construction set article (Überstix is held in Metal construction set); Fröbel gifts is from the earlier pass.")
add('Hinged-panel and sleeve set',"Complete: 5 of 5 names under hinged panels and sleeves in Wikipedia's Construction set article.")
add('Marble run',"No complete list exists; the Construction set article names no marble-run systems.")
n=len(K['Cube twisty puzzle']['x'])
add('Cube twisty puzzle',f"Complete: every physical cube and cuboid named in Wikipedia's Combination puzzle article and its Rubik's Cube navigation box ({n} entries; V-Cube 6 to 8 share one entry); the virtual higher-dimensional puzzles are software and out of scope.")
n=len(K['Non-cube twisty puzzle']['x'])
add('Non-cube twisty puzzle',f"Complete: every physical non-cubic twisty puzzle named in that article and box ({n} entries); Magic 120-cell is virtual and out of scope.")
for kn in('Put-together puzzle','Take-apart puzzle','Interlocking puzzle','Disentanglement puzzle','Sequential movement puzzle','Dexterity puzzle','Vexier puzzle','Folding puzzle','Puzzle vessel','Impossible object'):
    add(kn,f"Covers the items of {MP} that belong in this kind; no complete list of all mechanical puzzles exists, so beyond those pages it follows Slocum's classification. Sokoban, Tangloids and Human knot are software, a game and an activity and are out of scope.")
n=len(K['Model railway scale and gauge']['x'])
k=K['Model railway scale and gauge']
k['sel']=f"Wikipedia's Rail transport modelling scales, whole page read. Complete: {n} of {n} scales named (the static-model row and unnamed live-steam rows are left out)."
# toy soldiers
ts=K['Toy soldier & animal figure']
exec(open('rebuild/work/GAP_E1/ts.py').read().split("d=json.load")[0])
inkind={e['n'].lower() for e in ts['x']}
other={e['n'].lower() for kk in K.values() if kk is not ts for e in kk.get('x') or []}
inl=[x for x in names if x.lower() in inkind or x=='Britains']
oth=[x for x in names if x.lower() not in inkind and x!='Britains' and x.lower() in other]
ts['sel']=f"Follows Wikipedia's List of toy soldiers brands (fetched in full, {len(names)} names). Complete: {len(inl)} of {len(names)} names are entries here ({len(oth)} scale-kit makers on the list are entries of Scale model kit; Britains is 'Britains hollow-cast soldiers'). The list gives no country or year, so those fields are empty. Schleich and Papo are kept from their own pages."
print(len(names),len(inl),len(oth))
# stale sels
stale1="The entries come from the pages cited on each entry and are a starting list, not a complete canon; this kind has not yet had the canon pass."
c=0
for k in K.values():
    if not k.get('x'): continue
    sel=(k.get('sel') or '')
    if any(t in sel for t in('Complete:','Covers','No complete list')): continue
    sel=sel.replace(stale1,"The entries come from the pages cited on each entry.").replace(" it has not been matched to a canon.","")
    k['sel']=(sel.strip()+" No complete list exists; follows the pages cited on each entry.").strip(); c+=1
print('stale fixed',c)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
