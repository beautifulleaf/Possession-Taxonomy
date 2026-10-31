import json, re
ROOT='/home/user/Possession-Taxonomy/rebuild/'
P=ROOT+'out/E1.json'
d=json.load(open(P))
W='https://en.wikipedia.org/wiki/'
SKIP={'Building & construction','Puzzles, fidgets & desk toys'}
def E(n,d_,s,mk='',y='',a='',v=None,dt='',g=None,role=None,cty=None):
    e={'n':n,'a':a,'d':d_,'mk':mk,'y':y,'s':s,'v':v or []}
    if dt: e['dt']=dt
    if g: e['g']=g
    if role: e['role']=role
    return e
def V(n,d_='',mk='',y=''): return {'n':n,'mk':mk,'y':y,'d':d_}
def kinds():
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']: yield dp,s,k
def kind(name):
    for dp,s,k in kinds():
        if k['n']==name and dp['n'] not in SKIP: return k
    raise KeyError(name)
def sect(name):
    for dp in d['depts']:
        for s in dp['s']:
            if s['n']==name: return s
def has(k,n): return any(e['n'].lower()==n.lower() for e in k.get('x',[]))
def add(k,es):
    k.setdefault('x',[])
    for e in es:
        if not has(k,e['n']): k['x'].append(e)
def setmeta(k,nl,sel,xg=None):
    k['nl']=nl; k['sel']=sel
    if xg: k['xg']=xg
def dropx(k,names):
    k['x']=[e for e in k['x'] if e['n'] not in names]
removed_m={}
# 1. remove loose models everywhere outside the two finished departments
for dp,s,k in kinds():
    if dp['n'] in SKIP: continue
    if 'm' in k:
        removed_m[k['n']]=len(k['m']); del k['m']
CAT=W+'Category:Doll_brands'
def dl(n,d_,mk='',y='',s=CAT,**kw): return E(n,d_,s,mk=mk,y=y,**kw)
# ---- DOLLS
NLD='One entry is a named doll line, maker or tradition sold as its own thing; its revisions and variants are versions.'
def dsel(k,n,m,kindword):
    return f"Follows Wikipedia's Category:Doll brands (fetched: 14 subcategories and 60 pages). Covers {n} of about {m} pages in that category, those that are {kindword}; the other pages are plush, character, electronic, adult or non-doll toys, or belong to other kinds. Earlier entries from their own cited pages are kept."
