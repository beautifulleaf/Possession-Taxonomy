"""After a merge: list kinds of an earlier reader snapshot whose name no longer appears anywhere in the current
reader data (as a kind, type, archetype, version, model or alias), and stray departments (one shelf named like
the department, holding moved-in kinds). Usage: python3 tools/lost_check.py <git-ref of the earlier snapshot>"""
import json, glob, os, subprocess, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ref = sys.argv[1]
now = ' '.join(open(f).read().lower() for f in glob.glob('reader/[A-J]*.json'))
lost = []
for f in sorted(glob.glob('reader/[A-J]*.json')):
    c = os.path.basename(f)[:-5]
    try: old = json.loads(subprocess.run(['git', 'show', f'{ref}:rebuild/reader/{c}.json'], capture_output=True, text=True, check=True).stdout)
    except subprocess.CalledProcessError: continue
    for dp in old['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n'].lower().lstrip('=') not in now: lost.append((c, k['n'], len(k.get('x') or []), len(k.get('m') or [])))
print(len(lost), 'old kind names no longer found anywhere:')
for l in lost: print('  ', *l)
for f in sorted(glob.glob('reader/[A-J]*.json')):
    d = json.load(open(f)); out = json.load(open('out/' + os.path.basename(f)))
    od = {dp['n'] for dp in out['depts']}
    for dp in d['depts']:
        if dp['n'] not in od: print('stray dept', os.path.basename(f)[:-5], dp['n'], [k['n'] for s in dp['s'] for k in s['k']])
