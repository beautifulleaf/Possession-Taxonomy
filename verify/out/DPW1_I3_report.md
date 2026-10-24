# DPW1_I3 report: I3 Subscriptions, Memberships & Online Services (offline decision pass)

## Task 1: missing kinds (13 candidates)
- **Where they came from:** the 5 harvest items, with the VPN, password-manager and AI-assistant list split into 4 items. Also 5 types taken from the "gave" column of the fetch log. There was no DPMK_1_I3 file to skip against.
- **Decisions:** new_kind 0; covered 5; attribute 2; other_category 6 (I1 4, OUT 2); named_form 0.
  - **Covered:**
    - Fixed-wireless 4G/5G home broadband goes to I3.3.02, whose definition already names the router. The kind axis is the connection, and technology is an attribute (memo C10).
    - Free internet radio goes to I3.1.1.02. A free tier is a band-0 plan row; free-only radio is OUT.
    - A paid livestream channel subscription goes to I3.1.9.02.
    - The National Trust Explorer Pass goes to I3.4.2.01. Its term is a plan attribute.
    - Fortnite Crew goes to I3.1.7.02.
  - **Attribute:**
    - Starlink Roam is a plan of I3.3.04, with mobility as an attribute. The wording "home" in I3.3.04 should be widened.
    - Add-on channels and packs are plan rows with `addon_of` (memo 3.1, C3).
  - **Other category:**
    - VPN, password manager, AI assistant, and an AI plan that carries storage are I1 (P1).
    - A home security monitoring plan is OUT, as a service (a camera's cloud plan is I1 by P11).
    - Loose stock credit packs are OUT (P12).
- No new kinds, so no ids were allocated.

## Task 2: named forms (598 reviewed, 34 flagged)
- **drop 25:**
  - 8 duplicates: U-NEXT, TELASA, o2, Digi, M:TEL, Lebara Mobile, spusu Mobile, Lycamobile. Lycamobile also means the makers M-lycamobile and M-lyca-mobile should merge.
  - 4 free ad-supported services, which are OUT: Amazon MX Player, Waves, AccuRadio, Jango.
  - 2 shops: Bandcamp (a storefront) and sparhandy (a contract shop).
  - 1 one-off rental: Cellhire.
  - 1 business infrastructure product: Backblaze B2.
  - 8 wholesale, MVNE, IoT or business-only operators from the ARCEP list: Alphalink, Unyc, Transatel, Cubic, Keyyo, Sewan, SCT Telecom, Stelogy.
  - 1 holding company: Town Sports International.
- **move_kind 9:**
  - iHeartRadio, TuneIn, MyTuner Radio, Music Choice and Stingray Music go to I3.1.1.02. They are radio or channel networks, not on-demand libraries.
  - DigitAlb and Tata Play go to I3.1.3.03 (pay-TV).
  - YuppTV goes to I3.1.3.02 (live channels).
  - Airtel XStream goes to I3.1.9.01 (an aggregator bundle).
- **to_line 0:** Proton Workspace is already a line. Interrail's four passes sit in one kind and stay named forms (C2(d)).
- **Not flagged, on purpose:**
  - Operator brands stand as mobile-plan named forms. In connectivity the consumer brand is the service, as Netflix is.
  - Platform rows (Patreon, Substack, YouTube channel memberships, Supercast, Apple Podcasts Subscriptions) stay as the plan mechanism buyers name.

## Task 3: navigation
**Confirmed:** R-116's way in by use or need, with level 1 split by medium.
- 549 of 569 makers have one named form. Only Apple, Xfinity, Telekom and Interrail reach 3 or more.
- No scenes exist, and the maker role is owner, so brand and scene fail as a way in.
- The named forms bunch by access type: mobile 223, video 121, gyms 50, music 35, mail, storage and messaging 64.
- The third level is the provider list. For Phone and internet it needs facets (prepaid or contract, host network, MVNO, market) rather than a flat list. Market stays a facet, never a level (owner, no country way in).

**View sketch:**
- **L1:** Watch, Listen, Read, Play, Classes and wellness, Bundles and creator memberships, Online services and storage, Phone and internet, Memberships and passes, Boxes and clubs.
- **L2:** the kinds. For example:
  - Watch: on-demand video, live-TV streaming, pay-TV.
  - Phone and internet: mobile phone plan, data plan, broadband, satellite, home phone, bundle, travel eSIM.
- **L3:** providers (the named forms), each opening its plan ladder: seats, ads, tier, term.

## Rules applied
C2(a), (b), (d); C3 (`addon_of`, plan rows); C10 (technology as an attribute); R-58 (no ids used); P1, P2, P4, P11, P12, P15; memo §14 (free tier = band 0; free ad-supported = OUT); maker role owner (maker_roles.tsv); BRIEF (utility vs entertainment; one-off services OUT).

## Decisions resting on † claims (my own knowledge, offline; no fetched page)
- 17 drops: the free-only status of MX Player, Waves, AccuRadio and Jango; the store, shop and rental nature of Bandcamp, sparhandy and Cellhire; B2 as developer storage; the 8 B2B operators; TSI as a holding company.
- 4 moves: DigitAlb, Tata Play, YuppTV, Airtel XStream.
- The paid tiers of the 5 radio services moved to I3.1.1.02.

An apply pass may check any of these on a fetched page before loading.

Files: verify/out/DPW1_I3_kinds.tsv, verify/out/DPW1_I3_moves.tsv.
