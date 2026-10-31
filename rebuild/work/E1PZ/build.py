import json, copy, os
R='/home/user/Possession-Taxonomy/rebuild/'
W=R+'work/E1PZ/'
d=json.load(open(W+'bak/E1.json'))
br=json.load(open(W+'bak/E1_brands.json'))
WP='https://en.wikipedia.org/wiki/'
def A(n,dd,mk='',y='',s='',v=None,dt=None,a=''):
    o={'n':n,'a':a,'d':dd,'mk':mk,'y':y,'s':s,'v':v or []}
    if dt: o['dt']=dt
    return o
def V(n,mk='',y='',dd=''): return {'n':n,'mk':mk,'y':y,'d':dd}
def K(n,dd,s,x,a='',t=None,m=None,r=None):
    o={'n':n,'a':a,'d':dd}
    if t: o['t']=t
    o['s']=s; o['x']=x
    if m: o['m']=m
    if r: o['r']=r
    return o

# ---- locate old pieces
board=[dp for dp in d['depts'] if dp['n'].startswith('Board, card')][0]
skill=[dp for dp in d['depts'] if dp['n'].startswith('Skill, music')][0]
pz=[s for s in board['s'] if s['n']=='Puzzles'][0]
old={k['n']:k for k in pz['k']}
board['s']=[s for s in board['s'] if s['n']!='Puzzles']
sk=[s for s in skill['s'] if s['n']=='Skill toys & fidgets'][0]
oldsk={k['n']:k for k in sk['k']}
mech=old['Mechanical puzzle']
mx={x['n']:x for x in mech['x']}

# ---- 1 jigsaw
jig=copy.deepcopy(old['Jigsaw puzzle'])
jig['t']=[t for t in jig['t'] if t!='Puzzle globe']+['Standard 1,000-piece (about 38 x 27)']
jig['x']=[x for x in jig['x'] if x['n']!='Standard 1,000-piece puzzle']
jig['m']=[m for m in jig['m']]
j3=copy.deepcopy(old['3D jigsaw puzzle'])
shelf_jig={'n':'Jigsaw puzzles','k':[jig,j3]}

# ---- 2 twisty
rc=copy.deepcopy(mx["Rubik's Cube"])
rc['v']=[V('Magic Cube (Budapest)',"Rubik's",'1977','first test batches in Budapest toy shops'),
 V('Pentangle Puzzles UK licence','','1978','sold in the UK under licence'),
 V('Ideal Toy Corp. release','Ideal Toy Company','1980','renamed Rubik\'s Cube worldwide'),
 V('Pocket Cube 2x2x2',"Rubik's",'','official 2x2x2'),
 V("Rubik's Revenge 4x4x4","Rubik's",'','also sold as Master Cube'),
 V("Professor's Cube 5x5x5","Rubik's",'',''),
 V('Spin Master purchase of the brand','Spin Master','2021','completed 5 January 2021')]
rc['d']='3x3x3 rotating cube invented by Ernő Rubik as the Magic Cube; about 500 million cubes sold by 2024.'
rc['mk']="Rubik's"; rc['y']='1974'
rc['dt']='order (2x2 to 21x21) · stickered or stickerless · official or third-party'
cube=K('Cube twisty puzzle','A cube whose layers rotate to scramble and restore coloured faces, from 2x2x2 up to very large orders.',
 WP+"Rubik%27s_Cube",[rc,
  A("Nichols rotating-cube patent",'Larry D. Nichols patented an earlier rotating-cube puzzle, two years before Rubik built his prototype.','','1972',WP+"Rubik%27s_Cube",dt='patent US 3,655,201'),
  A('Big cube (6x6x6 and above)','Cubes beyond 5x5x5, made by third parties; 6x6x6 and 7x7x7 are recognised WCA puzzles, and sizes above 17x17x17 exist.','','',WP+'Speedcubing',
    v=[V('Over the Top Cube 17x17x17','Oskar van Deventer','2012','Guinness record holder 2012 to 2016')],dt='order · WCA puzzle (6x6x6, 7x7x7) or not')],
 a='Rubik\'s cube · magic cube · 3x3x3',t=['2x2x2 (Pocket Cube)','3x3x3','4x4x4 (Revenge)','5x5x5 (Professor\'s)','6x6x6 and 7x7x7','Larger orders','Stickered','Stickerless'])

noncube=K('Non-cube twisty puzzle','A rotating puzzle built on a pyramid, dodecahedron or other solid, or on a dial or split layer rather than a cube.',
 WP+'Combination_puzzle',[
  A('Pyraminx','Tetrahedron twisty puzzle by Uwe Mèffert, marketed worldwide by Tomy Toys from 1981.','Uwe Mèffert','early 1970s',WP+'Uwe_M%C3%A8ffert',
    v=[V('Tomy Toys release','Tomy','1981','first marketing')],dt='WCA puzzle · tetrahedron'),
  A('Megaminx','Dodecahedron twisty puzzle with 12 faces, devised independently by several people; Bandelow\'s Hungarian Supernova came first.','Uwe Mèffert','',WP+'Megaminx',
    v=[V('Hungarian Supernova','Christoph Bandelow','','pentagram cuts meet at the edges'),V('Mèffert Megaminx','Uwe Mèffert','','wider edges relative to corners')],dt='WCA puzzle · dodecahedron'),
  A('Skewb','Cube-shaped puzzle with diagonal cuts that turn corners, invented by Tony Durham and first sold by Mèffert as the Pyraminx Cube.','Uwe Mèffert','',WP+'Skewb',dt='WCA puzzle since 2014'),
  A('Square-1','Cube-shaped puzzle whose layers can change shape, invented by Karel Hršel and Vojtěch Kopský in 1990.','','1990',WP+'Square-1_(puzzle)',
    v=[V('Czechoslovak patent CS277266','Karel Hršel','1992','approved 26 October 1992'),V('US patent 5,193,809','Karel Hršel','1993','granted 16 March 1993')],a='Back to Square One · Cube 21',dt='WCA puzzle'),
  A("Rubik's Clock",'Double-sided puzzle of dials and pins, invented by Christopher Wiggs and Christopher Taylor; Rubik bought the patent.',"Rubik's",'1988',WP+"Rubik%27s_Clock",dt='WCA puzzle until the 2027 championship')],
 a='pyramid puzzle · dodecahedron puzzle',t=['Pyramid','Dodecahedron','Octahedron','Dial or clock','Shape-changing'])

