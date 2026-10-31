import json,os,re,collections,urllib.parse
P='/home/user/Possession-Taxonomy/rebuild/out/E3.json'
d=json.load(open(P))
def title(u):
    m=re.match(r'https?://en\.wikipedia\.org/wiki/(.+)',u)
    if m: return 'Wikipedia: '+urllib.parse.unquote(m.group(1)).replace('_',' ').split('#')[0]
    if 'query.wikidata' in u: return 'Wikidata query'
    return re.sub(r'^www\.','',urllib.parse.urlparse(u).netloc)
n=0
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      x=k.get('x',[])
      if not x: continue
      sel=k.get('sel','')
      sel=re.sub(r'\s*(Covers \d+ entries \(.*?\)(;[^.]*\.|\.)?)','',sel)
      sel=re.sub(r'[;,]?\s*covers \d+ entries\.?','',sel)
      sel=re.sub(r'\s*(No complete list exists;[^.]*\.|Complete: \d+ of \d+[^.]*\.|Covers \d+ of about[^.]*\.)\s*$','',sel).rstrip()
      if sel and not sel.endswith('.'): sel+='.'
      c=collections.Counter()
      for e in x:
          for s in [e.get('s')]+[v.get('s') for v in e.get('v',[]) if isinstance(v,dict)]:
              if s: c[title(s)]+=1
      refs=[t for t,_ in c.most_common()]
      shown=refs[:6]; rest=len(refs)-len(shown)
      txt=', '.join(shown)+(f' and {rest} other pages' if rest>0 else '')
      sel=(sel+' ' if sel else '')+f'No complete list exists; follows {txt} ({len(x)} entries).'
      k['sel']=sel; n+=1
print(n)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'.tmp',P)
