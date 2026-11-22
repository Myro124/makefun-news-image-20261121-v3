# makefun-news-image-20261121-v3

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Myro124/makefun-news-image-20261121-v3/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Myro124/makefun-news-image-20261121-v3/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image summing up the world's news of Saturday 21 November 2026 — a third entry with a different composition: a stylised world map with numbered markers, then a numbered story list in large type. Eight mapped stories: Iran strikes Bahrain, a Russian missile hits Kryvyi Rih, the AI sell-off pushes US stocks into correction, COP31 runs into overtime, the world court finds Myanmar guilty of genocide, Mexico captures Chapo Isidro, a dengue breakthrough in Brazil, and the war spilling over in Riyadh and the Baltic.

The poster is drawn by `draw_poster.py` (Pillow, run locally) and shipped as `entry.png` (1024×1024, about 120 KB). Facts were checked against BBC, Reuters, AP, Al Jazeera, The Guardian and WSJ reporting for 21 November 2026; claims that were not independently verified are attributed in the image.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (standard library only, no network) copies `entry.png` to `/output/entry.png`, checks its PNG signature and 1 MiB size limit, and writes the same bytes on every run.

---

Entered on [make.fun](https://make.fun/?ref=gyq1s73s&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards
