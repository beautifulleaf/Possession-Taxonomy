import sys; sys.path.insert(0,'work/C4/agent')
from rb_lib import *
HW='https://en.wikipedia.org/wiki/Horween_Leather_Company';CY='https://carryology.com/liking/industry/a-guide-to-the-worlds-most-extraordinary-tanneries/'
TD='https://tandyleather.com/pages/shop-categories'
kinds=[
{'n':'Vegetable-tanned leather','a':'veg-tan','d':'Leather tanned with plant tannins, sold as hides, sides or pieces for craft.','t':['tooling','harness','bridle','Tuscan vacchetta','natural','dyed'],'m':[],'s':TD,
 'x':[X('Badalassi Carlo Pueblo','Tuscan vegetable-tanned leather from Badalassi Carlo of Santa Croce sull\'Arno, known for Pueblo and Wax.','Badalassi Carlo',CY,v=[('Pueblo','Badalassi Carlo'),('Wax','Badalassi Carlo')],dt='weight · colour · finish'),
      X('Walpier Buttero','Tuscan vegetable-tanned leather from Walpier of Santa Croce sull\'Arno; the company also makes Toscano.','Walpier',CY,v=[('Buttero','Walpier'),('Toscano','Walpier')],dt='weight · colour'),
      X('Wickett & Craig English Bridle','Vegetable-tanned bridle leather from Wickett & Craig of Curwensville, Pennsylvania, a firm founded in Toronto.','Wickett & Craig',CY,v=[('English Bridle','Wickett & Craig')],dt='weight in oz · colour')]},
{'n':'Chrome-tanned and combination leather','a':'chrome-tan','d':'Leather tanned with chromium salts, or chrome then vegetable, sold for craft.','t':['chrome-tanned','combination-tanned','pull-up','aniline','shell cordovan'],'m':[],'s':TD,
 'x':[X('Horween Chromexcel','Combination-tanned, hot-stuffed pull-up leather developed by Isadore Horween as Aniline Chromexcel in 1911.','Horween',HW,'1911',v=[('Chromexcel','Horween','pull-up, oiled')],dt='weight · colour · finish'),
      X('Horween Shell Cordovan','Leather from the horse rump that Horween is known for; the Chicago Tribune called it the Cordovan capital of the world.','Horween',HW,dt='colour · finish')]},
{'n':'Suede','a':'','d':'Leather finished on the flesh side to a napped surface, sold for craft.','t':['pigskin','goat','cow split','lambskin'],'m':[],'s':TD},
{'n':'Hair-on hide','a':'','d':'Tanned hide with the hair left on, sold as craft material.','t':['cowhide','goat','sheep','deer'],'m':[],'s':TD},
{'n':'Leather lace','a':'','d':'Leather cut into lacing strips, sold for stitching and lacing.','t':['kangaroo','cowhide','deerskin','round lace'],'m':[],'s':TD},
]
brands=[B('Horween','United States','1905','Heritage manufactory','Chromexcel, cordovan','Chicago tannery founded by Isadore Horween, at 2015 North Elston Avenue since 1920.',s=HW,sig=['Horween Chromexcel','Horween Shell Cordovan']),
 B('Badalassi Carlo','Italy','','Heritage manufactory','Tuscan vegetable-tan','Santa Croce sull\'Arno tannery known for Pueblo and Wax.',s=CY,sig=['Badalassi Carlo Pueblo']),
 B('Walpier','Italy','','Heritage manufactory','Buttero','Santa Croce sull\'Arno tannery known for Buttero and Toscano.',s=CY,sig=['Walpier Buttero']),
 B('Wickett & Craig','United States','','Heritage manufactory','bridle leather','Curwensville, Pennsylvania tannery founded in Toronto, known for English Bridle.',s=CY,sig=['Wickett & Craig English Bridle'])]
save('08_00',kinds,brands,[],'Kept all 5 planned kinds. Conceria La Bretagna, Hermann Oak, Tempesta Elbamatt, Dublin not confirmed on fetched pages so left out.')

