import json,collections
B='/home/user/Possession-Taxonomy/rebuild/'
S=json.load(open(B+'SEGMENTS.json'))['domains']
todo=[l.rstrip('\n').split('\t') for l in open(B+'work/_seg/general_J.todo.tsv',encoding='utf-8')][1:]
m=[l.rstrip('\n').split('\t') for l in open(B+'work/_seg/general_J.map.tsv',encoding='utf-8')]
assert m[0]==['name','seg','kf']; m=m[1:]
dom={r[0]:r[1] for r in todo}
names=[r[0] for r in m]
assert collections.Counter(names)==collections.Counter(r[0] for r in todo)
for n,s,k in m:
    assert s in S[dom[n]]['segs'],(n,s); assert k and k==k.lower() and len(k.split())<=3,(n,k)
print('OK',len(m)); print(collections.Counter(r[1] for r in m).most_common())
