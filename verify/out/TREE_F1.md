# F1 Media & Publications: decided tree

Category: F1 Media & Publications (domain F, Culture, Records & Meaning). Membership test (placement key step 21): a published work fixed on a physical carrier, made to be read, viewed or listened to: books (including religious texts, colouring, puzzle and activity books, braille and large-print books), comics, magazines, maps, atlases and globes, sheet music, records, CDs, tapes, films and discs, and other recording carriers of any format; blank recording media and carriers the owner has recorded with published music or film (mixtapes) are F1 too; parts made for one carrier follow it here (S3). Not here: video games on any carrier (D5), software on a carrier (I1), works held only as files or entitlements, e-books and audiobook files (I2), home recordings on a physical carrier and kept ephemera (F5), posters and art prints (F2), calendars and blank staff paper (C5), tarot and oracle decks and ritual scrolls (F4), players, decks and projectors (D3), DJ equipment and timecode vinyl (E3), unexposed film stock (D4), snow globes (B4), working astronomical instruments (C6), and albums, binders, boxes, crates and shelves that hold several carriers (B1 when empty). Structure (Candidate A, decided; memo sections 3, 4b, 10, 12 and 14): sub-family by the physical carrier family the work is fixed on (F1.1 to F1.4), then the closing parts sub-family F1.5 (C5(d), CV-17, exempt from that axis; leaf axis: the object served), then leaf by the form in which the carrier is issued or read (nineteen leaves; the three cartographic leaves are kept although C5(b) would allow `leaf = null`), then kind (the format class, one stated kind axis per leaf, at the level where buyers compare quality or makers), then named form (edition design, line or maker model, uncapped, `maker_bound` flagged; not listed here). Genre, subject and content never divide F1; edition, printing, pressing, condition, region, era, trim class (ONIX list 175), paper class, binding material, antiquarian height class, page format, record diameter, speed, release type, weight (`weight_g`), `mastering` (direct-to-disc, all-analog, half-speed), `pressing_material` (SHM-CD, Blu-spec CD2, HQCD), `encoding` (HDCD, SACD hybrid), fidelity specs, cassette tape type, `content_type` (music, spoken word, audiobook, other sound), instrumentation, level, urtext, globe body, diameter, illumination, relief, `bar_cabinet`, map and atlas scope, packaging (Steelbook), video region code, set size (`unit`) and price band are attributes, tags, C13 platform rows or views, never kinds or leaves; release and copy facts (first edition, first printing, sealed, low serial number, domestic or import pressing of one release) are not stored (section 14). Tier is a C4 tier entry on named forms and lines (the CBR premium comics lines, F-9), never on a kind. Maker role (maker_roles.tsv, provisional): owner for the whole category; publishers, imprints, record labels, cartographic houses and globe makers enter through lines and named forms, never titles (F1-O1); pressing plants are maker rows of class supplier tied to labels by "OEM (builds for)" relations (section 14). Display groups (navigation proposal, display only, never moving a home; no group ids issued): Books (F1.1.1); Comics and manga (F1.1.2); Magazines, newspapers and zines (F1.1.3); Sheet music (F1.1.4); Maps, atlases and globes (F1.2, shown as three level-2 groups); Vinyl and other records (F1.3.1); Cassettes and tapes (F1.3.2); CDs and other audio discs (F1.3.3, with F1.3.4 shown inside it); Films and video (F1.4, its three leaves as level-2 groups); Sleeves, jackets and cases for one item (F1.5); plus a labels and imprints side tab and generated views (audiophile pressings, collectible books, Japanese formats, audiobooks from `content_type`). Quality markers (display, judged on the edition, named form, line or maker, never on the kind): collectible books by edition and printing, then condition on the book condition scale (registry row owed), then contemporary binding, completeness, quality of printing and binding, illustration and rarity; new books by binding class (hardback, then trade paperback, then mass-market, as `binding` and `paper_class` values); records by mastering and source (D2D, all-analog, UHQR, audiophile reissue label), then pressing plant, then weight (200 g, 180 g, then 140-150 g), then speed (45 rpm audiophile cut over 33 1/3), then condition of disc and jacket each on the Goldmine scale; audio discs by format spec (SACD and DVD-Audio, then HDCD, then CD 16-bit/44.1 kHz) and pressing material, then condition; video discs by resolution format (Ultra HD Blu-ray, then Blu-ray, then DVD; provisional), then packaging and region code; comics by the edition ladder (premium large format, omnibus, hardcover, trade, single issue; CBR S12) and then condition. Pending kinds: the memo marks 14 kinds † (F1.1.1.08, F1.1.3.04, F1.2.3.03, F1.3.1.02, F1.3.1.04, F1.3.4.01 and the eight F1.5 kinds) (no fetched page names them, or only one does); their ids are allocated here in memo order, each line ending in †, and a † kind enters the data only when a fetched page attests it. Leaf F1.3.4 and all five F1.5 leaves hold only † kinds and are provisional with them. Provisional levels: transcription disc F1.3.1.05 and Mini-CD F1.3.3.04 are kinds under the size-against-format rule (C6, CV-19, F-6) only if fetched sellers list them apart, else they become a `diameter` value of F1.3.1.01 and F1.3.3.01; every F1 call is provisional because the major retailers were blocked (section 14). Carriers and forms the memo lists as "also attested, enter at harvest" or "held out of the tree" are not kinds yet and have no id; each leaf names them, and at the harvest each takes the next free number under its leaf (R-58).

