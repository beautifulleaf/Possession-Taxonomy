import json, re
R='/home/user/Possession-Taxonomy/rebuild/'
P=json.load(open(R+'work/V4_E3_ORCH/ORCH.pass1.json'))
o,f,c=P['depts']
W='https://en.wikipedia.org/wiki/'
S_STR=W+'List_of_Stradivarius_instruments'; S_FREE=W+'Free_reed_aerophone'; S_BRASS=W+'Brass_instrument'
S_GUA=W+'Giuseppe_Guarneri'; S_AM=W+'Amati'
def norm(s): return re.sub(r"[\s'_\[\]\"‘’()]+",' ',s.lower()).strip()
def kind(d,n):
    for s in d['s']:
        for k in s['k']:
            if k['n']==n: return k
    raise KeyError(n)
def ent(k,n):
    for e in k['x']:
        if e['n']==n: return e
    raise KeyError(n)
def ysort(v):
    m=re.search(r'\d{4}',v['y']); return (int(m.group()) if m else 9999, v['n'])
rows=[l.split('|') for l in open(R+'work/V4_E3_ORCH/rows_strad.txt',encoding='utf-8').read().strip().split('\n')]
cnt={}
for n,y,t in rows: cnt[t]=cnt.get(t,0)+1
def yy(y): return '' if y=='not given' else y
MK='Antonio Stradivari'
def reset(e,typ):
    e['v']=[v for v in e.get('v',[]) if not (v.get('mk')==MK and v.get('d')==typ)]
def addv(e,typ):
    have={norm(v['n'])+v['y'] for v in e['v']}
    for n,y,t in rows:
        if t==typ and norm(n)+yy(y) not in have:
            e['v'].append({'n':n,'mk':MK,'y':yy(y),'d':typ})
    e['v'].sort(key=ysort)
violin=kind(o,'Violin'); viola=kind(o,'Viola'); cello=kind(o,'Cello')
st=ent(violin,'Antonio Stradivari'); reset(st,'violin'); addv(st,'violin')
sv=ent(viola,'Stradivari viola'); reset(sv,'viola'); addv(sv,'viola')
sc=ent(cello,'Stradivari cello'); reset(sc,'cello'); addv(sc,'cello')
for e in (st,sv,sc): e['s']=S_STR
# guarneri
g=ent(violin,'Giuseppe Guarneri del Gesù')
g['v']=[v for v in g['v'] if v.get('d')!='violin']
GN=[("Il Cannone Guarnerius","1743","used by Paganini; now in the City Hall of Genoa"),("Lord Wilton","1742","once owned by Yehudi Menuhin"),("Vieuxtemps Guarneri","1741","once owned by Henri Vieuxtemps"),("Ole Bull","1744","now at the Chimei Museum; believed to be his last work"),("The Cathedral","1731","played by George Enescu"),("King Joseph","1737","reportedly the first del Gesù to go to America (1868)"),("The King","1735","now in the Croatian Academy of Sciences and Arts"),("Lady Stretton","1728–29",""),("Lord Red","1727",""),("Lord Shaftsbury","c. 1730–31",""),("Lord Coke","1744",""),("Lord Dunmore (Gillot)","c. 1732",""),("Baron Heath","1729",""),("Baron Heath (second instrument)","1743",""),("Diable","1734",""),("Prince Doria","1733–34","bought by the Doria family in 1860"),("Prince of Orange","1744","displayed by the Prague National Museum"),("Mary Portman","1735",""),("Titan","c. 1741",""),("Castelbarco-Tarisio","c. 1732","now at the Chimei Museum"),("Lo Stauffer","c. 1731",""),("Lo Stauffer (Cremona)","1734","displayed by the City of Cremona"),("Chang","1717","bought by Sarah Chang from Isaac Stern")]
have={norm(v['n']) for v in g['v']}
for n,y,d in GN:
    if norm(n) in have: continue
    g['v'].append({'n':n,'mk':'Giuseppe Guarneri del Gesù','y':y,'d':d}); have.add(norm(n))
