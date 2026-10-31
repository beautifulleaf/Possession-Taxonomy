import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/F4.json'))
add={'Icon':' Icon-painting schools and iconographic types belong to the visual-art taxonomy.','Thangka & scroll painting':' Thangka painting styles belong to the visual-art taxonomy.','Yantra':' Yantra designs are diagrams (content), not listed here.'}
for D in d['depts']:
  for S in D['s']:
    for k in S['k']:
      k.pop('note',None)
      if k['n'] in add and add[k['n']] not in k['d']: k['d']+=add[k['n']]
json.dump(d,open(R+'work/V4_F4/t.json','w'),ensure_ascii=False,indent=1); os.replace(R+'work/V4_F4/t.json',R+'out/F4.json')
b=json.load(open(R+'out/F4_brands.json'))
drop={'HarperOne','Hay House','Nambé','Hasegawa'}
b['b']=[x for x in b['b'] if x['n'] not in drop]
def rec(n,c,d,s): return {"n":n,"c":c,"f":"","seg":"Specialist","kf":"","d":d,"lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":s}
W='https://en.wikipedia.org/wiki/'
b['b']+= [rec('A.G. Müller','','Card maker whose 1965 reprint of the Swiss Tarot is the 1JJ edition.',W+'Swiss_Tarot'),
 rec('J. G. Rauch','','Card factory of Johann Georg Rauch, which produced the first Swiss Tarot in 1831-1838.',W+'Swiss_Tarot'),
 rec('Johannes Müller','','Producer of the unaltered Swiss Tarot at Diessenhofen until 1860.',W+'Swiss_Tarot'),
 rec('Builders of the Adytum','','Organisation founded by Paul Foster Case that issues the B.O.T.A. tarot deck.',W+'B.O.T.A._tarot_deck'),
 rec('Naipes Comas','Spain','Spanish card printer that published Salvador Dalí\'s Tarot in 1984.',W+"Salvador_Dali's_Tarot")]
json.dump(b,open(R+'work/V4_F4/t.json','w'),ensure_ascii=False,indent=1); os.replace(R+'work/V4_F4/t.json',R+'out/F4_brands.json')
