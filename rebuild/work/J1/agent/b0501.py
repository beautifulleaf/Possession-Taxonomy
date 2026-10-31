import json,os
W='https://en.wikipedia.org/wiki/'
def X(n,d,s,mk='',y='',a='',v=None,dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s}
    if v: x['v']=v
    if dt: x['dt']=dt
    return x
def V(n,d='',mk='',y=''): return {'n':n,'mk':mk,'y':y,'d':d}
SP='https://wineandtravelitaly.com/food/salumi-piacentini-dop/'
TI='https://tienda.com/collections/lomo-pork-loin.oembed'
kinds=[
{'n':'Pancetta','a':'cured pork belly','d':'Pork belly salted and air-dried raw, eaten without cooking or used in cooking (not the fresh Spanish panceta).','s':'https://www.ditalia.com/collections/cured-salumi',
 't':['arrotolata (rolled)','tesa (flat)','affumicata (smoked)','cubed','sliced'],
 'x':[X('Pancetta arrotolata','Rolled and cased pancetta, typical of northern Italy.',W+'Pancetta',a='rolled pancetta'),
  X('Pancetta tesa','Flat, unrolled pancetta, typical of central and southern Italy.',W+'Pancetta',a='flat pancetta'),
  X('Pancetta Piacentina','PDO rolled pancetta of Piacenza province, 4–8 kg, red and pink-white layers when cut.',SP,dt='cylinder 4–8 kg'),
  X('Pancetta di Calabria','PDO pancetta; only pancetta made in Calabria may carry the name.',W+'Pancetta')]},
{'n':'Guanciale','a':'cured pork jowl','d':'Pork jowl salted and air-dried raw.','s':'https://www.ditalia.com/collections/cured-salumi',
 'x':[X('Roman guanciale','Central Italian jowl (Lazio, Umbria) seasoned with salt and black pepper; the fat of amatriciana and carbonara.',W+'Guanciale',dt='plain pepper or with peperoncino, garlic, herbs · whole or cubed')]},
{'n':'Coppa','a':'capocollo · capicola · cured pork neck','d':'The pork neck (collar) salted and air-dried raw, sold whole or sliced (coppa).','s':'https://www.ditalia.com/collections/cured-salumi',
 'x':[X('Coppa Piacentina','PDO coppa of Piacenza, a cylinder over 1.5 kg with bright red meat.',W+'Capocollo',v=[V('Coppa Piacentina','old data')]),
  X('Capocollo di Calabria','PDO capocollo of Calabria.',W+'Capocollo'),
  X('Coppa di Parma','PGI coppa from pork neck, aged about two to six months, made across Parma and neighbouring provinces.',"https://emiliaromagnaturismo.it/en/food-valley/pgi-coppa-di-parma"),
  X('Capocollo di Martina Franca','Apulian capocollo with EU protection.',W+'Capocollo'),
  X('Coppa de Corse','Corsican PDO coppa.',W+'Capocollo'),
  X('Kraški zašink','Slovenian Karst cured pork neck with EU protected designation.',W+'Capocollo')]},
{'n':'Cured pork loin (lomo)','a':'lomo · lomo embuchado · lountza','d':'The pork loin salted, seasoned and air-dried raw in a casing or net (lomo).','s':'https://farmfetch.co.uk/products/cobble-lane-cured-lomo-180g-1',
 't':['ibérico de bellota','serrano','whole','sliced'],
 'x':[X('Lomo embuchado','Spanish whole loin seasoned with garlic and smoked paprika, cased and aged for months.',TI,
        v=[V('Cinco Jotas 100% Ibérico de Bellota Loin','ibérico de bellota','Cinco Jotas'),V('Lomo Ibérico de Bellota','ibérico de bellota','Fermín'),V('Lomo Serrano','white pig','Fermín')],dt='ibérico label class or serrano · whole or sliced'),
  X('Lountza','Cypriot cured pork loin, sometimes spiced with coriander.',W+'Lomo_embuchado'),
  X('Balkan smoked pork loin','Loin brined in salt and garlic, then smoked and hung in winter winds for up to two months.',W+'Lomo_embuchado')]},
{'n':'Air-dried beef (bresaola)','a':'bresaola · cecina · cured beef','d':'A beef whole muscle salted and air-dried raw.','s':'https://www.ditalia.com/collections/cured-salumi',
 'x':[X('Bresaola della Valtellina','PGI air-dried top round of beef, aged two or three months until dark red.',W+'Bresaola'),
  X('Bündnerfleisch','Graubünden air-dried beef from upper thigh or shoulder, pressed into a rectangular shape.',W+'Bündnerfleisch',a='viande des Grisons'),
  X('Cecina de León','PGI salted, smoked and air-dried beef from the hind leg, León and Palencia.',W+'Cecina_(meat)',v=[V('Cecina de León','old data')]),
  X('Pastırma','Anatolian air-dried beef coated in çemen paste of fenugreek, cumin, garlic and paprika; Kayseri specialty.',W+'Pastirma',a='basturma · pastarma',
    v=[V('Pastarma Govezhda','Bulgarian beef pastarma, EU TSG','', '2017')]),
  X('Suho meso','Balkan cured beef without the çemen coating.',W+'Pastirma')]},
{'n':'Lardo','a':'salo · cured back fat','d':'Pork back fat cured with salt and seasoning, not rendered.','s':'https://www.bottegacremonese.it/en/salame-of-cremona/409-lardo-di-colonnata-igp-antica-larderia-mafalda.html',
 'x':[X('Lardo di Colonnata','Fatback cured for months with herbs in Carrara-marble basins at Colonnata; PGI since 2004.',W+'Lardo',y='2004',v=[V('Lardo di Colonnata','old data')]),
  X("Vallée d'Aoste Lard d'Arnad",'PDO (1996) back fat brined with herbs in wooden doïls at Arnad, Aosta Valley.',"https://en.wikipedia.org/wiki/Vall%C3%A9e_d%27Aoste_Lard_d%27Arnad",y='1996'),
  X('Salo','East European salt-cured slab of pork fat, sometimes with skin; seasoned with garlic or paprika, or smoked.',W+'Salo_(food)',a='slanina · słonina · szalonna')]},
]
brands=[
{'n':'Fermín','c':'Spain','seg':'Premium','kf':'ibérico charcuterie','d':'Spanish ibérico and serrano charcuterie maker whose loins and hams are sold in the US.','sig':['Lomo embuchado'],'s':TI},
{'n':'Consorzio dei Salumi Piacentini','c':'Italy','f':'1971','seg':'Institution & issuer','kf':'Piacenza PDOs','d':'Consortium promoting the three Piacenza PDO salumi: coppa, pancetta and salame.','sig':['Coppa Piacentina','Pancetta Piacentina'],'s':SP},
]
out={'kinds':kinds,'brands':brands,'traditions':[],'notes':'All six planned kinds kept with old sources. Pastırma put under air-dried beef. Cinco Jotas brand entry lives in 05_00. Left out: lomo PDO/ibérico label specifics beyond retailer data; Pancetta Piacentina ageing minimum and DOP year (only search snippets); Guanciale has no protected name (none found).'}
p='/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/05_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
