# Oroskin: From Skeleton Scaffold to Live Store and Shopify Theme Store Approval — A Step-by-Step Guide (researched September 28, 2026)

Your plan works, but only if you change two things now. First, stay on the current `main` (v1) structure of Skeleton, which uses sections and JSON templates. Do not move to the new block-first `rc-v2.0.0` branch, which removes both, while the Theme Store still requires them.\[1\] Second, you cannot launch the Phase 1 showcase from a normal dev store. Dev stores "can't be converted to production stores" and "can't be transferred to a client". Use a client transfer store, or a normal paid store, for anything that must go live.\[2\]

## TL;DR

- **Your base is correct, but pin the right version.** Shopify's current Theme Store requirements say "Shopify's Skeleton Theme is the only approved codebase for Theme Store development," and that themes "built on or derived from Dawn or Horizon are not eligible." Build on Skeleton's section-based `main` branch. Skeleton's `rc-v2.0.0` branch has "no sections, no JSON templates," but the Theme Store still requires JSON templates, section groups and a Custom Liquid section.
- **Use two stores and never push to a live theme.** Build and test on a free dev store. Run the live Oroskin showcase on a client transfer store or a paid store, because dev stores can't go to production. Push only with `shopify theme push --unpublished` or `--theme <id>`. Never use `--live`, `--allow-live` or `--publish`. Publish by hand in the admin.
- **The Theme Store bar is high and ongoing.** You need an average Lighthouse score of at least 60 for performance and 90 for accessibility. The average covers the home, product and collection pages, on desktop and mobile. There is a 5-stage review with no published turnaround time. You can price your theme from $100 to $500. You must answer support requests within two business days and wait at least four weeks between updates. Plan for custom brand fonts to be replaced, because "custom fonts aren't accepted."

---

## Key Findings

1. **The eligibility rule is confirmed.** The requirements page (shopify.dev, accessed Sept 28, 2026; the page itself is undated) says: "Shopify's Skeleton Theme is the only approved codebase for Theme Store development. Otherwise, themes must be built with fully original code. New theme submissions built on or derived from Dawn or Horizon are not eligible."\[3\] This rule arrived with the requirements update that took effect **May 15, 2025** (shopify.dev changelog).\[4\]
2. **There is a Skeleton version trap.** The `main` README says Skeleton "scaffolds JSON templates."\[5\]\[6\] The `rc-v2.0.0` branch is a release candidate. It says "No sections/ directory… No JSON templates and no schema presets" and "keep all CSS and JavaScript in assets/ rather [than] {% stylesheet %} / {% javascript %}."\[1\] The Theme Store still requires `index.json`, `product.json` and the other JSON templates, plus "Sections Everywhere" and section groups for the header and footer.\[3\] **I'm unsure** whether Shopify will change the Theme Store rules to match Skeleton v2. Until it does, v2 does not fit the current requirements.
3. **Dev stores have changed.** Stores are now managed in the **Dev Dashboard** (dev.shopify.com/dashboard). Its newest home page was announced on **Sept 25, 2026**.\[7\] Dev stores can use any plan (Basic, Grow, Advanced, Plus). They can be created from the CLI with `shopify store create dev`. Each organisation can have up to 250.\[2\] They are always password-protected.\[8\] They cannot be converted to production or transferred to anyone.\[2\]
4. **There is a conflict about demo stores.** Requirement §20 says: "To build your demo store, create a Client transfer store from your Shopify Partner Dashboard."\[3\] A separate shopify.dev dev-store page says: "You can use a dev store as a demo store in Shopify Theme Store listings."\[8\] Follow the stricter rule and use a client transfer store for the Theme Store demo.
5. **Revenue share is 15%.** The shopify.dev revenue-share page says "no fees for submitting themes" and "a 15% revenue share" on gross sales, plus a 2.9% processing fee.\[9\] An older themes.shopify.com guidelines snippet mentioned 0% on the first $1,000,000 each year. That page now redirects to shopify.dev/docs/storefronts/themes/store, which says "Themes sold through the Shopify Theme Store are subject to a 15% revenue share." Shopify's Help Center page "How Partners earn on Shopify" confirms it: "Sell a theme: 85% of revenue, Per sale." The 0%-on-$1M rule applies to apps only.

---

## Stage 1 — Where to start

**What.** Set up your accounts, a store to develop on, test data, the CLI and a clean repo.

**Why.** Shopify themes only render on Shopify's servers. You need a store connected to your local files before you can see anything. Good test data exposes layout bugs early, and the Theme Store reviewers will test with the same kind of data.

**Key terms.**
- *Partner account*: your free Shopify developer and agency account.
- *Dev Dashboard*: Shopify's newer hub for managing stores and apps.
- *Dev store* (development store): a free, password-protected test store.
- *Client transfer store*: a store you build and then hand over to an owner, who picks a paid plan.
- *Shopify CLI*: the command-line tool for previewing, pushing and checking themes.

**How.**
1. **Create a Partner account** at partners.shopify.com. This is the account you will later submit your theme from (Partner Dashboard → Themes → Submit a theme).\[10\]
2. **Open the Dev Dashboard** at dev.shopify.com/dashboard. Choose Stores → Create store → **Dev**, then pick a plan. If you prefer the terminal, run `shopify store create dev --name "oroskin-dev" --demo-data`.\[2\] Demo data matters because an empty store hides layout bugs. *Flag:* the dev-stores page shows `--demo-data`, but the themes dev-store page mentions `--with-demo-data`.\[8\] Run `shopify store create dev --help` to see which flag your version uses.
3. **Create a second dev store just for benchmarking.** Shopify's "Testing for performance" page says the benchmark "uses a development store pre-loaded with standardized test products."\[11\] Import Shopify's test product CSV into it. This way you measure your theme the same way reviewers do.\[12\]
4. **Don't turn on feature previews** on any store you may need to show publicly. Shopify says: "When a feature preview is enabled on a dev store, you don't have access to domains."\[2\] Also, "Development stores with developer previews enabled can't be transferred."\[3\]
5. **Install the tooling.** Install Shopify CLI (latest version; check with `shopify version`, upgrade with `shopify upgrade`).\[13\] Install the **Shopify Liquid VS Code extension**, which includes Theme Check and the Liquid Prettier plugin.\[14\]
6. **Run the theme locally.** From the theme root, run `shopify theme dev --store oroskin-dev`. This creates a *development theme*: a temporary, hidden theme that is "deleted from the store after seven days of inactivity" and also when you run `shopify auth logout`.\[15\] It hot-reloads CSS and section changes.\[13\]
7. **Organise the repo** (see below).

**Suggested repo layout.** Keep the theme at the repo root. The CLI and the GitHub integration only work with "the default Shopify theme folder structure."\[13\]
```
/assets /blocks /config /layout /locales /sections /snippets /templates (+ templates/customers)
.theme-check.yml
.prettierrc           # { "plugins": ["@shopify/prettier-plugin-liquid"] }
.shopifyignore
shopify.theme.toml    # CLI environments
package.json
/docs
```
Do not commit `config/markets.json`. The requirements say "Do not include the config/markets.json file with your theme when submitting."\[3\] If you plan to use a build step, keep the compiled output unminified. The Theme Store rejects minified `.css`/`.js`, except ES6 and third-party libraries, and it rejects Sass.\[3\]

