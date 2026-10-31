# executed inside build_part.py (shares E, V, add, addv, U)
U.update(dict(AK=WK + 'AKG_Acoustics', SE=WK + 'Sennheiser', EV=WK + 'Electro-Voice', AH=WK + 'Allen_%26_Heath', FZ=WK + 'Fazioli',
              KW=WK + 'Kawai_Musical_Instruments', TE=WK + 'Teenage_Engineering', CL=WK + 'Clavia', AR=WK + 'Arturia', EL=WK + 'Elektron_(company)',
              NO=WK + 'Novation_Digital_Music_Systems', AKA=WK + 'Akai', NI=WK + 'Native_Instruments', EM=WK + 'E-mu_Systems', EN=WK + 'Ensoniq',
              KU=WK + 'Kurzweil_Music_Systems', TS=WK + 'Technics_SL-1200', PD=WK + 'Pioneer_DJ', BE=WK + 'Behringer', AT=WK + 'Audio-Technica',
              AL=WK + 'Alesis', UA=WK + 'Universal_Audio_(company)', ZO=WK + 'Zoom_Corporation', FO=WK + 'Focusrite', ZIL='https://zildjian.com/pages/cymbal-category',
              CA=WK + 'Casio', GR=WK + 'Gretsch', SO=WK + 'Sonor', P5=WK + 'Sequential_Circuits_Prophet-5', DX=WK + 'Yamaha_DX7', MM=WK + 'Minimoog',
              T8=WK + 'Roland_TR-808', LM=WK + 'Linn_LM-1', SM58=WK + 'Shure_SM58', U47=WK + 'Neumann_U_47'))
MON, POL = 'Monophonic synthesizer', 'Polyphonic synthesizer'
# ---- Korg (List of Korg products, windows 0-135000 read; non-instrument rows such as tuners, effects, software out of scope)
add(POL,
    E('Korg Trident', 'Korg', '1980', 'Korg synthesizer of 1980.', 'KO'),
    E('Korg Sigma / Lambda / Delta', 'Korg', '1979–1980', 'Korg synthesizers of 1979 to 1980.', 'KO', v=[V('Sigma', 'Korg', '1979'), V('Lambda', 'Korg', '1979'), V('Delta', 'Korg', '1979')]),
    E('Korg PS-3300', 'Korg', '1977', 'Patchable polyphonic Korg synthesizer; the PS-3100 and PS-3200 date from the same year.', 'KO', v=[V('PS-3100', 'Korg', '1977'), V('PS-3200', 'Korg', '1977')]),
    E('Korg PE-2000', 'Korg', '1976', 'Korg polyphonic preset synthesizer, with the PE-1000.', 'KO', v=[V('PE-1000', 'Korg', '1976')]),
    E('Korg 770', 'Korg', '1977', 'Korg synthesizer of 1977.', 'KO'),
    E('Korg M-500 Micro Preset', 'Korg', '1977', 'Korg preset synthesizer of 1977.', 'KO'),
    E('Korg 900PS', 'Korg', '1975', 'Korg preset synthesizer of 1975.', 'KO'),
    E('Korg 707', 'Korg', '1987', 'Korg FM synthesizer of 1987.', 'KO'),
    E('Korg T series', 'Korg', '1989', 'Korg workstation improving on the M1: T1, T2 and T3.', 'KO', v=[V('T1', 'Korg', '1989'), V('T2', 'Korg', '1989'), V('T3', 'Korg', '1989')]),
    E('Korg 01/W', 'Korg', '1991', 'Korg PCM workstation of 1991; variants include 01/W ProX, 01/Wfd, 01/W-Pro and 01R/W.', 'KO'),
    E('Korg X3', 'Korg', '1993', 'Korg workstation of 1993 in keyboard (X3), mid-size (X2) and rack (X3R) versions.', 'KO', v=[V('X2', 'Korg', '1993'), V('X3R', 'Korg', '1993')]),
    E('Korg X5', 'Korg', '1994', 'Korg synthesizer workstation of 1994; the X5D and X5DR sound modules followed in 1995.', 'KO', v=[V('X5D / X5DR', 'Korg', '1995')]),
    E('Korg Trinity', 'Korg', '1995', 'Korg workstation of 1995.', 'KO'),
    E('Korg N364 / N264', 'Korg', '1996', 'Korg workstation of 1996.', 'KO'),
    E('Korg N5 / N1', 'Korg', '1998', 'Korg synthesizers of 1998; the N1R was the module.', 'KO', v=[V('N1', 'Korg', '1998'), V('N1R', 'Korg', '1998')]),
    E('Korg Triton', 'Korg', '1999', 'Korg workstation of 1999 with the Triton Rack (2000), Studio (2001), LE (2002) and Extreme (2004).', 'KO',
      v=[V('Triton Rack', 'Korg', '2000'), V('Triton Studio', 'Korg', '2001'), V('Triton LE', 'Korg', '2002'), V('Triton Extreme', 'Korg', '2004')]),
    E('Korg OASYS', 'Korg', '2005', 'Korg workstation of 2005.', 'KO'),
    E('Korg TR', 'Korg', '2006', 'Korg workstation of 2006.', 'KO'),
    E('Korg Radias', 'Korg', '2006', 'Korg synthesizer of 2006.', 'KO'),
    E('Korg MicroX / X50', 'Korg', '2006', 'Korg compact workstations of 2006.', 'KO', v=[V('MicroX', 'Korg', '2006'), V('X50', 'Korg', '2006')]),
    E('Korg M3', 'Korg', '2007', 'Korg workstation of 2007; the M50 followed in 2008.', 'KO', v=[V('M50', 'Korg', '2008')]),
    E('Korg R3', 'Korg', '2007', 'Korg synthesizer of 2007.', 'KO'),
    E('Korg PS60', 'Korg', '2010', 'Korg synthesizer of 2010.', 'KO'),
    E('Korg Microstation', 'Korg', '2010', 'Korg workstation of 2010.', 'KO'),
    E('Korg Krome', 'Korg', '2012', 'Korg workstation of 2012; the Krome EX followed in 2019.', 'KO', v=[V('Krome Platinum', 'Korg', '2017'), V('Krome EX', 'Korg', '2019')]),
    E('Korg Nu:Tekt', 'Korg', '2019', 'Korg synthesizer of 2019.', 'KO'),
    E('Korg Nautilus', 'Korg', '2020', 'Korg workstation of 2020; the Nautilus AT followed in 2023.', 'KO', v=[V('Nautilus AT', 'Korg', '2023')]))
