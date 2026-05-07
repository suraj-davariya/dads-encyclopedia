<div align="center">
  <img src="assets/logo-placeholder.png" alt="Dads Encyclopedia Logo" width="200"/>
  
  # 🍼 Ultimate First-Time Dad's Pregnancy Encyclopedia
  
  **The comprehensive, no-BS, action-oriented survival guide for modern fathers-to-be.**

  [![Version](https://img.shields.io/badge/version-1.0-blue.svg?style=for-the-badge&logo=appveyor)](https://github.com/your-username/dads-encyclopedia)
  [![Status](https://img.shields.io/badge/status-active-success.svg?style=for-the-badge)](https://github.com/your-username/dads-encyclopedia)
  [![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://github.com/your-username/dads-encyclopedia)
  [![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://github.com/your-username/dads-encyclopedia)
  [![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://github.com/your-username/dads-encyclopedia)
  
  [Live Demo](#) • [Installation](#-quick-start) • [Roadmap](#-roadmap) • [Contributing](CONTRIBUTING.md)
</div>

<br/>

> *"Because 'just be supportive' isn't a strategy. You need a mission control."* 🚀

Welcome to the **Ultimate First-Time Dad's Pregnancy Encyclopedia**. We took the massive, overwhelming mountain of pregnancy information and distilled it into an actionable, week-by-week playbook specifically designed for Dads. No jargon. No panic. Just exactly what you need to know, what you need to buy, and what you need to do right now.

---

## ✨ Features (Why This Rules)

- 📅 **40-Week Interactive Tracker:** A seamless, single-page experience covering pre-conception all the way to birth.
- 🦸‍♂️ **Dad's Mission Control:** Stop guessing. Get exact, tabbed checklists for **Emotional**, **Practical**, and **Relationship** tasks every single week.
- 🤰 **Partner Symptom Decoder:** Understand exactly what she's going through physically and emotionally, complete with the "Why it's happening" and "How you can help."
- 🛒 **The "No-Regrets" Shopping List:** Weekly breakdowns of must-haves and nice-to-haves. Skip the marketing fluff and buy what actually matters.
- 🧠 **Prenatal Bonding Lab:** Specific scripts, playlists, and challenges to start bonding with your baby before they even arrive.
- 🎨 **Premium UI/UX:** Built with a bespoke OKLCH color design system. It looks like a million bucks, works flawlessly on mobile, and features smooth trimester color transitions.

---

## 🏗️ Architecture & Tech Stack

This project is built for performance and absolute simplicity:
- **Frontend:** Pure Vanilla HTML5, CSS3 (using OKLCH design tokens), and ES6+ JavaScript.
- **Zero Dependencies:** No frameworks, no build steps, no complex setup. Just standard web technologies.
- **Mobile First:** Highly optimized for mobile devices with a fluid design system.

---

## 📂 Project Structure

```text
dads-encyclopedia/
├── assets/                  # 🖼️ Static assets (images, icons)
├── data/                    # 🗃️ JSON data batches for each week
│   └── batch_*.json         # Contains medically accurate milestone content
├── prompt-library/          # 🤖 AI prompts, architecture notes, and AI agent roles
├── app.js                   # ⚙️ Client-side interactivity (Tabs, Theme Toggles)
├── styles.css               # 💅 Premium design system and OKLCH color tokens
├── index.html               # 🌐 The generated production-ready application
└── CONTRIBUTING.md          # 🤝 Guidelines for joining the dad squad
```

---

## 🚀 Quick Start (Local Development)

Ready to contribute or run your own instance? It takes less than 2 minutes.

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/dads-encyclopedia.git
cd dads-encyclopedia
```

### 2. Make Content Updates
All the heavy lifting is in the `data/` folder. Modify or create a new `batch_X.json` file. Follow the template found in `prompt-library/weekly-template.md`.

### 3. Open and Explore
Simply open `index.html` in your web browser to start using the encyclopedia. For the best experience, including smooth navigation and saved progress, we recommend using a simple local server.

### 4. Launch Mission Control
Use any local server to test the UI (or simply double-click `index.html`):
```bash
# Example using npx (if you have Node.js)
npx serve .
```
Open [http://localhost:8000](http://localhost:8000) in your browser. 

---

## 🗺️ Roadmap

We are currently building out the 40-week masterplan. Track our progress below:

- [x] **Foundation:** Weeks 1–4 + Pre-Conception
- [x] **Phase 1 (First Trimester):** Weeks 5–13 (Morning sickness peak, first ultrasound)
- [ ] **Phase 2 (Second Trimester):** Weeks 14–27 (Anatomy scan, first kicks)
- [ ] **Phase 3 (Third Trimester):** Weeks 28–40+ (Birth plan, hospital bags)
- [ ] **Phase 4 (Birth & Beyond):** Labor, Delivery, and Month 1

---

## 🏷️ Commit Guidelines (Gitmoji Master Rule)

We take our version control seriously. You **MUST** use multiple [gitmojis](https://gitmoji.dev/) for every commit to keep our history highly visual and expressive. 

**Examples:**
- `✨ 👶 📝 Add Week 6 chapter and update timeline roadmap`
- `🐛 💄 🚑 Fix broken flexbox layout in mission control tabs`
- `♻️ 🎨 🏗️ Refactor CSS color tokens to OKLCH for dark mode`

See `.cursorrules` for full details.

---

## 🤝 Contributing

Dads help dads. Whether you're an OB-GYN, a frontend wizard, or a veteran dad with a solid tip on diaper genies—we want your PRs. Check out the [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

<br/>

<div align="center">
  <i>Built with ❤️, cold coffee, and minimal sleep for first-time dads everywhere.</i>
</div>