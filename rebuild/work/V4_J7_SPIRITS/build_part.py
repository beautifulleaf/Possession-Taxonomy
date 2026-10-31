import json,re,sys,copy,collections
sys.path.insert(0,'.')
from lists import *
from lists2 import *
W='https://en.wikipedia.org/wiki/'
GLOBAL={'Diageo','Pernod Ricard','Bacardi Limited','Suntory Global Spirits','LVMH','Brown-Forman','Campari','Rémy Cointreau'}
OLD=json.load(open('/home/user/Possession-Taxonomy/rebuild/out/J7.json'))
oldd={d['n']:d for d in OLD['depts'] if d['n'] in('Whisky','Spirits','Liqueurs')}
oldk={}
for d in oldd.values():
    for s in d['s']:
        for k in s['k']: oldk[k['n']]=k
def norm(s):
    s=s.lower().replace('’',"'").replace('é','e').replace('è','e').replace('ö','o').replace('ü','u').replace('ó','o').replace('í','i').replace('ç','c').replace('ú','u').replace('à','a').replace('â','a')
    s=re.sub(r"\b(the|distillery|distilleries|whisky|whiskey|tequila|gin|vodka|rum|single malt|scotch)\b",' ',s)
    return re.sub(r'[^a-z0-9]+',' ',s).strip()
OWN={}
for l in open('ownmap.txt'):
    n,o,c=l.rstrip('\n').split('|'); OWN[norm(n)]=(o,c)
REG={}  # brand register additions
def tier_for(own,cat=None,y=None):
    if not own or own=='Independent': return 'Independent' if own else None
    if own in GLOBAL: return 'Global group'
    return cat or 'Independent'
VER={}
for l in open('verified.txt'):
    p=(l.rstrip('\n').split('|')+['','','','',''])[:5]
    VER.setdefault(norm(p[0]),(p[1],p[3],p[4]))
def market(e,name=None,mk=None,own=None,cty=None,craft=False,nat=False,y=None):
    c=None;vk=None
    for key in (name or e['n'],mk or e.get('mk','')):
        if key and norm(key) in OWN and c is None: c=OWN[norm(key)][1]
        if key and norm(key) in VER and vk is None: vk=VER[norm(key)]
    cty=cty or c
    if own:
        e['own']=own; e['os']=e.get('s','')
    elif vk:
        e['own']=vk[0]; e['os']=vk[1]
        if vk[2]: e['own_y']=int(vk[2])
    if e.get('own'):
        REG[e['own']]=cty
    if nat: e['_nat']=1
    if cty: e['cty']=cty
    return e
STATS=collections.Counter(); DROP=collections.defaultdict(list)
def new(n,d,s,mk='',y='',g='',a='',**mkw):
    e={'n':n,'a':a,'d':d,'mk':mk,'y':str(y),'s':s}
    if g: e['g']=g
    return market(e,**mkw)
def merge(kind,newe,oldx,oldm,defg=''):
    """newe: list of new canonical entries; oldx: old entries; oldm: old models. Old entries matching a new one become versions/merged."""
    byn={norm(e['n']):e for e in newe}
    keys=sorted(byn,key=lambda k:-len(k))
    out=list(newe)
    def find(name,mk=''):
        nn=norm(name)
        if nn in byn: return byn[nn],True
        for k in keys:
            if k and (nn.startswith(k+' ') or (mk and norm(mk)==k)): return byn[k],False
        return None,False
    for o in oldx:
        t,exact=find(o['n'],o.get('mk',''))
        if t is None:
            o=copy.deepcopy(o); 
            if defg: o['g']=defg
            market(o); out.append(o); STATS['old kept as entry']+=1
        elif exact:
            for f in('d','a','dt','role'):
                if o.get(f) and (f!='d' or len(t['d'])<45 or True): t[f]=o[f] if f!='d' else t['d'] if False else o[f]
            t.setdefault('v',[]); t['v']+= [v for v in o.get('v',[]) if v['n'] not in [x['n'] for x in t['v']]]
            if o.get('s') and 'wikipedia' not in o['s']: pass
            STATS['old merged into list entry']+=1
        else:
            v={'n':o['n'],'mk':o.get('mk',''),'y':'','d':o.get('d','')[:80]}
            t.setdefault('v',[])
            if v['n'] not in [x['n'] for x in t['v']]: t['v'].append(v)
            for x in o.get('v',[]):
                if x['n'] not in [y['n'] for y in t['v']]: t['v'].append(x)
            STATS['old became version']+=1
    for m in oldm:
        t,exact=find(m[0],m[1] if len(m)>1 else '')
        if t is None: DROP[kind].append(m[0]); STATS['model dropped']+=1
        else:
            t.setdefault('v',[]); 
            if m[0] not in [x['n'] for x in t['v']]: t['v'].append({'n':m[0],'mk':m[1] if len(m)>1 else '','y':'','d':''}); STATS['model became version']+=1
    return out
def K(name,nl,sel,xg,entries,src=None,d=None,old=None,a=None,tt=True,r=True):
    o=oldk.get(old or name,{})
    k={'n':name,'a':a if a is not None else o.get('a',''),'d':d or o.get('d',''),'s':src or o.get('s',''),'nl':nl,'sel':sel}
    if xg: k['xg']=xg
    if o.get('tt') and tt: k['tt']=o['tt']
    if o.get('see'): k['see']=o['see']
    if o.get('r') and r: k['r']=o['r']
    if entries: k['x']=entries
    return k
def oldx(name): return oldk.get(name,{}).get('x',[])
def oldm(name): return oldk.get(name,{}).get('m',[])
def sortg(es,order=None):
    return es
RES=lambda s:s
# ---------- WHISKY ----------
SCOT=[l.split('|') for l in open('scot.txt').read().splitlines()]
def scot_owner(o):
    return {'Chivas Brothers':'Pernod Ricard','John Dewar & Sons':'Bacardi Limited','Nikka Whisky Distilling Co Ltd':'Nikka Whisky Distilling Co Ltd'}.get(o,o)
