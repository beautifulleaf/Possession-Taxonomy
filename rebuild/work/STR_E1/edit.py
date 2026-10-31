import json, re, os, copy, shutil, sys
ROOT = '/home/user/Possession-Taxonomy/rebuild/'
P = ROOT + 'out/E1.json'
BAK = ROOT + 'work/STR_E1/bak/E1.json'
d = json.load(open(BAK))           # always rebuild from the backup (idempotent)
before = dict(dep=len(d['depts']), shelves=sum(len(x['s']) for x in d['depts']),
              kinds=sum(len(s['k']) for x in d['depts'] for s in x['s']),
              arch=sum(len(k.get('x', [])) for x in d['depts'] for s in x['s'] for k in s['k']))
K = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            K[k['n']] = k
used = set()
W = 'https://en.wikipedia.org/wiki/'

def kd(n):
    used.add(n)
    return K[n]

def newkind(n, dfn, s, a='', tt=None, x=None, see=None, tg=None):
    k = {'n': n, 'a': a, 'd': dfn, 's': s}
    if tt: k['tt'] = tt
    if x: k['x'] = x
    if see: k['see'] = see
    K[n] = k
    used.add(n)
    return k

def arch(n, dfn, s, mk='', y='', v=None, a='', dt=''):
    o = {'n': n, 'a': a, 'd': dfn, 'mk': mk, 'y': y, 's': s, 'v': v or []}
    if dt: o['dt'] = dt
    return o

def demote(kname, anames, group='Named forms'):
    """remove generic archetypes from a kind, keeping their names as types"""
    k = K[kname]
    keep, moved = [], []
    for x in k.get('x', []):
        (moved if x['n'] in anames else keep).append(x)
    assert len(moved) == len(anames), (kname, anames, [x['n'] for x in k.get('x', [])])
    k['x'] = keep
    if not keep: k.pop('x')
    k.setdefault('_demoted', []).extend(x['n'] for x in moved)
    return moved

def setk(n, **kw):
    k = kd(n)
    for a, b in kw.items():
        if b is None: k.pop(a, None)
        else: k[a] = b
    return k

def shelf(n, t, ax, kinds):
    return {'n': n, 't': t, 'ax': ax, 'k': kinds}

# ---------------------------------------------------------------- generic demotions (generic descriptions, not named things)
DEMOTE = {
 'Interlocking puzzle': ['Six-piece burr', 'High-level burr', 'Diagonal burr'],
 'Impossible object': ['Ship in a bottle', 'Fruit in a bottle', 'Object in a bottle'],
 'Disentanglement puzzle': ['Wire disentanglement puzzle'],
 'Take-apart & trick-opening puzzle': ['Trick puzzle lock'],
 'Folding puzzle': ['Paper fold puzzle'],
 'Toy kite': ['Delta kite', 'Diamond kite', 'Box kite', 'Sled kite', 'Parafoil kite', 'Malay kite', 'Rokkaku kite', 'Fighter kite'],
 'Draughts set': ['International draughts set', 'English draughts set', 'Russian draughts set', 'Brazilian draughts set', 'Canadian checkers set'],
 'Xiangqi set': ['Traditional-character xiangqi set', 'Simplified-character xiangqi set', 'Same-character xiangqi set', 'Different-character xiangqi set'],
 'Baby doll': ['Reborn doll'],
 "Dolls' house miniatures": ['1:12 miniatures', '1:24 miniatures', '1:48 miniatures', '1:18 play-scale miniatures'],
 'Marble': ['Steelie', 'Contemporary art marble', 'German handmade glass marble', 'Clay and china marble'],
 'Game clock': ['Mechanical chess clock', 'Digital chess clock', 'Byo-yomi timer'],
 'Model railway controller': ['Analogue DC controller', 'DCC command station'],
 'Model railway decoder': ['DCC locomotive decoder', 'DCC accessory decoder'],
 'Point motor': ['Solenoid point motor', 'Slow-action stall motor'],
 'Toy ball': ['Utility ball'],
 'Juggling ball': ['Beanbag juggling ball', 'Stage ball', 'Bouncing ball'],
 'Juggling club': ['American-style wooden club', 'European club', 'One-piece plastic club', 'Multi-piece composite club'],
 'Devil stick': ['Tapered devil stick'],
 'Poi': ['Sock poi', 'Rope-and-ball poi'],
 'Yo-yo': ['Ball-bearing yo-yo'],
 'Bobblehead': ['Baseball bobblehead'],
 'Toy soldier & animal figure': ['Flat tin figure', 'Composition figures', 'Plastic toy soldiers'],
 'Bubble toy': ['Bubble ring'],
 'Dice set': ['Polyhedral RPG dice set'],
 'Table shuffleboard': ['Table shuffleboard'],
 'Novuss board': ['Novuss'],
}
# Domino archetypes by name
DOM = [x['n'] for x in K['Domino set'].get('x', [])]
DEMOTE['Domino set'] = DOM
demoted_log = []
for kn, an in DEMOTE.items():
    moved = demote(kn, an)
    demoted_log += [(kn, x['n']) for x in moved]

# ================================================================ FIDGETS (showcase)
fid_src = W + 'Fidget_toy'
old_spin = kd('Spinner'); old_click = kd('Clicker & button fidget'); old_slide = kd('Slider & haptic fidget')
old_sq = kd('Squeeze toy'); old_flip = kd('Flip & twist fidget'); old_worry = kd('Worry & hand-rolling object')
snake = [x for x in old_flip['x'] if x['n'] == "Rubik's Snake"][0]
tangle = [x for x in old_flip['x'] if x['n'] == 'Tangle'][0]
infcube = [x for x in old_flip['x'] if x['n'] == 'Infinity cube'][0]
infcube['mk'] = ''; infcube['d'] = 'Cube of linked smaller cubes, 2x2x2 in shape, that opens and folds back from different sides; six configurations.'
infcube['s'] = W + 'Infinity_cube'
spin_x = {x['n']: x for x in old_spin['x']}
pav = arch('Pavelsky three-lobed spinner patent', 'Three-lobed spinner on a central bearing patented by David Pavelsky in 2017, the year spinners boomed.',
           W + 'Fidget_spinner', mk='', y='2017', v=[{'n': 'Pavelsky design patent', 'mk': 'David Pavelsky', 'y': '2017', 'd': 'October, three-lobed spinner'}], dt='lobes · bearing · metal or plastic')
