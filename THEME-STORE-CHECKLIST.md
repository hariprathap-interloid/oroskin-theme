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
- [ ] ❌ Mobile menu *Parked: M2.6, waiting on the mobile design (decision 7).*
- [ ] 🟡 Search link and **predictive search**. *§4* *Search link done (M2.3); predictive search popup drafted in M7.7 (2026-10-27): products, suggestions, collections, pages, articles via the Predictive Search API, no-JS fallback = /search. Tick after browser testing.*
- [ ] 🟡 `<shopify-account>` in the **desktop and mobile** header. Skeleton has desktop only. *§4* *Desktop done (M2.3, LOGIN pill); mobile comes with the mobile header (decision 7).*
- [x] ❌ **Country/currency selector** and **language selector**. *§4* *Done M2.7 (`localization-form` snippet, footer).*
- [x] ❌ Menu defaults: `main-menu` for the header, `footer` for the footer. *§14*
- [x] ❌ **Newsletter signup form** in the footer. *§4* *Done M2.9 (`newsletter-form` snippet).*
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
- [ ] ❌ Localization form snippet, shared by the header and footer selectors *Snippet built (M2.7, footer); the header use comes with the mobile drawer (M2.6, decision 7).*
- [x] ❌ Every snippet starts with LiquidDoc (`{% doc %}`); every piece of text uses locales *Done M3.8: all 15 snippets have `{% doc %}`; new M2/M3 text is in locales.*

---

## M4 Homepage

