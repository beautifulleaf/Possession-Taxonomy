import json,re,sys
sys.path.insert(0,'.')
from names import *
d=json.load(open('/home/user/Possession-Taxonomy/rebuild/out/E4.json'))
def key(n):
  n=re.sub(r'\(.*?\)','',n.lower()); n=n.replace('sig sauer','sig').replace('čz','cz').replace('vz.','vz').replace('é','e')
  return re.sub(r'\W','',n)
have={}
for dep in d['depts']:
  for sh in dep['s']:
    for k in sh['k']:
      for e in k.get('x') or []: have[key(e['n'])]=(k['n'],e['n'])
print('PIST')
for n in sp(P1)+sp(P2):
  if key(n) not in have: print(' ',n)
print('SHOT')
for n in sp(S):
  if key(n) not in have: print(' ',n)
