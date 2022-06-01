import json
from pathlib import Path

from gp import Color, Palette

if __name__ == "__main__":
    root = Path(__file__).parent
    json_path = root / "gogh_themes.json"
    with json_path.open("r") as json_file:
        data = json.load(json_file)
    for theme in data["themes"]:
        name = f"Gogh - {theme['name']}"
        colors = []
        for color_name, color_hex in theme.items():
            if color_name == "name":
                continue
            colors.append(Color.from_hex(hexstr=color_hex, name=color_name))
        palette = Palette(name=name, colors=colors)
        outpath = root / "Gogh" / f"{name}.gpl"
        outpath.parent.mkdir(exist_ok=True)
        with outpath.open("wb") as outfile:
            outfile.write(palette.encode())
        print(name)
