#!/usr/bin/env python3
"""Generate Grammar Units 12-25."""

import os, re

BASE = '/home/jermu/workspace/eusa-sandbox'

UNITS_12_25 = [
  (12, "The Noun Phrase", "Compounding · Modification · Genitive · Apposition",
   """<div class="sect">
     <div class="sect-title">📖 Compounding Nouns</div>
     <div class="rule-box">
       <strong>Compound nouns:</strong> noun + noun (most common)<br>
       "classroom" (class + room) · "textbook" (text + book)<br>
       <strong>Patterns:</strong> noun+noun · adj+noun · verb+noun<br>
       "police station" · "bus stop" · "swimming pool"
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Tip:</strong> Noun+noun = the SECOND noun is the main thing. A "classroom" = a room for classes.</span></div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Modification (Adjectives + Nouns)</div>
     <div class="rule-box">
       <strong>Adj + Noun:</strong> "a <strong>cold</strong> day" · "a <strong>big</strong> house"<br>
       Multiple adjectives need a specific ORDER<br>
       Opinion → Size → Age → Shape → Colour → Origin
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Genitive ('s)</div>
     <div class="rule-box">
       <strong>Possession:</strong> noun + 's · "the teacher's book"<br>
       <strong>Use:</strong> people, animals, time expressions<br>
       "the boy's room" · "the dog's tail" · "yesterday's lesson"
     </div>
     <div class="usecase">
       <strong>Of-phrase:</strong> for places and things<br>
       "the roof of the house" · "the end of the story"<br>
       "the capital of the Philippines" = "Manila's capital" (NO — wrong!)
     </div>
   </div>""",
   [("The ___ teacher is very kind.", ["boy's","boys","boys'","boy"], 0),
    ("I need a new ___.", ["textbook","texts book","text book's","texts books"], 0),
    ("The ___ of the school is very old.", ["building","school's building","building's","school building"], 0),
    ("She is a ___ student.", ["kind","kindly","kindness","more kind"], 0),
    ("This is the ___ book I have ever read.", ["most interesting","more interesting","interestinger","most interesting"], 0),
    ("The children ___ in the park are happy.", ["who are playing","playing","are playing","that playing"], 0),
    ("A ___ house (adj order: color, age)", ["beautiful old","old beautiful","beautiful big","big old"], 0),
    ("The ___ of Manila is beautiful.", ["capital","Manila capital","capital's Manila","Manila's capital"], 0),
    ("She is ___ student in class.", ["the best","best","more best","the goodest"], 0),
    ("He gave me a ___ book.", ["large red","red large","large big","big red"], 0)],
   [("The ___ teacher is kind. (boy → ?)", "boy's"),
    ("I need a new ___. (textbook/text book)", "textbook"),
    ("The ___ of the school is old. (building/school building)", "building"),
    ("She is a ___ student. (kind/kindly)", "kind"),
    ("This is the ___ book. (interesting → compar)", "most interesting"),
    ("The children ___ in the park are happy. (play → ?)", "who are playing"),
    ("The ___ of Manila is beautiful. (capital)", "capital"),
    ("She is ___ student in class. (good → best)", "the best")],
   ["The teacher's book is on the table.",
    "I need a new textbook for class.",
    "The building of the school is old.",
    "She is a kind student.",
    "The children who are playing in the park are happy.",
    "The capital of Manila is beautiful.",
    "A beautiful old house stands on the hill.",
    "He gave me a large red book."],
   [("teacher's book","action"),("textbook","state"),("building of the school","state"),("kind student","action"),
    ("most interesting","state"),("who are playing","action"),("capital of Manila","state"),("large red book","action")]),

  (13, "Modals 1", "Can · Could · May · Might · Must · Have to",
   """<div class="sect">
     <div class="sect-title">📖 Can / Can't</div>
     <div class="rule-box">
       <strong>CAN:</strong> ability · permission · possibility<br>
       "I <strong>can swim</strong>." (ability)<br>
       "You <strong>can use</strong> my pen." (permission)<br>
       <strong>Can't:</strong> inability · prohibition<br>
       "I <strong>can't understand</strong>." (cannot)
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Could (Past Ability / Polite Request)</div>
     <div class="rule-box">
       <strong>Past ability:</strong> "When I was young, I <strong>could run</strong> fast."<br>
       <strong>Polite request:</strong> "<strong>Could</strong> you help me?" (softer than "Can")<br>
       <strong>Possibility:</strong> "It <strong>could rain</strong> later." (uncertain)
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Must / Have to / Mustn't</div>
     <div class="rule-box">
       <strong>Must / Have to:</strong> obligation, necessity<br>
       "You <strong>must</strong> study." · "You <strong>have to</strong> study."<br>
       <strong>Mustn't:</strong> prohibition (MUST NOT)<br>
       "You <strong>mustn't cheat</strong>." (never do this)<br>
       <strong>Don't have to:</strong> no obligation (optional)<br>
       "You <strong>don't have to come</strong>." (optional)
     </div>
   </div>""",
   [("You ___ study hard for the exam.", ["must","can","might","could"], 0),
    ("I ___ swim when I was five years old.", ["could","can","must","may"], 0),
    ("___ I use your phone?", ["Could","Must","Can","Have to"], 0),
    ("You ___ cheat in the exam. It's wrong.", ["mustn't","don't have to","don't must","can't"], 0),
    ("She ___ be at home by 9 PM. It's the rule.", ["has to","must","can","could"], 0),
    ("It ___ rain later. The sky is dark.", ["might","must","can","have to"], 0),
    ("You ___ do the homework if you want to pass.", ["must","can","could","might"], 0),
    ("He ___ speak three languages.", ["can","must","have to","mustn't"], 0),
    ("___ I help you with that?", ["May","Must","Have to","Can to"], 0),
    ("You ___ come early tomorrow. It's optional.", ["don't have to","mustn't","can't","haven't to"], 0)],
   [("You ___ study hard. (must/can)", "must"),
    ("I ___ swim when I was five. (can/could)", "could"),
    ("___ I use your phone? (Can/Could)", "Could"),
    ("You ___ cheat. It's wrong. (mustn't/don't have to)", "mustn't"),
    ("She ___ be at home by 9 PM. (must/has to)", "has to"),
    ("It ___ rain later. (might/must)", "might"),
    ("You ___ come early. It's optional. (don't have to/mustn't)", "don't have to"),
    ("He ___ speak three languages. (can/must)", "can")],
   ["You must study hard for the exam.",
    "I could swim when I was five years old.",
    "Could I use your phone?",
    "You mustn't cheat in the exam.",
    "She has to be at home by 9 PM.",
    "It might rain later.",
    "He can speak three languages.",
    "You don't have to come early tomorrow."],
   [("must study","action"),("could swim","action"),("use your phone","state"),("mustn't cheat","action"),
    ("has to be","state"),("might rain","action"),("can speak","state"),("don't have to come","action")]),

  (14, "Modals 2", "Should · Ought to · Would · Could have · Must have",
   """<div class="sect">
     <div class="sect-title">📖 Should / Shouldn't</div>
     <div class="rule-box">
       <strong>SHOULD:</strong> advice · recommendation<br>
       "You <strong>should study</strong> more." (advice)<br>
       <strong>SHOULDN'T:</strong> negative advice<br>
       "You <strong>shouldn't give up</strong>."
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Should = advice in present/future</strong></span></div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Would (Hypothetical / Polite)</div>
     <div class="rule-box">
       <strong>Hypothetical:</strong> "If I <strong>were</strong> you, I <strong>would study</strong>."<br>
       <strong>Polite request:</strong> "<strong>Would</strong> you like some tea?"<br>
       <strong>Would + have + past participle:</strong> unreal past<br>
       "If I had known, I <strong>would have helped</strong>."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Must have / Could have (Deduction)</div>
     <div class="rule-box">
       <strong>Must have:</strong> strong deduction about the past<br>
       "She <strong>must have left</strong>." (I'm sure she left)<br>
       <strong>Could have:</strong> missed opportunity<br>
       "You <strong>could have passed</strong>." (but you didn't)
     </div>
   </div>""",
   [("You ___ study harder. It's important.", ["should","must","can","would"], 0),
    ("If I were you, I ___ take the job.", ["would","can","must","could"], 0),
    ("She ___ have studied more. She failed.", ["shouldn't","wouldn't","mustn't","couldn't"], 0),
    ("He ___ be at home. His car is in the garage.", ["must","can","could","might"], 0),
    ("You ___ have told me earlier. I could have helped.", ["could","should","would","must"], 0),
    ("If I had studied, I ___ passed.", ["would have","must have","could have","should have"], 0),
    ("___ you like some tea?", ["Would","Can","Must","Should"], 0),
    ("She ___ have gone to the party. She was tired.", ["might","must","should","can"], 0),
    ("You ___ give up. Keep trying!", ["shouldn't","mustn't","don't have to","couldn't"], 0),
    ("He ___ have been at the meeting. I saw him there.", ["must","can","might","could"], 0)],
   [("You ___ study harder. (should/must)", "should"),
    ("If I were you, I ___ take the job. (would/should)", "would"),
    ("She ___ have studied more. (shouldn't/couldn't)", "shouldn't"),
    ("He ___ be at home. His car is there. (must/can)", "must"),
    ("You ___ have told me earlier. (could/should)", "could"),
    ("If I had studied, I ___ passed. (would have/must have)", "would have"),
    ("___ you like some tea? (Would/Can)", "Would"),
    ("You ___ give up. Keep trying! (shouldn't/mustn't)", "shouldn't")],
   ["You should study harder.",
    "If I were you, I would take the job.",
    "She should have studied more.",
    "He must be at home.",
    "You could have told me earlier.",
    "If I had studied, I would have passed.",
    "Would you like some tea?",
    "You shouldn't give up."],
   [("should study","action"),("would take","action"),("should have studied","action"),("must be","state"),
    ("could have told","action"),("would have passed","action"),("would like","state"),("shouldn't give up","action")]),

  (15, "Reported Speech", "Say vs Tell · Backshift · Reporting verbs",
   """<div class="sect">
     <div class="sect-title">📖 Say vs Tell</div>
     <div class="rule-box">
       <strong>SAY:</strong> no object needed · "She said hello."<br>
       <strong>TELL:</strong> needs object · "She told me a story."<br>
       <strong>Key:</strong> TELL always needs a person (indirect object)
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Backshift (Tense Changes)</div>
     <div class="rule-box">
       Direct: "I <strong>am</strong> studying." → Reported: "He said he <strong>was</strong> studying."<br>
       Direct: "I <strong>will come</strong>." → Reported: "He said he <strong>would come</strong>."<br>
       Direct: "I <strong>have</strong> finished." → Reported: "He said he <strong>had</strong> finished."<br>
       Direct: "I <strong>can swim</strong>." → Reported: "He said he <strong>could swim</strong>."
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Rule:</strong> Move tenses BACK one step: am→was, is→was, will→would, have→had, can→could</span></div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Reporting Verbs</div>
     <div class="rule-box">
       <strong>Say / Tell:</strong> basic reporting<br>
       <strong>Ask:</strong> questions · "He asked me what my name was."<br>
       <strong>Suggest / Recommend:</strong> ideas · "She suggested studying harder."<br>
       <strong>Warn / Advise:</strong> advice · "He warned me not to be late."
     </div>
   </div>""",
   [("She ___ she was tired.", ["said","told","asks","tell"], 0),
    ("He ___ me to study harder.", ["told","said","says","tell"], 0),
    ("'I am coming,' she said → She said she ___ coming.", ["was","is","will be","had been"], 0),
    ("'I will help you,' he said → He said he ___ help me.", ["would","will","can","must"], 0),
    ("He ___ me what my name was.", ["asked","said","told","says"], 0),
    ("She ___ studying harder.", ["suggested","said","told","ask"], 0),
    ("'I have finished,' he said → He said he ___ finished.", ["had","has","was","was having"], 0),
    ("He ___ me not to be late.", ["warned","said","suggested","told"], 0),
    ("'I can speak English,' she said → She said she ___ speak English.", ["could","can","was able to","might"], 0),
    ("She ___ that she was going to the market.", ["said","told","ask","suggested"], 0)],
   [("She ___ she was tired. (say/tell)", "said"),
    ("He ___ me to study harder. (tell/say)", "told"),
    ("'I am coming' → She said she ___ coming. (am → ?)", "was"),
    ("'I will help you' → He said he ___ help. (will → ?)", "would"),
    ("He ___ me what my name was. (ask/say)", "asked"),
    ("She ___ studying harder. (suggest/say)", "suggested"),
    ("'I have finished' → He said he ___ finished. (has → ?)", "had"),
    ("He ___ me not to be late. (warned/suggested)", "warned")],
   ["She said she was tired.",
    "He told me to study harder.",
    "She said she was coming.",
    "He said he would help me.",
    "He asked me what my name was.",
    "She suggested studying harder.",
    "He said he had finished.",
    "He warned me not to be late."],
   [("said she was","state"),("told me to study","action"),("was coming","action"),("would help","state"),
    ("asked me","action"),("suggested studying","action"),("had finished","state"),("warned me","action")]),

  (16, "Verb + Verb Patterns", "Gerunds · Infinitives · Meaning change patterns",
   """<div class="sect">
     <div class="sect-title">📖 Verb + Gerund (-ing) vs Verb + Infinitive (to)</div>
     <div class="rule-box">
       <strong>+ Gerund (-ing):</strong> enjoy · finish · stop · mind · suggest · practice · avoid<br>
       "I enjoy <strong>reading</strong>." · "She finished <strong>studying</strong>."<br>
       <strong>+ Infinitive (to):</strong> decide · want · need · hope · plan · learn · promise<br>
       "I decided <strong>to go</strong>." · "She wants <strong>to improve</strong>."
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Key:</strong> Some verbs can take BOTH with same meaning: like, love, hate, start, begin<br>
       "I like swimming" = "I like to swim" (same meaning)</span></div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Meaning Change</div>
     <div class="rule-box">
       <strong>remember + -ing:</strong> did something first, then remembered<br>
       "<strong>Remember to lock</strong> the door." (do this LATER)<br>
       "<strong>Remember locking</strong> the door." (memory of past action)<br>
       <strong>stop + -ing:</strong> stopped an activity<br>
       "<strong>Stop talking</strong>." (quit the activity)<br>
       <strong>try + -ing:</strong> experiment with something<br>
       "<strong>Try using</strong> a different method." (experiment)
     </div>
   </div>""",
   [("I enjoy ___ in the morning.", ["swimming","to swim","swim","swam"], 0),
    ("She decided ___ to the market.", ["to go","going","go","went"], 0),
    ("Remember ___ the door before you leave.", ["to lock","locking","lock","locked"], 0),
    ("I stopped ___ when the teacher came in.", ["talking","to talk","talk","talked"], 0),
    ("Try ___ a different method.", ["using","to use","use","used"], 0),
    ("He suggested ___ to the party.", ["going","to go","go","went"], 0),
    ("I remember ___ her at the conference.", ["meeting","to meet","meet","met"], 0),
    ("She hates ___ alone.", ["being","to be","be","been"], 0),
    ("I started ___ English three years ago.", ["learning","to learn","learn","learned"], 0),
    ("Remember ___ your homework tonight.", ["to do","doing","do","did"], 0)],
   [("I enjoy ___ in the morning. (swim → ?)", "swimming"),
    ("She decided ___ to the market. (go → ?)", "to go"),
    ("Remember ___ the door. (lock → ?)", "to lock"),
    ("I stopped ___ when the teacher came in. (talk → ?)", "talking"),
    ("Try ___ a different method. (use → ?)", "using"),
    ("He suggested ___ to the party. (go → ?)", "going"),
    ("I remember ___ her at the conference. (meet → ?)", "meeting"),
    ("She hates ___ alone. (be → ?)", "being")],
   ["I enjoy swimming in the morning.",
    "She decided to go to the market.",
    "Remember to lock the door before you leave.",
    "I stopped talking when the teacher came in.",
    "Try using a different method.",
    "He suggested going to the party.",
    "I remember meeting her at the conference.",
    "Remember to do your homework tonight."],
   [("swimming","action"),("to go","state"),("to lock","state"),("talking","action"),
    ("using","action"),("going","state"),("meeting","action"),("being","state")]),

  (17, "Conditionals 1", "Zero · First · Second · Third Conditional",
   """<div class="sect">
     <div class="sect-title">📖 Zero Conditional (General Truth)</div>
     <div class="rule-box">
       <strong>Form:</strong> If + Present Simple, Present Simple<br>
       <strong>Use:</strong> general truths, scientific facts, habits<br>
       "If you <strong>heat</strong> water, it <strong>boils</strong>."<br>
       "If it <strong>rains</strong>, I <strong>stay</strong> inside."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 First Conditional (Real Possible Future)</div>
     <div class="rule-box">
       <strong>Form:</strong> If + Present Simple, will + verb<br>
       <strong>Use:</strong> real and possible in the future<br>
       "If it <strong>rains</strong>, I <strong>will stay</strong> home."<br>
       "If you <strong>study</strong>, you <strong>will pass</strong>."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Second Conditional (Unreal Present/Future)</div>
     <div class="rule-box">
       <strong>Form:</strong> If + Past Simple, would + verb<br>
       <strong>Use:</strong> hypothetical, unreal, imaginary<br>
       "If I <strong>had</strong> a million dollars, I <strong>would travel</strong>."<br>
       "If I <strong>were</strong> you, I <strong>would accept</strong>."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Third Conditional (Unreal Past)</div>
     <div class="rule-box">
       <strong>Form:</strong> If + Past Perfect, would have + past participle<br>
       <strong>Use:</strong> unreal past situations and their results<br>
       "If I <strong>had studied</strong>, I <strong>would have passed</strong>."<br>
       "If she <strong>had left</strong> earlier, she <strong>would have caught</strong> the bus."
     </div>
   </div>""",
   [("If you ___ water, it boils. (heat)", ["heat","heated","will heat","would heat"], 0),
    ("If it rains, I ___ home.", ["will stay","stay","stayed","would stay"], 0),
    ("If I ___ a million dollars, I would travel.", ["had","have","would have","had had"], 0),
    ("If I were you, I ___ the job.", ["would accept","accept","will accept","accepted"], 0),
    ("If I ___ studied, I would have passed.", ["had","have","would","could"], 0),
    ("If you ___ hard, you will pass.", ["study","studied","will study","would study"], 0),
    ("If she left earlier, she ___ the bus.", ["would have caught","caught","will catch","would catch"], 0),
    ("If water ___ hot, it evaporates.", ["gets","got","will get","would get"], 0),
    ("If I ___ the answer, I would tell you.", ["knew","know","had known","would know"], 0),
    ("If he ___ here, he would help us.", ["were","is","was","be"], 0)],
   [("If you ___ water, it boils. (heat → ?)", "heat"),
    ("If it rains, I ___ home. (stay → ?)", "will stay"),
    ("If I ___ a million dollars... (have → ?)", "had"),
    ("If I were you, I ___ the job. (accept → ?)", "would accept"),
    ("If I ___ studied, I would have passed. (study → ?)", "had"),
    ("If you ___ hard, you will pass. (study → ?)", "study"),
    ("If she left earlier, she ___ the bus. (catch → ?)", "would have caught"),
    ("If I ___ the answer, I would tell you. (know → ?)", "knew")],
   ["If you heat water, it boils.",
    "If it rains, I will stay home.",
    "If I had a million dollars, I would travel.",
    "If I were you, I would accept the job.",
    "If I had studied, I would have passed.",
    "If you study hard, you will pass.",
    "If she left earlier, she would have caught the bus.",
    "If I knew the answer, I would tell you."],
   [("heats","action"),("will stay","state"),("had a million","state"),("would accept","action"),
    ("had studied","action"),("study hard","action"),("would have caught","action"),("knew","state")]),

  (18, "Conditionals 2", "Mixed · Wishes · Regrets · Inversions",
   """<div class="sect">
     <div class="sect-title">📖 Mixed Conditionals</div>
     <div class="rule-box">
       <strong>Past condition → Present result:</strong><br>
       "If I <strong>had studied</strong> medicine, I <strong>would be</strong> a doctor."<br>
       (studied in the past → now a doctor = unreal present)<br>
       <strong>Present condition → Past result:</strong><br>
       "If I <strong>were</strong> richer, I <strong>would have traveled</strong>."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Wishes</div>
     <div class="rule-box">
       <strong>Wish + Past Simple:</strong> present/future wish<br>
       "I <strong>wish I had</strong> more time." (I don't have time now)<br>
       "I <strong>wish I knew</strong> French." (I don't know French)<br>
       <strong>Wish + Past Perfect:</strong> past wish<br>
       "I <strong>wish I had studied</strong> harder." (I didn't study hard — regret)
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Inversion (Formal Conditionals)</div>
     <div class="rule-box">
       <strong>Formal:</strong> Had I known, I would have helped.<br>
       <strong>Formal:</strong> Should you need help, call me.<br>
       <strong>Formal:</strong> Were I you, I would accept.
     </div>
   </div>""",
   [("I wish I ___ more time.", ["had","have","would have","had had"], 0),
    ("If I had studied medicine, I ___ a doctor now.", ["would be","am","was","will be"], 0),
    ("I wish I ___ harder when I was in school.", ["had studied","studied","would have studied","study"], 0),
    ("___ I known, I would have helped.", ["Had","If","When","Would"], 0),
    ("If I were richer, I ___ traveled.", ["would have","would","will","could"], 0),
    ("I wish she ___ here now.", ["were","is","was","has been"], 0),
    ("Should you need help, ___ me.", ["call","called","calls","calling"], 0),
    ("I wish I ___ the opportunity.", ["had missed","missed","would have missed","miss"], 0),
    ("Had I seen her, I ___ her.", ["would have told","told","would tell","tell"], 0),
    ("If I ___ the job, I would be happy.", ["got","get","had gotten","will get"], 0)],
   [("I wish I ___ more time. (have → ?)", "had"),
    ("If I had studied medicine, I ___ a doctor now. (be → ?)", "would be"),
    ("I wish I ___ harder. (study → past)", "had studied"),
    ("___ I known... (formal start)", "Had"),
    ("If I were richer, I ___ traveled. (would/will)", "would have"),
    ("I wish she ___ here now. (is → ?)", "were"),
    ("Should you need help, ___ me. (call)", "call"),
    ("I wish I ___ the opportunity. (miss → past)", "had missed")],
   ["I wish I had more time.",
    "If I had studied medicine, I would be a doctor now.",
    "I wish I had studied harder when I was in school.",
    "Had I known, I would have helped.",
    "If I were richer, I would have traveled.",
    "I wish she were here now.",
    "Should you need help, call me.",
    "I wish I had missed the opportunity."],
   [("had more time","state"),("would be a doctor","state"),("had studied harder","action"),("had known","action"),
    ("would have traveled","state"),("were here","state"),("call me","action"),("had missed","action")]),

  (19, "Prepositions", "Time · Place · Phrasal verbs · Collocations",
   """<div class="sect">
     <div class="sect-title">📖 Prepositions of Time</div>
     <div class="rule-box">
       <strong>AT:</strong> specific time · "at 3 PM" · "at midnight" · "at night"<br>
       <strong>ON:</strong> days, dates · "on Monday" · "on 5th March" · "on my birthday"<br>
       <strong>IN:</strong> months, years, long periods · "in January" · "in 2024" · "in the morning"
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Prepositions of Place</div>
     <div class="rule-box">
       <strong>AT:</strong> point/location · "at school" · "at home" · "at the bus stop"<br>
       <strong>IN:</strong> enclosed space · "in the room" · "in Manila" · "in the box"<br>
       <strong>ON:</strong> surface · "on the table" · "on the wall" · "on the map"
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Phrasal Verbs & Collocations</div>
     <div class="rule-box">
       <strong>Verb + preposition:</strong> depend ON · believe IN · listen TO<br>
       <strong>Verb + adverb:</strong> give UP · look AFTER · turn OFF<br>
       <strong>Collocation:</strong> make an effort · do research · take a break
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Key:</strong> Prepositions cannot be changed — they are fixed! "depend ON" not "depend IN"</span></div>
   </div>""",
   [("I will see you ___ Monday.", ["on","in","at","by"], 0),
    ("She was born ___ 1995.", ["in","on","at","by"], 0),
    ("I always wake up ___ 6 AM.", ["at","in","on","by"], 0),
    ("The book is ___ the table.", ["on","in","at","by"], 0),
    ("She lives ___ Manila.", ["in","on","at","by"], 0),
    ("We depend ___ the weather for our plans.", ["on","in","at","by"], 0),
    ("He gave ___ smoking last year.", ["up","in","on","off"], 0),
    ("We arrived ___ the airport on time.", ["at","in","on","by"], 0),
    ("I always look ___ my younger brother.", ["after","on","in","at"], 0),
    ("She is good ___ languages.", ["at","in","on","by"], 0)],
   [("I will see you ___ Monday. (day)", "on"),
    ("She was born ___ 1995. (year)", "in"),
    ("I always wake up ___ 6 AM. (time)", "at"),
    ("The book is ___ the table. (surface)", "on"),
    ("She lives ___ Manila. (city)", "in"),
    ("We depend ___ the weather. (preposition)", "on"),
    ("He gave ___ smoking last year. (phrasal)", "up"),
    ("We arrived ___ the airport. (location)", "at")],
   ["I will see you on Monday.",
    "She was born in 1995.",
    "I always wake up at 6 AM.",
    "The book is on the table.",
    "She lives in Manila.",
    "We depend on the weather for our plans.",
    "He gave up smoking last year.",
    "We arrived at the airport on time."],
   [("on Monday","state"),("in 1995","state"),("at 6 AM","state"),("on the table","state"),
    ("in Manila","state"),("depend on","action"),("gave up","action"),("at the airport","state")]),

  (20, "Relative Clauses", "Defining · Non-defining · Relative adverbs",
   """<div class="sect">
     <div class="sect-title">📖 Defining Relative Clauses (No commas)</div>
     <div class="rule-box">
       <strong>WHO/WHOM:</strong> people<br>
       "The teacher <strong>who</strong> taught me is kind."<br>
       <strong>WHICH/THAT:</strong> things<br>
       "The book <strong>which</strong> I read was interesting."<br>
       <strong>WHOSE:</strong> possession<br>
       "The student <strong>whose</strong> book was lost came late."
     </div>
     <div class="usecase">
       <strong>That vs Which:</strong><br>
       "The book <strong>that</strong> I bought" (defining — no comma)<br>
       "<strong>Which</strong>, I think, is the best option." (non-defining — with comma)
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Non-Defining Relative Clauses (With commas)</div>
     <div class="rule-box">
       <strong>Use commas:</strong> extra information, can be removed<br>
       "Mrs. Cruz, <strong>who teaches</strong> English, is very kind."<br>
       "Manila, <strong>which is</strong> the capital, is a beautiful city."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Relative Adverbs (When / Where / Why)</div>
     <div class="rule-box">
       <strong>WHEN:</strong> time · "the day <strong>when</strong> I met her"<br>
       <strong>WHERE:</strong> place · "the place <strong>where</strong> I studied"<br>
       <strong>WHY:</strong> reason · "the reason <strong>why</strong> I came"
     </div>
   </div>""",
   [("The teacher ___ taught me is kind.", ["who","which","that","whose"], 0),
    ("The book ___ I read was interesting.", ["which","who","that","whom"], 0),
    ("The student ___ book was lost came late.", ["whose","who","which","that"], 0),
    ("Mrs. Cruz, ___ teaches English, is kind.", ["who","which","that","whom"], 0),
    ("Manila, ___ is the capital, is beautiful.", ["which","who","that","where"], 0),
    ("The day ___ I met her was special.", ["when","where","why","which"], 0),
    ("The place ___ I studied was quiet.", ["where","when","which","who"], 0),
    ("The reason ___ I came was to help.", ["why","when","where","which"], 0),
    ("The person ___ I spoke to was helpful.", ["whom","who","which","that"], 0),
    ("The car ___ was parked here is mine.", ["that","which","who","whose"], 0)],
   [("The teacher ___ taught me is kind. (people)", "who"),
    ("The book ___ I read was interesting. (things)", "which"),
    ("The student ___ book was lost came late. (possession)", "whose"),
    ("Mrs. Cruz, ___ teaches English, is kind. (extra info)", "who"),
    ("Manila, ___ is the capital, is beautiful. (extra info)", "which"),
    ("The day ___ I met her was special. (time)", "when"),
    ("The place ___ I studied was quiet. (place)", "where"),
    ("The reason ___ I came was to help. (reason)", "why")],
   ["The teacher who taught me is kind.",
    "The book which I read was interesting.",
    "The student whose book was lost came late.",
    "Mrs. Cruz, who teaches English, is kind.",
    "Manila, which is the capital, is beautiful.",
    "The day when I met her was special.",
    "The place where I studied was quiet.",
    "The reason why I came was to help."],
   [("who taught me","action"),("which I read","state"),("whose book was lost","action"),("who teaches","action"),
    ("which is the capital","state"),("when I met her","action"),("where I studied","state"),("why I came","state")]),

  (21, "Ways of Organising Texts", "Subject Choice · Introductory IT · Information Flow",
   """<div class="sect">
     <div class="sect-title">📖 Subject Choice in Academic Writing</div>
     <div class="rule-box">
       <strong>First person:</strong> "I believe..." · less formal<br>
       <strong>Third person:</strong> "Research shows..." · more formal<br>
       <strong>Impersonal:</strong> "It can be seen..." · most formal<br>
       "It is argued that..." · "This essay will examine..."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Introductory IT (Impersonal 'It')</div>
     <div class="rule-box">
       <strong>It + passive verb:</strong> formal academic style<br>
       "It <strong>is believed</strong> that..." · "It <strong>can be argued</strong>..."<br>
       "It <strong>should be noted</strong> that..." · "It <strong>is generally accepted</strong> that..."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Information Flow & Paragraphing</div>
     <div class="rule-box">
       <strong>Topic sentence:</strong> main idea of paragraph<br>
       <strong>Supporting:</strong> examples, data, explanation<br>
       <strong>Concluding:</strong> link back to main point<br>
       <strong>Transitional:</strong> link to next paragraph
     </div>
   </div>""",
   [("___ is believed that exercise improves health.", ["It","This","That","He"], 0),
    ("Research ___ that smoking causes cancer.", ["shows","say","state","claim"], 0),
    ("___ essay will examine the effects of social media.", ["This","It","That","Those"], 0),
    ("___ is argued that technology has changed education.", ["It","This","That","Those"], 0),
    ("The topic sentence should contain the ___ idea.", ["main","minor","supporting","concluding"], 0),
    ("It should be ___ that climate affects agriculture.", ["noted","argued","believed","known"], 0),
    ("The paragraph should end with a ___ sentence.", ["concluding","topic","supporting","transitional"], 0),
    ("This study ___ the relationship between poverty and education.", ["examines","examine","examining","examined"], 0),
    ("It is generally ___ that students learn better with visuals.", ["accepted","argued","stated","believed"], 0),
    ("The first sentence of a paragraph is the ___ sentence.", ["topic","supporting","concluding","transitional"], 0)],
   [("___ is believed that... (impersonal)", "It"),
    ("Research ___ that... (shows/say)", "shows"),
    ("___ essay will examine... (This/It)", "This"),
    ("It is ___ that climate affects agriculture. (noted/argued)", "noted"),
    ("The topic sentence should contain the ___ idea. (main/minor)", "main"),
    ("The paragraph should end with a ___ sentence. (concluding/supporting)", "concluding"),
    ("This study ___ the relationship... (examines/examine)", "examines"),
    ("It is generally ___ that... (accepted/argued)", "accepted")],
   ["It is believed that exercise improves health.",
    "Research shows that smoking causes cancer.",
    "This essay will examine the effects of social media.",
    "It is argued that technology has changed education.",
    "The topic sentence should contain the main idea.",
    "It should be noted that climate affects agriculture.",
    "The paragraph should end with a concluding sentence.",
    "The first sentence of a paragraph is the topic sentence."],
   [("is believed","state"),("shows that","action"),("will examine","action"),("is argued","state"),
    ("main idea","state"),("should be noted","action"),("concluding sentence","action"),("topic sentence","state")]),

  (22, "The Passive Voice", "All passive forms · FARO mnemonic · Agent removal",
   """<div class="sect">
     <div class="sect-title">📖 Passive Forms — FARO Mnemonic</div>
     <div class="rule-box">
       <strong>F</strong> (Future): will + be + past participle<br>
       "The project <strong>will be completed</strong> next month."<br>
       <strong>A</strong> (Present Perfect): has/have + been + past participle<br>
       "The work <strong>has been finished</strong>."<br>
       <strong>R</strong> (Past): was/were + past participle<br>
       "The letter <strong>was sent</strong> yesterday."<br>
       <strong>O</strong> (Present): is/am/are + past participle<br>
       "The lesson <strong>is taught</strong> by Mrs. Cruz."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Agent Removal</div>
     <div class="rule-box">
       <strong>by + agent:</strong> optional · "The lesson was taught <strong>by Mrs. Cruz</strong>."<br>
       <strong>With:</strong> tool/material · "The cake was made <strong>with chocolate</strong>."<br>
       <strong>Usually remove agent:</strong> when unknown, obvious, or unimportant
     </div>
   </div>""",
   [("The project ___ completed next month.", ["will be","is","was","has been"], 0),
    ("The work ___ finished yesterday.", ["was","is","will be","has been"], 0),
    ("The lesson ___ taught by Mrs. Cruz.", ["is","was","will be","has been"], 0),
    ("The letter ___ sent last week.", ["was","is","will be","has been"], 0),
    ("The homework ___ been submitted.", ["has","is","was","will"], 0),
    ("The building ___ being renovated.", ["is","was","will be","has"], 0),
    ("The exam ___ will be taken tomorrow.", ["will","has","is","was"], 0),
    ("The food ___ was prepared by the chef.", ["was","is","will be","has been"], 0),
    ("The letter ___ sent yet?", ["has been","was","is","will be"], 0),
    ("The students ___ being taught by the substitute.", ["are","were","is","will be"], 0)],
   [("The project ___ completed next month. (future passive)", "will be"),
    ("The work ___ finished yesterday. (past passive)", "was"),
    ("The lesson ___ taught by Mrs. Cruz. (present passive)", "is"),
    ("The letter ___ sent last week. (past passive)", "was"),
    ("The homework ___ been submitted. (PP passive)", "has"),
    ("The building ___ being renovated. (being done)", "is"),
    ("The food ___ was prepared by the chef. (past passive)", "was"),
    ("The letter ___ sent yet? (PP passive)", "has been")],
   ["The project will be completed next month.",
    "The work was finished yesterday.",
    "The lesson is taught by Mrs. Cruz.",
    "The letter was sent last week.",
    "The homework has been submitted.",
    "The building is being renovated.",
    "The food was prepared by the chef.",
    "The letter has been sent yet?"],
   [("will be completed","action"),("was finished","state"),("is taught","action"),("was sent","state"),
    ("has been submitted","action"),("is being renovated","action"),("was prepared","state"),("has been sent","action")]),

  (23, "Linking Ideas", "CARP: Contrast · Addition · Result · Purpose",
   """<div class="sect">
     <div class="sect-title">📖 Contrast Signals (CARP)</div>
     <div class="rule-box">
       <strong>HOWEVER / NEVERTHELESS:</strong> formal contrast<br>
       "Many students passed. <strong>However</strong>, some failed."<br>
       <strong>ALTHOUGH / EVEN THOUGH / DESPITE:</strong> concession<br>
       "<strong>Although</strong> she studied, she failed."<br>
       "<strong>Despite</strong> studying, she failed."<br>
       <strong>IN CONTRAST / ON THE OTHER HAND:</strong> comparison
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Addition Signals</div>
     <div class="rule-box">
       <strong>FURTHERMORE / MOREOVER:</strong> add stronger point<br>
       "<strong>Furthermore</strong>, the school offers free meals."<br>
       <strong>IN ADDITION / BESIDES / ALSO:</strong> add more<br>
       "<strong>In addition</strong>, there is a library."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Result & Purpose Signals</div>
     <div class="rule-box">
       <strong>THEREFORE / CONSEQUENTLY / AS A RESULT:</strong> result<br>
       "She studied hard. <strong>Therefore</strong>, she passed."<br>
       <strong>TO / IN ORDER TO / SO AS TO:</strong> purpose<br>
       "<strong>In order to</strong> pass, she studied hard."<br>
       <strong>SO THAT:</strong> purpose with subject<br>
       "<strong>So that</strong> she could pass, she studied hard."
     </div>
   </div>""",
   [("She studied hard. ___, she passed.", ["Therefore","Furthermore","Although","However"], 0),
    ("Many students passed. ___, some failed.", ["However","Therefore","Furthermore","Because"], 0),
    ("___ she was tired, she continued working.", ["Although","Therefore","Furthermore","Moreover"], 0),
    ("The school offers free meals. ___, it has a library.", ["Furthermore","However","Although","Despite"], 0),
    ("She studied hard ___ she could pass.", ["so that","because","although","however"], 0),
    ("___ studying, she failed the exam.", ["Despite","Although","However","Therefore"], 0),
    ("It rained heavily. ___, the event was cancelled.", ["Consequently","Although","Furthermore","Moreover"], 0),
    ("In order to ___, she woke up early.", ["succeed","success","successful","succeeding"], 0),
    ("She was sick. ___, she went to school.", ["Nevertheless","Therefore","Furthermore","Moreover"], 0),
    ("The lesson is difficult. ___, it is very useful.", ["Nevertheless","Because","Therefore","In addition"], 0)],
   [("She studied hard. ___, she passed. (result)", "Therefore"),
    ("Many students passed. ___, some failed. (contrast)", "However"),
    ("___ she was tired, she continued. (concession)", "Although"),
    ("The school offers free meals. ___, it has a library. (add)", "Furthermore"),
    ("She studied hard ___ she could pass. (purpose)", "so that"),
    ("___ studying, she failed. (despite/although)", "Despite"),
    ("It rained heavily. ___, the event was cancelled. (result)", "Consequently"),
    ("In order to ___, she woke up early. (purpose verb)", "succeed")],
   ["She studied hard. Therefore, she passed.",
    "Many students passed. However, some failed.",
    "Although she was tired, she continued working.",
    "The school offers free meals. Furthermore, it has a library.",
    "She studied hard so that she could pass.",
    "Despite studying, she failed the exam.",
    "It rained heavily. Consequently, the event was cancelled.",
    "In order to succeed, she woke up early."],
   [("studied hard","action"),("passed","state"),("was tired","state"),("continued working","action"),
    ("offers free meals","state"),("studied hard","action"),("failed","action"),("rained heavily","action")]),

  (24, "Showing Your Position", "Opinion phrases · Hedging · Academic stance",
   """<div class="sect">
     <div class="sect-title">📖 Opinion Phrases</div>
     <div class="rule-box">
       <strong>Strong:</strong> "I firmly believe..." · "It is clear that..."<br>
       <strong>Neutral:</strong> "I believe..." · "In my view..." · "From my perspective..."<br>
       <strong>Cautious:</strong> "It seems that..." · "It appears that..." · "I would argue that..."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Hedging (Academic Caution)</div>
     <div class="rule-box">
       <strong>Modal verbs:</strong> may, might, could, would<br>
       "This <strong>could</strong> be the best solution."<br>
       <strong>Qualifying adjectives:</strong> likely, probable, possible<br>
       "It is <strong>likely</strong> that students will benefit."<br>
       <strong>Verb patterns:</strong> tend to, seem to, appear to<br>
       "Students <strong>tend to</strong> perform better with visuals."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Academic Stance</div>
     <div class="rule-box">
       <strong>Avoid:</strong> I think, I believe, very, definitely<br>
       <strong>Use:</strong> This essay argues, It could be argued, The evidence suggests<br>
       "The evidence <strong>suggests that</strong> technology improves learning."
     </div>
   </div>""",
   [("I firmly ___ that education is important.", ["believe","think","am sure","know"], 0),
    ("It ___ that climate affects agriculture.", ["seems","is","looks","appears strongly"], 0),
    ("The evidence ___ that technology helps learning.", ["suggests","shows","proves","is"], 0),
    ("This ___ be the best solution.", ["could","is","must","will"], 0),
    ("Students ___ to perform better with visuals.", ["tend","want","like","need"], 0),
    ("It is ___ that she will succeed.", ["likely","sure","certain","obvious"], 0),
    ("In my ___, this approach is effective.", ["view","opinion","idea","mind"], 0),
    ("I would ___ that this is the correct method.", ["argue","say","think","believe"], 0),
    ("It ___ that the results are reliable.", ["appears","seems strong","is likely","looks"], 0),
    ("I strongly ___ that we should act now.", ["believe","think","am sure","know"], 0)],
   [("I firmly ___ that education is important. (believe/think)", "believe"),
    ("It ___ that climate affects agriculture. (seems/looks)", "seems"),
    ("The evidence ___ that technology helps. (suggests/shows)", "suggests"),
    ("This ___ be the best solution. (could/is)", "could"),
    ("Students ___ to perform better with visuals. (tend/want)", "tend"),
    ("It is ___ that she will succeed. (likely/sure)", "likely"),
    ("In my ___, this approach is effective. (view/opinion)", "view"),
    ("I would ___ that this is the correct method. (argue/say)", "argue")],
   ["I firmly believe that education is important.",
    "It seems that climate affects agriculture.",
    "The evidence suggests that technology helps learning.",
    "This could be the best solution.",
    "Students tend to perform better with visuals.",
    "It is likely that she will succeed.",
    "In my view, this approach is effective.",
    "I would argue that this is the correct method."],
   [("firmly believe","action"),("seems that","state"),("suggests that","action"),("could be","state"),
    ("tend to perform","action"),("is likely","state"),("in my view","state"),("would argue","action")]),

  (25, "Nominalisation", "Verbs to nouns · Nominal compounds · Density",
   """<div class="sect">
     <div class="sect-title">📖 Verbs to Nouns (Nominalisation)</div>
     <div class="rule-box">
       <strong>Purpose:</strong> make writing more formal and concise<br>
       "The government <strong>decided</strong>." → "<strong>The government's decision</strong>."<br>
       "The teacher <strong>explained</strong> the lesson." → "<strong>The teacher's explanation of the lesson.</strong>"
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Key verbs → nouns:</strong><br>
       decide → decision · explain → explanation · examine → examination<br>
       apply → application · permit → permission · conclude → conclusion</span></div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Nominal Compounds</div>
     <div class="rule-box">
       <strong>Adj + Noun:</strong> "environmental pollution"<br>
       <strong>Noun + Noun:</strong> "climate change policy"<br>
       <strong>Noun + verb-ing:</strong> "water pollution control"
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Information Density</div>
     <div class="rule-box">
       <strong>Use:</strong> compress multiple ideas into one noun phrase<br>
       "The <strong>rapid increase in student numbers</strong> caused problems."<br>
       (4 ideas: rapid / increase / student / numbers)
     </div>
   </div>""",
   [("The government's ___ to raise taxes was popular.", ["decision","decide","deciding","decided"], 0),
    ("Her ___ of the lesson was very clear.", ["explanation","explain","explaining","explained"], 0),
    ("The ___ of water is a serious problem.", ["pollution","pollute","polluting","polluted"], 0),
    ("The ___ of the exam will take place next week.", ["examination","examine","examining","examined"], 0),
    ("I made an ___ to study abroad.", ["application","apply","applying","applied"], 0),
    ("The ___ of the policy caused debate.", ["implementation","implement","implementing","implemented"], 0),
    ("The ___ of climate change is a global issue.", ["severity","severe","severely","most severe"], 0),
    ("Environmental ___ is increasing.", ["pollution","polluting","pollute","pollutes"], 0),
    ("The ___ of the rules was strictly enforced.", ["enforcement","enforce","enforcing","enforced"], 0),
    ("His ___ to the project was very valuable.", ["contribution","contribute","contributing","contributed"], 0)],
   [("The government's ___ to raise taxes. (decide → ?)", "decision"),
    ("Her ___ of the lesson was clear. (explain → ?)", "explanation"),
    ("The ___ of water is serious. (pollute → ?)", "pollution"),
    ("The ___ of the exam will take place. (examine → ?)", "examination"),
    ("I made an ___ to study abroad. (apply → ?)", "application"),
    ("The ___ of the policy caused debate. (implement → ?)", "implementation"),
    ("Environmental ___ is increasing. (pollute → noun)", "pollution"),
    ("The ___ of the rules was enforced. (enforce → ?)", "enforcement")],
   ["The government's decision to raise taxes was popular.",
    "Her explanation of the lesson was very clear.",
    "The pollution of water is a serious problem.",
    "The examination of the exam will take place next week.",
    "I made an application to study abroad.",
    "The implementation of the policy caused debate.",
    "Environmental pollution is increasing.",
    "The enforcement of the rules was strictly enforced."],
   [("government's decision","action"),("explanation of the lesson","state"),("pollution of water","state"),("examination","action"),
    ("made an application","action"),("implementation of the policy","action"),("environmental pollution","state"),("enforcement of the rules","action")]),
]

