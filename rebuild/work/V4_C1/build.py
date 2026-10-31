import json,re,os,collections
R='/home/user/Possession-Taxonomy/rebuild/'
W=R+'work/V4_C1/'
d=json.load(open(W+'bak/C1.json'))
dropped={'models_m':[],'entries_x':[]}
def D(n): return next(x for x in d['depts'] if x['n']==n)
def K(dn,kn):
    for s in D(dn)['s']:
        for k in s['k']:
            if k['n']==kn: return s,k
# --- log and remove all loose models
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            for m in k.pop('m',[]) or []: dropped['models_m'].append([dp['n'],k['n'],m])
# --- log and remove all named entries (rebuilt below for canon kinds)
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            if dp['n']!='Power tools' or k['n']!='Tool battery':
                for x in k.pop('x',[]) or []: dropped['entries_x'].append([dp['n'],k['n'],x['n']])
ARCHIVE=lambda x:x
# ================= PLANES =================
rows=[l.rstrip('\n').split('|',1) for l in open(W+'planes_raw.txt') if l.strip()]
PU='https://supertool.com/StanleyBG/stan%s.htm'
def frac(s): return s.replace('1/2','½').replace('1/4','¼').replace('3/4','¾')
def fr(s): return s.replace('1/2','½').replace('1/4','¼').replace('3/4','¾').replace('1/8','⅛').replace('3/8','⅜').replace('5/8','⅝').replace('7/8','⅞')
recs=[]
for pg,l in rows:
    m=re.match(r'#([AS]?)(\d+)(?: (\d/\d))?([A-Z]?)(?=[\s,])\s*,?\s*(.*)$',l)
    pre,num,fc,suf,rest=m.groups()
    rest=rest.strip()
    typ=re.split(r',\s*(?=\d|various|\(|width)|\s+(?=\d)',rest)[0]
    if re.match(r'^\d',typ): typ=''
    ln=re.search(r'(\d+(?: \d/\d)?)"?L\b',rest); ln=ln.group(1) if ln else ''
    ym=re.search(r'(\d{4})(?:\s*-\s*(\d{4}|\?))?\.?\s*\*?\s*$',rest)
    y1=ym.group(1) if ym else ''; y2=ym.group(2) if ym and ym.group(2) and ym.group(2)!='?' else ''
    yrs=(y1+('–'+y2 if y2 else '')) if y1 else ''
    recs.append(dict(pg=pg,pre=pre,num=int(num),fc=fc or '',suf=suf,typ=typ.rstrip('.,'),ln=fr(ln),yrs=yrs,y1=y1,key=(int(num),fc or '')))
groups=collections.OrderedDict()
for r in recs: groups.setdefault(r['key'],[]).append(r)
def label(r): 
    n=str(r['num'])+(' '+frac(r['fc']) if r['fc'] else '')
    return n.replace(' ½','½').replace(' ¼','¼').replace(' ¾','¾')
def kindof(num,fc,typ,hasdup):
    t=typ.lower(); n=num
    if 601<=n<=608 or 1<=n<=8 or 21<=n<=24 or 26<=n<=37 or n in(104,105,122,127,129,132,135,164,62): 
        if n==37: return 'Bench plane'
        return 'Bench plane'
    if 'block plane' in t or n==140: return 'Block plane'
    if 'scraper' in t or n==70: return 'Scraper'
    if 'cabinet makers' in t and 'rabbet' in t: return 'Shoulder plane'
    if 'tonguing' in t or 'match plane' in t: return 'Match and tonguing plane'
    if 'plow' in t or n==46: return 'Plough plane'
    if 'dado' in t: return 'Dado plane'
    if 'router' in t: return 'Router plane'
    if n in(45,55): return 'Combination plane'
    if 'beader' in t or 'beading' in t or 'corner rounding' in t: return 'Moulding plane'
    if 'rabbet' in t or 'filletster' in t: return 'Rebate plane'
    if 'scrub' in t: return 'Scrub plane'
    if 'circular' in t: return 'Circular plane'
    return 'Specialist plane'
