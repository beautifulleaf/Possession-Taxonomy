import json,os
W="https://en.wikipedia.org/wiki/"
kinds=[
 {"n":"Transit pass","a":"period transit pass · season ticket · rail pass · travelcard · 定期券",
  "d":"Pass for travel on a network or route, valid for a period or a number of journeys.",
  "t":["multi-country rail pass","one-country or regional rail pass","city or regional travelcard","commuter pass (fixed route)","period or travel-day validity","paper, smartcard or mobile"],
  "s":W+"Eurail_pass",
  "x":[
   {"n":"Interrail Global Pass","a":"Interrail","d":"Rail pass valid across all participating European countries, for flexible travel days or continuous validity.","mk":"Interrail B.V.","y":"1972","s":W+"Interrail",
    "v":[{"n":"Global Pass, flexible travel days","mk":"Interrail B.V.","y":"","d":"set number of travel days within a period"},
         {"n":"Global Pass, continuous","mk":"Interrail B.V.","y":"","d":"every day within the validity period"},
         {"n":"Global Pass Plus (beta)","mk":"Interrail B.V.","y":"","d":"includes the cost of many required reservations"},
         {"n":"One Country Pass","mk":"Interrail B.V.","y":"","d":"one country or a group such as Benelux or the Nordic countries"},
         {"n":"Interrail Nordic Pass","mk":"Interrail B.V.","y":"","d":"Nordic countries"},
         {"n":"Interrail Greek Islands Pass","mk":"Interrail B.V.","y":"","d":"ferries between Greek islands, not rail"}],
    "dt":"age band (child, youth under 27, adult, senior over 60) · class · paper or digital via Rail Planner app"},
   {"n":"Eurail Pass","a":"Eurail Global Pass","d":"Rail pass for non-European residents, first sold in 1959; merged into Interrail and the Eurail brand dropped in September 2026.","mk":"Interrail B.V.","y":"1959","s":W+"Interrail","v":[],"dt":"continent-wide or one-country · travel days"},
   {"n":"Japan Rail Pass","a":"JR Pass","d":"Pass for unlimited travel on Japan Railways Group lines, sold only to overseas visitors.","mk":"Japan Railways Group","y":"","s":W+"Japan_Rail_Pass",
    "v":[{"n":"Standard Car (ordinary)","mk":"Japan Railways Group","y":"","d":"7, 14 or 21 days"},
         {"n":"Green Car","mk":"Japan Railways Group","y":"","d":"first class; 7, 14 or 21 days"}],
    "dt":"validity 7/14/21 days · regional passes for JR Hokkaido, East, Central, West, Shikoku and Kyushu"},
   {"n":"Swiss Travel Pass","a":"formerly Swiss Pass","d":"All-in-one ticket for foreign visitors giving unlimited travel on Switzerland's public transport network.","mk":"","y":"","s":"https://www.myswitzerland.com/en/swiss-travel-pass.html","v":[],
    "dt":"3, 4, 6, 8 or 15 consecutive days · 1st or 2nd class · youth price · children free with Swiss Family Card"},
   {"n":"Deutschlandticket","a":"D-Ticket · 49-euro ticket","d":"Monthly auto-renewing subscription for nationwide local and regional public transport in Germany, second class.","mk":"","y":"2023","s":W+"Deutschlandticket",
    "v":[{"n":"Semesterticket supplement","mk":"","y":"","d":"discounted version offered by universities"}],
    "dt":"smartcard or app only · excludes most long-distance trains · employer and social discounts"},
   {"n":"London Travelcard","a":"Travelcard","d":"Transport for London ticket for unlimited travel within chosen London fare zones for a set period.","mk":"Transport for London","y":"1983","s":W+"Travelcard",
    "v":[{"n":"One-day Anytime / Off-Peak","mk":"Transport for London","y":"","d":"expires 04:29 next day"},
         {"n":"Seven-day","mk":"Transport for London","y":"","d":"season ticket"},
         {"n":"Monthly","mk":"Transport for London","y":"","d":"3.84 × the 7-day fare"},
         {"n":"Annual","mk":"Transport for London","y":"","d":"priced as 40 seven-day tickets"}],
    "dt":"zones 1–9 combinations · paper or Oyster"},
   {"n":"Navigo pass","a":"passe Navigo","d":"Île-de-France Mobilités smartcard carrying travel passes for the Paris region network.","mk":"Île-de-France Mobilités","y":"2001","s":W+"Navigo_pass",
    "v":[{"n":"Year Pass (Annuel)","mk":"Île-de-France Mobilités","y":"","d":"Travel card or smartphone"},
         {"n":"Month Pass (Mois)","mk":"Île-de-France Mobilités","y":"","d":""},
         {"n":"Week Pass (Semaine)","mk":"Île-de-France Mobilités","y":"","d":""},
         {"n":"Liberté+","mk":"Île-de-France Mobilités","y":"","d":"subscription"},
         {"n":"Navigo Easy","mk":"Île-de-France Mobilités","y":"","d":"€2 card for single tickets and day passes"}],
    "dt":"Travel, Découverte, Easy card or smartphone"},
   {"n":"Suica commuter pass","a":"teikiken · 定期券","d":"Commuter pass stored on a Suica card for one, three or six months between two designated stations.","mk":"JR East","y":"2001","s":W+"Suica",
    "v":[{"n":"Mobile Suica Commuter Pass","mk":"JR East","y":"","d":"on a phone"}],
    "dt":"1, 3 or 6 months · fixed route"}]},
 {"n":"Rail discount card","a":"railcard · discount card · BahnCard · Halbtax · Carte Avantage",
  "d":"Card bought for a year that cuts the price of rail tickets bought with it.",
  "t":["age-based (youth, senior)","group or family","regional network","disabled persons","annual, auto-renewing"],
  "s":W+"Railcard",
  "x":[
   {"n":"Railcard","a":"National Railcard","d":"British railcards giving about a third off most rail fares for eligible groups.","mk":"","y":"","s":W+"Railcard",
    "v":[{"n":"Network Railcard","mk":"","y":"1986","d":"South-east England"},
         {"n":"Senior Railcard","mk":"","y":"1992","d":"new version phased in"},
         {"n":"Two Together Railcard","mk":"","y":"2014","d":"two named people, off-peak"},
         {"n":"16–25 Railcard","mk":"","y":"","d":""},
         {"n":"Family & Friends Railcard","mk":"","y":"","d":"60% off child fares"},
         {"n":"Disabled Persons Railcard","mk":"","y":"","d":"by post or online"}],
    "dt":"one-year or three-year · physical or digital"},
   {"n":"BahnCard","a":"","d":"Deutsche Bahn card giving percentage discounts on rail fares, or unlimited travel at the top level.","mk":"Deutsche Bahn","y":"1992","s":W+"BahnCard",
    "v":[{"n":"BahnCard 25","mk":"Deutsche Bahn","y":"","d":"25% off long-distance fares"},
         {"n":"BahnCard 50","mk":"Deutsche Bahn","y":"","d":"50% off walk-on fares, 25% off saver fares"},
         {"n":"BahnCard 100","mk":"Deutsche Bahn","y":"","d":"annual unlimited-travel pass"}],
    "dt":"1st or 2nd class · youth and senior prices"},
   {"n":"Half Fare Travelcard","a":"Halbtax · demi-tarif","d":"Annual SBB card that halves or reduces most Swiss rail, boat and PostBus fares.","mk":"SBB","y":"","s":"https://www.sbb.ch/en/offers/half-fare-travelcard",
    "v":[{"n":"Half Fare Travelcard (adult 25+)","mk":"SBB","y":"","d":""},
         {"n":"Half Fare Travelcard for Youth","mk":"SBB","y":"","d":"16 to under 25"},
         {"n":"Half Fare Travelcard PLUS","mk":"SBB","y":"","d":"for frequent travellers"},
         {"n":"Swiss Half Fare Card","mk":"SBB","y":"","d":"for visitors from abroad"}],
    "dt":"stored on SwissPass · auto-renewing · same price for both classes"},
   {"n":"Carte Avantage","a":"","d":"SNCF discount card giving about 30% off TGV and Intercités fares for a year.","mk":"SNCF","y":"","s":"https://snowcarbon.co.uk/blog/sncfs-carte-avantage-discounts",
    "v":[{"n":"Carte Avantage (adult)","mk":"SNCF","y":"","d":"shares discount with a companion and up to three children"},
         {"n":"Carte Avantage Jeune","mk":"SNCF","y":"","d":"12–27"},
         {"n":"Carte Avantage Senior","mk":"SNCF","y":"","d":"60+"}],
    "dt":"12 months · €49"}]},
 {"n":"Vehicle-sharing membership","a":"car-sharing membership · car club · bike share · scooter share",
  "d":"Membership giving access to a shared fleet of cars, bikes or scooters; individual trips and hire fees are not included.",
  "t":["car share","bike share","scooter share","round-trip or free-floating","monthly or annual plan"],
  "s":"https://www.zipcar.com/",
  "m":[["Zipcar Membership","Zipcar"],["Citi Bike Annual Membership","Lyft"],["Santander Cycles Annual Membership","Transport for London"],["Santander Cycles Monthly Membership","Transport for London"],["Lime Ride Pass","Lime"]]}
]
def B(n,c,f,seg,kf,d,s,**k):
  b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}; b.update(k); return b
