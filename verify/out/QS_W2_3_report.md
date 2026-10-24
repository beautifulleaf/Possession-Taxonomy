# QS_W2_3 report (Allure Best of Beauty 2026 skin care, H1)
Scheme reused: SCH-allure-best-of-beauty (2026, date 2026-09-17, stale_after 2029-12-31); no schemes file.
Rows: tier_entries 14, named_forms 14, maker_kinds 14, makers 4 new (Sonni, The Face Shop, Lightsaver, OOTD; country not stated). 10 existing makers reused. All fetch_status partial.
Per kind: wash-off face mask 2 (OleHenriksen, Dr. Idriss), sleeping mask 1 (Fenty Skin), sheet mask 1 (Sonni), toner 3 (Laneige, Glow Recipe pads, Elemis pads), face cleanser 3, sunscreen 1 (Lightsaver tinted), serum 2 (OOTD, La Roche-Posay Mela B3), cream 1 (Tula eye balm).
Method: ~20 narrow Parallel excerpt fetches of the one skin-care page (WebFetch blocked); each returns one or two fragments, so coverage stays PARTIAL. Not reached: retinol, lip care, self-tanner, body, remaining serum/moisturizer/sunscreen winners (no heading surfaced). Full-page fetch not tried (Parallel returns empty on this site per S11 note).
Skips (no kind; missing kind?): face mist (Tower 28 SOS Rescue Spray), acne spot treatment / pimple patch (Byoma Blemish Acne Treatment Spot Paste, Starface Hydro-Star + Salicylic Acid), skin-care device (Therabody TheraFace Depuffing Wand, NuFace Trinity+ Complete Set, Beauty Power Eyebrow Razor). Self-tanner kind exists but no self-tanner winner surfaced (Isle of Paradise Self-Tan Drops from W2_2 not re-found on this page).
Already in data/ from W2_2 and skipped: Caudalie, Erly, Peach & Lily, SkinCeuticals, PanOxyl, Paula's Choice, Medik8, Olay, Shiseido eye cream, Beauty of Joseon oil, Inkey List balm, Rose Ingleton.
Judgement placements: Dr. Idriss Flash Mask as wash-off; Elemis pads as toner; Tula eye balm as cream; OOTD value is the section heading (sub-label not shown).
Scheme kinds_served needs adding: H1.1.1.01 (present), H1.1.5.01, H1.1.5.02, H1.1.5.03.
Helper: verify/work/QS_W2_3/build.py, fetched.tsv.
