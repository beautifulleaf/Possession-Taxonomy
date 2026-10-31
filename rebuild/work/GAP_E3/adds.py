import json,os,re
P='/home/user/Possession-Taxonomy/rebuild/out/E3.json'
d=json.load(open(P))
kinds={k['n']:k for dp in d['depts'] for sh in dp['s'] for k in sh['k']}
W='https://en.wikipedia.org/wiki/'
RW=W+'List_of_Rickenbacker_products'; RS='https://www.rickenbacker.com/series/legacy/'
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
allnames={norm(e['n']) for k in kinds.values() for e in k.get('x',[])}
added=[];skipped=[]
def gof(k,mk):
    for e in k['x']:
        if e.get('mk')==mk and e.get('g'): return e['g']
    for kk in kinds.values():
        for e in kk.get('x',[]):
            if e.get('mk')==mk and e.get('g'): return e['g']
def add(kind,n,mk,y,d_,s,g=None,v=None,role=None):
    k=kinds[kind]
    nn=norm(n)
    if nn in allnames or norm(mk+' '+n) in allnames: skipped.append(n);return
    g=g or gof(k,mk)
    assert g,(n,mk)
    e={'n':n,'d':d_,'mk':mk,'y':y,'s':s,'g':g}
    if v: e['v']=v
    allnames.add(nn)
    idx=None
    for i,x in enumerate(k['x']):
        if x.get('g')==g: idx=i
    if idx is None: k['x'].append(e)
    else: k['x'].insert(idx+1,e)
    added.append((kind,n))
def rk(kind,n,d_,y='',s=RW):
    add(kind,'Rickenbacker '+n,'Rickenbacker',y,d_,s,'United States · Rickenbacker')
SS='Solid-body electric guitar'; SH='Semi-hollow electric guitar'; HB='Hollow-body electric guitar'
# Rickenbacker
for n in ['400','425','430','450','460','470','480','481','483','490']:
    rk(SS,n,'Rickenbacker Spanish 400 series model, listed as a full-size solid body on the Rickenbacker products list.')
for n in ['610','615','625','650','660']:
    rk(SS,n,'Rickenbacker Spanish 600 series solid-body model named on the Rickenbacker products list.')
for n,t in [('650C Colorado','Series 600 model'),('650D Dakota','Series 600 model'),('650S Sierra','Series 600 model')]:
    rk(SS,n,'Rickenbacker '+t+' named on the maker\'s legacy page.',s=RS)
for n in ['800','850','900','950','1000']:
    rk(SS,n,'Rickenbacker Spanish 800/900 series model, solid body or 3/4 solid body, named on the Rickenbacker products list.')
for n in ['1993','1995','1996','1997','1998']:
    rk(SS,n,'Rose Morris export model; the number is a model code, not a year, per the Rickenbacker products list.')
for n in ['220','230','2050','2060']:
    rk(SH,n,'Rickenbacker Spanish 200 series hollow or semi-hollow model named on the Rickenbacker products list.')
for n in ['340','350','370','380L Laguna','381']:
    rk(SH,n,'Rickenbacker 300 series thin-body or semi-acoustic model named on the Rickenbacker products list and the maker\'s legacy page.')
EB='Electric bass guitar'
for n,dd in [('2020','Rickenbacker 2000 series bass'),('2030','Rickenbacker 2000 series bass'),('2050','Rickenbacker 2000 series bass'),('2060','Rickenbacker 2000 series bass'),('3000','Rickenbacker 3000 series bass'),('3001','Rickenbacker 3000 series bass'),('4000','Rickenbacker 4000 series bass, the series\' first model'),('4004 Cheyenne','Rickenbacker 4000 series bass named on the maker\'s legacy page'),('4004 Laredo','Rickenbacker 4000 series bass named on the maker\'s legacy page'),('1999','Rose Morris export version of the 4001 bass')]:
    rk(EB,n,dd+'.', s=RS if '4004' in n else RW)
SSA='Steel-string acoustic guitar'
for n in ['700C Comstock','700S Shasta','730L Laramie','730S Shiloh']:
    rk(SSA,n,'Rickenbacker 700 series acoustic guitar named on the maker\'s legacy page.',s=RS)
