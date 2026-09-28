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
- [ ] ❌ Rename `theme_info` to Oroskin, with a version and documentation/support URLs. *Why: required (§14), and it's what merchants see.*
- [ ] 🟡 **At least 4 colour settings**, each background paired with a foreground (text) colour. Skeleton has 2. *§16*
- [ ] 🟡 All fonts use `font_picker`, with a default from Shopify's font library. **No custom fonts.** *§15. Pick the closest library font to the Figma font now.*
- [ ] ❌ Favicon setting. *§14*
- [ ] ❌ Logo setting that works with wide, square and tall logos. *§14*
- [ ] ❌ Social media link settings. Leave the placeholders empty. *§13*
- [ ] ❌ "Enable animations" setting. *Our own decision.*

### CSS variables and base styles
- [ ] 🟡 Figma tokens (colours, type scale, spacing, radius) output once as `:root` variables in `snippets/css-variables.liquid`
- [ ] ✅ Bold, italic and bold-italic font variants loaded through `font_modify`. *§15*
- [ ] ❌ Rich-text styles for h1–h6, blockquote, ul and ol. **Each heading level must look different.** *§8, §12*
- [ ] ❌ Visible focus style on every link, button and input. *§12, for keyboard users.*
- [ ] ❌ Touch targets of at least 24×24px. *§12*
- [ ] ❌ Consistent button, link and form styles. *§3*

### Images
- [ ] 🟡 `snippets/image.liquid`: add `widths`, `sizes`, the `alt` text, and **eager loading + `fetchpriority="high"` for the hero, lazy loading below the fold**. Support focal points. *§4, §17. Lazy-loading the hero slows the page's main paint (LCP).*

### Animation system
- [ ] ❌ A `<animate-on-scroll>` web component: IntersectionObserver with `opacity` and `transform` only
- [ ] ❌ Content is hidden only when both the `.js` class and `prefers-reduced-motion: no-preference` apply. It stays visible without JavaScript.
- [ ] ❌ Never animate the hero or first-section content
- [ ] ❌ Animations are off inside the theme editor (`request.design_mode`). *§14: editor changes must show in the preview.*

### Clean-up and layout rules
- [ ] ❌ Delete `sections/hello-world.liquid` and use a real section in `templates/index.json`. *It contains hard-coded text.*
- [ ] ✅ `<html lang="{{ request.locale.iso_code }}">`; `content_for_header` left untouched. *§7*
- [ ] ✅ `routes` used for URLs. Keep doing this; never hard-code `/`. *§7*

---

## M2 Header & footer

- [ ] ✅ Header and footer are rendered through section groups. *§5*
- [ ] ❌ Logo, falling back to `shop.name`
- [ ] ❌ **Multi-level dropdown menu**, fully keyboard accessible. *§4, §12*
- [ ] ❌ Mobile menu
- [ ] ❌ Search link and **predictive search**. *§4*
- [ ] 🟡 `<shopify-account>` in the **desktop and mobile** header. Skeleton has desktop only. *§4*
- [ ] ❌ **Country/currency selector** and **language selector**. *§4*
- [ ] ❌ Menu defaults: `main-menu` for the header, `footer` for the footer. *§14*
- [ ] ❌ **Newsletter signup form** in the footer. *§4*
- [ ] ❌ Social media icons. *§13*
- [ ] ❌ **Follow on Shop** button (`login_button` filter, brand colours unchanged). *§4*
- [ ] ✅ Payment icons via `shop.enabled_payment_types`. *§7*
- [ ] ✅ `powered_by_link` present
- [ ] ❌ `rel="nofollow"` on links to Shopify domains. *§8*

---

## M3 Shared snippets + theme blocks

- [ ] ✅ Text block
- [ ] ❌ Heading, button and image blocks (the image block supports focal points)
- [ ] ❌ **Custom Liquid block** and **Custom Liquid section**, each with a `liquid` setting. *§5. Lets merchants paste app or embed code.*
- [ ] ❌ Product card snippet: full title, price, image, unit price and sale badge
- [ ] ❌ Price snippet: sale price, compare-at price, "from" price (`price_varies`, `price_min`) and unit price
- [ ] ❌ Localization form snippet, shared by the header and footer selectors
- [ ] ❌ Every snippet starts with LiquidDoc (`{% doc %}`); every piece of text uses locales

---

## M4 Homepage

- [ ] ❌ The Figma homepage sections. Each one needs a **preset**, real placeholder content and `!= blank` empty states. *§14*
- [ ] ❌ **Featured product** section with `@app` blocks and rich media. *§4, §5*
- [ ] ❌ No empty sections in the template. *§6, since Lighthouse tests real content.*

---

## M5 Collection

- [ ] 🟡 Collection title (never truncated), description and image
- [ ] 🟡 Product grid that handles mixed image ratios, using the product card. Includes unit price, sale badge and price range.
- [ ] ❌ **Faceted filters**: availability, price, type, vendor and variant options. Also on the search page. *§4*
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

- [ ] 🟡 Search: no-results message, products/articles/pages told apart (`object_type`), pagination, filters
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

## M10 Launch (Phase 1) → Phase 2 prep

- [ ] Showcase on a **client transfer store or a paid store**. A dev store can't go live.
- [ ] Phase 2:
  - theme name (1–2 words, under 30 characters)
  - version number and release notes
  - a demo store for each preset
  - public documentation and a support contact form
  - a support process that replies within 2 business days
  - *§18–§22*
