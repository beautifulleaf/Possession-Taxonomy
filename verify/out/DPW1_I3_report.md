# DPW1_I3 report: I3 Subscriptions, Memberships & Online Services (offline)

## Task 1: missing kinds (13 candidates)
**Decisions:** new_kind 0, covered 5, attribute 2, other_category 6 (I1 ×4, OUT ×2). No new ids were allocated.
- **Covered:**
  - Fixed-wireless 4G/5G home broadband goes to I3.3.02. Its definition already names the router, and technology is an attribute (C10).
  - Free radio goes to I3.1.1.02. A free tier is a band-0 plan row.
  - Paid livestream channel subscriptions go to I3.1.9.02.
  - The National Trust Explorer Pass goes to I3.4.2.01.
  - Fortnite Crew goes to I3.1.7.02.
- **Attribute:**
  - Starlink Roam is a plan under I3.3.04, with mobility as an attribute. The wording "home" in I3.3.04 should be widened.
  - Add-on channels and packs become plan rows with `addon_of` (memo 3.1, C3).
- **Other category:**
  - VPN, password manager, AI assistant, and an AI plan with bundled storage go to I1 (P1).
  - Home security monitoring is OUT, as a service.
  - Loose stock credit packs are OUT (P12).

## Task 2: named forms (598 reviewed, 34 flagged)
- **drop 25:**
  - 8 duplicates: U-NEXT, TELASA, o2, Digi, M:TEL, Lebara Mobile, spusu Mobile, Lycamobile. The makers M-lycamobile and M-lyca-mobile should merge.
  - 4 free ad-supported services: MX Player, Waves, AccuRadio, Jango.
  - Bandcamp (a storefront), sparhandy (a shop) and Cellhire (a one-off rental).
  - Backblaze B2 (business infrastructure).
  - 8 wholesale or B2B operators from the ARCEP list.
  - Town Sports International (a holding company).
- **move_kind 9:**
  - 5 radio or channel networks go to I3.1.1.02.
  - DigitAlb and Tata Play go to I3.1.3.03.
  - YuppTV goes to I3.1.3.02.
  - Airtel XStream goes to I3.1.9.01.
- **to_line 0.** Proton Workspace is already a line.
- **Kept on purpose:**
  - Operator brands stay as mobile-plan named forms, because the consumer brand is the service.
  - Platform rows (Patreon, Substack, Supercast and others) stay.

## Task 3: navigation
**Confirmed:** R-116's way in by use or need.
- 549 of 569 makers have one named form.
- There are no scenes, and the maker role is owner.
- The data bunches by access type: mobile 223, video 121, gyms 50, music 35.
- Phone and internet needs facets at level 3: prepaid or contract, host network, MVNO, market. Market is a facet only, never a level.

**View sketch:**
- **L1:** Watch, Listen, Read, Play, Classes and wellness, Bundles and creator memberships, Online services and storage, Phone and internet, Memberships and passes, Boxes and clubs.
- **L2:** the kinds, for example on-demand video, live-TV streaming, pay-TV.
- **L3:** the providers, each opening its plan ladder.

## Rules applied
C2(a), (b), (d); C3; C10; R-58; P1, P2, P11, P12, P15; memo §14; maker role owner.

## Decisions resting on † claims
- 17 drops: free-only status of 4 services; the store, shop or rental nature of 3; B2; the 8 B2B operators; TSI.
- 4 video moves.
- The paid tiers of the 5 moved radio services.

An apply pass may check these on a fetched page.
