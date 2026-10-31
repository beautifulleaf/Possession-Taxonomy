import json,os
P='rebuild/out/'
d=json.load(open(P+'I3.json')); B=json.load(open(P+'I3_brands.json'))
def find(n):
  for dp in d['depts']:
    for sh in dp['s']:
      for k in sh['k']:
        if k['n']==n: return k
def keep(k,key,idx): k[key]=[k[key][i] for i in idx]
def arch(n,d_,y,s,mk='',a='',v=None,dt=''):
  return {"n":n,"a":a,"d":d_,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
# I3-1 airline status
k=find("Airline status and frequent-flyer programme")
k['x']=[
 arch("AA ConciergeKey","American Airlines' invitation-only status above Executive Platinum, with no published criteria.","","https://onemileatatime.com/guides/american-airlines-concierge-key/","American Airlines","Concierge Key · CK",dt="invitation only · renewed each programme year"),
 arch("United Global Services","United's top MileagePlus tier, mainly by invitation; four million lifetime miles on United also qualify.","","https://www.pointhacks.com.au/mileageplus/united-global-services/","United Airlines","GS",dt="invitation or Million Miler route"),
 arch("BA Premier","British Airways' invitation-only tier for holders of large travel budgets, with no published criteria.","","https://travellingonpoints.com/article/airlines/british-airways/british-airways-premier-explained/","British Airways",dt="invitation only · nomination"),
 arch("Lufthansa HON Circle","Miles & More top tier, earned with 6,000 points a year on first and business class flights.","","https://onemileatatime.com/guides/lufthansa-hon-circle/","Lufthansa Group","HON Circle Member",dt="points-based (not invitation) · first and business class only"),
]
# I3-1 ski passes + I3-7 labels
k=find("Season ticket")
k['x']=[
 arch("Epic Pass","Vail Resorts' multi-resort ski season pass, with partner resorts in several countries.","","https://en.wikipedia.org/wiki/Epic_Pass","Vail Resorts",dt="full or limited-day tiers · partner resorts"),
 arch("Ikon Pass","Alterra Mountain Company's multi-resort ski season pass, announced in January 2018.","2018","https://en.wikipedia.org/wiki/Ikon_Pass","Alterra Mountain Company",dt="full or base tiers · partner resorts"),
]
find("Annual pass")['n']="Single-venue annual pass"
find("Multi-site membership")['n']="Heritage & parks membership"
find("Multi-venue pass")['n']="City & museum pass"
# I3-2 clubs
k=find("Private members' club")
new=[
 ("Garrick Club","London club founded in 1831 with ties to theatre and the arts, named after the actor David Garrick.","1831","https://en.wikipedia.org/wiki/Garrick_Club","election by members · arts and law"),
 ("Brooks's","Selective gentlemen's club at 60 St James's Street, London, founded in 1764.","1764","https://en.wikipedia.org/wiki/Brooks's","election by members"),
 ("Boodle's","London members' club at 28 St James's Street, founded in 1762 by Lord Shelburne.","1762","https://en.wikipedia.org/wiki/Boodle's","election by members"),
 ("Knickerbocker Club","Manhattan gentlemen's club at 2 East 62nd Street, founded in 1871.","1871","https://en.wikipedia.org/wiki/Knickerbocker_Club","election by members"),
 ("5 Hertford Street","Mayfair members-only club opened in 2012, owned by Robin Birley.","2012","https://en.wikipedia.org/wiki/5_Hertford_Street","members only · private club and nightclub"),
 ("Hong Kong Club","Hong Kong's oldest private members' club, opened in 1846.","1846","https://en.wikipedia.org/wiki/Hong_Kong_Club","business and dining club"),
]
have={x['n'] for x in k['x']}
for n,dd,y,s,dt in new:
  if n not in have: k['x'].append(arch(n,dd,y,s,dt=dt))
# jet card
k=find("Private jet card and membership")
k['x']=[
 arch("NetJets","Fractional ownership of business jets, plus jet cards sold as 25-hour blocks.","1964","https://en.wikipedia.org/wiki/NetJets","NetJets",dt="fractional share · jet card"),
 arch("VistaJet Program","Multi-year subscription guaranteeing availability, with jets hired by the hour flown.","2004","https://en.wikipedia.org/wiki/VistaJet","VistaJet",dt="Program subscription · Direct on request"),
]
k['m']=[m for m in k['m'] if m[1] not in('NetJets','VistaJet')]
k=find("Lifestyle concierge membership")
k['x']=[arch("Quintessentially","Members-only lifestyle management and concierge service covering travel, dining and events.","2000","https://en.wikipedia.org/wiki/Quintessentially_Group","Quintessentially",dt="individual and corporate memberships")]
k['m']=[m for m in k['m'] if m[1]!='Quintessentially']
# I3-3 caps
keep(find("Video streaming service"),'r',[0,1,3,5,8,12,13,17,20,22,23,24,25,26])
keep(find("Music streaming"),'r',[0,1,3,5,7])
keep(find("Mobile phone plan"),'r',[0,2,5,6,9,12,13,17,23,24,25,27,29,32,35,36,39,47,49,50,52,54,55])
keep(find("Broadband plan"),'r',[0,1,2,9])
g=find("Gym or leisure membership"); g['m']=[m for m in g['m'] if m[0] not in('24 Hour Fitness','Jetts Fitness','Fitness First','F45 Training','Orangetheory Fitness','John Reed Fitness')]
# I3-4
k=find("Personal stylist and personal shopper")
k['m']=[["Personal shopping","Harrods · Selfridges · UK"]]+[m for m in k['m'] if m[0]!="Personal shopping"]
# I3-5
k=find("Personal web and game-server hosting"); k['t']=[t for t in k['t'] if t!='domain name']
for n in ["VPN service","AI assistant subscription","Language-learning plan","Cloud storage plan","Stock library subscription","Season or battle pass"]:
  k=find(n); k['d']=k['d'].rstrip()+" Plan only; the product or asset is in I1 or I2."
d['lead']=d['lead'].rstrip('.')+"; where a plan gives access to software or an asset, the plan is here and the product is in I1 or I2."
# I3-6
k=find("Sports, hobby or social club membership")
k['t']=["single-sport club","multi-sport or athletic club","mountaineering or alpine club","enthusiast society or campaign group","supporters' membership of a sports club","membership grade: full, junior, family, associate"]
k=find("Gym or leisure membership")
k['t']=[t if 'boutique' not in t else "boutique studio" for t in k['t']]
# brands
names={x['n'].lower() for x in B['b']}
def addb(n,c,kf,dd,s):
  if n.lower() not in names: B['b'].append({"n":n,"c":c,"f":"","seg":"Mainstream","kf":kf,"d":dd,"s":s})
addb("American Airlines","","airline loyalty","Airline whose AAdvantage programme includes the invitation-only ConciergeKey tier.","https://onemileatatime.com/guides/american-airlines-concierge-key/")
addb("United Airlines","","airline loyalty","Airline whose MileagePlus programme includes the Global Services tier.","https://www.pointhacks.com.au/mileageplus/united-global-services/")
addb("British Airways","","airline loyalty","Airline whose Club programme includes the invitation-only Premier tier.","https://travellingonpoints.com/article/airlines/british-airways/british-airways-premier-explained/")
addb("Lufthansa Group","","airline loyalty","Airline group whose Miles & More programme tops out at HON Circle.","https://onemileatatime.com/guides/lufthansa-hon-circle/")
addb("Vail Resorts","United States","ski pass","Resort operator based in Broomfield, Colorado, running the Epic Pass.","https://en.wikipedia.org/wiki/Epic_Pass")
addb("Alterra Mountain Company","United States","ski pass","Denver-based resort company running the Ikon Pass.","https://en.wikipedia.org/wiki/Ikon_Pass")
B['b'].sort(key=lambda x:x['n'].lower())
for f,o in((P+'I3.json',d),(P+'I3_brands.json',B)):
  json.dump(o,open(f+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(f+'.tmp',f)
