import json, os
W='https://en.wikipedia.org/wiki/'
SOTH_NF='https://www.sothebys.com/en/articles/louis-vuitton-neverfull-the-tote-that-is-truly-never-full'
SOTH_GY='https://www.sothebys.com/en/articles/ultimate-guide-to-goyard-tote-styles-saint-louis-and-more'
SOTH_GP='https://www.sothebys.com/en/articles/hermes-garden-party-the-ultimate-tote-bag'
LC=W+'Longchamp_(company)'; BV=W+'Bottega_Veneta'; LV=W+'Louis_Vuitton'
tote={"n":"Tote bag","a":"tote · shopper tote","d":"Large, usually open-topped bag with two parallel handles rising from the sides of the body.",
 "t":["unstructured","structured","reversible","with removable pouch","north–south","east–west"],
 "s":"https://en.wikipedia.org/wiki/Handbag",
 "x":[
  {"n":"Saint Louis","a":"St. Louis tote","d":"Light, unlined, reversible open tote in chevron Goyardine canvas with leather handles and a removable pouch.","mk":"Goyard","y":"","s":SOTH_GY,
   "v":[{"n":"Saint Louis PM","mk":"Goyard","y":"","d":"smaller everyday size"},{"n":"Saint Louis GM","mk":"Goyard","y":"","d":"larger everyday size"},{"n":"Saint Louis XXL","mk":"Goyard","y":"","d":"largest size"}],
   "dt":"size PM · GM · XXL · Goyardine canvas colours · hand-painted personalisation"},
  {"n":"Neverfull","a":"LV Neverfull","d":"Open-topped canvas tote with side laces that cinch the body, slim shoulder straps and a detachable pouch.","mk":"Louis Vuitton","y":"2007","s":SOTH_NF,
   "v":[{"n":"Neverfull PM","mk":"Louis Vuitton","y":"","d":"smallest size, now hard to find"},{"n":"Neverfull MM","mk":"Louis Vuitton","y":"","d":"medium size, the most popular"},{"n":"Neverfull GM","mk":"Louis Vuitton","y":"","d":"largest size"},{"n":"Neverfull with detachable pouch","mk":"Louis Vuitton","y":"2013","d":"pouch included with every bag from 2013"}],
   "dt":"size PM · MM · GM · Monogram, Damier Ebène, Damier Azur canvas, Epi leather · lining colour · artist editions"},
  {"n":"Le Pliage","a":"Longchamp Pliage","d":"Foldable nylon-canvas tote with Russian-leather handles and flap that folds into a small square.","mk":"Longchamp","y":"1993","s":LC,
   "v":[{"n":"Original Le Pliage","mk":"Longchamp","y":"1993","d":"designed by Philippe Cassegrain"},{"n":"Jeremy Scott editions","mk":"Longchamp","y":"2005","d":"printed special editions"},{"n":"Mary Katrantzou printed totes","mk":"Longchamp","y":"2011","d":"designer collaboration"},{"n":"Sarah Morris limited edition","mk":"Longchamp","y":"2014","d":"artist edition"},{"n":"Pokémon collaboration","mk":"Longchamp","y":"2020","d":"shown at Paris Fashion Week"}],
   "dt":"size and handle length · nylon colour · leather trim colour · limited editions"},
  {"n":"Garden Party","a":"","d":"Logo-free open tote with expandable side snaps, in canvas or leather, carried by hand or elbow.","mk":"Hermès","y":"1964","s":SOTH_GP,
   "v":[{"n":"Garden Party 23","mk":"Hermès","y":"","d":"also called Neo or Mini Garden Party; snap closure"},{"n":"Garden Party 30","mk":"Hermès","y":"","d":""},{"n":"Garden Party 36 (PM)","mk":"Hermès","y":"","d":""},{"n":"Garden Party 49 (GM)","mk":"Hermès","y":"","d":"largest size"}],
   "dt":"size 23 · 30 · 36 · 49 · canvas, Togo, Negonda, Clemence, Swift leathers · colour"},
  {"n":"Cabat","a":"","d":"Unlined tote woven by hand from double-faced intrecciato leather, so inside and outside match.","mk":"Bottega Veneta","y":"2001","s":"https://www.wmagazine.com/fashion/bottega-veneta-cabat-bag-intrecciato-backstory",
   "v":[{"n":"Cabat (Tomas Maier)","mk":"Bottega Veneta","y":"2001","d":"Maier's first bag for the house"},{"n":"Frayed-edge Cabat","mk":"Bottega Veneta","y":"2025","d":"frayed leather version"}],
   "dt":"size mini · small · medium · large · leather colour"},
  {"n":"Book Tote","a":"Dior Book Tote","d":"Open rectangular canvas tote, often embroidered all over, with flat top handles.","mk":"Dior","y":"2018","s":"https://www.rebag.com/thevault/the-size-guide-dior-book-tote/",
   "v":[{"n":"Original Book Tote","mk":"Dior","y":"2018","d":"Spring/Summer 2018, Maria Grazia Chiuri; now the Medium"},{"n":"Small Book Tote","mk":"Dior","y":"2022","d":"added early 2022"},{"n":"Mini Book Tote","mk":"Dior","y":"","d":""},{"n":"Large Book Tote","mk":"Dior","y":"","d":""}],
   "dt":"size mini · small · medium · large · Oblique, embroidered or printed canvas, mesh · personalisation"},
  {"n":"Park Tote","a":"N/S Park Tote","d":"Soft, unlined calfskin tote with flat handles and an interior tie closure.","mk":"The Row","y":"","s":"https://fairlycurated.com/blog/2023/12/18/the-row-park-ns-tote-review-small-vs-medium-vs-large",
   "v":[{"n":"Small N/S Park Tote","mk":"The Row","y":"","d":""},{"n":"Medium N/S Park Tote","mk":"The Row","y":"","d":""},{"n":"Large N/S Park Tote","mk":"The Row","y":"","d":"grained calfskin, made in Italy"},{"n":"Park Tote with belt","mk":"The Row","y":"","d":"adjustable strap and interior pocket"}],
   "dt":"size small · medium · large · north–south or east–west · pebbled or smooth leather · colour"},
  {"n":"Andiamo","a":"","d":"Intrecciato-woven leather handbag introduced under Matthieu Blazy.","mk":"Bottega Veneta","y":"2023","s":BV,"v":[],"dt":"size · leather colour"},
  {"n":"Anjou","a":"","d":"Reversible tote with Goyardine canvas on one side and leather on the other, with removable pouch.","mk":"Goyard","y":"","s":SOTH_GY,
   "v":[],"dt":"size Mini · PM · MM · GM · canvas and leather colour"}],
 "m":[["Paloma","Christian Louboutin"],["Hana","JW PEI"],["Lotus","Khaite"]]}
