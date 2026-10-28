from lib import *
W='https://en.wikipedia.org/wiki/'
d=load(); bj=load(B)
def ax(kn,a,pos=None):
    k=kind(d,kn); x=k.setdefault('x',[])
    if any(i['n']==a['n'] for i in x): return
    if pos is None: x.append(a)
    else: x.insert(pos,a)
def find(kn,an):
    return [i for i in kind(d,kn)['x'] if i['n']==an][0]

# ---- paints
a=find('Watercolour paint','Schmincke Horadam Aquarell'); a['y']='1881'
a['dt']='half pans and 15 ml tubes · 180 colours incl. 92 single-pigment and 22 granulating · Akademie is the student line'
a['s']='https://www.cowlingandwilcox.com/blog/post/203-lets-think-schmincke'
a['v']=[ver('Akademie Aquarell','Schmincke','student-grade counterpart')]
a=find('Oil paint','Schmincke Mussini'); a['y']='1881'; a['s']='https://www.cowlingandwilcox.com/blog/post/203-lets-think-schmincke'
a['d']='German resin-oil paint, the first Schmincke product, named after Cesare Mussini.'
a=find('Watercolour paint','Daniel Smith Extra Fine Watercolor'); a['s']=W+'Daniel_Smith_(art_materials)'
a['v']=[ver('PrimaTek','Daniel Smith','pigments from semi-precious minerals and geological deposits such as lapis lazuli and amethyst')]
a['y']='1976'
a=find('Watercolour paint','Winsor & Newton Professional Water Colour')
a['v']=a.get('v',[])+[ver('Cotman','Winsor & Newton','student-grade watercolour and synthetic brush line')]
a['s']=W+'Winsor_%26_Newton'
a=find('Gouache','Winsor & Newton Designers Gouache'); a['y']='1937'; a['s']=W+'Winsor_%26_Newton'
liq=arch('Liquitex Heavy Body','Liquitex','Thick-bodied artists\' acrylic that holds brush and knife marks.',W+'Liquitex','1963',
 'tubes and jars · artist grade · thick body',[ver('Soft Body','Liquitex','thinner water-based acrylic sold from 1956','1956'),ver('Basics','Liquitex','student-priced line'),ver('Professional','Liquitex','artist-grade umbrella line incl. paint markers and Acrylic Ink')])
