import json,os,re
P='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(P+'J6.json'))
br=json.load(open(P+'J6_brands.json'))
K={}
for D in d['depts']:
  for S in D['s']:
    for k in S['k']: K[k['n']]=k
W='https://en.wikipedia.org/wiki/'
def add(kind,n,desc,s,g=None,y='',mk='',a='',dt='',**kw):
  k=K[kind]
  if any(e['n'].lower()==n.lower() for e in k['x']): return
  e={'n':n,'a':a,'d':desc,'mk':mk,'y':y,'s':s,'v':[],'dt':dt}
  if g: e['g']=g
  e.update(kw); k['x'].append(e)
def find(kind,n):
  for e in K[kind]['x']:
    if e['n']==n: return e
# ---- Darjeeling
dj='Darjeeling tea'; src=W+'Darjeeling_tea'
for e in K[dj]['x']: e['g']='Darjeeling Geographical Indication' if 'GI' in e['n'] else 'Estate'
yrs={'Tukvar':'1852 (Company experimental garden)','Steinthal':'1852 (Company experimental garden)','Alubari':'1852 (Company experimental garden)','Lebong':'1846 (Campbell planting)'}
for n in ['Arya','Avongrove','Badamtam','Balasun','Glenburn','Gopaldhara','Happy Valley','Jungpana','Lopchu',"Margaret's Hope",'North Tukvar','Okayti','Peshok','Phoobsering','Phuguri','Pussimbing','Puttabong','Rangli Rangliot','Teesta Valley','Thurbo','Mission Hill','Tukvar','Steinthal','Alubari','Lebong','Tumsong','Ambootia']:
  add(dj,n,'Tea estate in the Darjeeling hills named in the Wikipedia article on Darjeeling tea.',src,g='Estate',y=yrs.get(n,''))
K[dj]['nl']='One entry is a Darjeeling tea estate or the Darjeeling indication.'
# ---- Ceylon
cy='Ceylon tea'; sl=W+'Tea_production_in_Sri_Lanka'
for e in K[cy]['x']: e['g']='Growing region'
add(cy,'Nuwara Eliya','High-country tea district of Sri Lanka named in the Wikipedia article on tea production in Sri Lanka.',sl,g='Growing region')
add(cy,'Dambatenne estate','Tea estate at Haputale in the Sri Lankan hill country, at about 1,800 m above sea level.',sl,g='Estate')
add(cy,'Dunsinane Tea Estate','Tea estate about 80 km from Kandy named in the Wikipedia article on tea production in Sri Lanka.',sl,g='Estate')
add(cy,'Harrow Tea Estate','Tea estate about 80 km from Kandy named in the Wikipedia article on tea production in Sri Lanka.',sl,g='Estate')
# ---- Kenya
add('Kenyan, African & Black Sea tea','Kenyan highland black tea','Black tea from the Kenyan Highlands, Rift Valley and Limuru; tea was first introduced in 1903 and Kenya ranks third in tea exports after China and India.',W+'Tea_production_in_Kenya',y='1903',dt='KTDA smallholders produce over 60 % of Kenyan tea',g='Kenya')
for e in K['Kenyan, African & Black Sea tea']['x']:
  e.setdefault('g','Nepal' if 'Ilam' in e['n'] else ('Turkey' if 'Rize' in e['n'] else 'Kenya'))
# ---- Japanese
sc='Sencha & steamed green tea'; jt=W+'Japanese_tea'; sw=W+'Sencha'
for e in K[sc]['x']:
  e['g']='Cultivar' if e['n'] in('Yabukita','Yutakamidori','Sayamakaori') else ('Region or season' if e['n'] in('Uji sencha','Sayama sencha','Shincha') else 'Type')
