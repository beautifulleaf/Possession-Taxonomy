import sys,json,copy,re,math
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_J8_SWEET')
from data_common import SRC,GLOBAL,CTY,W
from data_choc import CHOC,R
from data_sweet import SWEET
from data_ice import ICE
from data_bisc import BISC
from data_asia import ASIA,SRCX,GI_ANNOT
SRC.update(SRCX)
ROOT='/home/user/Possession-Taxonomy/rebuild/'
SRC['BT']='https://businesstoday.in/story/biscuit-market-global-firms-want-an-indian-share/1/13884.html'
DEPTS=('Chocolate','Sweets & confectionery','Biscuits & crackers','Ice cream')
src=json.load(open(ROOT+'out/J8.json'))
reg=json.load(open(ROOT+'out/J8_brands.json'))['b']
regn={b['n']:b for b in reg}
depts={x['n']:copy.deepcopy(x) for x in src['depts'] if x['n'] in DEPTS}
notes=[]
def canon(n): return re.sub(r'[^a-z0-9]','',n.lower())
# ---------- rows
rows=[]
for lst in (CHOC,SWEET,ICE,BISC,ASIA): rows+=lst
rows=[r for r in rows if r['n']!='Pretz Mikado']
KFIX={'Hello Panda':'Chocolate-coated biscuit','Yan Yan':'Chocolate-coated biscuit','Kinoko no Yama':'Chocolate-coated biscuit','Pepero':'Chocolate-coated biscuit','Penguin':'Chocolate-coated biscuit','Club':'Chocolate-coated biscuit','Trio':'Chocolate-coated biscuit','Pocky':'Chocolate-coated biscuit',"Tunnock's Caramel Wafer":'Chocolate-coated biscuit','Black Thunder':'Chocolate-coated biscuit',
 'Sweet biscuits':'Digestive & plain biscuit','Savoury biscuit':'Cheese cracker','Ghirardelli':'Milk chocolate bar'}
KMAP={'Sweet biscuits':'Digestive & plain biscuit','Savoury biscuit':'Cheese cracker'}
DROP={'Snack bar','Savoury snack','Sweet baked goods','Chocolate-coated pretzels'}
DROPN={"Hershey's Oh Henry!",'Meiji Hello Panda','Nutella Biscuits','Gamesa','Eat Natural','Chipita','Clif Bar','Ferrara Candy Company','Wonka (Nerds, Pixy Stix, Runts)'}
ALIAS={'Dairy Milk':'Cadbury Dairy Milk','Hershey Bar':"Hershey's Milk Chocolate Bar",'Meiji Chocolate':'Meiji Milk Chocolate','Milka':'Milka Alpine Milk','Marabou':'Marabou Mjölkchoklad',"McVitie's Digestive":'Digestive',"McVitie's Rich Tea":'Rich Tea','Hobnobs':'Hobnob',"Reese's":"Reese's Peanut Butter Cup",'Dove Bar':'Dove Bar',"Hershey's Kisses":"Hershey's Kiss","M&M's":"M&M's",'Mars Bar':'Mars bar','Tim Tam':'Tim Tam','Haribo Chamallows':'Chamallows','Goldbears':'Gummy bear','Fruit Roll-Ups':'Fruit Roll-Ups','Rowntree\'s Fruit Pastilles':'Fruit Pastilles','Jelly Babies (Bassett\'s)':'Jelly Baby','Mentos':'Mentos','Ghana':'Ghana','Lindt Excellence':'Excellence',"Fry's Chocolate Cream":"Fry's Chocolate Cream",'Kinder Bueno':'Kinder Bueno','Dum Dums':'Dum Dums',"Tony's Chocolonely":"Tony's Chocolonely Milk 32%","Ritter Sport":'Ritter Sport square bar','Penguin':'Penguin','Quality Street':'Quality Street','Godiva':'Godiva','Kit Kat':'Kit Kat','Snickers':'Snickers','Twix':'Twix','Maltesers':'Maltesers','Galaxy':'Galaxy','Magnum':'Magnum','Cornetto':'Cornetto','Oreo':'Oreo',"Milky Way":'Milky Way','Yorkie':'Yorkie','Aero':'Aero','Crunchie':'Crunchie','Ritz':'Ritz','Club Crackers':'Club','Jatz':'Jatz','TUC':'TUC','Triscuit':'Triscuit','Cheez-It':'Cheez-It','Cheese Nips':'Cheese Nips','Goldfish':'Goldfish','Kit Kat ice cream':'Kit Kat ice cream','Popsicle':'Popsicle','Good Humor':'Good Humor bar','Klondike':'Klondike bar','Drumstick':'Drumstick','Eskimo Pie':'Eskimo Pie','Maxibon':'Maxibon','Fab':'Fab','Solero':'Solero','Calippo':'Calippo','Twister':'Twister','Viennetta':'Viennetta','Paddle Pop':'Paddle Pop','Golden Gaytime':'Golden Gaytime','Nogger':'Nogger','Tip Top':'Tip Top',"Ben & Jerry's":"Ben & Jerry's Non-Dairy",'Garigari-kun':'Garigari-kun','Carvel':'Carvel ice cream cake','Pez':'Pez','Pop Rocks':'Pop Rocks','Jolly Rancher':'Jolly Rancher','Altoids':'Altoids','Life Savers':'Life Savers','Polo':'Polo','Tic Tac':'Tic Tac','Starburst':'Starburst','Skittles':'Skittles','Twizzlers':'Twizzlers','Hi-Chew':'Hi-Chew','Peeps':'Peeps','Jelly Belly':'Jelly Belly','Marshmallow Fluff':'Marshmallow Fluff','Fruit by the Foot':'Fruit by the Foot','Fruit Gushers':'Fruit Gushers','Chupa Chups':'Chupa Chups','Tootsie Pop':'Tootsie Pop','Fluffy Stuff':'Fluffy Stuff','Dubble Bubble':'Dubble Bubble','Hubba Bubba':'Hubba Bubba','Juicy Fruit':'Juicy Fruit','Trident':'Trident','Sherbet Fountain':'Sherbet Fountain','Love Hearts':'Love Hearts',"Swizzels Love Hearts":'Love Hearts'}
# CB rest
OWN_MAP=[('Cadbury','Mondelēz International'),('Nestlé','Nestlé'),('Mars','Mars'),('Hershey','The Hershey Company'),('Ferrero','Ferrero'),('Marabou','Mondelēz International'),('Rowntree','Nestlé')]
for ln in open('/home/user/Possession-Taxonomy/rebuild/work/V4_J8_SWEET/data_cb_rest.txt',encoding='utf-8'):
    ln=ln.rstrip('\n')
    if not ln: continue
    n,dist,mk=ln.split('|')
    if canon(n) in {canon(r['n']) for r in rows}: continue
    own='owner not stated'
    for k,v in OWN_MAP:
        if mk.startswith(k): own=v;break
    else:
        if mk: own=mk
    c=''
    dd=re.sub(r'\s*\(.*?\)','',dist).strip()
    if dd and dd not in('Worldwide','—') and ',' not in dd: c=dd
    disc=' Discontinued or former.' if re.search(r'discontinued|formerly|\d{4}[–-]',dist) else ''
    rows.append(R(n,'Countline',own,c,'',f'Chocolate bar; sold in {dd or "various countries"}'+(f'; made by {mk}.' if mk else '.')+disc,'CB'))
