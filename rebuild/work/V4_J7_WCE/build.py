import json,os
W='https://en.wikipedia.org/wiki/'
def E(n,s,d,g='',y='',role=None,v=None,a=''):
    e={'n':n,'a':a,'d':d,'mk':'','y':y,'s':s,'v':v or []}
    if g:e['g']=g
    if role:e['role']=role
    return e
def V(n,d='',y=''): return {'n':n,'mk':'','y':y,'d':d}
def K(n,d,nl,sel,xg,tt,x,s):
    return {'n':n,'d':d,'nl':nl,'sel':sel,'xg':xg,'tt':tt,'x':x,'s':s}
COL=['Colour and style',['Red','White','Rosé','Sparkling','Sweet','Fortified']]
def tt(grapes): return [COL,['Permitted or leading grapes',grapes]]

# ---------- Germany ----------
GW=W+'German_wine'; GL=W+'List_of_German_wine_regions'
anb=[('Ahr','Pinot noir 64.7 %, Riesling 8.2 %','21 % white, 79 % red; 1 Bereich'),
('Baden','Pinot noir 32.1 %, Pinot gris 15.3 %, Müller-Thurgau 13.8 %','62 % white, 38 % red; 9 Bereiche'),
('Franken','Silvaner 25.3 %, Müller-Thurgau 22.3 %, Bacchus 11.9 %','83 % white, 17 % red; 3 Bereiche'),
('Hessische Bergstraße','Riesling 35.6 %, Pinot gris 12.8 %, Pinot noir 10.8 %','79 % white, 21 % red; 2 Bereiche'),
('Mittelrhein','Riesling 63.3 %, Pinot noir 10.7 %','84 % white, 16 % red; 2 Bereiche'),
('Mosel','Riesling 62.4 %, Müller-Thurgau 9.0 %, Elbling 5.0 %','91 % white, 9 % red; 6 Bereiche'),
('Nahe','Riesling 29.3 %, Müller-Thurgau 11.0 %','77 % white, 23 % red; 1 Bereich'),
('Pfalz','Riesling 25.2 %, Dornfelder 10.3 %','68 % white, 32 % red; 2 Bereiche'),
('Rheingau','Riesling 76.1 %, Pinot noir 12.6 %','85 % white, 15 % red; 1 Bereich'),
('Rheinhessen','Riesling 19.6 %, Müller-Thurgau 13.9 %, Dornfelder 11.0 %','74 % white, 26 % red; 3 Bereiche'),
('Saale-Unstrut','Müller-Thurgau 14.3 %, Pinot blanc 13.7 %, Riesling 9.4 %','77 % white, 23 % red; 2 Bereiche'),
('Sachsen','Riesling 14.2 %, Müller-Thurgau 11.4 %, Pinot blanc 11.5 %','81 % white, 19 % red; 2 Bereiche'),
('Württemberg','Trollinger 8.7 %, Lemberger 5.2 %','36 % white, 64 % red; 6 Bereiche')]
alias={'Franken':'Franconia','Pfalz':'Palatinate','Sachsen':'Saxony'}
k_anb=K('Germany: Anbaugebiete','The thirteen German quality-wine regions (Anbaugebiete), the top geographic tier of German wine.',
 'One entry is one of the thirteen German Anbaugebiete, the quality-wine regions defined in German wine law; its Bereiche are in the next kind.',
 'All thirteen Anbaugebiete in Wikipedia German wine (2023 area table), in the order of that table; Bereiche, Grosslagen and Landwein regions are separate kinds.',
 'one flat list of thirteen regions',tt(['Riesling','Müller-Thurgau','Silvaner','Pinot noir (Spätburgunder)','Pinot gris','Pinot blanc','Dornfelder','Trollinger','Lemberger','Bacchus','Elbling']),
 [E(n,GW,f'{c}; {gr}.',a=alias.get(n,'')) for n,gr,c in anb],GW)
ber={'Ahr':['Walporzheim/Ahrtal'],'Baden':['Badische Bergstraße','Bodensee','Breisgau','Kaiserstuhl','Kraichgau','Markgräflerland','Ortenau','Tauberfranken','Tuniberg'],
'Franken':['Maindreieck','Mainviereck','Steigerwald'],'Hessische Bergstraße':['Starkenburg','Umstadt'],'Mittelrhein':['Loreley','Siebengebirge'],
'Mosel':['Bernkastel','Burg Cochem','Moseltor','Obermosel','Ruwertal','Saar'],'Nahe':['Nahetal'],'Pfalz':['Mittelhaardt-Deutsche Weinstraße','Südliche Weinstraße'],
'Rheingau':['Johannisberg'],'Rheinhessen':['Bingen','Nierstein','Wonnegau'],'Saale-Unstrut':['Schlossneuenburg','Thüringen'],'Sachsen':['Dresden','Elstertal','Meissen'],
'Württemberg':['Bayerischer Bodensee','Kocher-Jagst-Tauber','Oberer Neckar','Remstal-Stuttgart','Württembergisch Bodensee','Württembergisch Unterland']}
gl={'Walporzheim/Ahrtal':['Klosterberg'],'Badische Bergstraße':['Hohenberg','Mannaberg','Rittersberg','Stiftsberg'],'Bodensee':['Sonnenufer'],'Breisgau':['Burg Lichteneck','Burg Zähringen','Schutterlindenberg'],'Kaiserstuhl':['Vulkanfelsen'],'Markgräflerland':['Attilafelsen','Burg Neuenfels','Lorettoberg','Vogtei Rötteln'],'Ortenau':['Fürsteneck','Schloss Rodeck'],'Tauberfranken':['Tauberklinge'],
'Maindreieck':['Burg','Engelsberg','Ewig Leben','Hofrat','Honigberg','Kirchberg','Marienberg','Markgraf Babenberg','Oelspiel','Ravensburg','Rosstal','Teufelstor'],'Mainviereck':['Heiligenthal','Reuschberg'],'Steigerwald':['Burgweg-Franken','Herrenberg','Kapellenberg','Schild','Schlossberg','Schlossstück'],
'Starkenburg':['Rott','Schlossberg','Wolfsmagen'],'Loreley':['Burg Hammerstein','Burg Rheinfels','Gedeonseck','Schloss Herrenberg','Lahntal','Loreleyfelsen','Marksburg','Schloss Reichenstein','Schloss Schönburg','Schloss Stahleck'],'Siebengebirge':['Petersberg'],
'Bernkastel':['Badstube','Kurfürstlay','Michelsberg','Münzlay','Nacktarsch','Probstberg','St. Michael','Schwarzlay','Vom Heißen Stein'],'Burg Cochem':['Goldbäumchen','Gradschaft','Rosenhang','Schwarze Katz','Weinhex'],'Moseltor':['Schloss Bübinger'],'Obermosel':['Gipfel','Königsberg'],'Ruwertal':['Römerlay'],'Saar':['Scharzberg'],
'Nahetal':['Burgweg-Nahe','Kronenberg','Paradiesgarten','Pfarrgarten','Rosengarten','Schlosskapelle','Sonnenborn'],
'Mittelhaardt-Deutsche Weinstraße':['Feuerberg','Gradenstück','Hochmess','Hofstück','Höllenpfad','Honigsäckel','Kobnert','Mariengarten','Meerspinne','Pfaffengrund','Rebstöckel','Rosenbühl','Schenkenböhl','Schnepfenflug an der Weinstraße','Schnepfenflug vom Zellertal','Schwarzerde'],
'Südliche Weinstraße':['Bischofskreuz','Guttenberg','Herrlich','Kloster Liebrauenberg','Königsgarten','Mandelhöhe','Ordensgut','Schloss Ludwigshöhe','Trappenberg'],
'Johannisberg':['Burgweg-Rheingau','Daubhaus','Deutelsberg','Erntebringer','Gottesthal','Heiligenstock','Honigberg','Mehrhölzchen','Steil','Steinmächer'],
'Bingen':['Abtey','Adelberg','Kaiserpfalz','Kurfüstenstück','Rheingrafenstein','Sankt Rochuskapelle'],'Nierstein':['Auflangen','Domherr','Güldenmorgen','Gutes Domtal','Krötenbrunnen','Petersberg','Rehbach','Rheinblick','Sankt Alban','Spiegelberg','Vogelsgärten'],'Wonnegau':['Bergkloster','Burg Rodenstein','Domblick','Gotteshilfe','Liebfrauenmorgen','Pilgerpfad','Sybillinenstein'],
'Schlossneuenburg':['Blütengrund','Göttersitz','Kelterberg','Schweigenberg'],'Thüringen':['Mark Brandenburg'],'Dresden':['Elbhänge','Lössnitz'],'Meissen':['Schloss-Weinberg','Spaargebirge'],
'Bayerischer Bodensee':['Lindauer Seegarten'],'Kocher-Jagst-Tauber':['Kocherberg','Tauberberg'],'Remstal-Stuttgart':['Hohenneuffen','Kopf','Sonnenbühl','Wartbühl','Weinsteige'],
'Württembergisch Unterland':['Heuchelberg','Kirchenweinberg','Lindelberg','Salzberg','Schalkstein','Schozachtal','Staufenberg','Stromberg','Wunnenstein']}
bx=[]
for a,bs in ber.items():
    for b in bs:
        bx.append(E(b,GL,f'Bereich (district) of the {a} Anbaugebiet.',g=a,v=[V(x,f'Grosslage (collective vineyard site) in the Bereich {b}') for x in gl.get(b,[])]))
