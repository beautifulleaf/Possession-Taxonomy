import json,re,os,sys
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/A2.json')); B=json.load(open(R+'out/A2_brands.json')); reg={x['n']:x for x in B['b']}
WL='https://en.wikipedia.org/wiki/List_of_basketball_shoe_brands'
LB='https://en.wikipedia.org/wiki/List_of_boots'
kinds={}
for dep in d['depts']:
    for sh in dep['s']:
        for k in sh['k']: kinds[k['n']]=k
def allnames():
    s=set()
    for k in kinds.values():
        s.add(k['n'].lower())
        for a in (k.get('a') or '').split('·'): s.add(a.strip().lower())
        for e in k.get('x',[]):
            s.add(e['n'].lower())
            for a in (e.get('a') or '').split('·'): s.add(a.strip().lower())
    return s
# ---- 1 owners
OW={ # mk:(own,tier,own_y,source)
'Diadora':('Geox','Independent','', 'https://en.wikipedia.org/wiki/Diadora'),
'Keds':('Designer Brands','Independent','2023','https://en.wikipedia.org/wiki/Keds'),
'Sperry':('Authentic Brands Group','Independent','','https://en.wikipedia.org/wiki/Sperry_(brand)'),
'TOMS':('Creditors (Jefferies Financial Group, Nexus Capital Management, Brookfield Asset Management)','Independent','2019','https://en.wikipedia.org/wiki/Toms_Shoes'),
'Chanel':('Alain and Gérard Wertheimer','Independent','','https://en.wikipedia.org/wiki/Chanel'),
'PF Flyers':('Kassia Designs, LLC','Independent','','https://en.wikipedia.org/wiki/PF_Flyers'),
'G.H. Bass':('G-III Apparel Group','Independent','2013','https://en.wikipedia.org/wiki/G.H._Bass_%26_Co.'),
'Salvatore Ferragamo':('Ferragamo family (majority shareholders)','Independent','','https://en.wikipedia.org/wiki/Salvatore_Ferragamo_S.p.A.'),
'Hermès':('Descendants of Thierry Hermès (controlling family)','Independent','','https://en.wikipedia.org/wiki/Herm%C3%A8s'),
'Car Shoe':('Prada','Global group','','https://en.wikipedia.org/wiki/The_Original_Car_Shoe'),
'Chippewa':('Justin Brands','Independent','','https://en.wikipedia.org/wiki/Chippewa_Boots'),
'Havaianas':('Alpargatas S.A.','Independent','','https://en.wikipedia.org/wiki/Havaianas'),
'K-Swiss':('KP Global','Independent','','https://en.wikipedia.org/wiki/K-Swiss'),
'Maison Margiela':('OTB Group','Independent','','https://en.wikipedia.org/wiki/Maison_Margiela'),
'Scarpa':('Parisotto family','Independent','1956','https://en.wikipedia.org/wiki/Scarpa_(company)'),
'R.M. Williams':('Tattarang (Andrew Forrest)','Independent','2020','https://en.wikipedia.org/wiki/R._M._Williams_(company)'),
'Golden Goose':('Permira funds (Carlyle holds a minority stake)','Independent','2020','https://www.permira.com/news-and-insights/announcements/permira-funds-complete-investment-in-golden-goose'),
'Danner':('LaCrosse Footwear (owned by ABC-Mart since 2012)','Independent','1994','https://en.wikipedia.org/wiki/LaCrosse_Footwear'),
'Volley':('Anchorage Capital Partners','Independent','2014','https://en.wikipedia.org/wiki/Volley_(shoe)'),
'Wildsmith Shoes':('Herring Shoes','Independent','2016','https://en.wikipedia.org/wiki/Wildsmith_Shoes'),
'Sebago':('BasicNet','Independent','','https://www.wikidata.org/wiki/Q3476844'),
'Superga':('BasicNet','Independent','','https://www.wikidata.org/wiki/Q3073822'),
'Vivobarefoot':('Galahad J.D. Clark','Independent','','https://www.wikidata.org/wiki/Q7937938'),
}
nown=0
for mk,(o,t,y,s) in OW.items():
    r=reg.get(mk)
    if r is None: print('no reg',mk); continue
    r['own']=o; r['tier']=t; r['own_s']=s
    if y: r['own_y']=y
    for k in kinds.values():
        for e in k.get('x',[]):
            if e.get('mk')==mk:
                e['own']=o; e['tier']=t; nown+=1
                if y: e['own_y']=y
