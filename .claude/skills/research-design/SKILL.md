---
name: research-design
description: Research website designs, full-page templates, and UI components from the live web — including 21st.dev (components), godly.website (full-page inspiration), and open search — screenshot them with Playwright, present the best references for the user to choose from, then adapt the chosen design into the project's vanilla HTML/CSS/JS conventions. Use when the user asks to research designs, find design/template/component inspiration, look at reference sites, or improve a page's look by drawing on other sites.
---

# Research Design

Research good website designs from the live web, **show** the user the best
finds, then rebuild the chosen one in this project's vanilla stack. Works at two
levels, auto-detected from the request:

- **Template mode** — a whole page or layout ("a landing page for a woodworking blog").
- **Component mode** — a single UI piece ("a sticky sidebar with an ad slot", "a pricing table").

## Why screenshots are mandatory

Fetched web pages arrive as raw markup — you cannot *see* them, so you cannot
judge a design from HTML alone. Every candidate must be screenshotted and then
read back as an image. That is the only reliable way to evaluate visual design.

## Workflow

### 1. Pin down the target
Confirm: template or component, what it's for, and which file it will land in
(e.g. `woodworking.html`). One short clarifying question only if genuinely unclear.

### 2. Find 5–8 references
Always start with the two primary galleries — do not skip them:
- **Components** → [21st.dev](https://21st.dev).
- **Full pages / layouts** → [godly.website](https://godly.website).

If the theme genuinely isn't represented there, do not force a poor match — fall
back to a similar curated gallery instead:
- Full-page inspiration: [Land-book](https://land-book.com),
  [Lapa Ninja](https://www.lapa.ninja), [Httpster](https://httpster.net),
  [One Page Love](https://onepagelove.com),
  [siteInspire](https://www.siteinspire.com),
  [Awwwards](https://www.awwwards.com), [Refero](https://refero.design).
- Components: [Tailwind UI](https://tailwindui.com),
  [shadcn/ui](https://ui.shadcn.com), [Aceternity UI](https://ui.aceternity.com),
  [Magic UI](https://magicui.design).

Use open `WebSearch` only as a last resort, after the galleries. Cast a wide net
— the user wants real choice, so collect 5–8 candidate URLs.

### 3. Screenshot every candidate
Use the bundled helper (saves full-page PNGs to a temp dir and prints each path):

```bash
python3 .claude/skills/research-design/scripts/screenshot.py URL1 URL2 URL3 ...
```

Then `Read` each printed path so you can actually see the designs.

### 4. Present a shortlist (inline)
Show the user what you found, one entry each:
- a one-line read of the design (what's strong about it),
- the source link,
- why it's relevant to their target.

Let the user pick. Do **not** silently choose and start building.

### 5. Extract the chosen design
From the screenshot, pull out the concrete spec: layout structure, exact hex
palette, type scale (sizes + weights), spacing rhythm, border radii, shadows,
and the signature pattern that makes it work.

### 6. Adapt into THIS project's stack
Rebuild it as **vanilla HTML/CSS/JS** following `.claude/rules/web.md`:
semantic elements, CSS custom properties for colors/spacing/sizes, `aria-label`s
on interactive elements, `const`/`let` (never `var`), 2-space indent.

- **React is not an option** — this project forbids a build system.
- **Translate, never paste** — 21st.dev components are React+Tailwind; convert
  them to vanilla CSS, do not carry utility classes into the codebase.
- Tailwind-CDN is allowed **only** for a throwaway recreation prototype, per
  web.md's recreation exception — not for components merged into the real site.

### 7. If improving an existing page, run the recreation loop
Follow web.md: screenshot your result with Playwright, `Read` it, compare to the
reference, list every mismatch, fix, and repeat at least 2 rounds until there are
no visible differences. Delete result screenshots afterward — never commit them.

## Rules
- Present **5–8** references — choice over frugality; the user opted into this.
- **Never dump raw fetched HTML into context** — screenshot + a short brief is
  what's useful; the markup is noise.
- Screenshots live in a temp dir and are **never committed**.
- Treat every find as **inspiration**: produce original output in this project's
  style, never lift a design wholesale.

## Output
1. A presented shortlist of 5–8 screenshotted references with links.
2. The user's chosen design, rebuilt in vanilla HTML/CSS/JS to project conventions.