k_ber=K('Germany: Bereiche','The Bereiche (districts) inside each German Anbaugebiet, each with its Grosslagen.',
 'One entry is one Bereich, a district inside an Anbaugebiet; the Grosslagen (collective vineyard sites) of the district are its versions.',
 'Every Bereich and Grosslage named in Wikipedia List of German wine regions as fetched (40 Bereiche); Einzellagen (single vineyards) and VDP Grosse Lage sites are out because no fetched page lists them. Wikipedia German wine says 39 Bereiche; the list page gives 40.',
 'by Anbaugebiet',[['Colour and style',['White','Red','Rosé','Sparkling']],['Leading grape',['Riesling','Pinot noir (Spätburgunder)','Silvaner','Müller-Thurgau','Pinot gris','Lemberger','Trollinger']]],bx,GL)
lw=[('Ahrtaler Landwein','Ahr'),('Rheinburgen-Landwein','Mittelrhein'),('Rheingauer Landwein','Rheingau'),('Nahegauer Landwein','Nahe'),('Rheinischer Landwein','Rheinhessen'),('Pfälzer Landwein','Pfalz'),('Starkenburger Landwein','Hessische Bergstraße'),('Landwein der Mosel','Mosel'),('Landwein Main','Franken'),('Schwäbischer Landwein','Württemberg'),('Badischer Landwein','Baden'),('Sächsischer Landwein','Sachsen'),('Mitteldeutscher Landwein','Saale-Unstrut'),
('Bayerischer Bodensee-Landwein',''),('Regensburger Landwein',''),('Taubertäler Landwein',''),('Brandenburger Landwein',''),('Mecklenburger Landwein',''),('Stargarder Land Landwein','')]
k_lw=K('Germany: Landwein regions','The regional Landwein (country wine) areas of Germany, a tier below quality wine.',
 'One entry is one German Landwein region, a protected geographical indication that lies over one or more quality-wine regions.',
 'The Landwein regions named in Wikipedia German wine; the page says 21, and 19 are named in the part read (the Saar and Ruwer Landweine are not named separately). Entries ordered with the quality region they overlie first.',
 'Landwein over a quality region, then those outside the quality regions',[['Colour and style',['Red','White','Rosé']]],
 [E(n,GW,(f'Landwein region over the {q} Anbaugebiet.' if q else 'Landwein region not mapped to a quality region by the page.'),g=('Over an Anbaugebiet' if q else 'Not mapped to an Anbaugebiet')) for n,q in lw],GW)
# ---------- Austria ----------
AW=W+'Austrian_wine'
dac=[('Weinviertel','2002','Grüner Veltliner; Reserve from 2009.','origin'),('Mittelburgenland','2005','Blaufränkisch red.',None),('Traisental','2006','',None),('Kremstal','2007','',None),('Kamptal','2008','',None),('Leithaberg','2009','White from 2009, red from 2008.',None),('Eisenberg','2009','Blaufränkisch is the local red.',None),('Neusiedlersee','2011','Klassik from 2011, Reserve 2010, sweet styles added 2020.',None),('Wiener Gemischter Satz','2013','Field blends (Gemischter Satz) from Vienna.',None),('Rosalia','2017','',None),('Vulkanland Steiermark','2018','',None),('Südsteiermark','2018','Sauvignon blanc dominates.',None),('Weststeiermark','2018','Schilcher rosé is the local speciality.',None),('Carnuntum','2019','Zweigelt and Blaufränkisch red.',None),('Wachau','2020','Dry whites graded Steinfeder, Federspiel, Smaragd.',None),('Ruster Ausbruch','2020','Sweet Trockenbeerenauslese-level dessert wine from Rust.',None),('Wagram','2021','',None),('Thermenregion','2023','',None)]
wach=[V('Steinfeder','lightest Wachau grade, up to 11.5 % alcohol, mostly for local drinking'),V('Federspiel','Wachau grade of 11.5 to 12.5 % alcohol, minimum must weight 17° KMW, about Kabinett level'),V('Smaragd','top Wachau grade, at least 12.5 % alcohol and at most 9 g/l residual sugar')]
ax=[]
for n,y,d,r in dac:
    ax.append(E(n,AW,(f'Austrian DAC, first vintage {y}. '+d).strip(),y=y,role=r,v=(wach if n=='Wachau' else [])))
k_dac=K('Austria: DAC appellations','The eighteen Districtus Austriae Controllatus (DAC) wine appellations of Austria.',
 'One entry is one Austrian DAC, a regional appellation named for its place, in the year order of its first vintage.',
 'All eighteen DACs in Wikipedia Austrian wine, ordered by first vintage; the Wachau grades (Steinfeder, Federspiel, Smaragd) are versions of Wachau. The ÖTW Erste Lage vineyard classification is not on a fetched page and is not included.',
 'by year of first DAC vintage',tt(['Grüner Veltliner','Welschriesling','Riesling','Blaufränkisch','Zweigelt','St. Laurent','Sauvignon blanc','Gemischter Satz field blend','Schilcher (Blauer Wildbacher)']),ax,AW)
