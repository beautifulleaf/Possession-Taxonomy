# F2 Art: decided tree

Category: F2 Art (domain F, Culture, Records & Meaning). Membership test (key step 20): made to be looked at as a picture on a flat or hung surface (paintings, drawings, prints, posters, art photographs, calligraphy, tapestries and textile hangings, artist trading cards), or as free-standing sculpture, including ornamental figurines of people and animals made in ceramic, glass, metal, stone, wood or resin, whatever the edition or price. Not here: figures of characters, action figures, vinyl and collectible-series figures and bobbleheads (E1); garden statues and gnomes, picture frames and empty frames (B4); vases, bowls and other vessels, however artistic (B4 or B5); a decorative or commemorative plate (B5); maps, atlas sheets and pictorial wall maps (F1); a bound artist's book (F1); a printed series card collected as a card, an art medal and a trophy (F3); icons, thangkas and other devotional scroll paintings, altarpieces, devotional statues made for a shrine and crucifixes (F4); a photographic print not issued as an edition or signed or stamped by its maker as a work (F5); a mount of one animal prepared as in life and a stone only cut and polished (F6); a photograph, video work, digital artwork or NFT held as a file (I2); an object with a lamp holder and cord sold as a light, Akari models included (B3); blank canvas, paint, pastels, clay, easels and printmaking matrices (C4); calligraphy brushes and pens (C5); rugs made to be walked on (B2). Structure (Candidate A, decided F2-O1; memo sections 3, 4b, 10 and 12): sub-family (the discipline of the work), then leaf (only in Prints, by printing-process family; Photographs, by process class; Sculpture, by the material family that makes the form; the other sub-families store `leaf = null`), then kind (the medium, technique or material: where buyers compare), then named form. Each object gets one kind. Subject, style, movement, era, size, colour, support, use (illustration, comic art), edition, authenticity, price, region and tradition are attributes, registry scales, tags or views, never kinds; no value for one work is stored (C16). Attributes decided at the build (memo section 14, DPH): `authenticity_class` on named forms (original, interpretive, reproduction, restrike; R-2 classification) and `edition_class` on named forms (unique, limited edition, open edition), together the "Original or edition?" filter (display only); `era` on named forms (antique, contemporary; makers take era from their years); `issue_form` (poster, print edition, proof), so posters are filed by printing process and a poster view is generated; photographic prints carry `process` and `mount_format` (CV-38). Edition size, numbering, signature, proof status, chop mark, blind stamp and certificate are facts of one edition or work, shown as buying guidance and stored nowhere. Giclée (a marketing name of F2.3.6.01) and clay (an alias of the ceramic leaf F2.5.4) are C9 aliases. Maker role (maker_roles.tsv, provisional): way in; artists, print studios, print publishers and figurine manufactories in the one uncapped maker ledger (artists with a ULAN `authority_id`), the artist tab co-equal with the medium tree. Display groups (navigation proposal and section 14, display only; the tree keeps the memo's sub-families, leaves and ids): level 1 in shop order Paintings (F2.1); Prints (F2.3); Photographs (F2.4); Sculpture and figurines (F2.5); Drawings (F2.2); Textile and fibre art (F2.6); Calligraphy (F2.7); Collage, mosaic and mixed work (F2.8); level 2 = the leaves of Prints (relief, intaglio, planographic, stencil, other and hybrid, digital), Photographs (F2.4.1 to F2.4.5) and Sculpture (the material leaves F2.5.1 to F2.5.9); a generated "Figurines" display group over F2.5.1.03, F2.5.4.02, F2.5.4.03, F2.5.5.01 and F2.5.6.01, with a figurine manufactory side tab (Lladró, Goebel, Royal Doulton, all †). Side views: artist tab; by tradition (nihonga, ukiyo-e, ink wash, scrolls); by movement or style (scene tags); by subject; posters (`issue_form = poster`); illustration and comic art (`use` tag). Quality markers (display): all art by authenticity and originality (original > interpretive > reproduction > restrike), then condition (one work's facts, never stored), then artist reputation and auction record (maker level), then market value against comparables, then style and appeal; prints by edition size and edition class (unique > limited > open), then hand signature and numbering, then documentation (one edition's facts), then original hand technique over photomechanical, then paper and ink, then market demand, with proof status per CAA as guidance; paintings by original against reproduction, then era, then artist and attribution (forgery risk stressed for Japanese and Chinese painting); photographs by process and print date against image date, then edition class. Registry rows needed (not kinds): the `authenticity_class` and edition-class scales, the CAA proof classes as a classification scale for guidance only, and the Artsy Rarity, LUMAS and Artfinder platform labels; auction records feed C4(d) price bands only.

