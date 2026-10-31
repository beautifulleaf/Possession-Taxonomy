import json, os, re
B='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(B+'out/J10.json')); br=json.load(open(B+'out/J10_brands.json'))
WP='https://en.wikipedia.org/wiki/'
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
def kind(name):
    for D in d['depts']:
        for S in D['s']:
            for K in S['k']:
                if K['n']==name:
                    K.setdefault('x',[]); return K
    raise KeyError(name)
def dept(name):
    return [D for D in d['depts'] if D['n']==name][0]
def shelf(dn,sn):
    return [S for S in dept(dn)['s'] if S['n']==sn][0]
registered={b['n'] for b in br['b']}
newbrands={}
def reg(n,c='',f='',seg='',kf='',dsc='',s='',lines=None):
    if n in registered or n in newbrands: return
    e={'n':n,'c':c,'f':f,'seg':seg or 'Independent','kf':kf,'d':dsc,'s':s}
    if lines: e['lines']=lines
    newbrands[n]=e

# ---------- A. Habanos ----------
HAB='https://www.habanos.com/en/the-habanos-brands-academia/'
tiers=[('Global brands',['Cohiba','Montecristo','Romeo y Julieta','Partagás','Hoyo de Monterrey','H. Upmann']),
 ('High value brands',['Trinidad','Bolívar','Punch',"Quai d'Orsay",'Ramón Allones']),
 ('Volume brands',['José L. Piedra','Quintero','Vegueros']),
 ('Rest of the portfolio',['Cuaba','San Cristóbal de la Habana','Fonseca','Vegas Robaina','Diplomáticos','El Rey del Mundo','Juan López','La Flor de Cano','La Gloria Cubana','Por Larrañaga','Rafael González','Saint Luis Rey','Sancho Panza'])]
K=kind('Habano (Cuban premium cigar)')
old=K['x']; oldm=K.get('m',[])
def okey(mk): return norm(mk)
new=[]
for g,names in tiers:
    for n in names:
        lines=[e for e in old if norm(e.get('mk',''))==norm(n) or norm(e['n']).startswith(norm(n))]
        e={'n':n,'a':'','d':'','mk':n,'y':'','s':HAB,'g':g,'own':'Habanos S.A.','tier':'Global group' if g=='Global brands' else 'National champion','cty':'Cuba'}
        vs=[]
        for l in lines:
            if not e['d'] and l.get('d'): e['d']=l['d']
            if not e['y'] and l.get('y'): e['y']=l['y']
            if l.get('s') and 'wikipedia' in l['s']: e['s2']=l['s']
            if not l.get('v'):
                if l is not lines[0] or len(lines)>1: vs.append({'n':l['n'],'y':l.get('y',''),'d':l.get('d','')})
            for v in l.get('v',[]):
                vs.append({'n':v['n'],'y':v.get('y',''),'d':(l['n']+('; '+v['d'] if v.get('d') else ''))})
        for mn,mo in oldm:
            if norm(mo)==norm(n): vs.append({'n':mn,'y':'','d':'vitola of '+n})
        if not e['d']: e['d']=f'Cuban premium cigar marque in the Habanos S.A. portfolio, listed under {g.lower()}.'
        e['v']=vs
        e['s']=e.pop('s2',e['s']) if False else e['s']
        new.append(e)
for e in new:
    if e['n']=='Montecristo': e['role']='landmark'
K['x']=new; K['m']=[]
K['nl']='One entry is a Cuban cigar marque sold by Habanos S.A. under its own name; its lines and vitolas (shape and size) are versions.'
K['sel']=('Every marque in the Habanos S.A. portfolio as listed on the Habanos Brands-Academia page, grouped by the portfolio tier the page gives (global, high value, volume, rest). Versions are the lines and vitolas found on the Wikipedia pages read earlier; marques without versions have no vitola list on a fetched page. '
 'Complete: 27 of 27 marques in the Habanos Brands-Academia page. Habanos S.A. was established in 1994 and is held equally by Cubatabaco and Altadis, whose stake Imperial Tobacco sold in 2020 (Wikipedia, Habanos S.A.).')
K['xg']='by Habanos portfolio tier'

