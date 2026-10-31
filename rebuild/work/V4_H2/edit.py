import json,os,collections
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'H2.json')); bj=json.load(open(R+'H2_brands.json')); b=bj['b']
names={x['n'] for x in b}
add=collections.OrderedDict()
def reg(maker,kind,src,model=None,rng=None):
    if not maker or maker in names: return
    e=add.setdefault(maker,{'n':maker,'c':'','f':'','seg':'Mainstream','kinds':[],'lines':[],'sig':[],'s':src,'kf':kind['n'].lower()})
    if kind['n'].lower() not in e['kinds']: e['kinds'].append(kind['n'].lower())
    if rng and rng not in e['lines']: e['lines'].append(rng)
    if model and model not in e['sig']: e['sig'].append(model)
removed=0
KEEP={'Collector cane','Manual wheelchair','Braille device'}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            for f in('m','r'):
                for e in k.get(f,[]) or []:
                    reg(e[1],k,k.get('s',''),e[0] if f=='m' else None,e[0] if f=='r' else None)
                    removed+=1
                if f in k: del k[f]
# collector canes
def kind(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k
W='https://en.wikipedia.org/wiki/Walking_stick'
c=kind('Collector cane')
old={x['n']:x for x in c['x']}
def E(n,a,dsc,g,src=W,dt='',**kw):
    e={'n':n,'a':a,'d':dsc,'mk':'','y':'','s':src,'g':g}
    if dt:e['dt']=dt
    e.update(kw); return e
G1,G2,G3='Named for the wood or plant','Regional and cultural sticks','Fitted and gadget canes'
c['x']=[
 E('Ashplant','','British or Irish stick of ash; Royal Tank Regiment officers carry one.',G1,dt='ash shaft'),
 E('Blackthorn stick','Shillelagh','Irish stick of blackthorn or oak, used as a walking stick and cudgel; the name means thonged willow.',G1,old['Shillelagh']['s'],old['Shillelagh']['dt']),
 E('Malacca cane','Malacca','Malay stick made from rattan palms (Calamus).',G1,dt='rattan shaft'),
 E('Penang lawyer','','Stick of stripped, straightened and polished Licuala palm stem.',G1,dt='Licuala palm shaft'),
 E('Supplejack','','Cane made from a tropical American vine.',G1,dt='vine shaft'),
 E('Whangee cane','whanghee','Asian bamboo cane with a curved handle, carried by the Tramp character and sold as a riding crop.',G1,dt='bamboo shaft · natural root handle'),
 E('Ziegenhainer','','Knotty German stick of European cornel, also used by duellists\' seconds as a melee weapon.',G1,dt='cornel wood · knotted shaft'),
 E('Kebbie','','Rough Scottish stick with a hooked head, similar to a shillelagh.',G2,dt='hooked head'),
 E('Makila','makhila','Basque staff, usually medlar wood, with gold or silver fittings that may conceal a steel blade.',G2,dt='medlar wood · metal fittings'),
 E('Waddy','','Australian Aboriginal walking stick or war club, about one metre long, sometimes with a stone head bound with string and beeswax.',G2,dt='length about one metre · stone or wooden head'),
 E('Dress cane','','Classic late 19th-century walking cane carried as part of formal dress.',G3),
 E('Retractable cane','','Cane that conceals features such as hidden compartments, pool cues or blades; popular with collectors.',G3,dt='hidden fitting'),
 E('Swordstick','sword cane','Cane whose shaft is a scabbard for a concealed blade; fashionable in the 18th and 19th centuries.',G3,old['Swordstick']['s'],old['Swordstick']['dt'],y='18th century'),
 E('Tippling cane','tippler','Cane with a hollowed compartment near the top for hiding a flask or vial.',G3,dt='hidden compartment'),
]
c['nl']='One entry is a named type of walking stick or cane collected for its wood, origin or fitting, rather than used as a mobility aid; makers are not entries.'
c['sel']="Every named stick or cane type in Wikipedia's Walking stick article, plus the Swordstick article for the swordstick. Shooting stick, alpenstock, pike staff and scout staff are left out as tools, and the cane gun, canne de combat and pace stick are only cross-references there. No whole-space reference exists."
c['xg']='by what the stick is known for'
c['see']=c.get('see',[])
# wheelchair
w=kind('Manual wheelchair')
ord_={'Everest & Jennings folding chair':0,'Quickie':1,'Küschall Competition':2,'TiLite titanium rigid chair':3}
w['x'].sort(key=lambda e:ord_[e['n']])
for e in w['x']:
    e['g']='Milestone lines'
    if e['n'].startswith('Everest'): e['role']='origin'
w['nl']='One entry is a manual wheelchair line that a fetched page names as a milestone in the chair\'s history; models and sizes are not entries.'
w['sel']='No whole-space reference exists. The four lines are those with their own Wikipedia articles or sections (Wheelchair, Marilyn Hamilton, Rainer Küschall, TiLite); the Everest & Jennings chair is the first mass-market wheelchair on the Wheelchair page.'
w['xg']='single section'
for e in w['x']:
    pass
# braille
br=kind('Braille device')
br['x'][0]['g']='Braille writers'
br['nl']='One entry is a braille writing or reading device line sold under its own name; later and adapted versions are versions.'
br['sel']='No whole-space reference exists. The one entry is the Perkins Brailler, which has its own Wikipedia article; makers of braille displays and note-takers are in the brand register.'
br['xg']='by device form'
# market panels
def dept(n): return [x for x in d['depts'] if x['n']==n][0]
dept('Monitors, tests & dosing')['ms']=[{"mkt":"Global home blood-pressure monitors","who":"Omron Healthcare","share":"about 46 %","yr":2015,"s":"https://www.omron.com/media/press/2016/12/h1205.html","note":"worldwide share by monetary value in FY2015, Omron's own research; the global market was 40 million units"}]
dept('Monitors, tests & dosing')['msum']='Omron states it held about 46 % of the world home blood-pressure monitor market by value in 2015. No independent ranking was found.'
H='https://hearinghealthmatters.org/hearing-news-watch/2013/research-firm-analyzes-market-share-retail-stores-prospects-of-major-hearing-aid-makers/'
dept('Hearing')['ms']=[{"mkt":"Global hearing aids","who":w_,"share":s_,"yr":2012,"s":H,"note":"unit sales, Sanford C. Bernstein estimate as reported in 2013"} for w_,s_ in [("Sonova","24 %"),("Demant","23 %"),("Siemens / Sivantos","17 %"),("GN Store Nord","16 %"),("Starkey","9 %"),("Widex","9 %")]]
dept('Hearing')['msum']='Six makers shared the hearing-aid market in 2012: Sonova 24 %, Demant 23 %, Sivantos 17 %, GN 16 %, Starkey and Widex 9 % each. The figures are by units and are old; WS Audiology formed in 2019 from Sivantos and Widex.'
dept('Supplements & nutrition')['ms']=[{"mkt":"Global vitamins, minerals and supplements","who":"Haleon","share":"about 3 %","yr":2023,"s":"https://www.sec.gov/Archives/edgar/data/1900304/000155837025003368/hln-20241231x20f.htm","note":"Haleon states it is the largest player; its own analysis of third-party data"}]
dept('Supplements & nutrition')['msum']='Haleon states it is the largest vitamins, minerals and supplements company in 2023, with about 3 % of the world market, so the field is fragmented.'
# register
for who,cty in [('Sonova',''),('Demant',''),('GN Store Nord',''),('Sivantos',''),('Haleon','')]:
    if who not in names and who not in add:
        add[who]={'n':who,'c':'','f':'','seg':'Professional & flagship','kinds':['hearing aids' if who!='Haleon' else 'supplements'],'lines':[],'sig':[],'s':H if who!='Haleon' else dept('Supplements & nutrition')['ms'][0]['s'],'kf':'owner group'}
for e in add.values():
    ks=', '.join(e.pop('kinds'))
    e['d']=f"Brand or maker of {ks}."
    e['sig']=e['sig'][:6]; e['eras']=[]; e['sc']=[]; e['rel']=[]
b.extend(add.values())
b.sort(key=lambda x:x['n'].lower())
for p,o in((R+'H2.json',d),(R+'H2_brands.json',bj),(R+'H2_renames.json',{})):
    open(p+'.tmp','w').write(json.dumps(o,ensure_ascii=False,indent=1)); os.replace(p+'.tmp',p)
print(removed,len(add))