Ids (R-58): F2.n is a sub-family and F2.n.m a leaf; a kind is F2.n.m.kk, or F2.n.kk where a sub-family has no leaf. The ids of memo section 13 (from the frozen tree audit/KL_F2_tree.md) are kept exactly; kinds the memo holds as provisional until attested take the next free number under their parent and carry †.

## F2.1 Paintings
Leaf axis: none (`leaf = null`). Kind axis: binder or medium of the paint; support and ground (canvas, panel, paper, silk) are attributes.
- F2.1.01 oil painting: pigment bound in a drying oil, on canvas, panel or a similar support.
- F2.1.02 acrylic painting: pigment bound in acrylic polymer emulsion.
- F2.1.03 watercolour: transparent pigment in gum arabic, applied wet, normally on paper.
- F2.1.04 gouache: opaque, chalk-bodied water-based colour, normally on paper.
- F2.1.05 ink wash painting: black or coloured ink brushed in graded washes on paper or silk, in the East Asian manner.
- F2.1.06 mineral-pigment painting (nihonga): ground mineral pigments fixed with animal glue on paper or silk (kind status provisional under CV-27 until a seller outside Japan lists it apart).
- F2.1.07 tempera painting: pigment bound in egg yolk or another egg or glue medium, usually on a prepared panel.
- F2.1.08 encaustic painting: pigment in hot beeswax, fused to a support.
- F2.1.09 fresco (detached or transferred): pigment applied to wet or dry lime plaster, now removed from its wall.
- F2.1.10 mixed-media painting: a painting in which several paint media or added materials are used together and the image is painted, not built from pasted elements.
- F2.1.11 spray-paint painting: an image made mainly with aerosol or spray paint on canvas, panel or another support.
- F2.1.12 portrait miniature: a small painted portrait made as a work of its own, often on vellum, ivory, card or metal (provisional until a page sells it as its own category, F-13). †
- F2.1.13 animation cel: an image hand-painted in acrylic on a transparent acetate sheet, made for an animated film (provisional until a page sells it as such, F2-O2). †

## F2.2 Drawings
Leaf axis: none (`leaf = null`). Kind axis: drawing medium; use (illustration, comic art, animation) is a tag.
- F2.2.01 graphite (pencil) drawing: an image drawn with graphite pencils.
- F2.2.02 charcoal drawing: an image drawn with charcoal.
- F2.2.03 pastel drawing: an image drawn with pigment sticks (soft pastel, oil pastel) on paper or a similar ground.
- F2.2.04 coloured-pencil drawing: an image drawn with pigmented pencils.
- F2.2.05 pen-and-ink drawing: an image drawn with pen, nib or marker in ink.

## F2.3 Prints
Leaf axis: family of printing process, oldest first. Kind axis: the technique. Every print is filed by how it was printed; issue form (poster) and support are attributes.
### F2.3.1 Relief
- F2.3.1.01 woodcut: an image cut with knives and gouges into the side grain of a wood block and printed from the raised surface.
- F2.3.1.02 linocut: an image cut into a linoleum sheet and printed from the raised surface.
- F2.3.1.03 wood engraving: an image cut with gravers into the end grain of a hardwood block.
### F2.3.2 Intaglio
- F2.3.2.01 etching: lines bitten into a coated metal plate with acid.
- F2.3.2.02 line engraving: lines cut into a metal plate with a burin.
- F2.3.2.03 drypoint: lines scratched directly into a plate with a needle, without acid.
- F2.3.2.04 mezzotint: a plate roughened all over with a rocker, then burnished from dark to light.
- F2.3.2.05 aquatint: tone made by acid biting through a porous ground of resin dust.
### F2.3.3 Planographic
- F2.3.3.01 stone lithograph: an image drawn with a greasy medium on limestone and printed from the stone.
- F2.3.3.02 offset lithograph: an image transferred from a plate through a rubber blanket to paper.
### F2.3.4 Stencil
- F2.3.4.01 screenprint: ink pushed through a mesh stencil, one stencil per colour.
### F2.3.5 Other and hybrid processes
- F2.3.5.01 monotype: a single unique impression pulled from a painted or inked blank surface.
- F2.3.5.02 monoprint: a unique impression from a reusable matrix, varied by inking or additions each time.
- F2.3.5.03 collagraph: a print from a plate built up by gluing materials onto a board.
### F2.3.6 Digital
- F2.3.6.01 inkjet print: an image sprayed from a print head with pigment or dye inks onto paper, canvas or another sheet; the printer system is the attribute `printing_system`.