k=kind('Fashion doll')
b=[e for e in k['x'] if e['n']=='Barbie'][0]
b['v']=[V('Barbie Teen-age Fashion Model (#1)','first doll, 11.5-inch body','Mattel','1959'),V('Barbie Fashionistas','tall, petite and curvy bodies added to the original body','Mattel','2016')]
add(k,[dl('My Scene','Teen fashion doll line.','Mattel'),dl('Ever After High','Teen fashion doll line of fairy-tale descendants.','Mattel'),dl('Rainbow High','Fashion doll line with bright hair and outfits.','MGA Entertainment'),dl('Lottie Dolls','Fashion doll line with a child-like body.','Arklu'),dl('Mariquita Pérez','Spanish fashion doll.'),dl('Betty Spaghetty','Doll with bendable spaghetti-like limbs.'),dl('Bratzillaz','Doll line spun off from Bratz.','MGA Entertainment'),dl('Flavas','Hip-hop styled fashion doll line.'),dl('Madame Alexander Doll Company','American doll maker with named collector doll lines.'),dl('Lady Lovely Locks','Doll line with long hair and hair-play accessories.'),dl('A Girl for All Time','British historical doll line.'),dl('Littlechap Family','Doll family with adult-style bodies and wardrobes.')])
setmeta(k,NLD,dsel(k,0,60,'fashion dolls'))
k['sel']=dsel(k,14,60,'fashion dolls').replace('Covers 0','Covers %d'%(len(k['x'])))
k['sel']="Follows Wikipedia's Category:Doll brands (fetched: 14 subcategories and 60 pages). Covers %d of about 60 pages in that category, the fashion and teen dolls; the other pages are plush, character, electronic, adult or non-doll toys, or belong to other kinds. Earlier entries from their own cited pages are kept."%len([e for e in k['x'] if e['s']==CAT])
k=kind('18-inch play doll')
setmeta(k,NLD,"Follows Wikipedia's Category:Doll brands (fetched). Covers 1 of about 60 pages (American Girl); Our Generation is kept from its own page. No further 18-inch lines appear in the category.")
k=kind('Baby doll')
add(k,[dl('Baby Alive','Baby doll that eats and wets.'),dl('Betsy Wetsy','Baby doll that drinks and wets.'),dl('Cicciobello','Italian baby doll.'),dl('Charmin\' Chatty','Talking doll line.'),dl('Playpal','Large child-sized doll.'),dl('My Buddy','Boy doll sold with a companion pairing.'),dl('Götz','German doll maker with named baby doll lines.')])
setmeta(k,NLD,"Follows Wikipedia's Category:Doll brands (fetched). Covers %d of about 60 pages, the baby and child dolls; the rest are other kinds. Earlier entries from their own cited pages are kept."%len([e for e in k['x'] if e['s']==CAT]))
k=kind('Ball-jointed doll')
add(k,[dl('Dollfie','Volks collector doll line from which Super Dollfie grew.','Volks')])
setmeta(k,NLD,"Follows Wikipedia's Category:Doll brands (fetched). Covers 1 of about 60 pages (Dollfie); Korean and Chinese ball-jointed dolls are kept from their own pages.")
k=kind('Rag doll')
add(k,[dl('Raggedy Ann','Cloth doll with red yarn hair.'),dl('Lenci doll','Felt doll made in Turin.'),dl('Annalee Dolls','Poseable cloth dolls with felt faces.')])
k['nl']=NLD; k['sel']="Follows Wikipedia's Category:Doll brands (fetched). Covers 3 of about 60 pages, the cloth and felt dolls; the rest are other kinds."
k=kind('Antique bisque doll')
add(k,[dl('Jumeau','French maker of bisque bébé dolls.'),dl('Kewpie','Cherub doll first drawn by Rose O\'Neill, made in bisque and later materials.')])
setmeta(k,NLD,"Follows Wikipedia's Category:Doll brands (fetched). Covers 2 of about 60 pages (Jumeau, Kewpie); the French and German types are kept from their own pages.")
for n in ['Traditional doll','Dolls\' house','Dolls\' house miniatures','Playset']:
    kk=kind(n); kk['sel']="No whole-space reference exists for this kind. The entries come from the pages cited on each entry; it has not been matched to a canon."
# brand rule: Sylvanian, Playmobil
dh=kind("Dolls' house")
dh['x']=[e for e in dh['x'] if e['n']!='Sylvanian Families houses']
ps=kind('Playset')
for e in ps['x']:
    if e['n']=='Sylvanian Families': e['v']=[V('Calico Critters','North American name','Epoch','1993')]
    if e['n']=='Playmobil': e['v']=[e2 for e2 in e['v'] if e2['n'] in('Steck-System','System-X','Playmobil 1.2.3 / Junior')]
# teddy bear
k=kind('Teddy bear')
TB=W+'Category:Teddy_bear_manufacturers'
for e in k['x']:
    if e['n']=='Steiff jointed bear':
        e['n']='Steiff'; e['role']='origin'
        e['d']='German maker whose 55 PB is described as the first plush bear with movable arms and legs.'
        e['v']=[V('55 PB','original jointed design; no original survives','Steiff','1902'),V('Black Titanic mourning bear','black bears made after the sinking','Steiff','1912'),V('Harlequin bear','','Steiff','1925')]
        e['s']=W+'Steiff'
    if e['n']=="Teddy's bear (Michtom)": e['n']='Ideal Novelty and Toy Co.'
