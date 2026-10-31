import json,os
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'D2.json'))
RN={'Poco models':'Poco','Lenovo models':'Lenovo tablets','Xiaomi models':'Xiaomi Pad'}
DROP={'Collins Radio 30L-1','Drake L-4','Samsung models'}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      k['x']=[x for x in k.get('x',[]) if x['n'] not in DROP] if 'x' in k else k.get('x')
      if k['x'] is None: k.pop('x')
      for x in k.get('x',[]): x['n']=RN.get(x['n'],x['n'])
json.dump(d,open(R+'D2.json.tmp','w'),ensure_ascii=False,indent=1); os.rename(R+'D2.json.tmp',R+'D2.json')
