# HV_E2_1 report (E2.1 to E2.6, wave 3)

**Kinds:** 40 of 40 attested (status attested, all with a full or partial fetched page). Not attested: none. Thin evidence: Paintball marker (one listing page, unavailable item, Planet Eclipse Emek/MG100, partial); Track spike (Marathon Sports sprint page shows brand collections but no model, partial); Hurdle (Gopher Sport page, partial); Padded cycling shorts (Pearl iZUMi collection, one model visible, partial); Bokken (single DAX listing); Wushu practice weapon (one IWUF dao listing, seller JinLi named, maker not).

**Named forms:** 279, in HV_E2_1_named_forms.tsv. **Lines:** 6 (Leon Paul Mag-Tec, Apex, Team FIE, Phoenix 350N, X-Change; SPES AP). **Makers:** 76 new rows in HV_E2_1_makers.tsv; 22 existing ids reused. Six ids were NOT reused because the existing row is a different brand (M-jt, M-advance, M-nova, M-swing, M-boreal, M-virtue), so new ids were made (-paintball, -paragliders, -climbing suffixes). Countries left empty except SPES (PL, from the fetched page). Owner-only maker role: makers appear only as owners of a named form or line.

**Catalogues:** the E2 anchor catalogues (USGA, ITTF, World Athletics, FIBA, LoftChart, RunRepeat, Intersport, Wikipedia) do not cover these sub-families, so open shops were used: Rock+Run (climbing), Leon Paul US (fencing), Kult of Athena and Faits d'Armes (HEMA), Dover Saddlery, Mantel, Red Wolf Airsoft, Badlands Paintball, Wills Wing, Paraglidingequipment.com, Freedom-Parapente, Powerkiter, Mademoiselle Danse, Fitshop (judo), Bushizo (kendo), eBay boxing category, Compass Point. Blocked pages (403/404) were retried with the Parallel fetch where noted in fetched.tsv; still failed: Bloch-linked Move Dancewear, MEC, Gill store, Yumping, Faits d'Armes jacket page.

**Missing kind?**
- Gymnastic apparatus (E2.2.3, no kinds in tree): balance beam, uneven/parallel/single bars, vault board, pommel horse sold as separate types, https://gophersport.com/sports/gymnastics/apparatuses
- HEMA plastron / gorget / HEMA trousers (probably E2.17 or E2.16, not mine): https://faitsdarmes.com/en/brand/5-spes?page=2
- Climbing: no caving gear page was fetched (E2.3.1 left empty; search found only guides).
- Airsoft: airsoft pistols and SMG sold as separate categories (https://www.redwolfairsoft.com/guns/airsoft-rifles/electric-rifles links an SMG section; the single marker kind may need splitting by type).
- Fencing: lame jacket, fencing glove, underarm protector, chest protector, fencing shoe on https://www.leonpaulusa.com/fencing-clothing-uniforms.html
- Dance: jazz shoe, character shoe (https://www.weissmans.com/shop/dancewear/black-orange-pink/400)
- Track: no starter electronic device kind (Gill Halo) beyond pistol.

**Process note:** one URL (badlandspaintball markers page) was typed by me rather than taken from a result and returned 404; a typed Weissmans variant also 404ed. Both are logged as failed and produced no rows.

Files: verify/out/HV_E2_1_kinds.tsv, _named_forms.tsv, _makers.tsv, _lines.tsv; fetch log verify/work/HV_E2_1/fetched.tsv; generator verify/work/HV_E2_1/build.py.
