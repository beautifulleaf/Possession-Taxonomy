# AUDIT J3 Dairy, Eggs & Alternatives (cold audit + retry round, 2026-10-31)

**Accuracy:** 6 wrong of 25 (24%), seed 7. All six are wrong-src: the name is real but sits on a sibling page.
- Boxcarr, James Ranch and Montchevre cite the wrong Good Food Awards year.
- CP-Meiji, Jesa Farm Dairy and Mlekara Subotica cite the Australia category page.

The fault is systemic:
- 37 of 74 Good Food Awards rows point to the wrong year page.
- 19 rows from other countries cite the Australia category.

`fix_src` in AUDIT_J3.json gives a fetched page that names each of them.

**Additions:** 290 brands, 8 regions.
- 92 are premium. They come from these juried competitions and tests:
  - ICDA 2025
  - Global Cheese Awards 2025
  - ACS 2024–25
  - British Cheese Awards 2012–2024
  - Mondial du Fromage and WCA (Minas Gerais)
  - America's Test Kitchen feta
  - Go Dairy Free plant cheese
  - Sporked eggs
  - National Natto competition
  - Royal Warrant
  - MOF title
- 198 are cultural:
  - Wikipedia articles and category members in 41 country categories and the brand categories
  - PDO member lists: Mozzarella di Bufala, Beaufort, Comté
  - market reports for Nigeria, Morocco, Tunisia, China and Russia
  - the qymyz festival
  - Paris cheese shops, recorded as sellers

The 8 regions:
- Comté AOP
- Beaufort AOP
- Mozzarella di Bufala Campana DOP
- Feta PDO
- Queijo Minas artesanal
- queso menonita (Chihuahua)
- Mito natto
- Kazakh qymyz

**Drops:** Grido Helado (ice cream, J8) and Whisps (cheese snack).

**Homonyms:** most harvest flags are wrong. Only Clover Industries clashes with a register brand (Clover, C4). Unflag these: Big M, Dare, Pauls, Pura, Krishna, Vita, Him, Vijaya and Britannia. Britannia is the same group as the biscuit maker, so cross-tag it. Merge Magnolia SMC with Magnolia (Philippine company), merge Les Fromages du Moulin with Rodolphe Le Meunier, and merge 11 duplicate pairs.

**Baby milks** belong to J3 (they are in the kinds file). Ten formula brands were added. Aptamil, HiPP, Holle, Kendamil and Bobbie still have no fetched independent page.

**Blind spots:**
- Great Taste dairy
- Manchego DOP and Feta PDO producer registers
- named makers of airag, kurt, smen, jben and labneh
- tempeh and Japanese tofu-shop makers
- Latin American majors: Conaprole, Colanta, Gloria, Itambé
- Maeil, Al Rawabi, Taanayel, Turkish İçim/Torku, Soummam, Candia

The names in the last two groups were seen only in search excerpts.

Full detail is in AUDIT_J3.json (`notes`, `fix_src`, `homonyms`, `merge`). The raw fetches are in AUDIT_J3_tmp/raw/.
