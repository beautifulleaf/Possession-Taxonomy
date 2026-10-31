import json, copy, os, shutil, sys, re

ROOT = '/home/user/Possession-Taxonomy/rebuild'
SRC = ROOT + '/work/STR_C2/bak/C2.json'     # frozen pre-pass copy
OUT = ROOT + '/out/C2.json'

d = json.load(open(SRC))
OLD = {}
OLDDEPT = {dp['n']: dp for dp in d['depts']}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            OLD[k['n']] = k

WIKI = 'https://en.wikipedia.org/wiki/'
S_MOW = WIKI + 'Lawn_mower'
S_GT = WIKI + 'Garden_tool'
S_BON = WIKI + 'Bonsai'
S_BE = 'https://www.bonsaiempire.com/basics/general/tools'
S_GH = WIKI + 'Garden_hose'
S_MOL = WIKI + 'Molluscicide'
S_MULCH = WIKI + 'Mulch'
S_GW = 'https://gardenersworld.com/product-guides/growing/greenhouse-accessories'
S_INYO = 'https://www.inyopools.com/Category/category_accessories.aspx'
S_BBQ = WIKI + 'Barbecue_grill'
S_TAN = WIKI + 'Tandoor'
S_FP = WIKI + 'Fire_pit'
S_TREL = WIKI + 'Trellis_(architecture)'
S_GT2 = 'https://gardentrellis.co.uk/page/news/view/four-of-the-best-plant-support-solutions'
S_WB = WIKI + 'Window_box'

renames = {'Plant support':'Plant stake & cane','Plant tie & label':'Plant tie','Potting compost, soil & mulch':'Potting compost','Bonsai wire & wire cutter':'Bonsai wire','Root hook & rake':'Root hook'}


def K(n, tt=None, old=None, d_=None, a=None, see=None, s=None, new=False,
      drop_x=(), add_x=(), m_only=None, merge=(), keep_t=False):
    if new:
        k = {'n': n, 'a': a or '', 'd': d_, 's': s}
    else:
        k = copy.deepcopy(OLD[old or n])
        k['n'] = n
        if d_:
            k['d'] = d_
        if a is not None:
            k['a'] = a
        if s:
            k['s'] = s
        if m_only is not None:
            k['m'] = [m for m in k.get('m', []) if m[0] in m_only]
        if drop_x == 'all':
            k['x'] = []
        elif drop_x:
            k['x'] = [x for x in k.get('x', []) if x['n'] not in drop_x]
        for mn in merge:
            o = OLD[mn]
            k.setdefault('m', []).extend(o.get('m', []) or [])
            k.setdefault('r', []).extend(o.get('r', []) or [])
            k.setdefault('x', []).extend(o.get('x', []) or [])
    if k.get('m'):
        seen=[]
        for m in k['m']:
            if m not in seen: seen.append(m)
        k['m']=seen
    k.pop('t', None)
    if add_x:
        k.setdefault('x', []).extend(add_x)
    if tt:
        k['tt'] = tt
    if see:
        k['see'] = see
    # tidy empties
    for f in ('x', 'm', 'r'):
        if f in k and not k[f]:
            del k[f]
    return k


def X(n, d_, s, mk='', y='', a='', v=None, dt=None):
    x = {'n': n, 'a': a, 'd': d_, 'mk': mk, 'y': y, 's': s, 'v': v or []}
    if dt:
        x['dt'] = dt
    return x


def SH(n, t, ax, kinds):
    sh = {'n': n, 't': t, 'k': kinds}
    if ax:
        sh['ax'] = ax
    return sh


def DP(n, t, ax, shelves):
    o = OLDDEPT[n]
    dep = {'n': n, 'mode': o['mode'], 't': t, 'ax': ax}
    if o.get('note'):
        dep['note'] = o['note']
    if o.get('b'):
        dep['b'] = o['b']
    dep['s'] = shelves
    return dep


depts = []

# ------------------------------------------------------------------ 1 LAWN CARE
mowers = SH(
    'Lawn mowers',
    'Machines that cut a whole lawn, from push reel mowers to ride-ons and robots; tools for edges and corners go on the Edging & trimming shelf.',
    'kinds by how the mower cuts and how it is steered: spinning blade, reel, air cushion, seated rider (ride-on, lawn tractor, zero-turn), robot, then parts',
    [
        K('Rotary mower', [
            ['Power source', ['Petrol', 'Cordless (battery)', 'Corded electric']],
            ['Drive', ['Push', 'Self-propelled']],
            ['Clippings', ['Collected in a box', 'Mulched back into the lawn']],
            ['Finish', ['Plain cut', 'Striped by a rear roller']]],
          see=[['C7', 'Flail mower', 'tractor-mounted mower for rough grass']]),
        K('Cylinder mower', [
            ['Power source', ['Hand-push', 'Petrol', 'Corded electric', 'Cordless (battery)']],
            ['Cutting unit', ['Fixed reel', 'Interchangeable cassette']]]),
        K('Hover mower', [['Power source', ['Corded electric', 'Cordless', 'Petrol']]]),
        K('Riding mower', [
            ['Layout', ['Rear-engine ride-on', 'Front-cut ride-on']],
            ['Power source', ['Petrol', 'Battery']]],
          d_='Compact seated mower with the engine behind the driver, for medium to large lawns; lawn tractors and zero-turn mowers have their own kinds.',
          m_only=['Merlin'],
          see=[['C2', 'Lawn tractor', 'larger seated mower that tows attachments'],
               ['C2', 'Zero-turn mower', 'seated mower steered by two levers']]),
        K('Lawn tractor', [
            ['Power source', ['Petrol', 'Battery']],
            ['Collection', ['Rear bag', 'Side discharge', 'Mulching deck']],
            ['Transmission', ['Manual gears', 'Hydrostatic']]],
          new=True, a='garden tractor · lawn rider',
          d_='Seated mower built like a small tractor, with a front-mounted deck, that can also tow trailers and rollers.',
          s=S_MOW),
        K('Zero-turn mower', [
            ['Power source', ['Petrol', 'Battery']],
            ['Steering', ['Twin lever', 'Stand-on']]],
          new=True, a='zero turn mower · ZTR',
          d_='Seated mower steered by two levers that drive each rear wheel separately, so it can turn on the spot.',
          s=S_MOW),
        K('Robotic mower', [
            ['Boundary', ['Boundary wire', 'Wire-free satellite (RTK)', 'Wire-free camera vision', 'Wire-free LiDAR']],
            ['Drive', ['Two-wheel drive', 'All-wheel drive']]]),
        K('Mower & trimmer spare parts', [
            ['Part', ['Mower blade', 'Trimmer line', 'Trimmer spool', 'Drive belt']]]),
    ])
# models that belonged to the old broad riding-mower kind
LT_MODELS = ['S130', 'S120', 'X350R', 'XT1 LT50', 'R 214TC', 'T6', 'TB30B']
ZT_MODELS = ['Z325E ZTrak', 'Titan MAX', 'Z6 ZT4214L', 'RZ 560']
for kk in mowers['k']:
    if kk['n'] == 'Lawn tractor':
        kk['m'] = [m for m in OLD['Riding mower']['m'] if m[0] in LT_MODELS]
    if kk['n'] == 'Zero-turn mower':
        kk['m'] = [m for m in OLD['Riding mower']['m'] if m[0] in ZT_MODELS]

