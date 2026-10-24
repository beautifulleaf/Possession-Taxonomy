# QS_W3_4 report

Rows written (verify/out/QS_W3_4_*.tsv): schemes 7, tier_entries 21, standards 23, standard_values 35, grading_scales 4, named_forms 44, makers 26, maker_kinds 37. No issuers or kinds files.

Schemes and editions: Euro NCAP (2025 and 2026 protocol results, 4 entries); J.D. Power IQS 2025 (7 entries); J.D. Power VDS 2026 (6); U.S. News Best OTC pharmacist panel 2026 (4); CCCA Full Classic, HearingTracker SoundScore and my-best (scheme row only, no product named on a fetched page).

Standards: CE design category, ISO 4210-2, EN 15194, BS 3632, BS EN 1647 (fetched page is the withdrawn 2004+A1:2008 edition; current edition page failed), HUD Code, IRC Appendix Q, ANSI A119.5, NFPA 1192, AS 4349.1, NZ LIM, USP Verified, NSF/ANSI 173, NSF Certified for Sport, Informed Sport, ConsumerLab (35 certified products as standard_values, kinds H2.7.1.1-3, 2.1, 4.1, 4.2 only; pet and other-kind items skipped), Clean Label Project, Non-GMO Project, NSF/ANSI 455-2 GMP, BIHS list, ANSI/ISEA Z308.1, BS 8599-1, ISO 3533.
Grading scales: UK EPC bands, RICS condition ratings, RICS levels, ALC grades.

Failed or blocked pages (WebFetch 403/redirect/503, then Parallel fallback): bihsoc.org list (503/network; BIHS page lists no devices, spreadsheet only), businesswire VDS release (403; the jdpower.com page worked), chanrobles, NSF/USP/wetestyoutrust (fixed by Parallel). Natural England ALC page is a survey-map legend (partial).

Left out, no defining page fetched: eBay Motors Exotics list (no eBay page defines it); Polaris snowmobile trim ladder (Polaris page names families, no ladder); Shimano/SRAM/Campagnolo ladders (only Cycling Weekly and Wikipedia, no maker page); ISO 8098 (no fetched page); Informed Choice; DIN 13157/13164/13169; China office grades (only a draft-translation index of GB/T 39069-2020); body_safe_class (computed, no URL); Euro NCAP Kia K4 and EV2 (body type not on page).
Caveats: CE category source is a law-firm page, not the Directive text; EPC pages are Barratt and Fuse, not gov.uk; ANSI A119.5/NFPA 1192 source is the Tiny Home Industry Association; Clean Label Project tiers (Purity Award) not defined on the fetched page.
Skips to other categories: none. Brand-level J.D. Power makers (9) have no maker_kinds row: missing kind?: passenger-car brand with no body-type kind.
