#!/usr/bin/env python3
"""
Add theme switcher to all HTML pages.

For each .html file:
  1. Add theme-manager.js <script> in <head> (first, before other scripts)
  2. Add theme.css <link> in <head>
  3. Remove the inline :root CSS variable blocks (--bg, --orange, etc.)
  4. Add a theme-toggle button in the header area (after EUSTAQUIA logo)

Usage: python3 add_theme_switcher.py [--dry-run]
"""

import os
import re
import sys

BASE = '/home/jermu/workspace/eusa-sandbox'
DRY_RUN = '--dry-run' in sys.argv

# Files to skip (not part of the site or use special handling)
SKIP_FILES = {'theme-manager.js', 'theme.css', 'update_styles.py', 
              'gen_units.py', 'gen_units_12_25.py', 'May_2026_Update_Plan.md',
              'wiki-get.py'}

# Scripts already in <head> that must come AFTER theme-manager.js
# We'll add theme-manager.js as the VERY FIRST script in <head>
HEAD_TEMPLATE = '''<script src="theme-manager.js"></script>
<link rel="stylesheet" href="theme.css">
'''

# Theme toggle button HTML
THEME_TOGGLE_HTML = '<button class="theme-toggle" onclick="EusaTheme.toggle()" title="Toggle light/dark theme" style="font-size:1rem;padding:4px 12px;">&#9790; / &#9728;</button>'


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # ── 1. Find <head> and insert our script+link ──────────────────────────
    # We want theme-manager.js to be the FIRST script in <head>
    head_end = content.find('</head>')
    if head_end == -1:
        print(f"  SKIP: no </head> in {os.path.basename(filepath)}")
        return

    # Check if already added
    if 'theme-manager.js' in content:
        print(f"  Already has theme-manager: {os.path.basename(filepath)}")
        return

    # Find the first <script> or <link> or <title> in <head>
    head_start = content.rfind('<head', 0, head_end)
    head_fragment = content[head_start:head_end]

    # Insert after <head> tag, before any other content
    head_tag_end = content.find('>', head_start) + 1
    insert_pos = head_tag_end

    content = content[:insert_pos] + '\n' + HEAD_TEMPLATE.strip() + '\n' + content[insert_pos:]

    # Fix head_end position (shifted by insertion length)
    head_end += len('\n' + HEAD_TEMPLATE.strip() + '\n')

    # ── 2. Find and remove inline CSS :root variable blocks ─────────────────
    # Pattern: :root { --var: value; ... } within a <style> block
    # These are the inline theme variables we want to remove from each file

    # Find <style> blocks
    style_blocks = list(re.finditer(r'<style[^>]*>(.*?)</style>', content, re.DOTALL))

    for m in reversed(style_blocks):  # iterate in reverse to preserve positions
        style_content = m.group(1)
        # Check if this style block contains :root CSS variable declarations
        if re.search(r':root\s*\{', style_content) and re.search(r'--[\w-]+\s*:', style_content):
            # Extract just the :root { ... } block
            root_match = re.search(r'(:root\s*\{[^}]+\})', style_content, re.DOTALL)
            if root_match:
                root_block = root_match.group(1)
                # Remove it from the style content
                new_style_content = style_content.replace(root_block, '')
                new_style = m.group(0).replace(style_content, new_style_content)
                content = content[:m.start()] + new_style + content[m.end():]
                print(f"  Removed :root vars from <style>: {os.path.basename(filepath)}")

    # ── 3. Add theme toggle button after EUSTAQUIA logo ────────────────────
    # Pattern: find "EUSTAQUIA" text followed by a nav/header element
    # We look for the EUSTAQUIA heading and insert toggle after it
    
    # Find the EUSTAQUIA text or logo area
    eusa_patterns = [
        r'(EUSTAQUIA</span>\s*</div>)',           # subjects.html pattern
        r'(>EUSTAQUIA\s*</span>\s*</div>)',        # grammar pages pattern  
        r'(<span[^>]*id=["\']logo[^"\']*["\'][^>]*>.*?EUSTAQUIA.*?</span>)',
        r'(EUSTAQUIA</div>)',
    ]
    
    toggle_inserted = False
    for pattern in eusa_patterns:
        match = re.search(pattern, content)
        if match:
            end_pos = match.end()
            # Insert toggle after this element
            content = content[:end_pos] + '\n' + THEME_TOGGLE_HTML + '\n' + content[end_pos:]
            toggle_inserted = True
            print(f"  Added toggle after EUSTAQUIA: {os.path.basename(filepath)}")
            break
    
    if not toggle_inserted:
        # Fallback: look for <header or .hero or .brand
        for fallback_pattern in [
            r'(<header[^>]*>)',          # <header> tag
            r'(<div[^>]*class=["\'][^"\']*hero[^"\']*["\'][^>]*>)',  # .hero div
            r'(<div[^>]*class=["\'][^"\']*brand[^"\']*["\'][^>]*>)', # .brand div
            r'(<nav[^>]*>)',             # <nav> tag
        ]:
            match = re.search(fallback_pattern, content)
            if match:
                end_pos = match.end()
                content = content[:end_pos] + '\n' + THEME_TOGGLE_HTML + '\n' + content[end_pos:]
                toggle_inserted = True
                print(f"  Added toggle after fallback ({fallback_pattern}): {os.path.basename(filepath)}")
                break

    if not toggle_inserted:
        print(f"  WARN: Could not find insert point for toggle: {os.path.basename(filepath)}")

    # ── 4. Write back ────────────────────────────────────────────────────────
    if content != original:
        if not DRY_RUN:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  UPDATED: {os.path.basename(filepath)}")
        else:
            print(f"  DRY RUN — would update: {os.path.basename(filepath)}")
    else:
        print(f"  No changes: {os.path.basename(filepath)}")


def main():
    html_files = [f for f in os.listdir(BASE) 
                  if f.endswith('.html') and f not in SKIP_FILES 
                  and os.path.isfile(os.path.join(BASE, f))]
    
    print(f"Processing {len(html_files)} HTML files...")
    
    for fname in sorted(html_files):
        filepath = os.path.join(BASE, fname)
        print(f"\nProcessing: {fname}")
        try:
            process_file(filepath)
        except Exception as e:
            print(f"  ERROR: {e}")

    print("\nDone!")

if __name__ == '__main__':
    main()