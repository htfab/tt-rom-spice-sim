GDS_NAME = "tt_um_chip_rom.gds"

layout = pya.CellView.active().layout()

rom_cell = None
for cell in layout.each_cell():
    if cell.name == "tt_um_chip_rom" or cell.name.endswith("_tt_um_chip_rom"):
        rom_cell = cell

if not rom_cell:
    raise Exception("ROM cell not found")

print(f"Extracting cell {rom_cell.name} into {GDS_NAME}")
rom_cell.name = "tt_um_chip_rom"
rom_cell.write(GDS_NAME)
