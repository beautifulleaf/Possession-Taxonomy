import json,copy
P='out/'
d=json.load(open(P+'B1.json')); br=json.load(open(P+'B1_brands.json')); mv=json.load(open(P+'B1_moves.json'))
def find(n):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==n: return dp,s,i,k
def remove(n):
    dp,s,i,k=find(n); s['k'].pop(i); return k
def addt(k,*ts):
    k.setdefault('t',[]); [k['t'].append(t) for t in ts if t not in k['t']]
cnt0={'kinds':sum(len(s['k']) for dp in d['depts'] for s in dp['s']),'arch':sum(len(k.get('x',[])) for dp in d['depts'] for s in dp['s'] for k in s['k'])}
# ---- B1-1/2 lounge split
dp,s,i,L=find('Lounge chair'); X={a['n']:a for a in L['x']}
def A(n,d_,mk,y,s_,v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s_,"v":v or [],"dt":dt}
def V(n,mk='',y='',d_=''): return {"n":n,"mk":mk,"y":y,"d":d_}
X['Paimio chair']['v']=[V('Artek production','Artek','','sold today as part of Artek\'s Representative Furniture')]
X['Tongue chair']['y']='1963'; X['Tongue chair']['v']=[V('Artifort original','Artifort','1963','Pierre Paulin; dated 1963 on the Artifort article, other sources differ')]
X['Mushroom chair']['v']=[V('Artifort original','Artifort','1959','developed for Artifort; in the MoMA permanent collection')]
X['Coconut chair']['v']=[V('Herman Miller original','Herman Miller','1955'),V('Current production','Herman Miller','','black leather only, without the matching ottoman')]
bkf=A('BKF chair','Bonet, Kurchan and Ferrari Hardoy\'s steel-rod frame holding a single sling seat, from Buenos Aires.','','1938','https://en.wikipedia.org/wiki/Butterfly_chair',
 [V('Argentine original','','1938','Grupo Austral; second prize at a 1940 exhibition'),V('Artek-Pascoe','Artek-Pascoe','early 1940s','New York production, slowed by wartime metal shortages'),V('Knoll production','Knoll','after 1945','US rights bought by Hans Knoll; stopped 1951 after losing an infringement case'),V('80th anniversary edition','Knoll','2018','Knoll re-release')],
 'sling: leather (original), canvas · black frame',a='Butterfly chair · Hardoy chair · Tripolina-type')
lcw=A('Eames LCW (Plywood Group lounge chair)','Charles and Ray Eames\'s moulded-plywood lounge chair on a wood frame, with separate seat and back.','Vitra','','https://www.nordicnew.nl/en/go/product/135230329',
 [V('LCW (Lounge Chair Wood)','Vitra','','68 cm high'),V('DCW (Dining Chair Wood)','Vitra','','72 cm high, same shells at dining height')],'ash or walnut veneer · natural or black stain · wood or metal frame',a='LCW · Lounge Chair Wood')
def Kn(n,d_,a,s_,order,extra):
    return {"n":n,"a":a,"d":d_,"s":s_,"x":[X[o] for o in order]+extra}
uph=Kn('Upholstered lounge chair','A designer easy chair whose comfort comes from padded, upholstered or sculpted seating on a wood or concealed frame.','easy chair · design lounge chair','https://en.wikipedia.org/wiki/Artifort',
 ['Eames Lounge Chair and Ottoman','Papa Bear chair','CH25','Ox chair','Safari chair','Mushroom chair','Tongue chair','Ribbon chair'],[])
upl_m=L.get('m',[]); uph['m']=upl_m
tub=Kn('Tubular & wire-frame lounge chair','A designer lounge chair built on a bent steel tube, rod or wire frame, with a sling, cushions or wire seat.','steel-frame lounge chair','https://en.wikipedia.org/wiki/Butterfly_chair',
 ['Wassily Chair','Grand Confort (LC2 / LC3)','Barcelona chair'],[bkf]+[]); 
tub['x']+= [X['Diamond chair'],X['Platner chair']]
mou=Kn('Moulded, shell & bentwood lounge chair','A designer lounge chair whose form comes from a moulded shell, bent plywood or bentwood, or shaped wood.','shell chair · plywood lounge chair','https://en.wikipedia.org/wiki/Paimio_Chair',
 ['Paimio chair','Red and Blue Chair','Egg chair','Swan chair','Womb chair','Ball chair','Coconut chair','Shell chair'],[lcw])
