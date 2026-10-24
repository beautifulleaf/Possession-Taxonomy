# B2 Soft Furnishings: decided tree

Category: B2 Soft Furnishings (domain B, Home). Membership test (placement key step 30, CATEGORIES_v0_7_3): made to cover, soften or dress beds, floors, windows, seats and tables, or to wrap or dry the body: bedding, mattress toppers, rugs and carpets (loose or fitted), chair and floor mats, blinds and curtains, cushions, throws, electric blankets, table linen, towels, swaddling cloths, travel pillows; curtain poles, rails and rings, and rug underlay, are B2 (K-189). Not here: mattresses, shiki-futon floor mattresses, futon sofas, bean bags, kotatsu tables, zaisu, poufs, ottomans and cots (B1); tapestries and textile hangings made to hang (F2, step 20); prayer rugs made as such (F4, K-113); sleeping bags and sleeping mats (E2); wearable baby sleeping bags and bathrobes (A1); beds, blankets and cushions made for an animal (B10); hard placemats, coasters, trivets, oven gloves and aprons (B5); flooring other than carpet and carpet tiles, plantation shutters and other fixed window joinery (C8); artificial turf (C2); mosquito nets (B8); towel radiators and heated towel rails (B7), heated airers (B6); car seat covers (G1, by S3); yardage fabric sold for sewing (C4, cross-link only); weighted blankets and orthopaedic pillows sold to treat a stated condition (H2, K-40). Structure (Candidate A, decided B-3, B-15, B-16, B2-O1, B2-O2; memo sections 3 and 10): sub-family by what the textile dresses, covers, screens or wraps (bed or heated table; floor; window, door or shower opening; seat; table and kitchen; body), closed by the sub-family "Parts and accessories made for one object", exempt from that axis (CV-17, C5(d)); leaf by product type sold as a shopping category in B2.1, B2.2 and B2.3; B2.4 to B2.7 hold 12 kinds or fewer and have no leaf (`leaf = null`); kind by the axis stated per leaf or leafless sub-family. Each object gets one kind. Size and size class, fitted or flat, fill, fill power, tog, warmth season, thread count (with the ASTM D3775 counting rule and a ply flag), weave, fibre and staple class, GSM, knot density, `process` (hand-knotted, hand-tufted, machine), `installation` (loose or fitted), EN 1307 use class, `weaving_environment` (on rug named forms: city or workshop, village, nomadic or tribal; a classification, never a ladder or a level), heading, lining, opacity, motorisation, weight, orthopaedic shaping, `fits` (the sofa or chair model a cover is made for), unit of sale (sets, K-1), setting, room, user (baby, child), region and culture are attributes or tags, never kinds; city, village and tribal rug names are provenance tags; travelling design names (Kilim, Soumak, Dhurrie, Aubusson, Gabbeh, Beni Ourain, Oushak, Bokhara, Savonnerie, Wilton, Axminster, kake-futon †) are non-maker named forms. Attributes to store (memo section 14): warmth_season, tog, fill_power, thread_count (with counting rule), knot_density, process, weaving_environment, opacity, en1307_use_class. A kind marked † is attested at the stage 3 harvest: its id is fixed here, and it enters the data only when one fetched page shows it made or sold (memo section 10, attestation list; for the chair pad, a page showing chair pads sold as a group). Maker role: owner (maker_roles.tsv, provisional): textile makers matter through named designs and lines; mass bedding, towels and curtains are bought by item and spec, and hand-woven rug workshops are recorded but are not the way in. Display groups (navigation proposal, display only, no id or leaf changes): Bed linen & bedding (B2.1.1, B2.1.2 less B2.1.2.06 and B2.1.2.07, B2.1.3, B2.1.4); Blankets & throws (B2.1.2.06, B2.1.2.07; memo section 14: B2.1.2 shows two groups, "Duvets and bed covers" and "Blankets and throws"); Rugs & mats (B2.2.1, level 2 by construction: handmade rugs, machine-made rugs and carpet, hide, felt and rag rugs; B2.2.2 less B2.2.2.02); Curtains & blinds (B2.3.1 less B2.3.1.03, B2.3.2); Cushions & seat covers (B2.4); Table & kitchen linen (B2.5); Towels & bath (B2.6 with B2.2.2.02 and B2.3.1.03); Curtain & rug fittings (B2.7). Season is a filter on bedding, not a level. Quality markers (display): bed linen by fibre and staple, weave and finish, ply, weight, then thread count last, colourfastness; duvets and pillows by fill and down fill power, tog for warmth by season (not a quality rank), casing fibre; handmade rugs by material, knot density, weaving tradition and environment, natural dyes, age and rarity; machine rugs and fitted carpet by EN 1307 use class; curtains, upholstery and cushion covers by abrasion (Martindale), pilling grade, lining and opacity; towels by fibre and staple, then GSM (bands held until a fetched page shows them). Side view: handmade rugs by weave and tradition (weaving environment, named weave, workshop where known), never a division by country.

