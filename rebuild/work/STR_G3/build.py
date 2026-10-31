import json,sys,os,copy
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import spec1,spec2,spec3
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/G3.json'))
old={k['n']:k for dp in d['depts'] for s in dp['s'] for k in s['k']}
olddept={dp['n']:dp for dp in d['depts']}
nk0=len(old); na0=sum(len(k.get('x',[])) for k in old.values())
renames={}; demoted=[]
def addm(k,key,item):
    L=k.setdefault(key,[])
    if item not in L: L.append(item)
def absorb(t,o):
    for x in o.get('x',[]):
        if x['n'] not in {y['n'] for y in t.setdefault('x',[])}: t['x'].append(x)
    for key in('m','r'):
        for it in o.get(key,[]) or []: addm(t,key,it)
    al=[a.strip() for a in (t.get('a') or '').split('·') if a.strip()]
    if o['n'] not in al: al.append(o['n'])
    t['a']=' · '.join(al)
    renames[o['n']]=t['n']
see_links={
"Range cooker":[["B5","Freestanding cooker","freestanding version"]],
"Built-in refrigerator":[["B5","Refrigerator","loose fridge"]],
"Built-in wine cabinet":[["B5","Wine fridge","freestanding wine fridge"],["G3","Wine cellar","a whole room"]],
"Wine cellar":[["G3","Built-in wine cabinet","a cabinet instead of a room"]],
"Hob":[["G3","Cooker hood","extracts above it"]],"Cooker hood":[["G3","Hob","the surface beneath"]],
"Kitchen tap":[["G3","Bath and basin tap","bathroom taps"]],"Bath and basin tap":[["G3","Kitchen tap","kitchen taps"]],
"Built-in coffee machine":[["B5","Capsule coffee machine","loose coffee machine"]],
"Heat-storage range cooker":[["G3","Range cooker","cooker without stored heat"]],
"Bathtub":[["H2","Bath lift","helps a person into the tub"]],
"Shower toilet and bidet seat":[["G3","Bidet","separate bidet"]],"Bidet":[["G3","Shower toilet and bidet seat","washing seat"]],
"Heated towel rail":[["B2","Towel","the towel itself"],["G3","Panel radiator","room radiator"]],
"Sauna cabin":[["G3","Steam room","steam instead of dry heat"]],"Steam room":[["G3","Sauna cabin","dry heat instead of steam"]],
"Hard-shell hot tub":[["I3","Pool and hot-tub maintenance","upkeep service"],["G3","Swim spa","spa to swim in"]],
"Swim spa":[["G3","Hard-shell hot tub","spa to sit in"]],
"Flueless fire":[["B7","Electric fireplace","portable electric fire"]],
"Wood-burning stove":[["G3","Inset and wall-hung fire","built-in fire"]],
"Inset and wall-hung fire":[["G3","Wood-burning stove","freestanding stove"]],
"Masonry heater":[["G3","Wood-burning stove","metal stove"]],
"Ceiling fan":[["B7","Pedestal fan","movable fan"]],
"In-wall and in-ceiling speaker":[["D3","In-wall and in-ceiling speaker","audio listing of the same speakers"]],
"Motorised TV lift and projection screen":[["D3","Projector screen","loose screen"]],
"Door":[["B8","Multipoint lock","lock for the door"]],
"Garage door":[["B8","Gate, garage & shutter lock","locks for it"]],
"Window guard":[["B8","Window lock","lock instead of guard"]],
"Stairlift":[["H2","Patient lift","lift for a person"],["G3","Home lift","lift in a shaft"]],
"Home lift":[["G3","Stairlift","chair on a stair rail"]],
"Staircase":[["G3","Stairlift","motor for the stairs"]],
"Storage heater":[["G3","Panel radiator","water-filled emitter"]],
"Panel radiator":[["G3","Heated towel rail","bathroom rail"]],
"Whole-house dehumidifier":[["B7","Dehumidifier","portable dehumidifier"]],
"Central vacuum system":[["B6","Cylinder vacuum cleaner","portable cleaner"]],
"Under-sink water filter":[["G3","Reverse-osmosis system","finer purification"],["B5","Water filter jug","jug filter"]],
"Reverse-osmosis system":[["G3","Under-sink water filter","simpler filter"]],
"Solar panel":[["G3","Solar water heater","sun heats water instead"]],
"Solar water heater":[["G3","Solar panel","sun makes power instead"]],
"Home battery":[["G3","Inverter","converts the stored power"]],
"Inverter":[["G3","Home battery","stores the power"]],
"Intruder alarm system":[["B8","Wireless alarm kit","boxed alarm kit"]],
"Door phone and video intercom":[["B8","Video doorbell","doorbell camera"]],
"In-ground swimming pool":[["C2","Above-ground pool","not built into the ground"]],
"Pergola":[["G3","Patio cover","solid roof"]],"Patio cover":[["G3","Pergola","open roof"]],
"Gazebo":[["G3","Summerhouse","enclosed building"]],"Summerhouse":[["G3","Gazebo","open-sided"]],
"Outdoor kitchen":[["C2","Open-fire grill","loose grill"]],
"Decking":[["G3","Patio","paved instead"]],"Patio":[["G3","Decking","raised timber instead"]],
"Garden shed":[["B8","Shed & garage security","security for it"]],
"Orangery":[["C2","Greenhouse","plant-growing building"]],
"Garden office":[["G3","Garden log cabin","log building"]],"Garden log cabin":[["G3","Garden office","insulated working room"]],
"Garage":[["G3","Carport","open shelter"]],"Carport":[["G3","Garage","enclosed"]],
"Under-cabinet light":[["B3","Strip light","loose strip"]],"Cove lighting":[["B3","Strip light","loose strip"]],
}
depts=[]
for dn,shs in spec2.STRUCT:
    od=olddept[dn]
    nd={'n':dn,'mode':od.get('mode','mixed'),'t':spec1.DEPT[dn][0],'ax':spec1.DEPT[dn][1]}
    if od.get('note') and False: nd['note']=od['note']
    if od.get('b'): nd['b']=od['b']
    nd['s']=[]
    for sn,ks in shs:
        sh={'n':sn,'t':spec1.SH[sn][0]}
        if spec1.SH[sn][1]: sh['ax']=spec1.SH[sn][1]
        sh['k']=[]
        for ks_ in ks:
            name,abs_=(ks_ if isinstance(ks_,tuple) else (ks_,[]))
            if name in spec2.NEW:
                n=spec2.NEW[name]; k={'n':name,'a':n['a'],'d':n['d'],'tt':n['tt'],'s':n['s']}
            else:
                k=copy.deepcopy(old[name])
                for a in abs_: absorb(k,old[a])
                tt=spec3.TT.get(name)
                if tt is None: sys.exit('no tt '+name)
                k['tt']=tt; k.pop('t',None)
                # demote generic archetypes
                keep=[]
                for x in k.get('x',[]):
                    if x['n'] in spec2.DEMOTE:
                        addm(k,'m',[x['n'],x.get('mk','')]); demoted.append((name,x['n']))
                    else: keep.append(x)
                if keep: k['x']=keep
                else: k.pop('x',None)
                for key in('m','r'):
                    if not k.get(key): k.pop(key,None)
            if name in see_links: k['see']=see_links[name]
            sh['k'].append(k)
        nd['s'].append(sh)
    depts.append(nd)
