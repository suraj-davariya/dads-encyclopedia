# Contributing to the First-Time Dad's Pregnancy Encyclopedia

Welcome! Whether you're a human contributor or an AI agent, we're thrilled you're helping build the most comprehensive, modern, and actionable pregnancy guide for first-time fathers.

## 🎯 The Core Philosophy
This encyclopedia is designed to be **empathetic, actionable, and strictly evidence-based**. Dads need to know *what is happening*, *what their partner needs*, and *what exact actions to take*. We avoid fluff and focus on utility.

---

## 📚 Project Architecture

This is a monolithic, frontend-only project:
- `index.html`: The entire application lives here. Each weekly chapter is an `<article>` tag.
- `styles.css`: The design system utilizing OKLCH color tokens and utility classes.
- `app.js`: Lightweight vanilla JavaScript for interactive elements (tabs, checklists, theme toggles).
- `prompt-library/`: The single source of truth for the project roadmap, templates, and verified sources.

---

## 🛠️ Workflow for Adding a New Week

If you are adding a new weekly chapter, you **MUST** follow this exact flow:

### 1. Template Adherence
Open `prompt-library/weekly-template.md`. **Do not deviate from this structure.** Every weekly chapter must include:
- Baby's Development (with size comparison)
- Partner's Journey (symptoms and empathy)
- Dad's Mission Control (Emotional, Practical, Relationship tabs)
- Prenatal Bonding Lab
- Shopping & Prep Checklist
- Medical Roadmap
- Weekly Challenge
- Expert Tips Carousel
- Quick Reference Cards
- SEO and Social Snippets

### 2. Injecting into HTML
Draft the content based on the template, then translate it into HTML using the exact same class structure as the existing chapters (e.g., `Week 4` and `Week 5`).
Insert the new `<article id="week-X">` into `index.html` in chronological order.

### 3. Update the UI Components
- Update the **Sidebar Progress Tracker** inside your new week's HTML block to show the current week as active.
- Update the **Trimester Navigation** block at the top of `index.html` to link to your new week (`<a href="#week-X">`).

### 4. Roadmap Verification
Once complete, open `prompt-library/master-prompt.md` and check off the week in the Build Roadmap section (`- [x]`).

---

## 🎨 Design System Guidelines
- **Do not use inline styles** unless absolutely necessary.
- **Color Themes**: Use our pre-defined CSS variables. Trimesters are color-coded:
  - First Trimester: `--t1-primary`
  - Second Trimester: `--t2-primary`
  - Third Trimester: `--t3-primary`
  - Birth: `--birth-primary`
- Ensure all new elements are fully responsive (test on mobile widths).

---

## 🚀 Git Commit Guidelines

We use highly expressive **Gitmoji** commits. Every commit message **MUST** include multiple gitmojis that accurately describe the changes. 

**Format:**
`<gitmoji 1> <gitmoji 2> <gitmoji 3> Commit message here`

**Examples:**
- `✨ 👶 📝 Add Week 6 chapter and update timeline roadmap`
- `🐛 💄 🚑 Fix broken flexbox layout in mission control tabs`
- `♻️ 🎨 🏗️ Refactor CSS color tokens to OKLCH for better dark mode support`

**If you are an AI agent making a commit on behalf of the user, you must strictly follow this multiple-gitmoji rule.**

---

Thank you for contributing! Let's build something great for dads everywhere.
