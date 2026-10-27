"""Build work/_harvest/lists/decisions.tsv from dec_*.txt plus automatic register/list matching."""
import sys, os, json, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
SEGS = json.load(open(R + 'SEGMENTS.json'))['domains']
dom = {c: d for d, v in SEGS.items() for c in v['cats'] if c != '*'}
AB = {'fashion': dict(LH='Luxury house', D='Designer', CP='Contemporary & premium', HW='Heritage & workwear', JD='Japanese & denim',
                      SW='Streetwear', OT='Outdoor & technical', AS='Athletic & sportswear', HS='High street', VB='Value & basics',
                      BA='Bespoke & artisan', TN='Traditional & national dress', SA='Subculture & alternative'),
      'luxury': dict(LH='Luxury house', HM='Haute maison', IM='Independent maker', D='Designer', P='Premium', M='Mainstream', V='Value',
                     BA='Bespoke & artisan', TR='Traditional & regional'),
      'general': dict(PF='Professional & flagship', P='Premium', M='Mainstream', V='Value', HMF='Heritage manufactory',
                      AI='Artisan & independent', SP='Specialist', OL='Own-label & retailer', II='Institution & issuer')}
RS = {'dup': None, 'sub': 'sub-line', 'unk': 'unidentified', 'retail': 'retail own-label', 'homeware': 'homeware',
      'merch': 'merch', 'eyewear line': 'eyewear line', 'out of scope': 'out of scope', 'single retailer': 'single retailer'}
W = os.path.dirname(os.path.abspath(__file__)) + '/'
dec = {}; errs = []
for p in sorted(glob.glob(W + 'dec_*.txt')):
    for line in open(p):
        if not line.strip(): continue
        f = line.rstrip('\n').split('|')
        k = (f[0], f[1])
        if k in dec: errs.append(f'decision twice {k}')
        dec[k] = f[2:]
reg, harv = register()
pre = {(l, nk(n)): h for l, n, h in json.load(open(W + 'pre.json'))}
FDK = {nk(r[0]): r for r in FD}
FMAP = {'dup': 'already in register', 'typo': 'already in register', 'sub': 'sub-line', 'merch': 'merch', 'unk': 'unidentified',
        'retail': 'retail own-label', 'scope': 'duplicate in lists'}
CORE = set(MAIN)
rows = []; used = set(); added = {}; dmeta = {}
def regreason(t):
    k = nk(t)
    return 'already in register' if k in reg else 'already harvested'
for l, n in items():
    key = (l, n); d = dec.get(key)
    if d is not None: used.add(key)
    row = None
    if d is None:
        if l in NN:
            o = on(n); hit = reg.get(nk(n)) or harv.get(nk(n)) or (len(ck(n)) > 3 and (reg.get(ck(n)) or harv.get(ck(n))))
            if hit: row = [n, l, 'skip', hit, '', '', '', '', '', regreason(hit)]
            elif o & CORE or nk(n) in {nk(x) for x in SCOPE19}: row = [n, l, 'skip', '', '', '', '', '', '', 'duplicate in lists']
            elif 'fashiola' in o and nk(n) in FDK:
                fr = FDK[nk(n)]
                row = [n, l, 'skip', fr[2], '', '', '', '', '', 'already harvested' if fr[1] == 'add' else FMAP.get(fr[5], fr[5])]
            elif not (('notino' in o and 'nordstrom' in o) or 'fashiola' in o):
                row = [n, l, 'skip', '', '', '', '', '', '', 'single retailer']
            elif l == 'nordstrom' and 'notino' in o:
                row = [n, l, 'skip', '', '', '', '', '', '', 'duplicate in lists']
            else: errs.append(f'need decision: {l}|{n} on {sorted(o)}'); continue
        elif pre.get((l, nk(n))):
            h = pre[(l, nk(n))]; t = h[4:] if h.startswith('reg:') else h.split(':', 1)[1]
            row = [n, l, 'skip', t, '', '', '', '', '', regreason(t)]
        elif l == 'luckyscent':
            o = on(n) & set(FRAG_LISTS) - {'luckyscent'}
            if o or 'fragrantica_popular' in on(n): errs.append(f'luckyscent passes rule, needs decision: {n} {o}'); continue
            row = [n, l, 'skip', '', '', '', '', '', '', 'fragrance: single retailer']
        else: errs.append(f'need decision: {l}|{n}'); continue
    elif d[0].startswith('-'):
        code = d[0][1:]; t = d[1] if len(d) > 1 else ''
        r = RS.get(code, code) if code != 'dup' else regreason(t)
        if code == 'dup' and nk(t) not in reg and nk(t) not in harv: errs.append(f'{n}: dup target {t} not found')
        row = [n, l, 'skip', t, '', '', '', '', '', r]
    else:
        cat, sg, nn, kf, c, y = d[:6]
        dm = dom.get(cat, 'general'); seg = AB[dm].get(sg)
        if not seg: errs.append(f'{n}: bad seg {sg} for {cat}')
        if nk(nn) in added:
            row = [n, l, 'skip', added[nk(nn)], '', '', '', '', '', 'duplicate in lists']
        else:
            lists = on(n, [l]) | on(nn)
            lists.discard('H4') if False else None
            if l in ('luckyscent', 'fragrantica_popular') and cat == 'H4' or (l == 'luckyscent'):
                fl = lists & set(FRAG_LISTS)
                if 'fragrantica_popular' not in lists and len(fl) < 2: errs.append(f'{n}: fails fragrance rule {sorted(lists)}')
            if l in NN:
                if not (('notino' in lists and 'nordstrom' in lists) or 'fashiola' in lists or lists & CORE): errs.append(f'{n}: fails two-list test')
            added[nk(nn)] = nn
            dmeta[nn] = sorted(lists)
            row = [n, l, 'add', nn, cat, seg or '', kf, c, y, '']
    rows.append(row)
for k in dec:
    if k not in used: errs.append(f'unused decision {k}')
if errs:
    print('\n'.join(errs)); sys.exit(1)
tmp = R + 'work/_harvest/lists/decisions.tsv.tmp'
with open(tmp, 'w') as fh:
    fh.write('name\tlist\taction\tn\tcat\tseg\tkf\tc\tf\treason\n')
    for r in rows: fh.write('\t'.join(r) + '\n')
os.replace(tmp, R + 'work/_harvest/lists/decisions.tsv')
json.dump(dmeta, open(W + 'lists_of_adds.json', 'w'), ensure_ascii=False, indent=0)
print('wrote', len(rows), collections.Counter(r[2] for r in rows))
