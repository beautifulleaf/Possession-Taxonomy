import json, os
W='https://en.wikipedia.org/wiki/'
MO=W+'Monotyping'; BM='https://www.britishmuseum.org/collection/object/P_1968-0210-31'; FA='https://www.famsf.org/artworks/flag-from-the-lead-reliefs-series'
NG='https://nga.gov.au/art-artists/the-kenneth-e-tyler-collection/artists/david-hockney'; CO=W+'Collagraphy'; DG='https://theartwolf.com/exhibitions/degas-moma-2016/'
def v(n,mk,y,d=""): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Monotype","a":"","d":"A unique print pulled from ink or paint on a smooth, featureless plate; any second 'ghost' pull is weaker.",
  "t":["dark-field (ink wiped away)","light-field (ink brushed on)","ghost impression","reworked with pastel or paint","traced monotype"],
  "s":"https://www.sothebys.com/en/articles/the-complete-collectors-guide-to-prints",
  "x":[
   {"n":"Castiglione monotype","a":"","d":"The earliest monotypes: brushed black-field images wiped to white, often night scenes.","mk":"Giovanni Benedetto Castiglione","y":"mid-1640s","s":MO,"v":[],"dt":"black field · subject · impression"},
   {"n":"Degas monotype","a":"","d":"Monotypes wiped, scraped and scratched by Degas, often reworked after printing.","mk":"Edgar Degas","y":"from c. 1876","s":DG,
    "v":[v("Beside the Sea","Edgar Degas","1876–77"),v("Dancer onstage with a bouquet","Edgar Degas","c. 1876")],"dt":"first vs cognate (ghost) pull · reworked or not"},
   {"n":"Gauguin traced monotype","a":"oil transfer drawing","d":"A line image made by drawing on the back of paper laid on an inked sheet, the drawing often surviving on the verso.","mk":"Paul Gauguin","y":"c. 1902","s":BM,
    "v":[v("Two Marquesans","Paul Gauguin","c. 1902","British Museum 1968,0210.31; pencil drawing on verso")],"dt":"recto print · verso drawing · ink colour"}
  ]},
 {"n":"Monoprint","a":"","d":"A one-of-a-kind impression from a plate with fixed features (lines or textures) that recur, varied each time by inking or additions.",
  "t":["varied inking","chine-collé additions","hand-coloured","series of variants"],"s":"https://www.artsy.net/categories"},
 {"n":"Collagraph","a":"collograph","d":"A print from a plate built by gluing materials such as card, fabric or string to a rigid board, inked as relief, intaglio or both.",
  "t":["intaglio-inked","relief-inked","combined inking","editioned","variable edition"],"s":"https://www.1stdibs.com/buy/collagraph-print/",
  "x":[{"n":"Glen Alps collagraph","a":"","d":"Collagraphs from glued-up plates as developed and named by Glen Alps in the 1950s.","mk":"Glen Alps","y":"1950s onward","s":CO,"v":[],"dt":"plate materials · inking method · edition"}]},
 {"n":"Embossed print","a":"blind embossing · inkless intaglio · relief print","d":"An image made by pressing damp paper into a carved or built-up plate so the design stands in relief, mainly without ink. Embossing added to an inked print is not this.",
  "t":["blind (inkless)","with colour","cast paper","pressed metal relief"],"s":"https://www.motokawa.com/technique-painting/",
  "x":[
   {"n":"Gemini lead relief","a":"Lead Reliefs","d":"Thin lead sheet pressed into relief from the artist's models and mounted like a print, published as an edition.","mk":"Jasper Johns","y":"1969","s":FA,
    "v":[v("Flag (Lead Reliefs)","Gemini G.E.L.","1969","printed by Kenneth Tyler; 432 × 584 mm")],"dt":"lead sheet · mount · edition number"},
   {"n":"Paper-pulp print","a":"Paper Pools · cast and pressed paper pulp","d":"Images formed in coloured paper pulp poured and pressed in moulds, made with master printer Kenneth Tyler.","mk":"Tyler Graphics","y":"1978","s":NG,
    "v":[v("Paper Pools (e.g. A diver, paper pool 17)","David Hockney","1978","multi-sheet compositions")],"dt":"single sheet vs multi-panel · colour variant"}
  ]}
]
def a(n,c,kf,d,s,sig,seg="Artisan & independent",f=""): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s,"sig":sig}
brands=[
 a("Giovanni Benedetto Castiglione","Italy","monotype","Genoese artist credited with inventing monotype in the 1640s.",MO,["Castiglione monotype"]),
 a("Edgar Degas","France","monotypes","French artist who made and reworked many monotypes.",DG,["Degas monotype"]),
 a("Paul Gauguin","France","traced monotype","French artist who developed the traced monotype.",BM,["Gauguin traced monotype"]),
 a("Glen Alps","United States","collagraph","American printmaker who named and developed the collagraph.",CO,["Glen Alps collagraph"]),
 a("Jasper Johns","United States","prints","American artist; Lead Reliefs published by Gemini G.E.L. in 1969.",FA,["Gemini lead relief"]),
 a("Tyler Graphics","United States","print workshop","Kenneth Tyler's print workshop where Hockney made the Paper Pools in 1978.",NG,["Paper-pulp print"],"Specialist"),
 a("David Hockney","United Kingdom","prints","English-born artist who worked in all four of Kenneth Tyler's workshops.",NG,["Paper-pulp print"]),
]
notes="Four old kinds kept, nothing merged; monotype/monoprint distinction kept in definitions. Monoprint has no archetype (no named reference found). Rauschenberg embossed works not confirmed by a fetched page, so left out. Gemini G.E.L. register entry is on shelf 02_03."
out={"kinds":kinds,"brands":brands,"traditions":[],"notes":notes}
p='/home/user/Possession-Taxonomy/rebuild/work/F2/shelves/02_04.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p)