edging = SH(
    'Edging & trimming',
    'Tools that cut grass the mower cannot reach, along walls, borders and paths, and that cut the edge line; mowing open lawn goes on the Lawn mowers shelf.',
    'kinds by how the edge is cut: spinning line, powered blade, blade pushed in by foot, hand shears',
    [
        K('String trimmer', [
            ['Power source', ['Cordless', 'Corded electric', 'Petrol']],
            ['Cutting head', ['Bump-feed line', 'Fixed line', 'Metal blade']],
            ['Format', ['Trimmer only', 'Trimmer and brushcutter combi']]],
          see=[['C2', 'Brush cutter', 'heavier machine that takes metal blades']]),
        K('Powered lawn edger', [
            ['Power source', ['Cordless', 'Corded electric', 'Petrol']],
            ['Format', ['Walk-behind with wheel', 'Stick edger']]],
          new=True, a='lawn edger · power edger',
          d_='Powered tool with a vertical blade that cuts a clean line between a lawn and a path or bed.',
          s=S_GT),
        K('Half-moon edger', [['Material', ['Stainless steel', 'Carbon steel']]]),
        K('Grass shears', [
            ['Grip', ['One-handed', 'Long-handled']],
            ['Power source', ['Hand-operated', 'Battery']]]),
    ])

treat = SH(
    'Lawn treatment & surfaces',
    'Tools and surfaces for clearing, aerating, feeding, firming and replacing a lawn; grass seed and turf as plants are sold with plants.',
    'kinds in the order of lawn care: sweep thatch and debris, rake out moss, open the soil, feed and sow, firm, replace with a synthetic surface',
    [
        K('Lawn sweeper', [
            ['Format', ['Push', 'Towed behind a tractor']]],
          new=True, a='leaf sweeper · lawn brush',
          d_='Machine with a rotating brush that sweeps leaves, twigs and clippings into a hopper as it is pushed or towed.',
          s=WIKI + 'Lawn_sweeper',
          see=[['C2', 'Leaf blower', 'moves debris by air instead']]),
        K('Scarifier', [
            ['Power source', ['Manual spring-tine rake', 'Electric', 'Petrol']],
            ['Tines', ['Spring tine', 'Fixed blade']]]),
        K('Lawn aerator', [
            ['Tine', ['Spike', 'Hollow-tine (plug)']],
            ['Format', ['Hand fork', 'Push roller', 'Tow-behind']]]),
        K('Broadcast spreader', [
            ['Spreading action', ['Hand-held', 'Wheeled broadcast', 'Wheeled drop']],
            ['Load', ['Grass seed', 'Granular feed', 'Grit and salt']]],
          see=[['C3', 'Lawn seed', 'what the spreader sows'],
               ['C7', 'Fertiliser spreader', 'tractor-scale version']]),
        K('Lawn roller', [
            ['Material', ['Water- or sand-filled plastic drum', 'Steel drum']],
            ['Format', ['Push', 'Tow-behind']]]),
        K('Artificial turf', [
            ['Pile height', ['Short', 'Medium', 'Long']],
            ['Use', ['Pet-friendly', 'Play area and fire-retardant', 'Putting green']]],
          see=[['C3', 'Turf', 'real turf grown as a lawn']]),
    ])
depts.append(DP(
    'Lawn care',
    'Machines and tools that cut, edge and treat a lawn; hedges and branches go under Cutting & pruning.',
    'Is the job cutting the whole lawn, finishing its edges, or treating the turf?',
    [mowers, edging, treat]))

# ------------------------------------------------------------------ 2 CUTTING & PRUNING
stem = SH(
    'Stem cutters',
    'One-handed cutters for flower stems, shoots and twigs up to finger thickness, such as secateurs, snips and pruning knives; thicker wood goes to Branch cutters.',
    'kinds by blade form: bypass scissors, fine snips, knife',
    [
        K('Secateurs', [
            ['Blade action', ['Bypass', 'Anvil', 'Ratchet', 'Parrot-beak']],
            ['Power source', ['Hand-operated', 'Battery-powered']],
            ['Handedness', ['Right-handed', 'Left-handed']]],
          drop_x=['Ratchet pruner'],
          see=[['C2', 'Garden snips', 'lighter, for soft stems']]),
        K('Garden snips', [
            ['Use', ['Flower and herb harvest', 'Fruit and grape picking', 'Topiary and fine trimming']]],
          see=[['C2', 'Secateurs', 'stronger, for woody stems']]),
        K('Pruning knife', [
            ['Blade', ['Pruning (hawkbill)', 'Grafting', 'Budding']],
            ['Construction', ['Fixed', 'Folding']],
            ['Handedness', ['Right-handed', 'Left-handed']]]),
    ])
branch = SH(
    'Branch cutters',
    'Hand tools for branches too thick for secateurs, cut by long handles, saw teeth or a reach pole; engine and battery saws go to Powered cutting tools.',
    'kinds by how the force is applied: lever handles, pull or push saw, saw or lopper on a pole',
    [
        K('Loppers', [
            ['Blade action', ['Bypass', 'Anvil', 'Ratchet', 'Geared']],
            ['Handles', ['Fixed', 'Telescopic']]]),
        K('Pruning saw', [
            ['Mounting', ['Folding', 'Fixed', 'Pole-mounted head']],
            ['Blade', ['Straight', 'Curved']],
            ['Cutting stroke', ['Pull stroke (Japanese style)', 'Push stroke']]],
          see=[['C1', 'Folding saw', 'woodworking and camp folding saw'],
               ['C2', 'Pole pruner', 'saw on a pole']]),
        K('Pole pruner', [
            ['Head', ['Lopper head', 'Saw head', 'Combined lopper and saw']],
            ['Pole', ['Fixed', 'Telescopic']]],
          a='high-branch shears · tree pruner · averruncator',
          see=[['C2', 'Pole saw', 'powered version']]),
    ])
blades = SH(
    'Hedge, grass & brush blades',
    'Hand blades clipped, swung or chopped through hedges, grass and brush: hedge shears, scythes, sickles, billhooks and machetes.',
    'kinds by how the blade moves: clipping shears, sweeping scythe, hooked sickle, chopping billhook and machete',
    [
        K('Hedge shears', [
            ['Blade', ['Straight', 'Wavy-edge', 'Short topiary blade']],
            ['Handles', ['Fixed', 'Telescopic']]],
          drop_x=['Japanese hand-forged hedge shears', 'Topiary shears'],
          see=[['C2', 'Hedge trimmer', 'powered version']]),
        K('Scythe', [
            ['Blade', ['Grass', 'Ditch', 'Bush', 'Garden', 'Field or hay']],
            ['Snath shape', ['Straight', 'Bent', 'Adjustable']],
            ['Grips', ['One-grip', 'Two-grip']],
            ['Handedness', ['Right-handed', 'Left-handed']],
            ['Sold as', ['Complete scythe', 'Blade only', 'Snath only']]]),
        K('Sickle', [
            ['Edge', ['Smooth', 'Serrated']],
            ['Handle', ['Straight', 'Cranked (offset)']]],
          drop_x=['Serrated sickle', 'Grass hook', 'Bagging hook']),
        K('Billhook', [
            ['Edge', ['Single-edged', 'Double-edged']],
            ['Handle', ['One-handed', 'Two-handed (long handle)']]],
          see=[['C1', 'Axe', 'chopping tool for wood']]),
        K('Machete', [
            ['Blade shape', ['Straight', 'Curved']],
            ['Blade back', ['Plain', 'Saw back']],
            ['Blade length', ['Short', 'Standard', 'Long']]]),
    ])
powered = SH(
    'Powered cutting tools',
    'Engine or battery tools that cut hedges, branches and brush; hand-driven blades go on the other shelves.',
    'kinds by cutting head: reciprocating blade bar, chain, chain on a pole, line or metal blade, swappable attachments',
    [
        K('Hedge trimmer', [
            ['Power source', ['Petrol', 'Cordless', 'Corded electric']],
            ['Reach', ['Standard', 'Long-reach (on a pole)', 'Mini shrub shear']]],
          see=[['C2', 'Hedge shears', 'hand tool']]),
        K('Chainsaw', [
            ['Power source', ['Petrol', 'Cordless', 'Corded electric']],
            ['Handle', ['Rear handle', 'Top handle (arborist)']]],
          see=[['C1', 'Chainsaw trousers', 'protective clothing']]),
        K('Pole saw', [
            ['Power source', ['Petrol', 'Cordless', 'Corded electric']],
            ['Pole', ['Fixed', 'Telescopic']]],
          see=[['C2', 'Pole pruner', 'hand-operated version']]),
        K('Brush cutter', [
            ['Power source', ['Petrol', 'Cordless']],
            ['Handle', ['Loop', 'Bike (cow-horn)']],
            ['Cutting head', ['Metal blade', 'Line head']]],
          see=[['C2', 'String trimmer', 'lighter line cutter']]),
        K('Garden multi-tool', [
            ['Powerhead', ['Petrol', 'Cordless']]]),
    ])
