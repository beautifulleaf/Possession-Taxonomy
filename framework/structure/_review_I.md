# Stage 2 domain review: I Software, Digital & Subscriptions (I1 to I3)

*Batch S2R_I. Cold, offline review (no web, no git) of memos framework/structure/I1.md, I2.md and I3.md and their sources files verify/out/S2_I1_sources.tsv, S2_I2_sources.tsv and S2_I3_sources.tsv, against BRIEF.md, framework/CATEGORIES_v0_6.md, framework/STAGE2_MEMO_TEMPLATE.md and the draft shared conventions C1 to C13 in framework/structure/_conventions.md. The three memos say they were prepared under C1 to C13, so section 3 checks each convention and lists the changes still needed. This is a reviewer's judgement, not an owner decision. Severity: **high** = breaks a shared rule (BRIEF, Appendix A, a convention), or would file many objects in two places; **medium** = one rule break, one contradiction or a clear split; **low** = wording, evidence or tidy-up.*

*Resume status: sections 1 and 2 are written. If a section below reads PENDING, continue from there.*

**Mechanical checks.**
- *Sources match.* I1 cites S01 to S31, and the TSV has 31 rows in the same order. The header says "37 fetched pages (… 31 rows)"; the six other pages are the failed fetches it lists. I2 cites S01 to S32, and the TSV has 32 rows. The header says 33 fetched pages, the extra one being the blocked Steam Community Market. I3 cites S01 to S38, and the TSV has 38 rows. Its header says 40 fetches, two of which carry no claims. Every key table matches its TSV row for row.
- *Depth and genre.* All three memos recommend at most four levels below the category (sub-family, leaf, kind, named form). No memo divides by content genre or subject. I1 drops Vector's subject split of education software, I2 bars genre from every level, and I3 drops sport, anime and audience.
- *Excerpt labelling.* I2 says the Kindle, Kobo and BookWalker store trees were seen only in search excerpts and does not cite them. I3 marks such kinds "search only" or "key". I1 has no search-only claims, but two of its rows are partial: S04's category list "collapsed on the fetched page", so the "32 categories" rests on a secondary blog (S30), and one Ninite heading is "elided".

## 1. Verdict table

| Code | Verdict | Top three issues |
|---|---|---|
| I1 Software | minor fixes | (1) It has two exempt sub-families, against C5(d), and one of them (SF13 device unlocks) has no source. The "Money and business" leaf is split by market (personal or business), a modifier the memo itself rejects in Candidate C. (2) Tiers and versions are handled inconsistently. Maker edition ladders are declared "not tiers", which conflicts with I3 and the domain E convention. Tier entries are put on versions, which C4(a) does not allow. Windows 11 Home and Pro are named forms in the tree but variants in the usability check. (3) Boundaries with I2 and I3 are left open: meditation and language apps against I3 classes, backup software against online backup, GIS against maps, plug-ins and sample libraries. Two products have no kind: the Creative Cloud all-apps bundle and audio plug-ins. |
| I2 Digital Media & Items | needs rework | (1) Some kinds are named after a platform, a maker or a region ("Kindle-format e-book", "Apple Books e-book", "Chinese reader-format e-book"). In audiobooks and video, rights state is used as the kind axis ("account-locked audiobook", "digital film licence" against "video file"), although the memo's own question 7 makes it an attribute. (2) Fonts get seven kinds by licence scope ("company desktop" among them, which is a market modifier), so one typeface family is a named form under up to seven kinds. The evidence is one US retailer. Music kinds follow codec family, not the Qobuz quality classes the memo cites, so a 24/192 FLAC splits. (3) The sub-family axis ("medium") changes meaning across sub-families, so texture packs, PSD templates and avatar models split between still images, design assets and game items. Sample packs, presets, LUTs, AI model files and messaging stickers have no kind. |
| I3 Subscriptions, Memberships & Online Services | minor fixes | (1) Maker plan ladders are tier entries on plan rows, which needs a C4(a) amendment. The price-band rule (annualised plan price) differs from I1's (first-year, one seat). The plan ledger is a third shape of the C3 variant ledger. (2) Some kinds break the memo's own axes. Newspapers and magazines are split by print or digital, which leaves a print newspaper subscription with no kind. "Meal-kit plan" is named by its goods, so member-chosen coffee or book plans have no home. Gym and sports club are two kinds that rest on one COICOP class, and that class lumps them together. (3) 17 of the 43 kinds rest only on the key text, a classification line or a single mention. Nothing covers the asset and font library plans that I2 sends to I3. The I1 boundaries for classes, backup, maps and device-tied plans are not closed. |

## 2. Findings by memo

Each finding gives severity, memo, evidence and an exact proposed fix. Cross-memo findings (X1 to X9) are in section 4. They are cited here where a fix depends on them.

### I1 Software

**I1-1 (medium) Two exempt sub-families, one of them unsourced.**
- *Evidence.* Section 3 creates "Two exempt sub-families (C5d)": SF12 "Add-ons made for one program" and SF13 "Unlocks for software built into a device". C5(d) allows one exempt sub-family, the parts sub-family. SF13 has "no fetched source", and object 20 (a paid driver-assistance unlock) "stays unplaced in the data". The device-unlock line also meets I3: a car's connected-services plan or a smartwatch eSIM line is a connection plan, not an unlock.
- *Fix.* Merge SF12 and SF13 into one exempt sub-family, "Add-ons and unlocks made for one program or device". Its leaf axis is the host. Leaves:
  - browser;
  - code editor or IDE;
  - office or productivity suite;
  - audio or graphics host (VST/AU and Photoshop plug-ins; see I1-5);
  - software built into a device (paid feature unlocks).
- The last leaf stays empty until a fetched source attests a kind (S6). Add the device-tied sentence X7(g) to section 9.

**I1-2 (medium) The "Money and business" leaf is split by market.**
- *Evidence.* The leaf axis is "whose money or work (personal; business operations)". Appendix A lists "market (domestic, commercial, professional)" as a modifier. Section 3, Candidate C, rejects market as an axis for exactly this reason ("A freelancer's invoicing tool is business software owned by a person"). The split also fails on real objects. Accounting software (QuickBooks for sole traders) and invoicing apps are used by a person and by a firm alike.
- *Fix.* Under the personal and prosumer scope, the sub-family has 5 kinds, so store `leaf = null` (C5(b)). Add a `market` tag (consumer, business) and a generated "business software" view. If the owner opens business software to Capterra depth (question 2), use the leaf axis "business function" with Capterra's department groups (finance and accounting, sales and customers, people and payroll, operations and stock). These are functions, not markets.

