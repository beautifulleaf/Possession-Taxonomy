import json, os, sys, copy, shutil, re
sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/STR_C4')
from c4struct import *   # noqa
R = '/home/user/Possession-Taxonomy/rebuild/'
SRC = R + 'work/STR_C4/bak/C4.json'   # always rebuild from the backup
d = json.load(open(SRC))

# index original kinds
kinds = {}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            kinds[k['n']] = k
orig_dept = {dp['n']: dp for dp in d['depts']}
orig_count = dict(depts=len(d['depts']), shelves=sum(len(dp['s']) for dp in d['depts']),
                  kinds=len(kinds), arch=sum(len(k.get('x', [])) for k in kinds.values()))

# ---- tt parsing
tt = {}
for fn in ('tt1.txt', 'tt2.txt', 'tt3.txt'):
    for line in open(R + 'work/STR_C4/' + fn, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip():
            continue
        name, rest = line.split(' || ', 1)
        groups = []
        for g in rest.split(' ;; '):
            lab, items = g.split(': ', 1)
            groups.append([lab.strip(), [i.strip() for i in items.split(' | ') if i.strip()]])
        assert name not in tt, name
        tt[name] = groups

# ---- merge Sock yarn into Wool yarn (carry archetypes, models, ranges)
sock = kinds['Sock yarn']
wool = kinds['Wool yarn']
for key in ('x', 'm', 'r'):
    wool.setdefault(key, [])
    for it in sock.get(key, []):
        if it not in wool[key]:
            wool[key].append(it)
wool['d'] = "Spun wool yarn sold in balls or skeins for knitting and crochet, graded by Craft Yarn Council weight 0 to 6, including wool-nylon sock yarn."
wool['a'] = (wool.get('a', '') + ' · sock yarn').strip(' ·')
del kinds['Sock yarn']

# ---- build final kind objects
final = {}      # final name -> kind dict
src_of = {}     # old name -> final name (for renames file)
renames = {}
inv_rename = {v: k for k, v in RENAME.items() if k != v and k not in MERGED}
for old, k in kinds.items():
    new = RENAME.get(old, old)
    kk = copy.deepcopy(k)
    kk['n'] = new
    final[new] = kk
    if new != old:
        renames[old] = new
renames['Sock yarn'] = 'Wool yarn'

D_OVER = {
 "Relief printing block": "Lino, wood or soft-cut block carved so that the raised surface prints.",
 "Braid, fringe and rickrack": "Braid, soutache, fringe, rickrack or pom-pom edging sold by the metre for sewing on.",
 "Embroidery hoop and frame": "Hoop or frame that holds cloth taut for hand stitching.",
 "Bookbinding needle, awl and thread": "Needle, awl and waxed thread for sewing the pages of a book by hand, with the case and Coptic binding structures.",
 "Head pin and eye pin": "Wire pin with a head or a loop that carries a single bead.",
 "Bail": "Finding that hangs a pendant from a chain or cord.",
 "Stitching pony": "Clamp that holds leather upright for hand stitching.",
}
for n, t in D_OVER.items():
    final[n]['d'] = t
final['Lampwork bead']['d'] = final['Lampwork bead']['d']

# new kinds
for n, spec in NEW.items():
    if n in final:
        raise SystemExit('new kind exists: ' + n)
    s = spec.get('s')
    if s is None:
        s = kinds[spec['borrow']]['s']
    k = {'n': n, 'a': spec.get('a', ''), 'd': spec['d'], 's': s}
    if spec.get('x'):
        k['x'] = spec['x']
    final[n] = k

# ---- archetype handling
def find_x(kind, name, mk=None):
    for i, x in enumerate(final[kind].get('x', [])):
        if x['n'] == name and (mk is None or x.get('mk') == mk):
            return i
    raise SystemExit(f'archetype {name!r} not in {kind}')

for kind, names in DROP_TO_TYPE.items():
    for nm in names:
        i = find_x(kind, nm)
        final[kind]['x'].pop(i)
for kind, names in TO_RANGE.items():
    for nm in names:
        i = find_x(kind, nm)
        x = final[kind]['x'].pop(i)
        r = final[kind].setdefault('r', [])
        ent = [nm, x.get('mk', '') or '']
        if ent not in r:
            r.append(ent)
for (frm, nm, to) in MOVE_X:
    if frm == 'Sock yarn':
        continue   # already merged
    i = find_x(frm, nm)
    x = final[frm]['x'].pop(i)
    final[to].setdefault('x', []).append(x)
for kind, lst in ADD_X.items():
    final[kind].setdefault('x', []).extend(lst)
# renames of archetypes
xren = {}
for k in final.values():
    for x in k.get('x', []):
        key = (x['n'], x.get('mk', ''))
        if key in X_RENAME_BY_MK:
            xren[x['n']] = X_RENAME_BY_MK[key]
            x['n'] = X_RENAME_BY_MK[key]
        elif x['n'] in X_RENAME and X_RENAME[x['n']] != x['n']:
            xren[x['n']] = X_RENAME[x['n']]
            x['n'] = X_RENAME[x['n']]
# drop empty x and the old 't'
for k in final.values():
    if not k.get('x'):
        k.pop('x', None)
    if not k.get('r'):
        k.pop('r', None)

# tt
placed = set()
missing = []
for n, k in final.items():
    if n not in tt:
        missing.append(n)
        continue
    k['tt'] = tt[n]
    k.pop('t', None)
if missing:
    raise SystemExit('no tt for: ' + '; '.join(missing))
extra = [n for n in tt if n not in final]
if extra:
    raise SystemExit('tt for unknown kinds: ' + '; '.join(extra))

# see links
SEE = {
 "Gouache": [["F2", "Gouache", "the same paint, listed for finished paintings"]],
 "Inkstone": [["C5", "Inkstone", "also listed with calligraphy and fountain-pen goods"]],
 "Sewing pattern": [["I2", "Sewing pattern", "the pattern as a design file"]],
 "Rotary cutter": [["C7", "Rotary cutter", "a tractor-mounted mower of the same name is a different tool"]],
 "Fuse bead": [["E1", "Fuse beads", "the toy-shop version sold as a kit"]],
 "Watercolour paint": [["C4", "Gansai and East Asian watercolour", "Japanese solid watercolour"]],
 "Gansai and East Asian watercolour": [["C4", "Watercolour paint", "Western tube and pan watercolour"]],
 "Soft pastels": [["C4", "Oil pastels", "oil-bound instead of dry"]],
 "Oil pastels": [["C4", "Soft pastels", "dry pigment sticks"]],
 "Crayon": [["C4", "Drawing chalk and sanguine", "chalk sticks for drawing"]],
 "Drawing chalk and sanguine": [["C4", "Crayon", "Conté and wax crayons"]],
 "Acrylic paint": [["C4", "Acrylic model paint", "the same binder made for models"]],
 "Acrylic model paint": [["C4", "Acrylic paint", "picture paint with the same binder"]],
 "Printing ink": [["C4", "Drawing ink", "ink for pen and brush"]],
 "Easel": [["C4", "Pochade box", "outdoor box with its own panel holder"]],
 "Pochade box": [["C4", "Easel", "stand-alone canvas support"]],
 "Embroidery machine": [["C4", "Sewing machine", "stitches seams rather than designs"]],
 "Sewing machine": [["C4", "Embroidery machine", "stitches designs from a hoop"]],
 "Pottery kiln": [["C4", "Glass-fusing kiln", "fires glass instead of clay"]],
 "Glass-fusing kiln": [["C4", "Pottery kiln", "fires clay instead of glass"]],
 "Lampwork bead": [["C4", "Lampworking torch", "the tool that makes it"]],
 "Lampworking torch": [["C4", "Lampwork bead", "what it makes"]],
 "Seed bead": [["C4", "Bead loom", "seed beads are woven on it"]],
 "Bead loom": [["C4", "Seed bead", "the bead it is made for"]],
 "Knitting needles": [["C4", "Knitting loom", "peg frame instead of needles"]],
 "Knitting loom": [["C4", "Knitting needles", "needles instead of a peg frame"]],
 "Craft cutting machine": [["C4", "Craft vinyl", "the film it cuts"]],
 "Craft vinyl": [["C4", "Craft cutting machine", "the machine that cuts it"]],
 "Washi paper": [["C4", "Washi tape", "tape made in washi style"]],
 "Washi tape": [["C4", "Washi paper", "handmade paper for brush work and printing"]],
 "Polymer clay": [["C4", "Air-dry clay", "hardens without an oven"]],
 "Air-dry clay": [["C4", "Polymer clay", "needs baking, not air"]],
 "Metal clay": [["C4", "Polymer clay", "baked, not fired to metal"]],
 "Craft glue": [["C4", "Model cement", "made for plastic kits"]],
 "Model cement": [["C4", "Craft glue", "general craft glue"]],
 "Hot-glue gun": [["C4", "Craft glue", "liquid glue instead of hot-melt"]],
 "Craft knife": [["C4", "Leather knife", "made for leather"]],
 "Leather knife": [["C4", "Craft knife", "general craft blade"]],
 "Airbrush": [["C4", "Airbrush compressor", "the air supply that drives it"]],
}
for n, lst in SEE.items():
    assert n in final, n
    for t in lst:
        if t[0] == 'C4':
            assert t[1] in final, t
    final[n]['see'] = lst

# ---- dept/shelf assembly
used = set()
newdepts = []
for ds in DEPTS:
    old = orig_dept[ds['n']]
    nd = {k: v for k, v in old.items() if k not in ('s',)}
    nd['t'] = ds['t']
    nd['ax'] = ds['ax']
    shelves = []
    for (sn, st, sax, names) in ds['shelves']:
        sh = {'n': sn, 't': st}
        if sax:
            sh['ax'] = sax
        ks = []
        for nm in names:
            if nm not in final:
                raise SystemExit('unknown kind on shelf: ' + nm)
            if nm in used:
                raise SystemExit('kind placed twice: ' + nm)
            used.add(nm)
            ks.append(final[nm])
        sh['k'] = ks
        shelves.append(sh)
    nd['s'] = shelves
    newdepts.append(nd)
unplaced = [n for n in final if n not in used]
if unplaced:
    raise SystemExit('unplaced kinds: ' + '; '.join(unplaced))

# dept notes: refresh to describe organisation
NOTES = {
 "Paints, brushes, paper & drawing media": "Art-shop goods by job in making a picture. Paint is ordered by medium, then house and line; Colour Index pigment codes are the comparison axis.",
 "Printing supplies & East Asian ink goods": "Printmaking supplies are grouped by process; the Four Treasures goods of East Asian brush and ink work have their own shelves.",
 "Fabric, thread & sewing machines": "Machines are tier picks with collectable vintage versions; cloth is organised by fibre and design house; notions are sold loose.",
}
for nd in newdepts:
    if nd['n'] in NOTES:
        nd['note'] = NOTES[nd['n']]

out = {'c': d['c'], 'rev': d.get('rev', True), 'lead': d['lead'], 'ax': CAT_AX, 'key': KEY,
       'b': d['b'], 'depts': newdepts}
nk = len(final)
na = sum(len(k.get('x', [])) for k in final.values())
stats = dict(before=orig_count, after=dict(depts=len(newdepts), shelves=sum(len(x['s']) for x in newdepts), kinds=nk, arch=na),
             new=sorted(NEW), renames=renames, xren=xren)
json.dump(stats, open(R + 'work/STR_C4/stats.json', 'w'), indent=1, ensure_ascii=False)
tmp = R + 'out/C4.json.tmp'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, R + 'out/C4.json')
# renames file
rn = R + 'out/C4_renames.json'
json.dump(renames, open(rn + '.tmp', 'w'), ensure_ascii=False, indent=1)
os.replace(rn + '.tmp', rn)
print(json.dumps(stats['before']), json.dumps(stats['after']))
