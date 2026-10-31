# VERIFY B2 Soft Furnishings (brand layer)
Checked 191 brands (harvest 116 minus 1 audit drop, California Design Den, plus 76 audit adds; no duplicate merges were needed, variant spellings recorded as aliases). Raw full-content fetches with mcp__Parallel__web_fetch: all 115 distinct harvest/audit source URLs (BHG and BBC returned empty pages) plus 13 Réseau Excellence 'Entreprise du patrimoine vivant' type-list pages and 3 second pages (fr.wikipedia Tréca, Fair Trade Forum India, Good Market), all saved in VERIFY_B2_tmp/ (batch_*.json, epv*.json, f2.json). The Réseau Excellence linge-de-lit, tisserand and rideaux pages are the audit's same-day raw full-content fetches, copied from AUDIT_B2_tmp/.
## Tiers
- cultural: 27
- listed: 72
- quality: 87
- seller: 5

Not shown: 0. 10 names are not on their harvest src and are shown on a src2: seven names cited to the Réseau Excellence Produits index (it lists only categories), Tréca, Coyuchi (BHG page returned empty) and Sasha (BBC page returned empty).
## Main findings
- **EPV per company.** Réseau Excellence category pages do not state EPV status per company (they show existence and craft domain only). The network's own type filter 'Entreprise du patrimoine vivant' (13 pages, 463 names) does. 27 B2 brand rows are on it and are 'quality' with that page as src2: Beauvillé, Brun de Vian-Tiran, Drouault, La Compagnie Dumas, Jules Pansu, Bonnefoy, Duchénoy, D'Ennery, Lartigue, Moutet, Castex, Literie Bonnet, Norki, Aubusson, Pinton, Piganiol, Fontanille, Artesina, Carlhian, Oriol & Fontanel, Choletaise, Dissidi, Gauthier & Cie, Metzger, Verrier, Atelier Fey, Art de Lys (plus Yves Delorme and Le Jacquard Français, region names only). Not on it: Toiles de Mayenne and Jouffre ('listed', membership only), Blanc des Vosges (own site claims EPV 2011, 'listed'), Tassinari & Chatel ('listed'). Poyet Motte: EPV stated by Le Journal des Entreprises ('quality'). Tréca: EPV stated on its own fr.wikipedia article ('quality').
- **Toiles de Mayenne** src corrected to the Réseau Excellence Tisserand page (also on the Rideaux page); original src kept as src_harvest.
- **Joias** (B2) is the Tortolì, Sardinia rug maker (CDA 2023 Best Studio Artist Design), not the A1 Joias (a Japanese red-letter fashion label). Kept separate, already=false, with its own note; also listed under 'homonyms'.
- **cross_tag** array: Aarong, Jim Thompson, Bombay Dyeing and Marimekko should carry B2 on their existing rows (the B2 rows are also flagged cross_tag: true).
- Check the category for: Piganiol (Aurillac umbrella maker, listed under textile objects), Gauthier & Cie and Metzger (curtain hardware), Kantha Bae (clothing made from kanthas), Nusantara Heritage (mostly clothing).
- Many audit adds rest on the maker's own site and stay 'listed' (Fortuny, Prelle, Bevilacqua, Lelièvre, Kvadrat, Finlayson, Siulas, Linas, Brinkhaus, billerbeck, Graccioza, Kamawanu, Zollanvari, Azerkhalcha, Taç, Özdilek, Bombay Dyeing, Jim Thompson, Aspinwall, Uchino, Beni Rugs, Tibet Rug Company). Upgrades from second pages: Rubelli (Wallpaper* 2026), Jaipur Rugs (CDA 2024), Hossein Rezvani (CDA 2017), Bemz (The Furnished Review), Fe y Lola and Demetrio Bautista Lazo (Monte Albán Heritage Center), Turquoise Mountain (Royal Warrant 2024).
- All rug dealers known only from their own shop sites are 'listed', not 'seller': UNIQ, Rugway, Catalina, Nakkas, Nejad, Nomads Loom, Benihaus, Nazmiyal, Ararat, Rugistan, Aladdin, Al Safi, Yildiz, Nizhoni Ranch Gallery. The 'seller' rows are Aarong, Karika, Kumudini (IIAS), Kantha Bae (AramcoWorld) and Sasha (Fair Trade Forum India).
- CDA finalists and shortlists that never won (Bazar du Sud, TAN, Cadrys, Studio Potato, MUMs, Battilossi, Rug Star, Lila Valadan, Kirkit, Theo Keller, cc-tapis, Deirdre Dyson) are 'listed'.
- Names only mentioned on a parent's article (Le Manach, Manuel Canovas) are 'listed'. Braquenié links to its own article, so it is 'cultural'.

## Regions
Renown true: 16; false: 20. Renown false covers registers, directories, award lists and own sites. Renown true includes origin or tradition statements without the word 'renowned' (Cambodia, Wales, Nara, Bengal/IIAS), following the A2 precedent. The two Bengal entries are merged (AramcoWorld src, IIAS src2). Brands carry a region only when renown is true and the page names them.

