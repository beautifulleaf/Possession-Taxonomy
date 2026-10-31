import json,re,os,copy
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/D2.json'))
brands=json.load(open(R+'out/D2_brands.json'))
ren=json.load(open(R+'out/D2_renames.json'))
removed=[]  # report
COMMODITY_DEPTS={'Power & charging','Cases & accessories'}
COMMODITY_KINDS={'Corded phone','Cordless phone','IP phone','Station microphone & headset','Digital-mode interface','Station power supply','Antenna rotator','Wall charger'}
def V(n,y='',d=None,mk=None):
    o={'n':n}
    if mk: o['mk']=mk
    o['y']=y
    if d: o['d']=d
    return o
def E(n,mk,y,s,v=None,d=None,a=''):
    return {'n':n,'a':a,'d':d or f"{mk}'s {n} line.",'mk':mk,'y':y,'s':s,'v':v or []}
# ---- rebuilt canon entries from fetched lists
S_IPAD='https://en.wikipedia.org/wiki/IPad'
ipad=[
 E('iPad','Apple','2010',S_IPAD,[V('iPad (1st generation)','2010','original'),V('iPad 2','2011'),V('iPad (3rd generation)','2012','first Retina display'),V('iPad (4th generation)','2012'),V('iPad (5th generation)','2017'),V('iPad (6th generation)','2018'),V('iPad (7th generation)','2019'),V('iPad (8th generation)','2020'),V('iPad (9th generation)','2021'),V('iPad (10th generation)','2022'),V('iPad (11th generation)','2025')],"Apple's standard tablet; the 2010 original defined the modern slate tablet."),
 E('iPad mini','Apple','2012',S_IPAD,[V('iPad mini (1st generation)','2012','original'),V('iPad mini 2','2013'),V('iPad mini 3','2014'),V('iPad mini 4','2015'),V('iPad mini (5th generation)','2019'),V('iPad mini (6th generation)','2021'),V('iPad mini (7th generation)','2024'),V('iPad mini (8th generation)','2026')],"Apple's small-screen iPad."),
 E('iPad Air','Apple','2013',S_IPAD,[V('iPad Air (1st generation)','2013','original'),V('iPad Air 2','2014'),V('iPad Air (3rd generation)','2019'),V('iPad Air (4th generation)','2020'),V('iPad Air (5th generation)','2022'),V('iPad Air (6th generation)','2024'),V('iPad Air (7th generation)','2025'),V('iPad Air (8th generation)','2026')],"Apple's mid-range iPad."),
 E('iPad Pro','Apple','2015',S_IPAD,[V('iPad Pro (1st generation)','2015','12.9-inch; a 9.7-inch model followed in 2016'),V('iPad Pro (2nd generation)','2017'),V('iPad Pro (3rd generation)','2018'),V('iPad Pro (4th generation)','2020'),V('iPad Pro (5th generation)','2021'),V('iPad Pro (6th generation)','2022'),V('iPad Pro (7th generation)','2024'),V('iPad Pro (8th generation)','2025','M5')],"Apple's top-end iPad."),
]
S_K='https://en.wikipedia.org/wiki/Amazon_Kindle'
kindle=[
 E('Kindle','Amazon','2007',S_K,[V('Kindle (1st generation)','2007','original'),V('Kindle 2','2009'),V('Kindle Keyboard','2010','Kindle 3'),V('Kindle 4','2011'),V('Kindle Touch','2011'),V('Kindle 5','2012'),V('Kindle 7','2014'),V('Kindle 8','2016'),V('Kindle 10','2019'),V('Kindle (2022)','2022','11th generation'),V('Kindle (2024)','2024')],"Amazon's e-reader line; the base model of each generation."),
 E('Kindle DX','Amazon','2009',S_K,[V('Kindle DX','2009'),V('Kindle DX International','2010'),V('Kindle DX Graphite','2010')],"Large-screen Kindle."),
 E('Kindle Paperwhite','Amazon','2012',S_K,[V('Kindle Paperwhite (1st generation)','2012','original'),V('Kindle Paperwhite 2','2013'),V('Kindle Paperwhite 3','2015'),V('Kindle Paperwhite 4','2018'),V('Kindle Paperwhite 5','2021'),V('Kindle Paperwhite Signature Edition','2021'),V('Kindle Paperwhite 6','','no date in the table'),V('Kindle Paperwhite 6 Signature Edition','','no date in the table')],"Backlit Kindle line."),
 E('Kindle Voyage','Amazon','2014',S_K,[V('Kindle Voyage','2014')],"Flush-front Kindle with page-press sensors."),
 E('Kindle Oasis','Amazon','2016',S_K,[V('Kindle Oasis (1st generation)','2016','original'),V('Kindle Oasis 2','2017'),V('Kindle Oasis 3','2019')],"Metal Kindle with page buttons."),
 E('Kindle Colorsoft','Amazon','2024',S_K,[V('Kindle Colorsoft Signature Edition','2024','first colour Kindle'),V('Kindle Colorsoft','2025'),V('Kindle Colorsoft Signature Edition (2025)','2025')],"Colour e-paper Kindle."),
]
S_GS='https://en.wikipedia.org/wiki/Samsung_Galaxy_S_series'
galS=[V('Galaxy S','2010','original'),V('Galaxy S II','2011'),V('Galaxy S III','2012'),V('Galaxy S4','2013'),V('Galaxy S5','2014'),V('Galaxy S6 / S6 Edge','2015'),V('Galaxy S6 Edge+','2015'),V('Galaxy S7 / S7 Edge','2016'),V('Galaxy S8 / S8+','2017'),V('Galaxy S9 / S9+','2018'),V('Galaxy S10e / S10 / S10+ / S10 5G','2019'),V('Galaxy S10 Lite','2020'),V('Galaxy S20 / S20+ / S20 Ultra','2020'),V('Galaxy S20 FE','2020'),V('Galaxy S21 / S21+ / S21 Ultra','2021'),V('Galaxy S21 FE','2022'),V('Galaxy S22 / S22+ / S22 Ultra','2022','Ultra gains the S Pen'),V('Galaxy S23 / S23+ / S23 Ultra','2023'),V('Galaxy S23 FE','2023'),V('Galaxy S24 / S24+ / S24 Ultra','2024'),V('Galaxy S24 FE','2024'),V('Galaxy S25 / S25+ / S25 Ultra','2025'),V('Galaxy S25 Edge','2025'),V('Galaxy S25 FE','2025'),V('Galaxy S26 / S26+ / S26 Ultra','2026'),V('Galaxy S26 FE','2026')]
S_GT='https://en.wikipedia.org/wiki/Samsung_Galaxy_Tab_series'
tabs=[
 E('Galaxy Tab (early lines)','Samsung','2010',S_GT,[V('Galaxy Tab 7.0','2010'),V('Galaxy Tab 8.9 / 10.1','2011'),V('Galaxy Tab 2','2012'),V('Galaxy Tab 3','2013'),V('Galaxy Tab 4','2014'),V('Galaxy Tab Pro','2014')],"Samsung's first tablet lines, before the S and A split."),
 E('Galaxy Tab S','Samsung','2014',S_GT,[V('Galaxy Tab S 8.4 / 10.5','2014','original')]+[V(f'Galaxy Tab {x}') for x in ['S2','S3','S4','S5e','S6','S7','S8','S9','S10','S11','S12']],"Samsung's flagship tablet line."),
 E('Galaxy Tab A','Samsung','',S_GT,[V(f'Galaxy Tab {x}') for x in ['A 8.0','A 9.7','A 10.1','A 10.5','A6','A7','A8','A9 / A9+','A11 / A11+']],"Samsung's entry-level tablet line."),
 E('Galaxy Tab Active','Samsung','2014',S_GT,[V('Galaxy Tab Active','2014'),V('Galaxy Tab Active 2','2017'),V('Galaxy Tab Active Pro','2019'),V('Galaxy Tab Active 3','2020'),V('Galaxy Tab Active 4 Pro','2022'),V('Galaxy Tab Active 5','2024'),V('Galaxy Tab Active 5 Pro','2025')],"Samsung's rugged tablet line."),
]
# ---- grouping for m / r
KLAB={'Handheld GPS':'handheld GPS units','Car sat-nav':'car sat-navs','Satellite phone':'satellite phones','Satellite messenger':'satellite messengers','Personal locator beacon':'locator beacons','Satellite hotspot':'satellite hotspots','HF base transceiver':'HF transceivers','Mobile transceiver':'mobile transceivers','Portable QRP transceiver':'portable transceivers','Amateur handheld transceiver':'handheld transceivers','Linear amplifier':'amplifiers','Walkie-talkie':'walkie-talkies','CB radio':'CB radios','Radio scanner':'scanners','Antenna tuner':'antenna tuners'}
def known(k):
    s=set()
    for x in k.get('x',[]):
        s.add(x['n'].lower())
        for v in x.get('v',[]): s.add(v['n'].lower())
    return s