g['v'].sort(key=ysort); g['s']=S_GUA
# amati
a=ent(violin,'Amati'); a['v']=[v for v in a['v'] if v.get('d')!='named Amati instrument on the Amati page']
AM=[("The Witten","Andrea Amati","c. 1560",""),("The IX Charles","Andrea Amati","c. 1560",""),("The ex Collis","Andrea Amati","c. 1560",""),("The ex Wahl","Andrea Amati","c. 1568",""),("The ex Herrmann","Andrea Amati's school","c. 1620",""),("The Henry IV","Girolamo Amati","c. 1590",""),("The Trampler","Antonio & Girolamo Amati","c. 1580–90",""),("The Stauffer","Antonio & Girolamo Amati","c. 1615",""),("The Zukerman, The Kashkashian","Antonio & Girolamo Amati","c. 1617",""),("The Medici, The Hamma","Antonio & Girolamo Amati","c. 1619",""),("The ex Wittgenstein","Antonio & Girolamo Amati","c. 1620",""),("The ex Vieuxtemps","Nicolò Amati","c. 1663","held by the National Museum of American History"),("The Berkitz, The Romanov","Nicolò Amati","c. 1677",""),("The ex Waters","Nicolò Amati","c. 1703",""),("The ex Francais","Girolamo Amati II","1708","")]
have={norm(v['n']) for v in a['v']}
for n,m,y,d in AM:
    if norm(n) in have: continue
    a['v'].append({'n':n,'mk':m,'y':y,'d':d or 'Amati instrument named on the Amati page'})
a['s']=S_AM
av=ent(viola,'Amati viola')
for n,m,y in [("The Stanley Solomon Tenore","Andrea Amati","c. 1536"),("From the Charles IX Set","Andrea Amati","c. 1564"),("The Violetta","Andrea Amati","c. 1570"),("The Crocifisso (Viola Medicea)","Antonio & Girolamo Amati","c. 1594")]:
    if norm(n) not in {norm(v['n']) for v in av['v']}: av['v'].append({'n':n,'mk':m,'y':y,'d':'named on the Amati page'})
ac=ent(cello,'Amati cello')
if norm('The King') not in {norm(v['n']) for v in ac['v']}: ac['v'].append({'n':'The King','mk':'Andrea Amati','y':'c. 1538–1545','d':'described as the oldest extant cello; National Music Museum, University of South Dakota'})
db=kind(o,'Double bass')
db['x'].append({'n':'Hieronymus II double bass','a':'','d':'Double bass by Girolamo Amati II, 1680, held by the National Music Museum, University of South Dakota.','mk':'Girolamo Amati','y':'1680','s':S_AM,'v':[],'g':'Amati'})
# harp, bow
hk=kind(o,'Harp'); hk['x'].append({'n':'Stradivari arpetta','a':'','d':'The one harp the Stradivarius list names.','mk':MK,'y':'','s':S_STR,'v':[{'n':'arpetta','mk':MK,'y':'','d':'harp'}],'g':MK})
bk=kind(o,'Bow'); bk['x'].append({'n':'King Charles IV Violin Bow','a':'','d':'The one bow the Stradivarius list names.','mk':MK,'y':'','s':S_STR,'v':[],'g':MK})
# mandolin entry in folk
mk_=kind(f,'Mandolin'); me=ent(mk_,'Antonio Stradivari mandolins')
me['v']=[{'n':'Cutler-Challen Choral Mandolino','mk':MK,'y':'1680','d':'mandolin'},{'n':'Mandolino Coristo','mk':MK,'y':'c. 1706','d':'mandolin'}]
me['d']='Mandolins made in the Stradivari workshop; the list names two.'; me['y']='1680–c. 1706'; me['s']=S_STR
# brass family members into orchestral kinds
FAM={'Trumpet':['Bass trumpet','Contrabass trumpet','Fanfare trumpet','Firebird trumpet','Flumpet','Piccolo trumpet','Pocket trumpet','Baroque trumpet','Slide trumpet','Keyed trumpet','Clarion'],
'Cornet':['Soprano cornet'],'Flugelhorn':['Fiscorn','Kuhlohorn'],'French horn':['Vienna horn','Mellophone'],
'Trombone':['Alto trombone','Bass trombone','Contrabass trombone','Soprano trombone','Valve trombone','Superbone','Trombonium','Buccin'],
'Baritone horn':['Tenor horn (alto horn)','Saxhorn','Marching baritone horn','Saxotromba','Saxtuba','Sudrophone'],'Euphonium':['Double bell euphonium','Marching euphonium'],
'Tuba':['Subcontrabass tuba','Helicon','Soprano helicon','Sousaphone','Cimbasso','Wagner tuba'],'Cornett':['Cornettino','Mute cornett','Tenor cornett']}
def mk_entry(n,s,reg='Family members',d=None):
    return {'n':n,'a':'','d':d or f'Named on the Brass instrument page.','mk':'','y':'','s':s,'v':[],'g':reg}
