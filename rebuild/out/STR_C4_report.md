# STR_C4 report: Craft & Art Supplies

Validated with `validate.py --v3` (OK, 0 errors). Size 366 KB.

**Counts, before to after:** departments 11 to 11; shelves 40 to 62; kinds 271 to 315; archetypes 379 to 284.

**Added:** category `ax` and `key` (11 steps plus a precedence note); `t` and `ax` on every department; `t` on every shelf and `ax` on shelves of four or more kinds; `tt` on every kind (hand-written, one question per group).

**Regrouped:** the long mixed shelves were split by one axis each: printing (by process), notions (fastenings, trims, fillings), beads (glass; natural/metal/plastic; findings; stringing; metal; tools), clay (fired, modelling, glazes, tools, kilns), glass (cold, hot, mosaic, casting, wax), leather (hides, tools, thread/dye/hardware), cutting tools, model supplies.

**Merged:** Sock yarn into Wool yarn (archetypes Jawoll and Alpaca Soft carried over).
**Renamed or split:** Printing block and plate to Relief printing block (plus new Intaglio plate); Trim to Braid, fringe and rickrack; Embroidery hoop to Embroidery hoop and frame; Bookbinding tools and materials to Bookbinding needle, awl and thread (plus Bookcloth and binding board, Bookbinding clamp and press); Pins, crimps and connectors to Head pin and eye pin (plus Crimp bead and crimp tube, Connector and link); Bail and bead cap to Bail (plus Bead cap); Stitching pony and leather thread to Stitching pony (plus Leather thread). All in `C4_renames.json`. No moves (`C4_moves.json` unchanged).

**Added kinds (45, each sourced):** drawing (Tracing paper, Drawing board, Drawing chalk and sanguine) from the Commons drawing-materials category; printmaking (Intaglio engraving tools, Lithography stone and plate, Squeegee); Four Treasures accessories; haberdashery (Snap fastener, Hook-and-loop tape, Hook and eye, Eyelet and grommet, Twill tape, Piping, Lace, Thimble); Knitting spool, Distaff, Backstrap loom; papier-mâché, papermaking mould, bookbinding; six bead kinds including Fuse bead; ceramics (Ceramic raw material, Slip and engobe, Ceramic decal, Gold and lustre, Pyrometric cone); Glass paint and silver stain, Lampwork mandrel, Candle wick trimmer, Leather mallet; Model decal, Cyanoacrylate glue, Fast-setting epoxy.

**Coverage references (fetched):** Wikipedia Printmaking, Four Treasures, Haberdashery, Knitting, Weaving, Spinning wheel, Embroidery, Paper craft, Papermaking, Bookbinding, Bead, Fuse beads, Pottery, Stained glass, Glassblowing, Glass bead making, Mosaic, Candle, Leather crafting, Pyrography, Floristry, Scale model, Airbrush; Commons drawing materials; Simple Wikipedia Paints; Kernowcraft jewellery tools.

**Archetypes demoted:** about 95 generic ones (e.g. H-frame easel, Reed, Roving, Kami, Stoneware clay body) became types in `tt`; about 45 maker ranges or SKUs (Pfeil gouges, YKK zip, Sew Simple FG304, HiyaHiya sets) moved to `r`. Bare names were prefixed with their maker. Added: Conté crayon, Rotring Rapidograph and Isograph, Hama, Perler, Pyssla. New brands: Conté à Paris, Beka, Fitzpatterns (the last two were missing from the index).

**Cross-links:** four required pairs (Gouache to F2, Inkstone to C5, Sewing pattern to I2, Rotary cutter to C7) plus Fuse bead to E1 and 28 internal links; all targets checked.

**Not done:** no retailer category page could be fetched (Blick, Jackson's, Tandy blocked), so craft tools, adhesives and model paints were checked against Wikipedia only; Floristry gave little. Few new named archetypes were added in variety departments for lack of fetched sources.
