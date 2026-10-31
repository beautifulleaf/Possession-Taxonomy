import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/J8.json'
d=json.load(open(P))
L='https://en.wikipedia.org/wiki/'
NOTE="Also placed: the full rows of Wikipedia's List of confectionery brands, List of ice cream brands, List of brand name breads and the snack, popcorn and nut rows of List of brand name food products, each read to its end (parlour and shop chains, defunct brands, companies without a product brand and generic sweet names left out). "
tgt=set(); owners={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k.get('x') and any(e['s'].startswith(L) and any(t in e['s'] for t in ('List_of_confectionery_brands','List_of_ice_cream','List_of_brand_name')) for e in k['x']) or any(e['s'] in (L+'Wonder_Bread',) for e in k.get('x',[])):
        pass
      for e in k.get('x',[]):
        pass
import re
names=set(open('/home/user/Possession-Taxonomy/rebuild/work/GAP_J8/names.txt').read().split('\n'))
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      new=[e for e in k.get('x',[]) if e['n'].lower() not in names and e.get('own') and e['s'].startswith(L) and e.get('cty') is not None and e['d'] and e['tier'] and e.get('v')==[]]
      # new entries are those not in names.txt (snapshot before round 2 and Mithai etc. lack 'own')
      if new and NOTE not in k['sel']:
        m=re.search(r'(Complete: \d+ of \d+ in |Covers \d+ of about \d+ in |No complete list exists; follows )',k['sel'])
        i=m.start() if m else len(k['sel'])
        k['sel']=k['sel'][:i]+NOTE+k['sel'][i:]
      for e in new:
        if e['own'] not in owners: owners[e['own']]=(e.get('cty',''),e['s'],e['tier'])
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
B=json.load(open('/home/user/Possession-Taxonomy/rebuild/out/J8_brands.json'))
have={b['n'] for b in B['b']}; c=0
for o,(cty,s,t) in owners.items():
    if o in have: continue
    B['b'].append({'n':o,'c':cty,'f':'','seg':'Mainstream','d':'Brand owner named on the cited Wikipedia list.','lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':s,'kf':'','own':o,'tier':t}); c+=1
json.dump(B,open('/home/user/Possession-Taxonomy/rebuild/out/J8_brands.json.tmp','w'),ensure_ascii=False,indent=1); os.replace('/home/user/Possession-Taxonomy/rebuild/out/J8_brands.json.tmp','/home/user/Possession-Taxonomy/rebuild/out/J8_brands.json')
print(c)
