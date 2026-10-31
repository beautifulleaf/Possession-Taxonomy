import json,os
W='https://en.wikipedia.org/wiki/'
JI=W+'Jamón_ibérico'; PR=W+'Prosciutto'; JS=W+'Jamón_serrano'
def X(n,d,s,mk='',y='',a='',v=None,dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s}
    if v: x['v']=v
    if dt: x['dt']=dt
    return x
def V(n,d='',mk='',y=''): return {'n':n,'mk':mk,'y':y,'d':d}
LABELS=[V('Black label: 100% ibérico de bellota','pure-bred, acorn-fed; only grade allowed to be called pata negra'),
 V('Red label: ibérico de bellota','acorn-fed, 75% or 50% Iberian ancestry'),
 V('Green label: ibérico cebo de campo','pastured, acorns and grain'),
 V('White label: ibérico de cebo','grain-fed, cured about 24 months')]
DTI='label class (black, red, green, white) · % ibérico breed · cure 24–48 months · whole on the bone, boneless or hand-sliced'
kinds=[
{'n':'Jamón ibérico','a':'Iberian ham · pata negra','d':'Dry-cured hind leg of the black Iberian pig, graded by breed purity and diet under Spain\'s four-colour label system.','s':JI,
 't':['bellota','cebo de campo','cebo','whole on the bone','boneless','hand-sliced'],
 'x':[X('Jamón de Guijuelo','PDO ham of 77 municipalities of south-east Salamanca; about 60% of jamón ibérico output.',JI,v=LABELS,dt=DTI),
  X('Jamón de Jabugo','PDO ham cured in the Sierra de Aracena and Picos de Aroche, Huelva.',JI,a='Jamón de Huelva',v=LABELS,dt=DTI),
  X('Dehesa de Extremadura','PDO ham from the cork- and holm-oak dehesa of Cáceres and Badajoz.',JI,v=LABELS,dt=DTI),
  X('Los Pedroches','PDO ham from Córdoba province, known for its V-shaped cut.',JI,v=LABELS,dt=DTI)]},
{'n':'Prosciutto crudo','a':'prosciutto · Italian dry-cured ham','d':'Italian raw ham: a pork hind leg salted and air-dried, usually eaten thinly sliced.','s':PR,
 't':['whole on the bone','boneless','pre-sliced'],
 'x':[X('Prosciutto di Parma','PDO ham of Parma, salted with sea salt only, aged at least 14 months and branded with the ducal crown.',PR,a='Parma ham',
        v=[V('Prosciutto di Parma','old data')],dt='aged 14–36 months · whole, boneless or sliced'),
  X('Prosciutto di San Daniele','PDO ham of San Daniele del Friuli; darker and sweeter than Parma.',PR,v=[V('San Daniele prosciutto','old data')]),
  X('Prosciutto Toscano','Tuscan PDO prosciutto.',PR),
  X('Prosciutto di Carpegna','PDO prosciutto from near Carpegna in Montefeltro.',PR),
  X('Prosciutto di Modena','PDO prosciutto of Modena.',PR),
  X('Prosciutto Veneto Berico-Euganeo','PDO prosciutto of the Veneto.',PR,a='Prosciutto Veneto'),
  X('Prosciutto di Norcia','PGI prosciutto of Norcia, Umbria.',PR),
  X('Prosciutto di Sauris','PGI prosciutto of Sauris, Friuli.',PR),
  X('Valle d\'Aosta Jambon de Bosses','PDO ham of the Aosta Valley.',PR),
  X('Culatello di Zibello','PDO cured from the inner muscle of the hind leg and aged in a bladder casing.',W+'Culatello',v=[V('Culatello di Zibello','old data')])]},
{'n':'Jamón serrano','a':'serrano ham','d':'Spanish dry-cured ham from white pigs, salted then hung for months; serrano is an EU traditional speciality guaranteed (TSG).','s':JS,
 't':['whole on the bone','boneless','sliced'],
 'x':[X('Jamón serrano TSG','Generic Spanish white-pig ham under EU traditional-speciality rules; salted about two weeks, then dried and hung up to 18 months.',JS,dt='curing time · whole or sliced'),
  X('Jamón de Teruel','PDO serrano-type ham of Teruel, Aragon.',JS),
  X('Jamón de Trevélez','PGI ham of Trevélez and nearby towns of the Alpujarra, Granada.',JS)]},
{'n':'Regional dry-cured hams','a':'dry-cured ham on the bone','d':'Protected or traditional raw dry-cured hams from outside the Spanish and Italian families, sold whole or sliced.','s':'https://farmfetch.co.uk/products/carmarthen-ham',
 'x':[X('Jambon de Bayonne','PGI ham of the Adour basin, aged at least 7 months and stamped with the Basque lauburu.',W+'Bayonne_ham',a='Bayonne ham'),
  X('Carmarthen Ham','Welsh air-dried, salt-cured ham, EU PGI in 2016; made by the Rees family.',"https://www.farminguk.com/news/carmarthen-ham-granted-eu-protected-name-status_44499.html",y='2016',v=[V('Carmarthen Ham','old data')]),
  X('Kraški pršut','Slovenian Karst dry-cured ham, protected 2012; one of several Balkan pršut names.',PR,v=[V('Dalmatinski pršut','protected 2016'),V('Drniški pršut','protected 2015'),V('Istarski pršut','protected 2015'),V('Krčki pršut','protected 2015')]),
  X('Presunto de Barrancos','Portuguese dry-cured ham from Barrancos made from the black Alentejano pig.',W+'Barrancos'),
  X('Jinhua ham','Chinese dry-cured ham of Jinhua, Zhejiang, made over 8–10 months; recorded since the Tang dynasty.',W+'Jinhua_ham'),
  X('Country ham','Heavily salted and usually hickory-smoked ham of the US South, aged months to years.',W+'Country_ham',a='Virginia ham',
    v=[V('Smithfield ham','Virginia law: dry-cured and aged at least six months within the town of Smithfield','', '1926')],dt='smoked or unsmoked · Virginia, Kentucky, Missouri, North Carolina styles')]},
{'n':'Smoked raw ham','a':'Speck · Schinken · smoked dry-cured ham','d':'Raw ham cured and cold-smoked, eaten thinly sliced, mainly from the Alps and Germany.','s':W+'Speck_Alto_Adige',
 'x':[X('Speck Alto Adige','PGI lightly smoked dry-cured ham of South Tyrol, aged at least 22 weeks.',W+'Speck_Alto_Adige',a='Südtiroler Speck',v=[V('Speck','old data')]),
  X('Schwarzwälder Schinken','PGI (1997) Black Forest ham, cold-smoked over local conifer wood.',W+'Black_Forest_ham',a='Black Forest ham',y='1997'),
  X('Westphalian ham','Dry-cured ham of Westphalia smoked over beechwood and juniper.',W+'Westphalian_ham',a='Westfälischer Schinken'),
  X('Ammerländer Schinken','PGI ham of Ammerland, dry-cured with salt and sugar and cold-smoked over beech.',W+'Ammerländer_Schinken',a='Ammerland ham',dt='bone-in or boneless')]},
{'n':'Cured shoulder (paleta)','a':'paleta · paletilla · cured pork shoulder','d':'The front leg of a pig salted and air-dried raw like jamón; smaller and cheaper.','s':'https://tienda.com/products/bone-in-iberico-de-bellota-shoulder-cinco-jotas-jm-109',
 'x':[X('Paleta ibérica','Ibérico shoulder sold under the same four-colour label ladder as jamón ibérico.',JI,v=LABELS+[V('Cinco Jotas Paleta Ibérica de Bellota','old data','Cinco Jotas')],dt=DTI),
  X('Paleta serrana','White-pig shoulder cured like serrano ham, sold for home use.',JS)]},
]
brands=[
{'n':'Sánchez Romero Carvajal','c':'Spain','f':'1879','seg':'Heritage manufactory','kf':'ibérico ham','d':'Jabugo ibérico house founded by Juan Rafael Sánchez Romero in 1879; partners Romero and Carvajal joined in 1910; makes Cinco Jotas.','lines':['Cinco Jotas'],'sig':['Jamón de Jabugo'],'rel':['Cinco Jotas'],'s':'https://www.esmadrid.com/en/node/68388'},
{'n':'Cinco Jotas','c':'Spain','f':'1879','seg':'Premium','kf':'100% ibérico bellota','d':'Ibérico brand (5J) of Sánchez Romero Carvajal, Jabugo.','sig':['Jamón de Jabugo','Paleta ibérica'],'rel':['Sánchez Romero Carvajal'],'s':'https://www.esmadrid.com/en/node/68388'},
{'n':'Joselito','c':'Spain','f':'1868','seg':'Premium','kf':'ibérico ham','d':'Gómez family ibérico ham house in Guijuelo, Salamanca.','sig':['Jamón de Guijuelo'],'s':'knowledge'},
{'n':'Consorzio del Prosciutto di Parma','c':'Italy','seg':'Institution & issuer','kf':'Parma PDO','d':'Producers\' consortium that guards the Prosciutto di Parma PDO and applies the ducal crown brand.','sig':['Prosciutto di Parma'],'s':PR},
]
out={'kinds':kinds,'brands':brands,'traditions':[],'notes':'Old "Dry-cured ham on the bone" became Regional dry-cured hams; its Parma, San Daniele and Culatello models moved to Prosciutto crudo archetypes and Speck to Smoked raw ham. Old Cured pork shoulder kept as Cured shoulder (paleta). Label classes as versions. Left out: Westfälischer Knochenschinken as a separate name and Presunto de Barrancos PDO status (no retrieved page states them); Smithfield Foods discontinued Genuine Smithfield Ham in 2024. Joselito founding from knowledge (official site 404).'}
p='/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/05_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
