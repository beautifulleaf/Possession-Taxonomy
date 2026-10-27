import json, os
W = 'https://en.wikipedia.org/wiki/'
def X(n, mk, y, s, d, v=(), a='', dt=''):
    x = {'n': n, 'a': a, 'd': d, 'mk': mk, 'y': y, 's': s if s.startswith('http') else W + s,
         'v': [dict(zip(('n', 'mk', 'y', 'd'), t)) for t in v]}
    if dt: x['dt'] = dt
    return x
Y, G = 'Yubico', 'Google'
key_x = [
 X('YubiKey', Y, '2008', 'YubiKey', 'Yubico\'s multi-protocol hardware key (FIDO, OTP, smart card), the reference personal security key.',
   [('YubiKey', Y, '2008', 'original'), ('YubiKey 2.0', Y, '2009', ''), ('YubiKey NEO', Y, '2012', 'sold to 2018'),
    ('YubiKey 4', Y, '2015', '4C USB-C version 2017'), ('YubiKey 5 Series', Y, '2018', 'current flagship: 5 NFC, 5C, 5C NFC, 5Ci, 5 Nano, 5C Nano'),
    ('YubiKey 5 FIPS Series', Y, '', 'FIPS-certified versions of the 5 Series'), ('YubiKey Bio - FIDO Edition', Y, '2021', 'fingerprint reader; USB-A and USB-C')],
   dt='USB-A, USB-C, Lightning · NFC · nano (stays in port) · FIPS'),
 X('Yubico Security Key', Y, '2018', 'YubiKey', 'Low-cost FIDO-only key from Yubico.',
   [('Security Key', Y, '2018', 'FIDO U2F/FIDO2'), ('Security Key NFC', Y, '2023', 'current'), ('Security Key C NFC', Y, '', 'USB-C')]),
 X('Google Titan Security Key', G, '2019', 'Titan_Security_Key', 'Google\'s FIDO security key, used to protect Google accounts.',
   [('Titan Bluetooth (T1/T2)', G, '', 'discontinued 2021'), ('Titan USB-A/NFC (K9T)', G, '', ''), ('Titan USB-C/NFC (YT1)', G, '', ''), ('Titan (K52T)', G, '2023', 'v2, stores up to 250 passkeys')]),
 X('Nitrokey', 'Nitrokey', '2015', 'Nitrokey', 'German open-source hardware and software security keys for encryption, signing and login.',
   [('Nitrokey Pro 2', 'Nitrokey', '', 'OpenPGP'), ('Nitrokey Start', 'Nitrokey', '', ''), ('Nitrokey Storage 2', 'Nitrokey', '', 'with encrypted storage'), ('Nitrokey FIDO2', 'Nitrokey', '', ''), ('Nitrokey 3', 'Nitrokey', '', 'current')]),
 X('SoloKeys Solo', 'SoloKeys', '', 'https://solokeys.com/collections/solo-2-secure', 'FIDO2 key whose firmware is published for developers.',
   [('Solo 2 USB-A', 'SoloKeys', '', ''), ('Solo 2C', 'SoloKeys', '', 'USB-C'), ('Solo 2A+ NFC', 'SoloKeys', '', ''), ('Solo 2C+ NFC', 'SoloKeys', '', '')]),
 X('Feitian ePass FIDO', 'Feitian', '', 'https://fido.ftsafe.com/products-epass-fido/', 'Inexpensive FIDO key range sold in many casings.',
   [('ePass FIDO K8', 'Feitian', '', ''), ('ePass FIDO K9', 'Feitian', '', ''), ('ePass FIDO A4B', 'Feitian', '', 'USB-A')]),
]
# K9 not on page; fix below
key_x[-1]['v'] = [v for v in key_x[-1]['v'] if v['n'] != 'ePass FIDO K9'] + [{'n': 'ePass FIDO K10', 'mk': 'Feitian', 'y': '', 'd': ''}]
T, L = 'Trezor', 'Ledger'
hw_x = [
 X('Trezor', T, '2014', 'https://coindesk.com/learn/trezor', 'The first Bitcoin hardware wallet, from SatoshiLabs; open-source design.',
   [('Trezor Model One', T, '2014', 'two buttons and a screen'), ('Trezor Model T', T, '', 'touchscreen'), ('Trezor Safe 3', T, '', ''), ('Trezor Safe 5', T, '', ''), ('Trezor Safe 7', T, '', '')]),
 X('Ledger Nano', L, '2016', 'https://fortune.com/ranking/crypto/2023/ledger', 'Ledger\'s USB-stick-sized hardware wallet line, the best-selling family.',
   [('Nano S', L, '2016', 'first Ledger wallet'), ('Nano X', L, '2019', ''), ('Nano S Plus', L, '', ''), ('Nano Gen5', L, '', '')]),
 X('Ledger Stax', L, '2022', 'https://fortune.com/ranking/crypto/2023/ledger', 'Ledger wallet designed with Tony Fadell.',
   [('Ledger Stax', L, '2022', ''), ('Ledger Flex', L, '', 'smaller E Ink sibling')]),
 X('Coldcard', 'Coinkite', '', 'https://athenaalpha.substack.com/p/coldcard-mk4-review-2024-pros-cons', 'Bitcoin-only hardware wallet built for air-gapped signing.',
   [('Coldcard Mk3', 'Coinkite', '', ''), ('Coldcard Mk4', 'Coinkite', '2022', 'microSD and NFC signing')]),
 X('BitBox02', 'Shift Crypto', '', 'https://www.spark.money/tools/coldcard-vs-bitbox-comparison', 'USB-C hardware wallet with open-source hardware, in Bitcoin-only and multi-coin editions.',
   [('BitBox02 Bitcoin-only', 'Shift Crypto', '', ''), ('BitBox02 Multi', 'Shift Crypto', '', '')]),
]
for x in hw_x:
    if x['n'] == 'Ledger Stax': x['v'][1]['d'] = ''
