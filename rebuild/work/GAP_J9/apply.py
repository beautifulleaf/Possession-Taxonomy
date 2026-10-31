import json,os,copy,re
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'J9.json')); br=json.load(open(R+'J9_brands.json'))
W='https://en.wikipedia.org/wiki/'
# name -> (own, own_y, tier, role, os, extra d, move)
G=dict()
def E(n,own,os_,tier='Independent',oy='',role=None,dnote=None,glob=None):
    G[n]=dict(own=own,os=os_,tier=tier,oy=oy,role=role,dn=dnote,glob=glob)
E('Saratoga','BlueTriton Brands',W+'Saratoga_Spring_Water',oy=2021)
E('Sinalco','Sinalco International GmbH & Co.',W+'Sinalco')
E('Ting','Pepsi-Cola Jamaica Bottling Company',W+'Ting_(drink)',tier=None,oy=1999)
E('Sidral Mundet','Coca-Cola FEMSA',W+'Sidral_Mundet',tier=None)
E('Fritz-kola','Mirco Wiegert (about two-thirds, 2020)',W+'Fritz-kola',tier='Craft & indie')
E('Ale-8-One','Rogers family',W+'Ale-8-One')
E('Calpis / Calpico','Asahi Breweries',W+'Calpis')
E('Calpis Soda','Asahi Breweries',W+'Calpis')
E('Lipovitan D','Taisho Pharmaceutical',W+'Lipovitan')
E('Krating Daeng','T.C. Pharmaceutical Industries',W+'Krating_Daeng')
E('Bionade','Hassia Group',W+'Bionade',oy=2018)
E('5-hour Energy','Living Essentials LLC',W+'5-hour_Energy')
E('Prime Hydration','Prime Hydration LLC',W+'Prime_(drink)')
E('Prime Energy','Prime Hydration LLC',W+'Prime_(drink)')
E('C4','Nutrabolt',W+'Keurig_Dr_Pepper')
E('Electrolit','Grupo PiSA',W+'Keurig_Dr_Pepper')
E('Ghost','Keurig Dr Pepper',W+'Keurig_Dr_Pepper',tier='Global group',glob='Keurig Dr Pepper')
E('La Colombe Draft Latte','Chobani',W+'La_Colombe_Coffee_Roasters',oy=2023)
E('Starbucks bottled Frappuccino','Starbucks',W+'Frappuccino')
E('Kirin Gogo no Kocha','Kirin Beverage','https://www.kirin.co.jp/experience/factory/en/gogo/sukkiricafe/')
E('Franklin & Sons Tonic','Global Brands','https://globalbrands.co.uk/our-brands/franklin-sons/')
E("Rose's lime juice",'Keurig Dr Pepper',W+'Rose%27s_lime_juice',tier='Global group',glob='Keurig Dr Pepper')
E('Capri-Sonne','Wild',W+'Capri-Sun')
E('Capri-Sun pouch','Wild',W+'Capri-Sun')
E("GT's Kombucha",'GT Dave',W+'GT%27s_Living_Foods')
E('Vimto cordial','Nichols plc',W+'Vimto')
E('Sherbat-i-Azam','Dabur',W+'Rooh_Afza')
E('Bottlegreen elderflower cordial','SHS Group','https://shs-group.co.uk/portfolio/bottlegreen')
E('Cockta','Atlantic Grupa','https://en.wikipedia.org/wiki/Cockta',oy=2010)
E('Cedevita','Atlantic Grupa',W+'Atlantic_Grupa',oy=2001)
E('Kola Real','Ajegroup',W+'Kola_Real')
E('Bilz y Pap','CCU (Compañía Cervecerías Unidas)',W+'Bilz_y_Pap')
E('Kem','CCU (Compañía Cervecerías Unidas)',W+'Kem_(drink)')
E("Dr. Brown's",'Honickman Companies',W+"Dr._Brown's",tier='Independent')
E('Cristaline','Alma Group',W+'Pierre_Papillaud')
E('Twizza','Varun Beverages',"https://www.foodbusinessmea.com/varun-beverages-completes-us125-2m-acquisition-of-south-africas-twizza/",oy=2026)
E('Hamoud Boualem','Hamoud Boualem SPA','https://familybusinesshistories.org/?p=3883',tier='National champion',role='landmark',dnote='Family-owned; its beverages command nearly 50 percent of the Algerian soft drinks market, per a family-business history.')
E('Julmust','Roberts (syrup maker)',W+'Julmust',tier='National champion',role='landmark',dnote='Outsells Coca-Cola in Sweden during the Christmas season; about 50 percent of December soft drink volume, per the article.')
# locate
kinds={};loc={}
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      kinds[(dp['n'],k['n'])]=(dp,sh,k)
      for x in k['x']: loc.setdefault(x['n'],[]).append((dp,sh,k,x))
done=[];miss=[]
def find_kind(dp,name):
  for sh in dp['s']:
    for k in sh['k']:
      if k['n']==name: return sh,k
