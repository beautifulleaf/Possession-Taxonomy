import csv,json
B='/home/user/Possession-Taxonomy/rebuild/work/_seg/'
ab={'PF':'Professional & flagship','P':'Premium','M':'Mainstream','V':'Value','H':'Heritage manufactory','A':'Artisan & independent','S':'Specialist','O':'Own-label & retailer','I':'Institution & issuer'}
rows=list(csv.reader(open(B+'general_B.todo.tsv',encoding='utf-8'),delimiter='\t'))[1:]
d={}
for f in ['d1','d2','d3']:
  for line in open(B+'general_B_work/'+f+'.txt',encoding='utf-8'):
    line=line.strip()
    if not line: continue
    i,s,k=line.split('|'); i=int(i)
    assert i not in d,i; d[i]=(ab[s],k.lower())
assert set(d)==set(range(1,len(rows)+1)),(len(d),len(rows))
tmp=B+'general_B.map.tsv.tmp'
with open(tmp,'w',encoding='utf-8',newline='') as o:
  o.write('name\tseg\tkf\n')
  for i,r in enumerate(rows,1): o.write(f'{r[0]}\t{d[i][0]}\t{d[i][1]}\n')
import os; os.replace(tmp,B+'general_B.map.tsv')
