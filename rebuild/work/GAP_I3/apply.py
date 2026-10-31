import json,re,os,sys
P='/home/user/Possession-Taxonomy/rebuild/out/I3.json'
d=json.load(open(P))
K={}
for dp in d['depts']:
    for s in dp['s']:
        for k in s['k']: K[k['n']]=k
WP='https://en.wikipedia.org/wiki/'
def ent(kind,n,noun,mk=None,y=None,g=None,s=None,role=None,own=None,cty=None):
    k=K[kind]
    names={e['n'].lower() for e in k.get('x',[])}
    if n.lower() in names: return
    e={'n':n,'d':f"{n} is {noun}"+(f" from {mk}." if mk and mk!=n else "."),'s':s,'v':[]}
    if mk: e['mk']=mk
    if own: e['own']=own
    if y: e['y']=str(y)
    if g: e['g']=g
    if role: e['role']=role
    if cty: e['cty']=cty
    k.setdefault('x',[]).append(e)
def setg(kind,mapping,default=None):
    for e in K[kind]['x']:
        if e['n'] in mapping: e['g']=mapping[e['n']]
        elif default and not e.get('g'): e['g']=default
def sel(kind,text,replace=True):
    k=K[kind]; old=k.get('sel','')
    k['sel']=text if replace else (old+' '+text)
# ---------- Email
s=WP+'Comparison_of_webmail_providers'; N='an email service'
for n,y in [('AOL Mail',1993),('HEY',2020),('Hushmail',1999),('Kolab Now',2013),('Lycos Mail',1997),('Mail.com',1995),('mailbox.org',2014),('Mailfence',2013),('Rediffmail',1997),('StartMail',2014)]:
    ent('Email service',n,N,y=y,s=s)
yrs={'Gmail':2004,'Outlook.com':1996,'Yahoo! Mail':1997,'iCloud Mail':2011,'Proton Mail':2014,'Tuta':2011,'Fastmail':1999,'GMX Mail':1997,'Mail.ru':1998,'Zoho Mail':2008,'Posteo':2009,'Yandex Mail':2000}
for e in K['Email service']['x']:
    if e['n'] in yrs: e['y']=str(yrs[e['n']])
    y=int(e['y']); e['g']='Launched in the '+('1990s' if y<2000 else '2000s' if y<2010 else '2010s' if y<2020 else '2020s')
K['Email service']['xg']='by launch decade'
sel('Email service',"Every row of Wikipedia's Comparison of webmail providers: Complete, 22 of 22 (the page's Outlook / Hotmail row is Outlook.com, its iCloud row is iCloud Mail, its mailbox row is mailbox.org; the last 8,776 characters of the page were not read). Sections by launch year as the page gives it; Outlook.com carries its 1996 Hotmail year.")
# ---------- VPN
s=WP+'Comparison_of_virtual_private_network_services'; N='a VPN service'
for n,mk in [('Avast SecureLine','Avast'),('Amnezia VPN',None),('Hotspot Shield','AnchorFree'),('IPVanish','Ziff Davis'),('NymVPN','Nym Technologies'),('PrivadoVPN',None),('SaferVPN',None)]:
    ent('VPN service',n,N,mk=mk or n,s=s)
sel('VPN service',"Every service in Wikipedia's Comparison of virtual private network services: Complete, 16 of 16 (the page's ProtonVPN is Proton VPN). Surfshark is not on the page and comes from the earlier pass.")
# ---------- Password
s=WP+'Comparison_of_password_managers'; N='a password manager with a paid plan'
for n in ['Enpass','Keeper','NordPass','Proton Pass','RoboForm','SafeInCloud','Intuitive Password']:
    ent('Password manager plan',n,N,mk=n,s=s)
sel('Password manager plan',"Wikipedia's Comparison of password managers, rows with a paid or subscription price: Complete, 11 of 13 in scope. Pleasant Password Server (a business server) and SecureSafe (an online file safe, listed in Cloud storage plan) are left out. Free-only managers are out of scope.")
# ---------- Cloud storage
sel('Cloud storage plan',"Complete for the in-scope rows: 23 of 23 (8 of the page's 31 rows are object stores, file lockers or enterprise tools and are out of scope).",replace=False)
# ---------- Backup
s=WP+'Comparison_of_online_backup_services'; N='an online backup service'
for n in ['CrashPlan','Livedrive','SpiderOak','ElephantDrive','Jungle Disk','KeepVault','MiMedia']:
    ent('Online backup plan',n,N,mk=n,s=s)
