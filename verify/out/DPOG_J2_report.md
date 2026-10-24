# DPOG_J2 report: J2 missing kinds from the origin-and-grade harvest (OG_J2)

Offline Opus pass under DPW2_COMMON (no web, no git, nothing written to data/). Input: OG_J2_missing_kinds.tsv, 21 designations giving 17 items, checked against data/kinds.tsv and the DPW2_J2 kinds (all attested). Task 2 skipped, so the moves file is header-only. Navigation unchanged (R-104).

## Task 1: decisions (17 items)
new_kind 12, covered 5.

**New kinds** (R-58: next free id under each parent, none reused; attested by HV_J2_NK4):
- J2.1.1.48 Tench
- J2.1.1.49 Pufferfish [fugu; fuku]
- J2.1.1.50 Sea trout or brown trout [sewin] (Salmo trutta).
- J2.1.1.51 Lamprey [nēģi]
- J2.1.1.52 Whitefish [vendace; pollan; muikku] (Coregonus).
- J2.1.1.53 Whitebait [shirasu] (fry of several species, raw or plain boiled)
- J2.1.1.54 Cutlassfish [hairtail; tachiuo; galchi]
- J2.2.11 Smoked shad
- J2.3.17 Stockfish [tørrfisk] (unsalted and air-dried, so it is not salt cod)
- J2.3.18 Dried rockfish [geonureok] †
- J2.4.31 Vinegar-marinated sea bream [sasazuke] (P4b; C11).
- J2.5.3.09 Vendace roe [löjrom] (J-5: roe kinds go by source species)

**Covered:**
- Salted anchovy (Ligurian and Collioure): J2.4.05. Salt against oil is pack medium, as DPW1 decided.
- Szilvásvárad trout: J2.1.1.06 rainbow trout †.
- Caviar d'Aquitaine: J2.5.1.11 †.
- Pollan: the new J2.1.1.52.
- Balatoni hal: covered by the species kinds as a tag.

## Designation map
verify/out/DPOG_J2_designation_kinds.tsv has 21 rows. Each binds one kind (a non-maker named form, JC1) except DS-hu-balatoni-hal, which binds a tag: its fish are sold species by species, not as a mix (P6). Its kinds_served are carp J2.1.1.44 and zander J2.1.1.43 (†); the full list comes from the specification, and a species with no kind (such as wels catfish or bream) returns as a missing kind. Rows on new kinds wait for HV_J2_NK4.

## Scope and wording calls
- **Live fish stay OUT (K-26).** Torafugu and tench are often sold live, so their attesting pages must show the fish sold dead, dressed or cut.
- **Lamprey cooking.** Roasting lamprey is plain cooking of one ingredient, an attribute. Jarred lamprey in a vinegar marinade is J2.4. If the Latvian specifications cover both forms, those designations become tags.
- **Whitebait coating.** Coated whitebait is prepared and OUT (P-P). Semi-dried shirasu-boshi would be J2.3.
- **Proposed wording changes (ids unchanged):**
  - J2.3.01 adds "unsalted air-dried stockfish is J2.3.17".
  - J2.1.1.06 adds "Salmo trutta is J2.1.1.50".
- **Possible typo.** "Lough Neah Pollan" is probably Lough Neagh. HV_J2_NK4 should check the register spelling.
- **Leaf size.** J2.1.1 grows to 54 kinds and J2.3 to 18. Display grouping (R-104(b)) still applies.

## Rules applied
C2(a)(c), C11, JC1, JC4, P2/K-26, P3, P4b, P6/K-46, P-P, J-5, R-58, R-96(c), R-104(b), R-112(a).

## Decisions resting on † claims (to confirm at attestation)
- Szilvásvárad trout is rainbow trout.
- Aquitaine caviar is A. baerii.
- 건우럭 is dried rockfish. If it is not, the designation goes to J2.1.1.47.
- The species of Balatoni hal.
- The product forms in the lamprey specifications.
