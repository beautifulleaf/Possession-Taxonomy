import json, os
RG='https://regenyei.com/feders/'; AL='https://myarmoury.com/review_alb_meyer.php'; RD='https://www.academyofhistoricalarts.co.uk/shop/red-dragon-synthetic-longsword'
BF='https://faitsdarmes.com/en/synthetic-longswords/259-black-fencer-longsword.html'; CG='https://cormnor.myportfolio.com/what-equipment-should-i-get-longsword'
HR='https://hroarr.com/reviews/review-spes-hema-jacket-axel-p-model/'; KA='https://kultofathena.com/product-category/hema/hema-swords'; SUB='https://ecsfencer.substack.com/p/fencing-kit-buying-guide'
def X(n,d,mk,y,s,v=(),dt='',a=''): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(n=a1,mk=b,y=c,d=e) for a1,b,c,e in v],"dt":dt}
kinds=[
{"n":"HEMA training sword","a":"waster · feder · federschwert · blunt trainer","d":"Blunt steel or synthetic sword made for sparring and drills in historical European martial arts (HEMA).",
 "t":["steel feder (federschwert)","steel blunt longsword","sabre","rapier","sidesword","messer","arming sword","synthetic (nylon or plastic)"],
 "s":"https://kultofathena.com/product-category/hema/hema-swords",
 "x":[X("Regenyei Standard Feder","Hungarian-made steel feder with a flexible, unsharpened blade and a schilt; long the community standard at HEMA events and clubs.","Regenyei","",RG,
        [("Short Feder","Regenyei","","shorter blade; spatulated tip"),("Tulip Feder","Regenyei","","Simple and Maestro versions"),("Trnava Feder","Regenyei","","parallel edges, robust build"),("Replica Feders","Regenyei","","based on museum originals"),("Tournament Saber","Regenyei","","sabre trainer")],"blade flex · pommel · guard (straight or rings)"),
      X("Albion Meyer","Blunt practice longsword with rounded point and winged schilt, named after Joachim Meyer's 1570 treatise; part of Albion's Maestro Line.","Albion Armorers","",AL,[],"high-carbon steel blade · stainless guard and pommel · hemp cord grip"),
      X("Castille MET Federschwert","American-made steel feder regarded as durable for rough sparring.","Castille Armory","",KA,[("Economy Longsword","Castille Armory","","")],""),
      X("Black Fencer synthetic longsword","Nylon longsword with steel guard and pommel, made to match a steel sword's weight and balance.","Black Fencer","",BF,[("Version 4","Black Fencer","","current version"),("Black Fencer Federschwert","Black Fencer","","feder form, stiffer blade")],"blade white or grey · grip rope natural or black"),
      X("Red Dragon synthetic longsword","Cheap plastic longsword with steel core and rubber grip for starting HEMA at home or club.","Red Dragon","",RD,[],"124 cm overall"),
      X("Purpleheart Pentti Meyer Federschwert","Synthetic feder with a stainless pommel, used as a club-standard trainer.","Purpleheart Armoury","",CG,[("Schiltless Pentti","Purpleheart Armoury","","without schilt, for Fiore"),("VB Feder","Purpleheart Armoury","","inexpensive steel feder")],"")],
 "m":[["Gothic Arming Sword","Fabri Armorum"],["Practical Bastard Sword","Kingston Arms"],["Sentry Longsword","Krieger Armory"],["Noestalgic Feder","Landsknecht Emporium"],["Volker type M5C Messer Blunt Trainer","Landsknecht Emporium"],["Gymnasium Saber","Viktor Berbekucz"],["Spatulated Tip Feder","Viktor Berbekucz"],["Standard Feder","Chlebowski"],["Ensifer Long","Ensifer"],["Fechtbuch Longsword Trainer","Arms & Armor"]]},
{"n":"HEMA fencing jacket","a":"HEMA gambeson","d":"Padded jacket made for HEMA, rated to a puncture resistance such as 350 N or 800 N where certified.",
 "t":["350 N","800 N","men's, women's","with rigid inserts","gambeson style"],
 "s":"https://faitsdarmes.com/en/brand/5-spes?page=2",
 "x":[X("SPES AP jacket","HEMA jacket developed with Axel Pettersson and the Swedish HEMA community; one of the first HEMA-specific jackets.","SPES","",HR,
        [("AP NG 800N HEMA Jacket","SPES","","800 N"),("AP Plus 350N HEMA Jacket","SPES","","350 N"),("AP PRO Plus 350N HEMA Jacket","SPES","","reinforced"),("AP Light","SPES","",""),("AP Light Pro","SPES","","rigid protection added")],"black, red, white · men's and women's cuts")],
 "m":[["Officer Jacket","SPES"],["FG Gambeson PRO 350N","SPES"],["Lynx Jacket","Lynx"]]},
{"n":"HEMA protective gloves","a":"HEMA gauntlets","d":"Padded or plated gloves that protect the hands from sword blows in HEMA sparring.",
 "t":["padded (soft)","hard-shell","lobster gauntlet","five-finger, three-finger (hoof) or mitten"],
 "s":"https://faitsdarmes.com/en/brand/5-spes?page=2",
 "x":[X("SPES Heavy Gloves","Heavily padded sparring gloves favoured by beginners, putting protection before dexterity.","SPES","",CG,[],"blast caps optional"),
      X("Sparring Gloves","Lightweight custom-made sparring gloves in five-finger, hoof or mitten styles.","Sparring Gloves","",CG,[],"custom fit")],
 "m":[["Lobster Shell Gloves V3","SPES"],["Visby Gauntlets","Visby"],["Progauntlet","Progauntlet"]]},
{"n":"HEMA chest protector","a":"plastron","d":"Rigid or padded chest guard worn under a HEMA jacket.",
 "t":["women's","men's","sports-bra integrated"],
 "s":"https://faitsdarmes.com/en/brand/5-spes?page=2",
 "m":[["Econoguard Women's Chest Protector","Leon Paul"],["Maxiguard","QP Sport"],["Body Protector Plastron (Level 2)","SPES"]]},
{"n":"HEMA gorget","a":"","d":"Rigid neck and throat guard worn for HEMA sparring.",
 "t":["under-jacket","articulated"],
 "s":"https://faitsdarmes.com/en/brand/5-spes?page=2",
 "m":[["Gorget","Destroyer Modz"],["Gorget","PBT"],["Gorget AR7013","Red Dragon"],["Articulated Gorget","Leon Paul"]]},
{"n":"HEMA fencing trousers","a":"","d":"Padded trousers or breeches made for HEMA sparring, with a puncture rating where given.",
 "t":["350 N","800 N","skirt"],
 "s":"https://faitsdarmes.com/en/brand/5-spes?page=2",
 "m":[["Locust Pants","SPES"],["Dragonfly","SPES"],["Hussar","SPES"],["Titan Breeches","Leon Paul"],["Fighting Pants","Lynx"]]},
]
K='knowledge'
brands=[
 {"n":"Regenyei","c":"Hungary","f":"","seg":"Artisan & independent","kf":"steel feders","d":"Hungarian armoury (Regenyei Armory) whose Standard Feder is widely used at HEMA events.","lines":["Standard Feder","Tulip Feder","Trnava Feder"],"eras":[],"sig":["Regenyei Standard Feder"],"sc":["HEMA"],"rel":[],"s":RG},
 {"n":"Albion Armorers","c":"United States","f":"","seg":"Artisan & independent","kf":"historical swords","d":"Wisconsin sword maker whose Maestro Line covers blunt practice swords.","lines":["Maestro Line"],"eras":[],"sig":["Albion Meyer"],"sc":["HEMA"],"rel":[],"s":AL},
 {"n":"Castille Armory","c":"United States","f":"","seg":"Specialist","kf":"HEMA trainers","d":"American maker of steel HEMA feders, rapiers and sabres.","lines":["Economy"],"eras":[],"sig":["Castille MET Federschwert"],"sc":["HEMA"],"rel":[],"s":CG},
 {"n":"Black Fencer","c":"","f":"","seg":"Specialist","kf":"synthetic swords","d":"Maker of nylon synthetic longswords and feders for HEMA.","lines":[],"eras":[],"sig":["Black Fencer synthetic longsword"],"sc":["HEMA"],"rel":[],"s":BF},
 {"n":"Red Dragon","c":"","f":"","seg":"Value","kf":"synthetic swords and HEMA kit","d":"Budget brand of synthetic swords, masks and HEMA protection.","lines":[],"eras":[],"sig":["Red Dragon synthetic longsword"],"sc":["HEMA"],"rel":[],"s":RD},
 {"n":"Purpleheart Armoury","c":"United States","f":"","seg":"Specialist","kf":"HEMA trainers","d":"HEMA supplier of synthetic and steel trainers, including the Pentti feder.","lines":[],"eras":[],"sig":["Purpleheart Pentti Meyer Federschwert"],"sc":["HEMA"],"rel":[],"s":CG},
 {"n":"SPES","c":"Poland","f":"","seg":"Specialist","kf":"HEMA protective gear","d":"HEMA protective-gear maker (SPES Historical Fencing Gear) known for the AP jacket.","lines":["AP","Locust","Hussar","Unity","Trinity"],"eras":[],"sig":["SPES AP jacket","SPES Heavy Gloves"],"sc":["HEMA"],"rel":[],"s":HR},
 {"n":"Sparring Gloves","c":"","f":"","seg":"Artisan & independent","kf":"HEMA gloves","d":"Maker of custom lightweight HEMA sparring gloves.","lines":[],"eras":[],"sig":["Sparring Gloves"],"sc":["HEMA"],"rel":[],"s":CG},
]
notes=("All 6 planned kinds kept. Swords organised as maker archetypes (Regenyei, Albion, Castille, Black Fencer, Red Dragon, Purpleheart) with old Kult of Athena models kept in m. "
 "Neyman jackets and the Albion Liechtenauer were not found on any retrieved page, so they are left out. Fencing-only brands (Leon Paul, PBT) appear in m only; their register entries are in shelf 13_00. "
 "SPES country from knowledge (not stated on hroarr page).")
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/E2/shelves/13_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
