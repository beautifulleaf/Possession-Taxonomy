# F3 Coins, Stamps, Medals & Trading Cards: decided tree

Category: F3 Coins, Stamps, Medals & Trading Cards (domain F, Culture, Records & Meaning). Membership test (placement key step 15, with K-27, K-107, K-117 to K-123): money, postage or an award in physical form: coins, banknotes and bullion (in circulation or not), postage stamps and postal stationery, medals and decorations, trophies, cups, shields, award plaques, championship rings and belts, regalia and insignia of office (maces, chains of office, gavels), tokens and scrip, non-game trading cards and collectible sticker series of the Panini type; and the parts made to hold or serve one coin, note, stamp, medal or card (S3). Not here: paper certificates, diplomas, share and bond certificates, cheques, traveller's cheques, postal orders, vouchers redeemable only with their issuer, payment, gift, telephone, transit, membership and key cards, picture postcards and any cover that is neither administration-issued nor first-day, advertising trade cards (F5); trading card games and their cards even when graded, casino and poker chips, game money, a token made to be used up in one coin-operated game or machine, toy crowns, collectible figures (E1); artist trading cards and free-standing figures made to be looked at (F2); devotional medals loose and carried luck tokens (F4); pins, badges and patches worn as ornament, a coin or ingot mounted to be worn, a devotional medal made to be worn, a crown or tiara worn as an ornament (A3); commemorative plates (B4 or B5) and wall plaques with no award function (B4); albums, binders, stock books, trays and coin tubes that hold several objects (B1); general-use stickers (C5); weapons made to fight (E4); native gold and element samples (F6); digital cards and tokens (I2); cryptocurrency holdings and individual unique items (OUT). Structure (Candidate A, decided, F-1; memo sections 3, 4b, 9, 10, 12 and 14): sub-family by issuing function (coin, paper money, bullion, token or scrip, postage, medal or insignia, award, card; F3.1 to F3.8), then the parts sub-family F3.9 (C5(d), exempt from that axis; leaf axis: object served), then leaf by the standing, form or purpose of the issue (F3.3 Bullion and F3.7 Trophies & awards have no leaf, `leaf = null`, C5(b)), then kind (the generic piece or class a person owns, stopping above the type, where the grade market sits), then named form (series, issue or iconic design, uncapped, `maker_bound` flagged; card product lines are C1 line rows; not listed here). Issuer and country, era, denomination, currency, year, metal, fineness, weight, `finish` (circulation strike, brilliant uncirculated, proof, reverse proof, bullion finish; Stempelglanz an alias of brilliant uncirculated, section 14), `unit` (single, strip, block, plate block, full sheet, roll, bag, set), `issue_class`, `postal_service`, `issuer_type`, `product_form`, `material`, theme, sport, league, franchise, event, occasion, rookie status, size (full-size or miniature), original or replica, catalogue number (identifier, after the licence check, F-14), maker, tier and price band are attributes, tags, identifiers, ledger rows or views, never kinds or leaves; error, die-variety, replacement-note, fancy-serial, parallel and numbered-card varieties are C3 variants; no grade value is stored (C16): the Sheldon, PMG, IBNS, stamp centering and gum, Mystic premium (platform label) and card-grader scales (PSA, BGS, SGC, CGC Cards, ACE, TAG) are grading-scale registry rows only (section 14). Huntington "Back of Book" and the issuer classes "Chinese stamps" and "overseas stamps" are views or issuer tags, never kinds (section 14). Maker role (maker_roles.tsv, provisional): owner for the whole category (issuers in the issuer table, mints, refiners, printers and card manufacturers through issues and lines; graders as certifier rows). Pending kinds: the memo marks 8 kinds † (chain of office, gavel, crown of office, championship belt, championship ring, medal ribbon, medal case, card toploader or sleeve; section 10 attestation list); their ids are allocated here in memo order, each line ending in †, and a † kind enters the data only when a fetched page attests it. The stamp-mount name in F3.9.2.01 and the Panini-type series names behind F3.8.2.01 are partly † (the kinds themselves are attested). Provisional homes: bullion coin F3.3.03 against non-circulating legal-tender coin F3.1.2.01 turns on finish and packaging, provisional until a mint page states the finishes (F3-O1); Confederate Currency and Military Payment Certificates sit as named forms under F3.4.4.01 until the issuer test is read (F-16); the alias 特殊切手 on F3.5.1.02 needs a fetched source for the term. Display groups (navigation proposal, display only, never moving a home; no group ids issued; display order follows Huntington, stamps and coins with bullion beside coins, section 14): Coins (F3.1); Bullion (F3.3); Banknotes and paper money (F3.2); Stamps and postal items (F3.5); Trading cards and stickers (F3.8); Medals, orders and insignia (F3.6); Tokens and scrip (F3.4); Trophies and awards (F3.7); Holders, slabs and mounts for one item (F3.9). Side views: a mint and refiner tab for bullion, a card brand tab, and generated views by issuer, era, theme and series and a "graded by" view over the scale registry; country is a filter inside them, never the front door. Quality markers (display, judged on the named form, line or maker or on the individual item, never on the kind; no grade stored): coins by wear (circulated grades), strike, contact marks, luster and eye appeal on the Sheldon ladder P-1 to MS-70, with proof and uncirculated a finish, not a condition, and mintage and die varieties adding rarity; stamps by correct identification, then condition and faults (thins, tears, repairs, re-perforation, regumming), gum (MNH > LH > HH > HR > OG > NG > RG), centering and margins (Gem > Superb > XF > VF > F > VG > poor), perforations, colour, cancellation and scarcity (Japan: issue era, unused full sheet with margins, gum, issue quantity, imprint, first-day postmark); cards by centering, corners, edges and surface, then the grader and grade; bullion by metal and fineness, weight, mint or refiner and premium over spot (price, not stored); banknotes on the PMG 70-point scale with EPQ; medals by place in an order of wear (scheme) then condition (no scale fetched); tokens and trophies by preference.