**Where.**
- Dev stores: shopify.dev/docs/apps/build/stores/development-stores (undated, accessed 2026-09-28)
- Stores overview: shopify.dev/docs/apps/build/stores
- Shopify CLI for themes: shopify.dev/docs/storefronts/themes/tools/cli
- Skeleton: github.com/Shopify/skeleton-theme (`main`; note that `rc-v2.0.0` exists)

**Checklist.**
- [ ] Partner account created
- [ ] `oroskin-dev` dev store with demo data (no feature preview)
- [ ] `oroskin-bench` dev store with Shopify's test product CSV
- [ ] CLI and VS Code Liquid extension installed
- [ ] `shopify theme dev` runs
- [ ] Repo on Skeleton `main` structure, with `.shopifyignore`, `.theme-check.yml` and `.prettierrc`

---

## Stage 2 — Official best practices and where to find them

**What.** These are the shopify.dev pages that define how a modern theme is built.

**Why.** Shopify changes often, and blogs go out of date fast. The Theme Store reviews your theme against these docs, not against tutorials.

**Key terms.**
- *Liquid*: Shopify's template language.
- *Section*: a full-width, merchant-editable module.
- *Theme block*: a reusable, nestable component stored in `/blocks`.
- *Snippet*: reusable code that merchants can't see in the editor.
- *Schema*: JSON inside `{% schema %}` that defines settings.
- *Locales*: translation files.

| Page (bookmark) | URL | What it teaches you | Date/status |
|---|---|---|---|
| Theme architecture | shopify.dev/docs/storefronts/themes/architecture | Folder structure and how templates, sections and blocks fit together | Undated, accessed 2026-09-28 |
| Sections | shopify.dev/docs/storefronts/themes/architecture/sections | Section schema, section groups, presets | Undated |
| Blocks (theme blocks) | shopify.dev/docs/storefronts/themes/architecture/blocks | Theme blocks vs section blocks, nesting, static blocks. There is a limit: "at most 300 theme blocks," and AI-generated (Sidekick) blocks count toward it\[16\] | Current |
| Snippets | shopify.dev/docs/storefronts/themes/architecture/snippets | `{% render %}`, parameters, scope. Snippets "are invisible to merchants in the theme editor"\[17\] | Current |
| settings_schema.json | shopify.dev/docs/storefronts/themes/architecture/config/settings-schema-json | Global theme settings and the required `theme_info` | Current |
| Input settings | shopify.dev/docs/storefronts/themes/architecture/settings/input-settings | Setting types: `color`, `font_picker`, `image_picker`, `liquid`, and more | Current |
| LiquidDoc | shopify.dev/docs/storefronts/themes/tools/liquid-doc | `{% doc %}` with `@param` for snippets and blocks. Theme Check validates it (for example, `MissingRenderSnippetArguments`)\[18\] | Announced mid-2025; current |
| `{% stylesheet %}` / `{% javascript %}` | shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags | One tag per file, no Liquid inside, CSS split per page, JS deferred\[19\] | Current |
| Locales | shopify.dev/docs/storefronts/themes/architecture/locales | Storefront and schema translation files | Undated |
| Theme Check | shopify.dev/docs/storefronts/themes/tools/theme-check | Linting rules and `.theme-check.yml` | Undated |
| Liquid reference | shopify.dev/docs/api/liquid | Every object, tag and filter | Living reference |

**Current status of the newer features (verified).**
- **Theme blocks** are live and are the recommended way to build composable pieces.
- **LiquidDoc / `{% doc %}`** is live. Shopify's changelog calls it "a new way to add structured documentation directly within your Liquid snippets, and blocks."\[20\] Shopify Developers announced it on X on June 9, 2025, together with "static params for static blocks" and OKLCH colour support.\[21\]
- **`{% stylesheet %}` / `{% javascript %}`** are supported. Shopify "subsets this CSS so that each page only loads the styles from files in its render tree." JavaScript is bundled and "loaded through a `<script>` tag with the defer attribute," with each file's code wrapped in its own function so errors stay contained.\[19\] Skeleton v2 RC drops these tags,\[1\] but v1 and the docs still support them.\[1\]
- **Prettier plugin**: the standalone repo is archived (June 20, 2024). The plugin now lives in Shopify/theme-tools. With Prettier 3+, you must declare `"plugins": ["@shopify/prettier-plugin-liquid"]`.\[22\]\[23\]

**How to study (in order).**
1. Read Architecture, then Sections, Blocks and Snippets, in one sitting.
2. Read the **Theme Store requirements** now, not in Phase 2. They affect your architecture and your fonts.
3. Read Dawn's `main-product.liquid` to see the product-block pattern, which the requirements page itself points to.\[3\] Then close it and write your own version.

**Checklist.**
- [ ] All pages above bookmarked
- [ ] Theme Store requirements read before you design any component
- [ ] Every snippet and block starts with a `{% doc %}` block

---

## Stage 3 — Development workflow

**What.** Linting, formatting, branching, GitHub sync, preview sharing, and protection for the live theme.

**Why.** One wrong push can overwrite a live storefront and the merchant's customisations. A strict workflow makes that mistake almost impossible.

**Key terms.**
- *Live (published) theme*: the one shoppers see.
- *Unpublished theme*: sits in the theme library, hidden from shoppers.
- *Theme editor*: the no-code customiser merchants use.
- *`settings_data.json`*: stores the merchant's editor choices.

**How.**
1. **Run Theme Check all the time.** The VS Code extension checks on open, change and save.\[24\] Run `shopify theme check` before every commit. Consider a pre-commit hook or a CI step.
2. **Format with Prettier.** Install `prettier` and `@shopify/prettier-plugin-liquid` locally as devDependencies. A global install won't work with the extension. Turn on format-on-save.\[25\]
3. **Branch simply.** Use `main` for release-ready code, `develop` for integration, and `feature/*` for features. Tag releases with semantic versions (`1.0.0`). The Theme Store later requires "X.Y.Z" versions and release notes.\[4\]
4. **Use the GitHub integration carefully.** It syncs both ways. Commits to a connected branch deploy to that theme. Edits in the admin or theme editor are "added as a commit to the connected branch." The branch must match the theme folder structure. "GitHub outside collaborators can't connect branches."\[26\] Connect a **`release` branch to an unpublished theme** first. Connect to the live theme only after the theme is stable. If someone edits in the theme editor, pull or merge before you push. *Community sources:* a Shopify Community thread ("Connecting Github theme to Shopify doesn't load in") says "Maximum theme size is 50MB," and users there report branch connections failing with a "50MB" error. The Pointsource Marketing blog (undated) says the same. This limit is not in the official docs, so treat it as community-sourced.
5. **Set up CLI environments** in `shopify.theme.toml`, so each command names its target explicitly:
   ```toml
   [environments.dev]
   store = "oroskin-dev"

   [environments.bench]
   store = "oroskin-bench"

   [environments.showcase]
   store = "oroskin-showcase"
   theme = "123456789012"   # an UNPUBLISHED theme ID
   ```
   Then run `shopify theme push -e showcase`. *Unsure:* I confirmed that environments exist and use `--environment`.\[13\] Check the exact key names against shopify.dev/docs/storefronts/themes/tools/cli/environments.
