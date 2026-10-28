import json,copy
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'C5.json'))
def loc(n):
    for di,dp in enumerate(d['depts']):
        for si,s in enumerate(dp['s']):
            for ki,k in enumerate(s['k']):
                if k['n']==n: return di,si,ki
def K(n):
    a,b,c=loc(n); return d['depts'][a]['s'][b]['k'][c]
def rm(n):
    a,b,c=loc(n); d['depts'][a]['s'][b]['k'].pop(c)
WP='https://en.wikipedia.org/wiki/Parker_Pen_Company'
cc=K('Cartridge-converter fountain pen')
cc['x'] += [
 {"n":"Parker 45","a":"","d":"Parker's cartridge-converter pen with a screw-in section, launched as the successor to the Parker 51 line's lower end.","mk":"Parker","y":"1960","s":WP,"v":[],"dt":"nib and finish variants · cartridge or converter"},
 {"n":"Parker 75","a":"","d":"Parker's sterling-silver-bodied cartridge-converter pen with a grip section that rotates to fit the hand.","mk":"Parker","y":"1964","s":WP,"v":[],"dt":"body finish · nib width"},
 {"n":"Jinhao X159","a":"","d":"Large resin pen with steel nib, styled on the Montblanc 149 and filled by converter.","mk":"Jinhao","y":"","s":"https://stridewise.com/jinhao-x159-fountain-pen-review/","v":[],"dt":"body colours · extra-fine or fine nib"}]
# fix definitions to what is sourced
cc['x'][-3]['d']="Parker's cartridge-converter pen of the early 1960s, listed among its key models."
cc['x'][-2]['d']="Parker's pen of the mid-1960s, listed among its key models."
keep={"Parker Sonnet","Parker Jotter","LAMY scala","Kaweco Perkeo","Waterman Carène","Waterman Expert","Platinum Plaisir","Conklin All American","Monteverde Prima","Pentel Tradio"}
cc['m']=[m for m in cc['m'] if m[0] in keep]
# vacuum kind: Wing Sung 601
K('Vacuum and plunger-filling fountain pen')['x'].append({"n":"Wing Sung 601","a":"","d":"Chinese-made pen modelled on the Parker 51, with a plunger under the blind cap and an ink window.","mk":"Wing Sung","y":"","s":"https://www.badgerandblade.com/forum/threads/for-parker-51-lovers-check-out-the-wing-sung-601.547191/","v":[],"dt":"body colours · steel nib"})
# C5-5
K('Fountain pen cartridge')['t']=["standard international (short, long)","proprietary","pigment cartridge"]
K('Pencil leads')['t']=["0.2–0.3 mm","0.5 mm","0.7 mm","0.9 mm and thicker","clutch-pencil (1.18–5.6 mm)","polymer-bound","colour"]
# merges
def merge(into,others,newname=None,alias=None,d_=None):
    k=K(into)
    for o in others:
        ok=K(o)
        k['t']=list(dict.fromkeys(k.get('t',[])+ok.get('t',[])))
        if ok.get('m'): k['m']=k.get('m',[])+ok['m']
        if ok.get('r'): k['r']=k.get('r',[])+ok['r']
        k['a']=' · '.join(x for x in dict.fromkeys([y for y in (k.get('a','')+' · '+ok.get('a','')+' · '+ok['n']).split(' · ') if y]) )
        rm(o)
    if newname: k['n']=newname
    if d_: k['d']=d_
