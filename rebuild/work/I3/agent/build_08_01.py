import json, os
W='https://en.wikipedia.org/wiki/'
TI='https://prnewswire.co.uk/news-releases/travelling-tutors-tutors-international-urge-clients-resuming-travel-to-enquire-about-full-time-private-tutors-now-875728175.html'
kinds=[
 {"n":"Nanny and au pair","a":"nanny · au pair · babysitter · childcare platform membership","tg":["baby"],
  "d":"Childcare at home by a nanny, au pair or regular sitter, found through an agency, sponsor programme or platform.",
  "t":["live-in nanny","daily nanny","nanny share","after-school nanny","maternity nurse","au pair (J-1 sponsor or agency)","babysitting platform membership","Ofsted-registered nanny (UK)"],
  "s":W+"Au_pair",
  "m":[["Care.com","Care.com · US, Canada, UK, Western Europe"],["Sittercity","Bright Horizons · US"],["Koru Kids","Koru Kids · UK"],
       ["Cultural Care Au Pair","Cultural Care · US J-1 sponsor"],["Au Pair in America","AIFS · US J-1 sponsor"],["Norland nanny","Norland College · UK"]]},
 {"n":"Dog walking and pet sitting","a":"dog walker · pet sitter · house sitting membership · doggy day care",
  "d":"Regular dog walks, drop-in visits, day care or home sitting for pets, usually booked through a platform.",
  "t":["dog walking","drop-in visits","doggy day care","home boarding","house-sitting membership","cat sitting"],
  "s":W+"Rover.com",
  "m":[["Rover","Rover Group · US, Western Europe"],["Wag!","Wag Labs · US"],["Pawshake","Pawshake · Europe, Australia, NZ"],
       ["TrustedHousesitters","TrustedHousesitters · worldwide (annual membership)"],["Cat in a Flat","Rover Group · UK"]]},
 {"n":"Personal trainer","a":"PT · fitness coach · online coaching",
  "d":"An exercise professional who plans and coaches a person's training over a run of sessions.",
  "t":["in-person at a gym","at-home","online coaching","block of sessions","small-group training"],
  "s":W+"Personal_trainer"},
 {"n":"Private tutor","a":"tutoring · tuition · learning centre programme · governess",
  "d":"Regular one-to-one or small-group teaching outside school, online, at home or at a learning centre.",
  "t":["online platform","in-person home tutor","learning-centre programme","exam preparation","residential or full-time tutor (luxury end)"],
  "s":W+"Wyzant",
  "m":[["Kumon","Kumon Institute of Education · Japan, 60+ countries"],["Mathnasium","Mathnasium · US, worldwide"],["Wyzant","IXL Learning · US"],
       ["MyTutor","MyTutor · UK"],["Tutors International","Tutors International · UK (Oxford), worldwide"]]},
 {"n":"Personal chef service","a":"private chef · meal-prep chef · household chef",
  "d":"A chef who cooks in the client's home on a regular schedule, from weekly meal prep to a full-time household post.",
  "t":["weekly meal-prep chef","private chef on retainer","full-time household chef","live-in chef"],
  "s":W+"Personal_chef",
  "m":[["Sous","Sous · US (Chicago)"],["Take a Chef","Take a Chef · Spain, worldwide"]]},
 {"n":"Personal stylist and personal shopper","a":"personal shopping · style concierge · wardrobe stylist",
  "d":"An adviser who chooses or recommends clothes for a client, in store, at home or online, on an ongoing basis.",
  "t":["department-store personal shopping","independent stylist retainer","wardrobe management","online styling service"],
  "s":W+"Personal_shopper",
  "m":[["Personal shopping","Harrods · UK"],["Personal shopping","Selfridges · UK"],["Style concierge","Harvey Nichols · UK"],
       ["Personal stylist service","Nordstrom · US"],["Personal shopper service","Bloomingdale's · US"],["Dappad","Dappad · UK (online, menswear)"]]},
]
def B(n,c,f,seg,kf,d,s,rel=None):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if rel: b["rel"]=rel
    return b
brands=[
 B("Care.com","United States","2007","Mainstream","care marketplace","Online marketplace matching families with nannies, sitters, tutors and other carers.",W+"Care.com"),
 B("Sittercity","United States","2001","Mainstream","babysitters","Chicago marketplace for babysitters, nannies and pet sitters, owned by Bright Horizons.",W+"Sittercity.com"),
 B("Koru Kids","United Kingdom","","Mainstream","after-school nannies","London childcare service matching families with part-time nannies and nanny shares.","https://www.korukids.co.uk/about-koru-kids"),
 B("Norland College","United Kingdom","1892","Institution & issuer","nanny training","Bath college that trains Norland nannies, a status symbol among wealthy families.",W+"Norland_College"),
 B("Au Pair in America","United States","1986","Institution & issuer","au pair programme","AIFS division running the first US State Department-designated au pair programme.","https://blogs.aupairinamerica.com/laa/au-pair-america/"),
 B("Rover","United States","2011","Mainstream","pet sitting","Seattle marketplace for dog walking, pet sitting and boarding in the US and Europe.",W+"Rover.com"),
 B("Wag!","United States","2015","Mainstream","dog walking","App connecting owners with dog walkers and pet carers; filed for bankruptcy in 2025.",W+"Wag_(company)"),
 B("Pawshake","","2013","Mainstream","pet sitting","Pet-sitting platform offering walks, drop-ins and home boarding.","https://www.pawshake.ie/about-us"),
 B("TrustedHousesitters","","","Specialist","house sitting","Annual-membership platform matching pet owners with house sitters in 140+ countries.","https://business-reporter.co.uk/management/trustedhousesitters-the-leading-travel-solution-for-pet-people"),
 B("Kumon","Japan","1958","Mainstream","maths and reading","Japanese after-school worksheet programme with over 26,000 centres worldwide.",W+"Kumon"),
 B("Mathnasium","United States","2002","Mainstream","maths tutoring","US maths learning-centre franchise with over 1,000 centres.",W+"Mathnasium"),
 B("Wyzant","United States","2005","Mainstream","tutor marketplace","Chicago online marketplace for hiring tutors.",W+"Wyzant"),
 B("Tutors International","United Kingdom","1999","Premium","full-time tutors","Oxford firm placing full-time and residential private tutors with wealthy families.",TI),
]
notes=("No old data for this shelf; all 6 planned kinds built new. Operators given in m as [operator/service, company · markets]. "
 "Personal trainer: no operators listed; the credential bodies named on the Wikipedia page (NASM, ACE, ACSM, NSCA, ISSA, NCCA accreditation in the US; CIMSPA Level 3 in the UK; REPs registers) should be dept-level criteria (b), not brands. "
 "Left out for want of a retrieved page: AuPairWorld, Varsity Tutors (404), Cat in a Flat kept only as a Rover subsidiary named on the Rover page. "
 "Take a Chef is mainly one-off dinners (listed as it also books multiple services); no sourced luxury household-chef agency found. "
 "Stitch Fix-type boxes stay in Curated subscription box; gyms/class passes in Gyms & fitness; meal kits and CookUnity-type delivered meals in Meal kit and menu plan.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/I3/shelves/08_01.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
