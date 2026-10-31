# VERIFY C4 Craft & Art Supplies

Raw fetch (mcp__Parallel__web_fetch, full_content) of all 100 distinct harvest/audit source URLs, plus the EPV CSV resource linked from the data.gouv dataset page and src2 pages (LoveCrafts GB A-Z, YarnSub, Needles and Things kit index, Kashoen, Cass Art Turner page, Toyo Co.). Pages in VERIFY_C4_tmp/pages/ (index.json maps URL to file). Blocked or empty: zoomjapan.info (bot check), nytimes.com (paywall, headline only), dw.com (excerpt mode only: Prym paragraph read).

Brands checked: 342 (harvest 289 minus 5 audit drops present in the harvest (Kagzi India, Talens, Golden, Princeton, Roberson) and 5 merged duplicate rows, plus 61 audit adds, plus Royal Talens and Golden Artist Colors created as merge targets). Not shown: 0. By tier: {"cultural": 38, "listed": 259, "quality": 41, "seller": 4}. Homonyms: 1. Regions: 28 (10 with renown).

## Tier rules applied
- cultural: Wikipedia category members; Wikipedia list rows only when the row links to the brand's own article (Łucznik, Tikkakoski, Patons and Baldwins); own Wikipedia article (Uroboros, Ueba Esou, Fevicol); Google Arts & Culture exhibit (Salim Kagzi); Kogei Japan representative maker of a designated traditional craft (Houkodou); press/independent pages treating the brand as an icon (Camel/Camlin, Prym, Citadel, Craftool, Barry King, Toika, Army Painter, Turbodork).
- quality: EPV state label (all 25 French rows confirmed in the data.gouv EPV CSV, src2); Handprint independent watercolour reviews (Blockx, Lukas, Maimeri, Royal Talens, Robert Doak); paint tests and reviews (Basecoat Lab, Spikey Bits, IPMS/USA, Ellen Wilberg); China Daily (Jinding craftsmanship); WIPO (Taew Thai Silk); Handwoven 1981 editorial (Leclerc); Italy Segreta (Amatruda); University of Alabama (Taller Santos Rojas).
- seller: Margilan Crafts Development Center, Fausto Santos, Batik Tulis Abimanyu, The Batik Library (pages name them as sellers of the traditional item).
- listed: every directory row (Jackson's, Jerry's, Cass Art, Clay-King, Wawak, Sewing Machines Plus, LoveCrafts, Wool Warehouse, Blick, Hobbylinc, SGAA, Crystal Valley, Art Shed, Ingebretsen's, TALAS), own websites, shop blogs (seller praise: Happibee, MaggieFrames, Whipstitch, Creative Glass Guild, Woolly Thistle, Cass Art brand page), forums (Modelers Alliance, FineScale), list rows without own article (Necchi, Riccar, Baby Lock to parent article only, Royal Warrant rows Hewit, Joel & Son, A.S. Handover).

## Audit items applied
- Dropped: Kagzi India (src names only the Kagzi community). Lion Capital, Newell Brands, ACCO Brands are not in the harvest (see index cleanup).
- Merged: Talens -> Royal Talens (new row, Cass Art "Talens"; Handprint quality); Golden -> Golden Artist Colors (new row, listed); Princeton -> Princeton Brush (alias); Roberson -> C Roberson (alias). Also merged: Chroma -> Chroma Australia, Coates -> Coates English Willow (Coates willow charcoal), Matisse (Derivan) -> Derivan, Das -> Das Clays, Khadi -> Khadi Papers, Patons -> Patons and Baldwins.
- 27 LoveCrafts yarn brands (resource_needed): the LoveCrafts US page shows only 11 brands now. src2 = Wool Warehouse yarn menu where it names them (WYS, Scheepjes, Rico, Patons, Bernat, King Cole, Stylecraft, Hayfield, James C. Brett), else YarnSub yarn database (yarnsub.com/yarns names all 27; the LoveCrafts GB A-Z also names most). All listed; none left unshown. Viking of Norway alias Viking Garn.
- Cass Art, Jackson's, Jerry's, Clay-King, Wawak, Sewing Machines Plus rows: listed; only Handprint-reviewed watercolour brands upgraded (Blockx, Lukas, Maimeri, Royal Talens). Of the ~15 Handprint brands, the others (Art Spectrum, Daniel Smith, Da Vinci, Holbein, Kremer, M. Graham, Old Holland, Schmincke, Sennelier, White Nights, W&N) are not C4 harvest rows; Utrecht is also reviewed but stays cultural (Wikipedia category).
- Happibee = seller praise: Mr. Hobby and AMMO listed; AK Interactive quality (src2 Basecoat Lab); Citadel cultural (src2 Basecoat Lab).
- "Turner" renamed Turner Colour Works (alias Turner): the Cass Art Turner page says "Based in Osaka Japan for over 70 years", so it is the Japanese paint maker; listed (seller praise only). No homonym in the register.
- Bothy Threads and Vervaco are not on the Wool Warehouse yarn menu; src2 Needles and Things kit-brand index.
- Kashoen: NYT page paywalled; src2 its own site, which places it in Kumano (Hiroshima), not Nara; listed. Toyo (glass cutters): SGAA names it only inside a toyoglasscutter.com link; src2 Toyo Co., Ltd. product page; listed.
- Audit adds re-tiered by rule: own-site only -> listed (J&FJ Baker, Appletons, Bohin, COSMO, Coates, Somerset Willow Growers, Glimåkra (Handwoven item is an advert), Kromski, Nabertherm, Bailey, Novita, Isager, Tassotti, Stockmar, Red Heart (owner press release), Lindström, Durston, Swanstrom, Fire Mountain Gems, Nakagawa Gofun); shop blog -> listed (Sandnes Garn); forum -> listed (Testors); Shetland.org naming only -> listed (Jamieson & Smith, Uradale, Aister Oo, Laxdale Yarn, Langsoond).

## Homonyms
- Riccar (sewing machines): Japanese sewing-machine maker; the register's Riccar (B6) is the US vacuum brand, a different company.
- Same company, unflagged: Ghana Textiles Printing (GTP) = GTP wax-print cloth in A1 (merge adds C4).

## Regions
| Region | Renown | Quote | Brands kept | Removed (not on page) |
|---|---|---|---|---|
| France | no | EPV register (data.gouv CSV): no renown statement | Établissements Bullier (Léonard pinceaux), Chassis France, Société des Ocres de France, Le Moulin à Couleurs, Bergère de France, Dentelles André Laude, Beauvillain Davoine, Sophie Hallette, Société Choletaise de Fabrication, Blanchard Franges, Carlhian, AJBiais, Sin-Rejac, Satab, Neyret, Declercq Passementiers, Passementerie Michel Sahuc, Effet Passementeries, Julien Faure, Fontanille, Ardelaine, Toulemonde Père et Fils, Janvier Gruson Prat, Artamin, Clayrton's, Usine Gallia, Corderie Palus, Girault | Sennelier, Canson, Clairefontaine, Conté à Paris, Lefranc & Bourgeois |
| Japan | no | zoomjapan.info returned a bot-check page only; no brand or renown could be read |  | Chikuhodo, Kuretake, Holbein, Kobaien, Kuroki |
| China | yes | The Huzhou writing brush, Hui ink, Xuan paper and Duan ink stone are "four treasures of study". | Jinding (Suzhou Huzhou Writing Brush Plant) |  |
| West Africa | no | Wikipedia: wax prints are "a type of common material for clothing in West Africa" (use, not renown) | Vlisco, Uniwax, Woodin, Ghana Textiles Printing (GTP), Akosombo Textiles Limited, Printex, ABC Wax |  |
| Norway / Iceland (Nordic) | no | retailer page | Rauma Ullvarefabrikk, Ístex |  |
| Czech Republic (Jablonec / Bohemian Paradise) | no | tourism directory; no renown statement for the bead speciality | Preciosa, Perlex, JSB Bijoux, Atlas Bijoux, Salansky & Co, Arcon Bijoux, Miyuki |  |
| United States | no | SGAA supplier directory | Bullseye Glass, Kokomo Opalescent Glass, Paul Wissmach Glass, Youghiogheny Opalescent Glass | Uroboros Glass, Spectrum Glass, Oceanside Glasstile |
| Peru / Andes | no | Grupo Inca own site | Incalpaca, Inca Tops, Amano Yarns, Pacomarca | Michell |
| Uruguay | no | malabrigo own site (says Uruguay has one of the biggest wool supplies; not renown for the speciality) | Malabrigo | Manos del Uruguay |
| India (Rajasthan, Sanganer) | yes | Jaipur lays claim to being the largest center of hand papermaking in India. |  | Salim Kagzi, Hussain Kagzi, Kagzi India, Khadi Papers |
| Nepal / Bhutan | no | Khadi Papers own site | Khadi Papers |  |
| Japan (Kumano, Hiroshima) | yes | Kumano is renowned for its government-designated traditional craft calligraphy brushes | Houkodou | Shougetsudo, Hiroshima Artist Brush Manufacturing, Hakuhodo, Chikuhodo |
| Japan (Tokushima) | no | Awagami own site | Awagami |  |
| Italy (Marche, Florence) | no | Fedrigoni press release: renown stated for the Fabriano brand, not the region | Fabriano | Zecchi |
| Australia / Oceania | no | retailer list | Derivan, Matisse (Derivan), Jo Sonja's, Art Spectrum, Blackwattle, Helmar, Chromacryl | Chroma Australia |
| Thailand | yes | By the 1960s, Thai silk had become world renowned | Jim Thompson | Taew Thai Silk |
| Uzbekistan (Fergana Valley, Margilan) | yes | The city, which today has a population of around 200,000, has long been synonymous with silk. | Yodgorlik Silk Factory | Khan Atlas Silk Factory, Margilan Crafts Center |
| Turkey | yes | Ebru, Turkish art of marbling (UNESCO Intangible Cultural Heritage Representative List) |  |  |
| Germany | no | forum thread | Harder & Steenbeck | Gutermann, Mettler |
| Spain / Japan / UK | no | shop blog (Happibee) | AK Interactive, Mr. Hobby (GSI Creos), AMMO by Mig Jimenez, Vallejo, Tamiya | Citadel |
| United Kingdom (Scotland) | no | Hewit own site; claim is about the company | J Hewit & Sons |  |
| San Pablito, Pahuatlán (Puebla, Mexico) | yes | una antigua técnica de fabricación de papel aún próspera, al punto de ser la marca de la localidad | Taller Santos Rojas, Fausto Santos (San Pablito amate) |  |
| Sheridan, Wyoming (USA) | yes | mention "Sheridan style tooling," the leatherworkers will most likely know you are talking about a particular style | Barry King Tools, Craftool Co. |  |
| Somerset Levels (England) | no | Coates own site | Coates English Willow | Somerset Willow Growers |
| Kyoto (Japan) | no | Wikipedia Ueba Esou: headquarters only, no regional renown | Ueba Esou (上羽絵惣) | COSMO (Lecien) |
| Amalfi (Campania, Italy) | yes | Formerly a hotspot of the papermaking craft, Amalfi was hit by a devastating flood in 1954 | Cartiera Amatruda |  |
| Shetland (Scotland) | yes | there is a long and bright future for Shetland's famous textiles industry | Jamieson & Smith (Shetland Wool Brokers), Uradale, Aister Oo, Laxdale Yarn, Langsoond, Jamieson's of Shetland |  |
| Giriloyo / Yogyakarta (Java, Indonesia) | no | workshop own blog | Batik Tulis Abimanyu (Giriloyo) |  |

Notes: France is the EPV register (no renown statement); Japan (zoomjapan) could not be read; Thailand renown rests on the Jim Thompson own site; San Pablito renown comes from the Xinhua page (src2) since the UA page states only continuity; Laxdale Yarn is named by Shetland.org as a mainland commission spinner of Shetland wool.

## Index cleanup (for the coordinator)
Corporate owners tagged as C4 brands in rebuild/reader/_brand_index.json, not in the C4 harvest and not added here: **Lion Capital**, **Newell Brands**, **ACCO Brands**. Demote to `rel` owner notes on their brands per PLAN.md INDEX CLEANUP.