ax('Acrylic paint',liq,0)
find('Acrylic paint','Liquitex Soft Body')['y']='1956'
find('Acrylic paint','Liquitex Soft Body')['s']=W+'Liquitex'
# ---- brushes
a=find('Watercolour and soft-hair brush','Series 7'); a['y']='1866'; a['s']='https://www.winsornewton.com/products/series-7-kolinsky-sable-brush-series-7-kolinsky-sable-round'
a['d']='Kolinsky sable round made by hand in England; the 1866 standard is set by Queen Victoria\'s No. 7 request.'
a['dt']='round · sizes 000 to 12 · short handle · seamless nickel-plated ferrule'
a=find('Watercolour and soft-hair brush','Da Vinci Maestro'); a['s']='https://www.cassart.co.uk/da-vinci-maestro-kolinsky-sable-watercolour-round-brush-extra-fine-point'
a['d']='Red Siberian Kolinsky sable round from selected male winter tails, listed as Series 10.'
a['dt']='round, extra-fine point · 20 sizes · short black polished handle · seamless silver ferrule'
ax('Oil and acrylic brush',arch('Galeria brushes','Winsor & Newton','Synthetic-fibre brush line made for acrylic paint.',W+'Winsor_%26_Newton',dt='synthetic fibre · acrylic range'))
ax('Oil and acrylic brush',arch('Winton brushes','Winsor & Newton','Natural-hair student brush line sold with Winton oil colour.',W+'Winsor_%26_Newton',dt='natural hair · student range'))
# ---- pencils & markers
a=find('Coloured pencil','Polychromos'); a['y']='1908'; a['s']=W+'Faber-Castell'
a=find('Coloured pencil','Luminance'); a['y']='2010'; a['s']=W+"Caran_d'Ache_(company)"
a=find('Coloured pencil','Premier'); a['s']=W+'Prismacolor'; a['y']='1938'
a['v']=[ver('Premier Soft Core','Prismacolor','soft wax-based colour pencil'),ver('Col-Erase','Prismacolor','erasable colour pencil'),ver('Verithin','Prismacolor','hard-core colour pencil'),ver('Premier Water-Soluble','Prismacolor','water-soluble colour pencil'),ver('Scholar','Prismacolor','student line')]
a['d']='Soft wax-based Prismacolor pencil, introduced under the brand by Eagle Pencil Company in 1938.'
ax('Alcohol markers',arch('Promarker','Winsor & Newton','Winsor & Newton alcohol marker range.',W+'Winsor_%26_Newton',dt='alcohol-based',v=[ver('Promarker Brush','Winsor & Newton','brush-nib version'),ver('Promarker Watercolour','Winsor & Newton','watercolour-effect version')]))
a=find('Paint markers','Posca'); a['y']='1983'; a['s']='https://shop.stlartsupply.com/products/uni-posca-paint-marker-pointed-fine-tip-pc-1m'
a['d']='Water-based opaque paint marker from Mitsubishi Pencil, launched in Japan in 1983.'
a['dt']='water-based opaque ink · permanent on porous surfaces'
a['v']=[ver(n,'Uni Mitsubishi Pencil',t) for n,t in [('PC-1MR','extra-fine tip'),('PC-1M','pointed fine tip, 0.7 mm'),('PC-3M','fine tip'),('PC-5M','medium tip'),('PC-8K','broad chisel tip'),('PCF-350','brush tip')]]
a=find('Fineliner and technical drawing pen','Pigment Liner'); a['s']='https://www.penaddict.com/blog/2012/3/9/staedtler-pigment-liner-03-mm-review.html'
a['d']='Archival pigment fineliner; reviewed as close to the Sakura Pigma Micron in ink and build, with a slightly softer tip.'
a=find('Fineliner and technical drawing pen','Pigma Micron')
a['dt']='tips 005 (0.2 mm) to 08 (0.5 mm) in the standard black set'
a['s']='https://www.penaddict.com/blog/2012/3/9/staedtler-pigment-liner-03-mm-review.html'
for kn,an,note in [('Brush pens','No. 40 Brush Pen','sable-hair tip, refillable')]: pass
# ---- pastels
ps='https://finearttutorials.com/?p=9863'
ax('Soft pastels',arch('Terry Ludwig Soft Pastels','Terry Ludwig','Medium-soft stick, firmer than Sennelier, Unison and Schmincke; 750 colours listed.',ps,dt='medium soft · 750 colours'))
ax('Soft pastels',arch('Art Spectrum Extra Soft','Art Spectrum','Medium-soft stick listed between Rembrandt and Terry Ludwig in hardness.',ps,dt='medium soft'))
ax('Soft pastels',arch('Mount Vision','Mount Vision','Medium-hardness handmade pastel by Karl Kelly, started in New York.',ps,dt='medium · firmer end of scale'))
# ---- paper
a=find('Sketchbook','Stillman & Birn sketchbook system'); a['s']='https://www.wellappointeddesk.com/2014/06/10/stillman-birn-paper-sampler/'
a['v']=[ver('Alpha','Stillman & Birn','150 gsm, cold-press, some tooth'),ver('Beta','Stillman & Birn','270 gsm, cold-press'),ver('Gamma','Stillman & Birn','150 gsm, warm ivory'),ver('Delta','Stillman & Birn','270 gsm, ivory, some texture'),ver('Epsilon','Stillman & Birn','150 gsm, smooth'),ver('Zeta','Stillman & Birn','270 gsm, smooth')]
a['dt']='six paper series · 150 or 270 gsm · cold-press, ivory or smooth'
ax('Sketchbook',arch('Moleskine sketchbook','Moleskine','Sketch format of the sewn notebook with rounded corners and elastic closure.',W+'Moleskine','1997','rounded corners · elastic band · ribbon marker · rear pocket'))
# ---- yarn & beads & clay
ax('Cotton and plant-fibre yarn',arch('Handknit Cotton','Rowan','100% cotton yarn, 92 yd per 50 g, made in Hungary.','https://theknittingloft.ca/collections/yarn/products/rowan-handknit-cotton',dt='4-4.5 mm needles · 100% cotton'))
a=find('Seed bead','Miyuki Delica'); a['dt']='sizes 15/0 to 8/0, 11/0 most common · cylindrical · thin wall, large hole'; a['s']='https://artbeads.com/toho-vs-miyuki-seed-beads-understanding-the-differences/'
ax('Seed bead',arch('Toho Aiko','Toho','Machine-cut cylindrical bead with a large hole for bead weaving and embroidery.','https://artbeads.com/toho-vs-miyuki-seed-beads-understanding-the-differences/','',dt='11/0 · silver-lined, gold-lined, rainbow finishes'))
bs='https://www.beadsandbeading.com/blog/fimo-clay-premo-sculpey-cane-making-sculpting/180/'
a=find('Polymer clay','Fimo'); a['s']=bs
a['v']=[ver('Classic','Staedtler','firm clay'),ver('Soft','Staedtler','softer, easier to condition'),ver('Effect','Staedtler','transparent, glitter and glow finishes'),ver('Puppen Fimo','Staedtler','doll-making clay')]
a=find('Polymer clay','Sculpey'); a['s']=bs
a['v']=[ver('Sculpey III','Polyform Products','soft, low-cost clay'),ver('Studio by Sculpey','Polyform Products','matte, strong after baking')]
ax('Polymer clay',arch('Premo Sculpey','Polyform Products','Artist-palette Sculpey line; the older formula was firm, the newer one softer.',bs,dt='artist palette colours',v=[ver('Premo Frost','Polyform Products','translucent colours')]),1)
a=find('Polymer clay','Kato Polyclay'); a['s']=bs
# remove promoted from m
k=kind(d,'Polymer clay'); k['m']=[m for m in k['m'] if m!=['Premo Sculpey','Sculpey']]
k=kind(d,'Soft pastels'); k['m']=[m for m in k['m'] if m[0]!='Terry Ludwig Soft Pastels']
# ---- new shelf: lace & knotting tools
kn=dept(d,"Yarn, fibre & needlework supplies")
tat={"n":"Tatting shuttle","a":"lace shuttle · tatting needle","d":"Small hand tool holding thread to form tatted knots; metal, ivory, plastic or a long needle.","s":W+'Tatting',
 "t":["pointed-oval shuttle","post shuttle","standard","large","tatting needle","cro-tatting hook","metal","plastic"],
 "x":[arch('Clover tatting shuttle','Clover','Plastic post shuttle in standard and large sizes with a pointed tip for joining picots.','https://blog.clover-usa.com/2016/11/17/tatting-shuttles-picot-gauge-set/',dt='post shuttle · standard or large · pointed tip')]}
