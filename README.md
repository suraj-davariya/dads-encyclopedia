# 🍼 Ultimate First-Time Dad's Pregnancy Encyclopedia

> **The ultimate, no-BS, action-oriented week-by-week pregnancy companion for modern fathers-to-be.**
> 
> *Because "just be supportive" isn't a strategy. You need a mission control.* 🚀

<div align="center">

[![Live Demo](https://img.shields.io/badge/⚡%20LIVE%20DEMO-🚀%20Launch%20Mission%20Control-ff6a1a?style=for-the-badge&logo=rocket)](https://suraj-davariya.github.io/dads-encyclopedia/)

[![Version](https://img.shields.io/badge/version-1.1--stable-blue.svg?style=flat-square&logo=git)](https://suraj-davariya.github.io/dads-encyclopedia/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://suraj-davariya.github.io/dads-encyclopedia/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](https://suraj-davariya.github.io/dads-encyclopedia/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://suraj-davariya.github.io/dads-encyclopedia/)

[⚡ Live Demo](https://suraj-davariya.github.io/dads-encyclopedia/) • [🛠️ Architecture](#-monolithic-architecture) • [🗺️ Roadmap](#-roadmap-completed-milestones) • [📦 Quick Start](#-quick-start-local-development)

</div>

***

> [!CAUTION]
> ### ⚠️ MEDICAL DISCLAIMER & CAUTION
> **THIS APPLICATION IS NOT MEDICAL ADVICE.** The content, checklists, symptom decoders, and clinical references provided in this pregnancy encyclopedia are for **educational and supportive purposes only**. They are designed exclusively to help first-time fathers understand the pregnancy journey and better support their partners. 
> 
> **For any medical concerns, symptoms, or health questions, always consult a licensed doctor, OB-GYN, midwife, or qualified healthcare professional immediately.** Never disregard professional medical advice or delay seeking it because of something read in this guide. The creator and contributors of this application assume no liability for medical decisions made based on this software.

***

Welcome to the **Ultimate First-Time Dad's Pregnancy Encyclopedia**. We took the overwhelming mountain of standard pregnancy information and distilled it into an actionable, premium week-by-week playbook specifically designed for Dads. No dry medical jargon. No panic. Just exactly what you need to know, what you need to buy, and what you need to do right now to step up as the ultimate partner.

***

## 🌟 Premium Interactive Features

### ⏱️ Labor Contraction Timer Coach
* **Automated 5-1-1 Analysis**: Real-time labor coach stopwatch that calculates contraction durations and intervals.
* **Clinical Phase Coaching**: Displays actionable advice based on clinical milestones (Early 🏠, Active Labor 🚨, Transition 🤰).
* **Zero Data Loss**: Automatically saves timing histories to persistent local storage so active logs are never lost.

### ✍️ Dad's Weekly Journal & Compiler
* **Mood Tracking**: Quick weekly energy and emotional check-in buttons (Exhausted, Excited, Overwhelmed).
* **Trimester Reflections**: Custom, reflective prompts designed for every specific trimester milestone.
* **Dad Wins & Timeline**: Log achievements and view your entire pregnancy diary in a beautiful interactive timeline modal (printable and exportable as JSON!).

### 🖨️ PDF & Ink-Saving Print Engine
* **Checks Isolation**: High-contrast, clean `@media print` stylesheets.
* **Isolated Lists**: Generate and print *only* the checklists (must-buys and dad tasks) with one click, perfect for sticking on the fridge or clipboard.

### 🎨 High-Fidelity UI/UX & Micro-Animations
* Staggered fade-in cards (`@keyframes slideUpFade`) creating a premium digital experience.
* Satined blurs (`backdrop-filter: blur(18px) saturate(180%)`) and beautiful glassmorphism.
* Trimester-coded sidebar progress dots with an active, breathing pulsating glow.

***

## 🧬 Monolithic Architecture

This project is engineered to be portable, lightweight, and incredibly fast:
* **The Monolith**: 100% self-contained in a single `index.html` structure. It loads instantly and runs entirely on the client side.
* **Design System**: Tailored HSL color variables (`styles.css`) for seamless Dark and Light theme scaling.
* **Persistent Storage**: Namespace-locked engines (`dads-encyclopedia-*`) that protect check items, journals, and contraction logs.
* **Zero Compilation**: Zero frameworks, zero dependencies, and no node_modules required.

```text
dads-encyclopedia/
├── prompt-library/          # 🤖 Spec-driven prompt assets and roadmap definitions
├── styles.css               # 💅 Premium CSS variables, color tokens, and custom keyframes
└── index.html               # 🌐 Monolithic application & client-side javascript engine
```

***

## 🗺️ Roadmap & Completed Milestones

We are systematically completing the pregnancy roadmap. Check our current progress below:

- [x] **Foundation Setup:** Weeks 1–4 + Pre-Conception (`prep` chapter)
- [x] **First Trimester:** Weeks 5–13 (Morning sickness, genetic screens, Week 12 Placenta Transitions)
- [x] **Second Trimester:** Weeks 14–27 (Ultrasounds, anatomy check-ins, Week 20 Halfway mark)
- [x] **Third Trimester Begins:** Weeks 28–32 (Week 28 RhoGAM, pediatrician prep, kick counts)
- [x] **Late Stage Ready:** Weeks 33–36 (Week 36 Nesting, GBS tests, car seat installation checks)
- [ ] **Phase 4 (Birth & Beyond):** Labor, Delivery, and Postpartum Month 1
- [x] **Labor Contraction Timer Coach Widget** (100% complete)
- [x] **Weekly Journal & Compiled Diary Timeline** (100% complete)

***

## 🚀 Quick Start (Local Development)

Launch your local pregnancy command center in seconds:

### 1. Launch a Local Server
For optimal browser security, local storage access, and resource isolation, run a simple local server:
```bash
# Python 3 local server
python3 -m http.server 8000
```

### 2. Open in Your Browser
Open your browser and navigate to:
```text
http://localhost:8000
```

***

## 🏷️ Version Control (Gitmoji Master Rule)
We follow strict version control guidelines. Every commit must combine multiple git emojis to keep our history visual and readable:
* `✨ 👶 📝` Add Week 36 milestones and update roadmap checklist
* `🐛 💄 🚑` Fix flexbox rendering bugs and update layout alignments
* `♻️ 🎨 🏗️` Refactor trimester variable color tokens for glowing highlights

***

<div align="center">
  <i>Built with ❤️, excessive caffeine, and minimal sleep for first-time dads everywhere.</i>
</div>