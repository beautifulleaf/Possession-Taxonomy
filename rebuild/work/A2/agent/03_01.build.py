import json, os
W="https://en.wikipedia.org/wiki/"
MULE=W+"Mule_(shoe)"; ESP=W+"Espadrille"; TRA=W+"Tr%C3%A4skor"
kinds=[
{"n":"Mule","a":"backless shoe · slide-on shoe","d":"Backless shoe with a closed toe, flat or heeled; a backless loafer is a mule.",
 "t":["flat mule","heeled mule","loafer mule","pointed-toe mule","wedge mule"],"s":MULE,
 "x":[
  {"n":"Princetown","a":"horsebit backless loafer","d":"Gucci's loafer-style mule worn by men and women, a backless take on the house loafer.","mk":"Gucci","y":"by 2015","s":MULE,
   "v":[{"n":"Kangaroo-fur-lined Princetown","mk":"Gucci","y":"2015","d":"fur-lined version criticised by anti-fur activists"}],
   "dt":"leather, velvet · lined or unlined · hardware"},
  {"n":"Spring-o-Lator mule","a":"Ballin' The Jack","d":"1950s heeled mule held on by an elastic strip in the footbed instead of a strap.","mk":"Herbert Levine","y":"1950s","s":MULE,
   "v":[{"n":"Ballin' The Jack","mk":"Herbert Levine","y":"1952","d":"pairs dated 1952 in the Met collection"}],
   "dt":"heel height · upper material"},
  {"n":"Marabou mule","a":"feather mule","d":"Heeled boudoir mule trimmed with marabou feathers, a 1950s glamour style.","mk":"","y":"1950s","s":MULE,
   "dt":"feather colour · heel height"}],
 "m":[["Laurieann Lux","Clarks"],["Olleya","Hush Puppies"],["Sherman","Steve Madden"]]},
{"n":"Clog","a":"","d":"Slip-on with a thick rigid sole of wood or moulded material, backed or backless.",
 "t":["backless","with heel strap","closed back","stapled","high-heeled"],"s":"https://www.birkenstock.in/pages/5-most-iconic-styles-by-birkenstock",
 "x":[
  {"n":"Swedish clog","a":"träskor · träsko","d":"Swedish clog, usually an alder sole with a nailed leather upper; older ones are all wood.","mk":"","y":"traditional","s":TRA,
   "v":[{"n":"Troentorp","mk":"Troentorp","y":"1907","d":"hand-crafted, nailed and wet-lasted clogs from Troentorp near Båstad"},
        {"n":"Swedish Hasbeens","mk":"","y":"","d":"maker named among Swedish clog brands"},
        {"n":"Lotta","mk":"","y":"","d":"maker named among Swedish clog brands"}],
   "dt":"alder, birch or pine sole · leather upper or all wood · painted or floral decoration"},
  {"n":"Boston","a":"Birkenstock Boston","d":"Birkenstock's backless clog on the cork footbed, released as the first cork clog.","mk":"Birkenstock","y":"1976","s":W+"Birkenstock",
   "dt":"suede, leather · cork-latex footbed · buckle strap"},
  {"n":"Professional","a":"Dansko Professional","d":"Dansko's work clog with contoured arch support, rocker-bottom sole and slightly raised heel.","mk":"Dansko","y":"","s":W+"Dansko",
   "dt":"oiled, box or patent leather · stapled or unstapled"},
  {"n":"Crocs clog","a":"Beach · Classic Clog","d":"Moulded foam clog with a vented forefoot and heel strap, the best-known modern clog.","mk":"Crocs","y":"2002","s":W+"Crocs",
   "v":[{"n":"Beach","mk":"Crocs","y":"2002","d":"first model, sold out at the Fort Lauderdale Boat Show"},
        {"n":"Classic Clog","mk":"Crocs","y":"","d":"fully moulded Croslite foam, vented forefoot, heel strap"}],
   "dt":"colourway · charms · lined or unlined"}]},
{"n":"Espadrille","a":"alpargata · espardenya · espartinak","d":"Canvas or fabric shoe on a rope (jute) sole or wedge.",
 "t":["flat","wedge","lace-up (ankle-tied)","slip-on"],"s":"https://www.theoutnet.com/en-us/shop/designers/castaner",
 "x":[
  {"n":"Traditional espadrille","a":"espardenya · alpargata","d":"Flat canvas shoe on a plaited fibre sole, Iberian peasant footwear since at least the 14th century.","mk":"","y":"by 1322","s":ESP,
   "dt":"canvas colour · ankle ties or slip-on · jute or esparto sole"},
  {"n":"Wedge espadrille","a":"Saint Laurent wedge","d":"Espadrille on a rope-covered wedge heel, first made by Castañer for Yves Saint Laurent.","mk":"Castañer","y":"1970","s":ESP,
   "v":[{"n":"Yves Saint Laurent wedge","mk":"Castañer","y":"1970","d":"commissioned after a Paris trade-fair meeting"}],
   "dt":"wedge height · ankle ties · canvas or leather upper"},
  {"n":"TOMS Alpargata","a":"TOMS slip-on","d":"Canvas slip-on adapted from the Argentine alpargata for North American buyers.","mk":"TOMS","y":"2006","s":W+"Toms_Shoes",
   "dt":"canvas colour · rubber or rope-look sole"}],
 "m":[["Dali Original","Soludos"],["Marseille Wedge","Soludos"]]}]