def scotch_entries(region):
    es=[]
    for n,r,o,y in SCOT:
        if r!=region: continue
        own=scot_owner(o); y=int(y)
        e=new(n,f"{region if region!='Island' else 'Island'} malt distillery, founded {y}; owned by {own}.",WIKI+'List_of_whisky_distilleries_in_Scotland',mk=n,y=str(y)+' (distillery)',own=own,cty='Scotland',craft=(y>=2000 and own not in GLOBAL))
        e['g']='Founded before 1900' if y<1900 else ('Founded 1900–1999' if y<2000 else 'Founded 2000 onwards')
        es.append(e)
    es.sort(key=lambda e:({'Founded before 1900':0,'Founded 1900–1999':1,'Founded 2000 onwards':2}[e['g']],int(e['y'][:4]),e['n']))
    return es
SMSEL="Every malt whisky distillery of the region in Wikipedia's List of whisky distilleries in Scotland (operating, newly built and announced, 2026 edition); core bottlings from the earlier edition are versions."
NLD="One entry is a malt whisky distillery; its core bottlings are versions."
reg_kinds=[('Islay single malt Scotch','Islay'),('Speyside single malt Scotch','Speyside'),('Highland single malt Scotch','Highland'),('Island single malt Scotch','Island'),('Campbeltown single malt Scotch','Campbeltown'),('Lowland single malt Scotch','Lowland')]
def regkind(name,region):
    ne=scotch_entries(region)
    es=merge(name,ne,oldx(name),oldm(name),'Founded 2000 onwards' if False else 'Other brands')
    es=[e for e in es]
    return K(name,NLD,SMSEL,'by founding period',es,src=WIKI+'List_of_whisky_distilleries_in_Scotland')
shelf1={'n':'Single malt Scotch by region','t':oldd['Whisky']['s'][0]['t'],'ax':oldd['Whisky']['s'][0]['ax'],'k':[regkind(a,b) for a,b in reg_kinds]}
ib=oldk['Independent bottlings of Scotch single malt']
ibx=[]
for e in ib['x']:
    e=copy.deepcopy(e); market(e); e['g']='Independent bottlers'; ibx.append(e)
shelf1['k'].append(K('Independent bottlings of Scotch single malt',"One entry is an independent bottler that buys casks and bottles single malt under its own name; its ranges are versions.","The independent bottlers already sourced in the previous edition; no whole-space reference list was fetched.",'',ibx,old='Independent bottlings of Scotch single malt'))
# blended & grain
bl_old=oldx('Blended Scotch whisky')
bl=[]
for e in bl_old:
    e=copy.deepcopy(e); market(e,nat=False); e['g']='Blended Scotch brands'; bl.append(e)
bl_models=oldm('Blended Scotch whisky')
for m in bl_models:
    STATS['model dropped']+=1; DROP['Blended Scotch whisky'].append(m[0])
shelf2={'n':'Blended & grain Scotch whisky','t':oldd['Whisky']['s'][1]['t'],'ax':oldd['Whisky']['s'][1]['ax'],'k':[
 K('Blended Scotch whisky',"One entry is a blended Scotch brand sold under its own name; age statements and special editions are versions.","The blended brands sourced in the previous edition and the owners' brand pages; Wikipedia has no complete list of blended Scotch brands.",'by owner group',bl,r=True),
 K('Blended malt Scotch whisky',"One entry is a blended malt brand, a blend of single malts from several distilleries; its age statements are versions.","The blended malt brands sourced in the previous edition; no complete reference list was found.",'',[market(copy.deepcopy(e)) for e in oldx('Blended malt Scotch whisky')]),
 K('Single grain Scotch whisky',"One entry is a Scotch grain whisky distillery, or a single-grain brand from one.","Every grain whisky distillery in Wikipedia's List of whisky distilleries in Scotland.",'by founding period',
   [dict(new(n,f"Grain whisky distillery at {loc}, founded {y}; owned by {o}.",WIKI+'List_of_whisky_distilleries_in_Scotland',mk=n,y=y+' (distillery)',own=o if o!='Pernod Ricard (Chivas Brothers)' else 'Pernod Ricard',cty='Scotland'),g='Founded before 1900' if int(y)<1900 else 'Founded 1900–1999' if int(y)<2000 else 'Founded 2000 onwards') for n,loc,o,y in (l.split('|') for l in GRAIN.splitlines())]+[market(copy.deepcopy(e)) for e in oldx('Single grain Scotch whisky')]),
 K('Blended grain Scotch whisky',"One entry is a blend of grain whiskies from several distilleries, sold under its own name.","The blended grain brand sourced in the previous edition.",'',[market(copy.deepcopy(e)) for e in oldx('Blended grain Scotch whisky')]),
]}
# American
def bourbon_entries():
    es=[]
    for l in BOURBON.splitlines():
        n,dist,own=l.split('|')
        es.append(new(n,f"Bourbon brand made at {dist}; owner {own}.",WIKI+'List_of_bourbon_brands',mk=own,own=own,cty='United States',g=dist,craft=False))
    return es
bo=bourbon_entries()
ao=oldx('Bourbon')
bx=merge('Bourbon',bo,ao,oldm('Bourbon'),'Other distilleries')
bk=K('Bourbon',"One entry is a bourbon brand sold under its own name; age statements, proof and single-barrel editions are versions.","Every brand in Wikipedia's List of bourbon brands (first 100,000 characters read), grouped by producing distillery; brands from the previous edition not on that list are in 'Other distilleries'.",'by producing distillery',bx,src=WIKI+'List_of_bourbon_brands')
def plain(name,nl,sel,g='Brands'):
    es=[]
    for e in oldx(name):
        e=copy.deepcopy(e); market(e); e['g']=g; es.append(e)
    for m in oldm(name): DROP[name].append(m[0]); STATS['model dropped']+=1
    return K(name,nl,sel,'',es)
