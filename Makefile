# SPDX-License-Identifier: Apache-2.0
# Author: Uri Shaked

GDS_FILE ?= tt_ihp_wrapper.gds

ifndef PDK_ROOT
$(error PDK_ROOT is not set.  Please set PDK_ROOT to the root directory of the PDK (e.g. ~/.volare))
endif

sim: tt_um_chip_rom.spice
	echo ".lib '$(PDK_ROOT)/ihp-sg13g2/libs.tech/ngspice/models/cornerMOSlv.lib' mos_tt" > pdk_lib.spice
	echo ".lib '$(PDK_ROOT)/ihp-sg13g2/libs.tech/ngspice/models/cornerCAP.lib' cap_typ" >> pdk_lib.spice
	ngspice -b testbench.spice
	python rom_dump.py

extract: $(GDS_FILE)
	klayout -b -r rom_extract.py $<

tt_um_chip_rom.spice: tt_um_chip_rom.gds
	./extract_spice.sh

.PHONY: sim extract
