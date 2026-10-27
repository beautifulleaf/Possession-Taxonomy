import json,os
W='https://en.wikipedia.org/wiki/'
def X(n,d,s,mk='',y='',a='',v=None,dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s}
    if v: x['v']=v
    if dt: x['dt']=dt
    return x
def V(n,d='',mk='',y=''): return {'n':n,'mk':mk,'y':y,'d':d}
kinds=[
{'n':'Jerky','a':'dried meat strips','d':'Lean meat cut into strips, seasoned and dehydrated, sold to eat as it is.','s':'https://thejerkyco.com.au/products/droewors-traditional',
 't':['beef','turkey','pork','game','smoked','marinated','sticks','slabs'],
 'x':[X('American jerky','Marinated or spice-rubbed meat strips heat-dried or smoked at low heat, often sweetened; Link Snacks (Jack Link\'s) leads North America.',W+'Jerky',dt='beef, turkey, game · flavour · sliced or chopped-and-formed'),
  X('Charqui','Andean dried salted meat of llama or alpaca from Peru, Bolivia and Chile; origin of the word jerky.',W+'Charqui',a="ch'arki · charque",v=[V('Brazilian charque','beef, industrialised in charqueadas')]),
  X('Kilishi','Hausa sun-dried beef strips dipped in a spiced groundnut paste (labu); Niger, Nigeria, Cameroon, Chad.',W+'Kilishi')]},
{'n':'Biltong & droëwors','a':'biltong · droewors · dry wors','d':'Southern African air-dried meat: vinegar- and coriander-cured strips (biltong) or thin dried sausage (droëwors).','s':W+'Biltong',
 't':['beef','game','ostrich','sliced','sticks','chilli'],
 'x':[X('Biltong','Thick strips of beef or game cured with vinegar, salt, pepper and coriander, air-dried slowly and rarely smoked.',W+'Biltong',dt='beef, kudu, springbok, wildebeest, ostrich · wet or dry · sliced or whole'),
  X('Droëwors','Thin dried sausage of beef and mutton fat seasoned with coriander, from the boerewors tradition.',W+'Droëwors',a='dry sausage')]},
{'n':'Bakkwa','a':'rougan · Chinese dried meat','d':'Chinese salty-sweet dried meat in thin sheets, seasoned with sugar, salt and soy sauce.','s':W+'Bakkwa',
 't':['pork','beef','chilli','sliced','minced'],
 'x':[X('Singapore-Malaysian bakkwa','Sweeter sheets air-dried then grilled over charcoal, eaten at Chinese New Year.',W+'Bakkwa',
        v=[V('Gourmet Bakkwa','','Bee Cheng Hiang','2003'),V('Chilli Gourmet Bakkwa','','Bee Cheng Hiang','2005')]),
  X('Fujian rougan','Rack-dried pork, beef or mutton sheets of Fujian origin.',W+'Bakkwa'),
  X('Shafu bakkwa','Softer style with more moisture and less sugar.',W+'Bakkwa')]},
{'n':'Pickled or fermented meat','a':'pickled chicken feet · nem','d':'Meat preserved by pickling in vinegar or brine, or by lactic fermentation, outside a sausage casing.','s':'https://www.weee.com/en/grocery-near-me/lang-en/explore/nem-chua',
 'x':[X('Nem chua','Vietnamese sweet-sour fermented pork with rind, garlic and chilli, leaf-wrapped; from Thanh Hoá.',W+'Nem_chua',v=[V('Nem chua','old data')]),
  X('Pickled meat snacks','US jarred offal in vinegar brine: pigs\' feet, gizzards, ears, lips, plus pickled sausage.',"https://en.wikipedia.org/wiki/Pickled_pigs'_feet",a="pickled pigs' feet",dt='feet, gizzards, ears, rinds, tails · red-dyed brine')]},
]
brands=[
{'n':'Bee Cheng Hiang','c':'Singapore','f':'1933','seg':'Heritage manufactory','kf':'bakkwa','d':'Singapore bakkwa maker that began as a market stall, with outlets in 13 territories.','sig':['Singapore-Malaysian bakkwa'],'s':W+'Bee_Cheng_Hiang'},
{'n':"Jack Link's",'c':'United States','seg':'Mainstream','kf':'jerky','d':'Jerky brand of Link Snacks, the largest North American jerky producer.','sig':['American jerky'],'s':W+'Jerky'},
]
out={'kinds':kinds,'brands':brands,'traditions':[],'notes':'Old Jerky kept (biltong alias moved to new kind Biltong & droëwors); new kinds Biltong & droëwors and Bakkwa sourced from Wikipedia. Thai naem left to the sausages shelf (it is a sausage). Carne seca/carne de sol not added (not described on retrieved pages).'}
p='/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/05_03.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
