import json,os
W='https://en.wikipedia.org/wiki/'
def V(n,mk="",y="",d=""): return {"n":n,"mk":mk,"y":y,"d":d}
def B(n,c,f,seg,kf,d,s,sig=None):
    b={"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
    if sig: b["sig"]=sig
    return b
def T(n,g,r,p,d,tech,mat,forms,ctr,auth,s): return {"n":n,"g":g,"r":r,"p":p,"d":d,"tech":tech,"mat":mat,"forms":forms,"ctr":ctr,"auth":auth,"s":s}
TP=W+"Tapestry"; AU=W+"Aubusson_tapestry"; SA=W+"Sampler_(needlework)"; MO=W+"Mola_(art_form)"
kinds=[
 {"n":"Tapestry","a":"woven tapestry · wall hanging","d":"A picture woven on a loom to hang on a wall.",
  "t":["wool","silk","verdure","figurative","modern artist tapestry","antique","reproduction"],
  "s":"https://www.1stdibs.com/creators/antique-textiles-galleries/furniture/wall-decorations/tapestry/",
  "x":[
   {"n":"Aubusson tapestry","a":"Aubusson-style tapestry","d":"Tapestry woven at Aubusson in central France since about 1300, with figures against verdure; UNESCO-listed in 2009.","mk":"","y":"c. 1300 onward","s":AU,
    "v":[V("Royal charter","","1665"),V("Designs by Boucher, Oudry and Huet","","18th century"),V("Postwar revival led by Jean Lurçat","Jean Lurçat","from 1939"),V("UNESCO listing","","2009")],
    "dt":"verdure or figure · wool · period vs 19th-century reproduction · size"},
   {"n":"Gobelins tapestry","a":"Gobelins Manufactory","d":"Tapestry from the Paris Gobelins works, bought by Colbert for Louis XIV in 1662.","mk":"Gobelins","y":"1662 onward","s":W+"Gobelin",
    "v":[V("Tapestry workshop added to the Gobelin dye-works","Gobelins","16th century"),V("Royal manufactory under Colbert","Gobelins","1662")],
    "dt":"series · weave · museum parallel"},
   {"n":"Flemish verdure tapestry","a":"Flemish tapestry","d":"Large workshop tapestry of landscape and animals, from northern France and the Low Countries, popular until the 18th century.","mk":"","y":"to 18th century","s":TP,
    "v":[V("Verdure tapestry","","","landscape and animals")],
    "dt":"border · borders cut down · fibre · restoration"},
   {"n":"Morris & Co. Merton Abbey tapestry","a":"Holy Grail tapestries","d":"Medieval-style hand-woven tapestries from Morris & Co.'s Merton Abbey works, which operated 1881–1940.","mk":"Morris & Co.","y":"1881–1940","s":W+"Merton_Abbey_Works",
    "v":[V("Holy Grail tapestries","Morris & Co.","1890s","figurative sets")],
    "dt":"designer · edition of weaving · workshop weave"},
   {"n":"Artist tapestry","a":"modern tapestry · Lurçat · Dovecot","d":"Tapestry woven from a modern artist's cartoon, led by Jean Lurçat's 1950s revival and Dovecot Studios.","mk":"Dovecot Studios","y":"1912 onward","s":W+"Dovecot_Studios",
    "v":[V("Dovecot founded by the 4th Marquess of Bute","Dovecot Studios","1912","weavers from Merton Abbey"),V("Moisson","Jean Lurçat","1938"),V("First Lausanne Biennale","","1962")],
    "dt":"artist · edition number · weaver · cartoon"}]},
 {"n":"Embroidered picture","a":"needlework picture · silk-work picture","d":"A picture worked in thread with a needle on a fabric ground.",
  "t":["needlepoint","silk-work","crewelwork","framed","antique","contemporary"],
  "s":"https://www.1stdibs.com/buy/completed-needlepoint",
  "x":[
   {"n":"Stumpwork picture","a":"raised work","d":"English raised embroidery of 1650–1700 with stitched figures standing off the ground, often on caskets.","mk":"","y":"c. 1650–1700","s":W+"Stumpwork",
    "v":[V("Stumpwork casket","","","panels mounted by a carpenter")],
    "dt":"padding · wire · beads and pearls · condition"},
   {"n":"Berlin wool work picture","a":"Berlin woolwork","d":"Charted needlepoint pattern worked in wool on canvas, popular 1804–1875.","mk":"","y":"1804–1875","s":W+"Berlin_wool_work",
    "v":[V("Patterns first published in Berlin","","early 19th century"),V("American magazine patterns","","1840s"),V("British boom after the Great Exhibition","","1851")],
    "dt":"tent stitch · wool · pattern source"},
   {"n":"Suzhou embroidery","a":"Su xiu","d":"Silk embroidery from Jiangsu, one of China's four great embroideries, with double-sided pieces from the late Qing.","mk":"","y":"over 2,000 years","s":W+"Suzhou_embroidery",
    "v":[V("Qing heyday with over 100 workshops in Suzhou","","Qing"),V("Double-sided embroidery","","late Qing"),V("Master Ling Shu"),V("Master Zhao Huijun")],
    "dt":"split silk thread · single or double-sided · maker"}]},
 {"n":"Needlework sampler","a":"sampler","d":"A piece of stitching made to show skill and record patterns, later a dated school exercise.",
  "t":["alphabet sampler","band sampler","spot sampler","schoolgirl sampler","mourning sampler","dated and signed"],
  "s":SA,
  "x":[
   {"n":"Band sampler","a":"","d":"Narrow sampler of the mid-17th century, densely worked and often dated and signed.","mk":"","y":"mid-17th century","s":SA,
    "v":[V("Jane Bostocke sampler","","1598","earliest dated English example")],
    "dt":"width 6–9 in · linen · motifs"},
   {"n":"Schoolgirl sampler","a":"alphabet and verse sampler","d":"Sampler stitched at school from the late 17th century, with alphabets, verses and pictures.","mk":"","y":"late 17th–19th century","s":SA,
    "v":[V("Mourning sampler","","18th–19th century"),V("Early Dutch sampler","","1608"),V("Barbados sampler","","1771")],
    "dt":"cross stitch · date · name · school style"}]},
 {"n":"Art quilt","a":"quilt as art · story quilt","d":"A quilt made to be hung and looked at as art rather than used as a bed cover.",
  "t":["pieced","appliquéd","story quilt","strip quilt","wall quilt"],
  "s":W+"Quilt",
  "x":[
   {"n":"Gee's Bend quilt","a":"Freedom Quilting Bee","d":"Quilts of the Gee's Bend, Alabama, community, which drew critical attention in the late 1990s.","mk":"","y":"18th century onward","s":W+"Mary_Lee_Bendolph",
    "v":[V("The Quilts of Gee's Bend (Whitney Museum)","","2002"),V("Strings","Mary Lee Bendolph","2003–04"),V("Past and Gone","Mary Lee Bendolph","2005"),V("Housetop variation on a US stamp","Mary Lee Bendolph","2006")],
    "dt":"pattern (Housetop, strings) · quilter · date"},
   {"n":"American art quilt","a":"studio art quilt","d":"Quilts treated as art after the Whitney's 1971 'Abstract Design in American Quilts'; art quilting boomed in the 1980s.","mk":"","y":"1971 onward","s":W+"Quilt",
    "v":[V("Abstract Design in American Quilts","","1971","Whitney Museum exhibition"),V("Story quilts","Faith Ringgold")],
    "dt":"artist · technique · hung display"}]},
 {"n":"Appliqué textile picture","a":"textile appliqué panel","d":"A picture made by sewing or cutting layers of fabric, as in molas, arpilleras and story cloths.",
  "t":["reverse appliqué","appliqué","embroidered","hand-sewn","tourist piece"],
  "s":W+"Appliqu%C3%A9",
  "x":[
   {"n":"Kuna mola","a":"Guna mola","d":"Reverse-appliqué panel of the Guna of Panama, made of two to seven layers of coloured cloth cut away.","mk":"","y":"","s":MO,
    "v":[V("Mola blouse panel"),V("Production for outsiders grew after the Second World War","","1940s")],
    "dt":"layers · motif (geometric, sea life, modern) · worn or unworn"},
   {"n":"Chilean arpillera","a":"arpilleras","d":"Cloth scene stitched in Chilean workshops under the Pinochet dictatorship and sent abroad via the Vicariate of Solidarity.","mk":"","y":"1974–1989","s":W+"Arpilleras",
    "v":[V("First Vicariate workshops","","1974"),V("About 200 workshops at the peak","","")],
    "dt":"sack cloth ground · found scraps · protest subject"},
   {"n":"Hmong story cloth","a":"paj ntaub","d":"Embroidered figurative scenes made by Hmong women in refugee camps in Thailand and Laos from the 1970s.","mk":"","y":"1970s onward","s":W+"Hmong_textile_art",
    "v":[V("Early refugee-life story cloths","","1970s")],
    "dt":"stitches (cross, chain, satin) · scene · tribal style"},
   {"n":"Abomey appliqué cloth","a":"Benin appliqué","d":"Appliquéd cloth of Abomey in Benin, a tradition since the 18th century linked to the kingdom of Danhomè.","mk":"","y":"18th century onward","s":W+"Appliqu%C3%A9",
    "v":[V("Danhomè court appliqué","","18th century")],
    "dt":"cut-out figures · symbols · age"}]}
]
brands=[
 B("Gobelins","France","","Heritage manufactory","tapestry","Paris tapestry manufactory, a royal works under Colbert from 1662.",W+"Gobelin",["Gobelins tapestry"]),
 B("Morris & Co.","United Kingdom","","Heritage manufactory","Arts and Crafts textiles","William Morris's firm; its Merton Abbey Works ran 1881–1940.",W+"Merton_Abbey_Works",["Morris & Co. Merton Abbey tapestry"]),
 B("Dovecot Studios","United Kingdom","1912","Artisan & independent","artist tapestry","Edinburgh tapestry studio founded in 1912 by the 4th Marquess of Bute.",W+"Dovecot_Studios",["Artist tapestry"])]
trad=[
 T("Aubusson tapestry","Textiles & rugs","Aubusson, France","c. 1300 onward","Tapestry of the upper Creuse valley, chartered in 1665 and UNESCO-listed in 2009.","low-warp weaving","wool, silk",["Aubusson tapestry"],["Aubusson"],"Weaving centre mark vs imitation; 19th-century reproductions",AU),
 T("Suzhou embroidery","Textiles & rugs","Suzhou, Jiangsu, China","over 2,000 years","One of the four great Chinese embroideries; double-sided work from the late Qing.","split-silk needlework","silk",["Suzhou embroidery"],["Suzhou"],"Hand vs machine; maker's name",W+"Suzhou_embroidery"),
 T("English stumpwork","Textiles & rugs","England","c. 1650–1700","Raised embroidery with padded figures, often on caskets.","padded and wire-supported stitches","silk, metal thread, beads",["Stumpwork picture"],[],"Period materials; later copies",W+"Stumpwork"),
 T("Berlin wool work","Textiles & rugs","Germany, Britain, United States","1804–1875","Charted wool needlepoint worked from printed patterns.","tent stitch on canvas","wool, canvas",["Berlin wool work picture"],["Berlin"],"Pattern source; dyes",W+"Berlin_wool_work"),
 T("Gee's Bend quilting","Textiles & rugs","Gee's Bend, Alabama","18th century onward","Quilting of a Black community, recognised nationally after the 2002 Whitney show.","piecing","cloth",["Gee's Bend quilt"],["Freedom Quilting Bee"],"Quilter attribution",W+"Mary_Lee_Bendolph"),
 T("Guna molas","Textiles & rugs","Panama","18th–20th century","Reverse-appliqué panels of the Guna people.","reverse appliqué","cotton cloth",["Kuna mola"],["Guna Yala"],"Worn vs made for sale",MO),
 T("Chilean arpilleras","Textiles & rugs","Chile","1974–1989","Cloth scenes made in church-backed workshops under dictatorship.","patchwork and stitching","sacking, scraps",["Chilean arpillera"],["Vicariate of Solidarity workshops"],"Workshop and date",W+"Arpilleras"),
 T("Hmong paj ntaub","Textiles & rugs","Laos, Thailand, Hmong diaspora","story cloth from 1970s","Hmong needlework, with story cloths of refugee life.","cross, chain and satin stitch, appliqué","cotton, thread",["Hmong story cloth"],["refugee camps in Thailand and Laos"],"Tribal pattern; date",W+"Hmong_textile_art")]
notes="Kept old Tapestry (Aubusson-style tapestry becomes the Aubusson archetype) and Embroidered picture kinds. Left out for lack of retrieved support: Fon attribution of Benin appliqué (page says Abomey/Danhomè only), Studio Art Quilt Associates, Chinese silk-work pictures beyond Suzhou, Flemish verdure named weavers. The Dovecot-Lurçat link is two separate facts. Bed quilts stay in B2."
json.dump({"kinds":kinds,"brands":brands,"traditions":trad,"notes":notes},open('work/F2/shelves/07_00.tmp','w'),ensure_ascii=False,indent=1)
os.rename('work/F2/shelves/07_00.tmp','work/F2/shelves/07_00.json')
