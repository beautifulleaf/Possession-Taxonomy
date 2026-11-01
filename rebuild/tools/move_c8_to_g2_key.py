"""Second half of the 2026-11-01 C8 -> G2 move (see tools/move_c8_to_g2.py): moves the three key steps."""
import json, os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
c8, g2 = (json.load(open(f'{R}/out/{c}.json')) for c in ('C8', 'G2'))
body = lambda k: re.sub(r'^\d+\.\s*', '', k)
c8k = [k for k in c8['key'] if not re.search(r'→ (Heritage & reclaimed materials|Masonry, roofing & insulation|Timber & sheet materials)$', k)]
c8k = [k.replace('a period or reclaimed item (zellige, reclaimed brick, chimney pot) goes to Heritage before its modern equivalent; ', 'building materials (timber, masonry, roofing, insulation, heritage and reclaimed materials) are Property &amp; Structures; ') for k in c8k]
c8['key'] = [f'{i + 1}. {body(k)}' if re.match(r'^\d+\.', k) else k for i, k in enumerate(c8k)]
steps = [k for k in g2['key'] if re.match(r'^\d+\.', k)]; notes = [k for k in g2['key'] if not re.match(r'^\d+\.', k)]
new = ['Is it a lime, earth or distemper finish, a regional period tile, or a salvaged building part? → Heritage & reclaimed materials',
       'Is it brick, block, cement, a roof covering, insulation or a flue? → Masonry, roofing & insulation',
       'Is it timber, a board, a metal section or a moulding? → Timber & sheet materials']
steps = steps[:5] + new + steps[5:]
notes = [n.replace('bare farmland step 4.', 'bare farmland step 4; a whole building is steps 1–5, the material it is built from steps 6–8, and a period or reclaimed item (zellige, reclaimed brick, chimney pot) is step 6 before its modern equivalent.') for n in notes]
g2['key'] = [f'{i + 1}. {body(k)}' for i, k in enumerate(steps)] + notes
for c, o in (('C8', c8), ('G2', g2)): json.dump(o, open(f'{R}/out/{c}.json', 'w'), ensure_ascii=False, indent=1)
print('C8', len(c8['key']), 'G2', len(g2['key']))
