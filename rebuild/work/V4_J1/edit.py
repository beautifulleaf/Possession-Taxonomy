import json,re,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/J1.json')); b=json.load(open(R+'out/J1_brands.json'))
removed={}
HAMS='https://en.wikipedia.org/wiki/List_of_hams'
SAUS='https://en.wikipedia.org/wiki/List_of_sausages'
ITA='https://en.wikipedia.org/wiki/List_of_Italian_food_and_drink_products_with_protected_status'
JAM='https://en.wikipedia.org/wiki/Jam%C3%B3n'
PROV='https://www.provisioneronline.com/articles/118845-2025-top-100-meat-and-poultry-processors-record-meat-sales-fuel-growth'
BOELL='https://eu.boell.org/en/2021/09/07/companies-dominating-market-farm-display-case'
TYS='https://en.wikipedia.org/wiki/Tyson_Foods'; HOR='https://en.wikipedia.org/wiki/Hormel_Foods'
JBS='https://en.wikipedia.org/wiki/JBS_S.A.'; SMI='https://en.wikipedia.org/wiki/Smithfield_Foods'
DCW='https://en.wikipedia.org/wiki/Danish_Crown_(company)'
FORT='https://www.fortune.com/article/best-meat-delivery-services/'
HSP='https://halalspy.com/halal-grocery/meat-delivery/best-halal-meat-delivery-uk/'
def E(n,d_,s,a='',y='',mk='',v=None,g=None,**kw):
    e={"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":v or []}
    if g: e['g']=g
    e.update(kw); return e