dropx(k,['Storybook bears'])
add(k,[E('Chad Valley','English toy maker listed among teddy bear manufacturers.',TB),E('J. K. Farnell','English teddy bear maker.',TB),E('Teddy-Hermann','German teddy bear maker.',TB),E('Vermont Teddy Bear Company','American teddy bear maker.',TB),E('Build-A-Bear Workshop','Retailer where customers stuff and dress their own bear.',TB),E('Jellycat','British soft-toy maker.',TB,mk='Jellycat'),E('Bukowski Design','Swedish soft-toy maker.',TB),E('Forever Toys','Teddy bear maker listed in the category.',TB),E('Charleen Kinser','Artist teddy bear maker.',TB),E('Teddy Atelier Stursberg','German artist teddy bear maker.',TB)])
for e in k['x']: e.setdefault('g','Maker')
setmeta(k,"One entry is a teddy bear maker sold under its own name; its landmark bears and revisions are versions.","Follows Wikipedia's Category:Teddy bear manufacturers. Complete: 14 of 14 pages in that category (Steiff, Merrythought, Gund and Ideal as earlier entries; Gund and Merrythought keep their own cited pages). Storybook bears is removed as it is not a maker.")
pl=kind('Plush toy')
dropx(pl,['Jellycat Bashful Bunny'])
add(pl,[dl('Monchhichi','Monkey-like plush doll with a sucking thumb.'),dl('Pound Puppies','Plush puppies sold with adoption papers.'),dl('Furskin Bears','Plush bear line.'),dl('The Hugga Bunch','Plush family line.')])
setmeta(pl,"One entry is a named plush line or brand; its sizes and revisions are versions.","Follows Wikipedia's Category:Doll brands (fetched) for the plush lines it names. Covers 4 of about 60 pages; Jellycat moved to Teddy bear, where the maker category lists it. Earlier entries are kept from their own pages.")
for e in pl['x']:
    if e['n']=='Beanie Babies': e['v']=[v for v in e['v'] if v['n']!='Poem swing tags']
# ---- ACTION FIGURES
k=kind('Action figure')
GJ=W+'List_of_G.I._Joe_series'; KS=W+'Kenner_Star_Wars_action_figures'; MU=W+'Masters_of_the_Universe'
k['x']=[e for e in k['x'] if e['n'] not in('G.I. Joe','Kenner Star Wars','Masters of the Universe')]
for e in k['x']: e['g']='Other toy lines'
gj=[('G.I. Joe: America\'s Movable Fighting Man','Hasbro','1964'),('G.I. Joe Adventure Team','Hasbro','1970'),('G.I. Joe: A Real American Hero','Hasbro','1982'),('G.I. Joe Hall of Fame','Hasbro','1991'),('Sgt. Savage and his Screaming Eagles','Hasbro','1994'),('G.I. Joe Classic Collection','Hasbro','1995'),('G.I. Joe Masterpiece Edition','Hasbro','1996'),('G.I. Joe Extreme','Hasbro','1996'),('G.I. Joe Timeless Collection','Hasbro','1998'),('G.I. Joe vs. Cobra','Hasbro','2002'),('G.I. Joe Sigma 6','Hasbro','2005'),('G.I. Joe 25th Anniversary','Hasbro','2007')]
ks=[('Early Bird Certificate Package','1977'),('Star Wars cardbacks','1977'),('Empire Strikes Back cardbacks','1980'),('Return of the Jedi cardbacks','1983'),('Power of the Force cardbacks','1984'),('Power of the Force figures with collector coins','1985'),('Droids','1985'),('Ewoks','1985'),('Power of the Force modern line','1995'),('Shadows of the Empire promotional figures','1996'),('Special Edition promotional figures','1997'),('Phantom Menace quote-chip figures','1999'),('Trilogo cardbacks, European market','')]
mu=[('Masters of the Universe (original toyline)','1982'),('Princess of Power','1985'),('He-Man: The New Adventures','1989'),('Masters of the Universe (200X)','2002'),('Masters of the Universe Classics and Super7','2008'),('Masters of the Universe Minis','2013'),('Masters of the Universe Origins','2019'),('She-Ra and the Princesses of Power','2019'),('Masters of the Universe Masterverse','2021'),('Masters of the Universe Chronicles and Core','2026')]
new=[E(n,'G.I. Joe toy line.',GJ,mk=m,y=y,g='G.I. Joe') for n,m,y in gj]
new+=[E(n,'Kenner Star Wars figure line or card series.',KS,mk='Kenner',y=y,g='Star Wars (Kenner)') for n,y in ks]
new+=[E(n,'Masters of the Universe toy line.',MU,mk='Mattel',y=y,g='Masters of the Universe') for n,y in mu]
k['x']=new+k['x']
setmeta(k,"One entry is a named action-figure toy line; its re-releases are versions.","G.I. Joe, Kenner Star Wars and Masters of the Universe follow fetched lists (Wikipedia's List of G.I. Joe series, Kenner Star Wars action figures, and the Masters of the Universe article). Complete: 12 of 12 G.I. Joe toylines, 13 of 13 Kenner Star Wars series and 10 of the 10 Masters of the Universe toylines the article names. Other lines are earlier entries from their own pages; Wikipedia's Category:Action figures names about 130 more lines that are not yet entered.","by franchise")
# Transformers
k=kind('Transforming robot toy')
for e in k['x']:
    if e['n']=='Transformers':
        e['v']=[V('Generation 1','Series 1, 28 figures','Hasbro','1984'),V('Generation 2','','Hasbro','1993'),V('Beast Wars','','Hasbro','1996'),V('Masterpiece','collector-scale figures, later MP36 Megatron','Takara Tomy','')]