spin = {'n': 'Spinner', 'a': 'hand spinner · fidget spinner',
        'd': 'A hand-held toy that spins freely on a central bearing; held in one hand and flicked, with no goal.',
        'tt': [['Body', ['Three-lobe', 'Two-lobe']], ['Material', ['Metal', 'Plastic']], ['Worn form', ['Spinner ring']]],
        's': W + 'Hand_spinner', 'x': [spin_x['Hettinger spinning toy'], spin_x['Torqbar'], pav],
        'see': [['E1', 'Haptic coin', 'spins between finger pads rather than on an axle']] if False else []}
spin.pop('see')
click = {'n': 'Clicker & switch fidget', 'a': 'fidget cube · click fidget',
         'd': 'A hand-held toy of buttons, switches and dials that are clicked, pressed and flipped; bubble-popping toys are poppers.',
         'tt': [['Form', ['Fidget cube', 'Button keychain', 'Click pad']], ['Controls', ['Buttons', 'Switches', 'Dials', 'Joystick']]],
         's': fid_src, 'x': [[x for x in old_click['x'] if x['n'] == 'Fidget Cube'][0]]}
popper = {'n': 'Popper', 'a': 'pop it · bubble popper · push-pop fidget',
          'd': 'A silicone board or toy of bubbles pushed in and out with a pop; the hand repeats the push and there is nothing to solve.',
          'tt': [['Form', ['Bubble board', 'Popper keychain', 'Spinner-popper', 'Push popper']], ['Shape', ['Round', 'Square', 'Animal or character']]],
          's': W + 'Pop_it',
          'x': [x for x in old_click['x'] if x['n'] in ('Coster bubble-popping toy', 'FoxMind Pop It')]}
slider_geneneric = demote  # (no-op reference)
slide = {'n': 'Slider & haptic fidget', 'a': 'EDC fidget slider · haptic coin · haptic slider',
         'd': 'A pocket metal object that slides back and forth, or spins between finger pads, against magnet resistance; sold for everyday carry.',
         'tt': [['Form', ['Magnetic slider', 'Haptic slider', 'Haptic coin']], ['Material', ['Stainless steel', 'Titanium', 'Ultem (PEI)']]],
         's': 'https://www.thecubicle.com/en-gr/products/qiyi-haptic-coin-spinner',
         'x': [arch('QiYi Haptic Coin', 'Coin-shaped fidget that spins freely between two stationary finger pads and clicks magnetically.',
                    'https://www.thecubicle.com/en-gr/products/qiyi-haptic-coin-spinner', mk='QiYi')]}
squeeze = {'n': 'Squeeze toy', 'a': 'stress ball · dough ball',
           'd': 'A soft toy squeezed in the hand to relieve tension, such as a foam stress ball (usually under about 7 cm) or a dough-filled cube.',
           'tt': [['Filling', ['Foam', 'Bean bag', 'Silicone', 'Dough-filled']], ['Shape', ['Ball', 'Cube', 'Animal or food shape']]],
           's': W + 'Stress_ball',
           'x': [arch('NeeDoh', 'Squeeze toy filled with a dough-like material, launched by Schylling as the Groovy Glob in 2017; the firmer Nice Cube followed about three years later.',
                      W + 'NeeDoh', mk='Schylling', y='2017',
                      v=[{'n': 'NeeDoh, The Groovy Glob', 'mk': 'Schylling', 'y': '2017', 'd': 'original round stress ball in neon colours'},
                         {'n': 'Nice Cube', 'mk': 'Schylling', 'y': '', 'd': 'square variant with a firmer filling, about three years after the original; the most popular style'}],
                      dt='shape · colour · size')],
           'see': [['E1', 'Plush toy', 'Squishmallows and other plush are soft toys, not fidgets']] if False else None}
squeeze.pop('see')
sqx = [x for x in old_sq['x'] if x['n'] == 'Squishy'][0]
squishy = {'n': 'Squishy', 'a': 'slow-rise squishy · mochi squishy',
           'd': 'A slow-rising foam or silicone squeeze toy in animal or food shapes, from Japan; reached the US in 2017.',
           'tt': [['Form', ['Slow-rise foam', 'Mochi squishy', 'Gel animal keychain']]],
           's': sqx['s'], 'see': [['E1', 'Plush toy', 'plush squeezables are soft toys']]}
stretch = {'n': 'Stretch fidget', 'a': 'stretchy fidget · fidget band',
           'd': 'A toy pulled and released in the hands, such as a water snake, stretchy string or fidget band; putty and slime are modelling toys.',
           'tt': [['Form', ['Water snake', 'Stretchy string', 'Fidget band', 'Bouncy band']]],
           's': 'https://specialneedstoys.com/usa/tactile/fidget?page=3',
           'see': [['E1', 'Slime & putty toy', 'putty and slime are craft toys']]}
flippy = {'n': 'Flippy chain', 'a': 'flip chain · bike-chain fidget',
          'd': 'A chain of linked metal or plastic parts that flips over itself from hand to hand.',
          'tt': [['Material', ['Metal', 'Plastic']]], 's': fid_src}
twist = {'n': 'Twist fidget', 'a': 'twisty fidget · tangle',
         'd': 'Linked curved segments that rotate and twist into endless shapes in one hand.',
         'tt': [['Size', ['Standard', 'Junior']]],
         's': tangle['s'], 'x': [tangle]}
fold = {'n': 'Fold fidget', 'a': 'infinity cube',
        'd': 'Linked blocks that fold and open over one another without a goal; cube-shaped versions are called infinity cubes.',
        'tt': [['Form', ['Infinity cube']]], 's': W + 'Infinity_cube', 'x': [infcube]}
bao = {'n': 'Baoding balls', 'a': 'Chinese health balls',
       'd': 'Two or more metal balls rotated in the palm to relax the hand; named after Baoding in China, where they were made from the Ming dynasty.',
       'tt': [['Material', ['Iron', 'Steel']]],
       's': W + 'Baoding_balls', 'x': [x for x in old_worry['x'] if x['n'] == 'Baoding balls']}
for x in bao['x']:
    x['s'] = W + 'Baoding_balls'
