import json,re,os
d=json.load(open('out/D1.json'))
cur=None;data={}
for l in open('work/CMP_DEV/nv_raw.txt'):
    l=l.strip()
    if l.startswith('#'): cur=l[1:]; data[cur]=[]
    elif l: n,dt=[p.strip() for p in l.split('|')]; data[cur].append((n,re.search(r'\d{4}',dt).group(),dt))
tot=0
for de in d['depts']:
 for s in de['s']:
  for k in s['k']:
   if k['n']=='Graphics card':
    for x in k['x']:
     if x['n'] in data:
      have={v['n'].lower() for v in x['v']}
      new=[]
      for n,y,dt in sorted(data[x['n']],key=lambda t:(t[1],t[0])):
        if n.lower() in have: continue
        have.add(n.lower()); new.append({'n':n,'mk':'Nvidia','y':y,'d':'Launched '+dt+'.'}); 
      x['v']+=new; tot+=len(new)
    k['sel']+=f" Covers {tot} individual GeForce and Titan desktop models added as versions from Wikipedia's Nvidia GPU list and the GeForce 20, 30, 40 and 50 series articles; the list's rebrand and workstation rows, mobile parts and a few undated rows (GeForce 9400 and 9500 GT, GTX 1660 Super and Ti) are missing."
json.dump(d,open('work/CMP_DEV/D1.tmp','w'),ensure_ascii=False,indent=1)
os.replace('work/CMP_DEV/D1.tmp','out/D1.json'); print(tot)
