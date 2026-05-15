#!/usr/bin/env python3
"""Update all EUSTAQUIA HTML pages — add shared CSS, bigger fonts, floating animation."""

import os, re

BASE = '/home/jermu/workspace/eusa-sandbox'
SHARED_CSS = '<link rel="stylesheet" href="grammar-shared.css">'
FLOAT_ANIM = '<script src="floating-anim.js"></script>'

# All pages to update
ALL_HTML = [
    'grammar-hub.html', 'grammar-unit-01.html',
    'ielts-grammar.html', 'ielts.html',
    'word-match.html', 'my-name.html',
    'element-mix.html', 'flag-match.html',
    'balance-lab.html', 'fraction-pizza.html',
    'geo-challenge.html', 'number-ninja.html',
    'subjects.html', 'index.html',
    'animal-sort.html', 'force-lab.html', 'gravity-drop.html',
    'time-train.html', 'quick-quiz.html',
    'demo-landing.html', 'demo-v2.html', 'demo-v3.html', 'demo-v4.html',
]

# Grammar pages that get the full dark theme treatment
GRAMMAR_PAGES = {
    'grammar-hub.html', 'grammar-unit-01.html',
    'ielts-grammar.html', 'ielts.html',
    'word-match.html',
}

# Font size override block
FONT_OVERRIDE = """
/* EUSTAQUIA — bigger fonts for readability */
body { font-size: 18px !important; line-height: 1.65 !important; }
h1 { font-size: 36px !important; }
h2 { font-size: 28px !important; }
h3 { font-size: 21px !important; }
.quiz-q, .fillin-q, .speak-q, .match-title { font-size: 18px !important; }
.sect-title { font-size: 19px !important; }
.quiz-opt, .fillin-opt, .match-word, .tb-stat { font-size: 15px !important; }
"""


def update_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html

    # 1. Add shared CSS after <head>
    if 'grammar-shared.css' not in html:
        html = html.replace('<head>', f'<head>\n{SHARED_CSS}')

    # 2. Add floating animation script before </body>
    if 'floating-anim.js' not in html:
        html = html.replace('</body>', f'{FLOAT_ANIM}\n</body>')

    # 3. Add font override before </style> (only if not already present)
    if 'EUSTAQUIA.*bigger fonts' not in html and '</style>' in html:
        html = html.replace('</style>', f'\n{FONT_OVERRIDE}</style>')

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        fname = os.path.basename(filepath)
        print(f'  Updated: {fname}')


def main():
    print('Updating all HTML pages with shared CSS + floating animation...')
    for fname in ALL_HTML:
        fpath = os.path.join(BASE, fname)
        if os.path.exists(fpath):
            update_page(fpath)
        else:
            print(f'  Skipped (not found): {fname}')
    print('Done!')


if __name__ == '__main__':
    main()