Ids (R-58): F3.n is a sub-family and F3.n.m a leaf; a kind is F3.n.m.kk, or F3.n.kk where a sub-family has no leaf.

## F3.1 Coins
Leaf axis: standing of the issue (circulating; collector; local and emergency; copies). Ancient and medieval coins share these kinds with `era` and `issuer` tags (F-14); denomination is an attribute; a roll or bag of like coins is the coin with `unit` (F3-7). Display group: Coins.

### F3.1.1 Circulating coins
- F3.1.1.01 Standard circulation coin: legal-tender coin struck for everyday circulation; a worn coin sold for its silver content (junk silver) is this kind with `metal_content` an attribute.
- F3.1.1.02 Circulating commemorative coin: legal-tender coin with a commemorative design issued into circulation at face value.

### F3.1.2 Collector coins
- F3.1.2.01 Non-circulating legal-tender coin: legal-tender coin issued for collectors, not circulation, including any coin struck in proof, reverse proof or another collector finish or issued in a mint's presentation packaging, even in gold.
- F3.1.2.02 Proof or mint set: set of coins issued and sold by a mint as one packaged product (the only set kind, K-1, S3a).

### F3.1.3 Local and emergency issues
- F3.1.3.01 Emergency coin: coin struck by an official authority in an emergency, such as a siege coin or official necessity coin.
- F3.1.3.02 Pattern or trial strike: coin struck to test a design, die or metal and not issued for circulation.

### F3.1.4 Copies
- F3.1.4.01 Replica, fantasy or counterfeit coin: copy of a coin, a coin-like piece of an issue that never existed, or a contemporary counterfeit made to pass as money.

## F3.2 Banknotes and paper money
Leaf axis: standing of the issue (circulating; non-circulating; local; copies). Paper circulated as money by a non-currency issuer is F3.4.4.01 (F-16); paper or polymer substrate is an attribute. Display group: Banknotes and paper money.

### F3.2.1 Circulating notes
- F3.2.1.01 Standard circulation note: banknote issued by a currency authority for everyday circulation.
- F3.2.1.02 Circulating commemorative note: banknote with a commemorative design issued into circulation at face value.

### F3.2.2 Non-circulating notes
- F3.2.2.01 Non-circulating note: legal-tender note issued for collectors and not put into circulation.
- F3.2.2.02 Specimen, trial or pattern note: note printed as a specimen, proof, trial or pattern, or prepared and never issued.

### F3.2.3 Local notes
- F3.2.3.01 Local or obsolete note: note issued by a local or private bank, or of an issue that is no longer current, such as US obsolete currency and National Banknotes.

### F3.2.4 Copies
- F3.2.4.01 Facsimile, fantasy or counterfeit note: facsimile of a real note, a note of an issue that never existed, or a contemporary counterfeit.
- F3.2.4.02 Prop or souvenir note: note-like piece made as a film prop, demonstration note or souvenir and not legal tender (K-120).

