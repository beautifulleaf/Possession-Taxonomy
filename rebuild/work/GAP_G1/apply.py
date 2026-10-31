import json,os,urllib.parse,re,sys
P='/home/user/Possession-Taxonomy/rebuild/out/G1.json'
W='/home/user/Possession-Taxonomy/rebuild/work/GAP_G1/'
d=json.load(open(P))
def norm(s): return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()
kinds={}
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']: kinds[k['n']]=k
def keys(e):
    ks={norm(e['n'])}
    s=e.get('s','')
    if '/wiki/' in s: ks.add(norm(urllib.parse.unquote(s.split('/wiki/')[1])))
    return ks
log=[]
CODES={'sal':'Saloon','lux':'Luxury saloon','hat':'Hatchback','est':'Estate','mpv':'MPV','suv':'SUV','cpe':'Coupé','cnv':'Convertible','rds':'Roadster','spt':'Sports car','gt':'Grand tourer','lim':'Limousine','mus':'Muscle car','sup':'Supercar','hyp':'Hypercar','mic':'Microcar','city':'City car','off':'Off-roader','kit':'Kit car','rac':'Track and racing car','tri':'Three-wheeled car','taxi':'Taxi','van':'Panel van','hot':'Hot hatch','kei':'Kei car','coach':'Coachbuilt car',
'spo':'Sport motorcycle','std':'Standard motorcycle','tou':'Touring motorcycle','cru':'Cruiser motorcycle','adv':'Adventure motorcycle','dsp':'Dual-sport motorcycle','end':'Enduro bike','mx':'Motocross bike','sm':'Supermoto','sco':'Scooter','mop':'Moped','mini':'Mini bike','trk':'Trike','scr':'Scrambler','caf':'Café racer','quad':'Quad bike','tra':'Trail bike','tri2':'Trials bike','cho':'Chopper and bobber','und':'Underbone motorcycle','side':'Motorcycle with sidecar'}
for fn,src in (('dec_cars.tsv','Car, body style not stated'),('dec_moto.tsv','Motorcycle, type not stated'),('dec2_cars.tsv','Car, body style not stated'),('dec2_moto.tsv','Motorcycle, type not stated')):
    if not os.path.exists(W+fn): continue
    dec={}
    for l in open(W+fn,encoding='utf8'):
        p=l.rstrip('\n').split('\t')
        if len(p)<3: continue
        dec[norm(p[0])]=(CODES.get(p[1],p[1]),p[2])
    k0=kinds[src]
    idx={}
    for e in k0['x']:
        for kk in keys(e): idx.setdefault(kk,[]).append(e)
    moved=[];yrs=0;miss=[]
    for t,(kind,y) in dec.items():
        es=idx.get(t)
        if not es: miss.append(t); continue
        for e in es:
            if y and not e.get('y'): e['y']=y; yrs+=1
            if kind!='-' and kind in kinds and e in k0['x'] and e not in moved:
                moved.append(e)
    ids={id(e) for e in moved}
    k0['x']=[e for e in k0['x'] if id(e) not in ids]
    for e in moved: kinds[ [dec_k for dec_k in [None]][0] or 'x'] if False else None
    # move
    for t,(kind,y) in dec.items():
        for e in idx.get(t,[]):
            if id(e) in ids and kind!='-' and kind in kinds:
                kinds[kind].setdefault('x',[]).append(e); ids.discard(id(e))
    print(src,'decisions',len(dec),'unmatched',len(miss),'moved',len(moved),'years set',yrs)
    print(' unmatched:',miss[:40])
    print(' remaining',len(k0['x']))
tmp=P+'.tmp'
json.dump(d,open(tmp,'w'),ensure_ascii=False)
os.replace(tmp,P)
