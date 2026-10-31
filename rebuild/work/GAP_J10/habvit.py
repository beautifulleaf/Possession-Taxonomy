import json,os
P='rebuild/out/J10.json'
d=json.load(open(P))
K=[K for D in d['depts'] for S in D['s'] for K in S['k'] if K['n'].startswith('Habano')][0]
W='https://en.wikipedia.org/wiki/'
V={'Vegueros':[('Especial No. 1','7½ in × 38; factory name Laguito No. 1'),('Especial No. 2','6 in × 38; Laguito No. 2'),('Mareva','5⅛ in × 42; Mareva'),('Seoane','4⅞ in × 33; Seoane'),('Tapados','46 × 120 mm; 2013 relaunch'),('Entretiempos','52 × 110 mm; 2013 relaunch')],
'Diplomáticos':[('No. 2','6⅛ in × 52; Pirámide'),('No. 4','5⅛ in × 42; Mareva'),('No. 5','4 in × 40; Perla')],
'La Gloria Cubana':[("Médaille d'Or No. 1",'7¼ in × 36'),("Médaille d'Or No. 2",'6¾ in × 43'),("Médaille d'Or No. 3",'6⅞ in × 28'),("Médaille d'Or No. 4",'6 in × 32'),('Taíno','7 in × 47'),('Glorioso','6⅛ in × 50; UK edition 2008'),('Deliciosos','5 in × 48; Cuba edition 2009'),('Belux No. 1','5½ in × 52; Belgium and Luxembourg edition 2011')],
'Por Larrañaga':[('Montecarlo','6¼ in × 33; Delicioso'),('Panetela','5 in × 36; Veguerito'),('Petit Corona','5⅛ in × 42; Mareva'),('Magnifico','6¾ in × 50; UK edition 2007'),('Belicoso Extra','5½ in × 52; Asia Pacific edition 2008'),('Valioso','6⅛ in × 52; Switzerland edition 2009'),('Encantos','6¾ in × 43; Asia Pacific edition 2010')],
'Rafael González':[('Coronas de Lonsdales','165 mm × 42'),('Perlas','about 102 mm × 40'),('Petit Coronas','129 mm × 42'),('Panetelas Extra','size not given')]}
S={'Vegueros':W+'Vegueros','Diplomáticos':W+'Diplom%C3%A1ticos_(brand)','La Gloria Cubana':W+'La_Gloria_Cubana_(cigar)','Por Larrañaga':W+'Por_Larra%C3%B1aga','Rafael González':'https://www.chaveta.com/blogs/cigar-journal/rafael-gonzalez-cigars-guide'}
for e in K['x']:
    if e['n'] in V and not e.get('v'):
        e['v']=[{'n':n,'y':'','d':dd} for n,dd in V[e['n']]]
        e['s2']=S[e['n']] if False else None
        del e['s2']
        e['d']=e['d'].rstrip('.')+f". Vitolas from {S[e['n']]}."
rest=[e['n'] for e in K['x'] if not e.get('v')]
K['sel']=K['sel'].rstrip()+" Vitola lists added for five more marques from Wikipedia and Chaveta; "+', '.join(rest)+" still have none (Wikipedia pages carry no vitolas, cubancigarwebsite.com returned 403, Firecrawl out of credits)."
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P); print(rest)