sel('Online backup plan',"Wikipedia's Comparison of online backup services (32 rows): Complete for consumer backup, 10 of 10 on the page (Backblaze, Carbonite, IDrive and the seven added); Acronis comes from the earlier pass. The other 22 rows are file-sync services (in Cloud storage plan), business backup (Barracuda, Unitrends, Zmanda, Egnyte, Syncplicity, Dropmysite) or backup software (Comodo Backup).")
# ---------- Antivirus
s=WP+'Antivirus_software'; N='an antivirus and security suite'
for n,mk in [('Bitdefender',None),('Kaspersky',None),('ESET',None),('AVG','Avira'),('Avira',None),('Trend Micro',None),('F-Secure',None),('Panda Security',None),('Dr.Web','Doctor Web'),('G Data','G Data CyberDefense'),('Sophos',None),('Malwarebytes',None),('Intego',None),('Comodo',None),('ZoneAlarm','Check Point'),('360 Total Security','Qihoo 360'),('BullGuard',None),('NANO Antivirus','NANO Security')]:
    ent('Antivirus and security suite',n,N,mk=(None if n=='AVG' else mk) or n,s=s)
for e in K['Antivirus and security suite']['x']:
    if e['n']=='AVG': e['mk']='AVG'; e['own']='Gen Digital'
sel('Antivirus and security suite',"Wikipedia's Antivirus software, read to its end (179,131 characters): consumer vendors it names, 21 here. Left out: freeware-only (Microsoft Defender, Security Essentials, ClamAV and its front ends, Immunet), historical products (Pasteur, ThunderByte, Dr Solomon's, VirusBuster, F-PROT, Anti4us, Flushot) and enterprise endpoint tools. The page does not say which products are sold as paid suites. No complete list exists beyond that.")
# ---------- Office
s=WP+'Comparison_of_office_suites'; N='an office suite sold by subscription'
for n,mk in [('Google Workspace','Google'),('WPS Office','Kingsoft'),('SoftMaker Office','SoftMaker'),('OfficeSuite','MobiSystems'),('OnlyOffice','Ascensio Systems'),('Zoho Workplace','Zoho')]:
    ent('Office and productivity suite',n,N,mk=mk,s=s)
sel('Office and productivity suite',"Wikipedia's Comparison of office suites, rows sold by subscription or cloud plan: Complete, 7 of 7 in scope. Left out: Ability Office, Hancom Office and WordPerfect Office (paid, but not described as subscriptions) and free suites.")
# ---------- Dating
s=WP+'Comparison_of_online_dating_services'; N='a dating service with a paid plan'
for n,mk,g in [('Badoo','Bumble Inc.','Bumble Inc.'),('BeautifulPeople',None,None),('Christian Connection',None,None),('Coffee Meets Bagel',None,None),('Cupid','NSI Holdings Ltd.',None),('eHarmony','ParshipMeet Holding GmbH','ParshipMeet'),('Feeld','Feeld Ltd',None),('Mamba',None,None),('Muzz','Shahzad Younas',None),('OkCupid','Match Group','Match Group'),('Parship','ParshipMeet Holding GmbH','ParshipMeet'),('Zoosk','Spark Networks Services GmbH','Spark Networks')]:
    ent('Dating app subscription',n,N,mk=mk or n,g=g,s=s)
setg('Dating app subscription',{'Tinder':'Match Group','Hinge+':'Match Group','Bumble':'Bumble Inc.'},'Other or owner not listed')
K['Dating app subscription']['xg']='by owner group (as the page gives it)'
sel('Dating app subscription',"Wikipedia's Comparison of online dating services (47 rows): Covers 15, the rows whose page text states a paid tier. Left out: rows with no paid plan stated, and adult, affair and casual-contact services (Adult FriendFinder, Ashley Madison, Gleeden, Manhunt, GayRomeo, DOWN).")
# ---------- Cloud gaming
s=WP+'Cloud_gaming'; N='a cloud gaming service'
ent('Cloud gaming service','SberPlay',N,mk='Sberbank',s=s); ent('Cloud gaming service','VK Play',N,mk='VK',s=s)
sel('Cloud gaming service',"Wikipedia's Cloud gaming, 10 active services: Complete for 7 (the 5 earlier plus SberPlay and VK Play). Left out: PlayStation Plus (in Game subscription), Netflix Games (a catalogue inside Netflix), AirConsole (browser party games), and the 11 defunct services.")
# ---------- Messaging
s=WP+'Comparison_of_cross-platform_instant_messaging_clients'; N='a messaging and video-call service'
for n in ['Google Chat','Jami','Skype','Snapchat','Threema','Wire']:
    ent('Messaging and video calls',n,N,mk=n if n not in('Google Chat','Skype','Snapchat') else {'Google Chat':'Google','Skype':'Microsoft','Snapchat':'Snap'}[n],s=s)