am=[bk,
 plain('Tennessee whiskey',"One entry is a Tennessee whiskey brand; age and barrel-proof editions are versions.","The brands sourced in the previous edition; no complete list was fetched."),
 plain('Rye whiskey',"One entry is a rye whiskey brand; age and barrel-proof editions are versions.","The brands sourced in the previous edition; no complete list was fetched."),
 plain('Wheat whiskey',"One entry is a wheat whiskey brand.","The brands sourced in the previous edition; no complete list was fetched."),
 plain('Corn whiskey',"One entry is a corn whiskey brand.","The brands sourced in the previous edition; no complete list was fetched."),
 plain('American single malt whiskey',"One entry is an American single malt distillery or brand.","The brands sourced in the previous edition; no complete list was fetched."),
 plain('Blended American whiskey',"One entry is a blended American whiskey brand.","None sourced yet; the kind is kept for the category.")]
shelf3={'n':'American whiskey','t':oldd['Whisky']['s'][2]['t'],'ax':oldd['Whisky']['s'][2]['ax'],'k':am}
# Irish
iro=[]
for n,loc,o,y in (l.split('|') for l in IRISH_OP.splitlines()):
    own='Independent' if o=='Independent' else o
    e=new(n,f"Irish whiskey distillery at {loc}, opened {y}"+(f"; owned by {o}." if o!='Independent' else "; independently owned."),WIKI+'List_of_whiskey_distilleries_in_Ireland',mk=n,y=y+' (distillery)',cty='Ireland',g='Operating distilleries')
    if o!='Independent':
        e['own']=o; e['tier']='Global group' if o in GLOBAL else 'Independent'
    else: e['tier']='Craft & indie' if int(y)>=2000 else 'Independent'
    iro.append(e)
for n,f,c in (l.split('|') for l in IRISH_CL.splitlines()):
    e=new(n,f"Closed Irish distillery, working {f}–{c}.",WIKI+'List_of_whiskey_distilleries_in_Ireland',mk=n,y=f+' (distillery)',cty='Ireland',g='Closed distilleries'); iro.append(e)
irx=merge('Irish whiskey',iro,oldx('Irish whiskey'),oldm('Irish whiskey'),'Brands')
irk=K('Irish whiskey',"One entry is an Irish whiskey distillery, operating or closed, or a brand sold under its own name; core bottlings are versions.","Every distillery in Wikipedia's List of whiskey distilleries in Ireland (47 operating, 22 closed), plus brands from the previous edition.",'by status',irx,src=WIKI+'List_of_whiskey_distilleries_in_Ireland')
shelf4={'n':'Irish whiskey','t':oldd['Whisky']['s'][3]['t'],'ax':oldd['Whisky']['s'][3]['ax'],'k':[plain('Irish single pot still whiskey',"One entry is a single pot still brand; age and cask editions are versions.","The brands sourced in the previous edition; no complete list was fetched."),irk]}
# Japanese etc
jo=[]
for n,o,loc,y in (l.split('|') for l in JAPAN.splitlines()):
    own={'Suntory':'Suntory Global Spirits'}.get(o,o)
    closed=y.startswith('closed')
    g='Established before 2008' if y=='pre-2008' else ('Closed' if closed else 'Opened or restarted from 2008')
    e=new(n,f"Japanese whisky distillery in {loc}"+(f", {y}" if y and y!='pre-2008' else '')+f"; operated by {o}.",WIKI+'Japanese_whisky',mk=n,y='' if y=='pre-2008' else y,cty='Japan',g=g,own=own)
    if own not in GLOBAL: e['tier']='Independent' if y=='pre-2008' or closed else 'Craft & indie'
    jo.append(e)
jx=merge('Japanese whisky',jo,oldx('Japanese whisky'),oldm('Japanese whisky'),'Brands')
jk=K('Japanese whisky',"One entry is a Japanese whisky distillery, or a brand sold under its own name; its core bottlings are versions.","Every distillery in the operating, restarted, closed and planned tables of Wikipedia's Japanese whisky article (first 100,000 characters read; planned sites left out).",'by period',jx,src=WIKI+'Japanese_whisky')
co=[]
for n,loc,o,br in (l.split('|') for l in CANADA.splitlines()):
    e=new(n,f"Canadian whisky distillery at {loc}; brands: {br}.",WIKI+'Canadian_whisky',mk=n,cty='Canada',own=o or None,g='Distilleries'); 
    for b in br.split('; '):
        e.setdefault('v',[]).append({'n':b,'mk':n,'y':'','d':''})
    if not o: e['tier']='Independent'
    co.append(e)
cx=merge('Canadian whisky',co,oldx('Canadian whisky'),oldm('Canadian whisky'),'Brands')
ck=K('Canadian whisky',"One entry is a Canadian whisky distillery; the brands it makes are versions.","Every distillery in Wikipedia's Canadian whisky article; brands from the previous edition without a listed distillery are separate entries.",'by kind of entry',cx,src=WIKI+'Canadian_whisky')
wk=plain('World whisky',"One entry is a whisky distillery outside Scotland, Ireland, the United States, Japan and Canada, or its brand.","The distilleries sourced in the previous edition; no whole-space list was fetched.",'Distilleries and brands')
shelf5={'n':'Japanese, Canadian & world whisky','t':oldd['Whisky']['s'][4]['t'],'ax':oldd['Whisky']['s'][4]['ax'],'k':[jk,ck,wk]}
whisky={'n':'Whisky','mode':'variety','t':oldd['Whisky']['t'],'ax':'Which category or legal style is it: Scotch by region, blended Scotch, Bourbon and Tennessee, Irish, Japanese, Canadian or world whisky?','note':'Category first; distillery or brand as the entry; core expressions as versions; owner group and tier on every entry.','b':oldd['Whisky']['b'],'s':[shelf1,shelf2,shelf3,shelf4,shelf5]}
# ---------- other departments (helper) ----------
def dept(n,t,ax,note,b,shelves,ms=None):
    d={'n':n,'mode':'variety','t':t,'ax':ax,'note':note,'b':b,'s':shelves}
    if ms: d['ms']=ms
    return d
