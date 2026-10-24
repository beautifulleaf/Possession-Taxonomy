# J6 Coffee, Tea & Cocoa: decided tree

Category: J6 Coffee, Tea & Cocoa (domain J, Groceries). Membership test: coffee, tea and cocoa as beans, leaves, powders or capsules, cocoa butter and cocoa paste, and other plant parts brewed as infusions (leaves, flowers, fruit, roots, bark, roasted grains), kava included, as bought (CATEGORIES_v0_7, K-50, K-51). Not here: ready-to-drink coffee and tea, kombucha, bubble tea and drinks already made (Culinary); a dry drink mix led by sugar, creamer or malt, and a sweetened or milk ready-to-drink (prepared, OUT; K-49, J6-O1); couverture, baking chocolate and chocolate chips, dried cooking herbs and spices sold in a jar, coffee syrup (J5); chocolate bars and confectionery (OUT); machines, grinders, kettles, teapots, infusers and filter papers (B5); recurring coffee or tea deliveries (I3); kratom, khat, areca, betel, cannabis and CBD teas and herbal smoking blends (B9); supplements, tinctures, capsules and extracts sold with a dose and a health claim (H2). Structure (Candidate A, memo sections 3 and 10): sub-family by the plant the product comes from (Coffea, Camellia sinensis, Theobroma cacao, any other plant), then leaf by one axis per sub-family (tea type by processing, ISO 20715, in J6.2; plant part infused in J6.4; no leaf in J6.1 and J6.3, leaf = null), then kind: the product as bought in coffee and cocoa, one kind per ISO tea type with one kind per defining process inside Green tea (J-15), and the herb or plant in infusions (J-15). Each object gets one kind. Whole bean or ground (grind), roast, origin and region, process (washed, natural, honey), variety (a row of the varieties table, never a kind; Geisha and others), single origin or blend, decaf (attribute `decaf`, JC4), brew target, pack form (loose, tea bag, pyramid bag, drip bag, tin, box), the dry-mix attribute `mix`, leaf grade, flush and harvest, raw (sheng) or ripe (shou) pu-erh and its pressed shape, cocoa alkalisation (natural, Dutch-process, black) and fat content, ICCO bean class, specialty grade (`specialty_grade`, SCA score with the 350 g defect gate), Cup of Excellence label, certifications, Direct Trade (a platform tag) and caffeine are attributes, tags or variants, never kinds; the capsule system is a C13 platform row. Named forms are origin or appellation names, blend styles, tea names, mate styles and maker-bound lines inside one kind; a line spanning kinds is a lines row (R-35). Maker role: none (maker_roles.tsv, provisional; grocery rule: origin, estate and grade replace the maker, roasters and estates enter through branded products, and a roaster, estate, tea house or pu-erh factory enters when a quality source names it, R-115 b; capsule-system owners stay C13 platform rows). A kind marked † is named by the memo without a fetched page and needs one before it enters the data (memo attestation list); the level of Pu-erh tea, Rooibos, Yerba mate and Kava is provisional until attested (CV-27, R-19). Tea capsules or pods, instant tea and liquid tea concentrate are J6 by decision but get no id until a fetched page attests them (J-14, J6-O1; R-96 c); an attested tea or cocoa capsule joins the coffee capsule kind and moves it to a J6 multi-use sub-family (J-14, CV-31). Display groups (navigation proposal, display only): G-J6-1 Coffee (J6.1; level 2 G-J6-10 Beans and ground J6.1.01, G-J6-11 Capsules and pods J6.1.04, G-J6-12 Instant and concentrate J6.1.03 and J6.1.05, G-J6-13 Green coffee for home roasting J6.1.02); G-J6-2 Tea (J6.2; level 2 G-J6-14 to G-J6-20 follow the leaves J6.2.1 to J6.2.7: white, green and matcha, yellow, oolong, black, pu-erh and dark, flavoured, scented and chai); G-J6-3 Cocoa & drinking chocolate (J6.3; level 2 G-J6-21 Cocoa powder and drinking chocolate J6.3.06 and J6.3.07, G-J6-22 Cacao beans, nibs, paste and butter J6.3.01 to J6.3.05, shells included); G-J6-4 Herbal & other infusions (J6.4; level 2 G-J6-23 Rooibos, mate and herb leaves J6.4.1, G-J6-24 Flower, fruit, root and grain infusions J6.4.2 to J6.4.5, G-J6-25 Herbal blends J6.4.0.01). Quality markers (display): coffee by green-bean defects, SCA cup score, Cup of Excellence result, traceability (farm or lot > region > country > blend), variety, then process and roast as choices; tea by type and processing, harvest season (first flush), dry leaf and liquor, named-area purity and storage, black tea by leaf grade, green tea by shading; cocoa by process (a choice), fat content and grind, bean class (provisional); infusions by plant and part (provisional).