# ---------- B. non-Cuban marques ----------
LIST=WP+'List_of_cigar_brands'
GLOB='Global group'; IND='Independent'
# (kind, name, country, owner, tier)
rows=[
('Dominican premium cigar','Arsen','Dominican Republic','Corporacion Cigar Export',IND),
('Dominican premium cigar','AVO','Dominican Republic','Davidoff',GLOB),
('Dominican premium cigar','Baccarat','Dominican Republic','Davidoff / Imperial Tobacco',GLOB),
('Dominican premium cigar','Carlos Toraño','Dominican Republic','General Cigar Company',IND),
('Dominican premium cigar','Diamond Crown','Dominican Republic','J.C. Newman',IND),
('Dominican premium cigar','Don Diego','Dominican Republic','Altadis',GLOB),
('Dominican premium cigar','Ernesto Perez-Carrillo','Dominican Republic','Perez-Carrillo Tabacalera La Alianza S.A.',IND),
('Dominican premium cigar','Henry Clay','Dominican Republic','Altadis',GLOB),
('Dominican premium cigar','Macanudo','Dominican Republic','General Cigar Company',IND),
('Dominican premium cigar','Montesino','Dominican Republic','Arturo Fuente',IND),
('Dominican premium cigar','Oliveros','Dominican Republic','Boutique Blends Cigars',IND),
('Dominican premium cigar','Quesada','Dominican Republic','Matasa',IND),
('Dominican premium cigar','Swag','Dominican Republic','Boutique Blends Cigars',IND),
('Dominican premium cigar','Vegafina','Dominican Republic','Altadis',GLOB),
('Dominican premium cigar','Zino','Dominican Republic','Davidoff',GLOB),
('Nicaraguan premium cigar','Cain','Nicaragua','Oliva Cigar Co.',IND),
('Nicaraguan premium cigar','Cigar Jesus','Nicaragua','Cigar Jesus',IND),
('Nicaraguan premium cigar','Don Pepin Garcia','Nicaragua','Tabacalera Nicaragua (Estelí)',IND),
('Nicaraguan premium cigar','Nub','Nicaragua','Oliva Cigar Co.',IND),
('Nicaraguan premium cigar','Plasencia','Nicaragua','Nestor Plasencia',IND),
('Nicaraguan premium cigar','San Miguel','Nicaragua','A. J. Fernandez Cigars',IND),
('Honduran premium cigar','Don Tomas','Honduras','General Cigar Company',IND),
('Honduran premium cigar','Flor de Selva','Honduras','Maya Selva',IND),
('Honduran premium cigar','Gispert','Honduras','Habanos S.A.; Altadis',GLOB),
('Honduran premium cigar','HPC','Honduras','Honduras Premium Cigars',IND),
('Honduran premium cigar','Villa Zamorano','Honduras','Maya Selva',IND),
('Mexican & Brazilian cigar','Windsor','Mexico','San Andres Southern Tobacco Co.',IND),
('Cigar from other countries','Chaman','Costa Rica','Vegas de Santiago',IND),
('Cigar from other countries','Bongani','Mozambique','Bongani Cigars',IND),
('Cigar from other countries','Alhambra','Philippines','Tabacalera Incorporada',IND),
('Cigar from other countries','Don Juan Urquijo','Philippines','Tabacalera Incorporada',IND),
('Cigar from other countries','Tabacalera','Philippines','Tabacalera Incorporada',IND),
('Cigar from other countries','Djarum','Indonesia','Djarum',IND),
('Cigar from other countries','Wolf & Eagles','Indonesia','Surobakku Group',IND),
('Cigar from other countries','Ritmeester','Netherlands','Dannemann Cigars',IND),
('Cigar from other countries','Willem II','Netherlands','Swedish Match',GLOB),
('Cigar from other countries','Vamma Del Sol','Greece','Konstantinedes Bros',IND),
('Cigar from other countries','Familija','Australia','Familija Cigars',IND),
('Cigar from other countries','Nicoya','Australia','Nicoya Cigars',IND),
('Cigar from other countries','Farvardin','Iran','Iranian Tobacco Company',IND),
('Cigar from other countries','Oliva (Belgian house)','Belgium','J. Cortès Cigars N.V.',IND),
('Cigar from other countries','King Edward the Seventh','United States','Swisher International Group',IND),
('Cigar from other countries','El Sol','United States','El Sol Cigars',IND),
('Cigar from other countries','Ben-Hur','United States','Wm. Tegge & Co.',IND),
('Cigar from other countries','Pacemaker','United States','Waitt & Bond',IND),
]
# new kind
NW=shelf('Cigars','New World premium cigars')
if not any(k['n']=='Cigar from other countries' for k in NW['k']):
    NW['k'].append({'n':'Cigar from other countries','a':'','d':'Cigar marque made outside the Americas\' main premium-cigar countries: Costa Rica, Mozambique, the Philippines, Indonesia, Europe, Australia, Iran and the United States.','s':LIST,'tt':[['Format',['Premium handmade','Machine-made']]],'x':[],'m':[]})
