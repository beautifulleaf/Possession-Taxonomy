import json, os
W='https://en.wikipedia.org/wiki/'
PJ='http://privatejetcardcomparisons.com/2024/04/16/sentient-jet-celebrates-25th-anniversary-of-inventing-the-jet-card/'
kinds=[
{"n":"Chauffeur service","a":"private chauffeur · chauffeur on retainer · long-term chauffeur hire · personal driver",
 "d":"A chauffeur and car retained by the week or month, or a full-time private driver, rather than a single ride.",
 "t":["weekly or monthly chauffeur hire","personal or business chauffeur account","full-time private chauffeur (agency-placed)","close-protection driver"],
 "s":W+"Chauffeur",
 "m":[["Long-term chauffeur hire, weekly or monthly (UK)","HCD Chauffeur Drive"],
      ["Prebooked chauffeur platform via local partners (Germany, worldwide)","Blacklane"]]},
{"n":"Private jet card and membership","a":"jet card · private aviation membership · fractional jet share · jet lease",
 "d":"Prepaid flight hours, a membership or a fractional share giving guaranteed access to an operator's private jets.",
 "t":["jet card (prepaid hours)","membership programme","fractional share","jet lease","multi-year subscription programme","cabin class: light, midsize, super-midsize, heavy"],
 "s":W+"Jet_card",
 "m":[["Fractional ownership and jet card (US)","NetJets"],
      ["Fractional ownership, lease and jet card (US)","Flexjet"],
      ["Jet card, the first, 1999 (US)","Sentient Jet"],
      ["Program multi-year subscription (Malta)","VistaJet"],
      ["Membership and on-demand flights (US)","XO"],
      ["Private aviation membership (US)","Wheels Up"]]},
{"n":"Boat club and fractional yacht","a":"boat club · boat-sharing membership · fractional yacht ownership · yacht share",
 "d":"Membership of a shared boat fleet, or a fractional share in a yacht with a set number of weeks aboard each year.",
 "t":["boat club membership (shared fleet)","fractional yacht share (e.g. quarter share)","yacht membership programme"],
 "s":W+"Freedom_Boat_Club",
 "m":[["Boat club membership, about 430 locations (US and abroad)","Freedom Boat Club"],
      ["Boat club membership, licensed local clubs (US, Canada)","Carefree Boat Club"],
      ["YachtQuarters quarter share, Princess 75 (Mallorca)","Princess Yachts"]]},
]
brands=[
{"n":"NetJets","c":"United States","f":"1964","seg":"Professional & flagship","kf":"fractional jets","d":"Columbus, Ohio fractional-ownership and jet-card operator, founded as Executive Jet Airways and owned by Berkshire Hathaway since 1998.","lines":["Fractional ownership","Jet card"],"s":W+"NetJets"},
{"n":"Flexjet","c":"United States","f":"1995","seg":"Premium","kf":"fractional jets","d":"Fractional ownership, leasing and jet-card operator started by Bombardier, owned by Directional Aviation since 2013.","rel":["Sentient Jet"],"s":W+"Flexjet"},
{"n":"Sentient Jet","c":"United States","seg":"Premium","kf":"jet cards","d":"Boston jet-card provider credited with inventing the jet card in 1999; part of Flexjet.","rel":["Flexjet"],"s":PJ},
{"n":"VistaJet","c":"Malta","f":"2004","seg":"Professional & flagship","kf":"jet subscription","d":"Global business-jet operator founded by Thomas Flohr, selling multi-year Program subscriptions for hours flown.","rel":["XO"],"s":W+"VistaJet"},
{"n":"XO","c":"United States","f":"2006","seg":"Premium","kf":"jet membership","d":"Fort Lauderdale private-aviation brand, formerly XOJET, under Vista Global since 2019.","rel":["VistaJet"],"s":W+"XOJET"},
{"n":"Wheels Up","c":"United States","f":"2013","seg":"Mainstream","kf":"jet membership","d":"New York private-aviation membership company founded by Kenny Dichter; absorbed Delta Private Jets in 2020.","s":W+"Wheels_Up"},
{"n":"Freedom Boat Club","c":"United States","f":"1989","seg":"Mainstream","kf":"boat club","d":"Sarasota-founded boat club giving members access to a shared fleet; owned by Brunswick since 2019.","s":W+"Freedom_Boat_Club"},
{"n":"Carefree Boat Club","c":"United States","f":"2002","seg":"Mainstream","kf":"boat club","d":"Boat club network of independently owned, licensed local clubs sharing boats across locations.","s":"https://boatingindustry.ca/current-news/carefree-opens-new-club-in-toronto-canada"},
{"n":"Blacklane","c":"Germany","f":"2011","seg":"Premium","kf":"chauffeur booking","d":"Berlin chauffeur-booking platform working with local chauffeur firms at fixed prebooked rates.","s":W+"Blacklane"},
{"n":"HCD Chauffeur Drive","c":"United Kingdom","seg":"Specialist","kf":"chauffeur hire","d":"London chauffeur firm offering day, weekly and monthly chauffeur hire.","s":"https://www.hcdchauffeurdrive.com/services/long-term-chauffeur/"},
]
notes=("New shelf, no old kinds. Single rides, single charters and one-off flights left out; owning a jet or yacht outright is G1; yacht clubs as social clubs stay in Clubs & status. "
"Blacklane kept as the brief's named chauffeur provider, but its Wikipedia article attests only prebooked rides, not retainers. "
"Princess Yachts YachtQuarters is listed under its maker; no register entry because Princess Yachts belongs in G1 and was not sourced as a brand here. "
"Left out: other fractional-yacht schemes (AvYachts, Dream Yacht, Sunseeker shares: seen only in search snippets, trading status unknown); Air Partner and Marquis Jet (named on the jet-card page only; Marquis Jet was folded into NetJets). "
"Sentient Jet founding is given as the 1999 jet-card launch; the Business Wire release was blocked (403) and Wikipedia has no article.")
p='work/I3/shelves/08_03.json'; json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":notes},open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
