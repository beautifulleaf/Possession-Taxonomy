# DPH_E memo notes (E1, E2, E3, E4; none built)

Offline Opus decision pass (SESSION_7 step 1; R-116 d, R-118 a). Each point is one structure_flags item of framework/structure/navigation/proposals.tsv, with its decision. Attribute rows: verify/out/DPH_E_attributes.tsv; scheme, standard, platform and grading-scale rows: verify/out/DPH_E_needs.tsv. Kind ids for E2 to E4 are given by the tree builder (R-58); E1 ids are the adopted ones of memo section 13, and none changes.

## E1

- **E1-1 Player count (attribute; partial revision of E-9, provisional).** Player count is printed on the box. It is a fact about the object, not a genre, mechanic or theme, so the owner's IE rule (BRIEF) does not bar it. Store `player_count` (min and max players) on the game named forms of E1.5.1.01, E1.5.2.02, E1.5.3.03, E1.5.3.04, E1.5.4.01, E1.5.5.01 and E1.5.6.07, as a facet. The builder should change the E-9 wording in the memo to say that mechanism, BGG Type and Category, theme, audience labels and complexity weight stay out (they are at most the IE link field), while printed player count, playing time and box age are attributes.
- **E1-2 Playing time (attribute, same revision).** Store `playing_time_min` (the printed range in minutes) on the same game named forms, as a facet. Weight and complexity stay in the IE link field.
- **E1-3 Box age (attribute).** Store `min_age` (the printed minimum age) on every E1 named form. The C6 user tag (baby, child, teen, adult) is derived from it, and the age-band filter reads it. Age is never a level.
- **E1-4 Warhammer-style faction (attribute, provisional).** Faction names what the miniatures in the box depict, as a character or franchise tag does (LEGO themes and Pop Mart characters are already tags). It is not lore-as-genre or a mechanic. Store `faction` on named forms of E1.5.5.01, E1.5.5.02 and E1.1.2.02. Its values are controlled per game system (the C13 row), taken from the publisher's own faction list. It is a facet only inside the game-system view. Rationale: Access Models filters on faction, and the Meeple Mountain guide says players choose by faction first.
- **E1-5 Miniatures-game army or unit box E1.5.5.02 (noted).** The kind stays †. Attest it in the E1 harvest on a publisher or shop page that sells army or unit boxes; faction boxes are its named forms.
- **E1-6 Paints, glues and tools (display_only; other_category C4).** These stay C4 (memo section 9.4). The Models group (G-E1-3) gets a generated cross-link "Paints, glues & tools (C4)" to the C4 modelling-supplies kinds once C4 is built. groups.tsv does not change, because a cross-link is not a member.
- **E1-7 Diorama and scenic kits (covered).** A building, ruin, terrain or diorama kit sold for scale models or miniatures is E1.3.1.01 Assembly scale model, with `subject` = "structure, terrain or diorama". Scenery sold for a model railway (gauge or railway scale stated) stays E1.3.2.05. Loose groundwork materials (static grass, flock, scatter, water effects) are model-making supplies and go to C4. Terrain packed in a game-system starter box is part of that box. E1.3.2.05 is not widened: its leaf is Model railways, so widening it would give placers a wrong home.
- **Display (display_only, from level2_note).** The radio-controlled vehicle (E1.4.03) and the slot-car set (E1.4.04) are also listed in the Models group as a hobby shelf. This is generated; their home does not change. Every group gets an age-band filter.
- **Needs.** Spiel des Jahres awards; maker kit skill levels; Gunpla grades (provisional); collector figure format ladder; BoardGameGeek rank (provisional); EN 71, ASTM F963 and CPSIA, ISO 8124 (gate standards, `standard_met`); TCG card grading scales (provisional); C13 rows for construction and track systems, railway scales and gauges, and TCG and miniatures game systems. The C13 `platform_type` list needs three new values: "toy construction or track system", "model scale and gauge" and "card or miniatures game system".
- **Maker role.** way_in (maker_roles.tsv row E1 *) confirmed. The brand and publisher tab sits beside the type path.

