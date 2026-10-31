import sys; sys.path.insert(0,'work/C4/agent')
from rb_lib import *
UR='https://en.wikipedia.org/wiki/Uroboros_Glass';CG='https://www.creativeglassguild.co.uk/blog/oceanside-glasstile-and-the-future-of-coe96'
LW='https://en.wikipedia.org/wiki/Lampworking';JM='https://www.journeymanhq.com/?p=755971';BU='https://en.wikipedia.org/wiki/Bullseye_Glass';TL='https://en.wikipedia.org/wiki/Tiffany_lamp';MB='https://en.wikipedia.org/wiki/Murano_beads'
MA='https://mosaicartsupply.com/product-category/stained-glass-tools'
kinds=[
{'n':'Stained-glass sheet','a':'art glass · fusing glass','d':'Coloured glass sheet sold for stained-glass work.','t':['cathedral (transparent)','opalescent','streaky','antique mouth-blown','fusing COE 90','fusing COE 96'],'m':[],'s':'https://mosaicartsupply.com/product-category/stained-art-glass/stained-glass/',
 'x':[X('Bullseye sheet glass','Portland, Oregon art glass maker founded 1974, a major supplier of raw glass to fused-glass artists.','Bullseye Glass',BU,'1974',dt='colour · opalescence · compatible glass system'),
      X('Spectrum and Uroboros (System 96)','COE 96 soft flat glass whose production passed to Oceanside Glasstile after Spectrum and Uroboros were due to close; Uroboros was founded by Eric Lovell in 1973.','Oceanside Glasstile',CG,'1973',v=[('Uroboros','Uroboros Glass','Portland firm, name retired by Oceanside in 2017'),('System 96','Youghiogheny Opalescent Glass','licensing taken over in 2019')],dt='colour · texture · COE 96'),
      X('Youghiogheny opalescent glass','Connellsville, Pennsylvania glassmaker that bought the Uroboros business from Oceanside in 2019 and took over System 96.','Youghiogheny Opalescent Glass',UR,dt='colour · opalescence')]},
{'n':'Copper foil and lead came','a':'','d':'Copper foil tape wrapped on glass edges, or grooved lead strips, that hold pieces together before soldering.','t':['copper foil (black, silver or copper back)','lead came','zinc came','brass came'],'m':[],'s':TL,
 'x':[X('Tiffany copper-foil method','Each glass piece is wrapped in thin copper foil and soldered, used by Tiffany Studios for lamp shades instead of lead came.','',TL,'1890s',dt='foil width · backing colour · solder finish')]},
{'n':'Stained-glass solder and flux','a':'','d':'Solder and flux made for joining stained-glass pieces.','t':['60/40 tin-lead','lead-free','gel flux','paste flux'],'m':[['Amerway 60/40 Lead-Tin Wire Solder','Amerway'],['Old Masters Gel Flux','Novacan']],'s':MA},
{'n':'Glass cutter','a':'','d':'Hand tool made for scoring glass.','t':['oil-filled','pistol grip','pencil grip','carbide wheel'],'m':[['Custom-Grip Supercutter','Toyo']],'s':MA},
{'n':'Glass pliers','a':'running pliers · grozing pliers','d':'Pliers made for breaking and nibbling scored glass.','t':['running pliers','breaking pliers','grozing pliers'],'m':[['Heavy Duty 8-inch Running Pliers','Leponitt']],'s':MA},
{'n':'Glass grinder','a':'','d':'Bench grinder made for smoothing cut stained glass.','t':['benchtop wet grinder','ring saw'],'m':[['Super Star II Electric','Glastar']],'s':MA},
{'n':'Glass-fusing kiln','a':'','d':'Kiln made only for fusing and slumping glass.','t':['top lid','clamshell','front loading','tabletop'],
 'm':[['Paragon Fusion 8','Paragon'],['Skutt FireBox 8','Skutt'],['Skutt FireBox 14','Skutt'],['Skutt GM-1014','Skutt'],['Skutt GM-1414','Skutt']],'r':[['GlassMaster','Skutt']],'s':'https://skutt.com/?p=76'},
{'n':'Lampwork torch and glass rod','a':'flameworking','d':'Torch and glass rods used to melt and shape glass beads and objects by hand.','t':['soft glass (soda-lime)','borosilicate','single-fuel torch','oxy-propane'],'m':[],'s':LW,
 'x':[X('Soft-glass lampworking','Lampworking melts glass rod with a torch; soft soda-lime or lead glass melts at lower temperature and is the most common, while borosilicate needs more heat.','',LW,dt='glass type · torch fuel · rod diameter')]},
]
brands=[
B('Bullseye Glass','United States','1974','Premium','fusing glass','Portland, Oregon maker of art glass for fusing, founded by Schwoerer, Lundstrom and Ahlgren.',s=BU,sig=['Bullseye sheet glass']),
B('Oceanside Glasstile','United States','','Premium','glass tile and sheet','Carlsbad, California producer that took over Spectrum and Uroboros glass production.',s=CG,sig=['Spectrum and Uroboros (System 96)']),
B('Youghiogheny Opalescent Glass','United States','','Heritage manufactory','opalescent glass','Connellsville, Pennsylvania glassmaker that acquired the Uroboros business in 2019.',s=UR,sig=['Youghiogheny opalescent glass']),
B('Toyo','Japan','','Premium','glass cutters','Japanese glass-cutter maker; its Supercutter is a common stained-glass choice.',s=JM),
B('Glastar','United States','','Specialist','glass grinders','Californian glassworking tool maker, known for the Super Star II grinder.',s=JM),
]
trads=[{'n':'Tiffany copper-foil glasswork','g':'Ceramics & glass','r':'United States','p':'1890s onward','d':'Assembly of lamp shades and window sections from glass wrapped in copper foil and soldered.','tech':'copper foil wrap and solder over numbered templates','mat':'art glass, copper foil, solder','forms':['Copper foil and lead came','Stained-glass solder and flux'],'ctr':['Tiffany Studios, Corona, Queens'],'auth':'foil-soldered seams in place of lead came','s':TL},
 {'n':'Murano lampwork','g':'Ceramics & glass','r':'Venice, Italy','p':'14th century onward','d':'Venetian torch-formed glass beads and objects, with fiorato and foil beads as signature forms.','tech':'lampworking on a mandrel with a torch','mat':'soft glass rod','forms':['Lampwork torch and glass rod'],'ctr':['Murano'],'auth':'individually formed beads','s':MB}]