Ids (R-58): F1.n is a sub-family and F1.n.m a leaf; a kind is F1.n.m.kk, or F1.n.kk where a sub-family has no leaf.

## F1.1 Printed volumes and serials
Leaf axis: the form in which the printed carrier is issued or read (book, comic or manga edition, periodical, printed music).

### F1.1.1 Books
Kind axis: binding class. Display group: Books. Trim class (ONIX B101 to B114, bunko B111 and shinsho B112 included), `paper_class`, `format_size` (folio to sextodecimo) and binding material are attributes. Enter at harvest (no id yet): fold-out book (ONIX BO), part-work (BN), novelty book (BK).
- F1.1.1.01 Hardback book: book bound in rigid boards (ONIX BB, trade cloth, relié); `binding` (trade cloth, library or reinforced binding, leather or fine binding) and `format_size` are attributes.
- F1.1.1.02 Paperback book: book bound in a flexible paper cover (ONIX BC, broché, poche), trade and mass-market alike; `trim_class` and `paper_class` are attributes.
- F1.1.1.03 Spiral-bound book: book whose leaves are held by a wire or plastic spiral or comb (ONIX BE).
- F1.1.1.04 Loose-leaf book: book issued as punched loose leaves held in a ring binder or post binding (ONIX BD).
- F1.1.1.05 Pamphlet or booklet, stapled: short publication of a few sheets bound by staples or saddle-stitching (ONIX BF).
- F1.1.1.06 Board book: book printed on thick laminated paperboard pages, made for young children (ONIX BH).
- F1.1.1.07 Rag, bath or foam book: book with pages of cloth, waterproof plastic or foam, made for babies (ONIX BI, BJ, BP).
- F1.1.1.08 Sewing or knitting pattern (paper): printed single-pattern sheet or envelope for sewing or knitting, issued as a loose sheet rather than bound (R-42; memo kind 7a; provisional until attested); craft, size range and garment made are attributes. †

### F1.1.2 Comic and manga editions
Kind axis: edition form. Display group: Comics and manga. Tankōbon, wide-ban, bunkoban, kanzenban, gōka aizōban, sōshūhen, the bande dessinée album and the publishers' lines are named forms.
- F1.1.2.01 Single-issue comic: saddle-stitched comic issue of one serial number (the "floppy"; ONIX pamphlet).
- F1.1.2.02 Collected softcover volume: softcover volume collecting several issues or chapters of a comic or manga (trade paperback, tankōbon; label_source: memo).
- F1.1.2.03 Collected hardcover volume: hardcover volume collecting several issues or chapters (label_source: memo).
- F1.1.2.04 Omnibus or compendium: thick single volume collecting a long run of issues or several collected volumes; `binding` is an attribute.
- F1.1.2.05 Pocket-size reissue: small-format reprint edition of a comic or manga already issued in collected volumes (bunkoban; label_source: memo).
- F1.1.2.06 Premium large-format edition: oversized deluxe edition on large trim and heavier paper (Absolute, kanzenban; label_source: memo).

### F1.1.3 Periodicals and newspapers
Kind axis: periodical form. Display group: Magazines, newspapers and zines. `page_format` (broadsheet, Berliner, tabloid, journal size, digest, A5, B5) is an attribute; single and back issues are individual items. Held out of the tree until a page is fetched (no id): mook or bookazine.
- F1.1.3.01 Newspaper: periodical issued daily or weekly on unbound newsprint sheets; `page_format` (broadsheet, Berliner, tabloid) is an attribute.
- F1.1.3.02 Magazine: periodical issue bound as a stapled or perfect-bound paper-covered booklet, digest-size magazines included; `page_format` is an attribute.
- F1.1.3.03 Bound periodical volume: book-form volume binding together a run of issues of one periodical (filed with periodicals against HS, F-8).
- F1.1.3.04 Zine or fanzine: small self-published or fan-made periodical, usually photocopied or short-run and stapled. †