def g_of(n):
    for lo,hi,lab in [(1,8,'Nos. 1–8 · Bailey bench planes'),(9,20,'Nos. 9–20 · early blocks and specials'),(21,37,'Nos. 21–37 · wood-bottomed bench planes'),(39,99,'Nos. 39–99 · joinery and specialist planes'),(100,299,'Nos. 100–299 · blocks, rabbets and scrapers'),(300,499,'Nos. 300–444 · late specials'),(601,608,'Nos. 601–608 · Bed Rock series')]:
        if lo<=n<=hi: return lab
    return ''
def lcfirst(s): return s[:1].lower()+s[1:] if s and not s[:2].isupper() else s
newk=collections.defaultdict(list)
for key,rs in groups.items():
    plain=[r for r in rs if not r['pre'] and not r['suf']]
    dup=len(plain)>1
    mains=plain if plain else rs[:1]
    for mr in mains:
        others=[r for r in rs if r is not mr and (r in plain and False or (r['pre'] or r['suf']))] if not dup else [r for r in rs if (r['pre'] or r['suf']) and (r['typ'].lower()[:6]==mr['typ'].lower()[:6] or (mr is mains[-1] and not any(r['typ'].lower()[:6]==q['typ'].lower()[:6] for q in mains)))]
        typ=mr['typ'] or (others[0]['typ'] if others else 'plane')
        nm='Stanley No. '+label(mr)
        if dup: nm+=' ('+typ.lower()+')'
        kd=kindof(mr['num'],mr['fc'],typ,dup)
        sent=f"Stanley {lcfirst(typ)}"+(f", {mr['ln']} in long" if mr['ln'] else '')+(f", made {mr['yrs']}" if mr['yrs'] else '')+'.'
        e={'n':nm,'d':sent,'mk':'Stanley','y':mr['y1'],'s':PU%mr['pg'],'g':g_of(mr['num'])}
        vs=[]
        for o in others:
            t=o['typ'] or typ
            vs.append({'n':'No. '+(o['pre']+label(o)+o['suf']) if o['pre'] else 'No. '+label(o)+o['suf'],'mk':'Stanley','y':o['yrs'],'d':(lcfirst(t)+(f", {o['ln']} in long" if o['ln'] else '')).strip(', ')})
        e['v']=vs
        if vs: e['dt']='letter or prefix variant · year'
        newk[kd].append(e)
# keep order by number within kind
PS=D('Woodworking hand tools')
psec=next(s for s in PS['s'] if s['n']=='Planes & scrapers')
kinds={k['n']:k for k in psec['k']}
dkinds={ 'Scrub plane':'Heavy plane with a curved iron that removes stock quickly before flattening.','Circular plane':'Plane with a flexing sole that cuts concave and convex curves.','Dado plane':'Plane that cuts a housing across the grain.','Match and tonguing plane':'Plane that cuts a tongue or a groove along a board edge.','Specialist plane':'Plane made for one narrow trade job, such as floor, chute-board, core-box or fibre-board work.'}
for kn,dd in dkinds.items():
    if kn not in kinds:
        k={'n':kn,'a':'','d':dd}; psec['k'].append(k); kinds[kn]=k
NL='One entry is one Stanley catalogue number; letter, prefix and half-size-suffix variants of the same number are versions.'
planeCounts={}
for kn,k in kinds.items():
    if kn in newk:
        lst=newk[kn]; planeCounts[kn]=len(lst)
        k['x']=lst; k['nl']=NL
        k['sel']=f"Follows Patrick's Blood and Gore, the numbered Stanley plane guide on supertool.com (pages 1–15), and Fine Woodworking's plane-number article. Maker versions (Record, Lie-Nielsen, Veritas) are not added because no fetched page ties them to a number. Covers {len(lst)} of about {len(lst)} numbers of this kind in the guide; the guide was read through a page summariser, so a heading may be missing, and numbers with no data on the page (#14, #53, #91) are left out."
    
# ================= KNIVES =================
KN=D('Knives, multi-tools & axes')
def setkind(dn,kn,**kw):
    s,k=K(dn,kn); k.update(kw); return k
WIKI=lambda p:'https://en.wikipedia.org/wiki/'+p
# Opinel
op=[('1','discontinued in 1932; 2 cm blade'),('2',''),('3',''),('4',''),('5',''),('6',''),('7','round-ended; sold as "My first Opinel"'),('8','8.5 cm blade'),('9',''),('10',''),('11','discontinued in 1935'),('12','12 cm blade'),('13','"Le Géant", 22 cm blade')]
ox=[]
for n,dd in op:
    ox.append({'n':f'Opinel No. {n}','d':('Folding knife in the Opinel numbered range'+(': '+dd if dd else '')+'.'),'mk':'Opinel','y':'','s':WIKI('Opinel'),'g':'Discontinued sizes' if n in('1','11') else 'Current sizes','v':[]})
