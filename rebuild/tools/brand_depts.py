"""File every brand of a category under a department (and, where possible, a kind) of that category's tree,
by script, no model tokens (owner, 2026-11-01). Order of evidence:
  1 named: the brand is a named entry, maker (mk) or model of a kind  -> that kind
  2 kf: the brand's own known-for text equals a kind name, alias or type value  -> that kind
  3 words: best word overlap between known-for (+ note) and a kind's vocabulary, if clear  -> that kind
Leftovers are written for a bulk pass. Output: work/BRAND_DEPTS/<C>.json {brand: [dept, kind, method]},
work/BRAND_DEPTS/_leftover.tsv, _summary.tsv. registers.py overlays dept/kind into the per-category view.
Usage: python3 tools/brand_depts.py [C ...]"""
import json, os, re, sys, glob, unicodedata, collections
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); W = f'{R}/work/BRAND_DEPTS'; os.makedirs(W, exist_ok=True)
STOP = set('and the of for with from a an in on by to or its it is as at maker makers brand brands company named owner known range ranges line lines products product sold sells uk us de la le'.split())
def norm(s): return re.sub(r'[^a-z0-9 ]', ' ', unicodedata.normalize('NFKD', (s or '').lower()).encode('ascii', 'ignore').decode())
def stem(w): return re.sub(r'(ies)$', 'y', re.sub(r'(?<=[a-z]{3})(es|s)$', '', w))
def words(s): return {stem(w) for w in norm(s).split() if len(w) > 2 and w not in STOP}
def key(s): return ' '.join(stem(w) for w in norm(s).split())
cats = sys.argv[1:] or sorted(c for c in (os.path.basename(p)[:-12] for p in glob.glob(f'{R}/out/*_brands.json') if re.match(r'^[A-J]\d+$', os.path.basename(p)[:-12])) if c != 'A1')  # A1 keeps its market-segment register
summ, left = [], []
BULK = {}  # bulk-pass answers for script leftovers: verify/work/BRANDSORT/out<N>.tsv  (CAT, brand, department number)
for p in glob.glob(f'{R}/../verify/work/BRANDSORT/out*.tsv'):
    for l in open(p).read().splitlines():
        f = l.split('\t')
        if len(f) == 3 and f[2].strip().isdigit(): BULK[(f[0], f[1])] = int(f[2])
# the answers are numbers in the department list given to the sorter (batch<N>.tsv): turn them into names, so a
# later restructure (J7 wine merged 2026-11-01) can map old department names onto new ones
NUMS = {}
for p in glob.glob(f'{R}/../verify/work/BRANDSORT/batch*.tsv'):
    for l in open(p).read().splitlines():
        m = re.match(r'^## (\S+)\s+departments: (.*)$', l)
        if m: NUMS[m.group(1)] = {int(a): b for a, b in (x.split('=', 1) for x in m.group(2).split(' | '))}
BULK = {k: NUMS.get(k[0], {}).get(v, '') for k, v in BULK.items() if v}
RENAMED = {**{n: 'Wine' for n in ('Wine of France', 'Wine of Italy', 'Wine of Spain & Portugal', 'Wine of Germany, Austria & Switzerland',
    'Wine of Hungary & Central Europe', 'Wine of the Balkans', 'Wine of Eastern Europe', 'Wine of Greece & Cyprus',
    'Wine of Turkey, the Caucasus & the Levant', 'Wine of the United States', 'Wine of Canada & Mexico', 'Wine of South America',
    'Wine of South Africa', 'Wine of Australia & New Zealand', 'Wine of England & Wales', 'Wine of China, Japan & India',
    'Wine styles across countries')}, 'No & low alcohol': 'Beer'}
