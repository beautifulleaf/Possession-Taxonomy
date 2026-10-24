# DPW1_F5 report: F5 Documents & Personal Records

Outputs: DPW1_F5_kinds.tsv (27 rows), DPW1_F5_moves.tsv (11 rows). There is no DPMK_1_F5 file.

## Task 1: missing kinds (27 candidates)
new_kind 7, named_form 7, covered 9, attribute 2, other_category 2 (hotel key fob → A4 keyring; brochure → F1).

New kinds take the next free id under R-58, checked against kinds.tsv and the tree map:
- F5.1.1.06 Citizenship or naturalisation certificate (no source URL; goes to HV_NK)
- F5.1.1.07 Social security or insurance card (no source URL; goes to HV_NK)
- F5.1.2.07 Confirmation or first communion certificate (EBTH)
- F5.2.1.05 Charge plate (eBay subcategory)
- F5.2.2.04 Prepaid e-money card (no source URL)
- F5.3.5.16 Visiting card (calling card) (eBay; Richmond class)
- F5.3.5.17 Lottery ticket (Colnect category)

Named forms: stateless travel document and laissez-passer (passport), lantern slide (slide), luggage, cigar-box and crate labels (label), commonplace book (filled notebook), reward of merit card (already stored).

## Task 2: named forms (267 reviewed, 11 flagged)
- **drop 3:** Ausweis (C11 alias); Geburts- und Taufschein (another title of Taufschein); Marriage Fraktur (Fraktur is a style).
- **move_kind 7:** Certificat d'études primaires → diploma; Edy, nanaco, Smart Purse, miniCash, Flazz and BRIZZI → F5.2.2.04.
- **to_line 1:** NCMC → L-npci-ncmc.

The other 243 transit cards stay: issued brands inside one kind.

## Task 3: navigation
I confirm R-116: F5 is entered by **type of object**. Every seller in the harvest divides the material by type: eBay (card types, phone cards, real-photo postcards, negatives, slides, albums), Colnect (bank, gift, hotel, phone, lottery and transport cards) and Collectors Weekly (passports, stock certificates, letters, menus, trade cards, ticket stubs).

Period appears only as a facet (eBay Documents 1800–1899), and railroadiana only as a topic view. 254 of the 267 named forms are transit cards under one kind, which puts them at level 3. Country stays a filter only (owner rule).

Sketch:
1. **Level 1:** Letters, autographs & manuscripts; Postcards & printed ephemera; Photographs, slides & negatives; Certificates, deeds & financial papers; Identity & travel papers; Cards & passes; Albums & scrapbooks; Home recordings.
2. **Level 2:** the kinds. For example, Cards & passes holds credit, debit, charge, charge plate, gift, e-money, telephone, transit, membership, key and SIM cards. Each new kind joins its leaf's group.
3. **Level 3:** the named forms (Suica, Oyster; carte de visite, real photo postcard; ICAO passport codes). Class, era, motif and issuer are filters.

## Rules applied
C2(a), C2(b), C3, C11, R-18 and R-35, R-58, one home per object, precedences P3, P5, P7.

## † claims (from knowledge, not on a fetched page)
- Edy, nanaco, Smart Purse, miniCash, Flazz and BRIZZI are general e-money cards. F5.2.2.04 and the six moves rest on this.
- NCMC is issued as debit, credit and prepaid cards.

## Notes
- F5.3.5.08 (printed advertisement or handbill) was loaded as attested, although the HV report says handbills have no category of their own. The logged musicgoldmine page lists handbills as a shop class, so the kind stands.
- F5.3.3.03 (home audio recording) is still unattested.