for n,dd,s in [('Asamushi sencha','Lightly steamed sencha.',sw),('Chumushi sencha','Medium-steamed sencha.',sw),('Fukamushi sencha','Deeply steamed sencha, named on the Wikipedia pages on sencha and Japanese tea.',sw),('Karigane sencha','Sencha that includes stems and other plant parts.',sw),('Aracha','Unfinished green tea named among the Japanese green teas on the Wikipedia article on Japanese tea.',jt),('Konacha','Fine tea fragments and powder from finished green tea, named on the Wikipedia article on Japanese tea.',jt),('Kamairicha','Pan-fired Japanese green tea named on the Wikipedia article on Japanese tea.',jt),('Tamaryokucha','Japanese green tea named on the Wikipedia article on Japanese tea.',jt),('Kokeicha','Japanese green tea style listed on RateTea.','https://ratetea.com/style.php'),('Kyobancha','Japanese green tea style listed on RateTea.','https://ratetea.com/style.php'),('Mecha','Japanese green tea style listed on RateTea.','https://ratetea.com/style.php')]:
  if n=='Tamaryokucha' and any(v['n']=='Tamaryokucha' for e in K[sc]['x'] for v in e.get('v',[])): continue
  add(sc,n,dd,s,g='Type')
mt='Matcha'
for e in K[mt]['x']: e['g']='Region'
for n,dd in [('Tencha','Leaf tea shaded before picking that is ground into matcha; named on the Wikipedia article on Japanese tea.')]:
  add(mt,n,dd,jt,g='Type')
for n,dd in [('Baba Mukashi','Oldest known matcha brand, named after Myoshuni, who died in 1598.'),('Hatsu Mukashi','Matcha brand presented to the shogun.'),('Ato Mukashi','Matcha brand presented to the shogun.'),('Taka no Tsume','Matcha brand named on the Wikipedia article on matcha.'),('Shiro','Matcha brand named on the Wikipedia article on matcha.')]:
  add(mt,n,dd,W+'Matcha',g='Historic brand')
add(mt,'Nishio matcha','Matcha from Nishio, Aichi, sold as a regional export brand.',W+'Matcha',g='Region')
add(mt,'Shizuoka matcha','Matcha from Shizuoka Prefecture, sold as a regional export brand.',W+'Matcha',g='Region')
gy='Gyokuro & kabusecha'
for e in K[gy]['x']:
  e['g']='Cultivar' if e['n'] in('Saemidori','Okumidori','Samidori') else ('Company' if 'Yamamotoyama' in e['n'] else 'Region')
for n in ['Asahi','Yamakai']:
  add(gy,n,'Gyokuro cultivar named on the Wikipedia article on gyokuro.',W+'Gyokuro',g='Cultivar')
add(gy,'Mie gyokuro','Gyokuro from Mie Prefecture; output rose from 3 tons in 2007 to 132 tons in 2008.',W+'Gyokuro',g='Region',y='2008')
# ---- Taiwan
tw='Taiwanese oolong'; tws=W+'Taiwanese_tea'
for n,dd,y in [('Qingxin oolong','Cultivar brought from the Wuyi Mountains to Dongding Village, Lugu, Nantou in 1855; about 60 % of Taiwan tea plants.','1855'),('Shan Lin Xi','High-mountain oolong region in Nantou.',''),('Hehuanshan','High-mountain tea region of Taiwan.',''),('Fushoushan','High-mountain tea region of Taiwan.',''),('Yushan','High-mountain tea region of Taiwan.',''),('Guifei (Honey oolong)','Bug-bitten oolong, usually roasted more heavily than Oriental Beauty.',''),('Four Season (Sijichun)','Cultivar developed by Taipei-area farmers for cheap, high year-round yields.',''),('Cuiyu (Jade oolong, No. 13)','Cultivar listed among the major Taiwanese tea varieties.','')]:
  add(tw,n,dd,tws,y=y)