setkind('Knives, multi-tools & axes','Friction folder & locking-collar knife',x=ox,nl='One entry is one numbered Opinel size; the numbers are the maker\'s size scale.',sel='Follows the Opinel article on Wikipedia, which lists the numbered range. The Opinel is held by the V&A (1985 selection), exhibited at MoMA and in Phaidon Design Classics, so the range qualifies under the icon rule. Complete: 13 of 13 sizes named there (Nos. 1 to 13); blade lengths are given for four only.')
# Buck 110 + lockback
setkind('Knives, multi-tools & axes','Lockback folder',x=[{'n':'Buck 110 Folding Hunter','a':'Model 110','d':'Buck\'s lockback folding hunting knife, first sold in 1964 and described as one of the most popular knives ever made.','mk':'Buck Knives','y':'1964','s':WIKI('Buck_Knives'),'role':'landmark','v':[{'n':'Buck 110 LT','mk':'Buck Knives','y':'2018','d':'lightweight FRN-handled version'}]}],nl='One entry is one named lockback model line from the references used.',sel='Follows the Buck Knives article on Wikipedia, which names the Model 110 and its variants. Covers 1 of about 1 lockback line in the references used; other makers\' lockbacks are not in a fetched reference.')
# Swiss Army knife
V=WIKI('Victorinox')
sx=[
 {'n':'Modell 1890','d':'First soldier\'s knife generation, first made by Wester & Co in Solingen and also by Elsener.','mk':'Wester & Co · Elsener','y':'1890','s':V,'g':'Soldier\'s knives'},
 {'n':'Modell 1908','d':'Second soldier\'s knife generation, made by several companies in Germany and Switzerland.','mk':'several makers','y':'1908','s':V,'g':'Soldier\'s knives'},
 {'n':'Modell 1951','d':'Third soldier\'s knife generation, made by several companies in Germany and Switzerland.','mk':'several makers','y':'1951','s':V,'g':'Soldier\'s knives'},
 {'n':'Modell 1961','d':'Fourth soldier\'s knife generation, made only by Victorinox and Wenger.','mk':'Victorinox · Wenger','y':'1961','s':V,'g':'Soldier\'s knives'},
 {'n':'Model 08','a':'Soldatenmesser 2008','d':'Soldier\'s knife introduced after the Wenger takeover and made only by Victorinox.','mk':'Victorinox','y':'2008','s':V,'g':'Soldier\'s knives'},
 {'n':'Officer\'s knife','a':'Schweizer Offiziers- und Sportmesser · Original Swiss Army Knife','d':'Knife patented in 1897 and later sold internationally as the Original Swiss Army Knife; the Swiss army did not adopt it as ordnance.','mk':'Victorinox','y':'1897','s':V,'g':'Civilian models'},
 {'n':'Champion','d':'Victorinox flagship before the SwissChamp, held in the permanent design collection of the Museum of Modern Art.','mk':'Victorinox','y':'','s':V,'g':'Civilian models','role':'landmark','v':[{'n':'SwissChamp','mk':'Victorinox','y':'1986','d':'successor flagship'}]},
 {'n':'SwissCard','d':'Credit-card-sized tool with 10 functions (Classic) or 13 (Quattro and Lite).','mk':'Victorinox','y':'','s':V,'g':'Civilian models','v':[{'n':'SwissCard Classic','mk':'Victorinox','y':'','d':'10 functions'},{'n':'SwissCard Quattro','mk':'Victorinox','y':'','d':'13 functions'},{'n':'SwissCard Lite','mk':'Victorinox','y':'','d':'13 functions, with a flashlight'}]},
]
for nm in ['Huntsman','Climber','Electrician','Money-Clip','Spirit','One-Hand Master RT','Craftsman','Broker','Pioneer']:
    sx.append({'n':nm,'d':'Victorinox model shown in the maker\'s gallery on Wikipedia; the page gives no year.','mk':'Victorinox','y':'','s':V,'g':'Civilian models'})
