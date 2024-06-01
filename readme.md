# Tildagon Bitmap Demo

1. Use the [st7789_mpy](https://github.com/russhughes/st7789_mpy) repo to convert your image to a compatible bitmap module
2. Import your newly created bitmap module (e.g. `from . import heartimage as heartimage`) with the output inside this module
3. `from tildagonos import tildagonos`
4. `tildagonos.tft.bitmap(heartimage, 50, 50)`
