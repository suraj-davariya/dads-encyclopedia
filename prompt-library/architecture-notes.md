# 🏗️ Encyclopedia Architecture Notes
> **Status:** Saved for future reference | **Version:** 1.0

## Current Architecture (Static HTML)
The encyclopedia currently uses a **static monolithic HTML** approach:
- All week chapters are injected as full `<article id="week-N">` blocks inside `index.html`
- Each week contains the same template sections: Quick Overview, Baby Development, Partner's Journey, Mission Control (tabbed), Bonding Lab, Checklist, Medical Roadmap, Expert Tips, Quick Ref Cards, Summary Box
- CSS is in `styles.css`, interactivity in `app.js`

---

## Future Architecture Option: JS Data-Driven SPA

If the project needs to scale to all 40+ weeks without a 500KB+ HTML file, consider migrating to a **JavaScript data-driven Single Page Application (SPA)**:

### Week Data Structure (per week)
```js
{
  week: 4,
  phase: 't1', // prep | t1 | t2 | t3 | birth
  title: "The Moment Everything Changes",
  emoji: "🌱",
  size: "poppy seed",
  weight: "< 1g",
  baby: [
    "Blastocyst implants in uterine wall.",
    "Neural tube begins forming.",
    "Heart tube starts pulsing.",
  ],
  symptoms: [
    { name: "Fatigue", why: "Rising progesterone", help: "Take over evening chores" },
  ],
  emotional: ["...", "..."],
  practical: ["...", "..."],
  relationship: { dates: [], intimacy: "...", conflict: "..." },
  bonding: { talk: "...", music: "...", challenge: { title: "...", body: "..." } },
  checklist: { must: [], optional: [], nursery: [] },
  medical: { appointments: [], tests: [], questions: [], redFlags: [] },
  tips: [
    { role: "OB-GYN", tip: "..." },
    { role: "Doula", tip: "..." },
    { role: "Dad Veteran", tip: "..." },
  ],
  takeaways: ["...", "...", "...", "...", "..."],
  actions: ["...", "...", "..."],
  reflection: "..."
}
```

### Week Groups
```js
const GROUPS = {
  prep:  { label: "Pre-Conception",    color: "#6b7280", weeks: ['prep'] },
  t1:    { label: "First Trimester",   color: "#d97706", weeks: [1,2,3,4,5,6,7,8,9,10,11,12,13] },
  t2:    { label: "Second Trimester",  color: "#16a34a", weeks: [14,15,16,17,18,19,20,21,22,23,24,25,26,27] },
  t3:    { label: "Third Trimester",   color: "#7c3aed", weeks: [28,29,30,31,32,33,34,35,36,37,38,39,40] },
  birth: { label: "Birth & Beyond",    color: "#dc2626", weeks: ['birth', 'postpartum'] }
}
```

### SPA HTML Shell
```
<header> (sticky nav, dark mode toggle)
<aside class="sidebar"> (week navigator grouped by trimester)
<main>
  <div id="week-display"></div>  <!-- JS renders here -->
  <div class="week-nav-btns">prev / next</div>
</main>
<footer>
<script>
  const WEEKS = { ...all data... };
  function renderWeek(num) { /* build and inject HTML */ }
  window.onload = () => renderWeek(4);
</script>
```

### Fruit Size Reference (all 40 weeks)
| Week | Fruit | Size |
|------|-------|------|
| 4 | Poppy Seed | < 1mm |
| 5 | Sesame Seed | 3mm |
| 6 | Sweet Pea | 5mm |
| 7 | Blueberry | 10mm |
| 8 | Kidney Bean | 16mm |
| 9 | Grape | 23mm |
| 10 | Kumquat | 3.1cm |
| 11 | Fig | 4.1cm |
| 12 | Lime | 5.4cm |
| 13 | Peach | 7.4cm |
| 14 | Lemon | 8.7cm |
| 15 | Apple | 10.1cm |
| 16 | Avocado | 11.6cm |
| 17 | Turnip | 13cm |
| 18 | Bell Pepper | 14.2cm |
| 19 | Tomato | 15.3cm |
| 20 | Banana | 25.6cm |
| 21 | Carrot | 26.7cm |
| 22 | Coconut | 27.8cm |
| 23 | Grapefruit | 28.9cm |
| 24 | Corn | 30cm |
| 25 | Cauliflower | 34.6cm |
| 26 | Scallion | 35.6cm |
| 27 | Head of Lettuce | 36.6cm |
| 28 | Eggplant | 37.6cm |
| 29 | Butternut Squash | 38.6cm |
| 30 | Cabbage | 39.9cm |
| 31 | Coconut | 41.1cm |
| 32 | Jicama | 42.4cm |
| 33 | Pineapple | 43.7cm |
| 34 | Cantaloupe | 45cm |
| 35 | Honeydew | 46.2cm |
| 36 | Romaine Lettuce | 47.4cm |
| 37 | Winter Melon | 48.6cm |
| 38 | Leek | 49.8cm |
| 39 | Mini Watermelon | 50.7cm |
| 40 | Small Pumpkin | 51.2cm |
