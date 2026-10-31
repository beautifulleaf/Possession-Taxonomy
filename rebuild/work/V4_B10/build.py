import json,os,re,copy
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/B10.json'))
brands=json.load(open(R+'out/B10_brands.json'))
SW='https://en.wikipedia.org/wiki/Saddle'; BW='https://en.wikipedia.org/wiki/Bit_(horse)'; HW='https://en.wikipedia.org/wiki/Beehive'
MARS='https://en.wikipedia.org/wiki/List_of_Mars_Inc._brands'; PUR='https://en.wikipedia.org/wiki/Nestl%C3%A9_Purina_PetCare'
SMU='https://en.wikipedia.org/wiki/J.M._Smucker'; HIL='https://en.wikipedia.org/wiki/Hill%27s_Pet_Nutrition'
BB='https://www.clearygottlieb.com/news-and-insights/news-listing/general-mills-completes-8-billion-acquisition-of-blue-buffalo-pet-products'
PFI='https://www.petfoodindustry.com/top-pet-food-companies/article/15751940/chart-top-20-pet-food-companies-2024-purina-mars-still-dominate'
PW='https://en.wikipedia.org/wiki/Pet_food'
kinds={}
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']: kinds[k['n']]=(dp,sh,k)
# --- 1 prune x (icon rule): keep canon kinds and origin entries
KEEP_KINDS={'Western saddle','Australian stock saddle','Side saddle','Treeless saddle','Stirrup','Snaffle bit','Curb bit','Bitless bridle','Reins','Falconry hood','Jesses and anklets','Falconry bells','Falconry glove','Falconry perch','Framed vertical hive','Long hive','Top-bar hive','Warré hive'}
KEEP_ORIGIN={('Dog head halter','Halti Headcollar'),('Dog lead','flexi retractable lead'),('Dog toy','Nylabone nylon chew bone'),('Cat toy','Cat Dancer'),('Aquarium filter','Eheim classic canister'),('Aquarium heater','Jäger regulator heater'),('Fish food','TetraMin'),('Formicarium','Janet nest'),('Side reins and lunging aids','Pessoa lungeing system')}
dropped=[];kept=[]
for n,(dp,sh,k) in kinds.items():
    nx=[]
    for x in k.get('x',[]) or []:
        if n in KEEP_KINDS and not (n=='Western saddle' and x['n']=='McClellan saddle') and not (n=='Treeless saddle'):
            nx.append(x)
        elif (n,x['n']) in KEEP_ORIGIN:
            x['role']='origin'; nx.append(x)
        else: dropped.append((n,x['n']))
    if nx: k['x']=nx
    else: k.pop('x',None)
# treeless: drop Ansur (not origin)
for n in list(kinds):
    pass
# --- 2 remove m and r
nm=0;nr=0
for n,(dp,sh,k) in kinds.items():
    nm+=len(k.pop('m',[]) or []); nr+=len(k.pop('r',[]) or [])
# generic nl/sel for commodity kinds holding only origin entries
for n,(dp,sh,k) in kinds.items():
    if k.get('x') and n not in KEEP_KINDS:
        k['nl']='One entry is the first product of its kind, as a fetched page states.'
        k['sel']='Commodity kind: no list of named products. Only the origin entry is kept (BRIEF.md icon rule); no design-collection or major-award landmark was confirmed on a fetched page.'
# --- 3 saddles
def E(n,dd,s,g,mk='',y='',a='',v=None,role=None):
    e={'n':n,'a':a,'d':dd,'mk':mk,'y':y,'s':s,'g':g}
    if v: e['v']=v
    if role: e['role']=role
    return e
