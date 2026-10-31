import json, copy, os, sys, shutil, re
sys.path.insert(0, '/home/user/Possession-Taxonomy/rebuild/work/STR_F1')
import spec
R = '/home/user/Possession-Taxonomy/rebuild/'
old = json.load(open(R + 'work/STR_F1/bak/F1.json'))
oldk = {}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']:
            oldk[k['n']] = copy.deepcopy(k)
before = dict(depts=len(old['depts']), shelves=sum(len(d['s']) for d in old['depts']), kinds=len(oldk),
              arch=sum(len(k.get('x', []) or []) for k in oldk.values()))

pool = {}
renames = {}
def put(k):
    assert k['n'] not in pool, k['n']
    pool[k['n']] = k

placed_old = set()
for name, k in oldk.items():
    if name in spec.MOVES_OUT:
        continue
    if name in spec.MERGED:
        renames[name] = spec.MERGED[name]
        continue
    # archetype handling
    drop = set(spec.DROP_X.get(name, []))
    to_r = spec.TO_R.get(name, {})
    xs = []
    for x in k.get('x', []) or []:
        if x['n'] in drop:
            continue
        if x['n'] in to_r:
            v = to_r[x['n']]
            if v:
                r = k.setdefault('r', [])
                if list(v) not in r:
                    r.append(list(v))
            continue
        xs.append(x)
    unknown = [n for n in list(drop) + list(to_r) if n not in [x['n'] for x in k.get('x', []) or []]]
    assert not unknown, (name, unknown)
    if 'x' in k:
        k['x'] = xs
        if not xs:
            del k['x']
    new = spec.RENAME.get(name, name)
    if new != name:
        renames[name] = new
        k['n'] = new
    put(k)

# splits and updates of renamed kinds
def upd(name, **kw):
    pool[name].update(kw)
upd("VHS-C cassette", a="VHS-C · S-VHS-C · compact VHS", d="JVC's compact VHS cassette of 1982 for camcorders, played in a VHS deck through an adapter cassette.",
    s="https://en.wikipedia.org/wiki/VHS-C")
upd("Wire recording", a="wire spool · magnetic wire", d="Sound recorded on fine steel wire wound on a spool, used for dictation and early home recording before tape.")
upd("Digital Audio Tape (DAT)", a="DAT · R-DAT", d="Sony's 1987 digital cassette that records 16-bit audio on a rotating head, popular for studio master tapes.",
    s="https://en.wikipedia.org/wiki/List_of_tape_cartridge_and_cassette_formats")
upd("Songbook", a="song collection · album · folio", d="Bound volume of popular songs in notation for voice, piano or guitar, usually one artist, show or theme.")
upd("Performance parts", a="set of parts · single part · instrumental part · score and parts",
    d="Performers' parts of a work issued separately, as a complete set or a single part, with or without the score.")
upd("Exhibition catalogue", d="Printed record of an exhibition, with illustrations and essays, issued by the museum, gallery or fair.")
upd("Photobook", d="Book in which photographs carry the content, made as a work in itself rather than a catalogue.")

def NKd(n, a, d, s, tt, **kw):
    return spec.NK(n, a, d, s, tt, **kw)
TAPE = "https://en.wikipedia.org/wiki/List_of_tape_cartridge_and_cassette_formats"
V8 = "https://en.wikipedia.org/wiki/8_mm_video_format"
extra = [
 NKd("Video8 and Hi8 cassette", "Video8 · Hi8 · 8 mm video · 8mm camcorder tape", "Sony and Kodak's 8 mm tape in a small cassette (1984), with the higher-quality Hi8 from 1989, for camcorders.", V8,
     [["Generation", ["Video8 (1984)", "Hi8 (1989)"]], ["Recording speed", ["SP", "LP"]], ["Length", ["30 minutes", "60 minutes", "90 minutes", "120 minutes"]]]),
 NKd("MiniDV cassette", "DV cassette · MiniDV · DVCAM", "Small digital videocassette of the DV system (1995), used in camcorders and for home editing.", "https://en.wikipedia.org/wiki/Timeline_of_video_formats",
     [["Cassette size", ["MiniDV", "Standard DV"]], ["Recording", ["SP", "LP"]], ["Length", ["60 minutes", "80 minutes"]]]),
 NKd("Digital8 cassette", "Digital8 · D8", "Sony's 1999 digital format recording DV data onto 8 mm tape, which also plays older Video8 and Hi8 tapes.", V8,
     [["Content", ["Blank", "Home-recorded"]], ["Length", ["60 minutes", "120 minutes"]], ["Tape", ["Hi8-type metal particle", "Evaporated metal"]]]),
 NKd("Elcaset", "Elcassette · large cassette", "Large audio cassette of 1976 by Sony, Panasonic and Teac, using quarter-inch tape at higher speed.", TAPE,
     [["Content", ["Blank", "Pre-recorded"]], ["Tape", ["¼-inch tape"]], ["Speed", ["9.5 cm/s"]]]),
 NKd("Digital Compact Cassette (DCC)", "DCC · digital cassette", "Philips and Matsushita's 1992 digital cassette that plays analogue compact cassettes in the same deck.", TAPE,
     [["Content", ["Blank", "Pre-recorded"]], ["Compression", ["PASC"]], ["Length", ["45 minutes", "90 minutes"]]]),
 NKd("Dictabelt", "Dictaphone belt · embossed belt", "Plastic belt embossed with a voice groove, used for office dictation from the 1940s.", oldk["Dictation and wire recording"]["s"],
     [["Belt", ["Plastic belt (about 15 minutes)"]], ["Content", ["Blank", "Recorded"]]]),
]
for k in extra:
    put(k)
