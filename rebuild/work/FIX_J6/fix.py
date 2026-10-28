import json,os,tempfile
P='out/J6'
d=json.load(open(P+'.json'));br=json.load(open(P+'_brands.json'));tr=json.load(open(P+'_traditions.json'))
def kinds():
  for dp in d['depts']:
    for s in dp['s']:
      for k in s['k']: yield dp,s,k
def kind(n): return next(k for _,_,k in kinds() if k['n']==n)
def dept(n): return next(dp for dp in d['depts'] if dp['n']==n)
def drop(k,names): k['x']=[x for x in k['x'] if x['n'] not in names]
def get(k,n): return next(x for x in k['x'] if x['n']==n)
W='https://en.wikipedia.org/wiki/'
# J6-5 merge single-origin
so=kind('Single-origin coffee')
def merge(newn,members,a,dd,s,y='',dt=''):
  xs=[get(so,m) for m in members]; i=so['x'].index(xs[0])
  vs=[]
  for x in xs:
    sub=''.join('' for _ in [0])
    extra=('; '+'; '.join(v['n']+(' ('+v['d']+')' if v.get('d') else '') for v in x.get('v',[]))) if x.get('v') else ''
    vs.append({"n":x['n'],"mk":"","y":x.get('y',''),"d":(x['d'].rstrip('.')+extra)[:400]})
  for x in xs: so['x'].remove(x)
  so['x'].insert(i,{"n":newn,"a":a,"d":dd,"mk":"","y":y,"s":s,"v":vs,"dt":dt})
merge('Ethiopia',['Ethiopia Yirgacheffe','Ethiopia Sidamo / Sidama','Ethiopia Guji','Ethiopia Harar'],'Ethiopian heirloom coffee','Arabica from Ethiopia sold by regional name: Yirgacheffe, Sidamo, Guji and Harar.',W+'Coffee_production_in_Ethiopia',dt='country → region · variety: Ethiopian heirloom · process: washed, natural')
merge('Indonesia',['Sumatra Mandheling','Gayo (Aceh)','Sulawesi Toraja Kalosi','Java Estate (Old Java)','Bali Kintamani'],'Indonesian coffee · Sumatra · Java · Sulawesi · Bali','Arabica from Indonesian islands sold by regional name, often wet-hulled in Sumatra and aged in Java.',W+'Coffee_production_in_Indonesia',dt='country → island or region → estate · process: giling basah, washed')
merge('Brazil',['Brazil natural (dry-processed)','Brazil Cerrado Mineiro'],'Brazilian coffee','Brazilian arabica, nearly all dry-processed; Minas Gerais supplies about half of national output.',W+'Coffee_production_in_Brazil',dt='country → region · process: natural, pulped natural')
pb=get(so,'Panama Boquete'); pb['dt']+=' · variety Geisha is also listed under Geisha & rare-variety coffee'
so['d']+=' Organised country → region → estate; variety and process are separate axes.'
# J6-4 concepts
cb=kind('Cacao beans'); drop(cb,['Motamayor ten genetic groups','Fine or flavour cocoa'])
cb['t']+=['Motamayor genetic group (Amelonado, Contamana, Criollo, Curaray, Guiana, Iquitos, Marañon, Nacional, Nanay, Purús)','ICCO fine or flavour class']
dept('Cocoa & drinking chocolate')['b'].append({"m":"Genetic group (Motamayor et al., 2008)","v":"","w":"Ten groups proposed from morphology, geography and genomics; a classification, not a grade. Source: Theobroma cacao page."})
mt=kind('Matcha'); drop(mt,['Koicha vs usucha','Historic Mukashi blends'])
mt['t']+=['koicha (thick tea, about 4 g in 30 ml)','historic blend names (Baba Mukashi, Hatsu Mukashi, Ato Mukashi)']
drop(kind('Flavoured tea'),['Fruit and floral blends'])
rp=kind('Raw pu-erh (sheng)'); drop(rp,["Pu'er cake (bing)"])
rp['t']=list(dict.fromkeys(rp['t']+['Zhuancha brick','Jinguan / Longzhu / Jingcha forms']))
# J6-2
cg=kind('Chinese green tea'); cg['x'].append({"n":"Gunpowder tea","a":"Zhu Cha · pinhead gunpowder · Temple of Heaven","d":"Green tea with each leaf rolled into a small pellet; tighter pellets mean higher grade, and it is the base for Maghrebi mint tea.","mk":"","y":"Tang dynasty (production)","s":W+'Gunpowder_tea',"v":[{"n":"Pingshui gunpowder (Temple of Heaven, Pinhead)","mk":"","y":"","d":"Zhejiang gunpowder named on the page"},{"n":"3505AAA","mk":"","y":"","d":"Highest alphanumeric grade; 9375 is a lower one"}],"dt":"grade: 3505AAA to 9375 · pellet size and shine · origin: Zhejiang, Taiwan"})
rg=kind('Roasted grain tea'); rg['x'].append({"n":"Sobacha (buckwheat tea)","a":"soba-cha · memil-cha · kuqiao-cha","d":"Roasted buckwheat brewed as a caffeine-free tea; Korean tartary buckwheat from Gangwon is nuttier.","mk":"","y":"","s":W+'Sobacha',"v":[],"dt":"form: roasted grain · steep 2-4 min at 90 C"})
# J6-3 mk cleanup
for dp,s,k in kinds():
  for x in k.get('x',[]):
    if x.get('mk') in ('Kunming and Menghai tea factories','Motamayor et al.','Scott Laboratories','Coffee Research Station, Kenya','Tea Research and Extension Station','Italian E.S.E. consortium'):
      x['d']=x['d'].rstrip('.')+('; by '+x['mk'] if x['mk'] not in x['d'] else ''); x['mk']=''
