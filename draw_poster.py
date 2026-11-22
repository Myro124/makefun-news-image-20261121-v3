"""Draw the 21 November 2026 world-news poster, version 3 (1024x1024 PNG).

Third entry for the make.fun news-image-20261121 bounty. A genuinely
different composition from v1/v2's newspaper grids: a stylised world
map with numbered markers, then a numbered story list in large type.
v2 tied v1 at 0.976591, so this version changes the composition
itself rather than the story count. The weakest item (the Riemann
claim, unverified) moves to the ALSO strip; the eight mapped stories
are the day's verified headline events.

Run locally with Pillow:  python3 draw_poster.py
Writes entry.png next to this file. The grader cannot install Pillow,
so the submitted entrypoint (main.py) ships the rendered PNG and
copies it to /output/entry.png deterministically.
All facts were checked against BBC / Reuters / AP / Al Jazeera /
The Guardian / WSJ reporting for Saturday 21 November 2026.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

NAVY = (15, 30, 58)
NAVY2 = (22, 44, 82)
SEA = (16, 52, 78)
LAND = (46, 130, 115)
GRID = (30, 80, 110)
GOLD = (232, 180, 60)
RED = (198, 48, 38)
CREAM = (248, 244, 232)
INK = (24, 28, 36)
GREY = (88, 96, 110)
WHITE = (255, 255, 255)


def font(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# ---- masthead ----
d.rectangle([0, 0, W, 148], fill=NAVY)
d.rectangle([0, 148, W, 154], fill=GOLD)
d.text((32, 20), "THE WORLD IN ONE DAY", font=font(SERIF_B, 60), fill=WHITE)
d.text((32, 96), "SATURDAY  •  21 NOVEMBER 2026", font=font(SANS_B, 32), fill=GOLD)
d.text((712, 96), "8 STORIES", font=font(SANS_B, 28), fill=(180, 200, 230))

# ---- map band ----
MAP_TOP, MAP_BOT = 154, 500
d.rectangle([0, MAP_TOP, W, MAP_BOT], fill=SEA)
# graticule
for gx in range(128, W, 128):
    d.line([gx, MAP_TOP, gx, MAP_BOT], fill=GRID, width=2)
for gy in range(MAP_TOP + 86, MAP_BOT, 86):
    d.line([0, gy, W, gy], fill=GRID, width=2)
# simplified continents (stylised flat map)
continents = [
    [(60, 262), (90, 212), (150, 176), (230, 160), (320, 165), (360, 190),
     (345, 230), (310, 250), (300, 282), (285, 320), (255, 355), (230, 340),
     (210, 300), (170, 290), (120, 300), (75, 295)],
    [(415, 175), (465, 170), (475, 195), (425, 200)],
    [(330, 385), (380, 368), (420, 390), (425, 430), (400, 480), (370, 498),
     (345, 470), (320, 430)],
    [(490, 205), (555, 188), (615, 192), (635, 222), (595, 245), (540, 248),
     (498, 228)],
    [(495, 270), (540, 255), (600, 255), (650, 275), (665, 320), (640, 380),
     (610, 425), (575, 435), (545, 400), (520, 350), (495, 310)],
    [(638, 195), (700, 175), (800, 170), (900, 175), (980, 205), (975, 250),
     (930, 280), (880, 275), (860, 310), (830, 340), (800, 320), (760, 290),
     (720, 280), (690, 250), (660, 230), (640, 215)],
    # Arabian peninsula, so the Gulf marker sits on land
    [(628, 240), (662, 255), (678, 290), (658, 320), (634, 300), (624, 265)],
    # India and South-East Asia tapers
    [(795, 295), (820, 350), (845, 335), (835, 290)],
    [(860, 300), (885, 345), (905, 330), (890, 295)],
    [(808, 408), (895, 403), (932, 428), (895, 455), (820, 450)],
]
for poly in continents:
    d.polygon(poly, fill=LAND)
for box in [(838, 318, 868, 338), (878, 338, 908, 358), (800, 348, 824, 366)]:
    d.ellipse(box, fill=LAND)
d.text((32, 468), "THE DAY, MAPPED — NUMBERS MATCH THE STORIES BELOW",
       font=font(SANS_B, 15), fill=(170, 200, 220))

# numbered markers: (number, x, y, lead?)
markers = [
    (1, 650, 275, True),
    (2, 585, 215, False),
    (3, 300, 245, False),
    (4, 620, 245, False),
    (5, 520, 212, False),
    (6, 203, 285, False),
    (7, 364, 380, False),
    (8, 575, 188, False),
]
for num, mx, my, lead in markers:
    r = 20 if lead else 17
    fill = GOLD if lead else RED
    num_fill = NAVY if lead else WHITE
    d.ellipse([mx - r, my - r, mx + r, my + r], fill=fill,
              outline=WHITE, width=3)
    label = str(num)
    tw = d.textlength(label, font=font(SANS_B, 19))
    d.text((mx - tw / 2, my - 13), label, font=font(SANS_B, 19), fill=num_fill)

# ---- numbered story list ----
stories = [
    ("IRAN STRIKES BAHRAIN",
     "Tehran says it hit two US bases; Bahrain reports a civilian site ablaze, no injuries."),
    ("MISSILE HITS KRYVYI RIH",
     "A Russian missile kills 2, dozens hurt, in Zelenskyy's hometown."),
    ("AI SELL-OFF ROCKS WALL ST",
     "S&P -3.7%, Dow -950 pts, Nasdaq -5.3%; Nvidia -14%, Anthropic -9%."),
    ("COP31 TALKS IN OVERTIME",
     "UN climate talks run past the Friday deadline with no deal."),
    ("MYANMAR GUILTY OF GENOCIDE",
     "The world court finds Myanmar responsible for the Rohingya genocide."),
    ("CHAPO ISIDRO CAPTURED",
     "FBI most-wanted cartel boss seized in Sinaloa; 11+ dead in the violence."),
    ("DENGUE BREAKTHROUGH",
     "Bacteria-carrying mosquitoes cut dengue cases among children in Brazil."),
    ("WAR SPILLS OVER",
     "Saudi stops Houthi missiles over Riyadh; drones hit a Russian ship off Finland."),
]
ROW_Y, ROW_H = 512, 56
for i, (title, body) in enumerate(stories):
    y = ROW_Y + i * ROW_H
    lead = i == 0
    r = 20
    cx, cy = 52, y + ROW_H // 2
    d.ellipse([cx - r, cy - r, cx + r, cy + r],
              fill=GOLD if lead else RED, outline=(210, 205, 190), width=2)
    label = str(i + 1)
    tw = d.textlength(label, font=font(SANS_B, 19))
    d.text((cx - tw / 2, cy - 13), label, font=font(SANS_B, 19),
           fill=NAVY if lead else WHITE)
    d.text((88, y + 4), title, font=font(SANS_B, 27), fill=INK)
    d.text((88, y + 31), body, font=font(SANS, 20), fill=(50, 56, 68))
    if i < len(stories) - 1:
        d.line([88, y + ROW_H - 2, 992, y + ROW_H - 2],
               fill=(215, 210, 195), width=2)

# ---- also strip + footer ----
AY = ROW_Y + 8 * ROW_H + 8
d.rounded_rectangle([24, AY, 1000, AY + 34], radius=10, fill=NAVY2)
d.text((40, AY + 8), "ALSO:  Riemann proof claimed with AI help  •  "
       "Iran says it downed a US drone near Qeshm",
       font=font(SANS_B, 16), fill=WHITE)
d.text((32, AY + 42), "Sources: BBC, Reuters, AP, Al Jazeera, The Guardian, WSJ  •  "
       "Claims are attributed where they were not independently verified.",
       font=font(SANS, 14), fill=GREY)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
