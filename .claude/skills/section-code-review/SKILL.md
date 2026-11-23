---
name: section-code-review
description: Oroskin theme only. Code review of ONE section or ONE page (its section files, their blocks and the snippets they render), not the whole diff or the whole codebase. Finds bugs with proof, ranks them, waits for the user's choice, then fixes and tests.
disable-model-invocation: true
argument-hint: "<section or page, e.g. faq | Contact page | sections/blog.liquid> [changes | full]"
---

# /section-code-review: review one section or page

**Input:** $ARGUMENTS

If the input is empty, ask which section or page to review, and stop.
Write all replies in ASD-STE100. Do not commit. No co-author line.

## 1. Find the scope (only these files)

1. **Page name** (e.g. "Contact page", "FAQ"): read `templates/<page>.json` (or `page.<name>.json`) and
   take every section `type` in it. **Section name**: match the file name in `sections/` or the
   schema `name` (its `t:general.*` value in `locales/en.default.schema.json`).
2. For each section file, add:
   - its blocks: the schema `blocks` types that start with `_` and every `content_for 'block', type:`;
   - its snippets: every `{% render '...' %}` (one level deep, plus snippets those render when they
     are only used by this section);
   - the template JSON when it is a page.
3. **Shared files** (a snippet or block that other sections also use, e.g. `faq-contact`,
   `quick-add`, `section-loading`, `image`): review only the parts this section uses, and list the
   other users (grep) so a change there is not a surprise.
4. **Mode** (second word of the input):
   - `changes` (default when the scope has uncommitted changes): review the `git diff` of the
     scope files, and read each changed file in full for context.
   - `full` (default when there are no changes): review the full files.
5. Print the scope as a short list (files + mode) before the review. Do not read files outside it,
   except to check a fact (a shared rule in `assets/critical.css`, a locale key, a caller).

## 2. Review (read every scope file in full)

Look for real defects only. Each finding needs a concrete failure: input or state → wrong result.
Check these, in this order:

1. **Liquid:** wrong filter order (`x | default: 'key' | t` also translates `x`), filters inside
   attributes (assign first), truthiness on text settings (`!= blank`), `nil` from a missing
   setting, a `capture` that is not `| strip`ped before it goes into an attribute, more than one
   `{% content_for 'blocks' %}` in one file (a 500 that Theme Check does not catch), `for` loops
   over 50 items, `section.blocks` settings read from a theme block (they are empty).
2. **Schema and locales:** every `t:` key and every `'key' | t` exists; setting ids not renamed
   (saved values); `visible_if` only on types that allow it (not `collection`, `article`,
   `product_list`); info text names the setting it depends on; presets valid; no leftover unused
   setting or key.
3. **JS:** every listener on one `AbortController` aborted in `disconnectedCallback` (the editor
   re-attaches a moved section: `connectedCallback` runs again); no work done twice after a
   re-attach (lists rebuilt, observers added, timers left running); `prefers-reduced-motion`
   followed; content visible without JS and before `:defined`; nothing typed by a visitor goes
   into `innerHTML`; editor events (`shopify:block:select` …) on the same signal.
4. **Accessibility:** names on buttons and links; real buttons for actions (no fake toggles:
   `aria-expanded` only on something that opens and closes); heading order (a hidden h2 when a
   visible one is empty); focus visible; live regions for results that change; alt text (empty for
   decoration).
5. **Performance:** images through `section-loading` (never lazy for the LCP, `fetchpriority=high`
   only in section 1); `sizes` that match the real rendered width on each breakpoint; no extra font
   faces (`font_modify` + `font_face`) for one small text; no CSS `mod()` / `round()` that old
   browsers drop.
6. **CSS:** rules that never apply because a global rule wins (`.button`, `input[type=…]` in
   `critical.css` beat one class: two classes needed); `--px` used without a value when "Scale
   with the screen" is off; `:empty` on an element that holds white space; physical vs logical
   positions (pins and photos that are never mirrored use `left` / `top`); overflow at 320 / 390 /
   820 / 1280px; duplicate or dead rules.
7. **Empty states:** the store with an empty setting, 0 blocks, 1 block, the maximum blocks; the
   theme editor shows a note instead of an empty space.

Do not report style preferences, things already listed as "Open" for this section in CLAUDE.md
(say "known" if one comes up), or contrast (that is decided in M9: log it only).

## 3. Verify before reporting

For each candidate finding, prove it:
- read the exact lines again and the rule that beats it (file + line);
- when a browser test is possible, test it (`iframe srcdoc` frames of the page, see CLAUDE.md;
  `theme dev` at `127.0.0.1:9292`);
- drop it when the proof fails. Mark a finding "likely" only when it can't be tested here (e.g. a
  form POST that `theme dev` refuses) and say why.

## 4. Report, then stop

One table, most severe first:

| # | Severity | File:line | Problem | Failure (input → result) | Fix (one line) |

Severity: **bug** (wrong result now), **risk** (wrong result in a real case: editor move, empty
setting, RTL, old browser), **cleanup** (dead code, duplicate rule). Under the table: the shared
files touched by each fix, and anything "known" or "likely".

Then ask: "Which numbers do I fix?" and stop. Do not edit before the answer.

## 5. Fix (after the answer)

1. Fix only the chosen numbers. Keep setting ids; add new `<section>_*` keys, never reword a shared
   key that other sections use.
2. Edit with the Edit tool or Node scripts. **No `sed -i` while `theme dev` runs** (its temp file is
   uploaded and breaks the preview).
3. Run `shopify theme check --path .` (must be clean) and check that every `t:` key in the scope
   exists.
4. Test each fix in the browser at 390 / 820 / 1280px (and the failure case from the table).
5. Report: a table with each number → fixed / not fixed (why), the test result, and what is still
   untested.
6. Update the section's entry in CLAUDE.md: "code review run and fixed" (or "code review run, no
   findings"), plus new Open items.
7. Give the `git add` / `commit` / `push` commands (the same for Git Bash, PowerShell and cmd), with
   only the scope files that changed. Do not commit.
