import json,os
P='/home/user/Possession-Taxonomy/rebuild/out/C5.json'
d=json.load(open(P))
K={}
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']: K[k['n']]=k
OW="owner not stated"
A="https://en.wikipedia.org/wiki/Abacus"
for n,y,r,dd in[("Roman abacus","1st century AD","Roman Empire","Roman counting board with grooves for beads."),("Korean jupan","c. 1400","Korea","Korean abacus, in use around 1400."),("Cranmer abacus","","","Abacus named on the Wikipedia article."),("Nepohualtzintzin","","Aztec","Aztec counting device named on the Wikipedia article."),("Yupana","","Inca","Inca counting board named on the Wikipedia article."),("Rekenrek","","Netherlands","Dutch counting frame named on the Wikipedia article."),("Sumerian abacus","2700-2300 BC","Mesopotamia","Earliest abacus named on the Wikipedia article."),("Salamis Tablet","300 BC","Greece","Greek counting board named on the Wikipedia article.")]:
  K['Abacus']['x'].append({"n":n,"a":"","d":dd,"mk":"","y":y,"s":A,"v":[],"g":r or "Other","own":OW,"tier":"Independent"})
M="https://en.wikipedia.org/wiki/Mechanical_pencil"
for n,y,mk,cty,dd in[("Ever-Ready Sharp Pencil","1915","Tokuji Hayakawa","Japan","Hayakawa's pencil of 1915, patented in Japan in 1920; later Sharp."),("Pentel Function 357","","Pentel","Japan","Pentel model named on the Wikipedia article."),("Pentel Black Polymer 999","","Pentel","Japan","Pentel model named on the Wikipedia article."),("Faber-Castell e-Motion","","Faber-Castell","Germany","Faber-Castell pencil named on the Wikipedia article."),("Lamy ABC","","Lamy","Germany","Lamy children's pencil named on the Wikipedia article."),("Yard-O-Led","","","","Propelling pencil named on the Wikipedia article.")]:
  K['Mechanical pencil']['x'].append({"n":n,"a":"","d":dd,"mk":mk,"y":y,"s":M,"v":[],"g":mk or "Other","own":OW,"tier":"Independent","cty":cty} if cty else {"n":n,"a":"","d":dd,"mk":mk,"y":y,"s":M,"v":[],"g":"Other","own":OW,"tier":"Independent"})
json.dump(d,open('/tmp/c5.tmp','w'),ensure_ascii=False,indent=1); os.replace('/tmp/c5.tmp',P)