Ids (R-58): B2.n is a sub-family and B2.n.m a leaf; a kind is B2.n.m.kk, or B2.n.kk where a sub-family has no leaf. B2 has no memo section 13 and no frozen audit tree; the sub-family and leaf codes are the memo's own (B2.<sub-family>.<leaf>, review C-9), and kind numbers are assigned here in the memo's order. The chair pad (memo section 14) takes the next free number in B2.4 (B2.4.07) and is listed after the scatter cushion, where the kind axis places it; the id is not a sort key.

## B2.1 Bed textiles (bed, or heated table)

Leaf axis: product type sold as a shopping category (bed linen, duvets and bed covers, pillows, mattress covers).

### B2.1.1 Bed linen
Kind axis: piece of the made bed.
- B2.1.1.01 Sheet: a flat or fitted sheet of woven or knitted fabric laid over the mattress or under the top cover; fitted or flat is an attribute.
- B2.1.1.02 Pillowcase: a removable fabric case that covers a bed pillow.
- B2.1.1.03 Duvet cover: a removable fabric bag, closed by buttons, ties or a zip, that encloses a duvet or comforter.
- B2.1.1.04 Valance or dust ruffle: a fabric skirt fitted between mattress and bed base that hides the base and legs.

### B2.1.2 Duvets and bed covers
Kind axis: construction, then warmth.
- B2.1.2.01 Duvet (insert): a filled top cover with loose fill in stitched channels or boxes, made to be used inside a removable duvet cover; fill, fill power and tog are attributes.
- B2.1.2.02 Comforter: a thick filled top cover sewn closed with the fill built in, used without a separate cover.
- B2.1.2.03 Quilt: a thinner top cover of two fabric layers with a light batting, held together by visible quilted stitching.
- B2.1.2.04 Bedspread or coverlet: a single-layer or lightly lined decorative cover laid over the made bed.
- B2.1.2.05 Featherbed: a thick feather- or down-filled pad laid on top of the mattress to sleep on. †
- B2.1.2.06 Blanket or throw: a woven, knitted or fleece cover without fill, for a bed or a sofa; size, weight (weighted blankets, unless sold to treat a stated condition) and setting are attributes.
- B2.1.2.07 Electric blanket (heated throw): a blanket or throw with built-in electric heating wires and a controller, laid on or under the sleeper or used on a sofa.
- B2.1.2.08 Kotatsu cover [kotatsu futon]: a quilted cover made to drape over a heated low table (kotatsu) and hold its warmth in. †

### B2.1.3 Pillows
Kind axis: use.
- B2.1.3.01 Bed pillow: a stuffed pillow made to support the head in bed; fill, firmness and orthopaedic shaping are attributes.
- B2.1.3.02 Travel pillow: a pillow, often U-shaped or inflatable, made to support the head and neck while sitting in transit.
- B2.1.3.03 Positioning cushion: a shaped foam or inflatable cushion made to hold the body in a chosen position (wedges and ramps); fill is an attribute. †

