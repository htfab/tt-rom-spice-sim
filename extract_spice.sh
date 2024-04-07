#! /bin/bash
magic -dnull -noconsole -rcfile $PDK_ROOT/sky130A/libs.tech/magic/sky130A.magicrc << EOF
gds read tt_um_chip_rom.gds
load tt_um_chip_rom
select cell tt_um_chip_rom
extract path extfiles
extract all
ext2spice lvs
ext2spice -p extfiles
EOF
