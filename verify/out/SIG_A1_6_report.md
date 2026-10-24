# SIG_A1_6 report (resumed run)

List rows: 125 houses, all now accounted for.

Rows already in the output when this run resumed: Fast Retailing (1), Fashion Box (3), Hanes Australasia (1), plus lines for Horace Small, Greiff and Felina.

Named forms added this run (13): Fox River Mills, Original Rockford Red Heel Monkey Sock (A1.5.2.01); Gas Jeans, Albert, Sax, Britty Up, Star, Beth (A1.2.1.01); Hejco, Kevin (A1.4.1.15), Kody (A1.2.2.07), Henrik (A1.1.2.02). Output holds 14 named-form rows in total, 8 lines rows (unchanged).

None found: every other house is in verify/work/SIG_A1_6/done.tsv. Most were obscure Finnish, Swedish or German firms with no findable page, or companies whose fetched pages showed only seasonal items, licensed brands or company history.

Problems:
- The Uniqlo page (NF-A1.4.1.14-S6001) returned 503 on every fetch this run, so its source is not in fetched.tsv and the row will be dropped at load unless the domain recovers.
- Several pages refused (403): FHB, Figaret, Fristads.
- Gul Steamer wetsuit and Code Zero drysuit fit no A1 kind (wetsuit and drysuit have no leaf); no page was fetched.
- Gas Jeans fit names come from one trade article that lists them as iconic fits without describing them.
- Hejco models come from retail listings that do not state years.
