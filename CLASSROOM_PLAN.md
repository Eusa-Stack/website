# Classroom — Kaikki Pelit & Sivut (Hierarkia)

**Päivämäärä:** 16.5.2026
**Tila:** SUUNNITELMA — tarkistettavana

---

## 🎓 Luokkahuone — Rakenne

Kaikki pelit ja sivut tulevat classroomiin. Sub-sivuja luodaan tarvittaessa.

---

## AIHE-HIERARKIA (7 ainetta)

```
🎓 Luokkahuone
│
├── 📐 Matematiikka (Math)
│     ├─ 🧮 Decimal Games — Beginner
│     ├─ ⚔️ Number Ninja — Advanced
│     └─ 🍕 Fraction Pizza — All Levels (murtoluvut)
│
├── 🌍 Maantiede (Geography)
│     ├─ 🏁 Flag Match — Beginner
│     └─ 🗺️ Geo Challenge — Advanced
│
├── 🏛️ Historia (History)
│     └─ ⏳ Time Train — Beginner
│
├── 🧪 Luonnontiede (Science)
│     ├─ 🌿 Biologia
│     │     └─ 🐾 Animal Sort — Beginner
│     ├─ ⚡ Fysiikka
│     │     ├─ 🪂 Gravity Drop — Beginner
│     │     └─ 🔬 Force Lab — Advanced
│     └─ ⚗️ Kemia
│           ├─ ⚗️ Element Mix — Beginner
│           └─ ⚖️ Balance Lab — Advanced
│
├── 📝 Kieli & Sanasto (English)
│     ├─ 💬 Sanat
│     │     ├─ 💬 Word Match Jr — Beginner
│     │     └─ ✏️ My Name! — Beginner
│     └─ 📚 Kielioppi
│           ├─ 📚 Grammar Hub — All (25 yksikköä)
│           ├─ 👩‍🏫 Grammar Coach — Personal
│           └─ 📝 IELTS Grammar — Intermediate
│
├── 🎓 IELTS Valmistautuminen (IELTS)
│     ├─ ⚡ 3-Day Power Study — All
│     ├─ 🎓 Academic vs General — Intermediate
│     ├─ 🏆 Band Score Tracker — Intermediate
│     ├─ ✍️ Writing Task 2 — Intermediate
│     ├─ 🎧📖✍️🗣️ All 4 Subjects — All
│     └─ 🔀 Drag & Sort Quiz — All
│
└── 🧠 Yleissivistys (General Knowledge)
      └─ 🧩 Quick Quiz — All Levels
```

---

## Yhteenveto: Mihin kaikki kuuluu?

| Aine | Peli/Sivu | Taso |
|---|---|---|
| **Matematiikka** | Decimal Games | Beginner |
| | Number Ninja | Advanced |
| | Fraction Pizza | All |
| **Maantiede** | Flag Match | Beginner |
| | Geo Challenge | Advanced |
| **Historia** | Time Train | Beginner |
| **Luonnontiede** | Animal Sort | Beginner |
| | Gravity Drop | Beginner |
| | Force Lab | Advanced |
| | Element Mix | Beginner |
| | Balance Lab | Advanced |
| **Kieli & Sanasto** | Word Match Jr | Beginner |
| | My Name! | Beginner |
| | Grammar Hub | All |
| | Grammar Coach | Personal |
| | IELTS Grammar | Intermediate |
| **IELTS** | 3-Day Power Study | All |
| | Academic vs General | Intermediate |
| | Band Score Tracker | Intermediate |
| | Writing Task 2 | Intermediate |
| | All 4 Subjects | All |
| | Drag & Sort Quiz | All |
| **Yleissivistys** | Quick Quiz | All |

**Yhteensä:** 14 peliä + 9 grammar/IELTS sivua = 23 kohdetta

---

## Sivuston rakenne

```
┌─────────────────────────────────────────────────────┐
│  [EduSuite 🎓]  [Koti] [📚 Aiheet] [🎓 Luokkahuone]  [Etusivu] [Luokkahuone] [☾/☀]  │
└─────────────────────────────────────────────────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
    index.html                      classroom.html
    (Etusivu)                       (Luokkahuone)
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                 ▼
              [Math 🧮]        [Science 🧪]       [IELTS 🎓]
              [Geo 🌍]        [History 🏛]       [Language 📝]
              ...                  ...              ...
```

---

## Classroom-sivu: Miten se toimii?

### Näkymä 1: Aihe-valikko (default)
- 7 isoa aine-korttia (emoji + nimi + pelimäärä)
- Click → näyttää sen aineen pelit samalla sivulla (JAVASCRIPT)

### Näkymä 2: Yksittäinen aihe
- Vasemmalla: "← Takaisin" + aineen nimi
- Oikealla: sen aineen pelit listana
- Voidaan myös avata omaksi sivuksi (/classroom/math.html)

### Esimerkki: Matematiikka klikattu
```
┌─────────────────────────────────────────────────────┐
│  [EduSuite 🎓]  [Koti] [📚 Aiheet] [🎓 Luokkahuone]  [Etusivu] [Luokkahuone] [☾/☀]  │
├─────────────────────────────────────────────────────┤
│                                                     │
│   📐 MATEMATIIKKA                      [← Takaisin] │
│                                                     │
│   ┌────────────┐ ┌────────────┐ ┌────────────┐     │
│   │   🧮       │ │   ⚔️       │ │   🍕       │     │
│   │  Decimal   │ │   Number   │ │  Fraction  │     │
│   │   Games    │ │   Ninja    │ │   Pizza    │     │
│   │  Beginner  │ │  Advanced  │ │    All     │     │
│   │     →      │ │     →      │ │     →      │     │
│   └────────────┘ └────────────┘ └────────────┘     │
│                                                     │
│   [Muut aiheet: Geo | Historia | Science | ...]     │
└─────────────────────────────────────────────────────┘
```