fast=K('Speedcube','Cube tuned for fast turning, with magnets and adjustable tension in many models, made by dedicated cube brands.',
 WP+'Speedcubing',[
  A('DaYan Guhong and Zhanchi','Cubes that were the main choice of many leading cubers around 2011 to 2015; DaYan returned with magnetic cubes in 2019.','DaYan','c. 2011-2015','https://ca.speedcube.com.au/blogs/speedcube-brands',
    v=[V('Guhong','DaYan','',''),V('Zhanchi (DaYan 5)','DaYan','',''),V('GuHong V3 M','DaYan','2019','magnetic'),V('TengYun M','DaYan','2019','magnetic')],dt='magnets · version number'),
  A('GAN356 line','Gancube cubes that added factory magnets and adjustable magnet strength; called the premium 3x3 speedcube.','Gancube','2016',WP+'Gancube',
    v=[V('GAN356 Air UM','Gancube','2016','first mass-produced cube with magnets in edges and corners'),V('GAN356 X','Gancube','2017','adjustable magnets'),V('GAN356 XS','Gancube','','movable edge magnets'),V('GAN11 M Pro','Gancube','2020','core-to-corner magnets'),V('GAN12 Maglev','Gancube','2021','first mass-produced maglev cube'),V('GAN13 Maglev','Gancube','2022','')],dt='order · magnet strength · maglev'),
  A('QiYi X-Man Tornado','QiYi flagship 3x3 from a maker that rose to prominence in 2018 with budget-priced cubes; sub-brands X-Man, MoFangGe and VALK.','QiYi','2018','https://ca.speedcube.com.au/blogs/speedcube-brands',
    v=[V('X-Man Tornado V3','QiYi','','current flagship')],dt='sub-brand · version'),
  A('MoYu cubes','Cubes from MoYu, one of the leading cube brands in China; MoFang JiaoShi (MFJS) is its budget subsidiary.','MoYu','','https://ca.speedcube.com.au/blogs/speedcube-brands',
    v=[V('MFJS cubes','MoYu','','cost-effective, smooth turning')],dt='subsidiary · version'),
  A('YJ and MGC cubes','Cubes from YJ (YongJun), a Chinese educational toy company designing puzzles since 2005; MGC is its popular sub-brand.','YJ','2005','https://ca.speedcube.com.au/blogs/speedcube-brands',dt='sub-brand · order')],
 a='speed cube',t=['3x3x3','Other orders and shapes','Magnetic','Maglev','Stickerless'])

smart=K('Smart cube','Cube with sensors and Bluetooth that track each turn for a companion app.',
 WP+'Gancube',[
  A('GAN356 i','Gancube\'s first smart cube, with Bluetooth that tracks turns in real time.','Gancube','2018',WP+'Gancube'),
  A('GoCube','Smart cube with sensors in every cube that tracks rotations and solving progress through an app; magnetic turning.','','','https://speedcubeshop.com/collections/gocube')],
 a='Bluetooth cube',t=['Bluetooth','App-tracked'])

shape=K('Bandaged & shape-mod puzzle','Twisty puzzle altered from a standard cube by fused pieces, added mechanisms or a new outline, often by independent designers.',
 WP+'Combination_puzzle',[
  A('Gear Cube','Cube whose turns mesh through gears, designed by Oskar van Deventer as the Caution Cube and mass-produced by Mèffert in 2010.','Oskar van Deventer','2010',WP+'Oskar_van_Deventer',
    v=[V('Gear Cube Extreme','Uwe Mèffert','2010',''),V('Gear Shift','Uwe Mèffert','2011','')]),
  A('Mosaic Cube','Van Deventer design mass-produced by Mèffert\'s.','Oskar van Deventer','2010',WP+'Oskar_van_Deventer'),
  A('Redi Cube','Van Deventer design mass-produced by MoYu.','Oskar van Deventer','2017',WP+'Oskar_van_Deventer'),
  A('Mixup Cube','Van Deventer design mass-produced by WitEden.','Oskar van Deventer','',WP+'Oskar_van_Deventer'),
  A("Rob's Pyraminx and Octahedron",'Van Deventer shape variants of the pyramid and octahedron, mass-produced by Mèffert\'s.','Oskar van Deventer','2014-2015',WP+'Oskar_van_Deventer',
    v=[V("Rob's Pyraminx",'Uwe Mèffert','2014',''),V("Rob's Octahedron",'Uwe Mèffert','2015','')]),
  A('Icosaix','Van Deventer icosahedron puzzle mass-produced by MF8.','Oskar van Deventer','2015',WP+'Oskar_van_Deventer')],
 a='bandaged cube · shape mod',t=['Bandaged cube','Void cube','Geared','Mixed-shape'])
shelf_tw={'n':'Twisty puzzles','k':[cube,noncube,fast,smart,shape]}