## F3.3 Bullion
No leaf (`leaf = null`; three kinds, C5(b)). Kind axis: form. Metal, fineness (millesimal fineness a class (i) standard) and weight are attributes; the mint or refiner is a maker row (LBMA Good Delivery a certification). Display group: Bullion (beside Coins).
- F3.3.01 Bullion bar: cast or minted bar of precious metal sold by metal content and weight.
- F3.3.02 Bullion round: coin-shaped piece of precious metal that is not legal tender, sold by metal content.
- F3.3.03 Bullion coin: legal-tender coin struck in a mint's bullion programme in the standard bullion finish.

## F3.4 Tokens and scrip
Leaf axis: what the token stands for (a service; trade and wages; tax and dues; money issued by a non-currency issuer). The business served (milk, beer, bread, pharmacy) is the attribute `business`; `issuer_type` is an attribute of F3.4.4.01. Display group: Tokens and scrip.

### F3.4.1 Tokens for a service
- F3.4.1.01 Transit and toll token: token issued to pay one fare or toll on a transit system, road or bridge.
- F3.4.1.02 Deposit token (locker or shopping cart): token issued to release a locker, shopping cart or similar deposit mechanism.

### F3.4.2 Tokens for trade and wages
- F3.4.2.01 Trade token or good-for piece: token issued by a merchant or private issuer to be exchanged for goods or a stated value.
- F3.4.2.02 Wage, work or ration token: token issued to workers as wages or work tally, or as a ration entitlement.

### F3.4.3 Tokens for tax and dues
- F3.4.3.01 Tax token: token issued to pay sales tax or another tax in fractions of the smallest coin.

### F3.4.4 Emergency money and scrip
- F3.4.4.01 Emergency money and scrip: paper or other money issued to circulate as money by a non-currency issuer (F-16).

## F3.5 Postage and postal items
Leaf axis: postal item type (adhesive stamp; stamp unit; postal stationery; cover; fiscal label); inside Adhesive stamps the axis is issue class. `issue_class`, `postal_service` and `unit` are attributes; plate block is a `unit` value (section 14). Display group: Stamps and postal items.

### F3.5.1 Adhesive stamps
- F3.5.1.01 Definitive stamp: everyday postage stamp of an ongoing series with no specific subject or issue code.
- F3.5.1.02 Commemorative or special-issue stamp [特殊切手]: postage stamp issued for a limited period to mark an event, subject or season.

### F3.5.2 Stamp units
- F3.5.2.01 Miniature or souvenir sheet: small sheet issued as a unit with one or more stamps and a decorated margin.
- F3.5.2.02 Stamp booklet: folded booklet of stamps issued by a postal administration as one unit.

### F3.5.3 Postal stationery
- F3.5.3.01 Stamped envelope: envelope with a printed stamp issued by a postal administration.
- F3.5.3.02 Postal card with printed stamp: postcard with a printed stamp issued by a postal administration.

### F3.5.4 Covers
- F3.5.4.01 First-day cover: cover issued by a postal administration or prepared as a first-day cover, carrying stamps cancelled on their day of issue (K-118).

### F3.5.5 Fiscal labels
- F3.5.5.01 Revenue stamp: stamp issued to show payment of a tax or fee rather than postage.

## F3.6 Medals and decorations
Leaf axis: purpose (honours and decorations; service; commemorative and art; award and membership; insignia of office, folded in from the former Regalia sub-family, F-15). Kinds follow the generic purpose ladder (section 8); regime or period, full-size or miniature and original or replica are attributes; a named group to one recipient and a particular mace are individual items and out. Display group: Medals, orders and insignia.

### F3.6.1 Honours and decorations
- F3.6.1.01 Order, badge or star: insignia of an order of chivalry or merit (badge, star, collar or sash badge).
- F3.6.1.02 Gallantry decoration: decoration awarded for a specific act of gallantry or distinguished service.

### F3.6.2 Service medals
- F3.6.2.01 Campaign medal: medal awarded for service in a named campaign or operation.
- F3.6.2.02 Long-service and good-conduct medal: medal awarded for a length of service or record of conduct.

### F3.6.3 Commemorative and art medals
- F3.6.3.01 Commemorative medal: medal struck to mark an event, person or anniversary, such as a coronation, jubilee, birth or visit.
- F3.6.3.02 Art medal: medal or plaquette struck or cast as a work of medallic art.
- F3.6.3.03 Souvenir medal or elongated coin: souvenir piece struck or rolled for a place or event, including a coin rolled out with a new design.

