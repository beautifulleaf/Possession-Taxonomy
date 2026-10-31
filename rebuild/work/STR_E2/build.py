import json, copy, os, sys, shutil, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import *
from tt_data import TT

R = '/home/user/Possession-Taxonomy/rebuild/'
old = json.load(open(R + 'work/STR_E2/bak/E2.json'))
Wk = lambda t: 'https://en.wikipedia.org/wiki/' + t

# index of old kinds
K = {}
for di, dp in enumerate(old['depts']):
    for s in dp['s']:
        for k in s['k']:
            K[k['n']] = k

# ---- merges: (old name) -> kept name ; carry archetypes, models, ranges
MERGE = {
 'HEMA fencing jacket': 'Fencing jacket',
 'HEMA protective gloves': 'Fencing glove',
 'HEMA chest protector': 'Fencing chest protector',
 'HEMA fencing trousers': 'Fencing breeches',
}
RENAME = {'HEMA gorget': 'Fencing gorget', 'Terminal tackle': 'Fishing hook'}
MOVE_OUT = {'Fingerboard': ('E1', 'Skill, music & novelty toys')}

# ---- generic archetypes demoted to types (kind -> names)
DEMOTE = {
 'Golf driver': ['M-series and carbon-face TaylorMade drivers'],
 'Pickleball paddle': ['Plywood pickleball paddle'],
 'Sliotar': ['Cork-core leather sliotar'],
 'Ice hockey stick': ['One-piece composite stick'],
 'Lacrosse stick': ['Plastic lacrosse head', 'Offset head', 'Wooden lacrosse stick'],
 'Hurley': ['Ash hurley'],
 'Goalie mask': ['Helmet and cage combination', 'Hybrid fibreglass-and-cage mask'],
 'Quiver': ['Arrow bag'],
 'Archery target': ['122 cm target face', '80 cm target face', '3-spot target face'],
 'Archery thumb ring': ['Flanged (pad) ring'],
 'Camping hammock': ['Bridge hammock'],
 'Tent': ['Pup tent'],
 'Bell tent': ['Military bell tent'],
 'Belay device': ['Figure of eight'],
 'Dive cylinder': ['Steel high-pressure cylinder'],
 'Surfboard': ['Longboard', 'Malibu / funboard', 'Shortboard', 'Gun', 'Hybrid', 'Tow-in board'],
 'Kitesurf kite': ['Leading-edge inflatable kite'],
 'Ice skate': ['Short-track speed blade', 'Nordic tour skate'],
 'Skateboard': ['Old school board'],
 'Fencing foil': ['Maraging FIE blade', 'Visconti grip', 'Belgian grip', 'Russian grip', 'Hungarian grip'],
 'Fencing epee': ['FIE épée blade', 'French grip', 'Italian grip'],
 'Fencing sabre': ['FIE sabre blade'],
 'Bokken': ['Standard bokken'],
 'Kendo armour': ['Bōgu set'],
 'HEMA protective gloves': ['Sparring Gloves'],
}

# ---- new kinds
def nk(n, d, s, a='', x=None, **kw):
    k = {'n': n, 'a': a, 'd': d, 's': s}
    if x: k['x'] = x
    k.update(kw); return k
def arch(n, d, mk, y, s, **kw):
    a = {'n': n, 'a': '', 'd': d, 'mk': mk, 'y': y, 's': s, 'v': []}; a.update(kw); return a