for n, k in spec.NEW_KINDS.items():
    put(copy.deepcopy(k))
for n in list(pool):
    pass
# new archetypes
for kn, xs in spec.NEW_X.items():
    pool[kn].setdefault('x', [])
    pool[kn]['x'] = xs + pool[kn].get('x', [])

# apply tt and see
for n, k in pool.items():
    if 'tt' in k:
        continue
    g = spec.TT.get(n)
    assert g, "missing tt for " + n
    k['tt'] = g
    k.pop('t', None)
for n, k in pool.items():
    k.pop('t', None)
    sv = spec.SEE.get(n, [])
    cur = k.get('see', []) or []
    for e in sv:
        if e not in cur:
            cur.append(e)
    if cur:
        k['see'] = cur

# assemble
oldd = {d['n']: d for d in old['depts']}
out = {k: v for k, v in old.items() if k != 'depts'}
out['ax'] = spec.CAT_AX
out['key'] = spec.CAT_KEY
out['depts'] = []
used = set()
for dd in spec.DEPTS:
    od = oldd[dd['n']]
    nd = {'n': dd['n'], 'mode': od['mode'], 't': dd['t'], 'ax': dd['ax']}
    if od.get('note'): nd['note'] = od['note']
    if od.get('b'): nd['b'] = od['b']
    nd['s'] = []
    for (sn, st, sax, kinds) in dd['shelves']:
        sh = {'n': sn, 't': st}
        if len(kinds) > 3 or sax:
            sh['ax'] = sax
        if len(kinds) > 3: assert sax, sn
        if not sax: sh.pop('ax', None)
        sh['k'] = []
        for kn in kinds:
            assert kn in pool, kn
            assert kn not in used, kn
            used.add(kn)
            sh['k'].append(pool[kn])
        nd['s'].append(sh)
    out['depts'].append(nd)
left = set(pool) - used
assert not left, left
# every old kind accounted
for n in oldk:
    assert n in spec.MOVES_OUT or n in renames or n in used, n

# moves
mp = R + 'out/F1_moves.json'
moves = json.load(open(R + 'work/STR_F1/bak/F1_moves.json'))
for n, (to, dept) in spec.MOVES_OUT.items():
    k = copy.deepcopy(oldk[n])
    if not any(e['kind']['n'] == n for e in moves['out']):
        moves['out'].append({'to': to, 'dept': dept, 'kind': k})

after = dict(depts=len(out['depts']), shelves=sum(len(d['s']) for d in out['depts']), kinds=len(used),
             arch=sum(len(k.get('x', []) or []) for d in out['depts'] for s in d['s'] for k in s['k']))
print('before', before); print('after', after); print('renames', renames)
tmp = R + 'work/STR_F1/F1.new.json'
json.dump(out, open(tmp, 'w'), ensure_ascii=False, indent=1)
json.dump(moves, open(R + 'work/STR_F1/F1_moves.new.json', 'w'), ensure_ascii=False, indent=1)
rn = {k: v for k, v in renames.items()}
json.dump(rn, open(R + 'work/STR_F1/F1_renames.new.json', 'w'), ensure_ascii=False, indent=1)
if '--write' in sys.argv:
    os.replace(tmp, R + 'out/F1.json')
    os.replace(R + 'work/STR_F1/F1_moves.new.json', mp)
    os.replace(R + 'work/STR_F1/F1_renames.new.json', R + 'out/F1_renames.json')
    print('written')