dropx(k,['Transformers Masterpiece'])
k['sel']="No whole-space reference exists for this kind. The entries come from the pages cited on each entry; Transformers is one entry whose versions are generations and scale."
# toy soldiers
k=kind('Toy soldier & animal figure')
TSB=W+'List_of_toy_soldiers_brands'
add(k,[E(n,'Toy soldier brand named in Wikipedia\'s list of toy soldier brands.',TSB) for n in ['Elastolin','Lineol','Timpo Toys','Crescent Toys','Louis Marx and Company','Manoil','Barclay','Heyde','Airfix']])
k['x'].sort(key=lambda e:e['n']) if False else None
setmeta(k,"One entry is a toy soldier or animal figure maker sold under its own name.","Follows Wikipedia's List of toy soldiers brands (fetched, about 150 names). Covers 9 of about 150; the rest are not yet entered. The earlier loose models (battle sets and brand names) are folded into these maker entries or removed.")
k=kind('Bobblehead')
# ---- MODELS
k=kind('Scale model kit')
POLY='''Academy Plastic Model (Korea)|Accurate Miniatures (USA)|Ace (Ukraine)|Ace Corporation (Korea)|Addar (USA)|Admiral (Czech Republic)|AFV Club (Taiwan)|Aim Fan Model (Ukraine)|Airfix (UK)|AK Interactive (Spain)|Alanger (Russia)|Alan Hobby (Russia)|AMT (USA)|Amusing Hobby (Japan)|Aoshima Bunka Kyozai (Japan)|Arii (Japan)|Ark Models (Russia)|Arma Hobby (Poland)|Arsenal Model Group (Ukraine)|Art Model (Ukraine)|Asuka Model (Japan)|Atlantis Models (USA)|Aurora Plastics Corporation (USA)|AvantGarde Model Kits (Macau)|AVD Models (Russia)|Avis (Ukraine)|Bandai (Japan)|Balaton Model (Hungary)|Beemax Model Kit (Macau)|Belkits (Belgium)|Big Planes Kits (Ukraine)|Bílek (Czech Republic)|Black Label (China)|Border Models (China)|Bronco Models (Hong Kong)|Caesar Miniatures (Taiwan)|Cavico (Japan)|C.C.Lee (China)|Clear Prop! (Ukraine)|Condor (Ukraine)|Cooperativa (Russia)|Copper State Models (Latvia)|Crown (Japan)|Cyber Hobby (China)|Czech Model (Czech Republic)|Daco Plast (Russia)|Davric (UK)|Delta 2 (Italy)|Dora Wings (Ukraine)|Doyusha (Japan)|Dragon Models Limited (Hong Kong)|Dream Model (China)|Eaglewall (UK)|Eastern Express (Russia)|Ebbro (Japan)|Eduard (Czech Republic)|Emhar (UK)|E-Model (China)|Encore E Models (USA)|ESCI (Italy)|Faller (Germany)|Fine Molds (Japan)|FinMilModels (Finland)|First To Fight (Poland)|Flagman (Russia)|Flametoys (Japan)|FlyHawk Model (China)|Foresight (Japan)|Freedom Model Kits (Taiwan)|Frog (UK)|Fujimi Mokei (Japan)|Games Workshop (UK)|Gaspatch Models (Greece)|Gecko Models (Hong Kong)|Gallery Models (USA)|Glencoe Models (USA)|Good Smile Company (Japan)|Gowland & Gowland (USA)|Great Wall Hobby (China)|GSI Creos (Japan)|Hasegawa (Japan)|HäT (USA)|Hawk (USA)|Hehexing (China)|Heller SA (France)|HK Models (Hong Kong)|HMA Garage (Japan)|Hobby Boss (China)|Hobbycraft (Canada)|Hobby Japan (Japan)|Huma Modell (Germany)|Humbrol (UK)|IBG Models (Poland)|ICM Holding (Ukraine)|Ideal Toy Company (USA)|Ilovekit (China)|Imai Kagaku (Japan)|Imex Model (USA)|Imperial Hobby Productions (USA)|Italeri (Italy)|Jo-Han (USA)|Kaiyodo (Japan)|Kawai (Japan)|Kinetic (Hong Kong)|Kiel Kraft (UK)|Kitty Hawk Models (China)|Kleeware (UK)|Kotobukiya (Japan)|KP Models (Czech Republic)|Life-Like (USA)|Lincoln International (Hong Kong)|Lindberg Models (USA)|Lion Roar (China)|LS (Japan)|Maco (Germany)|Magic Factory (China)|Marusan (Japan)|Master Model (Germany)|Master Box (Ukraine)|Matchbox (UK)|Max Factory (Japan)|Meng Model (China)|Merit (UK)|Merit International (China)|Micro Ace (Japan)|MiniArt (Ukraine)|Minicraft (USA)|Miniwing (Czech Republic)|Mirage Hobby (Poland)|Mirror Models (Ireland)|Mitsuwa Model (Japan)|Model Products Corporation (USA)|Modelcollect (China)|Modelcraft (Canada)|Modelex (Argentina)|Modelkasten (Japan)|Modelsvit (Ukraine)|Moebius Models (USA)|Monochrome (Japan)|Monogram (USA)|Monti System (Ukraine)|Mr. Hobby (Japan)|MSD Model (Russia)|Nagano (Japan)|Nichimo (Japan)|Nihon Plastic (Japan)|Nitto Kagaku (Japan)|Nu-Bee (Germany)|Nunu (Macau)|Occidental Réplicas (Portugal)|Otaki (Japan)|Orange Cat Industry (China)|Pacific Coast Models (USA)|Panda Hobby (Hong Kong)|Paramount (UK)|Palmer Plastics (USA)|Peco (UK)|Pegasus Hobbies (USA)|Pilot-Replicas (Sweden)|Pit-Road (Japan)|Plásticos Lodela (Mexico)|Plastic Soldier (UK)|Platz (Japan)|Playfix (Germany)|Plum (Japan)|PM Model (Turkey)|Preiser (Germany)|Protar (Italy)|PST (Belarus)|Pyro Plastics Corporation (USA)|Ratio (UK)|Renwal (USA)|Revell (USA)|Riich Models (China)|Roden (Ukraine)|ROKR (China)|Rosebud Kitmaster (UK)|Rosso (Japan)|Rubicon Models (UK)|R.V.Aircraft (Czech Republic)|Ryefield Model (Hong Kong)|Salvinos JR Models (USA)|Sankyo Mokei (Japan)|Sanwa Plastic (Japan)|Scalecraft (UK)|Skilcraft (USA)|Skunkmodels (Hong Kong)|Směr (Czech Republic)|S-Model (China)|Special Hobby (Czech Republic)|Starfix (Israel)|Strombecker (USA)|Sunny International (Japan)|Supermodel (Italy)|Suyata (Hong Kong)|Sweet (Japan)|Takom (Hong Kong)|Tamiya (Japan)|Tan Model (Turkey)|Tarangs (Sweden)|Tauro Model (Italy)|Testor Corporation (USA)|Tiger Model (Hong Kong)|Thunder Model (China)|Tokyo Marui (Japan)|Tomytec (Japan)|Toxso Model (China)|Trimaster (Japan)|Tristar (Hong Kong)|Trumpeter (China)|Tsukuda Hobby (Japan)|Unimodel (Ukraine)|Union Model (Japan)|Varney (USA)|VEB Plasticart (Germany)|Very Fire (China)|Vespid Models (China)|Vision Models (Taiwan)|Vulcan (UK)|Vulcan Scale Models (Hong Kong)|Wako (Japan)|Waltersons (Hong Kong)|Wave Corporation (Japan)|Williams Bros. (USA)|Wills Finecast (UK)|Wingsy Kits (Ukraine)|Wingnut Wings (New Zealand)|Xact Scale Models (Hong Kong)|Xuntong Model (China)|Yamashita Hobby (Japan)|Zoukei Mura (Japan)|ZTS Plastyk (Poland)|Zvezda (Russia)|12 Squad (USA)|Amodel (Ukraine)|Armory (Ukraine)|Aviation USK (USA)|AVI Models (Czech Republic)|AZ Model (Czech Republic)|Azur (Czech Republic)|Brengun (Czech Republic)|Fonderie Miniatures (France)|F-RSIN (France)|Fly Models (Czech Republic)|Griffon Model (Japan)|High Planes Models (Australia)|JAYS Model Kits (New Zealand)|Kiwi Wings (New Zealand)|Kora Models (Czech Republic)|Legato (Czech Republic)|Leoman (USA)|Mach2 (France)|Maquette (Russia)|Mark I. Models (Czech Republic)|Merlin Model (UK)|Military Wheels (Ukraine)|Mikromir (Ukraine)|MPM production (Czech Republic)|Olimp Model (Ukraine)|OzMods Scale Models (Australia)|Pavla Models (Czech Republic)|Pegasus (UK)|RS Models (Czech Republic)|Skif (Ukraine)|Sova-M (Ukraine)|Sword (Czech Republic)|Tasman Models (New Zealand)|Valom (Czech Republic)|Ventura Models (New Zealand)|Airmodel (Germany)|Broplan (Poland)|Combat Models (USA)|Contrail (UK)|Dinavector (Japan)|Dubena (Czechoslovakia)|Execuform (USA)|Formaplane (UK)|General Products (Japan)|Gerald J. Elliott (UK)|Modakit (UK)|ModelsPark (Latvia)|PSC (Czechoslovakia)|Rareplanes (UK)|Sanger (UK)'''
KM=W+'List_of_scale_model_kit_manufacturers'
seen={}
for it in POLY.split('|'):
    m=re.match(r'(.*) \((.*)\)$',it); n,c=m.group(1),m.group(2)
    key=n.lower()
    if key in seen: continue
    seen[key]=(n,c)
