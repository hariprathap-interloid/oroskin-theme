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
- Work branch: `feature/m5-collection` (pushed). Start a new branch for M8 (e.g. `feature/m8-pages`). Earlier: `feature/m4-homepage`, `feature/m1-foundation`, `feature/m2-header-footer`, `feature/m3-shared-blocks`.
- **Deadline: theme development done by 22 Oct 2026** (set 2026-10-10); documentation starts after that.
- **Milestone 1, Foundation: done (2026-10-12).** Built: theme identity, heading/body font pickers, colour schemes (`settings.color_schemes` → `.color-<id>` classes that set `--color-*` and paint; sections add `color-{{ section.settings.color_scheme.id }}`), type/spacing/radius/shadow/motion tokens (`snippets/css-variables.liquid`), Standard page width (1650px content at 1920px), logo/favicon/social/animation settings, base typography + `.rte` + `.eyebrow`, buttons (`.button`, `--secondary`, `--text`), focus ring, forms, responsive `image` snippet (auto eager/lazy by `section.index`, `priority`), and the `<animate-on-scroll>` system (`data-animate="fade-up|zoom-in"`, never on section 1). Step log: PDOS session files 2026-10-05 → 2026-10-12.
- **Milestone 2, Header & footer: done for desktop (2026-10-14).** Header (M2.1–M2.5: logo image/text/shop-name fallback, mega menu with `mega_menu_card` blocks and slider arrows bottom-right, search/cart/`<shopify-account>` LOGIN, sticky glass pill, transparent mode via `<sticky-header>`; sticky wrapper is `pointer-events: none`). Footer (M2.7–M2.10: full-width glass panel, columns from ONE nested `footer` menu, link grey = scheme text mix ≥ 4.5:1, `localization-form`, `newsletter-form` (customer form, no `autofocus`: focus via `data-focus-after-submit`; spacing with margins because Shopify injects an hCaptcha div), `social-icons` (7 networks, `icon-<name>.svg`), Follow on Shop, labelled payment icons, `powered_by_link`, clipped wordmark). M2.11: skip link + `<main id="MainContent" tabindex="-1">` in the layouts; Lighthouse accessibility checked. **Open:** M2.6 mobile drawer + mobile `<shopify-account>` (decision 7), predictive search (M8), Follow on Shop to verify on a store with Shop Pay, newsletter input border 1.03:1 (design vs WCAG, decide in M9), Dark/Red scheme contrast on the glass footer (M9). `theme dev` can't POST `/localization` or `/contact` (502): test forms on the preview link. Skeleton's Text block still has fixed sizes (rebuilt in M3).
- **Milestone 3, Shared blocks: done.** **Milestone 4, Homepage: nearly done (2026-10-22).** Sections: Hero, Scrolling showcase, Editor's Picks, Image banner (Manifesto + Trending sheet scene), Testimonials, Blog stories, promo banner, Icon features, Featured product, Trending products; shared `quick-add` snippet; Button block Style "Glass" for the hero. Uncommitted at session end: the glass button + homepage order, and the M4.6 New Arrivals deck (`sections/product-deck.liquid`, still being tested). See `HANDOFF.md` → "First task". **Next: ship those, Lighthouse, then M5 Collection.**
- **Milestone 7, Cart: in progress (branch `feature/m7-cart`, 2026-10-27).** Done: M7.1–M7.6 (cart page, order summary, coupons, gift wrap inside the card with Wrap style blocks, stepper fixes). Demo catalogue imported from `design/catalogue/products.csv` (built by `build.js`; images in Content → Files, same names). Collections: `new-arrivals` (tag new), `editors-picks`, skincare/fragrance/makeup by type. Generated PNGs carry the prompt as metadata, so set short alt text by hand on non-product files. New Arrivals deck: Card size setting, arc, first card active, `isolation: isolate` under the header. **Next: M7.7 search popup.** Open: hide the gift wrap product from the bag list?
- **Milestone 5, Collection: done (2026-10-29, branch `feature/m5-collection`, last commit 5693dc4).** Collection banner, bento/even product grid, toolbar (category pills from a menu via `snippets/category-pills.liquid`, count, styled SORT `base-select`), filter drawer (`snippets/filter-drawer.liquid` + `filter-group.liquid`, Figma 170:94885, live count, brief `design/briefs/filter-drawer.md`), pagination snippet, search page (grouped results, suggestions), collection list page (tiles/cards/overlay/bento, banner header). Shared `<results-view>` script lives in `snippets/results-view.liquid` (a section's own script only runs where that section is on the page). Colours on M5 pages use `--color-accent` (per scheme), never the fixed `--color-primary`, so red/dark schemes stay readable. Store setup still to do: "All products" link first in the `collection-pills` menu; collections' "Pill image" metafield (`custom.pill_image`) on other stores.
- **M8 progress (branch `feature/m8-pages`):** M8.1 Contact done (0bbbdb2). M8.2 Blog listing: done 2026-10-30 (befbf81; `blog-hero`, `blog-trending` + `_trending-article`, rebuilt `blog` listing with `article-card`, `read-time`, `trending-article` snippets, icon features in `templates/blog.json`; pagination restyled on all pages). Demo articles: `design/catalogue/blog/` (articles.json + import-articles.mjs via `shopify store execute`); replace the demo content, images and the Trending video with the Figma's before the showcase. M8.3 Blog details: built 2026-10-31 (`article-hero`, `article` (rich-text conventions styled by CSS + a Liquid pass, sticky sidebar, "The edit" rows at a `[products]` paragraph), `article-comments`, `article-related`; snippets `article-product-card`, `article-product-row`, `author-avatar`, `share-links`, quick-add `style: 'pill'`). Article fields (Settings > Custom data > Blog posts): `custom.products` (list of products), `custom.title_highlight` (single line text). Open: hero date uses a fixed format (use `format: 'date'`); test Load more + comment errors on the preview link. Next: M8.4 About us.
- **Next: Milestone 8, Remaining pages (before M6 Product, my choice 2026-10-29).** Order: M8.1 Contact (`page.contact.json` + contact form, Theme Store requirement) → M8.2 Blog listing → M8.3 Blog details → M8.4 About us → M8.5 FAQ → M8.6 Policies (B: CSS for built-in `/policies/*`; C: optional `page.policy` template that reads `shop.*_policy.body`) → M8.7 404, generic page, password, gift card (no Figma, M5 style). Parked: cookie preferences page (only if wired to the Customer Privacy API), account pages (new customer accounts are Shopify-hosted: branding or app extensions only). Each Figma page: `/design-brief <slug>` then `/learn-guide M8.x`.
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
- Performance targets from day one: Lighthouse mobile on home, collection and product. **Our goal: 100 in all four categories (never below 90).** Theme Store minimum: ≥ 60 performance, ≥ 90 accessibility. Measure on the real store in an incognito window; the local `theme dev` proxy and browser extensions distort scores.
- **Lighthouse baseline (2026-10-12, end of M1, local 127.0.0.1 with extensions, mobile):** performance 81 (FCP 3.2 s, LCP 3.6 s, TBT 90 ms, CLS 0, SI 4.7 s), accessibility 98, best practices 54, SEO 92.

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