6. **Share previews safely.**
   - `shopify theme dev` gives you a password-protected preview of your development theme.\[13\]
   - For a link that still works after you log out, run `shopify theme push --unpublished` (or `shopify theme share`) and share the preview from the admin.\[13\]
   - For Lighthouse, the admin "eye" preview gives "a shopifypreview.com URL that performance testing tools like Lighthouse can access without a store password."\[11\]
7. **Guard the live theme.**
   - Never type `--live`, `--allow-live` or `--publish`. The `push` docs list `--publish` as "Publish as the live theme after uploading."\[27\]
   - `theme dev` has an explicit flag to "Allow development on a live theme," so it won't touch the live theme by default.\[15\] Keep it that way.
   - Always push to an explicit `--theme <id>` or `--unpublished`. Run `shopify theme info` first to confirm which store you're on.\[13\]
   - Publish only by hand (admin → Themes → Publish), after a review.
   - On the showcase store, add `config/settings_data.json` and `templates/*.json` to the push ignore list once the content is set up. Otherwise a push can wipe editor changes.
   - *Community source (kaspianfuad.com CLI cheat sheet, 2026):* `shopify theme push --strict` blocks the push if Theme Check fails.\[28\] Check it with `shopify theme push --help`.

**Where.**
- CLI theme commands: shopify.dev/docs/api/shopify-cli/theme (`theme-dev`, `theme-push`, `theme-publish`)
- GitHub integration: shopify.dev/docs/storefronts/themes/tools/github
- Prettier plugin: shopify.dev/docs/storefronts/themes/tools/liquid-prettier-plugin; github.com/Shopify/theme-tools

**Checklist.**
- [ ] Theme Check passes with zero errors before every merge
- [ ] Prettier runs on save
- [ ] `shopify.theme.toml` environments exist, and only unpublished IDs are listed
- [ ] No `--live`, `--allow-live` or `--publish` in any script
- [ ] GitHub `release` branch connected to an unpublished theme

---

## Stage 4 — Building it right

**What.** Design tokens, CSS variables, loading assets only where they're used, images, and app blocks.

**Why.** The Theme Store checks every one of these. They also decide your Lighthouse score and how easy the theme is for merchants to edit.

**Key terms.**
- *Design tokens*: named design values such as colours, fonts and spacing.
- *`image_url` / `image_tag`*: Liquid filters that build CDN image URLs and `<img>` tags.
- *App block*: a block (`@app`) that installed apps can insert into your sections.

**How.**
1. **Put tokens in `settings_schema.json`.** Use `type: color` settings. The Theme Store requires "a minimum of 4 colors," and "all background color settings must include a corresponding foreground color setting." Use `type: font_picker` for typography, with a default such as `work_sans_n6`. Load bold, italic and bold-italic variants with `font_modify`. **Custom fonts aren't accepted** for the Theme Store.\[3\] If Oroskin's Figma uses a licensed brand font, you can self-host it for the Phase 1 showcase. For Phase 2, pick the closest font in Shopify's font library.
2. **Output the tokens as CSS variables** once, in a `<style>` block in `layout/theme.liquid` or a snippet. For example: `--color-bg: {{ settings.color_background }};`. Components then use `var(--color-bg)`, so they never read Liquid settings directly.
3. **Load CSS and JS only where they're used.**
   - Put the shared styles every page needs in Skeleton's `critical.css`.\[6\]\[29\]
   - Put component CSS inside that section or block's own `{% stylesheet %}`. Shopify then serves only the CSS for components on the current page.\[19\]
   - Put component JS in `{% javascript %}`, which is deferred automatically, or in a separate `assets/*.js` loaded with `defer` or `type="module"` only in the sections that need it.
   - Don't put Liquid inside these tags. It "can cause syntax errors."\[19\]
4. **Handle images the Shopify way.**
   - Always use `{{ image | image_url: width: 1600 | image_tag: widths: '600, 900, 1200, 1600', sizes: '100vw', alt: image.alt }}`. Shopify's filters generate the `srcset`, width and height (which prevents layout shift) and a CDN URL.\[30\]
   - Support focal points. They are required, and they come from the `image_picker` setting.\[3\]
   - **Never lazy-load the hero.** By default, `image_tag` uses `loading="eager"` for the first three sections and `lazy` for section 4 onward.\[31\]\[32\] Set it explicitly: eager plus `fetchpriority: 'high'` when `section.index == 1`, and lazy when `section.index > 3`. Shopify's doc says `nil` should "fall through to eager." Inside grids, use `forloop.index` so only the first visible cards load eagerly.\[31\]
   - Shopify's performance team found that LCP is "about 3 seconds slower on Shopify sites that lazy load the LCP" (HTTP Archive data, Sept 2022).\[33\] That data is old, but the rule still stands.
5. **Build the product page from blocks.** "Price, vendor, description… should each be individual blocks." Support `@app` blocks in the main product section and the featured product section. Add a **Custom Liquid** block and a **Custom Liquid** section, both with a `liquid` setting.\[3\] These let merchants install review, subscription and upsell apps without touching code.
6. **Build all required features from day one.** Retrofitting them is expensive. The list includes:
   - faceted filtering, predictive search, gift card template (with Apple Wallet and a QR code of at least 120px), unit pricing\[3\]
   - Shop Pay Installments banner, pickup availability, related and complementary products, rich media (3D and video)\[3\]
   - swatches, variant images, multi-level menus, newsletter form\[3\]
   - country and language selectors, Follow on Shop, and `<shopify-account>` in the header on desktop and mobile\[3\]
   - accelerated checkout on product and cart (on by default, with button colours unmodified)\[3\]
7. **Use the `routes` object for URLs.** Write `{{ routes.root_url }}`, never `/`. Put `lang="{{ request.locale.iso_code }}"` on `<html>`. Never parse `content_for_header`.\[3\]
8. **Keep strings in locales** (`locales/en.default.json` and `*.schema.json`). Write setting labels in sentence case and American English, with no ampersands.\[3\]

**Where.**
- Requirements §4–§17: shopify.dev/docs/storefronts/themes/store/requirements
- Never lazy-load LCP: shopify.dev/docs/storefronts/themes/best-practices/performance/never-lazy-load-lcp-image
- App blocks: shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks

**Checklist.**
- [ ] At least 4 colour settings, each background paired with a foreground
- [ ] All fonts use `font_picker` (Theme Store build)
- [ ] Every image goes through `image_url | image_tag` with `widths`, `sizes` and `alt`
- [ ] Hero is eager with `fetchpriority=high`; below-the-fold images are lazy
- [ ] `@app` and Custom Liquid blocks on product and featured-product sections
- [ ] No hard-coded URLs or strings