def make_quiz_js(quiz_items):
    items_js = "const QUIZ_DATA=[\n"
    for i, (q, opts, correct) in enumerate(quiz_items):
        opts_str = "[" + ",".join(f'"{o}"' for o in opts) + "]"
        items_js += f'  {{q:"{q}",opts:{opts_str},ans:{correct}}}'
        if i < len(quiz_items) - 1: items_js += ","
        items_js += "\n"
    items_js += "];\n"
    return items_js

def make_fillin_js(fillin_items):
    items_js = "const FILLIN_DATA=[\n"
    for i, (q, ans) in enumerate(fillin_items):
        items_js += f'  {{q:"{q}",ans:0,choices:["{ans}","wrong answer 1","wrong answer 2"]}}'
        if i < len(fillin_items) - 1: items_js += ","
        items_js += "\n"
    items_js += "];\n"
    return items_js

def make_speaking_js(sentences):
    items = ",".join(f'"{s}"' for s in sentences)
    return f"const SPEAK_DATA=[{items}];\n"

def make_match_js(match_items):
    verbs_js = "const VERBS=[\n"
    for i, (verb, cat) in enumerate(match_items):
        verbs_js += f'  {{word:"{verb}",category:"{cat}"}}'
        if i < len(match_items) - 1: verbs_js += ","
        verbs_js += "\n"
    verbs_js += "];\n"
    return verbs_js

