# D1 Computers & Components: decided tree, v2 (shopper paths)

Category: D1 Computers & Components (domain D, Electronics). Membership test: a desktop, laptop or convertible computer, its components, peripherals (keyboards, mice, monitors, printers, scanners and multifunction printers, webcams, speech microphones, drawing tablets, 3D printers, barcode scanners; computer speakers are D3), storage, networking, uninterruptible power supplies, point-of-sale terminals, card readers and cash registers, hardware wallets and security keys, cables with standard connectors and adapters made to connect electronic devices, generic chargers (USB, GaN, Qi), loose electronic components and maker boards. A device whose screen and keyboard can separate is D2 if sold as a tablet with an optional keyboard, and D1 if the keyboard comes with it.

Structure (owner restructure to shopper paths, BRIEF.md "Owner decisions on navigation"; R-71): sub-family = the shopper path, the aisle a buyer opens (a whole computer, a part for a build, the desk setup, printing, storage carried or kept outside the machine, the network, cables, electronics and maker parts, point of sale and security devices); then leaf (the axis stated per sub-family; skipped where a sub-family holds about 12 kinds or fewer, C5(b)); then kind (the physical class buyers compare inside); then named form. Compatibility codes, quality tiers, makers and named forms are not kinds. Kinds and definitions are those of TREE_D1.md and the 18 HVMK kinds (119 in all, every one attested on a fetched page, R-70); definitions are reworded only where the move needs it. This replaces TREE_D1.md; the old ids map to the new ones in verify/out/D1R_crosswalk.tsv.

Ids (R-58, reissued once under R-71(b)): D1.n is a sub-family and D1.n.m a leaf; a kind is D1.n.m.kk, or D1.n.kk where a sub-family has no leaf. The kind number follows display order at this reissue.

## D1.1 Computers

Leaf axis: none (9 kinds, C5(b)). Kind order: current machines as shops list them (laptop, then desktop forms from large to small), then the build-it-yourself body and the single-board computer, then the historic classes, which carry an era tag.

- D1.1.01 Laptop: portable computer with its screen and keyboard in one folding body.
- D1.1.02 Tower desktop PC: complete desktop computer in a tower case, with the parts fitted.
- D1.1.03 All-in-one PC: complete computer with the screen and the computer in one body.
- D1.1.04 Mini PC: complete desktop computer in a small box, sold as a ready machine.
- D1.1.05 Barebone kit: case, board and power supply sold as the body of a machine, to which the buyer adds the rest.
- D1.1.06 Single-board computer: complete computer on one board that runs an operating system (a board that does is this kind even with a microcontroller beside it).
- D1.1.07 Keyboard computer: computer built into its keyboard (historic class).
- D1.1.08 Pocket computer: programmable pocket computer (historic class; provisional until attested).
- D1.1.09 Trainer kit: kit sold to teach computing (historic class; provisional until attested).

## D1.2 PC parts

Leaf axis: build slot, the parts list a builder fills, in the order of PCPartPicker's list (CPU, CPU cooler, motherboard, memory, storage, video card, case, power supply) [S01], then the expansion cards and internal cables that UK and Japanese shops carry in the same parts tree [S02, S06]. Compatibility codes (socket, chipset, DDR and PCIe generation, M.2 length, board, case and PSU form factor) are attributes, not kinds.

### D1.2.1 Processors

- D1.2.1.01 Processor: central processing chip (CPU) of a computer.

### D1.2.2 Cooling

- D1.2.2.01 Air CPU cooler: heatsink with a fan that cools a processor by air.
- D1.2.2.02 All-in-one liquid cooler: sealed pump, radiator and block unit that cools a processor or graphics chip by liquid.
- D1.2.2.03 Custom-loop parts: separate parts (blocks, radiators, pumps, tubing) for building a liquid cooling loop.
- D1.2.2.04 Case fan: fan fitted to a computer case to move air.
- D1.2.2.05 Thermal paste: paste applied between a chip and its cooler.
- D1.2.2.06 Thermal pad: solid sheet of thermal interface material cut to sit between a chip or drive and its cooler.
- D1.2.2.07 M.2 heatsink: heat spreader fitted to an M.2 drive.
- D1.2.2.08 Fan controller: unit that sets the speed of case fans.

