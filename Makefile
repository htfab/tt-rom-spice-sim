# SPDX-License-Identifier: Apache-2.0
# Author: Uri Shaked

ifndef PDK_ROOT
$(error PDK_ROOT is not set.  Please set PDK_ROOT to the root directory of the PDK (e.g. ~/.volare))
endif

sim: tt_um_chip_rom.spice
	echo ".lib '$(PDK_ROOT)/sky130A/libs.tech/ngspice/sky130.lib.spice' tt" > pdk_lib.spice
	ngspice -b testbench.spice
	python rom_dump.py

.phony: sim

extract: openframe_project_wrapper.gds
	klayout -b -r rom_extract.py $<

tt_um_chip_rom.spice: tt_um_chip_rom.gds
	./extract_spice.sh
