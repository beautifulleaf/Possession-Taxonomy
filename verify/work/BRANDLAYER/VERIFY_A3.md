# VERIFY A3 Jewellery (brand layer)

Opus verifier, 2026-10-31. Input: A3.json (204 harvest brands) minus 11 audit drops, plus 38 audit add_brands = 232 rows; 2 merged (Benney into House of Benney, De Beers London into De Beers Diamond Jewellers) = **230 brand rows**. 21 harvest + 13 audit regions = **34 regions**. Status: complete.

## Method
Every distinct src page was fetched with mcp__Parallel__web_fetch (raw page text: full_content for category pages, the Time Out, AGTA, UKJA 2024, Visit Birmingham and VO+ Valenza pages; for long pages, verbatim excerpt mode keyed to the names, re-fetched in full where a name was missing). Each URL was fetched once for all names citing it. Fetch results were recorded per page in VERIFY_A3_tmp/t*.json and merged into v.json / r.json; build.py writes VERIFY_A3.json.

Tier rules applied: encyclopedia category member or a list row linking to its own article = cultural; museum or collection record = cultural; independent award, test, guild/standard or craft statement = quality; retail-only awards (Store Design, Online Retail Strategy, Supplier) do not count; own website, directory rows (Walpole, Ernest Jones, Crown Perth tenant page, Design Ireland, trade-show catalogue) and editorial rows without a craft/material claim = listed. No row qualified as 'seller' (the Native American makers are makers with a tradition tag; the retailer pages describing them are independent sources).

## Counts
- quality: 97
- cultural: 73
- listed: 60
- seller: 0
- shown false: 0. Three names were NOT on their cited page but were found on a second fetched page (src2): Ecksand (own site; not in the Canada category), Moraglione 1922 (ICE JIS 2019 exhibitor catalogue; not on VO+ Valenza), Smith & Pepper (own en.wikipedia article; defunct 1981; not on Visit Birmingham).
- regions: 34, renown true 17, renown false 17.

