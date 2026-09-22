# EduSuite — May 2026 Update Plan (Grammar Mastery Academy)

> **Client:** EUSTAQUIA | **Started:** 2026-05-14 | **Last updated:** 2026-05-15
> **Repo (source of truth):** Gitea `hermes/eusa-website` → production `github.com/Eusa-Stack/website`
> **Dev server:** `http://192.168.1.9:8877/` (kovaser Docker `eusa-http`, nginx:alpine)
> **Live:** https://eusa-stack.github.io/website/

---

## STATUS

| Phase | Deliverable | Status |
|-------|-------------|--------|
| 1 | MY NAME! activity (`my-name.html`) | ✅ Done |
| 2 | Grammar Hub, 5 modules (`grammar-hub.html`) | ✅ Done |
| 3 | 25 Grammar Units (`grammar-unit-01…25.html`) | ✅ Done |
| 4 | Personal Grammar Coach (`grammar-coach.html`) | ✅ Done |
| 5 | 6 IELTS pages | ✅ Done |
| 6 | Classroom / subjects update | ✅ Done |
| 7 | Navbar + theme unification across all pages | ✅ Done |
| — | Global shared footer | ✅ Done 16.5 |
| — | Home page intro rewritten (shorter) | ✅ Done 16.5 |

---

## ORIGINAL DESIGN BRIEF (client screenshots, 2026-05-14)

The client wants to transform EduSuite into a comprehensive **Grammar Mastery Academy** with multiple interactive course pages. The old `ielts-grammar.html` (35 KB, 25 MCQ topics) became a full course platform.

**Key insight from the 13 mockup screenshots:** all grammar images show the SAME dark-purple branded platform — "Grammar Meistery Hub" / "Grammar Mastery Academy", targeting IELTS Band 7+.

### Phase 1 — "MY NAME!" (source `my_name.png`, 1566x637)
- Green gradient background; "MY NAME!" — learn the letters in *your* name
- Input "TYPE YOUR STUDENT'S NAME HERE:" with hand pointer 👉; rounded gray field, placeholder "E.G. JUAN"
- Button "SET NAME!" with green checkmark ✓
- Implementation: `my-name.html`, one large letter card per letter, Web Speech API TTS per letter