**I1-3 (medium) Editions, versions and maker ladders are handled three ways.**
- *Evidence.*
  - Tree row 1 lists "Windows 11 Home, Windows 11 Pro" as named forms. Usability object 1 says "edition Pro is a variant". Row 1 also lists "Windows 95" as a named form, while question 6 leaves releases open.
  - Section 5 says maker edition ladders (Home below Pro, Personal below Family below Premium) "are `edition` variants, not tiers". I3 section 5 makes the same kind of ladder a tier entry on the plan row. The domain E review (decision 6) adopted "maker ladders as tier entries".
  - Section 5 puts lab results "on the named form or its variant (a product version such as Kaspersky Premium 21.24)". C4(a) lists only maker, line and named form as subjects.
- *Fix.*
  - **Releases.** The product line goes in the C1 lines table (Windows; Microsoft Office; Norton 360). A release sold under its own name is the named form (Windows 95, Windows 11, Office Home 2024, Microsoft 365). Editions, plans and minor versions are C3 variants (variant types `edition`, `plan`, `version`; X2).
  - **Ladders.** The maker's ladder becomes a tier entry with scheme `maker ladder: <named form>` on the variant rows, under the C4(a) amendment in X3.
  - **Lab results.** These are tier entries on the named form. The tested version goes in the entry, or the entry sits on the `version` variant under X3.
  - Rewrite section 5's last bullet and tree row 1 to match.

**I1-4 (low) A lab seal is a certification; Arena ranks models.**
- *Evidence.* AV-TEST's "Certified" seal (10 points or more, S20) is a pass mark against a published test. That is the same pattern as COSC, which C4(b) treats as an attribute. C1's A5 extension already has `certifications`. Arena (S22) ranks models from votes that change continuously, not the subscriptions people hold. Section 5 says so itself.
- *Fix.* Record AV-TEST Certified and AV-Comparatives Approved as a dated `certification` attribute on the version. Record the scored outcomes (AV-TEST points and TOP PRODUCT, AV-Comparatives Advanced+ and Top-Rated) as tier entries under two schemes, with the computed `disputed` flag. Store Arena entries only when owner question 1 rules that the model and the product are the same thing, and then only as dated snapshots.

**I1-5 (medium) Orphan, combined and missing kinds.**
- *Evidence.*
  - Edge object 1 says a hosted design tool "needs its own kind ('graphic design app')", but the tree does not add it.
  - Usability object 14 invents "database software" and files it under "Network and server tools". That leaf is about network clients, not data.
  - Row 11, "application launcher and file-search tool", joins three different products: Launchy (launcher), Everything (desktop search) and PowerToys (a utility bundle). Row 29 joins screen recording and live streaming.
  - The tree has no kind for **audio plug-ins** (VST/AU instruments and effects). These are a large compared class, with makers such as Native Instruments, Waves and Arturia. Placement step 5 sends them to I1, before E3.
  - Adobe **Creative Cloud Pro** (all apps, S27) is named for no single component. The bundle rule ("filed by the component it is named and sold for") therefore gives it no home.
  - The sub-family is called "Learning and reference" in the tree and "learning and home" in sections 3 and 4b.
- *Fix.*
  - Add "graphic design app" to Images and design (S02 Graphic Design Software).
  - Add a leaf "Data and servers" to Development, holding database software, SSH and file-transfer client, and network protocol analyser. Rename "Network and server tools" to match.
  - Split row 11 into "application launcher" and "desktop search tool". PowerToys becomes a named form of "system utility suite", or of "system cleaner and optimiser" if no source separates the two.
  - Add "audio plug-in (instrument or effect)" to the add-ons sub-family of I1-1. Its source is still to be fetched.
  - Add the kind "creative suite" to Creative production, with this sentence: *"An all-apps bundle of one maker's creative programs (Creative Cloud Pro, Affinity) is the kind 'creative suite'; a single-app plan is filed under that app's kind."*
  - Use one sub-family name throughout.

**I1-6 (medium) Choice-level evidence rests on an installer picker and on US review sites.**
- *Evidence.*
  - Section 4b decides the creative kinds from "Ninite lists Paint.NET (raster) and Inkscape (vector) separately" (S05). Ninite is a bulk installer of free programs (source type "enthusiast install catalogue"), not a comparison page.
  - All comparison evidence is US (PCMag, S15 and S16) or comes from the two test labs (DE, AT). No Japanese, Chinese or German comparison page was fetched for office, creative or media software. The Japanese, Chinese and German sources (S07 to S10) are download libraries.
  - UNSPSC (S12, S14) was read from a third-party mirror (usa.databasesets.com), not from the UNSPSC publisher.
  - The key table gives Capterra "eleven headline groups", while the TSV row says "10 headline groups" and then names 11.
- *Fix.* Before the owner approves, fetch one comparison or "best X" page for raster against vector editors, office suites and media players, from a non-US region (for example a Japanese price-comparison software ranking or a German test magazine). Mark the UNSPSC rows "mirror". Correct the Capterra count to the number the page shows.

**I1-7 (medium) Boundaries with I2 and I3 are open or answered differently.** See X7 (a) to (e), (g), (h) and (i).
- *Evidence.* Sentence 6 says "wellness and meditation apps are I1 by function", but key branch (a) puts "recorded and streamed classes" in I3, and I3 has the kind "recorded class subscription". "Backup and disk-cloning software" (row 6) meets I3's "online backup plan". "Earth-mapping and GIS software" (row 51, Google Earth) meets I3's "maps and navigation service". "VPN client" (row 14, WireGuard and Tailscale) is labelled as a client program, while the class buyers compare is consumer VPN services (NordVPN, Proton VPN), which I3's P1 also sends to I1. "Reference software (dictionary, encyclopedia)" meets I2 e-books.
- *Fix.* Adopt the X7 sentences in section 9. Rename row 14 "VPN service and client", and source one consumer VPN comparison page.