### D1.2.3 Motherboards

- D1.2.3.01 Motherboard [mainboard, Mainboard]: main circuit board of a computer, sold alone.
- D1.2.3.02 Board with CPU fitted: one object sold with the CPU soldered or fitted to the board, to be built into a machine.

### D1.2.4 Memory

- D1.2.4.01 DIMM memory module: full-size memory module for desktop computers.
- D1.2.4.02 SODIMM memory module: small-outline memory module for notebooks and small machines.

### D1.2.5 Internal storage

- D1.2.5.01 Internal SSD: solid-state drive fitted inside a computer, of any interface or size (M.2 or 2.5-inch).
- D1.2.5.02 Internal HDD: spinning-disk drive fitted inside a computer.

### D1.2.6 Graphics cards

- D1.2.6.01 Graphics card [video card; グラフィックボード; ビデオカード]: expansion card that renders images for a display or computes in place of a CPU, with or without display outputs.
- D1.2.6.02 External GPU enclosure: housing that holds a graphics card outside the computer and connects to it.

### D1.2.7 Cases

- D1.2.7.01 PC case: enclosure that holds a computer's board, drives and cards.

### D1.2.8 Power supplies

- D1.2.8.01 PC power supply unit: power supply fitted in a computer case to feed its parts.

### D1.2.9 Expansion cards

- D1.2.9.01 Sound card: card fitted inside the computer that handles audio (internal only; an external or USB one is D3).
- D1.2.9.02 Network adapter card: card fitted inside the computer that adds a network connection.
- D1.2.9.03 Video capture card: card fitted inside the computer that records a video signal.
- D1.2.9.04 I/O expansion card: card fitted inside the computer that adds ports.
- D1.2.9.05 TV tuner card: card fitted inside the computer that receives broadcast television.

### D1.2.10 Internal cables

- D1.2.10.01 Internal PC cable: cable that connects parts inside a computer case, including the PCIe riser cable by default.

## D1.3 Peripherals and desk setup

Leaf axis: device family on the desk (what the user handles or sets up beside the computer), with the mechanical-keyboard hobby's kits and parts as their own shelf beside keyboards, as keyboard shops show them (keyboards, kits, switches, keycaps, plates and stabilisers).

### D1.3.1 Keyboards

- D1.3.1.01 Keyboard: key-based input device sold ready to type (size class is an attribute).
- D1.3.1.02 Numeric keypad: separate input device with number keys.
- D1.3.1.03 Macro pad: separate input device of a few programmable keys, dials or sliders used for shortcuts, not for typing.

### D1.3.2 Keyboard kits and parts

- D1.3.2.01 Keyboard kit: case, plate and circuit board sold to be built into a keyboard.
- D1.3.2.02 Linear keyboard switch: loose keyboard switch with a smooth press and no bump or click.
- D1.3.2.03 Tactile keyboard switch: loose keyboard switch with a felt bump and no click.
- D1.3.2.04 Clicky keyboard switch: loose keyboard switch with a felt bump and an audible click.
- D1.3.2.05 Keycap set: set of keycaps for a keyboard.
- D1.3.2.06 Keyboard plate: plate that holds switches in a keyboard.
- D1.3.2.07 Keyboard stabiliser: stabiliser for the long keys of a keyboard.

### D1.3.3 Mice and pointing

- D1.3.3.01 Mouse: hand-held pointing device moved over a surface.
- D1.3.3.02 Trackball: pointing device operated by a fixed ball.
- D1.3.3.03 Pen tablet: drawing tablet used with a pen, with or without a built-in screen (a pen display is a pen tablet with a screen).

### D1.3.4 Monitors

- D1.3.4.01 Monitor: display sold for use with a computer.

### D1.3.5 Webcams, microphones and capture

- D1.3.5.01 Webcam: camera made for use with a computer.
- D1.3.5.02 Speech microphone: microphone made for speech, calls or streaming.
- D1.3.5.03 Video capture device: external device that records a video signal into a computer (connection is an attribute).