eng=kinds['English saddle'][2]
eng['x']=[
 E('Dressage saddle','English-style saddle with a long straight flap and deep seat for classical dressage.',SW,'English',y='18th century (Guérinière)'),
 E('Jumping saddle','English-style saddle with forward-angled flaps for the forward seat; Captain Federico Caprilli changed its design in the early 20th century.',SW,'English',y='early 20th century (Caprilli)'),
 E('Hunt seat saddle','English-style saddle named in the article for hunt seat riding.',SW,'English'),
 E('Eventing saddle','English-style saddle named in the article for eventing.',SW,'English'),
 E('Show jumping saddle','English-style saddle named in the article for show jumping.',SW,'English'),
 E('Saddle seat saddle','English-style saddle named in the article for saddle seat riding.',SW,'English'),
 E('Racing saddle','English-style saddle named in the article for racing.',SW,'English'),
 E('Polo saddle','English-style saddle named in the article for polo.',SW,'English'),
 E('Endurance saddle','Lightweight saddle with broad panels for long rides.',SW,'English'),
 E('Police saddle','English-style saddle with a tree that spreads the rider\'s weight.',SW,'English'),
 E('Flexible saddle','Saddle with a traditional tree and movable, adjustable panels.',SW,'English')]
eng['nl']='One entry is a named saddle type that Wikipedia lists under English-style riding; fit and make are versions or attributes.'
eng['sel']="Follows the English-style types named in Wikipedia's Saddle article. Complete: 11 of 11 English-style types named there (surfing saddle left out as not a riding saddle for horses)."
eng['xg']='by discipline'
we=kinds['Western saddle'][2]
we['x']=[x for x in we['x'] if x['n']=='Wade saddle']+[E('Trick riding saddle','Western-style saddle with a tall metal horn and reinforced handholds for stunt riding.',SW,'Western')]
for x in we['x']: x['g']='Western'
we['nl']='One entry is a named Western saddle type; makers and sizes are versions or attributes.'
we['sel']="Follows the Western types named in Wikipedia's Saddle article (Western, trick riding) with the Wade saddle from an earlier sourced page."
we['xg']='by use'
a=kinds['Australian stock saddle'][2]
for x in a['x']: x['g']='Australian'
a['nl']='One entry is a named Australian stock saddle pattern; makers are versions.'
a['sel']="Patterns from earlier sourced pages; the Saddle article names the Australian stock saddle only as a type."
a['xg']='by pattern'
# military kind
shelf=kinds['Western saddle'][1]
mil={'n':'Military saddle','a':'cavalry saddle','d':'Saddle made for mounted troops to carry weapons and equipment.','s':SW,
 'nl':'One entry is a named military saddle pattern; issue marks are versions.',
 'sel':"Follows the military saddles named in Wikipedia's Saddle article. Complete: 3 of 3 military patterns named there.",'xg':'by period',
 'x':[E('Four-horn Roman saddle','Early solid-treed saddle design with four horns.',SW,'Ancient',y='1st century BC',role='origin'),
  E('McClellan saddle','American cavalry saddle with an English-type tree, higher pommel and cantle and a split seat; used until the 1940s.',SW,'19th century',mk='George B. McClellan',y='1850s'),
  E('Universal Pattern saddle','British cavalry saddle issued in successive marks.',SW,'19th century',y='1891',v=[{'n':'Steel Arch Mark I','mk':'','y':'1891','d':''},{'n':'Mark II','mk':'','y':'1893','d':''},{'n':'Mark III','mk':'','y':'1898','d':''},{'n':'Fixed tree','mk':'','y':'1902','d':''},{'n':'Adjustable tree','mk':'','y':'1912','d':''}])]}
shelf['k'].insert(shelf['k'].index(we)+1,mil)
kinds['Military saddle']=(kinds['Western saddle'][0],shelf,mil)
sd=kinds['Side saddle'][2]
sd['nl']='One entry is a named side-saddle pattern.';sd['sel']="Patterns from earlier sourced pages; Wikipedia's Saddle article names the sidesaddle only as a type."
sd['xg']='by period'
for x in sd['x']: x['g']='Side saddle'
# saddle coverage on parent shelf note
for n in('Pack saddle','Treeless saddle'):
    kinds[n][2]['t']=kinds[n][2].get('t') or []
