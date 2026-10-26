import json, os
MA='https://themodernapprentice.com/gen_equipment.htm'
HOODS='https://www.themodernapprentice.com/hoods.htm'
TT='https://en.wikipedia.org/wiki/Falconry_training_and_technique'
JESS='https://en.wikipedia.org/wiki/Jess_(falconry)'
HC='https://www.hawk-conservancy.org/2020/10/05/the-equipment-we-use/'
GLOVE='https://www.themodernapprentice.com/glove.htm'
BELL='https://themodernapprentice.com/bell.htm'
PF='https://peregrinefund.org/sites/default/files/2019-09/bor-Asno-Pete.pdf'
LURE='https://en.wikipedia.org/wiki/Lure_(falconry)'
PER='https://themodernapprentice.com/perches.htm'
VA='https://collections.vam.ac.uk/item/O317603/falconry-bag/'
SJ='https://www.spokanejournal.com/articles/11753-fine-furnishings-for-falcons'
TEL='https://www.themodernapprentice.com/telemetry.htm'
WB='https://en.wikibooks.org/wiki/Falconry/Telemetry'
OR='https://oregonfalconers.com/?p=3673'
FAL='https://en.wikipedia.org/wiki/Falconry'
UN='https://ich.unesco.org/en/RL/falconry-a-living-human-heritage-01708?RL=01708'
TAK='https://en.wikipedia.org/wiki/Takagari'
def X(n,d,s,a='',mk='',y='',v=None,dt=''):
    return {"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"dt":dt}
def V(n,d='',mk='',y=''): return {"n":n,"mk":mk,"y":y,"d":d}
kinds=[
 {"n":"Falconry hood","a":"burqa (Arabic) · hawk hood","d":"Leather cap covering a raptor's eyes to keep it calm, opened and closed by braces at the back.","s":HOODS,
  "t":["blocked (moulded on a hood block)","unblocked","with braces","slip-on (no braces)","kip leather","kangaroo leather","top knot or plume","eye panels (felt)","rufter (trapping hood)"],
  "x":[
   X("Arab hood","Circular pattern moulded on a block, flat back, braces woven through leather pleats giving an accordion-like back.",HOODS,a="burqa · Bahraini hood",
     dt="leather colour · stitching and decoration · size by species"),
   X("Dutch hood","Traditionally three-piece hood moulded on a block, with an inverted-V back opening and a contoured beak opening; the widest-fitting style.",HOODS,a="blocked hood",
     v=[V("Three-piece Dutch","traditional construction, moulded on a Mollen block"),V("One-piece Dutch","modern construction"),V("Sugisaki Dutch chinstrap","Dutch pattern with adjustable chin strap","Kazuhiko Sugisaki")],
     dt="leather (kip, kangaroo) · feather or leather top knot · coloured panels · size"),
   X("Indian hood","Unblocked hood with a straight seam and triangular beak opening; suited to accipiters and eagles.",HOODS,a="Pakistan hood · Amritsari hood",
     v=[V("Afghan hood","chin strap made as a separate piece"),V("Sugisaki Pakistan (artistic) hood","modern modification of a Persian style","Kazuhiko Sugisaki")]),
   X("Anglo-Indian hood","Indian pattern cut from one piece of leather and fitted with Dutch-style braces; usually unblocked.",HOODS,y="probably 19th century",
     dt="one-piece leather · flared around the eyes"),
   X("Anglo-Syrian hood","Dutch hood modified with the Arab accordion back opening.",HOODS,a="Syrio-Dutch hood",mk="Griff Morgan-Jones"),
   X("Kazakh hood","Slip-on eagle hood with a tab at the top or back instead of a top knot, used by Kazakh eagle falconers.",HOODS,
     v=[V("Austringer field hood","blocked slip-on without braces, for accipiters and hawks","Ken Hooke"),V("Berkutchi hunter hood","slip-on eagle hood without braces","Griff Morgan-Jones")]),
   X("Khan hood","Modern hood combining Syrian, Dubai and Turkish styles.",HOODS,mk="Ken Hooke",
     v=[V("Spanish Khan"),V("Bonelli Khan"),V("Mjooke Khan","","Griff Morgan-Jones")]),
   X("British game-hawking hood","Traditional British hood with felt eye panels (red for game hawks, green for crow hawks) and a plume of quarry feathers.",HOODS),
   X("Moulded ultra-light hood","Polycarbonate hood about 30% lighter than a leather Dutch hood, with Gore-Tex braces; vented version available.",HOODS,mk="High-Tech Falconry",
     dt="vented or closed · colour"),
  ]},
 {"n":"Falconry glove","a":"gauntlet · hawking glove","d":"Thick leather glove, traditionally worn on the left hand, that serves as the bird's perch on the fist.","s":GLOVE,
  "t":["single thickness","double-thick over the hand","D-ring for tying the bird","custom-fitted","welder's glove (budget substitute)","left-hand","right-hand"],
  "x":[
   X("Falcon glove","Short glove covering only the hand and wrist.",GLOVE,dt="leather · single or double layer · D-ring"),
   X("Hawk gauntlet","Longer gauntlet-style glove with a long cuff, for powerful hawks.",GLOVE,dt="cuff length · double-thick palm and hand"),
   X("Eagle glove","Heavy glove or sheath that may cover the whole forearm and part of the chest.",TT),
   X("Mangalah","Cuff used instead of a gauntlet in Middle Eastern falconry.",MA,a="mankalah"),
  ]},
 {"n":"Jesses and anklets","a":"Aylmeri · bracelets","d":"Thin straps fitted to a raptor's legs by which the falconer holds or tethers it.","s":JESS,
  "t":["leather","kangaroo leather","nylon","parachute cord or braid","mews jesses (with swivel slit)","flying/hunting jesses (no slit)","jess extender"],
  "x":[
   X("Traditional jesses","Single knotted leather strap looped through itself around the ankle.",JESS),
   X("Aylmeri jesses","Two-part system: a grommeted leather anklet and a removable jess strap with a knotted button.",JESS,mk="Guy Aylmeri",y="1900s",
     v=[V("Mews jesses","longer, with a slit for the swivel and leash"),V("Flying jesses","short, plain and stiff, no slit")],
     dt="brass grommet · leather or nylon · width to leg length"),
   X("False Aylmeri","Anklet with a brass eyelet set clear of the toes, taking removable flying and mews jesses.",TT),
  ]},
 {"n":"Leash and swivel","a":"","d":"Tether that attaches a raptor's jesses to a perch or glove, joined by a two-part rotating swivel to stop tangling.","s":TT,
  "t":["leather leash","braided or synthetic leash","stainless-steel swivel","traditional swivel","large-ring swivel","button end","loop leash"]},
 {"n":"Falconry bells","a":"hawk bells","d":"Small bells fitted to a raptor so the falconer can hear it in cover.","s":BELL,
  "t":["leg bell (on a bewit)","tail bell (clip on a feather shaft)","neck bell","brass","German silver","nickel-steel","matched pair with different tones"],
  "x":[
   X("Indian bell","Hand-made bell from Lahore with a pulled-in, silver-soldered waist.",PF,a="Lahore bell",v=[V("Muhammed Din bell","hand-made in Lahore; shown to Pete Asborno in the early 1940s","Muhammed Din")]),
   X("Asborno bell","American hand-made falconry bells by Peter J. Asborno, 'Ye Olde Bellmaker', in three perfected designs.",PF,mk="Peter J. Asborno",y="1940s–1989",
     v=[V("Acorn bell","top and bottom halves overlapped; hole drilled outside the overlap for tone","Peter J. Asborno"),V("Small two-metal bell","nickel silver and beryllium, for kestrel, merlin, sharp-shin and Cooper's hawk","Peter J. Asborno")]),
  ]},
 {"n":"Falconry lure","a":"","d":"Leather pad dressed with wings or feathers, often shaped like quarry, used to exercise and recall a bird.","s":LURE,
  "t":["swing lure (short line)","long-line lure","pole lure","meat lure","feathered lure","drag lure"]},
 {"n":"Falconry perch","a":"","d":"Stand on which a tethered raptor sits when not flying, shaped to the bird's family.","s":PER,
  "t":["Astroturf top","cork top","rope wrap","ground spike","heavy feet","heated"],
  "x":[
   X("Block perch","Short solid block, the traditional perch for falcons.",PER,v=[V("Arab block","flat top on a narrow, often taller body"),V("English block","one solid piece tapering to a wide body")],dt="cork or Astroturf top · height · spike or base"),
   X("Bow perch","Rope-wrapped metal or wood bow with a sliding ring, the traditional perch for hawks, owls and eagles.",PER,v=[V("Double bow perch","portable trolley-style")]),
   X("Ring perch","Rotating ring on a single spike, for small hawks.",PER),
   X("Screen perch","Horizontal bar topping a taut canvas screen, used indoors.",PER),
   X("Shelf perch","Shelf projecting from a mews wall, covered in sisal or Astroturf.",PER),
   X("Meng perch","Tail-saver perch with narrow top, wide rayed base and high ring.",PER,a="tail-saver perch",mk="Heinz Meng"),
   X("Presley perch","Rotating ring on a post raised well above the ground.",PER,mk="Floyd Presley"),
  ]},
 {"n":"Hawking bag and vest","a":"falconer's bag · game bag · hawking vest","d":"Bag or vest worn by the falconer to carry lure, food, tools and quarry in the field.","s":VA,
  "t":["shoulder bag (worn on the right side)","vest","mesh game pouch","one-hand closures","blaze orange"],
  "x":[X("Falconer's bag","Multi-pocket bag worn on the right side, with mesh pouches to keep game cool.",VA,y="18th century (Vienna example, 1755)",dt="leather · silk · embroidery · brass one-hand clasps"),
       X("Hawking vest","Vest with large pockets that open or secure with one hand.",SJ,mk="Pineo Falconry Furniture",dt="colour incl. blaze orange")]},
 {"n":"Falconry telemetry","a":"radio tracking","d":"Radio transmitter carried by the bird and a hand-held directional receiver used to find it.","s":TEL,
  "t":["leg-mounted transmitter","tail-mounted transmitter","neck-mounted transmitter","backpack (Teflon harness)","GPS tracker","Yagi antenna","216–219 MHz receiver","headset"],
  "x":[X("Radio transmitter and receiver","Beeping transmitter on the leg, tail or back tracked with a portable receiver.",WB,
         v=[V("Marshall tracking receivers","","Marshall Radio Telemetry"),V("Merlin Systems transmitters and receivers","","Merlin Systems"),V("L.L Electronics receivers","","L.L Electronics"),V("The Falconer RB-4 receiver","")],
         dt="frequency and channel · transmitter weight · mount"),
       X("GPS falconry tracker","GPS unit giving the bird's position and flight data.",HC,v=[V("Marshall GPS system","","Marshall Radio Telemetry")])]},
 {"n":"Giant hood","a":"hawk box · transport box","d":"Box in which a hooded or unhooded raptor travels in the dark.","s":MA},
]
brands=[
 {"n":"Marshall Radio Telemetry","c":"","f":"","seg":"falconry telemetry","d":"Maker of falconry tracking receivers and a GPS system.","lines":["tracking receivers","GPS system"],"eras":[],"sig":["Radio transmitter and receiver","GPS falconry tracker"],"sc":["falconry"],"rel":["Merlin Systems","L.L Electronics"],"s":OR},
 {"n":"Merlin Systems","c":"","f":"","seg":"falconry telemetry","d":"Maker of budget falconry transmitters and receivers.","lines":["transmitters","receivers"],"eras":[],"sig":["Radio transmitter and receiver"],"sc":["falconry"],"rel":["Marshall Radio Telemetry"],"s":OR},
 {"n":"L.L Electronics","c":"","f":"","seg":"falconry telemetry","d":"Maker of budget telemetry receivers.","lines":["receivers"],"eras":[],"sig":["Radio transmitter and receiver"],"sc":["falconry"],"rel":["Marshall Radio Telemetry"],"s":OR},
 {"n":"Pineo Falconry Furniture","c":"United States","f":"","seg":"falconry furniture maker","d":"Doug and Trish Pineo's Spokane-area workshop making hand-made hoods, hawking vests and bags, leashes, gloves and hardware.","lines":["hoods","hawking vests and bags","leashes","gloves"],"eras":[],"sig":["Hawking vest","Dutch hood"],"sc":["falconry"],"rel":[],"s":SJ},
 {"n":"High-Tech Falconry","c":"","f":"","seg":"falconry hoods","d":"Maker of moulded polycarbonate ultra-light hoods designed by Justin Tanner and Mike Todd.","lines":["Moulded ultra-light hood"],"eras":[],"sig":["Moulded ultra-light hood"],"sc":["falconry"],"rel":[],"s":HOODS},
]
trads=[
 {"n":"Falconry (UNESCO intangible heritage)","g":"Sport & hunting","r":"24 states incl. UAE, Saudi Arabia, Qatar, Syria, Morocco, Kazakhstan, Mongolia, Pakistan, Korea and much of Europe","p":"over 4,000 years; inscribed 2010, extended 2012, 2016 and 2021","d":"Multinational UNESCO element covering the training and flying of birds of prey, its equipment and the bond between falconer and bird.","tech":"breeding, manning, training and flying raptors","mat":"leather, metal","forms":["Falconry hood","Falconry glove","Jesses and anklets","Falconry bells","Falconry lure"],"ctr":["falcon hospitals","breeding centres","traditional equipment makers"],"auth":"","s":UN},
 {"n":"Arab falconry","g":"Sport & hunting","r":"Arabian Peninsula and Middle East","p":"popular by the early 7th century; ongoing","d":"Desert falconry with saker falcons, using the blocked burqa hood with pleated back, the mangalah cuff and flat-topped block perches.","tech":"hand-stitched blocked leather hoods","mat":"leather","forms":["Arab hood","Mangalah","Arab block"],"ctr":["Abu Dhabi Falcon Hospital"],"auth":"","s":FAL},
 {"n":"Takagari (Japanese falconry)","g":"Sport & hunting","r":"Japan","p":"4th century (Nihon Shoki); flourished in the Edo period","d":"Japanese hawking of the court and samurai class, chiefly with goshawks, organised in schools (ryū) and kept today by enthusiast clubs.","tech":"","mat":"","forms":["Kinran hood"],"ctr":[],"auth":"","s":TAK},
]
notes=("New shelf, no old data. Hoods follow The Modern Apprentice hood-style survey (Arab/Bahraini, Dutch, Indian/Pakistan, Anglo-Indian, Anglo-Syrian, Kazakh, Khan, game-hawking, polycarbonate). Kinran hood, Sultan, Hu, Ferrug Buteo hoods left out as minor maker variants. "
 "Added 'Giant hood' (hawk box) as its own kind per the shelf brief. Individual craftsmen (Griff Morgan-Jones, Ken Hooke, Kazuhiko Sugisaki, Peter J. Asborno, Guy Aylmeri, Heinz Meng, Floyd Presley) appear as archetype/version makers but have no brand-register entries (designers, not brands). "
 "Telemetry: makers taken from Oregon Falconers 2019 notes; no individual model names confirmed, so versions name product lines only; country/founding left blank. Swing lure etc. kept as types (no named archetypes sourced). No bell or swivel brands confirmed beyond Asborno; creance, scale, cadge, bewits not added (accessories outside the planned list). "
 "Takagari equipment specifics not sourced, so the tradition entry stays general; the Kinran hood mention in forms was removed if unsourced.")
trads[2]["forms"]=[]
out={"kinds":kinds,"brands":brands,"traditions":trads,"notes":notes.replace(" the Kinran hood mention in forms was removed if unsourced."," forms left empty.")}
p='/home/user/Possession-Taxonomy/rebuild/work/B10/shelves/05_01.json'
json.dump(out,open(p+'.tmp','w'),ensure_ascii=False,indent=1); os.replace(p+'.tmp',p); print('ok')
