import re
p='/home/user/Possession-Taxonomy/rebuild/work/V4_J7_WCE/build.py'
s=open(p).read()
add = r'''
# ======== complete-lists additions ========
WG='https://winesofgreece.org/regions-wineries/appellations-and-classifications/?location=MACEDONIA_PDO_NAOUSSA'
known={n:(d,y) for n,g,d,s_,y in gr}
pdo={'Macedonia':['Goumenissa','Naoussa','Amyndeon','Slopes of Meliton'],'Epirus':['Zitsa'],'Thessaly':['Rapsani','Messenikola','Anchialos'],
'Peloponnese':['Mantinia','Nemea','Patras','Mavrodaphne of Patras','Muscat of Patras','Muscat of Rio Patras','Monemvasia-Malvasia'],
'Ionian Islands':['Robola of Kefalonia','Mavrodaphne of Kefalonia','Muscat of Kefalonia'],
'Aegean Islands':['Santorini','Paros','Malvasia Paros','Samos','Lemnos','Muscat of Lemnos','Rhodes','Muscat of Rhodes'],
'Crete':['Archanes','Dafnes','Peza','Handakas-Candia','Malvasia Handakas-Candia','Sitia','Malvasia Sitia']}
alias_g={'Amyndeon':'Amyntaio · Amynteo','Patras':'Patra','Rhodes':'Rodos','Lemnos':'Limnos','Messenikola':'Mesenikola','Handakas-Candia':'Chandakas-Candia'}
kn2={'Amyndeon':'Amyntaio','Mavrodaphne of Kefalonia':'Mavrodaphne of Cephalonia'}
gx=[]
for reg,ns in pdo.items():
    for n in ns:
        d,y=known.get(kn2.get(n,n),(f'Greek PDO in {reg}.',''))
        gx.append(E(n,WG,d,g=reg,y=y,a=alias_g.get(n,''),v=gv.get(n,[])))
k_gr=K('Greece: PDO wines','The 33 Greek wine PDOs on the Wines of Greece appellations list.',
 'One entry is one Greek PDO, a protected wine zone named for its place, sectioned by region.',
 'All 33 PDOs on the Wines of Greece "Appellations & Classifications" list (page read with Firecrawl); the eAmbrosia register itself is a JavaScript app and was not read. Details come from the Wikipedia, WineWithSeth and Wines of Greece pages fetched earlier; PDOs without a fetched description carry only their region.',
 'by Greek wine region',tt(['Xinomavro','Agiorgitiko','Moschofilero','Assyrtiko','Mavrodaphne','Muscat','Roditis','Kotsifali','Mandilaria','Liatiko','Vilana','Malvasia']),gx,WG)
pgi={'Thrace':['Thrace','Evros','Ismaros','Avdira'],
'Macedonia':['Macedonia','Kavala','Thasos','Pangeon','Drama','Agora','Serres','Slopes of Paiko','Slopes of Vertiskos','Nea Mesimvria','Thessaloniki','Epanomi','Halkidiki','Sithonia','Mount Athos','Pella','Florina','Kastoria','Imathia','Pieria','Kozani','Grevena','Siatista','Velvento'],
'Epirus':['Epirus','Ioannina','Metsovo'],
'Thessaly':['Thessalia','Krania','Elassona','Tyrnavos','Meteora','Kranona','Karditsa','Magnisia'],
'Sterea Ellada and Attica':['Sterea Ellada','Attiki','Anavyssos','Gerania','Ilion','Markopoulo','Pallini','Slopes of Parnitha','Spata','Slopes of Kithaironas','Slopes of Pendeliko','Retsina of Attiki','Retsina of Koropi','Retsina of Markopoulo','Retsina of Megara','Retsina of Mesogeia','Retsina of Paiania','Retsina of Pallini','Retsina of Pikermi','Retsina of Spata','Evia','Lilantio Pedio','Karystos','Ritsona','Retsina of Evia','Retsina of Halkida','Retsina of Gialtra','Retsina of Karystos','Thiva','Retsina of Viotia','Retsina of Thebes','Fthiotida','Atalanti Valley','Opountia Locris','Martino','Parnassos','Slopes of Knimida'],
'Peloponnese':['Peloponnese','Achaia','Slopes of Aigialia','Ilia','Pisatis','Letrinoi','Messinia','Trifilia','Pylia','Lakonia','Arkadia','Tegea','Argolida','Korinthos','Klimenti'],
'Ionian Islands':['Corfu','Halikouna','Lefkada','Slopes of Ainos','Metaxata','Mantzavinata','Zakynthos','Verdea of Zakynthos'],
'Aegean Sea Islands':['Aegean Sea','Lesvos','Chios','Slopes of Ampelos','Ikaria','Dodekanese','Kos','Cyclades','Thapsana'],
'Crete':['Crete','Chania','Kissamos','Iraklio','Lasithi','Rethimno']}
px=[]
for reg,ns in pgi.items():
    for n in ns:
        d='Greek PGI (local wine) in '+reg+'.'
        if n.startswith('Retsina'): d='Greek PGI for retsina, wine flavoured with pine resin, named for its Attica or Evia area.'
        if n=='Verdea of Zakynthos': d='Greek PGI with traditional designation (Verdea) for Zakynthos.'
        px.append(E('PGI '+n if False else n,WG,d,g=reg))
k_gp=K('Greece: PGI wines','The Greek wine PGIs (regional, district and area local wines) on the Wines of Greece list.',
 'One entry is one Greek PGI, a local-wine indication named for a region, district or area, sectioned by region.',
 f'All {len(px)} PGIs on the Wines of Greece "Appellations & Classifications" list, including the retsina and Verdea names; the Wines of Greece PGI article groups them as 8 regional, 37 district and 58 area wines plus the traditional-appellation wines. The old Retsina kind is merged here.',
 'by Greek wine region',tt(['Savatiano','Roditis','Assyrtiko','Agiorgitiko','Xinomavro','Mavrodaphne','Malagousia']),px,WG)
# Cyprus
PC='https://publications.gov.cy/assets/user/publications/Labels%20of%20Taste/31/'
k_cy=K('Cyprus: wine areas','The Cypriot PDOs and the four PGI district wines.','One entry is one Cypriot PDO or PGI wine area.','The five PDOs and four PGIs on the government "Labels of Taste" page; wine-route notes from Wikipedia Cypriot wine.','PDOs, then PGIs',tt(['Xynisteri','Mavro','Maratheftiko','Carignan','Shiraz','Yiannoudi','Ofthalmo']),
 [E('Laona Akamas',PC,'Cypriot PDO.',g='PDO'),E('Vouni Panagias-Ambelitis',PC,'Cypriot PDO.',g='PDO'),E('Pitsilia',PC,'Cypriot PDO.',g='PDO'),E('Krasochoria Lemesou',PC,'Cypriot PDO with the sub-regions Afamis and Laona.',g='PDO',v=[V('Afamis'),V('Laona')]),E('Commandaria',PC,'Cypriot PDO, also written Koumandaria, made by fourteen villages; sweet wine mainly from Mavro.',g='PDO')]+[E(n,PC,'Cypriot PGI local-wine district.',g='PGI') for n in ['Larnaka','Lemesos','Lefkosia','Pafos']],PC)
# Hungary extra
TH='https://tastehungary.com/journal/guide-to-hungarian-wine-regions/'
k_hs=K('Hungary: PDO sub-regions and large PDO areas','The Hungarian PDOs inside or above the 22 wine regions.','One entry is one Hungarian PDO that is a sub-region of a wine region or a large area grouping regions.','The sub-regions and large areas named on the Taste Hungary guide (2023: 31 PDOs and 6 PGIs); Kőszeg, Füred and Mura PDOs from later news were not read.','by parent region',[['Colour and style',['White','Red','Sparkling']]],
 [E('Tihany',TH,'Hungary\'s smallest wine appellation, 95 ha.',g='Balaton'),E('Káli',TH,'Sub-region of the three northern Balaton PDOs, 453 ha.',g='Balaton'),E('Somló',TH,'Sub-region of Nagy Somló, one of its hills, 326 ha.',g='Balaton'),
 E('Debrői Hárslevelű',TH,'Sub-region of Eger for white Hárslevelű only, 940 ha.',g='Eger'),E('Izsáki Arany Sárfehér',TH,'Sub-region of Kunság for white wine from Arany Sárfehér, 3,800 ha.',g='Duna'),E('Monor',TH,'Sub-region of Kunság, 340 ha.',g='Duna'),E('Soltvadkerti Ezerjó',TH,'Sub-region of Kunság for white and sparkling wine from Ezerjó.',g='Duna'),
 E('Duna',TH,'Large PDO area grouping Csongrád, Hajós-Baja and Kunság.',g='Large areas'),E('Pannon',TH,'Large PDO area grouping Pécs, Szekszárd, Tolna and Villány.',g='Large areas')],TH)
k_hp=K('Hungary: PGI areas','The six Hungarian wine PGIs, each covering several PDOs.','One entry is one Hungarian wine PGI, a large area over several PDOs.','The six PGIs on the Taste Hungary guide.','one flat list',[['Colour and style',['White','Red','Rosé','Sparkling']]],
 [E('Balaton',TH,'PGI around Lake Balaton, including nine PDOs.'),E('Balatonmelléki',TH,'PGI inside the Balaton PGI, little used since the Balaton PGI was approved.'),E('Felső-Magyarország',TH,'"Upper Hungary", around the Mátra, Bükk and Eger regions.'),E('Zemplén',TH,'PGI around Tokaj.'),E('Duna-Tisza közé',TH,'PGI between the Danube and the Tisza.'),E('Dunántúl',TH,'PGI west of the Danube.')],TH)
# Slovakia districts
SZ='https://sk.wikipedia.org/wiki/Zoznam_vinohradníckych_oblastí_Slovenska'
sk_d={'Malokarpatská':['Skalický','Záhorský','Stupavský','Bratislavský','Pezinský','Modranský','Doľanský','Orešanský','Senecký','Trnavský','Hlohovecký','Vrbovský'],'Južnoslovenská':['Šamorínsky','Dunajskostredský','Galantský','Palárikovský','Komárňanský','Hurbanovský','Strekovský','Štúrovský'],'Stredoslovenská':['Ipeľský','Hontiansky','Vinický','Modrokamenský','Fiľakovský','Gemerský','Tornaľský'],'Nitrianska':['Šintavský','Nitriansky','Radošinský','Zlatomoravský','Vrábeľský','Žitavský','Želiezovský','Tekovský','Pukanecký'],'Východoslovenská':['Moldavský','Sobranský','Michalovský','Kráľovskochlmecký']}
k_skd=K('Slovakia: wine districts','The 40 Slovak wine districts (vinohradnícke rajóny) in five regions.','One entry is one Slovak wine district (vinohradnícky rajón); the Tokaj region has no districts and is organised by village.','All 40 districts on the Slovak Wikipedia list of wine regions (municipalities of each district are not included).','by wine region',tt(['Grüner Veltliner','Welschriesling','Blaufränkisch','Müller-Thurgau','St. Laurent','Pinot blanc','Riesling']),
 [E(n+' vinohradnícky rajón',SZ,f'Wine district of the {r} wine region.',g=r) for r,ns in sk_d.items() for n in ns],SZ)
# Romania IGP
RC='https://www.winewithseth.com/winewiki/romania-wine-classification/'
k_roi=K('Romania: IGP wine regions','The Romanian IGP wine regions named on the classification page.','One entry is one Romanian IGP wine region.','The four IGP examples on WineWithSeth Romania wine classification; the page says there are 33 DOC and 12 IGP zones and does not list them all, so this is NOT the complete list.','one flat list',tt(['Fetească albă','Fetească regală','Fetească neagră']),
 [E(n,RC,'Romanian IGP wine region.') for n in ['Banat','Dobrogea','Muntenia','Transylvania']],RC)
# Switzerland cantonal
DW='https://de.wikipedia.org/wiki/Weinbau_in_der_Schweiz'
def cv(*ns): return [V(n) for n in ns]
ch=[('Valais (Wallis)','Fully, Saxon, Saillon, Chamoson, Ardon, Vétroz, Conthey, Savièse, Sion, Grimisuat, Ayent, Lens, Noble-Contrée, Sierre, Salquenen, Varen','AOC communes; Grand Cru sites Vétroz, St-Léonard, Fully.'),
('Vaud: La Côte (canton Vaud)','Morges, Aubonne, Féchy, Perroy, Mont-sur-Rolle, Tartegnin, Coteau de Vincy, Bursinel, Vinzel, Luins, Begnins, Nyon','AOC area of Vaud.'),
('Vaud: Lavaux','Lutry, Villette, Epesses, Dézaley (Grand Cru), Calamin (Grand Cru), Saint-Saphorin, Chardonne, Vevey, Montreux','AOC area of Vaud with two Grand Cru names.'),
('Vaud: Chablais','Villeneuve, Yvorne, Aigle, Ollon, Bex','AOC area of Vaud.'),
('Vaud: Nord Vaudois','Bonvillars, Côtes de l\'Orbe, Mont Vully','AOC area of Vaud.'),
('Geneva (Genève)','Choully, Satigny, Peissy, Russin, Dardagny, Lully, Bardonnex, Cologny, Jussy, Choulex, Hermance, Céligny, Collex-Bossy','Le Mandement region and AOC communes.'),
('Three Lakes: Bielersee','Twann, Ligerz, Tüscherz, Vingelz, Erlach, Tschugg','Sub-area of the Three Lakes region.'),
('Three Lakes: Neuchâtel','Vaumarcus, Fresens, Saint-Aubin-Sauges, Gorgier, Bevaix, Boudry, Cortaillod, Auvernier, Neuchâtel, Hauterive, Saint-Blaise, Cornaux, Cressier, Le Landeron, Neuenstadt, Schafis','Neuchâtelerweine, sub-area of the Three Lakes region.'),
('Three Lakes: Murtensee (Mont Vully)','Mont Vully','Sub-area of the Three Lakes region.'),
('Ticino','Giornico, Malvaglia, Biasca, Verscio, Gordola, Tenero, Gudo, Giubiasco, Rivera, Morcote, Rovio, Stabio, Morbio, Chiasso, Castel San Pietro','Appellation Ticino DOC Merlot; quality seal VITI.'),
('Zürich','Freienstein-Teufen, Stammheim, Dachsen, Andelfingen, Flaach, Neftenbach, Seuzach, Eglisau, Weiningen, Meilen, Stäfa, Au, Wädenswil, Richterswil','Regions Zürichsee shores, Limmattal, Zürcher Unterland, Zürcher Weinland.'),
('Schaffhausen','Klettgau, Munotrebberg, Thayngen, Stein am Rhein, Buchberg, Rüdlingen','Klettgau and the upper and lower parts of the canton.'),
('Aargau','Fricktal, Limmattal (Wettingen), Reusstal, Schenkenbergertal, Seetal and Wildegg, Geissberg, Unteres Aaretal','Cantonal wine areas.'),
('Thurgau','Seebachtal, Unteres Thurtal, Untersee, Rheingebiet, Lauchetal, Oberes Thurtal','Cantonal wine areas.'),
('St. Gallen','Sarganserland, Rheintal, Berneck, Thal, Balgach, Pfäfers, Quinten, Walenstadt','Cantonal wine areas.'),
('Luzern','Wiggertal, Sempachersee/Surental, Seetal, Vierwaldstättersee','AOC Luzern, introduced 2005.'),
('Thunersee (Bern)','Thun, Spiez, Oberhofen, Hilterfingen','Bernese lake wine area.'),
('Graubünden (Bündner Herrschaft)','Fläsch, Maienfeld, Jenins, Malans','Bündner Herrschaft villages.')]
k_chc=K('Switzerland: cantonal wine areas','The cantonal wine areas and AOC communes of Switzerland.',
 'One entry is one Swiss cantonal wine area or sub-area; the communes it names are its versions.',
 'The areas and communes named on German Wikipedia Weinbau in der Schweiz; the page does not give a full list of the 62 AOCs, and Basel and Solothurn have no named areas.','by canton',tt(['Chasselas','Pinot noir','Gamay','Merlot','Müller-Thurgau','Petite Arvine','Heida','Humagne rouge','Cornalin']),
 [E(n,DW,d,g=n.split(':')[0].split(' (')[0]) | {'v':cv(*[x.strip() for x in c.split(',')])} for n,c,d in ch],DW)
# VDP Grosse Lage versions
VD='https://www.winewithseth.com/winewiki/vdp-grosse-lage/'
for e in k_anb['x']:
    if e['n']=='Mosel': e['v']=[V('Scharzhofberg (Wiltingen)','VDP Grosse Lage',''),V('Wehlener Sonnenuhr','VDP Grosse Lage','')]
    if e['n']=='Rheingau': e['v']=[V('Kiedrich Gräfenberg','VDP Grosse Lage','')]
    if e['n']=='Nahe': e['v']=[V('Niederhäuser Hermannshöhle','VDP Grosse Lage',''),V('Oberhäuser Brücke','VDP Grosse Lage','')]
k_anb['sel']+=' VDP Grosse Lage versions are the five sites named on WineWithSeth VDP Grosse Lage; the VDP lists about 430, which no fetched page gives.'
'''
s=s.replace("def D(n,t,ax,shelves):",add+"\ndef D(n,t,ax,shelves):",1)
s=s.replace("[('Hungary','The 22 Hungarian wine regions, with Tokaj\\'s styles.','one kind',[k_hu]),('Czechia, Slovakia & Poland','Wine regions of the Czech Republic, Slovakia and Poland.','one kind per country',[k_cz,k_sk,k_pl])]",
 "[('Hungary','The Hungarian wine regions, their sub-regions and the PGIs.','kinds by tier',[k_hu,k_hs,k_hp]),('Czechia, Slovakia & Poland','Wine regions of the Czech Republic, Slovakia and Poland.','one kind per country',[k_cz,k_sk,k_skd,k_pl])]")
s=s.replace("[k_ro,k_bg]","[k_ro,k_roi,k_bg]")
s=s.replace("[('Greece','Greek PDO zones by region.','one kind',[k_gr])","[('Greece','Greek PDOs and PGIs by region.','kinds by tier',[k_gr,k_gp])")
s=s.replace("[k_ch,k_vd]","[k_ch,k_chc,k_vd]")
s=s.replace("'Kisi':'Georgia","'Retsina':'Greece: PGI wines','Kisi':'Georgia")
open(p,'w').write(s)