aw=[('Niederösterreich','Weinland','26,723 ha; Wachau, Kremstal, Kamptal, Traisental, Wagram, Weinviertel, Carnuntum, Thermenregion.'),('Burgenland','Weinland','11,538 ha; Neusiedlersee, Leithaberg, Mittelburgenland, Eisenberg.'),('Wien','Weinland','588 ha; the city of Vienna.'),('Steiermark','','5,109 ha; Vulkanland Steiermark, Südsteiermark, Weststeiermark.'),('Bergland','','243 ha; rest of Austria, no sub-regions listed.')]
k_aw=K('Austria: Weinbaugebiete','The wine-growing areas of Austria above the DACs: Niederösterreich, Burgenland, Wien, Steiermark and Bergland.',
 'One entry is one Austrian Weinbaugebiet (wine-growing area), the tier above the DACs.',
 'The five areas named in Wikipedia Austrian wine (2024 hectares).','Weinland, then Steiermark and Bergland',[['Colour and style',['White','Red','Rosé','Sparkling','Sweet']]],
 [E(n,AW,d,g=g or 'Other areas') for n,g,d in aw],AW)
# ---------- Switzerland ----------
SW=W+'Swiss_wine'; SS='https://www.swisswine.com/en/swiss-wine-regions'; SV='https://www.mescavesouvertes.ch/en/les-regions'
k_ch=K('Switzerland: wine regions','The six Swiss wine regions grouped from the cantonal AOCs.',
 'One entry is one of the six Swiss wine regions defined by Swiss Wine Promotion, which group the cantonal AOCs.',
 'The six regions on Swiss Wine Promotion and Wikipedia Swiss wine. The cantonal AOCs (62 according to Swiss Wine Promotion) are not listed on any fetched page except the Vaud ones in the next kind, so they are not included.',
 'one flat list of six regions',tt(['Pinot noir','Chasselas','Gamay','Merlot','Müller-Thurgau','Gamaret','Chardonnay','Petite Arvine','Humagne rouge','Cornalin','Heida']),
 [E('Valais',SS,'Alpine region with almost one third of Swiss vineyards; terraced vineyards.',v=[V('Vin des glaciers','solera-aged wine from the Rèze grape in larch or oak barrels')]),
  E('Vaud',SS,'Stretches from Lake Geneva to Lake Neuchâtel; six AOCs and two Grand Cru AOCs.'),
  E('German-speaking Switzerland',SS,'Sixteen cantons; Pinot noir and Müller-Thurgau dominate.'),
  E('Geneva',SW,'First canton to adopt an AOC label; Satigny is the largest winemaking municipality.'),
  E('Ticino',SS,'South of the Alps, facing Italy; Merlot is more than 80 % of the vineyard.'),
  E('Three Lakes (Trois-Lacs)',SS,'Neuchâtel, Lake Biel and Vully.',a='Trois-Lacs · Drei Seen',v=[V('Neuchâtel'),V('Lake Biel'),V('Vully')])],SS)
k_vd=K('Switzerland: Vaud AOCs','The six Vaud AOC areas and the Dézaley Grand Cru.',
 'One entry is one AOC area of the canton of Vaud.',
 'The six AOCs and the Dézaley Grand Cru named on the Vaud wine-region page; the page says there are two Vaud Grand Cru AOCs but names only Dézaley.',
 'one flat list',[['Colour and style',['White','Red','Rosé']],['Leading grape',['Chasselas','Pinot noir','Gamay']]],
 [E('La Côte',SV,'Vaud AOC area.'),E('Lavaux',SV,'Vaud AOC area of terraced vineyards on Lake Geneva.',v=[V('Dézaley Grand Cru','AOC Grand Cru located within Lavaux')]),E('Chablais',SV,'Vaud AOC area.'),E("Côtes de l'Orbe",SV,'Vaud AOC area.'),E('Bonvillars',SV,'Vaud AOC area.'),E('Vully',SV,'Vaud AOC area.')],SV)
# ---------- Hungary ----------
HW=W+'Hungarian_wine'; TJ=W+'Tokaji'; TR=W+'Tokaj_wine_region'
hu=[('Badacsony','Balaton','Volcanic soils; full-bodied whites with considerable acidity; Kéknyelű.'),('Balatonboglár','Balaton','Full-bodied whites and reds, moderate acidity.'),('Balaton-felvidék','Balaton','Volcanic soils; full-bodied whites.'),('Balatonfüred-Csopak','Balaton','Terra rossa soils; full-bodied whites.'),('Nagy-Somló','Balaton','Volcanic soil; full-bodied whites with high acidity; Olaszrizling, Hárslevelű, Furmint.'),('Zala','Balaton','Mainly white wines.'),
('Csongrád','Duna','Fresh, light wines.'),('Hajós-Baja','Duna','Fresh, light wines.'),('Kunság','Duna','Fresh, light wines.'),
('Bükk','Eger','Mainly white wines.'),('Eger','Eger','Fresh and full-bodied whites, good Pinot noirs; Leányka, Királyleányka, Olaszrizling, Kékfrankos.'),('Mátra','Eger','Elegant, full-bodied whites from volcanic soil.'),
('Neszmély','Észak-Dunántúl','Fresh, aromatic whites.'),('Etyek-Buda','Észak-Dunántúl','Fresh whites with considerable acidity.'),('Mór','Észak-Dunántúl','Volcanic soil; full-bodied whites; Ezerjó.'),('Pannonhalma','Észak-Dunántúl','Full-bodied whites.'),('Sopron','Észak-Dunántúl','Elegant reds; Kékfrankos.'),
('Pécs','Pannon','Mainly whites; Cirfandli.'),('Szekszárd','Pannon','Full-bodied, spicy reds; Kadarka, Kékfrankos, Cabernet franc, Merlot.'),('Tolna','Pannon','No description on the page.'),('Villány','Pannon','Robust, full-bodied, spicy reds; Blauer Portugieser, Cabernets, Merlot.'),
('Tokaj','Tokaj','Sweet botrytised aszú wines and dry Furmint; Furmint, Hárslevelű, Sárgamuskotály, Kövérszőlő, Zéta.')]
tok=[V('Tokaji Aszú','3 to 6 puttonyos, set by sugar and sugar-free extract; usually above 14 % alcohol'),V('Aszú-Eszencia','sweeter than 6 puttonyos'),V('Tokaji Eszencia','free-run juice of aszú berries, 500 to 700 g/l sugar, about 5 to 6 % alcohol'),V('Tokaji Szamorodni','from bunches with a share of botrytised berries; dry (száraz) or sweet (édes), about 14 % alcohol'),V('Tokaji Fordítás','must poured on used aszú dough'),V('Tokaji Máslás','must poured on aszú lees'),V('Dry Tokaji Furmint','single-vineyard dry Furmint, led by Szepsy Úrágya 2000; Mád makes a commune-level wine'),V('First-class vineyards (1730 classification)','vineyards sorted into first, second and third class by soil, sun and noble rot; completed by the 1765 and 1772 censuses')]
hx=[]
for n,g,d in hu:
    v=[]
    if n=='Tokaj':v=tok
    if n=='Eger':v=[V('Egri Bikavér','elegant red blend from Eger')]
    if n=='Szekszárd':v=[V('Szekszárdi Bikavér','red blend from Szekszárd')]
    hx.append(E(n,TJ if n=='Tokaj' else HW,d,g=g,v=v,role=('origin' if False else None)))