kx=[E(n,'Polystyrene scale model kit maker, %s.'%c,KM,g=c) for n,c in seen.values()]
kx.sort(key=lambda e:(e['g'],e['n'].lower()))
k['x']=kx; k.pop('r',None)
setmeta(k,"One entry is a company that makes scale model kits under its own name; its kits are what it sells, not entries.","Kit makers follow Wikipedia's List of scale model kit manufacturers (fetched). Covers the %d distinct makers in its three polystyrene sections (high-pressure, short-run and vacuum formed; makers listed in two sections are counted once). The resin, metal, wood, card and 3D-printed sections were not read. The earlier loose kit models (Spitfire, Panther and others) are removed: a kit belongs to its maker."%len(kx),"by home country")
for e in kx:
    if e['n']=='Airfix': e['role']='origin' if False else None
    if not e.get('role'): e.pop('role',None)
# die-cast
k=kind('Die-cast model')
DC=W+'List_of_model_car_brands'
for e in k['x']:
    if e['n']=='Matchbox 1-75':
        e['n']='Matchbox'; e['v']=[V('First three models','road roller, dump truck, cement mixer','Lesney','1953'),V('Models of Yesteryear','','Lesney','1956'),V('King Size','larger scale','Lesney','1960'),V('Superfast','low-friction wheels','Lesney','1969')]
    if e['n']=='Hot Wheels':
        e['v']=[v for v in e['v'] if v['n'] in('Mainline 1:64','Gran Toros 1:43','Sizzlers','Elite and replica models')]
