import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B
R = B.R
out, dl, rn, mv, missing = B.build()
assert not missing, missing
def wr(path, obj):
    tmp = path + '.tmp'
    json.dump(obj, open(tmp, 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(tmp, path)
# E2.json
wr(R + 'out/E2.json', out)
# renames
wr(R + 'out/E2_renames.json', rn)
# moves (append, never remove existing)
mvf = R + 'out/E2_moves.json'
cur = json.load(open(mvf)); cur.setdefault('out', [])
have = {(m['to'], m['kind']['n']) for m in cur['out']}
for m in mv:
    if (m['to'], m['kind']['n']) not in have: cur['out'].append(m)
wr(mvf, cur)
# brands
bf = R + 'out/E2_brands.json'
bb = json.load(open(bf)); names = {b['n'].lower() for b in bb['b']}
for nb in B.NEWBRANDS:
    if nb['n'].lower() not in names: bb['b'].append(nb)
wr(bf, bb)
json.dump(dl, open(R + 'work/STR_E2/demoted.json', 'w'), ensure_ascii=False, indent=1)
print('written')
