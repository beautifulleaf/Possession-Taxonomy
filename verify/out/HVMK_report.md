# HVMK: missing kinds and lines (A1, D1)

Offline; no data changed. Covers both candidate files and all 1,917 A1 and D1 named forms.

## Task 1: 81 items decided from 48 candidate rows

| Decision | Count |
|---|---|
| new_kind | 37 |
| covered | 21 (4 rewordings) |
| named_form | 19 |
| other_category | 3 (label printer C5, cutting plotter C4, tie bar A3) |
| attribute | 1 (thermal printer) |

**New kinds** (next free number, R-58).
- A1: A1.1.1.03 Tank top, A1.1.2.06 Blouse, A1.1.3.03 Sweater vest, A1.2.2.07–10 (Tailored trousers, Leggings, Culottes, Chainsaw chaps), A1.4.1.17–20 (Work jacket, Flight jacket, Anorak, Field jacket), A1.4.2.06 Overcoat, A1.4.2.07 Parka, A1.5.1.05 Shapewear, A1.6.13–16 (Face shield, Earplugs, Balaclava, Headband), A1.7.09 Pocket square.
- D1: D1.2.7.08 Thermal pad, D1.2.8.05 TV tuner card, D1.4.1.04 Macro pad, D1.4.5.06 Wide-format printer, D1.5.05–08 (Range extender, Powerline adapter, Modem, PoE injector), D1.6.11 DisplayPort cable, D1.8.2.04–08 (Potentiometer, Thermistor, Varistor, Transformer, Crystal or oscillator), D1.8.3.03 Diode, D1.8.3.04 LED, D1.9.12 Add-on board, D1.9.13 Laptop stand.

**Definition fixes.**
- Fleece pullover, pullover sweater and T-shirt: a short neck opening is allowed.
- Kurta: kurti stays an alias, and a kurta set is a named form.

**Rules:** C2(a), C2(c), C11, P14, P16, C10(b), C6, C12, S3, S3a, D-9. MA-1 and M-65 stay; the new jacket kinds take the other patterns.

## Task 2: 345 moves

- **to_line, 270 rows on 262 line ids.**
  - D1 (252): CPU classes, board, GPU, cooler and case series, VENGEANCE, YubiKey, Pico 1, and 186 of 330 laptop rows.
  - A1 (18): collections and series such as Smartwool, Modibodi, V-Gard, Glacier, Powerblend, Beefy-T.
- **drop, 71 rows.**
  - A1 (55): crafts, materials, attribute cuts and necklines, aliases, kind restatements, duplicates, yoroi hakama (E4), a sport sleeve (E2).
  - D1 (16): six tablets or organisers (D2), Alice layout, nine maker-plus-category titles.
  - Weave-named saris and dupattas stay (Shetland precedent).
- **move_kind, 4 rows:** TNF Arctic and McMurdo to Parka, Bump cap to Cap, Neckerchief to Scarf.

## Decisions that rest on † claims

- **Source may not show the type:** TV tuner card, shapewear, track pants, windpants, range extender, powerline adapter, modem, DisplayPort cable, wide-format printer, overcoat, field jacket, anorak, pocket square, face shield, blouse, controller card.
- **Kurta set:** named form, as no second-region page exists (C11).
- **Laptop list:** the range-or-model split and the D2 drops rest on general knowledge.

## Gaps

- Processor and graphics card kinds are left without chip-model named forms, and laptops need a model harvest.
- Cross-kind lines still need `line_id` on fine rows: Hestra, Reverse Weave, Marquette, Barbour International, Rugged Flex, Tech Fleece, Hosa Pro.
- The prompt's other-category examples (hardware wallet, barcode reader) are D1 tree kinds: marked covered.
- Alienware rows mix the M-dell and M-alienware maker ids.
- The kendo hakama against step 17 (kendo gear is E2) is still open.
