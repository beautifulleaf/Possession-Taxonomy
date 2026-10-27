import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
W='https://en.wikipedia.org/wiki/'
SF=W+'Singer_Featherweight'; SM=W+'Sewing_machine'; EU='https://sewingmachineman.substack.com/p/a-brief-history-of-european-sewing'
JU='https://www.seasonedhomemaker.com/review-new-juki-tl-2010q/'; OV=W+'Overlock'; CV=W+'Coverstitch'; BE=W+'Bernina_International'; JA=W+'Janome'
PF=W+'Pfaff'; S15='https://www.singersewinginfo.co.uk/singer_machines/domestic_machines/models/15/'; LA=W+'Longarm_quilting'
SC='https://www.schmetzneedles.com/blogs/blog/needle-eyes-points-and-tips-matter'; SG='https://www.singer.com/collections/all-singer-machines'; GA='https://gammill.com/'
kinds=[
{"n":"Sewing machine","a":"lockstitch machine · treadle machine · hand-crank machine","d":"Machine that sews seams with a lockstitch; vintage treadle and hand-crank models are types.","s":SG,
 "t":["treadle","hand-crank","mechanical","computerised","straight-stitch only","free-arm","semi-industrial"],
 "x":[
  X("Singer 15","Singer",S15,"Long-lived domestic lockstitch machine named in 1895 from the 1879 Improved Family; its 15x1 needle became a domestic standard.","1895",v=[("15-91 / 15K91","domestic, reverse feed, potted motor"),("15K88","fully reversible feed, droppable feed dogs"),("15K70-73","Japan-only, for kimono sewing")],dt="oscillating shuttle · treadle, hand-crank or electric"),
  X("Singer 221 Featherweight","Singer",SF,"Aluminium portable of about 11 lb, shown at the 1934 World's Fair; 3.0-3.5 million built.","1934",v=[("222K","free-arm, made in Scotland c. 1953-1961 for non-US markets")],dt="aluminium body · self-fastening bobbin case · straight stitch"),
  X("Bernina 530 Record","Bernina",BE,"First Bernina with a patented snap-on presser foot and semi-automatic buttonholes.","1954-1963",v=[("Model 105","first Bernina household machine, 1932"),("Model 125","first electric free-arm zigzag, 1945-1963"),("Model 830 Record","first with electronic foot control, 1971-1982")],dt="clip-on feet · all-metal"),
  X("Elna Lotus","Elna",EU,"Swiss portable whose built-in case opens like a flower; held in MoMA's collection.","",v=[("Elna #1 'Grasshopper'","1940")],dt="Swiss founded 1934"),
  X("Memory Craft 8000","Janome",JA,"First home machine with professional-style embroidery (1990); follows the Memory 7 of 1979.","1990",dt="computerised embroidery"),
  X("Heavy Duty","Singer",SG,"Current metal-frame family from the Singer range, sold as 4411, 4423, 4432, 4452, 4511, 4523, 4532, 4552, 6600C and Smart 9120.","",v=[("4452","32 stitches, extra-high speed, metal frame"),("9120 Smart Heavy Duty","app-connected, sewing or sewing-and-embroidery")],dt="metal frame · mechanical or computerised"),
  X("TL-2010Q","Juki",JU,"Single-needle straight-stitch quilting machine with a large harp space, designed for quilters.","",dt="straight stitch only · speed control · extension table"),
 ],
 "m":[["Innov-is A150","Brother"],["Innov-is A80","Brother"],["Innov-is NV1800Q","Brother"],["CS7000X","Brother"],["Emerald 118","Husqvarna Viking"],["Opal 670","Husqvarna Viking"],["Patchwork 7285Q","Singer"],["Quantum Stylist 9960","Singer"],["M1500","Singer"],["Gem","White Sewing Machine Company"],["105","Bernina"]]},
{"n":"Overlocker","a":"serger · overlock machine","d":"Machine that trims, seams and overcasts an edge in one pass with looper threads.","s":SG,
 "t":["3-thread","4-thread","5-thread","differential feed","air-threading","industrial 2-thread"],
 "x":[X("Baby Lock","Tacony",OV,"Home overlocker introduced to the US market by Nick Tacony, letting home sewers finish seams.","",dt="3-4 thread"),
      X("Home overlocker","Juki",OV,"Compact overlocker from the 1964 proposal of Japanese engineers who left their employer to found Juki.","1964",dt="")],
 "m":[["Heavy Duty 0420 Serger","Singer"],["Heavy Duty 0460 Serger","Singer"],["S0080 Serger","Singer"]]},
{"n":"Coverstitch machine","a":"coverhem machine · cover stitch","d":"Machine that sews parallel rows with a looper underneath for stretch hems and trims on knits.","s":CV,
 "t":["2-needle","3-needle","4-thread","combination overlocker-coverstitch"],
 "x":[X("Coverstitch (ISO 406/407)","",CV,"Two- or three-needle stitch with a looper on the reverse; used for knit hems, necklines and trim.","",dt="2 or 3 needles · looper thread on the outside for decoration")]},
{"n":"Embroidery machine","a":"","d":"Machine that stitches embroidery designs automatically from a hoop.","s":SG,
 "t":["embroidery-only","sewing and embroidery combination","multi-needle"],
 "x":[X("Memory Craft 8000","Janome",JA,"First home machine with professional-style embroidery, 1990.","1990",dt="")],
 "m":[["AVENEER EV1","Brother"],["Designer Quartz 29","Husqvarna Viking"],["SE9180","Singer"],["Smart Heavy Duty 9120 Sewing and Embroidery","Singer"]]},
{"n":"Longarm quilting machine","a":"","d":"Long-throat machine on a frame made for quilting through layered fabric.","s":GA,
 "t":["hand-guided","computer-guided","10-14 ft frame"],
 "x":[X("Statler","Gammill",GA,"Computerised Gammill longarm; Statler Ascend is the upgraded version.","",v=[("Statler Ascend","upgraded Statler")],dt="computerised"),
      X("Vision 2.0","Gammill",GA,"Hand-guided Gammill longarm.","",dt="hand-guided")]},
{"n":"Sewing machine needle","a":"","d":"Needle made for a sewing machine, chosen by point and size.","s":SC,
 "t":["Universal","Ballpoint/Jersey","Microtex (sharp)","Embroidery","Quilting","Denim","Metallic","Hemstitch","Super NonStick","twin needle"],
 "x":[X("Universal needle","SCHMETZ",SC,"Slightly rounded point for woven and knit fabrics; fits most household machines (system 130/705 H).","",dt="size 70/10 to 110/18"),
      X("Microtex Chrome","SCHMETZ",SC,"Very slim, sharp, chrome-plated needle for microfibres, silk and coated cloth; purple code.","",dt=""),
      X("Embroidery (Jersey) needle","SCHMETZ",SC,"Medium ballpoint needle that slips between knit fibres.","",dt="")],
 "m":[["Embroidery Needle","Organ"]]},
{"n":"Sewing machine feet and spare parts","a":"presser feet · bobbins · needle plates","d":"Presser feet, bobbins, bobbin cases, needle plates, extension tables and oil to fit a given machine.","s":"https://www.janome.com/product-category/accessories/sewing-machine-feet",
 "t":["presser foot","bobbin","bobbin case","needle plate","extension table","machine oil"],
 "m":[["9-groove Pintuck Foot","Bernina"],["Gathering Foot","Bernina"],["Ultra Glide Foot","Janome"],["Tricot Foot","Janome"],["Zig-Zag Foot A","Janome"],["Walking foot (even feed)",""],["Zipper foot",""],["Quarter-inch foot",""],["Buttonhole foot",""],["Blind-stitch foot",""],["Binding foot",""],["Sew Steady Classic Table for the Singer Featherweight","Sew Steady"],["Sew Steady Large Deluxe Table","Sew Steady"],["Class 66 bobbin",""]]},
]
brands=[
B("Singer","United States","1851","Heritage manufactory","sewing machines","American maker whose founder Isaac Merritt Singer took a US patent in 1851.",s=SM,sig=["Singer 15","Singer 221 Featherweight","Heavy Duty"]),
B("Bernina","Switzerland","1893","Premium","Swiss sewing machines","Family-owned Swiss maker; the Bernina name dates to 1932.",s=BE,sig=["Bernina 530 Record"],rel=["Bernette"]),
B("Elna","Switzerland","1934","Premium","portable machines","Swiss brand founded 1934, now owned by Janome.",s=EU,sig=["Elna Lotus"],rel=["Janome"]),
B("Janome","Japan","1921","Premium","computerised machines","Tokyo maker; Memory 7 (1979) was the first home computerised machine.",s=JA,sig=["Memory Craft 8000"],rel=["Elna"]),
B("Pfaff","Germany","1862","Premium","German machines","Kaiserslautern maker founded by Georg Michael Pfaff, now owned by SGSB.",s=PF),
B("Juki","Japan","","Professional & flagship","quilting and industrial","Japanese maker founded by engineers who proposed a compact home overlocker in 1964.",s=OV,sig=["TL-2010Q"]),
B("Brother","Japan","","Mainstream","home machines","Japanese maker; acquired the William Jones sewing machine factory in 1968.",s=SM),
B("Tacony","United States","","Specialist","Baby Lock","US company whose founder Nick Tacony introduced the Baby Lock overlocker.",s=OV),
B("Husqvarna Viking","Sweden","","Premium","Swedish machines","Swedish brand with origins in the 1870s, owner of Pfaff since 1999.",s=EU),
B("Gammill","United States","","Specialist","longarm quilters","US maker of Statler and Vision longarm quilting machines.",s=GA,sig=["Statler","Vision 2.0"]),
B("SCHMETZ","Germany","","Specialist","needles","German maker of sewing machine needles in the 130/705 H system.",s=SC,sig=["Universal needle","Microtex Chrome"]),
]
write('02_00',kinds,brands,[],"Pfaff 130, Singer 201, Elna Supermatic, Necchi BU/Supernova, Brother Innov-is archetype, Janome MC15000 left out (no retrieved page confirmed them; Singer 201 only a parts-store title; Necchi Mirella mentioned but no detail). Heavy Duty SKU run collapsed to one archetype. Spare parts collapsed to one entry. Organ needle kept in m. Bobbin/needle-plate/oil kinds merged as types.")
