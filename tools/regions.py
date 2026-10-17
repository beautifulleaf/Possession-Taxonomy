"""World regions for coverage (owner: every region's clothing brands represented, BRIEF 2026-10-17).
Twelve harvest regions built from UN M49 subregions (Central Asia joined with the Caucasus and Afghanistan; the
Baltics and the Balkans with Eastern Europe). ISO 3166-1 alpha-2 codes; country() normalises names to codes."""

REGIONS = {
    "West & Central Africa": "BJ BF CV CI GM GH GN GW LR ML MR NE NG SN SL TG SH CM CF TD CG CD GQ GA ST AO",
    "East & Southern Africa": "BI KM DJ ER ET KE MG MW MU YT MZ RE RW SC SO SS TZ UG ZM ZW BW SZ LS NA ZA IO TF",
    "North Africa & Middle East": "DZ EG LY MA SD TN EH AE BH IQ IR IL JO KW LB OM PS QA SA SY TR YE CY",
    "Central Asia & Caucasus": "KZ KG TJ TM UZ AM AZ GE AF",
    "South Asia": "BD BT IN MV NP PK LK",
    "Southeast Asia": "BN KH ID LA MY MM PH SG TH TL VN",
    "East Asia": "CN HK MO TW JP KR KP MN",
    "Eastern Europe": "BY BG CZ HU MD PL RO RU SK UA EE LV LT AL BA HR ME MK RS SI XK",
    "Western & Northern Europe": "AT BE FR DE LI LU MC NL CH DK FI IS IE NO SE GB FO AX GG JE IM IT ES PT GR MT SM VA AD GI",
    "North America": "US CA BM GL PM",
    "Latin America & Caribbean": ("MX BZ CR SV GT HN NI PA AR BO BR CL CO EC GY PY PE SR UY VE FK GF AG AW BS BB BQ VG KY CU CW "
                                  "DM DO GD GP HT JM MQ MS PR BL KN LC MF VC SX TT TC VI AI"),
    "Oceania": "AU NZ FJ PG SB VU NC PF WS TO KI TV NR PW FM MH CK NU CX CC NF GU MP AS WF TK PN",
}
REGION_OF = {c: r for r, cs in REGIONS.items() for c in cs.split()}

ALIASES = {"usa": "US", "u.s.": "US", "us": "US", "united states of america": "US", "america": "US",
           "uk": "GB", "u.k.": "GB", "england": "GB", "scotland": "GB", "wales": "GB", "northern ireland": "GB",
           "great britain": "GB", "britain": "GB", "south korea": "KR", "korea": "KR", "republic of korea": "KR",
           "north korea": "KP", "russia": "RU", "vietnam": "VN", "viet nam": "VN", "iran": "IR", "turkey": "TR",
           "türkiye": "TR", "turkiye": "TR", "czech republic": "CZ", "czechia": "CZ", "taiwan": "TW", "hong kong": "HK",
           "macau": "MO", "macao": "MO", "laos": "LA", "syria": "SY", "tanzania": "TZ", "bolivia": "BO",
           "venezuela": "VE", "moldova": "MD", "ivory coast": "CI", "côte d'ivoire": "CI", "cote d'ivoire": "CI",
           "drc": "CD", "dr congo": "CD", "democratic republic of the congo": "CD", "republic of the congo": "CG",
           "palestine": "PS", "kosovo": "XK", "brunei": "BN", "cape verde": "CV", "eswatini": "SZ", "swaziland": "SZ",
           "burma": "MM", "holland": "NL", "the netherlands": "NL", "uae": "AE", "emirates": "AE"}

def country(value):
    """Return an ISO alpha-2 code for a country name or code, or '' when it cannot be resolved."""
    v = (value or "").strip()
    if not v: return ""
    if len(v) == 2 and v.upper() in REGION_OF: return v.upper()
    low = v.lower().strip(" .")
    if low in ALIASES: return ALIASES[low]
    try:
        import pycountry
        return pycountry.countries.lookup(v).alpha_2
    except Exception:
        pass
    for part in v.replace(";", ",").replace("/", ",").split(","):  # "Tokyo, Japan" -> Japan
        p = part.strip().lower()
        if p in ALIASES: return ALIASES[p]
        try:
            import pycountry
            return pycountry.countries.lookup(part.strip()).alpha_2
        except Exception:
            continue
    return ""