### D1.3.6 Docks and desk accessories

- D1.3.6.01 Docking station: base that carries power delivery and several outputs for a laptop, which an adapter or hub does not.
- D1.3.6.02 KVM switch: switch that shares one keyboard, display and mouse between several computers.
- D1.3.6.03 Monitor arm or stand: arm, bracket or stand made to hold one screen.
- D1.3.6.04 Laptop stand: stand or riser without fans made to hold one laptop at a height or angle.
- D1.3.6.05 Laptop cooler: pad or stand with fans that cools a laptop.

## D1.4 Printing and scanning

Leaf axis: none (8 kinds, C5(b)). Kind order: machines (printing on paper, scanning, then 3D printing), then the supplies made for them, which shops sell in the same aisle ("printers, ink and toner").

- D1.4.01 Printer: machine that prints from a computer.
- D1.4.02 Multifunction printer: machine that prints and scans (and copies) for use with a computer.
- D1.4.03 Wide-format printer: printer that prints on roll or sheet media wider than A3, for drawings and posters.
- D1.4.04 Scanner: machine that scans documents or images into a computer.
- D1.4.05 3D printer: machine that builds objects by additive manufacturing.
- D1.4.06 Ink cartridge: ink supply made for one printer type.
- D1.4.07 Toner cartridge: toner supply made for one printer type.
- D1.4.08 3D-printer filament: filament made for 3D printers.

## D1.5 External storage and media

Leaf axis: none (9 kinds, C5(b)). Kind order: external drives, carried flash media, readers and housings, network storage, then disc and legacy drives.

- D1.5.01 External SSD: solid-state drive in its own case, connected from outside.
- D1.5.02 External HDD: spinning-disk drive in its own case, connected from outside.
- D1.5.03 USB flash drive: small flash storage device that plugs into a USB port.
- D1.5.04 Memory card: flash card of a standard format (SD, microSD, CompactFlash, CFexpress); a proprietary console-only card is D5.
- D1.5.05 Memory-card reader: device that reads memory cards and connects to a computer.
- D1.5.06 Drive enclosure: housing, sold empty, that turns a bare drive into an external drive.
- D1.5.07 NAS: network-attached storage device that holds drives and serves files over a network (a recorder sold only to run security cameras is B8).
- D1.5.08 Optical drive: drive that reads or writes discs, fitted in a drive bay or in its own case (connection is an attribute).
- D1.5.09 Floppy disk drive: drive that reads or writes floppy disks, internal or in its own case (connection is an attribute).

## D1.6 Networking and backup power

Leaf axis: none (8 kinds, C5(b)). Kind order: the path from the provider's line to the devices (modem, router, wireless coverage, wired distribution, power over the network), then the UPS that keeps the setup running.

- D1.6.01 Modem: device that connects a home network to a provider's cable, DSL, fibre or cellular line; one with a built-in router is this kind.
- D1.6.02 Wireless router: network device that routes traffic and provides wireless access.
- D1.6.03 Access point: network device that adds wireless access to a wired network.
- D1.6.04 Range extender: network device that receives a wireless signal and rebroadcasts it to widen coverage.
- D1.6.05 Network switch: network device that connects wired devices on a local network.
- D1.6.06 Powerline adapter: adapter that carries a network connection over a building's mains wiring, sold in pairs or kits.
- D1.6.07 PoE injector: device that adds power to an Ethernet cable to feed a powered network device.
- D1.6.08 UPS: uninterruptible power supply that keeps equipment running through a mains failure (a portable power station is B7).

## D1.7 Cables, adapters and chargers

Leaf axis: none (10 kinds, C5(b); connector family becomes the leaf axis if harvest takes the sub-family above about 12 kinds). Kind order: cables by connector family (data and video, network, audio and music), then adapters and hubs, then generic chargers.

