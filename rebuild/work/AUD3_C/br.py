import json,sys,collections
c=sys.argv[1]
d=json.load(open(f'reader/brands/{c}.json'))
b=d.get('b',d) if isinstance(d,dict) else d
print(c,'brands',len(b), 'keys', list(d.keys()) if isinstance(d,dict) else '')
print(collections.Counter(x.get('seg') for x in b))
print('; '.join(x['n']+'['+str(x.get('c',''))+']' for x in b))
try:
  t=json.load(open(f'reader/traditions/{c}.json')); t=t.get('t',t)
  print('TRAD',len(t),'; '.join(x['n'] for x in t))
except Exception as e: print('no trad',e)
