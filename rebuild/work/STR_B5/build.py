# -*- coding: utf-8 -*-
import json,sys,copy,os
sys.path.insert(0,'.')
from tt3 import TT
B='/home/user/Possession-Taxonomy/rebuild/'
old=json.load(open('bak/B5.json'))
K={}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
W='https://en.wikipedia.org/wiki/'
def NEW(n,a,d,s): return {'n':n,'a':a,'d':d,'s':W+s}
NK={
 'Karahi':NEW('Karahi','kadai · kadhai · Indian wok','Deep, round-bottomed pan with steep sides and two loop handles, from the Indian subcontinent, for frying and curries; a wok has shallower, flaring sides.','Karahi'),
 'Griddle & tawa':NEW('Griddle & tawa','comal · tava · plancha · flat-top','Broad flat plate or disc without ridges, for flatbreads, pancakes and searing; a ridged pan → Grill pan.','Griddle'),
 'Double boiler':NEW('Double boiler','bain-marie · water bath','Inner pan or bowl set over a larger pan of hot water, to heat custards, chocolate and sauces gently.','Bain-marie'),
 'Ramekin':NEW('Ramekin','soufflé dish · custard cup','Small straight-sided heatproof dish for baking and serving single portions of crème brûlée, soufflé and baked eggs.','Ramekin'),
 'Sujihiki':NEW('Sujihiki','suji-hiki · slicer','Long thin Japanese slicing knife, 240–300 mm, drawn through cooked meat and fish; the Western carving knife is its counterpart.','Japanese_kitchen_knife'),
 'Petty knife':NEW('Petty knife','petty · Japanese utility knife','Small Japanese double-bevel knife, 120–150 mm, for detail work and small produce; the counterpart of the paring and utility knife.','Japanese_kitchen_knife'),
 'Knife sharpener':{'n':'Knife sharpener','a':'pull-through sharpener · electric sharpener · sharpening system','d':'Device with fixed abrasives that restores an edge without stone skill; a loose stone → Whetstone.','s':K['Whetstone']['s']},
 'Potato masher':NEW('Potato masher','tater masher · crusher','Hand tool with a plate or wire head that crushes soft cooked food such as potatoes and beans.','Potato_masher'),
 'Garlic press':NEW('Garlic press','garlic crusher','Hand tool that forces garlic cloves through small holes to crush them.','Garlic_press'),
 'Citrus squeezer':NEW('Citrus squeezer','lemon squeezer · reamer','Hand tool that extracts juice from a halved citrus fruit by pressing or twisting it on a ridged cone or between levers.','Juicer'),
 'Salad spinner':NEW('Salad spinner','salad drier','Basket in a bowl that spins to fling the water off washed leaves.','Salad_spinner'),
 'Pastry brush':NEW('Pastry brush','basting brush','Brush for applying butter, oil, glaze or egg wash to food.','Pastry_brush'),
 'Popcorn maker':NEW('Popcorn maker','popcorn machine','Appliance that pops corn kernels with hot air or in a stirred heated pot.','Popcorn_maker'),
 'Ice maker':NEW('Ice maker','icemaker · ice machine','Stand-alone household appliance that makes ice cubes; the ice tray in a freezer is not one.','Ice_maker'),
 'Percolator':NEW('Percolator','coffee percolator · percolator pot','Pot that cycles nearly boiling water up a central tube and back through a basket of grounds, on the hob or electric.','Coffee_percolator'),
 'Milk frother':NEW('Milk frother','milk whisk · frothing wand','Tool that whips air into milk for foam, as a plunger, handheld wand or countertop machine; a steaming jug → Milk pitcher.','Milk_frother'),
 'Tea cosy':NEW('Tea cosy','tea cozy','Padded fabric cover put over a teapot to keep the tea warm.','Tea_cosy'),
 'Japanese tea caddy':NEW('Japanese tea caddy','chaki · natsume · chaire · chazutsu','Container for powdered or leaf tea in the Japanese tea ceremony: lacquered natsume, ceramic chaire or metal chazutsu.','Japanese_tea_utensils'),
 'Mizusashi':NEW('Mizusashi','fresh-water jar','Covered jar of cold water kept in the tea room to top up the kettle and rinse the bowl.','Japanese_tea_utensils'),
 'Hishaku':NEW('Hishaku','tea ladle · bamboo dipper','Bamboo dipper that ladles hot water from the kettle to the bowl and cold water from the jar.','Japanese_tea_utensils'),
 'Chafing dish':NEW('Chafing dish','buffet warmer','Metal pan on a stand heated from below, used to keep buffet food warm or cook at the table.','Chafing_dish'),
 'Toast rack':NEW('Toast rack','','Rack with upright dividers that holds slices of toast apart so they stay crisp.','Toast_rack'),
 'Freeze dryer':NEW('Freeze dryer','home freeze dryer','Household vacuum machine that freezes food and draws off its ice as vapour, for long-term dry storage.','Freeze-drying'),
 'Cookie jar':NEW('Cookie jar','biscuit barrel','Lidded pottery or glass jar that keeps biscuits and snacks on the counter.','Cookie_jar'),
 'Hip flask':NEW('Hip flask','pocket flask','Slim curved flask for carrying spirits in a pocket; a vacuum flask → Vacuum flask.','Hip_flask'),
}
NK['Double boiler']['d']=NK['Double boiler']['d']
def getk(n): return copy.deepcopy(K[n]) if n in K else copy.deepcopy(NK[n])

