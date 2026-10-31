# CPU, GPU data
IM='https://en.wikipedia.org/wiki/List_of_Intel_CPU_microarchitectures'
AM='https://en.wikipedia.org/wiki/List_of_AMD_CPU_microarchitectures'
AP='https://en.wikipedia.org/wiki/List_of_AMD_processors'
IC='https://en.wikipedia.org/wiki/List_of_Intel_Core_processors'
def V(n,y='',d='',mk=''): return {"n":n,"mk":mk,"y":y,"d":d}
def E(n,mk,y,d,s,g,v=None,a='',role=None,dt=None):
    e={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s,"v":v or [],"g":g}
    if role: e["role"]=role
    if dt: e["dt"]=dt
    return e
GI='Intel'; GA='AMD'; GO='Apple and other makers'
def i(n,y,d,v,**k): return E(n,'Intel',y,d,IM,GI,[V(*a,mk='Intel') for a in v],**k)
def a(n,y,d,v,s=AM,**k): return E(n,'AMD',y,d,s,GA,[V(*x,mk='AMD') for x in v],**k)
INTEL_NEW=[
 i('Intel 80286','1982','16-bit x86 chip with protected mode, used in the IBM PC/AT.',[('80286','1982','')]),
 i('Intel 80486','1989','Fourth-generation x86 chip with the maths unit on the die.',[('80486','1989','')]),
 i('Pentium (P5)','1993','Intel\'s fifth-generation x86 chip and the start of the Pentium brand.',[('Pentium (P5)','1993',''),('Pentium MMX','1997','MMX instructions')],a='P5'),
 i('P6 (Pentium Pro to Pentium III)','1995','Out-of-order x86 core behind Pentium Pro, Pentium II and Pentium III.',[('Pentium Pro','1995','P6, out-of-order execution'),('Pentium II','1997','Klamath'),('Pentium III','1999','Katmai')],a='P6'),
 i('NetBurst (Pentium 4)','2000','Long-pipeline core of the Pentium 4 and Pentium D.',[('Pentium 4 Willamette','2000',''),('Pentium 4 Northwood','2002',''),('Pentium 4 Prescott','2004',''),('Pentium D','2005','first multi-core Pentium')]),
 i('Pentium M','2003','Efficient mobile core (Banias, Dothan) that fed the later Core line.',[('Banias','2003',''),('Dothan','2004',''),('Yonah','','dual-core basis for the first Intel Core')]),
 i('Core / Core 2 (Intel Core microarchitecture)','2006','Dual- and quad-core design behind Core 2 Duo and Core 2 Quad; Penryn was the 45 nm shrink.',[('Core 2 Duo / Quad','2006',''),('Penryn','2007','45 nm shrink')],a='Core 2'),
 i('Nehalem','2008','First Core i3 / i5 / i7 generation, with the memory controller on the die.',[('Core i7 (1st gen)','2008',''),('Core i5 / i3 (1st gen)','',''),('Westmere','2010','32 nm shrink of Nehalem')],a='Core i 1st generation'),
 i('Sandy Bridge','2011','Second Core i generation with the graphics core on the CPU die.',[('Core i3 / i5 / i7 (2nd gen)','2011','')],a='Core i 2nd generation'),
 i('Ivy Bridge','2012','22 nm successor to Sandy Bridge.',[('Core i3 / i5 / i7 (3rd gen)','2012','')],a='Core i 3rd generation'),
 i('Haswell','2013','Fourth Core i generation; added AVX2 and FMA.',[('Core i3 / i5 / i7 (4th gen)','2013','')],a='Core i 4th generation'),
 i('Broadwell','2014','14 nm derivative of Haswell.',[('Core i3 / i5 / i7 (5th gen)','2014','')],a='Core i 5th generation'),
 i('Skylake','2015','Sixth Core i generation, the mainstream desktop chip that introduced DDR4.',[('Core i3 / i5 / i7 (6th gen)','2015','')],a='Core i 6th generation'),
 i('Kaby Lake','2016','Seventh Core i generation, successor to Skylake.',[('Core i3 / i5 / i7 (7th gen)','2016','')],a='Core i 7th generation'),
 i('Coffee Lake','2017','Eighth and ninth Core i generations, adding six and eight cores to mainstream desktops.',[('Core i3 / i5 / i7 (8th gen)','2017',''),('Core i5 / i7 / i9 (9th gen)','','Coffee Lake Refresh')],a='Core i 8th and 9th generation'),
 i('Cannon Lake','2018','Mobile-only 10 nm chip with the Palm Cove core.',[('Core i3-8121U','2018','')]),
 i('Comet Lake','2019','Tenth Core i generation for desktops, with up to ten cores.',[('Core i3 / i5 / i7 / i9 (10th gen desktop)','2019','')],a='Core i 10th generation'),
 i('Ice Lake','2019','10 nm Sunny Cove mobile chips, branded as 10th-generation Core.',[('Core i3 / i5 / i7 (Ice Lake)','2019','Sunny Cove core')],a='Sunny Cove'),
 i('Tiger Lake','2020','11th-generation Core mobile chips on the Willow Cove core.',[('Core i3 / i5 / i7 (11th gen mobile)','2020','Willow Cove core')],a='Willow Cove'),
 i('Rocket Lake','2021','11th-generation Core desktop chips, a 14 nm backport of Sunny Cove (Cypress Cove core).',[('Core i5 / i7 / i9 (11th gen desktop)','2021','Cypress Cove core')],a='Cypress Cove'),
 i('Alder Lake','2021','12th-generation Core, the first hybrid design with Golden Cove performance cores and Gracemont efficiency cores.',[('Core i3 / i5 / i7 / i9 (12th gen)','2021','Golden Cove and Gracemont')],a='Golden Cove',role='landmark'),
 i('Raptor Lake','2022','13th- and 14th-generation Core on the Raptor Cove core.',[('Core i3 / i5 / i7 / i9 (13th gen)','2022',''),('Core i3 / i5 / i7 / i9 (14th gen)','','Raptor Lake Refresh')],a='Raptor Cove'),
 i('Meteor Lake','2023','Chiplet mobile design with Redwood Cove cores, sold as Core Ultra Series 1.',[('Core Ultra 5 / 7 / 9 (Series 1)','2023','14 December 2023')],a='Redwood Cove'),
 i('Arrow Lake','2024','Desktop Core Ultra Series 2 on the Lion Cove core.',[('Core Ultra 5 / 7 / 9 (Series 2, desktop)','2024','')],a='Lion Cove'),
 i('Lunar Lake','2024','Low-power mobile Core Ultra Series 2 chips.',[('Core Ultra 200V','2024','')]),
 i('Panther Lake','2026','Mobile design on the Cougar Cove core, shown on Intel\'s roadmap.',[]),
 i('Intel Atom','2008','Low-power x86 line for netbooks, tablets and small devices, built on separate Atom-class cores.',[('Bonnell','2008','first Atom'),('Silvermont','2013',''),('Goldmont','2016',''),('Tremont','2020',''),('Gracemont','2021','efficiency cores in Alder Lake'),('Crestmont','2023',''),('Skymont','2024','')]),
]
AMD_NEW=[
 a('AMD K5','1996','AMD\'s first original x86 design.',[('K5','1996','')],s=AP),
 a('AMD K6','1997','Pentium-compatible design bought from NexGen\'s Nx686.',[('K6','1997',''),('K6-2','','added 3DNow!'),('K6-III','','three cache levels')],s=AP),
 a('Athlon (K7)','1999','AMD\'s K7 desktop core, the first desktop CPU to reach 1 GHz.',[('Athlon','1999',''),('Athlon XP','2001','Palomino to Barton'),('Sempron','2004','budget')],s=AP),
 a('Athlon 64 (K8)','2003','AMD\'s 64-bit x86 core with an integrated memory controller and HyperTransport.',[('Athlon 64','2003','Socket 754 and 939'),('Athlon 64 FX','2003','enthusiast'),('Athlon 64 X2','2005','first AMD dual-core desktop CPU')],s=AP,role='origin'),
 a('Phenom (K10)','2007','K10 core with shared L3 cache and 128-bit floating point units.',[('Phenom','2007','Agena'),('Phenom II','',''),('Athlon II','','')],s=AP),
 a('Bulldozer (FX)','2011','Module-based core family, ending with Excavator.',[('FX (Zambezi)','2011','Bulldozer'),('Piledriver','','second generation'),('Steamroller','','28 nm'),('Excavator','','last Bulldozer design')],s=AP),
 a('Bobcat, Jaguar and Puma','','Low-power cores for small and cheap devices, used in early APUs.',[('Bobcat','','Ontario and Zacate'),('Jaguar','','Kabini and Temash'),('Puma','','Beema and Mullins')]),
 a('Zen','2017','First Ryzen core, with simultaneous multithreading and Infinity Fabric.',[('Ryzen 1000 (Summit Ridge)','2017',''),('Threadripper 1000 (Whitehaven)','2017','TR4, 1950X')],s=AP,role='landmark'),
 a('Zen+','2018','Revised Zen on 12 nm.',[('Ryzen 2000 (Pinnacle Ridge)','2018',''),('Threadripper 2000 (Colfax)','2018','2990WX')],s=AP),
 a('Zen 2','2019','First chiplet design, on 7 nm.',[('Ryzen 3000 (Matisse)','2019',''),('Threadripper 3000 (Castle Peak)','2019','3970X, 3990X')],s=AP),
 a('Zen 3','2020','Redesigned cores on an optimised 7 nm process.',[('Ryzen 5000 (Vermeer)','2020',''),('Threadripper PRO 5000 (Chagall)','','sWRX8')],s=AP),
 a('Zen 3+','2022','Revision used in Ryzen 6000 mobile on 6 nm.',[('Ryzen 6000 mobile','2022','')]),
 a('Zen 4','2022','5 nm design behind Ryzen 7000 on socket AM5, with AVX-512.',[('Ryzen 7000 (Raphael)','2022',''),('Threadripper 7000 (Storm Peak)','2023','sTR5')],s=AP),
 a('Zen 5','2024','4 nm design with a full-width AVX-512 pipeline.',[('Ryzen 9000 (Granite Ridge)','2024',''),('Threadripper 9000','','9980X')],s=AP),
 a('Zen 6','','Sixth Zen generation on 3 nm, listed as upcoming.',[]),
]
CPU_KEEP=['Intel 4004','Intel 8086','Intel 80386','Intel Xeon','Apple M-series','Ryzen Threadripper']

