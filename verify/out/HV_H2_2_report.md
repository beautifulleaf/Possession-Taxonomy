# HV_H2_2 report (H2.5 to H2.8, wave 3)

**Kinds:** 51 of 51 attested (all worklist rows, incl. provisional H2.6.0.1). Not attested: none. H2.5.2.11 white cane is partial (RNIB long-canes collection showed brands and filters but no product names). H2.7.4.2 fish oil and H2.7.5.1 blends are partial (single Walgreens listing pages). H2.6.0.1 attested by German pharmacy category "Einzelmittel 1g" (Arnica, Rhus tox, Hekla lava C30 globuli); Walgreens and Boiron USA file single remedies by symptom, so the category is German-pharmacy only.

**Named forms:** 170 (maker-bound, owner-only role). **Lines:** 8 (Oticon Intent, Signia IX, Ocutech Reveal, Cellucor C4, ON Gold Standard, GU gels, Nuun, Huel powders). **Makers:** 53 new rows; 7 reused (M-eschenbach-optik, M-bausch-and-lomb, M-mead-johnson, M-phonak, M-oticon, M-widex, M-resound). Countries only where a page states them (Phonak CH, Oticon, Widex, Signia, ReSound DK, Starkey US, BRAND'S SG). The existing M-signia is a different (fashion) brand, so hearing-aid Signia is M-signia-hearing-aids.

**Caveats:** (1) Soft-lens brand-to-maker links (Alcon, CooperVision, J&J, Bausch + Lomb) are not shown per brand on the fetched Lens.com page, which only lists the four manufacturers; flagged in row notes. (2) Retail-page medicine and supplement brands (Zyrtec, Tylenol, Nature Made and similar) are entered as brand makers; owning companies are not named on the pages. Forms whose maker is not shown have maker_id empty. (3) Advil PM filed under oral analgesic (pain printed first). Magnesium + Ashwagandha products filed under H2.7.5.1 (mixed ingredients).

**Catalogues:** Anchor registries (AccessGUDID, EASTIN, DSLD, HearingTracker directory, Lens.com) were only partly used: HearingTracker overview and Lens.com served well; Walgreens category pages (WebFetch not needed; Parallel fetch worked) served H2.6 and H2.7 best; brand stores (Optimum Nutrition, Cellucor, Quest, GU, Huel, Nuun, Mead Johnson) served H2.8. DSLD, EASTIN and TAIS were not opened.

**missing kind?** (generic types seen on fetched pages that the tree lacks)
- electronic video / digital magnifier (H2.5.2): https://www.maxiaids.com/ (category link "Electronic Magnification - OCR") and https://specialneedscomputers.ca/collections/low-vision-magnifiers-for-the-visually-impaired (Magnifiers - Portable, Wearables)
- monocular / telescope for low vision (H2.5.2): https://carroll.org/product-category/magnification/magnifiers (Selsi Monocular), https://specialneedscomputers.ca/collections/low-vision-magnifiers-for-the-visually-impaired (Keplerian Telescopes)
- eye tracker for communication (H2.5.3): https://www.tobiidynavox.com/collections/devices (PCEye)
- cough drops / lozenges (H2.6.2): https://www.walgreens.com/store/c/cough-cold-and-flu-medications/ID=360549-tier2general
- fat burner / thermogenic (H2.8): https://cellucor.com/collections/sports-nutrition
- protein chips (H2.8.1): https://www.questnutrition.com/collections/protein-bars
- weight gainer (H2.8.1): https://www.optimumnutrition.com/en-us/collections/protein-powders (Serious Mass, Pro Gainer)

Files: verify/out/HV_H2_2_kinds.tsv, _named_forms.tsv, _makers.tsv, _lines.tsv; fetch log verify/work/HV_H2_2/fetched.tsv (56 fetches logged); build script verify/work/HV_H2_2/build.py.