# --- 4 bits
sn=kinds['Snaffle bit'][2]
sn['x']=[E('Bradoon','Snaffle bit worn with a curb bit in a double bridle.',BW,'Snaffle')]+sn['x']
for x in sn['x']: x['g']='Snaffle'
sn['nl']='One entry is a named snaffle-type bit; mouthpieces and sizes are versions.'
sn['sel']="Follows the bits named in Wikipedia's Bit (horse) article, with the Fulmer and Baucher from earlier sourced pages."; sn['xg']='by action'
cu=kinds['Curb bit'][2]
for x in cu['x']: x['g']='Curb'
cu['nl']='One entry is a named curb or combination bit; mouthpieces and sizes are versions.'
cu['sel']="Complete: 11 of 11 named bit types in Wikipedia's Bit (horse) article (snaffle, bradoon, curb, spade, Pelham, Kimblewick, Weymouth/double bridle, gag, Chifney, Tattersall ring, Liverpool); the Weymouth entry is the curb of the double bridle."
cu['xg']='by action'
gag=kinds['Gag bit'][2]
gag['d']=gag['d']
inh={'n':'In-hand bit','a':'leading bit','d':'Bit used only for leading a horse, not for riding.','s':BW,
 'nl':'One entry is a named bit used for leading only.','sel':"Complete: 2 of 2 named in-hand bits in Wikipedia's Bit (horse) article.",'xg':'by use',
 'x':[E('Chifney anti-rearing bit','Semicircular bit with three rings, used to limit rearing when leading a horse.',BW,'In-hand'),
      E('Tattersall ring bit','In-hand bit listed in the article without further description.',BW,'In-hand')]}
sh=kinds['Gag bit'][1]; sh['k'].insert(sh['k'].index(gag)+1,inh); kinds['In-hand bit']=(kinds['Gag bit'][0],sh,inh)
for n in ('Bitless bridle','Reins'):
    k=kinds[n][2]
    k['nl']='One entry is a named bitless bridle or rein pattern.' if n=='Bitless bridle' else 'One entry is a named rein pattern.'
    k['sel']='Patterns from earlier sourced pages (Wikipedia and maker pages); no whole-space reference list exists for this kind.'
    k['xg']='by tradition'
    for x in k['x']: x['g']=x.get('g') or 'Pattern'
st=kinds['Stirrup'][2]
st['nl']='One entry is a named English stirrup iron pattern.';st['sel']='Patterns from earlier sourced pages; no whole-space reference list exists.';st['xg']='by pattern'
for x in st['x']: x['g']='English'
# --- 5 falconry
for n in('Falconry hood','Jesses and anklets','Falconry bells','Falconry glove','Falconry perch'):
    k=kinds[n][2]
    k['nl']=f'One entry is a named pattern of {n.lower()} by region or maker.'
    k['sel']='Patterns named on earlier fetched falconry pages; no single whole-space reference exists. Not a complete list.'
    k['xg']='by pattern'
    for x in k['x']: x['g']=x.get('g') or 'Pattern'
# --- 6 hives
HM={'Langstroth hive':('Lorenzo Langstroth','1852'),'WBC hive':('William Broughton Carr','1890'),'Layens hive':('Georges de Layens','1864'),'Dadant hive':('Charles Dadant','1920'),'People\'s Hive':('Émile Warré','')}
for n in('Framed vertical hive','Long hive','Top-bar hive','Warré hive'):
    k=kinds[n][2]
    for x in k['x']:
        if x['n'] in HM:
            x['mk'],yy=HM[x['n']]
            if yy: x['y']=yy
            if x['n']=='Dadant hive': x['d']='Large-frame hive derived from the Dadant-Blatt hive; widespread in France, Italy and the Americas.'
        if x['n']=="People's Hive": x['n']='Warré hive'; x['a']="People's Hive"
        x['role']=x.get('role')
        if x['n'] in ('Langstroth hive',): x['role']='landmark'
        x['g']={'Framed vertical hive':'Framed vertical','Long hive':'Long','Top-bar hive':'Top-bar','Warré hive':'Vertical top-bar'}[n]
        if x.get('role') is None: x.pop('role')
    k['nl']='One entry is a named hive design with its inventor and year; box sizes and frame sizes are versions.'
    k['sel']="Hive designs named in the brief and in Wikipedia's Beehive article (Langstroth, Dadant, National, Warré, top-bar, Flow Hive, Layens) plus WBC, Smith, Commercial and Rose from earlier sourced pages. Covers 15 of about 15 designs named in the brief and those pages; Wikipedia gives inventor and year only for Langstroth, Dadant, Layens and WBC."
    k['xg']='by hive family'