---

## Stage 5 — Performance

**What.** Speed as users feel it and as Shopify measures it.

**Why.** Speed affects conversion and SEO. Google Search Central's page "Understanding Google Page Experience" says: "Core Web Vitals are used by our ranking systems." The same page warns that good scores don't "guarantee that your pages will rank at the top of Google Search results." Performance is also Stage 2 of Theme Store review.

**Key terms.**
- *LCP* (Largest Contentful Paint): when the biggest visible element finishes loading.
- *INP* (Interaction to Next Paint): how fast the page responds to input.
- *CLS* (Cumulative Layout Shift): how much the layout jumps while loading.
- *RUM*: real-user monitoring.

**How Shopify measures it.**
- **Theme Store:** "a minimum average Lighthouse performance score of 60 across the theme's product, collection, and home page, for both desktop and mobile," tested on a benchmark dataset.\[34\]\[35\] Sections "must contain actual images and content."\[3\]
- **Live stores:** the **Web Performance Dashboard** in the admin shows real-user Core Web Vitals. It was introduced on Jan 31, 2024, and replaced the old Speed Score.\[36\] Shopify notes that RUM data is "insufficient… on a new store, a low-traffic store, or a development store."\[11\] Expect it to stay empty until you have real traffic.

**How.**
1. Set your own budget above the minimum. Aim for Lighthouse mobile ≥ 80 on the benchmark store, LCP ≤ 2.5 s, INP ≤ 200 ms and CLS ≤ 0.1. Google Search Central ("Understanding Core Web Vitals and Google search results," updated 2025-12-10) says: "strive to have LCP occur within the first 2.5 seconds of the page starting to load" and "strive to have an INP of less than 200 milliseconds." The 60 score is only the pass mark.
2. Add the **Shopify Lighthouse CI GitHub Action** (`shopify/lighthouse-ci-action@v1`). It uploads your theme to the benchmark store and scores it on every push. The default `lhci_min_score_performance` is 0.6.\[34\]\[37\] Raise it to 0.8. It now authenticates with a Dev Dashboard app, using the secrets `SHOP_CLIENT_ID`, `SHOP_CLIENT_SECRET` and `SHOP_STORE`.\[12\]
3. Keep Liquid fast. Shopify says Liquid render time "directly determines Time to First Byte."\[30\] Avoid deeply nested loops over large collections.
4. Animate only `transform` and `opacity`, which you already do. Shopify's performance guide recommends preferring "transform/opacity animations over layout-property animations."\[30\]
5. Test manually with Chrome DevTools, PageSpeed Insights and WebPageTest against the shopifypreview.com URL.

**Where.** shopify.dev/docs/storefronts/themes/best-practices/performance (plus `/testing-for-performance`); shopify.dev/docs/storefronts/themes/tools/lighthouse-ci; github.com/Shopify/lighthouse-ci-action

**Checklist.**
- [ ] Benchmark store loaded with the official CSV
- [ ] Lighthouse CI on pull requests, threshold ≥ 0.8
- [ ] Home, product and collection pages average ≥ 60 on desktop and mobile (target 80+)
- [ ] No layout shift from fonts or images

---

## Stage 6 — Accessibility

**What.** Making the store usable for everyone, including keyboard and screen-reader users.

**Why.** It is required in Theme Store Stage 2 (Lighthouse ≥ 90) and Stage 3 (the manual rules).\[10\]\[35\]

**The rules Shopify checks (requirements §12).**
- "All parts of a page must be keyboard accessible, including dropdown navigation."\[3\]
- Focusable elements must have a visible focus state.\[3\]
- Focus order must match DOM order ("top-bottom, left-right").\[3\]
- Every image needs `alt`. Use `image.alt` or `image_tag: alt:`.\[3\]
- Form inputs need unique IDs and `<label for>` that matches.\[3\]
- The HTML must be valid.\[3\]
- Contrast must be 4.5:1 for body text, and 3:1 for text larger than 18pt and for non-text elements.\[3\]
- Touch targets must be at least 24×24 CSS pixels.\[3\]
- Headings h1–h6 must look different from each other.\[3\]

**How to test.**
1. Run Lighthouse and axe DevTools on every template.
2. Go through the whole purchase flow using only the keyboard: menu → product → variant → add to cart → cart → checkout.
3. Run a screen reader (VoiceOver or NVDA) on the header, product form and cart drawer.
4. **Disable JavaScript** in DevTools. Shopify's test guide asks you to "verify that navigation elements and the product form work without JavaScript."\[38\] Your no-JS visibility rule helps here.
5. Turn on "Reduce motion" at the OS level and check that the reveal animations disappear.

**Where.** shopify.dev/docs/storefronts/themes/best-practices/accessibility; requirements §6 and §12; shopify.dev/docs/storefronts/themes/store/test-theme

**Checklist.**
- [ ] Lighthouse accessibility ≥ 90 average
- [ ] Full keyboard purchase path works
- [ ] Focus states visible
- [ ] Menus and product form work without JS
- [ ] Reduced motion respected

---

## Stage 7 — SEO (deep dive)

### 7a. What Shopify does automatically
Shopify's Help Center "SEO overview" (undated, accessed 2026-09-28) says:
- canonical tags are "auto-generated… to prevent duplicate content"\[39\]\[40\]
- "sitemap.xml and robots.txt files are automatically generated"\[39\]\[40\]
- themes automatically generate title tags that include the store name\[41\]
- SSL is on by default\[41\]
- Google usually indexes new or updated content "within 48 to 72 hours"\[39\]

**Hreflang** is automatic too. Shopify "adds hreflang tags to your theme automatically through the content_for_header object."\[42\] These tags exist only for markets that have their own domain, subdomain or subfolder, and they "update automatically." The merchant can turn them off under Online Store → Preferences.\[43\]\[44\]

*Nuance:* the canonical tag is not fully automatic in a custom theme. Your theme has to output it (see 7b). What Shopify supplies is `canonical_url`.

### 7b. What you, the theme developer, must add
1. **Title, meta description and canonical** in `<head>`. The Theme Store requires "the theme SEO metadata code snippet with the title, meta description, and canonical URL."\[3\] Use `page_title` (plus the page number and `shop.name` where appropriate), `page_description` and `canonical_url`.\[45\]
2. **Open Graph and Twitter card tags.** These are required (§13). Use `page_image` for the share image. It is required too, and merchants set it in the admin.\[3\] Include `og:type` (product/article/website), `og:price:amount` and `og:price:currency` on products, and `twitter:card=summary_large_image`.
3. **Structured data (JSON-LD).**
   - **Product:** `<script type="application/ld+json">{{ product | structured_data }}</script>`. Shopify says this outputs "a schema.org Product if they have no variants, and a ProductGroup if they have one or more variants." It also works on `article` (as Article).\[46\]\[47\] The Theme Store requires "Google's rich product snippets."\[3\]
   - **Organization / WebSite** (home page): write these by hand with `shop.name`, `routes.root_url`, the logo from `settings`, and `sameAs` from your social settings. Use the `| json` filter on every value so quotes can't break the JSON.\[48\]
   - **BreadcrumbList** (product, collection, article): write this by hand from the collection context or `request.path`. `structured_data` does not produce it.
   - *Community source (Gist discussion, undated):* the built-in Product output may lack `hasMerchantReturnPolicy` and `shippingDetails`.\[49\]\[50\] Don't hand-write a second Product block, because duplicates confuse Google. Test with Google's Rich Results Test. The requirements page still links to the retired "Structured Data Testing Tool," which is an out-of-date link.\[3\]
