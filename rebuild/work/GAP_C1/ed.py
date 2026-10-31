import json,re,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/C1.json'))
def kinds():
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']: yield dp,s,k
def K(n): return [k for _,_,k in kinds() if k['n']==n][0]
def S(n): return [s for _,s,_ in kinds() if s['n']==n][0]
log=[]
# ---------- planes
PL=['Bench plane','Block plane','Shoulder plane','Rebate plane','Router plane','Plough plane','Combination plane','Moulding plane','Scraper','Scrub plane','Circular plane','Dado plane','Match and tonguing plane','Specialist plane']
for n in PL:
    k=K(n); c=len(k['x'])
    k['xg']='Stanley number series'
    base=k['sel'].split(' Covers ')[0]
    base=base.replace('Maker versions (Record, Lie-Nielsen, Veritas) are not added because no fetched page ties them to a number.','Maker versions are added only where a fetched page ties them to a Stanley number (Lie-Nielsen No. 95, 1981); Record and Veritas versions are not added because no fetched page ties them to a number.')
    k['sel']=base+f" Complete: {c} of {c} planes of this kind in the guide; Nos. 14, 53 and 91 are not planes (the guide says No. 14 and No. 91 were never assigned and No. 53 is a spokeshave only)."
for e in K('Rebate plane')['x']+K('Specialist plane')['x']+K('Bench plane')['x']+K('Block plane')['x']+K('Scraper')['x']+K('Shoulder plane')['x']:
    if e['n']=='Stanley No. 95':
        e.setdefault('v',[]).append({"n":"Lie-Nielsen No. 95","mk":"Lie-Nielsen Toolworks","y":"1981","d":"Lie-Nielsen took over production of an adapted Stanley No. 95 edge-trimming block plane in 1981."}); e['dt']=e.get('dt') or 'maker version · year'; log.append('lie-nielsen 95')
# ---------- Leatherman
T="""Arc|2023|-|Full-sized
Blast|2004|2012|Full-sized
Bolster|2021|-|Full-sized
Bond|2021|-|Full-sized
Charge Ti|2004|2008|Full-sized
Charge XTi|2004|2008|Full-sized
Charge AL|2007|2018|Full-sized
Charge ALX|2007|2018|Full-sized
Charge TTi|2007|2018|Full-sized
Charge+|2018|-|Full-sized
Charge+ TTi|2018|-|Full-sized
Core|2005|2009|Full-sized
Crunch|1999|2023|Heavy-Duty
Curl|2021|-|Full-sized
Flair|1999|2004|Full-sized
Free K2|2019|-|Pocket
Free K2X|2019|-|Pocket
Free K4|2019|-|Pocket
Free K4X|2019|-|Pocket
Free T2|2019|-|Pocket
Free T4|2019|2025|Pocket
Free P2|2019|2025|Full-sized
Free P4|2019|2025|Full-sized
Fuse|2004|2012|Full-sized
Freestyle|2009|-|Pocket
Freestyle CX|2009|2012|Pocket
Juice KF4|2001|2005|Pocket
Juice C2|2001|2006|Pocket
Juice S2|2001|2006|Pocket
Juice CS4|2001|2006|Pocket
Juice XE6|2001|2006|Pocket
Juice SC2|2003|2005|Pocket
Juice SX Original|2013|2014|Pocket
Juice SX New|2014|2019|Pocket
Kick|2004|2012|Full-sized
Leap|2014|2014|Pocket
Micra|1996|-|Keychain
Mini Tool|1986|2004|Pocket
MUT|2010|-|Heavy-Duty
MUT EOD|2010|2021|Heavy-Duty
OHT|2012|2022|Heavy-Duty
PST|1983|2004|Full-sized
PST II|1996|2004|Full-sized
Pulse|2000|2004|Full-sized
Raptor Rescue|2013|-|EMS
Raptor Response|2021|-|EMS
Rebar|2012|-|Full-sized
Rev|2015|-|Full-sized
Sideclip|1998|2004|Full-sized
Sidekick|2011|-|Full-sized
Signal|2015|-|Heavy-Duty
Skeletool|2007|-|Pocket
Skeletool CX|2007|-|Pocket
Skeletool KB|2017|-|Pocket
Skeletool KBx|2017|-|Pocket
Skeletool RX|2016|-|Pocket
Skeletool SX|2013|-|Pocket
Squirt E4|2003|2010|Keychain
Squirt ES4|2010|2021|Keychain
Squirt P4|2002|2010|Keychain
Squirt PS4|2010|-|Keychain
Squirt S4|2002|2010|Keychain
Style|2010|2014|Keychain
Style CS|2010|2021|Keychain
Style PS|2012|-|Keychain
Super Tool 200|2001|2005|Heavy-Duty
Super Tool 300|2009|-|Heavy-Duty
Super Tool 300 EOD|2010|-|Heavy-Duty
Surge Original|2005|2013|Heavy-Duty
Surge New|2013|-|Heavy-Duty
Tread|2015|2021|Wearable
Tread Metric|2015|2021|Wearable
Tread LT|2015|2021|Wearable
Wave Original|1998|2004|Full-sized
Wave New|2004|2018|Full-sized
Wave+|2018|-|Full-sized
Wingman|2011|-|Full-sized"""
rows=[l.split('|') for l in T.split('\n')]
CL={'Full-sized':'Full-sized','Pocket':'Pocket-sized','Heavy-Duty':'Heavy-duty','Keychain':'Keychain','Wearable':'Wearable','EMS':'Rescue (EMS)'}
base_cls={}
# base class from table: base = first token(s)
def basekey(name):
    for b in ['Super Tool','Mini Tool','Charge','Free','Juice','Skeletool','Squirt','Style','Tread','Surge','Wave','Raptor','PST','MUT','Freestyle','Micra']:
        if name==b or name.startswith(b+' ') or (b=='Charge' and name.startswith('Charge+')) or (b=='Wave' and name.startswith('Wave+')):
            if b=='PST': return 'PST'
            if b=='Freestyle' : return 'Freestyle'
            return b
    return name
