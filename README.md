# tt-rom-spice-sim

Simulates Tiny Tapeout ROM with ngspice, to dump the ROM contents.

## Dumping the ROM contents

To run the simulation:

```
make
```

The simulation should take a few minutes to run. At the end, the ROM contents will be dumped to the console.

It will also generate a `rom.bin` file with the ROM contents.

## Extracting the ROM from a Tiny Tapeout GDS file

Copy `tt_ihp_wrapper.gds` to the current directory, and run `make extract`. This will extract the ROM contents from the GDS file into `tt_um_chip_rom.gds` using a [klayout script](./rom_extract.py).

You can also extract from a specific GDS os OAS file by running `make extract GDS_FILE=yourfile.gds` or `make extract GDS_FILE=yourfile.oas`.
