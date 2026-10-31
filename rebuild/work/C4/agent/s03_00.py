import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
H='https://www.hobbycraft.co.uk/knitting-crochet'
RI='https://littleknits.com/collections/malabrigo-rios-yarn?page=2'; JS='https://hillsboroughyarn.com/tag/jamiesons/'; JW='https://www.lovecrafts.com/p/lang-yarns-jawoll'
LB='https://en.wikipedia.org/wiki/Lion_Brand_Yarns'; YW='https://en.wikipedia.org/wiki/Yarn_weight'; IS='https://istex.is/en/vorur/'; RG='https://lovecrafts.com/en-us/p/regia-alpaca-soft'
WE='https://woolandcompany.com/collections/lion-brand-wool-ease'; FT='https://www.woolandcompany.com/products/rowan-felted-tweed-200-barbara'; CS='https://yarn-store.com/yarn/by-brand/cascade/220-superwash/?page=5'
KH='https://www.lovecrafts.com/products/rowan-kidsilk-haze'; BT='https://ayarnstory.co.uk/collections/brooklyn-tweed-1'; DK='https://ritohobby.co.uk/170-drops-karisma-yarn-unicolor-01-off-white'; CT='https://en.wikipedia.org/wiki/Crochet_thread'
kinds=[
{"n":"Wool yarn","a":"knitting wool · worsted · DK","d":"Spun wool yarn sold in balls or skeins for knitting and crochet, graded by Craft Yarn Council weight 0-7.","s":H,
 "t":["lace (0)","fingering (1)","sport (2)","DK (3)","worsted/aran (4)","bulky (5)","super bulky (6)","superwash","tweed","fleece-dyed"],
 "x":[
  X("Cascade 220 Superwash","Cascade Yarns",CS,"100% superwash wool at light worsted to DK weight; the original 220 sets the same gauge guidance.","",dt="light worsted/DK · about 5 sts per inch on US 6-7"),
  X("Rios","Malabrigo",RI,"100% superwash merino worsted, about 210 yards per 100 g hank.","",dt="worsted · 210 yd / 100 g"),
  X("Shelter","Brooklyn Tweed",BT,"Worsted yarn spun in the US from Targhee-Columbia fleece from Wyoming sheep; Loft is fingering and Quarry bulky.","",v=[("Loft","fingering"),("Quarry","bulky")],dt="worsted · fleece-dyed colours"),
  X("Shetland Spindrift","Jamieson's of Shetland",JS,"100% Shetland wool, 2-ply fingering, 115 yards per 25 g skein, over 200 colours; used for stranded colourwork.","",dt="fingering · 200+ colours"),
  X("Lopi","Ístex",IS,"Icelandic wool range from lace Einband to super bulky Jöklalopi.","",v=[("Álafosslopi","bulky"),("Léttlopi","light weight"),("Plötulopi","unspun"),("Fjallalopi","about half Léttlopi thickness")],dt="100% wool except Hosuband"),
  X("Felted Tweed DK","Rowan",FT,"50% wool, 25% alpaca, 25% viscose DK, 191 yards per 50 g.","",dt="DK · 191 yd / 50 g"),
  X("Karisma","Garnstudio",DK,"Superwash-treated 100% wool, 100 m per 50 g.","",dt="superwash")],
 "m":[["128 Superwash","Cascade Yarns"],["Anchor Bay","Cascade Yarns"],["220","Cascade Yarns"],["Woolstok 150","Blue Sky Fibers"],["Woolstok 50","Blue Sky Fibers"],["Woolstok Light","Blue Sky Fibers"],["Woolstok Tweed Aran","Blue Sky Fibers"],["Dos Tierras","Malabrigo"],["Mecha","Malabrigo"],["Hue & Me","Lion Brand"],["Berkshire Bulky","Valley Yarns"],["Haydenville Bulky","Valley Yarns"],["Southwick","Valley Yarns"],["Solstice 4ply","West Yorkshire Spinners"]]},
{"n":"Sock yarn","a":"fingering · 4-ply sock","d":"Fingering-weight wool-nylon yarn made to wear well in knitted socks.","s":JW,
 "t":["wool-nylon blend","superwash","self-striping","reinforcement thread","hand-dyed","fingering (1)"],
 "x":[X("Jawoll","Lang Yarns",JW,"75% wool 25% nylon 4-ply, 210 m per 50 g, sold with a matching reinforcement thread for heels and toes.","",dt="2.5-3.5 mm needles"),
      X("Alpaca Soft","Regia",RG,"Sock-weight blend of 62% wool, 23% polyamide and 15% alpaca, 339 yards per 100 g.","",dt="fingering · 2.5-3.5 mm")],
 "m":[["KPPPM","Koigu"],["Signature 4 Ply","West Yorkshire Spinners"]]},
{"n":"Cotton and plant-fibre yarn","a":"cotton yarn","d":"Yarn spun from cotton or other plant fibres for summer knitting, crochet and dishcloths.","s":YW,
 "t":["mercerised","organic","pima","8/2 weaving cotton","linen","bamboo","hemp"],
 "m":[["Modern Cotton","Berroco"],["Modern Cotton DK","Berroco"],["Organic Worsted Cotton","Blue Sky Fibers"],["Prairie","Blue Sky Fibers"],["Nifty Cotton","Cascade Yarns"],["Ultra Pima","Cascade Yarns"],["Eco Vita 4","DMC"],["Happy Cotton","DMC"],["Knitty 10","DMC"],["Knitty 4","DMC"],["Natura","DMC"],["Samara","DMC"],["Cotton 4 Ply","Paintbox Yarns"],["Cotton DK","Paintbox Yarns"],["Cotton Glacé","Rowan"],["Cotton Trio","Rowan"],["Summerlite 4 Ply","Rowan"],["Summerlite DK","Rowan"],["Bio Bimbo","Sesia"],["Cotton Classic","Tahki Yarns"],["Cotton Supreme","Universal Yarn"],["8/2 Cotton","Valley Yarns"]]},
{"n":"Acrylic and blend yarn","a":"budget yarn · acrylic yarn","d":"Machine-washable acrylic or acrylic-blend yarn at value prices.","s":LB,
 "t":["100% acrylic","acrylic-wool blend","acrylic-nylon","self-striping cakes","novelty (chenille, fur)"],
 "x":[X("Wool-Ease","Lion Brand",WE,"80% acrylic, 20% wool worsted, 197 yards per 85 g; one of Lion Brand's most popular yarns.","",dt="worsted · machine washable")],
 "m":[["Comfort","Berroco"],["Comfort Chunky","Berroco"],["Caron Cakes","Caron"],["Homespun","Lion Brand"],["Rebel 4ply","King Cole"],["Encore Chunky Colorspun","Plymouth Yarn"],["Encore Starz","Plymouth Yarn"],["Hot Cakes","Plymouth Yarn"],["Simply DK","Paintbox Yarns"],["Snuggly DK","Sirdar"],["Special Chunky","Stylecraft"]]},
{"n":"Mohair, alpaca, cashmere and silk yarn","a":"luxury yarn · halo yarn","d":"Soft animal-fibre or silk yarn for lace, halo and next-to-skin knitting.","s":KH,
 "t":["mohair","alpaca","cashmere blend","silk","yak","merino-cashmere"],
 "x":[X("Kidsilk Haze","Rowan",KH,"70% mohair, 30% silk lace-weight, 210 m per 25 g ball.","",dt="lace weight · 25 g")],
 "m":[["Alpaca Classic","Rowan"],["Brushed Fleece","Rowan"],["Softyak DK","Rowan"],["Cashmerino DK","Debbie Bliss"]]},
{"n":"Crochet thread","a":"","d":"Fine tightly spun thread made for crochet and lacework.","s":"https://www.yarnbitsandbobs.com/shop/Threads-Cords--Specialty-Fibers/Crochet--Embroidery-Thread.htm",
 "t":["mercerised cotton","size 3 to 100","size 10 (bedspread weight)","metallic"],
 "m":[["Baroque Crochet Cotton","DMC"],["Cebelia","DMC"],["Metallic Thread","Lizbeth"],["Premium Thread","Lizbeth"]]},
{"n":"Macramé cord","a":"","d":"Twisted or braided cord sold for macramé knotting.","s":H,"t":["3-ply twisted cotton","braided","single strand","recycled cotton","jute"],"m":[]},
]
brands=[
B("Cascade Yarns","United States","","Mainstream","220 wool","US yarn company behind Cascade 220.",s=CS,sig=["Cascade 220 Superwash"]),
B("Malabrigo","Uruguay","","Premium","hand-dyed merino","Maker of Rios worsted merino.",s=RI,sig=["Rios"],s2=None) if False else B("Malabrigo","","","Premium","hand-dyed merino","Maker of Rios worsted superwash merino.",s=RI,sig=["Rios"]),
B("Brooklyn Tweed","United States","","Premium","American wool","US yarn company spinning Targhee-Columbia fleece from Wyoming sheep.",s=BT,sig=["Shelter"]),
B("Jamieson's of Shetland","United Kingdom","","Heritage manufactory","Shetland wool","Shetland spinner of Spindrift in 200+ colours.",s=JS,sig=["Shetland Spindrift"]),
B("Ístex","Iceland","","Heritage manufactory","Lopi","Icelandic wool company in Mosfellsbær making the Lopi range.",s=IS,sig=["Lopi"]),
B("Rowan","United Kingdom","","Premium","knitting yarn","British hand-knit yarn brand with Felted Tweed and Kidsilk Haze.",s=FT,sig=["Felted Tweed DK","Kidsilk Haze"]),
B("Lion Brand","United States","1878","Mainstream","budget yarn","Oldest US producer of knitting and craft yarn, in Carlstadt NJ; owner of Quince & Co since 2023.",s=LB,sig=["Wool-Ease"]),
B("Lang Yarns","Switzerland","","Mainstream","sock yarn","Maker of Jawoll sock yarn.",s=JW,sig=["Jawoll"]),
B("Regia","Germany","","Mainstream","sock yarn","Sock yarn brand with the Alpaca Soft blend.",s=RG,sig=["Alpaca Soft"]),
B("Garnstudio","Norway","","Value","DROPS yarns","Maker of DROPS yarns such as Karisma.",s=DK,sig=["Karisma"]),
]
write('03_00',kinds,brands,[],"Old 53 models distributed by fibre by my judgement (acrylic/cotton/luxury); Paintbox Simply DK, Berroco Comfort etc kept as flat models without confirmation of fibre. Left out: Drops Alpaca/Nepal, Paintbox archetype, Opal sock, Schachenmayr (no retrieved page), Regia core line; Cascade 220 original attested via the Superwash page; Malabrigo, Regia, Lang country omitted. Berroco 'Comfort' placed as acrylic-blend by knowledge.")
