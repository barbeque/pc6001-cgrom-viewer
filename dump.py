# internal 6847 CGROM
# column-major order

from PIL import Image
from bitstring import BitArray

# http://eighttails.seesaa.net/article/399694802.html
# says the PC-6001 font is 8 x 12 pixels, which it is, but the actual tile
# in the ROM seems to be 8 x 16 to keep things square
CHAR_WIDTH = 8
CHAR_HEIGHT = 16

# [y * width + x]

NUM_CHARS = 256 # number of chars in set to extract
DUMP_COLUMNS = 16
DUMP_ROWS = (NUM_CHARS // DUMP_COLUMNS)
DUMP_WIDTH = CHAR_WIDTH * DUMP_COLUMNS
DUMP_HEIGHT = CHAR_HEIGHT * DUMP_ROWS
all = Image.new(mode='1', size=(DUMP_WIDTH, DUMP_HEIGHT))

with open('CGROM60.60', 'rb') as f:
    rom = bytearray(f.read())
    a = BitArray(rom)

for character in range(0, 256):
    ptr = character * (CHAR_WIDTH*CHAR_HEIGHT) # tile molester says so, so..

    x = Image.new('1', (CHAR_WIDTH, CHAR_HEIGHT))

    for column in range(0, CHAR_WIDTH):
        for row in range(0, CHAR_HEIGHT):
            value = a[ptr + (row * CHAR_WIDTH) + column]
            x.putpixel((column, row), value)

            all_x = int((character % DUMP_COLUMNS) * CHAR_WIDTH + column)
            all_y = int((character // DUMP_ROWS) * CHAR_HEIGHT + row)
            all.putpixel((all_x, all_y), value)

    formatted = format(character, '03')
    x.save(f'out-{formatted}.png')
    all.save('all.png')