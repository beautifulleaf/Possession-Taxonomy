import json,sys,re
R='/home/user/Possession-Taxonomy/rebuild/'
d=json.load(open(R+'out/A5.json'))
W=[x for x in d['depts'] if x['n']=='Wristwatches'][0]
WP='https://en.wikipedia.org/wiki/'
CAT=WP+'Category:Watch_models'
CATO=WP+'Category:Omega_watches'; CATR=WP+'Category:Rolex_watches'; CATC=WP+'Category:Casio_watches'; CATT=WP+'Category:Timex_watches'
S=dict(rolex=WP+'Rolex',omega=WP+'Omega_SA',seiko=WP+'Seiko',gs=WP+'G-Shock',patek=WP+'Patek_Philippe_%26_Co.',ap=WP+'Audemars_Piguet',cartier=WP+'Cartier_(jeweler)',
 breitling=WP+'Breitling_SA',heuer=WP+'TAG_Heuer',iwc=WP+'IWC_Schaffhausen',jlc=WP+'Jaeger-LeCoultre',longines=WP+'Longines',tudor=WP+'Tudor_Watches',
 hamilton=WP+'Hamilton_Watch_Company',zenith=WP+'Zenith_(watchmaker)',tissot=WP+'Tissot',panerai=WP+'Panerai',vc=WP+'Vacheron_Constantin',swatch=WP+'Swatch',
 gseiko=WP+'Grand_Seiko',bulova=WP+'Bulova',lange=WP+'A._Lange_%26_S%C3%B6hne',hublot=WP+'Hublot',junghans=WP+'Junghans',casio=WP+'Casio',citizen=WP+'Citizen_Watch',
 movado=WP+'Movado_Group',timex=WP+'Timex_Group',fossil=WP+'Fossil_Group',black=WP+'Black_Watch_(wristwatch)',fo=WP+'Flying_Officer_Chronograph',gallet=WP+'Gallet_Clamshell',www=WP+'Waterproof_wristlet_watch',
 wd=lambda q:'https://www.wikidata.org/wiki/'+q)
SW='The Swatch Group';RI='Richemont';LV='LVMH';HW='Hans Wilsdorf Foundation (Rolex SA)'
NS='owner not stated'
# maker: (country, owner, tier, own_y)
M={
'Rolex':('Switzerland',HW,'Independent',''),'Tudor':('Switzerland',HW,'Independent',''),
'Patek Philippe':('Switzerland','Stern family (Patek Philippe)','Independent','1932'),
'Audemars Piguet':('Switzerland','Audemars Piguet (family-owned)','Independent',''),
'Omega':('Switzerland',SW,'Global group',''),'Blancpain':('Switzerland',SW,'Global group','1992'),'Breguet':('Switzerland',SW,'Global group','1999'),
'Longines':('Switzerland',SW,'Global group','1983'),'Hamilton':('United States',SW,'Global group',''),'Tissot':('Switzerland',SW,'Global group',''),'Swatch':('Switzerland',SW,'Global group',''),
'A. Lange & Söhne':('Germany',RI,'Global group','2000'),'IWC Schaffhausen':('Switzerland',RI,'Global group','2000'),'Jaeger-LeCoultre':('Switzerland',RI,'Global group','2000'),
'Panerai':('Italy',RI,'Global group',''),'Piaget':('Switzerland',RI,'Global group',''),'Vacheron Constantin':('Switzerland',RI,'Global group','1996'),'Cartier':('France',RI,'Global group',''),
'Van Cleef & Arpels':('France',RI,'Global group',''),
'Heuer':('Switzerland',LV,'Global group','1999'),'Zenith':('Switzerland',LV,'Global group','1999'),'Hublot':('Switzerland',LV,'Global group','2008'),'Bulgari':('Italy',LV,'Global group','2011'),
'Breitling':('Switzerland','Partners Group','Independent','2022'),
'Citizen':('Japan','Citizen Watch Co.','National champion',''),'Bulova':('United States','Citizen Watch Co.','Independent','2008'),
'Seiko':('Japan','Seiko Group Corporation','National champion',''),'Grand Seiko':('Japan','Seiko Group Corporation','National champion',''),
'Casio':('Japan','Casio Computer Co.','National champion',''),
'Zodiac':('Switzerland','Fossil Group','Independent','2001'),'Movado':('Switzerland','Movado Group','Independent',''),
'Timex':('United States','Timex Group','Independent',''),'Junghans':('Germany','Hans-Jochem Stein','Independent','2008'),
'Gallet':('Switzerland',NS,'',''),'Sinclair Radionics':('United Kingdom',NS,'',''),
}
CTY={'Baltic':'France','Chanel':'France','Chopard':'Switzerland','Christopher Ward':'United Kingdom','Doxa':'Switzerland','F.P. Journe':'Switzerland','Girard-Perregaux':'Switzerland','Glycine':'Switzerland','Greubel Forsey':'Switzerland','Lorier':'United States','MB&F':'Switzerland','Nomos Glashütte':'Germany','Orient':'Japan','Oris':'Switzerland','Philippe Dufour':'Switzerland','Poljot':'Russia','Richard Mille':'Switzerland','Sinn':'Germany','Tutima':'Germany','Universal Genève':'Switzerland','Urwerk':'Switzerland','Vostok':'Russia','':'' }
CORD=['Switzerland','Germany','Japan','United States','France','Italy','United Kingdom','Russia','']
def mkinfo(mk):
    if mk in M: return M[mk]
    return (CTY.get(mk,''),NS,'','')