canvas={"n":"Canvas tote","a":"boat tote · canvas shopper · cotton tote","d":"Simple tote of heavy cotton canvas (or jute) used for shopping, beach and everyday carrying.",
 "t":["cotton canvas","jute","with contrast trim","with zip top","printed or monogrammed"],
 "s":W+"Tote_bag",
 "x":[{"n":"Boat and Tote","a":"Bean's Ice Carrier","d":"Heavy cotton-canvas tote with a reinforced flat bottom and contrast trim, made in Maine.","mk":"L.L.Bean","y":"1944","s":"https://www.llbeanbusiness.com/bags-and-totes/tote-bags/1000247271.html",
   "v":[{"n":"Bean's Ice Carrier","mk":"L.L.Bean","y":"1944","d":"original ice-carrying bag"},{"n":"1944 Boat and Tote","mk":"L.L.Bean","y":"","d":"80th-anniversary edition, 24 oz canvas, removable shoulder strap"}],
   "dt":"size · handle length · trim colour · monogram"}]}
satchel={"n":"Satchel","a":"","d":"Soft-sided bag with a front-fastening flap, top handle and shoulder strap, originally for carrying books.",
 "t":["structured","soft","crossbody strap","buckle closure","lock closure"],
 "s":"https://en.wikipedia.org/wiki/Handbag",
 "x":[{"n":"School satchel","a":"book satchel","d":"Traditional leather book bag whose back extends into a front flap, worn across the body.","mk":"","y":"","s":W+"Satchel_(bag)","v":[],"dt":"leather · buckles · size"},
  {"n":"Classic satchel","a":"Cambridge satchel","d":"Handmade, colourful leather satchel based on the original Oxford and Cambridge school satchel.","mk":"Cambridge Satchel Company","y":"2008","s":W+"Cambridge_Satchel_Company","v":[],"dt":"size · leather colour · embossing"},
  {"n":"Bayswater","a":"","d":"Leather top-handle bag closed by Mulberry's Postman's Lock, designed by Nicholas Knightly.","mk":"Mulberry","y":"2003","s":"https://www.mulberry.com/us/bayswater",
   "v":[{"n":"Bayswater","mk":"Mulberry","y":"2003","d":"original"},{"n":"Bayswater Satchel","mk":"Mulberry","y":"","d":""},{"n":"Small Soft Bayswater","mk":"Mulberry","y":"","d":"heavy grain leather"},{"n":"Mini Zipped Bayswater","mk":"Mulberry","y":"","d":""},{"n":"Buckle Bayswater","mk":"Mulberry","y":"","d":""},{"n":"Bayswater Tote","mk":"Mulberry","y":"","d":""}],
   "dt":"size · Small Classic Grain or Heavy Grain leather · colour (Oak, Black…) · lock hardware"},
  {"n":"Rockstud","a":"","d":"Leather bag trimmed with pyramid studs, from the Rockstud accessory line.","mk":"Valentino","y":"2008–2012","s":W+"Valentino_(fashion_house)","v":[],"dt":"size · leather colour · stud finish"}]}