sel('Messaging and video calls',"Wikipedia's Comparison of cross-platform instant messaging clients, read to its end: the 18 apps its Media table marks as video-capable; Covers 15 of them here (FaceTime and Zoom Workplace come from the earlier pass). Left out: Google Messages and Apple Messages (phone message apps with no service plan) and Trillian (a client).")
# ---------- Genealogy
ent('Genealogy subscription','MyHeritage','a genealogy subscription',mk='MyHeritage',y=2003,s=WP+'MyHeritage',own='Francisco Partners')
K['Genealogy subscription']['x'][-1]['d']='MyHeritage is a genealogy subscription site founded in Israel in 2003 and acquired by Francisco Partners in 2021.'
sel('Genealogy subscription',"No complete list exists; follows Wikipedia's Ancestry.com and MyHeritage articles. Findmypast is not named on either page, and no fetched page lists genealogy subscriptions as a set.")
# ---------- Warehouse
s=WP+'Warehouse_club'
ent('Warehouse club membership','City Club','a warehouse club membership',mk='City Club',s=s); ent('Warehouse club membership','Landers Superstore','a warehouse club membership',mk='Landers Superstore',s=s)
sel('Warehouse club membership',"Wikipedia's Warehouse club: Complete, 11 of 11 active clubs (Metro AG is the page's Makro / Metro row); 15 defunct clubs are out of scope.")
# ---------- Lounge
s=WP+'Airport_lounge'; N='an airport lounge membership'
for n,mk in [('Delta Sky Club','Delta Air Lines'),('United Club','United Airlines'),('Alaska Lounge','Alaska Airlines'),('Qantas Club','Qantas'),('Koru Club','Air New Zealand'),('Centurion Lounge','American Express'),('Plaza Premium Lounge',None)]:
    ent('Airport lounge membership',n,N,mk=mk or n,s=s)
sel('Airport lounge membership',"Wikipedia's Airport lounge: Complete, 10 of 10 paid-membership lounge networks and airline clubs it names. Left out: invitation-only lounges (Chairman's Lounge, Beyond Lounges), invitation tiers (in Airline status), pay-per-use operators (Aspire Lounges, Global Lounge Network, Go Simply, Holiday Extras, LoungePass), rail lounges and cards that only bundle access.")
# ---------- Hotel
s=WP+'Hotel_loyalty_program'; N='a hotel loyalty scheme'
for n,mk in [('Choice Privileges','Choice Hotels'),('Wyndham Rewards','Wyndham Worldwide'),('M life Rewards','MGM Resorts International'),('Total Rewards','Caesars Entertainment'),('Ritz-Carlton Rewards','Ritz-Carlton'),('Preferred Hotels & Resorts','Preferred Hotels & Resorts'),('Leading Hotels of the World','Leading Hotels of the World'),('Hotels.com reward scheme','Hotels.com')]:
    ent('Hotel loyalty status',n,N,mk=mk,s=s)
sel('Hotel loyalty status',"Wikipedia's Hotel loyalty program: Complete, 13 of 13 named schemes (the page's Accor is ALL, its IHG Rewards Club is IHG One Rewards). Scheme names are the page's, so some are older than the current brand.")
# ---------- Gyms
s=WP+'List_of_health_club_chains'; N='a gym or leisure-club membership'
multi5={'Anytime Fitness','Gold\'s Gym','Snap Fitness','Fitness First','John Reed Fitness','McFit','Virgin Active','Hard Candy Fitness','World Gym','Jetts Fitness'}
mid={'Planet Fitness','Celebrity Fitness','F45 Training','Crunch Fitness','Equinox Fitness','LA Fitness','Orangetheory Fitness','24 Hour Fitness','Ben Dunne Gyms','GymNation'}
for n in ['24 Hour Fitness','Curves International','F45 Training','Fitness First','Orangetheory Fitness','Snap Fitness','World Gym','Blink Fitness','Town Sports International','Youfit','Hard Candy Fitness','John Reed Fitness','Celebrity Fitness','Jetts Fitness','GymNation','Bannatyne','Ben Dunne Gyms','Energie Group Gyms','Everlast Gyms','Gymbox','JD Sports Gyms','Places for People','Sports Direct Fitness','Total Fitness','Village Hotel Club','West Wood Club','Elixia','Gunze Sports Club','Talwalkars','EFM Health Clubs','Goodlife Health Clubs']:
    ent('Gym or leisure membership',n,N,mk=n,s=s)