- D1.7.01 USB cable: cable with USB connectors.
- D1.7.02 HDMI cable: cable with HDMI connectors.
- D1.7.03 DisplayPort cable: cable with DisplayPort or Mini DisplayPort connectors.
- D1.7.04 LAN cable: network cable with standard patch connectors.
- D1.7.05 Audio cable: audio cable with standard connectors.
- D1.7.06 Instrument cable: cable with standard connectors for connecting an instrument.
- D1.7.07 Microphone cable: cable with standard connectors for connecting a microphone.
- D1.7.08 MIDI cable: cable with MIDI connectors.
- D1.7.09 Adapter or hub: device that converts one standard connector to another or splits one port into several.
- D1.7.10 Generic charger: charger for many devices (USB, GaN or Qi); a charger made for one device follows it.

## D1.8 Electronics and maker parts

Leaf axis: component family as the distributor catalogue groups it, maker boards and kits first (provisional until the Mouser harvest; loose components are carried to the Mouser class level).

### D1.8.1 Maker boards and kits

- D1.8.1.01 Microcontroller board: board that runs one program on a microcontroller.
- D1.8.1.02 Add-on board for a maker board: board made to plug onto one maker-board family's header (HAT, shield, FeatherWing).
- D1.8.1.03 Electronics component kit: component kit without an experiment programme.

### D1.8.2 Passive components

- D1.8.2.01 Capacitor: passive component that stores charge.
- D1.8.2.02 Resistor: passive component that resists current.
- D1.8.2.03 Inductor: passive component that stores energy in a magnetic field.
- D1.8.2.04 Potentiometer: loose variable resistor set by a shaft, slider or trimmer screw.
- D1.8.2.05 Thermistor: loose resistor whose resistance changes with temperature (NTC or PTC).
- D1.8.2.06 Varistor: loose voltage-dependent resistor used to absorb surges.
- D1.8.2.07 Transformer: loose component that transfers power or signal between coils.
- D1.8.2.08 Crystal or oscillator: loose frequency-control component (quartz crystal, resonator or oscillator).

### D1.8.3 Semiconductors

- D1.8.3.01 Microcontroller chip: loose integrated circuit that holds a processor, memory and ports.
- D1.8.3.02 MOSFET: loose transistor used as a switch or amplifier.
- D1.8.3.03 Diode: loose semiconductor that lets current pass one way (rectifier, Zener, Schottky).
- D1.8.3.04 LED: loose light-emitting diode component for circuits (a lamp or bulb is B-lighting).

### D1.8.4 Electromechanical and interconnect

- D1.8.4.01 Relay: loose switch operated by an electromagnet.
- D1.8.4.02 Component connector: loose connector for circuit boards and wiring.

### D1.8.5 Sensors, RF and identification

- D1.8.5.01 Sensor: loose component that senses a physical quantity.
- D1.8.5.02 Blank RFID tag or card: unissued RFID tag or card (an issued card is F5).

## D1.9 Point of sale and security devices

Leaf axis: none (6 kinds, C5(b)). Kind order: the till and what reads at it, then the devices that hold a person's keys. This sub-family is not in the owner's list of eight: the key names these objects for D1 and none of the eight aisles is where a buyer looks for them (shops sell them as a point-of-sale aisle and as security keys).

- D1.9.01 Point-of-sale terminal: terminal at which a sale is rung up and paid.
- D1.9.02 Payment card reader: device that reads payment cards.
- D1.9.03 Cash register: till that records sales and holds cash.
- D1.9.04 Barcode scanner: device that reads barcodes, at a till or for stock.
- D1.9.05 Security key: device used to prove identity when signing in.
- D1.9.06 Hardware wallet: device that holds cryptocurrency keys.

## D1.10 Parts and accessories made for one computer or peripheral

Leaf axis: none (3 kinds); object served; exempt from the level-1 axis (C5(d)). It holds only parts made for one computer or peripheral that fit none of the shopper paths above.

- D1.10.01 Laptop AC adapter: power adapter made for one laptop.
- D1.10.02 Laptop battery: battery made for one laptop.
- D1.10.03 Laptop sleeve or case: sleeve or case made to hold or protect one laptop.

## Precedence inside D1

