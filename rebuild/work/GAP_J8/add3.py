import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/J8.json'
d=json.load(open(P))
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k['n']=='Potato crisps' and not any(e['n']=='Tasali' for e in k['x']):
        k['x'].append({"n":"Tasali","a":"","d":"Saudi Arabia's first local chips brand, launched by Savola Group in 1989; PepsiCo bought it in 2001.","mk":"PepsiCo","y":"1989","s":"https://en.wikipedia.org/wiki/Tasali_Snack_Foods","v":[],"own":"PepsiCo","tier":"Global group","cty":"Saudi Arabia","own_y":"2001","g":"PepsiCo"})
  if dp['n']=='Crisps & savoury snacks':
    dp['ms'].append({"mkt":"Saudi Arabian snack foods","who":"Tasali (PepsiCo)","share":"second largest snack food company; no figure","yr":2001,"s":"https://en.wikipedia.org/wiki/Tasali_Snack_Foods","note":"page states no numeric share; Middle East champion found"})
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