depts.append(DP(
    'Cutting & pruning',
    'Blades that cut stems, branches, hedges, grass and brush, by hand or by motor; lawn mowing goes under Lawn care and bonsai tools under Bonsai.',
    'How thick and tough is the growth being cut, and does the user or a motor drive the blade?',
    [stem, branch, blades, powered]))

# ------------------------------------------------------------------ 3 DIGGING & PLANTING
dig = SH(
    'Digging tools',
    'Tools driven into the ground to dig, lift and move soil: spades, forks, shovels, broadforks, mattocks, pickaxes and post-hole diggers.',
    'kinds by what the tool does to the soil: cut and lift, loosen, scoop and throw, rock back, swing to break, bore a hole',
    [
        K('Garden spade', [
            ['Blade', ['Digging', 'Border', 'Transplanting (narrow)']],
            ['Steel', ['Carbon steel', 'Stainless steel']],
            ['Handle grip', ['T-grip', 'D-grip', 'YD-grip']],
            ['Step', ['Treaded', 'Untreaded']],
            ['Handle length', ['Standard', 'Long-handled']]],
          drop_x=['Digging spade', 'Border spade', 'Transplanting spade']),
        K('Garden fork', [
            ['Tines', ['Digging', 'Border', 'Manure', 'Potato']],
            ['Steel', ['Carbon steel', 'Stainless steel']]],
          drop_x=['Digging fork', 'Border fork', 'Potato fork']),
        K('Shovel', [
            ['Blade', ['Round-point', 'Square-mouth', 'Spoon', 'Grain']],
            ['Handle grip', ['D-grip', 'Long straight']],
            ['Socket', ['Open socket', 'Closed socket']]],
          drop_x=['Round-point shovel', 'Square-mouth shovel', 'Grain shovel', 'Spoon shovel']),
        K('Broadfork', [
            ['Frame', ['Steel', 'Wooden handles']],
            ['Width', ['Standard', 'Raised-bed width']]]),
        K('Mattock', [
            ['Head', ['Pick', 'Cutter', 'Hoeing (adze)', 'Pronged']]],
          drop_x=['Pick mattock', 'Cutter mattock'],
          see=[['C2', 'Pickaxe', 'pick on both sides']]),
        K('Pickaxe', [
            ['Head', ['Pick', 'Railroad pick', 'Miner\'s pick']],
            ['Handle', ['Wooden', 'Fibreglass']]],
          new=True, a='pick · pick-axe',
          d_='Heavy tool with a pointed metal head set across a long handle, swung to break hard or stony ground.',
          s=WIKI + 'Pickaxe',
          see=[['C2', 'Mattock', 'pick on one side, adze on the other']]),
        K('Post-hole digger', [
            ['Action', ['Clamshell (twin hinged blades)', 'Earth auger']],
            ['Power source', ['Hand-operated', 'Powered']]],
          new=True, a='clamshell digger · post hole pincer · earth auger',
          d_='Tool with two hinged blades, or a turning auger, that bores narrow deep holes for fence posts and planting.',
          s=WIKI + 'Post_hole_digger'),
    ])
surface = SH(
    'Hoes, rakes & cultivators',
    'Tools that work the soil surface: hoes cut weeds, rakes level and clear, cultivators and tillers break the crust and mix the soil; digging a bed goes to Digging tools.',
    'kinds by action on the surface: push or draw a blade, level with teeth, claw, motor-driven tines',
    [
        K('Hoe', [
            ['Blade action', ['Dutch (push)', 'Draw', 'Swan-neck', 'Oscillating (stirrup)', 'Collinear', 'Fork hoe']],
            ['Format', ['Long-handled', 'Wheel hoe']]],
          drop_x=['Dutch hoe', 'Draw hoe', 'Swan-neck hoe', 'Oscillating hoe', 'Wheel hoe']),
        K('Garden rake', [
            ['Head', ['Bow', 'Flat-head (level-head)', 'Landscaping', 'Stone']]],
          drop_x=['Bow rake', 'Landscaping rake', 'Stone rake']),
        K('Hand cultivator', [
            ['Head', ['Three-tine claw', 'Single-tine weeder']],
            ['Handle', ['Short', 'Long']]]),
        K('Garden tiller', [
            ['Size', ['Mini tiller', 'Standard']],
            ['Tine position', ['Front-tine', 'Mid-tine']],
            ['Power source', ['Petrol', 'Corded electric', 'Cordless']]],
          see=[['C7', 'Seedbed combination', 'tractor-scale soil preparation']]),
    ])
planting = SH(
    'Planting tools',
    'Small hand tools that make holes for seeds, bulbs and young plants and lift weeds beside them; digging a whole bed goes to Digging tools.',
    'kinds by how the hole is made: scoop, slice, plug, point, then lifting weeds',
    [
        K('Hand trowel', [
            ['Material', ['Stainless steel', 'Forged carbon steel', 'Forged boron steel']],
            ['Blade', ['Wide scoop', 'Narrow transplanting']]],
          drop_x=['Narrow transplanting trowel']),
        K('Hori-hori', [
            ['Steel', ['Stainless steel', 'Carbon steel']],
            ['Features', ['With sheath', 'Depth markings']]]),
        K('Bulb planter', [['Format', ['Hand-held', 'Long-handled']]]),
        K('Dibber', [
            ['Material', ['Wood', 'Steel-tipped', 'Plastic']],
            ['Shape', ['Straight', 'T-handled', 'Trowel dibber']],
            ['Features', ['Depth markings']]],
          drop_x='all'),
        K('Hand weeder', [
            ['Format', ['Short-handled', 'Long-handled stand-up']],
            ['Head', ['Forked (grubber)', 'Corkscrew', 'Knife blade', 'Sickle blade']]],
          drop_x=['Japanese weeding sickle', 'Patio weeding knife', 'Stand-up weed puller']),
    ])
depts.append(DP(
    'Digging & planting',
    'Hand and powered tools that dig, break, level and plant soil; tools that cut plants go under Cutting & pruning.',
    'What is done to the soil: dig it out, work and level its surface, or set plants and bulbs in it?',
    [dig, surface, planting]))

# ------------------------------------------------------------------ 4 BONSAI
tok = copy.deepcopy(OLD['Bonsai pot'])
bonsai_pot = K('Bonsai pot', [
    ['Glaze', ['Unglazed (for evergreens)', 'Glazed (for deciduous trees)']],
    ['Shape', ['Rectangle', 'Oval', 'Round', 'Square', 'Cascade']],
    ['Size', ['Standard', 'Shohin']],
    ['Role', ['Tree pot', 'Accent pot']]],
    drop_x=['Gyozan bonsai pot', 'Reiho bonsai pot', 'Yamaaki bonsai pot', 'Koyo bonsai pot',
            'Shuho bonsai pot', 'Ikko bonsai pot', 'Antique-style Tokoname bonsai pot'],
    see=[['C3', 'Juniper bonsai', 'a tree grown in the pot']])
for xx in bonsai_pot['x']:
    if xx['n'] == 'Tokoname bonsai pot':
        xx['v'].append({'n': 'Antique-style Tokoname pot', 'mk': '', 'y': '',
                        'd': "collector's item still being made"})