def generate_unit(num, title, subtitle, lesson_html, quiz_items, fillin_items, speak_items, match_items):
    with open(os.path.join(BASE, 'grammar-unit-01.html')) as f:
        template = f.read()

    quiz_js = make_quiz_js(quiz_items)
    fillin_js = make_fillin_js(fillin_items)
    speak_js = make_speaking_js(speak_items)
    match_js = make_match_js(match_items)

    prev_num = num - 1 if num > 1 else None
    next_num = num + 1 if num < 25 else None
    prev_link = f'<a href="grammar-unit-{prev_num:02d}.html" class="btn-prev">← Unit {prev_num}</a>' if prev_num else '<span></span>'
    next_link = f'<a href="grammar-unit-{next_num:02d}.html" class="btn-next">Unit {next_num} →</a>' if next_num else '<span></span>'

    # Build unit tabs
    unit_tabs_html = ""
    for u in range(1, 26):
        active = "active" if u == num else ""
        href = f'grammar-unit-{u:02d}.html' if u != num else "#"
        short_names = {1:"Present Tenses",2:"Past Tenses",3:"Present Perfect",4:"Past Tenses 2",5:"Future 1",6:"Future 2",7:"Countable",8:"Nouns",9:"Pronouns",10:"Adjectives",11:"Comparing",12:"Noun Phrase",13:"Modals 1",14:"Modals 2",15:"Reported",16:"Verb Patterns",17:"Conditionals 1",18:"Conditionals 2",19:"Prepositions",20:"Relative",21:"Text Org.",22:"Passive",23:"Linking",24:"Position",25:"Nominalisation"}
        name = short_names.get(u, "...")
        unit_tabs_html += f'<a href="{href}" class="utab {active}"><span class="un">{u}</span><span style="font-size:0.72rem;color:var(--muted)">{name}</span></a>\n'

    html = template
    html = html.replace("Unit 1: Present Tenses — Grammar Mastery Academy", f"Unit {num}: {title} — Grammar Mastery Academy")
    html = html.replace("Unit 1 — Present Tenses", f"Unit {num} — {title}")
    html = html.replace("Present Simple · Continuous · State Verbs", subtitle)

    # Replace lesson content
    start = html.find('<div class="sect"')
    end = html.find('<div class="nav-btns"')
    if start != -1 and end != -1:
        html = html[:start] + lesson_html + '\n<div class="nav-btns">' + html[end + len('<div class="nav-btns">'):]

    # Replace nav buttons
    html = re.sub(r'<a href="grammar-hub.html" class="btn-prev">← Hub</a>', '<a href="grammar-hub.html" class="btn-prev">← Hub</a>', html)

    # Replace JS data
    html = re.sub(r'const QUIZ_DATA=\[.*?\];', quiz_js, html, flags=re.DOTALL)
    html = re.sub(r'const FILLIN_DATA=\[.*?\];', fillin_js, html, flags=re.DOTALL)
    html = re.sub(r'const SPEAK_DATA=\[.*?\];', speak_js, html, flags=re.DOTALL)
    html = re.sub(r'const VERBS=\[.*?\];', match_js, html, flags=re.DOTALL)

    # Update unit tabs
    html = re.sub(r'<div class="unit-tabs">.*?</div>', f'<div class="unit-tabs">{unit_tabs_html}</div>', html, flags=re.DOTALL)

    return html

def main():
    for unit in UNITS_12_25:
        num, title, subtitle, lesson_html, quiz_items, fillin_items, speak_items, match_items = unit
        print(f"Generating Unit {num}: {title}...")
        html = generate_unit(num, title, subtitle, lesson_html, quiz_items, fillin_items, speak_items, match_items)
        fname = f'grammar-unit-{num:02d}.html'
        fpath = os.path.join(BASE, fname)
        with open(fpath, 'w') as f:
            f.write(html)
        print(f"  Wrote: {fname} ({len(html)} bytes)")
    print("Done! 14 units (12-25) generated.")

if __name__ == '__main__':
    main()