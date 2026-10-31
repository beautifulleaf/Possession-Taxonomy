import sys,re,json,copy
sys.path.insert(0,'work/DEFER_STYLE')
from util import *
def kinds(d):
    out={}
    walk(d,lambda o,p: out.__setitem__(o['n'],o) if 'x' in o and o.get('n') and isinstance(o['x'],list) else None)
    return out
def parent_list(d,kn):
    res=[]
    def f(o,p):
        if isinstance(o.get('k'),list) and any(x.get('n')==kn for x in o['k']): res.append(o['k'])
    walk(d,f); return res[0]
# A2 Consul
P='out/A2.json'; d=load(P); K=kinds(d); ox=K['Oxford']['x']
e={"n":"Church's Consul","d":"Classic cap-toe Oxford on the 173 last, created in 1945 and named after the British ambassadors and politicians who wore it.","mk":"Church's","y":"1945","s":"https://www.pradagroup.com/en/news-media/news-section/churchs-consul-anniversary-edition.html","v":[],"g":"United Kingdom · Church's","own":"Prada","tier":"Independent","cty":"United Kingdom","own_y":"1999"}
i=[j for j,x in enumerate(ox) if x['g']=='United Kingdom · John Lobb'][-1]; ox.insert(i+1,e)
K['Oxford']['sel']+=" Defer pass 2026-10-31: Church's Consul added from the Prada Group news page; the Alden 990 plain-toe blucher page stayed unreadable (403)."
save(P,d)
# A3
P='out/A3.json'; d=load(P); K=kinds(d); sw=K['Swarovski jewellery lines']['x']
S='https://www.swarovski.com/en-SE/s-swarovski-hero-families'
for n in ['Idyllia','Dulcis','Chroma','Gema','Imber','Ariana Grande x Swarovski']:
    sw.append({"n":n,"mk":"Swarovski","s":S,"v":[],"g":"Named in the shop menu","own":"Swarovski","tier":"Global group","cty":"Austria"})
k=K['Swarovski jewellery lines']
k['sel']=k['sel'].replace('so other lines are missing.','so other lines are missing. Defer pass 2026-10-31: the Swedish hero-families page was read; it names Millenia, Matrix, Lucent and Constella as hero families and lists Idyllia, Dulcis, Chroma, Gema, Imber and the Ariana Grande capsule in its jewellery menu (the Florere, Minecraft and Rosenthal lines are home décor or licences and are left out). Dextera and the Atelier label are not on that page.')
src=K['Boucheron jewellery lines']; nk=copy.deepcopy(src)
nk.update({'n':'Dior jewellery lines','d':'Paris house founded by Christian Dior; its fashion jewellery includes the Tribales earrings.','s':'https://www.dior.com/en_us/fashion/products/E1038TRICY_D03S','nl':'One entry is a Dior jewellery line.','sel':'Dior US product page for the Tribales earrings (the Finnish collection page timed out twice); the page lists no other line. Complete: 1 of 1 line on the page read.','xg':'single section'})
nk['x']=[{"n":"Tribales","d":"Asymmetric earrings with two white resin pearls, one carrying a star and the other the CD initials, made in Germany; front and back can be mixed with other Tribales pieces.","mk":"Dior","s":"https://www.dior.com/en_us/fashion/products/E1038TRICY_D03S","v":[],"g":"On the product page","tier":"Global group","cty":"France"}]
for key in list(nk):
    if key in('own',): pass
lst=parent_list(d,'Boucheron jewellery lines'); i=[j for j,x in enumerate(lst) if x['n']=='Boucheron jewellery lines'][0]; lst.insert(i+1,nk)
save(P,d)
b=load('out/A3_brands.json')
for x in b['b']:
    if x['n']=='Dior': print('Dior brand',x)
# A4
P='out/A4.json'; d=load(P); K=kinds(d)
for k in K.values():
    for e in k['x']:
        if e.get('mk')=='Fendi' and e['n']=='Fendi Kan I':
            e['d']="Rectangular bag with a top flap and a shoulder or crossbody strap, launched in Fendi's Runway 2017 collection and made in dozens of colours and versions."; e['s']='https://www.purseblog.com/fendi/does-fendis-kan-i-collection-have-the-power-to-become-a-classic/'
        if e.get('mk')=='Marc Jacobs':
            e['own']='WHP Global and G-III Apparel Group (50/50 joint venture)'; e['tier']='Independent'; e['own_y']='2026'
LV=dict(own="LVMH",tier="Global group",cty="France",own_y="1987")
def lv(n,g,d_,s='https://us.louisvuitton.com/eng-us/women/handbags'):
    return dict({"n":n,"a":"","d":d_,"mk":"Louis Vuitton","y":"","s":s,"v":[],"dt":"","g":"France · Louis Vuitton"},**LV)
def add_lv(kn,es):
    x=K[kn]['x']; names={e['n'] for e in x}
    idx=[i for i,e in enumerate(x) if e.get('mk')=='Louis Vuitton']
    for e in es:
        if e['n'] not in names: x.insert(idx[-1]+1,e); idx.append(idx[-1]+1)
add_lv('Shoulder bag',[lv('Diane','', 'Listed on the Louis Vuitton US women\'s handbag page.'),lv('Boulogne','', 'Listed on the Louis Vuitton US women\'s handbag page, with a Nano Boulogne size.'),lv('Squire','', 'Listed on the Louis Vuitton US women\'s handbag page, also in an East-West shape.'),lv('Frivole','', 'Listed on the Louis Vuitton US women\'s handbag page as Nano Frivole.')])
add_lv('Pochette',[lv('Pochette Mia','', 'Listed on the Louis Vuitton US women\'s handbag page.'),lv('Vanity Pouch Trunk','', 'Listed on the Louis Vuitton US women\'s handbag page.')])
for k in K.values():
    for e in k['x']:
        if e.get('mk')=='Louis Vuitton':
            add={'Speedy':['Speedy Bandoulière 20','Speedy Bandoulière 25','Nano Speedy','Speedy Soft 30 Crafty'],'Neverfull':['Neverfull Inside Out'],'Alma':['Alma BB'],'Madeleine':['Nano Madeleine']}.get(e['n'])
            if add:
                have={v['n'] for v in e.get('v',[])}
                for a in add:
                    if a not in have: e.setdefault('v',[]).append({"n":a,"mk":"Louis Vuitton","y":"","d":"size or style listed on the US handbag page"})
K['Shoulder bag']['sel']+=' Defer pass 2026-10-31: the Louis Vuitton US women\'s handbag page was read (its first rows only; the full list is script-loaded) and its missing lines added.'
save(P,d)
b=load('out/A4_brands.json')
for x in b['b']:
    if x['n']=='Marc Jacobs':
        x.update({'f':'1984','d':'Fashion house founded in 1984 by Marc Jacobs and Robert Duffy; LVMH agreed in 2026 to sell it to a 50/50 joint venture of WHP Global and G-III Apparel Group, reported at $850 million.','own':'WHP Global and G-III Apparel Group (50/50 joint venture)','tier':'Independent','own_y':'2026','s':'https://chainstoreage.com/whp-global-deal-acquire-marc-jacobs'})
save('out/A4_brands.json',b)
# A5 Max Bill clock
P='out/A5.json'; d=load(P); K=kinds(d)
for e in K['Design clock']['x']:
    if e['n'].startswith('Max Bill wall clock'): print('A5 clock',json.dumps(e,ensure_ascii=False)[:400])
