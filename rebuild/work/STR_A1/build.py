import json,copy,sys,re,os
sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/STR_A1')
from dsl import *
import spec_a,spec_a2,spec_b,spec_c
R='/home/user/Possession-Taxonomy/rebuild/'
old=json.load(open(R+'work/STR_A1/bak/A1.json'))
OK={}; OD={}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']: OK[k['n']]=copy.deepcopy(k); OD[k['n']]=dp['n']
ALIAS={"Fedora":"Fedora & trilby","Morning dress":"Morning dress & tailcoat","Cummerbund & collar stay":"Formal accessories","Leather & suede jacket":"Casual jacket"}
DEMOTE={
"Basketball jersey":["NBA Association, Icon, Statement and City editions"],
"Ice-hockey jersey":["NHL alternate jersey"],"Baseball jersey":["Pinstripe jersey"],
"Blouse":["Pussy-bow blouse","Peasant blouse","Sailor blouse"],
"Aran jumper":["Traditional Aran fisherman's jumper"],"Guernsey (gansey)":["Traditional Guernsey","Yorkshire coast gansey"],
"Fair Isle jumper":["Fair Isle allover jumper"],"Lopapeysa":["Lopapeysa yoke sweater"],"Cowichan sweater":["Genuine Cowichan sweater"],
"Chinos":["Military khaki chino"],"Cargo trousers":["Military combat trouser"],"Joggers":["Grey jersey sweatpant"],
"Shirt dress":["1950s shirtwaist dress"],"Slip dress":["1990s minimalist slip dress"],"Shift & A-line dress":["1920s flapper shift"],
"Sheath & bodycon dress":["1950s wiggle dress"],"Fit-and-flare & swing dress":["1950s swing dress"],"Maxi dress":["Prairie dress"],
"Evening gown & cocktail dress":["Ball gown","Cocktail dress"],"Sundress & tea dress":["1950s sundress","Tea dress"],
"Pinafore dress":["Gymslip"],"Babydoll & smock dress":["Babydoll dress"],
"Jumpsuit":["Utility jumpsuit","Catsuit","Romper / playsuit"],"Skirt":["Prairie skirt"],
"Varsity jacket":["Letterman jacket"],"Tracksuit":["Shell suit"],"Cut-off vest":["Battle jacket"],
"Business suit":["Women's trouser suit"],"Blazer":["Navy double-breasted blazer","School blazer","Tweed sport coat & hacking jacket"],
"Waistcoat":["Suit waistcoat","Odd waistcoat","Evening waistcoat"],"Tuxedo":["Double-breasted dinner jacket","White dinner jacket"],
"Morning dress & tailcoat":["Morning coat","Evening tailcoat"],
"Tie":["Knit tie"],"Ascot & cravat":["Cravat (early)"],"Bow tie":["Black-tie bow tie"],
"Beach cover-up":["Beach kaftan","Sarong wrap"],
"Fedora & trilby":["Fedora","Trilby"],"Homburg":["Homburg"],"Boater":["Straw boater"],"Top hat":["Silk top hat","Opera hat"],
"Beret":["Military beret"],"Headscarf":["Instant hijab","Kerchief"],"Scarf":["Football scarf"],
"Abaya":["Black abaya"],"Thobe":["Saudi thobe"],"Bunad":["Regional bunader"],"Vyshyvanka":["Traditional regional vyshyvanka"],
"Hanbok":["Fashion hanbok"],"Workwear":[],
}
MOVE=[("Casual jacket","Pendleton 49er","Overshirt"),("Cardigan","Cowichan-style shawl-collar cardigan","Cowichan sweater")]
demoted=[]
for k,names in DEMOTE.items():
    if k not in OK: 
        if names: print('DEMOTE missing kind',k)
        continue
    keep=[]
    for x in OK[k].get('x',[]):
        if x['n'] in names: demoted.append((k,x['n']))
        else: keep.append(x)
    miss=[n for n in names if n not in [d[1] for d in demoted if d[0]==k]]
    if miss: print('DEMOTE missing arch',k,miss)
    OK[k]['x']=keep
for fr,a,to in MOVE:
    xs=OK[fr]['x']; i=[j for j,x in enumerate(xs) if x['n']==a]
    if not i: print('MOVE missing',a); continue
    OK[to].setdefault('x',[]).append(xs.pop(i[0]))
