import json, os, sys, shutil, copy, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c1struct as S

R = '/home/user/Possession-Taxonomy/rebuild'
W = R + '/work/STR_C1'
src = R + '/work/STR_C1/bak/C1.json'
if not os.path.exists(src):
    os.makedirs(W + '/bak', exist_ok=True)
    shutil.copy(R + '/out/C1.json', src)
    for f in ('C1_brands.json', 'C1_moves.json'):
        shutil.copy(R + '/out/' + f, W + '/bak/' + f)
old = json.load(open(src))

LIST = 'https://en.wikipedia.org/wiki/List_of_tools'
WRENCH = 'https://en.wikipedia.org/wiki/Wrench'
TROWEL = 'https://en.wikipedia.org/wiki/Trowel'
ROUTER = 'https://en.wikipedia.org/wiki/Router_(woodworking)'
CLAMP = 'https://en.wikipedia.org/wiki/Clamp_(tool)'
WELD = 'https://en.wikipedia.org/wiki/Welding'
LADDER = 'https://en.wikipedia.org/wiki/Ladder'
TOOLBOX = 'https://en.wikipedia.org/wiki/Toolbox'
PPE = 'https://en.wikipedia.org/wiki/Personal_protective_equipment'
HPLANE = 'https://en.wikipedia.org/wiki/Hand_plane'
SPY = 'https://en.wikipedia.org/wiki/Spyderco'
SAK = 'https://en.wikipedia.org/wiki/Swiss_Army_knife'

def K(n, d, s, a=''):
    return {"n": n, "a": a, "d": d, "s": s}

NEW = [
 K("Powder-actuated tool", "Tool that drives a pin or nail into concrete or steel with a small explosive charge.", LIST, "nail gun for concrete"),
 K("Router bit", "Cutter that fits a router to cut grooves, rebates, edge profiles and joints, from straight and flush-trim bits to ogee and dovetail bits.", ROUTER),
 K("Adze", "Axe-like tool with the blade set across the handle, swung to dress and hollow timber.", LIST),
 K("Mitre box", "Open box or frame with slots that guide a back saw through accurate angled cuts.", LIST, "miter box"),
 K("Bench hook", "Board with a stop that hooks over the bench edge and holds work still for sawing by hand.", LIST),
 K("Handscrew", "Clamp with two wooden jaws closed by two spindles, for gluing and holding without marking the work.", CLAMP, "hand screw · wooden clamp"),
 K("Toggle clamp", "Lever clamp that locks over centre to hold work down quickly, fitted to benches and jigs.", CLAMP, "hold-down clamp"),
 K("Nut driver", "Screwdriver-style tool with a hex socket that turns small nuts and hex-head screws.", LIST),
 K("Open-ended spanner", "One-piece spanner with a U-shaped jaw that grips two flats of a nut or bolt head, usually double-ended.", WRENCH, "open-end wrench"),
 K("Ring spanner", "One-piece spanner with a closed ring, six- or twelve-point, that grips all round a nut or bolt head.", WRENCH, "box-end wrench"),
 K("Breaker bar", "Long non-ratcheting socket handle that gives high leverage to free tight bolts.", WRENCH, "knuckle bar"),
 K("Pincers", "Pivoted jaws with sharp cutting edges, used to pull nails and nip off wire.", LIST),
 K("Tin snips", "Hand shears with short strong blades for cutting sheet metal; straight, left-cut and right-cut patterns.", LIST, "aviation snips"),
 K("Bolt cutter", "Long-handled cutter with compound leverage for chain, padlock shackles, bolts and rod.", LIST, "bolt cutters"),
 K("Screw extractor", "Reverse-threaded or fluted bit that bites into a broken screw so it can be backed out.", LIST),
 K("Tap and die set", "Taps cut internal threads and dies cut external ones; sold as sets with handles for hand threading.", LIST),
 K("Cold chisel", "Hardened steel chisel struck with a hammer to cut cold metal, brick and concrete.", LIST),
 K("Pipe cutter", "Clamp with a cutting wheel that is turned round a pipe to cut it square.", LIST, "tube cutter"),
 K("Plunger", "Rubber cup on a handle that clears a blocked sink, basin or toilet by pressure and suction.", LIST),
 K("Drain auger", "Flexible coiled cable that is fed into a drain and turned to break or retrieve a blockage.", LIST, "plumber's snake · drain snake"),
 K("Bricklayer's trowel", "Long triangular steel blade on a handle for picking up, spreading and cutting mortar.", TROWEL, "brick trowel"),
 K("Feeler gauge", "Set of thin steel blades of known thickness, pushed into a gap to measure its width.", LIST, "thickness gauge"),
 K("Thread pitch gauge", "Set of toothed leaves that are matched to a screw thread to read its pitch.", LIST, "screw pitch gauge"),
 K("Straightedge", "Rigid bar with one true edge for drawing a straight line or checking a surface is flat.", LIST),
 K("Winding sticks", "Pair of straight, parallel sticks sighted across a board to show whether it is twisted.", LIST),
 K("Scriber", "Hard pointed tool that scratches a fine line on metal or wood for cutting or drilling to.", LIST, "scribe"),
 K("Plumb bob", "Pointed weight on a string that hangs true vertical for marking or checking plumb.", LIST, "plummet"),
 K("Chalk line", "Reel of string in a chalk case that is snapped against a surface to leave a long straight line.", LIST, "chalk reel"),
 K("Voltage tester", "Pen or probe that shows whether a wire or socket is live, with or without touching the conductor.", LIST, "non-contact voltage tester"),
 K("Spot welder", "Welder whose copper electrodes press and pass current through overlapping sheets to fuse a spot.", WELD, "resistance spot welder"),
 K("Oxy-fuel cutting and welding set", "Torch, hoses, regulators and gas cylinders that burn oxygen with a fuel gas to weld, braze and cut steel.", WELD, "oxy-acetylene set · cutting torch"),
 K("Radial arm saw", "Circular saw hung from an arm over a table, pulled across the work to crosscut and rip.", LIST),
 K("Tongs", "Pivoted gripping tools for holding hot metal at the forge and anvil.", LIST),
 K("Platform ladder", "Stepladder with a large work platform and top handrail, so the user can stand and work with both hands.", LADDER),
 K("Mobile safety steps", "Self-supporting steps on wheels or castors, often with a small platform and handrail.", LADDER, "rolling steps"),
 K("Tool belt", "Belt with pockets and loops worn on the body to carry the tools needed for the job.", TOOLBOX, "tool apron"),
 K("Bucket organiser", "Fabric sleeve of pockets that fits round a plastic bucket to hold tools.", TOOLBOX, "bucket tool organizer"),
 K("Safety goggles", "Eye protection that seals round the eyes against dust, splashes and flying chips.", PPE, "goggles"),
]
NEWD = {k['n']: k for k in NEW}