---

## Tiedostot

### classroom.html (UUSI — pääsivu)
- Aihe-valikko (7 ainetta isoina korttina)
- JavaScript: klikkaus näyttää oikean aineen pelit
- Jaetut: navbar.css, theme.css, grammar-shared.css

### classroom/math.html (ALASIVU — valinnainen)
- Matematiikan omat pelit
- Voi toimia myös suoraan classroom.html:n kautta

### subjects.html
- Säilyy rinnakkain — grid-näkymä kaikista peleistä
- "🎓 Luokkahuone" -nappi vie classroom.html:en

---

## Child-friendly toteutus

### Periaatteet
1. **Iso emoji** joka aineella (≥48px) — visuaalinen
2. **Värikoodaus** — jokaisella aineella oma väri
3. **Ei liikaa kerralla** — default: 7 aine-korttia
4. **Suuret napit** — pelikortit ≥80px korkeat
5. **Selkeä takaisin-nappi** — aina näkyvissä alanäkymässä
6. **Taso-merkinnät** — Beginner/Advanced/All selkeästi

### Aineiden värit
```
Matematiikka    → oranssi  (#F4845F)
Maantiede       → sininen  (#4B9EFF)
Historia        → keltainen (#F7C948)
Luonnontiede    → violetti  (#A78BFA)
Kieli & Sanasto → vihreä   (#43B97A)
IELTS           → pinkki    (#F472B6)
Yleissivistys   → harmaa   (#94A3B8)
```

### Aine-kortit (default-näkymä)
```
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│      📐         │  │      🌍         │  │      🏛️         │
│   Matematiikka  │  │   Maantiede    │  │    Historia     │
│     3 peliä     │  │     2 peliä     │  │     1 peli      │
└─────────────────┘  └─────────────────┘  └─────────────────┘
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│      🧪         │  │      📝         │  │      🎓         │
│  Luonnontiede   │  │ Kieli & Sanasto │  │      IELTS      │
│     5 peliä     │  │     5 kohdetta  │  │     6 sivua     │
└─────────────────┘  └─────────────────┘  └─────────────────┘
┌─────────────────┐
│      🧠         │
│  Yleissivistys  │
│     1 peli      │
└─────────────────┘
```

### Pelikortit (aineen sisällä)
```
┌────────────────────────────────────────────┐
│  🧮  Decimal Games                         │
│  Opettele desimaaliluvut helposti!         │
│  🌱 Beginner                               │
│                                      [AVAA →] │
└────────────────────────────────────────────┘
```

---

## Tekninen toteutus

### classroom.html rakenne
```html
<!DOCTYPE html>
<html>
<head>
  <!-- theme-manager.js ENNEN mitään muuta -->
  <script src="theme-manager.js"></script>
  <link rel="stylesheet" href="theme.css">
  <link rel="stylesheet" href="navbar.css">
  <link rel="stylesheet" href="grammar-shared.css">
</head>
<body>

<!-- GLOBAL NAVBAR -->
<nav class="global-nav">...</nav>

<!-- AIHE-VALIKKO (default näkymä) -->
<div id="subject-grid" class="subject-grid">
  <!-- 7 aine-korttia -->
</div>

<!-- PELI-GRIDI (näkyy kun aihe valittu) -->
<div id="games-grid" class="games-grid" style="display:none">
  <!-- Pelikortit -->
</div>

<!-- FOOTER -->
<footer>...</footer>

<script>
const CLASSROOMS = [
  { id:'math', icon:'📐', name:'Matematiikka', color:'var(--orange)', items:[...] },
  { id:'science', icon:'🧪', name:'Luonnontiede', color:'var(--purple)', items:[...] },
  // ...
];

function showSubject(id) {
  // Piilota subject-grid, näytä games-grid
  // Lataa oikean aineen pelit
}
</script>
</body>
</html>
```

### Jaetut resurssit
- `navbar.css` — yhtenäinen navbar kaikille sivuille
- `theme.css` — värit (light + dark)
- `theme-manager.js` — teema-toggle
- `grammar-shared.css` — fontit ja perusystyylit

---

## Toteutus-järjestys

| Vaihe | Toimenpide |
|---|---|
| **A1** | `navbar.css` — luo yhtenäinen navbar-tyyli |
| **A2** | Päivitä `index.html` — uusi navbar (Koti/Aiheet/Luokkahuone + oikea links + theme) |
| **A3** | Päivitä `subjects.html` — sama navbar, classroom-linkki |
| **B1** | `classroom.html` — aihe-valikko (7 ainetta) + JS showSubject() |
| **B2** | `classroom.html` — pelikortit jokaiselle aineelle |
| **C** | RSYNC + Git + Testaa selaimessa |
| **D** | Wiki päivitys (id=25 Eusa-Stack) |

---

## Huomiot

1. **Kaikki 14 peliä** + 9 grammar/IELTS sivua → kaikki classroomissa
2. **Luonnontiede** on "container-aine" — sisältää Bio, Fysiikka, Kemia
3. **Kieli & Sanasto** sisältää sekä sanaston (Word Match, My Name!) että kieliopin (Grammar Hub, Coach, IELTS Grammar)
4. **IELTS** on oma ison osionsa — 6 sivua
5. **Fraction Pizza** → Matematiikka (murtoluvut = math)
6. **Quick Quiz** → Yleissivistys (General Knowledge)