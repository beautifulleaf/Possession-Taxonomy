import sys,json,re
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/DEFER_STYLE')
from util import *
P='out/H4.json'; d=load(P)
kinds={}
def f(o,p):
    if 'x' in o and 'sel' in o and o.get('n'): kinds[o['n']]=o
walk(d,f)
src=kinds['Alcohol-based perfume']
F='https://www.fragrantica.com/perfume/'
pl=json.load(open('work/DEFER_PERFUME/pl.json'))
order=['Before 1900','1900 to 1949','1950 to 1979','1980 to 1999','2000 to 2009','2010 onwards','Year not stated']
def key(x):
    try: yy=int(re.findall(r'\d{4}',x.get('y',''))[0])
    except Exception: yy=9999
    return (order.index(x['g']) if x['g'] in order else 99, yy, x['n'])
moved=[]
for name,houses,tk,fam,url in pl:
    note=''
    cand=[x for x in src['x'] if x['mk'] in houses and re.sub(r'[*]','',x['n']).replace('*',' ').strip()==name or (x['mk'] in houses and x['n'].replace('*',' ').replace('  ',' ')==name)]
    cand=[x for x in src['x'] if x['mk'] in houses and x['n'].replace('*',' ').replace('  ',' ').strip()==name]
    if len(cand)!=1: print('skip',name,len(cand)); continue
    e=cand[0]; src['x'].remove(e)
    e['d']=(f'Fragrantica states the family as {fam}. '+e.get('d','')).strip(); e['s']=url
    t=kinds[tk]['x']; pos=len(t)
    for i,x in enumerate(t):
        if key(x)>key(e): pos=i;break
    t.insert(pos,e); moved.append((tk,name))
n=len(src['x'])
src['sel']=re.sub(r'Covers \d+ of the 611',f'Covers {n} of the 611',src['sel'])
src['sel']+=f' Defer perfume round 2 (2026-10-31): {len(moved)} more placed from Fragrantica perfume pages.'
save(P,d); print(moved,n)
