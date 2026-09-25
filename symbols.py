"""Add the symbols that terminal programs draw and the source font does not have.

A terminal takes a missing glyph from a fallback font, at the size of that
font. Next to Snug Mono, whose cap height is short, those glyphs look too
large. These are drawn to the metrics of Snug Mono instead.

The source font varies its weight with one master, at the heaviest weight.
Each symbol with a stroke is drawn twice, at the stroke of the lightest and
of the heaviest weight, and the difference becomes that master. The symbols
then follow the letters at every weight, through the same avar curve.
"""
import math

from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib.tables._g_l_y_f import Glyph, GlyphComponent
from fontTools.ttLib.tables.TupleVariation import TupleVariation

CELL = 575
CX = CELL / 2
AXIS = 250           # the middle of the minus sign
CAP = 668
DOT_Y = 254          # the middle of the bullet, so • and ◦ are a pair
STROKE = (54, 158)   # the stem of | at wght 200 and at wght 800

R_BIG = 220          # ● ○ ◐, about the width of ×
R_SMALL = 166        # ◦, the size of •


def arc(pen, cx, cy, r, start, steps, d):
    """steps quadratic segments of 45 degrees each, from angle start, in
    direction d: -1 is clockwise. The points are the same for every r."""
    off = r / math.cos(math.pi / 8)  # where the tangents of two points meet

    def at(rad, deg):
        return rnd((cx + rad * math.cos(math.radians(deg)),
                    cy + rad * math.sin(math.radians(deg))))

    pen.moveTo(at(r, start))
    for k in range(steps):
        a = start + d * 45 * k
        pen.qCurveTo(at(off, a + d * 22.5), at(r, a + d * 45))
    pen.closePath()


def circle(pen, cx, cy, r, clockwise=True):
    arc(pen, cx, cy, r, 90, 8, -1 if clockwise else 1)


def left_half(pen, cx, cy, r):
    """The left half of a disc, clockwise: from the bottom round to the top.
    closePath draws the straight side."""
    arc(pen, cx, cy, r, 270, 4, -1)


def polygon(pen, pts):
    """A closed polygon. TrueType fills a clockwise contour. A shape that turns
    over at one stroke has the other order, and then the points of the two
    masters do not match, so that is an error and not a reversal."""
    area = sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]))
    assert area < 0, f"the polygon {pts} is not clockwise"
    pen.moveTo(rnd(pts[0]))
    for p in pts[1:]:
        pen.lineTo(rnd(p))
    pen.closePath()


def rnd(p):
    return (round(p[0]), round(p[1]))


def ring(pen, cy, r, s):
    """A circle outline. The stroke is a part of the stem, and less for a
    small ring: at the stem of a bold letter, ◦ has no hole left."""
    s *= 0.75 if r == R_BIG else 0.5
    circle(pen, CX, cy, r)
    circle(pen, CX, cy, r - s, clockwise=False)


def arrow(pen, s, up):
    """A shaft from the baseline to the cap height, with a solid head."""
    head_w, head_h = 400, 260
    tip, base = (CAP, CAP - head_h) if up else (0, head_h)
    end = 0 if up else CAP
    pts = [(CX, tip), (CX + head_w / 2, base), (CX + s / 2, base), (CX + s / 2, end),
           (CX - s / 2, end), (CX - s / 2, base), (CX - head_w / 2, base)]
    polygon(pen, pts if up else pts[::-1])  # a mirror turns the order


def chevron(pen, s):
    """❯, heavier than >, at the height of the lowercase."""
    t = s * 0.9 + 40  # the width of an arm, measured along a row
    left, tip, h = 110, 470, 248
    # Each arm is two parallel edges, t apart, so the left edge and the tip
    # stay where they are at every weight.
    polygon(pen, [(left, AXIS + h), (left + t, AXIS + h), (tip, AXIS),
                  (left + t, AXIS - h), (left, AXIS - h), (tip - t, AXIS)])