# ---- 3 mechanical by family
LILLY='https://blogs.libraries.indiana.edu/lilly/2025/04/02/what-are-mechanical-puzzles/'
MP=WP+'Mechanical_puzzle'
tang=copy.deepcopy(mx['Tangram']); tang['y']='late 1700s'
tang['v']=[V('Earliest extant set','','1802','given to Francis Waln'),V('First use of the word tangram','','1848','Thomas Hill'),V('The Anchor Puzzle','F. Ad. Richter','1891','German edition')]
put=K('Put-together puzzle','Loose pieces are assembled into a target shape, such as a silhouette, a cube or a rectangle.',LILLY,[
  tang,
  A('Soma cube','Seven pieces of three or four unit cubes that build a 3x3x3 cube, devised by Piet Hein during a lecture.','Piet Hein','1933',WP+'Soma_cube',dt='wood or plastic · colours'),
  A('Pentomino set','The twelve shapes made of five squares, named by Solomon Golomb; sold as puzzles and games.','','1953',WP+'Pentomino',
    v=[V('Golomb\'s Game','Solomon Golomb','','8x8 grid game'),V('Universe','Parker Brothers','1966','four sets of pentominoes'),V('Lonpos','','','pentominoes on different boards')],dt='material · board size'),
  A('Katamino','Gigamic game of polyomino pieces, from the French publisher Gigamic.','Gigamic','',WP+'Gigamic')],
  a='assembly puzzle · dissection puzzle',t=['Two-dimensional dissection','Three-dimensional packing'])
htrick=copy.deepcopy(mx['Japanese puzzle box (himitsu-bako)'])
take=K('Take-apart & trick-opening puzzle','A puzzle to open or take apart, such as a trick box or lock, with a hidden sequence of moves.',LILLY,[
  htrick,
  A('Karakuri Creation Group boxes','Trick boxes and wooden interlocking puzzles by twelve craftsmen in Hakone, sold as Karakuri Boxes.','Karakuri Creation Group','',
    'https://karakuri.gr.jp/en/about-kgc',v=[V('Hakone Karakuri Museum','Karakuri Creation Group','2013','opened in Hakone')],dt='number of moves · marquetry · size'),
  A('Akio Kamei trick box','Boxes shaped like everyday objects with hidden openings, based on kumiki interlocking puzzles; Kamei began making trick boxes in 1981.','Akio Kamei','1981','https://karakuri.gr.jp/creation/kamei/kamei.htm',
    v=[V('Karakuri Yasubei established','Akio Kamei','1981',''),V('Chairman of the Karakuri Creation Group','Akio Kamei','2011','')]),
  A('Constantin puzzle box','Wooden trick boxes with wheels, sliding panels and metal balls from Jean-Claude Constantin.','Jean-Claude Constantin','','https://kubiyagames.com/blogs/mechanical-puzzles-blog/more-puzzles-from-jean-claude-constantin',
    v=[V('PLD Puzzle Box','Jean-Claude Constantin','',''),V("Einstein's Spider Box",'Jean-Claude Constantin','',''),V('Viking Puzzle Box','Jean-Claude Constantin','',''),V('Secret Red Puzzle Box','Jean-Claude Constantin','','')],dt='moves · wood · size'),
  A('Trick puzzle lock','A lock that opens only by an unusual sequence of moves, often with hundreds of steps.','','',MP,
    v=[V('Alpha Puzzle Lock','Jean-Claude Constantin','',''),V('Sliding Lock Puzzle','Jean-Claude Constantin','',''),V('300 Move Void Lock Puzzle','Jean-Claude Constantin','',''),V('250 Move Schloss Puzzle Lock','Jean-Claude Constantin','','')]),
  A('Revival studio puzzle box','Hand-made boxes by Akio Kamei, Trevor Wood and Frank Chambers, who revived the art in the 1980s.','','1980s',WP+'Puzzle_box')],
  a='puzzle box · secret box · trick box',t=['Secret box','Trick lock','Match safe'])
six=copy.deepcopy(mx['Six-piece burr'])
six['a']='Chinese cross · puzzle knot'; six['y']='1698 engraving'
six['d']='Interlocking notched square sticks forming three crossed pairs; oldest known burr, first seen in a 1698 engraving.'
six['v']=[V('Altekruse','','1890','named after the patent holder; older puzzle'),V('Chuck','Edward Nelson','1897','patent'),V('Pagoda burr','','1928','described in Wyatt\'s Puzzles in Wood'),V('Cutler analysis','Bill Cutler','1978','published by Martin Gardner in Scientific American')]
six['dt']='level (moves to remove first piece) · notch pattern · wood'
inter=K('Interlocking puzzle','Pieces hold each other in place and must be separated, then reassembled; burrs are the classic form.',LILLY,[
  six,
  A('High-level burr','Six-piece burr needing many moves to free the first piece, found by computer-aided designers.','','1979',WP+'Burr_puzzle',
    v=[V('Level-3 burr','Stewart Coffin','1979',''),V('Level-5 burr','Bill Cutler','1985','highest possible with notchable pieces'),V('Level-7 burr','Philippe Dubois','','shortly after 1985')],dt='level'),
  A('Diagonal burr','Burr with V-shaped notches cut at 45 degrees, also called Giant Star.','','',WP+'Burr_puzzle',a='Giant Star')],
  a='burr · wood knot puzzle',t=['Six-piece burr','Larger burr','Diagonal burr'])
