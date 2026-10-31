import json,re,os
P='/home/user/Possession-Taxonomy/rebuild/out/E4.json'
d=json.load(open(P))
Y={"Mauser C96":"1899","Luger pistol":"1898","Mauser HSc":"1940","High Standard HDM":"1942","Ruby pistol":"1914","PSS Silent Pistol":"1983","Bauer Automatic":"1972","JO.LO.AR.":"1924","Kimber Custom":"1997","Ruger P series":"1985","Ruger LCP":"2008","Webley Self-Loading Pistol":"1910","Hamada Type pistol":"1941","Bergmann–Bayard pistol":"1901","Pistol F. Ascaso":"1937","Salvator Dormus pistol":"1891","Taurus Millennium series":"2005","FN FNP":"2007","FN Baby Browning":"1927","Steyr M":"1999","Nambu Type 94 pistol":"1935","Colt New Service":"1898","Colt Detective Special":"1927","Colt Walker":"1847","Colt Dragoon Revolver":"1848","Type 26 revolver":"1893","Malinnov pistol":"2013","Chiappa Rhino":"2009","Ruger Security-Six":"1972","Ruger Security Six":"1972","Beretta 92":"1980","Glock 17":"1980","Remington Model 870":"1951","Smith & Wesson Model 10":"1899","M1911":"1911","Colt M1911":"1911"}
Y={re.sub(r'\W','',k.lower()):v for k,v in Y.items()}
n=0
for dep in d['depts']:
  for sh in dep['s']:
    for k in sh['k']:
      for e in k.get('x') or []:
        key=re.sub(r'\W','',e['n'].lower())
        if key in Y and not e.get('y'): e['y']=Y[key]; n+=1
        if k['n']=='Sword tradition (den)' and 'Shint' not in k['sel']:
          pass
      if k['n']=='Sword tradition (den)':
        k['sel']=k['sel'].replace('the later Shintō and Shinshintō periods are not dated by that page','later periods are dated by japanesesword.net: Kotō to 1596, Shintō 1596 to 1781 and Shinshintō 1781 to 1876 (the page also gives 1764 and 1780 for the end of Shintō); Shintō schools there are Umetada, Horikawa, Osaka and Edo, and Shinshintō smiths Masahide, Naotane, Kiyomaro and Masayoshi')
print(n)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
B='/home/user/Possession-Taxonomy/rebuild/out/E4_brands.json'
b=json.load(open(B))
for x in b['b']:
  if x['n']=='Denix': x['f']='1967'; x['s']='https://www.denix.es/en/company/denix/'
json.dump(b,open(B+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(B+'.tmp',B)