for e in K['Gym or leisure membership']['x']:
    n=e['n']
    e['g']='In five or more countries' if n in multi5 else 'In two to four countries' if n in mid else 'In one country'
    if n in('Lifetime Fitness','Equinox Fitness'): pass
K['Gym or leisure membership']['xg']='by number of countries the page lists'
K['Gym or leisure membership']['x'].sort(key=lambda e:['In five or more countries','In two to four countries','In one country'].index(e['g']))
sel('Gym or leisure membership',"Wikipedia's List of health club chains: Complete, 45 of 49 chains. Left out: Bally Total Fitness, California Fitness and Esporta (defunct), Hypoxi (a treatment brand) and Les Mills (a class licensor). Sections count the countries the page lists the chain in.")
# ---------- Vehicle sharing
s=WP+'List_of_carsharing_organizations'; N='a car-sharing membership'
cs=[('AutoShare','Canada'),('BlueSG','Singapore'),('Bolt Drive','Estonia'),('Cambio CarSharing','Germany'),('Cityhop','New Zealand'),('Communauto','Canada'),('Community CarShare','Canada'),('Delimobil','Russia'),('Enjoy','Italy'),('Enterprise CarShare','United States'),('EvCard','China'),('Evo Car Share','Canada'),('Flexicar','Australia'),('Flinkster','Germany'),('Free2Move','France'),('GetGo','Singapore'),('Gig Car Share','United States'),('GoCar','Ireland'),('GoGet','Australia'),('Greenwheels','Netherlands'),('Modo','Canada'),('Mondo Ride','United Arab Emirates'),('MylesCar','India'),('Stadtmobil','Germany'),('Turo','United States'),('Uhaul Car Share','United States'),('Yandex.Drive','Russia'),('Yourdrive','New Zealand')]
reg={'Canada':'North America','United States':'North America','Singapore':'Asia','Estonia':'Europe','Germany':'Europe','New Zealand':'Oceania','Russia':'Europe and Russia','Italy':'Europe','China':'Asia','Australia':'Oceania','France':'Europe','Ireland':'Europe','Netherlands':'Europe','United Arab Emirates':'Asia','India':'Asia'}
for n,c in cs:
    ent('Vehicle-sharing membership',n,N,mk=n,g=reg[c],s=s,cty=c)
setg('Vehicle-sharing membership',{'Zipcar Membership':'North America','Citi Bike Annual Membership':'North America','Santander Cycles Annual Membership':'Europe','Santander Cycles Monthly Membership':'Europe'},'Several regions')
K['Vehicle-sharing membership']['xg']='by region'
sel('Vehicle-sharing membership',"Wikipedia's List of carsharing organizations (incomplete by its own description), current operators: Complete, 28 of 36 here plus Zipcar and the three bike-share memberships from the earlier pass. Left out: ride-hailing and taxi apps (Didi, Grab, Ola, Pathao, TappCar), a vehicle maker (Kandi), Witkar and the defunct section.")
# ---------- Motoring clubs
s=WP+'List_of_FIA_member_organisations'; N='a motoring club membership'
for n,c in [('Automobile Club d\'Italia','Italy'),('Touring Club Suisse','Switzerland'),('Automobile Club de Suisse','Switzerland'),('Touring Club Belgium','Belgium'),('Federation of Danish Motorists','Denmark'),('Norwegian Automobile Federation','Norway'),('Automobile Club Association','France'),('Automovil Club Argentino','Argentina'),('Automobile Association of Singapore','Singapore'),('Hong Kong Automobile Association','Hong Kong'),('Korea Automobile Association','South Korea'),('Automobile Association of South Africa','South Africa'),('Automobile Association of Kenya','Kenya'),('Automobile Club of Portugal','Portugal'),('Royal Automobile Club of Catalonia','Spain'),('New Zealand Automobile Association','New Zealand'),('Hellenic Automobile & Touring Services Club','Greece')]:
    ent('Motoring club and breakdown cover',n,N,mk=n,g=c,s=s,cty=c)
