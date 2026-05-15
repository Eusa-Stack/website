# EduSuite — Navbar & Classroom Redesign Plan

**Päivämäärä:** 16.5.2026
**Tila:** SUUNNITELMA — ei vielä toteutettu

---

## Nykytilanne

### Nykyinen navbar-ongelma

**index.html:** `nav` → vain EduSuite-brändi + YouTube-linkki
**subjects.html:** `nav` → EduSuite-brändi + "← Home"-linkki

 Molemmat navit ovat minimaalisia, epäyhtenäisiä, ja puuttuu:
 - Ei selkeää jakoa "etusivu / luokkahuone"
 - Ei vasenta sub-navia (aihe-linkit)
 - Ei theme toggle samassa paikassa molemmissa
 - Ei johdonmukaista rakennetta

---

## Uusi suunnitelma: Yläpalkki (Global Navbar)

### Rakenne: 3 osaa vaakasuunnassa

```
[VASEN]          [KESKI]          [OIKEA]
EduSuite         (tyhjä)          [Väriteema ☾/☀]
brändi +                           + Linkit: Etusivu | Luokkahuone
sub-nav
```

### Yksityiskohtainen jako:

#### Vasen (brändi + sub-nav)
```
EduSuite 🎓  [Koti] [📚 Aiheet] [🎓 Luokkahuone] [💬 Yhteys]
```

#### Keski
Tyhjä / flex-grow — tasapainoa varten

#### Oikea
```
[Etusivu] [Luokkahuone]  [☾ / ☀]
```

### KÄYTTÖLOGIIKKA:
- **Etusivu** → `index.html` (EUSTAQUIA - tarina, opettaja, mission)
- **Luokkahuone** → `classroom.html` (UUSI — kaikki pelit aineittain)
- **Aiheet** → `subjects.html` (nykyinen grid-näkymä)
- **Väriteema** → yksi ja sama `☾/☀` nappi kaikilla sivuilla, sama logiikka

### Child-friendly huomiot:
- Fontti: Fredoka (iso, pyöreä, ystävällinen)
- Nav-nappien koko: ≥44px korkea (kosketusystävällinen)
- Hover: selkeä värimuutos
- Ei liian montaa linkkiä kerralla

---

## Classroom (Luokkahuone) — Uudelleenrakennus

### Nykyinen ongelma:
`subjects.html` on sekava 10 aineen gridi ilman hierarkiaa. Lapset eksyvät kun on liikaa kerralla.

### Uusi rakenne: Koulu-metoforia

```
Luokkahuone
│
├── 🎨 Taide (Art)
│     └─ Tietokoneet & Teknologia
│
├── 📐 Matematiikka (Math)
│     ├─ Peruslaskut
│     ├─ Desimaalit
│     └─ Geometria / Murtoluvut
│
├── 🌍 Maantiede (Geography)
│     ├─ Liput
│     └─ Valtiot / Kaupungit
│
├── 🧪 Luonnontiede (Science)
│     ├─ Biologia (Eläimet Kasvit)
│     ├─ Fysiikka (Voima, Painovoima)
│     └─ Kemia (Alkuaineet)
│
├── 🏛️ Historia (History)
│     └─ Aikajanat
│
├── 📝 Kielioppi & Kirjoitus (English)
│     ├─ Vocabulary (Word Match, My Name)
│     ├─ Grammar Hub (25 yksikköä)
│     ├─ Grammar Coach (henkilökohtainen)
│     └─ IELTS (6 sivua)
│
├── 🧠 Yleissivistys (General Knowledge)
│     ├─ Quick Quiz
│     └─ Fraction Pizza
│
└── 📖 Lukeminen (Reading) — TULEE VIELÄ
```

### Classroom-sivu: `classroom.html`

Rakenne:
1. **Hero osio:** "🎓 Luokkahuone — Valitse aine" + haku
2. **Aine-valikko:** Isoja kortteja (subject cards), max 3 sarakkeetta
3. **Yksittäisen aineen sisällä:** Pelit ja sivut listana / card-gridinä

### Navigaatio classroomissa:
```
[Yläpalkki]
[Vasemmalta: Aihe-valikko] [Oikealla: Sisältö-grid]
```

Eli kun klikkaa ainetta → näyttää sen aineen pelit samalla sivulla (ei eri sivua).

---

## Toteutus-järjestys

### Vaihe A: Yläpalkki uusiksi (molemmat sivut)
1. Luo `navbar.css` — yhtenäinen global navbar-tyyli
2. Päivitä `index.html` nav — lisää "Luokkahuone" + "Aiheet" linkit + theme toggle
3. Päivitä `subjects.html` nav — sama rakenne, oikealla "Etusivu | Luokkahuone"
4. Varmista: molemmat navit identtiset lukuunottamatta aktiivista linkkiä