def stamp(e):
    mk=e.get('mk','')
    c,o,t,y=mkinfo(mk)
    if not mk:
        e['mk']=''
    e['cty']=c; e['own']=o
    if t: e['tier']=t
    if y: e['own_y']=y
    e['g']=(c or 'Maker not stated')+(': '+mk if mk else '')
# ---- additions
def N(n,mk,y,d,s,**kw):
    e=dict(n=n,d=d,mk=mk,y=y,s=s); e.update(kw); return e
ADD={
'Dive watch':[
 N('Hydronaut','Tudor','1999','Tudor dive line launched in 1999.',S['tudor']),
 N('Egiziano','Panerai','1956','GPF 2/56 "Egiziano Grosso" made for the Egyptian Navy in 1956.',S['panerai']),
],
'Pilot watch':[
 N('Special Pilot\'s Watch','IWC Schaffhausen','1936','Ref. 436, the groundwork for IWC\'s aviation collection.',S['iwc']),
 N('Big Pilot\'s Watch','IWC Schaffhausen','1940','Ref. 52 T.S.C., an observation watch for military pilots; re-interpreted in 2002 with a large case and clear dial.',S['iwc'],v=[{'n':'Ref. 52 T.S.C.','y':'1940','d':'observation watch for military pilots'},{'n':'Re-interpretation','y':'2002','d':'large case, clear dial'}]),
 N('Mark 11','IWC Schaffhausen','1948','Anti-magnetic pilot\'s watch.',S['iwc']),
 N('Weems Avigation','Longines','1927','Navigation wristwatch made with P.V.H. Weems; a smaller 33 mm version followed in 1937.',S['longines'],v=[{'n':'Original','y':'1927'},{'n':'33 mm version','y':'1937','d':'refs 3930, 3931, 4036'}]),
 N('Flying Officer Chronograph','Gallet','1939','Chronograph with a rotating 12-hour bezel and 23 city names for working out time changes; made by Gallet in La Chaux-de-Fonds from 1939.',S['fo']),
 N('Lone Eagle','Bulova','1927','Bulova watch modelled on Charles Lindbergh\'s 1927 transatlantic flight.',S['bulova']),
 N('Aerospace','Breitling','','Breitling aviation model with its own Wikipedia article; Breitling\'s page names Aerospace/Chronospace Auto as its aviation line.',CAT),
 N('Pilot','Zenith','','Current Zenith collection named on the maker page.',S['zenith']),
 N('Flightmaster','Omega','','Omega chronograph with its own Wikipedia article.',CATO),
],
'Field watch':[
 N('Ranger','Tudor','2014','Added to Tudor\'s Heritage collection in 2014.',S['tudor']),
 N('MIL-W-46374','','','US military specification for the field watch; has a Wikidata item as a watch.',S['wd']('Q6716100')),
 N('Colt','Breitling','','Breitling sports watch with its own Wikipedia article.',CAT),
 N('Expedition WS4','Timex','','Timex field watch with its own Wikipedia article.',CATT),
],
'GMT & world-time watch':[
 N('GMT-Master','Rolex','1954','Rolex dual-time watch, ref. 6542; the Rolex page gives 1954 in one place and 1955 in another.',S['rolex']),
],
'Chronograph':[
 N('Top Time','Breitling','','Breitling chronograph seen in the 1965 film Thunderball.',S['breitling']),
 N('Chronomaster','Zenith','','Current Zenith chronograph collection.',S['zenith']),
 N('Heritage Chrono','Tudor','2010','Tudor chronograph from the 2010 range.',S['tudor']),
 N('Omega Bullhead','Omega','','Omega chronograph with its own Wikipedia article (formerly listed as Seamaster Bullhead).',CATO),
 N('Omega 28.9 chronograph','Omega','','Omega chronograph with its own Wikipedia article.',CATO),
 N('Gallet Clamshell','Gallet','1936','Considered the first water-resistant chronograph; two-part case clamped round a flared crystal; made 1936 to 1951.',S['gallet'],role='origin'),
 N('Chronosplit','Heuer','1975','Digital chronograph from Heuer.',S['heuer']),
],
'Dress watch':[
 N('Jazzmaster','Hamilton','','Hamilton dress line; a Seaview Chronograph appeared in the 2020 film Tenet.',S['hamilton']),
 N('Campanola','Citizen','2000','Citizen mechanical line launched in 2000.',S['citizen']),
 N('Series 8','Citizen','','Citizen line named on the maker page.',S['citizen']),
 N('Langematik','A. Lange & Söhne','1997','Automatic line built on the Sax-0-Mat calibre.',S['lange']),
 N('Richard Lange','A. Lange & Söhne','','Current Lange family.',S['lange']),
 N('Classic Fusion','Hublot','','Hublot three-hand and chronograph line.',S['hublot']),
 N('Meister','Junghans','','Junghans line; a Chronoscope jubilee model appeared in 2011.',S['junghans']),
 N('King Seiko','Seiko','1961','Seiko line discontinued in 1975 and revived in 2022.',S['seiko']),
 N('Credor','Seiko','1974','Seiko\'s top-end dress brand.',S['seiko']),
 N('62GS','Grand Seiko','1967','First automatic Grand Seiko (Fratello dates it to 1966).',S['gseiko']),
 N('Elite','Zenith','','Zenith collection built on the Elite movement developed from 1991.',S['zenith']),
 N('1926','Tudor','2018','Tudor dress line announced at Baselworld 2018.',S['tudor']),
 N('Style','Tudor','2014','Tudor dress watches launched in 2014.',S['tudor']),
 N('1908','Rolex','','Rolex dress line.',S['rolex']),
 N('Luminor Due','Panerai','','Panerai model listed on the maker page.',S['panerai']),
],
'Prestige everyday watch':[
 N('Globemaster','Omega','','Omega line on which Master Chronometer certification debuted.',S['omega']),
 N('Drive de Cartier','Cartier','2016','Cartier cushion-case line launched in 2016.',S['cartier']),
],
'Everyday watch':[
 N('Seamaster Omegamatic','Omega','','Omega Seamaster with its own Wikipedia article.',CATO),
 N('Lord Matic','Seiko','1968','Seiko automatic line of 1968.',S['seiko']),
 N('Idea 2001','Tissot','1971','Tissot\'s first plastic watch.',S['tissot'],role='origin'),
 N('RockWatch','Tissot','1985','Tissot watch with a granite case, 1985.',S['tissot']),
 N('Swatch Skin','Swatch','1997','Ultra-thin Swatch line; the original launched 6 October 1997.',S['swatch']),
 N('Swatch Irony','Swatch','','Metal-cased Swatch line; the Irony Chronograph followed in 1996.',S['swatch']),
 N('Prince','Tudor','1952','Tudor\'s first self-winding model.',S['tudor']),
 N('North Flag','Tudor','2015','First Tudor with an in-house movement (MT5621).',S['tudor']),
 N('Formula 1','Heuer','','Current TAG Heuer line.',S['heuer']),
],
'Integrated-bracelet sports watch':[
 N('Link','Heuer','','Current TAG Heuer line.',S['heuer']),
],
'Shaped watch':[
 N('Duoplan','Jaeger-LeCoultre','1925','Rectangular two-movement-plate watch; sapphire glass from 1929.',S['jlc']),
],
'Electric & early quartz watch':[
 N('Oysterquartz','Rolex','','Rolex quartz line powered by the 5035/5055 movement, developed from the late 1960s.',S['rolex']),
 N('Electroquartz','Omega','','Omega early quartz watch with its own Wikipedia article.',CATO),
 N('Chrono-Quartz','Omega','','Omega early quartz chronograph with its own Wikipedia article.',CATO),
 N('Black Watch','Sinclair Radionics','1975','Electronic wristwatch with a red LED display that lit only when the case was pressed; launched September 1975.',S['black']),
 N('Casiotron','Casio','1974','Casio\'s first watch, QW02, November 1974.',S['casio']),
],
'Quartz watch':[
 N('Grand Seiko 9F','Grand Seiko','1993','High-grade quartz movement; the 95GS of 1988 marked the quartz return.',S['gseiko']),
 N('Precisionist','Bulova','2010','Bulova quartz line introduced in 2010.',S['bulova']),
],
'Digital watch':[
 N('Computron','Bulova','1976','Bulova LED watch introduced 1976; reissued 2019.',S['bulova']),
 N('T-Touch','Tissot','1999','First tactile watch, 1999.',S['tissot'],role='origin'),
 N('Digital Touch','Swatch','2011','Swatch touchscreen LCD watch.',S['swatch']),
 N('G-Shock Mudman','Casio','1985','DW-5500C of 1985; Mudman line from 1995.',S['gs']),
 N('G-Shock Rangeman','Casio','2013','GW-9400 of 2013; GPR-B1000 followed in 2018.',S['gs']),
 N('G-Shock Gulfmaster','Casio','2014','GWN-1000 of 2014; GWN-Q1000 in 2016.',S['gs']),
 N('G-Shock Gravitymaster','Casio','2016','GPW-1000.',S['gs']),
 N('G-Shock Raysman','Casio','1998','DW-9300.',S['gs']),
 N('G-Shock Wademan','Casio','1999','DW-9800.',S['gs']),
 N('G-Shock Gaussman','Casio','1999','AW-571.',S['gs']),
 N('G-Shock Lungman','Casio','1999','DWG-100.',S['gs']),
 N('G-Shock Antman','Casio','2000','GW-100.',S['gs']),
 N('G-Shock Riseman','Casio','2008','GW9200; the DW-9100 Riseman is named without a year.',S['gs']),
 N('G-Shock Fisherman','Casio','1996','DW-8600.',S['gs']),
 N('G-Shock Gulfman','Casio','','DW-9700 Gulfman, named without a year.',S['gs']),
 N('G-Shock Seaman','Casio','','DW-9950 Seaman, named without a year.',S['gs']),
 N('Baby-G','Casio','1994','G-Shock line, launched 1994.',S['gs']),
 N('MR-G','Casio','1996','Top-end G-Shock line (MRG-100 / DW-8900, 1996); MRG-B5000 in 2022.',S['gs']),
 N('MT-G','Casio','2000','Metal-Twisted G-Shock, MTG-100 of 2000.',S['gs']),
 N('G-Shock DW-6100','Casio','1992','G-Shock model of 1992.',CATC),
 N('Edifice','Casio','','Casio watch line with its own Wikipedia article.',CATC),
 N('Oceanus','Casio','','Casio watch line with its own Wikidata item.',S['wd']('Q5048930')),
 N('Pro Trek','Casio','','Casio outdoor line named on the maker page.',S['casio']),
 N('AE-1000W','Casio','','Casio digital watch with its own Wikipedia article.',CATC),
 N('Expedition WS4 (digital)','Timex','','','') ,
 N('HP-01','','','Calculator watch with its own Wikipedia article.',CAT),
 N('Ruputer','','','Wrist computer with its own Wikipedia article.',CAT),
],
'Radio-controlled watch':[
 N('Mega','Junghans','1990','Mega 1 of 1990 was Junghans\'s first radio-controlled wristwatch, designed by Hartmut Esslinger and Frog Design; the Mega line is dated 1991 elsewhere on the page.',S['junghans'],role='origin'),
],
'Chronometer watch':[
 N('Geophysic','Jaeger-LeCoultre','1958','JLC Geophysic of 1958.',S['jlc']),
],
'Alarm watch':[
 N('Advisor','Tudor','1957','Tudor alarm watch, 1957.',S['tudor']),
],
'Split-seconds chronograph':[
 N('Triple Split','A. Lange & Söhne','2018','Split-seconds chronograph introduced in January 2018.',S['lange']),
],
'Tourbillon watch':[
 N('Cabaret Tourbillon','A. Lange & Söhne','2008','Lange tourbillon with stop-seconds mechanism, 2008.',S['lange']),
],
'Grande-complication watch':[
 N('Grande Complication (Ref. 3770)','IWC Schaffhausen','1990','First wristwatch-sized Grande Complication with chronograph, minute repeater and perpetual calendar.',S['iwc'],role='origin'),
 N('Sky Moon Tourbillon','Patek Philippe','2001','First model Ref. 5002.',S['patek']),
 N('Les Cabinotiers','Vacheron Constantin','2024','Vacheron\'s unique-piece workshop; the Berkley Grand Complication was unveiled in 2024.',S['vc']),
],
'Avant-garde watch':[
 N('Royal Oak Concept','Audemars Piguet','2002','High-tech platform for innovation created by Claude Emmenegger.',S['ap']),
],
}
ADD['Digital watch']=[e for e in ADD['Digital watch'] if e['n']!='Expedition WS4 (digital)']
ADD['Digital watch'].append(N('Expedition WS4','Timex','','Timex digital watch with its own Wikipedia article.',CATT))
# remove duplicate across kinds
ADD['Field watch']=[e for e in ADD['Field watch'] if e['n']!='Expedition WS4']
# versions to add to existing entries (by entry name)
VADD={
 'Tank':[('Tank cintrée','1921',''),('Tank Louis Cartier','1922',''),('Tank Chinoise','1922',''),('Tank Américaine','1989',''),('Tank Française','1996','')],
 'Royal Oak':[('Perpetual Calendar','',''),('Repeater Supersonnerie','','')],
 'Code 11.59':[('Ultra-Complication Universelle RD#4','','')],
 'Octo Finissimo':[('Ultra Tourbillon','','')],
 'Portugieser':[('Grande Complication','','')],
 'Accutron':[('Accutron Spaceview','2020','')],
 'Swatch Original':[('Bioreloaded','2020','relaunch of the 1983 collection, partly bio-sourced')],
 "Pilot's Watch":[('Special Pilot\'s Watch (Ref. 436)','1936','')],
 'Yacht-Master':[('Yacht-Master II','','')],
}
ROLES={'Electric 500':'origin','Pulsar':'origin','Astron':'origin','Zulu Time':'origin','Datejust':'origin','Speedmaster Professional':'landmark','Museum Watch':'landmark'}
KD={ # nl per kind
}
NL="One entry is a watch model line sold under its own name; references, generations and special editions are versions."
CH={'Switzerland':0}
cov=[]
tot=0; removed=[]
mvers=[]
for sh in W['s']:
    for k in sh['k']:
        old=k.get('m',[])
        k.pop('m',None)
        for r in k.get('r',[]) or []: pass
        xs=k.get('x',[]) or []
        names={e['n'].lower() for e in xs}
        for e in ADD.get(k['n'],[]):
            if e['n'].lower() in names: continue
            e.setdefault('v',[])
            xs.append(e); names.add(e['n'].lower())
        for e in xs:
            if e['n'] in VADD:
                have={v['n'].lower() for v in e.get('v',[])}
                for n,y,dd in VADD[e['n']]:
                    if n.lower() not in have:
                        v={'n':n}
                        if y: v['y']=y
                        if dd: v['d']=dd
                        e.setdefault('v',[]).append(v)
            if e['n'] in ROLES: e['role']=ROLES[e['n']]
            # fix mk for former blank
            if e['n']=='W.W.W. "Dirty Dozen"': e['mk']='Buren, Cyma, Eterna, IWC, Longines, Omega and six other makers'; e['y']=e.get('y') or '1945'
            if e['n']=='A-11': e['mk']='United States military'
            if e['n'].startswith('B-Uhr'): e['mk']='German Luftwaffe'
        for e in xs:
            mk=e.get('mk','')
            if mk in('United States military',): e.update(cty='United States',own='United States military',g='United States: military issue')
            elif mk=='German Luftwaffe': e.update(cty='Germany',own='German Luftwaffe',g='Germany: military issue')
            elif mk.startswith('Buren'): e.update(cty='Switzerland',own=NS,g='Switzerland: military issue (twelve makers)')
            else: stamp(e)
        xs.sort(key=lambda e:(CORD.index(e['cty']) if e['cty'] in CORD else 99, e.get('mk',''), str(e.get('y') or '9999'), e['n']))
        k['x']=xs; tot+=len(xs)
        k['nl']=NL
        k['xg']='by maker country, then maker, then year'
        k['_n']=len(xs)
        for m in old: removed.append((k['n'],m))
