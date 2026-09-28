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
- `d:\shopify-oroskin\dawn\DEVELOPER-GUID.md`: CLI commands, Theme Check, Prettier, commit checklist.

## Current state (update as it changes)

- The theme is scaffolded from Skeleton at `d:\shopify-oroskin\custom-built-new-theme-oroskin\oroskin-theme`. Git has been initialised.
- Still blocked on:
  - [ ] Figma link or screenshots (needed before any section work)
  - [x] Development store created: `oroskin-dev` (admin.shopify.com/store/oroskin-dev). Preview with `shopify theme dev -e dev` (see `shopify.theme.toml`)
  - [ ] Brand assets: logo, fonts (with licences), product photography
- **Next milestone: 1, Foundation.** Figma tokens go into `config/settings_schema.json` and CSS variables in `layout/theme.liquid`. Add `base.css` (reset, typography, buttons, forms) and the animation system.

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
- Ask before assuming anything about the design.
- Don't commit or push unless I ask. **Never push to a live theme.**