SB=oldd['Spirits']['b']
def listed(prefix_name,items,src,desc,g,cty=None):
    return [new(n,desc.format(n=n,g=g),src,mk=n,g=g,cty=cty) for n in items]
# ---- brandy
cog=[]
for n,o in [('Hennessy','LVMH'),('Martell','Pernod Ricard'),('Rémy Martin','Rémy Cointreau'),('Courvoisier','Campari')]:
    cog.append(new(n,f"Cognac house; owned by {o}.",W+'Cognac',mk=n,cty='France',own=o,g='Houses with a stated owner'))
for n in ['Bache-Gabrielsen/Dupuy','Braastad','Camus','La Fontaine de La Pouyade','Château Fontpinot','Delamain','Pierre Ferrand','Frapin','Gautier','Hine','Marcel Ragnaud','Monnet','Moyet','Otard','Meukow','Croizet']:
    e=new(n,"Cognac house named in Wikipedia's Cognac article; no owner stated there.",W+'Cognac',mk=n,cty='France',g='Other houses named')
    market(e); cog.append(e)
for n in ['Ferrand','Vallein Tercinier','Bourgoin','Rémi Landier','François Voyer']:
    cog.append(new(n,"Cognac house named in whisky.fr's list of great houses; no owner stated there.",'https://www.whisky.fr/en/menu/blog/articles-cognac/great-cognac-houses',mk=n,cty='France',g='Other houses named'))
cogx=merge('Cognac',cog,oldx('Cognac'),oldm('Cognac'),'Other houses named')
for e in cogx:
    if e['n'] in('Hennessy','Martell','Rémy Martin','Courvoisier'): e['tier']='Global group'
cogk=K('Cognac',"One entry is a Cognac house; age grades and named blends are versions.","Every house named in Wikipedia's Cognac article and whisky.fr's list of great houses; Wikipedia has no complete list of Cognac houses.",'by owner stated',cogx,src=W+'Cognac')
crus=[('Grande Champagne','13,766 ha'),('Petite Champagne','16,171 ha'),('Borderies','4,160 ha'),('Fins Bois','34,265 ha'),('Bons Bois','combined with Bois Ordinaires, 19,979 ha'),('Bois Ordinaires','combined with Bons Bois, 19,979 ha')]
crk=K('Cognac cru',"One entry is one of the delimited Cognac growing areas; the age grades are versions of the house blends and are not repeated here.","The crus listed in Wikipedia's Cognac article, with the area it gives.",'',
 [new(n,f"Cognac growing area, {a}.",W+'Cognac',cty='France') for n,a in crus],src=W+'Cognac',d='A delimited Cognac growing area.',a='Cognac growing areas',tt=False)
for e in crk['x']: e['v']=[]
agk=K('Armagnac',"One entry is an Armagnac area or producer; vintage and age grades are versions.","The three areas of Wikipedia's Armagnac article plus producers sourced in the previous edition; the article names no houses.",'',
  [new('Bas-Armagnac',"Armagnac area producing about 62 % of Armagnac.",W+'Armagnac_(brandy)',cty='France',g='Areas'),new('Armagnac-Ténarèze',"Armagnac area producing about 37 % of Armagnac.",W+'Armagnac_(brandy)',cty='France',g='Areas'),new('Haut-Armagnac',"Armagnac area producing about 1 % of Armagnac.",W+'Armagnac_(brandy)',cty='France',g='Areas')]+merge('Armagnac',[],oldx('Armagnac'),oldm('Armagnac'),'Producers'),src=W+'Armagnac_(brandy)')
cal=K('Calvados',"One entry is a Calvados appellation or producer.","The three AOCs of Wikipedia's Calvados article plus producers sourced in the previous edition.",'',
  [new('AOC Calvados',"Broadest Calvados appellation, covering Calvados, Manche and Orne and parts of four other departments.",W+'Calvados_(brandy)',cty='France',g='Appellations'),new('AOC Calvados Pays d\'Auge',"Most restrictive Calvados appellation, in the east of the Calvados department and nearby districts.",W+'Calvados_(brandy)',cty='France',g='Appellations'),new('AOC Calvados Domfrontais',"Calvados appellation requiring at least 30 % pears.",W+'Calvados_(brandy)',cty='France',g='Appellations')]+[e for e in merge('Calvados',[],oldx('Calvados'),oldm('Calvados'),'Producers') if not e['n'].lower().startswith(('calvados','aoc'))],src=W+'Calvados_(brandy)')
pis=K('Pisco',"One entry is a pisco type or producer; vintages are versions.","The Peruvian types and Chilean producers in Wikipedia's Pisco article; the article links to a list of piscos that was not fetched.",'by country',
  [new('Pisco puro',"Peruvian pisco from a single grape variety, mostly Quebranta.",W+'Pisco',cty='Peru',g='Peru'),new('Pisco aromático',"Peruvian pisco from Muscat or Muscat-derived grapes.",W+'Pisco',cty='Peru',g='Peru'),new('Pisco mosto verde',"Peruvian pisco distilled from partially fermented must.",W+'Pisco',cty='Peru',g='Peru'),new('Pisco acholado',"Peruvian pisco blended from several grape varieties.",W+'Pisco',cty='Peru',g='Peru'),
   new('Capel',"Chilean pisco maker, Cooperativa Agrícola Pisquera Elqui Limitada.",W+'Pisco',mk='Capel',cty='Chile',g='Chile'),new('Pisco Aviador',"Chilean pisco brand.",W+'Pisco',cty='Chile',g='Chile'),new('Viña Ocucaje',"Peruvian pisco producer.",W+'Pisco',cty='Peru',g='Peru'),new('Efraín Wong',"Peruvian pisco producer.",W+'Pisco',cty='Peru',g='Peru')],src=W+'Pisco')
