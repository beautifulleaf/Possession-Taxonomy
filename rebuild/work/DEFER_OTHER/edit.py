import json, os, re, sys
OUT='/home/user/Possession-Taxonomy/rebuild/out/'
def load(n): return json.load(open(OUT+n+'.json'))
def save(n,d):
    p=OUT+n+'.json'; t=p+'.tmp'
    json.dump(d,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
def kind(d,i,j,k): return d['depts'][i]['s'][j]['k'][k]
def sep(s): return s if s.endswith('.') else s+'.'
report=[]

# ---------- B10 ----------
d=load('B10'); P='https://www.petfoodindustry.com/'
U1=P+'regions/us-and-canada/article/15752596/46-us-pet-food-companies-revenues-in-2024'
U2=P+'regions/latin-america-carribean/article/15684432/4-top-brazilian-pet-food-companies-revenues-in-2023'
U3=P+'pet-food-market/article/15465258/12-top-companies-in-latin-american-pet-food-industry'
ms=d['depts'][0]['ms']
def M(mkt,who,share,yr,s,note=''): ms.append({'mkt':mkt,'who':who,'share':share,'yr':yr,'s':s,'note':note})
M('United States pet food retail sales','All companies','US$65.8 billion, up 2.1 %',2024,U1,'American Pet Products Association figure as the page states it')
M('United States pet food company sales','J.M. Smucker','US$1.72 billion',2024,U1,'Petfood Industry revenue table')
M('United States pet food company sales','Simmons Pet Food','US$1.3 billion',2024,U1,'Petfood Industry revenue table; independent')
M('United States pet food company sales','Sunshine Mills','US$525 million',2024,U1,'Petfood Industry revenue table; independent')
M('United States pet food company sales','Tuffy\'s Pet Foods','US$415 million',2024,U1,'Petfood Industry revenue table; independent')
M('Brazil pet food company revenue','BRF Pet SA','US$578 million',2024,U2,'largest Brazilian pet food company; bought Hercosul and Mogiana in 2021 for R$1.35 billion')
M('Brazil pet food company revenue','Special Dog','US$370 million',2024,U2,'Brazilian independent, founded February 2001')
M('Brazil pet food company revenue','Premier Pet (Grandfood Industry and Trade)','US$200 million',2024,U2,'national champion in premium dog and cat food')
M('Brazil pet food company revenue','Total Alimentos (ADM Animal Nutrition)','US$190 million',2024,U2,'owned by ADM Animal Nutrition')
M('Brazil pet food market','All companies','US$9.37 billion expected',2024,U2,'Mordor Intelligence forecast as the page states it; largest in South America')
M('Argentina pet food','Grupo Pilar (Gepsa)','20 % share, behind Nestlé and Mars',2018,U3,'page lists Gepsa as the largest branded animal nutrition player in Argentina')
M('Chile pet food','NutriPro (Empresas Carozzi)','31 % share',2018,U3,'NutriPro is the leading Chilean pet food maker; Carozzi bought SoinPro in 2011')
M('Mexico pet food','Malta Texo de Mexico (Neovia)','third-largest producer',2018,U3,'')
save('B10',d)
b=load('B10_brands'); have={x['n'] for x in b['b']}
def BR(n,c,d_,s,kf,seg='Mainstream',f=None):
    if n in have: return
    e={'n':n,'c':c,'seg':seg,'d':d_,'s':s,'kf':kf}
    if f: e['f']=f
    b['b'].append(e); have.add(n)
BR('Special Dog','Brazil','Brazilian dog and cat food maker based in Santa Cruz do Rio Pardo, São Paulo, launched in February 2001.',U2,'dog and cat food',f='2001')
BR('Premier Pet','Brazil','Brazilian premium dog and cat food maker owned by Grandfood Industry and Trade; brands PremieR and Golden.',U2,'dog and cat food')
BR('BRF Pet','Brazil','Brazil\'s largest pet food company; entered in 2021 by buying Hercosul and Mogiana (Guabi).',U2,'dog and cat food')
BR('Total Alimentos','Brazil','Brazilian pet food maker owned by ADM Animal Nutrition with many own-label partnerships.',U2,'dog and cat food')
BR('Gepsa','Argentina','Pet food and feed division of Grupo Pilar, the largest branded animal nutrition player in Argentina.',U3,'dog and cat food')
BR('NutriPro','Chile','Leading Chilean pet food maker, part of Empresas Carozzi since the 2011 purchase of SoinPro.',U3,'dog and cat food')
BR('Simmons Pet Food','United States','Arkansas-based independent pet food maker with US$1.3 billion revenue in 2024.',U1,'dog and cat food',seg='Mainstream')
BR('Sunshine Mills','United States','American independent pet food maker with US$525 million revenue in 2024.',U1,'dog and cat food')
BR("Tuffy's Pet Foods",'United States','American independent pet food maker with US$415 million revenue in 2024.',U1,'dog and cat food')
save('B10_brands',b)
report.append('B10: all 3 pages read; 13 market facts added to Dogs (US, Brazil, Argentina, Chile, Mexico) and 9 brands to register.')

# ---------- C2 ----------
d=load('C2'); b=load('C2_brands')
for x in b['b']:
    if x['n']=='Recteq':
        x['d']='Maker of wood-pellet grills with Wi-Fi controllers, including the Bullseye Deluxe. Co-founded in 2009 by Ron Cundy and Ray Carnes in Augusta, Georgia; Norwest Equity Partners made a significant investment in 2021.'
        x['s']='https://www.businesswire.com/news/home/20210201005177/en/Leading-Pellet-Grill-Company-recteq-Expands-Consumer-Products-Portfolio-at-Norwest-Equity-Partners'
    if x['n']=='Komodo Kamado':
        x['d']='Maker of insulated, tiled kamado grills, designed by Dennis Linkletter, who runs a teak furniture factory in Indonesia; the 32 in Big Bad is its flagship. Sold direct.'
        x['s']='https://amazingribs.com/manufacturer/komodo-kamado/'
save('C2_brands',b)
k=kind(d,10,0,5)
for e in k['x']:
    if e['n']=='Recteq Bullseye Deluxe':
        e['d']=e['d']+' Recteq was co-founded in 2009 by Ron Cundy and Ray Carnes.'
k=kind(d,10,0,1)
for e in k['x']:
    if e['n']=='Komodo Kamado Big Bad':
        e['d']=e['d']+' Designed by Dennis Linkletter and sold direct.'
save('C2',d)
report.append('C2: done. Recteq founders (2009) and Norwest investment (2021) confirmed; Komodo Kamado designer and direct sales added; no owner company is stated for Komodo.')

# ---------- C4 ----------
b=load('C4_brands')
for x in b['b']:
    if x['n']=='Holbein':
        x['d']="Japanese maker of artists' colours, pencils and mediums, established in Osaka in the early 20th century; Artists' Watercolor dates from the early 1920s."
        x['s']='https://www.jacksonsart.com/en-us/brands/holbein'
save('C4_brands',b)
report.append('C4: done for Holbein (Osaka, early 20th century, watercolour early 1920s); the page names no owner.')

# ---------- D2 ----------
d=load('D2')
S1='https://appleinsider.com/articles/26/01/12/apple-dominated-2025-smartphone-market-with-a-20-share'
S2='https://www.sammyfans.com/2025/12/20/samsung-wearable-competitors-grew-sharply-in-2025/amp/'
d['depts'][0]['ms'].append({'mkt':'Global smartphones, full year','who':'Apple','share':'20 % share, up from 18 % in 2024','yr':2025,'s':S1,'note':'Counterpoint Research as AppleInsider reports it'})
w=d['depts'][2]['ms']
w.append({'mkt':'Global smartwatches and fitness trackers, first three quarters','who':'All vendors','share':'over 150 million units, up 10 %','yr':2025,'s':S2,'note':'IDC as Sammy Fans reports it'})
w.append({'mkt':'Global smartwatches and fitness trackers, first three quarters','who':'Apple','share':'27.9 million units, up 23.9 %','yr':2025,'s':S2,'note':'third place; share figure missing from the page'})
w.append({'mkt':'Global smartwatches and fitness trackers, first three quarters','who':'Samsung','share':'7.6 % share, 11.8 million units','yr':2025,'s':S2,'note':'fourth place, growth 1.5 %'})
save('D2',d)
report.append('D2: both pages read; Apple 20 % (2025 smartphones) and IDC Q1-Q3 2025 wearables added. The smartphone page gives only Apple\'s share in the excerpt; other vendors not stated.')

# ---------- E2 ----------
d=load('E2'); CS='https://coloradosun.com/2021/08/31/big-agnes-steamboat-gamber-colorado-outdoor-industry/'
n=0
def walk(o):
    global n
    if isinstance(o,dict):
        if o.get('mk')=='Big Agnes' and 'own' not in o:
            o['own']='Big Agnes (co-owned by founder Bill Gamber)'; o['tier']='Independent'; o['cty']='United States'; n+=1
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk(d); save('E2',d)
b=load('E2_brands')
for x in b['b']:
    if x['n']=='Big Agnes':
        x['d']='Steamboat Springs, Colorado maker of backpacking tents, bags and mats; founder Bill Gamber is co-owner and president.'; x['s']=CS; x['c']='United States'
save('E2_brands',b)
report.append(f'E2: Big Agnes done ({n} entries marked Independent, co-owned by founder Bill Gamber; no outside owner stated, founding year not on the fetched page). Winning still blocked: shop page returned only a footer.')

# ---------- E3 ----------
d=load('E3'); AM='https://www.americanmusical.com/c/brands/mesa-boogie/mesa-boogie-heads'
k=kind(d,2,0,1)
G='United States · Mesa/Boogie'
def head(n,a,desc,v):
    return {'n':n,'a':a,'d':desc,'mk':'Mesa/Boogie','y':'','s':AM,'v':[{'n':x,'mk':'Mesa/Boogie','y':'','d':y} for x,y in v],'g':G}
names={e['n'] for e in k['x']}
new=[head('Mesa/Boogie Mark Five','Mark V','Two-channel, six-mode Mark head sold in a 35 W version.',[('Mark Five 35','10/25/35 W')]),
 head('Mesa/Boogie Mark IIC+','Mark II C Plus','Vintage Boogie head based on the original Mark II dual-mode design.',[('Mark IIC+ HRG','60/100 W, reverb and graphic EQ')]),
 head('Mesa/Boogie Triple Rectifier','','Three-channel high-gain Rectifier head, listed as a 90s reissue.',[('90s Triple Rectifier Standard','150 W'),('90s Triple Rectifier Solo','150 W')]),
 head('Mesa/Boogie Badlander','','Rectifier-family head with tighter low end and less mid scoop than the Dual Rectifier.',[('Badlander 25','10/25 W'),('Badlander 100','100 W')]),
 head('Mesa/Boogie California Tweed','','Vintage-voiced 6V6 head.',[('California Tweed 6V6 4:40','2/40 W')]),
 head('Mesa/Boogie Fillmore','','Vintage-styled head from the other branch of the Boogie family tree.',[('Fillmore 50','40/60 W')]),
 head('Mesa/Boogie JP-2C','','John Petrucci signature head, the maker\'s first unlimited-build signature model.',[])]
for e in new:
    if e['n'] not in names: k['x'].append(e)
for e in k['x']:
    if e['n']=='Mesa/Boogie Mark VII':
        e['s']=e['s'] or AM
        if not e.get('v'): e['v']=[{'n':'Mark VII rackmount','mk':'Mesa/Boogie','y':'','d':'25/45/90 W'},{'n':'Mark VII 6L6/EL34','mk':'Mesa/Boogie','y':'','d':'25/45/90 W'}]
    if e['n']=='Mesa/Boogie Dual Rectifier' and not e.get('v'):
        e['v']=[{'n':'90s Dual Rectifier','mk':'Mesa/Boogie','y':'1992','d':'100 W; the retailer says the model was released in 1992'}]
k['sel']=sep(k['sel'].rstrip())+' Mesa/Boogie head list read from the American Musical Supply category (17 items: Mark, Rectifier, Badlander, California Tweed, Fillmore and JP-2C lines).'
k1=kind(d,0,0,0)
k1['sel']=sep(k1['sel'].rstrip())+' Jackson (18 models of the 2021 list on Wikipedia, plus the minor models) and ESP lines were re-read from Wikipedia and Reverb on 2026-10-31; all are held.'
save('E3',d)
b=load('E3_brands')
for x in b['b']:
    if x['n']=='Jackson':
        x['d']='Metal-guitar maker founded in 1980 in Glendora, California by Grover Jackson, maker of the Soloist, King V and Rhoads; Fender is the parent.'; x['s']='https://en.wikipedia.org/wiki/Jackson_Guitars'
    if x['n']=='ESP':
        x['d']='Tokyo maker founded in 1975 by Hisatake Shibuya as Electric Sound Products; the lower-priced LTD line followed in 1996.'; x['s']='https://reverb.com/news/a-brief-history-of-esp-guitars-from-replacement-to-refinement'
save('E3_brands',b)
report.append('E3: Mesa/Boogie 17-item head list read; 7 head lines added with versions. Jackson and ESP model lists re-read and already complete; brand facts updated. (Note: Reverb dates LTD to 1996, the entry says 1995.)')

# ---------- E4 ----------
d=load('E4'); k=kind(d,5,0,3); PY='https://www.pyramydair.com/product/barra-270z-pcp-air-rifle?m=7107'
if not any(e['n']=='Barra 270z' for e in k['x']):
    k['x'].append({'n':'Barra 270z','a':'','d':'Bolt-action pre-charged pneumatic repeater with a 322 cc over-the-barrel reservoir, external regulator and beech stock; .22 and .25.','mk':'Barra','y':'','s':PY,'v':[{'n':'.22','mk':'Barra','y':'','d':'10-round magazine, up to 1100 fps'},{'n':'.25','mk':'Barra','y':'','d':'9-round magazine, up to 1000 fps'}],'dt':'calibre'})
save('E4',d)
b=load('E4_brands')
if not any(x['n']=='Barra' for x in b['b']):
    b['b'].append({'n':'Barra','seg':'Mainstream','d':'Airgun maker of airsoft guns, BB guns and PCP air rifles, with the first mass-market full-auto BB rifle powered by a lithium battery.','s':PY,'kf':'air rifles'})
save('E4_brands',b)
report.append('E4: Barra 270z confirmed as PCP and added with its two calibres; Barra added to register.')

# ---------- E5 ----------
d=load('E5'); k=kind(d,7,2,0) if False else None
for i,dp in enumerate(d['depts']):
    for j,s in enumerate(dp.get('s',[])):
        for kk in s.get('k',[]):
            if kk['n']=='Arcade system board': k=kk
TA='https://emulation.gametechwiki.com/index.php/Taito'; CA='https://emulation.gametechwiki.com/index.php/Capcom'
names={e['n'] for e in k['x']}
def board(n,mk,y,desc,s,v=()):
    return {'n':n,'a':'','d':desc,'mk':mk,'y':y,'s':s,'v':[{'n':a,'mk':mk,'y':b_,'d':''} for a,b_ in v],'g':mk,'dt':''}
add=[board('Taito SJ System','Taito','1981','Taito board listed for 1981 to 1984 on the Emulation General Wiki.',TA),
 board('Taito Air System','Taito','1987','Taito board listed for 1987 to 1990.',TA),
 board('Taito Z System','Taito','1987','Taito board listed for 1987 to 1994, with the SZ System / 68020 from 1992.',TA,[('Z System','1987'),('SZ System / 68020','1992')]),
 board('Taito B System','Taito','1988','Taito board listed for 1988 to 1994.',TA),
 board('Taito F2 System','Taito','1988','Taito board listed for 1988 to 1994.',TA),
 board('Taito F1 System','Taito','1989','Taito board listed for 1989 to 1992.',TA),
 board('Taito H System','Taito','1988','Taito board listed for 1988 to 1989.',TA),
 board('Taito L System','Taito','1988','Taito board listed for 1988 to 1993.',TA),
 board('Taito X System','Taito','1988','Taito board listed for 1988 to 1992.',TA),
 board('Taito JC System','Taito','1995','Taito board listed for 1995 to 1998, with a PowerPC version in 1998.',TA,[('JC System','1995'),('PPC JC System','1998')]),
 board('Taito FX System','Taito','1995','PlayStation-based Taito boards listed for 1995 to 1997.',TA,[('FX-1A System','1995'),('FX-1B System','1996')]),
 board('Taito G-Net System','Taito','1998','PlayStation-based Taito board listed for 1998 to 2005.',TA),
 board('Taito Wolf System','Taito','1997','Taito board listed for 1997 to 1998.',TA),
 board('Taito Type Zero','Taito','1998','Taito board listed for 1998 to 2002.',TA),
 board('Capcom ZN','Capcom','1995','Capcom PlayStation-based boards listed for 1995 to 2000.',CA,[('ZN-1','1995'),('ZN-2','1997')])]
c=0
for e in add:
    if e['n'] not in names: k['x'].append(e); c+=1
k['sel']=sep(k['sel'].rstrip())+f' Taito and Capcom board lists on the Emulation General Wiki were read; {c} boards were added (years are the start of the listed range). arcadecontrols.com redirects to an emulator list with no boards. Atari, Irem, Data East, Cave and Konami later boards remain without a list.'
save('E5',d)
report.append(f'E5: Taito and Capcom pages read, {c} boards added; the arcadecontrols page is an emulator list only, so no all-maker board list was found.')

# ---------- E6 ----------
d=load('E6'); k=kind(d,0,2,0); SK='https://skiesandscopes.com/smart-telescopes'
for e in k['x']:
    if e['n']=='DWARF' and not any(v['n']=='DWARF 2' for v in e['v']):
        e['v'].insert(0,{'n':'DWARF 2','mk':'DwarfLab','y':'','d':'named as the predecessor of the Dwarf 3 on skiesandscopes.com'})
k['sel']="Smart telescopes named in Wikipedia's Robotic telescope and Unistellar articles and on the skiesandscopes.com index of models (Dwarf 2 and 3, Seestar S30, S50 and S50 Pro, Unistellar eVscope 2, Equinox 2, Odyssey and Odyssey Pro), which was read on 2026-10-31. No complete list exists; the index also holds a section of older and discontinued models that gave no names in the excerpt."
save('E6',d)
report.append('E6: skiesandscopes index read; Dwarf 2 added; all other listed models already held.')

# ---------- F3 ----------
d=load('F3'); k=kind(d,6,0,2); DD='https://prhome.defense.gov/Portals/52/Documents/RFM/MPP/OEPM/docs/US%20Awards%20Prior%20to%201960%20-%202014%2001%2003.pdf'
years={'American Campaign Medal':'1942','Asiatic-Pacific Campaign Medal':'1942','European-African-Middle Eastern Campaign Medal':'1942','Army of Occupation Medal':'1946','Mexican Border Service Medal':'1918','Philippine Campaign Medal':'1905'}
for e in k['x']:
    if e['n'] in years and not e.get('y'): e['y']=years[e['n']]
names={e['n'] for e in k['x']}
def med(n,y,desc): return {'n':n,'a':'','d':desc,'mk':'','y':y,'s':DD,'v':[],'g':'United States'}
add=[med('Army of Cuban Pacification Medal','1909','Army medal for service in Cuba between 6 October 1906 and 1 April 1909.'),
 med('Brevet Medal','1921','Marine Corps medal for distinguished service in the presence of the enemy in wars from the Mexican War to the Boxer Rebellion.'),
 med('Byrd Antarctic Expedition Medal','1936','Medal for members of the Second Byrd Antarctic Expedition who wintered at Little America or commanded its ships, 1933 to 1935.'),
 med('Cardenas Medal of Honor','1900','Coast Guard medal for the crew of the revenue cutter Hudson at Cardenas Harbor in the Spanish-American War.'),
 med('China Service Medal','','Navy medal for service in China.'),
 med('Dewey Medal','1898','Medal for crews of the ships at the Battle of Manila Bay on 1 May 1898, also called the Manila Bay Medal.'),
 med('Naval Reserve Medal','1938','Navy medal for each ten years of honourable service in the Naval Reserve before 12 September 1958.'),
 med('Navy Occupation Service Medal','1947','Navy medal for service in occupied territories after the Second World War.'),
 med('NC-4 Medal','1929','Navy medal created by Congress for the seven crew of the NC-4 flying boat on the first transatlantic flight in May 1919.'),
 med('Peary Polar Expedition Medal','','Medal for members of the 1908 to 1909 Peary Polar Expedition.'),
 med('Spanish War Service Medal','1918','Army medal for service between 20 April 1898 and 11 April 1899 by those not eligible for the Spanish Campaign Medal.'),
 med('Specially Meritorious Medal','1901','Navy medal for meritorious non-combat service during the war with Spain.'),
 med('United States Antarctic Expedition Medal','1945','Medal for members of the 1939 to 1941 Antarctic expedition.'),
 med('Women\'s Army Corps Service Medal','','Army medal for service in the Women\'s Army Auxiliary Corps and Women\'s Army Corps, 1942 to 1945.'),
 med('Yangtze Service Medal','1930','Navy medal for operations in the Yangtze River valley in 1926 to 1927 and 1930 to 1932.')]
c=0
for e in add:
    if e['n'] not in names: k['x'].append(e); c+=1
k['sel']=sep(k['sel'].rstrip())+f' The Department of Defense list of US awards before 1960 (45 awards) was read in full on 2026-10-31: {c} missing campaign and service medals were added and blank years filled. Medal of Freedom, Medal for Merit and Medal for Humane Action are decorations, not campaign medals, and are held elsewhere or not at all.'
save('F3',d)
report.append(f'F3: DoD pre-1960 list read; {c} medals added, years filled for 6. Decorations (Medal of Freedom, Merit, Humane Action) left out as out of kind.')

# ---------- F4 ----------
d=load('F4'); k=kind(d,2,2,5); PO='https://kolekcje.polin.pl/en/torah-mantle-meil'
if not any('Leszno' in e['n'] for e in k['x']):
    k['x'].append({'n':'Leszno Torah mantle','a':'me\'il','d':'Honey-coloured velvet mantle from near Łódź with gold edging and fringes, embroidered with the tablets, two lions, a crown and the donors Abraham and Chana Rosenbaum.','mk':'','y':'first half of the 20th century','s':PO,'dt':'velvet · embroidery','v':[]})
k['sel']='No complete list exists. Follows the Jewish Museum (New York) record of one mantle and the POLIN Museum record of the mantle held by the Local Museum in Leszno. Covers 2 pieces.'
save('F4',d)
report.append('F4: POLIN page read; Leszno mantle added (first half of the 20th century, bought 2008).')

# ---------- C1 ----------
d=load('C1'); k=kind(d,1,0,0); LV='https://www.leevalley.com/en-ca/shop/tools/hand-tools/planes/bevel-up/49708-veritas-low-angle-jack-plane'
for e in k['x']:
    if e['n']=='Stanley No. 62' and not any('Veritas' in v['n'] for v in e['v']):
        e['v'].append({'n':'Veritas Low-Angle Jack Plane','mk':'Veritas','y':'','d':'Lee Valley\'s 62½: bevel-up, 12° bed, 15 in long, ductile cast iron, made in Canada'})
        e['s']=e['s']
k['sel']=sep(k['sel'].rstrip())+' The Veritas Low-Angle Jack Plane is added as a version of No. 62 because Lee Valley designates it a 62½; the other Veritas plane pages were not reached.'
save('C1',d)
b=load('C1_brands')
report.append('C1: Lee Valley low-angle jack page read; Veritas 62½ added as a version of Stanley No. 62. Other Veritas category pages still not fetched.')

# ---------- C5 ----------
d=load('C5'); k=kind(d,1,2,0); BW='https://blackwing602.com/pages/volumes-pencil-guide'
vol=[('725','Newport Folk Festival','2015','Balanced','July 2015'),('211','John Muir','2015','Firm','September 2015'),('1138','A Trip to the Moon','2015','Soft','December 2015'),
('24','John Steinbeck','2016','Extra-firm','March 2016'),('56','Joe DiMaggio','2016','Firm','July 2016'),('344','Dorothea Lange','2016','Firm','September 2016'),('530','California Gold Rush','2016','Extra-firm','December 2016'),
('205','The Silk Road','2017','Firm','March 2017'),('73','Lake Tahoe','2017','Soft','June 2017'),('1','Guy Clark','2017','Balanced','September 2017'),('16.2','Ada Lovelace','2017','Firm','December 2017'),
('54','Surrealism','2018','Extra-firm','March 2018'),('33 1/3','Vinyl records','2018','Balanced','September 2018'),('4','Perseverance Mars rover mission','2018','Soft','December 2018'),
('811','Libraries','2019','Firm','March 2019'),('10','Nellie Bly','2019','Extra-firm','June 2019'),('42','Jackie Robinson','2019','Balanced','August 2019'),('155','Bauhaus','2019','Soft','November 2019'),
('840','Duke Kahanamoku','2020','Balanced','March 2020'),('3','Ravi Shankar','2020','Extra-firm','June 2020'),('XIX','The 19th Amendment','2020','Firm','September 2020'),('6','Independent businesses','2020','Soft','December 2020'),
('223','Woody Guthrie','2021','Balanced','March 2021'),('64','Comic books','2021','Firm','June 2021'),('651','Bruce Lee','2021','Extra-firm','September 2021'),('93','Corita Kent','2021','Soft','December 2021'),
('200','Coffeehouses','2022','Firm','March 2022'),('55','The Golden Ratio','2022','Balanced','June 2022'),('7','Animation','2022','Balanced','September 2022'),('192','John Lennon and Paul McCartney','2022','Extra-firm','December 2022'),
('20','Tabletop games','2023','Firm','March 2023'),('57','Jean-Michel Basquiat','2023','Soft','June 2023'),('17','Gardening','2023','Balanced','September 2023'),('2','Art and change','2023','2X firm','December 2023'),
('710','Jerry Garcia','2024','Soft','March 2024'),('746','The Golden Gate Bridge','2024','Firm','June 2024'),('71','Frank Lloyd Wright','2024','Extra-firm','September 2024'),
('11','Bill Russell','2025','Soft','February 2025'),('140','Culinary arts','2025','Balanced','May 2025')]
if not any(e['n']=='Blackwing Volumes' for e in k['x']):
    k['x'].append({'n':'Blackwing Volumes','a':'','d':'Quarterly limited-edition Blackwing pencils, each numbered for a person, place or subject, begun in 2015.','mk':'Blackwing','y':'2015','s':BW,'v':[{'n':f'Blackwing {a} ({b_})','mk':'Blackwing','y':c_,'d':f'{g} graphite, {r}'} for a,b_,c_,g,r in vol],'g':'United States','dt':'graphite grade · subject','cty':'United States'})
k['sel']=sep(k['sel'].rstrip())+' The Blackwing Volumes archive (2015 to May 2025) was read; two releases with no details on the page (Volume 10001 of 2018 and Volume 574 of 2024) are not listed.'
save('C5',d)
report.append('C5: Blackwing Volumes archive read (38 releases added as versions). Platinum guide, Koh-i-Noor, Midori and Noodler\'s list pages: search found no fetchable range pages (retailer snippets only); still blocked.')
open('/home/user/Possession-Taxonomy/rebuild/work/DEFER_OTHER/report_lines.txt','w').write('\n'.join(report))
print('\n'.join(report))
