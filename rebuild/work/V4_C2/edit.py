import json,os,copy
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/C2.json'))
W='https://en.wikipedia.org/wiki/'
def find(kn):
    for dep in d['depts']:
        for s in dep['s']:
            for k in s['k']:
                if k['n']==kn: return k
def dept(n): return [x for x in d['depts'] if x['n']==n][0]
removed_m=0; removed_x=[]
KEEP={'Original LÖWE anvil secateur','Grelinette'}
TREATED={'Lawn care','Outdoor cooking'}
for dep in d['depts']:
    for s in dep['s']:
        for k in s['k']:
            removed_m+=len(k.pop('m',[]) or [])
            if dep['n'] not in TREATED:
                keep=[x for x in k.get('x',[]) if x['n'] in KEEP]
                removed_x+= [x['n'] for x in k.get('x',[]) if x['n'] not in KEEP]
                if keep:
                    keep[0]['role']='origin'; k['x']=keep
                    k['nl']='One entry is the first product of its kind, as a fetched page states; the kind is otherwise a commodity with no named entries.'
                    k['sel']='No whole-space reference exists; one origin entry only, following the icon rule in BRIEF.md. Complete: 1 of 1 origin stated on the fetched page.'
                else: k.pop('x',None)
# ---------- helpers
def ent(n,d_,mk,y,s,own=None,tier=None,cty=None,own_y=None,role=None,g=None,a='',v=None):
    e={'n':n,'a':a,'d':d_,'mk':mk,'y':y,'s':s}
    if v: e['v']=v
    for k_,val in (('own',own),('tier',tier),('cty',cty),('own_y',own_y),('role',role),('g',g)):
        if val: e[k_]=val
    return e
def setx(k,xs,nl,sel,xg=None):
    k['x']=xs; k['nl']=nl; k['sel']=sel
    if xg: k['xg']=xg
def upd(k,name,**kw):
    for x in k['x']:
        if x['n']==name:
            for a,b in kw.items(): x[a]=b
            return x
    raise KeyError(name)
LM=W+'Lawn_mower'; HG=W+'Husqvarna_Group'
# ---------- Lawn care
k=find('Rotary mower')
upd(k,'Honda HRX',own='Honda Motor Co.',tier='Global group',cty='Japan')
upd(k,'Hayter Harrier',own='The Toro Company',tier='National champion',cty='United Kingdom',own_y='2005')
upd(k,'Victa rotary mower',cty='Australia',tier='National champion',role='landmark')
k['nl']='One entry is a pedestrian rotary mower line sold under its own name; deck sizes, drive types and engines are versions.'
k['sel']='Lines named on fetched pages for Victa (Wikipedia, Lawn mower), Honda (Honda press release) and Hayter (Wikipedia); no whole-space list of rotary mower lines exists. Covers 3 lines named on those pages; other makers appear as brands under Powered garden equipment brand.'
k=find('Cylinder mower')
upd(k,"Budding's mower",role='origin',cty='United Kingdom')
upd(k,'Ransomes Automaton',cty='United Kingdom')
k['nl']='One entry is a historic or modern cylinder (reel) mower line sold under its own name.'
k['sel']='Wikipedia Lawn mower lists Budding (1830), Ransomes, Thomas Green and Atco as the early makers. Complete: 4 of 4 cylinder mower lines named there; modern Allett ranges are held in the brand register.'
k=find('Hover mower')
upd(k,'Flymo hover mower',own='Husqvarna Group',tier='Global group',cty='United Kingdom',role='origin')
k['nl']='One entry is a hover mower line sold under its own name.'
k['sel']='Wikipedia Lawn mower credits Flymo with introducing the hover mower in 1964. Complete: 1 of 1 hover line named there.'
k=find('Riding mower')
upd(k,'Ideal Triplex',role='origin',cty='United States')
k['nl']='One entry is a riding mower line sold under its own name.'
k['sel']='Wikipedia Lawn mower credits the Ideal Power Mower Co. Triplex (1922) as the first self-propelled riding mower. Covers 1 of the lines named on that page; John Deere and Toro ride-on ranges appear as brands.'
k=find('Robotic mower')
upd(k,'Husqvarna Automower',own='Husqvarna Group',tier='Global group',cty='Sweden')
upd(k,'Bosch Indego',own='Robert Bosch GmbH',tier='Global group',cty='Germany')
upd(k,'Worx Landroid',own='Positec',tier='Independent')
upd(k,'Segway Navimow',tier='National champion',role='landmark',d='Wire-free robotic mower line; Euromonitor ranked Segway Navimow first worldwide for wire-free robotic mower unit sales in 2024.')
k['x'][4]['cty']='China'
k['x'].insert(0,k['x'].pop(0))
for nm,dd,mk,y,s,kw in [
 ('Robomow','Robotic mower line (RS, RL and RM series) from a maker that Report Prime ranks tenth among lawn mower companies; the RM400 is linked to Friendly Robotics.','Robomow','',W+'Robotic_lawn_mower',dict(a='Friendly Robotics',tier='Independent',v=[{'n':'Robomow RS630','mk':'Robomow','y':'','d':'RS series'},{'n':'Robomow RL1000','mk':'Robomow','y':'','d':'RL series'},{'n':'Robomow RM400','mk':'Robomow','y':'','d':'RM series'}])),
 ('Volta robotic mower','Mower that navigates by camera without a boundary wire; Wikipedia calls it the first commercially available robotic mower to use visual perception.','Volta','2019',W+'Robotic_lawn_mower',dict(role='origin')),
 ('Gardena robotic mower','Robotic mowers sold under the Gardena name and built by Husqvarna.','Gardena','',W+'Robotic_lawn_mower',dict(own='Husqvarna Group',tier='Global group',cty='Germany',own_y='2007')),
]:
    k['x'].append(ent(nm,dd,mk,y,s,**kw))
