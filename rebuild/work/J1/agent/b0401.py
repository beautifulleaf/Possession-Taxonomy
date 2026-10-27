import json,os
W='https://en.wikipedia.org/wiki/'
def X(n,d,s,mk='',y='',a='',v=None,dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s}
    if v: x['v']=v
    if dt: x['dt']=dt
    return x
kinds=[
{'n':'Pheasant','a':'','d':'Pheasant sold whole or as any cut, wild-shot or farm-reared.','s':'https://www.finefoodspecialist.co.uk/collections/game',
 't':['whole oven-ready','in feather','brace (cock and hen)','breasts'],
 'x':[X('Common pheasant','The pheasant reared and released in great numbers for shooting in Britain and Europe; hen birds are preferred for roasting.',W+'Common_pheasant',a='ring-necked pheasant',dt='hen or cock · wild-shot or farmed · UK season from 1 October')]},
{'n':'Grouse','a':'','d':'Grouse sold whole or as any cut, wild-shot.','s':'https://swaledale.co.uk/collections/wild-british-game-meat',
 't':['whole oven-ready','in feather','breasts'],
 'x':[X('Red grouse','Moorland grouse of Britain whose season opens on the Glorious Twelfth (12 August).',W+'Glorious_Twelfth',a='Glorious Twelfth grouse',dt='young or old bird · season from 12 August'),
  X('Black grouse','Larger grouse, male called blackcock; a listed game bird but rarely shot as numbers decline.',W+'Black_grouse',a='blackcock · greyhen · blackgame'),
  X('Ptarmigan','Mountain grouse of the Highlands and the Arctic; a festive dish in Iceland.',W+'Rock_ptarmigan',a='rock ptarmigan · rjúpa')]},
{'n':'Partridge','a':'','d':'Partridge sold whole or as any cut.','s':'https://swaledale.co.uk/collections/wild-british-game-meat',
 't':['whole oven-ready','in feather','breasts'],
 'x':[X('Red-legged partridge','Partridge introduced to Britain from France in the 18th century, now reared and released for shooting.',W+'Red-legged_partridge',a='French partridge',y='18th century (Britain)'),
  X('Grey partridge','Native European partridge, a popular game bird also introduced to North America.',W+'Grey_partridge',a='Hungarian partridge · hun')]},
{'n':'Wild duck','a':'mallard · teal · wigeon','d':'Wild duck (mallard, teal, wigeon) sold whole or as any cut.','s':'https://swaledale.co.uk/collections/wild-british-game-meat',
 't':['whole oven-ready','breasts','wigeon'],
 'x':[X('Mallard','The commonest wild duck shot; breast and thigh are eaten, roasted or braised.',W+'Mallard'),
  X('Teal','Small wild duck, a UK quarry species.',W+'Eurasian_teal',a='Eurasian teal · common teal')]},
{'n':'Pigeon & squab','a':'wood pigeon · squab · pigeonneau','d':'Wild wood pigeon or farmed young pigeon (squab) sold whole or as breasts.','s':'https://www.edenmoor.com/products/wild-wood-pigeon-breasts',
 't':['wood pigeon','squab (pigeonneau)','whole','breasts'],
 'x':[X('Wood pigeon','Wild pigeon shot in millions as quarry and crop pest across Europe; leaner and tougher than squab.',W+'Common_wood_pigeon',a='woodpigeon · ring dove'),
  X('Squab','Meat of a young domestic pigeon, usually about four weeks old.',W+'Squab_(food)',a='pigeonneau')]},
{'n':'Quail','a':'','d':'Quail sold whole, spatchcocked or boned.','s':'https://www.dartagnan.com/buy/comfort-foie-gras-poultry',
 't':['whole','spatchcocked','boned'],
 'x':[X('Japanese quail','The farmed quail, raised worldwide for eggs and meat; meat strains reach about 300 g.',W+'Japanese_quail',a='coturnix quail'),
  X('Common quail','European quail, heavily hunted on migration and sometimes farmed.',W+'Common_quail',a='European quail')]},
{'n':'Guinea fowl','a':'pintade','d':'Farmed guinea fowl sold whole or as any cut.','s':'https://www.salterandking.co.uk/collections/game-meat',
 't':['whole','supremes','legs'],
 'x':[X('Helmeted guineafowl','The domesticated guinea fowl species sold in Western supermarkets.',W+'Helmeted_guineafowl',a='pintade de Numidie'),
  X('Label Rouge guinea fowl','French free-range pintade fermière from a slow-growing breed, reared at least 94 days.','https://www.tastefrance.com/french-products/meat-products/guinea-fowl-label-rouge',a='pintade fermière Label Rouge'),
  X('Pintade de Bresse','Guinea fowl raised on farms in the Bresse region of eastern France.','https://www.fineandwild.com/products/pintade-de-bresse',a='guinea fowl de Bresse')]},
]
out={'kinds':kinds,'brands':[],'traditions':[],'notes':'All seven planned kinds kept; species are archetypes, season and wild/farmed are detail or types. Wigeon kept as a type (fetched page does not confirm it as food). Woodcock and snipe left out: no fetched page shows them sold. No brands (no maker archetypes).'}
p='/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/04_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
