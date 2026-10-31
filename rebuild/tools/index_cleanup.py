"""Index cleanup after the brand layer (coordinator, 2026-10-31; list in verify/retail/PLAN.md).
Edits out/<C>_brands.json (inputs of merge.py): splits rows that mix different companies (rename the
minority-sense entry with a qualifier), drops wrong-sense tags, corporate-owner and person rows,
fixes polluted fields, adds rel links. Log: work/INDEX_CLEANUP.log. Backups: work/INDEX_CLEANUP/.
Usage: python3 tools/index_cleanup.py   then  python3 merge.py <cats> ; registers ; build"""
import json, os, shutil
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RENAME = [  # (cat, old, new, field fixes)
    ('C1', 'Norton', 'Norton (abrasives)', {}), ('I1', 'Norton', 'Norton (security software)', {}),
    ('I3', 'Three', 'Three (mobile network)', {}),
    ('J10', 'Castello', 'Castello (pipes)', {}),
    ('J10', 'Clipper', 'Clipper (lighters)', {}), ('J9', 'Clipper', 'Clipper (soda)', {}),
    ('C7', 'Frontier', 'Frontier (implements)', {}), ('I3', 'Frontier', 'Frontier (internet)', {}),
    ('E2', 'Fox', 'Fox (fishing tackle)', {}), ('E3', 'Fox', 'Fox (bassoons)', {}),
    ('I3', 'Fox', 'Fox Corporation', {}), ('J8', 'Fox', 'Fox (confectionery)', {}),
    ('I1', 'Proton', 'Proton (privacy software)', {}), ('I3', 'Proton', 'Proton (privacy software)', {}),
    ('C2', 'Halls', 'Halls (greenhouses)', {'kf': 'greenhouses'}),
    ('C2', 'Viking', 'Viking (mowers)', {}), ('E2', 'Viking', 'Viking (skates)', {}),
    ('J7', 'Ferrari', 'Ferrari (Trento)', {}),
    ('C8', 'Fischer', 'Fischer (fixings)', {}), ('E6', 'Fischer', 'Fischer (barometers)', {}),
    ('G1', 'Bell', 'Bell (helicopters)', {}),
    ('C2', 'Stiga', 'Stiga (garden machinery)', {}),
    ('E2', 'Castellani', 'Castellani (shooting wear)', {}),
    ('F3', 'Select', 'Select (trading cards)', {}),
    ('E2', 'Mongoose', 'Mongoose (cricket bats)', {}),
    ('E2', 'Lynx', 'Lynx (fitness equipment)', {}), ('G3', 'Lynx', 'Lynx (grills)', {}),
    ('E4', 'Excalibur', 'Excalibur (crossbows)', {}),
    ('H1', 'Remington', 'Remington (grooming)', {}),
    ('E3', 'Linn', 'Linn Electronics', {}),
    ('J8', 'King', 'King (crisps)', {}),
    ('A5', 'Jaguar', 'Jaguar (watches)', {}),
    ('G1', 'Yeti', 'Yeti Cycles', {'kf': 'mountain bikes'}),
    ('J8', 'Sunbeam', 'Sunbeam (bread)', {}),
    ('A1', 'Imperial', 'Imperial (fashion)', {}),
    ('A5', 'Alpina', 'Alpina (watches)', {}),
    ('E3', 'Suzuki', 'Suzuki (harmonicas)', {}),
    ('E4', 'Benelli', 'Benelli Armi', {}),
    ('G1', 'Singer', 'Singer (cars)', {}),
    ('C8', 'Vitra (tiles)', 'VitrA (Eczacıbaşı)', {}), ('G3', 'VitrA (sanitaryware)', 'VitrA (Eczacıbaşı)', {}),
    ('E3', 'Bentley', 'Bentley (pianos)', {}),
    ('I1', 'AA6YQ', 'DXLab Suite', {}), ('I1', 'N3FJP', "N3FJP Software", {}),
    ('I1', 'Irfan Skiljan', 'IrfanView', {}), ('I1', 'Kovid Goyal', 'calibre', {}),
]
FIX = [  # (cat, name, field fixes) for polluted fields on the main-sense row
    ('G1', 'Ferrari', {'kf': 'sports cars'}), ('G1', 'Lynx', {'kf': 'snowmobiles'}),
    ('G1', 'Suzuki', {'kf': 'cars and motorcycles'}), ('C2', 'Wilkinson Sword', {'kf': 'garden tools'}),
    ('C5', 'Uni-ball', {'rel': ['Mitsubishi Pencil']}), ('C4', 'Uni-ball', {'rel': ['Mitsubishi Pencil']}),
    ('C5', 'Camlin', {'rel': ['Kokuyo Camlin']}), ('C5', 'Helix', {'rel': ['Maped']}),
    ('C5', 'Wahl-Eversharp', {'rel': ['Eversharp']}),
]
DROP = [  # (cat, name, why)
    ('C7', 'Ferrari', 'tractor sense already in Ferrari (tractors)'), ('C7', 'Deutz', 'tractor sense is Deutz-Fahr'),
    ('D3', 'Garrard', 'turntable sense is Garrard (turntables)'),
    ('H4', 'Shoyeido', 'incense maker: B4/F4, not perfume'), ('H4', 'Nippon Kodo', 'incense maker: B4/F4, not perfume'),
    ('I3', 'Financial Times', 'content publisher: deferred (owner rule)'),
    ('I3', 'The New York Times', 'content publisher: deferred (owner rule)'),
    ('C4', 'Lion Capital', 'corporate owner'), ('C4', 'ACCO Brands', 'corporate owner'),
    ('C2', 'BDT Capital Partners', 'corporate owner'),
    ('I3', 'Government of China (74.25 %)', 'ownership string'), ('I3', 'Government of India', 'ownership string'),
    ('I3', 'Government of Qatar', 'ownership string'), ('I3', 'Government of Vietnam', 'ownership string'),
] + [(c, 'Newell Brands', 'corporate owner') for c in ('B1', 'B3', 'B4', 'B5', 'C4', 'C5', 'G1')]
os.makedirs(f'{R}/work/INDEX_CLEANUP', exist_ok=True)
files, log = {}, []
def load(c):
    if c not in files:
        p = f'{R}/out/{c}_brands.json'; shutil.copy(p, f'{R}/work/INDEX_CLEANUP/{c}_brands.json.before')
        files[c] = json.load(open(p))
    return files[c]['b']