**I1-8 (low) The compatibility ledger mixes delivery with platforms.**
- *Evidence.* Section 6 puts AlternativeTo's "Online, SaaS, Self-Hosted" into the C13 ledger. Section 7 makes the same values a `delivery` attribute.
- *Fix.* The C13 ledger holds operating systems, host programs and package sources. Delivery (download, boxed, store app, web, self-hosted, portable) is an attribute with the shared value list of X5.

**I1-9 (low) Maker class, price band and scenes.** See X1 (community or foundation project), X4 (price band for free and recurring plans) and X6 (FOSS and vintage software as scene tags, if sourced).

### I2 Digital Media & Items

**I2-1 (high) Kinds named after a platform, a maker or a region.**
- *Evidence.* I2.1 has the kinds "Kindle-format e-book", "Apple Books e-book" and "Chinese reader-format e-book". The rules they break:
  - BRIEF and S2: a kind is a generic type.
  - C13: platforms are never levels.
  - C11: a regional name is a kind only when no generic kind covers the form, and the kind label is then the generic description.
- Section 4b says the format family "decides device, reflow and layout". Device compatibility is the C13 platform question, which the memo keeps off the tree everywhere else. The memo's own sources compare on **layout**. The German FAQ: EPUB "reflowable; novels", PDF "fixed layout; technical books" (S22). The Wikipedia comparison has a "word wrap" column (S03).
- Section 4b also changes the template's test ("quality or makers") to "quality or compatibility".
- *Fix.* Kinds by layout form, with the formats as named forms. Each format carries `maker_bound` yes or no, and a C13 row where a platform owns it.
  - "reflowable e-book file": EPUB, MOBI, AZW3, KFX, FB2, .ibook.
  - "fixed-layout e-book or document file": PDF, DjVu, and Apabi .ceb or .xeb, placed by its layout as S03 states.
  - "comic and image-sequence book file": CBZ, CBR, CB7.
  - "plain-text file": TXT, RTF, DOC.
  - "digital score file": provisional.
- Kindle, Apple Books, Apabi and tolino become C13 rows. Restore the template's test in 4b and record compatibility at named-form level.

**I2-2 (high) Rights state is a kind axis in two sub-families and an attribute everywhere else.**
- *Evidence.*
  - Question 7 and section 3 make rights state (open, watermark, account-locked, locker licence) an attribute.
  - Yet audiobook kinds 14 to 16 are "single-file", "multi-file set" and "account-locked". These are packaging and rights, not form. Section 4b says Libro.fm and Audible "differ by openness, not audio quality".
  - Moving-image kinds 18 and 19 are "digital film licence" (a locker) and "video file". Its axis is "holding form".
  - A Kindle KFX book (locked) and a watermarked EPUB are not split this way.
  - "Film" also leaves no home for a TV season bought to own, and film against TV is a content distinction.
- *Objects that split.* An Audible title held as AAX and converted to M4B (kind 16 or 14). A film bought on iTunes, downloaded, and also synced to Movies Anywhere (kind 18 or 19). A TV season bought on Apple TV (no kind).
- *Fix.*
  - Audiobooks: one kind, "audiobook file", with M4B, MP3 set, AA, AAX and AAXC as named forms (AAX and AAXC maker-bound).
  - Moving images: one kind, "digital video", with MP4, MOV and MKV and the locker entitlement as named forms. Movies Anywhere becomes a C13 row.
  - In both, `rights_state` and `unit` (title, episode, season, set) are attributes. Rights state gets the generated view "files I can keep outside any store" (section 7).
  - Own home videos are video files with how-acquired = own-made.

**I2-3 (high) Font kinds by licence scope.**
- *Evidence.*
  - Kinds 25 to 31 are seven licence scopes (desktop, company desktop, webfont, app, electronic document, digital ad, server), and the typeface family is the named form. A family licensed for desktop and web therefore sits under two kinds. One family can appear under seven, which breaks one home per named form (S1, C2).
  - "Company desktop" against "desktop" is a market and user split (Appendix A).
  - The only source for the kinds is MyFonts (S12, US). Monotype says "format is not … a license" (S11), which supports keeping licence off the format, not making it a kind.
  - Section 2 itself says licence scope is chosen "once the typeface is chosen", so buyers compare typefaces and foundries first.
- *Fix.* Adopt the memo's own alternative (question 3). One kind, "font family", with the typeface family as a maker-bound named form (foundry in the maker ledger). Licence scope becomes a C3 variant (variant type `licence scope`, X2). Format (OTF, TTF, WOFF2) and the variable capability are attributes (question 4). Classification classes (S29, S30) are non-exclusive tags.

**I2-4 (medium) Music kinds do not follow the evidence cited for them.**
- *Evidence.*
  - Section 4b says "Qobuz groups by quality class and then names formats" (S09). Qobuz's classes are 24-bit to 192 kHz, 24-bit to 96 kHz, 16-bit/44.1 kHz and lossy. The memo's kinds are codec families instead: lossy, lossless compressed, uncompressed PCM and studio-resolution (DSD and DXD only). A 24/192 FLAC is "lossless compressed" in the memo but sits in Qobuz's top class. A 24/96 WAV is "uncompressed PCM".
  - Bandcamp (S08) sells "one item" and lets the buyer pick the format afterwards from a dropdown, so the compared offer is not the format.
  - C4(b) makes bit depth and sampling rate attributes.
- *Fix.* Choose one option.
  - (a) One kind, "digital music file". Named forms are the formats (MP3, AAC, Ogg Vorbis, FLAC, ALAC, WAV, AIFF, DSD, DXD). `compression` (lossy, lossless, uncompressed), bit depth and sampling rate are C4(b) attributes. The hi-res view is generated (section 7). Recommended.
  - (b) Two kinds, "lossy music file" and "lossless music file", because the coding changes what can be recovered from the file, with DSD and DXD as named forms under lossless.
- Either way, a 24/192 FLAC has one home. Owner question 7.

**I2-5 (medium) The sub-family axis changes meaning, and production assets overlap finished media.**
- *Evidence.* The level-1 axis is "medium of the thing held: what it is when it is used". It holds for text, audio, video and still images. But I2.5 "Fonts and design assets" is defined by use as production material, I2.6 by where the item lives (a game or a platform), and I2.7 by register. Objects that split:
  - a PNG texture or background pack (I2.4 lossless raster or I2.5 background pack);
  - a PSD template sold on BOOTH, often a .psd and not a .psdt (I2.4 layered image or I2.5 design template);
  - a vector illustration pack (I2.4 vector graphic or I2.5);
  - a VRoid or VRChat avatar bought on BOOTH (I2.5 3D model or I2.6 character outfit or skin);
  - an NFT game skin (I2.6 or I2.7; question 6).