for m in oldm('Pisco'): DROP['Pisco'].append(m[0]); STATS['model dropped']+=1
bdk=[cogk,crk,agk,
 plain('Grape brandy',"One entry is a grape brandy brand.","The brands sourced in the previous edition; no complete list was fetched."),pis,
 plain('Grappa & pomace brandy',"One entry is a pomace brandy style or producer.","The entries sourced in the previous edition; no complete list was fetched."),cal,
 plain('Fruit brandy',"One entry is a fruit brandy style or producer.","The entries sourced in the previous edition; no complete list was fetched.")]
# fix Calvados/Armagnac leftovers: old Calvados entries shared names already
brandy=dept('Brandy','Spirits distilled from grape wine, grape pomace, apples or other fruit: Cognac, Armagnac, Calvados, pisco, grappa and fruit brandy; a sweetened one → Liqueurs.','Which protected brandy is it: Cognac, Armagnac, Calvados, pisco, another grape brandy, pomace brandy or fruit brandy?','Protected category or area first, then house or producer; age grades as versions.',[{'m':'Age grade','v':'VS < VSOP < XO','w':'The Cognac age grades in Wikipedia: VS at least 2 years, VSOP 4, Napoléon 6, XO 10.'}]+SB[:1],
  [{'n':'Cognac','t':'Brandy from the Cognac region, by cru and house.','ax':'kinds by area and house','k':[cogk,crk]},{'n':'Armagnac, Calvados & pisco','t':'Protected brandies of south-west France, Normandy and the Andes.','ax':'one kind per protected name','k':[agk,bdk[6],pis]},{'n':'Other brandy','t':'Grape, pomace and fruit brandies without a single protected name.','ax':'kinds by raw material','k':[bdk[3],bdk[5],bdk[7]]}])
# ---- rum
rum_e=[];agri=[]
for reg,cs in RUM.items():
    for c,names in cs.items():
        for n in names.split(';'):
            e=new(n,f"Rum brand or producer from {c}.",W+'List_of_rum_producers',mk=n,cty=c if c!='Several' else '',g=f"{reg}: {c}" if c!='Several' else 'Several countries')
            rum_e.append(e)
for n in MARTINIQUE.split(';'):
    agri.append(new(n,"Martinique rhum brand or distillery.",W+'List_of_rum_producers',mk=n,cty='Martinique',g='Martinique'))
for n in GUADELOUPE.split(';'):
    agri.append(new(n,"Guadeloupe rhum brand or distillery.",W+'List_of_rum_producers',mk=n,cty='Guadeloupe',g='Guadeloupe'))
rx=merge('Molasses rum',rum_e,oldx('Molasses rum'),oldm('Molasses rum'),'Other brands')
for e in rx:
    if e.get('own') in('Rémy Cointreau',) : pass
RUMNL="One entry is a rum brand or producer; age statements and editions are versions."
rumk=K('Molasses rum',RUMNL,"Every brand and producer in Wikipedia's List of rum producers outside Martinique and Guadeloupe (listed under Rhum agricole), by region and country.",'by region and country',rx,src=W+'List_of_rum_producers')
spk=plain('Spiced rum',RUMNL,"The brands sourced in the previous edition; no complete list was fetched.")
agx=merge('Rhum agricole',agri,oldx('Rhum agricole'),oldm('Rhum agricole'),'Other')
agrk=K('Rhum agricole',"One entry is a rhum brand or distillery of Martinique or Guadeloupe; age grades are versions.","The Martinique and Guadeloupe entries of Wikipedia's List of rum producers; the AOC Martinique rhum agricole is named in the previous edition only.",'by island',agx,src=W+'List_of_rum_producers')
cach=plain('Cachaça',"One entry is a cachaça brand; ageing and editions are versions.","The brands sourced in the previous edition; no complete list was fetched.")
ague=plain('Aguardiente',"One entry is an aguardiente brand.","None sourced yet; the kind is kept for the category.")
arr=plain('Arrack',"One entry is an arrack style or brand.","The styles sourced in the previous edition.")
rumdept=dept('Rum & cane spirits','Spirits distilled from sugar cane juice, syrup or molasses: rum, rhum agricole, cachaça, aguardiente and arrack.','What is it distilled from and where: molasses rum, spiced rum, cane-juice rhum or cachaça?','Region and country first; brand or producer as the entry.',SB[:1],
  [{'n':'Rum','t':'Rum from molasses or syrup, plain or spiced, by region.','ax':'kinds by whether spices are added','k':[rumk,spk]},{'n':'Cane juice and other cane spirits','t':'Spirits from fresh cane juice or sugar cane in the French islands, Brazil, Latin America and Asia.','ax':'kinds by tradition','k':[agrk,cach,ague,arr]}])
# ---- agave
tq=[]
for l in TEQUILA.splitlines():
    n,y=l.split('|')
    tq.append(new(n,"Tequila brand"+(f"; production began {y}." if y else "."),W+'List_of_tequilas',mk=n,y=y,cty='Mexico'))
