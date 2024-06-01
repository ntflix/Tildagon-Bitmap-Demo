# Tildagon Bitmap Demo

> Works as-is with a sparkly heart emoji.

> Follow below instructions for your own image.

1. Use the `utils/img2bitmap.py` tool in [st7789_mpy](https://github.com/russhughes/st7789_mpy) repo to convert your image to a compatible bitmap module
    - Paste the output of this into a new `.py` file inside your app directory, e.g. `heartimage.py`.
2. Import your newly created bitmap module (e.g. `from . import heartimage as heartimage`) with the output inside this module
3. Import `tildagonos` with `from tildagonos import tildagonos`
4. Use `tildagonos.tft.bitmap(heartimage, 50, 50)`, replacing the `heartimage`, and the x and y values (`50`, `50`) with your desired values
    - _Found in [badge-2024-software](https://github.com/emfcamp/badge-2024-software/blob/86547c67cc232e2883dd9f5a4561d7c429c36df4/modules/gc9a01py.py)_