ownmap={ # existing entries: owner stated by List of cigar brands -> (own, tier)
 'Arturo Fuente':('Arturo Fuente',IND),'Davidoff':('Davidoff',GLOB),'La Flor Dominicana':('La Flor Dominicana',IND),
 'Ashton':('Arturo Fuente',IND),'AJ Fernandez':('AJ Fernandez Incorporated',IND),'AJ Fernandez Cigars':('AJ Fernandez Incorporated',IND),
 'Camacho':('Oettinger Davidoff Group',GLOB),'Tatuaje':('Pete Johnson',IND),'Perdomo':('Tabacalera Perdomo',IND),'Joya de Nicaragua':('Joya de Nicaragua',IND),
 'My Father Cigars':('Jose Don Pepin Garcia',IND),'Oliva':('Oliva Cigar Co.',IND),'Dannemann':('Dannemann GmbH',IND),'Alec Bradley':('Alec Bradley',IND),
 'Rocky Patel':('owner not stated',IND),'Padrón':('owner not stated',IND),'CAO':('owner not stated',IND),'Drew Estate':('owner not stated',IND),
 'Te-Amo':('owner not stated',IND),'Santa Clara':('owner not stated',IND),'E.P. Carrillo':('owner not stated',IND),
}
kc={'Dominican premium cigar':'Dominican Republic','Nicaraguan premium cigar':'Nicaragua','Honduran premium cigar':'Honduras','Mexican & Brazilian cigar':'Mexico or Brazil'}
for kn,cty in kc.items():
    Kk=kind(kn)
    for e in Kk['x']:
        o=ownmap.get(e.get('mk',''))
        if o and 'own' not in e: e['own'],e['tier']=o
        elif 'own' not in e: e['own'],e['tier']='owner not stated',IND
        e.setdefault('cty',cty if kn!='Mexican & Brazilian cigar' else ('Brazil' if e.get('mk')=='Dannemann' else 'Mexico'))
        e.setdefault('g',e['own'] if e['own']!='owner not stated' else 'Owner not stated')
cnt=0
for kn,n,cty,own,tier in rows:
    Kk=kind(kn); Kk.setdefault('x',[])
    ex={norm(e['n']) for e in Kk['x']}|{norm(e.get('mk','')) for e in Kk['x']}
    if norm(n) in ex: continue
    Kk['x'].append({'n':n,'a':'','d':f'Cigar marque made in {cty}; the list names {own} as maker or owner.','mk':n,'y':'','s':LIST,'g':own,'own':own,'tier':tier,'cty':cty})
    cnt+=1
    reg(own,c='',dsc=f'Maker or owner of the cigar marque {n}.',s=LIST,seg='Artisan & independent' if tier==IND else 'Mainstream')
for kn in list(kc)+['Cigar from other countries']:
    Kk=kind(kn)
    Kk['xg']='by owner'
    Kk['nl']='One entry is a cigar marque or a distinct range sold under its own name; sizes and vitolas are versions.'
    Kk['sel']=('Marques of this country in Wikipedia\'s List of cigar brands, in the three table windows read (rows A to Z as the page returned them) with the owner or maker the list names; country is where the list says the marque is made. Marques whose country the list leaves blank are not placed. Existing range entries from the earlier pass stay. '
      'Covers '+str(len(Kk['x']))+' entries in this kind of about 150 rows in List of cigar brands; the rest have no country on the page or belong to the Cuban, machine-made or cigarillo kinds.')
LISTROWS=None

