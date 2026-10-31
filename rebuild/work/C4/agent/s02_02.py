import sys; sys.path.insert(0,'work/C4/agent')
from lib import *
W='https://en.wikipedia.org/wiki/'
SH=W+'Shibori'; RD=W+'Resist_dyeing'; CA=W+'Canting'; AD=W+'Adire_(textile_art)'; BA=W+'Bandhani'; DN='https://www.dharmatrading.com/blogs/a/dye-na-flow-faq'
PR='https://woolery.com/dyeing/synthetic-fiber-yarn-dyes/procion-mx-reactive-dyes.html'; DY=W+'Dylon'; RI=W+'Rit_(dye)'; IN=W+'Indigo_dye'; SE='https://www.deserres.ca/collections/pebeo-setacolor-paints?page=2'
kinds=[
{"n":"Fabric dye","a":"textile dye","d":"Dye made for colouring fabric and fibre, from cold-water fibre-reactive to hot-water household dye.","s":"https://www.dickblick.com/categories/painting/fabric/",
 "t":["fibre-reactive (cellulose)","acid dye (protein fibres)","all-purpose / multipurpose","machine dye","hand dye","tie-dye kit"],
 "x":[X("Procion MX","",PR,"Cold-water fibre-reactive dye that permanently dyes cellulose fibres at room temperature; also dyes wool and silk with acid.",dt="cotton, linen, viscose, hemp · intermixable colours"),
      X("Rit","Rit",RI,"American household dye first sold in 1916, in powder and solid forms, applied in hot water.","1916",dt="powder · liquid · colour remover"),
      X("Dylon","Dylon",DY,"British dye brand founded 1946; Machine Fabric Dye in 32 colours, Hand Dye in 21, Multipurpose in 26.","1946",v=[("Machine Fabric Dye","32 colours, reactive"),("Hand Dye","21 colours"),("Multipurpose Dye","26 colours, direct/acid/disperse mix, less wash-fast")],dt="machine · hand · multipurpose")]},
{"n":"Natural dye and indigo","a":"plant dye · indigo vat · aizome","d":"Plant, insect or mineral dyes and indigo, used in vats for resist and shibori work.","s":IN,
 "t":["natural indigo (Indigofera tinctoria)","Japanese indigo (Persicaria tinctoria)","Strobilanthes cusia","synthetic indigo","fermentation vat","reduction vat"],
 "x":[X("Natural indigo vat","",IN,"Indigo is insoluble and must be reduced to its soluble form in a vat; air then turns the dyed cloth blue. Japan used a heated vat of anaerobic bacteria.",dt="Indigofera, Persicaria or Strobilanthes · fermentation or chemical reduction")]},
{"n":"Batik wax and tjanting","a":"canting · batik wax · batik cap","d":"Hot wax and its pen-like copper applicator used to draw dye-resist designs on cloth.","s":CA,
 "t":["canting (tjanting) spout 1-2.5 mm","multi-spout canting","batik wax (malam)","cap stamp","electric canting"],
 "x":[X("Canting","",CA,"Pen-like tool with a copper wax reservoir, spout and bamboo handle that applies hot wax in Javanese batik tulis, possibly from the 12th century.","12th century",v=[("rengrengan","draws the first outline"),("isen","fills existing patterns")],dt="copper, bronze, zinc, iron or Teflon · one to seven spouts")]},
{"n":"Fabric paint","a":"textile paint","d":"Paint made to decorate fabric, heat-set or air-cured.","s":"https://www.dickblick.com/categories/painting/fabric/",
 "t":["fluid dye-like","opaque","light-fabric","shimmer","dimensional (puffy)","heat-set","air-dry"],
 "x":[X("Dye-Na-Flow","Jacquard",DN,"Water-based acrylic fluid textile paint with the consistency of water, for washes, silk painting and airbrushing.",dt="heat-set with a dry iron · dry-cleanable"),
      X("Setacolor","Pebeo",SE,"45 ml textile paints in Opaque, Light Fabric and Shimmer types.",dt="opaque · light fabric · shimmer · pearl")],
 "m":[["Dimensional Fabric Paint","Tulip"]]},
]
brands=[
B("Jacquard","United States","","Mainstream","dyes and textile paint","US maker of Dye-Na-Flow fluid textile paint.",s=DN,sig=["Dye-Na-Flow"]),
B("Pebeo","France","1920","Mainstream","hobby and fine-art colour","French maker of Setacolor textile paints.",s=SE,sig=["Setacolor"]),
B("Rit","United States","1916","Mainstream","household dye","American household dye brand owned by Nakoma Products.",s=RI,sig=["Rit"]),
B("Dylon","United Kingdom","1946","Mainstream","fabric dyes","British dye brand now owned by Henkel.",s=DY,sig=["Dylon"]),
B("Tulip","United States","","Mainstream","dimensional fabric paint","US craft brand of dimensional fabric paint.",sig=["Dimensional Fabric Paint"],s="knowledge"),
]
trad=[
{"n":"Shibori","g":"Textiles & rugs","r":"Japan","p":"8th century onward (Tōdai-ji, 756 CE)","d":"Japanese tie-dye by binding, stitching, folding or clamping cloth before dyeing.","tech":"Kanoko, miura, kumo, nui, arashi and itajime resists before dyeing.","mat":"Silk, cotton; indigo, safflower","forms":["Kanoko","Miura","Kumo","Nui","Arashi","Itajime"],"ctr":["Kyoto","Takasaki (beni itajime)"],"auth":"Some historic techniques, like original tsujigahana, cannot be fully recreated as the fabric is no longer made.","s":SH},
{"n":"Batik","g":"Textiles & rugs","r":"Java, Indonesia","p":"possibly 12th century (canting) onward","d":"Wax-resist dyeing in which hot wax drawn with a canting or stamped keeps dye from parts of the cloth.","tech":"Wax is applied, cloth dyed, wax removed by scraping or boiling, and the process repeated for each colour.","mat":"Cotton or silk; wax (malam); copper canting","forms":["Batik tulis (hand-drawn)"],"ctr":["Java"],"auth":"","s":CA},
{"n":"Adire","g":"Textiles & rugs","r":"South-western Nigeria (Yoruba)","p":"documented to the 1930s and revived from the 1960s","d":"Yoruba indigo cloth made by women with tied, stitched and paste-resist methods.","tech":"Oniko (tying), alabere (stitching) and eleko (cassava paste); cloth dyed repeatedly, up to 25 or more times.","mat":"Cotton; indigo; cassava paste; raffia","forms":["Oniko","Alabere","Eleko"],"ctr":["Abeokuta","Ibadan","Osogbo"],"auth":"Deep blue-black from many dips distinguishes quality cloth.","s":AD},
{"n":"Bandhani","g":"Textiles & rugs","r":"Gujarat and Rajasthan, India","p":"","d":"Indian tie-dye in which tiny points of cloth are tied to leave dotted patterns.","tech":"Cloth is plucked and tied tightly at points, then dyed in stages.","mat":"Cotton, silk","forms":["Dotted bandhani","Sungudi (Tamil Nadu)"],"ctr":["Jamnagar","Bhuj","Anjar","Mandvi","Jetpur","Rajkot"],"auth":"Bhuj is known for red bandhani.","s":BA},
]
write('02_02',kinds,brands,trad,"Aizome and boro: no retrieved page covered them (aizome folded into natural indigo vat; boro left out). Dharma Procion, Jacquard Procion MX: product pages blocked or unretrieved, so Procion MX is a maker-free archetype. Tulip kept as a flat model (no page). Traditions from Wikipedia; Pebeo founding from knowledge.")