tqx=merge('Tequila',tq,oldx('Tequila'),oldm('Tequila'),'Other brands')
tqk=K('Tequila',"One entry is a tequila brand sold under its own name; blanco, reposado and añejo expressions are versions.","Every brand in Wikipedia's List of tequilas, which is partial; brands from the previous edition are added. The NOM distillery register was not fetched.",'',tqx,src=W+'List_of_tequilas')
mzx=[new('Mezcal',"Certification category for mezcal.",W+'Mezcal',cty='Mexico',g='NOM categories'),new('Mezcal artesanal',"Certification category: traditional, artisanal production.",W+'Mezcal',cty='Mexico',g='NOM categories'),new('Mezcal ancestral',"Certification category: ancestral production.",W+'Mezcal',cty='Mexico',g='NOM categories')]
mz=merge('Mezcal',mzx+[new('Pierde Almas',"Mezcal brand founded by Jonathan Barbeiri.",W+'Mezcal',cty='Mexico',g='Brands'),new('Macario Partida distilleries',"Mezcal distilleries at Zapotitlán de Vadillo, Jalisco.",W+'Mezcal',cty='Mexico',g='Brands')],oldx('Mezcal'),oldm('Mezcal'),'Brands')
mzk=K('Mezcal',"One entry is a mezcal certification category or brand; classes (joven, reposado, añejo) are versions.","The three NOM categories and brands in Wikipedia's Mezcal article (first 100,000 characters read), plus brands from the previous edition.",'by kind of entry',mz,src=W+'Mezcal')
agt=K('Mezcal agave',"One entry is an agave species used for mezcal.","The agave types in Wikipedia's Mezcal article.",'',[new(n,f"Agave used for mezcal ({sp}).",W+'Mezcal',cty='Mexico') for n,sp in [('Espadín','Agave angustifolia, the most common'),('Arroqueño','Agave americana var. oaxacensis'),('Cirial','Agave karwinskii'),('Barril','Agave rodacantha'),('Mexicano','Agave macroacantha or rhodacantha'),('Cincoañero','Agave canatala'),('Tobalá','Agave potatorum, a famous wild agave'),('Madrecuixe','agave type named in the article'),('Tepeztate','agave type named in the article'),('Jabalí','agave type named in the article'),('Bicuixe','agave type named in the article')]],src=W+'Mezcal',d='Agave species named on mezcal labels.',a='mezcal agave types',tt=False)
for e in agt['x']: e['v']=[]
agave=dept('Agave','Spirits distilled from agave: tequila, mezcal, raicilla, bacanora and sotol.','Which agave spirit is it: tequila, mezcal or another desert-plant spirit?','Protected name first; brand as the entry; class as version.',SB[:1],
  [{'n':'Tequila','t':'Spirit from blue agave in the tequila region.','ax':'one kind','k':[tqk]},{'n':'Mezcal and other agave spirits','t':'Mezcal by category and agave, raicilla, bacanora and sotol.','ax':'kinds by name','k':[mzk,agt,plain('Raicilla',"One entry is a raicilla brand.","None sourced yet; the kind is kept for the category."),plain('Bacanora',"One entry is a bacanora brand.","None sourced yet; the kind is kept for the category."),plain('Sotol',"One entry is a sotol brand.","None sourced yet; the kind is kept for the category.")]}])
# ---- gin vodka aquavit
vx=[]
for c,ns in VODKA.items():
    for n in ns.split(';'):
        vx.append(new(n,f"Vodka brand from {c}.",W+'List_of_vodkas',mk=n,cty=c,g=c))
vx=merge('Vodka',vx,oldx('Vodka'),oldm('Vodka'),'Other brands')
vk=K('Vodka',"One entry is a vodka brand sold under its own name; flavours and sizes are versions.","Every brand in Wikipedia's List of vodkas (alphabetical by country), plus brands from the previous edition.",'by home country',vx,src=W+'List_of_vodkas')
fvx=plain('Flavoured vodka',"One entry is a flavoured vodka sold under its own name.","The vodkas sourced in the previous edition.")
gx=[new(n,f"Gin brand from {c}.",W+'List_of_gins',mk=n,cty=c,g=c) for n,c in (l.split('|') for l in GIN.splitlines())]
gx=merge('Gin',gx,oldx('Gin'),oldm('Gin'),'Other brands')
gk=K('Gin',"One entry is a gin brand sold under its own name; strengths and editions are versions.","Every brand in Wikipedia's List of gins (first 100,000 characters read), plus brands from the previous edition.",'by home country',gx,src=W+'List_of_gins')
gen=plain('Genever',"One entry is a genever style or brand.","The styles sourced in the previous edition.")
aq=plain('Aquavit',"One entry is an aquavit brand.","The brands sourced in the previous edition; Wikipedia's Aquavit article names none.")
ginv=dept('Gin, vodka & aquavit','Spirits distilled from grain or potato, plain or flavoured with botanicals: vodka, gin, genever and aquavit.','Which neutral or botanical spirit is it: vodka, flavoured vodka, gin, genever or aquavit?','Style first; brand as the entry; owner group and tier on each.',SB[:1],
  [{'n':'Vodka','t':'Neutral grain or potato spirit, plain or flavoured.','ax':'kinds by flavouring','k':[vk,fvx]},{'n':'Gin, genever & aquavit','t':'Spirits flavoured with juniper or caraway.','ax':'kinds by botanical','k':[gk,gen,aq]}])
# ---- anise & absinthe
anise=dept('Anise & absinthe','Spirits flavoured with aniseed, fennel or wormwood: pastis, ouzo, arak, rakı and absinthe.','Where is it from and what is it flavoured with: French pastis, Greek ouzo, Levantine arak, Turkish rakı or absinthe?','Style first; brand as the entry.',SB[:1],
  [{'n':'Anise spirits & absinthe','t':oldd['Spirits']['s'][3]['t'],'ax':oldd['Spirits']['s'][3]['ax'],'k':[plain('Pastis',"One entry is a pastis brand.","The brands sourced in the previous edition; no complete list was fetched."),plain('Ouzo',"One entry is an ouzo brand.","The brands sourced in the previous edition; no complete list was fetched."),plain('Arak & rakı',"One entry is an arak or rakı brand.","The brands sourced in the previous edition; no complete list was fetched."),plain('Absinthe',"One entry is an absinthe brand; verte and blanche are versions.","The brands sourced in the previous edition; the planned Wikipedia list of absinthe brands was not found.")]}])
