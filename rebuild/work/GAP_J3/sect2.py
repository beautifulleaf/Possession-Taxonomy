import json,re,os
P='../../out/J3.json'
d=json.load(open(P))
LEX={'Romagna':'Italy','Greek':'Greece','Epirus':'Greece','Cretan':'Greece','Italian':'Italy','Piedmont':'Italy','Lombardy':'Italy','Aosta':'Italy','Friuli':'Italy','Brazilian':'Brazil','Mexican':'Mexico','Filipino':'Philippines','Venezuela':'Venezuela','Portuguese':'Portugal','Loire':'France','Burgundy':'France','Provence':'France','Cévennes':'France','Périgord':'France','Dauphiné':'France','Lyonnais':'France','Poitou':'France','Touraine':'France','Berry':'France','Indre':'France','Rhône':'France','Chavignol':'France','Californian':'United States','California':'United States','Oregon':'United States','Vermont':'United States','Irish':'Ireland','Tipperary':'Ireland','Scottish':'United Kingdom','Inverness':'United Kingdom','Staffordshire':'United Kingdom','Swaledale':'United Kingdom','Cornish':'United Kingdom','Dorset':'United Kingdom','Buxton':'United Kingdom','Dovedale':'United Kingdom','Oxford':'United Kingdom','UK':'United Kingdom','Turkish':'Turkey','Bulgarian':'Bulgaria','Romanian':'Romania','Iranian':'Iran','Georgian':'Georgia','Serbian':'Serbia','Slovak':'Slovakia','Dutch':'Netherlands','Holland':'Netherlands','South Africa':'South Africa','Argentine':'Argentina','North Holland':'Netherlands'}
PEC={'Pecorino Romano':'Lazio','Pecorino Toscano':'Tuscany','Pecorino Sardo':'Sardinia','Pecorino Siciliano':'Sicily','Fiore Sardo':'Sardinia','Formaggio di fossa':'Emilia-Romagna','Pecorino di Filiano':'Basilicata','Pecorino di Picinisco':'Lazio','Piacentinu Ennese':'Sicily','Casu marzu':'Sardinia'}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      for e in k.get('x',[]):
        if e.get('g')=='Not stated' or (k['n']=='Pecorino'):
          t=e['d']+' '+e['n']
          g=None
          if k['n']=='Pecorino':
            g=PEC.get(e['n'])
            if not g:
              for r in ['Calabria','Tuscany','Campania','Sicily','Basilicata','Sardinia','Marche','Lazio','Abruzzo']:
                if r in e['d'] : g=r;break
            g=g or 'Other Italian regions'
          else:
            for kk,v in LEX.items():
              if re.search(r'\b'+kk+r'\b',t): g=v;break
          if not g and k['n']=='Gouda': g='Netherlands'
          if not g and k['n']=='Americas regional cheese': g='Argentina'
          if g: e['g']=g
      if k['n']=='Pecorino': k['xg']='by region of origin'
      # Wikidata UK 'England' -> unify
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      for e in k.get('x',[]):
        if e.get('g')=='Not stated': print(k['n'],e['n'],e['d'])
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'.tmp',P)
