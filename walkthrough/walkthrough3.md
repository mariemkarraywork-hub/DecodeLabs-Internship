# AI Recommendation Logic — Walkthrough

Match user interests to catalog items using tag overlap math. Simple logic, no random picks.

---

## Files

| File | Role |
|------|------|
| `recommend.py` | Python — tags in, top 5 out |
| `index.html` | Browser UI |
| `app.js` | Catalog + scoring + display |
| `styles.css` | Light/dark theme |

---

## The logic (3 steps)

**1. INPUT** — User picks tags. Every tag is cleaned: lowercase + trim.

**2. PROCESS** — Score each item with **Jaccard** (how many tags overlap).

```
score = shared tags / all unique tags
```

Browser also scores sliders with distance math, then blends both scores.

**3. OUTPUT** — Sort highest first. Show **top 5** with % scores.

---

## Commands

```powershell
cd "C:\Users\karra\.gemini\antigravity\scratch\IA\AI Recommendation Logic"
python recommend.py
python recommend.py --demo
Start-Process .\index.html
```

---

## `recommend.py` step by step

1. `CATALOG` — list of movies with tags
2. `clean_tag()` — lowercase and trim
3. `jaccard()` — count shared tags ÷ total unique tags
4. `get_recommendations()` — score all items, sort, keep top 5
5. `print_results()` — show title, score %, tags

Interactive: type tags like `sci-fi, mystery`

Demo: `python recommend.py --demo` runs test profile and prints PASS or FAIL

---

## Browser app step by step

1. Pick a domain tab (Movies, Books, Games, Travel)
2. Click interest tags
3. Move attribute sliders (optional)
4. See top 5 cards sorted by match %
5. Click **Show Match Breakdown** for tag + score details

Same Jaccard idea as Python. Sliders add a second score for numeric attributes.

---

## Jaccard example

You pick: `Sci-Fi`, `Drama`

Item has: `Sci-Fi`, `Drama`, `Thriller`

- Shared: 2 tags
- Total unique: 3 tags
- Score: 2 ÷ 3 = **67%**

---

## Verification test

```powershell
python recommend.py --demo
```

Profile: `sci-fi, thriller, action`

| Rank | Title | Score |
|------|-------|-------|
| 1 | Inception | 100% |
| 2 | The Dark Knight | 50% |
| 3 | Whiplash | 25% |

Should print **PASS**.

Browser check: Movies tab → select Sci-Fi, Thriller, Action → Inception is #1.

---

## P3 checklist

| Requirement | Where |
|-------------|-------|
| Mock catalog | `recommend.py` + `app.js` |
| User input | terminal + browser tags |
| Sanitize tags | `clean_tag` / `normalizeTag` |
| Jaccard similarity | `jaccard()` / `jaccardScore()` |
| Sort by score | both |
| Top 5 output | both |
| Show scores | print + match badge |
| Test scenario | `--demo` |

---

## Folder layout

```
AI Recommendation Logic/
├── recommend.py
├── index.html
├── app.js
├── styles.css
└── ../walkthrough/walkthrough3.md
```

---

## Level up later

1. Add more items to `CATALOG`
2. Port books/games to `recommend.py`
3. Save profiles to a JSON file
4. Connect browser to Python with Flask

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| No tags entered | Type comma-separated tags |
| Wrong order | Tags are case-insensitive |
| Only 5 cards | Top 5 by design |
| `--demo` fails | Run from project folder |

---

## Viva (one sentence)

> Tags go in, Jaccard scores each item, top 5 come out with visible percentages — the browser adds sliders and a visual UI.
