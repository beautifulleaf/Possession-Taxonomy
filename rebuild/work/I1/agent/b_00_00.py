import sys; sys.path.insert(0,'/home/user/Possession-Taxonomy/rebuild/work/I1/agent')
from put import put
WP='https://en.wikipedia.org/wiki/'
LL=WP+'List_of_Linux_distributions'
def V(n,mk='',y='',d=''): 
    v={'n':n}
    if mk: v['mk']=mk
    if y: v['y']=y
    if d: v['d']=d
    return v
win=[V('Windows 1.0','Microsoft','1985'),V('Windows 2.0','Microsoft','1987'),V('Windows 3.0','Microsoft','1990'),V('Windows 3.1','Microsoft','1992'),
 V('Windows 95','Microsoft','1995','Original, A, B (OSR2), B USB (OSR2.1), C (OSR2.5); the OSR releases were OEM-only'),
 V('Windows 98','Microsoft','1998','Second Edition followed'),V('Windows Me','Microsoft','2000'),
 V('Windows XP','Microsoft','2001','Home, Professional, N, Media Center, Tablet PC, Starter, Professional x64'),
 V('Windows Vista','Microsoft','2007','Starter, Home Basic, Home Premium, Business, Enterprise, Ultimate'),
 V('Windows 7','Microsoft','2009','Starter, Home Basic, Home Premium, Professional, Enterprise, Ultimate'),
 V('Windows 8','Microsoft','2012','Windows 8, Pro, Enterprise, RT'),V('Windows 8.1','Microsoft','2013','Same editions as Windows 8'),
 V('Windows 10','Microsoft','2015','Home, Pro, Pro for Workstations, Pro Education, Education, Enterprise, IoT Enterprise, S mode'),
 V('Windows 11','Microsoft','2021','Home, Pro, Pro for Workstations, Pro Education, Education, Enterprise, SE; N and KN editions without media player')]
mac=[]
for n,nm,y in [('Mac OS X 10.0','Cheetah','2001'),('Mac OS X 10.1','Puma','2001'),('Mac OS X 10.2','Jaguar','2002'),('Mac OS X 10.3','Panther','2003'),('Mac OS X 10.4','Tiger','2005'),('Mac OS X 10.5','Leopard','2007'),('Mac OS X 10.6','Snow Leopard','2009'),('Mac OS X 10.7','Lion','2011'),('OS X 10.8','Mountain Lion','2012'),('OS X 10.9','Mavericks','2013'),('OS X 10.10','Yosemite','2014'),('OS X 10.11','El Capitan','2015'),('macOS 10.12','Sierra','2016'),('macOS 10.13','High Sierra','2017'),('macOS 10.14','Mojave','2018'),('macOS 10.15','Catalina','2019'),('macOS 11','Big Sur','2020'),('macOS 12','Monterey','2021'),('macOS 13','Ventura','2022'),('macOS 14','Sonoma','2023'),('macOS 15','Sequoia','2024'),('macOS 26','Tahoe','2025'),('macOS 27','Golden Gate','2026')]:
    mac.append(V(f'{n} {nm}','Apple',y))
chrome=[V('ChromeOS','Google','2011','First shipped on Chromebooks in June 2011; proprietary, built on ChromiumOS'),
 V('ChromiumOS','Google','2009','Open-source project ChromeOS is partly derived from; source released November 2009'),
 V('ChromeOS Flex','Google','2022','Installable on non-Chromebook PCs and Macs; no Google Play or Android apps'),
 V('Googlebook OS','Google','','Announced Android-based successor to consumer ChromeOS')]
desk={'n':'Desktop operating system','a':'','d':'Operating system that runs a desktop or laptop computer and its applications.',
 't':['Home edition','Pro edition','Education edition','ARM build','install-on-old-PC edition'],'s':WP+'Comparison_of_operating_systems','tg':[],
 'x':[
 {'n':'Windows','a':'Microsoft Windows','d':'Microsoft\'s graphical operating system for PCs, sold in Home, Pro and business editions.','mk':'Microsoft','y':'1985','s':WP+'Microsoft_Windows_version_history','v':win,'dt':'edition (Home, Pro, Education, Enterprise) · architecture · language · retail or OEM licence'},
 {'n':'macOS','a':'Mac OS X · OS X','d':'Apple\'s operating system for Mac computers, named by cat, then California place after version 10.','mk':'Apple','y':'2001','s':WP+'MacOS_version_history','v':mac,'dt':'version name · Intel or Apple silicon support'},
 {'n':'ChromeOS','a':'Chrome OS','d':'Google\'s browser-centred operating system for Chromebooks and, as Flex, for ordinary PCs.','mk':'Google','y':'2011','s':WP+'ChromeOS','v':chrome,'dt':'Chromebook build · Flex install · Linux and Android app support'}]}