brands=[
 {"n":"Gucci","c":"Italy","f":"1921","seg":"luxury fashion house","d":"Florentine house founded by Guccio Gucci; known for its loafers.","lines":[],"eras":["Alessandro Michele, creative director from 2015"],"sig":["Princetown"],"sc":[],"rel":[],"s":W+"Gucci"},
 {"n":"Herbert Levine","c":"","f":"","seg":"designer women's shoes","d":"Shoe label behind the 1950s Spring-o-Lator mule.","lines":[],"eras":[],"sig":["Spring-o-Lator mule"],"sc":[],"rel":[],"s":MULE},
 {"n":"Birkenstock","c":"Germany","f":"1774","seg":"comfort footwear","d":"German footbed-sandal maker; its Boston was the first cork clog.","lines":[],"eras":[],"sig":["Boston"],"sc":[],"rel":[],"s":W+"Birkenstock"},
 {"n":"Dansko","c":"United States","f":"1990","seg":"comfort and work clogs","d":"Comfort footwear company in West Grove, Pennsylvania, founded by Peter Kjellerup and Mandy Cabot.","lines":[],"eras":[],"sig":["Professional"],"sc":[],"rel":[],"s":W+"Dansko"},
 {"n":"Crocs","c":"United States","f":"2002","seg":"moulded foam footwear","d":"Colorado company making Croslite foam clogs, starting with the Beach.","lines":[],"eras":[],"sig":["Crocs clog"],"sc":[],"rel":[],"s":W+"Crocs"},
 {"n":"Troentorp","c":"Sweden","f":"1907","seg":"traditional clogs","d":"Clog maker in Troentorp near Båstad, formerly Båstad Clogs.","lines":[],"eras":[],"sig":["Swedish clog"],"sc":[],"rel":[],"s":W+"Troentorp_Clogs"},
 {"n":"Castañer","c":"Spain","f":"","seg":"espadrilles","d":"Spanish espadrille maker that made the first wedge espadrille for Yves Saint Laurent.","lines":[],"eras":[],"sig":["Wedge espadrille"],"sc":[],"rel":[],"s":"https://www.unicohotels.com/en/blog/hotel-unico-madrid/castaner"},
 {"n":"TOMS","c":"United States","f":"2006","seg":"casual footwear","d":"Los Angeles company founded by Blake Mycoskie around an adapted alpargata.","lines":[],"eras":[],"sig":["TOMS Alpargata"],"sc":[],"rel":[],"s":W+"Toms_Shoes"},
 {"n":"Soludos","c":"United States","f":"2010","seg":"espadrilles","d":"New York espadrille brand founded by Nick Brown.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://www.glossy.co/fashion/day-in-the-life-soludos-ceo-and-founder-nick-brown/"},
 {"n":"Clarks","c":"United Kingdom","f":"1825","seg":"mainstream footwear","d":"British shoe company from Street, Somerset.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"knowledge"},
 {"n":"Hush Puppies","c":"United States","f":"1958","seg":"casual footwear","d":"American casual shoe brand owned by Wolverine World Wide.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"knowledge"},
 {"n":"Steve Madden","c":"United States","f":"1990","seg":"fashion footwear","d":"New York fashion shoe brand.","lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"knowledge"}]
trads=[
 {"n":"Espadrille making","g":"Textiles & rugs","r":"Catalonia, Aragon and the Basque Country","p":"documented since 1322","d":"Iberian craft of canvas shoes on plaited plant-fibre soles.","tech":"plaited fibre sole stitched to a canvas upper","mat":"esparto or jute, canvas","forms":["Traditional espadrille","Wedge espadrille"],"ctr":["Castañer"],"auth":"","s":ESP},
 {"n":"Swedish clog making","g":"Woodwork & furniture","r":"Southern Sweden (Skåne)","p":"traditional; 22 factories in 1905","d":"Swedish träskor with carved wooden soles, by hand or in factories.","tech":"carved wooden sole; leather upper wet-lasted and nailed","mat":"alder, birch or pine; leather","forms":["Swedish clog"],"ctr":["Troentorp","Vollsjö"],"auth":"","s":TRA}]
notes=("Mule: dropped retail SKUs Lucky Brand Dreya, Mia Ziva, Vionic Opal per plan; kept Clarks, Hush Puppies, Steve Madden as leftover m. "
 "Princetown year not confirmed (only that a 2015 version existed), so y='by 2015'; Gucci Horsebit loafer debut year left out (sources conflict 1952/1953). "
 "Clog: Dutch klomp, Danish træsko and geta left to Traditional footwear. Crocs checked: Wikipedia Clog article names Crocs as the best-known modern clog brand, so it stays here; Classic Clog year not confirmed. "
 "Dansko Professional launch year not found. Sven Clogs not attested, left out. Espadrille: Castañer founding year left blank (sources disagree: 1927 vs Rafael Castañer b. 1776); "
 "Soludos models kept in m. Parallel and Firecrawl tools were out of credit; used WebFetch/WebSearch. Purseblog and Net-a-Porter (Princetown) returned 403 and were not used.")
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes}
p="/home/user/Possession-Taxonomy/rebuild/work/A2/shelves/03_01.json"
json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