setg('Motoring club and breakdown cover',{'AAA membership':'United States','CAA membership':'Canada','AA breakdown cover':'United Kingdom','RAC breakdown cover':'United Kingdom','ADAC membership':'Germany','ÖAMTC membership':'Austria','ANWB membership':'Netherlands','NRMA membership':'Australia','RACV membership':'Australia','JAF membership':'Japan'})
sel('Motoring club and breakdown cover',"Wikipedia's List of FIA member organisations (about 150 rows in the first 100,000 of 106,330 characters): Covers 27, the national mobility clubs recognised by name. Left out: motorsport federations, caravan, camping and road-safety bodies, and clubs whose rows do not say whether they sell breakdown cover; those can be added when a fetched page states their cover.")
# ---------- Rail discount
s=WP+'Railcard'; N='a rail discount card'
for n,y in [('16–17 Saver',2019),('26–30 Railcard',2019),('HM Forces Railcard',None),('Veterans Railcard',None),('Highland Railcard',1988),('Devon & Cornwall Railcard',2006),('Dales Railcard',1995),('Heart of Wales Line Railcard',2000),('Esk Valley Railcard',None),('Cambrian Railcard',None),('Cotswold Line Railcard',None),('Pembrokeshire Railcard',None)]:
    ent('Rail discount card',n,N,mk=n,y=y,s=s,g='United Kingdom')
setg('Rail discount card',{'BahnCard':'Germany','Half Fare Travelcard':'Switzerland','Carte Avantage':'France'},'United Kingdom')
K['Rail discount card']['xg']='by country'
sel('Rail discount card',"Wikipedia's Railcard (UK schemes) plus BahnCard, Half Fare Travelcard and Carte Avantage from the earlier pass: Covers 13 of the 31 UK cards the page names; the rest are withdrawn or merged schemes (Cornish, Devon, West Highland, Valleys, Network Card, Senior Citizen, Gold Card, JobcentrePlus, GroupSave). No complete list exists for other countries.")
# ---------- Jet cards / concierge renames
ren={'Fractional ownership, lease and jet card':'Flexjet','Jet card, the first, 1999':'Sentient Jet','Membership and on-demand flights':'XO','Private aviation membership':'Wheels Up'}
for e in K['Private jet card and membership']['x']:
    if e['n'] in ren:
        e['n']=ren[e['n']]; e['d']=f"{e['n']} sells private jet cards and memberships."; e['v']=[]
        if e['n']=='Sentient Jet': e['role']='origin'; e['d']='Sentient Jet created the first jet card, according to Wikipedia\'s Jet card article.'
s=WP+'Jet_card'
for n,mk in [('Magellan Jets',None),('FlyExclusive Jet Club','FlyExclusive'),('Volato Stretch Card','Volato')]:
    ent('Private jet card and membership',n,'a private jet card',mk=mk or n,s=s)
sel('Private jet card and membership',"Wikipedia's Jet card: Complete, 10 of 11 operators it names (Marquis Jet, a NetJets business, and Air Partner and Airstream Jets are left out as they sell charter, not cards); Magellan's page name is Magellan Explorer. VistaJet comes from the earlier pass.")
for e in K['Lifestyle concierge membership']['x']:
    if e['n']=='Travel and lifestyle concierge': e['n']='Ten Lifestyle Group'; e['d']='Ten Lifestyle Group sells travel and lifestyle concierge memberships.'; e['v']=[]
    if e['n']=='Premium concierge and loyalty services': e['n']='John Paul'; e['d']='John Paul sells premium concierge and loyalty services.'; e['v']=[]
sel('Lifestyle concierge membership',"No complete list exists; follows Wikipedia's Quintessentially Group, which names Ten Lifestyle Group and John Paul as the same kind of service.")
# ---------- Meal kit / curated box
s=WP+'Meal_kit'; N='a meal kit service'
for n,y,c in [('Mad til Døren',2003,'Denmark'),('RetNemt',2006,'Denmark'),('Middagsfrid',2007,'Sweden'),('Linas Matkasse',2008,'Sweden'),('Cook it',None,None),('Goodfood',None,None),('Hungryroot',None,None),('Mindful Chef',None,None),('My Food Bag',None,None),('Purple Carrot',None,None),('Sunbasket',None,None),('Tovala',None,None)]:
    ent('Meal kit and menu plan',n,N,mk=n,y=y,s=s,cty=c)
