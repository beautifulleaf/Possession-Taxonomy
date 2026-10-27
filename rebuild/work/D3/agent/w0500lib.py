import json, os
def w(code, job, obj):
    p = f'/home/user/Possession-Taxonomy/rebuild/work/{code}/shelves/{job}.json'
    t = p + '.tmp'; json.dump(obj, open(t, 'w'), ensure_ascii=False, indent=1); os.replace(t, p)
def X(n, d, mk, y, s, v=(), a="", dt=""):
    x = {"n": n, "a": a, "d": d, "mk": mk, "y": y, "s": s, "v": [{"n": a_, "mk": b, "y": c, "d": e} for a_, b, c, e in v]}
    if dt: x["dt"] = dt
    return x
def B(n, c, f, seg, kf, d, s, sig=()):
    b = {"n": n, "c": c, "f": f, "seg": seg, "kf": kf, "d": d, "s": s}
    if sig: b["sig"] = list(sig)
    return b