k_hu=K('Hungary: wine regions','The 22 Hungarian wine regions, with Tokaj\'s wine styles and classes as versions.',
 'One entry is one of the 22 Hungarian wine regions, grouped by the wine-region group it belongs to.',
 'All 22 regions in Wikipedia Hungarian wine, by group (Balaton, Duna, Eger, Észak-Dunántúl, Pannon, Tokaj); Tokaj styles from Wikipedia Tokaji. The page names no PDO sub-districts and no named first-growth vineyards beyond Úrágya, so none are listed.',
 'by wine-region group',tt(['Furmint','Hárslevelű','Olaszrizling','Kékfrankos','Kadarka','Cabernet franc','Merlot','Ezerjó','Blauer Portugieser','Kéknyelű','Sárgamuskotály']),hx,HW)
# ---------- Czechia, Slovakia, Poland ----------
CZ=W+'Czech_wine'; SK=W+'Slovak_wine'; PL=W+'Polish_wine'
k_cz=K('Czechia: wine sub-regions','The two Czech wine regions and their six sub-regions, with the VOC appellations.',
 'One entry is one Czech wine sub-region (podoblast); VOC appellations are versions.',
 'The six sub-regions in Wikipedia Czech wine; VOC Znojmo, Mikulov and Mělník are the VOC examples that page names.','Moravia, then Bohemia',tt(['Pálava','Riesling','Pinot gris','Pinot noir','Blaufränkisch','Zweigelt','St. Laurent','Hibernal','Moravian Muscat']),
 [E('Mikulovská',CZ,'Moravian sub-region around Mikulov.',g='Moravia (about 96 % of Czech wine)',v=[V('VOC Mikulov')]),E('Znojemská',CZ,'Moravian sub-region around Znojmo.',g='Moravia (about 96 % of Czech wine)',v=[V('VOC Znojmo')]),E('Velkopavlovická',CZ,'Moravian sub-region around Velké Pavlovice.',g='Moravia (about 96 % of Czech wine)'),E('Slovácká',CZ,'Moravian sub-region of Slovácko.',g='Moravia (about 96 % of Czech wine)'),E('Mělnická',CZ,'Bohemian sub-region around Mělník.',g='Bohemia',v=[V('VOC Mělník')]),E('Litoměřická',CZ,'Bohemian sub-region around Litoměřice.',g='Bohemia')],CZ)
k_sk=K('Slovakia: wine regions','The six Slovak wine regions, with the Slovak Tokaj styles.',
 'One entry is one of the six Slovak wine regions.','The six regions in Wikipedia Slovak wine; the 40 districts are not named on the page. Slovak Tokaj styles from Wikipedia Tokaj wine region.','one flat list',tt(['Grüner Veltliner','Welschriesling','Blaufränkisch','Müller-Thurgau','St. Laurent','Pinot blanc','Riesling','Furmint','Lipovina (Hárslevelű)']),
 [E('Malokarpatská',SK,'Little Carpathians region.'),E('Južnoslovenská',SK,'South Slovak region.'),E('Nitrianska',SK,'Nitra region.'),E('Stredoslovenská',SK,'Central Slovak region.'),E('Východoslovenská',SK,'East Slovak region.'),
 E('Tokaj (Slovakia)',TR,'Seven communities: Bara, Čerhov, Černochov, Malá Tŕňa, Slovenské Nové Mesto, Veľká Tŕňa, Viničky.',a='Tokajská oblasť',v=[V('Tokajské samorodné'),V('Tokajská výberová esencia'),V('Tokajská esencia-nektár'),V('Mášláš'),V('Fordítáš'),V('Tokajský Furmint'),V('Tokajská Lipovina'),V('Tokajský Muškát žltý')])],SK)
k_pl=K('Poland: wine areas','The wine-growing areas of Poland named on the national wine page.',
 'One entry is one Polish wine-growing area; Poland has no appellation list on the fetched page.','Areas named in Wikipedia Polish wine; no official appellation list is on a fetched page.','one flat list',tt(['Regent','Rondo','Pinot noir','Solaris','Riesling','Seyval blanc','Pinot gris','Johanniter','Hibernal']),
 [E('Lower Silesia',PL,'South-western area with a strong grouping of wineries around Wrocław.'),E('Zielona Góra',PL,'Western area where wineries cluster.'),E('Lesser Poland',PL,'Southern area around Kraków.'),E('Subcarpathia',PL,'South-eastern area (Podkarpacie).'),E('Lublin',PL,'Eastern area including Kazimierz Dolny.')],PL)
# ---------- Balkans ----------
SI=W+'Slovenian_wine'; HR=W+'Croatian_wine'; RS=W+'Serbian_wine'; MK=W+'Macedonian_wine'; ME=W+'Montenegrin_wine'; AL=W+'Albanian_wine'; BA=W+'Bosnia_and_Herzegovina_wine'
sl=[('Goriška Brda','Primorska (Littoral)','Includes passito-style Verduc and Pikolit.'),('Koper','Primorska (Littoral)','Covers the Istrian peninsula.'),('Kras','Primorska (Littoral)','The Karst.',[V('Teran','traditional protected wine of the Karst')]),('Vipava Valley','Primorska (Littoral)',''),
('Bizeljsko-Sremič','Posavje (Lower Sava)','Known for sparkling wine.',[V('Bizeljčan','traditional protected wine')]),('Dolenjska (Lower Carniola)','Posavje (Lower Sava)','',[V('Cviček','traditional protected wine')]),('Bela krajina (White Carniola)','Posavje (Lower Sava)','',[V('Belokranjec','traditional protected wine'),V('Metliška Črnina','traditional protected wine')]),
('Radgona-Kapela','Podravje (Drava)','Méthode champenoise sparkling wine from 1852.'),('Ljutomer-Ormož','Podravje (Drava)',''),('Maribor','Podravje (Drava)',''),('Haloze','Podravje (Drava)',''),('Prekmurje','Podravje (Drava)',''),('Central Slovene Hills','Podravje (Drava)',''),('Šmarje-Virštanj','Podravje (Drava)','')]
k_si=K('Slovenia: wine districts','The Slovenian wine districts in the three wine regions.',
 'One entry is one Slovenian wine district; traditional protected wines are versions.','The districts named in Wikipedia Slovenian wine (14); the page does not use official PDO district names.','by wine region',tt(['Rebula (Ribolla)','Malvazija','Refošk','Merlot','Sauvignon blanc','Welschriesling','Šipon (Furmint)','Zweigelt','Blaufränkisch','Kraljevina']),
 [E(n,SI,(d or 'Slovenian wine district.'),g=g,v=(v[0] if v else [])) for n,g,d,*v in sl],SI)
