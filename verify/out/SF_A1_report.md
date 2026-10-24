# SF_A1 report (storefront check, clothing makers)

Worklist 160 makers; all 160 decided in verify/out/SF_A1_decisions.tsv.

- own-label: 78
- storefront: 10 (Dyco, Giglio, Claudio Antonioli, L&T, Mytheresa, OneStopPlus, Rent the Runway, RushOrderTees, Spread Group, Yoox Net-A-Porter)
- unclear: 72

Notes:
- Most storefront and unclear rows are fetch_status partial: the fetched page was silent on whether goods are own-label. Only the 10 storefront rows rest on a page showing multi-brand or platform resale.
- 13 unclear rows have no page at all (search found nothing usable; none fetched). 9 more are fetch failures (403/404) and are logged as failed in verify/work/SF_A1/fetched.tsv.
- Several own-label rows are partial (inferred from a manufacturer or brand description, or a company-wide private-brand statement for Bon-Ton and Stage Stores nameplates).
- Fetch log: verify/work/SF_A1/fetched.tsv. Nothing written to data/.