for e in sx: e.setdefault('v',[])
setkind('Knives, multi-tools & axes','Swiss Army knife',x=sx,nl='One entry is a named Swiss Army knife model or soldier\'s knife generation.',sel='Follows the Victorinox article on Wikipedia (owner Victorinox-Stiftung 90 % and Carl und Elise Elsener-Gut Stiftung 10 %; Wenger taken over 26 April 2005). Covers 17 of about 40 models; the page names the rest in a gallery without detail, and does not mention Classic SD, Spartan or Cybertool.')
# Leatherman
lines=collections.OrderedDict()
for l in open(W+'leatherman_raw.txt'):
    l=l.strip()
    if not l: continue
    m=re.match(r'^(.*) \(([^()]*)\)$',l); name,par=m.groups()
    name=name.replace(' - ',' – ')
    first=name.split()[0]
    line={'Super':'Super Tool','Mini':'Mini Tool'}.get(first,first).replace('+','')
    ym=re.match(r'(\d{4})',par); yr=ym.group(1) if ym else ''
    note=par.split(';',1)[1].strip() if ';' in par else par
    lines.setdefault(line,[]).append((name,yr,note))
KEY={'Micra','Squirt','Style','Tread'}
lx=[];kx=[]
LU=WIKI('Leatherman')
for line,vs in lines.items():
    ys=[v[1] for v in vs if v[1]]
    e={'n':'Leatherman '+line,'d':f"Leatherman model line; the maker's table lists {len(vs)} version{'s' if len(vs)>1 else ''}"+(f", the first sold in {min(ys)}" if ys else '')+'.','mk':'Leatherman','y':min(ys) if ys else '','s':LU,
       'v':[{'n':v[0],'mk':'Leatherman','y':v[1],'d':v[2]} for v in vs]} if len(vs)>1 else {'n':'Leatherman '+line,'d':f"Leatherman model line first sold in {vs[0][1]}; {vs[0][2]}." if vs[0][1] else 'Leatherman model line; the table gives no debut year.','mk':'Leatherman','y':vs[0][1],'s':LU,'v':[]}
    (kx if line in KEY else lx).append(e)