hr=[('Podunavlje','Eastern Continental','Baranja, Erdut, Srijem.'),('Slavonija','Eastern Continental','Premium Graševina; Daruvar, Đakovo, Kutjevo, Požega-Pleternica and others.'),('Moslavina','Western Continental','Škrlet, Kraljevina, Moslavac.'),('Plešivica','Western Continental','Samobor, Plešivica-Okić and others.'),('Pokuplje','Western Continental',''),('Prigorje-Bilogorje','Western Continental','Zagreb, Kalnik, Bilogora and others.'),('Zagorje-Međimurje','Western Continental',''),
('Istria','Coastal: Istria and Kvarner','Malvazija Istarska white and Teran red.'),('Hrvatsko Primorje','Coastal: Istria and Kvarner','Opatija-Rijeka-Vinodol and the islands Krk, Rab, Cres-Lošinj, Pag; Žlahtina on Krk.'),
('Northern Dalmatia','Coastal: Dalmatia','Pirovac-Skradin, Primošten, Šibenik, Zadar-Biograd; Babić, Debit.'),('Dalmatian interior','Coastal: Dalmatia','Dalmatinska Zagora, Imotski, Sinj; Kujundžuša.'),('Central and South Dalmatia','Coastal: Dalmatia','Kaštela-Trogir, Split-Omiš-Makarska, Neretva, Konavle, Pelješac and the islands; Plavac Mali, Pošip, Grk, Prošek.')]
k_hr=K('Croatia: wine sub-regions','The Croatian wine regions and sub-regions, with the named hill appellations as versions.',
 'One entry is one Croatian wine sub-region (podregija); named hills are versions.','The twelve sub-regions in Wikipedia Croatian wine (first 100,000 characters read). Croatia has no PDO list on that page; Dingač and Postup are named hills with Yugoslav state protection.','by wine region',tt(['Graševina','Plavac Mali','Malvazija Istarska','Teran','Pošip','Grk','Babić','Škrlet','Žlahtina','Kujundžuša']),
 [E(n,HR,d or 'Croatian wine sub-region.',g=g,v=([V('Dingač','Pelješac hill, registered for Yugoslav state protection in 1961','1961'),V('Postup','Pelješac hill, registered for Yugoslav state protection in 1967','1967'),V('Prošek','Dalmatian dessert wine from dried grapes')] if n.startswith('Central') else [])) for n,g,d in hr],HR)
rs=[('Srem','Vojvodina'),('Subotica','Vojvodina'),('Telečka','Vojvodina'),('Potisje','Vojvodina'),('Banat','Vojvodina'),('South Banat','Vojvodina'),('Bačka','Vojvodina'),('Pocerina-Valjevo','Central Serbia'),('Mlava','Central Serbia'),('Toplica','Central Serbia'),('Čačak-Kraljevo','Central Serbia'),('Three Moravas','Central Serbia'),('Belgrade','Central Serbia'),('Šumadija','Central Serbia'),('Negotin Valley','Eastern and southern Serbia'),('Knjaževac','Eastern and southern Serbia'),('Niš','Eastern and southern Serbia'),('Nišava','Eastern and southern Serbia'),('Leskovac','Eastern and southern Serbia'),('Vranje','Eastern and southern Serbia'),('North Metohija','Kosovo'),('South Metohija','Kosovo')]
k_rs=K('Serbia: wine regions','The 22 Serbian wine regions of the 2013 classification, including the Kosovo regions it lists.',
 'One entry is one wine region of the 2013 Serbian classification.','All 22 regions of the 2013 classification in Wikipedia Serbian wine (the 1970s classification of nine regions is not used); Fruška Gora is a hill area within Srem and not an entry.','by province',tt(['Prokupac','Vranac','Smederevka','Tamjanika','Krstač','Welschriesling (Grašac)','Merlot','Cabernet Sauvignon']),
 [E(n,RS,f'Serbian wine region in {g}.',g=g,v=([V('Bermet','revived traditional wine from Sremski Karlovci')] if n=='Srem' else [])) for n,g in rs],RS)
k_sb=K('Southern Balkans: wine regions','The wine regions of North Macedonia, Montenegro, Bosnia and Herzegovina and Albania named on national wine pages.',
 'One entry is one wine region or zone of a southern Balkan country, as the national wine page names it.','Regions named in Wikipedia pages for North Macedonia, Montenegro, Bosnia and Herzegovina and Albania; none of these pages lists protected names, so no appellation list is claimed.','by country',tt(['Vranec','Kratošija','Vranac','Krstač','Žilavka','Blatina','Shesh','Kallmet','Smederevka','Stanušina crna']),
 [E('Povardarie',MK,'Vardar valley around Negotino and Kavadarci; leading region for volume and quality.',g='North Macedonia'),E('Pčinja-Osogovo',MK,'Eastern region along the Bulgarian border.',g='North Macedonia'),E('Pelagonija-Polog',MK,'Western region around Lake Ohrid.',g='North Macedonia'),
 E('Lake Skadar region',ME,'The most important Montenegrin wine region; the page counts four regions and fifteen sub-regions without naming them.',g='Montenegro'),E('Montenegrin Adriatic coast',ME,'The other principal Montenegrin wine area.',g='Montenegro'),
 E('Southern Herzegovina',BA,'South of Mostar around Čitluk, Međugorje, Ljubuški and Čapljina.',g='Bosnia and Herzegovina'),E('Trebinje area',BA,'Includes the Tvrdoš Monastery cellars.',g='Bosnia and Herzegovina'),E('Northern Bosnia',BA,'Several wineries east of Banja Luka.',g='Bosnia and Herzegovina'),
 E('Albanian coastal plains',AL,'Western lowlands to 300 m: Tirana, Durrës, Shkodër, Lezhë, Fier, Vlorë, Delvinë.',g='Albania'),E('Albanian central hills',AL,'300 to 600 m: Elbasan, Krujë, Berat, Përmet, Librazhd.',g='Albania'),E('Albanian eastern sub-mountains',AL,'600 to 800 m: Pogradec, Korçë, Leskovik, Peshkopi.',g='Albania'),E('Albanian highlands',AL,'Vines to about 1,000 m on clay-silica soils.',g='Albania')],MK)
# ---------- Eastern Europe ----------
RO=W+'Romanian_wine'; BG=W+'Bulgarian_wine'; MD=W+'Moldovan_wine'; UA=W+'Ukrainian_wine'; RU=W+'Russian_wine'
ro={'Transylvanian Plateau':['Târnave','Alba','Aiud','Sebeș-Apold','Lechința'],'Moldavian Hills':['Cotnari','Iași','Huși','Zeletin','Colinele Tutovei','Dealul Bujorului','Iveşti','Nicoreşti','Covurlui','Panciu','Odobești','Cotești'],'Muntenia and Oltenia Hills':['Dealurile Buzăului','Dealu Mare','Ștefănești','Sâmburești','Drăgășani','Dealurile Craiovei','Podgoria Severinului','Plaiurile Drâncei'],'Banat Hills':['Moldova Nouă','Recaș','Silagiu','Teremia','Tirol'],'Crișana Hills and Maramureș':['Miniș-Măderat','Diosig','Șimleu Silvaniei','Valea lui Mihai'],'Dobruja Hills':['Sarica-Niculițel','Istria-Babadag','Murfatlar'],'Danube Terraces':['Greaca','Ostrov'],'Southern sandy regions':['Sadova-Corabia','Calafat','Podgoria Dacilor']}
k_ro=K('Romania: wine regions and vineyards','The Romanian wine regions (podgorii) grouped by hill area.',
 'One entry is one Romanian wine region or vineyard (podgorie) as the national wine page groups them.','All 8 hill groups and 43 vineyards in Wikipedia Romanian wine; the page does not list DOC or IGP names, so no appellation status is claimed.','by hill area',tt(['Fetească albă','Fetească regală','Fetească neagră','Crâmpoșie','Tămâioasă Românească','Busuioacă de Bohotin','Băbească neagră','Grasă de Cotnari']),
 [E(n,RO,f'Romanian wine region in the {g}.',g=g) for g,ns in ro.items() for n in ns],RO)
