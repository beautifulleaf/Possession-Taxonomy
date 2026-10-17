## Domain F
### Table
| code | name | sub-families | choice level | tier type | maker centrality | review verdict | kinds | daggers | OWNER marks |
|---|---|---|---|---|---|---|---|---|---|
| F1 | Media & Publications | Printed volumes and serials, Cartographic items, Sound carriers, Moving-image carriers, Parts and accessories (5) | Carrier system or binding class; comics by edition form; trim, diameter, speed are attributes | mixed | medium | minor fixes | 62 in worked tree | 54 | 48 |
| F2 | Art | Paintings, Drawings, Prints, Photographs, Sculpture, Textile and fibre hangings, Calligraphy, Collage mosaic and mixed work (8) | Medium, technique or material; sculpture by material family; subject, edition, size are not levels | preference | high | needs rework (figurines and sculpture only) | 64 | 45 | 28 |
| F3 | Coins, Stamps, Medals & Trading Cards | Coins, Banknotes and paper money, Bullion, Tokens and scrip, Postage and postal items, Medals and decorations, Trophies and awards, Trading cards, Regalia and insignia of office, Parts (10) | Standing or purpose of the issue; series and designs are named forms; grade never stored | mixed | high | minor fixes | 60 | 77 | 36 |
| F4 | Religious & Ceremonial Objects | Altars shrines and sacred images, Personal devotion aids, Ritual vessels implements and instruments, Light incense and offerings, Divination and esoteric tools, The dead (6) | Generic object form (C11); tradition names are named forms; scroll and case are separate kinds | preference | low | needs rework (kind level) | 62 | 82 | 41 |
| F5 | Documents & Personal Records | Issued documents, Cards passes and tokens, Personal records and keepsake papers (3, with 15 leaves) | Document or card type; carrier for records; page mechanism for albums | preference | low | minor fixes | 52 (80 to 120 at full coverage) | 28 | 24 |
| F6 | Natural History & Specimens | Minerals, Rocks, Fossils and fossil resin, Meteorites and impact glass, Gemstones and pearls (unset), Shells and marine hard parts, Preserved biological specimens, Element samples, Parts (F6.9 retired) | Species or trade name; organism group for fossils; class for meteorites; family for shells | mixed | low | minor fixes | about 70 in worked tree (550 to 900 estimated) | 64 | 31 |

### What conformance changed
- F1: Record kinds recut by groove standard; comics given own leaf with generic edition kinds and tankōbon, bunkoban, BD album as named forms; trim, diameter, fidelity became attributes; parts sub-family F1.5 added (F1-1, F1-2, F1-7, sec. 11).
- F2: Figurines got kinds in all six key materials, with manufactories as maker and line rows; poster kind and "original illustration art" deleted; aliases and printer systems left the named forms (sec. 11, F2-1 to F2-4).
- F3: Arcade token and airmail and postage-due kinds removed; trophies recut by form with material an attribute; card product lines became line rows; parts sub-family F3.10 added; motive tests replaced (sec. 11).
- F4: Kinds rebuilt as generic forms under C11 (prayer beads, household altar, incense burner, three bell kinds); leaf axes stated; "tier attributes" removed; diya, menorah, nativity set, offering vessels added (F4-1 to F4-5).
- F5: National ID designs, phonecard technology and acceptance class left the named forms; leaf axes restated; eight framework-only kinds marked dagger; album and ephemera questions deferred (F5-1 to F5-4, sec. 11).
- F6: Cut-state placement test added between Minerals and unset gems; pearls recut as saltwater and freshwater with trade names as named forms; study-set sub-family retired; specimen kinds added (F6-1 to F6-5).

