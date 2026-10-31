import json, os
W='https://en.wikipedia.org/wiki/'
SG='https://www.sothebys.com/en/articles/the-complete-collectors-guide-to-prints'
AP=W+'Apocalypse_(D%C3%BCrer)'; HB=W+'A_History_of_British_Birds'; NY=W+'New_Year_picture'; YL=W+'Yangliuqing_New_Year_pictures'
ST='https://www.staedelmuseum.de/en/the-mysteries-of-material'
PI='https://www.britishmuseum.org/collection/object/P_1994-1002-11'
NN='https://www.metmuseum.org/art/collection/search/337889'
MU='https://collections.vam.ac.uk/item/O71523/the-kiss-iv-woodcut-munch-edvard/'
kinds=[
 {"n":"Woodcut","a":"woodblock print · xylograph","d":"A print cut with knives and gouges into the side grain of a wood block and printed from the raised surface.",
  "t":["black-and-white","colour woodcut","chiaroscuro woodcut","book illustration","single sheet","lifetime impression","posthumous printing","on Japan paper"],
  "s":SG,
  "x":[
   {"n":"Dürer Apocalypse woodcut","a":"Apocalipsis cum figuris","d":"Dürer's 15 large woodcuts of the Book of Revelation, published by the artist with facing text.","mk":"Albrecht Dürer","y":"1498","s":AP,
    "v":[{"n":"1498 Latin edition","mk":"Albrecht Dürer","y":"1498","d":"Apocalipsis cum figuris, Nuremberg"},
         {"n":"1498 German edition","mk":"Albrecht Dürer","y":"1498","d":""},
         {"n":"1511 edition","mk":"Albrecht Dürer","y":"1511","d":"with Life of the Virgin and Large Passion; added title cut"},
         {"n":"Single-sheet impressions","mk":"Albrecht Dürer","y":"","d":"without text; e.g. The Four Horsemen (c. 1497–98)"}],
    "dt":"edition (text on verso or none) · sheet · impression quality · watermark"},
   {"n":"Munch woodcut","a":"","d":"Munch's colour woodcuts, with blocks sawn apart like a jigsaw for separate inking or printed over raw plank grain.","mk":"Edvard Munch","y":"1897–1902","s":MU,
    "v":[{"n":"The Kiss I and II","mk":"Edvard Munch","y":"1897","d":""},
         {"n":"The Kiss III","mk":"Edvard Munch","y":"1898","d":""},
         {"n":"The Kiss IV","mk":"Edvard Munch","y":"1902","d":"grey and black from two blocks on Japanese paper; printed by Lassally; V&A"}],
    "dt":"version · colours and blocks · paper · signed · printer"},
   {"n":"Gauguin Noa Noa woodcut","a":"Noa Noa suite","d":"Gauguin's ten Tahitian woodcuts made for his Noa Noa book project and first shown in his Paris studio in 1894.","mk":"Paul Gauguin","y":"1893–94","s":NN,
    "v":[{"n":"Fragrance (Noa Noa) title block","mk":"Paul Gauguin","y":"1893–94","d":"block of nine joined fruitwood sections; Met"}],
    "dt":"print from the suite · Gauguin's own or later printing · inking · paper"},
   {"n":"German Expressionist woodcut","a":"Brücke woodcut","d":"A bold woodcut by the Dresden Brücke group, who made the medium central to their work.","mk":"","y":"from 1905 to the 1920s–30s","s":ST,
    "v":[{"n":"Woodcuts","mk":"Ernst Ludwig Kirchner","y":"","d":"Brücke founder"},
         {"n":"Woodcuts","mk":"Erich Heckel","y":"","d":"Brücke founder"},
         {"n":"Woodcuts","mk":"Karl Schmidt-Rottluff","y":"","d":"Brücke founder"}],
    "dt":"artist · colour or black · block grain · edition or proof · paper"}]},
 {"n":"Linocut","a":"linoleum cut · lino print","d":"A print cut into a linoleum sheet and printed from the raised surface.",
  "t":["black-and-white","colour linocut","reduction linocut","multi-block","trial proof","numbered edition"],
  "s":SG,
  "x":[
   {"n":"Picasso reduction linocut","a":"","d":"A colour linocut printed from one block that is cut back between colours, so no further impressions can be pulled afterwards.","mk":"Pablo Picasso","y":"from 1959","s":PI,
    "v":[{"n":"Portrait de Jacqueline accoudée, au collier","mk":"Pablo Picasso","y":"1959","d":"three colours from one block; trial proof before the 1960 edition; British Museum"}],
    "dt":"trial proof or edition · number · signature · colours"}]},
 {"n":"Wood engraving","a":"","d":"A print cut with gravers into the end grain of a hardwood block.",
  "t":["book illustration","vignette","tail-piece","proof","later printing from the blocks"],
  "s":"https://gerrishfineart.com/product/gander/",
  "x":[
   {"n":"Bewick wood engraving","a":"","d":"Bewick's natural-history wood engravings on end-grain boxwood, with small humorous tail-pieces of country life.","mk":"Thomas Bewick","y":"1790–1820s","s":HB,
    "v":[{"n":"A General History of Quadrupeds","mk":"Thomas Bewick","y":"1790","d":"with Ralph Beilby"},
         {"n":"A History of British Birds, vol. 1 Land Birds","mk":"Thomas Bewick","y":"1797","d":"text by Ralph Beilby"},
         {"n":"A History of British Birds, vol. 2 Water Birds","mk":"Thomas Bewick","y":"1804","d":""},
         {"n":"Supplement","mk":"Thomas Bewick","y":"1821","d":""},
         {"n":"Memorial Edition","mk":"","y":"1885","d":"royal octavo"}],
    "dt":"edition · paper size · proof or book impression"}]},
 {"n":"Chinese New Year print","a":"nianhua · New Year picture","d":"A coloured woodblock print hung for decoration and ritual at Chinese New Year and replaced each year.",
  "t":["door god","Kitchen God","God of Wealth","babies and beauties","opera and story scenes","hand-coloured","colour-block printed"],
  "s":NY,
  "x":[
   {"n":"Yangliuqing New Year picture","a":"","d":"A Tianjin New Year picture combining woodblock printing with fine hand-colouring.","mk":"","y":"Ming; peak under the Yongzheng, Qianlong and Guangxu reigns","s":YL,
    "v":[{"n":"Dai Lianzeng workshop","mk":"","y":"","d":"introduced colour woodblock printing and refined hand-colouring"},
         {"n":"Qi Jianlong workshop","mk":"","y":"","d":""}],
    "dt":"subject · workshop · hand-colouring and gold · age (few pre-19th-century survivors)"},
   {"n":"Yangjiabu New Year picture","a":"Weifang New Year print","d":"A New Year print from the Yangjiabu workshops of Shandong.","mk":"","y":"","s":NY,
    "dt":"subject · colours · old or revival printing"},
   {"n":"Taohuawu New Year picture","a":"Suzhou New Year print","d":"A New Year print from the Taohuawu workshops of Suzhou.","mk":"","y":"","s":NY,
    "dt":"subject · colours · old or revival printing"}]}]
