"""F4 Religious & Ceremonial: regroup by object form first, faith tradition as a tag (owner 2026-10-28).
Lossless: every kind keeps its archetypes, models and sources; the old faith department becomes a `tg` tag.
Usage: python3 tools/f4_form_first.py   (rewrites out/F4.json; backup in bak/)"""
import json, os, shutil, time
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = 'out/F4.json'
os.makedirs('bak', exist_ok=True)
shutil.copy(SRC, f'bak/F4.{time.strftime("%Y%m%d%H%M%S")}.json')
d = json.load(open(SRC))

TAG = {'Christian': 'Christian', 'Jewish (Judaica)': 'Jewish', 'Islamic': 'Islamic', 'Buddhist': 'Buddhist'}
SHELF_TAG = {'Hindu puja': 'Hindu', 'Shinto': 'Shinto', 'Daoist & Chinese folk religion': 'Daoist & Chinese folk'}
kinds, oldb = {}, {}
for dp in d['depts']:
    oldb[dp['n']] = dp.get('b') or []
    for s in dp['s']:
        for k in s['k']:
            tag = TAG.get(dp['n']) or SHELF_TAG.get(s['n'])
            if s['n'] == 'Sikh & Jain':
                tag = 'Jain' if k['n'] == 'Siddhachakra yantra' else 'Sikh'
            if tag:
                k['tg'] = [t for t in (k.get('tg') or []) if t != tag] + [tag]
            kinds[k['n']] = k

def b(*pairs):  # criteria carried over from the old faith departments: (old dept, index)
    return [oldb[dn][i] for dn, i in pairs]

