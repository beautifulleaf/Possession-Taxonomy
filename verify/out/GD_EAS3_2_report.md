# GD_EAS3_2 report

Tied at garment level: 43 of 110 brands, 111 rows (verify/out/GD_EAS3_2_maker_kinds.tsv). Not found: 67 (verify/out/GD_EAS3_2_notfound.tsv). Fetch log: verify/work/GD_EAS3_2/fetched.tsv (86 fetches; failed ones are logged as failed and used by no row).

Most ties came from 10pinping, cnpp, maigoo and baiqiang category-ranking pages, whose brand entries list products. Others came from Reviewed.com (Halara), Canadian Cyclist (Jakroo), Winshang and Jiemian (Himalaya, Mobi Garden) and a FruitsFamily brand page (JIGOTT).

Points to check at load:
- GRC row is partial (smzdm post snippet).
- Jieniu: the page entry has slug jienius (Jienius).
- Laoweishi: the page entry is Lao Wei Shi.
- Guuuse Armor: matched by its Chinese name only.
- JIGOTT is listed as CN but the resale page is the Korean brand.
- Jakroo, GRC and Halara jerseys and other sport-specific garments were left out because cycling jerseys belong to E2.
- Brands whose pages name only uniforms, Tang or Zhongshan suits, or dance wear are not mapped where no A1 kind covers them.

Not found: mostly fashion-week designer labels (bjd.com.cn and Winshang roster pages), Toutiao women's-wear group brands, fire-equipment makers and brands whose entries are misattributed (Haoyi Beibei is baby bottles, Mo Lang is earphones, Liyu is shoe covers).
