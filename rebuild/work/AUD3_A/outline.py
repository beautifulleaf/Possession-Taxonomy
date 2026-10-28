import json,sys
c=sys.argv[1]
d=json.load(open(f'rebuild/reader/{c}.json'))
print(c, d['lead'])
tk=tx=0
for dp in d['depts']:
  nk=sum(len(s['k']) for s in dp['s']); na=sum(len(k.get('x',[])) for s in dp['s'] for k in s['k'])
  print(f"\n## {dp['n']} [{dp.get('mode')}] kinds={nk} arch={na} note={dp.get('note','')}")
  for s in dp['s']:
    print(f"  # {s['n']} ({len(s['k'])})")
    for k in s['k']:
      tk+=1; tx+=len(k.get('x',[]))
      xs=', '.join(x['n'] for x in k.get('x',[]))
      print(f"    - {k['n']} | t={len(k.get('t',[]))} x={len(k.get('x',[]))} m={len(k.get('m',[]))} r={len(k.get('r',[]))} :: {xs[:400]}")
      if k.get('t'): print(f"        t: {'; '.join(k['t'])[:400]}")
print('\nTOTAL kinds',tk,'arch',tx)
b=json.load(open(f'rebuild/reader/brands/{c}.json'))['b']
from collections import Counter
print('brands',len(b), Counter(x.get('seg') for x in b).most_common(15))
try:
  t=json.load(open(f'rebuild/reader/traditions/{c}.json'));t=t.get('t',t)
  print('traditions',len(t), Counter(x.get('g') for x in t)); print('; '.join(x['n'] for x in t))
except Exception as e: print(e)