- [ ] 🟡 The Figma homepage sections. Each one needs a **preset**, real placeholder content and `!= blank` empty states. *§14* *M4 (2026-10-22): 9 of 10 built, each with a preset and placeholders (hero, scrolling showcase, editor's picks, image banner ×2 presets, trending, testimonials, blog stories, feature icons, featured product). New Arrivals deck (M4.6) still open: a Product list stands in on the homepage.*
- [x] ✅ **Featured product** section with `@app` blocks and rich media. *§4, §5* *Done M4.13 (5b79cab): images, video, external video, 3D; `@app` + `@theme` blocks; swatches in M6.*
- [x] ✅ No empty sections in the template. *§6, since Lighthouse tests real content.* *M4.14: every homepage section has content; button links set; New Arrivals = Product list until the deck exists.*

---

## M5 Collection

- [ ] 🟡 Collection title (never truncated), description and image
- [ ] 🟡 Product grid that handles mixed image ratios, using the product card. Includes unit price, sale badge and price range.
- [ ] 🟡 **Faceted filters**: availability, price, type, vendor and variant options. Also on the search page. *§4* *Built M5.4 (collection) + M5.6 (search): `snippets/filter-drawer.liquid` renders whatever Search & Discovery returns (list, boolean, price range, swatches). Tested with availability, price and Size; tick after testing type / vendor on the store.*
- [ ] ❌ **Sort** dropdown
- [ ] ❌ Empty-collection message
- [ ] ✅ Pagination
- [ ] 🟡 Collection list page: `collection.featured_image` and pagination

---

## M6 Product

- [ ] ❌ The product section is built from **blocks**: title, price, vendor, description, variant picker, quantity and buy buttons. *§5*
- [ ] ❌ `@app` blocks and a Custom Liquid block. *§5*
- [ ] 🟡 Variant options shown **separately** (not one combined `<select>`), with **swatches** (`swatch.color` and `swatch.image`). *§7*
- [ ] ❌ **Variant images**: choosing a variant shows its image. *§4*
- [ ] 🟡 All media is viewable, including **3D models, video, YouTube and Vimeo**. *§4*
- [ ] ❌ Price, compare-at, sold-out and unit price update when the variant changes; first available variant selected on load. *§7*
- [ ] ❌ Tax-included note via `cart.taxes_included`
- [ ] 🟡 **Accelerated checkout buttons**, on by default. Skeleton has `payment_button`. *§4*
- [ ] ❌ **Shop Pay Installments** banner. *§4*
- [ ] ❌ **Pickup availability**. *§4*
- [ ] ❌ **Related** and **complementary** product recommendations. *§4*
- [ ] ❌ Gift card recipient fields: email, name, message and send date. *§7*
- [ ] ❌ "Add to cart" text moved to locales. It's currently hard-coded.

---

## M7 Cart

- [ ] 🟡 For each line item: image, title, `options_with_values`, unit price, final price and quantity
- [ ] 🟡 Visible total; tax note; changing a quantity refreshes all line items
- [ ] ❌ Empty-cart message
- [ ] ❌ **Cart notes**, **selling plans (subscriptions)** and **discounts** shown. *§4, §7*
- [ ] ❌ **Accelerated checkout** on the cart, on by default. *§4*
- [ ] ✅ Checkout button submits the cart form

---

## M8 Remaining pages + SEO

- [ ] 🟡 Search: no-results message, products/articles/pages told apart (`object_type`), pagination, filters *Built M5.6 (2026-10-29): product tiles + "Articles and pages" rows, no-results / no-match messages, pagination snippet, filters + sort. Tick after review.*
- [ ] 🟡 Blog: title, article image, **`article.excerpt_or_content`** (Skeleton uses `excerpt`), pagination
- [ ] 🟡 Article: `published_at`, paginated comments, success and error messages
- [ ] ❌ **`templates/page.contact.json`** with a contact form. *§5*
- [ ] 🟡 404 page: clear message, **search bar** and home link
- [ ] 🟡 Password page: logo or shop name, `password_message`, password form
- [ ] 🟡 Gift card page: code, **QR code (at least 120×120px)**, **Apple Wallet**, logo. *§7*
- [ ] ✅ Title, meta description, canonical, Open Graph and Twitter tags. *§11, §13*
- [ ] ✅ Product JSON-LD via `structured_data`. *§11*
- [ ] ❌ Organization and BreadcrumbList JSON-LD. *Not required, but good for SEO.*
- [ ] ✅ No `robots.txt.liquid`. *§11. Keep it that way.*

---

## M9 QA & performance

- [ ] Lighthouse averages across home, collection and product, on **desktop and mobile**: **performance ≥ 60** and **accessibility ≥ 90**. *§6*
- [ ] Keyboard-only purchase path; screen-reader pass; focus order matches the page order. *§12*
- [ ] Valid HTML; contrast 4.5:1 for body text and 3:1 for large text and UI elements. *§12*
- [ ] Every input has a unique `id` and a matching `<label for>`. *§12*
- [ ] Browsers: the latest Safari, Chrome, Firefox, Edge, iOS Safari, Chrome Mobile and Samsung Internet, plus the **Instagram, Facebook and Pinterest in-app browsers**. *§9*
- [ ] No Sass and no minified files of our own. *§10*
- [ ] Setting labels: sentence case, American English, and Shopify's terminology list ("home page", "main menu", "button label"…). *§14*
- [ ] No fake urgency, countdowns, stock counts or "people viewing" features. *§8*

---

## Parked: awaiting design and client confirmation

These are in the Figma but aren't native Shopify features. Don't build them until they're confirmed. Each one gets a **show/hide toggle** setting.

- [ ] Wishlist (heart icons plus the account wishlist). *Needs an app. Not allowed in the Theme Store version (§8), so it must be possible to switch it off.*
- [ ] Custom account pages: overview, details, orders, track order, refills, rewards, preferences. *Shopify hosts customer accounts itself; for now the theme only uses `<shopify-account>`.*
- [ ] Rewards and refills. *Need apps.*
- [ ] Notification bell with a badge. *Needs an app.*
- [ ] Compare products bar (collection page)
- [ ] Countdown timer ("Glow-Up Event"). *Only for real sales; §8 bans fake urgency.*
- [ ] Mobile layouts. *No mobile designs yet; to be decided later.*

---

## M10 Launch (Phase 1) → Phase 2 prep

- [ ] Showcase on a **client transfer store or a paid store**. A dev store can't go live.
- [ ] Phase 2:
  - theme name (1–2 words, under 30 characters)
  - version number and release notes
  - a demo store for each preset
  - public documentation and a support contact form
  - a support process that replies within 2 business days
  - *§18–§22*
