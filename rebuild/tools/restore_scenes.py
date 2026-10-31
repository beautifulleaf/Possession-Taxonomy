"""Bring the clothing scene view (owner decision 2026-10-17: scenes are the way into clothing) from the stage-3 reader
(pages/reader/A1.json, built from data/scenes.tsv and scene_tags.tsv) into the rebuild's A1 files. Scenes own nothing:
they list defining garments and brands, and brand names link to the brand register."""
import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
sc = json.load(open('../pages/reader/A1.json'))['scenes']
for p in ('out/A1.json', 'reader/A1.json'):
    d = json.load(open(p)); d['scenes'] = sc
    json.dump(d, open(p + '.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(p + '.tmp', p)
n = sum(1 + len(x.get('c') or []) for g in sc for x in g['s'])
print('scene groups', len(sc), 'scenes', n, 'brand placements', sum(len(x['b']) for g in sc for x in g['s']))
