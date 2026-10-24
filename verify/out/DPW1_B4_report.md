# DPW1_B4 report: B4 Decor (Opus decision pass, offline)

**Task 1, missing kinds (28 candidates):** 18 new_kind, 1 named_form, 2 attribute, 4 covered, 3 other_category. Input: the 11 "missing kind?" lines of HV_B4_1 (split into 17 items) and 11 types from the fetched.tsv "gave" column. There is no DPMK_1_B4 file.

New kinds. Each takes the next free id under its parent (R-58; data/kinds.tsv and TREE_B4_map.tsv checked, no ids reused):
- B4.1.1.05 Wall vase; B4.1.1.06 Apothecary jar
- B4.3.1.06 Floating candle; B4.3.2.02 Candlestick; B4.3.2.03 Tealight holder
- B4.4.1.08 Scented sachet; B4.4.2.06 Loose incense [bakhoor] (no logged page, so source_url is empty and HV_NK must attest it)
- B4.5.1.06 Wreath; B4.5.1.07 Christmas stocking; B4.5.2.04 Tree skirt; B4.5.2.05 Advent calendar (reusable); B4.5.3.05 Confetti; B4.5.4.02 Mirror ball [disco ball]
- B4.7.07 Wind spinner; B4.7.08 Garden pedestal or column
- B4.8.1.06 Feather banner; B4.8.1.07 House flag [decorative flag]
- B4.10.02 Ornament hook

Other decisions:
- **Named form:** bakhoor burner [mabkhara], under B4.4.2.04.
- **Attribute:** candle dish (holder_form "candle plate"); table and floor vase (size).
- **Covered:** smoke grenade (B4.5.3.04); banner (B4.8.2.01); garden sign (B4.8.2.02, stake mount); tassel garland (B4.5.1.03).
- **Other category:** tree stand to C3 (S3, K-72); wall hooks to B1 (step 30 lists hooks); hamayumi to F4 (step 14, B4-O2).

**Task 2, named forms (80 reviewed, 6 flagged):**
- Dropped: Bay Keramik "Valencia" (a glaze decor used on many shapes, so a pattern) and Achla "Gazing Globe" (only restates the kind name).
- Moved: IKEA KNAPPER and IKORNNES to the standing mirror B4.2.1.03. Both are free-standing framed mirrors, not leaners, which settles the harvester's caveat. KUNGSTÄRNA moves to the new tealight holder B4.3.2.03.
- To line: Look Viper becomes L-look-viper, because Viper 2.6 and Viper NT are separate models.
- No makers or shops are posing as named forms (maker role owner). The 9 existing lines stand.

**Task 3, navigation:** I confirm R-116's way in, **by type of object**. The harvested data supports it:
- Every shop page that served (John Lewis, IKEA, Target, Spotlight, Dehner, Wayfair, M&S) leads with item type, and colour, material and style are only filters.
- Makers are sparse and incidental (35, all owners of named forms), and named forms cluster in a few kinds (fog machines, fireworks, chimes). That leaves no brand path to lead with.
- Scenes do not apply. The creator-and-period view (1stDibs) stays a side view.

View, seasonal shown first in season:
- L1, display groups: Vases, bowls & ornaments · Mirrors & frames · Candles & holders · Home fragrance & incense · Seasonal & party · Artificial & dried plants · Garden ornaments · Flags & signs · Decorative lighting · Flagpoles & parts
- L2, leaves: for example Candles & holders → Candles / Candle holders / Candle tools. Seasonal & party → Hung & strung / Standing displays / Party consumables / Party effects.
- L3, kinds: for example Candles → container candle, tealight, votive, taper, pillar, floating candle. Hung & strung → bauble, topper, garland, wreath, stocking, bunting, streamer.

**Rules applied:** C2(a) choice level, C2(b) patterns, C2(d) and C1 lines, C6 size, C10 retail facets, C11 rule R, C12 rule M(a) (wall vase), S3 and CV-17 parts, B4-O2 and B4-O3, K-72, K-180, memo 4b and section 14, R-58, R-116.

**Decisions resting on † or thin evidence (provisional):**
- **Candlestick and tealight holder** rest only on the IKEA "gave" summary: shop categories for candlesticks and tealight holders. Under the memo section 14 instruction, that is enough to raise them as kinds. FINSMAK, sold as both, stays at B4.3.2.01, which keeps the other holder forms.
- **Tree skirt, stocking, advent calendar and ornament hook** cite the Old World Christmas ornaments page, which the harvester cited, though its "gave" summary does not name them. HV_NK should confirm each.
- **Rule M trigger:** row NF-B4.2.1.02-005 (Friends & Founders Arc) is noted as "Wall mirror or floor mirror". Memo 4b says one body sold both ways merges B4.2.1.01 and B4.2.1.02 into one kind with a placement attribute. I did not merge them, because that would reopen a structure. The owner or the next pass should check the 1stDibs page first.
- **Data gap:** B4.8.2.02 Wall sign or plaque is marked attested in HV_B4_1_kinds_unattested.tsv but is missing from data/kinds.tsv. It should be loaded, or its status corrected.