addv(POL, 'Korg Wavestation', V('Wavestation EX', 'Korg', '1991'), V('Wavestation A/D', 'Korg', '1991'), V('Wavestation SR', 'Korg', '1992'))
add(MON,
    E('Korg MS-10', 'Korg', '1978', 'Korg semi-modular synthesizer of 1978 beside the MS-20, MS-50 and SQ-10.', 'KO', v=[V('MS-50', 'Korg', '1978'), V('SQ-10', 'Korg', '1978')]),
    E('Korg Kaossilator', 'Korg', '2007', 'Korg dynamic phrase synthesizer of 2007, followed by the Kaossilator Pro (2010) and Kaossilator 2 (2012).', 'KO',
      v=[V('Kaossilator Pro', 'Korg', '2010'), V('Kaossilator 2', 'Korg', '2012'), V('Kaossilator Pro+', 'Korg', '2013'), V('Kaossilator 2S', 'Korg', '2015')]),
    E('Arturia MiniBrute', 'Arturia', '2012', 'Arturia analogue monosynth of 2012; the MicroBrute followed in 2013.', 'AR', v=[V('MicroBrute', 'Arturia', '2013')]),
    E('Novation Bass Station', 'Novation', '1993', 'Novation analogue monosynth of 1993.', 'NO'),
    E('Behringer Model D', 'Behringer', '', 'Behringer clone of the Minimoog; the Poly D was announced on 27 November 2019.', 'BE', v=[V('Poly D', 'Behringer', '2019')]),
    E('Behringer Pro-1', 'Behringer', '', 'Behringer clone of the Sequential Pro-One.', 'BE'),
    E('Behringer Neutron', 'Behringer', '2018', 'Behringer original semi-modular synthesizer, 2018 onwards.', 'BE'))
add(POL,
    E('Novation Supernova', 'Novation', '1998', 'Novation virtual-analogue synthesizer of 1998.', 'NO'),
    E('Novation Peak', 'Novation', '2017', 'Novation polyphonic synthesizer of 2017.', 'NO'),
    E('Nord Lead', 'Clavia', '1995', 'Clavia virtual-analogue synthesizer: Lead 1995, Lead 2 1997, Lead 3 2001, then Lead 2x, A1 and Lead 4.', 'CL',
      v=[V('Nord Lead 2', 'Clavia', '1997'), V('Nord Lead 3', 'Clavia', '2001'), V('Nord Lead 2x', 'Clavia'), V('Nord Lead 4', 'Clavia'), V('Nord Lead A1', 'Clavia')]),
    E('Nord Wave', 'Clavia', '2007', 'Clavia synthesizer of 2007; the Wave 2 is current.', 'CL', v=[V('Nord Wave 2', 'Clavia')]),
    E('Akai AX80', 'Akai Professional', '1984', 'Akai analogue synthesizer of 1984.', 'AKA'),
    E('Ensoniq ESQ-1', 'Ensoniq', '1986', 'Ensoniq digital-wave synthesizer of 1986; the SQ-80 followed in 1988.', 'EN', v=[V('SQ-80', 'Ensoniq', '1988')]),
    E('Ensoniq VFX', 'Ensoniq', '1989', 'Ensoniq synthesizer of 1989; the TS-10 followed in 1992.', 'EN', v=[V('TS-10', 'Ensoniq', '1992')]),
    E('Kurzweil K2000', 'Kurzweil', '1991', 'Kurzweil synthesizer-sampler of 1991; the K2500 (1995–1996), K2600 (1999) and K2700 (2021) followed.', 'KU',
      v=[V('K2500', 'Kurzweil', '1995'), V('K2600', 'Kurzweil', '1999'), V('K2661', 'Kurzweil', '2004'), V('K2700', 'Kurzweil', '2021')]),
    E('Kurzweil K1000', 'Kurzweil', '', 'Kurzweil sound keyboard named in the Kurzweil article; the K1200 and K150 sit beside it.', 'KU', v=[V('K1200', 'Kurzweil'), V('K150', 'Kurzweil')]))