# ---------- C. pipes ----------
PD='https://pipedia.org/wiki/Billiard'
shapes=['Apple','Author','Ball','Bent Apple','Bent Billiard','Bent Bulldog','Billiard','Blowfish','Brandy','Bullcap','Bulldog','Bullmoose','Calabash','Canadian','Cavalier','Cherrywood','Churchwarden','Cutty','Diplomat','Dublin','Duke/Don','Egg','Freehand','Gourd Calabash','Hawkbill','Horn','Liverpool','Lovat','Lumberman','Oom Paul/Hungarian','Oval','Panel Billiard','Pear/Acorn','Pickaxe','Poker','Pot','Prince','Rhodesian','Skater','Straight Rhodesian','Ukulele','Vestpocket','Volcano','Zulu/Woodstock']
# 'Tools' (not a shape), 'Chimney' (no page), 'Freehand' (a craft class, kept as kind) left out
desc={'Billiard':'Classic shape with a nearly cylindrical bowl, round shank and tapered stem, tilted slightly from the shank.',
'Apple':'Billiard with a rounder bowl.','Pot':'Billiard with a shorter bowl.','Poker':'Billiard with a flat-bottomed bowl.','Liverpool':'Billiard-derived shape with a longer shank and shorter stem.',
'Bent Billiard':'Billiard made with a bent stem.','Panel Billiard':'Billiard with flat panels on the bowl or shank.','Lumberman':'Long-shank shape derived from the Billiard.','Lovat':'Long-shank shape derived from the Billiard.',
'Canadian':'Long-shank shape derived from the Billiard.','Oom Paul/Hungarian':'Full-bent Billiard, sometimes called a Hungarian or an Oom Paul.',
'Pickaxe':'Freehand form named in the Pipedia shapes index.','Calabash':'Gourd-style pipe named in the Pipedia shapes index.','Gourd Calabash':'Calabash form made with a gourd bowl, named in the Pipedia shapes index.',
'Churchwarden':'Long-stemmed pipe.'}
fam={'Billiard family':['Billiard','Bent Billiard','Panel Billiard','Pot','Apple','Poker'],'Long-shank family':['Canadian','Liverpool','Lumberman','Lovat']}
def famof(n):
    for f,l in fam.items():
        if n in l: return f
    return 'Other shapes'
alias={'vestpocket':'vestpocket'}
Kb=kind('Briar pipe'); Kf=kind('Freehand pipe'); Kc=kind('Calabash pipe')
for _k in (Kb,Kf,Kc): _k.setdefault('x',[])
allex={norm(e['n']) for k in (Kb,Kf,Kc) for e in k['x']}|{'vestpocket'}
for e in Kb['x']:
    e['g']=famof(e['n']) if e['n'] not in('Sitter','Vest pocket','Tankard') else 'Other shapes'
    e.setdefault('own','owner not applicable');
freeh={'Blowfish','Volcano','Horn','Pickaxe','Freehand'}; calab={'Calabash','Gourd Calabash'}
added=0
for s in shapes:
    n=s.split('/')[0]; a=' · '.join(s.split('/')[1:])
    if norm(n) in allex or norm(n)=='freehand': continue
    ent={'n':n,'a':a,'d':desc.get(s,'Pipe shape listed in the Pipedia shapes index.'),'mk':'','y':'','s':PD,'g':famof(s)}
    if s in freeh: Kf['x'].append(ent)
    elif s in calab: Kc['x'].append(ent)
    else: Kb['x'].append(ent); added+=1
for e in Kb['x']+Kf['x']+Kc['x']:
    e.pop('own',None)
Kf['m']=[]
for k in (Kb,Kf,Kc):
    k['nl']='One entry is a named pipe shape (bowl and stem form) used by pipe makers; sizes and finishes are attributes.'
    k['xg']='by shape family'
Kb['sel']=('Pipe shapes in the Pipedia shapes index (navigation box on the Pipedia Billiard page), with the families Pipedia\'s Billiard essay gives; Calabash and Gourd Calabash sit in Calabash pipe, and Blowfish, Horn, Pickaxe and Volcano in Freehand pipe. Chimney (no page), Tools (not a shape) and Freehand (a class of pipe) are not entries. '
 'Complete: 44 of 44 shapes in Pipedia\'s Pipe shapes index that name a shape with a page; descriptions only where the essay gives one. Sitter and Tankard come from the earlier pass.')
Kf['sel']='Freehand forms from the Pipedia shapes index plus the Danish freehand school from the earlier pass. Complete for the forms the Pipedia index names (Blowfish, Horn, Pickaxe, Volcano). Elephant\'s Foot, Fig, Olifant and Ramses had no fetched page and were removed.'
Kc['sel']='Calabash forms in the Pipedia shapes index (Calabash, Gourd Calabash). Complete: 2 of 2.'

# ---------- D. heated tobacco and vape ----------
HT=WP+'Heated_tobacco_product'; EC=WP+'Electronic_cigarette'
Kh=kind('Heated-tobacco device')
Kh['m']=[]; Kh.pop('r',None)
PMI='Philip Morris International'
def ht(n,mk,y,dsc,own,tier,cty,ver=None,role=None,a=''):
    e={'n':n,'a':a,'d':dsc,'mk':mk,'y':y,'s':HT,'g':f'Maker: {own}','own':own,'tier':tier,'cty':cty,'v':ver or []}
    if role: e['role']=role
    return e
