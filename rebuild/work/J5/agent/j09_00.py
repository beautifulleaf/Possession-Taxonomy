from lib import *
def B(n,c,f,kf,d,s,seg="Specialist",lines=(),sig=()):
    return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"lines":list(lines),"eras":[],"sig":list(sig),"sc":[],"rel":[],"s":s}
HV=W+"List_of_hop_varieties"
kinds=[
{"n":"Hops","a":"","d":"Hops sold for brewing, as pellets or whole cones, by variety.","t":["pellets","whole cone","noble/aroma","bittering","dual-purpose"],"s":"https://northernbrewer.com/collections/beer-ingredients","m":[],
 "x":[
 X("Saaz","Žatec","Czech noble hop named after Žatec; mild, earthy, herbal and spicy, the hop of Bohemian pilsner; Czech alpha 2.5-4.0%.",W+"Saaz_hops",[],"aroma · low alpha",y="Bohemia"),
 X("Hallertau Mittelfrüh","Hallertauer","German hop from the Hallertau region of Bavaria, alpha about 3.5-5.5%.",HV,[],"noble aroma"),
 X("East Kent Goldings","Goldings","English hop sold under that name since 1838; smooth, sweet bitterness with spicy, earthy aroma.",HV,[],"English aroma",y="1838"),
 X("Fuggle","","English Kent hop noticed growing wild in 1861 and commercialised in 1875; earthier and less sweet than Goldings.",HV,[],"English aroma",y="1875"),
 X("Cascade","","American aroma hop from the USDA programme at Oregon State, bred 1956 and released 1971-72; floral, spicy and citrus with slight grapefruit.",W+"Cascade_hop",[],"American pale ale",y="1971"),
 X("Citra","HBC 394","American hop first crossed in 1990 and released in 2007; grapefruit and tropical fruit, alpha 11-13%.",HV,[],"high alpha",y="2007"),
 X("Mosaic","HBC 369","American hop with tropical, blueberry, tangerine, floral and earthy notes; alpha 11.5-13.5%.",HV,[],"high alpha"),
 X("Simcoe","YCR 14","American hop released in 2000: passion fruit, pine, earthy and citrus, alpha 12-14%.",HV,[],"high alpha",y="2000"),
 X("Nelson Sauvin","","New Zealand hop developed in 1987 and sold since 2000, with a strong suggestion of passionfruit.",HV,[],"Sauvignon blanc character",y="2000"),
 X("Galaxy","","Australian hop bred in 1994 with citrus and passionfruit aroma.",HV,[],"high oil",y="1994"),
 ]},
{"n":"Brewing malt and grain","a":"","d":"Malted barley and other grains for mashing: base malts that convert their own starch and specialty malts for colour and flavour.","t":["base malt","specialty malt","crushed","whole"],"s":W+"Mash_ingredients","m":[],
 "x":[
 X("Maris Otter","","Two-row winter barley bred at the Plant Breeding Institute, Cambridge, introduced in 1966 and prized for real ale.",W+"Maris_Otter",[],"English pale malt",y="1966"),
 X("Golden Promise","","Spring two-row barley from gamma-irradiated Maythorpe, grown commercially in Scotland from 1967; Simpsons Malt secured its variety rights in 2015.",W+"Golden_Promise",[],"Scottish pale malt",mk="Simpsons Malt",y="1967"),
 X("Pilsner malt","","The lightest generally available base malt, with a sweet malt flavour, basis of pale lagers.",W+"Mash_ingredients",[],"base"),
 X("Vienna malt","","Slightly darker, hotter-kilned malt for Vienna lager and Märzen, usually 10-15% of the grist but able to serve as base.",W+"Mash_ingredients",[],"base"),
 X("Munich malt","","Darker base malt for bocks with enough enzymes to self-convert; malty rather than sweet.",W+"Mash_ingredients",[],"base"),
 X("Crystal malt","caramel malt","Specialty malt wetted and roasted in a drum, fully converted, adding toffee-like sweetness; contains no enzymes.",W+"Mash_ingredients",[],"specialty"),
 X("Chocolate malt","","Specialty malt kilned hotter than amber malts, adding chocolate and cocoa flavour to porters and stouts; no enzymes.",W+"Mash_ingredients",[],"specialty"),
 ]},
{"n":"Malt extract","a":"","d":"Concentrated malt wort, liquid or dry, for brewing or baking.","t":["liquid","dry","pre-hopped"],"s":"https://northernbrewer.com/collections/beer-ingredients","m":[],"r":[["Briess malt extracts","Briess"],["Muntons malt extract","Muntons"],["Coopers malt extracts","Coopers"]]},
{"n":"Brewing yeast","a":"","d":"Yeast for home brewing and winemaking.","t":["dry","liquid","ale","lager","wine"],"s":"https://northernbrewer.com/collections/beer-ingredients","m":[],"r":[["Fermentis dry brewing yeasts","Fermentis"],["White Labs liquid yeasts","White Labs"],["Wyeast liquid yeasts","Wyeast Laboratories"]],
 "x":[
 X("SafAle US-05","Safale American","Fermentis dry American ale yeast, widely sold to homebrewers in sachets and 500 g packs.","https://www.northernbrewer.com/products/safale-us-05-american-ale-yeast",[],"dry ale yeast",mk="Fermentis"),
 X("Kveik","Norwegian farmhouse yeast","Family of Saccharomyces cerevisiae strains from western Norway that ferment up to 43 °C, finish fast and often give tropical-fruit aromas; sold by labs in several countries.",W+"Kveik",[],"high temperature · fast",y="traditional"),
 ]},
{"n":"Beer kits","a":"extract kits","d":"Ready-to-brew kits of malt extract, hops and yeast, from simple cans to all-grain sets.","t":["pre-hopped can","extract with steeping grain","all-grain"],"s":W+"Homebrewing","m":[],
 "x":[X("Coopers homebrew kits","Coopers DIY","Kits from Coopers of Adelaide, the world's largest producer of canned beer concentrate for homebrewing; brewery founded by Thomas Cooper in 1862.",W+"Coopers_Brewery",[],"canned concentrate",mk="Coopers",y="1862"),
      X("Muntons Flagship kits","","Muntons' craft-style 35-pint kits of Hazy IPA, Milk Stout and West Coast IPA, launched in 2021.","https://www.muntons.com/muntons-flagship-homebrew-kits-launched",[V("Hazy IPA","Muntons","2021","5% ABV"),V("Milk Stout","Muntons","2021","4% ABV"),V("West Coast IPA","Muntons","2021","7% ABV")],"35 pints · dry-hop pack",mk="Muntons",y="2021")]},
{"n":"Wine and cider kits","a":"grape concentrate","d":"Concentrated grape or apple juice kits for home wine and cider; grape concentrate bricks were once sold for this in Prohibition-era America.","t":["wine kit","cider kit","grape concentrate"],"s":W+"Vine-Glo","m":[]},
]
brands=[
B("Coopers","Australia","1862","homebrew kits","Adelaide brewery founded by Thomas Cooper in 1862; the world's largest producer of canned beer concentrate for homebrewing.",W+"Coopers_Brewery",sig=["Coopers homebrew kits"]),
B("Muntons","United Kingdom","","malt and homebrew kits","Stowmarket, Suffolk maltster making homebrew kits since the 1970s; Flagship range launched 2021.","https://www.muntons.com/muntons-flagship-homebrew-kits-launched",sig=["Muntons Flagship kits"]),
B("Simpsons Malt","United Kingdom","","Scottish malt","Maltster that bought a farm in 1983 to keep Golden Promise barley in supply and acquired its variety rights in 2015.",W+"Golden_Promise",seg="Heritage manufactory",sig=["Golden Promise"]),
B("Fermentis","France","","dry yeast","Maker of SafAle dry brewing yeasts including US-05.","https://www.northernbrewer.com/products/safale-us-05-american-ale-yeast",sig=["SafAle US-05"]),
]
notes="Weyermann, Crisp, WLP001 and Wyeast 1056 not confirmed on retrieved pages, so no archetypes; White Labs, Wyeast and Briess are kept as old-data ranges only. Wine and cider kit makers not found (only the historic Vine-Glo concentrate page). Hallertau Mittelfrüh character not described on the retrieved page. No traditions added."
write("09_00",kinds,brands,[],notes)
