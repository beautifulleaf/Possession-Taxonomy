# DPH_B memo notes: structure decisions for the build (domain B)

Opus decision pass, offline (R-116 d, R-118 a). Unbuilt categories: instructions bind the tree builder like memo text. Built categories (B3, B10): the points decided, with the rows in DPH_B_kinds.tsv. Attributes, needs and group changes are in the DPH_B_*.tsv files. "Provisional" means the call rests on memo text or memory and holds only once a fetched page attests it.

## B1
- **Futon mattress** (IKEA India "Futon mattresses" under sofa beds): covered by the memo's floor mattress kind. Rename it "Floor or futon mattress (shiki-futon)" (B1.2.2): a thin mattress that folds or rolls away, used on the floor or on a futon sofa frame. Add C9 alias rows "futon mattress" and "shiki-futon". A futon sofa sold with its mattress stays the futon sofa (B1.1.1, B-2). Provisional until a page shows the type.
- **Corner and L-shaped sofas**: attribute `configuration` of sectional sofa (values in DPH_B_attributes.tsv), plus alias row "corner sofa" → sectional sofa. No kind.
- **Sun lounger** (outdoor-only form): new kind under B1.1.2 Armchairs & lounge chairs, after chaise longue. Definition: "an outdoor reclining seat with an adjustable backrest, often on wheels, made to lie on in the sun". The upholstered indoor chaise longue keeps its kind. Next free kind number under B1.1.2. Provisional until a garden-furniture page shows sun loungers sold as a type.
- **Garden lounger set and garden furniture sets**: no kind. S3a files a furniture set by its pieces, with `unit_of_sale` = set (contents listed). Garden furniture stays a setting view (`setting` attribute).
- **Wall units and coat racks** (Stylight): noted. They support the TV unit and the coat rack (†) kinds. The harvest may use the Stylight page as the coat rack's attestation if it is fetched in full.
- **Albums and collection holders (B1.5.3)**: display only. Keep them in B1 (K-9). Show them as their own display group "Albums & collection holders", outside the furniture groups. No level change.
- **Attributes to store**: configuration, seat_count, setting, unit_of_sale, with_storage, martindale_rubs, firmness (scale named with the value), installation.
- **Needs**: Red Dot award (iii); a design-classic authenticity classification (C16); Martindale, FSC and GECA standards.