## E2

- **E2-1 Exercise bike types (split, provisional).** In the Cardio leaf of Gym, fitness and exercise, the memo kind "exercise bike" becomes **upright exercise bike** (the canonical form, listed first). Add two kinds:
  - **spin bike (indoor cycling bike)**: heavy front flywheel, road-bike riding position, standing out of the saddle possible.
  - **recumbent exercise bike**: a seat with a backrest and the pedals forward.
  The bodies differ, and Lifelong India compares the three types separately, so they pass C10's retail-facet test. Attest each on a fetched shop page that sells it as its own category. Resistance type (magnetic, friction, fan, water) is the attribute `resistance_type`, never a kind. Put the air (fan) bike, whose handles move with the pedals, on the harvest's "missing kind?" list: it is a kind only if a fetched page sells it as its own category. A bike trainer that holds a real bicycle stays G1 (P7).
- **E2-2 Pickleball and padel (new_kind).** Add two leaves to Racket and paddle sports (sport axis), each kind attested by a fetched shop page (Tennis Warehouse shelves, SportScheck "Padel-Tennis", Rebel Sport pickleball page):
  - **Padel**, with kinds **padel racket** and **padel ball**.
  - **Pickleball**, with kinds **pickleball paddle** and **pickleball ball**.
  Padel and pickleball shoes are E2 kinds only under K-127 (a performance model with a court-specific sole); otherwise they are A2. Nets and posts are kinds only if a page sells them for the one sport.
- **E2-3 Running (display_only).** No E2 leaf is added. The generated sport view "Running" lists the A2 running shoes, A1 running clothing, A4 running bags and vests, D2 GPS sports watches, H2 sports nutrition (E-18) and the E2 Track and field kinds (track spike, starting block, hurdle). Rebel Sport and Kakaku show running this way.
- **E2-4 Second-hand safety gear (noted).** Condition stays a shop facet only (C16), and no data is stored. The page for UIAA-certified kinds may carry the UIAA advice as display text.
- **E2-5 Thin evidence (noted, provisional).** Six usable pages back E2, and the big retailers were blocked. The display order of level 1 changes to shopper prominence: fitness first, then hiking and camping, then the rest (Kakaku order). The stored alphabetical order (memo section 8) is unchanged. This order and the quality orders are provisional.
- **HEMA (new_kind, from point E4-3, provisional).** Add a leaf **Historical European martial arts (HEMA)** under Combat and marker sports (discipline axis), with three kinds:
  - **HEMA training sword**: a blunt steel feder or a synthetic trainer. Its non-maker named forms are feder, synthetic longsword trainer and messer trainer, and the maker's models are maker-bound.
  - **HEMA fencing jacket**: padded, rated to 350 N or 800 N, recorded as `standard_met`.
  - **HEMA protective gloves**.
  The mask is the existing fencing mask kind; a back-of-head overlay made for one mask goes to the parts sub-family. Under K-87, step 10 and P8, a sharp sword is E4 and a decorative one B4. Each kind needs a fetched HEMA shop page.
- **Display groups for the build.** Use the 17 level-1 labels of the proposal, one per sub-family; "Protective gear & training aids (multisport)" is the multi-use sub-family. Each sport page shows its A1, A2 and A4 objects as a generated cross-category view (memo section 7). The racket finder is a view built from `racket_specs`.
- **Needs.** UIAA standards; EN PPE standards (numbers provisional); ISO 20957 (provisional); FIE homologation; EN ISO 23537; OutdoorGearLab and RunRepeat scores; the `player_level` scheme (shared with E3); maker boot ladders; the attribute-convention scales (willow grade, iron category, ski use class); C13 rows for ski sole standards, cleat systems and golf adapter sleeves (types exist since R-46).
- **Maker role.** owner (row E2 *) confirmed. Artisan cue makers, rod builders, bat makers and board shapers stay in the ledger as owners of their named forms.

