import json,sys,re
m=json.load(open('/home/user/Possession-Taxonomy/rebuild/meta.json'))
pats=[re.compile(p,re.I) for p in sys.argv[1:]]
for c in m['cats']:
  d=json.load(open('/home/user/Possession-Taxonomy/rebuild/reader/%s.json'%c['c']))
  for x in d['depts']:
    for s in x.get('s',[]):
      for k in s.get('k',[]):
        nm=k.get('n','')+' ('+k.get('a','')+')'
        for p in pats:
          if p.search(nm): print(p.pattern,'|',c['c'],'>',x['n'],'>',s['n'],'>',k.get('n',''))