Kh['x']=[
 ht('Premier','R. J. Reynolds','1988','Charcoal-heated cigarette system, withdrawn in 1989.','R.J. Reynolds','Global group','United States'),
 ht('Eclipse','R. J. Reynolds','mid-1990s','Carbon-ember heated-tobacco system of limited distribution.','R.J. Reynolds','Global group','United States',[{'n':'Revo','y':'','d':'repositioned Eclipse, withdrawn 2015'},{'n':'Steam Hot One','y':'','d':'Japan Tobacco variant sold in Japan'}]),
 ht('Accord','Philip Morris','1998','Philip Morris heated cigarette system sold as Oasis in Osaka; production ended 2006.',PMI,'Global group','United States'),
 ht('Heatbar',PMI,'2007','Philip Morris International system using specially designed cigarettes; discontinued.',PMI,'Global group','Switzerland'),
 ht('IQOS',PMI,'2014','Philip Morris International device heating tobacco sticks, launched in Nagoya and Milan in June 2014.',PMI,'Global group','Switzerland',
   [{'n':'IQOS 3','y':'2018','d':'launched in Tokyo, October 2018'},{'n':'IQOS Original','y':'','d':''},{'n':'IQOS ILUMA','y':'','d':''},{'n':'IQOS ILUMA ONE','y':'','d':''},{'n':'IQOS ILUMA PRIME','y':'','d':''}],role='landmark'),
 ht('glo','British American Tobacco','2016','British American Tobacco heated-tobacco device first sold in Japan.','British American Tobacco','Global group','United Kingdom',[{'n':'glo iFuse','y':'2015','d':'hybrid of heated tobacco and e-cigarette using Neopods'},{'n':'i-glo','y':'2017','d':'launched in Canada, May 2017'}]),
 ht('Ploom','Japan Tobacco','2016','Japan Tobacco heated-tobacco device launched in January 2016 with tobacco capsules.','Japan Tobacco','Global group','Japan',[{'n':'Ploom TECH+','y':'2019','d':'launched January 2019 in Tokyo'},{'n':'Ploom S','y':'2019','d':'launched January 2019 in Tokyo'},{'n':'Ploom EVO','y':'','d':''}]),
 ht('TEEPS',PMI,'2017','Philip Morris International lit-carbon system that looks like a cigarette, launched in the Dominican Republic.',PMI,'Global group','Switzerland'),
 ht('lil','Korea Tobacco & Ginseng Corp.','2017','Korean device heating cigarette sticks with a circular blade, launched 20 November 2017.','Korea Tobacco & Ginseng Corp.','National champion','South Korea'),
 ht('Mok','China Tobacco','2019','Compact heated-tobacco device launched in South Korea in May 2019.','China National Tobacco Corporation','National champion','China'),
 ht('Cigoo','Yunnan Xike Science & Technology','2020','Heated plant-particle product operating at 300 degrees Celsius, launched September 2020.','Yunnan Xike Science & Technology','Independent','China'),
 ht('TEO','Shenzhen ESON Technology','2021','Device for cigarette sticks and tobacco-free NEAFS sticks, launched December 2021.','Shenzhen ESON Technology','Independent','China'),
 ht('Pulze','Imperial Brands','2021','Imperial Brands device using iD tobacco sticks, piloted in the Czech Republic in 2021.','Imperial Brands','Global group','United Kingdom',[{'n':'Pulze 2.0','y':'2023','d':'Italy, Poland, Czech Republic, Greece'},{'n':'Pulze 3.0','y':'2025','d':'announced 18 September 2025'}]),
]
Kh['nl']='One entry is a heated-tobacco system sold under its own name; later models of the same system are versions, and the sticks are a separate kind.'
Kh['xg']='by maker'
Kh['sel']='Every heated-tobacco system for tobacco sticks named in the table of Wikipedia\'s Heated tobacco product (first 100,000 characters of the page). Dry-herb systems used mainly for cannabis (Pax, Firefly 2, iSmoke OneHitter) are under Portable vaporiser. Covers 13 of the 17 systems in the page table; the other four are dry-herb vaporisers or an unlaunched model.'
Kh['xg']='by maker'

def vp(kn,n,mk,y,dsc,own,tier,cty,ver=None,role=None):
    Kk=kind(kn)
    ex=[e for e in Kk['x'] if norm(e['n'])==norm(n)]
    if ex:
        e=ex[0]; e.update({'own':own,'tier':tier,'cty':cty,'g':f'Maker: {own}'})
        if role: e['role']=role
        return
    e={'n':n,'a':'','d':dsc,'mk':mk,'y':y,'s':EC,'g':f'Maker: {own}','own':own,'tier':tier,'cty':cty,'v':ver or []}
    if role: e['role']=role
    Kk['x'].append(e)