### F1.1.4 Printed music
Kind axis: completeness of the notation. Display group: Sheet music. Instrumentation, level, urtext and facsimile are attributes; method and tutor books are books (F1-O2). Enter at harvest (no id yet): piano reduction, single part. Held out of the tree until a page is fetched (no id): fake book (filed meanwhile as F1.1.4.07 with `notation = lead sheet`).
- F1.1.4.01 Full score: printed score showing every part of an ensemble work on the page at full size.
- F1.1.4.02 Miniature (study) score: full score reduced to pocket size for study (pocket score, Studienpartitur).
- F1.1.4.03 Vocal or piano-vocal score: score with the vocal parts in full and the accompaniment reduced for piano.
- F1.1.4.04 Score and parts: score issued together with the separate parts for each performer.
- F1.1.4.05 Set of parts: the separate performers' parts of a work issued without the score.
- F1.1.4.06 Choral octavo: single choral work printed in octavo format for choir use.
- F1.1.4.07 Songbook or collection: bound collection of songs or pieces, in notation for voice, piano or another instrument, lead-sheet books included.

## F1.2 Cartographic items
Leaf axis: the form in which the cartographic carrier is issued (sheet map, bound atlas, globe). `scope` (reference, road, street, walking, cycling, thematic), map style, series and region are attributes or named forms.

### F1.2.1 Maps
Kind axis: physical form. Display group: Maps, atlases and globes (level-2 group Maps). Enter at harvest (no id yet): tear-off map pad, custom map.
- F1.2.1.01 Folded map: printed map sheet folded to pocket size for carrying; `scope` is an attribute.
- F1.2.1.02 Wall map: map printed or mounted to hang flat on a wall, laminated or not.
- F1.2.1.03 Map booklet: map issued as a small stapled or bound booklet of map sections.

### F1.2.2 Atlases
Kind axis: binding. Display group: Maps, atlases and globes (level-2 group Atlases).
- F1.2.2.01 Bound atlas, hard or soft cover: book of maps bound in boards, a flexible cover or flexi-binding; `scope` is an attribute.
- F1.2.2.02 Spiral-bound atlas: book of maps held by a wire or plastic spiral so it lies flat (road atlases).

### F1.2.3 Globes
Kind axis: mount. Display group: Maps, atlases and globes (level-2 group Globes). `body` (terrestrial, celestial, lunar, planetary), `map_style`, `illuminated`, `relief`, diameter and `bar_cabinet` are attributes of all globes.
- F1.2.3.01 Desktop globe: globe on a short base or stand made to sit on a desk or table, mini globes included.
- F1.2.3.02 Floor globe: globe on a tall floor-standing stand or frame.
- F1.2.3.03 Hanging or suspended globe: globe made to hang from a ceiling or bracket. †

## F1.3 Sound carriers
Leaf axis: the recording technology of the carrier (grooved disc or cylinder, magnetic tape, optical disc, solid-state device). `content_type` (music, spoken word, audiobook, other sound) is an attribute of every sound kind; there is no audiobook kind (F-8).

### F1.3.1 Grooved discs and cylinders
Kind axis: groove standard, which decides the stylus and the deck. Display group: Vinyl and other records. `diameter`, `speed`, `release_type`, `weight_g`, `mastering`, colour and pressing are attributes. Enter at harvest (no id yet): Edison Disc, Pathé Disc, Mighty Tiny, Sopic.
- F1.3.1.01 Microgroove record: vinyl disc with fine grooves played with a microgroove stylus at 33 1/3, 45 or another speed (LP, EP, single); `diameter`, `speed`, `release_type`, `weight_g` and `mastering` are attributes.
- F1.3.1.02 Coarse-groove (78 rpm) record: shellac or early disc with wide grooves played at about 78 rpm with a coarse stylus (memo † on the term "coarse-groove" only; the 78 rpm shellac disc is attested). †
- F1.3.1.03 Flexi-disc: thin flexible vinyl sheet record, often bound into magazines.
- F1.3.1.04 Instantaneous disc, acetate or lathe cut: disc cut one at a time on a recording lathe, as an acetate or lacquer, not pressed. †
- F1.3.1.05 Transcription disc, 16 inch: 16-inch disc made for broadcast playback on a transcription deck (provisional under F-6: if no seller lists it apart, it is F1.3.1.01 with `diameter` 16 in).
- F1.3.1.06 Cylinder record: sound recorded in the groove of a cylinder (wax or celluloid) for a phonograph.