# ---- asian
bt=K('Baijiu aroma type',"One entry is a baijiu aroma type; the brands named for it are versions.","The aroma types in Wikipedia's Baijiu article, with the example brands it gives.",'',
  [dict(new(n,"Baijiu aroma type."+(f" Example brands: {b}." if b else ' No brand named in the article.'),W+'Baijiu',cty='China'),v=[{'n':x.strip(),'mk':'','y':'','d':''} for x in b.split(';') if x.strip()]) for n,b in BAIJIU_TYPES],src=W+'Baijiu',d='A baijiu style defined by its aroma.',a='baijiu aroma types',tt=False)
bjx=[]
for n,o in BAIJIU:
    e=new(n,f"Baijiu brand from {o}.",W+'Baijiu',mk=n,cty='China',g='Brands')
    bjx.append(e)
bjx=merge('Baijiu',bjx,oldx('Baijiu'),oldm('Baijiu'),'Brands')
for e in bjx:
    if e['n'] in('Kweichow Moutai','Wuliangye','Luzhou Laojiao'): e['tier']='National champion'
bjk=K('Baijiu',"One entry is a baijiu brand sold under its own name; vintages and strengths are versions.","The brand table in Wikipedia's Baijiu article (first 100,000 characters read), plus brands from the previous edition.",'',bjx,src=W+'Baijiu')
shx=merge('Shochu',[new(n,f"Shōchū type from {r}; base ingredient {b}.",W+'Shōchū',cty='Japan',g='Regional types') for n,b,r in [('Satsuma shōchū','sweet potato','Kagoshima'),('Kuma shōchū','rice','Hitoyoshi-bonchi, Kumamoto'),('Iki shōchū','barley','Iki, Nagasaki'),('Ryūkyū awamori','rice','Okinawa'),('Amami kokutō shōchū','brown sugar','the Amami Islands'),('Soba shōchū','buckwheat','Miyazaki'),('Kasutori shōchū','sake lees','northern Kyūshū')]],oldx('Shochu'),oldm('Shochu'),'Producers')
shk=K('Shochu',"One entry is a regional shōchū type or a producer; bottlings are versions.","The seven regional types in Wikipedia's Shōchū article (first 100,000 characters read) plus producers from the previous edition.",'by kind of entry',shx,src=W+'Shōchū')
awk=plain('Awamori',"One entry is an awamori brand.","None sourced yet; the previous edition held only models.")
sjx=merge('Soju',[new('Jinro',"Largest soju maker; reported as the world's best-selling branded spirit in 2019.",W+'Soju',mk='HiteJinro',cty='South Korea',own='HiteJinro',g='Makers',a='HiteJinro'),new('Chum-Churum',"Soju brand of Lotte Chilsung.",W+'Soju',mk='Lotte Chilsung',cty='South Korea',own='Lotte Chilsung',g='National brands'),new('Good Day',"Soju brand of Muhak, popular in South Gyeongsang and Ulsan.",W+'Soju',mk='Muhak',cty='South Korea',own='Muhak',g='Regional brands'),new('Cham',"Soju brand from Daegu.",W+'Soju',mk='Kumbokju',cty='South Korea',g='Regional brands'),new('Pureun-bam',"Soju brand from Jeju.",W+'Soju',mk='Jeju-soju',cty='South Korea',g='Regional brands'),new('Hwayo',"Distilled soju sold in five mixes, 17 to 53 % ABV.",W+'Soju',cty='South Korea',g='Distilled soju'),new('Andong Soju',"Traditionally distilled soju from Andong.",W+'Soju',cty='South Korea',g='Distilled soju'),new('Tokki Soju',"United States soju brand.",W+'Soju',cty='United States',g='Made outside Korea'),new('West 32',"United States soju brand.",W+'Soju',cty='United States',g='Made outside Korea'),new('Yong Soju',"Soju brand of Minhwa Spirits, Georgia, United States.",W+'Soju',cty='United States',g='Made outside Korea'),new('ISAE',"Soju brand of Kyopo Spirits, Germany.",W+'Soju',cty='Germany',g='Made outside Korea')],oldx('Soju'),oldm('Soju'),'Other brands')
for e in sjx:
    if e['n']=='Jinro': e['role']='landmark'; e['tier']='National champion'; e['own']='HiteJinro'
    if e['n']=='Chum-Churum': e['tier']='National champion'
sjk=K('Soju',"One entry is a soju brand or maker; flavours and strengths are versions.","The brands and makers named in Wikipedia's Soju article, plus brands from the previous edition.",'',sjx,src=W+'Soju')
SOJU_MS=[{"mkt":"South Korean soju","who":"HiteJinro","share":"almost half of the market","yr":2023,"s":W+'Soju',"note":"as of October 2023, per the article; four smaller companies together hold about 40 %"}]
asian=dept('Asian spirits','Spirits distilled from rice, sorghum and other grains in China, Japan and Korea: baijiu, shōchū, awamori and soju.','Where and from what: Chinese sorghum baijiu, Japanese shōchū and awamori, or Korean soju?','Aroma type or regional type first; brand as the entry.',SB[:1],
  [{'n':'China','t':'Chinese grain spirit sold by aroma type.','ax':'kinds by aroma and brand','k':[bt,bjk]},{'n':'Japan and Korea','t':'Japanese shōchū and awamori and Korean soju.','ax':'kinds by country','k':[shk,awk,sjk]}],ms=SOJU_MS)
# ---- liqueurs
def liqkind(name,nl):
    names=LIQ.get(name,'').split(';') if LIQ.get(name) else []
    es=[new(n,f"{name.capitalize() if False else 'Liqueur'} named in Wikipedia's List of liqueurs.",W+'List_of_liqueurs',mk=n,g='Brands and styles') for n in names]
    es=merge(name,es,oldx(name),oldm(name),'Brands and styles')
    return K(name,nl,"Every matching entry of Wikipedia's List of liqueurs (sections mapped to this kind), plus brands from the previous edition.",'',es,src=W+'List_of_liqueurs')
