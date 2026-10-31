import json, os
W='https://en.wikipedia.org/wiki/'
K=[]
def k(n,a,d,s,t=None,m=None,x=None):
    o={"n":n,"a":a,"d":d}
    if t: o["t"]=t
    o["s"]=s
    if x: o["x"]=x
    if m: o["m"]=m
    K.append(o)
def X(n,a,d,mk,y,s,v,dt): return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[{"n":a1,"mk":b,"y":c,"d":e} for a1,b,c,e in v],"dt":dt}
k("Energy drink","energy drink · energy tonic","Caffeinated soft drink, often with taurine and B vitamins, sold to reduce tiredness.",W+"Energy_drink",
  t=["regular","sugar-free / zero","flavoured edition","tonic bottle (non-carbonated)","high-caffeine fitness drink","coffee-energy hybrid"],
  x=[X("Lipovitan D","Lipovitan · Libogen · Livita","Small-bottle Japanese taurine tonic, the model for Asian energy drinks.","Taisho Pharmaceutical","1962",W+"Lipovitan",
       [("Lipovitan D","Taisho Pharmaceutical","1962","Flagship, 1,000 mg taurine"),("Lipovitan D Super","Taisho Pharmaceutical","","2,000 mg taurine"),("MAXIO","Taisho Pharmaceutical","","3,000 mg taurine")],"100 ml brown bottle · taurine strength"),
     X("Krating Daeng","Thai Red Bull","Thai sweet non-carbonated energy tonic from which Red Bull was adapted.","TCP Group","1976",W+"Krating_Daeng",[],"small glass bottle or can"),
     X("Red Bull","Red Bull Energy Drink","Carbonated taurine energy drink in a 250 ml can that defined the Western energy category.","Red Bull","1987",W+"Red_Bull",
       [("Red Bull Energy Drink","Red Bull","1987","Original, launched in Austria"),("Red Bull Sugarfree","Red Bull","2003","First variant"),("Red Bull Total Zero","Red Bull","2012","Zero-calorie"),("Red Bull Editions","Red Bull","2013","Flavoured line"),("Red Bull Zero","Red Bull","2018","Sugar-free, closer to original taste")],"250 ml can and larger · original, sugar-free, editions"),
     X("Monster Energy","Monster","Large-can American energy drink with a claw-mark logo, launched by Hansen Natural.","Monster Beverage","2002",W+"Monster_Energy",
       [("Monster Energy (original)","Monster Beverage","2002","Released 18 April 2002"),("Zero Ultra","Monster Beverage","","Zero-sugar 'White Monster'"),("Juice Monster","Monster Beverage","","Fruit-juice line, e.g. Pacific Punch"),("Java Monster","Monster Beverage","","Coffee-energy line")],"16 oz / 500 ml can · flavour lines"),
     X("Rockstar","Rockstar Energy","American large-can energy drink founded by Russell Weiner.","Rockstar","2001","https://en.wikipedia.org/wiki/Rockstar_(drink)",[],"can size · flavour"),
     X("Celsius","Celsius Live Fit","Sugar-free fitness energy drink with 200–270 mg caffeine per can.","Celsius Holdings","2004",W+"Celsius_Holdings",
       [("Celsius Live Fit","Celsius Holdings","","Core line"),("Celsius Essentials","Celsius Holdings","","Higher-caffeine line"),("Celsius On-The-Go","Celsius Holdings","","Powder sticks")],"12 oz can · flavour"),
     X("Prime Energy","","Caffeinated spin-off of the Prime brand launched by Logan Paul and KSI.","Prime Hydration","2023","https://en.wikipedia.org/wiki/Prime_(drink)",[],"can · flavour")],
  m=[["Lucozade Energy","Lucozade"],["Alani Nu","Celsius Holdings"],["V8 Energy","Campbell's"]])
