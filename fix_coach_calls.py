#!/usr/bin/env python3
"""Remove duplicate saveQuizResultToCoach calls — keep only at quiz completion."""

import os, re

BASE = '/home/jermu/workspace/eusa-sandbox'

UNITS = [
    (1, 'grammar-unit-01.html'), (2, 'grammar-unit-02.html'), (3, 'grammar-unit-03.html'),
    (4, 'grammar-unit-04.html'), (5, 'grammar-unit-05.html'), (6, 'grammar-unit-06.html'),
    (7, 'grammar-unit-07.html'), (8, 'grammar-unit-08.html'), (9, 'grammar-unit-09.html'),
    (10, 'grammar-unit-10.html'), (11, 'grammar-unit-11.html'), (12, 'grammar-unit-12.html'),
    (13, 'grammar-unit-13.html'), (14, 'grammar-unit-14.html'), (15, 'grammar-unit-15.html'),
    (16, 'grammar-unit-16.html'), (17, 'grammar-unit-17.html'), (18, 'grammar-unit-18.html'),
    (19, 'grammar-unit-19.html'), (20, 'grammar-unit-20.html'), (21, 'grammar-unit-21.html'),
    (22, 'grammar-unit-22.html'), (23, 'grammar-unit-23.html'), (24, 'grammar-unit-24.html'),
    (25, 'grammar-unit-25.html'),
]

for num, fname in UNITS:
    path = os.path.join(BASE, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the quiz completion block — only keep the save inside
    # Pattern: inside "if(quizIdx>=QUIZ_DATA.length)" we want ONE save call
    # Remove all other saveQuizResultToCoach calls that appear outside the completion block

    # The function saveQuizResultToCoach should stay (it's injected once at top)
    # The call inside the per-answer function (pickQuiz) should be removed
    # The call inside quiz completion (quizIdx>=length) should stay

    # Find all occurrences of the call
    occurrences = [m.start() for m in re.finditer(r"saveQuizResultToCoach\('[^']+',\s*'[^']+',\s*quizScore,", content)]
    print(f"{fname}: {len(occurrences)} saveQuizResultToCoach call(s) at positions: {occurrences[:5]}")

    if len(occurrences) <= 1:
        print(f"  OK — only 1 call, skipping")
        continue

    # Keep only the LAST occurrence (that's the completion block), remove others
    # The completion block is the one inside "if(quizIdx>=QUIZ_DATA.length){...}"
    # which ends with saveState();updateUI(); and then saveQuizResultToCoach
    # The per-answer calls are in the pickQuiz function before "quizIdx++"

    # Strategy: keep the occurrence closest to "quizIdx>=QUIZ_DATA.length" block
    # We'll remove all except the one that appears after "saveState();updateUI();"
    # in the quiz completion section

    # Simple approach: find the one in the completion block by looking for
    # "saveState();updateUI();" followed shortly by "saveQuizResultToCoach"
    completion_save = None
    for m in re.finditer(r"saveState\(\);[\s\S]{1,200}?saveQuizResultToCoach", content):
        completion_save = m.start()

    if completion_save is None:
        print(f"  WARN: could not find completion block, keeping last occurrence")
        completion_save = occurrences[-1]
        # Remove all but last
        to_remove = occurrences[:-1]
    else:
        # Keep completion save, remove all others
        to_remove = [pos for pos in occurrences if pos != completion_save]

    # Remove them (in reverse order to preserve positions)
    for pos in reversed(to_remove):
        # Find the full line with this call
        line_start = content.rfind('\n', 0, pos)
        line_end = content.find('\n', pos)
        if line_end < 0: line_end = len(content)
        # Remove the line
        content = content[:line_start] + content[line_end:]

    remaining = content.count("saveQuizResultToCoach")
    print(f"  → {remaining} calls remaining")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done!")