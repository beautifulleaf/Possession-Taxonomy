import json,os,re
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'E2.json'))
pats=[re.compile(r'Covers (\d+) [^.;]*? named on those pages; no complete [^.]*?(?:total is unknown|exists)(?: for this kind)?[^.]*\.'),
      re.compile(r'Covers (\d+) lines and makers from those pages, not every product on the market\.'),
      re.compile(r'Covers (\d+) lines or classes read from fetched pages[^;]*; no whole-space reference lists this kind, so this is not a complete list\.')]
ch=0;volkl=0
for dpt in d['depts']:
  for s in dpt['s']:
    for kk in s['k']:
      sel=kk.get('sel')
      for e in kk.get('x',[]):
        if e.get('mk')=='Völkl' or e['n'].startswith('Völkl'):
          for key,val in (('cty','Germany'),('own','Elevate Outdoor Collective (Kohlberg & Company)'),('tier','Independent'),('own_y','2017')):
            if not e.get(key): e[key]=val
          volkl+=1
      if not sel: continue
      for p in pats:
        m=p.search(sel)
        if m:
          n=len(kk.get('x',[]))
          kk['sel']=sel[:m.start()]+'No complete list exists; follows the maker and retailer range pages cited on each entry (%d entries).'%n+sel[m.end():]
          ch+=1; break
print(ch,volkl)
t=P+'E2.json.tmp'; json.dump(d,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,P+'E2.json')