DR = json.load(open(f'{W}/../DEPT_RENAMES.json')) if os.path.exists(f'{W}/../DEPT_RENAMES.json') else {}  # tools/merge_depts.py
for c in cats:
    tree = json.load(open(f'{R}/out/{c}.json')); B = json.load(open(f'{R}/out/{c}_brands.json'))['b']
    named, exact, vocab = {}, {}, []
    for d in tree['depts']:
        for s in d['s']:
            for k in s['k']:
                kd = (d['n'], k['n'])
                for x in k.get('x', []):
                    for n in [x.get('n'), x.get('mk')] + [v.get('mk') for v in x.get('v', []) if isinstance(v, dict)]:
                        if n: named.setdefault(key(n), kd)
                for m in k.get('m', []):
                    if isinstance(m, list) and len(m) > 1 and isinstance(m[1], str): named.setdefault(key(m[1]), kd)
                al = [a for a in re.split(r'[·,;]', k.get('a') or '') if a.strip()]; ty = [t for _, ts in k.get('tt', []) for t in ts] + list(k.get('t') or [])
                terms = [k['n']] + al + ty
                for pr, ts in ((0, [k['n']]), (1, al), (2, ty)):
                    for t in ts: exact.setdefault(key(t), []).append((pr, kd))
                vocab.append((kd, words(' '.join(terms + [s['n'], d['n']])), words(k['n'])))
    def pick(t):  # best-priority kinds for a term; several kinds in one department give the department only
        hs = exact.get(key(t))
        if not hs: return None
        best = min(p for p, _ in hs); ks = {kd for p, kd in hs if p == best}
        if len(ks) == 1: return next(iter(ks))
        ds = {d for d, _ in ks}
        return (next(iter(ds)), '') if len(ds) == 1 and best < 2 else None
    out, cnt = {}, collections.Counter()
    for b in B:
        n, kf, note = b['n'], b.get('kf') or '', b.get('d') or ''
        hit = named.get(key(n)); how = 'named'
        if not hit and kf:
            hit = pick(kf); how = 'kf'
            if not hit:  # kf may list several things: "tiles/sanitaryware", "paint / limewash"
                for part in re.split(r'[/,;·]| and ', kf):
                    hit = pick(part.strip())
                    if hit: break
        if not hit:
            ws = words(kf) or set(); ws2 = ws | words(note)
            if ws2:
                sc = sorted(((len(ws & v) * 3 + len(ws & kn) * 2 + len((ws2 - ws) & v), kd) for kd, v, kn in vocab), reverse=True)
                if sc and sc[0][0] >= 3 and (len(sc) == 1 or sc[0][0] > sc[1][0] or sc[0][1][0] == sc[1][1][0]):
                    hit = sc[0][1] if sc[0][0] > (sc[1][0] if len(sc) > 1 else 0) else (sc[0][1][0], '')
                    how = 'words'
        if hit and how == 'words': hit = (hit[0], '')  # word overlap is reliable for the department, not the kind
        if not hit and (c, n) in BULK:
            dn = RENAMED.get(BULK[(c, n)], BULK[(c, n)]); dn = DR.get(c, {}).get(dn, dn)
            if dn in {x['n'] for x in tree['depts']}: hit = (dn, ''); how = 'bulk'
        if hit: out[n] = [hit[0], hit[1], how]; cnt[how] += 1
        else: left.append(f'{c}\t{n}\t{kf[:50]}\t{note[:80]}'); cnt['left'] += 1
    json.dump(out, open(f'{W}/{c}.json', 'w'), ensure_ascii=False, indent=0)
    summ.append(f"{c}\t{len(B)}\t{cnt['named']}\t{cnt['kf']}\t{cnt['words'] + cnt['bulk']}\t{cnt['left']}")
open(f'{W}/_leftover.tsv', 'w').write('cat\tname\tkf\tnote\n' + '\n'.join(left) + '\n')
open(f'{W}/_summary.tsv', 'w').write('cat\tbrands\tnamed\tkf\twords\tleft\n' + '\n'.join(summ) + '\n')
t = [sum(int(r.split('\t')[i]) for r in summ) for i in range(1, 6)]
print('brands', t[0], 'named', t[1], 'kf', t[2], 'words', t[3], 'left', t[4])