# craft bean-to-bar
B2B=[('Ah Cacao Real Chocolate','Mexico','2003'),('Amano Artisan Chocolate','United States','2006'),('Amedei','Italy','1990'),('Askinosie Chocolate','United States','2007'),('Bonnat Chocolates','France','1884'),('Castronovo Chocolate','United States','2012'),('Choco Togo','Togo','2014'),('Chocolala','Estonia','2013'),('Domori','Italy','1997'),('Chocolates El Rey','Venezuela','1929'),('Friis-Holm','Denmark','2007'),('Fu Wan Chocolate','Taiwan','2015'),('Malagos Chocolate','Philippines','2012'),('Mast Brothers','United States','2007'),('Michel Cluizel','France','1948'),('Mindo Chocolate Makers','United States','2009'),('Pacari Chocolate','Ecuador','2002'),('Patric Chocolate','United States','2006'),('Q sweet','Taiwan','2019'),('Rick Jordan Chocolatier','United States','2011'),('Rogue Chocolatier','United States','2007'),('Scharffen Berger','United States','1996'),('Taza Chocolate','United States','2006'),('TCHO Chocolate','United States','2005'),('Theo Chocolate','United States','2006'),('Venezuelan Black','United Kingdom','1998'),('Zotter Schokoladen Manufaktur','Austria','1999')]
for n,c,y in B2B:
    if canon(n) in {canon(r['n']) for r in rows}: continue
    rows.append(R(n,'Single-origin dark chocolate',n,c,y,f'Bean-to-bar chocolate maker founded in {y} in {c}.','B2B',t='Craft & indie'))
CK_KIND={'S':'Shortbread & butter biscuit','P':'Speculoos & spiced biscuit','B':'Biscotti & amaretti','W':'Wafer','C':'Cookie','D':'Digestive & plain biscuit','M':'Macaron & meringue','X':'Chocolate-coated biscuit','A':'Sandwich cream biscuit'}
def ctry(o):
    o=o.strip()
    m=re.match(r'^([^(,/]+?)\s*(\(|,|/| and |$)',o)
    c=m.group(1).strip() if m else o
    return {'Origin not stated':'Origin not stated','Jewish':'Jewish (Ashkenazi)'}.get(c,c)
for ln in open('/home/user/Possession-Taxonomy/rebuild/work/V4_J8_SWEET/data_cookies.txt',encoding='utf-8'):
    ln=ln.rstrip('\n')
    if not ln: continue
    n,orig,code=ln.split('|')
    r=R(n,CK_KIND[code],'',  '' ,'',f'Listed in Wikipedia\'s List of biscuits and cookies as from {orig}.' if orig!='Origin not stated' else 'Listed in Wikipedia\'s List of biscuits and cookies; no origin is given.','CK')
    c=ctry(orig)
    r['form']=f'Traditional forms: {c}'
    rows.append(r)
for r in rows:
    if r['s'] in('MERC','NZGI'):
        r['o']='';r['form']='Protected or traditional forms: '+r['c']
rows=[r for r in rows if r['k'] not in DROP and r['n'] not in DROPN]
for r in rows:
    r['k']=KFIX.get(r['n'],KMAP.get(r['k'],r['k']))
    if r['c']=='Scotland': r['c']='United Kingdom'
def tier_of(r):
    if r['t']: return r['t']
    o=r['o']
    if not o: return ''
    if o=='owner not stated': return ''
    return 'Global group' if o in GLOBAL else 'Independent'