LNL="One entry is a liqueur brand or traditional style sold under its own name; flavours and strengths are versions."
LQ={n:liqkind(n,LNL) for n in LIQ}
for k in LQ.values():
    for e in k.get('x',[]):
        if 'List of liqueurs' in e['d']: e['d']=f"{k['n']} named in Wikipedia's List of liqueurs."
liq=dept('Liqueurs',oldd['Liqueurs']['t'],oldd['Liqueurs']['ax'],'Flavour family first; brand as the entry; owner group on each.',oldd['Liqueurs']['b'],
 [{'n':'Fruit & flower liqueurs','t':oldd['Liqueurs']['s'][0]['t'],'ax':oldd['Liqueurs']['s'][0]['ax'],'k':[LQ[n] for n in('Orange liqueur','Limoncello','Fruit liqueur','Sloe gin','Flower liqueur')]},
  {'n':'Herb, spice & bitter liqueurs','t':oldd['Liqueurs']['s'][1]['t'],'ax':oldd['Liqueurs']['s'][1]['ax'],'k':[LQ[n] for n in('Herb & spice liqueur','Anise liqueur','Amaro & bitter liqueur')]},
  {'n':'Cream, coffee & nut liqueurs','t':oldd['Liqueurs']['s'][2]['t'],'ax':oldd['Liqueurs']['s'][2]['ax'],'k':[LQ[n] for n in('Cream liqueur','Coffee liqueur','Nut liqueur','Chocolate liqueur','Honey liqueur','Whisky liqueur')]}])
depts=[whisky,brandy,rumdept,agave,ginv,anise,asian,liq]

GP={'Chivas Brothers':(W+'Pernod_Ricard',2001),'John Dewar & Sons':(W+'Bacardi',1998)}
for d in depts:
    for s_ in d['s']:
        for k in s_['k']:
            for e in k.get('x',[]):
                if e.get('own') in('Pernod Ricard','Bacardi Limited') and 'List_of_whisky_distilleries_in_Scotland' in e['s'] and e['y'].endswith('(distillery)'):
                    if e['own']=='Pernod Ricard': e['os']=W+'Pernod_Ricard'; e['own_y']=2001
                    else: e['os']=W+'Bacardi'; e['own_y']=1998
                e.pop('tier',None)
                if e.get('own'):
                    v=VER.get(norm(e['n']))
                    if v and v[0]==e['own']:
                        e['os']=v[1]
                        if v[2]: e['own_y']=int(v[2])
                    elif not e.get('os'): e['os']=e['s']
                if e.get('own') in GLOBAL: e['tier']='Global group'
                if e['n']=='Jinro': e['tier']='National champion'
                if not e.get('own') and 'independently owned' in e.get('d',''): e['tier']='Independent'; e['os']=e['s']
                if e.get('own')=='Independent': pass

# restore dropped models whose maker matches an existing entry
REST=collections.Counter(); STILL=collections.defaultdict(list)
allents=[(d['n'],k['n'],e) for d in depts for s_ in d['s'] for k in s_['k'] for e in k.get('x',[])]
for kind,names in DROP.items():
    mods={m[0]:m for m in oldk[kind].get('m',[])}
    kdept=[d['n'] for d in depts for s_ in d['s'] for k in s_['k'] if k['n']==kind][0]
    for nm in names:
        m=mods.get(nm); mk=m[1] if len(m)>1 else ''
        nn=norm(nm); tgt=None
        cands=[x for x in allents if x[0]==kdept]
        cands.sort(key=lambda x:(x[1]!=kind,-len(norm(x[2]['n']))))
        for dn,kn,e in cands:
            en=norm(e['n']); em=norm(e.get('mk',''))
            if len(en)>=3 and ((mk and norm(mk)==en) or (mk and em and norm(mk)==em and em!='') or nn.startswith(en+' ')):
                tgt=e;break
        if tgt is None: STILL[kind].append(nm+(' ('+mk+')' if mk else '')); continue
        v=tgt.setdefault('v',[])
        if nm not in [x['n'] for x in v]: v.append({'n':nm,'mk':mk,'y':'','d':'bottling'}); REST[kind]+=1
print('restored',sum(REST.values()),'still dropped',sum(len(v) for v in STILL.values()))
json.dump(STILL,open('still_dropped.json','w'),ensure_ascii=False,indent=0)
# dedupe entries by name within a kind; fill missing nl on kinds; ensure g on all entries of kinds with xg
for d in depts:
    for s in d['s']:
        for k in s['k']:
            seen={}
            xs=[]
            for e in k.get('x',[]):
                key=norm(e['n'])
                if key in seen: STATS['duplicate removed']+=1; continue
                seen[key]=1; xs.append(e)
            if xs: k['x']=xs
            elif 'x' in k: del k['x']
            for e in xs:
                if k.get('xg') and not e.get('g'): e['g']='Other'
brands=[]
for o,c in sorted(REG.items()):
    b={'n':o}
    if c: b['c']=c
    brands.append(b)
# move check: all old kinds
newk={k['n'] for d in depts for s in d['s'] for k in s['k']}
missing=[n for n in oldk if n not in newk]
renames={}
json.dump({'depts':depts,'brands':brands,'renames':renames,'moves':[]},open('/home/user/Possession-Taxonomy/rebuild/out/J7_parts/SPIRITS.json.tmp','w'),ensure_ascii=False,indent=1)
import os; os.replace('/home/user/Possession-Taxonomy/rebuild/out/J7_parts/SPIRITS.json.tmp','/home/user/Possession-Taxonomy/rebuild/out/J7_parts/SPIRITS.json')
print('missing old kinds:',missing)
print(dict(STATS)); print({k:len(v) for k,v in DROP.items()})
print('entries',sum(len(k.get('x',[])) for d in depts for s in d['s'] for k in s['k']))
json.dump(DROP,open('dropped_models.json','w'),ensure_ascii=False,indent=0)
