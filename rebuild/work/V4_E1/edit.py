import json, copy, os, sys
ROOT='/home/user/Possession-Taxonomy/rebuild/'
P=ROOT+'out/E1.json'
d=json.load(open(P))
renames={}
CS='https://en.wikipedia.org/wiki/Construction_set'
CC='https://en.wikipedia.org/wiki/Combination_puzzle'
MP='https://en.wikipedia.org/wiki/Category:Mechanical_puzzles'
MPC='https://en.wikipedia.org/wiki/Category:Mechanical_puzzle_cubes'
SL='https://www.woodpuzzles.com/puzzles_class_slocum.html'
RP='https://robspuzzlepage.com/classif2.htm'

def V(n,d_='',mk='',y=''): return {'n':n,'mk':mk,'y':y,'d':d_}
def E(n,d_,s,mk='',y='',a='',v=None,dt='',g=None,role=None):
    e={'n':n,'a':a,'d':d_,'mk':mk,'y':y,'s':s,'v':v or []}
    if dt: e['dt']=dt
    if g: e['g']=g
    if role: e['role']=role
    return e

def dept(name):
    return [x for x in d['depts'] if x['n']==name][0]
def kind(name):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==name: return k
    raise KeyError(name)
def take(name):
    """remove and return kind"""
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==name:
                    return s['k'].pop(i)
    raise KeyError(name)
def ent(kn,en):
    for e in kind(kn).get('x',[]):
        if e['n']==en: return e
    raise KeyError(en)
def K(n,d_,a='',s='',x=None,nl='',sel='',xg='',tt=None):
    k={'n':n,'a':a,'d':d_}
    if s: k['s']=s
    if tt: k['tt']=tt
    if x is not None:
        k['x']=x; k['nl']=nl; k['sel']=sel
        if xg: k['xg']=xg
    return k
def S(n,t,ax,ks):
    s={'n':n,'t':t}
    if ax: s['ax']=ax
    s['k']=ks
    return s
def setx(k,x,nl,sel,xg=''):
    k['x']=x; k['nl']=nl; k['sel']=sel
    if xg: k['xg']=xg
    else: k.pop('xg',None)
    k.pop('m',None); k.pop('r',None)

# ---------------------------------------------------------------- BUILDING
B=dept('Building & construction')
brick=take('Building brick set'); mini=take('Minifigure')
wood=take('Wooden construction set'); metal=take('Metal construction set')
rod=take('Rod-and-connector set'); mag=take('Magnetic tile set'); marble=take('Marble run')
renames['Minifigure']='Building brick set'

lego=E('LEGO','Danish brick system whose plastic bricks clip together by studs and tubes; the brand stands for itself, and its sets, themes and minifigures are catalogued at Brickset (https://brickset.com).',
 'https://en.wikipedia.org/wiki/Lego',mk='LEGO',y='1949',a='LEGO System',
 v=[V('LEGO System','Standard bricks; the studded brick was first sold as Automatic Binding Bricks in 1949, and the patent for the modern brick design was filed in Denmark on 28 January 1958.','LEGO','1949'),
    V('Duplo','Bricks whose lengths measure twice the width, height and depth of standard LEGO bricks, aimed at younger children.','LEGO','1969'),
    V('Technic','Line for emulating complex machinery, with pinned beams as well as studs.','LEGO','1977')],
 dt='system (standard, Duplo, Technic) · catalogue at Brickset',role='landmark')
# role only if a fetched page says best-selling/defining: construction-set article names Lego first among stud makers; keep no badge
lego.pop('role')
studs=[lego]
for n,dd in [('Mega Bloks','Studded building blocks from Mega Brands, listed in the Construction set article among the stud-joined systems.'),
 ('Cobi','Polish studded building blocks, listed among the stud-joined systems.'),
 ('Kre-O','Studded building system listed among the stud-joined systems.'),
 ('Loc Blocs','Studded building blocks listed among the stud-joined systems.'),
 ('Engino','Studded building system listed among the stud-joined systems.'),
 ('Rokenbok','Studded building system listed among the stud-joined systems.'),
 ('Coco','Studded building blocks listed among the stud-joined systems.'),
 ('Rasti','Studded building blocks listed among the stud-joined systems.'),
 ('Tente','Studded building system listed among the stud-joined systems.'),
 ('Betta Builda','Studded building system listed among the stud-joined systems.'),
 ('Oxford','Studded building blocks listed among the stud-joined systems.'),
 ('Clementoni mechanics','Studded mechanical building sets listed among the stud-joined systems.'),
 ('Fischertechnik','Technical building system listed among the stud-joined systems.')]:
    studs.append(E(n,dd,CS))
studs.append(E('Guangdong Loongon','Chinese maker of studded blocks, listed with its Cogo, Lepin and Xingboa brands.',CS,v=[V('Cogo','','Guangdong Loongon'),V('Lepin','','Guangdong Loongon'),V('Xingboa','','Guangdong Loongon')]))
setx(brick,studs,'One entry is a studded building-brick system sold under its own name; its sizes and technical ranges are versions, and its sets, themes and licences are not listed.',
 "Every maker that Wikipedia's Construction set article lists under the stud connection method, with LEGO at its systems (System, Duplo, Technic); LEGO sets and themes are left to Brickset.",'by maker')
brick['d']='A set of plastic bricks that clip together by studs and tubes, sold loose or as a model.'
# keep tt
# nut-and-bolt
metal_x=[ent_ for ent_ in metal['x']]
mx=[E('Mini Unit Beams','Panel-and-beam building set joined by pins or screws set perpendicular to the panel faces.',CS),
    E('Merkur','Perforated-strip building system joined by pins or screws.',CS),
    E('Steel Tec','Metal strip building system joined by pins or screws.',CS),
    E('Trix','Metal strip building system joined by pins or screws.',CS),
    E('FAC-System','Panel building system joined by pins or screws.',CS),
    E('Constructo Straws','Panel and strip building system joined by pins or screws.',CS),
    E('Überstix','Strip building system joined by pins or screws.',CS)]
setx(metal,metal_x+mx,'One entry is a building system whose strips or panels are joined by bolts, pins or screws, sold under its own name; outfit sizes and motorised sets are versions.',
 "Meccano and Erector Set from the earlier pass, plus every system that Wikipedia's Construction set article lists under panels joined by pins or screws set perpendicular to the panel faces.",'by maker')
