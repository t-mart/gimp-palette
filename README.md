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

## Installing Palette Files

Palette files should probably be installed into the `palettes/` directory of
your user GIMP profile directory (instead of the application's installation
directory).

See where your platform's at <https://www.gimp.org/tutorials/GIMPProfile/>.

As of writing, this is currently:

> - In Windows 7 and later versions:
>   `C:\Users\{your_id}\AppData\Roaming\GIMP\2.10` (a.k.a.
>   `%APPDATA%/GIMP/2.10`)
> - In Linux: `/home/{your_id}/.config/GIMP/2.10` (a.k.a.
>   `$XDG_CONFIG_HOME/GIMP/2.10`)
> - In OSX: `/Users/{your_id}/Library/GIMP/2.10/` or possibly
>   `/Users/{your_id}/Library/Application Support/GIMP/2.10/` (this could depend
>   on the GIMP build you use).
>   (`a.k.a. NSApplicationSupportDirectory/GIMP/2.10`)
