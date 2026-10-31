import json, os
W = 'https://en.wikipedia.org/wiki/'
PP = W + 'Private_press'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
kinds = [
 {"n": "Private press book", "a": "fine press book", "d": "Book designed, hand-set and printed, usually by hand press, at a private or fine press in a small edition.",
  "t": ["copy on vellum", "copy on handmade paper", "unbound in sheets", "publisher's binding", "special-bound copy"],
  "s": PP,
  "x": [
   X("Kelmscott Press book", "Hand-printed books in Morris's own Golden, Troy and Chaucer types with wood-engraved borders and initials.", "Kelmscott Press", "1891–1898", W + "Kelmscott_Press",
     [("Golden Type books", "Kelmscott Press", "1891", "Roman after 15th-century Venetian types"), ("Troy and Chaucer type books", "Kelmscott Press", "", "semi-Gothic"), ("Vellum copies", "Kelmscott Press", "", "a few copies of some books")],
     dt="type · paper (Batchelor handmade) or vellum · edition of about 300 · binding"),
   X("Doves Press book", "Austere unillustrated books in the single-size Doves Type, bound at the Doves Bindery.", "Doves Press", "1900–1916", W + "Doves_Press",
     [("Doves Bible", "Doves Press", "1902–1904", "5 volumes")], dt="paper or vellum · Doves Bindery binding"),
   X("Ashendene Press book", "St John Hornby's private press books in the Subiaco and Ptolemy types.", "Ashendene Press", "1895–1935", W + "Ashendene_Press",
     [("Subiaco type books", "Ashendene Press", "", ""), ("Ptolemy type books", "Ashendene Press", "", "")], dt="type · paper or vellum"),
   X("Essex House Press book", "Arts and Crafts books from C. R. Ashbee's Guild of Handicraft press, staffed by former Kelmscott printers.", "Essex House Press", "1898–1910", W + "Essex_House_Press",
     [("Endeavour type books", "Essex House Press", "1901", ""), ("Prayer Book type books", "Essex House Press", "1903", "")], dt="type · binding"),
   X("Cranach Presse book", "Anglo-German private press books with types by Edward Johnston and woodcuts by artists such as Maillol and Gill.", "Cranach Presse", "1913", "https://specialcollections-blog.lib.cam.ac.uk/?p=8365",
     dt="language edition · paper (Montval) or vellum · copy number"),
   X("Golden Cockerel Press book", "English fine press books known for original wood engravings and Eric Gill's Golden Cockerel type.", "Golden Cockerel Press", "1920–1961", W + "Golden_Cockerel_Press",
     [("Hal Taylor cooperative", "Golden Cockerel Press", "1920–1924", ""), ("Robert Gibbings era", "Golden Cockerel Press", "1924–1933", "wood engravings by Gill, Nash, Jones"),
      ("Golden Cockerel type", "Golden Cockerel Press", "1931", "designed by Eric Gill"), ("Sandford era", "Golden Cockerel Press", "1933–1959", "colour illustration")],
     dt="era · copy number · special binding"),
   X("Gregynog Press book", "Welsh private press books from Gregynog Hall, revived as Gwasg Gregynog.", "Gregynog Press", "1922", W + "Gregynog_Press",
     [("Davies sisters' press", "Gregynog Press", "1922", ""), ("Gwendolin type", "Gregynog Press", "1935", "by Graily Hewitt"), ("Gwasg Gregynog", "Gregynog Press", "1978", "University of Wales revival")],
     dt="era · special binding"),
   X("Nonesuch Press book", "Books designed by Francis Meynell and machine-printed by commercial printers for fine-press quality at lower prices.", "Nonesuch Press", "1922", W + "Nonesuch_Press",
     [("Meynell era", "Nonesuch Press", "1923", "first book May 1923"), ("Cygnet impression", "Nonesuch Press", "", "children's classics")], dt="limitation · binding"),
   X("Grabhorn Press book", "San Francisco fine printing by brothers Edwin and Robert Grabhorn.", "Grabhorn Press", "1920", W + "Grabhorn_Press", dt="limitation · binding"),
   X("Arion Press book", "Letterpress limited editions with original prints by prominent artists, set in hot-metal type.", "Arion Press", "1974", W + "Arion_Press",
     [("Lectern Bible", "Arion Press", "2000", "400 copies")], dt="limitation · original prints"),
  ]},
 {"n": "Subscription collector edition", "a": "book-club fine edition · leather-bound classic", "d": "Illustrated, decoratively bound edition of a classic sold by subscription or membership.",
  "t": ["full leather", "cloth with slipcase", "signed limited", "unsigned trade issue"],
  "s": W + "Limited_Editions_Club",
  "x": [
   X("Limited Editions Club", "Illustrated classics limited to 1,500 copies and signed by the illustrator or author, sold by subscription.", "Limited Editions Club", "1929", W + "Limited_Editions_Club",
     [("George Macy era", "Limited Editions Club", "1929–1956", "")], a="LEC", dt="monthly letter · signature · slipcase"),
   X("Heritage Press edition", "Lower-priced reissues of Limited Editions Club designs for a wider public.", "Heritage Press", "1935", W + "Limited_Editions_Club",
     [("First artist-signed volumes", "Heritage Press", "1935", "")], dt="Sandglass newsletter · slipcase"),
   X("Folio Society edition", "Illustrated hardback editions in specially designed bindings, sold first by membership.", "Folio Society", "1947", W + "Folio_Society",
     [("Membership book club", "Folio Society", "1947–2016", ""), ("Limited editions", "Folio Society", "", "hand-numbered, sometimes signed")], dt="slipcase · illustrator · limited or standard"),
   X("Franklin Library edition", "Leather-bound classics issued by subscription by the Franklin Mint's publishing arm.", "Franklin Library", "1973–2000", W + "Franklin_Mint",
     [("The Hundred Greatest Books of All Time", "Franklin Library", "", ""), ("Great Books of the Western World", "Franklin Library", "", "")], dt="series · leather colour"),
   X("Easton Press edition", "Premium leather-bound books with gilt edges, raised spine bands, ribbon markers and gold decoration.", "Easton Press", "1975", W + "Easton_Press",
     [("The Greatest Books Ever Written", "Easton Press", "", ""), ("Signed Modern Classics", "Easton Press", "", "")], dt="series · signed or unsigned · leather colour"),
  ]},
 {"n": "Limited signed edition", "a": "signed limited · collector's edition", "d": "Numbered or lettered special state of a book, signed by author or artist and printed in a fixed quantity.",
  "t": ["numbered", "lettered (26 or 52)", "traycased", "slipcased", "artist gift edition", "gift edition"],
  "s": "https://www.cemeterydance.com/faqs-book.html",
  "x": [
   X("Subterranean Press limited", "Genre fiction in signed numbered and lettered states with slipcases and traycases.", "Subterranean Press", "1995", W + "Subterranean_Press", dt="state · signature · case"),
   X("Centipede Press edition", "Oversized, signed or traycased collector hardbacks of horror, weird fiction and art books.", "Centipede Press", "2001", W + "Centipede_Press", dt="state · signature"),
   X("Suntup edition", "Letterpress fine-press limited editions in artist gift, numbered and lettered states.", "Suntup Editions", "2017", "https://www.finebooksmagazine.com/fine-books-news/suntup-editions-beautiful-stephen-king-books-prints",
     [("Artist Gift", "Suntup Editions", "", "signed by the illustrator"), ("Numbered", "Suntup Editions", "", ""), ("Lettered", "Suntup Editions", "", "moldmade paper")], dt="state · paper · signatures"),
   X("Lyra's Books edition", "Letterpress-printed leather-bound limited editions, lettered in solander traycases and numbered in slipcases.", "Lyra's Books", "", "https://www.collectiblebookvault.com/lyra/the-picture-of-dorian-gray-lettered",
     [("Lettered", "Lyra's Books", "", "26 copies, full goatskin, traycase"), ("Numbered", "Lyra's Books", "", "half leather, marbled boards, slipcase")], dt="state · leather · case"),
  ]},
 {"n": "Fine binding", "a": "extra binding · designer binding", "d": "Book bound or rebound by a named binder in high-quality materials, usually full leather with gold tooling.",
  "t": ["full leather", "half leather", "quarter leather", "gold tooled", "blind tooled", "jewelled", "inlaid or onlaid", "designer binding"],
  "s": W + "Bookbinding",
  "x": [
   X("Riviere binding", "Victorian trade fine binding identified by the binder's stamp inside the front cover.", "Riviere", "1829", W + "Robert_Riviere",
     [("Bound by R. Riviere, Bath", "Riviere", "1829–1832", ""), ("Riviere, London", "Riviere", "1840", "Great Queen Street, later Piccadilly"), ("Bound by Riviere & Son", "Riviere", "1880", "")], dt="stamp · leather · tooling"),
   X("Zaehnsdorf binding", "Distinct London fine binding style recognised by collectors.", "Zaehnsdorf", "1844", W + "Zaehnsdorf", dt="stamp · leather · tooling"),
   X("Doves Bindery binding", "Arts and Crafts bindings by T. J. Cobden-Sanderson, who also bound the Doves Press books.", "Doves Bindery", "1893", W + "T._J._Cobden-Sanderson", dt="leather · tooling"),
   X("Bayntun binding", "Bath fine bindings, joined with the Riviere bindery in 1939.", "Bayntun-Riviere", "1894", "https://georgebayntun.com/about-us",
     [("George Bayntun", "Bayntun-Riviere", "1894", "Northumberland Place, Bath"), ("Bayntun-Riviere", "Bayntun-Riviere", "1939", "Manvers Street")], dt="stamp · leather · tooling"),
   X("Sangorski & Sutcliffe binding", "Luxurious London bindings, famous for jewelled covers set with gold and precious stones.", "Sangorski & Sutcliffe", "1901", W + "Sangorski_&_Sutcliffe",
     [("Jewelled bindings", "Sangorski & Sutcliffe", "", "the Great Omar lost on the Titanic, 1912"), ("Shepherds revival", "Sangorski & Sutcliffe", "1998", "")], dt="stamp · jewels · leather"),
   X("Paul Bonet designer binding", "French modernist designer bindings using metals such as nickel, steel and duralumin in leather.", "Paul Bonet", "1926", "https://www.stephenongpin.com/artist/238576/paul-bonet",
     dt="unique design · materials · executing craftsmen"),
  ]},
 {"n": "Artist's book", "a": "livre d'artiste · bookwork", "d": "Work of art that uses the form of the book itself, editioned or unique.",
  "t": ["unique", "editioned", "codex", "scroll", "concertina", "boxed loose items"],
  "s": W + "Artist's_book",
  "x": [
   X("Russian Futurist book", "Small-edition books with handwritten text, lithographs and collage, where copies often differ.", "", "1910–1917", W + "Artist's_book", dt="lithograph or collage · edition"),
   X("Dieter Roth bookwork", "Books with holes or reused found printed matter that defined the modern artist's book.", "Dieter Roth", "1950s–1960s", W + "Artist's_book"),
   X("Conceptual photobook", "Cheap offset-printed books of serial photographs, in editions that grew into thousands.", "Ed Ruscha", "1963", W + "Artist's_book", dt="printing · edition size"),
  ]},
 {"n": "Facsimile edition", "a": "facsimile · quasi-original", "d": "Full-size reproduction of a manuscript or early book matching the original's colour, materials and flaws, often numbered.",
  "t": ["full facsimile", "partial facsimile", "with commentary volume", "numbered limited"],
  "s": W + "Facsimile",
  "x": [
   X("ADEVA facsimile", "Graz facsimiles setting high standards, notably of Aztec, Maya and Mixtec codices.", "Akademische Druck- u. Verlagsanstalt", "", "http://www.famsi.org/research/graz/", dt="codex · commentary"),
   X("Faksimile Verlag facsimile", "Lucerne facsimiles of illuminated medieval manuscripts with scholarly commentary volumes.", "Faksimile Verlag", "1974", "https://www.facsimilefinder.com/articles/treasures-of-the-past",
     [("First edition, 980 copies", "Faksimile Verlag", "1974", "")], dt="edition size · commentary"),
   X("Moleiro facsimile", "'Quasi-original' facsimiles of codices, maps and manuscripts in 987 notarised numbered copies.", "M. Moleiro Editor", "1991", W + "M._Moleiro_Editor", dt="copy number · binding"),
  ]},
 {"n": "Miniature book", "a": "thumb book · microminiature", "d": "Book no more than about 3 inches (76 mm) in height, width and thickness.",
  "t": ["macrominiature (3–4 in)", "miniature (≤3 in)", "microminiature (<1 in)", "ultra-microminiature (<1/4 in)", "thumb Bible"],
  "s": W + "Miniature_book",
  "x": [
   X("Diamond Classics", "Tiny-type London miniature classics.", "William Pickering", "1819", W + "Miniature_book"),
   X("Bryce miniature", "Glasgow miniatures, including a very small English dictionary, from a prolific maker of over 40 titles.", "David Bryce and Son", "19th century", W + "Miniature_book"),
   X("Collins Gem", "Pocket reference books.", "HarperCollins", "", W + "Miniature_book"),
  ]},
 {"n": "Proof copy", "a": "uncorrected proof · advance reading copy · ARC · bound galley", "d": "Pre-publication copy issued for review before final corrections, usually in paper covers.",
  "t": ["uncorrected proof", "advance reading copy", "bound galley", "unbound galleys"],
  "s": W + "Galley_proof"},
]
brands = []
def B(n, c, f, seg, kf, d, s, **kw):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "s": s}; b.update(kw); brands.append(b)
B("Kelmscott Press", "United Kingdom", "1891", "Artisan & independent", "private press", "William Morris and Emery Walker's Hammersmith press, closed 1898.", W + "Kelmscott_Press", sig=["Kelmscott Press book"], rel=["Doves Press", "Essex House Press"])
B("Doves Press", "United Kingdom", "1900", "Artisan & independent", "private press", "Hammersmith press of T. J. Cobden-Sanderson and Emery Walker, known for the Doves Type.", W + "Doves_Press", sig=["Doves Press book"], rel=["Doves Bindery", "Kelmscott Press"])
B("Ashendene Press", "United Kingdom", "1895", "Artisan & independent", "private press", "St John Hornby's press in Chelsea, 1895–1935.", W + "Ashendene_Press", sig=["Ashendene Press book"])
B("Essex House Press", "United Kingdom", "1898", "Artisan & independent", "private press", "C. R. Ashbee's Guild of Handicraft press, 1898–1910.", W + "Essex_House_Press", sig=["Essex House Press book"], rel=["Kelmscott Press"])
B("Cranach Presse", "Germany", "1913", "Artisan & independent", "private press", "Harry Graf Kessler's Weimar private press.", "https://specialcollections-blog.lib.cam.ac.uk/?p=8365", sig=["Cranach Presse book"])
B("Golden Cockerel Press", "United Kingdom", "1920", "Artisan & independent", "wood engravings", "English fine press, 1920–1961, at Waltham St Lawrence.", W + "Golden_Cockerel_Press", eras=["Hal Taylor, 1920–1924", "Robert Gibbings, 1924–1933", "Christopher Sandford, 1933–1959"], sig=["Golden Cockerel Press book"], rel=["Folio Society"])
B("Gregynog Press", "United Kingdom", "1922", "Artisan & independent", "private press", "Welsh press of Gwendoline and Margaret Davies at Gregynog Hall, revived as Gwasg Gregynog.", W + "Gregynog_Press", sig=["Gregynog Press book"])
B("Nonesuch Press", "United Kingdom", "1922", "Artisan & independent", "designed editions", "London press of Francis Meynell, Vera Mendel and David Garnett.", W + "Nonesuch_Press", sig=["Nonesuch Press book"], rel=["Limited Editions Club"])
B("Grabhorn Press", "United States", "1920", "Artisan & independent", "fine printing", "San Francisco press of Edwin and Robert Grabhorn.", W + "Grabhorn_Press", sig=["Grabhorn Press book"], rel=["Arion Press"])
B("Arion Press", "United States", "1974", "Artisan & independent", "letterpress", "Andrew Hoyem's San Francisco press, owner of the M&H Type foundry.", W + "Arion_Press", sig=["Arion Press book"], rel=["Grabhorn Press"])
B("Limited Editions Club", "United States", "1929", "Premium", "illustrated classics", "George Macy's subscription club for signed illustrated classics.", W + "Limited_Editions_Club", sig=["Limited Editions Club"], rel=["Heritage Press"])
B("Heritage Press", "United States", "1935", "Mainstream", "illustrated classics", "George Macy's lower-priced companion to the Limited Editions Club.", W + "Limited_Editions_Club", sig=["Heritage Press edition"], rel=["Limited Editions Club"])
B("Folio Society", "United Kingdom", "1947", "Premium", "illustrated editions", "London publisher of illustrated hardback editions, founded by Charles Ede.", W + "Folio_Society", sig=["Folio Society edition"])
B("Franklin Library", "United States", "1973", "Premium", "leather classics", "Publishing arm of the Franklin Mint, 1973–2000.", W + "Franklin_Mint", sig=["Franklin Library edition"], rel=["Easton Press"])
B("Easton Press", "United States", "1975", "Premium", "leather classics", "Norwalk, Connecticut maker of leather-bound books, part of MBI.", W + "Easton_Press", sig=["Easton Press edition"], rel=["Franklin Library"])
B("Subterranean Press", "United States", "1995", "Specialist", "genre limiteds", "Burton, Michigan publisher of signed limited genre editions.", W + "Subterranean_Press", sig=["Subterranean Press limited"])
B("Centipede Press", "United States", "2001", "Specialist", "horror limiteds", "Lakewood, Colorado publisher of luxury collector hardbacks, founded by Jerad Walters.", W + "Centipede_Press", sig=["Centipede Press edition"])
B("Suntup Editions", "United States", "2016", "Artisan & independent", "letterpress limiteds", "Southern California fine press publisher owned by Paul Suntup.", "https://www.finebooksmagazine.com/fine-books-news/suntup-editions-beautiful-stephen-king-books-prints", sig=["Suntup edition"])
B("Lyra's Books", "", "", "Artisan & independent", "leather limiteds", "Publisher of letterpress leather-bound lettered and numbered editions.", "https://www.collectiblebookvault.com/lyra/the-picture-of-dorian-gray-lettered", sig=["Lyra's Books edition"])
B("Riviere", "United Kingdom", "1829", "Heritage manufactory", "fine binding", "Bindery of Robert Riviere, Bath then London, later Riviere & Son.", W + "Robert_Riviere", sig=["Riviere binding"], rel=["Bayntun-Riviere"])
B("Zaehnsdorf", "United Kingdom", "1844", "Heritage manufactory", "fine binding", "London bindery founded by Joseph Zaehnsdorf, merged with Sangorski & Sutcliffe in 1988.", W + "Zaehnsdorf", sig=["Zaehnsdorf binding"], rel=["Sangorski & Sutcliffe"])
B("Doves Bindery", "United Kingdom", "1893", "Artisan & independent", "Arts and Crafts binding", "T. J. Cobden-Sanderson's Hammersmith bindery.", W + "T._J._Cobden-Sanderson", sig=["Doves Bindery binding"], rel=["Doves Press"])
B("Bayntun-Riviere", "United Kingdom", "1894", "Heritage manufactory", "fine binding", "Family-run Bath bindery founded by George Bayntun, joined with Riviere in 1939.", "https://georgebayntun.com/about-us", sig=["Bayntun binding"], rel=["Riviere"])
B("Sangorski & Sutcliffe", "United Kingdom", "1901", "Heritage manufactory", "jewelled bindings", "London bindery of Francis Sangorski and George Sutcliffe, owned by Shepherds since 1998.", W + "Sangorski_&_Sutcliffe", sig=["Sangorski & Sutcliffe binding"], rel=["Zaehnsdorf"])
B("Akademische Druck- u. Verlagsanstalt", "Austria", "", "Specialist", "codex facsimiles", "Graz facsimile publisher (ADEVA) known for Mesoamerican codices.", "http://www.famsi.org/research/graz/", sig=["ADEVA facsimile"])
B("Faksimile Verlag", "Switzerland", "1974", "Specialist", "manuscript facsimiles", "Lucerne publisher of illuminated-manuscript facsimiles.", "https://www.facsimilefinder.com/articles/treasures-of-the-past", sig=["Faksimile Verlag facsimile"])
B("M. Moleiro Editor", "Spain", "1991", "Specialist", "manuscript facsimiles", "Barcelona facsimile publisher founded by Manuel Moleiro.", W + "M._Moleiro_Editor", sig=["Moleiro facsimile"])
traditions = [
 {"n": "Arts and Crafts private press movement", "g": "Books & paper", "r": "England, then Germany and the United States", "p": "1891–1930s",
  "d": "Revival of hand-set, hand-printed books with designed types, handmade paper and wood engravings, begun by William Morris.",
  "tech": "hand composition, hand-press printing, wood engraving", "mat": "handmade paper, vellum, proprietary types",
  "forms": ["Private press book"], "ctr": ["Kelmscott Press", "Doves Press", "Essex House Press", "Ashendene Press", "Cranach Presse", "Golden Cockerel Press", "Gregynog Press"],
  "auth": "press colophon, edition statement, proprietary typeface, handmade paper watermark", "s": PP},
 {"n": "Western fine bookbinding", "g": "Books & paper", "r": "Europe", "p": "15th century–present",
  "d": "Hand binding in full or half leather with gold and blind tooling, from trade fine binderies to unique designer bindings.",
  "tech": "sewing on cords, rounding and backing, sewn headbands, gold and blind tooling", "mat": "goatskin, calf, gold leaf, marbled paper",
  "forms": ["Fine binding"], "ctr": ["Riviere", "Zaehnsdorf", "Doves Bindery", "Bayntun-Riviere", "Sangorski & Sutcliffe", "Paul Bonet"],
  "auth": "binder's stamp inside the front cover, quality of tooling and materials", "s": W + "Bookbinding"},
 {"n": "Paper marbling (ebru and suminagashi)", "g": "Books & paper", "r": "Japan; Iran, Central Asia, Ottoman Empire, Mughal India; later Europe", "p": "12th century (suminagashi); late 15th century onward (ebru)",
  "d": "Colours floated on water or a size are patterned and lifted onto paper, giving unique sheets used for endpapers, covers and edges.",
  "tech": "floating colours, combing and raking, laying paper on the bath", "mat": "gum tragacanth or carrageenan size, pigments, ox gall, kozo paper",
  "forms": ["Fine binding"], "ctr": ["Kyoto and Echizen", "Istanbul (Özbekler Tekkesi)", "Herat, Samarqand, Bukhara"],
  "auth": "each sheet a unique monotype; pattern style and size material fit period", "s": W + "Paper_marbling"},
]
notes = ("All eight planned new kinds built. Private presses ordered as in the brief. Easton, Franklin, Heritage and LEC from retrieved pages; "
         "Franklin Library founding/closing from the Franklin Mint article. Suntup founding given as late 2016 (operations from 2017). "
         "Lyra's Books country and founding not on retrieved page, left blank. ADEVA founding year not retrieved. Paul Bonet, Ed Ruscha, Dieter Roth, "
         "William Pickering, David Bryce and Son and HarperCollins are mk names without register entries. No book titles used as archetypes.")
out = {"kinds": kinds, "brands": brands, "traditions": traditions, "notes": notes}
p = '/home/user/Possession-Taxonomy/rebuild/work/F1/shelves/00_02.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
