import sys,json,re
sys.path.insert(0,'work/DEFER_STYLE')
from util import *
def apply(placements, urlmap, src_label='Fragrantica'):
    """placements: list of (house_names, perfume name, targetKind, familyText, url, fy)"""
    P='out/H4.json'; d=load(P)
    kinds={}
    def f(o,p):
        if 'x' in o and 'sel' in o and o.get('n'): kinds[o['n']]=o
    walk(d,f)
    src=kinds['Alcohol-based perfume']
    moved=0
    for houses,name,tk,fam,url,fy in placements:
        e=[x for x in src['x'] if x['n']==name and x['mk'] in houses]
        if len(e)!=1: print('skip',name,len(e)); continue
        e=e[0]; src['x'].remove(e)
        e['d']=(f'{src_label} states the family as {fam}. '+e.get('d','')).strip()
        e['s']=url
        tgt=kinds[tk]['x']
        # insert by g order then year then name
        order=['Before 1900','1900 to 1949','1950 to 1979','1980 to 1999','2000 to 2009','2010 onwards','Year not stated']
        def key(x): 
            try: yy=int(re.findall(r'\d{4}',x.get('y',''))[0])
            except Exception: yy=9999
            return (order.index(x['g']) if x['g'] in order else 99, yy, x['n'])
        pos=len(tgt)
        for i,x in enumerate(tgt):
            if key(x)>key(e): pos=i;break
        tgt.insert(pos,e); moved+=1
    n=len(src['x'])
    m=re.search(r'Covers (\d+) of the 611',src['sel'])
    if m: src['sel']=src['sel'].replace(m.group(0),f'Covers {n} of the 611')
    src['sel']+=f' Defer pass 2026-10-31: {moved} more placed from {src_label} perfume pages (Guerlain and Tom Ford houses); the rest still state no family on a fetched page.'
    save(P,d); print('moved',moved,'left',n)
