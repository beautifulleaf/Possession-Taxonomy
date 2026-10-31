import json,re,unicodedata
d=json.load(open('stageB.json'))
IWC='https://italianwinecentral.com/wp-content/uploads/DOCG-DOC-list-from-Italian-Wine-Central-July-2025.pdf'
REG={'Abruzzo':['Ortona'],'Basilicata':['Grottino di Roccanova'],'Campania':['Aversa','Casavecchia di Pontelatone'],
'Calabria':['Sant\'Anna di Isola Capo Rizzuto','Terre di Cosenza'],'Emilia-Romagna':['Colli d\'Imola','Emilia-Romagna','Romagna'],
'Friuli-Venezia Giulia':['Friuli (Friuli Venezia Giulia)','Friuli Colli Orientali'],'Liguria':['Portofino (Golfo del Tigullio)'],
'Lombardy':['Curtefranca','Oltrepò Pavese Pinot Grigio','Pinot Nero dell\'Oltrepò Pavese','Riviera del Garda Classico','Sangue di Giuda dell\'Oltrepò Pavese','Terre di Colleoni'],
'Marche':['Falerio','I Terreni di Sanseverino','San Ginesio','Serrapetrona','Terre di Offida'],'Molise':['Tintilia del Molise'],
'Piedmont':['Alba','Strevi','Valli Ossolane'],'Apulia':['Negramaro di Terra d\'Otranto'],'Sicily':['Pantelleria'],'Sardinia':['Cagliari'],
'Tuscany':['Val d\'Arno di Sopra','Valdichiana Toscana','Valdinievole','Vin Santo di Carmignano','Bolgheri Sassicaia','Grance Senesi','San Torpè','Terratico di Bibbona','Terre di Casole','Terre di Pisa'],
'Trentino-Alto Adige':['Valdadige Terradeiforti'],'Veneto':['Lessini Durello','Montello Asolo','Vigneti della Serenissima']}
tot=0
for dp in d['depts']:
    if dp['n']!='Wine of Italy': continue
    for s in dp['s']:
        for k in s['k']:
            if k['n'].endswith(': DOC appellations'):
                reg=k['n'].split(':')[0]
                new=REG.get(reg,[])
                have={e['n'] for e in k['x']}
                for nm in new:
                    if nm in have: continue
                    k['x'].append({'n':nm,'a':'','d':f'DOC appellation of {reg}.','mk':'','y':'','s':IWC,'v':[]}); tot+=1
                k['x'].sort(key=lambda e: unicodedata.normalize('NFKD',e['n']).lower())
                n=len(k['x'])
                base=k['sel'].split(' Covers 330')[0]
                k['sel']=base+f" Complete: {n} of {n} in Italian Wine Central's list of 332 DOC names (July 2025), with {len(new)} names added that Wikipedia's List of Italian DOC wines lacks."
# nominal check: Eastern Europe Romania left
def kind(n):
    for dp in d['depts']:
        for s in dp['s']:
            for k in s['k']:
                if k['n']==n: return k
def add(n,ents,sel_tail=None,sub=None):
    k=kind(n); have={e['n'] for e in k['x']}
    for e in ents:
        if e['n'] not in have:
            e.setdefault('a','');e.setdefault('y','');e.setdefault('v',[]);k['x'].append(e)
    if sel_tail:
        k['sel']=re.split(r'(No complete list exists;|Complete:|Covers \d)',k['sel'])[0].rstrip()+' '+sel_tail.format(n=len(k['x']))
W='https://en.wikipedia.org/wiki/'
def E(n,mk,d,s,cty=None,own=None,y=''):
    e={'n':n,'mk':mk,'d':d,'s':W+s,'y':y}
    if cty:e['cty']=cty
    if own:e['own']=own
    return e