save('07_00',kinds,brands,trads,'Kept all planned kinds, added Copper foil and lead came and Lampwork torch and glass rod. Kokomo, Wissmach, Lamberts, Effetre/Moretti, Hot Head, Nortel, Inland not confirmed on fetched pages, so left out. Tool models (Toyo, Glastar, Leponitt, Amerway, Novacan) are from the journeymanhq tool list.')

OR='https://i-m-magazine.com/business/orsoni-venezia-1888/';BZ='https://www.ganoksin.com/article/square-shaped-treasures-made-glass/';WN='https://mosaicshop.eu/blogs/nieuws/using-wheeled-glass-nipper-mosaic';MO='https://en.wikipedia.org/wiki/Mosaic'
MT='https://mosaicartsupply.com/product-category/glass-mosaic-tile/'
kinds=[
{'n':'Mosaic tile','a':'tessera','d':'Small tile or tessera sold for mosaic work.','t':['smalti','vitreous glass','stained glass cut','ceramic','marble and stone','gold-leaf glass'],'m':[['Morjo','Mosaic Art Supply'],['Thinny Pennies','Mosaic Art Supply']],'s':MT,
 'x':[X('Venetian smalti','Hand-cut opaque glass enamel tesserae made from sand, soda and metal oxides melted at 1,300 C, made by Orsoni in Venice since 1888.','Orsoni',OR,'1888',dt='colour (thousands of shades) · gold-leaf option · cut'),
      X('Bisazza glass mosaic','Italian glass tesserae maker founded in 1956; Le Gemme tesserae use powdered aventurine for a copper-toned sparkle.','Bisazza',BZ,'1956',v=[('Le Gemme','Bisazza','aventurine glass'),('Oro','Bisazza','24-karat gold foil between glass'),('Opus Romano','Bisazza','for heavy-traffic floors')],dt='series · colour')]},
{'n':'Mosaic nippers','a':'tile nippers','d':'Nippers made for shaping tile and glass tesserae.','t':['wheeled nippers','compound nippers','hammer and hardie'],'m':[],'s':MA if False else 'https://mosaicartsupply.com/product-category/stained-glass-tools',
 'x':[X('Wheeled mosaic nippers','Nippers with two hardened cutting wheels that clamp the tile and score it at one point; break is more predictable on glass than ceramic.','',WN,dt='wheel material · handle size')]},
{'n':'Mosaic grout','a':'','d':'Grout sold for filling the joints of mosaic work.','t':['sanded','unsanded','epoxy','coloured'],'m':[],'s':'https://mosaicartsupply.com/product-category/stained-glass-tools'},
{'n':'Mosaic base','a':'','d':'Backer board, mesh or form sold as the base for a mosaic.','t':['cement board','mesh','wood panel','3D form'],'m':[],'s':'https://mosaicartsupply.com/product-category/stained-glass-tools'},
]
brands=[B('Orsoni','Italy','1888','Heritage manufactory','Venetian smalti','Venice live-fire furnace founded by Angelo Orsoni, bought by the TREND Group in 2003.',s=OR,sig=['Venetian smalti']),
 B('Bisazza','Italy','1956','Premium','glass mosaic','Italian glass mosaic producer founded by Renato Bisazza.',s=BZ,sig=['Bisazza glass mosaic'])]
