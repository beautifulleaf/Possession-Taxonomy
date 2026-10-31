# VERIFY E3 Musical Instruments & Music Gear (Opus verifier)

Status: complete. Built by script from the raw saved pages in E3_tmp/ and AUDIT_E3_tmp/pages/ plus 57 pages fetched in this pass (VERIFY_E3_tmp/pages/, index.json; raw tool outputs in VERIFY_E3_tmp/raw/). Scripts: VERIFY_E3_tmp/stage1.py (shown + own-article link check), build.py (audit application, tiers, homonyms), final.py (regions, outputs).

## Counts

- Brands verified: 1619 (harvest 1497, audit additions 112, verifier homonym rows 10)
- By tier: cultural 978, listed 434, quality 205, seller 2
- Not shown on any fetched page: 1 (Felipe Conde: not on the Zavaleta page; listed only)
- Homonym rows (qualified names, homonym:true): 23; cross_tag (same company already in the register): 20
- Dropped: 256; merged as aliases: 125; moved to D3: 5 (MOVES_E3.json)
- Regions: 29, with renown quote 15, without 14

## Audit applied
- 357 audit drops: junk/navbox rows, church/concert-hall organ builders (172), museum-only makers (14), composer-builders (6), measurement/broadcast/software/holding companies; the 121 duplicate rows were merged as aliases (into a row here, or into the register name: Yamaha, Roland, Gibson, Taylor, Steinway & Sons, Martin, PRS, ...). Organ-builder merges whose target was itself dropped keep the alias only.
- installation_only (10: L-Acoustics, d&b audiotechnik, Meyer Sound, K-array, Renkus-Heinz, EAW, MTR, Ashly, Scully, MCI) dropped. Verifier also dropped "D&b audiotechnik" (second spelling, Music equipment category) and TOA Corporation (building PA/intercom). Kept: QSC (category member; its article shows its amps began as guitar amps for musicians, no portable-PA line named on the page), RCF (Wikipedia lists "ART 3/4/7/9 - Portable Speakers", "EVOX - Column Array Portable Speakers"); Bose cross-tagged to E3 from Wikipedia: "The Bose L1 is a range of portable line array loudspeaker systems for musicians".
- Lakeside Piano Company -> listed; the 251 audit 'listed' rows -> listed, except 28 category rows where the raw category page links the name to its own article (Bill Asher, Fishman, Glen, ATC, Dbx, ...): kept cultural (audit name-matching missed "(guitar maker)"-style titles).
- src_fix: 155 rows on the parent by-country category: 90 mapped by the audit, 64 of the 65 unmapped matched on the 14 country pages fetched here (Germany, Austria, Czech Republic, Finland, Hungary, Belgium, Japan, Italy, Brazil, China, Canada, Australia, France, Denmark); Beijing HsingHai is on the China page as "Beiijing HsingHai Musical Instruments Corporation". No row was left without a naming subcategory (organ builders among them were then dropped).
- not_on_src_page (3): all three are on their pages after all (eight-tones lists "Shanghai Dunhuang"; shakuhachi society has "Nick Hoko Bellando" and "Shugetsu (Seizan) Yamaguchi").
- Moves to D3 (Dynaco, Voice of Music, Cerwin-Vega, Fujikon, Lafayette) written fully verified to MOVES_E3.json under "D3" (Lafayette is already in D2 as Lafayette Radio Electronics).
- Kept organ makers (audit "pending a page"): Estey, Kimball, Wurlitzer, Link (also reed/home organs, pianos) stay; Positive Organ Co, Hope-Jones, Mander, Kenneth Tickell, Barton, Geneva, Kilgen, Marr and Colton, Robert Morton dropped: the List of pipe organ builders row shows nothing a person owns (church or cinema organs).
- Audit additions: 123 added (11 same-company masked brands went to cross_tag instead of rows); Dobner Michele (Consorzio) merged into Michele Giovanni Dobner (Triennale 2024).