dp['s'][0]  # noop
s['k'][i:i+1]=[uph,tub,mou]
assert len(uph['x'])+len(tub['x'])+len(mou['x'])==21+2, (len(uph['x']),len(tub['x']),len(mou['x']))
# B1-2 other icons
dp,s,i,arm=find('Armchair')
arm['x'].append(A('Chandigarh chair','Pierre Jeanneret and Eulie Chowdhury\'s wood and cane easy armchair made for the public buildings of Chandigarh.','','1950s','https://en.wikipedia.org/wiki/Chandigarh_chair',
 [V('Original Chandigarh production','','1950s','teak or other wood with woven cane, made in the city\'s workshops'),V('Easy armchair, cane and teak','','c. 1955/56','example in the Vitra Design Museum collection'),V('Later reproductions','','','no exclusive licence exists, so many studios make versions')],'wood: teak · cane or leather · armchair or office form · original or reproduction',a='Jeanneret chair · Pierre Jeanneret easy chair'))
dp,s,i,din=find('Dining chair')
din['x'].append(A('Standard chair','Jean Prouvé\'s steel and wood chair with heavy hollow rear legs carrying the load and lighter front legs.','Vitra','','https://www.connox.com/products/vitra-prouve-standard-sp-chair',
 [V('Standard SP','Vitra','','steel frame with shaped seat and backrest')],'frame finishes: warm grey, Japanese red, Prouvé Gris Vermeer, Bleu Dynastie, Bleu Marcoule, Blé Vert, basalt · seat colour',a='Prouvé Standard'))
din['x'].append(A('Cherner chair','Norman Cherner\'s moulded plywood chair with a sculpted seat and back, made in walnut-veneered laminated plywood.','Cherner Chair Company','1958','https://www.houzz.co.uk/ideabooks/34743058/thumbs/iconic-designs-the-cherner-chair-and-armchair-by-norman-cherner',
 [V('Plycraft production','Plycraft','1958','made after Cherner sued in 1961 with royalties and credit; continued to the early 1970s'),V('Cherner Chair Company reissue','Cherner Chair Company','1999','founded by his sons Benjamin and Thomas; built to his drawings'),V('Armchair','Cherner Chair Company','','arms; also used as an office chair'),V('Bar stool','Cherner Chair Company','','')],'ten finishes · armless chair, armchair or bar stool',a='Rockwell chair'))
dp,s,i,side=find('Side table')
side['x'].append(A('Adjustable Table E 1027','Eileen Gray\'s height-adjustable steel and glass side table, made for her E-1027 house.','','1927','https://en.wikipedia.org/wiki/Adjustable_Table_E_1027',
 [V('Original for the E-1027 house','','1927','stainless steel and tempered glass'),V('Zeev Aram edition','Zeev Aram','','Gray sold the design to the British maker Aram before she died')],'height 54–93 cm · frame finish · glass top',a='E1027 table · Eileen Gray table'))
# ---- B1-4 IKEA trimming
trim=0
for dpp in d['depts']:
  for ss in dpp['s']:
    for k in ss['k']:
        mm=k.get('m') or []; rr=k.get('r') or []
        mnames={t[0].lower() for t in mm}
        n0=len(mm)+len(rr)
        rr=[t for t in rr if t[0].lower() not in mnames]
        out={'m':[], 'r':[]}; ik=0
        for key,lst in (('m',mm),('r',rr)):
            for t in lst:
                if t[1]=='IKEA':
                    ik+=1
                    if ik>2: continue
                out[key].append(t)
        trim+=n0-len(out['m'])-len(out['r'])
        for key in ('m','r'):
            if out[key]: k[key]=out[key]
            else: k.pop(key,None)
# ---- B1-5
find('Dressing table')[3].pop('m',None)
# ---- B1-6 folds
def fold(src,dst,typ):
    remove(src); addt(find(dst)[3],typ)
fold('Slipper chair','Armchair','slipper chair (low, armless, upholstered)')
c=remove('Club chair'); addt(find('Armchair')[3],'club chair (deep, low, leather; round, square, cloud or moustache back)')
find('Armchair')[3]['a']+=' · club chair · fauteuil club'
fold('Locker','Storage cabinet','locker (tall narrow lockable cupboard)')
fold('Umbrella stand','Coat rack','umbrella stand')
fold('Magazine rack','Bookcase','magazine rack')
remove('Chair bed'); sb=find('Sofa bed')[3]; addt(sb,'chair bed (single armchair that unfolds into a bed)')
remove('Futon sofa'); addt(sb,'futon frame (wooden or metal, with or without mattress)'); sb['a']+=' · futon sofa · futon frame'
# ---- B1-8
gc=find('Gaming chair')[3]; gc['t']=[t for t in gc['t'] if t not in('force-feedback chair','simulator cockpit seat')]
gt=find('Game table')[3]; gt['t']=[t for t in gt['t'] if t not in('poker table','convertible pool-dining table')]
mv['out']+= [
 {"to":"E5","dept":"Controllers","kind":{"n":"Sim racing seat","a":"simulator cockpit seat · racing simulator seat · force-feedback seat","d":"A seat modelled on a real racing seat, mounted to a cockpit frame, giving a fixed driving position for a wheel and pedals.","t":["GT and touring car seat","Formula seat","rally seat","force-feedback (motion) seat"],"s":"https://shop.germansimracing.de/en/blogs/info/sim-racing-sitz","m":[],"r":[]}},
 {"to":"E1","dept":"Board, card & table games","kind":{"n":"Poker table","a":"card table · games table","d":"A table built for card games, covered in baize or speed cloth, often with a padded rail; antique card tables fold.","t":["oval","round","octagonal","fold-out","convertible pool-dining top","antique fold-over card table"],"s":"https://en.wikipedia.org/wiki/Poker_table","m":[],"r":[]}}]
