"""Split the cross-category registers into per-category files so the page loads only what a category needs.
  python3 tools/registers.py     (build.py runs it) writes
    reader/brands/<C>.json      {"b": [brand entries whose cats include C]}
    reader/traditions/<C>.json  {"t": [tradition entries whose cats include C]}
    reader/species/<C>.json     {"i": [rare-species entries of C]}
    reader/_brand_index.json    {"b": [[name, seg, kf, [cats]]]}  (A-Z finder and maker links)
and returns per-category counts for build.py."""
import json, os, glob
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def dump(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p + '.tmp', 'w') as f: json.dump(obj, f, ensure_ascii=False, separators=(',', ':'))
    os.replace(p + '.tmp', p)


def split():
    load = lambda p, k: json.load(open(p))[k] if os.path.exists(p) else []
    B, T, P = load('reader/_brands.json', 'b'), load('reader/_traditions.json', 't'), load('reader/_species.json', 'i')
    counts = {}
    for kind, items, key in (('brands', B, 'b'), ('traditions', T, 't'), ('species', P, 'i')):
        by = {}
        for e in items:
            for c in (e.get('cats') or [e.get('c')]):
                if c: by.setdefault(c, []).append(e)
        for f in glob.glob(f'reader/{kind}/*.json'):
            if os.path.basename(f)[:-5] not in by: os.remove(f)
        for c, lst in by.items():
            dump(f'reader/{kind}/{c}.json', {key: lst}); counts.setdefault(c, {})[kind] = len(lst)
    dump('reader/_brand_index.json', {'b': [[b['n'], b.get('seg') or '', b.get('kf') or '', b.get('cats') or [], b.get('an') or ''] for b in B]})
    return counts


if __name__ == '__main__':
    c = split(); print('registers split for', len(c), 'categories')
