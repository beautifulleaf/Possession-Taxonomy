# GD_EEU3_6 report

Scope: 123 Russian clothing brands. Source: productcenter.ru producer and product pages found through WebSearch or linked from fetched pages. Every fetched URL is logged in verify/work/GD_EEU3_6/fetched.tsv (124 fetches, all full).

- Brands tied at garment level: 111 (the original list has 123; all others are in the notfound file).
- Rows written: 377 in verify/out/GD_EEU3_6_maker_kinds.tsv.
- Not found / no A1 garment kind: 12 in verify/out/GD_EEU3_6_notfound.tsv:
  Ritter Brand (branded uniform only), Rossiyanka, SeViZe (PVC zip pullers), Sherstyanaya Strana (wool belts, home shoes), Chayka holding (fishing suit, bags), Slavteks (fabrics), Sportsolo (ski suits), SShEY MNOGO, Renessans, Syn Polka, Sleduet Shit, Stil-YuNITE.

Judgement calls to check:
- Rows whose notes say "(описание)" come from the company description text on the fetched page, not from a product card.
- SELFD: the page brand is SELFDOM (roster name SELFD, likely cut at the macron).
- Work, welder, medical and guard suits are written as work jacket A1.4.1.17 plus work pants A1.2.2.03 (medical suits as scrub top A1.1.1.05 plus A1.2.2.03).
- Sports suits and tracksuits are mapped to co-ord set A1.3.1.10.
- Pukhovik (down jackets) is mapped to puffer jacket A1.4.1.14 (SAPA long quilted jackets: puffer coat A1.4.2.04).
- Several maker entities show liquidation dates on productcenter.ru (RusCotton, Sanger, SangerStyle, SIFUR, Sinyaya Ptitsa, SFM.MODA, SeViZe); the garment evidence is still from the fetched pages.
