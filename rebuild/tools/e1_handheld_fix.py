"""E1: screen-based handheld games belong to E5 'LCD handheld game' (Game & Watch is already there; Mattel Auto Race moves).
Usage: python3 tools/e1_handheld_fix.py   (rewrites out/E1.json and out/E1_moves.json; backups in bak/)"""
import json, os, shutil, time
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ts = time.strftime('%Y%m%d%H%M%S'); os.makedirs('bak', exist_ok=True)
for f in ('out/E1.json', 'out/E1_moves.json'): shutil.copy(f, f'bak/{os.path.basename(f)}.{ts}')
d = json.load(open('out/E1.json')); mv = json.load(open('out/E1_moves.json'))
k = next(k for dp in d['depts'] for s in dp['s'] for k in s['k'] if k['n'] == 'Electronic handheld toy')
auto = next(x for x in k['x'] if x['n'] == 'Mattel Auto Race')
k['x'] = [x for x in k['x'] if x['n'] not in ('Mattel Auto Race', 'Game & Watch')]
k['d'] = 'Battery toy with lights, sounds or a simple display that you play by pressing, pulling or caring for; screen games are in Video Games.'
mv.setdefault('out', []).append({'to': 'E5', 'dept': '', 'kind': {'n': 'LCD handheld game', 'd': 'Handheld with its game or games built in on its own screen.', 'x': [auto]}})
for f, o in (('out/E1.json', d), ('out/E1_moves.json', mv)):
    json.dump(o, open(f + '.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(f + '.tmp', f)
print('ok', [x['n'] for x in k['x']])