for e in K[tw]['x']:
  if e['n']=='Dong Ding' and not e['y']: e['y']='1855 (Qingxin planting at Dongding Village)'
  e['g']='High-mountain tea' if e['n'] in('Alishan','Lishan','Dayuling','Shan Lin Xi','Hehuanshan','Fushoushan','Yushan') else ('Cultivar' if e['n'] in('Jin Xuan','Qingxin oolong','Four Season (Sijichun)','Cuiyu (Jade oolong, No. 13)') else 'Named oolong')
# ---- China black
bk='Chinese & Taiwanese black tea'; rt='https://ratetea.com/style.php'
for n in ['Bohea','Panyang Congou','Zao Bei Jian','Yunnan Gold']:
  add(bk,n,'Black tea style listed on RateTea.',rt,g='Chinese black tea')
add(bk,'Black Jade (TTES No. 18)','Taiwanese cultivar developed in the 1990s, mainly made into black tea.',tws,g='Taiwan',y='1990s')
for e in K[bk]['x']:
  if 'g' not in e or e['g']=='Black (Chinese tea list)': e['g']='Taiwan' if ('Sun Moon' in e['n'] or 'Black Jade' in e['n']) else 'Chinese black tea'
# ---- Chinese green g
for e in K['Chinese green tea']['x']:
  e['g']='Named on the Wikipedia list of Chinese teas' if e.get('g') else 'Further green teas'
  e['g']='Named on the Wikipedia list of Chinese teas' if e['n'] in('Baimao Hou','Chun Mee','Da Fang','Mengding Ganlu','Zhuyeqing') else 'Further green teas'
# ---- coffee entries
ev='Everyday ground & filter coffee'; bz='https://en.clickpetroleoegas.com.br/brazil-is-the-largest-coffee-producer-in-the-world-but-four-foreign-companies-control-more-than-half-of-the-domestic-market-including-brands-btl96/'
add(ev,'3 Corações','Brazilian market leader in packaged coffee; a joint venture of São Miguel Holding and Strauss Group with nine factories in Brazil.',bz,g='National champion: Brazil',mk='3 Corações',own='3corações (São Miguel Holding and Strauss Group, 50 % each)',tier='National champion',cty='Brazil',dt='Brazil: four companies hold 55.6 % of shelf sales')
add(ev,'Pilão','Brazilian coffee brand of JDE Peet\'s, sold with L\'OR, Café do Ponto, Pelé and Caboclo.',bz,g='Global group: JDE Peet\'s',mk='Pilão',own="JDE Peet's",tier='Global group',cty='Brazil')
for e in K[ev]['x']:
  if e['n']=='Dallmayr Prodomo': e['g']='Other brands: Germany'
  if e['n']=='Juhla Mokka': e['g']='Other brands: Finland'
  if e['n']=="Dunkin' Donuts": e['own']='Inspire Brands'; e['own_y']='2020'; e['d']=e['d'] if e.get('d') else e['d']
  if not e.get('g'): print('no g',e['n'])
ic='Instant coffee'
add(ic,'Maxim','Korean instant coffee-mix brand of Dongsuh Foods in Original, Mocha Gold and White Gold lines; Dongsuh held 89 % of the Korean market in 2021.','https://www.koreatimes.co.kr/lifestyle/trends/20231115/koreans-beloved-instant-coffee-mix-finds-its-place-on-global-stage',g='National champion: South Korea',mk='Maxim',own='Dongsuh Foods',tier='National champion',cty='South Korea',dt='stick-packed coffee mix; sold only in Korea')
add(ic,'G7','Vietnamese 3-in-1 instant coffee of Trung Nguyên, which took the top domestic position in 2016.',W+'Trung_Nguy%C3%AAn',g='National champion: Vietnam',mk='Trung Nguyên',own='Trung Nguyên',tier='National champion',cty='Vietnam',y='1996 (company founded)')
for e in K[ic]['x']:
  if not e.get('g'):
    e['g']={'Nescafé spray-dried instant':'Global group: Nestlé',"Nescafé Taster's Choice":'Global group: Nestlé','Starbucks VIA Ready Brew':'Global group: Starbucks Corporation'}.get(e['n'],'Other: no owner stated')