for kn,names in FAM.items():
    k=kind(o,kn); k.setdefault('x',[]); have={norm(e['n']) for e in k['x']}
    for n in names:
        if norm(n) not in have: k['x'].append(mk_entry(n,S_BRASS))
# folk regions
REG={}
def setr(r,names):
    for n in names.split(';'): REG[norm(n.strip())]=r
setr('Japan','Koto;Shō'); setr('Gabon, Cameroun, Guinea','Mvet'); setr('Madagascar','Valiha'); setr('Korea','Ajaeng;Gayageum'); setr('Vietnam','Đàn tranh;Đàn tính')
setr('China','Guqin;Guzheng;Yangqin;Bawu;Hulusi;Sheng;Sanxian'); setr('Benin','Adjalin'); setr('Indonesia','Kacapi'); setr('Finland, Karelia','Kantele')
setr('Central and Eastern Europe','Cimbalom'); setr('United States','Harpejji;Marxophone'); setr('Germany','Pantalon;Martinshorn'); setr('Greece','Psaltery'); setr('Middle East','Qanun')
setr('Iran and India','Santur'); setr('India','Shahi baaja;Swarmandal;Indian harmonium'); setr('Basque Country','Tambourin de Béarn'); setr('Inuit','Tautirut')
setr('Persia','Kamancheh'); setr('Mongolia','Morin khuur'); setr('Japan','Sanshin;Shamisen'); setr('Laos','Khene'); setr('Australia','Didgeridoo'); setr('Russia','Vladimirskiy rozhok')
NS='Region not stated'
LISTNAME={W+'List_of_musical_instruments_by_Hornbostel%E2%80%93Sachs_number:_32':"List of musical instruments by Hornbostel–Sachs number: 32",
W+'List_of_musical_instruments_by_Hornbostel%E2%80%93Sachs_number:_31':"List of musical instruments by Hornbostel–Sachs number: 31",
W+'List_of_musical_instruments_by_Hornbostel%E2%80%93Sachs_number:_421':"List of musical instruments by Hornbostel–Sachs number: 421",
W+'List_of_aerophones_by_Hornbostel%E2%80%93Sachs_number':"List of aerophones by Hornbostel–Sachs number",
W+'Reed_aerophone':"Reed aerophone article", W+'List_of_chordophones_by_Hornbostel%E2%80%93Sachs_number':"List of chordophones by Hornbostel–Sachs number",S_FREE:'Free reed aerophone article',S_BRASS:'Brass instrument article'}
# new folk additions
def add(kn,names,src,shelf=None,d=None):
    try: k=kind(f,kn)
    except KeyError:
        k={'n':kn,'a':'','d':d,'s':src,'x':[],'nl':'One entry is an instrument named in the reference; regional variants are versions.','xg':'country or region as the page states'}
        next(s for s in f['s'] if s['n']==shelf)['k'].append(k)
    have={norm(e['n']) for e in k['x']}
    for n in names:
        if norm(n) not in have:
            k['x'].append({'n':n,'a':'','d':'','mk':'','y':'','s':src,'v':[],'g':NS}); have.add(norm(n))