for k in ('tg',): desk.pop(k)
def A(n,d,mk,s,v,a='',y='',dt=''):
    x={'n':n,'a':a,'d':d,'mk':mk,'y':y,'s':s,'v':v}
    if dt: x['dt']=dt
    return x
linux={'n':'Linux distribution','a':'distro · GNU/Linux','d':'Complete operating system built around the Linux kernel, grouped here by the distribution it descends from.',
 't':['GNOME edition','KDE Plasma edition','Xfce edition','MATE edition','Cinnamon edition','LXQt edition','rolling release','point release','immutable','live USB','gaming','security testing','privacy-focused'],
 's':LL,'x':[
 A('Debian lineage','Debian and the distributions built on it, including the Ubuntu family.','Debian Project',LL,[
  V('Debian','Debian Project'),V('Ubuntu','Canonical','','Official flavours: Kubuntu, Lubuntu, Xubuntu, Ubuntu MATE, Ubuntu Budgie, Ubuntu Studio, Edubuntu, Ubuntu Cinnamon, Ubuntu Kylin'),
  V('Linux Mint','','','Unofficial Ubuntu derivative'),V('Pop!_OS','System76','','Unofficial Ubuntu derivative'),V('elementary OS','Elementary LLC','','Unofficial Ubuntu derivative'),V('Zorin OS','Zorin Group','','Unofficial Ubuntu derivative'),
  V('MX Linux','MX Linux team'),V('Kali Linux','Offensive Security','','Security testing'),V('Parrot OS','Parrot Dev Team','','Security testing'),V('Tails','Tails Development Team','','Privacy-focused live system'),V('Raspberry Pi OS'),V('Deepin','Wuhan Deepin Technology Co., Ltd.'),V('Devuan','','','Debian fork offering a choice of init systems'),V('Whonix'),V('PureOS'),V('Q4OS'),V('SparkyLinux'),V('KNOPPIX','','','Live system'),V('Endless OS'),V('Pardus','TUBITAK'),V('Trisquel')],
  y='',dt='release (stable, testing) · desktop environment · architecture'),
 A('Red Hat and Fedora lineage','Fedora and the RPM-based systems derived from it, including rebuilds of Red Hat Enterprise Linux.','Fedora Project',LL,[
  V('Fedora Linux','Fedora Project'),V('Rocky Linux','','','RHEL-based rebuild'),V('AlmaLinux','','','RHEL-based rebuild'),V('Nobara'),V('Bazzite','','','Gaming-focused'),V('Qubes OS','Invisible Things Lab','','Security through isolation'),V('Fedora Asahi Remix','','','For Apple silicon Macs'),V('Fedora CoreOS')],dt='spin (desktop environment) · edition · release'),
 A('Arch lineage','Arch Linux, a rolling-release system, and distributions built on its pacman packages.','',LL,[
  V('Arch Linux'),V('Manjaro Linux'),V('EndeavourOS'),V('CachyOS'),V('Garuda Linux'),V('SteamOS','Valve'),V('Arch Linux ARM'),V('Artix','','','Arch without systemd'),V('ArchBang'),V('BlackArch','','','Security testing'),V('Parabola'),V('Hyperbola'),V('RebornOS'),V('Archcraft'),V('Athena OS'),V('Mabox'),V('KaOS','','','Pacman-based but independent')],dt='desktop environment · installer · rolling snapshot'),
 A('openSUSE lineage','openSUSE and distributions built on it.','openSUSE Project',LL,[V('openSUSE','openSUSE Project'),V('GeckoLinux'),V('Linux Kamarada')]),
 A('Mandriva lineage','The Mandrake and Mandriva descendants, still kept up by community projects.','',LL,[V('Mageia','Mageia Community'),V('OpenMandriva Lx'),V('ROSA','LLC NTC IT ROSA'),V('PCLinuxOS'),V('ALT Linux','Alt Linux Team')]),
 A('Slackware lineage','Slackware, an early distribution kept deliberately simple, and its derivatives.','',LL,[V('Slackware'),V('Salix'),V('Slax'),V('Porteus'),V('Zenwalk')]),
 A('Gentoo lineage','Gentoo, which builds software from source, and its derivatives.','Gentoo Foundation',LL,[V('Gentoo Linux','Gentoo Foundation'),V('Calculate Linux'),V('Redcore')]),
 A('NixOS','Distribution configured declaratively through the Nix package manager, with atomic rollbacks.','NixOS Foundation',WP+'NixOS',[V('NixOS','NixOS Foundation','2006','First prototype 2006; first stable release 13.10 in 2013')],y='2006'),
 A('Independent distributions','Distributions that are not derived from the lineages above.','',LL,[V('Void Linux'),V('Alpine'),V('Solus'),V('Puppy Linux','Puppy Foundation'),V('Tiny Core Linux'),V('Guix System'),V('Linux From Scratch'),V('GoboLinux'),V('CRUX'),V('Source Mage')])]}
