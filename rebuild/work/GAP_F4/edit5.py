import json,os
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/F4.json'))
HUC='https://csm.huc.edu/?p=6796'; CH='https://www.chabad.org/library/article_cdo/aid/5283839/jewish/Why-Do-Torah-Scrolls-Have-Silver-Crowns.htm'; JM='https://collections.thejewishmuseum.org/collection/22372-torah-mantle'
def ent(n,y,desc,s,dt=''): return {'n':n,'a':'','d':desc,'mk':'','y':y,'s':s,'dt':dt,'v':[]}
shield={'n':'Torah shield (tas)','a':'Torah breastplate · choshen · tas','d':'Metal plate that hangs by chains over the front of a Torah scroll\'s mantle, often showing which scroll is read; also called a breastplate.','s':HUC,'m':[],'tg':['Jewish'],
 'tt':[['Material',['Silver','Silver gilt']],['Shape',['Crown-shaped','Rectangular','Round','Oval','Star of David']]],'see':[['F4','Torah finials','the other metal ornaments of the scroll']],
 'nl':'One entry is a named regional form or museum piece of Torah shield.',
 'sel':'No complete list exists. Follows the Hebrew Union College page Torah shield and the Chabad article on Torah crowns. Covers 4 forms and pieces named there.',
 'x':[ent('Italian crown-shaped shield','','Italian breastplate called a keter, shaped like a crown to evoke the crown of the Law.',HUC,'silver'),
 ent('Turkish tas','','Turkish shield called a tas or ziz, made oval, round or as a Star of David.',HUC,'silver'),
 ent('German and Dutch rectangular breastplate','17th century','Typically rectangular or square breastplate of Germany and Holland.',HUC,'silver'),
 ent('Augsburg neo-classical shield','1801','Shield by Franz Anton Gutwein of Augsburg, in the neo-classical style, held by the Hebrew Union College museum.',HUC,'silver')]}
mantle={'n':'Torah mantle','a':'meil · me\'il','d':'Fabric cover that dresses a Torah scroll, usually velvet with embroidery; the shield and finials are fitted over it.','s':JM,'m':[],'tg':['Jewish'],
 'tt':[['Material',['Velvet','Silk','Cotton velvet']],['Decoration',['Embroidered with metallic thread','Appliqued','Dedicatory inscription']]],'see':[['F4','Torah finials','the other ornaments dressing the scroll']],
 'nl':'One entry is a named regional form or museum piece of Torah mantle.',
 'sel':'No complete list exists. Follows the Jewish Museum (New York) record of one mantle; the POLIN Museum page could not be fetched (403). Covers 1 piece.',
 'x':[ent('Istanbul Torah mantle','c. 1881','Velvet cover embroidered with metallic thread in memory of Rachele, wife of Avraham Benguiat.',JM,'velvet · metallic thread')]}
yad=[ent('Mountain Jews flat-bar yad','','Flat bar pointer whose point is a broad leaf with a rounded tip; called etzba or kulmus.','https://en.wikipedia.org/wiki/Yad','bar'),
 ent('Mountain Jews twisted yad','','Bar twisted into a tight screw shape with a flat leaf-shaped point.','https://en.wikipedia.org/wiki/Yad','twisted bar'),
 ent('Russian filigree yad','19th century','Cast and filigree silver pointer, 11.5 inches long, in the Klutznick Collection at the Hebrew Union College museum.','https://csm.huc.edu/?p=9472','cast and filigree silver')]
for dp in d['depts']:
  for sh in dp['s']:
    names=[k['n'] for k in sh['k']]
    if 'Torah finials' in names:
      i=names.index('Torah finials')
      sh['k'][i+1:i+1]=[shield,mantle]
      for k in sh['k']:
        if k['n']=='Torah pointer':
          have={e['n'] for e in k['x']}
          k['x']+=[e for e in yad if e['n'] not in have]
          k['sel']='Follows the Wikipedia article Yad (found by search; the earlier page name returned 404) and a Hebrew Union College record. Covers 4 forms and pieces; the article names only Mountain Jews forms.'
        if k['n']=='Torah finials':
          k['sel']=k['sel'].replace(' Torah ornaments searched on Wikipedia (Torah ark has none), Chabad and a Hebrew Union College page: the shield or breastplate (tas) and the mantle have no kind here and are left for the owner queue. Covers 2 forms.',' Torah ornaments searched on Wikipedia (Torah ark has none), Chabad and a Hebrew Union College page: the shield and the mantle are now their own kinds. Covers 2 forms.')
json.dump(d,open(R+'work/GAP_F4/t.json','w'),ensure_ascii=False,indent=1); os.replace(R+'work/GAP_F4/t.json',R+'out/F4.json')
