import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
load=lambda p: json.load(open(R+p))
def save(p,o):
    t=R+p+'.tmp'; json.dump(o,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,R+p)
d=load('out/C7.json'); br=load('out/C7_brands.json'); B={x['n']:x for x in br['b']}
wd=lambda q:'https://www.wikidata.org/wiki/'+q
rows=[('Deere & Company','Q496302','United States','1837'),('AGCO','Q292292','United States','1990'),('Alamo Group','Q21198484','United States','1969'),('GEA Farm Technologies','Q446895','Germany','1881'),('Hanomag','Q29041','Germany','1871'),('Eicher','Q540281','Germany','1934'),('Chelyabinsk Tractor Plant','Q600277','Russia','1933'),('Lely Group','Q628343','Netherlands','1948'),('DeLaval','Q1179543','Sweden','1883'),('Horsch','Q1628943','Germany','1984'),('Joskin','Q1708740','Belgium','1968'),('Lemken','Q1816878','Germany','1780'),('Landini','Q2261849','Italy','1884'),('Ursus','Q2143828','Poland','1893'),('Väderstad','Q2535939','Sweden','1962'),('Pellenc','Q3117518','France','1973'),('Kesla','Q11871142','Finland','1960'),('Maschio Gaspardo','Q12735124','Italy','1964'),('Dewulf','Q112248004','Belgium','1946'),('Case IH','Q1046997','United States','1984'),('Reform','Q1769321','Austria','1910')]
miss=[]
for n,q,c,f in rows:
    if n not in B: miss.append(n); continue
    x=B[n]; x['c']=x.get('c') or c; x['f']=x.get('f') or f
    if not x.get('s'): x['s']=wd(q)
print('missing',miss)
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if not k.get('x'): continue
      if k['n']=='Cream separator':
        k['nl']="One entry is a make of cream separator named by a fetched page."
        k['xg']="Entry type"
        k['sel']="Follows the Wikipedia article Cream separator, which names Gustaf de Laval as the first maker. No complete list exists; follows that overview."
        for e in k['x']:
            e['g']='Origin'; e['role']='origin'
      else:
        k['sel']=k['sel'].rstrip()+" No complete list exists; follows the maker pages named here. Maker pages not read for this kind (Ford, Fendt, Hanomag, Eicher, SAME, Lamborghini, Caterpillar, Cletrac, Holt, Cub Cadet) keep the entries of the earlier pass."
T=d['depts'][0]
T['ms']+=[{"mkt":"Agricultural tractors, worldwide","who":who,"share":sh,"yr":2024,"s":"https://www.reportprime.com/agricultural-tractor-r19204/company","note":"vendor estimate, method not stated; another vendor lists Claas, not Mahindra, among the top five, so treat as indicative"} for who,sh in [("John Deere","18.0 %"),("CNH Industrial","12.5 %"),("Kubota Corporation","6.9 %"),("AGCO Corporation","6.1 %"),("Mahindra & Mahindra","5.2 %"),("CLAAS GmbH","3.8 %")]]
save('out/C7.json',d); save('out/C7_brands.json',br)