### F3.6.4 Award and membership medals
- F3.6.4.01 Award medal: disc medal given for achievement in sport, school, military or other competition, sports finisher's medals included (F3-O2).
- F3.6.4.02 Challenge coin or membership medal: coin-shaped medal issued to members of a unit, club or organisation.

### F3.6.5 Insignia of office
- F3.6.5.01 Mace: ceremonial staff carried as insignia of a parliamentary, civic, academic or judicial office.
- F3.6.5.02 Crown of office: crown that is regalia of an office (K-123). †
- F3.6.5.03 Chain of office: chain or collar worn as insignia of a civic or other office. †
- F3.6.5.04 Gavel: mallet used as insignia of a presiding office. †

## F3.7 Trophies and awards
No leaf (`leaf = null`; eight kinds, C5(b)). Kind axis: form; `material` (metal, crystal, glass, acrylic, resin, wood), size, engraving and sport are attributes. Display group: Trophies and awards.
- F3.7.01 Cup trophy: cup-shaped trophy on a base, perpetual cups included.
- F3.7.02 Shield: shield-shaped award, usually with plates for engraved names.
- F3.7.03 Plaque: flat award panel with an inscription, made to hang or stand.
- F3.7.04 Upright award: column, figure, star, block or obelisk award on a base.
- F3.7.05 Bowl, tankard or salver: bowl, tankard, tray or salver given as an award.
- F3.7.06 Rosette or ribbon: rosette or ribbon given as an award.
- F3.7.07 Championship belt: belt awarded to a champion (K-119). †
- F3.7.08 Championship ring: ring awarded to the members of a championship team or to a champion (K-119). †

## F3.8 Trading cards
Leaf axis: product form (single cards; collectible stickers; sealed product). Sport, league and franchise are tags; card build, rookie status and `product_form` are attributes; a complete factory set is the card kind with `unit` = set; product lines are C1 line rows; parallels and numbered cards are C3 variants. Display group: Trading cards and stickers.

### F3.8.1 Single cards
- F3.8.1.01 Base card: standard card of a numbered sports or non-sports series issued by a card manufacturer.
- F3.8.1.02 Insert or autograph card: card inserted at a lower rate than the base set, including signed and relic cards.
- F3.8.1.03 Product-issued card: card printed on the box, panel or packaging of another product and cut from it (hand-cut cards).

### F3.8.2 Collectible stickers
- F3.8.2.01 Collectible sticker: sticker of a numbered series of the Panini type made to be collected into an album (K-121).

### F3.8.3 Sealed product
- F3.8.3.01 Sealed card product: unopened pack, box, blaster, hanger or case of cards, with `product_form` an attribute.

## F3.9 Parts and accessories made for one coin, note, stamp, medal or card
Leaf axis: object served (coin and note; stamp; medal; card) (C5(d)), then part type. Size and material are attributes. Display group: Holders, slabs and mounts for one item.

### F3.9.1 Coin and note
- F3.9.1.01 Coin capsule or holder: capsule, flip or holder made to hold one coin or note.
- F3.9.1.02 Grading slab: sealed holder in which a grader encapsulates one coin, note or card.

### F3.9.2 Stamp
- F3.9.2.01 Stamp hinge or mount: hinge or clear mount made to fix one stamp in place.

### F3.9.3 Medal
- F3.9.3.01 Medal bar or ribbon bar [Ordenspange, Bandspange]: bar on which medals or their ribbons are mounted for wear.
- F3.9.3.02 Medal ribbon: length of ribbon made for one medal or decoration. †
- F3.9.3.03 Medal case: case made to hold one medal or decoration. †

### F3.9.4 Card
- F3.9.4.01 Card toploader or sleeve: rigid toploader or soft sleeve made to hold one card. †

## Precedence inside F3