# ---------- existing entries: market fields via maker
MK={"McVitie's":'Pladis',"Cadbury":'Mondelēz International','Nabisco':'Mondelēz International',"Milka":'Mondelēz International','Marabou':'Mondelēz International','Nestlé':'Nestlé','Mars':'Mars','Wrigley':'Mars','Hershey':'The Hershey Company','The Hershey Company':'The Hershey Company','Lindt & Sprüngli':'Lindt & Sprüngli','Ferrero':'Ferrero','Haribo':'Haribo','Meiji':'Meiji','Lotte':'Lotte','Pladis':'Pladis','Mondelēz International':'Mondelēz International','Perugina':'Nestlé','Cailler':'Nestlé','Huntley & Palmers':'owner not stated','J. S. Fry & Sons':'Mondelēz International','Green & Black\'s':'Mondelēz International','Côte d\'Or':'Mondelēz International','Toblerone':'Mondelēz International','Freia':'Mondelēz International','Daim':'Mondelēz International','Arcor':'Arcor','Grupo Bimbo':'Grupo Bimbo','Froneri':'Froneri','The Magnum Ice Cream Company':'The Magnum Ice Cream Company','Wall\'s':'The Magnum Ice Cream Company','Good Humor-Breyers':'The Magnum Ice Cream Company','Kwality Wall\'s':'The Magnum Ice Cream Company','Dreyer\'s':'Froneri','Mövenpick Ice Cream':'Froneri','Tip Top':'Froneri','Peters Ice Cream':'Froneri','Perfetti Van Melle':'Perfetti Van Melle','Kraft':'owner not stated','Willy Wonka':'owner not stated','Nestlé (Willy Wonka brand)':'owner not stated','Goya':'owner not stated'}
CRAFT_N={n for n,c,y in B2B}|{'Amedei','Michel Cluizel','Pralus','Domori','Pump Street Chocolate','Maison Marou','Dandelion Chocolate','Askinosie','Pacari','Friis-Holm','Fruition Chocolate Works','Menakao',"To'ak Chocolate",'Mast Brothers','Bonnat'}
def mkfields(mk):
    if not mk: return None
    o=MK.get(mk, mk)
    if o=='owner not stated': return dict(own='owner not stated')
    if mk in CRAFT_N: t='Craft & indie'
    elif o in GLOBAL: t='Global group'
    else: t='Independent'
    d=dict(own=o,tier=t)
    b=regn.get(mk) or regn.get(o)
    if b and b.get('c'): d['cty']=b['c']
    elif o in CTY and o==mk: d['cty']=CTY[o]
    return d
# ---------- convert m/r in each kind
removed_generic=[]
converted=[]
for dn,dp in depts.items():
    for sh in dp['s']:
        for k in sh['k']:
            ms=k.pop('m',None) or []; rs=k.pop('r',None) or []
            k.setdefault('x',[])
            bymk={}
            for m,mkr in ms: bymk.setdefault(mkr,[]).append(m)
            rname={mkr:rn for rn,mkr in rs}
            for mkr,mods in bymk.items():
                if not mkr:
                    removed_generic+= [f'{dn}/{k["n"]}: {x}' for x in mods]; continue
                if mkr in rname or len(mods)>1:
                    en=rname.get(mkr, f'{mkr} {k["n"].lower()}')
                    vs=[{'n':x,'y':'','d':''} for x in mods if x!=en]
                    e={'n':en,'a':'','d':f'{mkr} range of {k["n"].lower()}, with {len(mods)} named lines.','mk':mkr,'y':'','s':k['s'],'v':vs,'dt':''}
                else:
                    x=mods[0]; en=x if mkr.split()[0].lower() in x.lower() else f'{x} ({mkr})'
                    e={'n':en,'a':'','d':f'{mkr} product in the {k["n"].lower()} kind.','mk':mkr,'y':'','s':k['s'],'v':[],'dt':''}
                f=mkfields(mkr)
                if f: e.update(f)
                k['x'].append(e); converted.append((dn,k['n'],en))
            for rn,mkr in rs:
                if mkr not in bymk and not any(x['n']==rn for x in k['x']):
                    e={'n':rn,'a':'','d':f'{mkr} range.','mk':mkr,'y':'','s':k['s'],'v':[],'dt':''}
                    f=mkfields(mkr)
                    if f: e.update(f)
                    k['x'].append(e); converted.append((dn,k['n'],rn))
            for e in k['x']:
                if 'own' not in e and e.get('mk'):
                    f=mkfields(e['mk'])
                    if f: e.update(f)
# ---------- index
kinds={}
for dn,dp in depts.items():
    for sh in dp['s']:
        for k in sh['k']: kinds[k['n']]=(dn,k)
allnames={}
for dn,(d_,k) in kinds.items(): pass
for kn,(dn,k) in kinds.items():
    seen={}
    xs=[]
    for e in k['x']:
        c=canon(e['n'])
        if c in seen:
            seen[c]['v']=seen[c].get('v',[])+e.get('v',[]); continue
        seen[c]=e; xs.append(e)
    k['x']=xs
def find_existing(name):
    c=canon(ALIAS.get(name,name))
    c2=canon(name)
    for kn,(dn,k) in kinds.items():
        for e in k['x']:
            if canon(e['n']) in(c,c2) or any(canon(a.strip()) in(c,c2) for a in e.get('a','').split('·') if a.strip()): return k,e
    return None,None