girder=K('Girder-and-panel set','A set of girders and panels that bolt or clip together into buildings and frames.','girder and panel building set',CS,
 [E('Girder and Panel building sets','The article names these as a class of struts and panels combined into one system.',CS),
  E('Synestructics','Strut-and-panel building system.',CS),
  E('Ramagon','Strut-and-panel system; some panels have studs for LEGO-type clones.',CS),
  E('Bayko','Strut-and-panel building system.',CS),
  E('Construx','Strut-and-panel building system.',CS)],
 'One entry is a building system that combines struts and panels, sold under its own name.',
 "Every system that Wikipedia's Construction set article lists under struts and panels combined, except Geomag (magnetic).",'by maker')
# rod and connector
rx=rod['x']+[E('Playskool Pipeworks','Fixed-length struts joined at nodes.',CS),
  E('Cleversticks','Fixed-length struts joined at nodes.',CS),
  E('Zometool','Struts joined at icosahedral-symmetry nodes.',CS),
  E('Tesseract','Variable-length struts whose connection points start flexible and can be made rigid with clips.',CS)]
setx(rod,rx,'One entry is a building system of rods or struts joined at connectors, sold under its own name.',
 "Tinkertoy and K'Nex from the earlier pass, plus every system that Wikipedia's Construction set article lists under struts joined at nodes or variable-length struts.",'by maker')
# magnetic
mag['x']=mag['x']
setx(mag,mag['x'],'One entry is a building system whose parts join by magnets, sold under its own name.',
 "Magna-Tiles and Geomag from the earlier pass; Wikipedia's Construction set article names Geomag as the magnetic strut-and-panel system and gives no other named magnetic system.",'by maker')
# stacking
wx=wood['x']
for e in wx:
    e['g']='No connection (stacking)'
wx+= [E('Toy blocks','Plain building blocks with no connection between them.',CS,g='No connection (stacking)'),
      E('Lincoln Logs','Logs joined by notches; invented by John Lloyd Wright.',CS,mk='Lincoln Logs',a='',g='Notches'),
      E('GIK','Notched building pieces.',CS,g='Notches'),
      E('Stickle Bricks','Bricks that join by notches.',CS,g='Notches')]
setx(wood,wx,'One entry is a building system whose parts rest on one another or lock by notches, sold under its own name or as a tradition.',
 "Every system that Wikipedia's Construction set article lists under no connection or notches, with the Fröbel gifts and unit blocks from the earlier pass.",'by connection')
hinge=K('Hinged-panel and sleeve set','Panels joined by hinges, or parts joined by sleeves, into shapes and models.','',CS,
 [E('Tog\'l','Panels with flexible hinges between them.',CS,g='Hinged panels'),
  E('Jovo Click \'N Construct','Panels with flexible hinges between them.',CS,g='Hinged panels'),
  E('Zaks','Panels with flexible hinges between them.',CS,g='Hinged panels'),
  E('Polydron','Panels with flexible hinges between them.',CS,g='Hinged panels'),
  E('Capsela','Building parts joined by sleeves.',CS,g='Sleeves')],
 'One entry is a building system of hinged panels or sleeved parts, sold under its own name.',
 "Every system that Wikipedia's Construction set article lists under panels with flexible hinges or sleeves.",'by connection')
for k in [mini]: pass
# marble run
marble['nl']='One entry is a marble-run system sold under its own name; its starter and expansion sets are versions.'
marble['sel']="No whole-space reference exists for marble runs. Wikipedia's Construction set article describes the category without naming systems, so the entries are those found in the earlier pass and not yet checked against a list."
marble['xg']='by maker'
marble.pop('m',None); marble.pop('r',None)

robots=B['s'][2:]  # robots & coding, craft shelves
B['s']=[
 S('Stud-and-tube systems','Bricks and blocks that clip together by studs: LEGO and the systems listed beside it; rods → Rod-and-connector systems.','',[brick]),
 S('Nut-and-bolt systems','Strips, girders and panels fixed with pins, bolts or screws, from Meccano to girder-and-panel sets.','kinds by what is bolted: strips and beams, girders and panels',[metal,girder]),
 S('Rod-and-connector systems','Rods or struts pushed into connectors to form frames, from Tinkertoy to Zometool.','',[rod]),
 S('Magnetic systems','Tiles and bars that hold together by magnets.','',[mag]),
 S('Stacking & notch systems','Blocks that rest on one another or lock by notches, from Fröbel gifts to Lincoln Logs.','',[wood]),
 S('Hinge & sleeve systems','Panels joined by hinges, or parts joined by sleeves.','',[hinge]),
 S('Marble runs','Track pieces that guide a marble down a run built by the child.','',[marble]),
]+robots
B['t']='Toys sold as parts to join into something, sorted by how the parts connect: studs, bolts, rods, magnets, stacking, hinges; robots, coding toys and craft materials follow. A finished model → Models, kits & railways, a puzzle with one answer → Puzzles shelf.'
B['ax']='How are the parts joined: studs and tubes, nuts and bolts, rods and connectors, magnets, stacking, or hinges?'
B['note']='Brands with their own catalogue stand for themselves: LEGO is one entry with versions only for its systems, and its sets and themes are catalogued at Brickset.'
# strip content from Coding toy: LEGO Mindstorms/Boost are systems; keep. m dropped
kc=kind('Coding toy'); kc.pop('m',None)

# ---------------------------------------------------------------- PLAYMOBIL
pm=ent('Playset','Playmobil')
pm.update({'d':'German figure-and-building toy system with 7.5 cm figures at 1:24 scale; the brand stands for itself and its sets and themes are not listed.','mk':'Geobra Brandstätter','y':'1974',
 'v':[V('Steck-System','Original building system using tabs and slots; retired except for special reissues.','Geobra Brandstätter',''),
      V('System-X','Current standard building system: no tabs, small connector pieces and a special tool.','Geobra Brandstätter',''),
      V('Playmobil 1.2.3 / Junior','Sets and figures for children aged three and under.','Geobra Brandstätter',''),
      V('Playmobil Pro','White, simplified figures; available in the US from January 2020.','Geobra Brandstätter','2020')],
 'dt':'building system · figure line'})

