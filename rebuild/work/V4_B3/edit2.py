import json, re, os
R='/home/user/Possession-Taxonomy/rebuild/out/'
d=json.load(open(R+'B3.json'))
kinds={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: kinds[k['n']]=k
KM={'T':'Table lamp','F':'Floor lamp','D':'Desk lamp','P':'Pendant light','W':'Wall light','C':'Flush ceiling light','S':'Lamp shade'}
WORD={'T':'Table lamp','F':'Floor lamp','D':'Desk lamp','P':'Hanging lamp','W':'Wall lamp','C':'Ceiling lamp','S':'Lamp shade'}
MOMA='https://www.moma.org/collection/works?q=lamp&classifications=3'
VDM='https://collection.design-museum.de/en/collection/?q=lamp'
VA='https://api.vam.ac.uk/v2/objects/search?q=lamp%20designer&page_size=100&year_made_from=1900'
SRC={'M':MOMA,'V':VDM,'A':VA}
HOLD={'M':'MoMA','V':'the Vitra Design Museum','A':'the V&A'}
def norm(s): return re.sub(r'[^a-z0-9]','',s.lower())
def exists(n):
    for k in kinds.values():
        for x in k.get('x',[]):
            if norm(x['n'])==norm(n): return True
    return False
added=0
def add(t,n,who,y,src,mk='',extra=''):
    global added
    if exists(n): return False
    k=kinds[KM[t]]
    dd=f"{WORD[t]} by {who}, held by {HOLD[src]}." if who else f"{WORD[t]} held by {HOLD[src]}."
    if extra: dd=dd[:-1]+'; '+extra+'.'
    k.setdefault('x',[]).append({'n':n,'a':'','d':dd,'mk':mk,'y':y,'s':SRC[src],'v':[]})
    added+=1; return True
M=lambda *a,**k: add(*a[:4],'M',*a[4:],**k)
# MoMA (Design classification, search "lamp": 191 results, pages 1-4)
L=[('P','Soft Lamps','Arian Brekveld','1995'),('F','Moloch','Gaetano Pesce','1970-71'),('T','Less Lamp','Jordi Canudas','2006'),('T','Splight','Matali Crasset','2005'),
('W','Lucellino','Ingo Maurer','1992'),('F','Von Nessen floor lamp','Walter Von Nessen','c. 1927-35'),('T','Bellflower','Wieki Somers','2007'),('P','85 Lamps','Rody Graumans','1992'),
('T','Anywhere Lamp','Greta Von Nessen','1951'),('F','Pfisterer floor lamp','Peter Pfisterer','c. 1940'),('D','Weese and Baldwin desk lamp','Harry Weese and Benjamin Baldwin','c. 1940'),
('D','Von Nessen desk lamp','Walter Von Nessen','1927'),('T','Nénuphar','Louis Majorelle and Daum Frères','c. 1900'),('S','Mukuri','Ryo Suzuki (HONOKA.lab)','2023'),
('T','Cow Dung Lamp','Adhi Nugraha','2021'),('F','Rope Trick','Stefan Diez','2013'),('T','Jetzt','Axel Schmid','2009'),('T','Tear Drop','Tokujin Yoshioka','2007'),
('T','Fold','Alexander Taylor','2005'),('F','Dandelion','deepdesign (Matteo Bazzicalupo, Raffaella Mangiarotti)','2003'),('T','Lotus.MGX','Janne Kyttanen','2003'),('T','Twister.MGX','Janne Kyttanen','2003'),
('T','Bague','Patricia Urquiola and Eliana Gerotto','2003'),('T','Rainy Day','Kazuhiro Yamanaka','2003'),('P','Pipe','Herzog & de Meuron','2002'),('T','ToFU','Tokujin Yoshioka','2000'),
('T','Block Lamp','Harri Koskinen','1996'),('F','Loto','Guglielmo Berchicci','1997'),('T','Big Switch','Stefano Giovannoni','1996'),('T','Crinkle','Lyn Godley and Lloyd Schwan','1996'),
('T','Cardboard Lamp','interware SARL','1996'),('T','Globlow','Vesa Hinkola, Markus Nevalainen and Rane Vaskivuori','1996'),('T','Knitted Lamp','Hella Jongerius','1995'),
('T','Los Minimalos Dos','Ingo Maurer','1994'),('T','Milkbottle Lamp','Tejo Remy','1991'),('S','Lamp Shade 1','Sebastian Bergne','1991'),('T','Constanzina','Paolo Rizzatto','1992'),
('T','Miss Sissi','Philippe Starck','1991'),('T','On Off','Alberto Meda, Franco Raggi and Denis Santachiara','1983'),('T','Ara','Philippe Starck','1988'),
('P','Little Black Nothing','Ingo Maurer','1986'),('F','ID-S','Ettore Sottsass','1987'),('F','Corona','V.','1981'),('T','Eclipse','Maurício Klabin','1982'),
('P','Rietveld hanging lamp','Gerrit Rietveld','1920'),('D','Arcobaleno','Marco Zotta','1979'),('T','Bonderup and Thorup table lamps','Claus Bonderup and Torsten Thorup','1979'),
('F','Bonderup and Thorup floor lamp','Claus Bonderup and Torsten Thorup','1978'),('T','Delight','Frans van Nieuwenborg and Martijn Wegman','1978'),('T','Patroclo','Gae Aulenti','1975'),
('W','Ariette','Afra Scarpa and Tobia Scarpa','1973'),('D','Hamburger desk lamp','Peter Hamburger','1972'),('D','Sottsass desk lamp with mobile arm (32 205)','Ettore Sottsass','1972'),
('T','Psycho','Colombini & Guzzetti','1971'),('F','Ponte Arco','Studio AR.DI.TI','1971'),('T','B.T.2','Studio AR.DI.TI and Gianni Gamberini','1971'),('T','Topolino','Joe Colombo','1970'),
('F','Giunone','Vico Magistretti','1969'),('P','VP Globe','Verner Panton','1970'),('T','Light Sticks','Theodore Waddell and Dante Bandini','1970'),('T','Periscopio','Danilo Aroldi and Corrado Aroldi','1968'),
('T','Pillola','Cesare Casati','1968'),('T','Macchi Cassia table lamp (541)','Antonio Macchi Cassia','1968'),('T','Daruma','Sergio Asti','1968'),('T','Crack','Giampiero Bassi and Giovanni Bassi','1968'),
('T','Spring','Joe Colombo','1967'),('F','Tube','Tony Palladino and John Mascheroni','1968'),('T','Asteroid','Ettore Sottsass','1968'),('T','Equilibrium (537)','Vittorio Gregotti, Lodovico Meneghetti and Giotto Stoppino','1967'),
('F','Area (1112)','Neal Small','1966–1967'),('T','Gherpe','Superstudio','1967'),('F','Gregotti floor lamp (1008)','Vittorio Gregotti, Lodovico Meneghetti and Giotto Stoppino','1966'),
('D','Hartman reading lamp','Cedric Hartman','1966'),('T','Sarfatti lamp 600P','Gino Sarfatti','1966'),('F','Small floor lamp (2037)','Neal Small','1966'),('D','Wackerlin desk lamp','Dieter Wackerlin','1966'),
('D','Lytegem','Michael Lax','1965'),('T','Arteluce table lamp 594','Arteluce','1962'),('P','Falkland','Bruno Munari','1964'),('D','Cantilever desk lamp','Gerald Abramovitz','1961-63'),
('T','Vignelli table lamp','Massimo Vignelli','1962'),('F','Fahr floor lamp','Ekkehard Fahr','1960'),('F','Integra','Günther Ssymmank','1960'),('T','Arteluce table lamp 585','Arteluce','1958'),
('F','Bufet floor lamp','Michel Bufet',''),('T','Mayen table lamp','Paul Mayen',''),('T','Sarfatti lamp 566','Gino Sarfatti',''),('T','Sarfatti lamp 571','Gino Sarfatti',''),('F','Mouille floor lamp','Serge Mouille',''),
('C','Wood ceiling lamp','Gross Wood and Esther Wood',''),('T','Burnett three-piece table lamp','Joseph Burnett',''),('T','Gitlin T9','Harry Gitlin','1951'),('T','T-6-G','', '1951'),
('F','Alzabile','Ignazio Gardella','1948'),('T','Noguchi table lamp','Isamu Noguchi','1948'),('C','Versen ceiling lamp 5539','Kurt Versen',''),('D','Desk lamp 114','', '1939'),
('D','Brandt desk lamp 756','Marianne Brandt','c. 1930'),('D','Trabert desk lamp','Karl Trabert',''),('T','Ingolia table lamp','Anthony Ingolia','')]
for t,n,who,y in L: add(t,n,who,y,'M')
add('F','Coupé floor lamp','Joe Colombo','1966','M',mk='Oluce')
# Vitra Design Museum (category Floor lamp 5, Table lamp 8, Pendant lamp 1; keyword "lamp" 28)
V=[('F','Metacrilato','Joe Colombo','1965'),('F','Nuvola','Marcello Pietrantoni and Roberto Lucci','1966'),('F','Mushroom lamp','Verner Panton','1970'),('F','Sciuko','Achille and Pier Giacomo Castiglioni','1966'),
('T','Giant Bulb Opal','Ingo Maurer','1966'),('T','Lucidus Bloc','André Mounique','1944-45'),('T','Vademecum','Joe Colombo','1968'),('T','Topo','Joe Colombo','1970'),('P','Hanging lamp 4005','Achille and Pier Giacomo Castiglioni','1959'),
('F','Bracelli','Salvador Dalí','c. 1937'),('F','Gehry floor lamp','Frank Gehry',''),('T','Horse Lamp','Front','2006'),('P','Lighting Sculpture','Verner Panton','1981'),('F','Luminator (Chiesa)','Pietro Chiesa','1933'),
('T','Shelf lamp','Frank Gehry','1993'),('W','Spiegel lamp','Verner Panton','1968'),('T','Energy Collection','Marjan van Aubel','2012'),('T','w153 île','Inga Sempé','2015')]
for t,n,who,y in V: add(t,n,who,y,'V',mk=('Bayer AG' if n=='Mushroom lamp' else ''))
# V&A (API search "lamp designer", records 1900 onward, pages 1-5 of 6)
A=[('T','Flap Flap Lamp','Büro für Form','1997'),('D','Dell-Lampe Type K','Christian Dell','c. 1929'),('D','Cantilever fluorescent desk lamp 4155','Gerald Abramovitz','1961-63'),('T','Terminus','Martine Bedin','1981'),
('T','Little Sun','Olafur Eliasson','2012'),('D','Oceanic lamp','Michele De Lucchi','1981'),('T','Hugging Lamp','Gitta Gschwendtner','2002'),('T','Double Vision Lamp','Gitta Gschwendtner','2002'),
('T','Sinerpica','Michele De Lucchi','1979'),('F','Standard lamp','Émile-Jacques Ruhlmann','c. 1925'),('T','Unbelievably Modern Lamp','Garry Knox Bennett','1978'),('T','Mayday','Konstantin Grcic','1998-99'),
('T','Cosmolux','Dieter Rams','1964'),('P','Satina','Nigel Chapman','1958'),('T','Hebi','Isao Hosoe','1971'),('T','Bibibibi','Ingo Maurer','1982'),('T','Jack light','Tom Dixon','1996'),
('P','Moth Light','Michael Anastassiades','1998'),('T','Spike Light','Georgia Scott','1998'),('D','Versalite','A. B. Read','1948'),('F','Standard lamp for Edward James','Salvador Dalí','1938'),('T','Cupola','Peter Shire','1988')]
for t,n,who,y in A: add(t,n,who,y,'A')
# ADI Compasso items fetched
S={'ADI-Mix':'https://www.adidesignmuseum.org/en/collection/mix-table-lamp/','ADI-INEI':'https://www.adidesignmuseum.org/en/collection/in-ei-issey-miyake-collection-of-lamps/','ADI-Met':'https://www.adidesignmuseum.org/en/collection/metropoli-series-of-wall-and-ceiling-lamps/'}
def addx(kn,e):
    if not exists(e['n']): kinds[kn].setdefault('x',[]).append(e)
addx('Table lamp',{'n':'Mix','a':'','d':'LED reading lamp by Alberto Meda and Paolo Rizzatto that won the Compasso d\'Oro in 2008; MoMA holds a Mix lamp of 2005.','mk':'Luceplan','y':'2005','s':S['ADI-Mix'],'v':[],'role':'landmark'})
addx('Pendant light',{'n':'IN-EI','a':'','d':'Collection of lamps by Issey Miyake Reality Lab. that won the Compasso d\'Oro in 2014.','mk':'Artemide','y':'2014','s':S['ADI-INEI'],'v':[],'role':'landmark'})
addx('Wall light',{'n':'Metropoli','a':'','d':'Series of wall and ceiling lamps by Paolo Rizzatto and Alberto Meda that won the Compasso d\'Oro in 1994.','mk':'Luceplan','y':'1994','s':S['ADI-Met'],'v':[],'role':'landmark'})
# fixes
t=kinds['Table lamp']; t['x']=[x for x in t['x'] if x['n']!='Coupé' or x.get('s','').startswith('https://www.moma')]
for x in kinds['Desk lamp']['x']:
    if x['n']=='Ascent': x['d']='Table lamp with fixed hinge or base by Daniel Rybakken that won the Compasso d\'Oro in 2016.'; x['s']='https://www.adidesignmuseum.org/en/collection/ascent-table-lamp-with-fixed-hinge-or-with-base/'
for x in kinds['Wall light']['x']:
    if x['n']=='Counterbalance': x['s']='https://www.adidesignmuseum.org/en/collection/counterbalance-lamp/'
def ver(kn,en,vs):
    for x in kinds[kn]['x']:
        if x['n']==en:
            have={norm(v['n']) for v in x['v']}
            for v in vs:
                if norm(v['n']) not in have: x['v'].append(v)
ver('Desk lamp','Anglepoise 1227',[{'n':'Anglepoise 1208/1209','mk':'Herbert Terry & Sons','y':'','d':'listed by the Design Museum'},{'n':'Anglepoise Trade mark 90','mk':'Herbert Terry & Sons','y':'','d':'listed by the Design Museum'},{'n':'Anglepoise 90 PL','mk':'The Anglepoise Co.','y':'','d':'table study lamp'},{'n':'Anglepoise Type 75 revision','mk':'Anglepoise','y':'2004','d':'Kenneth Grange'},{'n':'Anglepoise Type 1228','mk':'Anglepoise','y':'2008','d':'Kenneth Grange'}])
ver('Table lamp','Akari',[{'n':'Akari 2P floor lamp','mk':'Ozeki & Co.','y':'1968','d':'held by MoMA'},{'n':'Akari L2','mk':'Ozeki & Co.','y':'','d':'floor lamp held by MoMA'},{'n':'Akari K4','mk':'Ozeki & Co.','y':'','d':'floor lamp held by MoMA'},{'n':'Akari 21A','mk':'Ozeki & Co.','y':'2016','d':'held by the V&A'},{'n':'Akari 33N','mk':'Ozeki & Co.','y':'1969','d':'held by the V&A'},{'n':'Akari UF3-Q','mk':'Ozeki & Co.','y':'1984','d':'held by the V&A'}])
ver('Table lamp','Wagenfeld lamp',[{'n':'MT8','mk':'','y':'c. 1924','d':'held by the V&A; MoMA holds a 1923-24 table lamp by Wagenfeld and Jucker'}])
ver('Pendant light','Caboche',[{'n':'Caboche Plus','mk':'Foscarini','y':'','d':'listed on the Foscarini brand page'}])
ver('Pendant light','PH lamp',[{'n':'PH 5','mk':'Louis Poulsen','y':'1958','d':'pendant lamp held by MoMA'}])
ver('Pendant light','Flowerpot',[{'n':'Flower Pot table lamp','mk':'','y':'c. 1969','d':'Verner Panton; held by the Vitra Design Museum'}])
for x in kinds['Duty torch']['x']:
    if x['n']=='Maglite D-cell': x['v']+= [{'n':'Maglite 2C','mk':'Maglite','y':'1983','d':'held by the V&A'},{'n':'Maglite 2D','mk':'Maglite','y':'1983','d':'held by the V&A'},{'n':'Maglite 4D','mk':'Maglite','y':'1983','d':'held by the V&A'}]
# restored from m_removed (fetched page names design and designer)
FL='https://www.lights.co.uk/brand/foscarini'; DI='https://designindex.org/index/design/foscarini.html'
addx('Table lamp',{'n':'Lumiere','a':'','d':'Lamp by Rodolfo Dordoni that gave Foscarini its first international attention.','mk':'Foscarini','y':'1990','s':DI,'v':[]})
addx('Table lamp',{'n':'Buds','a':'','d':'Foscarini lamp listed as Buds 2 on the brand page; the page names no designer.','mk':'Foscarini','y':'','s':FL,'v':[]})
addx('Table lamp',{'n':'Bon Jour','a':'','d':'Table lamp by Philippe Starck with a removable crown shade.','mk':'Flos','y':'','s':'https://shop.mohd.it/en/brands/flos/bon-jour.html','v':[{'n':'Bon Jour Unplugged','mk':'Flos','y':'','d':'cordless rechargeable version'},{'n':'Bon Jour Versailles','mk':'Flos','y':'','d':'copper top with transparent crown'}]})
addx('Table lamp',{'n':'Lampadina','a':'','d':'Table and wall lamps by Achille Castiglioni held by MoMA.','mk':'Flos','y':'c. 1971','s':MOMA,'v':[]})
addx('Floor lamp',{'n':'Birdie','a':'','d':'Floor lamp by Ludovica and Roberto Palomba.','mk':'Foscarini','y':'2011','s':DI,'v':[{'n':'Birdie Easy','mk':'Foscarini','y':'','d':'listed on the brand page'}]})
addx('Floor lamp',{'n':'Magneto','a':'','d':'Foscarini lamp listed on the brand page; the page names no designer.','mk':'Foscarini','y':'','s':FL,'v':[]})
addx('Pendant light',{'n':'Gregg','a':'','d':'Lamp by Ludovica and Roberto Palomba.','mk':'Foscarini','y':'2007','s':DI,'v':[]})
addx('Pendant light',{'n':'Aplomb','a':'','d':'Foscarini lamp listed on the brand page; the page names no designer.','mk':'Foscarini','y':'','s':FL,'v':[{'n':'Aplomb Mini','mk':'Foscarini','y':'','d':''},{'n':'Aplomb Large','mk':'Foscarini','y':'','d':''}]})
addx('Pendant light',{'n':'Spokes','a':'','d':'Foscarini lamp listed on the brand page as Spokes 2; the page names no designer.','mk':'Foscarini','y':'','s':FL,'v':[]})
for x in kinds['Floor lamp']['x']:
    if x['n']=='Twiggy' and not any('Wood' in v['n'] for v in x['v']): x['v'].append({'n':'Twiggy Wood','mk':'Foscarini','y':'','d':'listed on the brand page'})
# LIFX
addx('Standard bulb',{'n':'LIFX','a':'','d':'Wi-Fi smart bulb brand that needs no bridge; Feit Electric bought the brand in 2022 after the previous owner went into receivership.','mk':'LIFX','y':'','s':'https://9to5mac.com/2022/08/08/lifx-lives/','v':[],'own':'Feit Electric','own_y':'2022','tier':'Independent'})
# makers' country where a fetched page states it
CTY={'Artemide':'Italy','Louis Poulsen':'Denmark','Fritz Hansen':'Denmark'}
for k in kinds.values():
    for x in k.get('x',[]):
        if x.get('mk') in CTY and 'cty' not in x: x['cty']=CTY[x['mk']]
# regroup
def gof(y):
    mm=re.findall(r'\d{4}',y or '')
    if mm:
        yr=int(mm[0]); return 'Before 1900' if yr<1900 else f'{yr//10*10}s'
    if re.search(r'century|antiquity|Edo|Ottoman|Byzantine|tradition',y or ''): return 'Before 1900'
    return 'Date not stated'
CANON=("Follows design collections and awards on fetched pages: MoMA (Design classification, search \"lamp\": 191 results, all four pages read), the Vitra Design Museum online collection (categories Floor lamp, Table lamp, Pendant lamp and keyword \"lamp\": 28 results), the V&A (lamp records from 1900, pages 1 to 5 of 6 of the museum's search), the Design Museum London (Anglepoise holdings), the ADI Design Museum item pages and the Lightology list of Italian lighting classics; earlier-sourced classics stay. "
 "Covers 191 of 191 MoMA lamp results, 28 of 28 Vitra Design Museum lamp results, about 80 of 97 V&A lamp records from 1900 (page 6 and untitled, stage-design, poster and non-lamp records skipped), and 23 of 41 Lightology lamps (those whose type the page states); Compasso d'Oro: the ADI lighting winners found on the ADI item pages, the Wikipedia and Casa di Luce lists, not the full ADI list, which the museum site does not serve in a fetchable form. MoMA's Product design and Furniture classifications and the Design Museum London's lamps other than Anglepoise were not searched.")
for kn in ['Table lamp','Floor lamp','Desk lamp','Pendant light','Chandelier','Wall light','Flush ceiling light','Lamp shade']:
    k=kinds[kn]
    if 'x' not in k: continue
    k['nl']=k.get('nl') or f"One entry is a {kn.lower()} design with its maker, designer and year; sizes and finishes are versions."
    k['sel']=CANON; k['xg']='Decade of design'
    for x in k['x']: x['g']=gof(x.get('y'))
    k['x'].sort(key=lambda x:(x['g'],x.get('y') or '',x['n']))
tot=sum(len(k.get('x',[])) for k in kinds.values())
# bulbs coverage line update
for kn in ['Standard bulb','Tube light']:
    kinds[kn]['sel']=kinds[kn]['sel'].replace('the LIFX page could not be fetched, so LIFX is not listed.','LIFX is listed from a 9to5mac article because the Wikipedia page returned 404.')
json.dump(d,open(R+'B3.json.tmp','w'),ensure_ascii=False,indent=1); os.replace(R+'B3.json.tmp',R+'B3.json')
print('added',added,'total entries',tot)
