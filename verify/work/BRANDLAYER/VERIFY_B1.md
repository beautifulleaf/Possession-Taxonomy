# VERIFY B1 (Furniture & Storage), brand layer

Checked 533 brands: 397 from the harvest, minus 3 audit drops (Le Klint, Lambert & Fils, Colebrook Bosson Saunders), plus 144 audit additions, minus 6 merges. Every source page was fetched raw once (Parallel web_fetch, full_content) on 2026-10-31; pages are in VERIFY_B1_tmp/pages/ (index.json maps URL to file). Built by VERIFY_B1_tmp/build.py.

## Tiers
- cultural: 227
- listed: 165
- quality: 140
- seller: 1

## Not shown: 0
Every name is on its source page or on a src2 page.

## Re-sourced (src2): 35
- 12 Living Edge names no longer on the coat-stand page (BassamFellows, Bethan Gray, Bower Studios, La Chance, Caon, Derlot, Figueras, Howe, Limited Edition, The Wood Room, ZETR, Elite To Be) point to the Living Edge brand index (livingedge.com.au/brands); still listed (retailer).
- DENMARK-DESIGN: the 9 directory names now cite the maker's own article on the site (audit relayer). AP Stolen (Danish Furniture Makers' Control label), Bovirke ("reliable hub for high-quality production") and Johannes Hansen ("one of the leading Danish cabinetmaking workshops", precise production, Guild exhibitions) are quality; Andreas Tuck, E. Kold Christensen, France & Daverkosen, Ry Møbler, Planmøbler and Salesco (a sales cooperative, not a maker) state history only and are listed.
- Carolina Furniture six (Hickory Chair, Henredon, Kindel, Sherrill, Hancock and Moore, Henkel-Harris) cite Home News Now (High Point trade press) as src2 and stay quality; the other Carolina names are listed.
- Ducduc (Boston Magazine, 'Built to Last') and Oeuf NYC (TheRoundup test) cite independent pages and stay quality; the other 12 Hart names are listed.
- Legare Furniture and Murphy Door were not on the fetched category pages; each has its own English Wikipedia article (fetched), so cultural.
- Matt Sleeps: AD.nl returned a privacy gate; PlusOnline (Consumentenbond test, 'beste uit de test') fetched instead.
- Les Sièges d'Argentat: EPV list row reads D'ARGENTAT; the Nouvelle-Aquitaine EPV page confirms the label (renewed 2022). Alias D'Argentat.
- Nikari: the Condé Nast page is cut off after the photo caption; Fiskars Village page (Pro Finlandia Medal, highest-quality wooden furniture) used.
- Simon James Design and Resident: NZ Herald text is paywalled; named on resident.co.nz (own company site), so listed.
- Names printed in another script or form are aliases: Japanese makers on Murauchi, Yamagishi, Interiorshop and Praemio (匠工芸, 飛騨産業, 柏木工, 日進木工, 起立木工, 冨士ファニチア, モリタインテリア工業, カリモク, モリシゲ, キタニ, ADコア, 秋田木工, アカセ木工, マスターウォール, 浜本工芸, 高野木工, 綾野製作所, 小島工芸), 추용호 (Chu Yong-ho), Bydgoskie Fabryki Mebli, F.A.N., Makin, Nakata, Century, Sherrill.

## Merges
- Bernhardt -> Bernhardt Design
- Kashiwa -> Kashiwa Mokko
- Nissin -> Nissin Mokko
- Tonon -> Tonon & C.
- Takumi Kohgei -> Takumi Kogei
- Conde House -> Condehouse

## Relayer applied (audit)
- Retailer and directory lists are not quality evidence on their own: Living Edge, Nest, DWR, Hart (except Ducduc, Oeuf), Daniel House, Carolina Furniture (except the six), Comosum, Green Matters, Sleepworks, Casa Carigar, Ngala, Murauchi, Yamagishi, Interiorshop, Ookkuu, Praemio, Vermont Woods Studios, Nordic Nest, furniture.directory, Archello (brand-written profiles), 3daysofdesign exhibitor blurbs, own sites (Etel, Resident). Such names are 'listed' unless another fetched page (Wikipedia category, award, EPV, test) supports them; those upgrades are recorded in note and also_on (e.g. Lafuma Mobilier, Roset, Atelier d'Offard via EPV; Bernhardt Design via Red Dot; Caimi Brevetti and Hida Sangyo via Compasso d'Oro; Hanssem via Category:Furniture companies; Douglas & Douglas via House & Garden SA).
- Resol, Jardan, Savvy Rest, Ethnicraft, Humanscale, Varier: sustainability pages (Comosum, Green Matters) do not count; no other fetched page supports them, so all six are listed.
- False upgrade matches rejected by hand: Cane-line (sidebar link on a German Design Award page), Fursys (award belongs to iloom), AD Core, Paola Lenti (lifetime award to the person), Limited Edition and Case Furniture (common phrases), Koala (only 'tested' by CHOICE).

