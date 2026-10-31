import json,os
d=json.load(open('stageA.json'))
Q='https://en.wikipedia.org/wiki/Quinquina';V='https://en.wikipedia.org/wiki/Vermouth'
add={'Quinquina & americano':[
 {'n':'Bonal Gentiane-Quina','a':'','d':'Quinquina named on the Wikipedia Quinquina page.','mk':'Bonal','y':'','s':Q,'cty':'France'},
 {'n':'St. Raphaël','a':'','d':'Quinquina named on the Wikipedia Quinquina page.','mk':'St. Raphaël','y':'','s':Q,'cty':'France'}],
 'Vermouth':[
 {'n':'Gancia','a':'','d':'Italian vermouth house named on the Wikipedia Vermouth page.','mk':'Gancia','y':'','s':V,'cty':'Italy'},
 {'n':'Yzaguirre','a':'','d':'Red vermouth from Spain, as the Wikipedia Vermouth page captions it.','mk':'Yzaguirre','y':'','s':V,'cty':'Spain'},
 {'n':'Fot-Li','a':'','d':'Red vermouth from Spain, as the Wikipedia Vermouth page captions it.','mk':'Fot-Li','y':'','s':V,'cty':'Spain'}]}
removed=[]
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']:
            if 'm' in k:
                removed+= [(k['n'],m[0]) for m in k['m'] if not any(m[1] and m[1] in a['mk'] for a in add.get(k['n'],[]))]
                del k['m']
            if k['n'] in add:
                have={e['n'] for e in k['x']}
                for e in add[k['n']]:
                    if e['n'] not in have: k['x'].append(e)
                nn=len(k['x'])
                k['sel']=k['sel'].rsplit('No complete list exists',1)[0]+"No complete list exists; follows Wikipedia Vermouth and Quinquina, which name brands without a full list."
json.dump(d,open('stageB.json','w'),ensure_ascii=False)
json.dump(removed,open('removed_m.json','w'),ensure_ascii=False)
print(len(removed))