EXTRA_TAKE={"Bandana":{"Scarf":["Paisley bandana"]}}
used=set(); allnew=[]; moved_new=[]
def mkkind(item):
    if item['kind']=='old':
        key=ALIAS.get(item['old'],item['old'])
        if key not in OK: print('MISSING old',item['old']); return None
        k=OK[key]; used.add(key)
        if item['ren']: k['n']=item['ren']
        if item['d']: k['d']=item['d']
        if item['a']: k['a']=item['a']
        k.pop('t',None); k['tt']=item['tt']
        if item['see']: k['see']=item['see']
        return k
    take=dict(item['take']); take.update(EXTRA_TAKE.get(item['n'],{}))
    x=[]; s=item['s']; inh=None
    for ok,names in take.items():
        ok=ALIAS.get(ok,ok)
        src=OK[ok]; inh=inh or src.get('s')
        for nm in names:
            j=[i for i,a in enumerate(src.get('x',[])) if a['n']==nm]
            if not j: print('TAKE missing',nm,'in',ok); continue
            x.append(src['x'].pop(j[0]))
    if not s: s=(x[0]['s'] if x and False else None) or inh
    k=dict(n=item['n'],a=item['a'],d=item['d'],tt=item['tt'],s=s)
    if x: k['x']=x
    if item['see']: k['see']=item['see']
    allnew.append(k['n'])
    return k
def shelf(sh,pool):
    ks=[]
    for it in sh['k']:
        if isinstance(it,str): it=pool[it]
        k=mkkind(it)
        if k: ks.append(k)
    return dict(n=sh['n'],t=sh['t'],ax=sh['ax'],k=ks)
pool={}; pool.update(spec_a2.JEANS); pool.update(spec_a.SKIRT_KINDS)
specs=spec_a.DEPTS_A+spec_a2.DEPTS_B+spec_b.DEPTS_C+spec_c.DEPTS_D
bymap={d['n']:d for d in specs}
order=["Tops","Trousers, jeans & shorts","Dresses","Skirts, jumpsuits & sets","Coats & jackets","Suits & formalwear","Underwear, nightwear & swim","Hats & headwear","Scarves, gloves & belts","Traditional dress","Workwear & uniform clothing"]
oldb={dp['n']:dp.get('b') for dp in old['depts']}
bsrc={"Tops":"Tops","Trousers, jeans & shorts":"Trousers, jeans & shorts","Dresses":"Dresses, skirts & sets","Skirts, jumpsuits & sets":"Dresses, skirts & sets","Coats & jackets":"Coats & jackets","Suits & formalwear":"Suits & formalwear","Underwear, nightwear & swim":"Underwear, nightwear & swim","Hats & headwear":"Hats, scarves & accessories","Scarves, gloves & belts":"Hats, scarves & accessories","Traditional dress":"Traditional dress","Workwear & uniform clothing":"Workwear & uniform clothing"}
# tweaks
bymap["Traditional dress"]['s'][4]['ax']="kinds by region, from West Africa to the Horn, the Nile and the south"
depts=[]
for n in order:
    d=bymap[n]
    out=dict(n=n,mode=d['mode'],note=d['note'],t=d['t'],ax=d['ax'])
    b=oldb.get(bsrc[n]); 
    if b: out['b']=copy.deepcopy(b)
    out['s']=[shelf(sh,pool) for sh in d['s']]
    depts.append(out)

# carry leftover m/r
JB={'The Real McCoy\'s','Mister Freedom','ONI Denim','Burgus Plus','Edwin','Big John','orSlow','Naked & Famous Denim','3sixteen','Tellason','Benzak','Indigofera'}
JC={'Diesel','True Religion','Fashion Box','AMIRI','KSENIASCHNAIDER'}
def find(n):
    for d in depts:
        for sh in d['s']:
            for k in sh['k']:
                if k['n']==n: return k
tgt={'A':find('Heritage American jeans'),'B':find('Selvedge reproduction jeans'),'C':find('Fashion & designer jeans')}
for key in('m','r'):
    for e in OK['Jeans'].get(key,[]):
        t='B' if e[1] in JB else 'C' if e[1] in JC else 'A'
        tgt[t].setdefault(key,[]).append(e)
find('A-line skirt').setdefault('m',[]).extend([['Bel Skirt','Elizabeth Suzann']])
find('Circle & poodle skirt').setdefault('m',[]).extend([['Viva 40s tulip skirt','Pinup Girl Clothing']]); find('Circle & poodle skirt').setdefault('r',[]).extend([['Pinup Couture','Pinup Girl Clothing']])
# leftovers
left=[k for k in OK if k not in used]
print('UNPLACED OLD KINDS:',left)
for k in left:
    print(k,'m',OK[k].get('m'),'r',OK[k].get('r'),'x left',[x['n'] for x in OK[k].get('x',[])])
json.dump(dict(depts=depts,demoted=demoted,allnew=allnew,left=left),open(R+'work/STR_A1/stage.json','w'),ensure_ascii=False)
