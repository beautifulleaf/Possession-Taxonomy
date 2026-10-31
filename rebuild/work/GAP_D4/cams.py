import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/D4.json'
d=json.load(open(P))
kinds={k['n']:k for dep in d['depts'] for sh in dep['s'] for k in sh['k']}
def N(n,mk,y,desc,s,vers,g,**kw):
    e={'n':n,'a':'','d':desc,'mk':mk,'y':y,'s':s,'v':[{'n':a,'mk':mk,'y':b,'d':c} for a,b,c in vers],'dt':'','g':g}
    e.update(kw); return e
W='https://en.wikipedia.org/wiki/'
add={
'Film SLR camera':[
 N('Alpa','Pignons','','Swiss 35 mm reflex cameras by Pignons from the 1940s; Japanese-made Si2000 (M42) and Si3000 (Pentax K) followed.',W+'Alpa',[('Alpa-Reflex','',''),('Alpa 11','','last Pignons-made series'),('Si2000','','M42 mount, made by Chinon'),('Si3000','','Pentax K mount, made by Chinon')],'Alpa'),
 N('Fujica X','Fujifilm','','Fujifilm bayonet-mount SLRs of the late 1970s and early 1980s; the line ended in 1985.',W+'Fujica_X-mount',[('AX-1','',''),('AX-3','',''),('AX-5','',''),('AX Multi','',''),('STX-1','',''),('STX-1N','',''),('STX-2','',''),('MPF105X','',''),('MPF105XN','','')],'Fujica X'),
 N('Petri Flex','Petri','1959','Petri SLR line; the first, the Penta of 1959, used M42, and most later Flex bodies used a breech-lock bayonet.',W+'Petri_Camera',[('Penta','1959','M42 mount'),('Petri Flex V','',''),('Petri Flex 7','',''),('Petri FTX','1974','back to M42')],'Petri'),
 N('Praktina','Kamera-Werke Niedersedlitz','1953','East German 35 mm SLR system with interchangeable finders and film backs, built 1953 to 1958.','https://mikeeckman.com/praktina-fx-1953/',[('Praktina FX','1953','about 67,000 made across five generations'),('Praktina IIa','1958','final version; production ended 1960')],'Praktina'),
 N('Canon EOS film bodies','Canon','1987','Canon autofocus film SLRs on the EF mount, begun by the EOS 650, the first EOS camera.',W+'Canon_EOS_650',[('EOS 650','1987','first EOS camera; 2 March 1987'),('EOS 5 (A2)','1992','eye-controlled focusing'),('EOS-3','1998','45-point autofocus')],'Canon EF',role='origin'),
],
'Medium-format SLR camera':[
 N('Kowa Six','Kowa','1968','Japanese 120/220 medium-format SLR with a leaf shutter in the lens and a Kowa bayonet, made 1968 to 1972.','https://vintagecameradigest.com/kowa-six/',[],'Kowa Six'),
],
'DSLR camera':[
 N('Leica S','Leica','2008','Leica medium-format digital SLR system on the S mount, from the S2 to the S3.',W+'Leica_S-System',[('S2','2008',''),('S (Typ 006)','2012',''),('S (Typ 007)','2014','first CMOS sensor'),('S3','2018','announced October 2018')],'Leica S'),
 N('Samsung GX','Samsung','2006','Samsung DSLR on the Pentax KAF mount; the GX-1S was a rebadged Pentax *ist DS2 developed with Pentax.','https://www.photographyblog.com/news/samsung_gx_1s_dslr',[('GX-1S','2006','')],'Pentax K'),
],
'Mirrorless camera':[
 N('Olympus PEN E-P','Olympus','2009','Olympus digital PEN line on Micro Four Thirds, begun by the E-P1, the first Olympus MFT camera.',W+'Olympus_PEN_E-P1',[('E-P1','2009','announced 16 June 2009'),('E-P2','2009','announced November 2009')],'Micro Four Thirds'),
 N('Pentax K-01','Pentax','2012','Mirrorless body designed by Marc Newson that takes Pentax K-mount SLR lenses without an adapter.',W+'Pentax_K-01',[],'Pentax K'),
],
}
for kn,es in add.items():
    k=kinds[kn]; have={x['n'].lower() for x in k['x']}
    for e in es:
        if e['n'].lower() not in have: k['x'].append(e)
def yk(x):
    import re; m=re.search(r'\d{4}',x.get('y','') or ''); return int(m.group(0)) if m else 9999
for kn in add:
    k=kinds[kn]; first={}
    for x in k['x']: first[x['g']]=min(first.get(x['g'],9999),yk(x))
    k['x'].sort(key=lambda x:(first[x['g']],x['g'],yk(x),x['n']))
# light meter versions
lm=kinds['Light meter']
for x in lm['x']:
    if x['n']=='Weston Master':
        x['y']='1939'; x['s']=x.get('s')
        x['v']=[{'n':a,'mk':'Weston','y':b,'d':c} for a,b,c in [('Master','1939','Weston, Newark, New Jersey'),('Master II','1947','about; Sektonic made a licensed version from about 1953'),('Master III','1956',''),('Master V','1963','made in the UK 1963 to 1972'),('Euro-Master','1973','Sangamo Weston, later East Kilbride Instruments and Megatron'),('Euro-Master II','1985','Megatron, to 2010')]]
        x['d']='Weston exposure-meter line begun with the Master of 1939; later UK makers carried it on as the Euro-Master.'
        x['s']='https://www.35mmc.com/20/06/2025/weston-master-v-a-review-of-the-masterful-exposure-meter/'
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
print('ok')