# ---------------------------------------------------------------- HOT WHEELS
hw=ent('Die-cast model','Hot Wheels')
hw.update({'d':'Mattel\'s 1:64 toy cars, launched on 18 May 1968; the brand stands for itself and its castings and series are not listed.','y':'1968',
 'v':[V('Mainline 1:64','The mainstream car, about US$1.25 by the mid-2020s.','Mattel','1968'),
      V('Gran Toros 1:43','Larger 1:43 cars.','Mattel','1970'),
      V('Sizzlers','Battery-powered cars with a built-in motor.','Mattel','1970'),
      V('HIN, G-Machines and Customs','Slightly larger, more detailed models.','Mattel','2004'),
      V('Premium 1:64 (Car Culture)','Metal body and base, priced six to seven times a mainstream car.','Mattel','2016'),
      V('Elite and replica models','Detailed 1:18, 1:43 and 1:50 models, mostly licensed Ferraris.','Mattel','')],
 'dt':'scale · body material'})
kind('Die-cast model').pop('m',None)

# ---------------------------------------------------------------- FUNKO
vk=kind('Vinyl collectible figure')
vk['x']=[e for e in vk['x'] if e['n'] not in('Funko Pop!','Funko Vinyl Soda','Funko Mystery Minis')]
vk['x'].insert(0,E('Funko','Collectibles company founded in 1998 by Mike Becker; the brand stands for itself and its licences and character figures are not listed.',
 'https://en.wikipedia.org/wiki/Funko',mk='Funko',y='1998',
 v=[V('Pop! vinyl','Large-headed, small-bodied figures with round black eyes; line created 2010, revealed 2011, in 6, 10 and 18 inch sizes.','Funko','2010'),
    V('Vinyl Soda','Figures packed in a soda-can-style tin.','Funko',''),
    V('Mystery Minis','Blind-boxed figures styled differently from other Funko products.','Funko',''),
    V('Bitty Pop!','One-inch miniatures sold in an acrylic case; announced January 2023.','Funko','2023')],
 dt='format'))
vk['nl']='One entry is a collectible-figure brand that runs its own catalogue; its physical formats are versions and its characters are not listed.'
vk['sel']="Funko from Wikipedia's Funko article; the other entries are the designer-vinyl lines found in the earlier pass. No whole-space reference exists."
vk.pop('m',None)

# ---------------------------------------------------------------- WARHAMMER
ms=kind('Miniatures game starter set')
ms['x']=[e for e in ms['x'] if e['n'] not in('Warhammer 40,000','Warhammer Age of Sigmar')]
ms['x'].insert(0,E('Warhammer','British tabletop miniatures wargame first published by Games Workshop in 1983; the brand stands for itself and its armies, factions and models are not listed.',
 'https://en.wikipedia.org/wiki/Warhammer_(game)',mk='Games Workshop',y='1983',
 v=[V('Warhammer Fantasy Battle','The original medieval fantasy game; replaced by Age of Sigmar in 2015.','Games Workshop','1983'),
    V('Warhammer 40,000','Science-fiction counterpart; precursor Rogue Trader released in 1987.','Games Workshop','1987'),
    V('Warhammer Age of Sigmar','Replaced Warhammer Fantasy Battle in 2015 and reused its models in a new setting.','Games Workshop','2015'),
    V('Warhammer: The Old World','Reboot with a rules base like earlier editions; released 20 January 2024.','Games Workshop','2024')],
 dt='game system · miniature scale (28 mm standard)',role='origin'))
ms['nl']='One entry is a miniatures game sold under its own name, or a brand with its own catalogue; its game systems and editions are versions.'
ms['sel']="Warhammer from Wikipedia's Warhammer (game) article; Bolt Action and X-Wing from the earlier pass. No whole-space reference exists."

# ---------------------------------------------------------------- PUZZLES
PZ=dept('Puzzles, fidgets & desk toys')
jig=PZ['s'][0]
for k in jig['k']:
    k.pop('m',None); k.pop('r',None)
jp=kind('Jigsaw puzzle')
jp['nl']='One entry is a jigsaw tradition or puzzle brand, not a picture; sizes and cuts are versions.'
jp['sel']="No whole-space reference exists; the entries are the traditions and brands named by Wikipedia's Jigsaw puzzle and Wentworth Wooden Puzzles articles."
kind('3D jigsaw puzzle')['nl']='One entry is a solid-shape jigsaw sold under its own name.'
kind('3D jigsaw puzzle')['sel']='No whole-space reference exists; the single entry comes from the earlier pass.'
for k in jig['k']:
    k.pop('r',None)

# ---- twisty puzzles
cube=take('Cube twisty puzzle'); modc=take('Modified cube puzzle'); noncube=take('Non-cube twisty puzzle'); chain=take('Chain twisty puzzle')
renames['Modified cube puzzle']='Cube twisty puzzle'; renames['Chain twisty puzzle']='Folding puzzle'
old={e['n']:e for e in cube['x']+modc['x']+noncube['x']+chain['x']}
def oldv(n):
    e=old[n]; out=[V(e['n'],e['d'],e.get('mk',''),e.get('y',''))]
    for v in e.get('v',[]): out.append(V(v['n'],v.get('d',''),v.get('mk',''),v.get('y','')))
    return out
G3='Cube · face-turning'
rc=old["Rubik's Cube"]
speed=[]
for n in ['DaYan Guhong and Zhanchi','GAN356 line','QiYi X-Man Tornado','MoYu cubes','YJ and MGC cubes','GAN356 i','GoCube']:
    e=old[n]
    speed.append(V(e['n'],('smart cube: ' if n in('GAN356 i','GoCube') else 'speed cube: ')+e['d'],e.get('mk',''),e.get('y','')))
    for v in e.get('v',[]): speed.append(V(v['n'],'speed cube: '+v.get('d',''),e.get('mk',''),v.get('y','')))
