"""Clothing (A1) brand register, second level (owner, 2026-11-01): market segment stays the top level; inside it,
Traditional & national dress and Subculture & alternative split by the brand's main scene, every other segment by
home region. Fills from the Haiku pass verify/work/A1FILL/out.tsv (segment, country) where the data had none.
Called by registers.py on the A1 view: subgroup(list) -> list with 'sg' (and filled seg/c)."""
import os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEGS = ["Luxury house", "Designer", "Contemporary & premium", "Heritage & workwear", "Japanese & denim", "Streetwear", "Outdoor & technical",
        "Athletic & sportswear", "High street", "Value & basics", "Bespoke & artisan", "Traditional & national dress", "Subculture & alternative"]
SCENE = {'Traditional & national dress', 'Subculture & alternative'}
REG = [('Japan', 'Japan'), ('South Korea|Korea', 'Korea'), ('China|Hong Kong|Taiwan|Macau', 'Greater China'),
       ('United States|USA|US$', 'United States'), ('Canada', 'Canada'), ('United Kingdom|England|Scotland|Wales|Ireland|Northern Ireland|UK', 'UK & Ireland'),
       ('France|Monaco', 'France'), ('Italy', 'Italy'), ('Spain|Portugal', 'Spain & Portugal'),
       ('Denmark|Sweden|Norway|Finland|Iceland', 'Nordics'), ('Germany|Austria|Switzerland|Liechtenstein', 'Germany, Austria & Switzerland'),
       ('Netherlands|Belgium|Luxembourg', 'Benelux'), ('Poland|Czech|Slovakia|Hungary|Romania|Bulgaria|Ukraine|Russia|Belarus|Lithuania|Latvia|Estonia|Georgia|Serbia|Croatia|Slovenia|Bosnia|Albania|North Macedonia|Montenegro|Moldova|Greece|Cyprus', 'Central & Eastern Europe'),
       ('India|Pakistan|Bangladesh|Sri Lanka|Nepal', 'South Asia'),
       ('Indonesia|Malaysia|Singapore|Thailand|Vietnam|Philippines|Cambodia|Myanmar', 'Southeast Asia'),
       ('Australia|New Zealand', 'Australia & New Zealand'),
       ('Brazil|Mexico|Argentina|Colombia|Chile|Peru|Uruguay|Venezuela|Ecuador|Bolivia|Paraguay|Cuba|Guatemala|Costa Rica|Puerto Rico|Dominican', 'Latin America'),
       ('Turkey|Israel|Lebanon|United Arab Emirates|UAE|Saudi|Qatar|Kuwait|Bahrain|Oman|Jordan|Iran|Egypt|Morocco|Tunisia|Algeria', 'Middle East & North Africa'),
       ('Nigeria|Ghana|Kenya|South Africa|Senegal|Ethiopia|Ivory|Côte|Uganda|Tanzania|Rwanda|Cameroon|Zimbabwe|Mali|Togo|Benin', 'Sub-Saharan Africa')]
def region(c):
    c = (c or '').strip()
    for rx, r in REG:
        if re.search(r'^(' + rx + r')\b', c, re.I) or re.search(r'\b(' + rx + r')$', c, re.I): return r
    return 'Other or unknown region' if c else 'Region not recorded'
FILL = {}
p = f'{R}/../verify/work/A1FILL/out.tsv'
if os.path.exists(p):
    for l in open(p).read().splitlines():
        f = l.split('\t')
        if len(f) == 3: FILL[f[0]] = (f[1].strip(), f[2].strip())
def subgroup(lst):
    for e in lst:
        s, c = FILL.get(e['n'], ('-', '-'))
        if not e.get('seg') and s.isdigit() and 0 < int(s) <= len(SEGS): e['seg'] = SEGS[int(s) - 1]
        if not e.get('c') and c not in ('-', '?', ''): e['c'] = c
        e['sg'] = (e.get('sc') or ['Other'])[0] if e.get('seg') in SCENE else region(e.get('c'))
    return lst