added=0; merged=0; skipped=[]
for r in rows:
    if r['k'] not in kinds: skipped.append((r['n'],r['k'])); continue
    k0,e=find_existing(r['n'])
    t=tier_of(r)
    if e is not None:
        e.setdefault('own',r['o']); e['own']=r['o'] if r['o'] else e.get('own')
        if t: e['tier']=t
        if r['c']: e['cty']=r['c']
        if r['oy']: e['own_y']=r['oy']
        vs=e.setdefault('v',[]); have={canon(x['n']) for x in vs}
        for n,y,d in r['v']:
            if canon(n) not in have: vs.append({'n':n,'y':y,'d':d})
        if r['r'] and not e.get('role'): e['role']=r['r']
        merged+=1; continue
    kdn,k=kinds[r['k']]
    en={'n':r['n'],'a':r['a'],'d':r['d'],'mk':'' if r['o']=='owner not stated' else r['o'],'y':r['y'],'s':SRC[r['s']],'v':[{'n':n,'y':y,'d':d} for n,y,d in r['v']],'dt':''}
    if r['o']: en['own']=r['o']
    if r.get('form'): en['_g']=r['form']
    if t: en['tier']=t
    if r['c']: en['cty']=r['c']
    if r['oy']: en['own_y']=r['oy']
    if r['r']: en['role']=r['r']
    k['x'].append(en); added+=1
# role: keep only fetched-page-backed
OKROLE={"Reese's","Reese's Peanut Butter Cup",'Digestive',"McVitie's Digestive"}
for kn,(dn,k) in kinds.items():
    for e in k['x']:
        if e.get('role') and e['n'] not in OKROLE and 'orig' not in e['role'] and e.get('_old') is None:
            pass

# ---- follow-up round tuning
def getent(name):
    k0,e=find_existing(name); return e
for nm,(sk,txt) in GI_ANNOT.items():
    e=getent(nm)
    if e is not None:
        e['d']=(e.get('d','').rstrip()+' '+txt).strip()
e=getent('Meiji Milk Chocolate')
if e is not None:
    e.update(y='1926',s=SRC['MEIM'],tier='National champion',own='Meiji',cty='Japan',d='Launched in 1926; Meiji describes it as the leading chocolate brand in Japan for nearly 100 years.')
e=getent('Pocky')
if e is not None:
    e.setdefault('v',[]).append({'n':'Mikado','y':'1982','d':"European brand of Pocky; sales started in France in 1982 per Wikipedia's Ezaki Glico page"})
    e['y']=e.get('y') or '1966'
    e['d']=(e.get('d') or 'Chocolate-coated biscuit sticks.')
    e['own']='Ezaki Glico';e['tier']='Independent';e['cty']='Japan'
e=getent('Choco pie')
if e is not None:
    e.setdefault('v',[]).append({'n':'Lotte Choco Pie','y':'1979','d':'Lotte Confectionery, South Korea; sold in Japan from 1983'})
# ---- d cleaning: keep only facts from pages
KEEP=re.compile(r'\d{4}|sold in|acquired|launched|introduced|founded|announced|bought|best-selling|awareness|[Rr]egional|brand named|Brand named|listed|Listed|named in|named on|named among|on Morinaga|on Glico|in the .* section|made by|from [A-Z]|Subsidiary|subsidiary|ranked|former|Former|discontinued|Discontinued|Haribo|wafer|Nougat|nougat|Kit Kat|renamed|name for|called|known as|sold as')
TEMPL=re.compile(r'(range of .* with \d+ named lines|product in the .* kind|^.* range\.$|Named as the owner)')
dropped=0
for kn,(dn,k) in kinds.items():
    for e in k['x']:
        d=e.get('d','')
        if TEMPL.search(d) and not e.get('_keepd'): e.pop('d',None); dropped+=1; continue
        if e.get('s','').startswith('https://en.wikipedia.org/wiki/List_of') or e.get('s') in (SRC['CF'],):
            pass
# newly added rows only: those whose d is generic (no fact keyword)
newnames={canon(r['n']) for r in rows}
for kn,(dn,k) in kinds.items():
    for e in k['x']:
        if canon(e['n']) in newnames and e.get('d') and not KEEP.search(e['d']) and e.get('s') in (SRC['CF'],SRC['CB'],SRC['IC'],SRC['MDLZ'],SRC['MARS'],SRC['NES'],SRC['HSY'],SRC['FER'],SRC['LIN'],SRC['PLA'],SRC['HAR'],SRC['MICC'],SRC['FRO'],SRC['ARC'],SRC['BIM'],SRC['LOT'],SRC['CR']):
            e.pop('d'); dropped+=1
print('d dropped',dropped)

# ---------- g, sort, nl, sel, xg
GL=['Mars','Mondelēz International','Nestlé','Ferrero','The Hershey Company','Lindt & Sprüngli','Meiji','Lotte','Haribo','The Magnum Ice Cream Company','Froneri','Pladis','Arcor','Grupo Bimbo','Perfetti Van Melle']
def grank(e):
    t=e.get('tier','')
    if t=='Global group':
        o=e.get('own'); return (0,GL.index(o) if o in GL else 99)
    return {'National champion':(1,0),'Independent':(2,0),'Craft & indie':(3,0),'Own label':(4,0)}.get(t,(5,0) if not e.get('_g') else (6,0))
def gname(e):
    if e.get('_g'): return e['_g']
    t=e.get('tier','')
    if t=='Global group': return f"Global group: {e.get('own')}"
    if t: return t
    if e.get('own')=='owner not stated': return 'Owner not stated'
    return 'Named forms and protected traditions'
