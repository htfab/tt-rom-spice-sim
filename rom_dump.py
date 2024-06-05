# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2024, Tiny Tapeout LTD
# Author: Uri Shaked

import csv

def read_byte(data):
    result = 0
    for i, bit in enumerate(data):
        if bit >= 1.7:
            result |= 1 << i
        elif bit >= 0.1 or bit < -0.1: 
            return None
    return result

data = {}
with open("rom_signals.txt", 'r') as romfile:
    reader = csv.reader(romfile, delimiter=' ', skipinitialspace=True)
    headers = next(reader)
    for row in reader:
        row = dict(zip(headers, map(float, row[:-1])))
        addr = read_byte([row[f'addr{i}'] for i in range(8)])
        value = read_byte([row[f'data{i}'] for i in range(8)])
        if addr is not None and value is not None:
          data[addr] = value

rom_data = bytearray(256)
for byte_idx in range(0, len(rom_data)):
    rom_data[byte_idx] = data.get(byte_idx, 0)

with open("rom.bin", 'wb') as romfile:
    romfile.write(rom_data)

# The first 32 bytes are 7-segment encoded, so just dump them as hex
print("".join(f"{byte:02x}" for byte in rom_data[:32]))
print("")

# dump text
rom_text = rom_data[32:128].rstrip(b"\0").decode('ascii')
print(rom_text)
