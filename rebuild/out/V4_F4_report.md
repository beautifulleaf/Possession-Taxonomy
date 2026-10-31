# V4_F4 report: F4 Religious & Ceremonial Objects (named-entry pass)

Validate: `validate.py --v3 rebuild/out/F4.json` OK (154 kinds, 80 -> 102 entries). About 24 fetches; log in rebuild/work/V4_F4/sources.tsv. No market panel (per brief). Moves and renames files unchanged (empty).

## Per kind (entries before -> after)
- **Tarot deck** 6 -> 11, 10 loose models removed. Reference: Wikipedia categories Divination Tarot decks (6) and Tarot decks (2, both pages), plus Tarot playing card decks (15). Complete: 8 of 8 divination pages. Of 21 distinct pages, 10 kept (plus Etteilla from the earlier pass) and 11 game patterns (Minchiate, Tarocco, Tarot Nouveau etc.) left out. Added Swiss Tarot (1JJ), Oswald Wirth, B.O.T.A., Motherpeace, Dalí; sections historical / 1900 onwards; Etteilla origin, Rider-Waite-Smith landmark.
- **Butsudan** 5 -> 15. Complete: 15 of 15 butsudan crafts in the Wikipedia List of Traditional Crafts of Japan (244 crafts; two other rows are ritual implements). Sections by prefecture, year = designation year. Hasegawa maker ranges removed.
- **Hanukkah lamp** 0 -> 5 (from Wikipedia Hanukkah menorah; covers 5 of 15 named lamps; rest are monuments, novelties). 7 retail/museum models removed.
- **Nativity set** 5 -> 8 (7 of 12 named traditions in Nativity scene, plus Alpine crib from earlier).
- **Rosary / Prayer rope / Anglican prayer beads / Mala** +1/+1/+1/+2 from the Prayer beads page (12 named types, all placed across the six bead kinds).
- **Mushaf** 0 -> 2 (Medina Quran, Mushaf al-Tajwid): covers 2 of 31 in Wikipedia Mushaf; the rest are museum manuscripts or text editions (Literature). **Gutka & pothi** 0 -> 2 (Panj Granthi, Das Granthi). Sundar Gutka dropped: no fetched page. The five models parked in Bible were moved here.
- **Reliquary** 0 -> 1 (Limoges enamel chasse; covers 1 of 8 types, rest are single shrines). **Murti** +1 (Ganesha clay murti). 
- All other kinds with entries now carry `nl` and `sel` with a count line (mostly "Covers n forms"; no whole-space reference exists for them).

## Removed as out of scope
- Models (m): all 10 modern tarot decks, 13 oracle decks and Hay House range, Nambé/Yair Emanuel/Waterdale menorahs, Lindo-lamp and Raban models (Lindo returned as an entry), Bier Judaica finials, Sderot menorah, Belem and Diamond monstrances, Frankfurt spice box, Great Buddha of Kamakura (monument), I Ching kit. Oracle deck and I Ching set are now commodity kinds with no entries.
- Art traditions (visual-art taxonomy; kinds kept, d carries the pointer): Icon (4 iconographic types), Thangka (2 styles), Yantra (2 designs), Thuluth panel.
- Single museum objects with no design-collection confirmation fetched this pass: Qajar steel Qur'an case, Mughal jade rehal, Dee's obsidian mirror.

## Register
Added A.G. Müller, J. G. Rauch, Johannes Müller, Builders of the Adytum, Naipes Comas (country only for Naipes Comas, from fetched page). Dropped now-unused HarperOne, Hay House, Nambé, Hasegawa.

## Not sourced
No market data (none requested). Years for B.O.T.A. and Motherpeace are not given by their pages. Several single-article kinds could not be counted against a total; their sel says so. F4_traditions.json was not edited.