wstone = {'n': 'Worry stone', 'a': 'thumb stone',
          'd': 'A smooth oval stone with a thumb-sized dip, rubbed with the thumb; a folk practice with no single origin.',
          'tt': [['Stone', ['Polished stone', 'Crystal', 'Wood']]], 's': W + 'Worry_stone',
          'x': [x for x in old_worry['x'] if x['n'] == 'Worry stone']}
for x in wstone['x']:
    x['s'] = W + 'Worry_stone'
wbeads = {'n': 'Worry beads', 'a': 'komboloi · kompoloi',
          'd': 'A string of beads handled to pass the time, associated with Greece and Cyprus; secular, unlike prayer beads.',
          'tt': [['Beads', ['Wood', 'Stone', 'Plastic']]], 's': W + 'Komboloi',
          'x': [x for x in old_worry['x'] if x['n'] == 'Komboloi']}
for x in wbeads['x']:
    x['s'] = W + 'Komboloi'
begleri = {'n': 'Begleri', 'a': 'Greek skill beads',
           'd': 'Greek hand toy of a bead at each end of a short cord or chain, flicked and twirled; descended from the komboloi.',
           'tt': [['Form', ['Cord and beads', 'Rigid bar', 'Chain']]], 's': W + 'Begleri'}
for k in (spin, click, popper, slide, squeeze, squishy, stretch, flippy, twist, fold, bao, wstone, wbeads, begleri):
    K[k['n']] = k
    k.setdefault('a', '')
fidget_kinds = [spin, click, popper, slide, squeeze, squishy, stretch, flippy, twist, fold, bao, wstone, wbeads, begleri]
for n in ('Spinner', 'Clicker & button fidget', 'Slider & haptic fidget', 'Squeeze toy', 'Flip & twist fidget', 'Worry & hand-rolling object'):
    used.add(n)
K['Spinner'] = spin
K['Slider & haptic fidget'] = slide
K['Squeeze toy'] = squeeze
# demote the generic archetypes recorded above (Three-lobed spinner, magnetic push slider, stress ball)
demoted_log += [('Spinner', 'Three-lobed bearing spinner'), ('Slider & haptic fidget', 'Magnetic push slider'), ('Squeeze toy', 'Stress ball')]

# ================================================================ PUZZLES department
cube = kd('Cube twisty puzzle'); sp = kd('Speedcube'); sm = kd('Smart cube'); nc = kd('Non-cube twisty puzzle'); bm = kd('Bandaged & shape-mod puzzle')
cube['x'] = cube['x'] + sp['x'] + sm['x']
cube['a'] = "Rubik's cube · magic cube · speedcube · smart cube"
cube['d'] = 'A cube whose layers rotate to scramble and restore coloured faces, from 2x2x2 up to very large orders, including magnetic speedcubes and Bluetooth smart cubes.'
cube['tt'] = [['Order', ['2x2x2 (Pocket Cube)', '3x3x3', '4x4x4 (Revenge)', "5x5x5 (Professor's)", '6x6x6 and 7x7x7', 'Larger orders']],
              ['Surface', ['Stickered', 'Stickerless']],
              ['Tuning', ['Standard', 'Magnetic', 'Maglev', 'Speed-tuned']],
              ['Connectivity', ['Plain', 'Bluetooth smart cube', 'App-tracked']]]
cube.pop('t', None)
used.update(['Speedcube', 'Smart cube'])
bm['n'] = 'Modified cube puzzle'; K['Modified cube puzzle'] = bm; used.add('Modified cube puzzle')
bm['a'] = 'bandaged cube · shape-mod · mod cube'
bm['d'] = 'A cube-based puzzle altered in shape, gearing or constraint, such as bandaged, geared or mixed-shape cubes.'
bm['tt'] = [['Alteration', ['Bandaged cube', 'Void cube', 'Geared', 'Mixed-shape']]]
bm.pop('t', None)
bm['x'].append(arch('Sudoku Cube', 'Cube puzzle whose faces carry numbers to arrange as sudoku grids; devised by Jay Horowitz.', W + 'Combination_puzzle', mk='', y='2006'))
nc['x'].append(arch('Alexander\'s Star', 'Great-dodecahedron twisty puzzle listed among the classic polyhedral combination puzzles.', W + 'Combination_puzzle'))
nc['tt'] = [['Solid', ['Tetrahedron', 'Dodecahedron', 'Octahedron', 'Cube with diagonal cuts']], ['Mechanism', ['Dial or clock', 'Shape-changing layers']]]
nc.pop('t', None)
nc['d'] = 'A rotating puzzle built on a pyramid, dodecahedron or other solid, or on a dial or split layer rather than a plain cube.'
snake_k = newkind('Chain twisty puzzle', 'A chain of linked prisms or cubes twisted into shapes rather than scrambled; no colour pattern is restored.',
                  W + 'Combination_puzzle', a='snake puzzle · twisting chain',
                  tt=[['Units', ['Prisms on spring bolts', 'Elastic-linked cubelets (Snake Cube)']]],
                  x=[arch("Rubik's Snake", snake['d'], W + "Rubik%27s_Snake", mk="Rubik's", y='1981', dt='24 wedges · spring bolts')])
# jigsaw
jig = kd('Jigsaw puzzle'); jig['tt'] = [['Cut', ['Die-cut cardboard', 'Hand-cut wooden', 'Laser-cut wooden', 'Fully interlocking (Japanese style)']],
                                        ['Piece count', ["Children's (4-9 large pieces)", 'Family (100-550)', 'Adult (500-1,000)', 'Large (1,500-5,000)']],
                                        ['Picture', ['Picture-less', 'Double-sided', 'Corner-only monochrome']]]
jig.pop('t', None)
jig['s'] = W + 'Jigsaw_puzzle'
jig3 = kd('3D jigsaw puzzle')
mech_src = W + 'Mechanical_puzzle'
for n in ('Put-together puzzle', 'Take-apart & trick-opening puzzle', 'Interlocking puzzle', 'Disentanglement puzzle', 'Sequential movement puzzle',
          'Folding puzzle', 'Dexterity puzzle', 'Puzzle vessel', 'Impossible object', 'Single-player logic game'):
    kd(n)
