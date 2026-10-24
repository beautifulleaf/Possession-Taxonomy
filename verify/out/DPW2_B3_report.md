# DPW2_B3: B3 Lighting, second decision pass

Offline pass. Inputs: the "missing kind?" lists of MKH_B3_EUR and MKH_B3_NAO, plus grow light and troffer from the prompt. HV_B3_NK lists none, and MKH_B3_ASIA has no report. Named forms reviewed: the 23 added since DPW1.

## Missing kinds (21 rows)
- **new_kind 3** (each waits for attestation):
  - B3.5.06 LED strip profile (channel), a part of the strip light (S3).
  - B3.3.4.03 Mobile light tower.
  - B3.1.1.05 High-bay light (C12 M(a)).
- **covered 6:** aluminium profile (B3.5.06), pole sold alone (B3.5.02 lamp base), low-bay (B3.1.1.05), troffer (B3.1.1.04), wall pack (B3.1.4.05), canopy light (B3.1.1.01).
- **attribute 3:** salt lamp (material), solar street light (power source), tunable luminaire (light colour).
- **named_form 1:** balloon light under B3.3.4.03. It has no URL yet.
- **other_category 8:** grow light and pool light C2; marine light G1; obstruction and heliport lights C8; sign lighting B4; ceiling fan with light B7; medical luminaire H2.

## Named forms (6 of 23 flagged)
- **to_line 2:** the MITTLED and KÖLVATTEN rows repeat existing lines. Each line gains B3.1.3.04, which closes the DPW1 follow-up.
- **drop 4:** duplicates of stored rows (Mini Maglite, Mag-Tac, Maglite Solitaire, Source Four).
- **move_kind 0.**

## Scope calls (task 3)
- **Troffer: in B3.**
  - The key's step-30 test reads "of any capacity, domestic or commercial", and market is an Appendix A modifier.
  - R-108 and R-109 narrow maker harvests, not kinds.
  - A person can own one and fit it in a home drop ceiling.
  - It is covered by B3.1.1.04, because it swaps with an LED panel in the same grid slot (C10(b)).
  - Proposed wording, id unchanged (R-58): "Flat or shallow ceiling fitting set in a suspended-ceiling grid module or surface-mounted, giving an even spread of light; the troffer is this kind."
  - Add an alias row: troffer, US regional name (C9, C11).
- **Grow light: C2.** This is decided by function, not market: step 29 comes before step 30 (memo 9.3, C-14). A full-spectrum lamp not sold for plants stays B3.
- **Other commercial fittings:** high-bay, wall pack and canopy lights stay in B3 on the same test. Their makers stay hidden without a named form or line (R-109a).

## Findings for the apply step
- About 50 grow-light makers are tied at category level B3. Re-tie them to C2 at the C2 harvest.
- All 2,837 category-level B3 maker_kinds rows carry the note "listed as a clothing brand or designer". This looks like the A1 loader default, and the notes need rewording.
- HV_B3_NK says IKEA calls SKYDRAG and IRSTA "strips". DPW1 moved them to B3.1.3.04 on rigidity, a fact taken from memory (†). Recheck against a fetched page; it is not decided again here.

## Rules applied
Key steps 2, 29, 30, 32 and S3; Appendix A; C2(b)(d), C6, C9, C10, C11, C12; R-58, R-108, R-109; K-17, K-176, K-190, K-192; memo 9.3–9.5, 9.10, 9.14.