cast=copy.deepcopy(mx['Hanayama Cast puzzle'])
cast['d']='Metal cast disentanglement and lock puzzles, rated 1 (fun) to 6 (grandmaster).'
cast['v']=[V('Cast Marble','Hanayama','',''),V('Cast Infinity','Hanayama','',''),V('Cast Quartet','Hanayama','',''),V('Cast Coaster','Hanayama','',''),V('Cast NEWS','Hanayama','','')]
cast['dt']='difficulty level 1-6 · designer (e.g. Oskar van Deventer) · finish'
disent=K('Disentanglement puzzle','A ring, loop or wire object must be freed from another, or two linked pieces separated.',LILLY,[
  cast,
  A('Chinese rings','A loop on rings and pillars, solved by a binary move sequence; also Baguenaudier and Cardan\'s rings.','','early 16th century',WP+'Baguenaudier',
    v=[V('Yang Shen reference','','early 1500s','nine linked rings toy'),V('Luca Pacioli','','1509','De Viribus Quantitatis')],a='Baguenaudier · Cardan\'s rings'),
  A('Wire disentanglement puzzle','Bent wire pieces, vexiers and derringer puzzles, separated by working shapes through each other.','','',MP)],
  a='wire puzzle · cast puzzle',t=['Cast metal','Wire','Rope and string'],
  m=[m for m in mech['m'] if m[0] not in ('Katamino','Cast Quartet','Cast News')],r=mech['r'])
seq=K('Sequential movement puzzle','Repeated sliding or moving of parts reaches a target arrangement, as in sliding blocks and disk-moving puzzles.',LILLY,[
  copy.deepcopy(mx['Tower of Hanoi']),
  A('15 puzzle','Sliding-tile puzzle on a 4x4 frame; Noyes Chapman is credited with it, and it was a US fad in 1880.','Noyes Chapman','1880',WP+'15_puzzle',
    v=[V('Gem Puzzle','Matthias Rice','1880','popularised in Boston'),V('Sam Loyd $1,000 challenge','Sam Loyd','','impossible swap of tiles 14 and 15')],a='Gem Puzzle · Boss Puzzle · Game of Fifteen · Mystic Square'),
  A('Klotski','Sliding-block puzzle with one large piece to bring to an exit; from Huarong Dao and L\'Âne rouge.','','',WP+'Klotski',
    v=[V('Pennant Puzzle','Lewis W. Hardy','1909','copyrighted in Chicago'),V('Huarong Dao','','1938','earliest Chinese account'),V('Fleming patent GB 411515','John Harold Fleming','1934','79-step solution'),V('Basic Klotski','','','81-move minimum, Hordern code C27d')],a='Huarong Dao · L\'Âne rouge · Daughter in the Box',dt='layout · minimum moves'),
  A('Rush Hour','Sliding-block puzzle in which cars are moved to free a red car; invented by Nob Yoshigahara.','Nob Yoshigahara','1970s',WP+'Rush_Hour_(puzzle)',
    v=[V('US sale','ThinkFun','1996','sold in the United States'),V('Regular Edition','ThinkFun','','40 puzzles')],dt='edition · challenge count')],
  a='sliding puzzle · sliding-block puzzle',t=['Sliding tiles','Sliding blocks','Disk-moving'])
dex=K('Dexterity puzzle','A ball or object is guided by hand, usually by tilting or twisting, along a maze to a goal.',LILLY,[
  A('Perplexus','Handheld sphere with a 3D track; the player twists it to guide a steel ball through a maze; first sold as Superplexus.','Spin Master','2001',WP+'Perplexus',
    v=[V('Original (renamed Beast)','Perplexus LLC','2019','rebranded in 2019'),V('Rookie (renamed Rebel)','Perplexus LLC','2019','rebranded in 2019'),V('Epic','Perplexus LLC','',''),V('Perplexus LLC owned by Spin Master','Spin Master','2017','')],a='Superplexus',dt='version · track count'),
  A('Labyrinth tilt maze','Maze board tilted by two knobs to roll a steel marble to the end without falling in holes; Brio made it from 1946.','Brio','1946',WP+'Labyrinth_(marble_game)',
    v=[V('US introduction','Brio','c. 1950','')],dt='suspended knobs or handheld')],
  a='ball-in-maze · tilt puzzle',t=['Tilt-box maze','Handheld sphere maze'])
vessel=K('Puzzle vessel','A drinking vessel that is hard to drink from or pour without spilling.',LILLY,[
  A('Puzzle jug','Jug with a perforated neck and hidden tube, popular in the 17th and 18th centuries; the drinker must block holes to drink.','','c. 1300 (Exeter jug)',WP+'Puzzle_jug',
    v=[V('Exeter puzzle jug','','c. 1300','earliest English example, made in Saintonge, France')]),
  A('Fuddling cup','Drinking puzzle of linked cups, an ancestor that works differently from the puzzle jug.','','',WP+'Puzzle_jug'),
  A('Pot crown','Drinking puzzle that works differently from the puzzle jug.','','',WP+'Puzzle_jug')],
  a='trick vessel · puzzle jug',t=['Jug','Cup'])
imp=K('Impossible object','An object that seems too large or too complex to have been put where it sits, such as a ship inside a bottle.',LILLY,[
  A('Ship in a bottle','Model ship built inside a bottle; the oldest survivors are by Giovanni Biondo, dated 1784, 1786 and 1792.','Giovanni Biondo','late 18th century',WP+'Ship_in_a_bottle',
    v=[V('Biondo dated examples','Giovanni Biondo','1784-1792','1784, 1786 and 1792')]),
  A('Fruit in a bottle','Fruit grown or dried inside a bottle, as with Poire Williams pear brandy.','','',WP+'Ship_in_a_bottle'),
  A('Object in a bottle','Cards, padlocks, knots, scissors or a Rubik\'s Cube placed inside a bottle that looks too narrow.','','',WP+'Ship_in_a_bottle')],
  a='impossible bottle',t=['Ship in a bottle','Fruit in a bottle','Padlock or knot in a bottle'])