### B2.1.4 Mattress covers
Kind axis: layer.
- B2.1.4.01 Mattress protector: a thin, often waterproof cover fitted over or around the mattress to guard it against spills and wear.
- B2.1.4.02 Mattress pad: a thin quilted or padded layer fitted over the mattress for light extra comfort.
- B2.1.4.03 Mattress topper: a thicker removable layer of foam, latex, fibre or down laid on the mattress to change its feel.

## B2.2 Floor textiles

Leaf axis: product type sold as a shopping category (rugs and carpets, mats).

### B2.2.1 Rugs and carpets
Kind axis: construction, in HS 5701-5705 order; hand or machine is the attribute `process`, loose or fitted is `installation`.
- B2.2.1.01 Knotted-pile rug: a rug or carpet whose pile is formed by knots tied around the warps, by hand or machine.
- B2.2.1.02 Flatweave rug: a rug woven without pile, the pattern made by the weft (kilim, soumak, dhurrie constructions).
- B2.2.1.03 Woven pile rug or carpet: a rug or carpet whose pile is woven in with the backing on a loom (Wilton, Axminster constructions).
- B2.2.1.04 Tufted rug or carpet: a rug or carpet whose pile yarn is punched through a pre-made backing and fixed with adhesive, by hand gun or machine.
- B2.2.1.05 Hooked rug: a rug made by pulling loops of yarn or fabric strips through a woven backing with a hook.
- B2.2.1.06 Felt rug or carpet: a rug or carpet of matted fibre, made by felting rather than weaving.
- B2.2.1.07 Needlepunched carpet: a carpet or carpet tile whose fibres are interlocked by barbed needles into a dense non-woven sheet. †
- B2.2.1.08 Hide rug: a rug that is a tanned animal hide with its hair, or a patchwork of hides (cowhide, sheepskin).
- B2.2.1.09 Rag rug: a rug braided, woven or hooked from strips of reused cloth. †

### B2.2.2 Mats
Kind axis: job.
- B2.2.2.01 Door mat: a hard-wearing mat laid at a door to wipe shoes and catch dirt.
- B2.2.2.02 Bath mat: an absorbent mat laid beside a bath or shower to stand on with wet feet.
- B2.2.2.03 Kitchen mat: a mat or runner laid in front of a kitchen counter or sink to stand on while working. †
- B2.2.2.04 Chair mat: a mat laid under a desk chair to protect the floor and let castors roll.
- B2.2.2.05 Meditation mat: a flat padded mat laid on the floor under a meditation cushion or to sit on for meditation. †

## B2.3 Window and screening textiles (window, door or shower opening)

Leaf axis: product type sold as a shopping category (curtains, blinds and shades).

### B2.3.1 Curtains
Kind axis: fabric class and place hung; heading and lining are attributes.
- B2.3.1.01 Curtain: a panel of fabric hung from a pole or track to cover a window or door, lined or unlined.
- B2.3.1.02 Sheer, voile or net curtain: a curtain of light translucent fabric that filters light and gives daytime privacy.
- B2.3.1.03 Shower curtain: a water-resistant curtain hung from a rail to close a shower or bath opening.
- B2.3.1.04 Studio backdrop: a large cloth or paper-like textile sheet hung or stretched behind a subject in a photo or video studio. †

### B2.3.2 Blinds and shades
Kind axis: mechanism; fabric opacity, slat material and motorisation are attributes.
- B2.3.2.01 Roller blind: a single panel of fabric that rolls up onto a tube at the head of the window.
- B2.3.2.02 Roman blind: a fabric blind that folds up into horizontal pleats as it is raised by cords.
- B2.3.2.03 Venetian blind: a blind of horizontal slats that tilt and lift on cords or tapes.
- B2.3.2.04 Vertical blind: a blind of vertical vanes hung from a track that rotate and draw to one side.
- B2.3.2.05 Pleated blind: a blind of crisply pleated fabric that concertinas up or down.
- B2.3.2.06 Cellular shade: a pleated blind of two or more fabric layers forming insulating cells (honeycomb).
- B2.3.2.07 Panel blind: wide flat fabric panels that slide side to side on a multi-channel track.

## B2.4 Seat textiles

No leaf (`leaf = null`). Kind axis: form, stuffed piece before cover.
- B2.4.01 Scatter cushion: a loose stuffed decorative cushion for a sofa, chair or bed.
- B2.4.07 Chair pad (seat pad): a thin cushion, usually with ties or a non-slip back, made to lie on the seat of a chair. †
- B2.4.02 Floor cushion [zabuton]: a large flat cushion with no frame, made to sit on at floor level. †
- B2.4.03 Meditation cushion: a firm cushion with no frame, round or crescent, made to sit on for meditation (zafu). †
- B2.4.04 Cushion cover: a removable fabric case for a cushion, sold without or with the insert.
- B2.4.05 Sofa cover: a removable fabric cover (slipcover, throw-over or stretch cover) for a sofa, also when made to fit one model (the model in `fits`).
- B2.4.06 Chair cover: a removable fabric cover for a chair, dining and event chairs included, also when made to fit one model. †

## B2.5 Table and kitchen linen

No leaf (`leaf = null`). Kind axis: piece.
- B2.5.01 Tablecloth: a cloth laid over a table top to protect and dress it.
- B2.5.02 Table runner: a long narrow cloth laid along the centre of a table. †
- B2.5.03 Placemat (textile): a fabric mat laid under one place setting; hard placemats are B5. †
- B2.5.04 Cloth napkin: a square of fabric for wiping hands and mouth at table. †
- B2.5.05 Kitchen towel or tea towel: a cloth for drying dishes and hands in the kitchen.

## B2.6 Body textiles

No leaf (`leaf = null`). Kind axis: role and size, largest first; the carry cloth, which wraps goods, comes last.
- B2.6.01 Bath sheet: the largest bath towel, big enough to wrap the whole body.
- B2.6.02 Bath towel: a large absorbent towel for drying the body after bathing.
- B2.6.03 Hand towel: a mid-size towel for drying hands and face.
- B2.6.04 Washcloth: a small square towel (face cloth, flannel) for washing the face and body.
- B2.6.05 Beach towel: a large towel made to lie on at the beach or pool and dry off.
- B2.6.06 Flat-woven towel [peshtemal, hammam towel]: a thin flat-woven towel without terry loops, light and quick-drying.
- B2.6.07 Swaddling cloth: a square of soft fabric made to wrap a baby snugly.
- B2.6.08 Carry cloth [furoshiki]: a square cloth made to wrap and carry goods or gifts by knotting its corners. †

## B2.7 Parts and accessories made for one object

No leaf (`leaf = null`; leaves by object served, curtains and blinds, rugs, are held until the sub-family passes about 12 kinds). Kind axis: object served, then fitting type; exempt from the sub-family axis (C5(d)).
- B2.7.01 Curtain pole: a rod fixed above a window or door from which curtains hang on rings or by their heading.
- B2.7.02 Curtain track or rail: a fixed track with runners or gliders along which curtains are drawn.
- B2.7.03 Curtain rings and hooks: rings, hooks, gliders and clips that attach a curtain heading to its pole or track.
- B2.7.04 Rug pad or underlay: a pad laid under a rug or carpet to stop slipping, cushion it and protect the floor.

## Precedence inside B2

- Throw and blanket: an object that dresses a bed or a sofa is tested on the object (S5): one kind, B2.1.2.06 Blanket or throw, with setting (sofa), size and weight as attributes (B-16). A weighted blanket is B2.1.2.06 and an orthopaedic pillow B2.1.3.01, unless sold to treat a stated condition (then H2, K-40). A heated throw is B2.1.2.07.
- Cushion against pillow: a stuffed rectangle is filed by its use: B2.1.3.01 Bed pillow on the bed, B2.4.01 Scatter cushion on a seat. A positioning cushion, inflatable ones included, is B2.1.3.03 (K-82, H-14); furniture made to restrain or suspend is H3.
- Futon: the floor mattress (shiki-futon), the US futon sofa and a bean bag are B1; the quilt laid over a shiki-futon (kake-futon) is a named form of B2.1.2.02 Comforter †; the quilt that covers a kotatsu is B2.1.2.08 †, and the heated table itself is B1. A mattress topper, protector and pad are B2.1.4.03, B2.1.4.01 and B2.1.4.02.
- Rugs against hangings: an object made to be walked on, whether knotted, flatwoven or tufted, is a B2.2.1 rug even if later hung; an object made to be looked at (tapestry, textile hanging, Aubusson panel) is F2 under step 20; a rug made as a prayer rug is F4 (K-113). The made-for test decides, not the listing.
- Rug construction is the kind (B2.2.1.01 to B2.2.1.09); hand or machine is `process`; city, village and tribal names are provenance tags; a hide made into a rug is B2.2.1.08 (B-15), while the raw hide as material is C4.
- Fitted against loose: carpets and carpet tiles, loose or fitted, are B2.2.1 (fitted is the attribute `installation`); other flooring and tiles are C8; artificial turf is C2.
- Bath mat and shower curtain are made as a floor mat and a curtain: B2.2.2.02 and B2.3.1.03, with bathroom as a generated setting view; the display group Towels & bath shows them.
- Curtain fittings and rug underlay: poles, tracks or rails, rings and hooks and rug pads are B2.7.01 to B2.7.04 (K-189, S3), not C8; blind motors and pole or track systems are recorded in the compatibility ledger; fixed window joinery such as plantation shutters is C8; mosquito nets are B8.
- Table linen: tablecloths, runners, textile placemats and cloth napkins are B2.5.01 to B2.5.04 (B5-O1); hard placemats, coasters, trivets and boards, oven gloves and aprons are B5. Tea towels are B2.5.05, because towels of every kind are B2.
- Animals and babies: a bed, blanket or cushion made for an animal is B10; baby and children's bedding is B2 with user as a modifier; a cot is B1; a swaddling cloth is B2.6.07; wearable baby sleeping bags and bathrobes are A1; a hooded or ordinary towel is B2.6.
- Covers: cushion covers, sofa covers and chair covers are B2.4.04, B2.4.05 and B2.4.06, also when made to fit one sofa or chair model (the model in `fits`); a textile cover for furniture is never an S3 part (B2-O1). A cover made for a car seat follows S3 to G1.
- Floor seating: a cushion with no frame made to sit on at floor level is B2.4.02 (zabuton) or B2.4.03 (meditation cushion) †; a meditation mat is B2.2.2.05 †; a seat with a frame or rigid body (zaisu, stool, pouf, ottoman) and a bean bag are B1. A chair pad lying on a chair seat is B2.4.07 †.
- Heated objects: electric blankets and heated throws are B2.1.2.07; a towel radiator or heated towel rail is B7, a heated airer B6.
- Sleeping outdoors: sleeping bags and sleeping mats are E2; a down duvet is B2.1.2.01 even though fill power is the same measure.
- Sets: bedding sets, towel sets and kake-shiki futon sets are a unit-of-sale attribute; each piece is filed as its own kind and there are no suite kinds (K-1).
- Studio backdrops are B2.3.1.04 † (K-17); studio furniture is B1, and studio lights, stands and flashes are D4.
- Furoshiki and other carry cloths are B2.6.08 † (K-134), with a cross-reference from A4.
- Yardage fabric sold for sewing is C4 (craft), cross-linked only.