k("Energy shot","energy shot · 2 oz shot","Concentrated energy drink of about 50–60 ml with caffeine and B vitamins, taken in one swallow.",W+"5-hour_Energy",
  t=["regular strength","extra strength","decaf"],
  x=[X("5-hour Energy","","American 2 oz energy shot of caffeine and B vitamins, the best-known energy shot.","Living Essentials","2004",W+"5-hour_Energy",[],"2 oz bottle · strength · flavour")],
  m=[["Red Bull Energy Shot","Red Bull"]])
k("Mate soda","mate soda · yerba mate soda · Mate-Limonade","Carbonated soft drink flavoured and caffeinated with yerba mate extract.",W+"Club-Mate",
  t=["original","sugar-free","flavoured (pomegranate, cola)","winter spiced edition"],
  x=[X("Club-Mate","Club Mate","Lightly sweet carbonated mate drink from Franconia, a fixture of hacker and club culture.","Brauerei Loscher","1924",W+"Club-Mate",
       [("Sekt-Bronte","Geola Beverages","1924","Original drink, Dietenhofen"),("Club-Mate","Brauerei Loscher","1994","Marketed as Club-Mate"),("Winter Edition","Brauerei Loscher","2007","Spiced seasonal edition"),("Club-Mate Cola","Brauerei Loscher","2009","Cola with mate extract"),("Granat","Brauerei Loscher","2013","Pomegranate"),("Zero","Brauerei Loscher","2022","Sugar-free")],"0.5 l or 0.33 l glass bottle"),
     X("Materva","","Sweet carbonated Cuban yerba mate soda, produced in Miami since the 1960s.","","1920","https://en.wikipedia.org/wiki/Mate_(drink)",[],"bottle or can")],
  m=[["Sol Mate","Sol Mate"]])
k("Sports drink","sports drink · isotonic drink · electrolyte drink","Non-caffeinated drink of water, sugar and salts to replace fluid and energy during or after exercise.",W+"Sports_drink",
  t=["isotonic","hypotonic","hypertonic","low-sugar / zero","powder to mix"],
  x=[X("Gatorade","","The original sports drink, created at the University of Florida for its football team.","Gatorade","1965",W+"Gatorade",
       [("Gatorade Thirst Quencher","Stokely-Van Camp","1965","Original formula"),("Gatorade Frost","Gatorade","1997","Sub-line"),("G2","Gatorade","2007","Low-calorie"),("Gatorlyte","Gatorade","2021","Five-electrolyte blend")],"bottle size · flavour · powder"),
     X("Lucozade Sport","Lucozade","British glucose drink, created as Glucozade in 1927 and rebranded for sport and energy in 1983.","Lucozade","1927",W+"Lucozade",
       [("Glucozade","W. Owen & Son","1927","Original glucose drink, Newcastle"),("Lucozade Energy / Sport rebrand","Beecham Group","1983","Repositioned for energy and sport"),("Lucozade Zero","Lucozade","","Sugar-free")],"bottle · flavour"),
     X("Powerade","","Coca-Cola's sports drink, the main rival to Gatorade.","Powerade","1988",W+"Powerade",[("Powerade","Coca-Cola","1988","Original"),("Powerade Zero","Coca-Cola","2007","No sugar or calories")],"bottle · flavour"),
     X("Pocari Sweat","","Japanese 'ion supply' drink with a mild, slightly salty taste, widely sold across Asia.","Otsuka Pharmaceutical","1980",W+"Pocari_Sweat",[("Pocari Sweat","Otsuka Pharmaceutical","1980","Original"),("Pocari Sweat Ion Water","Otsuka Pharmaceutical","","Reduced-sugar")],"can, bottle or powder"),
     X("BodyArmor","Bodyarmor SuperDrink","Coconut-water-based sports drink sold as a natural rival to Gatorade, owned by Coca-Cola since 2021.","BodyArmor","2011",W+"Bodyarmor_SuperDrink",[("SuperDrink","BodyArmor","2011","Original"),("Lyte","BodyArmor","","Lower sugar"),("SportWater","BodyArmor","","Alkaline electrolyte water")],"bottle · flavour"),
     X("Prime Hydration","Prime","Influencer-launched electrolyte sports drink with coconut water, a 2022–23 craze.","Prime Hydration","2022","https://en.wikipedia.org/wiki/Prime_(drink)",[("Prime Hydration","Prime Hydration","2022","Launch"),("Prime Hydration+ Sticks","Prime Hydration","2022","Powder sticks")],"bottle · flavour")],
  m=[["Aquarius","Coca-Cola"],["Isostar","Isostar"]])