def H(n,c,note,s=HAMS,a=''): return E(n,f"{note}",s,a=a,g=c)
# additions: kind name -> entries
add={
'Prosciutto crudo':[
 H('Crudo di Cuneo','Italy','PDO raw ham of the Cuneo area, Piedmont.',ITA),
 H('Prosciutto amatriciano','Italy','PGI raw ham of Lazio.'),
 H('Prosciutto di suino nero dei Nebrodi','Italy','Sicilian raw ham from the Nebrodi black pig, listed without a protected status.'),
 H('Prosciutto di Bassiano','Italy','Raw ham of Bassiano, Lazio, listed without a protected status.'),
 H('Prosciutto di Venticano','Italy','Raw ham of Venticano, Campania, listed without a protected status.'),
 H('Prosciutto di Faeto','Italy','Raw ham of Faeto, Apulia, listed without a protected status.'),
 H('Prosciutto della Majella','Italy','Raw ham of the Majella area, Abruzzo, listed without a protected status.'),
 H('Prosciutto crudo di suino nero Casertano','Italy','Raw ham from the black Casertana pig, Campania.'),
 H('Prosciutto crudo dell\'Irpinia','Italy','Raw ham of Irpinia, Campania, listed without a protected status.')],
'Cured shoulder (paleta)':[E('Paleta de Teruel','Cured pork shoulder with PDO status, named beside Jamón de Teruel.',JAM)],
'Regional dry-cured hams':[
 H('Jambon noir de Bigorre','France','PDO ham from black Gascon pigs.'),
 H('Jambon de Kintoa','France','PDO ham from Basque pigs.'),
 H('Jambon de Corse','France','PDO ham from black Nustrale pigs of Corsica.'),
 H("Jambon d'Auvergne",'France','PGI ham of the Auvergne.'),
 H("Jambon de l'Ardèche",'France','PGI ham of the Ardèche.'),
 H('Jambon de Lacaune','France','PGI ham of Lacaune.'),
 H('Jambon de Vendée','France','PGI ham of the Vendée.'),
 H('Jambon sec des Ardennes','France','PGI dry-cured ham of the Ardennes.'),
 H('Jambon du Limousin','France','Ham of the Limousin, made from black cul-noir pigs.'),
 H('Rugao ham','China','Dry-cured ham of Jiangsu, first prepared in 1851.')],
'Smoked raw ham':[
 H('Tyrolean Speck','Italy and Austria','Juniper-flavoured boneless smoked ham, first mentioned in the early 13th century.',a='Tiroler Speck'),
 H('Éisleker ham','Luxembourg','Ham brine-cured then smoked, from the Éislek region.')],
'Cotechino':[E('Cotechino Modena','PGI fresh pork sausage of Modena, registered 1999.',ITA,y='1999'),
 E('Zampone Modena','PGI sausage of the Modena area stuffed into a pig trotter, registered 1999.',ITA,y='1999')],
'Italian sausage':[E('Salsiccia di Calabria','PDO fresh pork sausage of Calabria, registered 1998.',ITA,y='1998')],
'Italian salame':[
 E('Salame Brianza','PDO salame of Brianza, Lombardy, registered 1996.',ITA,y='1996'),
 E('Salame Cremona','PGI salame of Cremona, registered 2007.',ITA,y='2007'),
 E("Salame d'oca di Mortara",'PGI goose salame of Mortara, Lombardy, registered 2004.',ITA,y='2004'),
 E('Salame Piacentino','PDO salame of Piacenza, registered 1996.',ITA,y='1996'),
 E('Salame S. Angelo','PGI salame of Sant\'Angelo di Brolo, Sicily, registered 2008.',ITA,y='2008')],
'Protected-origin & breed lamb':[E('Agnello di Sardegna IGP','PGI lamb of Sardinia, registered 2001.',ITA,y='2001'),
 E('Cordero manchego IGP','PGI lamb of La Mancha, named among Spain\'s protected meats.','https://elordenmundial.com/mapas-y-graficos/carnes-embutidos-espana-indicacion-geografica-protegida/')],
'Whole chicken':[E('Pollo del Prat','Chicken of El Prat de Llobregat, named among Spain\'s protected meats.','https://elordenmundial.com/mapas-y-graficos/carnes-embutidos-espana-indicacion-geografica-protegida/'),
 E('Perdue chicken','Chicken sold under the Perdue Farms name; Perdue ranked ninth in the 2025 Top 100 US meat and poultry processors.',PROV,mk='Perdue Farms',own='Perdue Farms',tier='Independent',cty='United States'),
 E("Pilgrim's Pride chicken","Chicken sold by Pilgrim's Pride, 64 % bought by JBS in 2010 and 75 % owned by 2014.",JBS,mk="Pilgrim's Pride",own='JBS S.A.',tier='Global group',cty='United States',own_y='2010')],
'Turkey':[E('Jennie-O turkey','Turkey brand acquired by Hormel in 1986.',HOR,mk='Jennie-O',own='Hormel Foods',tier='Independent',cty='United States',own_y='1986')],
'Toulouse sausage':[E('Saucisse de Toulouse','Coarse fresh pork sausage of Toulouse, listed under France.',SAUS)],
'Merguez':[E('Merguez','Spiced fresh sausage listed under Algeria.',SAUS)],
'Boerewors':[E('Boerewors','Coiled fresh sausage listed under South Africa, Namibia and Zimbabwe.',SAUS,v=[{"n":n,"mk":"","y":"","d":"variant of boerewors"} for n in ('Garlic wors','Karoowors','Spekwors','Kameeldoring')])],
'Weisswurst':[E('Weisswurst','White veal-and-pork sausage listed under Germany.',SAUS)],
'Cervelat':[E('Cervelat','Swiss cooked sausage listed under Switzerland.',SAUS)],
'Saveloy':[E('Saveloy','Seasoned sausage listed under the United Kingdom and Australia.',SAUS)],
'Chả lụa':[E('Chả lụa','Vietnamese pork sausage listed under Vietnam.',SAUS)],
'Pepperoni':[E('Pepperoni','American spicy salami listed under the United States.',SAUS)],
'Frankfurter & hot dog':[E('Bockwurst','German sausage listed under Germany and the United States.',SAUS),
 E('Ball Park','Hot dog brand of Hillshire Brands, bought by Tyson Foods in 2014.',TYS,mk='Ball Park',own='Tyson Foods',tier='Global group',cty='United States',own_y='2014')],
'Breakfast sausage':[E('Jimmy Dean','Breakfast sausage brand of Hillshire Brands, bought by Tyson Foods in 2014.',TYS,mk='Jimmy Dean',own='Tyson Foods',tier='Global group',cty='United States',own_y='2014')],
'Kielbasa & smoked sausage':[E('Kranjska klobasa','Slovenian smoked sausage, listed under Slovenia.',SAUS),
 E('Debrecener','Smoked sausage listed under Hungary and Austria.',SAUS),
 E('Rookworst','Dutch smoked sausage listed under the Netherlands.',SAUS)],
'Thai & Southeast Asian sausage':[E('Sai krok Isan','Fermented Thai sausage listed under Thailand.',SAUS),
 E('Naem','Fermented Thai pork sausage listed under Thailand.',SAUS),
 E('Lạp xưởng','Vietnamese dried sausage listed under Vietnam.',SAUS),
 E('Lao sausage','Sausage listed under Laos with sai gork and sai ua.',SAUS)],
'Fresh chorizo & longaniza':[E('Vigan longganisa','Philippine longganisa listed under the Philippines.',SAUS),
 E('Lucban longganisa','Philippine longganisa listed under the Philippines.',SAUS)],
'Luncheon meat':[E('SPAM','Tinned pork luncheon meat introduced by Hormel in 1937.',HOR,y='1937',mk='Hormel Foods',own='Hormel Foods',tier='National champion',cty='United States',
   v=[{"n":"SPAM Classic","mk":"Hormel Foods","y":"","d":"original recipe"},{"n":"SPAM Lite","mk":"Hormel Foods","y":"","d":"lower fat"},{"n":"SPAM Less Sodium","mk":"Hormel Foods","y":"","d":"lower salt"}]),
  E('Tulip luncheon meat','Pork luncheon meat of Tulip, a subsidiary of Danish Crown.',DCW,mk='Tulip',own='Danish Crown',tier='Independent',cty='Denmark')],
}
# the new ham/sausage entries: need own? only brand ones. Dedup
CTY={'Pick':'Hungary','Herz':'Hungary','Hénaff':'France','KellyBronze':'United Kingdom','Gressingham Duck':'United Kingdom'}
brandfix={ 'KellyBronze':('KellyBronze','Independent','United Kingdom'),'Gressingham duck':('owner not stated','Independent','United Kingdom'),
 'Pick salami':('Pick','Independent','Hungary'),'Herz salami':('Herz','Independent','Hungary'),'Pâté Hénaff':('Hénaff','Independent','France'),
 'Beyond Burger':('Beyond Meat','Independent','United States'),'Impossible Burger':('Impossible Foods','Independent','United States'),
 'Tofurky roast':('Tofurky','Independent','United States'),'Linda McCartney vegetarian range':('Linda McCartney Foods','Independent','United Kingdom'),
 'Quorn':('owner not stated','Independent','United Kingdom')}