fold=K('Folding puzzle','A paper or tile object that is folded into a target shape or picture.',LILLY,[
  A("Rubik's Magic",'Eight square tiles on wires in a 2x4 rectangle that fold into shapes; patented by Rubik in 1985 and 1987.',"Rubik's",'1987',WP+"Rubik%27s_Magic",
    v=[V('Matchbox edition','Matchbox','1987',''),V('Master Edition 2x6','Matchbox','1987','12 tiles'),V('Oddzon re-release','Oddzon','1996','')],dt='tile count · colour'),
  A('Flexagon','Folded paper strip that can be flexed to show faces besides front and back; found by Arthur Stone.','','1939',WP+'Flexagon',
    v=[V('Martin Gardner article','Martin Gardner','1956','December Scientific American'),V('Hexmo','Russell Rogers and Leonard D\'Andrea','1959','patented hexahexaflexagon')],dt='faces · sides'),
  A('Paper fold puzzle','Paper folded to form a target picture, such as a Vesa Timonen puzzle or a folding map.','','2002',MP)],
  a='fold puzzle',t=['Tile folder','Paper flexagon'])
logic=K('Single-player logic game','A boxed solitaire puzzle with a set of challenges, solved by logic and spatial reasoning.',LILLY,[
  A('Peg solitaire','Pegs jump over each other on a board until one is left; English board 33 holes, French board 37.','','1697',WP+'Peg_solitaire',
    v=[V('Mercure galant description','','1697','first known print reference'),V('English board','','','33 holes'),V('French board','','','37 holes')],a='solitaire board game'),
  A('ThinkFun logic puzzle','Boxed logic puzzles from ThinkFun, formerly Binary Arts, with graded challenge cards.','ThinkFun','1985',WP+'ThinkFun',
    v=[V('Gravity Maze','ThinkFun','',''),V('Chocolate Fix','ThinkFun','','')],dt='edition · challenge count'),
  A('SmartGames IQ puzzle','Single-player logic puzzles from Smart Games of Belgium, with challenge booklets.','Smart Games','1992',WP+'Smart_Games',
    v=[V('Penguins on Ice','Smart Games','',''),V('Squirrels Go Nuts!','Smart Games','',''),V('Quadrillion','Smart Games','','')],dt='series · challenge count')],
  a='logic puzzle · brain teaser',t=['Peg board','Challenge-card puzzle'])
shelf_me={'n':'Mechanical puzzles by family','k':[put,take,inter,disent,seq,dex,vessel,imp,fold,logic]}

# ---- 4 fidgets
FT=WP+'Fidget_toy'
spin=K('Spinner','A hand-held toy that spins freely around a central bearing or axis.',WP+'Hand_spinner',[
  A('Three-lobed bearing spinner','Three-lobed body spinning on a central ball bearing; boomed in 2017, mostly made in China.','','2017',WP+'Fidget_spinner',
    v=[V('Pavelsky design patent','David Pavelsky','2017','October, three-lobed spinner')],dt='lobes · bearing · metal or plastic'),
  A('Torqbar','Metal spinner Scott McCoskery developed to fidget in meetings; provisional patent 2016, utility patent March 2018.','','2014',WP+'Fidget_spinner'),
  A('Hettinger spinning toy','Finger-frisbee spinning toy with no central bearing; patent filed 1993, issued 1997, lapsed 2005; wrongly credited as the spinner\'s invention.','','1993',WP+'Fidget_spinner')],
  a='hand spinner · fidget spinner',t=['Three-lobe','Two-lobe','Metal','Plastic','Spinner ring'])
click=K('Clicker & button fidget','A hand-held toy of buttons, switches and dials to click, press and flip.',FT,[
  A('Fidget Cube','Six-sided cube of switch, gears, rolling ball, joystick, spinning disk, worry stone and five buttons; funded on Kickstarter in 2016.','Antsy Labs','2016',WP+'Fidget_Cube',
    v=[V('Kickstarter campaign','Antsy Labs','2016','tenth among highest-funded crowdfunding projects at the time')],dt='sides · button type'),
  A('Coster bubble-popping toy','Mechanical design for a toy of pushable bubbles by Theo and Ora Coster of Theora Concepts, an Israeli couple, in 1975.','Theora Concepts','1975',WP+'Pop_it'),
  A('FoxMind Pop It','Silicone bubble board; FoxMind acquired the toy in 2009 and showed it as a logic game at the 2014 toy fairs.','FoxMind','2014',WP+'Pop_it',
    v=[V('FoxMind acquires the toy','FoxMind','2009',''),V('Toy Fairs launch','FoxMind','2014','Nuremberg and New York'),V('Target launch as Pop It!','FoxMind and Buffalo Games','2019','sold as Speedy Pop It!, in all US Target stores')],a='pop-it')],
  a='fidget cube · pop it',t=['Pop it','Fidget cube','Fidget keychain'])
slide=K('Slider & haptic fidget','A pocket metal slider that moves back and forth against magnet resistance, sold for everyday carry.',
 'https://frankiesautoelectrics.com.au/products/adhix-adxdrift-magnetic-slider-fidget-toy-edc-stainless-steel-drift-push-slider',[
  A('Magnetic push slider','Machined stainless-steel slider with embedded magnets that give resistance and a quiet glide.','','','https://frankiesautoelectrics.com.au/products/adhix-adxdrift-magnetic-slider-fidget-toy-edc-stainless-steel-drift-push-slider',dt='metal · magnet count · size')],
  a='EDC fidget slider',t=['Magnetic slider','Haptic slider'])
squeeze=K('Squeeze toy','A soft toy squeezed in the hand to relieve tension, usually under about 7 cm.',WP+'Stress_ball',[
  A('Stress ball','Squeezable ball up to about 7 cm in foam rubber, bean bag or silicone, often printed for promotion.','','',WP+'Stress_ball',dt='foam · bean bag · silicone'),
  A('Squishy','Slow-rising foam or rubber squeeze toy from Japan; reached the US in spring 2017.','','',WP+'Squishy',v=[V('Mochi squishy','','','small silicone toy in animal or food shapes')]),
  A('NeeDoh','Squeeze toy filled with non-toxic dough-like material.','','',WP+'Stress_ball')],
  a='stress ball · squishy',t=['Foam','Bean bag','Silicone','Dough-filled'])