## Tier rules applied
- quality: Red Dot ranking, Compasso d'Oro, Stiftung Warentest, The Bump test, EPV label, Homo Faber, AIDA award list, Salone 60-year craftsmanship tribute, CHOICE, Consumer Reports, Consumentenbond, German Design Award, iF, Good Design, The English Home, Interior Daily, House & Garden SA, WIPO, Gentleman's Journal, Nippon.com, Kogei Standard, Highlighting Japan, Euronews, Advantour, WCVB, Wallpaper*, ICI, Bourg-en-Bresse magazine, IG Siège de Liffol body (Henryot), Home News Now, and press lines quoted in notes.
- cultural: Wikipedia category members (any language; has_article true), own Wikipedia articles, Encyclopedia.com (Longaberger), Royal Warrant, Italian Marchi Storici register, INPI IG operator list, Korean intangible-heritage holders (Kim Chun-sik, Chu Yong-ho, So Byung-jin, Park Jong-deok).
- seller: Hohodang (Korea Herald: contemporary soban sold at Hohodang).
- listed: retailer, directory, own-site and business-press pages without a quality statement.

## Regions (30: renown 6, no renown 24)
- Denmark / Nordic countries: renown=False; brands kept 10; dropped (not on region page) 10. Wikipedia style article; describes Danish modern but states no regional renown in words.
- Nordic countries (Finland, Norway, Sweden): renown=False; brands kept 0; dropped (not on region page) 13. Wikipedia style article; "golden age of Scandinavian design" but no renown statement for furniture-making regions.
- Italy: renown=False; brands kept 0; dropped (not on region page) 24. it.wikipedia article on the Pesaro district: history only; none of the listed brands (Cassina, B&B Italia...) is named on it.
- Japan: renown=True; brands kept 11; dropped (not on region page) 8. Quote: "日本の６大家具産地 (Japan's six great furniture-producing areas)". Retailer column (Murauchi).
- Germany / Austria / Switzerland: renown=False; brands kept 16; dropped (not on region page) 4. Category page.
- France / Belgium: renown=False; brands kept 8; dropped (not on region page) 8. EPV list; no regional renown.
- United Kingdom: renown=False; brands kept 1; dropped (not on region page) 7. Royal Warrant page for Hypnos only; reputation is the company's, not the region's.
- Netherlands: renown=False; brands kept 6; dropped (not on region page) 1. Category page.
- United States / Canada: renown=False; brands kept 4; dropped (not on region page) 12. Retailer top-brands list.
- South Asia (India): renown=False; brands kept 4; dropped (not on region page) 2. Retailer blog on Indian craft clusters; describes clusters, no renown statement.
- East Asia (South Korea): renown=False; brands kept 2. Press feature on one company.
- East Asia (China): renown=False; brands kept 1; dropped (not on region page) 3. Award gallery.
- Southeast Asia: renown=False; brands kept 1; dropped (not on region page) 3. Gloster's own about page.
- Oceania: renown=False; brands kept 2; dropped (not on region page) 1. Category page.
- Central and Eastern Europe: renown=False; brands kept 5; dropped (not on region page) 3. Category page.
- Middle East (Turkey, Lebanon): renown=False; brands kept 4. Category page.
- Sub-Saharan Africa: renown=False; brands kept 6; dropped (not on region page) 9. Award body list of designers; acclaim is for designers, not a region.
- North Africa: renown=False; brands kept 4; dropped (not on region page) 2. Homo Faber ambassador page.
- Latin America & Caribbean: renown=False; brands kept 0; dropped (not on region page) 6. MoMA exhibition page (Latin American design 1940-1980): museum survey, no renown statement; none of the region brands named.
- East Asia (Japan): renown=True; brands kept 1; dropped (not on region page) 8. Quote: "craftsmen known as "Hida no Takumi (Masters of Hida)"". Regional tourism page (Central Japan).
- Southern Europe (Italy): renown=False; brands kept 9. Heritage marks register; no regional statement.
- Western Europe (United Kingdom): renown=False; brands kept 6. Royal Warrant list.
- Central Asia: renown=True; brands kept 0. Quote: "Khiva masters are renowned for the scaly texture of their carving". No named makers on the page.
- Korea: soban centres (Naju, Tongyeong, Haeju): renown=True; brands kept 3. Quote: "were known for their distinctive designs and high-quality production"
- Uzbekistan: Khiva (Khorezm) and Fergana woodcarving schools: renown=True; brands kept 1; dropped (not on region page) 1. Quote: "considered one of the most refined and expressive"
- Italy: Brianza furniture district (Meda, Cantù, Mariano Comense): renown=False; brands kept 8. Salone tribute PDF names Brianza firms; no statement that the district is renowned ("birthplace" wording not in the raw text).
- France: Liffol-le-Grand seat-making basin (Vosges, Haute-Marne, Meuse): renown=False; brands kept 4; dropped (not on region page) 2. INPI geographical-indication record (protected designation, operator list); the page states no renown in words.
- Mexico: Zacoalco de Torres (Jalisco) equipal chairs: renown=True; brands kept 1. Quote: "nationally and internationally renowned for the crafting of equipales"
- Philippines: Cebu rattan and natural-fibre furniture: renown=False; brands kept 1. WIPO article on one designer; Cebu not named in raw text.
- Japan: byōbu folding screens (Kyoto, Tokyo, Kamo): renown=False; brands kept 1; dropped (not on region page) 3. Article on one Tokyo workshop; no regional renown statement.