- *Fix.* State the level-1 axis as **what the held data is for**: read; heard; watched; viewed; built with (production assets); used inside a game or platform account; registered (a name or a token). Then add these precedence sentences to section 3:
  - *"A file sold as a pack, template, brush, texture, model, preset or sample for making other work is I2.5, whatever its file format; a single image held to be looked at is I2.4."*
  - *"An avatar, outfit or item that is equipped inside a game or platform account is I2.6; the same model held as a file to import into tools is I2.5."*
  - *"A token is I2.7 whatever it depicts or unlocks; its use is a tag."*

**I2-6 (medium) Data objects with no kind.**
- *Evidence.*
  - **Sample packs and instrument libraries** (Splice, Kontakt libraries), **presets and LUTs** (Lightroom presets, synth presets) and **MIDI files** are bought and kept in large numbers, but none has a kind.
  - S26 lists "digital planners", which have no kind either.
  - **AI model weight files** are left open in I1 question 10, and I2 is silent on them.
  - **Messaging sticker packs** (LINE, Telegram) are platform items outside games. "Chat emoticon" names only Steam and Fortnite.
  - Podcast episode (17) and digital score (9) have no source.
- *Fix.*
  - Add an I2.5 leaf "Sound, preset and model assets" with the kinds "audio sample pack or instrument library", "preset or LUT pack", "MIDI file" and "AI model file" (owner decision).
  - Add "digital planner" to the templates leaf (S26).
  - Rename I2.6 "Game and platform items" and add "messaging sticker pack" to its Expression leaf.
  - All of these are provisional until a fetched page attests them (S6), as kinds 9 and 17 already are.
  - Apply the boundary sentence X7(h) on both sides of I1 and I2.

**I2-7 (medium) Whole sub-families rest on one source or one platform.**
- *Evidence.*
  - Fonts: one retailer (S12).
  - Moving images: one Wikipedia page on a US locker, plus the Library of Congress (S20, S32). The memo says "thin evidence, no fetched video-store tree".
  - Domain names: IANA, ICANNWiki and JPRS. There is no registrar page showing how buyers choose (a retail registrar in two regions).
  - NFTs: OpenSea and ethereum.org, so Ethereum only. A token outside the ERC standards has no named form.
  - Game items: two Western fan databases and Steamworks.
  - The Library of Congress `preservation_rank` is one US source (the memo holds it back, correctly).
- *Fix.* Before data entry, fetch one retail or registrar page per thin sub-family in a second region, and one non-Ethereum NFT marketplace page. Until then, mark the kinds of I2.3, I2.5 (fonts) and I2.7 provisional.

**I2-8 (low) Domain names and individual items.**
- *Evidence.* Edge object 4 says a blockchain name "could be kind 55 to 57 or 58". The C9 table says "crypto domain name" is an NFT (token), not a DNS domain name. A specific registered name (example.co.jp, object 19) is one individual item.
- *Fix.* Keep the alias-table rule (a crypto domain is a token) and delete the edge-object hedge. Store domains only as kind and TLD named form, never the registered name itself (BRIEF: individual items are out). Registry premium is a `platform_tag` (as written).

**I2-9 (low) Maker class, scenes, variants and price.**
- *Evidence.*
  - `maker_class` adds "platform holder", where I3 says "platform owner".
  - Section 7's scene list cites evidence pages, not definition sources (C8).
  - Variants for game styles, wear and StatTrak need variant types that C3 lacks.
  - C4(d) is applied unchanged, although domains renew every year.
- *Fix.* X1, X6, X2 and X4.

**I2-10 (low) The usability claim is optimistic.** The memo says "all twenty land in one place without a tie-break". As written, 11 of 20 test objects split (usability test below). After I2-1 to I2-6, all but the NFT-game-item case would land.

### I3 Subscriptions, Memberships & Online Services

**I3-1 (medium) Maker ladders as tier entries on plan rows.**
- *Evidence.* Section 5 puts PlayStation Plus Essential, Extra and Premium (and the others) as tier entries "on the plan row of the named form". C4(a) lists maker, line and named form as subjects, not variants or plans. C4(e) asks for a second source from another region, which a maker's own ladder never has. I1 takes the opposite view (I1-3).
- *Fix.* Adopt X3. The ladder is a tier entry with scheme `maker ladder: <named form>` on the plan row. It is self-attested by the maker page and exempt from C4(e)'s second-region rule, and it is never compared across named forms.

**I3-2 (medium) Periodicals are split by delivery, against the memo's own rule.**
- *Evidence.* Section 3.2 rejects delivery as an axis ("use delivery as a plan attribute"). Yet kind 8 is "Digital newspaper subscription" and kind 9 is "Magazine subscription, print or digital". A print newspaper delivered to the home has no kind. COICOP 09.7.2 (S01), which the memo cites, includes "subscription for newspapers (home delivery)" beside internet subscriptions.
- *Fix.* Kinds by what the plan holds:
  - "newspaper subscription (one title)";
  - "magazine subscription (one title)";
  - "news and magazine library subscription (many titles)", with Apple News+ and d-magazine.
- Make `delivery` (print, digital, both) a plan attribute.

**I3-3 (medium) Member-place kinds rest on evidence that lumps them, and mix axes.**
- *Evidence.*
  - Kinds 31 "Gym or fitness-centre membership" and 32 "Sports club membership" cite only COICOP 09.4.6.2, whose text is "membership fees for sports clubs and fitness centres": one class.
  - Kind 34 "Social or hobby club membership" against kind 32 divides clubs by activity, a subject split like the one the memo drops for catalogues.
  - In "Site or collection", "Heritage and nature property membership", "Museum and gallery membership" and "Zoo, theme-park or attraction annual pass" are divided by the type of site.
