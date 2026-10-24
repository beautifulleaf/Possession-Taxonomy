# F4 Religious & Ceremonial Objects: decided tree

Category: F4 Religious & Ceremonial Objects (domain F). Membership test (step 14, with the step 7 note for relics): objects made for religious or spiritual practice and for the dead: what is set up to be venerated, what a practitioner holds, counts, kneels on or carries to pray, what is handled in a rite, what is lit, burned or set out, what is read or cast in divination, what holds the remains, marks the dead or covers the body or coffin, and parts made for one of these objects. Religious dress is A1, worn jewellery (a medal with chain or bail, a mala made as a necklace, ash jewellery) A3, printed religious texts F1, ketubahs and certificates F5 or F2, religious-subject art in another form F2 or B4, food and drink as eaten J, unworked stones and fossils F6, plots and buildings G2. Structure (Candidate A, decided): sub-family (the role the object plays in the practice, set by the in-category precedence below), then leaf (one axis stated per sub-family), then kind (the generic form a person can own, C11), then named form (tradition form, style, iconic design or maker's design, `maker_bound` yes or no, uncapped; not listed here). At most four levels (CV-16); every sub-family keeps its leaves as the memo decided (F4.2, F4.5, F4.6 and F4.7 may drop the leaf level, but the frozen ids keep it). Tradition and sect are a multi-valued C8 scene tag and a generated view, never a level, and no tradition name is an exception kind (F-3, CV-27); butsudan, kamidana, rosary, tasbih, mala, juzu, icon, thangka, chalice, kiddush cup, omamori and the like are named forms. These are attributes or tags and never kinds or leaves: tradition and sect, occasion, life-cycle stage, iconography (the figure shown), material, size and capacity (`capacity_class` on the cremation urn, C6), installation (wall-hung, C12), power source (electric or LED candles, C10), user (adult, child, pet; men, women), setting (home, congregation, grave, travel), region, era, maker and price band. No tier sits on any kind (C4(a)): steel gauge is a measured-spec attribute with its standard named (C4(c) class (i)), `relic_class` is a classification attribute, the kosher scroll grade is one C16 grading-scale registry row with no value stored, and a scribe's rabbinical certification is a `certifications` value on the maker row (a standard, never a tier). Memo section 14 (DPH, binding, R-118 a) adds attributes and no kinds: on the prayer rug `padding` (unpadded, padded), `non_slip_base` (yes, no) and `surface_fabric` (velvet, cotton, synthetic), with the travel mat a setting tag, not a named form; on maker-bound prayer-bead named forms `bead_treatment` (natural; treated, dyed or stabilised; imitation; wording provisional), `bead_count` and `bead_size_mm`; juzu wearer is a user tag. Maker role: owner (maker_roles.tsv, provisional): workshops, scribes, candle makers, Judaica designers, urn design houses and tarot publishers enter through named forms and lines in the shared, uncapped maker ledger. Sub-family and leaf names are the memo's; the display groups of the navigation proposal (proposals.tsv level1_groups: Home altars, shrines and sacred images; Prayer and devotion aids; Ritual vessels, implements and sacred scrolls; Lamps, candles, incense and offerings; Tarot, oracle and divination; Funeral and memorial; Fittings for one sacred or funerary object) map one to one onto F4.1 to F4.7, are display only and never change a home or an id; the tradition front-door filter, the occasion view, the tarot publisher tab and the cross-link views (religious jewellery in A3 beside the devotional medal; printed texts in F1; monastery products in their product categories; memorial tablet beside the household altar; ritual candle with ritual incense) are generated views. Kind ids are the adopted ids of memo section 13 (frozen tree audit/KL_F4_tree.md), kept exactly; kinds are listed in the order of the memo's section 3.4 worked tree (67 kinds). A kind marked † has no fetched page attesting it as an owned object and enters the data only on its own fetched page (memo section 10). Kinds whose generic label alone was written in the conformance or decision pass ("label †" in the memo) have attested named forms and are not marked here; the map records them as "label †".

Ids (R-58): F4.n is a sub-family and F4.n.m a leaf; a kind is F4.n.m.kk, or F4.n.kk where a sub-family has no leaf.

## F4.1 Altars, shrines and sacred images

Leaf axis: the form of the sacred focus (altar or shrine; flat image; three-dimensional image; relic and its container). Sub-family test: what is set up to be venerated. Display group: Home altars, shrines and sacred images.

### F4.1.1 Altars and shrines
- F4.1.1.01 Household altar or shrine: cabinet, shelf or box shrine kept in a home or room to hold sacred images, name tablets or talismans; style (modern, karaki, gold-leaf), wall-hung installation and compact or mini size are attributes.
- F4.1.1.02 Shrine boundary rope: rope hung to mark a sacred space or object in a rite (shimenawa a named form); a seasonal festival decoration such as the kadomatsu is B4. †

### F4.1.2 Flat images
- F4.1.2.01 Devotional panel painting: sacred picture painted on a rigid panel, framed or mounted to stand or hang (icon a named form).
- F4.1.2.02 Devotional scroll painting: sacred picture painted or printed on cloth or paper and mounted as a hanging scroll or rolled for hanging (thangka, kakejiku honzon scroll, pata).
- F4.1.2.03 Altarpiece: large sacred picture or carved screen made to stand behind or above an altar, old-master altarpieces included (K-108).

### F4.1.3 Three-dimensional images
- F4.1.3.01 Devotional statue: sculpted figure of a holy person, deity or saint made to be venerated; the figure is an iconography tag, not a kind.
- F4.1.3.02 Devotional cross: cross, with or without a figure on it, made to stand, hang or be held in veneration (crucifix a named form).
- F4.1.3.03 Nativity set: boxed or composed set of figures and a stable showing the birth of Jesus, sold and compared as one set (K-1). †

### F4.1.4 Relics and reliquaries
- F4.1.4.01 Relic: body part or belonging of a holy person, or a thing touched to one, kept for veneration; `relic_class` (first, second, third) is a classification attribute.
- F4.1.4.02 Reliquary: case or container made to hold and show a relic.

## F4.2 Personal devotion aids

Leaf axis: how the aid is used (counted; knelt or sat on; turned or flown; held, carried or used to bless). Sub-family test: what the practitioner holds, counts, kneels on or carries to pray. Display group: Prayer and devotion aids.

### F4.2.1 Counted
- F4.2.1.01 Prayer beads: string or loop of beads, knots or counters made to count prayers, with or without a cross, counter, tassel or guru bead (rosary, chaplet, tasbih, mala, juzu named forms); a necklace of the same beads made as jewellery is A3 (K-111).

### F4.2.2 Knelt or sat on
- F4.2.2.01 Prayer rug: rug or mat made to kneel, stand or prostrate on in prayer; `padding`, `non_slip_base` and `surface_fabric` are attributes, travel and children's are setting and user tags; a meditation cushion or mat is B2 (K-113).

### F4.2.3 Turned or flown
- F4.2.3.01 Prayer wheel: cylinder holding written prayers, turned by hand, wind or water.
- F4.2.3.02 Prayer flag: cloth flag printed with prayers or sacred images, hung to be blown by the wind.

### F4.2.4 Held, carried or used to bless
- F4.2.4.01 Devotional medal: loose medal of a saint or sacred subject made for devotion; one made with a chain or bail to be worn is A3, one struck to commemorate or reward F3 (K-107). †
- F4.2.4.02 Prayer card: printed card with a sacred image or prayer, kept or carried for devotion (K-112).
- F4.2.4.03 Holy-water font [stoup]: small basin for holy water, hung or stood by a door or in a room.
- F4.2.4.04 Holy-water bottle: bottle or flask made to hold blessed water. †
- F4.2.4.05 Carried protective charm: small charm carried, not worn as jewellery, for luck, protection or a named blessing (omamori, carried evil-eye charm); worn A3, issued for money F3 (K-117). †

## F4.3 Ritual vessels, implements and instruments

Leaf axis: how the object is handled in the rite (vessel; hand implement; text-bearing object; sound-maker). Sub-family test: what is handled in the rite. Display group: Ritual vessels, implements and sacred scrolls.

### F4.3.1 Vessels
- F4.3.1.01 Ritual cup: cup or goblet made to hold wine or another drink used in a rite (chalice, kiddush cup named forms).
- F4.3.1.02 Monstrance: display vessel with a window or frame, made to show a consecrated host.
- F4.3.1.03 Ritual food plate [seder plate]: plate or tray made to hold the symbolic foods of a rite; the food itself is not F4.

### F4.3.2 Hand implements
- F4.3.2.01 Aspergillum: sprinkler for holy water.
- F4.3.2.02 Torah pointer [yad]: slim rod ending in a pointing hand, held to follow the text when reading a scroll aloud.
- F4.3.2.03 Ritual sceptre [vajra]: short sceptre held in the hand in a rite.
- F4.3.2.04 Ritual knife: knife or blade made to be held in a rite, not to cut (athame, boline named forms).

### F4.3.3 Text-bearing objects
- F4.3.3.01 Doorpost scroll case [mezuzah case]: case made to hold a doorpost scroll and be fixed to a doorpost; material is an attribute.
- F4.3.3.02 Doorpost scroll [mezuzah scroll]: handwritten parchment strip of sacred text made to be put in a case and fixed to a doorpost; `script_style` and size class (to fit the case) are attributes, the kosher grade a registry row only.
- F4.3.3.03 Phylacteries [tefillin]: pair of small boxes holding handwritten sacred passages, with straps, made to be strapped to the arm and head in prayer.
- F4.3.3.04 Handwritten Torah scroll: handwritten scroll of the Five Books on parchment, made to be read in the rite; a printed Torah or Bible is F1 (K-112). †

### F4.3.4 Sound-makers
- F4.3.4.01 Ritual horn [shofar]: horn made to be blown in a rite.
- F4.3.4.02 Hand bell: bell held by a handle and rung in a rite or service (altar bell, sanctus bell, ghanta named forms).
- F4.3.4.03 Standing bowl bell: bowl-shaped bell that rests on a cushion or stand and is struck with a striker, made for a rite (rin; singing bowl only when made for a rite, otherwise E3, K-110).
- F4.3.4.04 Slit drum: hollow wooden block struck to keep rhythm in chanting (mokugyo a named form).

## F4.4 Light, incense and offerings

Leaf axis: what is lit, burned or set out (lamp and candle; incense and its burner; offering vessel and stand). Sub-family test: what is lit, burned or set out. Display group: Lamps, candles, incense and offerings.

### F4.4.1 Lamps and candles
- F4.4.1.01 Hanukkah lamp: nine-branch lamp or candle holder, eight places for the festival lights and one for the helper light.
- F4.4.1.02 Seven-branch menorah: seven-branch lamp or candle holder.
- F4.4.1.03 Oil lamp for worship: lamp burning oil or ghee, made for worship (diya, butter-lamp holder named forms).
- F4.4.1.04 Eternal light [sanctuary lamp]: lamp kept burning before a sanctuary or altar; electric or LED is a power attribute.
- F4.4.1.05 Altar candlestick: candle holder made to stand on or by an altar in a rite; an open candle holder for the home is B4 (K-180).
- F4.4.1.06 Ritual candle: candle made for a rite or devotion, including altar, votive, procession, Easter, grave, Yahrzeit and memorial candles (K-113); occasion is a tag, wax content and power attributes.
- F4.4.1.07 Advent wreath: wreath with candles used to count the weeks before Christmas. †
- F4.4.1.08 Ritual lantern: lantern made to be hung or set out in a rite or as a shrine offering (bon lantern, votive stone tōrō named forms); a garden tōrō or decorative lantern is B4, a lantern made to be carried as a light B3 (K-116, K-180).

### F4.4.2 Incense and burners
- F4.4.2.01 Ritual incense: incense made for a rite, in stick, cone, resin or church grade (senko, agarbatti named forms; a smudge bundle made for a named rite, K-115).
- F4.4.2.02 Incense burner: standing or hanging vessel for burning incense (koro, joss-stick pot, dhoop stand named forms; grave incense holders with setting tag grave).
- F4.4.2.03 Swung censer: incense burner hung on chains, to be swung.

### F4.4.3 Offering vessels and stands
- F4.4.3.01 Offering vessel: bowl, cup or vase made to hold water, rice, tea, flowers or other offerings (rice vessel, tea cup, altar flower vase; grave flower vases with setting tag grave).
- F4.4.3.02 Offering stand: stand or tray made to hold offerings.

## F4.5 Divination and esoteric tools

Leaf axis: deck, or other tool. Sub-family test: what is read or cast. Display group: Tarot, oracle and divination.

### F4.5.1 Decks
- F4.5.1.01 Tarot deck: 78-card deck with major and minor suits, sold for divination; each published deck design is a maker-bound named form under its publisher; a pack sold for card play is E1 (K-109).
- F4.5.1.02 Oracle deck: deck of cards with its own set of images and messages, any number of cards, sold for divination.
- F4.5.1.03 Lenormand deck: 36-card deck of the Lenormand pattern, sold for divination.

### F4.5.2 Other tools
- F4.5.2.01 Crystal ball: sphere used for scrying.
- F4.5.2.02 Spirit board: lettered board with a pointer, made for divination; made as a board game it is E1 (K-114). †
- F4.5.2.03 Rune set: set of stones, wood or tiles marked with runes, made for casting. †
- F4.5.2.04 I Ching coin set: coins or sticks made for casting the I Ching. †
- F4.5.2.05 Divination pendulum: weight on a chain or cord, made to be dangled for divination. †

## F4.6 The dead

Leaf axis: coffin; urn; marker; furnishing. Sub-family test: what holds the remains, marks the dead, or covers the body or coffin. Display group: Funeral and memorial.

### F4.6.1 Coffins
- F4.6.1.01 Coffin or casket: box that holds a body for burial or cremation; material, steel gauge, shape, sealing and biodegradable are attributes (rental casket a named form).

### F4.6.2 Urns
- F4.6.2.01 Cremation urn: container for cremated remains, of any capacity from a keepsake portion to a companion pair (`capacity_class`); not a worn piece of jewellery (F4-O1); pet urns carry a user tag.
- F4.6.2.02 Scattering urn: container made to release ashes on land, water or from the air.
- F4.6.2.03 Urn vault: outer box or liner made to hold an urn in the ground.

### F4.6.3 Markers
- F4.6.3.01 Grave marker: stone or plaque set on or at a grave (tombstone, tomb slab named forms).
- F4.6.3.02 Memorial tablet: tablet that stands for a dead person, inscribed with a name, kept at an altar or home (ihai a named form).

### F4.6.4 Furnishings
- F4.6.4.01 Funeral pall: cloth laid over a coffin (coffin cover a named form).
- F4.6.4.02 Burial shroud: cloth or set of cloths that wrap the body.

## F4.7 Parts and accessories made for one religious or funerary object

Leaf axis: the object served (CV-17, C5(d); opened by F-19). Display group: Fittings for one sacred or funerary object.

### F4.7.1 For Torah scrolls
- F4.7.1.01 Torah finial: ornament fitted to the top of a scroll's rollers.

### F4.7.2 For coffins
- F4.7.2.01 Coffin plate: plate fixed to a coffin, naming the dead.
- F4.7.2.02 Coffin pillow: pillow made for the inside of a coffin.

### F4.7.3 For cremation urns
- F4.7.3.01 Urn appliqué or medallion: plaque, appliqué or medallion made to be fixed to an urn.

## Precedence inside F4

- A part or accessory made for one F4 object goes to F4.7 first (CV-17). A doorpost scroll case is not such a part: it is the object fixed in the rite and is F4.3.3.01 (R-60 f; whether it moves to F4.7 under K-9 is an open owner question, memo section 12).
- Otherwise test in this order: the dead (F4.6: holds remains, marks the dead, covers the body or coffin), divination (F4.5), light, incense and offerings (F4.4: lit, burned or set out), sacred focus (F4.1), rite implement (F4.3), personal aid (F4.2).
- So a memorial lamp lit in a rite stays a lamp in F4.4.1 with a memorial tag, a grave light is a ritual candle (F4.4.1.06), an ihai on a butsudan marks the dead (memorial tablet F4.6.3.02), and an urn that holds ashes is F4.6 whatever its decoration.
- Lit objects are F4.4, not F4.1: a sanctuary lamp is the eternal light (F4.4.1.04) and an altar candle a ritual candle (F4.4.1.06), even where they stand at an altar; a candle holder made for a rite is the altar candlestick (F4.4.1.05).
- A keepsake or companion urn that is not worn stays a cremation urn (F4.6.2.01), capacity an attribute; a container made to release ashes is a scattering urn (F4.6.2.02); worn jewellery holding ashes is A3.
- A burner hung on chains to be swung is a swung censer (F4.4.2.03); a standing or hanging burner that is not swung is an incense burner (F4.4.2.02).
- Grave goods (memo section 14): grave stones and plaques are grave markers (F4.6.3.01); grave flower vases are offering vessels (F4.4.3.01) and grave incense holders incense burners (F4.4.2.02), each with setting tag grave; grave lights are ritual candles (F4.4.1.06); grave-cleaning brushes and cleaners are B6.
- The doorpost scroll (F4.3.3.02) and its case (F4.3.3.01) are two kinds compared separately; the text inside a mezuzah or tefillin is part of the ritual object, and a handwritten Torah scroll used in the rite is F4.3.3.04 (K-112).
- A holder or case made to hold and show a relic is a reliquary (F4.1.4.02), not a relic.
- A bowl-shaped bell, drum or horn made for a rite is F4.3.4; the same instrument made for meditation, sound baths or music is E3 (K-110).
- A deck, board or set made for divination is F4.5; a pack made for card play or a board game is E1 (K-109, K-114).
- A ritual implement that holds food or drink is F4.3.1 (ritual cup, ritual food plate); the food and drink are J.
- A Masonic or other fraternal ritual implement is filed under the F4 kind its form matches (ritual cup, hand implement, ritual candle); worn regalia are A1 and A3, insignia of office F3 (K-115).
- Sets and kits (K-1): a set of one kind is filed as that kind; a mixed set (mass set, altar-fitting set) is filed by its item of greatest value (the ritual cup; the incense burner or standing bowl bell) with its contents listed; a kit sold, standardised and compared as one object is a kind (the nativity set, F4.1.3.03).
