import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
W='https://en.wikipedia.org/wiki/'
H='https://www.hobbycraft.co.uk/sewing/haberdashery'
YK=W+'YKK'; ZI=W+'Zipper'; RI='https://www.riri.com/company/history/'; TH=W+'Sewing_thread'; BU=W+'Button'; SQ=W+'Sequin'
PE='https://lindas.com/pages/pellon-interfacing-complete-product-guide'; HO='https://lindas.com/blogs/tips-and-tricks/the-ultimate-guide-to-hobbs-batting-exploring-every-product-for-your-quilting-needs'
CO=W+'Coats_Group'; AU='https://lindas.com/pages/aurifil-thread'
kinds=[
{"n":"Sewing thread","a":"","d":"Thread made for hand or machine sewing.","s":H,
 "t":["cotton","polyester","core-spun cotton-wrapped polyester","silk","nylon monofilament","metallic","water-soluble","topstitching","40/50/60 wt"],
 "x":[X("Core-spun thread","",TH,"Polyester core wrapped in cotton or polyester staple: strong, slightly stretchy, little lint.","",dt="weight (wt), denier or tex · ply count"),
      X("Mako cotton thread","Aurifil",AU,"Milan family-owned maker of 100% Egyptian Mako cotton thread in 12, 40, 50 and 80 wt.","",dt="12wt, 40wt, 50wt, 80wt"),
      X("Coats thread","Coats",CO,"Paisley thread house descending from J. & P. Coats; apparel, accessory and footwear threads.","1830",dt="")]},
{"n":"Zip","a":"zipper · zip fastener","d":"Zip fastener sold loose for sewing in.","s":H,
 "t":["coil","metal","moulded plastic","invisible","reverse coil (water-resistant)","open-ended (separating)","closed-ended"],
 "x":[X("YKK zip","YKK",YK,"Japanese zip maker founded 1934, with about 45% of the world market.","1934",dt="coil, metal, moulded"),
      X("Riri zip","Riri",RI,"Swiss zip maker of Mendrisio; patented the first die-cast zip on nylon in 1950.","1950",dt="metal and high-tech lines"),
      X("Talon zip","Talon",ZI,"American maker with roots in Gideon Sundback's company; Sundback's 1917 patent set the two-row design.","1917",dt="")]},
{"n":"Button","a":"","d":"Button sold loose for sewing on.","s":H,
 "t":["sew-through (flat)","shank","self-shank","snap fastener","toggle","covered button","shell (mother-of-pearl)","metal","wood","plastic","size in lignes (40 L = 1 in)"]},
{"n":"Interfacing","a":"","d":"Stiffening fabric, fusible or sew-in, made to back other cloth.","s":H,
 "t":["fusible","sew-in","woven","non-woven","knit","fleece"],
 "x":[X("Shape-Flex SF101","Pellon",PE,"Light fusible woven interfacing, popular for bags and garments.","",v=[("931TD Midweight","fusible non-woven, medium"),("906F Sheerweight","fusible non-woven, very light"),("809 Décor-Bond","fusible non-woven, heavy"),("987F Sew-In Midweight","sew-in non-woven")],dt="weight · woven or non-woven · fusible or sew-in")]},
{"n":"Batting","a":"wadding","d":"Non-woven filling sheet sold by the metre or pack for quilting and padding.","s":"https://www.dickblick.com/categories/crafts/",
 "t":["cotton","80/20 cotton-polyester","wool","polyester","silk","low, medium or high loft","fusible","needle-punched"],
 "x":[X("Heirloom","Hobbs",HO,"Hobbs range of cotton, 80/20 blend and wool battings, low to high loft.","",v=[("Heirloom Premium 100% Cotton","low loft"),("Heirloom 80/20 Cotton Blend","low to medium loft"),("Heirloom 100% Wool","high loft")],dt="fibre · loft"),
      X("Tuscany Collection","Hobbs",HO,"Hobbs line in cotton, wool, silk and polyester.","",dt="fibre · loft")]},
{"n":"Ribbon","a":"","d":"Narrow woven strip sold for trimming and sewing.","s":H,"t":["satin","grosgrain","velvet","organza","double-faced","wired"]},
{"n":"Bias binding","a":"bias tape","d":"Bias-cut fabric tape sold loose for binding edges.","s":H,"t":["single fold","double fold","quilt binding","cotton","polyester"]},
{"n":"Elastic","a":"","d":"Stretch tape or cord sold loose for sewing into garments.","s":H,"t":["woven","knitted","braided","clear","waistband","cord"]},
{"n":"Trim","a":"lace · braid · fringe","d":"Lace, braid, fringe or pom-pom edging sold by the metre for sewing on.","s":H,"t":["lace","braid","fringe","pom-pom","rickrack","piping"]},
{"n":"Patch","a":"iron-on patch · sew-on patch","d":"Fabric patch or appliqué sold loose to iron or sew onto cloth.","s":H,"t":["iron-on","sew-on","embroidered","repair patch"]},
{"n":"Sequin","a":"paillette · spangle","d":"Small shiny disc or shape sold loose to sew or glue on.","s":H,
 "t":["centre-hole sequin","top-hole spangle","paillette (large flat)","faceted","cup sequin","vinyl","metal"]},
]
brands=[
B("YKK","Japan","1934","Professional & flagship","zips","World's largest zipper maker, about 45% of the market; founded in Tokyo by Tadao Yoshida.",s=YK,sig=["YKK zip"]),
B("Riri","Switzerland","","Premium","luxury zips","Swiss zip maker of Mendrisio, patented the first die-cast zip on nylon in 1950.",s=RI,sig=["Riri zip"]),
B("Talon","United States","","Heritage manufactory","original zippers","Meadville, Pennsylvania zip maker with roots in Sundback's company.",s=ZI,sig=["Talon zip"]),
B("Coats","United Kingdom","1830","Professional & flagship","thread","Paisley thread maker descended from J. & P. Coats, listed on the London Stock Exchange.",s=CO,sig=["Coats thread"]),
B("Aurifil","Italy","","Premium","Mako cotton thread","Family-owned Milan maker of Egyptian Mako cotton thread.",s=AU,sig=["Mako cotton thread"]),
B("Pellon","United States","","Mainstream","interfacing","US interfacing brand with Shape-Flex, Décor-Bond and sew-in lines.",s=PE,sig=["Shape-Flex SF101"]),
B("Hobbs","United States","","Mainstream","batting","Batting maker with the Heirloom and Tuscany collections.",s=HO,sig=["Heirloom","Tuscany Collection"]),
]
write('02_03',kinds,brands,[],"Gütermann, Mettler, Vilene, Warm & Natural, Quilters Dream not named in any retrieved page, so left out (searches only; Gütermann Wikipedia not found). Riri founding date conflicts across sources (1923 rights purchase, 1924 Halle, 1936 Mendrisio), so left blank. Minor kinds (ribbon, bias binding, elastic, trim, patch) kept as restraint entries with types only.")
