"""List kind names and archetype names that appear on more than one shelf of a category."""
import json, glob, collections, sys
c = sys.argv[1]
seen = collections.defaultdict(list)
for f in sorted(glob.glob(f'work/{c}/shelves/*.json')):
    j = f.split('/')[-1][:-5]
    for k in json.load(open(f))['kinds']:
        seen['K:' + k['n'].lower()].append(j)
        for x in k.get('x', []): seen['X:' + x['n'].lower()].append(j + '/' + k['n'])
for n, v in seen.items():
    if len(v) > 1: print(n, v)