hobby={'n':'Alternative & hobby operating system','a':'hobby OS · niche OS','d':'Desktop operating system outside Windows, macOS and Linux, kept alive by enthusiasts, such as BSDs, BeOS and Amiga descendants, and new from-scratch systems.',
 't':['BSD on the desktop','Unix-like from scratch','legacy-system continuation','retro platform'],'s':WP+'List_of_OSes','x':[
 A('FreeBSD and desktop BSDs','Unix descended from Berkeley BSD, first released in 1993, with desktop-oriented derivatives.','',WP+'FreeBSD',[V('FreeBSD','','1993','Grew out of 386BSD'),V('GhostBSD','Eric Turgeon','2010','Desktop distribution with MATE'),V('MidnightBSD','','2007','Desktop-focused, forked from FreeBSD 6.1'),V('DragonFly BSD','Matthew Dillon','','Forked from FreeBSD 4.8')],y='1993'),
 A('Haiku','Free re-implementation of BeOS, begun as OpenBeOS in 2001.','Haiku Inc',WP+'Haiku_(operating_system)',[V('R1/Alpha1','','2009'),V('R1/Alpha2','','2010'),V('R1/Alpha3','','2011'),V('R1/Alpha4','','2012'),V('R1/Beta1','','2018'),V('R1/Beta2','','2020'),V('R1/Beta3','','2021'),V('R1/Beta4','','2022'),V('R1/Beta5','','2024'),V('R1/Beta6','','2026','Preview')],y='2001'),
 A('RISC OS','Operating system for ARM computers, designed by Acorn for the Archimedes.','Acorn Computers',WP+'RISC_OS',[V('Arthur','Acorn Computers','1987','First release, Arthur 1.20'),V('RISC OS 2','Acorn Computers','1989'),V('RISC OS 3','Acorn Computers','1991','3.5 followed in 1994'),V('RISC OS 4','RISCOS Ltd','1999','Based on 3.8'),V('RISC OS 5','','2002','32-bit; first on the Iyonix PC; open-sourced 2018; 5.30 in April 2024'),V('RISC OS 6','RISCOS Ltd','2009','Proprietary; 6.20')],y='1987'),
 A('OS/2 continuations','Descendants of IBM OS/2 sold to enthusiasts and businesses.','Arca Noae',WP+'List_of_OSes',[V('ArcaOS','Arca Noae','','Warp 4.52 based'),V('eComStation','Serenity Systems','','Repackaged Warp 4.5')]),
 A('AmigaOS and descendants','Amiga-style systems: AmigaOS 4 for PowerPC and MorphOS.','',WP+'MorphOS',[V('AmigaOS 4','Hyperion Entertainment'),V('MorphOS','','2000','First release 0.1 in 2000; 3.20 in 2026')],y='1999'),
 A('ReactOS','Free system aiming at binary compatibility with Windows programs and drivers, still alpha.','ReactOS development team',WP+'ReactOS',[V('ReactOS 0.4.16','','2026','Latest release at retrieval')],y='1998'),
 A('SerenityOS','From-scratch Unix-like desktop with a 1990s-style interface; built from source, no releases.','Andreas Kling',WP+'SerenityOS',[],y='2018'),
 A('FreeDOS','Free MS-DOS-compatible system begun by Jim Hall in 1994.','',WP+'FreeDOS',[V('FreeDOS 1.0','','2006'),V('FreeDOS 1.1','','2012'),V('FreeDOS 1.2','','2016'),V('FreeDOS 1.3','','2022'),V('FreeDOS 1.4','','2025')],y='1994')]}
M=lambda *a:[list(x) for x in a]
vm={'n':'Virtual machine software','a':'virtualisation software','d':'Program that runs one or more virtual machines or whole guest systems on the owner\'s computer.',
 't':['hosted hypervisor','built-in OS hypervisor','full-system emulator','Apple silicon virtualiser'],'s':WP+'Comparison_of_platform_virtualization_software',
 'm':M(('VirtualBox','Oracle Corporation'),('VMware Workstation','VMware'),('VMware Fusion','VMware'),('VMware Player','VMware'),('Parallels Desktop for Mac','Parallels'),('Hyper-V','Microsoft'),('QEMU','QEMU project'),('UTM','Turing Software'),('KVM','Red Hat'),('Virtual Machine Manager','Red Hat'),('Proxmox VE','Proxmox'),('bhyve','FreeBSD Project'),('Windows Virtual PC','Microsoft'),('Virtual PC','Microsoft'),('DOSBox','Peter Veenstra'),('86Box',''),('Bochs',''))}
