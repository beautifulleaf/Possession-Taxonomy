import json, os
W='https://en.wikipedia.org/wiki/'
kinds=[
 {"n":"Home cleaning service","a":"regular cleaner · maid service · house cleaning plan",
  "d":"A cleaner who visits on a fixed schedule, supplied by an agency, franchise or booking platform.",
  "t":["weekly","fortnightly","agency-employed","platform freelancer","franchise team","eco cleaning","ironing add-on"],
  "s":"https://housekeep.com/home-cleaning/regular-cleaning/locations-city/london",
  "m":[["Merry Maids","Service Master Brands · US, Canada, UK"],["Molly Maid","Neighborly · US, Canada, UK, Japan, Portugal"],
       ["Helpling","Helpling · Germany, Europe, Australia"],["Housekeep","Housekeep · UK (London)"],["Jim's Cleaning","Jim's Group · Australia, NZ, UK, Canada"]]},
 {"n":"Window and gutter cleaning","a":"window cleaner round · window cleaning contract",
  "d":"Recurring exterior window cleaning on a set round, often with gutter, skylight and frame cleaning added.",
  "t":["traditional squeegee","water-fed pole (pure water)","gutter clearing","conservatory or solar-panel cleaning","monthly or eight-weekly round"],
  "s":W+"Window_cleaner",
  "m":[["Fish Window Cleaning","Fish Window Cleaning · US"]]},
 {"n":"Laundry and dry-cleaning subscription","a":"laundry pickup service · wash-and-fold plan · on-demand laundry",
  "d":"An app or online service that collects, washes or dry-cleans and returns clothes on a regular plan.",
  "t":["wash-and-fold","dry cleaning","shirt service","ironing service","locker drop-off"],
  "s":"https://www.uktech.news/news/uk-on-demand-laundry-tech-startups-20210519",
  "m":[["Laundryheap","Laundryheap · UK, US, Europe, Middle East"],["Rinse","Rinse · US, Toronto"],["Oxwash","Oxwash · UK (consumer side to Laundryheap)"],
       ["ihateironing","ihateironing · UK"],["Laundrapp","Laundrapp · UK"],["Love2Laundry","Love2Laundry · UK"]]},
 {"n":"Garden maintenance contract","a":"lawn care plan · lawn treatment programme · gardening round",
  "d":"Lawn, garden or tree care carried out on a retained annual or seasonal schedule.",
  "t":["lawn treatment plan","mowing round","full garden maintenance","tree and shrub care plan","aeration and scarification add-ons"],
  "s":W+"TruGreen",
  "m":[["TruGreen","TruGreen · US"],["GreenThumb","GreenThumb · UK"],["Jim's Mowing","Jim's Group · Australia, NZ, UK, Canada"]]},
 {"n":"Pool and hot-tub maintenance","a":"pool service · spa care plan · hot tub service plan",
  "d":"Regular servicing of a private pool or hot tub: cleaning, water treatment, draining and checks.",
  "t":["weekly pool service","seasonal opening and closing","annual hot-tub service","drain-and-refill visits","chemicals-included plan"],
  "s":"https://www.happyhottubs.co.uk/happy-care-plans",
  "m":[["America's Swimming Pool Company (ASP)","ASP · US"],["Poolwerx","Poolwerx · Australia, NZ, US"],["Lasting Care plan","Happy Hot Tubs · UK"]]},
 {"n":"Pest-control contract","a":"pest plan · termite bond · exterminator service",
  "d":"A recurring inspection and treatment plan against insects, rodents or termites, often with a guarantee.",
  "t":["general pest","termite protection contract","rodent","mosquito","wildlife control"],
  "s":W+"Terminix",
  "m":[["Orkin","Rollins · US, Canada, Australia, UK"],["Terminix","Rentokil Initial · US"],["Rentokil","Rentokil Initial · UK, Europe, Asia-Pacific"],
       ["HomeTeam Pest Defense","Rollins · US"],["Western Exterminator","Rentokil Initial · US"],["J.C. Ehrlich","Rentokil Initial · US"],["Critter Control","Rollins · US"]]},
 {"n":"Home emergency and appliance cover","a":"boiler cover · home emergency cover · appliance warranty · home warranty",
  "d":"A yearly or monthly plan that pays for repairs to heating, plumbing, electrics or appliances when they fail.",
  "t":["boiler and heating","plumbing and drains","electrics","appliance cover","whole-home warranty (US)","annual service included"],
  "s":"https://www.which.co.uk/reviews/boiler-servicing-contracts/article/how-to-choose-the-best-boiler-cover",
  "m":[["HomeCare","British Gas · UK"],["HomeServe","HomeServe · UK, US, France, Spain"],["Domestic & General","Domestic & General · UK, Europe, US"],
       ["American Home Shield","Frontdoor · US"]]},
 {"n":"Home security monitoring","a":"monitored alarm · alarm monitoring contract · central station monitoring",
  "d":"A contract under which an alarm receiving centre watches your home alarm and calls you or the emergency services.",
  "t":["professional monitoring","self-monitoring plan","video verification","keyholding and guard response","cellular backup"],
  "s":W+"Alarm_monitoring_center",
  "m":[["ADT","ADT · US"],["Verisure","Verisure · Europe, South America"],["Securitas Direct","Verisure · Spain, Portugal, Sweden"],
       ["SimpliSafe","SimpliSafe · US, UK"],["Vivint","NRG Energy · US"],["Ring Protect","Ring (Amazon) · US"]]},
]
def B(n,c,f,seg,kf,d,s,rel=None):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if rel: b["rel"]=rel
    return b