# archetypes removed because they describe a type, not a named thing (kind, archetype)
DEMOTE = {
 'Bench plane': ['Infill plane'], 'Plough plane': ['Match plane'], 'Moulding plane': ['Hollows and rounds'],
 'Scraper': ['Card scraper'], 'Kanna (Japanese plane)': ['Hira-ganna', 'Shiage-ganna', 'Hikōki-ganna'],
 'Back saw': ['Western dovetail saw', 'Carcass saw', 'Tenon saw', 'Sash saw', "Gent's saw", 'Mitre-box saw', 'Razor saw'],
 'Bow saw': ['Woodworking bucksaw'], 'Ryoba saw': ['Ryoba', 'Azebiki'], 'Dozuki saw': ['Dozuki'], 'Kataba saw': ['Kataba'],
 'Flush-cut saw': ['Kugihiki'],
 'Nomi (Japanese chisel)': ['Oire-nomi', 'Atsu-nomi', 'Mukōmachi-nomi', 'Shinogi-nomi', 'Tsuki-nomi', 'Kote-nomi'],
 'Whetstone': ['Arkansas stone', 'Coticule', 'Japanese natural stone', 'India stone'], 'Bradawl': ['Gimlet'],
 'Bench vice': ['Leg vice'], 'Adjustable wrench': ['Monkey wrench'],
 'Torque wrench': ['Sharp torque measuring wrench', 'Beam torque wrench', 'Click torque wrench'],
 'Socket wrench': ['Richardson ratcheting socket wrench', 'Quick-release ratchet', 'Pass-through socket system', 'Snap-on interchangeable sockets'],
 'Wire stripper': ['Compound automatic wire stripper'], 'Combination pliers': ["Lineman's pliers"],
 'Hacksaw': ['Junior hacksaw', 'Panel hacksaw'], 'File': ['Swiss-pattern file'],
 'Genno (Japanese hammer)': ['Ryōguchi genno', 'Kataguchi genno', 'Daruma genno', 'Funate genno'],
 'Caliper': ['Vernier caliper', 'Dial caliper'], 'Square': ['Try square', "Engineer's square"],
 'Marking gauge': ['Kebiki'], 'Marking knife': ['Shirabiki'], 'Angle finder': ['Sliding T bevel'],
 'Anvil': ['Double-horn anvil', "Farrier's anvil"],
}
# maker ranges: archetype -> range entry on the same kind (or other kind)
TO_R = {
 ('Axe', 'Hults Bruk forest axes'): ('Axe', ['Forest axes', 'Hults Bruk']),
 ('Axe', 'Wetterlings axes'): ('Axe', ['Axes', 'Wetterlings']),
 ('Screwdriver', 'Wiha screwdriver'): ('Screwdriver', ['Screwdrivers', 'Wiha']),
 ('Screwdriver', 'PB Swiss screwdriver'): ('Screwdriver', ['Screwdrivers', 'PB Swiss Tools']),
 ('Rasp', 'Auriou hand-cut rasp'): ('Rasp', ['Hand-cut rasps', 'Auriou']),
 ('Wood lathe', 'Robust lathes'): ('Wood lathe', ['Lathes', 'Robust']),
 ('Combination machine', 'Felder combination machine'): ('Combination machine', ['Combination machines', 'Felder']),
 ('Laser cutter', 'xTool'): ('Laser cutter', ['Laser cutters', 'xTool']),
 ('Micrometer', 'Starrett micrometer'): ('Micrometer', ['Micrometers', 'Starrett']),
 ('Micrometer', 'Moore & Wright micrometer'): ('Micrometer', ['Micrometers', 'Moore & Wright']),
 ('Genno (Japanese hammer)', 'Yamakichi genno'): ('Genno (Japanese hammer)', ['Genno', 'Yamakichi']),
}
MOVE_ARCH = {('Bar clamp', 'Jorgensen handscrew'): 'Handscrew'}
ADD_ARCH = {
 'Lockback folder': [{"n": "Spyderco Endura", "a": "", "d": "Spyderco's lockback folder with a round blade hole, made in several handle materials; the Endura 4 is built in Japan.", "mk": "Spyderco", "y": "", "s": SPY, "v": [], "dt": "handle: FRN, G10 · blade steel · plain or serrated edge"}],
 'Swiss Army knife': [{"n": "Victorinox Climber", "a": "", "d": "Mid-size Swiss Army knife with blade, scissors, corkscrew and other tools, named in the model history.", "mk": "Victorinox", "y": "", "s": SAK, "v": [], "dt": "frame 91 mm · tool count · handle colour"}],
 'Adjustable wrench': [{"n": "Crescent wrench", "a": "", "d": "Adjustable wrench with a movable jaw angled for tight spaces; the brand name became the common North American term.", "mk": "Crescent", "y": "", "s": WRENCH, "v": [], "dt": "length 4 to 18 in · finish"}],
 'Plough plane': [{"n": "Stanley No. 148 match plane", "a": "", "d": "Stanley's match plane for cutting matched tongue-and-groove boards.", "mk": "Stanley", "y": "", "s": HPLANE, "v": [], "dt": "cutter widths"}],
}
SEE = [
 ("Battery charger", "C8", "Battery charger", "household battery chargers"),
 ("Whetstone", "B5", "Whetstone", "kitchen whetstone"),
 ("Pocket knife sharpener", "B5", "Knife sharpener", "kitchen knife sharpeners"),
 ("Dust extractor", "B6", "Wet and dry vacuum cleaner", "household wet-and-dry vacuum"),
 ("Glue gun", "C4", "Hot-glue gun", "craft glue gun"),
 ("Utility knife", "C4", "Craft knife", "craft knife"),
 ("Fixed-blade EDC & bushcraft knife", "E4", "Hunting knife", "hunting knife"),
 ("Axe", "E2", "Ice axe", "climbing axe"),
 ("Gas torch", "C4", "Jewellery soldering torch", "jewellery torch"),
 ("Air compressor", "C4", "Airbrush compressor", "small airbrush compressor"),
 ("Submersible pump", "C2", "Garden water pump", "garden pump"),
 ("Bottle jack", "G1", "Trolley jack", "garage jacks"),
 ("Folding saw", "C2", "Pruning saw", "pruning saw"),
 ("Chainsaw trousers", "C2", "Chainsaw", "the saw they guard against"),
 ("Chainsaw chaps", "C2", "Chainsaw", "the saw they guard against"),
 ("Long nose pliers", "C4", "Jewellery pliers", "jewellery pliers"),
 ("Hacksaw", "C4", "Jeweller's saw", "fine jeweller's saw"),
 ("Ball-pein hammer", "C4", "Ring mandrel and jeweller's hammer", "jeweller's hammer"),
 ("Knee pads", "E2", "Knee pad", "sports knee pad"),
 ("Hard hat", "E2", "Climbing helmet" , "climbing helmet"),
 ("Router bit", "C1", "Router", "the tool it fits"),
 ("Drill bit", "C1", "Drill driver", "the tool it fits"),
]
KDEF = {  # definition rewrites
 "Bar clamp": "Clamp with a sliding jaw on a long bar, tightened by a screw or trigger to hold glued or fitted work.",
}