CLAUSE=("Model lines named on the fetched Wikipedia pages of each maker (Rolex, Omega, Seiko, G-Shock, Grand Seiko, Patek Philippe, Audemars Piguet, Cartier, Breitling, TAG Heuer, IWC, Jaeger-LeCoultre, Longines, Tudor, Hamilton, Zenith, Tissot, Panerai, Vacheron Constantin, Swatch, Bulova, A. Lange & Söhne, Hublot, Junghans, Citizen, Casio), "
 "every wristwatch page in Wikipedia's Category:Watch models and its Omega, Rolex, Casio and Timex subcategories, and the Wikidata items that are instances of watch (Q178794) and named wristwatch models; the earlier hand-built entries stay. Pocket watches, smartwatches and one-off museum objects are out of scope here. ")
for sh in W['s']:
    for k in sh['k']:
        k['sel']=CLAUSE+f"Covers {k['_n']} entries in this kind; Wikipedia's Category:Rolex watches is complete (15 of 15), the Omega (10), Casio (11) and Timex (4) categories are complete for wristwatch pages, and Watchbase blocked automated access, so lines of makers without a fetched page (Sinn, Oris, Nomos, Orient and most independents) rest on earlier sourcing."
        del k['_n']
# market
W['mode']='variety'
W['note']="Organised by type (kind → model line → reference or generation); the same model lines are also sectioned by maker country and maker, and the market layer gives each maker's owner, tier and home country. Calibres are named in the entry text (no movement kind)."
WS=lambda *a:a
ms=[
 dict(mkt='Swiss watch exports',who='Swiss watch industry (Federation of the Swiss Watch Industry)',share='CHF 25,552 million (-1.7 %)',yr=2025,s='https://monochrome-watches.com/swiss-watch-exports-down-2-percent-to-chf-25-billion-in-2025-mild-contraction-amid-challenging-times',note='export value against CHF 25,993 million in 2024'),
 dict(mkt='Swiss watch exports',who='United States (share of Swiss exports)',share='about 17 %',yr=2025,s='https://monochrome-watches.com/swiss-watch-exports-down-2-percent-to-chf-25-billion-in-2025-mild-contraction-amid-challenging-times',note='exports to the US fell 0.5 % in 2025; China fell 12 %, Hong Kong 6.5 %, Japan 5.8 %'),
 dict(mkt='Swiss watch exports by price band',who='Over CHF 3,000 export price',share='-1.9 %',yr=2025,s='https://monochrome-watches.com/swiss-watch-exports-down-2-percent-to-chf-25-billion-in-2025-mild-contraction-amid-challenging-times',note='change in value; CHF 500 to 3,000 stable; below CHF 500 down 4.5 %'),
 dict(mkt='Swiss watch industry by maker (Morgan Stanley / LuxeConsult)',who='Rolex',share='about 32 %',yr=2024,s='https://monochrome-watches.com/morgan-stanleys-top-50-watch-brands-for-2024',note='estimated turnover above CHF 10.5 billion; estimates, not brand-reported'),
 dict(mkt='Swiss watch industry by maker (Morgan Stanley / LuxeConsult)',who='Rolex, Patek Philippe, Audemars Piguet and Richard Mille',share='about 47 %',yr=2024,s='https://monochrome-watches.com/morgan-stanleys-top-50-watch-brands-for-2024',note='the "Big Four" combined'),
 dict(mkt='Swiss watch industry by maker (Morgan Stanley / LuxeConsult)',who='LVMH',share='just under 6 %',yr=2024,s='https://monochrome-watches.com/morgan-stanleys-top-50-watch-brands-for-2024',note='ranked fifth; Cartier second, Omega third'),
 dict(mkt='Swiss watch industry by maker (Morgan Stanley / LuxeConsult)',who='Rolex',share='about one third; about CHF 11 billion',yr=2025,s='https://www.thepeakmagazine.com.sg/watch-jewellery/swiss-watch-industry-report-2026',note='estimated turnover, first of six'),
 dict(mkt='Swiss watch industry by maker (Morgan Stanley / LuxeConsult)',who='Cartier',share='8 to 9 %; about CHF 3.5 to 3.6 billion',yr=2025,s='https://www.thepeakmagazine.com.sg/watch-jewellery/swiss-watch-industry-report-2026',note='second; Audemars Piguet about CHF 2.6 billion, Patek Philippe 2.5, Omega 2.2, Richard Mille 1.7'),
 dict(mkt='Group revenue',who='The Swatch Group',share='CHF 6.74 billion',yr=2024,s=S['swatch'],note='group revenue, a decrease'),
 dict(mkt='Group revenue',who='Richemont',share='EUR 21.4 billion',yr=2025,s=WP+'Richemont',note='whole group including jewellery; Compagnie Financière Rupert holds 10 % of equity and 51 % of votes'),
 dict(mkt='Group revenue',who='Citizen Watch',share='JPY 346.808 billion',yr=2026,s=S['citizen'],note='fiscal year ended 31 March 2026; watch segment external sales JPY 197.061 billion'),
 dict(mkt='Group revenue',who='Seiko Group',share='JPY 304.7 billion',yr=2024,s=S['seiko'],note='fiscal 2024'),
 dict(mkt='Group revenue',who='Casio',share='JPY 276.267 billion',yr=2026,s=S['casio'],note='fiscal year ended 31 March 2026; whole company, not watches alone'),
 dict(mkt='Group revenue',who='Fossil Group',share='US$1.14 billion',yr=2024,s=S['fossil'],note='whole group'),
 dict(mkt='Group revenue',who='Movado Group',share='US$752 million',yr=2023,s=S['movado'],note='whole group'),
 dict(mkt='Output',who='Patek Philippe',share='about 70,000 timepieces',yr=2023,s=S['patek'],note='Wikipedia infobox'),
 dict(mkt='Output',who='Audemars Piguet',share='50,000 (infobox) or about 40,000 (text)',yr=2023,s=S['ap'],note='the page gives both figures'),
]
W['ms']=ms
W['msum']="Swiss exports and the share of the four leading private makers are the best published picture of the luxury end; the groups' own revenue pages give the rest. Figures are estimates where marked, and Rolex and Patek Philippe publish no revenue."
W['b']=W['b']
out={'replaces':['Wristwatches'],'depts':[W],'renames':{},'moves':[]}
# brands
bd=json.load(open(R+'out/A5_brands.json'))['b']
have={b['n'].lower() for b in bd}
NB=[]
def nb(n,c,f,seg,dd,s):
    if n.lower() in have: return
    e={'n':n,'c':c,'seg':seg,'d':dd,'s':s}
    if f: e['f']=f
    NB.append(e)