PLAN = [
 ('Images, altars & shrines', 'variety', 'Sacred images and the home altars that hold them, across traditions; the tradition is a tag on each kind.',
  b(('Christian', 0), ('Christian', 2), ('Christian', 3), ('Buddhist', 1)), [
  ('Crosses, statues & images', ['Crucifix & devotional cross', 'Icon', 'Devotional statue', 'Murti', 'Buddha image', 'Thangka & scroll painting', 'Calligraphy wall panel', 'Khanda emblem', 'Siddhachakra yantra', 'Tsa-tsa', 'Nativity set']),
  ('Home altars & shrines', ['Home altarpiece & triptych', 'Home mandir', 'Butsudan', 'Kamidana', 'Household deity altar', 'Palki sahib', 'Miniature stupa', 'Prie-dieu']),
  ('Relics & reliquaries', ['Reliquary', 'Relic'])]),
 ('Prayer & devotion aids', 'variety', 'Objects held, worn, sounded or hung during prayer.',
  b(('Hindu, Sikh & Jain', 0), ('Islamic', 2), ('Islamic', 0), ('Islamic', 1), ('Shinto, Daoist & Chinese folk', 0)), [
  ('Prayer beads', ['Rosary', 'Prayer rope', 'Tasbih', 'Mala', 'Juzu']),
  ('Prayer mats, shawls & cloths', ['Prayer rug', 'Tallit', 'Rumala', 'Khata', 'Prayer flag', 'Shrine rope']),
  ('Bells, wheels & sound instruments', ['Prayer wheel', 'Standing bowl bell', 'Altar hand bell', 'Mokugyo', 'Tingsha', 'Damaru', 'Shankha', 'Shofar']),
  ('Medals, charms & talismans', ['Devotional medal', 'Scapular', 'Holy card', 'Protective charm', 'Ofuda', 'Ema', 'Daoist talisman', 'Bagua mirror']),
  ('Articles of faith worn', ['Tefillin', 'Kara', 'Kirpan', 'Kanga'])]),
 ('Scriptures, scrolls & holders', 'variety', 'Sacred texts as objects and the cases, stands and ornaments made for them; text editions belong to the Literature taxonomy.',
  b(('Jewish (Judaica)', 0), ('Jewish (Judaica)', 1), ('Jewish (Judaica)', 2)), [
  ('Scrolls & documents', ['Torah scroll', 'Mezuzah scroll', 'Ketubah']),
  ('Cases, stands & ornaments', ['Mezuzah case', 'Rehal', "Qur'an box & cover", 'Torah finials', 'Torah pointer'])]),
 ('Ritual vessels & implements', 'variety', 'Cups, plates and tools used in rites at home or in worship.',
  b(('Hindu, Sikh & Jain', 1), ('Hindu, Sikh & Jain', 2), ('Jewish (Judaica)', 3)), [
  ('Cups, plates & offering vessels', ['Chalice', 'Host vessel', 'Monstrance', 'Kiddush cup', 'Seder plate', 'Challah board & cover', 'Ritual washing cup', 'Etrog box', 'Spice box', 'Kalash', 'Puja thali', 'Offering vessel', 'Offering stand', 'Mandala offering set', 'Alms box']),
  ('Holy-water goods', ['Holy-water font', 'Holy-water bottle', 'Aspergillum']),
  ('Ritual tools & blades', ['Ritual spoon or ladle', 'Havan kund', 'Dorje (vajra)', 'Phurba', 'Kartika', 'Chaur sahib', 'Paper-streamer wand', 'Peach-wood sword', 'Qibla compass'])]),
 ('Light, incense & offerings', 'mixed', 'Lamps, candles, incense and burnt offerings; variety at the incense-connoisseur end, tier for everyday candles.',
  oldb['Incense, candles & offerings'], [
  ('Lamps & candleholders', ['Hanukkah lamp', 'Seven-branch menorah', 'Shabbat candlesticks', 'Altar candlestick', 'Sanctuary lamp & lampada', 'Oil lamp for worship', 'Ramadan lantern', 'Ritual lantern']),
  ('Candles & wreaths', ['Devotional candle', 'Paschal candle', 'Havdalah candle', 'Yahrzeit candle', 'Advent wreath']),
  ('Incense & burners', ['Ritual incense', 'Incense burner', 'Thurible & hand censer']),
  ('Paper offerings', ['Joss paper'])]),
 ('Tarot & divination', 'variety', None, oldb['Tarot & divination'], [
  ('Tarot & oracle decks', ['Tarot deck', 'Lenormand deck', 'Oracle deck']),
  ('Divination tools', ['Spirit board', 'Rune set', 'I Ching set', 'Kau cim', 'Jiaobei', 'Omikuji', 'Crystal ball', 'Scrying mirror', 'Divination pendulum', 'Dowsing rod']),
  ('Ritual-magic tools', ['Athame', 'Altar pentacle'])]),
 ('Funeral & memorial', 'tier', None, oldb['Funeral & memorial'], [
  ('Coffins, urns & grave markers', ['Coffin', 'Burial shroud', 'Cremation urn', 'Urn vault', 'Grave marker']),
  ('Home memorials & ancestor tablets', ['Memorial tablet', 'Ancestral tablet', 'Memorial register'])]),
]
old_note = {dp['n']: dp.get('note') for dp in d['depts']}
used, depts = set(), []
for name, mode, note, crit, shelves in PLAN:
    dp = {'n': name, 'mode': mode, 'note': note or old_note.get(name), 'b': crit, 's': []}
    for sn, names in shelves:
        dp['s'].append({'n': sn, 'k': [kinds[n] for n in names]})
        used.update(names)
    if not dp['note']: del dp['note']
    depts.append(dp)
left = set(kinds) - used
assert not left, f'unplaced kinds: {sorted(left)}'
d['depts'] = depts
d['lead'] = ('Objects owned for worship, devotion, divination and mourning, grouped by what the object is '
             '(images and altars, prayer aids, scriptures and holders, ritual vessels and tools, light and incense, '
             'divination, funeral goods); the faith tradition is a tag on each kind, and practices belong to the Spiritual pursuits taxonomy.')
tmp = SRC + '.tmp'
json.dump(d, open(tmp, 'w'), ensure_ascii=False, separators=(',', ':'))
os.replace(tmp, SRC)
print('kinds', len(kinds), 'depts', len(depts), 'tagged', sum(1 for k in kinds.values() if k.get('tg')))
