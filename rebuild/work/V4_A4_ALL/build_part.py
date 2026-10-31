import json,re,sys,os
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_A4_ALL')
from data import *
OW['Jimmy Choo']=('Capri Holdings','Global group','','2017')
base=json.load(open('/home/user/Possession-Taxonomy/rebuild/out/A4.json'))
depts=base['depts']
D={d['n']:d for d in depts}
def kinds(d):
    for s in d['s']:
        for k in s['k']: yield k
def findk(dn,kn):
    for k in kinds(D[dn]):
        if k['n']==kn: return k
    raise KeyError((dn,kn))
removed_m=[]
for d in depts:
    for k in kinds(d):
        if k.get('m'):
            removed_m.append((d['n'],k['n'],len(k['m'])))
        k.pop('m',None)
# add entries
added={}
for e in N:
    k=findk(e['dept'],e['kind'])
    xs=k.setdefault('x',[])
    if any(x['n'].lower()==e['n'].lower() for x in xs):
        print('dup',e['n']); continue
    x={'n':e['n'],'a':e['a'],'d':e['d'],'mk':e['mk'],'y':e['y'],'s':e['s'],'v':e['v'],'dt':e['dt']}
    xs.append(x); added[(e['dept'],e['n'])]=1
# fix existing mk
for k in kinds(D['Eyewear']):
    for x in k.get('x',[]):
        if x['n']=='Lemtosh': x['mk']='Moscot'
        if x['n']=='Persol 649': x['mk']='Persol'
# versions
for (dn,en),vs in ADDV.items():
    done=False
    for k in kinds(D[dn]):
        for x in k.get('x',[]):
            if x['n']==en:
                have={v['n'] for v in x.get('v',[])}
                for v in vs:
                    if v[0] not in have: x.setdefault('v',[]).append(dict(n=v[0],mk=x.get('mk',''),y=v[1],d=v[2]))
                done=True
    if not done: print('no entry for version',dn,en)
# owner fields + g
def yr(s):
    m=re.search(r'(\d{4})',s or ''); return int(m.group(1)) if m else 9999
OWNER_DEPTS_BY_GROUP={'Eyewear','Luggage & travel','Backpacks & belt bags'}
for d in depts:
    for k in kinds(d):
        for x in k.get('x',[]) or []:
            mk=x.get('mk','')
            if mk in OW:
                o=OW[mk]; x['own'],x['tier'],x['cty'],x['own_y']=o
                if d['n'] in OWNER_DEPTS_BY_GROUP: x['g']=o[0] if o[1]=='Global group' else 'Independent houses and makers'
                else: x['g']=(o[2] or 'Country not stated')+' · '+mk
            elif mk:
                x['g']='Other makers'
            else:
                x['g']='Traditional and unattributed forms'
            if d['n'] not in OWNER_DEPTS_BY_GROUP and mk not in OW and mk: x['g']='Other makers'
        if k.get('x'):
            k['x'].sort(key=lambda x:(x['g'].startswith('Traditional'),x['g'].startswith('Other'),x['g'],yr(x.get('y')),x['n']))
# roles
for x in findk('Umbrellas, fans & canes','Folding umbrella')['x']:
    if x['n']=='Jean Marius folding umbrella': x['role']='origin'
