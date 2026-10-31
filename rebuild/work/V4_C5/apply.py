import json,os,copy
P='/home/user/Possession-Taxonomy/rebuild/out/C5.json'
d=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/V4_C5/bak/C5.json'))
K={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
removed_m=sum(len(k.get('m',[])) for k in K.values()); removed_r=sum(len(k.get('r',[])) for k in K.values())
for k in K.values():
    k.pop('m',None); k.pop('r',None)
W='https://en.wikipedia.org/wiki/'
def E(n,mk,y,s,dd,v=None,a='',role=None):
    e={'n':n,'a':a,'d':dd,'mk':mk,'y':y,'s':s}
    if v: e['v']=[{'n':a_,'mk':mk,'y':b_,'d':c_} for a_,b_,c_ in v]
    if role: e['role']=role
    return e
def has(k,n): return any(x['n'].lower()==n.lower() for x in K[k].get('x',[]))
def add(kn,e):
    if not has(kn,e['n']): K[kn].setdefault('x',[]).append(e)
def drop(kn,names=None,keep=None):
    if names is None: K[kn]['x']=[x for x in K[kn].get('x',[]) if keep and x['n'] in keep]
    else: K[kn]['x']=[x for x in K[kn].get('x',[]) if x['n'] not in names]
def setrole(kn,n,r):
    for x in K[kn].get('x',[]):
        if x['n']==n: x['role']=r
def fix(kn,n,**kw):
    for x in K[kn].get('x',[]): 
        if x['n']==n: x.update(kw)
# ---- commodity kinds: icon rule only
drop('Pen refill',[x['n'] for x in K['Pen refill']['x']])
drop('Multi pen',[x['n'] for x in K['Multi pen']['x']])
drop('Pencil sharpener',[x['n'] for x in K['Pencil sharpener']['x']])
drop('Self-inking stamp',[x['n'] for x in K['Self-inking stamp']['x']])
drop('Name seal',[x['n'] for x in K['Name seal']['x']])
drop('Brush pen',[x['n'] for x in K['Brush pen']['x']])
drop('Dry-erase marker',[x['n'] for x in K['Dry-erase marker']['x']])
drop('Fineliner',keep=['Pentel Sign Pen']); setrole('Fineliner','Pentel Sign Pen','origin')
drop('Highlighter',keep=["Carter's Hi-Liter"]); setrole('Highlighter',"Carter's Hi-Liter",'origin')
drop('Permanent marker',keep=['Magic Marker']); setrole('Permanent marker','Magic Marker','origin')
drop('Gel pen',keep=['Sakura Ball Sign / Gelly Roll']); setrole('Gel pen','Sakura Ball Sign / Gelly Roll','origin')
drop('Rollerball pen',keep=['Ohto ceramic rollerball']); setrole('Rollerball pen','Ohto ceramic rollerball','origin')
drop('Ballpoint pen',keep=['Bic Cristal','Parker Jotter','Fisher Space Pen']); setrole('Ballpoint pen','Bic Cristal','landmark')
drop('Legal pad',keep=['Silver City Writing Tablet']); setrole('Legal pad','Silver City Writing Tablet','origin')
for kn in ('Ballpoint pen','Gel pen','Rollerball pen','Multi pen','Pen refill','Fineliner','Highlighter','Permanent marker','Dry-erase marker','Brush pen','Pencil sharpener','Self-inking stamp','Name seal'):
    pass
# ---- fountain pens
ctry={'Lamy':'Germany','Kaweco':'Germany','Pelikan':'Germany','Montblanc':'Germany','Graf von Faber-Castell':'Germany','OMAS':'Italy','Aurora':'Italy','Visconti':'Italy','TWSBI':'Taiwan','Pilot':'Japan','Platinum':'Japan','Sailor':'Japan','Namiki':'Japan','Nakaya':'Japan','Danitrio':'Japan','Pentel':'Japan','Parker':'United States','Cross':'United States','Sheaffer':'United States','Conklin':'United States','Esterbrook':'United States','Mabie Todd':'United States','Waterman':'France','Jinhao':'China','Wing Sung':'China','Speedball':'United States','Tachikawa':'Japan','Gillott':'United Kingdom','William Mitchell':'United Kingdom','Brause':'Germany','Leonardt':'United Kingdom','Hunt':'United States','JoWo':'Germany','Bock':'Germany','Schmidt':'Germany'}
add('Cartridge-converter fountain pen',E('Parker Sonnet','Parker','1993',W+'Parker_Pen_Company','Mid-range Parker cartridge-converter pen introduced in 1993.'))
add('Cartridge-converter fountain pen',E('Parker Vector','Parker','1986',W+'Parker_Pen_Company','Parker everyday pen from 1986, developed from the FP1 fountain pen and RB1 rollerball.',v=[('FP1','1984','fountain-pen precursor'),('RB1','1981','rollerball precursor')]))
add('Cartridge-converter fountain pen',E('Waterman C/F','Waterman','1953',W+'Waterman_S._A.','Waterman cartridge-filled pen of 1953.'))
add('Cartridge-converter fountain pen',E('Waterman Carène','Waterman','',W+'Waterman_S._A.','Waterman line named in the maker article without a year.'))
add('Cartridge-converter fountain pen',E('Waterman Expert','Waterman','',W+'Waterman_S._A.','Waterman line named in the maker article without a year.'))
add('Cartridge-converter fountain pen',E('Waterman Hémisphère','Waterman','',W+'Waterman_S._A.','Waterman line named in the maker article without a year.'))
add('Cartridge-converter fountain pen',E('Waterman Le Man 100','Waterman','1983',W+'Waterman_S._A.','Waterman pen of 1983.'))
fix('Cartridge-converter fountain pen','Aurora Duo-Cart',d_=0) if False else None
# Parker 45/75/61/180 etc stay; add Parker Duofold already; Jotter fountain pen = ballpoint entry
add('Sac-filling fountain pen',E('Parker Jointless','Parker','1899',W+'Parker_Pen_Company','Parker eyedropper-era pen; also listed as an eyedropper pen.')) if False else None
add('Cartridge-converter fountain pen',E('Parker 25','Parker','1975',W+'Parker_Pen_Company','Parker pen of 1975.'))
add('Cartridge-converter fountain pen',E('Parker 95','Parker','1988',W+'Parker_Pen_Company','Parker pen of 1988.'))
add('Retractable-nib fountain pen',E('Parker Jack Knife Safety','Parker','1909',W+'Parker_Pen_Company','Parker safety pen of 1909.'))
# roles
setrole('Sac-filling fountain pen','Parker 51','landmark'); setrole('Piston-filling fountain pen','Lamy 2000','landmark'); setrole('Retractable-nib fountain pen','Pilot Capless','landmark')
# loose-model promotions into versions
for x in K['Piston-filling fountain pen']['x']:
    if x['n']=='Lamy 2000':
        x.setdefault('v',[]).append({'n':'Lamy 2000 ballpoint','mk':'Lamy','y':'1966','d':'ballpoint of the same family'})
for kn in ['Cartridge-converter fountain pen','Piston-filling fountain pen','Vacuum and plunger-filling fountain pen','Sac-filling fountain pen','Eyedropper fountain pen','Retractable-nib fountain pen','Calligraphy fountain pen']:
    k=K[kn]
    for x in k['x']: x['g']=ctry.get(x.get('mk'),'Other makers')
    k['x'].sort(key=lambda x:(x['g']=='Other makers',x['g'],x.get('mk') or '',x.get('y') or '9999',x['n']))
    k['nl']='One entry is a fountain-pen model line sold under its own name; sizes, editions and revisions are versions.'
    k['xg']='by maker country, then maker'
    k['sel']='Model lines named by the maker histories on Wikipedia (Parker, Lamy, Waterman, Aurora, Montblanc, Pelikan) and by maker and retailer pages cited on each entry; no single complete list of fountain-pen lines exists. Covers {} lines; the many other lines of these makers are not listed.'.format(len(k['x']))
# ---- ink
k=K['Fountain pen ink']
for x in k['x']: x['g']=ctry.get(x.get('mk'),'Other makers') if x.get('mk') not in ('J. Herbin','Diamine','Noodler\'s','De Atramentis','Rohrer & Klingner') else {'J. Herbin':'France','Diamine':'United Kingdom',"Noodler's":'United States','De Atramentis':'Germany','Rohrer & Klingner':'Germany'}[x['mk']]
k['x'].sort(key=lambda x:(x['g'],x.get('mk') or '',x['n']))
k['nl']='One entry is a maker\'s bottled-ink line sold under its own name; its colours are versions only where the maker or retailer page lists them.'
k['xg']='by maker country, then maker'
k['sel']='Ink lines of the makers cited on each entry (maker and retailer pages); no complete register of ink lines exists. Covers {} lines.'.format(len(k['x']))
# nibs, dip pens
for kn in ['Dip pen nib','Dip pen holder','Glass pen','Fountain pen nib']:
    kk=K[kn]; kk['nl']='One entry is a nib, holder or nib unit sold under its own name; widths and finishes are versions.'
    for x in kk['x']: x['g']=ctry.get(x.get('mk'),'Other makers')
    kk['x'].sort(key=lambda x:(x['g'],x.get('mk') or '',x['n'])); kk['xg']='by maker country'
    kk['sel']='Makers named on the guide pages cited on each entry. Covers {} lines; no complete register of nibs exists.'.format(len(kk['x']))
# East Asian calligraphy tools
for kn in ['Calligraphy brush','Ink stick','Inkstone','Calligraphy paper']:
    kk=K[kn]; kk['nl']='One entry is a regional tradition of the tool, named by its place of making; workshop makers and grades are versions.'
    kk['xg']='by region'; kk['sel']='Traditions named in the Four Treasures of the Study article and the cited Japanese craft pages. Covers {} traditions; the scripts themselves belong to visual art (see Visual Entertainment).'.format(len(kk['x']))
    for x in kk['x']: x['g']='China' if any(w in x['n'] for w in ('Huzhou','Hui','Duan','She','Taohe','Chengni','Xuan')) else ('Korea' if x['n']=='Hanji' else 'Japan')
    kk['x'].sort(key=lambda x:(x['g'],x['n']))
# ---- pencils and notebooks
cm={'Koh-i-Noor Hardtmuth':'Czech Republic','Faber-Castell':'Germany','Eberhard Faber':'United States','Dixon Ticonderoga':'United States','Mitsubishi Pencil (Uni)':'Japan','Tombow':'Japan','Staedtler':'Germany','Sampson Mordan':'United Kingdom','Pentel':'Japan','Rotring':'Germany','Zebra':'Japan','Pilot':'Japan','Caran d\'Ache':'Switzerland','Eversharp':'United States','':'Other'}
setrole('Wooden pencil','Blackwing 602','landmark')
for kn,sel in [('Wooden pencil','Pencil lines named by the Wikipedia articles Pencil, Blackwing 602 and Dixon Ticonderoga and by the maker pages cited on each entry. Covers {} lines of the many in production.'),('Mechanical pencil','Lines named by the Wikipedia article Mechanical pencil and the review pages cited on each entry. Covers {} lines.'),('Lead holder','Lines named by the Wikipedia article Mechanical pencil and the review pages cited. Covers {} lines.')]:
    kk=K[kn]; kk['nl']='One entry is a pencil line sold under its own name; grades, sizes and revisions are versions.'
    for x in kk['x']: x['g']=cm.get(x.get('mk'),'Other')
    kk['x'].sort(key=lambda x:(x['g'],x.get('mk') or '',x.get('y') or '9999',x['n'])); kk['xg']='by maker country, then maker'; kk['sel']=sel.format(len(kk['x']))
nm={'Moleskine':'Italy','Leuchtturm1917':'Germany','Clairefontaine':'France','Midori':'Japan','KOKUYO':'Japan','Maruman':'Japan','Tomoegawa':'Japan','STALOGY':'Japan','Apica':'Japan','Baron Fig':'United States','Field Notes':'United States','Rite in the Rain':'United States','TRAVELER\'S COMPANY':'Japan','Filofax':'United Kingdom','Atoma':'Israel','Hobonichi':'Japan','Rhodia':'France','Crane':'United States','G. Lalo':'France','':'Other'}
setrole('Notebook','Moleskine notebook','landmark')
setrole('Diary or planner','Hobonichi Techo','landmark')
for kn in ['Notebook','Reporter\'s notebook','Lab & field notebook','Refillable notebook system','Diary or planner','Memo pad','Letter-writing paper set','Legal pad']:
    kk=K[kn]; kk['nl']='One entry is a notebook, planner or paper line sold under its own name; formats, rulings and yearly editions are versions.'
    for x in kk['x']: x['g']=nm.get(x.get('mk'),'Other')
    kk['x'].sort(key=lambda x:(x['g'],x.get('mk') or '',x.get('y') or '9999',x['n'])); kk['xg']='by maker country, then maker'
    kk['sel']='Lines named by the Wikipedia articles and maker or review pages cited on each entry; no complete register exists. Covers {} lines.'.format(len(kk['x']))
# ---- calculators and typewriters
HP='https://en.wikipedia.org/wiki/Hewlett-Packard_calculators'; GR='https://en.wikipedia.org/wiki/Graphing_calculator'
def hp(kn,items):
    for n,y in items: add(kn,E(n,'HP',y,HP,'HP calculator listed with its year on the Wikipedia list of HP calculators.'))
hp('Vintage electronic calculator',[('HP-80','1973'),('HP-45','1973'),('HP-21','1975'),('HP-25','1975'),('HP-55','1975'),('HP-67','1976'),('HP-97','1977'),('HP-41 series','1979')])
hp('Scientific calculator',[('HP-11C','1981'),('HP-15C','1982'),('HP-16C','1982'),('HP-10C','1982'),('HP-42S','1988'),('HP-32S','1988')])
hp('Financial calculator',[('HP-18C','1986'),('HP-10B','1987'),('HP-17B','1988'),('HP-19B','1988'),('HP-14B','1988')])
hp('Graphing calculator',[('HP-28S','1988'),('HP 48 series','1990'),('HP 38G','1995'),('HP 49/50 series','1999'),('HP 39G','2000')])
setrole('Vintage electronic calculator','HP-35','origin')
for n,y in [('TI-81','c. 1990'),('TI-83','c. 1996'),('TI-92','c. 1996'),('TI-89 series',''),('Voyage 200','')]: add('Graphing calculator',E(n,'Texas Instruments',y,GR,'Texas Instruments graphing calculator named on the Wikipedia article Graphing calculator.'))
for n,y in [('Casio fx-7000G','1985'),('Casio fx-9860G series','')]: add('Graphing calculator',E(n,'Casio',y,GR,'Casio graphing calculator named on the Wikipedia article Graphing calculator.'))
for x in K['Graphing calculator']['x']:
    if x['n']=='TI-83': x.setdefault('v',[]).append({'n':'TI-83 Plus','mk':'Texas Instruments','y':'','d':'successor with flash memory'})
    if x['n']=='TI-92': x.setdefault('v',[]).append({'n':'TI-92 Plus','mk':'Texas Instruments','y':'','d':'upgraded model'})
OL='https://en.wikipedia.org/wiki/Olivetti_typewriters'
for n,y in [('Olivetti M1','1911'),('Olivetti M20','1920'),('Olivetti M40','1930'),('Olivetti MP1','1932'),('Olivetti Studio 42','1935'),('Olivetti Lexikon 80','1948'),('Olivetti Studio 44','1952'),('Olivetti Diaspron 82','1959'),('Olivetti Lettera 32','1963'),('Olivetti Studio 45','1967'),('Olivetti Lettera 25','1972'),('Olivetti Lettera 35','1972'),('Olivetti Studio 46','1973'),('Olivetti Lettera 36','1974'),('Olivetti Lexikon 82','1976'),('Olivetti Lettera 10','1979')]:
    add('Manual typewriter',E(n,'Olivetti',y,OL,'Olivetti manual typewriter listed with its year in the Wikipedia article Olivetti typewriters.'))
for x in K['Manual typewriter']['x']:
    if x['n']=='Olivetti Lexikon 80': x.setdefault('v',[]).append({'n':'Lexikon 80e','mk':'Olivetti','y':'','d':'later model'})
add('Manual typewriter',E('Olivetti Lexikon 90 series','Olivetti','1972',OL,'Office machines of 1972 sold as Lexikon 90, 92, 93c and 94c.',v=[('Lexikon 90','1972','base model'),('Lexikon 92','1972',''),('Lexikon 93c','1972',''),('Lexikon 94c','1972','')]))
TY='https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Typewriters&cmlimit=500&format=json'
for n,mk in [('Royal 10','Royal'),('Royal Futura','Royal'),('Erika','Erika'),('Remington-Rand Quiet-Riter','Remington'),('Oliver Typewriter','Oliver Typewriter Company'),('Imperial typewriter','Imperial Typewriter Company'),('Ford Typewriter','Ford')]:
    add('Manual typewriter',E(n,mk,'',TY,'Typewriter named in the Wikipedia typewriter category.'))
for n,y in [('Olivetti Tekne 1','1962'),('Olivetti Praxis 48','1964'),('Olivetti Dora','1965'),('Olivetti Lettera DL','1965'),('Olivetti Editor 5','1969')]:
    add('Electric typewriter',E(n,'Olivetti',y,OL,'Olivetti electric typewriter listed with its year in the Wikipedia article Olivetti typewriters.'))
fix('Electronic typewriter','Olivetti Tes 501',y='1978')
add('Electronic typewriter',E('Olivetti TES 401','Olivetti','1978',OL,'Electronic typewriter of 1978.'))
add('Electronic typewriter',E('Olivetti ET series','Olivetti','',OL,'Family of electronic typewriters, ET 109 to ET 2500 and ET Compact.',v=[('ET 121','',''),('ET 201','',''),('ET 2000','',''),('ET Compact 50','',''),('ET Compact 70','','')]))
add('Electronic typewriter',E('Olivetti ETV series','Olivetti','1982',OL,'Family of electronic typewriters with display, ETV 300 of 1982 to ETV 5000 of 1988.',v=[('ETV 300','1982',''),('ETV 350','1984',''),('ETV 500','1986',''),('ETV 2900','1988','')]))
setrole('Manual typewriter','Sholes and Glidden','origin'); setrole('Manual typewriter','Olivetti Lettera 22','landmark'); setrole('Manual typewriter','Olivetti Valentine','landmark'); setrole('Electric typewriter','IBM Selectric','landmark')
setrole('Manual typewriter','Underwood No. 5','landmark')
for kn,sel in [('Manual typewriter','Wikipedia articles Olivetti typewriters (manual models) and the Typewriter category, plus the museum and collector pages cited on each entry. Covers {} models; the many other makers and models are not listed.'),('Electric typewriter','Wikipedia articles Olivetti typewriters and IBM Selectric. Covers {} models.'),('Electronic typewriter','Wikipedia article Olivetti typewriters. Covers {} entries (the ET and ETV families are shown as series).'),('Scientific calculator','Wikipedia article Hewlett-Packard calculators (HP RPN scientific models) and the pages cited on each entry. Covers {} lines.'),('Graphing calculator','Wikipedia articles Graphing calculator and Hewlett-Packard calculators. Covers {} lines.'),('Financial calculator','Wikipedia article Hewlett-Packard calculators and the cited pages. Covers {} lines.'),('Vintage electronic calculator','Wikipedia article Hewlett-Packard calculators (1970s models) and the pages cited. Covers {} lines.')]:
    kk=K[kn]; kk['nl']='One entry is a model line sold under its own name; revisions and regional variants are versions.'
    kk['x'].sort(key=lambda x:(x.get('mk') or '',x.get('y') or '9999',x['n'])); kk['xg']='by maker'
    for x in kk['x']: x['g']=x.get('mk') or 'Other'
    kk['sel']=sel.format(len(kk['x']))
for kn in ['Slide rule','Mechanical calculator','Abacus']:
    kk=K[kn]; kk['nl']='One entry is a model line or regional form sold or made under its own name; sizes and scales are versions.'
    for x in kk['x']: x['g']=x.get('mk') or 'Other'
    kk['x'].sort(key=lambda x:(x['g'],x.get('y') or '9999',x['n'])); kk['xg']='by maker'
    kk['sel']='Lines named by the museum and Wikipedia pages cited on each entry. Covers {} lines; there is no complete register.'.format(len(kk['x']))
# other kinds with entries: generic nl/sel
for k in K.values():
    if k.get('x') and 'nl' not in k:
        k['nl']='One entry is a named line sold under its own name; sizes and revisions are versions.'
        k['sel']='Lines named by the pages cited on each entry. Covers {} lines; no complete register exists.'.format(len(k['x']))
        k['xg']='by maker'
        for x in k['x']: x['g']=x.get('mk') or 'Other'
        k['x'].sort(key=lambda x:(x['g'],x.get('y') or '9999',x['n']))
# commodity kinds with no entries left: nothing. Rename Name seal etc untouched.
# market panel
for dp in d['depts']:
    if dp['n']=='Everyday pens & pencils':
        dp['ms']=[{'mkt':'Global writing instruments','who':'Newell Brands','share':'over 7.0 %','yr':2025,'s':'https://gminsights.com/industry-analysis/writing-instruments-market','note':'share of the market, as the page states'},
                  {'mkt':'Global writing instruments','who':'Shanghai M&G Stationery','share':'6.5 %','yr':2025,'s':'https://gminsights.com/industry-analysis/writing-instruments-market','note':'share of the market'},
                  {'mkt':'Global writing instruments','who':'Pilot Corporation','share':'4.2 %','yr':2025,'s':'https://gminsights.com/industry-analysis/writing-instruments-market','note':'share of the market'},
                  {'mkt':'Global writing instruments','who':'Newell Brands, Shanghai M&G, Pilot, BIC Group and Faber-Castell together','share':'24.3 %','yr':2025,'s':'https://gminsights.com/industry-analysis/writing-instruments-market','note':'top five combined; the page gives no separate share for BIC or Faber-Castell'}]
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
print('removed m',removed_m,'r',removed_r)
