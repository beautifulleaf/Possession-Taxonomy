import json,re,os
AOC='https://en.wikipedia.org/wiki/List_of_Appellation_d%27Origine_Contr%C3%B4l%C3%A9e_wines'
LR='https://en.wikipedia.org/wiki/List_of_appellations_in_Languedoc-Roussillon'
VDN='https://en.wikipedia.org/wiki/Vin_doux_naturel'
C1855='https://en.wikipedia.org/wiki/Bordeaux_Wine_Official_Classification_of_1855'
SE='https://en.wikipedia.org/wiki/Classification_of_Saint-%C3%89milion_wine'
GR='https://en.wikipedia.org/wiki/Classification_of_Graves_wine'
CH='https://www.enviedechamp.com/en/blog/29-the-notion-of-cru-in-champagne'
raw="""PASTE"""
rows=[]
for l in open('aoc.txt',encoding='utf8'):
    p=[x.strip() for x in l.split('|')]
    if len(p)==3: rows.append(p)
fix={'Cabardes':'Cabardès','Corbieres':'Corbières','Faugeres':'Faugères','Moulin a vent':'Moulin-à-Vent','Mazoyeres-Chambertin':'Mazoyères-Chambertin','Latricieres-Chambertin':'Latricières-Chambertin','Chambertin-Clos-de-Beze':'Chambertin-Clos de Bèze','Minervois-La Liviniere':'Minervois-La Livinière','Gros-plant-du-pays-nantais':'Gros Plant du Pays Nantais','Gaillac Premieres Côtess':'Gaillac Premières Côtes','Premieres Côtes de Blaye':'Premières Côtes de Blaye','Premieres Côtes de Bordeaux':'Premières Côtes de Bordeaux','Muscadet-Sevre et Maine':'Muscadet-Sèvre et Maine','Jasnieres':'Jasnières','Corse or Vin de Corse':'Corse (Vin de Corse)','Moulis or Moulis-en-Médoc':'Moulis (Moulis-en-Médoc)','Beaumes de Venise':'Beaumes de Venise','Charlemagne':'Charlemagne','Chorey-les-Beaune':'Chorey-lès-Beaune','Savigny-les-Beaune':'Savigny-lès-Beaune','Cairanne':'Cairanne','Bourgogne Epineuil':'Bourgogne Épineuil','Côtes de Toul':'Côtes de Toul','Mazis-Chambertin':'Mazis-Chambertin','Blanquette méthode ancestrale':'Blanquette méthode ancestrale','Bergerac sec':'Bergerac sec','Bâtard-Montrachet':'Bâtard-Montrachet','Mâcon':'Mâcon','Bordeaux Haut-Benauge':'Bordeaux Haut-Benauge','Vin de Savoie':'Vin de Savoie'}
ent={}
order=[]
for n,reg,y in rows:
    n=fix.get(n,n)
    if n in ent: continue
    yy=y if re.match(r'^\d{4}$',y) else ''
    ent[n]=dict(n=n,reg=reg,y=yy,s=AOC); order.append(n)
# extra from LR page and VDN page
for n in ['Berlou','Coteaux du Languedoc Pic Saint-Loup','Roquebrun','Terrasses du Larzac','La Clape','Côtes du Roussillon Les Aspres','Côtes du Roussillon Villages Caramany','Côtes du Roussillon Villages Lesquerde','Côtes du Roussillon Villages Latour de France','Côtes du Roussillon Villages Tautavel']:
    ent[n]=dict(n=n,reg='Languedoc-Roussillon',y='',s=LR)