kd('Dexterity puzzle')['see'] = [['E1', 'Dexterity game', 'same skill as a table game, but here with a goal']]
kd('Dexterity game')['see'] = [['E1', 'Dexterity puzzle', 'a tilt maze with a goal is a puzzle']]
kd('Table football') if False else None

# desk toys
newkind('Pin art', 'A grid of sliding pins pressed around a hand or object to leave a 3D impression; an executive toy.', W + 'Pin_Art', a='pinscreen · pin impression toy',
        tt=[['Pins', ['Metal', 'Plastic']], ['Size', ['Desk size', 'Large']]])
newkind('Useless machine', 'A box with a switch: turning it on makes a hand or lever come out and switch it off again.', W + 'Useless_machine', a='leave-me-alone box · ultimate machine',
        tt=[['Build', ['Kit', 'Ready-made', 'Wooden', 'Acrylic']]],
        x=[arch("Minsky's ultimate machine", 'Box whose lever switches itself off, believed to be invented by Marvin Minsky as a student at Bell Labs.', W + 'Useless_machine', y='1952',
                v=[{'n': 'Monster Inside the Black Box', 'mk': 'Captain Co.', 'y': '1960s', 'd': 'plastic box with a hand that switches itself off'}])])
newkind('Magic 8 Ball', 'A plastic ball shaken to answer yes-or-no questions, with a 20-sided die of answers floating in dark blue liquid.', W + 'Magic_8_Ball', a='fortune-telling ball',
        tt=[['Size', ['Standard', 'Mini', 'Keychain']]],
        x=[arch('Magic 8 Ball', 'Fortune-telling toy shaped like an oversized eight ball, invented by Albert C. Carter and Abe Bookman; now made by Mattel.', W + 'Magic_8_Ball',
                mk='Mattel', y='1946', v=[{'n': 'Alabe Crafts original', 'mk': '', 'y': '1946', 'd': 'company founded by Carter and Bookman'}])])
nc_desk = [kd("Newton's cradle"), kd('Magnet sphere set'), kd('Coil spring toy'), kd('Drinking bird'), kd('Kinetic sand & sand art')]
kd("Newton's cradle")['d'] = "A row of hanging steel balls that pass a knock along, the classic example of an office toy."

# ================================================================ other departments: adds
paper = newkind('Paper doll', 'A cut-out paper figure with paper clothes held on by tabs.', W + 'Doll', tt=[['Form', ['Book of cut-outs', 'Boxed set', 'Magnetic']]])
rag = newkind('Rag doll', 'A soft doll sewn from cloth scraps, often with a stitched or painted face; Raggedy Ann is the best known.', W + 'Doll',
              tt=[['Make', ['Home-sewn', 'Factory-made', 'Folk']]])
for n, dfn, tts in [('Fingerboard', 'A miniature skateboard worked with the fingertips for tricks on a desk or ramp.', [['Part', ['Deck', 'Trucks and wheels', 'Obstacle set']]]),
                    ('Paddleball', 'A wooden paddle with a rubber ball on an elastic string, bounced repeatedly against the paddle.', [['Build', ['Wooden', 'Plastic']]]),
                    ('Clackers', 'Two hard balls on a cord that swing up and down and strike together with a clack.', [['Ball', ['Acrylic', 'Plastic']]])]:
    newkind(n, dfn, W + 'Skill_toy', tt=tts)
newkind('Model engine', 'A working miniature steam, Stirling, internal-combustion or jet engine built from a kit.', W + 'Scale_model',
        tt=[['Engine', ['Steam', 'Stirling', 'Internal combustion', 'Jet']], ['Supply', ['Kit', 'Finished']]], a='working engine model')
newkind('Spring rider', 'A seat or animal fixed to a heavy spring that a child rocks on.', W + 'Playground', a='spring rocker', tt=[['Shape', ['Animal', 'Vehicle']]])
newkind('Roundabout', 'A flat rotating platform children push round and ride; known as a merry-go-round in the US.', W + 'Playground', a='merry-go-round', tt=[['Drive', ['Hand-pushed', 'Pedal or lever']]])

# poker table merged into casino gaming table
ct = kd('Casino gaming table'); pt = kd('Poker table'); used.add('Poker table')
ct['tt'] = [['Game', ['Poker table', 'Blackjack table', 'Craps table']], ['Poker table build', ['Oval', 'Round', 'Octagonal', 'Fold-out', 'Convertible pool-dining top']], ['Cloth', ['Table layout cloth']]]
ct['a'] = 'poker table'
# Game clock keeps Hourglass type
K['Game clock']['see'] = [['A5', 'Hourglass', 'the same sand timer, sold as a watch-type instrument']]
K['Piñata']['see'] = [['B4', 'Piñata', 'the party-decoration version']]
K['Marble']['see'] = [['F6', 'Marble', 'the stone, not the toy']]
K['Trading card packs & boxes']['see'] = [['F3', 'Non-sports trading card', 'collecting and grading view of cards']]
K['Slime & putty toy']['see'] = [['E1', 'Stretch fidget', 'stretchy hand toys held for fidgeting']]
K['Electronic handheld toy']['see'] = [['E5', 'LCD handheld game', 'handheld with games built in']]
K['Dolls\' pram']['see'] = [['E1', 'Baby doll', 'the doll that rides in it']]

# ================================================================ BUILD departments
def D(n, t, ax, shelves, keep=('mode', 'note', 'b')):
    old = next(x for x in d['depts'] if x['n'] == n)
    o = {'n': n}
    for f in keep:
        if f in old: o[f] = old[f]
    o['t'] = t; o['ax'] = ax; o['s'] = shelves
    return o

