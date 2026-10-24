# DPW1_J5 report (J5 Pantry Staples; offline Opus pass, wave 3)

Inputs: the COMMON and W3_ADD reading lists, TREE_J5 and its map, HV_J5_1–3 reports and fetch logs, DPMK_1_J5_kinds.tsv, and the J5 rows in data/ (174 kinds, 178 named forms, 0 lines).

## Task 1: missing kinds (13 candidates)
DPMK_1 already decided all 51 "missing kind?" items in the harvest reports, so they are skipped here. The 13 candidates below come from the shop categories in the fetch-log "gave" column and from named forms that are really generic types.
- **new_kind 0.**
- **covered 7:**
  - sushi rice and black glutinous rice → J5.1.1.04 and J5.1.1.07
  - idli rava → J5.1.4.09
  - potato and sweet-potato vermicelli → J5.2.5.01
  - Pastina and Wide egg noodles → J5.2.1.04 and J5.2.2.01 (these named forms only restate their kinds)
  - coconut chips → J5.4.2.01
- **attribute 5:** parboiled rice, fresh pasta (`storage_state`), Juwari soba (the buckwheat share), kachi ghani pressing, silken tofu (firmness).
- **named_form 1:** kombu and dashima under J5.10.1.02 Dried seaweed.
- **other_category 0.**

Still open (no candidate row): dried fruit. The Agranel shop has a "frutas deshidratadas" category, but the fetch log names no fruit type. J5.10.1 still needs its dried-fruit kinds from an HV_J5_NK or depth batch (R-59 c).

## Task 2: named forms (10 of 178 flagged)
- **drop 4:**
  - Pastina: restates its kind.
  - Wide egg noodles: the width is a size attribute.
  - Juwari soba: the tree makes the buckwheat share an attribute.
  - Pasta di Gragnano IGP: it spans three pasta kinds, so it is a designation tag, not a named form (JC1).
- **move_kind 2:**
  - Black Thai (purple sticky) rice → J5.1.1.07 Glutinous, because the rice key tests glutinous first.
  - Baby basmati (Kala Jeera) → J5.1.1.04 Medium- and short-grain. "Baby basmati" is the shop's wording (R-64). †
- **to_line 4** (maker-role "none": a range is a line, not a branded product; R-9, R-18):
  - L-fermentis-dry-yeast
  - L-wyeast-liquid-yeast
  - L-white-labs-liquid-yeast
  - L-briess-malt-extract
  Each covers one kind (J5.11.1.05 or J5.11.1.03).
- **Notes for the maker or polish pass, no move:**
  - "Whole grain thin spaghetti" should be renamed "Thin spaghetti".
  - "Medium shells" carries a size word.
  - Garbanzo de Escacena PGI and Longkou vermicelli rest only on nav-list pages.

## Task 3: navigation
I confirm R-116's way in: **type of object, as the shop aisle groups it**, then quality. The harvested data supports this:
- There are no J5 scene tags.
- 130 maker-bound named forms belong to 116 makers. Most brands appear once (Caputo has the most, with 4), so a brand-first page would be a flat list of single products.
- Every fetched shop page is an aisle or product page (Stop & Shop, Ocado, Weee, King Arthur, Northern Brewer).
- The depth that buyers compare sits inside a kind: protected names, cultivars, JAS types, ISO and UMF grades.

Olive oil and balsamic keep their side entry by ranked producer (proposals.tsv).

View sketch:
1. **Which aisle?** G-J5-1 to G-J5-9:
   - Oils, fats & vinegars
   - Rice, pasta, grains & pulses
   - Flour, sugar & baking
   - Spices, salt & stocks
   - Sauces & condiments
   - Tins, jars & preserves
   - Nuts, seeds & dried fruit
   - Honey, syrups & spreads
   - Tofu & meat alternatives

   Side entries: protected names, award winners, heritage foods, by tradition.
2. **Which product group?** The level-2 groups G-J5-10 to G-J5-34. Examples: Olive oil apart from other oils; Rice; Pasta & noodles; Pulses; Soy sauce & ferments; Table sauces.
3. **Which product?** A kind page shows "What makes the best" (markers.tsv) and "Who vouches", then named forms: protected names and cultivars first, then branded products (C7).

## Rules applied
C2(a), (b), (d); C3; C11; JC1; JC4; R-9; R-18; R-58; R-59 c; R-64; R-115 b; R-116; tree keys for rice, soba and tofu.

## Resting on † claims
- That Kalajeera is a short-grain non-basmati rice comes from general knowledge.
- Reading kombu and dashima as dried-seaweed named forms rests on a blog-shop page.

No new kind ids were issued, so nothing waits for an HV_NK attestation from this pass.
