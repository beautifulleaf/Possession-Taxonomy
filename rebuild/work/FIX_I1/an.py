import json,re
d=json.load(open('out/I1.json'))
b=json.load(open('out/I1_brands.json'))['b']
reg={x['n'].lower() for x in b}
miss={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      for a in k.get('x',[]):
        if not a.get('mk'): print('NOMK',k['n'],'|',a['n'])
        elif a['mk'].lower() not in reg: miss.setdefault(a['mk'],[]).append(a['n'])
        if re.search(r'^(other|independent|mastering chains|modular and|vocal effects|tape plug|character|dynamic eq|single-game|multi-network)|emulators$',a['n'],re.I): print('CATCH',k['n'],'|',a['n'],'|',len(a.get('v',[])),a.get('mk'))
print(len(miss));
for m,v in miss.items(): print(m,'<-',v)
