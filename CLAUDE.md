@AGENTS.md

# Oroskin theme: project context

Generic Shopify/Liquid rules live in `AGENTS.md` (imported above). This file holds only what is specific to Oroskin.

## The project

A fully custom Shopify theme for the brand **Oroskin**, built from a custom Figma design with scroll-triggered animations. It looks nothing like Dawn.

- **Phase 1:** an agency showcase site to win new clients. This is the priority.
- **Phase 2 (later, optional):** Theme Store hardening. Start it only after Phase 1 is live and stable.

## Decisions already made (do not re-litigate)

1. **Built on Shopify's Skeleton theme.** Dawn- or Horizon-derived themes are not eligible for the Theme Store. Skeleton is the only approved base.
2. **Dawn is a read-only reference** at `d:\shopify-oroskin\dawn`. **Read, don't copy.** Using the same Shopify APIs is fine. Copying Dawn's files, markup or JS classes is not.
3. **Animations:** native `IntersectionObserver` + CSS `opacity`/`transform`, inside an `<animate-on-scroll>` web component. There is a global "Enable animations" setting plus a per-section style. Respect `prefers-reduced-motion`, never hide the hero/LCP content, and keep content visible without JS. GSAP only if an effect truly needs it, bundled in `assets/`, never from a CDN. See roadmap Part 19.4.
4. **Scope: build every Theme Store–required feature during Phase 1**, inside its milestone. Oroskin adds no extra features beyond these; it only changes the design. Track them in `THEME-STORE-CHECKLIST.md`.
5. **Fonts (2026-09-28):** every font comes from Shopify's free font library through `font_picker` settings, so the merchant can change them in the theme editor. The Figma uses **Canela Text Trial**, a paid font with a trial licence only, so it is not used. Defaults: headings `newsreader_n4` (closest free match to Canela Text), body `plus_jakarta_sans_n4` (closest to Satoshi). The logo is an image upload, with the shop name as a text fallback.
6. **Parked features, awaiting design and client confirmation:** wishlist, custom account pages (overview/details/orders/track/refills/rewards/preferences), rewards, refills and the notification bell. Don't build them yet. When they are confirmed, each gets a **show/hide toggle** setting. Until then the header account icon only uses `<shopify-account>`, which links to Shopify's own customer accounts.
7. **Mobile:** there are no mobile designs yet. The developer will decide later. Build responsive CSS in a sensible way, but ask before designing mobile-specific layouts.

## Reference docs in this repo (excluded from Shopify push via `.shopifyignore`)

- `HANDOFF.md`: who the developer is, current state, blockers, first task.
- `SHOPIFY-LEARNING-ROADMAP.md`: the full guide. The most relevant parts:
  - **Part 19:** the project plan (setup, architecture, animation code, milestones, the "study this Dawn file" table)
  - Parts 9.4/9.5: why Skeleton and the Theme Store rules
  - Parts 2–7: Liquid, structure, sections/blocks/snippets, data, metafields
  - Part 12: performance. Part 13: the production process.
- `SHOPIFY-DEV-TO-LAUNCH-RESEARCH.md`: research report (Claude.ai, 2026-09-28) covering setup to live store to Theme Store approval, with sources. The most relevant parts:
  - Stage 1 and Stage 8: dev stores can't go live. Use a client transfer store or a paid store for the Phase 1 showcase.
  - Stage 3: CLI environments and rules for protecting the live theme
  - Stage 4: design tokens (at least 4 colours, each background paired with a foreground), `font_picker` only (no custom fonts on the Theme Store), images
  - Stage 7: SEO (what Shopify does automatically vs what the theme must add)
  - Stage 9: Theme Store submission, the review stages, rejection reasons
  - "Recommendations": stay on Skeleton v1 (`main`, not `rc-v2.0.0`), plus extra details for the animation system
  - "Caveats": items the research could not verify
- `design/figma/`: **local snapshot of the Figma design. Read it first.** It contains `tokens.md`/`tokens.json`, `typography.md`, and `screens/`, `components/` and `animations/` folders, each with a screenshot, raw MCP context and notes. It also has downloaded `assets/` and the full `metadata.xml` node tree, plus a `README.md` index. Call the Figma MCP only if something is missing or the design has changed. The `context*.jsx` files are React+Tailwind reference only; never copy them into the theme.
- `THEME-STORE-CHECKLIST.md`: every Theme Store requirement, grouped by milestone. Each item shows its Skeleton status (✅/🟡/❌). Tick items off as you finish them.
- `d:\shopify-oroskin\dawn\DEVELOPER-GUID.md`: CLI commands, Theme Check, Prettier, commit checklist.

## Current state (update as it changes)