sel('Meal kit and menu plan',"Wikipedia's Meal kit: Complete, 18 of 19 named companies (Plated is listed as defunct). Factor and Dinnerly come from the earlier pass. The page gives country and year for four companies only.")
ent('Curated subscription box','Bulu Box','a curated subscription box',mk='Bulu Box',s=WP+'Subscription_box')
sel('Curated subscription box',"Wikipedia's Subscription box names Birchbox, Dollar Shave Club (in Replenishment subscription), FabFitFun and Bulu Box: Complete, 3 of 3 boxes. The other entries come from the earlier pass and the listing site cited.")
# ---------- Frequent flyer
s=WP+'List_of_frequent_flyer_programs'; N='an airline frequent-flyer programme'
FF={
'North America':[('Isaruuk Rewards','Air Inuit'),('Connecting Rewards','Bearskin Airlines'),('Aurora Rewards','Canadian North'),('VIPorter','Porter Airlines'),('WestJet Rewards','WestJet'),('Club Premier','Aeroméxico'),('Atmos Rewards','Alaska Airlines'),('Avelo Plus','Avelo Airlines'),('Breezy Rewards','Breeze Airways'),('TrueBlue','JetBlue'),('Rapid Rewards','Southwest Airlines'),('Free Spirit','Spirit Airlines'),('FRONTIER Miles','Frontier Airlines'),('Sun Country Rewards','Sun Country Airlines')],
'Central America and Caribbean':[('BahamasAir Flyer','BahamasAir'),('Sir Turtle Rewards','Cayman Airways'),('LifeMiles','Avianca'),('Préférence','Air Caraïbes'),('Caribbean Miles','Caribbean Airlines'),('ConnectMiles','Copa Airlines')],
'South America':[('Aerolíneas Plus','Aerolíneas Argentinas'),('TudoAzul','Azul Brazilian Airlines'),('LATAM Pass','LATAM Airlines'),('Smiles','Gol Transportes Aéreos'),('Discount Club','JetSmart'),('Loyal Wings','Surinam Airways'),('AeroPass','Aeropostal'),('Avior Plus','Avior Airlines'),('Infinito','Conviasa'),('LASERClub','LASER Airlines')],
'Europe':[('AirRewards','Air Arabia'),('Leader','Belavia'),('Fly More','Bulgaria Air'),('OK Plus','Czech Airlines'),('EuroBonus','Scandinavian Airlines'),('Súlubonus','Atlantic Airways'),('Finnair Plus','Finnair'),('Club Corsair','Corsair'),('Miles+Bonus','Aegean Airlines'),('Wizz Discount Club','Wizz Air'),('Saga Club','Icelandair'),('AER Club','Aer Lingus'),('Millemiglia','Alitalia'),('airBaltic Club','airBaltic'),('Flypass','Air Malta'),('Air Moldova Club','Air Moldova'),('Norwegian Reward','Norwegian Air Shuttle'),('TAP Miles&Go','TAP Air Portugal'),('Carpatair Frequent Flyer','Carpatair'),('My Blue Air','Blue Air'),('Aeroflot Bonus','Aeroflot'),('S7 Priority','S7 Airlines'),('Golden Mile','Smartavia'),('Wings','Ural Airlines'),('Status','UTair'),('Elevate','Air Serbia'),('Suma','Air Europa'),('Bintermás','Binter Canarias'),('Iberia Plus','Iberia'),('Vueling Club','Vueling'),('BRA Vänner','BRA Braathens Regional Airlines'),('Panorama Club','Ukraine International Airlines'),('Bonus Club','Dniproavia Airlines'),('Aurigny Frequent Flyer','Aurigny'),('Flight Club / easyJet Plus','EasyJet'),('My Jet2 Travel Club','Jet2'),('Clan Loganair','Loganair'),('Flying Club','Virgin Atlantic')],
'Middle East':[('AZAL Miles','Azerbaijan Airlines'),('Falconflyer','Gulf Air'),('Mahan & Miles','Mahan Air'),('SkyGift','IranAir'),('Matmid Club','El Al'),('Royal Club (Royal Jordanian)','Royal Jordanian'),('Oasis Club','Kuwait Airways'),('Cedar Miles','Middle East Airlines'),('Sindbad','Oman Air'),('Privilege Club','Qatar Airways'),('Alfursan','Saudia'),('Sfeer','Riyadh Air'),('Nasmiles','Flynas'),('Alfuesan','Flyadeal'),('SaudiGulf Club','SaudiGulf'),('SyrianAir Frequent Flyer','Syrian Air'),('Pegasus Plus','Pegasus Airlines'),('SunExpress your benefits','SunExpress'),('Miles&Smiles','Turkish Airlines'),('Etihad Guest','Etihad Airways'),('Sama Club','Yemenia')],
'Asia':[('Ariana Loyalty Club','Ariana Afghan Airlines'),('Orange Miles','Kam Air'),('Saffron Rewards','Safi Airways'),('Biman Loyalty Club','Biman Bangladesh Airlines'),('Sky Star','US-Bangla Airlines'),('HappinessSmiles','Druk Air'),('Royal Skies','Royal Brunei Airlines'),('BIG','AirAsia'),('AngkorWards','Air Cambodia'),('PhoenixMiles','Air China'),('Fortune Wings Club','Hainan Airlines'),('Eastern Miles','China Eastern Airlines'),('Sky Pearl Club','China Southern Airlines'),('Seagull Club','Donghai Airlines'),('Egret Club','XiamenAir'),('Juneyao Air Club','Juneyao Airlines'),('Zunxiang Club','Kunming Airlines'),('Lucky Clouds Club','Okay Airways'),('Tianhaizhiyun Club','Qingdao Airlines'),('Golden Panda Club','Sichuan Airlines'),('Spring Pass','Spring Airlines'),('Asia Miles / Cathay','Cathay Pacific'),('Maharaja Club','Air India'),('Tata NeuPass','Air India Express'),('BluChip','IndiGo'),('Spice Club','SpiceJet'),('Batik Air Club','Batik Air'),('GarudaMiles','Garuda Indonesia'),('Lion Passport','Lion Air'),('ANA Mileage Club','All Nippon Airways'),('My AirDo','Air Do'),('AMX Point Card','Amakusa Airlines'),('JAL Mileage Bank','Japan Airlines'),('Peach Points','Peach Aviation'),('Solaseed Smile Club','Solaseed Air'),('Starlink Members','StarFlyer'),('Zipair Point Club','Zipair Tokyo'),('Nomad Club','Air Astana'),('Belek Bonus','Air Bishkek'),('Champa Muang Lao','Lao Airlines'),('Enrich','Malaysia Airlines'),('Sky Miles','Aero Mongolia'),('Hunnu Club','Hunnu Air'),('Blue Sky Mongolia','MIAT Mongolian Airlines'),('Royal Lotus Plus','Air Bagan'),('Sky Smiles Club','Myanmar Airways International'),('MNA Club','Myanmar National Airlines'),('Elite Club','Yangon Airways'),('Royal Club (Buddha Air)','Buddha Air'),('Saurya Saarathi','Saurya Airlines'),('High Flyer Club','Shree Airlines'),('SkyClub (Yeti Airlines)','Yeti Airlines'),('Go Rewards','Cebu Pacific'),('Mabuhay Miles','Philippine Airlines'),('PIA Awards Plus+','Pakistan International Airlines'),('Blue Miles','Airblue'),('Indus Miles','Air Indus'),('Fly & Stamp','Air Busan'),('Asiana Club','Asiana Airlines'),('Refresh Point','Jeju Air'),('SKYPASS','Korean Air'),('FlySmiLes','SriLankan Airlines'),('Dynasty Flyer','China Airlines'),('Infinity MileageLands','EVA Air'),('Cosmile','Starlux Airlines'),('FlyerBonus','Bangkok Airways'),('Royal Orchid Plus','Thai Airways'),('Vietjet Skyclub','Thai Vietjet Air'),('Nok Fan Club','Nok Air'),('Bamboo Club','Bamboo Airways'),('Sun Signature','Sun PhuQuoc Airways'),('Skyjoy','VietJet Air'),('LotuSmiles','Vietnam Airlines'),('UzAirPlus','Uzbekistan Airways')],
'Africa':[('Umbi Umbi Club','TAAG Angola Airlines'),('Air Algérie Plus','Air Algérie'),('EgyptAir Plus','EgyptAir'),('Sheba Miles','Ethiopian Airlines'),('sMiles Program','Air Côte d\'Ivoire'),('Asante Rewards','Kenya Airways'),('Rahal','Afriqiyah Airways'),('Namako','Air Madagascar'),('Kestrel Flyer','Air Mauritius'),('Safar Flyer','Royal Air Maroc'),('Flamingo Club','LAM Mozambique Airlines'),('Capricorne Program','Air Austral'),('Dream Miles','RwandAir'),('Voyager','South African Airways'),('Skybucks','Airlink'),('Twiga Miles','Air Tanzania'),('PAA Royal','Precision Air'),('ASKY Club','ASKY Airlines'),('Fidelys','TunisAir'),('Craneflyer','Uganda Airlines'),('Rainbow Club','Air Zimbabwe')],
'Oceania':[('Club Tiare','Air Tahiti Nui'),('Airpoints','Air New Zealand'),('Destinations','Air Niugini'),('Belama Club','Solomon Airlines')]}
for reg_,lst in FF.items():
    for n,mk in lst:
        ent('Airline status and frequent-flyer programme',n,N,mk=mk,g=reg_,s=s)