rcv=[V(v['n'],v.get('d',''),v.get('mk',''),v.get('y','')) for v in rc.get('v',[])]
BIG=old['Big cube (6x6x6 and above)']
cx=[
 E('Pocket Cube','2×2×2 cube puzzle.',CC,a='2×2×2',g=G3,y=''),
 E("Rubik's Cube",rc['d'] if rc['d'] else '3×3×3 cube puzzle.',CC,mk="Rubik's",y='1974',a='3×3×3 · Magic Cube',v=rcv+speed,g=G3,dt='standard · speed · smart',role='landmark'),
 E("Rubik's Revenge",'4×4×4 cube puzzle.',CC,a='4×4×4',g=G3),
 E("Professor's Cube",'5×5×5 cube puzzle.',CC,a='5×5×5',g=G3),
 E('V-Cube 6 to 8','6×6×6 to 8×8×8 cubes; the patent for larger cubes is held by Panagiotis Verdes.',CC,mk='Panagiotis Verdes',v=[V('V-Cube 6'),V('V-Cube 7'),V('V-Cube 8')]+[V(v['n'],v.get('d',''),v.get('mk',''),v.get('y','')) for v in BIG.get('v',[])],g=G3),
 E('Sudoku Cube','3×3×3 cube with numbers instead of colours; designed by Jay Horowitz.',CC,mk='Jay Horowitz',y='2006',g=G3),
 E('Calendar Cube','3×3×3 cube with calendar markings; Ideal produced a commercial version.',CC,g=G3),
 E('Magic Cube with numbers','3×3×3 cube with numbered faces.',CC,g=G3),
 E('Nine-Colour Cube','Rubik\'s Cube variation with nine colours.',CC,g=G3),
 E("Rubik's WOWCube",'Rubik\'s Cube variation with electronic modules.',CC,mk="Rubik's",g=G3),
 E('Mirror Blocks','Cube whose pieces differ in shape; also called the Bump Cube.',CC,g=G3),
 E('Nichols Cube Puzzle','Rotating-cube puzzle patented by Larry D. Nichols.',CC,mk='Larry D. Nichols',y='1972',g=G3),
 E('Gear Cube','Geared 3×3 cube designed by Oskar van Deventer.',CC,mk='Oskar van Deventer',y='2010',v=oldv('Gear Cube')[1:],g='Cube · geared'),
 E('Redi Cube','Cube puzzle designed by Oskar van Deventer.',old['Redi Cube']['s'],mk='Oskar van Deventer',y='2017',g='Cube · irregular'),
 E('Mosaic Cube','Cube puzzle designed by Oskar van Deventer.',old['Mosaic Cube']['s'],mk='Oskar van Deventer',y='2010',g='Cube · irregular'),
 E('Mixup Cube','Irregular cube designed by Oskar van Deventer.',CC,mk='Oskar van Deventer',g='Cube · irregular'),
 E('Bandaged cubes','Cubes with some pieces bound together.',CC,g='Cube · irregular'),
 E('Golden Cube','Irregular cube designed by Tony Fisher.',CC,mk='Tony Fisher',g='Cube · irregular'),
 E('Lan Lan Rex Cube','Irregular cube also called the Flower Box.',CC,g='Cube · irregular'),
 E('Ivy Cube','Irregular cube puzzle.',CC,g='Cube · irregular'),
 E('Rubik\'s Domino','2×3×3 cuboid puzzle.',CC,mk="Rubik's",g='Cuboid · face-turning'),
 E('Skewb','Cube whose axes of rotation pass through the corners, so each move is a deep cut affecting all six faces; invented by Tony Durham and marketed by Uwe Mèffert.','https://en.wikipedia.org/wiki/Skewb',mk='Uwe Mèffert',g='Cube · corner-turning',role=None),
 E('Dino Cube','Cube turned around its corners, three edge pieces at a time; invented by Robert Webb, first prototype 1985.','https://en.wikipedia.org/wiki/Dino_Cube',mk='Robert Webb',y='1985',g='Cube · corner-turning'),
 E('Helicopter Cube','Cube that turns around its edges rather than faces; invented by Adam G. Cowan in 2005 and built in 2006.','https://en.wikipedia.org/wiki/Helicopter_Cube',mk='Adam G. Cowan',y='2005',g='Cube · edge-turning'),
 E('Square-1','Cube puzzle whose layers change shape as they turn.',old['Square-1']['s'],y='1990',v=oldv('Square-1')[1:],g='Cube · shape-shifting'),
]
for e in cx:
    if e['n']=='Skewb': e['y']=''
cube_k=K('Cube twisty puzzle','A cube or cuboid whose layers or pieces turn to scramble and restore coloured faces, including large orders, altered cubes, magnetic speedcubes and Bluetooth smart cubes.',"Rubik's cube · magic cube · speedcube · smart cube",'https://en.wikipedia.org/wiki/Combination_puzzle',cx,
 "One entry is a cube or cuboid twisty-puzzle design; makers' speed and smart editions are versions, and speed or smart is an attribute.",
 "Every cube and cuboid in Wikipedia's Combination puzzle article (regular cuboids, pattern variations, irregular cuboids, geared puzzles) and its navigation box; sections follow shape and turning type, which the entries state from their own articles where fetched.",
 'by shape and turning type',cube['tt'])
P_=CC
tet=[E('Pyraminx','Tetrahedron puzzle, 3×3×3, designed by Uwe Mèffert.',P_,mk='Uwe Mèffert',y='1970',v=oldv('Pyraminx')[1:],g='Tetrahedron · face-turning'),
 E('Pyraminx Duo','Tetrahedron puzzle listed beside the Pyraminx.',CC,g='Tetrahedron · face-turning'),
 E('Pyramorphix','Tetrahedron puzzle, 2×2×2.',CC,g='Tetrahedron · face-turning'),
 E('BrainTwist','Tetrahedron puzzle, 2×2×2.',CC,g='Tetrahedron · face-turning'),
 E("Rob's Pyraminx",'Tetrahedron puzzle designed by Oskar van Deventer.',old["Rob's Pyraminx and Octahedron"]['s'],mk='Oskar van Deventer',y='2014',g='Tetrahedron · face-turning'),
 E('Face Turning Octahedron','Octahedron puzzle, 3×3×3.',CC,g='Octahedron · face-turning'),
 E('Skewb Diamond','Octahedron puzzle, 3×3×3.',CC,g='Octahedron · corner-turning'),
 E("Rob's Octahedron",'Octahedron puzzle designed by Oskar van Deventer.',old["Rob's Pyraminx and Octahedron"]['s'],mk='Oskar van Deventer',y='2015',g='Octahedron · face-turning'),
 E('Megaminx','Dodecahedron puzzle, 3×3×3; larger orders are versions.',old['Megaminx']['s'],mk='Uwe Mèffert',v=oldv('Megaminx')[1:]+[V('Gigaminx','5×5×5 dodecahedron','',''),V('Teraminx','7×7×7 dodecahedron','',''),V('Petaminx','9×9×9 dodecahedron','','')],g='Dodecahedron · face-turning'),
 E('Skewb Ultimate','Dodecahedron puzzle, 3×3×3.',CC,g='Dodecahedron · corner-turning'),
 E('Pyraminx Crystal','Dodecahedron puzzle, 3×3×3.',CC,g='Dodecahedron · edge-turning'),
 E("Alexander's Star",'Great dodecahedron puzzle, 3×3×3.',CC,g='Great dodecahedron · edge-turning'),
 E('Impossiball','Icosahedron puzzle, 2×2×2.',CC,g='Icosahedron'),
 E('Dogic','Icosahedron puzzle, 4×4×4.',CC,g='Icosahedron'),
 E('Icosaix','Icosahedron-based puzzle designed by Oskar van Deventer.',old['Icosaix']['s'],mk='Oskar van Deventer',y='2015',g='Icosahedron'),
 E('Tuttminx','Truncated icosahedron puzzle.',CC,g='Truncated icosahedron'),
 E("Rubik's Clock",old["Rubik's Clock"]['d'],old["Rubik's Clock"]['s'],mk="Rubik's",y='1988',g='Dials'),
]
for e in tet:
    if e['g'] in('Icosahedron','Truncated icosahedron','Great dodecahedron · edge-turning','Dials'): pass
