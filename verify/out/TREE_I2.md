# I2 Digital Media & Items: decided tree

Category: I2 Digital Media & Items (domain I, Software, Digital & Subscriptions). Membership test: anything that exists only as data and is held as a file, licence entitlement or registered token: e-books, audiobooks, digital music and film, podcasts kept as files, fonts, digital artwork, the owner's own photographs, home videos and scanned records held as files (the carrier decides: prints are F5), in-game and platform items (characters, skins, cosmetic and consumable items, platform profile items, messaging stickers), domain names and NFTs (CATEGORIES_v0_7 step 5, K-69). Not here: the same work on a disc, tape, cartridge or paper (F1; home recordings on a physical carrier and papers F5; edition or signed photographic prints F2); unredeemed download codes, cards and vouchers, gift-code, wallet and game or platform currencies, loose credits and time-limited digital rentals (OUT); games, expansions, add-ons that change play and mods (D5); programs, apps and plug-ins that add code, and reference works delivered as their own program (I1); plans, catalogue passes, asset-library subscriptions, battle or season passes and memberships also sold as a plan (I3); printed trading cards and paper stickers (F3, E1, C5). Game launchers, their free accounts and free locker accounts are not filed. Structure (Candidate A, decided I-2; memo sections 3 and 10): sub-family by what the held data is for (read, heard, watched, viewed, built with, used inside a game or platform account, registered), then leaf by one axis per sub-family (kind of recording in I2.2, I-9; asset class in I2.5; role of the item in the game or platform account in I2.6; register, DNS or blockchain, in I2.7; no leaf in I2.1, I2.3 and I2.4, leaf = null), then kind: the class buyers compare (layout form for text; one kind each for music, audiobooks, podcasts, video and fonts; file-format family for still images; asset class for production assets; item role for game and platform items; TLD eligibility class for domain names; token form for NFTs). Each object gets one kind. Platform, store, maker and region never name a kind (Kindle, Apple Books, Apabi, Kobo, tolino, Audible, BookWalker, Movies Anywhere, Steam, LINE, games, blockchains and naming roots are C13 rows); `rights_state` (open file, personalised watermark, account-locked, locker licence, token; no "rental" value), `unit`, `compression`, quality values (bitrate, bit depth, sampling rate, resolution), `abridgement` (on the audiobook named form), font file format and variable capability, `font_classification` (non-exclusive tags on the typeface family), licence scope (a variant for fonts, an attribute for single stock assets), how acquired, language and script, `delivery`, `preservation_rank`, rarity (a dated platform tag) and use tags of tokens are attributes, tags or variants, never kinds; genre and subject are barred (light novels are reflowable e-books; genre-led shop navigation is not imported). A particular registered domain name, a single token and the wear of one skin are individual items and are not stored. Maker role: owner (maker_roles.tsv, provisional: items carry their platform or issuer; foundries, issuers and platforms in the one maker ledger). A kind marked † is named by the memo without a fetched page and needs one before it enters the data (I-13, I-22); the leaf I2.5.4 holds only † kinds and is provisional with them; the ids of † kinds are allocated here (wave-2 convention) and are those of memo section 13. Display groups (navigation proposal, display only, one to one with the sub-families): G-I2-1 Read (I2.1); G-I2-2 Listen (I2.2); G-I2-3 Watch (I2.3); G-I2-4 View and keep images (I2.4); G-I2-5 Create with (fonts and assets) (I2.5); G-I2-6 Use in a game or platform (I2.6); G-I2-7 Register (names and tokens) (I2.7); level 2 follows the leaves. Quality markers (display): all media files by rights state first (DRM-free open file > personalised watermark > account-locked > locker licence), then format fit for the device; music and video by technical quality as measured attributes, never tiers (uncompressed or lossless 24-bit/192 kHz > 24/96 > 16/44.1 > lossy 320 kbps > V0 > 128; video 4K > HD > SD); audiobooks unabridged before abridged, then narration and production quality and length; fonts by typeface first, then licence-scope fit, script and language coverage, variable capability and foundry; domain names by TLD eligibility class, standard renewal price and registry premium status; game and platform items by rarity label (platform tag) and tradability on the platform.

Ids (R-58): I2.n is a sub-family and I2.n.m a leaf; a kind is I2.n.m.kk, or I2.n.kk where a sub-family has no leaf.

## I2.1 Text and document files

Read. No leaf (leaf = null); kind axis: layout form (I-7). Formats are named forms; e-reader platforms are C13 rows.

