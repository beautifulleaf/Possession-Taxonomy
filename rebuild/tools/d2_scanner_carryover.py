"""Carry radio-scanner models from D3 (removed there; D2 is the home) into D2's Radio scanner kind.
Usage: python3 tools/d2_scanner_carryover.py   (rewrites out/D2.json; backup in bak/)"""
import json, os, shutil, time
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
shutil.copy('out/D2.json', f'bak/D2.json.{time.strftime("%Y%m%d%H%M%S")}')
d = json.load(open('out/D2.json'))
k = next(k for dp in d['depts'] for s in dp['s'] for k in s['k'] if k['n'] == 'Radio scanner')
add = [['BC125AT', 'Uniden'], ['BCD436HP', 'Uniden'], ['SDS100', 'Uniden'], ['SDS200', 'Uniden'], ['HomePatrol-2', 'Uniden'], ['WS1010', 'Whistler']]
k['m'] = (k.get('m') or []) + [m for m in add if m not in (k.get('m') or [])]
k['t'] = list(dict.fromkeys((k.get('t') or []) + ['handheld', 'base or mobile', 'analogue', 'digital trunking']))
json.dump(d, open('out/D2.json.tmp', 'w'), ensure_ascii=False, separators=(',', ':')); os.replace('out/D2.json.tmp', 'out/D2.json')
print(len(k['m']), k['t'])