## Regions
| region | renown | brands kept (named raw on region src) | note |
|---|---|---|---|
| France: Place Vendôme Paris | no | Cartier, Van Cleef & Arpels, Chaumet | the-cartiers.com raw: Van Cleef & Arpels at 22 Place Vendôme since 1906, Cartier on adjacent rue de la Paix, Chaumet linked; describes the houses but no sentenc |
| Italy: Valenza (Piedmont) | yes | Giorgio Visconti, DI.GO., Damiani | VO+ raw; Moraglione 1922 and Picchiotti not on page; Cartier, Chopard, Bulgari, Rolex named only as brands producing there |
| Italy: Vicenza and Arezzo | yes | - | Picchiotti blog raw (a Valenza brand's page); Fratelli Bovo dropped; no Vicenza/Arezzo maker named. Same page names PICCHIOTTI in Valenza ('best known for fine  |
| India: Jaipur | yes | Raniwala 1881, The House of Rambhajos, The Gem Palace, Tallin Jewels, Sunita Shekhawat, Amrapali, Tribe Amrapali | Vogue India raw |
| Mexico: Taxco | yes | Antonio Pineda, William Spratling | Fowler Museum raw; Los Castillo, Margot de Taxco, Matilde Poulat and Sigi Pineda not seen in the fetched text (not confirmed) |
| USA Southwest: Navajo, Zuni and Hopi | yes | Hopi Silvercraft Cooperative Guild | Museum of Northern Arizona raw. Only the Guild is named on this page; Charles Loloma, Kelly Morgan, Rosabelle Shepherd, Loren Panteah and Yolanda Laate, Jesse J |
| Denmark / Scandinavia | no | Georg Jensen | src is Georg Jensen's own site; own site only |
| Thailand | no | Pacharee, Herkindnco, Pattaraphan, Sarran, Mormormor, Thammada Studio, Ravipa | raw page describes Thai jewellery tradition but does not call Thailand renowned; Kavant & Sharart and Pailin not on page (dropped) |
| UAE / Gulf: Dubai | yes | Samra, Bhaskar Devji Jewellers, La Marquise Jewellery | JCK raw; Vivaa (dropped as wholesaler) and Javeri (not on page) excluded |
| Japan: Toba, Ise-Shima (Mie) | yes | Mikimoto | Japan National Tourism Organization raw: Mikimoto Pearl Island, Toba |
| UK: Birmingham Jewellery Quarter | yes | - | Visit Birmingham raw; names no makers (Smith & Pepper and Harriet Kelsall absent) |
| Ireland: Galway | no | - | src is Thomas Dillon's own site; it claims to be the original Claddagh maker but does not state Galway's renown; own site cannot place a brand in a regional div |
| Niger / Sahara: Agadez (Tuareg) | no | - | src tuaregjewelry.com is the Koumama family's seller site; praises the family, not the region; A l'Atelier not on it |
| Central Asia: Turkmen and Uzbek | no | - | Met essay raw describes Turkmen silver jewellery tradition; no renown sentence and Ogulgerek Myradova not seen in fetched text |
| Australia: northwest coast | no | Paspaley | What's On Melbourne raw: Paspaley 'internationally known as the world’s largest producer of fine South Sea pearls'; renown is the company's, not the region's; L |
| Colombia | no | - | src is Muzo Emerald Colombia's own site ('legendary emerald mine'); own site only |
| South Africa | no | Nina Bosch, Mary Jean Jewellery, Skermunkil, Pina Jewels | Visi raw names the brands as South African but does not say South Africa is renowned for jewellery; Pichulik and Mamabolo also on page |
| Morocco: Tiznit (Amazigh) | yes | - | Slow Morocco raw; no workshop named |
| New Zealand: West Coast (Hokitika) | no | - | src is Moko Pounamu's own site; own site only; Mountain Jade (Rotorua) is not named on it |
| China | no | Lao Feng Xiang | src is Lao Feng Xiang's own US site (filigree named Intangible Cultural Heritage); own site only; Chow Sang Sang not seen |
| South Korea | no | Grace Lee | Who What Wear raw: Grace Lee Seoul-born; no regional renown statement |
| Italy: Torre del Greco (Naples) | yes | Ascione, Antonino De Simone, Falanga Coralli | Napolike raw |
| India: Jaipur (addition to harvest region) | yes | Birdhichand Ghanshyamdas, Surana Jewellers | GIA raw; same region as India: Jaipur (merge) |
| Hawaii | no | Maui Divers Jewelry | src is Maui Divers' own site; own site only; Philip Rickard not on it |
| Ghana: Krobo (Eastern Region) | yes | Cedi Beads | GhanaTRVL raw |
| Peru: Lima and Cusco | no | Graziella Laffi | LACMA raw: Laffi and modern Peruvian silver; no renown sentence found in excerpts; Ilaria not on this page (Indagare page says Ilaria raised the profile of Peru |
| Czechia: Turnov | yes | Granát Turnov | Czech EXPO pavilion partner page (promotional); renown stated for Bohemian garnet, not Turnov by name |
| Russia: Kubachi (Dagestan) | yes | Manaba Magomedova | Moscow Times raw |
| China: heritage gold (gufa huangjin) | yes | Laopu Gold, Chow Tai Fook | Beijing Review raw; renown is of the heritage-gold craft in China |
| Lebanon: Beirut | no | Nada Ghazal | JCK raw names Nada Ghazal in Beirut; no regional renown statement |
| Japan: Kyoto | no | Kazurasei | src is Kazurasei's own site; own site only |
| India: Hupari, Kolhapur | no | Parshwanath Jewellers | src is Parshwanath's own site ('famed across India for silverwork'); own site only |
| Morocco: Amazigh silver (fills harvest's empty Tiznit region) | yes | Amina Agueznay | en.wikipedia raw; renown is historical (Jewish Berber silversmiths emigrated late 1950s) |
| Indonesia: Kotagede (Yogyakarta) | yes | - | en.wikipedia raw; no maker named |

Renown false mostly because the region src is a maker's own site (Galway, Agadez, Colombia, NZ, Hawaii, Denmark, China, Kyoto, Hupari) or the page names brands without a renown sentence (Thailand, South Africa, South Korea, Beirut, Peru, Place Vendôme, Central Asia, Australia NW). Each needs a second independent page to stand as a regional division.

## Flags for merge
- Harvest region lists that failed the raw re-check (removed from region): Valenza: Moraglione 1922, Picchiotti; Taxco: Los Castillo, Margot de Taxco, Matilde Poulat, Sigi Pineda not seen in the fetched text; Birmingham: Smith & Pepper, Harriet Kelsall; Australia NW: Linneys; Hawaii: Philip Rickard; Peru: Ilaria; Central Asia: Ogulgerek Myradova; China: Chow Sang Sang; NZ: Mountain Jade; Southwest: only the Hopi Silvercraft Cooperative Guild is on the museum page (the other 10 makers carry Navajo/Zuni/Hopi tradition tags from their own pages).
- Merge: 'India: Jaipur (addition to harvest region)' into 'India: Jaipur'.
- Fit doubtful (not jewellery makers): Jean Puiforcat (tableware), Grant Macdonald Silversmiths, Thomas Lyte (trophies), Cara Murphy (silverware), Gebelein (hollowware), Burhouse (findings supplier), Gordon Marks (warrant as restorer), Titan Company (group; Tanishq parent).
- Defunct: Smith & Pepper (1981), A l'Atelier (Agadez guild; partners split 1998 per Smithsonian record).
- Source issue: Charles Loloma's harvest src is a Kiwix mirror (wiki.chogus.org), an archive copy that the rules forbid; replaced by his own en.wikipedia article (src2).
- Possible re-add for the audit: Fratelli Bovo (dropped as not on Picchiotti page) appears on the ICE JIS 2019 catalogue as a Trissino (Vicenza) maker, a directory row only.
- Sub-line: Tribe Amrapali is a line of Amrapali.

## Files
- verify/work/BRANDLAYER/VERIFY_A3.json
- verify/work/BRANDLAYER/VERIFY_A3_tmp/ (v.json, r.json, build.py, per-page t*.json)