add('Tennessee whiskey',[E('Benjamin Prichard\'s','Phil Prichard','Tennessee whiskey brand named on the Wikipedia Tennessee whiskey page.','Tennessee_whiskey','United States'),
 E('Chattanooga Whiskey','Chattanooga Whiskey Company','Tennessee whiskey brand named on the Wikipedia Tennessee whiskey page.','Tennessee_whiskey','United States'),
 E('Collier and McKeel','','Tennessee whiskey brand of Nashville, named on the Wikipedia Tennessee whiskey page.','Tennessee_whiskey','United States'),
 E('Farrar Distillery','Farrar Distillery','Tennessee whiskey distillery of Noah, named on the Wikipedia Tennessee whiskey page.','Tennessee_whiskey','United States'),
 E("Nelson's Green Brier",'Nelson\'s Green Brier Distillery','Nashville distillery named on the Wikipedia Tennessee whiskey page.','Tennessee_whiskey','United States'),
 E('Uncle Nearest Premium Whiskey','','Tennessee whiskey brand of Shelbyville, named on the Wikipedia Tennessee whiskey page.','Tennessee_whiskey','United States')],
 "Complete: 8 of 8 brands named on Wikipedia Tennessee whiskey (Jack Daniel's, George Dickel, Benjamin Prichard's, Chattanooga Whiskey, Collier and McKeel, Farrar, Nelson's Green Brier, Uncle Nearest) plus Gentleman Jack from the earlier edition; Ole Smoky is excluded because the page says its products are not sold as Tennessee whiskey.")
add('Rye whiskey',[E('Wild Turkey Rye','Wild Turkey','Rye whiskey named on the Wikipedia Rye whiskey page.','Rye_whiskey','United States','Campari Group'),
 E('George Dickel Rye','George Dickel','Rye whiskey named on the Wikipedia Rye whiskey page.','Rye_whiskey','United States','Diageo'),
 E('Pikesville Rye','Heaven Hill','Rye whiskey named on the Wikipedia Rye whiskey page.','Rye_whiskey','United States','Heaven Hill'),
 E('Jim Beam Rye','Jim Beam','Rye whiskey named on the Wikipedia Rye whiskey page.','Rye_whiskey','United States','Suntory Global Spirits'),
 E('Col. E. H. Taylor Rye','The Sazerac Company','Rye whiskey named on the Wikipedia Rye whiskey page.','Rye_whiskey','United States','The Sazerac Company'),
 E('Thomas H. Handy','The Sazerac Company','Rye whiskey named on the Wikipedia Rye whiskey page.','Rye_whiskey','United States','The Sazerac Company'),
 E("Jack Daniel's Rye",'Brown-Forman','Rye whiskey named on the Wikipedia Rye whiskey page.','Rye_whiskey','United States','Brown-Forman'),
 E('Alberta Premium','','Canadian rye whisky named on the Wikipedia Rye whiskey page.','Rye_whiskey','Canada'),
 E("Canadian Club Chairman's Select",'Canadian Club','Canadian rye whisky named on the Wikipedia Rye whiskey page.','Rye_whiskey','Canada'),
 E('Archie Rose Malted Rye','Archie Rose Distilling Co.','Australian malted rye whiskey named on the Wikipedia Rye whiskey page.','Rye_whiskey','Australia')],
 "Complete: {n} of {n} brands the Wikipedia Rye whiskey page names, plus earlier entries; the page names no European brand.")
add('Cachaça',[E('Novo Fogo','Novo Fogo','Cachaça producer named on the Wikipedia Cachaça page.','Cacha%C3%A7a','Brazil')],
 "No complete list exists; follows Wikipedia Cachaça, which names only Ypióca and Novo Fogo and links to a separate list of brands.")
add('Pastis',[E('Pacific','Pernod Ricard','Pastis brand named on the Wikipedia Pastis page.','Pastis','France','Pernod Ricard')],
 "Complete: {n} of {n} brands named on Wikipedia Pastis (Ricard, Pernod, Pastis 51, Pacific, Henri Bardouin).")