## E3

- **E3-1 Guitar body designs (named_form).** Under the solid-body electric guitar, the non-maker named forms are S-type, T-type, single-cut (Les Paul type) and the following, each attested on a fetched page:
  - double-cut;
  - SG-type;
  - superstrat;
  - offset (Jazzmaster and Jaguar type);
  - V-type;
  - Explorer-type.
  Thomann's group "Heavy" is a display group of the V, Explorer and other heavy shapes, not a named form. Maker models link to their design family by `design_family_id`. The bass guitar follows the same rule at harvest (P-type and J-type basses as non-maker named forms, attested).
- **E3-2 Seven- and eight-string and baritone (attribute).** These are `string_count` and `scale_class` (with `scale_length_in`) on named forms, not kinds (C2(b), C6).
- **E3-3a Desktop synth module (attribute).** The memo kind "keyboard synthesizer" becomes **synthesizer**, with `form_factor` = keyboard, desktop module or rack module. A desktop and a keyboard version of one model share a sound engine and are variants or named forms of one kind. The modular synthesizer module stays its own kind (made for one mount system, C12(a); Eurorack is a C13 row).
- **E3-3b Groovebox (new_kind, provisional).** Add the kind **groovebox** to the Synthesizers & electronic instruments leaf: an all-in-one instrument that combines synth, drum and sample voices with a built-in pattern sequencer. A unit sold as a drum machine or as a sampler keeps those kinds. Attest it on a fetched shop page that sells grooveboxes as their own category (Andertons separates them).
- **E3-4 Thomann shelves outside E3 (other_category, display_only).** Software is I1; sheet music is F1; stage lighting is B3; fog and haze machines are B4; broadcast and video gear is D3 or D4. The builder shows them as cross-links from the E3 page, never as E3 groups (K-145, step 22).
- **E3-5 Traditional Instruments shelf (display_only).** A region is never a group. The generated "by tradition" view (E-8) recreates the shelf from region tags.
- **E3-6 Guitar ladder evidence (noted, provisional).** It rests on two retailer and press pages with no community source; the next harvest adds weight.
- **Display groups for the build.** Use the 11 groups of the proposal:
  - Synths, drum machines & controllers: the synth leaf plus the E3.3 Controllers leaf.
  - Recording & live sound: microphones, mixers and interfaces, loudspeakers, headphones and IEM, signal processors; with a studio / stage toggle from `use` tags.
  - Woodwind & brass: two leaves.
  - Other instruments: lutes, zithers and harps, free reeds, mechanical instruments and other idiophones.
  - Parts, cases & accessories: E3.4 plus E3.5.
  - The remaining groups as listed in the proposal.
  A used and vintage toggle on every group reads era tags and the condition shop facet.
- **Needs.** Fender and other guitar ladders; drum ladders; band and orchestral build levels; the piano reviewer ladders (disputed); the Reverb condition scale (provisional); C13 module formats and MIDI. The `platform_type` list needs the value "module format".
- **Maker role.** way_in for instruments (row E3 *). Owner applies to E3.2 and E3.3; the row "studio, PA and effects gear" is read with scope E3.2 and E3.3 at build.

## E4