ent['Rasteau']=dict(n='Rasteau',reg='Rhône',y='',s=VDN)
ent['Muscat du Cap Corse']=dict(n='Muscat du Cap Corse',reg='Corsica',y='',s=VDN)
S=lambda *a:list(a)
K={}  # (shelf,kind)->names with group
def grp(kind,names): K[kind]=names
GC_N=['Chambertin','Chambertin-Clos de Bèze','Chapelle-Chambertin','Charmes-Chambertin','Griotte-Chambertin','Latricières-Chambertin','Mazis-Chambertin','Mazoyères-Chambertin','Ruchottes-Chambertin','Clos de la Roche','Clos Saint-Denis','Clos de Tart','Clos des Lambrays','Bonnes-Mares','Musigny','Clos de Vougeot','Échezeaux','Grands Échezeaux','La Grande Rue','La Romanée','La Tâche','Richebourg','Romanée-Conti','Romanée-Saint-Vivant']
GC_B=['Corton','Corton-Charlemagne','Charlemagne','Montrachet','Bâtard-Montrachet','Bienvenues-Bâtard-Montrachet','Chevalier-Montrachet','Criots-Bâtard-Montrachet']
GRAND=set(GC_N+GC_B)
LAYOUT=[
('Bordeaux','Wine regions of the Gironde, named by bank, district and style of wine.','kinds from the Médoc on the Left Bank round to the Right Bank, the sweet whites and the regional appellations',[
 ('Bordeaux: Left Bank appellations','Médoc appellations on the left bank of the Gironde estuary, led by the red wines of the 1855 classification.',['Médoc','Haut-Médoc','Listrac-Médoc','Moulis (Moulis-en-Médoc)','Margaux','Pauillac','Saint-Julien','Saint-Estèphe'],None,'Left Bank',[('Colour',['Red']),('Main grapes',['Cabernet Sauvignon','Merlot','Cabernet Franc','Petit Verdot'])]),
 ('Bordeaux: Graves and Pessac-Léognan appellations','Appellations of the Graves district south of Bordeaux city, red and dry white.',['Graves','Graves Supérieures','Pessac-Léognan'],None,'Graves',[('Colour',['Red','White','Sweet white']),('Main grapes',['Cabernet Sauvignon','Merlot','Sémillon','Sauvignon Blanc'])]),
 ('Bordeaux: Right Bank appellations','Appellations on the right bank of the Dordogne and Isle, led by Saint-Émilion and Pomerol.',['Saint-Émilion','Saint-Émilion Grand Cru','Lussac-Saint-Émilion','Montagne Saint-Émilion','Puisseguin Saint-Émilion','Saint-Georges Saint-Émilion','Pomerol','Lalande-de-Pomerol','Néac','Fronsac','Blaye','Côtes de Blaye','Premières Côtes de Blaye','Côtes de Bourg','Côtes de Castillon','Bordeaux Côtes de Francs'],None,'Right Bank',[('Colour',['Red','White']),('Main grapes',['Merlot','Cabernet Franc','Cabernet Sauvignon'])]),
 ('Bordeaux: sweet white appellations','Appellations for botrytised or late-harvest sweet white Bordeaux.',['Sauternes','Barsac','Cérons','Loupiac','Cadillac','Sainte-Croix-du-Mont','Bordeaux moelleux'],None,'Sweet white',[('Colour',['Sweet white']),('Main grapes',['Sémillon','Sauvignon Blanc','Muscadelle'])]),
 ('Bordeaux: Entre-Deux-Mers and regional appellations','Appellations covering the whole Bordeaux region or the area between the Garonne and Dordogne.',['Bordeaux','Bordeaux supérieur','Bordeaux rosé','Bordeaux clairet','Bordeaux sec','Bordeaux Haut-Benauge','Entre-Deux-Mers','Entre-Deux-Mers-Haut-Benauge','Graves de Vayres','Premières Côtes de Bordeaux','Côtes de Bordeaux Saint-Macaire','Sainte-Foy-Bordeaux','Crémant de Bordeaux'],None,'Regional',[('Colour and style',['Red','White','Rosé','Clairet','Sparkling']),('Main grapes',['Merlot','Cabernet Sauvignon','Sauvignon Blanc','Sémillon'])]),
]),
('Burgundy','Wine regions from Chablis south to the Mâconnais.','kinds from north to south along the Burgundy escarpment',[
 ('Burgundy: Chablis and Auxerrois appellations','Chardonnay-led appellations around Chablis in the north.',['Petit Chablis','Chablis','Chablis Premier Cru','Chablis Grand Cru','Irancy','Saint-Bris','Tonnerre'],None,'Chablis',[('Colour',['White','Red']),('Main grapes',['Chardonnay','Pinot Noir','Sauvignon Blanc'])]),
 ('Burgundy: Côte de Nuits appellations','Mainly red village and grand cru appellations of the northern Côte d\'Or.',['Marsannay','Fixin','Gevrey-Chambertin','Morey-Saint-Denis','Chambolle-Musigny','Vougeot','Vosne-Romanée','Nuits-Saint-Georges','Côte de Nuits-villages','Vins Fins de la Côte de Nuits','Bourgogne Hautes-côtes de Nuits']+GC_N,'GC','Côte de Nuits',[('Colour',['Red','White']),('Main grapes',['Pinot Noir','Chardonnay'])]),
 ('Burgundy: Côte de Beaune appellations','Red and white village and grand cru appellations of the southern Côte d\'Or.',['Ladoix','Pernand-Vergelesses','Aloxe-Corton','Savigny-lès-Beaune','Chorey-lès-Beaune','Beaune','Pommard','Volnay','Volnay Santenots','Monthelie','Auxey-Duresses','Saint-Romain','Meursault','Blagny','Puligny-Montrachet','Chassagne-Montrachet','Saint-Aubin','Santenay','Maranges','Côte de Beaune','Côte de Beaune-Villages','Bourgogne Hautes-côtes de Beaune']+GC_B,'GC','Côte de Beaune',[('Colour',['Red','White']),('Main grapes',['Pinot Noir','Chardonnay'])]),
 ('Burgundy: Côte Chalonnaise appellations','Village appellations south of the Côte d\'Or around Chalon-sur-Saône.',['Bouzeron','Rully','Mercurey','Givry','Montagny'],None,'Côte Chalonnaise',[('Colour',['Red','White']),('Main grapes',['Pinot Noir','Chardonnay','Aligoté'])]),
 ('Burgundy: Mâconnais appellations','Mostly white Chardonnay appellations of the Mâcon hills.',['Mâcon','Mâcon supérieur','Mâcon-villages','Pouilly-Fuissé','Pouilly-Loché','Pouilly-Vinzelles','Saint-Véran','Viré-Clessé'],None,'Mâconnais',[('Colour',['White','Red','Rosé']),('Main grapes',['Chardonnay','Gamay','Pinot Noir'])]),
 ('Burgundy: regional and sparkling appellations','Appellations that may be made anywhere in Burgundy, including Crémant de Bourgogne.',['Bourgogne','Bourgogne aligoté','Bourgogne clairet','Bourgogne clairet Côte chalonnaise','Bourgogne Coulanges-la-Vineuse','Bourgogne Côte Saint-Jacques','Bourgogne Côtes d\'Auxerre','Bourgogne Côtes du Couchois','Bourgogne Épineuil','Bourgogne grand ordinaire','Bourgogne La Chapelle Notre-Dame','Bourgogne le Chapitre','Bourgogne Montrecul','Bourgogne mousseux','Bourgogne ordinaire','Bourgogne Passe-tout-grains','Bourgogne Vézelay','Bourgogne rosé','Crémant de Bourgogne'],None,'Regional',[('Colour and style',['Red','White','Rosé','Clairet','Sparkling']),('Main grapes',['Pinot Noir','Chardonnay','Aligoté','Gamay'])]),
]),
('Beaujolais','Gamay country between Burgundy and the Rhône.','kinds from regional wines to the ten crus',[
 ('Beaujolais: regional appellations','Beaujolais, Beaujolais-Villages and the Lyonnais.',['Beaujolais','Beaujolais-Villages','Coteaux du Lyonnais'],None,'Regional',[('Colour',['Red','White','Rosé']),('Main grapes',['Gamay','Chardonnay'])]),
 ('Beaujolais: the ten crus','The ten named village appellations at the top of the Beaujolais range.',['Brouilly','Côte de Brouilly','Chénas','Chiroubles','Fleurie','Juliénas','Morgon','Moulin-à-Vent','Régnié','Saint-Amour'],None,'Crus',[('Colour',['Red']),('Main grapes',['Gamay'])]),
]),
('Rhône','Wine regions along the Rhône valley, northern and southern.','kinds from the northern crus to the southern villages and regional wines',[
 ('Rhône: Northern appellations','Small steep-slope appellations between Vienne and Valence.',['Côte-Rôtie','Condrieu','Château-Grillet','Saint-Joseph','Crozes-Hermitage','Hermitage','Cornas','Saint-Péray'],None,'Northern Rhône',[('Colour',['Red','White']),('Main grapes',['Syrah','Viognier','Marsanne','Roussanne'])]),
 ('Rhône: Southern appellations','Named crus and villages of the southern Rhône, including sweet fortified Muscat and Grenache.',['Châteauneuf-du-Pape','Gigondas','Vacqueyras','Lirac','Tavel','Vinsobres','Cairanne','Rasteau','Beaumes de Venise','Muscat de Beaumes-de-Venise'],None,'Southern Rhône',[('Colour and style',['Red','White','Rosé','Sweet fortified']),('Main grapes',['Grenache','Syrah','Mourvèdre','Muscat à petits grains'])]),
 ('Rhône: regional, Diois and Ardèche appellations','Broad Côtes du Rhône appellations and those of the Drôme and Ardèche.',['Côtes du Rhône','Côtes du Rhône Villages','Côtes du Ventoux','Côtes du Luberon','Coteaux du Tricastin','Côtes du Vivarais','Costières de Nîmes','Châtillon-en-Diois','Clairette de Die','Coteaux de Die','Crémant de Die'],None,'Regional',[('Colour and style',['Red','White','Rosé','Sparkling']),('Main grapes',['Grenache','Syrah','Clairette','Muscat'])]),
]),
('Loire','Wine regions along the Loire valley from the Atlantic to the Massif Central.','kinds from the Nantais upstream to the Centre',[
 ('Loire: Nantais appellations','Muscadet and related white appellations near Nantes.',['Muscadet','Muscadet-Coteaux de la Loire','Muscadet-Côtes de Grandlieu','Muscadet-Sèvre et Maine','Gros Plant du Pays Nantais'],None,'Nantais',[('Colour',['White']),('Main grapes',['Melon de Bourgogne','Folle Blanche'])]),
 ('Loire: Anjou and Saumur appellations','Chenin Blanc and Cabernet Franc appellations of Anjou and Saumur, dry, sweet and sparkling.',['Anjou','Anjou-Coteaux de la Loire','Anjou-Gamay','Anjou mousseux','Anjou Villages','Anjou Villages Brissac','Bonnezeaux','Cabernet d\'Anjou','Cabernet de Saumur','Chaume','Coteaux de l\'Aubance','Coteaux du Layon','Coteaux de Saumur','Quarts de Chaume','Rosé d\'Anjou','Rosé de Loire','Saumur','Saumur-Champigny','Saumur mousseux','Savennières','Savennières-Coulée-de-Serrant','Savennières-Roche-aux-Moines','Crémant de Loire'],None,'Anjou-Saumur',[('Colour and style',['Red','White','Rosé','Sweet','Sparkling']),('Main grapes',['Chenin Blanc','Cabernet Franc','Gamay'])]),
 ('Loire: Touraine appellations','Appellations of the Touraine, Vendômois and Poitou.',['Touraine','Touraine-Amboise','Touraine-Azay-le-Rideau','Touraine-Mesland','Touraine Noble Joué','Bourgueil','Saint-Nicolas-de-Bourgueil','Chinon','Vouvray','Montlouis','Cheverny','Cour-Cheverny','Valençay','Jasnières','Coteaux du Loir','Coteaux du Vendômois','Haut-Poitou'],None,'Touraine',[('Colour and style',['Red','White','Rosé','Sweet','Sparkling']),('Main grapes',['Chenin Blanc','Cabernet Franc','Sauvignon Blanc','Gamay'])]),
 ('Loire: Centre appellations','Sauvignon Blanc and Pinot Noir appellations of the upper Loire and Allier.',['Sancerre','Pouilly-Fumé','Pouilly-sur-Loire','Menetou-Salon','Quincy','Reuilly','Coteaux du Giennois','Orléans','Orléans-Cléry','Saint-Pourçain','Côte Roannaise','Côtes du Forez'],None,'Centre',[('Colour',['White','Red','Rosé']),('Main grapes',['Sauvignon Blanc','Pinot Noir','Gamay'])]),
]),
('Alsace and Lorraine','Wine regions of north-eastern France.','kinds by region',[
 ('Alsace appellations','The regional, grand cru and sparkling appellations of Alsace.',['Alsace','Alsace Grand Cru','Crémant d\'Alsace'],None,'Alsace',[('Colour and style',['White','Red','Rosé','Sparkling']),('Main grapes',['Riesling','Gewurztraminer','Pinot Gris','Muscat','Pinot Noir'])]),
 ('Lorraine: Côtes de Toul','The Côtes de Toul appellation of Lorraine.',['Côtes de Toul'],None,'Lorraine',[('Colour',['Red','Rosé','White','Grey wine']),('Main grapes',['Pinot Noir','Gamay','Auxerrois'])]),
]),
('Champagne','The Champagne wine region and its appellations.','one kind',[
 ('Champagne appellations','The Champagne appellation, still Coteaux Champenois and Rosé des Riceys.',['Champagne','Coteaux Champenois','Rosé des Riceys'],None,'Champagne',[('Colour and style',['White sparkling','Rosé sparkling','Still red','Still white','Still rosé']),('Main grapes',['Chardonnay','Pinot Noir','Pinot Meunier'])]),
]),
('Jura, Savoie and Bugey','Wine regions of the eastern Alps foothills.','kinds by region',[
 ('Jura appellations','Appellations of the Jura, including Château-Chalon and L\'Étoile.',['Arbois','Château-Chalon','Côtes du Jura','L\'Étoile','Crémant du Jura'],None,'Jura',[('Colour and style',['White','Red','Rosé','Sparkling','Yellow wine']),('Main grapes',['Chardonnay','Savagnin','Poulsard','Trousseau','Pinot Noir'])]),
 ('Savoie and Bugey appellations','Alpine appellations of Savoie and the Bugey.',['Vin de Savoie','Roussette de Savoie','Crépy','Seyssel','Bugey','Roussette du Bugey'],None,'Savoie and Bugey',[('Colour and style',['White','Red','Rosé','Sparkling']),('Main grapes',['Jacquère','Altesse','Gamay','Mondeuse'])]),
]),
('South West France','Wine regions of the Garonne, Dordogne and Pyrenees foothills.','kinds by river basin or mountain area',[
 ('South West: Bergerac and Duras appellations','Appellations of the Dordogne basin around Bergerac, Duras and Marmande.',['Bergerac','Bergerac sec','Bergerac rosé','Côtes de Bergerac','Côtes de Bergerac Blanc','Monbazillac','Pécharmant','Rosette','Saussignac','Montravel','Côtes de Montravel','Haut-Montravel','Côtes de Duras','Côtes du Marmandais','Buzet'],None,'Bergerac',[('Colour and style',['Red','White','Rosé','Sweet white']),('Main grapes',['Merlot','Cabernet Sauvignon','Sauvignon Blanc','Sémillon'])]),
 ('South West: Garonne, Lot and Tarn appellations','Appellations of the Lot, Tarn and upper Garonne valleys, including Cahors.',['Cahors','Fronton','Gaillac','Gaillac Premières Côtes','Coteaux du Quercy','Côtes de Millau','Marcillac','Vins d\'Entraygues et du Fel','Vins d\'Estaing','Saint-Sardos'],None,'Lot and Tarn',[('Colour and style',['Red','White','Rosé','Sparkling','Sweet white']),('Main grapes',['Malbec','Négrette','Fer Servadou','Duras','Mauzac'])]),
 ('South West: Pyrenees and Gascony appellations','Appellations of the Basque Country, Béarn and Gascony.',['Béarn','Irouléguy','Jurançon','Madiran','Pacherenc du Vic-Bilh','Pacherenc du Vic-Bilh Sec','Saint-Mont','Tursan'],None,'Pyrenees and Gascony',[('Colour and style',['Red','White','Rosé','Sweet white']),('Main grapes',['Tannat','Petit Manseng','Gros Manseng','Petit Courbu'])]),
]),
('Languedoc-Roussillon','Wine regions of the French Mediterranean coast west of the Rhône.','kinds from the Hérault and Gard through the Aude to Roussillon, then the IGP wines',[
 ('Languedoc: Hérault and Gard appellations','Appellations of the eastern Languedoc, including Faugères, Saint-Chinian and the Muscat sweet wines.',['Coteaux du Languedoc','Coteaux du Languedoc Pic Saint-Loup','Terrasses du Larzac','Faugères','Saint-Chinian','Berlou','Roquebrun','Clairette du Languedoc','Clairette de Bellegarde','Frontignan','Muscat de Frontignan','Muscat de Lunel','Muscat de Mireval','Muscat de Saint-Jean de Minervois'],None,'Hérault and Gard',[('Colour and style',['Red','White','Rosé','Sweet fortified']),('Main grapes',['Grenache','Syrah','Carignan','Mourvèdre','Muscat à petits grains','Clairette'])]),
 ('Languedoc: Aude appellations','Appellations of the Aude, including Corbières, Minervois and Limoux sparkling wines.',['Corbières','Fitou','Minervois','Minervois-La Livinière','Cabardès','Côtes de la Malepère','La Clape','Limoux','Blanquette de Limoux','Blanquette méthode ancestrale','Crémant de Limoux','Clairette de Bellegarde'][:-1],None,'Aude',[('Colour and style',['Red','White','Rosé','Sparkling']),('Main grapes',['Grenache','Syrah','Carignan','Chardonnay','Chenin Blanc','Mauzac'])]),
 ('Roussillon appellations','Appellations of the Pyrenean foothills near Perpignan, including the vins doux naturels of Banyuls, Maury and Rivesaltes.',['Côtes du Roussillon','Côtes du Roussillon Les Aspres','Côtes du Roussillon Villages','Côtes du Roussillon Villages Caramany','Côtes du Roussillon Villages Lesquerde','Côtes du Roussillon Villages Latour de France','Côtes du Roussillon Villages Tautavel','Collioure','Banyuls','Banyuls Grand Cru','Maury','Rivesaltes','Muscat de Rivesaltes','Grand Roussillon'],None,'Roussillon',[('Colour and style',['Red','White','Rosé','Sweet fortified']),('Main grapes',['Grenache','Syrah','Carignan','Mourvèdre','Muscat'])]),
]),
('Provence and Corsica','Wine regions of the south-eastern coast and Corsica.','kinds by region',[
 ('Provence appellations','Mainly rosé appellations of Provence, with the red wines of Bandol.',['Côtes de Provence','Coteaux d\'Aix-en-Provence','Coteaux Varois','Coteaux de Pierrevert','Les Baux-de-Provence','Bandol','Cassis','Bellet','Palette'],None,'Provence',[('Colour',['Rosé','Red','White']),('Main grapes',['Grenache','Cinsault','Mourvèdre','Syrah','Rolle'])]),
 ('Corsica appellations','Appellations of Corsica.',['Corse (Vin de Corse)','Ajaccio','Patrimonio','Muscat du Cap Corse'],None,'Corsica',[('Colour and style',['Red','White','Rosé','Sweet fortified']),('Main grapes',['Niellucciu','Sciaccarellu','Vermentinu','Muscat'])]),
]),
]
IGP=['Bessan','Bérange','Cassan','Catalan wine','Caux','Cessenon','Cévennes','Côtes Catalanes','Côtes de Lastours','Côtes de Pérignan','Côtes de Prouille','Côtes de Thau','Côtes de Thongue','Côtes du Céressou','Côtes du Vidourle','Côtes du Brian','Collines de la Moure','Coteaux du Libron','Coteaux d\'Enserune','Coteaux de Béssilles','Coteaux de Cèze','Coteaux de Fenouillèdes','Coteaux de Fontcaude','Coteaux de la Cabrerisse','Coteaux de Laurens','Coteaux de Miramont','Coteaux de Murviel','Coteaux de Narbonne','Coteaux de Peyriac','Coteaux du Littoral Audois','Coteaux du Pont du Gard','Coteaux du Salagou','Coteaux Flaviens','Duché d\'Uzès','Gorges de l\'Hérault','Hauterive','Hauts-de-Badens','L\'Ardailhou','La Bénovie','La Cité de Carcassonne','La Côte Vermeille','La Haute Vallée de l\'Aude','La Haute Vallée de l\'Orb','La Vallée du Paradis','La Vaunage','La Vicomté d\'Aumelas','La Vistrenque','Mont-Baudile','Monts de la Grage','Pays du Torgan','Petite Crau','Pézenas','Principauté d\'Orange','Sables du Golfe du Lion','Val de Cesse','Val de Dagne','Val de Montferrand','Vals d\'Agly']
# versions
def V(n,y,d): return dict(n=n,mk='',y=y,d=d)
ver={}
def add(app,v): ver.setdefault(app,[]).append(v)
r55=[('Pauillac',[('Château Lafite Rothschild','First Growth'),('Château Latour','First Growth'),('Château Mouton Rothschild','First Growth (elevated from Second Growth in 1973)'),('Pichon Longueville Baron','Second Growth'),('Pichon Longueville Comtesse de Lalande','Second Growth'),('Duhart-Milon','Fourth Growth'),('Pontet-Canet','Fifth Growth'),('Batailley','Fifth Growth'),('Haut-Batailley','Fifth Growth'),('Grand-Puy-Lacoste','Fifth Growth'),('Grand-Puy-Ducasse','Fifth Growth'),('Lynch-Bages','Fifth Growth'),('Lynch-Moussas','Fifth Growth'),('d\'Armailhac','Fifth Growth'),('Haut-Bages-Libéral','Fifth Growth'),('Pédesclaux','Fifth Growth'),('Clerc-Milon','Fifth Growth'),('Croizet-Bages','Fifth Growth')]),
('Margaux',[('Château Margaux','First Growth'),('Rauzan-Ségla','Second Growth'),('Rauzan-Gassies','Second Growth'),('Durfort-Vivens','Second Growth'),('Lascombes','Second Growth'),('Brane-Cantenac','Second Growth'),('Kirwan','Third Growth'),('d\'Issan','Third Growth'),('Giscours','Third Growth'),('Malescot St. Exupéry','Third Growth'),('Cantenac-Brown','Third Growth'),('Boyd-Cantenac','Third Growth'),('Palmer','Third Growth'),('Desmirail','Third Growth'),('Ferrière','Third Growth'),('Marquis d\'Alesme Becker','Third Growth'),('Pouget','Fourth Growth'),('Prieuré-Lichine','Fourth Growth'),('Marquis de Terme','Fourth Growth'),('Dauzac','Fifth Growth'),('du Tertre','Fifth Growth')]),
('Saint-Julien',[('Léoville-Las Cases','Second Growth'),('Léoville-Poyferré','Second Growth'),('Léoville-Barton','Second Growth'),('Gruaud-Larose','Second Growth'),('Ducru-Beaucaillou','Second Growth'),('Lagrange','Third Growth'),('Langoa-Barton','Third Growth'),('Saint-Pierre','Fourth Growth'),('Talbot','Fourth Growth'),('Branaire-Ducru','Fourth Growth'),('Beychevelle','Fourth Growth')]),
('Saint-Estèphe',[('Cos d\'Estournel','Second Growth'),('Montrose','Second Growth'),('Calon-Ségur','Third Growth'),('Lafon-Rochet','Fourth Growth'),('Cos Labory','Fifth Growth')]),
('Haut-Médoc',[('La Lagune','Third Growth'),('La Tour Carnet','Fourth Growth'),('Belgrave','Fifth Growth'),('de Camensac','Fifth Growth'),('Cantemerle','Fifth Growth (added 1856)')]),
('Sauternes',[('d\'Yquem','Premier Cru Supérieur'),('La Tour Blanche','Premier Cru'),('Lafaurie-Peyraguey','Premier Cru'),('Clos Haut-Peyraguey','Premier Cru'),('Rayne-Vigneau','Premier Cru'),('Suduiraut','Premier Cru'),('Guiraud','Premier Cru'),('Rieussec','Premier Cru'),('Rabaud-Promis','Premier Cru'),('Sigalas-Rabaud','Premier Cru'),('d\'Arche','Deuxième Cru'),('Filhot','Deuxième Cru'),('de Malle','Deuxième Cru'),('Romer','Deuxième Cru'),('Romer du Hayot','Deuxième Cru'),('Lamothe','Deuxième Cru'),('Lamothe-Guignard','Deuxième Cru')]),
('Barsac',[('Coutet','Premier Cru'),('Climens','Premier Cru'),('de Myrat','Deuxième Cru'),('Doisy Daëne','Deuxième Cru'),('Doisy-Dubroca','Deuxième Cru'),('Doisy-Védrines','Deuxième Cru'),('Broustet','Deuxième Cru'),('Nairac','Deuxième Cru'),('Caillou','Deuxième Cru'),('Suau','Deuxième Cru')])]
for app,l in r55:
    for n,r in l:
        nm=n if n.startswith('Château') else 'Château '+n
        add(app,V(nm,'1855',r+', 1855 classification'))