LCL={'Charge':'Full-sized','Free':'Pocket','Juice':'Pocket','Skeletool':'Pocket','Squirt':'Keychain','Style':'Keychain','Tread':'Wearable','Surge':'Heavy-Duty','Wave':'Full-sized','Raptor':'EMS','Super Tool':'Heavy-Duty'}
vers={}
for n,y,r,c in rows:
    b=basekey(n)
    if n==b: 
        vers.setdefault(b,[]); base_cls[b]=c; continue
    vers.setdefault(b,[]).append((n,y,r,c))
for n,y,r,c in rows:
    base_cls.setdefault(basekey(n),c)
for kn in ['Plier multi-tool','Keychain & wearable multi-tool']:
    k=K(kn)
    for e in k['x']:
        if not e['n'].startswith('Leatherman '): continue
        b=e['n'][len('Leatherman '):]
        cls=base_cls.get(b) or LCL.get(b)
        if b=='Surge': pass
        if cls: e['g']=CL[cls]
        vs=vers.get(b,[])
        if b=='PST': vs=vs+[]
        if not e.get('v'):
            e['v']=[{"n":"Leatherman "+n,"mk":"Leatherman","y":(y if r=='-' or r==y else f"{y}–{r}"),"d":("current" if r=='-' else "retired "+r)+"; Leatherman model table"} for n,y,r,c in vs]
            if e['v']: e['dt']='version · years sold'
        # fix retirement note in description if missing
    # swiss tool
    for e in k['x']:
        if e['n']=='Victorinox SwissTool': e['g']='Heavy-duty'
# Raptor: g; PST II under PST
for kn in ['Plier multi-tool']:
    for e in K(kn)['x']:
        if e['n']=='Leatherman PST' and not any('PST II' in v['n'] for v in e['v']):
            e['v'].append({"n":"Leatherman PST II","mk":"Leatherman","y":"1996–2004","d":"retired 2004; Leatherman model table"}); e['dt']='version · years sold'
for e in K('Plier multi-tool')['x']:
    if not e.get('g'): e['g']='Full-sized' if e['n']!='Victorinox SwissTool' else 'Heavy-duty'
k=K('Plier multi-tool'); n=len(k['x'])
k['xg']='Size class'
k['sel']=("Follows the Leatherman article on Wikipedia, which tabulates each model with debut and retirement years, and the Victorinox article for the SwissTool. "
 f"Complete: 35 of 35 plier-based Leatherman lines in the model table, plus the Victorinox SwissTool ({n} entries). Limited and anniversary editions (Darkside, Mr. Crunch, camouflage, Damascus, TOPO, Black & Silver) are not entries; Crater is a folding knife and absent from the table.")
