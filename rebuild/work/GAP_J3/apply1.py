import json,re,unicodedata,os
exec(open('adds.py').read())
def nz(s):
  s=unicodedata.normalize('NFKD',s.lower());s=''.join(c for c in s if not unicodedata.combining(c))
  s=re.sub(r'\b(pdo|pgi|pat|aop|aoc|tsg|cheese|kase|di|del|della|de|du|des|le|la)\b','',s)
  return re.sub(r'[^a-z0-9]','',s)
P='../../out/J3.json'
d=json.load(open(P))
kinds={};have={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      kinds[k['n']]=k
      for e in k.get('x',[]):
        for n in [e['n']]+[a for a in re.split(r'\s*·\s*',e.get('a','')) if a]: have[nz(n)]=e['n']
        for v in e.get('v',[]): have.setdefault(nz(v['n']),e['n'])
skip=[];add=0;seen=set()
for n,k,dd,s in A:
  if k not in kinds: print('NOKIND',k,n);continue
  key=nz(n)
  if key in have or key in seen: skip.append((n,have.get(key)));continue
  seen.add(key)
  kinds[k].setdefault('x',[]).append({'n':n,'a':'','d':dd,'mk':'','y':'','s':s,'v':[],'dt':''})
  add+=1
print('added',add,'skipped',len(skip));print(skip)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'.tmp',P)
