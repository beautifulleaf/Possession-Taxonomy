import json, os
W='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"Meal kit and menu plan","a":"meal kit · recipe box · ready-meal plan · member-selected menu plan","d":"Recurring delivery whose contents the member picks from the provider's menu, such as meal kits or ready-made meals.",
 "t":["recipe kit (cook at home)","ready-made meals","budget kit","organic or diet-specific kit","weekly plan with skips"],
 "s":"https://www.findsubscriptionboxes.com/",
 "m":[["HelloFresh","HelloFresh"],["Factor","HelloFresh"],["Green Chef","HelloFresh"],["EveryPlate","HelloFresh"],["Home Chef","Home Chef"],["Blue Apron","Blue Apron"],["Gousto","Gousto"],["Marley Spoon","Marley Spoon"],["Dinnerly","Marley Spoon"]]},
{"n":"Curated subscription box","a":"provider-curated box · subscription box · beauty box · snack box","d":"Recurring box whose contents the provider picks around a theme.",
 "t":["beauty and skincare","snack and sweets","pet","kids and STEM","clothing styling","hobby and history","book"],
 "s":"https://www.findsubscriptionboxes.com/",
 "m":[["Birchbox","Birchbox"],["ipsy","ipsy"],["Allure Sample Society","Allure"],["FabFitFun VIP Box","FabFitFun"],["BarkBox","BarkBox"],["KiwiCo","KiwiCo"],["Stitch Fix","Stitch Fix"],["Universal Yums","Universal Yums"],["Try The World","Try The World"],["Mysteries in Time","Mysteries in Time"]]},
{"n":"Replenishment subscription","a":"subscribe and save · autoship · auto-replenishment","d":"Scheduled repeat delivery of everyday consumables, such as razor blades, pet food or groceries, usually at a discount.",
 "t":["shaving and grooming","pet food and supplies","household and grocery staples","delivery every few weeks or months"],
 "s":"https://sell.amazon.com/programs/subscribe-and-save",
 "m":[["Subscribe & Save","Amazon"],["Autoship","Chewy"],["Dollar Shave Club","Dollar Shave Club"]]},
{"n":"Producer club","a":"producer allocation club · wine club · winery club","d":"A producer's own club that allocates its goods to members on a schedule.",
 "t":["winery club","brewery club","distillery club","quarterly or seasonal shipment","allocation or waiting list"],
 "s":"https://www.aowinery.com/wine-club/",
 "m":[["Alpha Omega Wine Club","Alpha Omega Winery"],["Knights Bridge Curated Collection","Knights Bridge Winery"],["Tawse Wine Club","Tawse Estate Winery"]]},
{"n":"Rental subscription","a":"goods rental subscription · clothing rental","d":"Subscription lending goods to be used and returned, such as clothes, furniture, toys, instruments or art. The rented goods are not owned.",
 "t":["clothing","furniture","toys","musical instruments","art"],
 "s":"https://www.renttherunway.com/how_renting_works",
 "m":[["Rent the Runway","Rent the Runway"],["Nuuly","URBN"]]}
]
brands=[
 {"n":"HelloFresh","c":"Germany","f":"2011","seg":"Mainstream","kf":"meal kits","d":"Berlin meal-kit company that also owns Factor, Green Chef and EveryPlate.","lines":["Factor","Green Chef","EveryPlate"],"rel":["Marley Spoon","Blue Apron"],"s":W+"HelloFresh"},
 {"n":"Blue Apron","c":"United States","f":"2012","seg":"Mainstream","kf":"meal kits","d":"New York meal-kit company, owned by Wonder Group since 2023.","s":W+"Blue_Apron"},
 {"n":"Gousto","c":"United Kingdom","f":"2012","seg":"Mainstream","kf":"recipe boxes","d":"London recipe-box company delivering in Great Britain and Ireland.","s":W+"Gousto"},
 {"n":"Marley Spoon","c":"Germany","seg":"Mainstream","kf":"meal kits","d":"Berlin-born meal-kit company with the lower-priced Dinnerly line.","lines":["Dinnerly"],"s":"https://techcrunch.com/2017/07/11/dinnerly/amp/"},
 {"n":"Dollar Shave Club","c":"United States","f":"2011","seg":"Value","kf":"razor subscription","d":"Razor-blade subscription started in California, majority-owned by Nexus Capital with Unilever.","s":W+"Dollar_Shave_Club"},
 {"n":"Chewy","c":"United States","f":"2011","seg":"Own-label & retailer","kf":"pet supplies","d":"Online pet retailer whose Autoship repeat orders drive most of its sales.","lines":["Autoship"],"s":W+"Chewy_(company)"},
 {"n":"Rent the Runway","c":"United States","f":"2009","seg":"Premium","kf":"clothing rental","d":"New York designer-clothing rental service whose subscriptions make up most of its business.","rel":["Nuuly"],"s":W+"Rent_the_Runway"}
]
notes=("Dissolved 'Other curated boxes', 'Beauty box' and 'Snack box' into Curated subscription box with types; dropped Oisoy Asian Snack Box (minor single-shop seller). "
 "Meal kits add Factor, Green Chef, EveryPlate, Blue Apron, Gousto, Marley Spoon and Dinnerly; coffee and book menu plans stay as covered by the definition. "
 "Replenishment subscription is NEW (Amazon Subscribe & Save, Chewy Autoship, Dollar Shave Club); Harry's left out because the retrieved page did not confirm a subscription. Rental adds Nuuly (URBN). Producer club keeps its three old examples.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/I3/shelves/07_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