Ids (R-58): J6.n is a sub-family and J6.n.m a leaf; a kind is J6.n.m.kk, or J6.n.kk where a sub-family has no leaf.

## J6.1 Coffee

No leaf (C5(b): under 12 kinds; leaf = null). Sub-family axis: the plant is Coffea. Kinds ordered by form as sold, by physical closeness to the roasted bean, machine-bound items last (memo section 8).
- J6.1.01 Roasted coffee: roasted coffee beans sold whole or ground (grind an attribute), including drip bags (a pack form).
- J6.1.02 Green (unroasted) coffee: raw, unroasted coffee beans sold to roast.
- J6.1.03 Instant coffee: soluble dried coffee extract, including a dry mix whose largest ingredient by weight is coffee (attribute `mix`, K-49).
- J6.1.04 Coffee capsule or pod (machine system): single-serve capsule, E.S.E. pod or paper pad of coffee made for one machine system (system in the C13 ledger).
- J6.1.05 Liquid coffee concentrate: liquid coffee extract sold to dilute, coffee its main ingredient; a sweetened or milk ready-to-drink is OUT (J6-O1).

## J6.2 Tea

Leaf axis: tea type by processing (ISO 20715), in order of oxidation: white, green, yellow, oolong, black, dark, then reprocessed. Inside a leaf with more than one kind, the kind axis is the process that defines the tea; region, cultivar, leaf grade and shop category are never the kind axis (J-15, review J6-6).

### J6.2.1 White tea
- J6.2.1.01 White tea: Camellia sinensis buds or young leaves withered and dried with little processing.

### J6.2.2 Green tea
Kind axis: the defining process (steaming, shading then steaming, pan-firing, roasting, grinding).
- J6.2.2.01 Steamed green tea: unoxidised tea fixed by steaming, rolled and dried (sencha, bancha).
- J6.2.2.02 Shade-grown steamed green tea: green tea from bushes shaded before harvest, then steamed (gyokuro). †
- J6.2.2.03 Pan-fired green tea: unoxidised tea fixed by heating in a pan or drum (Long Jing, Bi Luo Chun).
- J6.2.2.04 Roasted green tea: green tea roasted after fixing (hojicha). †
- J6.2.2.05 Powdered green tea (matcha): shade-grown, steamed, unrolled tea leaf stone-ground to a fine powder.

### J6.2.3 Yellow tea
- J6.2.3.01 Yellow tea: green-processed tea given a slow sealed yellowing step before drying.

### J6.2.4 Oolong tea
- J6.2.4.01 Oolong tea: partly oxidised tea, bruised and rolled between withering and fixing.

### J6.2.5 Black tea
- J6.2.5.01 Black tea (orthodox or CTC): fully oxidised tea, made orthodox or by CTC (leaf grade an attribute).

