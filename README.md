# gimp-palette

A Python library to create `.gpl` GIMP palette files.

## Example Usage

```python
from gp import Color, Palette

palette = Palette(
    name="foo",
    colors=[
        Color.from_hex("#aabbcc", "color1"),
        Color(red=1, green=2, blue=3, name="color2"),
    ],
)

with open("foo.gpl", "wb") as f:
    f.write(palette.encode())
```

(see also `example/__main__.py`)
