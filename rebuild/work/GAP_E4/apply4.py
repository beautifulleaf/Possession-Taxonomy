import json,re,os
P='/home/user/Possession-Taxonomy/rebuild/out/E4.json'
d=json.load(open(P))
Y={"Astra 680":"1981","BMS Cam rifle":"1980","British Bull Dog revolver":"1872","Colombo-Ricci revolver":"1910","Taurus Model 608":"1997","Taurus Model 689":"1988","Union Automatic Revolver":"1909","Beretta Ultraleggero":"2021","Blaser F3":"2004","Zig Zag revolver":"2014","MAG-7":"1995","NeoStead 2000":"2001","Walch Revolver":"1859","Webley Longspur":"1853","AMT AutoMag II":"1987","Remington Model 10":"1908","Remington Model 17":"1921","Remington Model 31":"1931","Spencer 1882":"1882","Stevens Model 520/620":"1909","Danuvia VD-01":"1990","Grendel P30":"1990","INDUMIL Córdova":"2015","Kimel AP-9":"1988","OTs-33 Pernach":"1995","Ruger Security-9":"2017","Scorpion silent pistol":"2012","Smith & Wesson Model 910":"1995","SIG P227":"2013","SIG P239":"1996","Star Model 14":"1914","Stoeger Luger":"1969","Tanfoglio Force":"1997","Benelli M1":"1986","Vektor CP1":"1996","Atchisson Assault Shotgun":"1972","Franchi AL-48":"1948","Franchi SPAS-12":"1979","Pancor Jackhammer":"1984","Browning BSS":"1971","Remington Model 11-48":"1948","Remington Model 11-87":"1987","Remington Model 1100":"1963","Remington Model 58":"1956","Remington Model SP-10":"1989","Remington V3":"2015","Remington Versa Max":"2010","Colt New Line":"1873","Colt Python":"1955","Benelli M4":"1998","Glock":"1982","Mossberg 183":"1947"}
R={"Spencer 1882":"origin","Browning Auto-5":"origin","Ithaca Mag-10":"origin","Glock":"origin","Mamba Pistol":"origin","Mossberg 500":"landmark","Stevens Model 77E":"landmark","Marlin Model 39A":"landmark","TT pistol":"landmark"}
nk=lambda s:re.sub(r'\W','',s.lower())
Y={nk(a):b for a,b in Y.items()}; R={nk(a):b for a,b in R.items()}
ny=0;nr=0;seen=set()
for dep in d['depts']:
  if dep['n']!='Firearms': continue
  for sh in dep['s']:
    for k in sh['k']:
      for e in k.get('x') or []:
        key=nk(e['n'])
        if key in Y and not e.get('y'):
          e['y']=Y[key]; ny+=1
          e['s']='https://en.wikipedia.org/wiki/'+e['n'].replace(' ','_')
        if key in R and not e.get('role'):
          e['role']=R[key]; nr+=1; seen.add(key)
          e['s']='https://en.wikipedia.org/wiki/'+e['n'].replace(' ','_')
print(ny,nr,set(R)-seen)
json.dump(d,open(P+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(P+'.tmp',P)
