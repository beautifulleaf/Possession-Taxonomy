import json,os,re,sys
sys.path.insert(0,'rebuild/work/GAP_E1')
P='rebuild/out/E1.json'
d=json.load(open(P))
K={}
for dp in d['depts']:
    for sh in dp['s']:
        for k in sh['k']: K[k['n']]=k
allx={}
for k in K.values():
    for e in k.get('x') or []: allx.setdefault(e['n'].lower(),e)
def add(kind,e):
    if e['n'].lower() in {x['n'].lower() for x in K[kind]['x']}: return False
    e.setdefault('a',''); e.setdefault('mk',''); e.setdefault('y',''); e.setdefault('v',[])
    K[kind]['x'].append(e); return True
n_add=0
# (a) toy soldiers
exec(open('rebuild/work/GAP_E1/ts.py').read().split("d=json.load")[0])
have={x['n'].lower() for k in K.values() for x in k.get('x') or []}
for n in names:
    if n.lower() in have or n=='Britains': continue
    add('Toy soldier & animal figure',{'n':n,'d':"Toy soldier brand named in Wikipedia's list of toy soldier brands.",'s':'https://en.wikipedia.org/wiki/List_of_toy_soldiers_brands','own':'owner not stated','tier':'Independent'}); n_add+=1
# (b) rail scales
R='https://en.wikipedia.org/wiki/Rail_transport_modelling_scales'
for n,dd,dt in[('Nn2','Scale 1:160 on 4.5 mm track (NMRA popular scales table).','1:160 · 4.5 mm'),('HOn30','Scale 1:87.1 on 9 mm track (NMRA popular scales table).','1:87.1 · 9 mm'),('HOm','Scale 1:87.1 on 12 mm track (NMRA popular scales table).','1:87.1 · 12 mm'),('Sn3','Scale 1:64 on 14.3 mm track (NMRA popular scales table).','1:64 · 14.3 mm')]:
    add('Model railway scale and gauge',{'n':n,'d':dd,'s':R,'dt':dt,'g':'NMRA popular scales'}); n_add+=1
# (c) puzzles
C='https://en.wikipedia.org/wiki/Combination_puzzle'
for n,dd in[("Rubik's Tower","2×2×4 cuboid puzzle named under non-uniform cuboids."),('Tower Cube',"2×2×3 cuboid puzzle named under non-uniform cuboids."),('Okamoto Cube','Non-uniform cuboid puzzle named in the article.'),('Siamese cubes','Pair of joined cube puzzles named in the article.'),('Fused cube','Non-uniform cuboid puzzle named in the article.'),('Void cube','Cube puzzle with the centre removed, named under non-uniform cuboids.'),('Crazy cube','Non-uniform cuboid puzzle of two types (I and II) named in the article.'),('Over The Top','17×17×17 cube, the largest named under non-uniform cuboids.')]:
    add('Cube twisty puzzle',{'n':n,'d':dd,'s':C,'g':'Cuboid · non-uniform'}); n_add+=1
for n,g,dd in[('Gigaminx','Dodecahedron · face-turning','Megaminx-type puzzle of larger order named in the article.'),('Teraminx','Dodecahedron · face-turning','Megaminx-type puzzle of larger order named in the article.'),('Petaminx','Dodecahedron · face-turning','Megaminx-type puzzle of larger order named in the article.'),('Orb-It','Sphere','Spherical puzzle named under non-Rubik-style three-dimensional puzzles.'),("Rubik's Triamid",'Other Rubik\'s-family puzzle',"Puzzle listed in the Rubik's Cube navigation box."),('Missing Link','Other Rubik\'s-family puzzle',"Puzzle listed in the Rubik's Cube navigation box and in Category:Mechanical puzzles."),("Rubik's Revolution",'Other Rubik\'s-family puzzle',"Handheld game listed in the Rubik's Cube navigation box.")]:
    add('Non-cube twisty puzzle',{'n':n,'d':dd,'s':C,'g':g}); n_add+=1