bpots = SH(
    'Pots, trays & stands',
    'Containers and supports that hold a bonsai: show pots, training boxes, slabs and display stands.',
    'kinds by role: show pot, grow-on box, rock-like slab, display stand',
    [bonsai_pot,
     K('Bonsai growing box', [['Material', ['Wood', 'Plastic']]],
       new=True, a='training box · development container',
       d_='Plain deep container in which a tree is grown on and trained before it moves to a show pot.', s=S_BON),
     K('Bonsai slab', [['Material', ['Concrete', 'Glass-reinforced plastic', 'Natural stone']]],
       new=True, a='rock slab',
       d_='Flat rock-like slab on which a tree and its moss are planted instead of in a pot.', s=S_BON),
     K('Bonsai display stand', [['Setting', ['Formal indoor stand', 'Wooden indoor stand', 'Outdoor bench']]],
       new=True, a='bonsai table · bonsai bench',
       d_='Stand, table or bench on which a bonsai is shown, indoors in a display alcove or outdoors.', s=S_BON),
     ])
bcut = SH(
    'Cutting tools',
    'Tools that cut twigs, branches and roots on a bonsai, from fine shears to hollow-cutting cutters; heavy garden saws go under Branch cutters.',
    'kinds by size and kind of cut: fine twig, flush hollow, deep hollow, thick limb, wire',
    [
        K('Bonsai shears', [
            ['Blade form', ['Butterfly', 'Standard', 'Long slim twig', 'Shohin and azalea']],
            ['Use', ['Twig cutting', 'Leaf trimming', 'Root cutting']]],
          drop_x='all'),
        K('Concave cutter', [
            ['Blade', ['Straight', 'Semi-round']],
            ['Steel', ['Carbon steel', 'Stainless steel']],
            ['Length', ['About 170 mm', 'Up to about 285 mm']]],
          drop_x='all'),
        K('Knob cutter', [
            ['Steel', ['Carbon steel', 'Stainless steel']],
            ['Size', ['Small', 'Standard', 'Large']]],
          drop_x='all'),
        K('Bonsai saw', [['Size', ['Large foldable', 'Medium foldable', 'Thin']]],
          new=True, a='Japanese pruning saw',
          d_='Japanese pull saw for branches and trunks too thick for shears or cutters, folding or fixed.', s=S_BE,
          see=[['C1', 'Ryoba saw', 'woodworking pull saw']]),
        K('Bonsai wire cutter', [['Size', ['Large', 'Small']]],
          old='Bonsai wire & wire cutter', drop_x='all',
          d_='Round-headed cutter that snips training wire close to the branch without marking the bark.'),
    ])
bshape = SH(
    'Wire & shaping tools',
    'Wire, levers and pliers that bend, position and carve a tree; cutting tools and root tools have their own shelves.',
    'kinds by stage of shaping: wire the branch, bend the limb, carve deadwood',
    [
        K('Bonsai wire', [
            ['Metal', ['Anodised aluminium', 'Annealed copper']],
            ['Gauge', ['Fine', 'Medium', 'Heavy']]],
          old='Bonsai wire & wire cutter', drop_x='all',
          d_='Soft wire wrapped round a branch to hold it in a new position while it sets.'),
        K('Bonsai branch bender', [['Type', ['Rubber-padded lever', 'Screw clamp']]],
          new=True, a='bending lever · branch clamp',
          d_='Padded steel lever or screw clamp that bends a heavy branch or trunk to a new line without breaking it.',
          s=S_BE),
        K('Jin pliers', [['Jaws', ['Straight', 'Angled']]],
          a='wire-bending pliers · deadwood pliers · jin plier'),
    ])
broot = SH(
    'Root & repotting tools',
    'Tools for lifting a tree from its pot, opening the root ball, combing the roots and turning the tree; cutting roots goes under Cutting tools.',
    'kinds by task: open the root ball, comb it out, place moss and soil, turn the tree',
    [
        K('Root hook', [
            ['Size', ['Small', 'Large']],
            ['Handle end', ['Plain', 'With tweezer', 'With spatula']]],
          old='Root hook & rake', drop_x='all',
          d_='Single-pronged hook that opens a root ball and separates tangled roots.'),
        K('Root rake', [
            ['Teeth', ['One', 'Two', 'Three']],
            ['Size', ['Small', 'Large']]],
          old='Root hook & rake', drop_x='all',
          d_='Small rake with one to three teeth that combs old soil out of the roots at repotting.'),
        K('Bonsai tweezers', [
            ['Tip', ['Straight', 'Bent']],
            ['Head', ['Plain tweezers', 'Tweezer-spatula']]],
          new=True, a='tweezer spatula',
          d_='Long tweezers, often with a spatula end, that place moss, lift weeds and press soil between roots.',
          s=S_BE),
        K('Bonsai turntable', [
            ['Frame', ['Flat disc', 'Tilting', 'Three-legged, height-adjustable']],
            ['Features', ['Ball-bearing', 'Lockable']]],
          drop_x='all'),
    ])
depts.append(DP(
    'Bonsai',
    'Pots, display pieces and tools made for keeping bonsai; the trees themselves are listed with plants.',
    'Is it a vessel or display piece, a cutting tool, a shaping tool, or a root tool?',
    [bpots, bcut, bshape, broot]))

# ------------------------------------------------------------------ 5 WATERING & PONDS
store = SH(
    'Storing & pumping water',
    'Containers that collect rainwater and pumps that move it round a garden; hoses and cans carry it on.',
    'kinds by stage: collect rainwater, then pump it',
    [
        K('Water butt', [
            ['Form', ['Standard barrel', 'Decorative barrel or urn']],
            ['Set-up', ['Single butt', 'Linked twin kit', 'With stand and diverter']]]),
        K('Garden water pump', [
            ['Type', ['Surface booster', 'Submersible', 'Barrel pump']],
            ['Power source', ['Mains', 'Battery-powered']]]),
    ])
carry = SH(
    'Cans, hoses & fittings',
    'What carries water from the tap or butt to the plant: watering cans, hoses, reels, fittings and nozzles.',
    'kinds by how water is carried to the plant: hand-carried can, hose, hose storage, joins, spray head',
    [
        K('Watering can', [
            ['Use', ['Outdoor long-reach', 'Indoor long-spout']],
            ['Material', ['Metal', 'Plastic']],
            ['Capacity', ['Small', 'Medium', 'Large']]]),
        K('Garden hose', [
            ['Construction', ['Reinforced', 'Anti-kink', 'Flat']],
            ['Format', ['Standard', 'Expandable']]],
          see=[['C8', 'Flexible hose', 'plumbing hose']]),
        K('Hose reel', [
            ['Mounting', ['Wall-mounted', 'Freestanding cart']],
            ['Winding', ['Hand crank', 'Auto-rewind']]]),
        K('Hose fittings', [
            ['Connection', ['Tap connector', 'Hose-to-hose connector', 'Quick-connect', 'Thread adaptor']],
            ['Thread', ['Garden hose thread (GHT)', 'British Standard Pipe (BSP)', 'NPT']]],
          a='hose connector · hose coupling · hose adaptor',
          d_='Connectors, couplings and adaptors that join a hose to a tap, a tool or another hose.'),
        K('Hose nozzle & spray gun', [
            ['Form', ['Spray nozzle', 'Pistol-grip spray gun', 'Lance']],
            ['Pattern', ['Single jet', 'Multi-pattern']]],
          new=True, a='spray gun · hose gun · spray nozzle',
          d_='Fitting on the end of a hose that shapes the water into a jet, spray or mist.', s=S_GH),
    ])