def convert_models(k):
    ks=k.get('s','')
    m=k.get('m') or []; r=k.get('r') or []
    ex=known(k)
    left=[]
    for n,mk in m:
        if n.lower() in ex or any(n.lower() in e for e in ex): removed.append(f'{k["n"]}: {mk} {n} (already a version)'); continue
        left.append((n,mk))
    out=[]
    for rn,rmk in r:
        grp=[(n,mk) for n,mk in left if mk==rmk and (n.lower().startswith(rn.lower().split()[0]) or rn.lower().endswith('numbered series'))]
        if rn.endswith('numbered series'):
            nm=rmk
        else: nm=rn if rmk.lower() in rn.lower() else f'{rmk} {rn}'
        if any(e['n']==nm for e in out): continue
        left=[t for t in left if t not in grp]
        out.append(E(nm,rmk,'',ks,[V(n) for n,_ in grp]))
    bymk={}
    for n,mk in left: bymk.setdefault(mk,[]).append(n)
    for mk,ns in bymk.items():
        if len(ns)>=2:
            out.append(E(f"{mk} {KLAB.get(k['n'],'models')}",mk,'',ks,[V(n) for n in ns]))
        else:
            n=ns[0]; nm=n if mk.lower() in n.lower() else f'{mk} {n}'
            out.append(E(nm,mk,'',ks,[]))
    return out
