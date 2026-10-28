import json,copy
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'J4.json'))
KEEP={'Apple':{'Discovery','Worcester Pearmain','Egremont Russet',"Ashmead's Kernel",'Blenheim Orange','James Grieve'},
'Pear':{'Concorde','Beurré Hardy'},'Plum':{'Cambridge Gage'},'Potato':{'Red Duke of York','Picasso'},
'Tomato':{'Marmande'},'Chilli':{'Hungarian Hot Wax','Fresno'},'Sweet pepper':{'Corno di Toro Rosso'},
'Pumpkin & winter squash':{'Crown Prince','Harlequin','Sweet Dumpling'},'Cabbage':{'Hispi'},
'Radish':{'French Breakfast 4 (Francis)'},'Chard':{'Bright Lights'},'Broad bean':{'Aquadulce Claudia'},
'Kale':{'Redbor'},'Garlic':{'Solent Wight'}}
removed=0;before=sum(len(k.get('x',[])) for dp in d['depts'] for s in dp['s'] for k in s['k'])
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if 'x' in k:
        nx=[]
        for a in k['x']:
          if 'rhs.org.uk' in a.get('s','') and a['n'] not in KEEP.get(k['n'],()): removed+=1
          else: nx.append(a)
        k['x']=nx
        if not nx: del k['x']
def kinds():
  for dp in d['depts']:
    for s in dp['s']:
      for k in s['k']: yield dp,s,k
def get(n):
  for dp,s,k in kinds():
    if k['n']==n: return k
def shelf(dept,name):
  dp=[x for x in d['depts'] if x['n']==dept][0]
  return [s for s in dp['s'] if s['n']==name][0]
def remove_kind(n):
  for dp,s,k in kinds():
    if k['n']==n: s['k'].remove(k); return k
# echo archetypes: Clementine -> promote versions
c=get('Clementine'); a=c['x'][0]
c['x']=[{'n':v['n'],'a':'','d':v['d'].replace(', old data',''),'mk':'','y':v.get('y',''),'s':a['s'],'v':[]} for v in a['v']]
for x in c['x']:
  if x['n']=='Fina': x['d']='Spanish clementine cultivar.'
  if x['n'].startswith('Clemenules'): x['d']='Mutation of Fina; the most widely planted clementine in Spain.'
# Japanese aromatic citrus
yz,su,kb=remove_kind('Yuzu'),remove_kind('Sudachi'),remove_kind('Kabosu')
mf='https://www.maff.go.jp/j/shokusan/gi_act/register/index.html'
kj={'n':'Japanese aromatic citrus','a':'yuzu · sudachi · kabosu','d':'Small acid Japanese citrus sold fresh for juice, zest and ponzu: yuzu, sudachi and kabosu.','t':['yuzu','sudachi','kabosu'],'s':'https://en.wikipedia.org/wiki/Kabosu',
 'x':[{'n':'Kito yuzu (木頭ゆず) GI','a':'','d':'Yuzu from Kito, Tokushima, protected as a Japanese geographical indication.','mk':'','y':'','s':mf,'v':[]},
      {'n':'Tokushima sudachi (徳島すだち) GI','a':'','d':'Sudachi from Tokushima, where about 98% of the crop is grown; Japanese geographical indication.','mk':'','y':'','s':mf,'v':[]}]}
sh=shelf('Fruit','Lemons, limes & aromatic citrus')
i=[k['n'] for k in sh['k']].index('Bitter orange'); sh['k'].insert(i,kj)
sh['n']='Lemons, limes & aromatic citrus'
# mushrooms
ms=[remove_kind(n) for n in ['Enoki','Shimeji','Maitake',"Lion's mane",'Wood ear']]
shm=shelf('Mushrooms & sea vegetables','Cultivated mushrooms')
shm['k'].append({'n':'Speciality cultivated mushrooms','a':'enoki · shimeji · maitake · lion\'s mane · wood ear','d':'Fresh cultivated mushrooms beyond button, shiitake and oyster, sold in clusters or trays.','t':['enoki','shimeji (beech)','maitake (hen-of-the-woods)',"lion's mane",'wood ear'],'s':'https://en.wikipedia.org/wiki/Grifola_frondosa','x':ms[1]['x']})
# sea vegetables
shs=shelf('Mushrooms & sea vegetables','Sea vegetables')
shs['k']+= [{'n':'Dulse','a':'Palmaria palmata · dillisk · söl','d':'Red seaweed eaten fresh off the shore or dried, in Ireland, Iceland and Atlantic Canada.','s':'https://en.wikipedia.org/wiki/Palmaria_palmata'},
 {'n':'Sea lettuce','a':'Ulva lactuca','d':'Bright green seaweed with thin sheets, eaten in soups and salads.','s':'https://en.wikipedia.org/wiki/Ulva_lactuca'}]
