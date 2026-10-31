# STR_H1 structure report: Personal Care & Beauty

**Counts (before → after):** departments 7 → 7; shelves 27 → 32; kinds 152 → 162; archetypes 349 → 315. `validate.py --v3` prints OK.

**Category:** added `ax` and a 7-step `key` with a precedence note (head clippers and depilatories sit in Shaving & hair removal; tinted moisturiser is a foundation when sold for colour). The lead did not contradict RULES.md and is unchanged.

**Departments and shelves:** every department has `t` and `ax`; every shelf has `t`, and `ax` when it holds more than three kinds. Kinds are ordered along each shelf axis (for example make-up by layer, styling products by hold, razors oldest first), not alphabetically.
- Skincare: new shelf "Facial tools & devices" (gua sha, devices).
- Hair: "Hair colour & wigs" now also holds relaxers.
- Oral care: the single shelf became Brushes, Pastes & rinses, Between the teeth, Tongue & dentures.
- Comfort & massage: split into Massage and Warmth.

**Kinds:** every kind now has hand-written `tt` (axis-labelled groups) in place of the flat `t`. Kinds without a flat `t` (baby items, such as Potty and Dummy) stay without `tt`.
- Renamed (in `out/H1_renames.json`): Hair oil → Hair oil & serum; Bath salts → Bath salts & bubble bath.
- Split: base coat, top coat and polish remover out of Nail polish types; after-sun dropped from Sunscreen types.
- Added, each with a fetched source: Facial oil (Skin care), Base coat & top coat, Nail polish remover (Nail polish), Hair relaxer (Hair straightening), Headband, Teeth-whitening strip (Tooth whitening), Toothpick, Tongue scraper, Denture cleaner (Oral hygiene), Hand sanitiser, Cotton bud (Cotton swab), Electric heating pad (Heating pad).
- Moved out: none. No kinds were merged or dropped.

**Generic archetypes demoted (34):**
- Types, in `tt`: Gua sha board, Jade roller, Acrylic sculpted nail, Emery board, Glass nail file, Sindoor, Kumkum, Tilaka, Kohl, Surma, Kajal, Tiro, Mehndi, Arab and Maghrebi henna, Painted bindi, Sticker bindi, Lace front wig, Full lace wig, Toupée, Clip-in and tape-in extensions, Two-plate flat iron, Military brush, Claw clip, Bobby pin, Scrunchie, Kamisori, Kese, Loofah.
- Models, in `m` with their versions: Sheet mask (My Beauty Diary), LED light therapy mask, MAC Eye Shadow (single), Magnetic lashes, Shampoo bar, Japanese nylon body towel.
- Ranges, in `r` (versions to `m`): Raquel Welch Signature Collection, Jon Renau SmartLace, Transformations top pieces, Reuzel colour-coded pomades, Böker straight razor, Noble Otter and Stirling shave soaps.

**Coverage references fetched:**
- Skincare: Wikipedia Skin care.
- Make-up: Wikipedia Cosmetics, Nail polish.
- Hair: Wikipedia Hair care, Hair straightening, Headband.
- Shaving: Wikipedia Razor (all its razor types are already kinds).
- Oral care: Wikipedia Oral hygiene, Tongue cleaner, Tooth whitening, Toothpick.
- Bath: Wikipedia Hand sanitizer, Cotton swab.
- Comfort: Wikipedia Heating pad.
- Details are in `work/STR_H1/sources.tsv`.

**Cross-links added (27 kinds carry `see`):** the three required pairs (Period underwear → A1, Highlighter → C5, Primer → E4) plus Headband and Hair clip, Hair towel, Bindi, Toiletry bag, Grooming mirror, and pairs inside H1. Every target was checked to exist.

**Not sourced / left out:** Facial oil had no page of its own (404), so it cites Skin care. After-sun, cuticle oil, body powder, foot spa and temporary tattoo found no usable fetched page and were not added. Perm kits were not added: the fetched page does not define perms.