4. **Heading order.** Each page gets exactly one `<h1>`: the product title, the collection title, or the hero heading on the home page. Merchants can reorder sections, so make the heading tag a setting or use `section.index` (h1 when index is 1, h2 otherwise).\[51\]
5. **Alt text.** Output `image.alt` everywhere. Fall back to the product title only for product media. Mark decorative images `alt=""`.
6. **robots.txt.liquid.** *Do not include it in the Theme Store version.* The requirements say "Themes must not include a robots.txt.liquid template."\[3\] For the Phase 1 showcase you *may* add one, but Shopify warns that Support "can't help with edits," and the default is "optimal for SEO."\[52\] My recommendation: don't add it unless you have a specific crawling problem.
7. **Hreflang.** Don't write it yourself while Shopify's automatic tags are on. You would only create duplicates. If you ever need custom tags, turn the automatic ones off first. Then "build the tags dynamically from the localization object," and never hard-code handles.\[42\]
8. **Other theme-side SEO.** Use real `<a href>` links for pagination and filters, add `rel="nofollow"` on links to Shopify domains,\[3\] and avoid the `within` filter on product links, because it creates duplicate URLs.\[46\]

### 7c. What the store owner must do at launch
1. **Connect the primary domain** (Settings → Domains) and make it primary. Canonicals, sitemaps and hreflang all follow the primary domain.
2. **Google Search Console.** Verify the domain property and submit `https://www.yourdomain.com/sitemap.xml`. It's an index that links to the product, collection, page and blog sitemaps.\[39\]\[53\]
3. **Google Merchant Center.** *Unverified in official sources during this research:* the usual path is Shopify's "Google & YouTube" sales-channel app, which syncs products to Merchant Center. Confirm this on help.shopify.com before launch.
4. **URL redirects** if Oroskin is moving from another platform. Map every old URL to its new Shopify URL with 301 redirects in the admin's URL redirects tool, or import them by CSV. *Unsure* of the current admin menu path; search help.shopify.com for "URL redirects."
5. Write unique titles and meta descriptions in each product's and collection's "Search engine listing" panel.

**Where.** shopify.dev/docs/storefronts/themes/seo (plus `/metadata` and `/hreflang`); shopify.dev/docs/api/liquid/filters/structured_data; help.shopify.com/en/manual/promoting-marketing/seo/seo-overview; help.shopify.com/en/manual/markets/seo

**Checklist.**
- [ ] title, description, canonical, OG and Twitter tags in `<head>`
- [ ] Product JSON-LD via `structured_data`; Organization and BreadcrumbList written by hand; Rich Results Test passes
- [ ] One `<h1>` per page
- [ ] No `robots.txt.liquid` in the Theme Store zip
- [ ] No hand-written hreflang
- [ ] Search Console verified and sitemap submitted; redirects imported

---

## Stage 8 — Going live (Phase 1 showcase)

**What.** Put the Oroskin theme on a real, public store.

**Why.** A password-protected dev store can't serve as a public showcase. Dev stores "can't remove the password page," "can't process real transactions," and "can't be converted to production stores."\[2\]

**How.**
1. **Choose the store type.** You have two options:
   - (a) Create a **client transfer store** in the Dev Dashboard. Build it, then transfer ownership to your agency's own merchant account. The new owner "selects a plan when they receive the transfer."\[54\]
   - (b) Sign up for a regular Shopify store under your agency and pay for it from the start.
   Shopify notes: "You can't directly change the plan of a client transfer store. Transfer the store to your client first."\[54\] Pending transfers "expire after 7 days."\[55\] Shopify Payments and other financial products must be turned off before transfer.\[54\] *Unsure:* whether you can transfer a store to your own agency. Confirm with Partner Support.
2. **Choose a plan.** Basic is enough for a showcase. I could not confirm prices from an official source. *Community source:* PageFly's guide (pagefly.io) says it checked shopify.com/pricing on July 30, 2026. It lists Basic at "$39/month ($29/month billed yearly)" plus "2.9% + 30¢ per online transaction" in the US. Craftshift quotes lower Basic prices ($27/$19), so check shopify.com/pricing yourself before you decide. The plan names used by Shopify's dev-store tools are Basic, Grow, Advanced and Plus.\[2\]
3. **Push the theme as unpublished.** Run `shopify theme push -e showcase --unpublished`, then set up content in the theme editor.
4. **Run the pre-launch checklist:** legal pages (privacy, terms, refund, shipping); a test order in test mode; favicon and social image; working 404, search, empty cart and empty collection pages; Lighthouse on the live preview; a keyboard pass; analytics and consent banner; redirects imported; domain DNS ready.
5. **Connect the domain** (Settings → Domains). Set it as primary and confirm SSL is active.
6. **Publish** in the admin: Themes → the Oroskin theme → Publish. Keep the previous theme as a rollback option.
7. **Remove the password page** (Online Store → Preferences). This only works on a paid plan.
8. **Monitor weeks 1–4:** Search Console coverage and Core Web Vitals; the admin Web Performance Dashboard once traffic arrives; JS errors; checkout conversion; 404s; and the speed cost of every app you install (re-run Lighthouse after each one).

**Checklist.**
- [ ] Store type chosen (not a dev store)
- [ ] Plan chosen
- [ ] Domain connected and set as primary
- [ ] Published by hand
- [ ] Password removed
- [ ] Search Console and sitemap set up
- [ ] 4-week monitoring plan in place

---

## Stage 9 — Theme Store submission (Phase 2)

**What.** Getting the theme listed and sold on themes.shopify.com.

**Why.** It is a large sales channel, but it comes with strict rules and a permanent support duty.

**Current requirements (summary).** The 22 sections of the requirements page cover exclusivity, architectural uniqueness, every §4 feature, the required JSON templates plus `gift_card.liquid`, the Lighthouse averages, browser support (including the Instagram, Facebook and Pinterest in-app browsers), no Sass or minified files, SEO, social, accessibility, settings wording, font picker, colour, responsive images, naming (1–2 words, under 30 characters), versions, demo stores, documentation and support. Uniqueness is judged on structure: "animation or transition tweaks" are listed as cosmetic changes that are "insufficient."\[3\]

**Review process (5 stages, per shopify.dev).**
1. Features and OS 2.0 compatibility\[10\]
2. Lighthouse performance and accessibility\[10\]
3. Technical: pages, functionality, browsers, assets, SEO, accessibility, social\[10\]
4. Design and UX: in-depth feedback, settings, font picker, colour, responsive images\[10\]
5. Pre-launch: exclusivity, naming, demo stores, docs, support\[10\]

