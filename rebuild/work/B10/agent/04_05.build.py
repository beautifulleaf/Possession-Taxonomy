import json,os
K=[]
K.append({"n":"Compound horse feed","a":"hard feed · concentrate · coarse mix · horse nuts · cubes · balancer",
 "d":"Manufactured concentrate feed for horses, as pellets, cubes, coarse mix, mash or balancer; complete or top-up.",
 "t":["cubes / nuts / pellets","coarse mix / muesli","mash","ration balancer","high-fibre / chaff-based","senior","stud and youngstock","performance / racing","low-starch / laminitis-safe","complete feed"],
 "s":"https://www.trouwnutrition.ca/en-ca/product-lister-equiline/",
 "m":[["Spillers Original Balancer","Spillers"],["Spillers Lite & Lean Balancer","Spillers"],["Spillers Happy Hoof","Spillers"],["Spillers Senior Super-Mash","Spillers"],["Spillers Horse & Pony Cubes","Spillers"],["Spillers HDF Power Cubes","Spillers"],
      ["No.4 Top Line Conditioning Cubes","Baileys Horse Feeds"],["No.14 Lo-Cal Balancer","Baileys Horse Feeds"],["No.15 Senior Mix","Baileys Horse Feeds"],
      ["Purina Equine Senior","Purina"],["Purina Omolene #400 Complete Advantage","Purina"],["Purina Enrich Plus","Purina"],
      ["Triple Crown Senior","Triple Crown"],["Triple Crown Complete","Triple Crown"],["Triple Crown Balancer","Triple Crown"],["Triple Crown Lite","Triple Crown"],
      ["Re-Leve Mix","Saracen Horse Feeds"],["Harbro Horse & Pony Nuts","Harbro"],["Harbro Horse & Pony Conditioning Mix","Harbro"]]})
K.append({"n":"Horse supplement","a":"feed supplement · equine supplement","d":"A nutritional supplement added to a horse's feed for joints, hooves, coat, digestion, calm behaviour or electrolytes.",
 "t":["joint","hoof","calmer","electrolyte","digestive / gut","respiratory","coat and skin","vitamin and mineral","senior","herbal"],
 "s":"https://australianmade.com.au/licensees/the-hoof-co/hoof-pack",
 "m":[["Spillers Flex Supplement","Spillers"],["Spillers Hoof Health Supplement","Spillers"],["Spillers Calm Supplement","Spillers"],["Spillers Ventil-Ate","Spillers"],
      ["Nutramax Cosequin ASU for horses","Nutramax"],["Nutramax Cosequin Original for horses","Nutramax"],
      ["Harbro Joint Care","Harbro"],["Harbro Hoof Care","Harbro"],["Harbro One Scoop","Harbro"],
      ["Dodson & Horrell Electrolytes For Horses & Ponies","Dodson & Horrell"],["Dodson & Horrell Mobility","Dodson & Horrell"],["Dodson & Horrell Placid Horse Calmer","Dodson & Horrell"],["Dodson & Horrell Daily Vitamins & Minerals","Dodson & Horrell"],
      ["Purina Outlast Gastric Support Horse Supplement","Purina"],["Baileys Keep Calm","Baileys Horse Feeds"],["Baileys Aqua-Aide","Baileys Horse Feeds"]]})
K.append({"n":"Hay","a":"forage · haylage","d":"Grass or legumes cut and dried for storage as feed for horses, rabbits, guinea pigs and other animals.",
 "t":["meadow hay","timothy","orchard grass","alfalfa (lucerne)","haylage","compressed bale","chopped forage / chaff","hay cubes"],
 "s":"https://en.wikipedia.org/wiki/Hay",
 "m":[["Burgess Excel Timothy Hay","Burgess Pet Care"],["Burgess Excel Long Stem Timothy Forage Hay","Burgess Pet Care"],["Oxbow Western Timothy Hay","Oxbow Animal Health"],["Full Cheeks Natural Timothy Hay","Full Cheeks"],
      ["Standlee Compressed Bale","Standlee Forage"],["Standlee Alfalfa Orchard Grass compressed bale","Standlee Forage"],
      ["Triple Crown Premium Grass Forage","Triple Crown"],["Triple Crown Naturals Timothy Balance Cubes","Triple Crown"],["Triple Crown Naturals Alfalfa Cubes","Triple Crown"]],
 "r":[["Burgess Excel","Burgess Pet Care"]]})
K.append({"n":"Hay net","a":"haynet · hay bag · slow feeder","d":"A net, bag or rack of rope, mesh or bars that holds hay for a horse to pull from.",
 "t":["standard haynet","slow-feed (small-hole) net","hay bag","wall hay rack","corner hay rack","ground-level feeding station"],
 "s":"https://australianmade.com.au/licensees/nhay",
 "m":[["Trickle Net Softee","Trickle Net"],["Trickle Net Shake & Graze Chaff Net","Trickle Net"],["Shires Soft Mesh Haynet","Shires"],["LeMieux Hungry Hippo Haynet","LeMieux"],["Hy Equestrian Slow Flow Ultra Haynet","Hy Equestrian"],
      ["Elico Little Piggy Haynet","Elico"],["Equilibrium PortionPacer","Equilibrium"],["KM Elite Elim-a-net","KM Elite"],["Nibbleze Haynet","Nibbleze"],["Stubbs Haysaver Wall Rack S14","Stubbs"]]})
