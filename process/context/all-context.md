# First-Time Dad's Pregnancy Encyclopedia - All Context

Last updated: May 31, 2026

This file is the root context entrypoint for the repo.

Use it for two things:

1. quick routing to the right context pack or root file
2. broad architecture and repository understanding

Start here before loading deeper context files.

---

## How This File Works (the `all-*.md` Convention)

Every `process/context/` directory has one `all-*.md` entrypoint that acts as an attachable quick router for that domain. This root file (`all-context.md`) is the top-level router. Context groups each have their own `all-{group}.md` entrypoint.

**The pattern:**

```
process/context/
  all-context.md                      <-- THIS FILE: root router
  tests/
    all-tests.md                      <-- group router for tests
```

**How agents use it:**

1. Agent reads `all-context.md` first (this file)
2. Finds the relevant context group from the routing tables below
3. Reads that group's `all-{group}.md` entrypoint (e.g., `tests/all-tests.md`)
4. Only then loads the specific deep doc needed

This layered routing keeps context windows small. Never load the whole `process/context/` tree.

---

## Quick Start

For most substantial tasks:

1. read this file first
2. choose the smallest relevant root file or context group from the tables below
3. only then load deeper files

---

## Current Root Entry Points

| File | Read when |
|---|---|
| `process/context/all-context.md` | any substantial planning, research, review, or implementation task |
| `process/context/tests/all-tests.md` | testing, verification, debugging test failures, execution planning |

## Current Context Groups

| Group | Entry point | Scope |
|---|---|---|
| `tests/` | `process/context/tests/all-tests.md` | Manual browser test scripts, progress and trimester glow checklists, Local Storage validation, layout verification |

## Task Routing Table

| If the task involves... | Start with | Then load |
|---|---|---|
| general repo research | `all-context.md` | `index.html` or relevant assets/data |
| testing or verification | `all-context.md` | `process/context/tests/all-tests.md` |
| UI/UX modifications | `all-context.md` | `<style>` block in `index.html` |
| functional script adjustments | `all-context.md` | `<script>` block in `index.html` |

## Context Group Lifecycle

Context groups are durable knowledge domains, not feature folders.

Create a group when:

- a topic has 3+ durable docs
- a single doc exceeds roughly 800 lines with separable subtopics
- multiple agents repeatedly need only one slice of a large context file
- the topic maps to a stable operational domain (tests, infra, database, auth, UI, workflows, etc.)

Do not create a group when:

- the content is a temporary report
- the content is a plan or execution artifact
- the topic is feature-specific and belongs in `process/features/...`

Move or split one group at a time. Use `all-{group}.md` entrypoints.

## Naming Convention

There are no `README.md` files inside `process/context/`.

Canonical entrypoints use `all-*.md`:

- root: `process/context/all-context.md`
- group: `process/context/{group}/all-{group}.md`

Each `all-{group}.md` file should act as the attachable quick router for that domain:

- tell the agent what the group covers
- give quick procedures and decision rules
- route to smaller deeper files

## Context Update Protocol

When durable project knowledge changes:

1. update the smallest relevant context file
2. update this file if routing, ownership, naming, or groups changed
3. update the owning `all-{group}.md` entrypoint when a group exists

---

## Repository Structure

```
dads-encyclopedia/
  .agents/            -- Agent profiles and skills
  .claude/            -- Claude Code configuration and scripts
  .codex/             -- Codex metadata
  .github/            -- GitHub Actions workflows
  .scripts/           -- Shell and Python helper scripts
  assets/             -- Images, SVGs, and other media
  data/               -- JSON weekly data batches (batch_1.json to batch_4.json)
  process/            -- operational workspace (harness)
    context/          -- durable project knowledge
      tests/          -- testing and verification
    development-protocols/ -- standards and protocols
    features/         -- feature-scoped storage
    general-plans/    -- cross-cutting plans
  prompt-library/     -- Prompts and templates for AI generation
  index.html          -- Premium Dark-First default Monolithic SPA (main entry point)
  app.js              -- Milestone 1 interactions (unused or historical)
  styles.css          -- Milestone 1 design system (unused or historical)
```

## Technology Stack

- **Architecture:** Monolithic Single Page Application (SPA), completely serverless, zero external network dependencies (except for web font hosting and Lucide CDN).
- **Styling:** Premium Vanilla CSS inside a single `<style>` block in `index.html`. Uses dynamic Custom Properties (CSS variables) for real-time light/dark theme switching, responsive typography (clamped values), HSL trimester glows, backdrop blur filters, and CSS transitions.
- **Typography:** Satoshi (sans-serif body), Cabinet Grotesk (display headings), and Instrument Serif (italicized accent font).
- **Icons:** Lucide Icons, dynamically resolved using `lucide.js`.
- **Data Layer:** Massive local dynamic dictionary `WEEKS_DATA` loaded inside `<script>`, covering weeks Pre-conception ("prep"), Weeks 1-42, and Birth ("birth").
- **State Management & Persistence:** LocalStorage-based caching system:
  - `dads-encyclopedia-checklists`: Key-value map of checked practical/mustBuy/optionalBuy items (Key: `${weekId}-${type}-${index}`)
  - `dads-encyclopedia-completed-weeks`: Key-value map of completed weeks (Key: `${weekId}`)
  - `theme`: Active color theme ('light' or 'dark')
- **Routing Engine:** Pure Vanilla JS hash-routing listener (`#week-{id}`) that maps dynamically to the `renderWeek()` method without full-page reloads.

## Key Patterns and Conventions

**DOM Manipulation:**
Dynamic, template-literal based rendering in Javascript (`renderWeek()`) that safely constructs the DOM structure on the fly from `WEEKS_DATA` dictionary records.

**Dynamic Trimester Color Theme Glows:**
Trimester-specific styling variables (e.g. `--color-t1`, `--color-t2`, etc.) are mapped to HSL values. In `calculateOverallProgress()`, Javascript reads the active article's trimester and dynamically applies glow borders and progress bar fills matching the active trimester theme.

**Local Storage Schema:**
- Checklist: `{"prep-practical-0": true, "week-4-mustBuy-1": true}`
- Completed Weeks: `{"prep": true, "4": true}`

**Naming:**
kebab-case for folder names and DOM IDs (`week-display-container`, `week-complete-btn`); camelCase for functional Javascript variables and methods (`renderWeek`, `toggleCheckItem`).

## Environment and Configuration

- **Development Port:** Local web server serves on `http://localhost:8000`.
- **Configuration Files:** `index.html` is the absolute configuration and execution source. No bundler or build configs are required.

## Scan Metadata

- Generated: 2026-05-31
- HEAD: 9ccf1cf
- Mode: Vanilla HTML5 / SPA Monolith
- Package manager: None (Static SPA served directly)
