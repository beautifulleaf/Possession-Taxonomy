import json,sys
j=sys.argv[1]
t=open(f'/home/user/Possession-Taxonomy/rebuild/work/I1/prompts/{j}.txt').read()
b=t[t.index('Old data for this shelf'):]; b=b[b.index('```json')+7:]; b=b[:b.index('```')]
old=set()
for o in json.loads(b):
    for k in ('m','r'):
        for a,c in o.get(k,[]): old.add(a.lower())
d=json.load(open(f'/home/user/Possession-Taxonomy/rebuild/work/I1/shelves/{j}.json'))
for k in d['kinds']:
    for key in ('m','r'):
        for a,c in k.get(key,[]):
            if a.lower() not in old: print('NEW', k['n'], key, a)
    for x in k.get('x',[]):
        for v in x.get('v',[]):
            if v['n'].lower() not in old: pass
