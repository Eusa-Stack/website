/**
 * EUSTAQUIA Theme Manager — cross-page theme persistence
 * 
 * Usage:
 *   1. Include this script in <head> BEFORE any other stylesheets:
 *      <script src="theme-manager.js"></script>
 *   2. The script auto-detects the page's default theme (from inline CSS vars)
 *      and syncs it with localStorage.
 *   3. On subsequent pages, the stored theme is applied immediately (no flash).
 *   4. User can click a theme toggle button (add .theme-toggle to any element)
 *      to switch themes. The choice persists across all pages.
 * 
 * CSS classes applied to <html>:
 *   data-theme="dark"  — dark/academic theme
 *   data-theme="light" — light/warm theme
 * 
 * Per-file theme defaults (defined in THEME_DEFAULTS):
 *   Grammar/IELTS pages → dark
 *   Math/Games/General pages → light
 */

(function() {
  'use strict';

  var STORAGE_KEY = 'eusa-theme';

  // Map of filename → default theme for pages that need special defaults.
  // Pages not listed here default to the theme detected from their CSS vars.
  var THEME_DEFAULTS = {
    // Grammar pages (all dark)
    'grammar-hub.html':         'dark',
    'grammar-unit-01.html':     'dark',
    'grammar-unit-02.html':     'dark',
    'grammar-unit-03.html':     'dark',
    'grammar-unit-04.html':     'dark',
    'grammar-unit-05.html':     'dark',
    'grammar-unit-06.html':     'dark',
    'grammar-unit-07.html':     'dark',
    'grammar-unit-08.html':     'dark',
    'grammar-unit-09.html':     'dark',
    'grammar-unit-10.html':     'dark',
    'grammar-unit-11.html':     'dark',
    'grammar-unit-12.html':     'dark',
    'grammar-unit-13.html':     'dark',
    'grammar-unit-14.html':     'dark',
    'grammar-unit-15.html':     'dark',
    'grammar-unit-16.html':     'dark',
    'grammar-unit-17.html':     'dark',
    'grammar-unit-18.html':     'dark',
    'grammar-unit-19.html':     'dark',
    'grammar-unit-20.html':     'dark',
    'grammar-unit-21.html':     'dark',
    'grammar-unit-22.html':     'dark',
    'grammar-unit-23.html':     'dark',
    'grammar-unit-24.html':     'dark',
    'grammar-unit-25.html':     'dark',
    // IELTS pages (dark)
    'ielts-grammar.html':        'dark',
    'ielts-3-day-power-study.html': 'dark',
    'ielts-academic-general.html': 'dark',
    'ielts-band-score.html':    'dark',
    'ielts-writing-task2.html': 'dark',
    'ielts-all-4-subjects-interactive.html': 'dark',
    'ielts-drag-sort-quiz.html': 'dark',
    'ielts-listening.html':     'dark',
    'ielts-speaking.html':      'dark',
    // Light pages
    'subjects.html':            'light',
    'index.html':               'light',
    'word-match.html':          'light',
    'my-name.html':             'light',
    'math-games.html':          'light',
    'animal-sort.html':         'light',
    'flag-match.html':          'light',
    'fraction-pizza.html':      'light',
    'geo-challenge.html':       'light',
    'balance-lab.html':         'light',
    'force-lab.html':           'light',
    'element-mix.html':         'light',
    'demo-landing.html':        'light',
    'demo-v2.html':             'light',
    'demo-v3.html':             'light',
    'demo-v4.html':             'light'
  };

  // Detect the default theme for the current page.
  // Returns 'dark' or 'light'.
  function detectDefaultTheme() {
    var filename = window.location.pathname.split('/').pop() || '';
    if (THEME_DEFAULTS[filename]) return THEME_DEFAULTS[filename];

    // Fallback: detect from CSS variables in <style> or inline on <html>/<body>
    var styles = document.querySelector('style');
    var text = styles ? styles.textContent : '';

    // Dark pages use --bg with a dark colour
    if (text.indexOf('--bg') !== -1 || text.indexOf('--purple') !== -1) {
      return 'dark';
    }
    // Light pages use --orange / --warm palette
    if (text.indexOf('--orange') !== -1 || text.indexOf('--text:') !== -1) {
      return 'light';
    }
    return 'light'; // safe default
  }

  // Get the stored theme from localStorage
  function getStoredTheme() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch(e) {
      return null;
    }
  }

  // Store the theme to localStorage
  function storeTheme(theme) {
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch(e) {}
  }

  // Apply a theme to <html>
  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
  }

  // Initialise: decide which theme to apply
  function init() {
    var stored = getStoredTheme();
    var defaultTheme = detectDefaultTheme();

    if (stored === 'dark' || stored === 'light') {
      // User has a stored preference — use it
      applyTheme(stored);
    } else {
      // First visit — use page default and store it
      applyTheme(defaultTheme);
      storeTheme(defaultTheme);
    }
  }

  // Public API: allow pages to call EusaTheme.set('dark') etc.
  window.EusaTheme = {
    set: function(theme) {
      storeTheme(theme);
      applyTheme(theme);
    },
    get: function() {
      return getStoredTheme() || detectDefaultTheme();
    },
    toggle: function() {
      var current = document.documentElement.getAttribute('data-theme') || detectDefaultTheme();
      var next = current === 'dark' ? 'light' : 'dark';
      this.set(next);
      return next;
    }
  };

  // Expose init for use by pages
  window.EusaTheme.init = init;

  // Auto-init on DOMContentLoaded (before paint)
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();