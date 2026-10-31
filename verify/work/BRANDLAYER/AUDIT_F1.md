# AUDIT F1 (cold, Opus)

SCOPE: owner 2026-10-31 (BRIEF.md) narrowed F1 to makers known for the physical object.
Classified by script (AUDIT_F1_tmp/classify.py): keep 132 (globes 62, maps 22, boutique video discs 20, audiophile reissues 9, private-press 7, scholarly sheet-music editions 6: Carus-Verlag, Ernst Eulenburg, Editions de l'Oiseau-Lyre, PWM Edition, Stainer & Bell, Editions Durand; audiophile labels from the record lists 6: Audio Fidelity Records, Chesky, Stockfisch, Telarc, Water Lily Acoustics, Linn Records); defer 4426 harvest rows + 46 RPG-book publishers from MOVES_E1 = 4472 rows in DEFER_F1.json (with src, evidence class, red-link flags and same-target merge groups); drop 192.
ACCURACY (keep group, seed 7): 25/25 shown on the fetched raw page and claim supported; 0 wrong.
Weak: 3 rows rest on Wikipedia category membership only (Bella Terra, Compass Maps, Universal Publishers), Three Blind Mice on a retailer page only.
WHOLE-FILE CHECKS (scripts against the harvester's saved raw pages F1_tmp/*.txt, re-located line by line, AUDIT_F1_tmp/locate.py): (1) 188 rows from List of independent UK record labels are the 'Music industry' navbox under References (genres, roles, charts, trade bodies, TV channels, retailers HMV/Fnac/Virgin Megastores, 't','v','e', truncated names Beggars/Domino/Secretly/Warner/Universal) plus 'Record production portal' (See also), 'Europe' and 'Tropes' (comics Works cited): all 192 dropped.
(2) 37 deferred rows link to red links (no own article) -> tier listed if ever used (e.g.
12-Gauge Comics, Tips Industries, Rainy Day Records, 16 manga publishers); 7 more point to a person/band article not the firm (Master Records and Variety Records -> Irving Mills, Ambush Reality -> Enter Shikari, Aida-Zee -> L.
Nathan Butler, Ominous Press -> Bart Sears, Hell Comics -> Air Pirates, iBooks -> Byron Preiss) -> listed.
(3) defunct labels: not separable by script from list pages; all record labels are deferred anyway, so the 'still owned and traded -> stays' rule passes to the future taxonomy.
(4) 37 same-target duplicate groups (e.g.
Cherry Red/Cherry Red Records, Nude/Nude Records, MLJ Magazines->Archie Comics, Americomics+Paragon->AC Comics, Carlsen Comics+Carlsen Manga, Panini Manga->Panini Comics, Humanoids Publishing+Shogun City->Les Humanoides Associes, Crunchyroll listed under Kaze) are in DEFER_F1.json 'merges'; one parse glitch 'Gringo Recordsjames' -> Gringo Records.
Most parenthesised names (Apollo Records (1928)/(1944) etc.) are genuinely different labels: keep the disambiguator, do not merge.
(5) Evidence classes: Girder retailer list = existence only (7 Girder rows to listed, 2 upgraded by Analog Planet); Arab World Books and African Books Collective = existence only; Boutique Blu-ray Wiki = existence only; Bookseller award rows = quality (all deferred now); Paste 2017 = independent editorial pick and COUNTS for its five headed entries, but its own text undercuts Olive Films and Twilight Time (bare-bones, scratched transfers) and the six names in its closing sentence are mentions only -> cultural.
(6) MOVES_E1.json: 46 RPG-book publishers, 0 overlap with the F1 harvest; all are genre book publishers -> deferred.
RETRIES (keep group only, regional publisher retries stopped per coordinator): audiophile press done (SoundStage!, Analog Planet, Victrola) -> pressing plants Pallas, RTI, QRP, Fidelity Record Pressing and ORG/Sundazed; boutique praise done (CBR, Paste) -> Fun City Editions, Indicator and Warner Archive upgraded; Royal Warrant done (Printweek 2026) -> hand binders and archival box/storage makers; maps -> swisstopo, Kummerly+Frey; fine-press awards: no Oak Knoll fine-press award exists as such (Oak Knoll is a dealer/publisher; FPBA was founded at Oak Knoll Fest); FPBA member list used for existence only.
BLIND SPOTS: storage & protection (comic bags, record sleeves, disc cases) still thin beyond BCW/E.
Gerber/Ultra Pro and the warrant archival firms; collectors' editions outside UK/US (Japan, Germany, Italy facsimile houses) not searched; scholarly music editions beyond Europe (Zen-On is deferred) not searched; globes after 1960 (Zoffoli found only on its own site, not recorded); Japanese/Chinese traditional book makers and Indian palm-leaf/pothi makers not searched.

## Additions (22)
- Schallplattenfabrik Pallas (premium, Germany): SoundStage! Hi-Fi: "Pallas and RTI are acknowledged as the best vinyl producers in the world" (German pressing plant, Diepholz, est. 1948)
- Record Technology Inc. (RTI) (premium, USA): SoundStage!: Pallas and RTI "acknowledged as the best vinyl producers in the world"; Victrola: opened 1974 with a focus on hi-fi records, "vaunted reputation"
- Quality Record Pressings (premium, USA): SoundStage!: Analogue Productions' own plant (Salina, Kansas, 2011) built "to make the best records in the world"; QRP pressings "just as good" as Pallas/RTI
- Fidelity Record Pressing (cultural, USA): Victrola: home of the Mobile Fidelity series, started by RTI veterans, "gotten great reviews in a hurry" (Victrola is a turntable maker, not a seller of these records)
- Original Recordings Group (premium, USA): SoundStage!: among American companies "producing good vinyl" with MoFi, Music Matters and Sundazed; = "Org Music" row in the record-label list (move from DEFER to keep and merge)
- Sundazed Records (cultural, USA): SoundStage!: among American companies producing good vinyl (reissue label)
- Fun City Editions (cultural, USA): CBR "10 Best Boutique Blu-Ray Brands" no.1: "newest boutique Blu-ray companies to make waves in the collecting community"
- swisstopo (premium, Switzerland): University of Zurich geography blog: Dufour map "a masterpiece of cartography"; the "Swiss style" earned the Topographical Bureau (swisstopo) "much praise and several international awards"
- Hallwag Kümmerly+Frey (cultural, Switzerland): Switzerland Tourism: Switzerland's leading publisher of tourism maps; red-and-yellow and blue maps "renowned wherever you go", "Swiss quality mapping"
- Temple Bookbinders (cultural, UK): Printweek 2026: Royal Warrant to HM The King, hand bookbinding and conservation (Oxford)
- Barnard & Westwood (cultural, UK): Printweek 2026: Royal Warrants to the King and Queen as printers and bookbinders (London, est. 1921); already known in C5, add F1 dept
- Blissetts (cultural, UK): Printweek 2023: holds a Royal Warrant as bookbinder; antique book restoration with hand tooling
- G Ryder & Co (cultural, UK): Printweek 2026: Royal Warrant, specialist box makers (book/archive boxes)
- I. Waterman (Boxmakers) (cultural, UK): Printweek 2026: Royal Warrant, manufacturer of archive boxes
- Conservation Resources (UK) (cultural, UK): Printweek 2026: Royal Warrant, manufacturers of archival storage materials
- Secol (cultural, UK): Printweek 2026: Royal Warrant, manufacturers of archival and photographic storage systems
- Maggs Bros (cultural, UK): Printweek 2026: Royal Warrant, purveyors of rare books and manuscripts (antiquarian dealer)
- Ninja Press (cultural, USA): Fine Press Book Association member press (association of book arts "that aspire to the highest standards of craft and design"); membership listing = existence only, tier listed
- Midnight Paper Sales (cultural, USA): Fine Press Book Association member press (association of book arts "that aspire to the highest standards of craft and design"); membership listing = existence only, tier listed
- Peter Koch Printers (cultural, USA): Fine Press Book Association member press (association of book arts "that aspire to the highest standards of craft and design"); membership listing = existence only, tier listed
- Deep Wood Press (cultural, USA): Fine Press Book Association member press (association of book arts "that aspire to the highest standards of craft and design"); membership listing = existence only, tier listed
- Greenboathouse Press (cultural, Canada): Fine Press Book Association member press (association of book arts "that aspire to the highest standards of craft and design"); membership listing = existence only, tier listed

## Tier changes
- Music Matters Jazz: premium (retailer page) -> premium. Analog Planet: "Music Matters set the standard for Blue Note reissues"; independent support for a Girder-only row
- Tone Poet Audiophile Vinyl Reissue Series: premium (retailer page) -> premium. Analog Planet best reissues of decade: Tone Poet Blue Notes "wildly popular" and "great sounding"; rename "Blue Note Tone Poet series" (sub-line of known Blue Note Records)
- Sam Records, Pure Pleasure Records, Electric Recording Company, Audio Fidelity, Reference Recordings, Three Blind Mice, Chasing The Dragon: premium -> listed. Girder Music is a retailer blog: existence only; no independent page fetched for these (Pure Pleasure/ERC/Reference Recordings are well known; leave to a later sweep)
- Indicator:  -> premium. CBR: "a step above the rest" for packaging/box sets
- Warner Archive Collection:  -> premium. CBR: care "just as good as the boutique labels", high-quality Blu-rays
- Olive Films, Twilight Time: premium -> cultural. Paste text describes bare-bones discs; Olive transfers "suffering from scratches and various video noise": boutique standing, not quality
- Cinema Guild, Oscilloscope Laboratories, Cohen Media, Blue Underground, Film Movement, Anchor Bay: premium -> cultural. named only in Paste's closing "also check out" sentence, not picks
- Org Music: DEFER -> keep. = Original Recordings Group, audiophile reissue label (SoundStage)

## Drops: 192 footer/navbox rows (list in AUDIT_F1.json)
