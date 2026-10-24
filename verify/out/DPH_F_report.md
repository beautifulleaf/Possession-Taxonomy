# DPH_F report: structure decision pass, domain F (F1–F6, none built)

Offline pass: no web, no git, nothing written to data/ or framework/. Inputs: the BRIEF, CONVENTIONS_v1, D4 (R-58, R-70, R-96 to R-118), maker_roles, the F rows of proposals.tsv, the F rows of the HOL_EV evidence files, and memos F1 to F6 (sections 3, 10, 12 and 13). F2 and F4 have node trees and memo kind ids. The others have none.

Because every category is unbuilt, all decisions are build notes (DPH_F_memo_notes.md, to be appended as memo section 14). DPH_F_kinds.tsv, DPH_F_moves.tsv and DPH_F_groups_changes.tsv hold only their header rows: there are no built kinds, and groups.tsv has no F groups.

## Points decided (structure_flags split, plus display points from the proposals)

| Code | new_kind | named_form | attribute | covered | other_category | other (ledger/registry) | display_only | noted | total |
|---|---|---|---|---|---|---|---|---|---|
| F1 | 0 | 1 | 3 | 0 | 2 | 3 | 1 | 3 | 13 |
| F2 | 0 | 0 | 4 | 2 | 0 | 0 | 2 | 3 | 11 |
| F3 | 0 | 0 | 3 | 1 | 0 | 3 | 2 | 3 | 12 |
| F4 | 0 | 0 | 2 | 3 | 1 | 1 | 2 | 1 | 10 |
| F5 | 1 | 0 | 3 | 0 | 0 | 0 | 1 | 2 | 7 |
| F6 | 1 | 0 | 4 | 1 | 1 | 0 | 1 | 1 | 9 |

No merges and no splits.

## New kinds (build instructions; ids are assigned at build under R-58)

- **F5.3e "printed advertisement or handbill"**: handbills, flyers, advertising leaflets and detached advertisement pages. Posters stay F2, broadsides and trade cards stay their own kinds. **Provisional**: only a buying guide (AbeBooks) names the type; a seller page must show it sold as its own category, or it becomes a named form of broadside.
- **F6.5 "Opal (cut)"**: cabochon, faceted or cutting-rough opal, sharing species_id with the F6.1 Opal kind (F-4 placement test). Gem Rock Auctions leads with opals. **Provisional** until a page shows cut opal sold.

## Other main calls

- UHQR is a maker-bound named form of the microgroove record (Analogue Productions); QRP's pressing is a maker-relations row.
- Pressing plants use maker_class "supplier"; no new class is added.
- Two-part record condition is one Goldmine registry row with components named in its notes.
- An ALS is a document_class value, not a named form.
- A travel prayer mat is the setting tag, not a named form.
- Grave-care goods get their homes ruled: markers F4.6.3.01, vases F4.4.3.01, incense holders F4.4.2.02, lights F4.4.1.06, cleaners B6.
- TCG grader scales are registered once across F3.8 and E1.

## Attributes (27; DPH_F_attributes.tsv)

- F1: mastering, weight_g, pressing_material, encoding, content_type
- F2: authenticity_class, edition_class, era, issue_form
- F3: finish (Stempelglanz is an alias of brilliant uncirculated), unit (adds plate block), postal_service
- F4: padding, non_slip_base, surface_fabric, bead_treatment, bead_count, bead_size_mm
- F5: document_class, print_process, motif, postcard_era
- F6: treatment, quantity, meteorite_form, presentation, size_class

All are facets.

## Needs (48; DPH_F_needs.tsv)

| Type | Count | Examples |
|---|---|---|
| Grading scales | 31 | Goldmine, Disk Union, book, comic; Sheldon, PMG, IBNS; stamp centering, gum, Mystic; PSA, BGS, SGC, CGC, ACE/TAG; authenticity, edition, CAA proof; kosher grade, relic class; autograph classes, Antiques in France; GIA ×3, gem clarity, mineral size, Geolitho/Conchology |
| Schemes | 5 | CBR (iii), Acoustic Sounds (vi), Artsy/LUMAS (vi), Artfinder (vi), UK order of wear (iii) |
| Platform sets | 4 | carrier systems, film gauges, video region codes, transit card systems |
| Standards | 12 | ONIX 175, IEC 60094, LBMA, fineness, sofer certification, casket gauge, ISO 18902/PAT, ISO/IEC 7810, ICAO 9303, Meteoritical Society, Nickel-Strunz, … |

## Thin evidence (provisional)

- Every F1 call: retailers were blocked and no community page was reached.
- Book and comic condition scales: no page fetched.
- The Blu-spec CD value; the all-analog and half-speed mastering values.
- F2 era values beyond antique and contemporary; figurine kinds are still unattested.
- Stempelglanz as an alias of brilliant uncirculated; F3-O1 finish (a mint page is still owed).
- Bead treatment wording; tasbih bead counts.
- Autograph class order; collotype and halftone print-process values; "greetings" as a motif.
- Meteorite form "fragment"; the order of the F6 markers (one guide each).
- The casket steel-gauge standard (owner unknown).
- Both new kinds.