### J6.2.6 Dark tea
- J6.2.6.01 Pu-erh tea: post-fermented Yunnan large-leaf tea, raw (sheng) or ripe (shou), loose or pressed into cakes, tuo cha or bricks (attributes). Level provisional until attested (R-19).
- J6.2.6.02 Other dark tea: post-fermented tea other than pu-erh (Liu Bao, Liu'an).

### J6.2.7 Reprocessed tea
- J6.2.7.01 Scented, flavoured and blended tea: tea of any base type scented, flavoured or blended with other ingredients (Earl Grey, jasmine tea, blooming tea, genmaicha).
- J6.2.7.02 Spiced tea blend (chai): tea blended with spices to brew as chai.

Not yet kinds (no id until a fetched page attests them; J-14, J6-O1, K-49): tea capsule or pod for a machine system (joins J6.1.04 and moves it to a J6 multi-use sub-family); instant tea; liquid tea concentrate sold to dilute.

## J6.3 Cocoa

No leaf (C5(b); leaf = null). Sub-family axis: the plant is Theobroma cacao. Kinds ordered along the bean-to-product chain (memo section 8).
- J6.3.01 Cocoa beans: whole cacao beans, raw, fermented and dried, or roasted.
- J6.3.02 Cocoa nibs: cocoa beans cracked and shelled into pieces, raw or roasted.
- J6.3.03 Cocoa shells and husks: the shell of the cocoa bean, sold for infusion.
- J6.3.04 Cocoa paste or mass: ground cocoa nibs set in a block or drops (cocoa liquor, ceremonial cacao); couverture and baking chocolate are J5 (K-50).
- J6.3.05 Cocoa butter: the fat pressed from cocoa paste (K-50).
- J6.3.06 Cocoa powder: unsweetened powder of pressed cocoa solids, natural, Dutch-process or black (alkalisation and fat content attributes).
- J6.3.07 Drinking chocolate powder: sweetened cocoa powder for a drink, cocoa its largest ingredient by weight; a sugar-led mix is OUT (K-49).

## J6.4 Herbal & other infusions

Leaf axis: plant part infused (not Camellia sinensis). Kind: the herb or plant (J-15); kinds alphabetical by English name inside a leaf (memo section 8). A blend with one plant at half its weight or more is filed under that plant's kind (K-46).

### J6.4.1 Leaves and herbs
- J6.4.1.01 Lemon verbena: dried lemon verbena leaves sold for infusion. †
- J6.4.1.02 Peppermint: dried peppermint leaves sold for infusion. †
- J6.4.1.03 Rooibos: dried, usually oxidised leaves and stems of Aspalathus linearis sold for infusion. Level provisional until attested (R-19).
- J6.4.1.04 Yerba mate: dried, usually aged leaves and stems of Ilex paraguariensis sold for infusion (con palo, despalada, chimarrão, barbacuá). Level provisional until attested (R-19).

### J6.4.2 Flowers
- J6.4.2.01 Chamomile: dried chamomile flowers sold for infusion. †
- J6.4.2.02 Elderflower: dried elder flowers sold for infusion. †
- J6.4.2.03 Hibiscus: dried hibiscus calyces and petals sold for infusion.
- J6.4.2.04 Lavender: dried lavender flowers sold for infusion. †

### J6.4.3 Fruits
- J6.4.3.01 Fruit tea (dried-fruit blend): blend of dried fruit pieces sold for infusion.
- J6.4.3.02 Rose hip: dried rose hips sold for infusion. †

### J6.4.4 Roots, bark and spice
- J6.4.4.01 Ginger: dried ginger root sold for infusion (in a jar as a cooking spice it is J5).
- J6.4.4.02 Kava (root powder): ground root of Piper methysticum sold to prepare as a drink. Level provisional until attested (R-19). †
- J6.4.4.03 Roasted chicory root (coffee substitute): roasted chicory root sold to brew as a coffee substitute (K-51). †
- J6.4.4.04 Turmeric: dried turmeric root sold for infusion (in a jar as a cooking spice it is J5). †

### J6.4.5 Seeds and roasted grains
- J6.4.5.01 Roasted barley tea: roasted barley grains sold to brew (K-51). †

### Mixed (leaf 0)
- J6.4.0.01 Herbal blend: blend of infusion plants from more than one plant part, none of which makes up half or more of its weight (final kind, K-46).

## Precedence inside J6

- Sub-family by plant: a product of Coffea is J6.1, of Camellia sinensis J6.2, of Theobroma cacao J6.3, of any other plant brewed as an infusion J6.4. Roasted chicory root and roasted barley are J6.4 (J6.4.4.03, J6.4.5.01; K-51) even when sold as coffee substitutes, because J6.1's axis is the plant Coffea; rooibos and yerba mate are J6.4 (J6.4.1.03, J6.4.1.04), not tea.
- Coffee: whole bean and ground are one kind, Roasted coffee (J6.1.01), with grind as an attribute (J-15); a drip bag is the pack form of roasted coffee, not a kind (J-14). A single-serve pack made for a machine system (capsule, E.S.E. pod, paper pad) is J6.1.04, with the system in the C13 ledger; one that needs no machine is a pack form. Decaf, origin, roast, process and variety are attributes; coffee syrup is J5, and a tasting set follows the sets rule (item of greatest value).
- Dry mixes and concentrates (K-49, J6-O1): a dry drink mix is J6 when coffee, tea or cocoa is its largest ingredient by weight, otherwise a prepared drink (OUT); a coffee-led mix (a 3-in-1 stick) is Instant coffee (J6.1.03) with the attribute `mix`, a cocoa-led one Drinking chocolate powder (J6.3.07). A liquid coffee concentrate sold to dilute is J6.1.05; a sweetened or milk ready-to-drink is OUT.
- Tea leaf by processing (ISO 20715): a tea of one base type flavoured, scented or blended with other ingredients is Reprocessed tea (J6.2.7.01), not its base type: Earl Grey, jasmine tea, blooming tea and genmaicha are named forms of J6.2.7.01, and an aromatised white tea goes there too. A tea blended with spices for chai is J6.2.7.02.
- Green tea kinds go by the defining process: sencha and bancha are named forms of steamed green tea (J6.2.2.01), gyokuro of shade-grown steamed green tea (J6.2.2.02), Long Jing and Bi Luo Chun of pan-fired green tea (J6.2.2.03), hojicha of roasted green tea (J6.2.2.04); matcha is powdered green tea (J6.2.2.05) under Green tea, though some shops give it its own branch (J-15).
- Black tea is one kind (J6.2.5.01): leaf grade, orthodox or CTC, flush and tea-bag form are attributes; Darjeeling, Assam, Ceylon, Keemun, Lapsang Souchong, English Breakfast and Ostfriesen blend are named forms. Chinese "red tea" (hong cha) is black tea; Chinese "dark tea" (hei cha) is J6.2.6, not black tea; rooibos "red tea" is J6.4.1.03.
- Pu-erh (J6.2.6.01): raw or ripe, pressed shape, vintage year and factory recipe are attributes or variant fields; aged pu-erh kept as a collection is still J6.2.6.01 (rule S5). Other post-fermented teas are J6.2.6.02.
- Cocoa: cocoa beans, nibs, shells, paste, butter, powder and drinking-chocolate powder are J6.3 (J6.3.01 to J6.3.07) whether bought to brew, drink or bake; plain unsweetened cocoa powder stays J6.3.06 when bought for baking; couverture, baking chocolate and chocolate chips are J5 (K-50). Cocoa powder against fat-reduced cocoa powder is a fat attribute on J6.3.06, not two kinds (JC4).
- Infusions: the herb or plant is the kind; a blend with one plant at half its weight or more is filed under that plant's kind, otherwise it is Herbal blend (J6.4.0.01; K-46). A herb or root sold as an infusion, loose or in bags, is J6.4 even when marketed as a wellness blend; the same plant sold in a jar as a dried cooking herb or spice (mint, ginger, turmeric) is J5; one sold with a dose and a health claim, or as a tincture, capsule or extract, is H2. Kava is J6.4.4.02; kratom, khat, areca, betel and cannabis or CBD tea are B9 (K-168).
- Sets and mixes across J6 sub-families are filed by the item of greatest value; capsules, pods, tea bags and drip bags are J6 under their kind, while the machine that takes them is B5.