lx.append({'n':'Victorinox SwissTool','d':'Victorinox plier multi-tool, named in the gallery on the Victorinox article; the page gives no year.','mk':'Victorinox','y':'','s':V,'v':[]})
nlx=len(lines)
setkind('Knives, multi-tools & axes','Plier multi-tool',x=lx,nl='One entry is one model line of plier multi-tool; size, finish and edition variants are versions.',sel=f'Follows the Leatherman article on Wikipedia, which tabulates each model with debut and retirement years, and the Victorinox article for the SwissTool. Covers {len(lx)-1} Leatherman lines of about {nlx}; limited editions (anniversary, camouflage, Damascus, TOPO, Black & Silver) and the folding Crater line are not listed.')
setkind('Knives, multi-tools & axes','Keychain & wearable multi-tool',x=kx,nl='One entry is one model line of small keychain or wearable multi-tool.',sel=f'Follows the Leatherman article on Wikipedia. Covers {len(kx)} lines (Micra, Squirt, Style, Tread) of about {nlx} Leatherman lines; the page marks only the Micra as a keychain tool, the other three keep their earlier placement.')
# Mora / Buck fixed blade
MU=WIKI('Mora_knife')
fx=[
 {'n':'Mora Companion','a':'Companion MG','d':'Mora general-purpose fixed blade in high-carbon and stainless steel; it replaces the discontinued 840 Clipper and 860 Clipper.','mk':'Morakniv','y':'','s':MU,'v':[{'n':'Companion MG High Carbon','mk':'Morakniv','y':'','d':'replaces the 840 Clipper'},{'n':'Companion MG Stainless','mk':'Morakniv','y':'','d':'replaces the 860 Clipper'}]},
 {'n':'Mora Basic','d':'Mora budget fixed blade.','mk':'Morakniv','y':'','s':MU,'v':[{'n':'Basic 511','mk':'Morakniv','y':'','d':'carbon steel'},{'n':'Basic 546','mk':'Morakniv','y':'','d':'stainless steel'}]},
 {'n':'Mora Bushcraft Series','d':'Mora line of fixed blades for bushcraft.','mk':'Morakniv','y':'','s':MU,'v':[]},
 {'n':'Mora Kansbol','d':'Mora fixed-blade model named on the Mora knife article.','mk':'Morakniv','y':'','s':MU,'v':[]},
 {'n':'Mora Garberg','d':'Mora fixed-blade model named on the Mora knife article.','mk':'Morakniv','y':'','s':MU,'v':[]},
 {'n':'Mora Outdoor 2000','d':'Mora fixed-blade model named on the Mora knife article.','mk':'Morakniv','y':'','s':MU,'v':[]},
 {'n':'Buckmaster','a':'Model 184','d':'Buck survival knife of 1984 with a hollow handle.','mk':'Buck Knives','y':'1984','s':WIKI('Buck_Knives'),'v':[]},
 {'n':'Buck Nighthawk','d':'Buck fixed blade of 1992–1993, also submitted to the US Marines as the "Best M9".','mk':'Buck Knives','y':'1992','s':WIKI('Buck_Knives'),'v':[]},
 {'n':'Buck M9 Bayonet','d':'Bayonet made by Buck for the US Army, with an initial order of 315,600.','mk':'Buck Knives','y':'','s':WIKI('Buck_Knives'),'v':[]},
]
setkind('Knives, multi-tools & axes','Fixed-blade EDC & bushcraft knife',x=fx,nl='One entry is one named fixed-blade model line; steel and handle variants are versions.',sel='Follows the Mora knife article and the Buck Knives article on Wikipedia. Complete: 9 of 9 fixed-blade models they name; neither page gives Mora years, and the Mora page names models only in a short list.')
# ================= POWER TOOLS =================
PT=D('Power tools')
GL='https://glg.com/articles/electric-power-tools-and-accessories-a-global-overview'
SBD=WIKI('Stanley_Black_%26_Decker'); TTI=WIKI('Techtronic_Industries')
BR=[
 ('DeWalt','Stanley Black & Decker','Global group','United States','1924','',WIKI('DeWalt'),'American brand founded in 1924; Black & Decker bought it in 1960. Its 20V MAX and FlexVolt battery platforms are below.'),
 ('Black+Decker','Stanley Black & Decker','Global group','United States','','2010',SBD,'Brand combined with Stanley in the 2010 merger that formed Stanley Black & Decker.'),
 ('Craftsman','Stanley Black & Decker','Global group','United States','1927','2017',WIKI('Craftsman_(tools)'),'Sears tool brand registered in 1927; Stanley Black & Decker closed the purchase on 9 March 2017.'),
 ('Milwaukee','Techtronic Industries','Global group','United States','1924','2005',WIKI('Milwaukee_Electric_Tool'),'American brand founded in 1924; Techtronic bought it in 2005 for $626.6 million.'),
 ('Ryobi','Techtronic Industries','Global group','Japan','1943','2000',WIKI('Ryobi'),'Japanese brand founded in 1943; Techtronic took the North American power tools business in 2000, Europe in 2001, and uses the name under licence.'),
 ('Bosch','Robert Bosch GmbH','Global group','Germany','1886','',WIKI('Robert_Bosch_GmbH'),'German group owned 94 % by the Robert Bosch Stiftung; one source in 2019 called its power tools division the world\'s largest by 2018 revenue.'),
 ('Makita','Makita Corporation','Global group','Japan','1915','',WIKI('Makita'),'Japanese maker listed on the Tokyo Stock Exchange; ranked fourth in the 2021 global ranking by GLG.'),
 ('Hilti','Hilti','Global group','Liechtenstein','1941','',WIKI('Hilti'),'Liechtenstein maker whose registered shares are all held by the Martin Hilti Family Trust; ranked fifth in the 2021 GLG ranking.'),
 ('Festool','TTS Tooltechnic Systems','Independent','Germany','1925','',WIKI('Festool'),'German maker founded in 1925 and a subsidiary of TTS Tooltechnic Systems; the page also describes it as family-owned.'),
]
bx=[]
for n,own,tier,cty,f,oy,src,dd in BR:
    e={'n':n,'d':dd,'mk':n,'y':f,'s':src,'own':own,'tier':tier,'cty':cty,'g':'Owned by '+own,'v':[]}
    if oy: e['own_y']=oy
    bx.append(e)