merge('Whiteboard',['Noticeboard','Chalkboard'],'Wall board',d_="Board fixed to a wall or set on an easel for writing or pinning notes: dry-erase, cork or chalk.")
merge('Calendar',['Day-by-day calendar'])
merge('Folder',['Punched pocket'])
K('Wall board')['t']=["dry-erase (melamine, magnetic steel, glass)","cork or fabric noticeboard","chalkboard","mobile easel"]
# C5-3
cd=K('Calligraphy desk accessories')
cd['t']=[t for t in cd['t'] if not t.startswith('water dropper') and not t.startswith('paperweight')]
cd['a']="shitajiki · fudeoki"
cd['d']="Small tools laid out for brush calligraphy: felt underlay, brush rest, ink-stick rest and brush roll."
a,b,c=loc('Calligraphy desk accessories')
d['depts'][a]['s'][b]['k'][c+1:c+1]=[
 {"n":"Water dropper","a":"suiteki","d":"Small vessel with a spout and air hole that drips water onto an inkstone for grinding ink.","t":["ceramic","bronze","jade or stone","figural (animal, fruit)","antique"],"s":"https://takase.com/learn-japanese-calligraphy/lesson-1/"},
 {"n":"Scholar's paperweight","a":"bunchin","d":"Bar-shaped weight laid on calligraphy paper to hold it flat.","t":["pair of bars","brass","wood","stone or jade","antique"],"s":"https://en.wikipedia.org/wiki/Paperweight"}]
# C5-7 rename shelf
for dp in d['depts']:
    for s in dp['s']:
        if s['n']=='East Asian calligraphy: the Four Treasures': s['n']='Brushes, ink sticks & inkstones'
# C5-2
SRC_I='https://en.wikipedia.org/wiki/Inkwell'
desk=[dp for dp in d['depts'] if dp['n']=='Desk & filing supplies'][0]
desk['s'].insert(1,{"n":"Desk accessories & collectables","k":[
 {"n":"Inkwell","a":"inkpot · inkstand · inkhorn","d":"Small lidded container of glass, porcelain, silver, brass or pewter that holds ink for dip pens and refilling.","t":["glass","porcelain","silver or pewter","brass","travelling (screw lid)","antique (over 100 years)"],"s":SRC_I},
 {"n":"Letter opener","a":"paper knife","d":"Knife-like desk tool for slitting envelopes, with a blunt blade and often a decorative handle.","t":["steel","silver or pewter","wood","ivory-free handle","antique paper knife"],"s":"https://en.wikipedia.org/wiki/Letter_opener"}]})
# C5-6 seals dept
nb=[dp for dp in d['depts'] if dp['n']=='Notebooks, planners & paper'][0]
si=[i for i,s in enumerate(nb['s']) if s['n']=='Seals & stamps'][0]
seal=nb['s'].pop(si)
idx=d['depts'].index(nb)
d['depts'].insert(idx+1,{"n":"Seals, stamps & sealing wax","mode":"mixed","b":[],"s":[seal]})
json.dump(d,open(P+'C5.json.tmp','w'),ensure_ascii=False,indent=1)
b=json.load(open(P+'C5_brands.json'))
have={x['n'].lower() for x in b['b']}
new=[("Jinhao","China","1988","Value","Chinese pens","Chinese brand of Shanghai Qiangu Stationery, known for low-cost fountain pens such as the X159.",["X159"],"https://stridewise.com/jinhao-x159-fountain-pen-review/",["Jinhao X159"]),
("Hero","China","1931","Value","Chinese pens","Shanghai pen company, originally Wolff Pen Manufacturing Company; the Hero 616 and 100 resemble the Parker 51.",["Hero 616","Hero 100"],"https://en.wikipedia.org/wiki/Shanghai_Hero_Pen_Company",[]),
("Wing Sung","China","","Value","Parker 51 homage","Chinese pen brand whose 601 is a Parker 51-style plunger filler.",["601"],"https://www.badgerandblade.com/forum/threads/for-parker-51-lovers-check-out-the-wing-sung-601.547191/",["Wing Sung 601"])]
for n,c,f,seg,kf,dd,l,s,sig in new:
    assert n.lower() not in have
    b['b'].append({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":dd,"lines":l,"eras":[],"sig":sig,"sc":[],"rel":[],"s":s})
json.dump(b,open(P+'C5_brands.json.tmp','w'),ensure_ascii=False,indent=1)