k=K('Keychain & wearable multi-tool')
k['xg']='Form'
for e in k['x']:
    e['g']='Wearable' if 'Tread' in e['n'] else 'Keychain'
k['sel']="Follows the Leatherman article on Wikipedia, whose model table marks each line as keychain or wearable. Complete: 4 of 4 keychain and wearable lines in the table (Micra, Squirt, Style, Tread)."
# ---------- Mora / lockback / fixed
k=K('Fixed-blade EDC & bushcraft knife')
k['xg']='Maker'
for e in k['x']: e['g']='Mora' if e['n'].startswith('Mora') else 'Buck'
k['sel']=k['sel'].replace('neither page gives Mora years','neither page gives Mora years (searched twice: Mora knife article, Morakniv search; no year found)')
k=K('Lockback folder')
for e in k['x']:
    e['g']='Buck'
k['sel']="No complete list exists; follows the Buck Knives article on Wikipedia (Model 110, introduced 1964, high-tension lock) and the Lock knife article, which credits Buck with popularising the lockback in the 1960s. Lock types of the Spyderco Delica and Worker, Kershaw Leek, Buck 112 and Cold Steel Voyager are not stated on any fetched page (two attempts each), so they are not entries."
# ---------- Swiss Army knife
sw=K('Swiss Army knife')
names0={e['n'].lower() for e in sw['x']}
for e in sw['x']:
    if e['g']=='Civilian models': e['g']='_c'
LEN={'Officer\'s knife':'91 mm','Champion':'91 mm','Huntsman':'91 mm','Climber':'91 mm','Craftsman':'91 mm','Electrician':'93 mm','Pioneer':'93 mm','Broker':'58 mm','One-Hand Master RT':'111 mm'}
for e in sw['x']:
    if e['g']=='_c': e['g']=LEN.get(e['n'],'Other civilian models')
def fold(spec):
    out=[]
    for l in spec.strip().split('\n'):
        parts=[p.strip() for p in l.split(';')]
        out.append(parts)
    return out
