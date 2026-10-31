import json,re,unicodedata
def nz(s):
    s=unicodedata.normalize('NFKD',s.lower());s=''.join(c for c in s if not unicodedata.combining(c))
    s=re.sub(r'\b(pdo|pgi|aop|aoc|dop|igp|tsg|gi|cheese|queso|queijo|formaggio|fromage)\b',' ',s)
    return ' '.join(re.sub(r'[^a-z0-9 ]',' ',s).split())
def existing(d):
    S={}
    for dp in d['depts']:
      for s in dp['s']:
        for k in s['k']:
          for x in k.get('x',[]):
            for a in [x['n']]+[t for t in re.split(r'\s*[·;]\s*',x.get('a','')) if t]+[v['n'] for v in x.get('v',[])]:
              S.setdefault(nz(a),(k['n'],x['n']))
    return S