brands=[
 B("Merry Maids","United States","1979","Mainstream","home cleaning","US residential cleaning franchise, part of ServiceMaster since 1988.",W+"Merry_Maids"),
 B("Molly Maid","United States","1979","Mainstream","home cleaning","Cleaning franchise founded in Canada, now part of Neighborly.",W+"Molly_Maid"),
 B("Helpling","Germany","2014","Mainstream","cleaning platform","Berlin online platform for booking home cleaners.",W+"Helpling"),
 B("TruGreen","United States","1969","Mainstream","lawn care","Largest US lawn-care company, founded as ChemLawn; sells recurring treatment plans.",W+"TruGreen"),
 B("Rentokil Initial","United Kingdom","1925","Professional & flagship","pest control","British pest-control group that owns Terminix and Ehrlich.",W+"Rentokil_Initial",["Terminix"]),
 B("Terminix","United States","1927","Mainstream","termite control","Memphis pest-control firm that pioneered the termite protection contract; owned by Rentokil Initial.",W+"Terminix",["Rentokil Initial"]),
 B("Orkin","United States","1901","Mainstream","pest control","Atlanta pest-control company owned by Rollins since 1964.",W+"Orkin"),
 B("HomeServe","United Kingdom","1993","Mainstream","home emergency cover","British home emergency repair-plan provider, owned by Brookfield since 2023.",W+"HomeServe"),
 B("American Home Shield","United States","1971","Mainstream","home warranty","US home warranty provider, part of Frontdoor.",W+"American_Home_Shield"),
 B("Domestic & General","United Kingdom","","Mainstream","appliance cover","London-based appliance protection and repair cover provider.",W+"Domestic_%26_General"),
 B("ADT","United States","1874","Mainstream","monitored alarms","US monitored home and small-business security provider, founded as American District Telegraph.",W+"ADT_Inc."),
 B("Verisure","Switzerland","1988","Premium","monitored alarms","European monitored-alarm company founded in Sweden as Securitas Direct.",W+"Verisure"),
 B("SimpliSafe","United States","2006","Value","DIY alarm monitoring","Boston DIY security system maker with monitoring plans and no long-term contract.",W+"SimpliSafe"),
 B("Vivint","United States","","Premium","smart home security","Utah smart-home security and monitoring company owned by NRG Energy.",W+"Vivint"),
]
notes=("No old data for this shelf; all 8 planned kinds built new. Operators given in m as [operator, parent · markets]. "
 "Left out for want of a retrieved source: The Maids, MaidPro, Window Genie, Weed Man, Davey, Ring brand entry (device maker, B8). "
 "Founding years left blank where sources conflict (Domestic & General 1859 vs 1912; Vivint 1997 vs 1999). "
 "Which? (June 2025 survey) names no recommended boiler-cover provider and finds cover usually poor value; Consumer Reports security ratings were paywalled and not used. "
 "One-off jobs (single deep clean, one-off repairs) excluded per BRIEF; alarm devices stay in B8, hot tubs in G3/Home Fixtures, medical alarms in H2.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/I3/shelves/08_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