SPECIAL={ # (kind, maker) -> entry name overrides handled by names above; plus merges
}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            commodity = dp['n'] in COMMODITY_DEPTS or k['n'] in COMMODITY_KINDS
            if commodity:
                for n,mk in k.get('m') or []: removed.append(f'{k["n"]}: {mk} {n} (commodity kind, no entries)')
                for n,mk in k.get('r') or []: removed.append(f'{k["n"]}: range {mk} {n} (commodity kind)')
                k.pop('m',None); k.pop('r',None)
                if k.get('x'): k['x']=k['x']
                continue
            if k.get('m') or k.get('r'):
                k.setdefault('x',[])
                k['x']+=convert_models(k)
            k.pop('m',None); k.pop('r',None)
# ---- replace canon entries
def kind(name):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==name: return k
def drop(k,names): k['x']=[x for x in k['x'] if x['n'] not in names]
k=kind('Touchscreen smartphone')
for x in k['x']:
    if x['n']=='Galaxy S': x['v']=galS
    if x['n']=='iPhone': x['v']=[v for v in x['v']]
    if x['n']=='Galaxy S': x['s']=S_GS
k=kind('Tablet'); drop(k,['iPad','Galaxy Tab S']); k['x']=ipad+tabs+k['x']
k=kind('E-reader'); drop(k,['Kindle']); k['x']=kindle+k['x']
# Boox android E Ink -> merge
k=kind('E-paper writing tablet'); ae=kind('Android E Ink tablet')
for x in (ae.get('x') or []): 
    x['v']=[V(v['n']) for v in x['v']]; k['x'].append(x)
for s in d['depts'][1]['s']:
    s['k']=[q for q in s['k'] if q['n']!='Android E Ink tablet']
