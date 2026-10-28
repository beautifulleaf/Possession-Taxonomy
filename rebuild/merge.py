"""Merge rebuilt categories from out/ into reader/, build registers and Baby view.
Usage: python3 merge.py A5 [B1 ...]   (codes whose out/ files are final)"""
import json, os, sys, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))
done = json.load(open('done.json')) if os.path.exists('done.json') else []
covered = json.load(open('moves_covered.json')) if os.path.exists('moves_covered.json') else {}
# coordinator: where a moved kind lands when its suggested dept is not a department of the target ("Dept / Shelf"),
# or "-" to drop it (catch-alls and duplicates the target already covers)
place = json.load(open('moves_place.json')) if os.path.exists('moves_place.json') else {}
def put(t, m, key):
    dest = place.get(key)
    if dest == '-': print('dropped', key); return
    if dest:
        dn, sn = [x.strip() for x in dest.split(' / ')]
        dp = next((dp for dp in t['depts'] if dp['n'] == dn), None)
        sh = next((s for s in dp['s'] if s['n'] == sn), None) if dp else None
        if sh is not None: sh['k'].append(m['kind']); return
        print('WARN moves_place target missing:', key, '->', dest)
    dp = next((dp for dp in t['depts'] if dp['n'] == m.get('dept')), None)
    if dp is None:
        dp = {'n': m.get('dept') or 'Moved in', 'mode': 'mixed', 'b': [], 's': [{'n': m.get('dept') or 'Moved in', 'k': []}]}
        t['depts'].append(dp)
    stems = lambda t: {w[:5] for w in t.lower().replace(',', ' ').replace('&', ' ').split() if len(w) > 3}
    ks = stems(m['kind']['n'])
    sh = max(dp['s'], key=lambda s: len(ks & stems(s['n'])))  # best word match; ties keep the first shelf
    sh['k'].append(m['kind'])
for c in sys.argv[1:]:
    d = json.load(open(f'out/{c}.json'))
    # re-apply kinds moved IN from categories merged earlier (the rebuilt file would otherwise drop them);
    # a kind whose name the rebuilt category already has is taken as covered by it
    names = {k['n'].lower() for dp in d['depts'] for s in dp['s'] for k in s['k']}
    if os.path.exists(f'out/{c}_moves.json'):  # kinds this category itself sends onward are not taken back in
        names |= {m['kind']['n'].lower() for m in json.load(open(f'out/{c}_moves.json')).get('out', [])
                  if place.get(c + '>' + m['to'] + ':' + m['kind']['n']) != '-'}
    for src in done:
        sp = f'out/{src}_moves.json'
        if src == c or not os.path.exists(sp): continue
        for m in json.load(open(sp)).get('out', []):
            if m['to'] != c or m['kind']['n'].lower() in names: continue
            cov = covered.get(src + '>' + c + ':' + m['kind']['n'])  # coordinator: moved kind already covered under another name
            if cov and cov.startswith('='):  # coordinator rename on arrival (e.g. an 'Other …' catch-all)
                m = dict(m, kind=dict(m['kind'], n=cov[1:])); print('renamed', m['kind']['n'])
                cov = None
            if cov:
                k = next((k for dp in d['depts'] for s in dp['s'] for k in s['k'] if k['n'] == cov), None)
                if k is not None:
                    for f in ('m', 'r'):
                        k[f] = (k.get(f) or []) + [x for x in (m['kind'].get(f) or []) if x not in (k.get(f) or [])]
                    print('folded', src + '>' + c + ':' + m['kind']['n'], 'into', cov); continue
            put(d, m, src + '>' + c + ':' + m['kind']['n']); names.add(m['kind']['n'].lower())
            print('re-applied', src + '>' + c + ':' + m['kind']['n'])
    json.dump(d, open(f'reader/{c}.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    if c not in done: done.append(c)
    mp = f'out/{c}_moves.json'
    mv = json.load(open(mp)).get('out', []) if os.path.exists(mp) else []
    applied = json.load(open('moves_applied.json')) if os.path.exists('moves_applied.json') else []
    for m in mv:
        key = c + '>' + m['to'] + ':' + m['kind']['n']
        if key in applied: continue
        tp = f"reader/{m['to']}.json"
        if not os.path.exists(tp): print('no target', m['to']); continue
        t = json.load(open(tp))
        names = {k['n'].lower(): k for dp in t['depts'] for s in dp['s'] for k in s['k']}
        if m['kind']['n'].lower() in names:
            k = names[m['kind']['n'].lower()]
            for f in ('m', 'r', 'x'):
                if m['kind'].get(f): k[f] = (k.get(f) or []) + m['kind'][f]
        else:
            put(t, m, key)
        json.dump(t, open(tp, 'w'), ensure_ascii=False, separators=(',', ':'))
        applied.append(key); print('moved', key)
    json.dump(applied, open('moves_applied.json', 'w'))
json.dump(done, open('done.json', 'w'))
# registers from all done categories
B = {}; T = {}
# coordinator: same-name brands that are different companies get distinct names per category (work/_clash/map.tsv)
CLASH = {}
if os.path.exists('work/_clash/map.tsv'):
    for ln in open('work/_clash/map.tsv').read().splitlines()[1:]:
        f = ln.split('\t')
        if len(f) >= 5: CLASH[(f[0].strip().lower(), f[1].strip())] = f[2:5]
for c in done:
    for b in json.load(open(f'out/{c}_brands.json')).get('b', []) if os.path.exists(f'out/{c}_brands.json') else []:
        ov = CLASH.get((b['n'].strip().lower(), c))
        if ov:
            b = dict(b, seg=ov[1], kf=ov[2], **({'n': ov[0], 'an': b['n']} if ov[0] != b['n'] else {}))
        k = b['n'].lower()
        if k in B:
            o = B[k]
            for f in ('lines', 'eras', 'sig', 'sc', 'rel'):
                o[f] = list(dict.fromkeys((o.get(f) or []) + (b.get(f) or [])))
            for f in ('c', 'f', 'seg', 'd', 's'):
                if not o.get(f) and b.get(f): o[f] = b[f]
            if c not in o['cats']: o['cats'].append(c)
        else:
            B[k] = dict(b, cats=[c])
    for t in json.load(open(f'out/{c}_traditions.json')).get('t', []) if os.path.exists(f'out/{c}_traditions.json') else []:
        k = t['n'].lower()
        if k in T:
            if c not in T[k]['cats']: T[k]['cats'].append(c)
            T[k]['forms'] = list(dict.fromkeys((T[k].get('forms') or []) + (t.get('forms') or [])))
        else:
            T[k] = dict(t, cats=[c])
json.dump({'b': sorted(B.values(), key=lambda b: b['n'].lower())}, open('reader/_brands.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump({'t': sorted(T.values(), key=lambda t: (t.get('g', ''), t['n']))}, open('reader/_traditions.json', 'w'), ensure_ascii=False, separators=(',', ':'))
baby = []
for p in sorted(glob.glob('reader/[A-J]*.json')):
    d = json.load(open(p))
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if 'baby' in (k.get('tg') or []): baby.append([d['c'], k['n'], dp['n']])
json.dump({'i': baby}, open('reader/_baby.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print('done', done, 'brands', len(B), 'traditions', len(T), 'baby', len(baby))