def indep_target(dp,sh,k):
  if sh['n']!='National & regional brands': return None
  nn=k['n'].replace('National','Independent',1)
  t=find_kind(dp,nn)
  if t: return t[1]
  nn2=nn.split(':')[0]
  t=find_kind(dp,nn2)
  if t: return t[1]
  ish=[s for s in dp['s'] if s['n'].startswith('Independents')][0]
  nk={a:copy.deepcopy(v) for a,v in k.items() if a!='x'}
  nk['n']=nn; nk['x']=[]
  ish['k'].append(nk); return nk
for n,g in G.items():
  if n not in loc: miss.append(n); continue
  dp,sh,k,x=loc[n][0]
  if x.get('own'): miss.append(n+' (already owned)'); continue
  x['own']=g['own']; x['os']=g['os']
  if g['tier']: x['tier']=g['tier']
  if g['oy']: x['own_y']=g['oy']
  if g['role']: x['role']=g['role']
  if g['dn']: x['d']=(x['d'].rstrip('. ')+'. '+g['dn']) if x['d'] else g['dn']
  tgt=None
  if g['glob']:
    for s2 in dp['s']:
      for k2 in s2['k']:
        if k2['n'].startswith(g['glob']+' '): tgt=k2;break
      if tgt:break
  elif g['tier']=='Independent' or g['tier']=='Craft & indie' and False:
    tgt=indep_target(dp,sh,k)
  if tgt is not None and tgt is not k:
    k['x'].remove(x); tgt['x'].append(x)
    done.append((n,k['n'],tgt['n']))
  else: done.append((n,k['n'],'(stay)'))
# market facts
for dp in d['depts']:
  if dp['n']=='Sodas':
    dp['ms'].append({"mkt":"Nigeria carbonated soft drinks","who":"Coca-Cola Nigeria","share":"market leader (no figure)","yr":2017,"s":"https://marketingedge.com.ng/coca-cola-tops-carbonated-drink-market-in-nigeria/","note":"Euromonitor International ranking as reported by Marketing Edge"})
  if dp['n']=='Water':
    dp['ms'].append({"mkt":"China bottled water","who":"Nongfu Spring","share":"top-selling brand (no figure)","yr":2012,"s":"https://en.wikipedia.org/wiki/Nongfu_Spring","note":"Nielsen data as quoted on the page; owned and chaired by founder Zhong Shanshan"})
# brand register
have={b['n'] for b in br['b']}
for o,c,s in [('Atlantic Grupa','Croatia',W+'Atlantic_Grupa'),('BlueTriton Brands','',W+'Saratoga_Spring_Water'),('Hassia Group','Germany',W+'Bionade'),('Chobani','',W+'La_Colombe_Coffee_Roasters'),('Honickman Companies','',W+"Dr._Brown's"),('Alma Group','France',W+'Pierre_Papillaud'),('Varun Beverages','India','https://www.foodbusinessmea.com/varun-beverages-completes-us125-2m-acquisition-of-south-africas-twizza/'),('Ajegroup','Peru',W+'Kola_Real'),('CCU (Compañía Cervecerías Unidas)','Chile',W+'Bilz_y_Pap'),('Wild','Germany',W+'Capri-Sun'),('Global Brands','',  'https://globalbrands.co.uk/our-brands/franklin-sons/'),('SHS Group','','https://shs-group.co.uk/portfolio/bottlegreen'),('Nutrabolt','',W+'Keurig_Dr_Pepper'),('Grupo PiSA','Mexico',W+'Keurig_Dr_Pepper'),('Hamoud Boualem SPA','Algeria','https://familybusinesshistories.org/?p=3883'),('Taisho Pharmaceutical','Japan',W+'Lipovitan'),('T.C. Pharmaceutical Industries','Thailand',W+'Krating_Daeng'),('Living Essentials LLC','United States',W+'5-hour_Energy'),('Prime Hydration LLC','United States',W+'Prime_(drink)'),('Sinalco International GmbH & Co.','Germany',W+'Sinalco'),('Dabur','India',W+'Rooh_Afza'),('Asahi Breweries','Japan',W+'Calpis'),('Pepsi-Cola Jamaica Bottling Company','Jamaica',W+'Ting_(drink)'),('Coca-Cola FEMSA','Mexico',W+'Sidral_Mundet'),('Rogers family','United States',W+'Ale-8-One'),('Kirin Beverage','Japan','https://www.kirin.co.jp/experience/factory/en/gogo/sukkiricafe/'),('Starbucks','United States',W+'Frappuccino'),('GT Dave','United States',W+'GT%27s_Living_Foods')]:
  if o not in have:
    br['b'].append({'n':o,'c':c,'f':'','seg':'Mainstream','d':'Brand owner named by a fetched reference.','lines':[],'eras':[],'sig':[o],'sc':[],'rel':[],'s':s,'kf':'soft drinks'}); have.add(o)
for p,o in (('J9.json',d),('J9_brands.json',br)):
  json.dump(o,open(R+p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+p+'.tmp',R+p)
print(len(done),'missing',miss)
for t in done: print(t)
