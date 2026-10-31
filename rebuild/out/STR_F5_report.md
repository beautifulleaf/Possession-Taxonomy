# STR_F5 report: Documents & Personal Records

**Counts, before to after.** Departments 7 to 7. Shelves 18 to 22. Kinds 70 to 84. Archetypes 114 to 74 (40 generic ones demoted into types).

**Category.** Added `ax` and a seven-step `key` with a precedence note. The lead is unchanged. Every department has `t` and `ax`, every shelf has `t`, and shelves with more than three kinds have `ax`. All kinds now use `tt`, with one-question groups.

**Regrouped.**
- Letters: three shelves, Signatures & signed objects, Letters/telegrams/cards, Diaries & manuscripts. The autograph album moved to the signatures shelf.
- Photographs: four shelves, Postcards, Photographs (oldest first), Slides/film/negatives, Albums & scrapbooks. The postcard album moved to the albums shelf.
- Ephemera: shelves reordered and renamed, with Receipt kept under Trade & business paper.
- Shares: split into Shares & bonds and Cheques & payment orders.
- Identity: split into State identity & travel papers and Work & event badges.
- Property papers: shelf renamed.

**Renamed or merged** (see `F5_renames.json`).
- Slide became 35 mm slide, which also removes the clash with A2 Slide.
- Identity document merged into National identity card. Social security card and citizenship certificate became its types.

**Added kinds, each with a fetched source:**
- Cased photograph (CCI note)
- Photo-booth strip (Wikipedia Photo booth)
- Instant print (Instant film)
- Lantern slide (Magic lantern)
- Home-movie film (Super 8)
- Scrapbook (Scrapbooking)
- Maximum card (Postcard)
- Telegram (Wikipedia Telegram)
- Dance card (Wikipedia Dance card)
- Life-event announcement (Ephemera)
- Promissory note (Wikipedia Promissory note)
- Visa & residence permit (Travel visa)
- Driving licence (Driver's license)

Reference-split kinds: View-Master reel split out of Slide (Wikipedia View-Master); National identity card (Wikipedia list of national identity card policies).

**Coverage references per shelf:**
- Letters: Autograph collecting.
- Postcards: Postcard.
- Ephemera: Ephemera.
- Shares and bonds: Scripophily.
- Phone cards: Telephone card.
- Identity and certificates: the per-kind pages above.

**Demoted generic archetypes** (now types or definitions):
- Signed photograph, Cut signature, Signed ball or bat, Game-worn jersey.
- Charter, Indenture, Papal bull, Firman, Ship's log.
- Armorial and pictorial bookplate, Exchange ex-libris.
- Engraved shop card, Ballad and Execution broadside, and similar.
- Photographic lantern slide became the archetype Hyalotype. View-Master reel became Sawyer's scenic reel under the new kind.
- Dance card became a kind.

**Cross-links added: 28**, targets checked against the reader files, into A3, A4, B5, C4, C5, D4, F1, F2 and F3. The STR_SEE Slide clash is resolved by renaming.

**Not done.**
- Ration book dropped: the source returned HTTP 410.
- Gift and membership card not split: no fetched Wikipedia page for loyalty cards.
- No new makers were needed, so `F5_brands.json` and `F5_moves.json` are unchanged.
- Most existing tier-department kinds carry the old source URL rather than a re-fetch.
