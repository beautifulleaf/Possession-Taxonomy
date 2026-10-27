import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/I1/agent')
from put import put
WP='https://en.wikipedia.org/wiki/'
LST=WP+'List_of_video_game_console_emulators'
def V(n,mk='',y='',d=''):
    v={'n':n}
    if mk: v['mk']=mk
    if y: v['y']=y
    if d: v['d']=d
    return v
def A(n,d,s,v,mk='',y='',a='',dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s,'v':v}
    if dt: x['dt']=dt
    return x
emu={'n':'Game emulator','a':'','d':'Program that imitates a game console\'s, arcade board\'s or home computer\'s hardware so that its games run on the owner\'s computer or phone.',
 't':['console emulator','arcade emulator','home-computer emulator','multi-system front end','phone emulator','browser emulator'],
 's':LST,'x':[
 A('MAME','Arcade-machine emulator begun by Nicola Salmoria in the 1990s that now also covers consoles and computers; the reference for preservation.',WP+'MAME',[V('MAME','','1997','First public release 5 February 1997'),V('MESS','','2015','Console and computer emulator on the MAME core; merged into MAME in May 2015 (0.162)')],y='1997',dt='driver set · ROM set (full, split, non-merged) · version'),
 A('RetroArch','Front end for the libretro API that runs emulators as loadable cores behind one interface.',WP+'RetroArch',[V('SSNES','','2010','Original name; renamed RetroArch in April 2012'),V('RetroArch 1.0','','2014','Version 1.0.0.0, January 2014')],y='2010',dt='core · platform · shader and input setup'),
 A('OpenEmu','Mac front end with a plug-in design that gathers console emulators in one library.',WP+'OpenEmu',[V('OpenNestopia','','2007','Original name'),V('OpenEmu 1.0','','2013')],y='2007'),
 A('Dolphin','GameCube and Wii emulator, first released in 2003 by F|RES and Henrik Rydgard (ector).',WP+'Dolphin_(emulator)',[V('Dolphin','','2003','Also covers Game Boy Player and Triforce arcade hardware')],y='2003'),
 A('Cemu','Wii U emulator, first released for Windows in 2015 and open-sourced with 2.0 in 2022.',WP+'Cemu',[V('Cemu 2.0','','2022','Open source under the Mozilla Public License; first Linux and later macOS builds')],y='2015'),
 A('Nintendo Switch emulators','Switch emulators and the forks that continued them after the 2024 shutdowns.',WP+'Yuzu_(emulator)',[V('Yuzu','','2018','Built by the Citra team; ended March 2024 after a Nintendo lawsuit'),V('Ryujinx','','2018','Written in C# by gdkchan; shut down October 2024'),V('Suyu','','2024','Yuzu fork; ceased 2025'),V('Torzu','','','Yuzu fork developed over Tor'),V('Eden','','','Active Yuzu continuation'),V('Citron','','','Active Yuzu continuation')],y='2018'),
 A('Nintendo 3DS emulators','Emulators for the 3DS.',LST,[V('Citra')]),
 A('NES and Famicom emulators','Emulators for the 8-bit Nintendo system.',LST,[V('FCEUX'),V('Nestopia'),V('NESticle')]),
 A('SNES emulators','Emulators for the Super Nintendo.',LST,[V('Snes9x'),V('ZSNES'),V('higan')]),
 A('Nintendo 64 emulators','Emulators for the N64, from the first high-level emulator to current plug-in ones.',LST,[V('UltraHLE'),V('Project64'),V('Mupen64Plus'),V('Project Unreality')]),
 A('Game Boy and Game Boy Advance emulators','Emulators for Nintendo handhelds.',LST,[V('VisualBoyAdvance'),V('VisualBoyAdvance-M'),V('Wzonka-Lad')]),
 A('PlayStation emulators','Emulators for the original PlayStation, from commercial products to current free ones.',LST,[V('DuckStation'),V('ePSXe'),V('PCSX-Reloaded'),V('bleem!'),V('bleemcast!'),V('Connectix Virtual Game Station','','','Discontinued commercial emulator')]),
 A('PCSX2','PlayStation 2 emulator, successor to the PCSX PlayStation emulator, first released in 2002.',WP+'PCSX2',[V('PCSX2','','2002','Begun 2001 by Linuzappz and Shadow')],y='2002'),
 A('RPCS3','PlayStation 3 emulator and debugger, first announced in 2011.',WP+'RPCS3',[V('RPCS3','','2011')],y='2011'),
 A('PPSSPP','PlayStation Portable emulator by Henrik Rydgard, publicly released in 2012.',WP+'Ppsspp',[V('PPSSPP','','2012')],y='2012'),
 A('PlayStation 4, 5 and Vita emulators','Early-stage emulators for newer Sony hardware and the Vita.',LST,[V('shadPS4'),V('KytyPS5'),V('Vita3K')]),
 A('DOSBox','Emulator that runs MS-DOS programs, mostly games; its forks carry on after 2019.',WP+'DOSBox',[V('DOSBox','Peter Veenstra','2002','Last stable release 0.74-3, June 2019'),V('DOSBox-X','','','Fork aimed at pre-2000 DOS and Windows 9x'),V('DOSBox Staging','','','Modern continuation'),V('DOSBox Pure','','','libretro core'),V('Em-DOSBox','','','Runs in a web browser')],y='2002'),
 A('ScummVM','Re-creation of adventure-game engines, started for LucasArts SCUMM titles; not a hardware emulator.',WP+'ScummVM',[V('ScummVM','','2001','First release October 2001')],y='2001'),
 A('VICE','Emulator for Commodore\'s 8-bit machines (C64, C128, VIC-20, Plus/4, PET).',WP+'VICE',[V('VICE','','1993')],y='1993'),
 A('WinUAE','Amiga emulator for Windows, bundled with Cloanto\'s Amiga Forever.',WP+'Amiga_Forever',[V('WinUAE','','','Emulation engine of the Windows Amiga Forever player'),V('E-UAE'),V('UAE')],mk='Cloanto'),
 A('Atari and pinball emulators','Single-purpose emulators for the Atari 2600, Neo Geo CD and pinball tables.',LST,[V('Stella'),V('NeoCD'),V('Visual Pinball')])],
 'm':[['Mednafen',''],['Delta','']]}