nc_k=K('Non-cube twisty puzzle','A rotating puzzle built on a tetrahedron, octahedron, dodecahedron, icosahedron or other solid, or on dials, rather than a cube.','pyramid puzzle · dodecahedron puzzle','https://en.wikipedia.org/wiki/Combination_puzzle',tet,
 'One entry is a non-cube twisty-puzzle design; larger orders and makers\' editions are versions.',
 "Every non-cubic puzzle in Wikipedia's Combination puzzle article (other polyhedra, non-Rubik-style) and its navigation box, in sections by solid and turning type. Virtual higher-dimensional puzzles (MagicCube4D and similar) are software and left to Interactive Entertainment.",
 'by solid and turning type',noncube['tt'])
PZ['s'][1]['k']=[cube_k,nc_k]
PZ['s'][1]['t']='Puzzles solved by turning layers or pieces of a cube or other solid until the pattern is restored, sorted by shape; a chain that folds → Mechanical puzzles, a sliding or take-apart puzzle → Mechanical puzzles.'
PZ['s'][1]['ax']='kinds by shape: cube and cuboid, or other solids and dials'

# ---- mechanical puzzles
ptog=take('Put-together puzzle'); tk=take('Take-apart & trick-opening puzzle'); il=take('Interlocking puzzle'); dis=take('Disentanglement puzzle')
sq=take('Sequential movement puzzle'); fo=take('Folding puzzle'); dx=take('Dexterity puzzle'); pv=take('Puzzle vessel'); io=take('Impossible object'); sl=take('Single-player logic game')
renames['Take-apart & trick-opening puzzle']='Take-apart puzzle'
mo=lambda k,n: [e for e in k['x'] if e['n']==n][0]
# put together
px=[mo(ptog,'Tangram'),mo(ptog,'Soma cube'),mo(ptog,'Pentomino set'),mo(ptog,'Katamino'),
    E("Hoffman's packing puzzle",'Solid-piece packing puzzle named by Wikipedia among assembly puzzles.',MPC+'',g='Three-dimensional assembly'),
    E('Bedlam cube','Cube-packing puzzle of solid pieces.',MPC,g='Three-dimensional assembly'),
    E('Conway puzzle','Cube-packing puzzle of solid blocks.',MPC,g='Three-dimensional assembly'),
    E('Diabolical cube','Cube-packing puzzle of solid pieces.',MPC,g='Three-dimensional assembly'),
    E('Slothouber–Graatsma puzzle','Cube-packing puzzle of solid blocks.',MPC,g='Three-dimensional assembly'),
    E('Egg of Columbus (tangram puzzle)','Tangram-type egg puzzle.',MP,g='Two-dimensional assembly'),
    E('Puzzle ring','Ring of linked bands that must be put together, classed by Slocum under miscellaneous put-together puzzles.',SL,g='Miscellaneous put-together'),
]
for e in px[:4]:
    e['g']='Two-dimensional assembly' if e['n'] in('Tangram',) else 'Three-dimensional assembly' if e['n'] in('Soma cube','Pentomino set','Katamino') else e.get('g')
px[2]['g']='Two-dimensional assembly'
setx(ptog,px,'One entry is a classic put-together puzzle design, or a brand that runs its own range of them; sets and sizes are versions.',
 "Assembly puzzles named by Wikipedia's Mechanical puzzle article and its category pages (Mechanical puzzles; Mechanical puzzle cubes), placed in the put-together class of Jerry Slocum's classification as given on WoodPuzzles; Katamino from the earlier pass.",'by two or three dimensions')
# take apart
kx=[e for e in tk['x']]
for e in kx: e['g']='Puzzle box'
setx(tk,kx,'One entry is a puzzle-box tradition or a maker whose boxes open by a hidden method; individual boxes are versions.',
 "Puzzle-box traditions and makers named by Wikipedia's Puzzle box article (Japanese puzzle box, Akio Kamei, Karakuri group, Constantin from the earlier pass), in Slocum's take-apart class.",'')
tk['d']='A box or object that must be opened or taken apart by finding a hidden method.'
# vexier
vx=K('Vexier puzzle','A trick puzzle whose method is concealed: puzzle locks that open by hidden mechanics, trick matchboxes and vanishing illusions.','trick lock · puzzle lock · vanish puzzle',SL,
 [E('Puzzle lock','Lock with unusual or hidden mechanics; ancient Chinese locks fall into three types and Roman mask padlocks date to the 2nd century BCE.','https://en.wikipedia.org/wiki/Puzzle_lock',g='Trick locks'),
  E('Trick matchbox','Matchbox or matchsafe that opens by a trick; Slocum lists it under trick openings.',SL,g='Trick containers'),
  E('Get Off the Earth','Vanishing-figures puzzle by Sam Loyd, named by Slocum as the vanish class example.',SL,g='Vanish puzzles'),
  E('Vanishing Leprechauns','Vanishing-figures puzzle named by Slocum in the vanish class.',SL,g='Vanish puzzles')],
 'One entry is a classic trick puzzle design, not a single maker\'s box.',
 "The trick-lock, trick-container and vanish subclasses of Slocum's classification as given on WoodPuzzles, with the Puzzle lock article of Wikipedia; Slocum's vanish class has two named examples only.",'by trick')
