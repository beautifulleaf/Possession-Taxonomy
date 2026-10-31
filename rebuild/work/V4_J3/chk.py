import sys,json
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/V4_J3')
from names import *
d=json.load(open('/home/user/Possession-Taxonomy/rebuild/out/J3.json'))
S=existing(d)
for l in open('/home/user/Possession-Taxonomy/rebuild/work/V4_J3/cand.txt'):
    n=l.split('|')[0].strip(); k=nz(n)
    hit=S.get(k)
    if not hit:
        # token containment
        for kk,v in S.items():
            if kk and (kk in k or k in kk) and len(kk)>5: hit=v;break
    print(('HAVE ' if hit else 'MISS ')+n, hit or '')
