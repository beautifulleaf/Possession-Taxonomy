import json,os,re
P='rebuild/out/B2.json'
exec(open('rebuild/work/V4_B2/fix.py').read().split("for dp in d['depts']")[0].split("d=json.load(open(P))")[1].join(["d=json.load(open(P))",""])) if False else None
d=json.load(open(P))
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      t=k.get('sel')
      if not t: continue
      ms=list(re.finditer(r'(Complete: |Covers )\d+ (of|pile)',t))
      if len(ms)>1:
          # keep last coverage sentence; drop earlier ones up to it
          k['sel']=t[:ms[0].start()].rstrip()+' '+t[ms[-1].start():]
          k['sel']=k['sel'].replace('  ',' ')
      if k['n']=='Flatweave rug': k['sel']=k['sel'].replace('for flatweaves. flatweave','for flatweaves.')
      if k['n']=='Moroccan rug': k['sel']=k['sel'].replace('are not added. Covers','Covers',1) if False else k['sel']
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k.get('sel') and k['n'] in('Flatweave rug','Persian rug','Moroccan rug','Central Asian rug'): print(k['sel'],'\n')
