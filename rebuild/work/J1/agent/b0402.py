import json,os
W='https://en.wikipedia.org/wiki/'
def X(n,d,s,mk='',y='',a='',v=None,dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s}
    if v: x['v']=v
    if dt: x['dt']=dt
    return x
kinds=[
{'n':'Rabbit','a':'','d':'Rabbit sold whole or jointed, or as saddle or legs, farmed or wild.','s':'https://www.dartagnan.com/buy/meat-game',
 't':['whole','jointed','saddle','legs'],
 'x':[X('Farmed rabbit','Meat of domestic rabbits bred for meat; most rabbit eaten worldwide, led by China, Italy, France and Spain.',W+'Rabbit_as_food',dt='whole, jointed, saddle or legs'),
  X('Wild rabbit','Wild European rabbit hunted as game; a small share of rabbit eaten.',W+'Rabbit_as_food',dt='whole in fur or oven-ready, jointed')]},
{'n':'Hare','a':'','d':'Hare sold whole or as any cut.','s':'https://curtispittsdeerservices.co.uk/product/whole-wild-hare/',
 't':['whole in fur','oven-ready','saddle','legs'],
 'x':[X('Brown hare','European hare, the main game mammal of Europe; darker and stronger than rabbit, classically jugged.',W+'European_hare',a='European hare · lièvre · Hase'),
  X('Mountain hare','Upland hare of the Scottish Highlands, long shot on grouse moors; protected in Scotland since 2020.',W+'Mountain_hare',a='blue hare · white hare')]},
{'n':'Wild boar','a':'','d':'Wild boar sold whole or as any cut, wild-shot or farmed.','s':'https://www.wildmeat.co.uk/collections/game-meat',
 't':['wild-shot','farmed','leg','shoulder','loin','rack'],
 'x':[X('European wild boar','Hunted big-game animal and ancestor of the domestic pig; meat comes from hunted and farmed animals.',W+'Wild_boar',a='sanglier · cinghiale · Wildschwein')]},
{'n':'Squirrel','a':'','d':'Squirrel meat sold whole or jointed to eat.','s':'https://www.wildmeat.co.uk/products/squirrel',
 'x':[X('Grey squirrel','Invasive grey squirrel culled in Britain and sold occasionally for meat; also hunted for food in North America.',W+'Eastern_gray_squirrel',a='eastern gray squirrel')]},
]
out={'kinds':kinds,'brands':[],'traditions':[],'notes':'All four planned kinds kept; rabbit, rabbit saddle and rabbit leg merged into Rabbit with types. Species and wild/farmed as archetypes. No brands (no maker archetypes).'}
p='/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/04_02.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
