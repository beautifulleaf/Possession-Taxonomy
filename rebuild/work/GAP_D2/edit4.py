import json,os,re,urllib.parse
P='rebuild/out/D2.json'
d=json.load(open(P))
n=0
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      x=k.get('x')
      if not x: continue
      refs=[];hosts=set()
      for e in x:
        u=e.get('s','')
        m=re.match(r'https://en\.wikipedia\.org/wiki/(.+)',u)
        if m:
          t=urllib.parse.unquote(m.group(1)).replace('_',' ')
          if t not in refs: refs.append(t)
        elif u: hosts.add(re.sub(r'^www\.','',re.match(r'https?://([^/]+)',u).group(1)))
      sel=k.get('sel','')
      # drop earlier coverage sentence if rerun
      sel=re.split(r'\s*No complete list exists; follows',sel)[0].strip()
      shown=refs[:6]
      txt='Wikipedia: '+', '.join(shown)+(f' and {len(refs)-6} more' if len(refs)>6 else '') if refs else ''
      if hosts: txt+=('; ' if txt else '')+'maker and retail pages ('+', '.join(sorted(hosts)[:4])+')'
      if not txt: txt='maker pages'
      k['sel']=(sel+' ' if sel else '')+f'No complete list exists; follows {txt}.'
      n+=1
json.dump(d,open('rebuild/work/GAP_D2/D2.tmp','w'),ensure_ascii=False,indent=1)
os.replace('rebuild/work/GAP_D2/D2.tmp','rebuild/out/D2.json')
print(n)