# nl / sel / xg
NL={
 'Handbags':"One entry is a handbag model line named by its house (Birkin, Kelly, Speedy, Baguette); sizes, leathers and editions are versions.",
 'Wallets & small leather goods':"One entry is a named small leather goods line from one maker (Goyard Saint-Sulpice, Bellroy Note Sleeve); sizes and colours are versions.",
 'Eyewear':"One entry is a frame model line from one maker (Ray-Ban Wayfarer, Persol 649, Oakley Frogskins, Moscot Lemtosh); sizes, lens options and colours are versions.",
 'Backpacks & belt bags':"One entry is a pack model line from one maker (Osprey Atmos AG, Gregory Baltoro, Fjällräven Kånken); litre sizes and generations are versions.",
 'Luggage & travel':"One entry is a luggage or travel-bag line from one maker (Rimowa Original, Samsonite Cosmolite, Tumi Alpha, Globe-Trotter Centenary); sizes are versions.",
 'Work bags':"One entry is a named work-bag line from one maker; sizes and colours are versions.",
 'Umbrellas, fans & canes':"One entry is an origin design, a design-collection landmark or a named traditional form (Knirps, Sensu, Uchiwa); no brand catalogue is listed.",
 'Bag accessories':"One entry is a named accessory line from one maker (Hermès Twilly, Fendi Bag Bugs); colours are versions.",
 'Baby carriers & changing bags':"One entry is a carrier line from one maker (BabyBjörn Baby Carrier, Ergobaby carrier); models and generations are versions; the carrier types themselves are kinds.",
}
SEL={
 'Handbags':"Lines named on the houses' own model pages and on Wikipedia house and handbag articles, fetched on 31 October 2026: Louis Vuitton (handbag page), Hermès (women's bags collection), Chanel (the CHANEL handbag), Dior (Bags by Line), Celine and Prada (collection filters), Loewe (bags by line), Fendi (bag lines), plus Wikipedia on Gucci, Bottega Veneta, Longchamp and the Handbag article.",
 'Wallets & small leather goods':"Lines already attested on the makers' pages and Wikipedia; no whole-space list of small leather goods exists.",
 'Eyewear':"Frame lines named on Wikipedia's Ray-Ban, Persol, Moscot and Oakley pages and on the makers' pages cited per entry.",
 'Backpacks & belt bags':"Pack lines named on the makers' own range pages fetched on 31 October 2026: Osprey (backpacking range and sizing chart), Gregory (backpacking packs), Deuter (backpacking packs), Fjällräven (Kånken range), Eastpak (backpack collection), JanSport (backpack finder) and Herschel (Little America).",
 'Luggage & travel':"Lines named on Wikipedia's Rimowa, Samsonite, Tumi and Louis Vuitton pages, plus earlier maker pages cited per entry.",
 'Work bags':"Lines already attested on the makers' pages; no whole-space list exists.",
 'Umbrellas, fans & canes':"Wikipedia's Umbrella and Hand fan articles, plus the maker and tradition pages cited per entry.",
 'Bag accessories':"Lines attested on the makers' pages; no whole-space list exists.",
 'Baby carriers & changing bags':"Wikipedia's Baby sling and BabyBjörn articles and a Maui Now profile of Ergobaby.",
}
COV={
 'Handbags':"Covers {n} lines of this kind; no complete list of named handbags exists. House pages for Gucci, Saint Laurent, Bottega Veneta, Goyard and Mulberry were blocked or did not name lines, so those houses appear only through lines already attested or named on Wikipedia, and Hermès, Louis Vuitton and Fendi list only the lines their pages showed.",
 'Eyewear':"Covers {n} lines of this kind; no complete list of frame models exists, and Wikipedia gave few model names for Persol, Oakley and Moscot.",
 'Backpacks & belt bags':"Covers {n} lines of this kind from the makers' range pages read; Herschel's other lines and pages of the Osprey, Eastpak and JanSport ranges that did not load are not included.",
 'Luggage & travel':"Covers {n} lines of this kind; Globe-Trotter's page could not be fetched, so its lines are the earlier ones only.",
}
XG={'Handbags':"by house country, then house",'Wallets & small leather goods':"by house country, then maker",'Eyewear':"by owner group, then maker",'Backpacks & belt bags':"by owner group, then maker",'Luggage & travel':"by owner group, then maker",'Work bags':"by house country, then maker",'Umbrellas, fans & canes':"by maker or tradition",'Bag accessories':"by house country, then maker",'Baby carriers & changing bags':"by maker"}
for d in depts:
    for k in kinds(d):
        if k.get('x'):
            n=len(k['x'])
            k['nl']=NL[d['n']]; k['xg']=XG[d['n']]
            cov=COV.get(d['n'],"Covers {n} lines of this kind; no complete list exists, and entries are the ones whose pages were fetched.").format(n=n)
            k['sel']=SEL[d['n']]+f" This kind holds {n} entries. "+cov