LC='https://en.wikipedia.org/wiki/Leather_crafting';SW='https://en.wikipedia.org/wiki/Swivel_knife';LK='https://en.wikipedia.org/wiki/Leather_carving';CR='https://projects.makesupply.co/reviews/review-crimson-leather-pricking-irons';SH='https://tandyleather.com/blogs/leathercraft-library/sheridan-style-carving'
kinds=[
{'n':'Leather punch and pricking iron','a':'stitching chisel · diamond chisel','d':'Hand tool made for punching holes or marking stitch positions in leather.','t':['round punch','pricking iron (marks)','diamond chisel (pierces)','hybrid iron','strap end punch'],'m':[],'s':TD,
 'x':[X('French-style pricking iron','Iron that marks stitch positions on the surface, followed by a diamond awl; contrasted with diamond chisels that punch through.','Vergez Blanchard',CR,dt='tooth count · pitch (mm) · tooth angle'),
      X('Crimson Hide pricking iron','Hybrid of a pricking iron and a diamond chisel that leaves a slotted hole slightly bigger than an iron and narrower than a chisel.','Crimson Hide',CR,dt='tooth count · pitch')]},
{'n':'Leather knife','a':'round knife · head knife · skiving knife','d':'Knife for cutting, trimming and thinning leather.','t':['round knife','head knife','skiving knife','clicker knife'],'m':[],'s':LC},
{'n':'Swivel knife','a':'','d':'Knife with a rotating barrel made for carving leather.','t':['standard barrel','ceramic blade','angled blade'],'m':[],'s':TD,
 'x':[X('Swivel knife','Chisel-edged blade on a rotating mount with finger saddle, ground to 30 degrees, used to cut outlines before tooling.','',SW,dt='blade width and angle · barrel style')]},
{'n':'Leather stamping tool','a':'','d':'Metal stamp struck to tool patterns into damp leather.','t':['beveler','pear shader','seeder','veiner','background tool','camouflage tool','geometric'],'m':[],'s':TD,
 'x':[X('Sheridan-style carving','Western floral carving style of wild roses in scroll patterns, developed by Don King of Sheridan, Wyoming, using swivel knife, bevelers, shaders, veiners and background tools.','Tandy Leather',SH,dt='tool set size · stamp series')]},
{'n':'Edge beveller and burnisher','a':'edge slicker','d':'Tools for rounding and polishing the cut edge of leather.','t':['edge beveller','wooden slicker','rotary burnisher'],'m':[],'s':LC},
{'n':'Stitching pony and leather thread','a':'','d':'Clamp to hold leather for hand stitching, with waxed thread.','t':['stitching pony','stitching horse','waxed linen thread','polyester thread'],'m':[],'s':LC},
{'n':'Leather dye','a':'','d':'Dye made for colouring leather.','t':['oil-based','alcohol-based','water-based'],'m':[],'s':TD,
 'x':[X('Leather dyeing','Oil, alcohol and water-based dyes soak into leather pores; water-based dyes penetrate less well.','',LC,dt='carrier · colour · penetration')]},
{'n':'Leather finish','a':'','d':'Sealer, antique or conditioner made to finish leather in leathercraft.','t':['sealer','antique paste','conditioner','resolene-type acrylic'],'m':[],'s':TD},
{'n':'Leathercraft hardware','a':'rivet · snap · buckle','d':'Rivets, snaps, buckles and similar fittings sold loose for leatherwork.','t':['rivet','snap','buckle','D-ring','Chicago screw'],'m':[],'s':TD},
]
brands=[B('Crimson Hide','','','Specialist','pricking irons','Maker of hybrid pricking irons reviewed by Make Supply.',s=CR,sig=['Crimson Hide pricking iron']),
 B('Vergez Blanchard','France','','Heritage manufactory','pricking irons','French-style pricking iron maker.',s=CR),
 B('Tandy Leather','United States','1919','Mainstream','leathercraft supply','Leathercraft retailer and Craftool toolmaker.',s=SH,sig=['Sheridan-style carving'])]