setg('Airline status and frequent-flyer programme',{'AA ConciergeKey':'North America','United Global Services':'North America','BA Premier':'Europe','Lufthansa HON Circle':'Europe','AAdvantage':'North America','SkyMiles':'North America','MileagePlus':'North America','Executive Club, now The British Airways Club':'Europe','Miles & More':'Europe','Flying Blue':'Europe','Skywards':'Middle East','KrisFlyer':'Asia','Qantas Frequent Flyer':'Oceania','Aeroplan':'North America','Velocity Frequent Flyer':'Oceania'})
K['Airline status and frequent-flyer programme']['xg']='by region'
sel('Airline status and frequent-flyer programme',"Wikipedia's List of frequent flyer programs, read to its end: every distinct programme it names (the lead airline is given; shared programmes such as Miles & More, Flying Blue, LATAM Pass and BIG appear once). Left out: Iberia Express and other rows with no programme, and the page's partner tables. Four invitation or top tiers come from earlier sources. Complete apart from small gaps in the Korea rows.")
# ---------- generic wording
pat=re.compile(r"Follows the page cited for this kind \((.+?)\); no complete reference exists for these services, so the list is not exhaustive\.")
for k in K.values():
    if k.get('sel'):
        k['sel']=pat.sub(lambda m:f"No complete list exists; follows the page cited for this kind ({m.group(1)}).",k['sel'])