You must pass each stage to reach the next one. Rejections arrive by email, and you can reply to discuss them. "If you resubmit your theme without addressing the reasons why it was rejected, then you could be temporarily suspended."\[10\]

**How to submit.**
1. Run `shopify theme package` to build the zip. The validator reads `theme_name` and the presets. **Names can't be changed after upload.**\[56\]
2. Go to Partner Dashboard → Themes → Submit a theme. Upload the zip, accept the Partner Agreement, fill in the listing form, then submit.\[10\]
3. You can upload a new zip until the review starts. The dashboard may take "up to 24 hours" to show the submission.\[10\]
4. Add themes@shopify.com and noreply@shopify.com to your allowed senders.\[10\]

**How long it takes.** **No official timeline is published.** The subagent checked the submit, rejections and updates pages and found none. Shopify says only that updates are reviewed "primarily… during Eastern Standard Time (EST) hours, Monday through Friday."\[4\] Treat any "X business days" figure you see online as unreliable. Some of those figures describe app review, not theme review.

**Common rejection reasons (official, verbatim):**
- missing mandatory features\[57\]
- failing technical requirements\[57\]
- "hasn't been sufficiently tested"\[57\]
- settings and labels that break the style and terminology rules\[57\]
- failing the accessibility or performance benchmarks\[57\]
- an incomplete listing, or grammar mistakes, or missing screenshots\[57\]
- demo stores that don't show the features with realistic use cases\[57\]
- "Demo stores use an outdated version of the theme"\[57\]
- unlicensed content\[57\]
- "code or components that are the intellectual property of another entity"\[57\]

**Demo store and presets.**
- Up to **five presets**, each with its own listing page, industry tag and catalog size. One preset must share the theme's name. Put extra preset templates in `/listings`.\[3\]\[4\]
- Each preset needs at least one demo store that matches its industry.\[3\] For Oroskin, "Beauty" fits.\[56\]
- Demo stores must have the Bogus Gateway or Shopify Payments test mode turned on, with all other checkout options off.\[3\]
- No Lorem Ipsum, no apps (with limited exceptions for free review and translation apps), no text baked into images, and `powered_by_link` left unchanged.\[3\]
- "On install, the theme should match the demo store's look." Demo images don't transfer on install.\[3\]
- Screenshots: desktop 1000×1248 or 2000×2496, mobile 750×1334. The mobile screenshot can't be a copy of the desktop one.\[56\]
- Listing: a tagline of 70 characters or fewer, three highlights, and one shared password for all demo stores.\[56\]

**Documentation.** You need public docs and a public support contact form before launch, both linked from your listing. The docs must match the setting labels and stay up to date.\[3\]

**Pricing.**
- $100–$500 USD, in $10 steps.\[56\]
- No submission fee.\[9\]
- 15% revenue share on gross sales, plus a 2.9% processing fee. Shopify's Help Center states it as "Sell a theme: 85% of revenue, Per sale." The 0%-on-$1M exemption applies to apps only.
- Customisation services can't be bundled into the theme price.\[3\]

**After approval.**
- Reply to support requests "within two business days."\[3\]
- "Fix critical bugs immediately or your theme may be temporarily removed."\[3\]
- Keep providing updates. Wait at least four weeks between updates; new themes may update every two weeks for their first two months.\[4\]
- Use semantic versioning and a `release-notes.md` file (required only after you are published).\[4\]
- Updates that rename or remove settings, sections or blocks become *manual* updates for merchants.\[4\] Avoid breaking changes.
- Shopify's own advice: "Being a Theme Partner is a full-time job."\[3\]

**Where.** shopify.dev/docs/storefronts/themes/store/requirements; …/store/review-process/submit-theme, /listings and /common-theme-rejections; …/store/success/updates; …/store/revenue-share

**Checklist.**
- [ ] Theme name follows the naming rules
- [ ] Every §4 feature and every required template built
- [ ] Lighthouse ≥ 60 and ≥ 90 on the benchmark store
- [ ] Client transfer demo store per preset, running the latest version
- [ ] Docs and contact form live
- [ ] Support process that replies within 2 business days
- [ ] Zip packaged with `shopify theme package`, with no `markets.json` and no `robots.txt.liquid`

---

## One-page timeline

| # | Stage | Main output | Rough effort (my estimate) |
|---|---|---|---|
| 1 | Setup | Requirements read; Partner account, 2 dev stores, CLI, repo, `theme dev` running | 2–3 days |
| 2 | Learn the docs | Bookmarks; one test section, block and snippet with LiquidDoc | 3–5 days |
| 3 | Workflow | Theme Check, Prettier, branches, environments, Lighthouse CI | 1–2 days |
| 4 | Build | Tokens, layout, header/footer groups, all templates, product blocks, required features | 6–12 weeks |
| 5 | Performance | Benchmark ≥ 80 target, LCP hero fixed | Ongoing, plus 1 week of hardening |
| 6 | Accessibility | ≥ 90, keyboard, screen reader and no-JS passes | Ongoing, plus 1 week |
| 7 | SEO | Metadata, OG/Twitter, JSON-LD, headings | 3–5 days |
| 8 | Phase 1 launch | Client transfer or paid store, domain, publish, Search Console, 4-week monitoring | 1 week, then monitoring |
| 9a | Phase 2 prep | Swap fonts to `font_picker`, remove credits, presets, demo stores, docs, support desk | 3–6 weeks |
| 9b | Submit and review | 5-stage review; no official timeline | Unknown; plan for several rounds |
| 9c | After approval | Support within 2 business days; updates at least 4 weeks apart | Permanent |

---

## Common beginner mistakes

1. Building the showcase on a dev store and finding out it can't go live or be transferred.
2. Turning on a feature preview on a store you later need to use as a demo or transfer.
3. Using `--live`, `--allow-live` or `--publish`, or pushing `settings_data.json` over a merchant's changes.
4. Lazy-loading the hero, or hiding it at `opacity:0` until JS runs. Both hurt LCP.
5. Designing around a custom brand font and then finding the Theme Store won't accept it.
6. Copying Dawn snippets "just this once." The requirements forbid derived code, and IP problems are a listed rejection reason.
7. Adding `robots.txt.liquid` or `config/markets.json` to the submission zip.
8. Writing duplicate Product JSON-LD next to `structured_data`, or writing hreflang by hand while the automatic tags are on.
9. Leaving support planning for later. You need replies within two business days from day one.

---

## Glossary (plain English)