# archetype moves / demotions
DEMOTE={'Frying pan':['Smooth-finish heritage skillet'],'Wok':['Hand-hammered pow wok'],'Cezve':['Hand-hammered copper cezve'],'Vietnamese phin':['Traditional stainless phin'],
 'Champagne glass':['Champagne coupe','Champagne flute'],'Cocktail glass':['Martini glass'],'Spirits glass':['Snifter','Shot glass'],
 'Cruet set':['Salt cellar','Silver cruet stand'],'Serving tray':["Butler's tray"],'Tureen':['Rabbit tureen'],'Butter dish':['French butter dish'],
 'Bottling equipment':['Swing-top bottle'],'Fermenter':['Glass carboy'],'Keg and kegerator':['Kegerator'],'Sourdough tools':['Banneton','Lame'],
 'Portafilter and baskets':['Bottomless portafilter'],'Ice cream maker':['Hand-cranked ice-and-salt freezer'],'Bar spoon':['Teardrop barspoon'],
 'Lunch box':['Bento box','Tiffin carrier','Character lunch box'],'Fermentation crock':['Tsukemono-ki pickle press'],'Cutting board':['Hinoki board']}
for kn,names in DEMOTE.items():
    K[kn]['x']=[x for x in K[kn].get('x',[]) if x['n'] not in names]
demoted=sum(len(v) for v in DEMOTE.values())
# carry-over moves of archetypes between kinds
def pull(kind,pred):
    xs=[x for x in K[kind].get('x',[]) if pred(x['n'])]
    K[kind]['x']=[x for x in K[kind].get('x',[]) if not pred(x['n'])]
    return xs