# --- 7 pet food brands
GR={'M':('Mars Petcare','Global group'),'P':('Nestlé Purina PetCare','Global group'),'C':('Colgate-Palmolive','Global group'),'G':('General Mills','Global group'),'S':('The J.M. Smucker Company','Global group')}
SRC={'M':MARS,'P':PUR,'S':SMU,'C':HIL,'G':BB}
def B(g,n,dd,y='',cty='',own_y='',a='',own=None,tier=None,s=None):
    o,t=GR.get(g,(None,None))
    e=E(n,dd,s or SRC[g],{'M':'Mars Petcare','P':'Nestlé Purina PetCare','C':'Hill\'s / Colgate-Palmolive','G':'General Mills','S':'J.M. Smucker'}[g] if g in GR else 'Independent',mk=n,y=y,a=a)
    e['own']=own or o; e['tier']=tier or t
    if cty:e['cty']=cty
    if own_y:e['own_y']=own_y
    return e
dogfood=[B('M','Pedigree','Dog food brand on the Mars Petcare list.',y='1934',cty='United Kingdom',s=MARS),
 B('M','Royal Canin','Dog and cat food brand on the Mars Petcare list.'),
 B('M','Iams','Dog and cat food brand on the Mars Petcare list; not sold under Mars in Europe.',y='1946'),
 B('M','Eukanuba','Dog food brand on the Mars Petcare list; not sold under Mars in Europe.',y='1969'),
 B('M','Nutro','Dog and cat food brand on the Mars Petcare list.'),
 B('M','Chappi','Dog food brand on the Mars Petcare list.'),
 B('M','Cesar','Small-dog wet food brand on the Mars Petcare list.',a='Cesar Canine Cuisine'),
 B('M','Orijen','Pet food brand on the Mars Petcare list.'),
 B('M','Acana','Pet food brand on the Mars Petcare list.'),
 B('P','Pro Plan','Performance dog and cat food brand of Purina.',a='Purina Pro Plan'),
 B('P','Dog Chow','Dog food brand of Purina.'),
 B('P','Beneful','Dog food brand of Purina.'),
 B('P','Alpo','Dog food brand of Purina.'),
 B('P','Purina ONE','Dog and cat food brand of Purina.'),
 B('P',"Lily's Kitchen",'British natural pet food brand bought by Purina in April 2020.',cty='United Kingdom',own_y='2020'),
 B('C',"Hill's Science Diet",'Everyday dog and cat food of Hill\'s Pet Nutrition, founded in 1907 in the United States.',y='1960',cty='United States',s=HIL),
 B('G','Blue Buffalo','Natural dog and cat food and treats brand, founded in 2002; General Mills bought it on 24 April 2018 for about $8 billion.',y='2002',own_y='2018',a='BLUE'),
 B('I','Nulo','Pet food maker whose US sales rose 2.1 % to $261.8 million in the 52 weeks to 18 January 2025.',own='Nulo Inc.',tier='Independent',s=PFI)]
dogtreat=[B('M','Greenies','Dental dog and cat treat brand on the Mars Petcare list.'),B('M','Schmackos','Dog treat brand on the Mars Petcare list.'),B('M','Pill Pockets','Treat brand for hiding pills, on the Mars Petcare list.'),
 B('P',"Beggin'",'Dog treat brand of Purina.'),B('P',"Waggin' Train",'Dog treat brand of Purina; acquisition completed 2010.',own_y='2010'),B('P','Canyon Creek','Dog treat brand of Purina.'),B('P',"Zuke's",'Cat and dog treat brand, bought by Purina in 2014.',own_y='2014'),
 B('S','Milk-Bone','Dog biscuit brand, bought by Smucker in 2015 with Big Heart Pet Brands.',own_y='2015'),B('S','Pup-Peroni','Dog snack brand, bought by Smucker in 2015 with Big Heart Pet Brands.',own_y='2015'),B('S','Snausages','Dog treat brand listed as a current Smucker pet brand.')]