## B2
- **Chair pad (seat pad)**: new kind in B2.4 Seat textiles (`leaf = null`), placed after scatter cushion (the axis puts stuffed pieces before covers). Definition: "a thin cushion, usually with ties or a non-slip back, made to lie on the seat of a chair". IKEA UK sells chair pads as their own category (HOL_EV evidence, https://www.ikea.com/gb/en/cat/textiles-tl001, partial fetch). The page that attests it must show chair pads sold as a group. Take the next free kind number in B2.4.
- **Weaving-environment tier** (city or workshop, village, nomadic or tribal): store it as the attribute `weaving_environment` on rug named forms. It is backed by a C16 grading-scale row with scale_type classification (R-2). It feeds the handmade-rug tradition view. It is never a ladder, a level or a division by country.
- **Season filter**: attribute `warmth_season` on duvets, comforters, quilts and seasonal bed linen, beside the measured `tog`. Season is the label shoppers filter on (BAUR); tog stays the spec.
- **Yardage fabric** (IKEA "Fabrics & sewing"): other category C4 (craft). Cross-link only.
- **B2.1.2 bed covers and blanket or throw**: display only. Show two groups: "Duvets and bed covers" and "Blankets and throws" (blanket or throw, electric blanket). Ids and the leaf are unchanged (B-16 keeps one blanket-or-throw kind).
- **Attributes to store**: warmth_season, tog, fill_power, thread_count (with counting rule), knot_density, process, weaving_environment, opacity, en1307_use_class.
- **Needs**: the weaving-environment classification scale; OEKO-TEX, GoodWeave, GOTS and EN 1307 standards; Consumer NZ bed-linen tests (ii).

## B3
- Smart lights, battery table lamps, children's lights and "LED lights" are not kinds. They are covered by the attributes connectivity, power_source and light_source and by the user tag; each feeds a generated view.
- Bulb page: cap platform rows are listed in needs and harvested by PF_3. The bulb ladder (cap > shape > lumens > colour) is provisional (noted).
- Fairy lights at Hoeffner: other category B4 (K-181). Show them as a cross-category link from Lamps.
- Hoeffner "Möbelleuchten": covered by B3.1.3.04 under-cabinet light.
- Wall-mounted lantern light B3.1.2.03 in the Outdoor group: display only. groups.tsv already does this, so nothing changes.
- **Attributes to store**: light_source, power_source, connectivity, colour_temperature_k, cri, lumens, ip_rating, fl1_ratings, cell_type.
- **Needs**: platforms for lamp caps and smart ecosystems; standards for FL1, IP code and energy labels.
- No new kinds and no moves.

## B4
- **Sundial**: remove it from the B4.7 tree at build (R-28: all sundials are A5, garden sundials included). The named form armillary sundial goes with it to A5. The garden view lists the A5 kind as a cross-category link.
- **Wall clocks**: A5. Cross-category link from the wall-decor group only.
- **Mass-market pictures, posters and canvas prints** (Hoeffner "Bilder", IKEA "Wall decor"): other category F2. Key step 20 covers prints and posters "whatever the edition or price", and K-139 says "Posters are F2". No B4 kind. A cross-link sits in the wall-decor group.
- **Wall stickers and decals**: new kind in B4.1.2 Bowls & decorative objects, after decorative wall panel. Name: "Wall sticker or decal". Definition: "a self-adhesive vinyl or film motif, pattern or lettering applied to a wall, window or furniture to decorate it". Reason: it is applied ornament, not a picture made to be hung or looked at as one (step 20). Provisional until a shop page shows wall stickers sold as a type. Signs (Hoeffner "Schilder") are covered by B4.8.2.
- **Decorative lantern (†)**: noted. The Hoeffner Accessoires page (https://www.hoeffner.de/accessoires_medium, full) lists lanterns as a decor type, which supports the kind at attestation.
- **Candle-holder types**: keep one kind "candle holder" (K-180), with the attribute `holder_form` (candlestick, candelabrum, tealight holder, votive holder, candle plate, wall sconce for candles, hurricane). Instruction for the harvest: if a fetched shop sells and compares candlesticks, candelabra or tealight holders as their own categories, raise them as kinds in the post-harvest pass. Provisional.
- **Windsock sentence** (for the memo and the next key revision): "A windsock made to show wind direction or strength (airfield, weather or site use) is C6 (step 23). A wind streamer or windsock made as a garden, festive or decorative ornament, the koinobori included, is B4.8.1." Rename the B4 kind "Decorative windsock or wind streamer". Step 30 lists windsocks in B4 and step 23 lists them in C6, so this goes to the framework conflicts log.
- **IKEA wrapping, noticeboards and storage boxes**: other categories (C5 for wrapping and noticeboards, B1.5.1 for storage boxes). Cross-links only.
- **Thin evidence**: noted. The quality markers and signals stay provisional (no community or test source was fetched).
- **Attributes to store**: holder_form, scent_family, wax_type, burn_time_h, chime_tuning.

## B5
- **Saute pan**: new kind in B5.1.1 Pans, after frying pan or skillet. Definition: "a wide pan with straight or high sides and usually a lid, for frying, braising and reducing". Its form differs from the sloped frying pan. IKEA Singapore sells "Saute pans" as a category (HOL_EV, https://www.ikea.com/sg/en/cat/cookware-kt003/?page=3, full). Next free number in B5.1.1.
- **Cookware set**: new kind, overriding the memo's default "mixed set by item of greatest value" for this one set. S3a admits a kit sold and compared as one object. Food Network and Consumer Reports rate cookware sets as units (HOL_EV, https://www.foodnetwork.com/how-to/packages/shopping/product-reviews/best-cookware-sets, full), and IKEA has a "Cookware sets" category. The set holds pans (B5.1.1) and pots (B5.1.2), so it is the final mixed kind of B5.1 with `leaf = null`, id B5.1.0.01 (R-58 leaf 0). Definition: "a set of pots and pans of one maker line, sold and rated as one object". The pieces list goes in `set_contents`. Dinner sets, cup-and-saucer sets and knife-block sets stay mixed sets filed by their item of greatest value, until a fetched tester compares them as one object.
- **Rice-cooker technology tiers**: attribute `heating_technology` (conventional, micom, IH, pressure IH) on named forms. The body is the same (rule T), so these are not kinds. The page shows them as the rice-cooker ladder.
- **Large appliances** (refrigerator, wine fridge, dishwasher, oven, hob): display only, in their own group "Large kitchen appliances". No move.
- **Kitchen organisation** (Rakuten racks and rails): racks and rails that hold several objects are B1.5.2 (racks, hooks and hangers). The dish rack stays B5.6. Part racks made for one appliance go to B5.7. Cross-link from the kitchen view.
- **Stage-of-work sub-families**: kept as the placement index (ids unchanged). Display groups follow shop families: cookware; bakeware; kitchen appliances; large appliances; knives and boards; kitchen tools and measuring; food storage; dinnerware and serveware; glassware and drinkware; coffee and tea; bar and home brewing; clean-up and kitchen wear.
- **Williams Sonoma, Sur La Table and NSF fetches failed**: noted. US specialist navigation stays provisional.
- **Attributes to store**: hob_compatibility, cookware_material, oven_safe_c, set_contents, steel_hardness_hrc, handle_style, heating_technology.

## B6
- **Mop-only robot** (idealo "Wischroboter"): new kind "Robot mop" in B6.1.3 Mops, after spray mop. Definition: "a self-driving floor cleaner that mops with a pad or roller and has no suction". The body differs from the vacuum: there is no suction unit, the pad or roller is driven and it carries a water tank. A robot vacuum that also mops stays the robot vacuum, with `mop_system`. Provisional until the idealo category (or another shop's) is fetched.
- **Parts for washers, dryers and irons**: at build, add B6.6 leaves only as parts are attested. B6.6.2 "Washing-machine and dryer parts" is for the lint filter, inlet or drain hose made for the machine, door seal and dryer belt. B6.6.3 "Iron and steam-generator parts" is for the anti-scale cartridge and the water tank. All of these are from memory and provisional. A leaf with no attested kind is not created.
- **Reliability scheme**: Which? brand reliability survey (class ii), as a tier entry on the maker with scope = kind (needs).
- **Tree not built**: noted. Groups come with the build. The display follows the proposal's level-1 groups.
- **Attributes to store**: mop_system, dock_level, navigation, dust_handling, power, detergent_enzyme, fragrance.

## B7
- **Display group "Heat pumps and air conditioning"** across B7.1.1, B7.1.2 and B7.2.1: display only (no id change). It holds the hydronic and ground-source heat pumps, every B7.1.2 kind and the heat-pump water heater.
- **Hybrid (dual-fuel) heat pumps**: attribute `heat_pump_configuration`. **Absorption heat pumps**: attribute `heat_pump_drive`. A kind only if a fetched source ranks it apart (C10(b)). Provisional.
- **Off-grid and RV solar kits** (The Solar Store "Kits"): new kind "Off-grid solar kit" in B7.3.1 Generation, after the plug-in balcony solar kit. Definition: "panels, charge controller or inverter and usually a battery, sold as one kit to power a place without a grid connection". RV, van, boat and cabin are use tags. S3a admits a kit sold as one, and the specialist shop gives it its own category (HOL_EV, https://thesolarstore.com/collections?page=2, full). It differs from the balcony kit, which feeds the grid and has no storage. Provisional until the kit page itself is fetched.
- **Combi boiler packs** (Wickes): covered by the central-heating boiler's function attribute (combi). Unit of sale is an attribute.
- **Tree not built**: noted.
- **Attributes to store**: heat_pump_configuration, heat_pump_drive, heat_source, refrigerant, cold_climate_listed, grid_connection, capacity (unit named).

## B8
- **Build its kinds before the page**: noted. The tree and the R-58 ids of memo section 13 are loaded. Kinds go into data/kinds.tsv with the next build or attestation batch.
- **Fire-rated safe**: not a kind. A safe with a burglary grade stays B8.1.4.1, with the fire rating as `fire_rating`. A container rated against fire only stays B8.1.4.2. Widen its name to "Fire-resistant safe, document box or chest" (id kept). Alias row "fire safe" as a homonym with both targets (C9).
- **Gun safe**: covered by B8.1.4.6. Widen the name to "Firearms cabinet or gun safe" (id kept), with alias rows "gun safe" and "gun cabinet". The burglary and fire ratings tell the tiers apart (class i attributes). Long-gun capacity is an attribute.
- **Lockable window handle**: non-maker named form under window lock B8.1.2.3.
- **Biometric access lock**: attribute `access_method` on the lock kinds (deadbolt, knob or lever lockset, euro cylinder, multipoint lock) and on safes. The lock bodies are the same (C10).
- **Cash box and key box** (Testsieger): covered by B8.1.4.5 and B8.1.4.3.
- **Attributes to store**: burglary_rating, fire_rating, lock_security_rating, attack_resistance, access_method, alarm_sensor, alarm_power, video_storage.
- **Needs**: the safe, lock, alarm, gate and extinguisher standards; LPU belts (iii); Consumer Reports cameras (ii); camera ecosystems (C13).

## B9
- **Cigar vitola kinds**: the kind stays the generic vitola (memo 4b, about 16). Add Petit corona, Lonsdale, Double corona and Gordo (alias Grande) as kinds in B9.P2. Also add the other vitolas the memo's fetched S2 and S3 pages name: Corona gorda, Lancero, Panatela, Belicoso, Culebra, Diadema (alias Salomón). Mareva becomes an alias of Petit corona (factory name). Lonsdale is provisional until a page shows it.
- **Order of the vitola kinds**: Corona first. Then the other parejos by size: petit corona, corona gorda, lonsdale, robusto, toro, churchill, double corona, gordo, panatela, lancero. Then the figurados: torpedo, belicoso, perfecto, diadema, culebra.
- **Figurado**: display only. Two display groups, "Parejos" and "Figurados". Figurado is never a kind.
- **Pipe-tobacco blend kinds**: add Virginia blend and Virginia/Perique blend. Merge the memo's American blend into a "Burley-based blend", with "American blend" as its alias (the US trade name for Burley-forward blends). English blend (alias Balkan) and Aromatic blend stay. Order: Virginia, Virginia/Perique, Burley-based, English, Aromatic. This follows SmokingPipes University and TobaccoReviews (HOL_EV, https://www.smokingpipes.com/smokingpipesblog/single.cfm/post/smokingpipes-university-tobacco-families, full). The merge is provisional: if a fetched page sells American blend apart from Burley-based blends, it becomes a kind again.
- **Flake cut**: attribute `tobacco_cut`, not a blend kind.
- **maker_roles.tsv scoped split**: covered. The two scoped B9 rows exist (R-116 c).
- **Attributes to store**: wrapper_shade, cigar_strength, cigar_size, construction, tobacco_cut, in_production, draw_style, cannabinoid_content. Batch lab certificates are individual-item facts and are not stored (C16).
- **Needs**: Cigar Aficionado (iii); TobaccoReviews (iii); maker pipe grades (iv); the wrapper-shade classification; the heated-tobacco and pod platforms.

## B10
- New kinds (attestation batch HV_B10_NK3):
  - B10.2.1.05 Veterinary diet (cat)
  - B10.2.1.06 Freeze-dried or air-dried cat food
  - B10.4.2.08 Lead rope
  - B10.12.5.01 Reins (new parts leaf B10.12.5 "Bridle")
  - B10.7.5.01 Cage-bird food (new leaf B10.7.5 "Feed and treats")
  - B10.9.3.02 Hive tool (gap found in the quality markers; memo §9 names hive tools B10)
  - B10.9.3.03 Queen-rearing kit, B10.9.3.04 Queen cage and B10.9.3.05 Grafting tool (provisional)
- Bee suit, veil and gloves: A1 (K-105). Candle-making equipment: C4.
- Parts sub-family B10.12 shown under the animals: display only. The new bridle-parts leaf joins the horse groups (groups changes).
- Fish, reptile and bird gear groupings: noted, provisional (no specialist page fetched).
- No moves: no stored named form belongs to a new kind.
- **Attributes to store**: life_stage, dog_size, health_need, nutritional_adequacy, grain, protein_source, riding_discipline, horse_size, saddle_fit, bit_fit, water_type, tank_volume_l, uvb_output, hive_box, cage_bird_species, bird_food_form, applies_to (listed in the attributes file).
