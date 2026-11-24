# Oroskin: Theme Store checklist, by milestone

This checklist lists everything Shopify requires, in the order we build it. Tick items as you finish them.

- **Source:** [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements), fetched 2026-09-28. The § numbers below refer to sections of that page. Re-check the page before you submit.
- **Scope decision:** every Theme Store–required feature is built during Phase 1, inside its milestone. Oroskin adds no extra features, only design.
- **Status key**, meaning what the Skeleton scaffold already has: ✅ done · 🟡 partial · ❌ missing

> ⚠️ **Uniqueness (§2).** Shopify rejects themes that are only "cosmetic changes", and it counts animations as cosmetic. To be approved, the theme has to feel different in its **layout and structure**: the grid, navigation, product cards and how media is shown. Phase 1 doesn't depend on this, but keep it in mind when you read the Figma design.

---

## M1 Foundation (start here)

Why first: every later section reads these settings, CSS variables and base styles. If they change later, you have to rework everything.

### Global settings (`config/settings_schema.json`)
- [x] ❌ Rename `theme_info` to Oroskin, with a version and documentation/support URLs. *Why: required (§14), and it's what merchants see.* *Done 2026-10-08 (`8cada3a`); the documentation URL is a placeholder until the docs exist (after 22 Oct).*
- [x] 🟡 **At least 4 colour settings**, each background paired with a foreground (text) colour. Skeleton has 2. *§16* *Done: `color_scheme_group` with 10 slots and 5 schemes (`50e7f8d`, `e99f4b9`).*
- [x] 🟡 All fonts use `font_picker`, with a default from Shopify's font library. **No custom fonts.** *§15. Decided: two font pickers, heading font (default `newsreader_n4`, replacing Canela) and body font (default `plus_jakarta_sans_n4`, replacing Satoshi).*
- [x] ❌ Favicon setting. *§14*
- [x] ❌ Logo setting that works with wide, square and tall logos. *§14* *Setting done (`13dc0aa`); rendering in the header is M2.*
- [x] ❌ Social media link settings. Leave the placeholders empty. *§13* *Done: 6 empty `url` settings; icons rendered in M2.*
- [x] ❌ "Enable animations" setting. *Our own decision.*

### CSS variables and base styles
- [x] 🟡 Figma tokens (colours, type scale, spacing, radius) output once as `:root` variables in `snippets/css-variables.liquid`
- [x] ✅ Bold, italic and bold-italic font variants loaded through `font_modify`. *§15*
- [x] ❌ Rich-text styles for h1–h6, blockquote, ul and ol. **Each heading level must look different.** *§8, §12*
- [x] ❌ Visible focus style on every link, button and input. *§12, for keyboard users.*
- [x] ❌ Touch targets of at least 24×24px. *§12* *Buttons 50px and text buttons 24px; check header/footer icons in M2.*
- [x] ❌ Consistent button, link and form styles. *§3*

### Images
- [x] 🟡 `snippets/image.liquid`: add `widths`, `sizes`, the `alt` text, and **eager loading + `fetchpriority="high"` for the hero, lazy loading below the fold**. Support focal points. *§4, §17. Lazy-loading the hero slows the page's main paint (LCP).*

### Animation system
- [x] ❌ A `<animate-on-scroll>` web component: IntersectionObserver with `opacity` and `transform` only
- [x] ❌ Content is hidden only when both the `.js` class and `prefers-reduced-motion: no-preference` apply. It stays visible without JavaScript.
- [x] ❌ Never animate the hero or first-section content
- [x] ❌ Animations are off inside the theme editor (`request.design_mode`). *§14: editor changes must show in the preview.*

### Clean-up and layout rules
- [x] ❌ Delete `sections/hello-world.liquid` and use a real section in `templates/index.json`. *It contains hard-coded text.*
- [x] ✅ `<html lang="{{ request.locale.iso_code }}">`; `content_for_header` left untouched. *§7*
- [x] ✅ `routes` used for URLs. Keep doing this; never hard-code `/`. *§7*

---

## M2 Header & footer