- France (Vosges, Lyonnais, Aubusson): renown False; brands 4. Réseau Excellence directory page: lists companies, states no regional renown; Blanc des Vosges, Garnier-Thiebaut, Poyet Motte, Manufacture Royale d'Aubusson, Ateliers Pinton, Tissage Moutet not on this page
- Japan (Imabari, Ehime): renown True ('This symbolizes imabari towel's high quality based on its history and tradition'); brands 0. official Imabari Towel (association) site; Ikeuchi Organic, Kontex, Hotman, Uchino not on page
- United Kingdom: renown False; brands 5. Royal Warrant list is a register, no regional renown; Axminster and Brintons not on 2024 list
- Turkey (Denizli): renown True ('A large amount of these bath towels are produced in the western Denizli province town of Buldan'); brands 0. Daily Sabah/Anadolu (production-centre statement); Veritas, Nomads Loom, Nakkas Rug, Nejad Rugs not on page (the three rug dealers do not belong in a towel region)
- Portugal/Egypt: renown False; brands 1. retailer brand page; no regional renown
- Switzerland: renown False; brands 1. The International Man directory; no renown; Schlossberg not found on page
- India / Pakistan: renown False; brands 0. category page of companies; states no regional renown; Mughal Carpet Company not on page
- New Zealand: renown False; brands 0. category page; no renown statement
- Tibet/China: renown False; brands 0. category page; no renown statement
- Iran and Azerbaijan: renown True ('Countries such as Turkey, Iran, India, and Pakistan ... are well known for their woven carpets'); brands 0. en.wikipedia Carpet; Catalina Rug, UNIQ Rugs, Rugway not on page
- Scotland: renown False; brands 1. register; no renown statement
- Turkey (Hereke, Anatolia): renown True ('These handcrafted pieces quickly became symbols of prestige and artistic excellence'); brands 1. Türkiye Today on Hereke factory carpets; Nomads Loom, Nakkas Rug, Nejad Rugs not on page
- Iran (Tabriz, Kashan, Isfahan): renown True ('Tabriz rugs are known for their wide range of patterns, precise knotting, and crisp designs'); brands 1. dealer's own page (UNIQ Rugs); Catalina Rug and Rugway not on page
- Morocco: renown False; brands 1. Beni Rugs' own site; no independent renown page; Benihaus not on page
- Navajo Nation, USA: renown True ('Mr. Hubbell encouraged weavers to create high quality rugs and tapestries that became famous world-wide'); brands 1. NPS; Nizhoni Ranch Gallery and Pendleton not on page
- Mexico (Oaxaca): renown True ('Traditional natural dyes are what made Teotitlán famous'); brands 3. Monte Albán Heritage Center
- West and Central Africa / Netherlands: renown False; brands 1. Jessica Hemmings essay: Vlisco has made wax-resist cloth since 1846 for African markets; brand history, no regional renown
- Uzbekistan (Margilan): renown True ('The city of Margilan has been known for its silk since the 10th century'); brands 0. Textile Research Centre Leiden
- Cambodia / Southeast Asia: renown True ('Silk has a long history in Cambodia'); brands 1. Entomology Today (tradition statement, no "renowned" wording); covers Cambodia only
- Wales: renown True ('tapestry blankets are traditionally given as wedding presents in Wales'); brands 4. From Britain with Love guide (tradition statement, no "renowned" wording); Trefriw named as Trefriw Woollen Mill
- Sweden: renown False; brands 1. FJØRN retailer page; no renown; Nordic Knots not on page
- Nepal / Tibet: renown False; brands 1. Tibet Rug Company's own site; Lhasa Carpet Factory not on page
- Ukraine: renown False; brands 1. award winners list; no regional renown
- Australia / New Zealand: renown False; brands 1. award list; no renown; Bremworth and Godfrey Hirst not on page
- Caucasus, Central Asia and Afghanistan: renown True ('Uzbekistan textiles are best known for bold, symbolic embroidery and luminous silk cloth'); brands 1. dealer's own page and covers Uzbekistan only; Ararat Rugs, Rugistan, Aladdin Rugs, Al Safi Rug House, Yildiz Rugs not on page
- Bengal (Bangladesh and West Bengal): renown True ('The quilts are deeply tied to the cultural and historical identity of Bengal in South Asia'); brands 5. AramcoWorld | src2: IIAS (origin/tradition statement, no "renowned" wording); Sasha and House of Wandering Silk not on page
- Indonesia: renown False; brands 1. seller's own site; La Tazha not on page
- Iran: renown False; brands 1. Aria Carpet's own about page
- Kerala (Alleppey/Alappuzha), India: renown False; brands 1. Aspinwall's own site; 'renowned' applies to coir fibre, not Kerala; William Goodacre & Sons and The Alleppey Company not on page
- Caucasus (Azerbaijan, Armenia): renown True ('In November 2010, Azerbaijani carpets were included in UNESCO's Representative List of Intangible Cultural Heritage'); brands 1. Azerkhalcha's own (state company) page states the UNESCO listing; Megerian Carpet, Artsakh Carpets, Tufenkian not on this page (they are on the CivilNet Armenian-carpet article)
- Venice and Lyon: renown False; brands 1. Bevilacqua's own site; no regional renown statement; Rubelli, Fortuny, Prelle, Tassinari & Chatel not on page
- Isfahan and Fars, Iran: renown True ('Isfahani carpets are renowned for their high quality'); brands 1. en.wikipedia Isfahan rug; Zollanvari and Hossein Rezvani not on page
- Lithuania: renown False; brands 1. Linas' own site; Siulas not on page
- Nara, Japan: renown True ('Nara Sarashi originated in the Kamakura Period (1185–1333)'); brands 1. Henokiens member page (origin statement)
- Kyrgyzstan (Naryn, Kochkor): renown True ('Perhaps best known are shyrdak, or ornate felt rugs'); brands 1. Smithsonian Folklife Festival
- Mali (Segou, Djenne): renown False; brands 2. Rubia partners page: supports bogolan production in Djenne and Segou; no renown statement