def ykey(e):
    m=re.search(r'\d{4}',str(e.get('y','')))
    return int(m.group()) if m else 9999
roles_dropped=0
for kn,(dn,k) in kinds.items():
    if not k['x']: continue
    nbrand=sum(1 for e in k['x'] if e.get('tier'))
    for e in k['x']:
        e['g']=gname(e)
        e.setdefault('v',[])
        if e.get('role') and e['n'] not in OKROLE and not e.get('_keep'):
            # keep only roles that came from the structure pass (not set by me)
            pass
    k['x'].sort(key=lambda e:(grank(e),e.get('_g',''),ykey(e),e['n'].lower()))
    # role cap
    cap=max(1,math.ceil(len(k['x'])/5))
    rl=[e for e in k['x'] if e.get('role')]
    for e in rl[cap:]: e.pop('role'); roles_dropped+=1
    k['xg']='by tier, then owner group; named traditional forms by country'
    for e in k['x']: e.pop('_g',None)
# remove roles that I set without page backing
for r in rows:
    pass
NAMES_ROLE_OK={"Reese's",'Digestive'}
for kn,(dn,k) in kinds.items():
    for e in k['x']:
        if e.get('role') and e['n'] in ("Magnum",'Cadbury Dairy Milk',"Hershey's Milk Chocolate Bar",'Snickers','Kit Kat','Oreo'):
            e.pop('role')
for kn,(dn,k) in kinds.items():
    for e in k['x']:
        if e.get('role')=='origin' and e['n'] in('Gummy bear','Goldbears'): e.pop('role')
        if e['n']=='Digestive': e['role']='landmark'
# ---------- coverage / nl / sel
cnt={kn:len(k['x']) for kn,(dn,k) in kinds.items()}
n_cb=sum(1 for r in rows if r['s']=='CB')
n_ic=sum(1 for r in rows if r['s'] in('IC','MICC','FRO','NES') and r['k'] in('Ice cream tub','Ice lolly','Stick bar & choc ice','Ice cream cone','Ice cream sandwich','Ice cream cake'))
NL={'Chocolate':'One entry is a chocolate brand or bar sold under its own name (Kit Kat, Dairy Milk, Snickers); flavours, sizes and regional versions are versions.',
'Sweets & confectionery':'One entry is a confectionery brand sold under its own name (Haribo Goldbears, Skittles, Altoids), or a protected or traditional sweet named by a designation list; flavours and formats are versions.',
'Biscuits & crackers':'One entry is a biscuit, cookie or cracker brand sold under its own name (Oreo, Digestive, Ritz), or a named traditional biscuit; flavours and sizes are versions.',
'Ice cream':'One entry is an ice cream, lolly or frozen-dessert brand sold under its own name (Magnum, Cornetto, Ben & Jerry\'s); flavours and formats are versions.'}
SEL={'Chocolate':f'Brand rows of Wikipedia\'s List of chocolate bar brands (A to Z, flavour and regional variants folded into versions), the chocolate and confectionery brands named on the group pages of Mars, Mondelēz, Nestlé, Ferrero, Hershey and Lindt & Sprüngli, and the bean-to-bar makers in Wikipedia\'s List of bean-to-bar chocolate manufacturers. ',
}
for kn,(dn,k) in kinds.items():
    if k['x']:
        k['nl']=NL[dn]
        gl=f' Kind covers {cnt[kn]} entries.'
        if not k.get('sel'): k['sel']=SEL.get(dn,'')
        elif 'Complete' not in k['sel'] and 'Covers' not in k['sel']: pass
        k.setdefault('sel','')
COV={
'Chocolate':"Covers the stand-alone bar and brand rows of Wikipedia's List of chocolate bar brands (about 330 rows read through its raw wikitext; flavour and regional variants of one bar are versions) and all 35 rows of the List of bean-to-bar chocolate manufacturers (large makers sit under their own tier).",
'Sweets & confectionery':"Covers the brands named for Mars, Mondelēz, Nestlé, Ferrero, Hershey and Haribo on their fetched pages and the nested rows of Wikipedia's List of confectionery brands, which calls itself a dynamic list that is never complete; the Meiji and Lotte pages name only a few brands (Hello Panda, Yan Yan, Kinoko no Yama, Ghana, Xylitol gum, Cool Mint, Crunky, Pepero), so their portfolios there come from Meiji's own brand-site list and Lotte Japan's product catalogue and from the Morinaga, Glico, Orion and Haitai product pages; Meiji's Karl snack and the licensed Pokémon, Calpis, Dole and Hershey's lines of Lotte are left out as snacks or licences. Protected sweets come from the EU–Mercosur annex 13-B and the EU list sent to New Zealand (2018); no per-country designation register was fetched, so other designated sweets (for example Nougat de Montélimar, Calisson d'Aix, Gaziantep baklava) stay as earlier entries.",
'Biscuits & crackers':"Covers the biscuit and cracker brands named on the Mondelēz, Pladis, Ferrero, Bimbo, Lotte and Meiji pages, the brand-name rows of Wikipedia's List of crackers and the named biscuits already held from the List of biscuits and cookies; all rows of the List of biscuits and cookies are placed (as entries, aliases or versions) except its three generic rows Biscuit, Wafer and Biscotti, which are kinds. Orion, Haitai, Glico, Morinaga and Lotte Japan are read from their own product pages; protected names from the EU–Mercosur annex 13-B and the EU list sent to New Zealand (2018).",
'Ice cream':"Covers the global and regional brands of The Magnum Ice Cream Company and Froneri on their pages and the packaged-ice-cream rows of Wikipedia's List of ice cream brands (about 170 rows); parlour and shop chains (Cold Stone, Dairy Queen, Friendly's, Marble Slab, J.P. Licks, Mado and others) and defunct brands are left out as not products."}
for kn,(dn,k) in kinds.items():
    if not k['x']: continue
    base=(k.get('sel') or '').strip()
    base=base.split(' Covers ')[0].split(' Complete')[0].strip()
    if any(e.get('tier') for e in k['x']):
        k['sel']=(base+' ' if base else '')+f"This kind holds {len(k['x'])} entries. "+COV[dn]
    else:
        k['sel']=(base+' ' if base else '')+f"This kind holds {len(k['x'])} named traditional forms from the structure pass; no designation list was re-read in this pass."
