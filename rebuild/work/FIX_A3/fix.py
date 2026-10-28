import json,os,copy
P='out/A3.json'
d=json.load(open(P))
def kinds():
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']: yield dp,s,k
def K(n):
    for dp,s,k in kinds():
        if k['n']==n: return dp,s,k
    raise KeyError(n)
def rm(n):
    dp,s,k=K(n); s['k'].remove(k); return k
def D(n): return [x for x in d['depts'] if x['n']==n][0]
def addt(k,ts):
    k['t']=list(k.get('t',[]))+[t for t in ts if t not in k.get('t',[])]
log=[]
# A3-1 earrings
_,_,hoop=K('Hoop earring'); _,_,drop=K('Drop earring'); _,_,stud=K('Stud earring')
rm('Huggie earring'); addt(hoop,['huggie (hugs the earlobe)'])
rm('Chandelier earring'); rm('Threader earring'); addt(drop,['chandelier (wider at base)','threader (chain pulled through the piercing)'])
dp,s,jk=K('Ear jacket')
ec=rm('Ear cuff'); rm('Ear climber')
jk['n']='Ear cuff & jacket'; jk['a']='ear jacket · ear climber · ear crawler · ear wrap'
jk['d']='Earring that wraps the ear or sits behind and in front of the lobe; some need no piercing.'
jk['t']=['ear cuff (cartilage wrap, no piercing)','ear jacket','ear climber','chained to lobe piercing']
jk['s']='https://en.wikipedia.org/wiki/Ear_piercing'
_,_,cl=K('Clip-on earring')
cl['x']=[{"n":"Miriam Haskell clip earrings","a":"","d":"Ornate beaded and glass costume clip earrings from the New York house, seldom signed before 1950.","mk":"Miriam Haskell","y":"1926 onwards","s":"https://en.wikipedia.org/wiki/Miriam_Haskell","v":[],"dt":"art glass · strass · gold-plate · signed or unsigned"}]
# stackable ring
_,_,band=K('Band ring'); st=rm('Stackable ring'); addt(band,['stackable (slim, worn in stacks)'])
# A3-3 new kinds
rings=K('Puzzle ring')[1]
def nk(n,a,dd,s,t=None,x=None):
    k={"n":n,"a":a,"d":dd,"s":s}
    if t:k['t']=t
    if x:k['x']=x
    return k
rings['k']+= [
 nk('Class ring','graduation ring · college ring · school ring','Ring worn by students and alumni to mark a final school year or graduation.','https://en.wikipedia.org/wiki/Class_ring',['high school','college','military academy']),
 nk('Mood ring','','Ring with a thermochromic stone that changes colour with finger temperature.','https://en.wikipedia.org/wiki/Mood_ring',['liquid-crystal stone'],
    [{"n":"Wernick mood ring","a":"","d":"The first commercial mood ring, conceived by Marvin Wernick, on sale from 1975.","mk":"","y":"1975","s":"https://en.wikipedia.org/wiki/Mood_ring","v":[],"dt":"thermochromic stone colour · band metal"}]),
 nk('Poison ring','pillbox ring','Ring with a hidden compartment that could hold poison or other substances.','https://en.wikipedia.org/wiki/Poison_ring',['hinged bezel','sliding bezel']),
 nk('Memento mori ring','mourning ring','Ring that commemorates the dead or reminds the wearer of death; medieval onwards, often an heirloom.','https://en.wikipedia.org/wiki/Mourning_jewellery',['mourning ring (commemorative)','skull motif']),
]
# jade bangle into Bangle
_,_,bg=K('Bangle'); addt(bg,['jade bangle (nephrite or jadeite)'])
# amulets: add to Pendant shelf
pend=K('Cameo')[1]
pend['k']+=[
 nk('Evil-eye amulet','nazar · nazar boncuğu','Glass amulet, usually blue and eye-shaped, worn against the evil eye; common from Turkey and Greece to South Asia.','https://en.wikipedia.org/wiki/Nazar_(amulet)',['glass bead','hamsa-backed','bracelet or pendant']),
 nk('Cornicello','Italian horn · cornetto','Twisted horn-shaped Italian amulet from southern Italy, worn against the evil eye and bad luck.','https://en.wikipedia.org/wiki/Cornicello',['gold','silver','red coral']),
]
# A3-4 stone shapes once
shape=set()
for n in ['Solitaire ring','Halo ring','Three-stone ring']:
    _,_,k=K(n); sh=[t for t in k['t'] if t.lower().startswith('shape:')]
    shape.update(sh); k['t']=[t for t in k['t'] if t not in sh]
