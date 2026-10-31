import json,copy,os,re
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'J9.json')); br=json.load(open(R+'J9_brands.json'))
W='https://www.wikidata.org/wiki/'
WP='https://en.wikipedia.org/wiki/'
# (name,cty): (own, own_y, source)
M={
('Vichy Catalan','Spain'):('Sociedad anónima Vichy Catalan','',W+'Q111043338'),
('Ifri Gazouz','Algeria'):('Ifri Group','',W+'Q130754413'),
('Pakola','Pakistan'):('Mehran Bottlers','',WP+'Pakola'),
('Milaf Cola','Saudi Arabia'):('Al Madinah Heritage','',W+'Q134392691'),
('Cola Turka','Turkey'):('Ülker','',W+'Q1107571'),
('Çamlıca','Turkey'):('Ülker','',W+'Q6035639'),
('Oasis','France'):('Suntory','',W+'Q3347884'),
('Natakhtari','Georgia'):('Efes Beverage Group','',W+'Q12013204'),
('Afri-Cola','Germany'):('Mineralbrunnen Überkingen-Teinach AG','',WP+'Afri-Cola'),
('Vita Cola','Germany'):('Thüringer Waldquell','',WP+'Vita_Cola'),
('Cidona','Ireland'):('Britvic','',WP+'Britvic'),
('Club','Ireland'):('Britvic','',W+'Q5136085'),
('MiWadi','Ireland'):('Britvic','',W+'Q6826958'),
('Mozell','Norway'):('Ringnes','',W+'Q114646384'),
('Solo (Norway)','Norway'):('Carlsberg Group','',WP+'Carlsberg_Group'),
('Villa','Norway'):('Ringnes','',W+'Q48358955'),
('Laranjada','Portugal'):('Madeira Brewery','',W+'Q3572103'),
('Baikal','Russia'):('PepsiCo','',W+'Q1860400'),
('Vinea','Slovakia'):('Kofola ČeskoSlovensko','',W+'Q1165857'),
('Apotekarnes Cola','Sweden'):('Pripps','',W+'Q2617585'),
('XL Cola','Sweden'):('Falcon Brewery','',W+'Q2645238'),
('Elmer Citro','Switzerland'):('Ramseier Suisse','',W+'Q1332913'),
('Vivi Kola','Switzerland'):('ViCOLLECTIVE AG','',W+'Q18413514'),
('Sukita','Brazil'):('Ambev','',W+'Q10374737'),
('Big Cola','Costa Rica'):('AJE Group','',W+'Q79357191'),
('Jupiña','Cuba'):('Cawy Bottling Company','',W+'Q16920231'),
('Nesbitt\'s','United States'):('Monarch Beverage Company','',W+'Q13516751'),
('Fever-Tree','United Kingdom'):('Fevertree Drinks plc','',WP+'Fever-Tree'),
('Innocent Smoothies','United Kingdom'):('The Coca-Cola Company','2013',WP+'Innocent_Drinks'),
('Kia-Ora','United Kingdom'):('The Coca-Cola Company','',W+'Q6403626'),
('V8','United States'):('Campbell Soup Company','1948',WP+'V8_(beverage)'),
('Kool-Aid','United States'):('Kraft Heinz','',W+'Q1531983'),
('Tang','United States'):('Mondelez International','',W+'Q2744433'),
('Crystal Light','United States'):('Kraft Heinz','',W+'Q5191273'),
('MiO','United States'):('Kraft Heinz','',W+'Q6826924'),
('Bikkle','Japan'):('Suntory','',W+'Q4907422'),
('Vitasoy','Hong Kong'):('Vitasoy International Holdings','',W+'Q7937007'),
('M-150 (Thailand)','Thailand'):('Osotspa','',WP+'Osotspa'),
('Shark','Thailand'):('Osotspa','',WP+'Osotspa'),
('Semtex','Czech Republic'):('Kofola ČeskoSlovensko','2009',WP+'Kofola'),
('Hell Energy Drink','Hungary'):('Hell Energy Hungary','',W+'Q12814582'),
('Materva','Cuba'):('Cawy Bottling Company','',W+'Q6786656'),
('Iyemon','Japan'):('Suntory','',W+'Q11379187'),
('Roots','Japan'):('Suntory Foods','',W+'Q11349209'),
('Wonda','Japan'):('Asahi Soft Drinks','',WP+'Asahi_Soft_Drinks'),
}
GLOBAL={'The Coca-Cola Company':'The Coca-Cola Company','PepsiCo':'PepsiCo','Suntory':'Suntory','Suntory Foods':'Suntory','Keurig Dr Pepper':'Keurig Dr Pepper'}
NOUN={'Water':'water','Sodas':'soda','Tonic & mixers':'mixer','Juices & smoothies':'juice','Syrups & cordials':'syrup and cordial','Fermented soft drinks':'fermented drink','Energy & sports drinks':'energy and sports drink','Ready-to-drink coffee & tea':'coffee and tea'}
def shelf(D,n):
    for s in D['s']:
        if s['n']==n: return s
