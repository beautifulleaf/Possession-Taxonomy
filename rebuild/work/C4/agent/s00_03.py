import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
W='https://en.wikipedia.org/wiki/'
PT='https://www.penciltalk.org/?p=106'; VI='https://thevirtualinstructor.com/blog/the-best-colored-pencils'
SEN='https://www.sennelier-colors.com/en/Oil-pastels_4.html'; FA='https://finearttutorials.com/?p=9863'
kinds=[
{"n":"Graphite pencil","a":"lead pencil · drawing pencil","d":"Wood-cased graphite pencil sold in a ladder of hardness grades for sketching and drawing.","s":W+"Pencil",
 "t":["hardness grades (H to B)","jumbo/woodless graphite","mechanical drawing pencil"],
 "x":[
  X("Mars Lumograph","Staedtler",PT,"German artists' graphite pencil, an icon of the type; 24 grades from 10H to 12B.","Mars brand registered 1900",dt="grade 10H to 12B · blue lacquer · jumbo version"),
  X("Mono 100","Tombow",PT,"Japanese drawing pencil judged smoother and richer than the Lumograph in a long-running review.",dt="grade ladder · erases cleanly"),
  X("9000","Faber-Castell",PT,"German artists' graphite pencil often cited as the budget alternative to Tombow.",dt="grade ladder"),
  X("Graphic","Derwent",W+"Pencil","English graphic pencil range with 20 grades from 9H to 9B.",dt="grade 9H to 9B")]},
{"n":"Coloured pencil","a":"colored pencil · pencil crayon","d":"Pencil with a coloured wax- or oil-bound core made for drawing; watercolour pencils form a separate soluble type.","s":"https://www.dickblick.com/categories/drawing/colored-pencils/",
 "t":["wax-based","oil-based","watercolour (water-soluble) pencil","pastel pencil","student grade","artist grade"],
 "x":[
  X("Polychromos","Faber-Castell",VI,"Oil-based artists' pencil with a harder core that holds a point; 120 colours.",dt="oil-based · 120 colours · hard core"),
  X("Luminance","Caran d'Ache",VI,"Wax-based artists' pencil, the brightest of the three leading ranges; 100 colours listed in this review.",dt="wax-based · opaque pigment · works on dark paper"),
  X("Premier","Prismacolor",VI,"Soft wax-based pencil with 150 colours, rich and layerable but brittle.",dt="wax-based · 150 colours · soft core")],
 "m":[["Luminance","Caran d'Ache"],["Chromaqua","Derwent"],["Color Drawing Pencils","Derwent"],["Inktense","Derwent"],["Albrecht Dürer Watercolor Pencils","Faber-Castell"],["Prismacolor Watercolor Pencils","Prismacolor"],["Studio Artists' Colored Pencils","Blick Art Materials"]]},
{"n":"Soft pastels","a":"pastel · hard pastel · pastel pencil · PanPastel","d":"Stick of pigment and little binder for drawing and painting; hard pastels, pastel pencils and pan pastels are types.","s":"https://opusartsupplies.com/collections/soft-pastels",
 "t":["hard pastel","pastel pencil","pan pastel","water-soluble pastel","half stick","handmade"],
 "x":[
  X("Sennelier Soft Pastels","Sennelier",FA,"French extra-soft, buttery pastels in 525 colours; crumbly.",dt="525 colours · extra soft"),
  X("Unison Soft Pastels","Unison Colour",FA,"Handmade in Northumberland, UK; 320 colours, firmer than Schmincke and Sennelier.",dt="320 colours · handmade"),
  X("Schmincke Soft Pastels","Schmincke",FA,"German pastels rated the softest in the review; 400 colours.",dt="400 colours · very soft"),
  X("Rembrandt Soft Pastels","Royal Talens",FA,"Firmest of the group and widely available; the budget standard.",dt="firm · square sticks"),
  X("Girault Soft Pastels","Girault",FA,"French medium-firm pastels, 300 colours, suited to detail.",dt="300 colours · medium firm"),
  X("PanPastel","PanPastel",FA,"Soft pastel pressed into a pan and applied with sponge tools; less dust, erasable.",dt="pan format · sponge applicators")],
 "m":[["Studio Square Soft Pastels","Blick Art Materials"],["Terry Ludwig Soft Pastels","Terry Ludwig"],["Handrolled Soft Pastels","Richeson"]]},
{"n":"Oil pastels","a":"oil pastel","d":"Pigment bound in non-drying oil and wax for drawing and painting without fixative.","s":SEN,
 "t":["student grade","artist grade","iridescent","large format"],
 "x":[
  X("Sennelier Oil Pastels","Sennelier",SEN,"First professional oil pastels, made in 1949 at Picasso's request; 110 classic and 10 iridescent colours.","1949",dt="120 colours · standard, large and giant sizes"),
  X("Cray-Pas","Sakura",W+"Oil_pastel","Original oil pastel, developed by Sakura in 1924 as an improved wax crayon.","1924",dt="paraffin wax, stearic acid, coconut oil binder")],
 "m":[["Neocolor/Neoart 6901 Wax Oil Pastels","Caran d'Ache"]]},
{"n":"Drawing charcoal","a":"vine charcoal · willow charcoal","d":"Stick of burnt wood or compressed charcoal powder used for drawing.","s":"https://www.dickblick.com/categories/pastels/",
 "t":["vine charcoal","willow charcoal","compressed charcoal","charcoal pencil","powdered charcoal"],"m":[]},
{"n":"Crayon","a":"wax crayon","d":"Stick of pigmented wax made for drawing and colouring pictures.","s":"https://www.dickblick.com/categories/pastels/",
 "t":["wax crayon","washable crayon","Conté crayon","chalk crayon"],
 "x":[X("Crayola Crayons","Crayola",W+"Crayon","Paraffin wax crayon sold by Binney & Smith from 1903.","1903",dt="box sizes · colour range")],"m":[]},
{"n":"Eraser and blending tool","a":"kneaded eraser · stump · tortillon","d":"Eraser or paper tool for lifting, softening and blending pencil, charcoal and pastel.","s":W+"Stump_(drawing)",
 "t":["kneaded eraser","vinyl eraser","blending stump","tortillon","chamois"],"m":[]},
{"n":"Fixative","a":"","d":"Spray or liquid sealer made to fix charcoal, pastel and pencil drawings.","s":"https://www.dickblick.com/categories/pastels/",
 "t":["workable fixative","final fixative","casein fixative","spray can","pump bottle"],"m":[]},
]
S="Professional & flagship"
brands=[
B("Staedtler","Germany","1835",S,"pencils","German pencil maker; Mars Lumograph is its artists' graphite line.",lines=["Mars Lumograph"],sig=["Mars Lumograph"],s=PT),
B("Tombow","Japan","1913","Professional & flagship","Mono pencils","Japanese stationery maker of the Mono graphite pencil.",sig=["Mono 100"]),
B("Faber-Castell","Germany","1761","Professional & flagship","pencils","German pencil maker with artist ranges 9000 and Polychromos.",sig=["9000","Polychromos"]),
B("Derwent","United Kingdom","1832","Professional & flagship","pencils","English pencil maker (Cumberland Pencil Company) with graphic and coloured ranges.",lines=["Graphic","Inktense","Chromaqua"],sig=["Graphic"]),
B("Caran d'Ache","Switzerland","1915","Premium","artists' pencils","Swiss maker of Luminance and Neocolor artists' pencils and crayons.",sig=["Luminance"]),
B("Prismacolor","United States","","Mainstream","soft coloured pencils","US brand of soft wax-based coloured pencils.",sig=["Premier"],s="knowledge"),
B("Sennelier","France","1887","Professional & flagship","pastels","Paris colourman who made the first professional oil pastels in 1949.",s=W+"Sennelier",sig=["Sennelier Oil Pastels","Sennelier Soft Pastels"]),
B("Schmincke","Germany","1881","Professional & flagship","pastels, watercolour","German artists' colour maker from Düsseldorf.",sig=["Schmincke Soft Pastels"],s="knowledge"),
B("Unison Colour","United Kingdom","","Artisan & independent","handmade pastels","Handmade soft pastels made in Northumberland.",sig=["Unison Soft Pastels"],s=FA),
B("Royal Talens","Netherlands","1899","Mainstream","Rembrandt pastels","Dutch art-materials maker whose Rembrandt line includes soft pastels.",sig=["Rembrandt Soft Pastels"]),
B("Girault","France","","Artisan & independent","soft pastels","French soft pastel maker.",sig=["Girault Soft Pastels"],s=FA),
B("PanPastel","United States","","Specialist","pan pastels","Maker of pan-format pastels applied with sponges.",sig=["PanPastel"],s=FA),
B("Sakura","Japan","1921","Mainstream","Cray-Pas","Japanese company that developed the oil pastel in 1924.",sig=["Cray-Pas"],s=W+"Oil_pastel"),
B("Crayola","United States","","Mainstream","crayons","US crayon brand of Binney & Smith, named 1903.",sig=["Crayola Crayons"],s=W+"Crayon"),
]
write('00_03',kinds,brands,[],"Old Blick Studio ranges trimmed to one model; Derwent Lightfast, Caran d'Ache Pablo and Neopastel archetypes left out (no retrieved page). Other pastels merged into Soft pastels (PanPastel as archetype/type). Brand facts for several brands from knowledge.")
