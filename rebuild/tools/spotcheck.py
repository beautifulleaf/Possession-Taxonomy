"""Post-batch spot check: python3 tools/spotcheck.py B5 B6 ...
- names from the FINDINGS row (capitalised terms) that do not appear anywhere in out/<CODE>*.json
- SKU dumps: kinds in tier departments with more than 12 flat models
- sources: every archetype/new-kind source in the retrieved log; live re-check of a random sample"""
import json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
os.chdir(os.path.dirname(HERE))
import netlib  # noqa
from run import findings_row, norm, retrieved_set  # noqa

STOP = {'Add', 'Variety', 'Mixed', 'Tier', 'Kind', 'NEW', 'Home', 'Fixtures', 'Built', 'Moves', 'Trade', 'Brands', 'Market',
        'Spare', 'Shoe', 'Sample', 'Scenes', 'Tools', 'Sports', 'Keep', 'One', 'Ranges', 'Classics', 'Baby', 'Parts'}


def terms(row):
    cells = row.split('|')
    txt = cells[4] if len(cells) > 4 else row
    out = []
    for t in re.findall(r"[A-Z][\w'’&.\-]+(?:\s+[A-Z0-9][\w'’&.\-]+)*", txt):
        t = t.strip(' .')
        if t.split()[0] in STOP or len(t) < 3: continue
        out.append(t)
    return list(dict.fromkeys(out))


def main(codes):
    ret = retrieved_set()
    for c in codes:
        blob = ''.join(open(f'out/{c}{s}.json').read() for s in ('', '_brands', '_traditions', '_moves') if os.path.exists(f'out/{c}{s}.json')).lower()
        d = json.load(open(f'out/{c}.json'))
        miss = [t for t in terms(findings_row(c)) if t.lower() not in blob]
        sku = [(k['n'], len(k.get('m') or [])) for dp in d['depts'] if dp['mode'] == 'tier' for s in dp['s'] for k in s['k'] if len(k.get('m') or []) > 12]
        srcs = [x['s'] for dp in d['depts'] for s in dp['s'] for k in s['k'] for x in k.get('x') or []]
        unlogged = [u for u in srcs if norm(u) not in ret]
        sample = random.sample(srcs, min(6, len(srcs)))
        live = []
        for u in sample:
            st, _ = netlib.get(u, tries=2, timeout=20, accept='text/html')
            live.append((st, u))
        print(f'== {c}: findings terms not found ({len(miss)}): {miss}')
        print(f'   tier SKU dumps (>12 models): {sku or "none"}')
        print(f'   archetype sources: {len(srcs)}, not in retrieved log: {len(unlogged)}')
        print('   live sample: ' + '; '.join(f'{st} {u}' for st, u in live))


if __name__ == '__main__':
    main(sys.argv[1:])
