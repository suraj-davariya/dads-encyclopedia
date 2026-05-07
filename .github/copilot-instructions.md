# First-Time Dad's Pregnancy Encyclopedia - Copilot & AI Instructions

## 📚 Project Overview
This project is a comprehensive, modern, and actionable pregnancy guide for first-time fathers. It provides week-by-week guidance, expert tips, financial planning, and relationship support. The entire project is self-contained in a monolithic HTML structure (`index.html`) with a unified design system (`styles.css`).

## 🎯 Primary Directives
1. **Follow the Master Prompt**: All AI assistants MUST consult and strictly follow the roadmap, guidelines, and tone defined in `prompt-library/master-prompt.md`.
2. **Template Adherence**: When generating new weekly chapters, you MUST use the exact structure defined in `prompt-library/weekly-template.md`. Do not invent new sections or omit existing ones.
3. **Verified Sources Only**: Any medical, financial, or expert advice must align with the tone of the verified resources listed in `prompt-library/source-library.md`.

## 🎨 HTML & CSS Guidelines
- **Structure**: All content is built within the `index.html` monolithic file. New weeks are added as `<article id="week-X">` segments.
- **Styling**: Do not write inline styles unless absolutely necessary. Use the established utility classes and OKLCH color tokens from `styles.css`.
- **Interactivity**: Use the established tab functions (`switchTab`), checklist toggles (`toggleCheck`), and scroll-tracking in `app.js`.

## ✍️ Tone and Voice
- **Empathetic & Actionable**: Dads need to know *what to do* and *how to help*. Keep the tone warm, modern, and inclusive.
- **No Medical Jargon without Explanation**: If you use a medical term (like "nuchal translucency"), explain it in plain English.
- **Humor**: Keep it light but respectful. Dad jokes are welcome, but never at the expense of the partner's comfort or the seriousness of the pregnancy.

## 🚀 Git Commit Guidelines (Gitmoji)
Whenever you write or suggest a git commit message, you **MUST** include MULTIPLE gitmojis that accurately reflect the changes made. Use them liberally to create highly visual and expressive commit history.

Examples of multiple gitmoji usage:
- `✨ 📝 ✨ Add Week 6 chapter and update timeline roadmap`
- `🐛 💄 🚑 Fix broken flexbox layout in mission control tabs`
- `♻️ 🎨 🏗️ Refactor CSS color tokens to OKLCH for better dark mode support`
- `✅ 🧪 🩺 Add tests for HTML validation and fix missing aria-labels`

**Common Gitmojis to use:**
- ✨ `:sparkles:` - New features
- 🐛 `:bug:` - Bug fixes
- 📝 `:memo:` - Documentation updates
- 💄 `:lipstick:` - UI/CSS changes
- ♻️ `:recycle:` - Refactoring code
- 🏗️ `:building_construction:` - Architectural changes
- 🎨 `:art:` - Improving structure/format
- 🚀 `:rocket:` - Deployment or significant milestones
- 🤢 `:nauseated_face:` - Adding morning sickness content (Week 5+)
- 👶 `:baby:` - Adding baby development content

## 🛠️ Typical Workflow for Adding a New Week
1. Consult `prompt-library/weekly-template.md` and copy its structure.
2. Draft the content focusing on Dad's Mission Control, Partner's Journey, and Baby Development.
3. Inject the content into `index.html` inside a new `<article id="week-X">`.
4. Update the sidebar progress tracker.
5. Update the navigation links in the `index.html` trimester navigation block.
6. Check off the week in `prompt-library/master-prompt.md` roadmap.
7. Commit changes with **multiple gitmojis**! (e.g., `✨ 👶 📝 Add Week 6 content and update index links`)