### Owner questions (merged)
1. ★ Empty photo albums, binders and boxes B1; filled albums and scrapbooks F5? Removes the seven album mechanism kinds and album lines from F5.3d. [yes] (F5 O1, sec. 10; F1, F3)
2. ★ Issuing function as first fork (nine sub-families plus parts), with collecting discipline as a generated view, or discipline first? [issuing function] (F3 sec. 10 item 1)
3. ★ Figurines: material-family leaves shared with sculpture, or a separate Figurines sub-family; split from sculpture once a retailer sells them apart? [material leaves, no split] (F2 sec. 10 item 3)
4. ★ Tradition is a tag and view, never a level; butsudan and other tradition names are named forms, no C2(c) exception kind? [C11, no exceptions] (F4 O1)
5. ★ Gems against minerals by cut state (faceted, cabochon, cutting rough F6.5; all else F6.1); drilled beads C4; amber and ammolite follow it or stay F6.3? [yes; stay F6.3] (F6 sec. 10 item 4)
6. Comics and manga: own leaf with generic edition kinds and tankōbon, bunkoban, kanzenban, BD album as named forms, or fold into books? [own leaf] (F1 sec. 10 item 1)
7. Record kinds by groove standard, or diameter kinds as a stated exception to the size rule? [groove standard] (F1 item 12)
8. Pocket and trade paperback as two kinds or one with `trim_class`; bunko, shinsho and newspaper formats as named forms or attributes? [one kind; attributes] (F1 items 3, 13, 20)
9. Bound periodical volume with periodicals (against HS) or books; Playaway players F1.3.4 or D3; bar globe kind or attribute; audiobooks by carrier? [periodicals; F1; attribute; yes] (F1 items 2, 4, 8, 9)
10. Premium-line tiers (Absolute, Omnibus, Masterworks) enter only with a second-region source? [hold] (F1 item 21)
11. Posters filed by printing process with `issue_form = poster`, or one poster kind in its own leaf whatever the process? [process] (F2 item 4)
12. Pastel drawing or painting; gouache its own kind or under watercolour; Photographs keep the joined leaf "Camera-less and instant" or use `leaf = null`? [drawing; own kind; keep] (F2 items 1, 2, sec. 11)
13. Installation, video, light, kinetic art and sculpture-lamps in F2 when free-standing, video works I2? Reproductions in F2 with `authenticity_class`? [yes; yes] (F2 items 5, 6)
14. Artists as an exemplar ledger with ULAN ids, or an authority link only; portrait miniature a kind once attested; hanging and handscroll as `mount_format`. [exemplar; attribute] (F2 items 7, 8)
15. Taxidermy: a mount of one animal is F6 however presented; a composition with other materials is F2? [yes] (F2 item 11, F6 item 9)
16. Coin kinds by standing of the issue with ancient coins in the same kinds under an `era` tag; token kinds stop at purpose class; catalogue numbers stored after a licence check? [yes] (F3 items 2, 3, 8, 9)
17. Regalia: keep sub-family F3.9, or fold into Medals as leaf "Insignia of office"; chain, gavel, crown of office unattested. [fold] (F3 item 10, 21)
18. Postal covers: only postal stationery, administration-issued and first-day covers F3, or any cover that went through the post? [narrow rule] (F3 item 17, F5 O11)
19. Sets: approve mint and proof sets and the rock and mineral teaching set as kit kinds; factory card set held? [first two] (F3 item 15, F6 item 8)
20. Championship rings and belts: F3 awards (step 15 list), or A3 and E2? Panini-type stickers F3, E1 or C5? [F3; F3 if sold as collectibles] (F3 items 18, 19)
21. Play, prop and souvenir money: game money E1, prop and souvenir notes F3? [yes] (F3 item 20)
22. Emergency note against scrip: keep two kinds, merge, or divide by issuer type? Wooden nickels unassigned. Worn coin or medal as jewellery: F3 or A3? [memo gives none] (F3 items 22, 23, 24)
23. Prayer rugs F4 or B2; candles made for a rite F4 or B3; prayer and holy cards F4, F1 or F5? [F4, F4, F4] (F4 O4)
24. Singing bowls E3 unless made for a rite; prayer-bead necklaces F4 with counter, tassel or guru bead, A3 as a necklace? [yes; yes] (F4 O5, O6)
25. Devotional images by kind (icon, thangka, altarpiece, shrine statue, crucifix) F4, including old-master altarpieces; other religious subjects F2 or B4? [yes] (F4 O7, F2 item 10)
26. Spirit boards F4 or E1 (tarot sold for card play E1); salagrama stone or fossil kept for worship F4 or F6? [F4 if divination; F4] (F4 O11, O12)
27. Masonic ritual objects, smudge bundles, bon lanterns and stone tōrō: F4 or elsewhere? [worn regalia by worn rules, implements F4; smudge B4; lanterns F4 only if made for altar, grave or Obon] (F4 O8, O17)
28. The dead as one sub-family with pets a user tag and urn capacity an attribute, or keepsake and companion urns as C6 exceptions? [attribute, no exception] (F4 O9)
29. Kosher scroll grade held until a second source, relic class an attribute; parts sub-family F4.7 for Torah finial and coffin plate? [hold; none yet] (F4 O10, O16)
30. Small ledger for Judaica silversmiths, church-candle makers, urn houses, tarot publishers inside the shared ledger? [yes] (F4 O13)
31. Keep the leaf level in F5, or drop it (F5.2 alone may under C5(b))? [keep] (F5 O7)
32. Kept printed ephemera (menus, invitations, trade cards, receipts, labels, bookplates) as F5 kinds by form? Grows F5 from about 52 to 120 kinds. [yes] (F5 O2)
33. Other people's photographs: maker-signed or editioned prints F2, every other print, slide, negative F5 (needs step 19 reworded)? [yes] (F5 O3, F2 item 9)
34. Developed negatives, home audio and home film F5 "on a physical carrier"; entitlements I3 and card F5; vaccination, school and tax papers F5? [yes] (F5 O4, O5, O9)
35. Variety rule, second clause: amethyst, agate, jasper, opal kinds or named forms of quartz; diamond and fancy-colour diamond two kinds? [kinds; two kinds] (F6 item 3, sec. 3)
36. Mineral leaf by Strunz, Dana or trade families, after the quartz placement is read; pearls as saltwater and freshwater kinds with Akoya, South Sea, Tahitian named forms? [Strunz; yes] (F6 items 2, 5)
37. Simulants out; slab, sphere, egg, palm stone in; lamp, carved animal, pendant out; fossil and skull replicas F2 if sculpture, E1 if toy or kit; human remains out, ivory and CITES in? [yes] (F6 items 6, 7)
38. Species and taxa loaded as named forms only when attested; element identity an attribute; healing and birthstone views generated from tags? [yes] (F6 item 12)