gmap={'Jambon de Bayonne':'France','Carmarthen Ham':'Wales','Kraški pršut':'Slovenia','Presunto de Barrancos':'Portugal','Jinhua ham':'China','Country ham':'United States','Xuanwei ham':'China','Njeguški pršut':'Montenegro','Lacón gallego':'Spain','Anfu ham':'China','Elenski but':'Bulgaria'}
ndrop=0; stats=[]
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
SELBASE={
 'Prosciutto crudo':f"Follows the Italian PDO and PGI ham names in {ITA} and the ham rows of {HAMS}. Complete: 11 of 11 raw-ham and culatello names (PDO and PGI) in the Italian list, plus the unprotected Italian raw hams in the list of hams; the Italian page was read to character 100,000 of 106,491.",
 'Regional dry-cured hams':f"Follows the non-Italian, non-Spanish hams of {HAMS} that are dry-cured and eaten raw. Covers the French, Chinese, Welsh, Balkan and US hams in the list; Spanish, Italian and smoked hams sit in their own kinds. The page lists about 64 rows; cooked and glazed hams are in other kinds.",
 'Smoked raw ham':f"Follows the smoked raw hams of {HAMS}. Covers the German, South Tyrolean and Luxembourg hams in that list.",
 'Cotechino':f"Follows the Modena PGI names in {ITA} (Cotechino Modena and Zampone Modena). Complete: 2 of 2 in that page.",
 'Italian salame':f"Follows the salame rows of {ITA}. Complete: 8 of 8 Italian PDO and PGI salame names in the page, plus the unprotected names already held; the page was read to character 100,000 of 106,491.",
 'Protected-origin & breed lamb':f"Follows protected lamb names found on the pages cited on each entry and the Italian list {ITA}. Not claimed complete.",
}
GENERIC_SEL=lambda refs:f"No whole-space reference was fetched for this kind; entries follow {refs}. Not claimed complete."
def nl_for(dept,k):
    n=k['n']
    if dept=='Meat alternatives': return 'One entry is a branded meat-alternative product line; recipe generations and flavours are versions.'
    if dept=='Beef & veal': return 'One entry is a named beef scheme: a prefecture or protected-origin name or a breed-society brand; grades and breeds are attributes.'
    if dept in('Pork','Lamb & goat','Poultry','Game','Other meats'): return 'One entry is a named breed line, protected-origin product or brand of this kind; grades and breeds are attributes.'
    if dept=='Deli, cooked & tinned meats': return 'One entry is a named regional product or brand of this kind; recipes and sizes are versions.'
    if dept=='Ham, bacon & cured meats': return 'One entry is a named ham or cured meat, protected (PDO, PGI) or traditional; ages and cuts are versions.'
    return 'One entry is a named sausage, protected (PDO, PGI) or traditional, or a brand; recipes and sizes are versions.'
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      n=k['n']; m=k.pop('m',[]); r=k.pop('r',[])
      xs=k.get('x') or []
      have={norm(x['n']) for x in xs}|{norm(a) for x in xs for a in re.split(r' · ',x.get('a','')) if a}
      pn=set()
      for e in add.get(n,[]):
        if norm(e['n']) in have: continue
        # check global dup
        xs.append(e); have.add(norm(e['n'])); pn.add(e['n'].lower())
        if e['n']=='Boerewors': pn|={t[0].lower() for t in m}
        if e['n']=='SPAM': pn|={t[0].lower() for t in m if 'SPAM' in t[0]}|{'tulip pork luncheon meat'}
      if n=='Boerewors': pn|={t[0].lower() for t in m}
      if n=='Luncheon meat': pn|={t[0].lower() for t in m if t[0].startswith(('SPAM','Tulip'))}
      rem=[t for t in m if t[0].lower() not in pn]
      if rem or r: removed[n]={'m':rem,'r':r}; ndrop+=len(rem)
      if xs:
        k['x']=xs
        for x in xs:
          if x['n'] in brandfix:
            o,t,c=brandfix[x['n']]; x['own']=o; x['tier']=t; x['cty']=c; x.setdefault('own_y','')
          if n=='Regional dry-cured hams' and (x['n'] in gmap): x['g']=gmap[x['n']]
        if n=='Regional dry-cured hams' or n=='Smoked raw ham' or n=='Prosciutto crudo':
          k['xg']='country'
          for x in xs:
            if not x.get('g'): x['g']={'Prosciutto crudo':'Italy','Smoked raw ham':'Germany'}.get(n,'')
            if n=='Regional dry-cured hams' and not x['g']: x['g']='Other'
        k['nl']=nl_for(dp['n'],k)
        if n in SELBASE: k['sel']=SELBASE[n]
        else:
          urls=[]
          for x in xs:
            if x['s'] not in urls: urls.append(x['s'])
          k['sel']=GENERIC_SEL('the pages cited on each entry'+(f' and the country names of {SAUS}' if any(x['s']==SAUS for x in xs) else ''))
        stats.append((n,len(xs)))
