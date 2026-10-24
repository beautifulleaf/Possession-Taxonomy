# Readability and organisation rules (R-126, session 12)

These rules govern what a shopper sees: display names, display groups and the reader page. They sit on top of the tree and never change it: kind ids, kind names in data/kinds.tsv, definitions and one home per object stay as they are. C1 Tools is the exemplar; the other categories follow once the owner approves it.

## Display names (framework/structure/navigation/display.tsv)
1. One name per kind: the name most shoppers in English-language shops use. Synonyms, regional names, native-script names and trade names go to `also_called` (joined by " · "), where search finds them; they are never shown inside the name.
2. Sentence case: a capital first letter, the rest lower case except proper nouns and acronyms (Track saw, MIG welder, CNC router).
3. A bracket stays in a name only when it tells two kinds apart and no plain wording does. Prefer plain wording ("Metal lathe", not "metal (engineering) lathe").
4. A foreign term stays as the name only where shops sell the object under it (Ryoba saw, Dozuki saw); otherwise the English name leads and the foreign term goes to `also_called` (Japanese plane, also called kanna).
5. A name must make sense inside its group without the id; where a bare word is ambiguous (brace, dolly), add the one word that settles it (Hand brace, Moving dolly).
6. No working terms on the reader page: no ids, "named form", "line", "attested", "kind" or source chips. A kind's card shows its name, also-called names, the definition, what makes a good one, and example models by maker; sources sit behind a link.

## Display groups (framework/structure/navigation/groups.tsv)
1. The first level follows how the category's shops split their departments, checked on fetched retailer pages (for tools: power tools, hand tools, workshop machinery, measuring, welding, ladders and lifting, site equipment, storage, accessories; Toolstation, Bunnings). A modifier the tree keeps off the tree (drive: hand, power, machine) may lead the display when shops lead with it; the display is a view, not the tree.
2. Five to nine first-level groups; a second level only where a first-level group holds more than about twelve kinds.
3. No group of one kind; a group of two only when nothing else fits. No group of more than about fifteen kinds; longer runs split by the way shops split them (by size, material or use), or show as an A–Z list only where shoppers search by name (minerals).
4. Group names are shop words, short, with "&" for pairs (Ladders, lifting & moving).
5. Every kind sits in exactly one group.

## Test
Each regrouped category passes a blind findability test before it ships: everyday shopper requests written by one agent from the kind list (never the group names), and a finder agent who sees only the reader structure (group names, display names, also-called, definitions) picks the group and kind for each. The test runs on the old and the new layout with the same requests; the new layout must find more, and every miss is reviewed.