hw=get(kind('Raw pu-erh (sheng)'),'Haiwan'); hw['d']='Private pu\'er factory founded in 1999 by Zhou Bing Liang, a former Menghai factory owner; recipe factory digit 8.'
get(rp,'Menghai factory recipes')['d']='Four-digit recipe numbers from the Menghai factory (factory digit 2); first digits give the year, third the leaf grade; 7542 dates from 1975.'
get(rp,'Xiaguan tea factory')['d']='Yunnan factory dating from the 1940s, recipe factory digit 3, known for tuocha.'
# brands
have={b['n'].lower() for b in br['b']}
PU=W+"Pu%27er_tea"
new=[
 ("Menghai Tea Factory","China","1940s","Heritage manufactory","pu'er recipes","Yunnan factory (Dayi) with recipe factory digit 2; adopted wet piling after 1973.",PU),
 ("Xiaguan Tea Factory","China","1940s","Heritage manufactory","tuocha","Yunnan factory with recipe factory digit 3.",PU),
 ("Haiwan Tea Factory","China","1999","Specialist","pu'er","Private pu'er factory founded by Zhou Bing Liang, a former Menghai factory owner.",PU),
 ("Kunming Tea Factory","China","","Heritage manufactory","ripe pu'er","Co-developed wet piling with Menghai in 1973; recipe factory digit 1.",PU),
 ("Kenya Tea Development Agency","Kenya","1964","Mainstream","smallholder tea","Smallholder-owned Kenyan company handling farming support, processing and marketing for tea growers.",W+"Kenya_Tea_Development_Agency"),
 ("Nestlé","Switzerland","1866","Mainstream","Nescafé, Nespresso","Vevey-based food and beverage group.",W+"Nestlé"),
 ("Camp Coffee","United Kingdom","1876","Heritage manufactory","coffee-chicory syrup","Glasgow coffee and chicory syrup, now mainly a baking ingredient; sources give 1876 or 1885.",W+"Camp_Coffee"),
 ("Kimbo","Italy","","Mainstream","Neapolitan espresso","Naples coffee roaster from Melito di Napoli, founded in the late 1950s as Cafè do Brasil by the Rubino brothers.","https://beverfood.com/torrefazione/kimbo-s-p-a"),
 ("Segafredo Zanetti","Italy","1973","Mainstream","Italian espresso","Bologna-based private coffee group that owns Segafredo and operates cafés.",W+"Segafredo_Zanetti"),
 ("Ninety Plus","","","Specialist","rare Gesha lots","Producer and trader of rare green coffee scoring above 90 points, from Ethiopia and its Panama estate.","https://venezianocoffee.com.au/blogs/coffee-information/ninety-plus-coffees"),
 ("Swiss Water Company","","","Specialist","water-process decaf","Decaffeination company behind Swiss Water decaf.",""),
 ("Caffita System","","","Mainstream","Caffitaly capsules","Capsule system behind Caffitaly and K-Fee.",""),
 ("Wuyi Mountains Zhengshan Tea Industry","China","","Specialist","Jin Jun Mei","Maker credited with Jin Jun Mei black tea.",""),
]
for n,c,f,seg,kf,dd,s in new:
  if n.lower() in have: continue
  br['b'].append({"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":dd,"s":s})
