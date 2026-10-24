## F1

- Mastering (Acoustic Sounds filters D2D, all-analog, half-speed): **attribute** `mastering` on named forms of the microgroove record (memo kind 33). Values: direct-to-disc, all-analog, half-speed mastered. It goes on reissue-series named forms, never on a title (F1-O1). Weight is the attribute `weight_g` (display bands 140-150, 180 and 200 g). Speed and release_type stay as the memo has them.
- UHQR (Analogue Productions): **named_form**. It is a maker-bound named form of the microgroove record (maker Analogue Productions). It stays inside one kind, so it is not a line (C2(d)). The same rule covers audiophile reissue series of one carrier, such as the Mobile Fidelity series. If a series spans vinyl and SACD, it is a lines row. The named form carries `mastering` and `weight_g`. Its pressing by Quality Record Pressings is a maker-relations row (QRP "OEM (builds for)" Analogue Productions, scope UHQR).
- Pressing plant as a maker class: **other (ledger)**. No new `maker_class` is added. A pressing plant (QRP, RTI, Optimal and the like) is a maker row of class "supplier", tied to labels by "OEM (builds for)" relations. Shoppers who look for a plant by name reach it through the labels and imprints side tab.
- Disc and sleeve graded separately: **other (registry)**. The Goldmine scale is one grading_scales row whose notes say "components: media | sleeve". No `component` column is added. Disk Union's S to C grade is a second row, scale_type platform label.
- Japanese CD sub-formats (SHM-CD, Blu-spec CD2, HQCD): **attribute** `pressing_material` on the compact disc (C10: same disc, same player). They are not kinds. Encoding (HDCD, SACD hybrid) stays the attribute `encoding`.
- Audiobooks: **attribute** `content_type` on the carrier kinds (music, spoken word, audiobook, other sound). A generated "audiobooks" view is built from it (display only). No audiobook kind is made (F-8).
- eBooks and calendars on the same shop menus: **other_category**. eBooks go to I2 and calendars to C5, shown as cross-links only.
- Book condition scale and the ABAA/ILAB glossary: **need**. One registry row, condition grade (Fine to Poor), provisional until the glossary page is fetched. A comic and magazine grading row is also owed (PSA grades comics, F3 memo S21), provisional.
- Rare-book markers "primacy", "first books", first edition and first printing: **noted**. These are facts of a title or a printing, which F1 does not store. They appear only as guidance text in the "What makes the best" box. The proposed collectible-books view therefore has no stored subject: it shows guidance and named lines (fine press, Folio Society) only.
- Pressing origin (domestic or import), sealed, used, low serial number, Steelbook and video region of one release: **noted**. These are release or copy facts and are not stored. Region codes enter only as C13 platform rows (DVD regions 1-8, Blu-ray A to C), with compatibility to D3 players.
- Turntable guide: **other_category**, D3 evidence, not used for F1.
- Build display groups as the proposal lists them: **display_only**. The solid-state leaf F1.3.4 is shown inside "CDs and other audio discs", and Maps, Atlases and Globes are three level-2 groups. A labels and imprints side tab is added. Kind ids are unchanged.
- Evidence thin (major retailers blocked, no community page): **noted**. Every F1 call is provisional.
- Needs for QS_ and PF_ batches: the Goldmine, Disk Union, book and comic scales, the CBR premium-lines scheme (iii), the Acoustic Sounds badges (vi), carrier-system, film-gauge and region-code platform rows, ONIX list 175 and IEC 60094 (DPH_F_needs.tsv).

## F2

- Original against reproduction is an early question (eBay.de, Nanboya): **attribute** `authenticity_class` on named forms (original, interpretive, reproduction, restrike; R-2 classification). The page uses it as its first filter (display only). No tree change.
- Edition class: **attribute** `edition_class` on named forms (unique, limited edition, open edition). Together with authenticity_class it makes the "Original or edition?" filter. Edition size, numbering, signature and proof status belong to one edition or impression and are never stored (C16). The CAA proof classes are registered as a classification scale for guidance only.
- Giclée and clay: **covered**. They are C9 aliases: giclée a marketing name of inkjet print F2.3.6.01, clay an alias for the ceramic leaf F2.5.4. The tools/ alias load writes the missing rows.
- Japanese against Western painting (Nanboya): **covered**. Tradition stays a tag and a generated view (C11), never a level. Mineral-pigment painting F2.1.06 keeps its provisional kind status until a seller outside Japan lists it apart (CV-27). If none does, it becomes a named form.
- Era as a top filter (eBay.de Antik, Zeitgenössisch): **attribute** `era` on named forms (antique, contemporary). Makers get era from their years. It is a view only, never a level. Further values only from a fetched list.
- Poster: **attribute** `issue_form` (poster, print edition, proof), restated from F-10 so a poster view can be generated. No poster kind.
- Chop mark, blind stamp and certificate: **noted**. These are facts of one edition or work. They are shown as buying guidance and stored nowhere.
- Figurines (kinds F2.5.1.03, F2.5.4.02, F2.5.4.03, F2.5.5.01, F2.5.6.01): **noted**. They still need a fetched retailer or replacement-dealer page at the F2 harvest (memo risk 1). The "Figurines" display group over these five kinds and a manufactory side tab (Lladró, Goebel, Royal Doulton) are built with the tree: **display_only**.
- Display order (Artfinder and Singulart): **display_only**. Paintings, Prints, Photographs, Sculpture, Drawings, then Textile, Calligraphy, Collage. Ids are unchanged. An artist tab sits beside the medium tree.
- Evidence thin (Saatchi blocked, no collector community page): **noted**.
- Needs: the authenticity_class, edition-class and CAA proof classification rows; Artsy Rarity, LUMAS and Artfinder platform labels (vi). Auction records feed C4(d) price bands only.