rd=D('Rings')
rd['b'].append({"m":"Stone shape","v":", ".join(sorted(t.split(':',1)[1].strip() for t in shape)),"w":"Declared once for all stone-set rings (solitaire, halo, three-stone, cluster, eternity) instead of repeated as types."})
rd['note']='Engagement rings by setting, everyday and designer bands by archetype; stone shape is one detail axis for the department (see criteria), not a kind or a repeated type.'
# A3-5 piercing ring
pi=K('Nose ring')[1]
pr=nk('Piercing ring','hoop · seamless ring · captive bead ring · clicker ring · nose ring · septum ring','Ring worn through a piercing; defined by its fastening and placed in a nostril, septum, ear or lip.','https://bodyjewelry.com/blog/whats-the-difference-between-a-captive-bead-ring-and-a-seamless-ring/')
pr['t']=['seamless (twist-open)','captive bead (CBR)','hinged segment clicker','septum retainer','placement: nose','placement: septum','placement: daith','placement: ear or lip']
pr['x']=copy.deepcopy(K('Nose ring')[2]['x'])+copy.deepcopy(K('Clicker ring')[2]['x'])
for n in ['Nose ring','Clicker ring','Seamless ring','Captive bead ring']: rm(n)
pi['k'].insert(3,pr)
# A3-6 parts
pt=D('Jewellery parts')['s'][0]
sp=nk('Spare parts','earring back · chain extender · ring guard','Replaceable bits owners swap in: earring backs, chain extenders and ring guards.','https://en.wikipedia.org/wiki/Earring')
sp['t']=['earring back (butterfly, screw, push)','chain extender','ring guard']
pt['k']=[sp]
# A3-7 hip-hop
_,_,nc=K('Necklace chain'); cu=rm('Cuban link chain'); ro=rm('Rope chain')
nc['x']+= [{**a} for a in cu['x']]
nc['x'].append({"n":"Cuban link","a":"Cuban chain · Cuban links","d":cu['d'],"mk":"","y":"","s":cu['s'],"v":[],"dt":"; ".join(cu['t'])})
nc['x'][-1]['v']=[{"n":a['n'],"d":a['d']} for a in nc['x'][-4:-1]]
nc['x']=nc['x'][:-4]+[nc['x'][-1]]
nc['x'].append({"n":"Rope chain","a":ro['a'],"d":ro['d'],"mk":"","y":"","s":ro['s'],"v":[{"n":a['n'],"mk":a.get('mk',''),"y":a.get('y',''),"d":a['d']} for a in ro['x']],"dt":"thickness · gold carat · diamond-cut or polished"})
_,_,pe=K('Pendant'); ip=rm('Iced-out pendant')
for a in ip['x']: a['dt']=(a.get('dt','')+' · iced-out pendant (hip-hop scene)').strip(' ·')
pe['x']+=ip['x']
gr=rm('Grillz')
hh=D('Hip-hop jewellery'); d['depts'].remove(hh)
hd=D('Hair & head jewellery'); hd['s'].append({"n":"Teeth","k":[gr]})
d['depts'] and None
nd=D('Necklaces & pendants'); nd['note']='Chain link patterns, including Cuban and rope chains, are archetypes of Necklace chain; tennis chains are on the Tennis necklace kind. Hip-hop pieces are tagged by scene in the brand register.'
hd['b']=hd.get('b',[])
# criterion from hip-hop dept kept
nd['b'].append(hh['b'][0])
json.dump(d,open('out/A3.tmp','w'),ensure_ascii=False,indent=1); os.replace('out/A3.tmp',P)
