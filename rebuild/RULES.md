# Possession Taxonomy audit — approved rules (owner-approved, binding)

## Goal
A complete, unambiguous, evidence-backed map of everything a person owns, serving two readers:
- **Hobbyists** (things a community compares, collects or argues about): judged on COVERAGE and organisation.
- **Quality-of-life buyers** (things you need to own well but don't study): judged on RESTRAINT — the right kind and what makes a good one, without trade-level detail.
Food categories (J) are about *products*, brands and quality grades — dishes live in a separate Culinary Taxonomy.

## Three audit checks for every category
1. Over-granularity for non-hobbyist items (attribute-only kinds, spare-part lists, near-duplicates, "Other …" catch-alls, SKU-level lists).
2. Lack of coverage for hobbyist items (missing icons, makers, named forms, lines, traditions; structure too flat).
3. Sub-optimal / confusing organisation (misplaced items, inconsistent axes, labels a reader wouldn't guess).

## Approved rules
- **Scope rule:** in scope only if owned for personal life (hobby or quality of life). Trade/institutional equipment drops out or stays kind-level with no models.
- **Parts departments** only where owners swap/upgrade parts (watches, PCs, bikes, cameras, guitars, aquariums, watch modding). Elsewhere one "Spare parts" entry per appliance.
- **Brand mode per category:** Variety (people explore/collect many brands → every notable brand, long tail as stubs), Tier (people pick the best one → brands covering most of the market + every brand topping an independent test such as Consumer Reports / Which? / CHOICE / RTINGS), Mixed (tier mainstream, variety at enthusiast end).
- **Brand completeness method (variety):** union of independent source types (reference DBs, retailer brand directories incl. non-Anglo, resale/archive, official bodies, community lists); measure with overlap/capture-recapture, saturation, held-out spot check; inclusion bar = sells under own name AND in a reference DB or 2 independent sources; full pages for core brands, stubs for the tail.
- **Reference-database rule:** for hobbyist/luxury categories, use the community's reference database and copy its organising axis (e.g. Watchbase, Fragrantica, Discogs, Brickset, Numista, Mindat, StockX/GOAT, Wikidata, Getty AAT). Retail catalogues only for QoL items. Retail-harvest skew (one shop dominating a kind) is a finding.
- **Archetype model standard (hobbyist items):** Kind → Archetype (named pattern/icon/silhouette/model family that exists apart from a single SKU, e.g. A-2 jacket, 501, Air Jordan 1, Submariner, Birkin) → Version (original/licensed/reproduction/interpretation; generations; reference numbers) → Detail (material, size, colourway, hardware). Ordered by significance, not alphabet. No flat SKU lists.
- **Brand register as a first-class browsable view:** one entry per brand (country, founding, segment, lines, eras/creative directors, signature archetypes, scenes, related brands); brands link to items, never duplicated per item/scene/kind. Brand ranges repeated across kinds is a finding.
- **Craft-traditions register:** one entry per artisan tradition (region, period, technique, materials, signature forms linked to kinds, centres/masters, authenticity markers). Applies in every category (rugs, ceramics, glass, metalwork, lacquer, textiles, furniture, knives…). Sources: UNESCO ICH, Japan's designated traditional crafts, auction categories, Getty AAT.
- **Period/style** is an attribute and a view (antiques, vintage), not a kind.
- **Multiple views over one dataset** where useful: By type · By brand/designer · By period/style · By tradition · By scene.
- **Baby & child** is a cross-cutting view, not a category; "user" is a tag.
- **Built-in vs movable vs raw supply:** built-in features of a home → new category *Home Fixtures & Features* (zones: Kitchen; Bath & wellness; Living & entertainment; Structure & circulation; Home systems; Outdoor & grounds). Movables → Home domain. Raw supply → Building Materials (shallow). Hot tubs, saunas, baths move to Home Fixtures.
- Approved moves already decided: Smoking & Vaping → food/drink domain beside wine & spirits; Video Games → Play domain; collection albums → with what they hold (F3/F5); new categories Fragrance, Bakery/Sweets/Snacks, Soft Drinks & Water; collector lines (publishers/labels) allowed as ranges in media; one-sport helmets → Sports; protective equipment → Tools; all frames & sunglasses → one Eyewear dept in A4; chess clocks → games.

- Later approvals: living animals ARE possessions (pets, horses, fish, livestock) via a breeds/species register drawn from breed registries — not inside equipment categories; B7 becomes "Portable Climate & Air" after built-ins move to Home Fixtures; new "Vehicle care & detailing" dept in Vehicles; decorative lighting merges into Lighting; militaria (deactivated ordnance, replica weapons) → Weapons; china/porcelain patterns follow house → pattern → piece.

- Batch-2 approvals: Outdoor cooking dept in Garden (kettle, kamado, offset, pellet, pizza oven; barbecue leaves Kitchen; built-in outdoor kitchens → Home Fixtures); Optical & Scientific moves to the Play domain as "Observing & Measuring"; a living-plants register mirrors the animal breeds register; knife rule: EDC/utility/bushcraft → Tools, kitchen → Kitchen, fighting/hunting → Weapons; collector machines shelf (typewriters, slide rules, vintage calculators); antique scientific instruments as a period view.

- **Titles are OUT of scope.** Separate future taxonomies cover Visual Entertainment (film/TV), Auditory Entertainment (music), Literature, and Interactive Entertainment (games, incl. board/card game titles), with genres and titles. This taxonomy covers the *object*: carrier/format, edition type, publisher/label collector lines, pressing/printing attributes, condition and grading, storage — and cross-links to those taxonomies. Do NOT recommend title lists. (Product lines that are not entertainment titles — LEGO sets, action-figure lines, coin/stamp issues — stay in scope.)
- **Pursuits are out of scope (owner 2026-10-28).** Separate taxonomies will cover all Physical, Creative, Intellectual and Spiritual pursuits (sports, art forms, crafts, puzzle-solving, faith practices). Do NOT delineate every sport, art form or practice. Keep categories object-focused but organised: group by what the object is (form, mechanism, maker, archetype), let a pursuit group equipment only where owners shop that way and the pursuit has distinct equipment, and cross-link to the pursuit taxonomy.
- **Owner 2026-10-28:** built-in light fittings (recessed downlights, track, under-cabinet) → G3 Home Fixtures; door and window locks stay in B8 (G3's multipoint lock → B8).
- Batch-3 approvals: pinball & arcade → Video Games "Arcade & coin-op"; "VR & XR" dept; Fishing and Target sports as own depts in Sports; technical sport-specific apparel/footwear stays with its sport; trading cards: game-system view in Toys, collecting/grading view in Coins/Stamps/Cards, cross-linked; enthusiast keyboards and vintage computers depts; ham radio added.

- Batch-4 approvals: minerals keep ~150–250 popular collector species in the tree, the rest in a Mindat-linked species register; faith & craft traditions are the primary browse axis for religious objects (superseded 2026-10-28: religious objects are grouped by object form first; the faith tradition is a tag on each kind and the traditions register stays as a view); Issuer register (mints, central banks, postal administrations) and a cross-category Grading-services register (PCGS, NGC, PSA, BGS, CGC, Goldmine…); collectible figurines are their own dept separate from fine art; studio ceramics/glass in Art; artist register keyed to ULAN.

- Attestation: a record in a recognised reference dataset (bulk download, API, Wikidata) counts as proof of existence when source and retrieval date are recorded. Source pack per category = bulk dataset → Wikidata backbone → targeted fetches for gaps only; cross-check against a second source plus held-out spot check.

## Output format (per category)
- One line: brand mode (variety/tier/mixed, per department if it differs).
- Numbered findings with short codes (e.g. RG1, RG2…) grouped under: Gaps for hobbyists · Too much detail · Confusing organisation. Each finding: what's wrong with concrete evidence from the data (counts, named items, maker skew) + the specific fix.
- A short "What it would look like" tree (≤10 lines) for the most important department, using the archetype standard.
- Mark facts from your own knowledge that need checking ("to verify"). Never invent counts — compute them from the JSON.
- Be concise: aim for ~350–550 words per category.

- Owner decisions 2026-10-27: (1) brand segments use the controlled vocabulary in SEGMENTS.json (fashion map; luxury map; quality ladder elsewhere) with a 'kf' known-for tag — clothing is about brands organised coherently, appliances about which are quality. (2) A blocked maker/retailer site is no reason to drop an item: establish it from outside databases and lists. (3) Recurring and retained services (cleaning, gardening, domestic staff, personal trainer, concierge, jet cards and similar) are IN, as a services department in I3 — they are purchases that improve quality of life and belong to luxury-lifestyle aspiration. One-off services stay out as BRIEF says.