M='https://en.wikipedia.org/wiki/Mechanical_puzzle'; MC='https://en.wikipedia.org/wiki/Category:Mechanical_puzzles'
for kind,n,g,dd,s in[('Interlocking puzzle','Holey burr puzzle','Burr','Burr puzzle with holes, named under non-Rubik-style three-dimensional puzzles.',C),
 ('Sequential movement puzzle','Geranium','Sliding piece','Two-dimensional puzzle named in the Combination puzzle article.',C),
 ('Sequential movement puzzle','Puck puzzle','Sliding piece','Sliding puzzle listed in Category:Mechanical puzzles.',MC),
 ('Sequential movement puzzle','Hoppers','Solitaire','Peg-jumping game listed in Category:Mechanical puzzles.',MC),
 ('Put-together puzzle','Herzberger Quader','Three-dimensional assembly','Assembly puzzle listed in Category:Mechanical puzzles.',MC),
 ('Put-together puzzle','Egg of Columbus (mechanical puzzle)','Three-dimensional assembly','Mechanical puzzle listed in Category:Mechanical puzzles; the tangram puzzle of the same name is a separate entry.',MC),
 ('Put-together puzzle','Stave Puzzles','Makers','Puzzle maker listed in Category:Mechanical puzzles.',MC),
 ('Put-together puzzle','Artifact Puzzles','Makers','Puzzle maker listed in Category:Mechanical puzzles.',MC),
 ('Put-together puzzle','E.S.R., Inc.','Makers','Puzzle maker listed in Category:Mechanical puzzles.',MC),
 ('Disentanglement puzzle','Derringer puzzle','Wire','Disentanglement puzzle named in the Mechanical puzzle article.',M),
 ('Folding puzzle','Fold puzzle (Timonen)','Sheets and strips','Folding puzzle by Vesa Timonen, 2002, named in the Mechanical puzzle article.',M),
 ('Folding puzzle','Infinity cube','Hinged chain','Hinged-block cube listed in Category:Mechanical puzzles; also treated as a fidget.',MC),
 ('Dexterity puzzle','Hedgehog in the Cage','Other notable puzzles','Named under other notable mechanical puzzles in the Mechanical puzzle article.',M),
 ('Dexterity puzzle','Nintendo Ten Billion Barrel','Other notable puzzles','Named under other notable mechanical puzzles in the Mechanical puzzle article.',M),
 ('Dexterity puzzle','Nintendo Tumbler Puzzle','Other notable puzzles','Nintendo puzzle listed in Category:Mechanical puzzles.',MC)]:
    e={'n':n,'d':dd,'s':s,'g':g}
    if n.startswith('Fold puzzle'): e['y']='2002'
    if add(kind,e): n_add+=1
# (d) rod and connector
add('Rod-and-connector set',{'n':'Interlocking disks','d':"Struts of fixed but multiple lengths joined by nodes, named in Wikipedia's Construction set article.",'s':'https://en.wikipedia.org/wiki/Construction_set'}); n_add+=1
print('added',n_add)
# (e) sections for construction kinds
CS='https://en.wikipedia.org/wiki/Construction_set'
for e in K['Building brick set']['x']: e['g']='LEGO' if e['n']=='LEGO' else 'Other stud systems'
K['Building brick set']['xg']='by maker'
for e in K['Metal construction set']['x']: e['g']='Panels of varying sizes and shapes'
for e in K['Girder-and-panel set']['x']: e['g']='Struts and panels'
for e in K['Rod-and-connector set']['x']: e['g']='Variable-length struts' if e['n']=='Tesseract' else 'Fixed-length struts joined by nodes'
for e in K['Magnetic tile set']['x']: e['g']='Magnetic'
for e in K['Marble run']['x']: e['g']='Marble run systems'
for kn in('Metal construction set','Girder-and-panel set','Rod-and-connector set','Magnetic tile set','Marble run'):
    K[kn]['xg']='by connection method (as the Construction set article groups them)'