upd(k,'MowBot',role='origin',d='Early robotic mower patented by S. Lawrence Bellinger in 1969.',cty='United States')
for x in k['x']:
    if x['n']=='Husqvarna Automower':
        x['v'].append({'n':'Automower CEORA','mk':'Husqvarna','y':'2022','d':'satellite-guided mower for lawns up to 75,000 square metres, no boundary wire'})
        x['s']=x['s']
k['nl']='One entry is a robotic mower line sold under its own name; models in the line are versions.'
k['sel']='Wikipedia Robotic lawn mower (named lines and makers), Husqvarna Group (CEORA, Gardena) and the Barrus/Euromonitor 2024 ranking page. Covers the 9 lines these pages name; Mammotion LUBA is kept from an earlier fetched maker page.'
k['x'].sort(key=lambda x:(x.get('y') or '9999',x['n']))
# brands kind
brand_defs=[
 # name, owner group, group tier, country, own_y, desc, src, role
 ('Husqvarna','Husqvarna Group','Global group','Sweden',None,'Husqvarna Group lead brand for chainsaws, mowers and robotic mowers.',HG,None),
 ('Gardena','Husqvarna Group','Global group','Germany','2007','German garden tool and watering brand bought by Husqvarna in 2007.',HG,None),
 ('McCulloch','Husqvarna Group','Global group','United States',None,'Chainsaw and garden tool brand listed among Husqvarna Group brands.',HG,None),
 ('Flymo','Husqvarna Group','Global group','United Kingdom',None,'Hover mower brand listed among Husqvarna Group brands.',HG,None),
 ('Poulan / PoulanPro','Husqvarna Group','Global group','United States',None,'US outdoor power brand listed among Husqvarna Group brands.',HG,None),
 ('Weed Eater','Husqvarna Group','Global group','United States',None,'String trimmer brand listed among Husqvarna Group brands.',HG,None),
 ('Jonsered','Husqvarna Group','Global group','Sweden',None,'Chainsaw brand listed among Husqvarna Group brands.',HG,None),
 ('Klippo','Husqvarna Group','Global group','Denmark',None,'Mower brand listed among Husqvarna Group brands.',HG,None),
 ('RedMax','Husqvarna Group','Global group','Japan',None,'Handheld power equipment brand listed among Husqvarna Group brands.',HG,None),
 ('Stihl','Andreas Stihl AG & Co. KG','Global group','Germany',None,'Founded 1926; Wikipedia calls it the biggest chainsaw maker in the world since 1971.',W+'Stihl','landmark'),
 ('Viking','Andreas Stihl AG & Co. KG','Global group','Austria','1992','Austrian mower maker acquired by Stihl in 1992.',W+'Stihl',None),
 ('Toro','The Toro Company','Global group','United States',None,'Founded 1914 as the Toro Motor Company.',W+'The_Toro_Company',None),
 ('Exmark','The Toro Company','Global group','United States','1997','Zero-turn mower brand acquired by Toro in 1997.',W+'The_Toro_Company',None),
 ('Lawn-Boy','The Toro Company','Global group','United States','1989','Mower brand bought by Toro from Outboard Marine Corporation in 1989.',W+'The_Toro_Company',None),
 ('Hayter','The Toro Company','Global group','United Kingdom','2005','British mower brand listed among Toro brands.',W+'The_Toro_Company',None),
 ('Irritrol','The Toro Company','Global group','United States',None,'Irrigation brand listed among Toro brands.',W+'The_Toro_Company',None),
 ('John Deere','Deere & Company','Global group','United States',None,'Lawn tractors, zero-turn mowers and Gator utility vehicles from Deere & Company.',W+'Deere_%26_Company',None),
 ('Lesco','Deere & Company','Global group','United States',None,'Turf and garden supplier listed among Deere subsidiaries.',W+'Deere_%26_Company',None),
 ('Honda','Honda Motor Co.','Global group','Japan',None,'Walk-behind petrol mowers; ranked third in the Report Prime lawn mower list for 2024.','https://www.reportprime.com/lawn-mower-r18944/company',None),
 ('MTD','MTD Products (SBD)','Global group','United States',None,'Residential ride-on maker ranked fifth in the Report Prime list for 2024.','https://www.reportprime.com/lawn-mower-r18944/company',None),
 ('Briggs & Stratton','Briggs & Stratton','Independent','United States',None,'Engine and push mower maker ranked sixth in the Report Prime list for 2024.','https://www.reportprime.com/lawn-mower-r18944/company',None),
 ('Stiga','Stiga S.p.A.','Independent','Italy',None,'Battery ride-on maker ranked seventh in the Report Prime list for 2024.','https://www.reportprime.com/lawn-mower-r18944/company',None),
 ('Makita','Makita Corporation','Global group','Japan',None,'Cordless outdoor power equipment maker ranked eighth in the Report Prime list for 2024.','https://www.reportprime.com/lawn-mower-r18944/company',None),
 ('Worx','Positec','Independent','China',None,'DIY robotic mower maker ranked ninth in the Report Prime list for 2024.','https://www.reportprime.com/lawn-mower-r18944/company',None),
]
# order by owner group then name
order=['Husqvarna Group','Andreas Stihl AG & Co. KG','The Toro Company','Deere & Company','Honda Motor Co.','MTD Products (SBD)','Briggs & Stratton','Stiga S.p.A.','Makita Corporation','Positec']
xs=[]
for n,o,t,c,oy,dd,s,role in sorted(brand_defs,key=lambda b:(order.index(b[1]),b[0])):
    e=ent(n,dd,n,'',s,own=o,tier=t,cty=c,own_y=oy,role=role,g='Group: '+o)
    xs.append(e)
