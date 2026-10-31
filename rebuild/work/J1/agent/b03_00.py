import json,os
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,v=None,dt='',a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
DA="https://www.dartagnan.com/buy/comfort-foie-gras-poultry"
QC="https://www.quechoisir.org/enquete-signe-de-qualite-les-derives-du-label-rouge-n4729"
kinds=[
{"n":"Whole chicken","a":"roasting chicken · roaster","d":"A whole dressed chicken carcass for roasting, including poussin and capon.",
 "t":["standard","free-range","organic","corn-fed","poussin","poularde","capon"],
 "s":DA,
 "x":[X("Poulet de Bresse AOP","White Bresse Gauloise chickens from a zone of Ain, Jura and Saône-et-Loire, sold with head, blue legs and a ringed left leg; name protected since 1936.","","1957",W+"Poulet_de_Bresse",
        [{"n":"Poulet de Bresse","mk":"","y":"","d":"slaughtered at 4 months, at least 1.2 kg"},
         {"n":"Poularde de Bresse","mk":"","y":"","d":"slaughtered at 5 months, at least 1.8 kg"},
         {"n":"Chapon de Bresse","mk":"","y":"","d":"capon, 8 months or older, at least 3 kg"}],"type · weight",a="Bresse chicken · volaille de Bresse"),
      X("Label Rouge farmhouse chicken","French Label Rouge poulet fermier: slow-growing breeds, outdoor run, at least 81 days old (about twice a standard bird).","","1965",QC,
        [{"n":"Poulet fermier des Landes","mk":"Les Fermiers Landais","y":"1965","d":"corn-fed, free range 81 days; first Label Rouge"},
         {"n":"Poulet fermier de Loué","mk":"Fermiers de Loué","y":"1958 (group)","d":"Sarthe cooperative of Label Rouge poultry farmers"}],"region · feed · age",a="poulet fermier Label Rouge"),
      X("Ixworth chicken","English table breed created at Ixworth, Suffolk by Reginald Appleyard as a fast-growing, high-quality meat bird.","","1932",W+"Ixworth_chicken",[],"heritage breed · weight"),
      X("Capon (Vilalba and Lugo)","Castrated, fattened cockerels from Vilalba and Lugo in Galicia, sold across Spain at Christmas.","","",W+"Capon",[],"weight")],
 "m":[["Green Circle Chicken, whole","D'Artagnan"]],
 "dt":"breed · label · age · weight"},
{"n":"Chicken breast","a":"chicken fillet","d":"The breast meat of a chicken, on or off the bone, skin-on or skinless.",
 "t":["supreme (wing bone on)","fillet","mini fillets","on the bone"],
 "s":"https://boucheriesnivernaises.com/en/product-category/poultry/"},
{"n":"Chicken leg & thigh","a":"chicken leg · chicken thigh · drumstick","d":"The leg of a chicken, as whole leg quarters or as thighs and drumsticks.",
 "t":["leg quarter","thigh","drumstick"],
 "s":DA,
 "m":[["Green Circle Chicken, leg quarters","D'Artagnan"]]},
{"n":"Chicken wings","a":"wings","d":"The wings of a chicken, whole or as flats and drumettes, sold raw.",
 "t":["whole wing","flats","drumettes"],
 "s":"https://meatpeoplebutcher.com/price-list"},
{"n":"Poultry mince & burgers","a":"ground chicken · ground turkey · ground duck","d":"Raw minced poultry meat sold loose, packed or shaped into burgers.",
 "t":["chicken mince","turkey mince","duck mince","burgers"],
 "s":"https://hudsonvalleyfoiegras.com/collections/duck"},
]
brands=[
{"n":"D'Artagnan","c":"United States","f":"1985","seg":"Specialist","kf":"game & poultry","d":"US purveyor of poultry, game, foie gras and charcuterie.","lines":["Green Circle Chicken"],"eras":[],"sig":[],"sc":[],"rel":[],"s":"knowledge"},
{"n":"Les Fermiers Landais","c":"France","f":"1965","seg":"Institution & issuer","kf":"Landes Label Rouge poultry","d":"Saint-Sever producer group behind the corn-fed poulet fermier des Landes, the first Label Rouge.","lines":["Poulet fermier des Landes"],"eras":[],"sig":["Label Rouge farmhouse chicken"],"sc":[],"rel":[],"s":"https://www.tourismelandes.com/en/commerce-service/Landes-farmers-a0013aqu047v502zi9/"},
{"n":"Fermiers de Loué","c":"France","f":"1958","seg":"Institution & issuer","kf":"Label Rouge poultry","d":"Sarthe cooperative (Cafel) of about 1,200 Label Rouge poultry and egg farmers.","lines":[],"eras":[],"sig":["Label Rouge farmhouse chicken"],"sc":[],"rel":[],"s":"https://www.lejournaldesentreprises.com/breve/angelo-carbonel-est-le-nouveau-president-des-fermiers-de-loue-2144438"},
]
notes=("All five old kinds kept (k59 breast, k60 leg renamed 'Chicken leg & thigh', k61 wings, k62 whole, k67 'Ground duck' widened to 'Poultry mince & burgers'). "
"D'Artagnan 'Green Circle Chicken' range (repeated on two kinds) moved to one brand-register line; its two models kept as flat m. Old model 'Poulet de Bresse' became an archetype. "
"Left out: corn-fed and heritage breeds as archetypes (kept as types; Ixworth sourced), D'Artagnan founding year from knowledge.")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J1/shelves/03_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