# market panels
HWI=W+'Herm%C3%A8s'
D['Handbags']['msum']="Luxury handbags sit with a few groups and some family-owned houses. The figures below are group-level, as the cited pages state them, with their years; no page gave a handbag-only share."
D['Handbags']['ms']=[
 {"mkt":"Hermès International ownership","who":"H51 (Hermès family holding)","share":"66.72 % of capital","yr":2025,"s":HWI,"note":"holding as at 12 March 2025; LVMH took 17.1 % in 2010 and redistributed it in 2014"},
 {"mkt":"Kering group sales","who":"Kering (Gucci, Saint Laurent, Bottega Veneta)","share":"EUR 14,675 million","yr":2025,"s":W+'Kering',"note":"group revenue, down from EUR 17,194 million in 2024 and EUR 19,566 million in 2023"},
 {"mkt":"Tapestry sales","who":"Tapestry (Coach, Kate Spade)","share":"US$7.01 billion","yr":2025,"s":W+'Tapestry,_Inc.',"note":"revenue to 28 June 2025; Stuart Weitzman sale to Calares completed 4 August 2025"},
 {"mkt":"Capri Holdings sales","who":"Capri Holdings (Michael Kors, Jimmy Choo)","share":"US$4.4 billion","yr":2025,"s":W+'Capri_Holdings',"note":"fiscal 2025, down 21 % from US$5.6 billion; Versace was sold to Prada in 2025 for EUR 1.25 billion"},
 {"mkt":"Richemont sales","who":"Richemont (Cartier, Delvaux, Serapian)","share":"EUR 21.4 billion","yr":2025,"s":W+'Richemont',"note":"group revenue, not leather goods alone"},
 {"mkt":"LVMH fashion and leather goods","who":"LVMH (Louis Vuitton, Dior, Fendi, Celine, Loewe)","share":"sales down 12 %","yr":2025,"s":W+'LVMH',"note":"figure from a Forbes headline cited on the page; no segment total given"},
]
D['Eyewear']['msum']="Eyewear is led by EssilorLuxottica, with Safilo, Marcolin and Kering Eyewear next. The figures are those the cited pages state, with their years; none is a share of the whole market."
D['Eyewear']['ms']=[
 {"mkt":"Sunglass Hut stores","who":"EssilorLuxottica","share":"3,131 locations","yr":2025,"s":W+'EssilorLuxottica',"note":"retail chain; LensCrafters had 1,098 and Óticas Carol 1,425"},
 {"mkt":"Safilo sales","who":"Safilo","share":"EUR 983.4 million","yr":2025,"s":W+'Safilo',"note":"revenue; HAL Holding raised its stake to 49.8 % in January 2019"},
 {"mkt":"Marcolin sales","who":"Marcolin","share":"EUR 547 million","yr":2022,"s":W+'Marcolin',"note":"revenue; VSP Vision completed its takeover in late 2025"},
 {"mkt":"Kering Eyewear sales","who":"Kering Eyewear","share":"about EUR 1.5 billion","yr":2023,"s":W+'Kering',"note":"group's eyewear arm, created in 2014"},
 {"mkt":"Second-largest eyewear group","who":"Kering Eyewear","share":"second place","yr":2022,"s":W+'Safilo',"note":"the Safilo page says Kering Eyewear became second largest in 2022"},
]
D['Luggage & travel']['msum']="Luggage is led by Samsonite, with Rimowa the main luxury name under LVMH. The figures are deal values the cited pages state, with their years; no page gave market shares."
D['Luggage & travel']['ms']=[
 {"mkt":"Samsonite takeover","who":"CVC Capital Partners","share":"US$1.7 billion","yr":2007,"s":W+'Samsonite',"note":"price of the July 2007 takeover"},
 {"mkt":"Tumi acquisition","who":"Samsonite","share":"US$1.8 billion","yr":2016,"s":W+'Tumi_Inc.',"note":"all-cash deal announced 4 March 2016"},
 {"mkt":"Rimowa stake","who":"LVMH","share":"80 % for EUR 640 million","yr":2016,"s":W+'Rimowa',"note":"acquired October 2016"},
 {"mkt":"Samsonite stock listing","who":"Samsonite International S.A.","share":"US$1.25 billion raised","yr":2011,"s":W+'Samsonite',"note":"Hong Kong IPO in June 2011"},
]
# fix rimowa year in dt? none
# brands
existing={b['n'] for b in json.load(open('/home/user/Possession-Taxonomy/rebuild/out/A4_brands.json'))['b']}
allb={b['n'] for b in json.load(open('/home/user/Possession-Taxonomy/rebuild/reader/_brands.json'))['b']} if 'b' in json.load(open('/home/user/Possession-Taxonomy/rebuild/reader/_brands.json')) else set()
def B(n,c,f,d,s,seg='Luxury house',kf='luxury goods'):
    return {'n':n,'seg':seg,'d':d,'lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':s,'kf':kf,'c':c,'f':f}