vp('Refillable pod kit','JUUL','Juul Labs','2015','','Juul Labs','Independent','United States',role='landmark')
vp('Refillable pod kit','Vuse','R.J. Reynolds','2014','Pod vape line from Reynolds American, now British American Tobacco; Vuse Alto held about 40 % of US e-cigarette sales in stores tracked by NielsenIQ in the 52 weeks to 15 June 2024.','British American Tobacco','Global group','United States')
vp('Refillable pod kit','NJOY','NJOY','2015','Vape brand listed among 2015 US market players; Altria acquired its e-vapor portfolio in 2023.','Altria','Global group','United States')
vp('Disposable vape','Elf Bar','Shenzhen iMiracle','2018','','Shenzhen iMiracle (EBDESIGN)','Independent','China')
vp('Cigalike','blu','Lorillard','2012','Vape brand bought by Lorillard as Blu eCigs in April 2012 and sold to Imperial Tobacco in July 2014.','Imperial Brands','Global group','United States')
vp('Cigalike','Ruyan','Hon Lik','2004','Early Chinese e-cigarette brand; Hon Lik registered the modern design patent in 2003 and the e-vapor business was sold to Imperial Brands in 2013.','Imperial Brands','Global group','China')
vp('Vape pen kit','eGo','Joyetech','2009','Joyetech vape pen series developed in 2009 with clearomizers and eGo batteries.','Joyetech','Independent','China')
for kn in ('Refillable pod kit','Disposable vape','Cigalike','Vape pen kit'):
    k=kind(kn); k['m']=[]; k.pop('r',None)
    k['nl']='One entry is a vape product line or hardware family sold under its own name; later models are versions.'
    k['xg']='by maker'
    k['sel']='Vape hardware lines named in Wikipedia\'s Electronic cigarette (first 100,000 characters), with owner and year as that page states. Covers the 7 lines the page names with an owner; SMOK, Vaporesso, OXVA, VooPoo and SKE are not on the page and their former model entries were removed.'
for kn in ('Box mod kit','Rebuildable tank atomiser (RTA)','Rebuildable dripping atomiser (RDA)'):
    k=kind(kn); k['nl']='One entry is a hobby vape hardware line named by a maker\'s review page; models are versions.'; k['xg']='by maker'
    k['sel']='No whole-space reference exists for hobby vape hardware; entries come from maker or reviewer pages read in the earlier pass.'
    for e in k['x']:
        e.setdefault('own',e.get('mk','') or 'owner not stated'); e.setdefault('tier','Craft & indie'); e.setdefault('cty','United States' if 'Goon' in e['n'] or 'Evolv' in e['n'] else '')
# ---------- E. cigarettes: owners ----------
CG={'Marlboro':('Philip Morris International','Global group','United States',None),
 'Lucky Strike':('British American Tobacco','Global group','United States',None),
 'Gauloises':('Imperial Brands','Global group','France',2008),'Gitanes':('Imperial Brands','Global group','France',2008),
 'Peace':('Japan Tobacco','National champion','Japan',None),'Seven Stars':('Japan Tobacco','National champion','Japan',None),
 'Camel':('R.J. Reynolds Tobacco Company (US); Japan Tobacco (elsewhere)','Global group','United States',None),
 'Dji Sam Soe':('Sampoerna','National champion','Indonesia',None),'Gudang Garam':('Gudang Garam','National champion','Indonesia',None),
 'Djarum':('Djarum','National champion','Indonesia',None),'Sampoerna A Mild':('Sampoerna','National champion','Indonesia',None),
 'Drum':('Imperial Brands','Global group','Netherlands',None),'Golden Virginia':('Imperial Brands','Global group','United Kingdom',None),
 'Amber Leaf':('Japan Tobacco','Global group','United Kingdom',2007)}
for kn in ('Manufactured cigarette','Roll-your-own tobacco','Kretek (clove cigarette)'):
    k=kind(kn)
    k['nl']='One entry is a cigarette or rolling-tobacco brand sold under its own name; pack sizes and variants are versions.'
    k['xg']='by owner'
    k['sel']='Brands named on the earlier pass, with owners taken from the company pages fetched in this pass (Philip Morris International, British American Tobacco, Japan Tobacco, Imperial Brands, Altria). No whole-space brand reference exists; the market panel above lists the groups. Owner not stated for brands the company pages do not list.'
    for e in k['x']:
        o=CG.get(e['n'])
        if o: e['own'],e['tier'],e['cty']=o[0],o[1],o[2];
        else: e.setdefault('own','owner not stated'); e.setdefault('tier','Independent'); e.setdefault('cty','')
        if o and o[3]: e['own_y']=str(o[3])
        e['g']=e['own'] if e['own']!='owner not stated' else 'Owner not stated'