dc='Decaffeinated coffee'
for e in K[dc]['x']:
  if e['n']=='Swiss Water decaf': e['g']='Process'
  if e['n']=='New England Coffee': e['own']='Reily Foods Company'; e['own_y']='2013'
  if e['n']=="Dunkin' Donuts": e['own']='Inspire Brands'; e['own_y']='2020'
# owners
tp=find('Breakfast & everyday black tea','Typhoo'); tp['own']='Supreme'; tp['own_y']='2024'
dm=add  # placeholder
add('Breakfast & everyday black tea','Dilmah','Sri Lankan tea brand founded by Merrill J. Fernando in 1985; named the 10th largest tea brand in the world as of 2023.',W+'Dilmah',g='National champion: Sri Lanka',mk='Dilmah',own='Ceylon Tea Services (about 66.6 %; MJF Holdings is the ultimate parent)',tier='National champion',cty='Sri Lanka',y='1985')
for e in K['Breakfast & everyday black tea']['x']:
  if e['n']=='Ito En': e['own']='Ito En, Ltd. (listed, Tokyo Stock Exchange)'
  if not e.get('g'): e['g']='Blend style'
dr=K['Drinking chocolate']['x']
for e in dr:
  if e['n']=='Cadbury Drinking Chocolate': e['own']='Mondelez International'; e['own_y']='2010'; e['tier']='Global group'; e['g']='Global group: Mondelez International'
  if e['n']=='Ghirardelli': e['own']='Lindt & Sprüngli'; e['own_y']='1998'; e['g']='Independent: Lindt & Sprüngli'
  if not e.get('g'): e['g']='Tradition'
# ---- market facts
cm=d['depts'][0]['ms']; tm=d['depts'][1]['ms']
cm+= [
 {'mkt':'Global coffee pods','who':'Nestlé (Nespresso)','share':'27.5 %','yr':2024,'s':'https://www.reportprime.com/coffee-pod-r17662/company','note':'Market-research aggregator ranking: Keurig Dr Pepper 22.7 %, JDE Peet\'s 16.9 %, Starbucks 10.4 %, Lavazza 7.1 %, Kraft Heinz 4.7 %, Dunkin\' 3.8 %, illy 2.8 %'},
 {'mkt':'Global coffee (analyst expectation)','who':"Keurig Dr Pepper with JDE Peet's",'share':'about 20 %','yr':2025,'s':'https://www.xataka.com/empresas-y-economia/gigante-refrescos-asalta-cafe-comprando-a-duenos-marcilla-lor-ahora-van-a-tarta-nestle/amp','note':'Analysts expect the combined business to match Nestlé at about 20 % each; deal about EUR 15.7 bn, announced 30 August 2025, closing expected first half of 2026'},
 {'mkt':'Brazilian packaged coffee','who':"3 Corações, JDE Peet's, Melitta and Nestlé",'share':'55.6 % together','yr':2026,'s':bz,'note':'Nielsen data compiled by Abic as quoted in an article of 26 March 2026; data year not stated; 3 Corações named market leader'},
 {'mkt':'South Korean instant coffee mix','who':'Dongsuh Foods (Maxim)','share':'89 %','yr':2021,'s':'https://www.koreajoongangdaily.com/kjd-special/why-how-korean-coffee-mixes-became-an-everyday-staple/11195350','note':'Namyang Dairies 7.2 % and Lotte Nestlé Korea 3.4 %; the Korea Times gives Dongsuh 87.9 % for 2022'},
]
tm+= [
 {'mkt':'World tea brands','who':'Dilmah','share':'10th largest tea brand','yr':2023,'s':W+'Dilmah','note':'Ranking as the Wikipedia article states it'},
 {'mkt':'Kenyan tea production','who':'Kenya Tea Development Agency smallholders','share':'over 60 %','yr':2023,'s':W+'Tea_production_in_Kenya','note':'KTDA members\' share of Kenyan production; the article gives no year for the share; 66 KTDA factories'},
 {'mkt':'UK black tea sales volume','who':'Typhoo','share':'fifth','yr':2022,'s':W+'Typhoo','note':'Rank by volume; the brand was bought by Supreme in December 2024 after administration'},
]
for m in tm:
  if m['who']=='Ito En' and m.get('yr') is None: pass