kinds = [
 {'n': 'Security key', 'a': 'hardware security key · FIDO key · U2F key · passkey key', 'd': 'Small device plugged in or tapped to prove identity when signing in.',
  't': ['USB-A', 'USB-C', 'NFC', 'biometric'], 's': 'https://yubico.com:443/products/security-key', 'x': key_x},
 {'n': 'Hardware wallet', 'a': 'cold wallet · crypto wallet', 'd': 'Device that holds cryptocurrency keys offline and signs transactions.',
  't': ['USB', 'Bluetooth', 'air-gapped (QR / microSD)', 'Bitcoin-only', 'multi-coin'], 's': 'https://shop.ledger.com/pages/hardware-wallet', 'x': hw_x},
]
K = 'knowledge'
def B(n, c, f, seg, kf, d, s=K, **kw):
    b = {'n': n, 'c': c, 'f': f, 'seg': seg, 'kf': kf, 'd': d, 's': s}; b.update(kw); return b
brands = [
 B(Y, 'Sweden', '2007', 'Professional & flagship', 'security keys', 'Stockholm maker of the YubiKey, founded by Jakob and Stina Ehrensvärd.', W + 'YubiKey', lines=['YubiKey 5', 'YubiKey Bio', 'Security Key'], sig=['YubiKey']),
 B(G, 'United States', '1998', 'Premium', 'search, Pixel', 'American technology company that sells the Titan Security Key.', sig=['Google Titan Security Key']),
 B('Nitrokey', 'Germany', '2015', 'Specialist', 'open-source keys', 'German maker of open-source security keys.', W + 'Nitrokey', sig=['Nitrokey']),
 B('SoloKeys', '', '', 'Artisan & independent', 'open FIDO2 keys', 'Small maker of FIDO2 security keys with published firmware.', 'https://solokeys.com/collections/solo-2-secure', sig=['SoloKeys Solo']),
 B('Feitian', 'China', '', 'Value', 'FIDO keys', 'Chinese maker of authentication hardware.', 'https://fido.ftsafe.com/products-epass-fido/', sig=['Feitian ePass FIDO']),
 B(T, 'Czech Republic', '2013', 'Professional & flagship', 'hardware wallets', 'Hardware wallet brand of SatoshiLabs, founded by Pavol Rusnak and Marek Palatinus.', 'https://coindesk.com/learn/trezor', sig=['Trezor']),
 B(L, 'France', '2014', 'Professional & flagship', 'hardware wallets', 'Paris maker of the Nano and Stax hardware wallets.', 'https://fortune.com/ranking/crypto/2023/ledger', lines=['Nano', 'Stax', 'Flex'], sig=['Ledger Nano', 'Ledger Stax']),
 B('Coinkite', 'Canada', '2012', 'Specialist', 'Bitcoin-only wallets', 'Canadian maker of the Coldcard Bitcoin hardware wallet.', 'https://athenaalpha.substack.com/p/coldcard-mk4-review-2024-pros-cons', sig=['Coldcard']),
 B('Shift Crypto', '', '', 'Specialist', 'BitBox wallets', 'Maker of the BitBox02 hardware wallet.', 'https://www.spark.money/tools/coldcard-vs-bitbox-comparison', sig=['BitBox02']),
]
out = {'kinds': kinds, 'brands': brands, 'traditions': [],
 'notes': 'Security key: 16 old Yubico SKUs (each 5-series form factor and its FIPS twin) folded into YubiKey and Yubico Security Key archetypes with form factors as detail; added Titan, Nitrokey, SoloKeys, Feitian. Hardware wallet: 10 old models became versions of Trezor, Ledger Nano and Ledger Stax; Coldcard and BitBox02 added. Keystone left out (no page fetched). Trezor Model T / Safe and Ledger Nano S Plus / Gen5 / Flex years unconfirmed, left blank.'}
p = '/home/user/Possession-Taxonomy/rebuild/work/D1/shelves/03_03.json'
json.dump(out, open(p + '.tmp', 'w'), ensure_ascii=False, indent=1); os.replace(p + '.tmp', p)
print('written')