N='https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units'
NG='https://en.wikipedia.org/wiki/GeForce'
AG='https://en.wikipedia.org/wiki/List_of_AMD_graphics_processing_units'
IA='https://en.wikipedia.org/wiki/Intel_Arc'
def g(n,mk,y,d,s,grp,v,**k): return E(n,mk,y,d,s,grp,[V(*x,mk=mk) for x in v],**k)
GN='Nvidia'; GR='AMD and ATI'; GIn='Intel'; GOt='Other makers'
GPU_NEW=[
 g('Fahrenheit (NV1 to RIVA TNT2)','Nvidia','1995','Nvidia\'s pre-GeForce cards.',N,GN,[('NV1','1995',''),('RIVA 128','1997',''),('RIVA TNT','1998',''),('RIVA TNT2','1999','TNT2 Ultra')]),
 g('Celsius (GeForce 256 and 2)','Nvidia','1999','First GeForce cards; the 256 was marketed as the first GPU.',N,GN,[('GeForce 256','1999','256 DDR'),('GeForce 2','2000','GeForce2 Ultra')],role='origin'),
 g('Kelvin (GeForce 3 and 4)','Nvidia','2001','Programmable-shader generation.',N,GN,[('GeForce 3','2001',''),('GeForce 4','2002','GeForce4 Ti 4600')]),
 g('Rankine (GeForce FX)','Nvidia','2003','GeForce FX 5000 series.',N,GN,[('GeForce FX 5000','2003','FX 5950 Ultra')]),
 g('Curie (GeForce 6 and 7)','Nvidia','2004','Last generation with AGP versions.',N,GN,[('GeForce 6','2004','6800 Ultra'),('GeForce 7','2005','7800 GTX 512')]),
 g('Tesla (GeForce 8 to 300)','Nvidia','2006','Unified-shader generation; the 8800 series was the first Direct3D 10 card.',NG,GN,[('GeForce 8','2006','8800 GTX, 8800 Ultra'),('GeForce 9','2008',''),('GeForce 100','2009','rebadged 9 series'),('GeForce 200','2008','GTX 280, GTX 285'),('GeForce 300','2009','rebranded 200 series')]),
 g('Fermi (GeForce 400 and 500)','Nvidia','2010','Fermi generation.',NG,GN,[('GeForce 400','2010','GTX 480'),('GeForce 500','2010','GTX 580, GTX 590')]),
 g('Kepler (GeForce 600 and 700)','Nvidia','2012','Kepler generation, which also introduced the GTX Titan.',NG,GN,[('GeForce 600','2012','GTX 680, GTX 690'),('GeForce 700','2013','GTX 780 Ti'),('GTX Titan family','2013','Titan, Titan Black, Titan Z')]),
 g('Maxwell (GeForce 900)','Nvidia','2014','Maxwell generation.',NG,GN,[('GeForce 900','2014','GTX 980, GTX Titan X')]),
 g('Pascal (GeForce 10)','Nvidia','2016','Pascal generation.',NG,GN,[('GeForce 10','2016','GTX 1080 Ti'),('Titan X Pascal / Titan Xp','2016–2017','')]),
 g('Volta (Titan V)','Nvidia','2017','Volta appears in the GeForce line only as the Titan V.',N,GN,[('Titan V','2017','')]),
 g('Turing (GeForce RTX 20 and GTX 16)','Nvidia','2018','First real-time ray tracing and DLSS; the GTX 16 series is Turing without RT cores.',NG,GN,[('GeForce RTX 20','2018','RTX 2080 Ti'),('GeForce GTX 16','2019','')],role='landmark'),
 g('Ampere (GeForce RTX 30)','Nvidia','2020','Ampere generation.',NG,GN,[('GeForce RTX 30','2020','RTX 3090 Ti')]),
 g('Ada Lovelace (GeForce RTX 40)','Nvidia','2022','Ada Lovelace generation.',NG,GN,[('GeForce RTX 40','2022','RTX 4090')]),
 g('Blackwell (GeForce RTX 50)','Nvidia','2025','Blackwell generation.',NG,GN,[('GeForce RTX 50','2025','RTX 5090')]),
 g('ATI Rage','ATI','1996','ATI\'s 3D Rage, Rage Pro and Rage 128 cards.',AG,GR,[('3D Rage','1996',''),('Rage Pro','',''),('Rage 128','1998','')]),
 g('Radeon R100 to R400','ATI','2000','First Radeon generations under ATI.',AG,GR,[('Radeon R100','2000',''),('Radeon R200','2001',''),('Radeon R300','2002',''),('Radeon R400','2004','')]),
 g('Radeon X1000 (R520)','ATI','2005','Last ATI-branded generation before the HD series.',AG,GR,[('Radeon X1000','2005','')]),
 g('TeraScale (Radeon HD 2000 to 6000)','AMD','2007','AMD bought ATI in 2006; TeraScale covers the HD 2000 to HD 6000 series.',AG,GR,[('Radeon HD 2000','2007','R600'),('Radeon HD 3000','2007',''),('Radeon HD 4000','2008','RV770'),('Radeon HD 5000','2009','Evergreen'),('Radeon HD 6000','2010','Northern Islands')]),
 g('Graphics Core Next (Radeon HD 7000 to Vega)','AMD','2012','GCN generations from Southern Islands to Vega.',AG,GR,[('Radeon HD 7000','2012','Southern Islands'),('Radeon 200','2013','Sea Islands'),('Radeon 300','2013–2014','Volcanic Islands'),('Radeon RX 400 / 500','2016','Polaris'),('Radeon RX Vega / VII','2017','Vega')]),
 g('RDNA (Radeon RX 5000)','AMD','2019','First RDNA generation, Navi 1x.',AG,GR,[('Radeon RX 5000','2019','RX 5700 XT')]),
 g('RDNA 2 (Radeon RX 6000)','AMD','2020','Navi 2x.',AG,GR,[('Radeon RX 6000','2020','')]),
 g('RDNA 3 (Radeon RX 7000)','AMD','2022','Navi 3x.',AG,GR,[('Radeon RX 7000','2022','')]),
 g('RDNA 4 (Radeon RX 9000)','AMD','2025','Navi 4x.',AG,GR,[('Radeon RX 9000','2025','')]),
 g('Arc Alchemist','Intel','2022','First Intel Arc generation (A-series).',IA,GIn,[('Arc A310 / A380','2022',''),('Arc A580','2023',''),('Arc A750 / A770','2022','8 GB and 16 GB A770')]),
 g('Arc Battlemage','Intel','2024','Second Arc generation (B-series).',IA,GIn,[('Arc B580','2024','December 2024'),('Arc B570','2025','January 2025')]),
]