- I2.1.01 Reflowable e-book file: a book package whose text reflows to the screen.
- I2.1.02 Fixed-layout e-book or document file: a file that keeps a fixed page, including a fixed-page text book and a scanned document saved as PDF or DjVu.
- I2.1.03 Digital comic or manga file (image-page book) [manga; webtoon; BD; 漫画; 만화]: a book whose pages are drawn or photographed images, read page by page or by vertical scroll (comic, manga, bande dessinée, webtoon), held in any container.
- I2.1.04 Plain and rich text file: a bare text or word-processor file with no e-book package.
- I2.1.05 Digital score file: a music score held as a file. †

## I2.2 Audio files

Heard. Leaf axis: kind of recording (music, spoken word, podcast; a form of medium, not a genre; I-9). Each leaf holds one kind.

### I2.2.1 Music recordings

- I2.2.1.01 Digital music file: music held as an audio file, lossy, lossless compressed or uncompressed (compression and resolution are attributes, I-8).

### I2.2.2 Spoken-word books

- I2.2.2.01 Audiobook file: a book read aloud, held as a file or file set, open or account-locked (`rights_state`), abridged or unabridged (`abridgement`).

### I2.2.3 Podcast episodes

- I2.2.3.01 Podcast episode file: an episode of a podcast kept as a file. †

## I2.3 Moving-image files

Watched. No leaf (leaf = null); one kind (I-10).

- I2.3.01 Digital video: film, TV, home video or video artwork held as a video file or as a purchased locker entitlement with no file held, any unit (title, episode, season).

## I2.4 Still-image files

Viewed. No leaf (leaf = null); kind axis: file-format family.

- I2.4.01 Camera raw photo file: an unprocessed image as recorded by a camera's sensor.
- I2.4.02 Lossy compressed photo file: a photograph or raster image saved with lossy compression.
- I2.4.03 Lossless raster image file: a pixel image saved uncompressed or with lossless compression.
- I2.4.04 Layered image file: a raster image file that keeps separate editable layers.
- I2.4.05 Vector graphic file: an image made of shapes and paths that scales without loss.

## I2.5 Fonts and production assets

Built with. Leaf axis: asset class.

### I2.5.1 Fonts

- I2.5.1.01 Digital font: a typeface family held as font files under a licence (the family is the named form, licence scope a variant, I-11).

### I2.5.2 Templates and production packs

Kind axis: file kind for the target tool.

- I2.5.2.01 Design template file: a layout file sold to be filled in or adapted in a design tool, including a PDF sewing or knitting pattern.
- I2.5.2.02 Brush pack: a set of brushes for a drawing or painting program.
- I2.5.2.03 Background, texture and frame pack: a pack of image materials sold for use in making other work.
- I2.5.2.04 Motion graphics template: an editable animated-graphics project file for a video or motion tool.
- I2.5.2.05 Digital planner: a planner or organiser held as a file to write in on a device.

### I2.5.3 3D assets

Kind axis: asset part.

- I2.5.3.01 3D model file: a three-dimensional model held as a file to import into tools, including an avatar model.
- I2.5.3.02 3D material file: a surface material or shader definition for 3D rendering.
- I2.5.3.03 3D light file: an environment lighting map or light setup for 3D rendering.

### I2.5.4 Sound, preset and model assets

Provisional with its kinds (I-13): files a program loads without adding code (K-71(h)).

- I2.5.4.01 Audio sample pack or instrument library: recorded sounds or a sampled instrument held as files for a music program. †
- I2.5.4.02 Preset or LUT pack: saved settings or colour look-up tables loaded by an editing or sound program. †
- I2.5.4.03 MIDI file: a file of note and control data that a program plays or edits. †
- I2.5.4.04 AI model file: AI model weights held as a file. †

## I2.6 Game and platform items

Used inside a game or platform account. Leaf axis: role of the item in the game or platform account. Game, platform and rarity are not levels (the game is a C13 row and a generated view, I-14); item designs are named forms, harvested uncapped.

### I2.6.1 Character and avatar wear

- I2.6.1.01 Character outfit or skin: an item that changes the look of a player's character or agent.
- I2.6.1.02 Avatar accessory: a worn add-on item for a character, such as back items, shoes, gloves or banners.
- I2.6.1.03 Companion: a pet or sidekick that accompanies a player's character.

### I2.6.2 Tools, weapons and vehicles

