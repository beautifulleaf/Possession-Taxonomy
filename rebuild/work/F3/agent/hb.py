import json, os
WP = "https://en.wikipedia.org/wiki/"
def X(n, d, s, mk="", y="", a="", v=None, dt=""):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s}
    x["v"] = [dict(zip(("n", "mk", "y", "d"), t)) for t in (v or [])]
    if dt: x["dt"] = dt
    return x
def K(n, d, s, a="", t=None, x=None, m=None, r=None, tg=None):
    k = {"n": n, "a": a, "d": d, "s": s}
    if t: k["t"] = t
    if tg: k["tg"] = tg
    if x: k["x"] = x
    if m: k["m"] = m
    if r: k["r"] = r
    return k
def B(n, c, f, kf, d, s, seg="Institution & issuer", **kw):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "s": s}
    b.update(kw); return b
def save(job, kinds, brands, trads, notes):
    p = f"/home/user/Possession-Taxonomy/rebuild/work/F3/shelves/{job}.json"
    tmp = p + ".tmp"
    json.dump({"kinds": kinds, "brands": brands, "traditions": trads, "notes": notes}, open(tmp, "w"), ensure_ascii=False, indent=1)
    os.replace(tmp, p); print("wrote", p)