dcl=[('Bburago','Italy'),('Brumm','Italy'),('Budgie Toys','England'),('Husky Toys','United Kingdom'),('Majorette','Germany'),('Maisto','made in Thailand'),('Minichamps','Germany'),('Norev','France'),('Oxford Diecast','United Kingdom'),('Polistil / Politoys','Italy'),('Johnny Lightning',''),('Joal','Spain'),('Guisval','Spain'),('Playart','Hong Kong'),('Mebetoys','Italy'),('Eligor Models','Switzerland/France'),('Gasquy-Septoy','Belgium'),('Efsi Toys','Netherlands'),('Best Box','Netherlands'),('AUTOart',''),('GreenLight',''),('Jada Toys',''),('Auto World','United States'),('Racing Champions','United States'),('Motormax','China'),('New-Ray','Hong Kong'),('Cararama','China'),('Hubley Manufacturing Company','United States'),('Lone Star Toys','United Kingdom'),('Crescent Toys','United Kingdom')]
add(k,[E(n,'Model car maker named in Wikipedia\'s list of model car brands%s.'%((', '+c) if c else ''),DC,mk=n,g='Other makers') for n,c in dcl])
for e in k['x']: e.setdefault('g','Founding lines')
k.pop('r',None)
setmeta(k,"One entry is a die-cast model car brand sold under its own name; its scale and system changes are versions.","Follows Wikipedia's List of model car brands (fetched, entries A to R only; the page continues to about 167,000 characters). Covers %d of about 130 listed up to R; the list mixes die-cast, plastic and resin makers, so only makers I took to be die-cast are entered. Hot Wheels and Matchbox stay one entry each."%len(k['x']))
# railway
sc=sect('Model railways')
RS=W+'Rail_transport_modelling_scales'
sd=[('Z','1:220','6.5 mm'),('N','1:160','9 mm'),('TT','1:120','12 mm'),('H0','1:87','16.5 mm'),('S','1:64','22.5 mm'),('0','1:45','32 mm'),('1','1:32','45 mm'),('II','1:22.5','64 mm'),('III','1:16','89 mm'),('V','1:11','127 mm'),('VII','1:8','184 mm'),('X','1:5.5','260 mm')]
rk={'n':'Model railway scale and gauge','a':'','d':'A standard ratio and track gauge to which model trains and track are made.','s':RS,'x':[E('%s scale'%n if n[0].isalpha() or n.isdigit() else n,'Scale %s on %s track (NEM standard gauge).'%(r,g_),RS,a='') for n,r,g_ in sd]}
for e,(n,r,g_) in zip(rk['x'],sd): e['dt']=r+' · '+g_; e['g']='NEM standard scale'
rk['nl']='One entry is a standard model railway scale and its track gauge.'
rk['sel']="Wikipedia's Rail transport modelling scales (fetched). Covers 12 standard-gauge scales of the NEM table; the page's narrow-gauge, NMRA, British and Japanese tables were not itemised by the reader and are not yet entered."
rk['xg']='by standard'
sc['k'].insert(0,rk)
for n in['Model railway train set','Model locomotive','Model rolling stock','Model railway track','Model railway controller','Model railway scenery & buildings']:
    kk=kind(n)
    kk['sel']="No whole-space reference exists for this kind. The entries come from the pages cited on each entry; scales and gauges are in Model railway scale and gauge, kit makers in Scale model kit."