depts = []
depts.append(D('Building & construction',
  'Toys sold as parts to join into something, from bricks and blocks to rods, marble runs, robots and craft materials; a finished model → Models, kits & railways, a puzzle with one answer → Puzzles shelf.',
  'How are the parts joined: studs and gravity, bolts and rods, channels, programming, or craft material shaped by hand?',
  [shelf('Brick & block systems', 'Pieces that clip, stack or snap together by studs, gravity or magnets: LEGO-type bricks and minifigures, wooden blocks, magnetic tiles; rods and girders → Rod, girder & track systems.',
         'kinds by how the pieces hold: studs, friction and gravity, magnets', [kd('Building brick set'), kd('Minifigure'), kd('Wooden construction set'), kd('Magnetic tile set')]),
   shelf('Rod, girder & track systems', 'Parts bolted, pushed or slotted into frames and channels: Meccano-type metal strips, Tinkertoy and K\'NEX rods, marble-run tracks; clip-on bricks → Brick & block systems.',
         'kinds by how parts join: bolted strips, pushed rods, slotted track', [kd('Metal construction set'), kd('Rod-and-connector set'), kd('Marble run')]),
   shelf('Robots & coding toys', 'Machines a child builds or programs to move: tin and battery robots, companion robots, floor robots and programmable kits; a radio-controlled car → Models, kits & railways.',
         'kinds by control: wound or remote first, then programmed', [kd('Toy robot'), kd('Coding toy')]),
   shelf('Craft & modelling toys', 'Materials a child shapes, draws with or fuses at home: modelling dough, drawing toys, light pegs, fuse beads, shrink plastic, slime; fidget putty → Fidgets.',
         'kinds by what the child works: dough, line, light, beads, heat, goo',
         [kd('Modelling dough'), kd('Drawing toy'), kd('Light-peg toy'), kd('Fuse beads'), kd('Shrink plastic'), kd('Slime & putty toy')])]))

depts.append(D('Dolls, plush & puppets',
  'Dolls, soft toys and puppets with the houses, clothes and prams that go with them; a collectible figure → Action figures & collectible figures, a porcelain figurine → F2.',
  'What is it: a doll, something a doll uses, or a soft or hand-worked figure?',
  [shelf('Modern dolls', 'Dolls made since about 1900 to dress, pose and play with: fashion dolls, 18-inch dolls, baby dolls, ball-jointed dolls; older and folk dolls → Antique & traditional dolls.',
         'kinds by build and size: slim fashion doll, 18-inch, baby, ball-jointed', [kd('Fashion doll'), kd('18-inch play doll'), kd('Baby doll'), kd('Ball-jointed doll')]),
   shelf('Antique & traditional dolls', 'Dolls of older materials or folk craft: rag, paper, bisque, wooden and ceremonial dolls; a modern reproduction sold for play → Modern dolls.',
         'kinds by material and age: cloth, paper, porcelain, folk', [rag, paper, kd('Antique bisque doll'), kd('Traditional doll')]),
   shelf('Doll accessories', "Clothes, shoes and prams made for dolls; furniture for a dolls' house → Dolls' houses & playsets.",
         'kinds by what the doll wears or rides in', [kd('Doll clothes & shoes'), kd("Dolls' pram")]),
   shelf("Dolls' houses & playsets", 'Houses, rooms, miniatures and figure sets that dolls and small figures live in; a model railway building → Models, kits & railways.',
         'kinds by what is sold: the house, its miniatures, the figure set', [kd("Dolls' house"), kd("Dolls' house miniatures"), kd('Playset')]),
   shelf('Soft toys & puppets', 'Fabric-covered toys cuddled or worked by hand: teddy bears, plush toys, puppets; a squeezable fidget → Fidgets.',
         'kinds by how it is held: cuddled (bear, plush) or worked by hand (puppet)', [kd('Teddy bear'), kd('Plush toy'), kd('Puppet')])]))

depts.append(D('Action figures & collectible figures',
  'Character figures to pose, display or collect, from jointed action figures to vinyl and designer pieces; a doll to dress → Dolls, plush & puppets, a porcelain figurine → F2.',
  'How is the figure made: jointed to pose, fixed to display, or vinyl to collect?',
  [shelf('Articulated action figures', 'Jointed figures sold in lines by scale: 3.75-inch to 7-inch play lines, transforming robots and sixth-scale collector figures; a fixed statue → Static & miniature figures.',
         'kinds by scale and purpose: play-scale lines, transforming robots, sixth-scale display', [kd('Action figure'), kd('Transforming robot toy'), kd('Sixth-scale collector figure')]),
   shelf('Static & miniature figures', 'Figures that do not pose: toy soldiers and animals, prize and scale statues, bobbleheads; a jointed figure → Articulated action figures.',
         'kinds by finish and purpose: play (soldiers, animals), display (statues), novelty (bobblehead)', [kd('Toy soldier & animal figure'), kd('Static figure'), kd('Bobblehead')]),
   shelf('Vinyl & designer collectibles', 'Vinyl and resin figures collected for design and rarity: licensed pop figures, artist designer toys, Japanese chibi figures; a jointed play figure → Articulated action figures.',
         'kinds by who designs and sells: licensed vinyl, artist designer toy, Japanese chibi', [kd('Vinyl collectible figure'), kd('Designer toy'), kd('Chibi figure')])]))

depts.append(D('Models, kits & railways',
  'Scaled copies of real vehicles, trains, engines and rockets that are built, displayed, run or flown; a toy car for small children → Toy vehicles & ride-ons, a full-size vehicle → G1.',
  'What does the model do: stand for display, run on a railway, be driven by radio or slot, or fly?',
  [shelf('Model kits & die-cast', 'Static scale models built from kits or bought finished: plastic kits, Gunpla, working engines, die-cast cars; a running locomotive → Model railways.',
         'kinds by how much the owner builds: kit to glue, snap-fit mecha kit, working engine kit, finished die-cast', [kd('Scale model kit'), kd('Gunpla & mecha model kit'), K['Model engine'], kd('Die-cast model')]),
   shelf('Model railways', 'Everything for a model railway layout: sets, locomotives, rolling stock, track, controls and scenery; a toy wooden railway → Toy vehicles & railways.',
         'kinds by role in a layout: train, track, control, scenery',
         [kd('Model railway train set'), kd('Model locomotive'), kd('Model rolling stock'), kd('Model railway track'), kd('Point motor'), kd('Model railway controller'), kd('Model railway decoder'), kd('Model railway scenery & buildings')]),
   shelf('Radio control & slot cars', 'Small cars, boats and aircraft steered by radio, slot or fixed track; a push-along toy → Toy vehicles & railways.',
         'kinds by how it is steered: by radio, by slot, by fixed track', [kd('Radio-controlled vehicle'), kd('Slot-car racing set'), kd('Mini 4WD')]),
   shelf('Model rocketry', 'Model rockets that fly on small solid motors: kits, motors and launch sets; a rocket kit that does not fly → Model kits & die-cast.',
         'kinds by what is bought: the rocket, its motor, the launcher', [kd('Model rocket kit'), kd('Model rocket motor'), kd('Model rocket launch set')])]))