cdry=[B('M','Whiskas','Cat food brand on the Mars Petcare list.',y='1936'),B('M','Kit-e-Kat','Cat food brand on the Mars Petcare list.'),B('M','Exelcat','Cat food brand on the Mars Petcare list.'),
 B('P','Friskies','Cat food brand from the Friskies PetCare Company, merged into Purina in 2001.'),B('P','Cat Chow','Cat food brand of Purina.'),B('P',"Kit 'n Kaboodle",'Cat food brand of Purina.'),
 B('S','Meow Mix','Cat food brand, bought by Smucker in 2015 with Big Heart Pet Brands.',y='1974',own_y='2015')]
cwet=[B('M','Sheba','Wet cat food brand on the Mars Petcare list.',y='1982'),B('P','Fancy Feast','Wet cat food brand of Purina.'),B('P','Felix','Cat food brand of Purina.'),B('P','Muse','Wet cat food brand of Purina.')]
ctreat=[B('M','Temptations','Cat treat brand on the Mars Petcare list.'),B('M','Dreamies','Cat treat brand on the Mars Petcare list.'),B('M','Catisfactions','Cat treat brand on the Mars Petcare list.')]
cfresh=[B('I','Freshpet','Publicly traded fresh pet food company named by Petfood Industry; first full-year positive net income in fiscal 2024.',own='Freshpet, Inc.',tier='Independent',s=PFI)]
cvet=[B('C',"Hill's Prescription Diet",'Veterinary diet range of Hill\'s Pet Nutrition.',cty='United States',s=HIL),B('M','Royal Canin Veterinary Diet','Veterinary diet range of Royal Canin.',own='Mars Petcare',tier='Global group',s=MARS),B('P','Pro Plan Veterinary Diets','Veterinary diet range of Purina Pro Plan.',s=PUR)]
litter=[B('P','Tidy Cats','Cat litter brand of Purina.')]
for e in cvet: e['g']={'Hill\'s Prescription Diet':'Hill\'s / Colgate-Palmolive','Royal Canin Veterinary Diet':'Mars Petcare','Pro Plan Veterinary Diets':'Nestlé Purina PetCare'}[e['n']]
allb=dogfood+dogtreat+cdry+cwet+ctreat+cfresh+cvet+litter
ncov=len(allb)
NL='One entry is a pet-food brand sold under its own name; product lines, formulas and flavours are versions or attributes.'
def SEL(extra=''):
    return ("Brands of the five groups that Wikipedia's Pet food article calls dominant in 2020 (Mars, Nestlé Purina PetCare, J.M. Smucker, Hill's/Colgate-Palmolive, Blue Buffalo/General Mills), taken from each group's brand page, with independents named by Petfood Industry. "+extra+f"Covers {ncov} brands across the pet-food kinds of about 65 pet-food, treat and litter brands on the Mars, Purina and Smucker pages; aquarium, equine and regional brands on those pages, and brands whose kind could not be fetched, are left out.")
for name,lst in {'Dog food':dogfood,'Dog treats':dogtreat,'Dry cat food':cdry,'Wet cat food':cwet,'Cat treats':ctreat,'Fresh, frozen and raw cat food':cfresh,'Veterinary cat food':cvet,'Cat litter':litter}.items():
    k=kinds[name][2]; k['x']=(k.get('x') or [])+lst; k['nl']=NL; k['sel']=SEL(); k['xg']='by owner group'
