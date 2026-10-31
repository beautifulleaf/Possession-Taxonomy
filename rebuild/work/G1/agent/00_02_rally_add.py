import json, os
P = '/home/user/Possession-Taxonomy/rebuild/work/G1/shelves/00_02.json'
d = json.load(open(P))
def kind(n): return [k for k in d['kinds'] if k['n'] == n][0]
names = {x['n'] for k in d['kinds'] for x in k.get('x', [])}
evo = {"n": "Mitsubishi Lancer Evolution", "a": "Lancer Evo · Evo",
 "d": "Turbocharged four-wheel-drive Lancer saloon built to homologate Mitsubishi's rally car.",
 "mk": "Mitsubishi", "y": "1992", "s": "https://en.wikipedia.org/wiki/Mitsubishi_Lancer_Evolution",
 "v": [{"n": "Evolution I", "mk": "Mitsubishi", "y": "1992", "d": "first generation, GSR and RS"},
       {"n": "Evolution II", "mk": "Mitsubishi", "y": "1994", "d": "260 PS"},
       {"n": "Evolution III", "mk": "Mitsubishi", "y": "1995", "d": "270 PS"},
       {"n": "Evolution IV", "mk": "Mitsubishi", "y": "1996", "d": "Active Yaw Control"},
       {"n": "Evolution V", "mk": "Mitsubishi", "y": "1998", "d": "wider body, Brembo brakes"},
       {"n": "Evolution VI", "mk": "Mitsubishi", "y": "1999", "d": ""},
       {"n": "Evolution VI Tommi Mäkinen Edition", "mk": "Mitsubishi", "y": "1999", "d": "limited edition"},
       {"n": "Evolution VII", "mk": "Mitsubishi", "y": "2001", "d": "Lancer Cedia platform"},
       {"n": "Evolution VIII", "mk": "Mitsubishi", "y": "2003", "d": "first sold in the US; FQ-400 in UK"},
       {"n": "Evolution IX", "mk": "Mitsubishi", "y": "2005", "d": "MIVEC"},
       {"n": "Evolution X", "mk": "Mitsubishi", "y": "2007", "d": "final generation, to 2016"}],
 "dt": "generation · trim (GSR, RS, MR, FQ) · manual or automatic"}
wrx = {"n": "Subaru Impreza WRX / WRX STI", "a": "Subaru WRX · WRX STI · Scooby",
 "d": "Turbocharged four-wheel-drive Impreza-based saloon, with the STI as its homologation-derived top version.",
 "mk": "Subaru", "y": "1992", "s": "https://en.wikipedia.org/wiki/Subaru_Impreza_WRX",
 "v": [{"n": "First generation (GC/GF)", "mk": "Subaru", "y": "1992", "d": "saloon and wagon; first STi 1994"},
       {"n": "Second generation (GD/GG)", "mk": "Subaru", "y": "2000", "d": "saloon and wagon"},
       {"n": "Third generation (GE/GH, GV/GR)", "mk": "Subaru", "y": "2007", "d": "saloon and hatch; widebody STI"},
       {"n": "WRX (VA)", "mk": "Subaru", "y": "2014", "d": "first WRX separate from the Impreza"},
       {"n": "WRX (VB)", "mk": "Subaru", "y": "2021", "d": "Subaru Global Platform"}],
 "dt": "generation · WRX or STI · saloon, wagon or hatch"}
delta = {"n": "Lancia Delta HF Integrale", "a": "Delta Integrale · Delta HF 4WD",
 "d": "Turbocharged four-wheel-drive Delta hatchback homologated for Lancia's rally programme.",
 "mk": "Lancia", "y": "1986", "s": "https://en.wikipedia.org/wiki/Lancia_Delta_HF_Integrale",
 "v": [{"n": "Delta HF 4WD", "mk": "Lancia", "y": "1986", "d": ""},
       {"n": "HF Integrale 8V", "mk": "Lancia", "y": "1987", "d": ""},
       {"n": "HF Integrale 16v", "mk": "Lancia", "y": "1989", "d": ""},
       {"n": "HF Integrale Evoluzione", "mk": "Lancia", "y": "1991", "d": ""},
       {"n": "HF Integrale Evoluzione II", "mk": "Lancia", "y": "1993", "d": ""}],
 "dt": "version · 8- or 16-valve · special editions"}
for kn, a in (("Sports car", evo), ("Sports car", wrx), ("Hot hatch", delta)):
    if a['n'] not in names: kind(kn)['x'].append(a)
bn = {b['n'] for b in d['brands']}
for b in [{"n": "Mitsubishi", "c": "Japan", "seg": "Mass-market cars", "d": "Japanese carmaker whose Lancer Evolution came from its rally programme.", "sig": ["Mitsubishi Lancer Evolution"], "s": "knowledge"},
          {"n": "Subaru", "c": "Japan", "seg": "Mass-market cars", "d": "Japanese carmaker known for flat engines and four-wheel drive.", "sig": ["Subaru Impreza WRX / WRX STI", "Toyota 86 / Subaru BRZ"], "s": "knowledge"},
          {"n": "Lancia", "c": "Italy", "f": "1906", "seg": "Mass-market and sports cars", "d": "Turin carmaker with a long rallying record.", "sig": ["Lancia Delta HF Integrale"], "s": "knowledge"}]:
    if b['n'] not in bn: d['brands'].append(b)
old = "Sports saloons (Lancer Evolution, Subaru WRX, Lancia Delta Integrale) and grand tourers (Ferrari 250 GTO) left for the saloon/grand-tourer shelves."
new = "Rally-homologation icons added in a follow-up: Lancer Evolution and Subaru Impreza WRX/STI under Sports car, Lancia Delta HF Integrale under Hot hatch. Grand tourers (Ferrari 250 GTO) left for the grand-tourer shelf."
assert old in d['notes']; d['notes'] = d['notes'].replace(old, new)
t = P + '.tmp'; json.dump(d, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, P)
print('ok')