- [x] ✅ Header and footer are rendered through section groups. *§5*
- [x] ❌ Logo, falling back to `shop.name` *Done M2.1: image / text logo / shop name.*
- [x] ❌ **Multi-level dropdown menu**, fully keyboard accessible. *§4, §12* *Done M2.2: `<details>` mega menu, Escape/outside click; keyboard-tested M2.11.*
- [x] ❌ Mobile menu *Done: `snippets/header-drawer.liquid` (menu button below phones / 990 / 1200px, setting `menu_button_breakpoint`), reviewed 2026-11-12 → 11-14.*
- [x] 🟡 Search link and **predictive search**. *§4* *Search link done (M2.3); predictive search popup committed in 25dff98 (`snippets/search-popup.liquid` + `sections/predictive-search.liquid`): products, suggestions, collections, pages, articles via the Predictive Search API, no-JS fallback = /search. Browser-tested 2026-11-05: open, starting groups, typing, no results, Enter, recent searches, keyboard + Escape, outside click.*
- [x] 🟡 Account link in the **desktop and mobile** header. *§4* *Desktop: our own `<account-menu>` (2026-11-05, decision 6); signed out = LOGIN link. Phones: the drawer has the LOGIN button, or signed in the account card (Hi name, email, the Customer account menu links, Sign out).*
- [x] ❌ **Country/currency selector** and **language selector**. *§4* *Done M2.7 (`localization-form` snippet, footer).*
- [x] ❌ Menu defaults: `main-menu` for the header, `footer` for the footer. *§14*
- [x] ❌ **Newsletter signup form** in the footer. *§4* *Done M2.9 (`newsletter-form` snippet). Also a "Newsletter" section for any page (`sections/newsletter.liquid`, 2026-11-24; same snippet).*
- [x] ❌ Social media icons. *§13* *Done M2.10 (`social-icons` snippet, 7 networks incl. WhatsApp).*
- [ ] 🟡 **Follow on Shop** button (`login_button` filter, brand colours unchanged). *§4* *Built M2.10 (shows when `shop.features.follow_on_shop?`); not available on the dev store, so verify on a store with Shop Pay before submission.*
- [x] ✅ Payment icons via `shop.enabled_payment_types`. *§7* *Labelled list (M2.10).*
- [x] ✅ `powered_by_link` present *Restored after the copyright (M2.10).*
- [x] ❌ `rel="nofollow"` on links to Shopify domains. *§8* *`powered_by_link` carries it; no other Shopify-domain links.*
- [x] ❌ **Skip link** (visible on focus) + `<main id="MainContent" tabindex="-1">` landmark. *Shopify accessibility best practices, "Global"* (added in M2.11)
- [x] ❌ No `autofocus` attributes, no positive `tabindex`. *same source* (added in M2.11)

---

## M3 Shared snippets + theme blocks

- [x] ✅ Text block *Rebuilt M3.1 on the type tokens (+ px custom size).*
- [x] ❌ Heading, button and image blocks (the image block supports focal points) *Done M3.2–M3.4 (+ Group upgraded for rows/columns).*
- [x] ❌ **Custom Liquid block** and **Custom Liquid section**, each with a `liquid` setting. *§5. Lets merchants paste app or embed code.* *Done M3.5.*
- [x] ❌ Product card snippet: full title, price, image, unit price and sale badge *Done M3.7 (`product-card`, badges from the Badge metaobject, `product-badge`).*
- [x] ❌ Price snippet: sale price, compare-at price, "from" price (`price_varies`, `price_min`) and unit price *Done M3.6.*
- [ ] ❌ Localization form snippet, shared by the header and footer selectors *Snippet built (M2.7, footer, reviewed 2026-11-18). The selector in the phone drawer is parked (option B, 2026-11-18): the footer one works on every screen size, so this is not required.*
- [x] ❌ Every snippet starts with LiquidDoc (`{% doc %}`); every piece of text uses locales *Done M3.8: all 15 snippets have `{% doc %}`; new M2/M3 text is in locales.*

---

## M4 Homepage