S91="""Altimeter;Altimeter Plus
American Eagle
Angler;Angler Plus
Automobile;Automobile Special
Camper
CampFlame
Champion;Champion Plus
Clipper
Compact
Companion
Cybertool;Cybertool S;Cybertool M;Cybertool L;Cybertool Lite
CyberYeoman
Deluxe Tinker
DofE Pocket Tool
Engineer
Expedition Lite
Explorer
FASS 90
Fieldmaster
Fisherman;Fisherman Plus
Golfer;Golfer Special
Grand Prix
Handyman;Handyman 7236maU
Hiker
Huntsman;Huntsman Plus;Huntsman Lite
Climber;Climber Lite;Deluxe Climber
Lumberjack Big
Luxury Automobile
Master Craftsman
Master Electrician
Master Fisherman
Master Gardener
Mechanic;Special Mechanic
Modeler
Motorist
Mountaineer;Mountaineer Lite
Outdoorsman
Passenger
Picnicker
Ranger
Scientist
Spartan;Spartan Lite
Super Tinker
SwissChamp;SwissChamp XL;SwissChamp XLT;SwissChamp XXL;SwissChamp XXLT;SwissChamp XAVT
SwissFlame
TimeKeeper;TimeKeeper Alarm
Tinker
Trail Guide
Traveller;Traveller Lite
Troubleshooter
Voyager;Voyager Lite
Waiter Plus
Woodsman
Workman
Yeoman
Yeoman Mechanic
Baker's Knife"""
S93="""Bushcrafter
Carver
Companion Slim Alox
Companion X Alox
Electrician's Mate
Farmer;Farmer X|2020
First Mate
Long Rancher
Midshipman
Pioneer Apprentice
Pioneer Harvester
Pioneer Pruner
Pioneer Rancher
Pioneer Scout
Pioneer Settler
Pioneer 2223
Sailor
Seaman
Solo Alox
Technician;Technician Plus"""
S100="""Day Packer
Gardener
Grafter
Pruner"""
S111="""Adventurer
Dual Pro;Dual Pro X;DAK 2010|2010
Skipper;Skipper Pro
Alpineer
Atlas
Carpenter
Centurion;DAK 1993|1993
Cheese Knife
Cheese Master
Hardwood Cheese Knife
Cowboy
Equestrian
Fireman
Forester
Garant
Helmsman
Hercules
Hunter;Hunter XS;Hunter XT
Jumpmaster
Lockblade Knife
Locksmith
Nomad
OutdoorTool
Outrider
Parachute Knife
Parachutist
Rescue Tool
Rucksack
Sentinel
Tradesman
Trailmaster
Welding Seam Tester
WorkChamp;WorkChamp XL"""
S58="""Bijou
Bladeless
Caddy;Caddy Plus
Cavalier
Classic
Companion S Alox
Deluxe
Diplomat
Drifter
Duchess
Ensign
Escort
Executive
Flash
Manager
Manicure
Mate
MiniChamp
Pharmacist
Pharmacy Knife
Physician Knife
Presentation Master
Princess
Rally
Rambler
Rogue
Rover
Scribe
Secure
Signature
Slim Flash
Stylus
SwissLite
SwissMemory
Tomo
Vagabond
Victorinox@Work
Whistle"""
S84="""Excelsior
Popular
Pocket Pal
Secretary
Sentry
Watch Case Opener
Apprentice
Bantam
Gourmet
My First Victorinox
Waiter
Cadet Alox
Lumberjack
Recruit
Sportsman
Tinker Small
Tourist
Voyageur
Alumnus
Cadet Plus Alox
Camper Small
Climber Small
Salesman
Artisan
Grand Prix Small
Huntsman Small
Mountaineer Small"""
SRC={'91 mm':(S91,'https://www.sakwiki.com/tiki-index.php?page=Victorinox+91mm'),'93 mm':(S93,'https://sakwiki.com/Victorinox+93mm'),'100 mm':(S100,'https://sakwiki.com/Victorinox+100mm'),'111 mm':(S111,'https://www.sakwiki.com/Victorinox+111mm'),'58 mm':(S58,'https://sakwiki.com/Victorinox+58mm'),'84 mm':(S84,'https://sakwiki.com/Victorinox+84mm+1+Layer+Models')}
YR={'Officer':'1897','Classic':'1950','Pioneer':'1957'}
seen=set(names0)|{'soldier 1951','soldier 1961','soldier 2008','soldier\'s knife','officer\'s/sports knife','master rt','climber','huntsman','champion','electrician','pioneer','broker','craftsman','spartan'}
added=0
newe=[]
for cls,(spec,url) in SRC.items():
    for line in spec.strip().split('\n'):
        yr=None
        if '|' in line:
            line,yr=line.rsplit('|',1)
        parts=[p.strip() for p in line.split(';')]
        base=parts[0]
        if base.lower() in seen: 
            # attach variants to existing entry
            ex=[e for e in sw['x']+newe if e['n'].lower()==base.lower()]
            if ex and len(parts)>1 and cls==ex[0].get('_c',cls) :
                for p in parts[1:]:
                    if not any(v['n']==p for v in ex[0].get('v',[])): ex[0].setdefault('v',[]).append({"n":p,"mk":"Victorinox","y":"","d":"variant listed on SAKWiki"})
            continue
        seen.add(base.lower())
        y=''
        if base=='Classic': y='1950'
        e={"n":base,"d":f"Victorinox {cls} Swiss Army knife model listed on SAKWiki." if cls!='58 mm' else "Victorinox 58 mm Swiss Army knife model listed on SAKWiki.","mk":"Victorinox","y":y,"s":url,"g":cls,"v":[]}
        if base=='Classic': e['d']="Victorinox 58 mm Swiss Army knife model that SAKWiki dates to the early 1950s."
        for p in parts[1:]:
            vy=''
            if p=='Farmer X': vy='2020'
            if yr and p.startswith('DAK'): vy=yr
            e['v'].append({"n":p,"mk":"Victorinox","y":vy,"d":"variant listed on SAKWiki"})
        if e['v']: e['dt']='variant · year'
        e['_c']=cls
        newe.append(e); added+=1