bob={"n":"Lace bobbin","a":"bobbin lace bobbin","d":"Wooden or bone thread holder with neck, head and shank, hung in pairs on a lace pillow.","s":W+'Bobbin_lace',
 "t":["Belgian","Binche","Portuguese","square","bone","wood","engraved"],
 "x":[arch('East Midlands bobbin','','Slender double-headed bobbin weighted with a spangle; also called Bucks or Midlands.',W+'Bobbin_lace',dt='double-headed · spangled · wood or bone'),
      arch('Honiton bobbin','','Slender bobbin, straight below the head, with a blunt point for sewing.',W+'Bobbin_lace',dt='straight shank · blunt point')]}
pil={"n":"Lace pillow","a":"bobbin-lace pillow","d":"Firm pillow on which bobbin lace is pinned and worked.","s":W+'Bobbin_lace',
 "t":["bolster","roller","cookie","block","straw-stuffed","polystyrene"]}
kn['s'].append({"n":"Lace & knotting tools","k":[tat,bob,pil]})
# ---- glass
gs=shelf(d,"Glass sheet, rod & tools")
old=[k for k in gs['k'] if k['n']=="Lampwork torch and glass rod"][0]
i=gs['k'].index(old)
torch={"n":"Lampworking torch","a":"flameworking torch · bead torch","d":"Gas torch that melts glass rod for beads and small objects; bench burner or hand torch.","s":W+'Lampworking',
 "t":["bench burner","hand torch","propane and air","propane and oxygen","MAPP gas","surface mix","internal mix"],
 "x":[arch('Hot Head','','Propane-only torch many beginners start with.','https://www.frit-happens.co.uk/wiki/Torch',dt='propane · fuel only'),
      arch('Nortel Minor','','Dual-fuel propane and oxygen torch widely used as a starter.','https://www.frit-happens.co.uk/wiki/Torch',dt='propane and oxygen'),
      arch('Bethlehem burner','','Dual-fuel propane and oxygen burner line.','https://www.frit-happens.co.uk/wiki/Torch',dt='propane and oxygen'),
      arch('Carlisle CC','','Dual-fuel propane and oxygen torch.','https://www.frit-happens.co.uk/wiki/Torch',dt='propane and oxygen')]}
