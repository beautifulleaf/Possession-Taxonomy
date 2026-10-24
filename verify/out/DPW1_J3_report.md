# DPW1_J3 report (J3 Dairy, Eggs & Alternatives; offline Opus decision pass)

Inputs: BRIEF, CONVENTIONS_v1, memo J3, D4 R-items, TREE_J3, HV_J3_1 report, J3 rows in data/ (69 kinds, 109 named forms, 2 lines).

## Task 1: missing kinds (19 candidates after splitting)
new_kind 14, attribute 2, named_form 3, covered 0, other_category 0.

New kinds (R-58, next free number under the parent):
- J3.2.1.07 Dairy coffee creamer; J3.2.1.08 Clotted cream; J3.2.1.09 Aerosol whipped cream
- J3.3.08 Soured milk (mesophilic cultured milk)
- J3.4.1.06 Ricotta; J3.4.1.07 Mascarpone; J3.4.2.02 Halloumi; J3.4.3.03 Provolone
- J3.4.6.05 Edam; J3.4.6.06 Manchego; J3.4.7.03 Gruyère; J3.4.7.04 Hard cooked-pressed cheese (Comté)
- J3.4.9.03 Blue cheese (generic); J3.4.9.04 Blue cheese (Roquefort)

Attributes: cooking cream (a use label: the fat tier decides single or whipping cream); chèvre (milk species). Named forms: filmjölk and viili under J3.3.08; matzoon stays under yoghurt.

Precedence to add to the tree: in Yoghurt and fermented milks, mesophilic soured milk is tested after kumys and before plain drinking yoghurt. Plain cream sold for coffee goes by its fat tier; a formulated creamer is J3.2.1.07.

## Task 2: named forms (6 flagged of 109)
- drop 4: Ciliegine (size); Borhani (flavoured drink, OUT by K-56); Buffalo curd and Yak butter (the names give only the milk species, which is an attribute).
- move_kind 2: Chaas and Yayık ayranı go to J3.1.05 Buttermilk (the liquid left after churning).
- to_line 0. The two existing lines (Carnation, HiPP Combiotik) are correct.
- Notes for the maker pass (no move needed): Keens, Pitchfork, Wookey Hole, Seriously Strong and Davidstow Cheddar are brands. They should be maker_bound = yes with makers. St Mang Limburger lacks a maker_id. Kaltbach is an Emmi line that spans several kinds.

## Task 3: navigation, by shopper path
Reasons from the data:
- No scene tags exist, and the memo asserts none.
- Only 36 of 236 makers carry a named form (53 maker-bound). About 200 makers are tied only at category level, so a brand-first page would be mostly empty brands.
- The depth sits under varieties: 27 protected names and 29 traditional names.
- Every retailer opens by product family. The cheese specialist opens by Soft, Hard or Blue.

View sketch:
1. **What are you buying?** Milk; Cream & butter; Yoghurt & fermented milks; Cheese; Eggs; Baby milks & milk powders; Dairy-free alternatives. Side entries are generated views: Lactose- and dairy-free; Goat, sheep & buffalo; Protected names by country; By tradition.
2. **Which type?** For example, Cheese splits into Fresh & soft (fresh/whey, bloomy, washed), Stretched & brined, Semi-hard, Hard, Blue, Processed, Dried dairy and Selection boxes. Milk splits into cow; goat, sheep & buffalo; buttermilk; evaporated, condensed & dulce de leche. Eggs split into hen; duck & quail; preserved.
3. **Which variety or product?** Kind pages have filters (fat, age, species, organic, farming code). Named forms are listed with protected names first, then makers' products (C7).

## Rules applied
- Rule P (1) and (3), and C11
- C2(a)–(c), C3, C6
- JC4
- K-49 and memo 9.7 (creamers), K-56, J-7
- The first-yes cheese key and the tree's species precedence
- R-58, R-96(c)

## Decisions resting on † claims
- **Roquefort and Comté:** their kind level is provisional until sellers in two regions are attested, as for Stilton (C11).
- **Halloumi, Gruyère and Manchego:** I assumed they are sold generically outside their protected areas. Either way they are kinds.
- **J3.3.08 Soured milk:** attested only by a Wikipedia list. A seller page is needed before entry.
- **Matzoon's culture:** not attested.
- **Blue cheese (generic):** the source is a cheese.com catalogue page.
- **Chaas and yayık ayranı:** read as churned buttermilks.

Flag: a generic blue-cheese kind weakens the C11 "no generic kind covers its form" basis for the Stilton, Gorgonzola and Roquefort kinds. Their Rule P(3) test (no sibling sold under the name) still holds, so I left them as they are.