addv(POL, 'Roland Jupiter-8', V('Jupiter-8 (Wikipedia Jupiter page)', 'Roland', '1981', 'Listed with the Jupiter-4 (1978) and Jupiter-6 (1983)'))
# Prophet-5 etc existing; DX7 versions
addv(POL, 'Yamaha DX7', V('TX7', 'Yamaha', '1985', 'Desktop module'), V('DX7II', 'Yamaha', '1987'), V('Reface DX', 'Yamaha', '2015', 'Smaller successor'))
addv(POL, 'Sequential Prophet-5', V('Prophet-5 (first shipment)', 'Sequential', '1978', 'Shipped after a January 1978 NAMM demonstration'))
# Korg organs, arrangers, pianos, controllers
add('Electronic organ',
    E('Korg KORGUE', 'Korg', '1972', 'Korg synthesizer organ of 1972, after the Prototype No.1 of 1970.', 'KO', v=[V('Prototype No.1', 'Korg', '1970')]),
    )
add('Portable keyboard',
    E('Korg SAS-20', 'Korg', '1983', 'Korg arranger keyboard of 1983.', 'KO'),
    E('Korg i-series arrangers', 'Korg', '1993', 'Korg arrangers 1993 to 1999: i3, i2, i1, i4S, i5S, i5M, ih, iX300, iS40, iS50, i30, i40M and iS35.', 'KO',
      v=[V(n, 'Korg', y) for n, y in [('i3', '1993'), ('i2', '1994'), ('i1', '1995'), ('i4S', '1995'), ('i5S', '1995'), ('i5M', '1995'), ('ih', '1995'), ('iX300', '1997'), ('iS40', '1998'), ('iS50', '1998'), ('i30', '1998'), ('i40M', '1999'), ('iS35', '1999')]]),
    E('Korg Pa series', 'Korg', '2000', 'Korg professional arrangers from the Pa80 (2000): Pa60, Pa1X, Pa50, Pa800, Pa2X Pro, Pa500, Pa588, Pa3X, Pa4X, Pa300, Pa900, Pa600, PA1000, PA700, Pa5x.', 'KO',
      v=[V(n, 'Korg', y) for n, y in [('Pa80', '2000'), ('Pa60', '2002'), ('Pa1X', '2004'), ('Pa800', '2006'), ('Pa2X Pro', '2007'), ('Pa500', '2008'), ('PA3X', '2011'), ('Pa300', '2014'), ('PA4X', '2015'), ('PA1000', '2017'), ('PA700', '2017'), ('Pa5x', '2022')]]),
    E('Korg microARRANGER', 'Korg', '2011', 'Compact Korg arranger of 2011.', 'KO'))
add('Digital piano',
    E('Korg SP series', 'Korg', '1999', 'Korg digital pianos: SP-100 (1999), SP170 (2010) and SP-280 (2013).', 'KO', v=[V('SP-100', 'Korg', '1999'), V('SP170', 'Korg', '2010'), V('SP-280', 'Korg', '2013')]),
    E('Korg Havian 30', 'Korg', '2015', 'Korg home piano of 2015.', 'KO'),
    E('Nord Stage', 'Clavia', '2005', 'Clavia stage keyboard of 2005, followed by Stage 2, 2EX, 3 and 4.', 'CL', v=[V('Nord Stage 2', 'Clavia'), V('Nord Stage 3', 'Clavia'), V('Nord Stage 4', 'Clavia')]),
    E('Nord Piano', 'Clavia', '2010', 'Clavia stage piano of 2010 with Piano 2 to 5.', 'CL', v=[V('Nord Piano 2', 'Clavia'), V('Nord Piano 3', 'Clavia'), V('Nord Piano 4', 'Clavia'), V('Nord Piano 5', 'Clavia')]),
    E('Kurzweil PC3', 'Kurzweil', '2008', 'Kurzweil performance controller of 2008; PC3K 2011, Artis 2013 and Forte 2014 followed.', 'KU', v=[V('PC3K', 'Kurzweil', '2011'), V('Artis', 'Kurzweil', '2013'), V('Forte', 'Kurzweil', '2014')]),
    E('Kawai Shigeru Kawai grands', 'Kawai', '1999', 'Kawai flagship grand series from 1999; the SK-EX concert grand dates from 2001.', 'KW'),
    E('Kawai ES series', 'Kawai', '', 'Kawai portable digital piano series; year not stated.', 'KW'),
    E('Kawai CA series', 'Kawai', '', 'Kawai Concert Artist digital piano series; year not stated.', 'KW'),
    E('Casio Privia', 'Casio', '', 'Casio digital piano series; the PX-S3100 is a current model.', 'CA', v=[V('PX-S3100', 'Casio')]),
    E('Casio Celviano', 'Casio', '', 'Casio home digital piano series; the Grand Hybrid is its hybrid line.', 'CA', v=[V('Grand Hybrid', 'Casio')]))
