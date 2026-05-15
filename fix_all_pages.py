#!/usr/bin/env python3
"""Fix ALL game pages — add global navbar + fix theme toggle + fix subjects.html links."""
import re
import os

GLOBAL_NAV = '''<!-- GLOBAL NAVBAR -->
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
</nav>
'''

def fix_page(fname):
    if not os.path.exists(fname):
        print(f"MISSING: {fname}")
        return

    with open(fname, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Already fixed
    if 'global-nav' in content and 'navbar.css' in content:
        print(f"SKIP {fname} — already fixed")
        return

    changed = False

    # 1. Add navbar.css and grammar-shared.css after theme.css
    if 'navbar.css' not in content:
        content = content.replace(
            '<link rel="stylesheet" href="theme.css">',
            '<link rel="stylesheet" href="theme.css">\n<link rel="stylesheet" href="navbar.css">\n<link rel="stylesheet" href="grammar-shared.css">'
        )
        changed = True

    # 2. Remove old nav patterns
    old_patterns = [
        # <a href="subjects.html" class="back-link">← All Games</a>
        r'<a href="subjects\.html" class="back-link">← All Games</a>\n?',
        # <a href="subjects.html" class="back-link">← Back</a>
        r'<a href="subjects\.html" class="back-link">← Back</a>\n?',
        # <a href="subjects.html" class="home-link">← Back to Subjects</a>
        r'<a href="subjects\.html" class="home-link">← Back to Subjects</a>\n?',
        # <a href="subjects.html">← Back</a> (no class)
        r'<a href="subjects\.html">← Back</a>\n?',
        # inline theme toggle button in header (old style)
        r'<button class="theme-toggle"[^>]*>[^<]*</button>\n?',
        r'<button class="btn btn-wht"[^>]*>← Back</button>\n?',
    ]

    for pat in old_patterns:
        if re.search(pat, content):
            content = re.sub(pat, '', content, flags=re.DOTALL)
            changed = True

    # 3. Replace subjects.html links in game-over screens too
    content = content.replace('href="subjects.html"', 'href="classroom.html"')

    # 4. Inject global nav right after <body...>
    body_match = re.search(r'<body[^>]*>', content)
    if body_match:
        insert_pos = body_match.end()
        if 'global-nav' not in content:
            content = content[:insert_pos] + '\n\n' + GLOBAL_NAV + content[insert_pos:]
            changed = True

    if changed:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {fname}")
    else:
        print(f"No changes: {fname}")

# All game pages that need fixing
PAGES = [
    # Games with old back-link nav
    "flag-match.html", "time-train.html", "word-match.html", "my-name.html",
    "gravity-drop.html", "element-mix.html", "number-ninja.html",
    "animal-sort.html", "force-lab.html", "balance-lab.html",
    "fraction-pizza.html", "geo-challenge.html",
    # Pages with inline theme toggle
    "grammar-hub.html", "grammar-coach.html", "ielts-grammar.html",
    "ielts.html", "ielts-3-day-power-study.html", "ielts-academic-general.html",
    # Standalone pages
    "quick-quiz.html", "math-games.html",
    # Grammar units (all 25)
] + [f"grammar-unit-{i:02d}.html" for i in range(1, 26)]

# Also add grammar units
for fname in PAGES:
    fix_page(fname)

# Grammar units special handling
for i in range(1, 26):
    fname = f"grammar-unit-{i:02d}.html"
    fix_page(fname)

# ielts pages
for fname in ["ielts-band-score.html", "ielts-writing-task2.html",
              "ielts-all-4-subjects-interactive.html", "ielts-drag-sort-quiz.html"]:
    fix_page(fname)

print("\nAll done!")