flip=K('Flip & twist fidget','A toy of linked parts that fold, flip or twist in the hands without a goal.',FT,[
  A('Tangle','Interlocking curved links that twist into endless shapes; made by Tangle Creations from 1981.','Tangle Creations','1981','https://toybook.com/backstory-tangle-the-original-fidget-was-40-years-ahead-of-the-curve',
    v=[V('TOMY Infinite Structural Puzzle','Tomy','1983','sold two years in Japan'),V('Tangle Jr.','James Industries','1989','distribution deal'),V('ZURU licence','ZURU','2017','two-year deal')],dt='links · colour · size'),
  A('Infinity cube','Cube of linked smaller cubes, 2x2x2 in shape, that can be folded and opened from different sides; six configurations.','','',WP+'Infinity_cube'),
  A("Rubik's Snake",'Chain of 24 right-angled triangular prisms joined by spring bolts, twisted into shapes; by Ernő Rubik.',"Rubik's",'1981',WP+'Rubik%27s_Snake')],
  a='infinity cube · twisty fidget',t=['Infinity cube','Linked-chain'])
worry=K('Worry & hand-rolling object','A smooth object rolled, rubbed or counted in the hand; secular worry beads only, as prayer beads sit in faith objects.',FT,[
  A('Baoding balls','Pairs of hollow metal balls with a chime, rotated in the palm; named after Baoding, China, from the Ming dynasty.','','Ming dynasty',WP+'Baoding_balls',
    v=[V('Cloisonné','','','decorative'),V('Stone (jade, agate, marble)','','','solid')],dt='material · diameter (about 45 mm to start)'),
  A('Worry stone','Smooth polished gemstone, about 3 cm, rubbed with the thumb; folk origins are claimed but unconfirmed.','','',WP+'Worry_stone'),
  A('Komboloi','Greek and Cypriot worry beads with no religious use, in amber, faturan or coral; from the komboskoini prayer rope.','','',WP+'Komboloi',dt='bead material · bead count')],
  a='worry beads · worry stone',t=['Baoding balls','Worry stone','Worry beads'])
shelf_fi={'n':'Fidgets','k':[spin,click,slide,squeeze,flip,worry]}

# ---- 5 desk
cradle=K("Newton's cradle",'A row of hanging steel balls that pass a knock along, shown on a desk as a momentum demonstration.',WP+"Newton%27s_cradle",[
  A("Prebble wooden Newton's cradle",'Wooden version named and sold by Simon Prebble\'s Scientific Demonstrations Ltd; Harrods first sold them.','Scientific Demonstrations Ltd','1967',WP+"Newton%27s_cradle"),
  A("Mariotte's impact demonstration",'Edme Mariotte\'s 17th-century demonstration of the law of impacts, presented to the French Academy in 1671.','','1671',WP+"Newton%27s_cradle")],
  a='executive pendulum',t=['Wooden frame','Chrome frame'])
mag=K('Magnet sphere set','A set of small neodymium spheres or cubes that link into shapes on a desk.',WP+'Neodymium_magnet',[
  A('Buckyballs','Desk-toy sets of up to 216 high-powered magnets, sold by Maxfield & Oberton; recalled and then sued by the CPSC.','Maxfield & Oberton','2009',
    'https://www.cpsc.gov/Newsroom/News-Releases/2012/cpsc-sues-maxfield-oberton-over-hazardous-buckyballs-and-buckycube-desk-toys-action',
    v=[V('Recall of 175,000 sets','Maxfield & Oberton','2010','labelled Ages 13+, below the F963-08 toy standard'),V('CPSC administrative complaint','CPSC','2012','filed 25 July after ingestion injuries'),V('Buckycubes','Maxfield & Oberton','','cube-shaped set')],dt='magnet count · sphere size · colour')],
  a='magnetic desk toy',t=['Spheres','Cubes'])
slinky=K('Coil spring toy','A helical spring toy that steps down stairs; the Slinky is the icon.',WP+'Slinky',[
  A('Slinky','Steel coil toy invented by Richard James in 1943; first sold at Gimbels in Philadelphia on 27 November 1945.','James Industries','1943',WP+'Slinky',
    v=[V('Gimbels demonstration','James Industries','1945','first 400 sold in 90 minutes'),V('American Toy Fair debut','James Industries','1946',''),V('Move to Hollidaysburg','James Industries','1964','')],dt='metal or plastic · length')],
  a='Slinky',t=['Steel','Plastic'])
bird=K('Drinking bird','A glass bird that bobs into a cup of water, driven by evaporation heat difference.',WP+'Drinking_bird',[
  A('Hillery and Sullivan drinking bird','Glass bird with a felt head and liquid in the body, patented by Arthur Hillery in 1945 and by Miles Sullivan of Bell Labs.','','1945',WP+'Drinking_bird',
    v=[V('Hillery patent','Arthur M. Hillery','1945','acetone as working fluid'),V('Sullivan patent','Miles V. Sullivan','1946','Bell Labs'),V('Plate design patent','Robert T. Plate','1947','')]),
  A('Insatiable birdie','Chinese toy of the 1910s to 1930s described by Yakov Perelman.','','1910s-1930s',WP+'Drinking_bird')],
  a='dipping bird',t=['Glass'])
