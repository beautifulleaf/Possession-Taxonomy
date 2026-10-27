import json, os
W='https://en.wikipedia.org/wiki/'
VA='https://collections.vam.ac.uk/item/O78270/ruins-of-rievaulx-abbey-yorkshire-watercolour-cotman-john-sell'
GO=W+'Gouache'; RE=W+'Pierre-Joseph_Redout%C3%A9'; A21='https://www.art-21.org/magazine/egg.aspx'; DW=W+'Detachment_of_wall_paintings'
kinds=[
 {"n":"Watercolour","a":"watercolor · aquarelle","d":"Transparent pigment in gum arabic, applied wet, normally on paper.",
  "t":["landscape","topographical view","botanical and natural history","portrait","marine","on paper","on vellum"],
  "s":"https://www.singulart.com/en/painting",
  "x":[
   {"n":"English landscape watercolour","a":"English watercolour school","d":"A landscape or topographical view in washes on paper, raised by English painters into a medium fit for exhibition.","mk":"","y":"later 18th – 19th century","s":VA,
    "v":[{"n":"The White House at Chelsea","mk":"Thomas Girtin","y":"1800","d":"broad washes of strong colour; Tate Britain"},
         {"n":"Ruins of Rievaulx Abbey, Yorkshire","mk":"John Sell Cotman","y":"1803","d":"watercolour on paper; V&A"},
         {"n":"Landscape watercolours","mk":"J. M. W. Turner","y":"","d":"Girtin's friend and rival"}],
    "dt":"size · sheet and mount · subject (abbey, river, town view) · drawing-master or amateur copy"},
   {"n":"Botanical watercolour","a":"flower painting · botanical illustration","d":"An exact watercolour of a plant drawn from life, made for botany or as a flower picture.","mk":"Pierre-Joseph Redouté","y":"c. 1800","s":RE,
    "v":[{"n":"Les Liliacées","mk":"Pierre-Joseph Redouté","y":"1802–1816","d":"8 volumes, published as coloured stipple engravings"},
         {"n":"Les Roses","mk":"Pierre-Joseph Redouté","y":"1817–1824","d":"3 volumes"},
         {"n":"Teacher's flower watercolours","mk":"Gerard van Spaendonck","y":"","d":"Redouté's teacher"}],
    "dt":"original watercolour or hand-coloured engraved plate · vellum or paper · species"}]},
 {"n":"Gouache","a":"body colour · opaque watercolour · poster paint","d":"Opaque, chalk-bodied water-based colour, normally on paper.",
  "t":["on paper","on board","with watercolour","airbrushed"],
  "s":"https://www.singulart.com/en/painting",
  "x":[
   {"n":"Gouache poster and cover design","a":"","d":"An original design in flat, quick-drying opaque colour made for a poster, magazine cover or stage set.","mk":"","y":"late 19th century onward","s":GO,
    "v":[{"n":"Femina cover design","mk":"Léon Bénigni","y":"1920s","d":"magazine cover"},
         {"n":"Stage design for a drama","mk":"Roman Nyman","y":"1923","d":""}],
    "dt":"design or finished artwork · board or paper · airbrush"},
   {"n":"Gouache landscape view","a":"","d":"A topographical landscape or view painted in opaque body colour, alone or with watercolour.","mk":"","y":"18th–19th century","s":GO,
    "v":[{"n":"Lago d'Averno","mk":"Jacob Philipp Hackert","y":"1794","d":""},
         {"n":"Exeter and the Canal Basin","mk":"John Gendall","y":"1835–1840","d":"watercolour and gouache"},
         {"n":"Sunset at Sea","mk":"Claude Monet","y":"1865–70","d":""}],
    "dt":"size · paper · pure gouache or mixed with watercolour"},
   {"n":"Gouache cut-out","a":"gouaches découpées","d":"Paper painted with gouache, then cut and arranged as a composition.","mk":"Henri Matisse","y":"","s":GO,
    "v":[{"n":"Blue Nudes","mk":"Henri Matisse","y":"","d":"series"}],"dt":"see also Collage"}]},
 {"n":"Tempera painting","a":"egg tempera","d":"Pigment bound in egg yolk or another egg or glue medium, usually on a prepared panel.",
  "t":["on gessoed panel","on Masonite","gold ground","religious subject","portrait"],
  "s":"https://www.singulart.com/en/painting",
  "x":[
   {"n":"Renaissance tempera panel","a":"","d":"An egg tempera picture on a gessoed wooden panel, the main easel medium from 13th-century portable altarpieces to the 15th century.","mk":"","y":"13th–15th century","s":A21,
    "v":[{"n":"Florentine tempera panels","mk":"Fra Angelico","y":"15th century","d":""},
         {"n":"Florentine tempera panels","mk":"Sandro Botticelli","y":"15th century","d":""}],
    "dt":"panel and gesso ground · altarpiece fragment or portrait · attribution"},
   {"n":"Modern egg tempera panel","a":"","d":"A 20th-century realist painting in egg tempera, built in fine layers on a gessoed panel.","mk":"Andrew Wyeth","y":"mid-20th century","s":A21,
    "v":[{"n":"Christina's World","mk":"Andrew Wyeth","y":"","d":""},
         {"n":"Government Bureau","mk":"George Tooker","y":"mid-20th century","d":""},
         {"n":"Egg tempera panels","mk":"Robert Vickrey","y":"","d":"wrote New Techniques in Egg Tempera (1973)"}],
    "dt":"panel size · Masonite or hardwood · traditional gesso"}]},
 {"n":"Fresco","a":"detached fresco · transferred fresco","d":"Pigment applied to wet or dry lime plaster, now removed from its wall.",
  "t":["buon fresco","fresco secco","fragment","on new support"],
  "s":"https://www.1stdibs.com/furniture/wall-decorations/paintings/spanish-16th-century-fresco-fragment/id-f_20435602",
  "x":[
   {"n":"Detached fresco fragment","a":"transferred wall painting","d":"A section of wall painting lifted from its wall and mounted on a new support so it can hang like a picture.","mk":"","y":"18th century onward (strappo)","s":DW,
    "v":[{"n":"Strappo","mk":"","y":"","d":"only the top paint layer lifted on cloth and glue; least invasive"},
         {"n":"Stacco","mk":"","y":"","d":"paint taken with its plaster"},
         {"n":"Stacco a massello","mk":"","y":"","d":"paint, plaster and part of the wall removed"}],
    "dt":"transfer method · new support (canvas, panel, honeycomb) · size · provenance and export licence"}]}]