shelf={'n':'Powered brand owners','t':'The companies behind mowers and powered garden tools, with the brands each owns; tools themselves are on the other shelves.','k':[{
 'n':'Powered garden equipment brand','a':'outdoor power equipment brand','d':'A brand of mowers, saws, trimmers or other powered garden machines, listed under the group that owns it.','s':HG,
 'x':xs,
 'nl':'One entry is a powered garden equipment brand sold under its own name, shown with its owner group; ranges are held in the brand register.',
 'sel':'Brands named on the fetched Wikipedia pages of Husqvarna Group, Stihl, The Toro Company and Deere & Company, plus the other companies in the Report Prime 2024 lawn mower top ten (Honda, MTD, Briggs & Stratton, Stiga, Makita, Worx; Robomow is under Robotic mower). Covers 24 brands; groups outside these pages (Bosch, Ryobi, Einhell) sit in the brand register.',
 'xg':'by owner group',
 'tt':[['Power source',['Petrol','Battery','Mains electric','Robotic']],['Market',['Domestic','Professional']]]}]}
dept('Lawn care')['s'].append(shelf)
dept('Lawn care')['ms']=[
 {'mkt':'Wire-free robotic lawn mowers, global','who':'Segway Navimow','share':'No. 1 by unit sales','yr':2024,'s':'https://www.servicedealer.co.uk/latest-news/market-leader-for-wire-free-robotic-mower-sales-revealed','note':'Euromonitor International ranking by unit volume across dealers, Amazon, direct stores and offline stores; no percentage given.'},
 {'mkt':'Outdoor power equipment, Husqvarna Group','who':'Husqvarna Group','share':'SEK 46.6 billion revenue','yr':2025,'s':HG,'note':'Group revenue across all products; brands Husqvarna, Gardena, McCulloch, Flymo and others.'},
 {'mkt':'Consumer watering products, Europe','who':'Husqvarna Group (Gardena)','share':'European leader','yr':2007,'s':HG,'note':'Wikipedia says Husqvarna became the European leader in consumer watering products after buying Gardena; later share not given.'},
 {'mkt':'Handheld forestry and chainsaws, global','who':'Stihl','share':'Largest chainsaw maker','yr':1971,'s':W+'Stihl','note':'Wikipedia says Stihl has been the biggest chainsaw maker in the world since 1971; 2025 revenue EUR 5.479 billion.'},
 {'mkt':'Lawn and turf equipment, Toro','who':'The Toro Company','share':'US$4.51 billion revenue','yr':2025,'s':W+'The_Toro_Company','note':'Group revenue across all products.'},
 {'mkt':'Lawn and garden, Deere','who':'Deere & Company','share':'US$45.7 billion revenue','yr':2025,'s':W+'Deere_%26_Company','note':'Group revenue across all products, mostly agriculture and construction.'},
 {'mkt':'Lawn mowers, global ranking','who':'Deere & Company, Husqvarna Group, Honda Motor Co., The Toro Company, MTD Products','share':'Ranked 1 to 5','yr':2024,'s':'https://www.reportprime.com/lawn-mower-r18944/company','note':'Report Prime top ten; its percentages add to 133.6 % and are not used here.'},
]
# ---------- Cutting & pruning market fact is in Lawn care ms (Stihl)
# ---------- Outdoor cooking
WW=W+'Weber_Inc.'
k=find('Kettle grill')
upd(k,'Weber Original Kettle',own='BDT Capital Partners',tier='Global group',cty='United States',own_y='2023',role='origin',d='Round charcoal kettle grill invented by George Stephen Sr. in 1951; the model that started the Weber range.')
k['nl']='One entry is a kettle grill line sold under its own name; sizes and generations are versions.'
k['sel']='Wikipedia Weber Inc. and the Weber history page name the original kettle as the founding product. Complete: 1 of 1 kettle lines named there.'
k=find('Kamado grill')
upd(k,'Mushikamado',role='origin',d='Traditional Japanese clay cooking stove from which the kamado-style cooker descends.')
upd(k,'Big Green Egg',own='Big Green Egg (privately held)',tier='Independent',cty='United States',d='Atlanta ceramic kamado founded by Ed Fisher in 1974, sold in seven sizes from Mini to 2XL.',role='landmark')
upd(k,'Kamado Joe Classic Joe',own='The Middleby Corporation',tier='Global group',cty='United States',own_y='2021')
upd(k,'Primo Oval',cty='United States')
k['nl']='One entry is a kamado or ceramic cooker line sold under its own name; sizes are versions.'
k['sel']='Wikipedia Kamado, Wikipedia Big Green Egg and the Middleby 2021 acquisition notice, plus maker pages for Primo and Komodo Kamado. Covers 5 lines; no whole-space list of kamado makers was found, and the Kamado Wikipedia page names none.'
k=find('Bullet smoker')
upd(k,'Weber Smokey Mountain Cooker',own='BDT Capital Partners',tier='Global group',cty='United States',own_y='2023')
k['nl']='One entry is a bullet smoker line sold under its own name.'
k['sel']='Weber history pages; Complete: 1 of 1 bullet smoker lines found on fetched pages.'
k=find('Offset smoker')
k['nl']='One entry is an offset smoker line sold under its own name.'
k['sel']='Maker pages fetched for each line; no whole-space reference exists. Covers 4 lines.'
k=find('Gas grill')
for n in ('Weber Genesis','Weber Spirit','Weber Summit','Weber Gas Barbecue Kettle'):
    upd(k,n,own='BDT Capital Partners',tier='Global group',cty='United States',own_y='2023')