auto = SH(
    'Sprinklers & irrigation',
    'Equipment that waters on its own, over a lawn, along a row, at a tree or on a timer; carrying water by hand is on the previous shelf.',
    'kinds by how water is spread: spray over an area, seep along a hose, drip at the root, slow-release at a tree, timed control',
    [
        K('Lawn sprinkler', [
            ['Pattern', ['Oscillating', 'Rotary', 'Pulsating', 'Pop-up']],
            ['Mounting', ['Ground spike', 'Sled base', 'Buried']]]),
        K('Soaker hose', [['Construction', ['Porous rubber', 'Perforated flat hose']]]),
        K('Drip irrigation kit', [
            ['Scale', ['Pot and balcony kit', 'Border and bed kit', 'Vegetable-bed kit']],
            ['Water source', ['Mains tap', 'Tank-fed']]]),
        K('Tree watering bag', [['Capacity', ['Small', 'Large']]]),
        K('Irrigation controller', [
            ['Format', ['Tap timer', 'Multi-zone controller', 'Smart (app) controller']],
            ['Power source', ['Battery', 'Mains']]]),
    ])
ponds = SH(
    'Garden ponds',
    'What makes and circulates a garden pond: liners, rigid shells and pumps; fish, filters and pond plants are sold under pets and plants.',
    'kinds by what makes the pond: flexible sheet, rigid shell, pump to move the water',
    [
        K('Pond liner', [['Material', ['EPDM rubber', 'PVC', 'Butyl']]],
          see=[['B10', 'Pond filter', 'filtration is sold with pond fish gear']]),
        K('Preformed pond', [
            ['Material', ['Rigid plastic', 'Fibreglass']],
            ['Style', ['Formal', 'Informal']]],
          d_='Rigid moulded pond shell set into the ground.',
          see=[['C3', 'Water lily', 'a pond plant']]),
        K('Pond pump', [
            ['Job', ['Filter feed', 'Fountain', 'Waterfall']],
            ['Power source', ['Mains', 'Solar']]],
          see=[['B10', 'Pond pump', 'the same pump sold for pond fish care'],
               ['B4', 'Garden fountain', 'a water feature']]),
    ])
depts.append(DP(
    'Watering & ponds',
    'Equipment that stores, carries and delivers water to a garden and holds it in a pond; pond fish and filters go under pets.',
    'Where is the water on its way: stored and pumped, carried to the plant, delivered automatically, or held in a pond?',
    [store, carry, auto, ponds]))

# ------------------------------------------------------------------ 6 POTS, BEDS & SUPPORTS
pots = SH(
    'Pots, planters & raised beds',
    'Containers and beds that hold plant roots, from pots and window boxes to hanging baskets and raised beds; the soil in them goes under Soil, feed & plant care.',
    'kinds by how the roots are held: portable pot, window box, hanging basket, breathable bag, self-watering reservoir, bed above ground',
    [
        K('Plant pot', [
            ['Material', ['Terracotta', 'Glazed ceramic', 'Plastic', 'Fibreclay']],
            ['Drainage', ['With drainage hole', 'Cachepot (outer pot, no drainage)']],
            ['Fitted with', ['Separate saucer']],
            ['Format', ['Standard', 'Vertical wall planter']]]),
        K('Window box', [['Material', ['Wood', 'Terracotta', 'Metal', 'Fibreglass', 'Vinyl']]],
          new=True, a='window flower box · window box planter',
          d_='Long planter fixed on or just below a window sill or railing so plants can be tended from indoors.',
          s=S_WB),
        K('Hanging basket', [
            ['Material', ['Wire', 'Rustic', 'Plastic']],
            ['Liner', ['Coir', 'Moss', 'Fibre']]]),
        K('Fabric grow pot', [['Material', ['Felt', 'Woven polypropylene']]]),
        K('Self-watering planter', [['Reservoir', ['Built-in base reservoir', 'Wick-fed']]]),
        K('Raised bed', [
            ['Material', ['Timber', 'Metal', 'Fabric']],
            ['Height', ['Ground-level frame', 'Elevated on legs']]]),
    ])
supports = SH(
    'Supports & ties',
    'What holds a plant up or fixes it in place: stakes, canes, trellis, arches, obelisks, ties and labels.',
    'kinds by what is held: a single upright stem, a climbing wall, a free-standing frame, then the tie and the label',
    [
        K('Plant stake & cane', [
            ['Form', ['Bamboo cane', 'Wooden stake', 'Metal stake', 'Ring or cage frame']]],
          old='Plant support',
          d_='Single upright, ring or cage that holds up a tall or heavy-headed plant.', a='stake · cane · support frame · plant cage'),
        K('Trellis', [
            ['Material', ['Wood', 'Bamboo', 'Metal']],
            ['Style', ['Fan', 'Panel', 'Slatted screen']]],
          old='Plant support', drop_x='all',
          d_='Open lattice of wood, bamboo or metal that holds climbing plants against a wall or fence.',
          s=S_TREL, a='trellis panel'),
        K('Garden arch & obelisk', [
            ['Form', ['Arch', 'Arbour', 'Obelisk (triangular)', 'Obelisk (tower)']],
            ['Material', ['Wood', 'Metal']]],
          new=True, a='rose arch · obelisk · garden tower',
          d_='Free-standing frame for climbers: an arch or arbour to walk through, or an obelisk to grow plants up.',
          s=S_GT2),
        K('Plant tie', [
            ['Material', ['Twine', 'Wire', 'Soft plastic or rubber']],
            ['Form', ['Clip', 'Tying tool (tapener)']]],
          old='Plant tie & label', a='garden twine · plant clip · tapener',
          d_='Twine, wire, clip or tool that fastens a plant to its support.'),
        K('Plant label', [
            ['Form', ['Pushed into the soil', 'Tied on', 'Pot-edge clip']]],
          old='Plant tie & label', a='garden label · plant marker',
          d_='Marker that names a plant or variety, pushed into the soil or tied on.'),
    ])
covers = SH(
    'Covers, fleece & netting',
    'Cloth, netting and small covers laid or hung over plants against frost, birds and pests; permanent structures go under Greenhouses & indoor growing.',
    'kinds by what the cover keeps off: frost, birds and pests, weather over a single plant',
    [
        K('Horticultural fleece', see=[['C8', 'Weed membrane', 'for weed suppression instead']]),
        K('Plant netting'),
        K('Cloche', [
            ['Form', ['Glass bell', 'Lantern', 'Tunnel']]],
          see=[['C2', 'Cold frame', 'larger low shelter']]),
    ])
depts.append(DP(
    'Pots, beds & plant supports',
    'Things that hold plant roots, hold a plant up or cover it: pots, beds, supports and covers; soil, feed and the plants themselves are elsewhere.',
    'Does it hold the roots, hold the plant up, or cover the plant?',
    [pots, supports, covers]))

# ------------------------------------------------------------------ 7 SOIL, FEED & PLANT CARE
OLD_PC = OLD['Potting compost, soil & mulch']
soil = SH(
    'Compost, soil & mulch',
    'Bagged growing media and ground cover: potting compost, topsoil, soil improver, mulch and grow bags; bags of gravel and bark chippings for paths go with building materials.',
    'kinds by where they go: in pots, in beds as soil, in beds as feed, on top as cover, in a ready-filled bag',
    [
        K('Potting compost', [
            ['Blend', ['Multi-purpose', 'Seed and cutting', 'Ericaceous', 'John Innes']],
            ['Peat content', ['Peat-free', 'Peat-based']]],
          old='Potting compost, soil & mulch', a='compost · growing medium · multi-purpose compost',
          d_='Growing medium for pots and seed trays, sold by blend and by whether it contains peat.'),
        K('Topsoil', [['Grade', ['Screened', 'General purpose']]],
          old='Potting compost, soil & mulch', a='garden soil',
          d_='Bagged or bulk garden soil for filling beds, levelling lawns and raising ground levels.'),
        K('Soil improver', [['Material', ['Composted bark', 'Manure', 'Garden compost', 'Mushroom compost']]],
          old='Potting compost, soil & mulch', a='soil conditioner · manure',
          d_='Organic material dug into a bed to feed the soil and improve its structure.'),
        K('Mulch', [
            ['Material', ['Bark chips', 'Wood chips', 'Straw', 'Pine straw', 'Compost']],
            ['Colour', ['Natural', 'Dyed']]],
          new=True, a='bark mulch · bark chippings',
          d_='Layer spread over soil to hold moisture and hold down weeds, such as bark, wood chips or straw.',
          s=S_MULCH,
          see=[['C8', 'Garden gravel', 'stone ground cover'],
               ['C8', 'Weed membrane', 'sheet laid under mulch']]),
        K('Grow bag', [['Fill', ['Multi-purpose compost', 'Tomato compost']]],
          old='Potting compost, soil & mulch', a='growing bag',
          d_='Sealed plastic bag of compost laid flat, cut open and planted directly, mainly for tomatoes and salad crops.'),
    ])
