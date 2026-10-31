import json
f='/home/user/Possession-Taxonomy/rebuild/out/E2_parts/RACKET.json'
p=json.load(open(f))
W='https://en.wikipedia.org/wiki/'
p['brands']=[
 {"n":"Amer Sports","c":"","seg":"Owner group","kf":"Wilson, Salomon, Arc'teryx, Atomic, DeMarini, Louisville Slugger","d":"Sporting goods group owned by Anta Sports since 2018; listed again in February 2024.","s":W+"Amer_Sports"},
 {"n":"Acushnet Company","c":"United States","seg":"Owner group","kf":"Titleist, FootJoy, Scotty Cameron, Pinnacle, Vokey","d":"Golf equipment group listed on the NYSE in 2016; Fila Korea held 53.1% from August 2018.","s":W+"Acushnet_Company"},
 {"n":"Topgolf Callaway Brands","c":"United States","f":"1982","seg":"Owner group","kf":"Callaway, Odyssey, TravisMathew, OGIO","d":"Renamed from Callaway Golf Company on 24 August 2022.","s":W+"Callaway_Golf_Company"},
 {"n":"Anta Sports","c":"","seg":"Owner group","kf":"Amer Sports","d":"Leads the consortium that has owned Amer Sports since 2018.","s":W+"Amer_Sports"},
 {"n":"Decathlon","c":"France","f":"1976","seg":"Retailer brand family","kf":"Kipsta, Domyos, Quechua","d":"Sports retailer founded in Lille by Michel Leclercq; 1,902 stores in 82 countries.","s":W+"Decathlon_(retailer)"},
 {"n":"TaylorMade","c":"United States","f":"1979","seg":"Specialist","kf":"metalwood drivers","d":"Founded by Gary Adams; owned by Centroid Investment Partners.","s":W+"TaylorMade"},
 {"n":"Peak Achievement Athletics","c":"","seg":"Owner group","kf":"Bauer Hockey","d":"Parent of Bauer since 2017; Fairfax Financial is its owner.","s":W+"Bauer_Hockey"},
 {"n":"Grays International","c":"United Kingdom","seg":"Owner group","kf":"Gilbert","d":"Bought Gilbert in 2002.","s":W+"Gilbert_Rugby"},
 {"n":"Centroid Investment Partners","c":"","seg":"Owner group","kf":"TaylorMade","d":"Owner of TaylorMade Golf.","s":W+"TaylorMade"},
 {"n":"Head Austria GmbH","c":"Austria","seg":"Owner group","kf":"Head, Penn, Mares, Tyrolia","d":"Parent of the Head brands; headquarters in Kennelbach.","s":W+"Head_(company)"},
]
p['brand_updates']={
 "Wilson":{"own":"Amer Sports","tier":"Global group","c":"United States"},
 "Wilson Sporting Goods":{"own":"Amer Sports","tier":"Global group","c":"United States"},
 "Titleist":{"own":"Acushnet Company","tier":"Global group","c":"United States"},
 "Scotty Cameron":{"own":"Acushnet Company","tier":"Global group","c":"United States"},
 "Head":{"own":"Head Austria GmbH","tier":"Independent","c":"Austria"},
 "Babolat":{"own":"Babolat","tier":"Independent","c":"France"},
 "Yonex":{"own":"Yonex","tier":"Independent","c":"Japan"},
 "Spalding":{"own":"Fruit of the Loom","tier":"Independent","c":"United States"},
 "Gilbert":{"own":"Grays International","tier":"Independent","c":"United Kingdom"},
 "Nike":{"own":"Nike, Inc.","tier":"Global group","c":"United States"},
 "Adidas":{"own":"Adidas AG","tier":"Global group","c":"Germany"},
 "Bauer Hockey":{"own":"Peak Achievement Athletics","tier":"Independent","c":"Canada"},
}
json.dump(p,open(f,'w'),ensure_ascii=False)