add('Pessac-Léognan',V('Château Haut-Brion','1855','First Growth, 1855 classification (listed as Pessac, Graves); classified red in the 1953 Graves classification'))
for n in ['Château Bouscaut','Château Carbonnieux','Domaine de Chevalier','Château Latour-Martillac','Château Malartic-Lagravière','Château Olivier']: add('Pessac-Léognan',V(n,'1953','Graves classification, red and white (1953, revised 1959)'))
for n in ['Château Couhins','Château Couhins-Lurton','Château Laville Haut-Brion']: add('Pessac-Léognan',V(n,'1953','Graves classification, white (1953, revised 1959)'))
for n in ['Château de Fieuzal','Château Haut-Bailly','Château La Mission Haut-Brion','Château Pape Clément','Château Smith Haut Lafitte']: add('Pessac-Léognan',V(n,'1953','Graves classification, red (1953, revised 1959)'))
add('Pessac-Léognan',V('Château La Tour Haut-Brion','1953','Graves classification, red; discontinued after the 2005 vintage'))
for n in ['Château Pavie','Château Figeac']: add('Saint-Émilion Grand Cru',V(n,'2022','Premier grand cru classé A, 2022 classification'))
for n in ['Château Beauséjour (Duffau-Lagarrosse)','Château Beau-Séjour Bécot','Château Bélair-Monange','Château Canon','Château Canon-la-Gaffelière','Château Larcis Ducasse','Château Pavie-Macquin','Château Troplong Mondot','Château Trotte Vieille','Château Valandraud','Clos Fourtet','La Mondotte']: add('Saint-Émilion Grand Cru',V(n,'2022','Premier grand cru classé B, 2022 classification'))
for n in ['Ambonnay','Avize','Aÿ','Beaumont-sur-Vesle','Bouzy','Chouilly','Cramant','Louvois','Mailly-Champagne','Le Mesnil-sur-Oger','Oger','Oiry','Puisieulx','Sillery','Tours-sur-Marne','Verzenay','Verzy']: add('Champagne',V(n,'','Grand cru village, rated 100 % on the échelle des crus'))
vsrc={'Pauillac':C1855,'Margaux':C1855,'Saint-Julien':C1855,'Saint-Estèphe':C1855,'Haut-Médoc':C1855,'Sauternes':C1855,'Barsac':C1855,'Pessac-Léognan':GR,'Saint-Émilion Grand Cru':SE,'Champagne':CH}
used=set()
shelves=[]
def mkdesc(e):
    n=e['n']; r=e['reg']; y=e['y']
    t=('Grand cru appellation' if n in GRAND else 'Appellation')
    s=f"{t} of {r.replace('Rhone Valley','Rhône')}" 
    if e['s']==AOC and y: s+=f", AOC {y}"
    elif e['s']!=AOC: s+=", named on the page cited"
    return s+'.'
