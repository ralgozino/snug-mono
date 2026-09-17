#!/usr/bin/env python3
"""Build Snug Mono from upstream Atkinson Hyperlegible Mono.

Snug Mono narrows the character cell and moves each glyph to the centre of the
new cell. The letterforms do not change. Only the empty space around them
becomes smaller.

Usage:  python3 build.py [factor]      # factor defaults to 0.91
"""
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from fontTools.ttLib import TTFont

UPSTREAM = ("https://raw.githubusercontent.com/googlefonts/"
            "atkinson-hyperlegible-next-mono/main/fonts/variable/")
SOURCES = {
    "AtkinsonHyperlegibleMono[wght].ttf": "SnugMono[wght].ttf",
    "AtkinsonHyperlegibleMono-Italic[wght].ttf": "SnugMono-Italic[wght].ttf",
}
RENAME = [("Atkinson Hyperlegible Mono", "Snug Mono"),
          ("AtkinsonHyperlegibleMono", "SnugMono")]
NAME_IDS = (1, 3, 4, 6, 16, 25)  # family, unique id, full, PostScript, typographic, variations prefix

ROOT = Path(__file__).parent
CACHE = ROOT / "build"
OUT = ROOT / "fonts"


def download(name):
    """Always get the current upstream file, so a rebuild picks up new releases."""
    CACHE.mkdir(exist_ok=True)
    dst = CACHE / name
    url = UPSTREAM + urllib.parse.quote(name)
    print(f"  download {name}")
    urllib.request.urlretrieve(url, dst)
    return dst


def tighten(font, factor):
    """Narrow every cell and move the outlines to keep them centred."""
    glyf, hmtx = font["glyf"], font["hmtx"]
    old = max(advance for advance, _ in hmtx.metrics.values())
    new = round(old * factor)
    shift = (new - old) // 2

    # Move all outlines, marks included, so stacked accents stay aligned.
    for name in font.getGlyphOrder():
        glyph = glyf[name]
        if glyph.numberOfContours > 0:
            glyph.coordinates.translate((shift, 0))

    # Composite glyphs read the bounds of their parts, so recalculate second.
    for name in font.getGlyphOrder():
        glyph = glyf[name]
        glyph.recalcBounds(glyf)
        advance, _ = hmtx[name]
        hmtx[name] = (new if advance else 0,
                      glyph.xMin if glyph.numberOfContours else 0)

    font["hhea"].advanceWidthMax = new
    font["OS/2"].xAvgCharWidth = new
    return old, new, shift


def rename(font):
    """Give the font its own family name, as the SIL OFL requires."""
    table = font["name"]
    for record in list(table.names):
        if record.nameID not in NAME_IDS:
            continue
        value = str(record)
        for old, new in RENAME:
            value = value.replace(old, new)
        table.setName(value, record.nameID, record.platformID,
                      record.platEncID, record.langID)

    for record in list(table.names):  # keep the upstream notice, add ours
        if record.nameID == 0 and "Snug Mono" not in str(record):
            table.setName(f"{record} Snug Mono is a modified version of that "
                          "software, with a narrower character cell.",
                          0, record.platformID, record.platEncID, record.langID)


def main():
    factor = float(sys.argv[1]) if len(sys.argv) > 1 else 0.91
    OUT.mkdir(exist_ok=True)
    version = None
    for src, dst in SOURCES.items():
        font = TTFont(download(src))
        version = font["name"].getDebugName(5)
        old, new, shift = tighten(font, factor)
        rename(font)
        font.save(OUT / dst)

        upem = font["head"].unitsPerEm
        cap = font["OS/2"].sCapHeight or 0
        worst = min(font["glyf"][n].xMin for n in font.getGlyphOrder()
                    if font["glyf"][n].numberOfContours > 0)
        print(f"  {dst}")
        print(f"    cell {old} -> {new} ({factor:.0%}), outlines moved {shift}")
        print(f"    cap height / cell = {cap / new:.3f}")
        print(f"    largest overhang  = {worst / upem:+.1%} em")
        assert 0.9 < cap / new < 1.3, "cap/cell ratio is out of the usual range"
        assert worst / upem > -0.12, "a glyph sticks out too far"

    # The fonts are binary, so record the upstream version as readable text.
    (ROOT / "UPSTREAM").write_text(
        f"Atkinson Hyperlegible Mono {version}\n"
        f"{UPSTREAM}\n"
        f"cell factor {factor}\n")
    print(f"OK - built from {version}")


if __name__ == "__main__":
    main()
