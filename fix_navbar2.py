#!/usr/bin/env python3
"""Fix 4 pages that are completely missing navbar AND theme toggle."""
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
    "ielts-band-score.html",
    "ielts-writing-task2.html",
    "ielts-all-4-subjects-interactive.html",
    "ielts-drag-sort-quiz.html",
]

for fname in PAGES:
    if not os.path.exists(fname):
        print(f"MISSING: {fname}")
        continue

    with open(fname, 'r') as f:
        content = f.read()

    if "global-nav" in content:
        print(f"SKIP {fname} — already has global-nav")
        continue

    # Add navbar.css + grammar-shared.css if missing
    if 'navbar.css' not in content:
        if '<link rel="stylesheet" href="theme.css">' in content:
            content = content.replace(
                '<link rel="stylesheet" href="theme.css">',
                '<link rel="stylesheet" href="theme.css">\n<link rel="stylesheet" href="navbar.css">\n<link rel="stylesheet" href="grammar-shared.css">'
            )
        elif '<head>' in content:
            content = content.replace(
                '<head>',
                '<head>\n<link rel="stylesheet" href="navbar.css">\n<link rel="stylesheet" href="grammar-shared.css">'
            )

    # Add theme-manager.js if missing
    if 'theme-manager.js' not in content:
        content = content.replace('<head>', '<head>\n<script src="theme-manager.js"></script>')

    # Inject navbar right after <body> or after decorative divs
    # Find body tag and inject after it
    body_match = re.search(r'<body[^>]*>', content)
    if body_match:
        insert_pos = body_match.end()
        content = content[:insert_pos] + '\n\n' + NEW_NAV + content[insert_pos:]
    else:
        print(f"ERROR: No <body> in {fname}")

    with open(fname, 'w') as f:
        f.write(content)
    print(f"Fixed: {fname}")

print("Done!")