- *Objects that split.* A David Lloyd or Virgin Active club (gym and tennis; kind 31 or 32). A golf club (32 or 34). Kew Gardens or RHS membership (35 or 37). A botanical garden or aquarium annual pass (36 or 37).
- *Fix.* Use the way of entering, which the operator pages show (National Trust: 500+ places; Art Fund: many museums; a gym: one operator's sites).
  - Leaf "Facility or group": "facility membership (gym, pool, sports centre, climbing wall)" and "members' club (joined to take part: sports, social or hobby)", with the activity as a tag.
  - Leaf "Site or collection": "multi-site membership (one body's network: National Trust, English Heritage)", "multi-venue pass scheme (entry to many bodies' venues: Art Fund, city museum passes)" and "single-venue annual pass (one museum, zoo, garden, aquarium or theme park)".
  - The site type is a tag.

**I3-4 (medium) Delivery kinds break their stated axis.**
- *Evidence.* The I3.5 kind axis is "who chooses what arrives". But kind 41 is named for its goods ("Meal-kit plan"), and kind 43 "Goods rental subscription" is a different axis (the member does not keep the goods). Objects that split:
  - a coffee plan where the member picks the beans (meal-kit plan or curated box);
  - Book of the Month, where the member chooses the title;
  - a wine merchant's case plan, Laithwaites style (curated box or producer allocation club);
  - a flower subscription.
- *Fix.*
  - Rename the kinds by the axis: "provider-curated box", "member-selected menu plan" (meal kits, coffee, books) and "producer allocation club" (a winery's, brewery's or distillery's own club). A merchant's case plan is a provider-curated box.
  - Take goods rental out of this axis. If the owner rules it in (I3-Q3), make it a kind with the axis note "goods lent and returned".
  - The goods type is a link (I3-Q1), as recommended.

**I3-5 (medium) Many kinds are not yet attested; regions are thin for places and deliveries.**
- *Evidence.* The memo's limits paragraph lists kinds 2, 4, 6, 7, 8, 9, 12, 19 to 23, 28 to 30, 37 and 39 as resting on the key text, a classification or a single mention: 17 of 43.
  - Kinds 4 (paid podcast), 22 (maps), 37 (zoo pass) and 39 (season ticket) have no fetched source at all, so S6 bars them from the data.
  - Place evidence is UK-heavy (S18 to S20, S30); Germany and Japan add only transit.
  - Delivery evidence is US (S03, S04, S34, S35), plus one Japanese guide.
- *Fix.* Mark these kinds provisional. Before data entry, fetch one provider page per key-only kind, one non-UK member-place page (a gym chain or a museum outside the UK) and one non-US delivery page.

**I3-6 (medium) No kind for production-asset and font library plans.**
- *Evidence.* I2 says "the Stock subscription is I3" (I2 usability object 12 and question 10). I3.1's leaves (music, audiobooks, video, text, comics, classes, games, bundles) cover no catalogue of production assets: Adobe Stock, Envato Elements, Splice sample plans, Monotype Fonts or Adobe Fonts sold alone. Creator memberships (Patreon) are a gap the memo lists (I3-Q7).
- *Fix.* Add an I3.1 leaf "Production assets" (medium of the catalogue: images, video, sounds, fonts and templates for making work) with the kind "asset-library subscription". Its named forms need sources. Add the X7(f) sentence to P2.

**I3-7 (low) "Season ticket" is a homonym.**
- *Evidence.* Kind 39 is "Season ticket (venue, club or event series)". In the UK, a "season ticket" is also a period rail pass, which is kind 38.
- *Fix.* Add a C9 row: "season ticket (UK rail) → period transit pass; season ticket (venue or club) → season ticket; relation: homonym".

**I3-8 (low) Soft kinds.**
- *Evidence.* Satellite internet (kind 27) is justified only by Uswitch listing it separately. C10(b) also asks whether the technology changes installation needs. A dish does, so the kind passes.
- *Fix.* Cite C10(b) installation in 4b. The three video kinds stay provisional (I3-Q10). YouTube TV is "live-TV streaming bundle". An IPTV package from a broadband provider is "pay-TV package" unless it is named for the line (then I3.3).

**I3-9 (low) Shared-schema items.** See X1 ("platform owner"; `platform_ids` duplicates C13), X2 (plan ledger), X4 (annualised price) and X9 (the gaps go to the framework conflicts log).

### Usability test: 20 objects per memo, filed by two builders from the memo as written

"Same" means both builders would reach the same kind. "Split" names the two homes a builder could choose. The finding that fixes each split is given in brackets.

- **I1.**
  - *Same (12):* 1Password family plan; Norton 360 Deluxe; Photoshop single-app plan; Office Home 2024; Microsoft 365 Family; ChatGPT Plus; VLC; Chrome; Visual Studio Code; 7-Zip; Blender; Quicken.
  - *Split (8):* Windows 11 Pro licence key (named form or variant) [I1-3]; Creative Cloud Pro (raster editor, a line, or no kind) [I1-5]; PowerToys (launcher kind or system cleaner) [I1-5]; Calm (I1 wellness app or I3 recorded classes) [X7a]; Duolingo Super (I1 language learning or I3 classes) [X7a]; Backblaze Personal Backup (I1 backup software or I3 online backup) [X7b]; Arturia Pigments or a Kontakt library (no kind; add-on or I2 data) [I1-5, X7h]; Steam client (I1 or I3) [X7e].
- **I2.**
  - *Same (9):* watermarked EPUB; CBZ manga volume; Bandcamp MP3 V0 album; own .ARW raw photo; Fortnite Outfit; CS2 knife finish; Steam foil trading card; example.co.jp; ERC-721 PFP.
  - *Split (11):* 24/192 FLAC album (lossless compressed or studio-resolution) [I2-4]; Audible title converted to M4B (account-locked or single-file) [I2-2]; iTunes film also in Movies Anywhere (film licence or video file) [I2-2]; TV season bought to own (no kind) [I2-2]; typeface with desktop and webfont licences (two kinds) [I2-3]; scanned letter saved as PDF (PDF document or scanned-page file) [state: a scan goes by its file format; DjVu and PDF scans are "fixed-layout file", I2-1]; PNG texture pack (lossless raster or background pack) [I2-5]; PSD template from BOOTH (layered image or design template) [I2-5]; VRChat avatar from BOOTH (3D model or outfit) [I2-5]; LINE sticker set (chat emoticon or none) [I2-6]; Kontakt sample library or Lightroom preset pack (no kind) [I2-6].
- **I3.**
  - *Same (12):* Spotify Premium Duo; Netflix with ads; Xbox Game Pass Ultimate; Kindle Unlimited; Google One 100 GB; giffgaff SIM-only; JioFiber; Deutschland-Ticket; National Trust joint; Art Fund pass; HelloFresh; Apple One Premier.
  - *Split (8):* UK annual rail season ticket (kind 38 or 39) [I3-7]; David Lloyd membership (gym or sports club) [I3-3]; Kew Gardens membership (heritage property or attraction pass) [I3-3]; a print newspaper home delivery (no kind) [I3-2]; Trade Coffee member-picked plan (meal-kit plan or curated box) [I3-4]; Laithwaites wine plan (curated box or producer club) [I3-4]; Adobe Stock plan (no kind) [I3-6]; Calm (I3 recorded classes or I1) [X7a].

## 3. Conformance to conventions C1 to C13

Each memo has its own C1 to C13 notes: I2 and I3 have a conformance section, and I1 cites the conventions in its text. The table lists what each memo must still change to conform. "OK" means no change is needed. Cells refer to the findings above and to section 4.

| Convention | I1 | I2 | I3 |
|---|---|---|---|
| C1 maker ledger: core, lines table, extensions | Core OK. Add `maker_class` "community or foundation project" (X1). Lines table for Windows, Office, Creative Cloud and Norton 360 (I1-3). Licence stays on the named form (OK). `parent_id` for Avast and AVG needs its own source (as the memo says). | Core OK. The six new `maker_class` values map to the domain list. "Platform holder" and I3's "platform owner" become one value (X1). Foundries are makers; formats are not makers (OK). | Core OK. The ten `maker_class` values map to X1. Drop the `platform_ids` column, because the C13 `owner` field already links maker and platform (X5). `host_network_id` and `markets_served` stay as I3 extensions. |
| C2 kind against named form, `maker_bound` | OK. Every named form is a product, `maker_bound` yes. A release is a named form; edition and plan are variants (I1-3). | Formats as named forms with `maker_bound` OK. Kinds named by platform or region must become generic (I2-1). Font licence scopes stop being kinds (I2-3). | OK. Services `maker_bound` yes; Deutschland-Ticket no. Seats and tiers are attributes. |
| C3 variant ledger | Needs the variant types `edition`, `plan` and `version`, plus the plan columns. The memo's proposed "types" (`licence_model`, `seat_count`, `term`) are columns, not types (X2). | Needs `licence scope` (fonts), `style` and `wear class` (game items) as variant types (X2). The format of one purchase is not a variant: each format is a named form. | Its plan ledger becomes the shared variant ledger with variant type `plan` (X2). |
| C4(a) to C4(c) tiers, spec ladders, platform tags | Maker ladders become tier entries on variants (X3, I1-3). Lab results become tier entries. Lab seals become `certification` attributes (I1-4). | OK. No tiers on kinds. Spec ladders (bit depth, sampling rate, resolution) are attributes. Rarity, wear and registry premium are `platform_tag`. | Tier entries on plan rows need the C4(a) amendment (X3). Allowances are attributes (OK). Catalogue size is a dated attribute (OK). |
| C4(d) price band | Free band and `price_model` (X4). The memo's "first year, one seat" rule is replaced by X4. | Apply X4 to domains (annual renewal) and fonts (per licence-scope variant). | The annualised rule fits X4. Lifetime terms as written (OK). |
| C4(e) sources for a tier scheme | AV-TEST (DE) and AV-Comparatives (AT) are two sources from two countries (OK). Arena is one source (hold it). | `preservation_rank` is held back (OK). | Maker ladders are exempt under X3. No other scheme. |
| C5 levels and axes | Merge the two exempt sub-families into one (I1-1). Money and business: `leaf = null` (I1-2). Leaf axes are stated (OK). | Restate the level-1 axis (I2-5). Leafless sub-families store `leaf = null` (OK). No parts sub-family (OK; S3 gives I2 no parts). | OK. Leaf skipped in I3.2, I3.3 and I3.5. No parts sub-family (OK). Plan add-ons go to the plan ledger. |
| C6 size, fit and user | OK. Audience and seats are tags or variants. | OK. File size and resolution are attributes. | OK in the memo. The step 5 note on seat structure conflicts with C6 (X9). |
| C7 order inside a leaf | OK. Variants by version, then plan. | OK for named forms. "Open standard first" is a stated secondary key and should be written into C7 as the I2 secondary key. | OK. Plans by seat, then ladder, then term. |
| C8 scene vocabulary | Scene tags for FOSS and vintage software if each gets a definition source; otherwise attributes as written (X6). | Each section 7 tag needs a definition source, not evidence pages (X6). | Empty; OK. |
| C9 alias and homonym table | OK (Microsoft 365 / Office 365; suite; launcher; client; 家計簿). | OK. Add "skin" as a three-way homonym once avatar skins are placed (I2-5). | Add "season ticket" (I3-7). Otherwise OK and rich. |
| C10 rule T | AI-enabled is an attribute; the assistants the key names are kinds (OK). Keep the AI image generator as one kind with `task_mode` (owner question). | DRM and the variable font capability are attributes (OK). | Satellite internet passes C10(b) by installation; say so (I3-8). |
| C11 rule R | OK (nengajō software is a named form under home publishing). | "Chinese reader-format e-book" breaks C11 (I2-1). | OK (定期券 and Deutschland-Ticket are named forms). |
| C12 rule M | Not applicable. | Not applicable. | Not applicable. |
| C13 compatibility ledger | Remove delivery values from the ledger (I1-8). Share the platform rows (X5). | Main device; add Kindle, Apple Books, Apabi and Movies Anywhere rows after I2-1 and I2-2. Share the rows (X5). | OK. Share the rows (X5). |

## 4. Cross-memo consistency

**X1 (medium) Maker ledger: three sets of `maker_class` values for one domain.**
- *Evidence.*
  - I1 adds "community or foundation project" (LibreOffice, Blender, KeePass).
  - I2 adds storefront, platform holder, format steward, foundry, registry operator and game publisher.
  - I3 adds platform owner, independent service, network operator, MVNO or reseller, non-profit membership body, venue or club operator, transport operator or association, marketplace operator, aggregator and resale marketplace. It also adds the columns `host_network_id`, `platform_ids` and `markets_served`.
  - "Platform holder" (I2) and "platform owner" (I3) are the same class.
  - Many makers appear in all three categories, and in D5: Apple, Google, Amazon, Microsoft, Adobe, Sony, Nintendo, Valve, Epic.
- *Proposed shared convention (domain I).*
  - One maker row per company across I1, I2, I3 and D5, with `known_for_kinds` derived from the named-form ledger (C1).
  - One `maker_class` list:
    - software publisher;
    - community or foundation project;
    - platform holder;
    - storefront or marketplace (with a `resale` flag);
    - game publisher;
    - type foundry;
    - format steward or standards body;
    - registry operator;
    - network operator;
    - MVNO or reseller;
    - membership body;
    - venue, club or attraction operator;
    - transport operator or association;
    - aggregator;
    - producer (for producer clubs);
    - curated-box company.
  - `platform_ids` leaves the maker ledger, because C13's `owner` links the two. `host_network_id` stays as an I3 extension. `markets_served` stays as a region-tag list.

**X2 (high) Variant ledger: three shapes.**
- *Evidence.*
  - I1 question 6 asks for "`version`, `edition_or_plan`, `licence_model`, `seat_count` and `term`" as variant types. That mixes types with columns.
  - I3 builds a plan ledger with variant type `plan` and about twenty columns.
  - I2 needs styles, wear and StatTrak for game items, and (after I2-3) licence scope for fonts.
  - C3 knows only colourway, material, print, size, reference, retro, collaboration and limited edition.
- *Proposed shared convention.* One C3 ledger.
  - **New variant types:** `edition`, `version`, `plan`, `licence scope`, `style`.
  - **New columns, used only by those types:**
    - `seat_structure`, `seat_count` and `eligibility`;
    - `term`;
    - `price_model` (free, freemium, one-time, subscription, bundle);
    - `list_price`, `currency`, `price_date` and `annual_price_usd`;
    - allowances (`storage_gb`, `data_gb`, `speed_mbps`, `devices`, `cloud_hours`, `credits_per_period`);
    - `components` (kind ids, for bundles);
    - `addon_of`;
    - `status` (active, closed to new members).
  - `licence_class` and `spdx_id` sit on the named form (I1), and a variant may override them (dual licensing).
  - One row type then serves Microsoft 365 Family (I1), a webfont licence for a family (I2) and Spotify Duo (I3).

**X3 (high) Tier entries from makers: I1 says no, I3 says yes, and C4(a) has no subject for them.**
- *Evidence.*
  - I1 section 5: maker edition ladders "are `edition` variants, not tiers, because the maker, not a third party, defines the order".
  - I3 section 5: maker ladders are "tier entries … on the plan row".
  - The domain E review (decision 6) adopted "maker ladders as tier entries" on lines.
  - C4(a) allows maker, line and named form as subjects. C4(e) asks for a second source from another region.
  - I1 also wants lab results on versions.
- *Proposed amendment to C4(a).* A tier entry may sit on a variant or plan row in two cases:
  - (i) The scheme is the maker's own ladder for one named form: `scheme = maker ladder: <named_form_id>`, value = the label, plus `rank`. Such a scheme is attested by the maker's page alone (exempt from C4(e)) and is never compared across named forms.
  - (ii) An external test scores a specific version (AV-TEST rounds).
  - Pass marks and seals are C4(b) `certification` attributes.
  - I1 changes its section 5 to match. I3 stays as written, apart from citing the amendment.

**X4 (high) Price band for free, recurring and per-seat prices: three rules.**
- *Evidence.*
  - I1 bands "from the first-year list price for one owner (one seat)", with a zero band and `price_model`.
  - I3 bands from "the annualised list price in USD at a dated rate" of the plan as sold, which means all seats for a family plan, with lifetime terms at full price.
  - I2 applies C4(d) unchanged, although domains renew every year and font prices vary by licence scope.
  - The rules give different bands for the same object. Spotify Family is one seat's share under I1, and the whole plan under I3.
- *Proposed addition to C4(d) for domain I.*
  - The band is computed on each variant or plan row, from the annualised list price of that plan as sold (all seats included, `seat_count` recorded), at a dated USD rate.
  - A promotional first-year price is recorded but not used.
  - One-time and perpetual licences use the full price; lifetime and multi-year terms use the full price with the term recorded.
  - Free plans get the band "0 (free)".
  - A domain name uses the TLD's standard annual renewal price, with registry premium as a `platform_tag`.
  - A named form's band is the band of its cheapest paid plan, plus a `has_free_plan` flag.

**X5 (medium) One compatibility ledger, one delivery list.**
- *Evidence.*
  - I1 lists operating systems, host programs and package sources, and also "Online, SaaS, Self-Hosted".
  - I2 lists Kindle, Kobo, tolino, Apple Books, Adobe DRM, Audible, Movies Anywhere, Steam, Fortnite, CS2, ERC-721 and ERC-1155, and the DNS root.
  - I3 lists PlayStation, Xbox, Nintendo, Apple, Google and Amazon ecosystems, host mobile networks and transport associations.
  - Several rows recur (Apple, Google, Amazon, Microsoft/Xbox, Sony, Nintendo, Valve), and D5 needs the same console rows.
  - Delivery values differ: I1 has download, boxed, store app, web, self-hosted and portable; I3 has stream, download, physical, entry and network.
- *Proposed shared convention.*
  - One C13 ledger for domain I and D5, with shared `platform_id`s. Fortnite and CS2 are rows only as game platforms for items; Kindle is a row as a reading platform.
  - One `delivery` attribute list: download; boxed or carrier; app store; web or hosted; self-hosted; portable; stream; physical delivery; entry to a place; network connection.
  - Delivery is never a C13 row.

**X6 (low) Scenes: none, a private list, and empty.**
- *Evidence.* I1 turns FOSS, freeware, vintage collecting and regional ecosystems into attributes and views. I2 has its own list (hi-res audio, e-reader ecosystems, doujin goods, skin traders, NFT communities, domain investors, type design), whose sources are evidence pages. I3 has no scenes.
- *Proposed.* Domain I uses the shared C8 list. Candidate tags are free and open-source software, retro software collecting, hi-res audio, doujin and creator goods, skin trading, NFT collecting and domain investing. Each tag needs a definition source (a community wiki or glossary) and is held back until it has one. Ecosystems and regions stay C13 rows and region tags, as the memos propose.

**X7 (high) Boundaries the memos leave open or answer differently.** Each item gives a proposed precedence sentence for both memos' section 9.
- **(a) Classes, wellness and learning apps (I1, I3).**
  - *Evidence.* I1 sentence 6 says "wellness and meditation apps are I1 by function". I3's kind 13 and key branch (a) put "recorded and streamed classes" in I3.
  - *Sentence.* *"A plan whose value is a library of recorded or streamed lessons, sessions or classes to watch or listen to (Apple Fitness+, Calm, Headspace, MasterClass, Peloton App) is I3, recorded class subscription. A program that does the exercise with the user, testing, correcting or adapting to the user's answers (Duolingo, Babbel, a typing tutor, a flashcard app), is I1, learning software."* I1 deletes "wellness and meditation apps are I1".
- **(b) Backup (I1 row 6, I3 kind 19).**
  - *Sentence.* *"Backup software that copies to the owner's own drives is I1. A plan whose value is keeping the backup on the provider's servers (Backblaze Personal Backup) is I3, even with its own client program. A package named and sold as a security or backup program that includes cloud space (Acronis) is I1."*
- **(c) Maps (I1 row 51, I3 kind 22).**
  - *Sentence.* *"A map or navigation service (Google Maps, Waze, Google Earth on the web, a paid navigation app with downloadable maps) is I3. A program that edits or analyses geographic data (QGIS, Google Earth Pro on the desktop) is I1, GIS software."*
- **(d) VPN.** Both memos send VPN to I1. I1 renames its kind "VPN service and client" (I1-7). I3's P1 stays as written.
- **(e) Game launchers and stores (I1 sentence 3, I1 question 3; nothing in I3).**
  - *Sentence (owner to confirm).* *"A game store or launcher client and its free account (Steam, Epic Games Launcher, GOG Galaxy) are not filed: they are the way games and items are bought and held. The games are D5, the items I2, and a paid subscription on the store is I3."* This follows the step 5 note ("the item held in it is in") and I3's rule that a mere way of buying is not filed.
- **(f) Production-asset plans (I2, I3).**
  - *Evidence.* I2 sends the Adobe Stock plan to I3. I3 has no kind for it (I3-6).
  - *Sentence (I3 P2).* *"A plan giving access to a library of images, video, sounds, fonts or templates for making work is I3, asset-library subscription; each asset downloaded and licensed under it is I2."*
- **(g) Plans tied to one device (I1 SF13, I3.3, I3.1).**
  - *Sentence.* *"A paid unlock or subscription that switches on a function of software built into one device (heated seats, driver assistance, a camera's extra recording mode) is I1. A plan whose value is a data connection for that device (car connected services, a smartwatch eSIM line) is I3, connectivity. A class catalogue for one device (Peloton All-Access) is I3, catalogue. Free companion apps are part of the device."*
- **(h) Data loaded by programs (I1 sentence 4, I2 boundary with I1).**
  - *Evidence.* The two sentences agree in general, but neither places presets, sample libraries, LUTs, MIDI files or AI model weights.
  - *Sentence.* *"A file that a program loads but that adds no executable code (sample library, instrument library, preset, LUT, MIDI file, AI model weights) is I2. A plug-in that adds processing code to a host program (VST/AU instrument or effect, image-editor filter plug-in, browser extension) is I1, add-on. A mod that changes a game's play is D5."*
- **(i) Reference works (I1 row 41, I2 text).**
  - *Sentence.* *"A dictionary, encyclopedia or other reference work held as a file in an e-book format is I2. One delivered as its own program, or on a disc as a program (Encarta, a dictionary app with its own search), is I1."*
- **(j) Credits (I1 object 10, I2 object 7, I3 object 8 and I3-Q4).**
  - *Evidence.* Firefly and Audible credits are OUT, and the plans are in. ClassPass is recommended IN, yet its plan is nothing but credits.
  - *Shared sentence.* *"A plan that renews credits each period is filed as the plan, by what the credits reach (I1 for software use, I3 for a catalogue or for venues), with `credits_per_period` as a plan attribute. Credits bought on their own, and balances that can be cashed or transferred, are OUT (step 1)."*
- **(k) NFT memberships and tickets (I2 question 6; nothing in I3).**
  - *Sentence (I3 P4).* *"A membership or pass carried by an NFT is I2 as the token. It is I3 only when the same access is also sold as a plan, which is then filed once, as the plan."*
- **(l) Messaging and video calls (I1 edge object 4, I1 question 3, I3 kind 21).** I3 renames kind 21 "messaging, calling and video-conferencing service" (WhatsApp, Zoom, Slack, Discord). I1 keeps the email client in I1 and the mailbox in I3 (both agree).

**X8 (low) Duplicated or doubly unsourced concepts.**
- Podcasts: I2 kind 17 (file) and I3 kind 4 (paid podcast subscription) are both unsourced. Fetch one page that covers both, and keep both kinds provisional until then.
- Audiobooks are consistent. The file is I2, the catalogue plan I3 and the credit OUT.
- Bundles are consistent: Microsoft 365 Family is I1, Google AI Pro is I1 and Google One is I3.
- No kind appears in two memos.

**X9 (medium) Framework conflicts to log (for framework/structure/_framework_conflicts.md; not applied here).**
- **Seat structure (I3 gap 5, I3-Q5).** The step 5 note counts "the seat structure (individual, family, student)" as part of the kind of access. C6 and Appendix A make user a tag. Both I1 and I3 treat seats as plan attributes. *Fix:* delete "and the seat structure (individual, family, student)" from the step 5 note, and add "seat structure is a plan attribute".
- **"In-game items" (I2).** The I2 branch and the D5 note should read "in-game and platform items", to include Steam profile items and messaging stickers.
- **Home recordings (I2).** The F1 note's "home recordings … are F5" should read "home recordings on a physical carrier are F5".
- **Domain names (I2).** The step 1 note should say that a domain name registration is I2, not a right in itself.
- **Medical software (I1 sentence 6).** Step 2 names devices and monitors, not software. *Fix:* add "software made to diagnose, treat or monitor a condition, such as a regulated medical app, is H2".
- **Gaps in I3's key (I3 section 9).** Goods rental subscriptions, hosting plans, creator memberships, the physical SIM card or eSIM profile, and car-sharing memberships.

## 5. Owner decisions raised (merged and de-duplicated)
PENDING