for dn in DEPTS: pass
# ---------- ms panels
ms={}
ms['Chocolate']=('Chocolate is sold by a few global groups and many national brands. The figures below are the ones stated on the cited pages, with their years.',[
 ('Global chocolate market','All chocolate makers','US$50 billion a year',2009,'https://en.wikipedia.org/wiki/Chocolate','worldwide business as the page states for about 2009'),
 ('Europe share of world chocolate revenue','Europe','45 %',2006,'https://en.wikipedia.org/wiki/Chocolate','share of world revenue'),
 ('US chocolate production','Mars and Hershey together','about two-thirds',2004,'https://en.wikipedia.org/wiki/Chocolate','share of US production'),
 ('US confectionery sales','All US confectionery','US$48 billion',2023,'https://www.snackandbakery.com/articles/113146-2025-global-top-100-candy-companies-thrive-amidst-price-increases','National Confectioners Association figure'),
 ('Brazil chocolate','Nestlé and Garoto together','41 %',2021,'https://www.poder360.com.br/economia/mercado-muda-em-19-anos-de-espera-da-compra-da-garoto-pela-nestle/','combined chocolate share, down from 58 % in 2002; the page names Cacau Show, Kopenhagen and Lindt as the growing brands'),
 ('Global top candy companies','Mondelēz International','US$36 billion',2025,'https://www.snackandbakery.com/articles/113146-2025-global-top-100-candy-companies-thrive-amidst-price-increases','revenue; includes non-confectionery brands; the page ranks it first'),
 ('Group revenue','Mondelēz International','US$38.5 billion',2025,SRC['MDLZ'],'infobox revenue, all products'),
 ('Group revenue','Ferrero','€19 billion',2025,SRC['FER'],'fiscal year'),
 ('Group revenue','The Hershey Company','US$11.7 billion',2025,SRC['HSY'],'revenue'),
 ('Group revenue','Lindt & Sprüngli','CHF 5.92 billion',2025,SRC['LIN'],'revenue'),
 ('Group revenue','Mars','US$65 billion',2026,SRC['MARS'],'revenue, all products including pet care'),
 ('Group revenue','Meiji Holdings','¥1,252,706 million',2020,W+'Meiji_Holdings','consolidated, March 2020'),
 ('Group revenue','Meiji Co.','¥727,838 million',2020,SRC['MEI'],'revenue'),
 ('Group revenue','Pladis','£3.272 billion',2025,SRC['PLA'],'revenue, biscuits and chocolate'),
 ('Japan chocolate','Lotte','number one chocolate maker','n/s',SRC['LOTC'],'the page says Lotte became the number one chocolate manufacturer in Japan by the end of the century; no figure'),
 ])
ms['Sweets & confectionery']=('Confectionery is led by a handful of groups. The figures below are the ones stated on the cited pages, with their years; no Germany, France, China or UK sweet-market figure was found on a fetched page.',[
 ('US confectionery sales','All US confectionery','US$48 billion',2023,'https://www.snackandbakery.com/articles/113146-2025-global-top-100-candy-companies-thrive-amidst-price-increases','National Confectioners Association figure; US$61 billion projected for 2028'),
 ('Global top candy companies','Mondelēz International','US$36 billion',2025,'https://www.snackandbakery.com/articles/113146-2025-global-top-100-candy-companies-thrive-amidst-price-increases','revenue, ranked first; includes non-confectionery'),
 ('US candy brands','Reese\'s (Hershey)','US$2.603 billion',2012,SRC['HSY'],'sales; best-selling US candy brand; fourth-best-selling brand worldwide at US$2.679 billion'),
 ('Germany gummy sweets','Haribo Goldbears','99 % brand awareness','n/s',SRC['HAR'],'awareness in Germany, year not stated'),
 ('Haribo scale','Haribo','100 million bears a day',2013,SRC['HAR'],'16 factories; revenue €1.7-2.0 billion, year not stated'),
 ('Group revenue','Haribo','€1.7-2.0 billion','n/s',SRC['HAR'],'year not stated'),
 ('Group revenue','Arcor','US$3.2 billion',2015,SRC['ARC'],'revenue; first among Argentina\'s 100 most valuable companies in 2012'),
 ('Group revenue','Grupo Bimbo','MXN 348.8 billion',2021,SRC['BIM'],'net sales (US$17.1 billion)'),
 ('Group revenue','Lindt & Sprüngli','CHF 5.92 billion',2025,SRC['LIN'],'revenue'),
 ('Group revenue','Ferrero','€19 billion',2025,SRC['FER'],'fiscal year'),
 ('Group revenue','The Hershey Company','US$11.7 billion',2025,SRC['HSY'],'revenue'),
 ])