- One home per object: a named form, line row or variant is a ledger row under one kind and never a second home; region, era, issuer, metal, denomination, sport, franchise, grade, edition, maker and collecting discipline never divide the tree (Candidates B and C and the Huntington order are generated views, section 14).
- A coin struck in a mint's bullion programme, in the standard bullion finish, is a bullion coin (F3.3.03); the same design struck as proof, reverse proof or another collector finish, or issued in a mint's presentation packaging, is a non-circulating legal-tender coin (F3.1.2.01); a worn circulation coin sold for its silver content is a standard circulation coin (F3.1.1.01) with a `metal_content` attribute (F3-O1, provisional until a mint page attests the finishes).
- A mint and proof set is a kind (F3.1.2.02); a roll or bag of like coins, a stamp single, strip, block, plate block or full sheet and a complete factory card set are the item they hold with `unit` as an attribute (K-1, S3a, F3-7).
- Paper or other money circulated by a non-currency issuer (scrip, emergency money, Notgeld, company scrip) is emergency money and scrip (F3.4.4.01), not a banknote kind (F-16); a voucher or gift certificate redeemable only with its issuer is F5.
- A token issued to stand for money or a service (transit, toll, deposit, trade, wage, tax: F3.4.1.01 to F3.4.3.01) is F3; casino and poker chips and a token made to be used up in one coin-operated game or machine are E1; payment, gift, telephone, transit, membership and key cards are F5 whether live, used or expired (K-118).
- Game money is E1; prop and souvenir notes are F3 (F3.2.4.02) (K-120).
- Postal stationery with a printed stamp (F3.5.3.01, F3.5.3.02) and a cover issued by a postal administration or prepared as a first-day cover (F3.5.4.01) are F3; any other used envelope, letter or picture postcard is F5, whatever stamps it carries, including a cover that passed through the post and is neither administration-issued nor first-day (K-118).
- An adhesive stamp has two kinds by issue class (F3.5.1.01, F3.5.1.02); airmail, postage due, official, semi-postal and express are `postal_service` values, not kinds (F3-O4).
- A disc medal, wherever sold, is a medal (F3.6), sports finisher's medals included (F3.6.4.01); a cup, shield, plaque, upright award, bowl, rosette, championship belt or championship ring is a trophy or award (F3.7.01 to F3.7.08) (F3-O2).
- A medal, order or decoration made as an award or commemoration is F3 whether it is worn, mounted on a bar or kept in a case (K-107); a medal bar or ribbon bar is a part (F3.9.3.01); a pin, badge or patch worn as ornament and not issued as an award is A3; an identity or access badge is F5.
- A medal made for devotion is F4 when loose and A3 when made with a chain or bail to be worn; a medal struck to commemorate or to reward, whatever its subject, is F3 (K-107). A token or charm made to bring luck or protection is F4 when carried, A3 when worn and F3 when issued for money (K-117).
- A coin or ingot made or mounted with a bail, loop or bezel to be worn is A3; one without a mount is F3 (K-122).
- A crown that is regalia of an office is F3 (F3.6.5.02); a crown or tiara worn as an ornament is A3; a toy crown is E1 (K-123). A sword, staff or mace carried as insignia of office and not made to fight is F3 (mace F3.6.5.01); a weapon made to fight is E4.
- Championship rings and belts are F3 awards (F3.7.08, F3.7.07) (K-119).
- A card made to be played in a game system is E1 even when graded, signed or never played; a non-game sports or entertainment card is F3 (F3.8) (F3-O3). An advertising or trade card issued by a business is F5; a card issued as part of a numbered series by a card manufacturer is F3. An artist trading card is F2.
- Collectible sticker series of the Panini type are F3 (F3.8.2.01) (K-121); stickers sold for general use are C5; messaging stickers are I2.
- An art medal struck or cast as a medal is F3 (F3.6.3.02); a free-standing figure made to be looked at is F2, and a figure made with an award plate or inscription field is F3 (F3.7.04).
- A trophy, cup, shield or award plaque is F3 whatever sport it names; signed or won sports equipment is still the equipment; a commemorative plate is a plate (B4 or B5); a wall plaque with no award function is B4.
- A capsule, slab, toploader, sleeve or case made to hold one coin, note, stamp, medal or card follows it into F3.9 (F3.9.1.01, F3.9.1.02, F3.9.3.03, F3.9.4.01); an empty album, binder, stock book, box, tray or coin tube made to hold several is B1 (K-9).
- A paper certificate or diploma, an award certificate, and a printed share or bond certificate, cheque, traveller's cheque or postal order kept as an object are F5 (K-27).
- A bullion bar, round or coin is F3 (F3.3.01 to F3.3.03); a nugget or specimen of native gold kept as a natural object, and an element sample, are F6.
- A card or coin that exists only as a token or file is I2; the printed card and the struck coin are F3; cryptocurrency holdings are out. Collectible figures, dolls and model vehicles are E1, even when sold in card-style collectible series.
