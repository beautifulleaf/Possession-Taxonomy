# DPH_J memo notes (domain J; offline Opus pass, R-116 d, R-118 a)

## J1
Not built. These notes bind the build like memo text (R-118 a).
- Build the tree from the memo's Candidate B (section 3 worked tree, section 10; 87 kinds, 24 marked †). Give ids by R-58 when it is built. A † kind gets its id only when a page attests it (R-96 c). No page may be generated before nodes and kinds are loaded.
- Level-1 display groups P-J1-1 to P-J1-9 sit over the tree as a display layer only:
  - Groups 1–6 are the J1-A animal leaves (veal shown with beef in P-J1-1, poultry split chicken / other poultry).
  - Group 7 is J1-B, group 8 is J1-C, group 9 is J1-D.
  - Level-2 groups for fresh meat (steaks, roasting joints, mince and burgers, slow-cook cuts, offal) are display only. No use class becomes a leaf.
- Bacon: the kind stays in J1-B raw-cured (memo tree). The shopper group "Bacon" (Whole Foods) is a level-2 display group under P-J1-7, beside ibérico, other dry-cured ham and cooked ham. Decision: display_only.
- Grading scales to harvest (needs file): USDA beef quality grades; JMGA yield and quality grades; BMS 1–12; Hanwoo grades; Ibérico colour labels (C16 classification); EU poultry farming terms; Global Animal Partnership steps. USDA Organic and Certified Humane are standards (certifications on the product, never tiers). Kobe Beef and the ham PDOs (Guijuelo, Jabugo, Dehesa de Extremadura, Los Pedroches) are designation rows: one-kind ones are named forms, multi-kind ones are tags (JC1).
- Meat breeds (cattle, pig, poultry) go into the varieties table as `variety_type` breed (JC7, R-112 a), with a VR_J1 harvest. A breed is never a kind or a level.
- Wagyu by prefecture is a generated view built from designation tags (Crowd Cow). There is no house tab, since the maker role is none.

## J2
Built. Points decided:
- The counter group becomes the stored kind attribute `species_group` (ten values). G-J2-7 to G-J2-16 are generated from it. Finfish J2.1.1 (now 55 kinds) gets no leaf split (R-58). Decision: attribute.
- Squid and octopus stay inside molluscs J2.1.3. Group G-J2-15 is renamed "Squid, cuttlefish and octopus". Decision: display_only.
- Fresh anchovy is a new kind, J2.1.1.55 Anchovy [boquerón; bocarte], in group Oily fish. Decision: new_kind.
- Fresh cuttlefish is a new kind, J2.1.3.16 Cuttlefish [sepia; seiche], in group G-J2-15. Decision: new_kind.
- Ōtoro, chūtoro and akami are non-maker named forms under bluefin J2.1.1.18 (J-1). The fat ladder is a generated view. Yellowfin akami waits for a page. Decision: named_form.
- Caviar grain grade: the attribute `grain_grade` (000 | 00 | 0) plus a grading_scales row (FAO). Producer grades stay tier entries. Decision: attribute.
- MSC, ASC and Seafood Watch become scheme rows, as tier entries on kinds with scope origin and method (R-118 c). Decision: needs.
- GS-ec-fish-size-categories gets its steps filled per species from Reg. 2406/96 Annex II. Decision: needs.
- Sashimi-grade collection: a generated view from the named-form attribute `raw_eating_asserted` (yes | not stated). Decision: display_only, attribute.
- `season` is an attribute on kinds, named forms and varieties (months at best, scope hemisphere or region). Decision: attribute.
- Noted for harvest: no raw bigeye or albacore tuna kind exists.

## J3
Built. Points decided:
- J3.4.6.08 split. The kind id stays, renamed "Semi-hard pressed cheese (farmhouse and regional types)". Eight new kinds take the generic types now held in the catch-all, and 15 named forms move:
  - J3.4.6.15 Tomme [toma]: Tome des Bauges, Tomme de Savoie, Tomme des Pyrénées, Toma Piemontese, Tomme Bejo.
  - J3.4.6.16 Soft thistle-rennet cheese (torta): Azeitão, Serpa, Serra da Estrela, La Serena.
  - J3.4.6.17 Wensleydale; .18 Caerphilly; .19 Lancashire; .20 Cheshire; .21 Gloucester (Double and Single).
  - J3.4.6.22 Spiced Dutch cheese (Leyden, nagelkaas): Boeren-Leidse, Kanterkaas.
  - 62 protected names and 4 maker forms stay in the catch-all. They have no generic type sold outside their own name (Cantal, Morbier, Mahón, Minas artesanal and the rest).
  - DPW2's named forms Caerphilly, Cheshire and Lancashire under the catch-all are superseded: the names become the kinds (with C9 aliases).
- Cheese key amendment (fixes the gap DPW2 noted): a soft, natural-rind ripened cheese that is neither bloomy nor washed is tested with J3.4.6 at the firmness step. So tortas file under J3.4.6.16. Évora and Nisa (firm) stay in the catch-all.
- Goat and sheep cheese: a generated side entry from the attribute `milk_species`. Decision: display_only.
- Raclette and fondue: a use view from the attribute `cheese_use`. Decision: display_only.
- World Cheese Awards, Great Taste, Slow Food Presidia, Stiftung Warentest and Ethical Consumer become scheme rows. Decision: needs.
- US egg housing labels become a grading_scales classification. Decision: needs.
- `season` is an attribute on cheese named forms where a specification gives months. Decision: attribute.
- Noted: Red Leicester and other territorials not in data may become kinds at harvest, at the same level.
- Designation rows of the moved forms take the new kind_id (designations.kind_id follows the named form).

