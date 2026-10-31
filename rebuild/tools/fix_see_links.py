"""One-off coordinator corrections to see-links after see_check.py: retarget or restore named links in reader/ and out/.
Each edit: (category, kind, target category, old target or None to add, new target, reason)."""
import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
EDITS = [
 ('A3', 'Evil-eye amulet', 'F4', 'Omamori', 'Evil-eye charm', None),
 ('A3', 'Cornicello', 'F4', 'Omamori', 'Evil-eye charm', None),
 ('E3', 'Singing bowl', 'F4', 'Altar handbell', 'Rin', None),
 ('B6', 'Fabric waterproofer', 'A2', None, 'Shoe polish and conditioner', 'shoe waterproofing sprays sit with shoe care'),
 ('E2', 'Wushu practice weapon', 'E4', None, 'Jian', 'live and display jian are weapons'),
]
for c, kn, tc, old, new, why in EDITS:
    for p in (f'reader/{c}.json', f'out/{c}.json'):
        d = json.load(open(p)); hit = False
        for dp in d['depts']:
            for s in dp['s']:
                for k in s['k']:
                    if k['n'] != kn: continue
                    see = k.setdefault('see', [])
                    if old:
                        for sv in see:
                            if sv[0] == tc and sv[1] == old: sv[1] = new; hit = True
                    elif not any(sv[0] == tc and sv[1] == new for sv in see):
                        see.append([tc, new, why]); hit = True
        json.dump(d, open(p + '.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(p + '.tmp', p)
        print(p, kn, '->', tc, new, 'ok' if hit else 'NOT FOUND')
