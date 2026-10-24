# DPW1_D3 report: D3 Audio & Video decision pass (offline)

## Task 1: missing kinds (43 items)
Sources: the HV_D3_1 and HV_D3_2 lists, split into single items, plus 5 wave-3 items from fetched.tsv and the harvested rows. There is no DPMK_1_D3 file. Counts: new_kind 16, covered 15, attribute 7, other_category 5.

New kinds (next free id, checked against data/kinds.tsv and TREE_D3_map.tsv):
- D3.2.2.04 MiniDisc deck, D3.2.2.05 DAT deck, D3.2.2.06 Reel-to-reel tape deck, D3.2.2.07 8-track player (D3.2.2 is split by carrier)
- D3.2.3.04 Movie server
- D3.2.4.02 Portable cassette player, D3.2.4.03 Portable CD player
- D3.3.2.03 Multichannel power amplifier, D3.3.2.04 Video processor
- D3.3.3.05 Bluetooth audio transmitter or receiver, D3.3.3.06 Equaliser or sound processor, D3.3.3.07 Master clock
- D3.4.1.08 On-wall speaker
- D3.8.13 Turntable plinth, D3.8.14 Earbud charging case (no page was fetched, so source_url is empty; it needs an HV_NK batch), D3.8.15 Headphone stand

Other categories: studio monitor and DJ turntable go to E3 (K-143), distribution amplifier to D1 (D1.7.09), power conditioner to C8 (step 32 branch 2), record-cleaning machine to F1 (S3).

Attributes: CD transport, SACD and CD recorder (all on D3.2.2.01), outdoor speaker, portable radio (D-18), laser TV (a C3 bundle on D3.1.2.02) and premounted cartridge.

D3.8 now has 15 kinds, past the "about 12" in CV-17. The next tree revision should open leaves by object served.

## Task 2: named forms (4 of 700 flagged)
- **to_line:** NF-D3.1.3.02-001 Kodak KodaScope becomes L-kodak-kodascope, a range of models.
- **move_kind:**
  - Sony DTC-60ES goes to D3.2.2.05 (DAT).
  - FiiO DM15 goes to D3.2.4.03 (portable CD player).
  - These two wait for their new kinds.
  - Sonos One goes to D3.4.1.07: voice is a modifier (D-14), and its successor, the Era 100, is filed there.

No drops: there are no duplicate names, and every row is a model under the owner role.

Noted, not flagged:
- **K-143 check needed.** These may be sold by their makers as studio or DJ gear and would then be E3; a maker page is needed to decide:
  - the beyerdynamic Pro lines, ATH-M, Shure SRH and AKG Pro headphones;
  - Sony MDR-7510 and MDR-CD900ST, and the IER-M series;
  - Neumann NDH 20;
  - Koss Pro DJ100;
  - the TASCAM 122mkIII deck.
- **Open-ear wireless earbuds.** Shokz OpenFit, OpenDots and Moondrop Pill are true wireless open-ear earbuds, filed at D3.5.2.05. ACCENTUM Open, an in-concha earbud, is at D3.5.2.04. A precedence sentence is needed. Proposal: an open ear canal outranks true wireless.

## Task 3: navigation
I confirm R-116 (proposals.tsv D3): the way in is by device type, in shoppers' order, with headphones first.
- **Device type:** 127 of 148 makers have named forms in one sub-family only. Only Sony (6) and Denon (5) span more than four sub-families. That argues against opening by brand.
- **Headphones first:** headphones and earphones hold 215 of the 700 named forms, the largest aisle.
- **No scene way in:** no D3 scene tags are harvested.

View:
1. **Level 1:** Headphones and earphones; TVs and projectors; Speakers and soundbars; Hi-fi amplifiers and DACs; Turntables, players and streamers; All-in-one systems and radios; Smart speakers and displays; Parts and accessories.
2. **Level 2:** the memo leaves (for example Headphones and Earphones; Televisions, Digital projectors, Film and slide projectors). D3.7 and D3.8 show their kinds directly.
3. **Level 3:** kinds, then named forms by maker. Use is a facet.

Side views: a brand tab for headphones, hi-fi separates and turntables; Home cinema; By display technology.

## Rules applied
- C2(b) and (d), C3, C5(b) and (d).
- S3 (step 8), K-1, K-2, K-3, K-8, K-143.
- D-14, D-15, D-18.
- R-58, R-70(d), R-116, R-122(c).
- Memo sections 3.5, 9 and 14.

## † claims (product facts not on a fetched page)
- Kodascope being a range.
- DTC-60ES being DAT.
- DM15 being portable.
- What "digital processor" means on Vintage Technics.
- The CD Soundmachine handle.
- Record cleaners going to F1, which rests on an S3 reading the F1 memo must confirm.
