import json,os
p='rebuild/out/B5.json'
d=json.load(open(p))
W='https://en.wikipedia.org/wiki/'
DK,FR,IT,UK,SE,DE='Denmark','France','Italy','United Kingdom','Sweden','Germany'
G={
'Bing & Grøndahl Christmas plate':DK,'Royal Copenhagen Christmas plate':DK,
'Acorn':DK,'Pyramid':DK,'AJ':DK,'Pride':UK,'Marly':FR,'Albi':FR,'Cannes':FR,'Thebe':SE,'Focus de Luxe':SE,'Citterio 98':'Finland','Goa':'Portugal','Nuovo Milano':IT,'Mami':IT,'Alveston':UK,'Radford':UK,'Bud':UK,'Stockholm':DE,
'Laguiole steak knife':FR,'Perceval 9.47':FR,'Opinel table knife':FR,
'Wakasa lacquered chopsticks':'Japan','Edo kibashi':'Japan',
'Bernadotte serving bowl':DK,'Cylinda-Line salad bowl':DK,'Kaymet tray':UK,'Girotondo':IT,'Vertigo':FR,
'Ostehøvel':'Norway','Girolle':'Switzerland','Le Creuset stoneware butter dish':FR,
'Cow creamer':'Netherlands','Bombè':IT,'Cylinda-Line':DK,'5070':IT,'Cylinda-Line salt and pepper set':DK,'Cylinda-Line coaster set':DK,
'Alessi 870 cocktail shaker':IT,'Henshall corkscrew':UK,
}
n=0
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      xs=k.get('x',[])
      if not xs or k['n'] in('Tableware house','Glassware house'):continue
      if all(e.get('g') for e in xs): continue
      for e in xs:
        if not e.get('g') and e['n'] in G:
            e['g']=G[e['n']]; e.setdefault('cty',G[e['n']]); n+=1
      if all(e.get('g') for e in xs):
          k['xg']='by country of the maker or origin, then year, then name'
          if len(xs)>=3: xs.sort(key=lambda e:(e['g'],e.get('y') or '9999',e['n']))
      else:
          print('left',k['n'],[e['n'] for e in xs if not e.get('g')])
          k.pop('xg',None)
print(n)
json.dump(d,open(p+'.tmp','w'),ensure_ascii=False,indent=1);os.rename(p+'.tmp',p)