mod={'n':'Game mod manager','a':'','d':'Program that downloads, installs, orders and switches game mods in a game\'s files without being a game or a mod itself.',
 't':['virtual file system','Nexus-linked','Thunderstore profiles','Minecraft platform','load-order sorter'],
 's':'https://tech-insider.org/vortex-vs-mod-organizer-2-vs-thunderstore-2026/','x':[
 A('Vortex','Nexus Mods\' own manager, the all-rounder for the Nexus catalogue.','https://tech-insider.org/vortex-vs-mod-organizer-2-vs-thunderstore-2026/',[V('Vortex','Nexus Mods','','v2.9.0 on 19 October 2026 per the page')],mk='Nexus Mods',dt='game · profile · deployment method'),
 A('Mod Organizer 2','Community successor to Mod Organizer, with a virtual file system suited to large Bethesda mod lists.','https://tech-insider.org/vortex-vs-mod-organizer-2-vs-thunderstore-2026/',[V('Mod Organizer 2','','','v2.5.2, August 2024 per the page')],dt='game · instance · profile'),
 A('Nexus Mods App','Nexus Mods\' newer app built around loadout switching.','https://www.itechguides.com/best/game-mod-managers/',[V('Nexus Mods App','Nexus Mods')],mk='Nexus Mods'),
 A('Thunderstore Mod Manager','Official client of the Thunderstore platform for BepInEx games such as Lethal Company and Valheim.','https://tech-insider.org/vortex-vs-mod-organizer-2-vs-thunderstore-2026/',[V('Thunderstore Mod Manager','','','Also known as r2modman; v3.2.17 per the page'),V('Gale Mod Manager'),V('Zephyr'),V('Prismo')]),
 A('Minecraft mod platforms','Launcher-style mod managers for Minecraft.','https://www.itechguides.com/best/game-mod-managers/',[V('CurseForge'),V('Modrinth')]),
 A('Single-game mod managers','Managers built around one game or engine.','https://www.itechguides.com/best/game-mod-managers/',[V('ME3Tweaks Mod Manager','ME3Tweaks','','Mass Effect'),V('CKAN','','','Indexed mod libraries'),V('RimSort','','','RimWorld'),V('Stardrop','','','Stardew Valley'),V('Wrye Bash','','','Bethesda-style mod management'),V('LOOT','','','Plugin load orders')])]}
brands=[{'n':'Nexus Mods','c':'United Kingdom','seg':'Specialist','kf':'mod hosting','d':'Mod-hosting site that develops the Vortex and Nexus Mods App managers.','s':'knowledge'}]
notes=('Game emulator: 40 flat models regrouped into 21 archetypes by system family (MAME, RetroArch, Dolphin, Cemu, Switch lineage, PlayStation lines, DOSBox, ScummVM, VICE, WinUAE, per-Nintendo-console groups); every old model kept as a version or in m. Added from fetched pages: OpenEmu is old; DOSBox forks, Eden/Citron/Torzu/Suyu, WinUAE/E-UAE/UAE, ScummVM, VICE. No emulator for Xbox, Mega Drive, Saturn, Dreamcast or DS appears on the fetched list, so none were added. '
 'Game mod manager: kept the 5 old models as archetypes, added CurseForge, Modrinth, CKAN, RimSort, Stardrop, Wrye Bash, LOOT, Gale, Zephyr, Prismo from the retrieved itechguides list; Nexus Mods App not covered by tech-insider so itechguides cited. Maker/year left blank where pages do not state them.')
put('00_01',{'kinds':[emu,mod],'brands':brands,'traditions':[],'notes':notes})