for kk in soil['k']:
    if kk['n'] != 'Potting compost':
        kk.pop('m', None); kk.pop('r', None); kk.pop('x', None)
make = SH(
    'Composting & soil testing',
    'Equipment for making compost, sifting soil and finding out what a bed needs; the compost itself is on the previous shelf.',
    'kinds by stage: make compost, sift it, test the soil',
    [
        K('Compost bin', [
            ['Form', ['Static bin', 'Tumbler', 'Wormery', 'Hot composter']],
            ['Material', ['Plastic', 'Timber']]]),
        K('Garden sieve', [
            ['Mesh', ['Fine', 'Coarse']],
            ['Frame', ['Wooden frame', 'Metal frame']]]),
        K('Soil test kit', [
            ['Measures', ['pH', 'NPK nutrients']],
            ['Method', ['Colour-change test', 'Electronic probe']]]),
    ])
feeds = SH(
    'Feeds & plant protection',
    'Products that feed plants or kill weeds, insects, slugs and fungi, and the sprayer to apply them; sprays for the home against pests are sold with household pest control.',
    'kinds by what they do: feed, kill weeds, kill insects, kill slugs, treat fungus, then apply',
    [
        K('Fertiliser', [
            ['Form', ['Granular', 'Liquid', 'Slow-release']],
            ['Use', ['All-purpose', 'Lawn feed', 'Tomato feed', 'Rose feed']]]),
        K('Herbicide', [
            ['Form', ['Concentrate', 'Ready-to-use']],
            ['Action', ['Contact', 'Systemic']],
            ['Range', ['Total weedkiller', 'Selective lawn weedkiller']]],
          see=[['C8', 'Weed membrane', 'non-chemical weed control']]),
        K('Insecticide', [
            ['Form', ['Ready-to-use spray', 'Concentrate']],
            ['Origin', ['Synthetic', 'Organic']]],
          see=[['B8', 'Insecticide', 'the same product sold for home pests']]),
        K('Slug pellets', [
            ['Active ingredient', ['Iron phosphate', 'Aluminium sulphate', 'Metaldehyde']],
            ['Form', ['Pellets', 'Bait']]],
          new=True, a='slug killer · snail bait · molluscicide',
          d_='Pellets or bait scattered round plants to kill slugs and snails.', s=S_MOL),
        K('Fungicide', [
            ['Form', ['Spray', 'Powder']],
            ['Action', ['Protective', 'Curative']]]),
        K('Garden sprayer', [
            ['Format', ['Trigger bottle', 'Pump-up pressure', 'Backpack']],
            ['Power source', ['Hand-pumped', 'Battery-powered']]]),
    ])
depts.append(DP(
    'Soil, feed & plant care',
    'What plants grow in, how that soil is made and tested, and what is added to feed or protect them; pots and beds go under Pots, beds & plant supports.',
    'Is it what the plant grows in, the means to make and test it, or what is added to feed or protect the plant?',
    [soil, make, feeds]))

# ------------------------------------------------------------------ 8 GREENHOUSES & INDOOR GROWING
shelters = SH(
    'Greenhouses, polytunnels & cold frames',
    'Structures that shelter plants outdoors, from walk-in glasshouses to hoop tunnels and low frames; garden sheds and summerhouses are garden buildings.',
    'kinds by size: walk-in glasshouse, walk-in hoop tunnel, low frame',
    [
        K('Greenhouse', [
            ['Frame', ['Aluminium', 'Cedar', 'Steel']],
            ['Glazing', ['Glass', 'Polycarbonate']],
            ['Shape', ['Free-standing', 'Lean-to', 'Octagonal']]],
          see=[['G3', 'Garden shed', 'garden building']]),
        K('Polytunnel', [
            ['Size', ['Domestic (6 to 14 ft wide)', 'Commercial (16 ft wide and over)', 'Mini polytunnel']],
            ['Cover', ['Polythene', 'Net']]]),
        K('Cold frame', [
            ['Material', ['Aluminium', 'Cedar']],
            ['Glazing', ['Polycarbonate', 'Toughened glass']],
            ['Type', ['Standard', 'Hotbed', 'Bulb frame']]],
          see=[['C2', 'Cloche', 'smaller cover over one plant']]),
    ])
climate = SH(
    'Greenhouse climate kit',
    'Fittings that control the temperature, sunlight and moisture inside a greenhouse.',
    'kinds by what they control: temperature, sunlight, moisture',
    [
        K('Greenhouse heater', [
            ['Fuel', ['Electric', 'Paraffin', 'Gas']]],
          new=True, a='greenhouse warmer',
          d_='Heater that keeps a greenhouse above frost and evens out swings in outdoor temperature.', s=S_GW),
        K('Greenhouse shading', [
            ['Form', ['Roller blind', 'Shade cloth', 'Shading paint']]],
          new=True, a='shade blind · shade netting',
          d_='Blind, cloth or paint that cuts strong sun so plants do not scorch.', s=S_GW),
        K('Capillary matting', [['Format', ['Roll', 'Cut mat']]],
          new=True, a='water-retaining matting',
          d_='Absorbent mat laid under pots that wicks water up from a reservoir to keep roots moist.', s=S_GW),
    ])
propag = SH(
    'Seed raising',
    'Trays and covered, heated beds for sowing seed and rooting cuttings.',
    'kinds by stage: tray that holds the seed, covered and heated bed that starts it',
    [
        K('Seed tray', [
            ['Format', ['Plain tray', 'Tray with cell inserts', 'Modular trays']],
            ['Material', ['Plastic', 'Biodegradable']]],
          new=True, a='seed trays and inserts · propagation tray',
          d_='Shallow tray, often with cell inserts, in which seed is sown and seedlings raised.', s=S_GW),
        K('Propagator', [
            ['Heating', ['Heated', 'Unheated']],
            ['Size', ['Windowsill', 'Full-size tray']]]),
    ])
indoor = SH(
    'Lights, tents & hydroponics',
    'Equipment for growing plants indoors without sun or soil: lights, enclosures, nutrient systems and the controllers that run them.',
    'kinds by what they supply: light, enclosure, nutrient water, control',
    [
        K('Grow light', [['Lamp', ['LED', 'HPS', 'CMH', 'Fluorescent']]]),
        K('Grow tent', [['Size', ['Compact', 'Standard', 'Large']]]),
        K('Hydroponic system', [['System', ['Deep water culture', 'Nutrient film', 'Drip', 'Wick']]]),
        K('Grow environment controller', [['Controls', ['Lights', 'Fans', 'Humidity', 'Temperature']]]),
    ])
depts.append(DP(
    'Greenhouses & indoor growing',
    'Structures and equipment for growing under cover, outdoors in a greenhouse or indoors under lights; garden sheds and summerhouses are buildings.',
    'Is it the shelter, the climate kit inside it, the kit for raising seedlings, or an indoor growing setup?',
    [shelters, climate, propag, indoor]))