# nursery dept
idx=[j for j,x in enumerate(d['depts']) if x['n']=='Beds & mattresses'][0]
bd=d['depts'][idx]; ns=[s for s in bd['s'] if s['n']=='Nursery furniture'][0]; bd['s'].remove(ns)
d['depts'].insert(idx+1,{"n":"Nursery & children's furniture","mode":"mixed","note":"Cots, high chairs and other furniture for babies and small children.","s":[ns]})
# ---- B1-9
sofa=find('Sofa')[3]
sofa['t']=[t for t in sofa['t'] if t not in('Art Deco','mid-century modern','leather','fabric','velvet')]
sofa['dt']='cover: leather, fabric, velvet · period: Art Deco, mid-century modern'
# ---- B1-7 Gillows
b=br['b']; g=[x for x in b if x['n']=='Gillows'][0]; g2=[x for x in b if x['n']=='Gillows of Lancaster and London'][0]
g['d']='Lancaster and London cabinetmakers credited with the original Davenport desk; made a bureau bedstead in 1788.'
g['sig']=g['sig']+g2['sig']; b.remove(g2)
txt=json.dumps(d,ensure_ascii=False).replace('"mk": "Gillows of Lancaster and London"','"mk": "Gillows"'); d=json.loads(txt)
# ---- B1-3 brands
def B(n,c,f,kf,dd,s_,sig=()):
    b.append({"n":n,"c":c,"f":f,"seg":"Premium","d":dd,"sig":list(sig),"s":s_,"kf":kf})
B('Fredericia','Denmark','1911','Danish modern','Danish furniture maker founded as a chair factory; long associated with Børge Mogensen.','https://connox.com/fredericia.html',['J39 Mogensen chair'])
B('Molteni&C','Italy','1934','Italian design','Giussano furniture maker that grew from an artisan workshop; Compasso d\'Oro career award 1994.','https://www.molteni.it/nl/eu/landing/molteni-mondo-history')
B('Minotti','Italy','1948','contemporary sofas','Furniture maker for homes and hospitality, with Rodolfo Dordoni as art director since 1998.','https://www.minotti.com/en/profile')
B('Cappellini','Italy','1946','design talent','Furniture maker that launched young designers such as Jasper Morrison and Marc Newson; part of Haworth.','https://collection.design-museum.de/en/artists/artist/8236/',['Flower Pot','Thinking Man\'s Chair'])
B('Moroso','Italy','1952','experimental design','Udine upholstery maker turned design brand; Ron Arad\'s Big Easy Chair launched it in 1988.','https://www.pamono.com/makers/moroso',['Big Easy Chair'])
B('&Tradition','Denmark','2010','Danish design reissues','Copenhagen brand mixing reissued mid-century classics with new designs.','https://www.skandium.com/pages/tradition-details',['Mayor sofa','Flowerpot lamp'])
b.append({"n":"Cherner Chair Company","c":"United States","f":"1999","seg":"Specialist","d":"Founded by Norman Cherner's sons; sole licensor of his chair designs.","sig":["Cherner chair"],"s":"https://www.houzz.co.uk/ideabooks/34743058/thumbs/iconic-designs-the-cherner-chair-and-armchair-by-norman-cherner","kf":"plywood chairs"})
cnt1={'kinds':sum(len(s['k']) for dp in d['depts'] for s in dp['s']),'arch':sum(len(k.get('x',[])) for dp in d['depts'] for s in dp['s'] for k in s['k'])}
print(cnt0,cnt1,'trimmed',trim)
for f,o in (('B1',d),('B1_brands',br),('B1_moves',mv)):
    json.dump(o,open(P+f+'.tmp','w'),ensure_ascii=False,indent=1); 
import os
for f in ('B1','B1_brands','B1_moves'): os.replace(P+f+'.tmp',P+f+'.json')
