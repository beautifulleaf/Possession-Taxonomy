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
def market(e,name=None,mk=None,own=None,cty=None,craft=False,nat=False,y=None):
    o=c=None
    for key in (name or e['n'],mk or e.get('mk','')):
        if key and norm(key) in OWN: o,c=OWN[norm(key)]; break
    own=own or o; cty=cty or c
    if own:
        e['own']=own
        e['tier']='National champion' if nat else ('Global group' if own in GLOBAL else ('Craft & indie' if craft else 'Independent'))
        REG[own]=cty
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
    own={'Suntory':'Suntory Global Spirits','Nikka':'Asahi Group Holdings','Kirin':'Kirin Holdings'}.get(o,o)
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
  [{'n':'Cognac','t':'Brandy from the Cognac region, by cru and house.','ax':'kinds by area and house','k':[cogk,crk]},{'n':'Armagnac, Calvados & pisco','t':'Protected brandies of south-west France, Normandy and the Andes.','ax':'one kind per protected name','k':[agk,cal,pis]},{'n':'Other brandy','t':'Grape, pomace and fruit brandies without a single protected name.','ax':'kinds by raw material','k':[bdk[3-2],bdk[4+0],bdk[6]]}])