japcad=pull('Tea caddy',lambda n: any(w in n for w in ('natsume','Katatsuki','Nasu','Bunrin','chazutsu')))
trizor=pull('Whetstone',lambda n:'Chef' in n)
NK['Japanese tea caddy']['x']=japcad; NK['Knife sharpener']['x']=trizor
# alias cleanups
K['Kitchen utility knife']['a']='sandwich knife · tomato knife · all-purpose knife'
K['Carving knife']['a']='slicing knife · slicer · ham knife'
K['Grill pan']['a']='ridged pan · griddle pan'
K['Crêpe pan']['a']='crepe pan · blini pan'
K['Whetstone']['a']='sharpening stone · water stone · toishi'
K['Whetstone']['d']='Abrasive stone that grinds a fresh edge on a knife, wetted with water or oil; a fixed-angle device → Knife sharpener.'
K['Grill pan']['d']='Heavy pan with a ridged surface that sears and marks food on the hob; a flat plate → Griddle & tawa.'
K['Tea caddy']['d']='Box, jar or canister for storing tea leaves, from Georgian wooden caddies to airtight tins; the Japanese ceremony caddy → Japanese tea caddy.'
K['Tea caddy']['a']='tea canister · tea chest'
K['Kitchen timer']['d']=K['Kitchen timer']['d']
K['Wine preserver']['d']='Device that keeps opened wine fresh or opens it up in the glass: vacuum pumps, inert-gas systems, stoppers and aerators.'
K['Pizza stone']['a']='baking stone · pizza steel · baking steel'
K['Pizza stone']['d']='Thick slab of cordierite, ceramic or steel preheated in the oven to crisp pizza and bread; a deep pan → Baking tray.'
K['Tea infuser and strainer']['d']=K['Tea infuser and strainer']['d']
K['Cookware set']['d']='Set of pots and pans from one maker line, sold and rated as one product.'
K['Hydration bladder']['d']='Flexible reservoir with a drinking tube for a rucksack; sport use → E2 Hydration pack.'
K['Dish rack']['d']=K['Dish rack']['d']
K['Home coffee roaster']['d']=K['Home coffee roaster']['d']

def shelf(n,t,ax,kinds):
    s={'n':n,'t':t}
    if ax: s['ax']=ax
    s['k']=[]
    for kn in kinds:
        k=getk(kn)
        tt=[[g.split(':',1)[0].strip(),[m.strip() for m in g.split(':',1)[1].split(';') if m.strip()]] for g in TT[kn].split('||')]
        k.pop('t',None); k['tt']=tt
        s['k'].append(k)
    return s
def dept(n,mode,note,t,ax,shelves): return {'n':n,'mode':mode,'note':note,'t':t,'ax':ax,'s':shelves,**({} )}
from spec import DEPTS, CAT
out={'c':'B5','rev':True,'lead':old['lead'],'ax':CAT['ax'],'key':CAT['key'],'b':old.get('b',[]),'depts':[]}
used=set()
for D in DEPTS:
    dd={'n':D['n'],'mode':D['mode'],'t':D['t'],'ax':D['ax']}
    if D.get('note'): dd['note']=D['note']
    if D.get('b'): dd['b']=D['b']
    dd['s']=[shelf(*sh) for sh in D['s']]
    out['depts'].append(dd)
    for sh in D['s']: used.update(sh[3])
od={dp['n']:dp for dp in old['depts']}
for dd in out['depts']:
    if dd['n'] in od and od[dd['n']].get('b'): dd['b']=od[dd['n']]['b']
missing=[n for n in K if n not in used]
print('kinds not placed:',missing)
# see links
from see import SEE
names={k['n'] for dp in out['depts'] for s in dp['s'] for k in s['k']}
for dp in out['depts']:
    for s in dp['s']:
        for k in s['k']:
            if k['n'] in SEE:
                k['see']=SEE[k['n']]
                for c,tn,w in k['see']:
                    if c=='B5': assert tn in names,(k['n'],tn)
                    else:
                        r=json.load(open(B+'reader/'+c+'.json'))
                        assert any(kk['n']==tn for d2 in r['depts'] for s2 in d2['s'] for kk in s2['k']),(c,tn)
json.dump(out,open('B5.new.json','w'),ensure_ascii=False,indent=1)
before=lambda d:(len(d['depts']),sum(len(x['s']) for x in d['depts']),sum(len(s['k']) for x in d['depts'] for s in x['s']),sum(len(k.get('x',[])) for x in d['depts'] for s in x['s'] for k in s['k']))
print('before',before(old),'after',before(out),'demoted',demoted)