upd(k,'Napoleon Prestige',tier='Independent',cty='Canada')
k['nl']='One entry is a gas grill line sold under its own name; sizes and burner counts are versions.'
k['sel']='Weber history pages and a Consumer Reports page for Napoleon. Covers 5 lines; no whole-space reference exists.'
k=find('Pellet grill')
upd(k,'Traeger pellet grill',own='Traeger, Inc.',tier='National champion',cty='United States',role='origin',d='Pellet grill created by Joe Traeger in 1985 and patented in 1987; Traeger called itself the category leader in its 2021 prospectus.')
upd(k,'Pit Boss pellet grill',own='Dansons',tier='Independent',cty='United States')
upd(k,'Louisiana Grills Founders Legacy',own='Dansons',tier='Independent',cty='United States',own_y='')
upd(k,'Weber SmokeFire',own='BDT Capital Partners',tier='Global group',cty='United States',own_y='2023')
upd(k,'Recteq Bullseye Deluxe',tier='Independent',cty='United States')
for x in k['x']:
    if not x.get('own_y'): x.pop('own_y',None)
k['nl']='One entry is a pellet grill line sold under its own name.'
k['sel']='Wikipedia Pellet grill (Traeger, Louisiana Grills and Pit Boss owners), Traeger 2021 prospectus, Weber and maker pages. Covers 5 lines; no whole-space list exists.'
k=find('Open-fire grill')
k['x']=[]; k.pop('x')
k['d']=k['d'].rstrip('.')+'. Regional barbecue traditions (parrilla, braai, Santa Maria, hibachi and shichirin) belong to the Culinary taxonomy.'
k=find('Flat-top griddle')
upd(k,'Blackstone griddle',tier='Independent',cty='United States')
k['nl']='One entry is a griddle line sold under its own name.'
k['sel']='Blackstone maker page. Covers 1 line; no whole-space reference exists.'
k=find('Portable grill')
k['x']=[x for x in k['x'] if x['n']!='Hibachi / shichirin']
upd(k,'LazyMan Model AP',role='origin') if False else None
for n in ('Weber Smokey Joe','Weber Q','Weber Go-Anywhere'):
    upd(k,n,own='BDT Capital Partners',tier='Global group',cty='United States',own_y='2023')
