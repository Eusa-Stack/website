#!/usr/bin/env python3
"""Fix navbar and theme toggle on all game pages."""
import re
import os

NEW_NAV = '''<!-- GLOBAL NAVBAR -->
<nav class="global-nav">
  <a href="index.html" class="nav-brand">
    <span class="nav-brand-e">Edu</span><span class="nav-brand-d">Suite</span><span class="nav-brand-dot">.</span>
  </a>
  <div class="nav-links">
    <a href="index.html" class="nav-link">🏠 Home</a>
    <a href="classroom.html" class="nav-link">🎓 Classroom</a>
  </div>
  <div class="nav-right">
    <button class="nav-theme-btn theme-toggle" onclick="EusaTheme.toggle()">☾ / ☀</button>
  </div>
</nav>'''

PAGES = [
    "flag-match.html", "time-train.html", "word-match.html", "my-name.html",
    "gravity-drop.html", "element-mix.html", "number-ninja.html", "quick-quiz.html",
    "animal-sort.html", "force-lab.html", "balance-lab.html", "fraction-pizza.html",
    "geo-challenge.html", "grammar-hub.html", "grammar-coach.html",
    "ielts-grammar.html", "ielts.html", "ielts-3-day-power-study.html",
    "ielts-academic-general.html",
]

for fname in PAGES:
    if not os.path.exists(fname):
        print(f"MISSING: {fname}")
        continue
    if "global-nav" in open(fname).read():
        print(f"SKIP {fname} — already has global-nav")
        continue

    with open(fname, 'r') as f:
        content = f.read()

    # Add navbar.css if missing
    if 'navbar.css' not in content:
        content = content.replace(
            '<link rel="stylesheet" href="theme.css">',
            '<link rel="stylesheet" href="theme.css">\n<link rel="stylesheet" href="navbar.css">'
        )

    # Remove old nav blocks
    old_navs = [
        r'<nav>.*?← All Games.*?</nav>',
        r'<nav>.*?← Back.*?</nav>',
        r'<nav>.*?← Back to.*?</nav>',
        r'<nav>.*?nav-yt.*?</nav>',
        r'<div class="nav">.*?</div>',
    ]
    for pat in old_navs:
        content = re.sub(pat, NEW_NAV, content, flags=re.DOTALL)

    with open(fname, 'w') as f:
        f.write(content)
    print(f"Fixed: {fname}")

print("Done!")