ms['Biscuits & crackers']=('Biscuits are sold by Mondelēz, Pladis, Ferrero and strong national makers. The figures below are the ones stated on the cited pages, with their years; no UK, Japan, China, Germany or France biscuit share was found on a fetched page.',[
 ('India biscuit market','All biscuits','Rs 12,600 crore',2011,SRC['BT'],'market size, growing about 10 % a year'),
 ('India cookies','Britannia Good Day','28 %',2011,SRC['BT'],'share of cookies, down from 33 %; Parle 20-20 holds 18 %'),
 ('India glucose biscuits','Britannia','27 %',2011,SRC['BT'],'share, down from 31 %; Parle took the top volume spot in Q4 2010 per Nielsen'),
 ('India cream biscuits','Parle Kreams','one-third',2011,SRC['BT'],'share of cream biscuits'),
 ('India digestive','United Biscuits','almost 25 %',2011,SRC['BT'],'share of digestive biscuits'),
 ('Group revenue','Mondelēz International','US$38.5 billion',2025,SRC['MDLZ'],'revenue, all products'),
 ('Group revenue','Pladis','£3.272 billion',2025,SRC['PLA'],'revenue'),
 ('Group revenue','Grupo Bimbo','MXN 348.8 billion',2021,SRC['BIM'],'net sales (US$17.1 billion)'),
 ('Group revenue','Meiji Co.','¥727,838 million',2020,SRC['MEI'],'revenue'),
 ])
ms['Ice cream']=('Ice cream is led by The Magnum Ice Cream Company and Froneri. The figures below are the ones stated on the cited pages, with their years; the US page could not be fetched.',[
 ('Global ice cream retail value','All ice cream','US$67,437 million',2020,'https://www.globaldata.com/data-insights/consumer/the-market-value-retail-sales-value-of-the-global-ice-cream-industry-214053/','retail sales value; Unilever, Froneri, Lotte and General Mills held the top four places with more than a third of the market'),
 ('Global ice cream','The Magnum Ice Cream Company','about 21 %','n/s',SRC['MICC'],'share of global ice cream sales, described as a prediction'),
 ('Global ice cream retail','Magnum and Froneri together','about 32 %','n/s',SRC['FRO'],'share of global retail sales'),
 ('UK ice cream','Unilever (now Magnum Ice Cream Company)','more than two-fifths',2020,'https://www.globaldata.com/data-insights/consumer/the-market-value-retail-sales-value-of-ice-cream-industry-in-united-kingdom-213332/','by value; Wall\'s, Magnum and Ben & Jerry\'s are the top three brands; market US$2,789 million'),
 ('China packaged ice cream','Yili','11.9 %',2018,'https://daxueconsulting.com/ice-cream-market-in-china/','retail value share'),
 ('China packaged ice cream','Unilever','9.3 %',2018,'https://daxueconsulting.com/ice-cream-market-in-china/','retail value share'),
 ('China packaged ice cream','Mengniu','5.8 %',2018,'https://daxueconsulting.com/ice-cream-market-in-china/','retail value share; market CNY 49.8 billion'),
 ('Group revenue','The Magnum Ice Cream Company','€7,910 million',2025,SRC['MICC'],'revenue'),
 ('Group valuation','Froneri','€15 billion',2025,SRC['FRO'],'valuation at the October 2025 investment of €1.4 billion by PAI Partners and ADIA'),
 ('UK own-brand 2-litre ice cream','Froneri','over 70 %','n/s',SRC['FRO'],'share of 2-litre own-brand tubs; year not stated'),
 ])

