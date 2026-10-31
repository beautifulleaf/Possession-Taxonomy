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
pl=[
('Alien',['Thierry Mugler'],'Amber fragrance','Oriental Woody',F+'Mugler/Alien-707.html'),
('Mugler Cologne',['Thierry Mugler'],'Citrus & eau de cologne','Citrus Aromatic',F+'Mugler/Mugler-Cologne-708.html'),
('B Men',['Thierry Mugler'],'Amber fragrance','Oriental Woody',F+'Mugler/B-Men-706.html'),
('Ice Men',['Thierry Mugler'],'Woody fragrance','Woody Aromatic',F+'Mugler/Ice-Men-1347.html'),
('Her',['Burberry'],'Floral fragrance','Floral Fruity Gourmand',F+'Burberry/Burberry-Her-51694.html'),
('Allure Sensuelle',['Chanel'],'Amber fragrance','Oriental Floral',F+'Chanel/Allure-Sensuelle-606.html'),
('Kenzo World',['Kenzo'],'Floral fragrance','Floral',F+'Kenzo/Kenzo-World-40278.html'),
('Armani Code',['Armani'],'Amber fragrance','Oriental Spicy',F+'Giorgio-Armani/Armani-Code-412.html'),
('Fleur du Male',['Jean Paul Gaultier'],'Fougère fragrance','Aromatic Fougère (Portuguese label Aromático Fougère)','https://www.fragrantica.com.br/perfume/Jean-Paul-Gaultier/Fleur-du-Male-2007-889.html'),
]
order=['Before 1900','1900 to 1949','1950 to 1979','1980 to 1999','2000 to 2009','2010 onwards','Year not stated']
def key(x):
    try: yy=int(re.findall(r'\d{4}',x.get('y',''))[0])
    except Exception: yy=9999
    return (order.index(x['g']) if x['g'] in order else 99, yy, x['n'])
moved=[]
for name,houses,tk,fam,url in pl:
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
src['sel']+=f' Defer perfume pass 2026-10-31: {len(moved)} more placed from Fragrantica perfume pages (Mugler, Burberry, Chanel, Kenzo, Armani, Jean Paul Gaultier); the free tier returns about five search hits per call, so the rest remain unplaced.'
save(P,d); print(moved,n)