for c, n, why in DROP:
    B = load(c); k = len(B); files[c]['b'] = [b for b in B if b['n'] != n]
    log.append(f'drop {c} {n}: {why} ({k - len(files[c]["b"])})')
for c, o, n, f in RENAME:
    B = load(c); hit = [b for b in B if b['n'] == o]
    if not hit: log.append(f'MISS rename {c} {o}'); continue
    have = next((b for b in B if b['n'] == n), None)
    for b in hit:
        if have is not None and have is not b:
            for kk, vv in b.items(): have.setdefault(kk, vv)
            B.remove(b); log.append(f'fold {c} {o} -> existing {n}')
        else:
            b['n'] = n; b.update(f); have = b; log.append(f'rename {c} {o} -> {n}')
for c, n, f in FIX:
    B = load(c); hit = [b for b in B if b['n'] == n]
    for b in hit:
        for kk, vv in f.items():
            b[kk] = sorted(set((b.get(kk) or []) + vv)) if kk == 'rel' else vv
    log.append(f'fix {c} {n} {f}' if hit else f'MISS fix {c} {n}')
for c, d in files.items():  # exact duplicate rows created by data history (e.g. Sunbeam G1 twice)
    seen, out = set(), []
    for b in d['b']:
        k = json.dumps(b, sort_keys=True, ensure_ascii=False)
        if k in seen: log.append(f'dedupe {c} {b["n"]}'); continue
        seen.add(k); out.append(b)
    d['b'] = out
    json.dump(d, open(f'{R}/out/{c}_brands.json', 'w'), ensure_ascii=False, indent=1)
open(f'{R}/work/INDEX_CLEANUP.log', 'w').write('\n'.join(log) + '\n')
print(' '.join(sorted(files))); print('\n'.join(l for l in log if l.startswith('MISS')) or 'no misses')