## Tier rules used
- Wikipedia category member or list row whose link goes to the brand's own article -> cultural (has_article true). List rows that are redlinks, plain text, external links, or link to another article (John Addison -> Lincolnshire bagpipes, Audiovox -> Paul Tutmarc, Currier -> Timothy Gilbert) -> listed. ENSCHU and WISTARIA link to their own Japanese Wikipedia articles -> cultural.
- Competition and award pages (Triennale Cremona, VSA, Mittenwald, TEC, MIPA, Sangeet Natak Akademi) -> quality; Consorzio Liutai A. Stradivari members -> quality (guild trademark with regulations and a control committee); Craftsmanship Magazine Paracho masters -> quality.
- Museum exhibits/collections (Birthplace of Country Music Museum, Berea College collection), heritage registers (Turkish Living Human Treasures, Fukuyama koto designated craft), GI holders (Miraj) and Sahapedia -> cultural.
- Retailer pages (Zavaleta, Musician's Mall, eight-tones, Ethnic Musical, Landtom, Sound of Asia, Charango Mall, Tapadum, Guitar Salon, charango.it), makers' own sites, and directories (pipers.ie, shakuhachi society, alphorns.com, miz workshop directory, ODP, JANM supplier list) -> listed. Kyoto koto shops Kanazen Gakki and Asano Gakki -> seller.
- Independent expert/press praise of craft -> quality (Hemen & Co in The Hindu; Homer Ledford, Kentucky Historical Society marker "a master craftsman"; Kaneko (Govt of Japan); djembe top-ten picks; tabla makers with craft statements; Kotoden; Fujii Koto; Adrian Villanueva). Wula Drum -> listed (the guide's author stocks it). Tin-whistle "prominent makers" named in Wikipedia without own articles -> listed.

## Homonyms (decided from fetched pages)
- Different company, new qualified row: Bogner (amplifiers) vs Bogner ski wear; Eden (bass amplifiers); Matchless (amplifiers) vs motorcycles; Paxman (horns) vs engines; Rico (reeds) vs yarn; Zimmermann (piano) vs fashion; Crescent (cymbals) vs wrenches; Ajax (drums) vs cleaner; Westfield (guitars) vs kit cars; Jeffries (concertinas) vs saddlery; John Addison (bagpipes) vs globes; Midas (mixing consoles, Wikipedia) vs shoes; Wittner (metronomes), Hering (harmonicas), Kala (ukuleles), Shires (trombones), Peterson (tuners), MSA (pedal steel guitars), Prim (strings), Sela (cajons), Aguilar (bass amplifiers) from own sites or a seller page -> listed. King Piano Co. and Ludwig & Co. flagged homonym (different firms from King brass / Ludwig drums, names already distinct).
- Same company -> cross_tag (not rows): Boosey & Hawkes (Wikipedia: "Until 2003, it was also a major manufacturer of brass, string and woodwind" instruments), Genelec, Tannoy, ADAM Audio, Amphion, PMC, PreSonus, Steinberg, Lexicon, Harrison Consoles, Studer, Bose (L1). Harvest rows that match D3-only register names (Westone, Milbert, Austrian Audio, Forsythe, Manley, ATC, Merging, Lipinski) are the same companies: kept unflagged in brands and also listed in cross_tag (in_brands true) so the merge adds E3.
- Watch list checked: Pearl (E3 drums; Pearl iZUMi is A1; Pearl Flutes kept as its own category member), Yamaha (all long forms merged into Yamaha; Yamaha Motor untouched), Roland, Korg, Gibson, Taylor, Steinway, Hohner (variants merged), Martin (C. F. Martin & Company merged into Martin; Martin Committee is a trumpet model, alias of Martin Band Instrument Company), Ludwig (Ludwig-Musser merged into Ludwig), Premier (Premier Percussion: no register clash). Tula microphones: no page found, not added. Akai: register already has Akai Professional in E3.

## Regions

| region | renown | quote / reason | brands kept | not shown |
|---|---|---|---|---|
| Mexico (Paracho, Michoacan) | yes | Why Paracho has been called the "guitar center of the world" is immediately clear. | 4 |  |
| Italy (Cremona) | no | the Consortium's own promotional site cannot establish regional renown; Cremona's renown is carried by the UNESCO region entry | 2 | Giuseppe Guarneri del Gesù, Filippo Anselmi, Massimo Ardoli |
| India (Miraj, Maharashtra) | yes | specially constructed by the legendary sitar-makers of Sitarmaker Galli | 1 |  |
| Japan (taiko) | no | taiko group history page: names makers but states no regional renown for taiko making | 3 | Miyoshi Daiko, Kato Taiko |
| Middle East (Syria, Egypt, Iraq, Turkey: oud) | no | specialist retailer page; describes where the oud is played, not a renowned making region | 4 |  |
| China (erhu, guzheng, pipa) | yes | The three most esteemed centres of erhu making are Beijing, Shanghai, and Suzhou. | 0 | Shanghai Dunhuang National Musical Instruments Factory, Caorong, Zhang Lian Jun, Huqiu |
| Ireland (uilleann pipes) | no | Na Piobairi Uilleann pipemaker directory: existence only, no renown statement | 8 |  |
| Switzerland (alphorn) | no | alphorn maker directory: no renown statement | 5 |  |
| Scotland (Highland bagpipes) | no | List of bagpipe makers: rows only, no statement that the region is renowned | 5 |  |
| Indonesia (Java: Wirun, Sukoharjo) | yes | famous as the center of gamelan production since a long time ago | 1 |  |
| Bolivia (Aiquile, Cochabamba) | yes | Aiquile has been the world's production capital for this instrument | 2 | Clarken Orosco, Mauro Nunez |
| Trinidad and Tobago (steelpan) | yes | In 1992, the steelpan was declared Trinidad and Tobago's national instrument | 4 |  |
| West Africa (Mandé: Gambia, Mali, Senegal) | no | Wikipedia Kora: no renown statement for a making region | 1 |  |
| Germany (pianos, organs, mics) | no | Wikipedia category page: names firms only, no renown statement | 4 | Klais Orgelbau, Walcker Orgelbau, Schoeps, Microtech Gefell |
| Australia (didgeridoo) | no | Open Directory category: existence only | 3 |  |
| Spain (Granada and Madrid) | no | retailer (Guitar Salon) workshop page: seller text, not independent renown | 5 | Manuel Contreras, Marcelino López Nieto |
| India (Kolkata) | no | Musician's Mall seller guide: praises shops, not independent regional renown | 4 | Hemen & Co |
| Turkey (Istanbul) | no | Akademie Solitude essay tells the story of Istanbul cymbal making but states no renown in so many words | 4 | Bosphorus Cymbals |
| Germany (Markneukirchen, Mittenwald) | yes | Nominierung des Vogtländischen Instrumentenbaus in Markneukirchen und Umgebung in das bundesweite Verzeichnis für das Immaterielle Kulturerbe | 1 | Ficker, Heberlein, Roth |
| United States (Appalachia) | yes | The craftsmanship and artistry of our region's stringed instrument makers are celebrated | 2 | Homer Ledford, Warren May, Appalachian School of Luthiery |
| Canada | no | VSA results blog: Canadian makers won medals; no regional renown statement | 3 |  |
| Japan (Fukuyama, Hiroshima): koto | yes | this instrument exudes the best of handmade craftsmanship | 1 | Fujii Koto Manufacturing |
| India (Kolkata, Mumbai/Pune, Delhi): tabla | yes | Calcutta / Kolkata ... also happens to produce extremely high quality tabla | 6 |  |
| Italy (Castelfidardo, Marche): accordions | yes | Castelfidardo, Italy is the preeminent center of accordion manufacture. | 9 |  |
| India (Miraj): sitar and tanpura - GI 2024 | yes | Miraj, a small town in Maharashtra's Sangli district known for its craftsmanship in making musical instruments | 2 | Faridsaheb Sitarmaker |
| Italy (Cremona): UNESCO intangible heritage | yes | Cremonese violin craftsmanship is highly renowned for its traditional process of fashioning and restoring violins | 52 |  |
| Germany (Markneukirchen, Vogtland Musikwinkel): current workshops | yes | Nominierung des Vogtländischen Instrumentenbaus in Markneukirchen und Umgebung in das bundesweite Verzeichnis für das Immaterielle Kulturerbe | 21 |  |
| Germany (Mittenwald): violin making | yes | The violins made in Mittenwald were instruments of great international renown | 1 |  |
| Italy (Naples, Rome): mandolins | no | a restorer's own site listing Neapolitan makers; no independent renown statement | 3 |  |

Regions are not quotas: no region was added to fill a gap. Cremona's harvest entry rests on the Consortium's own site (no renown); the UNESCO entry carries the renown and the 53 Consortium members. The Erhu entry keeps no brands (none of its four makers is named on the Wikipedia page).

## Open items for the coordinator
- Paulino Bernabe (guitar list) sits beside Paulino Bernabe Senior and II; left as is (father and son are distinct makers).
- Estey, Kimball, Wurlitzer, Link kept without a page showing home instruments.
- The register's 'King' entry carries both J8 and E3 (crisps and brass): worth a look at merge time.
