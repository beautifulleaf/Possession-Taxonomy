import json,re,os
P='../../out/J3.json'
d=json.load(open(P))
REG=['South Tyrol','Piedmont','Lombardy','Aosta Valley','Trentino','Veneto','Tuscany','Sardinia','Sicily','Basilicata','Campania','Calabria','Lazio','Marche','Umbria','Liguria','Friuli-Venezia Giulia','Emilia-Romagna','Apulia','Abruzzo','Molise']
CTY=['United Kingdom','England','Scotland','Wales','Ireland','Canada','Quebec','United States','Mexico','Argentina','Uruguay','Brazil','Chile','Colombia','Peru','Spain','Portugal','France','Italy','Germany','Netherlands','Belgium','Switzerland','Austria','Norway','Sweden','Denmark','Finland','Poland','Czechia','Slovakia','Hungary','Slovenia','Croatia','Serbia','Bosnia','Montenegro','Lithuania','Ukraine','Romania','Bulgaria','Greece','Cyprus','Turkey','Egypt','Levant','Iran','Armenia','Georgia','Israel','Albania','North Macedonia','Malta','Tunisia','China','Ethiopia','Isle of Wight','Cornwall','Devon','Yorkshire','Corsica','Catalonia','Tibet','Ossetia','Cyclades','Crete','Lemnos','Macedonia','Mexico','Czech','Hungary','Malta','Colombia','Western Sahara']
M={'Quebec':'Canada','Cornwall':'England','Devon':'England','Yorkshire':'England','Isle of Wight':'England','Corsica':'France','Catalonia':'Spain','Cyclades':'Greece','Crete':'Greece','Lemnos':'Greece','Macedonia':'Greece','Czech':'Czechia','Bosnia':'Bosnia and Herzegovina','Ossetia':'Georgia'}
UK={'England','Scotland','Wales'}
def find(text,L):
  best=None
  for c in L:
    m=re.search(r'\b'+re.escape(c)+r'\b',text)
    if m and (best is None or m.start()<best[0]): best=(m.start(),c)
  return best[1] if best else None
bad=[]
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      x=k.get('x',[])
      if len(x)<=12: continue
      italian=k['n'] in('Italian mountain cheese','Pecorino','Ricotta & whey cheese','Fresh soft cheese') 
      k['xg']='by region of origin' if k['n']=='Italian mountain cheese' else 'by country of origin'
      for e in x:
        t=e['d']+' '+e['n']
        g=None
        if k['n']=='Italian mountain cheese':
          g=find(e['d'],REG) or ('Italy' if 'Italy' in e['d'] else None) or 'Other Italian regions'
        else:
          c=find(e['d'],CTY)
          if c: g=M.get(c,c)
          if g in UK: g='United Kingdom'
        if not g:
          bad.append((k['n'],e['n'],e['d']))
          g='Not stated'
        e['g']=g
for b in bad: print(b)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1);os.replace(P+'.tmp',P)