k_bg=K('Bulgaria: wine regions','The five Bulgarian wine regions.','One entry is one of the five Bulgarian wine regions.','The five regions in Wikipedia Bulgarian wine; the page names no PDO or PGI areas.','from the Danube south',tt(['Mavrud','Gamza','Pamid','Dimyat','Red Misket','Shiroka Melnishka Losa','Muscat Ottonel','Cabernet Sauvignon','Merlot']),
 [E('Danubian Plain',BG,'North Bulgarian region on the south bank of the Danube; Gamza, Muscat Ottonel, Cabernet Sauvignon.'),E('Black Sea',BG,'East Bulgarian region with about 30 % of the vines; white wine, Dimyat, Riesling.'),E('Rose Valley',BG,'Sub-Balkan region of dry and off-dry whites.',v=[V('Sungurlare Valley','known for Red Misket')]),E('Thracian Lowland',BG,'South Bulgarian region; Mavrud, Merlot, Cabernet Sauvignon.'),E('Struma River Valley',BG,'South-west region with Mediterranean influence; Melnik.',v=[V('Melnik','Shiroka Melnishka Losa')])],BG)
k_md=K('Moldova: wine regions','The Moldovan protected wine regions and growing zones.','One entry is one Moldovan wine region with a protected geographical indication or a main growing zone.','The three PGI regions and four growing zones in Wikipedia Moldovan wine.','PGI regions, then growing zones',tt(['Fetească albă','Fetească regală','Rară neagră','Fetească neagră','Cabernet Sauvignon','Merlot','Rkatsiteli','Aligoté']),
 [E('Codru',MD,'Central historical region with a protected geographical indication.',g='Protected geographical indications'),E('Valul lui Traian',MD,'South-western historical region with a protected geographical indication.',g='Protected geographical indications'),E('Ștefan Vodă',MD,'South-eastern historical region with a protected geographical indication.',g='Protected geographical indications'),
  E('Bălți',MD,'Northern growing zone.',g='Growing zones'),E('Purcari',MD,'South-eastern growing zone.',g='Growing zones'),E('Cahul',MD,'Southern growing zone, suited to red sweet and semi-sweet wines.',g='Growing zones')],MD)
k_ua=K('Ukraine: wine areas','The wine areas of Ukraine named on the national wine page.','One entry is one Ukrainian wine area.','Areas named in Wikipedia Ukrainian wine; no appellation list is on the page.','by area',tt(['Aligoté','Muscat','Traminer','Cabernet Sauvignon','Chardonnay','Pinot noir','Rkatsiteli','Golubok']),
 [E('Southern Ukraine',UA,'Mykolaiv, Kherson, Dnipropetrovsk and Odesa oblasts.'),E('Bessarabia (Budjak)',UA,'Odesa Oblast; Shabo and Krynychne.'),E('Zakarpattia',UA,'Tisza valley, Carpathian Ruthenia.'),E('Crimea',UA,'Balaklava and Massandra; occupied by Russia since 2014.')],UA)
ru=['Sibirkovy','Tsimlyanski Cherny','Plechistik','Narma','Güliabi Dagestanski','Krasnostop Zolotovsky','Saperavi','Platovsky','Bastardo Magarachsky','Kefesia','Kokur Belyi']
k_ru=K('Russia: wine regions and appellations','The Russian wine regions and the controlled appellations the national wine page names.','One entry is one Russian wine region or controlled appellation.','Regions and the eleven appellations in Wikipedia Russian wine; the page gives no boundaries for the appellations.','regions, then appellations',tt(['Rkatsiteli','Aligoté','Saperavi','Cabernet Sauvignon','Merlot','Tsimlyansky Cherny','Krasnostop Zolotovsky']),
 [E(n,RU,'Wine region of Russia.',g='Regions') for n in ['Krasnodar (Kuban and Taman)','Rostov (Don Valley)','Stavropol','Dagestan']]+[E(n,RU,'Controlled appellation named on the page.',g='Controlled appellations') for n in ru],RU)
# ---------- Greece & Cyprus ----------
GRW=W+'Greek_wine'; GP='https://www.winewithseth.com/winewiki/opap-greek-pdo-classification-system/'; PE='https://www.winewithseth.com/winewiki/peloponnese-wine-region/'; CR='https://www.winewithseth.com/winewiki/crete-pdos-peza-archanes-dafnes-sitia/'; PD='https://www.winewithseth.com/winewiki/pdo-greece/'
gr=[('Naoussa','Macedonia','Age-worthy red from 100 % Xinomavro on the south-east slopes of Mount Vermio.',GP,'1971'),('Amyntaio','Macedonia','Xinomavro red, still rosé and sparkling wines on a plateau at 570 to 750 m.',PD,''),('Goumenissa','Macedonia','Xinomavro-based red.',GP,''),
('Rapsani','Thessaly','Xinomavro-based red.',GP,'1971'),('Nemea','Peloponnese','Red from 100 % Agiorgitiko.',PE,'1971'),('Mantinia','Peloponnese','White from at least 85 % Moschofilero.',PE,'1971'),('Patras','Peloponnese','Dry white from 100 % Roditis.',PE,'1972'),('Mavrodaphne of Patras','Peloponnese','Sweet fortified red from at least 51 % Mavrodaphne.',PE,'1971'),('Muscat of Patras','Peloponnese','Sweet wine from 100 % Muscat Blanc.',PE,''),('Muscat of Rio Patras','Peloponnese','Sweet wine from 100 % Muscat Blanc.',PE,''),('Monemvasia-Malvasia','Peloponnese','Sweet white from at least 51 % Monemvasia.',PE,''),
('Santorini','Aegean islands','Dry white from at least 85 % Assyrtiko; also Nykteri and sweet Vinsanto.',PD,'1971'),('Lemnos','Aegean islands','Sweet Muscat wine.',GP,''),('Samos','Aegean islands','Sweet Muscat wine.',GP,''),
('Mavrodaphne of Cephalonia','Ionian islands','Fortified red from Mavrodaphne.',GP,''),
('Peza','Crete','Largest Cretan PDO, about 70 % of Cretan wine; Kotsifali and Mandilaria reds, Vilana whites.',CR,''),('Archanes','Crete','Dry red co-fermented from Kotsifali and Mandilaria.',CR,''),('Dafnes','Crete','Liatiko dry reds and sweet wines from sun-dried grapes.',CR,''),('Sitia','Crete','Liatiko and Mandilaria reds; Vilana and Thrapsathiri whites.',CR,'')]
gv={'Santorini':[V('Nykteri','Santorini white'),V('Vinsanto','sweet, at least 51 % Assyrtiko, sun-dried')]}
k_gr=K('Greece: PDO wines','The Greek protected-designation wines named on fetched wine pages.',
 'One entry is one Greek PDO, a protected wine zone named for its place, sectioned by region.',
 'Greece has 33 PDOs and 114 PGIs (Vinepair, WineWithSeth). Only the 19 PDOs named with details on the fetched pages are listed; the eAmbrosia register was not retrievable, so this is NOT the complete list and the remaining PDOs and all PGIs are missing.',
 'by Greek wine region',tt(['Xinomavro','Agiorgitiko','Moschofilero','Assyrtiko','Mavrodaphne','Muscat','Roditis','Kotsifali','Mandilaria','Liatiko','Vilana']),
 [E(n,s,d,g=g,y=y,v=gv.get(n,[])) for n,g,d,s,y in gr],GP)