for sn,st,sax,kinds in LAYOUT:
    ks=[]
    for kn,kd,names,gcflag,reg,tt in kinds:
        xs=[]
        for nm in names:
            e=ent[nm]; used.add(nm)
            x=dict(n=nm,a='',d=mkdesc(e),mk='',y=e['y'],s=e['s'])
            if gcflag: x['g']='Grands crus' if nm in GRAND else 'Village, district and regional appellations'
            if nm in ver:
                x['v']=ver[nm]
                if vsrc.get(nm) and vsrc[nm]!=x['s']: x['s']=vsrc[nm] if nm!='Champagne' else x['s']
            xs.append(x)
        if gcflag: xs.sort(key=lambda x:(x['g']!='Grands crus',x['y'] or '9999',x['n']))
        else: xs.sort(key=lambda x:(x['y'] or '9999',x['n']))
        k=dict(n=kn,a='',d=kd,s=AOC,x=xs,tt=[[a,b] for a,b in tt],
          nl='One entry is a wine appellation (AOC or equivalent) with its own name and rules; classified châteaux or villages are versions.',
          sel="Every appellation of this district in Wikipedia's List of Appellation d'Origine Contrôlée wines, plus any named in the Languedoc-Roussillon list or the vin doux naturel article; classified estates and villages (1855, Graves 1953, Saint-Émilion 2022, Champagne grand cru villages) are versions.",
          xg=('by rank: grands crus first, then village and regional appellations' if gcflag else 'by year the appellation was established, then name'))
        ks.append(k)
    shelves.append(dict(n=sn,t=st,ax=sax,k=ks))
