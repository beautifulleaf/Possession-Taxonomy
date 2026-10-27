"""Merge rebuilt categories from out/ into reader/, build registers and Baby view.
Usage: python3 merge.py A5 [B1 ...]   (codes whose out/ files are final)"""
import json, os, sys, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))
done = json.load(open('done.json')) if os.path.exists('done.json') else []
covered = json.load(open('moves_covered.json')) if os.path.exists('moves_covered.json') else {}
for c in sys.argv[1:]:
    d = json.load(open(f'out/{c}.json'))
    # re-apply kinds moved IN from categories merged earlier (the rebuilt file would otherwise drop them);
    # a kind whose name the rebuilt category already has is taken as covered by it
    names = {k['n'].lower() for dp in d['depts'] for s in dp['s'] for k in s['k']}
    if os.path.exists(f'out/{c}_moves.json'):  # kinds this category itself sends onward are not taken back in
        names |= {m['kind']['n'].lower() for m in json.load(open(f'out/{c}_moves.json')).get('out', [])}
    for src in done:
        sp = f'out/{src}_moves.json'
        if src == c or not os.path.exists(sp): continue
        for m in json.load(open(sp)).get('out', []):
            if m['to'] != c or m['kind']['n'].lower() in names: continue
            cov = covered.get(src + '>' + c + ':' + m['kind']['n'])  # coordinator: moved kind already covered under another name
            if cov:
                k = next((k for dp in d['depts'] for s in dp['s'] for k in s['k'] if k['n'] == cov), None)
                if k is not None:
                    for f in ('m', 'r'):
                        k[f] = (k.get(f) or []) + [x for x in (m['kind'].get(f) or []) if x not in (k.get(f) or [])]
                    print('folded', src + '>' + c + ':' + m['kind']['n'], 'into', cov); continue
            dp = next((dp for dp in d['depts'] if dp['n'] == m.get('dept')), None)
            if dp is None:
                dp = {'n': m.get('dept') or 'Moved in', 'mode': 'mixed', 'b': [], 's': [{'n': m.get('dept') or 'Moved in', 'k': []}]}
                d['depts'].append(dp)
            dp['s'][0]['k'].append(m['kind']); names.add(m['kind']['n'].lower())
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
            dp = next((dp for dp in t['depts'] if dp['n'] == m.get('dept')), None)
            if dp is None:
                dp = {'n': m.get('dept') or 'Moved in', 'mode': 'mixed', 'b': [], 's': [{'n': m.get('dept') or 'Moved in', 'k': []}]}
                t['depts'].append(dp)
            dp['s'][0]['k'].append(m['kind'])
        json.dump(t, open(tp, 'w'), ensure_ascii=False, separators=(',', ':'))
        applied.append(key); print('moved', key)
    json.dump(applied, open('moves_applied.json', 'w'))
json.dump(done, open('done.json', 'w'))
# registers from all done categories
B = {}; T = {}
for c in done:
    for b in json.load(open(f'out/{c}_brands.json')).get('b', []) if os.path.exists(f'out/{c}_brands.json') else []:
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
