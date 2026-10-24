# DPW2_J3 report (J3, second decision pass; offline Opus)

Inputs: DPW1_J3 outputs; the MKH_J3_ASIA/EUR/GS/NAO and HV_J3_NK reports; the items in the prompt; OG_J3_EU/ROW and GR_J3 missing-kind lists (coordinator); J3 rows in data/ (83 kinds, 690 named forms, 585 reviewed here).

## Task 1: missing kinds (72 rows)
Decisions: new_kind 28, named_form 35, covered 5, attribute 1, other_category 3 (Yakult-type and flavoured milk are OUT by K-56; dairy-free butter goes to J5 by K-53).

New kinds:
- J3.4.1.08 Fresh white cheese (queso fresco), J3.4.1.09 Grilling cheese, J3.4.1.10 Brown whey cheese (brunost)
- J3.4.2.03 Brined white cheese, J3.4.2.04 Brined stretched-curd cheese (sulguni)
- J3.4.3.04 Kashkaval (kaşar), J3.4.3.05 String cheese, braided or wound, J3.4.3.06 Moulded smoked scalded-curd cheese (oscypek)
- J3.4.4.03 Bloomy-rind soft cheese (generic), J3.4.4.04 Lactic soft-ripened cheese (crottin type)
- J3.4.5.02 Washed-rind cheese (generic), J3.4.5.03 Sour-milk cheese (Harzer, Handkäse)
- J3.4.6.07 Raclette, J3.4.6.08 Semi-hard pressed cheese (tomme and farmhouse types), J3.4.6.09 Colby, J3.4.6.10 Monterey Jack, J3.4.6.11 Skin-ripened cheese (tulum), J3.4.6.12 Fontina, J3.4.6.13 Asiago, J3.4.6.14 Tilsit
- J3.4.7.05 Roomi, J3.4.7.06 Cotija, J3.4.8.06 Rushan
- J3.3.09 Fermented baked milk (ryazhenka), J3.5.05 Liquid egg, J3.5.06 Dried egg, J3.7.1.05 Walnut drink, J3.7.1.06 Peanut drink

Seven kinds have no harvest URL, so they go to attestation: J3.4.3.06, J3.4.4.03, J3.4.4.04, J3.4.5.03 and J3.4.6.12–14.

Named forms (not kinds):
- Under fresh white cheese: panela, queso blanco, Minas frescal, kesong puti, dangke, Chilean quesillo, cheese curds
- Under string cheese: Oaxaca, dil, örgü
- Under processed cheese: requeijão, Catupiry and cold-pack cheese
- Under the semi-hard generic: Caerphilly, Cheshire, Lancashire, mantecoso and Muenster
- Under grilling cheese: coalho and juustoleipä
- Single placements: rubing (paneer), kajmak (clotted cream), fromage blanc and frais (quark), brick (washed-rind generic)

## Task 2: named forms (51 flagged of 585)
- **move_kind 34:**
  - 18 white cheeses go from feta to J3.4.2.03.
  - Sulguni goes to J3.4.2.04.
  - 13 rows leave Mixed cheeses, which K-46 keeps for selections only.
  - Abbey Blue Brie goes to blue.
  - Half-and-half goes to single cream.
- **drop 14:** 8 duplicates of stored forms, 2 medical formulas (H2.8), 4 flavoured or sweetened drinks (K-56).
- **to_line 3:** Lurpak, Soyog and Zhenweiai.
- **Left on Mixed cheeses:** 10 rows whose type no page shows (H001–H004, H008, H009, H011, H012, H016, H020, H023). De Vinch and Hokkaido 100 become lines once their kinds are shown.
- **For the maker pass:** fix M-pnar to M-pinar-sut-urunleri; the Davidstow and Keens rows are duplicated, and the old rows lack makers.

## Task 3: scope calls (R-111)
- **Brined white cheese is a kind of its own (J3.4.2.03).** It is sold as "white cheese" in TR, the Balkans, EG and the Gulf. Feta keeps the cheese sold as feta. Ezine, Lighvan and all beyaz peynir rows move to the new kind.
- **"Georgian pickled cheese" is not a kind**, because a region never names one (C11). Its members are filed by form:
  - Sulguni gets its own brined stretched-curd kind (key step 5 before step 6), so it is no longer mozzarella.
  - Imeruli goes to J3.4.2.03, guda to tulum, and chechili and tenili to string cheese.
- **Wording to widen (ids unchanged, R-58):**
  - J3.4.7.04 becomes "Hard Alpine cooked-pressed cheese (Comté, Beaufort, Bergkäse)".
  - J3.4.7.02 becomes "Pecorino (hard sheep's-milk cheese)".
  - J3.4.1.06 becomes "Ricotta (whey cheese)".
  - J3.4.1.03 paneer loses "of South Asia".
  - J3.4.10.01 adds requeijão and cold-pack.
  - J3.4.2.01 feta adds "sold as feta".
  - J3.4.2.02 halloumi is for cheese kept in brine; a grilling cheese without brine is J3.4.1.09.
- **Precedence:** ryazhenka is tested after soured milk; out-of-shell egg products are tested first in Eggs.

## Designations (coordinator)
`verify/out/DPW2_J3_designation_kinds.tsv` assigns all 244 ids (EU 174, ROW 67, GR 3) to a kind. The largest groups are semi-hard generic 76, washed-rind 20, Alpine hard 19, brined white 19, lactic soft-ripened 16 and Pecorino 13. Two ids are cut off at source (`DS-gr-` for Xygalo Siteias and `DS-jp-` for Tokachi Raclette).

## Rules applied
C2(a)–(c), C11 (including the two-region tie-break), Rule P(1)/(3), JC1, JC4, K-46, K-53, K-56, K-57, H-11, R-58, and DPW1's generic-blue and chèvre calls.

## Decisions resting on † claims or memory
- Moved from memory: Sakura cheese to bloomy, Hollandia as a sweetened drink.
- Read from memory: the brine status of sulguni and coalho, and the Ukrainian bryndza as brined.
- Placed from memory: the designation style calls with no style hint.
- The two-region level is still unattested for Colby, Monterey Jack, Roomi, Rushan, oscypek and tulum.
- Gap in the cheese key: soft, natural-rind thistle-rennet tortas (Serra da Estrela, La Serena) fall through it. They are filed under the semi-hard generic for now.