addv('Digital piano', 'Korg Kronos', V('Kronos SE', 'Korg', '2019'), V('Kronos 2', 'Korg', '2014'), V('Kronos 2 Platinum', 'Korg', '2016'), V('Kronos 2 Gold', 'Korg', '2017'))
add('Upright piano', E('Kawai K Series uprights', 'Kawai', '', 'Kawai professional upright series; the K 15 is one model.', 'KW', v=[V('K 15', 'Kawai')]))
add('Vocoder', E('Korg VC-10', 'Korg', '1978', 'Korg vocoder of 1978.', 'KO'))
add('Sampler',
    E('Korg microSampler', 'Korg', '2009', 'Korg compact sampler of 2009.', 'KO'),
    E('Akai S900', 'Akai Professional', '1986', 'Akai rack sampler of 1986; the S950 and S1000 followed in 1988.', 'AKA', v=[V('S950', 'Akai Professional', '1988'), V('S1000', 'Akai Professional', '1988')]),
    E('E-mu Emulator III', 'E-mu Systems', '1987', 'E-mu sampler of 1987.', 'EM'),
    E('E-mu SP-12', 'E-mu Systems', '1985', 'E-mu sampling drum machine of 1985, before the SP-1200.', 'EM'),
    E('E-mu Emax', 'E-mu Systems', '1986', 'E-mu sampler of 1986.', 'EM'),
    E('E-mu Proteus', 'E-mu Systems', '1989', 'E-mu sound module; the text gives 1990 for the first Proteus.', 'EM'),
    E('Ensoniq EPS', 'Ensoniq', '1988', 'Ensoniq sampling keyboard of 1988; the ASR-10 followed in 1992.', 'EN', v=[V('ASR-10', 'Ensoniq', '1992')]),
    E('Teenage Engineering EP-133 K.O. II', 'Teenage Engineering', '2023', 'Teenage Engineering sampler of 2023; EP-1320 Medieval (2024) and EP-40 Riddim (2025) followed.', 'TE',
      v=[V('EP-1320 Medieval', 'Teenage Engineering', '2024'), V('EP-40 Riddim', 'Teenage Engineering', '2025')]))
addv('Sampler', 'Akai MPC',
     V('MPC3000LE', 'Akai Professional', '1999'), V('MPC500', 'Akai Professional', '2006'), V('MPC2500', 'Akai Professional', '2005'), V('MPC5000', 'Akai Professional', '2008'),
     V('MPC Renaissance / MPC Studio', 'Akai Professional', '2012'), V('MPC Element', 'Akai Professional', '2013'), V('MPC Touch', 'Akai Professional', '2015'),
     V('MPC Live / MPC X', 'Akai Professional', '2017'), V('MPC Force', 'Akai Professional', '2019'), V('MPC One / MPC Live II', 'Akai Professional', '2020'),
     V('MPC Studio II', 'Akai Professional', '2021'), V('MPC Key 61', 'Akai Professional', '2022'), V('MPC One+', 'Akai Professional', '2023'),
     V('MPC Live III', 'Akai Professional', '2025'), V('MPC XL', 'Akai Professional', '2026'))
addv('Sampler', 'E-mu SP-1200', V('SP-12 (predecessor)', 'E-mu Systems', '1985'))
add('Groovebox',
    E('Teenage Engineering OP-Z', 'Teenage Engineering', '2018', 'Teenage Engineering synthesizer-sequencer of 2018.', 'TE'),
    E('Teenage Engineering OP-XY', 'Teenage Engineering', '2024', 'Teenage Engineering sequencer-synthesizer of 2024.', 'TE'),
    E('Elektron Digitone Keys', 'Elektron', '2018', 'Keyboard version of the Digitone, 2018.', 'EL'),
    E('Elektron Analog Keys', 'Elektron', '2013', 'Elektron keyboard synthesizer-sequencer of 2013.', 'EL'),
    E('Novation Launchpad', 'Novation', '2009', 'Novation grid controller of 2009.', 'NO'))
addv('Groovebox', 'Korg Volca series', V('Volca Sample', 'Korg', '2014'), V('Volca FM', 'Korg', '2016'), V('Volca Kick', 'Korg', '2016'), V('Volca Modular', 'Korg', '2019'), V('Volca Nubass', 'Korg', '2019'), V('Volca FM2', 'Korg', '2022'))
addv('Groovebox', 'Teenage Engineering OP-1', V('OP-1 Field', 'Teenage Engineering', '2022'), V('OP-1', 'Teenage Engineering', '2010'))
addv('Groovebox', 'Teenage Engineering Pocket Operator',
     V('PO-12 / PO-14 / PO-16', 'Teenage Engineering', '2015'), V('PO-20 / PO-24 / PO-28', 'Teenage Engineering', '2016'), V('PO-32 Tonic', 'Teenage Engineering', '2017'),
     V('PO-33 KO! / PO-35 speak', 'Teenage Engineering', '2018'), V('POM-16 / POM-170 / POM-400', 'Teenage Engineering', '2019'))