- The theme is scaffolded from Skeleton at `d:\shopify-oroskin\custom-built-new-theme-oroskin\oroskin-theme`. Git has been initialised.
- Still blocked on:
  - [x] Figma: https://www.figma.com/design/EcvT6hH5DXNRzan3G8uVwf/Dev-OroSkin (file key `EcvT6hH5DXNRzan3G8uVwf`, one page, desktop 1920px frames; Figma MCP connected)
  - [x] Development store created: `oroskin-dev` (admin.shopify.com/store/oroskin-dev). Preview with `shopify theme dev -e dev` (see `shopify.theme.toml`)
  - [ ] Brand assets: logo and product photography (fonts are decided, see decision 5)
  - [ ] Designs for the parked features (decision 6) and for mobile (decision 7)
- Work branch: `feature/m1-foundation` (created from `main`).
- **Deadline: theme development done by 22 Oct 2026** (set 2026-10-10); documentation starts after that.
- **Milestone 1, Foundation: in progress.** Steps 1–3 done (test content; theme identity + homepage clean-up, `8cada3a`; heading/body font pickers, `1072d87`). Step 4 (colour schemes) is next. The step plan is in the PDOS session file of 2026-10-05; step status is in the latest session file. Figma tokens go into `config/settings_schema.json`, CSS variables in `snippets/css-variables.liquid`, base styles and the animation-hiding CSS in `assets/critical.css`.
- `design/` is ignored by git (local only, ~300 MB). Tokens are in `design/figma/tokens.md`.

## Build order (Phase 1 milestones)

1. Foundation
2. Header & footer
3. Shared snippets + theme blocks
4. Homepage
5. Collection (with filters)
6. Product (variants, add to cart, app blocks)
7. Cart
8. Remaining pages
9. QA & performance
10. Launch

## Conventions

- BEM class names: `.hero`, `.hero__title`, `.hero--dark`.
- Theme blocks in `blocks/` (heading, text, button, image) are written once and reused across sections.
- CSS and JS are scoped per component and load only where used.
- Every section has `{% schema %}` settings, a **preset**, `{{ block.shopify_attributes }}` on blocks, empty states (`!= blank`), placeholder content, and locale strings (no hardcoded text).
- Performance targets from day one: Lighthouse mobile **≥ 60 performance, ≥ 90 accessibility** on home, collection and product.

## Mistakes to watch for

- `{% include %}`: use `render`
- `img_url`: use `image_url` + `image_tag`
- Truthiness checks on text settings: use `!= blank`
- Filters inside filter arguments or attributes: `assign` first
- Hardcoded handles: use settings
- Lazy-loading the hero image

## How to work with me

- I'm a strong frontend developer (HTML/CSS/JS) but a **beginner in Shopify and Liquid**. Explain Shopify concepts simply, and say *why*, not just *what*. Don't assume I know the jargon.
- **One milestone at a time.** Explain what we're building and which Shopify objects/APIs it uses before writing code, then teach the Liquid in what you write.
- **Deadline mode (agreed 2026-10-10, until 22 Oct 2026): Claude drafts the code, I review, test and commit.** `/learn-guide <step>` explains the concepts fully, writes the step's code, then walks me through it line by line with a review-and-test list. If I ask to write a part myself, Claude leaves a `TODO(you)` there. Explanations must make sense without opening links; links are given last as "Cross-check".
- **Learning method (agreed 2026-10-05, paused by deadline mode): I write all theme code myself.** Claude switches roles only when I type a `/learn-*` command:
  - `/learn-start`, then `/learn-plan` (planner)
  - `/learn-guide` (`TODO(you)` comments with doc links, no solution)
  - `/learn-hint`, `/learn-example`, `/learn-pair` (when I'm stuck)
  - `/learn-check` (explains my diff), `/learn-mentor` (asks questions, then shows best practice)
  - `/learn-ship` (I commit and push), `/learn-wrap` (end of day)
  
  The playbook, with "when to use what" and the rules, is `C:\Users\Hariprathap\Desktop\personal-development-os\06-learning-sessions\README.md`. The daily log goes in `06-learning-sessions/YYYY/YYYY-MM-DD.md`.
- **Theme code:** in deadline mode, Claude writes theme code only through `/learn-guide` (one step at a time, explained) or when I ask for a fix. Outside deadline mode: never write or edit theme code except `TODO(you)` comments and small fixes I ask for. Log every question I ask in today's session file.
- **Colours: use hex.** It's what Shopify stores and it's exact. Use 8-digit hex for transparency, or `color-mix()`. Don't use `rgb()` triples.
- Ask before assuming anything about the design.
- Don't commit or push unless I ask. **Never push to a live theme.**
