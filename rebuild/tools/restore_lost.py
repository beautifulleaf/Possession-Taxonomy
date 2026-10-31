"""Restore concrete names the STR pass dropped. Compares each category's pre-pass backup (work/STR_<C>/bak/<C>.json)
with reader/<C>.json; every lost version, model or range, and every lost archetype that had a maker, is added back as a
model ["name","maker"] on the kind that now carries the old kind (same name, rename map, or alias). Maker-less lost
archetypes are generic patterns the pass demoted on purpose and are only listed. Writes reader/ and out/ alike and
work/_restore/<C>.tsv. Usage: python3 tools/restore_lost.py [--write] [CODES...]"""
import json, os, sys, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
W = '--write' in sys.argv; codes = [a for a in sys.argv[1:] if a != '--write']
os.makedirs('work/_restore', exist_ok=True)
low = lambda s: (s or '').strip().lower()
def kinds(d): return [k for dp in d['depts'] for s in dp['s'] for k in s['k']]
def names_in(k):
    out = {low(k['n'])}
    for x in k.get('x') or []:
        out.add(low(x['n'])); out |= {low(v['n']) for v in x.get('v') or []}
    out |= {low(m[0]) for m in (k.get('m') or []) + (k.get('r') or [])}
    for g in k.get('tt') or []: out |= {low(t) for t in g[1]}
    out |= {low(t) for t in k.get('t') or []}
    out |= {low(a) for a in (k.get('a') or '').split(' · ')}
    return out
grand = [0, 0, 0]
for bp in sorted(glob.glob('work/STR_*/bak/*.json')):
    c = bp.split('/')[1][4:]
    if os.path.basename(bp) != f'{c}.json' or (codes and c not in codes) or not os.path.exists(f'reader/{c}.json'): continue
    old = json.load(open(bp)); new = json.load(open(f'reader/{c}.json'))
    ren = json.load(open(f'out/{c}_renames.json')) if os.path.exists(f'out/{c}_renames.json') else {}
    present = set().union(*(names_in(k) for k in kinds(new)))
    byname = {low(k['n']): k for k in kinds(new)}
    byalias = {low(a): k for k in kinds(new) for a in (k.get('a') or '').split(' · ') if a}
    adds = {}; rows = []; generic = 0
    for k in kinds(old):
        tgt = byname.get(low(k['n'])) or byname.get(low(ren.get(k['n']))) or byalias.get(low(k['n']))
        cand = []
        for x in k.get('x') or []:
            mk = x.get('mk') or ''
            if low(x['n']) not in present:
                if mk: cand.append((x['n'], mk))
                else: generic += 1
            cand += [(v['n'], v.get('mk') or mk) for v in x.get('v') or [] if low(v['n']) not in present]
        cand += [(m[0], m[1] if len(m) > 1 else '') for m in (k.get('m') or []) + (k.get('r') or []) if low(m[0]) not in present]
        for n, mk in cand:
            if low(n) in present: continue
            present.add(low(n))
            if tgt is None: rows.append(f'{k["n"]}\t{n}\t{mk}\tUNPLACED'); continue
            adds.setdefault(tgt['n'], []).append([n, mk]); rows.append(f'{k["n"]}\t{n}\t{mk}\t-> {tgt["n"]}')
    restored = sum(len(v) for v in adds.values()); unplaced = sum(1 for r in rows if r.endswith('UNPLACED'))
    grand[0] += restored; grand[1] += unplaced; grand[2] += generic
    open(f'work/_restore/{c}.tsv', 'w').write('old kind\tname\tmaker\tplaced\n' + '\n'.join(rows) + '\n')
    if W and adds:
        for p in (f'reader/{c}.json', f'out/{c}.json'):
            d = json.load(open(p))
            for k in kinds(d):
                if k['n'] in adds:
                    have = {low(m[0]) for m in k.get('m') or []}
                    k['m'] = (k.get('m') or []) + [m for m in adds[k['n']] if low(m[0]) not in have]
            json.dump(d, open(p + '.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(p + '.tmp', p)
    if restored or unplaced: print(f'{c}: restored {restored}, unplaced {unplaced}, generic left out {generic}')
print('total restored', grand[0], 'unplaced', grand[1], 'generic left out', grand[2], '(written)' if W else '(dry run)')