# (f) facts
F={ # name: (cty,y,own,own_y,tier)
'Sindy':('United Kingdom','1963','Pedigree Toys & Brands Limited',None,None),
'Teddy-Hermann':('Germany','1912',None,None,None),'Jellycat':('United Kingdom','1999',None,None,None),
'Cabbage Patch Kids':('United States','1978',None,None,None),'Pound Puppies':('United States','1984',None,None,None),
'Monchhichi':('Japan','1974',None,None,None),'Mariquita Pérez':('Spain',None,None,None,None),
'Annalee Dolls':('United States','1955',None,None,None),'Baby Alive':('United States','1973',None,None,None),
'Betsy Wetsy':('United States','1934',None,None,None),'Betty Spaghetty':('United States','1998',None,None,None),
'Chad Valley':('United Kingdom',None,None,None,None),'Flavas':('United States','2003',None,None,None),
'My Buddy':('United States','1985',None,None,None),'Götz':('Germany','1950',None,None,None),
'A Girl for All Time':('United Kingdom','2012',None,None,None),'Playpal':('United States','1959',None,None,None),
'Lottie Dolls':('Ireland','2012',None,None,None),'Vermont Teddy Bear Company':('United States','1983',None,None,None),
'Build-A-Bear Workshop':('United States','1997',None,None,None),'Care Bears':('United States',None,None,None,None),
'Webkinz':(None,'2005',None,None,None),'Cicciobello':('Italy',None,None,None,None),'Bukowski Design':('Sweden',None,None,None,None),
'Fischertechnik':('Germany','1964','Fischerwerke',None,None),'Cobi':('Poland','1987',None,None,None),
'Construx':('United States','1983',None,None,None),'Kre-O':('United States','2011',None,None,None),
'Rokenbok':('United States',None,None,None,None),'Tente':('Spain','1972',None,None,None),
'Meccano':('United Kingdom','1901','Spin Master',None,'Global group'),'Tinkertoy':('United States',None,'Hasbro',None,'Global group'),
'Anchor Stone Blocks':('Germany',None,None,None,None),'Merkur':('Czech Republic','1920',None,None,None),
'Kapla':(None,'1986',None,None,None),
'Hama beads':('Denmark','1971','Malte Haaning Plastic A/S',None,'Independent'),
}
def setf(e,cty,y,own,tier):
    if cty and not e.get('cty'): e['cty']=cty
    if y and not e.get('y'): e['y']=y
    if own and e.get('own') in (None,'','owner not stated'):
        e['own']=own; e['tier']=tier or e.get('tier') or 'Independent'
    if tier=='Global group' and own: e['tier']=tier
cnt=0
for k in K.values():
    for e in k.get('x') or []:
        if e['n'] in F:
            if k['n'] in('Metal construction set',) and e['n']=='Merkur': pass
            setf(e,*F[e['n']][:3],F[e['n']][4]); cnt+=1
print('facts applied',cnt)
# Lionel
for k in K.values():
    for e in k.get('x') or []:
        if e['n'].startswith('Lionel') and e.get('own') in(None,'','owner not stated'):
            e['own']='Lionel Brands Group'; e['own_y']='2026'; e['cty']=e.get('cty') or 'United States'; e['tier']='Independent'
# Hama description
for e in K['Fuse beads']['x']:
    if e['n']=='Hama beads':
        e['mk']='Malte Haaning Plastic A/S'; e['d']='Fusible pegboard beads made in Nykøbing Mors, Denmark, by Malte Haaning Plastic A/S (founded 1961); midi beads were introduced in 1971.'; e['s']='https://hama.dk/en/pages/the-story-of-hama'
for e in K['Marble']['x']:
    if e['n']=='Marble King marble':
        e['y']='1949'; e['mk']='Marble King'; e['cty']='United States'; e['d']='Marble maker founded in 1949 by Berry Pink and Sellers Peltier in St. Marys, West Virginia, and moved to Paden City after a January 1958 fire; the only remaining American toy marble maker.'; e['s']='https://wvencyclopedia.org/entries/1443'
for e in K['Put-together puzzle']['x']:
    if e['n']=='Katamino': e['d']='Polyomino-piece puzzle game designed by André Perriolat and published by Gigamic.'; e['s']='https://www.boardgamebliss.com/collections/andre-perriolat/products/katamino'
# market facts
d['depts'][0]['ms']=[{'mkt':'US toy sales by category','who':'Building sets','share':'+16 % in dollar sales','yr':2024,'s':'https://www.toyassociation.org/ta/PressRoom2/News/2025_News/circana-us-2024-toy-sales-remain-flat-moving-from-correction-to-consistency.aspx','note':'Circana figure; fastest-growing US toy category, led by LEGO Botanicals; no company shares published'}]
ms=d['depts'][2].setdefault('ms',[])
ms.append({'mkt':'US toy market','who':'All makers','share':'about US$42.0 billion, -0.3 %','yr':2024,'s':'https://www.toyassociation.org/ta/PressRoom2/News/2025_News/circana-us-2024-toy-sales-remain-flat-moving-from-correction-to-consistency.aspx','note':'Circana projection to the full market; outdoor and sports toys largest category at US$4.3 billion; the article names properties (Pokemon, Barbie, Marvel, Hot Wheels, Star Wars), not company shares'})
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
