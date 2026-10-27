import csv,json,os
B='/home/user/Possession-Taxonomy/rebuild/work/_seg/'
C={'F':'Professional & flagship','P':'Premium','M':'Mainstream','V':'Value','H':'Heritage manufactory','A':'Artisan & independent','S':'Specialist','O':'Own-label & retailer','I':'Institution & issuer'}
rows=[l.rstrip('\n').split('\t') for l in open(B+'general_J.todo.tsv',encoding='utf-8')][1:]
d={}
for f in ['d1','d2','d3']:
    for l in open(B+'general_J_work/'+f+'.txt',encoding='utf-8'):
        l=l.strip()
        if not l: continue
        i,c,kf=l.split(' ',2)
        assert int(i) not in d,i; d[int(i)]=(C[c],kf.lower())
assert sorted(d)==list(range(1,len(rows)+1)),(len(d),len(rows))
tmp=B+'general_J.map.tsv.tmp'
with open(tmp,'w',encoding='utf-8') as o:
    o.write('name\tseg\tkf\n')
    for i,r in enumerate(rows,1): o.write(f'{r[0]}\t{d[i][0]}\t{d[i][1]}\n')
os.replace(tmp,B+'general_J.map.tsv')
