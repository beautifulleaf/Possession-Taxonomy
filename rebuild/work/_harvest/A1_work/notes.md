# A1 harvest notes
Entries kept in entries.tsv (n, seg-code, kf, c, f, srckey, d); srcmap.tsv maps keys to URLs; build.py writes A1.json.
## Sources tried
- Wikipedia List of denim jeans brands: fetched OK
- FashionUnited /brands: JS-rendered, only 10 names visible; not used
- SSENSE/Farfetch/MR PORTER/END A-Z: no index page found by search
- Wikipedia Category:Clothing brands + by-country: fetched OK
- Wikipedia country categories (US x2 pages, UK, IT, FR, JP, AU, CA, DE, IN, SE, NL, ES, KR, TR, DK, PK, BR, CN, UA, TW, MX, RU, HK, BE, CO, LK, PH, RS): fetched OK
- Wikipedia High fashion brands (3 pages), Haute couture, Sportswear brands (pages 1-2), Outdoor clothing brands: fetched OK
- Wikipedia Category: Underwear, Lingerie, Hosiery, Swimwear, Surfwear, Children's clothing brands, Fashion labels from India, Skateboarding companies; Template Clothing companies of Pakistan; articles Savile Row, Streetwear, Lolita fashion, Gothic fashion, Cyber goth, Ura-Harajuku; Lists of swimwear / lingerie brands: fetched OK
- Category:Streetwear_brands, Category:Workwear_brands: 404 (do not exist)
- Wikipedia Workwear article: no usable brands
- Denim Hunters Japanese denim guide, Heddels Japanese denim guide + tag page: fetched OK
- FashionUnited /brands retried via Firecrawl (coordinator fallback): still only 10 names (JS-rendered) - not used
- Rawr Denim, Vogue Runway index, Good On You directory, SSENSE/Farfetch/MR PORTER/END A-Z: no index page found via search; not fetched
- Knowledge batches: e_13 (Japanese/streetwear), e_14 (workwear/bespoke/hats), e_15 (traditional/subculture)
- Removed name collisions with other-domain register entries (Topper, Generation, Torani, Silhouette, Invicta, Oxbow); renamed Fox->Fox Racing, Morgan->Morgan de Toi, Zodiac->Zodiac Clothing
- Wikidata SPARQL not run (category coverage sufficed)