sand=K('Kinetic sand & sand art','Sand-based desk and play objects, from hydrophobic sand to coloured-sand pictures between glass.',WP+'Sand_art_and_play',[
  A('Kinetic Sand','Moldable sand toy, a trademark produced by Spin Master.','Spin Master','',WP+'Kinetic_sand'),
  A('Magic sand','Sand coated with trimethylsilanol vapour so it stays dry in water; first referenced in 1915.','','1915',WP+'Kinetic_sand'),
  A('Moving sand art','Coloured sand between glass sheets that forms pictures when the frame is turned.','','',WP+'Sand_art_and_play'),
  A('Sand picture in a bottle','Scenes made by pouring coloured sand into a bottle.','','',WP+'Sand_art_and_play')],
  a='moving sand · sand art',t=['Moulding sand','Framed sand picture','Bottle'])
shelf_de={'n':'Desk & executive toys','k':[cradle,mag,slinky,bird,sand]}

dept={'n':'Puzzles, fidgets & desk toys','mode':'variety',
 'note':'Objects only: puzzle-solving and speedcubing as pursuits live in separate taxonomies.',
 'b':[{'m':'Difficulty rating','v':'Hanayama 1 (fun) to 6 (grandmaster)','w':'Hanayama grades its Cast puzzles on one scale (Hanayama article).'},
      {'m':'Burr level','v':'moves needed to free the first piece; 5 is the highest with notchable pieces','w':'Cutler and Coffin measure for six-piece burrs (Burr puzzle article).'},
      {'m':'Order of a cube puzzle','v':'2x2x2 up to 17x17x17 and beyond','w':'Layers per side; named sizes are official Rubik\'s variants (Rubik\'s Cube article).'},
      {'m':'Piece count and cut','v':'die-cut or hand-cut; about 38 x 27 for 1,000 pieces','w':'Collectors prize hand-cut wooden jigsaws (Jigsaw puzzle article).'}],
 's':[shelf_jig,shelf_tw,shelf_me,shelf_fi,shelf_de]}
idx=d['depts'].index(board)
d['depts'].insert(idx+1,dept)

# ---- skill toys
sk['n']='Skill toys'
keep=['Yo-yo','Spinning top','Kendama','Toy flying disc','Toy kite','Toy ball','Bubble toy']
sk['k']=[oldsk[n] for n in keep]
el=K('Electronic handheld toy','A battery toy with built-in lights, sounds or a small display for one fixed game or pet; no screen game software.',WP+'Handheld_electronic_game',[
  A('Mattel Auto Race','Red-LED racing game from 1976, called the first handheld electronic game to use only solid-state electronics; designed by George Klose.','Mattel','1976',WP+'Mattel_Auto_Race'),
  A('Simon','Memory game of four lit coloured buttons that play tones, by Ralph Baer and Howard Morrison; sold 1.5 million by 1979.','Milton Bradley','1978',WP+'Simon_(game)',
    v=[V('Super Simon','Milton Bradley','',''),V('Pocket Simon','Milton Bradley','',''),V('Simon Swipe','Hasbro','','')]),
  A('Merlin','Handheld with six games on 11 lit buttons from Parker Brothers.','Parker Brothers','1978',WP+'Handheld_electronic_game'),
  A('Game & Watch','Nintendo single-game LCD handhelds with a clock, designed by Gunpei Yokoi; Ball launched 28 April 1980.','Nintendo','1980',WP+'Game_%26_Watch',
    v=[V('Ball','Nintendo','1980','28 April'),V('Donkey Kong','Nintendo','','about 8 million sold')],dt='game · screen · production run to 1991'),
  A('Bop It','Hand-held toy that calls commands such as Bop it, Twist it and Pull it; invented by Dan Klitsner.','Hasbro','1996',WP+'Bop_It'),
  A('Tamagotchi','Egg-shaped digital pet by Akihiro Yokoi and Aki Maita; launched in Japan on 23 November 1996.','Bandai','1996',WP+'Tamagotchi',
    v=[V('US release','Bandai','1997','1 May')],dt='generation · shell')],
  a='handheld electronic game · LCD game',t=['LED game','LCD game','Digital pet','Memory game'])
sk['k'].append(el)
skill['note']='Yo-yos, tops and kendama have hobby communities; party toys are tier.'
for s in skill['s']:
    if s['n']=='Skill toys & fidgets': s['n']='Skill toys'

# ---- brands
B=br['b']; have={b['n'].lower() for b in B}
def add(n,c,f,seg,kf,dd,s,sig=None,rel=None,lines=None):
    if n.lower() in have: print('dup',n); return
    e={'n':n,'c':c,'f':f,'seg':seg,'kf':kf,'d':dd}
    if lines: e['lines']=lines
    if sig: e['sig']=sig
    if rel: e['rel']=rel
    e['s']=s; B.append(e); have.add(n.lower())
