import json,os
Q='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(Q+'J6.json')); br=json.load(open(Q+'J6_brands.json'))
U='https://www.larepublica.co/empresas/lideres-del-mercado-retail-de-cafe-4005383'
d['depts'][0]['ms'].append({'mkt':'Colombian retail roasted coffee','who':'Colcafé (Grupo Nutresa)','share':'43 %','yr':2023,'s':U,'note':'Euromonitor retail sales as quoted by La República in November 2024: Nestlé 14 %, Torrecafé Águila Roja 9 %, Procafecol (Juan Valdez) 3.4 %, Casa Luker 2.3 %'})
k=[k for D in d['depts'] for S in D['s'] for k in S['k'] if k['n']=='Everyday ground & filter coffee'][0]
k['x'].append({'n':'Colcafé','a':'','d':'Colombian retail leader in roasted coffee with 43 % of retail sales in 2023; part of the coffee business of Grupo Nutresa.','mk':'Colcafé','y':'','s':U,'v':[],'dt':'Colombia: Euromonitor 2023','g':'National champion: Colombia','own':'Grupo Nutresa','tier':'National champion','cty':'Colombia'})
import re
k['sel']=re.sub(r'Covers \d+ brands',f"Covers {len(k['x'])} brands",k['sel'])
if not any(x['n']=='Grupo Nutresa' for x in br['b']): br['b'].append({'n':'Grupo Nutresa','c':'Colombia','f':'','seg':'Mainstream','kf':'coffee, chocolate','d':'Owner of Colcafé, the leading retail roasted coffee in Colombia.','s':U})
for f,o in [('J6.json',d),('J6_brands.json',br)]:
  json.dump(o,open(Q+f+'.new','w'),ensure_ascii=False,indent=1); os.replace(Q+f+'.new',Q+f)