k['nl']='One entry is a portable grill line sold under its own name.'
k['sel']='Weber history pages, Wikipedia Barbecue grill and maker pages. Covers 5 lines; no whole-space reference exists.'
k=find('Pizza oven')
for n in ('Ooni pellet oven','Ooni Pro','Ooni Koda','Ooni Karu'):
    upd(k,n,own='Ooni',tier='Independent',cty='United Kingdom')
upd(k,'Ooni Pro',y='2017',d='Wood and charcoal oven that raised funds on Indiegogo in April 2017 and shipped in November 2017.')
upd(k,'Ooni Koda',y='2019',d='Gas-fired oven introduced on 26 February 2019; the Koda 16 followed in March 2020.')
upd(k,'Ooni Karu',y='2019',d='Wood and charcoal oven launched on Kickstarter on 27 August 2019; Karu 16 followed in 2021.')
for n in ('Gozney Roccbox','Gozney Dome','Gozney Arc','Gozney Tread'):
    upd(k,n,tier='Independent',cty='United Kingdom')
k['x'].append(ent('Ooni Fyra','Pellet-fired portable oven; the Fyra 12 is the current model.','Ooni','',W+'Ooni_(company)',own='Ooni',tier='Independent',cty='United Kingdom'))
k['nl']='One entry is a pizza oven line sold under its own name; sizes are versions.'
k['sel']='Wikipedia Ooni (company) for Ooni lines, Gozney and Fontana maker pages. Covers 10 lines; no whole-space reference exists.'
k=find('Fire pit'); k.pop('x',None)
dept('Outdoor cooking')['ms']=[
 {'mkt':'US households owning a grill','who':'All grill brands','share':'60 % of households','yr':2021,'s':'https://www.sec.gov/Archives/edgar/data/1857853/000119312521231685/d128215d424b4.htm','note':'Estimate in the Traeger 2021 prospectus; about 20 million grills bought in the US in 2020.'},
 {'mkt':'Wood pellet grills, global','who':'Traeger, Inc.','share':'Self-described category leader','yr':2021,'s':'https://www.sec.gov/Archives/edgar/data/1857853/000119312521231685/d128215d424b4.htm','note':'Prospectus statement; no share percentage given. Average pellet grill price USD 596 in 2020.'},
 {'mkt':'Weber Inc.','who':'BDT Capital Partners','share':'Private since 2023','yr':2023,'s':WW,'note':'BDT bought a majority in 2010, listed it on the NYSE in 2021 and bought the remaining stock in 2023.'},
 {'mkt':'Kamado Joe, Masterbuilt, Char-Griller','who':'The Middleby Corporation','share':'Acquired together','yr':2021,'s':'https://www.middleby.com/newsroom/middleby-completes-kamado-joe-and-masterbuilt-acquisition-announces-addition-of-char-griller/','note':'Char-Griller revenue about USD 150 million in 2021.'},
 {'mkt':'Pit Boss and Louisiana Grills pellet grills','who':'Dansons','share':'Owner of both brands','yr':2019,'s':W+'Pellet_grill','note':'Wikipedia names Dansons as owner of Pit Boss and Louisiana Grills.'},
]
# ---------- Bonsai styles
B=W+'Bonsai_styles'
sty=[
('Trunk orientation','Chokkan','Formal upright','Straight upright trunk with branches tapering evenly from bottom to top.'),
('Trunk orientation','Moyogi','Informal upright','Trunk curves but the apex sits directly above the base.'),
('Trunk orientation','Shakan','Slanting','Trunk emerges at an angle, with the apex offset from the root base.'),
('Trunk orientation','Sho-shakan','Slight slant','Slight sideways lean named in the article introduction.'),
('Trunk orientation','Chu-shakan','Medium slant','Deeper one-sided lean named in the article introduction.'),
('Trunk orientation','Dai-shakan','Strong slant','Deepest one-sided lean named in the article introduction.'),
('Trunk orientation','Kengai','Cascade','Apex falls below the base of the pot, as on trees growing over water or down slopes.'),
('Trunk orientation','Han-kengai','Semi-cascade','Apex reaches the pot rim or lower, but not below the pot bottom.'),
('Trunk orientation','Takan-kengai','Multi-trunk cascade','Cascade style in which two or more trunks drop downward.'),
('Trunk and bark surface','Sabamiki','Split trunk · hollow trunk','Trunk split or hollowed by severe weathering.'),
('Trunk and bark surface','Sharimiki','Driftwood','Trunk with a large bare weathered section while live bark still carries sap.'),
('Trunk and bark surface','Nebikan','Twisted trunk · Nejikan','Style with a twisted trunk.'),
('Trunk and bark surface','Sabakan','Vertical split trunk','Style with a vertical split or hollows.'),
('Trunk and root placement','Neagari','Exposed root','Roots are bare and extend like trunk extensions above the soil.'),
('Trunk and root placement','Sekijoju','Root over rock · Deshojo','Roots wrap over a rock at the trunk base, then descend into soil.'),
('Trunk and root placement','Ishizuke','Clinging to a rock · Ishitsuki · Ishizuki','Roots grow in soil within the cracks and crevices of a rock.'),
('Several trunks from one root','Sokan','Twin trunk','Two trunks from one root system, one taller and thicker.'),
('Several trunks from one root','Sankan','Three trunk','Three trunks of varied size, arranged so no straight line crosses all three.'),
('Several trunks from one root','Gokan','Five trunk','Like the three-trunk style with a second dominant tree under the largest.'),
('Several trunks from one root','Nanakan','Seven trunk','Follows the five-trunk approach with more trunks.'),
('Several trunks from one root','Kyukan','Nine trunk','Follows the five-trunk approach with more trunks.'),
('Several trunks from one root','Kabudachi','Clump · Kabubuki','Three or more odd-numbered trunks sprouting from one point.'),
('Several trunks from one root','Korabuki','Turtle · stump','Multiple trunks rising from a domed turtle-back root base.'),
('Several trunks from one root','Ikadabuki','Straight-line raft · Ikadabuji','Line of new trunks grown from a tree that toppled sideways.'),
('Several trunks from one root','Netsunagari','Sinuous raft · Netsuranari','Like the straight-line raft but with a bending underlying trunk.'),
('Several trees on their own roots','Soju','Two tree','Two trees of one species with separate roots, one dominant.'),
('Several trees on their own roots','Sambon-yose','Three tree','Three trees, one dominant and two smaller.'),
('Several trees on their own roots','Gohon-yose','Five tree','Five trees with one or two dominant trees.'),
('Several trees on their own roots','Nanahon-yose','Seven tree','Seven trees, following the five-tree approach.'),
('Several trees on their own roots','Kyuhon-yose','Nine tree','Nine trees, following the five-tree approach.'),
('Several trees on their own roots','Yose-ue','Forest','Many trees in a low pot arranged to suggest a view into a forest.'),
('Branch placement and orientation','Bunjingi','Literati','Bare, often contorted trunk with branches kept few and concentrated near the apex.'),
('Branch placement and orientation','Hokidachi','Broom','Straight trunk with a ball-shaped crown of fine branching, often on elms.'),
('Branch placement and orientation','Takozukuri','Octopus','Short thick trunk with long curved branches like tentacles.'),
('Branch placement and orientation','Fukinagashi','Windswept','Branches shaped as if by constant wind from one direction; applies to several basic styles.'),
]
bx=[]
for g,n,al,dd in sty:
    e={'n':n,'a':al,'d':dd,'s':B,'g':g}
    if n=='Chokkan': e['role']='origin' if False else None
    e={q:v for q,v in e.items() if v}
    bx.append(e)