def getkind(D,sn,kn,proto):
    s=shelf(D,sn)
    if s is None:
        s={'n':sn,'k':[]}; D['s'].append(s)
    for k in s['k']:
        if k['n']==kn: return k
    k=copy.deepcopy(proto); k['n']=kn; k['x']=[]; s['k'].append(k); return k
done=[]; moves=[]; found=set()
for D in d['depts']:
  for s in list(D['s']):
    for k in list(s['k']):
      for x in list(k.get('x',[])):
        key=(x['n'],x['cty'])
        if x.get('own') or key not in M: continue
        own,y,src=M[key]; found.add(key)
        x['own']=own
        if y: x['own_y']=y
        x['os']=src
        noun=NOUN[D['n']]
        if own in GLOBAL:
            og=GLOBAL[own]; x['tier']='Global group'
            sn='Global groups'; kn='%s %s brands'%(og if og!='The Coca-Cola Company' else 'The Coca-Cola Company',noun)
            if og=='The Coca-Cola Company' and D['n'] in('Juices & smoothies',): kn='The Coca-Cola Company juice brands'
        else:
            x['tier']='Independent'; sn='Independents'
            ind=shelf(D,'Independents')
            m=re.search(r': (.+)$',k['n']); reg=m.group(1) if m else None
            names=[kk['n'] for kk in ind['k']] if ind else []
            if len(names)==1 or (names and ':' not in names[0]): kn=names[0]
            else: kn='Independent %s brands: %s'%(noun,reg)
        proto=ind['k'][0] if (sn=='Independents' and ind) else (shelf(D,sn)['k'][0] if shelf(D,sn) else k)
        tk=getkind(D,sn,kn,proto)
        # rename descriptive text if newly created
        if not tk['x'] and tk is not k:
            tk['d']=tk['d'] if tk['d'] else ''
        if tk is not k:
            k['x'].remove(x); tk['x'].append(x); moves.append((x['n'],D['n'],k['n'],tk['n']))
      
# drop emptied kinds, record renames
ren=json.load(open(R+'J9_renames.json'))
for D in d['depts']:
  for s in D['s']:
    for k in list(s['k']):
      if not k.get('x') and k['n'] in [m[2] for m in moves]:
        s['k'].remove(k); ren[k['n']]=[m[3] for m in moves if m[2]==k['n']][0]; print('kind emptied',k['n'])
# order entries in touched kinds by g then n
for D in d['depts']:
  for s in D['s']:
    for k in s['k']:
      if any(m[3]==k['n'] for m in moves): k['x'].sort(key=lambda x:(x.get('g',''),x['n']))
# brand register
have={r['n'] for r in br['b']}
for key,(own,y,src) in M.items():
    if key in found and own not in have:
        have.add(own); br['b'].append({'n':own,'c':'','f':'','seg':'Mainstream','d':'Company named as owner of drink brands on a fetched reference.','lines':[],'eras':[],'sig':[own],'sc':[],'rel':[],'s':src,'kf':'owner'})
print(len(found),'filled; missing',[k for k in M if k not in found])
for m in moves: print(m)
json.dump(d,open(R+'J9.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'J9.json.tmp',R+'J9.json')
json.dump(br,open(R+'J9_brands.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'J9_brands.json.tmp',R+'J9_brands.json')
json.dump(ren,open(R+'J9_renames.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'J9_renames.json.tmp',R+'J9_renames.json')