### Phase 2 — Grammar Mastery Hub (sources `grammar.png`, `grammar_hub.png`, `grammar_mastery.png`)
```
HEADER: "Grammar Meistery Hub" (dark)
        "5 MODULES | 50-ITEM ASSESSMENT"; Nav: Home | Module 1-5 | Assessment
HERO:   "Grammar Power Pack"
        Sub: "Prepositions - Conditionals - Verb Patterns - Reported Speech"
        Stats: "5 Modules | 50 Quiz Items | 3 Difficulty Levels | Target: Band 7+"
MODULES: 1 Prepositions · 2 Conditionals 1 · 3 Conditionals 2
         4 Verb+Verb Patterns · 5 Reported Speech
```
Palette from the screenshots: primary dark purple (~#3B2D8C), background near-black (#1a1a2e), violet accents, white on dark, cream/white for lesson content areas.

### Phase 3 — 25 Grammar Unit lesson pages (sources `grammar_1-3.png`)

Three views of 10 tabs each. **Unit list in order:**

| View | Units |
|---|---|
| 1–10 | Present Tenses · Past Tenses · Present Perfect · Past Tenses 2 · Future 1 · Future 2 · Countable/Uncountable · Referring to Nouns · Pronouns · Adjectives/Adverbs |
| 11–20 | Comparing Things · Noun Phrase · Modals 1 · Modals 2 · Reported Speech · Verb+Verb Patterns · Conditionals 1 · Conditionals 2 · Prepositions · Relative Clauses |
| 21–25 | Ways of Organising Texts · The Passive · Linking Ideas · Showing Your Position · Nominalisation |

**Memory anchors requested:** **FARO** (passive: Focus, Agent removal, Register, Objectivity) and **CARP** (linking: Contrast, Addition, Result, Purpose).

**5 activity types per unit:** 📖 Lesson · 📝 Quiz (MCQ) · ✏️ Fill-in blanks · 🎤 Speaking (TTS) · 🎯 Match game (drag-drop).
**Progress system:** 🔥 streak (consecutive correct) · ⭐ XP · % mastery per unit.

### Phase 4 — Personal Grammar Coach (source `Grammar_coach.png`)
File upload → error analysis → lessons built from the student's *own* errors. Seven topics:
1. DO/DOES/DON'T/DOESN'T · 2. WAS/WERE/WASN'T/WEREN'T · 3. Question formation · 4. State verbs — never -ING · 5. Comparatives — no double forms · 6. 50 real conversation questions · 7. After did/does/don't — base verb always.

Error table format: `| Verb | WRONG ✗ | CORRECT ✓ |` (e.g. know — "I am knowing" — "I know").

### Phase 5 — Six new IELTS pages

| Mockup | Delivered as | Type |
|---|---|---|
| ielts_3_day_power_study.png | `ielts-3-day-power-study.html` | Banner/hero |
| ielts_academin_vs_general_.png | `ielts-academic-general.html` | Comparison |
| ielts_lesson_1_all_4_subjects__interactive.png | `ielts-all-4-subjects-interactive.html` | Interactive card |
| ielts_master_academin_Band_score.png | `ielts-band-score.html` | Dark landing |
| IELTS_Writing_Task_2_may_8.png | `ielts-writing-task2.html` | Blog/lesson |
| Drag_and_sort_quiz_ielts.png | `ielts-drag-sort-quiz.html` | Drag-drop quiz |

### Design standards

- **Dark theme (grammar section):** header #1a1a2e or #3B2D8C, progress indicators (streak / mastery % / XP), horizontal scrollable unit tabs
- **Light theme (games/math):** orange #F4845F, green #43B97A, yellow #F7C948, pink #E85D75, purple #A78BFA, canvas floating symbols, warm gradients
- **Typography:** headings Fredoka · body Inter/Nunito · grammar rules Cormorant Garamond (serif italic) · grammar forms monospace
- **Child-friendly:** emoji ≥48 px, big touch targets, one subject at a time

---

## FILE INVENTORY

### Core pages (3)

| File | Purpose |
|---|---|
| `index.html` | Home — EUSTAQUIA story + CTA |
| `classroom.html` | Main hub — 7 subjects |
| `subjects.html` | Redirect → `classroom.html` |

### Games (14)

| File | Subject |
|---|---|
| `flag-match.html` · `geo-challenge.html` | Geography |
| `time-train.html` | History |
| `math-games.html` · `number-ninja.html` · `fraction-pizza.html` | Math |
| `animal-sort.html` | Biology |
| `gravity-drop.html` · `force-lab.html` | Physics |
| `element-mix.html` · `balance-lab.html` | Chemistry |
| `word-match.html` · `my-name.html` | Vocabulary |
| `quick-quiz.html` | General |

### Grammar (3 + 25 units)
`grammar-hub.html`, `grammar-coach.html`, `grammar-unit-01.html` … `grammar-unit-25.html`

### IELTS (8)
`ielts.html` · `ielts-grammar.html` · `ielts-3-day-power-study.html` · `ielts-academic-general.html` · `ielts-band-score.html` · `ielts-writing-task2.html` · `ielts-all-4-subjects-interactive.html` · `ielts-drag-sort-quiz.html`

### Shared / global resources

| File | Purpose |
|---|---|
| `navbar.css` | Global navbar styles (sticky, blur backdrop) |
| `theme.css` | Light/dark colour variables |
| `theme-manager.js` | Theme persistence (localStorage `eusa-theme`), `EusaTheme` object |
| `grammar-shared.css` | Fonts + shared styles |
| `floating-anim.js` | Canvas floating-symbol animation |
| `footer.css` | **Global footer styles** |
| `footer-inject.js` | **Global footer injection** |

---

## GLOBAL FOOTER (16.5.2026)

The footer used to be hand-written inline on every page, so it drifted page by page. It is now one shared definition, exactly like the navbar and the theme.

**How it works.** Each page carries only:

```html
<link rel="stylesheet" href="footer.css">      <!-- in <head> -->
<div id="shared-footer-placeholder"></div>     <!-- where the footer goes -->
<script src="footer-inject.js"></script>       <!-- last, before </body> -->
```

`footer-inject.js` renders the footer markup into the placeholder and removes it. Every page loads the same stylesheet, so **one edit to `footer.css` or `footer-inject.js` changes all 57 pages** — no per-page HTML.

Footer content:

```
© EUSTAQUIA — Global Educator
Classroom · YouTube · Privacy · tech-ant — tech-ant.fi
```

---

## BRANDING RULE (owner's decision, 16.5.2026)

**EduSuite is a client site. The client's brand is EUSTAQUIA and it stays.**

- The author credit appears **only in the footer**, on every page, small and quiet: `tech-ant — tech-ant.fi`, both words linking to `https://tech-ant.fi` (new tab), ~0.75–0.8 rem, purple at low opacity.
- **No author branding anywhere else** — not in the hero, not in the title, not in `<meta>` author/description, not in the `<h1>`, not in page titles.
- Do **not** rename the client's site, teacher name, or alt text. An earlier bulk "rebranding" commit that replaced EUSTAQUIA with the author's name across all pages was wrong and was reverted (`190549f`).

---

## HOME PAGE INTRO (16.5.2026)

The old intro was a long "27 years in classrooms" biography plus a mission line and a Montessori quote. The owner asked for it shorter. The `lumina-card` now carries:

> **Welcome, Young Learners! 🌱**
>
> This little learning space was created to make learning English, Math, and other subjects more interactive, meaningful, and fun. Explore, practice, count, solve, and discover—one small step at a time. 💛
>
> *"We may come to work with knowledge, but we leave each day with something new to learn."*

The heading uses `.lumina-welcome` (Cormorant Garamond, 26 px, 700).

---

## CLASSROOM STRUCTURE

```
🎓 Classroom — Choose a Subject
├── 📐 Math (3): math-games, number-ninja, fraction-pizza
├── 🌍 Geography (2): flag-match, geo-challenge
├── 🏛️ History (1): time-train
├── 🧪 Science (5): animal-sort, gravity-drop, force-lab, element-mix, balance-lab
├── 📝 Language (6): word-match, my-name, grammar-hub, grammar-coach, ielts-grammar, ielts
├── 🎓 IELTS (6): 3-day-power-study, academic-general, band-score, writing-task2, all-4-subjects, drag-sort-quiz
└── 🧠 General (1): quick-quiz
```

Stats bar: **10 Subjects · 14 Games · 24 Pages · 6–16 Age Range** — four compact `.stat-card` boxes (`.sn` number, `.sl` label). The search box and the All/Math/Science/Language/IELTS filter row were removed: they took space and were not used.

---

## NAVBAR (all pages, consistent)

```
[EduSuite .]  [🏠 Home]  [🎓 Classroom]       [Home]  [☾/☀]
```

Theme toggle ☾ dark / ☀ light, stored in localStorage `eusa-theme`, applied as `<html data-theme="dark|light">` (not a body class).

---

## BUG CORRECTIONS (16.5.2026)

1. **Missing navbar on 40+ game pages** — old `← All Games` / `← Back` nav. Fixed: global navbar everywhere; `navbar.css` + `grammar-shared.css` added where missing.
2. **Theme toggle broken on most pages** — `EustaTheme.toggle()` typo, and 4 IELTS pages had no `theme-manager.js` at all. Fixed to `EusaTheme.toggle()` everywhere.
3. **Background did not change with the theme** — 15 game pages hardcoded a `linear-gradient(...)` body background instead of `var(--bg)`, so dark mode showed a warm gradient. Fixed: all bodies use `var(--bg)`.
4. **Two theme toggles on `index.html`** — one in the navbar and one in the hero. The hero one was removed.
5. **`subjects.html` vs `classroom.html`** — two pages with the same purpose. Merged; `subjects.html` is now a redirect and every `href="subjects.html"` points to `classroom.html`.
6. **Classroom stats bar unstyled** — rendered as plain vertical text. Fixed with `.stats-bar` / `.stat-card` / `.sn` / `.sl`.
7. **Classroom `renderSubjectGrid` crash** — the function read `searchInput.value` unguarded; removing the search box broke the grid. Fixed with a null check.
8. **Classroom missing pages** — `ielts.html` and the 25 grammar units were unreachable from the classroom. Added.
9. **Footer drift** — replaced by the global footer above.
10. **Wrong author rebranding** — reverted (see Branding Rule).

---

## GIT HISTORY

| Commit | Date | Description |
|---|---|---|
| `8122dd5` | 16.5 | content: shorter welcome intro on index.html |
| `3e024a0` | 16.5 | feat: global shared footer (footer.css + footer-inject.js) |
| `190549f` | 16.5 | feat: subtle tech-ant footer branding on all pages |
| `6d5124a` | 16.5 | chore: rebranding (later reverted — see Branding Rule) |
| `3beb53b` | 16.5 | fix: theme toggle + stats bar + search removed |
| `3e4713b` | 16.5 | fix: global navbar + theme toggle on all pages |
| `80c1d46` | 16.5 | refactor: merged subjects into classroom |
| `84e9543` | 16.5 | feat: global navbar + classroom redesign |
| `35f5b23` | 15.5 | feat: Phase 7 subjects.html overhaul |
| `9cd9e84` | 15.5 | feat: 6 new IELTS pages |
| `c580d6f` | 14.5 | feat: Grammar Coach + unified theme system |
| `4baab15` | 13.5 | feat: 25 Grammar Units generated |
| `0cc73a2` | 12.5 | feat: Grammar Hub (5 modules) |
| `d638550` | 11.5 | feat: My Name! + Word Match Jr rebuild |

---

## PUBLISH WORKFLOW

```bash
# 1. development server (kovaser)
git push gitea main

# 2. production — GitHub Pages (needs the deploy key)
GIT_SSH_COMMAND="ssh -i ~/.ssh/eusa-website_deploy" git push origin main
```

GitHub Actions runs `.github/workflows/deploy.yml` → GitHub Pages. Verify in `/actions` that **both** runs are green (`Deploy to GitHub Pages` and `pages-build-deployment`), then check the live URL with `curl`.

---

## PITFALLS

- **Deploying to the dev server:** `rsync`/`scp` to `192.168.1.9` can time out; `cat FILE | base64 | ssh ... python3 -c "base64.b64decode(...)"` is the reliable path. Restart with `docker restart eusa-http`.
- **A pushed file is not a visible change** — nginx serves from the Docker mount `/mnt/media/eusa-sandbox`; confirm with `curl` against `:8877` before declaring done.
- **The wiki `update_page` replaces the entire page.** Read the page first and resend every unchanged section. Condensing a page to "summarise my work" silently deletes the original content — this happened to *this* page on 16.5 and was restored from `pageHistory`.
- **Do not bulk-rename the client's brand.** Search-and-replace across 55 files is fast and easy to get wrong; see the Branding Rule.
- **The browser tool blocks private addresses** — verify `192.168.1.9:8877` with `curl`, and use the public GitHub Pages URL for browser checks.
- **`subjects.html` is a redirect, not a page** — never link new content to it as if it were a destination.

---

*Original source files analysed: grammar.png, grammar_1-3.png, Grammar_coach.png, grammar_hub.png, grammar_mastery.png, ielts_*.png, Drag_and_sort_quiz_ielts.png, my_name.png — analysis via OCR (grammar images) + pixel analysis (IELTS images).*
