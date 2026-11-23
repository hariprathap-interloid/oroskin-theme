---
description: Oroskin theme only. Review one section until it is "done" (bugs, editor labels in ASD-STE100, responsive, accessibility, cleanup, code review, CLAUDE.md, commit commands)
argument-hint: <section name, e.g. Blog stories>
---

Review the "$ARGUMENTS" section of the Oroskin theme: find its file in `sections/` (match the
schema name or the file name), plus its blocks and snippets.

If `$ARGUMENTS` is empty, ask me which section to review, and stop.

Work one phase at a time. Stop after phase 1 and wait for my answers.
Write all replies and editor labels in ASD-STE100. Deadline mode: you draft, I test.

## Phase 1: review (no edits yet)

List bugs and best-practice issues, grouped and ranked:
- **Features:** test that every setting and block works (also empty / blank values, 1 item,
  max items, placeholders without content).
- **JS:** listeners on one AbortController (editor re-attach), reduced motion, no-JS /
  `:not(:defined)` state, no duplicate work after a re-attach.
- **Performance:** image loading (`section-loading` snippet, LCP never lazy), `sizes` computed
  from the settings, no CSS math that old browsers drop (`mod()`/`round()`) when Liquid can
  compute it.
- **Responsive:** phones < 750px, tablets 750–1199px, desktop ≥ 1200px. Check overflow,
  clipping, overlap. If the design for a size is missing, ASK me before you design it (I can
  give screenshots).
- **Accessibility:** names for links and buttons, keyboard and focus-visible order, correct ARIA
  (no fake toggles), alt text, headings, contrast (log only, decide in M9).
- **Editor:** the section name (one name everywhere, named by what it does, not by its content),
  and labels and help text that are not clear.

Ask me about anything in the design that is not clear.

## Phase 2: fix (after my answers)

- Fix the agreed items.
- **Settings:** regroup in this order: Content / Products or Blocks / Layout / Phones / Tablets /
  feature groups / Animation / Spacing / Colors (last). Labels and info in ASD-STE100.
  - Keep every setting id (saved values).
  - Do not change shared label keys: add new `<section>_*` keys.
  - A setting that depends on another: `visible_if` + info that names the other setting.
  - Highlight color: no default (empty = the scheme's accent).
- **CSS cleanup:** remove unused, duplicate and leftover rules.
- **Test:** in the browser at 390 / 820 / 1280px (`iframe srcdoc`), Theme Check clean, all `t:`
  keys exist.

## Phase 3: finish

- I run `/code-review`, then you fix the findings I choose.
- Update CLAUDE.md: "<section>: reviewed and done" + Open items + Next section (homepage order
  in `templates/index.json`).
- Give the `git add` / `commit` / `push` commands (the same for Git Bash, PowerShell and cmd).
  Do not commit. No co-author line.
