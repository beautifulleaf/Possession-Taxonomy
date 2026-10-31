import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
W='https://en.wikipedia.org/wiki/'
MS='https://www.missouriquiltco.com/blogs/missouri-star-blog/robert-kaufman-textiles-guide'; HT=W+'Harris_tweed'; VL=W+'Vlisco'; IL=W+'Irish_linen'; BL=W+'Belgian_Linen'
GP='https://gearpatrol.com/2018/01/23/great-denim-mills/'; SK=W+'Silk_fabrics'; JE=W+'Jersey_(fabric)'; FE=W+'Felt'; PC='https://lindas.com/pages/fabric-precut-guide-fat-quarters-jelly-rolls-layer-cakes'
DE=W+'Denim'; LB='https://collections.vam.ac.uk/item/O293231/tana-lawn-swatch-book-liberty--co/'
kinds=[
{"n":"Quilting and printed cotton","a":"quilting cotton · cotton fabric · printed lawn","d":"Plain-woven cotton cloth sold by the metre or in precuts for sewing and quilting.","s":"https://www.missouriquiltco.com/collections/fabric-by-the-yard-fby/brand-fabric-traditions",
 "t":["fat quarter (18 x 21 in)","fat eighth","jelly roll (2.5 in strips)","layer cake (10 in squares)","charm pack (5 in squares)","honey bun","solid","print","batik","yarn-dyed","flannel"],
 "x":[X("Kona Cotton Solids","Robert Kaufman",MS,"Quilting solids line with over 365 shades; the plain-colour reference for patchwork.","1984",dt="365+ colours · 100% cotton"),
      X("Essex Linen","Robert Kaufman",MS,"Linen-and-cotton blend from the same house, a standout favourite.","",dt=""),
      X("Tana Lawn","Liberty",LB,"Fine printed cotton lawn from Liberty & Co., London; the V&A holds a 1981 swatch book of its small florals and stripes.","",dt="fine lawn · small-scale florals, stripes")]},
{"n":"Denim","a":"selvedge denim · raw denim","d":"Cotton warp-faced twill, usually indigo, sold for sewing; selvedge is the premium shuttle-loom edge.","s":"https://www.onlinefabricstore.com/?srsltid=AU7gw4VpaeCIAIGAxl5XbMOgX4c0JYgvef1Of0kcpZoNpHHznSZLcwGq",
 "t":["selvedge","raw","stretch (up to 3% elastane)","sanforised","sulphur-dyed black","9-32 oz weight"],
 "x":[X("White Oak selvedge","Cone Denim",DE,"US mill whose selvedge denim long supplied Levi's; the White Oak mill retired its looms at the end of 2017.","",dt="Greensboro NC · shuttle loom"),
      X("Kaihara Denim","Kaihara",GP,"Fukuyama, Japan mill with roots in 1883 indigo weaving; first Japanese rope-dyed denim in 1970.","1970",dt="about 42 million m a year"),
      X("Kurabo KD-8","Kurabo",GP,"Osaka spinner's KD-8, the first Japanese selvedge denim.","",dt=""),
      X("Kuroki Denim","Kuroki",GP,"Ibara, Japan mill founded in 1950 and denim-only within about two decades.","1950",dt="in-house dyeing and weaving"),
      X("Candiani Denim","Candiani",GP,"Family-run Milan mill founded 1938 with a sustainability focus.","1938",dt="")]},
{"n":"Wool cloth and tweed","a":"worsted · flannel · Harris Tweed","d":"Woven wool cloth sold by the metre for coats, jackets and suits; tweed is the rough-textured country cloth.","s":HT,
 "t":["tweed","worsted","flannel","melton","boiled wool"],
 "x":[X("Harris Tweed","Harris Tweed Authority",HT,"Handwoven in the Outer Hebrides from island-dyed, island-spun virgin wool; Orb mark granted 1909 and defined by the 1993 Act.","1909",v=[("Kenneth Mackenzie mill","Stornoway, weaving Harris Tweed since 1906"),("Carloway Mill","smallest of the three mills"),("Harris Tweed Hebrides","Shawbost, reopened 2007")],dt="Orb mark · handwoven · 7.6 million yards peak in 1966")]},
{"n":"Linen fabric","a":"flax linen · Irish linen · Belgian linen","d":"Woven flax cloth sold by the metre, graded by origin labels.","s":BL,
 "t":["Irish linen","Belgian Linen","Masters of Linen","European Flax","damask","handkerchief weight"],
 "x":[X("Belgian Linen","Belgian Flax and Linen Association",BL,"Registered label (since 1960) requiring Belgian companies and at least 85% EU flax; Masters of Linen is the 1995 pan-European label.","1960",dt="Masters of Linen 100% Made in Europe"),
      X("Irish linen","Irish Linen Guild",IL,"Linen from yarn spun in Ireland from 100% flax; Thomas Ferguson & Co still weaves damask.","",dt="Irish Linen Guild logo")]},
{"n":"Silk fabric","a":"habotai · charmeuse · dupioni · shantung","d":"Woven silk cloth sold by the metre, from light habotai to textured dupioni.","s":SK,
 "t":["habotai (habutai)","charmeuse","dupioni","shantung","crêpe de chine","chiffon","organza","noil","tussah","taffeta"],
 "x":[X("Dupioni","",W+"Dupioni","Plain-weave silk with uneven weft yarn from entangled cocoons, popular in bridal and formal wear.","",dt=""),
      X("Charmeuse","",W+"Charmeuse","Satin-weave silk, shiny on one face and matte on the other.","",dt="")]},
{"n":"Knit jersey","a":"jersey · stretch knit","d":"Knitted stretch cloth sold for sewing.","s":"https://hartsfabric.com/fashion-apparel-fabrics/knits/jersey-knit-fabric",
 "t":["single jersey","double jersey","interlock","rib","ponte","stretch (elastane) jersey","cotton","viscose","wool"]},
{"n":"Wax-print fabric","a":"Dutch wax · African wax print · ankara","d":"Printed cotton cloth with a batik-like wax-resist look, sold in six- or twelve-yard pieces.","s":VL,
 "t":["Dutch wax","real wax","java print","fancy print","Chinese imitation"],
 "x":[X("Vlisco Dutch Wax","Vlisco",VL,"Cloth from Helmond, Netherlands, descended from imitation Indonesian batik; stamped 'Guaranteed Dutch Wax Vlisco' since 1963.","1846",v=[("Six Bougies","1945 shipment that sold at once"),("Si tu sors, je sors","bird-cage print with a nickname")],dt="27 treatments over two weeks"),
      X("Woodin","Vlisco",VL,"Group lifestyle brand aimed at young West and Central Africans.","",dt=""),
      X("Uniwax","Vlisco",VL,"Group brand established in 1970 with production in Ivory Coast.","1970",dt=""),
      X("GTP","Vlisco",VL,"Group brand established in 1966 with production in Ghana.","1966",dt="")]},
{"n":"Felt","a":"craft felt · wool felt","d":"Non-woven matted cloth sold as craft or sewing material.","s":"https://www.onlinefabricstore.com/?srsltid=AU7gw4VpaeCIAIGAxl5XbMOgX4c0JYgvef1Of0kcpZoNpHHznSZLcwGq",
 "t":["wool felt","acrylic/rayon felt","wet-felted","needle-felted","pressed felt"]},
]
S="Specialist"
brands=[
B("Robert Kaufman","United States","","Mainstream","Kona Cotton","US family-owned quilting fabric house behind Kona Cotton Solids and Essex Linen.",s=MS,sig=["Kona Cotton Solids","Essex Linen"],lines=["Kona Cotton","Essex Linen","Artisan Batiks","Yarn Dyes","Fusions"]),
B("Liberty","United Kingdom","1875","Premium","Tana Lawn","London department store and fabric house known for printed lawn.",s=LB,sig=["Tana Lawn"]),
B("Vlisco","Netherlands","1846","Premium","wax prints","Helmond textile printer founded 1846, makers of Dutch Wax.",s=VL,sig=["Vlisco Dutch Wax"],lines=["Vlisco","Woodin","Uniwax","GTP"]),
B("Cone Denim","United States","","Heritage manufactory","American selvedge","Maker of White Oak selvedge denim, Greensboro NC.",s=DE,sig=["White Oak selvedge"]),
B("Kaihara","Japan","","Heritage manufactory","denim","Fukuyama, Hiroshima denim mill.",s=GP,sig=["Kaihara Denim"]),
B("Kuroki","Japan","1950","Heritage manufactory","selvedge denim","Ibara, Japan denim mill founded 1950.",s=GP,sig=["Kuroki Denim"]),
B("Kurabo","Japan","1888","Heritage manufactory","denim","Osaka spinner founded 1888 that made Japan's first selvedge denim.",s=GP,sig=["Kurabo KD-8"]),
B("Candiani","Italy","1938","Heritage manufactory","sustainable denim","Family-run Milan denim mill founded 1938.",s=GP,sig=["Candiani Denim"]),
B("Harris Tweed Authority","United Kingdom","1993",  "Institution & issuer","Orb mark","Stornoway statutory body that inspects and stamps Harris Tweed.",s=HT,sig=["Harris Tweed"]),
B("Belgian Flax and Linen Association","Belgium","1960","Institution & issuer","Belgian Linen label","Trade association of over 1,500 flax growers and processors that runs the Belgian Linen mark.",s=BL,sig=["Belgian Linen"]),
B("Irish Linen Guild","Ireland","","Institution & issuer","Irish linen mark","Guild defining Irish linen and issuing its logo.",s=IL,sig=["Irish linen"]),
]
write('02_01',kinds,brands,[],"Moda, Art Gallery, FreeSpirit, Ruby Star, Linton, Abraham Moon, Nihon Menpu left out (no retrieved page named them; Hart's page blocked). Liberty Tana Lawn attested only by a V&A swatch-book record. Precut types in 't'. Felt/Jersey kept as old kinds. Liberty founding 1875 from knowledge.")