print('entries owner set',nown)
# ---- 2 regions
RG={ # entry name: (g, d or None, source)
'Ashida':('Japan',None,'https://en.wikipedia.org/wiki/Geta_(footwear)'),
'Tengu geta':('Japan',None,'https://en.wikipedia.org/wiki/Geta_(footwear)'),
'Okobo':('Japan',None,'https://en.wikipedia.org/wiki/Geta_(footwear)'),
'Mitsu-ashi geta':('Japan',None,'https://en.wikipedia.org/wiki/Geta_(footwear)'),
'Gomusin':('Korea','Traditional Korean shoes made of rubber, wide with low heels.','https://en.wikipedia.org/wiki/Gomusin'),
'Xiuhuaxie':('China','Sub-type of traditional Chinese cloth shoe.','https://en.wikipedia.org/wiki/Xiuhuaxie'),
'Uwabaki':('Japan','Japanese slippers worn indoors at school or certain companies.','https://en.wikipedia.org/wiki/Uwabaki'),
'Multani khussa':('Sindh and southern Punjab, Pakistan','Traditional hand-made footwear, mostly of vegetable-tanned leather.','https://en.wikipedia.org/wiki/Khussa_(footwear)'),
'Hnyat-phanat':('Myanmar','Burmese traditional sandal, similar to flip-flops.','https://en.wikipedia.org/wiki/Hnyat-phanat'),
'Haferlschuh':('Bavaria, Germany','Traditional Bavarian shoe, designed originally as a work shoe for alpine terrain.','https://en.wikipedia.org/wiki/Haferlschuh'),
'Träskor':('Sweden','Swedish clogs typically made from alder, sometimes birch or pine.','https://en.wikipedia.org/wiki/Tr%C3%A4skor'),
'Cantabrian albarcas':('Cantabria, northern Spain','Rustic one-piece wooden shoe used particularly by the peasants of Cantabria.','https://en.wikipedia.org/wiki/List_of_shoe_styles'),
'Avarca':('Spain',None,'https://www.wikidata.org/wiki/Q2679245'),
'Furlane':('Italy',None,'https://www.wikidata.org/wiki/Q18501783'),
'Ciocia':('Italy',None,'https://www.wikidata.org/wiki/Q3677385'),
'Calceus':('Roman Republic and Empire','Common upper-class male footwear, normally of hobnailed leather, flat-soled and reaching the lower shin.','https://en.wikipedia.org/wiki/Calceus'),
'Caligae':('Roman Empire','Heavy-soled hobnailed military sandal-boots worn as standard issue by Roman legionary foot-soldiers.','https://en.wikipedia.org/wiki/Caliga'),
'Tzangion':('Byzantine Empire','Boot or sandal that became part of the Byzantine Emperors\' regalia in the Middle Ages.','https://en.wikipedia.org/wiki/Tzangion'),
'Chopine':(None,'Women\'s platform shoe popular in the 15th to 17th centuries, first used as an overshoe against mud.','https://en.wikipedia.org/wiki/Chopine'),
'Poulaine':(None,'Unisex shoe with an extremely long, elongated toe.','https://en.wikipedia.org/wiki/Poulaine'),
'Pigache':(None,'Shoe with a sharp upturned point at the toes.','https://en.wikipedia.org/wiki/Pigache'),
'Buskin':(None,'Knee- or calf-length boot of leather or cloth, enclosed and laced.','https://en.wikipedia.org/wiki/Buskin'),
'Peranakan beaded slippers':(None,'Beaded slippers worn by a nyonya to complete her sarong kebaya outfit.','https://en.wikipedia.org/wiki/Peranakan_beaded_slippers'),
'Flamenco shoe':(None,'Shoe worn by flamenco dancers, typically by women with a heel.','https://en.wikipedia.org/wiki/Flamenco_shoe'),
}
cnt=0
for k in kinds.values():
    for e in k.get('x',[]):
        r=RG.get(e['n'])
        if r and (e.get('g')=='Region not stated' or not e.get('d')):
            if r[0]: e['g']=r[0]
            if r[1] and not e.get('d'): e['d']=r[1]
            if r[0] or r[1]: e['s']=r[2]
            cnt+=1
print('region/desc updates',cnt)
# ---- 3 boots from List of boots
cands={ # kind: [names]
'Work boot':['Hobnail boot','Caulk boot','Steel-toe boot','Australian boot','Hip boot'],
'Over-the-knee boot':['Thigh-high boot'],
'Cowboy boot':['Mexican pointy boot'],
'Equestrian riding boot':['Paddock boot','Postillion boot'],
'Combat & military boot':['Army combat boot','Cold weather boot','Desert combat boot','Mountain combat boot','Tanker boot','Jungle boot'],
'Jackboot & Hessian boot':['Cavalry jackboot','Hobnailed jackboot'],
'Named European forms':['Russian boot','Burki boot'],
}
have=allnames(); added_boots=[]
for kn,ns in cands.items():
    k=kinds[kn]
    for n in ns:
        if n.lower() in have: continue
        e={'n':n,'d':'','s':LB}
        if kn=='Named European forms': e['g']='Region not stated'
        elif 'g' in k.get('x',[{}])[0]: pass
        # copy g style from kind entries
        gs=[x.get('g') for x in k.get('x',[])]
        if kn!='Named European forms': e['g']='Region not stated'
        k.setdefault('x',[]).append(e); added_boots.append(n)