### Shared-rule questions raised in this domain
- C1 amendment: maker classes for domain F (publisher, mint, card manufacturer, certifier or grader, taxidermy studio and others) and the shared issuer table (F3, F5). All six memos depend on it.
- Line against named form (review C K4): F1 publisher lines, F2 figurine series, F3 card lines, F4 candle and statue lines.
- Grading-scale registry (extends C16): F1 condition scales, F2 authenticity and edition schemes, F3 Sheldon, PMG and PSA, F4 kosher grade, F6 seven seed rows.
- C6 addition, size against format: F1 film gauge, 16-inch disc and Mini-CD; F4 urn capacity; F3 and F6 need no change.
- C11 two-region tie-break (variety test): F1 bunko, F2 nihonga, F4 butsudan, F6 amethyst and pearls.
- C5(d) parts sub-families (X6): F1.5, F3.10, F6.10 now; F2, F4, F5 hold none until attested.
- Albums, binders and holders (X5): F1.5, F3.10, F5.3d.
- Sets, rolls and lots (X10, review C K6): F3 proof and mint sets, F6 teaching set, F4 nativity set.
- Cards, scrip and postal covers (X2) and religious medals (X1): F3, F4, F5 sentences in _framework_conflicts.md, domain F section.
- Photographs (X3, with `process` and `mount_format`) and devotional images (X4): F2, F4, F5; X3 needs step 19 wording changed.
- C13 compatibility ledger: F1 carrier systems, F5 card systems.
- C4(d) USD bands above 15,000 and the C7 non-maker-first amendment (domain G): F2 and F6 price range.
- C8 scene vocabulary, C16 individual-item facts, C17 jurisdiction ledger (CITES, ivory: F6, F2).
- Sources `fetch_status` column and excerpts file (X14): all six memos, needs a tools/ script.
- Other framework conflicts logged for domain F: step 15 rings, belts, play money; step 14 prayer rugs and rite candles; step 7 simulants and human specimens.
END F
