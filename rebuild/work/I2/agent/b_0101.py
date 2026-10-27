import sys; sys.path.insert(0,'work/I2/agent')
from put import put
W='https://en.wikipedia.org/wiki/'
def A(n,mk,y,s,d,v=(),a=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":W+s,"v":[dict(n=i[0],mk=i[1],y=i[2],d=i[3]) for i in v]}
kinds=[
{"n":"Sewing pattern","a":"PDF sewing pattern · paper pattern","d":"A printable PDF or paper pattern for sewing a garment or item.","t":["Printable PDF (A4/Letter)","Copy-shop large format","Projector file","Graded multi-size"],"s":"https://www.sewdirect.com/product/simplicity-s9964/","x":[
 A("Butterick graded patterns","Butterick","1860s","Butterick_Publishing_Company","Ebenezer Butterick's multi-size graded paper patterns, the first sold this way.",[("Vogue Patterns licence","Butterick","1961","Butterick licensed the Vogue name and bought its pattern division")]),
 A("McCall's patterns","McCall's","1870","McCall's","James McCall's printed patterns, run on after the magazine was sold."),
 A("Simplicity","Simplicity Pattern","1927","Simplicity_Pattern","New York pattern house sold as Simplicity, It's So Easy and New Look.")]},
{"n":"Knitting or crochet pattern","a":"PDF knitting pattern","d":"A downloadable pattern for knitting or crocheting.","t":["Chart","Written row-by-row","Garment","Accessory"],"s":"https://www.ravelry.com/stores/stella-charming-design","x":[
 A("Ravelry pattern store","Ravelry","2007","Ravelry","Community-edited database where designers sell PDF patterns, keeping 98.7 per cent of each sale.")]},
{"n":"Cross-stitch or embroidery chart","a":"counted cross-stitch chart · embroidery file","d":"A gridded chart for hand stitching, or a stitch file read by an embroidery machine.","t":["Counted cross-stitch chart","Stamped design","Machine embroidery: DST (Tajima and others)","Machine embroidery: PES (Brother, Baby Lock)","Machine embroidery: JEF (Janome)","Machine embroidery: VP3 (Pfaff, Husqvarna Viking)"],"s":W+"Cross-stitch"},
{"n":"Papercraft and cutting file","a":"SVG cut file · printable papercraft","d":"A vector file for a home cutting machine, or a printable sheet to fold and glue.","t":["Cut file for Cricut or Silhouette","Printable papercraft","Template for vinyl"],"s":W+"Cricut"},
]
brands=[
{"n":"Simplicity Pattern","c":"United States","f":"1927","seg":"Mainstream","kf":"sewing patterns","d":"New York pattern house founded by James J. Shapiro; now owned by Rubelmann Capital.","s":W+"Simplicity_Pattern"},
{"n":"Butterick","c":"United States","f":"","seg":"Mainstream","kf":"graded patterns","d":"Pioneer of graded sewing patterns; owner of the Vogue Patterns licence from 1961.","s":W+"Butterick_Publishing_Company"},
{"n":"McCall's","c":"United States","f":"1870","seg":"Mainstream","kf":"sewing patterns","d":"James McCall's pattern line, begun in 1870.","s":W+"McCall's"},
{"n":"Ravelry","c":"United States","f":"2007","seg":"Own-label & retailer","kf":"knit and crochet patterns","d":"Fibre-arts community site and PDF pattern store founded by Cassidy and Jessica Forbes.","s":W+"Ravelry"},
{"n":"Cricut","c":"United States","f":"","seg":"Mainstream","kf":"cutting machines","d":"Home cutting-machine maker whose Design Space software reads uploaded vector or bitmap files.","s":W+"Cricut"},
]
put('I2','01_01',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Archetypes are pattern houses and the Ravelry pattern store, since no individual named patterns were sourced and titles-style lists are avoided. Butterick founding year not stated on the fetched page, left blank. Cricut founding year left blank. SVG support for Cricut not confirmed by the page, so SVG is mentioned only as a cut-file kind. Burda not sourced and left out."})