bx.sort(key=lambda e:(e['own'],e['y'] or '9999',e['n']))
shelf={'n':'Power tool brands','t':'The makers whose names buyers choose, grouped by owner; a battery system is listed under Battery platforms, a single tool under its kind.','ax':'owner group, then brand','k':[{'n':'Power tool brand','a':'','d':'Maker sold under its own name whose cordless and corded tools are bought as a range.','nl':'One entry is one power tool brand sold under its own name; battery platforms are listed separately.','sel':'Brands of the owner groups named in the department\'s market panel (Stanley Black & Decker, Techtronic Industries, Bosch, Makita, Hilti, Festool), from each brand\'s Wikipedia article. Covers 9 of about 9 brands requested; Porter-Cable, Irwin, Lenox and AEG are not listed because the fetched pages give no country or founding year.','x':bx}]}
PT['s'].insert(0,shelf)
# battery platforms: owner fields
OWN={'Makita':('Makita Corporation','Global group','Japan'),'Milwaukee':('Techtronic Industries','Global group','United States'),'DeWalt':('Stanley Black & Decker','Global group','United States'),'Ryobi':('Techtronic Industries','Global group','Japan'),'Bosch':('Robert Bosch GmbH','Global group','Germany'),'Hilti':('Hilti','Global group','Liechtenstein'),'Festool':('TTS Tooltechnic Systems','Independent','Germany')}
s,k=K('Power tools','Tool battery')
k['nl']='One entry is one cordless battery platform: the packs and tools of one maker that fit each other.'
k['sel']='Platforms named on the makers\' own pages and in the retail pages cited per entry; no reference lists every platform. Covers 17 platforms of the makers above plus Metabo, Einhell, Ridgid and EGO; owners are stated only where a fetched page gives them.'
for e in k['x']:
    o=OWN.get(e.get('mk'))
    if o: e['own'],e['tier'],e['cty']=o
    if e['n'].startswith('Milwaukee M18') and e['n']=='Milwaukee M18': e['y']='2010'
dfix={ 'DeWalt 20V MAX / 18V XR':None }
# market panel
def ms(mkt,who,share,yr,s,note): return {'mkt':mkt,'who':who,'share':share,'yr':yr,'s':s,'note':note}
PT['ms']=[
 ms('Global power tools, company ranking','TTI (Techtronic Industries)','rank 1',2021,GL,'largest in both professional and DIY tools, per GLG'),
 ms('Global power tools, company ranking','Stanley Black & Decker','rank 2',2021,GL,'per GLG'),
 ms('Global power tools, company ranking','Bosch','rank 3',2021,GL,'per GLG'),
 ms('Global power tools, company ranking','Makita','rank 4',2021,GL,'GLG says "probably" fourth'),
 ms('Global power tools, company ranking','Hilti','rank 5',2021,GL,'per GLG'),
 ms('Global power tools by region','Asia-Pacific','about 35 %',2020,GL,'share of the global power tool market'),
 ms('Global power tools by region','North America','about 32 %',2020,GL,'share of the global power tool market'),
 ms('Global power tools by region','Europe','about 29 %',2020,GL,'share of the global power tool market'),
 ms('Power tools by country','United States','about 29 %',2020,GL,'largest single country market'),
 ms('Power tools by country','China','20–22 %',2020,GL,'share of the global market'),
 ms('Power tools by country','Germany','8–10 %',2020,GL,'share of the global market'),
 ms('Group revenue (not tools alone)','Stanley Black & Decker','US$15.1 billion',2025,SBD,'company revenue, not power-tool share'),
 ms('Group revenue (not tools alone)','Techtronic Industries','US$15.3 billion',2025,TTI,'company revenue, not power-tool share'),
 ms('Group revenue (not tools alone)','Makita','¥753.13 billion',2025,WIKI('Makita'),'company revenue'),
 ms('Group revenue (not tools alone)','Hilti','CHF 6.4 billion',2024,WIKI('Hilti'),'company revenue'),
 ms('Group revenue (not tools alone)','Bosch Group','€90.34 billion',2024,WIKI('Robert_Bosch_GmbH'),'group revenue; consumer goods, which include power tools, were 22 % of sales'),
]
d['rev']=d.get('rev',True)
json.dump(d,open(W+'C1.new.json','w'),ensure_ascii=False,indent=1)
json.dump(dropped,open(W+'dropped.json','w'),ensure_ascii=False,indent=0)
print({k:len(v) for k,v in dropped.items()}, planeCounts, len(lx),len(kx))