- **Shopper path first.** A kind sits in the aisle where a buyer looks for it (R-71). Inside PC parts the leaves are the build slots; a standard part that fits many machines (an M.2 SSD, a SODIMM) is a PC part whatever machine it goes into, never a part "made for one" computer.
- **Internal against external storage.** A drive fitted inside a computer, in a bay or an M.2 slot, is internal storage in PC parts (internal SSD D1.2.5.01, internal HDD D1.2.5.02), of any interface or size. The same drive class in its own case, connected from outside, is external storage (external SSD D1.5.01, external HDD D1.5.02). A drive enclosure sold empty is D1.5.06; one sold with a drive inside is an external drive. USB flash drives, memory cards, card readers and NAS are D1.5. Optical and floppy drives are D1.5 (D1.5.08, D1.5.09) whether fitted in a bay or in their own case, because buyers shop disc drives as their own class apart from the build's storage slot (PCPartPicker lists optical drives under accessories, not under storage [S01]); connection is an attribute. An M.2 heatsink is cooling (D1.2.2.07).
- **Monitor against TV (D3).** A display sold for use with a computer is a monitor (D1.3.4.01), whatever its size, panel or refresh rate, portable USB monitors included; a TV, projector or smart display is D3 even when it has computer inputs. The maker's sales class decides. A pen display is a pen tablet (D1.3.3.03); an electronic writing tablet is D2. A TV-tuner card fitted inside the computer is D1 (D1.2.9.05).
- **Dock against hub.** A docking station (D1.3.6.01) is a base that powers the laptop (power delivery from its own supply) and gives it several outputs; it is desk setup. An adapter or hub (D1.7.09) converts or splits ports and does not power the laptop; a hub with a pass-through charging port that only passes on another charger's power is an adapter or hub. A KVM switch (D1.3.6.02) shares a keyboard, display and mouse between computers and is desk setup; a network switch (D1.6.05) is networking.
- **Keyboard part against keyboard.** A keyboard sold ready to type, switches and keycaps fitted, is a keyboard (D1.3.1.01; a gaming or hot-swap keyboard included, size class an attribute). Anything sold to be assembled by the buyer into a keyboard is a keyboard kit (D1.3.2.01) when it is the case, plate and circuit board, and otherwise the part it is: loose switches by feel (linear D1.3.2.02, tactile D1.3.2.03, clicky D1.3.2.04), keycap set (D1.3.2.05), plate (D1.3.2.06), stabiliser (D1.3.2.07). These keyboard parts sit on the keyboard shelf, not in D1.10. A macro pad (D1.3.1.03) has a few programmable keys or dials for shortcuts; a numeric keypad (D1.3.1.02) has number keys.
- **A component sold loose against a part made for one device.** A component sold loose for any circuit (capacitor, resistor, diode, LED, connector, relay, sensor, microcontroller chip) is Electronics and maker parts (D1.8) whatever device it ends up in. A part made for one computer, peripheral or board family is filed in that device's aisle where one exists (internal PC cable D1.2.10.01, cooling D1.2.2, keyboard parts D1.3.2, ink and toner D1.4.06 and D1.4.07, add-on board for one maker-board family D1.8.1.02) and otherwise in D1.10 (laptop AC adapter, laptop battery, laptop sleeve or case).
- **Computer against board.** A board that runs an operating system and is sold to run as it is, is a single-board computer (D1.1.06), even with a microcontroller beside the processor and even when a maker shop sells it; a board that runs one program is a microcontroller board (D1.8.1.01). A motherboard sold with its CPU soldered or fitted, to which the buyer adds memory, storage and a case, is a board with CPU fitted (D1.2.3.02). A case, board and power supply sold as the body of a machine is a barebone kit (D1.1.05), not a PC part.
- **Board and CPU.** A CPU and a board sold together as a pair are a mixed set filed by the item of greatest value (processor D1.2.1.01 or motherboard D1.2.3.01) with a bundle variant. A compute accelerator card with no display output is a graphics card (D1.2.6.01) with zero display outputs; an external GPU enclosure is D1.2.6.02 in the graphics slot.
- **Form factor and compatibility codes.** Form factor is a kind boundary only where buyers never compare across it and one cannot replace the other in the same slot (DIMM D1.2.4.01 against SODIMM D1.2.4.02); it is an attribute where buyers compare across it inside one kind (ATX and SFX supply in D1.2.8.01, ATX and Mini-ITX board in D1.2.3.01, case size classes in D1.2.7.01, keyboard size classes in D1.3.1.01). Socket, chipset, DDR and PCIe generation and M.2 length are attributes; an M.2 NVMe drive and a 2.5-inch SATA drive are both an internal SSD (D1.2.5.01); internal SSD and HDD are separate kinds, as are air (D1.2.2.01) and all-in-one liquid (D1.2.2.02) coolers.
- **Internal card against external device.** A sound card is internal only (D1.2.9.01); an external or USB sound card, audio interface or converter is D3. A video capture card fitted inside the computer is D1.2.9.03; an external capture device is D1.3.5.03.
- **Webcams and microphones.** A webcam made for computers is D1.3.5.01; a network or surveillance camera is B8. A microphone made for speech, calls or streaming is a speech microphone (D1.3.5.02); one made for music is E3, and one sold for both is filed by the maker's stated first use. Headphones, headsets and computer speakers are D3.
- **Desk accessories against parts.** A stand, riser, arm or cooling pad made to hold one screen or laptop on the desk is desk setup (monitor arm or stand D1.3.6.03, laptop stand D1.3.6.04, laptop cooler D1.3.6.05). A sleeve or case made to hold or protect one laptop is D1.10.03. Furniture, racks and shelves are never parts.
- **Printing.** Printers, scanners, multifunction and wide-format printers (D1.4.01 to D1.4.04) are D1 whatever the connection of a given model; copiers, shredders, laminators, label makers and label printers are C5, and so is paper. Ink and toner cartridges (D1.4.06, D1.4.07) and 3D-printer filament (D1.4.08) are filed with the printers. A barcode scanner reads codes at a till or for stock and is D1.9.04; a scanner images pages into a computer (D1.4.04).
- **Cables and chargers.** A cable with standard connectors (USB D1.7.01, HDMI D1.7.02, DisplayPort D1.7.03, LAN D1.7.04, audio D1.7.05, instrument D1.7.06, microphone D1.7.07, MIDI D1.7.08) is D1.7 whatever device it serves; patch cables are filed by their connector family. A cable with a proprietary connector made for one device follows that device. A cable that connects parts inside a computer case is an internal PC cable (D1.2.10.01), the PCIe riser cable included until a fetched seller page says otherwise. A generic charger (D1.7.10) serves many devices; a laptop's own AC adapter (D1.10.01) or battery (D1.10.02) is a part made for one computer; a charger made for one phone or a power bank is D2, a charger for standard-size cells is C8, and a cordless-platform charger is C1.
- **Network and power.** A NAS is external storage (D1.5.07), not networking; a recorder sold only to run security cameras is B8. A modem with a built-in router is a modem (D1.6.01). A UPS is D1.6.08; home batteries, inverters, solar equipment and portable power stations are B7.
- **Media and cards.** A memory card of a standard format (D1.5.04) or a USB flash drive (D1.5.03) is D1 whatever device it is sold for; a proprietary console-only card is a D5 part. A blank RFID tag or card (D1.8.5.02) is D1; an issued payment, access or transit card is F5, but a hardware wallet (D1.9.06) or security key (D1.9.05) is D1.
- **Kits and tools.** Component kits without an experiment programme are D1 (D1.8.1.03); experiment kits are C6 and play robots and coding toys E1. Electronics instruments, soldering irons, multimeters and bench power supplies are C1.
- **Other categories.** A programmable pocket computer is D1 (D1.1.08); a PDA or electronic organiser is D2. A handheld gaming PC is D5 with a PC operating-system attribute; game controllers and VR headsets are D5, while a gaming keyboard, mouse, laptop or desktop is D1. A computer whose keyboard comes with it is D1 (laptop D1.1.01); a tablet sold with an optional keyboard is D2.
