import json,sys
f,pat=sys.argv[1],sys.argv[2].lower()
d=json.load(open(f'out/{f}.json'))
for de in d['depts']:
  for s in de.get('s',[]):
    for k in s.get('k',[]):
      if pat in k['n'].lower():
        print(de['n'],'|',s['n'],'|',k['n'],len(k.get('x',[])))
        print({a:b for a,b in k.items() if a not in('x',)})
        for x in k.get('x',[]):
          print('  ',x['n'],'|',x.get('y'),'|',x.get('g'),'|',x.get('mk'),'|',len(x.get('v',[])),'|',x.get('s'),'|',x.get('role'))
