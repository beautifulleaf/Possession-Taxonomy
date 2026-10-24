# DPW1_H2 report (H2 Health, Medical & Mobility)

Inputs: 30 split "missing kind?" items (HV_H2_1–3) and 13 fetch-log shop categories; no DPMK_1_H2 file. Outputs: verify/out/DPW1_H2_kinds.tsv (43 rows), DPW1_H2_moves.tsv (38).

## Task 1: missing kinds
new_kind 23, attribute 10, covered 8, named_form 1, other_category 1.

New kinds (next free ids per kinds.tsv and tree map): H2.1.1.4 manual blood-pressure kit; H2.1.3.4 HbA1c home test kit; H2.1.9.1 peak flow meter (new leaf H2.1.9 Lung function); H2.2.1.2 steam inhaler; H2.2.2.3 heat patch sold for pain; H2.2.4.5 penile traction device; H2.3.3.4 mobility vehicle lift; H2.4.1.3 bath lift; H2.4.1.4 tub transfer bench; H2.4.2.5 toilet safety frame; H2.4.3.4 bed rail; H2.5.2.12 electronic magnifier; H2.5.2.13 low-vision monocular; H2.5.3.2 eye-gaze access device; H2.6.9.1 corn and callus remover (new leaf H2.6.9 Skin and foot); H2.8.1.3 protein snack; H2.8.2.4 fat burner; H2.9.2.5 milk collector; H2.10.2.4 tubular bandage; H2.10.2.5 blister plaster; H2.10.2.6 wound-closure strip; H2.10.2.7 liquid bandage; H2.12.6.2 contact-lens rewetting drops.

Empty source_url (no logged page shows them; HV_NK attests): H2.1.1.4, H2.1.3.4, H2.1.9.1, H2.2.1.2, H2.5.2.12, H2.8.1.3, H2.8.2.4 and H2.12.6.2.

**New leaves H2.1.9 and H2.6.9 need node rows first** (apply_dp.py adds no nodes).

Other decisions:
- Covered: transport chair, weight gainer, walkers, bath benches, bath rails, ID necklaces, Lyric.
- Attribute: lozenge (a dose form), bandage materials, and facets of commodes, wheelchairs, readers, canes, stockings and capsules.
- Named form: Soothies, under nursing pad.
- Other category: lift chair to B1 (memo section 14).

## Task 2: named forms (38 of 503 flagged)
- **Drop, 26:**
  - 3 maker names (Elvie, Willow, Lexie)
  - 8 first-aid kits named only by a reference number or a category word
  - 7 RGP lens materials
  - 3 unbranded homeopathic remedies (H-8)
  - 5 size, format, material or colour variants
- **To line, 9:** four custom hearing-aid families that span the ITE and canal kinds, and five model ranges (Optelec, Clinton, JAY J2).
- **Move kind, 3:** Elvie Curve and Elvie Stride to wearable pump; Drive Air-Go to rollator.

## Task 3: navigation
I confirm R-116: by use or need, then product type.
- Walgreens sorts medicines by symptom.
- Drive, Binsons and Affinity sort by task or aid.
- The ADA guide sorts by device type.

Makers matter only inside a type (owner role). A brand tab only for hearing aids, contact lenses, supplements and sports nutrition, where sources list by brand.

First three levels:
1. The twelve need groups of proposals.tsv (Medicines … Parts, refills and consumables).
2. Leaves, for example Mobility aids → walking aids, wheeled seating, transfer and access.
3. Kinds (walking stick … rollator, knee walker), brand products below.

## Rules applied
C2, C3, C6, C10(b), H-2, H-8, H-9, K-31, K-33, K-38, K-39, R-58, R-116, memo §14.

## Resting on † or thin evidence
- The three moves rest on trade knowledge.
- The milk collector rests on one product.
- Corn, heat and spray plasters: the Galaxus page summary names only Compeed and Steri-Strip.

## Data issues
- H2.10.2.3 and H2.11.1.2 are unattested.
- Possible duplicate makers: Signia, Starkey, Ascensia.
- L-cellucor-c4 lacks H2.8.1.1.
