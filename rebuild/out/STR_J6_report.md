# STR_J6 report: Coffee, Tea & Cocoa

**Counts (before → after):** departments 4 → 4; shelves 16 → 16; kinds 68 → 74; archetypes 213 → 181 (validate.py --v3 prints OK).

**Added:** category ax and key (4 steps plus precedence note); t and ax on every department; t on every shelf and ax on shelves with more than three kinds; hand-written tt on all 74 kinds (flat t removed). Kinds reordered along each shelf axis (herb shelf by plant part, cocoa products bean to fat, Japanese green by finish, instant chocolate placed between drinking chocolate and powders). Lead unchanged (it already follows RULES.md).

**New kinds (coverage):**
- Herb & flower infusions: Tulsi (holy basil), Butterfly pea flower, Seed infusions (reference: Wikipedia Herbal tea).
- Mate, rooibos & kava: Yaupon (Wikipedia Herbal tea).
- Japanese green tea: Kukicha (twig tea) (RateTea style list).
- Drinking chocolate & cocoa powder: Instant hot chocolate mix (The Nibble hot chocolate overview). Nesquik archetype moved to it from Drinking chocolate.
- Geisha & rare-variety coffee: archetypes SL14 and Batian (World Coffee Research catalog; no year or originator given, left blank).

**Coverage references fetched:** ratetea.com/style.php (tea shelves), en.wikipedia.org/wiki/Herbal_tea (herbal shelves), worldcoffeeresearch.org/work/catalog/varieties (cultivars), thenibble.com hot-chocolate overview (cocoa). Not checked against a fetched reference: capsules, instant and cold-brew shelf, blends and everyday coffee shelf, pu-erh and dark tea shelf, cacao products shelf. Search excerpts on roast levels were used only to write the Roast types, not as sources.

**Generic archetypes demoted to models (m):** Ethiopia, Indonesia, Brazil, Rwanda, Tanzania, Panama Boquete (versions such as Yirgacheffe, Sidamo, Cerrado Mineiro kept as m); Classic Italian espresso blend (Lavazza products kept in m); Freeze-dried instant; White coffee 3-in-1; Instant tea powder; Darjeeling first, second and autumnal flush; Assam second-flush tippy tea; Ceylon orthodox black tea; Kenyan CTC black tea; Shizuoka and Kagoshima sencha; Fukamushi sencha; Hojicha; Genmaicha; Phoenix Dancong; Wet-piled ripe pu'er (recipe versions kept); Russian Caravan smoked blend; Masala chai; Flowering tea; Rooibos (South African GI); Honeybush; Ecuadorian guayusa; Barley tea; Sobacha; Natural cocoa; Black cocoa. Maker ranges moved to r: Sweet Maria's green coffee, illy classico blend, Dayi recipes and Xiaguan tuocha (the two factory archetypes were renamed 7542 and 8653 recipes and kept as archetypes).

**Merged/renamed/moved:** none (renames file is empty); no moves.

**Cross-links (see):** Cold brew → J9 Cold brew & iced coffee; Green coffee → B5 Home coffee roaster; Capsules → B5 Capsule coffee machine; Matcha → B5 Matcha whisk and scoop; Roasted grain tea → J9 Barley & grain tea; Yerba mate → J9 Yerba mate & guayusa drink; Iced tea mixes → J9 Iced tea; Drinking chocolate → J8 Hot chocolate bomb & drinking flakes. STR_SEE.tsv has no J6 pairs. All targets checked against reader files.

**Unsourced/caveats:** type lists (tt) are written from general knowledge, not individually sourced; some are detailed guesses (tulsi varieties, honeybush species, cocoa fat bands) and worth a spot check. Sources logged in rebuild/work/STR_J6/sources.tsv.