# ---- brands register
B=br['b']; have={x['n'].lower() for x in B}
def nb(n,c,f,kf,dd,s,seg='Mainstream'):
  if n.lower() not in have: B.append({'n':n,'c':c,'f':f,'seg':seg,'kf':kf,'d':dd,'s':s}); have.add(n.lower())
nb('3corações','Brazil','','packaged coffee','Joint venture of São Miguel Holding and Strauss Group, 50 % each; Brazilian coffee market leader.',bz)
nb('Pilão','Brazil','','packaged coffee','Brazilian coffee brand sold by JDE Peet\'s.',bz)
nb('Dongsuh Foods','South Korea','1976','instant coffee mix','Maker of Maxim; began selling individually packaged instant coffee mix in 1976.','https://www.koreajoongangdaily.com/kjd-special/why-how-korean-coffee-mixes-became-an-everyday-staple/11195350')
nb('Maxim','South Korea','','instant coffee mix','Dongsuh Foods brand with Original, Mocha Gold and White Gold mixes.','https://www.koreatimes.co.kr/lifestyle/trends/20231115/koreans-beloved-instant-coffee-mix-finds-its-place-on-global-stage')
nb('Inspire Brands','United States','2020','restaurant group','Bought Dunkin\' in a deal completed on 15 December 2020.',W+'Dunkin%27')
nb('Reily Foods Company','United States','','packaged food','New Orleans company that bought New England Tea & Coffee in December 2013.','https://dailycoffeenews.com/2013/12/31/new-england-coffee-acquired-by-new-orleans-based-reily-foods')
nb('Mondelez International','United States','2010','confectionery owner','Owner of Cadbury since 2010.',W+'Cadbury')
nb('Lindt & Sprüngli','Switzerland','1998','chocolate owner','Wholly owns Ghirardelli, acquired in 1998.',W+'Ghirardelli_Chocolate_Company')
nb('Supreme','United Kingdom','2024','consumer goods wholesaler','Manchester wholesaler that bought Typhoo in December 2024 for GBP 10.2 million.',W+'Typhoo')
nb('UCC Ueshima Coffee','Japan','1933','canned coffee','Kobe coffee company founded by Tadao Ueshima; brought out canned coffee with milk in 1969.',W+'UCC_Ueshima_Coffee_Co.')
nb('Juan Valdez','Colombia','2002','coffee shops','Chain founded in Bogotá in 2002 by the National Federation of Coffee Growers through Procafecol.',W+'Juan_Valdez_Caf%C3%A9')
nb('Ceylon Tea Services','Sri Lanka','','tea owner','Parent company holding about 66.6 % of Dilmah.',W+'Dilmah')
for x in B:
  if x['n']=='Typhoo': x['d']='Launched by John Sumner Jr in 1903; owners were Cadbury Schweppes, Premier Foods, Apeejay Surrendra (2005-2021), Zetland Capital and, from December 2024, Supreme.'
  if x['n']=='Dilmah' and not x.get('f'): x['f']='1985'
json.dump(d,open('/home/user/Possession-Taxonomy/rebuild/work/GAP_J6/J6.tmp','w'),ensure_ascii=False,indent=1)
json.dump(br,open('/home/user/Possession-Taxonomy/rebuild/work/GAP_J6/J6_brands.tmp','w'),ensure_ascii=False,indent=1)
print('ok')
