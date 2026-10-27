"""Controlled brand segments (SEGMENTS.json).

  python3 tools/segments.py dump        write work/_seg/<group>.todo.tsv (name, domain, current seg, desc, signature, cats)
  python3 tools/segments.py apply       read work/_seg/*.map.tsv (name<TAB>seg<TAB>kf) and rewrite seg/kf in
                                        out/<C>_brands.json (merged cats) and work/<C>/shelves/*.json (unmerged cats);
                                        backups in bak/seg/; then run merge.py (no args) and build.py
A brand's domain: fashion if any of its categories is fashion, else luxury if any is luxury, else general."""
import json, os, sys, glob, shutil, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import run  # noqa: E402  (chdirs to rebuild/)
from run import SEGMENTS, seg_domain

OUT = 'work/_seg'


def sources():
    """Yield (path, cat, brand-list getter) for every file that holds brand entries."""
    done = json.load(open('done.json'))
    for c in done:
        p = f'out/{c}_brands.json'
        if os.path.exists(p): yield p, c, 'b'
    for p in sorted(glob.glob('work/*/shelves/*.json')):
        c = p.split('/')[1]
        if c not in done: yield p, c, 'brands'


def domain_of(cats):
    ds = {seg_domain(c) for c in cats}
    return 'fashion' if 'fashion' in ds else 'luxury' if 'luxury' in ds else 'general'


def dump():
    os.makedirs(OUT, exist_ok=True)
    info = {}
    for p, c, key in sources():
        for b in json.load(open(p)).get(key) or []:
            if not isinstance(b, dict) or not b.get('n'): continue
            k = b['n'].strip()
            e = info.setdefault(k.lower(), {'n': k, 'cats': [], 'seg': set(), 'd': '', 'sig': []})
            if c not in e['cats']: e['cats'].append(c)
            if b.get('seg'): e['seg'].add(b['seg'])
            e['d'] = e['d'] or (b.get('d') or '')
            e['sig'] += [x for x in (b.get('sig') or []) + (b.get('lines') or []) if x not in e['sig']][:4]
    groups = collections.defaultdict(list)
    for e in info.values():
        dom = domain_of(e['cats'])
        g = dom if dom != 'general' else 'general_' + e['cats'][0][0]  # general split by domain letter
        groups[g].append((e['n'], dom, ' / '.join(sorted(e['seg'])), e['d'][:160], '; '.join(e['sig'][:4]), ' '.join(e['cats'])))
    for g, rows in sorted(groups.items()):
        with open(f'{OUT}/{g}.todo.tsv', 'w') as f:
            f.write('name\tdomain\tcurrent_seg\tdesc\tsignature\tcats\n')
            for r in sorted(rows): f.write('\t'.join(x.replace('\t', ' ').replace('\n', ' ') for x in r) + '\n')
        print(g, len(rows))


def apply():
    m = {}
    for p in sorted(glob.glob(f'{OUT}/*.map.tsv')):
        for line in open(p).read().splitlines()[1:]:
            parts = line.split('\t')
            if len(parts) >= 2 and parts[0].strip(): m[parts[0].strip().lower()] = (parts[1].strip(), parts[2].strip() if len(parts) > 2 else '')
    cats_of = collections.defaultdict(list)
    for p, c, key in sources():
        for b in json.load(open(p)).get(key) or []:
            if isinstance(b, dict) and b.get('n') and c not in cats_of[b['n'].strip().lower()]: cats_of[b['n'].strip().lower()].append(c)
    bad = [(n, s) for n, (s, _) in m.items() if s not in SEGMENTS[domain_of(cats_of.get(n) or ['?'])]['segs']]
    if bad: print('invalid segments (not applied):', bad[:30], len(bad))
    os.makedirs('bak/seg', exist_ok=True); changed = 0; missing = set()
    for p, c, key in sources():
        d = json.load(open(p)); hit = False
        for b in d.get(key) or []:
            if not isinstance(b, dict) or not b.get('n'): continue
            k = b['n'].strip().lower()
            if k not in m: missing.add(b['n']); continue
            s, kf = m[k]
            if s not in SEGMENTS[domain_of(cats_of[k])]['segs']: continue
            if b.get('seg') != s or (kf and b.get('kf') != kf):
                b['seg'] = s
                if kf: b['kf'] = kf
                hit = True; changed += 1
        if hit:
            shutil.copy(p, 'bak/seg/' + p.replace('/', '__'))
            with open(p + '.tmp', 'w') as f: json.dump(d, f, ensure_ascii=False, indent=1 if 'shelves' in p else None)
            os.replace(p + '.tmp', p)
    print('updated', changed, 'brand entries; unmapped', len(missing), sorted(missing)[:20])


if __name__ == '__main__':
    {'dump': dump, 'apply': apply}[sys.argv[1]]()