def B(n,c,kf,d,s,sig): return {"n":n,"c":c,"f":"","seg":"Artisan & independent","kf":kf,"d":d,"s":s,"sig":sig}
brands=[
 B("Albrecht Dürer","Germany","woodcut, engraving","German Renaissance painter and printmaker who published his own Apocalypse woodcuts in 1498.",AP,["Dürer Apocalypse woodcut"]),
 B("Edvard Munch","Norway","colour woodcut","Norwegian painter and printmaker known for jigsaw-cut colour woodcuts.",MU,["Munch woodcut"]),
 B("Paul Gauguin","France","woodcut","French painter whose Noa Noa woodcuts renewed the medium.",NN,["Gauguin Noa Noa woodcut"]),
 B("Pablo Picasso","Spain","reduction linocut","Spanish artist who developed the one-block reduction linocut from 1959.",PI,["Picasso reduction linocut"]),
 B("Thomas Bewick","United Kingdom","wood engraving","English wood engraver of natural-history books on end-grain boxwood.",HB,["Bewick wood engraving"]),
]
trads=[{"n":"Chinese New Year prints","g":"Paper & print","r":"China (Tianjin, Shandong, Suzhou, Hebei, Shaanxi, Sichuan)","p":"Tang origins; flourished late Ming to Qing; revived as heritage industry",
 "d":"Coloured woodblock pictures printed for decoration and ritual at Chinese New Year.","tech":"design pasted on a board and carved in relief; one block per colour, sometimes hand-coloured",
 "mat":"wood blocks, paper, colours","forms":["Chinese New Year print","door god","Kitchen God"],
 "ctr":["Yangliuqing (Tianjin)","Yangjiabu (Shandong)","Taohuawu (Suzhou)","Wuqiang (Hebei)","Fengxiang (Shaanxi)","Mianzhu (Sichuan)"],
 "auth":"few authentic examples date before the 19th century; most on the market are later or revival printings","s":NY}]
out={"kinds":kinds,"brands":brands,"traditions":trads,
 "notes":"All three old kinds kept; Chinese New Year print added with a tradition entry. Japanese woodblock prints are on their own shelf. Yangliuqing is a national ICH item (2006) per Wikipedia. No individual Brücke prints named because the fetched Städel page names none. Noa Noa later printings not confirmed on a fetched page, so left out."}
p='work/F2/shelves/02_01.json'; t=p+'.tmp'
json.dump(out,open(t,'w'),ensure_ascii=False,indent=1); os.replace(t,p)
