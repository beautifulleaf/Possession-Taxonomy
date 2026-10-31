import json,copy
P='/home/user/Possession-Taxonomy/rebuild/out/F3.json'
d=json.load(open('/home/user/Possession-Taxonomy/rebuild/work/FIX_F3/bak/F3.json'))
W='https://en.wikipedia.org/wiki/'
def A(n,d_,mk,y,s,v=(),dt='',a=''):
    return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":[{"n":x[0],"mk":x[1],"y":x[2],"d":x[3]} for x in v],**({"dt":dt} if dt else {})}
K={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
def addt(k,*ts):
    k.setdefault('t',[])
    for t in ts:
        if t not in k['t']: k['t'].append(t)
# F3-1
c=K['Circulation coin']['x']
c+=[
A("Euro definitive coins","Eight common-reverse coins of the euro area, each with a national obverse chosen by the issuing state.","", "2002",W+"Euro_coins",
  [("Common side","","2002","value, twelve stars and map of Europe by Luc Luycx"),("National sides","","2002","design chosen by each eurozone country")],"1 cent to 2 euro · issuing state on obverse"),
A("British pre-decimal silver","Crown, half crown, florin, shilling, sixpence and threepence struck in silver until decimalisation in 1971.","Royal Mint","to 1946",W+"Coins_of_the_pound_sterling",
  [("Sterling silver","Royal Mint","to 1920","925 fine"),("Debased silver","Royal Mint","1920–1946","500 fine"),("Cupronickel","Royal Mint","from 1947","no silver"),("Silver threepence","Royal Mint","to 1945","the twelve-sided 1937 threepence is nickel-brass")],"denomination · monarch · fineness by date"),
A("French Semeuse","Oscar Roty's Sower design for French silver coins, struck from 1897 and reused on later francs and euro cents.","Monnaie de Paris","1897",W+"Semeuse",
  [("50 centimes","Monnaie de Paris","1897","first Semeuse coin"),("Silver issues","Monnaie de Paris","to 1920","silver coins ended 1920"),("New franc","Monnaie de Paris","1960–2001","design reused on the 1 franc"),("Euro cents","Monnaie de Paris","2002","modernised by Laurent Jorio on 10, 20 and 50 cent")],"denomination · date · metal"),
A("Deutsche Mark coins","Coins of the West German mark, from 1 pfennig to 5 marks, issued from 1948 until the euro.","", "1948",W+"Deutsche_Mark",
  [("1 pfennig","","","rye stalks and oak branch"),("50 pfennig","","","sower with oak seedling"),("1 mark","","","oak leaves and Bundesadler"),("Commemorative 10 mark","","","silver")],"denomination · mint mark · year"),
A("Swiss Helvetia coins","Swiss franc coins with the seated Helvetia and a ring of stars, designed by Albert Walch.","Swissmint","1968",W+"Swiss_franc",
  [("22 stars","Swissmint","1968–1982","ring of 22 stars"),("23 stars","Swissmint","1983–","23 after Jura became a canton"),("1850 silver francs","Swissmint","1850","0.900 fine, later 0.835")],"denomination · star count · year"),
A("Indian rupee coins","Coins of independent India, from the 1950 anna series to the decimal paise and rupee coins.","", "1950",W+"Indian_rupee",
  [("Anna series","","1950","pice, annas and half-rupee, close to the last regal issues"),("Naye paise","","1957","decimal series; 'naye' dropped in 1964"),("Aluminium coins","","1964","up to 20 paise"),("Stainless steel","","1988–","also lighter ferritic steel 2005–2008")],"denomination · metal · emblem and motif"),
A("Canadian decimal coins","Royal Canadian Mint coins with the monarch's effigy and animal and ship reverses, including the loonie and toonie.","Royal Canadian Mint","1858",W+"Coins_of_the_Canadian_dollar",
  [("Loonie","Royal Canadian Mint","1987","$1, loon reverse"),("Toonie","Royal Canadian Mint","1996","$2, bimetallic, polar bear"),("Bluenose dime","Royal Canadian Mint","","Emanuel Hahn design"),("Penny","Royal Canadian Mint","to 2012","production stopped May 2012")],"denomination · effigy · year"),
A("Australian decimal coins","Coins introduced at decimalisation on 14 February 1966, with the $1 and $2 added in 1984 and 1988.","", "1966",W+"Coins_of_the_Australian_dollar",
  [("12-sided 50 cent","","1969","round original lasted one year"),("$1 coin","","1984","replaced the banknote"),("$2 coin","","1988","replaced the banknote"),("1 and 2 cent","","1966–1991","withdrawn from 1992")],"denomination · effigy · year"),
A("Japanese yen coins","Six circulating Japanese denominations dated by the emperor's regnal year, with no imperial portrait.","Japan Mint","1871",W+"Japanese_yen",
  [("500 yen cupronickel","Japan Mint","1982",""),("500 yen nickel-brass","Japan Mint","2000","after counterfeiting"),("500 yen bimetallic","Japan Mint","2021","extra security features")],"denomination · era year (Shōwa, Heisei, Reiwa)"),
]
e=K['Mint error coin']['x']
e+=[
A("1983 'New Pence' two pence","British 2p struck with the old 'NEW PENCE' reverse after the legend changed to 'TWO PENCE'.","Royal Mint","1983",W+"Error_coin",[],"obverse and reverse mismatch"),
A("2008 dateless twenty pence mule","British 20p mule pairing the 1982–2008 obverse with the 2008 reverse; neither bears a date.","Royal Mint","2008",W+"Error_coin",[],"no date"),
A("2013 James Joyce €10 coin","Irish silver €10 coin that misquoted a line from Ulysses.","","2013",W+"Error_coin",[],"die-setting error"),
A("2000 Australian dollar and ten cent mule","Australian mule coin struck with mismatched $1 and 10-cent dies.","","2000",W+"Error_coin",[],"mismatched dies"),
]
# F3-2 cards
base=K['Base card']['x']
base+=[
A("Topps Chrome Formula 1","Topps's flagship F1 chrome set, launched in 2020 under the Topps–Formula 1 licence.","Topps","2020","https://www.formula1.com/en/latest/article.formula-1-and-topps-sign-exclusive-global-licence-for-collectible-cards-and.58QfpRAAP8g4FM9yEUmZra.html",[("Topps Dynasty F1","Topps","2020","premium set with autographs and race-worn suit pieces"),("F1 Topps NOW","Topps","2020","print-on-demand cards")],"card number · parallel · serial number · grade"),
A("Topps UEFA Champions League","Topps cards and stickers for the UEFA Champions League, issued since 2015.","Topps","2015",W+"Topps",[("Match Attax","Topps","to 2019","Premier League card game")],"card number · parallel"),
A("Donruss (Panini)","Donruss football and other sports sets, run by Panini since it acquired the brand and its NFL and NFLPA licences in 2009.","Panini","2009",W+"Panini_Group",[],"card number · parallel · serial number"),
A("Leaf Metal Authentics","Leaf's metal-card line built on on-card autographs.","Leaf","2010",W+"Leaf_Trading_Cards",[("Leaf Photographic","Leaf","","each card carries a signed Polaroid")],"card number · autograph · serial number"),
]
K['Rookie card']['x'].append(A("Upper Deck Young Guns","Upper Deck's rookie subset, introduced in its 1990–91 hockey set of 550 cards in Low and High series.","Upper Deck","1990",W+"Upper_Deck_Company",[("Low Series #1–400","Upper Deck","1990",""),("High Series #401–550","Upper Deck","1990","")],"card number · series · grade"))
ins=K['Insert card']
ins['x']=[A("Topps Chrome baseball inserts","Insert subsets of a Topps Chrome baseball set, pulled at lower rates than the base cards.","Topps","2026",ins['s'],[(n,'Topps','','') for n,_ in ins.pop('m')],"insert set · parallel")]
au=K['Autograph card']
au['x'].append(A("Topps Chrome autograph sets","Autograph subsets within a Topps Chrome set, signed by rookies and legends.","Topps","",ins['s'],[(n,'Topps','','') for n,_ in au.pop('m')],"on-card or sticker · serial number"))
K['Collectible sticker']['x'].append(A("Panini FIFA World Cup sticker album","Panini's World Cup sticker albums, first published for the 1970 tournament in Mexico.","Panini","1970",W+"Panini_Group",[("2010","Panini","2010",""),("2018","Panini","2018","")],"edition · tournament year · sticker number"))
# box card -> type
addt(K['Base card'],'box card (hand-cut)')
# F3-3
addt(K['Love token and counterstamped coin'],'hobo nickel')
K['Love token and counterstamped coin']['x'].append(A("Hobo nickel","Nickel carved into a small relief portrait, mainly from Buffalo nickels, from 1913.","", "1913",W+"Hobo_nickel",[("Bertram Wiegand","","","carver from the 1910s"),("George 'Bo' Hughes","","","carved from the late 1910s to 1981"),("Ron Landis","","","from about 1995")],"base coin · carver · era (classic to 1940)"))
# F3-4
def popk(n):
    for dp in d['depts']:
        for s in dp['s']:
            for i,k in enumerate(s['k']):
                if k['n']==n: return s['k'].pop(i)
fdc=K['First-day cover']; addt(fdc,'maximum card (maxicard)','philatelic numismatic cover (PNC)')
fdc['d']=fdc['d']+" Maximum cards (matching stamp, picture and postmark) are a type."
popk('Maximum card'); popk('Philatelic numismatic cover'); popk('Box card')
# trophies
tr=[popk(n) for n in ['Trophy cup','Upright award','Award plaque or shield','Bowl, tankard or salver','Rosette or ribbon']]
trophy={"n":"Trophy or award","a":"cup · plaque · shield · rosette","d":"Object given as a prize or recognition: cup, upright award, plaque or shield, bowl, tankard or salver, rosette.","s":tr[0]['s'],"t":["trophy cup","perpetual cup","upright award (column, figure, star, obelisk)","plaque","shield","bowl","tankard","salver","rosette","award ribbon"]}
belt=K['Championship belt']; ring=K['Championship ring']
ring['x']=[
A("Super Bowl ring","NFL championship ring; the league pays up to $5,000 for up to 150 rings per winning team.","", "",W+"Championship_ring",[],"design chosen by winning team"),
A("NBA championship ring","Ring given to NBA title winners; design standardised 1969–1983, now chosen by the winning team.","", "",W+"Championship_ring",[],"design · gold weight · stones"),
A("World Series ring","MLB title ring, given to winners since 1932.","", "1932",W+"Championship_ring",[],"design · stones"),
A("Stanley Cup ring","NHL title ring, first ordered by the Montreal Hockey Club after its 1893 Stanley Cup win.","", "1893",W+"Championship_ring",[],"design · stones"),
A("Fan replica ring","Inexpensive replica of a championship ring sold or given to fans, such as 20,000 Toronto Raptors rings in 2019.","", "2019",W+"Championship_ring",[],"replica · giveaway")]
ring['t']=['team ring','replica ring']
belt['x']=[
A("Tom Cribb belt","Belt given in 1810 by King George III to boxer Tom Cribb, the first for in-ring achievement.","", "1810",W+"Championship_belt",[],"bare-knuckle era"),
A("Sanctioning-body title belt","Large ornate belt held by champions in boxing, wrestling and mixed martial arts, such as the World Boxing Council belt.","", "",W+"Championship_belt",[],"organisation · weight class · replica or title version")]
sh=[s for dp in d['depts'] if dp['n']=='Trophies & awards' for s in dp['s']][0]
sh['k']=[trophy,belt,ring]
# F3-5 tokens
sv=[popk(n) for n in ['Transit and toll token','Vending machine token','Locker and shopping cart token','Tax token']]
svc={"n":"Service token","a":"transit token · vending token · tax token · trolley token","d":"Token issued to pay a fare, buy from a machine, release a locker or trolley, or pay a tax in small fractions.","s":sv[0]['s'],
 "t":["transit and toll token","parking token","car-wash token","laundry token","telephone token","shopping-trolley token","locker token","sales tax token"],
 "x":[a for k in sv for a in k.get('x',[])]}
tk=[s for dp in d['depts'] if dp['n']=='Exonumia: tokens & medals' for s in dp['s'] if s['n']=='Tokens'][0]
i=[k['n'] for k in tk['k']].index('Admission, communion or voting token')
tk['k'].insert(i+1,svc)
# F3-6 orders
od=[dp for dp in d['depts'] if dp['n']=='Orders, decorations & medals'][0]
old={k['n']:k for s in od['s'] for k in s['k']}
iss={'British gallantry decoration':'United Kingdom','British order of chivalry':'United Kingdom','British campaign medal':'United Kingdom','British long-service medal':'United Kingdom','US gallantry and merit decoration':'United States','US campaign and service medal':'United States','French orders and decorations':'France','German and Prussian orders and decorations':'Germany and Prussia','Russian and Soviet orders and medals':'Russia and USSR','Japanese orders and decorations':'Japan','Orders of chivalry of other states':'other states'}
newk={}
def nk(n,dd,s_): newk[n]={"n":n,"a":"","d":dd,"s":s_,"t":[],"x":[],"m":[]}
nk('Gallantry and merit decoration',"Decoration for gallantry, wounds or distinguished service, from any issuing state; the state is the issuer.",old['British gallantry decoration']['s'])
nk('Order of chivalry or state order',"Insignia of an order of chivalry or state order (badge, star, collar or sash badge) from any issuing state.",old['British order of chivalry']['s'])
nk('Campaign medal',"Medal awarded for service in a named campaign, war or theatre, from any issuing state.",old['British campaign medal']['s'])
nk('Long-service and good-conduct medal',"Medal awarded for a length of service or record of conduct.",old['British long-service medal']['s'])
newk['Gallantry and merit decoration']['a']='gallantry cross · valour medal'
newk['Order of chivalry or state order']['a']='order · knighthood insignia'
dest={'Iron Cross':'G','Croix de guerre 1914–1918':'G','Médaille militaire':'G','Hero of the Soviet Union':'G','Order of the Golden Kite':'G','Good Conduct Medal':'L'}
def target(kn,a):
    if a['n'] in dest: t=dest[a['n']]
    elif kn in('British gallantry decoration','US gallantry and merit decoration'): t='G'
    elif kn in('British campaign medal','US campaign and service medal'): t='C'
    elif kn=='British long-service medal': t='L'
    else: t='O'
    return {'G':'Gallantry and merit decoration','O':'Order of chivalry or state order','C':'Campaign medal','L':'Long-service and good-conduct medal'}[t]
for kn,k in old.items():
    if kn not in iss: continue
    for a in k.get('x',[]):
        a=copy.deepcopy(a); a['dt']=(a.get('dt','')+' · ' if a.get('dt') else '')+'issuer: '+iss[kn]
        newk[target(kn,a)]['x'].append(a)
    for t in k.get('t',[]) or []:
        for tg in newk:
            if t not in newk[tg]['t'] and tg==target(kn,{'n':''}): newk[tg]['t'].append(t)
    for m in k.get('m',[]) or []:
        newk[target(kn,{'n':''})]['m'].append([m[0]+' ('+iss[kn]+')' if m[0] in('Distinguished Flying Cross','Meritorious Service Medal') else m[0],m[1]])
for k in newk.values():
    if not k['m']: del k['m']
    if not k['t']: del k['t']
case=old['Medal case']; mb=old['Medal mounting bar and ribbon']
addt(mb,'presentation case','medal case'); mb['d']=mb['d']+' Includes cases made to hold one medal.'
od['s']=[{"n":"Orders, decorations & medals by type","k":list(newk.values())},{"n":"Ribbons, bars & cases","k":[mb]}]
json.dump(d,open('/home/user/Possession-Taxonomy/rebuild/work/FIX_F3/F3.new.json','w'),ensure_ascii=False,indent=1)