- **App block (`@app`)**: a slot where installed apps can insert their own UI into your section.
- **`content_for_header`**: an object that must be output in `<head>`. Shopify injects scripts, the generated CSS and JS, and hreflang through it. Never modify it.
- **Development theme**: a hidden, temporary theme created by `shopify theme dev`. It's deleted after 7 days of inactivity or on logout.\[13\]
- **JSON template**: a template file (such as `product.json`) listing which sections appear and their settings. It is what makes "Sections Everywhere" possible.
- **LiquidDoc / `{% doc %}`**: structured comments that document a snippet's or block's parameters. Tools check them.
- **Online Store 2.0 (OS 2.0)**: the modern theme model with JSON templates, sections everywhere and app blocks.\[58\]
- **Preset**: a pre-set style of your theme (up to 5), each with its own listing and demo.
- **Section group**: lets merchants add and reorder sections in areas like the header and footer.
- **`settings_schema.json` / `settings_data.json`**: the global setting definitions, and the merchant's saved values.
- **`structured_data` filter**: Liquid filter that outputs schema.org JSON-LD for products and articles.\[47\]
- (Partner account, Dev Dashboard, dev store, client transfer store, CLI, section, theme block, snippet, schema, locales, live/unpublished theme, theme editor, LCP/INP/CLS and RUM are defined in each stage's "Key terms.")

---

## Top 10 links to bookmark

1. Theme Store requirements: https://shopify.dev/docs/storefronts/themes/store/requirements
2. Skeleton theme (use `main`): https://github.com/Shopify/skeleton-theme
3. Theme architecture: https://shopify.dev/docs/storefronts/themes/architecture
4. Blocks (theme blocks and app blocks): https://shopify.dev/docs/storefronts/themes/architecture/blocks
5. Liquid reference: https://shopify.dev/docs/api/liquid
6. Shopify CLI theme commands: https://shopify.dev/docs/api/shopify-cli/theme
7. Performance best practices: https://shopify.dev/docs/storefronts/themes/best-practices/performance
8. Testing for performance and Lighthouse CI: https://shopify.dev/docs/storefronts/themes/best-practices/performance/testing-for-performance
9. SEO for themes: https://shopify.dev/docs/storefronts/themes/seo
10. Submitting a theme (review stages): https://shopify.dev/docs/storefronts/themes/store/review-process/submit-theme

---

## Recommendations on your "final" decisions

**Decision 1 — Skeleton as the base: keep it, but pin v1.**
- This is the right call. Skeleton is officially "the only approved codebase."\[3\]
- **Risk:** Skeleton's `rc-v2.0.0` has no sections, no JSON templates and no `{% stylesheet %}`.\[1\] That conflicts with the current Theme Store requirements.
- Record the Skeleton commit you scaffolded from in your README, and don't merge upstream v2 changes.
- Check the requirements page and the shopify.dev changelog every month. If Shopify changes the Theme Store rules to allow block-first themes, reassess then.

**Decision 2 — Dawn is read-only: keep it, and write the rule down.**
- Reading Dawn to learn *patterns* matches what Shopify expects. The requirements page itself says "Refer to Dawn's main product section for an example."\[3\]
- But the rule is "fully original code." "Code or components that are the intellectual property of another entity" is a listed rejection reason.\[3\]\[57\]
- Protect yourself:
  - Never keep Dawn open in a split pane while you write the matching component.
  - Write your own component names and structure. Never mirror Dawn's file or class names.
  - Keep a short "clean-room" note in `/docs` that says Dawn was used only as a reference.
  - Also learn patterns from the Liquid reference and the shopify.dev feature guides (filtering, predictive search, cart), which are neutral sources.
- *Interpretation, not official:* short idioms that the docs themselves print, such as the `section.index` loading pattern, are safe to use. They come from Shopify's documentation, not from Dawn's code.

**Decision 3 — IntersectionObserver + transform/opacity + reduced motion + visible hero + no-JS content: strong. Add these details.**
1. **Gate the hiding CSS twice**, so content is visible by default:
   ```css
   @media (prefers-reduced-motion: no-preference) {
     .js reveal-on-scroll:not([data-revealed]) { opacity: 0; transform: translateY(16px); }
   }
   ```
   Add the `js` class with a one-line inline script in `<head>` (`document.documentElement.classList.add('js')`). If JS fails later, add a timeout fallback that reveals everything.
2. **Never wrap the hero, or any `section.index == 1` content, in the reveal component.** An element at `opacity:0` delays LCP. Also skip the reveal for any element already in the viewport on load. The observer's first callback reports it as intersecting, so reveal it immediately without a transition.
3. **Support the theme editor.** Custom elements run `connectedCallback` again when the editor re-renders a section, which is a real advantage of web components. Still, in `request.design_mode` show all content with no animation, so merchants aren't editing invisible blocks. The requirement: "Changes made in the theme editor must be reflected in the editor preview."\[3\]
4. **Watch for changes to reduced motion at runtime** (`matchMedia(...).addEventListener('change', …)`). Call `unobserve` after an element is revealed, to keep INP and memory low.
5. **Make it a merchant setting.** Add something like "Enable reveal animations on scroll" (sentence case, American English, following the terminology rules). Some merchants will want it off.
6. **Keep expectations right.** Animations are "cosmetic" in Shopify's uniqueness test. Put your originality into the grid, navigation, product-card system and media treatment the Figma design defines.\[3\]

**Two more decisions you haven't listed, but should make now.**
- **Fonts:** decide today how the Figma typography maps to Shopify's font library. For the Theme Store, "custom fonts aren't accepted."\[3\]
- **One codebase or two:** after approval, "themes listed on the Shopify Theme Store can only be distributed through the Shopify Theme Store," and they can't carry designer credits.\[3\] Keep the Phase 1 showcase on the same codebase, with agency credits only in store content, not in theme files. Don't give copies of this theme to clients. *Interpretation:* using it on your own showcase store is not "distribution," but confirm this with the Theme Partner team before you sign any client work based on it.

---

## Caveats

- Most shopify.dev pages show no "last updated" date, so the dates above are my access date (Sept 28, 2026) unless a changelog date is given. Check the requirements page again right before you submit.
- **Conflicts I could not resolve:** demo store type (client transfer store in the requirements vs dev store on the dev-store page), and the CLI demo-data flag name. The revenue-share conflict is resolved: 15% for themes, as confirmed by shopify.dev and the Help Center.
- **Not verified in official sources during this research:** Shopify plan prices (community figures only), the Merchant Center setup path, the admin menu path for URL redirects, the `--strict` push flag, the 50 MB GitHub branch limit (community-sourced only), and whether you can transfer a client transfer store to your own agency account.
- **Official review timeline:** none is published.
- **Effort estimates** in the timeline are my own judgement, not Shopify figures.

## Sources

1. [GitHub - Shopify/skeleton-theme at rc-v2.0.0 · GitHub](https://github.com/Shopify/skeleton-theme/tree/rc-v2.0.0)
2. [Dev stores](https://shopify.dev/docs/apps/build/stores/development-stores)
3. [Theme store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements)
4. [Updating your theme](https://shopify.dev/docs/storefronts/themes/store/success/updates)
5. [skeleton-theme/README.md at main · Shopify/skeleton-theme](https://github.com/Shopify/skeleton-theme/blob/main/README.md)
6. [module based v1.0.0](https://github.com/reza869/module-based-v1.0.0)
7. [The new Dev Dashboard: your command center for building - Shopify developer changelog](https://shopify.dev/changelog/the-new-dev-dashboard)
8. [Dev stores](https://shopify.dev/docs/storefronts/themes/tools/development-stores/transfer-development-stores)
9. [Revenue share for Shopify Theme Store developers](https://shopify.dev/docs/storefronts/themes/store/revenue-share)
10. [Submitting a theme to the Shopify Theme Store](https://shopify.dev/docs/storefronts/themes/store/review-process/submit-theme)
11. [Testing for performance](https://shopify.dev/docs/storefronts/themes/best-practices/performance/testing-for-performance)
12. [Shopify Lighthouse CI GitHub Action](https://shopify.dev/docs/storefronts/themes/tools/lighthouse-ci)
13. [Shopify CLI for themes](https://shopify.dev/docs/storefronts/themes/tools/cli)
14. [Shopify Liquid Prettier Plugin](https://shopify.dev/docs/storefronts/themes/tools/liquid-prettier-plugin)
15. [theme dev](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev)
16. [Blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks)
17. [Snippets](https://shopify.dev/docs/storefronts/themes/architecture/snippets)
18. [LiquidDoc - Shopify.dev](https://shopify.dev/docs/storefronts/themes/tools/liquid-doc.md)
19. [JavaScript and stylesheet tags](https://shopify.dev/docs/storefronts/themes/best-practices/javascript-and-stylesheet-tags)
20. [LiquidDoc for snippets and blocks - Shopify developer changelog](https://shopify.dev/changelog/liquiddoc-for-snippets-and-blocks)
21. [Shopify Developers on X: "3 LIQUID UPDATES TO POWER YOUR STACK Themes are getting even more composable: 📂 LiquidDoc Make your theme snippets error-proof: • Declare interfaces on snippets • Get refined code completions 🧊 Static params for static blocks Configure your blocks beyond the schema tag: •" / X](https://x.com/ShopifyDevs/status/1932105653796909304)
22. [GitHub - Shopify/prettier-plugin-liquid: Prettier Liquid/HTML plugin · GitHub](https://github.com/Shopify/prettier-plugin-liquid)
23. [Not respecting prettier config · Issue #192 · Shopify/prettier-plugin-liquid](https://github.com/Shopify/prettier-plugin-liquid/issues/192)
24. [GitHub - Shopify/theme-check-vscode: Official Shopify Liquid VS Code extension · GitHub](https://github.com/Shopify/theme-check-vscode)
25. [Use it in your editor · Shopify/prettier-plugin-liquid Wiki · GitHub](https://github.com/shopify/prettier-plugin-liquid/wiki/Use-it-in-your-editor)
26. [Shopify GitHub integration for themes](https://shopify.dev/docs/storefronts/themes/tools/github)
27. [theme push](https://shopify.dev/docs/api/shopify-cli/theme/theme-push)
28. [Shopify CLI Cheat Sheet: theme dev, CI Auth, check and console | Kaspian Fuad](https://kaspianfuad.com/blog/shopify-cli-cheat-sheet/)
29. [GitHub - Shopify/skeleton-theme: A minimal, carefully structured Shopify theme designed to help you quickly get started. Designed with modularity, maintainability, and Shopify's best practices in mind. · GitHub](https://github.com/shopify/skeleton-theme)
30. [Performance best practices for Shopify themes](https://shopify.dev/docs/storefronts/themes/best-practices/performance)
31. [Never lazy-load the LCP image](https://shopify.dev/docs/storefronts/themes/best-practices/performance/never-lazy-load-lcp-image)
32. [Announcing new Liquid features for better web performance](https://performance.shopify.com/blogs/blog/announcing-new-liquid-features-for-better-web-performance)
33. [Optimizing images for performance on Shopify – Performance @ Shopify](https://performance.shopify.com/blogs/blog/optimizing-images-for-performance-on-shopify)
34. [Performance best practices for Shopify themes](https://shopify.dev/docs/storefronts/themes/best-practices/performance?itcat=partner_blog&amp=&itterm=theme_store_success)
35. [How to test themes before submitting to the Shopify Theme Store - Shopify](https://www.shopify.com/partners/blog/test-shopify-theme)
36. [Shopify’s new web performance dashboard with real user insights](https://performance.shopify.com/blogs/blog/web-performance-dashboard)
37. [lighthouse ci action](https://github.com/Shopify/lighthouse-ci-action)
38. [Testing your theme for the Shopify Theme Store](https://shopify.dev/docs/storefronts/themes/store/test-theme)
39. [Shopify Help Center | SEO overview](https://help.shopify.com/en/manual/promoting-marketing/seo/seo-overview)
40. [Shopify Sitemap & Robots.txt SEO Guide 2026 | Technical Setup | Innovatrix Infotech](https://www.innovatrixinfotech.com/blog/shopify-sitemap-robots-txt-seo-2026)
41. [Shopify SEO 2026 — The Catalog-Ready Guide to Ranking a Shopify Store](https://shopifyranked.com/shopify-seo/)
42. [Use hreflang tags in your theme](https://shopify.dev/docs/storefronts/themes/seo/hreflang)
43. [Shopify Help Center | International SEO for markets](https://help.shopify.com/en/manual/markets/seo)
44. [Shopify Help Center | International domains](https://help.shopify.com/en/manual/international/managing-international-domains)
45. [Add SEO metadata to your theme](https://shopify.dev/docs/storefronts/themes/seo/metadata)
46. [theme-liquid-docs/data/filters.json at main · Shopify/theme-liquid-docs](https://github.com/Shopify/theme-liquid-docs/blob/main/data/filters.json)
47. [Liquid filters: structured\_data](https://shopify.dev/docs/api/liquid/filters/structured_data)
48. [Json-Ld code for each product page - Shopify Community](https://community.shopify.com/t/json-ld-code-for-each-product-page/552034/9)
49. [Shopify Schema Markup: How to Implement Structured Data?](https://meetanshi.com/blog/shopify-schema-markup/)
50. [This is the last microdata-schema for our Shopify themes · GitHub](https://gist.github.com/bakura10/75b03f0d92d73581bd8b0df7dc3c2db4)
51. [Every home opener renders the h1, and the first section's images load eagerly · Issue #183 · itsmylife44/shopify-theme-builder](https://github.com/itsmylife44/shopify-theme-builder/issues/183)
52. [Shopify Help Center | Editing robots.txt.liquid](https://help.shopify.com/en/manual/promoting-marketing/seo/editing-robots-txt)
53. [Shopify sitemap: 5 automatic sitemaps and how to audit them](https://lionelz.com/en/blog/shopify-sitemap-seo/)
54. [Client transfer stores](https://shopify.dev/docs/apps/build/dev-dashboard/stores/client-transfer-stores)
55. [Shopify Help Center | Transferring stores to clients](https://help.shopify.com/en/partners/dashboard/managing-stores/hand-off-development-stores)
56. [Theme Store listing page](https://shopify.dev/docs/storefronts/themes/store/review-process/listings)
57. [Common theme rejections](https://shopify.dev/docs/storefronts/themes/store/review-process/common-theme-rejections)
58. [Announcing Online Store 2.0](https://www.shopify.com/partners/blog/narrative-web-performance)