# IGP kind
igp=[dict(n=n,a='',d='Indication Géographique Protégée (IGP) wine zone of Languedoc-Roussillon, formerly a Vin de Pays.',mk='',y='',s=LR) for n in IGP]
igp.sort(key=lambda x:x['n'])
for sh in shelves:
    if sh['n']=='Languedoc-Roussillon':
        sh['k'].append(dict(n='Languedoc-Roussillon: IGP wines',a='Vin de Pays',d='Wines of a protected geographical indication in Languedoc-Roussillon, with looser rules than an AOC.',s=LR,x=igp,
          tt=[['Colour and style',['Red','White','Rosé','Sparkling']],['Grapes',['Any variety named in the zone\'s specification']]],
          nl='One entry is an IGP zone of Languedoc-Roussillon, whatever grape or colour it makes.',
          sel="Every IGP named in Wikipedia's List of appellations in Languedoc-Roussillon; the other French IGPs (75 in all per FranceAgriMer) were not found on a fetched list.",xg='alphabetical'))
        sh['ax']='kinds from the Hérault and Gard through the Aude to Roussillon, then the IGP wines'
miss=[n for n in order if n not in used]
print('unassigned',miss)
old=json.load(open('/home/user/Possession-Taxonomy/rebuild/out/J7.json'))
b0=old['depts'][0]['b'][0]
dept=dict(n='Wine of France',mode='mixed',
 t='French wine named by appellation, still, sparkling, sweet and fortified, with the classified estates and Champagne villages inside each; a wine of another country → its own wine department; a grape on its own → Grapes.',
 ax='Which region and appellation is the wine from, and which rank does it hold?',
 note='Organised region → district → appellation → classified estate or village. Producers outside a classification are not entries.',
 b=[b0],s=shelves,
 msum='French wine is mostly sold as appellation wine; the figures below are the last category shares and area on the cited pages.',
 ms=[dict(mkt='French wine production by category (2005 vintage)',who='AOC wines',share='53.4 %',yr=2005,s='https://en.wikipedia.org/wiki/French_wine',note='share of 43.9 million hl of production, excluding about 9.4 million hl for brandy'),
     dict(mkt='French wine production by category (2005 vintage)',who='Vin de Pays (now IGP) wines',share='33.9 %',yr=2005,s='https://en.wikipedia.org/wiki/French_wine',note='share of production'),
     dict(mkt='French vineyard area',who='All French vineyards',share='861,075 ha',yr=2007,s='https://en.wikipedia.org/wiki/French_wine',note='area at the 2007 harvest, as the page states')])