## F3

- Stamp scales now fetched: **need**, two registry rows, both condition grade: centering (Gem to Poor) and gum (MNH to RG), on the Mystic, Wikipedia and Warwick and Warwick pages. Mystic premium grades are a third row, platform label. The memo's "stamps unsourced" finding is closed. No grade is stored.
- Grader scales: **need**. PSA, BGS (subgrades, Black Label), SGC, CGC Cards, ACE and TAG are each registered once, with kinds_served covering F3.8 single cards and the E1 trading-card-game card kinds. TCG cards stay E1 even when graded (F3-O3). The graders are certifier or grader maker rows.
- Coin scales: **need**. The Sheldon 70-point scale serves F3.1 and the F3.3 bullion coin; PMG and IBNS serve F3.2.
- Stempelglanz: **attribute**. It is a value of `finish`: circulation strike, brilliant uncirculated, proof, reverse proof, bullion finish. A C9 alias row (German) points Stempelglanz to brilliant uncirculated, provisional. The Bundesbank page names strike quality only and defines no grades (**noted**). Finish still decides bullion against collector coin (F3-O1); a mint page for that is still owed.
- Huntington "Back of Book": **display_only**. A generated view over postal_service values (airmail, postage due, official, semi-postal), revenue stamps and postal stationery. "Possessions" is an issuer tag (**attribute**, issuer). "Plate Blocks" becomes the value "plate block" of `unit` (**attribute**). None of them is a kind.
- Otakaraya "Chinese stamps" and "overseas stamps": **noted**. These are issuer tags inside views, never levels (owner no-country rule).
- Population reports and set registries: **noted**. Grader data needs a source census before any view is built. Nothing is stored per card.
- Order of wear and bullion: the UK order of wear is a scheme (iii), already decided. LBMA Good Delivery is a certification on refiner rows. Millesimal fineness is a class (i) standard.
- Display order (proposal L1, Huntington order, bullion beside coins): **display_only**. Ids are unchanged at build.

## F4

- Religious jewellery (The Catholic Company opens with Jewelry): **display_only**. A cross-link view shows A3 cross pendants and medal necklaces next to the devotional medal F4.2.4.01. Nothing moves (K-107).
- Bibles, prayer books and Monastery Products: **other_category**. Printed religious texts go to F1 and monastery foods, cosmetics and drinks to their product categories, as cross-links only.
- Juzu split by wearer: **covered**. Wearer is the user tag (C6, men or women), not a named form. Sect stays a C8 tag or C3 variant (memo).
- Prayer-rug padding, non-slip base and surface fabric: **attribute**. Three attributes on F4.2.2.01: `padding` (unpadded, padded), `non_slip_base` (yes, no), `surface_fabric` (velvet, cotton, synthetic).
- Travel prayer mat: **covered**, no named form. Travel is the setting tag already decided in the memo. A travel mat is the same rug made thinner, smaller or folding (C2(b), C6). A retailer's travel-mat menu is a facet on the setting tag (C10 retail-facet rule), not a design asked for by name.
- Mala "natural against treated": **attribute** `bead_treatment` on maker-bound prayer-bead named forms (natural, treated (dyed or stabilised), imitation; wording provisional). `bead_count` and `bead_size_mm` are added from the same guide.
- Rakuten grave-care goods: **covered** or **other_category**, homes ruled for the harvest. Grave stones and plaques go to grave marker F4.6.3.01. Grave flower vases go to offering vessel F4.4.3.01 and grave incense holders to incense burner F4.4.2.02, each with setting tag "grave". Grave lights are ritual candle F4.4.1.06 (K-113). Grave-cleaning brushes and cleaners are B6.
- Scribes: **other (ledger)**. Scribes are maker rows of class "artisan or atelier", with a `certifications` value (rabbinical certification) where a page states it. The certification is a standard (class i); it is never a tier.
- Evidence thin (no Orthodox, Islamic retail tree, Sikh, Taoist or Chinese source): **noted**. Every call is provisional, and new kinds may come at harvest (memo risk).
- Needs: kosher scroll grade, rabbinical certification, relic class and the casket steel-gauge standard. The tradition front-door filter, occasion view and tarot publisher tab are generated views (**display_only**).

