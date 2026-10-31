import json, copy, os, sys
ROOT = '/home/user/Possession-Taxonomy/rebuild'
old = json.load(open(ROOT + '/work/STR_E4/bak/E4.json'))
K = {}
for dp in old['depts']:
    for s in dp['s']:
        for k in s['k']:
            K[k['n']] = k
USED = set()
WIKI = 'https://en.wikipedia.org/wiki/'

def mod(name, new_name=None, a=None, d=None, tt=None, drop_x=(), add_x=(), m=None, r=None, see=None, s=None, keep_x=None, x_order=None):
    k = copy.deepcopy(K[name]); USED.add(name)
    if new_name: k['n'] = new_name
    if a is not None: k['a'] = a
    if d is not None: k['d'] = d
    if s is not None: k['s'] = s
    k.pop('t', None)
    if tt is not None: k['tt'] = tt
    if drop_x or keep_x is not None:
        xs = []
        for x in k.get('x', []):
            if x['n'] in drop_x: continue
            if keep_x is not None and x['n'] not in keep_x: continue
            xs.append(x)
        k['x'] = xs
    if add_x:
        k['x'] = list(k.get('x', [])) + list(add_x)
    if x_order:
        by = {x['n']: x for x in k['x']}
        k['x'] = [by[n] for n in x_order if n in by] + [x for x in k['x'] if x['n'] not in x_order]
    if m is not None: k['m'] = m
    if r is not None: k['r'] = r
    if see: k['see'] = see
    for key in ('x', 'm', 'r'):
        if key in k and not k[key]: k.pop(key)
    return k

def nk(n, d, s, a='', tt=None, x=None, m=None, see=None, r=None):
    k = {'n': n, 'a': a, 'd': d, 's': s}
    if tt: k['tt'] = tt
    if x: k['x'] = x
    if m: k['m'] = m
    if r: k['r'] = r
    if see: k['see'] = see
    return k

def X(n, d, s, y='', mk='', dt=None):
    x = {'n': n, 'a': '', 'd': d, 'mk': mk, 'y': y, 's': s, 'v': []}
    if dt: x['dt'] = dt
    return x

def xold(kind, name):
    for x in K[kind]['x']:
        if x['n'] == name: return copy.deepcopy(x)
    raise KeyError((kind, name))

def moved_x(kind, names):
    return [xold(kind, n) for n in names]

def S(n, t, ax, kinds):
    s = {'n': n, 't': t}
    if ax: s['ax'] = ax
    s['k'] = kinds
    return s

def D(n, mode, t, ax, shelves, note=None, b=None):
    dp = {'n': n, 'mode': mode, 't': t, 'ax': ax}
    if note: dp['note'] = note
    if b: dp['b'] = b
    else:
        od = [x for x in old['depts'] if x['n'] == n]
        if od and od[0].get('b'): dp['b'] = od[0]['b']
    dp['s'] = shelves
    return dp

AGE = ['Age and making']
def age_tt(extra=None, labels=None):
    g = [['Age and making', ['Antique (kotō, shintō, shinshintō)', 'Gendaitō', 'Shinsakutō (licensed smith, since 1953)', 'Production replica']]]
    return (extra or []) + g

depts = []