add('Drum machine',
    E('Alesis HR-16', 'Alesis', '1987', 'Alesis drum machine of 1987.', 'AL'),
    E('Behringer RD-6', 'Behringer', '', 'Behringer clone of the Roland TR-606.', 'BE'),
    E('Elektron Machinedrum', 'Elektron', '2002', 'Elektron drum machine of 2002.', 'EL'),
    E('Elektron Analog Rytm', 'Elektron', '2014', 'Elektron analogue drum machine of 2014.', 'EL'),
    E('Elektron Syntakt', 'Elektron', '2022', 'Elektron drum and synth machine of 2022.', 'EL'),
    E('Korg Volca Beats', 'Korg', '2013', 'Korg drum machine of 2013, in the Volca series.', 'KO'))
add('Step sequencer', E('Arturia KeyStep', 'Arturia', '2016', 'Arturia keyboard controller and sequencer of 2016.', 'AR'))
add('MIDI keyboard controller',
    E('Arturia KeyStep', 'Arturia', '2016', 'Arturia keyboard controller and sequencer of 2016; the KeyStep Pro is its larger sibling.', 'AR', v=[V('KeyStep Pro', 'Arturia')]),
    E('Novation Launchkey', 'Novation', '2013', 'Novation controller keyboard of 2013; the SL MkIII followed in 2018.', 'NO', v=[V('SL MkIII', 'Novation', '2018')]),
    E('Akai MPK', 'Akai Professional', '2007', 'Akai controller keyboard series: MPK49 2007, MPK25/61/88 2009, MPK Mini MK II 2014, MPK Mini MK III 2020.', 'AKA',
      v=[V('MPK49', 'Akai Professional', '2007'), V('MPK25 / MPK61 / MPK88', 'Akai Professional', '2009'), V('MPK225 / MPK249 / MPK261', 'Akai Professional', '2014'), V('MPK Mini MK II', 'Akai Professional', '2014'), V('MPK Mini MK III', 'Akai Professional', '2020')]),
    E('Korg microKEY', 'Korg', '2010', 'Korg compact keyboard controller of 2010.', 'KO'),
    E('Korg nanoKEY / nano series', 'Korg', '2008', 'Korg nano series controllers of 2008; nanoSERIES 2 followed in 2011.', 'KO'),
    E('Korg Triton Taktile', 'Korg', '2014', 'Korg controller keyboard in 24 and 49 key sizes, 2014.', 'KO'))
add('Pad controller',
    E('Akai MPD', 'Akai Professional', '2002', 'Akai pad controllers: MPD16 2002, MPD24 2006, MPD32 2008, MPD26 2010.', 'AKA', v=[V('MPD16', 'Akai Professional', '2002'), V('MPD24', 'Akai Professional', '2006'), V('MPD32', 'Akai Professional', '2008'), V('MPD26', 'Akai Professional', '2010')]),
    E('Korg padKONTROL', 'Korg', '2006', 'Korg pad controller of 2006; the microKONTROL followed in 2003.', 'KO', v=[V('microKONTROL', 'Korg', '2003')]),
    E('Akai APC', 'Akai Professional', '', 'Akai Ableton clip launcher series: APC20, APC40 and APC40 MkII; years not stated.', 'AKA'))
add('Electronic percussion pad',
    E('Korg Wavedrum', 'Korg', '1994', 'Korg percussion instrument of 1994; Oriental, Mini and Global editions followed in 2011 to 2013.', 'KO',
      v=[V('Wavedrum Oriental', 'Korg', '2011'), V('Wavedrum Mini', 'Korg', '2011'), V('Wavedrum Global Edition', 'Korg', '2013')]),
    E('Nord Drum', 'Clavia', '2012', 'Clavia drum synthesizer of 2012, followed by Drum 2 and 3P.', 'CL', v=[V('Nord Drum 2', 'Clavia'), V('Nord Drum 3P', 'Clavia')]))
addv('Tonewheel organ', 'Hammond XK clonewheel line', V('XB-2 / XB-3 / XB-5', 'Hammond'), V('XK-3', 'Hammond', '2005', 'Sound on Sound review date'), V('SK1', 'Hammond', '2011', 'Keyboard review date'))
# ---- Keyboards (acoustic) from Fazioli / Kawai
addv('Grand piano', 'Fazioli F308', V('F308 prototype shown in public', 'Fazioli', '1987', 'Unveiled at NAMM in 1995'))
addv('Grand piano', 'Fazioli F278', V('F278 prototype', 'Fazioli', '1980', 'Completed late 1980'))
addv('Grand piano', 'Steinway Model D', V('Fibonacci limited edition', 'Steinway & Sons', '2015'))
addv('Player piano', 'Steinway Spirio', V('Spirio (introduced)', 'Steinway & Sons', '2015'), V('Spirio r', 'Steinway & Sons', '2018', 'Recording option added'))
# ---- Recording
add(LDC,
    E('AKG C 12', 'AKG', '1953', 'AKG tube condenser of 1953; the Telefunken ELA M 250 and M 251 followed in 1960.', 'AK', v=[V('Telefunken ELA M 250 / M 251', 'Telefunken', '1960')]),
    E('AKG C3000', 'AKG', '1993', 'AKG large-diaphragm condenser made 1993 to 2012 in five versions.', 'AK'),
    E('AKG SolidTube', 'AKG', '1997', 'AKG tube microphone of 1997, discontinued.', 'AK'),
    E('Teenage Engineering CM-15', 'Teenage Engineering', '2023', 'Teenage Engineering microphone of 2023.', 'TE'))
