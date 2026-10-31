import json,os,collections
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'C8.json')); bj=json.load(open(R+'C8_brands.json')); reg={x['n'] for x in bj['b']}
mk=collections.defaultdict(list); removed={}; cnt=collections.Counter()
def add(m,k):
    if k not in mk[m]: mk[m].append(k)
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      rm={}
      for key in ('m','r'):
        for t in k.pop(key,None) or []: add(t[1],k['n']); rm.setdefault(key,[]).append(t); cnt[key]+=1
      xs=k.pop('x',None)
      if xs:
        for x in xs:
          if x.get('mk'): add(x['mk'],k['n'])
          for v in x.get('v') or []:
            if v.get('mk'): add(v['mk'],k['n'])
        rm['x']=xs; cnt['x']+=len(xs)
      for f in ('nl','sel','xg','dt'): k.pop(f,None)
      if rm: removed[k['n']]=rm
json.dump(removed,open('removed.json','w'),ensure_ascii=False,indent=1)
info={'PPG Industries':('United States','1883','https://en.wikipedia.org/wiki/PPG_Industries'),
'AkzoNobel':('Netherlands','1994','https://en.wikipedia.org/wiki/AkzoNobel'),
'Nippon Paint Holdings':('Japan','1881','https://en.wikipedia.org/wiki/Nippon_Paint'),
'RPM International':('United States','1947','https://en.wikipedia.org/wiki/RPM_International'),
'Axalta Coating Systems':('United States','1866','https://en.wikipedia.org/wiki/Axalta'),
'Asian Paints':('India','1942','https://en.wikipedia.org/wiki/Asian_Paints'),
'Kansai Paint':('Japan','1918','https://en.wikipedia.org/wiki/Kansai_Paint'),
'Jotun':('Norway','','https://en.wikipedia.org/wiki/Jotun'),
'BASF Coatings':('','',''),'Pittsburgh Paints Company':('','','')}
for n in info: mk.setdefault(n,['Wall and ceiling paint'])
added=0
for m,ks in sorted(mk.items()):
    if m in reg or not m: continue
    c,f,s=info.get(m,('','',''))
    e={'n':m,'d':'Maker or brand named under '+', '.join(ks[:3])+'.','kf':ks[0].lower()}
    if c: e['c']=c
    if f: e['f']=f
    if s: e['s']=s
    bj['b'].append(e); added+=1
P='https://www.pcimag.com/articles/114746-2026-global-top-10-top-paint-and-coatings-companies'
N='https://www.pcimag.com/articles/114829-2026-pci-25-top-paint-and-coatings-companies'
g=[('The Sherwin-Williams Co.','Approx. $19.8 billion','2025','estimate; PCI says the company does not report coatings sales separately'),
('PPG Industries','$15.9 billion','2025',''),('AkzoNobel','Approx. $11.48 billion (EUR 10.158 billion)','2025',''),
('Nippon Paint Holdings Co.','Approx. $9.63 billion (JPY 1,440,476 million)','2025',''),
('RPM International Inc.','$7.37 billion','2025','fiscal year ended 31 May 2025'),
('Axalta Coating Systems','$5.117 billion','2025',''),('BASF Coatings','Approx. $4.63 billion (EUR 4.09 billion)','2025',''),
('Asian Paints Limited','Approx. $4.08 billion','2026','fiscal year ending 31 March 2026'),
('Kansai Paint Co. Ltd.','Approx. $3.94 billion','2026','fiscal year ending 31 March 2026'),('Jotun','Approx. $3.31 billion (NOK 34.33 billion)','2025','')]
na=[('The Sherwin-Williams Co.','Approx. $19.8 billion'),('PPG Industries','$15.9 billion'),('RPM International Inc.','$7.37 billion'),('Axalta Coating Systems','$5.117 billion'),('Behr Paint Co.','Approx. $2.34 billion'),('Benjamin Moore & Co.','Approx. $2.0 billion'),('The Pittsburgh Paints Company','Approx. $1.88 billion (PCI estimate)')]
ms=[{'mkt':f'Global paint and coatings, rank {i+1} by coatings sales','who':w,'share':sh,'yr':int(y),'s':P,'note':('sales, not market share; '+n) if n else 'sales, not market share'} for i,(w,sh,y,n) in enumerate(g)]
ms+=[{'mkt':f'North American paint and coatings, rank {i+1} by coatings sales','who':w,'share':sh,'yr':2025,'s':N,'note':'sales, not market share'} for i,(w,sh) in enumerate(na)]
for dp in d['depts']:
    if dp['n']=='Paint & decorating':
        dp['msum']='PCI ranks Sherwin-Williams first in both the world and North America on 2025 coatings sales, ahead of PPG; AkzoNobel, Nippon Paint and RPM follow worldwide. The figures are sales, not shares.'
        dp['ms']=ms
tmp=R+'C8.json.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,R+'C8.json')
tmp=R+'C8_brands.json.tmp'; json.dump(bj,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,R+'C8_brands.json')
print(cnt,added)
