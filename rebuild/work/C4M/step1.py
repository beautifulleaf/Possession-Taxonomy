from lib import *
d=load()
d['lead']="Materials, tools and machines for making things by hand, grouped as craft and art shops stock them: by material or tool type (paint, paper, fabric, yarn, beads, clay, glass, leather, adhesives), then kind, maker and named line. Crafts as practices sit in the Creative pursuits taxonomy."
dn={"Painting & drawing":("Paints, brushes, paper & drawing media","Art-shop goods grouped by medium: paint, brush and support, drawing material, ink and marker. Paint is organised by medium, then house and line; Colour Index pigment codes are the comparison axis."),
"Printmaking & ink painting":("Printing supplies & East Asian ink goods","Inks, blocks, presses and screens as printmaking suppliers stock them, plus the Four Treasures goods of East Asian brush and ink work."),
"Sewing & fabric":("Fabric, thread & sewing machines","Machines are tier picks with collectable vintage versions; fabric is a variety area organised by fibre and design house; notions are sold loose."),
"Knitting, crochet & needlecraft":("Yarn, fibre & needlework supplies","Yarn shop goods: yarn, needles, hooks, threads, cloth, spinning equipment and looms. Yarn follows Ravelry's axes: weight, fibre and named yarn line."),
"Papercraft & bookbinding":("Paper, card & binding materials","Decorative paper, card, stamps, dies and binding materials as paper-craft shops stock them."),
"Jewellery making & beads":("Beads, findings & jewellery tools","Bead-shop goods: beads and stones, findings and wire, and the hand tools and metal supplies used to assemble jewellery."),
"Pottery & sculpting":("Clay, glazes & kilns","Clay bodies, modelling clays, glazes and studio equipment grouped by material and machine."),
"Glass, resin & candle making":("Glass, resin & wax materials","Glass sheet, rod and tools, mosaic tile, casting resins and moulds, wax and soap bases, grouped by material."),
"Leather, wood & natural crafts":("Leather, cane, floral & wood supplies","Leather is organised by tannage, then tannery and named leather; cane, floristry and wood blanks are sold by material."),
"Scale modelling & miniature painting":("Model paints & hobby tools","Paints, adhesives, finishes and tools sold in hobby shops for plastic kits and miniatures; the kits themselves live in Toys & Games."),
}
for dp in d['depts']:
    if dp['n'] in dn: dp['n'],dp['note']=dn[dp['n']]
sn={"Paint-by-numbers & diamond painting":"Picture kits",
"Printmaking":"Printing inks, blocks & presses",
"Ink painting & calligraphy (Four Treasures)":"East Asian ink goods (Four Treasures)",
"Dyeing & surface design":"Dyes & fabric paints",
"Knitting & crochet tools":"Needles, hooks & yarn tools",
"Embroidery, cross-stitch & sashiko":"Needlework threads, cloth & hoops",
"Spinning & felting":"Spinning equipment & fibre",
"Weaving & knitting machines":"Looms & knitting machines",
"Stamping, embossing & die-cutting":"Stamps, inks & die-cutters",
"Metalsmithing & beading tools":"Jewellery tools & metal supplies",
"Stained glass, fusing & lampwork":"Glass sheet, rod & tools",
"Candle & soap making":"Candle & soap materials",
"Resin, moulding & casting":"Resin, moulds & casting materials",
"Mosaic":"Mosaic materials",
"Leathercraft tools & finishes":"Leather tools & finishes",
"Basketry & chair seating":"Cane, willow & seating materials",
"Flower arranging & pressing":"Floristry supplies",
"Wood & pyrography":"Wood blanks & burning pens",
"Sewing tools & patterns":"Sewing tools & patterns",
}
for dp in d['depts']:
    for s in dp['s']:
        if s['n'] in sn: s['n']=sn[s['n']]
# kind renames
def rn(old,new,alias=None):
    k=kind(d,old); k['n']=new
    if alias: k['a']=(k.get('a','')+' · '+alias).strip(' ·')
rn("Pochade and plein-air box","Pochade box","plein-air box")
rn("Pottery and sculpting hand tools","Clay hand tools","pottery tools · sculpting tools")
rn("Needlecraft and yarn kit","Needlework and yarn kit")
# merge shell assortment into pearl bead
sh=shelf(d,"Beads & stones"); sh['k']=[k for k in sh['k'] if k['n']!="Craft shell assortment"]
pb=kind(d,"Pearl bead"); pb['n']="Pearl and shell bead"; pb['a']=(pb.get('a','')+' · craft shell').strip(' ·'); pb['d']="Pearl or shell piece drilled ready for stringing."; pb['t']=pb.get('t',[])+['shell assortment']
# kiln spare parts into kiln
sh=shelf(d,"Wheels, kilns & studio equipment")
kk=kind(d,"Pottery kiln"); kk['t']=kk.get('t',[])+['replacement element, thermocouple and controller']
sh['k']=[k for k in sh['k'] if k['n']!="Kiln spare parts"]
# lampwork: remove technique archetype, kind rebuilt in later step
save(d)
print('ok')
