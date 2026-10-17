# Stage 2 shared conventions (draft, pending owner approval)


Drafted by the domain A review (framework/structure/_review_A.md, section 4) and adopted as the draft convention for every category, pending owner approval. Category-specific examples come from domain A; other categories apply the same rule to their own objects. 'Scene tags' (C8) apply wherever a category has scenes or cultures; otherwise leave them empty.

**C1. Maker ledger: one core schema and per-category extensions.**
- *Core columns (every category):* `maker_id`; `name`; `native_name`; `aliases`; `maker_class` (house or manufacture; independent; microbrand; retail own-label; licensee or diffusion; costume or fashion brand; artisan or atelier; supplier, such as a movement or fabric maker); `country`; `place`; `founded`; `ended`; `status` (active, defunct, revived); `parent_id` (group or licensor); `known_for_kinds` (kind ids); `scene_tags` (with `core` or `adjacent` strength, from C8); `price_band` (C4); `sources` (at least one fetched URL, and a second where available).
- *Separate tables, not columns:* **lines and collections** (`line_id`, `maker_id`, name, the kinds it spans, `tier` entries, years, sources: Momotaro Classic, Cartier Love, Seiko Prospex Sea, an Angelic Pretty print series, Rimowa Original); **tier entries** (C4); **named forms** (C2); **variants** (C3).
- *Extensions (category columns, optional):* A2 `construction_policy`; A3 `marks` (maker's marks and hallmark notes); A5 `movement_policy` and `certifications`.
- *Why:* A1's table is the fullest; A3 adds maker class and collections across forms; A5 adds per-source tiers. Putting known-for named forms in a column (as A2, A3, A4 and A5 do) duplicates the named-form ledger. Derive it from that ledger instead.

**C2. Kind against named form.**
- (a) The choice-level test in section 4b decides kind against named form. A **kind** is the level at which buyers compare quality or makers. A **named form** is a specific design below it. It is either **maker-bound** (a model or line: Levi's 501, Iron Ranger, Speedy, Submariner) or **not maker-bound** (a generic cut, iconic design or traditional variant that many makers make: penny loafer, Shetland sweater, klompen, furisode, kihei-style chain if kept, uchiwa, Vienna regulator). Record it with the field `maker_bound: yes | no`. This replaces A1's rule "many makers → kind". The number of makers is not the test; comparison is.
- (b) **Not named forms:** specifications and certifications (ISO 6425, MIL-W, EN ISO 20345 classes: attributes), link patterns, motifs and prints (attributes or variants), sizes (attributes), and colourways, reference numbers, collaborations and editions (variants, C3).
- (c) **Traditional and regional types** are kinds when a fetched source shows them sold or compared as their own category (sari, kurta, kimono, geta, maang tikka, mangalsutra, jhumka). Otherwise they are non-maker named forms under the nearest generic kind (borla under maang tikka; klompen under clog; uchiwa under rigid fan; sporran under pouch or belt bag). In both cases they carry a `region` or `culture` tag and appear in a generated "by tradition" view. Never put them in a leaf of their own (F4).

**C3. Variant ledger (optional, sparse, one schema).** Columns: `variant_id`, `named_form_id`, `variant_code` (maker's style code, lot or reference number: Lot 1001XX, IQ5495-005, a Submariner reference), `variant_type` (colourway; material; print; size; reference; retro or re-issue; collaboration; limited edition), `partner` (for collaborations), `year`, `sources`. A variant is never a level and never a kind. It is filled only where an owner-emphasis scene needs depth (sneakers, Japanese denim, lolita prints, watch references).

**C4. Tier and price band.**
- (a) A `tier` never sits on a kind. It sits on a maker, a line or a named form, as **tier entries**: (`subject_id`, `scheme`, `value`, `source_url`, `date`). A subject may have several entries from different sources, with a computed `disputed` flag (A5's model). A named form does not inherit a maker's tier unless an entry says so.
- (b) A spec ladder that is measured on the object (EN ISO 20345 class, COSC level, metal fineness, fill power, denim weight, Super number) is an **attribute** with its standard named, not a tier entry.
- (c) A platform's own segment labels (Grailed Core / Grails / Hype / Sartorial; StockX premium) are a dated `platform_tag`, not a tier.
- (d) A **price band** is one domain-wide scheme in one currency, so that A1 ($ to $$$$$), A5 (Jomashop USD bands) and A2, A3 and A4 (unspecified) share bands. Proposed: USD bands under 50, 50–150, 150–500, 500–1,500, 1,500–5,000, 5,000–15,000 and over 15,000. They are derived from a dated, sourced list price.
- (e) A tier scheme enters the data only with at least one fetched source, and preferably a second from another region (A3 and A4 fail this today).

**C5. Levels and axes.**
- (a) Fixed level names: category, sub-family, leaf, kind, named form. At most four levels below the category, and the named form counts as one of them.
- (b) A sub-family may skip the leaf level when it holds about 12 kinds or fewer. The data then stores the kind with `leaf = null`, not under a dummy leaf.
- (c) "One stated axis per level" is read as one axis per level **within each sub-family**. Each sub-family states the axis of its leaf level in its definition (A5: function for watches, placement for clocks; A2: shaft height in Boots, closure in Shoes).
- (d) Each A category ends with a sub-family "Parts and accessories made for one <object>" for the S3 items it receives (X7). It is the only sub-family exempt from the level-1 axis.

**C6. Size, fit and user.** Size (garment size, shoe size, ring size, case diameter, luggage size class, frame size) is always an attribute with its standard (ISO 8559-1, ISO 19407, ISO 8653, ISO 8624, airline bands). User (gender, child, baby, adapted) is always a tag with generated department views. Luggage size class is the only proposed exception (owner question A4-2).

**C7. Order inside a leaf.** Kinds go canonical form first, then the secondary key that the sub-family states (spec, height, formality or complexity). Named forms go by maker (in the order of the maker ledger's `name`), then by first-introduction year as attested, then alphabetically where no year is attested. Variants go by `variant_code` or year.

**C8. One scene vocabulary for domain A.** One controlled list of `scene_tags`, each with a definition source (an MFA style guide, a Subculture Wiki page, or a community wiki), `core` or `adjacent` strength, and tagging at the maker, kind and named-form levels, without automatic inheritance (A1, owner question 9). A2 and A4 use this list instead of their own labels. A tag that has no source is held back (A2 already says its labels are "not attested").

**C9. Alias and homonym table.** One table: `term`, `language` and `script`, `target_id`, `relation` (alias, regional name, homonym). For example: JSK = jumper dress; スカジャン = souvenir jacket; カバーオール = chore coat (JP), but coverall = boiler suit (US); longcase = grandfather clock; shopper = tote; wristlet → two targets. The labels are English, with a native-script label (A1, owner question 11).

