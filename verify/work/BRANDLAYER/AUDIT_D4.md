# AUDIT D4 Cameras & Photography (cold audit, BRANDLAYER)

## Accuracy
25 harvested brands sampled (random.seed(7), random.sample); all 9 distinct src pages fetched raw (Parallel web_fetch, full_content). **0/25 wrong**: every name is on its page and every claim is supported. Most claims are only 'listed' / 'has own article', so the check is weak.

- Tessina: shown yes, claim yes
- AstrHori: shown yes, claim yes (in TIPA manufacturer dropdown)
- 3 Legged Thing: shown yes, claim yes (CNET Best all-round tripod, Bucky given CNET Editors Choice)
- Retrospekt: shown yes, claim yes (in brand filter; existence only (seller list, tagged premium though no quality claim))
- Taylor Hobson: shown yes, claim yes
- AXIOM: shown yes, claim yes
- B+W: shown yes, claim yes (in brand filter; existence only)
- Newman-Sinclair: shown yes, claim yes
- Triggertrap: shown yes, claim yes
- Giottos: shown yes, claim yes (in brand filter; existence only)
- Yongnuo: shown yes, claim yes
- PGYTECH: shown yes, claim yes (TIPA 2025 Best Photo Backpack confirmed)
- Folmer and Schwing: shown yes, claim yes (shown; the list links it to the Graflex article, so "own article" is loose (Graflex already known))
- K. G. Corfield: shown yes, claim yes
- Mitchell Camera: shown yes, claim yes
- Negative Supply: shown yes, claim yes (in A-Z list; existence only)
- Candido: shown yes, claim yes (in A-Z list and Most Popular Brands)
- Auricon: shown yes, claim yes
- Silvestri: shown yes, claim yes
- Moviecam: shown yes, claim yes
- Calumet: shown yes, claim yes (in brand filter; existence only)
- Analog Forever: shown yes, claim yes (in A-Z list; existence only)
- Hirox: shown yes, claim yes (shown; but Hirox is a digital-microscope maker, weak D4 relevance)
- Deardorff: shown yes, claim yes (page is the Deardorff brand page itself; existence only)
- Sunpak: shown yes, claim yes (Sunpak flashes subcategory present)

Out of sample: **Metz** is cited to Category:Photographic flashes by brand but is not on that page. It is on the List of photographic equipment makers, so fix the src. **Layer problem**: the 52 Blue Moon names, the 20 Analogue Wonderland names and the TIPA-dropdown names are tagged 'premium' on evidence that only shows they exist; they should be tier 'listed'.

## Drops (11)
- Quantaray: Ritz Camera store house brand (private label, no cultural footprint); evidence is only a seller brand-filter list
- Promaster: distributor private label for accessories; evidence only a seller brand-filter list
- Rokunar: rebadged budget lens/accessory label; seller list only
- Kalimar: importer label for rebadged budget cameras and accessories; seller list only
- Hirox: digital microscope maker; in Wikipedia lens-manufacturer category but no camera-photography footprint (D4 test not met)
- Op/tech: duplicate of known 'Op/Tech USA'
- Franka-Werk: duplicate of 'Franka Kamerawerk' (same Bayreuth maker)
- Candido Collective: duplicate of 'Candido'
- Intrepid Camera Company: duplicate of 'Intrepid Camera' / known 'Intrepid'
- Arsenal: duplicate of 'Kiev-Arsenal' (Zavod Arsenal, Kiev)
- Hewes Products: duplicate of known 'Hewes'