# interlocking
ix=[mo(il,'Six-piece burr'),mo(il,'High-level burr'),mo(il,'Diagonal burr')]
for e in ix: e['g']='Burr'
ix[0]['v']=ix[0].get('v',[])
ix+=[E('Altekruse puzzle','Burr family named after William Altekruse, who held a patent in 1890.','https://en.wikipedia.org/wiki/Burr_puzzle',mk='William Altekruse',y='1890',g='Burr'),
 E('Chuck puzzle','Burr family patented by Edward Nelson in 1897; larger versions were named by Ron Cook.','https://en.wikipedia.org/wiki/Burr_puzzle',mk='Edward Nelson',y='1897',v=[V('Baby-chuck'),V('Papa-chuck'),V('Grandpapachuck'),V('Great Grandpapachuck')],g='Burr'),
 E('Pagoda burr','Burr family also called Japanese Crystal; mentioned in 1928.','https://en.wikipedia.org/wiki/Burr_puzzle',y='1928',g='Burr'),
 E('Lu Ban lock','Traditional Chinese name for burr puzzles, attributed to Lu Ban.','https://en.wikipedia.org/wiki/Burr_puzzle',g='Burr'),
 E('Edakoodam','Traditional Malayalam name for burr puzzles, from Kerala.','https://en.wikipedia.org/wiki/Burr_puzzle',g='Burr'),
 E('Happy Cube','Foam pieces folded and fitted into a cube; devised by Dirk Laureyssens in 1986.','https://en.wikipedia.org/wiki/Happy_Cube',mk='Dirk Laureyssens',y='1986',g='Geometric objects')]
setx(il,ix,'One entry is a classic interlocking-puzzle design or burr family; sizes and levels are versions.',
 "Burr families named by Wikipedia's Burr puzzle article, with Happy Cube from Wikipedia's mechanical puzzle cubes, in Slocum's interlocking class.",'by subclass')
# disentanglement
dxs=[mo(dis,'Hanayama Cast puzzle'),mo(dis,'Chinese rings')]
dxs[0]['g']='Cast iron and sheet metal'; dxs[1]['g']='Wire'
ex=dis.get('m',[])
have={v['n'] for v in dxs[0]['v']}
for n,_ in ex:
    if n not in have: dxs[0]['v'].append(V(n,'','Hanayama',''))
DP='https://en.wikipedia.org/wiki/Disentanglement_puzzle'
dxs[1]['n']='Chinese rings (Baguenaudier)'
dxs+=[E('Boomhower puzzle','Wire disentanglement puzzle designed by R. Boomhower in 1966.',DP,mk='R. Boomhower',y='1966',g='Wire'),
 E("Wit's End puzzle",'Wire disentanglement puzzle.',DP,g='Wire'),
 E('T-Bar puzzle','Disentanglement puzzle.',DP,g='Wire'),
 E('Mini Rope Bridge puzzle','Disentanglement puzzle.',DP,g='String'),
 E('Figure Eight puzzle','Disentanglement puzzle also called the Notorious Figure Eight or Possibly Impossible.',DP,g='String'),
 E('Mystery Key','Disentanglement puzzle issued by the Peter Pan company in the 1950s.',DP,mk='Peter Pan',y='1950s',g='Wire'),
 E('Kercang','Traditional puzzle of the Jakun indigenous people of Malaysia.',DP,g='Traditional'),
 E('Tavern puzzle','Brand-name set of wire and metal disentanglement puzzles.',DP,g='Cast iron and sheet metal')]
setx(dis,dxs,'One entry is a classic disentanglement puzzle or a brand that runs its own range of them; individual castings are versions.',
 "Puzzles named by Wikipedia's Disentanglement puzzle article and Hanayama from the earlier pass, in Slocum's disentanglement class (cast iron and sheet metal, wire, string).",'by material')
# sequential
sx=[mo(sq,'Tower of Hanoi'),mo(sq,'15 puzzle'),mo(sq,'Klotski'),mo(sq,'Rush Hour')]
for e in sx[:]: e['g']='Sliding piece' if e['n'] in('15 puzzle','Klotski','Rush Hour') else 'Miscellaneous sequential movement'
pegs=mo(sl,'Peg solitaire'); pegs['g']='Solitaire'
sx+=[pegs,
 E('Minus Cube','Sliding-cube puzzle, 2×2×2 minus one.',CC,g='Sliding piece'),
 E('Think-a-Dot','Mechanical toy named by Wikipedia as a simulated sequential-movement example.',MP,g='Miscellaneous sequential movement'),
 E('Magnetic Tower of Hanoi','Tower of Hanoi variant listed in the mechanical puzzles category.',MP,g='Miscellaneous sequential movement')]
sl['x']=[e for e in sl['x'] if e['n']!='Peg solitaire']
setx(sq,sx,'One entry is a classic sequential-movement puzzle design; editions and sizes are versions.',
 "Sequential-movement puzzles named by Wikipedia's Mechanical puzzle article, the Sliding puzzle article and the Mechanical puzzles category; rotating cube-type puzzles are in Twisty puzzles. Slocum's class has solitaire, counter, sliding piece, rotating and maze subclasses.",'by subclass')
# folding
fx=[mo(fo,"Rubik's Magic"),mo(fo,'Flexagon'),
 E('Snake cube','Chain of 27 or 64 cubelets joined by an elastic band.','https://en.wikipedia.org/wiki/Snake_cube',g='Hinged chain'),
 E("Rubik's Snake",old["Rubik's Snake"]['d'],old["Rubik's Snake"]['s'],mk="Rubik's",y='1981',g='Hinged chain'),
 E('Yoshimoto Cube','Folding cube of eight blocks listed in the mechanical puzzle cubes category.',MPC,g='Hinged chain')]