CY=W+'Cypriot_wine'
k_cy=K('Cyprus: wine areas','The Cypriot local-wine areas and the Commandaria zone.','One entry is one Cypriot wine area or protected zone.','The four local-wine areas and wine routes named in Wikipedia Cypriot wine; the page does not name the PDO areas individually other than Commandaria.','local-wine areas, then the Commandaria zone',tt(['Xynisteri','Mavro','Maratheftiko','Carignan','Shiraz','Yiannoudi','Ofthalmo']),
 [E(n,CY,'Cypriot local-wine (geographical indication) area.',g='Local-wine areas') for n in ['Lefkosia','Lemesos','Larnaca','Paphos']]+[E('Commandaria',CY,'Sweet, high-alcohol wine mainly from Mavro, listed as the Koumandaria wine route.',g='Protected zone',v=[])],CY)
# ---------- Turkey, Caucasus, Levant ----------
TW=W+'Turkish_wine'; GE=W+'Georgian_wine'; AM=W+'Armenian_wine'; LB=W+'Lebanese_wine'; IL=W+'Israeli_wine'
k_tr=K('Turkey: wine regions','The Turkish wine regions and the districts the national wine page names.','One entry is one Turkish wine region or district.','Regions and districts in Wikipedia Turkish wine; Turkey has no appellation list on the page.','by wine region',tt(['Öküzgözü','Boğazkere','Kalecik Karası','Papazkarası','Narince','Emir','Sultaniye','Bornova Misketi','Çalkarası']),
 [E('Thrace and Marmara',TW,'Kırklareli, Tekirdağ, Şarköy, Gelibolu; 30 to 40 % of Turkish wine.'),E('Aegean',TW,'Largest region by volume: Urla, Çeşme, Bozcaada, Denizli (Çal), Manisa.'),E('Central Anatolia',TW,'Cappadocia and Ankara, including Kalecik.'),E('Eastern and Southeastern Anatolia',TW,'Elazığ, Malatya, Diyarbakır, Mardin.'),E('Mediterranean',TW,'Scattered vineyards around Elmalı in Antalya.'),E('Black Sea',TW,'Tokat province.')],TW)
geo_r=[('Kakheti','Telavi and Kvareli micro-regions; about 70 % of Georgian grapes.'),('Kartli',''),('Imereti',''),('Racha-Lechkhumi and Kvemo Svaneti',''),('Adjara','')]
ge=[('Tsinandali','White','Rkatsiteli and Mtsvane; Telavi and Kvareli.'),('Mtsvane','White','Dry.'),('Tvishi','White','Natural semi-sweet Tsolikauri from Lechkhumi.'),('Pirosmani (white)','White','Semi-sweet; 40 % Tsolikauri, 60 % Tsitska.'),('Alaznis Veli','White','Semi-sweet.'),('Anakopia','White','Semi-dry Tsolikauri.'),('Khikhvi','White','Amber dessert wine.'),('Saamo','White','Sweet dessert Rkatsiteli.'),('Gelati','White','Dry Tsolikauri, Tsitska, Krakhuna.'),('Kakheti (table wine)','White','Amber Rkatsiteli and Mtsvane.'),('Bodbe','White','Rkatsiteli; Magaro.'),('Dimi','White','Tsolikauri, Krakhuna; Imereti.'),('Gareji','White','Dry Rkatsiteli and Mtsvane.'),('Ereti','White','Dry Rkatsiteli and Mtsvane.'),('Shuamta','White','Dry amber Rkatsiteli and Mtsvane.'),('Alazani (white)','White','Semi-sweet 100 % Rkatsiteli.'),('Alaverdi (white)','White',''),
('Tbilisuri','Rosé','Semi-dry; Saperavi, Cabernet, Rkatsiteli.'),('Aguna','Rosé','Semi-dry; Saperavi, Cabernet, Rkatsiteli.'),('Mtatsminda','Rosé','Semi-dry; Saperavi, Tavkveri, Asuretuli, Rkatsiteli.'),('Sachino','Rosé','Semi-dry; West Georgia.'),('Lykhny','Rosé','Semi-sweet Izabela; Abkhazia.'),
('Akhasheni','Red','Semi-sweet Saperavi from Gurjaani.'),('Khvanchkara','Red','Semi-sweet Alexandrouli and Mudzhuretuli from Racha.'),('Kindzmarauli','Red','Semi-sweet Saperavi from Kvareli.'),('Mukuzani','Red','Dry oak-aged 100 % Saperavi.'),('Napareuli','Red',''),('Ojaleshi','Red','Semi-sweet Ojaleshi from Samegrelo.'),('Pirosmani (red)','Red','Semi-sweet Saperavi.'),('Saperavi','Red','Extractive Saperavi from Kakheti.'),('Usakhelauri','Red','Semi-sweet; West Georgia.'),('Apsny','Red','Semi-sweet; Abkhazia.'),('Barakoni','Red','Semi-dry; Rioni gorge.'),('Salkhino','Red','Liqueur-type dessert wine.'),('Alazani (red)','Red','Semi-sweet; 60 % Saperavi, 40 % Rkatsiteli.'),('Alaverdi (red)','Red',''),('Rkatsiteli Mtsvani','Red',''),('Saperavi Dzelshavi','Red',''),
('Kardanakhi','Fortified','Amber fortified white, port type; Gurjaani.'),('Anaga','Fortified','Madeira-type.'),('Sighnaghi','Fortified','Amber, port type.'),('Veria','Fortified','Amber fortified white.'),('Lelo','Fortified','Golden, port type.'),('Marabda','Fortified','Light golden, port type.'),('Kolkheti','Fortified','Amber fortified white.'),('Taribana','Fortified','Port type; Rkatsiteli.')]
k_ge=K('Georgia: wine regions and named wines','The Georgian wine regions and the named wines the national wine page lists by colour and style.',
 'One entry is one Georgian named wine (appellation-style name) or wine region.','The five regions and 46 named wines in Wikipedia Georgian wine (first 100,000 characters read); the page does not mark which names are legally protected, so no PDO status is claimed. Mukuzani, Kindzmarauli, Khvanchkara, Akhasheni, Napareuli and Tsinandali take over the old Saperavi, Aleksandrouli and Rkatsiteli kinds.','regions, then wines by colour and style',tt(['Rkatsiteli','Mtsvane','Saperavi','Tsolikauri','Tsitska','Alexandrouli','Mudzhuretuli','Ojaleshi','Krakhuna','Khikhvi']),
 [E(n,GE,d or 'Georgian wine region.',g='Regions') for n,d in geo_r]+[E(n,GE,d or f'{c} Georgian wine.',g=f'{c} wines') for n,c,d in ge],GE)