d['depts']=depts
d['ax']=spec1.CAT_AX; d['key']=spec1.KEY
# see check
names={}
for dp in depts:
    for s in dp['s']:
        for k in s['k']: names[k['n']]=1
bad=[]
for dp in depts:
    for s in dp['s']:
        for k in s['k']:
            for c,n,w in k.get('see',[]):
                if c=='G3':
                    if n not in names: bad.append((c,n))
                else:
                    r=json.load(open(R+f'reader/{c}.json'))
                    rn={kk['n'] for a in r['depts'] for b in a['s'] for kk in b['k']}
                    if n not in rn: bad.append((c,n))
if bad: sys.exit('bad see %s'%bad)
nk=sum(len(s['k']) for dp in depts for s in dp['s']); na=sum(len(k.get('x',[])) for dp in depts for s in dp['s'] for k in s['k'])
print('kinds',nk0,'->',nk,'arch',na0,'->',na,'demoted',len(demoted))
json.dump(renames,open(R+'out/G3_renames.json','w'),indent=1,ensure_ascii=False)
tmp=R+'out/G3.json.tmp'
json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1)
if '--write' in sys.argv: os.replace(tmp,R+'out/G3.json')
json.dump(demoted,open(os.path.dirname(os.path.abspath(__file__))+'/demoted.json','w'),ensure_ascii=False)