- **E4-1 Everyday-carry or utility pocket knife (other_category C1).** Under K-83, EDC and other locking folders are C1 unless the blade is a weapon kind (karambit, push dagger, automatic or butterfly knife). No E4 kind is added; `deployment` stays an attribute.
- **E4-2 Bushcraft or survival knife (other_category C1).** It is filed by its working task (C1) unless the maker sells it as a fighting or hunting knife (E4.5 Bowie or fighting knife, or hunting knife). A use tag "camping" or "survival" may sit on an E4 knife only where the maker's page says so. Cross-domain: the C1 build needs kinds for the locking folding pocket knife and the fixed-blade outdoor (bushcraft) knife; this is passed to the C decision pass.
- **E4-3 HEMA training swords (other_category E2).** Blunt trainers (feders, synthetics) and their protective gear are E2 under K-87, key step 10 and P8; sharp swords stay E4.4; decorative ones are B4. The E2 kinds are in the E2 section above.
- **E4-4 Blade shape (attribute).** Store `blade_shape` on knife named forms as a facet, with the values drop point, clip point, spear point, tanto, sheepsfoot, wharncliffe, trailing point, hawkbill, dagger, reverse tanto and kukri.
- **E4-5 Skinner and gut hook (named_form plus attribute, provisional).** The skinning knife and the caping knife are non-maker named forms of the hunting knife: generic designs that hunting shops sell by name. Each needs a fetched page. The gut hook is a feature added to several blade shapes, so it is the yes/no attribute `gut_hook`, not a named form.
- **E4-6 Knife-steel reference table (attribute plus standard).** A domain reference table `steels` holds, for each steel:
  - steel_id, name and aliases;
  - the steel maker (the mill, as a maker row of class supplier);
  - its class (carbon, stainless, tool, powder metallurgy, laminated);
  - its typical HRC range and its sources.
  Knife and sword named forms carry `steel` (a steel_id) and `hardness_hrc` (to ISO 6508 Rockwell C), both as facets. Outdoor Life's steel scores are class (iii) tier entries on steel rows. C4 needs subject_type "steel": the second reference-row exception, after R-118(c)'s species entries. This is a schema change through tools/schema.py.
- **E4-7 NIJ edition change (attribute).** `protection_level` is scope-qualified by standard edition, and both editions' labels are held: NIJ 0101.06 IIA, II, IIIA, III, IV; NIJ 0123.00 HG1 to RF3; NIJ 0115.00 levels 1 to 3, edged blade or spike. Labels are not mapped from one edition to the other unless a fetched NIJ page gives the mapping. The level is a floor shown first on armour pages.
- **E4-8 4komma5 fishing shelf (other_category E2, covered).** Fishing tackle is E2 Angling (step 10 note: spearguns and other fishing tackle are E2).
- **E4-9 US-heavy, vendor-written evidence (noted, provisional).** Quality orders stay provisional until European and Japanese pages are fetched.
- **Display (display_only, from level2_note).** These are cross-links; the homes do not change:
  - arrows (81), crossbow bolts (82), bowstrings (84) and arrow rests (105) are also listed in the Bows group;
  - air-gun pellets (80) are also listed in the Air guns group;
  - Knives & daggers shows its kinds by blade style;
  - Swords and Armour carry an antique / modern-made toggle from era tags, with `nihonto_period` as a filter beneath it;
  - the use view (hunting, target and competition, self-defence, HEMA and re-enactment, collecting, martial arts) reads C8 use tags.
- **Maker role (needs a maker_roles.tsv update, provisional).** The scoped rows "blades and armour" and "firearms, air guns, archery and other weapons" are read at build as follows:
  - way_in: E4.4 Swords, E4.5 Knives and daggers, the E4.6 Polearms leaf, the E4.8 historical armour kinds (plate helmet, limb armour, plate harness, shield) and the E4.10 blade fittings leaf (tsuba makers via the school table);
  - owner: E4.1, E4.2, E4.3, E4.7, E4.9, the modern ballistic armour (soft vest, hard plate, stab vest, plate carrier, ballistic helmet) and the other E4.10 leaves.
  Modern body armour is chosen by model and NIJ level, not by maker.
- **Needs.** The three NIJ standards; Rockwell C; the steel reference table; Outdoor Life steel scores; HEMA maker reputation (provisional); NBTHK and NBSK papers; the Kult of Athena classes; World Archery equipment rules; C13 rows for cartridge standards, rail interfaces and the AR-15 pattern, magazine patterns, and bow limb and cam systems.