depts.append(D('Board, card & table games',
  'Games played with a board, cards, tiles, dice or a table, and their parts; a puzzle → Puzzles, fidgets & desk toys, a video game → E5.',
  'How is the game sold or played: as a classic fixed set, a published title, loose cards and dice, a collectable system, a table, or gambling gear?',
  [shelf('Traditional game sets', 'Boards and pieces for old games with fixed rules: chess, shogi, xiangqi, draughts, go, backgammon, mancala, dominoes, mahjong; a modern published game → Published games.',
         'kinds by game family: chess-type, draughts-type, territory, race, counting, tile',
         [kd('Chess set'), kd('Shogi set'), kd('Xiangqi set'), kd('Draughts set'), kd('Reversi set'), kd('Go set'), kd('Backgammon set'), kd('Mancala board'), kd('Domino set'), kd('Mahjong set'), kd('Game clock')]),
   shelf('Published games', 'A boxed modern game recorded by publisher and edition, defined by its main component; titles themselves belong to the games taxonomy, a classic fixed-rule set → Traditional game sets.',
         'kinds by main component: board, cards, tiles, dice', [kd('Board game'), kd('Card game'), kd('Tile game'), kd('Dice game')]),
   shelf('Cards, dice & game parts', 'Loose decks, dice and spare pieces used across many games; a collectable trading card → Trading card & miniatures games.',
         'kinds by component: cards (western, Japanese), dice, spare pieces', [kd('Playing cards'), kd('Hanafuda deck'), kd('Dice set'), kd('Replacement game pieces')]),
   shelf('Trading card & miniatures games', 'Collectable card and miniatures game products with the sleeves, boxes and mats that protect them; collecting and grading cards → F3.',
         'kinds by what is sold: cards, miniatures, then protection and storage',
         [kd('Trading card packs & boxes'), kd('Trading card single'), kd('Miniatures game starter set'), kd('Miniatures game army box'), kd('Card sleeve'), kd('Deck box'), kd('Playmat & card binder')]),
   shelf('Table & flicking games', 'Table-sized games where players kick, blow, flick, slide, cue or stack pieces; a full pool table → E2.',
         'kinds by how the piece moves: kicked, blown, flicked, slid, cued, stacked',
         [kd('Table football'), kd('Air hockey table'), kd('Carrom board'), kd('Crokinole board'), kd('Novuss board'), kd('Table shuffleboard'), kd('Bar billiards table'), kd('Dexterity game')]),
   shelf('Casino & party games', 'Gear for gambling-style and party games at home: tables, chips, shoes, wheels and bingo; a slot machine → E5.',
         'kinds by use: tables, chips, card handling, wheels and draws',
         [ct, kd('Poker chip set'), kd('Card shoe or shuffler'), kd('Roulette wheel'), kd('Bingo set'), kd('Prize wheel')])]))

depts.append(D('Puzzles, fidgets & desk toys',
  'Things handled for a goal or for the hand alone: a puzzle has a goal to reach, a fidget has none and is held while doing something else, a desk toy is set down and watched or played with; a game with rules → Board, card & table games.',
  'Is there a goal to reach, and is the object held in the hand or set down on a desk?',
  [shelf('Jigsaw puzzles', 'Pictures cut into pieces to fit back together, flat or in three dimensions; a puzzle of moving parts → Mechanical puzzles.',
         'kinds by flat picture or solid shape', [jig, jig3]),
   shelf('Twisty puzzles', 'Puzzles solved by turning layers of a cube, other solid or chain until the pattern is restored; a sliding or take-apart puzzle → Mechanical puzzles.',
         'kinds by what turns: cube layers, altered cubes, other solids, chains', [cube, bm, nc, snake_k]),
   shelf('Mechanical puzzles', 'Puzzles solved by moving, joining or separating solid parts, without turning layers; a twisting cube → Twisty puzzles, a cut picture → Jigsaw puzzles.',
         'kinds by what the solver does: put together, take apart, interlock, untangle, slide, fold, steer, drink, perceive',
         [kd('Put-together puzzle'), kd('Take-apart & trick-opening puzzle'), kd('Interlocking puzzle'), kd('Disentanglement puzzle'), kd('Sequential movement puzzle'),
          kd('Folding puzzle'), kd('Dexterity puzzle'), kd('Puzzle vessel'), kd('Impossible object'), kd('Single-player logic game')]),
   shelf('Fidgets', 'Hand toys with no goal, worked while the owner does something else; a toy with a goal → Mechanical puzzles or Twisty puzzles, a desk ornament → Desk toys.',
         'kinds by what the hand does: spin, click or press, pop, slide, squeeze or stretch, flip, twist or fold, roll, rub or thread', fidget_kinds),
   shelf('Desk toys', 'Toys set down on a desk to watch or play with, driven by momentum, magnets, springs, heat, sand or a switch; a lava or plasma lamp → B3, a snow globe → B4.',
         'kinds by what drives the motion: momentum, magnetism, spring, heat, sand, pins, a switch, liquid',
         [kd("Newton's cradle"), kd('Magnet sphere set'), kd('Coil spring toy'), kd('Drinking bird'), kd('Kinetic sand & sand art'), K['Pin art'], K['Useless machine'], K['Magic 8 Ball']])]))

depts.append(D('Pretend & role play',
  'Toys for acting out a role at home, in a shop, as a character or in a fight; a baby toy → Baby & toddler toys, a wearable costume → A1.',
  'What does the child act out: running a home or shop, being a character, or fighting?',
  [shelf('Home & shop play', 'Play kitchens, play food, shops and tools for acting out household and trade roles; dress-up → Dress-up & make-up.',
         'kinds by the role: cooking, shopkeeping and fixing', [kd('Play kitchen'), kd('Play food & cookware set'), kd('Toy shop or tool set')]),
   shelf('Dress-up & make-up', 'Accessories for being a character: hats, dress-up pieces and play make-up; a full costume → A1.',
         'kinds by what is worn: dress-up pieces, make-up, hats', [kd('Dress-up accessory'), kd('Play make-up set'), kd('Novelty hat')]),
   shelf('Toy blasters & swords', 'Foam, gel and water blasters and toy swords for pretend fights; a real replica weapon → Weapons.',
         'kinds by how it hits: dart, water, blade', [kd('Foam dart blaster'), kd('Water blaster'), kd('Toy sword')])]))