trads=[{'n':'Sheridan-style leather carving','g':'Leather & textile','r':'Sheridan, Wyoming, United States','p':'20th century','d':'Western floral leather tooling of roses in circular scrolls.','tech':'swivel knife outlines, then bevelling, pear shading, veining and background stamping on cased leather','mat':'vegetable-tanned leather','forms':['Leather stamping tool','Swivel knife'],'ctr':['King\'s Saddlery, Sheridan'],'auth':'rose and scroll patterns with shaded detail','s':SH}]
save('08_01',kinds,brands,trads,'Kept all planned kinds. Ritza Tiger Thread, Fiebing\'s, KS Blade, Amy Roke not confirmed from fetched pages, left out. Vergez Blanchard country/mk from the review only generally. Tandy 1919 from knowledge.')

BW='https://en.wikipedia.org/wiki/Basket_weaving';NH='https://nha.org/history-online/nantucket-lightship-baskets/';SM='https://shakermuseum.us/object?id=658';VD='https://www.vandykes.com/chair-cane-glossary/a/74/'
BK='https://www.basketweaving.com/shopsite_sc/store/html/basket-weaving-handle-techniques.html'
kinds=[
{'n':'Basketry willow','a':'withies · osier','d':'Cut willow rods grown and sold for weaving baskets.','t':['brown (unpeeled)','buff','white (peeled)','green'],'m':[],'s':BW,
 'x':[X('Willow wickerwork','Willow valued for flexibility and ease of growing; willow baskets were commonly called wickerwork in England.','',BW,dt='variety · length · processing')]},
{'n':'Basketry cane, reed and splint','a':'ash splint · cane · reed','d':'Cane, reed or wood splint sold for weaving baskets.','t':['flat reed','oval reed','round reed','cane','ash splint','oak splint'],'m':[],'s':BK,
 'x':[X('Reed and cane','Reed is the inner core of the rattan vine and cane its bark; flat reed suits square baskets, oval reed round baskets, round reed twining.','',VD,dt='shape · width · colour')]},
{'n':'Chair-seating cord and tape','a':'','d':'Cord and tape for weaving chair seats.','t':['seagrass','fibre rush','cattail rush','Shaker tape'],'m':[],'s':BK,
 'x':[X('Shaker tape','Woven tape seating used on Shaker slat-back chairs, such as a c. 1840 Mount Lebanon side chair with brown striped tape seat.','',SM,'c. 1840',dt='tape width · material · weave pattern')]},
{'n':'Cane webbing','a':'','d':'Pre-woven cane sheet sold for seating and panels.','t':['standard open mesh','fine mesh','radio weave'],'m':[],'s':BK},
{'n':'Raffia','a':'','d':'Palm-fibre strand sold for weaving and craft.','t':['natural','dyed','paper raffia'],'m':[],'s':'https://www.natuerlich-verpacken.de/raffia-natural-gift-ribbon-250-g'},
{'n':'Basketry and caning tool','a':'','d':'Packing tool, awl, reed gauge or peg made for basketry and caning.','t':['bodkin','packer','cane peg','reed cutter'],'m':[],'s':'http://www.caneweavingsupplies.com/product/commonwealth-basket-basketry-kit/'},
]
trads=[{'n':'Nantucket lightship baskets','g':'Wood & basketry','r':'Nantucket, United States','p':'19th century onward','d':'Island baskets woven on a mold with rattan staves, cane weavers and a solid wood base.','tech':'weaving over a wooden mold','mat':'rattan, cane, wood','forms':['Basketry cane, reed and splint'],'ctr':['Nantucket Lightship Basket Museum'],'auth':'rattan staves, cane weavers, solid wood base','s':NH},
 {'n':'Shaker tape seating','g':'Wood & basketry','r':'New England, United States','p':'19th century','d':'Chair seats woven from coloured tape on Shaker slat-back chairs.','tech':'woven tape seats','mat':'wool or cotton tape','forms':['Chair-seating cord and tape'],'ctr':['Mount Lebanon, New York'],'auth':'tape seat in checkerboard or herringbone weave','s':SM}]
