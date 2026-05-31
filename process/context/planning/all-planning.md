# First-Time Dad's Pregnancy Encyclopedia — Planning Context & Backlog Vault

Last updated: May 31, 2026

Attach this file first when planning, scoping, or initializing backlog features or milestones.

---

## 📂 Overview & Scope

This planning context serves as the canonical registry and brain vault for the application's roadmap. It contains:
1. **Standard planning routing tables** matching the harness conventions.
2. **Detailed backlog blueprints** for Options B, C, and PDF Export tools, ensuring no architectural details are lost across different runs or models.

---

## 🗺️ Quick Start

| Backlog Item | Target Component | Logic Type |
|---|---|---|
| **Option B: Special Sections** | `index.html` (Static Sections) | HTML5 semantic layouts + OKLCH style tokens |
| **Option C: Dad's Weekly Journal** | `index.html` (Sidebar) + localStorage | Javascript event listeners + localStorage persistence |
| **Option D: PDF Export Tool** | `index.html` (Header) + Print Styles | CSS `@media print` block + `window.print()` trigger |

---

## 📓 1. Option B: Special Sections Data Blueprint

### Section B: Relationship Compass
* **Objective**: Maintain intimacy, communication, and healthy partnerships during pregnancy.
* **Component Location**: Static section at the bottom of the dashboard or a dedicated tab.
* **Schema / Structure**:
  * **Intimacy Roadmap**: A trimester-by-trimester guide explaining medical safety, physical changes, and emotional intimacy.
  * **Division of Labor Model**: Chore redistribution templates designed to offset the partner's physical fatigue.
  * **Communication Prompts**: Weekly conversation starters to check in on parental alignment.

### Section D: Wellness Command Center
* **Objective**: Provide expectant fathers with stress relief, mental health check-ins, and core conditioning guidelines.
* **Component Location**: Dedicated drawer or modal in the UI.
* **Content Nodes**:
  * *Box Breathing Exercise*: Dynamic visual circle animation helping dads do 4-4-4-4 breathing (4s inhale, 4s hold, 4s exhale, 4s hold).
  * *Paternal Mental Health Checklist*: Self-assessment questions targeting postpartum depression signs in fathers (which affect ~10% of new dads).
  * *Functional Core Strength*: Core exercises tailored to prepare dads for carrying, lifting, and rocking infants.

### Section E: Cultural Celebrations & Milestones
* **Objective**: Log pregnancy milestones, photo diaries, and baby shower planning.
* **Content Nodes**:
  * *Baby Shower Checklist*: Timeline for organizing co-ed baby showers, registry tracking, and host guides.
  * *Bump Photo Diary Guide*: Weekly suggestions for capturing memory pictures safely and beautifully.

---

## ✍️ 2. Option C: Weekly Journal & Notes Logger

### Objective
Allow dads to record private notes, memories, and task reflections directly on the active week chapter.

### UI Blueprint
1. Add a beautiful card in the right-hand **Sidebar** of the week article:
```html
<div class="sidebar-card" style="margin-top:var(--space-6)">
  <div class="sidebar-title">✍️ Dad's Journal</div>
  <p style="font-size:var(--text-sm);margin-bottom:var(--space-3);color:var(--color-text-muted)">
    Record your thoughts, reactions, or specific notes for this week:
  </p>
  <textarea id="week-journal-input" 
            placeholder="How are you feeling? What surprised you this week?" 
            style="width:100%; min-height:100px; padding:var(--space-3); border-radius:var(--radius-md); background:var(--color-bg); border:1px solid var(--color-border); color:var(--color-text); font-family:var(--font-body); font-size:var(--text-sm); resize:vertical;"
            oninput="saveJournalEntry('${data.id}', this.value)"></textarea>
</div>
```

### State Storage & Loading Engine
1. **Saving Logic**:
```javascript
function saveJournalEntry(weekId, text) {
  const saved = JSON.parse(localStorage.getItem('dads-encyclopedia-journals') || '{}');
  saved[weekId] = text;
  localStorage.setItem('dads-encyclopedia-journals', JSON.stringify(saved));
}
```
2. **Loading / Rendering Logic**:
   Inside `renderWeek()`, read the saved journal and pre-populate the text area:
```javascript
function getSavedJournalEntry(weekId) {
  const saved = JSON.parse(localStorage.getItem('dads-encyclopedia-journals') || '{}');
  return saved[weekId] || '';
}
// In renderWeek HTML generation:
// ...
const journalValue = getSavedJournalEntry(data.id);
// ... inject into textarea value ...
```

---

## 🖨️ 3. PDF Export Tool (Print Optimization)

### Objective
Provide dads with a clean, physical copy of their weekly checklists and shopping guides to carry to stores or pin on refrigerators.

### Trigger Mechanism
Add an elegant printer-icon pill/button to the Command Center bar or Header:
```html
<button class="theme-toggle" onclick="window.print()" title="Print Checklist">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <polyline points="6 9 6 2 18 2 18 9"/>
    <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/>
    <rect x="6" y="14" width="12" height="8"/>
  </svg>
</button>
```

### Print Stylesheet Blueprint
Include a dedicated `@media print` query in the `<style>` block:
```css
@media print {
  /* Hide non-essential interactive layout parts */
  .site-header, 
  .theme-toggle, 
  .trimester-band, 
  .site-footer, 
  .sidebar-card:not(:last-child), 
  .mission-tabs, 
  .overview-grid,
  .progress-weeks,
  #week-complete-btn {
    display: none !important;
  }

  /* Reset layout structure for plain paper page flows */
  body {
    background: #fff !important;
    color: #000 !important;
    font-size: 12pt;
  }
  
  .container {
    max-width: 100% !important;
    padding: 0 !important;
  }
  
  .content-layout {
    display: block !important;
  }
  
  .main-content, .sidebar {
    width: 100% !important;
    float: none !important;
  }
  
  .info-card {
    background: none !important;
    border: none !important;
    box-shadow: none !important;
    page-break-inside: avoid;
    padding: 0 !important;
    margin-bottom: 2rem !important;
  }

  /* Make checkboxes print with empty squares and tick marks */
  .check-item {
    border: none !important;
    padding: 4px 0 !important;
  }
  .ci-box {
    border: 1px solid #000 !important;
    background: none !important;
  }
}
```