# ---------- F. cannabis flower commodity ----------
kf=kind('Cannabis flower'); removed=[e['n'] for e in kf['x']]; kf['x']=[]
# ---------- G. market panels ----------
TT='https://tobaccotactics.org/?p=19766'
def m(mkt,who,share,yr,s,note): return {'mkt':mkt,'who':who,'share':share,'yr':yr,'s':s,'note':note}
dept('Cigarettes & rolling')['ms']=[
 m('Global cigarettes (volume)','China National Tobacco Corporation','47 %',2025,TT,'share of total global cigarette sales by volume, including China'),
 m('Global cigarettes (volume)','Big four (Philip Morris International, British American Tobacco, Japan Tobacco, Imperial Brands)','just over 34 %',2025,TT,'combined global share by volume'),
 m('Cigarettes outside China (volume)','Big four combined','66 %',2025,TT,'share by volume excluding China'),
 m('Markets led, of 90 cigarette markets studied','Philip Morris International','38 markets',2020,TT,'number of markets dominated'),
 m('Markets led, of 90 cigarette markets studied','British American Tobacco','24 markets',2020,TT,'number of markets dominated'),
 m('Markets led, of 90 cigarette markets studied','Japan Tobacco International','8 markets',2020,TT,'number of markets dominated'),
 m('Markets led, of 90 cigarette markets studied','Imperial Brands','6 markets',2020,TT,'number of markets dominated'),
 m('China cigarettes','China National Tobacco Corporation','about 96 %','year not stated',WP+'China_National_Tobacco_Corporation','share of cigarette sales in China as the page states it'),
 m('Japan cigarettes','Japan Tobacco','66 %','year not stated',WP+'Japan_Tobacco','share of the Japanese cigarette market as the page states it'),
 m('Company net revenue','Philip Morris International','US$40.648 billion',2025,WP+'Philip_Morris_International','net revenue excluding excise taxes; more than 600 billion cigarettes and 155 billion heated tobacco units shipped'),
 m('Company revenue','British American Tobacco','GBP 25.610 billion',2025,WP+'British_American_Tobacco','revenue; second-largest tobacco company by net sales per the page'),
 m('Company revenue','Imperial Brands','GBP 32.171 billion',2025,WP+'Imperial_Brands','revenue as the page gives it; fourth-largest international cigarette company by market share'),
 m('Company revenue','Altria','US$23.28 billion',2025,WP+'Altria','revenue; parent of Philip Morris USA, John Middleton and the US Smokeless Tobacco Company'),
 m('Company revenue','Japan Tobacco','JPY 2.033 trillion',2012,WP+'Japan_Tobacco','latest revenue figure the page gives'),
]
dept('Vaping & heated tobacco')['ms']=[
 m('US e-cigarettes (Nielsen-monitored)','Juul Labs','over 72 %',2018,EC,'as of August 2018'),
 m('US e-cigarettes (Nielsen-monitored)','Vuse (British American Tobacco)','under 10 %',2018,EC,'closest competitor to Juul in August 2018'),
 m('US e-cigarettes in tracked stores','Vuse Alto (British American Tobacco)','about 40 %',2024,EC,'52 weeks ended 15 June 2024, NielsenIQ via an analyst cited by the Wall Street Journal'),
 m('Heated tobacco','Philip Morris International','155 billion heated tobacco units shipped',2025,WP+'Philip_Morris_International','shipment volume of IQOS sticks, as the page states'),
]
dept('Cigars')['ms']=[
 m('Premium handmade cigars (Cuba)','Habanos S.A.','27 marques',2024,HAB,'portfolio size; six global marques, five high value, three volume and thirteen others'),
 m('Premium handmade cigars (Cuba)','Cubatabaco and Altadis','50 % each',1994,WP+'Habanos_S.A.','equal ownership of Habanos S.A. when formed; Imperial Tobacco sold the Altadis premium-cigar stake in 2020 for a total of EUR 1,225 million'),
]
# ---------- H. brand register ----------
for n,c,f,dsc,s,lines in [
 ('Philip Morris International','Switzerland','','Cigarette group; brands named on its Wikipedia page: Marlboro, L&M, Chesterfield, Parliament, Philip Morris, IQOS, Zyn, Veev.',WP+'Philip_Morris_International',['Marlboro','L&M','Chesterfield','Parliament','Philip Morris','IQOS','Zyn','Veev']),
 ('British American Tobacco','United Kingdom','','Cigarette group; brands named on its Wikipedia page: Dunhill, Lucky Strike, Pall Mall, Kent, Rothmans, Vuse, glo, Velo.',WP+'British_American_Tobacco',['Dunhill','Lucky Strike','Pall Mall','Kent','Rothmans','Vuse','glo','Velo']),
 ('Japan Tobacco','Japan','','Cigarette group; brands named on its Wikipedia page: Winston, Camel (outside the US), Mevius, Ploom, LD.',WP+'Japan_Tobacco',['Winston','Camel','Mevius','Ploom','LD']),
 ('Imperial Brands','United Kingdom','','Cigarette group; brands named on its Wikipedia page include Davidoff, West, Gauloises, Gitanes, JPS, Kool, Golden Virginia, Drum, Rizla, blu, Pulze, Skruf.',WP+'Imperial_Brands',['Davidoff','West','Gauloises','Gitanes','JPS','Kool','Golden Virginia','Drum','Rizla','blu','Pulze','Zone X','Skruf']),
 ('Altria','United States','','US tobacco group; brands named on its Wikipedia page: Marlboro (Philip Morris USA), Black & Mild, Copenhagen, Skoal, On!, NJOY.',WP+'Altria',['Marlboro','Black & Mild','Copenhagen','Skoal','On!','NJOY']),
 ('China National Tobacco Corporation','China','1981','State tobacco monopoly; about 96 % of cigarette sales in China per its Wikipedia page.',WP+'China_National_Tobacco_Corporation',None),
 ('Korea Tobacco & Ginseng Corp.','South Korea','','Maker of the lil heated-tobacco device launched in November 2017.',HT,None),
 ('Cubatabaco','Cuba','','Cuban state tobacco company; half owner of Habanos S.A.',WP+'Habanos_S.A.',None),
 ('General Cigar Company','','','Cigar maker named as owner or maker of several marques in the List of cigar brands.',LIST,None),
 ('Oettinger Davidoff Group','','','Owner of Camacho and Davidoff group cigar marques per the List of cigar brands.',LIST,None),
 ('Altadis','Spain','','Tobacco company bought by Imperial Tobacco in February 2008; owned half of Habanos S.A. until 2020.',WP+'Habanos_S.A.',None),
 ('Tabacalera Incorporada','Philippines','','Owner of the Alhambra, Don Juan Urquijo and Tabacalera cigar marques in the List of cigar brands.',LIST,None),
 ('J.C. Newman','','','Owner of Diamond Crown, Cuesta-Rey and Maximus cigar marques per the List of cigar brands.',LIST,None),
 ('Matasa','Dominican Republic','','Maker named for the Quesada marque in the List of cigar brands.',LIST,None),
 ('Maya Selva','Honduras','','Maker of Flor de Selva and Villa Zamorano cigars per the List of cigar brands.',LIST,None),
]:
    reg(n,c,f,'Mainstream',kf='tobacco group' if lines else '',dsc=dsc,s=s,lines=lines)
