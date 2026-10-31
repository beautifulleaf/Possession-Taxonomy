import json,os,re
O='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(O+'J2.json'))
G='Protected and regional names'
kinds={k['n']:k for dep in d['depts'] for s in dep['s'] for k in s['k']}
def ent(n,d_,y,s,dt):return {"n":n,"a":"","d":d_,"mk":"","y":y,"s":s,"v":[],"g":G,"dt":dt}
add={'Scallop':ent('Coquille Saint-Jacques des Côtes d\'Armor PGI','Scallop of the Côtes d\'Armor, France; first registered with the EU on 19 June 1998 and carried into the UK scheme on 31 December 2020.','1998','https://Www.Gov.uk/protected-food-drink-names/coquille-saint-jacques-des-cotes-darmor','PGI · France'),
     'Vendace roe':ent('Vänerlöjrom PDO','Swedish roe product entered in the EU register as a PDO by Regulation 2021/2004 of 10 November 2021.','2021','https://lawplayer.com/eu/act/32021R2004','PDO · Sweden')}
for kn,e in add.items():
    k=kinds[kn]; k['x'].append(e)
    p=sum(1 for x in k['x'] if x.get('g','').startswith('Protected'))
    k['sel']=re.sub(r'Covers \d+ protected names',f'Covers {p} protected names',k['sel'])
    k['sel']=re.sub(r'The other \d+ entries',f"The other {len(k['x'])-p} entries",k['sel'])
for kn in ('Trout & char','Carp','Lamprey','Whitefish & vendace','Smoked haddock','Crayfish','Native flat oyster','Atlantic salmon','Eel'):
    k=kinds[kn]; p=sum(1 for x in k['x'] if x.get('g','').startswith('Protected'))
    assert f'Covers {p} protected' in k['sel'],(kn,k['sel'][-300:])
json.dump(d,open(O+'J2.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(O+'J2.json.tmp',O+'J2.json')
