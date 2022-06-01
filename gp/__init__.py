from __future__ import annotations
from typing import Optional
from attrs import frozen, field


@frozen(kw_only=True)
class Color:
    red: int
    green: int
    blue: int
    name: Optional[str] = field(default=None)

    def encode(self) -> bytes:
        line = f"{self.red: >3} {self.green: >3} {self.blue: >3}"
        if self.name is not None:
            line += f" {self.name}"
        line += "\n"
        return line.encode("utf-8")

    @classmethod
    def from_hex(cls, hexstr: str, name: str) -> Color:
        hexv = int(hexstr.removeprefix("#"), 16)
        red, green, blue = ((hexv >> (8 * shift)) & 0xFF for shift in range(2, -1, -1))
        return Color(name=name, red=red, green=green, blue=blue)


@frozen(kw_only=True)
class Palette:
    name: str
    comment_lines: Optional[list[str]] = field(default=None)
    colors: list[Color]
    columns: Optional[int] = field(default=None)

    def encode(self) -> bytes:
        # .gpl files terminate lines with just a \n (not a windows \r\n)
        # to keep local platform choice from expanding \n into \r\n, we
        # explicitly return bytes in this method.
        out = b"GIMP Palette\n"

        out += f"Name: {self.name}\n".encode("utf-8")

        if self.columns is not None:
            out += f"Columns: {self.columns}\n".encode("utf-8")

        out += "#\n".encode("utf-8")

        if self.comment_lines is not None:
            for comment_line in self.comment_lines:
                out += f"# {comment_line.rstrip()}\n".encode("utf-8")
            out += "#\n".encode("utf-8")

        for color in self.colors:
            out += color.encode()

        return out
