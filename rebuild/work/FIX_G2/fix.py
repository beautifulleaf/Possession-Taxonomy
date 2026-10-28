import json,unicodedata,re,copy
O='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(O+'G2.json'));T=json.load(open(O+'G2_traditions.json'));B=json.load(open(O+'G2_brands.json'))
def norm(s): return re.sub(r'[^a-z0-9 ]','',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip()
K={};SH={}
for dp in d['depts']:
  for s in dp['s']:
    SH[s['n']]=s
    for k in s['k']: K[k['n']]=k
def find_arch(sn):
    for k in SH[sn]['k']:
        for x in k.get('x',[]):
            yield k,x
def mergev(a,b):
    have={v['n'] for v in a.get('v',[])}
    for v in b.get('v',[]):
        if v['n'] not in have: a.setdefault('v',[]).append(v)
    al=[x.strip() for x in (a.get('a') or '').split('·') if x.strip()]
    for x in [x.strip() for x in (b.get('a') or '').split('·') if x.strip()]+[b['n']]:
        if x.lower() not in [y.lower() for y in al] and x.lower()!=a['n'].lower(): al.append(x)
    a['a']=' · '.join(al)
# ---- collect style and vernacular archetypes
styles=[];vern=[]
for sn,fam in (('Architectural styles (view)',styles),('Regional house traditions',vern)):
    for k,x in list(find_arch(sn)): fam.append((k['n'],x))
STYLEFORMS={'Classical & Georgian styles':['Detached house','Terraced house','Townhouse','Country house'],
 'Victorian & revival styles':['Detached house','Semi-detached house','Terraced house','Villa'],
 'Arts and Crafts & early modern styles':['Detached house','Semi-detached house','Bungalow'],
 'Modern & contemporary styles':['Detached house','Flat','Villa'],
 'Colonial & settler styles':['Detached house','Cottage','Farmhouse','Villa']}
REG={'British & Irish vernacular houses':'British Isles','Continental European vernacular houses':'Continental Europe','Mediterranean & Iberian houses':'Mediterranean and Iberia','Houses of the Americas':'Americas','Asian & Middle Eastern houses':'Asia and Middle East'}
PLACE={}
for n,kk in {'Terraced house':['Back-to-back house','Brownstone'],'Townhouse':['Machiya','Dutch canal house','Charleston single house','Shophouse'],
 'Cottage':['Thatched cob cottage','Blackhouse','Trullo','Dammuso','Cycladic house','Creole cottage','Shotgun house','Chattel house','Cape Cod','Saltbox'],
 'Farmhouse':['Longhouse','Wealden hall house','Cruck house','Bastle house','Low German house','Fachwerkhaus','Black Forest house','Geestharden house','Uthland-Frisian house','Upper Lusatian house','Frutighaus','Longère','Nordic log house','Masía','Casona','Connected farm','I-house','Upright and wing','Minka','Hanok'],
 'Castle & tower house':['Kulla','Vainakh residential tower','Casa torre'],
 'Detached house':['Dacha','Malay house','Assam-type house','Adobe pueblo-style house'],
 'Courtyard house':['Siheyuan','Fujian tulou','Riad','Haveli','Wind-tower house']}.items():
    for a in kk: PLACE[a]=n
# new kind: Courtyard house
K['Courtyard house']={"n":"Courtyard house","a":"patio house · atrium house","d":"A house whose main rooms face an open central yard; the form recurs in China, Morocco, Central Asia and India.","t":["Walled courtyard house","Multi-courtyard compound","Round or square communal earth building"],"s":"https://en.wikipedia.org/wiki/Courtyard_house","x":[]}
SH['House types']['k'].insert(SH['House types']['k'].index(K['Villa'])+1,K['Courtyard house'])
vreg=[]
capecod=None
for sh,x in vern:
    n=x['n']
    if n in('Cortijo','Finca','Yaodong','Pazo'):
        tgt={'Cortijo':'Hacienda & estancia','Finca':'Hacienda & estancia','Pazo':'Country house','Yaodong':'Earth-sheltered & cave house'}[n]
        for y in K[tgt].get('x',[]):
            if y['n']==n: mergev(y,x)
        continue
    if n=='Cape Cod':
        capecod=x; continue
    tk=PLACE[n]; x=copy.deepcopy(x); x['st']=REG[sh]  # view tag: regional tradition
    K[tk].setdefault('x',[]).append(x); vreg.append((tk,x,sh))
# Cape Cod merge
for sh,x in styles:
    if x['n']=='Cape Cod house':
        capecod_style=x
mergev(capecod_style,capecod); capecod_style['st']='Americas'; K['Cottage']['x'].insert(0,capecod_style)
# styles -> register
newT=[]
for sh,x in styles:
    if x['n']=='Cape Cod house': continue
    newT.append({"n":x['n'],"g":"Architectural styles","r":"","p":x.get('y',''),"d":x['d'],"tech":x.get('dt',''),"mat":"","forms":STYLEFORMS[sh],"ctr":[],"auth":"","s":x['s'],"a":x.get('a',''),"v":x.get('v',[])})
# remove shelves
for dp in d['depts']:
    dp['s']=[s for s in dp['s'] if s['n'] not in('Architectural styles (view)','Regional house traditions')]
# types hygiene
def drop(k,pre):
    K[k]['t']=[t for t in K[k]['t'] if not any(t.lower().startswith(p.lower()) for p in pre)]
drop('Country house',['Manor house','Ansitz','Pazo','Bastide','Georgian and Palladian','Victorian and Jacobethan'])
drop('Mansion',['Gilded Age','McMansion','Urban mansion'])
drop('Château',['Château viticole'])
drop('Castle & tower house',['Scottish tower','Irish tower','Schloss','Fortified manor'])
drop('Palazzo',['Piano nobile'])
drop('Chalet',['Traditional Alpine'])
drop('Hacienda & estancia',['Estancia','Finca','Quinta','Cortijo'])
drop('Terraced house',['Back-to-back','Brownstone'])
# ---- G2-4 single properties -> pattern archetypes
REN={'Necker Island':('Caribbean resort cay','Necker Island'),'Skorpios':('Aegean private island','Skorpios'),'Lānaʻi':('Whole populated island','Lānaʻi'),
 'Balmoral Estate':('Highland sporting estate','Balmoral Estate'),'Claiborne Farm':('Kentucky bluegrass stud farm','Claiborne Farm'),
 'Château Lafite Rothschild':('Bordeaux first-growth château estate','Château Lafite Rothschild'),'Tenuta San Guido':('Tuscan coastal tenuta','Tenuta San Guido'),
 'King Ranch':('Texas cattle ranch','King Ranch'),'Anna Creek Station':('Outback cattle station','Anna Creek Station'),'Spruce Creek Fly-In':('Residential fly-in airpark','Spruce Creek Fly-In')}
for k in K.values():
    for x in k.get('x',[]):
        if x['n'] in REN and k['n'] in('Private island','Sporting estate','Equestrian property','Vineyard & wine estate','Ranch & station','Airpark home & private airstrip'):
            nn,ex=REN[x['n']]; old=x['n']; x['ex']=[ex]; x['n']=nn
            x['a']=' · '.join([p for p in [x.get('a','')] if p and p!=nn]); x['y']=x.get('y','')
            x['d']=x.get('d') or ''
            print('renamed',old,'->',nn,'|',x['d'])
# ---- G2-2 burial
bs=SH['Burial places']
def mk(n,a,dd,t,src):return {"n":n,"a":a,"d":dd,"t":t,"s":src}
bs['k']=[mk('Burial plot','grave plot · grave space · cemetery plot','An in-ground grave space for a coffin or casket, including green burial and shared graves.',
 ['Single plot','Companion plot','Family plot','Gated estate','Hedge estate','Green burial plot (Baumgrab, shared-tree plot)','Communal grave space'],K['Ground burial plot']['s']),
 mk('Crypt & mausoleum','lawn crypt · mausoleum','An above-ground burial chamber: a space in a shared building or lawn crypt, or a private family mausoleum.',
 ['Lawn crypt','Mausoleum crypt (indoor)','Private mausoleum'],K['Private mausoleum']['s']),
 mk('Cremation plot & niche','columbarium niche · urn niche · urn garden','A space for cremated remains: an in-ground cremation plot, a columbarium niche or an urn stele.',
 ['Cremation plot','Columbarium niche','Urnenstele (urn stele)'],K['Columbarium niche']['s'])]
bs['k'][1]['s']=K['Private mausoleum']['s']
# farm buildings
fb=SH['Farm & estate buildings']
ts=[]
for kn in ['Barn','Stable block','Field shelter','Cart shed','Granary','Dovecote']:
    ts.append(kn); ts+= [f"{kn.lower()}: {t.lower() if not t[0].isupper() or t.split()[0] in ('Fixed','Mobile','Raised','Loft','Circular','Square','Lectern','Traditional','Timber','American','Threshing','Dutch','Tithe','Pole','Steel') else t}" for t in (K[kn].get('t') or [])]
fb['k']=[{"n":"Farm building","a":"agricultural building · outbuilding","d":"A working building on a farm or estate: barn, stable block, field shelter, cart shed, granary or dovecote.","t":ts,"s":K['Barn']['s']}]
# arable
fs=SH['Farm & rural land']; fs['k']=[k for k in fs['k'] if k['n']!='Arable land']
K['Farm']['t'].insert(1,'arable land (bare, no farmhouse)')
# ---- G2-1
PF='https://en.wikipedia.org/wiki/Prefabricated_home'
K['Kit & prefab house']['x']+= [
 {"n":"Leisurama","a":"","d":"Low-cost prefabricated holiday house designed by Andrew Geller and sold through Macy's; over 200 built at Montauk.","mk":"","y":"1963–1965","s":PF,"dt":"Montauk, New York · 1964 World's Fair showhouse"},
 {"n":"Maison Tropicale","a":"","d":"Aluminium prefabricated house designed by Jean Prouvé for use in Africa.","mk":"","y":"1940s","s":PF,"dt":"aluminium panels · demountable"},
 {"n":"Airey house","a":"","d":"Post-war British prefab built in large numbers.","mk":"","y":"1945–1948","s":PF,"dt":"concrete-column frame · estate or council use"},
 {"n":"Japanese steel-frame prefab house","a":"Sekisui House IS series","d":"Factory-built steel-frame detached house sold by Japan's large housebuilders.","mk":"Sekisui House","y":"","s":"https://en.wikipedia.org/wiki/Sekisui_House","v":[{"n":"IS series","mk":"Sekisui House","y":"","d":"one- and two-storey steel-frame houses"},{"n":"BIENA","mk":"Sekisui House","y":"","d":"three- and four-storey steel-frame houses"},{"n":"SHAWOOD","mk":"Sekisui House","y":"","d":"laminated-timber post-and-beam houses"}],"dt":"storeys · steel or laminated timber · energy standard (Green First)"}]
BR='https://en.wikipedia.org/wiki/Branded_residence'
K['Serviced & branded residence']['x']+=[
 {"n":"Hotel-brand residences","a":"hotel-branded residences","d":"Privately owned homes sold under a hotel group's name, with its services.","mk":"","y":"","s":BR,"v":[{"n":"Mandarin Oriental Residences","mk":"Mandarin Oriental","y":"","d":""},{"n":"Ritz-Carlton Residences","mk":"Ritz-Carlton","y":"","d":""}],"dt":"attached or standalone · service package · fees · rental programme"},
 {"n":"Fashion-house residences","a":"","d":"Homes sold under a fashion house's name and interior design.","mk":"","y":"","s":BR,"v":[{"n":"Armani residences","mk":"Armani","y":"","d":""},{"n":"Elie Saab residences","mk":"Elie Saab","y":"","d":""},{"n":"Missoni residences","mk":"Missoni","y":"","d":""}],"dt":"designer interiors · city or resort · fees"},
 {"n":"Automotive-marque residences","a":"","d":"Homes sold under a car maker's or design house's name.","mk":"","y":"","s":BR,"v":[{"n":"Aston Martin residences","mk":"Aston Martin","y":"","d":""},{"n":"Pininfarina residences","mk":"Pininfarina","y":"","d":""},{"n":"Tonino Lamborghini residences","mk":"Tonino Lamborghini","y":"","d":""}],"dt":"marque styling · amenities · fees"},
 {"n":"Designer-led branded residences","a":"","d":"Homes sold under a design company's name rather than a hotel or fashion house.","mk":"YOO","y":"","s":BR,"dt":"designer interiors · fees"}]
BH='https://en.wikipedia.org/wiki/Beach_hut'
bh={"n":"Beach hut","a":"beach cabana · bathing box","d":"A small hut above the high-tide line used for shelter, changing and storage, owned or leased on a bathing beach.","t":["Council-owned and let","Privately owned freehold or leasehold"],"s":BH,
 "x":[{"n":"Bournemouth beach hut","a":"","d":"Purpose-built hut on the Bournemouth seafront, from traditional wooden sheds to modern concrete terrace huts.","mk":"","y":"","s":BH,"dt":"timber or concrete · council or private"},
 {"n":"Mudeford Spit hut","a":"","d":"Private beach hut on Mudeford Spit; one sold for £170,000 in 2012.","mk":"","y":"","s":BH,"dt":"position · price"},
 {"n":"Brighton bathing box","a":"","d":"Brightly coloured bathing box at Brighton, Victoria, known from 1862.","mk":"","y":"1862 or earlier","s":BH,"dt":"colour scheme · licence"}]}
SH['Unusual & converted properties']['k'].append(bh)
TS='https://en.wikipedia.org/wiki/Timeshare'
ft={"n":"Fractional & timeshare","a":"timeshare · fractional ownership · vacation club","d":"A share in a holiday property giving set periods of use, either as a deed to part of the title or as a right to use.","t":["Deeded week","Right-to-use contract","Fixed week","Floating week","Rotating (flex) week","Points programme","Fractional title share (one-quarter, one-eighth)"],"s":TS,
 "x":[{"n":"Points-based vacation club","a":"points programme","d":"Annual points spent on stays across a resort group, introduced by Disney Vacation Club in 1991.","mk":"","y":"1991","s":TS,"dt":"points per year · resort group · exchange company (RCI, Interval International)"},
 {"n":"Fractional apartment share","a":"","d":"A share of the legal title to an apartment, often one-quarter, giving roughly three months' use a year.","mk":"","y":"","s":"https://en.wikipedia.org/wiki/Fractional_ownership","dt":"share size · weeks of use · holding entity"}]}
SH['Flats']['k'].append(ft)
# ---- traditions register
tr=T['t']
tr=[t for t in tr if t['n']!='Loess yaodong']
for t in tr:
    if t['n']=='Yaodong': t['g']='Vernacular architecture'
def match(x,t):
    nt=norm(t['n']); cands=[norm(x['n'])]+[norm(a) for a in (x.get('a') or '').split('·') if len(a.strip())>=5]
    return any(c and (c in nt or nt in c) for c in cands)
used=set()
for tk,x,sh in vreg:
    m=[i for i,t in enumerate(tr) if i not in used and (norm(x['n']) in norm(t['n']) or norm(t['n']) in norm(x['n']))]
    if not m: m=[i for i,t in enumerate(tr) if i not in used and match(x,t) and 'wealden' not in norm(t['n'])]
    if m:
        i=m[0];used.add(i);tr[i]['forms']=[tk];print('REG match',x['n'],'->',tr[i]['n'])
    else:
        e={"n":x['n'],"g":"Vernacular architecture","r":REG[sh],"p":x.get('y',''),"d":x['d'],"tech":x.get('dt',''),"mat":"","forms":[tk],"ctr":[],"auth":"","s":x['s']}
        tr.append(e);print('REG new',x['n'])
for t in tr:
    if t['n']=='Yaodong': t['forms']=['Earth-sheltered & cave house']
tr+=newT
# stale form names in leftover entries
valid=set(K)|{'Courtyard house'}
for t in tr:
    t['forms']=[f for f in t.get('forms',[]) if f in valid] or t.get('forms',[])
    if not any(f in valid for f in t.get('forms',[])): print('STALE forms',t['n'],t['forms'])
T['t']=tr
# ---- brands
bl=B['b']
def addb(n,c,f,seg,kf,dd,lines,sig,rel,s):
    if any(b['n'].lower()==n.lower() for b in bl):return
    bl.append({"n":n,"c":c,"f":f,"seg":seg,"d":dd,"lines":lines,"eras":[],"sig":sig,"sc":["branded residences"] if 'Resid' in ''.join(sig+lines) else ["prefab housing"],"rel":rel,"s":s,"kf":kf})
addb('Sekisui House','Japan','1960','Professional & flagship','prefab housebuilder','Osaka housebuilder spun off from Sekisui Chemical in 1960; sells steel-frame and timber detached houses.',['IS series','BIENA','SHAWOOD','Sha Maison','Grande Maison','Green First'],['Japanese steel-frame prefab house'],['Daiwa House'],'https://en.wikipedia.org/wiki/Sekisui_House')
addb('Daiwa House','Japan','1955','Professional & flagship','prefab housebuilder','Osaka company founded 1955 that builds prefabricated houses and commercial buildings.',[],[],['Sekisui House'],'https://en.wikipedia.org/wiki/Daiwa_House')
for n,kf in [('Mandarin Oriental','luxury hotels'),('Ritz-Carlton','luxury hotels')]:
    addb(n,'','','Premium',kf,'Hotel group listed among brands that sell branded residences.',[n+' Residences'],[n+' Residences'],['Four Seasons Hotels and Resorts'],BR)
for n,seg,kf in [('Armani','Luxury house','fashion'),('Elie Saab','Luxury house','couture'),('Missoni','Luxury house','knitwear'),('Aston Martin','Professional & flagship','grand tourers'),('Pininfarina','Heritage manufactory','car design'),('Tonino Lamborghini','Premium','lifestyle licensing')]:
    seg={'Luxury house':'Premium'}.get(seg,seg)
    addb(n,'','',seg,kf,'Listed among non-hotel brands that sell branded residences.',[n+' residences'],[n+' residences'],[],BR)
addb('YOO','United Kingdom','1999','Specialist','design-led residences','Design company founded in 1999 listed among non-hotel brands behind branded residences.',[],['Designer-led branded residences'],[],BR)
for b in bl:
    if b['n'] in('Four Seasons Hotels and Resorts','Aman Resorts'):
        b['rel']=sorted(set(b['rel']+['Mandarin Oriental','Ritz-Carlton']))
        
json.dump(d,open(O+'G2.json.tmp','w'),ensure_ascii=False,indent=1)
json.dump(T,open(O+'G2_traditions.json.tmp','w'),ensure_ascii=False,indent=1)
json.dump(B,open(O+'G2_brands.json.tmp','w'),ensure_ascii=False,indent=1)