# Gretsch
G='United States · Gretsch'
add(SS,'Silver Jet (G6129)','Gretsch','','Silver-sparkle sister of the Duo Jet named on the Gretsch 6128 page; variants include G6129T and G6129-1957.',W+'Gretsch_6128',G)
add(SS,'Round Up (G6130)','Gretsch','','Gretsch Duo Jet relative named on the Gretsch 6128 page.',W+'Gretsch_6128',G)
add(EB,'Thunder Jet (G6128B)','Gretsch','','Bass version of the Duo Jet named on the Gretsch 6128 page.',W+'Gretsch_6128',G)
add(HB,'Black Falcon (6136 SLBP)','Gretsch','','Brian Setzer black version of the White Falcon named on the Gretsch 6136 page.',W+'Gretsch_6136',G)
add(HB,'Silver Falcon (6136 TSL)','Gretsch','','Silver version of the White Falcon named on the Gretsch 6136 page.',W+'Gretsch_6136',G)
# Fender
F='United States · Fender'
add(SS,'Esquire','Fender','1950','Single-pickup bolt-on guitar, the first solid-body guitar Fender marketed; first made March 1950, second run 1951-1969.',W+'Fender_Esquire',gof(kinds[SS],'Fender'))
add(SS,'Marauder','Fender','1965','Guitar with four pickups hidden under the pickguard, in the 1965 catalogue but never in series production; a Modern Player version came in 2011.',W+'Fender_Marauder',gof(kinds[SS],'Fender'))
CA='Combo amp'
add(CA,'Fender Hot Rod DeVille','Fender','1996','60-watt three-channel tube combo in 2x12 or 4x10 form, a higher-gain Blues DeVille; versions II to IV.',W+'Fender_Hot_Rod_DeVille',gof(kinds[CA],'Fender'))
add(CA,'Fender Bandmaster Reverb','Fender','','Fender amplifier named in Wikipedia\'s Fender amplifiers category; no year stated there.',W+'Category:Fender_amplifiers',gof(kinds[CA],'Fender'))
add(CA,'Fender Vibrosonic Reverb','Fender','','Fender amplifier named in Wikipedia\'s Fender amplifiers category; no year stated there.',W+'Category:Fender_amplifiers',gof(kinds[CA],'Fender'))
# Vox
VX='United Kingdom · Vox'; VT='https://www.voxac30.org.uk/vox_ac30_timeline.html'
for n,y,dd in [('AC4','1962','Vox amplifier listed in the AC30 timeline for 1962.'),('AC30 Twin','1960','AC30 variant listed in the Vox AC30 timeline.'),('AC30 Super Twin','1961','Vox Super Twin amplifier listed for 1961 in the AC30 timeline.'),('T60 Bass','1962','Vox bass amplifier listed for 1962 in the AC30 timeline.'),('AC30 Super Transonic','1962','AC30 variant listed for 1962 in the AC30 timeline.'),('AC30 Bass','1960','AC30 bass variant listed for 1960 in the AC30 timeline.')]:
    add(CA,'Vox '+n,'Vox',y,dd,VT,VX)
# Epiphone
EP='United States · Epiphone'; EW=W+'Epiphone'
def ep(kind,n,y,dd): add(kind,'Epiphone '+n,'Epiphone',y,dd,EW,EP)
for n in ['Les Paul','SG','Flying V','Firebird','Explorer','G-400','Genesis','Nova','Spirit','Special']:
    ep(SS,n,'','Epiphone solid-body model named in the Epiphone article; no year stated there.')
for n in ['ES-335','ES-339']: ep(SH,n,'','Epiphone semi-hollow model named in the Epiphone article; no year stated there.')
for n,y in [('Byron','1938'),('Ritz','1941'),('Devon','1951'),('Kent','1950'),('Zenith',''),('Triumph',''),('Deluxe','')]:
    ep('Archtop acoustic guitar',n,y,'Epiphone archtop named in the Epiphone article.' if y else 'Epiphone archtop named in the Epiphone article; no year stated there.')
for n,y in [('FT 75','1935-1942'),('FT 37','1935-1942'),('FT 27','1935-1941'),('FT De Luxe','1939-1942'),('FT 50','1941-1950'),('FT 30','1941-1954'),('Hummingbird',''),('Dove',''),('J-200',''),('J-45','')]:
    ep(SSA,n,y,'Epiphone flat-top named in the Epiphone article.')
for n in ['Madrid','Classic','Seville']: ep('Classical guitar',n,{'Madrid':'1962','Classic':'1963','Seville':'1961'}[n],'Epiphone nylon-string guitar named in the Epiphone article.')
for n,y in [('Thunderbird Bass',''),('AccuBass',''),('RockBass',''),('PowerBass','')]: ep(EB,n,y,'Epiphone bass named in the Epiphone article; no year stated there.')
for n,y in [('Valve Junior','2005'),('So Cal','2005'),('Blues Custom','2005'),('Triggerman','2005'),('Valve Hot Rod','2009'),('Valve Senior','2009'),('Electar Century','1939')]:
    ep(CA,n,y,'Epiphone amplifier named in the Epiphone article.')
# Stradivari guitars
CG='Classical guitar'; SG_='https://en.wikipedia.org/wiki/List_of_Stradivarius_instruments'
vers=[{'n':'Hill','mk':'Antonio Stradivari','y':'1688','d':'held by the Ashmolean Museum, Oxford'},
 {'n':'Sabionari','mk':'Antonio Stradivari','y':'1679','d':'privately owned; restored by Lorenzo Frignani to its five-course baroque form and described as the only playable Stradivari guitar'},
 {'n':'Rawlins','mk':'Antonio Stradivari','y':'1700','d':'held by the National Music Museum, South Dakota; once owned by Louis Krasner'},
 {'n':'Vuillaume','mk':'Antonio Stradivari','y':'1711','d':'held by the Cite de la Musique, Paris; owned by Jean-Baptiste Vuillaume, acquired 1880'}]
vers[3]['d']=vers[3]['d'].replace('Cite','Cité')
k=kinds[CG]
k['x'].insert(0,{'n':'Stradivari guitar','a':'Stradivarius guitar','d':'Baroque guitars from Antonio Stradivari\'s Cremona workshop; five complete ones survive, four of them named on Wikipedia\'s list.','mk':'Antonio Stradivari','y':'1679-1711','s':SG_,'v':vers,'g':'Italy · Antonio Stradivari'})
added.append((CG,'Stradivari guitar'))
tmp=P+'.tmp'
json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1);os.replace(tmp,P)
print(len(added),'added; skipped dup:',skipped)