depts.append(D('Baby & toddler toys',
  'Toys a baby or toddler shakes, mouths, stacks, splashes with or listens to; a toy for age 3 and over → the matching department.',
  "What does the child do: handle and mouth it, play on it, or listen to it?",
  [shelf('Handheld baby toys', 'Small toys shaken, stacked, sorted or splashed with: rattles, stacking toys, shape sorters, bath toys; floor and table toys → Activity & audio toys.',
         'kinds by the action: shake, stack, sort, splash', [kd('Rattle'), kd('Stacking toy'), kd('Shape sorter'), kd('Bath toy')]),
   shelf('Activity & audio toys', 'Larger toys played on or listened to: activity play mats, activity tables, audio figures; handheld toys → Handheld baby toys.',
         'kinds by use: lying and reaching, sitting at a table, listening', [kd('Activity play mat'), kd('Activity table'), kd('Audio figure')])]))

depts.append(D('Skill, music & novelty toys',
  'Toys that train a hand skill or amuse, from yo-yos and kendama to kites, juggling props, magic sets and music toys; a fidget with no skill goal → Fidgets.',
  'What does the toy ask of the player: spin or catch, throw or fly, keep things in the air, or make sound, tricks and light?',
  [shelf('Spin, string & catch toys', 'Toys worked on a string, spun or batted by hand: yo-yos, tops, kendama, fingerboards, paddleball, clackers; a juggling prop → Juggling props.',
         'kinds by action: unwind and return, spin, catch, finger-steer, bat, clack', [kd('Yo-yo'), kd('Spinning top'), kd('Kendama'), K['Fingerboard'], K['Paddleball'], K['Clackers']]),
   shelf('Throw, roll & fly toys', 'Toys rolled, thrown, flown or blown: marbles, balls, flying discs, kites, bubbles; a juggling ball → Juggling props.',
         'kinds by how it travels: rolled, bounced, thrown, flown on a line, blown', [kd('Marble'), kd('Toy ball'), kd('Toy flying disc'), kd('Toy kite'), kd('Bubble toy')]),
   shelf('Juggling props', 'Objects tossed, balanced or swung in circus-style skills: juggling balls, clubs and rings, devil sticks, diabolo, poi; a yo-yo → Spin, string & catch toys.',
         'kinds by what is thrown or spun: tossed (ball, club, ring), balanced (devil stick), spun on string (diabolo, poi)',
         [kd('Juggling ball'), kd('Juggling club'), kd('Juggling ring'), kd('Devil stick'), kd('Diabolo'), kd('Poi')]),
   shelf('Music, magic & novelty', 'Toys that make sound, do a trick, save a coin, play a small electronic game, light up or burst: toy instruments, magic sets, mechanical banks, piñatas.',
         'kinds by what the toy does: sound, trick, coin, game, light, burst',
         [kd('Toy musical instrument'), kd('Magic set'), kd('Mechanical bank'), kd('Electronic handheld toy'), kd('Toy light'), kd('Piñata')])]))

depts.append(D('Toy vehicles & ride-ons',
  'Vehicles a child pushes, pulls, rides or runs on a toy track; a collector die-cast model → Models, kits & railways, an adult kick scooter → E2.',
  'How is it moved: pushed or pulled by hand along the floor or a toy track, or ridden by the child?',
  [shelf('Toy vehicles & railways', 'Toy cars, trucks and trains pushed, pulled or run on plastic or wooden track; a collector scale model → Models, kits & railways.',
         'kinds by how it travels: free-rolling, on wooden track, on plastic track', [kd('Push-along or pull-back toy vehicle'), kd('Wooden toy railway'), kd('Plastic toy railway')]),
   shelf('Ride-ons', 'Vehicles the child sits on: balance bikes, tricycles, ride-on cars and wagons; an adult bicycle → G1.',
         'kinds by how the child drives it: feet on the ground, pedals, battery, pulled', [kd('Balance bike'), kd("Children's tricycle"), kd('Ride-on car'), kd('Ride-on wagon')])]))

depts.append(D('Outdoor play',
  'Play equipment for a garden: swings, slides, trampolines, playhouses, sandpits and water play; an indoor activity table → Baby & toddler toys.',
  'What does the child do: climb and swing, bounce, hide and dig, or splash?',
  [shelf('Climb, swing & bounce', 'Frames and rides for moving the body: swing sets, slides, climbing frames, seesaws, spring riders, roundabouts, trampolines, inflatables.',
         'kinds by movement: swing, slide and climb, rock, spin, bounce',
         [kd('Swing set'), kd('Slide or climbing frame'), kd('Seesaw'), K['Spring rider'], K['Roundabout'], kd('Garden trampoline'), kd('Inflatable activity toy')]),
   shelf('Dens & digging', 'Garden spaces for make-believe and digging: playhouses and sandpits.',
         'kinds by use: shelter, digging', [kd('Playhouse'), kd('Sandpit')]),
   shelf('Water play', 'Garden water toys: paddling pools and splash toys; a swimming pool → Water sports.',
         'kinds by size: pool, hand toy', [kd('Paddling pool'), kd('Water play toy')])]))

depts.append(D('Science & discovery kits',
  'Kits for experiments and discovery at home; a classroom instrument → E6, a toy robot → Robots & coding toys.',
  'What does the child investigate or make: general experiments, chemistry, crystals or molecules?',
  [shelf('Science & discovery kits', 'Boxed kits for home experiments: general science, chemistry sets, crystal growing and molecular models; a telescope or microscope → E6.',
         'kinds by subject: general, chemistry, crystals, molecules', [kd('Science experiment kit'), kd('Chemistry set'), kd('Crystal-growing kit'), kd('Molecular model kit')])]))

# every kind placed? (removed kinds must be merged ones)
placed = {k['n'] for dp in depts for s in dp['s'] for k in s['k']}
merged = {'Speedcube', 'Smart cube', 'Clicker & button fidget', 'Flip & twist fidget', 'Worry & hand-rolling object', 'Poker table', 'Bandaged & shape-mod puzzle'}
lost = [n for n in K if n in used and n not in placed and n not in merged and n not in ('Spinner', 'Squeeze toy', 'Slider & haptic fidget')]
orig_names = {k['n'] for x in json.load(open(BAK))['depts'] for s in x['s'] for k in s['k']}
unplaced = [n for n in orig_names if n not in placed and n not in merged]
assert not unplaced, unplaced