# parse tt
TT = {}
for line in open(W + '/tt.txt', encoding='utf-8'):
    line = line.rstrip('\n')
    if not line.strip(): continue
    parts = line.split('|')
    TT[parts[0]] = [[g.split(':', 1)[0], [x for x in g.split(':', 1)[1].split(';') if x]] for g in parts[1:]]

# index old kinds
OLD = {}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']:
            OLD[k['n']] = (dp['n'], k)

placed = set()
out = copy.deepcopy(old)
depts_old = {dp['n']: dp for dp in old['depts']}
new_depts = []
removed_arch = []
for dn in S.ORDER:
    t, ax, shelves = S.D[dn]
    od = depts_old[dn]
    nd = {k: v for k, v in od.items() if k not in ('s',)}
    nd['t'] = t; nd['ax'] = ax
    ns = []
    for (sn, st, sax, kinds) in shelves:
        shelf = {"n": sn, "t": st}
        if sax: shelf['ax'] = sax
        ks = []
        for kn in kinds:
            if kn in NEWD:
                k = copy.deepcopy(NEWD[kn])
            else:
                if kn not in OLD: raise SystemExit('missing kind ' + kn)
                k = copy.deepcopy(OLD[kn][1]); placed.add(kn)
            ks.append(k)
        shelf['k'] = ks
        ns.append(shelf)
    nd['s'] = ns
    new_depts.append(nd)
