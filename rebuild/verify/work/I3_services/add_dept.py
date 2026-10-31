import json, os, sys
P = '/home/user/Possession-Taxonomy/rebuild/work/I3/plan.raw.json'
plan = json.load(open(P))
if any(d['n'] == 'Services & staff' for d in plan['depts']):
    sys.exit('already added')
plan['lead'] = plan['lead'].replace(
    "memberships and clubs, deliveries)",
    "memberships and clubs, deliveries, retained services and staff)")
assert 'retained services' in plan['lead']
SRC = (" Source each kind from a retrieved page (Wikipedia article, trade body, regulator or operator page). "
       "Operators go in m/r as market-covering firms by country; brand-register entries only if sourced. "
       "One-off jobs (a single deep clean, removals, a single repair, a one-off ride or charter) are OUT per BRIEF; only recurring contracts, retainers and memberships.")
dept = {
 "n": "Services & staff",
 "mode": "mixed",
 "note": "Recurring and retained services (owner decision 2026-10-27): tier for everyday home contracts, variety at the luxury end (staff, concierge, private aviation and yachting). One-off services stay out.",
 "b": [
  {"m": "Vetting and insurance", "v": "agency-employed, background-checked and insured > platform-vetted freelancer > unvetted",
   "w": "First; background checks (e.g. DBS in the UK), public-liability and employer's insurance, trade-body or regulator registration where one exists."},
  {"m": "Contract terms", "v": "rolling monthly > fixed term with break clause > long minimum term",
   "w": "Second; notice period, minimum term, cancellation and price-rise clauses, who employs the worker (agency or you)."},
  {"m": "Response times and service level", "w": "Third; call-out or emergency response time, cover for holidays and sickness, same named person each visit."},
  {"m": "Independent reviews", "w": "Fourth; Which? Trusted Traders, Checkatrade, Trustpilot, Care.com or Rover reviews, regulator reports (e.g. Ofsted for childcare)."},
  {"m": "Price per visit, hour or year", "v": "pay-per-visit < monthly plan < retainer < full-time staff",
   "w": "Last; compared on the same frequency of service."}
 ],
 "s": [
  {"n": "Home upkeep contracts", "web": True,
   "brief": "Tier shelf: everyday recurring contracts that keep a home running. For each kind list the market-covering operators/franchises by major market (US, UK, EU, Australia) plus test or survey winners (Which?, Consumer Reports, CHOICE) where they exist, ≈5–10 per kind; frequency and plan levels as t. Candidates to verify (not facts): cleaning – Molly Maid, Merry Maids, The Maids, Helpling, Housekeep; laundry – Laundryheap, Rinse, Oxwash; lawn and garden – TruGreen, Green Thumb; pest control – Rentokil, Terminix, Orkin; home and appliance cover – HomeServe, British Gas HomeCare, Domestic & General, American Home Shield; alarm monitoring – ADT, Verisure/Securitas Direct, SimpliSafe, Vivint, Ring Protect. Boundaries: alarm kits, cameras and sensors stay in B8 (only the monitoring contract is here); a hot tub itself is G3; personal medical alarms stay in H2. No archetypes needed; plain definitions." + SRC,
   "k": [
    {"n": "Home cleaning service", "old": [], "brief": "Regular cleaner via agency, franchise or platform; t: weekly, fortnightly, agency-employed, platform freelancer, eco cleaning."},
    {"n": "Window and gutter cleaning", "old": [], "brief": "Round-based recurring window cleaning; t: traditional, water-fed pole, gutter clearing, conservatory/solar-panel cleaning."},
    {"n": "Laundry and dry-cleaning subscription", "old": [], "brief": "Collection-and-delivery laundry plans; t: wash-and-fold, dry cleaning, shirt service, ironing service."},
    {"n": "Garden maintenance contract", "old": [], "brief": "Gardening and landscaping on a retained schedule; t: lawn treatment plan, mowing round, full garden maintenance, tree care plan."},
    {"n": "Pool and hot-tub maintenance", "old": [], "brief": "Weekly or seasonal pool/spa servicing; t: weekly service, opening/closing contract, chemicals-included plan."},
    {"n": "Pest-control contract", "old": [], "brief": "Recurring inspection and treatment plans; t: general pest, termite bond, rodent, mosquito."},
    {"n": "Home emergency and appliance cover", "old": [], "brief": "Merges boiler cover, home emergency cover, appliance cover and US home warranty; t: boiler and heating, plumbing and drains, electrics, appliance, whole-home warranty."},
    {"n": "Home security monitoring", "old": [], "brief": "Monitored-alarm contract (B8 has no such kind, only devices); t: professional monitoring, self-monitoring plan, keyholding and guard response, video verification."}
   ]},
  {"n": "Family, pet & personal services", "web": True,
   "brief": "Mixed shelf: retained help for children, pets and the person, from app platforms to elite agencies. Tier the everyday platforms (market leaders by country) and add the recognised luxury end as named entries where sourced. Candidates to verify (not facts): pets – Rover, Wag!, Pawshake, TrustedHousesitters; childcare – Care.com, Sittercity, Koru Kids, Norland-trained nannies, Cultural Care Au Pair, Au Pair in America, AuPairWorld; tutoring – Kumon, Mathnasium, MyTutor, Varsity Tutors, Wyzant, Tutors International; personal training – credential bodies (NASM, ACE, CIMSPA) as criteria, not brands; personal chef – private-chef platforms; styling – department-store personal shopping (Harrods, Selfridges, Nordstrom), independent stylists. Boundaries: gyms, class passes and fitness apps stay in Gyms & fitness / Games & learning; meal kits and ready-meal plans stay in Meal kit and menu plan; Stitch Fix-type boxes stay in Curated subscription box." + SRC,
   "k": [
    {"n": "Childcare: nanny and au pair", "old": [], "brief": "Retained childcare; t: live-in nanny, daily nanny, nanny share, maternity nurse, au pair (via agency), babysitting membership. Regulator/registration (e.g. Ofsted register) as criterion.", },
    {"n": "Dog walking and pet sitting", "old": [], "brief": "Recurring walks, day care and sitting; t: dog walking, drop-in visits, home boarding, house-sitting membership."},
    {"n": "Personal trainer", "old": [], "brief": "Ongoing one-to-one coaching; t: in-person, at-home, online coaching, block of sessions."},
    {"n": "Private tutor", "old": [], "brief": "Regular tutoring; t: online platform, in-person, learning-centre programme, residential/full-time tutor (luxury end)."},
    {"n": "Personal chef service", "old": [], "brief": "Retained chef cooking at home; t: weekly meal-prep chef, private chef on retainer, full-time household chef."},
    {"n": "Personal stylist and personal shopper", "old": [], "brief": "Ongoing wardrobe service; t: department-store personal shopping, independent stylist retainer, online styling subscription."}
   ]},
  {"n": "Household staff & concierge", "web": True,
   "brief": "Variety shelf (luxury lifestyle): named agencies and membership services, with founding year and country where sourced. Domestic staffing agencies as operators (candidates to verify: Greycoat Lumleys, Polo & Tweed, Bespoke Bureau, Silver Swan Recruitment; butler schools only as criteria); lifestyle concierge (Quintessentially, John Paul, Ten Lifestyle Group – if sourced; card-issuer concierge as a type only); concierge medicine (candidates: MDVIP, One Medical, Sollis Health; UK private GP subscriptions; executive health programmes) – check each is still trading. Staff roles are types, not kinds." + SRC,
   "k": [
    {"n": "Domestic staff via staffing agency", "old": [], "brief": "Merges housekeeper, butler and estate staff; t: housekeeper, house manager, butler, estate manager, nanny-housekeeper, couple (live-in), yacht/chalet staff."},
    {"n": "Lifestyle concierge membership", "old": [], "brief": "Retained personal-assistant service for bookings, access and errands; t: digital concierge, dedicated lifestyle manager, card-linked concierge."},
    {"n": "Wellness and medical concierge", "old": [], "brief": "Subscription primary care and health concierge; t: concierge medicine, private GP membership, executive health programme, wellness coaching retainer."}
   ]},
  {"n": "Chauffeur, jet & yacht", "web": True,
   "brief": "Variety shelf (luxury travel on a retained or membership basis): leading operators with founding year, country and plan types where sourced. Brand-register hints (if sourced): NetJets, VistaJet, Wheels Up, Flexjet, Sentient Jet, XO; boat clubs (candidates: Freedom Boat Club, Carefree Boat Club) as the everyday end of the yacht ladder; fractional superyacht schemes if sourced; chauffeur – Blacklane and similar hourly/retained providers, local chauffeur firms as types. Boundaries: single rides, single charters and one-off flights are OUT; owning a jet or yacht outright is G1 Vehicles; private members' and yacht clubs as social clubs stay in Clubs & status." + SRC,
   "k": [
    {"n": "Chauffeur service", "old": [], "brief": "Retained or account chauffeur; t: monthly retainer, personal account, full-time chauffeur (agency-placed), close-protection driver."},
    {"n": "Private jet card and membership", "old": [], "brief": "Prepaid flight hours or membership with an operator; t: jet card, membership programme, fractional share, jet lease; cabin class (light, midsize, heavy) as an axis."},
    {"n": "Boat club and fractional yacht", "old": [], "brief": "Membership or shared ownership of boats and yachts; t: boat club membership, fractional yacht share, yacht membership programme."}
   ]}
 ]
}
plan['depts'].append(dept)
tmp = P + '.tmp'
with open(tmp, 'w') as f: json.dump(plan, f, ensure_ascii=False, indent=1)
os.replace(tmp, P)
print('ok', len(plan['depts']))