ren['Android E Ink tablet']='E-paper writing tablet'
# ---- nl / sel / xg / g
SEL_DEF="No complete reference lists every line of this kind. Entries follow each maker's own named lines, with the Wikipedia or maker page cited on each entry; lines without such a page are not covered."
SEL_SPEC={
 'Touchscreen smartphone':"No single list covers every smartphone line. Entries are the platform lines of the main makers, each from its own Wikipedia article; iPhone and Galaxy S generations follow Wikipedia's List of iPhone models and Samsung Galaxy S series article. Pixel, Galaxy Note, Nexus and others follow their cited articles.",
 'Tablet':"iPad generations follow the model tables of Wikipedia's iPad article and Galaxy Tab lines follow Wikipedia's Samsung Galaxy Tab series; other lines follow their cited pages. Not every tablet maker is covered.",
 'E-reader':"Kindle generations follow the device table of Wikipedia's Amazon Kindle article (first 100,000 characters read); other lines follow their cited pages.",
 'Smartwatch':"Apple Watch generations follow the model table of Wikipedia's Apple Watch article; other lines follow their cited articles.",
 'Keypad phone':"No complete list of feature phones exists. Entries are collector models named in Wikipedia's List of Nokia products and in per-model articles; other makers are covered only where a model article was cited.",
 'Early mobile phone':"Entries follow the per-model Wikipedia articles cited; Nokia's 1G models are named in Wikipedia's List of Nokia products.",
 'Vintage telephone':"No complete list exists. Entries are the collector models named in the cited Wikipedia articles.",
}
NL_SPEC={
 'Touchscreen smartphone':"One entry is a smartphone platform line sold under one name, such as iPhone or Galaxy S; each generation, size or variant is a version.",
 'Keyboard smartphone':"One entry is a smartphone line with a physical keyboard; generations and variants are versions.",
 'Tablet':"One entry is a tablet line sold under one name, such as iPad Air or Galaxy Tab S; each generation is a version.",
 'E-reader':"One entry is an e-reader line, such as Kindle Paperwhite or Kobo Libra; each generation is a version.",
 'Smartwatch':"One entry is a smartwatch line, such as Apple Watch or Galaxy Watch; each generation is a version.",
 'Vintage telephone':"One entry is a telephone model or design type that collectors name; revisions and numbered variants are versions.",
 'Keypad phone':"One entry is a keypad mobile model family, such as the Nokia 3310; regional codes and refreshes are versions.",
}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            if not k.get('x'): continue
            k['nl']=NL_SPEC.get(k['n'],"One entry is a named device line or model from one maker, sold under its own name; generations, revisions and variants are versions.")
            k['sel']=SEL_SPEC.get(k['n'],SEL_DEF)
            k['xg']='maker'
            for x in k['x']:
                x['g']=x.get('mk') or 'Various makers'
                if x.get('d') is None: x['d']=''
                x['v']=[ (q if isinstance(q,dict) else V(q)) for q in x.get('v',[]) ]
            def yr(x):
                m=re.search(r'\d{4}',x.get('y') or ''); return int(m.group()) if m else 9999
            first={}
            for x in k['x']:
                first[x['g']]=min(first.get(x['g'],9999),yr(x))
            k['x'].sort(key=lambda x:(first[x['g']],x['g'],yr(x),x['n']))
# ---- market panel
IDC='https://www.gsmarena.com/idc_smartphone_shipments_up_23_in_q4_2025_apple_is_the_clear_winner_-news-71096.php'
CP='https://www.counterpointresearch.com/insight/us-smartphone-market-share/'
WP='https://en.wikipedia.org/wiki/Mobile_phone'
ms=[]
for w,sh,n in [('Apple','19.7 %','247.8 million units'),('Samsung','19.1 %','241.2 million units'),('Xiaomi','13.1 %','165.3 million units'),('vivo','8.2 %','103.9 million units'),('Oppo','8.1 %','102 million units')]:
    ms.append({'mkt':'Global smartphones','who':w,'share':sh,'yr':2025,'s':IDC,'note':f'share of shipments, {n}; IDC Worldwide Quarterly Mobile Phone Tracker, 13 January 2026'})
for w,a,b in [('Apple','67 %','54 %'),('Samsung','17 %','30 %'),('Motorola','10 %','11 %'),('Google','3 %','3 %')]:
    ms.append({'mkt':'US smartphones','who':w,'share':a,'yr':2025,'s':CP,'note':'share of shipments in Q4 2025, Counterpoint Research'})
    ms.append({'mkt':'US smartphones','who':w,'share':b,'yr':2026,'s':CP,'note':'share of shipments in Q2 2026, Counterpoint Research'})
for w,sh in [('Samsung','21 %'),('Apple','16 %'),('Xiaomi','13 %'),('Oppo','10 %'),('Vivo','9 %')]:
    ms.append({'mkt':'Global mobile phones (all handsets)','who':w,'share':sh,'yr':2022,'s':WP,'note':'top five makers as stated by the article, which cites Counterpoint Research; covers all mobile phones, not smartphones only'})
d['depts'][0]['ms']=ms
# ---- brand register
have={b['n'] for b in brands['b']}
add=set()
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            for x in k.get('x',[]):
                mk=x.get('mk')
                if mk and mk not in have: add.add(mk)
for mk in sorted(add): brands['b'].append({'n':mk,'c':'','f':'','seg':'Specialist','kf':'','d':f'Maker of the {mk} lines listed in this category.','sig':[]})
brands['b']=[b for b in brands['b']]
for fn,o in [('D2.json',d),('D2_brands.json',brands),('D2_renames.json',ren)]:
    json.dump(o,open(R+'out/'+fn+'.tmp','w'),ensure_ascii=False,indent=1); os.rename(R+'out/'+fn+'.tmp',R+'out/'+fn)
json.dump(removed,open('removed.json','w'),indent=1)
print(len(removed),'removed',len(add),'brands added')