fx[0]['g']='Sheets and strips'; fx[1]['g']='Sheets and strips'
FL='https://en.wikipedia.org/wiki/Flexagon'
fx[1]['v']=[V('Trihexaflexagon','Three-faced hexaflexagon folded from nine triangles; credited to Arthur H. Stone.','Arthur H. Stone','1939'),
 V('Hexahexaflexagon','Six-faced hexaflexagon of nineteen triangles; patented by Russell Rogers and Leonard D\'Andrea.','Russell Rogers and Leonard D\'Andrea','1959'),
 V('Tetra-tetra flexagon','Square-faced flexagon credited to Ernest Ranucci.','Ernest Ranucci',''),
 V('Tritetraflexagon','Simplest square-faced flexagon, three faces.','',''),
 V('Hexatetraflexagon','Cyclic square-faced flexagon with no dead ends.','',''),
 V('Nonplanar pentaflexagon','Pentagon-based flexagon that cannot lie flat; Harold V. McIntosh.','Harold V. McIntosh','2000')]
fx[1]['s']=FL
setx(fo,fx,'One entry is a classic folding-puzzle design; editions and flexagon types are versions.',
 "Folding puzzles named by Wikipedia's Flexagon article, Combination puzzle article and the mechanical puzzle cubes category, in Slocum's folding class; Rubik's Snake moves here from Twisty puzzles.",'by subclass')
fo['d']='A paper, hinged or chained object folded into a target shape or pattern.'
# dexterity
dxy=[mo(dx,'Perplexus'),mo(dx,'Labyrinth tilt maze')]
for e in dxy: e['g']='Maze dexterity'
dxy.append(E("Rubik's 360",'Derivative of the Rubik\'s Cube listed in its navigation box.',CC,mk="Rubik's",g='Rolling ball'))
setx(dx,dxy,'One entry is a classic dexterity-puzzle design or brand; editions are versions.',
 "Dexterity puzzles from the earlier pass, with Rubik's 360 from Wikipedia's Combination puzzle navigation box, in Slocum's dexterity class (throw and catch, rolling ball, maze dexterity). No whole-space reference names more.",'by subclass')
# puzzle vessel
JG='https://en.wikipedia.org/wiki/Puzzle_jug'
vsx=pv['x']+[E('Cadogan teapot','Pour-from-the-base teapot named by Slocum among puzzle vessels.',SL),E('Chinese puzzle wine pot','Trick wine pot named by Slocum among puzzle vessels.',SL)]
setx(pv,vsx,'One entry is a classic trick drinking vessel.',"Vessels named by Wikipedia's Puzzle jug article and Slocum's puzzle vessel class (puzzle jugs and mugs, Cadogan teapots, Chinese wine pots).",'')
# impossible
IB='https://en.wikipedia.org/wiki/Impossible_bottle'
ox=[mo(io,'Ship in a bottle'),mo(io,'Fruit in a bottle'),
 E('Passion bottle','Bottle holding the instruments of the Passion.',IB),
 E('God-in-a-bottle','Craft made in a German prisoner-of-war camp by an Irish soldier in the First World War.',IB),
 E('Arrow through a bottle','Impossible object named by Slocum.',SL)]
setx(io,ox,'One entry is a classic impossible-object type.',"Types named by Wikipedia's Impossible bottle article and Slocum's impossible objects class.",'')
# single-player logic
for k in [sl]:
    k['nl']='One entry is a brand of single-player logic puzzles; its games are not listed.'
    k['sel']='No whole-space reference exists; ThinkFun and SmartGames are brands with their own catalogue, so each stands for itself.'
    k.pop('m',None); k.pop('r',None)
mech=PZ['s'][2]
mech['k']=[ptog,tk,il,dis,sq,dx,vx,fo,pv,io,sl]
mech['t']='Puzzles solved by moving, joining or separating solid parts, sorted by Slocum\'s classes; a twisting cube → Twisty puzzles, a cut picture → Jigsaw puzzles.'
mech['ax']="kinds by Jerry Slocum's classes: put together, take apart, interlock, untangle, slide, steer, trick, fold, drink, perceive"

# ---- fidgets
fid=PZ['s'][3]
FD='https://en.wikipedia.org/wiki/Fidget_toy'
kk={k['n']:k for k in fid['k']}
def keep(kn,keepnames,nl,sel,g=''):
    k=kk[kn]; k['x']=[e for e in k.get('x',[]) if e['n'] in keepnames]
    if k['x']:
        k['nl']=nl; k['sel']=sel
        for e in k['x']: e['g']=g
    else:
        k.pop('x',None)
    return k
SELF="Entries with a traceable originator named by a fetched page; Wikipedia's Fidget toy article names no originators, so each comes from the page cited on the entry."
keep('Spinner',{'Hettinger spinning toy','Torqbar','Pavelsky three-lobed spinner patent'},'One entry is a spinning fidget with a traceable originator or patent.',SELF,'Rotating')
keep('Slider & haptic fidget',{'QiYi Haptic Coin'},'One entry is a metal fidget with a named maker.',SELF,'Linear')
keep('Squeeze toy',{'NeeDoh'},'One entry is a squeeze fidget with a named maker.',SELF,'Deforming')
keep('Clicker & switch fidget',{'Fidget Cube'},'One entry is a pressing fidget with a named maker.',SELF,'Discrete')
keep('Popper',{'Coster bubble-popping toy','FoxMind Pop It'},'One entry is a popping fidget with a named maker.',SELF,'Discrete')
keep('Twist fidget',{'Tangle'},'One entry is a twisting fidget with a named maker.',SELF,'Articulated')
keep('Fold fidget',set(),'','')
keep('Baoding balls',set(),'','')
keep('Worry stone',set(),'','')
keep('Worry beads',set(),'','')
for kn in ['Fold fidget']:
    pass