# ------------------------------------------------------------------ 9 CLEARING, CLEANING & SNOW
debris = SH(
    'Leaves, debris & dirt',
    'Tools that clear leaves, loose debris and ground-in dirt from lawns, paths and patios; clippings brushed up by a rotating brush are a lawn sweeper.',
    'kinds by how the surface is cleared: hand rake, blast of air, water jet',
    [
        K('Leaf rake', [['Material', ['Steel', 'Plastic', 'Bamboo']]]),
        K('Leaf blower', [
            ['Format', ['Handheld', 'Backpack', 'Blower-vac']],
            ['Power source', ['Cordless', 'Corded electric', 'Petrol']]],
          see=[['C2', 'Lawn sweeper', 'brushes debris up instead']]),
        K('Pressure washer', [
            ['Power source', ['Electric', 'Petrol']],
            ['Class', ['Light-duty', 'Medium', 'Heavy-duty']]]),
    ])
waste = SH(
    'Garden waste',
    'Tools that carry, shred or chip garden waste.',
    'kinds by what is done with the waste: carry, shred, chip',
    [
        K('Wheelbarrow', [
            ['Wheels', ['Single wheel', 'Two wheel']],
            ['Tray', ['Steel', 'Plastic']],
            ['Power source', ['Hand-pushed', 'Battery-powered']]],
          a='garden cart · barrow'),
        K('Garden shredder', [
            ['Mechanism', ['Impact', 'Quiet roller']]]),
        K('Wood chipper', [
            ['Power source', ['Electric', 'Petrol']],
            ['Branch size', ['Light', 'Medium', 'Heavy']]]),
    ])
snow = SH(
    'Snow clearing',
    'Hand and powered tools that clear snow from paths and drives.',
    None,
    [
        K('Snow shovel', [
            ['Form', ['Shovel', 'Pusher']],
            ['Material', ['Plastic', 'Aluminium', 'Steel']]],
          see=[['C2', 'Snow blower', 'powered']]),
        K('Snow blower', [
            ['Stages', ['Single-stage', 'Two-stage']],
            ['Power source', ['Petrol', 'Electric', 'Cordless']]],
          see=[['C7', 'Tractor snow blade and blower', 'tractor-mounted']]),
    ])
depts.append(DP(
    'Clearing, cleaning & snow',
    'Machines and tools that clear leaves, dirt, waste and snow from a garden and its paths; cutting plants goes under Cutting & pruning.',
    'What is being cleared: loose leaves and dirt, cut waste, or snow?',
    [debris, waste, snow]))

# ------------------------------------------------------------------ 10 POOLS
pools = SH(
    'Pools & covers',
    'Movable pools, their covers and ladders: framed and soft-sided pools; built-in pools are part of the home.',
    'kinds by structure: rigid frame, flexible wall, cover, way in',
    [
        K('Above-ground pool', [
            ['Wall', ['Steel frame', 'Metal wall']],
            ['Shape', ['Round', 'Rectangular', 'Oval']]],
          see=[['G3', 'In-ground swimming pool', 'built-in pool']]),
        K('Soft-sided pool', [
            ['Support', ['Inflatable ring', 'Held up by the water']],
            ['Size', ['Paddling pool', 'Family pool']]],
          see=[['E1', 'Paddling pool', "children's play pool"]]),
        K('Pool cover', [['Purpose', ['Solar cover', 'Winter cover', 'Safety cover', 'Leaf cover']]]),
        K('Pool ladder & steps', [
            ['Fit', ['Above-ground', 'In-ground']],
            ['Form', ['Ladder', 'Steps']]],
          new=True, a='pool steps',
          d_='Ladder or steps fixed to a pool edge to get in and out of the water.', s=S_INYO),
    ])
mach = SH(
    'Pumps, filters & heating',
    'The machinery that circulates, strains, sanitises and warms pool water.',
    'kinds in the order of the water flow: pump, filter, salt cell, heater, then spare parts',
    [
        K('Pool pump', [
            ['Speed', ['Single-speed', 'Variable-speed']],
            ['Fit', ['In-ground pool', 'Above-ground pool']],
            ['Job', ['Main circulation', 'Booster for a cleaner']]]),
        K('Pool filter', [['Medium', ['Sand', 'Cartridge', 'Diatomaceous earth (DE)']]]),
        K('Salt chlorinator'),
        K('Pool heater', [['Energy', ['Gas', 'Electric', 'Solar', 'Heat pump']]]),
        K('Pool spare parts', [['Part', ['Filter cartridge', 'DE grid']]]),
    ])
clean = SH(
    'Pool cleaning',
    'Machines and hand tools that remove dirt and leaves from a pool.',
    'kinds by who does the work: self-driving machine, then hand tools for the wall, the surface and the floor',
    [
        K('Pool cleaner', [
            ['Drive', ['Robotic', 'Suction-side', 'Pressure-side']],
            ['Job', ['Floor and wall cleaner', 'Surface skimmer (often solar)']]]),
        K('Pool brush', [['Surface', ['Vinyl-safe soft bristles', 'Concrete stiff bristles']]],
          new=True, a='pool wall brush',
          d_='Brush on a telescopic pole that scrubs pool walls and floor.', s=S_INYO),
        K('Pool skimmer net', [['Net', ['Shallow surface net', 'Deep bottom net']]],
          new=True, a='leaf skimmer · leaf rake',
          d_='Net on a telescopic pole that lifts leaves and debris off the water surface or the floor.', s=S_INYO),
        K('Pool vacuum head', [['Surface', ['Vinyl', 'Concrete']]],
          new=True, a='manual pool vacuum',
          d_='Head that fits a pole and hose to vacuum the pool floor by hand.', s=S_INYO),
    ])
water = SH(
    'Water care',
    'What tests the pool water and keeps it safe to swim in.',
    'kinds by step: measure, then treat',
    [
        K('Pool test kit', [['Method', ['Test strips', 'Liquid drop kit', 'Digital tester']]]),
        K('Pool sanitiser', [['Form', ['Chlorine tablets', 'Chlorine granules']]]),
        K('Pool thermometer', [['Form', ['Floating', 'Digital']]],
          new=True, a='water thermometer',
          d_='Thermometer that floats in or hangs from a pool to read the water temperature.', s=S_INYO),
    ])
depts.append(DP(
    'Pools & pool care',
    'Movable pools and the machinery, cleaners and chemicals that keep the water clean; built-in pools are part of the home.',
    'Is it the pool, the machinery that moves and heats the water, the cleaning, or the water treatment?',
    [pools, mach, clean, water]))

# ------------------------------------------------------------------ 11 OUTDOOR COOKING
kettle = K('Kettle grill', [
    ['Fuel', ['Charcoal', 'Gas-assist']],
    ['Shape', ['Round', 'Square']],
    ['Size', ['Compact', 'Standard', 'Large']]],
    merge=['Barbecue grill'], a='kettle barbecue · charcoal grill · barbecue grill',
    d_='Lidded round bowl grill on legs that cooks over charcoal, used for direct grilling or, with the coals to one side, roasting.')
renames['Barbecue grill'] = 'Kettle grill'
lidded = SH(
    'Lidded grills & smokers',
    'Full-size cookers with a lid or chamber, fuelled by charcoal, gas, pellets or mains electricity; open grates and carried grills go on the next shelf.',
    'kinds by fuel and chamber: charcoal in a bowl, egg, drum or firebox, then gas, pellets and electricity',
    [
        kettle,
        K('Kamado grill', [
            ['Material', ['Ceramic', 'Insulated steel']],
            ['Size', ['Table-top (mini)', 'Standard', 'Large']]]),
        K('Bullet smoker', [
            ['Design', ['Water smoker', 'Upright drum smoker']],
            ['Fuel', ['Charcoal', 'Gas', 'Electric']]],
          drop_x=['Upright drum smoker'],
          see=[['B5', 'Smoker box and curing equipment', 'indoor smoking gear']]),
        K('Offset smoker', [['Airflow', ['Classic offset', 'Reverse flow']]]),
        K('Gas grill', [
            ['Fuel', ['Propane (LPG)', 'Natural gas']],
            ['Burners', ['Infrared sear burner', 'Side burner']],
            ['Format', ['Freestanding cart', 'Built-in head']]]),
        K('Pellet grill', [
            ['Controller', ['Dial', 'Wi-Fi']],
            ['Combo', ['Pellet grill with griddle']]]),
        K('Electric grill', [['Format', ['Table-top', 'Cart']]],
          new=True, a='electric barbecue',
          d_='Grill heated by a mains electric element, so it needs no charcoal or gas.', s=S_BBQ,
          see=[['B5', 'Electric grill and hotplate', 'indoor kitchen appliance']]),
    ])
