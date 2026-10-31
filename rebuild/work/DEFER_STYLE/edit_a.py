import sys,re,json,copy
sys.path.insert(0,'work/DEFER_STYLE')
from util import *
def kinds(d):
    out={}
    walk(d,lambda o,p: out.__setitem__(o['n'],o) if 'x' in o and o.get('n') and isinstance(o['x'],list) else None)
    return out
def ins_after(lst,after_n,e):
    for i,x in enumerate(lst):
        if x['n']==after_n: lst.insert(i+1,e); return
    lst.append(e)
# ---------- A1
P='out/A1.json'; d=load(P); K=kinds(d)
mm='https://brand.maxmara.com/p-1016056106068-ludmilla-camel'
ins_after(K['Overcoat']['x'],'Max Mara Teddy Bear coat',{"n":"Max Mara Ludmilla","a":"Ludmilla Icon Coat","d":"Belted camel coat with a generous, enveloping silhouette; reinterpreted in 2016 and reissued in every Max Mara collection since.","mk":"Max Mara","y":"2016","s":mm,"v":[{"n":"Ludmilla Icon Coat","mk":"Max Mara","y":"2016","d":"Camel, tobacco, black and sand"}],"dt":"belted · camel, tobacco, black, sand","g":"Italy","cty":"Italy"})
K['Overcoat']['sel']+=' Defer pass 2026-10-31: Ludmilla restored from the Max Mara product page.'
def bump(k):
    m=re.search(r'Complete: (\d+) of (\d+) brand pieces',k['sel'])
    if m: k['sel']=k['sel'].replace(m.group(0),f'Complete: {int(m.group(1))+1} of {int(m.group(2))+1} brand pieces')
ins_after(K['Puffer jacket']['x'],'__end__',{"n":"Mountain Hardwear Ghost Whisperer","a":"Ghost Whisperer Down Jacket","d":"Ultralight 800-fill goose down jacket sold as a sustainable reimagining of the maker's best-selling ultralight down jacket; the men's jacket weighs 8 oz (226 g) with 2.6 oz of insulation.","mk":"Mountain Hardwear","y":"","s":"https://www.mountainhardwear.com/p/mens-ghost-whisperer-jacket-2104461_S.html","v":[],"dt":"800-fill goose down · Responsible Down Standard · light DWR coating","g":"Country not stated","own":"Columbia Sportswear","tier":"Global group","own_y":"2003"})
bump(K['Puffer jacket'])
ins_after(K['Shell jacket']['x'],'__end__',{"n":"Black Diamond Fineline Stretch Shell","a":"Fineline Stretch Shell","d":"Two-and-a-half-layer BD.dry waterproof, breathable stretch shell with pit zips and a helmet-compatible hood; 10 oz (283.5 g) in men's medium, in 50-denier fabric.","mk":"Black Diamond","y":"","s":"https://thebigoutside.com/review-black-diamond-fineline-stretch-shell-and-pants","v":[],"dt":"BD.dry 2.5L · stretch face fabric · packs into its pocket","g":"Country not stated"})
bump(K['Shell jacket'])
K['Shell jacket']['sel']+=' Defer pass 2026-10-31: Fineline and Ghost Whisperer restored; the Supreme Crest Coaches Jacket has no page (Supreme FW2025 preview lists only the Old English Arc Coaches Jacket).'
save(P,d)
B='out/A1_brands.json'; b=load(B)
for x in b['b']:
    if x['n']=='Rapsodia':
        x['d']='Argentine fashion group, renamed Grupo Alas in 2019; owns Rapsodia, Rapsodia Girls, Caro Cuore and Baby Cottons, with L Catterton as investor since February 2017.'
        x['own']='Grupo Alas (De Narváez group and L Catterton)'; x['own_y']='2017'
        x['s']='https://www.modaes.com/empresa/rapsodia-se-convierte-en-grupo-alas-y-acelera-hasta-doscientos-millones-con-todas-sus-marcas'
if not any(x['n']=='Black Diamond' for x in b['b']):
    b['b'].append({"n":"Black Diamond","seg":"Outdoor & technical","kf":"climbing and shell clothing","rel":[]})
save(B,b)
# ---------- A2
P='out/A2.json'; d=load(P); K=kinds(d)
for k in K.values():
    for e in k['x']:
        if e.get('mk')=='La Sportiva':
            e['own']='Lorenzo Delladio'; e['tier']='Independent'; e['own_y']='2017'; e['cty']='Italy'
ox=K['Oxford']; print('Oxford xg',ox['xg'],[ (e['n'],e.get('g')) for e in ox['x']][:8]); print(json.dumps([e for e in ox['x'] if e.get('own')][0],ensure_ascii=False)[:500])
save('/tmp/none','x') if False else None
save(P,d)
B='out/A2_brands.json'; b=load(B)
for x in b['b']:
    if x['n']=='La Sportiva':
        x.update({'d':'Italian climbing and mountain-footwear maker founded by Narciso Delladio in the Dolomites; Lorenzo Delladio became sole owner in 2017.','own':'Lorenzo Delladio','tier':'Independent','own_y':'2017','s':'https://www.lasportiva.com/en/company'})
    if x['n']=="Church's":
        x['d']="Northampton shoemaker founded by the Church family; Prada bought it in 1999, sold 55 % to Equinox in 2003 and bought that stake back in 2006."
        x['s']='https://www.wwd.com/business-news/financial/feature/prada-buys-back-church-s-stake-512765-2017923'
save(B,b)