brands=[
 B("Interrail B.V.","","","Specialist","rail passes","Company selling Interrail passes; formerly Eurail B.V., renamed in 2026.",W+"Interrail",sig=["Interrail Global Pass","Eurail Pass"]),
 B("Japan Railways Group","Japan","1987","Institution & issuer","Japan Rail Pass","Group of railway companies formed from Japanese National Railways.","knowledge",sig=["Japan Rail Pass"]),
 B("JR East","Japan","1987","Institution & issuer","Suica","East Japan Railway Company, largest of the JR group companies.","knowledge",sig=["Suica commuter pass"]),
 B("Transport for London","United Kingdom","2000","Institution & issuer","Travelcard","Local government body running London's transport network.","knowledge",sig=["London Travelcard"]),
 B("Île-de-France Mobilités","France","","Institution & issuer","Navigo","Transport authority for the Paris region.",W+"Navigo_pass",sig=["Navigo pass"]),
 B("Deutsche Bahn","Germany","1994","Institution & issuer","BahnCard","German national railway company.","knowledge",sig=["BahnCard"]),
 B("SBB","Switzerland","1902","Institution & issuer","Half Fare Travelcard","Swiss Federal Railways.","knowledge",sig=["Half Fare Travelcard"]),
 B("SNCF","France","1938","Institution & issuer","Carte Avantage","French national railway company.","knowledge",sig=["Carte Avantage"]),
 B("Zipcar","United States","2000","Mainstream","car sharing","Car-sharing membership service, owned by Avis Budget Group since 2013.",W+"Zipcar"),
 B("Lyft","United States","2012","Mainstream","Citi Bike","Ride-hailing company that owns Citi Bike through Motivate.",W+"Citi_Bike"),
 B("Lime","United States","2017","Mainstream","e-scooters","San Francisco micromobility company renting e-scooters, e-bikes and e-mopeds.",W+"Lime_(transportation_company)"),
]
notes=("Restraint pass kept, then extended with fetched sources. Transit pass: old models became archetypes/versions "
 "(Interrail Global Pass with Global/One Country/Nordic/Greek Islands versions; London Travelcard; Mobile Suica Commuter Pass under Suica commuter pass); "
 "added Eurail Pass (merged into Interrail Sept 2026), Japan Rail Pass, Swiss Travel Pass, Deutschlandticket, Navigo pass. "
 "NEW kind Rail discount card: Railcard, BahnCard, Half Fare Travelcard, Carte Avantage. "
 "Vehicle-sharing: added Citi Bike, Santander Cycles and Lime. Left out: Share Now (Wikipedia says it was folded into Free2Move by April 2024); "
 "Swiss Travel Pass and Deutschlandticket have no single issuer in the sources, so mk is empty; Carte Avantage year not confirmed on a fetched page.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p="work/I3/shelves/06_03.json"; t=p+".tmp"
json.dump(out,open(t,"w"),ensure_ascii=False,indent=1); os.replace(t,p)