addv(LDC, 'AKG C414', V('C414 LTD 60th anniversary edition', 'AKG', '2006'))
add(DYN,
    E('Sennheiser MD 21', 'Sennheiser', '1953', 'Sennheiser dynamic microphone of 1953.', 'SE'),
    E('Sennheiser MD 82', 'Sennheiser', '1956', 'Sennheiser microphone of 1956.', 'SE'),
    E('Sennheiser DM 2', 'Sennheiser', '1946', 'First original Sennheiser microphone design, 1946, with the DM 3 and DM 4.', 'SE', v=[V('DM 3', 'Sennheiser', '1946'), V('DM 4', 'Sennheiser', '1946')]),
    E('Electro-Voice Model 664', 'Electro-Voice', 'mid-1950s', 'Electro-Voice dynamic microphone of the mid-1950s.', 'EV'),
    E('Electro-Voice RE15', 'Electro-Voice', '1960s', 'Electro-Voice microphone of the 1960s.', 'EV'),
    E('Electro-Voice RE27N/D', 'Electro-Voice', 'late 1980s', 'Electro-Voice broadcast microphone of the late 1980s.', 'EV'),
    E('Electro-Voice N/DYM', 'Electro-Voice', 'mid-1980s', 'Electro-Voice microphone series of the mid-1980s.', 'EV'))
addv(DYN, 'Sennheiser MD 421', V('MD 421', 'Sennheiser', '1960'))
add(SDC, E('Electro-Voice Model 642 Cardiline', 'Electro-Voice', '1961', 'Electro-Voice long-range shotgun microphone of 1961.', 'EV'))
add('Wireless microphone system',
    E('AKG WMS100 / WMS900', 'AKG', '1991', 'AKG wireless microphone systems of 1991.', 'AK', v=[V('WMS100', 'AKG', '1991'), V('WMS900', 'AKG', '1991')]),
    E('Sennheiser Microport', 'Sennheiser', '1957', 'Sennheiser wireless microphone system of 1957.', 'SE'))
add('Audio interface',
    E('Universal Audio Apollo', 'Universal Audio', '2012', 'Universal Audio interface line from 2012.', 'UA', v=[V('Apollo Twin X Gen 2', 'Universal Audio'), V('Apollo X Gen 2', 'Universal Audio')]),
    E('Universal Audio Volt', 'Universal Audio', '2021', 'Universal Audio USB interface line from 2021.', 'UA'),
    E('Arturia AudioFuse', 'Arturia', '2015', 'Arturia interface of 2015.', 'AR'))
addv('Outboard processor', 'UREI 1176', V('1176 reissue (Universal Audio)', 'Universal Audio', '1999', 'The revived company first product'))
addv('Outboard processor', 'Teletronix LA-2A', V('LA-2A production by Studio Electronics', 'Universal Audio', '1967'))
add('Portable audio recorder',
    E('Zoom Handy Recorder', 'Zoom', '', 'Zoom Handy Recorder line: H4n (retired), H5, H5studio and H6.', 'ZO', v=[V('H4n', 'Zoom'), V('H5', 'Zoom'), V('H5studio', 'Zoom'), V('H6', 'Zoom')]),
    E('Teenage Engineering TP-7', 'Teenage Engineering', '2023', 'Teenage Engineering field recorder of 2023.', 'TE'),
    E('Korg MR-1000', 'Korg', '2006', 'Korg portable recorder of 2006 with the MR-1; the MR-2 (2010) and MR-2000s (2008) followed.', 'KO', v=[V('MR-1', 'Korg', '2006'), V('MR-2000s', 'Korg', '2008'), V('MR-2', 'Korg', '2010')]))
add('Multitrack recorder',
    E('Alesis ADAT', 'Alesis', '1991', 'Alesis digital multitrack tape recorder of 1991.', 'AL'),
    E('Zoom R8', 'Zoom', '', 'Zoom multitrack recorder.', 'ZO'))
add('Audio mixer',
    E('Allen & Heath SQ', 'Allen & Heath', '', 'Allen & Heath digital mixer line: SQ-5, SQ-6 and SQ-7.', 'AH', v=[V('SQ-5', 'Allen & Heath'), V('SQ-6', 'Allen & Heath'), V('SQ-7', 'Allen & Heath')]),
    E('Allen & Heath Qu', 'Allen & Heath', '', 'Allen & Heath compact digital mixer series.', 'AH'),
    E('Allen & Heath dLive', 'Allen & Heath', '', 'Allen & Heath live digital mixing system.', 'AH'),
    E('Allen & Heath Avantis', 'Allen & Heath', '', 'Allen & Heath digital mixer.', 'AH'),
    E('Teenage Engineering TX-6', 'Teenage Engineering', '2022', 'Teenage Engineering field mixer of 2022.', 'TE'),
    E('Zoom LiveTrak', 'Zoom', '', 'Zoom digital mixers L-8, L-12 and L-20R.', 'ZO', v=[V('L-8', 'Zoom'), V('L-12', 'Zoom'), V('L-20R', 'Zoom')]))
