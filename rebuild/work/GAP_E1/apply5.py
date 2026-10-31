import json,os,re
B='rebuild/work/GAP_E1/'
P='rebuild/out/E1.json'
d=json.load(open(P))
F=json.load(open(B+'facts.json')); F.update({k:{**F.get(k,{}),**v} for k,v in json.load(open(B+'facts_b.json')).items()})
manual={}
for n in['Kato Unitrack starter set','Kato C62','Kato EMD E5A "Silver Speed"','Kato Unitrack']: manual[n]={'cty':'Japan'}
manual['Fleischmann piccolo']={'cty':'Germany'}
for n in['Peco Streamline','Peco Setrack']: manual[n]={'cty':'United Kingdom'}
manual['Woodland Scenics scenery']={'cty':'United States'}
manual['Team Associated RC10']={'cty':'United States','own':'Thunder Tiger'}
manual['Duncan yo-yo']={'cty':'United States'}
manual['Bruder 1:16 vehicles']={'cty':'Germany'}
manual['Schoenhut toy piano']={'cty':'United States'}
manual['Brunswick air hockey table']={'cty':'United States'}
manual['Super Soaker']={'cty':'United States','own':'Hasbro'}
manual['Graham Farish N']={'cty':'United Kingdom','own':'Bachmann Industries','own_y':'2000'}
F.update({k:{**F.get(k,{}),**v} for k,v in manual.items()})
G={'Mattel','Hasbro','Bandai Namco Holdings','Simba Dickie Group'}
K={}
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']: K[k['n']]=k
applied=0
for k in K.values():
    for e in k.get('x') or []:
        f=F.get(e['n'])
        if e['n'].startswith('Märklin') and not e.get('cty'): f={**(f or {}),'cty':'Germany'}
        if not f: continue
        applied+=1
        if f.get('cty') and not e.get('cty'): e['cty']=f['cty']
        if f.get('y') and not e.get('y'): e['y']=f['y']
        o=f.get('own')
        if o and e.get('own') in(None,'','owner not stated'):
            e['own']=o; e['tier']='Global group' if o in G else (e.get('tier') or 'Independent')
            if f.get('own_y'): e['own_y']=f['own_y']
print('applied',applied)
# additions
def add(kind,e):
    if e['n'].lower() in {x['n'].lower() for x in K[kind]['x']}: return
    for a,b in(('a',''),('mk',''),('y',''),('v',[])): e.setdefault(a,b)
    K[kind]['x'].append(e)
add('Magnet sphere set',{'n':'NeoCube','d':'Set of small neodymium magnet spheres or cubes, sold in different regions as Buckyballs, Nanodots or NeoMagnets.','s':'https://ruwix.com/twisty-puzzles/neo-cubes-magnetic-balls-puzzle/'})
CE='https://ruwix.com/twisty-puzzles/electronic-rubiks-cube-puzzles/'
for n,dd,y in[('Giiker Cube','Smart cube described as the first that connects to a smartphone through Bluetooth and an app.',''),("Rubik's Touch",'Rubik\'s Cube that uses pseudo-touchscreens to control movement.',''),('Futuro Cube','Cube with touch and motion sensors inside.',''),("Rubik's Spark",'Electronic cube-style puzzle presented in 2016.','2016')]:
    add('Cube twisty puzzle',{'n':n,'d':dd,'s':CE,'y':y,'g':'Cube · smart'})
R='https://en.wikipedia.org/wiki/Lima_(models)'
add('Model rolling stock',{'n':'Lima','d':'Italian maker of model railways, founded in Vicenza in 1946; Hornby bought its assets and brands in 2004.','s':R,'mk':'Lima','y':'1946','cty':'Italy','own':'Hornby Railways','own_y':'2004','tier':'Independent',
 'v':[{'n':'OO gauge range','mk':'Lima','y':'1977','d':'British-outline range adopted in 1977.'},{'n':'Class 50 Thunderer','mk':'Lima','y':'','d':'Limited edition locomotive, mid-1990s.'},{'n':'Class 67','mk':'Lima','y':'2000','d':'Updated model, early 2000.'},{'n':'Tuborg and Carlsberg beer wagons','mk':'Lima','y':'','d':'Scandinavian wagon models.'},{'n':'Australian ranges','mk':'Lima','y':'','d':'NSW, Victorian and South Australian locomotives and Commonwealth Railways stainless steel carriages.'},{'n':'American N scale equipment','mk':'Lima','y':'','d':'Diesel locomotives, heavyweight passenger cars, freight cars and a caboose.'}]})
add('Model rolling stock',{'n':'Roco','d':'Austrian maker of model railways in Salzburg, founded in 1960 by Heinz Rössler; the company went bankrupt in 2005 and Modelleisenbahn GmbH took it over. The page names no rolling-stock series.','s':'https://en.wikipedia.org/wiki/Roco_(model_railroads)','mk':'Roco','y':'1960','cty':'Austria','own':'Modelleisenbahn GmbH','tier':'Independent',
 'v':[{'n':'Lionel HO trains','mk':'Roco','y':'1974','d':'Made by Roco in 1974 and 1975 before production moved to the Far East.'}]})
# sections
norm={'USA':'United States','UK':'United Kingdom','Korea':'South Korea'}
for kn in('Scale model kit','Die-cast model','Toy soldier & animal figure','Fashion doll','Teddy bear'):
    k=K[kn]
    for e in k['x']:
        g=e.get('g')
        if kn=='Toy soldier & animal figure' or kn in('Fashion doll','Teddy bear'):
            e['g']=e.get('cty') or 'Country not stated'
        else:
            g=norm.get(g,g)
            if g in(None,'Country not stated','Other makers','Founding lines') and e.get('cty'): g=e['cty']
            elif g in(None,): g='Country not stated'
            e['g']=g
    k['xg']="by maker's home country"
    ys=lambda e:(re.match(r'\d{4}',e.get('y') or '') and int(re.match(r'\d{4}',e['y']).group())) or 9999
    k['x'].sort(key=lambda e:(e['g'] in('Country not stated','Other makers'), e['g'], ys(e), e['n'].lower()))
ts=K['Toy soldier & animal figure']
ts['sel']=ts['sel'].replace("The list gives no country or year, so those fields are empty.","The list gives no country or year; countries come from the makers' own Wikipedia pages where one exists, otherwise 'Country not stated'.")
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
import collections
for kn in('Scale model kit','Die-cast model','Toy soldier & animal figure'):
    c=collections.Counter(e['g'] for e in K[kn]['x']); print(kn,len(c),c.get('Country not stated'),c.get('Other makers'))
