import json,os
p='/home/user/Possession-Taxonomy/rebuild/out/J7_parts/WIT.json'
d=json.load(open(p))
ent={}
for s in d['depts'][0]['s']:
    for k in s['k']:
        for e in k['x']: ent[(k['n'],e['n'])]=e
def add(kind,name,vs):
    e=ent[(kind,name)]; have={v['n'] for v in e['v']}
    for n,t in vs:
        if n not in have: e['v'].append({'n':n,'mk':'','y':'','d':t})
add('Lombardy: DOCG appellations','Franciacorta',[('Franciacorta Satèn',''),('Franciacorta Rosé',''),('Franciacorta Millesimato','')])
add('Veneto: DOCG appellations','Conegliano Valdobbiadene Prosecco',[('Superiore di Cartizze','')])
add('Sicily: DOC appellations','Marsala',[(n,'') for n in ['Marsala Vergine Stravecchio / Riserva','Marsala Vergine / Soleras','Marsala Superiore Riserva','Marsala Superiore','Marsala Fine']])
add('Sicily: DOC appellations','Moscato di Pantelleria',[('Passito di Pantelleria','')])
add('Veneto: DOC appellations','Breganze',[('Torcolato','')])
add('Piedmont: DOC appellations','Albugnano',[]) if False else None
# Passito di Caluso under Caluso (DOCG)
add('Piedmont: DOCG appellations','Caluso',[('Passito di Caluso','')])
d['renames'].update({
 'Prosecco':'Veneto: DOCG appellations','Franciacorta':'Lombardy: DOCG appellations',
 "Asti & Moscato d'Asti":'Piedmont: DOCG appellations','Brachetto':'Piedmont: DOCG appellations',
 'Lambrusco':'Emilia-Romagna: DOC appellations','Marsala':'Sicily: DOC appellations',
 'Passito & dried-grape wine':'Veneto: DOCG appellations'})
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.rename(p+'.tmp',p)
json.dump({'c':'J7','ax':'x','key':['1. x? → '+d['depts'][0]['n']],'depts':d['depts']},open('/tmp/WIT_check.json','w'))
