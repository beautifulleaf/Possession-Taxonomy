import json, os
W='https://en.wikipedia.org/wiki/'
kinds=[
 {"n":"Newspaper subscription","a":"newspaper digital subscription · news paywall · supporter membership",
  "d":"Subscription to one newspaper title, delivered in print, digitally or both.",
  "t":["digital only","print and digital bundle","weekend print","student","supporter or membership (no paywall)"],
  "s":"https://www.nytimes.com/subscription/all-access",
  "m":[["The New York Times All Access","The New York Times"],["The Wall Street Journal","Dow Jones (News Corp)"],["Financial Times","Nikkei Inc."],
       ["The Guardian supporter membership","Guardian Media Group"],["Le Monde","Groupe Le Monde"],["Die Zeit","Zeitverlag Gerd Bucerius"],
       ["Nihon Keizai Shimbun (Nikkei) digital","Nikkei Inc."]]},
 {"n":"Magazine subscription","a":"magazine subscription · digital magazine",
  "d":"Subscription to one magazine title, delivered in print, digitally or both.",
  "t":["print","digital","print and digital bundle","student"],
  "s":"https://www.newyorker.com/subscribe",
  "m":[["The Economist","The Economist Group"],["The New Yorker","The New Yorker"],["Cook's Illustrated","Cook's Illustrated"],["Golf Digest","Golf Digest"]]},
 {"n":"News and magazine library","a":"all-you-can-read news and magazine subscription · digital newsstand",
  "d":"Plan giving access to a library of many newspaper and magazine titles.",
  "t":["magazines only","newspapers and magazines","family sharing","bundled with other services"],
  "s":"https://www.readly.co/us/offers",
  "m":[["Apple News+","Apple"],["Readly","Readly"],["PressReader","PressReader"],["ZINIO Unlimited","ZINIO"]]},
 {"n":"E-book subscription","a":"e-book library subscription · unlimited reading",
  "d":"Plan giving access to a library of e-books to read while subscribed.",
  "t":["e-books only","e-books and audiobooks","borrowing limit","unlimited reading"],
  "s":"https://www.amazon.com/b?ie=UTF8&node=18473854011",
  "m":[["Kindle Unlimited","Amazon"],["Kobo Plus","Rakuten Kobo"],["Everand","Scribd Inc."],["Storytel","Storytel"]]},
 {"n":"Comic and manga subscription","a":"comic and manga library subscription · digital comics vault",
  "d":"Plan giving access to a library of comics or manga to read while subscribed.",
  "t":["publisher back-catalogue vault","simulpub manga app","monthly","annual"],
  "s":"https://mangaplus.shueisha.co.jp/web_pages/1174",
  "m":[["Marvel Unlimited","Marvel Comics"],["DC Universe Infinite","DC UNIVERSE INFINITE"],["Shonen Jump membership","Viz Media"],["MANGA Plus MAX","Shueisha"]]},
]
brands=[
 {"n":"The Wall Street Journal","c":"United States","f":"1889","seg":"Premium","kf":"business news","d":"New York business daily of Dow Jones, a News Corp division; over four million digital subscribers.","s":W+"The_Wall_Street_Journal"},
 {"n":"Financial Times","c":"United Kingdom","f":"1888","seg":"Premium","kf":"business news","d":"London business daily owned by Nikkei since 2015; pioneer of the metered paywall.","rel":["Nikkei Inc."],"s":W+"Financial_Times"},
 {"n":"The Guardian","c":"United Kingdom","f":"1821","seg":"Mainstream","kf":"reader-funded news","d":"British daily owned by the Scott Trust; open website funded by supporter memberships.","s":W+"The_Guardian"},
 {"n":"The Economist","c":"United Kingdom","f":"1843","seg":"Premium","kf":"current affairs weekly","d":"London weekly of current affairs and economics, in magazine format.","s":W+"The_Economist"},
 {"n":"Le Monde","c":"France","f":"1944","seg":"Mainstream","kf":"French daily","d":"Paris daily of Groupe Le Monde, mostly read by digital subscribers.","s":W+"Le_Monde"},
 {"n":"Die Zeit","c":"Germany","f":"1946","seg":"Mainstream","kf":"weekly newspaper","d":"Hamburg national weekly newspaper published on Thursdays.","s":W+"Die_Zeit"},
 {"n":"PressReader","c":"Canada","f":"1999","seg":"Mainstream","kf":"digital newsstand","d":"Vancouver all-you-can-read service of over 7,000 newspapers and magazines.","s":W+"PressReader"},
 {"n":"ZINIO","c":"","f":"2001","seg":"Mainstream","kf":"digital magazines","d":"Digital magazine newsstand and distributor offering ZINIO Unlimited.","s":"https://corp.zinio.com/distribution/"},
 {"n":"Marvel Comics","c":"United States","f":"","seg":"Mainstream","kf":"comics","d":"Disney-owned comics publisher running Marvel Unlimited, due to close in December 2026.","lines":["Marvel Unlimited"],"s":W+"Marvel_Unlimited"},
 {"n":"Viz Media","c":"United States","f":"","seg":"Specialist","kf":"manga","d":"North American manga publisher running the Shonen Jump app and vault.","s":W+"Weekly_Shonen_Jump_(American_magazine)"},
]
notes=("Titles kept only as representative leading subscription products (7 newspapers, 4 magazines). Marvel Unlimited is scheduled to close on 7 Dec 2026 (Wikipedia), kept with that note in the brand entry. "
 "Nextory left out of e-books: no retrieved page confirmed its e-book offer. Webtoon coins are I2, not here. Old kind sources kept.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='work/I3/shelves/02_00.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('written')