# ---- BOARD AND CARD
k=kind('Playing cards')
PC=W+'Playing_card'
for e in k['x']: e['g']='Pattern'
sys_=[('French-suited deck','Hearts, Diamonds, Clubs, Spades'),('German-suited deck','Hearts, Bells, Acorns, Leaves'),('Swiss-suited deck','Roses, Bells, Acorns, Shields'),('Italian-suited deck','Cups, Coins, Clubs, Swords'),('Spanish-suited deck','Cups, Coins, Clubs, Swords')]
k['x']=[E(n,'Deck using the suits %s.'%s_,PC,g='Suit system') for n,s_ in sys_]+k['x']
setmeta(k,"One entry is a deck suit system or regional deck pattern.","Suit systems follow Wikipedia's Playing card (fetched, first 100,000 of 182,000 characters): Complete: 5 of 5 suit systems asked for (French, German, Swiss, Italian, Spanish). Patterns are earlier entries from their own pages; the page itself names only the English and Belgian-Genoese patterns in the part read.","by suit system, then pattern")
kind('Hanafuda deck').pop('see',None) if False else None
k=kind('Trading card packs & boxes'); 
for f in('x','nl','sel','xg'): k.pop(f,None)
k=kind('Trading card single')
for f in('x','nl','sel','xg'): k.pop(f,None)
k=kind('Miniatures game starter set')
dropx(k,['Bolt Action','Star Wars: X-Wing'])
setmeta(k,"One entry is a miniatures-game brand whose starter sets and models are sold as one catalogue.","Warhammer from Wikipedia's Warhammer (game) article; one entry, its versions are game systems. Bolt Action and X-Wing are game titles and are removed.")
k=kind('Reversi set'); dropx(k,['Othello'])
k=kind('Dexterity game'); dropx(k,['Jenga','KerPlunk'])
setmeta(k,k['nl'],"The classic public-domain game is the entry; branded games such as Jenga and KerPlunk are titles and are removed.")
# ---- PRETEND
k=kind('Foam dart blaster')
nerf=E('Nerf','Foam-dart blaster brand; dart and ammunition systems are its versions.',W+'Nerf',mk='Nerf',y='2004',v=[V('N-Strike','first big blaster system','Nerf','2004'),V('N-Strike Elite','update of N-Strike darts','Nerf','2012'),V('Rival','High Impact Rounds','Nerf','2015'),V('Ultra','proprietary dart design','Nerf','2019')])
k['x']=[nerf]+[e for e in k['x'] if not e['n'].startswith('Nerf')]
k.pop('r',None)
setmeta(k,"One entry is a foam or gel blaster brand; its dart systems are versions.","Nerf is one entry from Wikipedia's Nerf article; Gel blaster is a separate type. No whole-space canon exists.")
kind('Water blaster').pop('r',None)
for n in ['Toy sword','Water play toy','Swing set']: kind(n).pop('r',None)
# ---- BABY
k=kind('Bath toy')
k['x']=[E('Rubber duck','Floating bath toy; Peter Ganine\'s duck design was patented in 1949 and over 50 million were sold.',W+'Rubber_duck',v=[V('Ganine floating duck','design patent filed 1947','', '1947'),V('Winsome Plastic Works duck','','Winsome Plastic Works','1948')],role='landmark')]
setmeta(k,"One entry is a classic bath toy named by a fetched page.","Rubber duck from Wikipedia's Rubber duck article (National Toy Hall of Fame 2013). Commodity kind: no other named entries.")
# ---- SKILL
k=kind('Toy flying disc')
for e in k['x']:
    if e['n']=='Pluto Platter / Frisbee':
        e['role']='landmark'; e['d']='Disc designed by Walter Frederick Morrison in 1955 and sold to Wham-O in 1957; Wikipedia calls it the archetype of all modern flying discs.'
        e['v']=[V('Pluto Platter','','Wham-O','1955'),V('Frisbee name','after Frisbie Pie Company tins','Wham-O','1957'),V('Redesign by Ed Headrick','','Wham-O','1964')]
