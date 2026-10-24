# DPW1_G2 report: G2 Property & Structures (offline)

## Task 1: missing kinds (57 rows)
Inputs: 49 HV_G2_1 items, 8 "gave"-column types; no DPMK_1_G2.

Counts: named_form 23, new_kind 12, covered 10, attribute 7, other_category 5.

**New kinds** (R-58 next free ids; each has a logged full URL):
- **New leaf G2.1.8 Other land by principal use** (it mirrors G2.3.7):
  - .1 parking space, which settles the open K-67 bay
  - .2 golf course
  - .3 campsite
  - .4 solar farm
  - .5 wind farm
  - .6 airstrip
- G-12 (kinds stop where portal filters stop); memo §4 expects 12–25 Land kinds, now 8. **Node G2.1.8 must be added to data/nodes.tsv before apply_dp.**
- G2.3.3.6 garden kitchen (filed by purpose, like the garden bar)
- G2.3.3.7 shepherd's hut (with a dwelling-test clause)
- G2.3.4.5 field shelter
- G2.3.5.6 patio cover (made for a wall mount, C12a)
- G2.3.7.6 data centre
- G2.3.7.7 bunker

**Other categories:** allotment OUT; porches and canopies C8; log, bin and bike stores B1.

**Main calls:**
- Attributes or tags: ruins, retirement and sheltered housing, wedding venue, kennels, anonymes Grab.
- Pub: named form under hotel (memo "finer function"; portals' Hotels and Leisure).
- Island and peatland are Land named forms.
- Urn pedestals, benches and boulders are niche forms, like the Urnenstele.

## Task 2: named forms (12 rows)
- **to_line (1):** Dunster "Utopia" becomes L-dunster-house-utopia, covering gazebo and pergola. NF-G2.3.5.2-001's line_id must be set by hand.
- **drop (9):**
  - C9 aliases: Townhouse, Chalet (Spain), Pareado, Adosado, Dúplex, Triplex
  - German allocation and capacity values (memo §7): Einzeltiefgrab, Mehrfachwahlgrab, Reihengrab
- **move_kind (2):** Timberlyne Poppy and Gunnar are horse-barn kits, so they move to stable block (rule 23). This rests on the row notes.

## Task 3: navigation
**Confirmed: R-116, by type of property.** Location is a filter, never a level.

Every harvested catalogue divides by type. Of the 216 named forms, 175 are factory-built models from 19 makers in 16 kinds, so a makers' ranges tab fits those groups only. The other 41 feed the "by tradition" view.

The first three levels:
1. **Houses and flats.** Houses (detached, semi-detached, terraced); flats and maisonettes; whole buildings.
2. **Park, mobile and floating homes.** From least to most fixed, plus a makers' ranges tab.
3. **Land and farms.** Plots; farm land; woodland; water; mixed holdings; new group "Leisure, energy and parking land" (G2.1.8).
4. **Garden buildings and outbuildings.** Garages and carports; sheds and workshops; garden rooms (with garden kitchen and shepherd's hut); barns and stables (with field shelter); gazebos, pergolas, patio covers and decks; pools.
5. **Commercial buildings.** By function, now with data centre and bunker.
6. **Burial places.** Eight kinds.

## Rules applied
C2(b), C3, C9, C12(a), C16, G-12, G-13, K-60, K-62, K-63, K-65, K-67, precedence rules 16, 18, 22–24, R-58, R-116.

## Resting on † or unread claims
- The LandSale kinds rest on its homepage menu; HV_NK should confirm them.
- "Roese" is read as Rosengrab.
- The well house as a shed form is provisional.
