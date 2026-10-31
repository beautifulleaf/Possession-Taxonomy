import sys; sys.path.insert(0,'work/C3/agent'); from w import w
def X(n,a,d,s,y='',v=(),dt='',mk=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s}
    if dt: x["dt"]=dt
    if v: x["v"]=[dict(zip(("n","mk","y","d"),t)) for t in v]
    return x
WP="https://en.wikipedia.org/wiki/"
US05="https://shop.theelectricbrewery.com/pages/fermentis-safale-us-05-dry-yeast"
W001="https://shop.TheElectricBrewery.com/pages/white-labs-wlp001-california-ale-yeast"
W002="https://shop.theelectricbrewery.com/pages/white-labs-wlp002-english-ale-yeast"
W3470="https://midwestsupplies.com/products/saflager-w-34-70-11-5-grams"
ICH="https://www.immateriellkulturarv.no/en/bidrag/traditional-farmhouse-brewing-with-kveik-in-western-norway/"
BYO="https://byo.com/article/kveik-norwegian-farmhouse-yeast-head"
VOSS="https://www.lallemandbrewing.com/en/south-america/products/lalbrew-voss-kveik-ale-yeast/"
S565="https://www.whitelabs.com/yeast-bank/wlp565-belgian-saison-i-ale-yeast"
EC="https://lallemandwine.com/en/united-kingdom-ireland/products/wine-yeasts/lalvin-ec1118-prise-de-mousse"
AAB="https://allaboutbeer.com/article/homebrewing-with-brettanomyces/"
WL,WY,FE,LA,OM="White Labs","Wyeast Laboratories","Fermentis","Lallemand","Omega Yeast"
DT="form (liquid, dry) · pack size · attenuation · temperature range"
kinds=[
 {"n":"Ale yeast","a":"top-fermenting yeast · Saccharomyces cerevisiae","d":"Living ale yeast culture, liquid or dried, kept or bought to ferment beer at home.","t":["liquid","dry","slant","harvested"],
  "s":"https://www.williamsbrewing.com/Home-Brewing-Supplies/Yeast/White-Labs-Liquid-Ale-Yeast/WLP001-California-Ale-Next-Generation","x":[
  X("Chico (American ale)","California ale · American ale","Clean, versatile Sierra Nevada Chico strain found in beers across America, sold by several labs.",US05,dt=DT,
    v=[("WLP001 California Ale",WL,"","liquid; Sierra Nevada as possible source"),("Wyeast 1056 American Ale",WY,"","liquid"),("SafAle US-05",FE,"","dry; formerly US-56")]),
  X("English ESB ale","London ESB · English ale","Very flocculent English bitter strain leaving clear beer with some sweetness; Fuller's a possible source.",W002,dt=DT,
    v=[("WLP002 English Ale",WL,"","liquid; milds, bitters, porters, stouts")]),
 ],"m":[["WLP060 American Ale Blend",WL],["WLP067 Coastal Haze Ale",WL]]},
 {"n":"Lager yeast","a":"bottom-fermenting yeast · Saccharomyces pastorianus","d":"Living lager yeast culture, liquid or dried, fermenting cool to make lagers at home.","t":["liquid","dry"],"s":W3470,"x":[
  X("Weihenstephan 34/70","W-34/70","German lager strain from Weihenstephan, clean and malt-forward.",W3470,dt=DT,
    v=[("SafLager W-34/70",FE,"","dry; 11.5 g sachet; 9–20 °C")]),
 ]},
 {"n":"Kveik & farmhouse yeast","a":"kveik · Norwegian farmhouse yeast · saison yeast","d":"Living farmhouse ale yeast, including Norwegian kveik that ferments very hot and fast and Belgian saison strains.","t":["liquid","dry","dried flakes or yeast ring"],
  "s":ICH,"x":[
  X("Voss kveik","","Kveik from Sigmund Gjernes of Voss, Norway, kept by traditional methods since the 1980s; neutral with orange notes at 35–40 °C.",VOSS,dt=DT,
    v=[("LalBrew Voss",LA,"","dry; 11 g and 500 g")]),
  X("Hornindal kveik","","Saccharomyces cerevisiae kveik from Hornindal in western Norway.",BYO,dt=DT),
  X("Stranda kveik","","Saccharomyces cerevisiae kveik from Stranda, Norway.",BYO,dt=DT),
  X("Muri kveik","","Kveik named for brewer Bjarne Muri, giving a clean tartness.",BYO,dt=DT),
  X("HotHead","OYL-057","Kveik strain from Omega adding orange notes, fermented around 32 °C.",BYO,mk=OM,dt=DT),
  X("Belgian saison (Wallonia)","Saison I","Classic Walloon saison strain giving earthy, peppery, spicy character; STA1 positive.",S565,dt=DT,
    v=[("WLP565 Belgian Saison I Ale",WL,"","liquid; 20–30 °C")]),
 ]},
 {"n":"Wild & souring cultures","a":"Brett · wild yeast · sour cultures","d":"Living Brettanomyces, Lactobacillus or Pediococcus cultures used for wild, sour and lambic-style beers.","t":["Brettanomyces","Lactobacillus","Pediococcus","mixed blend"],"s":AAB,"x":[
  X("Brettanomyces claussenii","B. anomalus","First Brettanomyces, isolated by Niels Hjelte Claussen from an English stock ale in 1903.",AAB,y="1903",v=[("WLP645",WL,"","")]),
  X("Brettanomyces bruxellensis","","Brett most associated with lambic and Flanders beers.",AAB,v=[("WLP650",WL,"",""),("Wyeast 5112",WY,"",""),("WLP644 B. bruxellensis Trois",WL,"","popular as a primary strain")]),
  X("Brettanomyces lambicus","","Brett strain for lambic-style beers.",AAB,v=[("WLP653",WL,"",""),("Wyeast 5526",WY,"","")]),
 ]},
 {"n":"Wine, cider & mead yeast","a":"","d":"Living liquid or dried yeast culture kept or bought to ferment wine, cider or mead at home.","t":["liquid","dry"],
  "s":"https://morebeer.com/products/white-labs-yeast-wlp715-champagne-wine-cider-mead-purepitchreg-generation-industry-leading-viability-150-billion-cells","x":[
  X("EC-1118 (Prise de Mousse)","champagne yeast","Saccharomyces cerevisiae bayanus isolated in Champagne; for sparkling secondary fermentation, cider, fruit wine and stuck ferments; to 18%.",EC,mk=LA,
    v=[("Lalvin EC-1118",LA,"","dry; 10–30 °C")]),
 ],"m":[["WLP715 Champagne",WL],["Wyeast 4946 Bold Red",WY]]},
 {"n":"Algae culture","a":"microalgae culture","d":"Living algae culture kept to grow or propagate.","t":["starter culture","live culture"],"s":"https://algaeresearchsupply.com/collections/algae-cultures","x":[
  X("Spirulina","Arthrospira platensis · Limnospira","Cyanobacterium grown in alkaline water at about 30 °C, mostly in raceway ponds.",WP+"Spirulina_(dietary_supplement)",v=[("Algae Culture Arthrospira platensis (Spirulina)","Algae Research Supply","","")]),
  X("Chlorella vulgaris","","Green unicellular microalga described by Beijerinck in 1890, sold as a supplement.",WP+"Chlorella_vulgaris",y="1890",v=[("Algae Culture Chlorella vulgaris","Algae Research Supply","","")]),
 ],"m":[["Algae Culture Isochrysis galbana","Algae Research Supply"],["Algae Culture Nannochloropsis sp.","Algae Research Supply"],["Algae Culture Tetraselmis chuii","Algae Research Supply"]]},
]
brands=[
 {"n":"White Labs","c":"United States","f":"1995","seg":"Specialist","kf":"liquid brewing yeast","d":"San Diego yeast lab selling liquid and dry brewing and wine yeasts.","sig":["WLP001 California Ale","WLP002 English Ale"],"s":"knowledge"},
 {"n":"Wyeast Laboratories","c":"United States","seg":"Specialist","kf":"liquid brewing yeast","d":"Oregon yeast lab known for liquid brewing yeasts in smack packs.","sig":["Wyeast 1056 American Ale"],"s":"knowledge"},
 {"n":"Fermentis","c":"France","seg":"Specialist","kf":"dry brewing yeast","d":"Lesaffre's fermentation business selling dry brewing yeasts.","sig":["SafAle US-05","SafLager W-34/70"],"s":"knowledge"},
 {"n":"Lallemand","c":"Canada","f":"1915","seg":"Specialist","kf":"dry yeast","d":"Montreal yeast and bacteria maker; LalBrew brewing and Lalvin wine yeasts.","lines":["LalBrew","Lalvin"],"sig":["LalBrew Voss","Lalvin EC-1118"],"s":"knowledge"},
 {"n":"Omega Yeast","c":"United States","seg":"Specialist","kf":"liquid yeast, kveik","d":"US liquid-yeast lab, maker of the HotHead kveik strain.","sig":["HotHead"],"s":BYO},
]
trads=[{"n":"Norwegian farmhouse brewing with kveik","g":"Food & drink","r":"Western Norway (Hordaland, Sogn og Fjordane, Møre og Romsdal)","p":"over 1,000 years","d":"Farm brewing of juniper-infused ale with each farm's own kveik yeast, passed down in families.",
 "tech":"juniper infusion, long boil or raw ale, warm fermentation of about 48 hours","mat":"malted barley, juniper, hops, kveik","forms":["Kveik & farmhouse yeast"],
 "ctr":["Voss","Hornindal (Kornøl festival)","Stranda"],"auth":"kveik kept on yeast rings, wooden logs or as dried flakes; strains named for farm or brewer","s":ICH}]
w('C3','10_02',{"kinds":kinds,"brands":brands,"traditions":trads,"notes":"Three old kinds kept with old s; lager, kveik/farmhouse and wild/souring kinds added. Chico strain versions by lab (WLP001, 1056, US-05) from The Electric Brewery page. Liquid equivalents of W-34/70 and Wyeast saison/1968 not added (only forum sources). No Lactobacillus product page retrieved, so souring bacteria are types only. Algae trimmed to Spirulina and Chlorella archetypes; other old cultures kept in m. Baker's yeast stays in J5."})