add('Ouzo',[],"Complete: 2 of 2 ouzo brands named on Wikipedia Ouzo (Tyrnavou, Plomari); Ouzo 12 is an earlier entry; Pallini Mistra is an Italian ouzo-like drink and excluded.")
add('Irish single pot still whiskey',[E('Dingle Single Pot Still','Dingle Distillery','Single pot still whiskey of Dingle, Co. Kerry, named on the Wikipedia Single pot still whiskey page.','Single_pot_still_whiskey','Ireland',y='2017'),
 E('Yellow Spot','Irish Distillers','Midleton single pot still whiskey named on the Wikipedia Single pot still whiskey page.','Single_pot_still_whiskey','Ireland','Irish Distillers'),
 E('Red Spot','Irish Distillers','Midleton single pot still whiskey named on the Wikipedia Single pot still whiskey page.','Single_pot_still_whiskey','Ireland','Irish Distillers'),
 E('Midleton Barry Crockett Legacy','Irish Distillers','Midleton single pot still whiskey named on the Wikipedia Single pot still whiskey page.','Single_pot_still_whiskey','Ireland','Irish Distillers'),
 E('Teeling Single Pot Still','Teeling Distillery','Single pot still whiskey of Dublin, named on the Wikipedia Single pot still whiskey page.','Single_pot_still_whiskey','Ireland',y='2018'),
 E('Drumshanbo Single Pot Still','The Shed Distillery','Single pot still whiskey of Co. Leitrim, named on the Wikipedia Single pot still whiskey page.','Single_pot_still_whiskey','Ireland'),
 E('Micil','','Single pot still whiskey of Co. Galway, named on the Wikipedia Single pot still whiskey page.','Single_pot_still_whiskey','Ireland'),
 E('Old Comber Single Pot Still','Echlinville Distillery','Single pot still whiskey of Co. Down, named on the Wikipedia Single pot still whiskey page.','Single_pot_still_whiskey','Ireland')],
 "Complete: {n} of {n} Irish single pot still brands on Wikipedia Single pot still whiskey (Redbreast, Green Spot, Yellow Spot, Red Spot, Midleton, Powers, Dingle, Teeling, Drumshanbo, Micil, Old Comber); the page's six non-Irish emulators are not single pot still by law and are left out.")
add('Arak & rakı',[E('Elite Arak','Joseph Gold & Sons','Israeli arak named on the Wikipedia Arak page.','Arak_(drink)','Israel'),
 E('Arak Ashkelon','Barkan Wine Cellars','Israeli arak named on the Wikipedia Arak page.','Arak_(drink)','Israel'),
 E('Arak Kawar','Kawar Distillery','Israeli arak named on the Wikipedia Arak page.','Arak_(drink)','Israel'),
 E('Arak Muaddi','Arak Muaddi','Palestinian arak named on the Wikipedia Arak page.','Arak_(drink)','Palestine'),
 E('Arak Zahlawi','','Lebanese arak of Zahlé, named on the Wikipedia Arak page.','Arak_(drink)','Lebanon'),
 E('Al-Rayan','','Syrian arak of a state-run firm based in Sweida, named on the Wikipedia Arak page.','Arak_(drink)','Syria'),
 E('Al-Mimas','','Syrian arak of a state-run firm near Homs, named on the Wikipedia Arak page.','Arak_(drink)','Syria')],
 "Complete: arak brands named on Wikipedia Arak (Israel, Palestine, Lebanon, Syria; {n} entries in all); the page's Spanish, Greek and Canadian araks and its Kawar and Gold sister brands are versions or left out; rakı has no list page fetched.")
add('Grappa & pomace brandy',[E('Nardini','Nardini','Grappa producer named on the Wikipedia Grappa page.','Grappa','Italy'),
 E('Jacopo Poli','Jacopo Poli','Grappa producer named on the Wikipedia Grappa page.','Grappa','Italy'),
 E('Marzadro','Marzadro Distillery','Grappa distillery named on the Wikipedia Grappa page for cherry-wood ageing.','Grappa','Italy')],
 "No complete list exists; Wikipedia Grappa names only Nardini, Jacopo Poli, Nonino and Marzadro.")
add('French cider',[E('Poiré Domfront','','Perry AOP of Domfront; AOC 2002, AOP 2004 per oriGIn.','Pastis','France',y='2002')],None)
k=kind('French cider')
for e in k['x']:
    if e['n']=='Poiré Domfront': e['s']='https://www.originfood.info/wp-content/uploads/2024/05/liste-aop-france-cidres-poires.pdf'
    yr={"Cidre Pays d'Auge":'1996','Cidre Cotentin':'2016','Cidre de Cornouaille':'1996','Cidre du Perche':'2022'}
    if e['n'] in yr and not e.get('y'): e['y']=yr[e['n']]
k['sel']=re.sub(r'Covers 5 of about \? .*$','',k['sel']).rstrip()+" Complete: 5 of 5 cider and perry AOPs on the oriGIn list of French AOP ciders and perries (Cornouaille, Pays d'Auge, Domfront, Cotentin, Perche), plus Eric Bordelet; Pommeau and cider spirits are in other kinds."
json.dump(d,open('stageC.json','w'),ensure_ascii=False)
print(tot)
