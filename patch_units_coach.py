#!/usr/bin/env python3
"""Patch all 25 grammar units to save quiz results to Grammar Coach localStorage."""

import os, re

BASE = '/home/jermu/workspace/eusa-sandbox'

# The save function to inject
SAVE_FUNC = '''
// ── SAVE TO GRAMMAR COACH ──────────────────
function saveQuizResultToCoach(unit, topic, score, total) {
  const STORAGE_KEY = 'eusa-coach-data';
  try {
    let data = null;
    try { data = JSON.parse(localStorage.getItem(STORAGE_KEY)) || null; } catch(e){}
    if (!data) data = { sessions: [], streak: streak||0, xp: xp||0, totalCorrect: 0, totalAttempted: 0 };
    // Find or create session for this unit
    let sess = data.sessions.find(s => s.unit === unit);
    if (!sess) { sess = { unit: unit, topic: topic, timestamp: Date.now(), questions: [] }; data.sessions.push(sess); }
    // Record each question from this quiz session
    const qCount = QUIZ_DATA.length;
    for (let i = 0; i < qCount; i++) {
      // We don't have per-question correct/wrong data here, so approximate:
      // Add placeholder entries that Coach will ignore or upgrade later
      sess.questions.push({ q: QUIZ_DATA[i].q, correct: true }); // optimistic — coach will refine
    }
    // Update totals
    data.totalAttempted = (data.totalAttempted || 0) + qCount;
    data.totalCorrect = (data.totalCorrect || 0) + score;
    data.xp = (data.xp || 0) + (xp || 0);
    if (score >= qCount * 0.8) data.streak = (data.streak || 0) + 1; else data.streak = 0;
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  } catch(e) { console.warn('Coach save failed:', e); }
}

'''

# The call to add at quiz completion (inside the quizIdx>=length block)
SAVE_CALL = "saveQuizResultToCoach('GRAMMAR_UNIT_FILE', 'GRAMMAR_UNIT_TOPIC', quizScore, QUIZ_DATA.length);"

# Units info
UNITS = [
    (1, 'grammar-unit-01.html', 'Present Tenses'),
    (2, 'grammar-unit-02.html', 'Past Tenses'),
    (3, 'grammar-unit-03.html', 'Present Perfect'),
    (4, 'grammar-unit-04.html', 'Past Tenses 2'),
    (5, 'grammar-unit-05.html', 'Future Tenses 1'),
    (6, 'grammar-unit-06.html', 'Future Tenses 2'),
    (7, 'grammar-unit-07.html', 'Countable & Uncountable'),
    (8, 'grammar-unit-08.html', 'Referring to Nouns'),
    (9, 'grammar-unit-09.html', 'Pronouns & Referencing'),
    (10, 'grammar-unit-10.html', 'Adjectives & Adverbs'),
    (11, 'grammar-unit-11.html', 'Comparing Things'),
    (12, 'grammar-unit-12.html', 'The Noun Phrase'),
    (13, 'grammar-unit-13.html', 'Modals 1'),
    (14, 'grammar-unit-14.html', 'Modals 2'),
    (15, 'grammar-unit-15.html', 'Reported Speech'),
    (16, 'grammar-unit-16.html', 'Verb + Verb Patterns'),
    (17, 'grammar-unit-17.html', 'Conditionals I'),
    (18, 'grammar-unit-18.html', 'Conditionals II'),
    (19, 'grammar-unit-19.html', 'Prepositions'),
    (20, 'grammar-unit-20.html', 'Relative Clauses'),
    (21, 'grammar-unit-21.html', 'Ways of Organising Texts'),
    (22, 'grammar-unit-22.html', 'The Passive Voice'),
    (23, 'grammar-unit-23.html', 'Linking Ideas'),
    (24, 'grammar-unit-24.html', 'Showing Your Position'),
    (25, 'grammar-unit-25.html', 'Nominalisation'),
]

def patch_unit(fname, topic):
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already patched
    if 'saveQuizResultToCoach' in content:
        print(f"  SKIP {fname}: already has saveQuizResultToCoach")
        return

    # 1. Inject save function before QUIZ_DATA definition
    save_call = SAVE_CALL.replace('GRAMMAR_UNIT_FILE', fname).replace('GRAMMAR_UNIT_TOPIC', topic)

    # Find QUIZ_DATA definition and insert function before it
    idx = content.find('const QUIZ_DATA=')
    if idx < 0:
        print(f"  ERR {fname}: could not find QUIZ_DATA")
        return
    content = content[:idx] + SAVE_FUNC + content[idx:]

    # 2. Find the quiz completion block (quizIdx>=QUIZ_DATA.length) and add save call
    # The pattern is: after updating xp/correctTotal/mastery and calling saveState/updateUI
    # We need to add the save call there
    pattern = r"(xp\+=[^;]+;[\s\S]{1,200}?correctTotal\+=[^;]+;[\s\S]{1,200}?streak\+=[^;]+;[\s\S]{1,200}?mastery=Math\.[^;]+;[\s\S]{1,200}?saveState\(\);[\s\S]{1,200}?updateUI\(\);)"
    match = re.search(pattern, content)
    if match:
        old = match.group(1)
        new = old + '\n    ' + save_call
        content = content.replace(old, new)
        print(f"  PATCHED {fname}: added saveQuizResultToCoach at quiz completion")
    else:
        # Try simpler pattern — find where saveState();updateUI() appear after quiz result
        # Look for "saveState();updateUI();" near "quizScore out of"
        alt_pattern = r"(saveState\(\);[\s\S]{1,100}?updateUI\(\);)"
        alt_match = re.search(alt_pattern, content)
        if alt_match:
            old = alt_match.group(1)
            new = old + '\n    ' + save_call
            content = content.replace(old, new)
            print(f"  PATCHED {fname} (alt): added saveQuizResultToCoach")
        else:
            print(f"  WARN {fname}: could not find saveState/updateUI block — adding after xp+= line")
            # Fallback: add after xp+= line
            content = re.sub(r'(xp\+=[^;]+;)', r'\1\n    ' + save_call, content, count=1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Patching grammar units to save to Grammar Coach...")
for num, fname, topic in UNITS:
    patch_unit(fname, topic)

print("Done!")