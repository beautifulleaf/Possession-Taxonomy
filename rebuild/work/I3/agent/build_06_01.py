import json, os
W='https://en.wikipedia.org/wiki/'
gyms=[["Planet Fitness","Planet Fitness"],["LA Fitness","LA Fitness"],["Equinox Fitness","Equinox Fitness"],["Lifetime Fitness","Lifetime Fitness"],["Crunch Fitness","Crunch Fitness"],["24 Hour Fitness","24 Hour Fitness"],["Anytime Fitness","Anytime Fitness"],["Gold's Gym","RSG Group"],["PureGym","PureGym"],["The Gym Group","The Gym Group"],["David Lloyd Leisure","David Lloyd Leisure"],["Virgin Active","Virgin Active"],["Nuffield Health","Nuffield Health"],["McFit","RSG Group"],["John Reed Fitness","RSG Group"],["GoodLife Fitness","GoodLife Fitness"],["Jetts Fitness","Jetts Fitness"],["Fitness First","Fitness First"],["F45 Training","F45 Training"],["Orangetheory Fitness","Orangetheory Fitness"]]
kinds=[
{"n":"Gym or leisure membership","a":"gym membership · health club · leisure centre membership · facility membership","d":"Membership of one operator's gym, pool, sports centre or climbing wall, usually paid monthly.",
 "t":["budget gym (low-cost, 24-hour)","mid-market gym","premium health club (pools, spa, racquets)","boutique studio (HIIT, cycling, yoga, boxing)","public pool or leisure centre","climbing wall","single-site or all-club access","off-peak, contract or no-contract plan"],
 "s":"https://www.planetfitness.com/gym-memberships","m":gyms},
{"n":"Class pass","a":"multi-studio class pass · corporate fitness pass · fitness aggregator","d":"Pass giving bookings at classes or entry across many studios and gyms, often paid in renewing credits or through an employer.",
 "t":["consumer credit plan","tiered network pass (more venues at higher tiers)","employer-subsidised corporate pass","digital classes add-on"],
 "s":"https://classpass.com/plans",
 "m":[["ClassPass","ClassPass"],["Urban Sports Club","Urban Sports Club"],["Wellhub (formerly Gympass)","Wellhub"],["EGYM Wellpass","EGYM Wellpass"]]}
]
brands=[
 {"n":"Planet Fitness","c":"United States","f":"1992","seg":"Value","kf":"budget gyms","d":"Low-cost gym franchise from Hampton, New Hampshire, aimed at casual and first-time users, with about 2,700 clubs.","lines":["Black Card"],"s":W+"Planet_Fitness"},
 {"n":"RSG Group","c":"Germany","f":"1996","seg":"Mainstream","kf":"gym chains","d":"Fitness group founded by Rainer Schaller that runs McFit, Gold's Gym and John Reed Fitness.","lines":["McFit","Gold's Gym","John Reed Fitness"],"s":W+"RSG_Group"},
 {"n":"ClassPass","c":"United States","f":"2013","seg":"Mainstream","kf":"class pass","d":"Subscription for booking classes at many studios, part of Mindbody and the Playlist group since 2021.","rel":["Wellhub","Urban Sports Club"],"s":W+"ClassPass"},
 {"n":"Wellhub","c":"United States","f":"2012","seg":"Mainstream","kf":"corporate fitness","d":"Employer-paid network of gyms, studios and wellness apps, founded in São Paulo as Gympass.","rel":["ClassPass","EGYM Wellpass"],"s":W+"Wellhub"},
 {"n":"PureGym","c":"United Kingdom","f":"2009","seg":"Value","kf":"budget gyms","d":"Low-cost, no-contract 24-hour gym chain from Leeds.","rel":["The Gym Group"],"s":"knowledge"},
 {"n":"Equinox Fitness","c":"United States","f":"1991","seg":"Premium","kf":"luxury gyms","d":"New York premium health-club chain.","s":"knowledge"},
 {"n":"David Lloyd Leisure","c":"United Kingdom","f":"1982","seg":"Premium","kf":"racquet clubs","d":"Premium health and racquets club chain founded by tennis player David Lloyd.","s":"knowledge"}
]
notes=("Gym list cut from 49 to 20 leading chains by country. Dropped defunct or absorbed: Bally Total Fitness, Esporta Health Clubs, California Fitness. Dropped non-gyms: Les Mills International (programme licensor), Hypoxi (device studio). "
 "Dropped long tail: Bannatyne, Ben Dunne Gyms, Blink Fitness, Celebrity Fitness, Curves International, EFM Health Clubs, Elixia, Energie Group Gyms, Everlast Gyms, Goodlife Health Clubs, Gunze Sports, GymNation, Gymbox, Hard Candy Fitness, JD Sports Gyms, Places for People, Snap Fitness, Sports Direct Fitness, Talwalkars, Total Fitness, Village Hotel Club, West Wood Club, World Gym, Youfit. "
 "FitX not added (no retrieved page). Urban Sports Club kept from old data (wiki page 404). Wellhub from Wikipedia (axios 403).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/I3/shelves/06_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