NB=[
 B('LVMH','France','1987','Group formed in 1987 by the merger of Louis Vuitton and Moët Hennessy; owns Louis Vuitton, Dior, Fendi, Celine, Loewe and Rimowa.',W+'LVMH','fashion & leather goods'),
 B('Kering','France','','Group renamed from PPR in March 2013; owns Gucci, Saint Laurent, Bottega Veneta, Balenciaga and Kering Eyewear.',W+'Kering','fashion & leather goods'),
 B('Chanel Limited','France','1910','Holding through which Alain and Gérard Wertheimer own the Chanel house, founded in Paris in 1910.',W+'Chanel','handbags'),
 B('Hermès International','France','1837','Parent of Hermès, founded in Paris in 1837 by Thierry Hermès; the family holding H51 held 66.72 % in 2025.',W+'Herm%C3%A8s','leather goods'),
 B('Prada Group','Italy','1913','Owner of Prada, Miu Miu, Church\'s, Car Shoe and Versace (bought from Capri Holdings in 2025).',W+'Prada','handbags'),
 B('Tapestry','United States','','Owner of Coach, Kate Spade (2017) and, until August 2025, Stuart Weitzman (2015); renamed from Coach, Inc. in 2017.',W+'Tapestry,_Inc.','handbags'),
 B('Capri Holdings','United States','','Renamed from Michael Kors Holdings on 2 January 2019; owns Michael Kors and Jimmy Choo, and sold Versace to Prada in 2025.',W+'Capri_Holdings','handbags'),
 B('Richemont','Switzerland','1988','Geneva luxury group founded in 1988; its maisons include Cartier, Dunhill, Serapian and Delvaux.',W+'Richemont','luxury goods'),
 B('Safilo','Italy','1934','Eyewear group founded in 1934 in Pieve di Cadore; owns Carrera, Polaroid Eyewear and Smith, and makes licensed frames.',W+'Safilo','eyewear','Mainstream'),
 B('Marcolin','Italy','1961','Eyewear maker founded in 1961 by Giovanni Marcolin; taken over by VSP Vision in late 2025.',W+'Marcolin','eyewear','Mainstream'),
 B('Kering Eyewear','France','2014','Eyewear arm of Kering created in 2014; about EUR 1.5 billion in sales in 2023.',W+'Kering','eyewear'),
 B('Samsonite International S.A.','Luxembourg','1910','Luggage group founded in 1910 in Denver; owns American Tourister, Hartmann, Gregory and Tumi.',W+'Samsonite','luggage','Mainstream'),
 B('Fenix Outdoor','','','Placeholder removed.',W+'Samsonite'),
]
NB=[b for b in NB if b['n']!='Fenix Outdoor']
brands=[b for b in NB if b['n'] not in existing and b['n'] not in allb]
# makers used as mk without register entry
mks={x['mk'] for d in depts for k in kinds(d) for x in k.get('x',[]) or [] if x.get('mk')}
reg=existing|allb|{b['n'] for b in brands}
missing=sorted(m for m in mks if m not in reg)
for m in missing:
    brands.append({'n':m,'seg':'Designer','d':'Named as maker of entries in the A4 bag and eyewear departments.','lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':'https://en.wikipedia.org/wiki/Handbag','kf':'','c':''})
upd={}
for mk,o in OW.items():
    upd[mk]={'own':o[0],'tier':o[1],'c':o[2]}
    if o[3]: upd[mk]['own_y']=o[3]
upd={k:v for k,v in upd.items() if k in reg or k in {b['n'] for b in brands}}
out={'replaces':[d['n'] for d in depts],'depts':depts,'brands':brands,'brand_updates':upd,'renames':{},'moves':[]}
json.dump(out,open('/home/user/Possession-Taxonomy/rebuild/out/A4_parts/ALL.json.tmp','w'),ensure_ascii=False)
os.replace('/home/user/Possession-Taxonomy/rebuild/out/A4_parts/ALL.json.tmp','/home/user/Possession-Taxonomy/rebuild/out/A4_parts/ALL.json')
print('removed m:',removed_m)
print('missing brands added:',missing)
print('entries:',sum(len(k.get('x',[])) for d in depts for k in kinds(d)),'size',os.path.getsize('/home/user/Possession-Taxonomy/rebuild/out/A4_parts/ALL.json'))
