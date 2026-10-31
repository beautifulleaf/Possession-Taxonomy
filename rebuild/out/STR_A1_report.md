# STR_A1 report: A1 Clothing structure pass

**Counts (before → after):** departments 9 → 11; shelves 32 → 43; kinds 227 → 255; archetypes 759 → 694. validate.py --v3 prints OK. Category `ax` and 11-step `key` added; `lead` reworded only to match the new departments. The scenes list and `_moves.json` and `_brands.json` are unchanged.

**Departments:** "Dresses, skirts & sets" split into "Dresses" (shelves by silhouette) and "Skirts, jumpsuits & sets"; "Hats, scarves & accessories" split into "Hats & headwear" (brimmed, caps and knits, head wraps, regional/ceremonial/uniform) and "Scarves, gloves & belts" (neck, hands, waist).

**Kinds split/merged/renamed:** Jeans (22 archetypes) → Heritage American, Selvedge reproduction, Fashion & designer jeans (models carried by maker). Skirt → nine silhouette kinds. Shorts → Shorts, Bermuda shorts, Denim shorts & cut-offs, Hot pants. Fedora & trilby → Fedora, Trilby. Morning dress & tailcoat → Morning dress, Tailcoat. Casual jacket → Leather & suede jacket (Pendleton 49er moved to Overshirt). Formal accessories → Cummerbund & collar stay. All 227 old kinds are placed; none dropped.

**Added (reference: Wikipedia pages fetched, logged in sources.tsv):** Skirt page → nine skirt kinds, Culottes; Trousers → Harem pants, Capri pants; Jacket → Norfolk jacket, Bolero, Donkey jacket; Dress → Wedding dress; Lingerie → Slip & petticoat, Suspender belt; Swimsuit → Rash guard; Scarf → Bandana, Neck gaiter; List of hat styles → Visor; Cricket clothing → Cricket shirt. Hat styles, Shirt and Jersey pages showed no further gaps.

**Demoted generic archetypes (65):** e.g. Ball gown, Cocktail dress, Waistcoat types, Prairie skirt, Letterman jacket, Shell suit, Traditional Aran/Guernsey/Lopapeysa, Silk top hat; folded into types, aliases or kind definitions. Archetypes moved: Cowichan-style cardigan, Pendleton 49er, Paisley bandana.

**tt:** every kind has hand-written typed groups; groups listing named garments were rewritten as attribute groups.

**Cross-links:** Hakama → E2 Hakama; Period underwear → H1 Period underwear; about 40 intra-A1 `see` links (Puffer coat/jacket, Bodysuit/Baby bodysuit, Tracksuit/Joggers, etc.).

**Not done / caveats:** Firecrawl was out of credits, so WebFetch was used. American football jersey was not added (no fetched source). Collar stay kept merged with Cummerbund (no fetched source). Each coverage check was against a single Wikipedia page per shelf, not a specialist retailer; Traditional dress and Workwear shelves were not re-checked against an external list. Réard bikini, Monokini and similar archetypes still lack `mk`.
