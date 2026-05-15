#!/usr/bin/env python3
"""Generate Grammar Units 2-25 from template."""

import os

BASE = '/home/jermu/workspace/eusa-sandbox'
TEMPLATE_PATH = os.path.join(BASE, 'grammar-unit-01.html')

with open(TEMPLATE_PATH) as f:
    TEMPLATE = f.read()

# Unit definitions: (number, title, subtitle, lesson_html, quiz items, fillin items, speaking items, match items)
UNITS = [
  (2, "Past Tenses", "Past Simple · Continuous · Perfect",
   """<div class="sect">
     <div class="sect-title">📖 Past Simple</div>
     <div class="rule-box">
       <strong>Form:</strong> subject + <em>verb-ed</em> (regular) OR <em>irregular past verb</em><br>
       <strong>Negatives:</strong> subject + did + not + base verb<br>
       <strong>Questions:</strong> Did + subject + base verb?
     </div>
     <div class="usecase">
       <strong>Use Past Simple for:</strong> completed actions in the past · habits in the past · sequences of completed events<br>
       "I <strong>studied</strong> English for five years." · "She <strong>moved</strong> to Manila in 2010."
     </div>
     <div class="usecase blue">
       <strong>Signal words:</strong> yesterday · last week · in 2015 · ago · when · then · first · after that
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Key:</strong> Past Simple always answers "When?" — the exact time the action finished.</span></div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Past Continuous</div>
     <div class="rule-box">
       <strong>Form:</strong> subject + was/were + <em>verb-ing</em><br>
       <strong>Negatives:</strong> subject + was/were + not + verb-ing
     </div>
     <div class="usecase">
       <strong>Use Past Continuous for:</strong> actions in progress at a specific past moment · longer background action interrupted by a short action<br>
       "I <strong>was reading</strong> when the phone <strong>rang</strong>."
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Pattern:</strong> "While + Past Continuous, Past Simple interrupt." · "Past Simple, while + Past Continuous."</span></div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Past Perfect</div>
     <div class="rule-box">
       <strong>Form:</strong> subject + had + <em>past participle</em><br>
       <strong>Negatives:</strong> subject + had + not + past participle<br>
       <strong>Use:</strong> action BEFORE another past action · "by the time" · "already" · "just"
     </div>
     <div class="usecase">
       <strong>Use Past Perfect for:</strong> showing which action happened first<br>
       "She <strong>had left</strong> before I <strong>arrived</strong>." · "By the time I finished, they <strong>had gone</strong>."
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Formula:</strong> Past Perfect = "HAD + DONE" · It happened BEFORE the other past event.</span></div>
     <div class="memory-anchor">
       <div class="anchor-title">🎯 Memory Anchor</div>
       <div class="anchor-letters">
         <div class="anchor-letter"><div class="letter">P</div><div class="key">Past</div><div class="meaning">yesterday</div></div>
         <div class="anchor-letter"><div class="letter">C</div><div class="key">Continuous</div><div class="meaning">was -ing</div></div>
         <div class="anchor-letter"><div class="letter">PP</div><div class="key">Past Perfect</div><div class="meaning">had done</div></div>
       </div>
     </div>
   </div>""",
   [("I ___ English when she called.", ["studied","am studying","study","will study"], 0),
    ("She ___ to London last year.", ["moved","was moving","has moved","is moving"], 0),
    ("They ___ TV when I arrived.", ["were watching","watched","are watching","watch"], 0),
    ("He ___ already ___ before the class started.", ["had / left","has / left","was / left","left"], 0),
    ("We ___ to the school every day as children.", ["walked","were walking","had walked","are walking"], 0),
    ("I ___ a book when the lights went out.", ["was reading","read","am reading","reads"], 0),
    ("She ___ her keys before she left home.", ["had lost","lost","has lost","was losing"], 0),
    ("They ___ the lesson when I entered.", ["were having","had","have","has"], 0),
    ("He ___ a teacher before becoming a principal.", ["was","had been","is","has been"], 0),
    ("By the time I ___ the movie, it ___ already ___ on TV.", ["arrived / had / started","arrive / has / started","arrived / was / starting","arrive / is / started"], 0)],
   [("She ___ to Manila in 2015. (moves/moved)", "moved"),
    ("I ___ English for 3 years. (study/studied)", "studied"),
    ("They ___ TV when I called. (watch/were watching)", "were watching"),
    ("He ___ already ___ before I came. (leaves/had left)", "had left"),
    ("We ___ to school every day as kids. (walk/walked)", "walked"),
    ("She ___ a letter when the phone rang. (writes/was writing)", "was writing"),
    ("By the time I arrived, they ___ the work. (finish/had finished)", "had finished"),
    ("He ___ a teacher for 10 years. (is/was)", "was")],
   ["I lived in Manila for five years.",
    "She was studying when the phone rang.",
    "They had left before I arrived.",
    "We walked to school every day.",
    "He was teaching English when I met him.",
    "By the time she arrived, I had finished.",
    "They were watching TV when the power went out.",
    "She moved to Cebu in 2018."],
   [("lived","action"),("was studying","state"),("had left","action"),("walked","action"),
    ("was teaching","state"),("had finished","action"),("were watching","action"),("moved","action")]),

  (3, "Present Perfect", "For/Since · Just · Already · Yet",
   """<div class="sect">
     <div class="sect-title">📖 Present Perfect — Key Concept</div>
     <div class="rule-box">
       <strong>Form:</strong> subject + have/has + <em>past participle</em><br>
       <strong>Use:</strong> past actions connected to NOW · experience · change · unfinished time
     </div>
     <div class="usecase">
       <strong>Use Present Perfect when:</strong><br>
       ✓ Experience: "I <strong>have visited</strong> Japan."<br>
       ✓ Change: "She <strong>has become</strong> a teacher."<br>
       ✓ Unfinished time: "I <strong>have studied</strong> today."<br>
       ✓ Result: "I <strong>have lost</strong> my keys." (now keyless)
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 For & Since</div>
     <div class="rule-box">
       <strong>FOR</strong> = duration · "for two hours" · "for a long time" · "for years"<br>
       <strong>SINCE</strong> = start point · "since 2015" · "since Monday" · "since I was a child"
     </div>
     <div class="usecase">
       <strong>I ___ here for three hours.</strong> (am waiting) → "have been waiting"<br>
       <strong>She ___ here since morning.</strong> (is waiting) → "has been waiting"
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Tip:</strong> For/Since = Present Perfect OR Present Perfect Continuous. "I have been waiting" = same meaning as "I have waited."</span></div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Just · Already · Yet</div>
     <div class="usecase">
       <strong>JUST</strong> = recently (positive) · "I have just finished."<br>
       <strong>ALREADY</strong> = earlier than expected (positive) · "I have already eaten."<br>
       <strong>YET</strong> = until now (negative/question) · "I haven't eaten yet." · "Have you finished yet?"
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Position:</strong> Just/Already = before past participle · Yet = at end of sentence.</span></div>
     <div class="memory-anchor">
       <div class="anchor-title">🎯 Memory Anchor</div>
       <div class="anchor-letters">
         <div class="anchor-letter"><div class="letter">H</div><div class="key">Have</div><div class="meaning">I/You/We/They</div></div>
         <div class="anchor-letter"><div class="letter">S</div><div class="key">Has</div><div class="meaning">He/She/It</div></div>
         <div class="anchor-letter"><div class="letter">PP</div><div class="key">Past Participle</div><div class="meaning">done/been/gone</div></div>
       </div>
     </div>
   </div>""",
   [("She ___ to Japan twice.", ["has been","was","is","has been"], 0),
    ("I ___ here since 9 AM.", ["have been waiting","am waiting","was waiting","had waited"], 0),
    ("He has ___ finished his homework.", ["already","yet","just","still"], 0),
    ("___ you ___ your keys?", ["Have / lost","Has / lost","Did / lost","Do / lose"], 0),
    ("I haven't called him ___.", ["yet","already","just","ever"], 0),
    ("They have ___ arrived.", ["just","yet","already","still"], 0),
    ("She has ___ here for two hours.", ["been waiting","waited","waiting","waits"], 0),
    ("By the time he arrived, she ___ already ___", ["had / left","has / left","was / leaving","did / leave"], 0),
    ("We have ___ this question before.", ["discussed","discuss","were discussing","are discussing"], 0),
    ("I ___ my bike since I was ten.", ["have owned","owned","own","am owning"], 0)],
   [("She ___ to Japan. (go/has been)", "has been"),
    ("I ___ here since morning. (am waiting/have been waiting)", "have been waiting"),
    ("He ___ already ___. (has/already finished)", "already finished"),
    ("___ you ___ your homework? (Did/done or Have/done)", "Have done"),
    ("I haven't called him ___. (yet/already)", "yet"),
    ("They have ___ arrived. (just/yet)", "just"),
    ("She ___ here for two hours. (waits/has been waiting)", "has been waiting"),
    ("We have ___ the question before. (discuss/discussed)", "discussed")],
   ["I have been to Japan twice.",
    "She has already finished her work.",
    "I haven't eaten lunch yet.",
    "We have known each other for years.",
    "They have just arrived at the school.",
    "She has been waiting since 9 AM.",
    "Have you ever visited Europe?",
    "I have already seen that movie."],
   [("have been","action"),("has been waiting","state"),("already finished","action"),("haven't eaten","state"),
    ("have just arrived","action"),("has been","action"),("have known","state"),("have seen","action")]),

  (4, "Past Tenses 2", "Past Perfect · Past Simple vs Past Perfect",
   """<div class="sect">
     <div class="sect-title">📖 Past Perfect — Deep Dive</div>
     <div class="rule-box">
       <strong>Purpose:</strong> Shows ANOTHER action happened BEFORE a past reference point<br>
       <strong>Formula:</strong> HAD + PAST PARTICIPLE<br>
       <strong>Signal words:</strong> before · after · by the time · already · just · never
     </div>
     <div class="usecase">
       "By the time I <strong>arrived</strong>, she <strong>had left</strong>."<br>
       (arrived = past reference point; had left = BEFORE)
     </div>
     <div class="usecase blue">
       <strong>Past Simple = both actions in the past:</strong><br>
       "She <strong>left</strong> before I <strong>arrived</strong>." (both finished, order is clear)<br>
       <strong>Past Perfect = earlier action:</strong><br>
       "She <strong>had left</strong> when I <strong>arrived</strong>." (left = BEFORE arrived)
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Past Simple vs Past Perfect</div>
     <div class="rule-box">
       <strong>Past Simple:</strong> both actions are completed; time is clear<br>
       <strong>Past Perfect:</strong> one action clearly BEFORE the other
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Rule:</strong> Use Past Perfect when the ORDER is not clear from time expressions. If "before" / "after" / "by the time" is used, Past Simple is often enough. Past Perfect adds emphasis on the earlier action.</span></div>
   </div>""",
   [("By the time I arrived, she ___.", ["had already left","left","has left","was leaving"], 0),
    ("He ___ the movie before I came.", ["had seen","saw","has seen","was seeing"], 0),
    ("She ___ her homework before the class started.", ["had finished","finished","has finished","was finishing"], 0),
    ("They ___ to the restaurant when we arrived.", ["had gone","went","have gone","were going"], 0),
    ("I ___ him before he became a teacher.", ["had met","met","have met","was meeting"], 0),
    ("By the time the teacher arrived, the students ___.", ["had started","started","are starting","start"], 0),
    ("She realized she ___ her wallet.", ["had forgotten","forgot","has forgotten","forgets"], 0),
    ("They were tired because they ___ all day.", ["had worked","worked","were working","work"], 0),
    ("He was sad because he ___ the game.", ["had lost","lost","has lost","was losing"], 0),
    ("I ___ her before at the conference.", ["had met","met","have met","was meeting"], 0)],
   [("By the time I arrived, she ___. (left/had left)", "had left"),
    ("He ___ the movie before I came. (saw/had seen)", "had seen"),
    ("She ___ her homework before class. (finished/had finished)", "had finished"),
    ("They ___ to the restaurant when we arrived. (went/had gone)", "had gone"),
    ("I ___ him before he became a teacher. (met/had met)", "had met"),
    ("She realized she ___ her wallet. (forgot/had forgotten)", "had forgotten"),
    ("They were tired because they ___ all day. (worked/had worked)", "had worked"),
    ("He was sad because he ___ the game. (lost/had lost)", "had lost")],
   ["By the time I arrived, she had already left.",
    "He had seen the movie before I came.",
    "She had finished her homework before class started.",
    "They had gone to the restaurant when we arrived.",
    "I had met him before he became a teacher.",
    "She realized she had forgotten her wallet.",
    "They were tired because they had worked all day.",
    "I had met her before at a conference."],
   [("had left","action"),("had seen","action"),("had finished","action"),("had gone","action"),
    ("had met","state"),("had forgotten","state"),("had worked","action"),("had lost","action")]),

  (5, "Future Tenses 1", "Will · Going to · Present Continuous",
   """<div class="sect">
     <div class="sect-title">📖 Will vs Going to</div>
     <div class="rule-box">
       <strong>WILL:</strong> spontaneous decision · prediction · promise · hope · threat<br>
       <strong>GOING TO:</strong> planned intention · evidence-based prediction
     </div>
     <div class="usecase">
       <strong>Will:</strong> "I <strong>will help</strong> you." (spontaneous — decided right now)<br>
       <strong>Going to:</strong> "I <strong>am going to help</strong> you." (already planned)
     </div>
     <div class="usecase">
       <strong>Prediction with evidence:</strong><br>
       "Look at those clouds! It <strong>is going to rain</strong>." (evidence visible)<br>
       <strong>Prediction without evidence:</strong><br>
       "I think it <strong>will rain</strong> tomorrow." (personal belief)
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Key:</strong> WILL = decision at the moment · GOING TO = plan made before</span></div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Present Continuous for Future</div>
     <div class="rule-box">
       <strong>Use:</strong> fixed arrangements in near future<br>
       "I <strong>am meeting</strong> her tomorrow at 3 PM."<br>
       "We <strong>are leaving</strong> on Friday."
     </div>
     <div class="memory-anchor">
       <div class="anchor-title">🎯 Memory Anchor</div>
       <div class="anchor-letters">
         <div class="anchor-letter"><div class="letter">W</div><div class="key">Will</div><div class="meaning">instant decision</div></div>
         <div class="anchor-letter"><div class="letter">G</div><div class="key">Going to</div><div class="meaning">planned intention</div></div>
         <div class="anchor-letter"><div class="letter">PC</div><div class="key">Present Cont.</div><div class="meaning">fixed arrangement</div></div>
       </div>
     </div>
   </div>""",
   [("I think it ___ rain tomorrow.", ["will","is going to","am going to","was going to"], 0),
    ("She ___ to the doctor tomorrow. (appointment)", ["is going","will go","goes","went"], 0),
    ("Look at those clouds! It ___ rain.", ["is going to","will","is","was going to"], 0),
    ("I ___ you a gift for your birthday.", ["will buy","am going to buy","buy","am buying"], 0),
    ("We ___ to the beach next weekend.", ["are going","will go","go","goes"], 0),
    ("He ___ the test tomorrow. (prepared)", ["is going to take","will take","takes","took"], 0),
    ("I just decided! I ___ the car now.", ["will wash","am going to wash","wash","am washing"], 0),
    ("They ___ to Manila next month.", ["are going","will travel","travel","travelled"], 0),
    ("The sky is dark. It ___ storm.", ["is going to","will","is","was going to"], 0),
    ("I ___ with you. I'll help! (spontaneous)", ["will come","am going to come","come","am coming"], 0)],
   [("I think it ___ rain tomorrow. (will/is going to)", "will"),
    ("She ___ to the doctor tomorrow. (is going/will go)", "is going"),
    ("Look at those clouds! It ___ rain. (will/is going to)", "is going to"),
    ("I ___ you a gift. (will buy/am going to buy)", "am going to buy"),
    ("We ___ to the beach next weekend. (go/are going)", "are going"),
    ("He ___ the test tomorrow. (is going to take/will take)", "is going to take"),
    ("I just decided! I ___ the car. (will wash/am going to wash)", "will wash"),
    ("They ___ to Manila next month. (travel/are going)", "are going")],
   ["I will help you with that.",
    "She is going to the doctor tomorrow.",
    "Look at those clouds! It is going to rain.",
    "We are leaving on Friday.",
    "I will buy you a gift.",
    "They are meeting us at the restaurant.",
    "I am going to study English tonight.",
    "He will call you later."],
   [("will help","action"),("is going to","state"),("is going to rain","action"),("will buy","action"),
    ("are leaving","state"),("will call","action"),("am going to study","state"),("will buy","action")]),

  (6, "Future Tenses 2", "Future Perfect · Future Continuous · Predictions",
   """<div class="sect">
     <div class="sect-title">📖 Future Perfect</div>
     <div class="rule-box">
       <strong>Form:</strong> will + have + past participle<br>
       <strong>Use:</strong> action that will be COMPLETED before a future point<br>
       "I <strong>will have finished</strong> by Friday."<br>
       "By the time you arrive, I <strong>will have left</strong>."
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Formula:</strong> WILL HAVE DONE · Completed BEFORE a future time.</span></div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Future Continuous</div>
     <div class="rule-box">
       <strong>Form:</strong> will + be + verb-ing<br>
       <strong>Use:</strong> action IN PROGRESS at a future time<br>
       "I <strong>will be working</strong> at 3 PM tomorrow."<br>
       "This time next week, I <strong>will be lying</strong> on the beach."
     </div>
     <div class="memory-anchor">
       <div class="anchor-title">🎯 Memory Anchor</div>
       <div class="anchor-letters">
         <div class="anchor-letter"><div class="letter">FP</div><div class="key">Future Perfect</div><div class="meaning">will have done</div></div>
         <div class="anchor-letter"><div class="letter">FC</div><div class="key">Future Continuous</div><div class="meaning">will be -ing</div></div>
       </div>
     </div>
   </div>""",
   [("I ___ my homework by 9 PM tonight.", ["will have finished","finished","am finishing","will finish"], 0),
    ("This time tomorrow, she ___ in Manila.", ["will be studying","studies","is studying","will study"], 0),
    ("By 2028, he ___ here for 10 years.", ["will have been","was","is","has been"], 0),
    ("They ___ English class at 4 PM.", ["will be having","have","are having","will have"], 0),
    ("By the time you call, I ___ dinner.", ["will have cooked","cook","cooked","am cooking"], 0),
    ("Next month, we ___ in a new school.", ["will be studying","studied","are studying","study"], 0),
    ("He ___ the report by Friday.", ["will have written","writes","wrote","is writing"], 0),
    ("This time next year, I ___ my degree.", ["will have finished","finish","am finishing","will finish"], 0),
    ("By the end of the week, she ___ all her lessons.", ["will have completed","completed","has completed","completes"], 0),
    ("Tomorrow at noon, they ___ lunch.", ["will be eating","eat","eaten","are eating"], 0)],
   [("I ___ my homework by 9 PM tonight. (will finish/will have finished)", "will have finished"),
    ("This time tomorrow, she ___ in Manila. (studies/will be studying)", "will be studying"),
    ("By 2028, he ___ here for 10 years. (was/will have been)", "will have been"),
    ("They ___ English class at 4 PM. (have/will be having)", "will be having"),
    ("By the time you call, I ___ dinner. (cook/will have cooked)", "will have cooked"),
    ("Next month, we ___ in a new school. (study/will be studying)", "will be studying"),
    ("He ___ the report by Friday. (writes/will have written)", "will have written"),
    ("This time next year, I ___ my degree. (finish/will have finished)", "will have finished")],
   ["I will have finished by 9 PM.",
    "This time tomorrow, she will be studying in Manila.",
    "By 2028, he will have been here for 10 years.",
    "They will be having English class at 4 PM.",
    "By the time you call, I will have cooked dinner.",
    "Next month, we will be studying in a new school.",
    "He will have written the report by Friday.",
    "This time next year, I will have finished my degree."],
   [("will have finished","action"),("will be studying","state"),("will have been","state"),("will be having","state"),
    ("will have cooked","action"),("will be studying","state"),("will have written","action"),("will have finished","action")]),

  (7, "Countable & Uncountable", "Much/Many · Some/Any · A few/Little",
   """<div class="sect">
     <div class="sect-title">📖 Countable Nouns</div>
     <div class="rule-box">
       <strong>Countable:</strong> can be counted · has singular & plural<br>
       <strong>1 apple, 2 apples, 3 apples</strong><br>
       <strong>Use:</strong> a/an, numbers, many, few<br>
       <strong>Question:</strong> How many?
     </div>
     <div class="usecase">
       "I have <strong>three apples</strong>." · "She owns <strong>two cars</strong>."<br>
       "<strong>A few</strong> students came late." (= some, but positive)<br>
       "<strong>Few</strong> students came." (= not many, negative feeling)
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Uncountable Nouns</div>
     <div class="rule-box">
       <strong>Uncountable:</strong> cannot be counted · no plural<br>
       <strong>water, rice, information, advice, homework, work</strong><br>
       <strong>Use:</strong> some, much, a little, no number<br>
       <strong>Question:</strong> How much?
     </div>
     <div class="usecase">
       "I have <strong>some water</strong>." · "<strong>Much</strong> time was wasted."<br>
       "<strong>A little</strong> sugar is enough." (= some, positive)<br>
       "<strong>Little</strong> sugar is not enough." (= not much, negative)
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Some / Any / Much / Many / A few / A little</div>
     <div class="rule-box">
       <strong>SOME:</strong> positive sentences, offers, requests (plural or uncountable)<br>
       <strong>ANY:</strong> questions, negatives (plural or uncountable)<br>
       <strong>MUCH:</strong> uncountable in questions/negatives<br>
       <strong>MANY:</strong> countable in questions/negatives<br>
       <strong>A FEW:</strong> countable = some (positive)<br>
       <strong>A LITTLE:</strong> uncountable = some (positive)
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Key:</strong> MUCH/MANY = questions & negatives · SOME = positive · ANY = questions & negatives</span></div>
   </div>""",
   [("How ___ apples do you have?", ["many","much","some","any"], 0),
    ("There is ___ water in the glass.", ["some","any","many","much"], 0),
    ("I don't have ___ money.", ["much","many","some","a few"], 0),
    ("She has ___ friends at school.", ["a few","little","much","any"], 0),
    ("Is there ___ milk left?", ["any","some","much","many"], 0),
    ("There is not ___ time left.", ["much","many","some","a few"], 0),
    ("I need ___ information about the course.", ["some","any","much","many"], 0),
    ("We have ___ ideas for the project.", ["a few","little","much","many"], 0),
    ("How ___ time do we have?", ["much","many","some","a few"], 0),
    ("There are ___ books on the table.", ["a few","little","much","some"], 0)],
   [("How ___ apples do you have? (many/much)", "many"),
    ("There is ___ water in the glass. (some/any)", "some"),
    ("I don't have ___ money. (much/many)", "much"),
    ("She has ___ friends at school. (few/a little)", "a few"),
    ("Is there ___ milk left? (any/some)", "any"),
    ("There is not ___ time left. (much/many)", "much"),
    ("I need ___ information. (some/any)", "some"),
    ("We have ___ ideas for the project. (few/a little)", "a few")],
   ["How many apples do you have?",
    "There is some water in the glass.",
    "I don't have much money.",
    "She has a few friends at school.",
    "Is there any milk left?",
    "We need some information about the course.",
    "There is a little sugar in the bowl.",
    "How much time do we have?"],
   [("many apples","action"),("some water","state"),("much money","state"),("a few friends","action"),
    ("any milk","state"),("much time","state"),("some information","state"),("a few ideas","action")]),

  (8, "Referring to Nouns", "Articles · Determiners · This/That · These/Those",
   """<div class="sect">
     <div class="sect-title">📖 Articles: A/An vs The</div>
     <div class="rule-box">
       <strong>A/AN:</strong> first mention · unknown · general category<br>
       "I saw <strong>a movie</strong>. The movie was great."<br>
       "<strong>An</strong> honest person." (vowel sound starts)
     </div>
     <div class="rule-box">
       <strong>THE:</strong> second mention · specific · unique · known<br>
       "The teacher" (who we know) · "the sun" · "the Philippines"
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Rule:</strong> First mention = A/AN · Second mention = THE · General truth = no article (I like coffee.)</span></div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Demonstratives: This/That/These/Those</div>
     <div class="rule-box">
       <strong>THIS/THESE:</strong> near (time & space)<br>
       <strong>THAT/THOSE:</strong> far (time & space)<br>
       "This book is mine." (near) · "That book is hers." (far)<br>
       "These students are from my class." · "Those are from another school."
     </div>
   </div>""",
   [("I saw ___ movie last night. It was great.", ["a","an","the","no article"], 0),
    ("___ sun is very bright today.", ["The","A","An","no article"], 0),
    ("She is ___ honest teacher I know.", ["the","a","an","no article"], 0),
    ("___ books on that table are mine.", ["Those","These","That","The"], 0),
    ("Is there ___ milk in the fridge?", ["any","some","the","much"], 0),
    ("I have ___ idea. Let's go to the beach!", ["an","a","the","some"], 0),
    ("This is ___ best teacher I have ever had.", ["the","a","an","no article"], 0),
    ("___ students over there are from the Philippines.", ["Those","These","This","That"], 0),
    ("She plays ___ piano every day.", ["the","a","an","no article"], 0),
    ("I need ___ information about the course.", ["some","any","the","much"], 0)],
   [("I saw ___ movie last night. (a/the)", "a"),
    ("___ sun is very bright today. (The/A)", "The"),
    ("She is ___ honest teacher. (an/a/the)", "an"),
    ("___ books on that table are mine. (Those/These)", "Those"),
    ("Is there ___ milk in the fridge? (any/some)", "any"),
    ("I have ___ idea. Let's go! (an/a)", "an"),
    ("This is ___ best teacher. (the/a)", "the"),
    ("___ students over there are from my class. (Those/These)", "Those")],
   ["I saw a movie last night.",
    "The sun is very bright today.",
    "She is an honest teacher.",
    "Those books on that table are mine.",
    "Is there any milk in the fridge?",
    "I have an idea! Let's go to the beach.",
    "This is the best teacher I have ever had.",
    "Those students over there are from my class."],
   [("a movie","action"),("the sun","state"),("an honest teacher","action"),("those books","state"),
    ("any milk","state"),("an idea","state"),("the best teacher","action"),("those students","state")]),

  (9, "Pronouns & Referencing", "Personal · Relative · Demonstrative Pronouns",
   """<div class="sect">
     <div class="sect-title">📖 Personal Pronouns</div>
     <div class="rule-box">
       <strong>Subject:</strong> I, you, he, she, it, we, they<br>
       <strong>Object:</strong> me, you, him, her, it, us, them<br>
       "<strong>She</strong> gave <strong>them</strong> the book." (subject + object)
     </div>
     <div class="usecase">
       <strong>Possessive:</strong> my, your, his, her, its, our, their<br>
       "<strong>My</strong> book is here." · "Their teacher is kind."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Relative Pronouns</div>
     <div class="rule-box">
       <strong>WHO:</strong> people (subject or object)<br>
       "The teacher <strong>who</strong> taught me is kind."<br>
       <strong>WHICH:</strong> things (subject or object)<br>
       "The book <strong>which</strong> I read was interesting."<br>
       <strong>THAT:</strong> people & things (defining clauses)<br>
       "The student <strong>that</strong> studied passed."
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Key:</strong> WHO = people · WHICH = things · THAT = people + things (defining only)</span></div>
   </div>""",
   [("The teacher ___ taught me is from the Philippines.", ["who","which","that","whom"], 0),
    ("The book ___ I read was interesting.", ["which","who","that","whose"], 0),
    ("The student ___ passed the exam was happy.", ["who","which","whom","whose"], 0),
    ("I gave the book to ___.", ["her","she","his","them"], 0),
    ("___ dog is that? It's ours.", ["Whose","Who","Which","Whom"], 0),
    ("The man ___ I met was very kind.", ["whom","who","which","that"], 0),
    ("She is a teacher ___ teaches English.", ["who","which","that","whose"], 0),
    ("The school ___ we visited was new.", ["which","who","that","whom"], 0),
    ("___ umbrella is this? It's mine.", ["Whose","Who","Which","Whom"], 0),
    ("The children ___ are playing are happy.", ["who","which","that","whose"], 0)],
   [("The teacher ___ taught me is from the Philippines. (who/which)", "who"),
    ("The book ___ I read was interesting. (which/who)", "which"),
    ("The student ___ passed was happy. (who/which)", "who"),
    ("I gave the book to ___. (her/she)", "her"),
    ("___ dog is that? It's ours. (Whose/Who)", "Whose"),
    ("The man ___ I met was very kind. (whom/who)", "whom"),
    ("She is a teacher ___ teaches English. (who/which)", "who"),
    ("The school ___ we visited was new. (which/who)", "which")],
   ["The teacher who taught me is from the Philippines.",
    "The book which I read was interesting.",
    "The student who passed was happy.",
    "I gave the book to her.",
    "Whose dog is that? It's ours.",
    "The man whom I met was very kind.",
    "She is a teacher who teaches English.",
    "The school which we visited was new."],
   [("who taught","action"),("which I read","state"),("who passed","action"),("her","state"),
    ("whose dog","state"),("whom I met","action"),("who teaches","action"),("which we visited","state")]),

  (10, "Adjectives & Adverbs", "Order · Comparison · -ly adverbs · Compound adjectives",
   """<div class="sect">
     <div class="sect-title">📖 Adjective Order</div>
     <div class="rule-box">
       <strong>Opinion → Size → Age → Shape → Colour → Origin → Material → Purpose</strong><br>
       "A beautiful small old round red Italian leather handbag."<br>
       "A lovely big new rectangular blue Japanese plastic water bottle."
     </div>
     <div class="tip-box"><span class="tip-icon">💡</span><span class="tip-text"><strong>Easy rule:</strong> Opinion comes FIRST. Always.</span></div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Comparison</div>
     <div class="rule-box">
       <strong>+er / +est:</strong> short adjectives<br>
       "tall → taller → tallest"<br>
       <strong>+ more / + most:</strong> long adjectives<br>
       "beautiful → more beautiful → most beautiful"<br>
       <strong>Irregular:</strong> good → better → best · bad → worse → worst
     </div>
     <div class="usecase">
       "<strong>As...as</strong> = equal comparison<br>
       "She is <strong>as tall as</strong> her brother."<br>
       "<strong>Not as...as</strong> = less than<br>
       "He is <strong>not as tall as</strong> his sister."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Adverbs (-ly)</div>
     <div class="rule-box">
       <strong>Formation:</strong> adjective + -ly<br>
       "quick → quickly" · "careful → carefully" · "beautiful → beautifully"<br>
       <strong>Exception:</strong> "good → well" (not "goodly")
     </div>
     <div class="usecase">
       "She <strong>sings beautifully</strong>." (how? = adverb)<br>
       "She is a <strong>beautiful singer</strong>." (what kind? = adjective)
     </div>
   </div>""",
   [("She is ___ than her sister.", ["taller","tallest","more tall","taller"], 0),
    ("He is the ___ student in the class.", ["best","goodest","most good","better"], 0),
    ("She sings ___. (beautiful)", ["beautifully","beautiful","goodly","beauty"], 0),
    ("This is ___ movie I have ever seen.", ["the best","better","gooder","most best"], 0),
    ("A ___ old house (opinion, age)", ["beautiful","big","old","tall"], 0),
    ("He runs ___ than his brother.", ["faster","more fast","fastest","faster"], 0),
    ("She is not ___ as her brother.", ["as tall","taller","tallest","so tall"], 0),
    ("He did the test ___ than me.", ["worse","worst","more bad","badder"], 0),
    ("A ___ man (adj/adv?)", ["kind","kindly"],"kind"),
    ("She spoke ___ to the student.", ["politely","polite","politeness","more polite"], 0)],
   [("She is ___ than her sister. (tall/taller)", "taller"),
    ("He is the ___ student. (good/best)", "best"),
    ("She sings ___. (beautiful → ?)", "beautifully"),
    ("This is ___ movie I have ever seen. (good → ?)", "the best"),
    ("He runs ___ than his brother. (fast → ?)", "faster"),
    ("She is not ___ as her brother. (tall → ?)", "as tall"),
    ("He did the test ___. (bad → ?)", "worse"),
    ("She spoke ___ to the student. (polite → ?)", "politely")],
   ["She is taller than her sister.",
    "He is the best student in the class.",
    "She sings beautifully.",
    "This is the best movie I have ever seen.",
    "He runs faster than his brother.",
    "She is not as tall as her brother.",
    "He did the test worse than me.",
    "She spoke politely to the student."],
   [("taller","action"),("best","state"),("beautifully","action"),("worse","action"),
    ("as tall","state"),("faster","action"),("the best","state"),("politely","action")]),

  (11, "Comparing Things", "Comparatives · Superlatives · As...as · Irregular",
   """<div class="sect">
     <div class="sect-title">📖 Comparatives & Superlatives</div>
     <div class="rule-box">
       <strong>Short adj:</strong> -er / -est · "tall → taller → tallest"<br>
       <strong>Long adj:</strong> more / most · "beautiful → more beautiful → most beautiful"<br>
       <strong>End in -y:</strong> -ier / -iest · "happy → happier → happiest"
     </div>
     <div class="usecase">
       "Manila is <strong>larger than</strong> Cebu." (comparative)<br>
       "Manila is <strong>the largest</strong> city in the Philippines." (superlative)
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 As...as (Equal Comparison)</div>
     <div class="rule-box">
       "<strong>As...as</strong> = equal · "She is <strong>as tall as</strong> me."<br>
       "<strong>Not as...as / not so...as</strong> = less than<br>
       "He is <strong>not as clever as</strong> his sister."
     </div>
   </div>
   <div class="sect">
     <div class="sect-title">📖 Irregular Comparisons</div>
     <div class="rule-box">
       good → better → best<br>
       bad → worse → worst<br>
       far → farther/further → farthest/furthest<br>
       much/many → more → most<br>
       little → less → least
     </div>
   </div>""",
   [("Manila is ___ Cebu.", ["larger than","big than","more big than","bigger"], 0),
    ("She is the ___ student in class.", ["best","goodest","most good","better"], 0),
    ("He is not ___ as his brother.", ["as tall","taller","tallest","so tall"], 0),
    ("This is ___ decision I have ever made.", ["the hardest","harder than","more hard","harder"], 0),
    ("He runs ___ than before.", ["faster","more fast","fastest","fastlier"], 0),
    ("She is ___ person I know.", ["the most generous","generouser","more generous","generouser"], 0),
    ("The book was ___ than the movie.", ["more interesting","interestinger","more interestinger","interesting"], 0),
    ("He did ___ than expected.", ["better","more good","gooder","best"], 0),
    ("This problem is ___ than that one.", ["easier","more easy","easyer","easyer"], 0),
    ("She sings ___ than anyone I know.", ["better","weller","more good","best"], 0)],
   [("Manila is ___ Cebu. (large → ?)", "larger than"),
    ("She is the ___ student. (good → ?)", "best"),
    ("He is not ___ as his brother. (tall → ?)", "as tall"),
    ("This is ___ decision. (hard → ?)", "the hardest"),
    ("He runs ___ than before. (fast → ?)", "faster"),
    ("The book was ___ than the movie. (interesting → ?)", "more interesting"),
    ("He did ___ than expected. (good → ?)", "better"),
    ("This problem is ___ than that one. (easy → ?)", "easier")],
   ["Manila is larger than Cebu.",
    "She is the best student in class.",
    "He is not as tall as his brother.",
    "This is the hardest decision I have ever made.",
    "He runs faster than before.",
    "The book was more interesting than the movie.",
    "He did better than expected.",
    "This problem is easier than that one."],
   [("larger than","action"),("the best","state"),("as tall","state"),("the hardest","action"),
    ("faster","action"),("more interesting","state"),("better","action"),("easier","state")]),
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
        unit_tabs_html += f'<a href="{href}" class="utab {active}"><span class="un">{u}</span><span style="font-size:0.72rem;color:var(--muted)">{"Present Tenses" if u==1 else "..."}</span></a>\n'

    html = TEMPLATE
    # Replace unit info
    html = html.replace("Unit 1: Present Tenses — Grammar Mastery Academy", f"Unit {num}: {title} — Grammar Mastery Academy")
    html = html.replace("Unit 1 — Present Tenses", f"Unit {num} — {title}")
    html = html.replace("Present Simple · Continuous · State Verbs", subtitle)

    # Replace lesson content
    start = html.find('<div class="sect"')
    end = html.find('<div class="nav-btns"')
    if start != -1 and end != -1:
        html = html[:start] + lesson_html + '\n<div class="nav-btns">' + html[end + len('<div class="nav-btns">'):]

    # Replace nav buttons
    html = html.replace(
        '<a href="grammar-hub.html" class="btn-prev">← Hub</a>',
        f'<a href="grammar-hub.html" class="btn-prev">← Hub</a>'
    )

    # Replace JS data
    # Remove old QUIZ/FILLIN/SPEAK/VERBS and insert new
    import re
    html = re.sub(r'const QUIZ_DATA=\[.*?\];', quiz_js, html, flags=re.DOTALL)
    html = re.sub(r'const FILLIN_DATA=\[.*?\];', fillin_js, html, flags=re.DOTALL)
    html = re.sub(r'const SPEAK_DATA=\[.*?\];', speak_js, html, flags=re.DOTALL)
    html = re.sub(r'const VERBS=\[.*?\];', match_js, html, flags=re.DOTALL)

    # Update unit tabs
    html = re.sub(r'<div class="unit-tabs">.*?</div>', f'<div class="unit-tabs">{unit_tabs_html}</div>', html, flags=re.DOTALL)

    return html

def main():
    for unit in UNITS:
        num, title, subtitle, lesson_html, quiz_items, fillin_items, speak_items, match_items = unit
        print(f"Generating Unit {num}: {title}...")
        html = generate_unit(num, title, subtitle, lesson_html, quiz_items, fillin_items, speak_items, match_items)
        fname = f'grammar-unit-{num:02d}.html'
        fpath = os.path.join(BASE, fname)
        with open(fpath, 'w') as f:
            f.write(html)
        print(f"  Wrote: {fname} ({len(html)} bytes)")
    print("Done! 10 units generated.")

if __name__ == '__main__':
    main()