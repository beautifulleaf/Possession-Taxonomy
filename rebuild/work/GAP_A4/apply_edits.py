import json,re,copy,os
O='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(O+'A4.json')); bj=json.load(open(O+'A4_brands.json')); b=bj['b']
bi={x['n']:x for x in b}
# --- brand register updates
cmap={'Osprey':('United States','1974','https://en.wikipedia.org/wiki/Osprey_Packs'),
'Monos':('Canada','2018','https://www.retaildive.com/news/monos-ceo-victor-tam-legacy-travel-luggage-brand-dtc/687936/'),
'Balenciaga':('Spain','1919','https://en.wikipedia.org/wiki/Balenciaga'),
'Oliver Peoples':('United States','1986','https://en.wikipedia.org/wiki/Oliver_Peoples'),
'Tanner Krolle':('United Kingdom','1856','https://en.wikipedia.org/wiki/Tanner_Krolle'),
'Mansur Gavriel':('United States','','https://www.laconceria.it/en/?p=75250'),
'Ridge':('United States','2013','https://en.wikipedia.org/wiki/Ridge_(company)'),
'Samuel Fox':('United Kingdom','','https://en.wikipedia.org/wiki/Samuel_Fox_(industrialist)'),
'Jenan Kazim':('United Kingdom','','https://www.core77.com/posts/36546/Making-a-Drip-Free-Car-Friendly-Umbrella'),
'Jean Marius':('France','1710','https://en.wikipedia.org/wiki/Umbrella'),
'Slawa Horowitz':('Austria','1929','https://en.wikipedia.org/wiki/Umbrella'),
'Kate Spade':('United States','1993','https://en.wikipedia.org/wiki/Kate_Spade_New_York'),
'Briggs & Riley':('United States','1993','https://en.wikipedia.org/wiki/Briggs_%26_Riley')}
def reg(n,c,f,s,dd='',seg='owner'):
    if n in bi:
        x=bi[n]
        if not x.get('c'): x['c']=c
        if not x.get('f') and f: x['f']=f
        return
    x={'n':n,'c':c,'f':f,'seg':seg,'d':dd,'lines':[],'eras':[],'sig':[],'sc':[],'rel':[],'s':s,'kf':'Mainstream'}
    b.append(x); bi[n]=x
for n,(c,f,s) in cmap.items(): reg(n,c,f,s,'')
reg('Challice Limited','Singapore','','https://en.wikipedia.org/wiki/Mulberry_Group','Majority owner of Mulberry with 56.4 per cent.')
reg('Oakley Capital','United Kingdom','','https://oakleycapital.com/latest-news/oakley-capital-acquires-globe-trotter/','Private equity business that agreed to buy a majority of Globe-Trotter in March 2020.')
reg('Eurazeo Brands','France','','https://fashionunited.uk/news/business/eurazeo-brands-invests-60-million-dollars-in-herschel-supply/2019110146021','Consumer brands division of Eurazeo; bought a minority stake in Herschel Supply in 2019.')
reg('L Catterton','','','https://fashionunited.uk/news/business/bernard-arnaults-l-catterton-snaps-up-stake-in-polene/2024083077337','Private-equity firm backed by LVMH; took a minority stake in Polène in 2024.')
reg('Tapestry, Inc.','United States','','https://en.wikipedia.org/wiki/Kate_Spade_New_York','Owner of Coach and Kate Spade New York; bought Kate Spade & Company in July 2017.')
reg('GF Capital Management & Advisors','United States','','https://www.laconceria.it/en/?p=75250','New York private equity fund that bought the core assets of Mansur Gavriel in 2019.')
reg('U.S. Luggage LLC','United States','','https://en.wikipedia.org/wiki/Briggs_%26_Riley','Bought Briggs & Riley in August 2000 with Richard Krulik.')
# --- entries
ENT=[e for dp in d['depts'] for sh in dp['s'] for k in sh['k'] for e in (k.get('x') or [])]
def kind(name):
    for dp in d['depts']:
        for sh in dp['s']:
            for k in sh['k']:
                if k['n']==name: return k
names={e['n'].lower() for e in ENT}
def addentry(kn,mk,n,desc,y,s):
    if n.lower() in names: return False
    k=kind(kn); tpl=copy.deepcopy([e for e in ENT if e['mk']==mk][0])
    tpl.update({'n':n,'d':desc,'y':y,'s':s,'v':[],'a':'','dt':''})
    k['x'].append(tpl); ENT.append(tpl); names.add(n.lower()); return True
added=[]
FL='https://luxe.digital/lifestyle/style/best-fendi-bags/'
for n,y,desc in [('Fendi First','2021','Soft pouch with an oversized F clasp.'),('Fendigraphy','2022','Crescent-curved hobo bag.'),('Fendi Sunshine','2020','Structured tote sold from small to large.'),('Fendi Origami','2023','Magnetic bag that folds into a bucket or opens into a shopper.'),('Fendi By The Way','2014','Barrel-shaped bag with a detachable strap.'),("Fendi C'Mon",'2023','Structured satchel in medium, mini and nano sizes.'),('Fendi Mon Tresor','2018','Drawstring bucket bag.'),('Fendi Kan I','2017','Structured everyday bag.')]:
    if addentry('Shoulder bag','Fendi',n,desc,y,FL): added.append(n)