trads=[{'n':'Roman and Byzantine mosaic','g':'Ceramics & glass','r':'Mediterranean','p':'3rd century BC to 15th century','d':'Mosaic from stone and handmade glass tesserae, from Roman opus tessellatum to golden Byzantine church interiors.','tech':'tesserae set in plaster or mortar; opus vermiculatum for fine detail','mat':'stone, glass enamel, gold','forms':['Mosaic tile','Mosaic nippers'],'ctr':['Constantinople','Venice'],'auth':'hand-cut tesserae set unevenly','s':MO}]
save('07_01',kinds,brands,trads,'Kept all 4 planned kinds. Leponitt nippers (no fetched page names the brand) and ceramic/stone tesserae not added.')

AR='https://www.artresin.com/blogs/artresin/casting-resin-vs-epoxy-resin';AM='https://www.artmolds.com/blogs/life-casting/epoxy-vs-polyurethane-resins-what-s-the-real-difference';MS='https://www.smooth-on.com/tb/files/MOLD_STAR_15_16_30_TB.pdf'
kinds=[
{'n':'Casting resin','a':'','d':'Two-part resin sold for craft casting.','t':['epoxy','polyurethane','polyester','UV resin','deep-pour','coating (art) resin'],'m':[['Gedeo Crystal Resin','Gedeo']],'s':'https://www.fredaldous.co.uk/collections/casting-materials',
 'x':[X('ArtResin','Two-part epoxy art resin with honey-like consistency and UV stabilisers, mixed 1:1 and fully cured in about three days.','ArtResin',AR,dt='epoxy · mix ratio 1:1 · layer depth about 1/8 to 1/4 in'),
      X('Polyurethane casting resin','Flexible, fast-hardening resin family (as little as 48 hours) that resists UV yellowing better than epoxy; contrasted with rigid epoxy.','ArtMolds',AM,dt='shore hardness · pot life · demould time')]},
{'n':'Mould-making rubber','a':'silicone rubber · latex','d':'Liquid or putty rubber sold to make flexible moulds.','t':['platinum-cure silicone','tin-cure silicone','latex','putty silicone'],'m':[],'s':'https://www.fredaldous.co.uk/collections/mould-making',
 'x':[X('Smooth-On Mold Star','Platinum silicone mixed 1A:1B by volume in 15 SLOW, 16 FAST and harder 30 grades; will not cure against sulfur surfaces.','Smooth-On',MS,v=[('Mold Star 15 SLOW','Smooth-On','50-minute pot life'),('Mold Star 16 FAST','Smooth-On','6-minute pot life'),('Mold Star 30','Smooth-On','30A Shore hardness')],dt='shore hardness · pot life · cure time')]},
{'n':'Craft mould','a':'silicone mould','d':'Mould made for craft casting in resin or plaster.','t':['silicone','polypropylene','rubber'],'m':[],'s':'https://www.fredaldous.co.uk/collections/mould-making'},
{'n':'Alginate moulding powder','a':'','d':'Seaweed-based powder mixed with water for quick life-casting moulds.','t':['fast set','slow set','dental grade'],'m':[],'s':'https://www.fredaldous.co.uk/collections/mould-making'},
{'n':'Casting plaster','a':'','d':'Plaster powder sold for craft casting and modelling.','t':['plaster of Paris','pottery plaster','dental stone'],'m':[],'s':'https://www.fredaldous.co.uk/collections/casting-materials'},
{'n':'Plaster bandage','a':'','d':'Gauze impregnated with plaster, sold for casting and modelling.','t':[],'m':[],'s':'https://www.fredaldous.co.uk/collections/clay'},
]
brands=[B('ArtResin','Canada','','Mainstream','art epoxy','Maker of a non-toxic, low-odour epoxy art resin.',s=AR,sig=['ArtResin']),
 B('Smooth-On','United States','','Professional & flagship','silicone rubbers','Maker of platinum silicone and urethane moulding and casting products.',s=MS,sig=['Smooth-On Mold Star'])]
save('07_02',kinds,brands,[],'Kept all 6 planned kinds. Resin Obsession, Alja-Safe, Ecoflex not confirmed on fetched pages; ArtResin country from knowledge (Canada).')
