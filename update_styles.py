#!/usr/bin/env python3
"""Update all EUSTAQUIA HTML pages to use grammar-shared.css theme."""

import os, re

CSS_LINK = '<link rel="stylesheet" href="grammar-shared.css">'

# Files that will use grammar-shared.css
GRAMMAR_FILES = [
    'grammar-hub.html',
    'grammar-unit-01.html',
]

# All HTML files to update font sizes
ALL_FILES = [
    'grammar-hub.html', 'grammar-unit-01.html',
    'ielts-grammar.html', 'ielts.html',
    'word-match.html', 'my-name.html',
    'element-mix.html', 'flag-match.html',
    'balance-lab.html', 'fraction-pizza.html',
    'geo-challenge.html', 'number-ninja.html',
]

def make_body_bigger(html):
    """Ensure body has a bigger base font."""
    # Replace body CSS to increase font
    html = re.sub(
        r'body\{font-family:[^;]+;background:var\(--bg\);color:var\(--white\);min-height:100vh;line-height:1\.\d+\}',
        'body{font-family:\'Inter\',sans-serif;font-size:18px;background:var(--bg);color:var(--white);min-height:100vh;line-height:1.65}',
        html
    )
    return html

def add_css_link(html, path):
    """Add grammar-shared.css link after <head> tag."""
    if 'grammar-shared.css' in html:
        return html  # already added
    html = html.replace('<head>', f'<head>\n{CSS_LINK}')
    return html

def update_grammar_pages():
    base = '/home/jermu/workspace/eusa-sandbox'
    for fname in GRAMMAR_FILES:
        fpath = os.path.join(base, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath) as f:
            html = f.read()
        html = add_css_link(html, fpath)
        with open(fpath, 'w') as f:
            f.write(html)
        print(f'Updated: {fname} → added grammar-shared.css')

def fix_font_sizes():
    """Add font-size override via CSS in all files."""
    font_override = """
/* bigger font override */
body { font-size: 18px !important; line-height: 1.65 !important; }
.quiz-q, .fillin-q, .speak-q, .match-title { font-size: 18px !important; }
.sect-title, .g-sect-title { font-size: 19px !important; }
.quiz-opt, .fillin-opt, .match-word, .tb-stat { font-size: 15px !important; }
"""
    base = '/home/jermu/workspace/eusa-sandbox'
    for fname in ALL_FILES:
        fpath = os.path.join(base, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath) as f:
            html = f.read()
        if 'font-size override marker' not in html:
            # Add before </style>
            if '</style>' in html:
                html = html.replace('</style>', font_override + '\n</style>')
            else:
                html += f'<style>{font_override}</style>'
        with open(fpath, 'w') as f:
            f.write(html)
        print(f'Fixed fonts: {fname}')

if __name__ == '__main__':
    update_grammar_pages()
    fix_font_sizes()
    print('Done!')