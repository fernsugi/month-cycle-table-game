#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════╗
║   MAHJONG-INSPIRED CARD GENERATOR                    ║
║   96 cards · 6 colors · 12 months + 4 winds          ║
╚══════════════════════════════════════════════════════╝
"""

import os
import math
import cairosvg
from PIL import Image

OUTPUT_CARDS = "./"
OUTPUT_SHEETS = "./"
os.makedirs(OUTPUT_CARDS, exist_ok=True)
os.makedirs(OUTPUT_SHEETS, exist_ok=True)

# ── Card canvas (poker size × 3 for crisp output) ──────────────────────────
W, H = 375, 525  # physical render size → 2.5" × 3.5" @ 150 DPI equivalent
R = 22  # corner radius

# ── Color Palette Definitions ───────────────────────────────────────────────
COLORS = {
    "green": {
        "name": "Green",
        "roman": "WOOD",
        "symbol": "竹",
        "number_zh": None,
        "bg1": "#072B07",
        "bg2": "#0E4F0E",
        "bg3": "#165816",
        "border": "#2E7D32",
        "border2": "#81C784",
        "border3": "#C8E6C9",
        "glow": "#4CAF50",
        "pip": "#A5D6A7",
        "text_main": "#FFFFFF",
        "text_dim": "#81C784",
        "accent1": "#00E676",
        "accent2": "#69F0AE",
        "grad_id": "gGreen",
    },
    "red": {
        "name": "Red",
        "roman": "FIRE",
        "symbol": "鳳",
        "number_zh": None,
        "bg1": "#3B0000",
        "bg2": "#7B0000",
        "bg3": "#9B0000",
        "border": "#C62828",
        "border2": "#EF9A9A",
        "border3": "#FFCDD2",
        "glow": "#FF1744",
        "pip": "#FF8A80",
        "text_main": "#FFFFFF",
        "text_dim": "#EF9A9A",
        "accent1": "#FF6E40",
        "accent2": "#FFAB91",
        "grad_id": "gRed",
    },
    "yellow": {
        "name": "Yellow",
        "roman": "EARTH",
        "symbol": "岩",
        "number_zh": None,
        "bg1": "#2D1B00",
        "bg2": "#5C3800",
        "bg3": "#7A4D00",
        "border": "#F9A825",
        "border2": "#FFE57F",
        "border3": "#FFF9C4",
        "glow": "#FFD600",
        "pip": "#FFF176",
        "text_main": "#FFFFFF",
        "text_dim": "#FFE082",
        "accent1": "#FFCA28",
        "accent2": "#FFE57F",
        "grad_id": "gYellow",
    },
    "blue": {
        "name": "Blue",
        "roman": "WATER",
        "symbol": "龍",
        "number_zh": None,
        "bg1": "#000D1F",
        "bg2": "#001A3D",
        "bg3": "#002B5C",
        "border": "#1565C0",
        "border2": "#64B5F6",
        "border3": "#BBDEFB",
        "glow": "#2979FF",
        "pip": "#90CAF9",
        "text_main": "#FFFFFF",
        "text_dim": "#64B5F6",
        "accent1": "#40C4FF",
        "accent2": "#80D8FF",
        "grad_id": "gBlue",
    },
    "black": {
        "name": "Black",
        "roman": "METAL",
        "symbol": "陰",
        "number_zh": None,
        "bg1": "#050505",
        "bg2": "#111111",
        "bg3": "#1A1A1A",
        "border": "#616161",
        "border2": "#BDBDBD",
        "border3": "#E0E0E0",
        "glow": "#9E9E9E",
        "pip": "#EEEEEE",
        "text_main": "#FFFFFF",
        "text_dim": "#BDBDBD",
        "accent1": "#E0E0E0",
        "accent2": "#F5F5F5",
        "grad_id": "gBlack",
    },
    "white": {
        "name": "White",
        "roman": "SILVER",
        "symbol": "陽",
        "number_zh": None,
        "bg1": "#C8C8C8",
        "bg2": "#E8E8E8",
        "bg3": "#F8F8F8",
        "border": "#9E9E9E",
        "border2": "#424242",
        "border3": "#212121",
        "glow": "#757575",
        "pip": "#424242",
        "text_main": "#212121",
        "text_dim": "#616161",
        "accent1": "#424242",
        "accent2": "#757575",
        "grad_id": "gWhite",
    },
}

# ── Wind cards ───────────────────────────────────────────────────────────────
WINDS = {
    "N": {"name": "North", "zh": "北"},
    "S": {"name": "South", "zh": "南"},
    "E": {"name": "East", "zh": "東"},
    "W": {"name": "West", "zh": "西"},
}

CJK_FONT = (
    "'Hiragino Mincho ProN', 'Toppan Bunkyu Mincho', 'Songti SC', "
    "'Songti TC', 'Noto Serif CJK JP', 'Noto Sans CJK JP', "
    "'Arial Unicode MS', serif"
)


# ── Decorative pip patterns per number (1–12 dots arranged elegantly) ────────
def pip_positions(n):
    """Return (cx, cy) list for n pips in a 120×120 box centred at 0,0"""
    p = []
    if n == 1:
        p = [(0, 0)]
    elif n == 2:
        p = [(0, -32), (0, 32)]
    elif n == 3:
        p = [(0, -40), (0, 0), (0, 40)]
    elif n == 4:
        p = [(-28, -28), (28, -28), (-28, 28), (28, 28)]
    elif n == 5:
        p = [(-30, -30), (30, -30), (0, 0), (-30, 30), (30, 30)]
    elif n == 6:
        p = [(-28, -36), (28, -36), (-28, 0), (28, 0), (-28, 36), (28, 36)]
    elif n == 7:
        p = [(-28, -40), (28, -40), (0, -13), (-28, 13), (28, 13), (-28, 40), (28, 40)]
    elif n == 8:
        p = [
            (-28, -40),
            (0, -40),
            (28, -40),
            (-28, 0),
            (28, 0),
            (-28, 40),
            (0, 40),
            (28, 40),
        ]
    elif n == 9:
        p = [
            (-28, -40),
            (0, -40),
            (28, -40),
            (-28, 0),
            (0, 0),
            (28, 0),
            (-28, 40),
            (0, 40),
            (28, 40),
        ]
    elif n == 10:
        p = [
            (-28, -44),
            (0, -44),
            (28, -44),
            (-28, -15),
            (28, -15),
            (0, 0),
            (-28, 15),
            (28, 15),
            (-28, 44),
            (28, 44),
        ]
    elif n == 11:
        p = [
            (-28, -44),
            (0, -44),
            (28, -44),
            (-28, -18),
            (0, -18),
            (28, -18),
            (-28, 18),
            (0, 18),
            (28, 18),
            (-28, 44),
            (28, 44),
        ]
    elif n == 12:
        p = [
            (-28, -44),
            (0, -44),
            (28, -44),
            (-28, -18),
            (0, -18),
            (28, -18),
            (-28, 18),
            (0, 18),
            (28, 18),
            (-28, 44),
            (0, 44),
            (28, 44),
        ]
    return p


def corner_ornament(x, y, rotate, color, size=18):
    """Small decorative corner flower/ornament"""
    c = color["border2"]
    a = color["accent1"]
    petals = ""
    for i in range(8):
        angle = i * 45
        rx, ry = size * 0.35, size * 0.12
        petals += f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{a}" opacity="0.9" transform="rotate({angle+rotate},{x},{y})"/>'
    return (
        f'<g transform="rotate({rotate},{x},{y})">'
        f"  {petals}"
        f'  <circle cx="{x}" cy="{y}" r="{size*0.14}" fill="{c}"/>'
        f"</g>"
    )


def diamond_divider(cx, y, c, w=100):
    """Horizontal ornamental divider with central diamond"""
    return (
        f'<line x1="{cx-w//2}" y1="{y}" x2="{cx-8}" y2="{y}" stroke="{c}" stroke-width="0.8" opacity="0.7"/>'
        f'<polygon points="{cx},{y-5} {cx+5},{y} {cx},{y+5} {cx-5},{y}" fill="{c}" opacity="0.9"/>'
        f'<line x1="{cx+8}" y1="{y}" x2="{cx+w//2}" y2="{y}" stroke="{c}" stroke-width="0.8" opacity="0.7"/>'
    )


def wave_pattern(color, n_waves=5, y_base=0, amplitude=6, width=300):
    """Subtle wave decoration line"""
    c = color["accent1"]
    pts = []
    steps = 80
    for i in range(steps + 1):
        x = i * width / steps
        y = y_base + amplitude * math.sin(i * n_waves * 2 * math.pi / steps)
        pts.append(f"{x:.1f},{y:.1f}")
    return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{c}" stroke-width="0.7" opacity="0.35"/>'


def bamboo_deco(cx, y, c, count=5):
    """Mini bamboo stalks decoration"""
    elems = []
    spacing = 12
    start_x = cx - spacing * (count - 1) / 2
    for i in range(count):
        x = start_x + i * spacing
        h = 22 + (i % 3) * 8
        elems.append(
            f'<rect x="{x-2}" y="{y-h}" width="4" height="{h}" rx="2" fill="{c}" opacity="0.5"/>'
            f'<line x1="{x-2}" y1="{y-h*0.3}" x2="{x+2}" y2="{y-h*0.3}" stroke="{c}" stroke-width="0.5" opacity="0.4"/>'
            f'<line x1="{x-2}" y1="{y-h*0.6}" x2="{x+2}" y2="{y-h*0.6}" stroke="{c}" stroke-width="0.5" opacity="0.4"/>'
        )
    return "".join(elems)


def flame_deco(cx, y, c):
    """Flame decoration"""
    elems = []
    for i in range(5):
        ox = (i - 2) * 14
        h = 20 + abs(i - 2) * 4
        elems.append(
            f'<ellipse cx="{cx+ox}" cy="{y-h//2}" rx="4" ry="{h//2}" fill="{c}" opacity="{0.3+abs(i-2)*0.05}"/>'
        )
    return "".join(elems)


def coin_deco(cx, y, c, count=5):
    """Coin circles decoration"""
    elems = []
    for i in range(count):
        ox = (i - count // 2) * 18
        elems.append(
            f'<circle cx="{cx+ox}" cy="{y}" r="7" fill="none" stroke="{c}" stroke-width="1.2" opacity="0.4"/>'
            f'<circle cx="{cx+ox}" cy="{y}" r="3" fill="{c}" opacity="0.3"/>'
        )
    return "".join(elems)


def wave_deco(cx, y, c):
    """Stylised wave decoration"""
    pts = []
    for i in range(61):
        x = cx - 40 + i * (80 / 60)
        yy = y + 6 * math.sin(i * 3 * math.pi / 60)
        pts.append(f"{x:.1f},{yy:.1f}")
    pts2 = []
    for i in range(61):
        x = cx - 40 + i * (80 / 60)
        yy = y + 6 * math.sin((i * 3 * math.pi / 60) + math.pi)
        pts2.append(f"{x:.1f},{yy:.1f}")
    return (
        f'<polyline points="{" ".join(pts)}" fill="none" stroke="{c}" stroke-width="1.5" opacity="0.5"/>'
        f'<polyline points="{" ".join(pts2)}" fill="none" stroke="{c}" stroke-width="1" opacity="0.3"/>'
    )


def wind_deco(cx, y, c):
    """Wind spiral decoration"""
    paths = ""
    for j, (r, arc) in enumerate([(14, 270), (10, 240), (6, 200)]):
        start_a = j * 30
        x0 = cx + r * math.cos(math.radians(start_a))
        y0 = y + r * math.sin(math.radians(start_a))
        x1 = cx + r * math.cos(math.radians(start_a + arc))
        y1 = y + r * math.sin(math.radians(start_a + arc))
        sweep = 1 if arc < 180 else 1
        large = 1 if arc > 180 else 0
        paths += f'<path d="M{x0:.1f},{y0:.1f} A{r},{r} 0 {large},{sweep} {x1:.1f},{y1:.1f}" fill="none" stroke="{c}" stroke-width="1.4" opacity="{0.5-j*0.1}"/>'
    return paths


def dragon_deco(cx, y, c):
    """Dragon scale/diamond decoration"""
    elems = []
    for row in range(2):
        for col in range(4):
            ox = (col - 1.5) * 20
            oy = row * 12
            elems.append(
                f'<polygon points="{cx+ox},{y+oy-7} {cx+ox+8},{y+oy} {cx+ox},{y+oy+7} {cx+ox-8},{y+oy}" '
                f'fill="none" stroke="{c}" stroke-width="0.8" opacity="0.45"/>'
            )
    return "".join(elems)


COLOR_DECOS = {
    "green": bamboo_deco,
    "red": flame_deco,
    "yellow": coin_deco,
    "blue": wave_deco,
    "black": wind_deco,
    "white": dragon_deco,
}


def make_card_svg(color_key, value, card_type="month"):
    c = COLORS[color_key]
    is_wind = card_type == "wind"
    n = value if not is_wind else None
    face_label = value if is_wind else str(n)
    center_zh = WINDS[value]["zh"] if is_wind else None
    footer_label = WINDS[value]["name"].upper() if is_wind else c["roman"]
    card_id = value if is_wind else f"{n:02d}"

    # ── defs ─────────────────────────────────────────────────────────────────
    grad_id = c["grad_id"]
    rad_id = f"rad_{grad_id}"
    shad_id = f"shad_{grad_id}_{card_id}"
    glow_id = f"glow_{grad_id}_{card_id}"
    clip_id = f"clip_{grad_id}_{card_id}"

    cx, cy = W / 2, H / 2

    # ── pip positions ─────────────────────────────────────────────────────────
    pip_r = 7.5
    pips_svg = ""
    pps = [] if is_wind else pip_positions(n)
    pip_cx, pip_cy = W / 2, H / 2 + 20  # slightly lower than centre
    for px, py in pps:
        pips_svg += (
            f'<circle cx="{pip_cx+px}" cy="{pip_cy+py}" r="{pip_r}" '
            f'fill="{c["pip"]}" opacity="0.85"/>'
            f'<circle cx="{pip_cx+px}" cy="{pip_cy+py}" r="{pip_r*0.45}" '
            f'fill="{c["accent1"]}" opacity="0.6"/>'
        )
    center_symbol_svg = ""
    if is_wind:
        center_symbol_svg = (
            f'<text x="{pip_cx}" y="{pip_cy+4}" text-anchor="middle" dominant-baseline="middle" '
            f'font-family="{CJK_FONT}" font-size="116" font-weight="bold" '
            f'fill="{c["pip"]}" filter="url(#{glow_id})" opacity="0.92">{center_zh}</text>'
            f'<text x="{pip_cx}" y="{pip_cy+4}" text-anchor="middle" dominant-baseline="middle" '
            f'font-family="{CJK_FONT}" font-size="116" font-weight="bold" '
            f'fill="none" stroke="{c["accent1"]}" stroke-width="1.4" opacity="0.55">{center_zh}</text>'
        )

    label_w, label_h = 108, 132
    label_x, label_y = 20, 20
    label_cx = label_x + label_w / 2
    label_main_y = label_y + 62
    label_font = 90 if is_wind else (120 if n < 10 else 90)

    bottom_x = W - label_x - label_w
    bottom_y = H - label_y - label_h
    bottom_cx = bottom_x + label_w / 2
    bottom_main_y = bottom_y + 71

    # ── colour-specific decoration ────────────────────────────────────────────
    deco_fn = COLOR_DECOS.get(color_key)
    top_deco = deco_fn(W / 2, 118, c["accent1"]) if deco_fn else ""
    bottom_deco = deco_fn(W / 2, H - 118, c["accent1"]) if deco_fn else ""

    # ── wavy background lines ─────────────────────────────────────────────────
    wave_lines = ""
    for i in range(7):
        wave_lines += wave_pattern(
            c, n_waves=4, y_base=70 + i * 60, amplitude=5, width=W
        )

    # ── corner ornaments ──────────────────────────────────────────────────────
    corners = (
        corner_ornament(28, 28, 0, c, 14)
        + corner_ornament(W - 28, 28, 90, c, 14)
        + corner_ornament(28, H - 28, 270, c, 14)
        + corner_ornament(W - 28, H - 28, 180, c, 14)
    )

    # ── SVG ───────────────────────────────────────────────────────────────────
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
     width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <!-- Main background gradient -->
    <linearGradient id="{grad_id}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%"   stop-color="{c['bg1']}"/>
      <stop offset="45%"  stop-color="{c['bg2']}"/>
      <stop offset="100%" stop-color="{c['bg3']}"/>
    </linearGradient>

    <!-- Radial highlight -->
    <radialGradient id="{rad_id}" cx="40%" cy="30%" r="65%">
      <stop offset="0%"   stop-color="#FFFFFF" stop-opacity="0.07"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </radialGradient>

    <!-- Drop shadow filter -->
    <filter id="{shad_id}">
      <feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="{c['glow']}" flood-opacity="0.4"/>
    </filter>

    <!-- Glow filter for symbol -->
    <filter id="{glow_id}">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur"/>
      <feBlend in="SourceGraphic" in2="blur" mode="normal"/>
    </filter>

    <!-- Clip to card shape -->
    <clipPath id="{clip_id}">
      <rect x="0" y="0" width="{W}" height="{H}" rx="{R}" ry="{R}"/>
    </clipPath>
  </defs>

  <!-- ── Card base ── -->
  <rect x="0" y="0" width="{W}" height="{H}" rx="{R}" ry="{R}"
        fill="url(#{grad_id})"/>
  <rect x="0" y="0" width="{W}" height="{H}" rx="{R}" ry="{R}"
        fill="url(#{rad_id})"/>

  <g clip-path="url(#{clip_id})">
    <!-- Background wave texture -->
    {wave_lines}
  </g>

  <!-- ── Outer ornamental border ── -->
  <rect x="5" y="5" width="{W-10}" height="{H-10}" rx="{R-2}" ry="{R-2}"
        fill="none" stroke="{c['border']}" stroke-width="1.8" opacity="0.6"/>
  <rect x="8" y="8" width="{W-16}" height="{H-16}" rx="{R-3}" ry="{R-3}"
        fill="none" stroke="{c['border2']}" stroke-width="0.7" opacity="0.5"/>

  <!-- ── Inner frame ── -->
  <rect x="16" y="16" width="{W-32}" height="{H-32}" rx="{R-6}" ry="{R-6}"
        fill="none" stroke="{c['border2']}" stroke-width="1.2"
        stroke-dasharray="4 3" opacity="0.45"/>

  <!-- ── Corner ornaments ── -->
  {corners}

  <!-- ── Top section: number + symbol ── -->
  <!-- Number label box -->
  <rect x="{label_x}" y="{label_y}" width="{label_w}" height="{label_h}" rx="8" ry="8"
        fill="{c['border']}" opacity="0.25"/>
  <rect x="{label_x}" y="{label_y}" width="{label_w}" height="{label_h}" rx="8" ry="8"
        fill="none" stroke="{c['border2']}" stroke-width="0.8" opacity="0.5"/>

  <!-- Arabic number (top-left) -->
  <text x="{label_cx}" y="{label_main_y}" text-anchor="middle" dominant-baseline="middle"
        font-family="Georgia, 'Times New Roman', serif"
        font-size="{label_font}" font-weight="bold"
        fill="{c['text_main']}" filter="url(#{shad_id})">{face_label}</text>

  <!-- Bottom-right mirrored (rotated) -->
  <rect x="{bottom_x}" y="{bottom_y}" width="{label_w}" height="{label_h}" rx="8" ry="8"
        fill="{c['border']}" opacity="0.25"/>
  <rect x="{bottom_x}" y="{bottom_y}" width="{label_w}" height="{label_h}" rx="8" ry="8"
        fill="none" stroke="{c['border2']}" stroke-width="0.8" opacity="0.5"/>

  <text x="{bottom_cx}" y="{bottom_main_y}" text-anchor="middle" dominant-baseline="middle"
        font-family="Georgia, 'Times New Roman', serif"
        font-size="{label_font}" font-weight="bold"
        fill="{c['text_main']}"
        transform="rotate(180,{bottom_cx},{bottom_main_y})">{face_label}</text>

  <!-- ── Top colour decoration ── -->
  {top_deco}

  <!-- ── Central medallion ── -->
  <!-- Outer ring -->
  <circle cx="{cx}" cy="{cy-10}" r="88"
          fill="none" stroke="{c['border']}" stroke-width="1"
          opacity="0.3" stroke-dasharray="2 4"/>
  <circle cx="{cx}" cy="{cy-10}" r="82"
          fill="none" stroke="{c['border2']}" stroke-width="0.6"
          opacity="0.25"/>
  <!-- Inner glow ring -->
  <circle cx="{cx}" cy="{cy-10}" r="76"
          fill="{c['border']}" opacity="0.08"/>

  <!-- ── Pips ── -->
  {pips_svg}
  {center_symbol_svg}

  <!-- ── Divider lines ── -->
  {diamond_divider(cx, 100, c['border2'], 100)}
  {diamond_divider(cx, H-100, c['border2'], 100)}

  <!-- ── Bottom colour decoration ── -->
  {bottom_deco}

  <!-- ── Footer: colour name ── -->
  <text x="{cx}" y="{H-26}" text-anchor="middle" dominant-baseline="middle"
        font-family="'Palatino Linotype', Palatino, 'Book Antiqua', serif"
        font-size="13" font-weight="bold" letter-spacing="4"
        fill="{c['text_dim']}" opacity="0.85">{footer_label}</text>

  <!-- ── Large background ghost symbol ── -->
  <text x="{cx}" y="{cy+5}" text-anchor="middle" dominant-baseline="middle"
        font-family="{CJK_FONT}" font-size="160" font-weight="bold"
        fill="{c['symbol'] and c['glow']}" opacity="0.06">{center_zh if is_wind else c['symbol']}</text>

</svg>"""
    return svg