## F2.4 Photographs
Leaf axis: process class, by chronology of invention. Kind axis: the process. Every photographic print is filed by process and carries `process` and `mount_format`.
### F2.4.1 Silver
- F2.4.1.01 gelatin silver print: silver halide in a gelatin layer on paper, exposed and developed in a darkroom.
- F2.4.1.02 daguerreotype: an image on a silvered copper plate.
### F2.4.2 Chromogenic and dye
- F2.4.2.01 chromogenic print: colour dyes formed in the layers of colour paper by development.
- F2.4.2.02 dye-transfer print: colour made by transferring dyes from matrices onto paper.
- F2.4.2.03 silver dye bleach print: colour dyes already in the paper, bleached away where not wanted.
### F2.4.3 Pigment and digital
- F2.4.3.01 archival pigment print: a pigment inkjet print of a photograph on fine-art paper.
### F2.4.4 Alternative and historic
- F2.4.4.01 platinum or palladium print: an image in platinum or palladium metal on paper.
- F2.4.4.02 cyanotype: an iron-salt print giving a blue image.
- F2.4.4.03 tintype: a positive image on a thin iron plate.
### F2.4.5 Camera-less and instant
- F2.4.5.01 photogram: an image made without a camera by placing objects on light-sensitive material.
- F2.4.5.02 instant print: a self-developing print from an instant camera or film pack.

## F2.5 Sculpture
Leaf axis: material family that makes the form. Kind axis: the material or material-defined type. Figurines are kinds in these leaves; there is no figurine sub-family. Form (freestanding, wall-object, bust, relief, outdoor, installation, kinetic, netsuke) and size are attributes.
### F2.5.1 Metal
- F2.5.1.01 bronze sculpture: cast copper-tin alloy, usually patinated.
- F2.5.1.02 steel and iron sculpture: steel, iron or other ferrous metal welded, forged, cut or bent to form.
- F2.5.1.03 pewter and other cast-metal figurine: an ornamental figure cast in pewter, zinc, tin or another non-bronze metal. †
### F2.5.2 Stone
- F2.5.2.01 stone carving: marble, limestone, alabaster or other stone carved to form.
- F2.5.2.02 jade carving: a figure or object carved from jade.
### F2.5.3 Wood and other carved organic material
- F2.5.3.01 wood carving: a figure or sculpture carved from wood.
- F2.5.3.02 ivory and bone carving: a figure or sculpture carved from ivory, bone, horn or antler.
### F2.5.4 Ceramic
- F2.5.4.01 terracotta sculpture: modelled or moulded clay fired without a glaze.
- F2.5.4.02 glazed earthenware and stoneware sculpture and figurine: a figure or sculpture in glazed fired clay other than porcelain.
- F2.5.4.03 porcelain and bone china figurine and sculpture: a figure or sculpture in porcelain or bone china.
### F2.5.5 Glass and crystal
- F2.5.5.01 glass and crystal sculpture and figurine: a blown, cast, fused or cut glass or lead-crystal figure or sculpture.
### F2.5.6 Resin, plaster, wax and plastic
- F2.5.6.01 resin sculpture and figurine: a cast resin figure or sculpture, usually painted.
- F2.5.6.02 plaster sculpture: cast or modelled plaster.
- F2.5.6.03 wax sculpture: modelled or cast wax.
### F2.5.7 Textile and soft
- F2.5.7.01 soft sculpture: a three-dimensional sculpture of fabric, fibre or other soft material, stuffed, wrapped or stitched.
### F2.5.8 Found and mixed
- F2.5.8.01 found-object assemblage: a sculpture assembled from found, salvaged or discarded objects, or from several materials none of which governs.
### F2.5.9 Light
- F2.5.9.01 neon sculpture: a sculpture in which a lit gas-discharge tube or an equivalent light source is the medium.

## F2.6 Textile and fibre hangings
Leaf axis: none (`leaf = null`). Kind axis: the named object.
- F2.6.01 tapestry: a picture or pattern woven on a loom to hang on a wall.
- F2.6.02 embroidered picture: a picture worked in thread with a needle on a fabric ground.

## F2.7 Calligraphy
Leaf axis: none (`leaf = null`). Kind axis: the named object; script styles and traditions are named forms with region tags, hanging scroll and handscroll are `mount_format` attributes.
- F2.7.01 brush and pen calligraphy: writing made as the picture, in brush or pen script.
- F2.7.02 seal carving [篆刻]: script characters carved into a seal of stone or another material as a work of art, sold as the seal or its impressions (provisional until a fetched seller sells it apart from calligraphy). †

## F2.8 Collage, mosaic and mixed work
Leaf axis: none (`leaf = null`). Kind axis: the named object.
- F2.8.01 collage: a picture built from pasted or bonded elements (paper, cloth, photographs, found flat material).
- F2.8.02 mosaic picture: a picture set in small pieces (tesserae) of stone, glass or ceramic.

## F2.9 Parts and accessories made for one artwork
Provisional (CV-17): the closing sub-family opens only when an S3 part is attested. Leaf axis: object served (no leaf yet). Frames are B4.
- F2.9.01 sculpture plinth or stand: a base, plinth or stand made for one sculpture (provisional until a page attests it). †

## Precedence inside F2
1. Pastel is a drawing (F2.2.03), not a painting.
2. Gouache is its own kind (F2.1.04), beside watercolour (F2.1.03).
3. A work whose image is built from pasted elements is a collage (F2.8.01); a painting with added materials is mixed media (F2.1.10).
4. A print is filed by its printing process. A poster has no kind of its own and carries `issue_form = poster`: a stone-lithograph poster is F2.3.3.01, a screenprinted poster F2.3.4.01. An inkjet reproduction of a painting is an inkjet print (F2.3.6.01), linked to the `authenticity_class` scale. A printed image on metal or canvas is filed by its process, with the support as an attribute.
5. Monotype (F2.3.5.01) and monoprint (F2.3.5.02) are prints; uniqueness is a fact of the kind, not a leaf. Chine-collé is an attribute, not a kind.
6. A photographic print is filed by its process. A camera-less image is a photogram (F2.4.5.01); a self-developing print from an instant camera is an instant print (F2.4.5.02). A platinum or palladium print is Alternative and historic (F2.4.4.01), not Silver.
7. Within one material a figurine and a sculpture are one kind; size, edition, price and maker are attributes or ledger facts and never choose the kind. An ornamental figurine is filed in the material leaf of its material (F2.5.1.03, F2.5.4.02, F2.5.4.03, F2.5.5.01, F2.5.6.01 and the other material kinds).
8. Form (freestanding, wall-object, bust, relief, outdoor) is an attribute. A cut or forged metal relief hung on a wall is filed under Metal (F2.5.1) with `form = wall-object`.
9. A netsuke is filed under the kind of the material it is carved from (a wood netsuke is F2.5.3.01, an ivory one F2.5.3.02), with `form = netsuke` on materials other than wood.
10. A work that combines animal parts with other materials, or several materials with none governing, is a found-object assemblage (F2.5.8.01).
11. An installation or kinetic work that is a free-standing object is filed under the sculpture leaf of its main material (Found and mixed F2.5.8 for several materials, Light F2.5.9 for light as the medium), with `form` = installation or kinetic. A light sculpture issued as a numbered or signed artwork edition is F2 (F2.5.9.01 or the main-material leaf).
12. A cast, replica or carved figure made as a sculpture, such as a replica of a fossil or skull, is filed by its material in F2.5; a carved block or plate sold to be looked at as a relief is F2, by its material.
13. Use (illustration, comic art, animation) is a tag, not a kind: an original comic page in pen and ink is F2.2.05, a gouache book illustration F2.1.04. An animation cel is F2.1.13 once attested.
14. Woven to hang is tapestry (F2.6.01); worked with a needle is an embroidered picture (F2.6.02). A ketubah or baptism certificate made as a picture is F2, filed by its medium.
15. Tradition is a tag and a view, never a level: Japanese and Western painting are not split; mineral-pigment painting keeps F2.1.06 only while its CV-27 tie-break holds, and otherwise becomes a named form under the nearest painting kind.
16. A hand-made card sold as an original artwork is F2, filed by its medium.