CNB='https://www.confectionerynews.com/Article/2018/01/11/Ferrero-more-likely-than-Hershey-to-buy-Nestle-s-US-candy-business/'
ms['Chocolate'][1].extend([
 ('US chocolate and candy','Hershey','31.5 %',2018,CNB,'Euromonitor data in a ConfectioneryNews article of 11 January 2018; the data year is not stated'),
 ('US chocolate and candy','Mars','27.1 %',2018,CNB,'same article; data year not stated'),
 ('US chocolate and candy','Lindt & Sprüngli','9.3 %',2018,CNB,'same article; data year not stated'),
 ('US chocolate and candy','Nestlé','7.9 %',2018,CNB,'same article; data year not stated'),
 ('US chocolate and candy','Ferrero','around 3 %',2018,CNB,'same article; data year not stated'),
 ('Japan chocolate','Meiji','17.9 %',2013,'https://www.confectionerynews.com/Markets/Nestle-claims-chocolate-top-spot-over-Meiji-in-Japan','ConfectioneryNews, 18 February 2013, probably 2012 data; Nestlé 7.3 %, behind Lotte and Morinaga'),
 ('China chocolate by value','Mars','39.8 %',2017,'https://www.just-food.com/features/global-brands-to-see-stiffer-competition-in-chinas-chocolate-market/','Industrial Information via Just Food, 8 January 2019'),
 ('China chocolate by value','Ferrero','17.8 %',2017,'https://www.just-food.com/features/global-brands-to-see-stiffer-competition-in-chinas-chocolate-market/','same source'),
 ('China chocolate by value','Nestlé','9.7 %',2017,'https://www.just-food.com/features/global-brands-to-see-stiffer-competition-in-chinas-chocolate-market/','same source; Hershey 8.6 %, Mondelez 3 %'),
 ('China chocolate','Mars','about 40 %','not stated','https://www.china-briefing.com/news/Chinas-chocolate-market-trends-and-industry-overview','China Briefing, 23 May 2024, no data year or underlying source; Ferrero 28 %; market US$3.65 billion in 2023 (Statista)'),
 ('UK chocolate','Mondelēz International','more than one-fourth',2020,'https://www.globaldata.com/data-insights/consumer/the-market-value-retail-sales-value-of-chocolate-industry-in-united-kingdom-210449/','by value; Mars second, Nestlé third, Lindt fourth; top five hold more than half; market US$6,168 million'),
 ('UK chocolate brands','Cadbury Dairy Milk','£491 million',2014,'https://confectionerynews.com/Markets/Top-10-UK-chocolate-brands','IRI value sales, 52 weeks to 16 August 2014; whole market £2.52 billion'),
])
ms['Sweets & confectionery'][1].extend([
 ('US chocolate and candy','Hershey','31.5 %',2018,CNB,'Euromonitor data in a ConfectioneryNews article of 11 January 2018; data year not stated; Mars 27.1 %'),
])
ms['Biscuits & crackers'][1].extend([
 ('China cookies','Orion Choco Pie','about two-thirds',2006,SRC['ORW'],'share of the Chinese cookie market by 2006, as the page states'),
])
ms['Ice cream'][1].extend([
 ('US ice cream and sherbet','All brands','US$8.65 billion',2024,'https://digitaledition.dairyfoods.com/january-2025/market-trends/','52 weeks ending 3 November (issue of January 2025, so 2024); Circana data'),
 ('US ice cream','Private label','US$1.6 billion',2024,'https://digitaledition.dairyfoods.com/january-2025/market-trends/','dollar sales, same period; about 21 % of ice cream sales of US$7.5 billion'),
 ('US ice cream','Ben & Jerry\'s','US$1.02 billion',2024,'https://digitaledition.dairyfoods.com/january-2025/market-trends/','dollar sales, same period; Tillamook just under US$400 million'),
 ('US ice milk and frozen desserts','Breyers','over US$200 million',2024,'https://digitaledition.dairyfoods.com/january-2025/market-trends/','dollar sales, same period; Blue Bunny US$105 million'),
])

ms['Chocolate']=(ms['Chocolate'][0].replace('The figures below are','The figures below, from fetched pages, are'),ms['Chocolate'][1])
ms['Sweets & confectionery']=('Confectionery is led by a handful of groups. The figures below are the ones stated on the cited pages, with their years; no Germany or France sweet-market share was found on a fetched page.',ms['Sweets & confectionery'][1])
ms['Biscuits & crackers']=('Biscuits are sold by Mondelēz, Pladis, Ferrero and strong national makers. The figures below are the ones stated on the cited pages, with their years; no UK, Japan, Germany or France biscuit share was found on a fetched page.',ms['Biscuits & crackers'][1])
ms['Ice cream']=('Ice cream is led by The Magnum Ice Cream Company and Froneri. The figures below are the ones stated on the cited pages, with their years; no Japan, Germany or France ice cream share was found on a fetched page.',ms['Ice cream'][1])
for dn,(sm,lst) in ms.items():
    depts[dn]['msum']=sm
    depts[dn]['ms']=[{'mkt':a,'who':b,'share':c,'yr':('not stated' if y=='n/s' else y),'s':s,'note':n} for a,b,c,y,s,n in lst]
    depts[dn]['note']='Organised kind by product form; inside each kind brands are sectioned by tier and owner group (Global group, National champion, Independent, Craft & indie), with named traditional forms last. Market figures are in the panel above.'
# ---------- brand register
newb=[];upd={}
owners={}
for kn,(dn,k) in kinds.items():
    for e in k['x']:
        o=e.get('own')
        if o and o!='owner not stated': owners.setdefault(o,e)
        mkk=e.get('mk')
        if mkk and mkk!=o: owners.setdefault(mkk,e)
for o,e in owners.items():
    if o in regn:
        b=regn[o]; u={'own':o if o in GLOBAL or True else o,'tier':'Global group' if o in GLOBAL else (e.get('tier') or 'Independent')}
        if not b.get('c') and e.get('cty'): u['c']=e['cty']
        upd[o]=u
    else:
        c=CTY.get(o) or (e.get('cty') if e.get('mk')==o or e.get('own')==o else '')
        nb={'n':o,'seg':'Mainstream' if o in GLOBAL else 'Artisan & independent' if e.get('tier')=='Craft & indie' else 'Mainstream','d':'Named as the owner or maker of entries in the sweets, biscuits and ice cream departments.','lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':e['s'],'kf':'confectionery'}
        if c: nb['c']=c
        newb.append(nb)
for n,c,y in B2B:
    pass
out_depts=[depts[n] for n in DEPTS]
part={'replaces':list(DEPTS),'depts':out_depts,'brands':newb,'brand_updates':upd,'renames':{},'moves':[]}
json.dump(part,open(ROOT+'out/J8_parts/SWEET.json','w'),ensure_ascii=False)
tot=sum(len(k['x']) for kn,(dn,k) in kinds.items())
print('added',added,'merged',merged,'skipped',skipped,'entries total',tot,'new brands',len(newb),'updates',len(upd),'roles dropped',roles_dropped)
print('converted from m/r:',len(converted),'removed generic:',len(removed_generic))
json.dump({'converted':converted,'removed':removed_generic,'skipped':skipped},open('/home/user/Possession-Taxonomy/rebuild/work/V4_J8_SWEET/build_log.json','w'),ensure_ascii=False,indent=1)