def generate_all():
    print("╔══════════════════════════════════════════════╗")
    print("║  Mahjong Card Generator  ·  96 cards         ║")
    print("╚══════════════════════════════════════════════╝")
    print()

    card_files = {}
    total = 0
    for color_key in COLORS:
        card_files[color_key] = []
        color_name = COLORS[color_key]["name"]
        print(f"  {color_name:10s} ", end="", flush=True)
        for n in range(1, 13):
            svg_data = make_card_svg(color_key, n)
            png_path = os.path.join(OUTPUT_CARDS, f"{color_key}_{n:02d}.png")
            cairosvg.svg2png(
                bytestring=svg_data.encode(),
                write_to=png_path,
                output_width=W * 2,  # @2x for crisp output
                output_height=H * 2,
            )
            card_files[color_key].append(png_path)
            total += 1
            print("▓", end="", flush=True)
        for wind in WINDS:
            svg_data = make_card_svg(color_key, wind, "wind")
            png_path = os.path.join(OUTPUT_CARDS, f"{color_key}_{wind}.png")
            cairosvg.svg2png(
                bytestring=svg_data.encode(),
                write_to=png_path,
                output_width=W * 2,  # @2x for crisp output
                output_height=H * 2,
            )
            card_files[color_key].append(png_path)
            total += 1
            print("▓", end="", flush=True)
        print(f"  ✓  ({len(card_files[color_key])} cards)")

    print(f"\n  {total} cards generated → {OUTPUT_CARDS}/\n")
    return card_files