# fix Prosciutto crudo existing Culatello: g Italy ok
# Meat box suppliers
def supplier(n,d_,s,g): 
    e=E(n,d_,s,mk=n,g=g); return e
box=None
for dp in d['depts']:
  for s in dp['s']:
    for k in s['k']:
      if k['n']=='Meat box': box=k
box['x']=[
 supplier('ButcherBox',"Named best overall in Fortune's 2026 guide to meat delivery services.",FORT,'Premium online butchers (US)'),
 supplier('GoodChop',"Named best customisable in Fortune's 2026 guide.",FORT,'Premium online butchers (US)'),
 supplier('Porter Road',"Named best butcher-style service in Fortune's 2026 guide.",FORT,'Premium online butchers (US)'),
 supplier('Backyard Butchers',"Named best for one-time purchases in Fortune's 2026 guide.",FORT,'Premium online butchers (US)'),
 supplier('Meatzy',"Named best for families in Fortune's 2026 guide.",FORT,'Premium online butchers (US)'),
 supplier('Crowd Cow',"Named best for grass-fed meat in Fortune's 2026 guide.",FORT,'Premium online butchers (US)'),
 supplier('Haloodies','First of four halal delivery services ranked by HalalSpy in 2026; HMC-certified, hand-slaughtered meat.',HSP,'Halal meat delivery (UK)'),
 supplier('Muslim Meat','Second in the HalalSpy 2026 ranking; HMC-certified, same-day delivery in London.',HSP,'Halal meat delivery (UK)'),
 supplier('Willowbrook Farm','Third in the HalalSpy 2026 ranking; HFA-certified farm-direct meat.',HSP,'Halal meat delivery (UK)'),
 supplier('Tayyib','Fourth in the HalalSpy 2026 ranking; HMC-certified, pasture-raised animals.',HSP,'Halal meat delivery (UK)')]