- [x] 🟡 The Figma homepage sections. Each one needs a **preset**, real placeholder content and `!= blank` empty states. *§14* *All 10 built, each with a preset and placeholders (hero, scrolling showcase, editor's picks, image banner ×2 presets, trending, testimonials, blog stories, feature icons, featured product, New Arrivals deck = `product-deck`, now on `templates/index.json`). Audit 2026-11-05.*
- [x] ✅ **Featured product** section with `@app` blocks and rich media. *§4, §5* *Done M4.13 (5b79cab): images, video, external video, 3D; `@app` + `@theme` blocks; swatches in M6.*
- [x] ✅ No empty sections in the template. *§6, since Lighthouse tests real content.* *M4.14: every homepage section has content; button links set; New Arrivals = Product list until the deck exists.*

---

## M5 Collection

*Audit 2026-11-05: M5 was built and tested on 2026-10-29 (branch `feature/m5-collection`) but never ticked here.*

- [x] 🟡 Collection title (never truncated), description and image *`sections/collection-banner.liquid`.*
- [x] 🟡 Product grid that handles mixed image ratios, using the product card. Includes unit price, sale badge and price range. *Bento / even grid; `product-card` + `price` snippets.*
- [x] 🟡 **Faceted filters**: availability, price, type, vendor and variant options. Also on the search page. *§4* *Built M5.4 (collection) + M5.6 (search): `snippets/filter-drawer.liquid` renders whatever Search & Discovery returns (list, boolean, price range, swatches). Tested with availability, price, Size, Product type and Brand (vendor, with its search box) on 2026-11-05; drawer widened to 384px and given one scrollbar.*
- [x] ❌ **Sort** dropdown *Styled `base-select` in the toolbar (collection + search).*
- [x] ❌ Empty-collection message *Two messages: empty collection (strip + suggestions) and "no filter match" (clear filters).*
- [x] ✅ Pagination *`snippets/pagination.liquid`.*
- [x] 🟡 Collection list page: `collection.featured_image` and pagination *`sections/collections.liquid`: tiles / cards / overlay / bento.*

---

## M6 Product

*Audit 2026-11-05: M6.1–M6.9 built and browser-tested, ticked below.*

- [x] ❌ The product section is built from **blocks**: title, price, vendor, description, variant picker, quantity and buy buttons. *§5* *`product-title`, `product-price`, `product-eyebrow` (type / vendor), `product-description`, `buy-buttons` (picker, quantity stepper, Add to cart, Buy now).*
- [x] ✅ `@app` blocks and a Custom Liquid block. *§5* *`sections/product.liquid` accepts `@theme` + `@app`; `blocks/custom-liquid.liquid` is a theme block, so it can be added there. Also `@app` in `product-panel`, `featured-product`, `product-reviews`.*
- [x] 🟡 Variant options shown **separately** (not one combined `<select>`), with **swatches** (`swatch.color` and `swatch.image`). *§7* *`buy-buttons`: one group per option, swatches from `swatch.color` / `swatch.image`. Retest swatch images with the new catalogue (T6).*
- [x] ❌ **Variant images**: choosing a variant shows its image. *§4* *`variant:change` moves the variant's `featured_media` first in the gallery (`sections/product.liquid`).*
- [ ] 🟡 All media is viewable, including **3D models, video, YouTube and Vimeo**. *§4* *Code handles all four (`product-media`, `product-lightbox`, featured product). **To do: test YouTube, Vimeo and a 3D model on a product (the demo catalogue has none yet).***
- [x] ❌ Price, compare-at, sold-out and unit price update when the variant changes; first available variant selected on load. *§7* *`product-price` swaps the variant's price (from the `price` snippet: compare-at, unit price); Add to cart shows Sold out / Unavailable; `selected_or_first_available_variant`; the plan price follows the selling plan.*
- [x] ❌ Tax-included note via `cart.taxes_included` *Price block and cart summary.*
- [x] 🟡 **Accelerated checkout buttons**, on by default. Skeleton has `payment_button`. *§4* *`show_dynamic_checkout` default true.*
- [x] ❌ **Shop Pay Installments** banner. *§4* *`form | payment_terms` in Buy buttons.*
- [x] ❌ **Pickup availability**. *§4* *`product-pickup` block (`store_availabilities`).*
- [x] ✅ **Related** and **complementary** product recommendations. *§4* (M6.5 complementary: sections/product-pairs.liquid; M6.9 related: sections/product-related.liquid, both via routes.product_recommendations_url)
- [x] ✅ Gift card recipient fields: email, name, message and send date. *§7* (M6.3 snippets/gift-card-recipient.liquid in Buy buttons; 2026-11-04: fields render with Shopify's property names, kept on the cart line, test checkout order #1005 on the dev store. 2026-11-05: gift card email received after fulfilling the line; turn on Settings > Checkout > Automatically fulfill gift cards.)
- [x] ❌ "Add to cart" text moved to locales. *Audit 2026-11-05: "Add to cart" only appears in comments now; every label uses `| t`.*

---

## M7 Cart

*Audit 2026-11-05: M7.1–M7.6 built and tested on 2026-10-27; M7.7 search popup committed in 25dff98 (see M2).*

- [x] 🟡 For each line item: image, title, `options_with_values`, unit price, final price and quantity *`snippets/cart-item.liquid`.*
- [x] 🟡 Visible total; tax note; changing a quantity refreshes all line items
- [x] ❌ Empty-cart message *`cart-empty` strip with buttons.*
- [x] ❌ **Cart notes**, **selling plans (subscriptions)** and **discounts** shown. *§4, §7* *Note in a `<details>` in the summary; `selling_plan_allocation` on the line; line and order discounts + coupon card.*
- [x] ❌ **Accelerated checkout** on the cart, on by default. *§4* *`show_express_checkout` default true.*
- [x] ✅ Checkout button submits the cart form
- [x] ➕ App blocks in the cart (2026-11-05), under the order summary.

---

## M8 Remaining pages + SEO

*Audit 2026-11-05: code for every page exists; the review pass (T2) is a browser check of each one.*

- [x] 🟡 Search: no-results message, products/articles/pages told apart (`object_type`), pagination, filters *Built M5.6 (2026-10-29): product tiles + "Articles and pages" rows, no-results / no-match messages, pagination snippet, filters + sort.*
- [x] 🟡 Blog: title, article image, **`article.excerpt_or_content`** (Skeleton uses `excerpt`), pagination *`sections/blog.liquid` + `article-card` (befbf81).*
- [x] 🟡 Article: `published_at`, paginated comments, success and error messages *`article-hero`, `article-comments` (moderation message, per-field errors). Tested 2026-11-05 on a moderated blog: the "sent" message now also comes from a script back-up (Shopify didn't report `posted_successfully?`).*
- [x] ❌ **`templates/page.contact.json`** with a contact form. *§5* *`contact-form` + channels, locations, map. Contact form posts only on the preview link, not on `theme dev` (502).*
- [x] 🟡 404 page: clear message, **search bar** and home link
- [x] 🟡 Password page: logo or shop name, `password_message`, password form
- [x] ✅ Gift card page: code, **QR code (at least 120×120px)**, **Apple Wallet**, logo. *§7* *Verified 2026-11-05 with the real gift card from order #1005.*
- [x] ✅ Title, meta description, canonical, Open Graph and Twitter tags. *§11, §13* *`snippets/meta-tags.liquid`.*
- [x] ✅ Product JSON-LD via `structured_data`. *§11* *Also FAQPage microdata on the FAQ sections.*
- [ ] ❌ Organization and BreadcrumbList JSON-LD. *Not required, but good for SEO. Optional, do in M9 if time allows.*
- [x] ✅ No `robots.txt.liquid`. *§11. Keep it that way.*

### Pages in the Figma with no template yet (audit 2026-11-05)
- [ ] Shipping (`design/figma/screens/shipping`): the built-in /policies/shipping-policy is styled; a page like Returns is open.
- [ ] Cookies (`screens/cookies`): a banner (Customer Privacy API) or a page? Confirm with the design.
- [ ] Track order (`screens/track-order-1|2`): Shopify hosts the order status; at most a form that leads there.
- [ ] Signed-in home (`after-home-1|2`, `new-arrivals-after-login`) and Sign out (`signout`): check what differs.

---

## M9 QA & performance

- [ ] Lighthouse averages across home, collection and product, on **desktop and mobile**: **performance ≥ 60** and **accessibility ≥ 90**. *§6*
- [ ] Keyboard-only purchase path; screen-reader pass; focus order matches the page order. *§12*
- [ ] Valid HTML; contrast 4.5:1 for body text and 3:1 for large text and UI elements. *§12*
- [ ] Every input has a unique `id` and a matching `<label for>`. *§12* *Audit 2026-11-24 (headless Chrome, 22 page states at 1280 / 390px): no duplicate ids, every field named, 5 fields given ids + `for`, payment icon ids made unique on the product page, filter drawer `autofocus` removed. Open states (filter drawer, search popup, phone menu, lightbox) clean in the second run. Password page audited 2026-11-24: clean (title fixed). Still to audit: gift card (needs a real URL).*
- [ ] Browsers: the latest Safari, Chrome, Firefox, Edge, iOS Safari, Chrome Mobile and Samsung Internet, plus the **Instagram, Facebook and Pinterest in-app browsers**. *§9*
- [x] No Sass and no minified files of our own. *§10* *Audit 2026-11-05: no `.min.*`, `.scss` or `.sass` in `assets/`. Keep it that way.*
- [ ] Setting labels: sentence case, American English, and Shopify's terminology list ("home page", "main menu", "button label"…). *§14*
- [ ] No fake urgency, countdowns, stock counts or "people viewing" features. *§8* *Audit 2026-11-05: `blocks/product-stock.liquid` shows "X pieces left" from the real `inventory_quantity`, only when tracked and low. Re-read §8 before submitting: if real counts are also banned, remove the count from the Theme Store version (keep "In stock").*

---

## Parked: awaiting design and client confirmation

These are in the Figma but aren't native Shopify features. Don't build them until they're confirmed. Each one gets a **show/hide toggle** setting.

- [x] ~~Wishlist, custom account pages, rewards, refills, notification bell~~ **Decided 2026-11-05 (decision 6, "A + C"):** not built in the theme. Accounts are Shopify-hosted and branded; the header has our own `<account-menu>` dropdown. These features come from apps (app embeds, the Apps section, `@app` blocks). Optional later: a browser-only wishlist with a show/hide toggle.
- [ ] Compare products bar (collection page)
- [x] Countdown timer ("Glow-Up Event"). *Built 2026-11-17 (`blocks/countdown.liquid`): counts to a real end date the merchant sets, hides or shows a message at the end (no fake reset). Pause button added 2026-11-24 (WCAG 2.2.2).*
- [x] Mobile layouts. *Done in the section reviews (2026-11-14 → 11-24) from the phone designs in `design/inbox/`; tablets mostly use the phone layout. Real-phone tests are still open per section (CLAUDE.md).*

---

## Theme Store submission: gaps found 2026-11-24

*Decided 2026-11-24 (user): the theme will be submitted to the Theme Store. Requirements, rejection, submit and listing pages read again the same day (no "last updated" date on them). Items below are what the theme or the plan does NOT meet yet.*

### Must fix in the code
- [x] **`<shopify-account>` in the header, desktop AND mobile (§4).** *Done 2026-11-25 (user's choice a): `<shopify-account menu="{customer_account_menu}">` replaces our `<account-menu>` (markup, CSS, script, locale keys `header.account_menu.*` removed). Signed out: our LOGIN pill in the `signed-out-avatar` slot (desktop 152 × 50, tablets 40px tall, phones a 40px round icon, 36px at rest over the hero); signed in: the component's initial with our sizes (`--shopify-account-avatar-size` / `-signed-in-avatar-size`) and glass colours. The part's ~50px minimum is reset; focus ring on the part. The sheet uses the header scheme's colours, the theme fonts, `--radius-md`, top = `--header-space`. On phones the button is always in the header bar (the drawer no longer has the account card, LOGIN or Sign out). Tested on theme dev at 320 / 390 / 820 / 1280: sheet opens (desktop top right, phones a bottom sheet with Sign in with Shop, email, Orders / Profile), Escape closes, keyboard ring. Not tested: signed in (needs a real sign-in), legacy customer accounts.*
- [x] **Setting defaults with demo content (§14: "Default values must not use Lorem Ipsum or demo content").** *Done 2026-11-25 (user chose "all as instructions"): every text default and preset value in 79 section / block files rewritten. Generic store headings kept ("Pairs well with", "Customer reviews"); story text and product claims became instructions for the merchant ("Describe a key benefit of this product."); names → "Customer name" / "Team member name"; numbers no longer read as facts (100, "Describe what this number shows"); places → "City" / "Street address"; dates and offer codes empty; brand name gone; "Figma" / "Oroskin" gone from help texts; British "centre" → "center". Only schema blocks changed (checked); the demo pages keep their saved text, except 404 text + links heading, password heading, search placeholder and the article page's comments / related headings (their templates don't save them). Still in the editor content (clean install item): `header-group.json` announcement ("OroSkin • … • Estd. 2026") and the old copy saved in `templates/*.json`.*
- [x] **Countdown preset date (2026-12-31)** expires. *Done: the Promo banner preset has no end date (hidden on the store, the editor note asks for a date); the date placeholder is `YYYY-MM-DD`. The homepage template still saves 2026-12-31 (clean install item).*
- [x] **Shipped templates and `settings_data.json` = the clean install state:** *Done 2026-11-25. Demo content backed up first: the QA theme's editor files pulled to `d:\shopify-oroskin\custom-built-new-theme-oroskin\oroskin-demo-content\` (outside the repo and the zip; the demo store is built from it). A script rewrote every saved setting by its schema type (section, theme block, local and nested blocks): text = the section preset's value for the same block in the same place, else the setting default, else any preset value for that block type, else empty (dates, offer codes, phone numbers, the countdown date stay empty on purpose); collections → `all` (Dawn's convention); products, product lists, blogs, articles, pages, images, videos and `shopify://` links removed (links to `collections/all` kept); menus other than main-menu / footer / customer-account-main-menu removed; selects, checkboxes, ranges, colors and color schemes kept (the look). `settings_data.json`: logo, favicon, logo text and social `#` links removed, the settings moved into the preset `OroSkin` (`current: "OroSkin"`). Checked on theme dev: 16 pages answer, no Liquid error, every template renders all its sections (empty only: Blog stories with no blog, "You might love" while the bag has items); `shopify theme package` zip: 312 files, `shopify://` only to collections/all, no dev-store handles, no markets.json / robots.txt.liquid. The CLI also packs `AGENTS.md` (Skeleton's generic file; `.shopifyignore` does not affect `theme package`). Still saved: Highlight color `#c8a24b` in several sections (waits for the design team).* Earlier wording: no demo collection handles (skincare, makeup, editors-picks), no demo metafields, no `shopify://` file URLs (support tip), but the same look as the demo store (§20: "On install, the theme should match the demo store's look").
- [x] **Setting labels audit (§14):** *Done 2026-11-25 against the §14 text style + terminology tables (re-read the same day): 1,889 editor texts scanned. Fixed: British spelling (Centred / Centre / grey → Centered / Center / gray, 11), "title" → "heading" for setting labels (Title, Card title, Support title, Video title…; Shopify's own "product title" / "page title" kept), "slider" → "Carousel" / "comparison line", "social" → "social media", "sign-up" → "signup", "Across / Down" → "Horizontal / Vertical position", image sizes in Shopify's format ("120 x 120px recommended", ".png" / ".svg" / ".webp"), "1200 px" → "1200px", every "as in the design" / "Figma" / demo reference removed from help texts, "Navigation" (admin path) → "Content > Menus". Kept on purpose: "Search & Discovery" (Shopify's app name, has "&"), "Custom Liquid" / "Shop Pay Installments" (proper nouns), numbered image labels "Photo 1–8" / "Card 1 (top left)" (they match the [image_N] tokens and positions; the rule is about option and section names), "Move left or right" (plain language), "Hide on phones" (checkbox meaning). No questions, no unused keys.*
- [ ] **Presets (settings_data `presets`):** at least one preset named like the theme; each further preset needs its own demo store + listing. Decide: 1 preset ("Beauty") to start.
- [ ] **`theme_info`:** name (1–2 words, < 30 characters, not changeable after upload, not a company name), version, documentation + support URLs. `theme_author` / support email: the partner's public ones.
- [ ] **Cart coupon field:** §8 lists "cart-level discount codes" among app-like features that need API access. Ours uses the Cart AJAX API `discount` field (no app). Confirm it is allowed (Shopify's own themes have it) or ask.
- [ ] **Comments without moderation (§7)** must work: test on an unmoderated blog.
- [ ] **Theme features that read custom metafields** (`custom.badges` + Badge metaobject, `custom.pill_image`, `custom.subtitle`, `custom.short_videos`): only standard `metaobject_type` in settings (we have none: checked), but a merchant has no such metafields. Document them, and make sure nothing looks broken without them.

### Must have outside the code
- [ ] **Rights (§3, §20, rejections "unlicensed content" / "another entity's IP"):** the Figma design (who owns it: the client?), the brand name "Oroskin", and the demo product images (AI-generated PNGs: the rules don't mention AI images; check the generator's licence). Without written rights: new name, own or licensed images.
- [ ] **Exclusivity (§1):** a Theme Store theme can't be distributed elsewhere. If the client store (Phase 1) also uses it, check this with Shopify / the client first.
- [ ] **Uniqueness (§2):** a short written case for the review notes (Product panels accordion, Product deck fan, Scrolling showcase, bento grid, pinned product tabs…). "Animation or transition tweaks" don't count.
- [ ] **Demo store per preset:** a *client transfer store* from the Dev Dashboard (a dev store can't be used), Beauty industry, realistic catalogue (a sale product, a sold-out variant, a multi-variant product, a gift card), Bogus Gateway or Shopify Payments test mode only, no apps except a free reviews / translation app, no text inside images, no Lorem ipsum, latest theme version, one password for all demo stores.
- [ ] **Lighthouse on the benchmark store:** averages over home, collection, product, desktop + mobile: performance ≥ 60, accessibility ≥ 90, with real content in every section.
- [ ] **Browsers (§9):** Safari (2 latest), Chrome (3), Firefox (3), Edge (2), iOS Safari (2), Chrome Mobile (3), Samsung Internet (2), Instagram / Facebook / Pinterest in-app (browse AND buy).
- [ ] **Listing:** desktop screenshot 1000 × 1248 or 2000 × 2496, mobile 750 × 1334 (not a copy of desktop), alt text; tagline ≤ 70 characters; industry Beauty; catalogue size; 3 highlights (image 1600 × 1200, title ≤ 30, text ≤ 140, or a YouTube video ≤ 2 min); metadata description; feature tags; review notes; price $100–$500 in $10 steps.
- [ ] **Public documentation (with an FAQ, labels as in the editor) and a support contact form** (name, email, store URL, description, file upload, auto-reply); a support process that answers in 2 business days; release notes + version.
- [ ] Allow-list themes@shopify.com, theme-submissions@shopify.com and noreply@shopify.com. One theme in review at a time; after a rejection, wait 30 days.
- [ ] Package with `shopify theme package` (no `config/markets.json`, no `robots.txt.liquid`, no designer credits or affiliate links).

---

## M10 Launch (Phase 1) → Phase 2 prep

*List written 2026-11-24 from the roadmap (Part 13, Stages 8–11) and every open item in CLAUDE.md. Who: **D** = developer, **C** = client / design team, **S** = store admin work.*

### 0. Blocker: the store
- [ ] **S** Showcase on a **client transfer store or a paid store**. A dev store can't go live (`oroskin-dev` stays the dev / QA store). Then add the `showcase` environment in `shopify.theme.toml` (unpublished theme id only, `ignore` the editor files).

### 1. Open M9 items to finish first
- [ ] **C** Gold colour: design team approval for `#8a6a1f` (2.1–2.3:1 → 4.86:1). Then set the Highlight color on the QA theme (Scrolling showcase, Cart, any other gold). If refused: put the code defaults back to `#c8a24b` (search popup, Scrolling showcase) and record the contrast fail as a known issue.
- [x] **D** Collection page Lighthouse fixes. *Done 2026-11-25: the first card on page 1 gets `priority` (eager + `fetchpriority="high"`; new `priority` param on `product-card`, passed to the `image` snippet); with the column switch the first 2 cards load eager with the bigger "fewer" view's `sizes` (one download covers both views; the rest stay lazy until the switch sets their sizes); sold-out option text 55% → 65%. Checked on theme dev at 2560px: one download per card photo, the first card is the LCP. (In an `iframe srcdoc` test frame an eager image downloads twice: the frame briefly has the parent window's width while it is created. Not a theme problem: a fresh image in the same frame picks the right file.)* Still to do: Lighthouse on the QA preview link: home, collection, product, cart; mobile + desktop (~1350px wide). Goal ≥ 90 everywhere; Theme Store minimum P ≥ 60, A ≥ 90.
- [ ] **D** Mobile performance (parked): `styles.css` size choice (keep the bundle or move page-only CSS to `assets/`).
- [ ] **D** Gift card page audit on a real URL (order #1005's card).
- [ ] **D + C** Real-device pass with the QA matrix (roadmap Stage 6): iPhone Safari, Android Chrome, iPad, laptop Chrome + Safari; plus Firefox, Edge, Samsung Internet and the Instagram / Facebook / Pinterest in-app browsers (§9). Each section's "Open: real phone test" note in CLAUDE.md belongs here.
- [ ] **D** Screen-reader pass (VoiceOver on iPhone, NVDA on Windows): home → collection → product → cart.
- [ ] **D** Media test: a product with YouTube, Vimeo and a 3D model (the demo catalogue has none).
- [ ] **D** Forms on the preview link (`theme dev` can't POST): contact, newsletter, localization switch, password, article comment.
- [ ] **D** Optional: Organization + BreadcrumbList JSON-LD (M8, not required).

### 2. Store setup (admin)
- [ ] **S** Pages: set each page's **Template** once the theme is published (about, faq, privacy, terms, returns, contact). Until then preview with `?view=`.
- [ ] **S** Settings > Policies: refund, privacy, terms, shipping, **contact information** and **legal notice** (the last two are empty).
- [ ] **S** Menus: `main-menu`, `footer` (nested), `customer_account_menu`, `collection-pills` with "All products" first.
- [ ] **S** Collections: the "Pill image" metafield (`custom.pill_image`) on each collection used in the pills.
- [ ] **S** Settings > Checkout: "Automatically fulfill gift cards" on.
- [ ] **S** Customer accounts: new customer accounts on, branding in Checkout and accounts → Customize.
- [ ] **S** Payments (Shop Pay for Follow on Shop and installments), shipping, taxes, markets / languages; one **test order**.
- [ ] **S** Apps from decision 6 (reviews, wishlist, rewards, back in stock for "Notify me") installed and placed.
- [ ] **S** Analytics and pixels (Customer events).
- [ ] **S** Domain, SSL, remove the store password.

### 3. Content
- [ ] **C** Real logo and product photography (still blocked, see CLAUDE.md).
- [ ] **C** Replace demo content: FAQ answers, team quotes, policy texts, the test text in the demo article ("Dataasd" after the lead), the "Hot" / "New" Badge entries' own colours (clear them for the gold pill).
- [ ] **C** Hero cut-outs uploaded at ~1400px wide (now 360–467px, blurry on large screens).
- [ ] **S** Homepage meta description (Online Store → Preferences) and the social sharing image; SEO titles on key pages.
- [ ] **S** Alt text on images in Content → Files (generated PNGs carry the prompt as metadata); the logo alt text.
- [ ] **S** Collection template: Icon features → Card style; promo card cut-outs.

### 4. Theme files before the final push
- [ ] **D** `theme_info`: documentation and support URLs (the documentation URL is a placeholder).
- [ ] **D** ~~Pull the QA theme's editor files into the repo~~ (changed 2026-11-25: the repo now holds the clean install templates; the QA editor content is the demo content, kept in `oroskin-demo-content/`). Before building the demo store from that folder, delete what comes back from old saves: `heading_level` / `tag` / `link_to_product` on product title blocks, `heading_tag: h2` in `page.returns.json`, the old spec-block order in Product highlights, Product tabs Layout (Stacked vs Tabbed).
- [ ] **D** Theme Check clean; `main` merged and pushed to the final (unpublished) theme.
- [ ] **D** Setting labels: sentence case, American English, Shopify's terms (§14).
- [ ] **D** Re-read §8 (fake urgency): the real low-stock count in `product-stock`.
- [ ] **D** Verify Follow on Shop on the Shop Pay store.

### 5. Launch day (roadmap Stage 10)
- [ ] **C** Written approval of the final preview theme; launch date agreed (not a Friday, not a sale period).
- [ ] **D** Duplicate the live theme as a backup.
- [ ] **S** Publish the approved theme (by hand in the admin, never from the CLI).
- [ ] **D** Smoke test: home → collection → product → add to cart → checkout (test order) → account; mobile and desktop.
- [ ] **D** If something breaks: publish the backup theme.

### 6. After launch (Stage 11)
- [ ] **D** Watch 1–2 weeks: errors, the Web performance report (real-user data), client feedback.
- [ ] **D** Tag the release `v1.0.0`; documentation (sections, metafields, settings) — the docs phase.
- [ ] Phase 2:
  - theme name (1–2 words, under 30 characters)
  - version number and release notes
  - a demo store for each preset
  - public documentation and a support contact form
  - a support process that replies within 2 business days
  - *§18–§22*
