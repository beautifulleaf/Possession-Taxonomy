import json, os
C = 'E1'
WP = 'https://en.wikipedia.org/wiki/'
def X(n, d, mk, y, s, v=(), a='', dt=''):
    x = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s, 'v': [dict(zip(('n', 'mk', 'y', 'd'), vv)) for vv in v]}
    if dt: x['dt'] = dt
    return x
def K(n, d, s, a='', t=None, x=None, m=None, r=None, tg=None):
    k = {'n': n, 'a': a, 'd': d}
    if t: k['t'] = t
    if tg: k['tg'] = tg
    k['s'] = s
    if x: k['x'] = x
    if m: k['m'] = m
    if r: k['r'] = r
    return k
def B(n, c, f, seg, kf, d, s, **kw):
    b = {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d}
    b.update(kw); b['s'] = s
    return {k: v for k, v in b.items() if v not in ('', None, [])}
def write(job, kinds, brands, trads, notes):
    p = f'work/{C}/shelves/{job}.json'; tmp = p + '.tmp'
    json.dump({'kinds': kinds, 'brands': brands, 'traditions': trads, 'notes': notes}, open(tmp, 'w'), ensure_ascii=False, indent=1)
    os.replace(tmp, p)