# ---------- remaining g gaps
setg('Live TV streaming',{'YouTube TV':'United States','Hulu + Live TV':'United States','Sling TV':'United States','DIRECTV':'United States','Fubo':'United States','Philo':'United States','Zattoo':'Outside the United States','waipu.tv':'Outside the United States','YuppTV':'Outside the United States'})
setg('Pay-TV package',{'Sky TV':'United Kingdom','Canal+':'France','DIRECTV':'United States','DISH':'United States','Xfinity TV':'United States','Foxtel':'Australia','Tata Play':'India'})
setg('Private members\' club',{'White\'s':'United Kingdom','Athenaeum':'United Kingdom','Reform Club':'United Kingdom','Travellers Club':'United Kingdom','Annabel\'s':'United Kingdom','Groucho Club':'United Kingdom','Soho House':'United Kingdom','Garrick Club':'United Kingdom','Brooks\'s':'United Kingdom','Boodle\'s':'United Kingdom','5 Hertford Street':'United Kingdom','Union Club of the City of New York':'United States','Zero Bond':'United States','Knickerbocker Club':'United States','Hong Kong Club':'Hong Kong'})
K['Private members\' club']['xg']='by country'
# coverage line for sports/etc handled by generic. Fixed wireless & grocery box, services: no entries.
# report on gaps
for n,k in K.items():
    if k.get('x'):
        if not k.get('sel') or not re.search(r'(Complete|Covers|No complete list exists)',k['sel']): print('NO COVERAGE LINE',n)
        if k.get('xg') and any(not e.get('g') for e in k['x']): print('MISSING g',n,[e['n'] for e in k['x'] if not e.get('g')][:8])
        if len(k['x'])>12 and not k.get('xg'): print('NEEDS SECTIONS',n,len(k['x']))
tmp=P+'.tmp'; json.dump(d,open(tmp,'w'),ensure_ascii=False,indent=1); os.replace(tmp,P)
print('written')