# --- 8 market panel
ms=[
 {"mkt":"Global pet food, treats and other pet products, retail sales","who":"All companies","share":"US$200 billion, +1.6 %","yr":2024,"s":PFI,"note":"Euromonitor figure as the page states it"},
 {"mkt":"Global pet food, by annual revenue","who":"Nestlé Purina PetCare and Mars Petcare","share":"largest annual revenues","yr":2024,"s":PFI,"note":"the page's top-20 ranking is a chart image; no figures were read from it"},
 {"mkt":"Pet food, world market","who":"Mars; Nestlé Purina PetCare; J.M. Smucker; Hill's (Colgate-Palmolive); Blue Buffalo (General Mills)","share":"dominated by these five","yr":2020,"s":PW,"note":"Wikipedia gives no individual shares"},
 {"mkt":"United States pet owner spending","who":"All pet owners","share":"US$152 billion","yr":2024,"s":PFI,"note":"American Pet Products Association figure as the page states it"},
 {"mkt":"Hill's Pet Nutrition within Colgate-Palmolive","who":"Hill's Pet Nutrition","share":"23.1 % of net sales","yr":2024,"s":PFI,"note":"fourth quarter; net sales up 2.3 %"},
 {"mkt":"General Mills pet segment","who":"General Mills (Blue Buffalo)","share":"net sales down 4 %","yr":2024,"s":PFI,"note":"fiscal year 2024 against 2023"},
 {"mkt":"Blue Buffalo purchase","who":"General Mills","share":"about US$8 billion enterprise value","yr":2018,"s":BB,"note":"completed 24 April 2018"},
 {"mkt":"United States independent: Nulo","who":"Nulo Inc.","share":"US$261.8 million sales","yr":2025,"s":PFI,"note":"52 weeks to 18 January 2025, up 2.1 %"}]
msum="Two groups, Nestlé Purina PetCare and Mars Petcare, lead the world pet food industry by revenue. Hill's, Blue Buffalo and Smucker's brands complete the five dominant groups. Independents such as Nulo and Freshpet are growing."
for dn in('Dogs','Cats'):
    for dp in d['depts']:
        if dp['n']==dn: dp['ms']=ms; dp['msum']=msum
# --- brand register
have={x['n'] for x in brands['b']}
def RB(n,c='',f='',kf='pet food',dd='',s=''):
    if n in have: return
    have.add(n); e={'n':n,'seg':'Mainstream','kf':kf,'d':dd,'s':s}
    if c:e['c']=c
    if f:e['f']=f
    brands['b'].append(e)
for e in allb:
    RB(e['mk'],e.get('cty',''),e.get('y','') if e['n'] in("Hill's Science Diet",'Blue Buffalo','Pedigree') else '',dd=e['d'],s=e['s'])
for n,dd,s in[('Mars Petcare','Pet-care division of Mars, Incorporated; owner of Pedigree, Whiskas, Royal Canin and others.',MARS),('Nestlé Purina PetCare','Pet food division formed in December 2001 from Nestlé and Ralston Purina.',PUR),("Hill's Pet Nutrition",'Pet food maker founded in 1907, now owned by Colgate-Palmolive.',HIL),('Colgate-Palmolive','Owner of Hill\'s Pet Nutrition.',HIL),('General Mills','Owner of Blue Buffalo since 2018.',BB),('The J.M. Smucker Company','Owner of Milk-Bone, Meow Mix and Pup-Peroni.',SMU),('Freshpet, Inc.','Fresh pet food maker.',PFI),('Nulo Inc.','Pet food maker.',PFI)]:
    RB(n,dd=dd,s=s,kf='pet food owner')
for b in brands['b']:
    if b['n']=='Blue Buffalo': b['f']='2002'
    if b['n']=="Hill's Pet Nutrition": b['c']='United States';b['f']='1907'
# other kinds retained: ensure brand register has mk for kept entries (already existing mostly)
json.dump(d,open(R+'work/V4_B10/B10.new.json','w'),ensure_ascii=False,indent=1)
json.dump(brands,open(R+'work/V4_B10/B10_brands.new.json','w'),ensure_ascii=False,indent=1)
json.dump({'dropped':dropped,'nm':nm,'nr':nr,'ncov':ncov},open(R+'work/V4_B10/stats.json','w'),ensure_ascii=False)
print(len(dropped),nm,nr,ncov)
