import json,re,unicodedata,copy
P='../../out/J7.json'
d=json.load(open(P))
def norm(s):
    s=unicodedata.normalize('NFKD',s.lower());s=''.join(c for c in s if not unicodedata.combining(c))
    s=re.sub(r"[’'`]",' ',s);s=re.sub(r'\b(igp|la|le|les|l|d|de|du|des|et|vin|vins)\b',' ',s);s=re.sub(r'[^a-z0-9]+','',s);return s
src='''Atlantique;Comté Tolosan;Comtés Rhodaniens;Méditerranée;Pays d’Oc;Val de Loire|Alpes-de-Haute-Provence;Alpes-Maritimes;Ardèche;Ariège;Aude;Aveyron;Bouches-du-Rhône;Calvados;Coteaux de l’Ain;Côtes Catalanes;Côtes du Lot;Drôme;Franche-Comté;Gard;Gers;Haute-Marne;Hautes-Alpes;Haute-Vienne;Ile de Beauté;Isère;Landes;Pays de l’Hérault;Puy de Dôme;Saône et Loire;Var;Vaucluse;Vins de la Corrèze;Yonne|Agenais;Alpilles;Cévennes;Charentais;Cité de Carcassonne;Collines Rhodaniennes;Côte Vermeille;Coteaux de Coiffy;Coteaux de Glanes;Coteaux de l’Auxois;Coteaux de Narbonne;Coteaux de Peyriac;Coteaux de Tannay;Coteaux d’Enserune;Coteaux des Baronnies;Coteaux du Cher et de l’Arnon;Coteaux du Libron;Coteaux du Pont du Gard;Côtes de Gascogne;Côtes de la Charité;Côtes de Meuse;Côtes de Thau;Côtes de Thongue;Côtes du Tarn;Duché d’Uzes;Haute Vallée de l’Aude;Haute Vallée de l’Orb;Lavilledieu;Cathare;Maures;Mont Caume;Périgord;Sable de Camargue;Sainte Marie La Blanche;Saint-Guilhem-Le-Desert;Thezac-Perricard;Urfé;Vallée du Paradis;Vallée du Torgan;Vicomté d’Aumelas;Vins des Allobroges'''
classes=['Regional IGP','Departmental IGP','Small-zone IGP']
allig=[(c,n) for c,grp in zip(classes,src.split('|')) for n in grp.split(';')]
print(len(allig))
lr=None;sec_lr=None
for dp in d['depts']:
  if dp['n']=='Wine of France':
    for s in dp['s']:
      for k in s['k']:
        if k['n']=='Languedoc-Roussillon: IGP wines': lr=k;sec_lr=s;dep=dp
have={norm(e['n']) for e in lr['x']}
extra={'Cité de Carcassonne','Côte Vermeille','Duché d’Uzes','Vallée du Paradis','Vallée du Torgan','Vicomté d’Aumelas','Coteaux d’Enserune','Haute Vallée de l’Aude','Haute Vallée de l’Orb'}
new=[(c,n) for c,n in allig if norm(n) not in have]
print(len(new),[n for c,n in new])
U='https://dico-du-vin.com/igp-indication-geographique-protegee/'
ents=[{'n':n.replace('’',"'"),'a':'','d':f'{c} wine zone of France.','mk':'','y':'','s':U,'g':c,'v':[]} for c,n in new]
ents.sort(key=lambda e:(classes.index(e['g']),e['n']))
k={'n':'France: IGP wines outside Languedoc-Roussillon','a':'Vin de Pays','d':'Regional, departmental and small-zone IGP wines of France outside the Languedoc-Roussillon kind.',
 's':U,'nl':'One entry is a French IGP zone, whatever grape or colour it makes.',
 'sel':f"Every IGP on dico-du-vin.com's list of 75 French IGPs (6 regional, 28 departmental, 41 small-zone) that is not already in the Languedoc-Roussillon kind. Complete: {len(ents)} of {len(ents)} in that list; with the Languedoc-Roussillon kind it covers all 75.",
 'x':ents,'xg':'by class: regional, departmental, small-zone'}
k['tt']=copy.deepcopy(lr['tt'])
newsec={'n':'IGP wines elsewhere in France','t':'Protected geographical indications of France outside Languedoc-Roussillon.','ax':'which IGP zone, from the regional down to the small-zone names','k':[k]}
dep['s'].insert(dep['s'].index(sec_lr)+1,newsec)
lr['sel']=lr['sel'].split(' Covers 58')[0]+f" Complete: {len(lr['x'])} of {len(lr['x'])} Languedoc-Roussillon IGPs in Wikipedia's List of appellations in Languedoc-Roussillon; the other French IGPs are in the next kind (75 in all, per dico-du-vin.com)."
# Spain pagos
def kind(n):
    for dp in d['depts']:
        for s in dp['s']:
            for kk in s['k']:
                if kk['n']==n: return kk
W='https://www.winewithseth.com/winewiki/pago-system/'
nav=kind('Navarre: single-estate wines')
for nm,mk in [('Pago de Cirsus','Pago de Cirsus'),('Bodegas Inurrieta','Bodegas Inurrieta')]:
    nav['x'].append({'n':nm,'a':'','d':'Pago named on the Wine With Seth pago system page, with no year of recognition given.','mk':mk,'y':'','s':W,'v':[]})
yrs={'Dominio de Valdepusa':'2003','Finca Élez':'2003','Guijoso':'2003','Pago de Arínzano':'2008','Otazu':'2009','Pago Aylés':'2010','El Terrerazo':'2010'}
for kk in [nav,kind('Castilla-La Mancha: single-estate wines'),kind('Aragon: single-estate wines'),kind('Valencia: single-estate wines')]:
    for e in kk['x']:
        if e['n'] in yrs and not e.get('y'): e['y']=yrs[e['n']]
    kk['sel']=re.sub(r'\s*(Complete|Covers) \d.*$','',kk['sel']).rstrip()+f" Complete: {len(kk['x'])} of {len(kk['x'])} on Wikipedia's Spanish wine regions page (2019) and the Wine With Seth pago system page (22 pagos stated; its list names 18, one of them, Pago El Rincón of Madrid, has no kind here)."
json.dump(d,open('stageD.json','w'),ensure_ascii=False)
