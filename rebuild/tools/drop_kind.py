"""Drop out-of-scope kinds from an out/ category file. Usage: python3 tools/drop_kind.py I2 "Kind name" ["Kind name" ...]"""
import json, os, sys, shutil
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
c, names = sys.argv[1], set(sys.argv[2:])
p = f'out/{c}.json'; os.makedirs('work/_drops', exist_ok=True); shutil.copy(p, f'work/_drops/{c}.json.bak')
d = json.load(open(p)); n = 0
for dp in d['depts']:
    for s in dp['s']:
        keep = [k for k in s['k'] if k['n'] not in names]; n += len(s['k']) - len(keep); s['k'] = keep
        for k in s['k']: k['see'] = [x for x in k.get('see') or [] if not (x[0] == c and x[1] in names)] or k.pop('see', None) or []
        for k in s['k']:
            if k.get('see') == []: k.pop('see')
    dp['s'] = [s for s in dp['s'] if s['k']]
json.dump(d, open(p + '.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace(p + '.tmp', p)
print('dropped', n)