LV='https://luxe.digital/style/best-louis-vuitton-bags/'
for n,y,desc in [('Petite Malle','2014','Small trunk-shaped bag.'),('Dauphine','2019','Reissue of a 1970s Louis Vuitton design, returned in the spring 2019 collection.'),('Twist','2015','Bag with the Louis Vuitton twist lock.'),('Looping','2002','Louis Vuitton bag listed by the guide with a 2002 date.'),('Lockit','2016','Louis Vuitton bag listed by the guide with a 2016 date.')]:
    if addentry('Shoulder bag','Louis Vuitton',n,desc,y,LV): added.append(n)
HL='https://legitapp.com/blog/12-must-know-hermes-bags'
for n,desc in [('Roulis','Hermès bag described as having a distinctive curved shape.'),('Massai','Hermès bag worn as a crossbody or shoulder bag.')]:
    if addentry('Shoulder bag','Hermès',n,desc,'',HL): added.append(n)
# Kate Spade
k=kind('Shoulder bag'); ks=copy.deepcopy([e for e in ENT if e['mk']=='Coach'][0])
if 'kate spade sam' not in names:
    ks.update({'n':'Kate Spade Sam','d':'The handbag the Kate Spade business started with in 1993.','y':'','s':'https://en.wikipedia.org/wiki/Kate_Spade_New_York','v':[],'mk':'Kate Spade','own':'Tapestry, Inc.','own_y':'2017','tier':'Global group','cty':'United States','a':'','dt':''})
    k['x'].append(ks); ENT.append(ks); added.append('Kate Spade Sam')
# --- owners
OWN={'Herschel Supply Co.':('Herschel Supply Co.','Independent',''),
'Mulberry':('Challice Limited','Independent',''),
'Globe-Trotter':('Oakley Capital','Independent','2020'),
'Polène':('Polène founders (Mothay family)','Independent',''),
'Away':('Privately held (venture-backed)','Independent',''),
'Monos':('Privately held (venture-backed)','Independent',''),
'Briggs & Riley':('U.S. Luggage LLC','Independent','2000'),
'Mansur Gavriel':('GF Capital Management & Advisors','Independent','2019'),
'Kate Spade':('Tapestry, Inc.','Global group','2017'),
'Persol':('EssilorLuxottica','Global group','1995')}
for e in ENT:
    o=OWN.get(e['mk'])
    if o and (not e.get('own') or e['mk'] in('Persol',)):
        e['own'],e['tier']=o[0],o[1]
        if o[2] and not e.get('own_y'): e['own_y']=o[2]
    c=(bi.get(e['mk']) or {}).get('c','')
    if c and not e.get('cty'): e['cty']=c
    if e['mk']=='Balenciaga': e['cty']='Spain'
    if e['mk']:
        e['g']=(e.get('cty') or c or 'Country not stated')+' · '+e['mk']
    else: e['g']='Traditional and unattributed forms'
# --- sel / xg
FAM={'Handbags':"No complete list of named handbags exists; this kind follows the houses' own model pages and the guides named above, each house covered as far as its page loaded (Fendi 12 lines, Hermès and Louis Vuitton also from guide pages). Telfar, Kate Spade, Persol and Warby Parker pages named no further model lines.",
'Eyewear':"No complete list exists; follows the frame lines named on the pages above. Persol 649 and 714 come from a fetched guide; Warby Parker, Gentle Monster (collaboration collections only) and Tom Ford pages named no model lines.",
'Luggage & travel':"No complete list exists; follows the maker pages and overviews above. Briggs & Riley and Away pages named no lines beyond those listed.",
'Backpacks & belt bags':"No complete list exists; follows the maker pages and overviews above.",
}
changed=0
for dp in d['depts']:
  for sh in dp['s']:
    for k in sh['k']:
      if not k.get('x'): continue
      s=k['sel']; cut=len(s)
      for m in ('This kind holds',' Covers ','Complete:','No complete list'):
          i=s.find(m)
          if i>0: cut=min(cut,i)
      base=s[:cut].rstrip()
      if not base.endswith('.'): base+='.'
      k['sel']=base+' '+FAM.get(dp['n'],'No complete list exists; follows the maker pages and overviews named above.')
      k['xg']='by the maker\'s home country, then maker; traditional forms last'
      k['x'].sort(key=lambda e:(e['g']=='Traditional and unattributed forms',e['g'],e.get('y') or '9999',e['n']))
      changed+=1
tmp=O+'A4.json.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,O+'A4.json')
tmp=O+'A4_brands.json.tmp'; json.dump(bj,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,O+'A4_brands.json')
print('added',added,'kinds',changed)