# traditions
T=lambda n,r,p,dd,tech,mat,forms,ctr,auth,s:{"n":n,"g":"Food & drink","r":r,"p":p,"d":dd,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":s}
tr['t']+=[
 T("Uji tea","Uji, Kyoto, Japan","Tea planted from the late 12th century; sencha 1738","Japanese shaded and steamed green tea from Uji and neighbouring Kyoto areas.","ōishita shading with straw or reed covers; steaming, rolling, kneading","Camellia sinensis, shade covers",["Uji matcha","Uji gyokuro","Uji sencha"],["Uji","Ujitawara","Wazuka","Minamiyamashiro"],"A regional name needs all-local leaf; many farmers still hand-process",W+"Uji_tea"),
 T("Darjeeling tea","Darjeeling and Kalimpong, West Bengal, India","1841 planting; first gardens 1856","Himalayan black tea famed for muscatel flavour, sold by flush.","long withering, rolling, oxidation on trays, firing","Bannockburn 157, Phoobsering 312, Ambari Vegetative 2 cultivars",["Darjeeling first flush","Darjeeling second flush","Darjeeling autumnal flush","Darjeeling GI"],["Makaibari","Glenburn","Castleton","Happy Valley","Jungpana"],"India's first GI (2004); EU PGI 2011; Tea Board logo certification mark",W+"Darjeeling_tea"),
 T("Kenyan smallholder tea","Kenyan Highlands, Kenya","Planted 1903; commercial from 1924","Black tea grown largely on smallholdings through the Kenya Tea Development Agency and sold at the Mombasa auction.","crush-tear-curl (CTC) processing, plus orthodox whole leaf","Camellia sinensis; purple-leaf cultivars",["Kenyan CTC black tea"],["Limuru","KTDA factories","Mombasa auction"],"Sold by auction lot and factory; no single certification mark named",W+"Tea_production_in_Kenya"),
 T("Taiwanese high-mountain oolong","Central Taiwan highlands above 1,000 m","","Oolong grown above 1,000 m in Nantou and Chiayi, hand-harvested at low yield.","hand harvest, tarp withering, bruising, oxidation over about 36-40 hours","Camellia sinensis",["Alishan","Dayuling","Lishan"],["Alishan","Dayuling","Yu Shan","Wushe","Lishan"],"Sweet, milky, floral cup; the source names no certification",W+"High-mountain_tea"),
 T("Turkish coffee","Turkey and the former Ottoman lands","In Istanbul by 1539","Very fine coffee boiled unfiltered with grounds left in the cup; on UNESCO's intangible heritage list.","brought to the boil up to three times in a cezve","Medium-roast arabica, copper cezve, thin porcelain cups",["Turkish coffee"],["Istanbul","Damascus","Aleppo","Cairo"],"Fine powder grind, cezve, thick froth, water served first",W+"Turkish_coffee"),
 T("Arabic coffee (qahwa)","Arabian Peninsula and the Levant","Mid-15th century or earlier","Lightly roasted coffee boiled unfiltered with cardamom and served unsweetened in small cups; on UNESCO's intangible heritage list.","roasting in a mihmas, pounding in a mihbaj, boiling without filtering","Arabica, cardamom, sometimes cloves or saffron",["Arabic coffee (qahwa)"],["Mokha","Hejaz","Levant"],"Dallah pot, finjan cups, three cups poured partway",W+"Arabic_coffee"),
 T("Ethiopian coffee ceremony","Ethiopia and Eritrea","","Household ritual of roasting, grinding and brewing coffee in a clay jebena for three rounds.","pan roasting, mukecha grinding, jebena boiling, three rounds (abol, tona, baraka)","Green coffee, clay jebena, handleless cups, incense",[],["household ceremony"],"Jebena pot, three rounds, hosted by the woman of the household",W+"Coffee_ceremony"),
 T("Gongfu cha","Chaoshan (Guangdong) and Fujian, China; Taiwan","About 18th century","Brewing method using small pots and many short infusions of a large leaf quantity.","short infusions of 10-15 seconds lengthening each pour","Yixing clay teapot or gaiwan, thin porcelain cups, fairness cup",["Wuyi rock oolong","Phoenix Dancong oolong","Raw pu-erh (sheng)"],["Chaozhou","Wuyi Mountains","Taiwan"],"Small vessels, repeated infusions, rinsing of pot and leaf",W+"Gongfu_tea_ceremony"),
 T("Maghrebi mint tea","Maghreb: Morocco, Algeria, Tunisia, Libya, Mauritania","Spread 18th-20th centuries","Gunpowder green tea brewed with fresh spearmint and sugar, poured from a height.","boiling water, leaves left in the pot, high pour","Gunpowder tea, spearmint, sugar",["Moroccan mint tea","Gunpowder tea"],["Morocco","Algeria"],"Served at least three glasses; flavour changes glass to glass",W+"Maghrebi_mint_tea"),
]
def save(o,f):
  fd,t=tempfile.mkstemp(dir='out');os.write(fd,json.dumps(o,indent=1,ensure_ascii=False).encode());os.close(fd);os.replace(t,f)
save(d,P+'.json');save(br,P+'_brands.json');save(tr,P+'_traditions.json')
