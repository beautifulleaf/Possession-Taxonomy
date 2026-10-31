import json,re
R='/home/user/Possession-Taxonomy/rebuild/'
p=json.load(open(R+'out/B5_parts/APPL.json'))
seen=set();nb=[]
for b in p['brands']:
    if b['n'] in seen: continue
    seen.add(b['n']); nb.append(b)
p['brands']=nb
bad=[]
for d in p['depts']:
  for s in d['s']:
    for k in s['k']:
      for e in k.get('x',[]):
        if e['n']=='Nescafé Dolce Gusto': e['mk']='Nescafé Dolce Gusto'
        if len(e.get('y',''))>14 and not re.fullmatch(r'(c\. )?\d{4}.*',e['y']): bad.append((e['n'],e['y']))
        for key in('own','tier','own_y'):
            if e.get(key) is None: e.pop(key,None)
        if e.get('role') is None: e.pop('role',None)
        if e['n']=='Mason jar': e['y']='19th century'; e['d']='Glass jar with a screw-thread lid patented by John Landis Mason in the 19th century.'
print(bad)
json.dump(p,open(R+'out/B5_parts/APPL.json','w'),ensure_ascii=False)
