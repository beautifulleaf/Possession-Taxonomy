import sys; sys.path.insert(0,'work/C4/agent')
from rb_lib import *
MT='https://www.perlesandco.co.uk/resources/ft29351-miyuki-vs-toho.html'
PR='https://en.wikipedia.org/wiki/Preciosa_(corporation)'
MU='https://en.wikipedia.org/wiki/Murano_beads'
FP='https://www.firemountaingems.com/learn/F64Z-article.html'
SD='https://potomacbeads.com/blog/superduo-bead-inspiration-products-ideas'
FM='https://www.firemountaingems.com/beads/'
kinds=[
{'n':'Seed bead','a':'rocaille · delica','d':'Small uniform glass bead sold for bead weaving and stringing.','t':['round (rocaille)','cylinder','cube','bugle','triangle','size 15/0 to 8/0','charlotte cut'],'m':[],'s':FM,
 'x':[X('Miyuki Delica','Cylindrical Japanese seed bead with squared, uncut ends and a large hole; sizes include 8/0, 10/0, 11/0 and 15/0, with 11/0 the most used.','Miyuki',MT,v=[('Delica 11/0','Miyuki','about 1.6 mm'),('Delica 8/0','Miyuki','about 3 mm')],dt='size · finish (matte, galvanised, opaque) · colour code'),
      X('Toho Treasure','Cylindrical Toho seed bead, comparable to Delica with a slightly larger hole and less regular shape according to a retailer guide.','Toho',MT,v=[('Treasures 1.8 mm','Toho','about 1.8 mm'),('Treasures 3.3 mm','Toho','about 3.3 mm')],dt='size · finish · colour'),
      X('Round rocaille','Round seed bead, less regular than a Delica and more versatile for stringing, weaving and embroidery; made by Miyuki, Toho and Czech makers.','Miyuki',MT,v=[('Miyuki Rocailles 11/0','Miyuki','about 2 mm'),('Toho Rocailles 11/0','Toho','about 2.2 mm')],dt='size · finish · colour')]},
{'n':'Fire-polished glass bead','a':'Czech fire-polish','d':'Faceted glass bead with fire-polished edges.','t':['round','rondelle','oval','faceted 2 to 12 mm','coated finish'],'m':[],'s':FM,
 'x':[X('Czech fire-polished bead','Faceted pressed-glass bead given a fire-polished finish, a technique developed by Czech glassworkers in the Jablonec region.','',FP,dt='size · facet shape · coating')]},
{'n':'Shaped pressed-glass bead','a':'two-hole bead','d':'Pressed glass bead in a designed shape, often with two holes, for bead weaving.','t':['two-hole','single-hole shaped','tile','cylinder','dagger'],'m':[],'s':SD,
 'x':[X('SuperDuo','Two-hole Czech pressed-glass bead with a pinched oval shape and two 0.8 mm holes.','',SD,dt='size 2.5 by 5 mm · colour · coating')]},
{'n':'Lampwork bead','a':'torch-worked bead','d':'Glass bead formed individually on a mandrel over a torch.','t':['Venetian fiorato','millefiori','foil bead','chevron','handmade artist bead'],'m':[],'s':MU,
 'x':[X('Murano lampwork bead','Bead formed on a mandrel with a torch or air-pump burner, the most time-consuming glass-bead method, with Murano subtypes such as fiorato and foil beads.','',MU,v=[('Fiorato (wedding cake) bead','','rose, swirl and dot overlays'),('Venetian foil bead','','')],dt='technique · size · cane colours')]},
{'n':'Gemstone bead','a':'','d':'Gemstone bead drilled ready for stringing.','t':['round','faceted','nugget','chip','carved'],'m':[],'s':FM},
{'n':'Pearl bead','a':'','d':'Pearl drilled ready for stringing.','t':['freshwater','glass pearl','crystal pearl','shell pearl'],'m':[],'s':FM},
{'n':'Rhinestone and craft stone','a':'','d':'Faceted glass or synthetic stone made to set or glue on.','t':['flatback','sew-on','pointed back','chaton','fancy stone'],'m':[],'s':FM,
 'x':[X('Preciosa crystal stones','Czech crystal stones from the Preciosa group of Jablonec nad Nisou, a maker of cut lead and lead-free crystal.','Preciosa',PR,dt='cut · size (SS) · foil or flatback')]},
{'n':'Craft shell assortment','a':'','d':'Unsorted assortment of shells sold for crafts.','t':[],'m':[],'s':'https://www.seashellsupply.com/shell-assortments'},
]
brands=[
B('Miyuki','Japan','','Specialist','seed beads','Japanese seed-bead maker of Delica cylinder beads and rocailles.',s=MT,sig=['Miyuki Delica','Round rocaille'],lines=['Delica','Rocailles','Bugles','Tila'],rel=['Toho']),
B('Toho','Japan','','Specialist','seed beads','Japanese seed-bead maker of Treasure cylinders and rocailles.',s=MT,sig=['Toho Treasure'],lines=['Treasures','Rocailles','Takumi LH','Demi Round'],rel=['Miyuki']),
B('Preciosa','Czech Republic','1948','Premium','crystal and beads','Jablonec nad Nisou crystal and glass bead group; brand registered 1915, company formed 1948.',s=PR,sig=['Preciosa crystal stones']),
]
save('05_00',kinds,brands,[],'Kept all planned kinds. Swarovski craft-channel claim not confirmed from fetched pages, so left out. Pearl, gemstone and shell kinds carry old data only. Preciosa seed bead rocailles not confirmed on fetched pages.')
