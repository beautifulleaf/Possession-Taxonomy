import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
INC = W + 'Incunable'
IM = W + 'Illuminated_manuscript'
WAS = W + 'Wasōbon'
CHN = W + 'Traditional_Chinese_bookbinding'
PALM = W + 'Palm-leaf_manuscript'
CHAP = W + 'Chapbook'
COL = 'https://exhibitions.library.columbia.edu/exhibits/show/quran/qurans/bindings'
ETH = 'https://www.textmanuscripts.com/medieval/ethiopian-psalter-in-geez-141654'
kinds = [
 {"n": "Incunabulum", "a": "incunable · cradle book", "d": "Book, pamphlet or broadside printed in Europe up to the end of 1500.",
  "t": ["on paper", "on vellum", "rubricated", "hand-coloured woodcuts", "block book", "fragment or single leaf"],
  "s": INC,
  "x": [
   X("Gutenberg Bible", "The first major book printed with movable type, in 42-line columns, at Mainz.", "Johannes Gutenberg", "1454–1455", W + "Gutenberg_Bible",
     [("Paper copies", "Johannes Gutenberg", "", "about three-quarters of the run"), ("Vellum copies", "Johannes Gutenberg", "", "")], a="42-line Bible · B42 · Mazarin Bible",
     dt="paper or vellum · complete or partial · single leaf"),
   X("Block book", "Book printed from one carved wooden block per page (xylographic printing).", "", "15th century", INC, dt="text and image cut together · hand colouring"),
   X("Jenson roman-type incunabulum", "Venetian books in the roman type that made the definitive break from blackletter.", "Nicolas Jenson", "1470", W + "Nicolas_Jenson", dt="paper or vellum · illumination"),
   X("Nuremberg Chronicle", "The most common incunable, a world history integrating some 1,800 woodcuts with the text.", "Anton Koberger", "1493", W + "Nuremberg_Chronicle",
     [("Latin edition", "Anton Koberger", "1493", "12 July"), ("German edition", "Anton Koberger", "1493", "23 December"), ("Augsburg pirated editions", "Johann Schönsperger", "late 1490s", "smaller format")],
     a="Liber Chronicarum · Schedel's Chronicle", dt="Latin or German · hand-coloured or plain · completeness · single leaves"),
   X("Aldine incunabulum", "Books from Aldus Manutius's Venetian press, including first editions of Greek texts.", "Aldine Press", "1495", W + "Aldine_Press", dt="Greek or Latin · condition"),
  ]},
 {"n": "Hand-press book", "a": "early printed book · post-incunable · antiquarian book", "d": "Book printed on a hand press after 1500 and before machine printing, roughly 1501–1830.",
  "t": ["post-incunable (1501–c.1540)", "folio", "quarto", "octavo", "duodecimo", "contemporary binding", "rebound"],
  "s": INC,
  "x": [
   X("Aldine octavo", "Small portable octavo editions, the first standard octavos, often in italic type, with the dolphin-and-anchor device.", "Aldine Press", "1501", W + "Aldine_Press",
     [("Libelli portatiles", "Aldine Press", "1505", ""), ("Later family editions", "Aldine Press", "1515–1597", "")], dt="italic or roman · device · vellum copies"),
   X("Plantin imprint", "Antwerp books of the Officina Plantiniana, including the multi-language Polyglot Bible.", "Officina Plantiniana", "1555", W + "Christophe_Plantin",
     [("Polyglot Bible (Biblia Regia)", "Officina Plantiniana", "1568–1572", "Latin, Greek, Syriac, Aramaic, Hebrew")], dt="format · device · binding"),
   X("Elzevir duodecimo", "Small 12mo, 16mo and 24mo Dutch editions prized for elegant design, clear type and fine paper.", "Elzevir", "17th century", W + "House_of_Elzevir",
     [("Republics series", "Elzevir", "1626–1649", "35 volumes, ancestor of the travel guide"), ("Amsterdam Elzevirs", "Elzevir", "1638", "Minerva device")], dt="format · Leiden or Amsterdam · tall copies"),
   X("Baskerville edition", "Birmingham printing in Baskerville's types on smooth wove paper with wide margins.", "John Baskerville", "1757", W + "John_Baskerville",
     [("Quarto Virgil", "John Baskerville", "1757", "wove paper"), ("Cambridge University printing", "John Baskerville", "1758", "")], dt="paper (wove or laid) · format"),
   X("Bodoni edition", "Parma printing in Bodoni's high-contrast Modern types, admired for spacing and layout.", "Giambattista Bodoni", "1768", W + "Giambattista_Bodoni",
     [("Ducal press", "Giambattista Bodoni", "1768", ""), ("Private press", "Giambattista Bodoni", "1791", ""), ("Manuale Tipografico", "Giambattista Bodoni", "1818", "posthumous type specimen")], dt="format · paper"),
  ]},
 {"n": "Illuminated manuscript", "a": "illuminated codex · miniature · cutting", "d": "Handwritten book whose text is decorated with initials, borders and miniatures, often in gold.",
  "t": ["complete codex", "single leaf", "cutting or miniature", "on vellum", "on paper"],
  "s": IM,
  "x": [
   X("Book of hours", "Lay prayer book for the canonical hours, the most common surviving medieval illuminated manuscript.", "", "later 13th–early 16th century", W + "Book_of_hours",
     [("Paris books of hours", "", "", "Paris led early illumination"), ("Flemish books of hours", "", "", "led until the early 16th century"), ("Printed books of hours", "", "late 15th century", "woodcut illustration")],
     dt="calendar · Little Office of the Virgin · miniatures count · single leaves"),
   X("Psalter", "Liturgical book usually containing all 150 psalms.", "", "medieval", IM, dt="miniatures · initials"),
   X("Gospel book", "The most lavish illuminated books of the first millennium.", "", "first millennium", IM, dt="Insular, Carolingian or Ottonian style"),
   X("Bestiary", "Illustrated book of animals with religious symbolism.", "", "medieval", IM),
   X("Illuminated Qur'an", "Qur'an manuscripts decorated with frontispieces and headings rather than figures.", "", "9th century", IM, dt="script · illuminated headings · binding"),
   X("Persian illustrated manuscript", "Whole books illustrated with Persian miniatures.", "", "14th century", IM, dt="miniatures · binding"),
  ]},
 {"n": "Manuscript book", "a": "codex · handwritten book", "d": "Handwritten codex not chiefly decorated, such as a commonplace book or a scriptural or liturgical manuscript.",
  "t": ["commonplace book", "recipe or remedy book", "on parchment", "on paper"],
  "s": W + "Commonplace_book",
  "x": [
   X("Commonplace book", "Personal notebook collecting quotations, recipes, remedies and other notes under subject headings.", "", "Renaissance–early 20th century", W + "Commonplace_book",
     [("Zibaldone", "", "Renaissance", "Italian miscellany")], dt="owner · contents · binding"),
   X("Ethiopian Ge'ez manuscript", "Parchment manuscript in Ge'ez script in black and red ink, sewn with link-stitch into wooden boards.", "", "", ETH,
     [("Psalter", "", "19th century", "")], dt="leaves · leather cover or bare boards"),
   X("Islamic manuscript in flap binding", "Manuscript in a leather binding with a fore-edge flap closing like an envelope, stored lying flat.", "", "", COL,
     [("Ottoman binding", "", "", "blind-tooling with gilt painting"), ("Qajar binding", "", "1795–1925", "crown-shaped pendants")], dt="blind or gold tooling · medallion and pendants"),
  ]},
 {"n": "Japanese thread-bound book", "a": "wahon · wasōbon · fukuro-toji · stab-bound book", "d": "Traditional Japanese book of folded washi sheets sewn at the loose edges, usually woodblock-printed.",
  "t": ["fukuro-toji (pouch)", "detchōsō (glued)", "tetsuyōsō (sewn)", "ōbon", "yotsuhanbon", "kobon", "manuscript or printed"],
  "s": WAS,
  "x": [
   X("Edo woodblock-printed book", "Commercially printed Edo-period book in fukuro-toji binding, the form of about 90% of Edo books.", "", "1603–1867", WAS, dt="size class · printing · covers"),
   X("Ehon", "Edo-period woodblock-printed illustrated book.", "", "Edo period", W + "Ehon",
     [("Monochrome ehon", "", "", ""), ("Polychrome (nishiki-e) printing", "", "1765", ""), ("First large full-colour commercial book", "", "1770", "Katsukawa Shunshō and Ippitsusai Bunchō")],
     dt="monochrome or colour · impression · completeness of volumes"),
  ]},
 {"n": "Chinese thread-bound book", "a": "xianzhuang · stitched binding", "d": "Chinese book of folded leaves side-stitched with silk cord through holes along the spine.",
  "t": ["four-hole (standard)", "six-hole (important books)", "paper cover (dark blue)", "yellow silk cover (imperial)", "with cloth case"],
  "s": CHN,
  "x": [
   X("Xianzhuang thread binding", "Side-stitched binding that replaced pasted bindings as the final phase of traditional East Asian bookbinding.", "", "16th–17th century", CHN,
     [("Chinese four-hole", "", "", "six holes for important books"), ("Korean odd-hole", "", "", "three or five holes")], dt="xuan paper · cover · cloth case with bone tallies"),
  ]},
 {"n": "Palm-leaf manuscript", "a": "lontar · pesa · olai", "d": "Manuscript on dried palmyra or talipot leaves, incised with a stylus and strung through holes.",
  "t": ["single leaf", "bundle", "with wooden covers"],
  "s": PALM,
  "x": [
   X("Indian palm-leaf manuscript", "Palm-leaf manuscripts from the subcontinent, where the form began.", "", "5th century BCE–19th century", PALM, dt="region (Odisha, Kerala, Tamil Nadu, Assam) · script"),
   X("Balinese lontar", "Indonesian palm-leaf manuscript, called lontar in Bali.", "", "", PALM),
   X("Burmese pesa", "Burmese palm-leaf manuscript.", "", "", PALM),
  ]},
 {"n": "Chapbook", "a": "street literature · bibliothèque bleue · cordel", "d": "Small cheap popular booklet of one folded sheet with crude woodcuts, sold by chapmen from the 16th to 19th centuries.",
  "t": ["8, 12, 16 or 24 pages", "saddle-stitched", "uncut sheet"],
  "s": CHAP,
  "x": [
   X("English chapbook", "Booklets of street literature sold door to door and at fairs.", "", "16th–19th century", CHAP),
   X("Bibliothèque bleue", "French chapbooks often wrapped in cheap blue paper.", "", "", CHAP),
   X("Pliego de cordel", "Spanish loose-sheet popular booklet.", "", "", CHAP, a="pliego suelto"),
   X("Literatura de cordel", "Portuguese and Brazilian popular booklets.", "", "", CHAP),
  ]},
]
brands = [
 {"n": "Aldine Press", "c": "Italy", "f": "1494", "seg": "Heritage manufactory", "kf": "octavos, italic type", "d": "Venetian press of Aldus Manutius, active until 1597.", "sig": ["Aldine octavo", "Aldine incunabulum"], "s": W + "Aldine_Press"},
 {"n": "Officina Plantiniana", "c": "Belgium", "f": "1555", "seg": "Heritage manufactory", "kf": "Antwerp printing", "d": "Christophe Plantin's Antwerp printing house, now the Plantin-Moretus Museum.", "sig": ["Plantin imprint"], "s": W + "Christophe_Plantin"},
 {"n": "Elzevir", "c": "Netherlands", "f": "1580", "seg": "Heritage manufactory", "kf": "small-format editions", "d": "Leiden and Amsterdam family of printers and publishers, active until 1712.", "sig": ["Elzevir duodecimo"], "s": W + "House_of_Elzevir"},
]
traditions = [
 {"n": "Western manuscript illumination", "g": "Books & paper", "r": "Europe and Byzantium", "p": "c. 400–16th century",
  "d": "Decoration of handwritten books with initials, borders, miniatures and burnished gold.", "tech": "pen and brush painting, gold leaf or shell gold, burnishing",
  "mat": "vellum, parchment, mineral and organic pigments, gold", "forms": ["Illuminated manuscript"], "ctr": ["Paris", "Flemish cities"],
  "auth": "parchment, pigments and script consistent with period; style (Insular, Carolingian, Ottonian, Romanesque, Gothic)", "s": IM},
 {"n": "Islamic manuscript and binding", "g": "Books & paper", "r": "Iran, Ottoman Empire, Arab world", "p": "9th century–19th century",
  "d": "Illuminated manuscripts in leather bindings with fore-edge and envelope flaps, stored lying flat.", "tech": "blind-tooling, block-stamped medallions, gold tooling, gilt painting",
  "mat": "leather, paper, gold", "forms": ["Illuminated manuscript", "Manuscript book"], "ctr": ["Ottoman", "Qajar Iran"],
  "auth": "flap structure, medallion-and-pendant stamping; binding may be later than the text block", "s": COL},
 {"n": "Ethiopian manuscript tradition", "g": "Books & paper", "r": "Ethiopia", "p": "",
  "d": "Parchment books in Ge'ez script, sewn with unsupported link-stitch and laced into wooden boards.", "tech": "link-stitch sewing, red and black ink rubrication",
  "mat": "parchment, wooden boards, leather", "forms": ["Manuscript book"], "ctr": [],
  "auth": "palaeography of the Ge'ez hand; board and sewing structure", "s": ETH},
 {"n": "Japanese wahon binding", "g": "Books & paper", "r": "Japan", "p": "late 8th century–Meiji period",
  "d": "Traditional Japanese book forms from scrolls to pouch-bound fukuro-toji books printed from woodblocks.", "tech": "fukuro-toji pouch binding, woodblock printing",
  "mat": "washi, thread", "forms": ["Japanese thread-bound book"], "ctr": ["Kyoto Gozan temples", "Edo commercial publishers"],
  "auth": "washi paper rather than wood-pulp paper; woodblock impression", "s": WAS},
 {"n": "Chinese thread binding", "g": "Books & paper", "r": "China, Korea, Japan, Vietnam", "p": "16th century onward",
  "d": "Side-stitched xianzhuang binding of folded leaves with silk cord, kept in cloth cases.", "tech": "folding printed sheets, punching four or six holes, stitching with double silk cord",
  "mat": "xuan paper, dyed paper or silk covers, white silk cord", "forms": ["Chinese thread-bound book"], "ctr": [],
  "auth": "hole count (Chinese even, Korean odd); paper and cover material", "s": CHN},
 {"n": "Palm-leaf manuscript tradition", "g": "Books & paper", "r": "South and Southeast Asia", "p": "5th century BCE–19th century",
  "d": "Texts incised into dried palm leaves and blackened, with leaves strung together through holes.", "tech": "stylus incision, colourant wiped into the grooves",
  "mat": "palmyra or talipot leaves, string", "forms": ["Palm-leaf manuscript"], "ctr": ["Saraswathi Mahal Library, Thanjavur", "Odisha State Museum", "Yangon"],
  "auth": "leaf preparation, script and regional format", "s": PALM},
]
notes = ("All eight planned new kinds built with archetypes. Printers Gutenberg, Jenson, Koberger, Baskerville and Bodoni are mk names without register entries; "
         "Aldine Press, Officina Plantiniana and Elzevir in the register. Hypnerotomachia and other individual titles not used beyond the brief's named reference books. "
         "Ethiopian and Islamic traditions sourced from a dealer catalogue entry and a Columbia exhibition page (Wikipedia pages for Islamic/Japanese bookbinding not found). "
         "Korean and Vietnamese thread binding noted under the Chinese tradition. Religious scripture cross-links F4.")
out = {"kinds": kinds, "brands": brands, "traditions": traditions, "notes": notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/F1/shelves/00_03.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