bshelf={'n':'Trees & styles','t':'The styled tree itself, named by its Japanese style; the species grown belongs to the living plants register.','k':[{
 'n':'Bonsai style','a':'bonsai tree style · bonsai form','d':'The shape a bonsai tree is trained into, named by trunk, root, group or branch form.','s':B,
 'nl':'One entry is a named bonsai style; Japanese name first, English names are aliases.',
 'sel':"Every style named in Wikipedia's Bonsai styles article, grouped by the article's headings. Complete: 35 of 35 styles named in Wikipedia's Bonsai styles article.",
 'xg':'by trunk, root, group or branch form','x':bx,
 'see':[['C3','Juniper bonsai','the species a style is applied to']]}]}
dept('Bonsai')['s'].insert(0,bshelf)
dept('Bonsai')['note']=(dept('Bonsai').get('note','')+' Styles are entries on Bonsai style; species belong to the living plants register.').strip()
json.dump(d,open(R+'work/V4_C2/C2.tmp','w'),ensure_ascii=False,indent=1)
os.replace(R+'work/V4_C2/C2.tmp',R+'out/C2.json')
print('removed m',removed_m,'removed x',len(removed_x))
json.dump(removed_x,open(R+'work/V4_C2/removed_x.json','w'),ensure_ascii=False)
