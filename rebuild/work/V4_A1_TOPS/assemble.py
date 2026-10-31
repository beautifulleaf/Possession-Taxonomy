import sys, json, copy, re, os
sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/V4_A1_TOPS')
import build_part as B
ROOT = B.ROOT
seg_new = {}
out_depts = []
used = set()
brands_in_entries = {}
for dp in B.OLD['depts']:
    if dp['n'] not in B.DEPTS:
        continue
    nd = {k: v for k, v in dp.items() if k != 's'}
    nd['s'] = []
    for sh in dp['s']:
        ns = {k: v for k, v in sh.items() if k != 'k'}
        ns['k'] = []
        for k in sh['k']:
            spec = B.KINDS[k['n']]
            used.add(k['n'])
            nk = {kk: vv for kk, vv in k.items() if kk not in ('x', 'm', 'r')}
            ents = [B.finish(copy.deepcopy(e), k['n']) for e in spec['entries']]
            ents.sort(key=B.sortkey)
            names = [e['n'] for e in ents]
            assert len(names) == len(set(names)), (k['n'], names)
            for e in ents:
                brands_in_entries.setdefault(e.get('mk', ''), e)
            nk['nl'] = spec['nl']
            n = len(ents)
            if n:
                nk['x'] = ents
                nk['xg'] = spec['xg']
                nk['sel'] = (f"Canon: every signature piece in the brand register that matches this garment, confirmed on its register page, and every originator named in {spec['ref']}. "
                             f"Complete: {n} of {n} in the brand register and the fetched Wikipedia articles.")
            else:
                nk['sel'] = (f"Canon: {spec['ref']}. Complete: 0 of 0, so the kind has no named entries; the garment is described by its attributes.")
            ns['k'].append(nk)
        nd['s'].append(ns)
    out_depts.append(nd)
assert used == set(B.KINDS), set(B.KINDS) - used
# brands
new_brands = []
upd = {}
for mk, e in brands_in_entries.items():
    if not mk:
        continue
    if mk in B.REG:
        if mk in B.OWN or B.cty(mk):
            u = {'c': B.REG[mk].get('c','')}
            if mk in B.OWN:
                u['own'] = B.OWN[mk][0]
                if B.OWN[mk][1]:
                    u['own_y'] = B.OWN[mk][1]
            upd[mk] = u
    else:
        new_brands.append(mk)
json.dump({'new': new_brands}, open(ROOT + 'rebuild/work/V4_A1_TOPS/newbrands.json', 'w'), ensure_ascii=False, indent=0)
part = {'replaces': B.DEPTS, 'depts': out_depts, 'brands': [], 'brand_updates': upd, 'renames': {}, 'moves': []}
json.dump(part, open(ROOT + 'rebuild/work/V4_A1_TOPS/part_draft.json', 'w'), ensure_ascii=False)
print(len(new_brands), new_brands)
print(sum(len(k.get('x', [])) for d in out_depts for s in d['s'] for k in s['k']), 'entries')
