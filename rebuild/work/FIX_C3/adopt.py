import json,re,collections
R='/home/user/Possession-Taxonomy/rebuild/'
c3=json.load(open(R+'out/C3.json'))
items=json.load(open(R+'work/FIX_J4/dropped_rhs_cultivars.json'))['items']
RHS='https://www.rhs.org.uk/plants/pdfs/rhs-recommended-award-of-garden-merit-fruit-veg.pdf'
M={ # j4 kind -> target C3 kind
'Apple':'Apple tree','Pear':'Pear tree','Plum':'Plum tree','Cherry':'Cherry tree','Strawberry':'Strawberry plant',
'Raspberry':'Raspberry plant','Blackberry':'Blackberry plant','Blueberry':'Blueberry bush','Blackcurrant':'Currant bush',
'Redcurrant & white currant':'Currant bush','Gooseberry':'Gooseberry bush','Table grape':'Grapevine','Rhubarb':'Rhubarb plant',
'Asparagus':'Asparagus plant','Basil':'Basil plant','Rosemary':'Rosemary','Tomato':'Tomato seed','Chilli':'Chilli & pepper seed',
'Sweet pepper':'Chilli & pepper seed','Pumpkin & winter squash':'Squash & pumpkin seed','Courgette':'Squash & pumpkin seed',
'Potato':'Seed potato','Garlic':'Seed garlic','Shallot':'Onion set','Coriander':'Herb seed','Parsley':'Herb seed','Dill':'Herb seed',
'Pea':'Bean & pea seed','Chicory':'Salad & leaf seed','Spinach':'Salad & leaf seed','Chard':'Salad & leaf seed',
'Kale':'Root & brassica seed','Kohlrabi':'Root & brassica seed','Pak choi':'Root & brassica seed','Turnip':'Root & brassica seed',
'Swede':'Root & brassica seed','Celeriac':'Root & brassica seed','Radish':'Root & brassica seed','Parsnip':'Root & brassica seed',
# new kinds
'Cabbage':'Cabbage seed','Chinese cabbage':'Cabbage seed','Cauliflower':'Cauliflower seed','Broccoli':'Broccoli seed',
'Brussels sprout':'Brussels sprout seed','Carrot':'Carrot seed','Beetroot':'Beetroot seed','Leek':'Leek seed',
'Bulb onion':'Onion seed','Spring onion':'Onion seed','Lettuce':'Lettuce seed','Cucumber':'Cucumber seed',
'Green bean':'Green bean seed','Broad bean':'Broad bean seed','Sweetcorn':'Sweetcorn seed','Aubergine':'Aubergine seed',
'Melon':'Melon seed','Celery':'Celery & fennel seed','Florence fennel':'Celery & fennel seed',
'Oregano & marjoram':'Oregano & marjoram plant','Medlar':'Medlar tree'}
NEW={ # name:(shelf, definition, aliases)
'Cabbage seed':('Seeds & cuttings','Packet of cabbage seed (Brassica oleracea Capitata group) sold for sowing; includes Chinese cabbage.','white cabbage seed · red cabbage seed · savoy seed'),
'Cauliflower seed':('Seeds & cuttings','Packet of cauliflower seed sold for sowing, by season of maturity.',''),
'Broccoli seed':('Seeds & cuttings','Packet of calabrese or sprouting broccoli seed sold for sowing.','calabrese seed'),
'Brussels sprout seed':('Seeds & cuttings','Packet of Brussels sprout seed sold for sowing.',''),
'Carrot seed':('Seeds & cuttings','Packet of carrot seed sold for sowing, by root shape and maturity.',''),
'Beetroot seed':('Seeds & cuttings','Packet of beetroot seed sold for sowing, round or long-rooted.','beet seed'),
'Leek seed':('Seeds & cuttings','Packet of leek seed sold for sowing, summer, autumn or winter types.',''),
'Onion seed':('Seeds & cuttings','Packet of bulb onion or spring onion seed sold for sowing.','spring onion seed · salad onion seed'),
'Lettuce seed':('Seeds & cuttings','Packet of lettuce seed sold for sowing, by head type.',''),
'Cucumber seed':('Seeds & cuttings','Packet of cucumber seed sold for sowing, greenhouse or ridge types.',''),
'Green bean seed':('Seeds & cuttings','Packet of runner or French bean seed sold for sowing, climbing or dwarf.','runner bean seed · French bean seed'),
'Broad bean seed':('Seeds & cuttings','Packet of broad bean seed (Vicia faba) sold for sowing, longpod or Windsor.','fava bean seed'),
'Sweetcorn seed':('Seeds & cuttings','Packet of sweetcorn seed sold for sowing.','maize seed'),
'Aubergine seed':('Seeds & cuttings','Packet of aubergine seed sold for sowing.','eggplant seed'),
'Melon seed':('Seeds & cuttings','Packet of melon seed sold for sowing.',''),
'Celery & fennel seed':('Seeds & cuttings','Packet of celery, celeriac-type or Florence fennel seed sold for sowing.',''),
'Oregano & marjoram plant':('Vegetable, herb & cannabis plants','Living oregano or marjoram plant grown for its aromatic leaves.','origanum'),
'Medlar tree':('Fruit trees','Living medlar tree (Mespilus germanica) grown for its fruit.',''),
}
loc={}
for dp in c3['depts']:
    for s in dp['s']:
        for k in s['k']:loc[k['n']]=(dp,s,k)
def norm(n):return re.sub(r"[^a-z0-9]","",n.lower())
shelves={s['n']:s for dp in c3['depts'] for s in dp['s']}
for n,(sh,d,a) in NEW.items():
    k={'n':n,'d':d,'s':RHS,'x':[]}
    if a:k['a']=a
    shelves[sh]['k'].append(k);loc[n]=(None,shelves[sh],k)
added=collections.Counter();dup=[]
for it in items:
    t=M[it['j4_kind']];k=loc[t][2]
    ex={norm(x['n']) for x in k.get('x',[])}
    a=dict(it['arch'])
    if norm(a['n']) in ex:dup.append((t,a['n']));continue
    a={kk:v for kk,v in a.items() if v not in ('',[])}
    a['d']=a['d'] if t!=it['j4_kind'] else a['d']
    k.setdefault('x',[]).append(a);added[t]+=1
json.dump(c3,open(R+'out/C3.json.tmp','w'),ensure_ascii=False,indent=1)
print(sum(added.values()),'added',len(dup),'dups',dup)
print(added)