## Additions (84 brands, 5 regions)
### Central & Eastern Europe (Dresden / Saxony)
- **Welta** (cultural; Germany; folding and TLR cameras): Dresden-area camera maker (Welta-Kamera-Werk Freital: Weltaflex, Penti); brand kept within VEB Pentacon; "the heart of the German camera industry lay in Dresden, Jena" [src](https://pixelcraft.photo.blog/2023/09/01/vintage-camera-makers-the-origins-of-pentacon)
- **Altissa** (cultural; Germany; box and 35mm cameras): Altissa-Camera-Werk Berthold Altmann, Dresden (Altissa, Altiflex, Altix cameras) [src](https://pixelcraft.photo.blog/2023/09/01/vintage-camera-makers-the-origins-of-pentacon)
- **Reflekta** (cultural; Germany; TLR cameras): Reflekta-Kamerawerk Tharandt (Reflekta II TLR), part of the Dresden camera industry [src](https://pixelcraft.photo.blog/2023/09/01/vintage-camera-makers-the-origins-of-pentacon)
- **Beier** (cultural; Germany; 35mm compact cameras): Freitaler camera industry Beier & Co. (Beirette cameras), merged into Pentacon 1980 [src](https://pixelcraft.photo.blog/2023/09/01/vintage-camera-makers-the-origins-of-pentacon)
- **Certo** (cultural; Germany; folding cameras): VEB Certo Kamerawerk Dresden, folding cameras [src](https://pixelcraft.photo.blog/2023/09/01/vintage-camera-makers-the-origins-of-pentacon)
- **Mentor** (cultural; Germany; large-format cameras): VEB Mentor Grossformatkamera, Dresden large format cameras; homonym - use "Mentor (Dresden)" [src](https://pixelcraft.photo.blog/2023/09/01/vintage-camera-makers-the-origins-of-pentacon)
- **Ernemann** (cultural; Germany; cameras and cine projectors (historic)): Ernemann camera factory site and Ernemann Tower (Dresden), used as Pentacon logo; Ernemann tower symbol on Praktisix [src](https://pixelcraft.photo.blog/2023/09/01/vintage-camera-makers-the-origins-of-pentacon)
- **Belca** (cultural; Germany; folding cameras): VEB Belca-Werk, Dresden, absorbed into Kamera-Werke Niedersedlitz 1957 (Belfoca cameras) [src](https://pixelcraft.photo.blog/2023/09/01/vintage-camera-makers-the-origins-of-pentacon)
### Central & Eastern Europe (Russia / former USSR)
- **Zenit** (cultural; Russia; 35mm film SLR cameras): Wikipedia list: KMZ (Krasnogorsk) makers of Zenit cameras; Zenit has its own article (Zenit (camera)) [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Zorki** (cultural; Russia; 35mm rangefinder cameras): Wikipedia list: KMZ makers of Zorki cameras (own article) [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Horizon** (cultural; Russia; panoramic film cameras): Wikipedia list: KMZ makers of Horizon (camera) panoramic cameras (own article); homonym, use "Horizon (KMZ)" [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Zenitar** (cultural; Russia; camera lenses): Wikipedia list: KMZ makers of Zenitar lenses (own article) [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **GOMZ** (cultural; Russia; cameras): State Optical-Mechanical Plant, Leningrad (LOMO before 1962); logo on early Lubitel-2, Sport, Reporter cameras [src](http://cameras.alfredklomp.com/logos)
- **Lubitel** (cultural; Russia; twin-lens reflex cameras): GOMZ/LOMO Lubitel twin-lens reflex camera line (Lubitel-2), iconic Soviet TLR [src](http://cameras.alfredklomp.com/logos)
- **Valdai** (cultural; Russia; camera lenses (Helios)): Valdai Optical-Mechanical Factory, prolific producer of Helios SLR lenses for KMZ and Zenit BelOMO [src](http://cameras.alfredklomp.com/logos)
- **Moskva** (cultural; Russia; folding medium-format cameras): KMZ product line (Moskva folding cameras) alongside Zorki, Zenit, Horizon [src](http://cameras.alfredklomp.com/logos)
### East Asia (China)
- **Marelux** (cultural; China; underwater housings): UWPG (seller-linked): aluminium housings tested to the same high standard as other high-end housings [src](https://www.uwphotographyguide.com/best-underwater-camera-housings)
- **Phenix** (cultural; China; 35mm cameras and lenses): Global Times: of China's 1950s-80s camera factories only Seagull (Shanghai) and Phoenix (Jiangxi) survived into the 21st century; Phoenix/Phenix cameras [src](https://www.globaltimes.cn/content/714483.shtml)
- **Kase** (premium; China; filters and filter systems): Amateur Photographer: Kase K9 holder "brilliantly designed", Testbench Gold 5 stars; On Landscape 10-stop ND test: Kase Wolverine "very good", one of only two almost completely neutral [src](https://amateurphotographer.com/round-ups/best-100mm-square-filter-holder-systems-for-landscape-photography)
### East Asia (China/Hong Kong)
- **Nauticam** (premium; Hong Kong; underwater housings): Competitor comparison (Outex): "Nauticam sits at the top of the market, and deservedly so"; Hong Kong CNC-machined aluminium housings; UWPG: "considered to be a top manufacturer of high-end underwater photographic equipment" [src](https://outex.com/blogs/guides/outex-vs-nauticam)
### East Asia (Japan)
- **Casio** (cultural; Japan; compact digital cameras): Wikipedia list (manufacturers of cameras); EISA 2004-2005 Digital Compact Camera award: Casio Exilim Pro EX-P600 (eisa-awards.org/history/photography/photography-2004-2005/); also in TIPA manufacturer list [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Widelux** (cultural; Japan; panoramic film cameras): Wikipedia list: Panon (see Widelux), own article; swing-lens panoramic camera [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Kyocera** (cultural; Japan; film cameras (Contax/Yashica era)): Wikipedia list: former producer of film cameras (own article); TIPA manufacturer list [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Ikegami** (cultural; Japan; broadcast video cameras): Wikipedia list of camera makers: Ikegami (Ikegami Tsushinki, own article) [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **LPL** (cultural; Japan; enlargers and easels): Wikipedia list of darkroom equipment makers: LPL (Japan) photographic enlargers and easels [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **JVC** (cultural; Japan; camcorders): Wikipedia Category:Movie camera manufacturers lists JVC (own article) [src](https://en.wikipedia.org/wiki/Category:Movie_camera_manufacturers)
- **Ebony** (premium; Japan; large-format view cameras): Luminous Landscape: Tokyo workshop of seven hand-building ebony/mahogany and titanium view cameras; "Ebony is the finest wooden field camera ever made" (reseller quote); ceased manufacturing June 2016 [src](https://luminous-landscape.com/era-ends-ebony-view-camera)
- **Tachihara** (premium; Japan; wooden field cameras): Ken Rockwell review: 100% handmade in Tokyo (Tachihara Professional Camera Works) from aged Hokkaido cherrywood; "very well made", woodwork more precise than far pricier cameras [src](https://www.kenrockwell.com/tech/tachihara.htm)
- **Nagaoka** (cultural; Japan; wooden field cameras): Large Format Page 5x7 round-up: Nagaoka 5x7, 3.5 lb, "reasonably well built" ultralight wooden field camera [src](https://largeformatphotography.info/roundup5x7.html)
- **Anba Ikeda** (cultural; Japan; wooden field cameras): Large Format Page 5x7 round-up: Anba Ikeda wooden field camera, similar to the Nagaoka [src](https://largeformatphotography.info/roundup5x7.html)
- **Toyo** (premium; Japan; large-format field and monorail cameras): Large Format Page review of Toyo 45A metal field camera: bash-proof, rigid; Luminous Landscape (2016): Toyo the last maker of plastic film holders; homonym - use "Toyo-View" [src](https://largeformatphotography.info/toyo.html)
- **Toho** (cultural; Japan; large-format cameras): Large Format Page 5x7 round-up: Toho field cameras (4x5 ultralight; also 5x7) [src](https://largeformatphotography.info/roundup5x7.html)
- **Sea & Sea** (cultural; Japan; underwater housings and strobes): UWPG (seller-linked): underwater housings since the early 1970s, solid mid-range to high-end choice; reviewer finds them well built and very reliable [src](https://www.uwphotographyguide.com/best-underwater-camera-housings)
- **Lambda (ラムダ)** (cultural; Japan; camera backpacks): Camera Grand Prix 2024 Camera Journal Press Club award, merit prize (功労賞): ラムダ, Japanese mountain camera-backpack maker (closed 2023) [src](https://ja.wikipedia.org/wiki/%E3%82%AB%E3%83%A1%E3%83%A9%E3%82%B0%E3%83%A9%E3%83%B3%E3%83%97%E3%83%AA)
- **Artisan & Artist** (premium; Japan; camera straps and cases): Finding Range review: materials "of the highest quality", hand stitching very neat, "construction is among the best out there"; Japanese strap and case maker (made in Japan per maker) [src](http://findingrange.com/2015/03/23/artisan-artist-silk-green-wrist-strap-review-for-leica)
- **Marumi** (cultural; Japan; filters): Digital Camera World review (fetched): Marumi "involved in the optics industry for over 85 years", one of the biggest filter ranges; DHG Super Circular PL "very good optically" [src](https://www.digitalcameraworld.com/reviews/marumi-dhg-super-circular-pl-polarizing-filter-review)
- **Nikkor** (cultural; Japan; camera lenses): Wikipedia Category:Photographic lenses by brand: Nikkor (own article); Nikon lens line - sub-brand, merge under Nikon if sub-brands are not listed separately [src](https://en.wikipedia.org/wiki/Category:Photographic_lenses_by_brand)
- **Takumar** (cultural; Japan; camera lenses): Wikipedia Category:Photographic lenses by brand: Takumar (Asahi/Pentax lens line, own article) - sub-brand [src](https://en.wikipedia.org/wiki/Category:Photographic_lenses_by_brand)
- **Rokkor** (cultural; Japan; camera lenses): Wikipedia Category:Photographic lenses by brand: Rokkor (Minolta lens line, own article) - sub-brand [src](https://en.wikipedia.org/wiki/Category:Photographic_lenses_by_brand)
- **Zuiko** (cultural; Japan; camera lenses): Wikipedia Category:Photographic lenses by brand: Zuiko (Olympus lens line, own article) - sub-brand [src](https://en.wikipedia.org/wiki/Category:Photographic_lenses_by_brand)
### East Asia (Taiwan)
- **Plustek** (premium; Taiwan; film scanners): PCMag review: OpticFilm 135i Ai rated 4.0 Excellent (brand page: "combines a top-tier film scanner with one of the top scanning utility apps") [src](https://www.pcmag.com/reviews/plustek-opticfilm-135i-ai)
### Middle East
- **Leaf** (premium; Israel; digital backs): Wikipedia list of camera accessory makers: Leaf (Israeli company), digital backs (own article); TIPA manufacturer list: Leaf America [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
### North America
- **Lytro** (cultural; United States; light-field cameras): Wikipedia list: Lytro, makers of consumer plenoptic (light-field) cameras [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Stereo Realist** (cultural; United States; stereo cameras): Wikipedia list: David White Company (Stereo Realist), own article [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **IMAX** (cultural; Canada; large-format cine cameras): Wikipedia list of camera makers: IMAX (own article) [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Omega** (cultural; United States; enlargers): Wikipedia list of darkroom equipment makers: Omega (USA) photographic enlargers; homonym (watches) - use "Omega enlargers" [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Carestream** (cultural; United States; photographic paper): Wikipedia list: Carestream (USA) manufacture of Kodak RA4 papers (formerly part of Kodak) [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Kino Flo** (premium; United States; film and TV lighting): Wikipedia: 1995 Academy technical achievement award; lights "considered a staple of a standard motion picture lighting package" [src](https://en.wikipedia.org/wiki/Kino_Flo)
- **Mole-Richardson** (cultural; United States; film lighting (Fresnels)): Wikipedia: Hollywood film lighting maker since 1927; invented the Fresnel Solar Spot (1935), four technical Academy Awards; "setting the standard for tungsten Fresnel fixtures"; ceased trading end 2025 [src](https://en.wikipedia.org/wiki/Mole-Richardson)
- **Wisner** (premium; United States; wooden field cameras): Large Format Page round-up: Wisner Traditional, Technical and Pocket Expedition field cameras (geared axis tilt, long bellows); camera-wiki: high-end large format cameras from Marion, Massachusetts [src](https://largeformatphotography.info/roundup5x7.html)
- **Aquatica** (premium; Canada; underwater housings): UWPG (seller-linked): Montreal maker founded 1982, housings milled from solid aluminium, "worldwide reputation as a leader and innovator" [src](https://www.uwphotographyguide.com/best-underwater-camera-housings)
- **ONA** (premium; United States; leather camera bags): Engadget review: brand "specializes in high-end, high-quality bags"; Italian tanned leather, "nothing about the Brixton Leather that isn't top-shelf" [src](https://www.engadget.com/2012-11-24-ona-brixton-leather-review-camera-laptop-messenger-bag.html)
- **Breakthrough Photography** (premium; United States; filters): On Landscape independent 10-stop ND test: X4 Breakthrough rated good, best of the round filters [src](https://www.onlandscape.co.uk/2017/07/nd-filters)
- **ProGrey** (premium; United States; filters): On Landscape 10-stop ND test: ProGrey USA Genesis IR rated very good [src](https://www.onlandscape.co.uk/2017/07/nd-filters)
- **Paul C. Buff** (cultural; United States; studio flash): PetaPixel: "lighting gear pioneer"; Nashville maker of White Lightning (1981), AlienBees, Einstein studio flashes that brought affordable studio flash to photographers and made competitors rethink products [src](https://petapixel.com/2015/03/24/lighting-gear-pioneer-paul-c-buff-passes-away-at-the-age-of-78)
### Northern Europe
- **Vintage Visual** (cultural; Estonia; film): TIPA archive manufacturer list: Vintage Visual Oü (award-winning); Analogue Wonderland film brand list [src](https://www.tipa.com/archive-search)
- **Imacon** (premium; Denmark; film scanners): Luminous Landscape (Michael Reichmann): Imacon Flextight "clearly superior scanner", first-rate build, Rodenstock optics; later sold as Hasselblad Flextight [src](https://luminous-landscape.com/imacon-comparison-2)
### Oceania
- **Crumpler** (cultural; Australia; camera bags): Wikipedia list of camera accessory makers: Crumpler (own article); Melbourne bag maker [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Røde** (premium; Australia; camera microphones): TIPA World Awards archive manufacturer list includes Rode (award-winning manufacturer); camera microphones [src](https://www.tipa.com/archive-search)
- **Miller** (premium; Australia; fluid heads and tripods): Wikipedia: Sydney maker; Robert Eric Miller invented the fluid head for motion picture cameras (patent 1946); joelwsmith: "Miller is THE O.G. ... synonymous with quality camera heads"; note: company announced closure Aug 2026 (CineD/Newsshooter excerpts) [src](https://en.wikipedia.org/wiki/Miller_Camera_Support_Equipment)
### South Asia
- **Vageeswari** (cultural; India; box and folding cameras): Wikipedia list: Vageeswari (Vageeswari Camera, own article) among camera manufacturers; Indian maker [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
### Southeast Asia
- **Champion** (cultural; Malaysia; photographic chemicals): Wikipedia list: Champion (Malaysia) manufacture of photographic chemicals; homonym - use "Champion Photochemistry" [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
### Southern Europe
- **AP Photo Industries** (cultural; Spain; darkroom equipment): Wikipedia list: AP Photo Industries (Spain) darkroom equipment, film cartridges, disposable cameras [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Isotta** (premium; Italy; underwater housings): UWPG (affiliated with Bluewater store; seller-linked, tier listed unless independently supported): family-owned Italian maker since 1967/1980, housings designed, made and tested in Italy, hand-finished CNC aluminium [src](https://www.uwphotographyguide.com/best-underwater-camera-housings)
### Western Europe
- **Hama** (cultural; Germany; camera accessories): Wikipedia list of camera accessory makers: Hama (Hama Photo, own article) [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Calypso** (cultural; France; underwater film camera): Wikipedia list: Atoms (Calypso underwater camera), own article [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Kienzle** (cultural; Germany; enlargers): Wikipedia list of darkroom equipment makers: Kienzle (Germany) photographic enlargers [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Moersch** (cultural; Germany; darkroom chemistry): Wikipedia list: Moersch (Germany) photographic chemicals [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Compard** (cultural; Germany; photographic chemicals): Wikipedia list: Compard (Germany) manufacture/packing of photographic chemicals (ex-Agfa products) [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Inoviscoat** (cultural; Germany; film coating): Wikipedia list: Inoviscoat (Germany) manufactures film components for other brands incl. Impossible Project, ADOX; now part of ORWO [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Hahnemühle** (premium; Germany; fine-art photographic paper): TIPA World Awards archive manufacturer list: Hahnemühle / Hahnemuhle FineArt (award-winning); also on Blue Moon brand list [src](https://www.tipa.com/archive-search)
- **Sachtler** (premium; Germany; fluid heads and video tripods): Best overall fluid heads; "engineered and built so incredibly well, they will last for years (and probably decades)" (26 years of use by reviewer) [src](https://www.joelwsmith.com/best-fluid-heads-video)
- **Seacam** (premium; Austria; underwater housings): Canon Rumors: "My favorite housings are from Seacam ... I have yet to use a housing that does controls better than a Seacam", 80 m rated [src](https://www.canonrumors.com/these-are-our-favourite-underwater-cameras/)
- **Wirgin** (cultural; Germany (not stated on page); 35mm SLR cameras): Wikipedia Category:Cameras by brand has subcategory "Wirgin cameras" (own category) [src](https://en.wikipedia.org/wiki/Category:Cameras_by_brand)
### Western Europe (UK)
- **Ross** (cultural; United Kingdom; camera lenses): Wikipedia list and Category:Lens manufacturers: Ross (optics), London lens maker (own article) [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **De Vere** (cultural; United Kingdom; enlargers): Wikipedia list: De Vere (UK) digital enlargers, previous manufacturer of quality analog photographic enlargers [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **RH Designs** (cultural; United Kingdom; darkroom meters and timers): Wikipedia list: SDS (UK) manufacture of RH Designs exposure meters (darkroom) [src](https://en.wikipedia.org/wiki/List_of_photographic_equipment_makers)
- **Vinten** (premium; United Kingdom; broadcast fluid heads and pedestals): Vinten Vector 750: "the best premium fluid head for live production money can buy" [src](https://www.joelwsmith.com/best-fluid-heads-video)
- **Gandolfi** (cultural; United Kingdom; wooden view cameras): Large Format Page 5x7 round-up: Gandolfi makes 5x7 cameras in a variety of configurations (London wooden camera makers) [src](https://largeformatphotography.info/roundup5x7.html)
- **Formatt-Hitech** (premium; United Kingdom; filters and filter systems): Amateur Photographer: Firecrest 100mm MKII 4.5 stars, "uniquely good for shooting very long exposures"; On Landscape ND test: Firecrest "good" [src](https://amateurphotographer.com/round-ups/best-100mm-square-filter-holder-systems-for-landscape-photography)
- **Lastolite** (premium; United Kingdom; reflectors and backgrounds): Amateur Photographer review: Lastolite Bottletop 120cm reflector kit "about as useful as they come", 5 out of 5 [src](https://amateurphotographer.com/field-tests/accessory_reviews/lastolite-circular-bottletop-reflector-120cm-kit-review)
### unassigned
- **Lotus View** (cultural; not stated on page; wooden field cameras): Large Format Page 5x7 round-up: Lotus view rapid field camera, cherrywood and anodized aluminium [src](https://largeformatphotography.info/roundup5x7.html)
- **Zoomar** (cultural; not stated on page; zoom lenses): Wikipedia Category:Photographic lenses by brand: Zoomar lens (own article) [src](https://en.wikipedia.org/wiki/Category:Photographic_lenses_by_brand)
- **Petie** (cultural; not stated on page; subminiature cameras): Wikipedia Category:Cameras by brand: Petie (own article), subminiature camera brand [src](https://en.wikipedia.org/wiki/Category:Cameras_by_brand)

## Regions
- **Central & Eastern Europe (Dresden / Saxony)**: heart of the German camera industry in Dresden, Jena and surroundings: Zeiss Ikon/Contax, Praktica, Exakta, Pentacon Six, folding and TLR makers merged into VEB Pentacon. Brands: Zeiss Ikon, Contax, Welta, Altissa, Reflekta, Belca, Praktica, Ihagee, Exakta, Meyer Optik Görlitz, Beier, Mentor, Certo, Pentacon, Ernemann [src](https://pixelcraft.photo.blog/2023/09/01/vintage-camera-makers-the-origins-of-pentacon)
- **Central & Eastern Europe (Russia / former USSR)**: Soviet camera and optics factories behind generic product names (Zorki, Zenit, Horizon, Moskva, Lubitel, Smena, Kiev, FED, Helios). Brands: KMZ, Zorki, Zenit, Horizon, Moskva, LOMO, GOMZ, Lubitel, FED, Arsenal, BelOMO, Peleng, LZOS, Valdai [src](http://cameras.alfredklomp.com/logos)
- **East Asia (China: state camera industry and handmade view cameras)**: 1950s-70s state camera factories in Shanghai, Beijing, Nanjing, Tianjin (Seagull TLRs, Dongfeng, Hongqi); survivors Seagull and Phoenix; modern handmade wooden view cameras in Haining (Chamonix) and Shanghai (Shen Hao). Brands: Seagull Camera, Phenix, Chamonix [src](https://www.globaltimes.cn/content/714483.shtml)
- **East Asia (Japan: handmade wooden field cameras)**: small Tokyo workshops hand-building wooden large-format field cameras (Ebony, Tachihara, Nagaoka, Anba Ikeda), alongside metal field cameras (Toyo, Wista, Horseman). Brands: Nagaoka, Anba Ikeda, Tachihara, Ebony, Toyo, Toho, Wista [src](https://largeformatphotography.info/roundup5x7.html)
- **Western Europe (Wetzlar, Germany)**: 'City of Optics': Kellner's Optical Institute (1849) taken over by Ernst Leitz; Barnack's Leica (1914/1924); Hensoldt optics. Brands: Leica [src](https://www.wetzlar.de/microsite/en/business/City-of-Optics.php)

## Notes
Accuracy: 25 sampled with random.seed(7)/random.sample over harvest 'brands'; all 9 distinct src pages re-fetched raw (Parallel web_fetch full_content). 0/25 wrong: every name is on its page and every claim (mostly 'listed'/'own article') is supported. Caveats: Folmer and Schwing links to the Graflex article (not its own); Hirox is a microscope maker (drop). Out-of-sample errors noticed: Metz is cited to Category:Photographic flashes by brand but is NOT on that page (it is on List of photographic equipment makers - fix src). Layer problem: the 52 Blue Moon brand-filter names, the 20 Analogue Wonderland names and the TIPA manufacturer-dropdown names are tagged 'premium' on existence-only seller/dropdown evidence; per SELLER PRAISE they should be tier 'listed' until an independent quality page exists. Several Blue Moon names are private labels (see drop). EISA spot-check: 1991-92 (Culmann 3080) and 2004-05 (Konica Minolta Anti Shake) rows confirmed on the year pages. Thin areas retried: EISA 2013-14, 2014-15, 2016-17, 2017-18, 2019-20, 2020-21, 2021-22 fetched via links on the EISA history index - only mainstream winners (Canon, Nikon, Sony, Fujifilm, Olympus, Panasonic, Sigma, Tamron, Samsung, Manfrotto, GoPro, Laowa, Zeiss) plus non-D4 (Eizo, Huawei, OPPO, DxO, Zoner, CEWE): no new D4 brands. Camera GP Japan: ja.wikipedia winners table fetched - new only Lambda (ラムダ, merit prize 2024); others mainstream. Wikipedia Category:Cameras by brand and Photographic lenses by brand fetched: Wirgin, Petie, Zoomar and lens lines Nikkor/Takumar/Rokkor/Zuiko added. Large format: Ebony, Tachihara, Toyo, Wisner, Gandolfi, Nagaoka, Anba Ikeda, Toho, Lotus View added (Chamonix, Shen Hao, Wista, Canham, Arca Swiss already known). Lighting: Kino Flo, Mole-Richardson, Paul C. Buff, Lastolite added (Profoto, broncolor, Elinchrom, Godox, Hensel known). Enlargers: LPL, Omega, De Vere, Kienzle from the Wikipedia darkroom list (Durst, Beseler, Kaiser known). Not retried: TIPA archive result pages, DPReview Gold Awards (no fetchable list found), instant film (New55/One Instant seen only in excerpts). The Wikipedia List of photographic equipment makers was under-harvested: Zenit, Zorki, Horizon, Zenitar, Casio, Vageeswari, Ross, Crumpler, Hama, Leaf, Lytro, Widelux, Kyocera, Calypso, Stereo Realist, IMAX, Ikegami and the darkroom/chemistry makers were all on the fetched page but missing from all known names. Regions: harvest region brand lists were empty; add_regions gives page-named brands for Dresden/Saxony, the Soviet factories, China, Japanese wooden field cameras and Wetzlar (Wetzlar page fetched excerpt shows only Leica; Kellner/Leitz/Hensoldt text is from the same page's search excerpt). REGIONS ARE NOT QUOTAS: Africa, Latin America, Central Asia and most of the Middle East have no notable makers in this concentrated industry and were not counted as omissions; Leaf (Israel), Vageeswari (India), Champion (Malaysia) are the only additions there. Seller-linked: Isotta, Aquatica, Sea & Sea, Marelux rest on Underwater Photography Guide, which is affiliated with Bluewater Photo store - tier 'listed' unless independently confirmed (Nauticam and Seacam have independent pages). Homonyms flagged: Horizon, Omega, Champion, Mentor, Toyo, Moment, Cactus (Wikipedia link confirms camera-equipment brand), Keystone (Keystone Camera Company), OPL (Optique & Precision de Levallois). Lens-line sub-brands (Nikkor, Takumar, Rokkor, Zuiko) and product lines (Lubitel, Moskva, Zorki, Zenit) may be merged under their makers if the register lists only companies.
