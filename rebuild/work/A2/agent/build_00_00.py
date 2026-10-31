import json, os
W='https://en.wikipedia.org/wiki/'
def X(n,d,mk,y,s,v=None,a='',dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":[dict(zip(("n","mk","y","d"),t)) for t in (v or [])],"dt":dt}
bball={"n":"Basketball sneaker","a":"high-top sneaker · hi-top · basketball shoe","d":"Lace-up sneaker from the basketball lineage, sold in high, mid and low cuts.",
 "t":["High","Mid","Low"],"s":W+"Sneakers","x":[
 X("Chuck Taylor All Star","Canvas basketball shoe with rubber toe cap and ankle patch on the high cut; reached its present form by 1923.","Converse","1917",W+"Converse_All_Star",
   [("Low-cut 'Oxford' version","Converse","1957","low cut, no ankle patch"),("Chuck 70","Converse","2013","retro of late-1960s/early-1970s build"),
    ("Chuck 70 De Luxe","Converse","",""),("Chuck Taylor All Star II","Converse","2015",""),("Chuck Taylor All Star Lift Platform","Converse","","platform sole"),("Andy Warhol collection","Converse","2015","collaboration")],
   a="Chucks · All Star · Cons",dt="high or low cut · canvas, leather · colours"),
 X("Air Jordan 1","Michael Jordan's first Nike signature basketball shoe, designed by Peter B. Moore; first of the numbered Air Jordan line.","Nike","1985",W+"Air_Jordan",
   [("Air Jordan 1 (original)","Nike","1985","public release 1 April 1985"),("Black/red re-release","Nike","1994","first retro"),
    ("Air Jordan III","Nike","1988","later Air Jordan generation"),("Air Jordan IV","Nike","1989","Tinker Hatfield"),("Air Jordan XI","Nike","1995","Tinker Hatfield"),
    ("Travis Scott 'Cactus Jack' Air Jordan 1","Nike","","collaboration")],
   a="AJ1 · Jordan 1",dt="High, Mid, Low · leather · colourway by style code"),
 X("Air Force 1","First basketball shoe with Nike Air cushioning, designed by Bruce Kilgore.","Nike","1982",W+"Nike_Air_Force_1",
   [("Air Force 1 (original)","Nike","1982",""),("DJ Clark Kent collaboration","Nike","2010",""),
    ("35th-anniversary collaborations","Nike","2017","Don C, Errolson Hugh, Travis Scott, Virgil Abloh")],
   a="AF1 · Air Force One",dt="Low, Mid, High · leather · colourway"),
 X("Dunk","College basketball shoe designed by Peter Moore, launched with the 'Be True to Your School' team colours pack.","Nike","1985",W+"Nike_Dunk",
   [("'Be True to Your School' pack","Nike","1985","Michigan, Kentucky, Iowa, Georgetown, Syracuse, St. John's, UNLV"),
    ("SB Dunk","Nike","","skateboarding version"),("Supreme SB Dunk","Nike","2003","collaboration"),("Comme des Garçons Dunk","Nike","2017","collaboration"),
    ("Travis Scott SB Dunk","Nike","2020","collaboration")],
   a="Nike Dunk · SB Dunk",dt="Low, Mid, High · leather, suede · colourway"),
 X("Blazer","Early Nike basketball shoe with leather or suede upper and oversized Swoosh.","Nike","1973",W+"Nike_Blazer",
   [("Blazer SB","Nike","2005","Lance Mountain"),("Off-White 'The Ten' Blazer","Nike","2017","collaboration"),("Sacai Blazer Low","Nike","2019","collaboration")],
   dt="Mid, Low · leather, suede · colourway"),
 X("Superstar","Low-top version of the Pro Model basketball shoe with rubber shell toe; adopted by Run-DMC.","adidas","1969",W+"Adidas_Superstar",
   [("Superstar II","adidas","c. 1976",""),("35th Anniversary Series","adidas","2005",""),("Superstar ADV","adidas","2015","skate version"),("Superstar XLG","adidas","2023","larger proportions")],
   a="shell toe · shell top",dt="leather · stripe colours"),
 X("Pump","Basketball shoe with an inflatable bladder in the tongue to tighten the fit.","Reebok","1989",W+"Reebok_Pump",
   [("Court Victory Pump","Reebok","1990","tennis; re-released 2014"),("Pump Omni OG re-release","Reebok","2013",""),("Instapump Fury","Reebok","1994","running; 20th-anniversary reissue 2014")],
   a="The Pump",dt="cut · colourway"),
 X("Pro Leather","Leather basketball shoe from Converse's 1970s range.","Converse","1976",W+"Converse_(brand)",[("The Weapon","Converse","1986","later Converse leather basketball shoe")]),
 ],"m":[["Star Player 76","Converse"],["Run Star","Converse"]]}
court={"n":"Court sneaker","a":"tennis sneaker · low-top sneaker · court shoe","d":"Low-cut leather or canvas sneaker descended from tennis and other court-sport shoes.",
 "t":["Low","Mid"],"s":W+"Sneakers","x":[
 X("Stan Smith","Plain white leather tennis shoe with perforated stripes, first sold as the Robert Haillet.","adidas","1965",W+"Adidas_Stan_Smith",
   [("adidas Robert Haillet","adidas","1965","original name"),("Stan Smith","adidas","1978","renamed"),("Stan Smith 80s","adidas","2008",""),("Stan Smith II","adidas","c. 2000","")],
   dt="leather, suede · heel-tab colour"),
 X("K-Swiss Classic","All-leather tennis shoe from Los Angeles, the brand's founding model.","K-Swiss","1966","https://footwearmagazine.com/10-interesting-facts-to-know-about-k-swiss/",
   [("Classic 2000","K-Swiss","2019","Breaking Bad collaboration")],dt="leather · colour"),
 X("Killshot","Low court shoe for racquetball and squash, revived in leather as the Killshot 2 through J.Crew.","Nike","1979","https://highsnobiety.com/p/nike-killshot-history",
   [("Killshot (mesh)","Nike","1979","original"),("Killshot 2","Nike","2009","leather revival via J.Crew"),("General release","Nike","2019","")],dt="leather, suede · colourway"),
 X("B.Elite","White leather tennis shoe with gold logo, made to mark Björn Borg's five Wimbledon titles.","Diadora","1981","https://www.stuartslondon.com/blogs/blog/the-story-behind-diadora-a-brief-history",
   a="Borg Elite",dt="leather · logo colour"),
 X("Club C 85","Clean leather tennis shoe with Union Jack side logo, built on the Revenge Plus.","Reebok","1985","https://www.80scasualclassics.co.uk/blog/reebok-club-c-85/",
   a="Club C",dt="leather · gum or white sole"),
 ],"m":[["Carnaby","Lacoste"]]}
canvas={"n":"Canvas sneaker","a":"plimsoll · sand shoe · daps · deck shoe","d":"Low-cut canvas shoe on a vulcanised rubber sole, from the plimsoll and early tennis lineage.",
 "t":["Low","High","Slip-on"],"s":W+"Sneakers","x":[
 X("Keds Champion","Canvas shoe with rubber sole, the first mass-marketed canvas-top shoe.","Keds","1916",W+"Keds"),
 X("Superga 2750","Canvas sneaker on a vulcanised rubber sole, made in Turin.","Superga","1925",W+"Superga_(brand)"),
 X("Green Flash","White canvas tennis plimsoll worn by Fred Perry for his Wimbledon wins of 1934–36.","Dunlop","1933","https://www.theindustry.fashion/?p=158691"),
 X("Jack Purcell","Canvas badminton shoe named for Jack Purcell; Converse took over the trademark in 1972.","B.F. Goodrich","1933",W+"Jack_Purcell",a="Smilies"),
 X("Spring Court G2","Canvas clay-court tennis shoe with four ventilation holes in a vulcanised sole, by Georges Grimmeisen.","Spring Court","1936","https://www.springcourt.com/en/content/24-la-spring-court-g2-",
   [("G2 Scratch Canvas","Spring Court","","hook-and-loop fastening")]),
 X("Volley","Australian canvas tennis shoe developed with Adrian Quist.","Volley","1939",W+"Dunlop_Volley",
   [("Volley OC","Volley","1939","original"),("Volley International","Volley","1970s","revised upper, injected sole"),("Deuce","Volley","","")]),
 X("PF Flyers All American","Canvas basketball shoe associated with Bob Cousy.","PF Flyers","1958",W+"PF_Flyers",
   [("Bob Cousy Lo","PF Flyers","2009","reissue"),("Center Hi","PF Flyers","","featured in The Sandlot, 1993")]),
 X("Vans Authentic","The original Vans deck shoe, sold on the opening day of the Anaheim store.","Vans","1966",W+"Vans"),
 ]}
brands=[
 {"n":"Converse","c":"United States","f":"1908","seg":"Heritage sneakers","d":"Massachusetts rubber-shoe maker known for the Chuck Taylor All Star; owned by Nike since 2003.","lines":["Chuck Taylor All Star","Chuck 70","Jack Purcell","One Star"],"sig":["Chuck Taylor All Star","Pro Leather"],"rel":["Nike","PF Flyers"],"s":W+"Converse_(brand)"},
 {"n":"Nike","c":"United States","f":"1964","seg":"Sportswear","d":"Oregon sportswear company; owns Converse and the Jordan Brand.","lines":["Jordan Brand","Nike SB"],"sig":["Air Jordan 1","Air Force 1","Dunk","Blazer","Killshot"],"rel":["Converse"],"s":"knowledge"},
 {"n":"adidas","c":"Germany","f":"1949","seg":"Sportswear","d":"German sportswear company founded by Adolf Dassler.","lines":["Originals"],"sig":["Superstar","Stan Smith"],"rel":["Puma"],"s":"knowledge"},
 {"n":"Reebok","c":"United Kingdom","f":"1958","seg":"Sportswear","d":"Sportswear brand of British origin known for the Pump and Club C.","sig":["Pump","Club C 85"],"s":"knowledge"},
 {"n":"K-Swiss","c":"United States","f":"1966","seg":"Tennis heritage","d":"Los Angeles tennis brand founded by Swiss brothers Art and Ernie Brunner.","sig":["K-Swiss Classic"],"s":W+"K-Swiss"},
 {"n":"Diadora","c":"Italy","f":"1948","seg":"Sportswear","d":"Italian sports brand from Caerano di San Marco.","sig":["B.Elite"],"s":"https://www.stuartslondon.com/blogs/blog/the-story-behind-diadora-a-brief-history"},
 {"n":"Lacoste","c":"France","f":"1933","seg":"Sportswear","d":"French tennis-born apparel and footwear brand.","s":"knowledge"},
 {"n":"Keds","c":"United States","f":"1916","seg":"Canvas sneakers","d":"US Rubber canvas-shoe brand; owned by Designer Brands since 2023.","sig":["Keds Champion"],"s":W+"Keds"},
 {"n":"Superga","c":"Italy","f":"1911","seg":"Canvas sneakers","d":"Turin rubber-soled footwear brand founded by Walter Martiny; part of BasicNet.","sig":["Superga 2750"],"s":W+"Superga_(brand)"},
 {"n":"Dunlop","c":"United Kingdom","seg":"Sports goods","d":"Rubber and sports brand whose Green Flash plimsoll dates from 1933.","sig":["Green Flash"],"rel":["Volley"],"s":"https://www.theindustry.fashion/?p=158691"},
 {"n":"Volley","c":"Australia","f":"1939","seg":"Canvas sneakers","d":"Australian canvas shoe brand begun by Dunlop Australia; now made by Brand Collective.","sig":["Volley"],"rel":["Dunlop"],"s":W+"Dunlop_Volley"},
 {"n":"B.F. Goodrich","c":"United States","seg":"Rubber manufacturer","d":"Akron rubber company that created PF Flyers and the Jack Purcell shoe.","sig":["Jack Purcell"],"rel":["PF Flyers","Converse"],"s":W+"PF_Flyers"},
 {"n":"PF Flyers","c":"United States","f":"1937","seg":"Canvas sneakers","d":"Akron canvas-shoe brand founded by B.F. Goodrich; owned by Kassia Designs since 2021.","sig":["PF Flyers All American"],"rel":["B.F. Goodrich","Converse"],"s":W+"PF_Flyers"},
 {"n":"Spring Court","c":"France","f":"1936","seg":"Canvas sneakers","d":"Paris canvas tennis-shoe maker founded by Georges Grimmeisen.","sig":["Spring Court G2"],"s":"https://www.springcourt.com/en/content/24-la-spring-court-g2-"},
 {"n":"Vans","c":"United States","f":"1966","seg":"Skate and canvas sneakers","d":"Anaheim maker of vulcanised canvas deck and skate shoes.","sig":["Vans Authentic"],"s":W+"Vans"},
]
notes=("Merged old k2 High-top sneaker into Basketball sneaker and k1 Low-top sneaker into Court sneaker; cut is now type t (High/Mid/Low). "
 "Dropped as retail SKU noise: adidas VL Court 3.0, Reebok Court Advance, Lacoste Straightset 2.0. Old 'Chuck 70' (low) folded into Chuck Taylor All Star versions. "
 "Left for other shelves: adidas Ozweego (Chunky sneaker), Puma Palermo (Terrace sneaker). Run Star and Star Player 76 kept in m (no archetype page retrieved). "
 "Lacoste Carnaby kept in m; Puma Smash not added (no page retrieved; Parallel and Firecrawl out of credit, Wikidata rate-limited). "
 "Vans Old Skool (#36, c. 1976) left to the Skate shoe shelf. AJ III/IV/XI kept as versions of Air Jordan 1 (the line).")
out={"kinds":[bball,court,canvas],"brands":brands,"traditions":[],"notes":notes}
p='work/A2/shelves/00_00.json'; t=p+'.tmp'; json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