### F1.3.2 Magnetic tape (audio)
Kind axis: tape system. Display group: Cassettes and tapes. `tape_type` (IEC I to IV) is an attribute. Enter at harvest (no id yet): Elcaset, DAT, DCC, ADAT, DTRS, open-reel tape, 8-track cartridge.
- F1.3.2.01 Compact cassette: audio tape in the standard two-hub compact cassette shell, pre-recorded or blank; `tape_type` is an attribute.
- F1.3.2.02 Microcassette family: audio tape in a cassette smaller than the compact cassette (microcassette, minicassette, picocassette; label_source: memo).

### F1.3.3 Optical audio discs
Kind axis: disc system. Display group: CDs and other audio discs. `encoding`, `pressing_material`, `bit_depth`, `sample_rate` and `hybrid` are attributes. Enter at harvest (no id yet): CDr, MiniDisc.
- F1.3.3.01 Compact disc, 12 cm: 12 cm optical disc in the Compact Disc Digital Audio system (16-bit, 44.1 kHz), audiobook CDs included; `encoding` (HDCD) and `pressing_material` (SHM-CD, Blu-spec CD2, HQCD) are attributes.
- F1.3.3.02 SACD: Super Audio CD carrying DSD audio, single-layer or hybrid with a CD layer; `hybrid` is an attribute.
- F1.3.3.03 DVD-Audio: DVD-format disc carrying high-resolution audio (up to 24-bit/192 kHz).
- F1.3.3.04 Mini-CD, 3 inch: 8 cm compact disc needing a tray recess or adapter (provisional under F-6: if no seller lists it apart, it is F1.3.3.01 with `diameter` 3 in).

### F1.3.4 Solid-state sound carriers
Kind axis: device type (a carrier that holds one work fixed on it and plays it). Display group: CDs and other audio discs (display move). A player that plays any loaded content is D3.
- F1.3.4.01 Pre-recorded digital audio player: self-contained device sold with one work (usually an audiobook) fixed on it and able to play only that work (Playaway type; ONIX AK). †

## F1.4 Moving-image carriers
Leaf axis: the recording technology of the carrier (videotape, video disc, motion-picture film). Video region codes are C13 platform rows (DVD regions, Blu-ray A to C); Steelbook packaging is an attribute.

### F1.4.1 Videotape
Kind axis: tape system. Display group: Films and video (level-2 group videotape). Enter at harvest (no id yet): S-VHS, Video 2000, Video8, U-matic, MiniDV, Cartrivision.
- F1.4.1.01 VHS cassette: video recording on half-inch tape in a VHS cassette.
- F1.4.1.02 Betamax cassette: video recording on half-inch tape in a Betamax cassette.

### F1.4.2 Video discs
Kind axis: disc system. Display group: Films and video (level-2 group video discs). Enter at harvest (no id yet): VCD, SVCD, HD DVD, UMD video, CED SelectaVision, VHD, CDV.
- F1.4.2.01 LaserDisc: 30 cm (or 20 cm) optical disc carrying analogue video.
- F1.4.2.02 DVD: 12 cm optical disc carrying standard-definition digital video.
- F1.4.2.03 Blu-ray: 12 cm optical disc in the Blu-ray system carrying high-definition video.
- F1.4.2.04 Ultra HD Blu-ray: 12 cm optical disc in the Ultra HD Blu-ray system, listed apart from Blu-ray.

### F1.4.3 Motion-picture film
Kind axis: gauge, which fixes the projector (C6, CV-19). Display group: Films and video (level-2 group film prints). Sound, base and colour are attributes. Enter at harvest (no id yet): regular 8 mm, 9.5 mm, 28 mm.
- F1.4.3.01 35 mm print: commercially released film print on 35 mm stock.
- F1.4.3.02 16 mm print: commercially released film print on 16 mm stock.
- F1.4.3.03 Super 8 print: commercially released film print on Super 8 stock.

## F1.5 Parts and accessories made for one carrier
Leaf axis: the object served (book, comic, record, disc, globe). Exempt from the level-1 axis (C5(d), CV-17). Display group: Sleeves, jackets and cases for one item. All kinds are † (no fetched page names them). Holders made for several carriers are B1.

### F1.5.1 Book parts
- F1.5.1.01 Dust jacket sold alone: loose paper wrapper made to cover one hardback book, sold apart from the book. †
- F1.5.1.02 Slipcase: open-ended box made to hold and protect one book or one set issued together. †

