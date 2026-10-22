# Project handoff: Oroskin Shopify theme (custom, built on Skeleton)

> **How to use this file:** paste its contents into a new Claude chat as the first message.
> Last updated: 2026-10-22

## Who I am

Frontend developer. Strong HTML, CSS, JavaScript and responsive design. **Beginner in Shopify, Liquid and theme development.** Explain Shopify/Liquid concepts in simple, clear sentences, and tell me *why*, not just *what*. Never assume I know Shopify jargon.

## What the project is

Build a **fully custom Shopify theme** from a Figma design for a brand called Oroskin.

- The Figma design is **completely custom** and looks nothing like Dawn.
- It has **scroll-triggered animations**.
- Goal 1: an agency **showcase site** to win new clients.
- Goal 2 (later, optional): list the theme on the **Shopify Theme Store**.

## Decisions already made (do not re-litigate)

1. **Start from Shopify's Skeleton theme**, not Dawn, and not an empty folder.
   Reason: Shopify's Theme Store requirements state that themes *"built on or derived from Dawn or Horizon are not eligible"* and that *"Shopify's Skeleton Theme is the only approved codebase for Theme Store development."* Stripping Dawn would also mean fighting its shared `base.css` / `global.js` on every page.
2. **Dawn stays as a read-only reference** at `d:\shopify-oroskin\dawn`. Rule: **read, don't copy.** Using the same Shopify APIs is fine; copying Dawn's files, markup or JS classes is not, because Theme Store code must be original.
3. **Two phases.** Phase 1 = the showcase site. Phase 2 = Theme Store hardening, started only after Phase 1 is live and stable.
4. **Animations** use native `IntersectionObserver` + CSS `transform`/`opacity`, inside a small web component. Merchant settings turn them on and off, `prefers-reduced-motion` is respected, the hero/LCP content is never hidden, and content stays visible without JS. GSAP only if an effect truly needs it, bundled into `assets/`, never from a CDN.

## Read this first

`SHOPIFY-LEARNING-ROADMAP.md` — a guide I built in a previous session. Most relevant parts:

- **Part 9.4 / 9.5** — why Skeleton, and the Theme Store eligibility rules
- **Part 19** — the full project plan: setup, architecture, the animation system with code, the milestone tables, and a "study this Dawn file" reference table
- Parts 2–7 explain Liquid, theme structure, sections/blocks/snippets, data and metafields
- Part 12 covers performance and Part 13 covers the production process

Also `SHOPIFY-DEV-TO-LAUNCH-RESEARCH.md`: a research report (2026-09-28) covering the full path from dev to live store to Theme Store approval, including SEO, with sources. Its key findings:
- Stay on Skeleton v1 (`main`).
- Dev stores can't go live, so use a client transfer store or a paid store for the showcase.
- The Theme Store doesn't accept custom fonts.

Also `THEME-STORE-CHECKLIST.md`: every Theme Store requirement, grouped by milestone and marked with its Skeleton status. **Scope decision:** every required feature is built during Phase 1. Oroskin adds no extra features, only design.

Also at `d:\shopify-oroskin\dawn\DEVELOPER-GUID.md`: CLI commands, Theme Check, Prettier, commit checklist.

## Current state (2026-10-22, end of session)

- Theme scaffolded from Skeleton at `d:\shopify-oroskin\custom-built-new-theme-oroskin\oroskin-theme`. Dev store `oroskin-dev`; preview with `shopify theme dev -e dev`.
- **Done and committed:** M1 Foundation, M2 Header & footer (desktop), M3 Shared blocks, and most of M4 Homepage on branch **`feature/m4-homepage`** (last commit `8b33cc6 Add testimonials to the homepage`).
- **Homepage sections built:** Hero, Scrolling showcase, Editor's Picks (`product-panels`), Image banner (Manifesto + Trending sheet scene), Testimonials, Blog stories, promo Image banner, Icon features, Featured product, Trending products. Quick add (`snippets/quick-add.liquid`) is shared.
- **Deadline mode is on** (until 22 Oct 2026, then documentation): Claude drafts via `/learn-guide`, I review, test and commit. Session log: `C:\Users\Hariprathap\Desktop\personal-development-os\06-learning-sessions\2026\2026-10-22.md`.

### Uncommitted work (review, test, then ship)

