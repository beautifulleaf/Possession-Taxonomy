# AU4 cold audit, round 7

Votes A B C; full sentences and definitions in AU4.tsv.

**Q0165 bowling bag (A4 A4 E2). Key: A4.** S3/A4 note: only a bag made to carry one sport object is E2; test as made. "Originally" leaves current use unstated. **Cause: definition.** New definition: "A structured handbag ... styled after the bags once made to carry a bowling ball but not made to hold one."

**Q0355 tricycle (G1 G1 E1). Key: E1 if made for a child, G1 if made for an adult.** Step 11 note: "children's tricycles ... are E1; adult tricycles are G1". The definition does not say who rides it. **Cause: definition.** Split it into *children's tricycle* (E1) and *adult tricycle* (G1). (Cut is by user; if it recurs, extend the 435 mm saddle cut.)

**R0069 integrated dishwasher (B5 B5 B6). Key: B5.** The first branch names "dishwashers", and installation is a modifier. **Cause: placer.**

**R0080 season ticket (I3 I3 F5). Key: I3.** Branch (d) covers "season tickets and passes ... valid for a period". **Cause: key.** The I3 note uses "pass" for both the entitlement and the F5 carrier.

**R0242 kite (E1 E1 E2). Key: E1.** It is made for play (step 25). The key never says what a "sport kite" is, so the definition's single string cannot decide. **Cause: key.**

**T0081 ten-class yoga card (I3 I3 F5). Key: I3, matching the gold.** Branch (d) covers passes valid for "a number of visits". The definition says "prepaid card", and the key files a card as F5. **Cause: definition.** New definition: "A prepaid right to ten classes at one yoga studio, held on a card, in an app or on the studio's account."

**T0036 jar of bolognese sauce (J5 J5 J5). Key: J5.** Step 3 note: "pasta and cooking sauces in jars, with or without meat, are sauces (J5)". The gold, OUT, predates the v0.5 food line. **Cause: gold.**

## Key changes for v0.7.3

1. Step 5 I3 note. Old: "The entitlement (a pass, membership or season right) is filed here whatever its form; the physical card or pass issued to carry it is F5 whether live, used or expired."
   New: "The entitlement (a membership, season ticket, or pass valid for a period or a number of visits) is filed here whatever it is held on (card, paper or app), and an item named or defined by that right is the entitlement; only a kind defined as the physical card or ticket itself is F5, whether live, used or expired."
2. Step 25 note. Old: "a regulation ball or a sport kite in a child's size stays E2."
   New: "a regulation ball or a sport kite (steered on two or more lines, or a traction or power kite) in a child's size stays E2; a single-line kite flown for play is E1."

## Gold changes

| id | old | new |
|---|---|---|
| T0036 | OUT | J5 |