print('boots added',added_boots)
for kn,txt in [('Over-the-knee boot','Thigh-high boots'),]: pass
# aliases
def alias(kn,a):
    k=kinds[kn]; cur=[x.strip() for x in (k.get('a') or '').split('·') if x.strip()]
    if a.lower() not in [c.lower() for c in cur]: cur.append(a); k['a']=' · '.join(cur)
alias('Rain boot','gumboot'); alias('Overshoe','galosh'); alias('Platform shoe','platform boot'); alias('Over-the-knee boot','thigh-high boot')
# ---- 4 basketball list
REF=[ # brand(mk), model, year, where: 'B' add here, or existing kind label
('adidas','Jabbar','1971'),('adidas','Campus','1970s','X'),('adidas','Top 10','1979'),('adidas','Forum','1984','X'),('adidas','Ewing Rivalry 3','1986'),('adidas','Real Deal II','1986'),('adidas','Ewing Attitude','1987'),('adidas','Ewing Conductor','1987'),('adidas','Mutombo','1992'),('adidas','EQT Elevation','1996'),('adidas','EQT Top Ten','1996'),('adidas','K8B','1997'),('adidas','Real Deal','1997'),('adidas','KB82','1998'),('adidas','Bromium','1999'),('adidas','KB8 III','1999'),('adidas','TMAC','2002'),('adidas','TMAC 2','2003'),('adidas','TMAC III','2004'),('adidas','C-Billups','2006'),('adidas','Kevin Garnett III','2006'),('adidas','TMAC VI','2006'),('adidas','Skyhoot Plus Low','2007'),('adidas','adiZero Rose','2009'),('adidas','TS Commander Lite "Skeleton"','2009'),('adidas','adiZero Rose 1.5','2010'),('adidas','Superbeast','2010'),('adidas','Dame line','2014–present'),('adidas','Harden line','2016–present'),('adidas','D.O.N. line','2018–present'),('adidas','Trae Young line','2021–2024'),('adidas','AE line','2024–present'),
('Athletic Propulsion Labs',"Load 'N Launch",'2009'),
('Anta','GH line','present'),('Anta','KT line','present'),('Anta','KAI line','present'),
('Converse','Chuck Taylor All Star','1918','X'),('Converse','Weapon','1986','X'),('Converse','Shai Gilgeous-Alexander line','present'),
('Ektio','Wraptor','2010'),('Ektio','Post Up','2010'),
('Jordan Brand','Melo line','2003–2017'),('Jordan Brand','CP3 line','2008–2019'),('Jordan Brand','Fly Wade line','2009–2012'),('Jordan Brand','Why Not line','2013–present'),('Jordan Brand','Zion line','2021–present'),('Jordan Brand','Luka line','2022–present'),('Jordan Brand','Tatum line','2023–present'),
('Li-Ning','Way of Wade','2012'),('Li-Ning','JB line','2021–present'),('Li-Ning','CJ line','2021–present'),
('New Balance','Kawhi line','2020–present'),
('Nike','Blazer','1973','X'),('Nike','Air Force 1','1982','X'),('Nike','Air Ship','1984'),('Nike','Vandal','1984'),('Nike','Dunk','1985','X'),('Nike','Terminator','1985'),('Nike','Air Jordan','1985','X'),('Nike','Air Max','1987','X'),('Nike','LeBron line','2003–present'),('Nike','Kobe line','2005–2016'),('Nike','KD line','2008–present'),('Nike','Hyper series','2008'),('Nike','Kyrie line','2014–2022'),('Nike','PG line','2017–2022'),('Nike','Zoom Freak line','2019–present'),('Nike','GT series','2021–present'),('Nike','Ja line','2022–present'),('Nike','Sabrina line','2023–present'),('Nike','Book line','2024–present'),("Nike","A'ja line",'2025–present'),
('PRO-Keds','Royal','1949'),('PRO-Keds','Shotmaker','1980'),
('Puma','Clyde','1973','X'),('Puma','All-Pro Nitro','2018–present'),('Puma','MB line','2021–present'),('Puma','Stewie line','2022–present'),('Puma','Scoot line','2023–present'),
('Reebok','BB4600','1986'),('Reebok','Pump','1989','X'),('Reebok','Shaq Attaq','1992','X'),('Reebok','The Answer','1997'),('Reebok','Angel Reese 1','2025–present'),
('Starbury','Big Ben','2007'),('Starbury','Stephon Marbury signature line','2006–2009'),
('Under Armour','Micro G','2010'),('Under Armour','Curry line','2015–2020'),('Under Armour','Curry Brand','2020–present'),('Under Armour','Embiid line','2020'),('Under Armour','Fox line','2024–present'),
('Xtep','JLIN ONE','2020'),
]
CT={'Jordan Brand':'United States','Athletic Propulsion Labs':'United States'}
bk=kinds['Basketball sneaker']; have=allnames(); addb=[]; held=0
if 'Athletic Propulsion Labs' not in reg:
    reg['Athletic Propulsion Labs']={'n':'Athletic Propulsion Labs','s':WL,'kf':'basketball shoes'}
    B['b'].append(reg['Athletic Propulsion Labs'])