bucket={"n":"Bucket bag","a":"","d":"Bucket-shaped bag with a round or oval base, closed by a drawstring or left open.",
 "t":["drawstring","open top","mini"],"tg":[],
 "s":"https://en.wikipedia.org/wiki/Handbag",
 "x":[{"n":"Reticule","a":"ridicule · indispensable","d":"Small drawstring handbag of net, velvet, silk or satin carried over the arm in the Regency era.","mk":"","y":"1795–1820","s":W+"Reticule_(handbag)","v":[],"dt":"netting, velvet, silk, satin · embroidery or beadwork"},
  {"n":"Kinchaku","a":"","d":"Traditional Japanese cloth drawstring bag for personal belongings, small ones hung from the obi.","mk":"","y":"","s":W+"Kinchaku","v":[{"n":"Kago","mk":"","y":"","d":"maiko and geisha bag with woven basket base"}],"dt":"size · fabric · cord"},
  {"n":"Noé","a":"Noe","d":"Drawstring bucket bag created to carry five bottles of champagne.","mk":"Louis Vuitton","y":"1932","s":"https://www.fashionphile.com/blogs/academy/louis-vuitton-noe-and-neonoe",
   "v":[{"n":"Noé","mk":"Louis Vuitton","y":"1932","d":"by Gaston-Louis Vuitton for a champagne producer"},{"n":"Petit Noé","mk":"Louis Vuitton","y":"","d":"smaller version"},{"n":"Noé BB","mk":"Louis Vuitton","y":"","d":""},{"n":"Nano Noé","mk":"Louis Vuitton","y":"","d":""},{"n":"NéoNoé","mk":"Louis Vuitton","y":"2017","d":"relaxed shape, coloured leather, BB and MM"}],
   "dt":"size · Monogram, Damier Azur canvas, Epi leather · trim colour"},
  {"n":"Bucket Bag","a":"Mansur Gavriel bucket","d":"Minimal leather bucket bag whose 2013 debut revived the form.","mk":"Mansur Gavriel","y":"2013","s":"https://www.mansurgavriel.com/pages/fw25-bucket-bags",
   "v":[{"n":"Mini Bucket Bag","mk":"Mansur Gavriel","y":"","d":"e.g. Black/Flamma"}],"dt":"size · leather or suede · colour · contrast lining"}]}
def B(n,c,f,seg,d,sig,s,eras=None,lines=None,rel=None):
    return {"n":n,"c":c,"f":f,"seg":seg,"d":d,"lines":lines or [],"eras":eras or [],"sig":sig,"sc":[],"rel":rel or [],"s":s}