EX = Wk('Exercise_machine'); FT = Wk('Fishing_tackle'); GE = Wk('Golf_equipment'); DE = Wk('Diving_equipment')
NEW = {
 'Vertical climber': nk('Vertical climber', 'Upright machine with two linked ladder rails that the user climbs hand over hand, listed as the Jacobs Ladder.', EX, 'Jacobs Ladder · ladder climber'),
 'Vibration plate': nk('Vibration plate', 'Platform that vibrates under a standing or exercising user, sold for whole-body vibration training and recovery.', EX, 'whole-body vibration machine'),
 'Racquetball racket': nk('Racquetball racket', 'Short, strung racket of no more than 22 inches used for racquetball, the court game devised in 1950 by Joseph Sobek.', Wk('Racquetball'), 'racquetball racquet'),
 'Racquetball': nk('Racquetball', 'Hollow rubber ball about 57 mm across, sold in speed colours, used in the court game of racquetball.', Wk('Racquetball'), 'racquetball ball'),
 'Golf tee': nk('Golf tee', 'Small peg that holds the ball above the ground for the opening stroke of a hole.', GE),
 'Golf shoe': nk('Golf shoe', 'Shoe with a spiked or spikeless sole made for walking the course and gripping during the swing.', GE),
 'Golf headcover': nk('Golf headcover', 'Cover that protects the head of a wood, hybrid or putter in the bag; also called a clubhead cover.', GE, 'clubhead cover'),
 'Divot repair tool': nk('Divot repair tool', 'Small forked tool for repairing ball marks on a green.', GE, 'pitch repairer · ball mark repair tool'),
 'Australian rules football': nk('Australian rules football', 'Oval leather or synthetic ball used in Australian rules football, kicked and handballed rather than thrown.', Wk('Sherrin'), 'Aussie rules ball', x=[
    arch('Sherrin football', 'Ball made by the Sherrin company, founded in Collingwood in 1880, and the official ball of the Australian Football League.', 'Sherrin', '1880', Wk('Sherrin'), dt='size · match or training grade')]),
 'Baseball': nk('Baseball', 'Sphere with a rubber or cork core wound in yarn and covered in leather, 9 to 9.25 inches round.', Wk('Baseball_(ball)'), 'baseball ball'),
 'Release aid': nk('Release aid', 'Trigger device that lets an archer let go of the string without using the fingers, for more consistent arrow flight.', Wk('Release_aid'), 'archery release · release'),
 'Billiard ball set': nk('Billiard ball set', 'Matched set of cue balls and object balls: 16 for American pool, 22 for snooker, three for carom.', Wk('Billiard_ball'), 'pool balls · snooker balls'),
 'Bocce set': nk('Bocce set', 'Set of large balls and a small jack rolled at one another, the Italian cousin of boules.', Wk('Lawn_game'), 'bocce balls'),
 'Horseshoe set': nk('Horseshoe set', 'Set of pitching horseshoes and stakes, with the stakes traditionally 40 feet apart.', Wk('Horseshoes_(game)'), 'horseshoes'),
 'Kubb set': nk('Kubb set', 'Swedish lawn game of ten wooden blocks, a king and six throwing batons.', Wk('Kubb'), 'Viking chess'),
 'Mölkky set': nk('Mölkky set', 'Finnish throwing game: a wooden pin thrown at twelve numbered skittles.', Wk('M%C3%B6lkky'), 'molkky', x=[
    arch('Mölkky', 'Finnish skittles game invented in 1996 by Lahden Paikka, played by tossing one pin at twelve numbered skittles.', 'Lahden Paikka', '1996', Wk('M%C3%B6lkky'), dt='pin set · carry bag')]),
 'Fishing hook': nk('Fishing hook', 'Barbed or barbless hook that holds the bait or fly and the fish; the last link in the rig.', FT, 'hook · terminal tackle'),
 'Fishing float': nk('Fishing float', 'Buoyant marker on the line that shows a bite and sets the depth of the bait.', FT, 'bobber · float'),
 'Fishing sinker': nk('Fishing sinker', 'Weight that carries the bait down and holds it in place, from split shot to feeder weights.', FT, 'weight · sinker or feeder'),
 'Swivel and snap': nk('Swivel and snap', 'Small metal links that join line, leader and lure without twisting.', FT, 'swivel · split ring · snap'),
 'Ice fishing auger': nk('Ice fishing auger', 'Hand or powered drill that cuts the hole through the ice for fishing.', Wk('Ice_fishing'), 'ice auger'),
 'Tip-up': nk('Tip-up', 'Wood or plastic frame with a line spool and a flag that rises when a fish takes the bait through the ice.', Wk('Ice_fishing'), 'ice fishing tip-up'),
 'Ice fishing rod': nk('Ice fishing rod', 'Small, light rod used with jigs or lures that the angler lifts to move the bait under the ice.', Wk('Ice_fishing'), 'jigging rod'),
 'Ice fishing shelter': nk('Ice fishing shelter', 'Enclosure set up on the ice to block wind and cold, from pop-up tents to heated huts.', Wk('Ice_fishing'), 'shanty · ice hut'),
 'Bear canister': nk('Bear canister', 'Hard-sided container that keeps backpackers\' food from bears.', Wk('Bear_canister'), 'bear-resistant food container'),
 'Tricam': nk('Tricam', 'Passive climbing protection that works both as a nut and as a cam in pockets and flares.', Wk('Tricam'), 'passive cam', x=[
    arch('Tricam', 'Passive nut-and-cam device invented by Greg Lowe in 1973, first sold in 1981 and now made by C.A.M.P.', 'CAMP', '1973', Wk('Tricam'), dt='size 0.5 to 6 · sling colour')]),
 'Climbing hold': nk('Climbing hold', 'Shaped grip bolted to a climbing wall for the hands and feet, from jugs to volumes.', Wk('Climbing_hold'), 'hold · wall hold'),
 'Portaledge': nk('Portaledge', 'Deployable hanging tent that lets big-wall climbers sleep suspended on a cliff for several days.', Wk('Portaledge'), 'hanging tent'),
 'Diving weight belt': nk('Diving weight belt', 'Belt or integrated pockets carrying lead weight so the diver can descend and hold depth.', DE, 'weight system · weights'),
 'Dive light': nk('Dive light', 'Waterproof torch for night, cave and deep diving, from handheld to canister and backup lights.', DE, 'dive torch'),
 'Drysuit': nk('Drysuit', 'Sealed suit that keeps the diver dry over thermal undergarments, for cold water; a wetsuit lets water in.', DE, 'dry suit'),
 'Skimboard': nk('Skimboard', 'Finless board smaller than a surfboard, thrown onto wet sand and thin water before riding a wave back in.', Wk('Skimboarding'), 'skim board'),
 'Variometer': nk('Variometer', 'Flight instrument that shows climb and sink rate, with an audible signal, used by glider and paraglider pilots.', Wk('Variometer'), 'vario'),
 'Pole vault pole': nk('Pole vault pole', 'Flexible pole of fibreglass and carbon, rated by the vaulter weight it suits.', Wk('Pole_vault'), 'vaulting pole'),
 'Irish dance shoe': nk('Irish dance shoe', 'Soft ghillies, reel shoes and fibreglass-tipped hard shoes worn for Irish dance.', Wk('Irish_dance'), 'ghillies · jig shoes · reel shoes'),
 'Wooden dummy': nk('Wooden dummy', 'Wooden post with arms and a leg used to train Wing Chun and other southern Chinese kung fu.', Wk('Mook_jong'), 'mook jong · mu ren zhuang'),
}
# new archetypes on existing kinds
NEWARCH = {
 'Tennis racket': [
  arch('Wilson T2000', 'Steel-framed racket whose wire wraps round the frame to form the string loops; popularised by Jimmy Connors.', 'Wilson', 'late 1960s', Wk('Tennis_racket')),
  arch('Spalding Smasher', 'Early aluminium racket, introduced in 1968.', 'Spalding', '1968', Wk('Tennis_racket')),
  arch('Head Competition', 'Early composite racket without graphite, used by Arthur Ashe.', 'Head', '', Wk('Tennis_racket')),
  arch('Yonex R-7', 'First midsize graphite racket, popularised by Martina Navratilova.', 'Yonex', '', Wk('Tennis_racket'))],
}
SEE = {
 'Hakama': [['A1','Hakama','the garment itself; here the budo practice version']],
 'Camp bed': [['B1','Camp bed','same object, sleeping at home']],
 'Trail camera': [['D4','Trail camera','photographic use']],
 'Flying disc': [['E1','Toy flying disc','toy version']],
 'Fitness trampoline': [['E1','Garden trampoline','play version']],
 'Kayak paddle': [['G1','Kayak','the boat it drives']],
 'Kick scooter': [['G1','Electric kick scooter','powered version']],
 'Unicycle': [['G1','Electric unicycle','powered version']],
 'Cycling shoe': [['G1','Bicycle pedals','pedal fitting']],
 'Fencing sabre': [['E4','Sabre','live blade']],
 'Wushu practice weapon': [['E4','Wushu jian','live or display blade']],
 'Gaiters': [['A2','Hiking boot','boot worn with them']],
 'Distress flare': [['E4','Flare pistol','']] if False else [],
 'Wetsuit': [['E2','Drysuit','sealed alternative for cold water']],
 'Drysuit': [['E2','Wetsuit','flooded alternative']],
 'Skateboard': [['A2','Skate shoe','shoe made for it']],
 'Snowshoe': [['E2','Microspikes','lighter traction']],
 'Microspikes': [['E2','Snowshoe','flotation on deep snow']],
 'Ice axe': [['E2','Ice tool','technical climbing version']],
 'Ice tool': [['E2','Ice axe','walking and glacier version']],
 'Climbing nut': [['E2','Tricam','passive cam']],
 'Tricam': [['E2','Climbing nut','simpler passive protection']],
 'Pétanque boules': [['E2','Bocce set','Italian equivalent']],
 'Bocce set': [['E2','Pétanque boules','French equivalent']],
 'Hockey gloves': [['E2','Goalie blocker','goalie hand protection']],
 'Squash racket': [['E2','Racquetball racket','longer-handled court cousin']],
 'Camping stove': [['B5','Kettle','kettle for the home kitchen']],
}
SEE = {k: v for k, v in SEE.items() if v}