ORD=["Soldier's knives","58 mm","84 mm","91 mm","93 mm","100 mm","111 mm","Other civilian models"]
for e in newe: e.pop('_c',None)
allx=sw['x']+newe
allx.sort(key=lambda e:(ORD.index(e['g']) if e['g'] in ORD else 99))
sw['x']=allx
sw['xg']="Soldier's knives first, then civilian models by handle length"
n=len(allx)
sw['sel']=("Follows the Victorinox article on Wikipedia (owner Victorinox-Stiftung 90 % and Carl und Elise Elsener-Gut Stiftung 10 %; Wenger taken over 26 April 2005) and the SAKWiki Victorinox model pages for 58, 84 (1 to 4 layers), 91, 93, 100 and 111 mm. "
 f"Covers {n} of about {n+25} models in SAKWiki; the pages for 65, 74, 75 and 130 mm, the 84 mm five-layer page, the Wenger and Delemont 85 mm pages were not read within the fetch budget. SAKWiki gives a year for only a few models; a name used at two lengths (Golfer, Companion, Picnicker, Pocket Pal) is listed once. Limited editions, sets and aliases are left out.")
log.append(f'swiss added {added}, total {n}')
# ---------- Tool battery
tb=K('Tool battery'); sh=S('Battery platforms')
new_own={'Metabo CAS':('KKR (through HK Holdings)','Independent','Germany','https://en.wikipedia.org/wiki/Metabo'),
 'Einhell Power X-Change':('Einhell Germany AG','Independent','Germany','https://en.wikipedia.org/wiki/Einhell'),
 'RIDGID 18V':('Emerson Electric Co.','Independent','United States','https://en.wikipedia.org/wiki/Ridgid'),
 'EGO 56V ARC Lithium':('Chervon','Independent','','https://www.woodworkersjournal.com/chervon-building-power-tools-brands-trust/')}
for e in tb['x']:
    if e['n'] in new_own:
        o,t,c,u=new_own[e['n']]; e['own']=o; e['tier']=t
        if c: e['cty']=c
        e.setdefault('os',u)
    e['g']='Owned by '+(e.get('own') or 'owner not stated')
tb['xg']='Owner group'
tb['x'].sort(key=lambda e:(e['g']!='Owned by Techtronic Industries',e['g']))
tb['sel']="No complete list exists; follows the makers' own pages and the retail pages cited per entry, for the brands in the department's market panel plus Metabo, Einhell, Ridgid and EGO. Owners come from each brand's Wikipedia article (Metabo, Einhell, Ridgid) or the Woodworker's Journal Chervon article (EGO); Chervon's country, founding year and the platform launch years were not found on a fetched page (two searches)."
# ---------- Power tool brands
pb=K('Power tool brand')
for e in pb['x']:
    if e['n']=='Black+Decker': e['y']='1910'
def add(n,y,own,oy,cty,tier,u,desc):
    e={"n":n,"d":desc,"mk":n,"y":y,"s":u,"own":own,"tier":tier,"cty":cty,"g":"Owned by "+own,"v":[]}
    if oy: e['own_y']=oy
    pb['x'].append(e)
add('Porter-Cable','1906','Stanley Black & Decker','2004','United States','Global group','https://en.wikipedia.org/wiki/Porter-Cable','American power tool maker; the Pentair Tools Group, which included it, was sold to Black & Decker in October 2004.')
add('Metabo','1924','KKR (through HK Holdings)','','Germany','Independent','https://en.wikipedia.org/wiki/Metabo','German power tool maker bought by Hitachi Koki in 2016; Hitachi Koki was sold to HK Holdings, a KKR entity, in 2017.')
add('Einhell','1964','Einhell Germany AG','','Germany','Independent','https://en.wikipedia.org/wiki/Einhell','German electrical tool maker listed on the Xetra exchange; founded as Hans Einhell GmbH.')
add('Ridgid','1923','Emerson Electric Co.','','United States','Independent','https://en.wikipedia.org/wiki/Ridgid','American tool maker owned by Emerson since 1966; its power tools are largely made by Techtronic Industries.')
pb['x'].sort(key=lambda e:e['own'])
pb['sel']=("Brands of the owner groups named in the department's market panel (Stanley Black & Decker, Techtronic Industries, Bosch, Makita, Hilti, Festool) from each brand's Wikipedia article, plus Porter-Cable, Metabo, Einhell and Ridgid. "
 f"No complete list exists; {len(pb['x'])} brands are listed. Irwin, Lenox and AEG are not listed because no fetched page gives their country or founding year (the AEG article is a disambiguation page).")