def triangle(pen, up):
    w, h = 500, 434  # equilateral, and as wide as ● is tall
    if up:
        polygon(pen, [(CX, AXIS + h / 2), (CX + w / 2, AXIS - h / 2), (CX - w / 2, AXIS - h / 2)])
    else:
        polygon(pen, [(CX, AXIS - h / 2), (CX - w / 2, AXIS + h / 2), (CX + w / 2, AXIS + h / 2)])


# codepoint -> (glyph name, draw(pen, stroke)). A symbol that ignores the
# stroke has no variation.
SYMBOLS = {
    0x25CF: ("uni25CF", lambda p, s: circle(p, CX, DOT_Y, R_BIG)),               # ●
    0x25CB: ("uni25CB", lambda p, s: ring(p, DOT_Y, R_BIG, s)),                  # ○
    0x25D0: ("uni25D0", lambda p, s: (ring(p, DOT_Y, R_BIG, s),                  # ◐
                                      left_half(p, CX, DOT_Y, R_BIG - s * 0.75 / 2))),
    0x25E6: ("uni25E6", lambda p, s: ring(p, DOT_Y, R_SMALL, s)),                # ◦
    0x25B2: ("uni25B2", lambda p, s: triangle(p, up=True)),                      # ▲
    0x25BC: ("uni25BC", lambda p, s: triangle(p, up=False)),                     # ▼
    0x2191: ("arrowup", lambda p, s: arrow(p, s, up=True)),                      # ↑
    0x2193: ("arrowdown", lambda p, s: arrow(p, s, up=False)),                   # ↓
    0x276F: ("uni276F", lambda p, s: chevron(p, s)),                             # ❯
}
# ✕ is the multiplication sign of the font, which already follows the weight.
COMPOSITES = {0x2715: ("uni2715", "multiply")}


def draw(fn, stroke, glyf):
    pen = TTGlyphPen(glyf)
    fn(pen, stroke)
    return pen.glyph()


def add_symbols(font):
    """Add each symbol that the font does not have. Return the ones added."""
    glyf, hmtx, gvar = font["glyf"], font["hmtx"], font["gvar"]
    cmap = font.getBestCmap()
    order = font.getGlyphOrder()
    peak = {"wght": (0.0, 1.0, 1.0)}
    hvar = font["HVAR"].table.AdvWidthMap.mapping if "HVAR" in font else None
    added = []

    def place(cp, name, glyph):
        order.append(name)
        glyf[name] = glyph
        glyph.recalcBounds(glyf)
        hmtx[name] = (CELL, glyph.xMin)
        if hvar is not None:
            hvar[name] = hvar[cmap[ord(" ")]]  # every advance is the same
        for table in font["cmap"].tables:
            if table.isUnicode():
                table.cmap[cp] = name
        added.append(chr(cp))

    for cp, (name, fn) in SYMBOLS.items():
        if cp in cmap:
            continue
        light, heavy = draw(fn, STROKE[0], glyf), draw(fn, STROKE[1], glyf)
        assert len(light.coordinates) == len(heavy.coordinates), f"{name}: the masters differ"
        light.flags[0] |= 0x40  # OVERLAP_SIMPLE: the contours of ◐ cross
        place(cp, name, light)
        deltas = [(bx - ax, by - ay) for (ax, ay), (bx, by)
                  in zip(light.coordinates, heavy.coordinates)]
        if any(d != (0, 0) for d in deltas):
            gvar.variations[name] = [TupleVariation(peak, deltas + [(0, 0)] * 4)]

    for cp, (name, base) in COMPOSITES.items():
        if cp in cmap:
            continue
        glyph = Glyph()
        comp = GlyphComponent()
        comp.glyphName, comp.x, comp.y, comp.flags = base, 0, 0, 0x4  # ROUND_XY_TO_GRID
        glyph.numberOfContours, glyph.components = -1, [comp]
        place(cp, name, glyph)  # the component varies, and so this does

    font.setGlyphOrder(order)
    return added
