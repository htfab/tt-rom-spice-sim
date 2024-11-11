GDS_NAME = "tt_um_chip_rom.gds"

layout = pya.CellView.active().layout()

rom_cell = None
for cell in layout.each_cell():
    if cell.name == "tt_um_chip_rom" or cell.name.endswith("_tt_um_chip_rom"):
        rom_cell = cell

if not rom_cell:
    raise Exception("ROM cell not found")

pins = [
    ('clk', 198720, 154480),
    ('ena', 202560, 154480),
    ('rst_n', 194880, 154480),
    ('ui_in[0]', 191040, 154480),
    ('ui_in[1]', 187200, 154480),
    ('ui_in[2]', 183360, 154480),
    ('ui_in[3]', 179520, 154480),
    ('ui_in[4]', 175680, 154480),
    ('ui_in[5]', 171840, 154480),
    ('ui_in[6]', 168000, 154480),
    ('ui_in[7]', 164160, 154480),
    ('uio_in[0]', 160320, 154480),
    ('uio_in[1]', 156480, 154480),
    ('uio_in[2]', 152640, 154480),
    ('uio_in[3]', 148800, 154480),
    ('uio_in[4]', 144960, 154480),
    ('uio_in[5]', 141120, 154480),
    ('uio_in[6]', 137280, 154480),
    ('uio_in[7]', 133440, 154480),
    ('uio_oe[0]', 68160, 154480),
    ('uio_oe[1]', 64320, 154480),
    ('uio_oe[2]', 60480, 154480),
    ('uio_oe[3]', 56640, 154480),
    ('uio_oe[4]', 52800, 154480),
    ('uio_oe[5]', 48960, 154480),
    ('uio_oe[6]', 45120, 154480),
    ('uio_oe[7]', 41280, 154480),
    ('uio_out[0]', 98880, 154480),
    ('uio_out[1]', 95040, 154480),
    ('uio_out[2]', 91200, 154480),
    ('uio_out[3]', 87360, 154480),
    ('uio_out[4]', 83520, 154480),
    ('uio_out[5]', 79680, 154480),
    ('uio_out[6]', 75840, 154480),
    ('uio_out[7]', 72000, 154480),
    ('uo_out[0]', 129600, 154480),
    ('uo_out[1]', 125760, 154480),
    ('uo_out[2]', 121920, 154480),
    ('uo_out[3]', 118080, 154480),
    ('uo_out[4]', 114240, 154480),
    ('uo_out[5]', 110400, 154480),
    ('uo_out[6]', 106560, 154480),
    ('uo_out[7]', 102720, 154480),
]

print(f"Extracting cell {rom_cell.name} into {GDS_NAME}")
rom_cell.name = "tt_um_chip_rom"

labels = rom_cell.shapes(layout.layer(67, 25))
for pin_name, x, y in pins:
    labels.insert(pya.Text(pin_name, pya.Trans(x, y)))

rom_cell.write(GDS_NAME)