def clean_kind(k):
    k = copy.deepcopy(k)
    t = k.pop('t', None)
    return k

def build():
    placed = set()
    out = {'c': 'E2', 'rev': True, 'lead': CAT_LEAD, 'ax': CAT_AX, 'key': CAT_KEY, 'b': old.get('b', []), 'depts': []}
    demoted_log = {}
    renames = {}
    moves_out = []
    def getkind(name):
        if name in NEW:
            k = copy.deepcopy(NEW[name]); placed.add(name); return k
        src = None
        for o, nn in RENAME.items():
            if nn == name: src = o
        src = src or name
        k = clean_kind(K[src]); k['n'] = name; placed.add(src)
        # merges
        for om, kept in MERGE.items():
            if kept == name:
                mk = K[om]; placed.add(om)
                k.setdefault('x', []); k['x'] += [x for x in copy.deepcopy(mk.get('x', [])) if x['n'] not in DEMOTE.get(om, [])]
                for key in ('m', 'r'):
                    cur = [tuple(z) for z in k.get(key, [])]
                    for z in mk.get(key, []):
                        if tuple(z) not in cur: cur.append(tuple(z))
                    if cur: k[key] = [list(z) for z in cur]
                renames[om] = name
        if src != name: renames[src] = name
        # demote
        dn = DEMOTE.get(name, []) + (DEMOTE.get(src, []) if src != name else [])
        if dn and k.get('x'):
            keep = []
            for x in k['x']:
                if x['n'] in dn: demoted_log.setdefault(name, []).append(x['n'])
                else: keep.append(x)
            k['x'] = keep
        if name in NEWARCH: k.setdefault('x', []); k['x'] += NEWARCH[name]
        if not k.get('x'): k.pop('x', None)
        return k
    allb = {}
    for (dn, mode, note, srcs, t, ax, shelves) in DEPTS:
        bl = []
        for i in srcs:
            for b in old['depts'][i].get('b', []):
                if b['m'] not in [z['m'] for z in bl]: bl.append(b)
        dept = {'n': dn, 'mode': mode, 'note': note, 'b': bl, 't': t, 'ax': ax, 's': []}
        for (sn, st, sax, kinds) in shelves:
            sh = {'n': sn, 't': st}
            if sax: sh['ax'] = sax
            sh['k'] = []
            for kn in kinds:
                k = getkind(kn)
                if kn in TT:
                    k['tt'] = TT[kn]
                if kn in SEE: k['see'] = SEE[kn]
                sh['k'].append(k)
            dept['s'].append(sh)
        out['depts'].append(dept)
    # moved out
    for name, (to, dept) in MOVE_OUT.items():
        placed.add(name)
        moves_out.append({'to': to, 'dept': dept, 'kind': clean_kind(K[name])})
    placed.add('Terminal tackle'); renames['Terminal tackle'] = 'Fishing hook'
    missing = [n for n in K if n not in placed]
    return out, demoted_log, renames, moves_out, missing

