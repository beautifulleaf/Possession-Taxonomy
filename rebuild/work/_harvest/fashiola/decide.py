"""Build decisions.tsv for the Fashiola 'new' names from dec*.txt (skip rows carry the reason in kf)."""
import json, re, unicodedata, os, glob, collections, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/../../..')
D = 'work/_harvest/fashiola/'
def nk(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower().replace('&', 'and')
    return re.sub(r'[^a-z0-9]', '', s)
SEGS = json.load(open('SEGMENTS.json'))['domains']
dom = {c: d for d, v in SEGS.items() for c in v['cats'] if c != '*'}
AB = {'fashion': dict(LH='Luxury house', D='Designer', CP='Contemporary & premium', HW='Heritage & workwear', JD='Japanese & denim',
                      SW='Streetwear', OT='Outdoor & technical', AS='Athletic & sportswear', HS='High street', VB='Value & basics',
                      BA='Bespoke & artisan', TN='Traditional & national dress', SA='Subculture & alternative'),
      'luxury': dict(LH='Luxury house', HM='Haute maison', IM='Independent maker', D='Designer', P='Premium', M='Mainstream', V='Value',
                     BA='Bespoke & artisan', TR='Traditional & regional'),
      'general': dict(PF='Professional & flagship', P='Premium', M='Mainstream', V='Value', HMF='Heritage manufactory',
                      AI='Artisan & independent', SP='Specialist', OL='Own-label & retailer', II='Institution & issuer')}
new = json.load(open(D + 'names.json'))['new']
lines = [l.rstrip('\n') for p in sorted(glob.glob(D + 'dec*.txt')) for l in open(p) if l.strip()]
byexact = {}; bynk = collections.defaultdict(list); errs = []
for l in lines:
    f = l.split('|'); byexact.setdefault(f[0], f); bynk[nk(f[0])].append(f)
rows = []; used = set()
for n in new:
    f = byexact.get(n)
    if f is None:
        c = [x for x in bynk.get(nk(n), []) if x[0] not in new]
        if len(c) != 1: errs.append(f'no unique decision for {n!r}: {c}'); continue
        f = c[0]
    if f[0] in used: errs.append(f'decision used twice {f[0]!r}')
    used.add(f[0])
    if f[1].startswith('-'):
        rows.append([n, 'skip', f[2] if len(f) > 2 else '', '', '', f[1][1:], '', ''])
    else:
        _, cat, sg, nn, kf, c, y = f
        d = dom.get(cat, 'general'); seg = AB[d].get(sg)
        if not seg: errs.append(f'{n}: bad seg {sg} for {cat}')
        rows.append([n, 'add', nn, cat, seg or '', kf, c, y])
for l in lines:
    if l.split('|')[0] not in used: errs.append(f'unused decision line: {l}')
if errs:
    print('\n'.join(errs)); sys.exit(1)
tmp = D + 'decisions.tsv.tmp'
with open(tmp, 'w') as fh:
    fh.write('name\taction\tn\tcat\tseg\tkf\tc\tf\n')
    for r in rows: fh.write('\t'.join(r) + '\n')
os.replace(tmp, D + 'decisions.tsv'); print('wrote', len(rows))