## F5

- Letter-class scale: **attribute**, not a named form. Register the classes ALS, LS, TLS, DS, AL, AQS, AMQS, ANS, SP and cut signature as one classification row, and store `document_class` on kinds as the classes each kind admits (letter F5.3a, autograph F5.3e, DS for issued documents). An ALS is not a named form. The class says how one sheet was written and signed. That is a fact of the object, not a design many makers make (C2(a)). Dealers' price order is shown as guidance. Order provisional.
- Picture postcard print process: **attribute** `print_process` on the picture postcard and the photographic print (chromolithograph, collotype, halftone, real photo; collotype and halftone provisional). Briefmarkenmesse ranks the process among value markers.
- Postcard motifs (Ortsansichten, Jugendstil, Eisenbahn und Schifffahrt, Militaria): **attribute** `motif` on publisher-series named forms. These are subject tags for views, never kinds. `postcard_era` is added (Pioneer, Divided Back, golden age 1895-1914).
- Printed advertisement: **new_kind**. Build instruction: add the kind "printed advertisement or handbill" to leaf F5.3e "Kept printed ephemera", after advertising trade card. Definition: "a single printed advertising item kept after use (handbill, flyer, advertising leaflet, a detached magazine or newspaper advertisement page); a large public notice is a broadside, a poster is F2 (issue_form poster), a trade card is the advertising trade card, a catalogue or booklet is F1." The AbeBooks ephemera guide lists advertisements as an ephemera type, but it is a guide, not a seller. The kind is therefore † and provisional until a fetched seller or dealer page sells advertisements or handbills as their own category (C2(a)). Otherwise it is a named form of broadside (R-19).
- Marketplaces keep one flat ephemera class (AbeBooks): **noted**. Nothing argues against the memo's kinds. Use display groups only.
- Display regrouping (proposal L2): **display_only**. Letters, autographs and manuscripts; postcards and printed ephemera (the real photo postcard cross-listed); certificates, deeds and financial papers; identity and travel papers; cards and passes; albums; home recordings. No id change. The autograph is cross-listed with letters.
- Evidence thin (no Japanese, Chinese or French document source beyond one listing): **noted**.
- Needs: the autograph classes, the Antiques in France condition steps (platform label), ISO 18902 and PAT, ISO/IEC 7810, ICAO 9303 and the transit card system platform rows.

## F6

- Opal: **new_kind**. Build instruction: add "Opal (cut)" to F6.5 "Coloured gemstones", beside Amethyst (cut) and Garnet (cut). Definition: "loose opal cut en cabochon or faceted, or opal rough sold as cutting material; an opal specimen, matrix piece or uncut nodule is the F6.1 kind Opal". It shares `species_id` with F6.1 Opal (F-4 placement test; F-23 keeps opal a kind). Named forms come from the harvest, each on a fetched page, with region tags where they apply (black, boulder, Welo or Ethiopian, fire opal). Gem Rock Auctions leads its menu with opals (fetched page https://www.gemrockauctions.com/). Provisional until a page shows cut opal sold.
- Pairs and lots (Gem Rock): **attribute** `quantity` (single, pair, lot, set of like specimens). These are not kinds. The mixed teaching set stays a kit kind (S3a).
- Meteorite form (Peltram individuals against cut): **attribute** `meteorite_form` (individual, cut slice, etched slice, fragment; fragment provisional).
- Chondrite and achondrite split (Peltram): **covered**. It matches the memo's kinds (ordinary and carbonaceous chondrite; lunar and Martian under achondrites). No change.
- Treatment: **attribute** `treatment` on coloured-gemstone and diamond kinds (untreated, unheated, heated, filled, diffused, other treatment). Kind rows list the treatments the trade applies to that species. A stone's own treatment is never stored (C16). `origin_type` (natural, cultured, laboratory-grown) stays as the memo has it.
- Presentation (FossilEra polished stones, spheres, pendants): **attribute** `presentation`. Values: natural specimen, specimen on matrix, rough, tumbled, polished, slab, sphere, egg, faceted, cabochon. A pendant mounted as jewellery is **other_category** A3. Faceted and cabochon pieces fall under the F-4 placement test into F6.5. Mineral `size_class` (thumbnail to large cabinet) is added from Intelligent Collector.
- Evidence (dealer pages only, no community page; marker order rests on one guide each): **noted**. The marker order is provisional.
- Gem labs (GIA, SSEF, Gübelin, AGL, AIGS, GFCO) are certifier or grader maker rows. One stone's report is never stored. The gem-lab view and the named-fall view are generated (**display_only**).
- Needs: GIA diamond, coloured-diamond and pearl systems; a coloured-stone clarity platform label; mineral size classes; Geolitho and Conchology labels; Meteoritical Society nomenclature; Nickel-Strunz.
