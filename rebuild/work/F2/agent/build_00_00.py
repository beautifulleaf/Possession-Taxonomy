import json, os
W='https://en.wikipedia.org/wiki/'
CF=W+'Color_field'
kinds=[
 {"n":"Oil painting","a":"oil on canvas · oil on panel","d":"Pigment bound in a drying oil, on canvas, panel or a similar support.",
  "t":["on canvas","on wood panel","on copper","on board","portrait","landscape","still life","history and religious subject","abstract"],
  "s":"https://www.singulart.com/en/painting",
  "x":[
   {"n":"Old Master painting","a":"Old Master","d":"A painting by a skilled European painter working before about 1800, including pupil and workshop pictures.","mk":"","y":"c. 1450–1800","s":W+"Old_Master","v":[],
    "dt":"attribution level (named hand, workshop, anonymous 'notname' master) · support (panel, canvas, copper) · school and date"},
   {"n":"Plein-air oil sketch","a":"en plein air painting · open-air oil study","d":"An oil painted outdoors in front of the motif to catch changing light and weather, often small and on panel or board.","mk":"","y":"1800 onward","s":W+"En_plein_air",
    "v":[{"n":"Theory of painting in situ","mk":"Pierre-Henri de Valenciennes","y":"1800","d":"set out in his treatise on landscape painting"},
         {"n":"Barbizon School","mk":"Charles-François Daubigny","y":"1830s","d":"with Théodore Rousseau"},
         {"n":"Macchiaioli","mk":"","y":"late 1850s","d":"Italian open-air group"},
         {"n":"Impressionist open-air painting","mk":"Claude Monet","y":"1860s","d":"with Renoir, Sisley and Bazille"}],
    "dt":"size (pochade box panels up to about 50 cm) · panel, board or canvas · tube paint after 1841"},
   {"n":"Colour-field canvas","a":"colour field painting","d":"A large abstract canvas built from broad, flat areas of colour rather than gesture.","mk":"","y":"1940s–1950s","s":CF,
    "v":[{"n":"Blurred-edge colour fields","mk":"Mark Rothko","y":"c. 1950","d":"stacked soft-edged fields"},
         {"n":"Zip paintings","mk":"Barnett Newman","y":"c. 1950","d":"flat fields divided by thin vertical zips"},
         {"n":"Torn-edge fields","mk":"Clyfford Still","y":"c. 1950","d":"jagged, heavily textured fields"}],
    "dt":"scale · oil or acrylic · stained or opaque surface"}]},
 {"n":"Acrylic painting","a":"acrylic on canvas","d":"Pigment bound in acrylic polymer emulsion, fast-drying and water-thinnable.",
  "t":["on canvas","on board","on paper","portrait","landscape","abstract","pop"],
  "s":"https://www.singulart.com/en/painting",
  "x":[
   {"n":"Stain painting","a":"soak-stain painting","d":"Thinned paint poured, brushed or rolled into unprimed cotton duck so that it soaks into the weave.","mk":"Helen Frankenthaler","y":"1952","s":CF,
    "v":[{"n":"Stain on raw canvas","mk":"Helen Frankenthaler","y":"1952","d":"pioneer of the method"},
         {"n":"Poured stripes and veils","mk":"Morris Louis","y":"1950s","d":"painted in Magna acrylic"},
         {"n":"Targets, Chevrons and Stripes","mk":"Kenneth Noland","y":"","d":"series"}],
    "dt":"Magna (solvent) or water-based acrylic · raw cotton duck · scale"},
   {"n":"Flat-colour acrylic canvas","a":"","d":"Large areas of flat, fast-drying acrylic colour with details added on top, typical of 1960s Californian and Pop painting.","mk":"David Hockney","y":"1960s","s":"https://tate.org.uk/art/artworks/hockney-a-bigger-splash-t03254/understanding-david-hockneys-bigger-splash",
    "v":[{"n":"A Bigger Splash","mk":"David Hockney","y":"1967","d":"acrylic on cotton duck, about 2.5 m square"}],
    "dt":"canvas size · stretched or unstretched duck"}]},
 {"n":"Mixed-media painting","a":"","d":"A painting in which several paint media or added materials are used together and the image is painted, not built from pasted elements.",
  "t":["oil and collage","acrylic and collage","with attached objects","on canvas","on panel"],
  "s":"https://www.artsy.net/categories",
  "x":[
   {"n":"Combine painting","a":"Combine","d":"A painting with everyday objects or printed matter attached, hovering between painting and sculpture.","mk":"Robert Rauschenberg","y":"mid-1950s–1961","s":W+"Combine_painting",
    "v":[{"n":"Bed","mk":"Robert Rauschenberg","y":"1955","d":""},
         {"n":"Monogram","mk":"Robert Rauschenberg","y":"1955–1959","d":"free-standing, with stuffed goat"},
         {"n":"Canyon","mk":"Robert Rauschenberg","y":"1959","d":"with taxidermied eagle"},
         {"n":"Fool's House","mk":"Jasper Johns","y":"1964","d":"broom attached to canvas"}],
    "dt":"wall-hung or free-standing · attached objects · oil, printed matter, fabric"}]},
 {"n":"Spray-paint and street-art painting","a":"spray-paint painting · aerosol painting · graffiti on canvas","d":"A work painted mainly with aerosol or stencilled spray paint on canvas, panel or another movable support, by a street or graffiti artist.",
  "t":["stencil","freehand aerosol","on canvas","on wood","on metal","removed wall section"],
  "s":"https://www.singulart.com/en/painting",
  "x":[
   {"n":"Stencil canvas","a":"","d":"A satirical stencilled image in spray paint, carried from street walls onto canvas and sold through the artist's own channel.","mk":"Banksy","y":"c. 2000 onward","s":W+"Banksy",
    "v":[{"n":"Devolved Parliament","mk":"Banksy","y":"2009","d":"largest known canvas, 4 m wide"},
         {"n":"Girl with Balloon / Love Is in the Bin","mk":"Banksy","y":"2018","d":"partly shredded at auction"}],
    "dt":"authentication by Pest Control Office · canvas, board or removed wall"},
   {"n":"Obey Giant stencil and collage","a":"OBEY","d":"Stencilled, screenprinted and collaged propaganda-style portraits on wood, metal and canvas, grown from a sticker campaign.","mk":"Shepard Fairey","y":"1989","s":W+"Shepard_Fairey",
    "v":[{"n":"Andre the Giant Has a Posse","mk":"Shepard Fairey","y":"1989","d":"sticker campaign"},
         {"n":"OBEY Giant","mk":"Shepard Fairey","y":"1996","d":"reworked image"},
         {"n":"Hope","mk":"Shepard Fairey","y":"2008","d":"Barack Obama portrait"}],
    "dt":"stencil, screenprint or collage · wood, metal, canvas"}]},
 {"n":"Encaustic painting","a":"hot wax painting","d":"Pigment in hot beeswax, often with damar resin, fused to a support with heat.",
  "t":["on panel","on canvas","with collage"],
  "s":"https://www.chairish.com/product/27987907/original-encaustic-painting-by-gina-cochran-the-rook",
  "x":[
   {"n":"Fayum mummy portrait","a":"Faiyum portrait · mummy portrait","d":"A naturalistic head-and-shoulders portrait on a thin wooden panel, set into the wrappings of a Roman-Egyptian mummy.","mk":"","y":"late 1st century BC – mid-3rd century AD","s":W+"Fayum_mummy_portraits",
    "v":[{"n":"Encaustic portrait","mk":"","y":"","d":"vivid colour, broad strokes"},
         {"n":"Tempera portrait","mk":"","y":"","d":"animal-glue binder, chalkier colour"}],
    "dt":"panel wood (limewood, oak, cedar, fig…) or linen shroud · provenance and export papers"},
   {"n":"Encaustic and collage painting","a":"","d":"Hot wax used both as paint and as adhesive for strips of cloth and newsprint on a canvas or panel.","mk":"Jasper Johns","y":"1954–1955","s":W+"Flag_(painting)",
    "v":[{"n":"Flag","mk":"Jasper Johns","y":"1954–1955","d":"encaustic, oil and collage on fabric mounted on plywood"}],
    "dt":"support · wax with oil · collage layers"}]}]
