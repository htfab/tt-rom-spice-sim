#! /bin/bash
#klayout -b -r $PDK_ROOT/ihp-sg13g2/libs.tech/klayout/tech/lvs/sg13g2_full.lylvs -rd in_gds=tt_um_chip_rom.gds -rd target_netlist=tt_um_chip_rom.spice -rd run_mode=deep -rd cdl_file=tt_um_chip_rom_ports.spice
klayout -b -r sg13g2_full.lylvs -rd in_gds=tt_um_chip_rom.gds -rd target_netlist=tt_um_chip_rom.spice -rd run_mode=deep -rd net_only=true
sed -i 's/^M\$/X&/' tt_um_chip_rom.spice