unplaced = [n for n in OLD if n not in placed]
if unplaced: raise SystemExit('unplaced old kinds: %s' % unplaced)

allk = {k['n']: k for d in new_depts for s in d['s'] for k in s['k']}
# archetype handling
for kn, names in DEMOTE.items():
    k = allk[kn]
    before = len(k.get('x', []))
    k['x'] = [x for x in k.get('x', []) if x['n'] not in names]
    removed_arch += [(kn, n) for n in names]
    assert before - len(k['x']) == len(names), (kn, names)
for (kn, an), (tk, rr) in TO_R.items():
    k = allk[kn]
    x = [a for a in k.get('x', []) if a['n'] == an]
    assert x, (kn, an)
    k['x'] = [a for a in k['x'] if a['n'] != an]
    r = allk[tk].setdefault('r', [])
    if rr not in r: r.append(rr)
for (kn, an), tk in MOVE_ARCH.items():
    k = allk[kn]
    x = [a for a in k['x'] if a['n'] == an]
    assert x
    k['x'] = [a for a in k['x'] if a['n'] != an]
    allk[tk].setdefault('x', []).extend(x)
for kn, xs in ADD_ARCH.items():
    allk[kn].setdefault('x', []).extend(xs)
# tt
missing_tt = []
for kn, k in allk.items():
    if kn in TT:
        k['tt'] = TT[kn]; k.pop('t', None)
    elif k.get('t'):
        missing_tt.append(kn)
    if kn in KDEF: k['d'] = KDEF[kn]
if missing_tt: print('OLD t WITHOUT tt:', missing_tt)
unused = [kn for kn in TT if kn not in allk]
if unused: print('tt for unknown kinds', unused)
# see
for (kn, c, tn, why) in SEE:
    if c == 'C1':
        assert tn in allk, tn
    else:
        rd = json.load(open('%s/reader/%s.json' % (R, c)))
        names = {k['n'] for dp in rd['depts'] for s in dp['s'] for k in s['k']}
        assert tn in names, (c, tn)
    allk[kn].setdefault('see', []).append([c, tn, why])
# drop empty x lists with no archetype (keep key tidy)
for k in allk.values():
    if 'x' in k and not k['x']: k['x'] = []
out['depts'] = new_depts
out['ax'] = S.CAT_AX
out['key'] = S.KEY
tmp = R + '/out/C1.json.tmp'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, R + '/out/C1.json')
json.dump({"removed_arch": removed_arch}, open(W + '/removed_arch.json', 'w'), ensure_ascii=False, indent=1)
print('built; kinds', len(allk), 'removed archetypes', len(removed_arch))