def B(n,c,kf,d,s,sig): return {"n":n,"c":c,"f":"","seg":"Artisan & independent","kf":kf,"d":d,"s":s,"sig":sig}
brands=[
 B("Thomas Girtin","United Kingdom","watercolour","English watercolourist (1775–1802), friend and rival of Turner, who helped make watercolour a respected art.",W+"Thomas_Girtin",["English landscape watercolour"]),
 B("John Sell Cotman","United Kingdom","watercolour","English landscape watercolourist (1782–1842) and Norwich drawing master.",VA,["English landscape watercolour"]),
 B("J. M. W. Turner","United Kingdom","watercolour, landscape","English Romantic landscape painter in oil and watercolour.","knowledge",["English landscape watercolour"]),
 B("Pierre-Joseph Redouté","Belgium","botanical","Painter and botanist (1759–1840) of roses and lilies, known as a master of botanical watercolour.",RE,["Botanical watercolour"]),
 B("Gerard van Spaendonck","Netherlands","flower painting","Botanical artist who taught Redouté.",RE,["Botanical watercolour"]),
 B("Henri Matisse","France","colour, cut-outs","French painter whose late works were gouache cut-outs.",GO,["Gouache cut-out"]),
 B("Jacob Philipp Hackert","Germany","landscape views","German landscape painter of Italian views in gouache.",GO,["Gouache landscape view"]),
 B("Andrew Wyeth","United States","egg tempera","American realist painter known for egg tempera panels such as Christina's World.",A21,["Modern egg tempera panel"]),
 B("George Tooker","United States","egg tempera","American painter of mid-century egg tempera pictures.",A21,["Modern egg tempera panel"]),
]
out={"kinds":kinds,"brands":brands,"traditions":[],
 "notes":"All four planned kinds kept; supports, subjects and techniques moved to t. No Getty ULAN pages retrieved, so artist entries cite fetched Wikipedia/V&A/art-21 pages (Turner from knowledge); founding year blank for artists. Icon-style tempera is left to F4 devotional panels; here the tempera archetype is the Renaissance panel. Animation cels (gouache on cel) belong on the Drawings shelf. Wyeth painting dates not given on the fetched page, so left blank. Brandywine PDF could not be read."}
p='work/F2/shelves/00_01.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