k_am=K('Armenia: wine regions','The Armenian wine regions named on the national wine page.','One entry is one Armenian wine region.','Regions named in Wikipedia Armenian wine (first 100,000 characters read); the page mentions no PGI list.','one flat list',tt(['Areni','Voskehat','Kangun','Saperavi','Pinot noir','Chilar']),
 [E('Vayots Dzor',AM,'Includes Areni; Areni and Voskehat grapes.'),E('Aragatsotn',AM,'Areni and Voskehat grapes.'),E('Ararat',AM,'Ararat plain; Areni, Saperavi, Muscat, Kharji.'),E('Armavir',AM,'Wines from the Ararat plain.'),E('Tavush',AM,'Aghstev valley; known for pomegranate wine.'),E('Gegharkunik',AM,'Region named on the page.'),E('Kotayk',AM,'Region named on the page.'),E('Shirak',AM,'Region named on the page.')],AM)
k_lb=K('Lebanon: wine regions','The Lebanese wine regions named on the national wine page.','One entry is one Lebanese wine region.','Regions in Wikipedia Lebanese wine; the page describes no formal appellation system.','one flat list',tt(['Cabernet Sauvignon','Syrah','Cinsault','Carignan','Merlot','Chardonnay','Obeideh','Merwah','Meksassi']),
 [E('Bekaa Valley',LB,'Produces most Lebanese wine; continental climate.'),E('Batroun',LB,'High-altitude district in North Lebanon.'),E('Mount Lebanon',LB,'High-altitude area.'),E('North Lebanon',LB,'High-altitude area.'),E('Southern Lebanon (Jezzine)',LB,'High-altitude area around Jezzine.')],LB)
k_il=K('Israel: wine regions','The Israeli wine regions and sub-regions named on the national wine page.','One entry is one Israeli wine region; sub-regions are versions.','Regions in Wikipedia Israeli wine; the page gives no full sub-region list.','one flat list',tt(['Cabernet Sauvignon','Merlot','Chardonnay','Sauvignon blanc','Cabernet franc','Syrah','Argaman']),
 [E('Galilee',IL,'Most suited region, high and cool.',v=[V('Upper Galilee'),V('Lower Galilee'),V('Golan Heights','legal status contested abroad')]),E('Judean Hills',IL,'Surrounds Jerusalem.'),E('Shimshon (Samson)',IL,'Between the Judean Hills and the coastal plain.'),E('Negev',IL,'Semi-arid, drip-irrigated vineyards.'),E('Sharon Plain',IL,'Near Zichron Ya\'akov and Binyamina; largest grape-growing area.')],IL)

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

def D(n,t,ax,shelves):
    return {'n':n,'mode':'variety','t':t,'ax':ax,'s':[{'n':sn,'t':st,'ax':sa,'k':ks} for sn,st,sa,ks in shelves],
     'b':[{'m':'Appellation and classification','v':'regional → district → village or vineyard where the country has a classification','w':'Official appellation systems set the expected quality and style.'},{'m':'Vintage and drinking window','w':'The harvest year decides whether the wine is ready, improving or past its best.'}]}
depts=[
D('Wine of Germany, Austria & Switzerland','Wine named for its German, Austrian or Swiss place: regions, districts and DAC or AOC areas; a grape sold worldwide → the grape departments.','Which country and which tier of its place system names the wine?',
 [('Germany','The German Anbaugebiete, their Bereiche and the Landwein regions.','kinds by tier of German place',[k_anb,k_ber,k_lw]),('Austria','The Austrian wine-growing areas and DACs.','kinds by tier',[k_aw,k_dac]),('Switzerland','The Swiss regions and the Vaud AOCs.','kinds by tier',[k_ch,k_chc,k_vd])]),
D('Wine of Hungary & Central Europe','Wine named for its Hungarian, Czech, Slovak or Polish place, including Tokaj and its sweet styles.','Which country and wine region names the wine?',
 [('Hungary','The Hungarian wine regions, their sub-regions and the PGIs.','kinds by tier',[k_hu,k_hs,k_hp]),('Czechia, Slovakia & Poland','Wine regions of the Czech Republic, Slovakia and Poland.','one kind per country',[k_cz,k_sk,k_skd,k_pl])]),
D('Wine of the Balkans','Wine named for its place in Slovenia, Croatia, Serbia and the southern Balkans.','Which country and wine region names the wine?',
 [('Slovenia & Croatia','Slovenian districts and Croatian sub-regions.','one kind per country',[k_si,k_hr]),('Serbia','The 22 Serbian wine regions.','one kind',[k_rs]),('Southern Balkans','North Macedonia, Montenegro, Bosnia and Herzegovina and Albania.','one kind',[k_sb])]),
D('Wine of Eastern Europe','Wine named for its place in Romania, Bulgaria, Moldova, Ukraine and Russia.','Which country and wine region names the wine?',
 [('Romania & Bulgaria','Romanian vineyards and Bulgarian regions.','one kind per country',[k_ro,k_roi,k_bg]),('Moldova, Ukraine & Russia','Moldovan PGI regions, Ukrainian areas and Russian appellations.','one kind per country',[k_md,k_ua,k_ru])]),
D('Wine of Greece & Cyprus','Wine named for its Greek or Cypriot place: PDO zones and island areas; a retsina or a sweet Samos is still named by its zone here.','Which country and which zone names the wine?',
 [('Greece','Greek PDOs and PGIs by region.','kinds by tier',[k_gr,k_gp]),('Cyprus','Cypriot local-wine areas and Commandaria.','one kind',[k_cy])]),
D('Wine of Turkey, the Caucasus & the Levant','Wine named for its place in Turkey, Georgia, Armenia, Lebanon and Israel, including Georgian named wines.','Which country and wine region names the wine?',
 [('Turkey','Turkish wine regions.','one kind',[k_tr]),('Georgia & Armenia','Georgian regions and named wines; Armenian regions.','one kind per country',[k_ge,k_am]),('Lebanon & Israel','Levant wine regions.','one kind per country',[k_lb,k_il])]),
]
renames={'Blaufränkisch':'Austria: DAC appellations','Zweigelt':'Austria: DAC appellations','Kadarka':'Hungary: wine regions','Furmint':'Hungary: wine regions','Tokaji':'Hungary: wine regions','Plavac Mali':'Croatia: wine sub-regions','Prokupac':'Serbia: wine regions','Mavrud':'Bulgaria: wine regions','Xinomavro':'Greece: PDO wines','Agiorgitiko':'Greece: PDO wines','Assyrtiko':'Greece: PDO wines','Moschofilero':'Greece: PDO wines','Saperavi':'Georgia: wine regions and named wines','Aleksandrouli':'Georgia: wine regions and named wines','Rkatsiteli':'Georgia: wine regions and named wines','Retsina':'Greece: PGI wines','Kisi':'Georgia: wine regions and named wines','Müller-Thurgau':'Germany: Anbaugebiete','Sylvaner':'Germany: Anbaugebiete','Kerner':'Germany: Anbaugebiete'}
out={'depts':depts,'brands':[],'renames':renames,'moves':[]}
json.dump(out,open('/home/user/Possession-Taxonomy/rebuild/out/J7_parts/WCE.json.tmp','w'),ensure_ascii=False,indent=1)
os.replace('/home/user/Possession-Taxonomy/rebuild/out/J7_parts/WCE.json.tmp','/home/user/Possession-Taxonomy/rebuild/out/J7_parts/WCE.json')
print(sum(len(k['x']) for d in depts for s in d['s'] for k in s['k']),'entries')