ac={'n':'App compatibility layer','a':'','d':'Program that runs another operating system\'s applications directly, without a virtual machine or emulated hardware.',
 't':['Windows apps on Linux','Windows apps on Mac','x86 on ARM translation','Android apps on desktop'],'s':WP+'Wine_(software)',
 'm':M(('Wine',''),('Proton','Valve'),('CrossOver','CodeWeavers'),('Bottles','Bottles developers'),('Wineskin',''),('Rosetta 2','Apple'),('Box64','ptitSeb'),('FEX','Ryan Houdek'),('Hangover','AndreRH'),('Winlator','brunodev85'),('WOW64','Microsoft'))}
B=lambda n,c,f,seg,kf,d,**k:dict({'n':n,'c':c,'f':f,'seg':seg,'kf':kf,'d':d,'s':'knowledge'},**k)
brands=[B('Microsoft','United States','1975','Mainstream','Windows','American software company that makes Windows.'),
 B('Apple','United States','1976','Premium','macOS','American company that makes the Mac and macOS.'),
 B('Google','United States','1998','Mainstream','ChromeOS','American company behind ChromeOS and Android.'),
 B('Valve','United States','1996','Mainstream','Steam, Proton','American games company behind Steam, SteamOS and Proton.'),
 B('Oracle Corporation','United States','1977','Mainstream','VirtualBox','American software company that owns VirtualBox.'),
 B('VMware','United States','1998','Premium','virtualisation','Virtualisation company behind Workstation, Player and Fusion.'),
 B('CodeWeavers','United States','1996','Specialist','CrossOver','Company that sells CrossOver and funds much Wine work.'),
 B('Acorn Computers','United Kingdom','1978','Heritage manufactory','RISC OS','British computer maker that designed RISC OS for its ARM machines.'),
 B('Canonical','United Kingdom','2004','Mainstream','Ubuntu','Company that publishes and supports Ubuntu.')]
notes=('Desktop operating system: 160-odd Linux/BSD/hobby names from old k9 redistributed into lineage archetypes (Linux distribution) and the hobby kind; Windows, macOS and ChromeOS are archetypes with versions/editions from fetched Wikipedia pages. '
 'Dropped as server, appliance, router, NAS, media-centre, phone or single-purpose systems: OpenWrt, VyOS, openmediavault, FreedomBox, Volumio, CoreELEC, LibreELEC, OSMC, Lakka, Recalbox, Batocera.linux, DietPi, Armbian, ZimaOS, Tribblix, openEuler, openKylin, LineageOS, Murena, postmarketOS, Mobian, Ubuntu Touch, also minor/dead or unplaced distros (Adelie, BigLinux, BlankOn, Bluefin, BunsenLabs, CAINE, Drauger OS, Elive, Emmabuntus, Exherbo, Feren OS, Finnix, Freespire, Linspire, Lindows, FydeOS, GNOME OS, Kicksecure, Kodachi, KDE neon, LinuxConsole, Nitrux, Obarun, Oreon, Pentoo, Peppermint OS, PikaOS, SliTaz, SolydXK, SystemRescue, TUXEDO OS, Ultramarine, Vanilla OS, Voyager, Wattos, antiX, blendOS, Linux Lite, Bodhi Linux, Damn Small Linux, Chimera, ChimeraOS). Classic Mac OS and other dead tails belong on the Classic software shelf. '
 'Virtual machine software cut from 50 to 17: dropped server/enterprise hypervisors (ESX/ESXi, XenServer, XCP-ng, Xen, PowerVM, z/VM, Virtuozzo, OpenVZ, OpenNebula, Oracle VM, Sun xVM, Virtual Iron, Wind River, PikeOS, LynxSecure, VirtualLogix, XtratuM, OKL4, RTS, Integrity VM), research/mainframe emulators (SIMH, GXemul, Hercules, Simics, CHARON, JPC, PearPC) and dead products (Virtual Server, VMware Server/ESX, Parallels Workstation, QuickTransit, SVISTA, Cooperative Linux, User Mode Linux, DOSEMU, LXC). UTM added from a fetched page. '
 'App compatibility layer cut from 21 to 11: dropped single-game or fringe wrappers (Sober, Vinegar, TeknoParrot, GameHub, MiceWine, libndk, libhoudini, Win3mu, NTVDMx64, Boxedwine). Brand entries use owner-approved knowledge.')
put('00_00',{'kinds':[desk,linux,hobby,vm,ac],'brands':brands,'traditions':[],'notes':notes})