box['xg']='supplier list'
box['nl']='One entry is an online butcher or halal delivery service named by a fetched ranked list; delivery platforms themselves are in I3.'
box['sel']=f"Follows the six services ranked in Fortune's guide ({FORT}) and the four halal services ranked by HalalSpy ({HSP}). Complete: 6 of 6 and 4 of 4 in those pages. No ranked list of kosher meat delivery or of premium UK butchers could be fetched (the Delicious magazine page returned 403)."
box['see']=[["I3","Subscription boxes & deliveries","delivery and subscription platforms"]]
# market summaries
def ms(mkt,who,share,yr,s,note): return {"mkt":mkt,"who":who,"share":share,"yr":yr,"s":s,"note":note}
for dp in d['depts']:
  dp['t']=dp['t'].rstrip()+' Halal, kosher, organic and welfare certifications are tags on a product, not kinds.' if dp['n'] not in('Meat alternatives',) and 'certifications are tags' not in dp['t'] else dp['t']
  N=dp['n']
  if N=='Beef & veal':
    dp['ms']=[ms('US beef','JBS, Tyson, Cargill and Marfrig together','85 %',2021,BOELL,'combined share as the article states it; the article is dated 7 September 2021 and mixes data years')]
    dp['msum']='Four firms (JBS, Tyson, Cargill and Marfrig) are put at 85 % of US beef in a 2021 article. No share was found for other markets.'
  if N=='Pork':
    dp['ms']=[ms('US pork','JBS, Tyson and Hormel together','66 %',2021,BOELL,'combined share as the article states it; article dated 7 September 2021'),
              ms('German processed pork','Tönnies, Westfleisch, Vion, Müller Group and Danish Crown together','two-thirds',2021,BOELL,'share of processed pork in Germany, as the article states it'),
              ms('World pork exports','Danish Crown','',2021,DCW,'described as the world\'s largest pork exporter and Europe\'s largest pork producer; turnover about DKK 60 billion; owned by 5,620 Danish farmers')]
    dp['msum']='In the US three firms hold about two thirds of pork, and in Germany five firms hold two thirds of processed pork (2021 article). Danish Crown is a farmer-owned cooperative.'
  if N=='Poultry':
    dp['ms']=[ms('US chicken','JBS (Pilgrim\'s), Tyson, Sanderson Farms and Perdue together','51 %',2021,BOELL,'combined share as the article states it; article dated 7 September 2021')]
    dp['msum']='Four firms hold 51 % of US chicken in a 2021 article. Perdue ranked ninth among US meat and poultry processors in 2025.'
  if N=='Deli, cooked & tinned meats':
    dp['ms']=[ms('US meat and poultry processors by net sales',w,f"US${v:,} million",2025,PROV,f"rank {r} of the 2025 Top 100; fiscal year not stated") for r,w,v in [(1,'Cargill Meat Solutions Corp.',160000),(2,'Sysco Corp.',78800),(3,'Tyson Foods Inc.',53613),(4,'JBS USA',37300),(5,'Smithfield Foods Inc.',14140),(6,'Conagra Brands LLC',12051),(7,'Hormel Foods Inc.',11900),(8,'National Beef Packing Co. LLC',11900),(9,'Perdue Farms Inc.',10300),(10,'Seaboard Foods LLC',9100)]]+[
      ms('World meat processing','JBS S.A.','US$86.2 billion revenue',2025,JBS,'described as the world\'s largest meat processing enterprise'),
      ms('Processed and branded meat','Tyson Foods','US$54.4 billion revenue',2025,TYS,'second-largest chicken, beef and pork processor after JBS; owns Jimmy Dean, Ball Park and Hillshire Farm'),
      ms('Processed and branded meat','Hormel Foods','US$12.1 billion revenue',2025,HOR,'owns Spam, Jennie-O and Applegate')]
    dp['msum']='The 2025 Top 100 list puts Cargill, Sysco, Tyson, JBS USA and Smithfield first by net sales. JBS is the largest meat processor worldwide; Tyson owns Jimmy Dean and Ball Park; Hormel owns Spam.'
  if N=='Sausages & salami':
    dp['msum']='Branded sausage here is led by Tyson (Jimmy Dean, Ball Park, bought 2014) and Smithfield, which WH Group bought in 2013 for US$4.72 billion. No share figures were found.'
  if N=='Other meats':
    dp['msum']='Supplier layer: six US and four UK halal online butchers named by ranked lists in 2026 are under Meat box. No kosher delivery list could be fetched.'