SC='https://ca.speedcube.com.au/blogs/speedcube-brands'
add('DaYan','China','','Specialist','speedcubes','Speedcube maker whose Guhong and Zhanchi cubes led the field around 2011 to 2015.',SC,sig=['DaYan Guhong and Zhanchi'],rel=['Gancube','MoYu','QiYi'])
add('MoYu','China','','Specialist','speedcubes','One of the leading cube brands in China; MoFang JiaoShi is its budget subsidiary.',SC,sig=['MoYu cubes'],lines=['MoFang JiaoShi (MFJS)'],rel=['Gancube','QiYi','DaYan'])
add('QiYi','China','','Specialist','budget speedcubes','Cube maker that came to prominence in 2018; sub-brands X-Man, MoFangGe and VALK.',SC,sig=['QiYi X-Man Tornado'],lines=['X-Man','MoFangGe','VALK'],rel=['Gancube','MoYu'])
add('YJ','China','','Specialist','twisty puzzles','YongJun, an educational toy company designing cubes and puzzles since 2005; MGC is a sub-brand.',SC,sig=['YJ and MGC cubes'],lines=['MGC'])
add('ThinkFun','United States','1985','Specialist','logic puzzles','Alexandria, Virginia puzzle company, formerly Binary Arts, owned by Ravensburger since 2017.',WP+'ThinkFun',sig=['ThinkFun logic puzzle','Rush Hour'],lines=['Rush Hour','Gravity Maze','Chocolate Fix'],rel=['Ravensburger'])
add('Smart Games','Belgium','1992','Specialist','logic puzzles','Kontich puzzle maker of the SmartGames IQ series.',WP+'Smart_Games',sig=['SmartGames IQ puzzle'],lines=['IQ series','Penguins on Ice','Quadrillion'])
add('Karakuri Creation Group','Japan','','Artisan & independent','trick boxes','Hakone group of twelve craftsmen making trick boxes and wooden interlocking puzzles.','https://karakuri.gr.jp/en/about-kgc',sig=['Karakuri Creation Group boxes'],rel=['Akio Kamei'])
add('Jean-Claude Constantin','','','Artisan & independent','puzzle designer','Designer of trick boxes, puzzle locks and maze puzzles, retailers call him the best-known contemporary puzzle designer.','https://kubiyagames.com/blogs/mechanical-puzzles-blog/more-puzzles-from-jean-claude-constantin',sig=['Constantin puzzle box'])
add('Antsy Labs','United States','','Specialist','Fidget Cube','Design studio of brothers Matthew and Mark McLachlan, makers of the Fidget Cube.',WP+'Fidget_Cube',sig=['Fidget Cube'])
add('Tangle Creations','United States','1981','Specialist','Tangle','Maker of the Tangle toy designed by Richard X. Zawitz.','https://toybook.com/backstory-tangle-the-original-fidget-was-40-years-ahead-of-the-curve',sig=['Tangle'])
add('Spin Master','Canada','1994','Mainstream','toys, Perplexus','Toronto toy company that owns Perplexus, Kinetic Sand and the Rubik\'s Cube brand.',WP+'Spin_Master',sig=['Perplexus','Kinetic Sand'],rel=["Rubik's"])
add('Milton Bradley','United States','1860','Heritage manufactory','games, Simon','Springfield game company bought by Hasbro in 1984; maker of Simon.',WP+'Milton_Bradley_Company',sig=['Simon'],rel=['Hasbro'])
add('Gigamic','France','1991','Specialist','abstract games','French publisher of Quarto, Quoridor and Katamino.',WP+'Gigamic',sig=['Katamino'])
add('Maxfield & Oberton','United States','','Specialist','magnet desk toys','New York maker of Buckyballs and Buckycubes, subject of a 2012 CPSC complaint.','https://www.cpsc.gov/Newsroom/News-Releases/2012/cpsc-sues-maxfield-oberton-over-hazardous-buckyballs-and-buckycube-desk-toys-action',sig=['Buckyballs'])
add('James Industries','United States','','Heritage manufactory','Slinky','Pennsylvania company founded by Richard and Betty James to sell the Slinky.',WP+'Slinky',sig=['Slinky'],rel=['Tangle Creations'])
D='Artisan & independent'
add('Oskar van Deventer','Netherlands','1965',D,'puzzle designer','Dutch puzzle designer of the Gear Cube and Redi Cube, and Hanayama puzzles.',WP+'Oskar_van_Deventer',sig=['Gear Cube','Redi Cube'],rel=['Hanayama'])
add('Stewart Coffin','United States','',D,'puzzle designer','American maker of over 500 polyhedral wooden puzzles, including Hectix.',WP+'Stewart_Coffin',sig=['High-level burr'])
add('Bill Cutler','','',D,'puzzle designer','Analysed the six-piece burr by computer, published by Martin Gardner in 1978.',WP+'Burr_puzzle',sig=['Six-piece burr','High-level burr'])
add('Akio Kamei','Japan','1948',D,'puzzle designer','Osaka-born trick-box maker who began in 1981 and chairs the Karakuri Creation Group.','https://karakuri.gr.jp/creation/kamei/kamei.htm',sig=['Akio Kamei trick box'],rel=['Karakuri Creation Group'])
add('Nob Yoshigahara','Japan','1936',D,'puzzle designer','Japanese puzzle inventor who licensed Rush Hour to Binary Arts, now ThinkFun.',WP+'Nob_Yoshigahara',sig=['Rush Hour'],rel=['ThinkFun','Hanayama'])
add('Ernő Rubik','Hungary','1944',D,'puzzle designer','Hungarian inventor of the Rubik\'s Cube, Magic and Snake.',WP+'Ern%C5%91_Rubik',sig=["Rubik's Cube","Rubik's Magic","Rubik's Snake"],rel=["Rubik's"])
add('Jerry Slocum','United States','1931',D,'puzzle collector and author','Collector and author whose puzzles went to Indiana University in 2006; co-created the puzzle classification with Jack Botermans.',WP+'Jerry_Slocum')
add('Piet Hein','Denmark','',D,'puzzle designer','Danish polymath who devised the Soma cube in 1933.',WP+'Soma_cube',sig=['Soma cube'])
add('Uwe Mèffert','Germany','1939',D,'puzzle designer','Puzzle designer and seller in Hong Kong; Pyraminx, Megaminx, Skewb, Gear Cube.',WP+'Uwe_M%C3%A8ffert',sig=['Pyraminx','Megaminx','Skewb'])
# update existing
for b in B:
    if b['n']=='Ravensburger' and not b.get('s'): b['s']=WP+'Ravensburger'
    if b['n']=='Gancube': b['rel']=['DaYan','MoYu','QiYi']; b['d']='Guangzhou speedcube maker (GAN) founded in 2014 by Jiang Ganyuan.'

# ---- write
def save(p,o):
    t=p+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,separators=(',',':')); os.replace(t,p)
save(R+'out/E1.json',d); save(R+'out/E1_brands.json',br)
print('written')
