import json, os
W='https://en.wikipedia.org/wiki/'
kinds=[
{"n":"Domestic staff via staffing agency","a":"household staff agency · private household recruitment · domestic staffing",
 "d":"Permanent or live-in household staff found and vetted by a specialist agency for a private home or estate.",
 "t":["housekeeper","house manager","butler","estate manager","nanny-housekeeper","couple (live-in)","private chef","chauffeur","yacht/chalet staff","temporary cover"],
 "s":W+"Domestic_worker",
 "m":[["Private household and estate staff placement (UK)","Greycoat Lumleys"],
      ["Luxury household staff recruitment and training (UK)","Polo & Tweed"],
      ["Household staff recruitment and butler training (UK)","Bespoke Bureau"],
      ["Residence, chalet and yacht staff recruitment (UK, US)","Silver Swan Recruitment"]]},
{"n":"Lifestyle concierge membership","a":"lifestyle management · personal concierge · concierge service",
 "d":"Retained personal-assistant service handling travel, restaurant, event and shopping requests for a member fee.",
 "t":["dedicated lifestyle manager","digital or app concierge","card-linked concierge (bank or card benefit)","corporate concierge benefit"],
 "s":W+"Quintessentially_Group",
 "m":[["Lifestyle management membership (UK)","Quintessentially"],
      ["Travel and lifestyle concierge (UK)","Ten Lifestyle Group"],
      ["Premium concierge and loyalty services (France)","John Paul"]]},
{"n":"Wellness and medical concierge","a":"concierge medicine · retainer medicine · private GP membership · boutique medicine",
 "d":"Annual or monthly fee for enhanced access to a doctor: same-day appointments, longer visits and direct contact.",
 "t":["concierge primary care (retainer)","private GP membership","concierge urgent and emergency care","executive health programme","wellness coaching retainer","family and paediatric plan"],
 "s":W+"Concierge_medicine",
 "m":[["Concierge primary-care membership (US)","MDVIP"],
      ["Primary-care membership (US)","One Medical"],
      ["Concierge urgent and emergency care membership (US)","Sollis Health"],
      ["My HCA GP / Flexible Care GP subscription (UK)","HCA Healthcare UK"],
      ["Annual GP, physio and mental-health membership (UK)","Doctor Care Anywhere"]]},
]
brands=[
{"n":"Greycoat Lumleys","c":"United Kingdom","seg":"Specialist","kf":"household staff","d":"UK agency placing nannies, maternity nurses and household staff with private clients for over 20 years.","s":"https://spears500.com/company/21/greycoat-lumleys"},
{"n":"Polo & Tweed","c":"United Kingdom","seg":"Specialist","kf":"luxury domestic staff","d":"Domestic staff recruitment and training firm founded by Lucy Challenger, placing butlers, nannies and household staff.","s":"https://www.countryandtownhouse.com/culture/polo-and-tweed/"},
{"n":"Bespoke Bureau","c":"United Kingdom","seg":"Specialist","kf":"household staff, butler training","d":"Luxury domestic staff recruitment and training agency founded by Sara Vestin Rahmani; runs The British Butler Academy.","s":"https://www.nannytax.co.uk/directory/bespoke-bureau"},
{"n":"Silver Swan Recruitment","c":"United Kingdom","f":"2013","seg":"Specialist","kf":"residence and yacht staff","d":"Household staff agency founded by Philippa Smith, starting with ski-chalet staff before residences and yachts; offices in London and Miami.","s":"https://spears500.com/adviser/23068/philippa-smith"},
{"n":"Quintessentially","c":"United Kingdom","f":"2000","seg":"Professional & flagship","kf":"lifestyle management","d":"London members-only lifestyle management and concierge service founded by Aaron Simpson, Ben Elliot and Paul Drummond.","s":W+"Quintessentially_Group"},
{"n":"Ten Lifestyle Group","c":"United Kingdom","f":"1998","seg":"Premium","kf":"travel and lifestyle concierge","d":"London concierge firm serving private and corporate members, including bank-card concierge programmes.","s":W+"Ten_Lifestyle_Group"},
{"n":"John Paul","c":"France","f":"2008","seg":"Premium","kf":"premium concierge","d":"Paris concierge and loyalty provider for luxury, finance and hospitality brands; Accor subsidiary since 2016.","s":"https://www.johnpaul.com/about-us/"},
{"n":"MDVIP","c":"United States","f":"2000","seg":"Professional & flagship","kf":"concierge primary care","d":"Boca Raton network of concierge physicians charging an annual membership on top of insurance.","s":W+"MDVIP"},
{"n":"One Medical","c":"United States","f":"2007","seg":"Mainstream","kf":"membership primary care","d":"San Francisco-founded membership primary-care provider, owned by Amazon since 2023 and offered with Prime.","s":W+"One_Medical"},
{"n":"Sollis Health","c":"United States","f":"2016","seg":"Premium","kf":"concierge emergency care","d":"New York membership urgent and emergency care clinics staffed by ER physicians.","s":"https://www.healthcare-brew.com/stories/2023/12/15/how-sollis-health-created-an-on-demand-emergency-room"},
{"n":"HCA Healthcare UK","c":"United Kingdom","seg":"Premium","kf":"private GP subscriptions","d":"Private hospital group offering My HCA GP and Flexible Care GP subscriptions with unlimited GP appointments.","s":"https://www.hcahealthcare.co.uk/private-gp-services"},
{"n":"Doctor Care Anywhere","c":"United Kingdom","seg":"Value","kf":"online GP membership","d":"UK online GP service with an annual membership covering GP, physiotherapy and mental-health consultations.","s":"https://doctorcareanywhere.com/membership-annual"},
]
notes=("New shelf, no old kinds. Staff roles are types (from the Wikipedia domestic-worker role list); butler schools (Ivor Spencer School, 1981; British Butler Academy) are criteria only, not kinds. "
"Card-issuer concierge is a type only. Executive health programmes kept as a type: the Mayo Clinic UK page returned 403, so no operator named. "
"Left out: Forward (concierge-medicine start-up, status not verified), SignatureMD and MD2 (only named on the Wikipedia article, current trading not checked). "
"Greycoat Lumleys founding year (1996) only seen in a search snippet, so omitted; Polo & Tweed and Bespoke Bureau founding years not found.")
p='work/I3/shelves/08_02.json'; json.dump({"kinds":kinds,"brands":brands,"traditions":[],"notes":notes},open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
