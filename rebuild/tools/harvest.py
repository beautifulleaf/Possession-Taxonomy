"""Brand-led harvest (owner decision 2026-10-27): grow a category's brand register from outside databases and lists,
independent of models.

  python3 tools/harvest.py check CODE      validate work/_harvest/CODE.json, print errors and new/duplicate counts
  python3 tools/harvest.py apply CODE      add the new brands to out/CODE_brands.json (backup in bak/harvest/);
                                           then run merge.py (no args) and build.py
Input work/_harvest/CODE.json = {"b": [BRAND, ...]} with BRAND as in SCHEMA.md; "s" is a retrieved page that names the
brand (a list/index page counts) logged with `python3 tools/local.py logsrc CODE harvest fetched <url>`, or "knowledge"
for a well-known brand. "seg" from SEGMENTS.json, "kf" a 1-3 word known-for tag."""
import json, os, sys, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import run  # noqa: E402  (chdirs to rebuild/)
from run import retrieved_set, norm, ALL_SEGS


def load(c):
    p = f'work/_harvest/{c}.json'
    return json.load(open(p)).get('b', []) if os.path.exists(p) else []


def existing():
    reg = {}
    if os.path.exists('reader/_brands.json'):
        for b in json.load(open('reader/_brands.json'))['b']: reg[b['n'].strip().lower()] = b
    return reg


def check(c, quiet=False):
    got = retrieved_set(); reg = existing(); errs = []; new = []; dup = []; seen = set()
    for b in load(c):
        n = (b.get('n') or '').strip()
        if not n: errs.append('entry without name'); continue
        k = n.lower()
        if k in seen: errs.append(f'{n}: listed twice'); continue
        seen.add(k)
        if b.get('seg') not in ALL_SEGS: errs.append(f'{n}: seg {b.get("seg")!r} not in SEGMENTS.json')
        s = b.get('s') or ''
        if s != 'knowledge' and norm(s) not in got: errs.append(f'{n}: s must be a retrieved, logged page or "knowledge" (got {s!r})')
        (dup if k in reg else new).append(b)
    if not quiet:
        print(f'{c}: {len(new)} new, {len(dup)} already in register, {len(errs)} errors')
        for e in errs[:60]: print(' -', e)
    return errs, new, dup


def apply(c):
    errs, new, dup = check(c, quiet=True)
    bad = {e.split(':')[0].lower() for e in errs}
    add = [dict(b, s='' if b.get('s') == 'knowledge' else b['s']) for b in new if b['n'].strip().lower() not in bad]
    p = f'out/{c}_brands.json'
    cur = json.load(open(p)) if os.path.exists(p) else {'b': []}
    have = {b['n'].strip().lower() for b in cur['b']}
    # brands already in the register (from another category) gain this category via a stub that merge.py folds in
    stubs = [{'n': b['n'], 'seg': b.get('seg'), 'kf': b.get('kf', '')} for b in dup if b['n'].strip().lower() not in have]
    os.makedirs('bak/harvest', exist_ok=True)
    if os.path.exists(p): shutil.copy(p, f'bak/harvest/{c}_brands.json')
    cur['b'] += [b for b in add if b['n'].strip().lower() not in have] + stubs
    with open(p + '.tmp', 'w') as f: json.dump(cur, f, ensure_ascii=False)
    os.replace(p + '.tmp', p)
    print(f'{c}: added {len(add)} new brands, linked {len(stubs)} existing; skipped {len(bad)} with errors')


if __name__ == '__main__':
    {'check': check, 'apply': apply}[sys.argv[1]](sys.argv[2])
