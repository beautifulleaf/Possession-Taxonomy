# GD_EEU3_5 report

123 brands (Eastern Europe, RU). Tied at garment level: 119 brands, 553 maker_kinds rows (verify/out/GD_EEU3_5_maker_kinds.tsv). Not found, no A1 garment form named on the fetched page: 4 (verify/out/GD_EEU3_5_notfound.tsv): Miasskaya Shveynaya Fabrika, NOVA TOUR, Oneself Fabric, PROTEKT.

Method: retailer-style pages first. The listed productcenter.ru roster pages gave each brand's producer URL (fetched pages' own links); each producer page was then fetched. The garment list came from the page's description and product list. Customer questions, OKVED codes and sidebar categories were ignored. Mishka Brend was found by search (productcenter.ru/producers/35996/mishka-briend) and fetched. All fetches are logged in verify/work/GD_EEU3_5/fetched.tsv; every source URL in the output is logged.

Conventions followed from earlier EEU batches: толстовки -> hoodie, жакеты/пиджаки -> blazer, пальто -> overcoat, шапки -> beanie, комбинезон -> jumpsuit, халат -> bathrobe (lab coat for workwear), sports suits -> joggers only (tracksuits are filed by pieces).

Caveats: M-nika matches three different productcenter firms named Nika (fur factory, sportswear Rostov, knitwear Kursk); each row cites the firm it came from. M-mila has two producer pages (1876 and 9298). OPTWILL's producer page is /producers/33787/elizavella (brand ELIZA).