nb('The Swatch Group','Switzerland','1983','Group','Biel/Bienne group formed in 1983 by the merger of ASUAG and SSIH; owns Omega, Longines, Tissot, Hamilton, Blancpain, Breguet and others.',S['swatch'])
nb('Richemont','Switzerland','','Group','Luxury group owning A. Lange & Söhne, IWC, Jaeger-LeCoultre, Panerai, Piaget, Vacheron Constantin and Cartier; Rupert family controls the votes.',WP+'Richemont')
nb('LVMH','France','','Group','Luxury group whose watch brands include TAG Heuer, Hublot, Zenith, Bulgari and Tiffany.',WP+'LVMH')
nb('Hans Wilsdorf Foundation (Rolex SA)','Switzerland','1905','Independent','Charitable foundation that owns Rolex and Tudor; Rolex was founded in 1905 and is based in Geneva.',S['tudor'])
nb('Citizen Watch Co.','Japan','1930','Group','Citizen Watch Co., Ltd. was incorporated in 1930; owns Bulova (2008), Frédérique Constant and Alpina (2016) and Arnold & Son (2012).',S['citizen'])
nb('Seiko Group Corporation','Japan','1881','Group','Founded in 1881 by Kintarō Hattori; holding company since 2001, renamed in 2022; owner is the Hattori family.',S['seiko'])
nb('Casio Computer Co.','Japan','1946','Group','Founded in 1946 as Kashio Seisakujo; maker of G-Shock.',S['casio'])
nb('Fossil Group','United States','1984','Group','Founded in 1984 in Texas; owns Zodiac (2001), Michele (2004), Skagen and Misfit.',S['fossil'])
nb('Movado Group','United States','1881','Group','Movado was founded in 1881 in La Chaux-de-Fonds; the group is based in New Jersey and owns Concord, EBEL, Olivia Burton and MVMT.',S['movado'])
nb('Timex Group','United States','1941','Group','Timex dates from the 1941 purchase of the Waterbury Clock Company; owned by Baupost Group since 2020 per Wikipedia.',S['timex'])
nb('Partners Group','Switzerland','','Investor','Took over the majority of Breitling from CVC on 23 December 2022.',S['breitling'])
nb('Gallet','Switzerland','','Independent','La Chaux-de-Fonds maker of the Clamshell and the Flying Officer chronograph.',S['gallet'])
nb('Sinclair Radionics','United Kingdom','','Independent','Maker of the 1975 Black Watch LED wristwatch.',S['black'])
nb('Junghans','Germany','1861','Independent','Schramberg maker founded 1861; owned by Hans-Jochem Stein since 2008.',S['junghans'])
BU={}
for n,t in [('Omega','Global group'),('Longines','Global group'),('Tissot','Global group'),('Hamilton','Global group'),('Blancpain','Global group'),('Breguet','Global group'),('Swatch','Global group'),('Jaeger-LeCoultre','Global group'),('IWC Schaffhausen','Global group'),('Vacheron Constantin','Global group'),('A. Lange & Söhne','Global group'),('Panerai','Global group'),('Cartier','Global group'),('Piaget','Global group'),('Zenith','Global group'),('Hublot','Global group'),('Bulgari','Global group'),('Rolex','Independent'),('Tudor','Independent'),('Patek Philippe','Independent'),('Audemars Piguet','Independent'),('Breitling','Independent'),('Seiko','National champion'),('Grand Seiko','National champion'),('Citizen','National champion'),('Casio','National champion'),('Bulova','Independent'),('Zodiac','Independent'),('Movado','Independent'),('Timex','Independent'),('Junghans','Independent')]:
    pass
BUP={}
for b in bd:
    if b['n'] in M:
        c,o,t,y=M[b['n']]
        u={'own':o,'tier':t,'c':c}
        if y: u['own_y']=y
        BUP[b['n']]=u
    elif b['n']=='TAG Heuer' :
        BUP['TAG Heuer']={'own':LV,'tier':'Global group','c':'Switzerland','own_y':'1999'}
out['brands']=NB; out['brand_updates']=BUP
json.dump(out,open(R+'out/A5_parts/WRIST.json','w'),ensure_ascii=False,indent=1)
json.dump({'removed':removed,'tot':tot},open(R+'work/V4_A5_WRIST/removed.json','w'),ensure_ascii=False,indent=1)
print('entries',tot,'removed m',len(removed),'new brands',len(NB),'bupd',len(BUP))
