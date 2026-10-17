# KLFIX1 report (2026-10-17)

Memos edited (backups in verify/work/KLFIX1/; section-12 entry "Kind-level test fixes (KLFIX1)"). Trees: verify/out/KL_<CODE>_tree_v2.md, ids kept.

## B8-27, B8-30 (Nomat)
Under rule T (C10), power and heat are attributes. A repeller uses no chemical. Expected kinds are unchanged.
- B8.4.3.6: "a plug-in heater that vaporises a liquid or mat insecticide refill" becomes "a powered unit, plug-in or battery, that releases insecticide into room air from a liquid, mat or cartridge refill, by a heater or by a fan without heat".
- B8.4.4.1: "a plug-in device that emits ultrasound or similar" becomes "a powered device that drives pests away by ultrasound or similar signals alone, with no insecticide or chemical refill".
- B8.6.3: "in one electric vaporiser" becomes "only in one maker's electric vaporiser units". Also new: rule 13 and memo §9.13.

## A2-26 (Kolhapuri)
Under F14 the Kolhapuri is already a flat strap sandal. Expected kind is unchanged.
- A2.4.01: "held by a strap between the toes" becomes "held only by a toe post … and the strap from it to the sides of the sole, with no other strap across or round the foot".
- A2.4.03: "straps across and round the foot" becomes "… including one that adds a toe loop or toe post to a strap across the foot (T-strap)".

## A2-28 (UGG Tasman II)
The expected answer is wrong:
- The edge-5/A-11 construction test files a moulded outsole outside Slippers.
- The builder's KL-A2-11 (UGG, backless, EVA) is a mule.
- Under R-64, "slipper" is the seller's alias.

Leaf 2.2 had no backed kind except loafer and moccasin.
- Slippers: "without a rigid outsole" becomes "without a rigid or moulded outsole: the sole is a thin, flexible layer of felt, fabric, leather, suede, foam or thin rubber".
- New kind A2.2.2.07 Plain slip-on shoe †: "laceless low shoe with a closed heel over a covered instep, on a moulded or stitched outsole, built as none of the kinds above".
- **Item:** KL-A2-28 changes from A2.5.01 to A2.2.2.07. It is backed and laceless, on a moulded EVA outsole.

## A2-07 (Dr. Martens 1461)
Item fault, already fixed. New rule: "A seller's style word … is a name, not a test … Oxford against Derby is decided by the lacing."

## G2 (wording only)
- 04/06 (G-13): principal use is "more than half of the holding's area". "A house with a garden" becomes "A house whose land is garden and grounds, or mostly so". Mixed holding: no use covers more than half, or areas are not given and the uses are several.
- 13 (G-16): lodge "twin-unit or wider" becomes "two or more sections joined on the pitch". Static caravan: "one section … whatever its width". Rule 20.
- 16 (K-63): the dwelling test applies "whatever it is sold as".
- 18: gazebo "roofed" becomes "with a roof (boarded, shingled, tiled or a fixed canopy)". Pergola: "side curtains … do not make it a gazebo".
- 21: garden log cabin is "not fitted for one purpose". Garden bar: "whatever its walls".
- 24: stable block "building of stalls" becomes "floor laid out mainly as stalls … even when sold as a horse barn".
- 25: workshop "making or repairing things" becomes "repair or craft work, domestic or commercial". Industrial unit: "producing goods".
- 30: green burial plot includes "one of several sites at a shared tree". Communal grave space: "no separate site for each".

Rules 21 to 24 restate these.

## Expected-kind changes
Only KL-A2-28, from A2.5.01 to A2.2.2.07, through a tools/kl_prepare.py fixitems entry. The v2 trees parse with tree_kinds: A2 has 63 kinds, B8 88, G2 55.
