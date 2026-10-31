import json, os
W='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"Private members' club","a":"members' club · social club · gentlemen's club · St James's club","d":"Membership of a private social club with its own clubhouse, admitting members by election or application.",
 "t":["gentlemen's club (traditional, St James's)","creative and media club","hospitality club group (multiple houses)","nightclub-style club","reciprocal membership (access to partner clubs)","membership grade: full, country, under-27 or junior, overseas"],
 "s":"https://www.sohohouse.com/membership",
 "x":[
  {"n":"White's","a":"White's Club","d":"London's oldest club, begun as Mrs White's Chocolate House and still men-only.","mk":"","y":"1693","s":W+"White's",
   "v":[{"n":"Mrs White's Chocolate House, 4 Chesterfield Street","y":"1693","d":"founded by Francesco Bianco"},{"n":"37–38 St James's Street","y":"1778","d":"present clubhouse"}],"dt":"election by members · men only"},
  {"n":"Athenaeum","a":"Athenaeum Club","d":"Pall Mall club for people distinguished in science, engineering, literature or the arts.","mk":"","y":"1824","s":W+"Athenaeum_Club,_London",
   "v":[{"n":"107 Pall Mall clubhouse","d":"by Decimus Burton"},{"n":"women admitted on equal terms","y":"2002"}],"dt":"election · intellectual membership"},
  {"n":"Reform Club","a":"","d":"Pall Mall club founded by political reformers, in Charles Barry's clubhouse.","mk":"","y":"1836","s":W+"Reform_Club",
   "v":[{"n":"Pall Mall clubhouse","y":"1841","d":"Sir Charles Barry"},{"n":"women admitted on equal terms","y":"1981"}],"dt":"election by members"},
  {"n":"Travellers Club","a":"","d":"Pall Mall gentlemen's club whose members first had to have travelled at least 500 miles from London.","mk":"","y":"1819","s":W+"Gentlemen's_club"},
  {"n":"Union Club of the City of New York","a":"Union Club","d":"New York gentlemen's club, one of the oldest in the United States.","mk":"","y":"1836","s":W+"Gentlemen's_club"},
  {"n":"Annabel's","a":"","d":"Mayfair members' club and nightclub founded by Mark Birley, owned by Richard Caring since 2007.","mk":"","y":"1963","s":W+"Annabel's",
   "v":[{"n":"44 Berkeley Square","y":"1963","d":"original basement club"},{"n":"46 Berkeley Square","y":"2018","d":"present townhouse"}],"dt":"application · dress code"},
  {"n":"Groucho Club","a":"The Groucho","d":"Soho club for people in publishing, media, entertainment and the arts.","mk":"","y":"1985","s":W+"Groucho_Club",
   "v":[{"n":"45 Dean Street, Soho","y":"1985"}],"dt":"two proposers needed"},
  {"n":"Soho House","a":"","d":"Club group for people in creative industries, grown from one Soho house to dozens worldwide.","mk":"Soho House","y":"1995","s":W+"Soho_House_(club)",
   "v":[{"n":"40 Greek Street, London","mk":"Soho House","y":"1995","d":"first house, by Nick Jones"},{"n":"Soho Farmhouse, Oxfordshire","mk":"Soho House","y":"2015","d":"countryside house"},{"n":"Every House membership","mk":"Soho House","d":"access to all houses"}],"dt":"Local House or Every House · age-based grades"},
  {"n":"Zero Bond","a":"","d":"Manhattan members' club at 0 Bond Street, admission by application.","mk":"","y":"2020","s":W+"Zero_Bond",
   "v":[{"n":"0 Bond Street, New York","y":"2020","d":"first club, Scott Sartiano"},{"n":"Wynn Las Vegas","y":"2026","d":"second location"}],"dt":"application · no photography"}
 ]},
{"n":"Golf or country club membership","a":"golf club · country club · golf membership","d":"Membership of a private club built around a golf course or sports grounds, with dining and social facilities.",
 "t":["private (members only)","semi-private (members plus paying visitors)","country club (golf, tennis, swimming, dining)","golf-community club (tied to a housing development)","membership grade: full, social, junior, country or overseas"],
 "s":W+"Country_club",
 "x":[
  {"n":"Royal and Ancient Golf Club of St Andrews","a":"R&A club","d":"St Andrews golf club, invitation-only, whose governing role passed to The R&A in 2004.","mk":"","y":"1754","s":W+"Royal_and_Ancient_Golf_Club_of_St_Andrews",
   "v":[{"n":"Society of St Andrews Golfers","y":"1754","d":"original name"},{"n":"women admitted","y":"2014"}],"dt":"about 2,400 members · invitation only"},
  {"n":"The Country Club, Brookline","a":"","d":"Massachusetts club regarded as the first US country club.","mk":"","y":"1882","s":W+"Country_club"},
  {"n":"Augusta National Golf Club","a":"Augusta National","d":"Georgia golf club of about 300 invited members, home of the Masters.","mk":"","y":"1932","s":W+"Augusta_National_Golf_Club",
   "v":[{"n":"Masters Tournament","y":"1934","d":"played there every year"}],"dt":"invitation only · no application"}
 ],
 "m":[["The Club at Grandezza Membership","The Club at Grandezza"]]},
{"n":"Airline status and frequent-flyer programme","a":"frequent-flyer programme · FFP · airline elite status · miles","d":"An airline's loyalty programme in which members earn miles or points and climb elite status tiers.",
 "t":["alliance tier: oneworld Ruby, Sapphire, Emerald","alliance tier: Star Alliance Silver, Gold","alliance tier: SkyTeam Elite, Elite Plus","qualification: miles, segments, spend or tier points","status match or challenge","co-branded credit card earning"],
 "s":W+"Frequent-flyer_program",
 "m":[["AAdvantage","American Airlines"],["SkyMiles (Medallion status)","Delta Air Lines"],["MileagePlus (Premier status)","United Airlines"],["Executive Club, now The British Airways Club","British Airways"],["Miles & More","Lufthansa Group"],["Flying Blue","Air France–KLM"],["Skywards","Emirates"],["KrisFlyer","Singapore Airlines"],["Qantas Frequent Flyer","Qantas"],["Aeroplan","Air Canada"],["Velocity Frequent Flyer","Virgin Australia"]]},
{"n":"Hotel loyalty status","a":"hotel loyalty programme · hotel elite status · hotel points","d":"A hotel group's loyalty programme in which members earn points and elite tiers through nights or spend.",
 "t":["entry member","mid tier (silver, gold)","top tier (platinum, diamond, globalist)","invitation-only tier","qualification: nights, points or spend","co-branded credit card status"],
 "s":W+"Marriott_Bonvoy",
 "m":[["Marriott Bonvoy (Silver to Ambassador Elite)","Marriott International"],["Hilton Honors (Silver, Gold, Diamond)","Hilton"],["World of Hyatt (Discoverist, Explorist, Globalist)","Hyatt"],["IHG One Rewards (Silver to Diamond Elite)","IHG Hotels & Resorts"],["ALL – Accor Live Limitless (Silver to Diamond)","Accor"]]},
{"n":"Airport lounge membership","a":"lounge pass · lounge access programme","d":"Paid membership giving entry to airport lounges, either one airline's lounges or a network of independent lounges.",
 "t":["lounge network membership (any airline)","airline lounge annual membership","credit-card lounge access","pay-per-visit","invitation-only lounge"],
 "s":W+"Airport_lounge",
 "m":[["Priority Pass (Standard, Standard Plus, Prestige)","Priority Pass"],["DragonPass (Classic, Preferential, Prestige)","DragonPass"],["Admirals Club","American Airlines"]]},
{"n":"Warehouse club membership","a":"wholesale club · membership warehouse","d":"Annual membership needed to shop at a no-frills warehouse store selling goods in bulk.",
 "t":["standard household membership","executive or premium membership (with annual reward)","business membership","trade-only card"],
 "s":W+"Warehouse_club",
 "m":[["Costco (Gold Star, Executive, Business)","Costco"],["Sam's Club","Walmart"],["BJ's Wholesale Club","BJ's Wholesale Club"],["PriceSmart","PriceSmart"],["Makro","Makro"],["Metro card (business customers)","Metro AG"],["Selgros","Selgros"],["S&R Membership Shopping","S&R"],["Wholesale Club","Loblaw"]]},
{"n":"Motoring club and breakdown cover","a":"automobile association · roadside assistance · breakdown recovery","d":"Annual membership of a motoring club giving roadside breakdown help, travel information and discounts.",
 "t":["roadside assistance only","home start","national recovery","European or international cover","personal (any car) or vehicle-based cover"],
 "s":W+"Automobile_association",
 "m":[["AAA membership (US)","AAA"],["CAA membership (Canada)","CAA"],["AA breakdown cover (UK)","The AA"],["RAC breakdown cover (UK)","RAC"],["ADAC membership (Germany)","ADAC"],["ÖAMTC membership (Austria)","ÖAMTC"],["ANWB membership (Netherlands)","ANWB"],["NRMA membership (NSW, Australia)","NRMA"],["RACV membership (Victoria, Australia)","RACV"],["JAF membership (Japan)","JAF"]]},
{"n":"Sports, hobby or social club membership","a":"club subscription · society membership · association membership","d":"Membership of a club or society for a sport, hobby or interest, usually paid yearly.",
 "t":["single-sport club (tennis, sailing, rowing, cricket)","multi-sport or athletic club","mountaineering or alpine club","enthusiast society or campaign group","supporters' membership of a sports club","membership grade: full, junior, family, associate"],
 "s":W+"Sports_club",
 "m":[["CAMRA membership","Campaign for Real Ale"],["Alpine Club membership","Alpine Club"],["New York Athletic Club membership","New York Athletic Club"]]}
]
brands=[
 {"n":"Soho House","c":"United Kingdom","f":"1995","seg":"Premium","kf":"members' clubs","d":"Members' club group founded by Nick Jones on Greek Street, London, now run by Soho House & Co.","lines":["Every House membership","Soho Farmhouse","Soho Home"],"sig":["Soho House"],"s":W+"Soho_House_(club)"},
 {"n":"Priority Pass","c":"United Kingdom","f":"1992","seg":"Mainstream","kf":"lounge access","d":"Independent airport lounge membership run by Collinson Group, with over 1,800 lounges.","lines":["Standard","Standard Plus","Prestige"],"rel":["DragonPass"],"s":W+"Priority_Pass"},
 {"n":"DragonPass","seg":"Mainstream","kf":"lounge access","d":"Independent airport lounge membership that grew from a lounge operator, adding dining and transfer discounts.","lines":["Classic","Preferential","Prestige"],"rel":["Priority Pass"],"s":"https://www.sleepinginairports.net/airport-lounges/dragonpass.htm"},
 {"n":"Costco","c":"United States","f":"1983","seg":"Own-label & retailer","kf":"warehouse club","d":"Membership warehouse chain from Issaquah, Washington, merged with Price Club in 1993.","lines":["Gold Star","Executive","Business"],"s":W+"Costco"},
 {"n":"AAA","c":"United States","f":"1902","seg":"Institution & issuer","kf":"roadside assistance","d":"American Automobile Association, a federation of motor clubs offering breakdown help and travel services.","rel":["CAA"],"s":"knowledge"},
 {"n":"The AA","c":"United Kingdom","f":"1905","seg":"Mainstream","kf":"breakdown cover","d":"British motoring organisation offering breakdown cover and motor insurance.","rel":["RAC"],"s":"knowledge"},
 {"n":"ADAC","c":"Germany","f":"1903","seg":"Institution & issuer","kf":"roadside assistance","d":"Allgemeiner Deutscher Automobil-Club, Germany's motoring club and breakdown service.","s":"knowledge"}
]
notes=("Old 'Club membership' (k36) became Private members' club; its Soho House model is now an archetype and The Club at Grandezza moved to Golf or country club membership as a flat model. "
 "No traditions apply. Core Club omitted (no page retrieved). TCS Switzerland omitted (not on the retrieved motoring-club page). Amex Centurion lounge access left as the 'credit-card lounge access' type, not a model. "
 "Airline programme owners for Miles & More and Skywards follow the shelf brief. executivetraveller.com blocked (403); IHG One Rewards attested from afar.com instead.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/I3/shelves/06_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