k.pop('r',None)
hk={'n':'Hula hoop','a':'','d':'A light ring spun around the waist, limbs or neck.','s':W+'Hula_hoop','x':[E('Toltoys plastic hoop','Australian maker that began mass-producing plastic hoops; 400,000 sold in 1957.',W+'Hula_hoop',mk='Toltoys',y='1957'),E('Wham-O hula hoop','Plastic hoop that set off the 1958 craze; 25 million sold in under four months.',W+'Hula_hoop',mk='Wham-O',y='1958',v=[V('Ball-bearing hoop','added a rattling sound','Wham-O','1965')],role='landmark')]}
hk['nl']='One entry is a named hula hoop product that a fetched page calls first or defining.'
hk['sel']="Wikipedia's Hula hoop (fetched). Commodity kind: it keeps the first mass-produced plastic hoop and the 1958 craze hoop (Toy Hall of Fame 1999) only."
s=sect('Throw, roll & fly toys'); s['k'].append(hk)
s2=sect('Throw, roll & fly toys')
# ---- market panel
ad=[x for x in d['depts'] if x['n'].startswith('Action figures')][0]
ST='https://www.statista.com/statistics/241241/revenue-of-major-toy-companies-worldwide'
ad['ms']=[{"mkt":"Global toy companies, by revenue","who":"LEGO Group","share":"1st of the companies listed","yr":2025,"s":ST,"note":"rank only; the page masks the revenue figure"},{"mkt":"Global toy companies, by revenue","who":"Bandai Namco","share":"2nd of the companies listed","yr":2025,"s":ST,"note":"rank only; fiscal year ended 31 March 2026, figure masked"}]
# ---- non-entry kinds: strip stale sel on kinds with no x
for dp,s,k in kinds():
    if dp['n'] in SKIP: continue
    if not k.get('x'):
        for f in('nl','sel','xg'): k.pop(f,None)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1)
import os; os.replace(P+'.tmp',P)
print(removed_m, sum(removed_m.values()))
