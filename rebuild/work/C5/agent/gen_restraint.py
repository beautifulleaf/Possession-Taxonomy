import json, os, sys
OUT = "/home/user/Possession-Taxonomy/rebuild/work/C5/shelves"
os.makedirs(OUT, exist_ok=True)
J = "https://www.jetpens.com/"
OW = "https://www.officeworks.com.au/shop/officeworks/c/office-supplies"
OWD = "https://www.officeworks.com.au/shop/officeworks/c/office-supplies/desktop-organisation-desk-accessories"
RY = "https://www.ryman.co.uk/stationery-page"
HO = "https://www.hope-education.co.uk/products/stationery-and-office/stationery-accessories/clips-pins-and-fasteners"
ST = "https://www.staples.com/shredders-projectors-office-machines/cat_SC1681"
def K(n,a,d,s,t=None,m=None,r=None):
    k={"n":n,"a":a,"d":d}
    if t: k["t"]=t
    if m: k["m"]=m
    if r: k["r"]=r
    k["s"]=s
    return k
shelves = {
"01_03": ([
 K("Eraser","rubber","Block or stick of rubber or plastic that rubs out pencil or ink marks.",J+"Erasers/ct/34",
   ["block","stick (pen-style)","electric","kneaded","foam","ink eraser"],
   [["Tombow MONO Eraser","Tombow"],["Tombow MONO Stick","Tombow"],["Uni Boxy Eraser","Mitsubishi Pencil (Uni)"],["Seed Kado Loop","Seed"],["PLUS Air-In","PLUS"],["Sakura Arch","Sakura"],["Sakura Foam Eraser W","Sakura"],["Sakura Sumo Grip","Sakura"],["Prismacolor Kneaded Rubber Eraser","Prismacolor"]],
   [["Tombow MONO","Tombow"]]),
 K("Correction tape","","Dispenser that lays a dry white film over a written mark.",J+"Correction-Products/ct/1352",
   ["disposable","refillable","tape width"],
   [["Tombow MONO Air","Tombow"],["KOKUYO Campus Correction Tape","KOKUYO"],["PLUS Whiper Petit","PLUS"],["MD Correction Tape","Midori"],["Midori MAPKA Correction Tape","Midori"]],
   [["Tombow MONO","Tombow"],["KOKUYO Campus","KOKUYO"],["MD","Midori"]]),
 K("Correction fluid","white-out · Tipp-Ex","Quick-drying white liquid brushed or penned over a written mark.","https://www.huntoffice.ie/tippex-rapid-fluid-20ml-white-88715-tx48004x.html",
   ["brush bottle","correction pen"],[["Tipp-Ex Rapid","Tipp-Ex"]]),
], "Restraint-only: three old kinds kept one-to-one with all old models (within limit, ordered by market reach). Form variants (block, stick, electric, kneaded, foam; disposable/refillable tape; bottle/pen) moved into t. Brief-named brands without old-data models (Staedtler Mars Plastic, Pentel Hi-Polymer, Pritt) not added: no web research on this shelf, so nothing named from memory. Kneaded erasers for art remain in C4; kneaded kept here only as a type."),
"02_01": ([
 K("Calendar","","Printed sheets of the days, weeks or months of a year, for the wall, desk or pocket.","https://www.staples.com/2027-at-a-glance-6-5-x-7-5-monthly-wall-calendar-white-purple-pm5-28-27/product_24677166",
   ["wall calendar","desk calendar","pocket calendar","monthly","weekly","year planner"]),
 K("Day-by-day calendar","sticky-note calendar · tear-off calendar · ひめくり · himekuri","Tear-off or sticky-note calendar with one sheet per day.",J+"Himekuri-Sticky-Note-Calendars/ct/6415",
   ["tear-off","sticky-note"]),
 K("Sticky notes","adhesive notes","Pad of small sheets with a repositionable adhesive strip (\"adhesive notes\" in Australia).",J+"Sticky-Notes/ct/1345",
   ["square pad","ruled","index flags","die-cut shape","standing"],
   [["KOKUYO Tack Memo","KOKUYO"],["Midori Journal Sticky Notes","Midori"],["Sun-Star UFO Standing Sticky Notes","Sun-Star"],["Mind Wave Stand Sticky Notes","Mind Wave"],["Furukawashiko Hitokoto","Furukawashiko"],["EL COMMUN Obake","EL COMMUN"]],
   [["STALOGY","STALOGY"]]),
 K("Index card","revision card · flash card","Cut card of plain or ruled stock sold in packs for notes, filing and revision.",J+"Paper/ct/1320",
   ["plain","ruled","grid","ring-bound"]),
 K("Printer paper","copy paper","Plain cut sheets sold by the ream for copiers and printers; photographic paper is in Cameras & Photography.","https://www.huntoffice.ie/navigator-universal-a4-80gsm-white-printer-paper-box-of-500-sheets-ream.html",
   ["A4","US Letter","A3","70–80 gsm everyday","90–100 gsm premium","recycled"],
   [["Navigator Universal","The Navigator Company"],["Xerox Premier","Xerox"],["HP Premium","HP"]]),
], "Restraint-only: the two Calendar kinds merged (wall, desk, pocket as t types; the second old entry had no source, so the first's s kept). Sticky-note calendar renamed Day-by-day calendar with tear-off and sticky-note types. Printer paper keeps the three market brands from the old data with sizes and gsm as types. No models dropped; nothing added from memory."),
"02_02": ([
 K("Envelope","","Folded paper cover for posting a letter or document.",J+"Stationery-Paper/ct/2714",
   ["DL","C5","C4","window","airmail","laid paper","self-seal","gummed"],
   [["Clairefontaine Triomphe Envelope","Clairefontaine"],["Original Crown Mill Classic Laid Envelopes","Original Crown Mill"],["MD Envelopes","Midori"],["LIFE One Touch Airmail Envelopes","LIFE"]],
   [["Clairefontaine Triomphe","Clairefontaine"],["MD","Midori"]]),
 K("Padded envelope","jiffy bag · mailer","Envelope lined with bubble or paper padding for posting small items.","https://shop.mailcoms.co.uk/products/paper-padded-envelopes-mailers-150x215mm",
   ["bubble-lined","paper-padded"]),
 K("Mailing tube","postal tube","Rigid tube for posting rolled documents.","https://shop.mailcoms.co.uk/collections/postal-tubes",
   ["round","triangular"]),
 K("Greeting card","","Folded printed card with envelope, sold blank inside or with a message, to be written and sent.","https://Quill.com/better-office-hello-cards-envelopes-6-x-4-assorted-colors-100-pack-64561/cbs/55380852.html",
   ["blank inside","with message","birthday","thank-you","seasonal"]),
 K("Gift wrap","wrapping paper","Printed or decorated paper sold for wrapping presents.","https://www.americanretailsupply.com/gift-wrapping-packaging/gift-wrap.html",
   ["roll","sheet","tissue paper"]),
 K("Sticker sheet","","Sheet of printed self-adhesive stickers sold as stationery (a collectible sticker series is in Coins, Stamps, Medals & Trading Cards).","https://www.jetpens.com/Midori-Planner-Stickers-Removable-Shopping/pd/43744",
   ["planner stickers","decorative","removable"],
   [["Midori Planner Stickers","Midori"],["MD Notebook Diary Stickers","Midori"],["STALOGY Removable Calendar Stickers","STALOGY"]],
   [["MD","Midori"],["STALOGY","STALOGY"]]),
], "Restraint-only: six old kinds kept one-to-one. Greeting card: the single bulk-pack office SKU (Better Office Hello Cards, 100-pack) dropped as SKU noise. Other short model lists kept. Sizes, closures and occasions moved to t."),
"03_00": ([
 K("Desk organiser","desk tidy · pen cup · pen pot","Desk-top unit or pot with compartments for pens, notes and small supplies.",OWD,
   ["multi-compartment organiser","pen cup","drawer unit","rotating caddy"]),
 K("Letter tray & magazine file","document tray · letter tray · magazine holder · desktop magazine file","Flat stackable tray or upright open-sided box that holds papers, files or magazines on a desk.",OWD,
   ["letter tray","stacking tray","magazine file"]),
 K("Desk pad","blotter · desk mat","Large mat or blotting pad laid on the desk top to write on.","https://www.lucrin.com/customizable-desk-blotter.htm",
   ["leather blotter","felt or PU mat","paper desk pad"],[["Lucrin customizable desk blotter","Lucrin"]]),
 K("Pen case","pencil case · pen sleeve · pen roll","Pouch, box, roll or sleeve that holds one or several pens and pencils.",RY,
   ["single-pen sleeve","pen roll","zip case","box","pouch"],
   [["LAMY leather case for 1 pen","LAMY"],["Kaweco Eco Pouch 1 Liliput pen","Kaweco"],["Franklin-Christoph Leather Pen Sleeve (1 pen)","Franklin-Christoph"],["Rickshaw Solo Pen Sleeve","Rickshaw"]],
   [["Rickshaw Solo Pen Sleeve","Rickshaw"]]),
 K("Whiteboard","dry-erase board","Smooth board written on with dry-erase markers.",RY,
   ["melamine","painted steel (magnetic)","glass","mobile easel"]),
 K("Noticeboard","pinboard · bulletin board","Cork or fabric board to which notices are pinned.",RY,["cork","fabric","combination"]),
 K("Chalkboard","blackboard","Board with a dark surface written on with chalk.","https://office-japan.jp/en",["wall","A-frame","chalk-marker"]),
 K("Clipboard","","Rigid board with a spring clip at the top that holds paper to write on.",J+"Paper/ct/1320",["board","folding (clip folder)","storage box"]),
], "Restraint-only per plan: Pen cup merged into Desk organiser; Document tray and Magazine holder merged into Letter tray & magazine file; Pencil case and Pen sleeve merged into Pen case (sleeve, roll, zip case, box as types; s kept from the Pencil case entry). All old models kept (within limit). No kinds dropped."),
"03_01": ([
 K("Ring binder","lever arch file","Stiff cover with a ring or lever-arch mechanism that holds punched sheets.",RY,
   ["2-ring","4-ring","D-ring","lever arch","presentation (clear overlay)"]),
 K("Folder","file folder · box file · document wallet","Card or plastic cover, wallet or lidded box that holds loose unpunched sheets without rings.","https://www.jetpens.com/Paper/ct/1320",
   ["folder","document wallet","clear pocket folder","suspension file","box file"]),
 K("Punched pocket","sheet protector","Clear plastic sleeve, open at one edge and punched to file a sheet in a ring binder.",RY,
   ["standard","heavy-duty","expanding"]),
 K("Clips, pins & fasteners","","Small fasteners that hold sheets together or pin them to a board.",HO,
   ["paper clip","bulldog clip","binder clip","rubber band","drawing pin","treasury tag","split pin (paper fastener)","office magnet"]),
], "Restraint-only per plan: Lever arch file merged into Ring binder; Box file merged into Folder; seven fastener kinds (paper clip, bulldog clip, rubber band, drawing pin, treasury tag, paper fastener/split pin, office magnet) collapsed into Clips, pins & fasteners as types, s kept from the paper clip entry. Old data had no models here, so none listed."),
"03_02": ([
 K("Stapler","ホチキス","Device that drives a wire staple through sheets to join them; staples are its consumable.",OW,
   ["desktop","plier","long-arm","heavy-duty","electric","staples (consumable)"],
   [["MAX Stapler HD-10","MAX Co., Ltd."],["Rapid staples 26/6","Rapid (staples)"]]),
 K("Hole punch","","Device that cuts filing holes in sheets.",OW,["2-hole","4-hole","single-hole","heavy-duty"]),
 K("Desk tape & dispenser","sticky tape · tape dispenser","Narrow transparent adhesive tape for paper, and the weighted holder that cuts it.",OW,
   ["clear tape","matte invisible tape","double-sided","dispenser"],
   [["Scotch Desktop Tape Dispenser C19-CLIP-SR-W (Clip & Twist)","3M"]]),
 K("Glue stick","","Solid glue in a twist-up tube for sticking paper.","https://www.henkel.co.uk/brands-and-businesses/pritt-548302",
   ["standard","disappearing colour","acid-free"],[["Pritt Stick","Henkel"]]),
 K("Scissors","","General-purpose scissors for paper and household use.",OW,["office","left-handed","children's"]),
 K("Paper trimmer","guillotine","Guillotine or rotary cutter that trims sheets straight.",OW,["guillotine","rotary"],
   [["Dahle 18E Vantage guillotine trimmer","Dahle"]]),
], "Restraint-only per plan: Staples merged into Stapler as a consumable type (Rapid staples 26/6 kept as its model); Desk tape and Tape dispenser merged. Desk tape kind s kept from the old Desk tape entry. Brief-named tier brands with no models in the old data (Swingline, Leitz, Fiskars, Rapid staplers) not added: no web research on this shelf and nothing named from memory."),
"03_03": ([
 K("Ruler","rule","Straight strip with a graduated scale for measuring and ruling lines.",OW,["plastic","steel","wooden","flexible","15 cm","30 cm"]),
 K("Geometry set","maths set","Case of drawing compass, protractor, set squares and ruler sold as one set.","https://www.ocado.com/products/staedtler-noris-maths-set-11-pieces-639762011",
   ["tin","zip case"],[["Helix Oxford Maths Set","Helix"],["Staedtler Noris Maths Set (11 pieces)","Staedtler"]]),
 K("Drawing compass","","Two-legged instrument that draws circles and arcs (a navigation compass is in Sports, Fitness & Recreation).",OW,["school compass","precision bow compass","beam compass"]),
 K("Postal scale","letter scale","Small scale for weighing letters and parcels for postage.","https://octopus-office.co.uk/postal-scales/",["digital","mechanical"]),
], "Restraint-only: four old kinds kept one-to-one with their old models (Helix Oxford and Staedtler Noris maths sets); material, size and construction variants as t types. Nothing dropped or added."),
"04_02": ([
 K("Label maker","label printer · label tape","Device that prints adhesive labels on tape, standalone or from a computer or phone; tape cartridges are its consumable.",ST,
   ["handheld","desktop","app-connected","label tape cassette (consumable)"],
   [["Brother PT-H101C","Brother"],["Brother PT-N10","Brother"],["Brother QL-600","Brother"],["NIIMBOT M2H","NIIMBOT"]],
   [["Brother TZe","Brother"]]),
 K("Shredder","paper shredder","Machine that cuts paper into strips or particles; bin liner bags are its consumable.",ST,
   ["strip-cut","cross-cut","micro-cut","auto-feed","shredder bag (consumable)"],
   [["Fellowes Powershred P-25S","Fellowes"],["Fellowes P-42C","Fellowes"],["Fellowes Cross Cut Paper Shredder 12C","Fellowes"],["Fellowes AutoMax 80M","Fellowes"]],
   [["Fellowes Powershred","Fellowes"]]),
 K("Laminator","","Machine that seals a sheet between plastic films by heat or pressure; pouches are its consumable.",ST,
   ["A4","A3","A2","hot","cold","laminating pouch (consumable)"],
   [["Fellowes Arc A4","Fellowes"],["Fellowes Pixel A4","Fellowes"],["Fellowes Jupiter A3","Fellowes"],["Swordfish Armoured 660 A2","Swordfish"]]),
 K("Binding machine","","Machine that punches and binds sheets with combs, wires or covers; spines and covers are its consumables.",ST,
   ["comb","wire","thermal","binding comb or spine (consumable)","binding cover (consumable)"]),
], "Restraint-only per plan: one consumables entry per machine as t types (Label tape into Label maker, keeping range Brother TZe; Shredder bag into Shredder; Laminating pouch into Laminator; Binding comb and Binding cover into Binding machine). All old models kept. Brief-named brands without old-data models (Rexel, GBC, Dymo) not added: no web research and nothing named from memory."),
}
only = sys.argv[1:] or list(shelves)
for job in only:
    kinds, notes = shelves[job]
    p = os.path.join(OUT, job + ".json"); tmp = p + ".tmp"
    with open(tmp, "w") as f:
        json.dump({"kinds": kinds, "brands": [], "traditions": [], "notes": notes}, f, ensure_ascii=False, indent=1)
    os.replace(tmp, p)
    print("wrote", p)