brands=[
 B("Louis Vuitton","France","1854","Luxury fashion house","Paris trunk maker turned luxury house known for monogram canvas bags.",["Noé","Neverfull","Keepall","Speedy"],LV,
   ["Marc Jacobs, artistic director from 1997","Nicolas Ghesquière, women's from 2013"],rel=["Goyard"]),
 B("Goyard","France","1853","Luxury trunk maker","Paris trunk maker known for chevron Goyardine canvas, introduced at the 1900 Exposition.",["Saint Louis","Anjou","Artois"],W+"Goyard",rel=["Louis Vuitton"]),
 B("Longchamp","France","1948","Premium leather goods","Paris leather-goods house founded by Jean Cassegrain.",["Le Pliage"],LC),
 B("Hermès","France","1837","Luxury fashion house","Paris saddler and luxury house founded by Thierry Hermès.",["Kelly","Birkin","Garden Party"],W+"Herm%C3%A8s",["Jean-Louis Dumas, 1978–2005","Pierre-Alexis Dumas, artistic director from 2005"]),
 B("Dior","France","1946","Luxury fashion house","Paris couture house founded by Christian Dior.",["Saddle bag","Book Tote"],W+"Dior",["John Galliano, 1997–2011","Maria Grazia Chiuri, 2016–2025","Jonathan Anderson, 2025–"]),
 B("Bottega Veneta","Italy","1966","Luxury leather goods","Vicenza-founded house known for intrecciato woven leather.",["Cabat","Andiamo"],BV,["Tomas Maier, 2001–2018","Daniel Lee, 2018–2021","Matthieu Blazy, 2021–2024","Louise Trotter, 2024–"]),
 B("The Row","United States","2006","Luxury fashion label","New York label founded by Mary-Kate and Ashley Olsen.",["Park Tote"],W+"The_Row_(fashion_label)"),
 B("L.L.Bean","United States","1912","Outdoor and casual retailer","Freeport, Maine outfitter founded by Leon Leonwood Bean.",["Boat and Tote"],W+"L.L.Bean"),
 B("Mulberry","United Kingdom","1971","Premium leather goods","Somerset leather-goods house founded by Roger Saul.",["Bayswater"],W+"Mulberry_(company)",["Emma Hill, 2007–2013","Johnny Coca, 2015–2020"]),
 B("Cambridge Satchel Company","United Kingdom","2008","Leather satchel maker","Cambridge maker of colourful handmade leather satchels founded by Julie Deane and Freda Thomas.",["Classic satchel"],W+"Cambridge_Satchel_Company"),
 B("Valentino","Italy","1960","Luxury fashion house","Rome couture house founded by Valentino Garavani; leather goods sold as Valentino Garavani.",["Rockstud"],W+"Valentino_(fashion_house)",["Maria Grazia Chiuri and Pierpaolo Piccioli, 2008–2016","Pierpaolo Piccioli, to 2024","Alessandro Michele, 2024–"],lines=["Valentino Garavani"]),
 B("Mansur Gavriel","","","Contemporary leather goods","Leather-goods label whose bucket bag drove the form's 2013 revival; made in Italy.",["Bucket Bag"],"https://www.mansurgavriel.com/pages/fw25-bucket-bags"),
]
notes=("Dropped from Tote bag: Tumi ranges Alpha, Alpha Bravo, Harrison, Voyageur and the Voyageur Just-in-Case Tote (brief: Tumi ranges belong in Tumi's brand entry). "
 "Old flat models Kinchaku and Reticule became maker-free archetypes; Rockstud (maker given as Valentino Garavani, now brand-register name Valentino) became an archetype; Andiamo and Park became archetypes; Paloma, Hana, Lotus stay in m. "
 "Not added (no retrievable source this session): The Row Park Tote launch year; Saint Louis launch year; Noé BB/Petit Noé years; Le Pliage Néo/Cuir variants; Boat and Tote 1965 relaunch (llbean.com blocked); Mansur Gavriel founding year/country (Wikipedia page missing). "
 "Dior official and PurseBlog pages returned 403; Le Pliage and Mansur Gavriel Wikipedia articles do not exist. No traditions added (kinchaku tradition page not retrieved).")
out={"kinds":[tote,canvas,satchel,bucket],"brands":brands,"traditions":[],"notes":notes}
p='work/A4/shelves/00_01.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p); print('ok')
