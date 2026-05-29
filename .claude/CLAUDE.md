# CLAUDE.md

Project-specific rules for this repository. Global rules (git workflow, irreversible actions, tone) are defined in ~/.claude/CLAUDE.md and apply here automatically.

---

## Project Overview

This repository contains two distinct types of work:

1. **Client-side web app** — Built with vanilla HTML, CSS, and JavaScript. Runs directly in the browser with no build tools or server-side dependencies.
2. **Python API endpoints for n8n** — Modal-deployed Python functions that serve as HTTP endpoints consumed by n8n workflows.

Treat these as separate contexts. Rules that apply to one do not necessarily apply to the other.

---

## Repository Structure

```
/
├── .claude/
│   ├── CLAUDE.md                  # This file — project AI instructions
│   ├── rules/
│   │   ├── modal.md               # Modal patterns (loads for *.py only)
│   │   └── web.md                 # Web style + ads + design recreation (loads for *.html/css/js only)
│   └── settings.local.json        # Local permissions (do not commit)
├── modal_app.py                   # Main Modal deployment file
├── .env                           # Local secrets (gitignored — never commit)
├── .env.example                   # Safe template for .env
├── *.html / *.css / *.js          # Web app files
```

Keep the structure flat. Do not introduce new folders unless explicitly requested.

---

## General Code Style

- Prefer **readability over cleverness**
- 2-space indentation for HTML/CSS/JS; 4-space for Python
- End every file with a **single trailing newline**
- Remove all debug `print` / `console.log` before committing
- No comments that restate what the code does — only comment on *why* when genuinely non-obvious

---

## What Claude Should Never Do

- **Do not introduce a build system** (Webpack, Vite, Parcel, etc.) for the web app
- **Do not add npm / package.json** for the web app unless explicitly asked
- **Do not add CSS or JS frameworks** to the web app — Tailwind via CDN is permitted for design recreation only
- **Do not deploy a Modal endpoint without Bearer token auth** — no exceptions
- **Do not use raw `dict` for Modal endpoint inputs** — always use Pydantic models

---

## Gotchas

- `woodworking.html` is the current web app entry point
- `.DS_Store` — never commit
- `.claude/settings.local.json` — never commit
- `.env` — never commit; use `.env.example` as the safe template
- Rotating `api-auth-token` immediately breaks all n8n workflows — treat as irreversible

---

## Scoped Rules (auto-loaded by file type)

@rules/modal.md
@rules/web.md
