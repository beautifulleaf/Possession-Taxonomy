import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
W='https://en.wikipedia.org/wiki/'
OR=W+'Origami_paper'; QU=W+'Quilling'; PM=W+'Paper_marbling'; BF=W+'Bone_folder'; BB=W+'Bookbinding'; MT='https://telegramco.com/brand-list/masking-tape-mt/'
CC='https://www.thepapermillstore.com/classic-crest-whitestone-card-stock-35-x-23-in-80-lb-cover-smooth-500-per-carton.html'
o={k['n']:k for k in old('04_00')}
kinds=[
{"n":"Cardstock","a":"cover stock · card base","d":"Heavy paper sold in sheets for card making and scrapbooking.","s":o['Cardstock']['s'],
 "t":["80 lb cover (about 216 gsm)","110 lb cover","smooth","textured","coloured","glitter","sticker (printable)"],
 "x":[X("Classic Crest","Neenah",CC,"Smooth uncoated cover stock in 80 lb (about 216 gsm); the card-making reference sheet.","",dt="80 lb or 110 lb cover · smooth or eggshell · many colours")],
 "m":o['Cardstock']['m']},
{"n":"Patterned craft paper","a":"scrapbook paper · paper pad","d":"Printed decorative paper sold in sheets or pads for scrapbooking and card making.","s":o['Patterned craft paper']['s'],"t":["12 x 12 in sheets","6 x 6 in pad","double-sided","collection / range"],"m":[]},
{"n":"Origami paper","a":"kami · origami sheets","d":"Square paper sheets made for paper folding.","s":OR,
 "t":["kami (75 mm, 6 in, 10 in)","paper-backed foil","washi","chiyogami","tant"],
 "x":[X("Kami","",OR,"Cheapest, thin, easy-to-fold origami paper, developed for schools and printed on one side.","",dt="75 mm · 6 in · 10 in squares"),
      X("Chiyogami (Yuzen)","",OR,"Japanese decorative kozo washi with repeating patterns, once block-printed and now mostly silkscreened.","",dt="kozo washi · patterned"),
      X("Paper-backed foil","",OR,"Thin foil bonded to very thin paper, usually silver or gold.","",dt="")]},
{"n":"Quilling paper","a":"quilling strips","d":"Narrow paper strips sold for rolling into quilled shapes.","s":QU,
 "t":["3 mm","5 mm (most common)","7 mm","10 mm","250+ colours","metallic edge"],
 "x":[X("Quilling strips","",QU,"Strips from about 3 to 10 mm wide, 5 mm most common, rolled on a slotted tool; craft revived in 1875 with the Mosaicon kit.","1875",dt="3, 5, 7, 10 mm")],"m":[]},
{"n":"Washi tape","a":"masking tape · decorative tape","d":"Decorative paper masking tape.","s":o['Washi tape']['s'],
 "t":["single colour","patterned","foil","die-cut","wide roll"],
 "x":[X("mt masking tape","Kamoi Kakoshi",MT,"Decorative washi tape launched in 2006 after three women showed Kamoi crafts made with its industrial masking tape.","2006",dt="single-colour and patterned")],
 "m":o['Washi tape']['m']},
{"n":"Marbling supplies","a":"ebru · suminagashi · marbling kits","d":"Size, colours and combs used to float and transfer marbled patterns onto paper or fabric.","s":PM,
 "t":["carrageenan size","gum tragacanth size","methylcellulose size","ox gall surfactant","acrylic marbling paint","alum mordant"],
 "x":[X("Suminagashi","",PM,"Japanese marbling in which ink floats on plain water and is stirred into designs, captured on washi.","12th century",dt="ink on water"),
      X("Ebru","",PM,"Colours float on a size of gum tragacanth, fenugreek or salep; arose in Persia and Central Asia in the 15th-16th centuries and spread to the Ottoman Empire.","15th-16th century",dt="plant mucilage size"),
      X("Western marbling","",PM,"European marbling for book endpapers, using carrageenan size since the late 19th century.","",dt="carrageenan size")]},
{"n":"Bookbinding tools and materials","a":"bookbinding kit · book cloth · binding board","d":"Needles, thread, board, bookcloth, glue and presses used to bind books by hand.","s":BB,
 "t":["bone folder","awl","bookbinding needle","waxed linen thread","bookcloth","binding board","PVA glue","finishing press"],
 "x":[X("Case binding","",BB,"Most common hardcover method: signatures glued into a text block and attached to a cardboard case covered in paper, cloth, vinyl or leather.","",dt="text block · case"),
      X("Coptic binding","",BB,"Sewing method that stitches pages together through the spine.","",dt="")]},
{"n":"Bone folder","a":"","d":"Smooth flat tool made for creasing and folding paper in bookbinding and card making.","s":o['Bone folder']['s'],
 "t":["bone","Teflon","plastic","bamboo (Japan)","pointed end"],
 "x":[X("Bone folder","",BF,"Dull-edged hand tool of cow or deer leg bone, ivory or plastic for sharp creases; bone is less likely to leave residue.","",dt="bone · Teflon · wood")],"m":[]},
{"n":"Scrapbook album","a":"","d":"Empty album made for scrapbooking.","s":o['Scrapbook album']['s'],"t":["post-bound","strap-hinge","ring binder","12 x 12 in","8.5 x 11 in"],"m":o['Scrapbook album']['m']},
]
brands=[
B("Neenah","United States","","Premium","fine paper","Maker of Classic Crest cover stock.",s=CC,sig=["Classic Crest"]),
B("Kamoi Kakoshi","Japan","","Heritage manufactory","mt washi tape","Japanese adhesive-tape maker; its mt brand began in 2006.",s=MT,sig=["mt masking tape"]),
]
trad=[
{"n":"Paper marbling (ebru and suminagashi)","g":"Paper & Japanese crafts","r":"Japan, Persia and Turkey, Europe","p":"12th century (suminagashi); 15th-16th century (ebru)","d":"Aqueous surface design in which colours float on water or size and are lifted onto paper.","tech":"Colours on water (suminagashi) or on a mucilage size (ebru, Western marbling) are patterned with combs or styluses and printed.","mat":"Size of carrageenan or gum tragacanth; ox gall; acrylic, gouache or oil colours; washi or alum-treated paper","forms":["Suminagashi","Ebru","Western marbled endpapers"],"ctr":["Kyoto","Istanbul"],"auth":"Each print is a unique monotype.","s":PM},
]
write('04_00',kinds,brands,trad,"Bazzill, Origamido, tant specifics left out (no retrieved page), Kamoi Kakoshi name and quill fact from the searches/pages as retrieved (Telegram page says Kamoi). Awl, linen thread and book cloth appear as types of bookbinding materials; the Bookbinding page covers bookcloth and bone folder but not awls or linen thread. Quilling Mosaicon year from the Quilling page.")
