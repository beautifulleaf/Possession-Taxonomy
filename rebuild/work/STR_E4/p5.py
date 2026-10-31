
# ================= ASSEMBLE =================
order = [swords, knives, polearms, archery, firearms, airguns, ammo, optics, selfdef, armour, modern, mil]
cat = {'c': 'E4', 'rev': True,
 'lead': old['lead'],
 'ax': 'What does the object do: cut or strike by hand, shoot a projectile, protect the wearer, or equip and supply a gun?',
 'key': [
  '1. Is it deactivated, inert or a copy that cannot fire or cut? → Militaria & replicas',
  '2. Is it a sword, or a guard, scabbard or fitting made for one? → Swords',
  '3. Is it a dagger, knife, bayonet or thrown blade? → Knives & daggers',
  '4. Is it a spear, axe, mace, hammer, or a stick, chain or blade used in martial arts? → Polearms, axes & martial arts weapons',
  '5. Is it a bow, crossbow, sling or other muscle-powered launcher, or an arrow, bolt or bow fitting? → Archery & slings',
  '6. Is it a gun that fires by burning powder, including muzzle-loaders? → Firearms',
  '7. Is it a gun that fires by compressed air or gas, or its pellets and gas? → Air guns',
  '8. Is it a round of ammunition, a component for loading one, or loading equipment? → Ammunition & reloading',
  '9. Does it sight, replace a part of, support, carry or clean a gun? → Optics, parts & shooting accessories',
  '10. Is it a spray, electric device, striker or blank-firing pistol carried to stop an attacker? → Self-defence',
  '11. Is it historical or reenactment armour, or a shield? → Armour & shields',
  '12. Is it a vest, plate or helmet rated against bullets or blades? → Modern body armour',
  '<i>Precedence: a deactivated or non-firing copy is Militaria before any weapon department; a bayonet is a knife, not a gun part; a blank-firing pistol is Self-defence, not Firearms; a sword that is only a practice or toy copy is E2 or E1.</i>'],
 'b': old.get('b', []), 'depts': order}
names = {}
dup = []
for dp in order:
    for s in dp['s']:
        for k in s['k']:
            if k['n'].lower() in names: dup.append(k['n'])
            names[k['n'].lower()] = k
print('unused old kinds:', sorted(set(K) - USED))
print('duplicates:', dup)
# demoted-archetype accounting
alltext = json.dumps(order, ensure_ascii=False).lower()
missing = []
newx = {x['n'].lower() for dp in order for s in dp['s'] for k in s['k'] for x in k.get('x', [])}
for kn, k in K.items():
    for x in k.get('x', []):
        if x['n'].lower() not in newx:
            # accounted if it appears as a tt member, alias or kind name
            ok = False
            for dp in order:
                for s in dp['s']:
                    for kk in s['k']:
                        if x['n'].lower() == kk['n'].lower(): ok = True
                        if x['n'].lower() in kk.get('a', '').lower(): ok = True
                        for g in kk.get('tt', []):
                            if any(x['n'].lower() in t.lower() for t in g[1]): ok = True
            if not ok: missing.append((kn, x['n']))
print('archetypes not accounted:', missing)
# see targets
import glob
def rk(code):
    p = f'{ROOT}/reader/{code}.json'
    d = json.load(open(p)); return {k['n'] for dp in d['depts'] for s in dp['s'] for k in s['k']}
cache = {}
bad = []
nsee = 0
for dp in order:
    for s in dp['s']:
        for k in s['k']:
            for sv in k.get('see', []):
                nsee += 1
                if sv[0] == 'E4':
                    if sv[1].lower() not in names: bad.append((k['n'], sv))
                else:
                    cache.setdefault(sv[0], rk(sv[0]))
                    if sv[1] not in cache[sv[0]]: bad.append((k['n'], sv))
print('see count', nsee, 'bad see', bad)
renames = {"Air rifle": "Spring-piston air rifle", "Air pistol": "Pneumatic air pistol", "Bayonet": "Knife bayonet", "Body armour": "Soft ballistic vest",
           "Plate helmet": "Historical helmet", "Reloading die": "Reloading die set", "Shield": "Round shield"}
for v in renames.values(): assert v.lower() in names, v
# stats
def stats(d):
    ds = len(d['depts']); sh = sum(len(x['s']) for x in d['depts']); ks = [k for x in d['depts'] for s in x['s'] for k in s['k']]
    return ds, sh, len(ks), sum(len(k.get('x', [])) for k in ks)
print('before', stats(old), 'after', stats(cat))
OUT = ROOT + '/out'
tmp = OUT + '/E4.json.tmp'
json.dump(cat, open(tmp, 'w'), ensure_ascii=False, indent=1)
os.replace(tmp, OUT + '/E4.json')
json.dump(renames, open(OUT + '/E4_renames.json', 'w'), ensure_ascii=False, indent=1)
print(os.path.getsize(OUT + '/E4.json'))