add('Mouth organs',['Khene','Lusheng','Mangtong','Saenghwang','Shō','Yu','Gourd mouth organ'],S_FREE,'Accordions & free reeds','Mouth-blown free-reed organs with pipes in a wind chest, named on the free reed aerophone page; the sheng has its own kind.')
add('Reed organs',['Pump organ','Physharmonica','Organetto','Guide-chant','Orthotonophonium'],S_FREE,'Accordions & free reeds','Free-reed organs and keyboards worked by bellows, named on the free reed aerophone page; the harmonium has its own kind.')
add('Blown keyed free reeds',['Claviola','Couesnophone','Harmoneon','Hornophone','Triola'],S_FREE,'Accordions & free reeds','Mouth-blown keyboard free-reed instruments, named on the free reed aerophone page; the melodica has its own kind.')
add('Diatonic harmonica',['Richter-tuned harmonica','Tremolo harmonica'],S_FREE)
add('Free-reed pipes',['Sneng'],S_FREE) if False else None
add('Natural horns & trumpets',['Alphorn','Lur','Carnyx','Buccina','Cornu','Nabal','Nyele','Sringa','Tibetan horn','Wazza','Vuvuzela','Vladimirskiy rozhok','Post horn','Dord','Natural horn','Keyed bugle','Contrabass bugle','Bazooka','Jazzophone'],S_BRASS)
add('Stringed novelties',[],S_32:=W+'x') if False else None
# regions and neutral descriptions
LISTSRC=set(LISTNAME)
for sh in f['s']:
    for k in sh['k']:
        for e in k.get('x',[]):
            e['g']=REG.get(norm(e['n']),NS)
            e['x_']=0
            if e['s'] in LISTSRC and not e.get('mk'):
                reg=e['g']
                e['d']=f"Instrument named in Wikipedia's {LISTNAME[e['s']]}"+('' if reg==NS else f"; the page places it in {reg}")+'.'
            e.pop('x_',None)
        if k.get('x'): k['x'].sort(key=lambda e:(e['g']==NS,e['g'],e['n']))
# nl/sel for all kinds with x lacking
for d in (o,f):
    for sh in d['s']:
        for k in sh['k']:
            if k.get('x'):
                k.setdefault('nl','One entry is an instrument type, maker or model line named on a fetched page; variants are versions.')
                k.setdefault('xg','maker, school or family')
# coverage lines
def strip_cov(k):
    k['sel']=re.sub(r'\s*(Covers|Complete:)[^.]*(\.[^.]*)?$','',k.get('sel','')).strip()
nviol=cnt['violin'];nvla=cnt['viola'];nvc=cnt['cello']
violin['sel']=("Follows Wikipedia's List of Stradivarius instruments, read in three 100,000-character WebFetch windows to the end of the page, and the Guarneri del Gesù and Amati pages for their named instruments; Stainer and Vuillaume have no instrument list. "
  f"Covers {nviol} Stradivari violins, as many as the page summary returned; the summary may have dropped rows.")
viola['sel']=f"Follows Wikipedia's List of Stradivarius instruments and the Amati page. Covers {nvla} Stradivari violas and 4 Amati violas from those pages."
cello['sel']=f"Follows Wikipedia's List of Stradivarius instruments and the Amati page. Covers {nvc} Stradivari cellos and the Amati 'King' from those pages."
for sh in f['s']:
    for k in sh['k']:
        if not k.get('x'): continue
        n=len(k['x'])
        srcs=sorted({LISTNAME[e['s']] for e in k['x'] if e['s'] in LISTNAME})
        if srcs:
            k['sel']=("Follows Wikipedia's "+'; '.join(srcs)+f". Covers {n} entries, every row the page extract returned for this family; the pages were read by extraction, so some rows may be missing. Region labels are the ones the pages state; otherwise 'Region not stated'.")
        else:
            k['sel']=f"Follows the pages cited on each entry; makers appear only where the page calls the model or system defining. Covers {n} entries. Region labels come from fetched pages only; otherwise 'Region not stated'."
for sh in o['s']:
    for k in sh['k']:
        if k['n'] in ('Trumpet','Cornet','Flugelhorn','French horn','Trombone','Baritone horn','Euphonium','Tuba','Cornett'):
            k['sel']=(k.get('sel','').strip()+" Family members follow the Brass instrument article's list; "+f"covers {len(k['x'])} entries.").strip()
f['note']='Shelf by sound source → kind by instrument → entry, sectioned by the country or region a fetched page states (otherwise Region not stated).'
json.dump(P,open(R+'out/E3_parts/ORCH.json','w'),ensure_ascii=False,indent=0)
print(cnt, sum(len(k.get('x',[])) for d in (o,f) for s in d['s'] for k in s['k']))
