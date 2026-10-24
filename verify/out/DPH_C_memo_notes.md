# DPH_C memo notes (session 7, R-118 a)

## C1
- **Demolition hammer (breaker, chisel-only): new kind.** The tree builder adds kind C1.4.1.04 "Demolition hammer (breaker)" in leaf C1.4.1 Hammers & mallets (leaf axis: tool family; hand, power and machine versions of a family share a leaf). Definition: powered percussion tool that drives a chisel or point by hammer blows only, with no rotation, to break concrete, masonry and tile. The rotary hammer C1.2.1.04 stays in Drills because it drills; a rotary hammer with a chisel-only mode stays a rotary hammer (primary action, C14 tie-break). Jackhammer and pneumatic or petrol breakers are this kind with `drive` an attribute; "jackhammer" goes to the alias table. Attest at harvest: a page selling demolition hammers or breakers as a type (Toolstation lists a Demolition group, HOL evidence https://toolstation.com/power-tools/c5). Provisional until attested.
- Display group G-C1-4-1 is renamed "Hammers, mallets & demolition hammers" (groups_changes).
- **Toolstation "Air Tools & Compressors": display only.** A `drive` view (pneumatic) over existing kinds plus the air compressor C1.9.2.01; no node.
- **Toolstation "Site equipment": display only.** A setting view over C1.8.4, C1.9.1 and C1.9.3; no node.
- **Memo section 13 kinds not yet in data/kinds.tsv: noted.** Loading the frozen tree is the build step; kind-level groups are checked after it. C1.4.1.04 is loaded with the tree only once its page is fetched.
- **Scheme rows owed: needs.** Consumer Reports, CHOICE and Stiftung Warentest (class ii), plus Pro Tool Reviews and CordlessPicker (memo; provisional). Listed in DPH_C_needs.tsv for QS_.
- **Battery platforms, SDS holders and stacking storage: needs (platform).** PF_4 harvests tool battery platforms; SDS-plus and SDS-max are tool-holder rows (new `platform_type` value "tool-holder system").
- **Attributes stored:** `drive`, `sold_as` (bare unit or kit, a variant attribute), `tool_holder`, `impact_energy_j`.
- Maker role stays owner (maker_roles.tsv), with the premium hand-tool makers tab built from named forms and lines.

## C2
- **Mower "lawn area suited": attribute.** `lawn_area_suited` on mower named forms (maker's stated maximum in square metres, display bands generated); the mowers page asks lawn size before mower type.
- **Secateurs "hand size": attribute.** `hand_size` (small, medium, large) on secateurs and loppers named forms; `cutting_action` (bypass, anvil, ratchet) confirmed as an attribute.
- **Spare-battery availability: attribute.** `spare_battery_available` on cordless machine named forms, linked to the battery platform row.
- **Garden multi-tool: new kind.** The tree builder adds kind "Garden multi-tool (split-shaft powerhead)" in C2.2 leaf Grass, brush & scrub cutters: a powered handle and motor unit that takes interchangeable cutting attachments (grass trimmer, hedge trimmer, pole pruner, brush cutter). Basis: B&Q lists the class (memo S3) and the C-10 combination-machine pattern files it by primary action. Attachments sold alone go to C2.10 (made for one machine); the shaft systems (Stihl KombiSystem, Ryobi Expand-It) are C13 platform rows; a Gardena combisystem manual handle stays a hand tool with its heads in C2.1 and C2.2. Provisional until a harvested seller page shows the class.
- **"No new kind or level is shown wrong": noted.**
- Needs: Which?, Consumer NZ, BBC Gardeners' World schemes; DLC list as a standard; battery and split-shaft platforms.

## C3
- **Place and light as the first filter: attribute (tags, not levels).** Controlled lists `light_need` (full sun, partial shade, full shade; bright direct, bright indirect, medium, low light) and `setting` (indoor room, balcony or patio, garden border, pond or bog, greenhouse or conservatory, terrarium) on kinds, with named forms allowed to override; also `hardiness_rating` (RHS H1a–H7 or USDA zone, scale named with each value) and `pet_safe`. These drive the "find a plant for your spot" finder; no leaf or level is named by a place (C11).
- **Mushroom log kit and grow kit: new kind.** North Spore lists "log kit" as a product type apart from plug and sawdust spawn (HOL evidence https://northspore.com/collections/all?page=1), which meets K-1 (a kit sold and compared as one object). The tree builder adds kind "Mushroom grow kit" in C3.4 leaf Fungal spawn: an inoculated log, block or bag of substrate sold to fruit mushrooms at home; `species` and `substrate` (log, sawdust block, straw, grain) are attributes. Mushroom spawn stays the kind for spawn sold to inoculate. A seed-starting set stays a mixed set filed by its item of greatest value (no seller compares it as a class). Provisional until the harvest fetches a grow-kit page.
- **Aquatic and bog leaf still empty: noted.** The leaf stays; its kinds enter when a pond-plant retailer tree is fetched (memo attestation list).
- **AAS and Thompson & Morgan not fetched: noted.** Seed award signals stay provisional.
- Needs: RHS AGM, AOS awards, AAS (provisional) as schemes; RHS hardiness and USDA zones as standards.
- Maker role stays none.

## C4
- **Craft storage (Hobbycraft "Home & Storage"): other category B1.** Already decided by K-172 and K-190 (storage holding several objects is never a part; craft storage and the craft table are B1, only the easel C4). No C4 kind.
- **Craft kits: new kinds for kits compared as one object; rule for the rest.** Under K-1, the builder adds kit kinds where the kit is the product shoppers compare, each as the final kind of its craft sub-family with `leaf = null` (leaf 0 in ids, as the R-58 mixed kind): "Paint-by-numbers kit" and "Diamond-painting kit" in C4.1 Picture-making, "Needlecraft kit (cross-stitch, embroidery, needlepoint)" in C4.3 Yarn & needlecraft. Each is provisional until a harvested seller page shows the kit type sold as a class (Hobbycraft "Craft Kits" product type, memo S5; Google "Art and Craft Kits", memo S30). Every other mixed kit (jewellery, candle, soap, mosaic kits) is filed by its item of greatest value with `kit_contents` listed. A kit made for play that cannot do the real job is E1 (C15).
- **"Hobbies & Games" and "Kids" departments: other category E1 and a user tag.** Not C4 groups; kids is the C6 user tag with a generated view.
- **Blick and Utrecht blocked: noted.** Art-supply navigation rests on the memo and stays provisional.
- **Scoped C4 yarn maker-role row: covered.** maker_roles.tsv already holds "C4 yarn way_in" (R-116 c).
- Attribute stored: `kit_contents`. Needs: ASTM D4303, Colour Index, CYC yarn weights, ACMI seals (standards).

## C5
- **Tree not built: build instruction.** Build from memo Candidate A (87 kinds, ids by R-58 at build), with the proposal's eight display groups (Pens; Pencils, erasers and correction; Ink, refills and pen parts; Notebooks and journals; Diaries, planners and calendars; Paper, cards and post; Desk, filing and office supplies; Calculators and office machines); no level change.
- **Paper stock (Tomoe River, MD Paper, Stalogy, Rhodia, Clairefontaine): lines rows plus an attribute.** A paper stock is a mill's or maker's line (lines table, maker class supplier where it supplies other makers; maker-relation "supplies paper to"); paper sold loose or as the maker's own notebook is a maker-bound named form linked to that line; a notebook by another maker carries `paper_stock` = the line id. Consensus and community rankings are tier entries on the line (scheme fountain-pen paper consensus, class iii). Not a kind, not a register.
- **Maker role (R-116 c): way in for fountain pens, fountain-pen ink and notebooks, planners and paper stocks (decided, provisional).** Shoppers and collectors choose these by house (Goulet and Cult Pens brand menus, Fountain Pen Network, collector market by maker, memo section 6). Scope: fountain pen and dip pen kinds, bottled ink and cartridges in C5.5 For fountain pens, and the C5.2 notebook, composition book, refillable notebook system, planner and diary kinds with C5.5 For planners and refillable notebooks. Everything else in C5 stays owner. Full maker ledger and maker pages there, seeded from shop brand lists and community lists; country never divides it. A scoped row for framework/structure/maker_roles.tsv: `C5 | fountain pens, fountain-pen ink, notebooks, planners and paper stocks | way_in | yes | houses are what pen and paper shoppers choose (DPH_C)`.
- **Retailer collections: never kinds.** Luxury → price band and the shop's `platform_tag` (class vi); Japanese → `culture` tag on the named form and scene `japanese-stationery`; Demonstrator → `body_material` value "transparent resin (demonstrator)"; Pocket → `pen_size` (C6); Vintage-inspired → dated `platform_tag`; Maki-e (with raden, urushi) → `decoration_technique`.
- **"Journal": alias** of notebook (C9 row).
- **"Special edition": variant** (variant_type limited edition or edition, C3). **"Rare or out of production": attribute** `production_status` (current, discontinued).
- **Label tape: new kind.** The builder adds leaf "For label makers" in C5.5 (leaf axis object served) with kind "Label tape cassette": a tape cartridge made to fit one label-maker system (S3); the systems (Brother TZe, DYMO D1, DYMO LetraTag, Epson LK) are C13 cartridge-standard rows. Provisional until attested.
- Shop experience tiers (Starter, Next level, Entry-level gold nib, Luxury) and best sellers per price band stay platform_tags over named forms, never levels.
- Needs: paper consensus and FPN schemes; hallmark, ISO 216, DIN 66399 standards; exam calculator lists; cartridge, label-tape and planner-refill platforms.

## C6
- **Dobsonian: kept a non-maker named form (C-18), featured.** C12(a) fails: the same Newtonian tube design is sold on rocker boxes, equatorial and alt-az mounts by the same makers, so the mount is an attribute. Shoppers get the Dobsonian entry through the `mount` facet and NF-C6.1.3.02-001 shown first in group Reflectors.
- **Astrograph recheck: attribute stands** (`designed_for` = imaging). **New kind C6.1.3.08 Schmidt astrograph (Schmidt camera)**, provisional and from memory: the prime-focus Schmidt (RASA) has no design kind; attest at HV_C6_NK; group Catadioptric telescopes.
- **New part kinds:** C6.5.1.13 Telescope finder; C6.5.1.14 Barlow lens; C6.5.1.15 Astronomical filter; C6.5.2.04 Microscope objective; C6.5.2.05 Microscope eyepiece (ocular). All go to attestation (HV_C6_NK); groups G-C6-12, G-C6-13 and G-C6-22 renamed and extended.
- **Telescope bundles and OTAs: attribute** `sold_as`. **Biosecurity and other fields of use: attribute** `area_of_application` (tags, facet). **Warentest pollutant results: noted** (tier entries on named forms).
- Attributes also stored: `mount`, `goto`, `objective_class`, `tube_length_standard`, `filter_type`, `finder_type`, `magnification_factor`.
- Noted for the HV_C6_NK harvest as "missing kind?": star diagonal, focal reducer or field flattener, filter wheel, dew heater.
- Needs: Warentest, Outdoor Life, BirdForum alpha (disputed), Best Binocular Reviews schemes; JIS B7157; PF_3 adds finder shoe, filter threads and microscope threads and tubes.

## C7
- **Chainsaw evidence (four of seven HOL rows): other category C2** (K-173). Its findings go to C2's build: the Stihl homeowner, farm and ranch, professional ladder as a maker scheme (class iv) on lines, dealer service as guidance, the KWF mark as a standard.
- **Size-class view crossing into C2: display only.** The generated size-class view over tractor named forms (`size_class`: sub-compact, compact, utility, agricultural) shows C2 lawn tractors and ride-on mowers as cross-links; they keep their C2 home (K-99, one home per object).
- **Landwirt "Spezial- und Kleintraktoren" and "Mäh- und Bergtraks": covered.** Small tractors are the standard four-wheel tractor (or narrow orchard and vineyard tractor) with a size label; Mäh- und Bergtraks are the slope (mower-carrier) tractor. No new kind.
- **No new kinds from the evidence; memo † kinds still owed: noted.**
- Attribute stored: `size_class` (maker label on named forms). Needs: Nebraska Tractor Test, DLG, top agrar schemes; KWF mark standard (provisional); hitch categories and PTO rows (C13).

## C8
- **Woodwork and trim paint (gloss, satinwood): covered** by memo kind "wood and metal paint", which the builder names "Woodwork and metal paint (trim paint)"; gloss and satinwood are `gloss_level` values.
- **Primer and undercoat: covered** by the primer kind, defined as "primer or undercoat (preparatory coat)"; `coat_role` (primer, undercoat, primer-undercoat, sealer).
- **Spray paint, tile paint, furniture paint: covered** (already memo kinds in C8.7 Paints).
- **Dowel pin: new kind** "Dowel (dowel pin)" in C8.3 leaf Connectors & supports: a wooden, plastic or metal pin set into holes to join or align two parts. Provisional until attested (Tooled-Up group, HOL evidence https://www.tooled-up.com/fixings-fasteners/cat/22/?page=1).
- **Packer (shim): new kind** "Packer (shim)" in C8.3 leaf Connectors & supports: a thin plate or wedge set under or behind a frame or fixing to level or space it. Provisional, same source.
- **Clip: not a kind (display only).** The shelf mixes clips for different objects; the builder adds "Cable clip" in C8.6 Cable & flex and "Pipe clip" in C8.5 Pipe, each provisional until a page sells it as a type; spring and other clips wait for evidence.
- **Resin for chemical anchors: covered** by the chemical anchor kind (resin cartridges and capsules are that kind; studs are steel anchors or included parts).
- **Floor tile against wall tile: noted** (confirmed); `tile_material`, `pei_rating`, `slip_rating`, `water_absorption_class` stored as attributes.
- **Structural (strength-graded) timber: attribute** `strength_class` (C16, C24, further EN 338 classes as fetched) and `treatment_class` on sawn timber; no new kind.
- **Plumbing, electrical, adhesives, batteries, fuels and packing without HOL evidence: noted**; their ladders stay provisional on the memo.
- Attribute stored also: `gloss_level`. Needs: Warentest and Choice paint schemes; EN 13300, EN 338, EN 335, PEI, DIN 51130 and ANSI A326.3, ISO 898-1 standards.
- Maker role stays none; brand is a filter.