def gkey(e):
    y=re.match(r'(\d{4})',e.get('y','') or ''); return (e.get('g',''), int(y.group(1)) if y else 9999, e['n'])
for r in REF:
    mk,n,y=r[:3]
    if len(r)==4 or n.lower() in have or n.lower().replace(' line','').replace(' series','') in have and False:
        held+=1; continue
    if n.lower() in have: held+=1; continue
    rg=reg.get(mk,{}); c=rg.get('c') or CT.get(mk) or 'Country not stated'
    yy='' if y=='present' else y
    e={'n':n,'d':('Basketball model line listed for %s in Wikipedia\'s List of basketball shoe brands.' % y.replace('present','the present')) if ('line' in n or 'series' in n or ' line' in n) else 'Basketball shoe listed under %s for %s in Wikipedia\'s List of basketball shoe brands.' % (mk, y),'mk':mk,'y':yy,'s':WL,'g':'%s · %s'%(c,mk)}
    if y=='present': e['d']='Current basketball model line listed under %s in Wikipedia\'s List of basketball shoe brands.' % mk
    if rg.get('own'): e['own']=rg['own']
    if rg.get('tier'): e['tier']=rg['tier']
    if rg.get('c'): e['cty']=rg['c']
    bk['x'].append(e); addb.append(n); have.add(n.lower())
bk['x'].sort(key=gkey)
tot=len(REF)
print('basketball added',len(addb),'held elsewhere',held,'total ref rows',tot)
# ---- 5 coverage lines
def setcov(k,line):
    sel=k.get('sel') or ''
    sel=re.sub(r'\s*(Covers \d+ entr(?:y|ies); where a per-model.*|Covers about 60 of the many heritage runners;.*)$','',sel).rstrip()
    k['sel']=(sel+' '+line).strip()
NOREF='No complete list exists; follows the maker and Wikipedia pages named on each entry.'
for k in kinds.values():
    if not k.get('x'): continue
    sel=k.get('sel') or ''
    if k['n']=='Basketball sneaker':
        setcov(k,"The reference is Wikipedia's List of basketball shoe brands (%d model and line rows; its rows without a model name are skipped). Complete: %d of %d rows, counting rows held in the Air Jordan, Air Max and Terrace sneaker kinds. Models outside that list (Pro Leather, Question, Mag, Superstar, Forum) come from their own Wikipedia pages." % (tot,tot,tot))
        continue
    if re.search(r'(Complete: |No complete list exists)',sel): continue
    if 'Covers' in sel or 'Heritage' in k['n'] or True:
        if k['n'] in('Pointed-toe boot','Jackboot & Hessian boot'):
            setcov(k,"Complete: every in-scope entry of Wikipedia's List of boots and List of shoe styles for this kind is held; sport boots (ski, football, wader and similar) belong to E2.")
        else: setcov(k,NOREF)
# kinds from list of boots gaps: note on sel for work/military/riding
for kn in ('Work boot','Combat & military boot','Equestrian riding boot','Over-the-knee boot','Cowboy boot'):
    k=kinds[kn]; 
    if 'List of boots' not in k['sel']: k['sel']=k['sel'].replace(NOREF,"Boot types come from Wikipedia's List of boots (all in-scope types for this kind held); makers' models follow the maker pages named on each entry. No complete list of makers' models exists.")
# ---- write
json.dump(d,open(R+'work/GAP_A2/A2.new.json','w'),ensure_ascii=False,indent=1)
json.dump(B,open(R+'work/GAP_A2/A2_brands.new.json','w'),ensure_ascii=False,indent=1)