kk['Fold fidget']['d']=kk['Fold fidget']['d']
def shelf(n,t,ks): return S(n,t,'',[kk[x] for x in ks])
fid_shelves=[
 shelf('Rotating fidgets','Fidgets that spin on a bearing or string: hand spinners and begleri; a top → Skill, music & novelty toys.',['Spinner','Begleri']),
 shelf('Linear fidgets','Fidgets worked by sliding or rubbing in a line: haptic sliders and worry stones.',['Slider & haptic fidget','Worry stone']),
 shelf('Deforming fidgets','Fidgets worked by squeezing, stretching or squashing: squeeze toys, squishies and stretch toys.',['Squeeze toy','Squishy','Stretch fidget']),
 shelf('Discrete-action fidgets','Fidgets with separate things to click, pop or count: switch cubes, poppers and worry beads.',['Clicker & switch fidget','Popper','Worry beads']),
 shelf('Articulated fidgets','Fidgets of linked parts that flip, twist or fold: flippy chains, twist fidgets and infinity cubes.',['Flippy chain','Twist fidget','Fold fidget']),
 shelf('Rolling fidgets','Fidgets of balls that roll in the palm: Baoding balls.',['Baoding balls']),
]
kk['Fold fidget']['x']=[]; kk['Fold fidget'].pop('x')
PZ['t']=PZ['t']
PZ['ms']=[
 {'mkt':'Global fidget toys','who':'All makers','share':'USD 9.0 billion','yr':2025,'s':'https://market.us/report/fidget-toys-market/','note':'market size, as the report states it; forecast USD 18.2 billion by 2035'},
 {'mkt':'Global fidget toys, by product','who':'Fidget spinners','share':'40.00 %','yr':2025,'s':'https://market.us/report/fidget-toys-market/','note':'share of the market; the other 60.00 % covers cubes, pop toys, stress balls, putty and slime, rings, chains and boards'},
 {'mkt':'Global fidget toys, by channel','who':'Online retail','share':'50.00 %','yr':2025,'s':'https://market.us/report/fidget-toys-market/','note':'share of sales by distribution channel'},
 {'mkt':'Global fidget toys, mass-market and branded toy companies','who':'LEGO Group, Hasbro, Mattel, Spin Master, ZURU, Ravensburger, Fat Brain Toys, Schylling, Goliath Games, Fun In Motion Toys, Tangle Creations, Antsy Labs, ARK Therapeutic Services, The Pencil Grip, Harkla','share':'','yr':2025,'s':'https://market.us/report/fidget-toys-market/','note':'key players named by the report; no individual shares given'},
 {'mkt':'Boutique metal fidgets','who':'Specialist makers of machined stainless-steel and titanium sliders and spinners','share':'','yr':2026,'s':'https://www.titanfidget.com/blogs/news/are-expensive-fidget-toys-worth-it-the-honest-truth-about-price-vs-performance','note':'one maker\'s page gives example prices of $24.90, $75 and $99; no share or maker list is published'},
]
# desk toys
dsk=PZ['s'][4]
dk={k['n']:k for k in dsk['k']}
def gset(kn,g,nl='',sel=''):
    for e in dk[kn].get('x',[]): e['g']=g
PRIN={"Newton's cradle":'Momentum and collision','Magnet sphere set':'Magnetism','Coil spring toy':'Elasticity','Drinking bird':'Heat and evaporation','Kinetic sand & sand art':'Granular matter','Useless machine':'Switch mechanism','Magic 8 Ball':'Buoyancy and chance'}
for kn,g in PRIN.items():
    gset(kn,g)
    k=dk[kn]; k['nl']='One entry is a desk-toy design or brand that demonstrates one physical principle; its editions are versions.'
    k['sel']="No whole-space reference exists. Wikipedia's Desk toy article names ten examples without inventors, so the entries are the designs from the earlier pass and the fetched pages cited on each."
    k['xg']='by physical principle'
    k.pop('m',None); k.pop('r',None)
dk['Pin art']['x']=[E('Pin Art','Crowded array of pins free to slide in and out independently, forming a raised impression; listed among 1987 introductions.','https://en.wikipedia.org/wiki/Pin_Art',y='1987',g='Sliding pins')]
dk['Pin art']['nl']='One entry is a desk-toy design that demonstrates one physical principle.'
dk['Pin art']['sel']="Wikipedia's Pin Art article; it names no inventor for the toy."
dk['Pin art']['xg']='by physical principle'
lava=K('Lava lamp','A lamp whose heated wax rises and sinks through a liquid; a decorative lamp → B3.','',"https://en.wikipedia.org/wiki/Lava_lamp",
 [E('Astro lamp','Lava lamp invented by Edward Craven Walker; Crestworth Ltd launched the first Astro lamp in 1963, and his company was renamed Mathmos in 1992.','https://en.wikipedia.org/wiki/Lava_lamp',mk='Crestworth',y='1963',g='Heat and convection',role='origin')],
 'One entry is a lava-lamp design with a traceable originator.',"Wikipedia's Lava lamp article; it names one originator.",'by physical principle')
plasma=K('Plasma globe','A glass globe with a central electrode and a low-pressure gas that forms glowing filaments.','plasma lamp',"https://en.wikipedia.org/wiki/Plasma_globe",
 [E('Tesla plasma lamp','Original plasma lamp credited to Nikola Tesla, described in US patent 514,170 of 6 February 1894.','https://en.wikipedia.org/wiki/Plasma_globe',mk='Nikola Tesla',y='1894',g='Electric discharge')],
 'One entry is a plasma-lamp design with a traceable originator.',"Wikipedia's Plasma globe article; it names one originator.",'by physical principle')
dsk['k']+=[lava,plasma]
dsk['t']="Toys set down on a desk to watch or play with, sorted by the physical principle they show: momentum, magnetism, elasticity, heat, sand, pins, a switch; a lava or plasma lamp is also a decorative lamp → B3, a snow globe → B4."
dsk['ax']='kinds by the principle at work: momentum, magnetism, elasticity, heat, granular matter, sliding pins, a switch, buoyancy'
# replace fidget shelf
i=PZ['s'].index(fid)
PZ['s'][i:i+1]=fid_shelves
PZ['note']='Objects only: puzzle-solving and speedcubing as pursuits live in separate taxonomies. Mechanical puzzles follow Slocum\'s classes; twisty puzzles are sorted by shape and turning type; fidgets by motion; desk toys by physical principle.'
# generic nl/sel on all other kinds with x
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            if k.get('x') and not k.get('nl'):
                k['nl']="One entry is a named %s design, brand or tradition sold as its own thing; its revisions and variants are versions."%k['n'].lower()
                k['sel']="No whole-space reference exists for this kind. The entries come from the pages cited on each entry and are a starting list, not a complete canon; this kind has not yet had the canon pass."
# write
tmp=P+'.tmp'
json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1)
os.replace(tmp,P)
json.dump(renames,open(ROOT+'out/E1_renames.json','w'),ensure_ascii=False,indent=1)
print('ok')