renames={"Bordeaux red blend":"Bordeaux: Left Bank appellations","Merlot":"Bordeaux: Right Bank appellations","Sauternes & Barsac":"Bordeaux: sweet white appellations","White blend":"Bordeaux: Entre-Deux-Mers and regional appellations","Pinot Noir":"Burgundy: Côte de Nuits appellations","Chardonnay":"Burgundy: Côte de Beaune appellations","Crémant":"Burgundy: regional and sparkling appellations","Gamay":"Beaujolais: the ten crus","Viognier":"Rhône: Northern appellations","Cabernet Franc":"Loire: Anjou and Saumur appellations","Chenin Blanc":"Loire: Touraine appellations","Melon de Bourgogne":"Loire: Nantais appellations","Sauvignon Blanc":"Loire: Centre appellations","Muscat":"Alsace appellations","Savagnin":"Jura appellations","Altesse":"Savoie and Bugey appellations","Pétillant naturel":"Languedoc: Aude appellations","Vin doux naturel":"Roussillon appellations","Non-vintage Champagne":"Champagne appellations","Vintage Champagne":"Champagne appellations","Prestige cuvée Champagne":"Champagne appellations","Rosé Champagne":"Champagne appellations"}
out=dict(depts=[dept],brands=[],renames=renames,moves=[])
os.makedirs('/home/user/Possession-Taxonomy/rebuild/out/J7_parts',exist_ok=True)
tmp='/home/user/Possession-Taxonomy/rebuild/out/J7_parts/WFR.json.tmp'
json.dump(out,open(tmp,'w'),ensure_ascii=False,indent=1)
os.rename(tmp,'/home/user/Possession-Taxonomy/rebuild/out/J7_parts/WFR.json')
print(sum(len(k['x']) for s in shelves for k in s['k']),'entries')