### Vaihe B: Classroom-sivu (`classroom.html`)
1. Suunnittele hierarkia: 8-9 ainetta
2. Kirjoita `classroom.html` — subject-selector + dynamic content loading
3. Käytä `SUBJECTS` data-struktuuria (JavaScript) — yksi paikka hallita kaikkea
4. Sub-linkit vasemmalla (aiheesta riippuen)

### Vaihe C: Integrointi
1. `subjects.html` linkittää `classroom.html`:een ("🎓 Luokkahuone"-nappi)
2. Classroom ja subjects jakavat saman `SUBJECTS` datan
3. Footer päivitykset

---

## Yksityiskohdat

### Navbar CSS (navbar.css)
```css
/* Fixed top, blur backdrop, 60px korkea */
.global-nav {
  display: flex;
  align-items: center;
  padding: 0 1.2rem;
  height: 60px;
  background: rgba(255,255,255,0.85);
  backdrop-filter: blur(16px);
  border-bottom: 3px solid var(--yellow);
  position: sticky; top: 0; z-index: 200;
  gap: 0.5rem;
}
.nav-brand { font-family: 'Fredoka'; font-size: 22px; font-weight: 700; }
.nav-links { display: flex; gap: 0.3rem; margin-left: 1rem; }
.nav-link { padding: 0.45rem 0.9rem; border-radius: 12px; font-size: 14px; font-weight: 700; text-decoration: none; color: var(--text); transition: 0.15s; }
.nav-link:hover { background: rgba(244,132,95,0.12); }
.nav-link.active { background: rgba(244,132,95,0.18); color: var(--orange); }
.nav-right { margin-left: auto; display: flex; align-items: center; gap: 0.5rem; }
.nav-page-links { display: flex; gap: 0.4rem; font-size: 13px; font-weight: 700; }
.nav-page-link { color: var(--soft); text-decoration: none; padding: 0.3rem 0.6rem; border-radius: 8px; transition: 0.15s; }
.nav-page-link:hover { color: var(--text); background: rgba(0,0,0,0.06); }
.theme-btn { font-size: 1rem; padding: 4px 12px; }
```

### Classroom Data Structure
```javascript
const CLASSROOMS = [
  {
    id: 'math',
    icon: '📐',
    name: 'Matematiikka',
    nameEn: 'Math',
    color: 'var(--orange)',
    topics: [
      { name: 'Desimaalit', icon: '🧮', href: 'math-games.html', lvl: 'Beginner' },
      { name: 'Luvut & Numeerisuus', icon: '⚔️', href: 'number-ninja.html', lvl: 'Advanced' },
    ]
  },
  {
    id: 'science',
    icon: '🧪',
    name: 'Luonnontiede',
    nameEn: 'Science',
    color: 'var(--purple)',
    topics: [
      { name: 'Biologia', icon: '🌿', href: 'animal-sort.html', lvl: 'Beginner' },
      { name: 'Fysiikka', icon: '⚡', href: 'gravity-drop.html', lvl: 'Beginner' },
      { name: 'Kemia', icon: '⚗️', href: 'element-mix.html', lvl: 'Beginner' },
    ]
  },
  // ... jne
];
```

### Child-Friendly periaatteet
- **Iso iconi joka aineelle** (≥48px) — visuaalinen-orientaatio
- **Värikoodatut aiheet** — oranssi=math, violetti=science, vihreä=english jne.
- **Yksi aihe kerrallaan** — ei 10 aineen sekoa
- **Selkeä "mene takaisin"** -nappi jokaisessa aliosiossa
- **Ei pitkää tekstiä** — pikkulapset ei jaksa lukea
- **Suuret napit** — min 60px korkea
- **Äänikomennot** — mahdollisuuksien mukaan

---

## Tiedostot joita muutetaan

| Tiedosto | Toimenpide |
|---|---|
| `navbar.css` | UUSI — jaettu navbar-tyyli |
| `index.html` | Nav päivitys — lisää Luokkahuone-linkit + oikea navbar |
| `subjects.html` | Nav päivitys — yhtenäinen rakenne, classroom-linkki |
| `classroom.html` | UUSI — koko luokkahuone-sivu |
| `theme.css` | Navbar-tyylit? Tai erillinen navbar.css? |
| `floating-anim.js` | Poista duplicate — siirry navbar.commonta |

---

## Seisake-piste (checkpoint)

**Ennen toteutusta — hyväksyttävä:**
1. Navbar-rakenne: 3 osaa (vasen brandi, keski tyhjä, oikea links + theme)
2. Classroom-hierarkia: 8 ainetta hyväksytty
3. Child-friendly periaatteet: hyväksytty
4. Tiedostolistaus: hyväksytty

---

## Notaatiot
- Kaikki nav-barit käyttävät samaa CSS:ää (`navbar.css`)
- `classroom.html` on uusi sivu — ei korvata `subjects.html`
- Molemmat (`subjects.html` ja `classroom.html`) toimivat rinnakkain
- `subjects.html` voi säilyä "nopea grid-näkymä" -linkkinä Classroomiin