save('08_02',kinds,[],trads,'Merged old kinds as planned. Somerset willow and Japanese bamboo basketry traditions not confirmed on fetched pages (search snippets only), left out. No brands.')

FR='https://bloomist.com/blogs/journal/the-flower-frog-what-it-is-how-to-arrange-with-one';NH2='https://nhm.ac.uk/discover/how-to-press-flowers.html';OA='https://oasisfloralproducts.com/pages/know-foam'
kinds=[
{'n':'Kenzan (pin frog)','a':'flower frog','d':'Heavy base with rows of needles that holds stems in place for ikebana.','t':['round','rectangular','crescent','stainless steel','brass'],'m':[],'s':FR,
 'x':[X('Ikebana kenzan','Rows of brass or steel needles on a heavy base, an essential ikebana tool that let arrangers position each stem deliberately.','',FR,dt='shape · pin density · metal')]},
{'n':'Floral foam','a':'','d':'Absorbent foam made to hold stems in arrangements.','t':['wet foam','dry foam','Maxlife (more degradable)','Midnight (black)','bricks, spheres, wreath bases'],
 'm':[['OASIS Standard Floral Foam Maxlife','Smithers-Oasis (OASIS Floral Products)'],['OASIS Instant Deluxe Floral Foam Maxlife','Smithers-Oasis (OASIS Floral Products)'],['OASIS Midnight Standard Brick','Smithers-Oasis (OASIS Floral Products)'],['OASIS SEC Dry Foam','Smithers-Oasis (OASIS Floral Products)']],'r':[['Maxlife','Smithers-Oasis (OASIS Floral Products)'],['Midnight','Smithers-Oasis (OASIS Floral Products)']],'s':'https://fiftyflowers.com/products/oasis-designer-block'},
{'n':'Florist wire','a':'','d':'Wire made for binding and supporting stems.','t':['stub wire','reel wire','paddle wire'],'m':[['OASIS Florist Wire','Smithers-Oasis (OASIS Floral Products)']],'s':'https://fiftyflowers.com/products/oasis-florist-wire-18-gauge-18-inch'},
{'n':'Floral stem tape','a':'','d':'Stretchy waxed tape made for wrapping flower stems.','t':['green','white','brown'],'m':[],'s':'https://oasisfloralproducts.com/pages/know-foam'},
{'n':'Floral pin','a':'','d':'U-pin or foam pin made to fix stems and moss in arrangements.','t':['U-pin','corsage pin'],'m':[],'s':'https://oasisfloralproducts.com/pages/know-foam'},
{'n':'Flower press','a':'plant press','d':'Boards and straps or screws that hold flowers flat between absorbent sheets to dry.','t':['wooden bolted press','strap press','book press'],'m':[],'s':NH2,
 'x':[X('Herbarium-style pressing','Pressing flowers between newspaper under even weight for days to weeks; museum herbarium sheets survive from the late 1600s.','',NH2,dt='press size · board material')]},
]
brands=[B('Smithers-Oasis','United States','1954','Mainstream','floral foam','Maker of OASIS floral foam, founded 1954.',s=OA,sig=[])]
brands[0].pop('sig')
trads=[{'n':'Ikebana','g':'Wood & basketry','r':'Japan','p':'','d':'Japanese flower arranging stressing space, line and the relation of stems, often using a kenzan.','tech':'stems fixed on kenzan pins; heaven, human and earth principles (shin, soe, hikae)','mat':'cut flowers, branches, kenzan','forms':['Kenzan (pin frog)'],'ctr':[],'auth':'asymmetric line arrangements','s':FR}]
save('08_03',kinds,brands,trads,'Kept all planned kinds; trimmed OASIS models to 4 types. Ikenobo and Sogetsu schools not confirmed on fetched pages, so not named.')