NEWBRANDS = [
 {'n': 'Sherrin', 'c': 'Australia', 'f': '1880', 'seg': 'Heritage manufactory', 'kf': 'Australian rules footballs', 'd': 'Collingwood ball maker founded by Thomas W. Sherrin; official ball of the Australian Football League.', 'sig': ['Sherrin football'], 's': Wk('Sherrin')},
 {'n': 'Lahden Paikka', 'c': 'Finland', 'f': '', 'seg': 'Specialist', 'kf': 'Mölkky', 'd': 'Finnish company that invented the Mölkky throwing game in 1996.', 'sig': ['Mölkky'], 's': Wk('M%C3%B6lkky')},
]

if __name__ == '__main__':
    out, dl, rn, mv, missing = build()
    print('missing kinds:', missing)
    json.dump(out, open(R + 'work/STR_E2/E2.new.json', 'w'), ensure_ascii=False, indent=1)
    json.dump({'demoted': dl, 'renames': rn, 'moves': mv}, open(R + 'work/STR_E2/log.json', 'w'), ensure_ascii=False, indent=1)
    nk_ = sum(len(s['k']) for d in out['depts'] for s in d['s'])
    print(len(out['depts']), sum(len(d['s']) for d in out['depts']), nk_, sum(len(k.get('x', [])) for d in out['depts'] for s in d['s'] for k in s['k']))
    # kinds without tt
    print('no tt:', [k['n'] for d in out['depts'] for s in d['s'] for k in s['k'] if 'tt' not in k])
    print('tt without kind:', [n for n in TT if n not in {k['n'] for d in out['depts'] for s in d['s'] for k in s['k']}])