### F1.5.2 Comic parts
- F1.5.2.01 Comic bag: clear plastic bag sized to hold one comic issue. †
- F1.5.2.02 Backing board: stiff board placed behind one comic in its bag to keep it flat. †

### F1.5.3 Record parts
- F1.5.3.01 Record inner sleeve: paper or poly sleeve that holds one record disc inside its jacket. †
- F1.5.3.02 Record outer sleeve: clear protective sleeve made to cover one record jacket. †

### F1.5.4 Disc parts
- F1.5.4.01 CD jewel case: hinged plastic case made to hold one compact disc with its booklet and tray card. †

### F1.5.5 Globe parts
- F1.5.5.01 Globe stand or meridian: stand, cradle or meridian ring sold for one globe. †

## Precedence inside F1

- One home per object: a named form, line, variant or edition is a ledger row under one kind and never a second home; genre, subject and content type never decide a home.
- A comic or manga volume is filed in F1.1.2 whatever its binding or trim; F1.1.1 holds books that are not comics. The single-issue comic (F1.1.2.01) is filed with comics, with a cross-reference to periodicals, because it is a staple-bound serial issue.
- The bound volume of a magazine is a bound periodical volume (F1.1.3.03) and stays with its issues, against HS, which sends it to books (F-8).
- Bunko and shinsho are `trim_class` values of the paperback book (F1.1.1.02), not kinds or named forms; trade and mass-market paperbacks are one kind with `paper_class` (F-7). Tankōbon, bunkoban, kanzenban and the bande dessinée album are named forms under the generic comic edition kinds (F1.1.2.02, F1.1.2.05, F1.1.2.06, F1.1.2.03; C11).
- A pattern book is a book by its binding (F1.1.1.01 to F1.1.1.04); a single-pattern sheet or envelope is F1.1.1.08; a PDF pattern is I2 (R-42, C4-O1). Method and tutor books are books, not printed music (F1-O2). A fake book is filed as a songbook or collection (F1.1.4.07) with `notation = lead sheet` until it is attested.
- An audiobook is filed by its carrier: an audiobook on CD is a compact disc (F1.3.3.01) with `content_type` spoken word or audiobook; a Playaway-type player is F1.3.4.01; an audiobook held only as a file is I2 (F-8, I-10).
- Record diameter, speed and release type never make a kind: a 7-inch single and a 12-inch LP are both microgroove records (F1.3.1.01). The 16-inch transcription disc (F1.3.1.05) and the 3-inch Mini-CD (F1.3.3.04) are kinds only because they need a different deck or tray, and fall back to a `diameter` value if sellers do not list them apart (CV-19, F-6). Japanese CD sub-formats (SHM-CD, Blu-spec CD2, HQCD) are `pressing_material` values of the compact disc (F1.3.3.01); UHQR and other audiophile reissue series of one carrier are maker-bound named forms of the microgroove record, and a series that spans vinyl and SACD is a lines row (section 14).
- A globe that opens as a drinks cabinet is a globe (F1.2.3) with the attribute `bar_cabinet` (F-8); a mini globe is a desktop globe (F1.2.3.01) with a diameter value.
- A set of like carriers is filed as that carrier with a `unit` attribute (a three-LP box set is F1.3.1.01, unit 3); a mixed multi-carrier pack (Blu-ray plus DVD, a book with a CD, a VinylDisc) is filed once by its item of greatest value, normally its primary carrier, with its contents listed; no set is a kind (S3a, K-1).
- A holder, case, sleeve or stand made for one carrier follows it into F1.5 (a stand sold for one globe is F1.5.5.01); an album, binder, box, crate or shelf made to hold several carriers is B1 when empty, a filled photo album or scrapbook F5 and a blank scrapbook album C4 (S3, K-9).
- Boundaries that bound these kinds: a disc or cartridge made to run a video game is D5 and a disc of software I1, while an enhanced CD published as a music release stays F1; a work held only as a file or entitlement is I2 and a digital audio player that plays any loaded content D3; a film reel, tape or disc shot or recorded by the owner or family is F5, a commercially released print (F1.4.3) or a mixtape made from published music or film is F1, and kept programmes and postcards are F5; a published art book is F1, a poster F2, a calendar or blank staff paper C5, a map (F1.2.1), a single atlas sheet or a pictorial wall map F1 and a print made as art that depicts a place F2; a record player or deck is D3 and DJ equipment including timecode vinyl E3; a snow globe is B4; a published celestial globe or star chart is F1 and a telescope or working astronomical instrument C6; blank recording media are F1 and unexposed film stock D4; a tarot, oracle or Lenormand deck is F4 and a pack made for card play E1; a printed religious text is F1 and a scroll made for use in a rite F4.
