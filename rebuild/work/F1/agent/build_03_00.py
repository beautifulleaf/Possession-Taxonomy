import json, os
W = 'https://en.wikipedia.org/wiki/'
K = 'knowledge'
def X(n, d, mk, y, s, v=(), a="", dt=""):
    return {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [dict(zip(("n", "mk", "y", "d"), t)) for t in v], "dt": dt}
MM = W + 'Marvel_Masterworks'; DCA = W + 'DC_Archive_Editions'; AE = W + 'Artist%27s_Edition'; DCL = W + 'List_of_DC_Comics_reprint_collections'
MO = W + 'Marvel_Omnibus'; EPIC = W + 'Marvel_Epic_Collection'; ABS = 'https://biffbampop.com/2009/03/02/reading-the-watchmen-japer-contemplates-the-absolute-version-of-the-seminal-story/'
TK = W + 'Tank%C5%8Dbon'; JUMP = W + 'Jump_(magazine_line)'; DJ = W + 'Doujinshi'; WSM = W + 'Weekly_Sh%C5%8Dnen_Magazine'
CGC = W + 'Certified_Guaranty_Company'; BD = 'https://centerforbookarts.org/exhibitions/from-bande-dessinee-to-artists-book-testing-the-limits-of-franco-belgian-comics'
CMP = 'https://gocollect.com/index.php/blog/image-comics-reprints-the-walking-dead-compendium-vol-1'
CBR = 'https://www.cbr.com/comic-format-reading-guide'
kinds = [
 {"n": "Single-issue comic", "a": "floppy · comic book", "d": "Comic issue of one serial number, stapled through the fold (the \"floppy\").",
  "t": ["first printing", "later printing", "cover variant (incentive, retailer, sketch, virgin)", "newsstand or direct edition", "signed", "raw (ungraded)",
        "CGC graded slab (0.5–10)", "CGC Universal (blue label)", "CGC Signature Series (yellow label)", "CGC Qualified (green label)", "CGC Restored (purple label)", "bagged and boarded"],
  "s": CBR,
  "x": [
   X("CGC-graded comic", "Single issue graded on a 0.5–10 scale and sonically sealed in a tamper-evident holder with a colour-coded label.", "Certified Guaranty Company", "2000", CGC,
     [("Universal", "Certified Guaranty Company", "", "blue label, unrestored"), ("Signature Series", "Certified Guaranty Company", "", "yellow label, signature witnessed by CGC"),
      ("Qualified", "Certified Guaranty Company", "", "green label, significant defect or unwitnessed signature"), ("Restored", "Certified Guaranty Company", "", "purple label"),
      ("Conserved", "Certified Guaranty Company", "", "blue/purple label, structural repairs")],
     a="slab · slabbed comic", dt="grade · label colour · page quality"),
  ]},
 {"n": "Collected softcover volume", "a": "trade paperback · TPB · tankōbon", "d": "Softcover volume collecting several issues or chapters of a comic or manga.",
  "t": ["B6 tankōbon", "A5 tankōbon", "wide-ban (A5)", "shinsōban (new-cover edition)", "first printing", "obi strip", "colour", "black and white"],
  "s": CBR,
  "x": [
   X("Jump Comics", "Shueisha's main tankōbon imprint for series from Weekly Shōnen Jump and the other Jump magazines.", "Shueisha", "", JUMP,
     [("Jump Comics", "Shueisha", "", "standard tankōbon"), ("Shonen Jump (English edition)", "Viz Media", "2003", "US imprint of the Jump line")], dt="volume number · obi · printing"),
   X("Shōnen Magazine Comics", "Kodansha's tankōbon imprint for series from Weekly Shōnen Magazine.", "Kodansha", "", TK, [], a="KC", dt="volume number · obi"),
   X("Shōnen Sunday Comics", "Shogakukan's tankōbon imprint for series from Weekly Shōnen Sunday.", "Shogakukan", "", TK, [], dt="volume number · obi"),
   X("Shōnen Champion Comics", "Akita Shoten's tankōbon imprint for its Shōnen Champion series.", "Akita Shoten", "", TK, [], dt="volume number"),
   X("Marvel Epic Collection", "Marvel's numbered full-colour paperbacks collecting whole runs of a title, with spine colour by line.", "Marvel", "2013", EPIC,
     [("First volume", "Marvel", "2013", "September 2013, released out of numbered order")], a="Epic Collection", dt="volume number · spine colour · 288–528 pages"),
  ],
  "m": [["Marvel Essentials", "Marvel"], ["Marvel Premier Collection", "Marvel"], ["Marvel-Verse", "Marvel"], ["DC Showcase", "DC"], ["DC Compact Comics", "DC"], ["Kadokawa Comics Ace", "KADOKAWA"]]},
 {"n": "Collected hardcover volume", "a": "hardcover collection · HC", "d": "Hardcover volume collecting several issues or chapters of a comic.",
  "t": ["dust jacket", "variant dust jacket", "restored colour", "first printing", "later printing"],
  "s": CBR,
  "x": [
   X("Marvel Masterworks", "Marvel's premium hardcover reprints of classic runs, with restored art and era-coded dust jackets.", "Marvel", "1987", MM,
     [("Original series", "Marvel", "1987", "27 volumes to 1994, marble-look jackets"), ("Relaunch", "Marvel", "2003", "silver jackets; regular and limited marble-style variant jackets"),
      ("Golden Age Masterworks", "Marvel", "2004", "gold jackets, to 2012"), ("Atlas Era Masterworks", "Marvel", "2006", "red jackets, to 2013"),
      ("Masterworks trade paperbacks", "Marvel", "2009", "lower-priced softcovers, to 2015"), ("Mighty Marvel Masterworks", "Marvel", "2021", "smaller manga-sized softcovers, to 2025")],
     dt="volume number · jacket style · regular or variant · printing"),
   X("DC Archive Editions", "DC's hardcover reprints of early Golden and Silver Age series, with restored pages.", "DC", "1989", DCA,
     [("Launch volume", "DC", "1989", "US$39.95"), ("Later volumes", "DC", "2009", "US$59.99"), ("Final volume", "DC", "2014", "line succeeded by DC Omnibus")],
     a="DC Archives", dt="volume number · printing"),
   X("DC Deluxe Edition", "DC's oversized full-colour hardcover reprints of about 7.5 × 11 inches, thinner than an omnibus.", "DC", "", DCL, [], a="Deluxe Hardcover", dt="trim size · printing"),
  ]},
 {"n": "Omnibus", "a": "compendium · OHC", "d": "Thick single volume collecting a long run of issues or several collected volumes; the binding is noted.",
  "t": ["hardcover omnibus", "softcover compendium", "standard cover", "direct-market variant cover", "first printing", "later printing"],
  "s": CBR,
  "x": [
   X("Marvel Omnibus", "Marvel's large-format full-colour hardcovers of complete runs, often by one writer or artist.", "Marvel", "2005", MO,
     [("Precursor collection", "Marvel", "2004", "992-page Barnes & Noble exclusive, not branded omnibus"), ("First Omnibus", "Marvel", "2005", "848 pages, US$45"),
      ("Direct-market variant cover", "Marvel", "2005", "comic-shop-only covers")], dt="page count · standard or DM cover · printing"),
   X("DC Omnibus", "DC's thick hardcover reprint line that followed the Archive Editions.", "DC", "", DCA, [], dt="page count · printing"),
   X("Image compendium", "Image Comics' black-and-white softcover bricks of over a thousand pages collecting about 48 issues each.", "Image Comics", "2010", CMP,
     [("First compendium", "Image Comics", "2010", "1,088 pages, 48 issues, US$59.99")], dt="page count · printing"),
  ],
  "m": [["DC Finest", "DC"]]},
 {"n": "Premium large-format edition", "a": "Absolute · Artist's Edition · kanzenban", "d": "Oversized or deluxe edition on large trim and heavier paper, often slipcased.",
  "t": ["slipcase", "oversized trim", "limited printing", "signed and numbered"],
  "s": CBR,
  "x": [
   X("DC Absolute Edition", "DC's oversized slipcased hardcovers with recoloured art and supplementary material.", "DC", "", ABS,
     [("Absolute Edition", "DC", "2005", "black slipcase, about 8.5 × 12.5 inches")], a="Absolute", dt="slipcase · trim · printing"),
   X("Artist's Edition", "Same-size reproductions of original comic art, scanned in colour but printed to show pasteovers and blue pencil.", "IDW Publishing", "2010", AE,
     [("Artist's Edition", "IDW Publishing", "2010", "usually 12 × 17 inches, some 14 × 20 or 15 × 22"), ("Artifact Edition", "IDW Publishing", "2014", "selected pages, to 2020"),
      ("Artist's Edition Portfolio", "IDW Publishing", "", "loose pages in a hardcover folder"), ("Studio Edition", "Fantagraphics", "", "Fantagraphics' equivalent"),
      ("Gallery Edition", "Dark Horse Comics", "", "Dark Horse's equivalent"), ("Art Edition", "Dynamite Entertainment", "", "Dynamite's equivalent")],
     dt="trim size · scanned from original art or not · printing"),
   X("Kanzenban", "Japanese 'complete edition' manga in A5, restoring chapter covers, colour pages and side stories.", "", "", TK, [], a="complete edition", dt="A5 · colour pages"),
   X("Aizōban", "Japanese collector's edition manga with special covers, better paper and slipcases, in limited runs.", "", "", TK,
     [("Gōka aizōban", "", "", "luxury collector's edition")], a="collector's edition", dt="slipcase · limited run"),
   X("Sōshūhen", "Shueisha's B5 compilation volumes collecting several tankōbon with bonus material.", "Shueisha", "2008", TK, [], dt="B5"),
  ],
  "m": [["DC Deluxe Hardcovers", "DC"], ["Dynamite Definitive Editions", "Dynamite Entertainment"], ["Atlas Artist Edition", "Fantagraphics"], ["Marvel Gallery Editions", "Marvel"]]},
 {"n": "Pocket-size reissue", "a": "bunkoban", "d": "Small-format reprint of a comic or manga already issued in collected volumes, with more pages per volume.",
  "t": ["A6 bunko", "new cover", "fewer, thicker volumes"], "s": TK,
  "x": [
   X("Bunkoban", "A6 paperback manga reissue, thicker than a tankōbon and often with a new cover.", "", "", TK,
     [("Shueisha Comic Bunko", "Shueisha", "", "Shueisha's bunkoban imprint")], dt="A6 · volume count")]},
 {"n": "Bande dessinée album", "a": "BD album · comic album", "d": "Franco-Belgian comic book in the album format, typically 48 colour pages in a hard cover of about 11.5 × 8 inches.",
  "t": ["hardcover (cartonné)", "softcover (broché)", "48 pages", "first edition (édition originale)", "later printing", "tirage de tête (deluxe limited)", "intégrale (omnibus)"],
  "s": BD,
  "x": [
   X("Standard 48-page album", "The dominant Franco-Belgian format: 48 colour pages in a hard cover, numbered within its series.", "", "", BD, [],
     a="48CC", dt="publisher · album number · printing · cover")],
  "m": [["Album (bande dessinée)", ""]]},
 {"n": "Manga anthology magazine", "a": "manga magazine · phonebook manga", "d": "Thick weekly or monthly manga anthology on cheap newsprint, carrying chapters of many series; treated as disposable.",
  "t": ["weekly", "monthly", "special or combined issue", "with furoku (bonus gift)"], "s": TK,
  "x": [
   X("Weekly Shōnen Jump", "Shueisha's weekly boys' manga anthology, flagship of the Jump magazine line.", "Shueisha", "1968", JUMP,
     [("Shōnen Jump", "Shueisha", "1968", "original name"), ("Weekly Young Jump", "Shueisha", "1979", "seinen sister"), ("V Jump", "Shueisha", "1993", ""),
      ("Jump SQ.", "Shueisha", "2007", "replaced Monthly Shōnen Jump"), ("English edition", "Viz Media", "2003", "US edition")], dt="issue number · year"),
   X("Weekly Shōnen Magazine", "Kodansha's weekly boys' manga anthology, launched 17 March 1959.", "Kodansha", "1959", WSM,
     [("Combined issue with Weekly Shōnen Sunday", "Kodansha", "2008", "joint special issue of 19 March 2008")], dt="issue number · year"),
   X("Weekly Shōnen Sunday", "Shogakukan's weekly boys' manga anthology, launched just after its rival Weekly Shōnen Magazine.", "Shogakukan", "", WSM, [], dt="issue number · year"),
  ]},
 {"n": "Dōjinshi", "a": "doujinshi · fan comic", "d": "Self-published Japanese manga or magazine, often derivative fan work, sold mainly at events such as Comiket and specialist shops.",
  "t": ["original work", "parody (aniparo)", "adult (18-kin)", "circle-published", "bought at Comiket", "shop copy"], "s": DJ},
]
brands = [
 {"n": "Marvel", "c": "United States", "f": "1939", "seg": "Mainstream", "kf": "superhero comics", "d": "American comic publisher, founded as Timely Comics, with reprint lines from Masterworks to Omnibus.",
  "lines": ["Marvel Masterworks", "Marvel Omnibus", "Marvel Epic Collection", "Marvel Essentials"], "sig": ["Marvel Masterworks", "Marvel Omnibus", "Marvel Epic Collection"], "rel": ["DC"], "s": K},
 {"n": "DC", "c": "United States", "f": "1934", "seg": "Mainstream", "kf": "superhero comics", "d": "American comic publisher with Archive, Absolute, Deluxe and Omnibus reprint lines.",
  "lines": ["DC Archive Editions", "DC Absolute Edition", "DC Omnibus", "DC Finest", "DC Compact Comics", "Showcase Presents"], "sig": ["DC Archive Editions", "DC Absolute Edition"], "rel": ["Marvel"], "s": K},
 {"n": "IDW Publishing", "c": "United States", "f": "1999", "seg": "Specialist", "kf": "Artist's Editions", "d": "San Diego publisher that created the same-size Artist's Edition format in 2010.", "lines": ["Artist's Edition", "Artifact Edition"], "sig": ["Artist's Edition"], "s": AE},
 {"n": "Image Comics", "c": "United States", "f": "1992", "seg": "Mainstream", "kf": "creator-owned comics", "d": "Creator-owned American publisher known for thousand-page compendium paperbacks.", "sig": ["Image compendium"], "s": K},
 {"n": "Fantagraphics", "c": "United States", "f": "1976", "seg": "Artisan & independent", "kf": "alternative comics", "d": "Seattle publisher of alternative comics and classic strip reprints, including Studio Editions.", "s": K},
 {"n": "Dark Horse Comics", "c": "United States", "f": "1986", "seg": "Specialist", "kf": "licensed comics", "d": "Oregon publisher whose Gallery Editions reproduce original art.", "s": K},
 {"n": "Dynamite Entertainment", "c": "United States", "f": "2004", "seg": "Specialist", "kf": "licensed comics", "d": "New Jersey publisher with Art Editions and Definitive Editions.", "s": K},
 {"n": "Shueisha", "c": "Japan", "f": "1925", "seg": "Mainstream", "kf": "Jump manga", "d": "Tokyo publisher of the Jump magazine line and Jump Comics tankōbon.", "lines": ["Jump Comics", "Shueisha Comic Bunko", "Jump Remix"], "sig": ["Weekly Shōnen Jump", "Jump Comics"], "rel": ["Viz Media"], "s": JUMP},
 {"n": "Kodansha", "c": "Japan", "f": "1909", "seg": "Mainstream", "kf": "manga", "d": "Tokyo publisher of Weekly Shōnen Magazine and the Shōnen Magazine Comics imprint.", "sig": ["Weekly Shōnen Magazine", "Shōnen Magazine Comics"], "s": WSM},
 {"n": "Shogakukan", "c": "Japan", "f": "1922", "seg": "Mainstream", "kf": "manga", "d": "Tokyo publisher of Weekly Shōnen Sunday and the Shōnen Sunday Comics imprint.", "sig": ["Weekly Shōnen Sunday", "Shōnen Sunday Comics"], "s": K},
 {"n": "Akita Shoten", "c": "Japan", "f": "1948", "seg": "Mainstream", "kf": "manga", "d": "Tokyo publisher of Shōnen Champion and the Shōnen Champion Comics imprint.", "sig": ["Shōnen Champion Comics"], "s": K},
 {"n": "Viz Media", "c": "United States", "f": "", "seg": "Specialist", "kf": "manga in English", "d": "US publisher of the English Shonen Jump magazine and imprint.", "rel": ["Shueisha"], "s": JUMP},
 {"n": "Certified Guaranty Company", "c": "United States", "f": "2000", "seg": "Institution & issuer", "kf": "comic grading", "d": "Grading service that encapsulates comics in labelled slabs on a 0.5–10 scale.", "sig": ["CGC-graded comic"], "s": CGC},
 {"n": "Dupuis", "c": "Belgium", "f": "1922", "seg": "Mainstream", "kf": "bande dessinée", "d": "Belgian comics publisher of Franco-Belgian albums and a weekly comics magazine.", "s": K},
 {"n": "Casterman", "c": "Belgium", "f": "1780", "seg": "Heritage manufactory", "kf": "bande dessinée", "d": "Tournai publisher and printer, a long-standing publisher of bande dessinée albums.", "s": K},
 {"n": "Dargaud", "c": "France", "f": "1936", "seg": "Mainstream", "kf": "bande dessinée", "d": "French publisher of bande dessinée albums.", "s": K},
 {"n": "Le Lombard", "c": "Belgium", "f": "1946", "seg": "Mainstream", "kf": "bande dessinée", "d": "Brussels publisher founded by Raymond Leblanc, publisher of bande dessinée albums.", "s": K},
]
notes = ("All six old kinds kept; Bande dessinée album, Manga anthology magazine and Dōjinshi added. Collected-edition lines became archetypes (Masterworks, DC Archive, Deluxe, Epic Collection moved from Omnibus to softcover since it is a paperback line, Marvel/DC Omnibus, Image compendium, Absolute, Artist's Edition with Studio/Gallery/Art Edition equivalents, kanzenban, aizōban, sōshūhen, bunkoban); manga labels Jump Comics, Shōnen Magazine/Sunday/Champion Comics as archetypes. "
         "Kadokawa SKU labels trimmed to Kadokawa Comics Ace (Asuka, Beam, Bushiroad, Dengeki, Dragon Comics Age, Harta dropped); Marvel GN dropped as generic. Old 'Tankōbon', 'Wide-ban' models became t; Mighty Marvel Masterworks became a Masterworks version. "
         "Grading and variants went to t/dt plus a CGC archetype. No comic titles named. BD publishers are brand entries only (from knowledge) since no per-publisher album line was fetched.")
out = {"kinds": kinds, "brands": brands, "traditions": [], "notes": notes}
p = 'work/F1/shelves/03_00.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