open_ = SH(
    'Open & portable cookers',
    'Cookers with no lid or chamber, or small enough to carry: open grates, flat plates and travel grills.',
    'kinds by how the food meets the heat: open grate over fire, flat steel plate, small carried grill',
    [
        K('Open-fire grill', [
            ['Format', ['Freestanding', 'Portable', 'Built-in', 'Tabletop']],
            ['Grate', ['Fixed', 'Adjustable height']],
            ['Form', ['Brazier (no lid)']]]),
        K('Flat-top griddle', [
            ['Fuel', ['Gas', 'Pellet']],
            ['Format', ['Cart', 'Tabletop']],
            ['Lid', ['Open', 'With hood']]],
          see=[['B5', 'Griddle & tawa', 'cookware version']]),
        K('Portable grill', [
            ['Fuel', ['Charcoal', 'Gas cartridge or propane', 'Electric']],
            ['Form', ['Tabletop', 'Folding legs']]],
          see=[['E2', 'Camping stove', 'stove for camping']]),
    ])
ovens = SH(
    'Outdoor ovens',
    'Ovens for baking pizza, flatbread and roasting outdoors; grills and smokers are on the other shelves.',
    'kinds by oven form: open domed oven, deep vase-shaped clay oven',
    [
        K('Pizza oven', [
            ['Fuel', ['Wood-fired', 'Gas', 'Multi-fuel', 'Wood pellet', 'Electric']],
            ['Format', ['Portable', 'Countertop', 'Freestanding on a stand or cart', 'Built-in masonry']]],
          drop_x=['Masonry (brick) oven'],
          see=[['B5', 'Pizza stone', 'baking stone for a grill or oven']]),
        K('Tandoor', [
            ['Material', ['Clay', 'Stainless steel', 'Mild steel drum']],
            ['Fuel', ['Charcoal or wood', 'Gas', 'Electric']]],
          new=True, a='tandir · tonir · tannur',
          d_='Deep vase-shaped oven, usually clay, with a fire in the base, used for flatbreads on the wall and meat on skewers.',
          s=S_TAN),
    ])
fire = SH(
    'Fire pits & patio heating',
    'Features that warm people outdoors with open fire or radiant heat; cookers are on the other shelves.',
    'kinds by how they heat: open fire in a container, enclosed fireplace, bottle-fed chimney, radiant heater',
    [
        K('Fire pit', [
            ['Fuel', ['Wood-burning', 'Gas or propane', 'Bioethanol']],
            ['Form', ['Fire bowl', 'Fire ring', 'Smokeless double-wall', 'Table']]],
          add_x=[X('Dakota fire pit', 'Two-hole fire pit that draws air through a second hole and so burns with little smoke.',
                   S_FP)]),
        K('Outdoor fireplace', [['Fuel', ['Wood', 'Gas']]],
          new=True, a='garden fireplace',
          d_='Freestanding or built chimney fireplace that holds the whole fire, as an alternative to an open ring.',
          s=S_FP),
        K('Chiminea', [['Material', ['Clay', 'Cast iron', 'Aluminium']]]),
        K('Patio heater', [
            ['Fuel', ['Propane', 'Natural gas', 'Electric']],
            ['Mounting', ['Freestanding', 'Wall-mounted', 'Hanging', 'Tabletop']]],
          see=[['B7', 'Portable gas heater', 'indoor and outdoor gas heater']]),
    ])
accs = SH(
    'Fuel & accessories',
    'What fuels, lights, tends and measures an outdoor cooker; the cookers themselves are on the other shelves.',
    'kinds in the order of use: fuel, lighting, tending, measuring, roasting',
    [
        K('Barbecue fuel', [
            ['Charcoal', ['Lump charcoal', 'Briquettes', 'Binchotan (white charcoal)']],
            ['Wood', ['Pellets', 'Cooking chunks', 'Smoking chips', 'Logs']],
            ['Gas', ['Propane']]],
          see=[['C8', 'Lump charcoal', 'charcoal sold as fuel'],
               ['C8', 'Charcoal briquettes', 'briquettes sold as fuel'],
               ['C8', 'Smoking wood', 'wood chunks and chips']]),
        K('Chimney starter', [['Form', ['Steel cylinder', 'Lighting cone']]],
          see=[['C8', 'Firelighter', 'other way to light a fire']]),
        K('Barbecue tools & accessories', [
            ['Handling food', ['Tongs', 'Spatula', 'Fork', 'Grill basket', 'Pizza peel']],
            ['Care', ['Grill brush', 'Grill cover']]],
          d_='Hand tools and add-ons for turning, holding and cleaning food and grills.'),
        K('Grill thermometer', [['Reading', ['Dial', 'Leave-in probe', 'Wireless']]],
          see=[['B5', 'Kitchen thermometer', 'kitchen use']]),
        K('Rotisserie', [['Parts', ['Spit rod', 'Electric motor kit']]]),
    ])
depts.append(DP(
    'Outdoor cooking',
    'Cookers, fire features and gear for cooking and keeping warm outdoors; built-in outdoor kitchens are home features and camp stoves are camping gear.',
    'Is it a cooker, a fire or heater to sit by, or something used with a cooker?',
    [lidded, open_, ovens, fire, accs]))

# ------------------------------------------------------------------ assemble
new = {
    'c': d['c'], 'rev': d['rev'], 'lead': d['lead'], 'b': d.get('b', []),
    'ax': 'Which garden job is it for: mowing, cutting plants, digging, bonsai, watering, holding plants, feeding and protecting, growing under cover, clearing, swimming or cooking outdoors?',
    'key': [
        '1. Does it mow, edge or treat a lawn? → Lawn care',
        '2. Does it cut stems, branches, hedges, grass or brush, by hand or by motor? → Cutting & pruning',
        '3. Does it dig, break, level or plant the soil? → Digging & planting',
        '4. Is it a pot, display piece or tool made for bonsai? → Bonsai',
        '5. Does it store, carry or spread water for plants, or hold a pond? → Watering & ponds',
        '6. Does it hold plant roots, hold a plant up or cover it? → Pots, beds & plant supports',
        '7. Is it soil, compost, feed, a weed, pest or disease product, or a tool to make or test soil? → Soil, feed & plant care',
        '8. Does it shelter plants under cover, or raise them with heat and light? → Greenhouses & indoor growing',
        '9. Does it clear leaves, dirt, waste or snow? → Clearing, cleaning & snow',
        '10. Is it a movable pool, or equipment to circulate, clean or treat its water? → Pools & pool care',
        '11. Does it cook food or warm people outdoors? → Outdoor cooking',
        '<i>Precedence: a bonsai tool is Bonsai (step 4) before Cutting & pruning (step 2); a pool pump is Pools (step 10) before Watering & ponds (step 5); a fire pit that only warms people stays in Outdoor cooking (step 11).</i>',
    ],
    'depts': depts,
}
json.dump(new, open(OUT + '.tmp', 'w'), indent=1, ensure_ascii=False)
os.replace(OUT + '.tmp', OUT)

# check every old kind is accounted for
newnames = {k['n'] for dp in depts for s in dp['s'] for k in s['k']}
lost = [n for n in OLD if n not in newnames and n not in renames]
print('old kinds not carried by name:', lost)
json.dump(renames, open(ROOT + '/work/STR_C2/renames_pending.json', 'w'), indent=1)