k("Electrolyte drink & tablets","electrolyte tablets · hydration powder · drink mix","Tablets and powder sticks of salts, sometimes with sugar, dissolved in water for everyday or sport hydration.","https://nuunlife.com/company",
  t=["effervescent tablet","powder stick","zero sugar","with caffeine","with vitamins"],
  m=[["Nuun Sport","Nuun"],["Nuun Zero Sugar","Nuun"],["Liquid I.V. drink mix","Liquid I.V."],["Prime Hydration+ Sticks","Prime Hydration"],["Gatorlyte","Gatorade"],["Flash I.V. Sticks","BodyArmor"],["Celsius On-The-Go","Celsius Holdings"]])
k("Protein & recovery drink","protein shake · RTD protein · recovery drink","Ready-to-drink milk- or plant-based shake with added protein for training recovery or meals.",W+"Muscle_Milk",
  t=["milk protein","plant protein","high-protein low-sugar","chocolate milk recovery"],
  m=[["Muscle Milk","CytoSport"],["Prime Protein","Prime Hydration"]])
k("Functional & vitamin drink","vitamin water · enhanced water · functional beverage","Drinks sold for added vitamins, electrolytes or claimed effects, such as enhanced waters and 'smart' drinks.",W+"Functional_beverage",
  t=["vitamin water","enhanced water","nootropic / 'smart' drink","adaptogen drink","relaxation drink"],
  x=[X("Vitaminwater","Glacéau Vitaminwater","Flavoured enhanced water with added vitamins from Glacéau, owned by Coca-Cola since 2007.","Glacéau","2000",W+"Vitaminwater",[],"bottle · flavour · zero")],
  m=[["Smartwater","Glacéau"]])