K.append({"n":"Salt and mineral lick","a":"salt block · mineral block · lick · rock salt lick","d":"A block of salt or minerals that a horse or other livestock licks for sodium and trace minerals.",
 "t":["white salt block","mineral block","Himalayan rock salt","rock salt on rope","flavoured treat lick","lick holder"],
 "s":"https://en.wikipedia.org/wiki/Salt_lick",
 "m":[["Tough1 Himalayan Rock Horse Salt Block","Tough 1"],["Tough1 Himalayan Rock Salt on Rope","Tough 1"],["Jolly Stall Snack Himalayan Rock Salt Refill","Horsemen's Pride"],["Dodson & Horrell Uniblock Mineral Lick","Dodson & Horrell"],["Harbro Horse & Pony Grass Block","Harbro"],["Stubbs Standard Salt Lick Holder (S25PE)","Stubbs"]]})
K.append({"n":"Feed bucket and manger","a":"feed tub · manger · corner feeder · stable bucket","d":"A bucket, tub or fixed rack from which a horse eats its hard feed or fodder.",
 "t":["hanging bucket","flat-sided bucket","ground feed tub","corner manger","portable manger","swivelling manger","foal feeder"],
 "s":"https://en.wikipedia.org/wiki/Manger",
 "m":[["Stubbs Large Portable Manger (S5L)","Stubbs"],["Stubbs Plastic Portable Manger (S5PE)","Stubbs"],["Stubbs Swivelling Manger (S300)","Stubbs"],["Stubbs Large Feed Tub (S44AFT)","Stubbs"],["Stubbs Stable Bucket - Large (S85A)","Stubbs"],["Stubbs Jumbo Feed/Water Bucket (S43)","Stubbs"]]})
K.append({"n":"Horse treats","a":"horse cookies · horse biscuits · lick treats","d":"Small biscuits, nuggets or licks given to a horse as a reward or to keep it occupied.",
 "t":["biscuits / cookies","nuggets","hanging lick","stable toy refill","medication-hiding treat"],
 "s":"https://jefferspet.com/collections/horse-treats-toys",
 "m":[["Likit Refill","Likit"],["Likit Boredom Buster","Likit"],["Mrs. Pastures Horse Cookies","Mrs. Pastures"],["Stud Muffins Horse Treats","Stud Muffins"],["Purina Nicker Makers","Purina"],["Manna Pro Bite-Size Nuggets","Manna Pro"],["Jolly Stall Snack Refills","Horsemen's Pride"],["Spillers Meadow Herb Treats","Spillers"],["Spillers Apple Treats","Spillers"],["Baileys Tasty Treats","Baileys Horse Feeds"],["Dodson & Horrell Carrot & Mint Treats","Dodson & Horrell"]]})
B=[
 {"n":"Spillers","c":"United Kingdom","seg":"Horse feed","d":"UK horse feed brand of Mars Horsecare.","lines":["HDF","Ulca","Happy Hoof","Senior"],"rel":["Mars Horsecare"],"s":"https://millbryhill.co.uk/collections/brand-spillers-horse-feeds"},
 {"n":"Baileys Horse Feeds","c":"United Kingdom","seg":"Horse feed","d":"Essex feed miller selling a numbered range of horse cubes, mixes and balancers.","lines":["No.4 Top Line","No.14 Lo-Cal","Speedi-Beet"],"s":"https://madbarn.com/brand/baileys-horse-feeds/"},
 {"n":"Dodson & Horrell","c":"United Kingdom","seg":"Horse feed and supplements","d":"British horse feed and supplement maker.","s":"https://tannertrading.co.uk/dodson-and-horrell/"},
 {"n":"Purina","c":"United States","seg":"Horse feed","d":"US animal feed maker (Purina Animal Nutrition) whose horse range includes Omolene, Equine Senior and Ultium.","lines":["Omolene","Equine Senior","Ultium","Enrich Plus"],"s":"https://shop.purinamills.com/collections/horse-products/special-needs"},
 {"n":"Triple Crown","c":"United States","seg":"Horse feed","d":"US horse feed brand known for beet-pulp senior and low-starch feeds.","lines":["Senior","Naturals","Diamond"],"s":"https://madbarn.com/brand/triple-crown/"},
 {"n":"Saracen Horse Feeds","c":"United Kingdom","seg":"Horse feed","d":"British performance horse feed maker; Re-Leve is its low-starch range.","lines":["Re-Leve"],"s":"https://madbarn.com/feeds/re-leve-mix-saracen-horse-feeds/"},
 {"n":"Stubbs","c":"United Kingdom","seg":"Stable equipment","d":"British maker of stable mangers, buckets, hay racks and lick holders.","s":"https://watermanscountrysupplies.co.uk/stubbs/"},
 {"n":"Likit","seg":"Horse treats and stable toys","d":"Brand of hanging lick treats and boredom-buster stable toys for horses.","s":"https://jefferspet.com/collections/horse-treats-toys"}]
notes=("Kept all 4 old kinds; added Salt and mineral lick, Feed bucket and manger, Horse treats (new, sourced). Tier shelf: no archetypes. "
 "Compound feed cut from 39 SKUs (33 Spillers, 6 Harbro) to 19 across Spillers, Baileys, Purina, Triple Crown, Saracen, Harbro; feed forms moved to t. "
 "Supplements trimmed (Cosequin variants, Spillers Instant Energy, Harbro Lami Care dropped) and D&H, Purina, Baileys added; types joint/hoof/calmer/electrolyte etc. "
 "Hay kept old Burgess/Oxbow/Standlee models plus Triple Crown forage; Grab & Go bale dropped as SKU duplicate. "
 "Spillers Ulca, Stamina+, Racehorse and Stud lines left out as SKU noise. Wynnstay retailer page 403 so not used. No traditions apply.")
out={"kinds":K,"brands":B,"traditions":[],"notes":notes}
p='work/B10/shelves/04_05.json'; json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