addv('Audio mixer', 'Allen & Heath SQ', V('SQ-5', 'Allen & Heath'))
# ---- Drums
add('Acoustic drum kit', E('Sonor Sonorlite', 'Sonor', '1980s', 'Sonor kit of the 1980s, with the Hilite.', 'SO', v=[V('Hilite', 'Sonor', '1980s')]),
    E('Sonor X-Ray Acrylic', 'Sonor', '', 'Sonor acrylic kit, reintroduced; year not stated.', 'SO'))
add('Snare drum', E('Johannes Link Parade Snare', 'Sonor', '1942', 'Parade snare drum of 1942 named in the Sonor article.', 'SO'))
add('Cymbal',
    E('Zildjian K Custom', 'Zildjian', '', 'Zildjian K-family line named on the Zildjian site.', 'ZIL'),
    E('Zildjian S Family', 'Zildjian', '', 'Zildjian S Zildjian and S Dark lines.', 'ZIL', v=[V('S Zildjian', 'Zildjian'), V('S Dark', 'Zildjian')]),
    E('Zildjian Planet Z', 'Zildjian', '', 'Zildjian I-family Planet Z line named on the Zildjian site.', 'ZIL'),
    E('Zildjian K Orchestral', 'Zildjian', '', 'Zildjian orchestral K lines: K Orchestral, K Constantinople Orchestral, K Klassisch Symphonic, K Symphonic.', 'ZIL'),
    E('Zildjian Z-MAC', 'Zildjian', '', 'Zildjian Z-MAC marching cymbals named on the Zildjian site.', 'ZIL'))
# ---- DJ
addv('DJ turntable', 'Technics SL-1200',
     V('SL-1200MK2', 'Technics', '1979', 'Series ran to 2010'), V('SL-1210MK2', 'Technics', '1979'), V('SL-1200MK3', 'Technics', '1989', 'Japan only'),
     V('SL-1200M3D', 'Technics', '1997'), V('SL-1200MK5', 'Technics', '2000'), V('SL-1200MK6', 'Technics', '2008', 'February 2008, Japan'),
     V('SL-1200G', 'Technics', '2016'), V('SL-1200GAE', 'Technics', '2016', '50th Anniversary Edition, 1,200 units'), V('SL-1200GR', 'Technics', '2017'),
     V('SL-1200MK7', 'Technics', '2019'), V('SL-1210GAE', 'Technics', '2020', '55th Anniversary Edition, 1,210 units'))
add('DJ mixer', E('Korg KM-2', 'Korg', '2001', 'Korg DJ mixer of 2001; the KM202 and KM404 followed in 2007.', 'KO', v=[V('KM202 / KM404', 'Korg', '2007')]))
addv('DJ controller', 'Pioneer XDJ-RX', V('XDJ-RX', 'Pioneer DJ', '2015'))
add('DJ controller',
    E('Pioneer DDJ-SX', 'AlphaTheta (Pioneer DJ)', '2014', 'Pioneer DJ controller line named in the Pioneer DJ article; the DDJ-SX2 is shown for 2014 and the DDJ-RX for 2015.', 'PD',
      v=[V('DDJ-SX2', 'Pioneer DJ', '2014'), V('DDJ-RX', 'Pioneer DJ', '2015')]))

