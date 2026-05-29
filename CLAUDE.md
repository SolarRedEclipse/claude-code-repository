# CLAUDE.md

This file provides authoritative guidance to Claude Code when working in this repository. All instructions here take precedence over Claude's default behaviors. Read this file in full before taking any action.

---

## Project Overview

This is a client-side web application built with vanilla HTML, CSS, and JavaScript. There are no build tools, no package managers, and no server-side dependencies. Every feature runs directly in the browser.

- **Stack:** HTML5, CSS3, Vanilla JavaScript (ES6+)
- **Entry point:** `index.html` (or the primary `.html` file in the root)
- **Deployment:** Static file hosting (no build step required)

---

## Repository Structure

```
/
├── CLAUDE.md              # This file — AI instructions
├── .claude/               # Claude Code configuration
│   └── settings.local.json
├── *.html                 # Application pages
├── *.css                  # Stylesheets (if separated)
└── *.js                   # JavaScript modules (if separated)
```

Keep the structure flat and simple. Do not introduce folders, frameworks, or build systems unless the user explicitly requests it.

---

## Git Workflow

Always commit and push after every meaningful change. Follow this exact sequence:

```bash
git add <specific-file>
git commit -m "Imperative-mood message here"
git push
```

### Commit Message Rules

- Use the **imperative mood**: `Add`, `Fix`, `Remove`, `Update`, `Refactor` — not `Added`, `Fixes`, `Removing`
- Be specific and concise: describe *what changed*, not *why* (the diff shows what; the message provides context)
- Keep the subject line under 72 characters
- Do **not** use generic messages like `Update files` or `Fix stuff`

**Good examples:**
```
Add keyboard shortcut for backspace
Fix division by zero display error
Remove unused CSS variables
Refactor button click handler into named function
```

### Branching

- `main` is the production branch — always keep it stable and deployable
- For experimental features, create a short-lived branch: `git checkout -b feature/description`
- Merge back to `main` via a clean commit once the feature is complete

---

## Code Style & Conventions

### General

- Prefer **readability over cleverness** — code is read far more than it is written
- Use **2-space indentation** consistently across all file types
- Always use **double quotes** for HTML attributes and **single quotes** for JavaScript strings
- End every file with a **single trailing newline**
- Remove all **console.log** statements before committing

### HTML

- Use semantic elements: `<main>`, `<section>`, `<article>`, `<nav>`, `<button>` — avoid `<div>` soup
- Every interactive element must have an accessible `aria-label` or visible label
- Boolean attributes written without values: `disabled`, `required`, not `disabled="true"`
- Keep inline styles to zero; all styling belongs in CSS

### CSS

- Use **CSS custom properties** (`--var-name`) for colors, spacing, and font sizes
- Organize rules in this order: layout → box model → typography → visual → animation
- Use `rem` for font sizes, `px` for borders, `%` or `fr` for layout widths
- Avoid `!important` — if you need it, the selector structure is wrong

### JavaScript

- Use `const` by default; use `let` only when reassignment is needed; never use `var`
- Use **arrow functions** for callbacks; use **named functions** for top-level declarations
- Prefer `addEventListener` over inline `onclick` HTML attributes
- Keep functions small and single-purpose — if a function needs a comment to explain what it does, consider splitting it
- **No external libraries or CDN imports** unless explicitly approved by the user

---

## Testing & Verification

Since this project has no test framework, verification is done manually in the browser:

1. Open the HTML file directly in a browser (`open index.html` or equivalent)
2. Test the **golden path** — the primary intended use case
3. Test **edge cases**: empty input, very large numbers, rapid repeated clicks, keyboard-only navigation
4. Check the browser **console** for errors (`F12` → Console tab) — it must be clean
5. Verify in at least one Chromium-based browser (Chrome, Edge, or Brave)

Report any console errors as bugs before marking a task complete. Do not claim a feature works without manually testing it.

---

## Development Commands

```bash
# Open the app in the default browser (macOS)
open index.html

# Check git status
git status

# Stage a specific file
git add <filename>

# Commit with message
git commit -m "Your message here"

# Push to remote
git push

# View recent history
git log --oneline -10
```

---

## What Claude Should Never Do

- **Do not introduce a build system** (Webpack, Vite, Parcel, etc.) unless explicitly asked
- **Do not add npm / package.json** unless explicitly asked
- **Do not add CSS frameworks** (Bootstrap, Tailwind, etc.) unless explicitly asked
- **Do not add JavaScript frameworks** (React, Vue, etc.) unless explicitly asked
- **Do not add comments** that merely restate what the code does — only comment on *why* when genuinely non-obvious
- **Do not use `git add .` or `git add -A`** — always stage specific files by name to avoid committing unintended files
- **Do not amend published commits** — create a new commit instead
- **Do not skip pre-commit hooks** (`--no-verify`)
- **Do not push to `main` with `--force`**

---

## Gotchas & Project-Specific Notes

- `calculator.html` was the original entry point — check git log if referencing prior state
- `.DS_Store` files are untracked and should never be committed — they are macOS metadata
- The `.claude/settings.local.json` file contains local permission settings and should not be committed to a shared remote

---

## Tone & Collaboration

- Be **concise** in responses — avoid restating what was just done
- When asked an open-ended question ("what should we do?"), give a **recommendation with the key tradeoff** in 2–3 sentences, then wait for approval before implementing
- When a task is ambiguous, **ask one clarifying question** rather than making assumptions
- Prefer **editing existing files** over creating new ones
- Do not add features, abstractions, or refactors beyond what was explicitly requested