## J4
Built. Points decided:
- `season` is an attribute (months at best, ranges start–end, scope hemisphere or origin region) on kinds, varieties and named forms. It feeds the in-season view. Decision: attribute.
- The variety fields `taste`, `use`, `keeping` and `picking_season` are attributes on varieties. Their value lists are provisional until the Orange Pippin filters are fetched. Decision: attribute.
- Sea vegetables stay in J4.4 (J-10) and are shown as G-J4-26. This is provisional until a page shows fresh or frozen seaweed sold. Dried seaweed is J5.10.1.02 and is cross-linked. Further fresh sea vegetables are noted for harvest; samphire goes to stems and shoots. Decision: display_only, noted.
- New herb kinds, in group G-J4-23: J4.3.08 Dill, .09 Rosemary, .10 Sage, .11 Chives. Garlic chive stays in alliums. Herbs now hold 11 kinds plus mixed, not past 12, so no leaf yet. Decision: new_kind.
- A one-off vegetable box is covered by the mixed kinds (J4.0.01, J4.2.0.01). A recurring box subscription is I3. Decision: covered, other_category.
- The RHS Award of Garden Merit becomes a scheme row on cultivar named forms. Decision: needs.

## J5
Tree nodes are built, kinds are not. Notes for the build:
- Load the memo's section 13 kind ids (frozen tree audit/KL_J5_tree.md) into data/kinds.tsv before any group is applied. † kinds wait for attestation (R-96 c).
- Owed: an OG/GR pass for J5.
  - Designations: balsamic DOP/IGP, olive-oil PDOs, San Marzano DOP; one-kind ones are named forms (JC1).
  - Grading scales: EU olive-oil categories, JAS 1703, ISO 3632, UMF/MGO, USDA nut grades, the Japanese rice ranking (needs file).
- Attributes: `harvest_date`, `broken_pct`, `grain_length_mm`, `moisture_pct`, `additive_free`, and `certification` (organic | non-GMO | regenerative organic | fair trade).
- Schemes: Great Taste (shared with J3), NYIOOC (provisional), Olive Oil Times ranking, Slow Food Ark of Taste and Presidia. The COOC seal and the APEDA basmati minimum are standards.
- Flour (J5.1.4) shown with baking and stocks (J5.9.5) shown with spices and salt: display only. The tree placement stands, and a later blind test may revisit it. Decision: display_only.
- Tinned fish and meat in G-J5-6: cross-links to J2.4 and J1-D only, with one home each. Decision: display_only.
- Dried seaweed J5.10.1.02 is cross-linked from J4 G-J4-26.

## J6
Not built. Notes for the build:
- Build the memo's section 10 tree (41 kinds, ids by R-58 at build). Groups G-J6-1 to G-J6-25 follow the proposal.
- Cup of Excellence thresholds (87+, 90+ Presidential) are on a fetched page. The dagger can be lifted at the sourcing check. Decision: noted.
- Coffee varieties (Geisha and others) go into the varieties table (JC7) with a harvest. A variety is never a kind.
- Specialty grade: the attribute `specialty_grade` plus a grading_scales row (SCA score with the 350 g defect gate). Decision: attribute, needs.
- Decaf is the attribute `decaf`, never a kind (JC4). Certifications are an attribute. Direct Trade is a platform tag (C4 vi).
- Coffee syrup is not a J6 kind (J5 flavouring or syrup leaf). Tasting sets follow the sets rule (item of greatest value). Decision: other_category / covered.
- Herbal infusion markers are provisional: no evidence was fetched. Decision: noted.
- Tea capsules stay unattested and J-14 stays open. Decision: noted.

## J7
Not built. Notes for the build:
- Build the memo's section 10 tree, including the 17 CV-40 designation kinds. Groups G-J7-1 to G-J7-26 follow the proposal.
- Official classifications have fetched pages, so the dagger is lifted for scheme entry. Decision: noted.
- Crus:
  - Bordeaux 1855 and Saint-Émilion classify estates, so they are tier entries on makers (schemes in the needs file).
  - Burgundy grand and premier crus and Alsace grands crus are vineyard designations: non-maker named forms of the grape kind carrying `designation_id` (J-16), with the attribute `cru_class`.
- Whisky attributes: `chill_filtered`, `added_colour`, `single_cask`, `cask_strength`, `cask_type`. Spirits get a `flavour_profile` vocabulary (two values attested, the rest from the fetched shop list).
- Beer kinds are seeded from the BJCP 2021 guidelines (standard row; the fetched page is the 1999 list). The six memo style kinds stay, and further BJCP styles enter as kinds on a fetched page.
- Community beer scores are shown relative to style. Decision: display_only.
- Mead and cider stay in J7.3 (memo), with cross-links from the BJCP style list. Decision: display_only.
