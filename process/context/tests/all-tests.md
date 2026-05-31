# First-Time Dad's Pregnancy Encyclopedia - All Tests

Last updated: May 31, 2026

Attach this file first when the task involves testing, verification, or test debugging.

This is the fast operator guide for the testing surface:

- how to run the preview server
- browser manual-verification checklists
- how to quickly debug local storage and routing issues
- what to look out for during verification

---

## How This File Works

This is the `all-tests.md` entrypoint for the `tests/` context group. It follows the `all-*.md` routing convention:

1. Agents read `all-context.md` first and get routed here for testing tasks.
2. This file gives quick decision rules, commands, and verification protocols.
3. For deeper details, agents follow the routing table below to specific docs.

---

## What This Covers

- Development server initialization
- Comprehensive manual browser testing procedures
- Verification of dynamic HSL trimester glows
- LocalStorage state validation
- Theme toggle and mobile responsiveness audit

## Read This When

Use this file when you need to:

- run manual verification protocols on the web page
- verify UI layouts, theme styles, and interactions
- debug local storage state persistence or dynamic rendering logic

---

## Quick Decision Guide

### Use Chrome DevTools / Browser Preview when
- verifying visual consistency, color contrast, and layout responsiveness
- checking dynamic hash updates in the URL bar
- testing the dynamic checkmark completion effects (confetti/checkmark animation)

### Use localStorage inspector when
- verifying checkbox persistence
- validating week completion markers
- clearing state for clean-slate testing

---

## Default Verification Order

Unless the task clearly needs a different path:

1. Start the local preview python web server (`python3 -m http.server 8000`).
2. Navigate to `http://localhost:8000`.
3. Open Developer Tools (F12 or Cmd+Opt+I) to monitor console errors.
4. Perform the interactive checklist actions (theme toggle, week rendering, checkbox toggling).
5. Verify Local Storage state objects inside the Application tab.

---

## Commands

### Serve the App Locally
To serve the static monolithic SPA on port 8000, run:
```bash
python3 -m http.server 8000
```
Then navigate to: `http://localhost:8000`

---

## Manual Browser Verification Checklist

Perform these test cases to verify the integrity and premium user experience of the Pregnancy Encyclopedia:

### 1. Interactive Theme Toggle Test
- **Action**: Click the theme toggle icon (sun/moon) in the top-right header.
- **Expected Results**:
  - The document root `<html>` attribute should toggle between `data-theme="dark"` and `data-theme="light"`.
  - The page background and text colors must transition smoothly.
  - The SVG icon inside the button should dynamically toggle between the Sun (for dark mode) and Moon (for light mode).
  - The preference must persist in localStorage under the `theme` key. Upon reloading the page, the user's selected theme must remain active.

### 2. Hash-Routing & Week Rendering Test
- **Action**: Click on a trimester button in the navigation band, or a specific week dot in the Sidebar grid, or edit the URL hash manually to `#week-12`.
- **Expected Results**:
  - The URL in the address bar must update to match the week key (e.g. `#week-12`).
  - The central container `week-display-container` must render the correct week data from `WEEKS_DATA` without a full page reload.
  - The Trimester Band button corresponding to the rendered week's trimester must become highlighted.
  - The top header nav pill for the active trimester must become highlighted.
  - The Command Center dashboard must immediately update the Phase name (e.g. "FIRST TRIMESTER"), the Week title (e.g. "Week 12"), and the correct baby size estimate (e.g. "Plum").
  - The page must scroll smoothly to the top of the week content container.

### 3. Checklists & Progress Calculation Test
- **Action**: Locate "Dad's Mission Control", click the tabs to switch to the "Practical" panel, and click a checkbox. Then, click "Mark Week as Completed" in the sidebar card.
- **Expected Results**:
  - Clicking a checkbox should instantly toggle the item state visually, add a temporary checkmark celebration micro-animation (`✅`), and persist the value under `dads-encyclopedia-checklists` in localStorage.
  - The Command Center dashboard "Tasks Completed" progress bar must dynamically recalculate the overall progress percentage, adjusting its HSL glow background and label (e.g. "12 / 185 tasks (6%)") on the fly.
  - Clicking "Mark Week as Completed" must update the button text to "✓ Marked as Completed", add the `.completed` class to the button, persist the state under `dads-encyclopedia-completed-weeks` in localStorage, and update the matching dot in the sidebar dot grid to have the `.completed` style instantly.
  - The Command Center "Pregnancy Progress" progress bar must recalculate and update the completed week count (e.g. "5 / 44 weeks (11%)") dynamically.

### 4. Dynamic Trimester Accent & Glow Test
- **Action**: Navigate between Pre-conception (`#week-prep`), Trimester 1 (`#week-4`), Trimester 2 (`#week-16`), Trimester 3 (`#week-30`), and Birth (`#week-birth`).
- **Expected Results**:
  - The header border and progress bar fills in the Command Center must instantly change color matching the current trimester theme:
    - Pre-conception: Blue glow (`--color-prep-accent`)
    - Trimester 1: Yellow glow (`--color-t1-accent`)
    - Trimester 2: Green glow (`--color-t2-accent`)
    - Trimester 3: Purple glow (`--color-t3-accent`)
    - Birth & Beyond: Red glow (`--color-birth-accent`)
  - The week header background must have a smooth vertical gradient starting from the trimester glow color transitioning down to the dark background.

---

## Debugging Quick Reference

- **Clean State Testing**: To reset the app completely for a fresh walkthrough, run this command in the browser Console:
  ```javascript
  localStorage.clear();
  location.reload();
  ```
- **Lucide Icons Not Loading**: Ensure you are online as the app uses `https://unpkg.com/lucide@latest` to pull Lucide. If offline, the icons will fall back gracefully to empty spaces or raw text.
- **Unreachable Hash**: If you enter a hash that does not exist (e.g. `#week-999`), the app will fall back to rendering the default week (`Week 4`).

---

## Known Gaps

- No automated Jest or Playwright test suites are set up. Verification relies entirely on visual audits, console log inspection, and manual testing.
