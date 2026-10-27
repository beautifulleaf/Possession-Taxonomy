from lib import *
def B(n,c,f,kf,d,s,seg="Mainstream",lines=(),sig=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":[],"s":s}
M=W+"Mustard_(condiment)"
kinds=[
{"n":"Ketchup","a":"catsup","d":"Thick sweet-sour tomato table sauce; mushroom ketchup is the older British form.","t":["tomato","mushroom","reduced sugar"],"s":W+"Ketchup","m":[["Heinz Tomato Ketchup","Kraft Heinz"]]},
{"n":"Mayonnaise","a":"","d":"Emulsion of oil, egg yolk and an acid, sold in US, Southern and Japanese styles.","t":["egg-free","Japanese (rice vinegar, egg yolk)","light"],"s":W+"Mayonnaise","m":[["Ballymaloe Mayonnaise","Ballymaloe"],["Hellmann's Real Mayonnaise","Hellmann's"],["Kewpie Mayonnaise","Kewpie"],["Duke's Mayonnaise","Duke's"]]},
{"n":"Mustard","a":"","d":"Prepared mustard, a paste of ground seed with vinegar, wine or water, in regional styles.","t":["smooth","wholegrain","hot","mild"],"s":M,"m":[["Maille Dijon Mustard","Maille"],["Colman's English Mustard","Colman's"]],
 "x":[X("Dijon mustard","","Smooth brown-seed mustard made with white wine or verjuice, current form dating to Jean Naigeon in 1856; the name is generic and unprotected.",W+"Dijon_mustard",[V("Maille Dijon Mustard","Maille"),V("Grey Poupon","","1866","Originated in Dijon")],"brown seed · white wine · smooth",y="1856"),
      X("Moutarde de Meaux","Pommery mustard","Coarse-ground, grainy mustard from Meaux, best known under the Pommery brand.",W+"List_of_mustard_brands",[],"grainy"),
      X("English mustard","Colman's English","Bright yellow, thick, strong mustard from yellow and brown seed with low acidity; Colman's, Norwich, 1814.",W+"Colman's",[V("Colman's English Mustard","Colman's","1814")],"hot",mk="Colman's",y="1814"),
      X("Bavarian sweet mustard","süßer Senf","Sugar-sweetened mustard served with Weißwurst and Leberkäse; Händlmaier of Regensburg developed its recipe in 1914.",W+"H%C3%A4ndlmaier",[V("Händlmaier sweet mustard","Händlmaier","1914")],"sweet",mk="Händlmaier",y="1914"),
      X("American yellow mustard","ballpark mustard","Mild, vinegary, turmeric-yellow mustard introduced in 1904 as 'cream salad mustard'.",M,[V("French's","French's","1904")],"mild",y="1904"),
      X("Spicy brown mustard","deli-style","Coarse brown-seed mustard with a speckled look and more bite than yellow.",M,[V("Gulden's","Gulden's","","Known for spicy brown")],"coarse")]},
{"n":"Brown sauce","a":"","d":"British and Irish dark, tangy sauce of tomatoes, malt vinegar, molasses, dates and tamarind.","t":["fruity","spicy"],"s":W+"Brown_sauce","m":[["HP Sauce","HP Foods"],["Daddies Sauce","Daddies"]]},
{"n":"Barbecue sauce","a":"BBQ sauce","d":"Thick sweet, smoky or tangy sauce for grilled meat, with strong regional US styles.","t":["tomato-based","vinegar","mustard","white (mayonnaise)"],"s":W+"Barbecue_sauce","m":[],
 "x":[X("Kansas City barbecue sauce","","Thick, sweet, reddish-brown tomato sauce with sugar, vinegar and spices; the basis of typical commercial sauce.",W+"Barbecue_sauce",[],"sweet tomato"),
      X("Carolina barbecue sauces","","Thin vinegar-and-pepper sauce in the east, and yellow mustard sauce in South Carolina.",W+"Barbecue_sauce",[V("Eastern vinegar-pepper"),V("South Carolina mustard")],"vinegar · mustard"),
      X("Texas barbecue sauce","","Medium-thick sauce with cumin, chilli, black pepper and onion, less tomato and sugar.",W+"Barbecue_sauce",[],"cumin · chilli"),
      X("Alabama white sauce","","Mayonnaise-based sauce with cider vinegar, sugar and pepper from North Alabama, served on chicken and pork.",W+"Barbecue_sauce",[],"mayonnaise-based")]},
{"n":"Worcestershire sauce","a":"","d":"Fermented brown sauce of vinegar, molasses, tamarind and anchovy, first sold in Worcester in 1837.","t":["malt vinegar (UK)","spirit vinegar (US)","anchovy-free"],"s":W+"Worcestershire_sauce","m":[["Lea & Perrins Worcestershire Sauce","Lea & Perrins"],["French's Worcestershire Sauce","French's"]]},
{"n":"Salad dressing","a":"","d":"Pourable dressings for salad: vinaigrettes, creamy dressings, ranch, Caesar and French.","t":["vinaigrette","creamy","ranch","Caesar","Thousand Island"],"s":W+"Salad_dressing","m":[["Newman's Own Classic Oil & Vinegar Dressing","Newman's Own"]]},
{"n":"Salad cream","a":"","d":"Pourable egg, oil and vinegar emulsion, sharper and thinner than mayonnaise; first made commercially by Heinz in 1914.","t":["original","light"],"s":W+"Salad_cream","m":[["Heinz Salad Cream","Heinz"]]},
{"n":"Horseradish","a":"","d":"Prepared grated horseradish in vinegar, cream or mayonnaise, or with beetroot.","t":["vinegar","creamed","white chrain","red chrain (beetroot)"],"s":W+"Horseradish","m":[["Ba-Tampte Prepared Horseradish","Ba-Tampte"],["Boar's Head Pub Style Horseradish","Boar's Head"],["Gold's Fresh Grated Prepared Horseradish","Gold's"]]},
{"n":"Prepared wasabi","a":"","d":"Wasabi paste in a tube or bottle, usually made from horseradish, mustard and green colouring rather than true wasabi.","t":["real wasabi rhizome","horseradish-based","powder"],"s":W+"Wasabi","m":[]},
{"n":"Cooking bitters","a":"bitters sold as a flavouring by the dash","d":"Concentrated bitter flavouring used a few drops at a time. Bitter liqueurs and drinking bitters sold by the glass are in Wine, Beer & Spirits.","t":["aromatic","orange","Creole"],"s":W+"Bitters","m":[["Angostura Aromatic Bitters","Angostura"],["Peychaud's Bitters","Peychaud's"]]},
]
brands=[
B("Heinz","United States","1869","ketchup","Pittsburgh food company founded by Henry J. Heinz; Tomato Ketchup launched 1876 in an octagonal bottle from 1889; now Kraft Heinz.",W+"Heinz_Tomato_Ketchup",lines=["Tomato Ketchup","Salad Cream","HP Sauce","Daddies","Lea & Perrins"],sig=["Heinz Tomato Ketchup"]),
B("Hellmann's","United States","1913","mayonnaise","Blue Ribbon mayonnaise from Richard Hellman's New York deli; sold as Best Foods in the western US; owned by Unilever.",W+"Hellmann%27s_and_Best_Foods"),
B("Kewpie","Japan","1925","Japanese mayonnaise","Japanese mayonnaise made with egg yolk, from Toichiro Nakashima; mayonnaise production began 1925.",W+"Kewpie_(mayonnaise)"),
B("Duke's","United States","1917","Southern mayonnaise","Mayonnaise created by Eugenia Duke in Greenville, South Carolina; extra yolk, no sugar, cider vinegar.",W+"Duke's_Mayonnaise"),
B("Colman's","United Kingdom","1814","English mustard","Norwich mustard maker founded by Jeremiah Colman; owned by Unilever since 1995.",W+"Colman's",seg="Heritage manufactory"),
B("Maille","France","1747","Dijon mustard","French mustard and pickle company founded in Marseille in 1747; a Unilever subsidiary.",W+"List_of_mustard_brands",seg="Heritage manufactory"),
B("Händlmaier","Germany","1910","sweet Bavarian mustard","Regensburg mustard maker whose sweet mustard recipe dates to 1914.",W+"H%C3%A4ndlmaier",seg="Heritage manufactory"),
B("Lea & Perrins","United Kingdom","1837","Worcestershire sauce","Worcester chemists' sauce commercialised in 1837; a UK subsidiary of Kraft Heinz.",W+"Lea_&_Perrins",seg="Heritage manufactory"),
B("HP Sauce","United Kingdom","1895","brown sauce","Britain's leading brown sauce, with about 75% of sales; owned by Kraft Heinz since 2005.",W+"HP_Sauce"),
B("Daddies","United Kingdom","1904","brown sauce","UK brown sauce (1904) and ketchup (1930) brand, owned by Heinz since 2005.",W+"Daddies"),
]
notes="Kewpie, Duke's and others added to mayonnaise m from retrieved pages. Texas and other BBQ styles attested from the Barbecue sauce page; branded BBQ sauces (e.g. KC Masterpiece) not added. Test winners not retrieved. Moutarde de Meaux/Pommery sourced from List of mustard brands (no dedicated page). Cooking bitters keep old Angostura/Peychaud's."
write("05_00",kinds,brands,[],notes)