# category b: certification criterion
d['b'].append({"m":"Certification tags","v":"welfare: Global Animal Partnership step 1 < 2 < 3 < 4 < 5 < 5+","w":"Halal, kosher, organic and welfare schemes are tags on a product. Kosher: OU (1923), OK (1935), KOF-K, Star-K and CRC certify over 80 % of US kosher food (Wikipedia). Welfare: RSPCA Assured (UK, 1994), Certified Humane (US, 2003), Global Animal Partnership (US, 2008). Halal: HMC and HFA in the UK."})
# brands
have={x['n'].lower() for x in b['b']}
def B(n,c,seg,kf,dd,s,f=''):
    if n.lower() in have: return
    x={"n":n,"c":c,"seg":seg,"kf":kf,"d":dd,"s":s}
    if f: x['f']=f
    b['b'].append(x); have.add(n.lower())
B('JBS S.A.','Brazil','Mainstream','meat processor',"World's largest meat processor; owns Swift, Pilgrim's Pride, Seara, Moy Park and Primo Smallgoods.",JBS)
B("Pilgrim's Pride",'United States','Mainstream','chicken',"US chicken processor, 64 % bought by JBS in 2010.",JBS)
B('Smithfield Foods','United States','Mainstream','pork and ham','US pork processor, bought by WH Group in 2013 for US$4.72 billion.',SMI,'1936')
B('WH Group','China','Mainstream','meat processor','Parent of Smithfield Foods since 2013 (as Shuanghui Group).',SMI)
B('Danish Crown','Denmark','Mainstream','pork cooperative','Farmer-owned Danish cooperative; owner of Tulip.',DCW)
B('Ball Park','United States','Mainstream','hot dogs','Hot dog brand of Hillshire Brands, owned by Tyson since 2014.',TYS)
B('SPAM','United States','Mainstream','luncheon meat','Tinned pork luncheon meat introduced by Hormel in 1937.',HOR,'1937')
B('Jennie-O','United States','Mainstream','turkey','Turkey brand acquired by Hormel in 1986.',HOR)
B('OU Kosher','United States','Institution & issuer','kosher certifier','Orthodox Union kosher certification, founded 1923.','https://en.wikipedia.org/wiki/Kosher_certification_agency','1923')
B('OK Laboratories','United States','Institution & issuer','kosher certifier','Kosher certifier founded 1935 by Abraham Goldstein.','https://en.wikipedia.org/wiki/Kosher_certification_agency','1935')
for n in ('Star-K','KOF-K','CRC'): B(n,'United States','Institution & issuer','kosher certifier','One of the five US kosher agencies certifying over 80 % of US kosher food.','https://en.wikipedia.org/wiki/Kosher_certification_agency')
B('Humane Farm Animal Care','United States','Institution & issuer','welfare certifier','Runs the Certified Humane label, founded 2003.','https://en.wikipedia.org/wiki/Certified_Humane','2003')
B('RSPCA Assured','United Kingdom','Institution & issuer','welfare certifier','Farm assurance label run by the RSPCA, founded 1994 as Freedom Food.','https://en.wikipedia.org/wiki/RSPCA_Assured','1994')
B('Global Animal Partnership','United States','Institution & issuer','welfare certifier','Five-step animal welfare rating, founded 2008.','https://en.wikipedia.org/wiki/Global_Animal_Partnership','2008')
for n,dd,s in [('GoodChop','Online meat delivery named best customisable by Fortune in 2026.',FORT),('Porter Road','Online butcher named best butcher-style by Fortune in 2026.',FORT),('Backyard Butchers','Online butcher named best for one-time purchases by Fortune in 2026.',FORT),('Meatzy','Meat delivery named best for families by Fortune in 2026.',FORT),('Crowd Cow','Meat delivery named best for grass-fed meat by Fortune in 2026.',FORT)]: B(n,'United States','Specialist','meat delivery',dd,s)
for n,dd in [('Haloodies','HMC-certified halal meat delivery, first in the HalalSpy 2026 ranking.'),('Muslim Meat','HMC-certified halal delivery, second in the HalalSpy 2026 ranking.'),('Willowbrook Farm','HFA-certified farm-direct halal meat, third in the HalalSpy 2026 ranking.'),('Tayyib','HMC-certified pasture-raised halal meat, fourth in the HalalSpy 2026 ranking.')]: B(n,'United Kingdom','Specialist','halal meat delivery',dd,HSP)
for x in b['b']:
  if x['n']=='ButcherBox': x['d']=x['d']
def wr(p,o):
    json.dump(o,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
wr(R+'out/J1.json',d); wr(R+'out/J1_brands.json',b); wr(R+'work/V4_J1/removed_m.json',removed)
print(stats, ndrop)
