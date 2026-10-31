import json,os
p='rebuild/out/F5.json'
d=json.load(open(p))
upd={'Bamforth & Co Ltd':'1870','Sawyer\'s':'1914','Stenders Kunstforlag':'1889','G. Kolff & Co.':'1848','Curt Teich':'1898','King and McGaw':'1982','JOB Collection':'1895','Association of Mouth and Foot Painting Artists of the World':'1957'}
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      if k['n']=='Picture postcard':
        for e in k['x']:
          if e['n'] in upd: e['y']=upd[e['n']]
          if e['n']=='JOB Collection': e['g']='France'
          if e['n']=='Stenders Kunstforlag': e['d']+=' Founded 1889 per its Wikipedia article (a source title gives 1888).'
          if e['n']=='Association of Mouth and Foot Painting Artists of the World': e['d']+=' Founded 1957 per its Wikipedia article (a category gives 1956).'
        order=[]
        for e in k['x']:
          if e['g'] not in order: order.append(e['g'])
        k['x'].sort(key=lambda e:(order.index(e['g']), e['y'] or '9999', e['n']))
        k['sel']+=' Complete: 58 of 58 publishers (59 category pages, Joseph Salmon merged into J Salmon Ltd) in Wikipedia Category:Postcard publishers, re-read 2026-10-31 with no subcategories. Founding years added where a fetched page states a firm start; blank where the page gives none (individuals show lifespans only).'
      if k['n']=='Charge card':
        k['sel']+=' No complete list exists; follows the Credit card article, and by the icons rule only the origin is listed.'
      if k['n']=='Transit card':
        k['sel']+=' Complete: 681 of 681 named cards in Wikipedia\'s List of public transport smart cards (rows without a card name excluded).'
open(p+'.tmp','w').write(json.dumps(d,ensure_ascii=False,indent=1));os.replace(p+'.tmp',p)
