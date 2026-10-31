"""Coordinator pass after STR: rename same-name kinds that are different objects (old name kept as an alias),
and cross-link same-name kinds that are the same object in two categories. Edits reader/ and out/ alike;
renames are appended to out/<CODE>_renames.json."""
import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
RENAME = [('C1', 'Tongs', "Blacksmith's tongs"), ('C4', 'Squeegee', 'Screen-printing squeegee'),
          ('F3', 'Storage box', 'Collector storage box'), ('J4', 'Drumstick', 'Drumstick (moringa pod)'),
          ('A3', 'Nipple shield', 'Nipple shield jewellery'), ('D4', 'Changing bag', 'Film changing bag')]
LINK = [('E4', 'Sgian-dubh', 'A1', 'Sgian-dubh', 'worn with Highland dress'),
        ('E4', 'Release aid', 'E2', 'Release aid', 'archery accessory listed with archery'),
        ('C2', 'Trellis', 'C8', 'Trellis', 'also sold as timber with fencing'),
        ('B3', 'Dive light', 'E2', 'Dive light', 'also listed with diving kit')]
def load(c): return {p: json.load(open(p)) for p in (f'reader/{c}.json', f'out/{c}.json')}
def save(fs):
    for p, d in fs.items(): json.dump(d, open(p + '.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(p + '.tmp', p)
def kinds(d): return [k for dp in d['depts'] for s in dp['s'] for k in s['k']]
for c, old, new in RENAME:
    fs = load(c)
    for d in fs.values():
        for k in kinds(d):
            if k['n'] == old:
                k['n'] = new; k['a'] = ' · '.join(x for x in [old] + [a for a in (k.get('a') or '').split(' · ') if a] if x)
    save(fs)
    rp = f'out/{c}_renames.json'; r = json.load(open(rp)) if os.path.exists(rp) else {}
    r[old] = new; json.dump(r, open(rp, 'w'), ensure_ascii=False, indent=1); print('renamed', c, old, '->', new)
for a, an, b, bn, why in LINK:
    for (c, n, tc, tn) in ((a, an, b, bn), (b, bn, a, an)):
        fs = load(c)
        for d in fs.values():
            for k in kinds(d):
                if k['n'] == n and not any(sv[0] == tc and sv[1] == tn for sv in k.get('see') or []):
                    k.setdefault('see', []).append([tc, tn, why])
        save(fs)
    print('linked', a, an, '<->', b, bn)