- I2.6.2.01 Weapon skin: a finish that changes the look of an in-game weapon.
- I2.6.2.02 Tool and traversal skin: an item that changes the look of an in-game tool or traversal gear (pickaxe, glider, trails).
- I2.6.2.03 Wrap or surface finish: a finish applied across the surfaces of vehicles, weapons or other items.

### I2.6.3 Expression

- I2.6.3.01 Emote: an animation or dance a player's character performs on command.
- I2.6.3.02 Spray or graffiti: an image a player places on surfaces in the game world.
- I2.6.3.03 In-game sticker or charm: a sticker, patch or charm applied to an in-game item.
- I2.6.3.04 Chat emoticon: a small image used in a game's or platform's chat.
- I2.6.3.05 Music kit or lobby music: an item that replaces a game's music or lobby track.
- I2.6.3.06 Messaging sticker pack: a set of stickers used in a messaging platform's chats. †

### I2.6.4 Containers and unlocks

- I2.6.4.01 Loot container: an item that opens to give one or more random items.
- I2.6.4.02 Unlock key: an item that opens a loot container.

### I2.6.5 Collectibles and profile items

- I2.6.5.01 Platform trading card: a collectible card held as data in a game platform account (foil is a style variant).
- I2.6.5.02 Profile background: an image item shown behind a platform profile.
- I2.6.5.03 Badge or pin: a badge or pin item shown on a platform profile or in a game.

## I2.7 Names and tokens

Registered. Leaf axis: register (DNS or blockchain).

### I2.7.1 Domain names

Kind axis: eligibility class of the TLD (I-12); each TLD is a named form.

- I2.7.1.01 Open generic-TLD domain name: a domain-name registration under a generic TLD open to any registrant.
- I2.7.1.02 Country-code domain name: a domain-name registration under a country-code TLD that is not reserved to a registrant class.
- I2.7.1.03 Eligibility-restricted domain name: a domain-name registration under a second-level name reserved to a registrant class, or in a sponsored or restricted gTLD.

### I2.7.2 Tokens

Kind axis: token form (I2-O1); token standards, then NFT collections (maker-bound), are named forms.

- I2.7.2.01 Unique (1/1) NFT: a non-fungible token that is the only one of its token ID.
- I2.7.2.02 Semi-fungible NFT: a token issued in several identical copies under one token ID.

## Precedence inside I2

- A file sold as a pack, template, brush, texture, model, preset or sample for making other work is I2.5, whatever its file format; a single image, clip or track held to be looked at, watched or heard is filed by its medium (I2.2, I2.3, I2.4), even when it was licensed as a stock asset. A PDF sewing or knitting pattern is I2.5.2.01 Design template file.
- An avatar, outfit or item that is equipped inside a game or platform account is I2.6 (for example I2.6.1.01 Character outfit or skin); the same model held as a file to import into tools is I2.5.3.01 3D model file.
- A token is I2.7.2 (I2.7.2.01 or I2.7.2.02 by token form) whatever it depicts or unlocks; its use (art, PFP, game item, membership, ticket, domain) is a tag. A blockchain domain name is a token, I2.7.2.01 Unique (1/1) NFT, not a DNS name.
- An e-book package that reflows to the screen (EPUB, Kindle formats, FictionBook, .ibook) is I2.1.01 Reflowable e-book file; a file that keeps a fixed page (PDF, DjVu), including a scan saved as PDF or DjVu, is I2.1.02 Fixed-layout e-book or document file; a bare text or word-processor file with no e-book package is I2.1.04 Plain and rich text file.
- A book of image pages is I2.1.03 Digital comic or manga file whatever its container; a scanned document or a fixed-page text book stays I2.1.02, and a reflowing book I2.1.01. EPUB, AZW3 and PDF keep their one home under I2.1.01 or I2.1.02 (the I2.1.03 page cross-links them, display only).
- A second-level name reserved to a registrant class (CO.JP, AC.JP, ED.JP, GO.JP) and a name in a sponsored or restricted gTLD are I2.7.1.03 Eligibility-restricted domain names; other names under a country code are I2.7.1.02 Country-code domain names.
- A photograph, home video or scan held only as a file is I2 whoever made it or is shown; a scan is filed by its file format (TIFF in I2.4.03; PDF or DjVu in I2.1.02); a digital artwork file is I2, and a video work held as a file is I2.3.01 Digital video.
- A purchased film or TV title is I2.3.01 Digital video whether a file is held or only a locker entitlement (`rights_state` = locker licence); a time-limited rental is OUT.