def B(n,c,kf,d,s,sig=None): 
  b={"n":n,"c":c,"f":"","seg":"Artisan & independent","kf":kf,"d":d,"s":s}
  if sig: b["sig"]=sig
  return b
brands=[
 B("Banksy","United Kingdom","street art","Pseudonymous England-based street artist known for satirical stencils; new works sold only through Pest Control.",W+"Banksy",["Stencil canvas"]),
 B("Shepard Fairey","United States","street art","American street artist (born 1970) behind OBEY Giant and the 2008 Hope poster.",W+"Shepard_Fairey",["Obey Giant stencil and collage"]),
 B("Jasper Johns","United States","flags, encaustic","American painter who revived encaustic with his flag, target and number paintings.",W+"Flag_(painting)",["Encaustic and collage painting"]),
 B("Robert Rauschenberg","United States","combines","American artist who coined the Combine, mixing painting and attached objects.",W+"Combine_painting",["Combine painting"]),
 B("David Hockney","United Kingdom","acrylic, pools","British painter, an early heavy user of acrylic, known for Californian swimming-pool pictures.","https://tate.org.uk/art/artworks/hockney-a-bigger-splash-t03254/understanding-david-hockneys-bigger-splash",["Flat-colour acrylic canvas"]),
 B("Mark Rothko","United States","colour field","American painter (1903–1970) of large soft-edged colour fields.",CF,["Colour-field canvas"]),
 B("Barnett Newman","United States","colour field","American painter (1905–1970) of flat colour fields divided by zips.",CF,["Colour-field canvas"]),
 B("Clyfford Still","United States","colour field","American painter (1904–1980) of jagged, textured colour fields.",CF,["Colour-field canvas"]),
 B("Helen Frankenthaler","United States","stain painting","American painter (1928–2011) who pioneered stain painting on raw canvas in 1952.",CF,["Stain painting"]),
 B("Morris Louis","United States","stain painting","American painter (1912–1962) of poured, stained fields in Magna acrylic.",CF,["Stain painting"]),
 B("Kenneth Noland","United States","colour field","American painter (1924–2010) of Targets, Chevrons and Stripes series.",CF,["Stain painting"]),
 B("Claude Monet","France","Impressionism","French Impressionist and leading advocate of painting outdoors.",W+"En_plein_air",["Plein-air oil sketch"]),
 B("Charles-François Daubigny","France","Barbizon School","French Barbizon School landscape painter who worked outdoors.",W+"En_plein_air",["Plein-air oil sketch"]),
 B("Pierre-Henri de Valenciennes","France","landscape theory","French painter and theorist (1750–1819) who set out painting landscape in situ.",W+"En_plein_air",["Plein-air oil sketch"]),
]
for b in brands:
  if b["c"]=="" : pass
out={"kinds":kinds,"brands":brands,"traditions":[],
 "notes":"All five planned kinds kept (Spray-paint painting renamed Spray-paint and street-art painting). Supports and genres moved to t. Archetypes sourced from fetched Wikipedia/Tate pages. No Getty ULAN pages retrieved, so artist entries cite the fetched Wikipedia/Tate pages instead; founding year left blank for artists. Old Master archetype has no versions because the fetched page gives no reference artists by name. artnet and MoMA pages blocked (403). No traditions on this shelf (artisan schools are elsewhere). Fairey's Hope is a poster but kept as the reference version of his portrait style."}
p='work/F2/shelves/00_00.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