# ---------------------------------------------------------------- auto tt for kinds that still hold a flat t
MAT = re.compile(r'\b(wood|wooden|plastic|metal|vinyl|resin|glass|silicone|foam|bone|ivory|steel|cloth|paper|brass|rubber|bakelite|melamine|melamine|leather|jade|hardwood|boxwood|mohair|cast iron|tin|bamboo|cardboard)\b', re.I)
SCL = re.compile(r'(\d|inch|\bmm\b|\bcm\b|scale|gauge|\bsize\b|order|large|mini|micro)', re.I)
EDI = re.compile(r'(edition|complete|sealed|incomplete|expansion|promo|pledge|exclusive|variant|chase|first|boxed|carded|raw|graded|printing|unlimited|common|rare|foil)', re.I)
def auto_tt(t):
    g = {'Scale or size': [], 'Material': [], 'Edition and condition': [], 'Form and use': []}
    for x in t:
        if EDI.search(x): g['Edition and condition'].append(x)
        elif SCL.search(x): g['Scale or size'].append(x)
        elif MAT.search(x): g['Material'].append(x)
        else: g['Form and use'].append(x)
    return [[a, b] for a, b in g.items() if b]
for dp in depts:
    for s in dp['s']:
        for k in s['k']:
            dem = k.pop('_demoted', [])
            if k.get('t') and not k.get('tt'):
                k['tt'] = auto_tt(k.pop('t'))
            elif 't' in k and not k['t']:
                k.pop('t')
            if k.get('t') and k.get('tt'):
                k.pop('t')
            if dem:
                have = {x.lower() for g in k.get('tt', []) for x in g[1]}
                add = [x for x in dem if x.lower() not in have]
                if add:
                    k.setdefault('tt', []).append(['Named forms', add])
            if 'a' not in k: k['a'] = ''

# special manual axis labels where auto grouping is weak
def retag(n, tt):
    k = next(k for dp in depts for s in dp['s'] for k in s['k'] if k['n'] == n)
    k['tt'] = tt
retag('Model railway train set', [['Scale or gauge', ['Z (1:220, 6.5 mm)', 'N (1:160; British N 1:148, 9 mm)', 'TT / TT:120 (1:120, 12 mm)', 'HO / H0 (1:87, 16.5 mm)', 'OO (1:76.2, 16.5 mm)', 'EM and P4 finescale (4 mm scale)', 'S (1:64)', 'O (1:43.5–1:48, 32 mm)', 'Gauge 1 (1:32, 45 mm)', 'G / garden (about 1:22.5, 45 mm)']],
                                  ['Control', ['Analogue DC', 'Digital (DCC)']]]) if False else None

# ---------------------------------------------------------------- category
d['ax'] = 'What is the toy for: building, pretending, dressing a doll, posing a figure, modelling, playing a game, handling a puzzle, practising a skill, a baby, riding or outdoors?'
d['key'] = [
  '1. Is it for a baby or toddler to shake, stack, mouth or splash with? → Baby & toddler toys',
  '2. Is it a game with rules played with a board, cards, tiles, dice or a table, including trading cards and miniatures games? → Board, card & table games',
  '3. Is it handled for a goal to solve, or for the hand alone, or set on a desk to watch (puzzle, cube, fidget, desk toy)? → Puzzles, fidgets & desk toys',
  '4. Is it a scaled copy of a real vehicle, engine or train that is built, run or flown (kits, die-cast, railways, radio control, rockets)? → Models, kits & railways',
  '5. Is it a doll, bear, plush toy or puppet, or a house, clothes or pram for one? → Dolls, plush & puppets',
  '6. Is it a character figure to pose, display or collect? → Action figures & collectible figures',
  '7. Is it sold as parts to join, a robot to program or craft material to shape (bricks, blocks, marble runs, dough, beads)? → Building & construction',
  '8. Is it a vehicle the child pushes, pulls, rides or runs on a toy track? → Toy vehicles & ride-ons',
  '9. Is it a kit for experiments and discovery? → Science & discovery kits',
  '10. Does the child act out a role with it (kitchen, shop, dress-up, foam blaster)? → Pretend & role play',
  '11. Is it playground equipment for a garden? → Outdoor play',
  '12. Is it a yo-yo, top, kite, juggling prop, magic set or other skill, music or novelty toy? → Skill, music & novelty toys',
  '<i>Precedence: a die-cast car is a model (step 4) before a push-along toy (step 8); a toy that is only squeezed, spun or clicked is a fidget (step 3) before a novelty toy (step 12); a jointed figure sold as a doll to dress is a doll (step 5).</i>'
]
d['depts'] = depts

# ---------------------------------------------------------------- see targets must exist
def kind_names(code):
    if code == 'E1': return placed
    try:
        j = json.load(open(ROOT + 'reader/%s.json' % code))
    except Exception:
        return None
    return {k['n'] for dp in j.get('depts', []) for s in dp.get('s', []) for k in s.get('k', [])}
cache = {}
dropped_see = []
for dp in depts:
    for s in dp['s']:
        for k in s['k']:
            if k.get('see'):
                keep = []
                for sv in k['see']:
                    if sv[0] not in cache: cache[sv[0]] = kind_names(sv[0])
                    names = cache[sv[0]]
                    if names is not None and sv[1] in names: keep.append(sv)
                    else: dropped_see.append((k['n'], sv))
                if keep: k['see'] = keep
                else: k.pop('see')

# ---------------------------------------------------------------- write
tmp = P + '.tmp'
json.dump(d, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, P)
after = dict(dep=len(depts), shelves=sum(len(x['s']) for x in depts), kinds=len(placed),
             arch=sum(len(k.get('x', [])) for x in depts for s in x['s'] for k in s['k']))
print('before', before); print('after', after)
print('dropped see', dropped_see)
print('demoted', len(demoted_log))
json.dump({'demoted': demoted_log, 'dropped_see': dropped_see, 'before': before, 'after': after}, open(ROOT + 'work/STR_E1/log.json', 'w'), indent=1)