# Crown melon
mel=get('Melon')
mel['x'].append({'n':'Shizuoka Crown melon','a':'Crown melon · king of fruits','d':'Premium greenhouse muskmelon from Shizuoka, one fruit per plant, sold only with a certified seal.','mk':'','y':'','s':'https://ikigaifruits.com/blogs/news/all-about-japans-number-1-luxury-fruit-the-crown-melon','v':[]})
# mixed packs dissolved
mp=[x for x in d['depts'] if x['n']=='Mixed packs & gift fruit'][0]
gift=[k for k in mp['s'][0]['k'] if k['n']=='Fruit gift box'][0]
gift['t']=gift['t']+['mixed fruit pack']
get('Blueberry')['t']=get('Blueberry')['t']+['mixed berry pack']
msl=get('Mixed salad leaves'); msl['t']=msl.get('t',[])+['mixed vegetable pack','crudité tray']
d['depts'].remove(mp)
fr=[x for x in d['depts'] if x['n']=='Fruit'][0]
def merge(dp,names,new,lead):
  ss=[s for s in dp['s'] if s['n'] in names]
  ks=[k for s in ss for k in s['k']]
  ks.sort(key=lambda k:k['n']!=lead)
  pos=dp['s'].index(ss[0])
  for s in ss: dp['s'].remove(s)
  dp['s'].insert(pos,{'n':new,'k':ks})
merge(fr,['Apples','Pears, quinces & loquats'],'Pome fruit','Apple')
merge(fr,['Strawberries','Berries & currants'],'Soft fruit','Strawberry')
merge(fr,['Mangoes','Bananas, pineapples & papayas'],'Mangoes, bananas, pineapples & papayas','Mango')
fr['s'].append({'n':'Premium & gift fruit','k':[gift]})
vg=[x for x in d['depts'] if x['n']=='Vegetables'][0]
merge(vg,['Potatoes','Sweet potatoes & tropical roots'],'Potatoes, sweet potatoes & tropical roots','Potato')
after=sum(len(k.get('x',[])) for dp,s,k in kinds())
print('archetypes',before,'->',after,'removed rhs',removed)
json.dump(d,open(P+'J4.json.tmp','w'),ensure_ascii=False,indent=1)
b=json.load(open(P+'J4_brands.json'))
def br(n,c,f,kf,dsc,s,rel=[]):
  return {'n':n,'c':c,'f':f,'seg':'Specialist','kf':kf,'d':dsc,'s':s}
pr='https://www.producereport.com/article/south-tyrol-reveals-secrets-its-high-quality-apples'
names={x['n'].lower() for x in b['b']}
new=[br('VOG','Italy','1945','South Tyrol apples','Consortium of 13 South Tyrol apple cooperatives and sole marketer of their fruit.',pr),
 br('Marlene','Italy','','South Tyrol apples','Apple brand owned exclusively by VOG, for PGI South Tyrol apples.',pr),
 br('Val Venosta','Italy','','Val Venosta apples','Vinschgau/Val Venosta apple brand of the VI.P consortium of seven cooperatives.',pr),
 br('Melinda','Italy','','Trentino apples','Trentino apple consortium, partner of VOG and VI.P in export marketing.','https://www.fruitnet.com/eurofruit/apple-competition-strikes-gold/4558.article')]
new[1]['rel']=['VOG'];new[2]['rel']=['VOG']
for n in new:
  if n['n'].lower() not in names: b['b'].append(n)
json.dump(b,open(P+'J4_brands.json.tmp','w'),ensure_ascii=False,indent=1)