for jn in ('Juul Labs','Elf Bar'):pass
for n in ('Vuse','blu','NJOY','Ruyan','Joyetech','Shenzhen iMiracle (EBDESIGN)','Hon Lik','Iranian Tobacco Company'):
    reg(n,'','', 'Mainstream' if n in('Vuse','blu','NJOY') else 'Independent', kf='vape',dsc=f'{n}: vape maker or brand named on the Electronic cigarette page.' if n!='Iranian Tobacco Company' else 'Owner of the Farvardin cigar marque per the List of cigar brands.', s=EC if n!='Iranian Tobacco Company' else LIST)
# lines for existing group entries
for b in br['b']:
    for n,c,f,dsc,s,lines in []: pass
LINES={'Philip Morris International':['Marlboro','L&M','Chesterfield','Parliament','Philip Morris','IQOS','Zyn','Veev'],'British American Tobacco':['Dunhill','Lucky Strike','Pall Mall','Kent','Rothmans','Vuse','glo','Velo'],'Japan Tobacco':['Winston','Camel','Mevius','Ploom','LD'],'Imperial Brands':['Davidoff','West','Gauloises','Gitanes','JPS','Kool','Golden Virginia','Drum','Rizla','blu','Pulze','Zone X','Skruf']}
for b in br['b']:
    if b['n'] in LINES and not b.get('lines'): b['lines']=LINES[b['n']]
br['b'].extend(newbrands.values())

# ---------- write ----------
def w(p,o):
    t=p+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
w(B+'out/J10.json',d); w(B+'out/J10_brands.json',br)
print('rows added',cnt,'briar added',added,'brands added',len(newbrands),'removed flower',removed)
