import json, os
DS="https://doublestonesteel.com/blog/products/my-favourite-modernist-steel-door-handles-and-their-designers"
DZ="https://www.dezeen.com/2026/07/27/fsb-1138-door-handle-dieter-rams/"
FSB="https://fsbna.com/us/company/about"
kinds=[
 {"n":"Door handle","a":"door lever · door furniture","d":"Lever, knob or pull handle set for a door, without a lock; handle sets with a lock are in Home Safety & Security.",
  "t":["lever on rose","lever on backplate","knob","pull handle"],
  "s":"https://en.wikipedia.org/wiki/Door_handle",
  "x":[
   {"n":"Gropius door handle","a":"Bauhaus handle","d":"Walter Gropius lever with a cylindrical grip on a cranked, squared stem.","mk":"S.A. Loevy","y":"1923","s":DS,"v":[],"dt":"finish · rose or backplate"},
   {"n":"Wittgenstein door handle","a":"Haus Wittgenstein handle","d":"Ludwig Wittgenstein's handle for Haus Wittgenstein in Vienna, a prototype for curved tubular handles.","mk":"","y":"1927","s":"https://en.wikipedia.org/wiki/Door_handle","v":[],"dt":"finish"},
   {"n":"Wagenfeld door handle","a":"","d":"Lever designed by Wilhelm Wagenfeld in 1928; he designed a second handle in 1966.","mk":"","y":"1928","s":DS,
    "v":[{"n":"WD28CHR","mk":"Tecnoline","y":"","d":"polished stainless steel reissue"}],"dt":"finish"},
   {"n":"Lubetkin extended lever","a":"","d":"Extended lever by Max Burchartz, first conceived in 1929 as an economy item.","mk":"","y":"1929","s":DS,"v":[],"dt":"bronze and other finishes"},
   {"n":"FSB 1138","a":"Rams handle","d":"Dieter Rams lever with round rose, index-finger recess and gently rounded lever, from FSB's 1986 handle workshop.","mk":"FSB","y":"1986","s":DZ,
    "v":[{"n":"Original","mk":"FSB","y":"1986","d":"aluminium and thermoplastic; discontinued 2005"},
         {"n":"Relaunch","mk":"FSB","y":"2026","d":"all-aluminium"}],"dt":"aluminium · rose"},
   {"n":"FSB 1292","a":"","d":"Lever handle series developed by FSB with Foster + Partners.","mk":"FSB","y":"","s":FSB,"v":[],"dt":"finish"}
  ]},
 {"n":"Door hinge","a":"","d":"Hinge on which a door, gate or window leaf swings.",
  "t":["butt","parliament","butterfly","flush","tee","H","single cranked","double cranked","spring","continuous"],
  "s":"https://en.wikipedia.org/wiki/Hinge"},
 {"n":"Cabinet knob","a":"cabinet pull · drawer knob","d":"Knob or pull handle fitted to a cabinet door or drawer.",
  "t":["knob","pull handle","cup handle"],
  "m":[["Kensington Knurled Cabinet Knob","Elite Knobs & Handles"]],
  "s":"https://www.screwfix.com/c/security-ironmongery/cabinet-knobs/cat840284"},
 {"n":"Door knocker","a":"","d":"Hinged knocker and striking plate fixed to an outside door.",
  "t":["ring","hammer","figural"],
  "s":"https://en.wikipedia.org/wiki/Door_knocker"},
 {"n":"Letter plate","a":"letter flap · letterbox · mail slot","d":"Slot with flap and plate cut through a door to take post.",
  "t":["horizontal","vertical","gravity flap","sprung flap","inner flap","letter cage"],
  "m":[["Nu Mail Edge 68 Letter Plate","Fab & Fix"]],
  "s":"https://en.wikipedia.org/wiki/Letter_box"},
]
brands=[
 {"n":"FSB","c":"Germany","f":"1881","seg":"design door and window hardware","d":"Franz Schneider Brakel, door and window handle maker founded in Iserlohn and based in Brakel since 1909.",
  "lines":["FSB 1292 series"],"eras":["Otl Aicher, from 1981","1986 handle workshop (Rams, Botta, Hollein, Mendini)"],"sig":["FSB 1138","FSB 1292"],"sc":[],"rel":[],"s":FSB},
 {"n":"HOPPE","c":"Switzerland","f":"1952","seg":"mainstream door and window hardware","d":"Family firm founded by Friedrich Hoppe in Heiligenhaus, later Stadtallendorf; Swiss-headquartered maker of door and window hardware.",
  "lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://archello.com/de/brand/hoppe"},
 {"n":"Carlisle Brass","c":"United Kingdom","f":"1986","seg":"mainstream architectural ironmongery","d":"Carlisle-based maker and distributor of door furniture, hinges, locks, latches and cabinet hardware.",
  "lines":[],"eras":[],"sig":[],"sc":[],"rel":[],"s":"https://bira.co.uk/suppliers/carlisle-brass-limited"},
]
out={"kinds":kinds,"brands":brands,"traditions":[],
 "notes":"Fire-rated Smith & Locke SKU list dropped (trade SKUs) and replaced by sourced design-classic archetypes; blank hinge patterns became types. From the Anvil left out (no fetchable brand page); FSB 1020/Potente left out (MoMA page blocked). No traditions needed."}
p="work/C8/shelves/08_00.json"; json.dump(out,open(p+".tmp","w"),ensure_ascii=False,indent=1); os.replace(p+".tmp",p)
