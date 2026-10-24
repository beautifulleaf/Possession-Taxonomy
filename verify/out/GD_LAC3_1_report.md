# GD_LAC3_1 report

Brands tied at garment level: 113 of 145. Rows written: 459 (28 with fetch_status partial: maker-level or inferred ties, noted in the notes column). Not found: 32 brands, listed in GD_LAC3_1_notfound.tsv.

Method: retailer-first step was the directoriodefabricas.com category pages (27 fetched), which name garments for some brands and link brand sites. I then fetched brand sites and directory profile pages. Every source in the output is logged in verify/work/GD_LAC3_1/fetched.tsv (about 150 fetches, including failures).

Caveats:
- Group-level ties (partial): Gino Ferretti, Romesy, Vittorio Manzini (Macarsa), Angelo Perucci, High Society, Jean Miro (Camisas Haber's), Fratelos, Klopman Designes, Men Lova (ISCO), Tall and Cachet (Swantex).
- Jeans inferred from "vaquero": Aventurero SNB, Tucson SNB.
- Generic Spanish "campera/chamarra" mapped to A1.4.1.22 (casual jacket). "Buzo/sudadera" mapped to sweatshirt. "Chaleco" mapped to waistcoat only where the shop menu named it formal.
- Blocked or failed: Instagram (429), Facebook (login wall), Lider.cl and Mercado Libre (bot or 403), Palacio de Hierro (403), canela-601.cl (503), diltexbrands.com (521).