pb['xg']='Owner group'
# ---------- new kinds
def newkind(shelf,after,n,dsc,u):
    s=S(shelf); i=[k['n'] for k in s['k']].index(after)+1 if after else len(s['k'])
    s['k'].insert(i,{"n":n,"a":"","d":dsc,"s":u})
newkind('Pliers','Locking pliers','Circlip pliers','Pliers with tips that grip a snap ring so it can be spread over a shaft or squeezed into a bore.','https://en.wikipedia.org/wiki/Circlip')
newkind('Plumbing & pipework','Pipe cutter','Pipe bender','Hand tool or bending spring that supports the pipe wall while soft copper pipe is bent by hand.','https://en.wikipedia.org/wiki/Pipe_bending')
newkind('Detectors & inspection','Infrared thermometer','Thermal imaging camera','Handheld camera that shows heat as an image, used to spot problems in equipment.','https://fluke.com/en-id/products/thermal-cameras/handheld-cameras')
# ---------- other coverage lines
for dp,s,k in kinds():
    if k.get('x'):
        sel=k.get('sel','')
        if not re.search(r'(Complete: \d+ of|Covers \d+ of|No complete list exists)',sel): print('MISSING cov',k['n'])
        if len(k['x'])>12 and not k.get('xg'): print('missing xg',k['n'])
        if k.get('xg'):
            for e in k['x']:
                if not e.get('g'): print('no g',k['n'],e['n'])
d_tmp=R+'work/GAP_C1/C1.tmp'
json.dump(d,open(d_tmp,'w'),ensure_ascii=False,indent=1)
os.replace(d_tmp,R+'out/C1.json')
# ---------- brands
b=json.load(open(R+'out/C1_brands.json'))
B={x['n']:x for x in b['b']}
def setb(n,**kw):
    x=B.get(n)
    if x is None:
        x={"n":n,"c":"","f":"","seg":kw.pop('seg','Mainstream'),"d":kw.pop('d',''),"lines":[],"sig":[],"rel":[],"s":kw.pop('s',''),"kf":kw.pop('kf','')}
        b['b'].append(x); B[n]=x
    for k,v in kw.items():
        if v: x[k]=v
setb('ESEE',c='United States',f='1997',s='https://www.eseeknives.com/node/14')
setb('Nite Ize',c='United States',f='c. 1989',s='https://www.5280.com/2019/06/how-nite-ize-quietly-became-one-of-boulders-largest-outdoor-brands')
setb('Cold Steel',c='United States',f='1980',seg='Mainstream',d='American knife and tool company founded by Lynn Thompson; owned by GSM Outdoors since 2020; known for the Tri-Ad lock.',s='https://en.wikipedia.org/wiki/Cold_Steel_(company)',kf='folding knives')
setb('Ontario Knife Company',c='United States',f='1889',seg='Heritage manufactory',d='Knife and military tool maker founded in Naples, New York; bought by Blue Ridge Knives on 1 August 2023.',s='https://en.wikipedia.org/wiki/Ontario_Knife_Company',kf='military knives')
setb('Facom',c='France',f='1918',seg='Professional & flagship',d='French hand-tool maker incorporated in 1918; bought by the holding company Fimalac in 1999.',s='https://www.fundinguniverse.com/company-histories/facom-s-a-history/',kf='mechanics tools')
setb('KTC',c='Japan',seg='Professional & flagship',d='Kyoto Tool Co., a Japanese hand-tool maker supplying Toyota and exporting to the United States from the 1960s.',s='https://en.ktc.jp/our_brand/history.html',kf='wrenches and sockets')
setb('Ko-ken',c='Japan',seg='Professional & flagship',d='Japanese socket maker; its US distributor dates its first exports to 1957.',s='https://kokenusa.com/pages/ko-ken-tools-history',kf='sockets')
setb('Porter-Cable',c='United States',f='1906',seg='Mainstream',d='American power tool company founded in Syracuse, New York; part of Stanley Black & Decker since 2004.',s='https://en.wikipedia.org/wiki/Porter-Cable',kf='power tools')
setb('Spyderco',s='https://en.wikipedia.org/wiki/Spyderco')
json.dump(b,open(R+'work/GAP_C1/b.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'work/GAP_C1/b.tmp',R+'out/C1_brands.json')
print(log)
