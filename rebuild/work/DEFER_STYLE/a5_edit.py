import json,os
P='out/A5.json'
d=json.load(open(P))
META={'Longines':('Switzerland','The Swatch Group','Global group','1983'),
'Hamilton':('United States','The Swatch Group','Global group',''),
'Tudor':('Switzerland','Hans Wilsdorf Foundation (Rolex SA)','Independent',''),
'Zenith':('Switzerland','LVMH','Global group','1999')}
NEW={ 'Dive watch':[('Longines','HydroConquest','longines/hydroconquest',233),('Longines','Legend Diver','longines/legend-diver',38),('Hamilton','Frogman','hamilton/frogman',22)],
'Dress watch':[('Longines','Master Collection','longines/master-collection',487),('Longines','La Grande Classique','longines/la-grande-classique',447),('Longines','Elegant Collection','longines/elegant',138),('Longines','Flagship','longines/flagship',126),('Hamilton','Intra-Matic','hamilton/intra-matic',36),('Hamilton','Boulton','hamilton/boulton',13),('Hamilton','Timeless Classic','hamilton/timeless-classic',10),('Tudor','Classic','tudor/classic',88),('Tudor','Monarch','tudor/monarch',2)],
'Everyday watch':[('Longines','Presence','longines/presence',333),('Longines','Spirit','longines/spirit',116),('Hamilton','Railroad','hamilton/railroad',43),('Hamilton','Valiant','hamilton/valiant',11),('Hamilton','American Classic','hamilton/american-classic',24),('Hamilton','Spirit of Liberty','hamilton/spirit-of-liberty',19),('Tudor','Royal','tudor/royal',95)],
'Chronograph':[('Hamilton','Pan Europ','hamilton/pan-europ',7)],
'Flyback chronograph':[('Tudor','Grantour','tudor/grantour',5)],
'Quartz watch':[('Longines','Conquest V.H.P.','longines/conquest-v-h-p',116)],
'Field watch':[('Hamilton','Khaki Action','hamilton/khaki-action',18)]}
VERS={'Black Bay':[('Black Bay 54','tudor/black-bay-54'),('Black Bay 58','tudor/black-bay-58'),('Black Bay 68','tudor/black-bay-68'),('Black Bay GMT','tudor/black-bay-gmt')],
'Defy':[('Defy Skyline','zenith/defy-skyline')],'Chronomaster':[('Chronomaster Sport','zenith/chronomaster-sport'),('Chronomaster Original','zenith/chronomaster-original'),('Chronomaster Open','zenith/chronomaster-open')]}
OLD="Watchbase for other makers is blocked and deferred."
NEWS="Watchbase brand pages were read in the defer pass for Seiko, Tudor, Longines, Hamilton, Zenith and Tissot and their clear model families added; the Lange, Vacheron Constantin, Panerai and Citizen pages gave no family list."
added=0
def walk(o):
    global added
    if isinstance(o,dict):
        if 'x' in o and o.get('n') in NEW:
            names={e['n'] for e in o['x']}
            for mk,n,slug,cnt in NEW[o['n']]:
                if n in names: continue
                cty,own,tier,oy=META[mk]
                e={'n':n,'d':f'{mk} model family that Watchbase lists with {cnt} watches.','mk':mk,'y':'','s':'https://watchbase.com/'+slug.split('/')[0],'v':[],'cty':cty,'own':own,'tier':tier}
                if oy:e['own_y']=oy
                e['g']=f'{cty}: {mk}'
                idx=[i for i,x in enumerate(o['x']) if x.get('g')==e['g']]
                pos=idx[-1]+1 if idx else len(o['x'])
                o['x'].insert(pos,e); added+=1
        if 'x' in o:
            for e in o['x']:
                if e.get('n') in VERS and e.get('mk') in('Tudor','Zenith'):
                    have={v['n'] for v in e.get('v',[])}
                    for vn,slug in VERS[e['n']]:
                        if vn not in have:
                            e.setdefault('v',[]).append({'n':vn,'y':'','d':'family listed on Watchbase'}); added+=1
        if isinstance(o.get('sel'),str) and OLD in o['sel']: o['sel']=o['sel'].replace(OLD,NEWS)
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for i in o: walk(i)
walk(d)
open(P+'.tmp','w').write(json.dumps(d,ensure_ascii=False,indent=1) if False else json.dumps(d,ensure_ascii=False))
os.rename(P+'.tmp',P); print('added',added)
