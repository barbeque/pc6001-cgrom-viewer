# internal 6847 CGROM
# column-major order

from PIL import Image
from bitstring import BitArray

CHAR_WIDTH = 4
CHAR_HEIGHT = 8

offset = 5
ptr = offset * (CHAR_WIDTH * CHAR_HEIGHT) # 5x7 bits makes no sense.

with open('CGROM60.60', 'rb') as f:
    a = BitArray(bytearray(f.read()))

x = Image.new('1', (CHAR_WIDTH, CHAR_HEIGHT))

for column in range(0, CHAR_WIDTH):
    for row in range(0, CHAR_HEIGHT):
        value = a[ptr + (column * CHAR_HEIGHT) + row]
        x.putpixel((column, row), value)

x.save('out.png')