rod={"n":"Lampwork glass rod","a":"glass rod · glass tube","d":"Glass rod or tube melted at a torch; soft soda-lime and lead glass, or hard borosilicate.","s":W+'Lampworking',
 "t":["soda-lime (soft)","lead glass","borosilicate (hard)","rod","tube","coefficient of expansion"],
 "x":[arch('Effetre','Effetre Murano','Medium-soft soda-lime glass of 104 COE, formerly sold as Moretti.',W+'Effetre_glass',dt='104 COE · working temperature about 945 C · wide colour range')]}
blow={"n":"Glassblowing blowpipe and punty","a":"pontil · blowing iron","d":"Hollow blowpipe that gathers and inflates molten glass, and the solid punty that holds the piece for finishing.","s":W+'Glassblowing',"t":["blowpipe","punty","steel","iron"]}
jack={"n":"Glassblowing jacks, blocks and paddles","d":"Hand tools for shaping hot glass: tweezer-like jacks, water-soaked fruitwood blocks and flat wood or graphite paddles.","s":W+'Glassblowing',"t":["jacks","block","paddle","marver"]}
gs['k'][i:i+1]=[torch,rod,blow,jack]
# brands
have={x['n'].lower() for x in bj['b']}
def br(n,c,f,seg,kf,dd,s,sig=None):
    if n.lower() in have: return
    o={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":dd,"s":s}
    if sig:o['sig']=sig
    bj['b'].append(o)
br('Moleskine','Italy','1997','Premium','notebooks','Milan brand that reintroduced the black oil-cloth notebook in 1997.',W+'Moleskine',['Classic notebook'])
br('Terry Ludwig','United States','','Artisan & independent','soft pastels','American maker of handmade soft pastels.',ps,['Terry Ludwig Soft Pastels'])
br('Mount Vision','United States','','Artisan & independent','soft pastels','Handmade soft pastels by Karl Kelly, started in New York.',ps,['Mount Vision'])
br('Effetre Murano','Italy','','Heritage manufactory','Murano glass rod','Murano maker of Effetre soda-lime lampwork glass, formerly Moretti.',W+'Effetre_glass',['Effetre'])
save(d); save(bj,B); print('ok')