Two pieces of work are mixed in the working tree. Ship them as two commits.

1. **Hero "Explore collection" glass button + M4.14 homepage order**
   - `blocks/button.liquid`: new Style option **Glass** (`.button--glass`).
   - `assets/critical.css`: `.button--glass` = solid `--color-button`, `border: none`, 60px tall, 25px side padding, 10px gap, weight 400, hover darkens and keeps the shadow. Primary button (login, subscribe) is unchanged: 85% fill, 1px border, `0 4px 20px #00000033`.
   - `snippets/css-variables.liquid`: `--shadow-button-glass: 0 4px 15px #00000040, 0 3px 15px #00000014, inset 1px 1px 4px #ffffff` (the 3 Figma shadows; the Figma Glass Refraction/Depth/Dispersion are not possible in CSS).
   - `locales/en.default.schema.json`: the "Glass" style label.
   - `templates/index.json`: pulled from the dev theme with my section order; hero button `style: glass`; banner links restored (`shopify://collections/all`, `shopify://blogs/featured`). **Editor saves overwrite this file while `theme dev` runs: check it before committing.**
   - `THEME-STORE-CHECKLIST.md`: M4 ticks.
2. **M4.6 New Arrivals deck (draft, being tested)**
   - `sections/product-deck.liquid` (new, preset "New arrivals"): eyebrow + heading + "Fresh this week" pill; collection cards that start stacked and fan out on scroll (`--fan-progress`, smoothed like the Image banner). The fan never moves; hover (mouse), tap or Tab makes a card active **in its own place** (on top, 8% bigger, keeps its tilt) with quick add + glass info card (title, subtitle/description, price, Buy now → product page). Each card has a "Show {title}" pick button for keyboard/touch. Spread adapts to 3–8 cards (`--half`).
   - "Explore all": pale gold glass pill at rest; on hover a gold circle grows from the left and fills it, text turns white, the paper plane flies out and back. (A "filled at rest, two planes" variant was tried and reverted.)
   - `assets/icon-send.svg` (Figma plane) and `assets/icon-buy.svg` (Figma buy icon; its clip paths were removed so ids don't repeat on the page).
   - `locales/en.default.json`: `products.deck.show`; `locales/en.default.schema.json`: `general.product_deck`, `general.new_arrivals`, `labels.deck_*`.
   - Not yet added to `index.json`: I add it in the editor.

### Open decisions

- White text on gold (Buy now, scroll scene) and gold on pale gold (Explore all) are about 2–2.4:1, below the WCAG 4.5:1 minimum. Decide in M9.
- M2.6 mobile drawer and all mobile-specific layouts (decision 7). Parked features (decision 6).
- Multi-variant quick add adds the first available variant (client to confirm).

## How I want you to work with me

- **One milestone at a time.** Don't dump the whole theme at once.
- **Explain before generating.** Tell me what we're building, which Shopify objects/APIs it uses and why, then write the code.
- **Teach me the Liquid** in what you write. I want to understand every line, not paste it blindly.
- Every section needs: `{% schema %}` settings, a **preset**, `{{ block.shopify_attributes }}` on blocks, empty states (`!= blank`), placeholder content, and locale strings instead of hardcoded text.
- Watch for these mistakes: `{% include %}` (use `render`), `img_url` (use `image_url` + `image_tag`), truthiness checks on text settings (use `!= blank`), **filters inside filter arguments** (invalid — `assign` first), hardcoded handles (use settings), lazy-loading the hero image.
- Performance: our goal is Lighthouse mobile 100 in all four categories (never below 90); Theme Store minimum ≥ 60 performance, ≥ 90 accessibility.
- Ask me before assuming anything about the design. Figma details are in `design/figma/` (read first).
- Don't commit or push unless I ask. Never push to a live theme.

## First task (next session)

1. `/learn-check` the uncommitted work above, then `/learn-ship` it as two commits: (a) glass button + homepage order + checklist, (b) New Arrivals deck + icons + locales.
2. Add the New Arrivals section in the editor in the Figma position (after the scrolling showcase / gold band), pick a collection sorted newest first, then pull `index.json` and commit it.
3. Lighthouse mobile on the preview link (home), then close M4 and merge `feature/m4-homepage`.
4. Next milestone: **M5 Collection (with filters)**.
