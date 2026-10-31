import json
P='/home/user/Possession-Taxonomy/rebuild/out/A1_parts/TRAD.json'
part=json.load(open(P)); dep=part['depts'][0]
K={k['n']:k for s in dep['s'] for k in s['k']}
k=K['Traje de flamenca']
for e in k['x']: e['g']='Andalusia'
k['nl']="One entry is a named style of the traje de flamenca, as Wikipedia's Traje de flamenca article gives them."
k['sel']="Styles named in Wikipedia's Traje de flamenca article (whole page read): traje de lunares and the Marisol style; traje de gitana is an alias of the kind. Complete: 2 of 2."
k['xg']='by region'
for kn,g in [('Zhongshan suit','China'),('Kaba and slit','Ghana'),('Toub','Sudan'),('Southern African dress','Namibia and Botswana'),('Trachtenjanker','Alps'),('Bombachas & gaucho dress','Río de la Plata')]:
    k=K[kn]
    for e in k['x']: e['g']=g
    k['sel']=k['sel'].replace('Forms carried over from the structure pass','The single (or few) form(s) carried over from the structure pass')+' No further regional forms were looked up for this kind within the fetch budget.'
    k['xg']='by region'
json.dump(part,open(P,'w'),ensure_ascii=False,indent=1)
# counts
tot=0;roles=0
for kk in K.values():
    for e in kk.get('x',[]):
        tot+=1; roles+= 1 if e.get('role') else 0
print(tot,roles,len(K))