# --- confirmation of loose-model conversions: name -> (source key, year, description)
CONFIRM = {
    'Moog Messenger': ('MO', '2025', 'Moog monophonic synthesizer of 2025.'), 'Moog Grandmother': ('MO', '2018', 'Moog semi-modular synthesizer, 2018 onwards.'),
    'Moog Subsequent 37': ('MO', '2017', 'Moog analogue paraphonic synthesizer, 2017 onwards; the CV edition dates from 2017.'),
    'Moog Muse': ('MO', '2024', 'Moog polyphonic synthesizer of 2024.'), 'Moog One': ('MO', '2018', 'Moog polyphonic synthesizer, 2018 onwards.'),
    'Sequential Prophet-6': ('SQ', '2015', 'Dave Smith Instruments six-voice synthesizer of 2015.'),
    'Arturia MiniFreak': ('AR', '2022', 'Arturia hybrid synthesizer of 2022.'), 'Arturia PolyBrute': ('AR', '2021', 'Arturia analogue polysynth of 2021.'),
    'Elektron Machinedrum': ('EL', '2002', 'Elektron drum machine of 2002.'), 'Elektron Analog Rytm': ('EL', '2014', 'Elektron analogue drum machine of 2014.'),
    'Elektron Syntakt': ('EL', '2022', 'Elektron drum and synth machine of 2022.'),
    'Alesis SR-16': ('AL', '', 'Alesis drum machine named in the Alesis article; year not stated.'), 'Alesis DM5 module': ('AL', '', 'Alesis drum module cited in 1996; year not stated.'),
    'Neumann TLM 103': ('NE', '', 'Neumann TLM condenser named in the Neumann article; year not stated.'),
    'Shure KSM313': ('SH', '2009', 'Shure ribbon microphone of 2009.'), 'Shure KSM353': ('SH', '2009', 'Shure ribbon microphone of 2009.'),
    'Audio-Technica AT-LP120X': ('AT', '2019', 'Updated AT-LP120 series shown at CES 2019.'), 'Audio-Technica ATH-M40x': ('AT', '2014', 'Audio-Technica monitor headphone of 2014.'),
    'Audio-Technica ATH-R70xa': ('AT', '', 'Audio-Technica reference headphone named in the Audio-Technica article (2026 TEC Award).'),
    'Pioneer DDJ-SX2': ('PD', '2014', 'Pioneer DJ controller of 2014.'), 'Pioneer DJ DDJ-RX': ('PD', '2015', 'Pioneer DJ controller of 2015.'),
    'Kawai CA series': ('KW', '', 'Kawai Concert Artist digital piano series; year not stated.'), 'Kawai ES series': ('KW', '', 'Kawai portable digital piano series; year not stated.'),
    'Nord Electro': ('CL', '2001', 'Clavia Nord Electro of 2001; Electro 2 to 6 followed.'),
    'Fazioli F-series grands': ('FZ', '', 'Fazioli F156, F183, F198, F212, F228, F278 and F308; prototypes from 1980.'),
    'AKG C1000S': ('AK', '1986–2012', 'AKG small-diaphragm condenser made 1986 to 2012 in four versions.'),
    'Pioneer CMX-5000': ('CDJ', '2000', 'Pioneer CD player listed in the CDJ article, March 2000.'),
    'Pioneer CMX-3000': ('CDJ', '2003', 'Pioneer CD player listed in the CDJ article, 2003.'),
    'Pioneer MEP-7000': ('CDJ', '2007', 'Pioneer media player listed in the CDJ article, late 2007.'),
    'Lowrey home organ': ('KW', '', 'Lowrey home organs; Kawai owns Lowrey, year not stated.'),
}
# names removed because a version/entry now exists or is in r
DUPES = {'Shure Beta 52A', 'Shure QLXD24/SM58', 'Shure PSM300', 'Clavia Nord Piano 3', 'Arturia DrumBrute Impact', 'Arturia KeyStep Pro', 'Casio Privia PX-S3100',
         'Casio Celviano Grand Hybrid', 'Universal Audio Apollo Twin X Gen 2', 'Universal Audio Apollo X Gen 2', 'Zoom H5studio', 'Allen & Heath SQ5', 'Kawai K 15',
}
ROLES = {'Sequential Prophet-5': ('origin', 'P5'), 'Yamaha DX7': ('landmark', 'DX'), 'Minimoog Model D': ('origin', 'MM'), 'Roland TR-808': ('landmark', 'T8'),
         'Linn LM-1 Drum Computer': ('origin', 'LM'), 'Shure SM58': ('landmark', 'SM58'), 'Neumann U 47': ('origin', 'U47')}
OWN2 = {
    'Sequential': ('Focusrite plc', 'Independent', '', '2021'), 'Novation': ('Focusrite plc', 'Independent', '', '2004'), 'ADAM Audio': ('Focusrite plc', 'Independent', '', '2019'),
    'Alesis': ('inMusic Brands', 'Independent', '', '2012'), 'Akai Professional': ('inMusic Brands', 'Independent', '', '2012'), 'Rane': ('inMusic Brands', 'Independent', '', '2016'),
    'Native Instruments': ('inMusic Brands', 'Independent', '', '2026'), 'Behringer': ('Music Tribe', 'Independent', '', ''),
    'Kurzweil': ('Hyundai Development Company', 'Independent', '', '2006'), 'E-mu Systems': ('Creative Technology', 'Independent', '', '1993'),
    'Ensoniq': ('Creative Technology', 'Independent', '', '1998'), 'Allen & Heath': ('Audiotonix Group', 'Independent', '', ''),
    'Electro-Voice': ('Bosch', 'Global group', '', '2006'), 'AKG': ('Samsung Electronics', 'Global group', '', '2017'), 'Elektron': ('Bonnier Capital', 'Independent', '', '2026'),
    'Universal Audio': ('Bill Putnam Jr.', 'Independent', '', ''), 'Technics': ('Panasonic Corporation', 'Global group', '', ''),
    'AlphaTheta (Pioneer DJ)': ('Noritsu', 'Independent', 'Japan', '2020'), 'Clavia': ('Clavia DMI AB', 'Independent', 'Sweden', ''),
    'Lowrey': ('Kawai', 'Independent', '', ''), 'Kawai': ('Kawai', 'Independent', '', ''), 'Gretsch': ('Gretsch family', 'Independent', '', ''),
}
