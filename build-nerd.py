#!/usr/bin/env python3
"""Build the Nerd Font variants of Snug Mono.

The Nerd Fonts patcher cannot read a variable font. It uses the default
instance, which for this font is ExtraLight. This script first makes static
instances at the usual four styles, then patches each one.

The script needs FontForge with the Python module, and it needs network access
for the patcher. Run build.py first.

Usage:  python3 build-nerd.py
"""
import hashlib
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

PATCHER_VERSION = "v3.5.1"
PATCHER_URL = (f"https://github.com/ryanoasis/nerd-fonts/releases/download/"
               f"{PATCHER_VERSION}/FontPatcher.zip")
PATCHER_SHA256 = "42bcb32145499a35732274c7fc48deb434ad0d2e0e118f98527c1479c6fa251a"

# Two variants. The standard one keeps the natural width of each icon, which
# makes the icons larger. The Mono one squeezes every icon into one cell.
VARIANTS = {"standard": [], "mono": ["--mono"]}

# style name -> (source file, weight)
STYLES = {
    "Regular": ("SnugMono[wght].ttf", 400),
    "Bold": ("SnugMono[wght].ttf", 700),
    "Italic": ("SnugMono-Italic[wght].ttf", 400),
    "BoldItalic": ("SnugMono-Italic[wght].ttf", 700),
}

ROOT = Path(__file__).parent
FONTS = ROOT / "fonts"
OUT = FONTS / "nerd"
WORK = ROOT / "build"


def get_patcher():
    """Download the patcher and make sure that the file is the expected one."""
    WORK.mkdir(exist_ok=True)
    archive = WORK / "FontPatcher.zip"
    if not archive.exists():
        print(f"  download FontPatcher {PATCHER_VERSION}")
        urllib.request.urlretrieve(PATCHER_URL, archive)

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    if digest != PATCHER_SHA256:
        sys.exit(f"FontPatcher.zip has checksum {digest}, expected {PATCHER_SHA256}")

    target = WORK / "patcher"
    if not (target / "font-patcher").exists():
        with zipfile.ZipFile(archive) as z:
            z.extractall(target)
    return target


def make_static(style, source, weight):
    """Write a static instance of the variable font at one weight."""
    font = TTFont(FONTS / source, recalcTimestamp=False)
    instantiateVariableFont(font, {"wght": weight}, inplace=True, updateFontNames=True)
    path = WORK / f"SnugMono-{style}.ttf"
    font.save(path)
    return path


def main():
    if not shutil.which("fontforge"):
        sys.exit("fontforge is not installed. See the README for how to install it.")

    patcher = get_patcher()
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    for style, (source, weight) in STYLES.items():
        static = make_static(style, source, weight)
        for variant, flags in VARIANTS.items():
            print(f"  patch {static.name} ({variant})")
            subprocess.run(
                ["fontforge", "-script", str(patcher / "font-patcher"), str(static),
                 "--complete",      # every glyph set
                 "--careful",       # never replace a glyph the font already has
                 "--quiet",
                 *flags,
                 "--outputdir", str(OUT)],
                cwd=patcher, check=True,
                stdout=subprocess.DEVNULL, stderr=None)

    # FontForge stamps its own build date. Copy the source date over it so
    # that two builds of the same source give identical bytes.
    reference = TTFont(FONTS / "SnugMono[wght].ttf", recalcTimestamp=False)["head"]
    for path in OUT.glob("*.ttf"):
        font = TTFont(path, recalcTimestamp=False)
        font["head"].modified = reference.modified
        font["head"].created = reference.created
        font.save(path)

    built = sorted(OUT.glob("*.ttf"))
    expected = len(STYLES) * len(VARIANTS)
    if len(built) != expected:
        sys.exit(f"Expected {expected} fonts, got {len(built)}")

    for path in built:
        font = TTFont(path)
        family = font["name"].getDebugName(16) or font["name"].getDebugName(1)
        # The standard variant gives icons a wider advance, so measure a letter.
        cell = font["hmtx"][font.getBestCmap()[ord("M")]][0]
        count = len(font.getGlyphOrder())
        print(f"  {path.name}  family={family!r} cell={cell} glyphs={count}")
        assert "Nerd Font" in family, "the patcher did not rename the family"
        assert cell == 575, f"the cell of the letters changed to {cell}"
        assert count > 3000, "the icon glyphs are missing"
    print("OK")


if __name__ == "__main__":
    main()