B=[
 {"n":"Taisho Pharmaceutical","c":"Japan","seg":"Pharmaceuticals & tonics","d":"Japanese drug maker that created Lipovitan D.","sig":["Lipovitan D"],"s":W+"Lipovitan"},
 {"n":"TCP Group","c":"Thailand","seg":"Energy drinks","d":"Thai maker of Krating Daeng, founded by Chaleo Yoovidhya as T.C. Pharmaceutical.","sig":["Krating Daeng"],"rel":["Red Bull"],"s":W+"Krating_Daeng"},
 {"n":"Red Bull","c":"Austria","f":"1984","seg":"Energy drinks","d":"Fuschl am See company of Dietrich Mateschitz and Chaleo Yoovidhya; drink launched 1987.","lines":["Sugarfree","Zero","Editions"],"sig":["Red Bull"],"rel":["TCP Group"],"s":W+"Red_Bull"},
 {"n":"Monster Beverage","c":"United States","seg":"Energy drinks","d":"Corona, California company, formerly Hansen Natural, maker of Monster Energy.","lines":["Zero Ultra","Juice Monster","Java Monster"],"sig":["Monster Energy"],"s":W+"Monster_Energy"},
 {"n":"Rockstar","c":"United States","f":"2001","seg":"Energy drinks","d":"Energy-drink brand founded by Russell Weiner; owned by PepsiCo since 2020.","sig":["Rockstar"],"s":"https://en.wikipedia.org/wiki/Rockstar_(drink)"},
 {"n":"Celsius Holdings","c":"United States","f":"2004","seg":"Fitness energy drinks","d":"Boca Raton maker of Celsius; agreed to buy Alani Nu in 2025.","lines":["Live Fit","Essentials","Alani Nu"],"sig":["Celsius"],"s":W+"Celsius_Holdings"},
 {"n":"Prime Hydration","c":"United States","f":"2022","seg":"Sports & energy drinks","d":"Drinks brand launched by Logan Paul and KSI with Congo Brands.","lines":["Prime Hydration","Prime Energy"],"sig":["Prime Hydration","Prime Energy"],"s":"https://en.wikipedia.org/wiki/Prime_(drink)"},
 {"n":"Living Essentials","c":"United States","seg":"Energy shots","d":"Maker of 5-hour Energy, founded by Manoj Bhargava.","sig":["5-hour Energy"],"s":W+"5-hour_Energy"},
 {"n":"Brauerei Loscher","c":"Germany","seg":"Brewery & soft drinks","d":"Münchsteinach brewery that has made Club-Mate since 1994.","sig":["Club-Mate"],"s":W+"Club-Mate"},
 {"n":"Gatorade","c":"United States","f":"1965","seg":"Sports drinks","d":"Sports-drink brand from the University of Florida, owned by PepsiCo since 2001.","lines":["G2","Gatorlyte"],"sig":["Gatorade"],"s":W+"Gatorade"},
 {"n":"Lucozade","c":"United Kingdom","f":"1927","seg":"Energy & sports drinks","d":"Newcastle glucose drink brand, owned by Suntory since 2013.","lines":["Energy","Sport","Zero","Alert"],"sig":["Lucozade Sport"],"s":W+"Lucozade"},
 {"n":"Powerade","c":"United States","f":"1988","seg":"Sports drinks","d":"Coca-Cola's sports-drink brand.","lines":["Zero"],"sig":["Powerade"],"s":W+"Powerade"},
 {"n":"Otsuka Pharmaceutical","c":"Japan","seg":"Pharmaceuticals & drinks","d":"Japanese company that makes Pocari Sweat.","sig":["Pocari Sweat"],"s":W+"Pocari_Sweat"},
 {"n":"BodyArmor","c":"United States","f":"2011","seg":"Sports drinks","d":"Queens-based sports drink founded by Lance Collins and Mike Repole, wholly owned by Coca-Cola since 2021.","lines":["Lyte","SportWater","Flash I.V."],"sig":["BodyArmor"],"s":W+"Bodyarmor_SuperDrink"},
 {"n":"Nuun","c":"United States","seg":"Electrolyte tablets","d":"Maker of effervescent electrolyte tablets that split electrolytes from carbohydrates.","lines":["Sport","Zero Sugar","Immunity","Energy"],"s":"https://nuunlife.com/company"},
 {"n":"Liquid I.V.","c":"United States","f":"2012","seg":"Electrolyte drink mix","d":"Californian oral-rehydration-style drink mix brand, acquired by Unilever in 2020.","s":"https://www.cbinsights.com/company/liquid-iv"},
 {"n":"Glacéau","c":"United States","seg":"Enhanced water","d":"New York maker of Vitaminwater and Smartwater, owned by Coca-Cola since 2007.","lines":["Vitaminwater","Smartwater"],"sig":["Vitaminwater"],"s":W+"Vitaminwater"},
 {"n":"CytoSport","c":"United States","f":"1998","seg":"Sports nutrition","d":"Benicia, California maker of Muscle Milk, owned by PepsiCo since 2019.","lines":["Muscle Milk"],"s":W+"Muscle_Milk"},
]
notes=("All 7 planned kinds kept (no old data). Left out: Bacchus (wiki 404), Monster Rehab and undated flavour lists, Liquid I.V. line names (not on retrieved page), "
"adaptogen/nootropic brands (none on retrieved pages), Mate Mate/Flora Power (not on pages). Materva maker not stated. Medical ORS left to H2.")
import sys; sys.path.insert(0,"/home/user/Possession-Taxonomy/rebuild/work/J9/agent"); from segfix import fix; fix(B)
out={"kinds":K,"brands":B,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/J9/shelves/06_00.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