def make_preview_sheet(card_files):
    """Compose a 16×6 print-ready PNG sheet with all 96 cards."""
    print("  Building preview sheets …")
    cols, rows = 16, 6
    margin = 20
    gap = 10
    thumb_w, thumb_h = W, H  # @1x for sheet

    sheet_w = cols * thumb_w + (cols - 1) * gap + margin * 2
    sheet_h = rows * thumb_h + (rows - 1) * gap + margin * 2

    sheet = Image.new("RGB", (sheet_w, sheet_h), (30, 28, 26))

    for row_i, color_key in enumerate(COLORS):
        for col_i, png_path in enumerate(card_files[color_key]):
            card_img = Image.open(png_path).convert("RGB")
            card_img = card_img.resize((thumb_w, thumb_h), Image.LANCZOS)
            x = margin + col_i * (thumb_w + gap)
            y = margin + row_i * (thumb_h + gap)
            sheet.paste(card_img, (x, y))

    sheet_path = os.path.join(OUTPUT_SHEETS, "all_96_cards_sheet.png")
    sheet.save(sheet_path, "PNG", optimize=True)
    print(f"  Sheet saved → {sheet_path}")

    # Per-colour sheets (1 row each, nicer for sharing)
    for color_key in COLORS:
        card_count = len(card_files[color_key])
        cw = card_count * thumb_w + (card_count - 1) * gap + margin * 2
        ch = thumb_h + margin * 2
        csheet = Image.new("RGB", (cw, ch), (30, 28, 26))
        for col_i, png_path in enumerate(card_files[color_key]):
            card_img = Image.open(png_path).convert("RGB")
            card_img = card_img.resize((thumb_w, thumb_h), Image.LANCZOS)
            csheet.paste(card_img, (margin + col_i * (thumb_w + gap), margin))
        csheet.save(os.path.join(OUTPUT_SHEETS, f"row_{color_key}.png"), "PNG", optimize=True)
    print(f"  Per-colour rows saved → {OUTPUT_SHEETS}/\n")


if __name__ == "__main__":
    card_files = generate_all()
    make_preview_sheet(card_files)
    print("  Done! 🀄")
    print(f"  Cards  : {OUTPUT_CARDS}/")
    print(f"  Sheets : {OUTPUT_SHEETS}/")
